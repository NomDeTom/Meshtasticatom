# Sweep blocks-2026-10-16-1430165

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** rolling
- **seed base** 1430165 · seeds 1430165
- **blocks** 87 run
- **compute** 11.2 h of simulator time across every cell
- **generated** 2026-10-16T08:42:46+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>71 warnings</summary>

- DB-hotstore-stress: max-num-nodes=10: decode_failures 59
- DB-hotstore-stress: max-num-nodes=120: decode_failures 106
- DB-hotstore-stress: max-num-nodes=250: decode_failures 102
- DB-warm: warm-num-nodes=0: queue drops 13.8% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 95
- DB-warm: warm-num-nodes=25: queue drops 13.8% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 95
- DB-warm: warm-num-nodes=100: queue drops 13.8% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 95
- DB-warm: warm-num-nodes=2000: queue drops 13.8% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 95
- DG-burst: burst-loss=0.2: decode_failures 5
- DG-burst: burst-loss=0.3: decode_failures 23
- DG-outage: burst-loss=0.1: decode_failures 45
- DG-outage: burst-loss=0.2: decode_failures 29
- DG-outage: burst-loss=0.3: decode_failures 29
- LD-chatty-hops: broadcast-interval-s=300: queue drops 14.5% of transmissions - airtime here is measured through a cap
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 35
- LD-chatty: broadcast-interval-s=300: queue drops 10.9% of transmissions - airtime here is measured through a cap
- LD-chatty: broadcast-interval-s=300: decode_failures 30
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 13.8% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 95
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 18.8% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 63
- MS-hopscale: nodes=250: decode_failures 201
- MS-hopscale: nodes=500: decode_failures 5
- MS-oversubscribed: nodes=250: decode_failures 106
- MS-oversubscribed: nodes=500: decode_failures 6
- MS-router-late: router-late-fraction=0.1: misdecodes 1
- MS-stretch: stretch=2.0: decode_failures 8
- MS-topology: topology=corridor: decode_failures 46
- MS-topology: slower: 3.95 s per simulated hour against 1.91 over 56 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-preset: faster: 1.27 s per simulated hour against 2.86 over 56 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-preset-turbo: preset=EXTRA_SHORT_TURBO: 3 archives requested, 2 placed - group on the placed count
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 5
- RT-spread: faster: 1.11 s per simulated hour against 2.24 over 56 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-bucket-mode: bucket-mode=global: misdecodes 32
- SF-bucket-mode: bucket-mode=time: misdecodes 32
- SF-bucket-mode: bucket-mode=window: misdecodes 18
- SF-bucket-time: time-bucket-s=600: misdecodes 132
- SF-bucket-time: time-bucket-s=1800: misdecodes 32
- SF-bucket-time: time-bucket-s=3600: misdecodes 20
- SF-cadence: trigger=interval: misdecodes 20
- SF-cadence: trigger=aimd: misdecodes 2
- SF-cadence: trigger=bucket+interval: misdecodes 35
- SF-capacity-local: capacity=4: decode_failures 53
- SF-capacity-local: capacity=8: decode_failures 18
- SF-capacity: capacity=4: decode_failures 53
- SF-capacity: capacity=8: decode_failures 18
- SF-capacity-window: capacity=8: misdecodes 25
- SF-capacity-window: capacity=8: decode_failures 1
- SF-capacity-window: capacity=16: misdecodes 31
- SF-capacity-window: capacity=32: misdecodes 18
- SF-catchup: catch-up-hours=: misdecodes 35
- SF-catchup: catch-up-hours=02-06: decode_failures 23
- SF-catchup: catch-up-hours=00-08: misdecodes 1
- SF-catchup: catch-up-hours=00-08: decode_failures 21
- SF-hops-flat: hops-apart=4: decode_failures 46
- SF-hops-spread: hops-apart=4: decode_failures 46
- SF-place-flat: place=spread: decode_failures 29
- SF-place-spread: place=spread: decode_failures 29
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 18
- SF-replay-order: replay-ordering=heard: misdecodes 19
- SF-window-size: window-size=8: misdecodes 144
- SF-window-size: window-size=16: misdecodes 72
- SF-window-size: window-size=32: misdecodes 18
- TH-congestion-input: congestion-input=hotstore: decode_failures 106
- TH-congestion-input: congestion-input=truesize: decode_failures 69
- TH-congestion-input: slower: 46.5 s per simulated hour against 11.1 over 56 prior run(s) - 4.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- TH-congestion: no-congestion-scaling=True: queue drops 13.2% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 96

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `TH-congestion-input` | 46.5 | 11.1 | 4.18x | 56 |
| `MS-topology` | 3.95 | 1.91 | 2.07x | 56 |
| `LD-chatty-hops` | 6.69 | 3.8 | 1.76x | 56 |
| `AD-flooding` | 1.66 | 2.5 | 0.66x | 56 |
| `MS-roles-fav` | 1.12 | 1.73 | 0.65x | 56 |
| `SF-place-flat` | 1.86 | 2.86 | 0.65x | 56 |
| `SF-place-spread` | 1.8 | 2.77 | 0.65x | 56 |
| `DM-mode` | 1.87 | 2.89 | 0.65x | 56 |
| `MS-router-late` | 1.1 | 1.72 | 0.64x | 56 |
| `SF-servers-allrouters` | 1.12 | 1.83 | 0.61x | 56 |
| `SF-servers-spread` | 1.35 | 2.22 | 0.61x | 56 |
| `RF-pulse` | 0.966 | 1.61 | 0.60x | 56 |
| `RT-adopt` | 2.4 | 3.99 | 0.60x | 56 |
| `RF-preset-turbo` | 0.918 | 1.53 | 0.60x | 52 |
| `SF-resolve` | 0.908 | 1.53 | 0.59x | 56 |
| `SF-bucket-mode` | 0.86 | 1.45 | 0.59x | 56 |
| `PR-dmmode-cr` | 1.47 | 2.52 | 0.59x | 56 |
| `SF-replay-order-broadcast` | 0.94 | 1.68 | 0.56x | 56 |
| `SF-cadence` | 1.97 | 3.54 | 0.56x | 56 |
| `SC-signing` | 0.985 | 1.78 | 0.55x | 56 |
| `AD-siting` | 0.78 | 1.42 | 0.55x | 56 |
| `AD-amplify-worst` | 0.988 | 1.84 | 0.54x | 56 |
| `RT-hopspread` | 1.07 | 2.03 | 0.53x | 56 |
| `RT-spread` | 1.11 | 2.24 | 0.50x | 56 |
| `RF-preset` | 1.27 | 2.86 | 0.44x | 56 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.983 | 0.983 | 0.891 → 0.904 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.968 | 0.968 | 0.894 → 0.904 | 1.2x bytes_on_air | up | 3 |
| `RF-preset-turbo` | preset | **held** | 0.076 → 0.968 | 0.892 | 0.053 → 0.894 | 54x sr_bytes | up | 5 |
| `AD-siting` | siting-mix | **text** | 0.042 → 0.881 | 0.839 | 0.041 → 0.875 | 4.9x advert_bytes | down | 3 |
| `RF-txpower` | tx-power | **text** | 0.078 → 0.898 | 0.820 | 0.077 → 0.894 | 7.5x advert_bytes | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.123 → 0.915 | 0.792 | 0.126 → 0.837 | 1.5e+02x sr_airtime | down | 4 |
| `MS-stretch` | stretch | **text** | 0.123 → 0.898 | 0.775 | 0.121 → 0.894 | 3.8x advert_bytes | down | 4 |
| `MS-siting` | siting-mix | **text** | 0.234 → 0.972 | 0.738 | 0.228 → 0.972 | 2.4x advert_bytes | up | 4 |
| `RF-bw500` | preset | **text** | 0.175 → 0.838 | 0.663 | 0.174 → 0.823 | 2.8x sr_airtime | up | 3 |
| `MS-hopscale` | nodes | **text** | 0.314 → 0.898 | 0.584 | 0.309 → 0.894 | 15x sr_bytes | down | 4 |
| `RF-eu-presets` | preset | **text** | 0.435 → 0.898 | 0.463 | 0.427 → 0.894 | 2.4x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.435 → 0.898 | 0.463 | 0.427 → 0.894 | 3.1x sr_airtime | up | 3 |
| `MS-oversubscribed` | nodes | **text** | 0.319 → 0.778 | 0.459 | 0.315 → 0.770 | 4.5x sr_bytes | down | 3 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.566 → 0.920 | 0.354 | 0.549 → 0.918 | 7.7x sr_airtime | down | 3 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.539 → 0.867 | 0.328 | 0.326 → 0.517 | 6.3x sr_airtime | up | 3 |
| `DG-outage` | burst-loss | **text** | 0.574 → 0.898 | 0.324 | 0.545 → 0.894 | 2.8x sr_bytes | down | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.638 → 0.961 | 0.323 | 0.625 → 0.960 | 7.3x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.614 → 0.898 | 0.284 | 0.574 → 0.894 | 3.1x sr_bytes | down | 4 |
| `MS-size` | nodes | **text** | 0.656 → 0.898 | 0.242 | 0.644 → 0.894 | 4.7x sr_bytes | down | 5 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.491 → 0.710 | 0.220 | 0.475 → 0.689 | 1.3x sr_airtime | up | 2 |
| `MS-topology` | topology | **text** | 0.736 → 0.955 | 0.219 | 0.721 → 0.955 | 4.7x sr_bytes | up | 4 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.752 → 0.960 | 0.208 | 0.751 → 0.959 | 6.2x sr_airtime | down | 2 |
| `RT-hoplimit` | hop-limit | **text** | 0.776 → 0.958 | 0.181 | 0.758 → 0.957 | 2.2x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.776 → 0.954 | 0.177 | 0.758 → 0.952 | 2x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **text** | 0.733 → 0.898 | 0.165 | 0.727 → 0.894 | 1.4x sr_bytes | down | 4 |
| `MS-density` | nodes | **text** | 0.806 → 0.963 | 0.156 | 0.791 → 0.961 | 5.4x sr_airtime | up | 5 |
| `SC-signing` | signature-policy | **text** | 0.771 → 0.898 | 0.127 | 0.771 → 0.894 | 1.2x sr_airtime | down | 3 |
| `RT-spread` | hop-spread | **text** | 0.776 → 0.898 | 0.121 | 0.758 → 0.894 | 1.9x sr_bytes | up | 2 |
| `DB-platform` | platform-mix | **text** | 0.803 → 0.923 | 0.120 | 0.795 → 0.920 | 2.1x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.811 → 0.923 | 0.112 | 0.804 → 0.920 | 2.2x sr_airtime | up | 4 |
| `DG-loss` | extra-loss | **text** | 0.798 → 0.898 | 0.099 | 0.786 → 0.894 | 1.7x sr_bytes | down | 4 |
| `LD-interval` | broadcast-interval-s | **text** | 0.853 → 0.936 | 0.084 | 0.843 → 0.934 | 5.5x sr_airtime | up | 4 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.898 → 0.970 | 0.072 | 0.894 → 0.970 | 1.5x sr_bytes | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.898 → 0.962 | 0.064 | 0.894 → 0.960 | 1.3x bytes_on_air | up | 3 |
| `AD-flooding` | role-mix | **text** | 0.881 → 0.942 | 0.061 | 0.875 → 0.941 | 2.6x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.881 → 0.942 | 0.061 | 0.875 → 0.941 | 2.6x bytes_on_air | up | 3 |
| `SF-hops-flat` | hops-apart | **held** | 0.931 → 0.983 | 0.052 | 0.891 → 0.896 | 2x sr_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.931 → 0.983 | 0.052 | 0.891 → 0.902 | 2x sr_bytes | up | 5 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.693 → 0.743 | 0.049 | 0.692 → 0.741 | 1.4x sr_airtime | down | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.850 → 0.898 | 0.048 | 0.507 → 0.543 | 1.4x sr_airtime | up | 2 |
| `RF-duct` | duct-per-hour | **text** | 0.898 → 0.943 | 0.045 | 0.894 → 0.938 | 1.3x sr_bytes | up | 3 |
| `SF-place-flat` | place | **held** | 0.938 → 0.981 | 0.043 | 0.894 → 0.907 | 2.9x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.938 → 0.981 | 0.043 | 0.894 → 0.907 | 2.9x sr_bytes | up | 6 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.860 → 0.899 | 0.039 | 0.851 → 0.894 | 1.4x sr_airtime | down | 4 |
| `SF-catchup` | catch-up-hours | **text** | 0.872 → 0.909 | 0.037 | 0.864 → 0.905 | 9.6x sr_bytes | up | 3 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.887 → 0.922 | 0.035 | 0.881 → 0.917 | 2.1x bytes_on_air | down | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.898 → 0.930 | 0.032 | 0.894 → 0.927 | 3.3x bytes_on_air | down | 2 |
| `MS-roles-fav` | role-mix | **text** | 0.890 → 0.921 | 0.031 | 0.886 → 0.918 | 1.1x bytes_on_air | down | 2 |
| `SF-cadence` | trigger | **text** | 0.872 → 0.902 | 0.030 | 0.864 → 0.901 | 20x sr_bytes | down | 4 |
| `FW-versions` | profile | **held** | 0.968 → 0.997 | 0.029 | 0.888 → 0.908 | 3.3x bytes_on_air | down | 5 |
| `FW-mixed` | legacy-fraction | **text** | 0.891 → 0.919 | 0.029 | 0.884 → 0.913 | 2.1x bytes_on_air | down | 4 |
| `FW-firmware` | profile | **held** | 0.968 → 0.995 | 0.027 | 0.894 → 0.900 | 3.3x bytes_on_air | down | 2 |
| `AD-worst` | role-placement | **text** | 0.861 → 0.887 | 0.026 | 0.848 → 0.881 | 1.3x sr_bytes | down | 2 |
| `MS-roles` | role-mix | **text** | 0.881 → 0.905 | 0.024 | 0.875 → 0.901 | 1.1x bytes_on_air | down | 2 |
| `AD-badrouters` | role-placement | **text** | 0.859 → 0.881 | 0.022 | 0.848 → 0.875 | 1.2x sr_bytes | down | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.888 → 0.911 | 0.022 | 0.883 → 0.905 | 1.1x sr_bytes | up | 2 |
| `RT-hopassign` | hop-assign | **held** | 0.968 → 0.989 | 0.021 | 0.890 → 0.894 | 1.5x sr_bytes | up | 2 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.950 → 0.968 | 0.018 | 0.894 → 0.908 | 24x sr_airtime | down | 3 |
| `SF-sr-retries` | sr-retries | **held** | 0.968 → 0.985 | 0.016 | 0.887 → 0.903 | 1.2x sr_bytes | up | 4 |
| `MS-router-late` | router-late-fraction | **held** | 0.963 → 0.979 | 0.015 | 0.891 → 0.909 | 1.4x bytes_on_air | up | 4 |
| `DM-mode` | dm-mode | **text** | 0.863 → 0.878 | 0.015 | 0.863 → 0.878 | 1.1x bytes_on_air | up | 3 |
| `SF-servers-flat` | servers | **held** | 0.966 → 0.981 | 0.015 | 0.882 → 0.896 | 8x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.966 → 0.981 | 0.015 | 0.882 → 0.896 | 8x sr_bytes | up | 4 |
| `SF-provide-transport` | provide-transport | **text** | 0.898 → 0.912 | 0.014 | 0.892 → 0.894 | 1.9x sr_airtime | up | 2 |
| `SF-replay-order` | replay-ordering | **held** | 0.968 → 0.982 | 0.014 | 0.894 → 0.901 | 1.2x sr_bytes | up | 2 |
| `SF-capacity` | capacity | **text** | 0.895 → 0.908 | 0.013 | 0.890 → 0.905 | 5.2x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **text** | 0.895 → 0.908 | 0.013 | 0.890 → 0.905 | 5.2x advert_bytes | down | 5 |
| `SF-window-size` | window-size | **text** | 0.890 → 0.903 | 0.013 | 0.885 → 0.897 | 4.8x advert_bytes | up | 3 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.960 → 0.971 | 0.011 | 0.870 → 0.876 | 1.1x sr_airtime | down | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.968 → 0.979 | 0.010 | 0.890 → 0.900 | 2.6x advert_bytes | up | 4 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.968 → 0.978 | 0.010 | 0.892 → 0.897 | 1.2x sr_bytes | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.968 → 0.978 | 0.010 | 0.892 → 0.897 | 1.2x sr_bytes | up | 4 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.895 → 0.905 | 0.009 | 0.890 → 0.900 | 5.6x advert_bytes | up | 3 |
| `SF-servers-allrouters` | servers | **text** | 0.900 → 0.909 | 0.009 | 0.896 → 0.907 | 2x sr_airtime | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.972 → 0.980 | 0.009 | 0.892 → 0.895 | 1.2x sr_bytes | up | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.898 → 0.906 | 0.008 | 0.894 → 0.902 | 1.1x sr_bytes | up | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.968 → 0.976 | 0.008 | 0.894 → 0.899 | 3x sr_airtime | up | 2 |
| `SF-width` | short-id-bits | **held** | 0.968 → 0.976 | 0.008 | 0.894 → 0.899 | 3.1x advert_bytes | up | 4 |
| `LD-diurnal` | diurnal | **text** | 0.898 → 0.906 | 0.008 | 0.894 → 0.902 | 1.2x advert_bytes | down | 3 |
| `SF-capacity-window` | capacity | **held** | 0.970 → 0.976 | 0.006 | 0.891 → 0.897 | 2.6x advert_bytes | up | 3 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.960 → 0.965 | 0.005 | 0.959 → 0.965 | 1.1x sr_bytes | down | 2 |
| `SF-resolve` | resolve | **held** | 0.968 → 0.973 | 0.005 | 0.894 → 0.897 | 5.7x advert_bytes | = | 3 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.868 → 0.870 | 0.002 | 0.868 → 0.870 | 1x sr_bytes | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.958 → 0.960 | 0.002 | 0.957 → 0.959 | 1.2x sr_airtime | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.960 → 0.961 | 0.001 | 0.959 → 0.961 | 1x sr_bytes | up | 2 |

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
| none | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| sprinkled | 1 | 0.955 | 0.955 | 0.000 | - | - | 0.991 | 0.991 | 0.703 | 1.09x | 20.1/27.7/29.7% | 1.2/5.4% | 3 |
| arms-race | 1 | 0.970 | 0.970 | 0.000 | - | - | 0.991 | 0.991 | 0.901 | 0.90x | 24.3/28.3/31.0% | 0.9/5.5% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario rolling`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 0.1 | 1 | 0.944 | 0.939 | 0.005 | - | - | 0.995 | 0.995 | 0.833 | 1.13x | 20.3/24.3/26.4% | 1.5/5.1% | 3 |
| 0.3 | 1 | 0.962 | 0.960 | 0.002 | - | - | 0.999 | 1.000 | 0.882 | 1.00x | 22.0/26.4/30.7% | 1.3/5.0% | 3 |

### `AD-badrouters` - role-placement  `--scenario rolling`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.881 | 0.875 | 0.006 | - | - | 0.974 | 0.976 | 0.510 | 1.13x | 15.9/24.9/27.6% | 1.7/5.2% | 3 |
| inverse | 1 | 0.859 | 0.848 | 0.011 | - | - | 0.971 | 0.972 | 0.617 | 1.13x | 15.0/19.9/22.1% | 2.0/3.6% | 3 |
| random | 1 | 0.880 | 0.871 | 0.009 | - | - | 0.967 | 0.968 | 0.523 | 1.16x | 16.1/23.9/25.1% | 1.9/4.9% | 3 |

### `AD-flooding` - role-mix  `--scenario rolling`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.881 | 0.875 | 0.006 | - | - | 0.974 | 0.976 | 0.510 | 1.13x | 15.9/24.9/27.6% | 1.7/5.2% | 3 |
| all-routers | 1 | 0.942 | 0.941 | 0.001 | - | - | 0.985 | 0.985 | 0.796 | 2.89x | 35.9/48.3/51.6% | 4.7/5.3% | 3 |

### `AD-nomute` - role-mix  `--scenario rolling`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.881 | 0.875 | 0.006 | - | - | 0.974 | 0.976 | 0.510 | 1.13x | 15.9/24.9/27.6% | 1.7/5.2% | 3 |
| no-mute | 1 | 0.907 | 0.903 | 0.003 | - | - | 0.981 | 0.982 | 0.674 | 1.25x | 17.6/24.0/26.5% | 2.1/5.1% | 3 |
| all-routers | 1 | 0.942 | 0.941 | 0.001 | - | - | 0.985 | 0.985 | 0.796 | 2.89x | 35.9/48.3/51.6% | 4.7/5.3% | 3 |

### `AD-siting` - siting-mix  `--scenario rolling`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.881 | 0.875 | 0.006 | - | - | 0.974 | 0.976 | 0.510 | 1.13x | 15.9/24.9/27.6% | 1.7/5.2% | 3 |
| local-typical | 1 | 0.606 | 0.591 | 0.015 | - | - | 0.852 | 0.855 | 0.000 | 1.21x | 12.8/22.5/27.3% | 1.9/4.8% | 3 |
| basement-heavy | 1 | 0.042 | 0.041 | 0.001 | - | - | 0.217 | 0.222 | 0.000 | 0.36x | 0.2/3.9/9.1% | 0.2/2.4% | 3 |

### `AD-worst` - role-placement  `--scenario rolling`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.887 | 0.881 | 0.006 | - | - | 0.965 | 0.966 | 0.072 | 2.34x | 19.3/29.6/37.3% | 1.7/5.6% | 3 |
| inverse | 1 | 0.861 | 0.848 | 0.013 | - | - | 0.967 | 0.969 | 0.073 | 2.27x | 17.6/25.4/32.3% | 1.8/3.4% | 3 |

### `BL-control` - protocol  `--scenario rolling`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.904 | 0.904 | 0.000 | - | - | 0 | 0.000 | 0.726 | 1.27x | 17.9/26.4/29.0% | 1.9/5.2% | 3 |
| sr | 1 | 0.904 | 0.891 | 0.013 | - | - | 0.983 | 0.984 | 0.734 | 1.32x | 18.6/27.2/29.9% | 2.0/5.4% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario rolling`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.811 | 0.804 | 0.007 | - | - | 0.904 | 0.908 | 0.664 | 3.15x | 39.4/66.7/71.2% | 4.5/10.2% | 3 |
| 100 | 1 | 0.923 | 0.920 | 0.004 | - | - | 0.978 | 0.978 | 0.780 | 1.65x | 20.8/39.7/42.1% | 2.3/5.4% | 3 |
| 120 | 1 | 0.923 | 0.920 | 0.004 | - | - | 0.978 | 0.978 | 0.780 | 1.65x | 20.8/39.7/42.1% | 2.3/5.4% | 3 |
| 250 | 1 | 0.923 | 0.920 | 0.004 | - | - | 0.978 | 0.978 | 0.780 | 1.65x | 20.8/39.7/42.1% | 2.3/5.4% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario rolling`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.334 | 0.326 | 0.007 | - | - | 0.539 | 0.733 | 0.179 | 11.68x | 40.7/58.4/69.0% | 4.1/10.5% | 3 |
| 120 | 1 | 0.522 | 0.507 | 0.015 | - | - | 0.850 | 0.911 | 0.228 | 4.70x | 16.8/27.5/36.6% | 1.5/5.3% | 3 |
| 250 | 1 | 0.532 | 0.517 | 0.015 | - | - | 0.867 | 0.913 | 0.239 | 4.57x | 16.3/26.3/35.3% | 1.5/5.1% | 3 |

> max-num-nodes=10: decode_failures 59

> max-num-nodes=120: decode_failures 106

> max-num-nodes=250: decode_failures 102

### `DB-platform` - platform-mix  `--scenario rolling`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.923 | 0.920 | 0.004 | - | - | 0.978 | 0.978 | 0.780 | 1.65x | 20.8/39.7/42.1% | 2.3/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.923 | 0.920 | 0.004 | - | - | 0.978 | 0.978 | 0.780 | 1.65x | 20.8/39.7/42.1% | 2.3/5.4% | 3 |
| constrained | 1 | 0.803 | 0.795 | 0.008 | - | - | 0.899 | 0.903 | 0.643 | 3.15x | 39.4/66.8/71.3% | 4.6/10.2% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario rolling`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.743 | 0.741 | 0.002 | - | - | 0.853 | 0.928 | 0.552 | 5.70x | 63.3/72.1/75.5% | 4.1/12.0% | 3 |
| 25 | 1 | 0.743 | 0.741 | 0.002 | - | - | 0.853 | 0.928 | 0.552 | 5.70x | 63.3/72.1/75.5% | 4.1/12.0% | 3 |
| 100 | 1 | 0.743 | 0.741 | 0.002 | - | - | 0.853 | 0.928 | 0.552 | 5.70x | 63.3/72.1/75.5% | 4.1/12.0% | 3 |
| 2000 | 1 | 0.743 | 0.741 | 0.002 | - | - | 0.853 | 0.928 | 0.552 | 5.70x | 63.3/72.1/75.5% | 4.1/12.0% | 3 |

> warm-num-nodes=0: queue drops 13.8% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 95

> warm-num-nodes=25: queue drops 13.8% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 95

> warm-num-nodes=100: queue drops 13.8% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 95

> warm-num-nodes=2000: queue drops 13.8% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 95

### `DG-burst` - burst-loss  `--scenario rolling`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 0.1 | 1 | 0.813 | 0.796 | 0.017 | - | - | 0.961 | 0.963 | 0.601 | 1.27x | 18.1/26.6/29.5% | 2.0/5.0% | 3 |
| 0.2 | 1 | 0.714 | 0.684 | 0.029 | - | - | 0.922 | 0.937 | 0.469 | 1.18x | 16.9/24.9/27.8% | 1.8/4.5% | 3 |
| 0.3 | 1 | 0.614 | 0.574 | 0.040 | - | - | 0.827 | 0.872 | 0.366 | 1.09x | 15.8/23.2/26.2% | 1.7/4.0% | 3 |

> burst-loss=0.2: decode_failures 5

> burst-loss=0.3: decode_failures 23

### `DG-loss` - extra-loss  `--scenario rolling`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 0.1 | 1 | 0.875 | 0.868 | 0.007 | - | - | 0.966 | 0.968 | 0.667 | 1.37x | 19.4/28.1/30.8% | 2.2/5.2% | 3 |
| 0.2 | 1 | 0.834 | 0.825 | 0.009 | - | - | 0.943 | 0.948 | 0.560 | 1.44x | 20.4/29.7/32.6% | 2.3/5.2% | 3 |
| 0.3 | 1 | 0.798 | 0.786 | 0.012 | - | - | 0.927 | 0.932 | 0.536 | 1.46x | 21.1/30.4/33.3% | 2.3/5.0% | 3 |

### `DG-outage` - burst-loss  `--scenario rolling`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 0.1 | 1 | 0.801 | 0.788 | 0.013 | - | - | 0.928 | 0.964 | 0.626 | 1.24x | 17.7/25.8/28.5% | 1.9/4.9% | 3 |
| 0.2 | 1 | 0.698 | 0.676 | 0.021 | - | - | 0.887 | 0.943 | 0.396 | 1.19x | 17.1/24.9/28.0% | 1.8/4.5% | 3 |
| 0.3 | 1 | 0.574 | 0.545 | 0.028 | - | - | 0.723 | 0.864 | 0.322 | 1.08x | 15.9/22.9/25.8% | 1.7/4.3% | 3 |

> burst-loss=0.1: decode_failures 45

> burst-loss=0.2: decode_failures 29

> burst-loss=0.3: decode_failures 29

### `DM-mode` - dm-mode  `--scenario rolling`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.863 | 0.863 | 0.000 | - | - | 0.964 | 0.965 | 0.687 | 1.80x | 25.1/37.3/40.8% | 2.8/7.3% | 3 |
| directed-with-late-flood | 1 | 0.876 | 0.876 | 0.000 | - | - | 0.971 | 0.975 | 0.674 | 1.60x | 22.2/33.5/36.7% | 2.5/6.7% | 3 |
| m4-early-flood | 1 | 0.878 | 0.878 | 0.000 | - | - | 0.968 | 0.971 | 0.673 | 1.60x | 22.3/33.3/36.6% | 2.5/6.6% | 3 |

### `FW-firmware` - profile  `--scenario rolling`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.905 | 0.900 | 0.005 | - | - | 0.995 | 0.995 | 0.622 | 0.71x | 10.0/11.9/13.1% | 1.1/1.9% | 3 |
| 2.8 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario rolling`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 0.25 | 1 | 0.898 | 0.893 | 0.005 | - | - | 0.984 | 0.985 | 0.708 | 1.19x | 16.8/23.5/26.1% | 1.9/4.8% | 3 |
| 0.5 | 1 | 0.919 | 0.913 | 0.006 | - | - | 0.995 | 0.995 | 0.766 | 1.10x | 15.0/20.8/23.4% | 1.8/4.2% | 3 |
| 0.75 | 1 | 0.891 | 0.884 | 0.006 | - | - | 0.990 | 0.992 | 0.634 | 0.86x | 11.7/15.4/17.1% | 1.3/3.6% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario rolling`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 0.25 | 1 | 0.902 | 0.896 | 0.005 | - | - | 0.987 | 0.989 | 0.711 | 1.17x | 16.3/23.2/25.8% | 1.9/4.7% | 3 |
| 0.5 | 1 | 0.922 | 0.917 | 0.005 | - | - | 0.993 | 0.993 | 0.800 | 1.08x | 15.1/20.7/23.3% | 1.7/4.2% | 3 |
| 0.75 | 1 | 0.887 | 0.881 | 0.006 | - | - | 0.985 | 0.986 | 0.626 | 0.85x | 11.8/15.6/17.4% | 1.4/3.7% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario rolling`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.930 | 0.927 | 0.003 | - | - | 0.989 | 0.989 | 0.748 | 0.69x | 9.8/14.9/16.9% | 1.0/3.0% | 3 |
| signing=true | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |

### `FW-versions` - profile  `--scenario rolling`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.894 | 0.888 | 0.006 | - | - | 0.991 | 0.991 | 0.588 | 0.70x | 10.2/12.9/13.9% | 1.1/2.1% | 3 |
| 2.5 | 1 | 0.897 | 0.891 | 0.006 | - | - | 0.993 | 0.995 | 0.598 | 0.74x | 10.8/13.6/14.7% | 1.2/2.2% | 3 |
| 2.6 | 1 | 0.901 | 0.895 | 0.006 | - | - | 0.993 | 0.995 | 0.600 | 0.70x | 10.5/13.3/14.4% | 1.1/2.2% | 3 |
| 2.7 | 1 | 0.912 | 0.908 | 0.004 | - | - | 0.997 | 0.997 | 0.660 | 0.75x | 10.4/17.5/18.8% | 1.1/3.1% | 3 |
| 2.8 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.920 | 0.918 | 0.002 | - | - | 0.985 | 0.985 | 0.741 | 0.92x | 12.7/18.6/20.8% | 1.4/3.7% | 3 |
| 900 | 1 | 0.853 | 0.843 | 0.010 | - | - | 0.957 | 0.959 | 0.635 | 2.08x | 29.2/42.9/47.3% | 3.2/8.6% | 3 |
| 300 | 1 | 0.566 | 0.549 | 0.017 | - | - | 0.711 | 0.777 | 0.405 | 4.34x | 58.4/73.4/78.9% | 6.2/16.8% | 3 |

> broadcast-interval-s=300: queue drops 10.9% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 30

### `LD-chatty-hops` - broadcast-interval-s  `--scenario rolling`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.961 | 0.960 | 0.002 | - | - | 0.997 | 0.999 | 0.861 | 0.91x | 12.7/18.0/19.9% | 1.4/3.4% | 3 |
| 900 | 1 | 0.926 | 0.923 | 0.004 | - | - | 0.985 | 0.985 | 0.782 | 2.37x | 33.2/45.4/49.6% | 3.5/8.8% | 3 |
| 300 | 1 | 0.638 | 0.625 | 0.013 | - | - | 0.786 | 0.823 | 0.462 | 4.75x | 62.8/74.7/79.8% | 7.3/16.8% | 3 |

> broadcast-interval-s=300: queue drops 14.5% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 35

### `LD-diurnal` - diurnal  `--scenario rolling`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.906 | 0.902 | 0.003 | - | - | 0.975 | 0.977 | 0.722 | 1.20x | 16.9/24.9/27.5% | 1.8/5.0% | 3 |
| sinusoid | 1 | 0.900 | 0.896 | 0.004 | - | - | 0.973 | 0.975 | 0.708 | 1.21x | 17.0/25.0/27.5% | 1.8/4.9% | 3 |
| commuter | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.853 | 0.843 | 0.010 | - | - | 0.957 | 0.959 | 0.635 | 2.08x | 29.2/42.9/47.3% | 3.2/8.6% | 3 |
| 3600 | 1 | 0.920 | 0.918 | 0.002 | - | - | 0.985 | 0.985 | 0.741 | 0.92x | 12.7/18.6/20.8% | 1.4/3.7% | 3 |
| 10800 | 1 | 0.931 | 0.928 | 0.003 | - | - | 0.991 | 0.992 | 0.759 | 0.60x | 8.4/12.2/13.7% | 0.9/2.4% | 3 |
| 43200 | 1 | 0.936 | 0.934 | 0.002 | - | - | 0.992 | 0.992 | 0.762 | 0.44x | 6.1/8.9/10.0% | 0.7/1.8% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario rolling`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 0.25 | 1 | 0.899 | 0.893 | 0.006 | - | - | 0.971 | 0.974 | 0.722 | 1.36x | 19.1/28.3/31.2% | 2.1/5.6% | 3 |
| 1.0 | 1 | 0.891 | 0.886 | 0.006 | - | - | 0.973 | 0.975 | 0.698 | 1.55x | 21.7/32.2/35.5% | 2.4/6.5% | 3 |
| 4.0 | 1 | 0.860 | 0.851 | 0.009 | - | - | 0.953 | 0.953 | 0.659 | 1.92x | 27.4/40.6/44.9% | 2.9/8.3% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario rolling`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.743 | 0.741 | 0.002 | - | - | 0.853 | 0.928 | 0.552 | 5.70x | 63.3/72.1/75.5% | 4.1/12.0% | 3 |
| 1.0 | 1 | 0.693 | 0.692 | 0.001 | - | - | 0.811 | 0.910 | 0.531 | 6.06x | 65.9/73.6/77.1% | 4.4/12.9% | 3 |

> traceroute-per-hour=0.0: queue drops 13.8% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 95

> traceroute-per-hour=1.0: queue drops 18.8% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 63

### `MS-density` - nodes  `--scenario rolling`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.806 | 0.791 | 0.015 | - | - | 0.941 | 0.942 | 0.545 | 1.43x | 24.2/31.4/34.2% | 3.6/7.1% | 3 |
| 60 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 90 | 1 | 0.946 | 0.944 | 0.002 | - | - | 0.997 | 0.998 | 0.759 | 1.53x | 19.4/27.3/31.0% | 1.4/4.8% | 3 |
| 120 | 1 | 0.960 | 0.959 | 0.001 | - | - | 1.000 | 1.000 | 0.789 | 1.99x | 24.5/32.0/35.5% | 1.3/5.1% | 3 |
| 150 | 1 | 0.963 | 0.961 | 0.002 | - | - | 1.000 | 1.000 | 0.826 | 2.35x | 27.9/35.6/38.7% | 1.2/5.6% | 3 |

### `MS-hopscale` - nodes  `--scenario rolling`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 120 | 1 | 0.782 | 0.773 | 0.009 | - | - | 0.905 | 0.907 | 0.509 | 2.33x | 16.3/27.1/34.6% | 1.7/4.4% | 3 |
| 250 | 1 | 0.523 | 0.507 | 0.016 | - | - | 0.866 | 0.913 | 0.222 | 4.97x | 17.7/29.5/39.5% | 1.6/5.8% | 3 |
| 500 | 1 | 0.314 | 0.309 | 0.004 | - | - | 0.520 | 0.521 | 0.076 | 10.07x | 18.5/29.4/46.0% | 1.7/6.4% | 3 |

> nodes=250: decode_failures 201

> nodes=500: decode_failures 5

### `MS-oversubscribed` - nodes  `--scenario rolling`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.778 | 0.770 | 0.008 | - | - | 0.912 | 0.913 | 0.533 | 2.14x | 14.9/24.9/31.9% | 1.5/4.0% | 3 |
| 250 | 1 | 0.522 | 0.507 | 0.015 | - | - | 0.850 | 0.911 | 0.228 | 4.70x | 16.8/27.5/36.6% | 1.5/5.3% | 3 |
| 500 | 1 | 0.319 | 0.315 | 0.004 | - | - | 0.539 | 0.539 | 0.076 | 9.22x | 17.0/27.0/42.4% | 1.5/5.5% | 3 |

> nodes=250: decode_failures 106

> nodes=500: decode_failures 6

### `MS-roles` - role-mix  `--scenario rolling`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.905 | 0.901 | 0.004 | - | - | 0.992 | 0.992 | 0.672 | 1.28x | 17.8/26.7/29.6% | 2.0/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.881 | 0.875 | 0.006 | - | - | 0.974 | 0.976 | 0.510 | 1.13x | 15.9/24.9/27.6% | 1.7/5.2% | 3 |

### `MS-roles-fav` - role-mix  `--scenario rolling`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.921 | 0.918 | 0.004 | - | - | 0.992 | 0.992 | 0.715 | 1.36x | 18.9/28.0/31.2% | 2.0/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.890 | 0.886 | 0.004 | - | - | 0.962 | 0.962 | 0.549 | 1.26x | 17.8/29.5/31.5% | 2.0/5.1% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario rolling`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 0.05 | 1 | 0.896 | 0.891 | 0.006 | - | - | 0.978 | 0.978 | 0.719 | 1.45x | 19.5/34.1/37.5% | 2.1/5.3% | 3 |
| 0.1 | 1 | 0.897 | 0.894 | 0.004 | - | - | 0.963 | 0.964 | 0.715 | 1.58x | 20.4/38.8/41.8% | 2.2/5.4% | 3 |
| 0.2 | 1 | 0.912 | 0.909 | 0.003 | - | - | 0.979 | 0.979 | 0.731 | 1.79x | 23.8/42.7/47.1% | 2.5/5.3% | 3 |

> router-late-fraction=0.1: misdecodes 1

### `MS-siting` - siting-mix  `--scenario rolling`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| local-typical | 1 | 0.630 | 0.612 | 0.017 | - | - | 0.834 | 0.836 | 0.000 | 1.33x | 14.1/24.1/29.1% | 2.1/5.1% | 3 |
| event | 1 | 0.234 | 0.228 | 0.006 | - | - | 0.422 | 0.423 | 0.000 | 1.14x | 5.7/18.0/23.4% | 1.3/4.9% | 3 |
| backbone | 1 | 0.972 | 0.972 | 0.000 | - | - | 0.995 | 0.995 | 0.881 | 1.13x | 29.4/37.5/39.9% | 1.4/5.6% | 3 |

### `MS-size` - nodes  `--scenario rolling`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.896 | 0.885 | 0.011 | - | - | 0.969 | 0.972 | 0.700 | 1.45x | 32.1/39.1/41.7% | 3.5/7.7% | 3 |
| 60 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 90 | 1 | 0.796 | 0.787 | 0.010 | - | - | 0.975 | 0.977 | 0.568 | 1.76x | 15.2/29.7/34.9% | 1.8/4.3% | 3 |
| 120 | 1 | 0.782 | 0.773 | 0.009 | - | - | 0.905 | 0.907 | 0.509 | 2.33x | 16.3/27.1/34.6% | 1.7/4.4% | 3 |
| 150 | 1 | 0.656 | 0.644 | 0.011 | - | - | 0.751 | 0.752 | 0.403 | 2.58x | 15.5/22.0/25.3% | 1.5/4.3% | 3 |

### `MS-stretch` - stretch  `--scenario rolling`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 1.25 | 1 | 0.698 | 0.686 | 0.012 | - | - | 0.891 | 0.894 | 0.286 | 1.37x | 14.2/22.6/26.6% | 2.0/5.1% | 3 |
| 1.5 | 1 | 0.491 | 0.475 | 0.015 | - | - | 0.723 | 0.725 | 0.031 | 1.39x | 11.0/19.5/23.7% | 2.3/4.6% | 3 |
| 2.0 | 1 | 0.123 | 0.121 | 0.002 | - | - | 0.262 | 0.275 | 0.000 | 0.94x | 3.5/15.4/19.1% | 1.3/4.3% | 3 |

> stretch=2.0: decode_failures 8

### `MS-topology` - topology  `--scenario rolling`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| clustered | 1 | 0.906 | 0.905 | 0.001 | - | - | 0.979 | 0.981 | 0.000 | 1.23x | 27.8/37.2/39.2% | 1.7/5.5% | 3 |
| corridor | 1 | 0.736 | 0.721 | 0.015 | - | - | 0.906 | 0.937 | 0.303 | 1.22x | 16.3/27.3/30.1% | 1.8/5.4% | 3 |
| hub | 1 | 0.955 | 0.955 | 0.000 | - | - | 0.993 | 0.993 | 0.752 | 1.20x | 27.3/37.6/38.9% | 1.5/5.5% | 3 |

> topology=corridor: decode_failures 46

> slower: 3.95 s per simulated hour against 1.91 over 56 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-crladder` - coding-rate-ladder  `--scenario rolling`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.876 | 0.876 | 0.000 | - | - | 0.971 | 0.975 | 0.674 | 1.60x | 22.2/33.5/36.7% | 2.5/6.7% | 3 |
| True | 1 | 0.870 | 0.870 | 0.000 | - | - | 0.960 | 0.963 | 0.680 | 1.59x | 22.0/33.1/36.5% | 2.4/6.5% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario rolling`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.870 | 0.870 | 0.000 | - | - | 0.960 | 0.963 | 0.680 | 1.59x | 22.0/33.1/36.5% | 2.4/6.5% | 3 |
| m4-early-flood | 1 | 0.868 | 0.868 | 0.000 | - | - | 0.959 | 0.960 | 0.678 | 1.60x | 22.2/33.5/36.9% | 2.4/6.6% | 3 |

### `PR-protocol` - protocol  `--scenario rolling`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.904 | 0.904 | 0.000 | - | - | 0 | 0.000 | 0.726 | 1.27x | 17.9/26.4/29.0% | 1.9/5.2% | 3 |
| chain | 1 | 0.899 | 0.898 | 0.002 | - | - | 0.939 | 0.980 | 0.739 | 1.50x | 20.9/31.0/34.3% | 2.3/6.1% | 3 |
| sr | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |

### `PR-repeats` - extra-repeats  `--scenario rolling`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| True | 1 | 0.906 | 0.902 | 0.005 | - | - | 0.975 | 0.975 | 0.748 | 1.31x | 18.3/27.1/30.0% | 2.0/5.4% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario rolling`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.960 | 0.959 | 0.001 | - | - | 1.000 | 1.000 | 0.789 | 1.99x | 24.5/32.0/35.5% | 1.3/5.1% | 3 |
| True | 1 | 0.961 | 0.961 | 0.001 | - | - | 1.000 | 1.000 | 0.808 | 2.02x | 24.8/32.3/35.8% | 1.3/5.1% | 3 |

### `RF-bw500` - preset  `--scenario rolling`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.175 | 0.174 | 0.000 | - | - | 0.343 | 0.345 | 0.000 | 0.05x | 0.2/0.9/1.3% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.568 | 0.554 | 0.014 | - | - | 0.806 | 0.810 | 0.031 | 0.34x | 2.7/5.6/6.8% | 0.5/1.2% | 3 |
| LONG_TURBO | 1 | 0.838 | 0.823 | 0.015 | - | - | 0.931 | 0.931 | 0.585 | 1.28x | 14.6/21.6/25.1% | 1.9/4.8% | 3 |

### `RF-duct` - duct-per-hour  `--scenario rolling`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 0.25 | 1 | 0.914 | 0.909 | 0.005 | - | - | 0.983 | 0.983 | 0.747 | 1.24x | 19.5/27.4/30.0% | 1.8/5.3% | 3 |
| 1.0 | 1 | 0.943 | 0.938 | 0.004 | - | - | 0.991 | 0.991 | 0.825 | 1.03x | 23.0/29.6/31.9% | 1.4/5.3% | 3 |

### `RF-eu-presets` - preset  `--scenario rolling`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.435 | 0.427 | 0.008 | - | - | 0.698 | 0.703 | 0.031 | 0.18x | 1.2/2.7/3.8% | 0.3/0.8% | 3 |
| LONG_FAST | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| LITE_FAST | 1 | 0.860 | 0.852 | 0.008 | - | - | 0.954 | 0.954 | 0.432 | 1.05x | 12.7/21.1/23.4% | 1.6/3.9% | 3 |
| NARROW_SLOW | 1 | 0.886 | 0.877 | 0.008 | - | - | 0.967 | 0.970 | 0.715 | 1.34x | 17.0/27.3/29.9% | 2.0/5.0% | 3 |

### `RF-noise` - noise-profile  `--scenario rolling`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| temporal | 1 | 0.830 | 0.822 | 0.008 | - | - | 0.941 | 0.944 | 0.561 | 1.31x | 18.5/26.9/29.1% | 1.9/5.2% | 3 |
| transient | 1 | 0.898 | 0.893 | 0.005 | - | - | 0.969 | 0.970 | 0.730 | 1.30x | 18.1/26.8/29.6% | 2.0/5.3% | 3 |
| periodic | 1 | 0.733 | 0.727 | 0.006 | - | - | 0.804 | 0.806 | 0.552 | 1.23x | 17.5/25.3/27.9% | 1.9/4.7% | 3 |

### `RF-preset` - preset  `--scenario rolling`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.435 | 0.427 | 0.008 | - | - | 0.698 | 0.703 | 0.031 | 0.18x | 1.2/2.7/3.8% | 0.3/0.8% | 3 |
| LONG_FAST | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| LONG_MODERATE | 1 | 0.848 | 0.841 | 0.007 | - | - | 0.936 | 0.937 | 0.658 | 3.35x | 52.2/66.0/69.7% | 4.8/12.7% | 3 |

> faster: 1.27 s per simulated hour against 2.86 over 56 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-preset-turbo` - preset  `--scenario rolling`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.053 | 0.053 | 0.000 | - | - | 0.076 | 0.152 | 0.000 | 0.01x | 0.0/0.1/0.3% | 0.0/0.0% | 2 |
| SHORT_TURBO | 1 | 0.175 | 0.174 | 0.000 | - | - | 0.343 | 0.345 | 0.000 | 0.05x | 0.2/0.9/1.3% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| LONG_TURBO | 1 | 0.838 | 0.823 | 0.015 | - | - | 0.931 | 0.931 | 0.585 | 1.28x | 14.6/21.6/25.1% | 1.9/4.8% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.881 | 0.876 | 0.005 | - | - | 0.959 | 0.959 | 0.610 | 1.81x | 23.8/34.9/36.6% | 2.8/7.1% | 3 |

> preset=EXTRA_SHORT_TURBO: 3 archives requested, 2 placed - group on the placed count

### `RF-pulse` - noise-pulse-interval-ms  `--scenario rolling`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.843 | 0.837 | 0.006 | - | - | 0.915 | 0.917 | 0.659 | 1.29x | 18.3/26.8/29.6% | 2.0/5.2% | 3 |
| 10000 | 1 | 0.733 | 0.727 | 0.006 | - | - | 0.804 | 0.806 | 0.552 | 1.23x | 17.5/25.3/27.9% | 1.9/4.7% | 3 |
| 4000 | 1 | 0.505 | 0.502 | 0.003 | - | - | 0.552 | 0.596 | 0.302 | 1.08x | 15.7/22.3/24.7% | 1.7/3.6% | 3 |
| 2000 | 1 | 0.126 | 0.126 | 0.000 | - | - | 0.123 | 0.195 | 0.072 | 0.76x | 11.5/16.8/18.3% | 1.2/2.0% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 5

### `RF-stretch-duct` - duct-per-hour  `--scenario rolling`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.491 | 0.475 | 0.015 | - | - | 0.723 | 0.725 | 0.031 | 1.39x | 11.0/19.5/23.7% | 2.3/4.6% | 3 |
| 1.0 | 1 | 0.710 | 0.689 | 0.022 | - | - | 0.853 | 0.854 | 0.364 | 1.16x | 16.7/24.2/26.5% | 1.7/4.7% | 3 |

### `RF-txpower` - tx-power  `--scenario rolling`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 22 | 1 | 0.521 | 0.499 | 0.022 | - | - | 0.765 | 0.769 | 0.031 | 1.39x | 11.0/20.7/25.0% | 2.3/4.8% | 3 |
| 17 | 1 | 0.157 | 0.154 | 0.003 | - | - | 0.308 | 0.310 | 0.000 | 1.18x | 5.3/17.9/21.0% | 1.8/4.5% | 3 |
| 14 | 1 | 0.078 | 0.077 | 0.001 | - | - | 0.149 | 0.190 | 0.000 | 0.74x | 2.3/12.0/16.3% | 0.9/3.4% | 3 |

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario rolling`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.960 | 0.959 | 0.001 | - | - | 1.000 | 1.000 | 0.789 | 1.99x | 24.5/32.0/35.5% | 1.3/5.1% | 3 |
| True | 1 | 0.958 | 0.957 | 0.001 | - | - | 0.998 | 0.999 | 0.787 | 2.32x | 28.0/36.0/39.7% | 1.5/5.8% | 3 |

### `RT-favourites` - favourite-routers  `--scenario rolling`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.888 | 0.883 | 0.005 | - | - | 0.965 | 0.966 | 0.714 | 1.43x | 19.0/32.9/35.7% | 2.1/5.3% | 3 |
| True | 1 | 0.911 | 0.905 | 0.005 | - | - | 0.979 | 0.980 | 0.743 | 1.48x | 19.6/33.7/36.7% | 2.1/5.3% | 3 |

### `RT-hopassign` - hop-assign  `--scenario rolling`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| random | 1 | 0.900 | 0.890 | 0.010 | - | - | 0.989 | 0.991 | 0.690 | 1.30x | 18.4/26.5/29.4% | 2.0/5.2% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario rolling`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.776 | 0.758 | 0.019 | - | - | 0.977 | 0.979 | 0.418 | 0.96x | 13.7/22.1/25.0% | 1.4/4.6% | 3 |
| 7 | 1 | 0.954 | 0.952 | 0.002 | - | - | 0.997 | 0.997 | 0.847 | 1.39x | 19.5/27.7/30.5% | 2.2/5.3% | 3 |
| 15 | 1 | 0.958 | 0.957 | 0.001 | - | - | 0.991 | 0.991 | 0.883 | 1.42x | 19.9/28.0/30.8% | 2.2/5.4% | 3 |
| 32 | 1 | 0.958 | 0.957 | 0.001 | - | - | 0.991 | 0.991 | 0.883 | 1.42x | 19.9/28.0/30.8% | 2.2/5.4% | 3 |

### `RT-hopspread` - hop-limit  `--scenario rolling`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.776 | 0.758 | 0.019 | - | - | 0.977 | 0.979 | 0.418 | 0.96x | 13.7/22.1/25.0% | 1.4/4.6% | 3 |
| 5 | 1 | 0.917 | 0.911 | 0.006 | - | - | 0.995 | 0.995 | 0.771 | 1.29x | 18.2/26.9/29.7% | 2.0/5.3% | 3 |
| 7 | 1 | 0.954 | 0.952 | 0.002 | - | - | 0.997 | 0.997 | 0.847 | 1.39x | 19.5/27.7/30.5% | 2.2/5.3% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario rolling`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| KNOWN_ONLY | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.908 | 0.908 | 0.000 | - | - | 0.950 | 0.982 | 0.740 | 1.27x | 17.9/26.4/29.0% | 1.9/5.1% | 3 |

### `RT-spread` - hop-spread  `--scenario rolling`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.776 | 0.758 | 0.019 | - | - | 0.977 | 0.979 | 0.418 | 0.96x | 13.7/22.1/25.0% | 1.4/4.6% | 3 |
| True | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |

> faster: 1.11 s per simulated hour against 2.24 over 56 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SC-signing` - signature-policy  `--scenario rolling`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| BALANCED | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| STRICT | 1 | 0.771 | 0.771 | 0.000 | - | - | 0.848 | 0.848 | 0.586 | 1.43x | 20.0/29.1/32.3% | 2.2/5.7% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario rolling`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| dm | 1 | 0.904 | 0.899 | 0.005 | - | - | 0.976 | 0.976 | 0.727 | 1.29x | 18.0/26.7/29.7% | 2.0/5.4% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario rolling`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.895 | 0.890 | 0.004 | - | - | 0.970 | 0.972 | 0.700 | 1.32x | 18.5/27.4/30.2% | 2.0/5.4% | 3 |
| local | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| time | 1 | 0.905 | 0.900 | 0.004 | - | - | 0.979 | 0.981 | 0.713 | 1.35x | 18.7/27.9/30.8% | 2.1/5.6% | 3 |
| window | 1 | 0.896 | 0.891 | 0.005 | - | - | 0.972 | 0.975 | 0.687 | 1.32x | 18.4/27.1/29.9% | 2.0/5.4% | 3 |

> bucket-mode=global: misdecodes 32

> bucket-mode=time: misdecodes 32

> bucket-mode=window: misdecodes 18

### `SF-bucket-time` - time-bucket-s  `--scenario rolling`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.895 | 0.890 | 0.005 | - | - | 0.976 | 0.977 | 0.712 | 1.47x | 20.1/30.1/33.2% | 2.3/6.1% | 3 |
| 1800 | 1 | 0.905 | 0.900 | 0.004 | - | - | 0.979 | 0.981 | 0.713 | 1.35x | 18.7/27.9/30.8% | 2.1/5.6% | 3 |
| 3600 | 1 | 0.903 | 0.899 | 0.004 | - | - | 0.973 | 0.976 | 0.703 | 1.31x | 18.2/27.0/29.8% | 2.0/5.4% | 3 |

> time-bucket-s=600: misdecodes 132

> time-bucket-s=1800: misdecodes 32

> time-bucket-s=3600: misdecodes 20

### `SF-cadence` - trigger  `--scenario rolling`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| interval | 1 | 0.884 | 0.877 | 0.006 | - | - | 0.962 | 0.965 | 0.700 | 1.76x | 23.7/35.9/40.1% | 2.6/7.6% | 3 |
| aimd | 1 | 0.902 | 0.901 | 0.002 | - | - | 0.949 | 0.979 | 0.725 | 1.29x | 18.2/27.0/29.6% | 2.0/5.3% | 3 |
| bucket+interval | 1 | 0.872 | 0.864 | 0.008 | - | - | 0.958 | 0.958 | 0.666 | 1.81x | 24.5/37.5/42.0% | 2.6/8.4% | 3 |

> trigger=interval: misdecodes 20

> trigger=aimd: misdecodes 2

> trigger=bucket+interval: misdecodes 35

### `SF-capacity` - capacity  `--scenario rolling`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.908 | 0.905 | 0.003 | - | - | 0.979 | 0.980 | 0.734 | 1.30x | 18.2/27.0/29.8% | 2.0/5.4% | 3 |
| 8 | 1 | 0.895 | 0.890 | 0.005 | - | - | 0.969 | 0.970 | 0.713 | 1.29x | 18.0/26.7/29.4% | 2.0/5.3% | 3 |
| 16 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.31x | 18.3/27.1/30.0% | 2.0/5.4% | 3 |
| 32 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 50 | 1 | 0.899 | 0.894 | 0.005 | - | - | 0.976 | 0.976 | 0.719 | 1.30x | 18.2/27.0/29.9% | 2.0/5.4% | 3 |

> capacity=4: decode_failures 53

> capacity=8: decode_failures 18

### `SF-capacity-local` - capacity  `--scenario rolling`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.908 | 0.905 | 0.003 | - | - | 0.979 | 0.980 | 0.734 | 1.30x | 18.2/27.0/29.8% | 2.0/5.4% | 3 |
| 8 | 1 | 0.895 | 0.890 | 0.005 | - | - | 0.969 | 0.970 | 0.713 | 1.29x | 18.0/26.7/29.4% | 2.0/5.3% | 3 |
| 16 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.31x | 18.3/27.1/30.0% | 2.0/5.4% | 3 |
| 32 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 50 | 1 | 0.899 | 0.894 | 0.005 | - | - | 0.976 | 0.976 | 0.719 | 1.30x | 18.2/27.0/29.9% | 2.0/5.4% | 3 |

> capacity=4: decode_failures 53

> capacity=8: decode_failures 18

### `SF-capacity-window` - capacity  `--scenario rolling`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.902 | 0.897 | 0.005 | - | - | 0.970 | 0.973 | 0.720 | 1.30x | 18.3/27.0/29.6% | 2.0/5.3% | 3 |
| 16 | 1 | 0.900 | 0.896 | 0.004 | - | - | 0.976 | 0.976 | 0.717 | 1.30x | 18.2/27.0/29.7% | 2.0/5.3% | 3 |
| 32 | 1 | 0.896 | 0.891 | 0.005 | - | - | 0.972 | 0.975 | 0.687 | 1.32x | 18.4/27.1/29.9% | 2.0/5.4% | 3 |

> capacity=8: misdecodes 25

> capacity=8: decode_failures 1

> capacity=16: misdecodes 31

> capacity=32: misdecodes 18

### `SF-catchup` - catch-up-hours  `--scenario rolling`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.872 | 0.864 | 0.008 | - | - | 0.958 | 0.958 | 0.666 | 1.81x | 24.5/37.5/42.0% | 2.6/8.4% | 3 |
| 02-06 | 1 | 0.907 | 0.904 | 0.003 | - | - | 0.963 | 0.981 | 0.718 | 1.34x | 18.6/27.6/30.6% | 2.1/5.6% | 3 |
| 00-08 | 1 | 0.909 | 0.905 | 0.004 | - | - | 0.970 | 0.982 | 0.708 | 1.41x | 19.4/28.9/32.2% | 2.2/5.9% | 3 |

> catch-up-hours=: misdecodes 35

> catch-up-hours=02-06: decode_failures 23

> catch-up-hours=00-08: misdecodes 1

> catch-up-hours=00-08: decode_failures 21

### `SF-hops-flat` - hops-apart  `--scenario rolling`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.898 | 0.896 | 0.003 | - | - | 0.963 | 0.964 | 0.725 | 1.31x | 18.4/27.2/29.9% | 2.1/5.4% | 3 |
| 2 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 3 | 1 | 0.904 | 0.891 | 0.013 | - | - | 0.983 | 0.984 | 0.734 | 1.32x | 18.6/27.2/29.9% | 2.0/5.4% | 3 |
| 4 | 1 | 0.905 | 0.896 | 0.009 | - | - | 0.931 | 0.983 | 0.723 | 1.32x | 18.8/27.6/30.3% | 2.0/5.4% | 3 |

> hops-apart=4: decode_failures 46

### `SF-hops-spread` - hops-apart  `--scenario rolling`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.898 | 0.896 | 0.003 | - | - | 0.963 | 0.964 | 0.725 | 1.31x | 18.4/27.2/29.9% | 2.1/5.4% | 3 |
| 2 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 3 | 1 | 0.904 | 0.891 | 0.013 | - | - | 0.983 | 0.984 | 0.734 | 1.32x | 18.6/27.2/29.9% | 2.0/5.4% | 3 |
| 4 | 1 | 0.905 | 0.896 | 0.009 | - | - | 0.931 | 0.983 | 0.723 | 1.32x | 18.8/27.6/30.3% | 2.0/5.4% | 3 |
| 5 | 1 | 0.926 | 0.902 | 0.024 | - | - | 0.978 | 0.986 | 0.723 | 1.29x | 18.3/27.0/29.5% | 2.0/5.3% | 3 |

> hops-apart=4: decode_failures 46

### `SF-jitter-global` - advert-jitter-s  `--scenario rolling`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.896 | 0.892 | 0.004 | - | - | 0.969 | 0.970 | 0.723 | 1.30x | 18.2/26.9/29.6% | 2.0/5.4% | 3 |
| 30 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 120 | 1 | 0.902 | 0.897 | 0.005 | - | - | 0.978 | 0.979 | 0.733 | 1.33x | 18.4/27.3/30.2% | 2.0/5.4% | 3 |
| 600 | 1 | 0.897 | 0.893 | 0.004 | - | - | 0.972 | 0.973 | 0.728 | 1.32x | 18.4/27.1/30.1% | 2.0/5.4% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario rolling`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.896 | 0.892 | 0.004 | - | - | 0.969 | 0.970 | 0.723 | 1.30x | 18.2/26.9/29.6% | 2.0/5.4% | 3 |
| 30 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 120 | 1 | 0.902 | 0.897 | 0.005 | - | - | 0.978 | 0.979 | 0.733 | 1.33x | 18.4/27.3/30.2% | 2.0/5.4% | 3 |
| 600 | 1 | 0.897 | 0.893 | 0.004 | - | - | 0.972 | 0.973 | 0.728 | 1.32x | 18.4/27.1/30.1% | 2.0/5.4% | 3 |

### `SF-place-flat` - place  `--scenario rolling`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.914 | 0.894 | 0.020 | - | - | 0.938 | 0.974 | 0.725 | 1.35x | 19.4/27.9/30.5% | 2.1/5.4% | 3 |
| routers | 1 | 0.909 | 0.907 | 0.003 | - | - | 0.981 | 0.981 | 0.736 | 1.31x | 18.2/27.2/30.0% | 2.0/5.3% | 3 |
| alternate-routers | 1 | 0.901 | 0.899 | 0.002 | - | - | 0.968 | 0.969 | 0.728 | 1.31x | 18.4/27.3/29.9% | 2.0/5.3% | 3 |
| beside-router | 1 | 0.897 | 0.894 | 0.003 | - | - | 0.959 | 0.959 | 0.732 | 1.30x | 18.2/27.0/29.8% | 2.0/5.3% | 3 |
| random-clients | 1 | 0.903 | 0.894 | 0.009 | - | - | 0.979 | 0.980 | 0.716 | 1.31x | 18.5/27.3/30.0% | 2.0/5.3% | 3 |
| hops-apart | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |

> place=spread: decode_failures 29

### `SF-place-spread` - place  `--scenario rolling`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.914 | 0.894 | 0.020 | - | - | 0.938 | 0.974 | 0.725 | 1.35x | 19.4/27.9/30.5% | 2.1/5.4% | 3 |
| routers | 1 | 0.909 | 0.907 | 0.003 | - | - | 0.981 | 0.981 | 0.736 | 1.31x | 18.2/27.2/30.0% | 2.0/5.3% | 3 |
| alternate-routers | 1 | 0.901 | 0.899 | 0.002 | - | - | 0.968 | 0.969 | 0.728 | 1.31x | 18.4/27.3/29.9% | 2.0/5.3% | 3 |
| beside-router | 1 | 0.897 | 0.894 | 0.003 | - | - | 0.959 | 0.959 | 0.732 | 1.30x | 18.2/27.0/29.8% | 2.0/5.3% | 3 |
| random-clients | 1 | 0.903 | 0.894 | 0.009 | - | - | 0.979 | 0.980 | 0.716 | 1.31x | 18.5/27.3/30.0% | 2.0/5.3% | 3 |
| hops-apart | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |

> place=spread: decode_failures 29

### `SF-provide-transport` - provide-transport  `--scenario rolling`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| broadcast | 1 | 0.912 | 0.892 | 0.020 | - | - | 0.972 | 0.972 | 0.751 | 1.35x | 18.7/27.8/30.6% | 2.1/5.5% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario rolling`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| heard | 1 | 0.907 | 0.901 | 0.006 | - | - | 0.982 | 0.983 | 0.723 | 1.32x | 18.4/27.2/30.0% | 2.0/5.4% | 3 |

> replay-ordering=heard: misdecodes 19

### `SF-replay-order-broadcast` - replay-ordering  `--scenario rolling`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.912 | 0.892 | 0.020 | - | - | 0.972 | 0.972 | 0.751 | 1.35x | 18.7/27.8/30.6% | 2.1/5.5% | 3 |
| heard | 1 | 0.918 | 0.895 | 0.024 | - | - | 0.980 | 0.981 | 0.759 | 1.36x | 19.0/27.9/30.7% | 2.1/5.5% | 3 |

> replay-ordering=heard: misdecodes 18

### `SF-resolve` - resolve  `--scenario rolling`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| enum | 1 | 0.902 | 0.897 | 0.005 | - | - | 0.973 | 0.980 | 0.725 | 1.30x | 18.2/27.0/30.0% | 2.0/5.5% | 3 |
| hybrid | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |

### `SF-servers-allrouters` - servers  `--scenario rolling`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.909 | 0.907 | 0.003 | - | - | 0.981 | 0.981 | 0.736 | 1.31x | 18.2/27.2/30.0% | 2.0/5.3% | 3 |
| 6 | 1 | 0.900 | 0.896 | 0.004 | - | - | 0.976 | 0.976 | 0.716 | 1.34x | 18.6/28.0/30.7% | 2.0/5.6% | 6 |

### `SF-servers-flat` - servers  `--scenario rolling`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.899 | 0.896 | 0.003 | - | - | 0.966 | 0.968 | 0.710 | 1.31x | 18.3/27.2/29.9% | 2.0/5.3% | 2 |
| 3 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 5 | 1 | 0.906 | 0.893 | 0.013 | - | - | 0.981 | 0.981 | 0.727 | 1.35x | 18.9/28.1/30.8% | 2.1/5.7% | 5 |
| 8 | 1 | 0.896 | 0.882 | 0.014 | - | - | 0.971 | 0.974 | 0.712 | 1.37x | 19.2/28.6/31.3% | 2.1/5.7% | 8 |

### `SF-servers-spread` - servers  `--scenario rolling`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.899 | 0.896 | 0.003 | - | - | 0.966 | 0.968 | 0.710 | 1.31x | 18.3/27.2/29.9% | 2.0/5.3% | 2 |
| 3 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 5 | 1 | 0.906 | 0.893 | 0.013 | - | - | 0.981 | 0.981 | 0.727 | 1.35x | 18.9/28.1/30.8% | 2.1/5.7% | 5 |
| 8 | 1 | 0.896 | 0.882 | 0.014 | - | - | 0.971 | 0.974 | 0.712 | 1.37x | 19.2/28.6/31.3% | 2.1/5.7% | 8 |

### `SF-signed` - signed  `--scenario rolling`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| True | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario rolling`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.893 | 0.887 | 0.006 | - | - | 0.968 | 0.972 | 0.690 | 1.22x | 17.0/25.4/28.1% | 1.9/5.0% | 3 |
| 1 | 1 | 0.908 | 0.903 | 0.005 | - | - | 0.985 | 0.985 | 0.707 | 1.21x | 16.8/25.1/27.8% | 1.9/5.0% | 3 |
| 2 | 1 | 0.894 | 0.890 | 0.004 | - | - | 0.974 | 0.975 | 0.714 | 1.19x | 16.5/24.8/27.5% | 1.9/4.9% | 3 |
| 4 | 1 | 0.894 | 0.890 | 0.004 | - | - | 0.970 | 0.970 | 0.722 | 1.22x | 17.0/25.4/28.0% | 1.9/5.0% | 3 |

### `SF-width` - short-id-bits  `--scenario rolling`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.901 | 0.896 | 0.004 | - | - | 0.970 | 0.971 | 0.729 | 1.31x | 18.4/27.1/29.7% | 2.0/5.3% | 3 |
| 24 | 1 | 0.900 | 0.895 | 0.005 | - | - | 0.976 | 0.979 | 0.731 | 1.32x | 18.5/27.3/30.2% | 2.0/5.4% | 3 |
| 32 | 1 | 0.898 | 0.894 | 0.004 | - | - | 0.968 | 0.970 | 0.722 | 1.29x | 18.1/26.8/29.5% | 2.0/5.3% | 3 |
| 64 | 1 | 0.904 | 0.899 | 0.005 | - | - | 0.975 | 0.976 | 0.740 | 1.31x | 18.4/27.1/29.9% | 2.0/5.4% | 3 |

### `SF-window-size` - window-size  `--scenario rolling`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.890 | 0.885 | 0.005 | - | - | 0.967 | 0.969 | 0.717 | 1.41x | 19.5/28.9/31.9% | 2.2/5.7% | 3 |
| 16 | 1 | 0.903 | 0.897 | 0.006 | - | - | 0.977 | 0.978 | 0.723 | 1.34x | 18.8/27.8/30.6% | 2.1/5.5% | 3 |
| 32 | 1 | 0.896 | 0.891 | 0.005 | - | - | 0.972 | 0.975 | 0.687 | 1.32x | 18.4/27.1/29.9% | 2.0/5.4% | 3 |

> window-size=8: misdecodes 144

> window-size=16: misdecodes 72

> window-size=32: misdecodes 18

### `TH-congestion` - no-congestion-scaling  `--scenario rolling`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.960 | 0.959 | 0.001 | - | - | 1.000 | 1.000 | 0.789 | 1.99x | 24.5/32.0/35.5% | 1.3/5.1% | 3 |
| True | 1 | 0.752 | 0.751 | 0.002 | - | - | 0.860 | 0.944 | 0.567 | 5.68x | 63.3/71.9/75.5% | 4.1/11.8% | 3 |

> no-congestion-scaling=True: queue drops 13.2% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 96

### `TH-congestion-input` - congestion-input  `--scenario rolling`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.522 | 0.507 | 0.015 | - | - | 0.850 | 0.911 | 0.228 | 4.70x | 16.8/27.5/36.6% | 1.5/5.3% | 3 |
| truesize | 1 | 0.557 | 0.543 | 0.014 | - | - | 0.898 | 0.934 | 0.243 | 3.55x | 12.4/22.3/30.0% | 1.1/4.3% | 3 |

> congestion-input=hotstore: decode_failures 106

> congestion-input=truesize: decode_failures 69

> slower: 46.5 s per simulated hour against 11.1 over 56 prior run(s) - 4.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `TH-congestion-mode` - congestion-mode  `--scenario rolling`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.965 | 0.965 | 0.001 | - | - | 0.999 | 0.999 | 0.810 | 1.85x | 22.8/29.8/33.1% | 1.2/4.7% | 3 |
| adaptive | 1 | 0.960 | 0.959 | 0.001 | - | - | 1.000 | 1.000 | 0.789 | 1.99x | 24.5/32.0/35.5% | 1.3/5.1% | 3 |

