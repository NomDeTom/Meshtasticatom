# Sweep blocks-2026-09-27-2797880

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** valleys
- **seed base** 2797880 · seeds 2797880
- **blocks** 87 run
- **compute** 10.6 h of simulator time across every cell
- **generated** 2026-09-27T09:15:51+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>89 warnings</summary>

- AD-amplifiers: amplifier-mix=sprinkled: decode_failures 2
- AD-badrouters: role-placement=inverse: decode_failures 17
- AD-siting: siting-mix=local-typical: decode_failures 21
- BL-control: protocol=sr: decode_failures 22
- BL-control: slower: 4.31 s per simulated hour against 1.81 over 37 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 93
- DB-hotstore-stress: max-num-nodes=120: decode_failures 8
- DB-hotstore-stress: max-num-nodes=250: decode_failures 9
- DB-warm: warm-num-nodes=0: queue drops 16.7% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 42
- DB-warm: warm-num-nodes=25: queue drops 16.7% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 42
- DB-warm: warm-num-nodes=100: queue drops 16.7% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 42
- DB-warm: warm-num-nodes=2000: queue drops 16.7% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 42
- DG-burst: burst-loss=0.2: decode_failures 2
- DG-burst: burst-loss=0.3: decode_failures 30
- DG-loss: extra-loss=0.3: decode_failures 22
- DG-outage: burst-loss=0.1: decode_failures 14
- DG-outage: burst-loss=0.2: decode_failures 29
- DG-outage: burst-loss=0.3: decode_failures 28
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 30
- FW-mixed: legacy-fraction=0.5: decode_failures 2
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 6
- LD-chatty: broadcast-interval-s=300: decode_failures 24
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 16.7% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 42
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 26.8% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 73
- MS-density: nodes=40: decode_failures 18
- MS-hopscale: nodes=250: decode_failures 9
- MS-hopscale: nodes=500: decode_failures 97
- MS-oversubscribed: nodes=250: decode_failures 8
- MS-oversubscribed: nodes=500: decode_failures 78
- MS-siting: siting-mix=local-typical: decode_failures 29
- MS-stretch: stretch=1.25: decode_failures 32
- MS-stretch: stretch=2.0: decode_failures 11
- PR-crladder: coding-rate-ladder=False: decode_failures 30
- PR-crladder: slower: 7.12 s per simulated hour against 2.79 over 37 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 3
- RF-bw500: preset=SHORT_TURBO: decode_failures 17
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 10
- RF-bw500: slower: 4.11 s per simulated hour against 1.82 over 37 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-preset: preset=LONG_MODERATE: decode_failures 13
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 17
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 8
- RF-txpower: tx-power=22: decode_failures 14
- RF-txpower: tx-power=17: decode_failures 11
- RF-txpower: tx-power=14: decode_failures 3
- SF-bucket-mode: bucket-mode=global: misdecodes 40
- SF-bucket-mode: bucket-mode=time: misdecodes 13
- SF-bucket-mode: bucket-mode=window: misdecodes 25
- SF-bucket-time: time-bucket-s=600: misdecodes 116
- SF-bucket-time: time-bucket-s=1800: misdecodes 13
- SF-bucket-time: time-bucket-s=3600: misdecodes 5
- SF-cadence: trigger=interval: misdecodes 12
- SF-cadence: trigger=interval: decode_failures 3
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=aimd: decode_failures 3
- SF-cadence: trigger=bucket+interval: misdecodes 12
- SF-capacity-local: capacity=4: decode_failures 95
- SF-capacity-local: capacity=8: decode_failures 32
- SF-capacity: capacity=4: decode_failures 95
- SF-capacity: capacity=8: decode_failures 32
- SF-capacity-window: capacity=8: misdecodes 19
- SF-capacity-window: capacity=8: decode_failures 27
- SF-capacity-window: capacity=16: misdecodes 14
- SF-capacity-window: capacity=32: misdecodes 25
- SF-catchup: catch-up-hours=: misdecodes 12
- SF-catchup: catch-up-hours=02-06: misdecodes 2
- SF-catchup: catch-up-hours=02-06: decode_failures 41
- SF-catchup: catch-up-hours=00-08: misdecodes 1
- SF-catchup: catch-up-hours=00-08: decode_failures 42
- SF-hops-flat: hops-apart=3: decode_failures 22
- SF-hops-flat: hops-apart=4: decode_failures 29
- SF-hops-spread: hops-apart=3: decode_failures 22
- SF-hops-spread: hops-apart=4: decode_failures 29
- SF-hops-spread: hops-apart=5: decode_failures 1
- SF-place-flat: place=spread: decode_failures 23
- SF-place-spread: place=spread: decode_failures 23
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 7
- SF-replay-order: replay-ordering=heard: misdecodes 19
- SF-window-size: window-size=8: misdecodes 103
- SF-window-size: window-size=16: misdecodes 71
- SF-window-size: window-size=32: misdecodes 25
- TH-congestion-input: congestion-input=hotstore: decode_failures 8
- TH-congestion: no-congestion-scaling=True: queue drops 14.0% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 61

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `PR-crladder` | 7.12 | 2.79 | 2.55x | 37 |
| `BL-control` | 4.31 | 1.81 | 2.38x | 37 |
| `RF-bw500` | 4.11 | 1.82 | 2.25x | 37 |
| `AD-siting` | 3.01 | 1.53 | 1.96x | 37 |
| `MS-stretch` | 3.89 | 2 | 1.95x | 37 |
| `RF-txpower` | 3.13 | 1.61 | 1.95x | 37 |
| `MS-siting` | 3.49 | 1.89 | 1.84x | 36 |
| `DM-mode` | 5.49 | 3.27 | 1.68x | 37 |
| `AD-badrouters` | 3.39 | 2.1 | 1.62x | 37 |
| `SF-hops-flat` | 5.71 | 3.8 | 1.50x | 37 |
| `LD-chatty-hops` | 2.89 | 4.36 | 0.66x | 37 |
| `AD-amplifiers` | 1.1 | 1.68 | 0.65x | 37 |
| `SF-place-spread` | 1.78 | 2.84 | 0.62x | 37 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.966 | 0.966 | 0.838 → 0.852 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.930 | 0.930 | 0.849 → 0.852 | 1x bytes_on_air | up | 2 |
| `RF-preset-turbo` | preset | **held** | 0.114 → 0.966 | 0.852 | 0.064 → 0.842 | 48x sr_bytes | up | 5 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.106 → 0.917 | 0.811 | 0.095 → 0.792 | 1.5e+02x sr_airtime | down | 4 |
| `RF-txpower` | tx-power | **held** | 0.185 → 0.966 | 0.780 | 0.088 → 0.842 | 16x sr_bytes | down | 4 |
| `AD-siting` | siting-mix | **held** | 0.194 → 0.969 | 0.775 | 0.068 → 0.837 | 6x sr_bytes | down | 3 |
| `MS-siting` | siting-mix | **text** | 0.199 → 0.963 | 0.763 | 0.196 → 0.962 | 4x sr_airtime | up | 4 |
| `MS-stretch` | stretch | **text** | 0.126 → 0.847 | 0.721 | 0.119 → 0.842 | 3x sr_bytes | down | 4 |
| `RF-bw500` | preset | **text** | 0.193 → 0.762 | 0.570 | 0.185 → 0.751 | 1.9x advert_bytes | up | 3 |
| `MS-hopscale` | nodes | **text** | 0.332 → 0.847 | 0.515 | 0.328 → 0.842 | 9.8x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **text** | 0.336 → 0.823 | 0.487 | 0.332 → 0.818 | 6.7x sr_bytes | down | 3 |
| `RF-eu-presets` | preset | **text** | 0.398 → 0.847 | 0.450 | 0.393 → 0.842 | 2.3x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.398 → 0.847 | 0.450 | 0.393 → 0.842 | 3x sr_airtime | up | 3 |
| `MS-topology` | topology | **text** | 0.629 → 0.969 | 0.340 | 0.609 → 0.968 | 1.9x sr_bytes | up | 4 |
| `DG-outage` | burst-loss | **text** | 0.512 → 0.847 | 0.335 | 0.491 → 0.842 | 1.9x sr_bytes | down | 4 |
| `SF-place-flat` | place | **held** | 0.645 → 0.978 | 0.333 | 0.842 → 0.858 | 2.2x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.645 → 0.978 | 0.333 | 0.842 → 0.858 | 2.2x sr_bytes | up | 6 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.575 → 0.907 | 0.333 | 0.562 → 0.906 | 7.7x sr_airtime | down | 3 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.561 → 0.882 | 0.320 | 0.545 → 0.879 | 6.4x sr_airtime | down | 3 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.540 → 0.839 | 0.298 | 0.329 → 0.547 | 6x sr_airtime | up | 3 |
| `DG-burst` | burst-loss | **text** | 0.552 → 0.847 | 0.295 | 0.521 → 0.842 | 2.1x sr_bytes | down | 4 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.357 → 0.629 | 0.272 | 0.351 → 0.618 | 1.8x sr_airtime | up | 2 |
| `MS-density` | nodes | **text** | 0.715 → 0.966 | 0.251 | 0.700 → 0.965 | 4.9x advert_bytes | up | 5 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.745 → 0.958 | 0.213 | 0.738 → 0.958 | 5.7x sr_airtime | down | 2 |
| `RT-hoplimit` | hop-limit | **text** | 0.701 → 0.909 | 0.208 | 0.681 → 0.907 | 1.8x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.701 → 0.897 | 0.196 | 0.681 → 0.895 | 1.8x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **text** | 0.685 → 0.847 | 0.162 | 0.679 → 0.842 | 1.3x sr_bytes | down | 4 |
| `AD-badrouters` | role-placement | **text** | 0.688 → 0.844 | 0.156 | 0.656 → 0.837 | 1.7x sr_bytes | down | 3 |
| `RT-spread` | hop-spread | **text** | 0.701 → 0.847 | 0.146 | 0.681 → 0.842 | 1.5x sr_bytes | up | 2 |
| `MS-size` | nodes | **text** | 0.719 → 0.847 | 0.128 | 0.705 → 0.842 | 4x sr_bytes | down | 5 |
| `DG-loss` | extra-loss | **text** | 0.725 → 0.847 | 0.122 | 0.710 → 0.842 | 1.6x sr_bytes | down | 4 |
| `DB-platform` | platform-mix | **text** | 0.779 → 0.894 | 0.115 | 0.772 → 0.892 | 2.1x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.790 → 0.894 | 0.105 | 0.782 → 0.892 | 2.2x sr_airtime | up | 4 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.847 → 0.946 | 0.098 | 0.842 → 0.945 | 2.4x sr_bytes | up | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.815 → 0.906 | 0.091 | 0.807 → 0.904 | 5.6x sr_airtime | up | 4 |
| `SC-signing` | signature-policy | **text** | 0.756 → 0.847 | 0.091 | 0.756 → 0.842 | 1.2x sr_airtime | down | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.718 → 0.802 | 0.085 | 0.625 → 0.706 | 1.4x sr_airtime | down | 2 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.847 → 0.931 | 0.083 | 0.842 → 0.913 | 1.4x sr_airtime | up | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.847 → 0.919 | 0.071 | 0.842 → 0.913 | 1.2x sr_bytes | up | 3 |
| `FW-versions` | profile | **text** | 0.847 → 0.917 | 0.069 | 0.842 → 0.912 | 3.1x bytes_on_air | down | 5 |
| `FW-firmware` | profile | **text** | 0.847 → 0.912 | 0.065 | 0.842 → 0.907 | 3x bytes_on_air | down | 2 |
| `SF-cadence` | trigger | **held** | 0.910 → 0.969 | 0.059 | 0.805 → 0.849 | 13x advert_bytes | down | 4 |
| `FW-mixed` | legacy-fraction | **text** | 0.847 → 0.896 | 0.048 | 0.842 → 0.890 | 2.1x bytes_on_air | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.917 → 0.966 | 0.048 | 0.842 → 0.863 | 20x sr_airtime | down | 3 |
| `FW-signing-cost` | profile-flag | **text** | 0.847 → 0.894 | 0.047 | 0.842 → 0.892 | 3.3x bytes_on_air | down | 2 |
| `AD-nomute` | role-mix | **text** | 0.835 → 0.881 | 0.046 | 0.826 → 0.879 | 2.6x bytes_on_air | up | 3 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.847 → 0.894 | 0.046 | 0.842 → 0.889 | 2.2x bytes_on_air | up | 4 |
| `SF-catchup` | catch-up-hours | **text** | 0.815 → 0.855 | 0.040 | 0.805 → 0.851 | 9.2x advert_bytes | up | 3 |
| `SF-hops-spread` | hops-apart | **text** | 0.847 → 0.887 | 0.039 | 0.840 → 0.852 | 1.9x sr_bytes | up | 5 |
| `TH-congestion-input` | congestion-input | **text** | 0.549 → 0.589 | 0.039 | 0.538 → 0.578 | 1.4x sr_airtime | up | 2 |
| `AD-flooding` | role-mix | **text** | 0.844 → 0.881 | 0.037 | 0.837 → 0.879 | 2.6x bytes_on_air | up | 2 |
| `SF-hops-flat` | hops-apart | **held** | 0.930 → 0.966 | 0.036 | 0.840 → 0.849 | 1.9x sr_bytes | down | 4 |
| `LD-diurnal` | diurnal | **text** | 0.847 → 0.880 | 0.032 | 0.842 → 0.877 | 1.4x sr_bytes | down | 3 |
| `SF-provide-transport` | provide-transport | **text** | 0.847 → 0.876 | 0.029 | 0.842 → 0.843 | 3x sr_airtime | up | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.821 → 0.849 | 0.028 | 0.812 → 0.844 | 1.5x sr_airtime | down | 4 |
| `MS-router-late` | router-late-fraction | **text** | 0.847 → 0.871 | 0.023 | 0.842 → 0.868 | 1.3x bytes_on_air | up | 4 |
| `MS-roles` | role-mix | **text** | 0.844 → 0.863 | 0.019 | 0.837 → 0.857 | 1.1x sr_bytes | down | 2 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.847 → 0.866 | 0.018 | 0.842 → 0.862 | 1.1x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.847 → 0.866 | 0.018 | 0.842 → 0.862 | 1.1x sr_airtime | up | 4 |
| `SF-capacity` | capacity | **text** | 0.847 → 0.865 | 0.017 | 0.842 → 0.860 | 5.3x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **text** | 0.847 → 0.865 | 0.017 | 0.842 → 0.860 | 5.3x advert_bytes | down | 5 |
| `SF-servers-flat` | servers | **text** | 0.847 → 0.863 | 0.016 | 0.842 → 0.854 | 5.2x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **text** | 0.847 → 0.863 | 0.016 | 0.842 → 0.854 | 5.2x sr_bytes | up | 4 |
| `SF-capacity-window` | capacity | **held** | 0.958 → 0.973 | 0.016 | 0.846 → 0.849 | 1.9x advert_bytes | up | 3 |
| `SF-sr-retries` | sr-retries | **text** | 0.846 → 0.860 | 0.015 | 0.841 → 0.854 | 1.1x sr_bytes | = | 4 |
| `DM-mode` | dm-mode | **text** | 0.816 → 0.831 | 0.014 | 0.816 → 0.831 | 1.3x sr_airtime | up | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.859 → 0.872 | 0.013 | 0.854 → 0.868 | 1x bytes_on_air | up | 2 |
| `SF-width` | short-id-bits | **held** | 0.966 → 0.979 | 0.013 | 0.842 → 0.854 | 3.1x advert_bytes | down | 4 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.946 → 0.959 | 0.013 | 0.822 → 0.833 | 1.1x sr_airtime | down | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.847 → 0.860 | 0.012 | 0.842 → 0.854 | 1.1x sr_bytes | up | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.948 → 0.959 | 0.011 | 0.831 → 0.833 | 1.1x sr_airtime | up | 2 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.968 → 0.979 | 0.011 | 0.847 → 0.854 | 5.3x advert_bytes | down | 3 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.847 → 0.858 | 0.011 | 0.842 → 0.854 | 3.1x advert_bytes | down | 4 |
| `SF-advert-transport` | advert-transport | **text** | 0.847 → 0.857 | 0.009 | 0.842 → 0.851 | 2.9x sr_airtime | up | 2 |
| `SF-window-size` | window-size | **text** | 0.848 → 0.857 | 0.009 | 0.842 → 0.851 | 4.8x advert_bytes | up | 3 |
| `PR-repeats` | extra-repeats | **text** | 0.847 → 0.856 | 0.008 | 0.842 → 0.851 | 1x sr_bytes | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.951 → 0.958 | 0.007 | 0.950 → 0.958 | 1.2x sr_airtime | down | 2 |
| `RT-hopassign` | hop-assign | **text** | 0.847 → 0.854 | 0.007 | 0.842 → 0.847 | 1.1x sr_airtime | up | 2 |
| `SF-resolve` | resolve | **text** | 0.847 → 0.854 | 0.006 | 0.842 → 0.847 | 5.7x advert_bytes | = | 3 |
| `AD-worst` | role-placement | **text** | 0.843 → 0.849 | 0.006 | 0.833 → 0.843 | 1.1x sr_bytes | down | 2 |
| `MS-roles-fav` | role-mix | **held** | 0.959 → 0.964 | 0.005 | 0.865 → 0.870 | 1.1x sr_bytes | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.971 → 0.974 | 0.004 | 0.843 → 0.844 | 1x sr_bytes | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.958 → 0.962 | 0.003 | 0.958 → 0.961 | 1.1x sr_airtime | down | 2 |
| `SF-servers-allrouters` | servers | **text** | 0.852 → 0.855 | 0.003 | 0.850 → 0.851 | 2.3x sr_bytes | up | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.994 → 0.995 | 0.001 | 0.958 → 0.958 | 1x sr_bytes | up | 2 |

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
| none | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| sprinkled | 1 | 0.866 | 0.854 | 0.012 | - | - | 0.962 | 0.967 | 0.566 | 1.30x | 16.7/25.0/28.0% | 1.9/5.5% | 3 |
| arms-race | 1 | 0.946 | 0.945 | 0.001 | - | - | 0.986 | 0.986 | 0.717 | 1.13x | 21.7/29.5/33.1% | 1.4/5.5% | 3 |

> amplifier-mix=sprinkled: decode_failures 2

### `AD-amplify-worst` - amplify-worst  `--scenario valleys`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 0.1 | 1 | 0.876 | 0.867 | 0.008 | - | - | 0.958 | 0.962 | 0.221 | 1.23x | 17.1/23.7/30.8% | 1.8/5.3% | 3 |
| 0.3 | 1 | 0.931 | 0.913 | 0.018 | - | - | 0.994 | 0.995 | 0.742 | 1.13x | 18.8/23.8/33.0% | 1.6/5.0% | 3 |

### `AD-badrouters` - role-placement  `--scenario valleys`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.844 | 0.837 | 0.007 | - | - | 0.969 | 0.972 | 0.000 | 1.11x | 15.5/23.2/26.2% | 1.9/5.1% | 3 |
| inverse | 1 | 0.688 | 0.656 | 0.032 | - | - | 0.887 | 0.925 | 0.163 | 1.08x | 12.6/18.2/21.0% | 2.0/4.0% | 3 |
| random | 1 | 0.789 | 0.777 | 0.013 | - | - | 0.954 | 0.955 | 0.192 | 1.12x | 14.2/19.0/20.4% | 2.0/4.6% | 3 |

> role-placement=inverse: decode_failures 17

### `AD-flooding` - role-mix  `--scenario valleys`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.844 | 0.837 | 0.007 | - | - | 0.969 | 0.972 | 0.000 | 1.11x | 15.5/23.2/26.2% | 1.9/5.1% | 3 |
| all-routers | 1 | 0.881 | 0.879 | 0.003 | - | - | 0.959 | 0.959 | 0.339 | 2.88x | 33.7/41.7/45.2% | 4.7/5.6% | 3 |

### `AD-nomute` - role-mix  `--scenario valleys`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.844 | 0.837 | 0.007 | - | - | 0.969 | 0.972 | 0.000 | 1.11x | 15.5/23.2/26.2% | 1.9/5.1% | 3 |
| no-mute | 1 | 0.835 | 0.826 | 0.009 | - | - | 0.965 | 0.967 | 0.189 | 1.27x | 16.0/22.2/25.4% | 1.9/4.9% | 3 |
| all-routers | 1 | 0.881 | 0.879 | 0.003 | - | - | 0.959 | 0.959 | 0.339 | 2.88x | 33.7/41.7/45.2% | 4.7/5.6% | 3 |

### `AD-siting` - siting-mix  `--scenario valleys`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.844 | 0.837 | 0.007 | - | - | 0.969 | 0.972 | 0.000 | 1.11x | 15.5/23.2/26.2% | 1.9/5.1% | 3 |
| local-typical | 1 | 0.712 | 0.694 | 0.018 | - | - | 0.827 | 0.899 | 0.000 | 1.25x | 12.2/21.2/24.7% | 2.1/5.1% | 3 |
| basement-heavy | 1 | 0.069 | 0.068 | 0.001 | - | - | 0.194 | 0.196 | 0.000 | 0.52x | 1.1/7.4/9.6% | 0.4/2.8% | 3 |

> siting-mix=local-typical: decode_failures 21

### `AD-worst` - role-placement  `--scenario valleys`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.849 | 0.843 | 0.006 | - | - | 0.963 | 0.964 | 0.000 | 2.24x | 17.8/29.0/35.8% | 1.6/5.5% | 3 |
| inverse | 1 | 0.843 | 0.833 | 0.009 | - | - | 0.968 | 0.968 | 0.000 | 2.15x | 16.4/23.7/28.9% | 1.6/3.3% | 3 |

### `BL-control` - protocol  `--scenario valleys`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.852 | 0.852 | 0.000 | - | - | 0 | 0.000 | 0.210 | 1.28x | 16.7/22.7/27.1% | 1.8/5.2% | 3 |
| sr | 1 | 0.870 | 0.849 | 0.021 | - | - | 0.930 | 0.959 | 0.207 | 1.31x | 17.0/23.4/27.9% | 1.8/5.4% | 3 |

> protocol=sr: decode_failures 22

> slower: 4.31 s per simulated hour against 1.81 over 37 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario valleys`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.790 | 0.782 | 0.007 | - | - | 0.920 | 0.921 | 0.220 | 3.25x | 40.8/58.1/66.4% | 4.5/10.6% | 3 |
| 100 | 1 | 0.894 | 0.892 | 0.003 | - | - | 0.969 | 0.969 | 0.257 | 1.67x | 21.3/31.8/38.3% | 2.2/5.6% | 3 |
| 120 | 1 | 0.894 | 0.892 | 0.003 | - | - | 0.969 | 0.969 | 0.257 | 1.67x | 21.3/31.8/38.3% | 2.2/5.6% | 3 |
| 250 | 1 | 0.894 | 0.892 | 0.003 | - | - | 0.969 | 0.969 | 0.257 | 1.67x | 21.3/31.8/38.3% | 2.2/5.6% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario valleys`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.335 | 0.329 | 0.006 | - | - | 0.540 | 0.633 | 0.134 | 11.49x | 40.4/65.4/77.5% | 4.1/10.5% | 3 |
| 120 | 1 | 0.549 | 0.538 | 0.011 | - | - | 0.837 | 0.841 | 0.172 | 4.76x | 16.5/32.9/47.2% | 1.6/6.2% | 3 |
| 250 | 1 | 0.557 | 0.547 | 0.010 | - | - | 0.839 | 0.842 | 0.176 | 4.57x | 15.8/31.4/45.2% | 1.6/5.8% | 3 |

> max-num-nodes=10: decode_failures 93

> max-num-nodes=120: decode_failures 8

> max-num-nodes=250: decode_failures 9

### `DB-platform` - platform-mix  `--scenario valleys`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.894 | 0.892 | 0.003 | - | - | 0.969 | 0.969 | 0.257 | 1.67x | 21.3/31.8/38.3% | 2.2/5.6% | 3 |
| baymesh-2026-08 | 1 | 0.894 | 0.892 | 0.003 | - | - | 0.969 | 0.969 | 0.257 | 1.67x | 21.3/31.8/38.3% | 2.2/5.6% | 3 |
| constrained | 1 | 0.779 | 0.772 | 0.008 | - | - | 0.912 | 0.912 | 0.213 | 3.25x | 40.7/58.3/66.4% | 4.4/10.6% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario valleys`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.713 | 0.706 | 0.007 | - | - | 0.802 | 0.835 | 0.477 | 5.81x | 57.0/75.5/79.8% | 4.2/12.7% | 3 |
| 25 | 1 | 0.713 | 0.706 | 0.007 | - | - | 0.802 | 0.835 | 0.477 | 5.81x | 57.0/75.5/79.8% | 4.2/12.7% | 3 |
| 100 | 1 | 0.713 | 0.706 | 0.007 | - | - | 0.802 | 0.835 | 0.477 | 5.81x | 57.0/75.5/79.8% | 4.2/12.7% | 3 |
| 2000 | 1 | 0.713 | 0.706 | 0.007 | - | - | 0.802 | 0.835 | 0.477 | 5.81x | 57.0/75.5/79.8% | 4.2/12.7% | 3 |

> warm-num-nodes=0: queue drops 16.7% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 42

> warm-num-nodes=25: queue drops 16.7% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 42

> warm-num-nodes=100: queue drops 16.7% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 42

> warm-num-nodes=2000: queue drops 16.7% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 42

### `DG-burst` - burst-loss  `--scenario valleys`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 0.1 | 1 | 0.756 | 0.741 | 0.016 | - | - | 0.946 | 0.949 | 0.176 | 1.20x | 16.0/21.8/26.3% | 1.7/4.9% | 3 |
| 0.2 | 1 | 0.660 | 0.633 | 0.027 | - | - | 0.909 | 0.919 | 0.109 | 1.18x | 15.8/21.7/26.2% | 1.7/4.7% | 3 |
| 0.3 | 1 | 0.552 | 0.521 | 0.031 | - | - | 0.805 | 0.851 | 0.089 | 1.05x | 14.3/19.9/24.2% | 1.5/4.1% | 3 |

> burst-loss=0.2: decode_failures 2

> burst-loss=0.3: decode_failures 30

### `DG-loss` - extra-loss  `--scenario valleys`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 0.1 | 1 | 0.817 | 0.809 | 0.007 | - | - | 0.953 | 0.958 | 0.177 | 1.36x | 17.9/24.4/28.9% | 2.0/5.4% | 3 |
| 0.2 | 1 | 0.783 | 0.773 | 0.010 | - | - | 0.949 | 0.953 | 0.141 | 1.40x | 18.4/25.2/29.7% | 2.1/5.2% | 3 |
| 0.3 | 1 | 0.725 | 0.710 | 0.015 | - | - | 0.899 | 0.918 | 0.120 | 1.42x | 19.0/25.9/30.3% | 2.1/5.0% | 3 |

> extra-loss=0.3: decode_failures 22

### `DG-outage` - burst-loss  `--scenario valleys`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 0.1 | 1 | 0.751 | 0.738 | 0.013 | - | - | 0.936 | 0.964 | 0.159 | 1.21x | 16.0/22.2/26.7% | 1.7/5.3% | 3 |
| 0.2 | 1 | 0.639 | 0.620 | 0.020 | - | - | 0.869 | 0.921 | 0.096 | 1.16x | 15.6/21.4/25.7% | 1.7/4.6% | 3 |
| 0.3 | 1 | 0.512 | 0.491 | 0.021 | - | - | 0.660 | 0.809 | 0.087 | 1.07x | 14.8/20.3/24.8% | 1.6/4.3% | 3 |

> burst-loss=0.1: decode_failures 14

> burst-loss=0.2: decode_failures 29

> burst-loss=0.3: decode_failures 28

### `DM-mode` - dm-mode  `--scenario valleys`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.816 | 0.816 | 0.000 | - | - | 0.951 | 0.956 | 0.221 | 1.69x | 22.2/30.2/35.9% | 2.4/7.0% | 3 |
| directed-with-late-flood | 1 | 0.831 | 0.831 | 0.000 | - | - | 0.948 | 0.968 | 0.218 | 1.53x | 20.2/27.9/33.2% | 2.1/6.6% | 3 |
| m4-early-flood | 1 | 0.829 | 0.829 | 0.000 | - | - | 0.960 | 0.965 | 0.202 | 1.53x | 20.3/27.8/33.1% | 2.2/6.6% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 30

### `FW-firmware` - profile  `--scenario valleys`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.912 | 0.907 | 0.005 | - | - | 0.986 | 0.987 | 0.766 | 0.78x | 8.6/12.6/14.1% | 1.3/2.1% | 3 |
| 2.8 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario valleys`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 0.25 | 1 | 0.874 | 0.868 | 0.006 | - | - | 0.979 | 0.983 | 0.640 | 1.14x | 13.6/18.8/21.3% | 1.7/4.8% | 3 |
| 0.5 | 1 | 0.884 | 0.874 | 0.010 | - | - | 0.985 | 0.986 | 0.537 | 1.07x | 11.8/18.0/20.4% | 1.7/4.2% | 3 |
| 0.75 | 1 | 0.896 | 0.890 | 0.005 | - | - | 0.991 | 0.992 | 0.693 | 0.88x | 11.4/15.8/18.5% | 1.4/3.7% | 3 |

> legacy-fraction=0.5: decode_failures 2

### `FW-mixed-26` - legacy-fraction  `--scenario valleys`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 0.25 | 1 | 0.862 | 0.855 | 0.007 | - | - | 0.977 | 0.980 | 0.655 | 1.15x | 13.8/19.0/21.1% | 1.8/4.8% | 3 |
| 0.5 | 1 | 0.875 | 0.865 | 0.010 | - | - | 0.984 | 0.985 | 0.501 | 1.04x | 11.8/17.6/20.1% | 1.7/4.1% | 3 |
| 0.75 | 1 | 0.894 | 0.889 | 0.005 | - | - | 0.989 | 0.990 | 0.693 | 0.83x | 10.8/15.3/18.2% | 1.3/3.6% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario valleys`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.894 | 0.892 | 0.002 | - | - | 0.988 | 0.988 | 0.279 | 0.69x | 9.3/13.1/15.9% | 1.0/3.1% | 3 |
| signing=true | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |

### `FW-versions` - profile  `--scenario valleys`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.912 | 0.906 | 0.006 | - | - | 0.992 | 0.994 | 0.680 | 0.77x | 8.9/13.6/15.5% | 1.2/2.8% | 3 |
| 2.5 | 1 | 0.917 | 0.912 | 0.005 | - | - | 0.996 | 0.997 | 0.676 | 0.80x | 9.2/13.7/15.4% | 1.3/2.8% | 3 |
| 2.6 | 1 | 0.916 | 0.911 | 0.005 | - | - | 0.995 | 0.997 | 0.687 | 0.75x | 8.7/13.6/15.4% | 1.2/2.8% | 3 |
| 2.7 | 1 | 0.916 | 0.912 | 0.004 | - | - | 0.990 | 0.992 | 0.682 | 0.77x | 9.6/13.8/16.9% | 1.2/3.1% | 3 |
| 2.8 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.882 | 0.879 | 0.003 | - | - | 0.982 | 0.982 | 0.230 | 0.87x | 11.4/15.5/18.5% | 1.2/3.6% | 3 |
| 900 | 1 | 0.815 | 0.807 | 0.008 | - | - | 0.951 | 0.954 | 0.215 | 2.06x | 26.7/36.9/43.4% | 2.9/8.5% | 3 |
| 300 | 1 | 0.561 | 0.545 | 0.016 | - | - | 0.749 | 0.800 | 0.148 | 4.37x | 51.4/69.5/75.6% | 6.2/16.9% | 3 |

> broadcast-interval-s=300: decode_failures 24

### `LD-chatty-hops` - broadcast-interval-s  `--scenario valleys`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.907 | 0.906 | 0.002 | - | - | 0.967 | 0.969 | 0.274 | 0.95x | 11.9/16.0/19.0% | 1.4/3.5% | 3 |
| 900 | 1 | 0.846 | 0.840 | 0.006 | - | - | 0.930 | 0.932 | 0.216 | 2.29x | 29.0/38.3/45.5% | 3.4/8.7% | 3 |
| 300 | 1 | 0.575 | 0.562 | 0.013 | - | - | 0.691 | 0.730 | 0.141 | 4.82x | 55.6/71.9/77.1% | 7.1/17.9% | 3 |

> broadcast-interval-s=300: decode_failures 6

### `LD-diurnal` - diurnal  `--scenario valleys`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.880 | 0.877 | 0.003 | - | - | 0.981 | 0.982 | 0.255 | 1.18x | 15.6/21.4/25.8% | 1.7/5.0% | 3 |
| sinusoid | 1 | 0.868 | 0.864 | 0.004 | - | - | 0.973 | 0.974 | 0.231 | 1.16x | 15.1/20.6/24.8% | 1.7/4.8% | 3 |
| commuter | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.815 | 0.807 | 0.008 | - | - | 0.951 | 0.954 | 0.215 | 2.06x | 26.7/36.9/43.4% | 2.9/8.5% | 3 |
| 3600 | 1 | 0.882 | 0.879 | 0.003 | - | - | 0.982 | 0.982 | 0.230 | 0.87x | 11.4/15.5/18.5% | 1.2/3.6% | 3 |
| 10800 | 1 | 0.895 | 0.892 | 0.002 | - | - | 0.986 | 0.987 | 0.231 | 0.57x | 7.5/10.2/12.3% | 0.8/2.4% | 3 |
| 43200 | 1 | 0.906 | 0.904 | 0.002 | - | - | 0.996 | 0.997 | 0.237 | 0.41x | 5.2/7.1/8.6% | 0.6/1.7% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario valleys`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 0.25 | 1 | 0.849 | 0.844 | 0.005 | - | - | 0.972 | 0.973 | 0.209 | 1.36x | 17.9/24.4/29.2% | 1.9/5.7% | 3 |
| 1.0 | 1 | 0.837 | 0.831 | 0.006 | - | - | 0.964 | 0.964 | 0.182 | 1.48x | 19.6/26.9/31.9% | 2.1/6.3% | 3 |
| 4.0 | 1 | 0.821 | 0.812 | 0.009 | - | - | 0.969 | 0.970 | 0.210 | 1.85x | 24.2/34.3/40.2% | 2.6/8.0% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario valleys`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.713 | 0.706 | 0.007 | - | - | 0.802 | 0.835 | 0.477 | 5.81x | 57.0/75.5/79.8% | 4.2/12.7% | 3 |
| 1.0 | 1 | 0.632 | 0.625 | 0.007 | - | - | 0.718 | 0.762 | 0.410 | 6.38x | 60.9/76.5/81.0% | 4.6/13.8% | 3 |

> traceroute-per-hour=0.0: queue drops 16.7% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 42

> traceroute-per-hour=1.0: queue drops 26.8% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 73

### `MS-density` - nodes  `--scenario valleys`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.715 | 0.700 | 0.015 | - | - | 0.783 | 0.903 | 0.348 | 1.35x | 18.8/25.9/33.3% | 3.2/7.0% | 3 |
| 60 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 90 | 1 | 0.936 | 0.932 | 0.004 | - | - | 0.994 | 0.995 | 0.760 | 1.64x | 18.4/28.0/31.5% | 1.5/5.0% | 3 |
| 120 | 1 | 0.958 | 0.958 | 0.001 | - | - | 0.994 | 0.994 | 0.757 | 2.10x | 22.9/39.0/45.0% | 1.4/5.1% | 3 |
| 150 | 1 | 0.966 | 0.965 | 0.001 | - | - | 1.000 | 1.000 | 0.828 | 2.64x | 28.2/47.0/54.1% | 1.3/5.5% | 3 |

> nodes=40: decode_failures 18

### `MS-hopscale` - nodes  `--scenario valleys`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 120 | 1 | 0.828 | 0.821 | 0.006 | - | - | 0.981 | 0.981 | 0.400 | 2.21x | 16.1/26.1/31.1% | 1.5/5.5% | 3 |
| 250 | 1 | 0.547 | 0.536 | 0.011 | - | - | 0.826 | 0.828 | 0.162 | 5.06x | 17.5/35.2/50.6% | 1.7/6.6% | 3 |
| 500 | 1 | 0.332 | 0.328 | 0.004 | - | - | 0.514 | 0.541 | 0.090 | 10.40x | 19.0/34.7/54.7% | 1.7/7.0% | 3 |

> nodes=250: decode_failures 9

> nodes=500: decode_failures 97

### `MS-oversubscribed` - nodes  `--scenario valleys`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.823 | 0.818 | 0.005 | - | - | 0.970 | 0.972 | 0.389 | 2.02x | 14.7/23.8/28.3% | 1.4/5.0% | 3 |
| 250 | 1 | 0.549 | 0.538 | 0.011 | - | - | 0.837 | 0.841 | 0.172 | 4.76x | 16.5/32.9/47.2% | 1.6/6.2% | 3 |
| 500 | 1 | 0.336 | 0.332 | 0.004 | - | - | 0.517 | 0.547 | 0.088 | 9.80x | 18.2/32.5/51.3% | 1.6/6.5% | 3 |

> nodes=250: decode_failures 8

> nodes=500: decode_failures 78

### `MS-roles` - role-mix  `--scenario valleys`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.863 | 0.857 | 0.006 | - | - | 0.980 | 0.980 | 0.200 | 1.26x | 16.7/22.8/27.1% | 1.8/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.844 | 0.837 | 0.007 | - | - | 0.969 | 0.972 | 0.000 | 1.11x | 15.5/23.2/26.2% | 1.9/5.1% | 3 |

### `MS-roles-fav` - role-mix  `--scenario valleys`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.874 | 0.870 | 0.004 | - | - | 0.964 | 0.967 | 0.243 | 1.35x | 17.4/23.4/27.9% | 1.9/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.869 | 0.865 | 0.004 | - | - | 0.959 | 0.961 | 0.000 | 1.28x | 18.1/25.9/30.8% | 2.3/5.1% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario valleys`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 0.05 | 1 | 0.851 | 0.847 | 0.005 | - | - | 0.970 | 0.970 | 0.218 | 1.45x | 18.4/27.2/34.8% | 2.0/5.6% | 3 |
| 0.1 | 1 | 0.858 | 0.855 | 0.003 | - | - | 0.966 | 0.966 | 0.223 | 1.59x | 21.0/31.7/39.3% | 2.1/5.6% | 3 |
| 0.2 | 1 | 0.871 | 0.868 | 0.003 | - | - | 0.975 | 0.976 | 0.190 | 1.73x | 23.8/33.7/40.4% | 2.4/5.5% | 3 |

### `MS-siting` - siting-mix  `--scenario valleys`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| local-typical | 1 | 0.705 | 0.692 | 0.013 | - | - | 0.870 | 0.896 | 0.000 | 1.53x | 13.8/22.9/29.7% | 2.6/5.2% | 3 |
| event | 1 | 0.199 | 0.196 | 0.003 | - | - | 0.365 | 0.368 | 0.000 | 1.43x | 7.1/19.8/24.3% | 2.0/5.3% | 3 |
| backbone | 1 | 0.963 | 0.962 | 0.001 | - | - | 0.986 | 0.987 | 0.797 | 1.07x | 23.0/32.6/36.3% | 1.2/5.6% | 3 |

> siting-mix=local-typical: decode_failures 29

### `MS-size` - nodes  `--scenario valleys`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.844 | 0.830 | 0.014 | - | - | 0.956 | 0.960 | 0.616 | 1.48x | 23.6/34.6/37.1% | 3.6/7.8% | 3 |
| 60 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 90 | 1 | 0.796 | 0.783 | 0.013 | - | - | 0.959 | 0.962 | 0.430 | 1.74x | 13.6/25.8/33.0% | 1.6/5.1% | 3 |
| 120 | 1 | 0.828 | 0.821 | 0.006 | - | - | 0.981 | 0.981 | 0.400 | 2.21x | 16.1/26.1/31.1% | 1.5/5.5% | 3 |
| 150 | 1 | 0.719 | 0.705 | 0.014 | - | - | 0.868 | 0.869 | 0.268 | 2.85x | 16.8/28.9/34.4% | 1.5/5.5% | 3 |

### `MS-stretch` - stretch  `--scenario valleys`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 1.25 | 1 | 0.650 | 0.620 | 0.031 | - | - | 0.785 | 0.886 | 0.286 | 1.42x | 13.2/19.8/24.1% | 2.2/5.7% | 3 |
| 1.5 | 1 | 0.357 | 0.351 | 0.006 | - | - | 0.544 | 0.550 | 0.000 | 1.32x | 11.0/16.5/21.0% | 2.2/4.9% | 3 |
| 2.0 | 1 | 0.126 | 0.119 | 0.007 | - | - | 0.381 | 0.450 | 0.000 | 0.78x | 3.4/9.4/12.6% | 1.0/3.5% | 3 |

> stretch=1.25: decode_failures 32

> stretch=2.0: decode_failures 11

### `MS-topology` - topology  `--scenario valleys`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| clustered | 1 | 0.966 | 0.964 | 0.002 | - | - | 0.993 | 0.993 | 0.721 | 1.15x | 25.1/36.3/38.0% | 1.5/5.5% | 3 |
| corridor | 1 | 0.629 | 0.609 | 0.020 | - | - | 0.858 | 0.860 | 0.270 | 1.41x | 17.4/21.4/24.1% | 2.4/5.0% | 3 |
| hub | 1 | 0.969 | 0.968 | 0.000 | - | - | 0.992 | 0.992 | 0.749 | 1.13x | 25.3/35.1/37.2% | 1.5/5.6% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario valleys`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.831 | 0.831 | 0.000 | - | - | 0.948 | 0.968 | 0.218 | 1.53x | 20.2/27.9/33.2% | 2.1/6.6% | 3 |
| True | 1 | 0.833 | 0.833 | 0.000 | - | - | 0.959 | 0.965 | 0.205 | 1.52x | 20.3/27.7/33.0% | 2.2/6.6% | 3 |

> coding-rate-ladder=False: decode_failures 30

> slower: 7.12 s per simulated hour against 2.79 over 37 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-dmmode-cr` - dm-mode  `--scenario valleys`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.833 | 0.833 | 0.000 | - | - | 0.959 | 0.965 | 0.205 | 1.52x | 20.3/27.7/33.0% | 2.2/6.6% | 3 |
| m4-early-flood | 1 | 0.822 | 0.822 | 0.000 | - | - | 0.946 | 0.957 | 0.213 | 1.53x | 20.3/27.7/33.1% | 2.1/6.6% | 3 |

> dm-mode=m4-early-flood: decode_failures 3

### `PR-protocol` - protocol  `--scenario valleys`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.852 | 0.852 | 0.000 | - | - | 0 | 0.000 | 0.210 | 1.28x | 16.7/22.7/27.1% | 1.8/5.2% | 3 |
| chain | 1 | 0.841 | 0.838 | 0.003 | - | - | 0.915 | 0.970 | 0.222 | 1.49x | 19.7/26.8/31.9% | 2.1/6.3% | 3 |
| sr | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |

### `PR-repeats` - extra-repeats  `--scenario valleys`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| True | 1 | 0.856 | 0.851 | 0.004 | - | - | 0.972 | 0.973 | 0.231 | 1.32x | 17.2/23.6/28.0% | 1.8/5.5% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario valleys`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.958 | 0.958 | 0.001 | - | - | 0.994 | 0.994 | 0.757 | 2.10x | 22.9/39.0/45.0% | 1.4/5.1% | 3 |
| True | 1 | 0.959 | 0.958 | 0.001 | - | - | 0.995 | 0.995 | 0.759 | 2.12x | 22.9/39.1/45.1% | 1.4/5.1% | 3 |

### `RF-bw500` - preset  `--scenario valleys`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.193 | 0.185 | 0.008 | - | - | 0.502 | 0.549 | 0.000 | 0.05x | 0.3/0.7/1.2% | 0.1/0.3% | 3 |
| MEDIUM_TURBO | 1 | 0.461 | 0.450 | 0.010 | - | - | 0.683 | 0.711 | 0.000 | 0.27x | 2.2/3.9/4.2% | 0.4/1.2% | 3 |
| LONG_TURBO | 1 | 0.762 | 0.751 | 0.011 | - | - | 0.945 | 0.947 | 0.000 | 1.26x | 13.2/19.9/23.4% | 1.9/5.2% | 3 |

> preset=SHORT_TURBO: decode_failures 17

> preset=MEDIUM_TURBO: decode_failures 10

> slower: 4.11 s per simulated hour against 1.82 over 37 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-duct` - duct-per-hour  `--scenario valleys`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 0.25 | 1 | 0.873 | 0.868 | 0.005 | - | - | 0.981 | 0.982 | 0.296 | 1.29x | 18.5/24.3/29.1% | 1.8/5.6% | 3 |
| 1.0 | 1 | 0.919 | 0.913 | 0.005 | - | - | 0.987 | 0.987 | 0.596 | 1.14x | 22.4/27.8/32.7% | 1.4/5.7% | 3 |

### `RF-eu-presets` - preset  `--scenario valleys`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.398 | 0.393 | 0.005 | - | - | 0.688 | 0.691 | 0.000 | 0.16x | 0.9/2.3/2.9% | 0.2/0.7% | 3 |
| LONG_FAST | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| LITE_FAST | 1 | 0.807 | 0.798 | 0.010 | - | - | 0.965 | 0.966 | 0.000 | 1.04x | 11.9/16.8/21.9% | 1.6/4.3% | 3 |
| NARROW_SLOW | 1 | 0.820 | 0.813 | 0.007 | - | - | 0.962 | 0.963 | 0.000 | 1.33x | 15.9/23.8/28.2% | 2.0/5.4% | 3 |

### `RF-noise` - noise-profile  `--scenario valleys`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| temporal | 1 | 0.771 | 0.762 | 0.009 | - | - | 0.950 | 0.953 | 0.043 | 1.30x | 16.9/23.1/27.7% | 1.9/5.3% | 3 |
| transient | 1 | 0.847 | 0.840 | 0.006 | - | - | 0.965 | 0.965 | 0.191 | 1.32x | 17.2/23.4/27.8% | 1.9/5.5% | 3 |
| periodic | 1 | 0.685 | 0.679 | 0.006 | - | - | 0.805 | 0.808 | 0.158 | 1.21x | 16.0/21.8/26.1% | 1.8/4.7% | 3 |

### `RF-preset` - preset  `--scenario valleys`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.398 | 0.393 | 0.005 | - | - | 0.688 | 0.691 | 0.000 | 0.16x | 0.9/2.3/2.9% | 0.2/0.7% | 3 |
| LONG_FAST | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| LONG_MODERATE | 1 | 0.829 | 0.803 | 0.026 | - | - | 0.928 | 0.930 | 0.630 | 3.33x | 46.3/58.3/61.6% | 4.2/12.6% | 3 |

> preset=LONG_MODERATE: decode_failures 13

### `RF-preset-turbo` - preset  `--scenario valleys`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.064 | 0.064 | 0.000 | - | - | 0.114 | 0.320 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.193 | 0.185 | 0.008 | - | - | 0.502 | 0.549 | 0.000 | 0.05x | 0.3/0.7/1.2% | 0.1/0.3% | 3 |
| LONG_FAST | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| LONG_TURBO | 1 | 0.762 | 0.751 | 0.011 | - | - | 0.945 | 0.947 | 0.000 | 1.26x | 13.2/19.9/23.4% | 1.9/5.2% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.845 | 0.839 | 0.006 | - | - | 0.964 | 0.965 | 0.407 | 1.85x | 22.4/31.7/37.0% | 2.5/7.4% | 3 |

> preset=SHORT_TURBO: decode_failures 17

### `RF-pulse` - noise-pulse-interval-ms  `--scenario valleys`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.798 | 0.792 | 0.006 | - | - | 0.917 | 0.918 | 0.194 | 1.28x | 16.9/23.1/27.7% | 1.8/5.2% | 3 |
| 10000 | 1 | 0.685 | 0.679 | 0.006 | - | - | 0.805 | 0.808 | 0.158 | 1.21x | 16.0/21.8/26.1% | 1.8/4.7% | 3 |
| 4000 | 1 | 0.464 | 0.460 | 0.005 | - | - | 0.545 | 0.608 | 0.082 | 1.05x | 14.1/19.4/23.2% | 1.6/3.7% | 3 |
| 2000 | 1 | 0.095 | 0.095 | 0.000 | - | - | 0.106 | 0.195 | 0.013 | 0.72x | 9.7/13.7/16.7% | 1.1/2.1% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 8

### `RF-stretch-duct` - duct-per-hour  `--scenario valleys`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.357 | 0.351 | 0.006 | - | - | 0.544 | 0.550 | 0.000 | 1.32x | 11.0/16.5/21.0% | 2.2/4.9% | 3 |
| 1.0 | 1 | 0.629 | 0.618 | 0.011 | - | - | 0.743 | 0.746 | 0.296 | 1.12x | 13.7/19.1/23.2% | 1.7/4.8% | 3 |

### `RF-txpower` - tx-power  `--scenario valleys`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 22 | 1 | 0.451 | 0.440 | 0.011 | - | - | 0.671 | 0.686 | 0.000 | 1.32x | 10.6/16.9/19.7% | 2.0/5.3% | 3 |
| 17 | 1 | 0.192 | 0.186 | 0.006 | - | - | 0.431 | 0.505 | 0.000 | 1.12x | 6.4/12.1/19.1% | 1.5/5.0% | 3 |
| 14 | 1 | 0.088 | 0.088 | 0.000 | - | - | 0.185 | 0.449 | 0.000 | 0.65x | 2.6/6.7/12.2% | 0.9/3.3% | 3 |

> tx-power=22: decode_failures 14

> tx-power=17: decode_failures 11

> tx-power=14: decode_failures 3

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario valleys`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.958 | 0.958 | 0.001 | - | - | 0.994 | 0.994 | 0.757 | 2.10x | 22.9/39.0/45.0% | 1.4/5.1% | 3 |
| True | 1 | 0.951 | 0.950 | 0.001 | - | - | 0.994 | 0.994 | 0.718 | 2.45x | 26.0/43.7/50.3% | 1.6/5.7% | 3 |

### `RT-favourites` - favourite-routers  `--scenario valleys`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.859 | 0.854 | 0.004 | - | - | 0.975 | 0.976 | 0.182 | 1.42x | 17.9/26.1/32.8% | 1.9/5.6% | 3 |
| True | 1 | 0.872 | 0.868 | 0.004 | - | - | 0.968 | 0.968 | 0.223 | 1.46x | 18.4/26.4/33.2% | 2.0/5.5% | 3 |

### `RT-hopassign` - hop-assign  `--scenario valleys`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| random | 1 | 0.854 | 0.847 | 0.007 | - | - | 0.971 | 0.972 | 0.241 | 1.24x | 16.4/22.2/26.7% | 1.7/5.2% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario valleys`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.701 | 0.681 | 0.021 | - | - | 0.906 | 0.910 | 0.060 | 0.97x | 13.1/19.6/23.0% | 1.3/4.7% | 3 |
| 7 | 1 | 0.897 | 0.895 | 0.002 | - | - | 0.969 | 0.969 | 0.258 | 1.45x | 18.5/24.6/29.4% | 2.1/5.6% | 3 |
| 15 | 1 | 0.904 | 0.902 | 0.002 | - | - | 0.961 | 0.962 | 0.264 | 1.44x | 18.4/24.4/29.3% | 2.1/5.6% | 3 |
| 32 | 1 | 0.909 | 0.907 | 0.002 | - | - | 0.967 | 0.967 | 0.271 | 1.42x | 18.2/24.0/28.8% | 2.1/5.5% | 3 |

### `RT-hopspread` - hop-limit  `--scenario valleys`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.701 | 0.681 | 0.021 | - | - | 0.906 | 0.910 | 0.060 | 0.97x | 13.1/19.6/23.0% | 1.3/4.7% | 3 |
| 5 | 1 | 0.844 | 0.836 | 0.008 | - | - | 0.954 | 0.956 | 0.181 | 1.30x | 17.2/23.2/27.6% | 1.8/5.3% | 3 |
| 7 | 1 | 0.897 | 0.895 | 0.002 | - | - | 0.969 | 0.969 | 0.258 | 1.45x | 18.5/24.6/29.4% | 2.1/5.6% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario valleys`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| KNOWN_ONLY | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.863 | 0.863 | 0.000 | - | - | 0.917 | 0.979 | 0.234 | 1.27x | 16.6/22.6/27.1% | 1.8/5.2% | 3 |

### `RT-spread` - hop-spread  `--scenario valleys`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.701 | 0.681 | 0.021 | - | - | 0.906 | 0.910 | 0.060 | 0.97x | 13.1/19.6/23.0% | 1.3/4.7% | 3 |
| True | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |

### `SC-signing` - signature-policy  `--scenario valleys`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| BALANCED | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| STRICT | 1 | 0.756 | 0.756 | 0.000 | - | - | 0.887 | 0.887 | 0.125 | 1.41x | 18.5/25.0/29.9% | 2.0/5.8% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario valleys`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| dm | 1 | 0.857 | 0.851 | 0.006 | - | - | 0.974 | 0.975 | 0.219 | 1.28x | 16.8/23.0/27.8% | 1.8/5.5% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario valleys`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.854 | 0.850 | 0.004 | - | - | 0.971 | 0.973 | 0.222 | 1.31x | 17.1/23.5/28.0% | 1.8/5.5% | 3 |
| local | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| time | 1 | 0.858 | 0.854 | 0.004 | - | - | 0.971 | 0.976 | 0.222 | 1.36x | 17.8/24.3/28.8% | 1.9/5.7% | 3 |
| window | 1 | 0.854 | 0.849 | 0.005 | - | - | 0.973 | 0.976 | 0.203 | 1.31x | 17.2/23.5/28.1% | 1.8/5.4% | 3 |

> bucket-mode=global: misdecodes 40

> bucket-mode=time: misdecodes 13

> bucket-mode=window: misdecodes 25

### `SF-bucket-time` - time-bucket-s  `--scenario valleys`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.852 | 0.847 | 0.005 | - | - | 0.979 | 0.980 | 0.213 | 1.45x | 19.0/25.8/30.6% | 2.0/6.2% | 3 |
| 1800 | 1 | 0.858 | 0.854 | 0.004 | - | - | 0.971 | 0.976 | 0.222 | 1.36x | 17.8/24.3/28.8% | 1.9/5.7% | 3 |
| 3600 | 1 | 0.854 | 0.849 | 0.005 | - | - | 0.968 | 0.977 | 0.223 | 1.32x | 17.2/23.6/28.1% | 1.9/5.5% | 3 |

> time-bucket-s=600: misdecodes 116

> time-bucket-s=1800: misdecodes 13

> time-bucket-s=3600: misdecodes 5

### `SF-cadence` - trigger  `--scenario valleys`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| interval | 1 | 0.834 | 0.827 | 0.008 | - | - | 0.969 | 0.971 | 0.229 | 1.75x | 22.6/31.2/37.2% | 2.5/8.0% | 3 |
| aimd | 1 | 0.850 | 0.849 | 0.001 | - | - | 0.910 | 0.973 | 0.192 | 1.33x | 17.3/23.6/28.2% | 1.9/5.5% | 3 |
| bucket+interval | 1 | 0.815 | 0.805 | 0.010 | - | - | 0.945 | 0.946 | 0.224 | 1.78x | 22.9/31.7/37.6% | 2.5/8.2% | 3 |

> trigger=interval: misdecodes 12

> trigger=interval: decode_failures 3

> trigger=aimd: misdecodes 3

> trigger=aimd: decode_failures 3

> trigger=bucket+interval: misdecodes 12

### `SF-capacity` - capacity  `--scenario valleys`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.852 | 0.847 | 0.005 | - | - | 0.970 | 0.974 | 0.224 | 1.33x | 17.3/23.7/28.5% | 1.8/5.6% | 3 |
| 8 | 1 | 0.849 | 0.843 | 0.006 | - | - | 0.964 | 0.967 | 0.213 | 1.30x | 17.1/23.4/27.9% | 1.8/5.6% | 3 |
| 16 | 1 | 0.865 | 0.860 | 0.004 | - | - | 0.981 | 0.983 | 0.209 | 1.31x | 17.2/23.4/27.9% | 1.8/5.4% | 3 |
| 32 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 50 | 1 | 0.848 | 0.842 | 0.006 | - | - | 0.974 | 0.975 | 0.231 | 1.32x | 17.2/23.5/28.2% | 1.9/5.6% | 3 |

> capacity=4: decode_failures 95

> capacity=8: decode_failures 32

### `SF-capacity-local` - capacity  `--scenario valleys`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.852 | 0.847 | 0.005 | - | - | 0.970 | 0.974 | 0.224 | 1.33x | 17.3/23.7/28.5% | 1.8/5.6% | 3 |
| 8 | 1 | 0.849 | 0.843 | 0.006 | - | - | 0.964 | 0.967 | 0.213 | 1.30x | 17.1/23.4/27.9% | 1.8/5.6% | 3 |
| 16 | 1 | 0.865 | 0.860 | 0.004 | - | - | 0.981 | 0.983 | 0.209 | 1.31x | 17.2/23.4/27.9% | 1.8/5.4% | 3 |
| 32 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 50 | 1 | 0.848 | 0.842 | 0.006 | - | - | 0.974 | 0.975 | 0.231 | 1.32x | 17.2/23.5/28.2% | 1.9/5.6% | 3 |

> capacity=4: decode_failures 95

> capacity=8: decode_failures 32

### `SF-capacity-window` - capacity  `--scenario valleys`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.850 | 0.846 | 0.004 | - | - | 0.958 | 0.968 | 0.211 | 1.27x | 16.7/22.8/27.2% | 1.8/5.3% | 3 |
| 16 | 1 | 0.852 | 0.847 | 0.005 | - | - | 0.969 | 0.969 | 0.212 | 1.29x | 16.9/23.0/27.6% | 1.8/5.4% | 3 |
| 32 | 1 | 0.854 | 0.849 | 0.005 | - | - | 0.973 | 0.976 | 0.203 | 1.31x | 17.2/23.5/28.1% | 1.8/5.4% | 3 |

> capacity=8: misdecodes 19

> capacity=8: decode_failures 27

> capacity=16: misdecodes 14

> capacity=32: misdecodes 25

### `SF-catchup` - catch-up-hours  `--scenario valleys`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.815 | 0.805 | 0.010 | - | - | 0.945 | 0.946 | 0.224 | 1.78x | 22.9/31.7/37.6% | 2.5/8.2% | 3 |
| 02-06 | 1 | 0.851 | 0.847 | 0.004 | - | - | 0.940 | 0.974 | 0.220 | 1.33x | 17.4/23.8/28.5% | 1.9/5.7% | 3 |
| 00-08 | 1 | 0.855 | 0.851 | 0.003 | - | - | 0.945 | 0.979 | 0.221 | 1.40x | 18.2/24.8/30.0% | 2.0/6.2% | 3 |

> catch-up-hours=: misdecodes 12

> catch-up-hours=02-06: misdecodes 2

> catch-up-hours=02-06: decode_failures 41

> catch-up-hours=00-08: misdecodes 1

> catch-up-hours=00-08: decode_failures 42

### `SF-hops-flat` - hops-apart  `--scenario valleys`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.850 | 0.848 | 0.003 | - | - | 0.947 | 0.949 | 0.203 | 1.31x | 17.0/23.3/28.0% | 1.8/5.4% | 3 |
| 2 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 3 | 1 | 0.870 | 0.849 | 0.021 | - | - | 0.930 | 0.959 | 0.207 | 1.31x | 17.0/23.4/27.9% | 1.8/5.4% | 3 |
| 4 | 1 | 0.860 | 0.840 | 0.019 | - | - | 0.945 | 0.969 | 0.217 | 1.33x | 17.3/24.0/28.6% | 1.8/5.6% | 3 |

> hops-apart=3: decode_failures 22

> hops-apart=4: decode_failures 29

### `SF-hops-spread` - hops-apart  `--scenario valleys`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.850 | 0.848 | 0.003 | - | - | 0.947 | 0.949 | 0.203 | 1.31x | 17.0/23.3/28.0% | 1.8/5.4% | 3 |
| 2 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 3 | 1 | 0.870 | 0.849 | 0.021 | - | - | 0.930 | 0.959 | 0.207 | 1.31x | 17.0/23.4/27.9% | 1.8/5.4% | 3 |
| 4 | 1 | 0.860 | 0.840 | 0.019 | - | - | 0.945 | 0.969 | 0.217 | 1.33x | 17.3/24.0/28.6% | 1.8/5.6% | 3 |
| 5 | 1 | 0.887 | 0.852 | 0.035 | - | - | 0.962 | 0.970 | 0.223 | 1.31x | 17.0/23.6/28.2% | 1.9/5.6% | 3 |

> hops-apart=3: decode_failures 22

> hops-apart=4: decode_failures 29

> hops-apart=5: decode_failures 1

### `SF-jitter-global` - advert-jitter-s  `--scenario valleys`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.856 | 0.850 | 0.006 | - | - | 0.977 | 0.978 | 0.203 | 1.29x | 16.9/23.2/27.6% | 1.8/5.4% | 3 |
| 30 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 120 | 1 | 0.851 | 0.846 | 0.005 | - | - | 0.973 | 0.973 | 0.205 | 1.31x | 17.1/23.5/28.0% | 1.8/5.5% | 3 |
| 600 | 1 | 0.866 | 0.862 | 0.004 | - | - | 0.980 | 0.983 | 0.225 | 1.31x | 17.2/23.4/28.0% | 1.8/5.5% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario valleys`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.856 | 0.850 | 0.006 | - | - | 0.977 | 0.978 | 0.203 | 1.29x | 16.9/23.2/27.6% | 1.8/5.4% | 3 |
| 30 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 120 | 1 | 0.851 | 0.846 | 0.005 | - | - | 0.973 | 0.973 | 0.205 | 1.31x | 17.1/23.5/28.0% | 1.8/5.5% | 3 |
| 600 | 1 | 0.866 | 0.862 | 0.004 | - | - | 0.980 | 0.983 | 0.225 | 1.31x | 17.2/23.4/28.0% | 1.8/5.5% | 3 |

### `SF-place-flat` - place  `--scenario valleys`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.862 | 0.853 | 0.010 | - | - | 0.645 | 0.939 | 0.233 | 1.29x | 16.9/22.9/27.5% | 1.8/5.3% | 3 |
| routers | 1 | 0.852 | 0.850 | 0.002 | - | - | 0.971 | 0.972 | 0.203 | 1.29x | 16.9/23.1/27.7% | 1.8/5.4% | 3 |
| alternate-routers | 1 | 0.862 | 0.858 | 0.003 | - | - | 0.975 | 0.977 | 0.208 | 1.32x | 17.2/23.7/28.1% | 1.8/5.4% | 3 |
| beside-router | 1 | 0.857 | 0.850 | 0.006 | - | - | 0.978 | 0.979 | 0.203 | 1.30x | 17.0/23.5/28.1% | 1.8/5.4% | 3 |
| random-clients | 1 | 0.890 | 0.854 | 0.035 | - | - | 0.953 | 0.973 | 0.213 | 1.33x | 17.4/23.6/28.3% | 1.9/5.4% | 3 |
| hops-apart | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |

> place=spread: decode_failures 23

### `SF-place-spread` - place  `--scenario valleys`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.862 | 0.853 | 0.010 | - | - | 0.645 | 0.939 | 0.233 | 1.29x | 16.9/22.9/27.5% | 1.8/5.3% | 3 |
| routers | 1 | 0.852 | 0.850 | 0.002 | - | - | 0.971 | 0.972 | 0.203 | 1.29x | 16.9/23.1/27.7% | 1.8/5.4% | 3 |
| alternate-routers | 1 | 0.862 | 0.858 | 0.003 | - | - | 0.975 | 0.977 | 0.208 | 1.32x | 17.2/23.7/28.1% | 1.8/5.4% | 3 |
| beside-router | 1 | 0.857 | 0.850 | 0.006 | - | - | 0.978 | 0.979 | 0.203 | 1.30x | 17.0/23.5/28.1% | 1.8/5.4% | 3 |
| random-clients | 1 | 0.890 | 0.854 | 0.035 | - | - | 0.953 | 0.973 | 0.213 | 1.33x | 17.4/23.6/28.3% | 1.9/5.4% | 3 |
| hops-apart | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |

> place=spread: decode_failures 23

### `SF-provide-transport` - provide-transport  `--scenario valleys`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| broadcast | 1 | 0.876 | 0.843 | 0.034 | - | - | 0.971 | 0.973 | 0.280 | 1.40x | 18.3/24.7/29.4% | 2.0/5.8% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario valleys`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| heard | 1 | 0.860 | 0.854 | 0.005 | - | - | 0.977 | 0.979 | 0.232 | 1.31x | 17.2/23.6/28.1% | 1.8/5.5% | 3 |

> replay-ordering=heard: misdecodes 19

### `SF-replay-order-broadcast` - replay-ordering  `--scenario valleys`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.876 | 0.843 | 0.034 | - | - | 0.971 | 0.973 | 0.280 | 1.40x | 18.3/24.7/29.4% | 2.0/5.8% | 3 |
| heard | 1 | 0.879 | 0.844 | 0.035 | - | - | 0.974 | 0.976 | 0.258 | 1.41x | 18.4/24.9/29.6% | 2.0/5.8% | 3 |

> replay-ordering=heard: misdecodes 7

### `SF-resolve` - resolve  `--scenario valleys`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| enum | 1 | 0.854 | 0.847 | 0.006 | - | - | 0.971 | 0.973 | 0.200 | 1.32x | 17.1/23.6/28.3% | 1.8/5.7% | 3 |
| hybrid | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |

### `SF-servers-allrouters` - servers  `--scenario valleys`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.852 | 0.850 | 0.002 | - | - | 0.971 | 0.972 | 0.203 | 1.29x | 16.9/23.1/27.7% | 1.8/5.4% | 3 |
| 6 | 1 | 0.855 | 0.851 | 0.004 | - | - | 0.972 | 0.973 | 0.208 | 1.34x | 17.5/23.9/28.5% | 1.9/5.6% | 6 |

### `SF-servers-flat` - servers  `--scenario valleys`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.856 | 0.854 | 0.002 | - | - | 0.960 | 0.968 | 0.218 | 1.29x | 16.8/23.0/27.5% | 1.8/5.3% | 2 |
| 3 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 5 | 1 | 0.863 | 0.851 | 0.013 | - | - | 0.972 | 0.974 | 0.222 | 1.34x | 17.5/23.7/28.4% | 1.9/5.5% | 5 |
| 8 | 1 | 0.858 | 0.843 | 0.015 | - | - | 0.975 | 0.977 | 0.213 | 1.38x | 18.0/24.4/29.3% | 2.0/5.7% | 8 |

### `SF-servers-spread` - servers  `--scenario valleys`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.856 | 0.854 | 0.002 | - | - | 0.960 | 0.968 | 0.218 | 1.29x | 16.8/23.0/27.5% | 1.8/5.3% | 2 |
| 3 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 5 | 1 | 0.863 | 0.851 | 0.013 | - | - | 0.972 | 0.974 | 0.222 | 1.34x | 17.5/23.7/28.4% | 1.9/5.5% | 5 |
| 8 | 1 | 0.858 | 0.843 | 0.015 | - | - | 0.975 | 0.977 | 0.213 | 1.38x | 18.0/24.4/29.3% | 2.0/5.7% | 8 |

### `SF-signed` - signed  `--scenario valleys`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| True | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario valleys`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.858 | 0.853 | 0.005 | - | - | 0.964 | 0.969 | 0.215 | 1.19x | 15.8/21.5/25.8% | 1.7/5.0% | 3 |
| 1 | 1 | 0.860 | 0.854 | 0.007 | - | - | 0.975 | 0.978 | 0.216 | 1.21x | 16.0/21.8/26.1% | 1.7/5.1% | 3 |
| 2 | 1 | 0.846 | 0.841 | 0.005 | - | - | 0.962 | 0.964 | 0.259 | 1.21x | 16.0/21.9/26.1% | 1.7/5.1% | 3 |
| 4 | 1 | 0.858 | 0.853 | 0.005 | - | - | 0.973 | 0.975 | 0.226 | 1.17x | 15.5/21.2/25.3% | 1.6/5.0% | 3 |

### `SF-width` - short-id-bits  `--scenario valleys`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.858 | 0.854 | 0.004 | - | - | 0.973 | 0.974 | 0.222 | 1.29x | 16.9/23.2/27.8% | 1.8/5.4% | 3 |
| 24 | 1 | 0.856 | 0.851 | 0.005 | - | - | 0.979 | 0.981 | 0.212 | 1.32x | 17.3/23.8/28.4% | 1.9/5.6% | 3 |
| 32 | 1 | 0.847 | 0.842 | 0.005 | - | - | 0.966 | 0.966 | 0.199 | 1.31x | 17.1/23.4/28.0% | 1.9/5.5% | 3 |
| 64 | 1 | 0.856 | 0.851 | 0.004 | - | - | 0.972 | 0.973 | 0.224 | 1.32x | 17.3/23.6/28.1% | 1.9/5.5% | 3 |

### `SF-window-size` - window-size  `--scenario valleys`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.848 | 0.842 | 0.006 | - | - | 0.970 | 0.972 | 0.210 | 1.39x | 18.2/24.8/29.4% | 1.9/5.8% | 3 |
| 16 | 1 | 0.857 | 0.851 | 0.005 | - | - | 0.978 | 0.979 | 0.217 | 1.32x | 17.3/23.6/28.1% | 1.8/5.5% | 3 |
| 32 | 1 | 0.854 | 0.849 | 0.005 | - | - | 0.973 | 0.976 | 0.203 | 1.31x | 17.2/23.5/28.1% | 1.8/5.4% | 3 |

> window-size=8: misdecodes 103

> window-size=16: misdecodes 71

> window-size=32: misdecodes 25

### `TH-congestion` - no-congestion-scaling  `--scenario valleys`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.958 | 0.958 | 0.001 | - | - | 0.994 | 0.994 | 0.757 | 2.10x | 22.9/39.0/45.0% | 1.4/5.1% | 3 |
| True | 1 | 0.745 | 0.738 | 0.008 | - | - | 0.838 | 0.871 | 0.498 | 5.62x | 56.0/74.7/79.3% | 4.0/12.2% | 3 |

> no-congestion-scaling=True: queue drops 14.0% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 61

### `TH-congestion-input` - congestion-input  `--scenario valleys`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.549 | 0.538 | 0.011 | - | - | 0.837 | 0.841 | 0.172 | 4.76x | 16.5/32.9/47.2% | 1.6/6.2% | 3 |
| truesize | 1 | 0.589 | 0.578 | 0.010 | - | - | 0.870 | 0.873 | 0.179 | 3.61x | 12.4/26.4/38.7% | 1.2/5.2% | 3 |

> congestion-input=hotstore: decode_failures 8

### `TH-congestion-mode` - congestion-mode  `--scenario valleys`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.962 | 0.961 | 0.001 | - | - | 0.997 | 0.997 | 0.760 | 1.95x | 21.2/36.4/42.0% | 1.2/4.8% | 3 |
| adaptive | 1 | 0.958 | 0.958 | 0.001 | - | - | 0.994 | 0.994 | 0.757 | 2.10x | 22.9/39.0/45.0% | 1.4/5.1% | 3 |

