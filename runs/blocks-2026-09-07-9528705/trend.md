# Sweep blocks-2026-09-07-9528705

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** rolling
- **seed base** 9528705 · seeds 9528705
- **blocks** 87 run
- **compute** 11.8 h of simulator time across every cell
- **generated** 2026-09-07T08:53:01+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>101 warnings</summary>

- AD-siting: siting-mix=local-typical: decode_failures 17
- AD-siting: siting-mix=basement-heavy: decode_failures 1
- AD-siting: slower: 3.12 s per simulated hour against 1.35 over 17 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- BL-control: protocol=sr: decode_failures 23
- BL-control: slower: 4.55 s per simulated hour against 1.74 over 17 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 51
- DB-warm: warm-num-nodes=0: queue drops 19.6% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 119
- DB-warm: warm-num-nodes=25: queue drops 19.6% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 119
- DB-warm: warm-num-nodes=100: queue drops 19.6% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 119
- DB-warm: warm-num-nodes=2000: queue drops 19.6% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 119
- DG-burst: burst-loss=0.1: decode_failures 1
- DG-burst: burst-loss=0.2: decode_failures 5
- DG-burst: burst-loss=0.3: decode_failures 31
- DG-loss: extra-loss=0.2: decode_failures 1
- DG-loss: extra-loss=0.3: decode_failures 4
- DG-outage: burst-loss=0.1: decode_failures 28
- DG-outage: burst-loss=0.2: decode_failures 33
- DG-outage: burst-loss=0.3: decode_failures 24
- DM-mode: dm-mode=flood-only: decode_failures 8
- DM-mode: dm-mode=m4-early-flood: decode_failures 1
- FW-versions: profile=2.7: decode_failures 1
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 9
- LD-chatty: broadcast-interval-s=300: decode_failures 26
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 19.6% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 119
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 28.9% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 97
- MS-density: nodes=40: decode_failures 18
- MS-density: nodes=150: misdecodes 1
- MS-hopscale: nodes=250: decode_failures 10
- MS-hopscale: nodes=500: decode_failures 204
- MS-oversubscribed: nodes=500: decode_failures 121
- MS-siting: siting-mix=local-typical: decode_failures 11
- MS-siting: siting-mix=event: decode_failures 2
- MS-size: nodes=40: decode_failures 28
- MS-size: nodes=150: decode_failures 2
- MS-stretch: stretch=1.5: decode_failures 28
- MS-stretch: stretch=2.0: decode_failures 3
- MS-topology: topology=clustered: decode_failures 2
- PR-crladder: coding-rate-ladder=True: decode_failures 1
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 1
- PR-repeats-busy: extra-repeats=True: misdecodes 1
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 27
- RF-eu-presets: preset=SHORT_FAST: decode_failures 8
- RF-preset: preset=SHORT_FAST: decode_failures 8
- RF-preset: preset=LONG_MODERATE: decode_failures 16
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 6
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 28
- RF-txpower: tx-power=22: decode_failures 23
- RF-txpower: tx-power=14: decode_failures 1
- RT-hoplimit: hop-limit=3: decode_failures 1
- RT-hopspread: hop-limit=3: decode_failures 1
- RT-spread: hop-spread=False: decode_failures 1
- SF-bucket-mode: bucket-mode=global: misdecodes 35
- SF-bucket-mode: bucket-mode=time: misdecodes 23
- SF-bucket-mode: bucket-mode=window: misdecodes 25
- SF-bucket-time: time-bucket-s=600: misdecodes 131
- SF-bucket-time: time-bucket-s=1800: misdecodes 23
- SF-bucket-time: time-bucket-s=3600: misdecodes 7
- SF-cadence: trigger=interval: misdecodes 15
- SF-cadence: trigger=aimd: misdecodes 2
- SF-cadence: trigger=aimd: decode_failures 3
- SF-cadence: trigger=bucket+interval: misdecodes 14
- SF-capacity-local: capacity=4: decode_failures 96
- SF-capacity-local: capacity=8: decode_failures 72
- SF-capacity-local: capacity=16: decode_failures 2
- SF-capacity: capacity=4: decode_failures 96
- SF-capacity: capacity=8: decode_failures 72
- SF-capacity: capacity=16: decode_failures 2
- SF-capacity-window: capacity=8: misdecodes 21
- SF-capacity-window: capacity=8: decode_failures 33
- SF-capacity-window: capacity=16: misdecodes 14
- SF-capacity-window: capacity=16: decode_failures 3
- SF-capacity-window: capacity=32: misdecodes 25
- SF-catchup: catch-up-hours=: misdecodes 14
- SF-catchup: catch-up-hours=02-06: decode_failures 37
- SF-catchup: catch-up-hours=00-08: misdecodes 1
- SF-catchup: catch-up-hours=00-08: decode_failures 38
- SF-hops-flat: hops-apart=3: decode_failures 23
- SF-hops-flat: hops-apart=4: decode_failures 30
- SF-hops-spread: hops-apart=3: decode_failures 23
- SF-hops-spread: hops-apart=4: decode_failures 30
- SF-hops-spread: hops-apart=5: decode_failures 30
- SF-jitter-global: advert-jitter-s=600: decode_failures 2
- SF-jitter-local: advert-jitter-s=600: decode_failures 2
- SF-place-flat: place=spread: decode_failures 26
- SF-place-spread: place=spread: decode_failures 26
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 3
- SF-replay-order: replay-ordering=heard: misdecodes 10
- SF-servers-flat: servers=8: misdecodes 1
- SF-servers-spread: servers=8: misdecodes 1
- SF-window-size: window-size=8: misdecodes 120
- SF-window-size: window-size=16: misdecodes 58
- SF-window-size: window-size=32: misdecodes 25
- TH-congestion-input: congestion-input=truesize: decode_failures 1
- TH-congestion: no-congestion-scaling=True: queue drops 18.6% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 100

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `BL-control` | 4.55 | 1.74 | 2.61x | 17 |
| `AD-siting` | 3.12 | 1.35 | 2.31x | 17 |
| `RF-txpower` | 2.68 | 1.59 | 1.69x | 17 |
| `MS-oversubscribed` | 30.7 | 18.6 | 1.65x | 17 |
| `RF-bw500` | 3.93 | 2.41 | 1.63x | 17 |
| `MS-hopscale` | 27.3 | 18.1 | 1.51x | 17 |
| `RF-duct` | 1.23 | 1.87 | 0.66x | 17 |
| `AD-worst` | 2.48 | 3.86 | 0.64x | 17 |
| `SC-signing` | 1.27 | 2.11 | 0.60x | 17 |
| `FW-mixed-26` | 1.09 | 1.82 | 0.60x | 17 |
| `RT-favourites` | 0.917 | 1.73 | 0.53x | 17 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.977 | 0.977 | 0.869 → 0.872 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.958 | 0.958 | 0.868 → 0.872 | 1x bytes_on_air | up | 2 |
| `RF-preset-turbo` | preset | **held** | 0.039 → 0.977 | 0.938 | 0.057 → 0.871 | 63x sr_bytes | up | 5 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.103 → 0.932 | 0.829 | 0.090 → 0.815 | 1.5e+02x sr_airtime | down | 4 |
| `MS-siting` | siting-mix | **text** | 0.154 → 0.979 | 0.826 | 0.152 → 0.978 | 4.9x sr_airtime | up | 4 |
| `RF-txpower` | tx-power | **held** | 0.194 → 0.977 | 0.783 | 0.100 → 0.871 | 7.4x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **text** | 0.084 → 0.857 | 0.772 | 0.082 → 0.842 | 3.6x advert_bytes | down | 3 |
| `MS-stretch` | stretch | **text** | 0.114 → 0.884 | 0.770 | 0.112 → 0.871 | 7x sr_airtime | down | 4 |
| `RF-bw500` | preset | **held** | 0.195 → 0.910 | 0.716 | 0.159 → 0.783 | 5.3x sr_airtime | up | 3 |
| `RF-eu-presets` | preset | **text** | 0.254 → 0.884 | 0.630 | 0.245 → 0.871 | 2.5x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.254 → 0.884 | 0.630 | 0.245 → 0.871 | 2.5x sr_airtime | up | 3 |
| `MS-hopscale` | nodes | **text** | 0.317 → 0.884 | 0.567 | 0.310 → 0.871 | 11x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **text** | 0.321 → 0.812 | 0.492 | 0.314 → 0.803 | 5.5x sr_bytes | down | 3 |
| `MS-topology` | topology | **held** | 0.568 → 0.994 | 0.426 | 0.552 → 0.967 | 3.4x sr_airtime | up | 4 |
| `MS-density` | nodes | **text** | 0.554 → 0.970 | 0.415 | 0.534 → 0.969 | 5.8x advert_bytes | up | 5 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.451 → 0.823 | 0.372 | 0.331 → 0.565 | 5.9x sr_airtime | up | 3 |
| `DG-outage` | burst-loss | **text** | 0.537 → 0.884 | 0.347 | 0.514 → 0.871 | 1.8x sr_bytes | down | 4 |
| `DG-burst` | burst-loss | **text** | 0.567 → 0.884 | 0.317 | 0.533 → 0.871 | 1.8x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.605 → 0.908 | 0.303 | 0.574 → 0.899 | 6x sr_airtime | down | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.644 → 0.942 | 0.298 | 0.624 → 0.939 | 6.3x sr_airtime | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.351 → 0.638 | 0.286 | 0.343 → 0.616 | 1.8x sr_airtime | up | 2 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.720 → 0.970 | 0.250 | 0.715 → 0.969 | 5x sr_airtime | down | 2 |
| `RT-hoplimit` | hop-limit | **text** | 0.727 → 0.949 | 0.223 | 0.685 → 0.946 | 3.3x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.727 → 0.932 | 0.205 | 0.685 → 0.927 | 2.8x sr_bytes | up | 3 |
| `MS-size` | nodes | **held** | 0.811 → 0.977 | 0.166 | 0.733 → 0.871 | 3.4x sr_airtime | down | 5 |
| `RF-noise` | noise-profile | **text** | 0.723 → 0.884 | 0.161 | 0.708 → 0.871 | 1.4x sr_bytes | down | 4 |
| `RT-spread` | hop-spread | **text** | 0.727 → 0.884 | 0.157 | 0.685 → 0.871 | 2x sr_bytes | up | 2 |
| `SC-signing` | signature-policy | **text** | 0.752 → 0.884 | 0.132 | 0.752 → 0.871 | 1.3x sr_airtime | down | 3 |
| `DG-loss` | extra-loss | **text** | 0.765 → 0.884 | 0.119 | 0.745 → 0.871 | 1.5x sr_bytes | down | 4 |
| `SF-place-flat` | place | **held** | 0.860 → 0.977 | 0.117 | 0.866 → 0.879 | 4.1x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.860 → 0.977 | 0.117 | 0.866 → 0.879 | 4.1x sr_bytes | up | 6 |
| `DB-hotstore` | max-num-nodes | **text** | 0.833 → 0.928 | 0.095 | 0.824 → 0.925 | 2x sr_airtime | up | 4 |
| `LD-interval` | broadcast-interval-s | **text** | 0.835 → 0.921 | 0.086 | 0.818 → 0.916 | 5.1x sr_airtime | up | 4 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.884 → 0.964 | 0.080 | 0.871 → 0.963 | 1.9x sr_bytes | up | 3 |
| `AD-flooding` | role-mix | **text** | 0.857 → 0.936 | 0.080 | 0.842 → 0.932 | 2.5x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.857 → 0.936 | 0.080 | 0.842 → 0.932 | 2.5x bytes_on_air | up | 3 |
| `DB-platform` | platform-mix | **text** | 0.849 → 0.928 | 0.080 | 0.839 → 0.925 | 2x sr_airtime | down | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.629 → 0.706 | 0.077 | 0.624 → 0.699 | 1.4x sr_airtime | down | 2 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.904 → 0.977 | 0.073 | 0.871 → 0.881 | 28x sr_airtime | down | 3 |
| `SF-hops-flat` | hops-apart | **held** | 0.909 → 0.977 | 0.067 | 0.867 → 0.879 | 3.7x sr_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.909 → 0.977 | 0.067 | 0.867 → 0.879 | 3.7x sr_bytes | down | 5 |
| `FW-mixed` | legacy-fraction | **text** | 0.831 → 0.897 | 0.066 | 0.824 → 0.893 | 1.9x sr_bytes | down | 4 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.884 → 0.943 | 0.059 | 0.871 → 0.933 | 1.3x sr_bytes | up | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.884 → 0.933 | 0.049 | 0.871 → 0.922 | 1.3x sr_bytes | up | 3 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.849 → 0.893 | 0.044 | 0.844 → 0.887 | 2x bytes_on_air | up | 4 |
| `AD-badrouters` | role-placement | **text** | 0.813 → 0.857 | 0.044 | 0.793 → 0.842 | 1.4x sr_bytes | down | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.882 → 0.922 | 0.040 | 0.875 → 0.919 | 1.3x sr_bytes | up | 2 |
| `SF-cadence` | trigger | **held** | 0.937 → 0.977 | 0.040 | 0.847 → 0.884 | 14x advert_bytes | down | 4 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.848 → 0.884 | 0.035 | 0.831 → 0.871 | 1.5x sr_airtime | down | 4 |
| `RT-hopassign` | hop-assign | **held** | 0.943 → 0.977 | 0.034 | 0.836 → 0.871 | 1.3x sr_bytes | down | 2 |
| `TH-congestion-input` | congestion-input | **text** | 0.565 → 0.599 | 0.034 | 0.555 → 0.589 | 1.4x sr_airtime | up | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.884 → 0.914 | 0.031 | 0.871 → 0.906 | 3.3x bytes_on_air | down | 2 |
| `SF-catchup` | catch-up-hours | **held** | 0.940 → 0.968 | 0.028 | 0.847 → 0.884 | 9.4x advert_bytes | down | 3 |
| `SF-provide-transport` | provide-transport | **text** | 0.884 → 0.910 | 0.026 | 0.870 → 0.871 | 2.6x sr_airtime | up | 2 |
| `MS-roles` | role-mix | **text** | 0.857 → 0.882 | 0.026 | 0.842 → 0.868 | 1.1x bytes_on_air | down | 2 |
| `AD-worst` | role-placement | **text** | 0.742 → 0.767 | 0.025 | 0.732 → 0.762 | 1.3x sr_bytes | down | 2 |
| `FW-versions` | profile | **text** | 0.884 → 0.908 | 0.024 | 0.871 → 0.900 | 3.1x bytes_on_air | down | 5 |
| `FW-firmware` | profile | **text** | 0.884 → 0.905 | 0.021 | 0.871 → 0.897 | 3x bytes_on_air | down | 2 |
| `LD-diurnal` | diurnal | **text** | 0.884 → 0.902 | 0.018 | 0.871 → 0.891 | 1.2x sr_bytes | down | 3 |
| `DM-mode` | dm-mode | **text** | 0.836 → 0.854 | 0.018 | 0.836 → 0.854 | 1.1x sr_bytes | up | 3 |
| `MS-router-late` | router-late-fraction | **text** | 0.884 → 0.901 | 0.018 | 0.871 → 0.896 | 1.4x sr_bytes | up | 4 |
| `SF-capacity-window` | capacity | **held** | 0.965 → 0.983 | 0.018 | 0.874 → 0.879 | 2.3x advert_bytes | up | 3 |
| `SF-servers-flat` | servers | **text** | 0.874 → 0.890 | 0.017 | 0.862 → 0.874 | 5.1x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **text** | 0.874 → 0.890 | 0.017 | 0.862 → 0.874 | 5.1x sr_bytes | up | 4 |
| `MS-roles-fav` | role-mix | **held** | 0.950 → 0.965 | 0.015 | 0.874 → 0.885 | 1.1x sr_bytes | down | 2 |
| `SF-capacity` | capacity | **held** | 0.966 → 0.980 | 0.014 | 0.871 → 0.880 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.966 → 0.980 | 0.014 | 0.871 → 0.880 | 5.3x advert_bytes | up | 5 |
| `SF-servers-allrouters` | servers | **text** | 0.871 → 0.884 | 0.013 | 0.869 → 0.876 | 2.6x sr_bytes | up | 2 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.878 → 0.890 | 0.012 | 0.866 → 0.878 | 1.1x sr_airtime | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.878 → 0.890 | 0.012 | 0.866 → 0.878 | 1.1x sr_airtime | down | 4 |
| `SF-width` | short-id-bits | **text** | 0.883 → 0.893 | 0.010 | 0.871 → 0.880 | 3.1x advert_bytes | up | 4 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.974 → 0.983 | 0.009 | 0.869 → 0.877 | 2.6x advert_bytes | up | 4 |
| `PR-repeats` | extra-repeats | **held** | 0.977 → 0.985 | 0.008 | 0.871 → 0.880 | 1.1x sr_bytes | up | 2 |
| `SF-window-size` | window-size | **text** | 0.880 → 0.887 | 0.007 | 0.866 → 0.875 | 4.4x advert_bytes | up | 3 |
| `SF-sr-retries` | sr-retries | **text** | 0.886 → 0.892 | 0.007 | 0.874 → 0.881 | 1.2x sr_bytes | down | 4 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.850 → 0.856 | 0.006 | 0.850 → 0.856 | 1x sr_airtime | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.979 → 0.985 | 0.005 | 0.870 → 0.874 | 1x sr_bytes | up | 2 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.884 → 0.888 | 0.004 | 0.873 → 0.878 | 5.2x advert_bytes | up | 3 |
| `SF-replay-order` | replay-ordering | **held** | 0.977 → 0.981 | 0.004 | 0.871 → 0.872 | 1x sr_airtime | up | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.970 → 0.973 | 0.003 | 0.854 → 0.856 | 1.1x sr_bytes | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.966 → 0.970 | 0.003 | 0.965 → 0.969 | 1.1x bytes_on_air | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.970 → 0.972 | 0.002 | 0.969 → 0.971 | 1.1x sr_airtime | down | 2 |
| `SF-advert-transport` | advert-transport | **text** | 0.884 → 0.885 | 0.002 | 0.871 → 0.872 | 2.3x sr_airtime | up | 2 |
| `SF-resolve` | resolve | **held** | 0.976 → 0.977 | 0.001 | 0.871 → 0.871 | 5.8x advert_bytes | = | 3 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.970 → 0.971 | 0.001 | 0.969 → 0.969 | 1.1x sr_bytes | up | 2 |

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
| none | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| sprinkled | 1 | 0.926 | 0.923 | 0.004 | - | - | 0.986 | 0.988 | 0.733 | 1.24x | 17.4/24.5/30.9% | 1.8/5.1% | 3 |
| arms-race | 1 | 0.964 | 0.963 | 0.001 | - | - | 0.996 | 0.996 | 0.821 | 1.06x | 19.1/25.7/29.7% | 1.4/5.2% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario rolling`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 0.1 | 1 | 0.904 | 0.891 | 0.013 | - | - | 0.940 | 0.945 | 0.757 | 1.14x | 16.4/22.8/27.8% | 1.5/5.3% | 3 |
| 0.3 | 1 | 0.943 | 0.933 | 0.009 | - | - | 0.984 | 0.985 | 0.813 | 1.03x | 18.6/24.1/27.9% | 1.4/4.9% | 3 |

### `AD-badrouters` - role-placement  `--scenario rolling`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.857 | 0.842 | 0.014 | - | - | 0.961 | 0.962 | 0.437 | 1.14x | 14.5/23.3/27.5% | 1.9/5.3% | 3 |
| inverse | 1 | 0.813 | 0.793 | 0.019 | - | - | 0.943 | 0.947 | 0.435 | 1.11x | 14.1/19.2/27.7% | 2.0/4.1% | 3 |
| random | 1 | 0.826 | 0.814 | 0.012 | - | - | 0.944 | 0.946 | 0.514 | 1.12x | 14.9/20.4/22.2% | 1.9/5.0% | 3 |

### `AD-flooding` - role-mix  `--scenario rolling`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.857 | 0.842 | 0.014 | - | - | 0.961 | 0.962 | 0.437 | 1.14x | 14.5/23.3/27.5% | 1.9/5.3% | 3 |
| all-routers | 1 | 0.936 | 0.932 | 0.004 | - | - | 0.996 | 0.996 | 0.801 | 2.81x | 32.4/41.7/44.5% | 4.6/5.3% | 3 |

### `AD-nomute` - role-mix  `--scenario rolling`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.857 | 0.842 | 0.014 | - | - | 0.961 | 0.962 | 0.437 | 1.14x | 14.5/23.3/27.5% | 1.9/5.3% | 3 |
| no-mute | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.968 | 0.971 | 0.669 | 1.24x | 15.6/21.6/28.4% | 1.9/5.4% | 3 |
| all-routers | 1 | 0.936 | 0.932 | 0.004 | - | - | 0.996 | 0.996 | 0.801 | 2.81x | 32.4/41.7/44.5% | 4.6/5.3% | 3 |

### `AD-siting` - siting-mix  `--scenario rolling`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.857 | 0.842 | 0.014 | - | - | 0.961 | 0.962 | 0.437 | 1.14x | 14.5/23.3/27.5% | 1.9/5.3% | 3 |
| local-typical | 1 | 0.564 | 0.541 | 0.023 | - | - | 0.734 | 0.793 | 0.000 | 1.18x | 11.5/19.8/26.0% | 1.9/5.1% | 3 |
| basement-heavy | 1 | 0.084 | 0.082 | 0.002 | - | - | 0.271 | 0.276 | 0.000 | 0.54x | 1.9/5.7/10.3% | 0.5/3.0% | 3 |

> siting-mix=local-typical: decode_failures 17

> siting-mix=basement-heavy: decode_failures 1

> slower: 3.12 s per simulated hour against 1.35 over 17 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-worst` - role-placement  `--scenario rolling`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.767 | 0.762 | 0.005 | - | - | 0.918 | 0.918 | 0.000 | 2.39x | 15.8/29.2/35.9% | 1.8/5.3% | 3 |
| inverse | 1 | 0.742 | 0.732 | 0.009 | - | - | 0.925 | 0.925 | 0.000 | 2.28x | 13.5/24.3/30.2% | 1.7/3.4% | 3 |

### `BL-control` - protocol  `--scenario rolling`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.872 | 0.872 | 0.000 | - | - | 0 | 0.000 | 0.673 | 1.21x | 16.1/22.2/27.3% | 1.7/5.1% | 3 |
| sr | 1 | 0.887 | 0.868 | 0.019 | - | - | 0.958 | 0.995 | 0.712 | 1.26x | 16.6/22.9/28.4% | 1.8/5.4% | 3 |

> protocol=sr: decode_failures 23

> slower: 4.55 s per simulated hour against 1.74 over 17 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario rolling`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.833 | 0.824 | 0.010 | - | - | 0.929 | 0.929 | 0.686 | 3.05x | 39.0/56.0/62.8% | 4.3/10.3% | 3 |
| 100 | 1 | 0.928 | 0.925 | 0.003 | - | - | 0.983 | 0.983 | 0.793 | 1.53x | 20.0/30.0/34.1% | 2.1/5.3% | 3 |
| 120 | 1 | 0.928 | 0.925 | 0.003 | - | - | 0.983 | 0.983 | 0.793 | 1.53x | 20.0/30.0/34.1% | 2.1/5.3% | 3 |
| 250 | 1 | 0.928 | 0.925 | 0.003 | - | - | 0.983 | 0.983 | 0.793 | 1.53x | 20.0/30.0/34.1% | 2.1/5.3% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario rolling`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.335 | 0.331 | 0.004 | - | - | 0.451 | 0.530 | 0.116 | 11.39x | 43.5/60.3/72.9% | 4.0/10.7% | 3 |
| 120 | 1 | 0.565 | 0.555 | 0.011 | - | - | 0.812 | 0.815 | 0.153 | 4.46x | 17.4/27.5/37.7% | 1.5/5.5% | 3 |
| 250 | 1 | 0.576 | 0.565 | 0.011 | - | - | 0.823 | 0.825 | 0.146 | 4.30x | 16.8/26.3/36.4% | 1.4/5.5% | 3 |

> max-num-nodes=10: decode_failures 51

### `DB-platform` - platform-mix  `--scenario rolling`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.928 | 0.925 | 0.003 | - | - | 0.983 | 0.983 | 0.793 | 1.53x | 20.0/30.0/34.1% | 2.1/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.928 | 0.925 | 0.003 | - | - | 0.983 | 0.983 | 0.793 | 1.53x | 20.0/30.0/34.1% | 2.1/5.3% | 3 |
| constrained | 1 | 0.849 | 0.839 | 0.010 | - | - | 0.951 | 0.951 | 0.668 | 3.05x | 38.9/56.1/62.5% | 4.4/10.3% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario rolling`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.706 | 0.699 | 0.006 | - | - | 0.794 | 0.869 | 0.504 | 5.83x | 59.7/75.0/79.7% | 4.2/13.5% | 3 |
| 25 | 1 | 0.706 | 0.699 | 0.006 | - | - | 0.794 | 0.869 | 0.504 | 5.83x | 59.7/75.0/79.7% | 4.2/13.5% | 3 |
| 100 | 1 | 0.706 | 0.699 | 0.006 | - | - | 0.794 | 0.869 | 0.504 | 5.83x | 59.7/75.0/79.7% | 4.2/13.5% | 3 |
| 2000 | 1 | 0.706 | 0.699 | 0.006 | - | - | 0.794 | 0.869 | 0.504 | 5.83x | 59.7/75.0/79.7% | 4.2/13.5% | 3 |

> warm-num-nodes=0: queue drops 19.6% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 119

> warm-num-nodes=25: queue drops 19.6% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 119

> warm-num-nodes=100: queue drops 19.6% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 119

> warm-num-nodes=2000: queue drops 19.6% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 119

### `DG-burst` - burst-loss  `--scenario rolling`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 0.1 | 1 | 0.790 | 0.765 | 0.026 | - | - | 0.957 | 0.963 | 0.541 | 1.18x | 15.6/22.1/27.1% | 1.7/5.1% | 3 |
| 0.2 | 1 | 0.681 | 0.646 | 0.035 | - | - | 0.902 | 0.916 | 0.418 | 1.12x | 14.9/21.0/26.3% | 1.7/4.6% | 3 |
| 0.3 | 1 | 0.567 | 0.533 | 0.034 | - | - | 0.759 | 0.862 | 0.324 | 1.01x | 13.6/19.1/24.3% | 1.5/4.0% | 3 |

> burst-loss=0.1: decode_failures 1

> burst-loss=0.2: decode_failures 5

> burst-loss=0.3: decode_failures 31

### `DG-loss` - extra-loss  `--scenario rolling`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 0.1 | 1 | 0.855 | 0.839 | 0.015 | - | - | 0.973 | 0.976 | 0.578 | 1.33x | 17.6/24.0/29.4% | 1.9/5.4% | 3 |
| 0.2 | 1 | 0.827 | 0.810 | 0.017 | - | - | 0.966 | 0.971 | 0.515 | 1.38x | 18.3/25.1/30.6% | 2.1/5.2% | 3 |
| 0.3 | 1 | 0.765 | 0.745 | 0.020 | - | - | 0.929 | 0.939 | 0.419 | 1.41x | 18.5/25.7/31.1% | 2.2/5.0% | 3 |

> extra-loss=0.2: decode_failures 1

> extra-loss=0.3: decode_failures 4

### `DG-outage` - burst-loss  `--scenario rolling`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 0.1 | 1 | 0.778 | 0.759 | 0.018 | - | - | 0.916 | 0.961 | 0.536 | 1.19x | 15.9/22.0/27.3% | 1.7/5.1% | 3 |
| 0.2 | 1 | 0.659 | 0.635 | 0.024 | - | - | 0.838 | 0.923 | 0.402 | 1.10x | 14.6/20.6/26.0% | 1.7/4.5% | 3 |
| 0.3 | 1 | 0.537 | 0.514 | 0.023 | - | - | 0.688 | 0.874 | 0.343 | 1.05x | 13.9/20.1/25.0% | 1.6/4.2% | 3 |

> burst-loss=0.1: decode_failures 28

> burst-loss=0.2: decode_failures 33

> burst-loss=0.3: decode_failures 24

### `DM-mode` - dm-mode  `--scenario rolling`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.836 | 0.836 | 0.000 | - | - | 0.958 | 0.969 | 0.606 | 1.65x | 21.8/30.2/36.3% | 2.3/7.0% | 3 |
| directed-with-late-flood | 1 | 0.854 | 0.854 | 0.000 | - | - | 0.973 | 0.979 | 0.625 | 1.52x | 20.1/28.3/33.9% | 2.1/6.6% | 3 |
| m4-early-flood | 1 | 0.850 | 0.850 | 0.000 | - | - | 0.963 | 0.971 | 0.648 | 1.51x | 20.1/28.2/33.8% | 2.2/6.6% | 3 |

> dm-mode=flood-only: decode_failures 8

> dm-mode=m4-early-flood: decode_failures 1

### `FW-firmware` - profile  `--scenario rolling`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.905 | 0.897 | 0.007 | - | - | 0.986 | 0.986 | 0.660 | 0.73x | 8.5/11.5/12.4% | 1.2/1.9% | 3 |
| 2.8 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario rolling`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 0.25 | 1 | 0.831 | 0.824 | 0.007 | - | - | 0.922 | 0.923 | 0.512 | 1.16x | 14.2/22.0/24.1% | 1.7/4.5% | 3 |
| 0.5 | 1 | 0.897 | 0.893 | 0.004 | - | - | 0.981 | 0.982 | 0.601 | 1.05x | 13.5/19.2/23.3% | 1.6/4.1% | 3 |
| 0.75 | 1 | 0.881 | 0.878 | 0.003 | - | - | 0.964 | 0.964 | 0.550 | 0.91x | 10.8/15.7/18.5% | 1.4/3.6% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario rolling`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 0.25 | 1 | 0.849 | 0.844 | 0.005 | - | - | 0.948 | 0.949 | 0.487 | 1.15x | 14.2/21.8/23.8% | 1.7/4.5% | 3 |
| 0.5 | 1 | 0.893 | 0.887 | 0.006 | - | - | 0.977 | 0.978 | 0.641 | 1.06x | 13.8/19.5/23.9% | 1.6/4.2% | 3 |
| 0.75 | 1 | 0.891 | 0.886 | 0.005 | - | - | 0.976 | 0.977 | 0.606 | 0.86x | 10.4/15.2/17.9% | 1.3/3.5% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario rolling`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.914 | 0.906 | 0.008 | - | - | 0.988 | 0.989 | 0.721 | 0.67x | 9.2/12.9/16.2% | 0.9/3.1% | 3 |
| signing=true | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |

### `FW-versions` - profile  `--scenario rolling`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.897 | 0.888 | 0.009 | - | - | 0.992 | 0.993 | 0.685 | 0.72x | 8.7/12.5/13.7% | 1.2/2.4% | 3 |
| 2.5 | 1 | 0.893 | 0.885 | 0.008 | - | - | 0.987 | 0.989 | 0.675 | 0.73x | 8.9/12.5/13.8% | 1.2/2.3% | 3 |
| 2.6 | 1 | 0.890 | 0.881 | 0.009 | - | - | 0.983 | 0.985 | 0.646 | 0.71x | 8.8/12.7/13.8% | 1.2/2.4% | 3 |
| 2.7 | 1 | 0.908 | 0.900 | 0.009 | - | - | 0.984 | 0.990 | 0.689 | 0.74x | 9.3/14.2/16.5% | 1.2/3.2% | 3 |
| 2.8 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |

> profile=2.7: decode_failures 1

### `LD-chatty` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.908 | 0.899 | 0.009 | - | - | 0.983 | 0.985 | 0.729 | 0.85x | 11.0/15.4/18.9% | 1.2/3.7% | 3 |
| 900 | 1 | 0.835 | 0.818 | 0.018 | - | - | 0.958 | 0.960 | 0.603 | 1.95x | 25.7/35.6/43.1% | 2.7/8.4% | 3 |
| 300 | 1 | 0.605 | 0.574 | 0.032 | - | - | 0.809 | 0.848 | 0.342 | 4.22x | 51.6/67.7/75.0% | 6.3/16.7% | 3 |

> broadcast-interval-s=300: decode_failures 26

### `LD-chatty-hops` - broadcast-interval-s  `--scenario rolling`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.942 | 0.939 | 0.003 | - | - | 0.990 | 0.990 | 0.812 | 0.92x | 11.8/15.5/19.5% | 1.3/3.6% | 3 |
| 900 | 1 | 0.884 | 0.876 | 0.008 | - | - | 0.962 | 0.964 | 0.737 | 2.23x | 28.7/37.7/46.8% | 3.2/8.7% | 3 |
| 300 | 1 | 0.644 | 0.624 | 0.020 | - | - | 0.825 | 0.831 | 0.466 | 4.69x | 55.7/69.9/77.0% | 6.9/16.9% | 3 |

> broadcast-interval-s=300: decode_failures 9

### `LD-diurnal` - diurnal  `--scenario rolling`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.902 | 0.891 | 0.011 | - | - | 0.986 | 0.987 | 0.702 | 1.15x | 15.1/21.1/25.8% | 1.6/5.1% | 3 |
| sinusoid | 1 | 0.895 | 0.883 | 0.011 | - | - | 0.980 | 0.980 | 0.694 | 1.14x | 15.0/20.8/25.5% | 1.6/4.9% | 3 |
| commuter | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.835 | 0.818 | 0.018 | - | - | 0.958 | 0.960 | 0.603 | 1.95x | 25.7/35.6/43.1% | 2.7/8.4% | 3 |
| 3600 | 1 | 0.908 | 0.899 | 0.009 | - | - | 0.983 | 0.985 | 0.729 | 0.85x | 11.0/15.4/18.9% | 1.2/3.7% | 3 |
| 10800 | 1 | 0.921 | 0.916 | 0.006 | - | - | 0.990 | 0.992 | 0.742 | 0.56x | 7.2/9.9/12.2% | 0.8/2.4% | 3 |
| 43200 | 1 | 0.921 | 0.914 | 0.008 | - | - | 0.991 | 0.992 | 0.741 | 0.40x | 5.2/7.1/8.7% | 0.6/1.8% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario rolling`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 0.25 | 1 | 0.882 | 0.869 | 0.013 | - | - | 0.975 | 0.977 | 0.676 | 1.27x | 16.9/23.5/28.8% | 1.8/5.6% | 3 |
| 1.0 | 1 | 0.876 | 0.861 | 0.014 | - | - | 0.982 | 0.982 | 0.656 | 1.45x | 19.2/26.7/32.5% | 2.1/6.4% | 3 |
| 4.0 | 1 | 0.848 | 0.831 | 0.018 | - | - | 0.966 | 0.969 | 0.608 | 1.76x | 23.6/33.8/40.7% | 2.6/8.0% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario rolling`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.706 | 0.699 | 0.006 | - | - | 0.794 | 0.869 | 0.504 | 5.83x | 59.7/75.0/79.7% | 4.2/13.5% | 3 |
| 1.0 | 1 | 0.629 | 0.624 | 0.005 | - | - | 0.717 | 0.821 | 0.443 | 6.31x | 63.7/76.6/80.5% | 4.6/14.7% | 3 |

> traceroute-per-hour=0.0: queue drops 19.6% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 119

> traceroute-per-hour=1.0: queue drops 28.9% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 97

### `MS-density` - nodes  `--scenario rolling`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.554 | 0.534 | 0.020 | - | - | 0.714 | 0.746 | 0.175 | 1.07x | 14.8/22.1/27.0% | 2.5/5.9% | 3 |
| 60 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 90 | 1 | 0.948 | 0.946 | 0.003 | - | - | 0.996 | 0.996 | 0.637 | 1.58x | 17.9/27.6/32.3% | 1.4/4.8% | 3 |
| 120 | 1 | 0.970 | 0.969 | 0.001 | - | - | 0.999 | 1.000 | 0.812 | 2.13x | 24.9/37.5/42.8% | 1.4/5.3% | 3 |
| 150 | 1 | 0.968 | 0.966 | 0.003 | - | - | 0.999 | 0.999 | 0.851 | 2.51x | 30.6/39.0/44.3% | 1.1/5.8% | 3 |

> nodes=40: decode_failures 18

> nodes=150: misdecodes 1

### `MS-hopscale` - nodes  `--scenario rolling`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 120 | 1 | 0.813 | 0.805 | 0.008 | - | - | 0.932 | 0.933 | 0.408 | 2.25x | 16.3/23.8/30.0% | 1.5/4.9% | 3 |
| 250 | 1 | 0.564 | 0.553 | 0.011 | - | - | 0.811 | 0.817 | 0.162 | 4.86x | 18.9/30.0/41.5% | 1.6/6.3% | 3 |
| 500 | 1 | 0.317 | 0.310 | 0.007 | - | - | 0.532 | 0.547 | 0.088 | 10.07x | 18.0/34.1/50.2% | 1.7/7.2% | 3 |

> nodes=250: decode_failures 10

> nodes=500: decode_failures 204

### `MS-oversubscribed` - nodes  `--scenario rolling`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.812 | 0.803 | 0.009 | - | - | 0.934 | 0.934 | 0.404 | 2.06x | 14.9/21.8/27.3% | 1.4/4.5% | 3 |
| 250 | 1 | 0.565 | 0.555 | 0.011 | - | - | 0.812 | 0.815 | 0.153 | 4.46x | 17.4/27.5/37.7% | 1.5/5.5% | 3 |
| 500 | 1 | 0.321 | 0.314 | 0.007 | - | - | 0.545 | 0.557 | 0.088 | 9.34x | 16.9/31.8/46.5% | 1.5/6.5% | 3 |

> nodes=500: decode_failures 121

### `MS-roles` - role-mix  `--scenario rolling`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.882 | 0.868 | 0.014 | - | - | 0.978 | 0.980 | 0.659 | 1.24x | 16.3/22.8/28.0% | 1.7/5.5% | 3 |
| baymesh-2026-08 | 1 | 0.857 | 0.842 | 0.014 | - | - | 0.961 | 0.962 | 0.437 | 1.14x | 14.5/23.3/27.5% | 1.9/5.3% | 3 |

### `MS-roles-fav` - role-mix  `--scenario rolling`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.893 | 0.885 | 0.008 | - | - | 0.965 | 0.966 | 0.678 | 1.28x | 16.9/23.4/28.9% | 1.8/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.882 | 0.874 | 0.008 | - | - | 0.950 | 0.952 | 0.514 | 1.31x | 16.9/26.0/30.8% | 2.1/5.2% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario rolling`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 0.05 | 1 | 0.889 | 0.882 | 0.008 | - | - | 0.979 | 0.980 | 0.653 | 1.36x | 17.2/27.4/32.0% | 1.8/5.4% | 3 |
| 0.1 | 1 | 0.898 | 0.892 | 0.006 | - | - | 0.981 | 0.982 | 0.660 | 1.49x | 19.7/32.4/36.7% | 2.1/5.2% | 3 |
| 0.2 | 1 | 0.901 | 0.896 | 0.005 | - | - | 0.974 | 0.974 | 0.629 | 1.66x | 21.9/35.0/38.9% | 2.2/5.2% | 3 |

### `MS-siting` - siting-mix  `--scenario rolling`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| local-typical | 1 | 0.698 | 0.678 | 0.020 | - | - | 0.828 | 0.911 | 0.000 | 1.32x | 12.7/19.7/25.1% | 2.1/5.0% | 3 |
| event | 1 | 0.154 | 0.152 | 0.002 | - | - | 0.292 | 0.293 | 0.000 | 1.08x | 6.0/11.1/16.3% | 1.7/3.7% | 3 |
| backbone | 1 | 0.979 | 0.978 | 0.001 | - | - | 0.999 | 1.000 | 0.929 | 1.11x | 26.2/35.1/38.2% | 1.4/5.5% | 3 |

> siting-mix=local-typical: decode_failures 11

> siting-mix=event: decode_failures 2

### `MS-size` - nodes  `--scenario rolling`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.828 | 0.814 | 0.014 | - | - | 0.907 | 0.939 | 0.490 | 1.38x | 24.8/36.2/39.6% | 3.1/7.6% | 3 |
| 60 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 90 | 1 | 0.869 | 0.863 | 0.006 | - | - | 0.977 | 0.977 | 0.572 | 1.70x | 16.2/25.3/29.5% | 1.6/4.9% | 3 |
| 120 | 1 | 0.813 | 0.805 | 0.008 | - | - | 0.932 | 0.933 | 0.408 | 2.25x | 16.3/23.8/30.0% | 1.5/4.9% | 3 |
| 150 | 1 | 0.746 | 0.733 | 0.014 | - | - | 0.811 | 0.815 | 0.310 | 2.66x | 16.5/23.2/27.0% | 1.6/5.0% | 3 |

> nodes=40: decode_failures 28

> nodes=150: decode_failures 2

### `MS-stretch` - stretch  `--scenario rolling`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 1.25 | 1 | 0.647 | 0.640 | 0.007 | - | - | 0.823 | 0.825 | 0.375 | 1.24x | 11.5/18.4/20.6% | 1.9/4.9% | 3 |
| 1.5 | 1 | 0.351 | 0.343 | 0.008 | - | - | 0.542 | 0.635 | 0.115 | 1.23x | 8.4/18.0/20.9% | 1.9/5.0% | 3 |
| 2.0 | 1 | 0.114 | 0.112 | 0.002 | - | - | 0.254 | 0.316 | 0.000 | 0.75x | 3.2/10.4/12.6% | 0.9/2.8% | 3 |

> stretch=1.5: decode_failures 28

> stretch=2.0: decode_failures 3

### `MS-topology` - topology  `--scenario rolling`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| clustered | 1 | 0.917 | 0.908 | 0.008 | - | - | 0.957 | 0.974 | 0.195 | 1.19x | 19.8/31.3/33.4% | 1.5/5.4% | 3 |
| corridor | 1 | 0.554 | 0.552 | 0.003 | - | - | 0.568 | 0.569 | 0.397 | 1.45x | 16.5/27.7/28.9% | 2.3/5.1% | 3 |
| hub | 1 | 0.968 | 0.967 | 0.001 | - | - | 0.994 | 0.995 | 0.897 | 1.16x | 25.1/34.1/37.9% | 1.7/5.4% | 3 |

> topology=clustered: decode_failures 2

### `PR-crladder` - coding-rate-ladder  `--scenario rolling`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.854 | 0.854 | 0.000 | - | - | 0.973 | 0.979 | 0.625 | 1.52x | 20.1/28.3/33.9% | 2.1/6.6% | 3 |
| True | 1 | 0.856 | 0.856 | 0.000 | - | - | 0.970 | 0.976 | 0.651 | 1.52x | 20.3/28.2/33.8% | 2.1/6.6% | 3 |

> coding-rate-ladder=True: decode_failures 1

### `PR-dmmode-cr` - dm-mode  `--scenario rolling`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.856 | 0.856 | 0.000 | - | - | 0.970 | 0.976 | 0.651 | 1.52x | 20.3/28.2/33.8% | 2.1/6.6% | 3 |
| m4-early-flood | 1 | 0.850 | 0.850 | 0.000 | - | - | 0.965 | 0.973 | 0.666 | 1.51x | 20.2/28.1/33.7% | 2.2/6.6% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 1

### `PR-protocol` - protocol  `--scenario rolling`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.872 | 0.872 | 0.000 | - | - | 0 | 0.000 | 0.673 | 1.21x | 16.1/22.2/27.3% | 1.7/5.1% | 3 |
| chain | 1 | 0.873 | 0.869 | 0.004 | - | - | 0.909 | 0.975 | 0.643 | 1.43x | 18.8/26.1/31.6% | 2.0/6.1% | 3 |
| sr | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |

### `PR-repeats` - extra-repeats  `--scenario rolling`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| True | 1 | 0.891 | 0.880 | 0.012 | - | - | 0.985 | 0.986 | 0.685 | 1.26x | 16.6/23.0/28.0% | 1.7/5.4% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario rolling`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.970 | 0.969 | 0.001 | - | - | 0.999 | 1.000 | 0.812 | 2.13x | 24.9/37.5/42.8% | 1.4/5.3% | 3 |
| True | 1 | 0.971 | 0.969 | 0.002 | - | - | 1.000 | 1.000 | 0.822 | 2.12x | 24.8/37.1/42.4% | 1.4/5.2% | 3 |

> extra-repeats=True: misdecodes 1

### `RF-bw500` - preset  `--scenario rolling`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.161 | 0.159 | 0.002 | - | - | 0.195 | 0.198 | 0.000 | 0.04x | 0.2/0.5/0.7% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.415 | 0.409 | 0.006 | - | - | 0.652 | 0.672 | 0.094 | 0.25x | 1.8/3.6/4.8% | 0.3/1.1% | 3 |
| LONG_TURBO | 1 | 0.797 | 0.783 | 0.014 | - | - | 0.910 | 0.913 | 0.578 | 1.23x | 12.5/19.0/22.1% | 1.8/4.6% | 3 |

> preset=MEDIUM_TURBO: decode_failures 27

### `RF-duct` - duct-per-hour  `--scenario rolling`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 0.25 | 1 | 0.890 | 0.879 | 0.012 | - | - | 0.978 | 0.979 | 0.691 | 1.20x | 17.3/23.6/28.2% | 1.6/5.5% | 3 |
| 1.0 | 1 | 0.933 | 0.922 | 0.010 | - | - | 0.990 | 0.991 | 0.788 | 0.96x | 21.0/26.1/28.3% | 1.2/5.3% | 3 |

### `RF-eu-presets` - preset  `--scenario rolling`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.254 | 0.245 | 0.009 | - | - | 0.487 | 0.520 | 0.039 | 0.12x | 0.6/2.0/2.4% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| LITE_FAST | 1 | 0.838 | 0.828 | 0.010 | - | - | 0.967 | 0.970 | 0.527 | 0.94x | 10.9/16.6/19.1% | 1.3/4.2% | 3 |
| NARROW_SLOW | 1 | 0.857 | 0.850 | 0.007 | - | - | 0.977 | 0.977 | 0.608 | 1.20x | 14.4/21.7/25.1% | 1.6/5.3% | 3 |

> preset=SHORT_FAST: decode_failures 8

### `RF-noise` - noise-profile  `--scenario rolling`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| temporal | 1 | 0.814 | 0.794 | 0.020 | - | - | 0.960 | 0.964 | 0.546 | 1.24x | 15.6/22.1/27.6% | 1.8/5.3% | 3 |
| transient | 1 | 0.880 | 0.866 | 0.014 | - | - | 0.982 | 0.984 | 0.663 | 1.23x | 16.2/22.6/27.5% | 1.7/5.4% | 3 |
| periodic | 1 | 0.723 | 0.708 | 0.015 | - | - | 0.821 | 0.830 | 0.487 | 1.19x | 15.7/21.7/26.9% | 1.8/4.9% | 3 |

### `RF-preset` - preset  `--scenario rolling`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.254 | 0.245 | 0.009 | - | - | 0.487 | 0.520 | 0.039 | 0.12x | 0.6/2.0/2.4% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| LONG_MODERATE | 1 | 0.835 | 0.813 | 0.022 | - | - | 0.947 | 0.979 | 0.625 | 3.10x | 45.6/58.2/65.7% | 4.5/12.7% | 3 |

> preset=SHORT_FAST: decode_failures 8

> preset=LONG_MODERATE: decode_failures 16

### `RF-preset-turbo` - preset  `--scenario rolling`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.057 | 0.057 | 0.000 | - | - | 0.039 | 0.039 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.161 | 0.159 | 0.002 | - | - | 0.195 | 0.198 | 0.000 | 0.04x | 0.2/0.5/0.7% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| LONG_TURBO | 1 | 0.797 | 0.783 | 0.014 | - | - | 0.910 | 0.913 | 0.578 | 1.23x | 12.5/19.0/22.1% | 1.8/4.6% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.869 | 0.859 | 0.010 | - | - | 0.970 | 0.973 | 0.665 | 1.71x | 20.8/29.8/35.7% | 2.4/7.0% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario rolling`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.831 | 0.815 | 0.016 | - | - | 0.932 | 0.933 | 0.617 | 1.24x | 16.5/23.0/28.1% | 1.8/5.3% | 3 |
| 10000 | 1 | 0.723 | 0.708 | 0.015 | - | - | 0.821 | 0.830 | 0.487 | 1.19x | 15.7/21.7/26.9% | 1.8/4.9% | 3 |
| 4000 | 1 | 0.440 | 0.437 | 0.003 | - | - | 0.486 | 0.597 | 0.232 | 1.00x | 13.1/18.9/23.4% | 1.5/3.5% | 3 |
| 2000 | 1 | 0.090 | 0.090 | 0.000 | - | - | 0.103 | 0.193 | 0.041 | 0.71x | 9.5/13.4/16.9% | 1.1/2.0% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 6

### `RF-stretch-duct` - duct-per-hour  `--scenario rolling`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.351 | 0.343 | 0.008 | - | - | 0.542 | 0.635 | 0.115 | 1.23x | 8.4/18.0/20.9% | 1.9/5.0% | 3 |
| 1.0 | 1 | 0.638 | 0.616 | 0.022 | - | - | 0.796 | 0.804 | 0.469 | 0.95x | 12.3/20.1/22.9% | 1.3/4.5% | 3 |

> duct-per-hour=0.0: decode_failures 28

### `RF-txpower` - tx-power  `--scenario rolling`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 22 | 1 | 0.377 | 0.371 | 0.006 | - | - | 0.557 | 0.597 | 0.127 | 1.23x | 8.9/17.1/19.9% | 1.8/4.7% | 3 |
| 17 | 1 | 0.148 | 0.144 | 0.004 | - | - | 0.194 | 0.200 | 0.000 | 0.91x | 4.4/10.3/13.9% | 1.2/3.1% | 3 |
| 14 | 1 | 0.104 | 0.100 | 0.004 | - | - | 0.269 | 0.292 | 0.000 | 0.70x | 3.0/7.1/11.7% | 1.0/2.8% | 3 |

> tx-power=22: decode_failures 23

> tx-power=14: decode_failures 1

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario rolling`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.970 | 0.969 | 0.001 | - | - | 0.999 | 1.000 | 0.812 | 2.13x | 24.9/37.5/42.8% | 1.4/5.3% | 3 |
| True | 1 | 0.966 | 0.965 | 0.002 | - | - | 0.999 | 0.999 | 0.804 | 2.46x | 28.2/41.4/46.6% | 1.7/5.8% | 3 |

### `RT-favourites` - favourite-routers  `--scenario rolling`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.882 | 0.875 | 0.006 | - | - | 0.970 | 0.972 | 0.627 | 1.30x | 16.6/25.7/30.4% | 1.7/5.4% | 3 |
| True | 1 | 0.922 | 0.919 | 0.003 | - | - | 0.979 | 0.979 | 0.767 | 1.40x | 17.8/26.3/31.6% | 2.0/5.3% | 3 |

### `RT-hopassign` - hop-assign  `--scenario rolling`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| random | 1 | 0.856 | 0.836 | 0.020 | - | - | 0.943 | 0.946 | 0.600 | 1.22x | 16.1/22.0/27.6% | 1.7/5.2% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario rolling`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.727 | 0.685 | 0.042 | - | - | 0.943 | 0.953 | 0.352 | 0.93x | 12.4/18.8/23.3% | 1.3/4.6% | 3 |
| 7 | 1 | 0.932 | 0.927 | 0.005 | - | - | 0.986 | 0.988 | 0.798 | 1.37x | 17.8/23.7/29.7% | 1.9/5.5% | 3 |
| 15 | 1 | 0.949 | 0.946 | 0.003 | - | - | 0.986 | 0.987 | 0.846 | 1.38x | 17.8/23.7/29.7% | 2.0/5.4% | 3 |
| 32 | 1 | 0.948 | 0.945 | 0.002 | - | - | 0.984 | 0.985 | 0.842 | 1.36x | 17.7/23.3/29.3% | 1.9/5.3% | 3 |

> hop-limit=3: decode_failures 1

### `RT-hopspread` - hop-limit  `--scenario rolling`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.727 | 0.685 | 0.042 | - | - | 0.943 | 0.953 | 0.352 | 0.93x | 12.4/18.8/23.3% | 1.3/4.6% | 3 |
| 5 | 1 | 0.877 | 0.863 | 0.014 | - | - | 0.979 | 0.981 | 0.658 | 1.26x | 16.5/22.5/28.1% | 1.8/5.3% | 3 |
| 7 | 1 | 0.932 | 0.927 | 0.005 | - | - | 0.986 | 0.988 | 0.798 | 1.37x | 17.8/23.7/29.7% | 1.9/5.5% | 3 |

> hop-limit=3: decode_failures 1

### `RT-rebroadcast` - rebroadcast-mode  `--scenario rolling`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| KNOWN_ONLY | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.881 | 0.881 | 0.000 | - | - | 0.904 | 0.982 | 0.696 | 1.20x | 15.9/22.2/27.1% | 1.7/5.2% | 3 |

### `RT-spread` - hop-spread  `--scenario rolling`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.727 | 0.685 | 0.042 | - | - | 0.943 | 0.953 | 0.352 | 0.93x | 12.4/18.8/23.3% | 1.3/4.6% | 3 |
| True | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |

> hop-spread=False: decode_failures 1

### `SC-signing` - signature-policy  `--scenario rolling`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| BALANCED | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| STRICT | 1 | 0.752 | 0.752 | 0.000 | - | - | 0.853 | 0.855 | 0.568 | 1.35x | 17.6/24.4/29.9% | 1.9/5.7% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario rolling`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| dm | 1 | 0.885 | 0.872 | 0.013 | - | - | 0.977 | 0.978 | 0.676 | 1.22x | 16.0/22.5/27.5% | 1.7/5.5% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario rolling`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.882 | 0.869 | 0.013 | - | - | 0.974 | 0.976 | 0.661 | 1.24x | 16.5/22.9/27.9% | 1.7/5.4% | 3 |
| local | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| time | 1 | 0.887 | 0.877 | 0.011 | - | - | 0.978 | 0.983 | 0.668 | 1.27x | 16.8/23.4/28.3% | 1.8/5.6% | 3 |
| window | 1 | 0.887 | 0.875 | 0.013 | - | - | 0.983 | 0.986 | 0.690 | 1.25x | 16.6/23.0/28.1% | 1.7/5.4% | 3 |

> bucket-mode=global: misdecodes 35

> bucket-mode=time: misdecodes 23

> bucket-mode=window: misdecodes 25

### `SF-bucket-time` - time-bucket-s  `--scenario rolling`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.884 | 0.873 | 0.011 | - | - | 0.976 | 0.980 | 0.672 | 1.38x | 17.9/25.0/30.0% | 1.9/6.1% | 3 |
| 1800 | 1 | 0.887 | 0.877 | 0.011 | - | - | 0.978 | 0.983 | 0.668 | 1.27x | 16.8/23.4/28.3% | 1.8/5.6% | 3 |
| 3600 | 1 | 0.888 | 0.878 | 0.011 | - | - | 0.978 | 0.983 | 0.671 | 1.26x | 16.6/23.2/28.4% | 1.8/5.5% | 3 |

> time-bucket-s=600: misdecodes 131

> time-bucket-s=1800: misdecodes 23

> time-bucket-s=3600: misdecodes 7

### `SF-cadence` - trigger  `--scenario rolling`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| interval | 1 | 0.864 | 0.849 | 0.015 | - | - | 0.966 | 0.970 | 0.636 | 1.70x | 21.8/30.6/35.9% | 2.4/9.1% | 3 |
| aimd | 1 | 0.886 | 0.884 | 0.003 | - | - | 0.937 | 0.989 | 0.672 | 1.26x | 16.7/23.0/28.2% | 1.7/5.4% | 3 |
| bucket+interval | 1 | 0.863 | 0.847 | 0.016 | - | - | 0.968 | 0.970 | 0.658 | 1.69x | 21.9/30.4/35.9% | 2.4/8.6% | 3 |

> trigger=interval: misdecodes 15

> trigger=aimd: misdecodes 2

> trigger=aimd: decode_failures 3

> trigger=bucket+interval: misdecodes 14

### `SF-capacity` - capacity  `--scenario rolling`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.891 | 0.878 | 0.013 | - | - | 0.978 | 0.988 | 0.669 | 1.25x | 16.4/23.0/28.0% | 1.7/5.5% | 3 |
| 8 | 1 | 0.887 | 0.877 | 0.010 | - | - | 0.966 | 0.980 | 0.679 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 16 | 1 | 0.885 | 0.873 | 0.012 | - | - | 0.980 | 0.981 | 0.670 | 1.24x | 16.6/23.1/28.0% | 1.7/5.5% | 3 |
| 32 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 50 | 1 | 0.891 | 0.880 | 0.012 | - | - | 0.980 | 0.981 | 0.684 | 1.25x | 16.5/23.0/28.1% | 1.7/5.5% | 3 |

> capacity=4: decode_failures 96

> capacity=8: decode_failures 72

> capacity=16: decode_failures 2

### `SF-capacity-local` - capacity  `--scenario rolling`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.891 | 0.878 | 0.013 | - | - | 0.978 | 0.988 | 0.669 | 1.25x | 16.4/23.0/28.0% | 1.7/5.5% | 3 |
| 8 | 1 | 0.887 | 0.877 | 0.010 | - | - | 0.966 | 0.980 | 0.679 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 16 | 1 | 0.885 | 0.873 | 0.012 | - | - | 0.980 | 0.981 | 0.670 | 1.24x | 16.6/23.1/28.0% | 1.7/5.5% | 3 |
| 32 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 50 | 1 | 0.891 | 0.880 | 0.012 | - | - | 0.980 | 0.981 | 0.684 | 1.25x | 16.5/23.0/28.1% | 1.7/5.5% | 3 |

> capacity=4: decode_failures 96

> capacity=8: decode_failures 72

> capacity=16: decode_failures 2

### `SF-capacity-window` - capacity  `--scenario rolling`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.889 | 0.879 | 0.010 | - | - | 0.965 | 0.987 | 0.685 | 1.23x | 16.3/22.7/27.7% | 1.7/5.4% | 3 |
| 16 | 1 | 0.888 | 0.874 | 0.013 | - | - | 0.982 | 0.987 | 0.684 | 1.23x | 16.2/22.6/27.7% | 1.7/5.4% | 3 |
| 32 | 1 | 0.887 | 0.875 | 0.013 | - | - | 0.983 | 0.986 | 0.690 | 1.25x | 16.6/23.0/28.1% | 1.7/5.4% | 3 |

> capacity=8: misdecodes 21

> capacity=8: decode_failures 33

> capacity=16: misdecodes 14

> capacity=16: decode_failures 3

> capacity=32: misdecodes 25

### `SF-catchup` - catch-up-hours  `--scenario rolling`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.863 | 0.847 | 0.016 | - | - | 0.968 | 0.970 | 0.658 | 1.69x | 21.9/30.4/35.9% | 2.4/8.6% | 3 |
| 02-06 | 1 | 0.891 | 0.884 | 0.007 | - | - | 0.949 | 0.986 | 0.685 | 1.28x | 17.0/23.6/28.6% | 1.8/5.6% | 3 |
| 00-08 | 1 | 0.875 | 0.869 | 0.007 | - | - | 0.940 | 0.984 | 0.677 | 1.35x | 17.6/24.8/30.0% | 1.9/6.2% | 3 |

> catch-up-hours=: misdecodes 14

> catch-up-hours=02-06: decode_failures 37

> catch-up-hours=00-08: misdecodes 1

> catch-up-hours=00-08: decode_failures 38

### `SF-hops-flat` - hops-apart  `--scenario rolling`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.880 | 0.879 | 0.002 | - | - | 0.972 | 0.972 | 0.679 | 1.21x | 16.0/22.4/27.4% | 1.7/5.2% | 3 |
| 2 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 3 | 1 | 0.887 | 0.868 | 0.019 | - | - | 0.958 | 0.995 | 0.712 | 1.26x | 16.6/22.9/28.4% | 1.8/5.4% | 3 |
| 4 | 1 | 0.885 | 0.867 | 0.018 | - | - | 0.909 | 0.990 | 0.658 | 1.25x | 16.5/22.9/28.1% | 1.8/5.5% | 3 |

> hops-apart=3: decode_failures 23

> hops-apart=4: decode_failures 30

### `SF-hops-spread` - hops-apart  `--scenario rolling`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.880 | 0.879 | 0.002 | - | - | 0.972 | 0.972 | 0.679 | 1.21x | 16.0/22.4/27.4% | 1.7/5.2% | 3 |
| 2 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 3 | 1 | 0.887 | 0.868 | 0.019 | - | - | 0.958 | 0.995 | 0.712 | 1.26x | 16.6/22.9/28.4% | 1.8/5.4% | 3 |
| 4 | 1 | 0.885 | 0.867 | 0.018 | - | - | 0.909 | 0.990 | 0.658 | 1.25x | 16.5/22.9/28.1% | 1.8/5.5% | 3 |
| 5 | 1 | 0.885 | 0.867 | 0.018 | - | - | 0.909 | 0.990 | 0.658 | 1.25x | 16.5/22.9/28.1% | 1.8/5.5% | 3 |

> hops-apart=3: decode_failures 23

> hops-apart=4: decode_failures 30

> hops-apart=5: decode_failures 30

### `SF-jitter-global` - advert-jitter-s  `--scenario rolling`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.890 | 0.878 | 0.012 | - | - | 0.985 | 0.985 | 0.668 | 1.24x | 16.4/23.1/27.9% | 1.7/5.5% | 3 |
| 30 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 120 | 1 | 0.889 | 0.877 | 0.012 | - | - | 0.982 | 0.983 | 0.664 | 1.25x | 16.4/23.0/28.0% | 1.7/5.5% | 3 |
| 600 | 1 | 0.878 | 0.866 | 0.013 | - | - | 0.980 | 0.981 | 0.668 | 1.26x | 16.7/23.1/28.1% | 1.7/5.6% | 3 |

> advert-jitter-s=600: decode_failures 2

### `SF-jitter-local` - advert-jitter-s  `--scenario rolling`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.890 | 0.878 | 0.012 | - | - | 0.985 | 0.985 | 0.668 | 1.24x | 16.4/23.1/27.9% | 1.7/5.5% | 3 |
| 30 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 120 | 1 | 0.889 | 0.877 | 0.012 | - | - | 0.982 | 0.983 | 0.664 | 1.25x | 16.4/23.0/28.0% | 1.7/5.5% | 3 |
| 600 | 1 | 0.878 | 0.866 | 0.013 | - | - | 0.980 | 0.981 | 0.668 | 1.26x | 16.7/23.1/28.1% | 1.7/5.6% | 3 |

> advert-jitter-s=600: decode_failures 2

### `SF-place-flat` - place  `--scenario rolling`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.890 | 0.866 | 0.023 | - | - | 0.860 | 0.937 | 0.671 | 1.27x | 16.7/22.8/28.4% | 1.8/5.4% | 3 |
| routers | 1 | 0.871 | 0.869 | 0.002 | - | - | 0.973 | 0.973 | 0.653 | 1.24x | 16.4/22.9/27.9% | 1.7/5.3% | 3 |
| alternate-routers | 1 | 0.880 | 0.879 | 0.002 | - | - | 0.972 | 0.972 | 0.679 | 1.21x | 16.0/22.4/27.4% | 1.7/5.2% | 3 |
| beside-router | 1 | 0.875 | 0.873 | 0.002 | - | - | 0.977 | 0.977 | 0.676 | 1.25x | 16.5/23.1/28.2% | 1.8/5.3% | 3 |
| random-clients | 1 | 0.891 | 0.875 | 0.016 | - | - | 0.977 | 0.979 | 0.668 | 1.27x | 17.1/23.5/28.5% | 1.7/5.5% | 3 |
| hops-apart | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |

> place=spread: decode_failures 26

### `SF-place-spread` - place  `--scenario rolling`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.890 | 0.866 | 0.023 | - | - | 0.860 | 0.937 | 0.671 | 1.27x | 16.7/22.8/28.4% | 1.8/5.4% | 3 |
| routers | 1 | 0.871 | 0.869 | 0.002 | - | - | 0.973 | 0.973 | 0.653 | 1.24x | 16.4/22.9/27.9% | 1.7/5.3% | 3 |
| alternate-routers | 1 | 0.880 | 0.879 | 0.002 | - | - | 0.972 | 0.972 | 0.679 | 1.21x | 16.0/22.4/27.4% | 1.7/5.2% | 3 |
| beside-router | 1 | 0.875 | 0.873 | 0.002 | - | - | 0.977 | 0.977 | 0.676 | 1.25x | 16.5/23.1/28.2% | 1.8/5.3% | 3 |
| random-clients | 1 | 0.891 | 0.875 | 0.016 | - | - | 0.977 | 0.979 | 0.668 | 1.27x | 17.1/23.5/28.5% | 1.7/5.5% | 3 |
| hops-apart | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |

> place=spread: decode_failures 26

### `SF-provide-transport` - provide-transport  `--scenario rolling`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| broadcast | 1 | 0.910 | 0.870 | 0.041 | - | - | 0.979 | 0.980 | 0.718 | 1.31x | 17.6/24.1/29.0% | 1.8/5.6% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario rolling`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| heard | 1 | 0.885 | 0.872 | 0.013 | - | - | 0.981 | 0.983 | 0.676 | 1.22x | 16.2/22.5/27.4% | 1.7/5.4% | 3 |

> replay-ordering=heard: misdecodes 10

### `SF-replay-order-broadcast` - replay-ordering  `--scenario rolling`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.910 | 0.870 | 0.041 | - | - | 0.979 | 0.980 | 0.718 | 1.31x | 17.6/24.1/29.0% | 1.8/5.6% | 3 |
| heard | 1 | 0.915 | 0.874 | 0.041 | - | - | 0.985 | 0.987 | 0.711 | 1.33x | 17.7/24.3/29.2% | 1.9/5.7% | 3 |

> replay-ordering=heard: misdecodes 3

### `SF-resolve` - resolve  `--scenario rolling`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| enum | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.976 | 0.982 | 0.697 | 1.24x | 16.3/22.8/27.9% | 1.7/5.5% | 3 |
| hybrid | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |

### `SF-servers-allrouters` - servers  `--scenario rolling`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.871 | 0.869 | 0.002 | - | - | 0.973 | 0.973 | 0.653 | 1.24x | 16.4/22.9/27.9% | 1.7/5.3% | 3 |
| 6 | 1 | 0.884 | 0.876 | 0.007 | - | - | 0.983 | 0.984 | 0.685 | 1.25x | 16.7/23.4/28.3% | 1.8/5.5% | 6 |

### `SF-servers-flat` - servers  `--scenario rolling`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.874 | 0.862 | 0.011 | - | - | 0.974 | 0.979 | 0.651 | 1.24x | 16.3/22.7/27.7% | 1.7/5.3% | 2 |
| 3 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 5 | 1 | 0.890 | 0.874 | 0.016 | - | - | 0.988 | 0.990 | 0.661 | 1.28x | 17.0/23.6/28.7% | 1.8/5.7% | 5 |
| 8 | 1 | 0.890 | 0.872 | 0.018 | - | - | 0.985 | 0.987 | 0.666 | 1.30x | 17.1/24.1/28.9% | 1.8/5.6% | 8 |

> servers=8: misdecodes 1

### `SF-servers-spread` - servers  `--scenario rolling`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.874 | 0.862 | 0.011 | - | - | 0.974 | 0.979 | 0.651 | 1.24x | 16.3/22.7/27.7% | 1.7/5.3% | 2 |
| 3 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 5 | 1 | 0.890 | 0.874 | 0.016 | - | - | 0.988 | 0.990 | 0.661 | 1.28x | 17.0/23.6/28.7% | 1.8/5.7% | 5 |
| 8 | 1 | 0.890 | 0.872 | 0.018 | - | - | 0.985 | 0.987 | 0.666 | 1.30x | 17.1/24.1/28.9% | 1.8/5.6% | 8 |

> servers=8: misdecodes 1

### `SF-signed` - signed  `--scenario rolling`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| True | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario rolling`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.892 | 0.881 | 0.011 | - | - | 0.983 | 0.987 | 0.669 | 1.22x | 16.0/22.1/27.1% | 1.7/5.2% | 3 |
| 1 | 1 | 0.890 | 0.879 | 0.011 | - | - | 0.979 | 0.980 | 0.658 | 1.20x | 15.7/21.7/26.6% | 1.7/5.2% | 3 |
| 2 | 1 | 0.886 | 0.874 | 0.011 | - | - | 0.981 | 0.982 | 0.658 | 1.19x | 15.7/21.8/26.6% | 1.7/5.2% | 3 |
| 4 | 1 | 0.888 | 0.878 | 0.010 | - | - | 0.981 | 0.983 | 0.673 | 1.19x | 15.7/21.7/26.7% | 1.6/5.1% | 3 |

### `SF-width` - short-id-bits  `--scenario rolling`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.885 | 0.873 | 0.012 | - | - | 0.984 | 0.987 | 0.660 | 1.24x | 16.4/22.7/27.7% | 1.7/5.4% | 3 |
| 24 | 1 | 0.883 | 0.871 | 0.012 | - | - | 0.978 | 0.979 | 0.676 | 1.24x | 16.3/22.7/27.8% | 1.7/5.4% | 3 |
| 32 | 1 | 0.884 | 0.871 | 0.013 | - | - | 0.977 | 0.979 | 0.665 | 1.24x | 16.4/22.9/27.9% | 1.7/5.5% | 3 |
| 64 | 1 | 0.893 | 0.880 | 0.013 | - | - | 0.986 | 0.988 | 0.662 | 1.25x | 16.5/23.0/27.9% | 1.8/5.5% | 3 |

### `SF-window-size` - window-size  `--scenario rolling`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.881 | 0.867 | 0.014 | - | - | 0.978 | 0.980 | 0.666 | 1.30x | 17.3/23.9/28.8% | 1.8/5.7% | 3 |
| 16 | 1 | 0.880 | 0.866 | 0.014 | - | - | 0.976 | 0.978 | 0.679 | 1.26x | 16.6/23.2/28.2% | 1.7/5.5% | 3 |
| 32 | 1 | 0.887 | 0.875 | 0.013 | - | - | 0.983 | 0.986 | 0.690 | 1.25x | 16.6/23.0/28.1% | 1.7/5.4% | 3 |

> window-size=8: misdecodes 120

> window-size=16: misdecodes 58

> window-size=32: misdecodes 25

### `TH-congestion` - no-congestion-scaling  `--scenario rolling`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.970 | 0.969 | 0.001 | - | - | 0.999 | 1.000 | 0.812 | 2.13x | 24.9/37.5/42.8% | 1.4/5.3% | 3 |
| True | 1 | 0.720 | 0.715 | 0.005 | - | - | 0.801 | 0.887 | 0.511 | 5.77x | 59.4/74.9/79.6% | 4.2/13.5% | 3 |

> no-congestion-scaling=True: queue drops 18.6% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 100

### `TH-congestion-input` - congestion-input  `--scenario rolling`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.565 | 0.555 | 0.011 | - | - | 0.812 | 0.815 | 0.153 | 4.46x | 17.4/27.5/37.7% | 1.5/5.5% | 3 |
| truesize | 1 | 0.599 | 0.589 | 0.010 | - | - | 0.844 | 0.848 | 0.156 | 3.41x | 13.2/22.2/30.6% | 1.1/4.7% | 3 |

> congestion-input=truesize: decode_failures 1

### `TH-congestion-mode` - congestion-mode  `--scenario rolling`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.972 | 0.971 | 0.001 | - | - | 0.999 | 0.999 | 0.819 | 1.94x | 22.7/34.3/39.2% | 1.3/4.8% | 3 |
| adaptive | 1 | 0.970 | 0.969 | 0.001 | - | - | 0.999 | 1.000 | 0.812 | 2.13x | 24.9/37.5/42.8% | 1.4/5.3% | 3 |

