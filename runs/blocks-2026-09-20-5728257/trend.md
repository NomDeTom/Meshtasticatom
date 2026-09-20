# Sweep blocks-2026-09-20-5728257

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** coastal
- **seed base** 5728257 · seeds 5728257
- **blocks** 87 run
- **compute** 9.9 h of simulator time across every cell
- **generated** 2026-09-20T09:06:54+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>79 warnings</summary>

- AD-badrouters: role-placement=inverse: decode_failures 24
- AD-siting: siting-mix=basement-heavy: decode_failures 5
- AD-worst: role-placement=degree: decode_failures 95
- AD-worst: role-placement=inverse: decode_failures 87
- AD-worst: slower: 28.7 s per simulated hour against 3.48 over 30 prior run(s) - 8.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 13
- DB-warm: warm-num-nodes=0: queue drops 12.4% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 80
- DB-warm: warm-num-nodes=25: queue drops 12.4% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 80
- DB-warm: warm-num-nodes=100: queue drops 12.4% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 80
- DB-warm: warm-num-nodes=2000: queue drops 12.4% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 80
- DG-burst: burst-loss=0.2: decode_failures 21
- DG-burst: burst-loss=0.3: decode_failures 28
- DG-loss: extra-loss=0.3: decode_failures 3
- DG-outage: burst-loss=0.1: decode_failures 34
- DG-outage: burst-loss=0.2: decode_failures 40
- DG-outage: burst-loss=0.3: decode_failures 27
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 19
- LD-chatty: broadcast-interval-s=300: decode_failures 26
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 12.4% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 80
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 23.3% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 112
- MS-density: nodes=40: decode_failures 15
- MS-hopscale: nodes=120: decode_failures 4
- MS-hopscale: nodes=250: decode_failures 1
- MS-hopscale: nodes=500: decode_failures 6
- MS-oversubscribed: nodes=500: decode_failures 3
- MS-oversubscribed: faster: 9.65 s per simulated hour against 19.9 over 30 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-siting: siting-mix=event: 3 archives requested, 2 placed - group on the placed count
- MS-size: nodes=120: decode_failures 4
- MS-stretch: stretch=1.5: decode_failures 6
- MS-stretch: stretch=2.0: decode_failures 2
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 12
- RF-eu-presets: preset=SHORT_FAST: decode_failures 1
- RF-preset: preset=SHORT_FAST: decode_failures 1
- RF-preset: preset=LONG_MODERATE: misdecodes 1
- RF-preset: preset=LONG_MODERATE: decode_failures 9
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 4
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 6
- RF-stretch-duct: duct-per-hour=1.0: decode_failures 10
- RF-txpower: tx-power=22: decode_failures 11
- RF-txpower: tx-power=17: decode_failures 15
- RT-hoplimit: hop-limit=3: decode_failures 5
- RT-hopspread: hop-limit=3: decode_failures 5
- RT-spread: hop-spread=False: decode_failures 5
- SF-bucket-mode: bucket-mode=global: misdecodes 47
- SF-bucket-mode: bucket-mode=time: misdecodes 27
- SF-bucket-mode: bucket-mode=window: misdecodes 21
- SF-bucket-time: time-bucket-s=600: misdecodes 140
- SF-bucket-time: time-bucket-s=1800: misdecodes 27
- SF-bucket-time: time-bucket-s=3600: misdecodes 5
- SF-cadence: trigger=interval: misdecodes 15
- SF-cadence: trigger=aimd: misdecodes 4
- SF-cadence: trigger=bucket+interval: misdecodes 20
- SF-capacity-local: capacity=4: decode_failures 102
- SF-capacity-local: capacity=8: decode_failures 47
- SF-capacity: capacity=4: decode_failures 102
- SF-capacity: capacity=8: decode_failures 47
- SF-capacity-window: capacity=8: misdecodes 25
- SF-capacity-window: capacity=8: decode_failures 34
- SF-capacity-window: capacity=16: misdecodes 30
- SF-capacity-window: capacity=32: misdecodes 21
- SF-catchup: catch-up-hours=: misdecodes 20
- SF-catchup: catch-up-hours=02-06: decode_failures 38
- SF-catchup: catch-up-hours=00-08: decode_failures 38
- SF-hops-spread: faster: 1.92 s per simulated hour against 4.56 over 30 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-place-flat: place=spread: decode_failures 1
- SF-place-spread: place=spread: decode_failures 1
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 6
- SF-replay-order: replay-ordering=heard: misdecodes 10
- SF-window-size: window-size=8: misdecodes 172
- SF-window-size: window-size=16: misdecodes 75
- SF-window-size: window-size=32: misdecodes 21
- TH-congestion: no-congestion-scaling=True: queue drops 11.7% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 66

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `AD-worst` | 28.7 | 3.48 | 8.24x | 30 |
| `RF-stretch-duct` | 4.27 | 2.28 | 1.87x | 30 |
| `AD-badrouters` | 3.79 | 2.05 | 1.84x | 30 |
| `RF-txpower` | 2.84 | 1.6 | 1.78x | 30 |
| `MS-size` | 2.16 | 3.38 | 0.64x | 30 |
| `SF-place-flat` | 1.87 | 3.01 | 0.62x | 30 |
| `DB-hotstore-stress` | 13.5 | 22.7 | 0.59x | 30 |
| `SF-hops-flat` | 1.92 | 3.45 | 0.56x | 30 |
| `SF-place-spread` | 1.61 | 2.92 | 0.55x | 30 |
| `TH-congestion-input` | 5.92 | 10.8 | 0.55x | 30 |
| `SF-cadence` | 1.85 | 3.41 | 0.54x | 30 |
| `MS-hopscale` | 9.58 | 18.5 | 0.52x | 30 |
| `MS-oversubscribed` | 9.65 | 19.9 | 0.48x | 30 |
| `SF-hops-spread` | 1.92 | 4.57 | 0.42x | 30 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.985 | 0.985 | 0.887 → 0.908 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.982 | 0.982 | 0.896 → 0.908 | 1.1x bytes_on_air | up | 2 |
| `RF-txpower` | tx-power | **held** | 0.040 → 0.985 | 0.945 | 0.086 → 0.902 | 70x sr_bytes | down | 4 |
| `RF-preset-turbo` | preset | **held** | 0.043 → 0.985 | 0.943 | 0.052 → 0.902 | 43x sr_airtime | up | 5 |
| `MS-siting` | siting-mix | **held** | 0.135 → 1.000 | 0.865 | 0.190 → 0.978 | 35x sr_bytes | up | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.141 → 0.937 | 0.796 | 0.111 → 0.846 | 1.1e+02x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **text** | 0.043 → 0.832 | 0.789 | 0.042 → 0.824 | 5.5x advert_bytes | down | 3 |
| `MS-stretch` | stretch | **text** | 0.151 → 0.907 | 0.756 | 0.146 → 0.902 | 2.9x sr_airtime | down | 4 |
| `RF-bw500` | preset | **text** | 0.173 → 0.828 | 0.655 | 0.168 → 0.822 | 3.3x sr_bytes | up | 3 |
| `MS-hopscale` | nodes | **text** | 0.323 → 0.907 | 0.584 | 0.321 → 0.902 | 8.2x bytes_on_air | down | 4 |
| `RF-eu-presets` | preset | **text** | 0.338 → 0.907 | 0.570 | 0.325 → 0.902 | 1.6x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.338 → 0.907 | 0.570 | 0.325 → 0.902 | 2x sr_airtime | up | 3 |
| `MS-oversubscribed` | nodes | **held** | 0.495 → 0.974 | 0.478 | 0.325 → 0.740 | 5x bytes_on_air | down | 3 |
| `MS-density` | nodes | **held** | 0.545 → 0.999 | 0.454 | 0.683 → 0.967 | 7.7x sr_airtime | up | 5 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.625 → 0.954 | 0.329 | 0.608 → 0.953 | 7.9x sr_airtime | down | 3 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.603 → 0.931 | 0.328 | 0.582 → 0.927 | 7.5x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.584 → 0.907 | 0.323 | 0.557 → 0.902 | 2.3x sr_bytes | down | 4 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.433 → 0.748 | 0.315 | 0.417 → 0.698 | 1.7x sr_airtime | up | 2 |
| `DG-burst` | burst-loss | **text** | 0.599 → 0.907 | 0.308 | 0.563 → 0.902 | 2.3x sr_bytes | down | 4 |
| `MS-topology` | topology | **text** | 0.680 → 0.956 | 0.276 | 0.675 → 0.955 | 2.3x sr_bytes | up | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.390 → 0.635 | 0.245 | 0.322 → 0.512 | 5.8x sr_airtime | up | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.741 → 0.952 | 0.210 | 0.707 → 0.950 | 2.4x sr_bytes | up | 4 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.760 → 0.964 | 0.204 | 0.750 → 0.963 | 4.5x sr_airtime | down | 2 |
| `RT-hopspread` | hop-limit | **text** | 0.741 → 0.941 | 0.200 | 0.707 → 0.938 | 2.2x sr_bytes | up | 3 |
| `MS-size` | nodes | **text** | 0.709 → 0.907 | 0.198 | 0.695 → 0.902 | 4.3x sr_bytes | down | 5 |
| `RF-noise` | noise-profile | **text** | 0.732 → 0.907 | 0.176 | 0.724 → 0.902 | 1.3x sr_bytes | down | 4 |
| `RT-spread` | hop-spread | **text** | 0.741 → 0.907 | 0.166 | 0.707 → 0.902 | 1.9x sr_bytes | up | 2 |
| `DG-loss` | extra-loss | **text** | 0.772 → 0.907 | 0.136 | 0.756 → 0.902 | 1.5x sr_bytes | down | 4 |
| `AD-flooding` | role-mix | **text** | 0.832 → 0.946 | 0.115 | 0.824 → 0.944 | 2.4x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.832 → 0.946 | 0.115 | 0.824 → 0.944 | 2.4x bytes_on_air | up | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.654 → 0.756 | 0.102 | 0.646 → 0.748 | 1.4x sr_airtime | down | 2 |
| `SC-signing` | signature-policy | **text** | 0.811 → 0.907 | 0.097 | 0.811 → 0.902 | 1.3x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.842 → 0.930 | 0.089 | 0.831 → 0.927 | 2.3x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.849 → 0.930 | 0.082 | 0.838 → 0.927 | 2.2x sr_airtime | down | 3 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.912 → 0.985 | 0.072 | 0.902 → 0.903 | 26x sr_airtime | down | 3 |
| `AD-badrouters` | role-placement | **text** | 0.768 → 0.832 | 0.063 | 0.753 → 0.824 | 1.6x sr_bytes | down | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.883 → 0.946 | 0.063 | 0.873 → 0.943 | 5.2x sr_airtime | up | 4 |
| `MS-roles` | role-mix | **text** | 0.832 → 0.891 | 0.060 | 0.824 → 0.885 | 1.1x bytes_on_air | down | 2 |
| `SF-cadence` | trigger | **held** | 0.926 → 0.985 | 0.059 | 0.882 → 0.902 | 13x advert_bytes | down | 4 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.907 → 0.965 | 0.058 | 0.902 → 0.964 | 1.9x sr_bytes | up | 3 |
| `MS-roles-fav` | role-mix | **held** | 0.925 → 0.972 | 0.047 | 0.859 → 0.897 | 1.1x sr_bytes | down | 2 |
| `RT-hopassign` | hop-assign | **text** | 0.864 → 0.907 | 0.043 | 0.857 → 0.902 | 1.1x sr_bytes | down | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.864 → 0.907 | 0.043 | 0.856 → 0.902 | 1.5x sr_airtime | down | 4 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.907 → 0.944 | 0.036 | 0.902 → 0.940 | 1.6x sr_bytes | up | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.907 → 0.942 | 0.035 | 0.902 → 0.936 | 1.3x bytes_on_air | up | 3 |
| `SF-catchup` | catch-up-hours | **held** | 0.949 → 0.976 | 0.027 | 0.882 → 0.902 | 9.2x advert_bytes | down | 3 |
| `TH-congestion-input` | congestion-input | **text** | 0.513 → 0.539 | 0.026 | 0.506 → 0.532 | 1.4x sr_airtime | up | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.907 → 0.933 | 0.026 | 0.902 → 0.930 | 3.3x bytes_on_air | down | 2 |
| `SF-place-flat` | place | **text** | 0.903 → 0.924 | 0.021 | 0.897 → 0.905 | 3.1x sr_bytes | down | 6 |
| `SF-place-spread` | place | **text** | 0.903 → 0.924 | 0.021 | 0.897 → 0.905 | 3.1x sr_bytes | down | 6 |
| `FW-mixed` | legacy-fraction | **text** | 0.886 → 0.907 | 0.021 | 0.866 → 0.902 | 2x bytes_on_air | down | 4 |
| `SF-hops-flat` | hops-apart | **text** | 0.901 → 0.919 | 0.019 | 0.896 → 0.902 | 1.9x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **text** | 0.901 → 0.919 | 0.019 | 0.896 → 0.902 | 2.1x sr_bytes | up | 5 |
| `RT-favourites` | favourite-routers | **text** | 0.908 → 0.924 | 0.016 | 0.904 → 0.919 | 1.1x bytes_on_air | up | 2 |
| `DM-mode` | dm-mode | **text** | 0.868 → 0.882 | 0.014 | 0.868 → 0.882 | 1.1x bytes_on_air | up | 3 |
| `MS-router-late` | router-late-fraction | **held** | 0.972 → 0.985 | 0.013 | 0.899 → 0.904 | 1.3x bytes_on_air | down | 4 |
| `LD-diurnal` | diurnal | **text** | 0.907 → 0.920 | 0.012 | 0.902 → 0.915 | 1.2x sr_bytes | down | 3 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.895 → 0.907 | 0.012 | 0.877 → 0.902 | 2.1x bytes_on_air | down | 4 |
| `AD-worst` | role-placement | **held** | 0.882 → 0.894 | 0.012 | 0.785 → 0.793 | 1x bytes_on_air | up | 2 |
| `FW-versions` | profile | **text** | 0.900 → 0.912 | 0.011 | 0.894 → 0.906 | 3.2x bytes_on_air | up | 5 |
| `SF-servers-flat` | servers | **held** | 0.979 → 0.989 | 0.010 | 0.886 → 0.902 | 6.7x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.979 → 0.989 | 0.010 | 0.886 → 0.902 | 6.7x sr_bytes | up | 4 |
| `SF-capacity-window` | capacity | **held** | 0.970 → 0.980 | 0.009 | 0.895 → 0.899 | 2x advert_bytes | up | 3 |
| `SF-provide-transport` | provide-transport | **text** | 0.907 → 0.916 | 0.009 | 0.889 → 0.902 | 2.9x sr_airtime | up | 2 |
| `SF-window-size` | window-size | **text** | 0.898 → 0.907 | 0.009 | 0.890 → 0.902 | 6x advert_bytes | up | 3 |
| `SF-sr-retries` | sr-retries | **text** | 0.894 → 0.903 | 0.008 | 0.889 → 0.898 | 1.1x sr_bytes | up | 4 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.900 → 0.908 | 0.008 | 0.895 → 0.903 | 1.1x sr_bytes | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.900 → 0.908 | 0.008 | 0.895 → 0.903 | 1.1x sr_bytes | up | 4 |
| `SF-resolve` | resolve | **held** | 0.977 → 0.985 | 0.007 | 0.901 → 0.902 | 5.7x advert_bytes | = | 3 |
| `SF-width` | short-id-bits | **text** | 0.900 → 0.907 | 0.007 | 0.896 → 0.902 | 3.1x advert_bytes | down | 4 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.897 → 0.903 | 0.007 | 0.891 → 0.899 | 5.3x advert_bytes | up | 3 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.901 → 0.907 | 0.006 | 0.895 → 0.902 | 3x advert_bytes | up | 4 |
| `SF-capacity` | capacity | **held** | 0.979 → 0.985 | 0.006 | 0.897 → 0.902 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.979 → 0.985 | 0.006 | 0.897 → 0.902 | 5.3x advert_bytes | up | 5 |
| `SF-replay-order` | replay-ordering | **held** | 0.979 → 0.985 | 0.006 | 0.899 → 0.902 | 1x sr_bytes | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.959 → 0.964 | 0.005 | 0.957 → 0.963 | 1.2x bytes_on_air | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.976 → 0.981 | 0.005 | 0.889 → 0.894 | 1.1x sr_airtime | up | 2 |
| `FW-firmware` | profile | **held** | 0.985 → 0.989 | 0.005 | 0.902 → 0.902 | 3.1x bytes_on_air | down | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.985 → 0.989 | 0.004 | 0.901 → 0.902 | 2.8x sr_airtime | up | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.974 → 0.978 | 0.004 | 0.882 → 0.882 | 1.1x sr_bytes | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.964 → 0.966 | 0.002 | 0.963 → 0.965 | 1.1x sr_airtime | down | 2 |
| `PR-repeats` | extra-repeats | **held** | 0.983 → 0.985 | 0.001 | 0.902 → 0.902 | 1x sr_airtime | down | 2 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.978 → 0.979 | 0.001 | 0.882 → 0.883 | 1.1x sr_airtime | up | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.984 → 0.985 | 0.001 | 0.899 → 0.905 | 2.7x sr_bytes | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.963 → 0.964 | 0.001 | 0.962 → 0.963 | 1.1x sr_bytes | down | 2 |

### Moved no delivery measure

Not the same as having done nothing: several arms hold delivery flat by design and differ in what they spend. Three ways of reconciling the same two sets had better agree on what is held; where they differ is the price.

| block | arm | price | cells |
| --- | --- | --- | --: |
| `DB-warm` | warm-num-nodes | - | 4 |
| `SF-signed` | signed | 1.4x advert_bytes | 2 |

## Every block

### `AD-amplifiers` - amplifier-mix  `--scenario coastal`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| sprinkled | 1 | 0.919 | 0.904 | 0.016 | - | - | 0.983 | 0.985 | 0.771 | 1.21x | 17.9/24.7/28.6% | 1.8/5.2% | 3 |
| arms-race | 1 | 0.965 | 0.964 | 0.001 | - | - | 0.989 | 0.989 | 0.897 | 0.88x | 22.5/25.9/28.3% | 0.8/5.4% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario coastal`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 0.1 | 1 | 0.928 | 0.920 | 0.008 | - | - | 0.991 | 0.993 | 0.841 | 1.17x | 18.6/23.3/27.5% | 1.8/5.1% | 3 |
| 0.3 | 1 | 0.944 | 0.940 | 0.003 | - | - | 0.987 | 0.987 | 0.876 | 1.01x | 22.1/27.7/31.1% | 1.3/4.8% | 3 |

### `AD-badrouters` - role-placement  `--scenario coastal`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.832 | 0.824 | 0.008 | - | - | 0.933 | 0.937 | 0.610 | 1.18x | 16.8/22.3/25.9% | 2.0/5.1% | 3 |
| inverse | 1 | 0.768 | 0.753 | 0.015 | - | - | 0.899 | 0.917 | 0.520 | 1.07x | 13.7/18.2/21.6% | 1.9/3.6% | 3 |
| random | 1 | 0.778 | 0.765 | 0.013 | - | - | 0.893 | 0.894 | 0.572 | 1.05x | 14.0/18.2/22.3% | 1.8/4.5% | 3 |

> role-placement=inverse: decode_failures 24

### `AD-flooding` - role-mix  `--scenario coastal`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.832 | 0.824 | 0.008 | - | - | 0.933 | 0.937 | 0.610 | 1.18x | 16.8/22.3/25.9% | 2.0/5.1% | 3 |
| all-routers | 1 | 0.946 | 0.944 | 0.002 | - | - | 0.997 | 0.998 | 0.854 | 2.77x | 32.5/39.4/45.4% | 4.5/5.3% | 3 |

### `AD-nomute` - role-mix  `--scenario coastal`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.832 | 0.824 | 0.008 | - | - | 0.933 | 0.937 | 0.610 | 1.18x | 16.8/22.3/25.9% | 2.0/5.1% | 3 |
| no-mute | 1 | 0.880 | 0.874 | 0.006 | - | - | 0.967 | 0.970 | 0.612 | 1.30x | 16.3/22.5/26.8% | 2.0/5.3% | 3 |
| all-routers | 1 | 0.946 | 0.944 | 0.002 | - | - | 0.997 | 0.998 | 0.854 | 2.77x | 32.5/39.4/45.4% | 4.5/5.3% | 3 |

### `AD-siting` - siting-mix  `--scenario coastal`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.832 | 0.824 | 0.008 | - | - | 0.933 | 0.937 | 0.610 | 1.18x | 16.8/22.3/25.9% | 2.0/5.1% | 3 |
| local-typical | 1 | 0.539 | 0.533 | 0.006 | - | - | 0.742 | 0.745 | 0.000 | 1.24x | 12.2/18.1/24.2% | 2.2/5.1% | 3 |
| basement-heavy | 1 | 0.043 | 0.042 | 0.001 | - | - | 0.183 | 0.204 | 0.000 | 0.35x | 0.4/3.3/7.6% | 0.2/2.2% | 3 |

> siting-mix=basement-heavy: decode_failures 5

### `AD-worst` - role-placement  `--scenario coastal`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.800 | 0.793 | 0.006 | - | - | 0.882 | 0.924 | 0.143 | 2.42x | 18.3/32.5/39.5% | 1.8/5.8% | 3 |
| inverse | 1 | 0.796 | 0.785 | 0.011 | - | - | 0.894 | 0.936 | 0.129 | 2.31x | 15.9/27.0/32.9% | 1.8/3.7% | 3 |

> role-placement=degree: decode_failures 95

> role-placement=inverse: decode_failures 87

> slower: 28.7 s per simulated hour against 3.48 over 30 prior run(s) - 8.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `BL-control` - protocol  `--scenario coastal`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.908 | 0.908 | 0.000 | - | - | 0 | 0.000 | 0.730 | 1.24x | 17.1/22.0/24.1% | 1.9/5.0% | 3 |
| sr | 1 | 0.912 | 0.896 | 0.016 | - | - | 0.982 | 0.986 | 0.746 | 1.30x | 17.9/22.8/25.3% | 2.0/5.4% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario coastal`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.928 | 0.930 | 0.724 | 3.06x | 40.3/56.5/63.1% | 4.3/10.0% | 3 |
| 100 | 1 | 0.930 | 0.927 | 0.004 | - | - | 0.975 | 0.975 | 0.871 | 1.57x | 21.3/31.0/35.4% | 2.1/5.3% | 3 |
| 120 | 1 | 0.930 | 0.927 | 0.004 | - | - | 0.975 | 0.975 | 0.871 | 1.57x | 21.3/31.0/35.4% | 2.1/5.3% | 3 |
| 250 | 1 | 0.930 | 0.927 | 0.004 | - | - | 0.975 | 0.975 | 0.871 | 1.57x | 21.3/31.0/35.4% | 2.1/5.3% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario coastal`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.326 | 0.322 | 0.004 | - | - | 0.390 | 0.391 | 0.149 | 11.16x | 40.2/54.5/66.1% | 3.9/10.8% | 3 |
| 120 | 1 | 0.513 | 0.506 | 0.006 | - | - | 0.617 | 0.619 | 0.263 | 4.06x | 14.8/21.6/29.8% | 1.3/5.2% | 3 |
| 250 | 1 | 0.519 | 0.512 | 0.007 | - | - | 0.635 | 0.636 | 0.267 | 4.00x | 14.6/20.8/28.7% | 1.3/5.1% | 3 |

> max-num-nodes=10: decode_failures 13

### `DB-platform` - platform-mix  `--scenario coastal`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.930 | 0.927 | 0.004 | - | - | 0.975 | 0.975 | 0.871 | 1.57x | 21.3/31.0/35.4% | 2.1/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.930 | 0.927 | 0.004 | - | - | 0.975 | 0.975 | 0.871 | 1.57x | 21.3/31.0/35.4% | 2.1/5.3% | 3 |
| constrained | 1 | 0.849 | 0.838 | 0.011 | - | - | 0.934 | 0.936 | 0.717 | 3.06x | 40.1/56.5/63.0% | 4.3/10.0% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario coastal`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.756 | 0.748 | 0.008 | - | - | 0.884 | 0.913 | 0.604 | 5.45x | 59.3/72.2/76.0% | 3.9/12.3% | 3 |
| 25 | 1 | 0.756 | 0.748 | 0.008 | - | - | 0.884 | 0.913 | 0.604 | 5.45x | 59.3/72.2/76.0% | 3.9/12.3% | 3 |
| 100 | 1 | 0.756 | 0.748 | 0.008 | - | - | 0.884 | 0.913 | 0.604 | 5.45x | 59.3/72.2/76.0% | 3.9/12.3% | 3 |
| 2000 | 1 | 0.756 | 0.748 | 0.008 | - | - | 0.884 | 0.913 | 0.604 | 5.45x | 59.3/72.2/76.0% | 3.9/12.3% | 3 |

> warm-num-nodes=0: queue drops 12.4% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 80

> warm-num-nodes=25: queue drops 12.4% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 80

> warm-num-nodes=100: queue drops 12.4% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 80

> warm-num-nodes=2000: queue drops 12.4% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 80

### `DG-burst` - burst-loss  `--scenario coastal`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 0.1 | 1 | 0.807 | 0.789 | 0.017 | - | - | 0.974 | 0.977 | 0.645 | 1.24x | 17.0/22.5/24.9% | 1.8/5.0% | 3 |
| 0.2 | 1 | 0.717 | 0.687 | 0.030 | - | - | 0.922 | 0.940 | 0.580 | 1.14x | 15.8/21.0/23.6% | 1.7/4.5% | 3 |
| 0.3 | 1 | 0.599 | 0.563 | 0.036 | - | - | 0.820 | 0.873 | 0.461 | 1.03x | 14.2/19.3/22.1% | 1.5/4.0% | 3 |

> burst-loss=0.2: decode_failures 21

> burst-loss=0.3: decode_failures 28

### `DG-loss` - extra-loss  `--scenario coastal`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 0.1 | 1 | 0.878 | 0.871 | 0.008 | - | - | 0.979 | 0.982 | 0.720 | 1.36x | 18.6/24.2/26.9% | 2.0/5.2% | 3 |
| 0.2 | 1 | 0.837 | 0.825 | 0.012 | - | - | 0.966 | 0.969 | 0.657 | 1.37x | 18.5/24.6/27.8% | 2.1/5.0% | 3 |
| 0.3 | 1 | 0.772 | 0.756 | 0.016 | - | - | 0.929 | 0.944 | 0.563 | 1.41x | 19.1/25.4/29.0% | 2.2/4.9% | 3 |

> extra-loss=0.3: decode_failures 3

### `DG-outage` - burst-loss  `--scenario coastal`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 0.1 | 1 | 0.799 | 0.788 | 0.011 | - | - | 0.942 | 0.972 | 0.599 | 1.20x | 16.3/22.0/24.4% | 1.7/4.9% | 3 |
| 0.2 | 1 | 0.687 | 0.665 | 0.022 | - | - | 0.845 | 0.912 | 0.560 | 1.15x | 15.5/21.0/23.6% | 1.7/4.4% | 3 |
| 0.3 | 1 | 0.584 | 0.557 | 0.027 | - | - | 0.759 | 0.873 | 0.419 | 1.08x | 15.0/19.9/22.9% | 1.6/4.4% | 3 |

> burst-loss=0.1: decode_failures 34

> burst-loss=0.2: decode_failures 40

> burst-loss=0.3: decode_failures 27

### `DM-mode` - dm-mode  `--scenario coastal`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.868 | 0.868 | 0.000 | - | - | 0.973 | 0.976 | 0.701 | 1.72x | 23.3/30.7/34.0% | 2.5/7.0% | 3 |
| directed-with-late-flood | 1 | 0.882 | 0.882 | 0.000 | - | - | 0.974 | 0.979 | 0.727 | 1.57x | 21.2/28.4/31.3% | 2.3/6.5% | 3 |
| m4-early-flood | 1 | 0.874 | 0.874 | 0.000 | - | - | 0.970 | 0.977 | 0.720 | 1.56x | 21.2/28.2/31.1% | 2.3/6.4% | 3 |

### `FW-firmware` - profile  `--scenario coastal`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.908 | 0.902 | 0.006 | - | - | 0.989 | 0.994 | 0.702 | 0.72x | 8.5/12.3/14.0% | 1.2/1.8% | 3 |
| 2.8 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario coastal`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 0.25 | 1 | 0.886 | 0.866 | 0.020 | - | - | 0.979 | 0.985 | 0.653 | 1.16x | 14.3/20.9/22.9% | 1.7/4.6% | 3 |
| 0.5 | 1 | 0.893 | 0.886 | 0.007 | - | - | 0.987 | 0.988 | 0.713 | 1.01x | 13.0/17.8/22.0% | 1.5/3.8% | 3 |
| 0.75 | 1 | 0.904 | 0.890 | 0.013 | - | - | 0.990 | 0.991 | 0.738 | 0.89x | 11.2/16.2/18.4% | 1.3/3.6% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario coastal`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 0.25 | 1 | 0.895 | 0.877 | 0.019 | - | - | 0.985 | 0.986 | 0.686 | 1.15x | 14.5/20.4/22.6% | 1.7/4.5% | 3 |
| 0.5 | 1 | 0.896 | 0.888 | 0.007 | - | - | 0.987 | 0.989 | 0.721 | 0.98x | 13.0/17.8/22.1% | 1.5/3.8% | 3 |
| 0.75 | 1 | 0.906 | 0.895 | 0.012 | - | - | 0.989 | 0.989 | 0.741 | 0.86x | 11.0/16.1/18.3% | 1.3/3.6% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario coastal`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.933 | 0.930 | 0.003 | - | - | 0.989 | 0.991 | 0.801 | 0.67x | 9.7/12.3/13.7% | 0.9/3.0% | 3 |
| signing=true | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |

### `FW-versions` - profile  `--scenario coastal`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.900 | 0.894 | 0.006 | - | - | 0.986 | 0.990 | 0.640 | 0.73x | 9.2/13.5/15.2% | 1.2/2.4% | 3 |
| 2.5 | 1 | 0.901 | 0.895 | 0.006 | - | - | 0.986 | 0.989 | 0.656 | 0.73x | 9.1/13.5/15.1% | 1.1/2.3% | 3 |
| 2.6 | 1 | 0.902 | 0.896 | 0.006 | - | - | 0.990 | 0.994 | 0.637 | 0.72x | 9.3/13.8/15.5% | 1.2/2.5% | 3 |
| 2.7 | 1 | 0.912 | 0.906 | 0.005 | - | - | 0.980 | 0.982 | 0.655 | 0.74x | 9.3/15.9/17.5% | 1.1/3.2% | 3 |
| 2.8 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario coastal`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.931 | 0.927 | 0.003 | - | - | 0.994 | 0.995 | 0.810 | 0.86x | 11.8/15.2/16.8% | 1.3/3.5% | 3 |
| 900 | 1 | 0.883 | 0.873 | 0.009 | - | - | 0.981 | 0.983 | 0.746 | 2.00x | 27.2/35.6/39.4% | 3.0/8.2% | 3 |
| 300 | 1 | 0.603 | 0.582 | 0.021 | - | - | 0.798 | 0.827 | 0.411 | 4.32x | 54.7/66.9/74.3% | 6.6/14.8% | 3 |

> broadcast-interval-s=300: decode_failures 26

### `LD-chatty-hops` - broadcast-interval-s  `--scenario coastal`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.954 | 0.953 | 0.001 | - | - | 0.991 | 0.991 | 0.853 | 0.91x | 12.5/15.2/16.7% | 1.3/3.4% | 3 |
| 900 | 1 | 0.904 | 0.898 | 0.006 | - | - | 0.966 | 0.967 | 0.819 | 2.35x | 31.5/39.3/43.1% | 3.5/8.8% | 3 |
| 300 | 1 | 0.625 | 0.608 | 0.017 | - | - | 0.796 | 0.802 | 0.506 | 4.93x | 60.8/71.0/76.0% | 7.7/16.1% | 3 |

> broadcast-interval-s=300: decode_failures 19

### `LD-diurnal` - diurnal  `--scenario coastal`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.920 | 0.915 | 0.004 | - | - | 0.988 | 0.989 | 0.772 | 1.17x | 16.1/20.9/22.9% | 1.7/4.9% | 3 |
| sinusoid | 1 | 0.914 | 0.908 | 0.006 | - | - | 0.989 | 0.990 | 0.772 | 1.21x | 16.5/21.3/23.4% | 1.8/4.8% | 3 |
| commuter | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario coastal`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.883 | 0.873 | 0.009 | - | - | 0.981 | 0.983 | 0.746 | 2.00x | 27.2/35.6/39.4% | 3.0/8.2% | 3 |
| 3600 | 1 | 0.931 | 0.927 | 0.003 | - | - | 0.994 | 0.995 | 0.810 | 0.86x | 11.8/15.2/16.8% | 1.3/3.5% | 3 |
| 10800 | 1 | 0.936 | 0.932 | 0.004 | - | - | 0.994 | 0.994 | 0.819 | 0.57x | 7.8/10.1/11.2% | 0.8/2.3% | 3 |
| 43200 | 1 | 0.946 | 0.943 | 0.002 | - | - | 0.999 | 1.000 | 0.823 | 0.42x | 5.6/7.3/8.0% | 0.6/1.7% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario coastal`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 0.25 | 1 | 0.900 | 0.894 | 0.006 | - | - | 0.984 | 0.985 | 0.759 | 1.35x | 18.5/24.1/26.5% | 2.0/5.6% | 3 |
| 1.0 | 1 | 0.894 | 0.887 | 0.007 | - | - | 0.981 | 0.982 | 0.752 | 1.49x | 20.5/26.6/29.4% | 2.2/6.2% | 3 |
| 4.0 | 1 | 0.864 | 0.856 | 0.008 | - | - | 0.972 | 0.972 | 0.706 | 1.88x | 26.0/34.2/38.0% | 2.7/8.1% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario coastal`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.756 | 0.748 | 0.008 | - | - | 0.884 | 0.913 | 0.604 | 5.45x | 59.3/72.2/76.0% | 3.9/12.3% | 3 |
| 1.0 | 1 | 0.654 | 0.646 | 0.008 | - | - | 0.795 | 0.840 | 0.497 | 6.11x | 64.5/74.8/78.0% | 4.4/14.0% | 3 |

> traceroute-per-hour=0.0: queue drops 12.4% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 80

> traceroute-per-hour=1.0: queue drops 23.3% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 112

### `MS-density` - nodes  `--scenario coastal`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.692 | 0.683 | 0.009 | - | - | 0.545 | 0.812 | 0.240 | 1.29x | 19.8/26.1/30.9% | 3.3/6.5% | 3 |
| 60 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 90 | 1 | 0.943 | 0.934 | 0.009 | - | - | 0.993 | 0.994 | 0.682 | 1.58x | 20.1/28.1/32.2% | 1.4/5.0% | 3 |
| 120 | 1 | 0.964 | 0.963 | 0.001 | - | - | 0.998 | 0.999 | 0.837 | 1.86x | 22.2/31.8/35.5% | 1.2/4.8% | 3 |
| 150 | 1 | 0.968 | 0.967 | 0.001 | - | - | 0.999 | 0.999 | 0.875 | 2.44x | 27.6/38.2/43.5% | 1.2/5.6% | 3 |

> nodes=40: decode_failures 15

### `MS-hopscale` - nodes  `--scenario coastal`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 120 | 1 | 0.758 | 0.745 | 0.013 | - | - | 0.961 | 0.963 | 0.273 | 2.00x | 14.7/21.4/26.4% | 1.3/5.2% | 3 |
| 250 | 1 | 0.503 | 0.497 | 0.006 | - | - | 0.609 | 0.610 | 0.270 | 4.34x | 15.9/22.8/31.8% | 1.5/5.6% | 3 |
| 500 | 1 | 0.323 | 0.321 | 0.003 | - | - | 0.483 | 0.483 | 0.127 | 10.12x | 19.3/32.3/46.4% | 1.7/6.8% | 3 |

> nodes=120: decode_failures 4

> nodes=250: decode_failures 1

> nodes=500: decode_failures 6

### `MS-oversubscribed` - nodes  `--scenario coastal`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.755 | 0.740 | 0.015 | - | - | 0.974 | 0.974 | 0.258 | 1.90x | 14.0/20.1/24.8% | 1.2/4.9% | 3 |
| 250 | 1 | 0.513 | 0.506 | 0.006 | - | - | 0.617 | 0.619 | 0.263 | 4.06x | 14.8/21.6/29.8% | 1.3/5.2% | 3 |
| 500 | 1 | 0.328 | 0.325 | 0.003 | - | - | 0.495 | 0.496 | 0.125 | 9.38x | 17.7/29.9/42.6% | 1.6/6.3% | 3 |

> nodes=500: decode_failures 3

> faster: 9.65 s per simulated hour against 19.9 over 30 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-roles` - role-mix  `--scenario coastal`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.891 | 0.885 | 0.006 | - | - | 0.971 | 0.972 | 0.768 | 1.31x | 17.9/23.2/25.4% | 1.9/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.832 | 0.824 | 0.008 | - | - | 0.933 | 0.937 | 0.610 | 1.18x | 16.8/22.3/25.9% | 2.0/5.1% | 3 |

### `MS-roles-fav` - role-mix  `--scenario coastal`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.902 | 0.897 | 0.005 | - | - | 0.972 | 0.973 | 0.788 | 1.35x | 18.3/23.7/26.1% | 2.0/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.866 | 0.859 | 0.007 | - | - | 0.925 | 0.928 | 0.701 | 1.36x | 18.9/26.0/29.8% | 2.3/5.1% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario coastal`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 0.05 | 1 | 0.905 | 0.899 | 0.006 | - | - | 0.977 | 0.978 | 0.791 | 1.39x | 18.8/27.1/32.0% | 1.9/5.1% | 3 |
| 0.1 | 1 | 0.906 | 0.900 | 0.005 | - | - | 0.972 | 0.972 | 0.795 | 1.48x | 19.9/30.9/36.0% | 2.0/5.1% | 3 |
| 0.2 | 1 | 0.908 | 0.904 | 0.004 | - | - | 0.972 | 0.972 | 0.804 | 1.63x | 21.3/32.4/38.0% | 2.1/5.1% | 3 |

### `MS-siting` - siting-mix  `--scenario coastal`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| local-typical | 1 | 0.640 | 0.634 | 0.006 | - | - | 0.815 | 0.817 | 0.000 | 1.48x | 13.4/20.7/26.3% | 2.3/5.4% | 3 |
| event | 1 | 0.190 | 0.190 | 0.000 | - | - | 0.135 | 0.269 | 0.000 | 1.23x | 6.5/14.8/19.5% | 1.9/4.7% | 2 |
| backbone | 1 | 0.978 | 0.978 | 0.000 | - | - | 1.000 | 1.000 | 0.883 | 1.08x | 26.9/35.5/37.2% | 1.2/5.4% | 3 |

> siting-mix=event: 3 archives requested, 2 placed - group on the placed count

### `MS-size` - nodes  `--scenario coastal`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.899 | 0.879 | 0.020 | - | - | 0.992 | 0.995 | 0.742 | 1.43x | 26.3/31.0/37.1% | 3.3/7.8% | 3 |
| 60 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 90 | 1 | 0.830 | 0.819 | 0.011 | - | - | 0.940 | 0.942 | 0.405 | 1.58x | 14.8/22.2/26.2% | 1.4/5.3% | 3 |
| 120 | 1 | 0.758 | 0.745 | 0.013 | - | - | 0.961 | 0.963 | 0.273 | 2.00x | 14.7/21.4/26.4% | 1.3/5.2% | 3 |
| 150 | 1 | 0.709 | 0.695 | 0.014 | - | - | 0.904 | 0.905 | 0.177 | 2.56x | 15.0/22.0/28.7% | 1.4/4.8% | 3 |

> nodes=120: decode_failures 4

### `MS-stretch` - stretch  `--scenario coastal`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 1.25 | 1 | 0.680 | 0.666 | 0.014 | - | - | 0.881 | 0.886 | 0.260 | 1.32x | 13.2/21.3/27.4% | 2.0/5.1% | 3 |
| 1.5 | 1 | 0.433 | 0.417 | 0.017 | - | - | 0.699 | 0.815 | 0.026 | 1.35x | 9.2/18.9/20.5% | 1.9/4.8% | 3 |
| 2.0 | 1 | 0.151 | 0.146 | 0.005 | - | - | 0.379 | 0.405 | 0.000 | 0.87x | 3.8/9.3/13.0% | 1.2/3.5% | 3 |

> stretch=1.5: decode_failures 6

> stretch=2.0: decode_failures 2

### `MS-topology` - topology  `--scenario coastal`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| clustered | 1 | 0.946 | 0.945 | 0.002 | - | - | 0.989 | 0.989 | 0.704 | 1.09x | 29.1/37.1/38.3% | 1.5/5.5% | 3 |
| corridor | 1 | 0.680 | 0.675 | 0.005 | - | - | 0.895 | 0.895 | 0.297 | 1.26x | 14.2/25.2/28.5% | 1.7/5.8% | 3 |
| hub | 1 | 0.956 | 0.955 | 0.001 | - | - | 0.987 | 0.987 | 0.799 | 1.17x | 27.5/35.9/38.2% | 1.7/5.4% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario coastal`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.882 | 0.882 | 0.000 | - | - | 0.974 | 0.979 | 0.727 | 1.57x | 21.2/28.4/31.3% | 2.3/6.5% | 3 |
| True | 1 | 0.882 | 0.882 | 0.000 | - | - | 0.978 | 0.982 | 0.710 | 1.56x | 21.1/28.4/31.3% | 2.3/6.5% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario coastal`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.882 | 0.882 | 0.000 | - | - | 0.978 | 0.982 | 0.710 | 1.56x | 21.1/28.4/31.3% | 2.3/6.5% | 3 |
| m4-early-flood | 1 | 0.883 | 0.883 | 0.000 | - | - | 0.979 | 0.983 | 0.703 | 1.57x | 21.2/28.3/31.2% | 2.3/6.4% | 3 |

### `PR-protocol` - protocol  `--scenario coastal`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.908 | 0.908 | 0.000 | - | - | 0 | 0.000 | 0.730 | 1.24x | 17.1/22.0/24.1% | 1.9/5.0% | 3 |
| chain | 1 | 0.890 | 0.887 | 0.003 | - | - | 0.922 | 0.980 | 0.734 | 1.46x | 20.0/26.1/28.8% | 2.2/5.9% | 3 |
| sr | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |

### `PR-repeats` - extra-repeats  `--scenario coastal`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| True | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.983 | 0.984 | 0.778 | 1.28x | 17.4/22.6/24.9% | 1.9/5.2% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario coastal`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.964 | 0.963 | 0.001 | - | - | 0.998 | 0.999 | 0.837 | 1.86x | 22.2/31.8/35.5% | 1.2/4.8% | 3 |
| True | 1 | 0.963 | 0.962 | 0.001 | - | - | 0.999 | 0.999 | 0.853 | 1.93x | 22.9/32.5/36.4% | 1.3/4.9% | 3 |

### `RF-bw500` - preset  `--scenario coastal`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.173 | 0.168 | 0.005 | - | - | 0.410 | 0.412 | 0.000 | 0.04x | 0.2/0.5/0.7% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.458 | 0.446 | 0.013 | - | - | 0.770 | 0.832 | 0.017 | 0.26x | 1.8/4.1/4.7% | 0.4/1.1% | 3 |
| LONG_TURBO | 1 | 0.828 | 0.822 | 0.006 | - | - | 0.941 | 0.941 | 0.424 | 1.28x | 13.2/20.9/25.5% | 2.0/4.8% | 3 |

> preset=MEDIUM_TURBO: decode_failures 12

### `RF-duct` - duct-per-hour  `--scenario coastal`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 0.25 | 1 | 0.915 | 0.910 | 0.005 | - | - | 0.982 | 0.982 | 0.813 | 1.21x | 19.1/24.1/26.4% | 1.7/5.3% | 3 |
| 1.0 | 1 | 0.942 | 0.936 | 0.006 | - | - | 0.985 | 0.985 | 0.870 | 1.02x | 23.9/28.3/30.4% | 1.3/5.4% | 3 |

### `RF-eu-presets` - preset  `--scenario coastal`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.338 | 0.325 | 0.012 | - | - | 0.665 | 0.672 | 0.000 | 0.13x | 0.7/1.7/2.5% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| LITE_FAST | 1 | 0.855 | 0.848 | 0.008 | - | - | 0.977 | 0.978 | 0.634 | 0.98x | 12.0/16.4/19.1% | 1.5/4.0% | 3 |
| NARROW_SLOW | 1 | 0.867 | 0.858 | 0.009 | - | - | 0.975 | 0.975 | 0.634 | 1.24x | 16.1/21.5/24.8% | 1.9/5.2% | 3 |

> preset=SHORT_FAST: decode_failures 1

### `RF-noise` - noise-profile  `--scenario coastal`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| temporal | 1 | 0.825 | 0.814 | 0.011 | - | - | 0.959 | 0.961 | 0.629 | 1.29x | 17.2/23.1/26.2% | 2.0/5.1% | 3 |
| transient | 1 | 0.896 | 0.890 | 0.006 | - | - | 0.975 | 0.976 | 0.739 | 1.28x | 17.4/22.7/25.0% | 1.9/5.2% | 3 |
| periodic | 1 | 0.732 | 0.724 | 0.008 | - | - | 0.819 | 0.821 | 0.588 | 1.18x | 16.1/20.9/23.4% | 1.7/4.6% | 3 |

### `RF-preset` - preset  `--scenario coastal`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.338 | 0.325 | 0.012 | - | - | 0.665 | 0.672 | 0.000 | 0.13x | 0.7/1.7/2.5% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| LONG_MODERATE | 1 | 0.876 | 0.861 | 0.015 | - | - | 0.958 | 0.962 | 0.685 | 3.23x | 47.9/61.7/67.1% | 4.7/12.2% | 3 |

> preset=SHORT_FAST: decode_failures 1

> preset=LONG_MODERATE: misdecodes 1

> preset=LONG_MODERATE: decode_failures 9

### `RF-preset-turbo` - preset  `--scenario coastal`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.052 | 0.052 | 0.000 | - | - | 0.043 | 0.044 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.173 | 0.168 | 0.005 | - | - | 0.410 | 0.412 | 0.000 | 0.04x | 0.2/0.5/0.7% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| LONG_TURBO | 1 | 0.828 | 0.822 | 0.006 | - | - | 0.941 | 0.941 | 0.424 | 1.28x | 13.2/20.9/25.5% | 2.0/4.8% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.899 | 0.891 | 0.008 | - | - | 0.985 | 0.987 | 0.785 | 1.75x | 22.8/29.3/32.4% | 2.5/6.9% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario coastal`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.853 | 0.846 | 0.008 | - | - | 0.937 | 0.940 | 0.719 | 1.26x | 17.3/22.3/24.5% | 1.9/5.0% | 3 |
| 10000 | 1 | 0.732 | 0.724 | 0.008 | - | - | 0.819 | 0.821 | 0.588 | 1.18x | 16.1/20.9/23.4% | 1.7/4.6% | 3 |
| 4000 | 1 | 0.476 | 0.468 | 0.008 | - | - | 0.549 | 0.593 | 0.342 | 1.03x | 14.1/18.5/21.1% | 1.6/3.5% | 3 |
| 2000 | 1 | 0.111 | 0.111 | 0.000 | - | - | 0.141 | 0.209 | 0.052 | 0.73x | 9.9/13.9/16.4% | 1.1/2.2% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 4

### `RF-stretch-duct` - duct-per-hour  `--scenario coastal`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.433 | 0.417 | 0.017 | - | - | 0.699 | 0.815 | 0.026 | 1.35x | 9.2/18.9/20.5% | 1.9/4.8% | 3 |
| 1.0 | 1 | 0.748 | 0.698 | 0.050 | - | - | 0.890 | 0.899 | 0.502 | 1.01x | 17.1/23.0/24.7% | 1.4/4.7% | 3 |

> duct-per-hour=0.0: decode_failures 6

> duct-per-hour=1.0: decode_failures 10

### `RF-txpower` - tx-power  `--scenario coastal`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 22 | 1 | 0.434 | 0.417 | 0.018 | - | - | 0.705 | 0.788 | 0.054 | 1.43x | 9.5/19.1/22.2% | 2.0/5.2% | 3 |
| 17 | 1 | 0.155 | 0.150 | 0.005 | - | - | 0.350 | 0.386 | 0.000 | 0.88x | 3.9/9.0/12.5% | 1.2/3.4% | 3 |
| 14 | 1 | 0.087 | 0.086 | 0.000 | - | - | 0.040 | 0.044 | 0.000 | 0.64x | 2.7/5.6/9.5% | 1.0/2.6% | 3 |

> tx-power=22: decode_failures 11

> tx-power=17: decode_failures 15

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario coastal`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.964 | 0.963 | 0.001 | - | - | 0.998 | 0.999 | 0.837 | 1.86x | 22.2/31.8/35.5% | 1.2/4.8% | 3 |
| True | 1 | 0.959 | 0.957 | 0.001 | - | - | 0.999 | 0.999 | 0.827 | 2.28x | 26.9/37.8/41.1% | 1.5/5.6% | 3 |

### `RT-favourites` - favourite-routers  `--scenario coastal`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.908 | 0.904 | 0.004 | - | - | 0.976 | 0.976 | 0.801 | 1.34x | 17.8/25.8/30.3% | 1.8/5.0% | 3 |
| True | 1 | 0.924 | 0.919 | 0.005 | - | - | 0.979 | 0.979 | 0.842 | 1.44x | 19.1/27.2/31.5% | 1.9/5.2% | 3 |

### `RT-hopassign` - hop-assign  `--scenario coastal`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| random | 1 | 0.864 | 0.857 | 0.007 | - | - | 0.964 | 0.964 | 0.719 | 1.25x | 17.1/22.5/24.7% | 1.8/5.3% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario coastal`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.741 | 0.707 | 0.034 | - | - | 0.942 | 0.953 | 0.498 | 0.95x | 13.1/18.4/20.8% | 1.3/4.6% | 3 |
| 7 | 1 | 0.941 | 0.938 | 0.003 | - | - | 0.988 | 0.989 | 0.833 | 1.41x | 19.3/23.9/26.3% | 2.0/5.4% | 3 |
| 15 | 1 | 0.951 | 0.949 | 0.003 | - | - | 0.985 | 0.985 | 0.853 | 1.44x | 19.6/24.2/26.6% | 2.1/5.4% | 3 |
| 32 | 1 | 0.952 | 0.950 | 0.001 | - | - | 0.982 | 0.982 | 0.846 | 1.44x | 19.5/24.2/26.6% | 2.1/5.4% | 3 |

> hop-limit=3: decode_failures 5

### `RT-hopspread` - hop-limit  `--scenario coastal`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.741 | 0.707 | 0.034 | - | - | 0.942 | 0.953 | 0.498 | 0.95x | 13.1/18.4/20.8% | 1.3/4.6% | 3 |
| 5 | 1 | 0.895 | 0.887 | 0.008 | - | - | 0.982 | 0.984 | 0.750 | 1.32x | 18.1/23.0/25.4% | 1.9/5.3% | 3 |
| 7 | 1 | 0.941 | 0.938 | 0.003 | - | - | 0.988 | 0.989 | 0.833 | 1.41x | 19.3/23.9/26.3% | 2.0/5.4% | 3 |

> hop-limit=3: decode_failures 5

### `RT-rebroadcast` - rebroadcast-mode  `--scenario coastal`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| KNOWN_ONLY | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.903 | 0.903 | 0.000 | - | - | 0.912 | 0.982 | 0.737 | 1.25x | 17.4/22.3/24.4% | 1.9/5.1% | 3 |

### `RT-spread` - hop-spread  `--scenario coastal`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.741 | 0.707 | 0.034 | - | - | 0.942 | 0.953 | 0.498 | 0.95x | 13.1/18.4/20.8% | 1.3/4.6% | 3 |
| True | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |

> hop-spread=False: decode_failures 5

### `SC-signing` - signature-policy  `--scenario coastal`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| BALANCED | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| STRICT | 1 | 0.811 | 0.811 | 0.000 | - | - | 0.899 | 0.899 | 0.672 | 1.44x | 19.3/25.4/28.0% | 2.1/5.8% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario coastal`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| dm | 1 | 0.908 | 0.901 | 0.007 | - | - | 0.989 | 0.990 | 0.774 | 1.27x | 17.5/22.7/25.1% | 1.9/5.3% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario coastal`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.902 | 0.896 | 0.005 | - | - | 0.981 | 0.982 | 0.739 | 1.26x | 17.3/22.6/24.9% | 1.9/5.2% | 3 |
| local | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| time | 1 | 0.901 | 0.895 | 0.005 | - | - | 0.980 | 0.981 | 0.762 | 1.33x | 18.1/23.6/25.9% | 2.0/5.5% | 3 |
| window | 1 | 0.904 | 0.899 | 0.005 | - | - | 0.980 | 0.982 | 0.766 | 1.27x | 17.5/22.4/24.7% | 1.9/5.2% | 3 |

> bucket-mode=global: misdecodes 47

> bucket-mode=time: misdecodes 27

> bucket-mode=window: misdecodes 21

### `SF-bucket-time` - time-bucket-s  `--scenario coastal`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.897 | 0.891 | 0.006 | - | - | 0.977 | 0.980 | 0.728 | 1.42x | 19.5/25.4/28.1% | 2.1/6.0% | 3 |
| 1800 | 1 | 0.901 | 0.895 | 0.005 | - | - | 0.980 | 0.981 | 0.762 | 1.33x | 18.1/23.6/25.9% | 2.0/5.5% | 3 |
| 3600 | 1 | 0.903 | 0.899 | 0.005 | - | - | 0.981 | 0.985 | 0.741 | 1.28x | 17.6/22.9/25.1% | 1.9/5.3% | 3 |

> time-bucket-s=600: misdecodes 140

> time-bucket-s=1800: misdecodes 27

> time-bucket-s=3600: misdecodes 5

### `SF-cadence` - trigger  `--scenario coastal`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| interval | 1 | 0.895 | 0.888 | 0.007 | - | - | 0.980 | 0.984 | 0.747 | 1.70x | 22.8/30.0/34.0% | 2.5/7.3% | 3 |
| aimd | 1 | 0.898 | 0.897 | 0.001 | - | - | 0.926 | 0.982 | 0.731 | 1.29x | 17.8/22.9/25.2% | 1.9/5.2% | 3 |
| bucket+interval | 1 | 0.890 | 0.882 | 0.008 | - | - | 0.976 | 0.977 | 0.754 | 1.73x | 23.2/30.7/34.9% | 2.5/7.4% | 3 |

> trigger=interval: misdecodes 15

> trigger=aimd: misdecodes 4

> trigger=bucket+interval: misdecodes 20

### `SF-capacity` - capacity  `--scenario coastal`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.903 | 0.899 | 0.004 | - | - | 0.979 | 0.981 | 0.758 | 1.29x | 17.6/23.1/25.5% | 1.9/5.3% | 3 |
| 8 | 1 | 0.903 | 0.897 | 0.007 | - | - | 0.982 | 0.986 | 0.758 | 1.27x | 17.5/22.6/24.9% | 1.9/5.2% | 3 |
| 16 | 1 | 0.905 | 0.899 | 0.006 | - | - | 0.982 | 0.982 | 0.771 | 1.28x | 17.5/22.6/25.0% | 1.9/5.2% | 3 |
| 32 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 50 | 1 | 0.906 | 0.901 | 0.005 | - | - | 0.981 | 0.982 | 0.758 | 1.28x | 17.5/22.7/24.9% | 1.9/5.2% | 3 |

> capacity=4: decode_failures 102

> capacity=8: decode_failures 47

### `SF-capacity-local` - capacity  `--scenario coastal`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.903 | 0.899 | 0.004 | - | - | 0.979 | 0.981 | 0.758 | 1.29x | 17.6/23.1/25.5% | 1.9/5.3% | 3 |
| 8 | 1 | 0.903 | 0.897 | 0.007 | - | - | 0.982 | 0.986 | 0.758 | 1.27x | 17.5/22.6/24.9% | 1.9/5.2% | 3 |
| 16 | 1 | 0.905 | 0.899 | 0.006 | - | - | 0.982 | 0.982 | 0.771 | 1.28x | 17.5/22.6/25.0% | 1.9/5.2% | 3 |
| 32 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 50 | 1 | 0.906 | 0.901 | 0.005 | - | - | 0.981 | 0.982 | 0.758 | 1.28x | 17.5/22.7/24.9% | 1.9/5.2% | 3 |

> capacity=4: decode_failures 102

> capacity=8: decode_failures 47

### `SF-capacity-window` - capacity  `--scenario coastal`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.901 | 0.898 | 0.004 | - | - | 0.970 | 0.981 | 0.761 | 1.27x | 17.4/22.5/24.7% | 1.9/5.2% | 3 |
| 16 | 1 | 0.902 | 0.895 | 0.006 | - | - | 0.979 | 0.983 | 0.766 | 1.26x | 17.4/22.5/24.7% | 1.9/5.2% | 3 |
| 32 | 1 | 0.904 | 0.899 | 0.005 | - | - | 0.980 | 0.982 | 0.766 | 1.27x | 17.5/22.4/24.7% | 1.9/5.2% | 3 |

> capacity=8: misdecodes 25

> capacity=8: decode_failures 34

> capacity=16: misdecodes 30

> capacity=32: misdecodes 21

### `SF-catchup` - catch-up-hours  `--scenario coastal`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.890 | 0.882 | 0.008 | - | - | 0.976 | 0.977 | 0.754 | 1.73x | 23.2/30.7/34.9% | 2.5/7.4% | 3 |
| 02-06 | 1 | 0.905 | 0.902 | 0.003 | - | - | 0.949 | 0.986 | 0.751 | 1.28x | 17.7/22.9/25.2% | 1.9/5.3% | 3 |
| 00-08 | 1 | 0.905 | 0.902 | 0.003 | - | - | 0.959 | 0.986 | 0.762 | 1.35x | 18.6/24.4/26.9% | 2.0/5.7% | 3 |

> catch-up-hours=: misdecodes 20

> catch-up-hours=02-06: decode_failures 38

> catch-up-hours=00-08: decode_failures 38

### `SF-hops-flat` - hops-apart  `--scenario coastal`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.901 | 0.900 | 0.001 | - | - | 0.980 | 0.981 | 0.745 | 1.28x | 17.6/22.6/25.0% | 1.9/5.2% | 3 |
| 2 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 3 | 1 | 0.912 | 0.896 | 0.016 | - | - | 0.982 | 0.986 | 0.746 | 1.30x | 17.9/22.8/25.3% | 2.0/5.4% | 3 |
| 4 | 1 | 0.919 | 0.899 | 0.021 | - | - | 0.981 | 0.984 | 0.748 | 1.29x | 17.7/22.6/25.0% | 1.9/5.3% | 3 |

### `SF-hops-spread` - hops-apart  `--scenario coastal`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.901 | 0.900 | 0.001 | - | - | 0.980 | 0.981 | 0.745 | 1.28x | 17.6/22.6/25.0% | 1.9/5.2% | 3 |
| 2 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 3 | 1 | 0.912 | 0.896 | 0.016 | - | - | 0.982 | 0.986 | 0.746 | 1.30x | 17.9/22.8/25.3% | 2.0/5.4% | 3 |
| 4 | 1 | 0.919 | 0.899 | 0.021 | - | - | 0.981 | 0.984 | 0.748 | 1.29x | 17.7/22.6/25.0% | 1.9/5.3% | 3 |
| 5 | 1 | 0.917 | 0.896 | 0.020 | - | - | 0.987 | 0.992 | 0.753 | 1.30x | 17.9/22.9/25.4% | 1.9/5.5% | 3 |

> faster: 1.92 s per simulated hour against 4.56 over 30 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-jitter-global` - advert-jitter-s  `--scenario coastal`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.900 | 0.895 | 0.005 | - | - | 0.978 | 0.978 | 0.773 | 1.26x | 17.3/22.4/24.7% | 1.9/5.2% | 3 |
| 30 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 120 | 1 | 0.908 | 0.903 | 0.005 | - | - | 0.985 | 0.987 | 0.771 | 1.28x | 17.6/22.7/24.9% | 1.9/5.2% | 3 |
| 600 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.981 | 0.982 | 0.778 | 1.27x | 17.4/22.5/24.8% | 1.9/5.2% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario coastal`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.900 | 0.895 | 0.005 | - | - | 0.978 | 0.978 | 0.773 | 1.26x | 17.3/22.4/24.7% | 1.9/5.2% | 3 |
| 30 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 120 | 1 | 0.908 | 0.903 | 0.005 | - | - | 0.985 | 0.987 | 0.771 | 1.28x | 17.6/22.7/24.9% | 1.9/5.2% | 3 |
| 600 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.981 | 0.982 | 0.778 | 1.27x | 17.4/22.5/24.8% | 1.9/5.2% | 3 |

### `SF-place-flat` - place  `--scenario coastal`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.924 | 0.897 | 0.027 | - | - | 0.977 | 0.985 | 0.727 | 1.31x | 17.9/23.0/25.4% | 1.9/5.3% | 3 |
| routers | 1 | 0.906 | 0.905 | 0.001 | - | - | 0.985 | 0.985 | 0.748 | 1.27x | 17.5/22.7/25.0% | 1.9/5.2% | 3 |
| alternate-routers | 1 | 0.903 | 0.898 | 0.004 | - | - | 0.986 | 0.987 | 0.737 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| beside-router | 1 | 0.904 | 0.903 | 0.002 | - | - | 0.985 | 0.985 | 0.749 | 1.29x | 17.6/22.8/25.0% | 1.9/5.2% | 3 |
| random-clients | 1 | 0.909 | 0.903 | 0.006 | - | - | 0.990 | 0.990 | 0.737 | 1.26x | 17.3/22.4/24.7% | 1.9/5.1% | 3 |
| hops-apart | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |

> place=spread: decode_failures 1

### `SF-place-spread` - place  `--scenario coastal`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.924 | 0.897 | 0.027 | - | - | 0.977 | 0.985 | 0.727 | 1.31x | 17.9/23.0/25.4% | 1.9/5.3% | 3 |
| routers | 1 | 0.906 | 0.905 | 0.001 | - | - | 0.985 | 0.985 | 0.748 | 1.27x | 17.5/22.7/25.0% | 1.9/5.2% | 3 |
| alternate-routers | 1 | 0.903 | 0.898 | 0.004 | - | - | 0.986 | 0.987 | 0.737 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| beside-router | 1 | 0.904 | 0.903 | 0.002 | - | - | 0.985 | 0.985 | 0.749 | 1.29x | 17.6/22.8/25.0% | 1.9/5.2% | 3 |
| random-clients | 1 | 0.909 | 0.903 | 0.006 | - | - | 0.990 | 0.990 | 0.737 | 1.26x | 17.3/22.4/24.7% | 1.9/5.1% | 3 |
| hops-apart | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |

> place=spread: decode_failures 1

### `SF-provide-transport` - provide-transport  `--scenario coastal`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| broadcast | 1 | 0.916 | 0.889 | 0.027 | - | - | 0.976 | 0.977 | 0.804 | 1.36x | 18.6/24.2/26.5% | 2.0/5.5% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario coastal`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| heard | 1 | 0.904 | 0.899 | 0.005 | - | - | 0.979 | 0.980 | 0.781 | 1.30x | 17.8/23.1/25.4% | 2.0/5.3% | 3 |

> replay-ordering=heard: misdecodes 10

### `SF-replay-order-broadcast` - replay-ordering  `--scenario coastal`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.916 | 0.889 | 0.027 | - | - | 0.976 | 0.977 | 0.804 | 1.36x | 18.6/24.2/26.5% | 2.0/5.5% | 3 |
| heard | 1 | 0.921 | 0.894 | 0.027 | - | - | 0.981 | 0.982 | 0.784 | 1.38x | 18.8/24.3/26.8% | 2.0/5.6% | 3 |

> replay-ordering=heard: misdecodes 6

### `SF-resolve` - resolve  `--scenario coastal`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| enum | 1 | 0.906 | 0.901 | 0.005 | - | - | 0.977 | 0.983 | 0.763 | 1.26x | 17.3/22.7/25.0% | 1.8/5.2% | 3 |
| hybrid | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |

### `SF-servers-allrouters` - servers  `--scenario coastal`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.906 | 0.905 | 0.001 | - | - | 0.985 | 0.985 | 0.748 | 1.27x | 17.5/22.7/25.0% | 1.9/5.2% | 3 |
| 6 | 1 | 0.907 | 0.899 | 0.008 | - | - | 0.984 | 0.984 | 0.737 | 1.32x | 18.0/23.4/25.8% | 2.0/5.4% | 6 |

### `SF-servers-flat` - servers  `--scenario coastal`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.902 | 0.900 | 0.002 | - | - | 0.979 | 0.981 | 0.721 | 1.30x | 17.9/22.9/25.2% | 1.9/5.3% | 2 |
| 3 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 5 | 1 | 0.909 | 0.901 | 0.009 | - | - | 0.989 | 0.992 | 0.765 | 1.32x | 18.0/23.4/25.8% | 2.0/5.4% | 5 |
| 8 | 1 | 0.900 | 0.886 | 0.013 | - | - | 0.982 | 0.983 | 0.740 | 1.35x | 18.5/24.0/26.5% | 2.0/5.5% | 8 |

### `SF-servers-spread` - servers  `--scenario coastal`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.902 | 0.900 | 0.002 | - | - | 0.979 | 0.981 | 0.721 | 1.30x | 17.9/22.9/25.2% | 1.9/5.3% | 2 |
| 3 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 5 | 1 | 0.909 | 0.901 | 0.009 | - | - | 0.989 | 0.992 | 0.765 | 1.32x | 18.0/23.4/25.8% | 2.0/5.4% | 5 |
| 8 | 1 | 0.900 | 0.886 | 0.013 | - | - | 0.982 | 0.983 | 0.740 | 1.35x | 18.5/24.0/26.5% | 2.0/5.5% | 8 |

### `SF-signed` - signed  `--scenario coastal`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| True | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario coastal`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.902 | 0.898 | 0.004 | - | - | 0.974 | 0.978 | 0.737 | 1.17x | 15.9/21.0/23.2% | 1.7/4.8% | 3 |
| 1 | 1 | 0.899 | 0.893 | 0.006 | - | - | 0.973 | 0.977 | 0.763 | 1.17x | 16.1/21.2/23.3% | 1.8/4.9% | 3 |
| 2 | 1 | 0.894 | 0.889 | 0.005 | - | - | 0.972 | 0.977 | 0.750 | 1.19x | 16.3/21.2/23.3% | 1.8/4.9% | 3 |
| 4 | 1 | 0.903 | 0.897 | 0.006 | - | - | 0.978 | 0.981 | 0.774 | 1.20x | 16.4/21.6/23.7% | 1.8/4.9% | 3 |

### `SF-width` - short-id-bits  `--scenario coastal`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.904 | 0.898 | 0.006 | - | - | 0.982 | 0.982 | 0.757 | 1.27x | 17.5/22.7/25.0% | 1.9/5.2% | 3 |
| 24 | 1 | 0.900 | 0.896 | 0.005 | - | - | 0.979 | 0.979 | 0.758 | 1.27x | 17.4/22.6/24.9% | 1.9/5.2% | 3 |
| 32 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.987 | 0.774 | 1.28x | 17.6/22.7/25.0% | 1.9/5.2% | 3 |
| 64 | 1 | 0.903 | 0.899 | 0.004 | - | - | 0.980 | 0.981 | 0.747 | 1.29x | 17.6/22.9/25.1% | 1.9/5.3% | 3 |

### `SF-window-size` - window-size  `--scenario coastal`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.898 | 0.890 | 0.008 | - | - | 0.983 | 0.984 | 0.768 | 1.40x | 19.1/25.0/27.6% | 2.1/5.7% | 3 |
| 16 | 1 | 0.907 | 0.902 | 0.005 | - | - | 0.985 | 0.986 | 0.759 | 1.29x | 17.7/23.0/25.3% | 1.9/5.3% | 3 |
| 32 | 1 | 0.904 | 0.899 | 0.005 | - | - | 0.980 | 0.982 | 0.766 | 1.27x | 17.5/22.4/24.7% | 1.9/5.2% | 3 |

> window-size=8: misdecodes 172

> window-size=16: misdecodes 75

> window-size=32: misdecodes 21

### `TH-congestion` - no-congestion-scaling  `--scenario coastal`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.964 | 0.963 | 0.001 | - | - | 0.998 | 0.999 | 0.837 | 1.86x | 22.2/31.8/35.5% | 1.2/4.8% | 3 |
| True | 1 | 0.760 | 0.750 | 0.010 | - | - | 0.901 | 0.912 | 0.580 | 5.45x | 59.4/72.3/76.0% | 3.9/12.4% | 3 |

> no-congestion-scaling=True: queue drops 11.7% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 66

### `TH-congestion-input` - congestion-input  `--scenario coastal`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.513 | 0.506 | 0.006 | - | - | 0.617 | 0.619 | 0.263 | 4.06x | 14.8/21.6/29.8% | 1.3/5.2% | 3 |
| truesize | 1 | 0.539 | 0.532 | 0.007 | - | - | 0.638 | 0.639 | 0.275 | 3.05x | 11.0/17.1/23.6% | 1.0/4.2% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario coastal`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.966 | 0.965 | 0.001 | - | - | 1.000 | 1.000 | 0.847 | 1.79x | 21.4/30.7/34.1% | 1.2/4.6% | 3 |
| adaptive | 1 | 0.964 | 0.963 | 0.001 | - | - | 0.998 | 0.999 | 0.837 | 1.86x | 22.2/31.8/35.5% | 1.2/4.8% | 3 |

