# Sweep blocks-2026-10-12-9356937

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** valleys
- **seed base** 9356937 · seeds 9356937
- **blocks** 87 run
- **compute** 10.5 h of simulator time across every cell
- **generated** 2026-10-12T10:31:28+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>89 warnings</summary>

- AD-amplify-worst: amplify-worst=0.1: decode_failures 9
- AD-worst: role-placement=inverse: decode_failures 10
- BL-control: protocol=sr: decode_failures 33
- BL-control: slower: 5.73 s per simulated hour against 1.82 over 52 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore: max-num-nodes=10: misdecodes 1
- DB-hotstore-stress: max-num-nodes=10: decode_failures 65
- DB-hotstore-stress: max-num-nodes=120: decode_failures 112
- DB-hotstore-stress: max-num-nodes=250: decode_failures 100
- DB-hotstore-stress: slower: 53.5 s per simulated hour against 22.1 over 52 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-platform: platform-mix=constrained: misdecodes 1
- DB-warm: warm-num-nodes=0: queue drops 15.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 106
- DB-warm: warm-num-nodes=25: queue drops 15.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 106
- DB-warm: warm-num-nodes=100: queue drops 15.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 106
- DB-warm: warm-num-nodes=2000: queue drops 15.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 106
- DG-burst: burst-loss=0.3: decode_failures 31
- DG-outage: burst-loss=0.1: decode_failures 36
- DG-outage: burst-loss=0.2: decode_failures 33
- DG-outage: burst-loss=0.3: decode_failures 37
- LD-chatty-hops: broadcast-interval-s=300: queue drops 11.0% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 15.1% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 106
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 22.4% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 108
- MS-density: nodes=40: decode_failures 2
- MS-density: nodes=120: misdecodes 1
- MS-hopscale: nodes=250: decode_failures 23
- MS-hopscale: nodes=500: decode_failures 12
- MS-oversubscribed: nodes=250: decode_failures 112
- MS-oversubscribed: nodes=500: decode_failures 5
- MS-roles: role-mix=legacy-default: misdecodes 1
- MS-stretch: stretch=2.0: decode_failures 6
- PR-dmmode-cr: faster: 1.27 s per simulated hour against 2.68 over 52 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- PR-repeats-busy: extra-repeats=False: misdecodes 1
- RF-bw500: preset=SHORT_TURBO: decode_failures 10
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 6
- RF-eu-presets: preset=SHORT_FAST: decode_failures 6
- RF-preset: preset=SHORT_FAST: decode_failures 6
- RF-preset: preset=LONG_MODERATE: misdecodes 1
- RF-preset: preset=LONG_MODERATE: decode_failures 10
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 10
- RF-txpower: tx-power=22: decode_failures 5
- RF-txpower: tx-power=17: decode_failures 17
- RT-adopt: no-adopt-hop-recommendation=False: misdecodes 1
- SF-bucket-mode: bucket-mode=global: misdecodes 35
- SF-bucket-mode: bucket-mode=time: misdecodes 54
- SF-bucket-mode: bucket-mode=window: misdecodes 26
- SF-bucket-time: time-bucket-s=600: misdecodes 143
- SF-bucket-time: time-bucket-s=1800: misdecodes 54
- SF-bucket-time: time-bucket-s=3600: misdecodes 27
- SF-cadence: trigger=interval: misdecodes 32
- SF-cadence: trigger=aimd: misdecodes 5
- SF-cadence: trigger=bucket+interval: misdecodes 39
- SF-capacity-local: capacity=4: decode_failures 35
- SF-capacity-local: capacity=8: misdecodes 1
- SF-capacity: capacity=4: decode_failures 35
- SF-capacity: capacity=8: misdecodes 1
- SF-capacity-window: capacity=8: misdecodes 22
- SF-capacity-window: capacity=16: misdecodes 16
- SF-capacity-window: capacity=32: misdecodes 26
- SF-catchup: catch-up-hours=: misdecodes 39
- SF-catchup: catch-up-hours=02-06: decode_failures 16
- SF-catchup: catch-up-hours=00-08: misdecodes 2
- SF-catchup: catch-up-hours=00-08: decode_failures 14
- SF-hops-flat: hops-apart=3: decode_failures 33
- SF-hops-flat: hops-apart=4: decode_failures 27
- SF-hops-spread: hops-apart=3: decode_failures 33
- SF-hops-spread: hops-apart=4: decode_failures 27
- SF-hops-spread: hops-apart=5: decode_failures 13
- SF-place-flat: place=spread: decode_failures 9
- SF-place-spread: place=spread: decode_failures 9
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 19
- SF-replay-order: replay-ordering=heard: misdecodes 20
- SF-servers-allrouters: servers=6: misdecodes 7
- SF-servers-flat: servers=8: misdecodes 1
- SF-servers-spread: servers=8: misdecodes 1
- SF-window-size: window-size=8: misdecodes 103
- SF-window-size: window-size=16: misdecodes 68
- SF-window-size: window-size=32: misdecodes 26
- TH-congestion-input: congestion-input=hotstore: decode_failures 112
- TH-congestion-input: congestion-input=truesize: decode_failures 1
- TH-congestion-input: slower: 22.4 s per simulated hour against 10.8 over 52 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- TH-congestion-mode: congestion-mode=adaptive: misdecodes 1
- TH-congestion: no-congestion-scaling=False: misdecodes 1
- TH-congestion: no-congestion-scaling=True: queue drops 15.3% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 106

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `BL-control` | 5.73 | 1.82 | 3.14x | 52 |
| `DB-hotstore-stress` | 53.5 | 22.1 | 2.42x | 52 |
| `TH-congestion-input` | 22.4 | 10.8 | 2.07x | 52 |
| `AD-worst` | 6.01 | 3.39 | 1.77x | 52 |
| `AD-amplify-worst` | 2.96 | 1.85 | 1.60x | 52 |
| `RF-bw500` | 2.89 | 1.85 | 1.56x | 52 |
| `PR-repeats-busy` | 2.54 | 3.79 | 0.67x | 52 |
| `LD-chatty` | 3.23 | 4.84 | 0.67x | 52 |
| `SF-capacity-local` | 1.18 | 1.78 | 0.67x | 52 |
| `DM-mode` | 2.09 | 3.14 | 0.67x | 52 |
| `RT-adopt` | 2.65 | 3.99 | 0.67x | 52 |
| `SF-place-flat` | 1.88 | 2.86 | 0.66x | 52 |
| `AD-badrouters` | 1.3 | 2 | 0.65x | 52 |
| `MS-siting` | 1.2 | 1.86 | 0.65x | 51 |
| `RF-duct` | 1.11 | 1.75 | 0.64x | 52 |
| `SF-capacity-window` | 0.977 | 1.61 | 0.61x | 52 |
| `SF-jitter-global` | 1.05 | 1.77 | 0.59x | 52 |
| `DB-hotstore` | 1.4 | 2.36 | 0.59x | 52 |
| `PR-protocol` | 0.817 | 1.39 | 0.59x | 52 |
| `DG-loss` | 1.33 | 2.28 | 0.58x | 52 |
| `RT-spread` | 1.36 | 2.33 | 0.58x | 52 |
| `SF-bucket-time` | 0.922 | 1.59 | 0.58x | 52 |
| `FW-firmware` | 0.983 | 1.7 | 0.58x | 52 |
| `SF-cadence` | 2.03 | 3.63 | 0.56x | 52 |
| `LD-traceroute` | 1.15 | 2.08 | 0.55x | 52 |
| `SF-resolve` | 0.831 | 1.54 | 0.54x | 52 |
| `AD-siting` | 0.759 | 1.42 | 0.54x | 52 |
| `SF-width` | 0.892 | 1.67 | 0.54x | 52 |
| `MS-roles` | 0.889 | 1.72 | 0.52x | 52 |
| `FW-mixed` | 0.865 | 1.68 | 0.51x | 52 |
| `SF-advert-transport` | 0.882 | 1.72 | 0.51x | 52 |
| `AD-amplifiers` | 0.815 | 1.6 | 0.51x | 52 |
| `SF-sr-retries` | 0.783 | 1.56 | 0.50x | 52 |
| `PR-dmmode-cr` | 1.27 | 2.68 | 0.47x | 52 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.927 | 0.927 | 0.832 → 0.837 | 1.2x bytes_on_air | up | 3 |
| `MS-siting` | siting-mix | **text** | 0.179 → 0.977 | 0.798 | 0.176 → 0.977 | 3.5x sr_airtime | up | 4 |
| `BL-control` | protocol | **held** | 0 → 0.772 | 0.772 | 0.831 → 0.837 | 1x bytes_on_air | up | 2 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.143 → 0.887 | 0.744 | 0.113 → 0.782 | 95x sr_airtime | down | 4 |
| `RF-preset-turbo` | preset | **text** | 0.092 → 0.834 | 0.742 | 0.089 → 0.832 | 4.1x advert_bytes | up | 5 |
| `RF-txpower` | tx-power | **text** | 0.132 → 0.834 | 0.702 | 0.129 → 0.832 | 4.4x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **text** | 0.136 → 0.813 | 0.676 | 0.134 → 0.810 | 2.8x advert_bytes | down | 3 |
| `MS-stretch` | stretch | **text** | 0.188 → 0.834 | 0.646 | 0.185 → 0.832 | 4.1x sr_airtime | down | 4 |
| `RF-bw500` | preset | **text** | 0.255 → 0.777 | 0.522 | 0.240 → 0.773 | 2.6x sr_bytes | up | 3 |
| `MS-hopscale` | nodes | **text** | 0.333 → 0.834 | 0.501 | 0.328 → 0.832 | 15x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.469 → 0.957 | 0.488 | 0.333 → 0.810 | 4.4x bytes_on_air | down | 3 |
| `SF-place-flat` | place | **held** | 0.534 → 0.949 | 0.414 | 0.826 → 0.842 | 1.8x advert_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.534 → 0.949 | 0.414 | 0.826 → 0.842 | 1.8x advert_bytes | up | 6 |
| `RF-eu-presets` | preset | **text** | 0.439 → 0.834 | 0.394 | 0.422 → 0.832 | 3x sr_bytes | up | 4 |
| `RF-preset` | preset | **text** | 0.439 → 0.834 | 0.394 | 0.422 → 0.832 | 3x sr_bytes | up | 3 |
| `SF-hops-flat` | hops-apart | **held** | 0.574 → 0.927 | 0.354 | 0.823 → 0.833 | 5.9x sr_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.574 → 0.927 | 0.354 | 0.823 → 0.833 | 5.9x sr_bytes | down | 5 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.557 → 0.904 | 0.347 | 0.323 → 0.555 | 6.5x sr_airtime | up | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.539 → 0.882 | 0.343 | 0.526 → 0.881 | 8.4x sr_airtime | down | 3 |
| `MS-topology` | topology | **held** | 0.661 → 0.992 | 0.331 | 0.610 → 0.938 | 2x sr_airtime | up | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.575 → 0.856 | 0.281 | 0.554 → 0.855 | 6.3x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.560 → 0.834 | 0.274 | 0.533 → 0.832 | 3.7x sr_bytes | down | 4 |
| `DG-burst` | burst-loss | **text** | 0.571 → 0.834 | 0.263 | 0.531 → 0.832 | 3.5x sr_bytes | down | 4 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.451 → 0.702 | 0.251 | 0.437 → 0.691 | 1.5x sr_airtime | up | 2 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.739 → 0.954 | 0.216 | 0.729 → 0.952 | 4.4x sr_airtime | down | 2 |
| `MS-density` | nodes | **text** | 0.773 → 0.967 | 0.194 | 0.763 → 0.965 | 6.4x sr_airtime | up | 5 |
| `SC-signing` | signature-policy | **text** | 0.671 → 0.834 | 0.163 | 0.671 → 0.832 | 1.6x sr_airtime | down | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.686 → 0.849 | 0.163 | 0.654 → 0.847 | 2.4x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.686 → 0.849 | 0.163 | 0.654 → 0.847 | 2.3x sr_bytes | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.686 → 0.834 | 0.148 | 0.654 → 0.832 | 2.2x sr_bytes | up | 2 |
| `RF-noise` | noise-profile | **text** | 0.701 → 0.838 | 0.136 | 0.697 → 0.835 | 1.2x sr_airtime | down | 4 |
| `MS-size` | nodes | **text** | 0.744 → 0.874 | 0.130 | 0.735 → 0.865 | 5.6x sr_bytes | down | 5 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.834 → 0.943 | 0.109 | 0.832 → 0.937 | 3.4x sr_bytes | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.834 → 0.940 | 0.107 | 0.832 → 0.938 | 1.3x bytes_on_air | up | 3 |
| `AD-badrouters` | role-placement | **text** | 0.712 → 0.813 | 0.101 | 0.698 → 0.810 | 1.4x sr_bytes | down | 3 |
| `DG-loss` | extra-loss | **text** | 0.738 → 0.834 | 0.096 | 0.729 → 0.832 | 1.5x sr_bytes | down | 4 |
| `DB-hotstore` | max-num-nodes | **text** | 0.757 → 0.852 | 0.094 | 0.751 → 0.851 | 2.1x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.766 → 0.852 | 0.085 | 0.760 → 0.851 | 2.1x sr_airtime | down | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.834 → 0.914 | 0.080 | 0.832 → 0.912 | 1.2x bytes_on_air | up | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.804 → 0.883 | 0.079 | 0.802 → 0.882 | 5.3x sr_airtime | up | 4 |
| `FW-versions` | profile | **text** | 0.834 → 0.908 | 0.074 | 0.832 → 0.906 | 3.1x bytes_on_air | down | 5 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.683 → 0.747 | 0.064 | 0.673 → 0.738 | 1.3x sr_airtime | down | 2 |
| `FW-firmware` | profile | **text** | 0.834 → 0.897 | 0.063 | 0.832 → 0.892 | 3.1x bytes_on_air | down | 2 |
| `AD-flooding` | role-mix | **text** | 0.813 → 0.869 | 0.056 | 0.810 → 0.868 | 2.3x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.813 → 0.869 | 0.056 | 0.810 → 0.868 | 2.3x bytes_on_air | up | 3 |
| `FW-mixed` | legacy-fraction | **text** | 0.834 → 0.890 | 0.056 | 0.832 → 0.886 | 2.1x bytes_on_air | up | 4 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.834 → 0.886 | 0.052 | 0.832 → 0.883 | 2.1x bytes_on_air | up | 4 |
| `MS-roles-fav` | role-mix | **held** | 0.916 → 0.969 | 0.052 | 0.817 → 0.868 | 1.1x advert_bytes | down | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.894 → 0.943 | 0.049 | 0.541 → 0.579 | 1.3x sr_airtime | up | 2 |
| `MS-roles` | role-mix | **text** | 0.813 → 0.854 | 0.041 | 0.810 → 0.852 | 1.1x sr_airtime | down | 2 |
| `RT-hopassign` | hop-assign | **text** | 0.834 → 0.872 | 0.038 | 0.832 → 0.870 | 1.1x advert_bytes | up | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.834 → 0.870 | 0.037 | 0.832 → 0.869 | 3.3x bytes_on_air | down | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.800 → 0.834 | 0.033 | 0.795 → 0.832 | 1.4x sr_airtime | down | 4 |
| `SF-catchup` | catch-up-hours | **text** | 0.808 → 0.839 | 0.032 | 0.802 → 0.838 | 11x sr_bytes | up | 3 |
| `SF-cadence` | trigger | **text** | 0.808 → 0.839 | 0.031 | 0.802 → 0.839 | 24x sr_bytes | down | 4 |
| `DM-mode` | dm-mode | **text** | 0.794 → 0.822 | 0.028 | 0.794 → 0.822 | 1.1x sr_airtime | up | 3 |
| `LD-diurnal` | diurnal | **text** | 0.834 → 0.861 | 0.027 | 0.832 → 0.859 | 1.3x sr_bytes | down | 3 |
| `MS-router-late` | router-late-fraction | **text** | 0.834 → 0.856 | 0.022 | 0.832 → 0.854 | 1.3x bytes_on_air | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.906 → 0.927 | 0.021 | 0.832 → 0.836 | 25x sr_airtime | down | 3 |
| `SF-advert-transport` | advert-transport | **held** | 0.927 → 0.947 | 0.019 | 0.832 → 0.844 | 3.9x sr_airtime | up | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.840 → 0.859 | 0.019 | 0.837 → 0.857 | 1x sr_bytes | up | 2 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.799 → 0.815 | 0.016 | 0.799 → 0.815 | 1.1x sr_airtime | down | 2 |
| `SF-resolve` | resolve | **held** | 0.927 → 0.943 | 0.015 | 0.832 → 0.840 | 5.6x advert_bytes | = | 3 |
| `SF-capacity` | capacity | **held** | 0.927 → 0.939 | 0.011 | 0.832 → 0.837 | 5.4x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.927 → 0.939 | 0.011 | 0.832 → 0.837 | 5.4x advert_bytes | up | 5 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.927 → 0.939 | 0.011 | 0.832 → 0.837 | 1.1x sr_bytes | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.927 → 0.939 | 0.011 | 0.832 → 0.837 | 1.1x sr_bytes | up | 4 |
| `SF-width` | short-id-bits | **text** | 0.831 → 0.841 | 0.010 | 0.828 → 0.839 | 3.2x advert_bytes | up | 4 |
| `AD-worst` | role-placement | **text** | 0.757 → 0.767 | 0.010 | 0.744 → 0.760 | 1.4x sr_bytes | down | 2 |
| `SF-provide-transport` | provide-transport | **text** | 0.834 → 0.844 | 0.010 | 0.829 → 0.832 | 1.8x sr_airtime | up | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.922 → 0.932 | 0.010 | 0.830 → 0.834 | 3.1x advert_bytes | up | 4 |
| `SF-servers-flat` | servers | **held** | 0.927 → 0.937 | 0.010 | 0.830 → 0.840 | 7.1x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.927 → 0.937 | 0.010 | 0.830 → 0.840 | 7.1x sr_bytes | up | 4 |
| `PR-repeats` | extra-repeats | **held** | 0.927 → 0.936 | 0.009 | 0.832 → 0.833 | 1.1x sr_bytes | up | 2 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.928 → 0.936 | 0.008 | 0.829 → 0.833 | 5.3x advert_bytes | down | 3 |
| `SF-servers-allrouters` | servers | **text** | 0.836 → 0.843 | 0.007 | 0.833 → 0.842 | 2.4x sr_bytes | down | 2 |
| `SF-sr-retries` | sr-retries | **held** | 0.926 → 0.933 | 0.007 | 0.830 → 0.837 | 1.1x sr_airtime | up | 4 |
| `SF-replay-order` | replay-ordering | **held** | 0.927 → 0.933 | 0.006 | 0.832 → 0.834 | 1.2x sr_bytes | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.954 → 0.960 | 0.005 | 0.952 → 0.958 | 1.1x sr_bytes | down | 2 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.815 → 0.820 | 0.005 | 0.815 → 0.820 | 1.1x sr_airtime | down | 2 |
| `SF-capacity-window` | capacity | **held** | 0.927 → 0.932 | 0.005 | 0.830 → 0.834 | 2.3x advert_bytes | up | 3 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.951 → 0.954 | 0.004 | 0.948 → 0.952 | 1.2x sr_airtime | down | 2 |
| `SF-window-size` | window-size | **held** | 0.932 → 0.935 | 0.003 | 0.830 → 0.834 | 5.4x advert_bytes | down | 3 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.954 → 0.956 | 0.002 | 0.952 → 0.954 | 1x sr_bytes | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.844 → 0.845 | 0.001 | 0.829 → 0.829 | 1.2x sr_bytes | up | 2 |

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
| none | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| sprinkled | 1 | 0.882 | 0.880 | 0.002 | - | - | 0.951 | 0.951 | 0.179 | 1.16x | 18.1/24.1/28.1% | 1.3/5.4% | 3 |
| arms-race | 1 | 0.940 | 0.938 | 0.002 | - | - | 0.970 | 0.970 | 0.788 | 1.02x | 21.0/26.8/30.8% | 1.1/5.4% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario valleys`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 0.1 | 1 | 0.903 | 0.892 | 0.011 | - | - | 0.947 | 0.963 | 0.488 | 1.26x | 18.8/26.1/28.3% | 1.8/5.4% | 3 |
| 0.3 | 1 | 0.943 | 0.937 | 0.005 | - | - | 0.995 | 0.996 | 0.833 | 1.00x | 18.6/24.0/28.0% | 1.2/4.5% | 3 |

> amplify-worst=0.1: decode_failures 9

### `AD-badrouters` - role-placement  `--scenario valleys`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.813 | 0.810 | 0.003 | - | - | 0.923 | 0.924 | 0.000 | 1.20x | 17.0/25.9/29.3% | 1.9/5.5% | 3 |
| inverse | 1 | 0.712 | 0.698 | 0.014 | - | - | 0.877 | 0.879 | 0.000 | 1.06x | 14.3/19.6/23.0% | 2.0/3.4% | 3 |
| random | 1 | 0.787 | 0.769 | 0.018 | - | - | 0.914 | 0.914 | 0.000 | 1.07x | 14.7/20.0/23.2% | 1.9/4.6% | 3 |

### `AD-flooding` - role-mix  `--scenario valleys`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.813 | 0.810 | 0.003 | - | - | 0.923 | 0.924 | 0.000 | 1.20x | 17.0/25.9/29.3% | 1.9/5.5% | 3 |
| all-routers | 1 | 0.869 | 0.868 | 0.001 | - | - | 0.928 | 0.929 | 0.000 | 2.78x | 35.7/44.6/46.8% | 4.7/5.2% | 3 |

### `AD-nomute` - role-mix  `--scenario valleys`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.813 | 0.810 | 0.003 | - | - | 0.923 | 0.924 | 0.000 | 1.20x | 17.0/25.9/29.3% | 1.9/5.5% | 3 |
| no-mute | 1 | 0.860 | 0.858 | 0.002 | - | - | 0.973 | 0.975 | 0.000 | 1.29x | 17.0/24.6/27.2% | 1.9/5.4% | 3 |
| all-routers | 1 | 0.869 | 0.868 | 0.001 | - | - | 0.928 | 0.929 | 0.000 | 2.78x | 35.7/44.6/46.8% | 4.7/5.2% | 3 |

### `AD-siting` - siting-mix  `--scenario valleys`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.813 | 0.810 | 0.003 | - | - | 0.923 | 0.924 | 0.000 | 1.20x | 17.0/25.9/29.3% | 1.9/5.5% | 3 |
| local-typical | 1 | 0.685 | 0.680 | 0.005 | - | - | 0.839 | 0.840 | 0.000 | 1.33x | 13.4/26.1/30.2% | 2.1/5.3% | 3 |
| basement-heavy | 1 | 0.136 | 0.134 | 0.003 | - | - | 0.338 | 0.340 | 0.000 | 0.82x | 3.4/13.4/16.6% | 1.1/4.1% | 3 |

### `AD-worst` - role-placement  `--scenario valleys`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.767 | 0.760 | 0.007 | - | - | 0.899 | 0.900 | 0.000 | 2.46x | 14.6/30.6/38.4% | 2.0/5.6% | 3 |
| inverse | 1 | 0.757 | 0.744 | 0.014 | - | - | 0.893 | 0.905 | 0.000 | 2.31x | 12.9/24.9/31.4% | 1.9/3.2% | 3 |

> role-placement=inverse: decode_failures 10

### `BL-control` - protocol  `--scenario valleys`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.837 | 0.837 | 0.000 | - | - | 0 | 0.000 | 0.000 | 1.26x | 17.2/25.0/27.6% | 1.9/5.2% | 3 |
| sr | 1 | 0.844 | 0.831 | 0.013 | - | - | 0.772 | 0.943 | 0.000 | 1.30x | 17.8/25.8/28.3% | 2.0/5.7% | 3 |

> protocol=sr: decode_failures 33

> slower: 5.73 s per simulated hour against 1.82 over 52 prior run(s) - 3.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario valleys`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.757 | 0.751 | 0.006 | - | - | 0.846 | 0.846 | 0.000 | 2.95x | 41.0/56.9/60.2% | 4.2/10.2% | 3 |
| 100 | 1 | 0.852 | 0.851 | 0.001 | - | - | 0.918 | 0.919 | 0.000 | 1.51x | 21.0/30.5/33.2% | 2.1/5.3% | 3 |
| 120 | 1 | 0.852 | 0.851 | 0.001 | - | - | 0.918 | 0.919 | 0.000 | 1.51x | 21.0/30.5/33.2% | 2.1/5.3% | 3 |
| 250 | 1 | 0.852 | 0.851 | 0.001 | - | - | 0.918 | 0.919 | 0.000 | 1.51x | 21.0/30.5/33.2% | 2.1/5.3% | 3 |

> max-num-nodes=10: misdecodes 1

### `DB-hotstore-stress` - max-num-nodes  `--scenario valleys`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.330 | 0.323 | 0.007 | - | - | 0.557 | 0.726 | 0.145 | 11.44x | 38.5/61.1/74.8% | 3.9/11.6% | 3 |
| 120 | 1 | 0.552 | 0.541 | 0.011 | - | - | 0.894 | 0.921 | 0.207 | 4.61x | 15.2/31.9/42.3% | 1.5/6.9% | 3 |
| 250 | 1 | 0.565 | 0.555 | 0.010 | - | - | 0.904 | 0.924 | 0.219 | 4.46x | 14.7/30.5/40.5% | 1.4/6.7% | 3 |

> max-num-nodes=10: decode_failures 65

> max-num-nodes=120: decode_failures 112

> max-num-nodes=250: decode_failures 100

> slower: 53.5 s per simulated hour against 22.1 over 52 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-platform` - platform-mix  `--scenario valleys`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.852 | 0.851 | 0.001 | - | - | 0.918 | 0.919 | 0.000 | 1.51x | 21.0/30.5/33.2% | 2.1/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.852 | 0.851 | 0.001 | - | - | 0.918 | 0.919 | 0.000 | 1.51x | 21.0/30.5/33.2% | 2.1/5.3% | 3 |
| constrained | 1 | 0.766 | 0.760 | 0.006 | - | - | 0.860 | 0.861 | 0.000 | 2.96x | 40.9/56.9/60.3% | 4.2/10.2% | 3 |

> platform-mix=constrained: misdecodes 1

### `DB-warm` - warm-num-nodes  `--scenario valleys`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.747 | 0.738 | 0.009 | - | - | 0.865 | 0.917 | 0.469 | 5.47x | 59.5/73.1/78.1% | 4.1/12.0% | 3 |
| 25 | 1 | 0.747 | 0.738 | 0.009 | - | - | 0.865 | 0.917 | 0.469 | 5.47x | 59.5/73.1/78.1% | 4.1/12.0% | 3 |
| 100 | 1 | 0.747 | 0.738 | 0.009 | - | - | 0.865 | 0.917 | 0.469 | 5.47x | 59.5/73.1/78.1% | 4.1/12.0% | 3 |
| 2000 | 1 | 0.747 | 0.738 | 0.009 | - | - | 0.865 | 0.917 | 0.469 | 5.47x | 59.5/73.1/78.1% | 4.1/12.0% | 3 |

> warm-num-nodes=0: queue drops 15.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 106

> warm-num-nodes=25: queue drops 15.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 106

> warm-num-nodes=100: queue drops 15.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 106

> warm-num-nodes=2000: queue drops 15.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 106

### `DG-burst` - burst-loss  `--scenario valleys`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 0.1 | 1 | 0.753 | 0.741 | 0.011 | - | - | 0.929 | 0.931 | 0.000 | 1.24x | 17.2/25.3/27.7% | 1.8/5.0% | 3 |
| 0.2 | 1 | 0.664 | 0.637 | 0.026 | - | - | 0.898 | 0.900 | 0.000 | 1.14x | 16.0/23.8/25.7% | 1.7/4.4% | 3 |
| 0.3 | 1 | 0.571 | 0.531 | 0.040 | - | - | 0.831 | 0.862 | 0.000 | 1.06x | 15.1/22.7/24.5% | 1.6/4.0% | 3 |

> burst-loss=0.3: decode_failures 31

### `DG-loss` - extra-loss  `--scenario valleys`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 0.1 | 1 | 0.814 | 0.810 | 0.004 | - | - | 0.924 | 0.925 | 0.000 | 1.36x | 18.7/27.2/29.4% | 2.0/5.3% | 3 |
| 0.2 | 1 | 0.787 | 0.781 | 0.006 | - | - | 0.921 | 0.922 | 0.000 | 1.40x | 19.3/28.2/30.2% | 2.0/5.2% | 3 |
| 0.3 | 1 | 0.738 | 0.729 | 0.008 | - | - | 0.896 | 0.898 | 0.000 | 1.44x | 20.3/29.4/31.3% | 2.1/5.0% | 3 |

### `DG-outage` - burst-loss  `--scenario valleys`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 0.1 | 1 | 0.741 | 0.731 | 0.011 | - | - | 0.906 | 0.924 | 0.000 | 1.23x | 16.9/24.9/27.3% | 1.9/5.1% | 3 |
| 0.2 | 1 | 0.638 | 0.619 | 0.019 | - | - | 0.823 | 0.866 | 0.000 | 1.15x | 16.1/23.8/26.0% | 1.7/4.2% | 3 |
| 0.3 | 1 | 0.560 | 0.533 | 0.026 | - | - | 0.836 | 0.885 | 0.000 | 1.11x | 16.1/24.2/25.8% | 1.7/5.2% | 3 |

> burst-loss=0.1: decode_failures 36

> burst-loss=0.2: decode_failures 33

> burst-loss=0.3: decode_failures 37

### `DM-mode` - dm-mode  `--scenario valleys`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.794 | 0.794 | 0.000 | - | - | 0.906 | 0.908 | 0.000 | 1.71x | 23.4/33.7/36.9% | 2.5/7.1% | 3 |
| directed-with-late-flood | 1 | 0.820 | 0.820 | 0.000 | - | - | 0.925 | 0.926 | 0.000 | 1.55x | 21.2/30.6/33.7% | 2.4/6.5% | 3 |
| m4-early-flood | 1 | 0.822 | 0.822 | 0.000 | - | - | 0.929 | 0.931 | 0.000 | 1.54x | 21.1/30.6/33.6% | 2.4/6.4% | 3 |

### `FW-firmware` - profile  `--scenario valleys`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.897 | 0.892 | 0.004 | - | - | 0.981 | 0.983 | 0.551 | 0.74x | 10.0/11.9/14.3% | 1.2/2.0% | 3 |
| 2.8 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario valleys`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 0.25 | 1 | 0.877 | 0.873 | 0.004 | - | - | 0.967 | 0.969 | 0.509 | 1.16x | 16.5/22.5/24.8% | 1.7/5.0% | 3 |
| 0.5 | 1 | 0.862 | 0.859 | 0.003 | - | - | 0.950 | 0.953 | 0.340 | 0.99x | 13.9/19.6/23.5% | 1.5/4.2% | 3 |
| 0.75 | 1 | 0.890 | 0.886 | 0.003 | - | - | 0.970 | 0.970 | 0.469 | 0.88x | 10.9/15.5/16.9% | 1.3/2.9% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario valleys`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 0.25 | 1 | 0.870 | 0.866 | 0.005 | - | - | 0.962 | 0.963 | 0.492 | 1.12x | 16.2/22.5/24.7% | 1.6/4.9% | 3 |
| 0.5 | 1 | 0.868 | 0.864 | 0.004 | - | - | 0.962 | 0.962 | 0.329 | 0.95x | 13.4/18.9/23.6% | 1.4/4.2% | 3 |
| 0.75 | 1 | 0.886 | 0.883 | 0.003 | - | - | 0.963 | 0.963 | 0.504 | 0.88x | 11.0/15.7/17.2% | 1.4/2.9% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario valleys`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.870 | 0.869 | 0.001 | - | - | 0.954 | 0.955 | 0.000 | 0.69x | 9.7/14.5/16.1% | 1.1/3.1% | 3 |
| signing=true | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |

### `FW-versions` - profile  `--scenario valleys`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.888 | 0.885 | 0.004 | - | - | 0.974 | 0.975 | 0.456 | 0.76x | 10.8/13.4/16.4% | 1.2/2.4% | 3 |
| 2.5 | 1 | 0.887 | 0.884 | 0.004 | - | - | 0.974 | 0.974 | 0.453 | 0.77x | 10.7/13.2/16.3% | 1.2/2.4% | 3 |
| 2.6 | 1 | 0.878 | 0.874 | 0.004 | - | - | 0.969 | 0.970 | 0.428 | 0.74x | 10.5/13.2/16.4% | 1.2/2.4% | 3 |
| 2.7 | 1 | 0.908 | 0.906 | 0.001 | - | - | 0.985 | 0.985 | 0.462 | 0.76x | 10.9/14.8/18.3% | 1.1/3.0% | 3 |
| 2.8 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.856 | 0.855 | 0.002 | - | - | 0.946 | 0.946 | 0.000 | 0.90x | 12.0/17.7/19.4% | 1.3/3.6% | 3 |
| 900 | 1 | 0.804 | 0.802 | 0.003 | - | - | 0.907 | 0.907 | 0.000 | 2.06x | 27.7/40.1/44.1% | 3.1/8.5% | 3 |
| 300 | 1 | 0.575 | 0.554 | 0.020 | - | - | 0.763 | 0.763 | 0.000 | 4.37x | 55.4/72.6/76.6% | 6.6/16.8% | 3 |

### `LD-chatty-hops` - broadcast-interval-s  `--scenario valleys`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.882 | 0.881 | 0.001 | - | - | 0.946 | 0.947 | 0.000 | 0.94x | 12.4/17.7/19.3% | 1.4/3.6% | 3 |
| 900 | 1 | 0.811 | 0.808 | 0.003 | - | - | 0.877 | 0.877 | 0.000 | 2.31x | 30.4/42.2/46.0% | 3.4/8.7% | 3 |
| 300 | 1 | 0.539 | 0.526 | 0.013 | - | - | 0.657 | 0.657 | 0.000 | 4.88x | 58.5/74.2/77.6% | 7.2/17.4% | 3 |

> broadcast-interval-s=300: queue drops 11.0% of transmissions - airtime here is measured through a cap

### `LD-diurnal` - diurnal  `--scenario valleys`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.861 | 0.859 | 0.002 | - | - | 0.953 | 0.953 | 0.000 | 1.20x | 16.4/24.1/26.5% | 1.8/5.0% | 3 |
| sinusoid | 1 | 0.850 | 0.848 | 0.002 | - | - | 0.941 | 0.942 | 0.000 | 1.19x | 15.9/23.2/25.5% | 1.8/4.8% | 3 |
| commuter | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.804 | 0.802 | 0.003 | - | - | 0.907 | 0.907 | 0.000 | 2.06x | 27.7/40.1/44.1% | 3.1/8.5% | 3 |
| 3600 | 1 | 0.856 | 0.855 | 0.002 | - | - | 0.946 | 0.946 | 0.000 | 0.90x | 12.0/17.7/19.4% | 1.3/3.6% | 3 |
| 10800 | 1 | 0.873 | 0.873 | 0.000 | - | - | 0.954 | 0.955 | 0.000 | 0.57x | 7.5/10.9/11.9% | 0.9/2.2% | 3 |
| 43200 | 1 | 0.883 | 0.882 | 0.000 | - | - | 0.963 | 0.963 | 0.000 | 0.42x | 5.6/8.2/9.1% | 0.6/1.7% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario valleys`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 0.25 | 1 | 0.832 | 0.830 | 0.002 | - | - | 0.929 | 0.930 | 0.000 | 1.40x | 19.1/27.5/30.3% | 2.2/5.8% | 3 |
| 1.0 | 1 | 0.826 | 0.823 | 0.004 | - | - | 0.930 | 0.931 | 0.000 | 1.53x | 20.9/30.3/33.4% | 2.3/6.5% | 3 |
| 4.0 | 1 | 0.800 | 0.795 | 0.006 | - | - | 0.914 | 0.914 | 0.000 | 1.89x | 26.2/38.6/41.6% | 2.8/8.3% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario valleys`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.747 | 0.738 | 0.009 | - | - | 0.865 | 0.917 | 0.469 | 5.47x | 59.5/73.1/78.1% | 4.1/12.0% | 3 |
| 1.0 | 1 | 0.683 | 0.673 | 0.009 | - | - | 0.802 | 0.895 | 0.410 | 5.98x | 62.7/75.4/79.5% | 4.5/12.9% | 3 |

> traceroute-per-hour=0.0: queue drops 15.1% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 106

> traceroute-per-hour=1.0: queue drops 22.4% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 108

### `MS-density` - nodes  `--scenario valleys`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.773 | 0.763 | 0.009 | - | - | 0.862 | 0.906 | 0.401 | 1.45x | 20.0/30.9/35.5% | 3.4/7.2% | 3 |
| 60 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 90 | 1 | 0.938 | 0.936 | 0.002 | - | - | 0.992 | 0.993 | 0.562 | 1.61x | 19.4/30.5/34.2% | 1.5/5.0% | 3 |
| 120 | 1 | 0.954 | 0.952 | 0.002 | - | - | 0.998 | 0.998 | 0.709 | 1.93x | 23.0/34.3/39.1% | 1.3/5.1% | 3 |
| 150 | 1 | 0.967 | 0.965 | 0.002 | - | - | 0.999 | 0.999 | 0.747 | 2.70x | 27.9/45.0/51.0% | 1.3/5.6% | 3 |

> nodes=40: decode_failures 2

> nodes=120: misdecodes 1

### `MS-hopscale` - nodes  `--scenario valleys`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 120 | 1 | 0.811 | 0.805 | 0.007 | - | - | 0.962 | 0.964 | 0.219 | 2.32x | 17.2/34.1/40.4% | 1.6/5.6% | 3 |
| 250 | 1 | 0.556 | 0.546 | 0.011 | - | - | 0.918 | 0.922 | 0.213 | 4.96x | 16.2/34.8/45.4% | 1.6/7.4% | 3 |
| 500 | 1 | 0.333 | 0.328 | 0.005 | - | - | 0.468 | 0.468 | 0.112 | 10.26x | 18.0/37.0/49.2% | 1.7/6.2% | 3 |

> nodes=250: decode_failures 23

> nodes=500: decode_failures 12

### `MS-oversubscribed` - nodes  `--scenario valleys`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.817 | 0.810 | 0.006 | - | - | 0.957 | 0.959 | 0.200 | 2.17x | 16.0/31.9/37.7% | 1.5/5.1% | 3 |
| 250 | 1 | 0.552 | 0.541 | 0.011 | - | - | 0.894 | 0.921 | 0.207 | 4.61x | 15.2/31.9/42.3% | 1.5/6.9% | 3 |
| 500 | 1 | 0.338 | 0.333 | 0.005 | - | - | 0.469 | 0.470 | 0.115 | 9.60x | 16.6/34.6/46.9% | 1.6/5.8% | 3 |

> nodes=250: decode_failures 112

> nodes=500: decode_failures 5

### `MS-roles` - role-mix  `--scenario valleys`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.854 | 0.852 | 0.002 | - | - | 0.963 | 0.964 | 0.000 | 1.29x | 17.6/26.0/28.6% | 2.0/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.813 | 0.810 | 0.003 | - | - | 0.923 | 0.924 | 0.000 | 1.20x | 17.0/25.9/29.3% | 1.9/5.5% | 3 |

> role-mix=legacy-default: misdecodes 1

### `MS-roles-fav` - role-mix  `--scenario valleys`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.870 | 0.868 | 0.002 | - | - | 0.969 | 0.969 | 0.000 | 1.34x | 18.0/26.7/29.3% | 2.0/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.820 | 0.817 | 0.003 | - | - | 0.916 | 0.917 | 0.000 | 1.30x | 18.3/28.9/31.8% | 2.2/5.4% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario valleys`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 0.05 | 1 | 0.851 | 0.848 | 0.002 | - | - | 0.929 | 0.929 | 0.000 | 1.45x | 20.4/28.8/31.7% | 2.2/5.3% | 3 |
| 0.1 | 1 | 0.856 | 0.854 | 0.002 | - | - | 0.932 | 0.934 | 0.000 | 1.50x | 21.5/31.5/33.9% | 2.2/5.2% | 3 |
| 0.2 | 1 | 0.849 | 0.848 | 0.002 | - | - | 0.916 | 0.917 | 0.000 | 1.72x | 24.9/36.6/40.5% | 2.4/5.1% | 3 |

### `MS-siting` - siting-mix  `--scenario valleys`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| local-typical | 1 | 0.717 | 0.712 | 0.005 | - | - | 0.851 | 0.853 | 0.000 | 1.45x | 14.0/24.8/30.1% | 1.9/5.5% | 3 |
| event | 1 | 0.179 | 0.176 | 0.003 | - | - | 0.389 | 0.393 | 0.000 | 1.15x | 6.6/13.7/19.4% | 1.6/4.2% | 3 |
| backbone | 1 | 0.977 | 0.977 | 0.000 | - | - | 0.998 | 0.998 | 0.861 | 1.02x | 26.4/31.2/33.9% | 1.1/5.5% | 3 |

### `MS-size` - nodes  `--scenario valleys`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.874 | 0.865 | 0.009 | - | - | 0.961 | 0.964 | 0.559 | 1.48x | 26.5/34.2/38.9% | 3.3/7.6% | 3 |
| 60 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 90 | 1 | 0.796 | 0.791 | 0.005 | - | - | 0.922 | 0.923 | 0.000 | 1.66x | 16.4/28.1/32.6% | 1.5/5.3% | 3 |
| 120 | 1 | 0.811 | 0.805 | 0.007 | - | - | 0.962 | 0.964 | 0.219 | 2.32x | 17.2/34.1/40.4% | 1.6/5.6% | 3 |
| 150 | 1 | 0.744 | 0.735 | 0.009 | - | - | 0.913 | 0.914 | 0.154 | 2.91x | 16.6/32.2/36.3% | 1.6/5.9% | 3 |

### `MS-stretch` - stretch  `--scenario valleys`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 1.25 | 1 | 0.650 | 0.638 | 0.012 | - | - | 0.826 | 0.832 | 0.000 | 1.24x | 14.0/19.5/22.5% | 1.8/5.0% | 3 |
| 1.5 | 1 | 0.451 | 0.437 | 0.014 | - | - | 0.706 | 0.710 | 0.000 | 1.25x | 12.1/16.5/18.6% | 1.8/5.0% | 3 |
| 2.0 | 1 | 0.188 | 0.185 | 0.003 | - | - | 0.291 | 0.335 | 0.000 | 1.17x | 6.0/11.7/15.7% | 1.8/4.5% | 3 |

> stretch=2.0: decode_failures 6

### `MS-topology` - topology  `--scenario valleys`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| clustered | 1 | 0.944 | 0.938 | 0.006 | - | - | 0.992 | 0.993 | 0.683 | 1.03x | 19.6/25.7/28.6% | 1.1/5.4% | 3 |
| corridor | 1 | 0.627 | 0.610 | 0.017 | - | - | 0.661 | 0.662 | 0.376 | 1.30x | 15.4/20.6/23.2% | 2.2/5.0% | 3 |
| hub | 1 | 0.917 | 0.909 | 0.008 | - | - | 0.972 | 0.973 | 0.656 | 1.16x | 27.7/37.0/38.7% | 1.5/5.5% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario valleys`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.820 | 0.820 | 0.000 | - | - | 0.925 | 0.926 | 0.000 | 1.55x | 21.2/30.6/33.7% | 2.4/6.5% | 3 |
| True | 1 | 0.815 | 0.815 | 0.000 | - | - | 0.925 | 0.928 | 0.000 | 1.53x | 21.0/30.6/33.4% | 2.3/6.5% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario valleys`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.815 | 0.815 | 0.000 | - | - | 0.925 | 0.928 | 0.000 | 1.53x | 21.0/30.6/33.4% | 2.3/6.5% | 3 |
| m4-early-flood | 1 | 0.799 | 0.799 | 0.000 | - | - | 0.910 | 0.910 | 0.000 | 1.55x | 21.3/31.0/34.0% | 2.4/6.5% | 3 |

> faster: 1.27 s per simulated hour against 2.68 over 52 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `PR-protocol` - protocol  `--scenario valleys`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.837 | 0.837 | 0.000 | - | - | 0 | 0.000 | 0.000 | 1.26x | 17.2/25.0/27.6% | 1.9/5.2% | 3 |
| chain | 1 | 0.838 | 0.836 | 0.002 | - | - | 0.921 | 0.935 | 0.000 | 1.48x | 20.0/29.1/32.6% | 2.3/6.1% | 3 |
| sr | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |

### `PR-repeats` - extra-repeats  `--scenario valleys`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| True | 1 | 0.836 | 0.833 | 0.003 | - | - | 0.936 | 0.936 | 0.000 | 1.31x | 17.7/25.8/28.4% | 2.0/5.4% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario valleys`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.954 | 0.952 | 0.002 | - | - | 0.998 | 0.998 | 0.709 | 1.93x | 23.0/34.3/39.1% | 1.3/5.1% | 3 |
| True | 1 | 0.956 | 0.954 | 0.002 | - | - | 0.999 | 0.999 | 0.721 | 1.98x | 23.4/34.9/39.8% | 1.3/5.2% | 3 |

> extra-repeats=False: misdecodes 1

### `RF-bw500` - preset  `--scenario valleys`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.255 | 0.240 | 0.015 | - | - | 0.512 | 0.530 | 0.000 | 0.06x | 0.4/0.8/1.0% | 0.1/0.3% | 3 |
| MEDIUM_TURBO | 1 | 0.512 | 0.496 | 0.015 | - | - | 0.747 | 0.774 | 0.000 | 0.27x | 2.6/4.1/4.5% | 0.4/1.1% | 3 |
| LONG_TURBO | 1 | 0.777 | 0.773 | 0.004 | - | - | 0.894 | 0.896 | 0.000 | 1.25x | 14.2/19.6/24.5% | 1.8/4.8% | 3 |

> preset=SHORT_TURBO: decode_failures 10

> preset=MEDIUM_TURBO: decode_failures 6

### `RF-duct` - duct-per-hour  `--scenario valleys`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 0.25 | 1 | 0.856 | 0.852 | 0.004 | - | - | 0.942 | 0.942 | 0.091 | 1.25x | 19.4/27.3/29.5% | 1.9/5.4% | 3 |
| 1.0 | 1 | 0.914 | 0.912 | 0.002 | - | - | 0.972 | 0.973 | 0.406 | 1.07x | 23.6/30.6/32.1% | 1.4/5.5% | 3 |

### `RF-eu-presets` - preset  `--scenario valleys`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.439 | 0.422 | 0.017 | - | - | 0.679 | 0.711 | 0.000 | 0.16x | 1.3/2.4/2.8% | 0.2/0.7% | 3 |
| LONG_FAST | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| LITE_FAST | 1 | 0.779 | 0.775 | 0.004 | - | - | 0.910 | 0.910 | 0.000 | 0.96x | 13.3/17.8/21.2% | 1.4/4.2% | 3 |
| NARROW_SLOW | 1 | 0.813 | 0.810 | 0.003 | - | - | 0.925 | 0.925 | 0.000 | 1.22x | 16.7/22.8/26.3% | 1.8/5.3% | 3 |

> preset=SHORT_FAST: decode_failures 6

### `RF-noise` - noise-profile  `--scenario valleys`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| temporal | 1 | 0.764 | 0.758 | 0.005 | - | - | 0.901 | 0.904 | 0.000 | 1.28x | 17.2/25.3/28.1% | 1.8/5.3% | 3 |
| transient | 1 | 0.838 | 0.835 | 0.002 | - | - | 0.938 | 0.938 | 0.000 | 1.30x | 17.6/25.7/28.3% | 2.0/5.4% | 3 |
| periodic | 1 | 0.701 | 0.697 | 0.004 | - | - | 0.804 | 0.804 | 0.000 | 1.23x | 17.0/24.8/26.8% | 1.9/4.7% | 3 |

### `RF-preset` - preset  `--scenario valleys`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.439 | 0.422 | 0.017 | - | - | 0.679 | 0.711 | 0.000 | 0.16x | 1.3/2.4/2.8% | 0.2/0.7% | 3 |
| LONG_FAST | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| LONG_MODERATE | 1 | 0.823 | 0.813 | 0.010 | - | - | 0.894 | 0.901 | 0.543 | 3.46x | 47.6/63.2/67.5% | 4.7/12.4% | 3 |

> preset=SHORT_FAST: decode_failures 6

> preset=LONG_MODERATE: misdecodes 1

> preset=LONG_MODERATE: decode_failures 10

### `RF-preset-turbo` - preset  `--scenario valleys`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.092 | 0.089 | 0.003 | - | - | 0.228 | 0.231 | 0.000 | 0.01x | 0.1/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.255 | 0.240 | 0.015 | - | - | 0.512 | 0.530 | 0.000 | 0.06x | 0.4/0.8/1.0% | 0.1/0.3% | 3 |
| LONG_FAST | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| LONG_TURBO | 1 | 0.777 | 0.773 | 0.004 | - | - | 0.894 | 0.896 | 0.000 | 1.25x | 14.2/19.6/24.5% | 1.8/4.8% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.819 | 0.816 | 0.003 | - | - | 0.912 | 0.912 | 0.000 | 1.78x | 23.2/31.7/36.7% | 2.6/7.2% | 3 |

> preset=SHORT_TURBO: decode_failures 10

### `RF-pulse` - noise-pulse-interval-ms  `--scenario valleys`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.786 | 0.782 | 0.004 | - | - | 0.887 | 0.887 | 0.000 | 1.28x | 17.5/25.4/28.1% | 2.0/5.1% | 3 |
| 10000 | 1 | 0.701 | 0.697 | 0.004 | - | - | 0.804 | 0.804 | 0.000 | 1.23x | 17.0/24.8/26.8% | 1.9/4.7% | 3 |
| 4000 | 1 | 0.467 | 0.461 | 0.005 | - | - | 0.565 | 0.576 | 0.000 | 1.07x | 15.1/22.0/23.5% | 1.6/3.7% | 3 |
| 2000 | 1 | 0.113 | 0.113 | 0.000 | - | - | 0.143 | 0.219 | 0.000 | 0.73x | 10.7/15.8/17.3% | 1.1/2.2% | 3 |

### `RF-stretch-duct` - duct-per-hour  `--scenario valleys`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.451 | 0.437 | 0.014 | - | - | 0.706 | 0.710 | 0.000 | 1.25x | 12.1/16.5/18.6% | 1.8/5.0% | 3 |
| 1.0 | 1 | 0.702 | 0.691 | 0.011 | - | - | 0.857 | 0.857 | 0.292 | 1.05x | 16.3/20.9/24.4% | 1.4/4.8% | 3 |

### `RF-txpower` - tx-power  `--scenario valleys`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 22 | 1 | 0.485 | 0.465 | 0.020 | - | - | 0.737 | 0.752 | 0.000 | 1.19x | 10.9/16.3/19.7% | 1.7/4.7% | 3 |
| 17 | 1 | 0.219 | 0.212 | 0.007 | - | - | 0.388 | 0.465 | 0.000 | 1.14x | 6.7/14.1/17.9% | 1.7/4.8% | 3 |
| 14 | 1 | 0.132 | 0.129 | 0.003 | - | - | 0.261 | 0.267 | 0.000 | 0.96x | 4.9/9.7/13.4% | 1.6/3.8% | 3 |

> tx-power=22: decode_failures 5

> tx-power=17: decode_failures 17

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario valleys`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.954 | 0.952 | 0.002 | - | - | 0.998 | 0.998 | 0.709 | 1.93x | 23.0/34.3/39.1% | 1.3/5.1% | 3 |
| True | 1 | 0.951 | 0.948 | 0.003 | - | - | 0.999 | 1.000 | 0.689 | 2.35x | 27.5/39.2/44.5% | 1.6/5.8% | 3 |

> no-adopt-hop-recommendation=False: misdecodes 1

### `RT-favourites` - favourite-routers  `--scenario valleys`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.840 | 0.837 | 0.003 | - | - | 0.925 | 0.926 | 0.000 | 1.39x | 19.7/27.6/30.1% | 1.9/5.3% | 3 |
| True | 1 | 0.859 | 0.857 | 0.002 | - | - | 0.935 | 0.935 | 0.000 | 1.44x | 20.0/28.0/30.7% | 1.9/5.3% | 3 |

### `RT-hopassign` - hop-assign  `--scenario valleys`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| random | 1 | 0.872 | 0.870 | 0.002 | - | - | 0.963 | 0.964 | 0.000 | 1.31x | 17.6/26.0/28.6% | 2.0/5.4% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario valleys`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.686 | 0.654 | 0.032 | - | - | 0.893 | 0.898 | 0.000 | 0.97x | 14.1/21.9/23.4% | 1.3/5.1% | 3 |
| 7 | 1 | 0.849 | 0.847 | 0.002 | - | - | 0.913 | 0.913 | 0.000 | 1.40x | 18.5/26.6/29.1% | 2.1/5.4% | 3 |
| 15 | 1 | 0.837 | 0.835 | 0.002 | - | - | 0.896 | 0.897 | 0.000 | 1.45x | 18.8/27.0/29.5% | 2.1/5.5% | 3 |
| 32 | 1 | 0.837 | 0.835 | 0.002 | - | - | 0.896 | 0.897 | 0.000 | 1.45x | 18.8/27.0/29.5% | 2.1/5.5% | 3 |

### `RT-hopspread` - hop-limit  `--scenario valleys`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.686 | 0.654 | 0.032 | - | - | 0.893 | 0.898 | 0.000 | 0.97x | 14.1/21.9/23.4% | 1.3/5.1% | 3 |
| 5 | 1 | 0.815 | 0.812 | 0.004 | - | - | 0.913 | 0.913 | 0.000 | 1.32x | 17.9/25.6/28.0% | 2.0/5.4% | 3 |
| 7 | 1 | 0.849 | 0.847 | 0.002 | - | - | 0.913 | 0.913 | 0.000 | 1.40x | 18.5/26.6/29.1% | 2.1/5.4% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario valleys`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| KNOWN_ONLY | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.836 | 0.836 | 0.000 | - | - | 0.906 | 0.933 | 0.000 | 1.28x | 17.5/25.3/27.9% | 2.0/5.3% | 3 |

### `RT-spread` - hop-spread  `--scenario valleys`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.686 | 0.654 | 0.032 | - | - | 0.893 | 0.898 | 0.000 | 0.97x | 14.1/21.9/23.4% | 1.3/5.1% | 3 |
| True | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |

### `SC-signing` - signature-policy  `--scenario valleys`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| BALANCED | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| STRICT | 1 | 0.671 | 0.671 | 0.000 | - | - | 0.768 | 0.770 | 0.000 | 1.43x | 19.2/28.2/30.7% | 2.1/5.8% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario valleys`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| dm | 1 | 0.848 | 0.844 | 0.004 | - | - | 0.947 | 0.948 | 0.000 | 1.27x | 17.3/25.3/27.9% | 1.9/5.4% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario valleys`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.832 | 0.830 | 0.002 | - | - | 0.922 | 0.923 | 0.000 | 1.28x | 17.5/25.6/28.2% | 1.9/5.3% | 3 |
| local | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| time | 1 | 0.836 | 0.833 | 0.003 | - | - | 0.932 | 0.934 | 0.000 | 1.34x | 18.2/26.6/29.3% | 2.0/5.6% | 3 |
| window | 1 | 0.837 | 0.834 | 0.003 | - | - | 0.932 | 0.933 | 0.000 | 1.28x | 17.5/25.3/28.0% | 1.9/5.3% | 3 |

> bucket-mode=global: misdecodes 35

> bucket-mode=time: misdecodes 54

> bucket-mode=window: misdecodes 26

### `SF-bucket-time` - time-bucket-s  `--scenario valleys`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.833 | 0.829 | 0.004 | - | - | 0.936 | 0.937 | 0.000 | 1.46x | 19.6/28.6/31.6% | 2.1/6.1% | 3 |
| 1800 | 1 | 0.836 | 0.833 | 0.003 | - | - | 0.932 | 0.934 | 0.000 | 1.34x | 18.2/26.6/29.3% | 2.0/5.6% | 3 |
| 3600 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.928 | 0.930 | 0.000 | 1.30x | 17.6/25.6/28.3% | 2.0/5.4% | 3 |

> time-bucket-s=600: misdecodes 143

> time-bucket-s=1800: misdecodes 54

> time-bucket-s=3600: misdecodes 27

### `SF-cadence` - trigger  `--scenario valleys`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| interval | 1 | 0.813 | 0.808 | 0.005 | - | - | 0.918 | 0.920 | 0.000 | 1.79x | 23.9/35.1/38.5% | 2.7/8.0% | 3 |
| aimd | 1 | 0.839 | 0.839 | 0.001 | - | - | 0.918 | 0.935 | 0.000 | 1.31x | 17.8/25.8/28.5% | 2.0/5.4% | 3 |
| bucket+interval | 1 | 0.808 | 0.802 | 0.005 | - | - | 0.913 | 0.914 | 0.000 | 1.84x | 24.7/36.4/40.1% | 2.8/8.4% | 3 |

> trigger=interval: misdecodes 32

> trigger=aimd: misdecodes 5

> trigger=bucket+interval: misdecodes 39

### `SF-capacity` - capacity  `--scenario valleys`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.838 | 0.835 | 0.003 | - | - | 0.932 | 0.933 | 0.000 | 1.28x | 17.4/25.3/27.9% | 2.0/5.4% | 3 |
| 8 | 1 | 0.836 | 0.833 | 0.003 | - | - | 0.934 | 0.935 | 0.000 | 1.28x | 17.5/25.4/28.0% | 2.0/5.4% | 3 |
| 16 | 1 | 0.838 | 0.834 | 0.004 | - | - | 0.939 | 0.939 | 0.000 | 1.29x | 17.6/25.7/28.3% | 2.0/5.4% | 3 |
| 32 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 50 | 1 | 0.840 | 0.837 | 0.003 | - | - | 0.939 | 0.940 | 0.000 | 1.30x | 17.7/25.8/28.5% | 2.0/5.4% | 3 |

> capacity=4: decode_failures 35

> capacity=8: misdecodes 1

### `SF-capacity-local` - capacity  `--scenario valleys`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.838 | 0.835 | 0.003 | - | - | 0.932 | 0.933 | 0.000 | 1.28x | 17.4/25.3/27.9% | 2.0/5.4% | 3 |
| 8 | 1 | 0.836 | 0.833 | 0.003 | - | - | 0.934 | 0.935 | 0.000 | 1.28x | 17.5/25.4/28.0% | 2.0/5.4% | 3 |
| 16 | 1 | 0.838 | 0.834 | 0.004 | - | - | 0.939 | 0.939 | 0.000 | 1.29x | 17.6/25.7/28.3% | 2.0/5.4% | 3 |
| 32 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 50 | 1 | 0.840 | 0.837 | 0.003 | - | - | 0.939 | 0.940 | 0.000 | 1.30x | 17.7/25.8/28.5% | 2.0/5.4% | 3 |

> capacity=4: decode_failures 35

> capacity=8: misdecodes 1

### `SF-capacity-window` - capacity  `--scenario valleys`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.928 | 0.000 | 1.27x | 17.4/25.1/27.7% | 1.9/5.3% | 3 |
| 16 | 1 | 0.833 | 0.830 | 0.003 | - | - | 0.931 | 0.932 | 0.000 | 1.26x | 17.2/25.2/27.7% | 1.9/5.2% | 3 |
| 32 | 1 | 0.837 | 0.834 | 0.003 | - | - | 0.932 | 0.933 | 0.000 | 1.28x | 17.5/25.3/28.0% | 1.9/5.3% | 3 |

> capacity=8: misdecodes 22

> capacity=16: misdecodes 16

> capacity=32: misdecodes 26

### `SF-catchup` - catch-up-hours  `--scenario valleys`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.808 | 0.802 | 0.005 | - | - | 0.913 | 0.914 | 0.000 | 1.84x | 24.7/36.4/40.1% | 2.8/8.4% | 3 |
| 02-06 | 1 | 0.836 | 0.835 | 0.001 | - | - | 0.922 | 0.932 | 0.000 | 1.32x | 18.0/26.2/28.9% | 2.0/5.5% | 3 |
| 00-08 | 1 | 0.839 | 0.838 | 0.002 | - | - | 0.923 | 0.934 | 0.000 | 1.39x | 18.8/27.5/30.4% | 2.1/5.8% | 3 |

> catch-up-hours=: misdecodes 39

> catch-up-hours=02-06: decode_failures 16

> catch-up-hours=00-08: misdecodes 2

> catch-up-hours=00-08: decode_failures 14

### `SF-hops-flat` - hops-apart  `--scenario valleys`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.833 | 0.833 | 0.000 | - | - | 0.927 | 0.928 | 0.000 | 1.28x | 17.4/25.3/27.9% | 2.0/5.3% | 3 |
| 2 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 3 | 1 | 0.844 | 0.831 | 0.013 | - | - | 0.772 | 0.943 | 0.000 | 1.30x | 17.8/25.8/28.3% | 2.0/5.7% | 3 |
| 4 | 1 | 0.827 | 0.823 | 0.004 | - | - | 0.574 | 0.923 | 0.000 | 1.29x | 17.7/25.7/28.3% | 1.9/5.6% | 3 |

> hops-apart=3: decode_failures 33

> hops-apart=4: decode_failures 27

### `SF-hops-spread` - hops-apart  `--scenario valleys`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.833 | 0.833 | 0.000 | - | - | 0.927 | 0.928 | 0.000 | 1.28x | 17.4/25.3/27.9% | 2.0/5.3% | 3 |
| 2 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 3 | 1 | 0.844 | 0.831 | 0.013 | - | - | 0.772 | 0.943 | 0.000 | 1.30x | 17.8/25.8/28.3% | 2.0/5.7% | 3 |
| 4 | 1 | 0.827 | 0.823 | 0.004 | - | - | 0.574 | 0.923 | 0.000 | 1.29x | 17.7/25.7/28.3% | 1.9/5.6% | 3 |
| 5 | 1 | 0.852 | 0.829 | 0.023 | - | - | 0.918 | 0.949 | 0.000 | 1.29x | 17.6/25.7/28.1% | 2.0/5.9% | 3 |

> hops-apart=3: decode_failures 33

> hops-apart=4: decode_failures 27

> hops-apart=5: decode_failures 13

### `SF-jitter-global` - advert-jitter-s  `--scenario valleys`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.836 | 0.834 | 0.002 | - | - | 0.931 | 0.933 | 0.000 | 1.28x | 17.4/25.5/28.1% | 2.0/5.4% | 3 |
| 30 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 120 | 1 | 0.841 | 0.837 | 0.004 | - | - | 0.939 | 0.939 | 0.000 | 1.28x | 17.4/25.3/28.0% | 1.9/5.3% | 3 |
| 600 | 1 | 0.836 | 0.834 | 0.002 | - | - | 0.932 | 0.933 | 0.000 | 1.30x | 17.7/25.7/28.5% | 2.0/5.4% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario valleys`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.836 | 0.834 | 0.002 | - | - | 0.931 | 0.933 | 0.000 | 1.28x | 17.4/25.5/28.1% | 2.0/5.4% | 3 |
| 30 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 120 | 1 | 0.841 | 0.837 | 0.004 | - | - | 0.939 | 0.939 | 0.000 | 1.28x | 17.4/25.3/28.0% | 1.9/5.3% | 3 |
| 600 | 1 | 0.836 | 0.834 | 0.002 | - | - | 0.932 | 0.933 | 0.000 | 1.30x | 17.7/25.7/28.5% | 2.0/5.4% | 3 |

### `SF-place-flat` - place  `--scenario valleys`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.841 | 0.832 | 0.009 | - | - | 0.534 | 0.873 | 0.000 | 1.28x | 17.6/25.4/28.0% | 2.0/5.4% | 3 |
| routers | 1 | 0.843 | 0.842 | 0.001 | - | - | 0.938 | 0.938 | 0.000 | 1.28x | 17.6/25.6/28.3% | 2.0/5.4% | 3 |
| alternate-routers | 1 | 0.827 | 0.826 | 0.002 | - | - | 0.918 | 0.918 | 0.000 | 1.27x | 17.3/25.5/28.0% | 1.9/5.3% | 3 |
| beside-router | 1 | 0.838 | 0.834 | 0.004 | - | - | 0.933 | 0.935 | 0.000 | 1.29x | 17.8/25.6/28.1% | 2.0/5.4% | 3 |
| random-clients | 1 | 0.841 | 0.833 | 0.008 | - | - | 0.949 | 0.953 | 0.000 | 1.28x | 17.7/25.5/28.0% | 1.9/5.4% | 3 |
| hops-apart | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |

> place=spread: decode_failures 9

### `SF-place-spread` - place  `--scenario valleys`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.841 | 0.832 | 0.009 | - | - | 0.534 | 0.873 | 0.000 | 1.28x | 17.6/25.4/28.0% | 2.0/5.4% | 3 |
| routers | 1 | 0.843 | 0.842 | 0.001 | - | - | 0.938 | 0.938 | 0.000 | 1.28x | 17.6/25.6/28.3% | 2.0/5.4% | 3 |
| alternate-routers | 1 | 0.827 | 0.826 | 0.002 | - | - | 0.918 | 0.918 | 0.000 | 1.27x | 17.3/25.5/28.0% | 1.9/5.3% | 3 |
| beside-router | 1 | 0.838 | 0.834 | 0.004 | - | - | 0.933 | 0.935 | 0.000 | 1.29x | 17.8/25.6/28.1% | 2.0/5.4% | 3 |
| random-clients | 1 | 0.841 | 0.833 | 0.008 | - | - | 0.949 | 0.953 | 0.000 | 1.28x | 17.7/25.5/28.0% | 1.9/5.4% | 3 |
| hops-apart | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |

> place=spread: decode_failures 9

### `SF-provide-transport` - provide-transport  `--scenario valleys`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| broadcast | 1 | 0.844 | 0.829 | 0.015 | - | - | 0.929 | 0.930 | 0.000 | 1.32x | 17.9/26.1/28.8% | 2.0/5.4% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario valleys`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| heard | 1 | 0.837 | 0.834 | 0.003 | - | - | 0.933 | 0.935 | 0.000 | 1.31x | 17.8/25.9/28.6% | 2.0/5.5% | 3 |

> replay-ordering=heard: misdecodes 20

### `SF-replay-order-broadcast` - replay-ordering  `--scenario valleys`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.844 | 0.829 | 0.015 | - | - | 0.929 | 0.930 | 0.000 | 1.32x | 17.9/26.1/28.8% | 2.0/5.4% | 3 |
| heard | 1 | 0.845 | 0.829 | 0.016 | - | - | 0.929 | 0.930 | 0.000 | 1.33x | 18.1/26.1/28.9% | 2.0/5.5% | 3 |

> replay-ordering=heard: misdecodes 19

### `SF-resolve` - resolve  `--scenario valleys`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| enum | 1 | 0.843 | 0.840 | 0.004 | - | - | 0.943 | 0.944 | 0.000 | 1.26x | 17.1/25.1/27.7% | 1.9/5.3% | 3 |
| hybrid | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |

### `SF-servers-allrouters` - servers  `--scenario valleys`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.843 | 0.842 | 0.001 | - | - | 0.938 | 0.938 | 0.000 | 1.28x | 17.6/25.6/28.3% | 2.0/5.4% | 3 |
| 6 | 1 | 0.836 | 0.833 | 0.003 | - | - | 0.933 | 0.933 | 0.000 | 1.32x | 18.0/26.4/29.1% | 2.0/5.6% | 6 |

> servers=6: misdecodes 7

### `SF-servers-flat` - servers  `--scenario valleys`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.841 | 0.840 | 0.001 | - | - | 0.934 | 0.935 | 0.000 | 1.27x | 17.4/25.4/28.0% | 1.9/5.3% | 2 |
| 3 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 5 | 1 | 0.837 | 0.832 | 0.005 | - | - | 0.929 | 0.931 | 0.000 | 1.33x | 18.0/26.2/28.9% | 2.0/5.6% | 5 |
| 8 | 1 | 0.838 | 0.830 | 0.009 | - | - | 0.937 | 0.937 | 0.000 | 1.38x | 18.7/27.3/29.7% | 2.0/5.9% | 8 |

> servers=8: misdecodes 1

### `SF-servers-spread` - servers  `--scenario valleys`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.841 | 0.840 | 0.001 | - | - | 0.934 | 0.935 | 0.000 | 1.27x | 17.4/25.4/28.0% | 1.9/5.3% | 2 |
| 3 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 5 | 1 | 0.837 | 0.832 | 0.005 | - | - | 0.929 | 0.931 | 0.000 | 1.33x | 18.0/26.2/28.9% | 2.0/5.6% | 5 |
| 8 | 1 | 0.838 | 0.830 | 0.009 | - | - | 0.937 | 0.937 | 0.000 | 1.38x | 18.7/27.3/29.7% | 2.0/5.9% | 8 |

> servers=8: misdecodes 1

### `SF-signed` - signed  `--scenario valleys`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| True | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario valleys`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.832 | 0.830 | 0.002 | - | - | 0.926 | 0.928 | 0.000 | 1.22x | 16.6/24.0/26.4% | 1.9/5.0% | 3 |
| 1 | 1 | 0.836 | 0.834 | 0.002 | - | - | 0.928 | 0.929 | 0.000 | 1.22x | 16.7/24.1/26.5% | 1.9/5.0% | 3 |
| 2 | 1 | 0.839 | 0.837 | 0.001 | - | - | 0.933 | 0.933 | 0.000 | 1.22x | 16.6/23.8/26.3% | 1.9/5.0% | 3 |
| 4 | 1 | 0.839 | 0.837 | 0.001 | - | - | 0.933 | 0.933 | 0.000 | 1.22x | 16.6/23.8/26.3% | 1.9/5.0% | 3 |

### `SF-width` - short-id-bits  `--scenario valleys`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.835 | 0.832 | 0.003 | - | - | 0.931 | 0.932 | 0.000 | 1.27x | 17.4/25.4/28.0% | 1.9/5.3% | 3 |
| 24 | 1 | 0.831 | 0.828 | 0.003 | - | - | 0.929 | 0.930 | 0.000 | 1.26x | 17.2/25.0/27.6% | 2.0/5.3% | 3 |
| 32 | 1 | 0.834 | 0.832 | 0.002 | - | - | 0.927 | 0.929 | 0.000 | 1.29x | 17.6/25.7/28.3% | 1.9/5.4% | 3 |
| 64 | 1 | 0.841 | 0.839 | 0.003 | - | - | 0.937 | 0.937 | 0.000 | 1.31x | 17.7/25.8/28.5% | 2.0/5.5% | 3 |

### `SF-window-size` - window-size  `--scenario valleys`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.834 | 0.830 | 0.004 | - | - | 0.933 | 0.933 | 0.000 | 1.38x | 18.6/27.0/29.9% | 2.1/5.7% | 3 |
| 16 | 1 | 0.836 | 0.832 | 0.004 | - | - | 0.935 | 0.935 | 0.000 | 1.31x | 17.9/25.9/28.7% | 2.0/5.4% | 3 |
| 32 | 1 | 0.837 | 0.834 | 0.003 | - | - | 0.932 | 0.933 | 0.000 | 1.28x | 17.5/25.3/28.0% | 1.9/5.3% | 3 |

> window-size=8: misdecodes 103

> window-size=16: misdecodes 68

> window-size=32: misdecodes 26

### `TH-congestion` - no-congestion-scaling  `--scenario valleys`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.954 | 0.952 | 0.002 | - | - | 0.998 | 0.998 | 0.709 | 1.93x | 23.0/34.3/39.1% | 1.3/5.1% | 3 |
| True | 1 | 0.739 | 0.729 | 0.010 | - | - | 0.853 | 0.915 | 0.466 | 5.54x | 60.0/73.4/78.1% | 4.1/12.1% | 3 |

> no-congestion-scaling=False: misdecodes 1

> no-congestion-scaling=True: queue drops 15.3% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 106

### `TH-congestion-input` - congestion-input  `--scenario valleys`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.552 | 0.541 | 0.011 | - | - | 0.894 | 0.921 | 0.207 | 4.61x | 15.2/31.9/42.3% | 1.5/6.9% | 3 |
| truesize | 1 | 0.589 | 0.579 | 0.010 | - | - | 0.943 | 0.944 | 0.222 | 3.63x | 11.7/26.9/35.2% | 1.1/6.0% | 3 |

> congestion-input=hotstore: decode_failures 112

> congestion-input=truesize: decode_failures 1

> slower: 22.4 s per simulated hour against 10.8 over 52 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `TH-congestion-mode` - congestion-mode  `--scenario valleys`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.960 | 0.958 | 0.002 | - | - | 0.999 | 1.000 | 0.686 | 1.92x | 22.7/33.5/38.2% | 1.3/5.0% | 3 |
| adaptive | 1 | 0.954 | 0.952 | 0.002 | - | - | 0.998 | 0.998 | 0.709 | 1.93x | 23.0/34.3/39.1% | 1.3/5.1% | 3 |

> congestion-mode=adaptive: misdecodes 1

