# Sweep blocks-2026-09-10-5606890

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** coastal
- **seed base** 5606890 · seeds 5606890
- **blocks** 87 run
- **compute** 10.5 h of simulator time across every cell
- **generated** 2026-09-10T08:47:27+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>89 warnings</summary>

- AD-badrouters: role-placement=random: misdecodes 1
- AD-flooding: role-mix=all-routers: misdecodes 1
- AD-nomute: role-mix=all-routers: misdecodes 1
- AD-siting: siting-mix=local-typical: 3 archives requested, 2 placed - group on the placed count
- AD-siting: siting-mix=basement-heavy: decode_failures 2
- AD-worst: role-placement=inverse: decode_failures 1
- DB-hotstore-stress: max-num-nodes=10: decode_failures 52
- DB-hotstore-stress: max-num-nodes=120: decode_failures 1
- DB-hotstore-stress: max-num-nodes=250: decode_failures 2
- DB-warm: warm-num-nodes=0: queue drops 12.6% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 90
- DB-warm: warm-num-nodes=25: queue drops 12.6% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 90
- DB-warm: warm-num-nodes=100: queue drops 12.6% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 90
- DB-warm: warm-num-nodes=2000: queue drops 12.6% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 90
- DG-burst: burst-loss=0.2: decode_failures 29
- DG-burst: burst-loss=0.3: decode_failures 32
- DG-loss: extra-loss=0.2: misdecodes 1
- DG-outage: burst-loss=0.1: decode_failures 28
- DG-outage: burst-loss=0.2: decode_failures 36
- DG-outage: burst-loss=0.3: decode_failures 22
- LD-chatty-hops: broadcast-interval-s=300: queue drops 19.0% of transmissions - airtime here is measured through a cap
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 37
- LD-chatty: broadcast-interval-s=300: queue drops 15.1% of transmissions - airtime here is measured through a cap
- LD-chatty: broadcast-interval-s=300: decode_failures 20
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 12.6% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 90
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 23.9% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 92
- MS-density: nodes=40: decode_failures 12
- MS-density: nodes=90: misdecodes 1
- MS-density: nodes=150: misdecodes 1
- MS-hopscale: nodes=250: decode_failures 10
- MS-hopscale: nodes=500: decode_failures 1
- MS-oversubscribed: nodes=250: decode_failures 1
- MS-roles-fav: role-mix=baymesh-2026-08: misdecodes 1
- MS-siting: siting-mix=local-typical: 3 archives requested, 2 placed - group on the placed count
- MS-siting: siting-mix=event: decode_failures 8
- MS-stretch: stretch=1.5: decode_failures 27
- MS-stretch: stretch=2.0: decode_failures 7
- RF-bw500: preset=SHORT_TURBO: decode_failures 6
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 41
- RF-eu-presets: preset=SHORT_FAST: decode_failures 4
- RF-preset: preset=SHORT_FAST: decode_failures 4
- RF-preset: preset=LONG_MODERATE: decode_failures 1
- RF-preset-turbo: preset=EXTRA_SHORT_TURBO: decode_failures 9
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 6
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 27
- RF-stretch-duct: duct-per-hour=1.0: decode_failures 8
- RF-stretch-duct: slower: 7.13 s per simulated hour against 2.8 over 20 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-txpower: tx-power=22: decode_failures 25
- RF-txpower: tx-power=17: decode_failures 1
- SF-bucket-mode: bucket-mode=global: misdecodes 40
- SF-bucket-mode: bucket-mode=time: misdecodes 50
- SF-bucket-mode: bucket-mode=window: misdecodes 31
- SF-bucket-time: time-bucket-s=600: misdecodes 125
- SF-bucket-time: time-bucket-s=1800: misdecodes 50
- SF-bucket-time: time-bucket-s=3600: misdecodes 15
- SF-cadence: trigger=interval: misdecodes 26
- SF-cadence: trigger=aimd: misdecodes 4
- SF-cadence: trigger=bucket+interval: misdecodes 31
- SF-capacity-local: capacity=4: decode_failures 45
- SF-capacity: capacity=4: decode_failures 45
- SF-capacity-window: capacity=8: misdecodes 25
- SF-capacity-window: capacity=8: decode_failures 3
- SF-capacity-window: capacity=16: misdecodes 27
- SF-capacity-window: capacity=32: misdecodes 31
- SF-catchup: catch-up-hours=: misdecodes 31
- SF-catchup: catch-up-hours=02-06: decode_failures 3
- SF-catchup: faster: 3.02 s per simulated hour against 9.66 over 20 prior run(s) - 3.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-hops-flat: hops-apart=4: decode_failures 28
- SF-hops-spread: hops-apart=4: decode_failures 28
- SF-hops-spread: hops-apart=5: decode_failures 39
- SF-place-flat: place=spread: decode_failures 34
- SF-place-spread: place=spread: decode_failures 34
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 17
- SF-replay-order: replay-ordering=heard: misdecodes 26
- SF-servers-allrouters: servers=6: misdecodes 1
- SF-servers-flat: servers=8: misdecodes 1
- SF-servers-spread: servers=8: misdecodes 1
- SF-window-size: window-size=8: misdecodes 154
- SF-window-size: window-size=16: misdecodes 69
- SF-window-size: window-size=32: misdecodes 31
- TH-congestion-input: congestion-input=hotstore: decode_failures 1
- TH-congestion-input: congestion-input=truesize: decode_failures 5
- TH-congestion: no-congestion-scaling=True: queue drops 11.0% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 106

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `RF-stretch-duct` | 7.13 | 2.8 | 2.55x | 20 |
| `RF-bw500` | 4.63 | 2.44 | 1.90x | 20 |
| `RF-txpower` | 2.77 | 1.6 | 1.73x | 20 |
| `LD-chatty-hops` | 6.98 | 4.28 | 1.63x | 20 |
| `RF-preset-turbo` | 2.53 | 1.56 | 1.62x | 16 |
| `DM-mode` | 2.19 | 3.27 | 0.67x | 20 |
| `AD-siting` | 1.27 | 1.9 | 0.67x | 20 |
| `MS-hopscale` | 12 | 18 | 0.67x | 20 |
| `MS-oversubscribed` | 12.3 | 19 | 0.65x | 20 |
| `PR-dmmode-cr` | 1.64 | 2.57 | 0.64x | 20 |
| `RF-preset` | 1.71 | 3.01 | 0.57x | 20 |
| `AD-badrouters` | 1.19 | 2.13 | 0.56x | 20 |
| `SF-catchup` | 3.02 | 9.66 | 0.31x | 20 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.997 | 0.997 | 0.918 → 0.925 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.996 | 0.996 | 0.924 → 0.925 | 1x bytes_on_air | up | 2 |
| `RF-preset-turbo` | preset | **text** | 0.058 → 0.925 | 0.866 | 0.058 → 0.922 | 7.2x advert_bytes | up | 5 |
| `AD-siting` | siting-mix | **text** | 0.049 → 0.902 | 0.853 | 0.046 → 0.897 | 8.6x sr_bytes | down | 3 |
| `RF-txpower` | tx-power | **text** | 0.097 → 0.925 | 0.828 | 0.093 → 0.922 | 3.9x advert_bytes | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.156 → 0.948 | 0.792 | 0.138 → 0.875 | 86x sr_airtime | down | 4 |
| `MS-stretch` | stretch | **text** | 0.159 → 0.925 | 0.765 | 0.155 → 0.922 | 3.4x advert_bytes | down | 4 |
| `RF-bw500` | preset | **text** | 0.182 → 0.874 | 0.692 | 0.179 → 0.871 | 3x advert_bytes | up | 3 |
| `MS-hopscale` | nodes | **text** | 0.334 → 0.925 | 0.591 | 0.332 → 0.922 | 8.4x sr_bytes | down | 4 |
| `RF-eu-presets` | preset | **held** | 0.423 → 0.997 | 0.574 | 0.348 → 0.922 | 4.4x sr_airtime | up | 4 |
| `RF-preset` | preset | **held** | 0.423 → 0.997 | 0.574 | 0.348 → 0.922 | 5.4x sr_airtime | up | 3 |
| `MS-siting` | siting-mix | **held** | 0.472 → 0.998 | 0.527 | 0.482 → 0.976 | 13x sr_bytes | up | 4 |
| `MS-oversubscribed` | nodes | **text** | 0.336 → 0.832 | 0.496 | 0.334 → 0.825 | 5.2x bytes_on_air | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.505 → 0.840 | 0.335 | 0.496 → 0.827 | 1.7x sr_airtime | up | 2 |
| `MS-topology` | topology | **text** | 0.613 → 0.938 | 0.324 | 0.597 → 0.937 | 2x sr_bytes | up | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.618 → 0.938 | 0.320 | 0.604 → 0.936 | 11x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.610 → 0.925 | 0.315 | 0.584 → 0.922 | 2.6x sr_bytes | down | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.654 → 0.955 | 0.300 | 0.645 → 0.954 | 9.2x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.650 → 0.925 | 0.275 | 0.607 → 0.922 | 3.1x sr_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.510 → 0.747 | 0.237 | 0.335 → 0.552 | 5.3x sr_airtime | up | 3 |
| `MS-size` | nodes | **text** | 0.721 → 0.925 | 0.204 | 0.710 → 0.922 | 3.9x sr_bytes | down | 5 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.783 → 0.966 | 0.183 | 0.771 → 0.963 | 4.5x sr_airtime | down | 2 |
| `RT-hoplimit` | hop-limit | **text** | 0.794 → 0.955 | 0.161 | 0.773 → 0.955 | 2.8x sr_bytes | up | 4 |
| `RF-noise` | noise-profile | **text** | 0.769 → 0.925 | 0.156 | 0.764 → 0.922 | 1.3x sr_bytes | down | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.794 → 0.941 | 0.147 | 0.773 → 0.940 | 2.3x sr_bytes | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.794 → 0.925 | 0.131 | 0.773 → 0.922 | 1.7x sr_bytes | up | 2 |
| `SC-signing` | signature-policy | **text** | 0.805 → 0.925 | 0.119 | 0.805 → 0.922 | 1.3x sr_airtime | down | 3 |
| `MS-density` | nodes | **text** | 0.853 → 0.970 | 0.118 | 0.834 → 0.969 | 4.6x sr_airtime | up | 5 |
| `DG-loss` | extra-loss | **text** | 0.832 → 0.925 | 0.093 | 0.821 → 0.922 | 1.5x sr_bytes | down | 4 |
| `DB-hotstore` | max-num-nodes | **text** | 0.857 → 0.945 | 0.088 | 0.851 → 0.943 | 2.5x sr_airtime | up | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.688 → 0.774 | 0.086 | 0.678 → 0.764 | 1.3x sr_airtime | down | 2 |
| `SF-hops-spread` | hops-apart | **held** | 0.915 → 0.997 | 0.081 | 0.920 → 0.924 | 3x sr_bytes | down | 5 |
| `DB-platform` | platform-mix | **text** | 0.866 → 0.945 | 0.078 | 0.860 → 0.943 | 2.6x sr_airtime | down | 3 |
| `SF-place-flat` | place | **held** | 0.923 → 0.997 | 0.074 | 0.922 → 0.926 | 3.3x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.923 → 0.997 | 0.074 | 0.922 → 0.926 | 3.3x sr_bytes | up | 6 |
| `AD-flooding` | role-mix | **text** | 0.902 → 0.950 | 0.048 | 0.897 → 0.949 | 2.3x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.902 → 0.950 | 0.048 | 0.897 → 0.949 | 2.3x bytes_on_air | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.925 → 0.971 | 0.047 | 0.922 → 0.971 | 1.8x sr_bytes | up | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.904 → 0.946 | 0.042 | 0.897 → 0.945 | 5.5x sr_airtime | up | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.925 → 0.966 | 0.042 | 0.922 → 0.965 | 1.6x bytes_on_air | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.925 → 0.964 | 0.039 | 0.922 → 0.960 | 1.5x sr_bytes | up | 3 |
| `TH-congestion-input` | congestion-input | **held** | 0.739 → 0.777 | 0.038 | 0.545 → 0.578 | 1.4x sr_airtime | up | 2 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.960 → 0.997 | 0.037 | 0.922 → 0.922 | 26x sr_airtime | down | 3 |
| `MS-roles` | role-mix | **text** | 0.902 → 0.929 | 0.027 | 0.897 → 0.926 | 1.2x sr_bytes | down | 2 |
| `SF-cadence` | trigger | **held** | 0.971 → 0.997 | 0.026 | 0.906 → 0.924 | 15x sr_bytes | down | 4 |
| `RT-hopassign` | hop-assign | **text** | 0.899 → 0.925 | 0.025 | 0.893 → 0.922 | 1.2x sr_bytes | down | 2 |
| `SF-hops-flat` | hops-apart | **held** | 0.972 → 0.997 | 0.025 | 0.920 → 0.924 | 3x sr_bytes | down | 4 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.900 → 0.925 | 0.024 | 0.895 → 0.922 | 1.5x sr_airtime | down | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.925 → 0.941 | 0.017 | 0.922 → 0.941 | 3.4x bytes_on_air | down | 2 |
| `FW-mixed` | legacy-fraction | **held** | 0.981 → 0.997 | 0.016 | 0.922 → 0.935 | 2.1x bytes_on_air | down | 4 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.925 → 0.941 | 0.016 | 0.922 → 0.937 | 2.2x bytes_on_air | up | 4 |
| `RT-favourites` | favourite-routers | **text** | 0.932 → 0.947 | 0.016 | 0.929 → 0.947 | 1.1x bytes_on_air | up | 2 |
| `AD-worst` | role-placement | **text** | 0.735 → 0.748 | 0.013 | 0.721 → 0.739 | 1.1x sr_bytes | down | 2 |
| `MS-roles-fav` | role-mix | **text** | 0.931 → 0.944 | 0.013 | 0.927 → 0.942 | 1.2x sr_bytes | down | 2 |
| `FW-versions` | profile | **text** | 0.925 → 0.937 | 0.012 | 0.922 → 0.934 | 3.6x bytes_on_air | down | 5 |
| `SF-catchup` | catch-up-hours | **text** | 0.912 → 0.924 | 0.012 | 0.906 → 0.923 | 12x sr_bytes | up | 3 |
| `MS-router-late` | router-late-fraction | **text** | 0.924 → 0.936 | 0.012 | 0.922 → 0.933 | 1.3x bytes_on_air | up | 4 |
| `AD-badrouters` | role-placement | **text** | 0.891 → 0.902 | 0.011 | 0.884 → 0.897 | 1.1x advert_bytes | down | 3 |
| `DM-mode` | dm-mode | **text** | 0.902 → 0.911 | 0.010 | 0.902 → 0.911 | 1.3x sr_airtime | up | 3 |
| `SF-sr-retries` | sr-retries | **held** | 0.989 → 0.997 | 0.008 | 0.923 → 0.926 | 1.1x sr_bytes | down | 4 |
| `LD-diurnal` | diurnal | **text** | 0.925 → 0.932 | 0.008 | 0.922 → 0.930 | 1.3x sr_bytes | down | 3 |
| `SF-width` | short-id-bits | **text** | 0.920 → 0.928 | 0.008 | 0.917 → 0.926 | 3.1x advert_bytes | down | 4 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.929 → 0.936 | 0.007 | 0.914 → 0.923 | 1.1x sr_bytes | up | 2 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.990 → 0.997 | 0.007 | 0.918 → 0.921 | 5.7x advert_bytes | down | 3 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.922 → 0.928 | 0.006 | 0.919 → 0.925 | 1.1x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.922 → 0.928 | 0.006 | 0.919 → 0.925 | 1.1x sr_airtime | up | 4 |
| `SF-provide-transport` | provide-transport | **held** | 0.991 → 0.997 | 0.006 | 0.914 → 0.922 | 1.9x sr_airtime | down | 2 |
| `SF-servers-flat` | servers | **text** | 0.923 → 0.928 | 0.005 | 0.916 → 0.922 | 6.9x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **text** | 0.923 → 0.928 | 0.005 | 0.916 → 0.922 | 6.9x sr_bytes | up | 4 |
| `FW-firmware` | profile | **text** | 0.925 → 0.929 | 0.005 | 0.922 → 0.926 | 3.5x bytes_on_air | down | 2 |
| `SF-resolve` | resolve | **held** | 0.992 → 0.997 | 0.004 | 0.922 → 0.923 | 5.7x advert_bytes | = | 3 |
| `SF-window-size` | window-size | **text** | 0.922 → 0.926 | 0.004 | 0.917 → 0.924 | 5.5x advert_bytes | up | 3 |
| `SF-capacity` | capacity | **held** | 0.993 → 0.997 | 0.004 | 0.918 → 0.922 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.993 → 0.997 | 0.004 | 0.918 → 0.922 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-window` | capacity | **text** | 0.922 → 0.926 | 0.004 | 0.919 → 0.924 | 2.7x advert_bytes | up | 3 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.993 → 0.997 | 0.003 | 0.921 → 0.924 | 2.8x advert_bytes | down | 4 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.966 → 0.969 | 0.003 | 0.963 → 0.967 | 1.1x sr_airtime | down | 2 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.903 → 0.906 | 0.003 | 0.903 → 0.906 | 1x sr_airtime | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.966 → 0.969 | 0.003 | 0.963 → 0.966 | 1x sr_bytes | up | 2 |
| `PR-repeats` | extra-repeats | **held** | 0.994 → 0.997 | 0.002 | 0.922 → 0.923 | 1x sr_bytes | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.964 → 0.966 | 0.002 | 0.960 → 0.963 | 1.2x sr_airtime | down | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.925 → 0.926 | 0.002 | 0.922 → 0.923 | 1.2x sr_bytes | up | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.995 → 0.997 | 0.002 | 0.922 → 0.923 | 3.7x sr_airtime | down | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.987 → 0.988 | 0.001 | 0.906 → 0.906 | 1.1x sr_airtime | down | 2 |
| `SF-servers-allrouters` | servers | **text** | 0.924 → 0.925 | 0.000 | 0.922 → 0.923 | 2.3x sr_bytes | up | 2 |

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
| none | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| sprinkled | 1 | 0.961 | 0.959 | 0.002 | - | - | 0.993 | 0.993 | 0.833 | 1.23x | 21.1/26.9/29.0% | 1.7/5.3% | 3 |
| arms-race | 1 | 0.971 | 0.971 | 0.000 | - | - | 0.992 | 0.992 | 0.912 | 0.94x | 24.6/28.7/31.5% | 1.0/5.4% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario coastal`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 0.1 | 1 | 0.932 | 0.924 | 0.008 | - | - | 0.982 | 0.986 | 0.619 | 1.28x | 21.3/28.4/31.6% | 1.9/5.3% | 3 |
| 0.3 | 1 | 0.964 | 0.960 | 0.004 | - | - | 0.999 | 0.999 | 0.894 | 1.00x | 23.1/27.9/30.4% | 1.3/4.9% | 3 |

### `AD-badrouters` - role-placement  `--scenario coastal`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.902 | 0.897 | 0.004 | - | - | 0.982 | 0.983 | 0.545 | 1.31x | 18.5/28.2/32.5% | 2.3/5.3% | 3 |
| inverse | 1 | 0.891 | 0.884 | 0.007 | - | - | 0.986 | 0.987 | 0.460 | 1.26x | 17.1/23.9/27.9% | 2.3/4.1% | 3 |
| random | 1 | 0.891 | 0.885 | 0.006 | - | - | 0.983 | 0.984 | 0.445 | 1.30x | 17.5/23.9/28.8% | 2.3/4.6% | 3 |

> role-placement=random: misdecodes 1

### `AD-flooding` - role-mix  `--scenario coastal`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.902 | 0.897 | 0.004 | - | - | 0.982 | 0.983 | 0.545 | 1.31x | 18.5/28.2/32.5% | 2.3/5.3% | 3 |
| all-routers | 1 | 0.950 | 0.949 | 0.001 | - | - | 0.997 | 0.997 | 0.515 | 2.96x | 39.8/49.8/52.6% | 4.8/5.4% | 3 |

> role-mix=all-routers: misdecodes 1

### `AD-nomute` - role-mix  `--scenario coastal`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.902 | 0.897 | 0.004 | - | - | 0.982 | 0.983 | 0.545 | 1.31x | 18.5/28.2/32.5% | 2.3/5.3% | 3 |
| no-mute | 1 | 0.931 | 0.929 | 0.003 | - | - | 0.993 | 0.993 | 0.451 | 1.41x | 18.7/26.9/30.6% | 2.1/5.3% | 3 |
| all-routers | 1 | 0.950 | 0.949 | 0.001 | - | - | 0.997 | 0.997 | 0.515 | 2.96x | 39.8/49.8/52.6% | 4.8/5.4% | 3 |

> role-mix=all-routers: misdecodes 1

### `AD-siting` - siting-mix  `--scenario coastal`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.902 | 0.897 | 0.004 | - | - | 0.982 | 0.983 | 0.545 | 1.31x | 18.5/28.2/32.5% | 2.3/5.3% | 3 |
| local-typical | 1 | 0.655 | 0.655 | 0.000 | - | - | 0.403 | 0.805 | 0.000 | 1.40x | 13.9/27.6/32.0% | 2.3/5.5% | 2 |
| basement-heavy | 1 | 0.049 | 0.046 | 0.003 | - | - | 0.213 | 0.236 | 0.000 | 0.47x | 0.7/5.8/8.5% | 0.2/2.4% | 3 |

> siting-mix=local-typical: 3 archives requested, 2 placed - group on the placed count

> siting-mix=basement-heavy: decode_failures 2

### `AD-worst` - role-placement  `--scenario coastal`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.748 | 0.739 | 0.010 | - | - | 0.921 | 0.922 | 0.000 | 2.21x | 14.7/26.8/32.8% | 1.7/5.7% | 3 |
| inverse | 1 | 0.735 | 0.721 | 0.014 | - | - | 0.917 | 0.917 | 0.000 | 2.17x | 13.7/24.1/29.3% | 1.7/3.5% | 3 |

> role-placement=inverse: decode_failures 1

### `BL-control` - protocol  `--scenario coastal`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.925 | 0.925 | 0.000 | - | - | 0 | 0.000 | 0.530 | 1.41x | 19.8/29.4/33.0% | 2.1/5.2% | 3 |
| sr | 1 | 0.931 | 0.924 | 0.007 | - | - | 0.996 | 0.997 | 0.497 | 1.45x | 20.2/30.0/33.9% | 2.2/5.4% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario coastal`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.857 | 0.851 | 0.006 | - | - | 0.952 | 0.959 | 0.456 | 3.49x | 46.1/68.3/73.5% | 5.1/10.2% | 3 |
| 100 | 1 | 0.945 | 0.943 | 0.002 | - | - | 0.995 | 0.995 | 0.550 | 1.78x | 24.4/39.6/44.5% | 2.5/5.4% | 3 |
| 120 | 1 | 0.945 | 0.943 | 0.002 | - | - | 0.995 | 0.995 | 0.550 | 1.78x | 24.4/39.6/44.5% | 2.5/5.4% | 3 |
| 250 | 1 | 0.945 | 0.943 | 0.002 | - | - | 0.995 | 0.995 | 0.550 | 1.78x | 24.4/39.6/44.5% | 2.5/5.4% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario coastal`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.345 | 0.335 | 0.010 | - | - | 0.510 | 0.548 | 0.136 | 11.59x | 44.6/56.2/69.0% | 4.1/10.6% | 3 |
| 120 | 1 | 0.559 | 0.545 | 0.014 | - | - | 0.739 | 0.741 | 0.187 | 4.39x | 17.4/25.1/33.1% | 1.5/5.2% | 3 |
| 250 | 1 | 0.567 | 0.552 | 0.014 | - | - | 0.747 | 0.748 | 0.192 | 4.26x | 16.9/24.1/32.1% | 1.4/4.9% | 3 |

> max-num-nodes=10: decode_failures 52

> max-num-nodes=120: decode_failures 1

> max-num-nodes=250: decode_failures 2

### `DB-platform` - platform-mix  `--scenario coastal`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.945 | 0.943 | 0.002 | - | - | 0.995 | 0.995 | 0.550 | 1.78x | 24.4/39.6/44.5% | 2.5/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.945 | 0.943 | 0.002 | - | - | 0.995 | 0.995 | 0.550 | 1.78x | 24.4/39.6/44.5% | 2.5/5.4% | 3 |
| constrained | 1 | 0.866 | 0.860 | 0.006 | - | - | 0.960 | 0.962 | 0.433 | 3.49x | 46.3/68.2/73.6% | 5.1/10.2% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario coastal`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.774 | 0.764 | 0.010 | - | - | 0.867 | 0.930 | 0.577 | 5.55x | 61.6/72.3/75.4% | 3.6/14.1% | 3 |
| 25 | 1 | 0.774 | 0.764 | 0.010 | - | - | 0.867 | 0.930 | 0.577 | 5.55x | 61.6/72.3/75.4% | 3.6/14.1% | 3 |
| 100 | 1 | 0.774 | 0.764 | 0.010 | - | - | 0.867 | 0.930 | 0.577 | 5.55x | 61.6/72.3/75.4% | 3.6/14.1% | 3 |
| 2000 | 1 | 0.774 | 0.764 | 0.010 | - | - | 0.867 | 0.930 | 0.577 | 5.55x | 61.6/72.3/75.4% | 3.6/14.1% | 3 |

> warm-num-nodes=0: queue drops 12.6% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 90

> warm-num-nodes=25: queue drops 12.6% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 90

> warm-num-nodes=100: queue drops 12.6% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 90

> warm-num-nodes=2000: queue drops 12.6% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 90

### `DG-burst` - burst-loss  `--scenario coastal`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 0.1 | 1 | 0.840 | 0.828 | 0.012 | - | - | 0.983 | 0.990 | 0.405 | 1.39x | 19.6/29.2/32.8% | 2.1/5.0% | 3 |
| 0.2 | 1 | 0.747 | 0.721 | 0.026 | - | - | 0.946 | 0.973 | 0.337 | 1.29x | 18.7/28.1/31.4% | 2.0/4.5% | 3 |
| 0.3 | 1 | 0.650 | 0.607 | 0.043 | - | - | 0.895 | 0.925 | 0.256 | 1.18x | 17.3/26.2/29.6% | 1.8/4.1% | 3 |

> burst-loss=0.2: decode_failures 29

> burst-loss=0.3: decode_failures 32

### `DG-loss` - extra-loss  `--scenario coastal`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 0.1 | 1 | 0.908 | 0.904 | 0.004 | - | - | 0.994 | 0.995 | 0.437 | 1.51x | 21.1/31.2/34.8% | 2.3/5.3% | 3 |
| 0.2 | 1 | 0.880 | 0.873 | 0.007 | - | - | 0.987 | 0.988 | 0.388 | 1.58x | 22.5/33.2/36.6% | 2.5/5.3% | 3 |
| 0.3 | 1 | 0.832 | 0.821 | 0.011 | - | - | 0.969 | 0.971 | 0.330 | 1.59x | 22.6/33.7/37.2% | 2.5/5.0% | 3 |

> extra-loss=0.2: misdecodes 1

### `DG-outage` - burst-loss  `--scenario coastal`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 0.1 | 1 | 0.828 | 0.819 | 0.009 | - | - | 0.968 | 0.989 | 0.408 | 1.37x | 19.5/29.2/33.0% | 2.1/5.1% | 3 |
| 0.2 | 1 | 0.720 | 0.704 | 0.017 | - | - | 0.886 | 0.954 | 0.331 | 1.29x | 18.8/28.1/31.6% | 2.0/4.7% | 3 |
| 0.3 | 1 | 0.610 | 0.584 | 0.026 | - | - | 0.811 | 0.921 | 0.242 | 1.19x | 17.3/25.9/29.5% | 1.8/4.1% | 3 |

> burst-loss=0.1: decode_failures 28

> burst-loss=0.2: decode_failures 36

> burst-loss=0.3: decode_failures 22

### `DM-mode` - dm-mode  `--scenario coastal`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.902 | 0.902 | 0.000 | - | - | 0.991 | 0.992 | 0.484 | 1.93x | 26.8/39.7/44.6% | 3.0/7.3% | 3 |
| directed-with-late-flood | 1 | 0.906 | 0.906 | 0.000 | - | - | 0.988 | 0.991 | 0.489 | 1.76x | 24.7/36.8/41.5% | 2.7/6.7% | 3 |
| m4-early-flood | 1 | 0.911 | 0.911 | 0.000 | - | - | 0.997 | 0.997 | 0.497 | 1.75x | 24.5/36.6/41.1% | 2.7/6.7% | 3 |

### `FW-firmware` - profile  `--scenario coastal`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.929 | 0.926 | 0.003 | - | - | 0.996 | 0.997 | 0.548 | 0.74x | 10.0/13.2/14.6% | 1.1/1.9% | 3 |
| 2.8 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario coastal`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 0.25 | 1 | 0.939 | 0.935 | 0.004 | - | - | 0.995 | 0.996 | 0.637 | 1.27x | 17.5/24.4/28.3% | 1.9/4.8% | 3 |
| 0.5 | 1 | 0.929 | 0.926 | 0.003 | - | - | 0.981 | 0.981 | 0.714 | 1.06x | 15.1/19.4/22.5% | 1.7/4.1% | 3 |
| 0.75 | 1 | 0.929 | 0.924 | 0.004 | - | - | 0.984 | 0.984 | 0.654 | 0.97x | 13.1/17.0/18.3% | 1.5/3.6% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario coastal`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 0.25 | 1 | 0.941 | 0.937 | 0.003 | - | - | 0.995 | 0.995 | 0.651 | 1.24x | 17.2/24.5/27.9% | 1.9/4.8% | 3 |
| 0.5 | 1 | 0.932 | 0.929 | 0.003 | - | - | 0.989 | 0.990 | 0.693 | 1.03x | 15.2/19.1/22.2% | 1.5/4.1% | 3 |
| 0.75 | 1 | 0.929 | 0.924 | 0.006 | - | - | 0.984 | 0.985 | 0.638 | 0.93x | 12.9/16.6/18.1% | 1.5/3.6% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario coastal`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.941 | 0.941 | 0.001 | - | - | 0.998 | 0.998 | 0.508 | 0.75x | 10.8/16.7/19.3% | 1.1/3.0% | 3 |
| signing=true | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |

### `FW-versions` - profile  `--scenario coastal`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.930 | 0.927 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 0.72x | 10.3/14.3/15.9% | 1.1/2.5% | 3 |
| 2.5 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.994 | 0.994 | 0.536 | 0.75x | 10.6/14.5/16.1% | 1.2/2.5% | 3 |
| 2.6 | 1 | 0.929 | 0.926 | 0.003 | - | - | 0.995 | 0.996 | 0.519 | 0.71x | 10.4/14.3/16.0% | 1.1/2.5% | 3 |
| 2.7 | 1 | 0.937 | 0.934 | 0.003 | - | - | 0.995 | 0.996 | 0.521 | 0.73x | 10.8/15.3/17.5% | 1.1/3.2% | 3 |
| 2.8 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario coastal`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.938 | 0.936 | 0.002 | - | - | 0.998 | 0.998 | 0.525 | 0.98x | 13.6/20.1/22.6% | 1.5/3.6% | 3 |
| 900 | 1 | 0.904 | 0.897 | 0.007 | - | - | 0.995 | 0.997 | 0.460 | 2.35x | 32.4/48.0/53.4% | 3.6/8.7% | 3 |
| 300 | 1 | 0.618 | 0.604 | 0.014 | - | - | 0.740 | 0.877 | 0.263 | 4.88x | 61.2/76.5/80.8% | 7.6/15.8% | 3 |

> broadcast-interval-s=300: queue drops 15.1% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 20

### `LD-chatty-hops` - broadcast-interval-s  `--scenario coastal`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.955 | 0.954 | 0.001 | - | - | 0.998 | 0.998 | 0.553 | 1.00x | 13.8/20.0/22.3% | 1.5/3.5% | 3 |
| 900 | 1 | 0.915 | 0.912 | 0.003 | - | - | 0.982 | 0.983 | 0.528 | 2.69x | 36.0/51.6/56.4% | 4.2/9.1% | 3 |
| 300 | 1 | 0.654 | 0.645 | 0.010 | - | - | 0.784 | 0.863 | 0.315 | 5.24x | 63.6/76.7/80.8% | 8.5/15.5% | 3 |

> broadcast-interval-s=300: queue drops 19.0% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 37

### `LD-diurnal` - diurnal  `--scenario coastal`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.932 | 0.930 | 0.002 | - | - | 0.997 | 0.997 | 0.530 | 1.37x | 19.0/28.3/31.9% | 2.1/5.1% | 3 |
| sinusoid | 1 | 0.930 | 0.928 | 0.002 | - | - | 0.997 | 0.997 | 0.486 | 1.30x | 18.3/27.0/30.3% | 2.0/4.8% | 3 |
| commuter | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario coastal`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.904 | 0.897 | 0.007 | - | - | 0.995 | 0.997 | 0.460 | 2.35x | 32.4/48.0/53.4% | 3.6/8.7% | 3 |
| 3600 | 1 | 0.938 | 0.936 | 0.002 | - | - | 0.998 | 0.998 | 0.525 | 0.98x | 13.6/20.1/22.6% | 1.5/3.6% | 3 |
| 10800 | 1 | 0.946 | 0.945 | 0.001 | - | - | 1.000 | 1.000 | 0.568 | 0.65x | 9.0/13.2/14.7% | 1.0/2.3% | 3 |
| 43200 | 1 | 0.946 | 0.945 | 0.001 | - | - | 0.997 | 0.997 | 0.563 | 0.47x | 6.6/9.7/10.8% | 0.8/1.7% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario coastal`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 0.25 | 1 | 0.924 | 0.921 | 0.003 | - | - | 0.995 | 0.995 | 0.474 | 1.54x | 21.4/31.8/35.8% | 2.4/5.7% | 3 |
| 1.0 | 1 | 0.914 | 0.910 | 0.004 | - | - | 0.993 | 0.994 | 0.468 | 1.71x | 23.8/35.4/40.0% | 2.6/6.4% | 3 |
| 4.0 | 1 | 0.900 | 0.895 | 0.005 | - | - | 0.992 | 0.992 | 0.450 | 2.15x | 30.1/44.9/50.6% | 3.3/8.3% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario coastal`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.774 | 0.764 | 0.010 | - | - | 0.867 | 0.930 | 0.577 | 5.55x | 61.6/72.3/75.4% | 3.6/14.1% | 3 |
| 1.0 | 1 | 0.688 | 0.678 | 0.010 | - | - | 0.783 | 0.875 | 0.476 | 6.11x | 65.9/74.9/77.8% | 4.1/15.1% | 3 |

> traceroute-per-hour=0.0: queue drops 12.6% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 90

> traceroute-per-hour=1.0: queue drops 23.9% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 92

### `MS-density` - nodes  `--scenario coastal`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.853 | 0.834 | 0.018 | - | - | 0.923 | 0.947 | 0.486 | 1.61x | 24.1/32.3/39.2% | 3.8/7.5% | 3 |
| 60 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 90 | 1 | 0.965 | 0.962 | 0.003 | - | - | 0.996 | 0.996 | 0.730 | 1.55x | 20.3/29.5/35.4% | 1.3/5.2% | 3 |
| 120 | 1 | 0.966 | 0.963 | 0.003 | - | - | 1.000 | 1.000 | 0.876 | 1.90x | 23.9/30.6/34.7% | 1.2/5.3% | 3 |
| 150 | 1 | 0.970 | 0.969 | 0.002 | - | - | 0.999 | 0.999 | 0.846 | 2.48x | 30.1/43.8/50.6% | 1.2/5.5% | 3 |

> nodes=40: decode_failures 12

> nodes=90: misdecodes 1

> nodes=150: misdecodes 1

### `MS-hopscale` - nodes  `--scenario coastal`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 120 | 1 | 0.830 | 0.823 | 0.007 | - | - | 0.930 | 0.931 | 0.474 | 2.08x | 15.7/22.4/28.8% | 1.5/5.0% | 3 |
| 250 | 1 | 0.554 | 0.541 | 0.014 | - | - | 0.738 | 0.739 | 0.194 | 4.75x | 19.0/27.4/36.3% | 1.6/5.6% | 3 |
| 500 | 1 | 0.334 | 0.332 | 0.002 | - | - | 0.463 | 0.464 | 0.086 | 10.31x | 19.3/32.9/55.5% | 1.8/5.8% | 3 |

> nodes=250: decode_failures 10

> nodes=500: decode_failures 1

### `MS-oversubscribed` - nodes  `--scenario coastal`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.832 | 0.825 | 0.007 | - | - | 0.933 | 0.933 | 0.480 | 1.88x | 14.2/20.4/26.0% | 1.3/4.5% | 3 |
| 250 | 1 | 0.559 | 0.545 | 0.014 | - | - | 0.739 | 0.741 | 0.187 | 4.39x | 17.4/25.1/33.1% | 1.5/5.2% | 3 |
| 500 | 1 | 0.336 | 0.334 | 0.002 | - | - | 0.462 | 0.462 | 0.085 | 9.65x | 18.1/30.4/52.7% | 1.6/5.4% | 3 |

> nodes=250: decode_failures 1

### `MS-roles` - role-mix  `--scenario coastal`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.929 | 0.926 | 0.003 | - | - | 0.991 | 0.991 | 0.488 | 1.43x | 20.1/30.0/33.6% | 2.2/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.902 | 0.897 | 0.004 | - | - | 0.982 | 0.983 | 0.545 | 1.31x | 18.5/28.2/32.5% | 2.3/5.3% | 3 |

### `MS-roles-fav` - role-mix  `--scenario coastal`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.944 | 0.942 | 0.002 | - | - | 0.997 | 0.997 | 0.493 | 1.48x | 20.8/30.5/33.8% | 2.3/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.931 | 0.927 | 0.003 | - | - | 0.987 | 0.987 | 0.645 | 1.47x | 20.7/32.5/37.0% | 2.6/5.3% | 3 |

> role-mix=baymesh-2026-08: misdecodes 1

### `MS-router-late` - router-late-fraction  `--scenario coastal`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 0.05 | 1 | 0.934 | 0.933 | 0.001 | - | - | 0.997 | 0.997 | 0.485 | 1.57x | 22.0/34.9/39.8% | 2.4/5.3% | 3 |
| 0.1 | 1 | 0.924 | 0.923 | 0.002 | - | - | 0.992 | 0.992 | 0.483 | 1.69x | 22.9/38.6/44.6% | 2.4/5.3% | 3 |
| 0.2 | 1 | 0.936 | 0.933 | 0.003 | - | - | 0.997 | 0.997 | 0.463 | 1.91x | 27.2/43.7/48.2% | 2.7/5.3% | 3 |

### `MS-siting` - siting-mix  `--scenario coastal`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| local-typical | 1 | 0.796 | 0.796 | 0.000 | - | - | 0.472 | 0.944 | 0.000 | 1.68x | 17.1/30.3/35.5% | 2.7/5.4% | 2 |
| event | 1 | 0.515 | 0.482 | 0.033 | - | - | 0.674 | 0.701 | 0.000 | 1.63x | 9.2/16.7/23.2% | 2.6/4.9% | 3 |
| backbone | 1 | 0.977 | 0.976 | 0.002 | - | - | 0.998 | 0.999 | 0.914 | 1.16x | 31.5/39.4/41.5% | 1.4/5.6% | 3 |

> siting-mix=local-typical: 3 archives requested, 2 placed - group on the placed count

> siting-mix=event: decode_failures 8

### `MS-size` - nodes  `--scenario coastal`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.915 | 0.910 | 0.005 | - | - | 0.963 | 0.965 | 0.547 | 1.44x | 29.4/36.4/42.9% | 2.9/8.1% | 3 |
| 60 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 90 | 1 | 0.871 | 0.860 | 0.012 | - | - | 0.963 | 0.965 | 0.601 | 1.65x | 16.1/21.8/25.5% | 1.6/4.9% | 3 |
| 120 | 1 | 0.830 | 0.823 | 0.007 | - | - | 0.930 | 0.931 | 0.474 | 2.08x | 15.7/22.4/28.8% | 1.5/5.0% | 3 |
| 150 | 1 | 0.721 | 0.710 | 0.011 | - | - | 0.879 | 0.879 | 0.418 | 2.70x | 16.1/22.6/27.0% | 1.6/5.0% | 3 |

### `MS-stretch` - stretch  `--scenario coastal`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 1.25 | 1 | 0.773 | 0.769 | 0.005 | - | - | 0.921 | 0.923 | 0.456 | 1.47x | 13.8/22.5/28.3% | 2.2/5.4% | 3 |
| 1.5 | 1 | 0.505 | 0.496 | 0.009 | - | - | 0.661 | 0.721 | 0.169 | 1.46x | 10.5/19.2/24.7% | 2.2/5.0% | 3 |
| 2.0 | 1 | 0.159 | 0.155 | 0.004 | - | - | 0.311 | 0.325 | 0.000 | 1.02x | 5.2/11.1/14.1% | 1.5/4.3% | 3 |

> stretch=1.5: decode_failures 27

> stretch=2.0: decode_failures 7

### `MS-topology` - topology  `--scenario coastal`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| clustered | 1 | 0.914 | 0.912 | 0.002 | - | - | 0.948 | 0.948 | 0.284 | 1.10x | 24.4/35.6/36.7% | 1.3/5.3% | 3 |
| corridor | 1 | 0.613 | 0.597 | 0.016 | - | - | 0.749 | 0.749 | 0.325 | 1.21x | 15.6/22.5/24.1% | 1.6/5.6% | 3 |
| hub | 1 | 0.938 | 0.937 | 0.001 | - | - | 0.961 | 0.961 | 0.820 | 1.17x | 28.9/36.8/38.4% | 1.6/5.4% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario coastal`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.906 | 0.906 | 0.000 | - | - | 0.988 | 0.991 | 0.489 | 1.76x | 24.7/36.8/41.5% | 2.7/6.7% | 3 |
| True | 1 | 0.906 | 0.906 | 0.000 | - | - | 0.987 | 0.991 | 0.478 | 1.76x | 24.5/36.7/41.1% | 2.7/6.7% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario coastal`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.906 | 0.906 | 0.000 | - | - | 0.987 | 0.991 | 0.478 | 1.76x | 24.5/36.7/41.1% | 2.7/6.7% | 3 |
| m4-early-flood | 1 | 0.903 | 0.903 | 0.000 | - | - | 0.989 | 0.992 | 0.469 | 1.74x | 24.3/36.2/40.9% | 2.7/6.6% | 3 |

### `PR-protocol` - protocol  `--scenario coastal`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.925 | 0.925 | 0.000 | - | - | 0 | 0.000 | 0.530 | 1.41x | 19.8/29.4/33.0% | 2.1/5.2% | 3 |
| chain | 1 | 0.919 | 0.918 | 0.001 | - | - | 0.972 | 0.995 | 0.490 | 1.63x | 22.8/33.6/37.9% | 2.5/6.1% | 3 |
| sr | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |

### `PR-repeats` - extra-repeats  `--scenario coastal`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| True | 1 | 0.926 | 0.923 | 0.003 | - | - | 0.994 | 0.995 | 0.514 | 1.45x | 20.3/30.1/33.7% | 2.2/5.4% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario coastal`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.966 | 0.963 | 0.003 | - | - | 1.000 | 1.000 | 0.876 | 1.90x | 23.9/30.6/34.7% | 1.2/5.3% | 3 |
| True | 1 | 0.969 | 0.966 | 0.002 | - | - | 1.000 | 1.000 | 0.880 | 1.88x | 23.4/29.9/33.8% | 1.2/5.2% | 3 |

### `RF-bw500` - preset  `--scenario coastal`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.182 | 0.179 | 0.003 | - | - | 0.339 | 0.349 | 0.000 | 0.05x | 0.3/0.6/0.8% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.550 | 0.544 | 0.006 | - | - | 0.760 | 0.806 | 0.000 | 0.32x | 2.2/4.8/6.2% | 0.5/1.2% | 3 |
| LONG_TURBO | 1 | 0.874 | 0.871 | 0.003 | - | - | 0.964 | 0.964 | 0.367 | 1.50x | 16.1/24.8/27.7% | 2.3/5.0% | 3 |

> preset=SHORT_TURBO: decode_failures 6

> preset=MEDIUM_TURBO: decode_failures 41

### `RF-duct` - duct-per-hour  `--scenario coastal`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 0.25 | 1 | 0.935 | 0.932 | 0.003 | - | - | 0.997 | 0.997 | 0.588 | 1.18x | 20.4/28.6/32.0% | 1.7/5.2% | 3 |
| 1.0 | 1 | 0.966 | 0.965 | 0.002 | - | - | 0.999 | 0.999 | 0.843 | 0.89x | 26.9/32.9/34.0% | 1.0/5.4% | 3 |

### `RF-eu-presets` - preset  `--scenario coastal`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.351 | 0.348 | 0.003 | - | - | 0.423 | 0.588 | 0.000 | 0.15x | 1.0/2.0/2.6% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| LITE_FAST | 1 | 0.906 | 0.903 | 0.004 | - | - | 0.995 | 0.995 | 0.388 | 1.14x | 13.8/21.1/23.9% | 1.8/4.1% | 3 |
| NARROW_SLOW | 1 | 0.904 | 0.900 | 0.003 | - | - | 0.995 | 0.996 | 0.360 | 1.38x | 17.4/26.8/30.3% | 2.2/5.2% | 3 |

> preset=SHORT_FAST: decode_failures 4

### `RF-noise` - noise-profile  `--scenario coastal`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| temporal | 1 | 0.872 | 0.865 | 0.007 | - | - | 0.985 | 0.988 | 0.402 | 1.48x | 20.2/30.0/33.4% | 2.3/5.3% | 3 |
| transient | 1 | 0.919 | 0.916 | 0.003 | - | - | 0.994 | 0.995 | 0.492 | 1.47x | 20.4/30.2/34.0% | 2.3/5.4% | 3 |
| periodic | 1 | 0.769 | 0.764 | 0.005 | - | - | 0.843 | 0.846 | 0.354 | 1.36x | 19.2/28.4/31.7% | 2.1/4.7% | 3 |

### `RF-preset` - preset  `--scenario coastal`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.351 | 0.348 | 0.003 | - | - | 0.423 | 0.588 | 0.000 | 0.15x | 1.0/2.0/2.6% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| LONG_MODERATE | 1 | 0.842 | 0.833 | 0.009 | - | - | 0.926 | 0.926 | 0.633 | 3.76x | 57.6/71.5/73.8% | 5.8/12.3% | 3 |

> preset=SHORT_FAST: decode_failures 4

> preset=LONG_MODERATE: decode_failures 1

### `RF-preset-turbo` - preset  `--scenario coastal`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.058 | 0.058 | 0.001 | - | - | 0.162 | 0.169 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.182 | 0.179 | 0.003 | - | - | 0.339 | 0.349 | 0.000 | 0.05x | 0.3/0.6/0.8% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| LONG_TURBO | 1 | 0.874 | 0.871 | 0.003 | - | - | 0.964 | 0.964 | 0.367 | 1.50x | 16.1/24.8/27.7% | 2.3/5.0% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.914 | 0.910 | 0.004 | - | - | 0.991 | 0.992 | 0.394 | 2.04x | 26.6/37.3/41.5% | 3.1/7.2% | 3 |

> preset=EXTRA_SHORT_TURBO: decode_failures 9

> preset=SHORT_TURBO: decode_failures 6

### `RF-pulse` - noise-pulse-interval-ms  `--scenario coastal`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.878 | 0.875 | 0.003 | - | - | 0.948 | 0.950 | 0.450 | 1.42x | 19.9/29.5/33.1% | 2.2/5.2% | 3 |
| 10000 | 1 | 0.769 | 0.764 | 0.005 | - | - | 0.843 | 0.846 | 0.354 | 1.36x | 19.2/28.4/31.7% | 2.1/4.7% | 3 |
| 4000 | 1 | 0.525 | 0.522 | 0.003 | - | - | 0.584 | 0.621 | 0.184 | 1.14x | 16.4/24.3/27.2% | 1.8/3.6% | 3 |
| 2000 | 1 | 0.138 | 0.138 | 0.000 | - | - | 0.156 | 0.223 | 0.034 | 0.78x | 11.7/17.8/20.2% | 1.2/2.1% | 3 |

### `RF-stretch-duct` - duct-per-hour  `--scenario coastal`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.505 | 0.496 | 0.009 | - | - | 0.661 | 0.721 | 0.169 | 1.46x | 10.5/19.2/24.7% | 2.2/5.0% | 3 |
| 1.0 | 1 | 0.840 | 0.827 | 0.014 | - | - | 0.913 | 0.925 | 0.700 | 1.02x | 20.3/26.6/29.7% | 1.4/5.0% | 3 |

> duct-per-hour=0.0: decode_failures 27

> duct-per-hour=1.0: decode_failures 8

> slower: 7.13 s per simulated hour against 2.8 over 20 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-txpower` - tx-power  `--scenario coastal`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 22 | 1 | 0.506 | 0.500 | 0.005 | - | - | 0.663 | 0.738 | 0.089 | 1.43x | 9.8/19.1/24.2% | 2.2/5.0% | 3 |
| 17 | 1 | 0.169 | 0.167 | 0.003 | - | - | 0.318 | 0.331 | 0.000 | 1.04x | 5.7/12.2/15.8% | 1.4/4.3% | 3 |
| 14 | 1 | 0.097 | 0.093 | 0.004 | - | - | 0.275 | 0.277 | 0.000 | 0.72x | 2.7/7.6/10.3% | 1.0/3.5% | 3 |

> tx-power=22: decode_failures 25

> tx-power=17: decode_failures 1

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario coastal`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.966 | 0.963 | 0.003 | - | - | 1.000 | 1.000 | 0.876 | 1.90x | 23.9/30.6/34.7% | 1.2/5.3% | 3 |
| True | 1 | 0.964 | 0.960 | 0.004 | - | - | 1.000 | 1.000 | 0.876 | 2.22x | 27.4/34.4/38.2% | 1.4/5.9% | 3 |

### `RT-favourites` - favourite-routers  `--scenario coastal`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.932 | 0.929 | 0.002 | - | - | 0.996 | 0.996 | 0.455 | 1.52x | 21.7/33.1/37.9% | 2.3/5.3% | 3 |
| True | 1 | 0.947 | 0.947 | 0.001 | - | - | 0.997 | 0.997 | 0.533 | 1.63x | 23.1/34.4/39.4% | 2.4/5.4% | 3 |

### `RT-hopassign` - hop-assign  `--scenario coastal`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| random | 1 | 0.899 | 0.893 | 0.006 | - | - | 0.991 | 0.991 | 0.384 | 1.42x | 20.0/29.6/33.2% | 2.1/5.3% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario coastal`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.794 | 0.773 | 0.020 | - | - | 0.980 | 0.983 | 0.201 | 1.08x | 15.6/24.7/28.6% | 1.6/4.8% | 3 |
| 7 | 1 | 0.941 | 0.940 | 0.001 | - | - | 0.989 | 0.989 | 0.576 | 1.53x | 21.1/30.6/34.3% | 2.4/5.4% | 3 |
| 15 | 1 | 0.955 | 0.955 | 0.000 | - | - | 0.994 | 0.994 | 0.574 | 1.55x | 21.5/31.2/34.8% | 2.4/5.5% | 3 |
| 32 | 1 | 0.947 | 0.946 | 0.000 | - | - | 0.985 | 0.985 | 0.574 | 1.53x | 21.2/30.9/34.4% | 2.4/5.4% | 3 |

### `RT-hopspread` - hop-limit  `--scenario coastal`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.794 | 0.773 | 0.020 | - | - | 0.980 | 0.983 | 0.201 | 1.08x | 15.6/24.7/28.6% | 1.6/4.8% | 3 |
| 5 | 1 | 0.904 | 0.901 | 0.003 | - | - | 0.987 | 0.987 | 0.441 | 1.43x | 19.8/29.5/33.2% | 2.2/5.3% | 3 |
| 7 | 1 | 0.941 | 0.940 | 0.001 | - | - | 0.989 | 0.989 | 0.576 | 1.53x | 21.1/30.6/34.3% | 2.4/5.4% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario coastal`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| KNOWN_ONLY | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.922 | 0.922 | 0.000 | - | - | 0.960 | 0.994 | 0.491 | 1.39x | 19.5/29.0/32.6% | 2.2/5.2% | 3 |

### `RT-spread` - hop-spread  `--scenario coastal`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.794 | 0.773 | 0.020 | - | - | 0.980 | 0.983 | 0.201 | 1.08x | 15.6/24.7/28.6% | 1.6/4.8% | 3 |
| True | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |

### `SC-signing` - signature-policy  `--scenario coastal`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| BALANCED | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| STRICT | 1 | 0.805 | 0.805 | 0.000 | - | - | 0.883 | 0.884 | 0.348 | 1.61x | 22.4/33.0/36.9% | 2.5/5.8% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario coastal`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| dm | 1 | 0.925 | 0.923 | 0.003 | - | - | 0.995 | 0.996 | 0.481 | 1.42x | 19.8/29.6/33.3% | 2.2/5.4% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario coastal`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.926 | 0.923 | 0.003 | - | - | 0.995 | 0.996 | 0.508 | 1.45x | 20.2/30.1/33.8% | 2.3/5.4% | 3 |
| local | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| time | 1 | 0.925 | 0.921 | 0.003 | - | - | 0.994 | 0.996 | 0.498 | 1.49x | 20.6/30.6/34.4% | 2.3/5.6% | 3 |
| window | 1 | 0.926 | 0.924 | 0.002 | - | - | 0.993 | 0.993 | 0.493 | 1.43x | 20.0/29.7/33.5% | 2.2/5.4% | 3 |

> bucket-mode=global: misdecodes 40

> bucket-mode=time: misdecodes 50

> bucket-mode=window: misdecodes 31

### `SF-bucket-time` - time-bucket-s  `--scenario coastal`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.921 | 0.918 | 0.004 | - | - | 0.997 | 0.997 | 0.497 | 1.62x | 22.3/32.8/36.8% | 2.5/6.1% | 3 |
| 1800 | 1 | 0.925 | 0.921 | 0.003 | - | - | 0.994 | 0.996 | 0.498 | 1.49x | 20.6/30.6/34.4% | 2.3/5.6% | 3 |
| 3600 | 1 | 0.921 | 0.919 | 0.003 | - | - | 0.990 | 0.996 | 0.492 | 1.45x | 20.2/29.9/33.8% | 2.2/5.4% | 3 |

> time-bucket-s=600: misdecodes 125

> time-bucket-s=1800: misdecodes 50

> time-bucket-s=3600: misdecodes 15

### `SF-cadence` - trigger  `--scenario coastal`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| interval | 1 | 0.911 | 0.907 | 0.005 | - | - | 0.987 | 0.990 | 0.481 | 1.98x | 27.5/40.5/44.7% | 3.1/7.9% | 3 |
| aimd | 1 | 0.925 | 0.924 | 0.001 | - | - | 0.971 | 0.996 | 0.502 | 1.48x | 20.6/30.7/34.4% | 2.3/5.5% | 3 |
| bucket+interval | 1 | 0.912 | 0.906 | 0.006 | - | - | 0.988 | 0.988 | 0.482 | 2.02x | 28.2/41.2/45.3% | 3.1/8.0% | 3 |

> trigger=interval: misdecodes 26

> trigger=aimd: misdecodes 4

> trigger=bucket+interval: misdecodes 31

### `SF-capacity` - capacity  `--scenario coastal`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.923 | 0.920 | 0.003 | - | - | 0.993 | 0.993 | 0.491 | 1.42x | 19.7/29.4/33.1% | 2.2/5.3% | 3 |
| 8 | 1 | 0.922 | 0.920 | 0.002 | - | - | 0.994 | 0.995 | 0.510 | 1.44x | 20.1/30.0/33.7% | 2.2/5.4% | 3 |
| 16 | 1 | 0.921 | 0.918 | 0.003 | - | - | 0.993 | 0.993 | 0.505 | 1.46x | 20.3/30.4/34.2% | 2.2/5.4% | 3 |
| 32 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 50 | 1 | 0.921 | 0.918 | 0.003 | - | - | 0.995 | 0.995 | 0.497 | 1.45x | 20.2/30.1/33.8% | 2.3/5.4% | 3 |

> capacity=4: decode_failures 45

### `SF-capacity-local` - capacity  `--scenario coastal`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.923 | 0.920 | 0.003 | - | - | 0.993 | 0.993 | 0.491 | 1.42x | 19.7/29.4/33.1% | 2.2/5.3% | 3 |
| 8 | 1 | 0.922 | 0.920 | 0.002 | - | - | 0.994 | 0.995 | 0.510 | 1.44x | 20.1/30.0/33.7% | 2.2/5.4% | 3 |
| 16 | 1 | 0.921 | 0.918 | 0.003 | - | - | 0.993 | 0.993 | 0.505 | 1.46x | 20.3/30.4/34.2% | 2.2/5.4% | 3 |
| 32 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 50 | 1 | 0.921 | 0.918 | 0.003 | - | - | 0.995 | 0.995 | 0.497 | 1.45x | 20.2/30.1/33.8% | 2.3/5.4% | 3 |

> capacity=4: decode_failures 45

### `SF-capacity-window` - capacity  `--scenario coastal`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.926 | 0.922 | 0.004 | - | - | 0.993 | 0.996 | 0.469 | 1.43x | 19.9/29.6/33.3% | 2.2/5.3% | 3 |
| 16 | 1 | 0.922 | 0.919 | 0.003 | - | - | 0.993 | 0.993 | 0.478 | 1.45x | 20.2/30.1/33.9% | 2.2/5.4% | 3 |
| 32 | 1 | 0.926 | 0.924 | 0.002 | - | - | 0.993 | 0.993 | 0.493 | 1.43x | 20.0/29.7/33.5% | 2.2/5.4% | 3 |

> capacity=8: misdecodes 25

> capacity=8: decode_failures 3

> capacity=16: misdecodes 27

> capacity=32: misdecodes 31

### `SF-catchup` - catch-up-hours  `--scenario coastal`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.912 | 0.906 | 0.006 | - | - | 0.988 | 0.988 | 0.482 | 2.02x | 28.2/41.2/45.3% | 3.1/8.0% | 3 |
| 02-06 | 1 | 0.924 | 0.923 | 0.002 | - | - | 0.980 | 0.997 | 0.479 | 1.50x | 20.8/31.0/34.7% | 2.3/5.6% | 3 |
| 00-08 | 1 | 0.924 | 0.923 | 0.001 | - | - | 0.980 | 0.993 | 0.495 | 1.55x | 21.5/31.9/35.8% | 2.4/5.8% | 3 |

> catch-up-hours=: misdecodes 31

> catch-up-hours=02-06: decode_failures 3

> faster: 3.02 s per simulated hour against 9.66 over 20 prior run(s) - 3.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-hops-flat` - hops-apart  `--scenario coastal`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.924 | 0.922 | 0.002 | - | - | 0.995 | 0.995 | 0.509 | 1.47x | 20.4/30.3/34.1% | 2.2/5.4% | 3 |
| 2 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 3 | 1 | 0.931 | 0.924 | 0.007 | - | - | 0.996 | 0.997 | 0.497 | 1.45x | 20.2/30.0/33.9% | 2.2/5.4% | 3 |
| 4 | 1 | 0.935 | 0.920 | 0.014 | - | - | 0.972 | 0.997 | 0.502 | 1.47x | 20.4/30.3/34.4% | 2.3/5.5% | 3 |

> hops-apart=4: decode_failures 28

### `SF-hops-spread` - hops-apart  `--scenario coastal`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.924 | 0.922 | 0.002 | - | - | 0.995 | 0.995 | 0.509 | 1.47x | 20.4/30.3/34.1% | 2.2/5.4% | 3 |
| 2 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 3 | 1 | 0.931 | 0.924 | 0.007 | - | - | 0.996 | 0.997 | 0.497 | 1.45x | 20.2/30.0/33.9% | 2.2/5.4% | 3 |
| 4 | 1 | 0.935 | 0.920 | 0.014 | - | - | 0.972 | 0.997 | 0.502 | 1.47x | 20.4/30.3/34.4% | 2.3/5.5% | 3 |
| 5 | 1 | 0.933 | 0.920 | 0.012 | - | - | 0.915 | 0.991 | 0.499 | 1.46x | 20.2/30.3/34.3% | 2.2/5.6% | 3 |

> hops-apart=4: decode_failures 28

> hops-apart=5: decode_failures 39

### `SF-jitter-global` - advert-jitter-s  `--scenario coastal`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.922 | 0.919 | 0.003 | - | - | 0.993 | 0.993 | 0.495 | 1.45x | 20.2/30.0/33.8% | 2.2/5.4% | 3 |
| 30 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 120 | 1 | 0.924 | 0.922 | 0.003 | - | - | 0.996 | 0.997 | 0.500 | 1.46x | 20.2/30.2/33.9% | 2.2/5.4% | 3 |
| 600 | 1 | 0.928 | 0.925 | 0.004 | - | - | 0.997 | 0.997 | 0.495 | 1.44x | 20.1/30.0/33.7% | 2.2/5.4% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario coastal`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.922 | 0.919 | 0.003 | - | - | 0.993 | 0.993 | 0.495 | 1.45x | 20.2/30.0/33.8% | 2.2/5.4% | 3 |
| 30 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 120 | 1 | 0.924 | 0.922 | 0.003 | - | - | 0.996 | 0.997 | 0.500 | 1.46x | 20.2/30.2/33.9% | 2.2/5.4% | 3 |
| 600 | 1 | 0.928 | 0.925 | 0.004 | - | - | 0.997 | 0.997 | 0.495 | 1.44x | 20.1/30.0/33.7% | 2.2/5.4% | 3 |

### `SF-place-flat` - place  `--scenario coastal`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.936 | 0.922 | 0.014 | - | - | 0.923 | 0.989 | 0.503 | 1.47x | 20.6/30.5/33.9% | 2.2/5.4% | 3 |
| routers | 1 | 0.924 | 0.923 | 0.001 | - | - | 0.993 | 0.993 | 0.492 | 1.44x | 20.0/29.9/33.7% | 2.2/5.4% | 3 |
| alternate-routers | 1 | 0.924 | 0.922 | 0.002 | - | - | 0.993 | 0.993 | 0.485 | 1.45x | 20.2/30.2/34.1% | 2.2/5.5% | 3 |
| beside-router | 1 | 0.924 | 0.922 | 0.002 | - | - | 0.995 | 0.995 | 0.498 | 1.42x | 19.8/29.6/33.3% | 2.2/5.3% | 3 |
| random-clients | 1 | 0.931 | 0.926 | 0.005 | - | - | 0.997 | 0.998 | 0.489 | 1.48x | 20.5/30.7/34.5% | 2.3/5.5% | 3 |
| hops-apart | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |

> place=spread: decode_failures 34

### `SF-place-spread` - place  `--scenario coastal`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.936 | 0.922 | 0.014 | - | - | 0.923 | 0.989 | 0.503 | 1.47x | 20.6/30.5/33.9% | 2.2/5.4% | 3 |
| routers | 1 | 0.924 | 0.923 | 0.001 | - | - | 0.993 | 0.993 | 0.492 | 1.44x | 20.0/29.9/33.7% | 2.2/5.4% | 3 |
| alternate-routers | 1 | 0.924 | 0.922 | 0.002 | - | - | 0.993 | 0.993 | 0.485 | 1.45x | 20.2/30.2/34.1% | 2.2/5.5% | 3 |
| beside-router | 1 | 0.924 | 0.922 | 0.002 | - | - | 0.995 | 0.995 | 0.498 | 1.42x | 19.8/29.6/33.3% | 2.2/5.3% | 3 |
| random-clients | 1 | 0.931 | 0.926 | 0.005 | - | - | 0.997 | 0.998 | 0.489 | 1.48x | 20.5/30.7/34.5% | 2.3/5.5% | 3 |
| hops-apart | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |

> place=spread: decode_failures 34

### `SF-provide-transport` - provide-transport  `--scenario coastal`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| broadcast | 1 | 0.929 | 0.914 | 0.015 | - | - | 0.991 | 0.991 | 0.527 | 1.49x | 20.6/30.5/34.3% | 2.3/5.6% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario coastal`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| heard | 1 | 0.926 | 0.923 | 0.003 | - | - | 0.997 | 0.997 | 0.480 | 1.44x | 20.1/29.9/33.7% | 2.2/5.4% | 3 |

> replay-ordering=heard: misdecodes 26

### `SF-replay-order-broadcast` - replay-ordering  `--scenario coastal`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.929 | 0.914 | 0.015 | - | - | 0.991 | 0.991 | 0.527 | 1.49x | 20.6/30.5/34.3% | 2.3/5.6% | 3 |
| heard | 1 | 0.936 | 0.923 | 0.013 | - | - | 0.995 | 0.996 | 0.533 | 1.50x | 20.7/30.8/34.6% | 2.3/5.6% | 3 |

> replay-ordering=heard: misdecodes 17

### `SF-resolve` - resolve  `--scenario coastal`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| enum | 1 | 0.926 | 0.923 | 0.003 | - | - | 0.992 | 0.992 | 0.497 | 1.43x | 19.9/29.8/33.6% | 2.2/5.4% | 3 |
| hybrid | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |

### `SF-servers-allrouters` - servers  `--scenario coastal`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.924 | 0.923 | 0.001 | - | - | 0.993 | 0.993 | 0.492 | 1.44x | 20.0/29.9/33.7% | 2.2/5.4% | 3 |
| 6 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.993 | 0.993 | 0.486 | 1.50x | 20.8/31.1/35.0% | 2.3/5.7% | 6 |

> servers=6: misdecodes 1

### `SF-servers-flat` - servers  `--scenario coastal`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.923 | 0.921 | 0.002 | - | - | 0.994 | 0.994 | 0.505 | 1.45x | 20.2/30.1/33.7% | 2.2/5.4% | 2 |
| 3 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 5 | 1 | 0.928 | 0.922 | 0.006 | - | - | 0.997 | 0.997 | 0.513 | 1.47x | 20.5/30.4/34.1% | 2.2/5.5% | 5 |
| 8 | 1 | 0.925 | 0.916 | 0.009 | - | - | 0.994 | 0.995 | 0.501 | 1.52x | 21.3/31.5/35.1% | 2.3/5.6% | 8 |

> servers=8: misdecodes 1

### `SF-servers-spread` - servers  `--scenario coastal`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.923 | 0.921 | 0.002 | - | - | 0.994 | 0.994 | 0.505 | 1.45x | 20.2/30.1/33.7% | 2.2/5.4% | 2 |
| 3 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 5 | 1 | 0.928 | 0.922 | 0.006 | - | - | 0.997 | 0.997 | 0.513 | 1.47x | 20.5/30.4/34.1% | 2.2/5.5% | 5 |
| 8 | 1 | 0.925 | 0.916 | 0.009 | - | - | 0.994 | 0.995 | 0.501 | 1.52x | 21.3/31.5/35.1% | 2.3/5.6% | 8 |

> servers=8: misdecodes 1

### `SF-signed` - signed  `--scenario coastal`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| True | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario coastal`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.928 | 0.926 | 0.002 | - | - | 0.997 | 0.997 | 0.523 | 1.38x | 19.0/28.4/31.9% | 2.1/5.1% | 3 |
| 1 | 1 | 0.929 | 0.926 | 0.002 | - | - | 0.996 | 0.997 | 0.487 | 1.39x | 19.3/28.6/32.2% | 2.1/5.1% | 3 |
| 2 | 1 | 0.929 | 0.926 | 0.002 | - | - | 0.997 | 0.997 | 0.530 | 1.41x | 19.5/29.0/32.5% | 2.1/5.2% | 3 |
| 4 | 1 | 0.926 | 0.923 | 0.003 | - | - | 0.989 | 0.990 | 0.526 | 1.40x | 19.4/29.0/32.5% | 2.1/5.1% | 3 |

### `SF-width` - short-id-bits  `--scenario coastal`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.995 | 0.995 | 0.502 | 1.43x | 19.9/29.8/33.6% | 2.2/5.4% | 3 |
| 24 | 1 | 0.928 | 0.926 | 0.003 | - | - | 0.996 | 0.997 | 0.517 | 1.45x | 20.1/29.9/33.8% | 2.3/5.4% | 3 |
| 32 | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.997 | 0.997 | 0.515 | 1.46x | 20.4/30.2/34.1% | 2.3/5.5% | 3 |
| 64 | 1 | 0.920 | 0.917 | 0.004 | - | - | 0.995 | 0.996 | 0.480 | 1.45x | 20.2/30.0/33.8% | 2.2/5.4% | 3 |

### `SF-window-size` - window-size  `--scenario coastal`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.925 | 0.921 | 0.004 | - | - | 0.997 | 0.997 | 0.530 | 1.56x | 21.5/31.9/35.9% | 2.4/5.8% | 3 |
| 16 | 1 | 0.922 | 0.917 | 0.005 | - | - | 0.994 | 0.994 | 0.506 | 1.49x | 20.7/30.7/34.5% | 2.3/5.5% | 3 |
| 32 | 1 | 0.926 | 0.924 | 0.002 | - | - | 0.993 | 0.993 | 0.493 | 1.43x | 20.0/29.7/33.5% | 2.2/5.4% | 3 |

> window-size=8: misdecodes 154

> window-size=16: misdecodes 69

> window-size=32: misdecodes 31

### `TH-congestion` - no-congestion-scaling  `--scenario coastal`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.966 | 0.963 | 0.003 | - | - | 1.000 | 1.000 | 0.876 | 1.90x | 23.9/30.6/34.7% | 1.2/5.3% | 3 |
| True | 1 | 0.783 | 0.771 | 0.011 | - | - | 0.874 | 0.949 | 0.593 | 5.48x | 61.0/72.1/75.3% | 3.5/13.8% | 3 |

> no-congestion-scaling=True: queue drops 11.0% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 106

### `TH-congestion-input` - congestion-input  `--scenario coastal`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.559 | 0.545 | 0.014 | - | - | 0.739 | 0.741 | 0.187 | 4.39x | 17.4/25.1/33.1% | 1.5/5.2% | 3 |
| truesize | 1 | 0.591 | 0.578 | 0.013 | - | - | 0.777 | 0.780 | 0.191 | 3.31x | 13.1/19.3/25.1% | 1.1/4.3% | 3 |

> congestion-input=hotstore: decode_failures 1

> congestion-input=truesize: decode_failures 5

### `TH-congestion-mode` - congestion-mode  `--scenario coastal`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.969 | 0.967 | 0.003 | - | - | 1.000 | 1.000 | 0.875 | 1.74x | 22.0/28.0/31.6% | 1.1/5.0% | 3 |
| adaptive | 1 | 0.966 | 0.963 | 0.003 | - | - | 1.000 | 1.000 | 0.876 | 1.90x | 23.9/30.6/34.7% | 1.2/5.3% | 3 |

