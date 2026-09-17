# Sweep blocks-2026-09-17-6492742

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** ridge
- **seed base** 6492742 · seeds 6492742
- **blocks** 86 run, 1 missing
- **compute** 11.1 h of simulator time across every cell
- **generated** 2026-09-17T09:05:58+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>92 warnings</summary>

- AD-siting: siting-mix=local-typical: decode_failures 14
- AD-worst: role-placement=degree: decode_failures 49
- AD-worst: role-placement=inverse: decode_failures 4
- AD-worst: slower: 7.83 s per simulated hour against 3.48 over 27 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- BL-control: protocol=sr: decode_failures 42
- BL-control: slower: 4.46 s per simulated hour against 1.7 over 27 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore: max-num-nodes=100: misdecodes 1
- DB-hotstore: max-num-nodes=120: misdecodes 1
- DB-hotstore: max-num-nodes=250: misdecodes 1
- DB-hotstore-stress: max-num-nodes=10: decode_failures 48
- DB-platform: platform-mix=uniform: misdecodes 1
- DB-platform: platform-mix=baymesh-2026-08: misdecodes 1
- DB-warm: warm-num-nodes=0: queue drops 27.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 88
- DB-warm: warm-num-nodes=25: queue drops 27.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 88
- DB-warm: warm-num-nodes=100: queue drops 27.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 88
- DB-warm: warm-num-nodes=2000: queue drops 27.1% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 88
- DG-burst: burst-loss=0.1: decode_failures 2
- DG-burst: burst-loss=0.2: decode_failures 24
- DG-burst: burst-loss=0.3: decode_failures 38
- DG-loss: extra-loss=0.3: decode_failures 6
- DG-outage: burst-loss=0.1: decode_failures 51
- DG-outage: burst-loss=0.2: decode_failures 38
- DG-outage: burst-loss=0.3: decode_failures 37
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 29
- LD-chatty: broadcast-interval-s=300: decode_failures 36
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 27.1% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 88
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 36.4% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 68
- MS-hopscale: nodes=120: decode_failures 72
- MS-hopscale: nodes=500: decode_failures 13
- MS-oversubscribed: nodes=120: decode_failures 45
- MS-oversubscribed: nodes=500: decode_failures 2
- MS-router-late: router-late-fraction=0.05: misdecodes 1
- MS-size: nodes=120: decode_failures 72
- MS-stretch: stretch=2.0: decode_failures 18
- MS-topology: topology=corridor: decode_failures 3
- RF-eu-presets: preset=SHORT_FAST: decode_failures 6
- RF-eu-presets: preset=LITE_FAST: decode_failures 26
- RF-eu-presets: slower: 4.1 s per simulated hour against 2.03 over 27 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-noise: noise-profile=temporal: decode_failures 1
- RF-noise: noise-profile=periodic: decode_failures 1
- RF-preset: preset=SHORT_FAST: decode_failures 6
- RF-preset: preset=LONG_MODERATE: decode_failures 9
- RF-pulse: noise-pulse-interval-ms=10000: decode_failures 1
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 9
- RF-txpower: tx-power=14: decode_failures 6
- RT-hoplimit: hop-limit=3: decode_failures 12
- RT-hopspread: hop-limit=3: decode_failures 12
- RT-spread: hop-spread=False: decode_failures 12
- SF-bucket-mode: bucket-mode=global: misdecodes 36
- SF-bucket-mode: bucket-mode=time: misdecodes 37
- SF-bucket-mode: bucket-mode=window: misdecodes 16
- SF-bucket-time: time-bucket-s=600: misdecodes 124
- SF-bucket-time: time-bucket-s=1800: misdecodes 37
- SF-bucket-time: time-bucket-s=3600: misdecodes 16
- SF-cadence: trigger=interval: misdecodes 15
- SF-cadence: trigger=interval: decode_failures 5
- SF-cadence: trigger=aimd: misdecodes 4
- SF-cadence: trigger=aimd: decode_failures 14
- SF-cadence: trigger=bucket+interval: misdecodes 20
- SF-capacity-local: capacity=4: decode_failures 98
- SF-capacity-local: capacity=8: decode_failures 46
- SF-capacity: capacity=4: decode_failures 98
- SF-capacity: capacity=8: decode_failures 46
- SF-capacity-window: capacity=8: misdecodes 19
- SF-capacity-window: capacity=8: decode_failures 31
- SF-capacity-window: capacity=16: misdecodes 17
- SF-capacity-window: capacity=16: decode_failures 1
- SF-capacity-window: capacity=32: misdecodes 16
- SF-catchup: catch-up-hours=: misdecodes 20
- SF-catchup: catch-up-hours=02-06: decode_failures 41
- SF-catchup: catch-up-hours=00-08: decode_failures 38
- SF-hops-flat: hops-apart=3: decode_failures 42
- SF-hops-spread: hops-apart=3: decode_failures 42
- SF-hops-spread: hops-apart=5: decode_failures 32
- SF-place-flat: place=spread: decode_failures 4
- SF-place-flat: place=random-clients: decode_failures 50
- SF-place-spread: place=spread: decode_failures 4
- SF-place-spread: place=random-clients: decode_failures 50
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 7
- SF-replay-order: replay-ordering=heard: misdecodes 11
- SF-window-size: window-size=8: misdecodes 146
- SF-window-size: window-size=16: misdecodes 52
- SF-window-size: window-size=32: misdecodes 16
- TH-congestion: no-congestion-scaling=True: queue drops 22.5% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: misdecodes 1
- TH-congestion: no-congestion-scaling=True: decode_failures 82

</details>

Blocks that produced no JSON (their job failed, timed out, or was cancelled): `MS-siting`

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `BL-control` | 4.46 | 1.7 | 2.63x | 27 |
| `AD-worst` | 7.83 | 3.48 | 2.25x | 27 |
| `RF-eu-presets` | 4.1 | 2.03 | 2.02x | 27 |
| `MS-size` | 6.26 | 3.39 | 1.84x | 27 |
| `FW-signing-cost` | 2.7 | 1.58 | 1.70x | 27 |
| `SF-place-spread` | 4.48 | 2.86 | 1.57x | 27 |
| `SF-place-flat` | 4.46 | 2.86 | 1.56x | 27 |
| `AD-siting` | 2.1 | 1.35 | 1.55x | 27 |
| `RF-bw500` | 1.26 | 1.88 | 0.67x | 27 |
| `RF-duct` | 1.1 | 1.76 | 0.63x | 27 |
| `AD-badrouters` | 1.32 | 2.17 | 0.61x | 27 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `RF-preset-turbo` | preset | **held** | 0.000 → 0.975 | 0.975 | 0.045 → 0.871 | 3.3x bytes_on_air | up | 5 |
| `PR-protocol` | protocol | **held** | 0 → 0.945 | 0.945 | 0.860 → 0.871 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.943 | 0.943 | 0.866 → 0.869 | 1x bytes_on_air | up | 2 |
| `RF-txpower` | tx-power | **held** | 0.099 → 0.945 | 0.847 | 0.092 → 0.871 | 21x sr_airtime | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.107 → 0.884 | 0.776 | 0.107 → 0.812 | 1.6e+02x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **text** | 0.080 → 0.835 | 0.755 | 0.077 → 0.824 | 5.4x sr_bytes | down | 3 |
| `MS-stretch` | stretch | **text** | 0.195 → 0.883 | 0.688 | 0.188 → 0.871 | 3.1x sr_airtime | down | 4 |
| `RF-bw500` | preset | **held** | 0.251 → 0.853 | 0.602 | 0.242 → 0.716 | 4.6x sr_airtime | up | 3 |
| `RF-eu-presets` | preset | **text** | 0.326 → 0.883 | 0.556 | 0.323 → 0.871 | 2.9x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.326 → 0.883 | 0.556 | 0.323 → 0.871 | 3.4x sr_airtime | up | 3 |
| `MS-hopscale` | nodes | **text** | 0.331 → 0.883 | 0.552 | 0.328 → 0.871 | 8.6x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **text** | 0.335 → 0.783 | 0.448 | 0.332 → 0.772 | 4.4x bytes_on_air | down | 3 |
| `MS-topology` | topology | **text** | 0.587 → 0.954 | 0.368 | 0.552 → 0.953 | 3.3x sr_bytes | up | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.597 → 0.938 | 0.341 | 0.576 → 0.934 | 8.9x sr_airtime | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.356 → 0.691 | 0.334 | 0.352 → 0.678 | 1.9x sr_airtime | up | 2 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.577 → 0.902 | 0.325 | 0.552 → 0.895 | 8.1x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.563 → 0.883 | 0.320 | 0.534 → 0.871 | 2.2x sr_bytes | down | 4 |
| `DG-burst` | burst-loss | **text** | 0.576 → 0.883 | 0.307 | 0.533 → 0.871 | 2.5x sr_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.570 → 0.842 | 0.272 | 0.338 → 0.556 | 5.4x sr_airtime | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.716 → 0.952 | 0.236 | 0.709 → 0.949 | 4.3x sr_airtime | down | 2 |
| `MS-size` | nodes | **text** | 0.696 → 0.890 | 0.194 | 0.684 → 0.884 | 7.6x sr_bytes | down | 5 |
| `RT-hoplimit` | hop-limit | **text** | 0.740 → 0.933 | 0.192 | 0.693 → 0.932 | 3x sr_bytes | up | 4 |
| `MS-density` | nodes | **text** | 0.795 → 0.975 | 0.179 | 0.785 → 0.974 | 5.8x sr_airtime | up | 5 |
| `RT-hopspread` | hop-limit | **text** | 0.740 → 0.917 | 0.177 | 0.693 → 0.911 | 2.4x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **text** | 0.712 → 0.883 | 0.170 | 0.702 → 0.871 | 1.6x sr_bytes | down | 4 |
| `RT-spread` | hop-spread | **text** | 0.740 → 0.883 | 0.143 | 0.693 → 0.871 | 2.2x sr_bytes | up | 2 |
| `SC-signing` | signature-policy | **text** | 0.748 → 0.883 | 0.135 | 0.748 → 0.871 | 1.3x sr_airtime | down | 3 |
| `DG-loss` | extra-loss | **text** | 0.766 → 0.883 | 0.117 | 0.744 → 0.871 | 1.6x sr_bytes | down | 4 |
| `DB-platform` | platform-mix | **text** | 0.806 → 0.906 | 0.101 | 0.794 → 0.901 | 2.3x sr_airtime | down | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.883 → 0.981 | 0.098 | 0.871 → 0.981 | 1.6x bytes_on_air | up | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.825 → 0.921 | 0.095 | 0.810 → 0.916 | 5.5x sr_airtime | up | 4 |
| `DB-hotstore` | max-num-nodes | **text** | 0.815 → 0.906 | 0.091 | 0.802 → 0.901 | 2.1x sr_airtime | up | 4 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.883 → 0.972 | 0.089 | 0.871 → 0.970 | 2.5x sr_bytes | up | 3 |
| `AD-flooding` | role-mix | **text** | 0.835 → 0.921 | 0.086 | 0.824 → 0.915 | 2.6x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.835 → 0.921 | 0.086 | 0.824 → 0.915 | 2.6x bytes_on_air | up | 3 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.871 → 0.945 | 0.075 | 0.864 → 0.871 | 30x sr_airtime | down | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.641 → 0.704 | 0.063 | 0.633 → 0.697 | 1.4x sr_airtime | down | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.821 → 0.883 | 0.062 | 0.804 → 0.871 | 1.5x sr_airtime | down | 4 |
| `SF-cadence` | trigger | **held** | 0.886 → 0.945 | 0.060 | 0.830 → 0.871 | 14x advert_bytes | down | 4 |
| `RT-hopassign` | hop-assign | **held** | 0.892 → 0.945 | 0.053 | 0.834 → 0.871 | 1.1x sr_bytes | down | 2 |
| `SF-place-flat` | place | **held** | 0.932 → 0.983 | 0.051 | 0.853 → 0.871 | 2.9x sr_bytes | down | 6 |
| `SF-place-spread` | place | **held** | 0.932 → 0.983 | 0.051 | 0.853 → 0.871 | 2.9x sr_bytes | down | 6 |
| `FW-versions` | profile | **held** | 0.945 → 0.994 | 0.048 | 0.871 → 0.923 | 3.3x bytes_on_air | down | 5 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.883 → 0.930 | 0.047 | 0.871 → 0.924 | 2.1x bytes_on_air | up | 4 |
| `FW-mixed` | legacy-fraction | **held** | 0.945 → 0.990 | 0.045 | 0.871 → 0.922 | 2.1x bytes_on_air | up | 4 |
| `SF-hops-flat` | hops-apart | **held** | 0.936 → 0.981 | 0.045 | 0.861 → 0.871 | 3.5x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.936 → 0.981 | 0.045 | 0.860 → 0.871 | 3.5x sr_bytes | up | 5 |
| `RF-duct` | duct-per-hour | **text** | 0.883 → 0.926 | 0.043 | 0.871 → 0.919 | 1.4x sr_bytes | up | 3 |
| `FW-firmware` | profile | **held** | 0.945 → 0.986 | 0.040 | 0.871 → 0.917 | 3.2x bytes_on_air | down | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.834 → 0.870 | 0.035 | 0.552 → 0.585 | 1.4x sr_airtime | up | 2 |
| `AD-worst` | role-placement | **text** | 0.767 → 0.800 | 0.033 | 0.752 → 0.792 | 1.1x sr_bytes | down | 2 |
| `AD-badrouters` | role-placement | **text** | 0.804 → 0.835 | 0.031 | 0.783 → 0.824 | 1.3x sr_bytes | down | 3 |
| `SF-sr-retries` | sr-retries | **held** | 0.940 → 0.970 | 0.031 | 0.872 → 0.879 | 1.3x sr_bytes | up | 4 |
| `MS-roles` | role-mix | **text** | 0.835 → 0.865 | 0.030 | 0.824 → 0.855 | 1.2x bytes_on_air | down | 2 |
| `SF-capacity-window` | capacity | **held** | 0.916 → 0.945 | 0.028 | 0.857 → 0.869 | 1.9x advert_bytes | up | 3 |
| `FW-signing-cost` | profile-flag | **text** | 0.883 → 0.911 | 0.028 | 0.871 → 0.905 | 3.3x bytes_on_air | down | 2 |
| `MS-roles-fav` | role-mix | **held** | 0.917 → 0.945 | 0.028 | 0.854 → 0.870 | 1.2x sr_bytes | down | 2 |
| `MS-router-late` | router-late-fraction | **held** | 0.927 → 0.954 | 0.027 | 0.859 → 0.880 | 1.3x bytes_on_air | up | 4 |
| `SF-catchup` | catch-up-hours | **text** | 0.850 → 0.872 | 0.022 | 0.832 → 0.866 | 9.3x advert_bytes | up | 3 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.855 → 0.876 | 0.021 | 0.841 → 0.864 | 5.5x advert_bytes | up | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.875 → 0.896 | 0.021 | 0.865 → 0.888 | 1.1x sr_bytes | up | 2 |
| `SF-servers-flat` | servers | **held** | 0.934 → 0.956 | 0.021 | 0.857 → 0.871 | 5.7x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.934 → 0.956 | 0.021 | 0.857 → 0.871 | 5.7x sr_bytes | up | 4 |
| `SF-window-size` | window-size | **held** | 0.927 → 0.945 | 0.017 | 0.851 → 0.869 | 5.7x advert_bytes | up | 3 |
| `SF-provide-transport` | provide-transport | **held** | 0.929 → 0.945 | 0.017 | 0.858 → 0.871 | 2.2x sr_airtime | down | 2 |
| `LD-diurnal` | diurnal | **held** | 0.945 → 0.962 | 0.016 | 0.871 → 0.889 | 1.3x sr_bytes | down | 3 |
| `DM-mode` | dm-mode | **text** | 0.822 → 0.836 | 0.015 | 0.822 → 0.836 | 1.4x sr_airtime | up | 3 |
| `SF-resolve` | resolve | **held** | 0.931 → 0.945 | 0.014 | 0.860 → 0.871 | 5.9x advert_bytes | = | 3 |
| `SF-width` | short-id-bits | **held** | 0.934 → 0.947 | 0.013 | 0.862 → 0.872 | 3x advert_bytes | down | 4 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.933 → 0.945 | 0.012 | 0.863 → 0.871 | 3.1x advert_bytes | up | 4 |
| `SF-replay-order` | replay-ordering | **text** | 0.871 → 0.883 | 0.012 | 0.861 → 0.871 | 1.1x sr_airtime | down | 2 |
| `SF-capacity` | capacity | **held** | 0.934 → 0.945 | 0.011 | 0.862 → 0.871 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.934 → 0.945 | 0.011 | 0.862 → 0.871 | 5.3x advert_bytes | up | 5 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.952 → 0.961 | 0.010 | 0.949 → 0.959 | 1.1x sr_bytes | down | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.902 → 0.911 | 0.009 | 0.836 → 0.836 | 1.4x sr_airtime | up | 2 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.944 → 0.953 | 0.009 | 0.864 → 0.872 | 1x sr_bytes | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.944 → 0.953 | 0.009 | 0.864 → 0.872 | 1x sr_bytes | up | 4 |
| `SF-servers-allrouters` | servers | **held** | 0.979 → 0.987 | 0.007 | 0.863 → 0.864 | 2.2x sr_bytes | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.946 → 0.952 | 0.006 | 0.941 → 0.949 | 1.1x sr_airtime | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.952 → 0.957 | 0.006 | 0.949 → 0.955 | 1.1x sr_bytes | up | 2 |
| `PR-repeats` | extra-repeats | **held** | 0.940 → 0.945 | 0.006 | 0.868 → 0.871 | 1x sr_airtime | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.879 → 0.884 | 0.006 | 0.851 → 0.858 | 1.1x sr_bytes | down | 2 |
| `SF-advert-transport` | advert-transport | **text** | 0.878 → 0.883 | 0.004 | 0.866 → 0.871 | 2.3x sr_airtime | down | 2 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.836 → 0.840 | 0.003 | 0.836 → 0.840 | 1.1x sr_airtime | up | 2 |

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
| none | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| sprinkled | 1 | 0.957 | 0.956 | 0.002 | - | - | 0.996 | 0.997 | 0.791 | 1.11x | 20.8/27.5/29.1% | 1.5/5.3% | 3 |
| arms-race | 1 | 0.981 | 0.981 | 0.000 | - | - | 1.000 | 1.000 | 0.943 | 0.78x | 23.1/28.3/29.3% | 0.7/5.4% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario ridge`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 0.1 | 1 | 0.917 | 0.912 | 0.005 | - | - | 0.994 | 0.996 | 0.653 | 1.12x | 19.7/24.1/27.3% | 1.7/4.4% | 3 |
| 0.3 | 1 | 0.972 | 0.970 | 0.002 | - | - | 0.998 | 0.998 | 0.896 | 0.89x | 21.5/27.9/29.9% | 1.0/5.1% | 3 |

### `AD-badrouters` - role-placement  `--scenario ridge`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.835 | 0.824 | 0.011 | - | - | 0.922 | 0.923 | 0.430 | 1.08x | 15.7/21.3/25.2% | 1.8/5.0% | 3 |
| inverse | 1 | 0.804 | 0.785 | 0.019 | - | - | 0.915 | 0.916 | 0.510 | 1.10x | 14.1/20.2/22.5% | 2.0/3.3% | 3 |
| random | 1 | 0.805 | 0.783 | 0.023 | - | - | 0.937 | 0.938 | 0.318 | 1.09x | 14.9/21.9/25.9% | 1.9/4.1% | 3 |

### `AD-flooding` - role-mix  `--scenario ridge`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.835 | 0.824 | 0.011 | - | - | 0.922 | 0.923 | 0.430 | 1.08x | 15.7/21.3/25.2% | 1.8/5.0% | 3 |
| all-routers | 1 | 0.921 | 0.915 | 0.006 | - | - | 0.966 | 0.966 | 0.821 | 2.78x | 33.7/44.8/46.8% | 4.5/5.1% | 3 |

### `AD-nomute` - role-mix  `--scenario ridge`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.835 | 0.824 | 0.011 | - | - | 0.922 | 0.923 | 0.430 | 1.08x | 15.7/21.3/25.2% | 1.8/5.0% | 3 |
| no-mute | 1 | 0.870 | 0.856 | 0.014 | - | - | 0.946 | 0.946 | 0.573 | 1.21x | 16.2/22.2/25.7% | 1.9/5.1% | 3 |
| all-routers | 1 | 0.921 | 0.915 | 0.006 | - | - | 0.966 | 0.966 | 0.821 | 2.78x | 33.7/44.8/46.8% | 4.5/5.1% | 3 |

### `AD-siting` - siting-mix  `--scenario ridge`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.835 | 0.824 | 0.011 | - | - | 0.922 | 0.923 | 0.430 | 1.08x | 15.7/21.3/25.2% | 1.8/5.0% | 3 |
| local-typical | 1 | 0.668 | 0.654 | 0.014 | - | - | 0.673 | 0.833 | 0.000 | 1.29x | 12.1/21.6/28.0% | 2.0/4.9% | 3 |
| basement-heavy | 1 | 0.080 | 0.077 | 0.002 | - | - | 0.220 | 0.228 | 0.000 | 0.56x | 1.8/5.4/11.2% | 0.4/2.8% | 3 |

> siting-mix=local-typical: decode_failures 14

### `AD-worst` - role-placement  `--scenario ridge`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.800 | 0.792 | 0.008 | - | - | 0.903 | 0.908 | 0.000 | 2.39x | 15.7/30.4/35.5% | 1.8/5.3% | 3 |
| inverse | 1 | 0.767 | 0.752 | 0.015 | - | - | 0.909 | 0.910 | 0.000 | 2.25x | 13.9/24.7/32.3% | 1.8/3.4% | 3 |

> role-placement=degree: decode_failures 49

> role-placement=inverse: decode_failures 4

> slower: 7.83 s per simulated hour against 3.48 over 27 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `BL-control` - protocol  `--scenario ridge`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.869 | 0.869 | 0.000 | - | - | 0 | 0.000 | 0.609 | 1.24x | 16.6/24.4/27.6% | 1.8/5.1% | 3 |
| sr | 1 | 0.888 | 0.866 | 0.022 | - | - | 0.943 | 0.975 | 0.614 | 1.30x | 17.1/25.3/28.7% | 1.9/5.3% | 3 |

> protocol=sr: decode_failures 42

> slower: 4.46 s per simulated hour against 1.7 over 27 prior run(s) - 2.6x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario ridge`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.815 | 0.802 | 0.013 | - | - | 0.902 | 0.906 | 0.579 | 2.91x | 38.3/57.1/61.7% | 4.2/9.6% | 3 |
| 100 | 1 | 0.906 | 0.901 | 0.005 | - | - | 0.959 | 0.960 | 0.673 | 1.48x | 20.0/31.0/34.0% | 2.0/5.1% | 3 |
| 120 | 1 | 0.906 | 0.901 | 0.005 | - | - | 0.959 | 0.960 | 0.673 | 1.48x | 20.0/31.0/34.0% | 2.0/5.1% | 3 |
| 250 | 1 | 0.906 | 0.901 | 0.005 | - | - | 0.959 | 0.960 | 0.673 | 1.48x | 20.0/31.0/34.0% | 2.0/5.1% | 3 |

> max-num-nodes=100: misdecodes 1

> max-num-nodes=120: misdecodes 1

> max-num-nodes=250: misdecodes 1

### `DB-hotstore-stress` - max-num-nodes  `--scenario ridge`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.344 | 0.338 | 0.006 | - | - | 0.570 | 0.592 | 0.135 | 11.68x | 42.9/60.3/72.3% | 4.1/10.2% | 3 |
| 120 | 1 | 0.560 | 0.552 | 0.009 | - | - | 0.834 | 0.834 | 0.232 | 4.55x | 17.0/28.7/39.2% | 1.5/5.4% | 3 |
| 250 | 1 | 0.564 | 0.556 | 0.008 | - | - | 0.842 | 0.843 | 0.223 | 4.39x | 16.4/27.8/38.1% | 1.5/5.2% | 3 |

> max-num-nodes=10: decode_failures 48

### `DB-platform` - platform-mix  `--scenario ridge`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.906 | 0.901 | 0.005 | - | - | 0.959 | 0.960 | 0.673 | 1.48x | 20.0/31.0/34.0% | 2.0/5.1% | 3 |
| baymesh-2026-08 | 1 | 0.906 | 0.901 | 0.005 | - | - | 0.959 | 0.960 | 0.673 | 1.48x | 20.0/31.0/34.0% | 2.0/5.1% | 3 |
| constrained | 1 | 0.806 | 0.794 | 0.012 | - | - | 0.886 | 0.887 | 0.588 | 2.91x | 38.4/57.3/61.7% | 4.2/9.6% | 3 |

> platform-mix=uniform: misdecodes 1

> platform-mix=baymesh-2026-08: misdecodes 1

### `DB-warm` - warm-num-nodes  `--scenario ridge`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.704 | 0.697 | 0.006 | - | - | 0.842 | 0.916 | 0.552 | 5.30x | 61.6/76.7/81.1% | 3.7/13.4% | 3 |
| 25 | 1 | 0.704 | 0.697 | 0.006 | - | - | 0.842 | 0.916 | 0.552 | 5.30x | 61.6/76.7/81.1% | 3.7/13.4% | 3 |
| 100 | 1 | 0.704 | 0.697 | 0.006 | - | - | 0.842 | 0.916 | 0.552 | 5.30x | 61.6/76.7/81.1% | 3.7/13.4% | 3 |
| 2000 | 1 | 0.704 | 0.697 | 0.006 | - | - | 0.842 | 0.916 | 0.552 | 5.30x | 61.6/76.7/81.1% | 3.7/13.4% | 3 |

> warm-num-nodes=0: queue drops 27.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 88

> warm-num-nodes=25: queue drops 27.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 88

> warm-num-nodes=100: queue drops 27.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 88

> warm-num-nodes=2000: queue drops 27.1% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 88

### `DG-burst` - burst-loss  `--scenario ridge`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 0.1 | 1 | 0.781 | 0.760 | 0.021 | - | - | 0.913 | 0.922 | 0.476 | 1.19x | 15.7/23.9/26.8% | 1.7/4.8% | 3 |
| 0.2 | 1 | 0.683 | 0.652 | 0.032 | - | - | 0.854 | 0.888 | 0.396 | 1.13x | 15.4/23.2/26.0% | 1.7/4.4% | 3 |
| 0.3 | 1 | 0.576 | 0.533 | 0.043 | - | - | 0.749 | 0.820 | 0.299 | 1.04x | 14.4/21.7/24.2% | 1.5/3.8% | 3 |

> burst-loss=0.1: decode_failures 2

> burst-loss=0.2: decode_failures 24

> burst-loss=0.3: decode_failures 38

### `DG-loss` - extra-loss  `--scenario ridge`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 0.1 | 1 | 0.844 | 0.828 | 0.016 | - | - | 0.928 | 0.931 | 0.575 | 1.33x | 17.7/26.2/29.0% | 2.0/5.1% | 3 |
| 0.2 | 1 | 0.818 | 0.802 | 0.016 | - | - | 0.905 | 0.912 | 0.509 | 1.38x | 18.8/27.3/30.3% | 2.0/5.1% | 3 |
| 0.3 | 1 | 0.766 | 0.744 | 0.021 | - | - | 0.876 | 0.903 | 0.424 | 1.40x | 19.0/27.9/30.9% | 2.1/4.9% | 3 |

> extra-loss=0.3: decode_failures 6

### `DG-outage` - burst-loss  `--scenario ridge`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 0.1 | 1 | 0.745 | 0.727 | 0.018 | - | - | 0.874 | 0.909 | 0.453 | 1.19x | 15.8/24.0/26.9% | 1.8/4.8% | 3 |
| 0.2 | 1 | 0.651 | 0.632 | 0.018 | - | - | 0.783 | 0.881 | 0.371 | 1.13x | 15.6/23.0/26.0% | 1.6/4.5% | 3 |
| 0.3 | 1 | 0.563 | 0.534 | 0.029 | - | - | 0.728 | 0.861 | 0.283 | 1.09x | 15.2/22.7/25.2% | 1.6/4.1% | 3 |

> burst-loss=0.1: decode_failures 51

> burst-loss=0.2: decode_failures 38

> burst-loss=0.3: decode_failures 37

### `DM-mode` - dm-mode  `--scenario ridge`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.822 | 0.822 | 0.000 | - | - | 0.897 | 0.899 | 0.579 | 1.65x | 21.5/32.4/36.8% | 2.5/6.8% | 3 |
| directed-with-late-flood | 1 | 0.836 | 0.836 | 0.000 | - | - | 0.902 | 0.908 | 0.600 | 1.52x | 20.0/30.2/34.0% | 2.3/6.1% | 3 |
| m4-early-flood | 1 | 0.825 | 0.825 | 0.000 | - | - | 0.897 | 0.902 | 0.585 | 1.57x | 20.4/31.1/35.1% | 2.3/6.4% | 3 |

### `FW-firmware` - profile  `--scenario ridge`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.920 | 0.917 | 0.004 | - | - | 0.986 | 0.986 | 0.641 | 0.71x | 10.2/12.2/13.1% | 1.2/2.0% | 3 |
| 2.8 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario ridge`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 0.25 | 1 | 0.926 | 0.922 | 0.004 | - | - | 0.990 | 0.991 | 0.679 | 1.18x | 16.6/22.7/25.6% | 1.7/4.8% | 3 |
| 0.5 | 1 | 0.898 | 0.889 | 0.009 | - | - | 0.974 | 0.975 | 0.705 | 0.96x | 13.3/18.7/20.4% | 1.5/4.1% | 3 |
| 0.75 | 1 | 0.921 | 0.914 | 0.007 | - | - | 0.984 | 0.984 | 0.638 | 0.85x | 12.6/15.5/17.6% | 1.4/2.9% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario ridge`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 0.25 | 1 | 0.921 | 0.918 | 0.004 | - | - | 0.987 | 0.988 | 0.694 | 1.14x | 16.1/22.5/25.2% | 1.7/4.8% | 3 |
| 0.5 | 1 | 0.902 | 0.894 | 0.007 | - | - | 0.983 | 0.985 | 0.671 | 0.94x | 13.0/18.4/20.3% | 1.5/4.0% | 3 |
| 0.75 | 1 | 0.930 | 0.924 | 0.006 | - | - | 0.989 | 0.990 | 0.652 | 0.84x | 12.9/15.8/18.0% | 1.4/3.0% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario ridge`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.911 | 0.905 | 0.006 | - | - | 0.963 | 0.965 | 0.670 | 0.68x | 9.4/14.2/16.1% | 1.0/3.0% | 3 |
| signing=true | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |

### `FW-versions` - profile  `--scenario ridge`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.913 | 0.910 | 0.003 | - | - | 0.985 | 0.987 | 0.638 | 0.70x | 10.8/13.0/14.8% | 1.0/2.4% | 3 |
| 2.5 | 1 | 0.918 | 0.916 | 0.002 | - | - | 0.993 | 0.993 | 0.639 | 0.72x | 10.8/13.0/14.9% | 1.1/2.4% | 3 |
| 2.6 | 1 | 0.920 | 0.918 | 0.002 | - | - | 0.994 | 0.994 | 0.643 | 0.68x | 10.7/12.9/14.9% | 1.0/2.5% | 3 |
| 2.7 | 1 | 0.925 | 0.923 | 0.002 | - | - | 0.990 | 0.990 | 0.647 | 0.70x | 11.0/13.7/16.2% | 0.9/3.1% | 3 |
| 2.8 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.961 | 0.961 | 0.643 | 0.84x | 11.0/16.5/18.6% | 1.3/3.4% | 3 |
| 900 | 1 | 0.825 | 0.810 | 0.016 | - | - | 0.891 | 0.893 | 0.565 | 1.97x | 26.0/38.1/43.1% | 3.0/7.9% | 3 |
| 300 | 1 | 0.577 | 0.552 | 0.025 | - | - | 0.701 | 0.740 | 0.411 | 4.39x | 53.5/72.3/76.9% | 6.6/15.4% | 3 |

> broadcast-interval-s=300: decode_failures 36

### `LD-chatty-hops` - broadcast-interval-s  `--scenario ridge`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.938 | 0.934 | 0.004 | - | - | 0.975 | 0.976 | 0.727 | 0.93x | 12.1/17.2/19.4% | 1.4/3.5% | 3 |
| 900 | 1 | 0.874 | 0.865 | 0.009 | - | - | 0.920 | 0.921 | 0.684 | 2.28x | 29.5/42.0/46.9% | 3.5/8.5% | 3 |
| 300 | 1 | 0.597 | 0.576 | 0.021 | - | - | 0.681 | 0.702 | 0.430 | 4.83x | 57.7/73.7/77.7% | 7.4/16.3% | 3 |

> broadcast-interval-s=300: decode_failures 29

### `LD-diurnal` - diurnal  `--scenario ridge`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.898 | 0.889 | 0.009 | - | - | 0.962 | 0.962 | 0.652 | 1.18x | 15.7/23.3/26.2% | 1.8/4.8% | 3 |
| sinusoid | 1 | 0.887 | 0.877 | 0.010 | - | - | 0.947 | 0.952 | 0.611 | 1.16x | 15.3/22.8/25.7% | 1.7/4.7% | 3 |
| commuter | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.825 | 0.810 | 0.016 | - | - | 0.891 | 0.893 | 0.565 | 1.97x | 26.0/38.1/43.1% | 3.0/7.9% | 3 |
| 3600 | 1 | 0.902 | 0.895 | 0.007 | - | - | 0.961 | 0.961 | 0.643 | 0.84x | 11.0/16.5/18.6% | 1.3/3.4% | 3 |
| 10800 | 1 | 0.916 | 0.910 | 0.006 | - | - | 0.971 | 0.971 | 0.645 | 0.59x | 7.6/11.6/12.9% | 0.9/2.4% | 3 |
| 43200 | 1 | 0.921 | 0.916 | 0.005 | - | - | 0.973 | 0.973 | 0.635 | 0.42x | 5.4/8.2/9.2% | 0.6/1.7% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario ridge`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 0.25 | 1 | 0.876 | 0.862 | 0.013 | - | - | 0.940 | 0.941 | 0.633 | 1.33x | 17.5/26.3/29.7% | 1.9/5.4% | 3 |
| 1.0 | 1 | 0.855 | 0.841 | 0.014 | - | - | 0.926 | 0.928 | 0.585 | 1.49x | 19.7/29.3/33.1% | 2.2/6.0% | 3 |
| 4.0 | 1 | 0.821 | 0.804 | 0.017 | - | - | 0.903 | 0.905 | 0.560 | 1.86x | 24.9/37.1/42.1% | 2.7/7.7% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario ridge`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.704 | 0.697 | 0.006 | - | - | 0.842 | 0.916 | 0.552 | 5.30x | 61.6/76.7/81.1% | 3.7/13.4% | 3 |
| 1.0 | 1 | 0.641 | 0.633 | 0.007 | - | - | 0.796 | 0.880 | 0.499 | 5.66x | 64.0/77.7/81.3% | 4.1/14.2% | 3 |

> traceroute-per-hour=0.0: queue drops 27.1% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 88

> traceroute-per-hour=1.0: queue drops 36.4% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 68

### `MS-density` - nodes  `--scenario ridge`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.795 | 0.785 | 0.010 | - | - | 0.908 | 0.908 | 0.471 | 1.50x | 21.0/30.6/34.0% | 3.5/7.4% | 3 |
| 60 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 90 | 1 | 0.954 | 0.952 | 0.002 | - | - | 0.995 | 0.995 | 0.747 | 1.50x | 19.9/28.0/31.6% | 1.3/4.8% | 3 |
| 120 | 1 | 0.952 | 0.949 | 0.003 | - | - | 0.999 | 0.999 | 0.840 | 1.99x | 23.9/43.1/47.4% | 1.3/5.3% | 3 |
| 150 | 1 | 0.975 | 0.974 | 0.001 | - | - | 0.998 | 0.998 | 0.854 | 2.53x | 29.9/46.3/51.0% | 1.2/5.8% | 3 |

### `MS-hopscale` - nodes  `--scenario ridge`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 120 | 1 | 0.773 | 0.760 | 0.013 | - | - | 0.914 | 0.918 | 0.390 | 2.28x | 16.2/31.5/40.1% | 1.6/5.1% | 3 |
| 250 | 1 | 0.554 | 0.544 | 0.010 | - | - | 0.822 | 0.822 | 0.233 | 5.03x | 18.8/31.8/42.9% | 1.7/6.0% | 3 |
| 500 | 1 | 0.331 | 0.328 | 0.003 | - | - | 0.493 | 0.493 | 0.132 | 10.13x | 20.5/31.0/47.3% | 1.7/6.3% | 3 |

> nodes=120: decode_failures 72

> nodes=500: decode_failures 13

### `MS-oversubscribed` - nodes  `--scenario ridge`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.783 | 0.772 | 0.011 | - | - | 0.892 | 0.913 | 0.431 | 2.13x | 15.3/29.3/37.1% | 1.5/4.8% | 3 |
| 250 | 1 | 0.560 | 0.552 | 0.009 | - | - | 0.834 | 0.834 | 0.232 | 4.55x | 17.0/28.7/39.2% | 1.5/5.4% | 3 |
| 500 | 1 | 0.335 | 0.332 | 0.004 | - | - | 0.494 | 0.494 | 0.138 | 9.34x | 18.9/28.6/43.8% | 1.6/5.7% | 3 |

> nodes=120: decode_failures 45

> nodes=500: decode_failures 2

### `MS-roles` - role-mix  `--scenario ridge`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.865 | 0.855 | 0.011 | - | - | 0.934 | 0.937 | 0.582 | 1.25x | 16.6/24.7/27.9% | 1.8/5.1% | 3 |
| baymesh-2026-08 | 1 | 0.835 | 0.824 | 0.011 | - | - | 0.922 | 0.923 | 0.430 | 1.08x | 15.7/21.3/25.2% | 1.8/5.0% | 3 |

### `MS-roles-fav` - role-mix  `--scenario ridge`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.880 | 0.870 | 0.010 | - | - | 0.945 | 0.945 | 0.605 | 1.28x | 16.8/24.8/27.8% | 1.9/5.0% | 3 |
| baymesh-2026-08 | 1 | 0.861 | 0.854 | 0.007 | - | - | 0.917 | 0.918 | 0.479 | 1.23x | 17.3/25.7/28.8% | 2.0/4.9% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario ridge`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 0.05 | 1 | 0.870 | 0.859 | 0.010 | - | - | 0.927 | 0.928 | 0.610 | 1.34x | 17.0/28.6/31.3% | 1.9/4.9% | 3 |
| 0.1 | 1 | 0.887 | 0.875 | 0.011 | - | - | 0.950 | 0.951 | 0.611 | 1.49x | 19.9/32.6/36.2% | 2.0/5.0% | 3 |
| 0.2 | 1 | 0.888 | 0.880 | 0.009 | - | - | 0.954 | 0.955 | 0.622 | 1.68x | 23.2/36.3/39.6% | 2.2/5.1% | 3 |

> router-late-fraction=0.05: misdecodes 1

### `MS-size` - nodes  `--scenario ridge`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.887 | 0.884 | 0.003 | - | - | 0.950 | 0.952 | 0.701 | 1.46x | 29.0/40.0/42.7% | 3.2/8.1% | 3 |
| 60 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 90 | 1 | 0.890 | 0.882 | 0.007 | - | - | 0.990 | 0.992 | 0.558 | 1.68x | 15.9/26.0/31.7% | 1.5/4.7% | 3 |
| 120 | 1 | 0.773 | 0.760 | 0.013 | - | - | 0.914 | 0.918 | 0.390 | 2.28x | 16.2/31.5/40.1% | 1.6/5.1% | 3 |
| 150 | 1 | 0.696 | 0.684 | 0.012 | - | - | 0.855 | 0.857 | 0.326 | 2.72x | 15.8/34.0/40.0% | 1.5/5.4% | 3 |

> nodes=120: decode_failures 72

### `MS-stretch` - stretch  `--scenario ridge`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 1.25 | 1 | 0.565 | 0.554 | 0.011 | - | - | 0.788 | 0.789 | 0.170 | 1.36x | 13.5/19.5/22.8% | 1.9/5.2% | 3 |
| 1.5 | 1 | 0.356 | 0.352 | 0.004 | - | - | 0.530 | 0.533 | 0.000 | 1.67x | 12.2/20.9/22.7% | 2.6/6.1% | 3 |
| 2.0 | 1 | 0.195 | 0.188 | 0.007 | - | - | 0.382 | 0.437 | 0.000 | 1.12x | 6.0/10.6/14.5% | 1.6/4.6% | 3 |

> stretch=2.0: decode_failures 18

### `MS-topology` - topology  `--scenario ridge`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| clustered | 1 | 0.940 | 0.939 | 0.000 | - | - | 1.000 | 1.000 | 0.000 | 1.09x | 32.2/39.2/40.7% | 1.1/5.6% | 3 |
| corridor | 1 | 0.587 | 0.552 | 0.035 | - | - | 0.877 | 0.882 | 0.272 | 1.36x | 14.9/24.1/26.1% | 2.1/5.6% | 3 |
| hub | 1 | 0.954 | 0.953 | 0.001 | - | - | 0.986 | 0.987 | 0.637 | 1.09x | 27.1/36.3/37.5% | 1.5/5.5% | 3 |

> topology=corridor: decode_failures 3

### `PR-crladder` - coding-rate-ladder  `--scenario ridge`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.836 | 0.836 | 0.000 | - | - | 0.902 | 0.908 | 0.600 | 1.52x | 20.0/30.2/34.0% | 2.3/6.1% | 3 |
| True | 1 | 0.836 | 0.836 | 0.000 | - | - | 0.911 | 0.912 | 0.608 | 1.55x | 20.3/30.5/34.7% | 2.3/6.5% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario ridge`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.836 | 0.836 | 0.000 | - | - | 0.911 | 0.912 | 0.608 | 1.55x | 20.3/30.5/34.7% | 2.3/6.5% | 3 |
| m4-early-flood | 1 | 0.840 | 0.840 | 0.000 | - | - | 0.913 | 0.917 | 0.606 | 1.54x | 20.4/30.3/34.4% | 2.3/6.4% | 3 |

### `PR-protocol` - protocol  `--scenario ridge`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.869 | 0.869 | 0.000 | - | - | 0 | 0.000 | 0.609 | 1.24x | 16.6/24.4/27.6% | 1.8/5.1% | 3 |
| chain | 1 | 0.862 | 0.860 | 0.002 | - | - | 0.872 | 0.943 | 0.616 | 1.46x | 19.4/28.7/32.4% | 2.2/5.9% | 3 |
| sr | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |

### `PR-repeats` - extra-repeats  `--scenario ridge`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| True | 1 | 0.881 | 0.868 | 0.013 | - | - | 0.940 | 0.940 | 0.640 | 1.27x | 16.8/25.0/28.1% | 1.9/5.2% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario ridge`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.952 | 0.949 | 0.003 | - | - | 0.999 | 0.999 | 0.840 | 1.99x | 23.9/43.1/47.4% | 1.3/5.3% | 3 |
| True | 1 | 0.957 | 0.955 | 0.002 | - | - | 0.999 | 0.999 | 0.862 | 2.01x | 24.0/43.3/47.7% | 1.3/5.2% | 3 |

### `RF-bw500` - preset  `--scenario ridge`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.244 | 0.242 | 0.002 | - | - | 0.251 | 0.255 | 0.000 | 0.06x | 0.3/0.6/0.9% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.418 | 0.414 | 0.004 | - | - | 0.613 | 0.613 | 0.000 | 0.28x | 2.0/4.0/4.3% | 0.4/1.1% | 3 |
| LONG_TURBO | 1 | 0.724 | 0.716 | 0.007 | - | - | 0.853 | 0.856 | 0.391 | 1.14x | 12.2/17.9/20.9% | 1.7/4.7% | 3 |

### `RF-duct` - duct-per-hour  `--scenario ridge`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 0.25 | 1 | 0.886 | 0.875 | 0.011 | - | - | 0.940 | 0.941 | 0.662 | 1.19x | 19.1/26.7/29.6% | 1.7/5.3% | 3 |
| 1.0 | 1 | 0.926 | 0.919 | 0.007 | - | - | 0.954 | 0.957 | 0.805 | 0.97x | 24.8/31.1/33.1% | 1.2/5.5% | 3 |

### `RF-eu-presets` - preset  `--scenario ridge`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.326 | 0.323 | 0.003 | - | - | 0.487 | 0.533 | 0.000 | 0.15x | 1.0/1.8/2.2% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| LITE_FAST | 1 | 0.774 | 0.758 | 0.016 | - | - | 0.933 | 0.981 | 0.392 | 0.92x | 10.9/16.4/19.8% | 1.2/4.0% | 3 |
| NARROW_SLOW | 1 | 0.827 | 0.816 | 0.011 | - | - | 0.927 | 0.932 | 0.456 | 1.19x | 14.8/21.2/24.9% | 1.6/5.1% | 3 |

> preset=SHORT_FAST: decode_failures 6

> preset=LITE_FAST: decode_failures 26

> slower: 4.1 s per simulated hour against 2.03 over 27 prior run(s) - 2.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-noise` - noise-profile  `--scenario ridge`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| temporal | 1 | 0.764 | 0.744 | 0.021 | - | - | 0.874 | 0.882 | 0.351 | 1.26x | 15.9/24.8/27.4% | 1.7/5.1% | 3 |
| transient | 1 | 0.863 | 0.849 | 0.014 | - | - | 0.929 | 0.932 | 0.601 | 1.23x | 16.4/24.3/27.4% | 1.8/5.0% | 3 |
| periodic | 1 | 0.712 | 0.702 | 0.011 | - | - | 0.780 | 0.785 | 0.465 | 1.15x | 15.4/22.9/25.7% | 1.7/4.4% | 3 |

> noise-profile=temporal: decode_failures 1

> noise-profile=periodic: decode_failures 1

### `RF-preset` - preset  `--scenario ridge`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.326 | 0.323 | 0.003 | - | - | 0.487 | 0.533 | 0.000 | 0.15x | 1.0/1.8/2.2% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| LONG_MODERATE | 1 | 0.816 | 0.805 | 0.011 | - | - | 0.905 | 0.915 | 0.575 | 3.21x | 51.5/59.8/67.1% | 4.6/12.8% | 3 |

> preset=SHORT_FAST: decode_failures 6

> preset=LONG_MODERATE: decode_failures 9

### `RF-preset-turbo` - preset  `--scenario ridge`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.045 | 0.045 | 0.000 | - | - | 0.000 | 0.000 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.244 | 0.242 | 0.002 | - | - | 0.251 | 0.255 | 0.000 | 0.06x | 0.3/0.6/0.9% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| LONG_TURBO | 1 | 0.724 | 0.716 | 0.007 | - | - | 0.853 | 0.856 | 0.391 | 1.14x | 12.2/17.9/20.9% | 1.7/4.7% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.871 | 0.856 | 0.015 | - | - | 0.975 | 0.981 | 0.735 | 1.71x | 21.3/30.5/33.7% | 2.7/6.8% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario ridge`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.825 | 0.812 | 0.012 | - | - | 0.884 | 0.884 | 0.577 | 1.23x | 16.5/24.4/27.5% | 1.8/4.9% | 3 |
| 10000 | 1 | 0.712 | 0.702 | 0.011 | - | - | 0.780 | 0.785 | 0.465 | 1.15x | 15.4/22.9/25.7% | 1.7/4.4% | 3 |
| 4000 | 1 | 0.466 | 0.460 | 0.006 | - | - | 0.509 | 0.562 | 0.236 | 1.05x | 14.3/20.9/23.3% | 1.5/3.5% | 3 |
| 2000 | 1 | 0.107 | 0.107 | 0.000 | - | - | 0.107 | 0.184 | 0.045 | 0.73x | 10.7/14.7/16.5% | 1.1/2.0% | 3 |

> noise-pulse-interval-ms=10000: decode_failures 1

> noise-pulse-interval-ms=4000: decode_failures 9

### `RF-stretch-duct` - duct-per-hour  `--scenario ridge`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.356 | 0.352 | 0.004 | - | - | 0.530 | 0.533 | 0.000 | 1.67x | 12.2/20.9/22.7% | 2.6/6.1% | 3 |
| 1.0 | 1 | 0.691 | 0.678 | 0.012 | - | - | 0.765 | 0.768 | 0.478 | 1.00x | 18.0/22.2/24.6% | 1.4/5.0% | 3 |

### `RF-txpower` - tx-power  `--scenario ridge`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 22 | 1 | 0.367 | 0.362 | 0.005 | - | - | 0.561 | 0.562 | 0.000 | 1.67x | 12.3/20.8/22.7% | 2.6/6.1% | 3 |
| 17 | 1 | 0.215 | 0.212 | 0.002 | - | - | 0.243 | 0.247 | 0.000 | 1.19x | 6.6/12.0/16.1% | 1.8/4.7% | 3 |
| 14 | 1 | 0.092 | 0.092 | 0.000 | - | - | 0.099 | 0.173 | 0.000 | 0.69x | 2.9/5.9/9.8% | 0.9/3.0% | 3 |

> tx-power=14: decode_failures 6

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario ridge`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.952 | 0.949 | 0.003 | - | - | 0.999 | 0.999 | 0.840 | 1.99x | 23.9/43.1/47.4% | 1.3/5.3% | 3 |
| True | 1 | 0.946 | 0.941 | 0.004 | - | - | 0.998 | 0.999 | 0.838 | 2.28x | 26.6/47.3/52.0% | 1.5/5.7% | 3 |

### `RT-favourites` - favourite-routers  `--scenario ridge`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.875 | 0.865 | 0.010 | - | - | 0.932 | 0.934 | 0.614 | 1.32x | 17.0/27.6/30.2% | 1.9/5.1% | 3 |
| True | 1 | 0.896 | 0.888 | 0.007 | - | - | 0.942 | 0.942 | 0.644 | 1.41x | 18.2/28.7/31.4% | 2.0/5.1% | 3 |

### `RT-hopassign` - hop-assign  `--scenario ridge`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| random | 1 | 0.849 | 0.834 | 0.015 | - | - | 0.892 | 0.893 | 0.579 | 1.22x | 16.3/23.9/27.2% | 1.8/5.0% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario ridge`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.740 | 0.693 | 0.048 | - | - | 0.865 | 0.886 | 0.241 | 0.94x | 12.7/20.2/23.5% | 1.2/4.4% | 3 |
| 7 | 1 | 0.917 | 0.911 | 0.006 | - | - | 0.956 | 0.957 | 0.693 | 1.39x | 18.4/26.1/29.5% | 2.1/5.3% | 3 |
| 15 | 1 | 0.933 | 0.932 | 0.001 | - | - | 0.962 | 0.963 | 0.732 | 1.40x | 18.5/25.9/29.2% | 2.2/5.2% | 3 |
| 32 | 1 | 0.932 | 0.930 | 0.002 | - | - | 0.965 | 0.966 | 0.724 | 1.42x | 18.9/26.1/29.5% | 2.2/5.3% | 3 |

> hop-limit=3: decode_failures 12

### `RT-hopspread` - hop-limit  `--scenario ridge`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.740 | 0.693 | 0.048 | - | - | 0.865 | 0.886 | 0.241 | 0.94x | 12.7/20.2/23.5% | 1.2/4.4% | 3 |
| 5 | 1 | 0.876 | 0.863 | 0.013 | - | - | 0.938 | 0.942 | 0.576 | 1.27x | 16.9/25.0/28.2% | 1.9/5.2% | 3 |
| 7 | 1 | 0.917 | 0.911 | 0.006 | - | - | 0.956 | 0.957 | 0.693 | 1.39x | 18.4/26.1/29.5% | 2.1/5.3% | 3 |

> hop-limit=3: decode_failures 12

### `RT-rebroadcast` - rebroadcast-mode  `--scenario ridge`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| KNOWN_ONLY | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.864 | 0.864 | 0.000 | - | - | 0.871 | 0.934 | 0.587 | 1.23x | 16.5/24.2/27.5% | 1.8/5.0% | 3 |

### `RT-spread` - hop-spread  `--scenario ridge`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.740 | 0.693 | 0.048 | - | - | 0.865 | 0.886 | 0.241 | 0.94x | 12.7/20.2/23.5% | 1.2/4.4% | 3 |
| True | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |

> hop-spread=False: decode_failures 12

### `SC-signing` - signature-policy  `--scenario ridge`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| BALANCED | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| STRICT | 1 | 0.748 | 0.748 | 0.000 | - | - | 0.825 | 0.828 | 0.516 | 1.36x | 17.8/26.5/29.8% | 2.1/5.4% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario ridge`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| dm | 1 | 0.878 | 0.866 | 0.013 | - | - | 0.947 | 0.948 | 0.594 | 1.28x | 16.8/25.4/28.6% | 1.9/5.3% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario ridge`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.874 | 0.863 | 0.011 | - | - | 0.933 | 0.934 | 0.606 | 1.28x | 17.0/25.4/28.4% | 1.9/5.2% | 3 |
| local | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| time | 1 | 0.876 | 0.864 | 0.013 | - | - | 0.941 | 0.941 | 0.618 | 1.29x | 16.9/25.5/28.7% | 1.9/5.3% | 3 |
| window | 1 | 0.880 | 0.869 | 0.011 | - | - | 0.945 | 0.948 | 0.611 | 1.25x | 16.7/24.7/27.8% | 1.9/5.1% | 3 |

> bucket-mode=global: misdecodes 36

> bucket-mode=time: misdecodes 37

> bucket-mode=window: misdecodes 16

### `SF-bucket-time` - time-bucket-s  `--scenario ridge`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.855 | 0.841 | 0.014 | - | - | 0.923 | 0.924 | 0.591 | 1.44x | 18.6/28.2/31.5% | 2.1/5.9% | 3 |
| 1800 | 1 | 0.876 | 0.864 | 0.013 | - | - | 0.941 | 0.941 | 0.618 | 1.29x | 16.9/25.5/28.7% | 1.9/5.3% | 3 |
| 3600 | 1 | 0.876 | 0.864 | 0.012 | - | - | 0.932 | 0.939 | 0.613 | 1.27x | 16.7/25.0/28.1% | 1.9/5.2% | 3 |

> time-bucket-s=600: misdecodes 124

> time-bucket-s=1800: misdecodes 37

> time-bucket-s=3600: misdecodes 16

### `SF-cadence` - trigger  `--scenario ridge`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| interval | 1 | 0.847 | 0.830 | 0.018 | - | - | 0.908 | 0.913 | 0.604 | 1.74x | 21.4/34.6/38.3% | 2.5/7.3% | 3 |
| aimd | 1 | 0.866 | 0.863 | 0.003 | - | - | 0.886 | 0.934 | 0.616 | 1.28x | 16.9/25.1/28.3% | 1.9/5.1% | 3 |
| bucket+interval | 1 | 0.850 | 0.832 | 0.018 | - | - | 0.922 | 0.922 | 0.586 | 1.79x | 21.9/35.5/39.0% | 2.6/7.5% | 3 |

> trigger=interval: misdecodes 15

> trigger=interval: decode_failures 5

> trigger=aimd: misdecodes 4

> trigger=aimd: decode_failures 14

> trigger=bucket+interval: misdecodes 20

### `SF-capacity` - capacity  `--scenario ridge`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.874 | 0.862 | 0.011 | - | - | 0.939 | 0.942 | 0.604 | 1.27x | 16.7/25.1/28.2% | 1.9/5.2% | 3 |
| 8 | 1 | 0.873 | 0.863 | 0.011 | - | - | 0.934 | 0.938 | 0.604 | 1.26x | 16.8/25.0/28.2% | 1.9/5.2% | 3 |
| 16 | 1 | 0.876 | 0.866 | 0.011 | - | - | 0.935 | 0.937 | 0.622 | 1.26x | 16.8/24.9/28.0% | 1.9/5.1% | 3 |
| 32 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 50 | 1 | 0.878 | 0.867 | 0.012 | - | - | 0.945 | 0.947 | 0.606 | 1.28x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |

> capacity=4: decode_failures 98

> capacity=8: decode_failures 46

### `SF-capacity-local` - capacity  `--scenario ridge`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.874 | 0.862 | 0.011 | - | - | 0.939 | 0.942 | 0.604 | 1.27x | 16.7/25.1/28.2% | 1.9/5.2% | 3 |
| 8 | 1 | 0.873 | 0.863 | 0.011 | - | - | 0.934 | 0.938 | 0.604 | 1.26x | 16.8/25.0/28.2% | 1.9/5.2% | 3 |
| 16 | 1 | 0.876 | 0.866 | 0.011 | - | - | 0.935 | 0.937 | 0.622 | 1.26x | 16.8/24.9/28.0% | 1.9/5.1% | 3 |
| 32 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 50 | 1 | 0.878 | 0.867 | 0.012 | - | - | 0.945 | 0.947 | 0.606 | 1.28x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |

> capacity=4: decode_failures 98

> capacity=8: decode_failures 46

### `SF-capacity-window` - capacity  `--scenario ridge`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.867 | 0.857 | 0.009 | - | - | 0.916 | 0.934 | 0.602 | 1.26x | 16.7/24.8/28.1% | 1.9/5.1% | 3 |
| 16 | 1 | 0.873 | 0.859 | 0.013 | - | - | 0.932 | 0.936 | 0.609 | 1.25x | 16.6/24.7/27.9% | 1.9/5.1% | 3 |
| 32 | 1 | 0.880 | 0.869 | 0.011 | - | - | 0.945 | 0.948 | 0.611 | 1.25x | 16.7/24.7/27.8% | 1.9/5.1% | 3 |

> capacity=8: misdecodes 19

> capacity=8: decode_failures 31

> capacity=16: misdecodes 17

> capacity=16: decode_failures 1

> capacity=32: misdecodes 16

### `SF-catchup` - catch-up-hours  `--scenario ridge`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.850 | 0.832 | 0.018 | - | - | 0.922 | 0.922 | 0.586 | 1.79x | 21.9/35.5/39.0% | 2.6/7.5% | 3 |
| 02-06 | 1 | 0.872 | 0.866 | 0.005 | - | - | 0.907 | 0.934 | 0.615 | 1.30x | 17.1/25.7/29.0% | 1.9/5.3% | 3 |
| 00-08 | 1 | 0.871 | 0.866 | 0.005 | - | - | 0.909 | 0.936 | 0.601 | 1.39x | 18.1/27.7/30.9% | 2.0/5.7% | 3 |

> catch-up-hours=: misdecodes 20

> catch-up-hours=02-06: decode_failures 41

> catch-up-hours=00-08: decode_failures 38

### `SF-hops-flat` - hops-apart  `--scenario ridge`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.863 | 0.861 | 0.001 | - | - | 0.936 | 0.937 | 0.600 | 1.27x | 16.9/24.9/28.1% | 1.9/5.1% | 3 |
| 2 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 3 | 1 | 0.888 | 0.866 | 0.022 | - | - | 0.943 | 0.975 | 0.614 | 1.30x | 17.1/25.3/28.7% | 1.9/5.3% | 3 |
| 4 | 1 | 0.900 | 0.863 | 0.037 | - | - | 0.981 | 0.989 | 0.653 | 1.27x | 17.0/24.8/28.0% | 1.8/5.2% | 3 |

> hops-apart=3: decode_failures 42

### `SF-hops-spread` - hops-apart  `--scenario ridge`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.863 | 0.861 | 0.001 | - | - | 0.936 | 0.937 | 0.600 | 1.27x | 16.9/24.9/28.1% | 1.9/5.1% | 3 |
| 2 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 3 | 1 | 0.888 | 0.866 | 0.022 | - | - | 0.943 | 0.975 | 0.614 | 1.30x | 17.1/25.3/28.7% | 1.9/5.3% | 3 |
| 4 | 1 | 0.900 | 0.863 | 0.037 | - | - | 0.981 | 0.989 | 0.653 | 1.27x | 17.0/24.8/28.0% | 1.8/5.2% | 3 |
| 5 | 1 | 0.893 | 0.860 | 0.033 | - | - | 0.956 | 0.986 | 0.606 | 1.27x | 17.2/25.1/28.2% | 1.8/5.3% | 3 |

> hops-apart=3: decode_failures 42

> hops-apart=5: decode_failures 32

### `SF-jitter-global` - advert-jitter-s  `--scenario ridge`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.876 | 0.864 | 0.012 | - | - | 0.944 | 0.945 | 0.611 | 1.28x | 16.9/25.3/28.5% | 1.9/5.2% | 3 |
| 30 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 120 | 1 | 0.877 | 0.865 | 0.011 | - | - | 0.945 | 0.946 | 0.608 | 1.27x | 16.8/25.1/28.3% | 1.9/5.2% | 3 |
| 600 | 1 | 0.884 | 0.872 | 0.012 | - | - | 0.953 | 0.954 | 0.599 | 1.28x | 16.9/25.2/28.3% | 1.9/5.2% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario ridge`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.876 | 0.864 | 0.012 | - | - | 0.944 | 0.945 | 0.611 | 1.28x | 16.9/25.3/28.5% | 1.9/5.2% | 3 |
| 30 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 120 | 1 | 0.877 | 0.865 | 0.011 | - | - | 0.945 | 0.946 | 0.608 | 1.27x | 16.8/25.1/28.3% | 1.9/5.2% | 3 |
| 600 | 1 | 0.884 | 0.872 | 0.012 | - | - | 0.953 | 0.954 | 0.599 | 1.28x | 16.9/25.2/28.3% | 1.9/5.2% | 3 |

### `SF-place-flat` - place  `--scenario ridge`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.911 | 0.864 | 0.047 | - | - | 0.974 | 0.988 | 0.615 | 1.31x | 17.4/25.5/28.6% | 2.0/5.1% | 3 |
| routers | 1 | 0.873 | 0.864 | 0.009 | - | - | 0.979 | 0.985 | 0.624 | 1.28x | 17.0/25.0/28.3% | 1.9/5.2% | 3 |
| alternate-routers | 1 | 0.874 | 0.867 | 0.006 | - | - | 0.983 | 0.985 | 0.606 | 1.25x | 16.6/24.3/27.5% | 1.9/5.1% | 3 |
| beside-router | 1 | 0.893 | 0.869 | 0.023 | - | - | 0.981 | 0.983 | 0.621 | 1.27x | 17.0/24.9/28.3% | 1.9/5.1% | 3 |
| random-clients | 1 | 0.871 | 0.853 | 0.019 | - | - | 0.932 | 0.974 | 0.607 | 1.28x | 17.1/24.9/28.3% | 2.0/5.2% | 3 |
| hops-apart | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |

> place=spread: decode_failures 4

> place=random-clients: decode_failures 50

### `SF-place-spread` - place  `--scenario ridge`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.911 | 0.864 | 0.047 | - | - | 0.974 | 0.988 | 0.615 | 1.31x | 17.4/25.5/28.6% | 2.0/5.1% | 3 |
| routers | 1 | 0.873 | 0.864 | 0.009 | - | - | 0.979 | 0.985 | 0.624 | 1.28x | 17.0/25.0/28.3% | 1.9/5.2% | 3 |
| alternate-routers | 1 | 0.874 | 0.867 | 0.006 | - | - | 0.983 | 0.985 | 0.606 | 1.25x | 16.6/24.3/27.5% | 1.9/5.1% | 3 |
| beside-router | 1 | 0.893 | 0.869 | 0.023 | - | - | 0.981 | 0.983 | 0.621 | 1.27x | 17.0/24.9/28.3% | 1.9/5.1% | 3 |
| random-clients | 1 | 0.871 | 0.853 | 0.019 | - | - | 0.932 | 0.974 | 0.607 | 1.28x | 17.1/24.9/28.3% | 2.0/5.2% | 3 |
| hops-apart | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |

> place=spread: decode_failures 4

> place=random-clients: decode_failures 50

### `SF-provide-transport` - provide-transport  `--scenario ridge`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| broadcast | 1 | 0.884 | 0.858 | 0.026 | - | - | 0.929 | 0.931 | 0.652 | 1.32x | 17.4/25.9/29.2% | 1.9/5.3% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario ridge`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| heard | 1 | 0.871 | 0.861 | 0.009 | - | - | 0.934 | 0.938 | 0.586 | 1.27x | 17.0/25.2/28.3% | 1.9/5.2% | 3 |

> replay-ordering=heard: misdecodes 11

### `SF-replay-order-broadcast` - replay-ordering  `--scenario ridge`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.884 | 0.858 | 0.026 | - | - | 0.929 | 0.931 | 0.652 | 1.32x | 17.4/25.9/29.2% | 1.9/5.3% | 3 |
| heard | 1 | 0.879 | 0.851 | 0.027 | - | - | 0.928 | 0.930 | 0.643 | 1.34x | 17.6/26.3/29.6% | 2.0/5.4% | 3 |

> replay-ordering=heard: misdecodes 7

### `SF-resolve` - resolve  `--scenario ridge`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| enum | 1 | 0.872 | 0.860 | 0.012 | - | - | 0.931 | 0.934 | 0.621 | 1.28x | 16.9/25.3/28.4% | 1.9/5.2% | 3 |
| hybrid | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |

### `SF-servers-allrouters` - servers  `--scenario ridge`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.873 | 0.864 | 0.009 | - | - | 0.979 | 0.985 | 0.624 | 1.28x | 17.0/25.0/28.3% | 1.9/5.2% | 3 |
| 6 | 1 | 0.875 | 0.863 | 0.012 | - | - | 0.987 | 0.991 | 0.616 | 1.30x | 17.2/25.7/29.2% | 1.9/5.4% | 6 |

### `SF-servers-flat` - servers  `--scenario ridge`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.870 | 0.861 | 0.008 | - | - | 0.934 | 0.938 | 0.616 | 1.27x | 16.9/25.0/28.0% | 1.9/5.1% | 2 |
| 3 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 5 | 1 | 0.879 | 0.860 | 0.018 | - | - | 0.956 | 0.957 | 0.608 | 1.29x | 17.1/25.4/28.6% | 1.9/5.2% | 5 |
| 8 | 1 | 0.875 | 0.857 | 0.018 | - | - | 0.953 | 0.955 | 0.622 | 1.35x | 17.6/26.3/29.8% | 2.0/5.4% | 8 |

### `SF-servers-spread` - servers  `--scenario ridge`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.870 | 0.861 | 0.008 | - | - | 0.934 | 0.938 | 0.616 | 1.27x | 16.9/25.0/28.0% | 1.9/5.1% | 2 |
| 3 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 5 | 1 | 0.879 | 0.860 | 0.018 | - | - | 0.956 | 0.957 | 0.608 | 1.29x | 17.1/25.4/28.6% | 1.9/5.2% | 5 |
| 8 | 1 | 0.875 | 0.857 | 0.018 | - | - | 0.953 | 0.955 | 0.622 | 1.35x | 17.6/26.3/29.8% | 2.0/5.4% | 8 |

### `SF-signed` - signed  `--scenario ridge`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| True | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario ridge`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.883 | 0.874 | 0.009 | - | - | 0.948 | 0.950 | 0.589 | 1.17x | 15.3/23.3/26.3% | 1.7/4.8% | 3 |
| 1 | 1 | 0.890 | 0.879 | 0.011 | - | - | 0.970 | 0.971 | 0.609 | 1.15x | 15.0/23.0/25.9% | 1.7/4.8% | 3 |
| 2 | 1 | 0.882 | 0.872 | 0.010 | - | - | 0.940 | 0.940 | 0.621 | 1.15x | 15.0/23.0/25.9% | 1.7/4.7% | 3 |
| 4 | 1 | 0.883 | 0.873 | 0.010 | - | - | 0.954 | 0.957 | 0.607 | 1.15x | 14.9/22.7/25.6% | 1.7/4.7% | 3 |

### `SF-width` - short-id-bits  `--scenario ridge`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.883 | 0.872 | 0.011 | - | - | 0.946 | 0.947 | 0.616 | 1.28x | 17.1/25.3/28.5% | 1.9/5.2% | 3 |
| 24 | 1 | 0.878 | 0.865 | 0.014 | - | - | 0.947 | 0.948 | 0.600 | 1.27x | 17.0/25.0/28.2% | 1.9/5.2% | 3 |
| 32 | 1 | 0.883 | 0.871 | 0.011 | - | - | 0.945 | 0.946 | 0.621 | 1.27x | 16.9/25.2/28.4% | 1.9/5.2% | 3 |
| 64 | 1 | 0.873 | 0.862 | 0.011 | - | - | 0.934 | 0.936 | 0.621 | 1.26x | 16.7/25.0/28.1% | 1.9/5.2% | 3 |

### `SF-window-size` - window-size  `--scenario ridge`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.870 | 0.854 | 0.015 | - | - | 0.936 | 0.936 | 0.611 | 1.37x | 18.0/26.8/30.2% | 2.0/5.5% | 3 |
| 16 | 1 | 0.863 | 0.851 | 0.013 | - | - | 0.927 | 0.928 | 0.584 | 1.30x | 17.2/25.4/28.7% | 1.9/5.2% | 3 |
| 32 | 1 | 0.880 | 0.869 | 0.011 | - | - | 0.945 | 0.948 | 0.611 | 1.25x | 16.7/24.7/27.8% | 1.9/5.1% | 3 |

> window-size=8: misdecodes 146

> window-size=16: misdecodes 52

> window-size=32: misdecodes 16

### `TH-congestion` - no-congestion-scaling  `--scenario ridge`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.952 | 0.949 | 0.003 | - | - | 0.999 | 0.999 | 0.840 | 1.99x | 23.9/43.1/47.4% | 1.3/5.3% | 3 |
| True | 1 | 0.716 | 0.709 | 0.007 | - | - | 0.874 | 0.921 | 0.564 | 5.17x | 60.4/76.3/80.8% | 3.6/12.9% | 3 |

> no-congestion-scaling=True: queue drops 22.5% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: misdecodes 1

> no-congestion-scaling=True: decode_failures 82

### `TH-congestion-input` - congestion-input  `--scenario ridge`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.560 | 0.552 | 0.009 | - | - | 0.834 | 0.834 | 0.232 | 4.55x | 17.0/28.7/39.2% | 1.5/5.4% | 3 |
| truesize | 1 | 0.593 | 0.585 | 0.008 | - | - | 0.870 | 0.870 | 0.223 | 3.56x | 12.9/23.9/32.4% | 1.1/4.6% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario ridge`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.961 | 0.959 | 0.002 | - | - | 1.000 | 1.000 | 0.849 | 1.83x | 22.0/40.3/44.4% | 1.2/4.9% | 3 |
| adaptive | 1 | 0.952 | 0.949 | 0.003 | - | - | 0.999 | 0.999 | 0.840 | 1.99x | 23.9/43.1/47.4% | 1.3/5.3% | 3 |

