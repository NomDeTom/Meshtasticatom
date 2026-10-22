# Sweep blocks-2026-10-22-5470031

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** rolling
- **seed base** 5470031 · seeds 5470031
- **blocks** 87 run
- **compute** 10.7 h of simulator time across every cell
- **generated** 2026-10-22T09:20:26+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>85 warnings</summary>

- AD-badrouters: role-placement=degree: decode_failures 2
- AD-flooding: role-mix=baymesh-2026-08: decode_failures 2
- AD-nomute: role-mix=baymesh-2026-08: decode_failures 2
- AD-siting: siting-mix=uniform: decode_failures 2
- AD-siting: siting-mix=local-typical: decode_failures 3
- DB-hotstore: max-num-nodes=10: decode_failures 31
- DB-hotstore-stress: max-num-nodes=10: decode_failures 9
- DB-hotstore-stress: faster: 9.43 s per simulated hour against 21.8 over 62 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- DB-warm: warm-num-nodes=0: queue drops 11.0% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 116
- DB-warm: warm-num-nodes=25: queue drops 11.0% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 116
- DB-warm: warm-num-nodes=100: queue drops 11.0% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 116
- DB-warm: warm-num-nodes=2000: queue drops 11.0% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 116
- DG-burst: burst-loss=0.2: decode_failures 36
- DG-burst: burst-loss=0.3: decode_failures 32
- DG-loss: faster: 1.1 s per simulated hour against 2.28 over 62 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- DG-outage: burst-loss=0.1: decode_failures 27
- DG-outage: burst-loss=0.2: decode_failures 33
- DG-outage: burst-loss=0.3: decode_failures 23
- DM-mode: dm-mode=flood-only: decode_failures 15
- DM-mode: dm-mode=m4-early-flood: decode_failures 39
- DM-mode: slower: 8.06 s per simulated hour against 3.12 over 62 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 23
- LD-chatty: broadcast-interval-s=300: decode_failures 23
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 11.0% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 116
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 22.8% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 74
- MS-density: nodes=150: misdecodes 2
- MS-hopscale: nodes=500: decode_failures 223
- MS-oversubscribed: nodes=500: decode_failures 87
- MS-roles: role-mix=baymesh-2026-08: decode_failures 2
- MS-siting: siting-mix=local-typical: decode_failures 22
- MS-size: nodes=150: decode_failures 3
- MS-stretch: stretch=1.25: decode_failures 19
- MS-stretch: stretch=1.5: decode_failures 7
- PR-crladder: coding-rate-ladder=True: decode_failures 2
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 2
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 11
- RF-bw500: preset=SHORT_TURBO: decode_failures 1
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 12
- RF-preset: preset=LONG_MODERATE: decode_failures 5
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 1
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 6
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 7
- RF-stretch-duct: duct-per-hour=1.0: decode_failures 25
- RF-stretch-duct: slower: 6.16 s per simulated hour against 1.83 over 62 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-txpower: tx-power=22: decode_failures 10
- RT-hoplimit: hop-limit=3: decode_failures 1
- RT-hopspread: hop-limit=3: decode_failures 1
- RT-spread: hop-spread=False: decode_failures 1
- SF-bucket-mode: bucket-mode=global: misdecodes 32
- SF-bucket-mode: bucket-mode=time: misdecodes 24
- SF-bucket-mode: bucket-mode=window: misdecodes 31
- SF-bucket-time: time-bucket-s=600: misdecodes 99
- SF-bucket-time: time-bucket-s=1800: misdecodes 24
- SF-bucket-time: time-bucket-s=3600: misdecodes 9
- SF-cadence: trigger=interval: misdecodes 18
- SF-cadence: trigger=aimd: misdecodes 4
- SF-cadence: trigger=bucket+interval: misdecodes 15
- SF-capacity-local: capacity=4: decode_failures 77
- SF-capacity-local: capacity=8: decode_failures 28
- SF-capacity: capacity=4: decode_failures 77
- SF-capacity: capacity=8: decode_failures 28
- SF-capacity-window: capacity=8: misdecodes 35
- SF-capacity-window: capacity=8: decode_failures 16
- SF-capacity-window: capacity=16: misdecodes 25
- SF-capacity-window: capacity=32: misdecodes 31
- SF-catchup: catch-up-hours=: misdecodes 15
- SF-catchup: catch-up-hours=02-06: decode_failures 24
- SF-catchup: catch-up-hours=00-08: decode_failures 24
- SF-hops-flat: hops-apart=4: decode_failures 43
- SF-hops-spread: hops-apart=4: decode_failures 43
- SF-hops-spread: hops-apart=5: decode_failures 24
- SF-place-flat: place=spread: decode_failures 26
- SF-place-spread: place=spread: decode_failures 26
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 8
- SF-replay-order: replay-ordering=heard: misdecodes 22
- SF-window-size: window-size=8: misdecodes 130
- SF-window-size: window-size=16: misdecodes 72
- SF-window-size: window-size=32: misdecodes 31
- TH-congestion: no-congestion-scaling=True: decode_failures 89

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `RF-stretch-duct` | 6.16 | 1.82 | 3.38x | 62 |
| `DM-mode` | 8.06 | 3.12 | 2.58x | 62 |
| `DB-hotstore` | 4.32 | 2.37 | 1.83x | 62 |
| `MS-stretch` | 3.37 | 2.03 | 1.66x | 62 |
| `MS-siting` | 2.87 | 1.82 | 1.58x | 61 |
| `MS-hopscale` | 26.7 | 17.1 | 1.56x | 62 |
| `SF-capacity-window` | 1.07 | 1.61 | 0.67x | 62 |
| `RF-duct` | 1.15 | 1.75 | 0.66x | 62 |
| `PR-protocol` | 0.875 | 1.39 | 0.63x | 62 |
| `SF-window-size` | 0.852 | 1.37 | 0.62x | 62 |
| `FW-signing-cost` | 0.961 | 1.59 | 0.60x | 62 |
| `SF-cadence` | 2.14 | 3.61 | 0.59x | 62 |
| `SF-jitter-local` | 1.06 | 1.79 | 0.59x | 62 |
| `SF-servers-flat` | 1.28 | 2.3 | 0.56x | 62 |
| `MS-topology` | 0.976 | 1.91 | 0.51x | 62 |
| `RF-preset-turbo` | 0.781 | 1.53 | 0.51x | 58 |
| `DG-loss` | 1.1 | 2.28 | 0.48x | 62 |
| `DB-hotstore-stress` | 9.43 | 21.8 | 0.43x | 62 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.995 | 0.995 | 0.836 → 0.860 | 1.1x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.980 | 0.980 | 0.849 → 0.860 | 1.1x bytes_on_air | up | 2 |
| `RF-txpower` | tx-power | **held** | 0.072 → 0.995 | 0.923 | 0.064 → 0.856 | 39x sr_bytes | down | 4 |
| `RF-preset-turbo` | preset | **held** | 0.074 → 0.995 | 0.921 | 0.054 → 0.856 | 37x sr_bytes | up | 5 |
| `MS-siting` | siting-mix | **held** | 0.100 → 0.999 | 0.899 | 0.134 → 0.974 | 41x sr_bytes | up | 4 |
| `RF-bw500` | preset | **held** | 0.074 → 0.963 | 0.889 | 0.097 → 0.744 | 36x sr_bytes | up | 3 |
| `AD-siting` | siting-mix | **held** | 0.039 → 0.918 | 0.879 | 0.029 → 0.659 | 1.1e+02x sr_bytes | down | 3 |
| `MS-stretch` | stretch | **held** | 0.120 → 0.995 | 0.874 | 0.085 → 0.856 | 42x sr_bytes | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.141 → 0.946 | 0.804 | 0.110 → 0.801 | 73x sr_airtime | down | 4 |
| `RF-eu-presets` | preset | **text** | 0.251 → 0.865 | 0.615 | 0.248 → 0.856 | 2.5x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.251 → 0.865 | 0.615 | 0.248 → 0.856 | 4.1x sr_airtime | up | 3 |
| `MS-hopscale` | nodes | **text** | 0.319 → 0.865 | 0.546 | 0.314 → 0.856 | 18x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **text** | 0.323 → 0.772 | 0.449 | 0.318 → 0.763 | 4.9x bytes_on_air | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **held** | 0.354 → 0.771 | 0.416 | 0.352 → 0.641 | 5.5x sr_airtime | up | 2 |
| `MS-topology` | topology | **text** | 0.562 → 0.935 | 0.373 | 0.551 → 0.935 | 2.2x sr_airtime | up | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.569 → 0.928 | 0.360 | 0.547 → 0.926 | 7.7x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.520 → 0.865 | 0.345 | 0.497 → 0.856 | 2.4x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.559 → 0.888 | 0.329 | 0.533 → 0.884 | 7x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.538 → 0.865 | 0.327 | 0.498 → 0.856 | 2.7x sr_bytes | down | 4 |
| `MS-density` | nodes | **text** | 0.683 → 0.972 | 0.289 | 0.656 → 0.971 | 6.2x sr_airtime | up | 5 |
| `RT-hoplimit` | hop-limit | **text** | 0.672 → 0.937 | 0.265 | 0.631 → 0.935 | 2.7x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.672 → 0.909 | 0.238 | 0.631 → 0.905 | 2.1x sr_bytes | up | 3 |
| `MS-size` | nodes | **text** | 0.641 → 0.865 | 0.224 | 0.620 → 0.856 | 6.6x sr_bytes | down | 5 |
| `AD-flooding` | role-mix | **text** | 0.695 → 0.913 | 0.218 | 0.659 → 0.909 | 2.6x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.695 → 0.913 | 0.218 | 0.659 → 0.909 | 2.6x bytes_on_air | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.672 → 0.865 | 0.194 | 0.631 → 0.856 | 2.2x sr_bytes | up | 2 |
| `DB-hotstore-stress` | max-num-nodes | **text** | 0.319 → 0.508 | 0.189 | 0.315 → 0.504 | 4x sr_airtime | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.780 → 0.965 | 0.185 | 0.769 → 0.963 | 3.7x sr_airtime | down | 2 |
| `MS-roles` | role-mix | **text** | 0.695 → 0.869 | 0.174 | 0.659 → 0.860 | 1.8x sr_bytes | down | 2 |
| `RF-noise` | noise-profile | **text** | 0.705 → 0.865 | 0.160 | 0.692 → 0.856 | 1.4x sr_bytes | down | 4 |
| `SC-signing` | signature-policy | **text** | 0.706 → 0.865 | 0.160 | 0.706 → 0.856 | 1.1x advert_bytes | down | 3 |
| `DG-loss` | extra-loss | **text** | 0.712 → 0.865 | 0.153 | 0.691 → 0.856 | 1.5x sr_bytes | down | 4 |
| `SF-hops-flat` | hops-apart | **held** | 0.853 → 0.995 | 0.142 | 0.847 → 0.856 | 4.1x sr_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.853 → 0.995 | 0.142 | 0.847 → 0.856 | 4.1x sr_bytes | down | 5 |
| `MS-roles-fav` | role-mix | **text** | 0.748 → 0.874 | 0.127 | 0.723 → 0.866 | 1.5x sr_bytes | down | 2 |
| `DB-platform` | platform-mix | **text** | 0.775 → 0.889 | 0.113 | 0.759 → 0.884 | 2.1x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.784 → 0.889 | 0.104 | 0.770 → 0.884 | 2x sr_airtime | up | 4 |
| `LD-interval` | broadcast-interval-s | **text** | 0.808 → 0.905 | 0.097 | 0.794 → 0.901 | 4.8x sr_airtime | up | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.686 → 0.780 | 0.094 | 0.679 → 0.771 | 1.5x sr_airtime | down | 2 |
| `AD-amplify-worst` | amplify-worst | **held** | 0.906 → 0.995 | 0.089 | 0.856 → 0.935 | 1.8x sr_airtime | down | 3 |
| `SF-place-flat` | place | **held** | 0.911 → 0.995 | 0.084 | 0.843 → 0.856 | 4.1x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.911 → 0.995 | 0.084 | 0.843 → 0.856 | 4.1x sr_bytes | up | 6 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.865 → 0.944 | 0.079 | 0.856 → 0.944 | 1.6x sr_airtime | up | 3 |
| `AD-badrouters` | role-placement | **text** | 0.695 → 0.774 | 0.079 | 0.659 → 0.760 | 1.4x sr_bytes | up | 3 |
| `FW-mixed` | legacy-fraction | **text** | 0.815 → 0.886 | 0.071 | 0.804 → 0.878 | 2.2x bytes_on_air | up | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.865 → 0.927 | 0.062 | 0.856 → 0.922 | 1.4x sr_bytes | up | 3 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.820 → 0.880 | 0.061 | 0.810 → 0.873 | 2.4x bytes_on_air | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.937 → 0.995 | 0.058 | 0.851 → 0.856 | 20x sr_airtime | down | 3 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.813 → 0.865 | 0.052 | 0.798 → 0.856 | 1.4x sr_airtime | down | 4 |
| `AD-worst` | role-placement | **text** | 0.771 → 0.821 | 0.050 | 0.754 → 0.812 | 1.2x sr_bytes | down | 2 |
| `SF-cadence` | trigger | **held** | 0.950 → 0.995 | 0.044 | 0.819 → 0.856 | 13x advert_bytes | down | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.865 → 0.900 | 0.035 | 0.856 → 0.896 | 3.3x bytes_on_air | down | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.623 → 0.657 | 0.034 | 0.498 → 0.530 | 1.5x sr_airtime | up | 2 |
| `SF-catchup` | catch-up-hours | **held** | 0.958 → 0.980 | 0.023 | 0.821 → 0.844 | 9.5x advert_bytes | down | 3 |
| `FW-versions` | profile | **text** | 0.857 → 0.876 | 0.020 | 0.848 → 0.867 | 3.5x bytes_on_air | up | 5 |
| `SF-provide-transport` | provide-transport | **held** | 0.978 → 0.995 | 0.017 | 0.841 → 0.856 | 2.5x sr_airtime | down | 2 |
| `SF-resolve` | resolve | **held** | 0.978 → 0.995 | 0.017 | 0.842 → 0.856 | 5.7x advert_bytes | = | 3 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.851 → 0.865 | 0.015 | 0.841 → 0.856 | 1.1x sr_airtime | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.851 → 0.865 | 0.015 | 0.841 → 0.856 | 1.1x sr_airtime | down | 4 |
| `SF-servers-allrouters` | servers | **held** | 0.900 → 0.915 | 0.014 | 0.837 → 0.849 | 2.5x sr_bytes | down | 2 |
| `MS-router-late` | router-late-fraction | **held** | 0.982 → 0.995 | 0.013 | 0.856 → 0.863 | 1.3x bytes_on_air | down | 4 |
| `SF-capacity` | capacity | **text** | 0.852 → 0.865 | 0.013 | 0.842 → 0.856 | 5.3x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **text** | 0.852 → 0.865 | 0.013 | 0.842 → 0.856 | 5.3x advert_bytes | down | 5 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.853 → 0.865 | 0.012 | 0.842 → 0.856 | 2.4x advert_bytes | up | 4 |
| `SF-servers-flat` | servers | **text** | 0.856 → 0.868 | 0.012 | 0.838 → 0.856 | 6.8x sr_bytes | down | 4 |
| `SF-servers-spread` | servers | **text** | 0.856 → 0.868 | 0.012 | 0.838 → 0.856 | 6.8x sr_bytes | down | 4 |
| `SF-sr-retries` | sr-retries | **text** | 0.855 → 0.866 | 0.011 | 0.846 → 0.859 | 1.2x sr_bytes | up | 4 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.842 → 0.853 | 0.011 | 0.832 → 0.842 | 5.3x advert_bytes | up | 3 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.955 → 0.965 | 0.010 | 0.953 → 0.963 | 1.2x sr_airtime | down | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.985 → 0.995 | 0.009 | 0.847 → 0.856 | 2.5x sr_airtime | down | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.858 → 0.867 | 0.009 | 0.850 → 0.859 | 1x sr_airtime | up | 2 |
| `RT-hopassign` | hop-assign | **text** | 0.856 → 0.865 | 0.009 | 0.845 → 0.856 | 1.4x sr_airtime | down | 2 |
| `DM-mode` | dm-mode | **text** | 0.814 → 0.822 | 0.009 | 0.814 → 0.822 | 1.2x sr_airtime | up | 3 |
| `LD-diurnal` | diurnal | **text** | 0.865 → 0.874 | 0.009 | 0.856 → 0.867 | 1.4x sr_bytes | down | 3 |
| `SF-replay-order` | replay-ordering | **text** | 0.857 → 0.865 | 0.008 | 0.846 → 0.856 | 1.2x sr_bytes | down | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.966 → 0.974 | 0.008 | 0.820 → 0.825 | 1.1x sr_airtime | up | 2 |
| `SF-width` | short-id-bits | **text** | 0.857 → 0.865 | 0.008 | 0.848 → 0.856 | 3.1x advert_bytes | up | 4 |
| `SF-window-size` | window-size | **held** | 0.983 → 0.991 | 0.008 | 0.846 → 0.853 | 5x advert_bytes | down | 3 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.967 → 0.974 | 0.007 | 0.825 → 0.828 | 1x sr_bytes | down | 2 |
| `SF-capacity-window` | capacity | **text** | 0.854 → 0.861 | 0.007 | 0.844 → 0.852 | 2.2x advert_bytes | down | 3 |
| `FW-firmware` | profile | **held** | 0.989 → 0.995 | 0.005 | 0.852 → 0.856 | 3.3x bytes_on_air | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.877 → 0.883 | 0.005 | 0.835 → 0.841 | 1.2x sr_airtime | up | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.862 → 0.865 | 0.003 | 0.852 → 0.856 | 1x sr_airtime | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.965 → 0.966 | 0.001 | 0.963 → 0.965 | 1x sr_airtime | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.965 → 0.966 | 0.001 | 0.963 → 0.964 | 1x sr_airtime | down | 2 |

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
| none | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| sprinkled | 1 | 0.944 | 0.944 | 0.001 | - | - | 0.988 | 0.988 | 0.700 | 1.02x | 18.8/23.5/27.6% | 1.3/5.2% | 3 |
| arms-race | 1 | 0.933 | 0.932 | 0.001 | - | - | 0.965 | 0.965 | 0.714 | 1.06x | 24.3/30.6/34.0% | 1.3/5.5% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario rolling`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 0.1 | 1 | 0.897 | 0.884 | 0.013 | - | - | 0.906 | 0.908 | 0.748 | 1.26x | 17.7/23.6/27.7% | 2.0/5.2% | 3 |
| 0.3 | 1 | 0.943 | 0.935 | 0.008 | - | - | 0.983 | 0.983 | 0.856 | 1.00x | 20.7/25.7/30.7% | 1.2/5.1% | 3 |

### `AD-badrouters` - role-placement  `--scenario rolling`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.695 | 0.659 | 0.035 | - | - | 0.918 | 0.939 | 0.205 | 1.04x | 14.9/20.4/24.0% | 1.8/4.6% | 3 |
| inverse | 1 | 0.774 | 0.760 | 0.014 | - | - | 0.979 | 0.984 | 0.421 | 1.14x | 13.9/18.4/21.5% | 2.2/3.5% | 3 |
| random | 1 | 0.770 | 0.755 | 0.015 | - | - | 0.964 | 0.966 | 0.255 | 1.15x | 15.1/20.1/22.9% | 1.7/5.0% | 3 |

> role-placement=degree: decode_failures 2

### `AD-flooding` - role-mix  `--scenario rolling`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.695 | 0.659 | 0.035 | - | - | 0.918 | 0.939 | 0.205 | 1.04x | 14.9/20.4/24.0% | 1.8/4.6% | 3 |
| all-routers | 1 | 0.913 | 0.909 | 0.003 | - | - | 0.994 | 0.995 | 0.751 | 2.73x | 31.7/43.9/46.9% | 4.5/5.4% | 3 |

> role-mix=baymesh-2026-08: decode_failures 2

### `AD-nomute` - role-mix  `--scenario rolling`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.695 | 0.659 | 0.035 | - | - | 0.918 | 0.939 | 0.205 | 1.04x | 14.9/20.4/24.0% | 1.8/4.6% | 3 |
| no-mute | 1 | 0.824 | 0.812 | 0.012 | - | - | 0.996 | 0.997 | 0.427 | 1.27x | 15.9/20.6/23.1% | 2.1/5.0% | 3 |
| all-routers | 1 | 0.913 | 0.909 | 0.003 | - | - | 0.994 | 0.995 | 0.751 | 2.73x | 31.7/43.9/46.9% | 4.5/5.4% | 3 |

> role-mix=baymesh-2026-08: decode_failures 2

### `AD-siting` - siting-mix  `--scenario rolling`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.695 | 0.659 | 0.035 | - | - | 0.918 | 0.939 | 0.205 | 1.04x | 14.9/20.4/24.0% | 1.8/4.6% | 3 |
| local-typical | 1 | 0.537 | 0.526 | 0.010 | - | - | 0.627 | 0.782 | 0.000 | 1.07x | 10.1/20.3/25.3% | 1.8/5.0% | 3 |
| basement-heavy | 1 | 0.029 | 0.029 | 0.000 | - | - | 0.039 | 0.116 | 0.000 | 0.31x | 0.6/3.0/7.0% | 0.2/1.8% | 3 |

> siting-mix=uniform: decode_failures 2

> siting-mix=local-typical: decode_failures 3

### `AD-worst` - role-placement  `--scenario rolling`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.821 | 0.812 | 0.009 | - | - | 0.942 | 0.943 | 0.000 | 2.46x | 16.0/25.7/34.3% | 1.9/5.6% | 3 |
| inverse | 1 | 0.771 | 0.754 | 0.016 | - | - | 0.928 | 0.929 | 0.000 | 2.29x | 13.6/22.0/30.2% | 1.9/3.3% | 3 |

### `BL-control` - protocol  `--scenario rolling`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.860 | 0.860 | 0.000 | - | - | 0 | 0.000 | 0.630 | 1.36x | 17.0/27.0/29.7% | 2.2/4.7% | 3 |
| sr | 1 | 0.872 | 0.849 | 0.023 | - | - | 0.980 | 0.987 | 0.625 | 1.44x | 18.0/28.0/30.8% | 2.4/5.0% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario rolling`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.784 | 0.770 | 0.014 | - | - | 0.931 | 0.950 | 0.572 | 3.07x | 38.0/63.2/65.5% | 4.8/9.9% | 3 |
| 100 | 1 | 0.889 | 0.884 | 0.005 | - | - | 0.987 | 0.988 | 0.668 | 1.61x | 20.2/37.3/38.9% | 2.5/5.3% | 3 |
| 120 | 1 | 0.889 | 0.884 | 0.005 | - | - | 0.987 | 0.988 | 0.668 | 1.61x | 20.2/37.3/38.9% | 2.5/5.3% | 3 |
| 250 | 1 | 0.889 | 0.884 | 0.005 | - | - | 0.987 | 0.988 | 0.668 | 1.61x | 20.2/37.3/38.9% | 2.5/5.3% | 3 |

> max-num-nodes=10: decode_failures 31

### `DB-hotstore-stress` - max-num-nodes  `--scenario rolling`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.319 | 0.315 | 0.004 | - | - | 0.461 | 0.465 | 0.088 | 11.03x | 38.3/59.2/68.0% | 3.8/10.5% | 3 |
| 120 | 1 | 0.502 | 0.498 | 0.004 | - | - | 0.623 | 0.623 | 0.116 | 4.45x | 15.8/26.5/31.4% | 1.5/4.8% | 3 |
| 250 | 1 | 0.508 | 0.504 | 0.004 | - | - | 0.631 | 0.631 | 0.115 | 4.32x | 15.3/25.9/30.4% | 1.5/4.7% | 3 |

> max-num-nodes=10: decode_failures 9

> faster: 9.43 s per simulated hour against 21.8 over 62 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `DB-platform` - platform-mix  `--scenario rolling`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.889 | 0.884 | 0.005 | - | - | 0.987 | 0.988 | 0.668 | 1.61x | 20.2/37.3/38.9% | 2.5/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.889 | 0.884 | 0.005 | - | - | 0.987 | 0.988 | 0.668 | 1.61x | 20.2/37.3/38.9% | 2.5/5.3% | 3 |
| constrained | 1 | 0.775 | 0.759 | 0.016 | - | - | 0.938 | 0.944 | 0.544 | 3.07x | 38.0/63.3/65.6% | 4.7/10.0% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario rolling`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.780 | 0.771 | 0.009 | - | - | 0.918 | 0.955 | 0.594 | 5.50x | 57.3/71.3/75.1% | 3.7/14.2% | 3 |
| 25 | 1 | 0.780 | 0.771 | 0.009 | - | - | 0.918 | 0.955 | 0.594 | 5.50x | 57.3/71.3/75.1% | 3.7/14.2% | 3 |
| 100 | 1 | 0.780 | 0.771 | 0.009 | - | - | 0.918 | 0.955 | 0.594 | 5.50x | 57.3/71.3/75.1% | 3.7/14.2% | 3 |
| 2000 | 1 | 0.780 | 0.771 | 0.009 | - | - | 0.918 | 0.955 | 0.594 | 5.50x | 57.3/71.3/75.1% | 3.7/14.2% | 3 |

> warm-num-nodes=0: queue drops 11.0% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 116

> warm-num-nodes=25: queue drops 11.0% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 116

> warm-num-nodes=100: queue drops 11.0% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 116

> warm-num-nodes=2000: queue drops 11.0% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 116

### `DG-burst` - burst-loss  `--scenario rolling`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 0.1 | 1 | 0.757 | 0.736 | 0.021 | - | - | 0.979 | 0.982 | 0.525 | 1.31x | 16.7/25.6/28.6% | 2.1/4.5% | 3 |
| 0.2 | 1 | 0.652 | 0.621 | 0.031 | - | - | 0.916 | 0.945 | 0.395 | 1.21x | 15.9/23.7/26.7% | 1.9/4.0% | 3 |
| 0.3 | 1 | 0.538 | 0.498 | 0.039 | - | - | 0.799 | 0.885 | 0.295 | 1.10x | 14.6/21.2/24.2% | 1.8/3.5% | 3 |

> burst-loss=0.2: decode_failures 36

> burst-loss=0.3: decode_failures 32

### `DG-loss` - extra-loss  `--scenario rolling`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 0.1 | 1 | 0.821 | 0.809 | 0.011 | - | - | 0.973 | 0.973 | 0.534 | 1.43x | 18.1/27.4/30.4% | 2.3/4.7% | 3 |
| 0.2 | 1 | 0.777 | 0.759 | 0.017 | - | - | 0.960 | 0.966 | 0.468 | 1.47x | 18.9/27.9/30.9% | 2.4/4.7% | 3 |
| 0.3 | 1 | 0.712 | 0.691 | 0.021 | - | - | 0.930 | 0.942 | 0.375 | 1.46x | 19.4/28.1/30.9% | 2.4/4.5% | 3 |

> faster: 1.1 s per simulated hour against 2.28 over 62 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `DG-outage` - burst-loss  `--scenario rolling`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 0.1 | 1 | 0.758 | 0.744 | 0.013 | - | - | 0.951 | 0.978 | 0.497 | 1.30x | 16.5/24.9/27.8% | 2.1/4.5% | 3 |
| 0.2 | 1 | 0.629 | 0.608 | 0.020 | - | - | 0.788 | 0.921 | 0.333 | 1.22x | 15.9/24.4/27.2% | 2.0/4.3% | 3 |
| 0.3 | 1 | 0.520 | 0.497 | 0.024 | - | - | 0.725 | 0.870 | 0.306 | 1.11x | 14.5/20.9/23.8% | 1.9/3.5% | 3 |

> burst-loss=0.1: decode_failures 27

> burst-loss=0.2: decode_failures 33

> burst-loss=0.3: decode_failures 23

### `DM-mode` - dm-mode  `--scenario rolling`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.814 | 0.814 | 0.000 | - | - | 0.964 | 0.979 | 0.577 | 1.79x | 22.4/34.9/38.4% | 2.9/6.1% | 3 |
| directed-with-late-flood | 1 | 0.820 | 0.820 | 0.000 | - | - | 0.966 | 0.980 | 0.579 | 1.66x | 21.0/32.9/36.3% | 2.7/5.8% | 3 |
| m4-early-flood | 1 | 0.822 | 0.822 | 0.000 | - | - | 0.967 | 0.981 | 0.579 | 1.65x | 20.7/32.4/35.7% | 2.7/5.7% | 3 |

> dm-mode=flood-only: decode_failures 15

> dm-mode=m4-early-flood: decode_failures 39

> slower: 8.06 s per simulated hour against 3.12 over 62 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-firmware` - profile  `--scenario rolling`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.862 | 0.852 | 0.009 | - | - | 0.989 | 0.991 | 0.558 | 0.77x | 8.6/11.4/12.1% | 1.2/2.0% | 3 |
| 2.8 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario rolling`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 0.25 | 1 | 0.815 | 0.804 | 0.011 | - | - | 0.962 | 0.962 | 0.546 | 1.18x | 14.5/20.6/23.0% | 1.9/4.3% | 3 |
| 0.5 | 1 | 0.886 | 0.878 | 0.008 | - | - | 0.996 | 0.997 | 0.521 | 1.06x | 13.2/17.7/20.9% | 1.7/4.1% | 3 |
| 0.75 | 1 | 0.866 | 0.856 | 0.009 | - | - | 0.987 | 0.987 | 0.601 | 0.88x | 10.8/14.8/16.7% | 1.5/3.5% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario rolling`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 0.25 | 1 | 0.820 | 0.810 | 0.009 | - | - | 0.967 | 0.970 | 0.571 | 1.21x | 14.9/21.4/24.0% | 2.0/4.5% | 3 |
| 0.5 | 1 | 0.880 | 0.873 | 0.007 | - | - | 0.989 | 0.989 | 0.530 | 1.03x | 12.9/17.4/20.2% | 1.6/4.0% | 3 |
| 0.75 | 1 | 0.873 | 0.865 | 0.009 | - | - | 0.990 | 0.991 | 0.599 | 0.84x | 10.3/14.5/16.4% | 1.4/3.4% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario rolling`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.900 | 0.896 | 0.004 | - | - | 0.995 | 0.996 | 0.683 | 0.76x | 9.9/15.8/17.6% | 1.2/2.8% | 3 |
| signing=true | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |

### `FW-versions` - profile  `--scenario rolling`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.863 | 0.855 | 0.008 | - | - | 0.987 | 0.991 | 0.590 | 0.74x | 8.9/11.8/12.5% | 1.2/2.6% | 3 |
| 2.5 | 1 | 0.857 | 0.848 | 0.008 | - | - | 0.988 | 0.989 | 0.574 | 0.75x | 8.9/11.8/12.5% | 1.2/2.6% | 3 |
| 2.6 | 1 | 0.857 | 0.849 | 0.008 | - | - | 0.989 | 0.989 | 0.570 | 0.72x | 8.8/11.6/12.6% | 1.2/2.6% | 3 |
| 2.7 | 1 | 0.876 | 0.867 | 0.009 | - | - | 0.987 | 0.988 | 0.598 | 0.75x | 9.1/13.0/14.6% | 1.1/3.0% | 3 |
| 2.8 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.888 | 0.884 | 0.005 | - | - | 0.995 | 0.995 | 0.649 | 0.94x | 11.7/18.7/20.8% | 1.5/3.3% | 3 |
| 900 | 1 | 0.808 | 0.794 | 0.014 | - | - | 0.972 | 0.973 | 0.555 | 2.19x | 27.3/42.0/46.0% | 3.6/7.4% | 3 |
| 300 | 1 | 0.559 | 0.533 | 0.026 | - | - | 0.779 | 0.882 | 0.381 | 4.64x | 54.7/74.9/78.5% | 7.2/13.7% | 3 |

> broadcast-interval-s=300: decode_failures 23

### `LD-chatty-hops` - broadcast-interval-s  `--scenario rolling`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.928 | 0.926 | 0.002 | - | - | 0.991 | 0.991 | 0.687 | 1.06x | 13.3/19.8/21.6% | 1.7/3.5% | 3 |
| 900 | 1 | 0.862 | 0.854 | 0.009 | - | - | 0.973 | 0.975 | 0.632 | 2.48x | 31.1/44.0/47.8% | 4.1/7.6% | 3 |
| 300 | 1 | 0.569 | 0.547 | 0.021 | - | - | 0.759 | 0.795 | 0.357 | 4.95x | 58.0/75.6/79.0% | 7.6/13.7% | 3 |

> broadcast-interval-s=300: decode_failures 23

### `LD-diurnal` - diurnal  `--scenario rolling`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.874 | 0.867 | 0.006 | - | - | 0.994 | 0.995 | 0.608 | 1.32x | 16.5/26.1/28.9% | 2.1/4.6% | 3 |
| sinusoid | 1 | 0.865 | 0.858 | 0.007 | - | - | 0.989 | 0.993 | 0.600 | 1.27x | 15.8/25.6/28.1% | 2.0/4.5% | 3 |
| commuter | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.808 | 0.794 | 0.014 | - | - | 0.972 | 0.973 | 0.555 | 2.19x | 27.3/42.0/46.0% | 3.6/7.4% | 3 |
| 3600 | 1 | 0.888 | 0.884 | 0.005 | - | - | 0.995 | 0.995 | 0.649 | 0.94x | 11.7/18.7/20.8% | 1.5/3.3% | 3 |
| 10800 | 1 | 0.905 | 0.901 | 0.004 | - | - | 0.998 | 0.998 | 0.659 | 0.62x | 7.7/12.3/13.6% | 1.0/2.2% | 3 |
| 43200 | 1 | 0.901 | 0.898 | 0.003 | - | - | 0.995 | 0.996 | 0.635 | 0.45x | 5.6/8.9/9.9% | 0.7/1.6% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario rolling`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 0.25 | 1 | 0.847 | 0.836 | 0.011 | - | - | 0.985 | 0.987 | 0.603 | 1.44x | 18.1/28.6/31.4% | 2.3/5.0% | 3 |
| 1.0 | 1 | 0.840 | 0.829 | 0.011 | - | - | 0.981 | 0.983 | 0.593 | 1.59x | 20.2/31.3/34.5% | 2.6/5.5% | 3 |
| 4.0 | 1 | 0.813 | 0.798 | 0.015 | - | - | 0.978 | 0.981 | 0.573 | 2.00x | 25.4/38.4/42.8% | 3.2/6.8% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario rolling`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.780 | 0.771 | 0.009 | - | - | 0.918 | 0.955 | 0.594 | 5.50x | 57.3/71.3/75.1% | 3.7/14.2% | 3 |
| 1.0 | 1 | 0.686 | 0.679 | 0.007 | - | - | 0.835 | 0.908 | 0.502 | 6.22x | 63.2/74.5/77.6% | 4.2/16.0% | 3 |

> traceroute-per-hour=0.0: queue drops 11.0% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 116

> traceroute-per-hour=1.0: queue drops 22.8% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 74

### `MS-density` - nodes  `--scenario rolling`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.683 | 0.656 | 0.028 | - | - | 0.872 | 0.900 | 0.384 | 1.36x | 16.6/23.3/28.0% | 3.4/5.8% | 3 |
| 60 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 90 | 1 | 0.948 | 0.947 | 0.002 | - | - | 0.998 | 0.998 | 0.756 | 1.53x | 18.2/26.2/29.3% | 1.4/5.1% | 3 |
| 120 | 1 | 0.965 | 0.963 | 0.002 | - | - | 0.999 | 0.999 | 0.850 | 1.90x | 21.9/29.9/33.5% | 1.2/5.1% | 3 |
| 150 | 1 | 0.972 | 0.971 | 0.001 | - | - | 0.999 | 0.999 | 0.872 | 2.50x | 27.5/38.6/44.1% | 1.3/5.6% | 3 |

> nodes=150: misdecodes 2

### `MS-hopscale` - nodes  `--scenario rolling`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 120 | 1 | 0.767 | 0.757 | 0.010 | - | - | 0.966 | 0.967 | 0.474 | 2.17x | 16.1/21.6/27.9% | 1.6/4.7% | 3 |
| 250 | 1 | 0.489 | 0.485 | 0.004 | - | - | 0.611 | 0.611 | 0.103 | 4.78x | 16.9/28.6/33.8% | 1.6/5.2% | 3 |
| 500 | 1 | 0.319 | 0.314 | 0.005 | - | - | 0.560 | 0.577 | 0.063 | 10.53x | 18.8/31.2/51.3% | 1.8/7.0% | 3 |

> nodes=500: decode_failures 223

### `MS-oversubscribed` - nodes  `--scenario rolling`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.772 | 0.763 | 0.009 | - | - | 0.964 | 0.965 | 0.487 | 1.99x | 14.8/19.7/25.5% | 1.4/4.3% | 3 |
| 250 | 1 | 0.502 | 0.498 | 0.004 | - | - | 0.623 | 0.623 | 0.116 | 4.45x | 15.8/26.5/31.4% | 1.5/4.8% | 3 |
| 500 | 1 | 0.323 | 0.318 | 0.005 | - | - | 0.568 | 0.575 | 0.059 | 9.60x | 17.2/28.3/46.6% | 1.6/6.2% | 3 |

> nodes=500: decode_failures 87

### `MS-roles` - role-mix  `--scenario rolling`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.869 | 0.860 | 0.009 | - | - | 0.988 | 0.989 | 0.582 | 1.41x | 17.7/27.9/30.7% | 2.2/4.9% | 3 |
| baymesh-2026-08 | 1 | 0.695 | 0.659 | 0.035 | - | - | 0.918 | 0.939 | 0.205 | 1.04x | 14.9/20.4/24.0% | 1.8/4.6% | 3 |

> role-mix=baymesh-2026-08: decode_failures 2

### `MS-roles-fav` - role-mix  `--scenario rolling`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.874 | 0.866 | 0.008 | - | - | 0.989 | 0.989 | 0.579 | 1.42x | 17.9/27.8/30.6% | 2.3/4.9% | 3 |
| baymesh-2026-08 | 1 | 0.748 | 0.723 | 0.024 | - | - | 0.947 | 0.949 | 0.222 | 1.19x | 16.6/26.0/29.0% | 1.9/4.5% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario rolling`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 0.05 | 1 | 0.866 | 0.858 | 0.008 | - | - | 0.982 | 0.982 | 0.627 | 1.49x | 18.4/32.4/34.6% | 2.3/5.1% | 3 |
| 0.1 | 1 | 0.868 | 0.861 | 0.007 | - | - | 0.985 | 0.987 | 0.610 | 1.61x | 21.0/36.5/38.4% | 2.4/5.1% | 3 |
| 0.2 | 1 | 0.869 | 0.863 | 0.007 | - | - | 0.982 | 0.982 | 0.625 | 1.81x | 22.9/40.5/43.4% | 2.7/5.2% | 3 |

### `MS-siting` - siting-mix  `--scenario rolling`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| local-typical | 1 | 0.579 | 0.565 | 0.014 | - | - | 0.684 | 0.763 | 0.000 | 1.40x | 11.8/21.6/28.3% | 2.3/5.0% | 3 |
| event | 1 | 0.134 | 0.134 | 0.000 | - | - | 0.100 | 0.300 | 0.000 | 1.07x | 3.8/18.4/26.3% | 1.3/4.5% | 3 |
| backbone | 1 | 0.975 | 0.974 | 0.000 | - | - | 0.999 | 0.999 | 0.865 | 1.05x | 25.3/29.0/30.8% | 1.2/5.6% | 3 |

> siting-mix=local-typical: decode_failures 22

### `MS-size` - nodes  `--scenario rolling`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.837 | 0.820 | 0.017 | - | - | 0.967 | 0.971 | 0.668 | 1.41x | 23.1/30.3/34.3% | 3.3/7.2% | 3 |
| 60 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 90 | 1 | 0.850 | 0.836 | 0.014 | - | - | 0.980 | 0.987 | 0.574 | 1.67x | 15.6/22.0/26.0% | 1.7/4.3% | 3 |
| 120 | 1 | 0.767 | 0.757 | 0.010 | - | - | 0.966 | 0.967 | 0.474 | 2.17x | 16.1/21.6/27.9% | 1.6/4.7% | 3 |
| 150 | 1 | 0.641 | 0.620 | 0.021 | - | - | 0.797 | 0.800 | 0.234 | 2.75x | 15.4/26.8/31.6% | 1.5/4.8% | 3 |

> nodes=150: decode_failures 3

### `MS-stretch` - stretch  `--scenario rolling`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 1.25 | 1 | 0.598 | 0.570 | 0.029 | - | - | 0.843 | 0.911 | 0.168 | 1.45x | 13.1/23.3/29.3% | 2.2/5.1% | 3 |
| 1.5 | 1 | 0.354 | 0.352 | 0.002 | - | - | 0.354 | 0.629 | 0.056 | 1.34x | 9.0/18.9/24.3% | 2.0/4.6% | 3 |
| 2.0 | 1 | 0.085 | 0.085 | 0.000 | - | - | 0.120 | 0.181 | 0.000 | 0.64x | 2.0/10.1/13.2% | 0.8/2.8% | 3 |

> stretch=1.25: decode_failures 19

> stretch=1.5: decode_failures 7

### `MS-topology` - topology  `--scenario rolling`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| clustered | 1 | 0.934 | 0.933 | 0.001 | - | - | 0.979 | 0.979 | 0.573 | 1.19x | 23.5/32.8/33.9% | 1.4/5.5% | 3 |
| corridor | 1 | 0.562 | 0.551 | 0.011 | - | - | 0.715 | 0.716 | 0.333 | 1.33x | 15.1/22.9/26.1% | 2.1/5.2% | 3 |
| hub | 1 | 0.935 | 0.935 | 0.000 | - | - | 0.972 | 0.973 | 0.809 | 1.22x | 27.3/35.8/37.2% | 1.6/5.5% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario rolling`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.820 | 0.820 | 0.000 | - | - | 0.966 | 0.980 | 0.579 | 1.66x | 21.0/32.9/36.3% | 2.7/5.8% | 3 |
| True | 1 | 0.825 | 0.825 | 0.000 | - | - | 0.974 | 0.986 | 0.599 | 1.66x | 20.8/32.5/35.8% | 2.7/5.8% | 3 |

> coding-rate-ladder=True: decode_failures 2

### `PR-dmmode-cr` - dm-mode  `--scenario rolling`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.825 | 0.825 | 0.000 | - | - | 0.974 | 0.986 | 0.599 | 1.66x | 20.8/32.5/35.8% | 2.7/5.8% | 3 |
| m4-early-flood | 1 | 0.828 | 0.828 | 0.000 | - | - | 0.967 | 0.985 | 0.599 | 1.66x | 21.0/32.7/36.1% | 2.7/5.8% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 2

> dm-mode=m4-early-flood: decode_failures 11

### `PR-protocol` - protocol  `--scenario rolling`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.860 | 0.860 | 0.000 | - | - | 0 | 0.000 | 0.630 | 1.36x | 17.0/27.0/29.7% | 2.2/4.7% | 3 |
| chain | 1 | 0.839 | 0.836 | 0.003 | - | - | 0.944 | 0.981 | 0.594 | 1.55x | 19.5/31.0/34.4% | 2.5/5.4% | 3 |
| sr | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |

### `PR-repeats` - extra-repeats  `--scenario rolling`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| True | 1 | 0.862 | 0.852 | 0.010 | - | - | 0.993 | 0.995 | 0.635 | 1.41x | 17.6/27.7/30.5% | 2.3/4.9% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario rolling`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.965 | 0.963 | 0.002 | - | - | 0.999 | 0.999 | 0.850 | 1.90x | 21.9/29.9/33.5% | 1.2/5.1% | 3 |
| True | 1 | 0.966 | 0.965 | 0.002 | - | - | 0.999 | 0.999 | 0.871 | 1.91x | 21.8/29.6/33.1% | 1.2/5.0% | 3 |

### `RF-bw500` - preset  `--scenario rolling`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.097 | 0.097 | 0.000 | - | - | 0.074 | 0.182 | 0.000 | 0.04x | 0.1/0.7/0.9% | 0.0/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.390 | 0.381 | 0.009 | - | - | 0.515 | 0.726 | 0.000 | 0.24x | 1.6/3.9/5.4% | 0.3/0.9% | 3 |
| LONG_TURBO | 1 | 0.760 | 0.744 | 0.015 | - | - | 0.963 | 0.971 | 0.435 | 1.34x | 12.7/23.9/27.1% | 2.2/4.5% | 3 |

> preset=SHORT_TURBO: decode_failures 1

> preset=MEDIUM_TURBO: decode_failures 12

### `RF-duct` - duct-per-hour  `--scenario rolling`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 0.25 | 1 | 0.872 | 0.861 | 0.011 | - | - | 0.991 | 0.992 | 0.658 | 1.31x | 19.0/28.5/31.0% | 2.0/4.9% | 3 |
| 1.0 | 1 | 0.927 | 0.922 | 0.006 | - | - | 0.994 | 0.994 | 0.779 | 1.05x | 23.7/30.3/32.3% | 1.6/5.0% | 3 |

### `RF-eu-presets` - preset  `--scenario rolling`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.251 | 0.248 | 0.003 | - | - | 0.401 | 0.406 | 0.000 | 0.13x | 0.7/2.1/2.7% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| LITE_FAST | 1 | 0.785 | 0.773 | 0.012 | - | - | 0.980 | 0.982 | 0.473 | 1.02x | 11.4/18.0/21.0% | 1.7/3.8% | 3 |
| NARROW_SLOW | 1 | 0.815 | 0.801 | 0.014 | - | - | 0.989 | 0.990 | 0.534 | 1.33x | 15.1/25.6/28.2% | 2.1/4.7% | 3 |

### `RF-noise` - noise-profile  `--scenario rolling`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| temporal | 1 | 0.749 | 0.730 | 0.019 | - | - | 0.961 | 0.966 | 0.469 | 1.39x | 17.3/26.1/29.6% | 2.2/4.7% | 3 |
| transient | 1 | 0.849 | 0.841 | 0.009 | - | - | 0.985 | 0.987 | 0.611 | 1.39x | 17.5/27.3/30.0% | 2.2/4.8% | 3 |
| periodic | 1 | 0.705 | 0.692 | 0.012 | - | - | 0.843 | 0.851 | 0.449 | 1.31x | 16.7/25.0/27.8% | 2.1/4.3% | 3 |

### `RF-preset` - preset  `--scenario rolling`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.251 | 0.248 | 0.003 | - | - | 0.401 | 0.406 | 0.000 | 0.13x | 0.7/2.1/2.7% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| LONG_MODERATE | 1 | 0.814 | 0.801 | 0.014 | - | - | 0.962 | 0.962 | 0.669 | 3.39x | 47.5/60.4/63.3% | 5.3/12.4% | 3 |

> preset=LONG_MODERATE: decode_failures 5

### `RF-preset-turbo` - preset  `--scenario rolling`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.054 | 0.054 | 0.000 | - | - | 0.166 | 0.167 | 0.000 | 0.01x | 0.0/0.1/0.2% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.097 | 0.097 | 0.000 | - | - | 0.074 | 0.182 | 0.000 | 0.04x | 0.1/0.7/0.9% | 0.0/0.2% | 3 |
| LONG_FAST | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| LONG_TURBO | 1 | 0.760 | 0.744 | 0.015 | - | - | 0.963 | 0.971 | 0.435 | 1.34x | 12.7/23.9/27.1% | 2.2/4.5% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.825 | 0.809 | 0.016 | - | - | 0.971 | 0.973 | 0.576 | 1.90x | 21.5/35.4/38.1% | 3.0/6.3% | 3 |

> preset=SHORT_TURBO: decode_failures 1

### `RF-pulse` - noise-pulse-interval-ms  `--scenario rolling`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.809 | 0.801 | 0.009 | - | - | 0.946 | 0.950 | 0.563 | 1.39x | 17.6/27.4/30.3% | 2.2/4.7% | 3 |
| 10000 | 1 | 0.705 | 0.692 | 0.012 | - | - | 0.843 | 0.851 | 0.449 | 1.31x | 16.7/25.0/27.8% | 2.1/4.3% | 3 |
| 4000 | 1 | 0.413 | 0.409 | 0.004 | - | - | 0.522 | 0.583 | 0.208 | 1.06x | 14.0/20.0/22.5% | 1.8/3.2% | 3 |
| 2000 | 1 | 0.110 | 0.110 | 0.000 | - | - | 0.141 | 0.221 | 0.061 | 0.72x | 9.6/13.8/15.7% | 1.2/1.9% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 6

### `RF-stretch-duct` - duct-per-hour  `--scenario rolling`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.354 | 0.352 | 0.002 | - | - | 0.354 | 0.629 | 0.056 | 1.34x | 9.0/18.9/24.3% | 2.0/4.6% | 3 |
| 1.0 | 1 | 0.685 | 0.641 | 0.044 | - | - | 0.771 | 0.819 | 0.455 | 1.05x | 13.8/21.7/24.4% | 1.4/4.3% | 3 |

> duct-per-hour=0.0: decode_failures 7

> duct-per-hour=1.0: decode_failures 25

> slower: 6.16 s per simulated hour against 1.83 over 62 prior run(s) - 3.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-txpower` - tx-power  `--scenario rolling`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 22 | 1 | 0.340 | 0.334 | 0.006 | - | - | 0.439 | 0.670 | 0.000 | 1.35x | 8.8/21.1/27.6% | 2.0/4.7% | 3 |
| 17 | 1 | 0.106 | 0.106 | 0.000 | - | - | 0.072 | 0.183 | 0.000 | 0.84x | 2.7/15.0/17.5% | 1.0/3.4% | 3 |
| 14 | 1 | 0.065 | 0.064 | 0.001 | - | - | 0.164 | 0.164 | 0.000 | 0.61x | 1.4/8.5/13.2% | 0.8/2.9% | 3 |

> tx-power=22: decode_failures 10

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario rolling`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.965 | 0.963 | 0.002 | - | - | 0.999 | 0.999 | 0.850 | 1.90x | 21.9/29.9/33.5% | 1.2/5.1% | 3 |
| True | 1 | 0.955 | 0.953 | 0.002 | - | - | 0.996 | 0.996 | 0.831 | 2.28x | 25.7/34.2/37.7% | 1.5/5.8% | 3 |

### `RT-favourites` - favourite-routers  `--scenario rolling`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.858 | 0.850 | 0.008 | - | - | 0.989 | 0.990 | 0.621 | 1.47x | 18.0/31.8/33.8% | 2.2/5.2% | 3 |
| True | 1 | 0.867 | 0.859 | 0.009 | - | - | 0.989 | 0.990 | 0.633 | 1.48x | 18.4/31.5/33.6% | 2.3/5.2% | 3 |

### `RT-hopassign` - hop-assign  `--scenario rolling`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| random | 1 | 0.856 | 0.845 | 0.011 | - | - | 0.988 | 0.988 | 0.606 | 1.38x | 17.7/26.5/29.2% | 2.2/4.7% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario rolling`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.672 | 0.631 | 0.041 | - | - | 0.969 | 0.974 | 0.326 | 1.03x | 13.2/21.2/23.7% | 1.6/4.0% | 3 |
| 7 | 1 | 0.909 | 0.905 | 0.004 | - | - | 0.990 | 0.990 | 0.664 | 1.56x | 19.7/28.6/31.3% | 2.5/5.0% | 3 |
| 15 | 1 | 0.935 | 0.933 | 0.002 | - | - | 0.982 | 0.982 | 0.722 | 1.60x | 20.3/29.6/32.2% | 2.6/5.1% | 3 |
| 32 | 1 | 0.937 | 0.935 | 0.002 | - | - | 0.984 | 0.984 | 0.743 | 1.59x | 20.2/29.6/32.2% | 2.6/5.1% | 3 |

> hop-limit=3: decode_failures 1

### `RT-hopspread` - hop-limit  `--scenario rolling`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.672 | 0.631 | 0.041 | - | - | 0.969 | 0.974 | 0.326 | 1.03x | 13.2/21.2/23.7% | 1.6/4.0% | 3 |
| 5 | 1 | 0.844 | 0.832 | 0.011 | - | - | 0.982 | 0.983 | 0.575 | 1.40x | 17.9/26.8/29.4% | 2.3/4.8% | 3 |
| 7 | 1 | 0.909 | 0.905 | 0.004 | - | - | 0.990 | 0.990 | 0.664 | 1.56x | 19.7/28.6/31.3% | 2.5/5.0% | 3 |

> hop-limit=3: decode_failures 1

### `RT-rebroadcast` - rebroadcast-mode  `--scenario rolling`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| KNOWN_ONLY | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.851 | 0.851 | 0.000 | - | - | 0.937 | 0.991 | 0.625 | 1.37x | 17.3/27.0/29.7% | 2.2/4.7% | 3 |

### `RT-spread` - hop-spread  `--scenario rolling`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.672 | 0.631 | 0.041 | - | - | 0.969 | 0.974 | 0.326 | 1.03x | 13.2/21.2/23.7% | 1.6/4.0% | 3 |
| True | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |

> hop-spread=False: decode_failures 1

### `SC-signing` - signature-policy  `--scenario rolling`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| BALANCED | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| STRICT | 1 | 0.706 | 0.706 | 0.000 | - | - | 0.872 | 0.873 | 0.443 | 1.51x | 19.1/29.5/32.6% | 2.4/5.1% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario rolling`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| dm | 1 | 0.858 | 0.847 | 0.011 | - | - | 0.985 | 0.986 | 0.607 | 1.39x | 17.4/27.6/30.6% | 2.2/4.9% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario rolling`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.856 | 0.846 | 0.010 | - | - | 0.986 | 0.987 | 0.620 | 1.41x | 17.7/27.8/30.6% | 2.3/4.9% | 3 |
| local | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| time | 1 | 0.853 | 0.842 | 0.011 | - | - | 0.989 | 0.989 | 0.625 | 1.41x | 17.7/27.6/30.5% | 2.3/4.9% | 3 |
| window | 1 | 0.856 | 0.846 | 0.010 | - | - | 0.983 | 0.985 | 0.602 | 1.37x | 17.2/27.3/30.0% | 2.2/4.8% | 3 |

> bucket-mode=global: misdecodes 32

> bucket-mode=time: misdecodes 24

> bucket-mode=window: misdecodes 31

### `SF-bucket-time` - time-bucket-s  `--scenario rolling`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.842 | 0.832 | 0.010 | - | - | 0.981 | 0.983 | 0.618 | 1.53x | 19.1/29.6/32.8% | 2.5/5.3% | 3 |
| 1800 | 1 | 0.853 | 0.842 | 0.011 | - | - | 0.989 | 0.989 | 0.625 | 1.41x | 17.7/27.6/30.5% | 2.3/4.9% | 3 |
| 3600 | 1 | 0.852 | 0.841 | 0.011 | - | - | 0.985 | 0.987 | 0.604 | 1.39x | 17.4/27.5/30.3% | 2.2/4.8% | 3 |

> time-bucket-s=600: misdecodes 99

> time-bucket-s=1800: misdecodes 24

> time-bucket-s=3600: misdecodes 9

### `SF-cadence` - trigger  `--scenario rolling`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| interval | 1 | 0.833 | 0.819 | 0.013 | - | - | 0.979 | 0.982 | 0.601 | 1.75x | 22.6/34.4/38.7% | 2.8/6.5% | 3 |
| aimd | 1 | 0.849 | 0.847 | 0.002 | - | - | 0.950 | 0.989 | 0.623 | 1.40x | 17.6/27.5/30.4% | 2.3/4.9% | 3 |
| bucket+interval | 1 | 0.833 | 0.821 | 0.013 | - | - | 0.980 | 0.982 | 0.594 | 1.78x | 23.1/34.9/39.1% | 2.9/6.6% | 3 |

> trigger=interval: misdecodes 18

> trigger=aimd: misdecodes 4

> trigger=bucket+interval: misdecodes 15

### `SF-capacity` - capacity  `--scenario rolling`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.857 | 0.847 | 0.011 | - | - | 0.986 | 0.991 | 0.622 | 1.40x | 17.5/27.8/30.7% | 2.2/4.9% | 3 |
| 8 | 1 | 0.852 | 0.842 | 0.011 | - | - | 0.982 | 0.984 | 0.604 | 1.39x | 17.4/27.6/30.5% | 2.2/4.9% | 3 |
| 16 | 1 | 0.860 | 0.851 | 0.009 | - | - | 0.989 | 0.990 | 0.617 | 1.39x | 17.5/27.4/30.2% | 2.2/4.8% | 3 |
| 32 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 50 | 1 | 0.857 | 0.847 | 0.010 | - | - | 0.984 | 0.985 | 0.615 | 1.41x | 17.6/27.8/30.6% | 2.2/4.9% | 3 |

> capacity=4: decode_failures 77

> capacity=8: decode_failures 28

### `SF-capacity-local` - capacity  `--scenario rolling`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.857 | 0.847 | 0.011 | - | - | 0.986 | 0.991 | 0.622 | 1.40x | 17.5/27.8/30.7% | 2.2/4.9% | 3 |
| 8 | 1 | 0.852 | 0.842 | 0.011 | - | - | 0.982 | 0.984 | 0.604 | 1.39x | 17.4/27.6/30.5% | 2.2/4.9% | 3 |
| 16 | 1 | 0.860 | 0.851 | 0.009 | - | - | 0.989 | 0.990 | 0.617 | 1.39x | 17.5/27.4/30.2% | 2.2/4.8% | 3 |
| 32 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 50 | 1 | 0.857 | 0.847 | 0.010 | - | - | 0.984 | 0.985 | 0.615 | 1.41x | 17.6/27.8/30.6% | 2.2/4.9% | 3 |

> capacity=4: decode_failures 77

> capacity=8: decode_failures 28

### `SF-capacity-window` - capacity  `--scenario rolling`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.861 | 0.852 | 0.009 | - | - | 0.982 | 0.988 | 0.615 | 1.38x | 17.2/27.5/30.4% | 2.2/4.8% | 3 |
| 16 | 1 | 0.854 | 0.844 | 0.009 | - | - | 0.983 | 0.984 | 0.588 | 1.38x | 17.3/27.3/30.1% | 2.2/4.8% | 3 |
| 32 | 1 | 0.856 | 0.846 | 0.010 | - | - | 0.983 | 0.985 | 0.602 | 1.37x | 17.2/27.3/30.0% | 2.2/4.8% | 3 |

> capacity=8: misdecodes 35

> capacity=8: decode_failures 16

> capacity=16: misdecodes 25

> capacity=32: misdecodes 31

### `SF-catchup` - catch-up-hours  `--scenario rolling`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.833 | 0.821 | 0.013 | - | - | 0.980 | 0.982 | 0.594 | 1.78x | 23.1/34.9/39.1% | 2.9/6.6% | 3 |
| 02-06 | 1 | 0.849 | 0.843 | 0.005 | - | - | 0.958 | 0.985 | 0.619 | 1.42x | 17.7/27.9/30.8% | 2.3/5.0% | 3 |
| 00-08 | 1 | 0.850 | 0.844 | 0.005 | - | - | 0.964 | 0.984 | 0.637 | 1.46x | 18.2/28.8/32.0% | 2.3/5.3% | 3 |

> catch-up-hours=: misdecodes 15

> catch-up-hours=02-06: decode_failures 24

> catch-up-hours=00-08: decode_failures 24

### `SF-hops-flat` - hops-apart  `--scenario rolling`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.857 | 0.854 | 0.003 | - | - | 0.914 | 0.914 | 0.627 | 1.39x | 17.5/27.9/30.5% | 2.3/4.9% | 3 |
| 2 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 3 | 1 | 0.872 | 0.849 | 0.023 | - | - | 0.980 | 0.987 | 0.625 | 1.44x | 18.0/28.0/30.8% | 2.4/5.0% | 3 |
| 4 | 1 | 0.868 | 0.847 | 0.021 | - | - | 0.853 | 0.990 | 0.615 | 1.41x | 17.7/27.7/30.3% | 2.3/4.9% | 3 |

> hops-apart=4: decode_failures 43

### `SF-hops-spread` - hops-apart  `--scenario rolling`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.857 | 0.854 | 0.003 | - | - | 0.914 | 0.914 | 0.627 | 1.39x | 17.5/27.9/30.5% | 2.3/4.9% | 3 |
| 2 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 3 | 1 | 0.872 | 0.849 | 0.023 | - | - | 0.980 | 0.987 | 0.625 | 1.44x | 18.0/28.0/30.8% | 2.4/5.0% | 3 |
| 4 | 1 | 0.868 | 0.847 | 0.021 | - | - | 0.853 | 0.990 | 0.615 | 1.41x | 17.7/27.7/30.3% | 2.3/4.9% | 3 |
| 5 | 1 | 0.872 | 0.850 | 0.022 | - | - | 0.887 | 0.996 | 0.617 | 1.44x | 17.9/28.2/30.9% | 2.3/5.0% | 3 |

> hops-apart=4: decode_failures 43

> hops-apart=5: decode_failures 24

### `SF-jitter-global` - advert-jitter-s  `--scenario rolling`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.863 | 0.853 | 0.010 | - | - | 0.992 | 0.993 | 0.625 | 1.39x | 17.3/27.2/30.0% | 2.2/4.8% | 3 |
| 30 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 120 | 1 | 0.855 | 0.847 | 0.009 | - | - | 0.985 | 0.987 | 0.631 | 1.40x | 17.5/27.6/30.4% | 2.2/4.9% | 3 |
| 600 | 1 | 0.851 | 0.841 | 0.010 | - | - | 0.984 | 0.985 | 0.604 | 1.40x | 17.6/27.8/30.6% | 2.2/4.9% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario rolling`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.863 | 0.853 | 0.010 | - | - | 0.992 | 0.993 | 0.625 | 1.39x | 17.3/27.2/30.0% | 2.2/4.8% | 3 |
| 30 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 120 | 1 | 0.855 | 0.847 | 0.009 | - | - | 0.985 | 0.987 | 0.631 | 1.40x | 17.5/27.6/30.4% | 2.2/4.9% | 3 |
| 600 | 1 | 0.851 | 0.841 | 0.010 | - | - | 0.984 | 0.985 | 0.604 | 1.40x | 17.6/27.8/30.6% | 2.2/4.9% | 3 |

### `SF-place-flat` - place  `--scenario rolling`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.896 | 0.848 | 0.049 | - | - | 0.939 | 0.989 | 0.630 | 1.45x | 18.2/28.7/31.2% | 2.3/5.2% | 3 |
| routers | 1 | 0.854 | 0.849 | 0.005 | - | - | 0.915 | 0.915 | 0.614 | 1.40x | 17.5/28.1/30.7% | 2.2/5.0% | 3 |
| alternate-routers | 1 | 0.846 | 0.843 | 0.004 | - | - | 0.911 | 0.912 | 0.598 | 1.41x | 17.6/28.5/31.0% | 2.3/5.0% | 3 |
| beside-router | 1 | 0.851 | 0.849 | 0.003 | - | - | 0.914 | 0.915 | 0.613 | 1.41x | 17.6/28.0/30.5% | 2.3/4.9% | 3 |
| random-clients | 1 | 0.861 | 0.849 | 0.012 | - | - | 0.978 | 0.979 | 0.630 | 1.42x | 17.8/27.9/30.6% | 2.3/4.9% | 3 |
| hops-apart | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |

> place=spread: decode_failures 26

### `SF-place-spread` - place  `--scenario rolling`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.896 | 0.848 | 0.049 | - | - | 0.939 | 0.989 | 0.630 | 1.45x | 18.2/28.7/31.2% | 2.3/5.2% | 3 |
| routers | 1 | 0.854 | 0.849 | 0.005 | - | - | 0.915 | 0.915 | 0.614 | 1.40x | 17.5/28.1/30.7% | 2.2/5.0% | 3 |
| alternate-routers | 1 | 0.846 | 0.843 | 0.004 | - | - | 0.911 | 0.912 | 0.598 | 1.41x | 17.6/28.5/31.0% | 2.3/5.0% | 3 |
| beside-router | 1 | 0.851 | 0.849 | 0.003 | - | - | 0.914 | 0.915 | 0.613 | 1.41x | 17.6/28.0/30.5% | 2.3/4.9% | 3 |
| random-clients | 1 | 0.861 | 0.849 | 0.012 | - | - | 0.978 | 0.979 | 0.630 | 1.42x | 17.8/27.9/30.6% | 2.3/4.9% | 3 |
| hops-apart | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |

> place=spread: decode_failures 26

### `SF-provide-transport` - provide-transport  `--scenario rolling`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| broadcast | 1 | 0.877 | 0.841 | 0.037 | - | - | 0.978 | 0.982 | 0.626 | 1.44x | 18.1/28.2/31.0% | 2.3/4.9% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario rolling`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| heard | 1 | 0.857 | 0.846 | 0.011 | - | - | 0.987 | 0.990 | 0.616 | 1.39x | 17.4/27.5/30.1% | 2.2/4.8% | 3 |

> replay-ordering=heard: misdecodes 22

### `SF-replay-order-broadcast` - replay-ordering  `--scenario rolling`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.877 | 0.841 | 0.037 | - | - | 0.978 | 0.982 | 0.626 | 1.44x | 18.1/28.2/31.0% | 2.3/4.9% | 3 |
| heard | 1 | 0.883 | 0.835 | 0.048 | - | - | 0.980 | 0.985 | 0.622 | 1.46x | 18.3/28.4/31.3% | 2.4/5.0% | 3 |

> replay-ordering=heard: misdecodes 8

### `SF-resolve` - resolve  `--scenario rolling`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| enum | 1 | 0.852 | 0.842 | 0.010 | - | - | 0.978 | 0.984 | 0.625 | 1.38x | 17.3/27.4/30.3% | 2.2/4.9% | 3 |
| hybrid | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |

### `SF-servers-allrouters` - servers  `--scenario rolling`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.854 | 0.849 | 0.005 | - | - | 0.915 | 0.915 | 0.614 | 1.40x | 17.5/28.1/30.7% | 2.2/5.0% | 3 |
| 6 | 1 | 0.841 | 0.837 | 0.004 | - | - | 0.900 | 0.901 | 0.608 | 1.44x | 18.0/29.2/31.9% | 2.4/5.2% | 6 |

### `SF-servers-flat` - servers  `--scenario rolling`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.857 | 0.848 | 0.008 | - | - | 0.984 | 0.986 | 0.637 | 1.39x | 17.4/27.7/30.3% | 2.2/4.8% | 2 |
| 3 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 5 | 1 | 0.868 | 0.849 | 0.019 | - | - | 0.987 | 0.989 | 0.614 | 1.44x | 18.1/28.3/31.2% | 2.3/5.0% | 5 |
| 8 | 1 | 0.856 | 0.838 | 0.018 | - | - | 0.984 | 0.985 | 0.632 | 1.48x | 18.4/28.3/31.4% | 2.4/5.0% | 8 |

### `SF-servers-spread` - servers  `--scenario rolling`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.857 | 0.848 | 0.008 | - | - | 0.984 | 0.986 | 0.637 | 1.39x | 17.4/27.7/30.3% | 2.2/4.8% | 2 |
| 3 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 5 | 1 | 0.868 | 0.849 | 0.019 | - | - | 0.987 | 0.989 | 0.614 | 1.44x | 18.1/28.3/31.2% | 2.3/5.0% | 5 |
| 8 | 1 | 0.856 | 0.838 | 0.018 | - | - | 0.984 | 0.985 | 0.632 | 1.48x | 18.4/28.3/31.4% | 2.4/5.0% | 8 |

### `SF-signed` - signed  `--scenario rolling`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| True | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario rolling`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.862 | 0.851 | 0.011 | - | - | 0.986 | 0.987 | 0.614 | 1.31x | 16.5/26.0/28.6% | 2.1/4.5% | 3 |
| 1 | 1 | 0.855 | 0.846 | 0.009 | - | - | 0.989 | 0.990 | 0.608 | 1.31x | 16.4/25.8/28.4% | 2.1/4.6% | 3 |
| 2 | 1 | 0.866 | 0.859 | 0.007 | - | - | 0.989 | 0.992 | 0.635 | 1.33x | 16.5/26.3/29.0% | 2.1/4.7% | 3 |
| 4 | 1 | 0.866 | 0.859 | 0.007 | - | - | 0.989 | 0.992 | 0.635 | 1.33x | 16.5/26.3/29.0% | 2.1/4.7% | 3 |

### `SF-width` - short-id-bits  `--scenario rolling`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.857 | 0.848 | 0.009 | - | - | 0.989 | 0.990 | 0.635 | 1.40x | 17.6/27.6/30.4% | 2.2/4.8% | 3 |
| 24 | 1 | 0.860 | 0.852 | 0.008 | - | - | 0.988 | 0.989 | 0.630 | 1.39x | 17.5/27.3/30.1% | 2.2/4.8% | 3 |
| 32 | 1 | 0.865 | 0.856 | 0.009 | - | - | 0.995 | 0.996 | 0.630 | 1.40x | 17.6/27.6/30.4% | 2.2/4.9% | 3 |
| 64 | 1 | 0.859 | 0.851 | 0.008 | - | - | 0.990 | 0.992 | 0.626 | 1.39x | 17.4/27.6/30.4% | 2.2/4.8% | 3 |

### `SF-window-size` - window-size  `--scenario rolling`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.857 | 0.847 | 0.009 | - | - | 0.991 | 0.992 | 0.612 | 1.46x | 18.2/28.8/31.8% | 2.3/5.1% | 3 |
| 16 | 1 | 0.862 | 0.853 | 0.009 | - | - | 0.989 | 0.990 | 0.606 | 1.43x | 17.9/28.1/30.9% | 2.3/4.9% | 3 |
| 32 | 1 | 0.856 | 0.846 | 0.010 | - | - | 0.983 | 0.985 | 0.602 | 1.37x | 17.2/27.3/30.0% | 2.2/4.8% | 3 |

> window-size=8: misdecodes 130

> window-size=16: misdecodes 72

> window-size=32: misdecodes 31

### `TH-congestion` - no-congestion-scaling  `--scenario rolling`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.965 | 0.963 | 0.002 | - | - | 0.999 | 0.999 | 0.850 | 1.90x | 21.9/29.9/33.5% | 1.2/5.1% | 3 |
| True | 1 | 0.780 | 0.769 | 0.010 | - | - | 0.927 | 0.956 | 0.590 | 5.45x | 57.0/71.0/74.9% | 3.6/14.0% | 3 |

> no-congestion-scaling=True: decode_failures 89

### `TH-congestion-input` - congestion-input  `--scenario rolling`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.502 | 0.498 | 0.004 | - | - | 0.623 | 0.623 | 0.116 | 4.45x | 15.8/26.5/31.4% | 1.5/4.8% | 3 |
| truesize | 1 | 0.534 | 0.530 | 0.004 | - | - | 0.657 | 0.658 | 0.109 | 3.24x | 11.4/20.5/23.8% | 1.1/3.8% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario rolling`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.966 | 0.964 | 0.002 | - | - | 0.999 | 0.999 | 0.855 | 1.82x | 20.9/28.5/31.7% | 1.1/4.9% | 3 |
| adaptive | 1 | 0.965 | 0.963 | 0.002 | - | - | 0.999 | 0.999 | 0.850 | 1.90x | 21.9/29.9/33.5% | 1.2/5.1% | 3 |

