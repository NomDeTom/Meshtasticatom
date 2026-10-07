# Sweep blocks-2026-10-07-7896540

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** ridge
- **seed base** 7896540 · seeds 7896540
- **blocks** 87 run
- **compute** 13.1 h of simulator time across every cell
- **generated** 2026-10-07T10:09:44+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>111 warnings</summary>

- AD-badrouters: role-placement=degree: decode_failures 21
- AD-badrouters: role-placement=inverse: decode_failures 24
- AD-badrouters: role-placement=random: decode_failures 7
- AD-badrouters: slower: 5.88 s per simulated hour against 2 over 47 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-flooding: role-mix=baymesh-2026-08: decode_failures 21
- AD-flooding: slower: 5.73 s per simulated hour against 2.5 over 47 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-nomute: role-mix=baymesh-2026-08: decode_failures 21
- AD-siting: siting-mix=uniform: decode_failures 21
- AD-siting: slower: 2.95 s per simulated hour against 1.39 over 47 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 45
- DB-hotstore-stress: max-num-nodes=120: decode_failures 95
- DB-hotstore-stress: max-num-nodes=250: decode_failures 91
- DB-hotstore-stress: slower: 44 s per simulated hour against 21.9 over 47 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-warm: warm-num-nodes=0: queue drops 19.3% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 97
- DB-warm: warm-num-nodes=25: queue drops 19.3% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 97
- DB-warm: warm-num-nodes=100: queue drops 19.3% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 97
- DB-warm: warm-num-nodes=2000: queue drops 19.3% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 97
- DG-burst: burst-loss=0.1: decode_failures 1
- DG-burst: burst-loss=0.2: decode_failures 22
- DG-burst: burst-loss=0.3: decode_failures 30
- DG-loss: extra-loss=0.3: decode_failures 23
- DG-outage: burst-loss=0.1: decode_failures 52
- DG-outage: burst-loss=0.2: decode_failures 48
- DG-outage: burst-loss=0.3: decode_failures 25
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 28
- LD-chatty: broadcast-interval-s=900: decode_failures 2
- LD-chatty: broadcast-interval-s=300: decode_failures 31
- LD-interval: broadcast-interval-s=900: decode_failures 2
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 19.3% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 97
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 25.5% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 95
- MS-density: nodes=150: decode_failures 8
- MS-hopscale: nodes=120: decode_failures 59
- MS-hopscale: nodes=250: decode_failures 137
- MS-hopscale: nodes=500: decode_failures 2
- MS-oversubscribed: nodes=120: decode_failures 37
- MS-oversubscribed: nodes=250: decode_failures 95
- MS-roles-fav: role-mix=baymesh-2026-08: decode_failures 1
- MS-roles: role-mix=baymesh-2026-08: decode_failures 21
- MS-roles: slower: 5.05 s per simulated hour against 1.7 over 47 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-siting: siting-mix=event: decode_failures 5
- MS-size: nodes=120: decode_failures 59
- MS-stretch: stretch=1.25: decode_failures 2
- MS-stretch: stretch=1.5: decode_failures 1
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 1
- PR-repeats-busy: extra-repeats=True: misdecodes 1
- RF-bw500: preset=SHORT_TURBO: decode_failures 2
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 24
- RF-bw500: slower: 3.95 s per simulated hour against 1.82 over 47 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-eu-presets: preset=SHORT_FAST: decode_failures 11
- RF-noise: noise-profile=temporal: decode_failures 2
- RF-noise: noise-profile=periodic: decode_failures 1
- RF-preset: preset=SHORT_FAST: decode_failures 11
- RF-preset: preset=LONG_MODERATE: decode_failures 40
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 2
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 1
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 5
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 1
- RF-txpower: tx-power=22: decode_failures 20
- RF-txpower: tx-power=17: decode_failures 3
- RT-hoplimit: hop-limit=3: decode_failures 1
- RT-hopspread: hop-limit=3: decode_failures 1
- RT-spread: hop-spread=False: decode_failures 1
- SF-bucket-mode: bucket-mode=global: misdecodes 25
- SF-bucket-mode: bucket-mode=time: misdecodes 11
- SF-bucket-mode: bucket-mode=window: misdecodes 17
- SF-bucket-time: time-bucket-s=600: misdecodes 125
- SF-bucket-time: time-bucket-s=1800: misdecodes 11
- SF-bucket-time: time-bucket-s=3600: misdecodes 3
- SF-bucket-time: time-bucket-s=3600: decode_failures 2
- SF-cadence: trigger=interval: misdecodes 13
- SF-cadence: trigger=interval: decode_failures 7
- SF-cadence: trigger=aimd: misdecodes 2
- SF-cadence: trigger=aimd: decode_failures 3
- SF-cadence: trigger=bucket+interval: misdecodes 17
- SF-capacity-local: capacity=4: decode_failures 96
- SF-capacity-local: capacity=8: decode_failures 84
- SF-capacity-local: capacity=16: decode_failures 12
- SF-capacity: capacity=4: decode_failures 96
- SF-capacity: capacity=8: decode_failures 84
- SF-capacity: capacity=16: decode_failures 12
- SF-capacity-window: capacity=8: misdecodes 10
- SF-capacity-window: capacity=8: decode_failures 66
- SF-capacity-window: capacity=16: misdecodes 16
- SF-capacity-window: capacity=16: decode_failures 4
- SF-capacity-window: capacity=32: misdecodes 17
- SF-catchup: catch-up-hours=: misdecodes 17
- SF-catchup: catch-up-hours=02-06: misdecodes 1
- SF-catchup: catch-up-hours=02-06: decode_failures 34
- SF-catchup: catch-up-hours=00-08: decode_failures 33
- SF-hops-flat: hops-apart=4: decode_failures 28
- SF-hops-spread: hops-apart=4: decode_failures 28
- SF-hops-spread: hops-apart=5: decode_failures 20
- SF-place-flat: place=spread: decode_failures 1
- SF-place-spread: place=spread: decode_failures 1
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 3
- SF-replay-order: replay-ordering=heard: misdecodes 18
- SF-window-size: window-size=8: misdecodes 160
- SF-window-size: window-size=16: misdecodes 54
- SF-window-size: window-size=32: misdecodes 17
- TH-congestion-input: congestion-input=hotstore: decode_failures 95
- TH-congestion-input: congestion-input=truesize: decode_failures 74
- TH-congestion-input: slower: 43.1 s per simulated hour against 10.5 over 47 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- TH-congestion-mode: congestion-mode=static: misdecodes 1
- TH-congestion: no-congestion-scaling=True: queue drops 16.8% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 116

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `TH-congestion-input` | 43.1 | 10.5 | 4.09x | 47 |
| `MS-roles` | 5.05 | 1.7 | 2.98x | 47 |
| `AD-badrouters` | 5.88 | 2 | 2.95x | 47 |
| `AD-flooding` | 5.73 | 2.5 | 2.29x | 47 |
| `RF-bw500` | 3.95 | 1.82 | 2.17x | 47 |
| `AD-siting` | 2.95 | 1.39 | 2.13x | 47 |
| `DB-hotstore-stress` | 44 | 21.9 | 2.01x | 47 |
| `DG-loss` | 4.37 | 2.27 | 1.93x | 47 |
| `AD-nomute` | 4.37 | 2.28 | 1.91x | 47 |
| `RF-preset` | 5.39 | 2.85 | 1.89x | 47 |
| `MS-size` | 6.35 | 3.39 | 1.87x | 47 |
| `RF-txpower` | 2.67 | 1.58 | 1.69x | 47 |
| `DG-outage` | 10.6 | 6.81 | 1.56x | 47 |
| `RF-preset-turbo` | 1 | 1.54 | 0.65x | 43 |
| `PR-repeats-busy` | 2.43 | 3.79 | 0.64x | 47 |
| `AD-amplifiers` | 1.01 | 1.61 | 0.63x | 47 |
| `MS-topology` | 1.03 | 1.97 | 0.52x | 47 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.984 | 0.984 | 0.844 → 0.856 | 1.1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.975 | 0.975 | 0.837 → 0.856 | 1.2x bytes_on_air | up | 3 |
| `RF-preset-turbo` | preset | **held** | 0.038 → 0.975 | 0.938 | 0.029 → 0.852 | 52x advert_bytes | up | 5 |
| `RF-txpower` | tx-power | **held** | 0.132 → 0.975 | 0.843 | 0.042 → 0.852 | 8.6x advert_bytes | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.100 → 0.915 | 0.816 | 0.089 → 0.791 | 1.5e+02x sr_airtime | down | 4 |
| `MS-stretch` | stretch | **held** | 0.165 → 0.975 | 0.810 | 0.078 → 0.852 | 7x sr_airtime | down | 4 |
| `RF-bw500` | preset | **held** | 0.186 → 0.960 | 0.774 | 0.080 → 0.782 | 5.7x advert_bytes | up | 3 |
| `AD-siting` | siting-mix | **text** | 0.051 → 0.819 | 0.767 | 0.051 → 0.794 | 6.5x sr_bytes | down | 3 |
| `MS-siting` | siting-mix | **text** | 0.238 → 0.979 | 0.740 | 0.231 → 0.979 | 3.7x sr_bytes | up | 4 |
| `RF-eu-presets` | preset | **text** | 0.253 → 0.865 | 0.613 | 0.248 → 0.852 | 2.7x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.253 → 0.865 | 0.613 | 0.248 → 0.852 | 3.1x sr_airtime | up | 3 |
| `MS-topology` | topology | **held** | 0.405 → 0.987 | 0.582 | 0.394 → 0.951 | 7.4x sr_airtime | up | 4 |
| `MS-hopscale` | nodes | **text** | 0.284 → 0.865 | 0.581 | 0.280 → 0.852 | 6.9x bytes_on_air | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.399 → 0.909 | 0.510 | 0.284 → 0.737 | 4.3x bytes_on_air | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.327 → 0.708 | 0.381 | 0.319 → 0.684 | 2.5x sr_airtime | up | 2 |
| `DG-outage` | burst-loss | **text** | 0.500 → 0.865 | 0.365 | 0.477 → 0.852 | 1.9x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.534 → 0.886 | 0.353 | 0.512 → 0.875 | 6.6x sr_airtime | down | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.590 → 0.941 | 0.351 | 0.571 → 0.939 | 7.5x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.548 → 0.865 | 0.317 | 0.513 → 0.852 | 2x sr_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.408 → 0.724 | 0.317 | 0.289 → 0.483 | 8.8x sr_airtime | up | 3 |
| `MS-density` | nodes | **text** | 0.658 → 0.952 | 0.294 | 0.652 → 0.951 | 7.6x sr_airtime | up | 5 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.699 → 0.943 | 0.245 | 0.693 → 0.942 | 4.4x sr_airtime | down | 2 |
| `MS-size` | nodes | **text** | 0.643 → 0.865 | 0.222 | 0.634 → 0.852 | 6.3x sr_airtime | down | 5 |
| `RT-hoplimit` | hop-limit | **text** | 0.733 → 0.941 | 0.209 | 0.692 → 0.940 | 2.6x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.733 → 0.923 | 0.191 | 0.692 → 0.919 | 2.2x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **text** | 0.699 → 0.865 | 0.166 | 0.686 → 0.852 | 1.4x sr_bytes | down | 4 |
| `DG-loss` | extra-loss | **text** | 0.714 → 0.865 | 0.151 | 0.691 → 0.852 | 1.6x sr_bytes | down | 4 |
| `RT-spread` | hop-spread | **text** | 0.733 → 0.865 | 0.132 | 0.692 → 0.852 | 1.7x sr_bytes | up | 2 |
| `SC-signing` | signature-policy | **text** | 0.752 → 0.865 | 0.113 | 0.752 → 0.852 | 1.4x sr_airtime | down | 3 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.873 → 0.975 | 0.102 | 0.851 → 0.852 | 35x sr_airtime | down | 3 |
| `AD-flooding` | role-mix | **text** | 0.819 → 0.920 | 0.102 | 0.794 → 0.914 | 2.2x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.819 → 0.920 | 0.102 | 0.794 → 0.914 | 2.2x bytes_on_air | up | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.805 → 0.906 | 0.102 | 0.784 → 0.899 | 4.8x sr_airtime | up | 4 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.865 → 0.965 | 0.100 | 0.852 → 0.964 | 2.6x sr_bytes | up | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.823 → 0.921 | 0.098 | 0.812 → 0.917 | 2.1x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.838 → 0.921 | 0.083 | 0.826 → 0.917 | 2x sr_airtime | down | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.865 → 0.946 | 0.081 | 0.852 → 0.942 | 1.7x sr_bytes | up | 3 |
| `TH-congestion-input` | congestion-input | **held** | 0.715 → 0.795 | 0.080 | 0.477 → 0.511 | 1.6x sr_airtime | up | 2 |
| `RF-duct` | duct-per-hour | **text** | 0.865 → 0.945 | 0.080 | 0.852 → 0.936 | 1.6x bytes_on_air | up | 3 |
| `SF-cadence` | trigger | **held** | 0.906 → 0.975 | 0.069 | 0.820 → 0.852 | 14x advert_bytes | down | 4 |
| `AD-badrouters` | role-placement | **text** | 0.755 → 0.819 | 0.064 | 0.726 → 0.794 | 1.5x sr_bytes | down | 3 |
| `FW-versions` | profile | **text** | 0.865 → 0.928 | 0.063 | 0.852 → 0.925 | 3.1x bytes_on_air | down | 5 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.611 → 0.669 | 0.058 | 0.607 → 0.664 | 1.2x sr_airtime | down | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.809 → 0.865 | 0.056 | 0.788 → 0.852 | 1.5x sr_airtime | down | 4 |
| `MS-roles` | role-mix | **text** | 0.819 → 0.864 | 0.046 | 0.794 → 0.853 | 1.5x sr_bytes | down | 2 |
| `FW-firmware` | profile | **text** | 0.865 → 0.908 | 0.043 | 0.852 → 0.903 | 3.1x bytes_on_air | down | 2 |
| `SF-hops-flat` | hops-apart | **held** | 0.943 → 0.984 | 0.042 | 0.844 → 0.854 | 1.9x sr_bytes | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.943 → 0.984 | 0.042 | 0.844 → 0.854 | 1.9x sr_bytes | down | 5 |
| `SF-place-flat` | place | **text** | 0.849 → 0.889 | 0.040 | 0.847 → 0.853 | 2.9x sr_bytes | down | 6 |
| `SF-place-spread` | place | **text** | 0.849 → 0.889 | 0.040 | 0.847 → 0.853 | 2.9x sr_bytes | down | 6 |
| `SF-catchup` | catch-up-hours | **held** | 0.930 → 0.970 | 0.040 | 0.823 → 0.854 | 9.1x advert_bytes | down | 3 |
| `FW-signing-cost` | profile-flag | **text** | 0.865 → 0.904 | 0.039 | 0.852 → 0.896 | 3.3x bytes_on_air | down | 2 |
| `SF-capacity-window` | capacity | **held** | 0.945 → 0.976 | 0.031 | 0.850 → 0.857 | 2.3x advert_bytes | up | 3 |
| `SF-provide-transport` | provide-transport | **text** | 0.865 → 0.894 | 0.029 | 0.834 → 0.852 | 3.4x sr_airtime | up | 2 |
| `MS-roles-fav` | role-mix | **held** | 0.952 → 0.980 | 0.028 | 0.849 → 0.875 | 1x bytes_on_air | down | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.872 → 0.900 | 0.028 | 0.859 → 0.890 | 1.1x sr_bytes | up | 2 |
| `RT-hopassign` | hop-assign | **text** | 0.839 → 0.865 | 0.026 | 0.824 → 0.852 | 1.1x sr_airtime | down | 2 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.865 → 0.887 | 0.021 | 0.852 → 0.877 | 2.3x bytes_on_air | up | 4 |
| `FW-mixed` | legacy-fraction | **text** | 0.865 → 0.886 | 0.021 | 0.852 → 0.878 | 2.2x bytes_on_air | up | 4 |
| `MS-router-late` | router-late-fraction | **text** | 0.865 → 0.886 | 0.021 | 0.852 → 0.877 | 1.2x bytes_on_air | up | 4 |
| `DM-mode` | dm-mode | **text** | 0.806 → 0.825 | 0.019 | 0.806 → 0.825 | 1.2x sr_airtime | up | 3 |
| `LD-diurnal` | diurnal | **text** | 0.865 → 0.882 | 0.017 | 0.852 → 0.870 | 1.2x sr_bytes | down | 3 |
| `SF-window-size` | window-size | **text** | 0.853 → 0.870 | 0.017 | 0.839 → 0.858 | 4.4x advert_bytes | up | 3 |
| `AD-worst` | role-placement | **held** | 0.891 → 0.907 | 0.015 | 0.715 → 0.735 | 1.3x sr_bytes | up | 2 |
| `SF-servers-flat` | servers | **held** | 0.971 → 0.984 | 0.013 | 0.834 → 0.852 | 7.3x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.971 → 0.984 | 0.013 | 0.834 → 0.852 | 7.3x sr_bytes | up | 4 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.965 → 0.978 | 0.013 | 0.834 → 0.841 | 1.1x sr_airtime | up | 2 |
| `SF-sr-retries` | sr-retries | **held** | 0.968 → 0.981 | 0.013 | 0.844 → 0.856 | 1.2x sr_bytes | down | 4 |
| `SF-servers-allrouters` | servers | **held** | 0.959 → 0.970 | 0.011 | 0.841 → 0.847 | 2.7x sr_bytes | up | 2 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.851 → 0.862 | 0.011 | 0.837 → 0.850 | 5.4x advert_bytes | up | 3 |
| `SF-capacity` | capacity | **text** | 0.855 → 0.865 | 0.010 | 0.840 → 0.852 | 5.3x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **text** | 0.855 → 0.865 | 0.010 | 0.840 → 0.852 | 5.3x advert_bytes | down | 5 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.863 → 0.872 | 0.009 | 0.849 → 0.859 | 1.1x sr_bytes | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.863 → 0.872 | 0.009 | 0.849 → 0.859 | 1.1x sr_bytes | up | 4 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.943 → 0.952 | 0.009 | 0.942 → 0.951 | 1.1x bytes_on_air | down | 2 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.857 → 0.865 | 0.009 | 0.845 → 0.852 | 2.6x advert_bytes | up | 4 |
| `SF-width` | short-id-bits | **held** | 0.975 → 0.983 | 0.008 | 0.847 → 0.852 | 3.1x advert_bytes | down | 4 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.936 → 0.943 | 0.007 | 0.935 → 0.942 | 1.2x sr_airtime | down | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.975 → 0.982 | 0.007 | 0.852 → 0.853 | 2.5x sr_airtime | up | 2 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.819 → 0.824 | 0.005 | 0.819 → 0.824 | 1.1x sr_airtime | down | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.860 → 0.865 | 0.005 | 0.847 → 0.852 | 1x sr_bytes | down | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.862 → 0.865 | 0.003 | 0.850 → 0.852 | 1x sr_airtime | down | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.958 → 0.960 | 0.002 | 0.824 → 0.825 | 1.1x sr_airtime | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.943 → 0.945 | 0.002 | 0.942 → 0.944 | 1x sr_airtime | up | 2 |
| `SF-resolve` | resolve | **text** | 0.864 → 0.865 | 0.002 | 0.849 → 0.852 | 5.7x advert_bytes | = | 3 |

### Moved no delivery measure

Not the same as having done nothing: several arms hold delivery flat by design and differ in what they spend. Three ways of reconciling the same two sets had better agree on what is held; where they differ is the price.

| block | arm | price | cells |
| --- | --- | --- | --: |
| `DB-warm` | warm-num-nodes | - | 4 |
| `SF-signed` | signed | 1.4x advert_bytes | 2 |

## Every block

### `AD-amplifiers` - amplifier-mix  `--scenario ridge`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| sprinkled | 1 | 0.936 | 0.932 | 0.004 | - | - | 0.992 | 0.993 | 0.778 | 1.23x | 18.3/24.6/27.7% | 1.9/5.4% | 3 |
| arms-race | 1 | 0.965 | 0.964 | 0.001 | - | - | 0.989 | 0.989 | 0.906 | 1.06x | 23.9/29.3/30.7% | 1.3/5.3% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario ridge`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 0.1 | 1 | 0.890 | 0.879 | 0.012 | - | - | 0.934 | 0.938 | 0.668 | 1.23x | 16.6/22.9/27.7% | 1.7/5.0% | 3 |
| 0.3 | 1 | 0.946 | 0.942 | 0.005 | - | - | 0.989 | 0.990 | 0.812 | 1.00x | 19.9/27.0/29.6% | 1.3/4.9% | 3 |

### `AD-badrouters` - role-placement  `--scenario ridge`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.819 | 0.794 | 0.025 | - | - | 0.944 | 0.956 | 0.479 | 1.24x | 14.1/22.8/27.3% | 2.2/5.1% | 3 |
| inverse | 1 | 0.755 | 0.726 | 0.029 | - | - | 0.903 | 0.942 | 0.085 | 1.08x | 11.9/17.8/23.2% | 2.0/3.1% | 3 |
| random | 1 | 0.787 | 0.768 | 0.019 | - | - | 0.943 | 0.954 | 0.406 | 1.14x | 13.5/17.1/20.8% | 1.9/4.4% | 3 |

> role-placement=degree: decode_failures 21

> role-placement=inverse: decode_failures 24

> role-placement=random: decode_failures 7

> slower: 5.88 s per simulated hour against 2 over 47 prior run(s) - 2.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-flooding` - role-mix  `--scenario ridge`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.819 | 0.794 | 0.025 | - | - | 0.944 | 0.956 | 0.479 | 1.24x | 14.1/22.8/27.3% | 2.2/5.1% | 3 |
| all-routers | 1 | 0.920 | 0.914 | 0.007 | - | - | 0.995 | 0.996 | 0.781 | 2.75x | 28.2/36.0/39.7% | 4.4/5.5% | 3 |

> role-mix=baymesh-2026-08: decode_failures 21

> slower: 5.73 s per simulated hour against 2.5 over 47 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-nomute` - role-mix  `--scenario ridge`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.819 | 0.794 | 0.025 | - | - | 0.944 | 0.956 | 0.479 | 1.24x | 14.1/22.8/27.3% | 2.2/5.1% | 3 |
| no-mute | 1 | 0.861 | 0.847 | 0.014 | - | - | 0.984 | 0.984 | 0.605 | 1.35x | 15.5/21.6/24.2% | 2.0/5.3% | 3 |
| all-routers | 1 | 0.920 | 0.914 | 0.007 | - | - | 0.995 | 0.996 | 0.781 | 2.75x | 28.2/36.0/39.7% | 4.4/5.5% | 3 |

> role-mix=baymesh-2026-08: decode_failures 21

### `AD-siting` - siting-mix  `--scenario ridge`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.819 | 0.794 | 0.025 | - | - | 0.944 | 0.956 | 0.479 | 1.24x | 14.1/22.8/27.3% | 2.2/5.1% | 3 |
| local-typical | 1 | 0.601 | 0.579 | 0.022 | - | - | 0.851 | 0.852 | 0.000 | 1.26x | 12.6/19.8/28.4% | 2.0/5.6% | 3 |
| basement-heavy | 1 | 0.051 | 0.051 | 0.001 | - | - | 0.179 | 0.180 | 0.000 | 0.44x | 0.4/6.5/10.6% | 0.2/2.7% | 3 |

> siting-mix=uniform: decode_failures 21

> slower: 2.95 s per simulated hour against 1.39 over 47 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-worst` - role-placement  `--scenario ridge`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.740 | 0.735 | 0.005 | - | - | 0.891 | 0.892 | 0.114 | 2.46x | 15.9/30.2/38.3% | 1.9/5.7% | 3 |
| inverse | 1 | 0.727 | 0.715 | 0.012 | - | - | 0.907 | 0.907 | 0.135 | 2.36x | 14.1/24.7/33.0% | 1.9/3.3% | 3 |

### `BL-control` - protocol  `--scenario ridge`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.856 | 0.856 | 0.000 | - | - | 0 | 0.000 | 0.670 | 1.38x | 15.5/23.9/27.3% | 2.0/5.0% | 3 |
| sr | 1 | 0.865 | 0.844 | 0.021 | - | - | 0.984 | 0.987 | 0.669 | 1.44x | 16.3/24.9/28.4% | 2.1/5.3% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario ridge`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.823 | 0.812 | 0.011 | - | - | 0.931 | 0.939 | 0.625 | 3.43x | 35.1/54.5/62.1% | 4.9/10.3% | 3 |
| 100 | 1 | 0.921 | 0.917 | 0.004 | - | - | 0.980 | 0.980 | 0.727 | 1.76x | 18.3/29.6/34.1% | 2.5/5.4% | 3 |
| 120 | 1 | 0.921 | 0.917 | 0.004 | - | - | 0.980 | 0.980 | 0.727 | 1.76x | 18.3/29.6/34.1% | 2.5/5.4% | 3 |
| 250 | 1 | 0.921 | 0.917 | 0.004 | - | - | 0.980 | 0.980 | 0.727 | 1.76x | 18.3/29.6/34.1% | 2.5/5.4% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario ridge`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.293 | 0.289 | 0.003 | - | - | 0.408 | 0.572 | 0.097 | 11.20x | 36.0/65.8/77.7% | 3.9/10.8% | 3 |
| 120 | 1 | 0.488 | 0.477 | 0.011 | - | - | 0.715 | 0.790 | 0.126 | 4.62x | 15.2/33.8/46.8% | 1.5/5.8% | 3 |
| 250 | 1 | 0.495 | 0.483 | 0.012 | - | - | 0.724 | 0.797 | 0.134 | 4.51x | 15.1/32.7/45.0% | 1.5/5.7% | 3 |

> max-num-nodes=10: decode_failures 45

> max-num-nodes=120: decode_failures 95

> max-num-nodes=250: decode_failures 91

> slower: 44 s per simulated hour against 21.9 over 47 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-platform` - platform-mix  `--scenario ridge`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.921 | 0.917 | 0.004 | - | - | 0.980 | 0.980 | 0.727 | 1.76x | 18.3/29.6/34.1% | 2.5/5.4% | 3 |
| baymesh-2026-08 | 1 | 0.921 | 0.917 | 0.004 | - | - | 0.980 | 0.980 | 0.727 | 1.76x | 18.3/29.6/34.1% | 2.5/5.4% | 3 |
| constrained | 1 | 0.838 | 0.826 | 0.012 | - | - | 0.951 | 0.956 | 0.657 | 3.44x | 35.3/54.6/62.2% | 4.9/10.4% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario ridge`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.669 | 0.664 | 0.004 | - | - | 0.775 | 0.833 | 0.396 | 5.59x | 53.9/75.6/79.3% | 4.0/12.5% | 3 |
| 25 | 1 | 0.669 | 0.664 | 0.004 | - | - | 0.775 | 0.833 | 0.396 | 5.59x | 53.9/75.6/79.3% | 4.0/12.5% | 3 |
| 100 | 1 | 0.669 | 0.664 | 0.004 | - | - | 0.775 | 0.833 | 0.396 | 5.59x | 53.9/75.6/79.3% | 4.0/12.5% | 3 |
| 2000 | 1 | 0.669 | 0.664 | 0.004 | - | - | 0.775 | 0.833 | 0.396 | 5.59x | 53.9/75.6/79.3% | 4.0/12.5% | 3 |

> warm-num-nodes=0: queue drops 19.3% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 97

> warm-num-nodes=25: queue drops 19.3% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 97

> warm-num-nodes=100: queue drops 19.3% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 97

> warm-num-nodes=2000: queue drops 19.3% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 97

### `DG-burst` - burst-loss  `--scenario ridge`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 0.1 | 1 | 0.773 | 0.750 | 0.023 | - | - | 0.960 | 0.967 | 0.545 | 1.34x | 15.4/23.2/26.8% | 2.0/4.9% | 3 |
| 0.2 | 1 | 0.673 | 0.639 | 0.034 | - | - | 0.900 | 0.925 | 0.398 | 1.24x | 14.3/21.9/24.8% | 1.8/4.4% | 3 |
| 0.3 | 1 | 0.548 | 0.513 | 0.035 | - | - | 0.794 | 0.855 | 0.293 | 1.11x | 13.3/20.4/22.9% | 1.6/3.8% | 3 |

> burst-loss=0.1: decode_failures 1

> burst-loss=0.2: decode_failures 22

> burst-loss=0.3: decode_failures 30

### `DG-loss` - extra-loss  `--scenario ridge`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 0.1 | 1 | 0.827 | 0.811 | 0.016 | - | - | 0.970 | 0.974 | 0.592 | 1.46x | 16.7/24.8/28.5% | 2.1/5.1% | 3 |
| 0.2 | 1 | 0.785 | 0.763 | 0.022 | - | - | 0.960 | 0.963 | 0.505 | 1.47x | 16.9/25.3/28.8% | 2.1/4.9% | 3 |
| 0.3 | 1 | 0.714 | 0.691 | 0.023 | - | - | 0.908 | 0.934 | 0.398 | 1.49x | 17.2/26.0/29.4% | 2.2/4.9% | 3 |

> extra-loss=0.3: decode_failures 23

### `DG-outage` - burst-loss  `--scenario ridge`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 0.1 | 1 | 0.755 | 0.735 | 0.021 | - | - | 0.944 | 0.970 | 0.544 | 1.36x | 15.5/23.9/27.5% | 2.0/5.2% | 3 |
| 0.2 | 1 | 0.651 | 0.624 | 0.027 | - | - | 0.837 | 0.915 | 0.432 | 1.28x | 14.9/22.5/25.3% | 1.9/4.6% | 3 |
| 0.3 | 1 | 0.500 | 0.477 | 0.023 | - | - | 0.674 | 0.833 | 0.301 | 1.15x | 13.4/20.9/24.0% | 1.7/4.2% | 3 |

> burst-loss=0.1: decode_failures 52

> burst-loss=0.2: decode_failures 48

> burst-loss=0.3: decode_failures 25

### `DM-mode` - dm-mode  `--scenario ridge`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.806 | 0.806 | 0.000 | - | - | 0.959 | 0.966 | 0.602 | 1.94x | 21.8/32.7/37.8% | 2.9/6.9% | 3 |
| directed-with-late-flood | 1 | 0.825 | 0.825 | 0.000 | - | - | 0.960 | 0.978 | 0.616 | 1.72x | 19.3/29.4/34.1% | 2.5/6.3% | 3 |
| m4-early-flood | 1 | 0.818 | 0.818 | 0.000 | - | - | 0.956 | 0.972 | 0.619 | 1.74x | 19.4/29.6/34.4% | 2.6/6.4% | 3 |

### `FW-firmware` - profile  `--scenario ridge`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.908 | 0.903 | 0.005 | - | - | 0.995 | 0.996 | 0.757 | 0.82x | 9.2/12.3/14.0% | 1.4/1.9% | 3 |
| 2.8 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario ridge`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 0.25 | 1 | 0.886 | 0.878 | 0.008 | - | - | 0.978 | 0.979 | 0.678 | 1.28x | 15.4/23.3/26.7% | 1.9/4.9% | 3 |
| 0.5 | 1 | 0.878 | 0.872 | 0.006 | - | - | 0.978 | 0.979 | 0.691 | 1.10x | 11.7/18.7/21.2% | 1.6/4.2% | 3 |
| 0.75 | 1 | 0.868 | 0.853 | 0.015 | - | - | 0.984 | 0.988 | 0.605 | 0.91x | 10.9/15.2/18.1% | 1.5/3.6% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario ridge`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 0.25 | 1 | 0.887 | 0.877 | 0.009 | - | - | 0.984 | 0.986 | 0.703 | 1.23x | 15.1/22.9/26.2% | 1.9/4.8% | 3 |
| 0.5 | 1 | 0.874 | 0.865 | 0.009 | - | - | 0.987 | 0.988 | 0.709 | 1.10x | 12.1/19.1/21.4% | 1.8/4.3% | 3 |
| 0.75 | 1 | 0.866 | 0.852 | 0.014 | - | - | 0.977 | 0.978 | 0.577 | 0.87x | 10.5/14.8/17.6% | 1.4/3.5% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario ridge`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.904 | 0.896 | 0.008 | - | - | 0.991 | 0.992 | 0.731 | 0.77x | 8.9/14.2/16.2% | 1.2/3.0% | 3 |
| signing=true | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |

### `FW-versions` - profile  `--scenario ridge`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.910 | 0.905 | 0.005 | - | - | 0.991 | 0.991 | 0.752 | 0.83x | 9.8/13.1/15.4% | 1.4/2.3% | 3 |
| 2.5 | 1 | 0.911 | 0.907 | 0.004 | - | - | 0.992 | 0.992 | 0.745 | 0.85x | 9.8/13.2/15.5% | 1.4/2.3% | 3 |
| 2.6 | 1 | 0.915 | 0.911 | 0.004 | - | - | 0.993 | 0.993 | 0.756 | 0.82x | 9.9/13.2/15.6% | 1.3/2.3% | 3 |
| 2.7 | 1 | 0.928 | 0.925 | 0.003 | - | - | 0.992 | 0.992 | 0.783 | 0.85x | 10.8/15.2/18.3% | 1.3/3.1% | 3 |
| 2.8 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.886 | 0.875 | 0.011 | - | - | 0.984 | 0.987 | 0.653 | 0.96x | 10.7/16.5/18.8% | 1.5/3.5% | 3 |
| 900 | 1 | 0.805 | 0.784 | 0.020 | - | - | 0.966 | 0.967 | 0.599 | 2.27x | 25.5/38.2/43.9% | 3.4/8.2% | 3 |
| 300 | 1 | 0.534 | 0.512 | 0.022 | - | - | 0.733 | 0.812 | 0.311 | 4.61x | 49.0/68.1/75.5% | 6.8/15.7% | 3 |

> broadcast-interval-s=900: decode_failures 2

> broadcast-interval-s=300: decode_failures 31

### `LD-chatty-hops` - broadcast-interval-s  `--scenario ridge`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.941 | 0.939 | 0.002 | - | - | 0.990 | 0.991 | 0.742 | 1.11x | 12.5/17.8/20.2% | 1.7/3.6% | 3 |
| 900 | 1 | 0.886 | 0.879 | 0.007 | - | - | 0.967 | 0.967 | 0.706 | 2.60x | 29.2/41.1/46.7% | 3.9/8.5% | 3 |
| 300 | 1 | 0.590 | 0.571 | 0.019 | - | - | 0.759 | 0.811 | 0.408 | 5.21x | 54.2/70.7/77.7% | 8.0/16.2% | 3 |

> broadcast-interval-s=300: decode_failures 28

### `LD-diurnal` - diurnal  `--scenario ridge`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.882 | 0.870 | 0.012 | - | - | 0.987 | 0.989 | 0.680 | 1.34x | 15.0/23.1/26.3% | 2.0/4.9% | 3 |
| sinusoid | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.982 | 0.986 | 0.663 | 1.31x | 14.8/22.7/25.7% | 2.0/4.7% | 3 |
| commuter | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.805 | 0.784 | 0.020 | - | - | 0.966 | 0.967 | 0.599 | 2.27x | 25.5/38.2/43.9% | 3.4/8.2% | 3 |
| 3600 | 1 | 0.886 | 0.875 | 0.011 | - | - | 0.984 | 0.987 | 0.653 | 0.96x | 10.7/16.5/18.8% | 1.5/3.5% | 3 |
| 10800 | 1 | 0.906 | 0.899 | 0.007 | - | - | 0.989 | 0.989 | 0.716 | 0.66x | 7.2/11.1/12.5% | 1.0/2.3% | 3 |
| 43200 | 1 | 0.906 | 0.899 | 0.007 | - | - | 0.991 | 0.992 | 0.725 | 0.47x | 5.2/7.9/9.0% | 0.7/1.7% | 3 |

> broadcast-interval-s=900: decode_failures 2

### `LD-traceroute` - traceroute-per-hour  `--scenario ridge`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 0.25 | 1 | 0.859 | 0.846 | 0.013 | - | - | 0.975 | 0.981 | 0.658 | 1.51x | 16.9/26.0/29.8% | 2.2/5.5% | 3 |
| 1.0 | 1 | 0.847 | 0.832 | 0.015 | - | - | 0.975 | 0.982 | 0.627 | 1.68x | 18.8/28.9/33.1% | 2.5/6.2% | 3 |
| 4.0 | 1 | 0.809 | 0.788 | 0.021 | - | - | 0.965 | 0.968 | 0.590 | 2.07x | 23.6/36.4/41.8% | 3.0/7.9% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario ridge`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.669 | 0.664 | 0.004 | - | - | 0.775 | 0.833 | 0.396 | 5.59x | 53.9/75.6/79.3% | 4.0/12.5% | 3 |
| 1.0 | 1 | 0.611 | 0.607 | 0.004 | - | - | 0.726 | 0.789 | 0.364 | 6.00x | 57.0/76.3/79.8% | 4.3/13.1% | 3 |

> traceroute-per-hour=0.0: queue drops 19.3% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 97

> traceroute-per-hour=1.0: queue drops 25.5% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 95

### `MS-density` - nodes  `--scenario ridge`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.658 | 0.652 | 0.007 | - | - | 0.789 | 0.791 | 0.000 | 1.31x | 17.7/24.1/31.8% | 3.1/6.4% | 3 |
| 60 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 90 | 1 | 0.934 | 0.931 | 0.003 | - | - | 0.992 | 0.993 | 0.729 | 1.65x | 18.6/32.3/36.9% | 1.5/5.2% | 3 |
| 120 | 1 | 0.943 | 0.942 | 0.002 | - | - | 0.994 | 0.994 | 0.641 | 2.19x | 22.3/41.8/46.4% | 1.5/5.3% | 3 |
| 150 | 1 | 0.952 | 0.951 | 0.002 | - | - | 0.996 | 0.996 | 0.715 | 2.78x | 27.4/49.9/56.0% | 1.4/5.6% | 3 |

> nodes=150: decode_failures 8

### `MS-hopscale` - nodes  `--scenario ridge`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 120 | 1 | 0.734 | 0.725 | 0.009 | - | - | 0.886 | 0.966 | 0.197 | 2.24x | 14.6/27.5/33.1% | 1.6/5.3% | 3 |
| 250 | 1 | 0.484 | 0.473 | 0.011 | - | - | 0.712 | 0.789 | 0.133 | 4.98x | 16.2/37.0/51.0% | 1.6/6.5% | 3 |
| 500 | 1 | 0.284 | 0.280 | 0.003 | - | - | 0.398 | 0.399 | 0.088 | 9.64x | 16.7/31.9/45.6% | 1.6/5.3% | 3 |

> nodes=120: decode_failures 59

> nodes=250: decode_failures 137

> nodes=500: decode_failures 2

### `MS-oversubscribed` - nodes  `--scenario ridge`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.748 | 0.737 | 0.012 | - | - | 0.909 | 0.968 | 0.213 | 2.09x | 13.6/25.6/31.0% | 1.5/4.8% | 3 |
| 250 | 1 | 0.488 | 0.477 | 0.011 | - | - | 0.715 | 0.790 | 0.126 | 4.62x | 15.2/33.8/46.8% | 1.5/5.8% | 3 |
| 500 | 1 | 0.287 | 0.284 | 0.003 | - | - | 0.399 | 0.400 | 0.081 | 8.88x | 15.5/29.5/42.0% | 1.5/4.8% | 3 |

> nodes=120: decode_failures 37

> nodes=250: decode_failures 95

### `MS-roles` - role-mix  `--scenario ridge`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.864 | 0.853 | 0.011 | - | - | 0.975 | 0.977 | 0.624 | 1.43x | 16.0/24.8/28.2% | 2.1/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.819 | 0.794 | 0.025 | - | - | 0.944 | 0.956 | 0.479 | 1.24x | 14.1/22.8/27.3% | 2.2/5.1% | 3 |

> role-mix=baymesh-2026-08: decode_failures 21

> slower: 5.05 s per simulated hour against 1.7 over 47 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-roles-fav` - role-mix  `--scenario ridge`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.886 | 0.875 | 0.010 | - | - | 0.980 | 0.983 | 0.699 | 1.50x | 16.6/25.5/28.7% | 2.3/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.867 | 0.849 | 0.018 | - | - | 0.952 | 0.952 | 0.598 | 1.43x | 15.7/25.5/30.5% | 2.6/5.0% | 3 |

> role-mix=baymesh-2026-08: decode_failures 1

### `MS-router-late` - router-late-fraction  `--scenario ridge`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 0.05 | 1 | 0.868 | 0.855 | 0.014 | - | - | 0.975 | 0.981 | 0.641 | 1.53x | 16.3/27.2/33.1% | 2.2/5.1% | 3 |
| 0.1 | 1 | 0.870 | 0.859 | 0.012 | - | - | 0.979 | 0.980 | 0.644 | 1.63x | 17.1/29.9/35.5% | 2.2/5.4% | 3 |
| 0.2 | 1 | 0.886 | 0.877 | 0.009 | - | - | 0.987 | 0.988 | 0.637 | 1.79x | 19.5/33.7/36.9% | 2.4/5.2% | 3 |

### `MS-siting` - siting-mix  `--scenario ridge`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| local-typical | 1 | 0.661 | 0.652 | 0.009 | - | - | 0.858 | 0.863 | 0.000 | 1.54x | 14.6/21.5/28.3% | 2.4/5.9% | 3 |
| event | 1 | 0.238 | 0.231 | 0.008 | - | - | 0.459 | 0.466 | 0.000 | 1.40x | 7.1/22.1/33.8% | 1.8/5.4% | 3 |
| backbone | 1 | 0.979 | 0.979 | 0.000 | - | - | 0.998 | 0.998 | 0.927 | 1.13x | 31.1/39.2/40.4% | 1.5/5.5% | 3 |

> siting-mix=event: decode_failures 5

### `MS-size` - nodes  `--scenario ridge`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.787 | 0.779 | 0.008 | - | - | 0.912 | 0.916 | 0.242 | 1.38x | 22.1/29.1/33.7% | 3.1/7.3% | 3 |
| 60 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 90 | 1 | 0.760 | 0.751 | 0.009 | - | - | 0.910 | 0.911 | 0.447 | 1.58x | 12.3/23.5/27.5% | 1.4/4.8% | 3 |
| 120 | 1 | 0.734 | 0.725 | 0.009 | - | - | 0.886 | 0.966 | 0.197 | 2.24x | 14.6/27.5/33.1% | 1.6/5.3% | 3 |
| 150 | 1 | 0.643 | 0.634 | 0.009 | - | - | 0.929 | 0.929 | 0.000 | 2.90x | 14.2/33.2/41.2% | 1.6/6.1% | 3 |

> nodes=120: decode_failures 59

### `MS-stretch` - stretch  `--scenario ridge`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 1.25 | 1 | 0.640 | 0.630 | 0.010 | - | - | 0.896 | 0.900 | 0.290 | 1.38x | 11.0/20.1/22.6% | 2.0/5.0% | 3 |
| 1.5 | 1 | 0.327 | 0.319 | 0.008 | - | - | 0.576 | 0.600 | 0.026 | 1.32x | 8.8/15.0/17.9% | 2.0/4.7% | 3 |
| 2.0 | 1 | 0.078 | 0.078 | 0.000 | - | - | 0.165 | 0.170 | 0.000 | 0.65x | 2.8/5.0/6.2% | 1.0/1.9% | 3 |

> stretch=1.25: decode_failures 2

> stretch=1.5: decode_failures 1

### `MS-topology` - topology  `--scenario ridge`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| clustered | 1 | 0.900 | 0.900 | 0.001 | - | - | 0.952 | 0.952 | 0.461 | 1.12x | 25.5/34.6/36.3% | 1.4/5.4% | 3 |
| corridor | 1 | 0.394 | 0.394 | 0.001 | - | - | 0.405 | 0.405 | 0.027 | 1.51x | 17.4/22.9/26.2% | 2.4/6.1% | 3 |
| hub | 1 | 0.956 | 0.951 | 0.005 | - | - | 0.987 | 0.988 | 0.872 | 1.20x | 31.0/38.8/40.5% | 1.7/5.7% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario ridge`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.825 | 0.825 | 0.000 | - | - | 0.960 | 0.978 | 0.616 | 1.72x | 19.3/29.4/34.1% | 2.5/6.3% | 3 |
| True | 1 | 0.824 | 0.824 | 0.000 | - | - | 0.958 | 0.974 | 0.625 | 1.73x | 19.3/29.7/34.4% | 2.5/6.4% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario ridge`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.824 | 0.824 | 0.000 | - | - | 0.958 | 0.974 | 0.625 | 1.73x | 19.3/29.7/34.4% | 2.5/6.4% | 3 |
| m4-early-flood | 1 | 0.819 | 0.819 | 0.000 | - | - | 0.954 | 0.973 | 0.620 | 1.75x | 19.6/30.1/34.9% | 2.6/6.5% | 3 |

> dm-mode=m4-early-flood: decode_failures 1

### `PR-protocol` - protocol  `--scenario ridge`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.856 | 0.856 | 0.000 | - | - | 0 | 0.000 | 0.670 | 1.38x | 15.5/23.9/27.3% | 2.0/5.0% | 3 |
| chain | 1 | 0.843 | 0.837 | 0.005 | - | - | 0.904 | 0.978 | 0.625 | 1.65x | 18.6/28.3/32.4% | 2.5/5.9% | 3 |
| sr | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |

### `PR-repeats` - extra-repeats  `--scenario ridge`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| True | 1 | 0.862 | 0.850 | 0.013 | - | - | 0.974 | 0.978 | 0.676 | 1.46x | 16.4/24.9/28.7% | 2.2/5.3% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario ridge`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.943 | 0.942 | 0.002 | - | - | 0.994 | 0.994 | 0.641 | 2.19x | 22.3/41.8/46.4% | 1.5/5.3% | 3 |
| True | 1 | 0.945 | 0.944 | 0.002 | - | - | 0.994 | 0.994 | 0.656 | 2.20x | 22.2/41.5/46.0% | 1.5/5.2% | 3 |

> extra-repeats=True: misdecodes 1

### `RF-bw500` - preset  `--scenario ridge`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.081 | 0.080 | 0.001 | - | - | 0.186 | 0.190 | 0.000 | 0.03x | 0.1/0.3/0.4% | 0.0/0.1% | 3 |
| MEDIUM_TURBO | 1 | 0.406 | 0.384 | 0.022 | - | - | 0.762 | 0.820 | 0.028 | 0.25x | 1.6/2.9/3.7% | 0.4/1.0% | 3 |
| LONG_TURBO | 1 | 0.793 | 0.782 | 0.011 | - | - | 0.960 | 0.960 | 0.496 | 1.35x | 12.5/21.0/23.4% | 1.9/4.9% | 3 |

> preset=SHORT_TURBO: decode_failures 2

> preset=MEDIUM_TURBO: decode_failures 24

> slower: 3.95 s per simulated hour against 1.82 over 47 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-duct` - duct-per-hour  `--scenario ridge`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 0.25 | 1 | 0.882 | 0.867 | 0.015 | - | - | 0.981 | 0.983 | 0.719 | 1.32x | 18.6/26.4/29.8% | 1.9/5.3% | 3 |
| 1.0 | 1 | 0.945 | 0.936 | 0.009 | - | - | 0.995 | 0.996 | 0.863 | 0.91x | 24.1/30.0/31.7% | 1.1/5.0% | 3 |

### `RF-eu-presets` - preset  `--scenario ridge`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.253 | 0.248 | 0.004 | - | - | 0.582 | 0.620 | 0.028 | 0.12x | 0.6/1.4/2.0% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| LITE_FAST | 1 | 0.826 | 0.818 | 0.008 | - | - | 0.979 | 0.982 | 0.554 | 1.09x | 10.8/18.1/20.9% | 1.6/4.1% | 3 |
| NARROW_SLOW | 1 | 0.851 | 0.840 | 0.012 | - | - | 0.970 | 0.974 | 0.649 | 1.38x | 14.4/21.9/26.4% | 2.1/5.0% | 3 |

> preset=SHORT_FAST: decode_failures 11

### `RF-noise` - noise-profile  `--scenario ridge`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| temporal | 1 | 0.773 | 0.753 | 0.021 | - | - | 0.965 | 0.972 | 0.418 | 1.43x | 15.9/24.7/27.9% | 2.0/5.2% | 3 |
| transient | 1 | 0.856 | 0.841 | 0.015 | - | - | 0.979 | 0.980 | 0.627 | 1.43x | 16.1/24.4/27.9% | 2.1/5.2% | 3 |
| periodic | 1 | 0.699 | 0.686 | 0.013 | - | - | 0.815 | 0.827 | 0.495 | 1.32x | 15.1/22.6/26.0% | 2.0/4.6% | 3 |

> noise-profile=temporal: decode_failures 2

> noise-profile=periodic: decode_failures 1

### `RF-preset` - preset  `--scenario ridge`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.253 | 0.248 | 0.004 | - | - | 0.582 | 0.620 | 0.028 | 0.12x | 0.6/1.4/2.0% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| LONG_MODERATE | 1 | 0.837 | 0.824 | 0.012 | - | - | 0.941 | 0.956 | 0.727 | 3.61x | 46.9/63.2/67.1% | 5.7/12.7% | 3 |

> preset=SHORT_FAST: decode_failures 11

> preset=LONG_MODERATE: decode_failures 40

### `RF-preset-turbo` - preset  `--scenario ridge`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.029 | 0.029 | 0.000 | - | - | 0.038 | 0.043 | 0.000 | 0.01x | 0.0/0.0/0.0% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.081 | 0.080 | 0.001 | - | - | 0.186 | 0.190 | 0.000 | 0.03x | 0.1/0.3/0.4% | 0.0/0.1% | 3 |
| LONG_FAST | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| LONG_TURBO | 1 | 0.793 | 0.782 | 0.011 | - | - | 0.960 | 0.960 | 0.496 | 1.35x | 12.5/21.0/23.4% | 1.9/4.9% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.851 | 0.837 | 0.014 | - | - | 0.965 | 0.968 | 0.709 | 1.98x | 19.7/31.2/35.7% | 3.1/6.9% | 3 |

> preset=SHORT_TURBO: decode_failures 2

### `RF-pulse` - noise-pulse-interval-ms  `--scenario ridge`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.803 | 0.791 | 0.013 | - | - | 0.915 | 0.924 | 0.606 | 1.40x | 16.0/24.3/27.8% | 2.0/5.0% | 3 |
| 10000 | 1 | 0.699 | 0.686 | 0.013 | - | - | 0.815 | 0.827 | 0.495 | 1.32x | 15.1/22.6/26.0% | 2.0/4.6% | 3 |
| 4000 | 1 | 0.426 | 0.421 | 0.005 | - | - | 0.489 | 0.578 | 0.239 | 1.10x | 12.7/18.8/21.7% | 1.6/3.5% | 3 |
| 2000 | 1 | 0.089 | 0.089 | 0.000 | - | - | 0.100 | 0.173 | 0.032 | 0.71x | 8.4/12.6/14.7% | 1.1/2.0% | 3 |

> noise-pulse-interval-ms=10000: decode_failures 1

> noise-pulse-interval-ms=4000: decode_failures 5

### `RF-stretch-duct` - duct-per-hour  `--scenario ridge`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.327 | 0.319 | 0.008 | - | - | 0.576 | 0.600 | 0.026 | 1.32x | 8.8/15.0/17.9% | 2.0/4.7% | 3 |
| 1.0 | 1 | 0.708 | 0.684 | 0.024 | - | - | 0.838 | 0.838 | 0.516 | 0.85x | 15.1/20.4/22.4% | 1.2/4.3% | 3 |

> duct-per-hour=0.0: decode_failures 1

### `RF-txpower` - tx-power  `--scenario ridge`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 22 | 1 | 0.365 | 0.351 | 0.014 | - | - | 0.568 | 0.724 | 0.027 | 1.31x | 8.7/14.3/17.8% | 2.1/4.7% | 3 |
| 17 | 1 | 0.080 | 0.079 | 0.001 | - | - | 0.180 | 0.184 | 0.000 | 0.67x | 3.0/5.7/7.4% | 1.0/2.3% | 3 |
| 14 | 1 | 0.043 | 0.042 | 0.001 | - | - | 0.132 | 0.137 | 0.000 | 0.44x | 1.5/2.7/4.0% | 0.7/1.3% | 3 |

> tx-power=22: decode_failures 20

> tx-power=17: decode_failures 3

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario ridge`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.943 | 0.942 | 0.002 | - | - | 0.994 | 0.994 | 0.641 | 2.19x | 22.3/41.8/46.4% | 1.5/5.3% | 3 |
| True | 1 | 0.936 | 0.935 | 0.001 | - | - | 0.994 | 0.994 | 0.624 | 2.54x | 25.7/46.1/51.0% | 1.7/5.8% | 3 |

### `RT-favourites` - favourite-routers  `--scenario ridge`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.872 | 0.859 | 0.013 | - | - | 0.981 | 0.984 | 0.677 | 1.50x | 16.3/26.8/31.5% | 2.1/5.3% | 3 |
| True | 1 | 0.900 | 0.890 | 0.009 | - | - | 0.983 | 0.983 | 0.739 | 1.59x | 17.3/27.6/31.8% | 2.3/5.2% | 3 |

### `RT-hopassign` - hop-assign  `--scenario ridge`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| random | 1 | 0.839 | 0.824 | 0.015 | - | - | 0.970 | 0.973 | 0.594 | 1.40x | 15.8/23.7/27.3% | 2.1/5.0% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario ridge`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.733 | 0.692 | 0.040 | - | - | 0.950 | 0.959 | 0.387 | 1.06x | 12.2/20.0/23.5% | 1.5/4.6% | 3 |
| 7 | 1 | 0.923 | 0.919 | 0.005 | - | - | 0.986 | 0.986 | 0.716 | 1.64x | 18.5/26.6/30.3% | 2.5/5.4% | 3 |
| 15 | 1 | 0.941 | 0.940 | 0.002 | - | - | 0.987 | 0.987 | 0.700 | 1.68x | 18.9/26.9/30.4% | 2.6/5.4% | 3 |
| 32 | 1 | 0.940 | 0.937 | 0.002 | - | - | 0.983 | 0.983 | 0.729 | 1.67x | 18.7/26.8/30.2% | 2.6/5.4% | 3 |

> hop-limit=3: decode_failures 1

### `RT-hopspread` - hop-limit  `--scenario ridge`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.733 | 0.692 | 0.040 | - | - | 0.950 | 0.959 | 0.387 | 1.06x | 12.2/20.0/23.5% | 1.5/4.6% | 3 |
| 5 | 1 | 0.876 | 0.866 | 0.011 | - | - | 0.981 | 0.983 | 0.643 | 1.49x | 16.9/24.9/28.4% | 2.2/5.2% | 3 |
| 7 | 1 | 0.923 | 0.919 | 0.005 | - | - | 0.986 | 0.986 | 0.716 | 1.64x | 18.5/26.6/30.3% | 2.5/5.4% | 3 |

> hop-limit=3: decode_failures 1

### `RT-rebroadcast` - rebroadcast-mode  `--scenario ridge`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| KNOWN_ONLY | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.851 | 0.851 | 0.000 | - | - | 0.873 | 0.980 | 0.652 | 1.38x | 15.5/23.8/27.1% | 2.0/4.9% | 3 |

### `RT-spread` - hop-spread  `--scenario ridge`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.733 | 0.692 | 0.040 | - | - | 0.950 | 0.959 | 0.387 | 1.06x | 12.2/20.0/23.5% | 1.5/4.6% | 3 |
| True | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |

> hop-spread=False: decode_failures 1

### `SC-signing` - signature-policy  `--scenario ridge`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| BALANCED | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| STRICT | 1 | 0.752 | 0.752 | 0.000 | - | - | 0.882 | 0.888 | 0.510 | 1.56x | 17.4/26.6/30.5% | 2.4/5.6% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario ridge`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| dm | 1 | 0.868 | 0.853 | 0.015 | - | - | 0.982 | 0.983 | 0.641 | 1.39x | 15.6/24.0/27.6% | 2.1/5.2% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario ridge`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.863 | 0.851 | 0.012 | - | - | 0.976 | 0.981 | 0.651 | 1.45x | 16.3/24.7/28.4% | 2.2/5.2% | 3 |
| local | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| time | 1 | 0.857 | 0.845 | 0.011 | - | - | 0.968 | 0.970 | 0.633 | 1.49x | 16.7/25.4/29.1% | 2.2/5.4% | 3 |
| window | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.974 | 0.977 | 0.656 | 1.42x | 16.0/24.5/28.0% | 2.1/5.2% | 3 |

> bucket-mode=global: misdecodes 25

> bucket-mode=time: misdecodes 11

> bucket-mode=window: misdecodes 17

### `SF-bucket-time` - time-bucket-s  `--scenario ridge`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.851 | 0.837 | 0.014 | - | - | 0.976 | 0.980 | 0.653 | 1.59x | 17.8/26.8/30.7% | 2.4/5.8% | 3 |
| 1800 | 1 | 0.857 | 0.845 | 0.011 | - | - | 0.968 | 0.970 | 0.633 | 1.49x | 16.7/25.4/29.1% | 2.2/5.4% | 3 |
| 3600 | 1 | 0.862 | 0.850 | 0.012 | - | - | 0.974 | 0.982 | 0.662 | 1.43x | 16.1/24.7/28.2% | 2.1/5.2% | 3 |

> time-bucket-s=600: misdecodes 125

> time-bucket-s=1800: misdecodes 11

> time-bucket-s=3600: misdecodes 3

> time-bucket-s=3600: decode_failures 2

### `SF-cadence` - trigger  `--scenario ridge`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| interval | 1 | 0.836 | 0.820 | 0.015 | - | - | 0.955 | 0.970 | 0.609 | 1.93x | 21.3/32.2/36.5% | 2.8/7.1% | 3 |
| aimd | 1 | 0.853 | 0.848 | 0.004 | - | - | 0.906 | 0.987 | 0.660 | 1.46x | 16.3/25.2/28.8% | 2.2/5.3% | 3 |
| bucket+interval | 1 | 0.840 | 0.823 | 0.017 | - | - | 0.970 | 0.975 | 0.631 | 1.97x | 21.7/32.8/37.3% | 2.9/7.3% | 3 |

> trigger=interval: misdecodes 13

> trigger=interval: decode_failures 7

> trigger=aimd: misdecodes 2

> trigger=aimd: decode_failures 3

> trigger=bucket+interval: misdecodes 17

### `SF-capacity` - capacity  `--scenario ridge`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.862 | 0.849 | 0.013 | - | - | 0.968 | 0.978 | 0.638 | 1.44x | 16.1/24.7/28.2% | 2.1/5.3% | 3 |
| 8 | 1 | 0.864 | 0.852 | 0.012 | - | - | 0.971 | 0.977 | 0.638 | 1.42x | 15.9/24.5/28.1% | 2.1/5.3% | 3 |
| 16 | 1 | 0.860 | 0.847 | 0.013 | - | - | 0.978 | 0.978 | 0.637 | 1.44x | 16.2/24.9/28.5% | 2.1/5.3% | 3 |
| 32 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 50 | 1 | 0.855 | 0.840 | 0.015 | - | - | 0.974 | 0.979 | 0.642 | 1.43x | 16.1/24.7/28.3% | 2.1/5.3% | 3 |

> capacity=4: decode_failures 96

> capacity=8: decode_failures 84

> capacity=16: decode_failures 12

### `SF-capacity-local` - capacity  `--scenario ridge`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.862 | 0.849 | 0.013 | - | - | 0.968 | 0.978 | 0.638 | 1.44x | 16.1/24.7/28.2% | 2.1/5.3% | 3 |
| 8 | 1 | 0.864 | 0.852 | 0.012 | - | - | 0.971 | 0.977 | 0.638 | 1.42x | 15.9/24.5/28.1% | 2.1/5.3% | 3 |
| 16 | 1 | 0.860 | 0.847 | 0.013 | - | - | 0.978 | 0.978 | 0.637 | 1.44x | 16.2/24.9/28.5% | 2.1/5.3% | 3 |
| 32 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 50 | 1 | 0.855 | 0.840 | 0.015 | - | - | 0.974 | 0.979 | 0.642 | 1.43x | 16.1/24.7/28.3% | 2.1/5.3% | 3 |

> capacity=4: decode_failures 96

> capacity=8: decode_failures 84

> capacity=16: decode_failures 12

### `SF-capacity-window` - capacity  `--scenario ridge`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.863 | 0.857 | 0.007 | - | - | 0.945 | 0.980 | 0.653 | 1.40x | 15.8/24.3/27.7% | 2.1/5.1% | 3 |
| 16 | 1 | 0.862 | 0.850 | 0.013 | - | - | 0.976 | 0.980 | 0.644 | 1.41x | 15.9/24.4/27.9% | 2.1/5.1% | 3 |
| 32 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.974 | 0.977 | 0.656 | 1.42x | 16.0/24.5/28.0% | 2.1/5.2% | 3 |

> capacity=8: misdecodes 10

> capacity=8: decode_failures 66

> capacity=16: misdecodes 16

> capacity=16: decode_failures 4

> capacity=32: misdecodes 17

### `SF-catchup` - catch-up-hours  `--scenario ridge`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.840 | 0.823 | 0.017 | - | - | 0.970 | 0.975 | 0.631 | 1.97x | 21.7/32.8/37.3% | 2.9/7.3% | 3 |
| 02-06 | 1 | 0.862 | 0.854 | 0.008 | - | - | 0.930 | 0.981 | 0.655 | 1.47x | 16.4/25.3/28.9% | 2.2/5.4% | 3 |
| 00-08 | 1 | 0.858 | 0.850 | 0.008 | - | - | 0.931 | 0.977 | 0.643 | 1.55x | 17.3/26.4/30.2% | 2.3/5.7% | 3 |

> catch-up-hours=: misdecodes 17

> catch-up-hours=02-06: misdecodes 1

> catch-up-hours=02-06: decode_failures 34

> catch-up-hours=00-08: decode_failures 33

### `SF-hops-flat` - hops-apart  `--scenario ridge`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.858 | 0.854 | 0.004 | - | - | 0.980 | 0.980 | 0.654 | 1.42x | 15.9/24.6/28.1% | 2.1/5.2% | 3 |
| 2 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 3 | 1 | 0.865 | 0.844 | 0.021 | - | - | 0.984 | 0.987 | 0.669 | 1.44x | 16.3/24.9/28.4% | 2.1/5.3% | 3 |
| 4 | 1 | 0.870 | 0.849 | 0.021 | - | - | 0.943 | 0.971 | 0.642 | 1.44x | 16.2/24.7/28.3% | 2.1/5.3% | 3 |

> hops-apart=4: decode_failures 28

### `SF-hops-spread` - hops-apart  `--scenario ridge`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.858 | 0.854 | 0.004 | - | - | 0.980 | 0.980 | 0.654 | 1.42x | 15.9/24.6/28.1% | 2.1/5.2% | 3 |
| 2 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 3 | 1 | 0.865 | 0.844 | 0.021 | - | - | 0.984 | 0.987 | 0.669 | 1.44x | 16.3/24.9/28.4% | 2.1/5.3% | 3 |
| 4 | 1 | 0.870 | 0.849 | 0.021 | - | - | 0.943 | 0.971 | 0.642 | 1.44x | 16.2/24.7/28.3% | 2.1/5.3% | 3 |
| 5 | 1 | 0.863 | 0.847 | 0.016 | - | - | 0.944 | 0.981 | 0.656 | 1.43x | 16.0/24.6/28.1% | 2.1/5.3% | 3 |

> hops-apart=4: decode_failures 28

> hops-apart=5: decode_failures 20

### `SF-jitter-global` - advert-jitter-s  `--scenario ridge`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.863 | 0.849 | 0.014 | - | - | 0.984 | 0.984 | 0.620 | 1.42x | 15.9/24.3/27.9% | 2.1/5.2% | 3 |
| 30 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 120 | 1 | 0.872 | 0.859 | 0.013 | - | - | 0.983 | 0.983 | 0.667 | 1.43x | 16.1/24.7/28.2% | 2.1/5.2% | 3 |
| 600 | 1 | 0.864 | 0.852 | 0.013 | - | - | 0.983 | 0.983 | 0.649 | 1.44x | 16.2/24.6/28.3% | 2.1/5.2% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario ridge`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.863 | 0.849 | 0.014 | - | - | 0.984 | 0.984 | 0.620 | 1.42x | 15.9/24.3/27.9% | 2.1/5.2% | 3 |
| 30 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 120 | 1 | 0.872 | 0.859 | 0.013 | - | - | 0.983 | 0.983 | 0.667 | 1.43x | 16.1/24.7/28.2% | 2.1/5.2% | 3 |
| 600 | 1 | 0.864 | 0.852 | 0.013 | - | - | 0.983 | 0.983 | 0.649 | 1.44x | 16.2/24.6/28.3% | 2.1/5.2% | 3 |

### `SF-place-flat` - place  `--scenario ridge`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.889 | 0.851 | 0.038 | - | - | 0.971 | 0.982 | 0.654 | 1.43x | 16.0/24.5/28.0% | 2.1/5.1% | 3 |
| routers | 1 | 0.849 | 0.847 | 0.002 | - | - | 0.959 | 0.960 | 0.661 | 1.43x | 16.0/25.0/28.6% | 2.1/5.2% | 3 |
| alternate-routers | 1 | 0.850 | 0.848 | 0.002 | - | - | 0.959 | 0.960 | 0.669 | 1.43x | 16.0/24.7/28.2% | 2.1/5.2% | 3 |
| beside-router | 1 | 0.851 | 0.847 | 0.004 | - | - | 0.971 | 0.972 | 0.668 | 1.41x | 15.7/24.6/28.2% | 2.1/5.1% | 3 |
| random-clients | 1 | 0.864 | 0.853 | 0.010 | - | - | 0.963 | 0.967 | 0.645 | 1.44x | 16.1/24.8/28.4% | 2.1/5.1% | 3 |
| hops-apart | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |

> place=spread: decode_failures 1

### `SF-place-spread` - place  `--scenario ridge`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.889 | 0.851 | 0.038 | - | - | 0.971 | 0.982 | 0.654 | 1.43x | 16.0/24.5/28.0% | 2.1/5.1% | 3 |
| routers | 1 | 0.849 | 0.847 | 0.002 | - | - | 0.959 | 0.960 | 0.661 | 1.43x | 16.0/25.0/28.6% | 2.1/5.2% | 3 |
| alternate-routers | 1 | 0.850 | 0.848 | 0.002 | - | - | 0.959 | 0.960 | 0.669 | 1.43x | 16.0/24.7/28.2% | 2.1/5.2% | 3 |
| beside-router | 1 | 0.851 | 0.847 | 0.004 | - | - | 0.971 | 0.972 | 0.668 | 1.41x | 15.7/24.6/28.2% | 2.1/5.1% | 3 |
| random-clients | 1 | 0.864 | 0.853 | 0.010 | - | - | 0.963 | 0.967 | 0.645 | 1.44x | 16.1/24.8/28.4% | 2.1/5.1% | 3 |
| hops-apart | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |

> place=spread: decode_failures 1

### `SF-provide-transport` - provide-transport  `--scenario ridge`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| broadcast | 1 | 0.894 | 0.834 | 0.060 | - | - | 0.965 | 0.971 | 0.724 | 1.54x | 17.3/26.3/30.0% | 2.3/5.5% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario ridge`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| heard | 1 | 0.860 | 0.847 | 0.014 | - | - | 0.974 | 0.977 | 0.655 | 1.42x | 16.1/24.5/28.0% | 2.1/5.2% | 3 |

> replay-ordering=heard: misdecodes 18

### `SF-replay-order-broadcast` - replay-ordering  `--scenario ridge`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.894 | 0.834 | 0.060 | - | - | 0.965 | 0.971 | 0.724 | 1.54x | 17.3/26.3/30.0% | 2.3/5.5% | 3 |
| heard | 1 | 0.902 | 0.841 | 0.061 | - | - | 0.978 | 0.981 | 0.727 | 1.57x | 17.6/26.8/30.7% | 2.3/5.6% | 3 |

> replay-ordering=heard: misdecodes 3

### `SF-resolve` - resolve  `--scenario ridge`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| enum | 1 | 0.864 | 0.849 | 0.014 | - | - | 0.975 | 0.978 | 0.655 | 1.44x | 16.1/24.6/28.3% | 2.1/5.4% | 3 |
| hybrid | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |

### `SF-servers-allrouters` - servers  `--scenario ridge`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.849 | 0.847 | 0.002 | - | - | 0.959 | 0.960 | 0.661 | 1.43x | 16.0/25.0/28.6% | 2.1/5.2% | 3 |
| 6 | 1 | 0.848 | 0.841 | 0.007 | - | - | 0.970 | 0.970 | 0.638 | 1.47x | 16.4/25.6/29.2% | 2.2/5.4% | 6 |

### `SF-servers-flat` - servers  `--scenario ridge`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.856 | 0.852 | 0.004 | - | - | 0.971 | 0.973 | 0.644 | 1.41x | 15.7/24.4/27.9% | 2.1/5.1% | 2 |
| 3 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 5 | 1 | 0.866 | 0.850 | 0.016 | - | - | 0.984 | 0.985 | 0.652 | 1.45x | 16.5/24.9/28.4% | 2.1/5.3% | 5 |
| 8 | 1 | 0.859 | 0.834 | 0.024 | - | - | 0.982 | 0.983 | 0.669 | 1.50x | 17.1/25.6/29.2% | 2.2/5.5% | 8 |

### `SF-servers-spread` - servers  `--scenario ridge`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.856 | 0.852 | 0.004 | - | - | 0.971 | 0.973 | 0.644 | 1.41x | 15.7/24.4/27.9% | 2.1/5.1% | 2 |
| 3 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 5 | 1 | 0.866 | 0.850 | 0.016 | - | - | 0.984 | 0.985 | 0.652 | 1.45x | 16.5/24.9/28.4% | 2.1/5.3% | 5 |
| 8 | 1 | 0.859 | 0.834 | 0.024 | - | - | 0.982 | 0.983 | 0.669 | 1.50x | 17.1/25.6/29.2% | 2.2/5.5% | 8 |

### `SF-signed` - signed  `--scenario ridge`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| True | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario ridge`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.862 | 0.849 | 0.012 | - | - | 0.981 | 0.984 | 0.631 | 1.34x | 15.0/23.3/26.6% | 2.0/4.9% | 3 |
| 1 | 1 | 0.857 | 0.847 | 0.010 | - | - | 0.969 | 0.978 | 0.670 | 1.33x | 14.8/23.0/26.2% | 2.0/4.8% | 3 |
| 2 | 1 | 0.868 | 0.856 | 0.012 | - | - | 0.976 | 0.977 | 0.656 | 1.33x | 14.8/23.1/26.4% | 2.0/4.8% | 3 |
| 4 | 1 | 0.857 | 0.844 | 0.013 | - | - | 0.968 | 0.973 | 0.640 | 1.34x | 15.0/23.1/26.4% | 2.0/4.9% | 3 |

### `SF-width` - short-id-bits  `--scenario ridge`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.865 | 0.851 | 0.014 | - | - | 0.983 | 0.983 | 0.656 | 1.42x | 16.1/24.4/28.0% | 2.1/5.2% | 3 |
| 24 | 1 | 0.864 | 0.852 | 0.012 | - | - | 0.980 | 0.981 | 0.648 | 1.43x | 16.0/24.5/28.2% | 2.2/5.2% | 3 |
| 32 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.975 | 0.980 | 0.629 | 1.44x | 16.3/24.7/28.3% | 2.1/5.3% | 3 |
| 64 | 1 | 0.862 | 0.847 | 0.014 | - | - | 0.979 | 0.979 | 0.646 | 1.44x | 16.1/25.0/28.5% | 2.2/5.3% | 3 |

### `SF-window-size` - window-size  `--scenario ridge`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.853 | 0.839 | 0.014 | - | - | 0.974 | 0.977 | 0.645 | 1.52x | 17.0/26.0/29.8% | 2.3/5.5% | 3 |
| 16 | 1 | 0.870 | 0.858 | 0.012 | - | - | 0.982 | 0.985 | 0.665 | 1.45x | 16.2/24.9/28.5% | 2.2/5.3% | 3 |
| 32 | 1 | 0.865 | 0.852 | 0.013 | - | - | 0.974 | 0.977 | 0.656 | 1.42x | 16.0/24.5/28.0% | 2.1/5.2% | 3 |

> window-size=8: misdecodes 160

> window-size=16: misdecodes 54

> window-size=32: misdecodes 17

### `TH-congestion` - no-congestion-scaling  `--scenario ridge`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.943 | 0.942 | 0.002 | - | - | 0.994 | 0.994 | 0.641 | 2.19x | 22.3/41.8/46.4% | 1.5/5.3% | 3 |
| True | 1 | 0.699 | 0.693 | 0.006 | - | - | 0.818 | 0.860 | 0.415 | 5.42x | 52.5/75.1/79.1% | 3.9/12.2% | 3 |

> no-congestion-scaling=True: queue drops 16.8% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 116

### `TH-congestion-input` - congestion-input  `--scenario ridge`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.488 | 0.477 | 0.011 | - | - | 0.715 | 0.790 | 0.126 | 4.62x | 15.2/33.8/46.8% | 1.5/5.8% | 3 |
| truesize | 1 | 0.527 | 0.511 | 0.015 | - | - | 0.795 | 0.840 | 0.131 | 3.31x | 10.5/26.8/37.5% | 1.0/5.0% | 3 |

> congestion-input=hotstore: decode_failures 95

> congestion-input=truesize: decode_failures 74

> slower: 43.1 s per simulated hour against 10.5 over 47 prior run(s) - 4.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `TH-congestion-mode` - congestion-mode  `--scenario ridge`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.952 | 0.951 | 0.002 | - | - | 0.994 | 0.995 | 0.646 | 1.96x | 19.8/37.5/41.6% | 1.3/4.7% | 3 |
| adaptive | 1 | 0.943 | 0.942 | 0.002 | - | - | 0.994 | 0.994 | 0.641 | 2.19x | 22.3/41.8/46.4% | 1.5/5.3% | 3 |

> congestion-mode=static: misdecodes 1

