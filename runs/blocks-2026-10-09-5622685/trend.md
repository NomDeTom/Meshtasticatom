# Sweep blocks-2026-10-09-5622685

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** alpine
- **seed base** 5622685 · seeds 5622685
- **blocks** 87 run
- **compute** 9.2 h of simulator time across every cell
- **generated** 2026-10-09T10:03:24+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>96 warnings</summary>

- AD-amplifiers: amplifier-mix=sprinkled: decode_failures 3
- AD-amplify-worst: faster: 0.903 s per simulated hour against 1.83 over 49 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- AD-siting: siting-mix=basement-heavy: 3 archives requested, 2 placed - group on the placed count
- AD-siting: faster: 0.699 s per simulated hour against 1.45 over 49 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- AD-worst: role-placement=degree: decode_failures 100
- AD-worst: role-placement=inverse: decode_failures 26
- AD-worst: slower: 16.9 s per simulated hour against 3.41 over 49 prior run(s) - 4.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- BL-control: protocol=sr: decode_failures 1
- DB-hotstore-stress: max-num-nodes=10: decode_failures 47
- DB-hotstore-stress: max-num-nodes=120: decode_failures 89
- DB-hotstore-stress: max-num-nodes=250: decode_failures 27
- DB-warm: warm-num-nodes=0: decode_failures 23
- DB-warm: warm-num-nodes=25: decode_failures 23
- DB-warm: warm-num-nodes=100: decode_failures 23
- DB-warm: warm-num-nodes=2000: decode_failures 23
- DG-burst: burst-loss=0.3: decode_failures 12
- DG-burst: faster: 2.39 s per simulated hour against 5.11 over 49 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- DG-outage: burst-loss=0.1: decode_failures 27
- DG-outage: burst-loss=0.2: decode_failures 49
- DG-outage: burst-loss=0.3: decode_failures 27
- DM-mode: faster: 1.36 s per simulated hour against 3.22 over 49 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- FW-mixed-26: legacy-fraction=0.25: decode_failures 3
- FW-mixed-26: legacy-fraction=0.75: decode_failures 1
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 5
- LD-chatty: broadcast-interval-s=300: decode_failures 7
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 23
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 81
- LD-traceroute-small: faster: 17.4 s per simulated hour against 37.7 over 49 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-density: nodes=150: misdecodes 1
- MS-hopscale: nodes=250: decode_failures 63
- MS-hopscale: nodes=500: decode_failures 16
- MS-oversubscribed: nodes=250: decode_failures 89
- MS-oversubscribed: nodes=500: decode_failures 7
- MS-roles-fav: faster: 0.865 s per simulated hour against 1.75 over 49 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-siting: faster: 0.894 s per simulated hour against 1.89 over 48 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-stretch: stretch=1.5: decode_failures 1
- MS-stretch: faster: 0.924 s per simulated hour against 2.18 over 49 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-topology: topology=corridor: decode_failures 34
- RF-bw500: preset=SHORT_TURBO: decode_failures 2
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 12
- RF-eu-presets: preset=SHORT_FAST: decode_failures 8
- RF-eu-presets: preset=LITE_FAST: decode_failures 11
- RF-preset: preset=SHORT_FAST: decode_failures 8
- RF-preset: preset=LONG_MODERATE: decode_failures 23
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 2
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 2
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 1
- RF-txpower: tx-power=22: decode_failures 5
- RF-txpower: tx-power=14: decode_failures 2
- RT-rebroadcast: rebroadcast-mode=CORE_PORTNUMS_ONLY: decode_failures 5
- SF-bucket-mode: bucket-mode=global: misdecodes 36
- SF-bucket-mode: bucket-mode=time: misdecodes 39
- SF-bucket-mode: bucket-mode=window: misdecodes 28
- SF-bucket-time: time-bucket-s=600: misdecodes 137
- SF-bucket-time: time-bucket-s=1800: misdecodes 39
- SF-bucket-time: time-bucket-s=3600: misdecodes 17
- SF-cadence: trigger=interval: misdecodes 25
- SF-cadence: trigger=interval: decode_failures 1
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=aimd: decode_failures 3
- SF-cadence: trigger=bucket+interval: misdecodes 24
- SF-capacity-local: capacity=4: decode_failures 68
- SF-capacity-local: capacity=8: decode_failures 25
- SF-capacity: capacity=4: decode_failures 68
- SF-capacity: capacity=8: decode_failures 25
- SF-capacity-window: capacity=8: misdecodes 22
- SF-capacity-window: capacity=8: decode_failures 14
- SF-capacity-window: capacity=16: misdecodes 37
- SF-capacity-window: capacity=32: misdecodes 28
- SF-catchup: catch-up-hours=: misdecodes 24
- SF-catchup: catch-up-hours=02-06: decode_failures 39
- SF-catchup: catch-up-hours=00-08: decode_failures 36
- SF-hops-flat: hops-apart=3: decode_failures 1
- SF-hops-flat: hops-apart=4: decode_failures 36
- SF-hops-spread: hops-apart=3: decode_failures 1
- SF-hops-spread: hops-apart=4: decode_failures 36
- SF-hops-spread: hops-apart=5: decode_failures 38
- SF-place-flat: place=spread: decode_failures 17
- SF-place-flat: place=routers: decode_failures 2
- SF-place-flat: place=alternate-routers: decode_failures 8
- SF-place-flat: place=random-clients: decode_failures 26
- SF-place-spread: place=spread: decode_failures 17
- SF-place-spread: place=routers: decode_failures 2
- SF-place-spread: place=alternate-routers: decode_failures 8
- SF-place-spread: place=random-clients: decode_failures 26
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 13
- SF-replay-order: replay-ordering=heard: misdecodes 23
- SF-servers-allrouters: servers=3: decode_failures 2
- SF-sr-retries: faster: 0.753 s per simulated hour against 1.57 over 49 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- SF-window-size: window-size=8: misdecodes 90
- SF-window-size: window-size=16: misdecodes 47
- SF-window-size: window-size=32: misdecodes 28
- TH-congestion-input: congestion-input=hotstore: decode_failures 89
- TH-congestion-input: congestion-input=truesize: decode_failures 62
- TH-congestion-input: slower: 27.7 s per simulated hour against 11.2 over 49 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- TH-congestion: no-congestion-scaling=True: decode_failures 31

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `AD-worst` | 16.9 | 3.41 | 4.94x | 49 |
| `TH-congestion-input` | 27.7 | 11.2 | 2.48x | 49 |
| `MS-topology` | 3.84 | 1.93 | 1.99x | 49 |
| `RF-eu-presets` | 3.29 | 1.85 | 1.78x | 49 |
| `SF-place-flat` | 4.59 | 2.86 | 1.60x | 49 |
| `PR-crladder` | 1.87 | 2.79 | 0.67x | 49 |
| `RF-preset-turbo` | 1 | 1.53 | 0.65x | 45 |
| `SF-capacity-window` | 1.03 | 1.6 | 0.64x | 49 |
| `TH-congestion` | 10.9 | 17 | 0.64x | 49 |
| `SF-replay-order` | 0.999 | 1.59 | 0.63x | 49 |
| `LD-chatty-hops` | 2.5 | 4.19 | 0.60x | 49 |
| `RT-adopt` | 2.36 | 3.98 | 0.59x | 49 |
| `DB-warm` | 19.8 | 33.5 | 0.59x | 49 |
| `SF-bucket-time` | 0.94 | 1.61 | 0.58x | 49 |
| `SF-resolve` | 0.888 | 1.54 | 0.58x | 49 |
| `LD-chatty` | 2.81 | 4.97 | 0.57x | 49 |
| `DB-hotstore` | 1.31 | 2.37 | 0.55x | 49 |
| `RF-noise` | 2.63 | 4.91 | 0.54x | 49 |
| `FW-signing-cost` | 0.85 | 1.6 | 0.53x | 49 |
| `PR-dmmode-cr` | 1.38 | 2.6 | 0.53x | 49 |
| `SF-jitter-global` | 0.94 | 1.77 | 0.53x | 49 |
| `AD-amplify-worst` | 0.903 | 1.83 | 0.49x | 49 |
| `MS-roles-fav` | 0.865 | 1.75 | 0.49x | 49 |
| `AD-siting` | 0.699 | 1.45 | 0.48x | 49 |
| `SF-sr-retries` | 0.753 | 1.57 | 0.48x | 49 |
| `MS-siting` | 0.894 | 1.89 | 0.47x | 48 |
| `DG-burst` | 2.39 | 5.11 | 0.47x | 49 |
| `LD-traceroute-small` | 17.4 | 37.7 | 0.46x | 49 |
| `DM-mode` | 1.36 | 3.22 | 0.42x | 49 |
| `MS-stretch` | 0.924 | 2.18 | 0.42x | 49 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.963 | 0.963 | 0.765 → 0.773 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.930 | 0.930 | 0.763 → 0.765 | 1.2x bytes_on_air | up | 3 |
| `MS-siting` | siting-mix | **text** | 0.073 → 0.972 | 0.898 | 0.072 → 0.969 | 6.3x sr_airtime | up | 4 |
| `AD-siting` | siting-mix | **held** | 0.137 → 0.922 | 0.785 | 0.093 → 0.734 | 33x sr_bytes | down | 3 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.137 → 0.900 | 0.763 | 0.100 → 0.730 | 89x sr_airtime | down | 4 |
| `RF-preset-turbo` | preset | **held** | 0.190 → 0.935 | 0.745 | 0.051 → 0.771 | 5.2x advert_bytes | up | 5 |
| `MS-stretch` | stretch | **held** | 0.204 → 0.930 | 0.726 | 0.090 → 0.763 | 4.7x advert_bytes | down | 4 |
| `RF-txpower` | tx-power | **text** | 0.068 → 0.775 | 0.707 | 0.068 → 0.763 | 4.5x sr_airtime | down | 4 |
| `RF-eu-presets` | preset | **held** | 0.339 → 0.930 | 0.591 | 0.253 → 0.763 | 7.4x sr_airtime | up | 4 |
| `RF-preset` | preset | **held** | 0.339 → 0.930 | 0.591 | 0.253 → 0.770 | 11x sr_airtime | up | 3 |
| `RF-bw500` | preset | **text** | 0.133 → 0.680 | 0.547 | 0.128 → 0.666 | 2.6x advert_bytes | up | 3 |
| `MS-hopscale` | nodes | **held** | 0.469 → 0.930 | 0.461 | 0.316 → 0.763 | 11x sr_bytes | down | 4 |
| `MS-topology` | topology | **text** | 0.505 → 0.928 | 0.423 | 0.495 → 0.927 | 3.1x sr_bytes | up | 4 |
| `MS-density` | nodes | **text** | 0.540 → 0.956 | 0.416 | 0.531 → 0.953 | 5.2x sr_airtime | up | 5 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.284 → 0.659 | 0.375 | 0.281 → 0.649 | 2.4x sr_airtime | up | 2 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.532 → 0.883 | 0.352 | 0.519 → 0.881 | 8.6x sr_airtime | down | 3 |
| `MS-oversubscribed` | nodes | **held** | 0.463 → 0.789 | 0.326 | 0.316 → 0.626 | 4.5x bytes_on_air | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.456 → 0.775 | 0.318 | 0.434 → 0.763 | 2.7x sr_bytes | down | 4 |
| `RT-hoplimit` | hop-limit | **text** | 0.590 → 0.895 | 0.305 | 0.554 → 0.894 | 2x sr_bytes | up | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.459 → 0.746 | 0.287 | 0.308 → 0.486 | 5.9x sr_airtime | up | 3 |
| `DG-burst` | burst-loss | **text** | 0.499 → 0.775 | 0.276 | 0.459 → 0.763 | 2.5x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.535 → 0.809 | 0.274 | 0.508 → 0.801 | 7.4x sr_airtime | down | 3 |
| `RT-hopspread` | hop-limit | **text** | 0.590 → 0.849 | 0.259 | 0.554 → 0.846 | 1.8x sr_bytes | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.590 → 0.775 | 0.185 | 0.554 → 0.763 | 1.7x sr_bytes | up | 2 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.743 → 0.926 | 0.183 | 0.724 → 0.919 | 4.2x sr_airtime | down | 2 |
| `MS-size` | nodes | **text** | 0.634 → 0.804 | 0.171 | 0.623 → 0.787 | 3.8x sr_bytes | down | 5 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.775 → 0.926 | 0.152 | 0.763 → 0.920 | 1.8x sr_bytes | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.775 → 0.922 | 0.147 | 0.763 → 0.913 | 1.5x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **held** | 0.783 → 0.930 | 0.146 | 0.617 → 0.763 | 1.4x sr_bytes | down | 4 |
| `DG-loss` | extra-loss | **text** | 0.643 → 0.775 | 0.131 | 0.622 → 0.763 | 1.5x sr_bytes | down | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.775 → 0.901 | 0.127 | 0.763 → 0.895 | 1.3x sr_bytes | up | 3 |
| `SC-signing` | signature-policy | **text** | 0.671 → 0.775 | 0.103 | 0.671 → 0.763 | 1.3x sr_airtime | down | 3 |
| `AD-flooding` | role-mix | **text** | 0.753 → 0.856 | 0.103 | 0.734 → 0.846 | 2.2x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.753 → 0.856 | 0.103 | 0.734 → 0.846 | 2.2x bytes_on_air | up | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.733 → 0.833 | 0.100 | 0.716 → 0.826 | 5.8x sr_airtime | up | 4 |
| `DB-hotstore` | max-num-nodes | **text** | 0.746 → 0.844 | 0.097 | 0.735 → 0.837 | 2.1x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.747 → 0.844 | 0.096 | 0.735 → 0.837 | 2.2x sr_airtime | down | 3 |
| `FW-versions` | profile | **text** | 0.775 → 0.859 | 0.084 | 0.763 → 0.845 | 3.2x bytes_on_air | down | 5 |
| `FW-mixed` | legacy-fraction | **held** | 0.888 → 0.971 | 0.083 | 0.753 → 0.789 | 2.1x sr_bytes | up | 4 |
| `FW-mixed-26` | legacy-fraction | **held** | 0.900 → 0.974 | 0.074 | 0.760 → 0.798 | 2.5x sr_bytes | up | 4 |
| `FW-firmware` | profile | **text** | 0.775 → 0.846 | 0.071 | 0.763 → 0.830 | 3.1x bytes_on_air | down | 2 |
| `SF-hops-spread` | hops-apart | **held** | 0.897 → 0.963 | 0.066 | 0.763 → 0.778 | 3.7x sr_bytes | down | 5 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.837 → 0.901 | 0.064 | 0.672 → 0.717 | 1.4x sr_airtime | down | 2 |
| `SF-place-flat` | place | **held** | 0.909 → 0.972 | 0.063 | 0.763 → 0.779 | 3.4x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.909 → 0.972 | 0.063 | 0.763 → 0.779 | 3.4x sr_bytes | up | 6 |
| `SF-hops-flat` | hops-apart | **held** | 0.901 → 0.963 | 0.062 | 0.763 → 0.778 | 3.3x sr_bytes | up | 4 |
| `TH-congestion-input` | congestion-input | **held** | 0.717 → 0.775 | 0.058 | 0.483 → 0.512 | 1.6x sr_airtime | up | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.775 → 0.825 | 0.051 | 0.763 → 0.819 | 3.4x bytes_on_air | down | 2 |
| `SF-servers-flat` | servers | **held** | 0.930 → 0.977 | 0.047 | 0.763 → 0.776 | 7.6x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.930 → 0.977 | 0.047 | 0.763 → 0.776 | 7.6x sr_bytes | up | 4 |
| `AD-badrouters` | role-placement | **held** | 0.877 → 0.922 | 0.045 | 0.693 → 0.734 | 1.3x sr_bytes | down | 3 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.892 → 0.930 | 0.038 | 0.763 → 0.778 | 18x sr_airtime | down | 3 |
| `SF-provide-transport` | provide-transport | **text** | 0.775 → 0.812 | 0.037 | 0.763 → 0.771 | 2.7x sr_airtime | up | 2 |
| `AD-worst` | role-placement | **held** | 0.842 → 0.876 | 0.035 | 0.651 → 0.682 | 1.1x sr_airtime | up | 2 |
| `RT-hopassign` | hop-assign | **text** | 0.742 → 0.775 | 0.033 | 0.730 → 0.763 | 1.4x sr_bytes | down | 2 |
| `MS-router-late` | router-late-fraction | **text** | 0.775 → 0.806 | 0.031 | 0.763 → 0.797 | 1.3x bytes_on_air | up | 4 |
| `RT-favourites` | favourite-routers | **text** | 0.806 → 0.836 | 0.030 | 0.797 → 0.829 | 1.1x sr_bytes | up | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.749 → 0.779 | 0.030 | 0.732 → 0.769 | 1.4x sr_airtime | down | 4 |
| `MS-roles` | role-mix | **text** | 0.753 → 0.782 | 0.029 | 0.734 → 0.770 | 1.3x sr_bytes | down | 2 |
| `LD-diurnal` | diurnal | **text** | 0.775 → 0.800 | 0.025 | 0.763 → 0.789 | 1.2x sr_bytes | down | 3 |
| `SF-resolve` | resolve | **held** | 0.930 → 0.954 | 0.024 | 0.763 → 0.784 | 5.6x advert_bytes | = | 3 |
| `MS-roles-fav` | role-mix | **held** | 0.907 → 0.931 | 0.024 | 0.782 → 0.793 | 1.2x sr_airtime | down | 2 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.930 → 0.953 | 0.024 | 0.763 → 0.778 | 1.1x sr_airtime | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.930 → 0.953 | 0.024 | 0.763 → 0.778 | 1.1x sr_airtime | down | 4 |
| `SF-capacity` | capacity | **text** | 0.775 → 0.797 | 0.022 | 0.763 → 0.785 | 5.1x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **text** | 0.775 → 0.797 | 0.022 | 0.763 → 0.785 | 5.1x advert_bytes | down | 5 |
| `SF-cadence` | trigger | **held** | 0.908 → 0.930 | 0.022 | 0.749 → 0.779 | 16x sr_bytes | down | 4 |
| `SF-advert-transport` | advert-transport | **held** | 0.930 → 0.950 | 0.020 | 0.763 → 0.781 | 3x sr_airtime | up | 2 |
| `SF-catchup` | catch-up-hours | **text** | 0.766 → 0.785 | 0.020 | 0.749 → 0.777 | 9.5x advert_bytes | up | 3 |
| `SF-width` | short-id-bits | **held** | 0.930 → 0.949 | 0.019 | 0.763 → 0.779 | 3x advert_bytes | down | 4 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.925 → 0.945 | 0.019 | 0.757 → 0.775 | 5.3x advert_bytes | up | 3 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.930 → 0.948 | 0.019 | 0.763 → 0.771 | 3x advert_bytes | up | 4 |
| `PR-repeats` | extra-repeats | **text** | 0.775 → 0.791 | 0.016 | 0.763 → 0.781 | 1.1x sr_bytes | up | 2 |
| `SF-servers-allrouters` | servers | **text** | 0.808 → 0.823 | 0.015 | 0.770 → 0.774 | 2.4x sr_bytes | up | 2 |
| `SF-window-size` | window-size | **text** | 0.772 → 0.787 | 0.014 | 0.760 → 0.779 | 4.8x advert_bytes | up | 3 |
| `SF-capacity-window` | capacity | **text** | 0.779 → 0.793 | 0.014 | 0.767 → 0.780 | 2x advert_bytes | down | 3 |
| `DM-mode` | dm-mode | **text** | 0.746 → 0.757 | 0.012 | 0.746 → 0.757 | 1.3x sr_airtime | up | 3 |
| `SF-sr-retries` | sr-retries | **held** | 0.938 → 0.948 | 0.011 | 0.773 → 0.777 | 1.1x sr_bytes | down | 4 |
| `SF-replay-order` | replay-ordering | **held** | 0.930 → 0.939 | 0.009 | 0.763 → 0.770 | 1.2x sr_bytes | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.917 → 0.926 | 0.009 | 0.909 → 0.919 | 1.2x sr_airtime | down | 2 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.751 → 0.758 | 0.006 | 0.751 → 0.758 | 1.1x sr_airtime | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.939 → 0.945 | 0.006 | 0.771 → 0.771 | 1.1x sr_bytes | down | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.993 → 0.996 | 0.003 | 0.919 → 0.921 | 1x sr_airtime | up | 2 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.755 → 0.758 | 0.003 | 0.755 → 0.758 | 1.2x sr_airtime | down | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.926 → 0.928 | 0.002 | 0.919 → 0.921 | 1x advert_bytes | down | 2 |

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
| none | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| sprinkled | 1 | 0.823 | 0.810 | 0.013 | - | - | 0.962 | 0.968 | 0.370 | 1.25x | 16.4/21.4/24.7% | 1.7/5.4% | 3 |
| arms-race | 1 | 0.926 | 0.920 | 0.007 | - | - | 0.978 | 0.979 | 0.791 | 1.09x | 18.8/24.1/26.5% | 1.3/5.2% | 3 |

> amplifier-mix=sprinkled: decode_failures 3

### `AD-amplify-worst` - amplify-worst  `--scenario alpine`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 0.1 | 1 | 0.839 | 0.824 | 0.015 | - | - | 0.954 | 0.954 | 0.491 | 1.28x | 16.5/21.8/24.1% | 2.0/4.8% | 3 |
| 0.3 | 1 | 0.922 | 0.913 | 0.009 | - | - | 0.983 | 0.984 | 0.814 | 1.12x | 17.8/24.7/26.6% | 1.5/4.8% | 3 |

> faster: 0.903 s per simulated hour against 1.83 over 49 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `AD-badrouters` - role-placement  `--scenario alpine`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.753 | 0.734 | 0.020 | - | - | 0.922 | 0.922 | 0.307 | 1.15x | 14.0/20.5/23.3% | 2.1/5.0% | 3 |
| inverse | 1 | 0.718 | 0.693 | 0.024 | - | - | 0.877 | 0.879 | 0.292 | 1.13x | 13.0/17.7/21.8% | 2.0/4.0% | 3 |
| random | 1 | 0.724 | 0.709 | 0.014 | - | - | 0.918 | 0.919 | 0.291 | 1.13x | 12.9/20.3/22.8% | 1.9/4.9% | 3 |

### `AD-flooding` - role-mix  `--scenario alpine`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.753 | 0.734 | 0.020 | - | - | 0.922 | 0.922 | 0.307 | 1.15x | 14.0/20.5/23.3% | 2.1/5.0% | 3 |
| all-routers | 1 | 0.856 | 0.846 | 0.010 | - | - | 0.962 | 0.964 | 0.461 | 2.57x | 29.3/35.2/38.9% | 4.2/5.1% | 3 |

### `AD-nomute` - role-mix  `--scenario alpine`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.753 | 0.734 | 0.020 | - | - | 0.922 | 0.922 | 0.307 | 1.15x | 14.0/20.5/23.3% | 2.1/5.0% | 3 |
| no-mute | 1 | 0.783 | 0.769 | 0.014 | - | - | 0.919 | 0.920 | 0.361 | 1.28x | 15.7/22.1/26.1% | 2.0/5.0% | 3 |
| all-routers | 1 | 0.856 | 0.846 | 0.010 | - | - | 0.962 | 0.964 | 0.461 | 2.57x | 29.3/35.2/38.9% | 4.2/5.1% | 3 |

### `AD-siting` - siting-mix  `--scenario alpine`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.753 | 0.734 | 0.020 | - | - | 0.922 | 0.922 | 0.307 | 1.15x | 14.0/20.5/23.3% | 2.1/5.0% | 3 |
| local-typical | 1 | 0.406 | 0.395 | 0.011 | - | - | 0.621 | 0.624 | 0.000 | 1.03x | 7.8/20.7/23.7% | 1.5/4.8% | 3 |
| basement-heavy | 1 | 0.093 | 0.093 | 0.000 | - | - | 0.137 | 0.274 | 0.000 | 0.67x | 1.6/9.1/15.9% | 0.3/3.5% | 2 |

> siting-mix=basement-heavy: 3 archives requested, 2 placed - group on the placed count

> faster: 0.699 s per simulated hour against 1.45 over 49 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `AD-worst` - role-placement  `--scenario alpine`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.695 | 0.682 | 0.012 | - | - | 0.842 | 0.866 | 0.000 | 2.27x | 14.6/25.1/32.7% | 1.8/5.7% | 3 |
| inverse | 1 | 0.674 | 0.651 | 0.022 | - | - | 0.876 | 0.884 | 0.000 | 2.20x | 13.3/21.2/29.0% | 1.7/3.4% | 3 |

> role-placement=degree: decode_failures 100

> role-placement=inverse: decode_failures 26

> slower: 16.9 s per simulated hour against 3.41 over 49 prior run(s) - 4.9x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `BL-control` - protocol  `--scenario alpine`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.765 | 0.765 | 0.000 | - | - | 0 | 0.000 | 0.317 | 1.22x | 14.8/20.7/24.0% | 1.9/4.9% | 3 |
| sr | 1 | 0.813 | 0.773 | 0.039 | - | - | 0.963 | 0.982 | 0.334 | 1.27x | 15.5/21.5/24.9% | 2.0/5.3% | 3 |

> protocol=sr: decode_failures 1

### `DB-hotstore` - max-num-nodes  `--scenario alpine`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.746 | 0.735 | 0.012 | - | - | 0.868 | 0.870 | 0.224 | 2.76x | 33.3/48.4/55.7% | 4.0/9.4% | 3 |
| 100 | 1 | 0.844 | 0.837 | 0.007 | - | - | 0.949 | 0.949 | 0.288 | 1.44x | 17.6/26.1/30.7% | 2.1/5.2% | 3 |
| 120 | 1 | 0.844 | 0.837 | 0.007 | - | - | 0.949 | 0.949 | 0.288 | 1.44x | 17.6/26.1/30.7% | 2.1/5.2% | 3 |
| 250 | 1 | 0.844 | 0.837 | 0.007 | - | - | 0.949 | 0.949 | 0.288 | 1.44x | 17.6/26.1/30.7% | 2.1/5.2% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario alpine`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.319 | 0.308 | 0.011 | - | - | 0.459 | 0.552 | 0.153 | 11.14x | 40.8/51.3/60.9% | 4.0/10.2% | 3 |
| 120 | 1 | 0.501 | 0.483 | 0.018 | - | - | 0.717 | 0.752 | 0.230 | 4.27x | 16.4/21.9/26.1% | 1.5/4.5% | 3 |
| 250 | 1 | 0.505 | 0.486 | 0.019 | - | - | 0.746 | 0.764 | 0.231 | 4.20x | 16.0/21.5/25.3% | 1.5/4.5% | 3 |

> max-num-nodes=10: decode_failures 47

> max-num-nodes=120: decode_failures 89

> max-num-nodes=250: decode_failures 27

### `DB-platform` - platform-mix  `--scenario alpine`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.844 | 0.837 | 0.007 | - | - | 0.949 | 0.949 | 0.288 | 1.44x | 17.6/26.1/30.7% | 2.1/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.844 | 0.837 | 0.007 | - | - | 0.949 | 0.949 | 0.288 | 1.44x | 17.6/26.1/30.7% | 2.1/5.2% | 3 |
| constrained | 1 | 0.747 | 0.735 | 0.013 | - | - | 0.868 | 0.868 | 0.225 | 2.76x | 33.3/48.5/55.8% | 4.0/9.4% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario alpine`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.737 | 0.717 | 0.020 | - | - | 0.901 | 0.924 | 0.495 | 5.47x | 54.3/67.7/75.5% | 4.0/12.1% | 3 |
| 25 | 1 | 0.737 | 0.717 | 0.020 | - | - | 0.901 | 0.924 | 0.495 | 5.47x | 54.3/67.7/75.5% | 4.0/12.1% | 3 |
| 100 | 1 | 0.737 | 0.717 | 0.020 | - | - | 0.901 | 0.924 | 0.495 | 5.47x | 54.3/67.7/75.5% | 4.0/12.1% | 3 |
| 2000 | 1 | 0.737 | 0.717 | 0.020 | - | - | 0.901 | 0.924 | 0.495 | 5.47x | 54.3/67.7/75.5% | 4.0/12.1% | 3 |

> warm-num-nodes=0: decode_failures 23

> warm-num-nodes=25: decode_failures 23

> warm-num-nodes=100: decode_failures 23

> warm-num-nodes=2000: decode_failures 23

### `DG-burst` - burst-loss  `--scenario alpine`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 0.1 | 1 | 0.692 | 0.673 | 0.019 | - | - | 0.907 | 0.911 | 0.236 | 1.19x | 14.5/20.9/24.2% | 1.9/4.7% | 3 |
| 0.2 | 1 | 0.591 | 0.558 | 0.033 | - | - | 0.860 | 0.878 | 0.167 | 1.09x | 13.6/19.7/22.9% | 1.8/4.2% | 3 |
| 0.3 | 1 | 0.499 | 0.459 | 0.040 | - | - | 0.780 | 0.806 | 0.120 | 1.01x | 12.6/18.5/21.7% | 1.6/3.7% | 3 |

> burst-loss=0.3: decode_failures 12

> faster: 2.39 s per simulated hour against 5.11 over 49 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `DG-loss` - extra-loss  `--scenario alpine`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 0.1 | 1 | 0.748 | 0.734 | 0.015 | - | - | 0.921 | 0.921 | 0.253 | 1.30x | 15.8/22.5/25.9% | 2.0/5.0% | 3 |
| 0.2 | 1 | 0.712 | 0.694 | 0.018 | - | - | 0.909 | 0.911 | 0.193 | 1.33x | 16.4/22.7/26.5% | 2.1/4.8% | 3 |
| 0.3 | 1 | 0.643 | 0.622 | 0.022 | - | - | 0.847 | 0.851 | 0.147 | 1.35x | 16.9/23.4/27.4% | 2.1/4.6% | 3 |

### `DG-outage` - burst-loss  `--scenario alpine`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 0.1 | 1 | 0.678 | 0.661 | 0.017 | - | - | 0.889 | 0.921 | 0.240 | 1.19x | 14.7/20.9/24.1% | 1.9/4.8% | 3 |
| 0.2 | 1 | 0.581 | 0.557 | 0.024 | - | - | 0.839 | 0.882 | 0.160 | 1.10x | 13.6/19.9/23.0% | 1.7/4.5% | 3 |
| 0.3 | 1 | 0.456 | 0.434 | 0.023 | - | - | 0.694 | 0.803 | 0.141 | 1.04x | 13.0/19.1/22.5% | 1.6/4.0% | 3 |

> burst-loss=0.1: decode_failures 27

> burst-loss=0.2: decode_failures 49

> burst-loss=0.3: decode_failures 27

### `DM-mode` - dm-mode  `--scenario alpine`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.746 | 0.746 | 0.000 | - | - | 0.925 | 0.926 | 0.287 | 1.60x | 19.3/27.7/31.7% | 2.5/6.5% | 3 |
| directed-with-late-flood | 1 | 0.751 | 0.751 | 0.000 | - | - | 0.930 | 0.932 | 0.322 | 1.46x | 17.7/25.6/29.4% | 2.2/6.1% | 3 |
| m4-early-flood | 1 | 0.757 | 0.757 | 0.000 | - | - | 0.927 | 0.930 | 0.301 | 1.47x | 17.9/25.8/29.6% | 2.3/6.2% | 3 |

> faster: 1.36 s per simulated hour against 3.22 over 49 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `FW-firmware` - profile  `--scenario alpine`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.846 | 0.830 | 0.015 | - | - | 0.963 | 0.966 | 0.526 | 0.72x | 8.3/10.3/12.1% | 1.2/2.0% | 3 |
| 2.8 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario alpine`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 0.25 | 1 | 0.782 | 0.753 | 0.029 | - | - | 0.888 | 0.898 | 0.559 | 1.14x | 13.1/16.4/19.2% | 1.8/3.9% | 3 |
| 0.5 | 1 | 0.809 | 0.789 | 0.021 | - | - | 0.957 | 0.967 | 0.539 | 0.96x | 11.9/16.9/18.8% | 1.6/3.8% | 3 |
| 0.75 | 1 | 0.803 | 0.784 | 0.018 | - | - | 0.971 | 0.973 | 0.387 | 0.87x | 10.4/13.6/16.5% | 1.2/3.3% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario alpine`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 0.25 | 1 | 0.791 | 0.760 | 0.031 | - | - | 0.900 | 0.901 | 0.575 | 1.11x | 13.0/16.4/18.3% | 1.7/3.8% | 3 |
| 0.5 | 1 | 0.819 | 0.798 | 0.021 | - | - | 0.965 | 0.971 | 0.555 | 0.97x | 11.7/17.1/18.8% | 1.6/3.8% | 3 |
| 0.75 | 1 | 0.802 | 0.782 | 0.020 | - | - | 0.974 | 0.976 | 0.382 | 0.85x | 10.4/13.7/16.6% | 1.3/3.3% | 3 |

> legacy-fraction=0.25: decode_failures 3

> legacy-fraction=0.75: decode_failures 1

### `FW-signing-cost` - profile-flag  `--scenario alpine`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.825 | 0.819 | 0.006 | - | - | 0.973 | 0.973 | 0.382 | 0.68x | 8.5/12.2/14.0% | 1.0/3.0% | 3 |
| signing=true | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |

### `FW-versions` - profile  `--scenario alpine`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.849 | 0.836 | 0.013 | - | - | 0.964 | 0.971 | 0.521 | 0.72x | 8.9/11.0/13.2% | 1.1/2.2% | 3 |
| 2.5 | 1 | 0.833 | 0.820 | 0.013 | - | - | 0.957 | 0.958 | 0.480 | 0.75x | 9.2/11.3/13.4% | 1.2/2.3% | 3 |
| 2.6 | 1 | 0.833 | 0.819 | 0.015 | - | - | 0.951 | 0.954 | 0.472 | 0.70x | 8.9/11.1/13.3% | 1.1/2.3% | 3 |
| 2.7 | 1 | 0.859 | 0.845 | 0.014 | - | - | 0.961 | 0.965 | 0.541 | 0.70x | 8.6/11.6/13.9% | 1.1/2.8% | 3 |
| 2.8 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.809 | 0.801 | 0.008 | - | - | 0.959 | 0.960 | 0.304 | 0.86x | 10.4/14.6/16.9% | 1.3/3.5% | 3 |
| 900 | 1 | 0.733 | 0.716 | 0.017 | - | - | 0.901 | 0.902 | 0.276 | 1.99x | 24.0/33.9/38.6% | 3.1/7.9% | 3 |
| 300 | 1 | 0.535 | 0.508 | 0.027 | - | - | 0.734 | 0.742 | 0.166 | 4.52x | 51.9/67.2/73.1% | 7.1/15.4% | 3 |

> broadcast-interval-s=300: decode_failures 7

### `LD-chatty-hops` - broadcast-interval-s  `--scenario alpine`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.883 | 0.881 | 0.002 | - | - | 0.974 | 0.974 | 0.491 | 0.97x | 11.5/15.9/18.0% | 1.5/3.6% | 3 |
| 900 | 1 | 0.814 | 0.811 | 0.003 | - | - | 0.927 | 0.927 | 0.425 | 2.22x | 26.1/36.5/41.4% | 3.3/8.4% | 3 |
| 300 | 1 | 0.532 | 0.519 | 0.013 | - | - | 0.711 | 0.719 | 0.253 | 4.87x | 55.2/69.9/75.4% | 7.7/16.5% | 3 |

> broadcast-interval-s=300: decode_failures 5

### `LD-diurnal` - diurnal  `--scenario alpine`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.800 | 0.789 | 0.011 | - | - | 0.954 | 0.955 | 0.319 | 1.18x | 14.3/20.4/23.5% | 1.9/4.9% | 3 |
| sinusoid | 1 | 0.791 | 0.780 | 0.011 | - | - | 0.948 | 0.949 | 0.337 | 1.17x | 14.1/20.1/23.1% | 1.8/4.7% | 3 |
| commuter | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.733 | 0.716 | 0.017 | - | - | 0.901 | 0.902 | 0.276 | 1.99x | 24.0/33.9/38.6% | 3.1/7.9% | 3 |
| 3600 | 1 | 0.809 | 0.801 | 0.008 | - | - | 0.959 | 0.960 | 0.304 | 0.86x | 10.4/14.6/16.9% | 1.3/3.5% | 3 |
| 10800 | 1 | 0.821 | 0.816 | 0.005 | - | - | 0.970 | 0.970 | 0.351 | 0.56x | 6.8/9.7/11.1% | 0.9/2.3% | 3 |
| 43200 | 1 | 0.833 | 0.826 | 0.007 | - | - | 0.987 | 0.987 | 0.362 | 0.36x | 4.3/6.3/7.3% | 0.6/1.6% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario alpine`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 0.25 | 1 | 0.779 | 0.769 | 0.010 | - | - | 0.940 | 0.943 | 0.325 | 1.29x | 15.6/22.2/25.6% | 2.0/5.3% | 3 |
| 1.0 | 1 | 0.778 | 0.766 | 0.012 | - | - | 0.939 | 0.940 | 0.319 | 1.43x | 17.4/24.8/28.5% | 2.2/5.9% | 3 |
| 4.0 | 1 | 0.749 | 0.732 | 0.017 | - | - | 0.912 | 0.916 | 0.297 | 1.74x | 21.5/30.8/35.5% | 2.7/7.2% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario alpine`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.737 | 0.717 | 0.020 | - | - | 0.901 | 0.924 | 0.495 | 5.47x | 54.3/67.7/75.5% | 4.0/12.1% | 3 |
| 1.0 | 1 | 0.688 | 0.672 | 0.015 | - | - | 0.837 | 0.904 | 0.468 | 6.11x | 58.7/71.1/77.9% | 4.5/13.0% | 3 |

> traceroute-per-hour=0.0: decode_failures 23

> traceroute-per-hour=1.0: decode_failures 81

> faster: 17.4 s per simulated hour against 37.7 over 49 prior run(s) - 2.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-density` - nodes  `--scenario alpine`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.540 | 0.531 | 0.009 | - | - | 0.763 | 0.771 | 0.000 | 1.11x | 13.7/23.7/32.1% | 2.5/6.5% | 3 |
| 60 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 90 | 1 | 0.913 | 0.910 | 0.003 | - | - | 0.985 | 0.985 | 0.703 | 1.51x | 16.8/24.1/28.5% | 1.5/4.7% | 3 |
| 120 | 1 | 0.926 | 0.919 | 0.007 | - | - | 0.993 | 0.993 | 0.694 | 1.90x | 19.9/30.1/36.0% | 1.3/4.7% | 3 |
| 150 | 1 | 0.956 | 0.953 | 0.003 | - | - | 0.998 | 0.999 | 0.833 | 2.54x | 26.7/34.1/38.1% | 1.3/5.6% | 3 |

> nodes=150: misdecodes 1

### `MS-hopscale` - nodes  `--scenario alpine`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 120 | 1 | 0.646 | 0.629 | 0.017 | - | - | 0.798 | 0.798 | 0.192 | 2.23x | 14.9/20.5/22.6% | 1.6/4.4% | 3 |
| 250 | 1 | 0.503 | 0.487 | 0.016 | - | - | 0.714 | 0.755 | 0.249 | 4.50x | 17.2/23.3/27.6% | 1.6/4.9% | 3 |
| 500 | 1 | 0.319 | 0.316 | 0.004 | - | - | 0.469 | 0.469 | 0.125 | 9.75x | 19.4/28.1/39.9% | 1.7/6.5% | 3 |

> nodes=250: decode_failures 63

> nodes=500: decode_failures 16

### `MS-oversubscribed` - nodes  `--scenario alpine`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.642 | 0.626 | 0.016 | - | - | 0.789 | 0.792 | 0.164 | 2.06x | 13.8/19.0/21.0% | 1.5/4.2% | 3 |
| 250 | 1 | 0.501 | 0.483 | 0.018 | - | - | 0.717 | 0.752 | 0.230 | 4.27x | 16.4/21.9/26.1% | 1.5/4.5% | 3 |
| 500 | 1 | 0.320 | 0.316 | 0.004 | - | - | 0.463 | 0.463 | 0.127 | 9.04x | 17.9/25.8/36.5% | 1.6/5.7% | 3 |

> nodes=250: decode_failures 89

> nodes=500: decode_failures 7

### `MS-roles` - role-mix  `--scenario alpine`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.782 | 0.770 | 0.013 | - | - | 0.944 | 0.945 | 0.363 | 1.30x | 15.6/22.1/25.3% | 2.0/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.753 | 0.734 | 0.020 | - | - | 0.922 | 0.922 | 0.307 | 1.15x | 14.0/20.5/23.3% | 2.1/5.0% | 3 |

### `MS-roles-fav` - role-mix  `--scenario alpine`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.802 | 0.793 | 0.009 | - | - | 0.931 | 0.931 | 0.397 | 1.34x | 15.9/22.5/25.5% | 2.0/5.1% | 3 |
| baymesh-2026-08 | 1 | 0.797 | 0.782 | 0.015 | - | - | 0.907 | 0.910 | 0.345 | 1.29x | 15.9/22.6/26.7% | 2.3/5.0% | 3 |

> faster: 0.865 s per simulated hour against 1.75 over 49 prior run(s) - 2.0x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-router-late` - router-late-fraction  `--scenario alpine`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 0.05 | 1 | 0.805 | 0.795 | 0.010 | - | - | 0.948 | 0.949 | 0.310 | 1.35x | 16.5/24.3/28.8% | 2.1/5.1% | 3 |
| 0.1 | 1 | 0.805 | 0.797 | 0.008 | - | - | 0.940 | 0.943 | 0.319 | 1.44x | 17.6/26.5/32.4% | 2.2/5.1% | 3 |
| 0.2 | 1 | 0.806 | 0.795 | 0.010 | - | - | 0.931 | 0.933 | 0.292 | 1.63x | 20.3/31.8/38.6% | 2.3/5.0% | 3 |

### `MS-siting` - siting-mix  `--scenario alpine`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| local-typical | 1 | 0.501 | 0.495 | 0.006 | - | - | 0.756 | 0.756 | 0.000 | 1.30x | 9.7/24.4/27.3% | 2.1/4.9% | 3 |
| event | 1 | 0.073 | 0.072 | 0.002 | - | - | 0.188 | 0.196 | 0.000 | 0.67x | 2.8/6.4/12.2% | 0.9/3.0% | 3 |
| backbone | 1 | 0.972 | 0.969 | 0.002 | - | - | 1.000 | 1.000 | 0.881 | 1.06x | 22.8/27.4/29.5% | 1.3/5.3% | 3 |

> faster: 0.894 s per simulated hour against 1.89 over 48 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-size` - nodes  `--scenario alpine`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.804 | 0.787 | 0.017 | - | - | 0.955 | 0.959 | 0.410 | 1.38x | 21.0/30.0/36.1% | 3.2/7.5% | 3 |
| 60 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 90 | 1 | 0.780 | 0.769 | 0.011 | - | - | 0.870 | 0.871 | 0.450 | 1.72x | 14.3/21.9/25.0% | 1.7/4.7% | 3 |
| 120 | 1 | 0.646 | 0.629 | 0.017 | - | - | 0.798 | 0.798 | 0.192 | 2.23x | 14.9/20.5/22.6% | 1.6/4.4% | 3 |
| 150 | 1 | 0.634 | 0.623 | 0.011 | - | - | 0.803 | 0.804 | 0.277 | 2.68x | 14.8/23.4/31.0% | 1.5/4.4% | 3 |

### `MS-stretch` - stretch  `--scenario alpine`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 1.25 | 1 | 0.513 | 0.501 | 0.011 | - | - | 0.754 | 0.755 | 0.035 | 1.30x | 11.7/17.1/21.6% | 2.0/5.1% | 3 |
| 1.5 | 1 | 0.284 | 0.281 | 0.003 | - | - | 0.439 | 0.445 | 0.029 | 1.31x | 8.6/15.6/16.5% | 2.0/4.9% | 3 |
| 2.0 | 1 | 0.090 | 0.090 | 0.000 | - | - | 0.204 | 0.206 | 0.000 | 0.71x | 3.5/7.9/10.9% | 1.1/2.4% | 3 |

> stretch=1.5: decode_failures 1

> faster: 0.924 s per simulated hour against 2.18 over 49 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-topology` - topology  `--scenario alpine`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| clustered | 1 | 0.807 | 0.801 | 0.006 | - | - | 0.888 | 0.889 | 0.000 | 1.02x | 22.3/27.4/29.7% | 1.2/5.4% | 3 |
| corridor | 1 | 0.505 | 0.495 | 0.009 | - | - | 0.625 | 0.659 | 0.179 | 1.48x | 16.7/23.4/25.6% | 2.2/6.4% | 3 |
| hub | 1 | 0.928 | 0.927 | 0.001 | - | - | 0.966 | 0.966 | 0.569 | 1.27x | 27.3/38.1/39.8% | 1.8/5.6% | 3 |

> topology=corridor: decode_failures 34

### `PR-crladder` - coding-rate-ladder  `--scenario alpine`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.751 | 0.751 | 0.000 | - | - | 0.930 | 0.932 | 0.322 | 1.46x | 17.7/25.6/29.4% | 2.2/6.1% | 3 |
| True | 1 | 0.758 | 0.758 | 0.000 | - | - | 0.929 | 0.931 | 0.320 | 1.47x | 17.7/26.0/29.7% | 2.3/6.2% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario alpine`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.758 | 0.758 | 0.000 | - | - | 0.929 | 0.931 | 0.320 | 1.47x | 17.7/26.0/29.7% | 2.3/6.2% | 3 |
| m4-early-flood | 1 | 0.755 | 0.755 | 0.000 | - | - | 0.930 | 0.931 | 0.323 | 1.48x | 18.0/26.2/29.9% | 2.3/6.3% | 3 |

### `PR-protocol` - protocol  `--scenario alpine`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.765 | 0.765 | 0.000 | - | - | 0 | 0.000 | 0.317 | 1.22x | 14.8/20.7/24.0% | 1.9/4.9% | 3 |
| chain | 1 | 0.770 | 0.765 | 0.005 | - | - | 0.902 | 0.941 | 0.300 | 1.45x | 17.2/25.4/28.8% | 2.2/6.0% | 3 |
| sr | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |

### `PR-repeats` - extra-repeats  `--scenario alpine`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| True | 1 | 0.791 | 0.781 | 0.010 | - | - | 0.940 | 0.942 | 0.355 | 1.27x | 15.3/21.7/24.9% | 2.0/5.1% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario alpine`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.926 | 0.919 | 0.007 | - | - | 0.993 | 0.993 | 0.694 | 1.90x | 19.9/30.1/36.0% | 1.3/4.7% | 3 |
| True | 1 | 0.928 | 0.921 | 0.007 | - | - | 0.996 | 0.997 | 0.716 | 1.94x | 20.2/30.1/36.1% | 1.3/4.6% | 3 |

### `RF-bw500` - preset  `--scenario alpine`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.133 | 0.128 | 0.005 | - | - | 0.340 | 0.344 | 0.000 | 0.04x | 0.2/0.5/0.6% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.378 | 0.369 | 0.009 | - | - | 0.456 | 0.625 | 0.034 | 0.23x | 1.6/3.2/4.5% | 0.4/1.0% | 3 |
| LONG_TURBO | 1 | 0.680 | 0.666 | 0.013 | - | - | 0.848 | 0.853 | 0.064 | 1.18x | 12.1/16.4/21.4% | 1.8/4.6% | 3 |

> preset=SHORT_TURBO: decode_failures 2

> preset=MEDIUM_TURBO: decode_failures 12

### `RF-duct` - duct-per-hour  `--scenario alpine`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 0.25 | 1 | 0.821 | 0.809 | 0.012 | - | - | 0.954 | 0.954 | 0.435 | 1.19x | 16.2/22.5/25.1% | 1.7/5.1% | 3 |
| 1.0 | 1 | 0.901 | 0.895 | 0.007 | - | - | 0.978 | 0.978 | 0.676 | 1.02x | 19.7/24.8/26.8% | 1.2/5.1% | 3 |

### `RF-eu-presets` - preset  `--scenario alpine`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.254 | 0.253 | 0.001 | - | - | 0.339 | 0.444 | 0.035 | 0.12x | 0.7/1.6/2.0% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| LITE_FAST | 1 | 0.750 | 0.732 | 0.019 | - | - | 0.840 | 0.859 | 0.206 | 0.96x | 10.7/14.6/18.3% | 1.5/3.8% | 3 |
| NARROW_SLOW | 1 | 0.772 | 0.755 | 0.017 | - | - | 0.886 | 0.893 | 0.259 | 1.21x | 13.6/18.8/24.2% | 1.8/4.6% | 3 |

> preset=SHORT_FAST: decode_failures 8

> preset=LITE_FAST: decode_failures 11

### `RF-noise` - noise-profile  `--scenario alpine`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| temporal | 1 | 0.673 | 0.659 | 0.013 | - | - | 0.866 | 0.866 | 0.170 | 1.25x | 14.6/20.6/24.9% | 1.9/4.9% | 3 |
| transient | 1 | 0.767 | 0.758 | 0.009 | - | - | 0.929 | 0.931 | 0.304 | 1.26x | 15.1/21.2/24.6% | 2.0/5.1% | 3 |
| periodic | 1 | 0.628 | 0.617 | 0.011 | - | - | 0.783 | 0.784 | 0.186 | 1.16x | 14.1/20.0/23.1% | 1.8/4.4% | 3 |

### `RF-preset` - preset  `--scenario alpine`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.254 | 0.253 | 0.001 | - | - | 0.339 | 0.444 | 0.035 | 0.12x | 0.7/1.6/2.0% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| LONG_MODERATE | 1 | 0.795 | 0.770 | 0.025 | - | - | 0.878 | 0.947 | 0.666 | 3.04x | 39.7/51.9/58.0% | 4.4/11.5% | 3 |

> preset=SHORT_FAST: decode_failures 8

> preset=LONG_MODERATE: decode_failures 23

### `RF-preset-turbo` - preset  `--scenario alpine`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.052 | 0.051 | 0.001 | - | - | 0.190 | 0.196 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.133 | 0.128 | 0.005 | - | - | 0.340 | 0.344 | 0.000 | 0.04x | 0.2/0.5/0.6% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| LONG_TURBO | 1 | 0.680 | 0.666 | 0.013 | - | - | 0.848 | 0.853 | 0.064 | 1.18x | 12.1/16.4/21.4% | 1.8/4.6% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.780 | 0.771 | 0.009 | - | - | 0.935 | 0.937 | 0.253 | 1.75x | 20.2/28.6/32.8% | 2.8/6.8% | 3 |

> preset=SHORT_TURBO: decode_failures 2

### `RF-pulse` - noise-pulse-interval-ms  `--scenario alpine`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.741 | 0.730 | 0.011 | - | - | 0.900 | 0.901 | 0.275 | 1.21x | 14.8/20.9/24.1% | 1.9/4.8% | 3 |
| 10000 | 1 | 0.628 | 0.617 | 0.011 | - | - | 0.783 | 0.784 | 0.186 | 1.16x | 14.1/20.0/23.1% | 1.8/4.4% | 3 |
| 4000 | 1 | 0.381 | 0.376 | 0.005 | - | - | 0.476 | 0.512 | 0.082 | 1.00x | 12.5/17.5/20.7% | 1.6/3.4% | 3 |
| 2000 | 1 | 0.100 | 0.100 | 0.000 | - | - | 0.137 | 0.188 | 0.022 | 0.72x | 9.6/12.8/14.7% | 1.1/1.9% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 2

### `RF-stretch-duct` - duct-per-hour  `--scenario alpine`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.284 | 0.281 | 0.003 | - | - | 0.439 | 0.445 | 0.029 | 1.31x | 8.6/15.6/16.5% | 2.0/4.9% | 3 |
| 1.0 | 1 | 0.659 | 0.649 | 0.010 | - | - | 0.739 | 0.739 | 0.491 | 0.95x | 12.8/16.4/21.5% | 1.3/4.3% | 3 |

> duct-per-hour=0.0: decode_failures 1

### `RF-txpower` - tx-power  `--scenario alpine`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 22 | 1 | 0.345 | 0.342 | 0.003 | - | - | 0.310 | 0.412 | 0.035 | 1.40x | 8.7/17.9/22.1% | 2.3/5.2% | 3 |
| 17 | 1 | 0.129 | 0.124 | 0.005 | - | - | 0.319 | 0.322 | 0.000 | 0.85x | 4.3/9.6/13.0% | 1.4/3.2% | 3 |
| 14 | 1 | 0.068 | 0.068 | 0.001 | - | - | 0.229 | 0.241 | 0.000 | 0.56x | 2.6/5.3/8.1% | 0.9/2.5% | 3 |

> tx-power=22: decode_failures 5

> tx-power=14: decode_failures 2

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario alpine`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.926 | 0.919 | 0.007 | - | - | 0.993 | 0.993 | 0.694 | 1.90x | 19.9/30.1/36.0% | 1.3/4.7% | 3 |
| True | 1 | 0.917 | 0.909 | 0.008 | - | - | 0.990 | 0.991 | 0.679 | 2.22x | 22.9/34.4/40.9% | 1.5/5.2% | 3 |

### `RT-favourites` - favourite-routers  `--scenario alpine`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.806 | 0.797 | 0.009 | - | - | 0.955 | 0.956 | 0.245 | 1.31x | 16.0/22.8/27.3% | 1.9/5.2% | 3 |
| True | 1 | 0.836 | 0.829 | 0.007 | - | - | 0.954 | 0.954 | 0.268 | 1.36x | 16.8/23.4/27.7% | 2.0/5.1% | 3 |

### `RT-hopassign` - hop-assign  `--scenario alpine`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| random | 1 | 0.742 | 0.730 | 0.011 | - | - | 0.918 | 0.918 | 0.377 | 1.27x | 14.8/21.8/24.9% | 1.9/5.2% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario alpine`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.590 | 0.554 | 0.036 | - | - | 0.842 | 0.842 | 0.216 | 1.08x | 13.4/18.8/23.2% | 1.5/4.8% | 3 |
| 7 | 1 | 0.849 | 0.846 | 0.003 | - | - | 0.943 | 0.944 | 0.495 | 1.38x | 16.4/23.0/26.2% | 2.1/5.3% | 3 |
| 15 | 1 | 0.895 | 0.894 | 0.001 | - | - | 0.960 | 0.961 | 0.577 | 1.43x | 17.2/23.6/26.8% | 2.2/5.3% | 3 |
| 32 | 1 | 0.894 | 0.892 | 0.001 | - | - | 0.955 | 0.955 | 0.572 | 1.41x | 16.6/23.3/26.4% | 2.1/5.3% | 3 |

### `RT-hopspread` - hop-limit  `--scenario alpine`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.590 | 0.554 | 0.036 | - | - | 0.842 | 0.842 | 0.216 | 1.08x | 13.4/18.8/23.2% | 1.5/4.8% | 3 |
| 5 | 1 | 0.763 | 0.753 | 0.010 | - | - | 0.935 | 0.937 | 0.362 | 1.24x | 14.6/21.6/24.9% | 1.9/5.1% | 3 |
| 7 | 1 | 0.849 | 0.846 | 0.003 | - | - | 0.943 | 0.944 | 0.495 | 1.38x | 16.4/23.0/26.2% | 2.1/5.3% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario alpine`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| KNOWN_ONLY | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.779 | 0.778 | 0.001 | - | - | 0.892 | 0.940 | 0.327 | 1.23x | 15.0/20.8/24.1% | 1.9/4.9% | 3 |

> rebroadcast-mode=CORE_PORTNUMS_ONLY: decode_failures 5

### `RT-spread` - hop-spread  `--scenario alpine`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.590 | 0.554 | 0.036 | - | - | 0.842 | 0.842 | 0.216 | 1.08x | 13.4/18.8/23.2% | 1.5/4.8% | 3 |
| True | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |

### `SC-signing` - signature-policy  `--scenario alpine`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| BALANCED | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| STRICT | 1 | 0.671 | 0.671 | 0.000 | - | - | 0.847 | 0.852 | 0.188 | 1.36x | 16.7/23.2/26.7% | 2.1/5.5% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario alpine`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| dm | 1 | 0.794 | 0.781 | 0.013 | - | - | 0.950 | 0.950 | 0.309 | 1.24x | 15.1/21.4/24.7% | 2.0/5.2% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario alpine`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.778 | 0.768 | 0.010 | - | - | 0.934 | 0.934 | 0.318 | 1.27x | 15.4/21.9/25.2% | 2.0/5.2% | 3 |
| local | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| time | 1 | 0.782 | 0.771 | 0.011 | - | - | 0.945 | 0.945 | 0.333 | 1.29x | 15.6/22.1/25.4% | 2.0/5.3% | 3 |
| window | 1 | 0.779 | 0.767 | 0.013 | - | - | 0.948 | 0.949 | 0.300 | 1.25x | 15.1/21.2/24.6% | 2.0/5.1% | 3 |

> bucket-mode=global: misdecodes 36

> bucket-mode=time: misdecodes 39

> bucket-mode=window: misdecodes 28

### `SF-bucket-time` - time-bucket-s  `--scenario alpine`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.771 | 0.757 | 0.014 | - | - | 0.925 | 0.927 | 0.293 | 1.39x | 16.5/24.4/27.5% | 2.1/5.8% | 3 |
| 1800 | 1 | 0.782 | 0.771 | 0.011 | - | - | 0.945 | 0.945 | 0.333 | 1.29x | 15.6/22.1/25.4% | 2.0/5.3% | 3 |
| 3600 | 1 | 0.785 | 0.775 | 0.010 | - | - | 0.939 | 0.939 | 0.316 | 1.27x | 15.5/21.8/25.2% | 2.0/5.2% | 3 |

> time-bucket-s=600: misdecodes 137

> time-bucket-s=1800: misdecodes 39

> time-bucket-s=3600: misdecodes 17

### `SF-cadence` - trigger  `--scenario alpine`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| interval | 1 | 0.767 | 0.750 | 0.017 | - | - | 0.930 | 0.933 | 0.294 | 1.69x | 19.6/31.0/34.5% | 2.5/7.7% | 3 |
| aimd | 1 | 0.782 | 0.779 | 0.003 | - | - | 0.908 | 0.945 | 0.323 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| bucket+interval | 1 | 0.766 | 0.749 | 0.017 | - | - | 0.923 | 0.923 | 0.293 | 1.70x | 19.9/30.7/34.2% | 2.5/7.3% | 3 |

> trigger=interval: misdecodes 25

> trigger=interval: decode_failures 1

> trigger=aimd: misdecodes 3

> trigger=aimd: decode_failures 3

> trigger=bucket+interval: misdecodes 24

### `SF-capacity` - capacity  `--scenario alpine`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.797 | 0.785 | 0.012 | - | - | 0.951 | 0.951 | 0.329 | 1.25x | 15.1/21.6/25.0% | 2.0/5.2% | 3 |
| 8 | 1 | 0.786 | 0.774 | 0.012 | - | - | 0.933 | 0.936 | 0.330 | 1.26x | 15.2/21.7/25.0% | 2.0/5.2% | 3 |
| 16 | 1 | 0.785 | 0.774 | 0.011 | - | - | 0.945 | 0.945 | 0.317 | 1.25x | 15.0/21.3/24.5% | 2.0/5.0% | 3 |
| 32 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 50 | 1 | 0.779 | 0.769 | 0.010 | - | - | 0.938 | 0.940 | 0.300 | 1.25x | 15.0/21.2/24.4% | 1.9/5.1% | 3 |

> capacity=4: decode_failures 68

> capacity=8: decode_failures 25

### `SF-capacity-local` - capacity  `--scenario alpine`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.797 | 0.785 | 0.012 | - | - | 0.951 | 0.951 | 0.329 | 1.25x | 15.1/21.6/25.0% | 2.0/5.2% | 3 |
| 8 | 1 | 0.786 | 0.774 | 0.012 | - | - | 0.933 | 0.936 | 0.330 | 1.26x | 15.2/21.7/25.0% | 2.0/5.2% | 3 |
| 16 | 1 | 0.785 | 0.774 | 0.011 | - | - | 0.945 | 0.945 | 0.317 | 1.25x | 15.0/21.3/24.5% | 2.0/5.0% | 3 |
| 32 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 50 | 1 | 0.779 | 0.769 | 0.010 | - | - | 0.938 | 0.940 | 0.300 | 1.25x | 15.0/21.2/24.4% | 1.9/5.1% | 3 |

> capacity=4: decode_failures 68

> capacity=8: decode_failures 25

### `SF-capacity-window` - capacity  `--scenario alpine`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.790 | 0.779 | 0.011 | - | - | 0.951 | 0.958 | 0.316 | 1.25x | 15.1/21.3/24.6% | 2.0/5.1% | 3 |
| 16 | 1 | 0.793 | 0.780 | 0.013 | - | - | 0.948 | 0.948 | 0.331 | 1.24x | 15.0/21.1/24.4% | 1.9/5.0% | 3 |
| 32 | 1 | 0.779 | 0.767 | 0.013 | - | - | 0.948 | 0.949 | 0.300 | 1.25x | 15.1/21.2/24.6% | 2.0/5.1% | 3 |

> capacity=8: misdecodes 22

> capacity=8: decode_failures 14

> capacity=16: misdecodes 37

> capacity=32: misdecodes 28

### `SF-catchup` - catch-up-hours  `--scenario alpine`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.766 | 0.749 | 0.017 | - | - | 0.923 | 0.923 | 0.293 | 1.70x | 19.9/30.7/34.2% | 2.5/7.3% | 3 |
| 02-06 | 1 | 0.785 | 0.777 | 0.008 | - | - | 0.918 | 0.945 | 0.310 | 1.28x | 15.6/22.2/25.6% | 2.0/5.4% | 3 |
| 00-08 | 1 | 0.783 | 0.774 | 0.009 | - | - | 0.921 | 0.941 | 0.295 | 1.35x | 16.1/23.7/27.1% | 2.1/5.8% | 3 |

> catch-up-hours=: misdecodes 24

> catch-up-hours=02-06: decode_failures 39

> catch-up-hours=00-08: decode_failures 36

### `SF-hops-flat` - hops-apart  `--scenario alpine`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.786 | 0.778 | 0.009 | - | - | 0.901 | 0.903 | 0.319 | 1.25x | 15.1/21.3/24.7% | 2.0/5.0% | 3 |
| 2 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 3 | 1 | 0.813 | 0.773 | 0.039 | - | - | 0.963 | 0.982 | 0.334 | 1.27x | 15.5/21.5/24.9% | 2.0/5.3% | 3 |
| 4 | 1 | 0.824 | 0.766 | 0.058 | - | - | 0.903 | 0.989 | 0.402 | 1.29x | 15.8/21.8/25.0% | 2.0/5.2% | 3 |

> hops-apart=3: decode_failures 1

> hops-apart=4: decode_failures 36

### `SF-hops-spread` - hops-apart  `--scenario alpine`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.786 | 0.778 | 0.009 | - | - | 0.901 | 0.903 | 0.319 | 1.25x | 15.1/21.3/24.7% | 2.0/5.0% | 3 |
| 2 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 3 | 1 | 0.813 | 0.773 | 0.039 | - | - | 0.963 | 0.982 | 0.334 | 1.27x | 15.5/21.5/24.9% | 2.0/5.3% | 3 |
| 4 | 1 | 0.824 | 0.766 | 0.058 | - | - | 0.903 | 0.989 | 0.402 | 1.29x | 15.8/21.8/25.0% | 2.0/5.2% | 3 |
| 5 | 1 | 0.812 | 0.765 | 0.048 | - | - | 0.897 | 0.996 | 0.416 | 1.30x | 15.8/21.9/25.1% | 2.0/5.2% | 3 |

> hops-apart=3: decode_failures 1

> hops-apart=4: decode_failures 36

> hops-apart=5: decode_failures 38

### `SF-jitter-global` - advert-jitter-s  `--scenario alpine`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.789 | 0.777 | 0.011 | - | - | 0.953 | 0.954 | 0.305 | 1.26x | 15.1/21.7/24.9% | 2.0/5.2% | 3 |
| 30 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 120 | 1 | 0.787 | 0.776 | 0.010 | - | - | 0.952 | 0.954 | 0.326 | 1.28x | 15.5/21.9/25.2% | 2.0/5.2% | 3 |
| 600 | 1 | 0.789 | 0.778 | 0.011 | - | - | 0.946 | 0.946 | 0.326 | 1.25x | 15.2/21.5/24.9% | 2.0/5.1% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario alpine`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.789 | 0.777 | 0.011 | - | - | 0.953 | 0.954 | 0.305 | 1.26x | 15.1/21.7/24.9% | 2.0/5.2% | 3 |
| 30 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 120 | 1 | 0.787 | 0.776 | 0.010 | - | - | 0.952 | 0.954 | 0.326 | 1.28x | 15.5/21.9/25.2% | 2.0/5.2% | 3 |
| 600 | 1 | 0.789 | 0.778 | 0.011 | - | - | 0.946 | 0.946 | 0.326 | 1.25x | 15.2/21.5/24.9% | 2.0/5.1% | 3 |

### `SF-place-flat` - place  `--scenario alpine`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.833 | 0.771 | 0.062 | - | - | 0.909 | 0.972 | 0.327 | 1.29x | 15.8/21.2/24.8% | 2.0/5.0% | 3 |
| routers | 1 | 0.808 | 0.774 | 0.034 | - | - | 0.972 | 0.983 | 0.290 | 1.25x | 15.2/21.3/24.7% | 2.0/5.1% | 3 |
| alternate-routers | 1 | 0.798 | 0.772 | 0.027 | - | - | 0.923 | 0.966 | 0.304 | 1.25x | 15.2/21.5/24.9% | 2.0/5.2% | 3 |
| beside-router | 1 | 0.794 | 0.779 | 0.015 | - | - | 0.962 | 0.966 | 0.311 | 1.27x | 15.2/21.7/25.2% | 2.0/5.2% | 3 |
| random-clients | 1 | 0.812 | 0.767 | 0.045 | - | - | 0.922 | 0.973 | 0.445 | 1.29x | 15.3/21.9/25.1% | 2.0/5.1% | 3 |
| hops-apart | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |

> place=spread: decode_failures 17

> place=routers: decode_failures 2

> place=alternate-routers: decode_failures 8

> place=random-clients: decode_failures 26

### `SF-place-spread` - place  `--scenario alpine`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.833 | 0.771 | 0.062 | - | - | 0.909 | 0.972 | 0.327 | 1.29x | 15.8/21.2/24.8% | 2.0/5.0% | 3 |
| routers | 1 | 0.808 | 0.774 | 0.034 | - | - | 0.972 | 0.983 | 0.290 | 1.25x | 15.2/21.3/24.7% | 2.0/5.1% | 3 |
| alternate-routers | 1 | 0.798 | 0.772 | 0.027 | - | - | 0.923 | 0.966 | 0.304 | 1.25x | 15.2/21.5/24.9% | 2.0/5.2% | 3 |
| beside-router | 1 | 0.794 | 0.779 | 0.015 | - | - | 0.962 | 0.966 | 0.311 | 1.27x | 15.2/21.7/25.2% | 2.0/5.2% | 3 |
| random-clients | 1 | 0.812 | 0.767 | 0.045 | - | - | 0.922 | 0.973 | 0.445 | 1.29x | 15.3/21.9/25.1% | 2.0/5.1% | 3 |
| hops-apart | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |

> place=spread: decode_failures 17

> place=routers: decode_failures 2

> place=alternate-routers: decode_failures 8

> place=random-clients: decode_failures 26

### `SF-provide-transport` - provide-transport  `--scenario alpine`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| broadcast | 1 | 0.812 | 0.771 | 0.041 | - | - | 0.945 | 0.945 | 0.355 | 1.31x | 15.7/22.4/25.6% | 2.1/5.3% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario alpine`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| heard | 1 | 0.782 | 0.770 | 0.012 | - | - | 0.939 | 0.940 | 0.310 | 1.24x | 15.0/21.1/24.4% | 2.0/5.1% | 3 |

> replay-ordering=heard: misdecodes 23

### `SF-replay-order-broadcast` - replay-ordering  `--scenario alpine`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.812 | 0.771 | 0.041 | - | - | 0.945 | 0.945 | 0.355 | 1.31x | 15.7/22.4/25.6% | 2.1/5.3% | 3 |
| heard | 1 | 0.806 | 0.771 | 0.035 | - | - | 0.939 | 0.940 | 0.376 | 1.30x | 15.7/22.2/25.5% | 2.1/5.3% | 3 |

> replay-ordering=heard: misdecodes 13

### `SF-resolve` - resolve  `--scenario alpine`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| enum | 1 | 0.796 | 0.784 | 0.013 | - | - | 0.954 | 0.955 | 0.303 | 1.25x | 15.2/21.6/25.1% | 2.0/5.2% | 3 |
| hybrid | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |

### `SF-servers-allrouters` - servers  `--scenario alpine`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.808 | 0.774 | 0.034 | - | - | 0.972 | 0.983 | 0.290 | 1.25x | 15.2/21.3/24.7% | 2.0/5.1% | 3 |
| 6 | 1 | 0.823 | 0.770 | 0.053 | - | - | 0.983 | 0.988 | 0.304 | 1.30x | 15.8/22.5/25.8% | 2.0/5.4% | 6 |

> servers=3: decode_failures 2

### `SF-servers-flat` - servers  `--scenario alpine`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.778 | 0.772 | 0.005 | - | - | 0.935 | 0.938 | 0.302 | 1.24x | 15.1/21.2/24.5% | 2.0/5.2% | 2 |
| 3 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 5 | 1 | 0.799 | 0.773 | 0.026 | - | - | 0.975 | 0.976 | 0.322 | 1.30x | 15.7/22.2/25.8% | 2.1/5.3% | 5 |
| 8 | 1 | 0.798 | 0.776 | 0.022 | - | - | 0.977 | 0.978 | 0.318 | 1.33x | 15.9/22.6/26.5% | 2.1/5.5% | 8 |

### `SF-servers-spread` - servers  `--scenario alpine`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.778 | 0.772 | 0.005 | - | - | 0.935 | 0.938 | 0.302 | 1.24x | 15.1/21.2/24.5% | 2.0/5.2% | 2 |
| 3 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 5 | 1 | 0.799 | 0.773 | 0.026 | - | - | 0.975 | 0.976 | 0.322 | 1.30x | 15.7/22.2/25.8% | 2.1/5.3% | 5 |
| 8 | 1 | 0.798 | 0.776 | 0.022 | - | - | 0.977 | 0.978 | 0.318 | 1.33x | 15.9/22.6/26.5% | 2.1/5.5% | 8 |

### `SF-signed` - signed  `--scenario alpine`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| True | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario alpine`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.785 | 0.775 | 0.011 | - | - | 0.939 | 0.939 | 0.267 | 1.18x | 14.4/20.3/23.5% | 1.9/4.8% | 3 |
| 1 | 1 | 0.788 | 0.775 | 0.012 | - | - | 0.940 | 0.940 | 0.282 | 1.18x | 14.3/20.3/23.4% | 1.9/4.8% | 3 |
| 2 | 1 | 0.785 | 0.777 | 0.008 | - | - | 0.948 | 0.949 | 0.260 | 1.19x | 14.4/20.6/23.7% | 1.9/4.9% | 3 |
| 4 | 1 | 0.784 | 0.773 | 0.010 | - | - | 0.938 | 0.938 | 0.265 | 1.19x | 14.4/20.3/23.4% | 1.9/4.8% | 3 |

> faster: 0.753 s per simulated hour against 1.57 over 49 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `SF-width` - short-id-bits  `--scenario alpine`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.789 | 0.777 | 0.012 | - | - | 0.949 | 0.950 | 0.318 | 1.25x | 15.0/21.3/24.6% | 1.9/5.1% | 3 |
| 24 | 1 | 0.788 | 0.779 | 0.008 | - | - | 0.935 | 0.938 | 0.316 | 1.26x | 15.2/21.4/24.7% | 2.0/5.1% | 3 |
| 32 | 1 | 0.775 | 0.763 | 0.011 | - | - | 0.930 | 0.931 | 0.324 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |
| 64 | 1 | 0.780 | 0.770 | 0.011 | - | - | 0.937 | 0.940 | 0.316 | 1.27x | 15.3/21.7/25.0% | 2.0/5.2% | 3 |

### `SF-window-size` - window-size  `--scenario alpine`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.772 | 0.760 | 0.013 | - | - | 0.936 | 0.937 | 0.324 | 1.33x | 15.9/23.1/26.4% | 2.1/5.5% | 3 |
| 16 | 1 | 0.787 | 0.779 | 0.008 | - | - | 0.941 | 0.942 | 0.306 | 1.29x | 15.5/22.1/25.4% | 2.0/5.3% | 3 |
| 32 | 1 | 0.779 | 0.767 | 0.013 | - | - | 0.948 | 0.949 | 0.300 | 1.25x | 15.1/21.2/24.6% | 2.0/5.1% | 3 |

> window-size=8: misdecodes 90

> window-size=16: misdecodes 47

> window-size=32: misdecodes 28

### `TH-congestion` - no-congestion-scaling  `--scenario alpine`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.926 | 0.919 | 0.007 | - | - | 0.993 | 0.993 | 0.694 | 1.90x | 19.9/30.1/36.0% | 1.3/4.7% | 3 |
| True | 1 | 0.743 | 0.724 | 0.019 | - | - | 0.890 | 0.933 | 0.508 | 5.42x | 53.9/67.3/75.2% | 3.9/12.0% | 3 |

> no-congestion-scaling=True: decode_failures 31

### `TH-congestion-input` - congestion-input  `--scenario alpine`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.501 | 0.483 | 0.018 | - | - | 0.717 | 0.752 | 0.230 | 4.27x | 16.4/21.9/26.1% | 1.5/4.5% | 3 |
| truesize | 1 | 0.530 | 0.512 | 0.019 | - | - | 0.775 | 0.788 | 0.242 | 3.16x | 12.1/16.5/21.0% | 1.0/3.8% | 3 |

> congestion-input=hotstore: decode_failures 89

> congestion-input=truesize: decode_failures 62

> slower: 27.7 s per simulated hour against 11.2 over 49 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `TH-congestion-mode` - congestion-mode  `--scenario alpine`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.928 | 0.921 | 0.006 | - | - | 0.993 | 0.994 | 0.705 | 1.86x | 19.5/29.2/34.9% | 1.3/4.5% | 3 |
| adaptive | 1 | 0.926 | 0.919 | 0.007 | - | - | 0.993 | 0.993 | 0.694 | 1.90x | 19.9/30.1/36.0% | 1.3/4.7% | 3 |

