# Sweep blocks-2026-10-30-9979272

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** alpine
- **seed base** 9979272 · seeds 9979272
- **blocks** 87 run
- **compute** 9.2 h of simulator time across every cell
- **generated** 2026-10-30T10:01:08+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>89 warnings</summary>

- AD-amplify-worst: amplify-worst=0.1: decode_failures 56
- AD-amplify-worst: slower: 5.53 s per simulated hour against 1.79 over 70 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-badrouters: role-placement=random: misdecodes 1
- AD-badrouters: role-placement=random: decode_failures 3
- AD-siting: siting-mix=local-typical: decode_failures 28
- AD-siting: siting-mix=basement-heavy: decode_failures 6
- AD-siting: slower: 3.4 s per simulated hour against 1.42 over 70 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-worst: role-placement=degree: decode_failures 3
- BL-control: protocol=sr: decode_failures 25
- BL-control: slower: 3.9 s per simulated hour against 1.81 over 70 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 41
- DB-hotstore-stress: max-num-nodes=250: decode_failures 3
- DB-warm: warm-num-nodes=0: queue drops 10.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 86
- DB-warm: warm-num-nodes=25: queue drops 10.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 86
- DB-warm: warm-num-nodes=100: queue drops 10.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 86
- DB-warm: warm-num-nodes=2000: queue drops 10.9% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 86
- DG-burst: burst-loss=0.2: decode_failures 2
- DG-burst: burst-loss=0.3: decode_failures 32
- DG-outage: burst-loss=0.1: decode_failures 41
- DG-outage: burst-loss=0.2: decode_failures 38
- DG-outage: burst-loss=0.3: decode_failures 28
- FW-mixed-26: legacy-fraction=0.5: decode_failures 40
- FW-mixed: legacy-fraction=0.5: decode_failures 39
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 6
- LD-chatty: broadcast-interval-s=300: decode_failures 29
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 10.9% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 86
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 19.2% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 93
- MS-density: nodes=90: misdecodes 1
- MS-density: nodes=120: misdecodes 1
- MS-siting: siting-mix=local-typical: decode_failures 2
- MS-size: nodes=150: decode_failures 18
- MS-stretch: faster: 1.02 s per simulated hour against 2.1 over 70 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-topology: topology=corridor: decode_failures 7
- MS-topology: topology=hub: misdecodes 1
- PR-repeats-busy: extra-repeats=False: misdecodes 1
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 2
- RF-preset: faster: 1.24 s per simulated hour against 2.77 over 70 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 1
- RF-txpower: tx-power=22: decode_failures 1
- RF-txpower: tx-power=14: decode_failures 5
- RT-adopt: no-adopt-hop-recommendation=False: misdecodes 1
- SF-bucket-mode: bucket-mode=global: misdecodes 35
- SF-bucket-mode: bucket-mode=time: misdecodes 26
- SF-bucket-mode: bucket-mode=window: misdecodes 29
- SF-bucket-time: time-bucket-s=600: misdecodes 127
- SF-bucket-time: time-bucket-s=1800: misdecodes 26
- SF-bucket-time: time-bucket-s=3600: misdecodes 11
- SF-cadence: trigger=interval: misdecodes 15
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=bucket+interval: misdecodes 17
- SF-capacity-local: capacity=4: decode_failures 97
- SF-capacity-local: capacity=8: decode_failures 34
- SF-capacity: capacity=4: decode_failures 97
- SF-capacity: capacity=8: decode_failures 34
- SF-capacity-window: capacity=8: misdecodes 16
- SF-capacity-window: capacity=8: decode_failures 44
- SF-capacity-window: capacity=16: misdecodes 16
- SF-capacity-window: capacity=32: misdecodes 29
- SF-catchup: catch-up-hours=: misdecodes 17
- SF-catchup: catch-up-hours=02-06: decode_failures 2
- SF-catchup: catch-up-hours=00-08: misdecodes 1
- SF-catchup: catch-up-hours=00-08: decode_failures 2
- SF-catchup: faster: 3.47 s per simulated hour against 9.05 over 70 prior run(s) - 2.6x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-hops-flat: hops-apart=3: decode_failures 25
- SF-hops-flat: hops-apart=4: decode_failures 28
- SF-hops-spread: hops-apart=3: decode_failures 25
- SF-hops-spread: hops-apart=4: decode_failures 28
- SF-hops-spread: hops-apart=5: decode_failures 34
- SF-place-flat: place=spread: decode_failures 22
- SF-place-spread: place=spread: decode_failures 22
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 9
- SF-replay-order: replay-ordering=heard: misdecodes 21
- SF-servers-flat: servers=5: misdecodes 1
- SF-servers-flat: servers=8: misdecodes 1
- SF-servers-spread: servers=5: misdecodes 1
- SF-servers-spread: servers=8: misdecodes 1
- SF-window-size: window-size=8: misdecodes 118
- SF-window-size: window-size=16: misdecodes 60
- SF-window-size: window-size=32: misdecodes 29
- TH-congestion-input: congestion-input=truesize: decode_failures 78
- TH-congestion-mode: congestion-mode=adaptive: misdecodes 1
- TH-congestion: no-congestion-scaling=False: misdecodes 1
- TH-congestion: no-congestion-scaling=True: decode_failures 62

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `AD-amplify-worst` | 5.53 | 1.79 | 3.08x | 70 |
| `AD-siting` | 3.4 | 1.42 | 2.39x | 70 |
| `BL-control` | 3.9 | 1.81 | 2.16x | 70 |
| `TH-congestion-input` | 20.1 | 10.2 | 1.97x | 70 |
| `FW-mixed` | 3.03 | 1.67 | 1.81x | 70 |
| `DB-platform` | 1.62 | 2.41 | 0.67x | 70 |
| `RT-hopspread` | 1.32 | 2.03 | 0.65x | 70 |
| `PR-crladder` | 1.78 | 2.79 | 0.64x | 70 |
| `RF-stretch-duct` | 1.16 | 1.82 | 0.64x | 70 |
| `SF-window-size` | 0.862 | 1.37 | 0.63x | 70 |
| `RF-eu-presets` | 1.13 | 1.82 | 0.62x | 70 |
| `LD-chatty-hops` | 2.27 | 3.8 | 0.60x | 70 |
| `RT-adopt` | 2.31 | 3.89 | 0.59x | 70 |
| `MS-oversubscribed` | 11.5 | 19.6 | 0.59x | 70 |
| `SF-place-flat` | 1.59 | 2.74 | 0.58x | 70 |
| `RF-noise` | 2.8 | 4.93 | 0.57x | 70 |
| `DM-mode` | 1.63 | 2.89 | 0.56x | 70 |
| `MS-hopscale` | 9.54 | 17.1 | 0.56x | 70 |
| `AD-flooding` | 1.33 | 2.42 | 0.55x | 70 |
| `TH-congestion` | 9.18 | 17.1 | 0.54x | 70 |
| `MS-stretch` | 1.02 | 2.1 | 0.49x | 70 |
| `RF-preset` | 1.24 | 2.77 | 0.45x | 70 |
| `SF-catchup` | 3.47 | 9.05 | 0.38x | 70 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.970 | 0.970 | 0.827 → 0.832 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.924 | 0.924 | 0.827 → 0.832 | 1x bytes_on_air | up | 2 |
| `MS-siting` | siting-mix | **text** | 0.145 → 0.978 | 0.833 | 0.142 → 0.977 | 4.2x sr_airtime | up | 4 |
| `RF-preset-turbo` | preset | **held** | 0.147 → 0.970 | 0.823 | 0.073 → 0.829 | 8x sr_airtime | up | 5 |
| `MS-stretch` | stretch | **held** | 0.176 → 0.970 | 0.794 | 0.132 → 0.829 | 10x sr_airtime | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.126 → 0.908 | 0.782 | 0.096 → 0.769 | 1e+02x sr_airtime | down | 4 |
| `RF-txpower` | tx-power | **text** | 0.105 → 0.837 | 0.732 | 0.102 → 0.829 | 3.7x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **text** | 0.135 → 0.799 | 0.665 | 0.133 → 0.786 | 5.5x sr_bytes | down | 3 |
| `MS-hopscale` | nodes | **held** | 0.336 → 0.976 | 0.640 | 0.330 → 0.829 | 8.4x bytes_on_air | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.353 → 0.981 | 0.627 | 0.330 → 0.734 | 4.6x bytes_on_air | down | 3 |
| `RF-bw500` | preset | **text** | 0.202 → 0.772 | 0.570 | 0.200 → 0.766 | 2.1x advert_bytes | up | 3 |
| `RF-eu-presets` | preset | **text** | 0.317 → 0.837 | 0.519 | 0.309 → 0.829 | 2.3x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.317 → 0.837 | 0.519 | 0.309 → 0.829 | 2.8x sr_airtime | up | 3 |
| `MS-topology` | topology | **text** | 0.524 → 0.940 | 0.416 | 0.507 → 0.939 | 2.1x sr_bytes | up | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.581 → 0.916 | 0.335 | 0.562 → 0.914 | 7.2x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.506 → 0.837 | 0.330 | 0.477 → 0.829 | 2.4x sr_bytes | down | 4 |
| `DG-burst` | burst-loss | **text** | 0.522 → 0.837 | 0.314 | 0.485 → 0.829 | 2.2x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.557 → 0.871 | 0.314 | 0.535 → 0.868 | 6x sr_airtime | down | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.634 → 0.912 | 0.278 | 0.601 → 0.908 | 2.3x sr_bytes | up | 4 |
| `MS-density` | nodes | **text** | 0.691 → 0.960 | 0.270 | 0.677 → 0.960 | 4.3x sr_airtime | up | 5 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.411 → 0.667 | 0.256 | 0.330 → 0.547 | 5.1x sr_airtime | up | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.404 → 0.652 | 0.249 | 0.401 → 0.646 | 1.4x sr_airtime | up | 2 |
| `RT-hopspread` | hop-limit | **text** | 0.634 → 0.881 | 0.247 | 0.601 → 0.873 | 2x sr_bytes | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.634 → 0.837 | 0.203 | 0.601 → 0.829 | 1.6x sr_bytes | up | 2 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.765 → 0.960 | 0.195 | 0.760 → 0.960 | 4.9x sr_airtime | down | 2 |
| `SF-hops-flat` | hops-apart | **held** | 0.776 → 0.970 | 0.194 | 0.827 → 0.834 | 3.6x sr_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.776 → 0.970 | 0.194 | 0.827 → 0.840 | 3.6x sr_bytes | down | 5 |
| `RF-noise` | noise-profile | **text** | 0.654 → 0.839 | 0.185 | 0.645 → 0.829 | 1.4x sr_bytes | down | 4 |
| `DG-loss` | extra-loss | **text** | 0.694 → 0.837 | 0.143 | 0.678 → 0.829 | 1.3x sr_bytes | down | 4 |
| `AD-badrouters` | role-placement | **text** | 0.662 → 0.799 | 0.137 | 0.629 → 0.786 | 1.2x sr_bytes | down | 3 |
| `SF-place-flat` | place | **held** | 0.847 → 0.970 | 0.122 | 0.828 → 0.832 | 3.9x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.847 → 0.970 | 0.122 | 0.828 → 0.832 | 3.9x sr_bytes | up | 6 |
| `SC-signing` | signature-policy | **text** | 0.724 → 0.837 | 0.112 | 0.724 → 0.829 | 1.3x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.763 → 0.872 | 0.109 | 0.742 → 0.863 | 2x sr_airtime | up | 4 |
| `MS-size` | nodes | **text** | 0.728 → 0.837 | 0.109 | 0.719 → 0.829 | 5.3x sr_bytes | down | 5 |
| `FW-mixed` | legacy-fraction | **held** | 0.878 → 0.982 | 0.104 | 0.820 → 0.867 | 2.3x sr_bytes | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.770 → 0.872 | 0.101 | 0.747 → 0.863 | 2x sr_airtime | down | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.837 → 0.932 | 0.096 | 0.829 → 0.927 | 1.4x sr_bytes | up | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.802 → 0.896 | 0.094 | 0.789 → 0.894 | 4.8x sr_airtime | up | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.654 → 0.744 | 0.090 | 0.651 → 0.740 | 1.4x sr_airtime | down | 2 |
| `AD-flooding` | role-mix | **text** | 0.799 → 0.882 | 0.083 | 0.786 → 0.879 | 2.5x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.799 → 0.882 | 0.083 | 0.786 → 0.879 | 2.5x bytes_on_air | up | 3 |
| `FW-mixed-26` | legacy-fraction | **held** | 0.904 → 0.985 | 0.081 | 0.807 → 0.860 | 2.6x sr_bytes | up | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.837 → 0.907 | 0.071 | 0.829 → 0.898 | 1.2x sr_bytes | up | 3 |
| `AD-amplify-worst` | amplify-worst | **held** | 0.930 → 0.996 | 0.066 | 0.829 → 0.888 | 3x sr_bytes | up | 3 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.914 → 0.970 | 0.055 | 0.829 → 0.834 | 17x sr_airtime | down | 3 |
| `FW-versions` | profile | **text** | 0.837 → 0.892 | 0.055 | 0.829 → 0.889 | 3x bytes_on_air | down | 5 |
| `MS-roles-fav` | role-mix | **held** | 0.916 → 0.964 | 0.048 | 0.810 → 0.847 | 1.1x advert_bytes | down | 2 |
| `SF-cadence` | trigger | **held** | 0.923 → 0.970 | 0.047 | 0.800 → 0.832 | 14x sr_bytes | down | 4 |
| `RT-hopassign` | hop-assign | **text** | 0.791 → 0.837 | 0.046 | 0.778 → 0.829 | 1.2x sr_bytes | down | 2 |
| `MS-roles` | role-mix | **text** | 0.799 → 0.839 | 0.040 | 0.786 → 0.830 | 1.2x bytes_on_air | down | 2 |
| `FW-firmware` | profile | **text** | 0.837 → 0.875 | 0.038 | 0.829 → 0.865 | 3.1x bytes_on_air | down | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.660 → 0.698 | 0.037 | 0.542 → 0.576 | 1.5x sr_airtime | up | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.846 → 0.880 | 0.034 | 0.837 → 0.871 | 1.1x sr_bytes | up | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.806 → 0.837 | 0.031 | 0.793 → 0.829 | 1.4x sr_airtime | down | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.837 → 0.867 | 0.030 | 0.829 → 0.862 | 3.3x bytes_on_air | down | 2 |
| `SF-provide-transport` | provide-transport | **text** | 0.837 → 0.866 | 0.030 | 0.828 → 0.829 | 2.6x sr_airtime | up | 2 |
| `SF-catchup` | catch-up-hours | **text** | 0.812 → 0.842 | 0.029 | 0.800 → 0.838 | 11x sr_bytes | up | 3 |
| `LD-diurnal` | diurnal | **text** | 0.837 → 0.862 | 0.025 | 0.829 → 0.855 | 1.2x advert_bytes | down | 3 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.823 → 0.842 | 0.020 | 0.812 → 0.834 | 5.2x advert_bytes | up | 3 |
| `MS-router-late` | router-late-fraction | **held** | 0.951 → 0.970 | 0.018 | 0.826 → 0.836 | 1.4x bytes_on_air | down | 4 |
| `SF-capacity-window` | capacity | **held** | 0.947 → 0.964 | 0.017 | 0.819 → 0.835 | 2.4x advert_bytes | up | 3 |
| `SF-servers-allrouters` | servers | **held** | 0.951 → 0.967 | 0.016 | 0.817 → 0.832 | 3.5x sr_bytes | up | 2 |
| `SF-sr-retries` | sr-retries | **held** | 0.958 → 0.971 | 0.013 | 0.822 → 0.835 | 1.1x sr_bytes | down | 4 |
| `AD-worst` | role-placement | **text** | 0.816 → 0.828 | 0.012 | 0.810 → 0.824 | 1.1x bytes_on_air | down | 2 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.964 → 0.975 | 0.011 | 0.827 → 0.839 | 1.1x sr_bytes | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.964 → 0.975 | 0.011 | 0.827 → 0.839 | 1.1x sr_bytes | down | 4 |
| `SF-advert-transport` | advert-transport | **text** | 0.837 → 0.848 | 0.011 | 0.829 → 0.841 | 2.8x sr_airtime | up | 2 |
| `DM-mode` | dm-mode | **held** | 0.952 → 0.962 | 0.009 | 0.799 → 0.808 | 1.1x sr_bytes | up | 3 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.964 → 0.973 | 0.009 | 0.825 → 0.834 | 3x advert_bytes | down | 4 |
| `SF-servers-flat` | servers | **held** | 0.970 → 0.979 | 0.009 | 0.829 → 0.840 | 7x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.970 → 0.979 | 0.009 | 0.829 → 0.840 | 7x sr_bytes | up | 4 |
| `SF-capacity` | capacity | **text** | 0.837 → 0.845 | 0.008 | 0.829 → 0.838 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **text** | 0.837 → 0.845 | 0.008 | 0.829 → 0.838 | 5.3x advert_bytes | up | 5 |
| `SF-width` | short-id-bits | **held** | 0.964 → 0.972 | 0.008 | 0.826 → 0.832 | 3.1x advert_bytes | up | 4 |
| `SF-window-size` | window-size | **held** | 0.964 → 0.971 | 0.007 | 0.824 → 0.830 | 5.2x advert_bytes | down | 3 |
| `SF-replay-order` | replay-ordering | **text** | 0.837 → 0.843 | 0.006 | 0.829 → 0.834 | 1.1x sr_bytes | up | 2 |
| `SF-resolve` | resolve | **held** | 0.964 → 0.970 | 0.005 | 0.829 → 0.829 | 5.7x advert_bytes | = | 3 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.952 → 0.957 | 0.005 | 0.808 → 0.810 | 1.1x sr_airtime | up | 2 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.806 → 0.810 | 0.004 | 0.806 → 0.810 | 1x sr_bytes | down | 2 |
| `PR-repeats` | extra-repeats | **held** | 0.966 → 0.970 | 0.004 | 0.829 → 0.832 | 1.1x sr_bytes | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.966 → 0.970 | 0.004 | 0.827 → 0.828 | 1.1x sr_bytes | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.960 → 0.964 | 0.003 | 0.960 → 0.963 | 1.1x sr_airtime | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.957 → 0.960 | 0.003 | 0.956 → 0.960 | 1.2x bytes_on_air | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.960 → 0.962 | 0.001 | 0.960 → 0.961 | 1x sr_bytes | up | 2 |

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
| none | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| sprinkled | 1 | 0.879 | 0.875 | 0.004 | - | - | 0.989 | 0.990 | 0.626 | 1.25x | 15.1/24.5/27.9% | 1.9/5.3% | 3 |
| arms-race | 1 | 0.932 | 0.927 | 0.005 | - | - | 0.987 | 0.988 | 0.737 | 1.10x | 17.4/24.5/27.8% | 1.5/5.3% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario alpine`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 0.1 | 1 | 0.862 | 0.847 | 0.015 | - | - | 0.930 | 0.956 | 0.421 | 1.24x | 15.2/24.8/29.3% | 1.9/5.4% | 3 |
| 0.3 | 1 | 0.896 | 0.888 | 0.008 | - | - | 0.996 | 0.998 | 0.524 | 1.11x | 16.0/23.9/29.0% | 1.6/5.1% | 3 |

> amplify-worst=0.1: decode_failures 56

> slower: 5.53 s per simulated hour against 1.79 over 70 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-badrouters` - role-placement  `--scenario alpine`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.799 | 0.786 | 0.013 | - | - | 0.941 | 0.943 | 0.457 | 1.07x | 13.4/22.5/25.6% | 1.8/5.2% | 3 |
| inverse | 1 | 0.662 | 0.629 | 0.033 | - | - | 0.858 | 0.865 | 0.389 | 0.99x | 10.8/16.7/19.5% | 1.8/3.0% | 3 |
| random | 1 | 0.731 | 0.716 | 0.015 | - | - | 0.931 | 0.936 | 0.438 | 1.06x | 11.8/18.5/22.4% | 1.8/4.5% | 3 |

> role-placement=random: misdecodes 1

> role-placement=random: decode_failures 3

### `AD-flooding` - role-mix  `--scenario alpine`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.799 | 0.786 | 0.013 | - | - | 0.941 | 0.943 | 0.457 | 1.07x | 13.4/22.5/25.6% | 1.8/5.2% | 3 |
| all-routers | 1 | 0.882 | 0.879 | 0.003 | - | - | 0.974 | 0.976 | 0.678 | 2.66x | 30.0/38.8/43.5% | 4.4/5.4% | 3 |

### `AD-nomute` - role-mix  `--scenario alpine`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.799 | 0.786 | 0.013 | - | - | 0.941 | 0.943 | 0.457 | 1.07x | 13.4/22.5/25.6% | 1.8/5.2% | 3 |
| no-mute | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.957 | 0.958 | 0.479 | 1.23x | 13.7/22.4/25.9% | 1.9/5.3% | 3 |
| all-routers | 1 | 0.882 | 0.879 | 0.003 | - | - | 0.974 | 0.976 | 0.678 | 2.66x | 30.0/38.8/43.5% | 4.4/5.4% | 3 |

### `AD-siting` - siting-mix  `--scenario alpine`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.799 | 0.786 | 0.013 | - | - | 0.941 | 0.943 | 0.457 | 1.07x | 13.4/22.5/25.6% | 1.8/5.2% | 3 |
| local-typical | 1 | 0.531 | 0.522 | 0.009 | - | - | 0.707 | 0.737 | 0.000 | 1.32x | 10.6/23.6/29.6% | 2.0/5.6% | 3 |
| basement-heavy | 1 | 0.135 | 0.133 | 0.001 | - | - | 0.288 | 0.377 | 0.000 | 0.80x | 1.8/12.1/19.1% | 0.3/4.3% | 3 |

> siting-mix=local-typical: decode_failures 28

> siting-mix=basement-heavy: decode_failures 6

> slower: 3.4 s per simulated hour against 1.42 over 70 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-worst` - role-placement  `--scenario alpine`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.828 | 0.824 | 0.004 | - | - | 0.940 | 0.940 | 0.141 | 2.31x | 16.2/29.9/36.7% | 1.7/5.6% | 3 |
| inverse | 1 | 0.816 | 0.810 | 0.006 | - | - | 0.948 | 0.948 | 0.111 | 2.20x | 14.9/24.1/30.8% | 1.7/3.2% | 3 |

> role-placement=degree: decode_failures 3

### `BL-control` - protocol  `--scenario alpine`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.832 | 0.832 | 0.000 | - | - | 0 | 0.000 | 0.480 | 1.20x | 14.7/21.9/26.2% | 1.8/5.2% | 3 |
| sr | 1 | 0.847 | 0.827 | 0.019 | - | - | 0.924 | 0.954 | 0.486 | 1.22x | 15.2/22.5/26.8% | 1.8/5.5% | 3 |

> protocol=sr: decode_failures 25

> slower: 3.9 s per simulated hour against 1.81 over 70 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario alpine`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.763 | 0.742 | 0.020 | - | - | 0.892 | 0.899 | 0.538 | 2.98x | 35.4/56.1/61.7% | 4.4/9.6% | 3 |
| 100 | 1 | 0.872 | 0.863 | 0.009 | - | - | 0.955 | 0.958 | 0.615 | 1.56x | 18.8/30.6/34.6% | 2.3/5.2% | 3 |
| 120 | 1 | 0.872 | 0.863 | 0.009 | - | - | 0.955 | 0.958 | 0.615 | 1.56x | 18.8/30.6/34.6% | 2.3/5.2% | 3 |
| 250 | 1 | 0.872 | 0.863 | 0.009 | - | - | 0.955 | 0.958 | 0.615 | 1.56x | 18.8/30.6/34.6% | 2.3/5.2% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario alpine`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.337 | 0.330 | 0.007 | - | - | 0.411 | 0.436 | 0.121 | 11.28x | 42.0/64.6/73.8% | 3.8/11.4% | 3 |
| 120 | 1 | 0.558 | 0.542 | 0.015 | - | - | 0.660 | 0.660 | 0.198 | 4.36x | 17.2/30.1/36.7% | 1.3/6.0% | 3 |
| 250 | 1 | 0.562 | 0.547 | 0.015 | - | - | 0.667 | 0.670 | 0.191 | 4.26x | 16.8/29.5/36.1% | 1.3/5.8% | 3 |

> max-num-nodes=10: decode_failures 41

> max-num-nodes=250: decode_failures 3

### `DB-platform` - platform-mix  `--scenario alpine`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.872 | 0.863 | 0.009 | - | - | 0.955 | 0.958 | 0.615 | 1.56x | 18.8/30.6/34.6% | 2.3/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.872 | 0.863 | 0.009 | - | - | 0.955 | 0.958 | 0.615 | 1.56x | 18.8/30.6/34.6% | 2.3/5.2% | 3 |
| constrained | 1 | 0.770 | 0.747 | 0.024 | - | - | 0.911 | 0.912 | 0.534 | 2.98x | 35.4/56.1/61.7% | 4.4/9.6% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario alpine`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.744 | 0.740 | 0.004 | - | - | 0.871 | 0.907 | 0.536 | 5.84x | 56.9/73.5/78.0% | 4.0/12.9% | 3 |
| 25 | 1 | 0.744 | 0.740 | 0.004 | - | - | 0.871 | 0.907 | 0.536 | 5.84x | 56.9/73.5/78.0% | 4.0/12.9% | 3 |
| 100 | 1 | 0.744 | 0.740 | 0.004 | - | - | 0.871 | 0.907 | 0.536 | 5.84x | 56.9/73.5/78.0% | 4.0/12.9% | 3 |
| 2000 | 1 | 0.744 | 0.740 | 0.004 | - | - | 0.871 | 0.907 | 0.536 | 5.84x | 56.9/73.5/78.0% | 4.0/12.9% | 3 |

> warm-num-nodes=0: queue drops 10.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 86

> warm-num-nodes=25: queue drops 10.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 86

> warm-num-nodes=100: queue drops 10.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 86

> warm-num-nodes=2000: queue drops 10.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 86

### `DG-burst` - burst-loss  `--scenario alpine`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 0.1 | 1 | 0.749 | 0.732 | 0.017 | - | - | 0.950 | 0.955 | 0.414 | 1.17x | 14.3/22.0/26.3% | 1.7/5.1% | 3 |
| 0.2 | 1 | 0.640 | 0.609 | 0.031 | - | - | 0.906 | 0.914 | 0.315 | 1.09x | 13.4/20.8/25.3% | 1.6/4.5% | 3 |
| 0.3 | 1 | 0.522 | 0.485 | 0.037 | - | - | 0.780 | 0.835 | 0.225 | 1.00x | 12.4/19.7/23.8% | 1.6/4.1% | 3 |

> burst-loss=0.2: decode_failures 2

> burst-loss=0.3: decode_failures 32

### `DG-loss` - extra-loss  `--scenario alpine`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 0.1 | 1 | 0.813 | 0.805 | 0.009 | - | - | 0.969 | 0.971 | 0.461 | 1.29x | 15.7/23.9/28.2% | 1.9/5.3% | 3 |
| 0.2 | 1 | 0.763 | 0.753 | 0.010 | - | - | 0.945 | 0.949 | 0.394 | 1.34x | 16.4/25.3/29.6% | 2.0/5.2% | 3 |
| 0.3 | 1 | 0.694 | 0.678 | 0.016 | - | - | 0.907 | 0.911 | 0.333 | 1.36x | 16.9/26.2/30.5% | 2.0/5.0% | 3 |

### `DG-outage` - burst-loss  `--scenario alpine`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 0.1 | 1 | 0.723 | 0.703 | 0.019 | - | - | 0.898 | 0.925 | 0.359 | 1.15x | 14.1/21.7/26.1% | 1.7/5.2% | 3 |
| 0.2 | 1 | 0.608 | 0.587 | 0.022 | - | - | 0.844 | 0.895 | 0.262 | 1.10x | 13.5/21.5/25.6% | 1.6/4.8% | 3 |
| 0.3 | 1 | 0.506 | 0.477 | 0.029 | - | - | 0.739 | 0.831 | 0.209 | 1.05x | 13.0/19.9/24.4% | 1.6/4.0% | 3 |

> burst-loss=0.1: decode_failures 41

> burst-loss=0.2: decode_failures 38

> burst-loss=0.3: decode_failures 28

### `DM-mode` - dm-mode  `--scenario alpine`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.799 | 0.799 | 0.000 | - | - | 0.953 | 0.961 | 0.481 | 1.63x | 19.8/30.0/35.4% | 2.4/7.1% | 3 |
| directed-with-late-flood | 1 | 0.808 | 0.808 | 0.000 | - | - | 0.952 | 0.962 | 0.508 | 1.46x | 17.9/27.4/32.5% | 2.2/6.5% | 3 |
| m4-early-flood | 1 | 0.805 | 0.805 | 0.000 | - | - | 0.962 | 0.971 | 0.480 | 1.49x | 18.1/27.8/33.0% | 2.2/6.6% | 3 |

### `FW-firmware` - profile  `--scenario alpine`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.875 | 0.865 | 0.009 | - | - | 0.975 | 0.978 | 0.366 | 0.71x | 8.4/10.7/12.6% | 1.1/1.9% | 3 |
| 2.8 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario alpine`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 0.25 | 1 | 0.856 | 0.853 | 0.002 | - | - | 0.961 | 0.962 | 0.541 | 1.18x | 13.9/20.2/23.2% | 1.7/4.8% | 3 |
| 0.5 | 1 | 0.832 | 0.820 | 0.012 | - | - | 0.878 | 0.935 | 0.331 | 1.03x | 13.0/16.9/19.7% | 1.6/4.0% | 3 |
| 0.75 | 1 | 0.870 | 0.867 | 0.003 | - | - | 0.982 | 0.982 | 0.195 | 0.89x | 10.6/14.8/17.5% | 1.3/3.0% | 3 |

> legacy-fraction=0.5: decode_failures 39

### `FW-mixed-26` - legacy-fraction  `--scenario alpine`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 0.25 | 1 | 0.858 | 0.856 | 0.001 | - | - | 0.968 | 0.968 | 0.545 | 1.15x | 13.8/19.8/22.8% | 1.8/4.8% | 3 |
| 0.5 | 1 | 0.825 | 0.807 | 0.018 | - | - | 0.904 | 0.933 | 0.268 | 1.02x | 13.1/16.8/20.1% | 1.5/4.1% | 3 |
| 0.75 | 1 | 0.865 | 0.860 | 0.004 | - | - | 0.985 | 0.985 | 0.159 | 0.88x | 10.6/14.9/18.1% | 1.3/3.1% | 3 |

> legacy-fraction=0.5: decode_failures 40

### `FW-signing-cost` - profile-flag  `--scenario alpine`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.867 | 0.862 | 0.004 | - | - | 0.971 | 0.972 | 0.538 | 0.66x | 8.3/12.7/15.6% | 1.0/3.1% | 3 |
| signing=true | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |

### `FW-versions` - profile  `--scenario alpine`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.880 | 0.871 | 0.009 | - | - | 0.978 | 0.982 | 0.386 | 0.73x | 9.1/12.1/14.2% | 1.1/2.4% | 3 |
| 2.5 | 1 | 0.874 | 0.866 | 0.007 | - | - | 0.975 | 0.976 | 0.382 | 0.75x | 9.2/12.2/14.3% | 1.2/2.5% | 3 |
| 2.6 | 1 | 0.879 | 0.870 | 0.008 | - | - | 0.984 | 0.984 | 0.416 | 0.73x | 9.1/12.3/14.7% | 1.1/2.4% | 3 |
| 2.7 | 1 | 0.892 | 0.889 | 0.003 | - | - | 0.978 | 0.980 | 0.424 | 0.73x | 9.3/13.0/15.4% | 1.1/3.0% | 3 |
| 2.8 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.871 | 0.868 | 0.004 | - | - | 0.984 | 0.984 | 0.533 | 0.83x | 10.2/15.1/18.1% | 1.3/3.6% | 3 |
| 900 | 1 | 0.802 | 0.789 | 0.013 | - | - | 0.957 | 0.958 | 0.484 | 1.96x | 23.7/36.0/42.4% | 2.9/8.6% | 3 |
| 300 | 1 | 0.557 | 0.535 | 0.022 | - | - | 0.771 | 0.848 | 0.324 | 4.14x | 47.6/69.7/76.1% | 6.2/16.8% | 3 |

> broadcast-interval-s=300: decode_failures 29

### `LD-chatty-hops` - broadcast-interval-s  `--scenario alpine`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.916 | 0.914 | 0.002 | - | - | 0.983 | 0.983 | 0.638 | 0.91x | 10.8/15.2/18.2% | 1.6/3.5% | 3 |
| 900 | 1 | 0.853 | 0.843 | 0.010 | - | - | 0.958 | 0.959 | 0.580 | 2.14x | 25.7/36.6/43.4% | 3.4/8.6% | 3 |
| 300 | 1 | 0.581 | 0.562 | 0.020 | - | - | 0.795 | 0.843 | 0.383 | 4.63x | 51.9/71.2/77.6% | 7.3/17.3% | 3 |

> broadcast-interval-s=300: decode_failures 6

### `LD-diurnal` - diurnal  `--scenario alpine`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.862 | 0.855 | 0.006 | - | - | 0.971 | 0.973 | 0.545 | 1.17x | 14.4/21.5/25.7% | 1.8/5.2% | 3 |
| sinusoid | 1 | 0.853 | 0.846 | 0.007 | - | - | 0.967 | 0.971 | 0.523 | 1.09x | 13.3/19.9/23.7% | 1.7/4.8% | 3 |
| commuter | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.802 | 0.789 | 0.013 | - | - | 0.957 | 0.958 | 0.484 | 1.96x | 23.7/36.0/42.4% | 2.9/8.6% | 3 |
| 3600 | 1 | 0.871 | 0.868 | 0.004 | - | - | 0.984 | 0.984 | 0.533 | 0.83x | 10.2/15.1/18.1% | 1.3/3.6% | 3 |
| 10800 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.976 | 0.978 | 0.564 | 0.56x | 6.8/9.9/11.9% | 0.9/2.4% | 3 |
| 43200 | 1 | 0.896 | 0.894 | 0.002 | - | - | 0.988 | 0.988 | 0.569 | 0.41x | 4.9/7.3/8.9% | 0.7/1.8% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario alpine`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 0.25 | 1 | 0.828 | 0.820 | 0.008 | - | - | 0.960 | 0.960 | 0.497 | 1.29x | 15.6/23.8/28.4% | 1.9/5.7% | 3 |
| 1.0 | 1 | 0.829 | 0.821 | 0.008 | - | - | 0.968 | 0.969 | 0.504 | 1.40x | 17.0/26.0/30.9% | 2.1/6.2% | 3 |
| 4.0 | 1 | 0.806 | 0.793 | 0.013 | - | - | 0.956 | 0.960 | 0.468 | 1.69x | 20.3/32.9/39.2% | 2.4/8.0% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario alpine`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.744 | 0.740 | 0.004 | - | - | 0.871 | 0.907 | 0.536 | 5.84x | 56.9/73.5/78.0% | 4.0/12.9% | 3 |
| 1.0 | 1 | 0.654 | 0.651 | 0.002 | - | - | 0.783 | 0.849 | 0.445 | 6.46x | 61.3/75.7/80.4% | 4.6/13.9% | 3 |

> traceroute-per-hour=0.0: queue drops 10.9% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 86

> traceroute-per-hour=1.0: queue drops 19.2% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 93

### `MS-density` - nodes  `--scenario alpine`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.691 | 0.677 | 0.013 | - | - | 0.918 | 0.921 | 0.289 | 1.25x | 17.0/23.0/29.2% | 2.6/6.5% | 3 |
| 60 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 90 | 1 | 0.915 | 0.910 | 0.005 | - | - | 0.991 | 0.991 | 0.622 | 1.66x | 17.7/30.1/34.7% | 1.5/5.2% | 3 |
| 120 | 1 | 0.960 | 0.960 | 0.001 | - | - | 1.000 | 1.000 | 0.838 | 2.04x | 21.8/32.7/37.5% | 1.3/5.2% | 3 |
| 150 | 1 | 0.954 | 0.953 | 0.001 | - | - | 0.996 | 0.996 | 0.737 | 2.58x | 27.2/41.6/44.7% | 1.3/5.7% | 3 |

> nodes=90: misdecodes 1

> nodes=120: misdecodes 1

### `MS-hopscale` - nodes  `--scenario alpine`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 120 | 1 | 0.742 | 0.734 | 0.008 | - | - | 0.976 | 0.977 | 0.000 | 2.20x | 15.7/24.8/33.1% | 1.5/5.1% | 3 |
| 250 | 1 | 0.555 | 0.540 | 0.015 | - | - | 0.651 | 0.653 | 0.189 | 4.73x | 18.4/32.4/39.4% | 1.5/6.6% | 3 |
| 500 | 1 | 0.333 | 0.330 | 0.003 | - | - | 0.336 | 0.336 | 0.075 | 9.99x | 20.1/31.9/42.0% | 1.7/5.9% | 3 |

### `MS-oversubscribed` - nodes  `--scenario alpine`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.742 | 0.734 | 0.008 | - | - | 0.981 | 0.982 | 0.000 | 2.06x | 14.7/23.5/31.4% | 1.4/4.8% | 3 |
| 250 | 1 | 0.558 | 0.542 | 0.015 | - | - | 0.660 | 0.660 | 0.198 | 4.36x | 17.2/30.1/36.7% | 1.3/6.0% | 3 |
| 500 | 1 | 0.333 | 0.330 | 0.003 | - | - | 0.353 | 0.354 | 0.077 | 9.35x | 19.0/29.9/39.8% | 1.6/5.5% | 3 |

### `MS-roles` - role-mix  `--scenario alpine`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.839 | 0.830 | 0.009 | - | - | 0.974 | 0.975 | 0.521 | 1.26x | 15.5/23.3/27.7% | 1.9/5.6% | 3 |
| baymesh-2026-08 | 1 | 0.799 | 0.786 | 0.013 | - | - | 0.941 | 0.943 | 0.457 | 1.07x | 13.4/22.5/25.6% | 1.8/5.2% | 3 |

### `MS-roles-fav` - role-mix  `--scenario alpine`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.856 | 0.847 | 0.009 | - | - | 0.964 | 0.965 | 0.583 | 1.32x | 16.3/23.3/27.7% | 2.1/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.822 | 0.810 | 0.012 | - | - | 0.916 | 0.919 | 0.471 | 1.26x | 16.2/25.4/28.4% | 2.1/5.1% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario alpine`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 0.05 | 1 | 0.846 | 0.836 | 0.010 | - | - | 0.963 | 0.963 | 0.548 | 1.35x | 16.4/28.0/31.7% | 2.0/5.3% | 3 |
| 0.1 | 1 | 0.842 | 0.830 | 0.012 | - | - | 0.951 | 0.954 | 0.552 | 1.48x | 18.6/31.5/36.9% | 2.2/5.1% | 3 |
| 0.2 | 1 | 0.838 | 0.826 | 0.012 | - | - | 0.958 | 0.958 | 0.528 | 1.68x | 20.4/34.1/41.5% | 2.4/5.1% | 3 |

### `MS-siting` - siting-mix  `--scenario alpine`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| local-typical | 1 | 0.615 | 0.610 | 0.005 | - | - | 0.769 | 0.779 | 0.000 | 1.47x | 11.2/21.1/30.5% | 2.3/5.2% | 3 |
| event | 1 | 0.145 | 0.142 | 0.003 | - | - | 0.355 | 0.357 | 0.000 | 1.07x | 5.5/11.5/20.2% | 1.6/4.1% | 3 |
| backbone | 1 | 0.978 | 0.977 | 0.001 | - | - | 0.997 | 0.997 | 0.936 | 1.08x | 23.0/31.4/36.0% | 1.2/5.5% | 3 |

> siting-mix=local-typical: decode_failures 2

### `MS-size` - nodes  `--scenario alpine`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.794 | 0.783 | 0.012 | - | - | 0.939 | 0.939 | 0.326 | 1.40x | 21.2/33.8/38.4% | 3.0/7.2% | 3 |
| 60 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 90 | 1 | 0.764 | 0.753 | 0.011 | - | - | 0.967 | 0.967 | 0.402 | 1.59x | 14.5/22.2/25.4% | 1.4/5.4% | 3 |
| 120 | 1 | 0.742 | 0.734 | 0.008 | - | - | 0.976 | 0.977 | 0.000 | 2.20x | 15.7/24.8/33.1% | 1.5/5.1% | 3 |
| 150 | 1 | 0.728 | 0.719 | 0.009 | - | - | 0.963 | 0.972 | 0.362 | 2.75x | 15.9/28.9/38.3% | 1.5/5.4% | 3 |

> nodes=150: decode_failures 18

### `MS-stretch` - stretch  `--scenario alpine`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 1.25 | 1 | 0.641 | 0.635 | 0.006 | - | - | 0.885 | 0.886 | 0.225 | 1.30x | 11.5/21.6/26.1% | 1.8/5.3% | 3 |
| 1.5 | 1 | 0.404 | 0.401 | 0.003 | - | - | 0.716 | 0.720 | 0.036 | 1.27x | 9.8/17.4/21.9% | 1.9/5.3% | 3 |
| 2.0 | 1 | 0.133 | 0.132 | 0.000 | - | - | 0.176 | 0.176 | 0.000 | 0.88x | 4.2/8.8/10.0% | 1.3/3.3% | 3 |

> faster: 1.02 s per simulated hour against 2.1 over 70 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-topology` - topology  `--scenario alpine`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| clustered | 1 | 0.940 | 0.939 | 0.001 | - | - | 0.996 | 0.996 | 0.000 | 1.17x | 24.0/30.7/34.4% | 1.4/5.5% | 3 |
| corridor | 1 | 0.524 | 0.507 | 0.017 | - | - | 0.651 | 0.672 | 0.197 | 1.35x | 17.8/22.0/23.1% | 2.1/5.6% | 3 |
| hub | 1 | 0.917 | 0.916 | 0.001 | - | - | 0.974 | 0.974 | 0.695 | 1.28x | 25.6/36.2/38.5% | 1.9/5.6% | 3 |

> topology=corridor: decode_failures 7

> topology=hub: misdecodes 1

### `PR-crladder` - coding-rate-ladder  `--scenario alpine`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.808 | 0.808 | 0.000 | - | - | 0.952 | 0.962 | 0.508 | 1.46x | 17.9/27.4/32.5% | 2.2/6.5% | 3 |
| True | 1 | 0.810 | 0.810 | 0.000 | - | - | 0.957 | 0.972 | 0.499 | 1.48x | 18.1/27.8/33.0% | 2.2/6.6% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario alpine`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.810 | 0.810 | 0.000 | - | - | 0.957 | 0.972 | 0.499 | 1.48x | 18.1/27.8/33.0% | 2.2/6.6% | 3 |
| m4-early-flood | 1 | 0.806 | 0.806 | 0.000 | - | - | 0.955 | 0.970 | 0.494 | 1.48x | 18.1/27.8/32.9% | 2.2/6.6% | 3 |

### `PR-protocol` - protocol  `--scenario alpine`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.832 | 0.832 | 0.000 | - | - | 0 | 0.000 | 0.480 | 1.20x | 14.7/21.9/26.2% | 1.8/5.2% | 3 |
| chain | 1 | 0.831 | 0.827 | 0.003 | - | - | 0.924 | 0.973 | 0.502 | 1.42x | 17.3/26.3/31.1% | 2.1/6.3% | 3 |
| sr | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |

### `PR-repeats` - extra-repeats  `--scenario alpine`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| True | 1 | 0.840 | 0.832 | 0.008 | - | - | 0.966 | 0.967 | 0.527 | 1.24x | 15.1/22.7/27.0% | 1.9/5.4% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario alpine`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.960 | 0.960 | 0.001 | - | - | 1.000 | 1.000 | 0.838 | 2.04x | 21.8/32.7/37.5% | 1.3/5.2% | 3 |
| True | 1 | 0.962 | 0.961 | 0.001 | - | - | 0.999 | 0.999 | 0.849 | 2.06x | 21.9/32.7/37.6% | 1.3/5.1% | 3 |

> extra-repeats=False: misdecodes 1

### `RF-bw500` - preset  `--scenario alpine`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.202 | 0.200 | 0.002 | - | - | 0.450 | 0.453 | 0.000 | 0.06x | 0.3/0.7/1.1% | 0.1/0.3% | 3 |
| MEDIUM_TURBO | 1 | 0.437 | 0.429 | 0.008 | - | - | 0.710 | 0.712 | 0.068 | 0.25x | 1.9/3.5/4.8% | 0.4/1.0% | 3 |
| LONG_TURBO | 1 | 0.772 | 0.766 | 0.006 | - | - | 0.937 | 0.938 | 0.357 | 1.22x | 11.5/19.8/23.8% | 1.8/5.2% | 3 |

> preset=MEDIUM_TURBO: decode_failures 2

### `RF-duct` - duct-per-hour  `--scenario alpine`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 0.25 | 1 | 0.860 | 0.850 | 0.011 | - | - | 0.968 | 0.968 | 0.591 | 1.18x | 16.0/24.3/27.9% | 1.8/5.4% | 3 |
| 1.0 | 1 | 0.907 | 0.898 | 0.010 | - | - | 0.982 | 0.983 | 0.708 | 1.08x | 20.1/27.7/30.8% | 1.6/5.5% | 3 |

### `RF-eu-presets` - preset  `--scenario alpine`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.317 | 0.309 | 0.008 | - | - | 0.589 | 0.590 | 0.015 | 0.13x | 1.0/1.8/2.4% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| LITE_FAST | 1 | 0.790 | 0.786 | 0.004 | - | - | 0.955 | 0.957 | 0.405 | 0.97x | 10.1/17.3/20.6% | 1.5/4.2% | 3 |
| NARROW_SLOW | 1 | 0.799 | 0.790 | 0.009 | - | - | 0.962 | 0.965 | 0.423 | 1.26x | 13.7/23.4/27.5% | 1.9/5.2% | 3 |

### `RF-noise` - noise-profile  `--scenario alpine`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| temporal | 1 | 0.762 | 0.749 | 0.014 | - | - | 0.941 | 0.944 | 0.384 | 1.24x | 14.7/23.5/26.9% | 1.9/5.4% | 3 |
| transient | 1 | 0.839 | 0.826 | 0.013 | - | - | 0.973 | 0.976 | 0.519 | 1.23x | 14.9/22.6/26.7% | 1.9/5.4% | 3 |
| periodic | 1 | 0.654 | 0.645 | 0.010 | - | - | 0.789 | 0.794 | 0.306 | 1.14x | 14.0/21.1/25.4% | 1.7/4.7% | 3 |

### `RF-preset` - preset  `--scenario alpine`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.317 | 0.309 | 0.008 | - | - | 0.589 | 0.590 | 0.015 | 0.13x | 1.0/1.8/2.4% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| LONG_MODERATE | 1 | 0.822 | 0.801 | 0.021 | - | - | 0.943 | 0.946 | 0.589 | 3.17x | 41.0/59.3/64.9% | 4.5/12.4% | 3 |

> faster: 1.24 s per simulated hour against 2.77 over 70 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-preset-turbo` - preset  `--scenario alpine`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.073 | 0.073 | 0.000 | - | - | 0.147 | 0.147 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.202 | 0.200 | 0.002 | - | - | 0.450 | 0.453 | 0.000 | 0.06x | 0.3/0.7/1.1% | 0.1/0.3% | 3 |
| LONG_FAST | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| LONG_TURBO | 1 | 0.772 | 0.766 | 0.006 | - | - | 0.937 | 0.938 | 0.357 | 1.22x | 11.5/19.8/23.8% | 1.8/5.2% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.832 | 0.824 | 0.007 | - | - | 0.965 | 0.965 | 0.479 | 1.74x | 19.1/29.7/33.4% | 2.7/7.2% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario alpine`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.778 | 0.769 | 0.009 | - | - | 0.908 | 0.909 | 0.453 | 1.18x | 14.6/22.2/26.4% | 1.8/5.1% | 3 |
| 10000 | 1 | 0.654 | 0.645 | 0.010 | - | - | 0.789 | 0.794 | 0.306 | 1.14x | 14.0/21.1/25.4% | 1.7/4.7% | 3 |
| 4000 | 1 | 0.404 | 0.399 | 0.005 | - | - | 0.514 | 0.547 | 0.155 | 1.01x | 12.4/19.1/23.2% | 1.6/3.7% | 3 |
| 2000 | 1 | 0.096 | 0.096 | 0.000 | - | - | 0.126 | 0.200 | 0.038 | 0.70x | 8.8/13.3/16.5% | 1.1/2.1% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 1

### `RF-stretch-duct` - duct-per-hour  `--scenario alpine`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.404 | 0.401 | 0.003 | - | - | 0.716 | 0.720 | 0.036 | 1.27x | 9.8/17.4/21.9% | 1.9/5.3% | 3 |
| 1.0 | 1 | 0.652 | 0.646 | 0.006 | - | - | 0.859 | 0.860 | 0.341 | 1.11x | 14.3/19.9/24.2% | 1.6/5.0% | 3 |

### `RF-txpower` - tx-power  `--scenario alpine`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 22 | 1 | 0.409 | 0.404 | 0.005 | - | - | 0.654 | 0.657 | 0.075 | 1.30x | 9.7/16.8/23.3% | 2.1/4.8% | 3 |
| 17 | 1 | 0.186 | 0.183 | 0.003 | - | - | 0.367 | 0.371 | 0.000 | 1.21x | 6.4/13.1/18.8% | 1.7/4.8% | 3 |
| 14 | 1 | 0.105 | 0.102 | 0.003 | - | - | 0.275 | 0.357 | 0.000 | 0.79x | 3.3/7.8/13.6% | 1.2/3.7% | 3 |

> tx-power=22: decode_failures 1

> tx-power=14: decode_failures 5

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario alpine`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.960 | 0.960 | 0.001 | - | - | 1.000 | 1.000 | 0.838 | 2.04x | 21.8/32.7/37.5% | 1.3/5.2% | 3 |
| True | 1 | 0.957 | 0.956 | 0.001 | - | - | 0.999 | 1.000 | 0.835 | 2.46x | 25.6/37.3/42.0% | 1.6/5.8% | 3 |

> no-adopt-hop-recommendation=False: misdecodes 1

### `RT-favourites` - favourite-routers  `--scenario alpine`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.846 | 0.837 | 0.009 | - | - | 0.965 | 0.966 | 0.531 | 1.33x | 15.9/27.2/30.3% | 2.0/5.3% | 3 |
| True | 1 | 0.880 | 0.871 | 0.010 | - | - | 0.977 | 0.978 | 0.591 | 1.40x | 16.9/27.2/30.5% | 2.2/5.2% | 3 |

### `RT-hopassign` - hop-assign  `--scenario alpine`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| random | 1 | 0.791 | 0.778 | 0.013 | - | - | 0.954 | 0.955 | 0.487 | 1.23x | 14.9/22.8/27.0% | 1.9/5.5% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario alpine`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.634 | 0.601 | 0.033 | - | - | 0.930 | 0.930 | 0.285 | 0.97x | 11.7/20.8/24.5% | 1.4/5.4% | 3 |
| 7 | 1 | 0.881 | 0.873 | 0.008 | - | - | 0.970 | 0.970 | 0.593 | 1.35x | 16.2/23.0/27.4% | 2.2/5.4% | 3 |
| 15 | 1 | 0.908 | 0.904 | 0.004 | - | - | 0.973 | 0.976 | 0.638 | 1.36x | 16.3/23.2/27.6% | 2.3/5.4% | 3 |
| 32 | 1 | 0.912 | 0.908 | 0.004 | - | - | 0.977 | 0.978 | 0.636 | 1.37x | 16.3/23.2/27.7% | 2.3/5.4% | 3 |

### `RT-hopspread` - hop-limit  `--scenario alpine`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.634 | 0.601 | 0.033 | - | - | 0.930 | 0.930 | 0.285 | 0.97x | 11.7/20.8/24.5% | 1.4/5.4% | 3 |
| 5 | 1 | 0.830 | 0.823 | 0.007 | - | - | 0.969 | 0.970 | 0.494 | 1.22x | 14.8/22.3/26.5% | 1.8/5.4% | 3 |
| 7 | 1 | 0.881 | 0.873 | 0.008 | - | - | 0.970 | 0.970 | 0.593 | 1.35x | 16.2/23.0/27.4% | 2.2/5.4% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario alpine`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| KNOWN_ONLY | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.835 | 0.834 | 0.001 | - | - | 0.914 | 0.973 | 0.516 | 1.19x | 14.5/21.8/26.1% | 1.8/5.2% | 3 |

### `RT-spread` - hop-spread  `--scenario alpine`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.634 | 0.601 | 0.033 | - | - | 0.930 | 0.930 | 0.285 | 0.97x | 11.7/20.8/24.5% | 1.4/5.4% | 3 |
| True | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |

### `SC-signing` - signature-policy  `--scenario alpine`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| BALANCED | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| STRICT | 1 | 0.724 | 0.724 | 0.000 | - | - | 0.863 | 0.866 | 0.391 | 1.35x | 16.5/24.6/29.3% | 2.1/5.8% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario alpine`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| dm | 1 | 0.848 | 0.841 | 0.007 | - | - | 0.965 | 0.967 | 0.513 | 1.19x | 14.6/22.4/26.7% | 1.8/5.4% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario alpine`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.836 | 0.828 | 0.009 | - | - | 0.965 | 0.967 | 0.491 | 1.24x | 15.0/22.7/27.1% | 1.9/5.4% | 3 |
| local | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| time | 1 | 0.842 | 0.834 | 0.009 | - | - | 0.973 | 0.973 | 0.493 | 1.26x | 15.3/23.3/27.6% | 1.9/5.5% | 3 |
| window | 1 | 0.834 | 0.825 | 0.009 | - | - | 0.964 | 0.966 | 0.502 | 1.22x | 14.9/22.6/26.8% | 1.8/5.4% | 3 |

> bucket-mode=global: misdecodes 35

> bucket-mode=time: misdecodes 26

> bucket-mode=window: misdecodes 29

### `SF-bucket-time` - time-bucket-s  `--scenario alpine`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.823 | 0.812 | 0.010 | - | - | 0.960 | 0.962 | 0.482 | 1.39x | 16.7/25.6/30.1% | 2.1/6.1% | 3 |
| 1800 | 1 | 0.842 | 0.834 | 0.009 | - | - | 0.973 | 0.973 | 0.493 | 1.26x | 15.3/23.3/27.6% | 1.9/5.5% | 3 |
| 3600 | 1 | 0.838 | 0.829 | 0.009 | - | - | 0.963 | 0.966 | 0.505 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |

> time-bucket-s=600: misdecodes 127

> time-bucket-s=1800: misdecodes 26

> time-bucket-s=3600: misdecodes 11

### `SF-cadence` - trigger  `--scenario alpine`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| interval | 1 | 0.820 | 0.809 | 0.011 | - | - | 0.961 | 0.964 | 0.484 | 1.65x | 19.6/31.9/36.9% | 2.5/8.1% | 3 |
| aimd | 1 | 0.836 | 0.832 | 0.003 | - | - | 0.923 | 0.974 | 0.527 | 1.25x | 15.4/22.9/27.3% | 1.9/5.4% | 3 |
| bucket+interval | 1 | 0.812 | 0.800 | 0.012 | - | - | 0.956 | 0.956 | 0.462 | 1.69x | 19.8/32.7/38.0% | 2.5/8.4% | 3 |

> trigger=interval: misdecodes 15

> trigger=aimd: misdecodes 3

> trigger=bucket+interval: misdecodes 17

### `SF-capacity` - capacity  `--scenario alpine`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.842 | 0.832 | 0.010 | - | - | 0.966 | 0.972 | 0.525 | 1.23x | 14.8/23.0/27.4% | 1.8/5.6% | 3 |
| 8 | 1 | 0.845 | 0.838 | 0.007 | - | - | 0.971 | 0.976 | 0.514 | 1.22x | 14.9/22.5/26.8% | 1.8/5.4% | 3 |
| 16 | 1 | 0.841 | 0.835 | 0.007 | - | - | 0.967 | 0.968 | 0.528 | 1.21x | 14.7/22.4/26.6% | 1.8/5.4% | 3 |
| 32 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 50 | 1 | 0.844 | 0.837 | 0.007 | - | - | 0.972 | 0.974 | 0.517 | 1.24x | 15.1/23.0/27.4% | 1.9/5.5% | 3 |

> capacity=4: decode_failures 97

> capacity=8: decode_failures 34

### `SF-capacity-local` - capacity  `--scenario alpine`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.842 | 0.832 | 0.010 | - | - | 0.966 | 0.972 | 0.525 | 1.23x | 14.8/23.0/27.4% | 1.8/5.6% | 3 |
| 8 | 1 | 0.845 | 0.838 | 0.007 | - | - | 0.971 | 0.976 | 0.514 | 1.22x | 14.9/22.5/26.8% | 1.8/5.4% | 3 |
| 16 | 1 | 0.841 | 0.835 | 0.007 | - | - | 0.967 | 0.968 | 0.528 | 1.21x | 14.7/22.4/26.6% | 1.8/5.4% | 3 |
| 32 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 50 | 1 | 0.844 | 0.837 | 0.007 | - | - | 0.972 | 0.974 | 0.517 | 1.24x | 15.1/23.0/27.4% | 1.9/5.5% | 3 |

> capacity=4: decode_failures 97

> capacity=8: decode_failures 34

### `SF-capacity-window` - capacity  `--scenario alpine`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.841 | 0.835 | 0.006 | - | - | 0.947 | 0.971 | 0.518 | 1.21x | 14.8/22.4/26.7% | 1.8/5.4% | 3 |
| 16 | 1 | 0.830 | 0.819 | 0.011 | - | - | 0.961 | 0.963 | 0.507 | 1.22x | 15.0/22.5/26.8% | 1.8/5.4% | 3 |
| 32 | 1 | 0.834 | 0.825 | 0.009 | - | - | 0.964 | 0.966 | 0.502 | 1.22x | 14.9/22.6/26.8% | 1.8/5.4% | 3 |

> capacity=8: misdecodes 16

> capacity=8: decode_failures 44

> capacity=16: misdecodes 16

> capacity=32: misdecodes 29

### `SF-catchup` - catch-up-hours  `--scenario alpine`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.812 | 0.800 | 0.012 | - | - | 0.956 | 0.956 | 0.462 | 1.69x | 19.8/32.7/38.0% | 2.5/8.4% | 3 |
| 02-06 | 1 | 0.842 | 0.838 | 0.004 | - | - | 0.930 | 0.967 | 0.498 | 1.23x | 15.1/22.9/27.2% | 1.8/5.5% | 3 |
| 00-08 | 1 | 0.837 | 0.833 | 0.004 | - | - | 0.930 | 0.966 | 0.501 | 1.30x | 15.9/24.2/28.6% | 2.0/5.8% | 3 |

> catch-up-hours=: misdecodes 17

> catch-up-hours=02-06: decode_failures 2

> catch-up-hours=00-08: misdecodes 1

> catch-up-hours=00-08: decode_failures 2

> faster: 3.47 s per simulated hour against 9.05 over 70 prior run(s) - 2.6x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-hops-flat` - hops-apart  `--scenario alpine`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.832 | 0.830 | 0.002 | - | - | 0.960 | 0.960 | 0.490 | 1.21x | 14.9/22.3/26.7% | 1.8/5.3% | 3 |
| 2 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 3 | 1 | 0.847 | 0.827 | 0.019 | - | - | 0.924 | 0.954 | 0.486 | 1.22x | 15.2/22.5/26.8% | 1.8/5.5% | 3 |
| 4 | 1 | 0.849 | 0.834 | 0.015 | - | - | 0.776 | 0.940 | 0.528 | 1.24x | 15.1/22.6/27.1% | 1.8/5.5% | 3 |

> hops-apart=3: decode_failures 25

> hops-apart=4: decode_failures 28

### `SF-hops-spread` - hops-apart  `--scenario alpine`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.832 | 0.830 | 0.002 | - | - | 0.960 | 0.960 | 0.490 | 1.21x | 14.9/22.3/26.7% | 1.8/5.3% | 3 |
| 2 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 3 | 1 | 0.847 | 0.827 | 0.019 | - | - | 0.924 | 0.954 | 0.486 | 1.22x | 15.2/22.5/26.8% | 1.8/5.5% | 3 |
| 4 | 1 | 0.849 | 0.834 | 0.015 | - | - | 0.776 | 0.940 | 0.528 | 1.24x | 15.1/22.6/27.1% | 1.8/5.5% | 3 |
| 5 | 1 | 0.858 | 0.840 | 0.018 | - | - | 0.856 | 0.981 | 0.523 | 1.22x | 14.9/22.6/27.0% | 1.8/5.5% | 3 |

> hops-apart=3: decode_failures 25

> hops-apart=4: decode_failures 28

> hops-apart=5: decode_failures 34

### `SF-jitter-global` - advert-jitter-s  `--scenario alpine`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.836 | 0.827 | 0.010 | - | - | 0.969 | 0.971 | 0.499 | 1.23x | 14.9/22.6/26.9% | 1.8/5.4% | 3 |
| 30 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 120 | 1 | 0.846 | 0.839 | 0.006 | - | - | 0.975 | 0.977 | 0.484 | 1.22x | 14.9/22.5/26.7% | 1.8/5.4% | 3 |
| 600 | 1 | 0.839 | 0.830 | 0.009 | - | - | 0.964 | 0.964 | 0.516 | 1.22x | 14.9/22.5/26.7% | 1.8/5.4% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario alpine`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.836 | 0.827 | 0.010 | - | - | 0.969 | 0.971 | 0.499 | 1.23x | 14.9/22.6/26.9% | 1.8/5.4% | 3 |
| 30 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 120 | 1 | 0.846 | 0.839 | 0.006 | - | - | 0.975 | 0.977 | 0.484 | 1.22x | 14.9/22.5/26.7% | 1.8/5.4% | 3 |
| 600 | 1 | 0.839 | 0.830 | 0.009 | - | - | 0.964 | 0.964 | 0.516 | 1.22x | 14.9/22.5/26.7% | 1.8/5.4% | 3 |

### `SF-place-flat` - place  `--scenario alpine`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.868 | 0.828 | 0.040 | - | - | 0.847 | 0.972 | 0.525 | 1.25x | 15.3/23.1/27.5% | 1.8/5.6% | 3 |
| routers | 1 | 0.833 | 0.832 | 0.001 | - | - | 0.951 | 0.951 | 0.508 | 1.22x | 14.9/22.5/26.7% | 1.8/5.3% | 3 |
| alternate-routers | 1 | 0.834 | 0.830 | 0.004 | - | - | 0.962 | 0.963 | 0.497 | 1.21x | 14.7/22.4/26.7% | 1.8/5.4% | 3 |
| beside-router | 1 | 0.834 | 0.830 | 0.004 | - | - | 0.948 | 0.950 | 0.493 | 1.22x | 15.0/22.6/26.9% | 1.8/5.4% | 3 |
| random-clients | 1 | 0.843 | 0.828 | 0.015 | - | - | 0.940 | 0.942 | 0.556 | 1.22x | 15.0/22.2/26.5% | 1.8/5.2% | 3 |
| hops-apart | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |

> place=spread: decode_failures 22

### `SF-place-spread` - place  `--scenario alpine`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.868 | 0.828 | 0.040 | - | - | 0.847 | 0.972 | 0.525 | 1.25x | 15.3/23.1/27.5% | 1.8/5.6% | 3 |
| routers | 1 | 0.833 | 0.832 | 0.001 | - | - | 0.951 | 0.951 | 0.508 | 1.22x | 14.9/22.5/26.7% | 1.8/5.3% | 3 |
| alternate-routers | 1 | 0.834 | 0.830 | 0.004 | - | - | 0.962 | 0.963 | 0.497 | 1.21x | 14.7/22.4/26.7% | 1.8/5.4% | 3 |
| beside-router | 1 | 0.834 | 0.830 | 0.004 | - | - | 0.948 | 0.950 | 0.493 | 1.22x | 15.0/22.6/26.9% | 1.8/5.4% | 3 |
| random-clients | 1 | 0.843 | 0.828 | 0.015 | - | - | 0.940 | 0.942 | 0.556 | 1.22x | 15.0/22.2/26.5% | 1.8/5.2% | 3 |
| hops-apart | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |

> place=spread: decode_failures 22

### `SF-provide-transport` - provide-transport  `--scenario alpine`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| broadcast | 1 | 0.866 | 0.828 | 0.038 | - | - | 0.966 | 0.968 | 0.578 | 1.28x | 15.6/23.5/27.7% | 1.9/5.6% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario alpine`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| heard | 1 | 0.843 | 0.834 | 0.009 | - | - | 0.971 | 0.973 | 0.508 | 1.23x | 15.0/22.7/27.0% | 1.9/5.4% | 3 |

> replay-ordering=heard: misdecodes 21

### `SF-replay-order-broadcast` - replay-ordering  `--scenario alpine`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.866 | 0.828 | 0.038 | - | - | 0.966 | 0.968 | 0.578 | 1.28x | 15.6/23.5/27.7% | 1.9/5.6% | 3 |
| heard | 1 | 0.870 | 0.827 | 0.043 | - | - | 0.970 | 0.974 | 0.584 | 1.31x | 15.9/23.9/28.3% | 2.0/5.7% | 3 |

> replay-ordering=heard: misdecodes 9

### `SF-resolve` - resolve  `--scenario alpine`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| enum | 1 | 0.839 | 0.829 | 0.010 | - | - | 0.964 | 0.970 | 0.501 | 1.23x | 15.1/23.2/27.6% | 1.8/5.6% | 3 |
| hybrid | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |

### `SF-servers-allrouters` - servers  `--scenario alpine`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.833 | 0.832 | 0.001 | - | - | 0.951 | 0.951 | 0.508 | 1.22x | 14.9/22.5/26.7% | 1.8/5.3% | 3 |
| 6 | 1 | 0.827 | 0.817 | 0.010 | - | - | 0.967 | 0.967 | 0.489 | 1.25x | 15.1/23.2/27.5% | 1.9/5.7% | 6 |

### `SF-servers-flat` - servers  `--scenario alpine`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.845 | 0.840 | 0.005 | - | - | 0.972 | 0.975 | 0.504 | 1.22x | 14.9/22.6/26.9% | 1.8/5.4% | 2 |
| 3 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 5 | 1 | 0.843 | 0.833 | 0.011 | - | - | 0.979 | 0.982 | 0.493 | 1.25x | 15.1/23.1/27.4% | 1.8/5.6% | 5 |
| 8 | 1 | 0.843 | 0.831 | 0.013 | - | - | 0.976 | 0.978 | 0.512 | 1.29x | 15.4/24.0/28.4% | 1.9/5.8% | 8 |

> servers=5: misdecodes 1

> servers=8: misdecodes 1

### `SF-servers-spread` - servers  `--scenario alpine`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.845 | 0.840 | 0.005 | - | - | 0.972 | 0.975 | 0.504 | 1.22x | 14.9/22.6/26.9% | 1.8/5.4% | 2 |
| 3 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 5 | 1 | 0.843 | 0.833 | 0.011 | - | - | 0.979 | 0.982 | 0.493 | 1.25x | 15.1/23.1/27.4% | 1.8/5.6% | 5 |
| 8 | 1 | 0.843 | 0.831 | 0.013 | - | - | 0.976 | 0.978 | 0.512 | 1.29x | 15.4/24.0/28.4% | 1.9/5.8% | 8 |

> servers=5: misdecodes 1

> servers=8: misdecodes 1

### `SF-signed` - signed  `--scenario alpine`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| True | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario alpine`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.842 | 0.835 | 0.007 | - | - | 0.971 | 0.978 | 0.492 | 1.18x | 14.3/21.5/25.6% | 1.8/5.1% | 3 |
| 1 | 1 | 0.837 | 0.830 | 0.008 | - | - | 0.967 | 0.972 | 0.501 | 1.18x | 14.4/21.6/25.8% | 1.8/5.1% | 3 |
| 2 | 1 | 0.831 | 0.822 | 0.009 | - | - | 0.958 | 0.963 | 0.517 | 1.18x | 14.4/21.8/25.9% | 1.8/5.2% | 3 |
| 4 | 1 | 0.835 | 0.825 | 0.010 | - | - | 0.963 | 0.965 | 0.529 | 1.19x | 14.6/21.9/25.9% | 1.8/5.2% | 3 |

### `SF-width` - short-id-bits  `--scenario alpine`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.835 | 0.826 | 0.009 | - | - | 0.964 | 0.965 | 0.494 | 1.22x | 14.9/22.5/26.7% | 1.8/5.4% | 3 |
| 24 | 1 | 0.841 | 0.832 | 0.009 | - | - | 0.971 | 0.974 | 0.509 | 1.22x | 14.9/22.5/26.8% | 1.8/5.4% | 3 |
| 32 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.970 | 0.971 | 0.502 | 1.23x | 14.9/22.6/27.0% | 1.8/5.4% | 3 |
| 64 | 1 | 0.841 | 0.832 | 0.009 | - | - | 0.972 | 0.974 | 0.490 | 1.23x | 15.0/22.7/27.0% | 1.9/5.4% | 3 |

### `SF-window-size` - window-size  `--scenario alpine`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.835 | 0.824 | 0.011 | - | - | 0.971 | 0.971 | 0.497 | 1.32x | 16.2/24.4/28.9% | 2.0/5.8% | 3 |
| 16 | 1 | 0.839 | 0.830 | 0.009 | - | - | 0.964 | 0.967 | 0.508 | 1.22x | 14.8/22.4/26.7% | 1.8/5.4% | 3 |
| 32 | 1 | 0.834 | 0.825 | 0.009 | - | - | 0.964 | 0.966 | 0.502 | 1.22x | 14.9/22.6/26.8% | 1.8/5.4% | 3 |

> window-size=8: misdecodes 118

> window-size=16: misdecodes 60

> window-size=32: misdecodes 29

### `TH-congestion` - no-congestion-scaling  `--scenario alpine`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.960 | 0.960 | 0.001 | - | - | 1.000 | 1.000 | 0.838 | 2.04x | 21.8/32.7/37.5% | 1.3/5.2% | 3 |
| True | 1 | 0.765 | 0.760 | 0.005 | - | - | 0.902 | 0.922 | 0.537 | 5.69x | 55.8/73.1/77.6% | 3.9/12.5% | 3 |

> no-congestion-scaling=False: misdecodes 1

> no-congestion-scaling=True: decode_failures 62

### `TH-congestion-input` - congestion-input  `--scenario alpine`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.558 | 0.542 | 0.015 | - | - | 0.660 | 0.660 | 0.198 | 4.36x | 17.2/30.1/36.7% | 1.3/6.0% | 3 |
| truesize | 1 | 0.592 | 0.576 | 0.016 | - | - | 0.698 | 0.706 | 0.195 | 3.40x | 13.2/24.1/29.7% | 1.0/5.0% | 3 |

> congestion-input=truesize: decode_failures 78

### `TH-congestion-mode` - congestion-mode  `--scenario alpine`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.964 | 0.963 | 0.001 | - | - | 1.000 | 1.000 | 0.846 | 1.92x | 20.5/31.0/35.4% | 1.2/4.9% | 3 |
| adaptive | 1 | 0.960 | 0.960 | 0.001 | - | - | 1.000 | 1.000 | 0.838 | 2.04x | 21.8/32.7/37.5% | 1.3/5.2% | 3 |

> congestion-mode=adaptive: misdecodes 1

