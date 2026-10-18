# Sweep blocks-2026-10-18-9852879

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** valleys
- **seed base** 9852879 · seeds 9852879
- **blocks** 87 run
- **compute** 10.9 h of simulator time across every cell
- **generated** 2026-10-18T08:31:00+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>101 warnings</summary>

- AD-nomute: role-mix=no-mute: decode_failures 1
- BL-control: protocol=sr: decode_failures 19
- BL-control: slower: 3.94 s per simulated hour against 1.81 over 58 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 45
- DB-hotstore-stress: max-num-nodes=250: decode_failures 3
- DB-warm: warm-num-nodes=0: queue drops 10.4% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 75
- DB-warm: warm-num-nodes=25: queue drops 10.4% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 75
- DB-warm: warm-num-nodes=100: queue drops 10.4% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 75
- DB-warm: warm-num-nodes=2000: queue drops 10.4% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 75
- DG-burst: burst-loss=0.1: decode_failures 2
- DG-burst: burst-loss=0.2: decode_failures 28
- DG-burst: burst-loss=0.3: decode_failures 27
- DG-loss: extra-loss=0.2: decode_failures 1
- DG-loss: extra-loss=0.3: decode_failures 8
- DG-outage: burst-loss=0.1: decode_failures 32
- DG-outage: burst-loss=0.2: decode_failures 22
- DG-outage: burst-loss=0.3: decode_failures 32
- DM-mode: dm-mode=flood-only: decode_failures 12
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 24
- DM-mode: dm-mode=m4-early-flood: decode_failures 22
- DM-mode: slower: 8.66 s per simulated hour against 2.71 over 58 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-mixed: legacy-fraction=0.25: decode_failures 9
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 3
- LD-chatty: broadcast-interval-s=300: decode_failures 31
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 10.4% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 75
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 16.8% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 86
- MS-density: nodes=40: decode_failures 26
- MS-hopscale: nodes=250: decode_failures 1
- MS-hopscale: nodes=500: decode_failures 14
- MS-hopscale: faster: 7.99 s per simulated hour against 17.7 over 58 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-oversubscribed: nodes=500: decode_failures 9
- MS-siting: siting-mix=event: decode_failures 4
- MS-siting: siting-mix=backbone: misdecodes 1
- MS-size: nodes=150: decode_failures 77
- MS-size: slower: 7.3 s per simulated hour against 3.37 over 58 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-stretch: stretch=1.25: decode_failures 3
- MS-stretch: stretch=1.5: decode_failures 15
- MS-topology: topology=corridor: decode_failures 1
- PR-crladder: coding-rate-ladder=False: decode_failures 24
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 6
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 28
- RF-eu-presets: preset=SHORT_FAST: decode_failures 9
- RF-eu-presets: preset=LITE_FAST: decode_failures 1
- RF-noise: noise-profile=periodic: decode_failures 7
- RF-preset: preset=SHORT_FAST: decode_failures 9
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 7
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 3
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 15
- RF-stretch-duct: duct-per-hour=1.0: decode_failures 46
- RF-stretch-duct: slower: 8.91 s per simulated hour against 1.83 over 58 prior run(s) - 4.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-txpower: tx-power=22: decode_failures 17
- RF-txpower: tx-power=17: 3 archives requested, 2 placed - group on the placed count
- SF-bucket-mode: bucket-mode=global: misdecodes 34
- SF-bucket-mode: bucket-mode=time: misdecodes 19
- SF-bucket-mode: bucket-mode=window: misdecodes 19
- SF-bucket-time: time-bucket-s=600: misdecodes 99
- SF-bucket-time: time-bucket-s=1800: misdecodes 19
- SF-bucket-time: time-bucket-s=3600: misdecodes 6
- SF-bucket-time: time-bucket-s=3600: decode_failures 4
- SF-cadence: trigger=interval: misdecodes 10
- SF-cadence: trigger=interval: decode_failures 19
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=aimd: decode_failures 2
- SF-cadence: trigger=bucket+interval: misdecodes 17
- SF-capacity-local: capacity=4: decode_failures 100
- SF-capacity-local: capacity=8: decode_failures 90
- SF-capacity-local: capacity=16: decode_failures 7
- SF-capacity: capacity=4: decode_failures 100
- SF-capacity: capacity=8: decode_failures 90
- SF-capacity: capacity=16: decode_failures 7
- SF-capacity-window: capacity=8: misdecodes 6
- SF-capacity-window: capacity=8: decode_failures 112
- SF-capacity-window: capacity=16: misdecodes 13
- SF-capacity-window: capacity=16: decode_failures 11
- SF-capacity-window: capacity=32: misdecodes 19
- SF-catchup: catch-up-hours=: misdecodes 17
- SF-catchup: catch-up-hours=02-06: decode_failures 40
- SF-catchup: catch-up-hours=00-08: decode_failures 43
- SF-hops-flat: hops-apart=3: decode_failures 19
- SF-hops-flat: hops-apart=4: decode_failures 18
- SF-hops-spread: hops-apart=3: decode_failures 19
- SF-hops-spread: hops-apart=4: decode_failures 18
- SF-place-flat: place=spread: decode_failures 14
- SF-place-spread: place=spread: decode_failures 14
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 1
- SF-replay-order-broadcast: replay-ordering=heard: decode_failures 13
- SF-replay-order: replay-ordering=heard: misdecodes 11
- SF-servers-flat: servers=2: decode_failures 11
- SF-servers-flat: servers=8: misdecodes 1
- SF-servers-spread: servers=2: decode_failures 11
- SF-servers-spread: servers=8: misdecodes 1
- SF-window-size: window-size=8: misdecodes 134
- SF-window-size: window-size=16: misdecodes 57
- SF-window-size: window-size=32: misdecodes 19
- TH-congestion: no-congestion-scaling=True: decode_failures 85

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `RF-stretch-duct` | 8.91 | 1.82 | 4.88x | 58 |
| `DM-mode` | 8.66 | 2.71 | 3.20x | 58 |
| `BL-control` | 3.94 | 1.81 | 2.18x | 58 |
| `MS-size` | 7.3 | 3.37 | 2.16x | 58 |
| `SF-cadence` | 5.98 | 3.4 | 1.76x | 58 |
| `PR-dmmode-cr` | 4.34 | 2.52 | 1.73x | 58 |
| `SF-capacity-window` | 2.6 | 1.59 | 1.64x | 58 |
| `RF-bw500` | 3.16 | 1.95 | 1.63x | 58 |
| `SF-servers-spread` | 3.39 | 2.19 | 1.55x | 58 |
| `SF-replay-order-broadcast` | 2.56 | 1.66 | 1.55x | 58 |
| `SF-bucket-time` | 2.4 | 1.57 | 1.53x | 58 |
| `LD-traceroute-small` | 21.5 | 37.5 | 0.57x | 58 |
| `MS-hopscale` | 7.99 | 17.7 | 0.45x | 58 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.965 | 0.965 | 0.833 → 0.860 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.944 | 0.944 | 0.854 → 0.860 | 1x bytes_on_air | up | 2 |
| `MS-siting` | siting-mix | **text** | 0.091 → 0.972 | 0.881 | 0.089 → 0.970 | 5.4x advert_bytes | up | 4 |
| `RF-preset-turbo` | preset | **held** | 0.116 → 0.965 | 0.849 | 0.039 → 0.856 | 15x sr_bytes | up | 5 |
| `RF-txpower` | tx-power | **held** | 0.117 → 0.965 | 0.848 | 0.051 → 0.856 | 43x sr_bytes | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.087 → 0.906 | 0.819 | 0.084 → 0.791 | 1.4e+02x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **text** | 0.036 → 0.833 | 0.797 | 0.035 → 0.822 | 8x sr_bytes | down | 3 |
| `MS-stretch` | stretch | **held** | 0.195 → 0.965 | 0.770 | 0.100 → 0.856 | 5.2x advert_bytes | down | 4 |
| `RF-bw500` | preset | **held** | 0.247 → 0.939 | 0.692 | 0.104 → 0.772 | 4.1x advert_bytes | up | 3 |
| `RF-eu-presets` | preset | **text** | 0.275 → 0.866 | 0.591 | 0.270 → 0.856 | 2.6x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.275 → 0.866 | 0.591 | 0.270 → 0.856 | 3.3x sr_airtime | up | 3 |
| `MS-hopscale` | nodes | **text** | 0.305 → 0.866 | 0.561 | 0.301 → 0.856 | 7.8x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **text** | 0.305 → 0.748 | 0.443 | 0.302 → 0.740 | 4.4x bytes_on_air | down | 3 |
| `MS-topology` | topology | **held** | 0.584 → 0.992 | 0.408 | 0.536 → 0.933 | 2.2x sr_bytes | down | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.591 → 0.937 | 0.346 | 0.575 → 0.934 | 8.3x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.524 → 0.866 | 0.342 | 0.496 → 0.856 | 1.8x sr_bytes | down | 4 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.418 → 0.752 | 0.334 | 0.405 → 0.718 | 2.5x sr_airtime | up | 2 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.575 → 0.890 | 0.315 | 0.556 → 0.883 | 7.1x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.558 → 0.866 | 0.308 | 0.518 → 0.856 | 1.9x sr_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.607 → 0.861 | 0.254 | 0.314 → 0.511 | 4.6x sr_airtime | up | 3 |
| `MS-density` | nodes | **text** | 0.705 → 0.949 | 0.243 | 0.685 → 0.947 | 4.7x sr_airtime | up | 5 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.721 → 0.940 | 0.219 | 0.694 → 0.933 | 3.5x sr_airtime | down | 2 |
| `RT-hoplimit` | hop-limit | **text** | 0.721 → 0.930 | 0.209 | 0.686 → 0.928 | 2.8x sr_bytes | up | 4 |
| `MS-size` | nodes | **text** | 0.675 → 0.866 | 0.191 | 0.661 → 0.856 | 6.9x sr_bytes | down | 5 |
| `RT-hopspread` | hop-limit | **text** | 0.721 → 0.910 | 0.189 | 0.686 → 0.905 | 2.4x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **held** | 0.783 → 0.967 | 0.184 | 0.672 → 0.856 | 1.2x advert_bytes | down | 4 |
| `DG-loss` | extra-loss | **text** | 0.703 → 0.866 | 0.163 | 0.684 → 0.856 | 1.4x sr_bytes | down | 4 |
| `RT-spread` | hop-spread | **text** | 0.721 → 0.866 | 0.145 | 0.686 → 0.856 | 1.6x sr_bytes | up | 2 |
| `SC-signing` | signature-policy | **text** | 0.722 → 0.866 | 0.144 | 0.722 → 0.856 | 1.3x sr_airtime | down | 3 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.844 → 0.965 | 0.121 | 0.845 → 0.856 | 29x sr_airtime | down | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.810 → 0.913 | 0.103 | 0.794 → 0.908 | 5.3x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.797 → 0.891 | 0.094 | 0.786 → 0.886 | 2.1x sr_airtime | down | 3 |
| `AD-flooding` | role-mix | **text** | 0.833 → 0.924 | 0.091 | 0.822 → 0.920 | 2.2x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.833 → 0.924 | 0.091 | 0.822 → 0.920 | 2.2x bytes_on_air | up | 3 |
| `SF-cadence` | trigger | **held** | 0.878 → 0.965 | 0.087 | 0.819 → 0.856 | 13x advert_bytes | down | 4 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.866 → 0.951 | 0.085 | 0.856 → 0.950 | 2.7x sr_bytes | up | 3 |
| `SF-place-flat` | place | **held** | 0.889 → 0.967 | 0.079 | 0.843 → 0.857 | 3.2x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.889 → 0.967 | 0.079 | 0.843 → 0.857 | 3.2x sr_bytes | up | 6 |
| `DB-hotstore` | max-num-nodes | **text** | 0.814 → 0.891 | 0.077 | 0.806 → 0.886 | 2.2x sr_airtime | up | 4 |
| `SF-capacity-window` | capacity | **held** | 0.889 → 0.961 | 0.072 | 0.841 → 0.849 | 2.3x sr_bytes | up | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.866 → 0.936 | 0.070 | 0.856 → 0.930 | 1.4x bytes_on_air | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.866 → 0.931 | 0.065 | 0.856 → 0.925 | 1.4x sr_bytes | up | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.656 → 0.720 | 0.064 | 0.629 → 0.697 | 1.2x sr_airtime | down | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.803 → 0.866 | 0.063 | 0.787 → 0.856 | 1.5x sr_airtime | down | 4 |
| `SF-catchup` | catch-up-hours | **held** | 0.910 → 0.956 | 0.046 | 0.821 → 0.852 | 9.1x advert_bytes | down | 3 |
| `SF-servers-flat` | servers | **held** | 0.950 → 0.986 | 0.035 | 0.845 → 0.860 | 4.4x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.950 → 0.986 | 0.035 | 0.845 → 0.860 | 4.4x sr_bytes | up | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.866 → 0.899 | 0.033 | 0.856 → 0.893 | 3.2x bytes_on_air | down | 2 |
| `FW-versions` | profile | **text** | 0.866 → 0.898 | 0.032 | 0.856 → 0.896 | 3.4x bytes_on_air | down | 5 |
| `MS-roles-fav` | role-mix | **held** | 0.935 → 0.967 | 0.032 | 0.856 → 0.876 | 1.2x sr_airtime | down | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.908 → 0.939 | 0.031 | 0.814 → 0.817 | 1.2x sr_airtime | up | 2 |
| `MS-roles` | role-mix | **text** | 0.833 → 0.863 | 0.030 | 0.822 → 0.855 | 1.2x bytes_on_air | down | 2 |
| `SF-provide-transport` | provide-transport | **text** | 0.866 → 0.895 | 0.029 | 0.841 → 0.856 | 4.1x sr_airtime | up | 2 |
| `TH-congestion-input` | congestion-input | **text** | 0.520 → 0.549 | 0.028 | 0.508 → 0.537 | 1.4x sr_airtime | up | 2 |
| `FW-firmware` | profile | **text** | 0.866 → 0.893 | 0.027 | 0.856 → 0.889 | 3.4x bytes_on_air | down | 2 |
| `SF-hops-flat` | hops-apart | **held** | 0.944 → 0.967 | 0.024 | 0.854 → 0.860 | 2.1x sr_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.944 → 0.967 | 0.024 | 0.853 → 0.860 | 2.1x sr_bytes | down | 5 |
| `RT-favourites` | favourite-routers | **text** | 0.864 → 0.885 | 0.022 | 0.854 → 0.878 | 1.1x sr_bytes | up | 2 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.950 → 0.971 | 0.021 | 0.842 → 0.862 | 1.1x sr_bytes | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.950 → 0.971 | 0.021 | 0.842 → 0.862 | 1.1x sr_bytes | down | 4 |
| `AD-worst` | role-placement | **text** | 0.724 → 0.745 | 0.021 | 0.709 → 0.733 | 1.2x sr_bytes | down | 2 |
| `AD-badrouters` | role-placement | **held** | 0.941 → 0.962 | 0.021 | 0.802 → 0.822 | 1.1x sr_bytes | up | 3 |
| `FW-mixed-26` | legacy-fraction | **held** | 0.963 → 0.983 | 0.021 | 0.856 → 0.871 | 2.2x bytes_on_air | up | 4 |
| `FW-mixed` | legacy-fraction | **held** | 0.965 → 0.983 | 0.019 | 0.856 → 0.865 | 2.1x bytes_on_air | up | 4 |
| `SF-capacity` | capacity | **held** | 0.948 → 0.965 | 0.018 | 0.845 → 0.856 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.948 → 0.965 | 0.018 | 0.845 → 0.856 | 5.3x advert_bytes | up | 5 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.922 → 0.939 | 0.017 | 0.814 → 0.817 | 1.1x sr_bytes | down | 2 |
| `MS-router-late` | router-late-fraction | **text** | 0.866 → 0.883 | 0.017 | 0.856 → 0.876 | 1.3x bytes_on_air | up | 4 |
| `LD-diurnal` | diurnal | **text** | 0.866 → 0.882 | 0.016 | 0.856 → 0.874 | 1.3x sr_bytes | down | 3 |
| `DM-mode` | dm-mode | **held** | 0.908 → 0.923 | 0.015 | 0.802 → 0.814 | 1.2x sr_airtime | down | 3 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.948 → 0.962 | 0.014 | 0.833 → 0.841 | 1.1x sr_airtime | down | 2 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.852 → 0.866 | 0.014 | 0.841 → 0.857 | 5.4x advert_bytes | up | 3 |
| `RT-hopassign` | hop-assign | **text** | 0.866 → 0.878 | 0.012 | 0.856 → 0.871 | 1.3x sr_bytes | up | 2 |
| `SF-window-size` | window-size | **text** | 0.849 → 0.861 | 0.012 | 0.837 → 0.849 | 5.4x advert_bytes | up | 3 |
| `SF-sr-retries` | sr-retries | **held** | 0.955 → 0.967 | 0.012 | 0.861 → 0.864 | 1.2x sr_bytes | up | 4 |
| `SF-servers-allrouters` | servers | **held** | 0.943 → 0.955 | 0.012 | 0.843 → 0.844 | 2.5x sr_bytes | up | 2 |
| `SF-width` | short-id-bits | **held** | 0.965 → 0.975 | 0.010 | 0.850 → 0.859 | 3.1x advert_bytes | up | 4 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.931 → 0.940 | 0.009 | 0.922 → 0.933 | 1.2x sr_airtime | down | 2 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.859 → 0.866 | 0.007 | 0.847 → 0.856 | 3.2x advert_bytes | up | 4 |
| `SF-advert-transport` | advert-transport | **held** | 0.965 → 0.972 | 0.007 | 0.856 → 0.856 | 2.4x sr_airtime | up | 2 |
| `PR-repeats` | extra-repeats | **held** | 0.960 → 0.965 | 0.005 | 0.853 → 0.856 | 1x sr_airtime | down | 2 |
| `SF-resolve` | resolve | **text** | 0.864 → 0.866 | 0.003 | 0.852 → 0.856 | 5.7x advert_bytes | = | 3 |
| `SF-replay-order` | replay-ordering | **text** | 0.864 → 0.866 | 0.002 | 0.853 → 0.856 | 1.1x sr_airtime | down | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.997 → 0.999 | 0.001 | 0.932 → 0.933 | 1x sr_bytes | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.940 → 0.941 | 0.001 | 0.933 → 0.933 | 1.1x sr_airtime | down | 2 |

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
| none | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| sprinkled | 1 | 0.914 | 0.910 | 0.004 | - | - | 0.976 | 0.976 | 0.435 | 1.24x | 19.0/23.7/26.6% | 1.7/5.4% | 3 |
| arms-race | 1 | 0.951 | 0.950 | 0.001 | - | - | 0.980 | 0.980 | 0.760 | 1.09x | 22.2/28.5/30.5% | 1.4/5.2% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario valleys`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 0.1 | 1 | 0.890 | 0.883 | 0.006 | - | - | 0.973 | 0.976 | 0.660 | 1.44x | 16.9/28.1/31.2% | 2.2/5.7% | 3 |
| 0.3 | 1 | 0.931 | 0.925 | 0.006 | - | - | 0.989 | 0.990 | 0.777 | 1.17x | 19.4/26.0/31.1% | 1.7/4.7% | 3 |

### `AD-badrouters` - role-placement  `--scenario valleys`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.833 | 0.822 | 0.011 | - | - | 0.941 | 0.947 | 0.601 | 1.25x | 13.8/24.4/29.3% | 2.1/5.2% | 3 |
| inverse | 1 | 0.820 | 0.802 | 0.018 | - | - | 0.962 | 0.964 | 0.569 | 1.22x | 13.7/19.4/22.7% | 2.2/3.5% | 3 |
| random | 1 | 0.823 | 0.806 | 0.017 | - | - | 0.957 | 0.961 | 0.500 | 1.26x | 14.1/20.5/25.0% | 2.0/5.0% | 3 |

### `AD-flooding` - role-mix  `--scenario valleys`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.833 | 0.822 | 0.011 | - | - | 0.941 | 0.947 | 0.601 | 1.25x | 13.8/24.4/29.3% | 2.1/5.2% | 3 |
| all-routers | 1 | 0.924 | 0.920 | 0.004 | - | - | 0.984 | 0.985 | 0.805 | 2.78x | 28.2/42.3/47.2% | 4.5/5.2% | 3 |

### `AD-nomute` - role-mix  `--scenario valleys`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.833 | 0.822 | 0.011 | - | - | 0.941 | 0.947 | 0.601 | 1.25x | 13.8/24.4/29.3% | 2.1/5.2% | 3 |
| no-mute | 1 | 0.874 | 0.865 | 0.009 | - | - | 0.972 | 0.975 | 0.669 | 1.43x | 15.4/22.9/27.5% | 2.2/5.2% | 3 |
| all-routers | 1 | 0.924 | 0.920 | 0.004 | - | - | 0.984 | 0.985 | 0.805 | 2.78x | 28.2/42.3/47.2% | 4.5/5.2% | 3 |

> role-mix=no-mute: decode_failures 1

### `AD-siting` - siting-mix  `--scenario valleys`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.833 | 0.822 | 0.011 | - | - | 0.941 | 0.947 | 0.601 | 1.25x | 13.8/24.4/29.3% | 2.1/5.2% | 3 |
| local-typical | 1 | 0.668 | 0.659 | 0.009 | - | - | 0.828 | 0.829 | 0.000 | 1.28x | 14.7/25.3/32.7% | 2.1/5.3% | 3 |
| basement-heavy | 1 | 0.036 | 0.035 | 0.001 | - | - | 0.148 | 0.148 | 0.000 | 0.39x | 0.2/4.5/8.2% | 0.2/2.3% | 3 |

### `AD-worst` - role-placement  `--scenario valleys`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.745 | 0.733 | 0.012 | - | - | 0.924 | 0.925 | 0.000 | 2.42x | 13.9/26.5/34.3% | 1.8/5.8% | 3 |
| inverse | 1 | 0.724 | 0.709 | 0.015 | - | - | 0.929 | 0.930 | 0.000 | 2.33x | 13.0/22.3/30.7% | 1.9/3.4% | 3 |

### `BL-control` - protocol  `--scenario valleys`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.860 | 0.860 | 0.000 | - | - | 0 | 0.000 | 0.664 | 1.45x | 15.7/26.6/30.4% | 2.2/5.1% | 3 |
| sr | 1 | 0.871 | 0.854 | 0.018 | - | - | 0.944 | 0.960 | 0.632 | 1.50x | 16.2/27.4/31.3% | 2.3/5.4% | 3 |

> protocol=sr: decode_failures 19

> slower: 3.94 s per simulated hour against 1.81 over 58 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario valleys`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.814 | 0.806 | 0.009 | - | - | 0.912 | 0.915 | 0.618 | 3.44x | 35.6/62.6/67.1% | 5.0/9.8% | 3 |
| 100 | 1 | 0.891 | 0.886 | 0.005 | - | - | 0.956 | 0.957 | 0.650 | 1.81x | 19.1/35.1/38.5% | 2.6/5.3% | 3 |
| 120 | 1 | 0.891 | 0.886 | 0.005 | - | - | 0.956 | 0.957 | 0.650 | 1.81x | 19.1/35.1/38.5% | 2.6/5.3% | 3 |
| 250 | 1 | 0.891 | 0.886 | 0.005 | - | - | 0.956 | 0.957 | 0.650 | 1.81x | 19.1/35.1/38.5% | 2.6/5.3% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario valleys`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.324 | 0.314 | 0.010 | - | - | 0.607 | 0.629 | 0.115 | 11.48x | 39.8/58.7/69.3% | 4.0/11.9% | 3 |
| 120 | 1 | 0.520 | 0.508 | 0.013 | - | - | 0.852 | 0.854 | 0.169 | 4.58x | 16.1/27.8/37.8% | 1.5/6.3% | 3 |
| 250 | 1 | 0.524 | 0.511 | 0.013 | - | - | 0.861 | 0.863 | 0.174 | 4.46x | 15.6/26.3/36.1% | 1.5/6.0% | 3 |

> max-num-nodes=10: decode_failures 45

> max-num-nodes=250: decode_failures 3

### `DB-platform` - platform-mix  `--scenario valleys`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.891 | 0.886 | 0.005 | - | - | 0.956 | 0.957 | 0.650 | 1.81x | 19.1/35.1/38.5% | 2.6/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.891 | 0.886 | 0.005 | - | - | 0.956 | 0.957 | 0.650 | 1.81x | 19.1/35.1/38.5% | 2.6/5.3% | 3 |
| constrained | 1 | 0.797 | 0.786 | 0.011 | - | - | 0.900 | 0.900 | 0.603 | 3.43x | 35.5/62.6/67.1% | 5.0/9.7% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario valleys`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.720 | 0.697 | 0.023 | - | - | 0.869 | 0.911 | 0.466 | 6.02x | 56.8/71.5/76.5% | 4.3/13.6% | 3 |
| 25 | 1 | 0.720 | 0.697 | 0.023 | - | - | 0.869 | 0.911 | 0.466 | 6.02x | 56.8/71.5/76.5% | 4.3/13.6% | 3 |
| 100 | 1 | 0.720 | 0.697 | 0.023 | - | - | 0.869 | 0.911 | 0.466 | 6.02x | 56.8/71.5/76.5% | 4.3/13.6% | 3 |
| 2000 | 1 | 0.720 | 0.697 | 0.023 | - | - | 0.869 | 0.911 | 0.466 | 6.02x | 56.8/71.5/76.5% | 4.3/13.6% | 3 |

> warm-num-nodes=0: queue drops 10.4% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 75

> warm-num-nodes=25: queue drops 10.4% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 75

> warm-num-nodes=100: queue drops 10.4% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 75

> warm-num-nodes=2000: queue drops 10.4% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 75

### `DG-burst` - burst-loss  `--scenario valleys`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 0.1 | 1 | 0.773 | 0.752 | 0.021 | - | - | 0.929 | 0.939 | 0.563 | 1.40x | 15.2/25.8/29.6% | 2.1/4.8% | 3 |
| 0.2 | 1 | 0.652 | 0.621 | 0.031 | - | - | 0.842 | 0.879 | 0.439 | 1.27x | 14.2/24.1/27.7% | 2.0/4.3% | 3 |
| 0.3 | 1 | 0.558 | 0.518 | 0.041 | - | - | 0.779 | 0.824 | 0.341 | 1.16x | 13.0/22.3/25.9% | 1.7/3.8% | 3 |

> burst-loss=0.1: decode_failures 2

> burst-loss=0.2: decode_failures 28

> burst-loss=0.3: decode_failures 27

### `DG-loss` - extra-loss  `--scenario valleys`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 0.1 | 1 | 0.820 | 0.807 | 0.013 | - | - | 0.943 | 0.945 | 0.610 | 1.49x | 16.2/27.3/31.4% | 2.2/5.2% | 3 |
| 0.2 | 1 | 0.772 | 0.757 | 0.015 | - | - | 0.920 | 0.924 | 0.532 | 1.53x | 16.7/28.3/32.5% | 2.3/5.1% | 3 |
| 0.3 | 1 | 0.703 | 0.684 | 0.020 | - | - | 0.865 | 0.882 | 0.454 | 1.51x | 16.6/28.7/32.9% | 2.3/4.9% | 3 |

> extra-loss=0.2: decode_failures 1

> extra-loss=0.3: decode_failures 8

### `DG-outage` - burst-loss  `--scenario valleys`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 0.1 | 1 | 0.738 | 0.720 | 0.019 | - | - | 0.896 | 0.926 | 0.538 | 1.39x | 15.1/25.7/29.3% | 2.1/4.9% | 3 |
| 0.2 | 1 | 0.653 | 0.630 | 0.024 | - | - | 0.824 | 0.911 | 0.361 | 1.30x | 14.4/24.1/27.8% | 2.0/4.9% | 3 |
| 0.3 | 1 | 0.524 | 0.496 | 0.028 | - | - | 0.735 | 0.842 | 0.308 | 1.19x | 13.6/23.4/26.9% | 1.8/4.2% | 3 |

> burst-loss=0.1: decode_failures 32

> burst-loss=0.2: decode_failures 22

> burst-loss=0.3: decode_failures 32

### `DM-mode` - dm-mode  `--scenario valleys`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.802 | 0.802 | 0.000 | - | - | 0.923 | 0.951 | 0.614 | 1.99x | 21.3/36.3/41.3% | 3.0/7.0% | 3 |
| directed-with-late-flood | 1 | 0.814 | 0.814 | 0.000 | - | - | 0.908 | 0.941 | 0.622 | 1.80x | 19.4/33.2/37.9% | 2.7/6.4% | 3 |
| m4-early-flood | 1 | 0.813 | 0.813 | 0.000 | - | - | 0.913 | 0.947 | 0.621 | 1.83x | 19.5/33.5/38.2% | 2.8/6.5% | 3 |

> dm-mode=flood-only: decode_failures 12

> dm-mode=directed-with-late-flood: decode_failures 24

> dm-mode=m4-early-flood: decode_failures 22

> slower: 8.66 s per simulated hour against 2.71 over 58 prior run(s) - 3.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-firmware` - profile  `--scenario valleys`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.893 | 0.889 | 0.004 | - | - | 0.988 | 0.989 | 0.569 | 0.79x | 8.7/11.9/13.4% | 1.3/1.8% | 3 |
| 2.8 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario valleys`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 0.25 | 1 | 0.872 | 0.865 | 0.007 | - | - | 0.965 | 0.972 | 0.608 | 1.30x | 13.6/24.1/27.4% | 2.1/4.9% | 3 |
| 0.5 | 1 | 0.869 | 0.862 | 0.008 | - | - | 0.977 | 0.981 | 0.660 | 1.12x | 12.8/18.0/21.1% | 1.8/4.1% | 3 |
| 0.75 | 1 | 0.868 | 0.864 | 0.003 | - | - | 0.983 | 0.984 | 0.565 | 0.98x | 10.9/15.4/16.4% | 1.6/3.6% | 3 |

> legacy-fraction=0.25: decode_failures 9

### `FW-mixed-26` - legacy-fraction  `--scenario valleys`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 0.25 | 1 | 0.864 | 0.857 | 0.007 | - | - | 0.963 | 0.965 | 0.596 | 1.30x | 13.5/23.7/27.1% | 2.0/4.9% | 3 |
| 0.5 | 1 | 0.877 | 0.871 | 0.006 | - | - | 0.974 | 0.976 | 0.663 | 1.12x | 12.8/18.0/21.4% | 1.8/4.2% | 3 |
| 0.75 | 1 | 0.868 | 0.864 | 0.004 | - | - | 0.983 | 0.984 | 0.583 | 0.96x | 10.9/15.6/16.7% | 1.6/3.6% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario valleys`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.899 | 0.893 | 0.006 | - | - | 0.983 | 0.984 | 0.667 | 0.82x | 8.9/15.6/18.0% | 1.2/3.2% | 3 |
| signing=true | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |

### `FW-versions` - profile  `--scenario valleys`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.883 | 0.880 | 0.004 | - | - | 0.983 | 0.983 | 0.573 | 0.79x | 8.9/13.0/14.6% | 1.3/1.9% | 3 |
| 2.5 | 1 | 0.877 | 0.872 | 0.005 | - | - | 0.978 | 0.978 | 0.540 | 0.81x | 9.1/13.1/14.7% | 1.3/2.0% | 3 |
| 2.6 | 1 | 0.881 | 0.876 | 0.005 | - | - | 0.983 | 0.983 | 0.563 | 0.77x | 8.8/12.9/14.7% | 1.2/1.8% | 3 |
| 2.7 | 1 | 0.898 | 0.896 | 0.003 | - | - | 0.980 | 0.980 | 0.566 | 0.83x | 9.4/16.2/18.6% | 1.3/3.1% | 3 |
| 2.8 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.890 | 0.883 | 0.007 | - | - | 0.978 | 0.979 | 0.698 | 0.99x | 10.5/17.7/20.2% | 1.5/3.5% | 3 |
| 900 | 1 | 0.810 | 0.794 | 0.016 | - | - | 0.933 | 0.939 | 0.614 | 2.34x | 25.1/42.9/48.4% | 3.5/8.3% | 3 |
| 300 | 1 | 0.575 | 0.556 | 0.020 | - | - | 0.735 | 0.803 | 0.398 | 4.71x | 49.1/73.2/79.4% | 7.3/15.6% | 3 |

> broadcast-interval-s=300: decode_failures 31

### `LD-chatty-hops` - broadcast-interval-s  `--scenario valleys`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.937 | 0.934 | 0.003 | - | - | 0.991 | 0.991 | 0.739 | 1.11x | 11.7/18.5/21.3% | 1.7/3.5% | 3 |
| 900 | 1 | 0.875 | 0.866 | 0.009 | - | - | 0.958 | 0.959 | 0.676 | 2.68x | 28.2/45.1/51.2% | 4.1/8.6% | 3 |
| 300 | 1 | 0.591 | 0.575 | 0.016 | - | - | 0.694 | 0.709 | 0.397 | 5.38x | 53.8/74.1/80.1% | 8.7/16.5% | 3 |

> broadcast-interval-s=300: decode_failures 3

### `LD-diurnal` - diurnal  `--scenario valleys`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.882 | 0.874 | 0.008 | - | - | 0.975 | 0.975 | 0.682 | 1.41x | 15.1/25.7/29.4% | 2.1/5.1% | 3 |
| sinusoid | 1 | 0.881 | 0.871 | 0.010 | - | - | 0.981 | 0.981 | 0.673 | 1.34x | 14.5/24.8/28.1% | 2.0/4.8% | 3 |
| commuter | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.810 | 0.794 | 0.016 | - | - | 0.933 | 0.939 | 0.614 | 2.34x | 25.1/42.9/48.4% | 3.5/8.3% | 3 |
| 3600 | 1 | 0.890 | 0.883 | 0.007 | - | - | 0.978 | 0.979 | 0.698 | 0.99x | 10.5/17.7/20.2% | 1.5/3.5% | 3 |
| 10800 | 1 | 0.906 | 0.901 | 0.005 | - | - | 0.984 | 0.985 | 0.687 | 0.69x | 7.4/12.3/14.1% | 1.1/2.5% | 3 |
| 43200 | 1 | 0.913 | 0.908 | 0.005 | - | - | 0.988 | 0.989 | 0.702 | 0.51x | 5.3/9.1/10.2% | 0.8/1.9% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario valleys`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 0.25 | 1 | 0.854 | 0.842 | 0.013 | - | - | 0.961 | 0.962 | 0.640 | 1.56x | 16.7/28.5/32.4% | 2.4/5.5% | 3 |
| 1.0 | 1 | 0.845 | 0.832 | 0.013 | - | - | 0.958 | 0.960 | 0.646 | 1.74x | 18.7/31.9/36.3% | 2.6/6.2% | 3 |
| 4.0 | 1 | 0.803 | 0.787 | 0.015 | - | - | 0.933 | 0.935 | 0.603 | 2.16x | 23.4/40.3/45.9% | 3.3/7.9% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario valleys`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.720 | 0.697 | 0.023 | - | - | 0.869 | 0.911 | 0.466 | 6.02x | 56.8/71.5/76.5% | 4.3/13.6% | 3 |
| 1.0 | 1 | 0.656 | 0.629 | 0.027 | - | - | 0.836 | 0.872 | 0.404 | 6.60x | 60.9/74.0/78.9% | 4.9/14.9% | 3 |

> traceroute-per-hour=0.0: queue drops 10.4% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 75

> traceroute-per-hour=1.0: queue drops 16.8% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 86

### `MS-density` - nodes  `--scenario valleys`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.705 | 0.685 | 0.020 | - | - | 0.887 | 0.947 | 0.000 | 1.28x | 19.6/28.7/32.7% | 3.3/6.8% | 3 |
| 60 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 90 | 1 | 0.915 | 0.909 | 0.006 | - | - | 0.991 | 0.993 | 0.703 | 1.74x | 17.1/28.8/33.4% | 1.7/5.2% | 3 |
| 120 | 1 | 0.940 | 0.933 | 0.007 | - | - | 0.999 | 0.999 | 0.711 | 2.04x | 21.2/29.4/33.3% | 1.4/5.5% | 3 |
| 150 | 1 | 0.949 | 0.947 | 0.002 | - | - | 0.999 | 0.999 | 0.764 | 2.56x | 25.6/36.3/42.6% | 1.3/5.5% | 3 |

> nodes=40: decode_failures 26

### `MS-hopscale` - nodes  `--scenario valleys`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 120 | 1 | 0.747 | 0.740 | 0.007 | - | - | 0.953 | 0.954 | 0.353 | 2.24x | 14.4/23.8/32.1% | 1.5/4.9% | 3 |
| 250 | 1 | 0.510 | 0.498 | 0.012 | - | - | 0.832 | 0.832 | 0.184 | 4.88x | 17.2/29.4/40.3% | 1.7/6.8% | 3 |
| 500 | 1 | 0.305 | 0.301 | 0.004 | - | - | 0.600 | 0.601 | 0.068 | 9.77x | 18.0/29.8/42.2% | 1.6/7.4% | 3 |

> nodes=250: decode_failures 1

> nodes=500: decode_failures 14

> faster: 7.99 s per simulated hour against 17.7 over 58 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-oversubscribed` - nodes  `--scenario valleys`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.748 | 0.740 | 0.008 | - | - | 0.955 | 0.955 | 0.349 | 2.12x | 13.6/22.6/30.4% | 1.5/4.6% | 3 |
| 250 | 1 | 0.520 | 0.508 | 0.013 | - | - | 0.852 | 0.854 | 0.169 | 4.58x | 16.1/27.8/37.8% | 1.5/6.3% | 3 |
| 500 | 1 | 0.305 | 0.302 | 0.004 | - | - | 0.597 | 0.598 | 0.075 | 9.19x | 17.1/28.2/39.4% | 1.5/6.8% | 3 |

> nodes=500: decode_failures 9

### `MS-roles` - role-mix  `--scenario valleys`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.962 | 0.963 | 0.658 | 1.50x | 16.1/27.4/31.2% | 2.3/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.833 | 0.822 | 0.011 | - | - | 0.941 | 0.947 | 0.601 | 1.25x | 13.8/24.4/29.3% | 2.1/5.2% | 3 |

### `MS-roles-fav` - role-mix  `--scenario valleys`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.882 | 0.876 | 0.007 | - | - | 0.967 | 0.970 | 0.687 | 1.53x | 16.5/27.7/31.5% | 2.3/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.864 | 0.856 | 0.007 | - | - | 0.935 | 0.935 | 0.703 | 1.47x | 16.4/28.4/34.1% | 2.6/5.2% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario valleys`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 0.05 | 1 | 0.868 | 0.859 | 0.009 | - | - | 0.963 | 0.964 | 0.647 | 1.63x | 17.5/32.4/36.2% | 2.4/5.3% | 3 |
| 0.1 | 1 | 0.869 | 0.862 | 0.007 | - | - | 0.956 | 0.956 | 0.641 | 1.68x | 17.6/34.6/38.1% | 2.4/5.1% | 3 |
| 0.2 | 1 | 0.883 | 0.876 | 0.007 | - | - | 0.963 | 0.964 | 0.701 | 1.90x | 21.0/39.4/46.0% | 2.6/5.0% | 3 |

### `MS-siting` - siting-mix  `--scenario valleys`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| local-typical | 1 | 0.729 | 0.723 | 0.006 | - | - | 0.867 | 0.868 | 0.000 | 1.44x | 15.4/27.2/33.8% | 2.2/5.6% | 3 |
| event | 1 | 0.091 | 0.089 | 0.002 | - | - | 0.191 | 0.246 | 0.000 | 0.75x | 2.2/7.9/12.7% | 0.8/3.8% | 3 |
| backbone | 1 | 0.972 | 0.970 | 0.003 | - | - | 0.996 | 0.997 | 0.902 | 1.33x | 30.5/40.0/43.0% | 1.8/5.6% | 3 |

> siting-mix=event: decode_failures 4

> siting-mix=backbone: misdecodes 1

### `MS-size` - nodes  `--scenario valleys`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.752 | 0.742 | 0.009 | - | - | 0.881 | 0.881 | 0.323 | 1.60x | 24.6/37.8/41.0% | 3.9/7.4% | 3 |
| 60 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 90 | 1 | 0.832 | 0.827 | 0.006 | - | - | 0.964 | 0.965 | 0.529 | 1.75x | 13.2/23.8/27.5% | 1.6/5.4% | 3 |
| 120 | 1 | 0.747 | 0.740 | 0.007 | - | - | 0.953 | 0.954 | 0.353 | 2.24x | 14.4/23.8/32.1% | 1.5/4.9% | 3 |
| 150 | 1 | 0.675 | 0.661 | 0.014 | - | - | 0.944 | 0.952 | 0.239 | 2.69x | 14.5/23.9/29.3% | 1.5/5.5% | 3 |

> nodes=150: decode_failures 77

> slower: 7.3 s per simulated hour against 3.37 over 58 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-stretch` - stretch  `--scenario valleys`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 1.25 | 1 | 0.603 | 0.585 | 0.018 | - | - | 0.810 | 0.817 | 0.036 | 1.35x | 11.3/19.7/23.2% | 2.0/5.2% | 3 |
| 1.5 | 1 | 0.418 | 0.405 | 0.013 | - | - | 0.570 | 0.698 | 0.102 | 1.24x | 8.4/14.9/20.0% | 1.8/5.0% | 3 |
| 2.0 | 1 | 0.101 | 0.100 | 0.001 | - | - | 0.195 | 0.206 | 0.000 | 0.71x | 2.5/7.7/10.8% | 0.8/3.3% | 3 |

> stretch=1.25: decode_failures 3

> stretch=1.5: decode_failures 15

### `MS-topology` - topology  `--scenario valleys`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| clustered | 1 | 0.935 | 0.933 | 0.002 | - | - | 0.992 | 0.992 | 0.000 | 1.14x | 21.4/28.3/31.5% | 1.5/5.6% | 3 |
| corridor | 1 | 0.557 | 0.536 | 0.021 | - | - | 0.584 | 0.586 | 0.219 | 1.29x | 14.8/21.7/24.0% | 1.9/5.5% | 3 |
| hub | 1 | 0.922 | 0.919 | 0.003 | - | - | 0.954 | 0.954 | 0.699 | 1.20x | 23.0/35.4/37.2% | 1.8/5.5% | 3 |

> topology=corridor: decode_failures 1

### `PR-crladder` - coding-rate-ladder  `--scenario valleys`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.814 | 0.814 | 0.000 | - | - | 0.908 | 0.941 | 0.622 | 1.80x | 19.4/33.2/37.9% | 2.7/6.4% | 3 |
| True | 1 | 0.817 | 0.817 | 0.000 | - | - | 0.939 | 0.952 | 0.621 | 1.84x | 19.8/33.8/38.6% | 2.8/6.5% | 3 |

> coding-rate-ladder=False: decode_failures 24

### `PR-dmmode-cr` - dm-mode  `--scenario valleys`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.817 | 0.817 | 0.000 | - | - | 0.939 | 0.952 | 0.621 | 1.84x | 19.8/33.8/38.6% | 2.8/6.5% | 3 |
| m4-early-flood | 1 | 0.814 | 0.814 | 0.000 | - | - | 0.922 | 0.937 | 0.627 | 1.84x | 19.7/33.9/38.7% | 2.8/6.6% | 3 |

> dm-mode=m4-early-flood: decode_failures 6

### `PR-protocol` - protocol  `--scenario valleys`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.860 | 0.860 | 0.000 | - | - | 0 | 0.000 | 0.664 | 1.45x | 15.7/26.6/30.4% | 2.2/5.1% | 3 |
| chain | 1 | 0.836 | 0.833 | 0.003 | - | - | 0.868 | 0.960 | 0.635 | 1.70x | 18.0/31.0/35.3% | 2.5/6.0% | 3 |
| sr | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |

### `PR-repeats` - extra-repeats  `--scenario valleys`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| True | 1 | 0.862 | 0.853 | 0.009 | - | - | 0.960 | 0.962 | 0.677 | 1.51x | 16.1/27.5/31.2% | 2.3/5.4% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario valleys`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.940 | 0.933 | 0.007 | - | - | 0.999 | 0.999 | 0.711 | 2.04x | 21.2/29.4/33.3% | 1.4/5.5% | 3 |
| True | 1 | 0.940 | 0.932 | 0.008 | - | - | 0.997 | 0.998 | 0.705 | 2.05x | 21.1/29.2/33.0% | 1.4/5.4% | 3 |

### `RF-bw500` - preset  `--scenario valleys`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.105 | 0.104 | 0.002 | - | - | 0.247 | 0.248 | 0.000 | 0.03x | 0.1/0.4/0.6% | 0.0/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.452 | 0.442 | 0.009 | - | - | 0.594 | 0.798 | 0.111 | 0.28x | 1.7/3.9/5.6% | 0.3/1.2% | 3 |
| LONG_TURBO | 1 | 0.777 | 0.772 | 0.004 | - | - | 0.939 | 0.940 | 0.539 | 1.39x | 11.1/20.0/23.4% | 2.1/5.1% | 3 |

> preset=MEDIUM_TURBO: decode_failures 28

### `RF-duct` - duct-per-hour  `--scenario valleys`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 0.25 | 1 | 0.872 | 0.863 | 0.009 | - | - | 0.964 | 0.966 | 0.691 | 1.44x | 17.9/28.5/32.2% | 2.1/5.4% | 3 |
| 1.0 | 1 | 0.936 | 0.930 | 0.006 | - | - | 0.989 | 0.990 | 0.832 | 1.06x | 22.8/30.7/33.6% | 1.4/5.2% | 3 |

### `RF-eu-presets` - preset  `--scenario valleys`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.275 | 0.270 | 0.005 | - | - | 0.405 | 0.544 | 0.000 | 0.13x | 0.6/1.7/2.9% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| LITE_FAST | 1 | 0.829 | 0.820 | 0.009 | - | - | 0.969 | 0.974 | 0.560 | 1.15x | 11.1/20.4/24.4% | 1.8/4.1% | 3 |
| NARROW_SLOW | 1 | 0.831 | 0.821 | 0.010 | - | - | 0.956 | 0.956 | 0.558 | 1.48x | 14.5/25.3/30.9% | 2.3/5.2% | 3 |

> preset=SHORT_FAST: decode_failures 9

> preset=LITE_FAST: decode_failures 1

### `RF-noise` - noise-profile  `--scenario valleys`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| temporal | 1 | 0.771 | 0.756 | 0.015 | - | - | 0.935 | 0.938 | 0.522 | 1.45x | 15.2/26.5/30.5% | 2.2/5.3% | 3 |
| transient | 1 | 0.862 | 0.851 | 0.011 | - | - | 0.967 | 0.969 | 0.646 | 1.49x | 15.9/27.3/31.0% | 2.3/5.4% | 3 |
| periodic | 1 | 0.684 | 0.672 | 0.012 | - | - | 0.783 | 0.798 | 0.491 | 1.35x | 14.7/24.8/28.4% | 2.1/4.6% | 3 |

> noise-profile=periodic: decode_failures 7

### `RF-preset` - preset  `--scenario valleys`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.275 | 0.270 | 0.005 | - | - | 0.405 | 0.544 | 0.000 | 0.13x | 0.6/1.7/2.9% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| LONG_MODERATE | 1 | 0.843 | 0.830 | 0.013 | - | - | 0.945 | 0.947 | 0.703 | 3.84x | 47.8/66.7/70.7% | 5.6/11.9% | 3 |

> preset=SHORT_FAST: decode_failures 9

### `RF-preset-turbo` - preset  `--scenario valleys`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.039 | 0.039 | 0.000 | - | - | 0.116 | 0.116 | 0.000 | 0.01x | 0.0/0.1/0.2% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.105 | 0.104 | 0.002 | - | - | 0.247 | 0.248 | 0.000 | 0.03x | 0.1/0.4/0.6% | 0.0/0.2% | 3 |
| LONG_FAST | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| LONG_TURBO | 1 | 0.777 | 0.772 | 0.004 | - | - | 0.939 | 0.940 | 0.539 | 1.39x | 11.1/20.0/23.4% | 2.1/5.1% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.841 | 0.829 | 0.011 | - | - | 0.950 | 0.953 | 0.621 | 2.03x | 19.9/33.4/37.2% | 3.0/6.9% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario valleys`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.802 | 0.791 | 0.011 | - | - | 0.906 | 0.907 | 0.602 | 1.43x | 15.6/26.4/30.1% | 2.2/5.1% | 3 |
| 10000 | 1 | 0.684 | 0.672 | 0.012 | - | - | 0.783 | 0.798 | 0.491 | 1.35x | 14.7/24.8/28.4% | 2.1/4.6% | 3 |
| 4000 | 1 | 0.423 | 0.416 | 0.007 | - | - | 0.471 | 0.557 | 0.242 | 1.11x | 12.3/21.0/24.3% | 1.7/3.5% | 3 |
| 2000 | 1 | 0.084 | 0.084 | 0.000 | - | - | 0.087 | 0.161 | 0.045 | 0.73x | 8.3/14.3/17.5% | 1.1/2.0% | 3 |

> noise-pulse-interval-ms=10000: decode_failures 7

> noise-pulse-interval-ms=4000: decode_failures 3

### `RF-stretch-duct` - duct-per-hour  `--scenario valleys`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.418 | 0.405 | 0.013 | - | - | 0.570 | 0.698 | 0.102 | 1.24x | 8.4/14.9/20.0% | 1.8/5.0% | 3 |
| 1.0 | 1 | 0.752 | 0.718 | 0.034 | - | - | 0.857 | 0.878 | 0.503 | 0.97x | 15.6/20.7/25.0% | 1.3/4.7% | 3 |

> duct-per-hour=0.0: decode_failures 15

> duct-per-hour=1.0: decode_failures 46

> slower: 8.91 s per simulated hour against 1.83 over 58 prior run(s) - 4.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-txpower` - tx-power  `--scenario valleys`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 22 | 1 | 0.416 | 0.408 | 0.007 | - | - | 0.534 | 0.718 | 0.108 | 1.30x | 7.7/17.0/22.3% | 2.0/5.0% | 3 |
| 17 | 1 | 0.110 | 0.110 | 0.000 | - | - | 0.117 | 0.234 | 0.000 | 0.74x | 2.9/8.0/10.8% | 0.9/3.1% | 2 |
| 14 | 1 | 0.051 | 0.051 | 0.000 | - | - | 0.121 | 0.122 | 0.000 | 0.53x | 1.5/5.5/8.3% | 0.6/2.3% | 3 |

> tx-power=22: decode_failures 17

> tx-power=17: 3 archives requested, 2 placed - group on the placed count

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario valleys`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.940 | 0.933 | 0.007 | - | - | 0.999 | 0.999 | 0.711 | 2.04x | 21.2/29.4/33.3% | 1.4/5.5% | 3 |
| True | 1 | 0.931 | 0.922 | 0.010 | - | - | 0.997 | 0.997 | 0.678 | 2.42x | 24.6/33.3/37.4% | 1.6/6.1% | 3 |

### `RT-favourites` - favourite-routers  `--scenario valleys`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.864 | 0.854 | 0.010 | - | - | 0.958 | 0.959 | 0.609 | 1.56x | 16.4/31.1/34.7% | 2.3/5.2% | 3 |
| True | 1 | 0.885 | 0.878 | 0.007 | - | - | 0.961 | 0.962 | 0.652 | 1.68x | 17.6/32.1/35.8% | 2.5/5.3% | 3 |

### `RT-hopassign` - hop-assign  `--scenario valleys`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| random | 1 | 0.878 | 0.871 | 0.007 | - | - | 0.963 | 0.964 | 0.685 | 1.51x | 16.2/27.2/31.0% | 2.3/5.2% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario valleys`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.721 | 0.686 | 0.034 | - | - | 0.914 | 0.919 | 0.354 | 1.09x | 12.2/23.0/26.5% | 1.5/4.7% | 3 |
| 7 | 1 | 0.910 | 0.905 | 0.004 | - | - | 0.969 | 0.969 | 0.696 | 1.61x | 17.3/28.0/31.9% | 2.5/5.3% | 3 |
| 15 | 1 | 0.927 | 0.924 | 0.002 | - | - | 0.971 | 0.972 | 0.739 | 1.62x | 17.4/28.0/31.9% | 2.5/5.3% | 3 |
| 32 | 1 | 0.930 | 0.928 | 0.002 | - | - | 0.972 | 0.974 | 0.730 | 1.63x | 17.4/28.0/31.9% | 2.5/5.3% | 3 |

### `RT-hopspread` - hop-limit  `--scenario valleys`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.721 | 0.686 | 0.034 | - | - | 0.914 | 0.919 | 0.354 | 1.09x | 12.2/23.0/26.5% | 1.5/4.7% | 3 |
| 5 | 1 | 0.866 | 0.856 | 0.009 | - | - | 0.955 | 0.959 | 0.673 | 1.50x | 16.2/27.2/31.1% | 2.3/5.2% | 3 |
| 7 | 1 | 0.910 | 0.905 | 0.004 | - | - | 0.969 | 0.969 | 0.696 | 1.61x | 17.3/28.0/31.9% | 2.5/5.3% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario valleys`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| KNOWN_ONLY | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.845 | 0.845 | 0.000 | - | - | 0.844 | 0.959 | 0.655 | 1.45x | 15.7/26.6/30.3% | 2.2/5.1% | 3 |

### `RT-spread` - hop-spread  `--scenario valleys`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.721 | 0.686 | 0.034 | - | - | 0.914 | 0.919 | 0.354 | 1.09x | 12.2/23.0/26.5% | 1.5/4.7% | 3 |
| True | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |

### `SC-signing` - signature-policy  `--scenario valleys`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| BALANCED | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| STRICT | 1 | 0.722 | 0.722 | 0.000 | - | - | 0.832 | 0.837 | 0.503 | 1.59x | 17.1/28.9/32.9% | 2.4/5.7% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario valleys`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| dm | 1 | 0.866 | 0.856 | 0.011 | - | - | 0.972 | 0.975 | 0.635 | 1.46x | 15.7/27.1/30.7% | 2.2/5.5% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario valleys`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.859 | 0.847 | 0.012 | - | - | 0.964 | 0.967 | 0.666 | 1.51x | 16.2/27.6/31.4% | 2.3/5.4% | 3 |
| local | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| time | 1 | 0.861 | 0.851 | 0.009 | - | - | 0.963 | 0.969 | 0.659 | 1.51x | 16.2/27.6/31.3% | 2.3/5.4% | 3 |
| window | 1 | 0.861 | 0.849 | 0.012 | - | - | 0.961 | 0.963 | 0.647 | 1.47x | 15.8/26.8/30.6% | 2.3/5.3% | 3 |

> bucket-mode=global: misdecodes 34

> bucket-mode=time: misdecodes 19

> bucket-mode=window: misdecodes 19

### `SF-bucket-time` - time-bucket-s  `--scenario valleys`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.852 | 0.841 | 0.011 | - | - | 0.964 | 0.968 | 0.629 | 1.65x | 17.7/29.9/34.0% | 2.5/6.0% | 3 |
| 1800 | 1 | 0.861 | 0.851 | 0.009 | - | - | 0.963 | 0.969 | 0.659 | 1.51x | 16.2/27.6/31.3% | 2.3/5.4% | 3 |
| 3600 | 1 | 0.866 | 0.857 | 0.008 | - | - | 0.960 | 0.973 | 0.648 | 1.48x | 15.8/27.0/30.8% | 2.2/5.2% | 3 |

> time-bucket-s=600: misdecodes 99

> time-bucket-s=1800: misdecodes 19

> time-bucket-s=3600: misdecodes 6

> time-bucket-s=3600: decode_failures 4

### `SF-cadence` - trigger  `--scenario valleys`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| interval | 1 | 0.832 | 0.819 | 0.013 | - | - | 0.935 | 0.954 | 0.624 | 1.95x | 20.3/35.7/39.7% | 2.9/7.7% | 3 |
| aimd | 1 | 0.846 | 0.842 | 0.004 | - | - | 0.878 | 0.959 | 0.644 | 1.51x | 16.2/27.7/31.5% | 2.3/5.3% | 3 |
| bucket+interval | 1 | 0.837 | 0.821 | 0.017 | - | - | 0.956 | 0.958 | 0.647 | 2.00x | 20.9/36.6/40.8% | 3.0/7.9% | 3 |

> trigger=interval: misdecodes 10

> trigger=interval: decode_failures 19

> trigger=aimd: misdecodes 3

> trigger=aimd: decode_failures 2

> trigger=bucket+interval: misdecodes 17

### `SF-capacity` - capacity  `--scenario valleys`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.862 | 0.850 | 0.011 | - | - | 0.957 | 0.965 | 0.651 | 1.50x | 16.1/27.6/31.2% | 2.2/5.5% | 3 |
| 8 | 1 | 0.856 | 0.845 | 0.011 | - | - | 0.948 | 0.957 | 0.669 | 1.49x | 16.0/27.5/31.1% | 2.2/5.5% | 3 |
| 16 | 1 | 0.859 | 0.849 | 0.010 | - | - | 0.958 | 0.963 | 0.668 | 1.47x | 15.7/26.9/30.6% | 2.2/5.3% | 3 |
| 32 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 50 | 1 | 0.862 | 0.852 | 0.010 | - | - | 0.965 | 0.967 | 0.657 | 1.47x | 15.8/26.9/30.6% | 2.3/5.3% | 3 |

> capacity=4: decode_failures 100

> capacity=8: decode_failures 90

> capacity=16: decode_failures 7

### `SF-capacity-local` - capacity  `--scenario valleys`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.862 | 0.850 | 0.011 | - | - | 0.957 | 0.965 | 0.651 | 1.50x | 16.1/27.6/31.2% | 2.2/5.5% | 3 |
| 8 | 1 | 0.856 | 0.845 | 0.011 | - | - | 0.948 | 0.957 | 0.669 | 1.49x | 16.0/27.5/31.1% | 2.2/5.5% | 3 |
| 16 | 1 | 0.859 | 0.849 | 0.010 | - | - | 0.958 | 0.963 | 0.668 | 1.47x | 15.7/26.9/30.6% | 2.2/5.3% | 3 |
| 32 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 50 | 1 | 0.862 | 0.852 | 0.010 | - | - | 0.965 | 0.967 | 0.657 | 1.47x | 15.8/26.9/30.6% | 2.3/5.3% | 3 |

> capacity=4: decode_failures 100

> capacity=8: decode_failures 90

> capacity=16: decode_failures 7

### `SF-capacity-window` - capacity  `--scenario valleys`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.848 | 0.843 | 0.005 | - | - | 0.889 | 0.968 | 0.658 | 1.48x | 15.9/26.9/30.6% | 2.2/5.2% | 3 |
| 16 | 1 | 0.852 | 0.841 | 0.011 | - | - | 0.941 | 0.952 | 0.669 | 1.48x | 15.9/27.2/30.8% | 2.2/5.3% | 3 |
| 32 | 1 | 0.861 | 0.849 | 0.012 | - | - | 0.961 | 0.963 | 0.647 | 1.47x | 15.8/26.8/30.6% | 2.3/5.3% | 3 |

> capacity=8: misdecodes 6

> capacity=8: decode_failures 112

> capacity=16: misdecodes 13

> capacity=16: decode_failures 11

> capacity=32: misdecodes 19

### `SF-catchup` - catch-up-hours  `--scenario valleys`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.837 | 0.821 | 0.017 | - | - | 0.956 | 0.958 | 0.647 | 2.00x | 20.9/36.6/40.8% | 3.0/7.9% | 3 |
| 02-06 | 1 | 0.858 | 0.852 | 0.006 | - | - | 0.910 | 0.969 | 0.651 | 1.51x | 16.1/27.8/31.5% | 2.3/5.5% | 3 |
| 00-08 | 1 | 0.857 | 0.850 | 0.007 | - | - | 0.912 | 0.962 | 0.667 | 1.58x | 16.9/28.9/32.6% | 2.4/5.9% | 3 |

> catch-up-hours=: misdecodes 17

> catch-up-hours=02-06: decode_failures 40

> catch-up-hours=00-08: decode_failures 43

### `SF-hops-flat` - hops-apart  `--scenario valleys`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.858 | 0.854 | 0.004 | - | - | 0.967 | 0.968 | 0.669 | 1.49x | 16.0/27.2/31.0% | 2.2/5.2% | 3 |
| 2 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 3 | 1 | 0.871 | 0.854 | 0.018 | - | - | 0.944 | 0.960 | 0.632 | 1.50x | 16.2/27.4/31.3% | 2.3/5.4% | 3 |
| 4 | 1 | 0.876 | 0.860 | 0.016 | - | - | 0.955 | 0.976 | 0.675 | 1.49x | 15.9/27.1/31.0% | 2.2/5.4% | 3 |

> hops-apart=3: decode_failures 19

> hops-apart=4: decode_failures 18

### `SF-hops-spread` - hops-apart  `--scenario valleys`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.858 | 0.854 | 0.004 | - | - | 0.967 | 0.968 | 0.669 | 1.49x | 16.0/27.2/31.0% | 2.2/5.2% | 3 |
| 2 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 3 | 1 | 0.871 | 0.854 | 0.018 | - | - | 0.944 | 0.960 | 0.632 | 1.50x | 16.2/27.4/31.3% | 2.3/5.4% | 3 |
| 4 | 1 | 0.876 | 0.860 | 0.016 | - | - | 0.955 | 0.976 | 0.675 | 1.49x | 15.9/27.1/31.0% | 2.2/5.4% | 3 |
| 5 | 1 | 0.871 | 0.853 | 0.017 | - | - | 0.957 | 0.968 | 0.675 | 1.48x | 15.9/27.2/31.1% | 2.3/5.3% | 3 |

> hops-apart=3: decode_failures 19

> hops-apart=4: decode_failures 18

### `SF-jitter-global` - advert-jitter-s  `--scenario valleys`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.864 | 0.856 | 0.009 | - | - | 0.967 | 0.969 | 0.674 | 1.49x | 15.9/27.3/31.0% | 2.2/5.3% | 3 |
| 30 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 120 | 1 | 0.872 | 0.862 | 0.010 | - | - | 0.971 | 0.974 | 0.679 | 1.48x | 15.9/27.2/31.1% | 2.3/5.3% | 3 |
| 600 | 1 | 0.852 | 0.842 | 0.011 | - | - | 0.950 | 0.953 | 0.648 | 1.49x | 16.0/27.2/31.0% | 2.3/5.3% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario valleys`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.864 | 0.856 | 0.009 | - | - | 0.967 | 0.969 | 0.674 | 1.49x | 15.9/27.3/31.0% | 2.2/5.3% | 3 |
| 30 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 120 | 1 | 0.872 | 0.862 | 0.010 | - | - | 0.971 | 0.974 | 0.679 | 1.48x | 15.9/27.2/31.1% | 2.3/5.3% | 3 |
| 600 | 1 | 0.852 | 0.842 | 0.011 | - | - | 0.950 | 0.953 | 0.648 | 1.49x | 16.0/27.2/31.0% | 2.3/5.3% | 3 |

### `SF-place-flat` - place  `--scenario valleys`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.873 | 0.854 | 0.020 | - | - | 0.889 | 0.965 | 0.663 | 1.49x | 16.1/26.9/30.7% | 2.2/5.2% | 3 |
| routers | 1 | 0.844 | 0.843 | 0.001 | - | - | 0.943 | 0.944 | 0.648 | 1.49x | 16.1/27.3/31.3% | 2.2/5.4% | 3 |
| alternate-routers | 1 | 0.851 | 0.849 | 0.002 | - | - | 0.949 | 0.949 | 0.653 | 1.48x | 15.9/27.3/31.0% | 2.2/5.3% | 3 |
| beside-router | 1 | 0.862 | 0.857 | 0.005 | - | - | 0.967 | 0.969 | 0.664 | 1.48x | 15.9/27.4/31.1% | 2.3/5.4% | 3 |
| random-clients | 1 | 0.862 | 0.847 | 0.015 | - | - | 0.959 | 0.961 | 0.660 | 1.51x | 16.2/27.8/31.6% | 2.3/5.4% | 3 |
| hops-apart | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |

> place=spread: decode_failures 14

### `SF-place-spread` - place  `--scenario valleys`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.873 | 0.854 | 0.020 | - | - | 0.889 | 0.965 | 0.663 | 1.49x | 16.1/26.9/30.7% | 2.2/5.2% | 3 |
| routers | 1 | 0.844 | 0.843 | 0.001 | - | - | 0.943 | 0.944 | 0.648 | 1.49x | 16.1/27.3/31.3% | 2.2/5.4% | 3 |
| alternate-routers | 1 | 0.851 | 0.849 | 0.002 | - | - | 0.949 | 0.949 | 0.653 | 1.48x | 15.9/27.3/31.0% | 2.2/5.3% | 3 |
| beside-router | 1 | 0.862 | 0.857 | 0.005 | - | - | 0.967 | 0.969 | 0.664 | 1.48x | 15.9/27.4/31.1% | 2.3/5.4% | 3 |
| random-clients | 1 | 0.862 | 0.847 | 0.015 | - | - | 0.959 | 0.961 | 0.660 | 1.51x | 16.2/27.8/31.6% | 2.3/5.4% | 3 |
| hops-apart | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |

> place=spread: decode_failures 14

### `SF-provide-transport` - provide-transport  `--scenario valleys`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| broadcast | 1 | 0.895 | 0.841 | 0.054 | - | - | 0.962 | 0.964 | 0.718 | 1.61x | 17.2/29.3/33.2% | 2.4/5.6% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario valleys`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| heard | 1 | 0.864 | 0.853 | 0.011 | - | - | 0.964 | 0.966 | 0.669 | 1.48x | 15.7/27.0/30.7% | 2.2/5.3% | 3 |

> replay-ordering=heard: misdecodes 11

### `SF-replay-order-broadcast` - replay-ordering  `--scenario valleys`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.895 | 0.841 | 0.054 | - | - | 0.962 | 0.964 | 0.718 | 1.61x | 17.2/29.3/33.2% | 2.4/5.6% | 3 |
| heard | 1 | 0.883 | 0.833 | 0.050 | - | - | 0.948 | 0.958 | 0.717 | 1.58x | 16.8/28.7/32.6% | 2.4/5.5% | 3 |

> replay-ordering=heard: misdecodes 1

> replay-ordering=heard: decode_failures 13

### `SF-resolve` - resolve  `--scenario valleys`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| enum | 1 | 0.864 | 0.852 | 0.012 | - | - | 0.967 | 0.975 | 0.664 | 1.50x | 16.0/27.5/31.2% | 2.3/5.5% | 3 |
| hybrid | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |

### `SF-servers-allrouters` - servers  `--scenario valleys`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.844 | 0.843 | 0.001 | - | - | 0.943 | 0.944 | 0.648 | 1.49x | 16.1/27.3/31.3% | 2.2/5.4% | 3 |
| 6 | 1 | 0.847 | 0.844 | 0.003 | - | - | 0.955 | 0.955 | 0.651 | 1.53x | 16.6/28.5/32.2% | 2.3/5.5% | 6 |

### `SF-servers-flat` - servers  `--scenario valleys`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.867 | 0.860 | 0.007 | - | - | 0.950 | 0.971 | 0.668 | 1.48x | 15.9/27.1/30.9% | 2.2/5.3% | 2 |
| 3 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 5 | 1 | 0.861 | 0.847 | 0.014 | - | - | 0.976 | 0.978 | 0.673 | 1.53x | 16.3/27.8/31.8% | 2.3/5.3% | 5 |
| 8 | 1 | 0.863 | 0.845 | 0.019 | - | - | 0.986 | 0.987 | 0.681 | 1.55x | 16.6/28.2/32.1% | 2.3/5.4% | 8 |

> servers=2: decode_failures 11

> servers=8: misdecodes 1

### `SF-servers-spread` - servers  `--scenario valleys`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.867 | 0.860 | 0.007 | - | - | 0.950 | 0.971 | 0.668 | 1.48x | 15.9/27.1/30.9% | 2.2/5.3% | 2 |
| 3 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 5 | 1 | 0.861 | 0.847 | 0.014 | - | - | 0.976 | 0.978 | 0.673 | 1.53x | 16.3/27.8/31.8% | 2.3/5.3% | 5 |
| 8 | 1 | 0.863 | 0.845 | 0.019 | - | - | 0.986 | 0.987 | 0.681 | 1.55x | 16.6/28.2/32.1% | 2.3/5.4% | 8 |

> servers=2: decode_failures 11

> servers=8: misdecodes 1

### `SF-signed` - signed  `--scenario valleys`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| True | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario valleys`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.869 | 0.861 | 0.008 | - | - | 0.955 | 0.963 | 0.666 | 1.39x | 14.8/25.5/29.1% | 2.1/4.9% | 3 |
| 1 | 1 | 0.870 | 0.861 | 0.008 | - | - | 0.967 | 0.971 | 0.659 | 1.37x | 14.6/25.0/28.5% | 2.1/4.8% | 3 |
| 2 | 1 | 0.875 | 0.864 | 0.010 | - | - | 0.966 | 0.968 | 0.676 | 1.38x | 14.8/25.3/28.7% | 2.1/4.9% | 3 |
| 4 | 1 | 0.873 | 0.864 | 0.008 | - | - | 0.963 | 0.966 | 0.673 | 1.38x | 14.8/25.2/28.6% | 2.1/4.9% | 3 |

### `SF-width` - short-id-bits  `--scenario valleys`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.864 | 0.853 | 0.011 | - | - | 0.967 | 0.970 | 0.632 | 1.49x | 15.9/27.3/31.0% | 2.2/5.4% | 3 |
| 24 | 1 | 0.862 | 0.850 | 0.012 | - | - | 0.975 | 0.978 | 0.656 | 1.48x | 15.8/27.1/30.8% | 2.2/5.3% | 3 |
| 32 | 1 | 0.866 | 0.856 | 0.010 | - | - | 0.965 | 0.968 | 0.683 | 1.49x | 15.8/27.3/31.0% | 2.2/5.3% | 3 |
| 64 | 1 | 0.868 | 0.859 | 0.009 | - | - | 0.970 | 0.973 | 0.655 | 1.50x | 16.1/27.5/31.3% | 2.2/5.4% | 3 |

### `SF-window-size` - window-size  `--scenario valleys`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.849 | 0.837 | 0.012 | - | - | 0.954 | 0.957 | 0.652 | 1.59x | 16.9/28.9/32.8% | 2.4/5.6% | 3 |
| 16 | 1 | 0.856 | 0.845 | 0.011 | - | - | 0.954 | 0.958 | 0.669 | 1.52x | 16.2/27.6/31.5% | 2.3/5.4% | 3 |
| 32 | 1 | 0.861 | 0.849 | 0.012 | - | - | 0.961 | 0.963 | 0.647 | 1.47x | 15.8/26.8/30.6% | 2.3/5.3% | 3 |

> window-size=8: misdecodes 134

> window-size=16: misdecodes 57

> window-size=32: misdecodes 19

### `TH-congestion` - no-congestion-scaling  `--scenario valleys`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.940 | 0.933 | 0.007 | - | - | 0.999 | 0.999 | 0.711 | 2.04x | 21.2/29.4/33.3% | 1.4/5.5% | 3 |
| True | 1 | 0.721 | 0.694 | 0.028 | - | - | 0.889 | 0.915 | 0.471 | 6.04x | 56.9/71.4/76.5% | 4.3/13.6% | 3 |

> no-congestion-scaling=True: decode_failures 85

### `TH-congestion-input` - congestion-input  `--scenario valleys`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.520 | 0.508 | 0.013 | - | - | 0.852 | 0.854 | 0.169 | 4.58x | 16.1/27.8/37.8% | 1.5/6.3% | 3 |
| truesize | 1 | 0.549 | 0.537 | 0.012 | - | - | 0.880 | 0.880 | 0.192 | 3.41x | 11.8/22.2/31.0% | 1.1/5.3% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario valleys`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.941 | 0.933 | 0.008 | - | - | 0.998 | 0.998 | 0.688 | 1.87x | 19.2/27.1/30.8% | 1.3/5.0% | 3 |
| adaptive | 1 | 0.940 | 0.933 | 0.007 | - | - | 0.999 | 0.999 | 0.711 | 2.04x | 21.2/29.4/33.3% | 1.4/5.5% | 3 |

