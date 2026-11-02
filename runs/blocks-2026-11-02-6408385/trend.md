# Sweep blocks-2026-11-02-6408385

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** rolling
- **seed base** 6408385 · seeds 6408385
- **blocks** 87 run
- **compute** 10.7 h of simulator time across every cell
- **generated** 2026-11-02T11:16:47+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>88 warnings</summary>

- AD-amplifiers: faster: 0.785 s per simulated hour against 1.59 over 73 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- AD-siting: siting-mix=local-typical: decode_failures 30
- AD-worst: role-placement=degree: decode_failures 87
- AD-worst: role-placement=inverse: decode_failures 101
- AD-worst: slower: 24.9 s per simulated hour against 3.48 over 73 prior run(s) - 7.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 52
- DB-hotstore-stress: max-num-nodes=120: decode_failures 51
- DB-hotstore-stress: max-num-nodes=250: decode_failures 59
- DB-platform: platform-mix=constrained: decode_failures 1
- DB-warm: warm-num-nodes=0: queue drops 16.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 114
- DB-warm: warm-num-nodes=25: queue drops 16.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 114
- DB-warm: warm-num-nodes=100: queue drops 16.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 114
- DB-warm: warm-num-nodes=2000: queue drops 16.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 114
- DG-burst: burst-loss=0.2: decode_failures 3
- DG-burst: burst-loss=0.3: decode_failures 19
- DG-outage: burst-loss=0.1: decode_failures 12
- DG-outage: burst-loss=0.2: decode_failures 30
- DG-outage: burst-loss=0.3: decode_failures 27
- DM-mode: faster: 1.24 s per simulated hour against 3.06 over 73 prior run(s) - 2.5x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- FW-signing-cost: profile-flag=signing=false: misdecodes 1
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 11
- LD-chatty: broadcast-interval-s=900: misdecodes 1
- LD-chatty: broadcast-interval-s=300: decode_failures 28
- LD-interval: broadcast-interval-s=900: misdecodes 1
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 16.9% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 114
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 25.7% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 116
- MS-hopscale: nodes=250: decode_failures 85
- MS-hopscale: nodes=500: decode_failures 1
- MS-oversubscribed: nodes=250: decode_failures 51
- MS-router-late: router-late-fraction=0.1: misdecodes 1
- MS-siting: siting-mix=event: decode_failures 26
- MS-siting: siting-mix=backbone: misdecodes 1
- MS-size: nodes=150: decode_failures 92
- MS-size: slower: 8.46 s per simulated hour against 3.42 over 73 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-topology: topology=corridor: decode_failures 2
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 4
- RF-eu-presets: preset=SHORT_FAST: decode_failures 14
- RF-preset: preset=SHORT_FAST: decode_failures 14
- RF-preset: preset=LONG_MODERATE: decode_failures 19
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 4
- RF-txpower: tx-power=22: decode_failures 2
- RF-txpower: tx-power=17: decode_failures 5
- RT-rebroadcast: faster: 0.776 s per simulated hour against 1.55 over 73 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-bucket-mode: bucket-mode=global: misdecodes 33
- SF-bucket-mode: bucket-mode=time: misdecodes 43
- SF-bucket-mode: bucket-mode=window: misdecodes 26
- SF-bucket-time: time-bucket-s=600: misdecodes 124
- SF-bucket-time: time-bucket-s=1800: misdecodes 43
- SF-bucket-time: time-bucket-s=3600: misdecodes 16
- SF-cadence: trigger=interval: misdecodes 23
- SF-cadence: trigger=aimd: misdecodes 4
- SF-cadence: trigger=bucket+interval: misdecodes 21
- SF-cadence: faster: 1.77 s per simulated hour against 3.62 over 73 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-capacity-local: capacity=4: decode_failures 97
- SF-capacity-local: capacity=8: decode_failures 2
- SF-capacity: capacity=4: decode_failures 97
- SF-capacity: capacity=8: decode_failures 2
- SF-capacity-window: capacity=8: misdecodes 20
- SF-capacity-window: capacity=8: decode_failures 4
- SF-capacity-window: capacity=16: misdecodes 24
- SF-capacity-window: capacity=32: misdecodes 26
- SF-capacity-window: faster: 0.788 s per simulated hour against 1.59 over 73 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-catchup: catch-up-hours=: misdecodes 21
- SF-catchup: catch-up-hours=02-06: decode_failures 25
- SF-catchup: catch-up-hours=00-08: misdecodes 1
- SF-catchup: catch-up-hours=00-08: decode_failures 24
- SF-hops-flat: faster: 1.68 s per simulated hour against 4.01 over 73 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-hops-spread: hops-apart=5: decode_failures 28
- SF-place-flat: place=spread: decode_failures 2
- SF-place-spread: place=spread: decode_failures 2
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 15
- SF-replay-order: replay-ordering=heard: misdecodes 16
- SF-servers-flat: servers=8: misdecodes 1
- SF-servers-spread: servers=8: misdecodes 1
- SF-servers-spread: faster: 1.04 s per simulated hour against 2.21 over 73 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-window-size: window-size=8: misdecodes 148
- SF-window-size: window-size=16: misdecodes 62
- SF-window-size: window-size=32: misdecodes 26
- TH-congestion-input: congestion-input=hotstore: decode_failures 51
- TH-congestion-input: congestion-input=truesize: decode_failures 13
- TH-congestion: no-congestion-scaling=True: queue drops 14.6% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 63

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `AD-worst` | 24.9 | 3.48 | 7.16x | 73 |
| `MS-size` | 8.46 | 3.42 | 2.48x | 73 |
| `MS-siting` | 3.33 | 1.75 | 1.90x | 72 |
| `RF-preset` | 5.04 | 2.77 | 1.82x | 73 |
| `TH-congestion-input` | 18.4 | 10.3 | 1.78x | 73 |
| `AD-siting` | 2.51 | 1.45 | 1.73x | 73 |
| `DB-hotstore-stress` | 35.8 | 20.9 | 1.71x | 73 |
| `RF-bw500` | 1.26 | 1.9 | 0.66x | 73 |
| `FW-versions` | 1 | 1.53 | 0.66x | 73 |
| `SF-servers-allrouters` | 1.18 | 1.83 | 0.65x | 73 |
| `PR-crladder` | 1.8 | 2.79 | 0.64x | 73 |
| `TH-congestion` | 10.9 | 17 | 0.64x | 73 |
| `AD-badrouters` | 1.15 | 1.79 | 0.64x | 73 |
| `RT-hoplimit` | 1.12 | 1.75 | 0.64x | 73 |
| `SF-capacity-local` | 1.08 | 1.72 | 0.62x | 73 |
| `MS-stretch` | 1.33 | 2.16 | 0.61x | 73 |
| `PR-dmmode-cr` | 1.56 | 2.6 | 0.60x | 73 |
| `RF-preset-turbo` | 0.885 | 1.48 | 0.60x | 69 |
| `FW-firmware` | 0.958 | 1.65 | 0.58x | 73 |
| `DG-loss` | 1.31 | 2.27 | 0.57x | 73 |
| `RF-duct` | 0.979 | 1.73 | 0.57x | 73 |
| `MS-roles` | 0.938 | 1.68 | 0.56x | 73 |
| `PR-protocol` | 0.751 | 1.36 | 0.55x | 73 |
| `FW-mixed` | 0.899 | 1.67 | 0.54x | 73 |
| `SF-resolve` | 0.798 | 1.51 | 0.53x | 73 |
| `RT-rebroadcast` | 0.776 | 1.55 | 0.50x | 73 |
| `SF-capacity-window` | 0.788 | 1.59 | 0.49x | 73 |
| `AD-amplifiers` | 0.785 | 1.59 | 0.49x | 73 |
| `SF-cadence` | 1.77 | 3.62 | 0.49x | 73 |
| `SF-servers-spread` | 1.04 | 2.21 | 0.47x | 73 |
| `SF-hops-flat` | 1.68 | 4.01 | 0.42x | 73 |
| `DM-mode` | 1.24 | 3.06 | 0.40x | 73 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.991 | 0.991 | 0.896 → 0.902 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.985 | 0.985 | 0.897 → 0.902 | 1x bytes_on_air | up | 2 |
| `AD-siting` | siting-mix | **held** | 0.024 → 0.975 | 0.951 | 0.042 → 0.855 | 2.3e+02x sr_bytes | down | 3 |
| `RF-txpower` | tx-power | **held** | 0.047 → 0.991 | 0.945 | 0.053 → 0.900 | 89x sr_bytes | down | 4 |
| `RF-preset-turbo` | preset | **held** | 0.093 → 0.991 | 0.899 | 0.039 → 0.900 | 12x advert_bytes | up | 5 |
| `MS-stretch` | stretch | **held** | 0.188 → 0.991 | 0.803 | 0.111 → 0.900 | 8.1x sr_airtime | down | 4 |
| `RF-bw500` | preset | **held** | 0.140 → 0.943 | 0.802 | 0.104 → 0.825 | 12x sr_bytes | up | 3 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.143 → 0.931 | 0.788 | 0.121 → 0.835 | 96x sr_airtime | down | 4 |
| `MS-hopscale` | nodes | **held** | 0.388 → 0.991 | 0.603 | 0.311 → 0.900 | 12x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.390 → 0.986 | 0.596 | 0.312 → 0.797 | 4.9x sr_bytes | down | 3 |
| `RF-eu-presets` | preset | **text** | 0.316 → 0.905 | 0.589 | 0.307 → 0.900 | 2.4x advert_bytes | up | 4 |
| `RF-preset` | preset | **text** | 0.316 → 0.905 | 0.589 | 0.307 → 0.900 | 3x sr_airtime | up | 3 |
| `MS-siting` | siting-mix | **text** | 0.409 → 0.974 | 0.565 | 0.403 → 0.973 | 2x sr_bytes | up | 4 |
| `MS-topology` | topology | **text** | 0.615 → 0.975 | 0.360 | 0.588 → 0.972 | 2.3x sr_bytes | up | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.606 → 0.937 | 0.331 | 0.592 → 0.936 | 9.7x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.579 → 0.905 | 0.326 | 0.555 → 0.900 | 2.9x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.630 → 0.928 | 0.298 | 0.615 → 0.925 | 8.1x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.620 → 0.905 | 0.285 | 0.576 → 0.900 | 2.9x sr_bytes | down | 4 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.444 → 0.717 | 0.273 | 0.438 → 0.704 | 2x sr_airtime | up | 2 |
| `MS-density` | nodes | **text** | 0.726 → 0.971 | 0.245 | 0.711 → 0.970 | 6x sr_airtime | up | 5 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.382 → 0.615 | 0.233 | 0.333 → 0.560 | 5.9x sr_airtime | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.736 → 0.955 | 0.220 | 0.728 → 0.952 | 4x sr_airtime | down | 2 |
| `RT-hoplimit` | hop-limit | **text** | 0.742 → 0.931 | 0.189 | 0.712 → 0.931 | 2.3x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.742 → 0.928 | 0.186 | 0.712 → 0.927 | 2.1x sr_bytes | up | 3 |
| `MS-size` | nodes | **text** | 0.730 → 0.905 | 0.175 | 0.708 → 0.900 | 14x sr_bytes | down | 5 |
| `RT-spread` | hop-spread | **text** | 0.742 → 0.905 | 0.163 | 0.712 → 0.900 | 1.8x sr_bytes | up | 2 |
| `RF-noise` | noise-profile | **text** | 0.743 → 0.905 | 0.162 | 0.736 → 0.900 | 1.3x sr_airtime | down | 4 |
| `SC-signing` | signature-policy | **text** | 0.761 → 0.905 | 0.144 | 0.761 → 0.900 | 1.4x sr_airtime | down | 3 |
| `DG-loss` | extra-loss | **text** | 0.791 → 0.905 | 0.114 | 0.773 → 0.900 | 1.7x sr_bytes | down | 4 |
| `AD-badrouters` | role-placement | **text** | 0.756 → 0.863 | 0.107 | 0.741 → 0.855 | 1.6x sr_bytes | down | 3 |
| `DB-platform` | platform-mix | **text** | 0.854 → 0.939 | 0.085 | 0.843 → 0.937 | 2.1x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.854 → 0.939 | 0.085 | 0.846 → 0.937 | 2.2x sr_airtime | up | 4 |
| `AD-flooding` | role-mix | **text** | 0.863 → 0.946 | 0.083 | 0.855 → 0.945 | 2.6x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.863 → 0.946 | 0.083 | 0.855 → 0.945 | 2.6x bytes_on_air | up | 3 |
| `SF-hops-spread` | hops-apart | **held** | 0.911 → 0.993 | 0.082 | 0.897 → 0.905 | 2x sr_bytes | down | 5 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.646 → 0.723 | 0.077 | 0.637 → 0.715 | 1.2x sr_airtime | down | 2 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.905 → 0.968 | 0.064 | 0.900 → 0.966 | 1.5x sr_bytes | up | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.873 → 0.934 | 0.061 | 0.865 → 0.932 | 4.7x sr_airtime | up | 4 |
| `RT-hopassign` | hop-assign | **text** | 0.845 → 0.905 | 0.060 | 0.828 → 0.900 | 1.2x sr_airtime | down | 2 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.905 → 0.958 | 0.053 | 0.900 → 0.957 | 1.9x sr_bytes | up | 3 |
| `TH-congestion-input` | congestion-input | **held** | 0.615 → 0.655 | 0.040 | 0.552 → 0.589 | 1.4x sr_airtime | up | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.865 → 0.905 | 0.040 | 0.855 → 0.900 | 1.5x sr_airtime | down | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.953 → 0.991 | 0.038 | 0.899 → 0.900 | 24x sr_airtime | down | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.905 → 0.943 | 0.038 | 0.900 → 0.939 | 1.3x bytes_on_air | up | 3 |
| `MS-roles` | role-mix | **text** | 0.863 → 0.898 | 0.035 | 0.855 → 0.893 | 1.2x bytes_on_air | down | 2 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.881 → 0.914 | 0.033 | 0.869 → 0.907 | 2.1x bytes_on_air | down | 4 |
| `FW-mixed` | legacy-fraction | **text** | 0.889 → 0.920 | 0.031 | 0.880 → 0.913 | 2x bytes_on_air | down | 4 |
| `SF-cadence` | trigger | **held** | 0.962 → 0.991 | 0.029 | 0.882 → 0.900 | 18x sr_bytes | down | 4 |
| `AD-worst` | role-placement | **text** | 0.758 → 0.785 | 0.027 | 0.727 → 0.766 | 1.1x sr_bytes | down | 2 |
| `MS-roles-fav` | role-mix | **text** | 0.880 → 0.907 | 0.027 | 0.875 → 0.900 | 1.1x sr_airtime | down | 2 |
| `SF-hops-flat` | hops-apart | **held** | 0.968 → 0.993 | 0.025 | 0.897 → 0.903 | 1.7x sr_bytes | up | 4 |
| `MS-router-late` | router-late-fraction | **text** | 0.905 → 0.927 | 0.022 | 0.900 → 0.923 | 1.4x bytes_on_air | up | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.905 → 0.921 | 0.016 | 0.900 → 0.919 | 3.3x bytes_on_air | down | 2 |
| `SF-place-flat` | place | **text** | 0.904 → 0.920 | 0.016 | 0.897 → 0.908 | 2.9x sr_bytes | down | 6 |
| `SF-place-spread` | place | **text** | 0.904 → 0.920 | 0.016 | 0.897 → 0.908 | 2.9x sr_bytes | down | 6 |
| `SF-provide-transport` | provide-transport | **text** | 0.905 → 0.921 | 0.016 | 0.900 → 0.900 | 1.8x sr_airtime | up | 2 |
| `SF-catchup` | catch-up-hours | **text** | 0.889 → 0.903 | 0.014 | 0.882 → 0.901 | 9.4x advert_bytes | up | 3 |
| `LD-diurnal` | diurnal | **text** | 0.905 → 0.917 | 0.013 | 0.900 → 0.915 | 1.3x sr_bytes | down | 3 |
| `SF-capacity` | capacity | **held** | 0.979 → 0.991 | 0.012 | 0.897 → 0.900 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.979 → 0.991 | 0.012 | 0.897 → 0.900 | 5.3x advert_bytes | up | 5 |
| `DM-mode` | dm-mode | **held** | 0.976 → 0.988 | 0.012 | 0.875 → 0.887 | 1.2x sr_airtime | up | 3 |
| `FW-versions` | profile | **text** | 0.905 → 0.917 | 0.012 | 0.900 → 0.914 | 3.2x bytes_on_air | down | 5 |
| `FW-firmware` | profile | **text** | 0.905 → 0.915 | 0.010 | 0.900 → 0.908 | 3.2x bytes_on_air | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.945 → 0.955 | 0.010 | 0.942 → 0.952 | 1.2x sr_airtime | down | 2 |
| `SF-servers-flat` | servers | **held** | 0.981 → 0.991 | 0.010 | 0.896 → 0.900 | 6.5x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.981 → 0.991 | 0.010 | 0.896 → 0.900 | 6.5x sr_bytes | up | 4 |
| `SF-window-size` | window-size | **text** | 0.897 → 0.907 | 0.010 | 0.890 → 0.902 | 4.5x advert_bytes | up | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.913 → 0.922 | 0.009 | 0.908 → 0.918 | 1.1x sr_bytes | up | 2 |
| `SF-sr-retries` | sr-retries | **text** | 0.901 → 0.909 | 0.008 | 0.895 → 0.904 | 1.1x sr_bytes | down | 4 |
| `SF-width` | short-id-bits | **text** | 0.901 → 0.909 | 0.008 | 0.897 → 0.905 | 3.1x advert_bytes | up | 4 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.899 → 0.906 | 0.007 | 0.893 → 0.900 | 5.3x advert_bytes | up | 3 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.905 → 0.910 | 0.005 | 0.899 → 0.905 | 1.1x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.905 → 0.910 | 0.005 | 0.899 → 0.905 | 1.1x sr_airtime | up | 4 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.988 → 0.992 | 0.005 | 0.900 → 0.902 | 2.4x sr_bytes | up | 4 |
| `SF-resolve` | resolve | **text** | 0.905 → 0.909 | 0.004 | 0.900 → 0.905 | 5.7x advert_bytes | = | 3 |
| `SF-replay-order` | replay-ordering | **held** | 0.988 → 0.991 | 0.003 | 0.894 → 0.900 | 1.2x sr_bytes | down | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.990 → 0.993 | 0.003 | 0.899 → 0.903 | 2.1x sr_bytes | up | 2 |
| `SF-capacity-window` | capacity | **text** | 0.907 → 0.910 | 0.003 | 0.901 → 0.905 | 3.2x advert_bytes | up | 3 |
| `PR-repeats` | extra-repeats | **text** | 0.905 → 0.908 | 0.003 | 0.900 → 0.904 | 1x sr_airtime | up | 2 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.885 → 0.887 | 0.002 | 0.885 → 0.887 | 1.1x sr_airtime | up | 2 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.885 → 0.887 | 0.002 | 0.885 → 0.887 | 1x sr_bytes | down | 2 |
| `SF-advert-transport` | advert-transport | **text** | 0.905 → 0.907 | 0.002 | 0.900 → 0.901 | 3x sr_airtime | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.990 → 0.992 | 0.002 | 0.898 → 0.900 | 1.2x sr_bytes | up | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.998 → 0.999 | 0.001 | 0.952 → 0.952 | 1x bytes_on_air | down | 2 |
| `TH-congestion-mode` | congestion-mode | **held** | 0.999 → 0.999 | 0.000 | 0.952 → 0.952 | 1x sr_airtime | up | 2 |

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
| none | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| sprinkled | 1 | 0.916 | 0.908 | 0.008 | - | - | 0.982 | 0.983 | 0.403 | 1.02x | 16.1/22.2/26.3% | 1.4/5.1% | 3 |
| arms-race | 1 | 0.958 | 0.957 | 0.001 | - | - | 0.986 | 0.986 | 0.532 | 0.93x | 20.1/25.3/28.8% | 0.9/5.2% | 3 |

> faster: 0.785 s per simulated hour against 1.59 over 73 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `AD-amplify-worst` - amplify-worst  `--scenario rolling`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 0.1 | 1 | 0.923 | 0.918 | 0.005 | - | - | 0.992 | 0.993 | 0.707 | 1.15x | 17.1/23.2/29.1% | 1.6/5.2% | 3 |
| 0.3 | 1 | 0.968 | 0.966 | 0.002 | - | - | 0.998 | 0.998 | 0.903 | 0.92x | 20.9/25.4/28.8% | 1.0/5.3% | 3 |

### `AD-badrouters` - role-placement  `--scenario rolling`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.975 | 0.975 | 0.627 | 1.06x | 14.2/20.5/28.5% | 1.4/5.2% | 3 |
| inverse | 1 | 0.849 | 0.837 | 0.013 | - | - | 0.978 | 0.979 | 0.639 | 1.12x | 13.3/18.1/23.4% | 1.8/4.2% | 3 |
| random | 1 | 0.756 | 0.741 | 0.015 | - | - | 0.922 | 0.923 | 0.299 | 1.03x | 13.3/18.2/25.1% | 1.6/4.8% | 3 |

### `AD-flooding` - role-mix  `--scenario rolling`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.975 | 0.975 | 0.627 | 1.06x | 14.2/20.5/28.5% | 1.4/5.2% | 3 |
| all-routers | 1 | 0.946 | 0.945 | 0.001 | - | - | 0.992 | 0.992 | 0.816 | 2.77x | 32.7/39.4/44.7% | 4.5/5.2% | 3 |

### `AD-nomute` - role-mix  `--scenario rolling`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.975 | 0.975 | 0.627 | 1.06x | 14.2/20.5/28.5% | 1.4/5.2% | 3 |
| no-mute | 1 | 0.887 | 0.879 | 0.008 | - | - | 0.988 | 0.988 | 0.638 | 1.26x | 15.8/21.7/26.7% | 1.7/5.2% | 3 |
| all-routers | 1 | 0.946 | 0.945 | 0.001 | - | - | 0.992 | 0.992 | 0.816 | 2.77x | 32.7/39.4/44.7% | 4.5/5.2% | 3 |

### `AD-siting` - siting-mix  `--scenario rolling`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.975 | 0.975 | 0.627 | 1.06x | 14.2/20.5/28.5% | 1.4/5.2% | 3 |
| local-typical | 1 | 0.625 | 0.603 | 0.021 | - | - | 0.813 | 0.855 | 0.000 | 1.16x | 11.2/20.6/25.5% | 1.7/5.2% | 3 |
| basement-heavy | 1 | 0.042 | 0.042 | 0.000 | - | - | 0.024 | 0.036 | 0.000 | 0.44x | 1.0/3.8/9.3% | 0.4/2.4% | 3 |

> siting-mix=local-typical: decode_failures 30

### `AD-worst` - role-placement  `--scenario rolling`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.785 | 0.766 | 0.019 | - | - | 0.881 | 0.914 | 0.000 | 2.42x | 15.9/26.9/33.5% | 1.9/5.9% | 3 |
| inverse | 1 | 0.758 | 0.727 | 0.031 | - | - | 0.877 | 0.920 | 0.000 | 2.32x | 14.7/23.1/33.4% | 1.8/3.4% | 3 |

> role-placement=degree: decode_failures 87

> role-placement=inverse: decode_failures 101

> slower: 24.9 s per simulated hour against 3.48 over 73 prior run(s) - 7.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `BL-control` - protocol  `--scenario rolling`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.902 | 0.902 | 0.000 | - | - | 0 | 0.000 | 0.694 | 1.21x | 14.7/22.6/28.2% | 1.6/5.0% | 3 |
| sr | 1 | 0.909 | 0.897 | 0.011 | - | - | 0.985 | 0.985 | 0.715 | 1.25x | 15.2/23.4/29.1% | 1.7/5.1% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario rolling`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.854 | 0.846 | 0.008 | - | - | 0.952 | 0.955 | 0.668 | 3.02x | 38.9/53.8/64.4% | 4.0/10.4% | 3 |
| 100 | 1 | 0.939 | 0.937 | 0.002 | - | - | 0.990 | 0.990 | 0.758 | 1.49x | 19.8/28.6/35.2% | 1.8/5.3% | 3 |
| 120 | 1 | 0.939 | 0.937 | 0.002 | - | - | 0.990 | 0.990 | 0.758 | 1.49x | 19.8/28.6/35.2% | 1.8/5.3% | 3 |
| 250 | 1 | 0.939 | 0.937 | 0.002 | - | - | 0.990 | 0.990 | 0.758 | 1.49x | 19.8/28.6/35.2% | 1.8/5.3% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario rolling`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.339 | 0.333 | 0.006 | - | - | 0.382 | 0.411 | 0.137 | 11.67x | 43.1/64.7/73.1% | 4.0/11.4% | 3 |
| 120 | 1 | 0.561 | 0.552 | 0.009 | - | - | 0.615 | 0.639 | 0.192 | 4.49x | 17.3/29.3/37.3% | 1.5/5.1% | 3 |
| 250 | 1 | 0.568 | 0.560 | 0.008 | - | - | 0.608 | 0.636 | 0.194 | 4.37x | 16.8/28.4/35.9% | 1.4/5.0% | 3 |

> max-num-nodes=10: decode_failures 52

> max-num-nodes=120: decode_failures 51

> max-num-nodes=250: decode_failures 59

### `DB-platform` - platform-mix  `--scenario rolling`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.939 | 0.937 | 0.002 | - | - | 0.990 | 0.990 | 0.758 | 1.49x | 19.8/28.6/35.2% | 1.8/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.939 | 0.937 | 0.002 | - | - | 0.990 | 0.990 | 0.758 | 1.49x | 19.8/28.6/35.2% | 1.8/5.3% | 3 |
| constrained | 1 | 0.854 | 0.843 | 0.011 | - | - | 0.955 | 0.956 | 0.660 | 3.02x | 39.0/53.8/64.5% | 4.1/10.4% | 3 |

> platform-mix=constrained: decode_failures 1

### `DB-warm` - warm-num-nodes  `--scenario rolling`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.723 | 0.715 | 0.008 | - | - | 0.892 | 0.932 | 0.542 | 5.45x | 57.8/75.9/80.6% | 3.9/12.1% | 3 |
| 25 | 1 | 0.723 | 0.715 | 0.008 | - | - | 0.892 | 0.932 | 0.542 | 5.45x | 57.8/75.9/80.6% | 3.9/12.1% | 3 |
| 100 | 1 | 0.723 | 0.715 | 0.008 | - | - | 0.892 | 0.932 | 0.542 | 5.45x | 57.8/75.9/80.6% | 3.9/12.1% | 3 |
| 2000 | 1 | 0.723 | 0.715 | 0.008 | - | - | 0.892 | 0.932 | 0.542 | 5.45x | 57.8/75.9/80.6% | 3.9/12.1% | 3 |

> warm-num-nodes=0: queue drops 16.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 114

> warm-num-nodes=25: queue drops 16.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 114

> warm-num-nodes=100: queue drops 16.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 114

> warm-num-nodes=2000: queue drops 16.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 114

### `DG-burst` - burst-loss  `--scenario rolling`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 0.1 | 1 | 0.815 | 0.798 | 0.017 | - | - | 0.977 | 0.981 | 0.622 | 1.17x | 14.6/22.6/28.0% | 1.6/4.7% | 3 |
| 0.2 | 1 | 0.707 | 0.674 | 0.033 | - | - | 0.923 | 0.940 | 0.494 | 1.14x | 14.5/22.7/27.8% | 1.6/4.4% | 3 |
| 0.3 | 1 | 0.620 | 0.576 | 0.043 | - | - | 0.887 | 0.924 | 0.383 | 1.04x | 13.2/20.9/26.1% | 1.5/4.0% | 3 |

> burst-loss=0.2: decode_failures 3

> burst-loss=0.3: decode_failures 19

### `DG-loss` - extra-loss  `--scenario rolling`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 0.1 | 1 | 0.882 | 0.875 | 0.007 | - | - | 0.987 | 0.987 | 0.662 | 1.34x | 16.7/25.4/30.6% | 1.8/5.2% | 3 |
| 0.2 | 1 | 0.838 | 0.826 | 0.011 | - | - | 0.973 | 0.974 | 0.591 | 1.40x | 17.6/26.5/31.8% | 2.0/5.1% | 3 |
| 0.3 | 1 | 0.791 | 0.773 | 0.018 | - | - | 0.950 | 0.956 | 0.506 | 1.42x | 17.9/26.4/32.4% | 2.1/4.8% | 3 |

### `DG-outage` - burst-loss  `--scenario rolling`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 0.1 | 1 | 0.806 | 0.791 | 0.015 | - | - | 0.963 | 0.968 | 0.592 | 1.21x | 15.0/23.2/28.6% | 1.6/5.0% | 3 |
| 0.2 | 1 | 0.694 | 0.675 | 0.018 | - | - | 0.873 | 0.959 | 0.502 | 1.13x | 14.4/22.4/27.5% | 1.6/4.6% | 3 |
| 0.3 | 1 | 0.579 | 0.555 | 0.025 | - | - | 0.739 | 0.876 | 0.331 | 1.07x | 13.8/21.8/27.0% | 1.5/4.3% | 3 |

> burst-loss=0.1: decode_failures 12

> burst-loss=0.2: decode_failures 30

> burst-loss=0.3: decode_failures 27

### `DM-mode` - dm-mode  `--scenario rolling`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.875 | 0.875 | 0.000 | - | - | 0.976 | 0.978 | 0.673 | 1.65x | 20.0/30.7/38.2% | 2.2/6.8% | 3 |
| directed-with-late-flood | 1 | 0.885 | 0.885 | 0.000 | - | - | 0.988 | 0.989 | 0.689 | 1.51x | 18.5/28.6/35.6% | 2.0/6.3% | 3 |
| m4-early-flood | 1 | 0.887 | 0.887 | 0.000 | - | - | 0.984 | 0.986 | 0.706 | 1.51x | 18.6/28.6/35.5% | 2.0/6.2% | 3 |

> faster: 1.24 s per simulated hour against 3.06 over 73 prior run(s) - 2.5x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `FW-firmware` - profile  `--scenario rolling`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.915 | 0.908 | 0.007 | - | - | 0.989 | 0.990 | 0.636 | 0.69x | 8.8/11.5/13.2% | 1.2/1.9% | 3 |
| 2.8 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario rolling`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 0.25 | 1 | 0.920 | 0.913 | 0.007 | - | - | 0.989 | 0.990 | 0.722 | 1.15x | 15.5/22.0/24.4% | 1.8/4.7% | 3 |
| 0.5 | 1 | 0.889 | 0.880 | 0.009 | - | - | 0.993 | 0.993 | 0.552 | 0.96x | 12.9/17.5/18.7% | 1.5/4.1% | 3 |
| 0.75 | 1 | 0.902 | 0.897 | 0.006 | - | - | 0.993 | 0.994 | 0.627 | 0.86x | 10.9/14.7/17.2% | 1.4/3.1% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario rolling`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 0.25 | 1 | 0.914 | 0.907 | 0.007 | - | - | 0.987 | 0.987 | 0.752 | 1.16x | 15.5/21.8/24.2% | 1.8/4.8% | 3 |
| 0.5 | 1 | 0.881 | 0.869 | 0.012 | - | - | 0.989 | 0.989 | 0.537 | 0.95x | 12.9/17.6/19.0% | 1.4/4.1% | 3 |
| 0.75 | 1 | 0.901 | 0.895 | 0.007 | - | - | 0.993 | 0.995 | 0.660 | 0.83x | 10.7/14.4/16.9% | 1.2/3.1% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario rolling`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.921 | 0.919 | 0.002 | - | - | 0.995 | 0.995 | 0.736 | 0.66x | 8.4/13.3/16.9% | 0.8/3.0% | 3 |
| signing=true | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |

> profile-flag=signing=false: misdecodes 1

### `FW-versions` - profile  `--scenario rolling`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.912 | 0.906 | 0.005 | - | - | 0.991 | 0.992 | 0.613 | 0.69x | 9.3/12.6/14.9% | 1.2/2.1% | 3 |
| 2.5 | 1 | 0.909 | 0.904 | 0.005 | - | - | 0.986 | 0.987 | 0.594 | 0.72x | 9.6/12.9/15.2% | 1.2/2.1% | 3 |
| 2.6 | 1 | 0.909 | 0.905 | 0.004 | - | - | 0.989 | 0.990 | 0.589 | 0.70x | 9.6/13.1/15.7% | 1.1/2.2% | 3 |
| 2.7 | 1 | 0.917 | 0.914 | 0.003 | - | - | 0.989 | 0.990 | 0.578 | 0.70x | 9.5/14.5/16.9% | 1.1/3.1% | 3 |
| 2.8 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.928 | 0.925 | 0.003 | - | - | 0.996 | 0.996 | 0.753 | 0.83x | 10.1/15.5/19.2% | 1.1/3.5% | 3 |
| 900 | 1 | 0.873 | 0.865 | 0.008 | - | - | 0.975 | 0.976 | 0.671 | 2.01x | 24.2/37.2/46.0% | 2.7/8.2% | 3 |
| 300 | 1 | 0.630 | 0.615 | 0.016 | - | - | 0.798 | 0.866 | 0.458 | 4.54x | 52.4/70.9/79.4% | 6.4/15.9% | 3 |

> broadcast-interval-s=900: misdecodes 1

> broadcast-interval-s=300: decode_failures 28

### `LD-chatty-hops` - broadcast-interval-s  `--scenario rolling`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.937 | 0.936 | 0.001 | - | - | 0.986 | 0.986 | 0.789 | 0.93x | 11.3/16.6/20.5% | 1.3/3.6% | 3 |
| 900 | 1 | 0.903 | 0.897 | 0.006 | - | - | 0.966 | 0.967 | 0.743 | 2.22x | 26.4/39.6/48.5% | 3.0/8.5% | 3 |
| 300 | 1 | 0.606 | 0.592 | 0.015 | - | - | 0.770 | 0.801 | 0.438 | 4.96x | 55.9/72.8/80.1% | 7.2/17.1% | 3 |

> broadcast-interval-s=300: decode_failures 11

### `LD-diurnal` - diurnal  `--scenario rolling`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.917 | 0.915 | 0.002 | - | - | 0.990 | 0.992 | 0.724 | 1.15x | 14.1/21.7/27.1% | 1.5/4.9% | 3 |
| sinusoid | 1 | 0.911 | 0.907 | 0.004 | - | - | 0.991 | 0.991 | 0.708 | 1.14x | 14.0/21.3/26.7% | 1.4/4.7% | 3 |
| commuter | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.873 | 0.865 | 0.008 | - | - | 0.975 | 0.976 | 0.671 | 2.01x | 24.2/37.2/46.0% | 2.7/8.2% | 3 |
| 3600 | 1 | 0.928 | 0.925 | 0.003 | - | - | 0.996 | 0.996 | 0.753 | 0.83x | 10.1/15.5/19.2% | 1.1/3.5% | 3 |
| 10800 | 1 | 0.927 | 0.924 | 0.003 | - | - | 0.996 | 0.996 | 0.747 | 0.56x | 6.9/10.3/12.7% | 0.7/2.3% | 3 |
| 43200 | 1 | 0.934 | 0.932 | 0.002 | - | - | 0.998 | 0.998 | 0.773 | 0.41x | 4.9/7.4/9.2% | 0.5/1.7% | 3 |

> broadcast-interval-s=900: misdecodes 1

### `LD-traceroute` - traceroute-per-hour  `--scenario rolling`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 0.25 | 1 | 0.897 | 0.891 | 0.006 | - | - | 0.986 | 0.986 | 0.696 | 1.34x | 16.2/25.1/31.1% | 1.7/5.5% | 3 |
| 1.0 | 1 | 0.900 | 0.891 | 0.009 | - | - | 0.994 | 0.994 | 0.674 | 1.48x | 18.2/28.1/35.0% | 2.0/6.2% | 3 |
| 4.0 | 1 | 0.865 | 0.855 | 0.010 | - | - | 0.977 | 0.978 | 0.657 | 1.86x | 23.0/35.4/44.0% | 2.6/7.8% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario rolling`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.723 | 0.715 | 0.008 | - | - | 0.892 | 0.932 | 0.542 | 5.45x | 57.8/75.9/80.6% | 3.9/12.1% | 3 |
| 1.0 | 1 | 0.646 | 0.637 | 0.008 | - | - | 0.827 | 0.891 | 0.465 | 5.96x | 62.2/76.9/81.0% | 4.5/12.9% | 3 |

> traceroute-per-hour=0.0: queue drops 16.9% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 114

> traceroute-per-hour=1.0: queue drops 25.7% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 116

### `MS-density` - nodes  `--scenario rolling`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.726 | 0.711 | 0.015 | - | - | 0.855 | 0.858 | 0.516 | 1.35x | 18.2/27.3/35.9% | 3.2/7.0% | 3 |
| 60 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 90 | 1 | 0.935 | 0.930 | 0.005 | - | - | 0.991 | 0.991 | 0.610 | 1.50x | 18.1/29.7/32.7% | 1.3/4.7% | 3 |
| 120 | 1 | 0.955 | 0.952 | 0.003 | - | - | 0.999 | 1.000 | 0.838 | 2.03x | 22.9/41.0/46.3% | 1.3/4.7% | 3 |
| 150 | 1 | 0.971 | 0.970 | 0.001 | - | - | 1.000 | 1.000 | 0.870 | 2.44x | 28.2/40.9/44.9% | 1.2/5.6% | 3 |

### `MS-hopscale` - nodes  `--scenario rolling`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 120 | 1 | 0.796 | 0.783 | 0.013 | - | - | 0.984 | 0.984 | 0.000 | 2.16x | 15.9/28.3/33.0% | 1.5/5.0% | 3 |
| 250 | 1 | 0.560 | 0.552 | 0.009 | - | - | 0.602 | 0.631 | 0.207 | 4.78x | 18.3/31.1/39.5% | 1.6/5.5% | 3 |
| 500 | 1 | 0.314 | 0.311 | 0.003 | - | - | 0.388 | 0.388 | 0.060 | 10.15x | 19.5/28.5/41.1% | 1.8/6.1% | 3 |

> nodes=250: decode_failures 85

> nodes=500: decode_failures 1

### `MS-oversubscribed` - nodes  `--scenario rolling`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.807 | 0.797 | 0.010 | - | - | 0.986 | 0.986 | 0.000 | 1.99x | 14.5/26.0/30.5% | 1.4/4.5% | 3 |
| 250 | 1 | 0.561 | 0.552 | 0.009 | - | - | 0.615 | 0.639 | 0.192 | 4.49x | 17.3/29.3/37.3% | 1.5/5.1% | 3 |
| 500 | 1 | 0.315 | 0.312 | 0.003 | - | - | 0.390 | 0.390 | 0.065 | 9.45x | 18.3/26.4/37.4% | 1.6/5.5% | 3 |

> nodes=250: decode_failures 51

### `MS-roles` - role-mix  `--scenario rolling`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.898 | 0.893 | 0.005 | - | - | 0.982 | 0.982 | 0.656 | 1.24x | 15.0/23.0/28.6% | 1.6/5.1% | 3 |
| baymesh-2026-08 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.975 | 0.975 | 0.627 | 1.06x | 14.2/20.5/28.5% | 1.4/5.2% | 3 |

### `MS-roles-fav` - role-mix  `--scenario rolling`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.907 | 0.900 | 0.007 | - | - | 0.982 | 0.984 | 0.695 | 1.30x | 16.0/24.0/29.7% | 1.8/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.880 | 0.875 | 0.005 | - | - | 0.962 | 0.964 | 0.714 | 1.23x | 16.6/23.0/31.9% | 2.0/5.2% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario rolling`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 0.05 | 1 | 0.915 | 0.910 | 0.005 | - | - | 0.988 | 0.989 | 0.697 | 1.41x | 18.8/27.8/34.1% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.919 | 0.916 | 0.003 | - | - | 0.986 | 0.986 | 0.706 | 1.50x | 20.0/28.6/37.1% | 1.9/5.2% | 3 |
| 0.2 | 1 | 0.927 | 0.923 | 0.004 | - | - | 0.986 | 0.986 | 0.669 | 1.69x | 22.7/31.6/39.5% | 2.4/5.2% | 3 |

> router-late-fraction=0.1: misdecodes 1

### `MS-siting` - siting-mix  `--scenario rolling`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| local-typical | 1 | 0.661 | 0.647 | 0.013 | - | - | 0.855 | 0.856 | 0.000 | 1.39x | 12.3/20.8/27.1% | 2.2/5.2% | 3 |
| event | 1 | 0.409 | 0.403 | 0.006 | - | - | 0.593 | 0.630 | 0.000 | 1.22x | 8.4/15.3/22.6% | 1.9/5.1% | 3 |
| backbone | 1 | 0.974 | 0.973 | 0.001 | - | - | 0.999 | 1.000 | 0.712 | 1.07x | 25.4/34.1/36.5% | 1.2/5.6% | 3 |

> siting-mix=event: decode_failures 26

> siting-mix=backbone: misdecodes 1

### `MS-size` - nodes  `--scenario rolling`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.898 | 0.891 | 0.007 | - | - | 0.976 | 0.978 | 0.791 | 1.48x | 26.6/32.9/41.4% | 3.5/7.6% | 3 |
| 60 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 90 | 1 | 0.861 | 0.855 | 0.006 | - | - | 0.987 | 0.988 | 0.451 | 1.62x | 16.4/23.9/26.9% | 1.6/5.1% | 3 |
| 120 | 1 | 0.796 | 0.783 | 0.013 | - | - | 0.984 | 0.984 | 0.000 | 2.16x | 15.9/28.3/33.0% | 1.5/5.0% | 3 |
| 150 | 1 | 0.730 | 0.708 | 0.022 | - | - | 0.952 | 0.966 | 0.468 | 2.81x | 16.5/26.2/33.4% | 1.5/5.9% | 3 |

> nodes=150: decode_failures 92

> slower: 8.46 s per simulated hour against 3.42 over 73 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-stretch` - stretch  `--scenario rolling`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 1.25 | 1 | 0.771 | 0.748 | 0.023 | - | - | 0.912 | 0.913 | 0.489 | 1.31x | 12.1/18.4/25.5% | 2.1/4.8% | 3 |
| 1.5 | 1 | 0.444 | 0.438 | 0.007 | - | - | 0.531 | 0.541 | 0.000 | 1.27x | 10.8/15.2/18.7% | 2.1/4.3% | 3 |
| 2.0 | 1 | 0.111 | 0.111 | 0.001 | - | - | 0.188 | 0.217 | 0.000 | 0.77x | 4.4/10.1/14.0% | 1.1/3.0% | 3 |

### `MS-topology` - topology  `--scenario rolling`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| clustered | 1 | 0.975 | 0.972 | 0.003 | - | - | 0.998 | 0.999 | 0.816 | 0.96x | 27.0/32.3/33.8% | 1.0/5.6% | 3 |
| corridor | 1 | 0.615 | 0.588 | 0.027 | - | - | 0.741 | 0.742 | 0.426 | 1.20x | 15.3/19.7/21.5% | 1.8/4.8% | 3 |
| hub | 1 | 0.951 | 0.949 | 0.002 | - | - | 0.989 | 0.990 | 0.799 | 1.15x | 25.3/35.7/37.2% | 1.5/5.4% | 3 |

> topology=corridor: decode_failures 2

### `PR-crladder` - coding-rate-ladder  `--scenario rolling`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.885 | 0.885 | 0.000 | - | - | 0.988 | 0.989 | 0.689 | 1.51x | 18.5/28.6/35.6% | 2.0/6.3% | 3 |
| True | 1 | 0.887 | 0.887 | 0.000 | - | - | 0.989 | 0.990 | 0.663 | 1.51x | 18.6/28.7/35.7% | 2.0/6.3% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario rolling`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.887 | 0.887 | 0.000 | - | - | 0.989 | 0.990 | 0.663 | 1.51x | 18.6/28.7/35.7% | 2.0/6.3% | 3 |
| m4-early-flood | 1 | 0.885 | 0.885 | 0.000 | - | - | 0.987 | 0.987 | 0.703 | 1.50x | 18.3/28.4/35.2% | 1.9/6.2% | 3 |

### `PR-protocol` - protocol  `--scenario rolling`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.902 | 0.902 | 0.000 | - | - | 0 | 0.000 | 0.694 | 1.21x | 14.7/22.6/28.2% | 1.6/5.0% | 3 |
| chain | 1 | 0.897 | 0.896 | 0.002 | - | - | 0.962 | 0.989 | 0.681 | 1.42x | 17.4/27.1/33.7% | 1.8/5.9% | 3 |
| sr | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |

### `PR-repeats` - extra-repeats  `--scenario rolling`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| True | 1 | 0.908 | 0.904 | 0.004 | - | - | 0.993 | 0.993 | 0.734 | 1.26x | 15.5/23.8/29.5% | 1.6/5.2% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario rolling`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.955 | 0.952 | 0.003 | - | - | 0.999 | 1.000 | 0.838 | 2.03x | 22.9/41.0/46.3% | 1.3/4.7% | 3 |
| True | 1 | 0.954 | 0.952 | 0.003 | - | - | 0.998 | 0.998 | 0.834 | 2.08x | 23.5/41.9/47.3% | 1.4/4.8% | 3 |

### `RF-bw500` - preset  `--scenario rolling`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.105 | 0.104 | 0.001 | - | - | 0.140 | 0.140 | 0.000 | 0.04x | 0.2/0.5/0.6% | 0.0/0.1% | 3 |
| MEDIUM_TURBO | 1 | 0.488 | 0.478 | 0.010 | - | - | 0.597 | 0.605 | 0.000 | 0.28x | 2.1/3.3/4.4% | 0.5/1.0% | 3 |
| LONG_TURBO | 1 | 0.840 | 0.825 | 0.015 | - | - | 0.943 | 0.944 | 0.580 | 1.18x | 12.4/18.0/23.7% | 1.7/4.8% | 3 |

> preset=MEDIUM_TURBO: decode_failures 4

### `RF-duct` - duct-per-hour  `--scenario rolling`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 0.25 | 1 | 0.919 | 0.914 | 0.005 | - | - | 0.990 | 0.991 | 0.737 | 1.19x | 17.1/24.5/30.0% | 1.5/5.2% | 3 |
| 1.0 | 1 | 0.943 | 0.939 | 0.004 | - | - | 0.993 | 0.993 | 0.820 | 0.94x | 21.6/27.4/31.8% | 1.1/5.3% | 3 |

### `RF-eu-presets` - preset  `--scenario rolling`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.316 | 0.307 | 0.008 | - | - | 0.420 | 0.442 | 0.000 | 0.13x | 0.9/1.5/2.0% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| LITE_FAST | 1 | 0.876 | 0.867 | 0.009 | - | - | 0.974 | 0.975 | 0.632 | 0.98x | 11.3/16.7/22.4% | 1.3/4.0% | 3 |
| NARROW_SLOW | 1 | 0.890 | 0.879 | 0.011 | - | - | 0.972 | 0.974 | 0.697 | 1.21x | 15.1/20.0/26.4% | 1.8/5.1% | 3 |

> preset=SHORT_FAST: decode_failures 14

### `RF-noise` - noise-profile  `--scenario rolling`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| temporal | 1 | 0.836 | 0.827 | 0.009 | - | - | 0.966 | 0.967 | 0.544 | 1.29x | 15.4/23.5/29.8% | 1.9/5.1% | 3 |
| transient | 1 | 0.897 | 0.891 | 0.006 | - | - | 0.987 | 0.987 | 0.684 | 1.24x | 15.1/23.3/29.2% | 1.6/5.2% | 3 |
| periodic | 1 | 0.743 | 0.736 | 0.007 | - | - | 0.836 | 0.838 | 0.568 | 1.17x | 14.7/22.4/27.6% | 1.6/4.6% | 3 |

### `RF-preset` - preset  `--scenario rolling`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.316 | 0.307 | 0.008 | - | - | 0.420 | 0.442 | 0.000 | 0.13x | 0.9/1.5/2.0% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| LONG_MODERATE | 1 | 0.857 | 0.845 | 0.012 | - | - | 0.943 | 0.950 | 0.695 | 3.20x | 45.5/62.6/65.8% | 4.3/12.1% | 3 |

> preset=SHORT_FAST: decode_failures 14

> preset=LONG_MODERATE: decode_failures 19

### `RF-preset-turbo` - preset  `--scenario rolling`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.039 | 0.039 | 0.000 | - | - | 0.093 | 0.097 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.105 | 0.104 | 0.001 | - | - | 0.140 | 0.140 | 0.000 | 0.04x | 0.2/0.5/0.6% | 0.0/0.1% | 3 |
| LONG_FAST | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| LONG_TURBO | 1 | 0.840 | 0.825 | 0.015 | - | - | 0.943 | 0.944 | 0.580 | 1.18x | 12.4/18.0/23.7% | 1.7/4.8% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.904 | 0.894 | 0.010 | - | - | 0.981 | 0.983 | 0.699 | 1.73x | 21.1/29.1/36.4% | 2.4/7.1% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario rolling`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.841 | 0.835 | 0.007 | - | - | 0.931 | 0.932 | 0.646 | 1.23x | 15.1/23.4/28.9% | 1.6/5.0% | 3 |
| 10000 | 1 | 0.743 | 0.736 | 0.007 | - | - | 0.836 | 0.838 | 0.568 | 1.17x | 14.7/22.4/27.6% | 1.6/4.6% | 3 |
| 4000 | 1 | 0.494 | 0.487 | 0.007 | - | - | 0.585 | 0.617 | 0.300 | 1.05x | 13.2/19.8/24.5% | 1.6/3.6% | 3 |
| 2000 | 1 | 0.121 | 0.121 | 0.000 | - | - | 0.143 | 0.244 | 0.063 | 0.72x | 9.2/13.2/17.6% | 1.1/2.1% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 4

### `RF-stretch-duct` - duct-per-hour  `--scenario rolling`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.444 | 0.438 | 0.007 | - | - | 0.531 | 0.541 | 0.000 | 1.27x | 10.8/15.2/18.7% | 2.1/4.3% | 3 |
| 1.0 | 1 | 0.717 | 0.704 | 0.013 | - | - | 0.780 | 0.780 | 0.358 | 0.91x | 14.1/18.0/22.5% | 1.3/4.4% | 3 |

### `RF-txpower` - tx-power  `--scenario rolling`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 22 | 1 | 0.449 | 0.442 | 0.007 | - | - | 0.516 | 0.523 | 0.000 | 1.40x | 11.2/15.4/19.8% | 2.4/4.8% | 3 |
| 17 | 1 | 0.102 | 0.101 | 0.001 | - | - | 0.135 | 0.144 | 0.000 | 0.79x | 4.5/11.1/13.1% | 1.1/2.6% | 3 |
| 14 | 1 | 0.053 | 0.053 | 0.000 | - | - | 0.047 | 0.114 | 0.000 | 0.49x | 1.9/7.3/10.1% | 0.7/2.3% | 3 |

> tx-power=22: decode_failures 2

> tx-power=17: decode_failures 5

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario rolling`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.955 | 0.952 | 0.003 | - | - | 0.999 | 1.000 | 0.838 | 2.03x | 22.9/41.0/46.3% | 1.3/4.7% | 3 |
| True | 1 | 0.945 | 0.942 | 0.004 | - | - | 0.999 | 0.999 | 0.817 | 2.38x | 26.6/46.5/52.1% | 1.6/5.5% | 3 |

### `RT-favourites` - favourite-routers  `--scenario rolling`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.913 | 0.908 | 0.006 | - | - | 0.991 | 0.992 | 0.696 | 1.38x | 18.4/26.1/32.6% | 1.8/5.3% | 3 |
| True | 1 | 0.922 | 0.918 | 0.004 | - | - | 0.982 | 0.983 | 0.721 | 1.42x | 18.9/26.4/32.8% | 2.0/5.2% | 3 |

### `RT-hopassign` - hop-assign  `--scenario rolling`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| random | 1 | 0.845 | 0.828 | 0.017 | - | - | 0.961 | 0.962 | 0.558 | 1.24x | 15.1/23.1/28.7% | 1.6/5.1% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario rolling`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.742 | 0.712 | 0.031 | - | - | 0.961 | 0.964 | 0.427 | 0.95x | 12.0/19.6/24.9% | 1.3/4.6% | 3 |
| 7 | 1 | 0.928 | 0.927 | 0.002 | - | - | 0.983 | 0.983 | 0.758 | 1.35x | 16.4/24.4/30.3% | 1.8/5.3% | 3 |
| 15 | 1 | 0.931 | 0.931 | 0.000 | - | - | 0.976 | 0.976 | 0.797 | 1.39x | 16.8/24.7/30.8% | 1.9/5.4% | 3 |
| 32 | 1 | 0.931 | 0.931 | 0.000 | - | - | 0.976 | 0.976 | 0.797 | 1.39x | 16.8/24.7/30.8% | 1.9/5.4% | 3 |

### `RT-hopspread` - hop-limit  `--scenario rolling`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.742 | 0.712 | 0.031 | - | - | 0.961 | 0.964 | 0.427 | 0.95x | 12.0/19.6/24.9% | 1.3/4.6% | 3 |
| 5 | 1 | 0.881 | 0.872 | 0.009 | - | - | 0.975 | 0.975 | 0.663 | 1.27x | 15.4/23.7/29.5% | 1.7/5.2% | 3 |
| 7 | 1 | 0.928 | 0.927 | 0.002 | - | - | 0.983 | 0.983 | 0.758 | 1.35x | 16.4/24.4/30.3% | 1.8/5.3% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario rolling`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| KNOWN_ONLY | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.899 | 0.899 | 0.000 | - | - | 0.953 | 0.987 | 0.708 | 1.22x | 14.9/23.0/28.6% | 1.6/5.0% | 3 |

> faster: 0.776 s per simulated hour against 1.55 over 73 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RT-spread` - hop-spread  `--scenario rolling`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.742 | 0.712 | 0.031 | - | - | 0.961 | 0.964 | 0.427 | 0.95x | 12.0/19.6/24.9% | 1.3/4.6% | 3 |
| True | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |

### `SC-signing` - signature-policy  `--scenario rolling`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| BALANCED | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| STRICT | 1 | 0.761 | 0.761 | 0.000 | - | - | 0.858 | 0.858 | 0.536 | 1.39x | 17.0/25.9/32.2% | 1.8/5.7% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario rolling`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| dm | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.992 | 0.992 | 0.715 | 1.23x | 15.0/23.3/29.2% | 1.6/5.2% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario rolling`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.988 | 0.988 | 0.700 | 1.26x | 15.5/23.8/29.6% | 1.6/5.3% | 3 |
| local | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| time | 1 | 0.906 | 0.900 | 0.006 | - | - | 0.992 | 0.992 | 0.713 | 1.29x | 15.7/24.2/30.2% | 1.6/5.4% | 3 |
| window | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.989 | 0.990 | 0.692 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |

> bucket-mode=global: misdecodes 33

> bucket-mode=time: misdecodes 43

> bucket-mode=window: misdecodes 26

### `SF-bucket-time` - time-bucket-s  `--scenario rolling`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.899 | 0.893 | 0.006 | - | - | 0.988 | 0.988 | 0.705 | 1.39x | 17.0/26.4/32.7% | 1.8/5.9% | 3 |
| 1800 | 1 | 0.906 | 0.900 | 0.006 | - | - | 0.992 | 0.992 | 0.713 | 1.29x | 15.7/24.2/30.2% | 1.6/5.4% | 3 |
| 3600 | 1 | 0.902 | 0.897 | 0.005 | - | - | 0.987 | 0.987 | 0.703 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |

> time-bucket-s=600: misdecodes 124

> time-bucket-s=1800: misdecodes 43

> time-bucket-s=3600: misdecodes 16

### `SF-cadence` - trigger  `--scenario rolling`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| interval | 1 | 0.890 | 0.882 | 0.008 | - | - | 0.981 | 0.981 | 0.675 | 1.72x | 21.4/33.5/42.0% | 2.2/8.5% | 3 |
| aimd | 1 | 0.900 | 0.899 | 0.001 | - | - | 0.962 | 0.989 | 0.714 | 1.25x | 15.3/23.6/29.4% | 1.6/5.2% | 3 |
| bucket+interval | 1 | 0.889 | 0.882 | 0.008 | - | - | 0.980 | 0.980 | 0.705 | 1.74x | 21.5/33.8/42.4% | 2.1/8.5% | 3 |

> trigger=interval: misdecodes 23

> trigger=aimd: misdecodes 4

> trigger=bucket+interval: misdecodes 21

> faster: 1.77 s per simulated hour against 3.62 over 73 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-capacity` - capacity  `--scenario rolling`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.903 | 0.899 | 0.004 | - | - | 0.979 | 0.984 | 0.701 | 1.24x | 15.2/23.5/29.5% | 1.6/5.3% | 3 |
| 8 | 1 | 0.902 | 0.898 | 0.005 | - | - | 0.986 | 0.986 | 0.689 | 1.23x | 15.0/23.2/28.9% | 1.6/5.2% | 3 |
| 16 | 1 | 0.903 | 0.897 | 0.006 | - | - | 0.990 | 0.991 | 0.697 | 1.24x | 15.1/23.4/29.1% | 1.6/5.2% | 3 |
| 32 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 50 | 1 | 0.903 | 0.898 | 0.004 | - | - | 0.981 | 0.981 | 0.683 | 1.25x | 15.2/23.5/29.4% | 1.6/5.2% | 3 |

> capacity=4: decode_failures 97

> capacity=8: decode_failures 2

### `SF-capacity-local` - capacity  `--scenario rolling`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.903 | 0.899 | 0.004 | - | - | 0.979 | 0.984 | 0.701 | 1.24x | 15.2/23.5/29.5% | 1.6/5.3% | 3 |
| 8 | 1 | 0.902 | 0.898 | 0.005 | - | - | 0.986 | 0.986 | 0.689 | 1.23x | 15.0/23.2/28.9% | 1.6/5.2% | 3 |
| 16 | 1 | 0.903 | 0.897 | 0.006 | - | - | 0.990 | 0.991 | 0.697 | 1.24x | 15.1/23.4/29.1% | 1.6/5.2% | 3 |
| 32 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 50 | 1 | 0.903 | 0.898 | 0.004 | - | - | 0.981 | 0.981 | 0.683 | 1.25x | 15.2/23.5/29.4% | 1.6/5.2% | 3 |

> capacity=4: decode_failures 97

> capacity=8: decode_failures 2

### `SF-capacity-window` - capacity  `--scenario rolling`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.990 | 0.992 | 0.710 | 1.24x | 15.1/23.4/29.3% | 1.6/5.2% | 3 |
| 16 | 1 | 0.910 | 0.905 | 0.004 | - | - | 0.990 | 0.992 | 0.701 | 1.23x | 15.0/23.1/28.7% | 1.6/5.1% | 3 |
| 32 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.989 | 0.990 | 0.692 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |

> capacity=8: misdecodes 20

> capacity=8: decode_failures 4

> capacity=16: misdecodes 24

> capacity=32: misdecodes 26

> faster: 0.788 s per simulated hour against 1.59 over 73 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-catchup` - catch-up-hours  `--scenario rolling`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.889 | 0.882 | 0.008 | - | - | 0.980 | 0.980 | 0.705 | 1.74x | 21.5/33.8/42.4% | 2.1/8.5% | 3 |
| 02-06 | 1 | 0.903 | 0.901 | 0.002 | - | - | 0.971 | 0.990 | 0.695 | 1.30x | 16.0/24.7/30.8% | 1.7/5.5% | 3 |
| 00-08 | 1 | 0.902 | 0.900 | 0.002 | - | - | 0.972 | 0.989 | 0.709 | 1.37x | 16.8/25.9/32.3% | 1.8/5.8% | 3 |

> catch-up-hours=: misdecodes 21

> catch-up-hours=02-06: decode_failures 25

> catch-up-hours=00-08: misdecodes 1

> catch-up-hours=00-08: decode_failures 24

### `SF-hops-flat` - hops-apart  `--scenario rolling`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.902 | 0.898 | 0.003 | - | - | 0.968 | 0.968 | 0.711 | 1.25x | 15.3/23.4/29.2% | 1.7/5.2% | 3 |
| 2 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 3 | 1 | 0.909 | 0.897 | 0.011 | - | - | 0.985 | 0.985 | 0.715 | 1.25x | 15.2/23.4/29.1% | 1.7/5.1% | 3 |
| 4 | 1 | 0.918 | 0.903 | 0.015 | - | - | 0.993 | 0.995 | 0.703 | 1.26x | 15.4/23.6/29.3% | 1.7/5.2% | 3 |

> faster: 1.68 s per simulated hour against 4.01 over 73 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-hops-spread` - hops-apart  `--scenario rolling`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.902 | 0.898 | 0.003 | - | - | 0.968 | 0.968 | 0.711 | 1.25x | 15.3/23.4/29.2% | 1.7/5.2% | 3 |
| 2 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 3 | 1 | 0.909 | 0.897 | 0.011 | - | - | 0.985 | 0.985 | 0.715 | 1.25x | 15.2/23.4/29.1% | 1.7/5.1% | 3 |
| 4 | 1 | 0.918 | 0.903 | 0.015 | - | - | 0.993 | 0.995 | 0.703 | 1.26x | 15.4/23.6/29.3% | 1.7/5.2% | 3 |
| 5 | 1 | 0.915 | 0.905 | 0.009 | - | - | 0.911 | 0.986 | 0.720 | 1.26x | 15.6/23.5/29.4% | 1.7/5.3% | 3 |

> hops-apart=5: decode_failures 28

### `SF-jitter-global` - advert-jitter-s  `--scenario rolling`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.905 | 0.899 | 0.006 | - | - | 0.990 | 0.991 | 0.703 | 1.25x | 15.2/23.6/29.4% | 1.6/5.2% | 3 |
| 30 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 120 | 1 | 0.905 | 0.901 | 0.005 | - | - | 0.991 | 0.992 | 0.691 | 1.26x | 15.3/23.8/29.6% | 1.7/5.2% | 3 |
| 600 | 1 | 0.910 | 0.905 | 0.005 | - | - | 0.994 | 0.994 | 0.724 | 1.26x | 15.4/23.8/29.6% | 1.6/5.2% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario rolling`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.905 | 0.899 | 0.006 | - | - | 0.990 | 0.991 | 0.703 | 1.25x | 15.2/23.6/29.4% | 1.6/5.2% | 3 |
| 30 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 120 | 1 | 0.905 | 0.901 | 0.005 | - | - | 0.991 | 0.992 | 0.691 | 1.26x | 15.3/23.8/29.6% | 1.7/5.2% | 3 |
| 600 | 1 | 0.910 | 0.905 | 0.005 | - | - | 0.994 | 0.994 | 0.724 | 1.26x | 15.4/23.8/29.6% | 1.6/5.2% | 3 |

### `SF-place-flat` - place  `--scenario rolling`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.920 | 0.898 | 0.021 | - | - | 0.980 | 0.986 | 0.680 | 1.27x | 15.5/23.8/29.8% | 1.7/5.5% | 3 |
| routers | 1 | 0.907 | 0.903 | 0.004 | - | - | 0.990 | 0.990 | 0.704 | 1.26x | 15.4/23.6/29.4% | 1.7/5.3% | 3 |
| alternate-routers | 1 | 0.904 | 0.903 | 0.001 | - | - | 0.979 | 0.980 | 0.700 | 1.25x | 15.1/23.3/29.2% | 1.7/5.2% | 3 |
| beside-router | 1 | 0.912 | 0.908 | 0.004 | - | - | 0.993 | 0.993 | 0.709 | 1.26x | 15.3/23.6/29.4% | 1.7/5.2% | 3 |
| random-clients | 1 | 0.920 | 0.897 | 0.023 | - | - | 0.991 | 0.992 | 0.692 | 1.27x | 15.5/23.7/29.2% | 1.6/5.2% | 3 |
| hops-apart | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |

> place=spread: decode_failures 2

### `SF-place-spread` - place  `--scenario rolling`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.920 | 0.898 | 0.021 | - | - | 0.980 | 0.986 | 0.680 | 1.27x | 15.5/23.8/29.8% | 1.7/5.5% | 3 |
| routers | 1 | 0.907 | 0.903 | 0.004 | - | - | 0.990 | 0.990 | 0.704 | 1.26x | 15.4/23.6/29.4% | 1.7/5.3% | 3 |
| alternate-routers | 1 | 0.904 | 0.903 | 0.001 | - | - | 0.979 | 0.980 | 0.700 | 1.25x | 15.1/23.3/29.2% | 1.7/5.2% | 3 |
| beside-router | 1 | 0.912 | 0.908 | 0.004 | - | - | 0.993 | 0.993 | 0.709 | 1.26x | 15.3/23.6/29.4% | 1.7/5.2% | 3 |
| random-clients | 1 | 0.920 | 0.897 | 0.023 | - | - | 0.991 | 0.992 | 0.692 | 1.27x | 15.5/23.7/29.2% | 1.6/5.2% | 3 |
| hops-apart | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |

> place=spread: decode_failures 2

### `SF-provide-transport` - provide-transport  `--scenario rolling`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| broadcast | 1 | 0.921 | 0.900 | 0.021 | - | - | 0.990 | 0.991 | 0.727 | 1.29x | 15.7/24.3/30.2% | 1.7/5.4% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario rolling`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| heard | 1 | 0.902 | 0.894 | 0.008 | - | - | 0.988 | 0.988 | 0.689 | 1.25x | 15.2/23.5/29.4% | 1.7/5.2% | 3 |

> replay-ordering=heard: misdecodes 16

### `SF-replay-order-broadcast` - replay-ordering  `--scenario rolling`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.921 | 0.900 | 0.021 | - | - | 0.990 | 0.991 | 0.727 | 1.29x | 15.7/24.3/30.2% | 1.7/5.4% | 3 |
| heard | 1 | 0.920 | 0.898 | 0.022 | - | - | 0.992 | 0.992 | 0.730 | 1.28x | 15.6/24.0/29.8% | 1.6/5.3% | 3 |

> replay-ordering=heard: misdecodes 15

### `SF-resolve` - resolve  `--scenario rolling`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| enum | 1 | 0.909 | 0.905 | 0.004 | - | - | 0.989 | 0.990 | 0.709 | 1.24x | 15.1/23.6/29.5% | 1.7/5.3% | 3 |
| hybrid | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |

### `SF-servers-allrouters` - servers  `--scenario rolling`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.907 | 0.903 | 0.004 | - | - | 0.990 | 0.990 | 0.704 | 1.26x | 15.4/23.6/29.4% | 1.7/5.3% | 3 |
| 6 | 1 | 0.906 | 0.899 | 0.006 | - | - | 0.993 | 0.993 | 0.712 | 1.29x | 15.6/24.2/30.0% | 1.7/5.5% | 6 |

### `SF-servers-flat` - servers  `--scenario rolling`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.899 | 0.896 | 0.003 | - | - | 0.981 | 0.984 | 0.714 | 1.23x | 15.1/23.2/28.9% | 1.6/5.1% | 2 |
| 3 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 5 | 1 | 0.905 | 0.898 | 0.008 | - | - | 0.983 | 0.984 | 0.688 | 1.27x | 15.5/24.0/29.9% | 1.7/5.3% | 5 |
| 8 | 1 | 0.906 | 0.897 | 0.010 | - | - | 0.991 | 0.992 | 0.686 | 1.34x | 16.1/25.2/31.0% | 1.8/5.5% | 8 |

> servers=8: misdecodes 1

### `SF-servers-spread` - servers  `--scenario rolling`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.899 | 0.896 | 0.003 | - | - | 0.981 | 0.984 | 0.714 | 1.23x | 15.1/23.2/28.9% | 1.6/5.1% | 2 |
| 3 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 5 | 1 | 0.905 | 0.898 | 0.008 | - | - | 0.983 | 0.984 | 0.688 | 1.27x | 15.5/24.0/29.9% | 1.7/5.3% | 5 |
| 8 | 1 | 0.906 | 0.897 | 0.010 | - | - | 0.991 | 0.992 | 0.686 | 1.34x | 16.1/25.2/31.0% | 1.8/5.5% | 8 |

> servers=8: misdecodes 1

> faster: 1.04 s per simulated hour against 2.21 over 73 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-signed` - signed  `--scenario rolling`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| True | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario rolling`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.909 | 0.904 | 0.005 | - | - | 0.988 | 0.991 | 0.730 | 1.19x | 14.4/22.1/27.5% | 1.6/4.9% | 3 |
| 1 | 1 | 0.903 | 0.899 | 0.004 | - | - | 0.985 | 0.988 | 0.719 | 1.19x | 14.5/22.3/27.6% | 1.5/4.9% | 3 |
| 2 | 1 | 0.901 | 0.895 | 0.006 | - | - | 0.988 | 0.989 | 0.671 | 1.20x | 14.6/22.5/27.8% | 1.5/4.9% | 3 |
| 4 | 1 | 0.906 | 0.902 | 0.004 | - | - | 0.989 | 0.991 | 0.710 | 1.20x | 14.6/22.5/27.7% | 1.5/4.9% | 3 |

### `SF-width` - short-id-bits  `--scenario rolling`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.901 | 0.897 | 0.004 | - | - | 0.987 | 0.987 | 0.702 | 1.25x | 15.3/23.6/29.4% | 1.6/5.3% | 3 |
| 24 | 1 | 0.909 | 0.905 | 0.004 | - | - | 0.992 | 0.992 | 0.718 | 1.25x | 15.3/23.7/29.6% | 1.7/5.2% | 3 |
| 32 | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.991 | 0.992 | 0.718 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |
| 64 | 1 | 0.902 | 0.897 | 0.005 | - | - | 0.989 | 0.989 | 0.704 | 1.26x | 15.4/23.7/29.7% | 1.6/5.3% | 3 |

### `SF-window-size` - window-size  `--scenario rolling`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.897 | 0.890 | 0.007 | - | - | 0.990 | 0.991 | 0.692 | 1.35x | 16.4/25.3/31.6% | 1.8/5.6% | 3 |
| 16 | 1 | 0.905 | 0.899 | 0.006 | - | - | 0.988 | 0.989 | 0.712 | 1.27x | 15.5/23.9/29.9% | 1.7/5.3% | 3 |
| 32 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.989 | 0.990 | 0.692 | 1.25x | 15.2/23.5/29.2% | 1.6/5.2% | 3 |

> window-size=8: misdecodes 148

> window-size=16: misdecodes 62

> window-size=32: misdecodes 26

### `TH-congestion` - no-congestion-scaling  `--scenario rolling`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.955 | 0.952 | 0.003 | - | - | 0.999 | 1.000 | 0.838 | 2.03x | 22.9/41.0/46.3% | 1.3/4.7% | 3 |
| True | 1 | 0.736 | 0.728 | 0.008 | - | - | 0.908 | 0.942 | 0.553 | 5.34x | 57.3/75.3/80.3% | 3.9/11.7% | 3 |

> no-congestion-scaling=True: queue drops 14.6% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 63

### `TH-congestion-input` - congestion-input  `--scenario rolling`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.561 | 0.552 | 0.009 | - | - | 0.615 | 0.639 | 0.192 | 4.49x | 17.3/29.3/37.3% | 1.5/5.1% | 3 |
| truesize | 1 | 0.597 | 0.589 | 0.009 | - | - | 0.655 | 0.666 | 0.198 | 3.51x | 13.7/23.4/30.0% | 1.1/4.4% | 3 |

> congestion-input=hotstore: decode_failures 51

> congestion-input=truesize: decode_failures 13

### `TH-congestion-mode` - congestion-mode  `--scenario rolling`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.955 | 0.952 | 0.003 | - | - | 0.999 | 1.000 | 0.822 | 1.97x | 22.0/39.8/44.9% | 1.3/4.7% | 3 |
| adaptive | 1 | 0.955 | 0.952 | 0.003 | - | - | 0.999 | 1.000 | 0.838 | 2.03x | 22.9/41.0/46.3% | 1.3/4.7% | 3 |

