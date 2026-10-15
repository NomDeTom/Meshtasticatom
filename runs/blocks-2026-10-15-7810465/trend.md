# Sweep blocks-2026-10-15-7810465

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** alpine
- **seed base** 7810465 · seeds 7810465
- **blocks** 87 run
- **compute** 8.7 h of simulator time across every cell
- **generated** 2026-10-15T08:23:57+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>81 warnings</summary>

- AD-siting: siting-mix=local-typical: decode_failures 30
- AD-siting: siting-mix=basement-heavy: decode_failures 8
- AD-siting: slower: 2.92 s per simulated hour against 1.39 over 55 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- BL-control: protocol=sr: decode_failures 35
- BL-control: slower: 5.12 s per simulated hour against 1.81 over 55 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 38
- DB-hotstore-stress: max-num-nodes=250: decode_failures 2
- DB-warm: warm-num-nodes=0: decode_failures 58
- DB-warm: warm-num-nodes=25: decode_failures 58
- DB-warm: warm-num-nodes=100: decode_failures 58
- DB-warm: warm-num-nodes=2000: decode_failures 58
- DG-burst: burst-loss=0.2: decode_failures 3
- DG-burst: burst-loss=0.3: decode_failures 33
- DG-outage: burst-loss=0.1: decode_failures 39
- DG-outage: burst-loss=0.2: decode_failures 24
- DG-outage: burst-loss=0.3: decode_failures 25
- FW-mixed-26: legacy-fraction=0.5: decode_failures 28
- FW-mixed-26: slower: 3.88 s per simulated hour against 1.69 over 55 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-mixed: legacy-fraction=0.5: decode_failures 2
- FW-versions: profile=2.5: decode_failures 1
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 3
- LD-chatty: broadcast-interval-s=300: decode_failures 2
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 58
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 16.5% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 39
- MS-hopscale: nodes=250: decode_failures 2
- MS-hopscale: nodes=500: decode_failures 22
- MS-oversubscribed: nodes=500: decode_failures 6
- MS-size: nodes=150: decode_failures 1
- MS-stretch: stretch=2.0: 3 archives requested, 2 placed - group on the placed count
- MS-topology: topology=corridor: decode_failures 1
- RF-bw500: preset=SHORT_TURBO: decode_failures 14
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 8
- RF-eu-presets: preset=SHORT_FAST: 3 archives requested, 2 placed - group on the placed count
- RF-preset: preset=SHORT_FAST: 3 archives requested, 2 placed - group on the placed count
- RF-preset: preset=LONG_MODERATE: decode_failures 4
- RF-preset: faster: 1.31 s per simulated hour against 2.87 over 55 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 14
- RF-txpower: tx-power=22: decode_failures 11
- RF-txpower: tx-power=17: decode_failures 14
- RT-rebroadcast: rebroadcast-mode=CORE_PORTNUMS_ONLY: decode_failures 3
- SF-bucket-mode: bucket-mode=global: misdecodes 44
- SF-bucket-mode: bucket-mode=time: misdecodes 39
- SF-bucket-mode: bucket-mode=window: misdecodes 28
- SF-bucket-time: time-bucket-s=600: misdecodes 118
- SF-bucket-time: time-bucket-s=1800: misdecodes 39
- SF-bucket-time: time-bucket-s=3600: misdecodes 8
- SF-cadence: trigger=interval: misdecodes 13
- SF-cadence: trigger=aimd: misdecodes 4
- SF-cadence: trigger=bucket+interval: misdecodes 20
- SF-capacity-local: capacity=4: decode_failures 102
- SF-capacity-local: capacity=8: decode_failures 28
- SF-capacity: capacity=4: decode_failures 102
- SF-capacity: capacity=8: decode_failures 28
- SF-capacity-window: capacity=8: misdecodes 31
- SF-capacity-window: capacity=8: decode_failures 35
- SF-capacity-window: capacity=16: misdecodes 23
- SF-capacity-window: capacity=32: misdecodes 28
- SF-catchup: catch-up-hours=: misdecodes 20
- SF-catchup: catch-up-hours=02-06: misdecodes 2
- SF-catchup: catch-up-hours=02-06: decode_failures 16
- SF-catchup: catch-up-hours=00-08: decode_failures 19
- SF-hops-flat: hops-apart=3: decode_failures 35
- SF-hops-flat: hops-apart=4: decode_failures 18
- SF-hops-spread: hops-apart=3: decode_failures 35
- SF-hops-spread: hops-apart=4: decode_failures 18
- SF-hops-spread: hops-apart=5: decode_failures 34
- SF-place-flat: place=spread: decode_failures 31
- SF-place-flat: place=random-clients: decode_failures 41
- SF-place-spread: place=spread: decode_failures 31
- SF-place-spread: place=random-clients: decode_failures 41
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 10
- SF-replay-order: replay-ordering=heard: misdecodes 28
- SF-servers-flat: servers=5: misdecodes 1
- SF-servers-flat: servers=8: misdecodes 1
- SF-servers-spread: servers=5: misdecodes 1
- SF-servers-spread: servers=8: misdecodes 1
- SF-window-size: window-size=8: misdecodes 136
- SF-window-size: window-size=16: misdecodes 68
- SF-window-size: window-size=32: misdecodes 28
- TH-congestion: no-congestion-scaling=True: decode_failures 56

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `BL-control` | 5.12 | 1.81 | 2.82x | 55 |
| `FW-mixed-26` | 3.88 | 1.69 | 2.30x | 55 |
| `AD-siting` | 2.92 | 1.39 | 2.10x | 55 |
| `RF-bw500` | 3.16 | 1.94 | 1.63x | 55 |
| `SF-place-spread` | 4.37 | 2.75 | 1.59x | 55 |
| `MS-density` | 2.15 | 3.24 | 0.66x | 55 |
| `SF-bucket-mode` | 0.917 | 1.45 | 0.63x | 55 |
| `SF-capacity` | 1.07 | 1.7 | 0.62x | 55 |
| `PR-repeats-busy` | 2.34 | 3.78 | 0.62x | 55 |
| `LD-chatty-hops` | 2.24 | 3.85 | 0.58x | 55 |
| `LD-chatty` | 2.71 | 4.67 | 0.58x | 55 |
| `SF-signed` | 0.978 | 1.69 | 0.58x | 55 |
| `LD-diurnal` | 0.874 | 1.51 | 0.58x | 55 |
| `LD-interval` | 0.749 | 1.31 | 0.57x | 55 |
| `MS-siting` | 1.05 | 1.84 | 0.57x | 54 |
| `SF-servers-flat` | 1.3 | 2.29 | 0.57x | 55 |
| `SF-width` | 0.938 | 1.66 | 0.57x | 55 |
| `MS-stretch` | 1.13 | 2.03 | 0.56x | 55 |
| `TH-congestion` | 9.07 | 17.1 | 0.53x | 55 |
| `MS-hopscale` | 9.38 | 17.9 | 0.52x | 55 |
| `RF-preset` | 1.31 | 2.87 | 0.46x | 55 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `MS-siting` | siting-mix | **held** | 0.017 → 0.998 | 0.981 | 0.144 → 0.975 | 1.7x bytes_on_air | up | 4 |
| `PR-protocol` | protocol | **held** | 0 → 0.970 | 0.970 | 0.805 → 0.824 | 1.2x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.954 | 0.954 | 0.823 → 0.824 | 1x bytes_on_air | up | 2 |
| `RF-txpower` | tx-power | **held** | 0.018 → 0.970 | 0.952 | 0.108 → 0.816 | 1.9x bytes_on_air | down | 4 |
| `MS-stretch` | stretch | **held** | 0.107 → 0.970 | 0.862 | 0.172 → 0.816 | 60x sr_bytes | down | 4 |
| `RF-eu-presets` | preset | **held** | 0.135 → 0.971 | 0.836 | 0.358 → 0.816 | 80x sr_airtime | up | 4 |
| `RF-preset` | preset | **held** | 0.135 → 0.971 | 0.836 | 0.358 → 0.816 | 1.1e+02x sr_airtime | up | 3 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.113 → 0.917 | 0.804 | 0.099 → 0.768 | 1.4e+02x sr_airtime | down | 4 |
| `RF-preset-turbo` | preset | **text** | 0.079 → 0.822 | 0.743 | 0.078 → 0.816 | 3.3x advert_bytes | up | 5 |
| `AD-siting` | siting-mix | **text** | 0.083 → 0.801 | 0.718 | 0.078 → 0.789 | 3.8x advert_bytes | down | 3 |
| `RF-bw500` | preset | **held** | 0.313 → 0.904 | 0.591 | 0.205 → 0.728 | 3.2x sr_airtime | up | 3 |
| `MS-hopscale` | nodes | **held** | 0.462 → 0.970 | 0.509 | 0.313 → 0.816 | 8.5x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **held** | 0.464 → 0.966 | 0.503 | 0.318 → 0.718 | 4.4x bytes_on_air | down | 3 |
| `MS-density` | nodes | **text** | 0.597 → 0.958 | 0.361 | 0.588 → 0.956 | 8x sr_airtime | up | 5 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.557 → 0.901 | 0.344 | 0.538 → 0.899 | 7x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.488 → 0.822 | 0.334 | 0.469 → 0.816 | 2.2x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.552 → 0.861 | 0.308 | 0.531 → 0.856 | 6.6x sr_airtime | down | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.612 → 0.916 | 0.304 | 0.586 → 0.914 | 2.4x sr_bytes | up | 4 |
| `DG-burst` | burst-loss | **text** | 0.524 → 0.822 | 0.298 | 0.498 → 0.816 | 2.3x sr_bytes | down | 4 |
| `MS-topology` | topology | **text** | 0.659 → 0.917 | 0.258 | 0.639 → 0.917 | 2.8x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.612 → 0.868 | 0.256 | 0.586 → 0.864 | 1.9x sr_bytes | up | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.399 → 0.634 | 0.236 | 0.393 → 0.623 | 1.5x sr_airtime | up | 2 |
| `SF-hops-spread` | hops-apart | **held** | 0.753 → 0.970 | 0.216 | 0.816 → 0.823 | 4x sr_bytes | down | 5 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.492 → 0.708 | 0.216 | 0.337 → 0.530 | 5.1x sr_airtime | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.612 → 0.822 | 0.210 | 0.586 → 0.816 | 1.6x sr_bytes | up | 2 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.743 → 0.952 | 0.209 | 0.735 → 0.949 | 5.5x sr_airtime | down | 2 |
| `RF-noise` | noise-profile | **text** | 0.661 → 0.822 | 0.161 | 0.655 → 0.816 | 1.3x sr_airtime | down | 4 |
| `DG-loss` | extra-loss | **text** | 0.686 → 0.822 | 0.136 | 0.671 → 0.816 | 1.7x sr_bytes | down | 4 |
| `FW-versions` | profile | **text** | 0.692 → 0.822 | 0.130 | 0.681 → 0.816 | 3.6x bytes_on_air | up | 5 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.822 → 0.943 | 0.121 | 0.816 → 0.939 | 2.1x sr_bytes | up | 3 |
| `MS-size` | nodes | **text** | 0.709 → 0.822 | 0.113 | 0.704 → 0.816 | 4.3x sr_airtime | down | 5 |
| `SF-hops-flat` | hops-apart | **held** | 0.871 → 0.970 | 0.099 | 0.816 → 0.823 | 2.5x sr_bytes | down | 4 |
| `SC-signing` | signature-policy | **text** | 0.724 → 0.822 | 0.098 | 0.724 → 0.816 | 1.2x sr_airtime | down | 3 |
| `FW-firmware` | profile | **text** | 0.725 → 0.822 | 0.097 | 0.711 → 0.816 | 3.6x bytes_on_air | up | 2 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.725 → 0.817 | 0.093 | 0.639 → 0.722 | 1.6x sr_airtime | down | 2 |
| `LD-interval` | broadcast-interval-s | **text** | 0.787 → 0.875 | 0.088 | 0.777 → 0.873 | 5x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.777 → 0.863 | 0.086 | 0.766 → 0.857 | 2.2x sr_airtime | down | 3 |
| `AD-badrouters` | role-placement | **text** | 0.717 → 0.801 | 0.084 | 0.697 → 0.789 | 1.2x sr_bytes | down | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.822 → 0.906 | 0.084 | 0.816 → 0.905 | 1.5x sr_bytes | up | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.780 → 0.863 | 0.083 | 0.769 → 0.857 | 2.2x sr_airtime | up | 4 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.783 → 0.863 | 0.081 | 0.776 → 0.859 | 2.1x bytes_on_air | up | 4 |
| `AD-flooding` | role-mix | **text** | 0.801 → 0.881 | 0.080 | 0.789 → 0.876 | 2.2x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.801 → 0.881 | 0.080 | 0.789 → 0.876 | 2.2x bytes_on_air | up | 3 |
| `SF-place-flat` | place | **held** | 0.898 → 0.970 | 0.072 | 0.809 → 0.820 | 3.6x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.898 → 0.970 | 0.072 | 0.809 → 0.820 | 3.6x sr_bytes | up | 6 |
| `FW-mixed` | legacy-fraction | **text** | 0.787 → 0.859 | 0.071 | 0.781 → 0.855 | 2.1x bytes_on_air | up | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.822 → 0.891 | 0.069 | 0.816 → 0.884 | 1.2x bytes_on_air | up | 3 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.918 → 0.970 | 0.051 | 0.816 → 0.825 | 23x sr_airtime | down | 3 |
| `FW-signing-cost` | profile-flag | **text** | 0.822 → 0.866 | 0.044 | 0.816 → 0.864 | 3.3x bytes_on_air | down | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.780 → 0.823 | 0.043 | 0.771 → 0.816 | 1.4x sr_airtime | down | 4 |
| `SF-cadence` | trigger | **held** | 0.929 → 0.970 | 0.040 | 0.793 → 0.825 | 13x advert_bytes | down | 4 |
| `RT-hopassign` | hop-assign | **held** | 0.931 → 0.970 | 0.038 | 0.816 → 0.817 | 1x sr_bytes | down | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.826 → 0.857 | 0.031 | 0.819 → 0.851 | 1.1x bytes_on_air | up | 2 |
| `MS-roles` | role-mix | **text** | 0.801 → 0.831 | 0.030 | 0.789 → 0.824 | 1.6x sr_bytes | down | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.708 → 0.737 | 0.029 | 0.525 → 0.554 | 1.4x sr_airtime | up | 2 |
| `MS-router-late` | router-late-fraction | **text** | 0.822 → 0.848 | 0.026 | 0.816 → 0.843 | 1.3x bytes_on_air | up | 4 |
| `SF-catchup` | catch-up-hours | **held** | 0.941 → 0.966 | 0.025 | 0.793 → 0.818 | 9.4x advert_bytes | down | 3 |
| `AD-worst` | role-placement | **text** | 0.782 → 0.807 | 0.025 | 0.775 → 0.801 | 1.1x sr_bytes | down | 2 |
| `MS-roles-fav` | role-mix | **held** | 0.919 → 0.940 | 0.021 | 0.822 → 0.835 | 1.2x sr_bytes | down | 2 |
| `SF-servers-flat` | servers | **held** | 0.959 → 0.980 | 0.020 | 0.809 → 0.820 | 6.5x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.959 → 0.980 | 0.020 | 0.809 → 0.820 | 6.5x sr_bytes | up | 4 |
| `SF-provide-transport` | provide-transport | **text** | 0.822 → 0.842 | 0.020 | 0.810 → 0.816 | 2.3x sr_airtime | up | 2 |
| `SF-sr-retries` | sr-retries | **held** | 0.964 → 0.982 | 0.018 | 0.821 → 0.836 | 1.1x sr_bytes | down | 4 |
| `SF-servers-allrouters` | servers | **held** | 0.958 → 0.975 | 0.018 | 0.813 → 0.814 | 2.2x sr_bytes | up | 2 |
| `SF-window-size` | window-size | **held** | 0.957 → 0.974 | 0.017 | 0.809 → 0.816 | 5.9x advert_bytes | down | 3 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.957 → 0.973 | 0.016 | 0.804 → 0.820 | 5.5x advert_bytes | up | 3 |
| `DM-mode` | dm-mode | **text** | 0.784 → 0.800 | 0.016 | 0.784 → 0.800 | 1.3x sr_airtime | up | 3 |
| `LD-diurnal` | diurnal | **text** | 0.822 → 0.837 | 0.015 | 0.816 → 0.833 | 1.2x advert_bytes | down | 3 |
| `SF-capacity` | capacity | **held** | 0.960 → 0.973 | 0.013 | 0.811 → 0.820 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.960 → 0.973 | 0.013 | 0.811 → 0.820 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-window` | capacity | **held** | 0.957 → 0.970 | 0.013 | 0.811 → 0.817 | 2x advert_bytes | down | 3 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.957 → 0.970 | 0.013 | 0.811 → 0.821 | 2.9x advert_bytes | down | 4 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.941 → 0.952 | 0.011 | 0.937 → 0.949 | 1.3x sr_airtime | down | 2 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.785 → 0.795 | 0.011 | 0.785 → 0.795 | 1.1x sr_airtime | down | 2 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.817 → 0.827 | 0.010 | 0.811 → 0.821 | 1.1x sr_airtime | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.817 → 0.827 | 0.010 | 0.811 → 0.821 | 1.1x sr_airtime | up | 4 |
| `SF-width` | short-id-bits | **held** | 0.965 → 0.974 | 0.009 | 0.816 → 0.823 | 3.1x advert_bytes | up | 4 |
| `SF-advert-transport` | advert-transport | **text** | 0.822 → 0.830 | 0.008 | 0.816 → 0.825 | 3.2x sr_airtime | up | 2 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.795 → 0.800 | 0.005 | 0.795 → 0.800 | 1.1x sr_airtime | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.838 → 0.842 | 0.004 | 0.807 → 0.810 | 1x sr_airtime | down | 2 |
| `TH-congestion-mode` | congestion-mode | **held** | 0.997 → 1.000 | 0.003 | 0.949 → 0.952 | 1.1x bytes_on_air | down | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.822 → 0.824 | 0.002 | 0.816 → 0.819 | 1x sr_bytes | up | 2 |
| `SF-replay-order` | replay-ordering | **held** | 0.970 → 0.971 | 0.002 | 0.816 → 0.818 | 1.1x sr_bytes | up | 2 |
| `SF-resolve` | resolve | **held** | 0.968 → 0.970 | 0.001 | 0.816 → 0.816 | 5.7x advert_bytes | = | 3 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.952 → 0.953 | 0.001 | 0.949 → 0.950 | 1x bytes_on_air | up | 2 |

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
| none | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| sprinkled | 1 | 0.838 | 0.833 | 0.005 | - | - | 0.965 | 0.965 | 0.272 | 1.27x | 16.0/25.7/27.8% | 1.8/5.4% | 3 |
| arms-race | 1 | 0.906 | 0.905 | 0.001 | - | - | 0.960 | 0.960 | 0.560 | 1.20x | 20.0/28.1/31.6% | 1.7/5.4% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario alpine`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 0.1 | 1 | 0.859 | 0.839 | 0.020 | - | - | 0.982 | 0.982 | 0.415 | 1.38x | 17.2/26.3/29.9% | 1.9/5.5% | 3 |
| 0.3 | 1 | 0.943 | 0.939 | 0.004 | - | - | 0.992 | 0.993 | 0.780 | 1.07x | 18.1/24.4/27.7% | 1.4/4.9% | 3 |

### `AD-badrouters` - role-placement  `--scenario alpine`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.801 | 0.789 | 0.012 | - | - | 0.941 | 0.943 | 0.331 | 1.19x | 14.7/21.5/25.2% | 2.0/5.0% | 3 |
| inverse | 1 | 0.717 | 0.697 | 0.019 | - | - | 0.886 | 0.889 | 0.228 | 1.09x | 12.5/16.6/21.9% | 1.9/3.6% | 3 |
| random | 1 | 0.771 | 0.758 | 0.013 | - | - | 0.945 | 0.947 | 0.314 | 1.21x | 13.6/18.8/22.4% | 2.1/4.7% | 3 |

### `AD-flooding` - role-mix  `--scenario alpine`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.801 | 0.789 | 0.012 | - | - | 0.941 | 0.943 | 0.331 | 1.19x | 14.7/21.5/25.2% | 2.0/5.0% | 3 |
| all-routers | 1 | 0.881 | 0.876 | 0.005 | - | - | 0.986 | 0.986 | 0.431 | 2.66x | 29.4/37.3/40.3% | 4.5/5.2% | 3 |

### `AD-nomute` - role-mix  `--scenario alpine`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.801 | 0.789 | 0.012 | - | - | 0.941 | 0.943 | 0.331 | 1.19x | 14.7/21.5/25.2% | 2.0/5.0% | 3 |
| no-mute | 1 | 0.819 | 0.810 | 0.009 | - | - | 0.946 | 0.948 | 0.302 | 1.34x | 15.6/22.6/24.7% | 2.1/4.9% | 3 |
| all-routers | 1 | 0.881 | 0.876 | 0.005 | - | - | 0.986 | 0.986 | 0.431 | 2.66x | 29.4/37.3/40.3% | 4.5/5.2% | 3 |

### `AD-siting` - siting-mix  `--scenario alpine`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.801 | 0.789 | 0.012 | - | - | 0.941 | 0.943 | 0.331 | 1.19x | 14.7/21.5/25.2% | 2.0/5.0% | 3 |
| local-typical | 1 | 0.634 | 0.614 | 0.020 | - | - | 0.774 | 0.849 | 0.000 | 1.11x | 10.4/24.0/29.0% | 1.7/5.1% | 3 |
| basement-heavy | 1 | 0.083 | 0.078 | 0.004 | - | - | 0.257 | 0.284 | 0.000 | 0.55x | 1.5/7.5/10.7% | 0.3/2.8% | 3 |

> siting-mix=local-typical: decode_failures 30

> siting-mix=basement-heavy: decode_failures 8

> slower: 2.92 s per simulated hour against 1.39 over 55 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-worst` - role-placement  `--scenario alpine`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.807 | 0.801 | 0.006 | - | - | 0.967 | 0.968 | 0.000 | 2.36x | 16.0/25.7/31.4% | 1.9/5.3% | 3 |
| inverse | 1 | 0.782 | 0.775 | 0.007 | - | - | 0.957 | 0.957 | 0.000 | 2.37x | 14.6/25.4/29.5% | 1.9/3.6% | 3 |

### `BL-control` - protocol  `--scenario alpine`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.824 | 0.824 | 0.000 | - | - | 0 | 0.000 | 0.366 | 1.31x | 15.8/24.1/26.0% | 1.8/5.1% | 3 |
| sr | 1 | 0.846 | 0.823 | 0.024 | - | - | 0.954 | 0.983 | 0.334 | 1.34x | 16.0/24.6/26.5% | 1.8/5.1% | 3 |

> protocol=sr: decode_failures 35

> slower: 5.12 s per simulated hour against 1.81 over 55 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario alpine`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.780 | 0.769 | 0.012 | - | - | 0.938 | 0.939 | 0.314 | 2.93x | 35.0/51.0/56.2% | 3.8/10.0% | 3 |
| 100 | 1 | 0.863 | 0.857 | 0.006 | - | - | 0.972 | 0.973 | 0.401 | 1.52x | 18.4/27.6/30.6% | 1.9/5.3% | 3 |
| 120 | 1 | 0.863 | 0.857 | 0.006 | - | - | 0.972 | 0.973 | 0.401 | 1.52x | 18.4/27.6/30.6% | 1.9/5.3% | 3 |
| 250 | 1 | 0.863 | 0.857 | 0.006 | - | - | 0.972 | 0.973 | 0.401 | 1.52x | 18.4/27.6/30.6% | 1.9/5.3% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario alpine`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.342 | 0.337 | 0.005 | - | - | 0.492 | 0.497 | 0.076 | 11.49x | 39.7/56.4/71.4% | 4.1/10.5% | 3 |
| 120 | 1 | 0.534 | 0.525 | 0.008 | - | - | 0.708 | 0.711 | 0.128 | 4.42x | 15.1/26.3/37.5% | 1.4/5.3% | 3 |
| 250 | 1 | 0.538 | 0.530 | 0.008 | - | - | 0.707 | 0.709 | 0.131 | 4.34x | 14.9/25.6/36.3% | 1.4/5.2% | 3 |

> max-num-nodes=10: decode_failures 38

> max-num-nodes=250: decode_failures 2

### `DB-platform` - platform-mix  `--scenario alpine`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.863 | 0.857 | 0.006 | - | - | 0.972 | 0.973 | 0.401 | 1.52x | 18.4/27.6/30.6% | 1.9/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.863 | 0.857 | 0.006 | - | - | 0.972 | 0.973 | 0.401 | 1.52x | 18.4/27.6/30.6% | 1.9/5.3% | 3 |
| constrained | 1 | 0.777 | 0.766 | 0.011 | - | - | 0.928 | 0.929 | 0.323 | 2.94x | 35.0/51.0/56.2% | 3.8/10.0% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario alpine`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.730 | 0.722 | 0.007 | - | - | 0.817 | 0.918 | 0.517 | 5.71x | 57.6/72.7/77.5% | 4.1/12.8% | 3 |
| 25 | 1 | 0.730 | 0.722 | 0.007 | - | - | 0.817 | 0.918 | 0.517 | 5.71x | 57.6/72.7/77.5% | 4.1/12.8% | 3 |
| 100 | 1 | 0.730 | 0.722 | 0.007 | - | - | 0.817 | 0.918 | 0.517 | 5.71x | 57.6/72.7/77.5% | 4.1/12.8% | 3 |
| 2000 | 1 | 0.730 | 0.722 | 0.007 | - | - | 0.817 | 0.918 | 0.517 | 5.71x | 57.6/72.7/77.5% | 4.1/12.8% | 3 |

> warm-num-nodes=0: decode_failures 58

> warm-num-nodes=25: decode_failures 58

> warm-num-nodes=100: decode_failures 58

> warm-num-nodes=2000: decode_failures 58

### `DG-burst` - burst-loss  `--scenario alpine`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 0.1 | 1 | 0.726 | 0.709 | 0.017 | - | - | 0.939 | 0.948 | 0.231 | 1.26x | 15.5/23.8/25.9% | 1.8/5.0% | 3 |
| 0.2 | 1 | 0.630 | 0.603 | 0.027 | - | - | 0.906 | 0.917 | 0.168 | 1.16x | 14.5/22.2/24.0% | 1.7/4.5% | 3 |
| 0.3 | 1 | 0.524 | 0.498 | 0.026 | - | - | 0.783 | 0.868 | 0.103 | 1.07x | 13.7/20.9/22.7% | 1.5/4.0% | 3 |

> burst-loss=0.2: decode_failures 3

> burst-loss=0.3: decode_failures 33

### `DG-loss` - extra-loss  `--scenario alpine`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 0.1 | 1 | 0.786 | 0.779 | 0.008 | - | - | 0.968 | 0.969 | 0.232 | 1.39x | 17.0/25.7/27.6% | 2.0/5.2% | 3 |
| 0.2 | 1 | 0.751 | 0.742 | 0.009 | - | - | 0.947 | 0.951 | 0.187 | 1.41x | 17.6/26.3/28.3% | 2.0/5.1% | 3 |
| 0.3 | 1 | 0.686 | 0.671 | 0.015 | - | - | 0.911 | 0.918 | 0.137 | 1.43x | 18.3/26.7/29.0% | 2.1/5.0% | 3 |

### `DG-outage` - burst-loss  `--scenario alpine`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 0.1 | 1 | 0.728 | 0.714 | 0.014 | - | - | 0.911 | 0.945 | 0.267 | 1.26x | 15.3/23.5/25.7% | 1.8/5.1% | 3 |
| 0.2 | 1 | 0.621 | 0.599 | 0.022 | - | - | 0.885 | 0.921 | 0.172 | 1.18x | 14.6/22.0/24.4% | 1.7/4.6% | 3 |
| 0.3 | 1 | 0.488 | 0.469 | 0.019 | - | - | 0.694 | 0.880 | 0.101 | 1.08x | 13.8/20.9/23.0% | 1.6/4.2% | 3 |

> burst-loss=0.1: decode_failures 39

> burst-loss=0.2: decode_failures 24

> burst-loss=0.3: decode_failures 25

### `DM-mode` - dm-mode  `--scenario alpine`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.784 | 0.784 | 0.000 | - | - | 0.956 | 0.958 | 0.316 | 1.78x | 21.3/32.6/35.4% | 2.4/6.9% | 3 |
| directed-with-late-flood | 1 | 0.800 | 0.800 | 0.000 | - | - | 0.958 | 0.961 | 0.323 | 1.61x | 19.5/29.9/32.4% | 2.2/6.3% | 3 |
| m4-early-flood | 1 | 0.788 | 0.788 | 0.000 | - | - | 0.958 | 0.959 | 0.306 | 1.62x | 19.6/30.1/32.7% | 2.2/6.4% | 3 |

### `FW-firmware` - profile  `--scenario alpine`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.725 | 0.711 | 0.014 | - | - | 0.902 | 0.902 | 0.041 | 0.68x | 8.1/10.9/12.6% | 1.1/1.9% | 3 |
| 2.8 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario alpine`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 0.25 | 1 | 0.787 | 0.781 | 0.006 | - | - | 0.969 | 0.969 | 0.149 | 1.18x | 14.4/19.5/23.5% | 1.6/5.1% | 3 |
| 0.5 | 1 | 0.796 | 0.788 | 0.008 | - | - | 0.920 | 0.921 | 0.310 | 1.03x | 11.6/17.3/20.2% | 1.5/4.0% | 3 |
| 0.75 | 1 | 0.859 | 0.855 | 0.004 | - | - | 0.980 | 0.981 | 0.065 | 0.89x | 10.7/14.6/17.1% | 1.4/3.5% | 3 |

> legacy-fraction=0.5: decode_failures 2

### `FW-mixed-26` - legacy-fraction  `--scenario alpine`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 0.25 | 1 | 0.783 | 0.776 | 0.007 | - | - | 0.963 | 0.964 | 0.136 | 1.19x | 14.5/19.8/23.9% | 1.6/5.2% | 3 |
| 0.5 | 1 | 0.804 | 0.797 | 0.007 | - | - | 0.923 | 0.933 | 0.265 | 1.01x | 11.4/17.1/20.5% | 1.4/4.0% | 3 |
| 0.75 | 1 | 0.863 | 0.859 | 0.004 | - | - | 0.985 | 0.986 | 0.038 | 0.86x | 10.5/14.6/17.5% | 1.3/3.6% | 3 |

> legacy-fraction=0.5: decode_failures 28

> slower: 3.88 s per simulated hour against 1.69 over 55 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-signing-cost` - profile-flag  `--scenario alpine`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.866 | 0.864 | 0.003 | - | - | 0.988 | 0.988 | 0.362 | 0.72x | 9.0/14.3/15.4% | 0.9/3.1% | 3 |
| signing=true | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |

### `FW-versions` - profile  `--scenario alpine`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.712 | 0.700 | 0.012 | - | - | 0.900 | 0.901 | 0.040 | 0.68x | 8.3/11.6/13.7% | 1.0/2.5% | 3 |
| 2.5 | 1 | 0.698 | 0.686 | 0.012 | - | - | 0.882 | 0.885 | 0.030 | 0.71x | 8.5/11.9/14.1% | 1.1/2.5% | 3 |
| 2.6 | 1 | 0.692 | 0.681 | 0.011 | - | - | 0.870 | 0.876 | 0.030 | 0.68x | 8.4/11.9/14.3% | 1.0/2.6% | 3 |
| 2.7 | 1 | 0.717 | 0.707 | 0.010 | - | - | 0.891 | 0.895 | 0.041 | 0.71x | 8.6/14.9/17.6% | 0.9/3.2% | 3 |
| 2.8 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |

> profile=2.5: decode_failures 1

### `LD-chatty` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.861 | 0.856 | 0.004 | - | - | 0.979 | 0.980 | 0.340 | 0.91x | 10.8/16.7/17.9% | 1.2/3.6% | 3 |
| 900 | 1 | 0.787 | 0.777 | 0.009 | - | - | 0.952 | 0.954 | 0.280 | 2.08x | 25.0/37.8/40.6% | 2.9/8.1% | 3 |
| 300 | 1 | 0.552 | 0.531 | 0.021 | - | - | 0.798 | 0.820 | 0.197 | 4.49x | 48.5/69.0/75.7% | 6.7/15.6% | 3 |

> broadcast-interval-s=300: decode_failures 2

### `LD-chatty-hops` - broadcast-interval-s  `--scenario alpine`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.901 | 0.899 | 0.002 | - | - | 0.976 | 0.976 | 0.462 | 0.99x | 11.5/17.0/18.3% | 1.4/3.5% | 3 |
| 900 | 1 | 0.822 | 0.812 | 0.010 | - | - | 0.945 | 0.945 | 0.406 | 2.36x | 27.5/40.8/44.2% | 3.3/8.5% | 3 |
| 300 | 1 | 0.557 | 0.538 | 0.020 | - | - | 0.770 | 0.780 | 0.257 | 4.99x | 53.1/71.2/77.8% | 7.4/16.1% | 3 |

> broadcast-interval-s=300: decode_failures 3

### `LD-diurnal` - diurnal  `--scenario alpine`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.836 | 0.831 | 0.004 | - | - | 0.972 | 0.974 | 0.334 | 1.27x | 15.3/23.5/25.2% | 1.7/5.0% | 3 |
| sinusoid | 1 | 0.837 | 0.833 | 0.004 | - | - | 0.977 | 0.977 | 0.326 | 1.21x | 14.5/22.2/24.1% | 1.6/4.7% | 3 |
| commuter | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.787 | 0.777 | 0.009 | - | - | 0.952 | 0.954 | 0.280 | 2.08x | 25.0/37.8/40.6% | 2.9/8.1% | 3 |
| 3600 | 1 | 0.861 | 0.856 | 0.004 | - | - | 0.979 | 0.980 | 0.340 | 0.91x | 10.8/16.7/17.9% | 1.2/3.6% | 3 |
| 10800 | 1 | 0.867 | 0.865 | 0.002 | - | - | 0.980 | 0.982 | 0.346 | 0.60x | 7.2/11.2/11.9% | 0.8/2.4% | 3 |
| 43200 | 1 | 0.875 | 0.873 | 0.002 | - | - | 0.988 | 0.988 | 0.352 | 0.46x | 5.6/8.8/9.3% | 0.6/1.9% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario alpine`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 0.25 | 1 | 0.823 | 0.816 | 0.007 | - | - | 0.974 | 0.975 | 0.311 | 1.44x | 17.3/26.6/28.4% | 2.0/5.6% | 3 |
| 1.0 | 1 | 0.803 | 0.795 | 0.008 | - | - | 0.961 | 0.962 | 0.344 | 1.57x | 19.0/29.1/31.4% | 2.1/6.2% | 3 |
| 4.0 | 1 | 0.780 | 0.771 | 0.009 | - | - | 0.956 | 0.956 | 0.296 | 1.92x | 23.5/35.8/38.8% | 2.6/7.8% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario alpine`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.730 | 0.722 | 0.007 | - | - | 0.817 | 0.918 | 0.517 | 5.71x | 57.6/72.7/77.5% | 4.1/12.8% | 3 |
| 1.0 | 1 | 0.646 | 0.639 | 0.007 | - | - | 0.725 | 0.869 | 0.440 | 6.40x | 62.1/75.2/79.7% | 4.6/14.2% | 3 |

> traceroute-per-hour=0.0: decode_failures 58

> traceroute-per-hour=1.0: queue drops 16.5% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 39

### `MS-density` - nodes  `--scenario alpine`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.597 | 0.588 | 0.008 | - | - | 0.690 | 0.690 | 0.228 | 1.19x | 13.6/23.7/27.1% | 3.0/5.9% | 3 |
| 60 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 90 | 1 | 0.908 | 0.905 | 0.003 | - | - | 0.979 | 0.979 | 0.636 | 1.58x | 18.3/24.7/28.2% | 1.4/4.8% | 3 |
| 120 | 1 | 0.952 | 0.949 | 0.003 | - | - | 0.997 | 0.999 | 0.773 | 2.02x | 23.3/32.8/37.0% | 1.3/5.1% | 3 |
| 150 | 1 | 0.958 | 0.956 | 0.002 | - | - | 1.000 | 1.000 | 0.790 | 2.61x | 28.0/41.3/45.0% | 1.3/5.8% | 3 |

### `MS-hopscale` - nodes  `--scenario alpine`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 120 | 1 | 0.729 | 0.718 | 0.011 | - | - | 0.970 | 0.974 | 0.197 | 2.21x | 14.0/28.1/34.4% | 1.4/5.3% | 3 |
| 250 | 1 | 0.532 | 0.523 | 0.008 | - | - | 0.708 | 0.709 | 0.133 | 4.75x | 16.1/28.6/40.6% | 1.6/5.8% | 3 |
| 500 | 1 | 0.317 | 0.313 | 0.004 | - | - | 0.462 | 0.463 | 0.034 | 10.17x | 19.3/29.7/50.6% | 1.8/6.1% | 3 |

> nodes=250: decode_failures 2

> nodes=500: decode_failures 22

### `MS-oversubscribed` - nodes  `--scenario alpine`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.728 | 0.718 | 0.011 | - | - | 0.966 | 0.969 | 0.183 | 2.12x | 13.4/26.6/32.6% | 1.4/5.0% | 3 |
| 250 | 1 | 0.534 | 0.525 | 0.008 | - | - | 0.708 | 0.711 | 0.128 | 4.42x | 15.1/26.3/37.5% | 1.4/5.3% | 3 |
| 500 | 1 | 0.322 | 0.318 | 0.004 | - | - | 0.464 | 0.464 | 0.030 | 9.19x | 17.4/26.5/45.0% | 1.6/5.5% | 3 |

> nodes=500: decode_failures 6

### `MS-roles` - role-mix  `--scenario alpine`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.831 | 0.824 | 0.007 | - | - | 0.951 | 0.953 | 0.257 | 1.32x | 16.0/24.4/26.2% | 1.7/5.1% | 3 |
| baymesh-2026-08 | 1 | 0.801 | 0.789 | 0.012 | - | - | 0.941 | 0.943 | 0.331 | 1.19x | 14.7/21.5/25.2% | 2.0/5.0% | 3 |

### `MS-roles-fav` - role-mix  `--scenario alpine`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.842 | 0.835 | 0.007 | - | - | 0.940 | 0.942 | 0.339 | 1.40x | 16.8/25.4/27.2% | 1.9/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.830 | 0.822 | 0.008 | - | - | 0.919 | 0.921 | 0.375 | 1.32x | 16.0/23.3/27.5% | 2.3/4.9% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario alpine`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 0.05 | 1 | 0.831 | 0.826 | 0.005 | - | - | 0.964 | 0.964 | 0.335 | 1.46x | 17.8/26.8/31.2% | 1.8/5.3% | 3 |
| 0.1 | 1 | 0.840 | 0.834 | 0.006 | - | - | 0.970 | 0.972 | 0.368 | 1.49x | 18.7/28.5/31.8% | 1.9/5.2% | 3 |
| 0.2 | 1 | 0.848 | 0.843 | 0.006 | - | - | 0.970 | 0.970 | 0.337 | 1.69x | 21.8/31.6/35.9% | 2.3/5.2% | 3 |

### `MS-siting` - siting-mix  `--scenario alpine`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| local-typical | 1 | 0.742 | 0.732 | 0.010 | - | - | 0.914 | 0.915 | 0.000 | 1.49x | 12.8/26.5/33.7% | 2.1/5.3% | 3 |
| event | 1 | 0.144 | 0.144 | 0.000 | - | - | 0.017 | 0.025 | 0.000 | 0.88x | 3.4/10.0/17.5% | 1.2/4.8% | 3 |
| backbone | 1 | 0.976 | 0.975 | 0.001 | - | - | 0.998 | 0.998 | 0.886 | 1.12x | 25.4/32.4/35.9% | 1.5/5.5% | 3 |

### `MS-size` - nodes  `--scenario alpine`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.736 | 0.719 | 0.017 | - | - | 0.921 | 0.936 | 0.304 | 1.29x | 19.9/29.9/35.7% | 3.1/6.7% | 3 |
| 60 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 90 | 1 | 0.779 | 0.772 | 0.007 | - | - | 0.958 | 0.958 | 0.267 | 1.72x | 14.5/22.4/27.3% | 1.5/5.2% | 3 |
| 120 | 1 | 0.729 | 0.718 | 0.011 | - | - | 0.970 | 0.974 | 0.197 | 2.21x | 14.0/28.1/34.4% | 1.4/5.3% | 3 |
| 150 | 1 | 0.709 | 0.704 | 0.006 | - | - | 0.962 | 0.963 | 0.287 | 2.77x | 15.4/27.2/34.7% | 1.4/5.5% | 3 |

> nodes=150: decode_failures 1

### `MS-stretch` - stretch  `--scenario alpine`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 1.25 | 1 | 0.572 | 0.560 | 0.011 | - | - | 0.821 | 0.822 | 0.000 | 1.33x | 12.3/17.5/21.0% | 1.9/5.0% | 3 |
| 1.5 | 1 | 0.399 | 0.393 | 0.005 | - | - | 0.654 | 0.655 | 0.000 | 1.41x | 10.8/15.2/18.3% | 2.2/5.2% | 3 |
| 2.0 | 1 | 0.172 | 0.172 | 0.000 | - | - | 0.107 | 0.215 | 0.000 | 0.94x | 5.0/7.6/9.8% | 1.6/3.0% | 2 |

> stretch=2.0: 3 archives requested, 2 placed - group on the placed count

### `MS-topology` - topology  `--scenario alpine`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| clustered | 1 | 0.903 | 0.901 | 0.003 | - | - | 0.962 | 0.963 | 0.613 | 1.16x | 23.1/30.8/33.0% | 1.6/5.3% | 3 |
| corridor | 1 | 0.659 | 0.639 | 0.021 | - | - | 0.931 | 0.953 | 0.140 | 1.38x | 15.2/22.1/27.5% | 2.1/5.4% | 3 |
| hub | 1 | 0.917 | 0.917 | 0.000 | - | - | 0.954 | 0.954 | 0.649 | 1.15x | 23.4/33.0/34.2% | 1.5/5.3% | 3 |

> topology=corridor: decode_failures 1

### `PR-crladder` - coding-rate-ladder  `--scenario alpine`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.800 | 0.800 | 0.000 | - | - | 0.958 | 0.961 | 0.323 | 1.61x | 19.5/29.9/32.4% | 2.2/6.3% | 3 |
| True | 1 | 0.795 | 0.795 | 0.000 | - | - | 0.955 | 0.958 | 0.300 | 1.59x | 19.0/29.4/32.1% | 2.2/6.3% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario alpine`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.795 | 0.795 | 0.000 | - | - | 0.955 | 0.958 | 0.300 | 1.59x | 19.0/29.4/32.1% | 2.2/6.3% | 3 |
| m4-early-flood | 1 | 0.785 | 0.785 | 0.000 | - | - | 0.955 | 0.958 | 0.295 | 1.60x | 19.4/29.6/32.3% | 2.2/6.3% | 3 |

### `PR-protocol` - protocol  `--scenario alpine`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.824 | 0.824 | 0.000 | - | - | 0 | 0.000 | 0.366 | 1.31x | 15.8/24.1/26.0% | 1.8/5.1% | 3 |
| chain | 1 | 0.807 | 0.805 | 0.002 | - | - | 0.910 | 0.967 | 0.311 | 1.54x | 18.6/28.6/30.6% | 2.1/6.0% | 3 |
| sr | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |

### `PR-repeats` - extra-repeats  `--scenario alpine`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| True | 1 | 0.824 | 0.819 | 0.005 | - | - | 0.971 | 0.971 | 0.343 | 1.35x | 16.3/25.0/26.8% | 1.9/5.3% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario alpine`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.952 | 0.949 | 0.003 | - | - | 0.997 | 0.999 | 0.773 | 2.02x | 23.3/32.8/37.0% | 1.3/5.1% | 3 |
| True | 1 | 0.953 | 0.950 | 0.003 | - | - | 0.997 | 0.999 | 0.795 | 2.07x | 23.8/33.3/37.5% | 1.3/5.2% | 3 |

### `RF-bw500` - preset  `--scenario alpine`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.210 | 0.205 | 0.005 | - | - | 0.313 | 0.464 | 0.000 | 0.05x | 0.3/0.5/0.7% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.431 | 0.419 | 0.012 | - | - | 0.435 | 0.627 | 0.000 | 0.24x | 1.6/2.7/4.6% | 0.4/1.0% | 3 |
| LONG_TURBO | 1 | 0.734 | 0.728 | 0.006 | - | - | 0.904 | 0.905 | 0.320 | 1.29x | 12.0/19.1/22.6% | 2.0/4.6% | 3 |

> preset=SHORT_TURBO: decode_failures 14

> preset=MEDIUM_TURBO: decode_failures 8

### `RF-duct` - duct-per-hour  `--scenario alpine`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 0.25 | 1 | 0.851 | 0.845 | 0.006 | - | - | 0.972 | 0.974 | 0.432 | 1.27x | 18.6/27.2/29.0% | 1.7/5.4% | 3 |
| 1.0 | 1 | 0.891 | 0.884 | 0.007 | - | - | 0.983 | 0.984 | 0.557 | 1.17x | 21.5/29.0/31.3% | 1.5/5.5% | 3 |

### `RF-eu-presets` - preset  `--scenario alpine`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.358 | 0.358 | 0.000 | - | - | 0.135 | 0.270 | 0.000 | 0.13x | 0.9/1.3/2.1% | 0.2/0.5% | 2 |
| LONG_FAST | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| LITE_FAST | 1 | 0.765 | 0.759 | 0.005 | - | - | 0.945 | 0.945 | 0.162 | 1.01x | 10.2/15.7/18.3% | 1.4/3.9% | 3 |
| NARROW_SLOW | 1 | 0.798 | 0.784 | 0.014 | - | - | 0.971 | 0.973 | 0.265 | 1.30x | 14.1/21.4/25.3% | 1.8/5.1% | 3 |

> preset=SHORT_FAST: 3 archives requested, 2 placed - group on the placed count

### `RF-noise` - noise-profile  `--scenario alpine`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| temporal | 1 | 0.728 | 0.718 | 0.010 | - | - | 0.940 | 0.941 | 0.120 | 1.32x | 15.9/24.1/26.0% | 1.9/5.1% | 3 |
| transient | 1 | 0.814 | 0.807 | 0.006 | - | - | 0.965 | 0.966 | 0.311 | 1.33x | 16.1/24.7/26.6% | 1.8/5.3% | 3 |
| periodic | 1 | 0.661 | 0.655 | 0.006 | - | - | 0.810 | 0.818 | 0.178 | 1.24x | 15.2/23.3/25.1% | 1.8/4.6% | 3 |

### `RF-preset` - preset  `--scenario alpine`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.358 | 0.358 | 0.000 | - | - | 0.135 | 0.270 | 0.000 | 0.13x | 0.9/1.3/2.1% | 0.2/0.5% | 2 |
| LONG_FAST | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| LONG_MODERATE | 1 | 0.830 | 0.789 | 0.041 | - | - | 0.971 | 0.978 | 0.542 | 3.36x | 43.0/61.2/65.0% | 5.0/12.2% | 3 |

> preset=SHORT_FAST: 3 archives requested, 2 placed - group on the placed count

> preset=LONG_MODERATE: decode_failures 4

> faster: 1.31 s per simulated hour against 2.87 over 55 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `RF-preset-turbo` - preset  `--scenario alpine`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.079 | 0.078 | 0.001 | - | - | 0.300 | 0.300 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.210 | 0.205 | 0.005 | - | - | 0.313 | 0.464 | 0.000 | 0.05x | 0.3/0.5/0.7% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| LONG_TURBO | 1 | 0.734 | 0.728 | 0.006 | - | - | 0.904 | 0.905 | 0.320 | 1.29x | 12.0/19.1/22.6% | 2.0/4.6% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.822 | 0.815 | 0.007 | - | - | 0.968 | 0.969 | 0.416 | 1.82x | 20.4/30.2/34.5% | 2.5/7.0% | 3 |

> preset=SHORT_TURBO: decode_failures 14

### `RF-pulse` - noise-pulse-interval-ms  `--scenario alpine`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.773 | 0.768 | 0.006 | - | - | 0.917 | 0.918 | 0.265 | 1.31x | 16.0/24.3/26.3% | 1.8/5.0% | 3 |
| 10000 | 1 | 0.661 | 0.655 | 0.006 | - | - | 0.810 | 0.818 | 0.178 | 1.24x | 15.2/23.3/25.1% | 1.8/4.6% | 3 |
| 4000 | 1 | 0.414 | 0.409 | 0.006 | - | - | 0.521 | 0.585 | 0.052 | 1.04x | 13.0/19.7/21.5% | 1.6/3.5% | 3 |
| 2000 | 1 | 0.099 | 0.099 | 0.000 | - | - | 0.113 | 0.206 | 0.012 | 0.73x | 9.4/13.5/15.0% | 1.2/1.9% | 3 |

### `RF-stretch-duct` - duct-per-hour  `--scenario alpine`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.399 | 0.393 | 0.005 | - | - | 0.654 | 0.655 | 0.000 | 1.41x | 10.8/15.2/18.3% | 2.2/5.2% | 3 |
| 1.0 | 1 | 0.634 | 0.623 | 0.011 | - | - | 0.810 | 0.815 | 0.356 | 1.11x | 11.8/16.6/20.8% | 1.6/4.6% | 3 |

### `RF-txpower` - tx-power  `--scenario alpine`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 22 | 1 | 0.408 | 0.402 | 0.006 | - | - | 0.441 | 0.610 | 0.000 | 1.38x | 9.9/14.6/23.3% | 2.3/5.3% | 3 |
| 17 | 1 | 0.198 | 0.192 | 0.006 | - | - | 0.329 | 0.466 | 0.000 | 1.03x | 5.5/9.3/13.0% | 1.6/3.6% | 3 |
| 14 | 1 | 0.108 | 0.108 | 0.000 | - | - | 0.018 | 0.026 | 0.000 | 0.71x | 3.5/7.0/9.6% | 1.0/3.0% | 3 |

> tx-power=22: decode_failures 11

> tx-power=17: decode_failures 14

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario alpine`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.952 | 0.949 | 0.003 | - | - | 0.997 | 0.999 | 0.773 | 2.02x | 23.3/32.8/37.0% | 1.3/5.1% | 3 |
| True | 1 | 0.941 | 0.937 | 0.004 | - | - | 0.996 | 0.997 | 0.763 | 2.44x | 27.6/37.8/42.2% | 1.6/5.9% | 3 |

### `RT-favourites` - favourite-routers  `--scenario alpine`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.826 | 0.819 | 0.007 | - | - | 0.971 | 0.971 | 0.326 | 1.37x | 16.7/25.6/28.6% | 1.8/5.2% | 3 |
| True | 1 | 0.857 | 0.851 | 0.006 | - | - | 0.969 | 0.970 | 0.393 | 1.49x | 18.2/26.9/30.3% | 2.0/5.3% | 3 |

### `RT-hopassign` - hop-assign  `--scenario alpine`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| random | 1 | 0.826 | 0.817 | 0.009 | - | - | 0.931 | 0.931 | 0.379 | 1.33x | 16.0/23.9/26.0% | 1.8/5.1% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario alpine`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.612 | 0.586 | 0.026 | - | - | 0.834 | 0.840 | 0.185 | 1.01x | 12.3/19.2/21.6% | 1.4/4.4% | 3 |
| 7 | 1 | 0.868 | 0.864 | 0.004 | - | - | 0.954 | 0.954 | 0.428 | 1.46x | 17.1/25.4/27.5% | 2.0/5.2% | 3 |
| 15 | 1 | 0.916 | 0.914 | 0.002 | - | - | 0.971 | 0.972 | 0.552 | 1.53x | 17.8/26.3/28.3% | 2.1/5.4% | 3 |
| 32 | 1 | 0.904 | 0.902 | 0.002 | - | - | 0.954 | 0.954 | 0.525 | 1.54x | 17.8/26.2/28.2% | 2.2/5.3% | 3 |

### `RT-hopspread` - hop-limit  `--scenario alpine`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.612 | 0.586 | 0.026 | - | - | 0.834 | 0.840 | 0.185 | 1.01x | 12.3/19.2/21.6% | 1.4/4.4% | 3 |
| 5 | 1 | 0.796 | 0.787 | 0.009 | - | - | 0.929 | 0.930 | 0.320 | 1.32x | 15.9/23.9/25.9% | 1.8/5.1% | 3 |
| 7 | 1 | 0.868 | 0.864 | 0.004 | - | - | 0.954 | 0.954 | 0.428 | 1.46x | 17.1/25.4/27.5% | 2.0/5.2% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario alpine`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| KNOWN_ONLY | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.825 | 0.825 | 0.000 | - | - | 0.918 | 0.971 | 0.333 | 1.31x | 15.9/24.2/26.0% | 1.8/5.0% | 3 |

> rebroadcast-mode=CORE_PORTNUMS_ONLY: decode_failures 3

### `RT-spread` - hop-spread  `--scenario alpine`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.612 | 0.586 | 0.026 | - | - | 0.834 | 0.840 | 0.185 | 1.01x | 12.3/19.2/21.6% | 1.4/4.4% | 3 |
| True | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |

### `SC-signing` - signature-policy  `--scenario alpine`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| BALANCED | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| STRICT | 1 | 0.724 | 0.724 | 0.000 | - | - | 0.881 | 0.883 | 0.256 | 1.48x | 17.8/27.1/29.0% | 2.0/5.7% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario alpine`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| dm | 1 | 0.830 | 0.825 | 0.005 | - | - | 0.975 | 0.977 | 0.327 | 1.32x | 16.0/24.8/26.7% | 1.8/5.5% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario alpine`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.826 | 0.821 | 0.006 | - | - | 0.968 | 0.969 | 0.318 | 1.36x | 16.3/25.2/27.1% | 1.8/5.4% | 3 |
| local | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| time | 1 | 0.823 | 0.818 | 0.005 | - | - | 0.969 | 0.972 | 0.324 | 1.37x | 16.6/25.5/27.5% | 1.9/5.5% | 3 |
| window | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.957 | 0.958 | 0.327 | 1.35x | 16.3/25.2/27.1% | 1.8/5.3% | 3 |

> bucket-mode=global: misdecodes 44

> bucket-mode=time: misdecodes 39

> bucket-mode=window: misdecodes 28

### `SF-bucket-time` - time-bucket-s  `--scenario alpine`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.812 | 0.804 | 0.007 | - | - | 0.957 | 0.958 | 0.329 | 1.49x | 17.8/27.7/30.1% | 2.0/6.2% | 3 |
| 1800 | 1 | 0.823 | 0.818 | 0.005 | - | - | 0.969 | 0.972 | 0.324 | 1.37x | 16.6/25.5/27.5% | 1.9/5.5% | 3 |
| 3600 | 1 | 0.826 | 0.820 | 0.006 | - | - | 0.973 | 0.978 | 0.307 | 1.35x | 16.4/25.1/27.0% | 1.9/5.4% | 3 |

> time-bucket-s=600: misdecodes 118

> time-bucket-s=1800: misdecodes 39

> time-bucket-s=3600: misdecodes 8

### `SF-cadence` - trigger  `--scenario alpine`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| interval | 1 | 0.808 | 0.801 | 0.007 | - | - | 0.952 | 0.961 | 0.311 | 1.76x | 20.9/32.5/35.3% | 2.5/7.4% | 3 |
| aimd | 1 | 0.826 | 0.825 | 0.001 | - | - | 0.929 | 0.977 | 0.330 | 1.37x | 16.4/25.2/27.1% | 1.9/5.3% | 3 |
| bucket+interval | 1 | 0.803 | 0.793 | 0.010 | - | - | 0.966 | 0.966 | 0.297 | 1.83x | 21.6/34.4/37.6% | 2.5/8.9% | 3 |

> trigger=interval: misdecodes 13

> trigger=aimd: misdecodes 4

> trigger=bucket+interval: misdecodes 20

### `SF-capacity` - capacity  `--scenario alpine`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.816 | 0.811 | 0.005 | - | - | 0.960 | 0.962 | 0.304 | 1.36x | 16.4/25.3/27.6% | 1.9/5.6% | 3 |
| 8 | 1 | 0.823 | 0.817 | 0.006 | - | - | 0.972 | 0.974 | 0.319 | 1.34x | 16.2/25.0/26.9% | 1.8/5.4% | 3 |
| 16 | 1 | 0.825 | 0.820 | 0.005 | - | - | 0.973 | 0.975 | 0.318 | 1.33x | 16.0/24.7/26.7% | 1.8/5.3% | 3 |
| 32 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 50 | 1 | 0.825 | 0.819 | 0.007 | - | - | 0.973 | 0.974 | 0.333 | 1.34x | 16.2/25.0/26.9% | 1.9/5.3% | 3 |

> capacity=4: decode_failures 102

> capacity=8: decode_failures 28

### `SF-capacity-local` - capacity  `--scenario alpine`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.816 | 0.811 | 0.005 | - | - | 0.960 | 0.962 | 0.304 | 1.36x | 16.4/25.3/27.6% | 1.9/5.6% | 3 |
| 8 | 1 | 0.823 | 0.817 | 0.006 | - | - | 0.972 | 0.974 | 0.319 | 1.34x | 16.2/25.0/26.9% | 1.8/5.4% | 3 |
| 16 | 1 | 0.825 | 0.820 | 0.005 | - | - | 0.973 | 0.975 | 0.318 | 1.33x | 16.0/24.7/26.7% | 1.8/5.3% | 3 |
| 32 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 50 | 1 | 0.825 | 0.819 | 0.007 | - | - | 0.973 | 0.974 | 0.333 | 1.34x | 16.2/25.0/26.9% | 1.9/5.3% | 3 |

> capacity=4: decode_failures 102

> capacity=8: decode_failures 28

### `SF-capacity-window` - capacity  `--scenario alpine`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.821 | 0.815 | 0.006 | - | - | 0.961 | 0.972 | 0.332 | 1.35x | 16.3/25.1/27.0% | 1.8/5.3% | 3 |
| 16 | 1 | 0.822 | 0.817 | 0.005 | - | - | 0.970 | 0.972 | 0.301 | 1.34x | 16.2/24.8/26.6% | 1.8/5.2% | 3 |
| 32 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.957 | 0.958 | 0.327 | 1.35x | 16.3/25.2/27.1% | 1.8/5.3% | 3 |

> capacity=8: misdecodes 31

> capacity=8: decode_failures 35

> capacity=16: misdecodes 23

> capacity=32: misdecodes 28

### `SF-catchup` - catch-up-hours  `--scenario alpine`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.803 | 0.793 | 0.010 | - | - | 0.966 | 0.966 | 0.297 | 1.83x | 21.6/34.4/37.6% | 2.5/8.9% | 3 |
| 02-06 | 1 | 0.819 | 0.815 | 0.004 | - | - | 0.941 | 0.969 | 0.320 | 1.37x | 16.5/25.5/27.7% | 1.9/5.6% | 3 |
| 00-08 | 1 | 0.822 | 0.818 | 0.004 | - | - | 0.947 | 0.969 | 0.309 | 1.42x | 17.1/26.5/28.8% | 1.9/6.0% | 3 |

> catch-up-hours=: misdecodes 20

> catch-up-hours=02-06: misdecodes 2

> catch-up-hours=02-06: decode_failures 16

> catch-up-hours=00-08: decode_failures 19

### `SF-hops-flat` - hops-apart  `--scenario alpine`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.823 | 0.820 | 0.003 | - | - | 0.951 | 0.951 | 0.308 | 1.36x | 16.5/25.2/27.1% | 1.9/5.3% | 3 |
| 2 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 3 | 1 | 0.846 | 0.823 | 0.024 | - | - | 0.954 | 0.983 | 0.334 | 1.34x | 16.0/24.6/26.5% | 1.8/5.1% | 3 |
| 4 | 1 | 0.842 | 0.817 | 0.024 | - | - | 0.871 | 0.971 | 0.411 | 1.34x | 16.2/24.7/26.6% | 1.8/5.1% | 3 |

> hops-apart=3: decode_failures 35

> hops-apart=4: decode_failures 18

### `SF-hops-spread` - hops-apart  `--scenario alpine`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.823 | 0.820 | 0.003 | - | - | 0.951 | 0.951 | 0.308 | 1.36x | 16.5/25.2/27.1% | 1.9/5.3% | 3 |
| 2 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 3 | 1 | 0.846 | 0.823 | 0.024 | - | - | 0.954 | 0.983 | 0.334 | 1.34x | 16.0/24.6/26.5% | 1.8/5.1% | 3 |
| 4 | 1 | 0.842 | 0.817 | 0.024 | - | - | 0.871 | 0.971 | 0.411 | 1.34x | 16.2/24.7/26.6% | 1.8/5.1% | 3 |
| 5 | 1 | 0.844 | 0.823 | 0.021 | - | - | 0.753 | 0.967 | 0.327 | 1.34x | 16.0/24.6/26.5% | 1.8/5.1% | 3 |

> hops-apart=3: decode_failures 35

> hops-apart=4: decode_failures 18

> hops-apart=5: decode_failures 34

### `SF-jitter-global` - advert-jitter-s  `--scenario alpine`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.826 | 0.821 | 0.005 | - | - | 0.974 | 0.975 | 0.328 | 1.34x | 16.2/24.9/26.8% | 1.8/5.3% | 3 |
| 30 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 120 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.969 | 0.970 | 0.306 | 1.34x | 16.2/25.0/26.9% | 1.8/5.4% | 3 |
| 600 | 1 | 0.827 | 0.821 | 0.006 | - | - | 0.975 | 0.977 | 0.318 | 1.35x | 16.4/25.2/27.1% | 1.9/5.4% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario alpine`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.826 | 0.821 | 0.005 | - | - | 0.974 | 0.975 | 0.328 | 1.34x | 16.2/24.9/26.8% | 1.8/5.3% | 3 |
| 30 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 120 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.969 | 0.970 | 0.306 | 1.34x | 16.2/25.0/26.9% | 1.8/5.4% | 3 |
| 600 | 1 | 0.827 | 0.821 | 0.006 | - | - | 0.975 | 0.977 | 0.318 | 1.35x | 16.4/25.2/27.1% | 1.9/5.4% | 3 |

### `SF-place-flat` - place  `--scenario alpine`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.844 | 0.814 | 0.031 | - | - | 0.898 | 0.961 | 0.323 | 1.38x | 16.5/25.3/27.3% | 1.9/5.1% | 3 |
| routers | 1 | 0.817 | 0.813 | 0.004 | - | - | 0.958 | 0.959 | 0.330 | 1.35x | 16.4/25.3/27.3% | 1.9/5.4% | 3 |
| alternate-routers | 1 | 0.822 | 0.820 | 0.002 | - | - | 0.953 | 0.953 | 0.350 | 1.35x | 16.4/25.2/27.1% | 1.9/5.3% | 3 |
| beside-router | 1 | 0.824 | 0.817 | 0.007 | - | - | 0.964 | 0.964 | 0.337 | 1.36x | 16.4/25.2/27.0% | 1.8/5.3% | 3 |
| random-clients | 1 | 0.823 | 0.809 | 0.014 | - | - | 0.904 | 0.970 | 0.342 | 1.37x | 16.4/25.0/26.7% | 1.9/5.2% | 3 |
| hops-apart | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |

> place=spread: decode_failures 31

> place=random-clients: decode_failures 41

### `SF-place-spread` - place  `--scenario alpine`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.844 | 0.814 | 0.031 | - | - | 0.898 | 0.961 | 0.323 | 1.38x | 16.5/25.3/27.3% | 1.9/5.1% | 3 |
| routers | 1 | 0.817 | 0.813 | 0.004 | - | - | 0.958 | 0.959 | 0.330 | 1.35x | 16.4/25.3/27.3% | 1.9/5.4% | 3 |
| alternate-routers | 1 | 0.822 | 0.820 | 0.002 | - | - | 0.953 | 0.953 | 0.350 | 1.35x | 16.4/25.2/27.1% | 1.9/5.3% | 3 |
| beside-router | 1 | 0.824 | 0.817 | 0.007 | - | - | 0.964 | 0.964 | 0.337 | 1.36x | 16.4/25.2/27.0% | 1.8/5.3% | 3 |
| random-clients | 1 | 0.823 | 0.809 | 0.014 | - | - | 0.904 | 0.970 | 0.342 | 1.37x | 16.4/25.0/26.7% | 1.9/5.2% | 3 |
| hops-apart | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |

> place=spread: decode_failures 31

> place=random-clients: decode_failures 41

### `SF-provide-transport` - provide-transport  `--scenario alpine`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| broadcast | 1 | 0.842 | 0.810 | 0.032 | - | - | 0.963 | 0.964 | 0.356 | 1.41x | 17.0/26.0/28.0% | 1.9/5.4% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario alpine`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| heard | 1 | 0.823 | 0.818 | 0.005 | - | - | 0.971 | 0.973 | 0.321 | 1.33x | 16.1/24.8/26.7% | 1.8/5.3% | 3 |

> replay-ordering=heard: misdecodes 28

### `SF-replay-order-broadcast` - replay-ordering  `--scenario alpine`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.842 | 0.810 | 0.032 | - | - | 0.963 | 0.964 | 0.356 | 1.41x | 17.0/26.0/28.0% | 1.9/5.4% | 3 |
| heard | 1 | 0.838 | 0.807 | 0.031 | - | - | 0.959 | 0.959 | 0.342 | 1.41x | 17.1/26.1/28.2% | 1.9/5.5% | 3 |

> replay-ordering=heard: misdecodes 10

### `SF-resolve` - resolve  `--scenario alpine`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| enum | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.968 | 0.971 | 0.308 | 1.36x | 16.4/25.6/27.5% | 1.8/5.6% | 3 |
| hybrid | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |

### `SF-servers-allrouters` - servers  `--scenario alpine`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.817 | 0.813 | 0.004 | - | - | 0.958 | 0.959 | 0.330 | 1.35x | 16.4/25.3/27.3% | 1.9/5.4% | 3 |
| 6 | 1 | 0.822 | 0.814 | 0.008 | - | - | 0.975 | 0.977 | 0.309 | 1.38x | 16.7/25.7/27.9% | 1.9/5.6% | 6 |

### `SF-servers-flat` - servers  `--scenario alpine`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.821 | 0.816 | 0.005 | - | - | 0.959 | 0.960 | 0.309 | 1.34x | 16.2/24.8/26.8% | 1.8/5.2% | 2 |
| 3 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 5 | 1 | 0.833 | 0.820 | 0.013 | - | - | 0.980 | 0.980 | 0.312 | 1.37x | 16.6/25.6/27.5% | 1.9/5.5% | 5 |
| 8 | 1 | 0.826 | 0.809 | 0.017 | - | - | 0.975 | 0.977 | 0.311 | 1.42x | 17.1/26.4/28.6% | 2.0/5.8% | 8 |

> servers=5: misdecodes 1

> servers=8: misdecodes 1

### `SF-servers-spread` - servers  `--scenario alpine`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.821 | 0.816 | 0.005 | - | - | 0.959 | 0.960 | 0.309 | 1.34x | 16.2/24.8/26.8% | 1.8/5.2% | 2 |
| 3 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 5 | 1 | 0.833 | 0.820 | 0.013 | - | - | 0.980 | 0.980 | 0.312 | 1.37x | 16.6/25.6/27.5% | 1.9/5.5% | 5 |
| 8 | 1 | 0.826 | 0.809 | 0.017 | - | - | 0.975 | 0.977 | 0.311 | 1.42x | 17.1/26.4/28.6% | 2.0/5.8% | 8 |

> servers=5: misdecodes 1

> servers=8: misdecodes 1

### `SF-signed` - signed  `--scenario alpine`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| True | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario alpine`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.841 | 0.836 | 0.005 | - | - | 0.982 | 0.984 | 0.353 | 1.24x | 15.0/22.9/24.6% | 1.7/4.8% | 3 |
| 1 | 1 | 0.828 | 0.821 | 0.007 | - | - | 0.964 | 0.964 | 0.317 | 1.24x | 14.9/23.0/24.8% | 1.7/4.8% | 3 |
| 2 | 1 | 0.836 | 0.829 | 0.006 | - | - | 0.974 | 0.976 | 0.344 | 1.25x | 15.0/22.9/24.6% | 1.7/4.9% | 3 |
| 4 | 1 | 0.828 | 0.821 | 0.006 | - | - | 0.975 | 0.978 | 0.327 | 1.23x | 14.8/22.7/24.4% | 1.7/4.8% | 3 |

### `SF-width` - short-id-bits  `--scenario alpine`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.821 | 0.816 | 0.005 | - | - | 0.965 | 0.966 | 0.316 | 1.34x | 16.2/24.9/26.8% | 1.8/5.3% | 3 |
| 24 | 1 | 0.825 | 0.819 | 0.006 | - | - | 0.974 | 0.975 | 0.323 | 1.35x | 16.4/25.2/27.2% | 1.8/5.4% | 3 |
| 32 | 1 | 0.822 | 0.816 | 0.006 | - | - | 0.970 | 0.972 | 0.309 | 1.35x | 16.2/25.0/27.0% | 1.8/5.3% | 3 |
| 64 | 1 | 0.828 | 0.823 | 0.005 | - | - | 0.968 | 0.969 | 0.311 | 1.33x | 16.1/24.7/26.5% | 1.8/5.2% | 3 |

### `SF-window-size` - window-size  `--scenario alpine`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.816 | 0.809 | 0.007 | - | - | 0.971 | 0.971 | 0.317 | 1.43x | 17.1/26.5/28.6% | 2.0/5.7% | 3 |
| 16 | 1 | 0.823 | 0.816 | 0.007 | - | - | 0.974 | 0.975 | 0.323 | 1.35x | 16.2/24.9/26.8% | 1.8/5.3% | 3 |
| 32 | 1 | 0.817 | 0.811 | 0.006 | - | - | 0.957 | 0.958 | 0.327 | 1.35x | 16.3/25.2/27.1% | 1.8/5.3% | 3 |

> window-size=8: misdecodes 136

> window-size=16: misdecodes 68

> window-size=32: misdecodes 28

### `TH-congestion` - no-congestion-scaling  `--scenario alpine`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.952 | 0.949 | 0.003 | - | - | 0.997 | 0.999 | 0.773 | 2.02x | 23.3/32.8/37.0% | 1.3/5.1% | 3 |
| True | 1 | 0.743 | 0.735 | 0.008 | - | - | 0.823 | 0.924 | 0.532 | 5.60x | 56.7/72.3/77.0% | 4.0/12.5% | 3 |

> no-congestion-scaling=True: decode_failures 56

### `TH-congestion-input` - congestion-input  `--scenario alpine`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.534 | 0.525 | 0.008 | - | - | 0.708 | 0.711 | 0.128 | 4.42x | 15.1/26.3/37.5% | 1.4/5.3% | 3 |
| truesize | 1 | 0.561 | 0.554 | 0.008 | - | - | 0.737 | 0.737 | 0.149 | 3.36x | 11.2/21.7/31.0% | 1.0/4.5% | 3 |

### `TH-congestion-mode` - congestion-mode  `--scenario alpine`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.955 | 0.952 | 0.003 | - | - | 1.000 | 1.000 | 0.785 | 1.91x | 22.0/31.0/34.9% | 1.3/4.9% | 3 |
| adaptive | 1 | 0.952 | 0.949 | 0.003 | - | - | 0.997 | 0.999 | 0.773 | 2.02x | 23.3/32.8/37.0% | 1.3/5.1% | 3 |

