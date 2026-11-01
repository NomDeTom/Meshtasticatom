# Sweep blocks-2026-11-01-5676536

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** alpine
- **seed base** 5676536 · seeds 5676536
- **blocks** 87 run
- **compute** 9.9 h of simulator time across every cell
- **generated** 2026-11-01T10:33:55+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>98 warnings</summary>

- AD-amplifiers: amplifier-mix=arms-race: decode_failures 33
- AD-amplifiers: slower: 4.29 s per simulated hour against 1.58 over 72 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- AD-badrouters: role-placement=inverse: decode_failures 1
- BL-control: protocol=sr: decode_failures 15
- BL-control: slower: 3.92 s per simulated hour against 1.82 over 72 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- DB-hotstore-stress: max-num-nodes=10: decode_failures 71
- DB-hotstore-stress: max-num-nodes=120: decode_failures 2
- DB-warm: warm-num-nodes=0: queue drops 16.8% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 79
- DB-warm: warm-num-nodes=25: queue drops 16.8% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 79
- DB-warm: warm-num-nodes=100: queue drops 16.8% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 79
- DB-warm: warm-num-nodes=2000: queue drops 16.8% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 79
- DG-burst: burst-loss=0.2: decode_failures 4
- DG-burst: burst-loss=0.3: decode_failures 26
- DG-loss: extra-loss=0.3: decode_failures 27
- DG-outage: burst-loss=0.1: decode_failures 55
- DG-outage: burst-loss=0.2: decode_failures 34
- DG-outage: burst-loss=0.3: decode_failures 35
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 4
- DM-mode: dm-mode=m4-early-flood: decode_failures 3
- FW-mixed-26: legacy-fraction=0.25: decode_failures 1
- FW-versions: profile=2.6: decode_failures 2
- LD-chatty-hops: broadcast-interval-s=3600: misdecodes 1
- LD-chatty-hops: broadcast-interval-s=300: queue drops 10.8% of transmissions - airtime here is measured through a cap
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 44
- LD-chatty: broadcast-interval-s=300: decode_failures 22
- LD-interval: broadcast-interval-s=10800: misdecodes 1
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 16.8% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 79
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 22.3% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 102
- MS-density: nodes=120: misdecodes 1
- MS-density: nodes=150: decode_failures 4
- MS-hopscale: nodes=250: decode_failures 1
- MS-hopscale: nodes=500: decode_failures 21
- MS-oversubscribed: nodes=250: decode_failures 2
- MS-oversubscribed: nodes=500: decode_failures 30
- MS-size: nodes=150: decode_failures 2
- MS-stretch: stretch=1.25: decode_failures 20
- PR-crladder: coding-rate-ladder=False: decode_failures 4
- PR-repeats-busy: extra-repeats=False: misdecodes 1
- RF-eu-presets: preset=NARROW_SLOW: decode_failures 2
- RF-preset: preset=LONG_MODERATE: decode_failures 53
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 3
- RF-txpower: tx-power=14: decode_failures 13
- RT-adopt: no-adopt-hop-recommendation=False: misdecodes 1
- SF-advert-transport: advert-transport=dm: misdecodes 1
- SF-bucket-mode: bucket-mode=global: misdecodes 42
- SF-bucket-mode: bucket-mode=time: misdecodes 38
- SF-bucket-mode: bucket-mode=window: misdecodes 22
- SF-bucket-time: time-bucket-s=600: misdecodes 110
- SF-bucket-time: time-bucket-s=1800: misdecodes 38
- SF-bucket-time: time-bucket-s=3600: misdecodes 11
- SF-bucket-time: time-bucket-s=3600: decode_failures 3
- SF-cadence: trigger=interval: misdecodes 15
- SF-cadence: trigger=interval: decode_failures 8
- SF-cadence: trigger=aimd: misdecodes 2
- SF-cadence: trigger=aimd: decode_failures 13
- SF-cadence: trigger=bucket+interval: misdecodes 17
- SF-capacity-local: capacity=4: decode_failures 67
- SF-capacity-local: capacity=8: decode_failures 26
- SF-capacity-local: capacity=16: decode_failures 1
- SF-capacity: capacity=4: decode_failures 67
- SF-capacity: capacity=8: decode_failures 26
- SF-capacity: capacity=16: decode_failures 1
- SF-capacity-window: capacity=8: misdecodes 5
- SF-capacity-window: capacity=8: decode_failures 63
- SF-capacity-window: capacity=16: misdecodes 28
- SF-capacity-window: capacity=16: decode_failures 15
- SF-capacity-window: capacity=32: misdecodes 22
- SF-catchup: catch-up-hours=: misdecodes 17
- SF-catchup: catch-up-hours=02-06: decode_failures 49
- SF-catchup: catch-up-hours=00-08: decode_failures 50
- SF-hops-flat: hops-apart=3: decode_failures 15
- SF-hops-flat: hops-apart=4: decode_failures 25
- SF-hops-spread: hops-apart=3: decode_failures 15
- SF-hops-spread: hops-apart=4: decode_failures 25
- SF-hops-spread: hops-apart=5: decode_failures 25
- SF-place-flat: place=spread: decode_failures 18
- SF-place-flat: place=random-clients: decode_failures 36
- SF-place-spread: place=spread: decode_failures 18
- SF-place-spread: place=random-clients: decode_failures 36
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 8
- SF-replay-order: replay-ordering=heard: misdecodes 18
- SF-servers-flat: servers=5: misdecodes 1
- SF-servers-spread: servers=5: misdecodes 1
- SF-window-size: window-size=8: misdecodes 119
- SF-window-size: window-size=16: misdecodes 50
- SF-window-size: window-size=32: misdecodes 22
- TH-congestion-input: congestion-input=hotstore: decode_failures 2
- TH-congestion-input: congestion-input=truesize: decode_failures 2
- TH-congestion-mode: congestion-mode=adaptive: misdecodes 1
- TH-congestion: no-congestion-scaling=False: misdecodes 1
- TH-congestion: no-congestion-scaling=True: queue drops 13.6% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 80

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `AD-amplifiers` | 4.29 | 1.58 | 2.71x | 72 |
| `BL-control` | 3.92 | 1.82 | 2.15x | 72 |
| `DG-loss` | 3.7 | 2.25 | 1.65x | 72 |
| `MS-roles-fav` | 1.1 | 1.7 | 0.64x | 72 |
| `LD-traceroute-small` | 23.1 | 36.2 | 0.64x | 72 |
| `RT-spread` | 1.41 | 2.23 | 0.63x | 72 |
| `SF-provide-transport` | 1.08 | 1.75 | 0.62x | 72 |
| `MS-siting` | 1.07 | 1.77 | 0.61x | 71 |
| `SF-jitter-local` | 1.04 | 1.76 | 0.59x | 72 |
| `MS-size` | 2.04 | 3.45 | 0.59x | 72 |
| `AD-siting` | 0.876 | 1.49 | 0.59x | 72 |
| `TH-congestion-mode` | 1.94 | 3.33 | 0.58x | 72 |
| `AD-amplify-worst` | 1.06 | 1.84 | 0.58x | 72 |
| `RF-stretch-duct` | 1.05 | 1.82 | 0.57x | 72 |
| `RT-adopt` | 2.22 | 3.89 | 0.57x | 72 |
| `MS-topology` | 1.03 | 1.92 | 0.53x | 72 |
| `MS-hopscale` | 8.87 | 17.1 | 0.52x | 72 |
| `RT-hoplimit` | 0.901 | 1.76 | 0.51x | 72 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.947 | 0.947 | 0.792 → 0.802 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.939 | 0.939 | 0.792 → 0.802 | 1.2x bytes_on_air | up | 3 |
| `MS-siting` | siting-mix | **text** | 0.144 → 0.972 | 0.827 | 0.144 → 0.971 | 11x sr_airtime | up | 4 |
| `RF-preset-turbo` | preset | **held** | 0.120 → 0.939 | 0.819 | 0.072 → 0.795 | 9.8x sr_airtime | up | 5 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.114 → 0.883 | 0.769 | 0.096 → 0.742 | 1.5e+02x sr_airtime | down | 4 |
| `RF-txpower` | tx-power | **text** | 0.104 → 0.803 | 0.700 | 0.101 → 0.795 | 4x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **held** | 0.189 → 0.868 | 0.679 | 0.078 → 0.701 | 6.4x sr_bytes | down | 3 |
| `MS-stretch` | stretch | **text** | 0.137 → 0.803 | 0.666 | 0.136 → 0.795 | 11x sr_bytes | down | 4 |
| `RF-bw500` | preset | **text** | 0.179 → 0.721 | 0.543 | 0.173 → 0.714 | 2.6x advert_bytes | up | 3 |
| `MS-topology` | topology | **text** | 0.429 → 0.924 | 0.494 | 0.422 → 0.919 | 3.1x sr_airtime | up | 4 |
| `MS-hopscale` | nodes | **held** | 0.457 → 0.939 | 0.482 | 0.331 → 0.795 | 8.2x bytes_on_air | down | 4 |
| `RF-eu-presets` | preset | **text** | 0.325 → 0.803 | 0.478 | 0.324 → 0.795 | 3.8x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.325 → 0.803 | 0.478 | 0.324 → 0.795 | 4.4x sr_airtime | up | 3 |
| `MS-oversubscribed` | nodes | **held** | 0.473 → 0.924 | 0.451 | 0.333 → 0.722 | 4.9x sr_bytes | down | 3 |
| `SF-place-flat` | place | **held** | 0.588 → 0.939 | 0.351 | 0.788 → 0.797 | 4.5x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.588 → 0.939 | 0.351 | 0.788 → 0.797 | 4.5x sr_bytes | up | 6 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.305 → 0.634 | 0.329 | 0.301 → 0.631 | 2.1x sr_airtime | up | 2 |
| `DG-outage` | burst-loss | **text** | 0.481 → 0.803 | 0.322 | 0.456 → 0.795 | 2.1x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.531 → 0.843 | 0.312 | 0.512 → 0.838 | 8.4x sr_airtime | down | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.585 → 0.896 | 0.310 | 0.577 → 0.894 | 9.2x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.498 → 0.803 | 0.306 | 0.458 → 0.795 | 2.2x sr_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.492 → 0.747 | 0.255 | 0.299 → 0.492 | 5.4x sr_airtime | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.704 → 0.941 | 0.237 | 0.693 → 0.939 | 4x sr_airtime | down | 2 |
| `MS-density` | nodes | **text** | 0.711 → 0.943 | 0.233 | 0.701 → 0.940 | 5.6x sr_airtime | up | 5 |
| `RT-hoplimit` | hop-limit | **text** | 0.695 → 0.880 | 0.185 | 0.657 → 0.879 | 2.1x sr_bytes | up | 4 |
| `MS-size` | nodes | **text** | 0.664 → 0.843 | 0.179 | 0.653 → 0.836 | 5.5x sr_bytes | down | 5 |
| `SF-hops-spread` | hops-apart | **held** | 0.776 → 0.947 | 0.171 | 0.791 → 0.797 | 4x sr_bytes | down | 5 |
| `AD-flooding` | role-mix | **text** | 0.711 → 0.882 | 0.170 | 0.701 → 0.876 | 2.5x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.711 → 0.882 | 0.170 | 0.701 → 0.876 | 2.5x bytes_on_air | up | 3 |
| `RF-noise` | noise-profile | **held** | 0.773 → 0.941 | 0.168 | 0.634 → 0.795 | 1.5x sr_airtime | down | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.695 → 0.862 | 0.167 | 0.657 → 0.859 | 2x sr_bytes | up | 3 |
| `SC-signing` | signature-policy | **text** | 0.648 → 0.803 | 0.155 | 0.648 → 0.795 | 1.3x sr_airtime | down | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.803 → 0.951 | 0.148 | 0.795 → 0.947 | 1.2x bytes_on_air | up | 3 |
| `DG-loss` | extra-loss | **text** | 0.681 → 0.803 | 0.122 | 0.667 → 0.795 | 1.4x sr_bytes | down | 4 |
| `MS-roles` | role-mix | **text** | 0.711 → 0.831 | 0.119 | 0.701 → 0.820 | 1.2x bytes_on_air | down | 2 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.803 → 0.915 | 0.112 | 0.795 → 0.906 | 2.2x sr_bytes | up | 3 |
| `RT-spread` | hop-spread | **text** | 0.695 → 0.803 | 0.108 | 0.657 → 0.795 | 1.7x sr_bytes | up | 2 |
| `MS-roles-fav` | role-mix | **text** | 0.733 → 0.839 | 0.106 | 0.723 → 0.832 | 1.1x advert_bytes | down | 2 |
| `DB-platform` | platform-mix | **text** | 0.713 → 0.817 | 0.104 | 0.698 → 0.810 | 2.1x sr_airtime | down | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.768 → 0.862 | 0.094 | 0.756 → 0.857 | 5.5x sr_airtime | up | 4 |
| `FW-firmware` | profile | **text** | 0.803 → 0.894 | 0.091 | 0.795 → 0.887 | 3x bytes_on_air | down | 2 |
| `DB-hotstore` | max-num-nodes | **text** | 0.726 → 0.817 | 0.090 | 0.712 → 0.810 | 2.2x sr_airtime | up | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.803 → 0.892 | 0.089 | 0.795 → 0.884 | 1.3x sr_bytes | up | 3 |
| `AD-badrouters` | role-placement | **text** | 0.711 → 0.800 | 0.088 | 0.701 → 0.790 | 1.4x sr_bytes | up | 3 |
| `FW-versions` | profile | **text** | 0.803 → 0.887 | 0.084 | 0.795 → 0.883 | 3.2x bytes_on_air | down | 5 |
| `FW-mixed` | legacy-fraction | **text** | 0.799 → 0.882 | 0.083 | 0.795 → 0.876 | 2.2x bytes_on_air | down | 4 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.803 → 0.878 | 0.075 | 0.795 → 0.874 | 2.2x bytes_on_air | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.871 → 0.939 | 0.067 | 0.795 → 0.801 | 20x sr_airtime | down | 3 |
| `SF-cadence` | trigger | **held** | 0.878 → 0.939 | 0.061 | 0.766 → 0.796 | 13x advert_bytes | down | 4 |
| `SF-servers-flat` | servers | **held** | 0.914 → 0.973 | 0.059 | 0.790 → 0.797 | 6.4x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.914 → 0.973 | 0.059 | 0.790 → 0.797 | 6.4x sr_bytes | up | 4 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.753 → 0.803 | 0.051 | 0.738 → 0.795 | 1.6x sr_airtime | down | 4 |
| `TH-congestion-input` | congestion-input | **held** | 0.747 → 0.790 | 0.042 | 0.485 → 0.522 | 1.6x sr_airtime | up | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.803 → 0.845 | 0.042 | 0.795 → 0.840 | 3.3x bytes_on_air | down | 2 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.633 → 0.673 | 0.040 | 0.623 → 0.664 | 1.2x sr_airtime | down | 2 |
| `SF-catchup` | catch-up-hours | **text** | 0.778 → 0.815 | 0.037 | 0.766 → 0.810 | 9.6x advert_bytes | up | 3 |
| `SF-capacity-window` | capacity | **held** | 0.901 → 0.934 | 0.032 | 0.787 → 0.801 | 2.1x advert_bytes | up | 3 |
| `SF-hops-flat` | hops-apart | **text** | 0.793 → 0.826 | 0.032 | 0.791 → 0.795 | 4x sr_bytes | up | 4 |
| `SF-provide-transport` | provide-transport | **text** | 0.803 → 0.827 | 0.024 | 0.787 → 0.795 | 3.1x sr_airtime | up | 2 |
| `AD-worst` | role-placement | **text** | 0.788 → 0.810 | 0.022 | 0.773 → 0.804 | 1.1x bytes_on_air | down | 2 |
| `SF-sr-retries` | sr-retries | **held** | 0.933 → 0.954 | 0.021 | 0.798 → 0.811 | 1.1x sr_bytes | down | 4 |
| `LD-diurnal` | diurnal | **text** | 0.803 → 0.823 | 0.020 | 0.795 → 0.816 | 1.3x advert_bytes | down | 3 |
| `MS-router-late` | router-late-fraction | **held** | 0.919 → 0.939 | 0.019 | 0.795 → 0.808 | 1.4x bytes_on_air | down | 4 |
| `SF-servers-allrouters` | servers | **held** | 0.926 → 0.942 | 0.016 | 0.788 → 0.792 | 3.1x sr_bytes | up | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.797 → 0.812 | 0.016 | 0.789 → 0.804 | 1.1x sr_bytes | up | 2 |
| `RT-hopassign` | hop-assign | **text** | 0.803 → 0.819 | 0.015 | 0.795 → 0.803 | 1.2x sr_bytes | up | 2 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.766 → 0.778 | 0.012 | 0.766 → 0.778 | 1x advert_bytes | down | 2 |
| `DM-mode` | dm-mode | **text** | 0.758 → 0.770 | 0.012 | 0.758 → 0.770 | 1.1x sr_airtime | up | 3 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.931 → 0.942 | 0.012 | 0.788 → 0.798 | 5.3x advert_bytes | up | 3 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.931 → 0.942 | 0.011 | 0.788 → 0.797 | 2.8x advert_bytes | down | 4 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.931 → 0.942 | 0.011 | 0.792 → 0.800 | 1.1x sr_airtime | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.931 → 0.942 | 0.011 | 0.792 → 0.800 | 1.1x sr_airtime | down | 4 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.941 → 0.951 | 0.010 | 0.939 → 0.950 | 1.1x sr_bytes | down | 2 |
| `SF-window-size` | window-size | **held** | 0.934 → 0.943 | 0.009 | 0.791 → 0.796 | 4.7x advert_bytes | down | 3 |
| `SF-capacity` | capacity | **held** | 0.933 → 0.942 | 0.009 | 0.792 → 0.799 | 5.3x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **held** | 0.933 → 0.942 | 0.009 | 0.792 → 0.799 | 5.3x advert_bytes | down | 5 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.770 → 0.778 | 0.008 | 0.770 → 0.778 | 1.1x sr_airtime | up | 2 |
| `PR-repeats` | extra-repeats | **text** | 0.803 → 0.810 | 0.007 | 0.795 → 0.803 | 1.1x sr_bytes | up | 2 |
| `SF-replay-order` | replay-ordering | **held** | 0.939 → 0.945 | 0.006 | 0.795 → 0.799 | 1.1x sr_bytes | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.935 → 0.941 | 0.006 | 0.933 → 0.939 | 1.2x sr_airtime | down | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.939 → 0.944 | 0.006 | 0.795 → 0.797 | 3x sr_airtime | up | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.941 → 0.945 | 0.004 | 0.939 → 0.943 | 1x bytes_on_air | up | 2 |
| `SF-resolve` | resolve | **held** | 0.935 → 0.939 | 0.004 | 0.792 → 0.795 | 5.7x advert_bytes | = | 3 |
| `SF-width` | short-id-bits | **text** | 0.800 → 0.804 | 0.004 | 0.791 → 0.795 | 3.1x advert_bytes | up | 4 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.827 → 0.830 | 0.003 | 0.787 → 0.789 | 1.1x sr_airtime | up | 2 |

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
| none | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| sprinkled | 1 | 0.841 | 0.837 | 0.004 | - | - | 0.951 | 0.953 | 0.316 | 1.40x | 18.3/29.9/32.8% | 2.2/5.2% | 3 |
| arms-race | 1 | 0.915 | 0.906 | 0.009 | - | - | 0.954 | 0.968 | 0.559 | 1.22x | 19.1/26.6/28.8% | 1.7/5.4% | 3 |

> amplifier-mix=arms-race: decode_failures 33

> slower: 4.29 s per simulated hour against 1.58 over 72 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-amplify-worst` - amplify-worst  `--scenario alpine`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.882 | 0.873 | 0.009 | - | - | 0.988 | 0.990 | 0.224 | 1.31x | 18.8/26.3/28.4% | 1.9/5.2% | 3 |
| 0.3 | 1 | 0.951 | 0.947 | 0.005 | - | - | 0.999 | 0.999 | 0.858 | 1.06x | 19.7/24.6/28.6% | 1.4/5.0% | 3 |

### `AD-badrouters` - role-placement  `--scenario alpine`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.711 | 0.701 | 0.011 | - | - | 0.868 | 0.870 | 0.000 | 1.10x | 15.9/23.7/27.2% | 1.7/5.1% | 3 |
| inverse | 1 | 0.773 | 0.761 | 0.013 | - | - | 0.892 | 0.895 | 0.341 | 1.11x | 14.2/19.5/22.3% | 2.0/3.2% | 3 |
| random | 1 | 0.800 | 0.790 | 0.010 | - | - | 0.928 | 0.931 | 0.212 | 1.17x | 14.4/19.6/24.3% | 2.0/4.7% | 3 |

> role-placement=inverse: decode_failures 1

### `AD-flooding` - role-mix  `--scenario alpine`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.711 | 0.701 | 0.011 | - | - | 0.868 | 0.870 | 0.000 | 1.10x | 15.9/23.7/27.2% | 1.7/5.1% | 3 |
| all-routers | 1 | 0.882 | 0.876 | 0.006 | - | - | 0.953 | 0.954 | 0.664 | 2.70x | 34.3/45.8/47.7% | 4.4/5.3% | 3 |

### `AD-nomute` - role-mix  `--scenario alpine`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.711 | 0.701 | 0.011 | - | - | 0.868 | 0.870 | 0.000 | 1.10x | 15.9/23.7/27.2% | 1.7/5.1% | 3 |
| no-mute | 1 | 0.822 | 0.808 | 0.014 | - | - | 0.951 | 0.952 | 0.248 | 1.29x | 16.8/23.7/27.0% | 2.0/5.1% | 3 |
| all-routers | 1 | 0.882 | 0.876 | 0.006 | - | - | 0.953 | 0.954 | 0.664 | 2.70x | 34.3/45.8/47.7% | 4.4/5.3% | 3 |

### `AD-siting` - siting-mix  `--scenario alpine`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.711 | 0.701 | 0.011 | - | - | 0.868 | 0.870 | 0.000 | 1.10x | 15.9/23.7/27.2% | 1.7/5.1% | 3 |
| local-typical | 1 | 0.674 | 0.667 | 0.007 | - | - | 0.857 | 0.858 | 0.000 | 1.22x | 12.0/23.4/29.0% | 1.9/5.1% | 3 |
| basement-heavy | 1 | 0.079 | 0.078 | 0.001 | - | - | 0.189 | 0.190 | 0.000 | 0.49x | 0.6/6.4/8.5% | 0.3/2.5% | 3 |

### `AD-worst` - role-placement  `--scenario alpine`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.810 | 0.804 | 0.006 | - | - | 0.936 | 0.937 | 0.000 | 2.41x | 17.1/29.9/37.3% | 1.9/5.8% | 3 |
| inverse | 1 | 0.788 | 0.773 | 0.015 | - | - | 0.951 | 0.951 | 0.000 | 2.25x | 14.1/24.6/32.9% | 1.8/3.2% | 3 |

### `BL-control` - protocol  `--scenario alpine`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.802 | 0.802 | 0.000 | - | - | 0 | 0.000 | 0.202 | 1.27x | 17.9/25.2/27.4% | 1.8/5.1% | 3 |
| sr | 1 | 0.826 | 0.792 | 0.033 | - | - | 0.947 | 0.967 | 0.202 | 1.31x | 18.2/25.8/28.2% | 1.9/5.3% | 3 |

> protocol=sr: decode_failures 15

> slower: 3.92 s per simulated hour against 1.82 over 72 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `DB-hotstore` - max-num-nodes  `--scenario alpine`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.726 | 0.712 | 0.014 | - | - | 0.850 | 0.851 | 0.256 | 3.02x | 39.1/65.1/68.1% | 4.3/10.2% | 3 |
| 100 | 1 | 0.817 | 0.810 | 0.006 | - | - | 0.924 | 0.925 | 0.175 | 1.59x | 20.7/37.7/40.1% | 2.1/5.5% | 3 |
| 120 | 1 | 0.817 | 0.810 | 0.006 | - | - | 0.924 | 0.925 | 0.175 | 1.59x | 20.7/37.7/40.1% | 2.1/5.5% | 3 |
| 250 | 1 | 0.817 | 0.810 | 0.006 | - | - | 0.924 | 0.925 | 0.175 | 1.59x | 20.7/37.7/40.1% | 2.1/5.5% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario alpine`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.305 | 0.299 | 0.006 | - | - | 0.492 | 0.523 | 0.053 | 11.12x | 36.9/64.5/73.4% | 3.8/10.0% | 3 |
| 120 | 1 | 0.495 | 0.485 | 0.009 | - | - | 0.747 | 0.749 | 0.064 | 4.60x | 15.1/32.5/39.8% | 1.5/5.5% | 3 |
| 250 | 1 | 0.501 | 0.492 | 0.009 | - | - | 0.747 | 0.748 | 0.065 | 4.44x | 14.6/30.9/38.0% | 1.4/5.0% | 3 |

> max-num-nodes=10: decode_failures 71

> max-num-nodes=120: decode_failures 2

### `DB-platform` - platform-mix  `--scenario alpine`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.817 | 0.810 | 0.006 | - | - | 0.924 | 0.925 | 0.175 | 1.59x | 20.7/37.7/40.1% | 2.1/5.5% | 3 |
| baymesh-2026-08 | 1 | 0.817 | 0.810 | 0.006 | - | - | 0.924 | 0.925 | 0.175 | 1.59x | 20.7/37.7/40.1% | 2.1/5.5% | 3 |
| constrained | 1 | 0.713 | 0.698 | 0.015 | - | - | 0.836 | 0.837 | 0.233 | 3.02x | 39.1/65.1/68.2% | 4.3/10.2% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario alpine`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.673 | 0.664 | 0.009 | - | - | 0.808 | 0.832 | 0.351 | 5.87x | 53.9/75.9/79.9% | 4.3/13.2% | 3 |
| 25 | 1 | 0.673 | 0.664 | 0.009 | - | - | 0.808 | 0.832 | 0.351 | 5.87x | 53.9/75.9/79.9% | 4.3/13.2% | 3 |
| 100 | 1 | 0.673 | 0.664 | 0.009 | - | - | 0.808 | 0.832 | 0.351 | 5.87x | 53.9/75.9/79.9% | 4.3/13.2% | 3 |
| 2000 | 1 | 0.673 | 0.664 | 0.009 | - | - | 0.808 | 0.832 | 0.351 | 5.87x | 53.9/75.9/79.9% | 4.3/13.2% | 3 |

> warm-num-nodes=0: queue drops 16.8% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 79

> warm-num-nodes=25: queue drops 16.8% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 79

> warm-num-nodes=100: queue drops 16.8% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 79

> warm-num-nodes=2000: queue drops 16.8% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 79

### `DG-burst` - burst-loss  `--scenario alpine`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.711 | 0.693 | 0.018 | - | - | 0.911 | 0.914 | 0.184 | 1.22x | 17.4/24.7/27.0% | 1.8/4.9% | 3 |
| 0.2 | 1 | 0.606 | 0.572 | 0.033 | - | - | 0.840 | 0.848 | 0.176 | 1.13x | 16.3/23.3/25.4% | 1.7/4.5% | 3 |
| 0.3 | 1 | 0.498 | 0.458 | 0.039 | - | - | 0.755 | 0.772 | 0.129 | 1.03x | 15.1/21.7/23.8% | 1.5/3.9% | 3 |

> burst-loss=0.2: decode_failures 4

> burst-loss=0.3: decode_failures 26

### `DG-loss` - extra-loss  `--scenario alpine`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.761 | 0.751 | 0.010 | - | - | 0.905 | 0.907 | 0.192 | 1.35x | 19.1/26.6/29.1% | 2.0/5.1% | 3 |
| 0.2 | 1 | 0.728 | 0.717 | 0.011 | - | - | 0.893 | 0.895 | 0.205 | 1.37x | 19.5/27.9/30.2% | 2.0/5.0% | 3 |
| 0.3 | 1 | 0.681 | 0.667 | 0.014 | - | - | 0.841 | 0.865 | 0.206 | 1.36x | 19.4/28.1/30.3% | 2.1/4.7% | 3 |

> extra-loss=0.3: decode_failures 27

### `DG-outage` - burst-loss  `--scenario alpine`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 0.1 | 1 | 0.692 | 0.679 | 0.013 | - | - | 0.864 | 0.888 | 0.133 | 1.23x | 17.5/24.8/27.0% | 1.8/5.0% | 3 |
| 0.2 | 1 | 0.581 | 0.559 | 0.022 | - | - | 0.790 | 0.850 | 0.165 | 1.12x | 16.2/23.1/25.3% | 1.7/4.5% | 3 |
| 0.3 | 1 | 0.481 | 0.456 | 0.026 | - | - | 0.644 | 0.746 | 0.097 | 1.06x | 15.6/22.4/24.2% | 1.6/4.3% | 3 |

> burst-loss=0.1: decode_failures 55

> burst-loss=0.2: decode_failures 34

> burst-loss=0.3: decode_failures 35

### `DM-mode` - dm-mode  `--scenario alpine`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.758 | 0.758 | 0.000 | - | - | 0.912 | 0.914 | 0.186 | 1.72x | 23.7/34.2/36.9% | 2.5/6.9% | 3 |
| directed-with-late-flood | 1 | 0.770 | 0.770 | 0.000 | - | - | 0.919 | 0.922 | 0.193 | 1.56x | 21.6/31.4/34.1% | 2.2/6.4% | 3 |
| m4-early-flood | 1 | 0.770 | 0.770 | 0.000 | - | - | 0.920 | 0.921 | 0.205 | 1.57x | 21.7/31.6/34.1% | 2.3/6.4% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 4

> dm-mode=m4-early-flood: decode_failures 3

### `FW-firmware` - profile  `--scenario alpine`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.894 | 0.887 | 0.007 | - | - | 0.977 | 0.978 | 0.702 | 0.77x | 9.2/12.9/13.9% | 1.3/2.1% | 3 |
| 2.8 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario alpine`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 0.25 | 1 | 0.826 | 0.823 | 0.004 | - | - | 0.900 | 0.904 | 0.343 | 1.27x | 15.9/26.6/30.2% | 1.9/4.8% | 3 |
| 0.5 | 1 | 0.882 | 0.876 | 0.006 | - | - | 0.939 | 0.940 | 0.624 | 1.11x | 13.2/21.4/24.2% | 1.7/4.1% | 3 |
| 0.75 | 1 | 0.799 | 0.796 | 0.003 | - | - | 0.930 | 0.930 | 0.253 | 0.86x | 9.9/16.6/18.4% | 1.4/3.5% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario alpine`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 0.25 | 1 | 0.818 | 0.814 | 0.004 | - | - | 0.892 | 0.895 | 0.368 | 1.23x | 15.5/25.9/29.6% | 1.9/4.7% | 3 |
| 0.5 | 1 | 0.878 | 0.874 | 0.004 | - | - | 0.946 | 0.948 | 0.615 | 1.07x | 13.2/21.0/23.8% | 1.7/4.1% | 3 |
| 0.75 | 1 | 0.806 | 0.804 | 0.002 | - | - | 0.939 | 0.940 | 0.249 | 0.84x | 10.2/16.7/18.6% | 1.3/3.5% | 3 |

> legacy-fraction=0.25: decode_failures 1

### `FW-signing-cost` - profile-flag  `--scenario alpine`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.845 | 0.840 | 0.005 | - | - | 0.967 | 0.969 | 0.164 | 0.69x | 10.3/14.8/16.1% | 1.0/3.0% | 3 |
| signing=true | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |

### `FW-versions` - profile  `--scenario alpine`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.876 | 0.870 | 0.006 | - | - | 0.958 | 0.960 | 0.665 | 0.77x | 9.7/14.2/15.5% | 1.2/2.1% | 3 |
| 2.5 | 1 | 0.876 | 0.869 | 0.008 | - | - | 0.968 | 0.968 | 0.652 | 0.76x | 9.4/13.7/15.0% | 1.2/2.1% | 3 |
| 2.6 | 1 | 0.878 | 0.872 | 0.006 | - | - | 0.966 | 0.970 | 0.663 | 0.73x | 9.3/13.8/15.0% | 1.2/2.0% | 3 |
| 2.7 | 1 | 0.887 | 0.883 | 0.004 | - | - | 0.961 | 0.963 | 0.654 | 0.80x | 10.6/18.4/20.2% | 1.2/3.3% | 3 |
| 2.8 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |

> profile=2.6: decode_failures 2

### `LD-chatty` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.843 | 0.838 | 0.005 | - | - | 0.966 | 0.966 | 0.194 | 0.88x | 12.3/17.2/18.7% | 1.3/3.5% | 3 |
| 900 | 1 | 0.768 | 0.756 | 0.013 | - | - | 0.909 | 0.910 | 0.183 | 2.06x | 28.6/40.6/43.8% | 2.9/8.2% | 3 |
| 300 | 1 | 0.531 | 0.512 | 0.019 | - | - | 0.730 | 0.747 | 0.147 | 4.52x | 56.5/73.7/76.7% | 6.7/16.2% | 3 |

> broadcast-interval-s=300: decode_failures 22

### `LD-chatty-hops` - broadcast-interval-s  `--scenario alpine`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.896 | 0.894 | 0.001 | - | - | 0.982 | 0.983 | 0.201 | 0.95x | 13.0/17.6/19.0% | 1.4/3.5% | 3 |
| 900 | 1 | 0.848 | 0.842 | 0.005 | - | - | 0.942 | 0.944 | 0.218 | 2.32x | 31.4/42.9/46.4% | 3.4/8.5% | 3 |
| 300 | 1 | 0.585 | 0.577 | 0.008 | - | - | 0.732 | 0.761 | 0.180 | 4.86x | 58.8/74.9/77.9% | 7.1/16.9% | 3 |

> broadcast-interval-s=3600: misdecodes 1

> broadcast-interval-s=300: queue drops 10.8% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 44

### `LD-diurnal` - diurnal  `--scenario alpine`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.823 | 0.816 | 0.007 | - | - | 0.947 | 0.948 | 0.200 | 1.22x | 17.1/24.2/26.3% | 1.8/4.9% | 3 |
| sinusoid | 1 | 0.818 | 0.808 | 0.009 | - | - | 0.950 | 0.953 | 0.206 | 1.17x | 16.5/23.2/25.2% | 1.7/4.6% | 3 |
| commuter | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.768 | 0.756 | 0.013 | - | - | 0.909 | 0.910 | 0.183 | 2.06x | 28.6/40.6/43.8% | 2.9/8.2% | 3 |
| 3600 | 1 | 0.843 | 0.838 | 0.005 | - | - | 0.966 | 0.966 | 0.194 | 0.88x | 12.3/17.2/18.7% | 1.3/3.5% | 3 |
| 10800 | 1 | 0.856 | 0.851 | 0.005 | - | - | 0.972 | 0.972 | 0.214 | 0.58x | 8.1/11.4/12.4% | 0.9/2.3% | 3 |
| 43200 | 1 | 0.862 | 0.857 | 0.005 | - | - | 0.981 | 0.981 | 0.196 | 0.41x | 5.8/8.2/8.9% | 0.6/1.7% | 3 |

> broadcast-interval-s=10800: misdecodes 1

### `LD-traceroute` - traceroute-per-hour  `--scenario alpine`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 0.25 | 1 | 0.802 | 0.793 | 0.009 | - | - | 0.935 | 0.935 | 0.212 | 1.36x | 19.1/27.1/29.4% | 2.0/5.4% | 3 |
| 1.0 | 1 | 0.788 | 0.777 | 0.011 | - | - | 0.928 | 0.930 | 0.186 | 1.50x | 21.2/30.1/32.6% | 2.1/6.1% | 3 |
| 4.0 | 1 | 0.753 | 0.738 | 0.015 | - | - | 0.912 | 0.913 | 0.186 | 1.89x | 26.8/38.0/41.1% | 2.7/7.8% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario alpine`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.673 | 0.664 | 0.009 | - | - | 0.808 | 0.832 | 0.351 | 5.87x | 53.9/75.9/79.9% | 4.3/13.2% | 3 |
| 1.0 | 1 | 0.633 | 0.623 | 0.011 | - | - | 0.772 | 0.794 | 0.331 | 6.25x | 56.7/76.9/80.7% | 4.7/14.0% | 3 |

> traceroute-per-hour=0.0: queue drops 16.8% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 79

> traceroute-per-hour=1.0: queue drops 22.3% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 102

### `MS-density` - nodes  `--scenario alpine`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.711 | 0.701 | 0.009 | - | - | 0.889 | 0.890 | 0.000 | 1.42x | 24.2/32.1/35.3% | 3.4/7.1% | 3 |
| 60 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 90 | 1 | 0.905 | 0.899 | 0.006 | - | - | 0.974 | 0.974 | 0.537 | 1.54x | 17.0/29.0/31.2% | 1.5/4.9% | 3 |
| 120 | 1 | 0.941 | 0.939 | 0.003 | - | - | 0.990 | 0.990 | 0.608 | 2.13x | 19.8/39.2/43.3% | 1.5/5.3% | 3 |
| 150 | 1 | 0.943 | 0.940 | 0.003 | - | - | 0.997 | 0.997 | 0.678 | 2.76x | 24.8/45.2/49.9% | 1.4/5.6% | 3 |

> nodes=120: misdecodes 1

> nodes=150: decode_failures 4

### `MS-hopscale` - nodes  `--scenario alpine`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 120 | 1 | 0.734 | 0.725 | 0.008 | - | - | 0.915 | 0.915 | 0.302 | 2.21x | 14.4/28.8/34.1% | 1.5/5.4% | 3 |
| 250 | 1 | 0.495 | 0.485 | 0.010 | - | - | 0.743 | 0.744 | 0.071 | 4.96x | 16.4/35.1/43.0% | 1.6/5.8% | 3 |
| 500 | 1 | 0.334 | 0.331 | 0.003 | - | - | 0.457 | 0.457 | 0.038 | 10.41x | 20.1/31.6/47.0% | 1.8/7.0% | 3 |

> nodes=250: decode_failures 1

> nodes=500: decode_failures 21

### `MS-oversubscribed` - nodes  `--scenario alpine`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.731 | 0.722 | 0.009 | - | - | 0.924 | 0.925 | 0.300 | 2.09x | 13.8/27.3/32.2% | 1.4/5.0% | 3 |
| 250 | 1 | 0.495 | 0.485 | 0.009 | - | - | 0.747 | 0.749 | 0.064 | 4.60x | 15.1/32.5/39.8% | 1.5/5.5% | 3 |
| 500 | 1 | 0.337 | 0.333 | 0.004 | - | - | 0.473 | 0.474 | 0.045 | 9.61x | 18.3/29.0/43.1% | 1.6/6.3% | 3 |

> nodes=250: decode_failures 2

> nodes=500: decode_failures 30

### `MS-roles` - role-mix  `--scenario alpine`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.831 | 0.820 | 0.011 | - | - | 0.966 | 0.967 | 0.176 | 1.30x | 18.3/25.9/28.3% | 1.9/5.2% | 3 |
| baymesh-2026-08 | 1 | 0.711 | 0.701 | 0.011 | - | - | 0.868 | 0.870 | 0.000 | 1.10x | 15.9/23.7/27.2% | 1.7/5.1% | 3 |

### `MS-roles-fav` - role-mix  `--scenario alpine`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.839 | 0.832 | 0.007 | - | - | 0.954 | 0.959 | 0.210 | 1.34x | 18.8/26.5/28.8% | 2.0/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.733 | 0.723 | 0.010 | - | - | 0.860 | 0.860 | 0.000 | 1.25x | 18.0/28.0/31.5% | 2.0/5.0% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario alpine`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 0.05 | 1 | 0.809 | 0.800 | 0.009 | - | - | 0.937 | 0.939 | 0.202 | 1.46x | 19.8/33.1/36.8% | 2.1/5.4% | 3 |
| 0.1 | 1 | 0.807 | 0.799 | 0.008 | - | - | 0.935 | 0.937 | 0.188 | 1.53x | 20.9/37.6/40.8% | 2.0/5.4% | 3 |
| 0.2 | 1 | 0.818 | 0.808 | 0.010 | - | - | 0.919 | 0.920 | 0.494 | 1.78x | 24.3/42.9/46.2% | 2.5/5.3% | 3 |

### `MS-siting` - siting-mix  `--scenario alpine`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| local-typical | 1 | 0.667 | 0.664 | 0.003 | - | - | 0.780 | 0.780 | 0.000 | 1.47x | 13.1/26.8/30.1% | 2.4/4.9% | 3 |
| event | 1 | 0.144 | 0.144 | 0.000 | - | - | 0.196 | 0.199 | 0.000 | 1.00x | 5.3/10.6/16.6% | 1.6/3.8% | 3 |
| backbone | 1 | 0.972 | 0.971 | 0.001 | - | - | 0.999 | 0.999 | 0.775 | 1.13x | 25.2/32.2/35.9% | 1.4/5.7% | 3 |

### `MS-size` - nodes  `--scenario alpine`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.843 | 0.836 | 0.008 | - | - | 0.957 | 0.957 | 0.224 | 1.46x | 28.6/37.3/39.9% | 3.6/7.9% | 3 |
| 60 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 90 | 1 | 0.744 | 0.729 | 0.015 | - | - | 0.922 | 0.923 | 0.233 | 1.78x | 16.7/31.5/35.7% | 1.7/5.4% | 3 |
| 120 | 1 | 0.734 | 0.725 | 0.008 | - | - | 0.915 | 0.915 | 0.302 | 2.21x | 14.4/28.8/34.1% | 1.5/5.4% | 3 |
| 150 | 1 | 0.664 | 0.653 | 0.012 | - | - | 0.849 | 0.850 | 0.158 | 2.89x | 15.4/41.5/47.4% | 1.6/5.4% | 3 |

> nodes=150: decode_failures 2

### `MS-stretch` - stretch  `--scenario alpine`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 1.25 | 1 | 0.607 | 0.590 | 0.017 | - | - | 0.797 | 0.818 | 0.217 | 1.40x | 12.7/19.1/21.6% | 2.1/5.3% | 3 |
| 1.5 | 1 | 0.305 | 0.301 | 0.004 | - | - | 0.472 | 0.475 | 0.000 | 1.31x | 8.5/19.3/24.3% | 2.0/5.2% | 3 |
| 2.0 | 1 | 0.137 | 0.136 | 0.001 | - | - | 0.283 | 0.283 | 0.000 | 0.92x | 4.0/14.5/19.2% | 1.0/4.3% | 3 |

> stretch=1.25: decode_failures 20

### `MS-topology` - topology  `--scenario alpine`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| clustered | 1 | 0.834 | 0.834 | 0.001 | - | - | 0.924 | 0.924 | 0.000 | 1.02x | 27.2/34.5/35.8% | 1.2/5.8% | 3 |
| corridor | 1 | 0.429 | 0.422 | 0.007 | - | - | 0.519 | 0.523 | 0.287 | 1.40x | 18.8/27.4/29.8% | 1.9/6.2% | 3 |
| hub | 1 | 0.924 | 0.919 | 0.005 | - | - | 0.984 | 0.985 | 0.609 | 1.26x | 25.0/36.9/38.6% | 1.9/5.6% | 3 |

### `PR-crladder` - coding-rate-ladder  `--scenario alpine`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.770 | 0.770 | 0.000 | - | - | 0.919 | 0.922 | 0.193 | 1.56x | 21.6/31.4/34.1% | 2.2/6.4% | 3 |
| True | 1 | 0.778 | 0.778 | 0.000 | - | - | 0.927 | 0.930 | 0.188 | 1.57x | 21.7/31.8/34.4% | 2.3/6.6% | 3 |

> coding-rate-ladder=False: decode_failures 4

### `PR-dmmode-cr` - dm-mode  `--scenario alpine`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.778 | 0.778 | 0.000 | - | - | 0.927 | 0.930 | 0.188 | 1.57x | 21.7/31.8/34.4% | 2.3/6.6% | 3 |
| m4-early-flood | 1 | 0.766 | 0.766 | 0.000 | - | - | 0.918 | 0.919 | 0.203 | 1.57x | 21.4/31.7/34.2% | 2.3/6.5% | 3 |

### `PR-protocol` - protocol  `--scenario alpine`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.802 | 0.802 | 0.000 | - | - | 0 | 0.000 | 0.202 | 1.27x | 17.9/25.2/27.4% | 1.8/5.1% | 3 |
| chain | 1 | 0.794 | 0.792 | 0.002 | - | - | 0.870 | 0.936 | 0.200 | 1.50x | 20.6/29.8/32.5% | 2.2/6.0% | 3 |
| sr | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |

### `PR-repeats` - extra-repeats  `--scenario alpine`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| True | 1 | 0.810 | 0.803 | 0.007 | - | - | 0.937 | 0.939 | 0.190 | 1.30x | 18.2/25.9/28.1% | 1.9/5.2% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario alpine`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.941 | 0.939 | 0.003 | - | - | 0.990 | 0.990 | 0.608 | 2.13x | 19.8/39.2/43.3% | 1.5/5.3% | 3 |
| True | 1 | 0.945 | 0.943 | 0.002 | - | - | 0.993 | 0.994 | 0.614 | 2.21x | 20.7/40.3/44.4% | 1.5/5.4% | 3 |

> extra-repeats=False: misdecodes 1

### `RF-bw500` - preset  `--scenario alpine`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.179 | 0.173 | 0.005 | - | - | 0.343 | 0.343 | 0.000 | 0.05x | 0.3/0.7/1.0% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.430 | 0.410 | 0.020 | - | - | 0.683 | 0.685 | 0.000 | 0.27x | 2.0/4.4/6.1% | 0.4/1.1% | 3 |
| LONG_TURBO | 1 | 0.721 | 0.714 | 0.007 | - | - | 0.871 | 0.871 | 0.278 | 1.26x | 13.6/24.6/27.3% | 1.8/5.0% | 3 |

### `RF-duct` - duct-per-hour  `--scenario alpine`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 0.25 | 1 | 0.823 | 0.812 | 0.011 | - | - | 0.945 | 0.945 | 0.266 | 1.25x | 18.7/26.1/28.1% | 1.8/5.2% | 3 |
| 1.0 | 1 | 0.892 | 0.884 | 0.008 | - | - | 0.968 | 0.968 | 0.536 | 1.03x | 20.8/27.5/30.5% | 1.4/5.2% | 3 |

### `RF-eu-presets` - preset  `--scenario alpine`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.325 | 0.324 | 0.001 | - | - | 0.508 | 0.509 | 0.000 | 0.15x | 1.1/2.7/3.4% | 0.2/0.7% | 3 |
| LONG_FAST | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| LITE_FAST | 1 | 0.753 | 0.746 | 0.007 | - | - | 0.883 | 0.885 | 0.276 | 0.99x | 11.6/20.2/24.0% | 1.4/4.1% | 3 |
| NARROW_SLOW | 1 | 0.763 | 0.755 | 0.008 | - | - | 0.877 | 0.879 | 0.223 | 1.28x | 15.1/26.0/29.0% | 1.9/5.1% | 3 |

> preset=NARROW_SLOW: decode_failures 2

### `RF-noise` - noise-profile  `--scenario alpine`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| temporal | 1 | 0.730 | 0.716 | 0.014 | - | - | 0.902 | 0.904 | 0.197 | 1.33x | 17.7/25.7/28.5% | 2.0/5.1% | 3 |
| transient | 1 | 0.801 | 0.792 | 0.009 | - | - | 0.941 | 0.943 | 0.187 | 1.32x | 18.4/26.2/28.5% | 1.9/5.3% | 3 |
| periodic | 1 | 0.643 | 0.634 | 0.010 | - | - | 0.773 | 0.780 | 0.186 | 1.20x | 16.8/23.7/26.0% | 1.7/4.5% | 3 |

### `RF-preset` - preset  `--scenario alpine`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.325 | 0.324 | 0.001 | - | - | 0.508 | 0.509 | 0.000 | 0.15x | 1.1/2.7/3.4% | 0.2/0.7% | 3 |
| LONG_FAST | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| LONG_MODERATE | 1 | 0.784 | 0.770 | 0.014 | - | - | 0.867 | 0.898 | 0.395 | 3.31x | 48.9/61.3/65.8% | 4.6/13.5% | 3 |

> preset=LONG_MODERATE: decode_failures 53

### `RF-preset-turbo` - preset  `--scenario alpine`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.073 | 0.072 | 0.001 | - | - | 0.120 | 0.123 | 0.000 | 0.01x | 0.0/0.1/0.2% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.179 | 0.173 | 0.005 | - | - | 0.343 | 0.343 | 0.000 | 0.05x | 0.3/0.7/1.0% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| LONG_TURBO | 1 | 0.721 | 0.714 | 0.007 | - | - | 0.871 | 0.871 | 0.278 | 1.26x | 13.6/24.6/27.3% | 1.8/5.0% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.787 | 0.776 | 0.011 | - | - | 0.908 | 0.911 | 0.215 | 1.83x | 22.5/36.3/38.7% | 2.7/6.9% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario alpine`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.752 | 0.742 | 0.010 | - | - | 0.883 | 0.889 | 0.180 | 1.27x | 18.0/25.3/27.5% | 1.9/4.9% | 3 |
| 10000 | 1 | 0.643 | 0.634 | 0.010 | - | - | 0.773 | 0.780 | 0.186 | 1.20x | 16.8/23.7/26.0% | 1.7/4.5% | 3 |
| 4000 | 1 | 0.408 | 0.403 | 0.006 | - | - | 0.495 | 0.533 | 0.092 | 1.02x | 14.4/20.5/22.5% | 1.5/3.5% | 3 |
| 2000 | 1 | 0.096 | 0.096 | 0.000 | - | - | 0.114 | 0.175 | 0.023 | 0.71x | 10.3/15.2/16.8% | 1.1/2.1% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 3

### `RF-stretch-duct` - duct-per-hour  `--scenario alpine`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.305 | 0.301 | 0.004 | - | - | 0.472 | 0.475 | 0.000 | 1.31x | 8.5/19.3/24.3% | 2.0/5.2% | 3 |
| 1.0 | 1 | 0.634 | 0.631 | 0.003 | - | - | 0.742 | 0.742 | 0.171 | 1.09x | 13.7/22.0/24.1% | 1.5/4.6% | 3 |

### `RF-txpower` - tx-power  `--scenario alpine`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 22 | 1 | 0.401 | 0.383 | 0.018 | - | - | 0.607 | 0.608 | 0.000 | 1.33x | 10.3/20.0/26.0% | 1.9/4.9% | 3 |
| 17 | 1 | 0.164 | 0.161 | 0.002 | - | - | 0.298 | 0.300 | 0.000 | 1.06x | 6.9/16.0/20.8% | 1.5/4.7% | 3 |
| 14 | 1 | 0.104 | 0.101 | 0.003 | - | - | 0.264 | 0.274 | 0.000 | 0.74x | 3.6/8.6/11.9% | 1.1/3.6% | 3 |

> tx-power=14: decode_failures 13

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario alpine`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.941 | 0.939 | 0.003 | - | - | 0.990 | 0.990 | 0.608 | 2.13x | 19.8/39.2/43.3% | 1.5/5.3% | 3 |
| True | 1 | 0.935 | 0.933 | 0.002 | - | - | 0.988 | 0.989 | 0.602 | 2.49x | 23.3/44.4/48.9% | 1.7/5.8% | 3 |

> no-adopt-hop-recommendation=False: misdecodes 1

### `RT-favourites` - favourite-routers  `--scenario alpine`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.797 | 0.789 | 0.008 | - | - | 0.925 | 0.926 | 0.189 | 1.42x | 19.0/32.3/35.0% | 2.1/5.4% | 3 |
| True | 1 | 0.812 | 0.804 | 0.008 | - | - | 0.918 | 0.921 | 0.188 | 1.46x | 19.2/32.3/35.2% | 2.1/5.3% | 3 |

### `RT-hopassign` - hop-assign  `--scenario alpine`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| random | 1 | 0.819 | 0.803 | 0.015 | - | - | 0.948 | 0.950 | 0.170 | 1.29x | 18.3/25.6/27.8% | 1.8/5.2% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario alpine`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.695 | 0.657 | 0.038 | - | - | 0.904 | 0.910 | 0.116 | 0.99x | 14.2/21.5/23.6% | 1.4/4.4% | 3 |
| 7 | 1 | 0.862 | 0.859 | 0.003 | - | - | 0.954 | 0.954 | 0.177 | 1.42x | 19.4/26.7/29.0% | 2.1/5.3% | 3 |
| 15 | 1 | 0.877 | 0.876 | 0.001 | - | - | 0.955 | 0.957 | 0.183 | 1.44x | 19.7/26.9/29.2% | 2.2/5.4% | 3 |
| 32 | 1 | 0.880 | 0.879 | 0.001 | - | - | 0.957 | 0.958 | 0.196 | 1.44x | 19.6/26.8/29.1% | 2.2/5.3% | 3 |

### `RT-hopspread` - hop-limit  `--scenario alpine`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.695 | 0.657 | 0.038 | - | - | 0.904 | 0.910 | 0.116 | 0.99x | 14.2/21.5/23.6% | 1.4/4.4% | 3 |
| 5 | 1 | 0.824 | 0.811 | 0.013 | - | - | 0.951 | 0.953 | 0.167 | 1.33x | 18.6/26.0/28.3% | 1.9/5.2% | 3 |
| 7 | 1 | 0.862 | 0.859 | 0.003 | - | - | 0.954 | 0.954 | 0.177 | 1.42x | 19.4/26.7/29.0% | 2.1/5.3% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario alpine`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| KNOWN_ONLY | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.802 | 0.801 | 0.000 | - | - | 0.871 | 0.945 | 0.184 | 1.25x | 17.6/24.8/27.0% | 1.8/5.0% | 3 |

### `RT-spread` - hop-spread  `--scenario alpine`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.695 | 0.657 | 0.038 | - | - | 0.904 | 0.910 | 0.116 | 0.99x | 14.2/21.5/23.6% | 1.4/4.4% | 3 |
| True | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |

### `SC-signing` - signature-policy  `--scenario alpine`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| BALANCED | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| STRICT | 1 | 0.648 | 0.648 | 0.000 | - | - | 0.800 | 0.801 | 0.109 | 1.43x | 20.1/28.3/30.7% | 2.1/5.6% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario alpine`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| dm | 1 | 0.807 | 0.797 | 0.010 | - | - | 0.944 | 0.944 | 0.197 | 1.27x | 17.9/25.5/27.7% | 1.8/5.2% | 3 |

> advert-transport=dm: misdecodes 1

### `SF-bucket-mode` - bucket-mode  `--scenario alpine`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.807 | 0.797 | 0.010 | - | - | 0.942 | 0.942 | 0.199 | 1.30x | 18.3/25.8/27.9% | 1.9/5.2% | 3 |
| local | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| time | 1 | 0.797 | 0.788 | 0.009 | - | - | 0.931 | 0.931 | 0.187 | 1.34x | 18.9/26.6/28.8% | 2.0/5.4% | 3 |
| window | 1 | 0.803 | 0.794 | 0.009 | - | - | 0.934 | 0.938 | 0.191 | 1.29x | 18.2/25.7/27.9% | 1.9/5.2% | 3 |

> bucket-mode=global: misdecodes 42

> bucket-mode=time: misdecodes 38

> bucket-mode=window: misdecodes 22

### `SF-bucket-time` - time-bucket-s  `--scenario alpine`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.798 | 0.788 | 0.010 | - | - | 0.939 | 0.941 | 0.188 | 1.44x | 19.4/28.9/31.2% | 2.1/5.8% | 3 |
| 1800 | 1 | 0.797 | 0.788 | 0.009 | - | - | 0.931 | 0.931 | 0.187 | 1.34x | 18.9/26.6/28.8% | 2.0/5.4% | 3 |
| 3600 | 1 | 0.807 | 0.798 | 0.009 | - | - | 0.942 | 0.946 | 0.182 | 1.30x | 18.3/26.0/28.1% | 1.9/5.2% | 3 |

> time-bucket-s=600: misdecodes 110

> time-bucket-s=1800: misdecodes 38

> time-bucket-s=3600: misdecodes 11

> time-bucket-s=3600: decode_failures 3

### `SF-cadence` - trigger  `--scenario alpine`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| interval | 1 | 0.779 | 0.769 | 0.009 | - | - | 0.914 | 0.921 | 0.194 | 1.77x | 22.7/35.8/38.9% | 2.6/8.0% | 3 |
| aimd | 1 | 0.798 | 0.796 | 0.002 | - | - | 0.878 | 0.935 | 0.170 | 1.30x | 18.2/25.8/28.0% | 1.9/5.2% | 3 |
| bucket+interval | 1 | 0.778 | 0.766 | 0.011 | - | - | 0.914 | 0.915 | 0.193 | 1.78x | 23.0/35.6/38.9% | 2.6/7.5% | 3 |

> trigger=interval: misdecodes 15

> trigger=interval: decode_failures 8

> trigger=aimd: misdecodes 2

> trigger=aimd: decode_failures 13

> trigger=bucket+interval: misdecodes 17

### `SF-capacity` - capacity  `--scenario alpine`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.938 | 0.940 | 0.201 | 1.28x | 18.0/25.6/27.8% | 1.9/5.1% | 3 |
| 8 | 1 | 0.800 | 0.792 | 0.009 | - | - | 0.933 | 0.935 | 0.186 | 1.31x | 18.4/26.1/28.3% | 1.9/5.2% | 3 |
| 16 | 1 | 0.807 | 0.799 | 0.008 | - | - | 0.942 | 0.943 | 0.202 | 1.28x | 18.0/25.5/27.6% | 1.8/5.1% | 3 |
| 32 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 50 | 1 | 0.805 | 0.799 | 0.007 | - | - | 0.936 | 0.938 | 0.183 | 1.31x | 18.2/26.1/28.3% | 1.9/5.2% | 3 |

> capacity=4: decode_failures 67

> capacity=8: decode_failures 26

> capacity=16: decode_failures 1

### `SF-capacity-local` - capacity  `--scenario alpine`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.938 | 0.940 | 0.201 | 1.28x | 18.0/25.6/27.8% | 1.9/5.1% | 3 |
| 8 | 1 | 0.800 | 0.792 | 0.009 | - | - | 0.933 | 0.935 | 0.186 | 1.31x | 18.4/26.1/28.3% | 1.9/5.2% | 3 |
| 16 | 1 | 0.807 | 0.799 | 0.008 | - | - | 0.942 | 0.943 | 0.202 | 1.28x | 18.0/25.5/27.6% | 1.8/5.1% | 3 |
| 32 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 50 | 1 | 0.805 | 0.799 | 0.007 | - | - | 0.936 | 0.938 | 0.183 | 1.31x | 18.2/26.1/28.3% | 1.9/5.2% | 3 |

> capacity=4: decode_failures 67

> capacity=8: decode_failures 26

> capacity=16: decode_failures 1

### `SF-capacity-window` - capacity  `--scenario alpine`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.805 | 0.801 | 0.004 | - | - | 0.901 | 0.945 | 0.186 | 1.26x | 17.8/25.2/27.4% | 1.8/5.1% | 3 |
| 16 | 1 | 0.795 | 0.787 | 0.009 | - | - | 0.921 | 0.934 | 0.171 | 1.29x | 18.1/25.7/27.9% | 1.9/5.2% | 3 |
| 32 | 1 | 0.803 | 0.794 | 0.009 | - | - | 0.934 | 0.938 | 0.191 | 1.29x | 18.2/25.7/27.9% | 1.9/5.2% | 3 |

> capacity=8: misdecodes 5

> capacity=8: decode_failures 63

> capacity=16: misdecodes 28

> capacity=16: decode_failures 15

> capacity=32: misdecodes 22

### `SF-catchup` - catch-up-hours  `--scenario alpine`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.778 | 0.766 | 0.011 | - | - | 0.914 | 0.915 | 0.193 | 1.78x | 23.0/35.6/38.9% | 2.6/7.5% | 3 |
| 02-06 | 1 | 0.806 | 0.802 | 0.005 | - | - | 0.913 | 0.953 | 0.188 | 1.35x | 18.9/27.1/29.6% | 1.9/5.6% | 3 |
| 00-08 | 1 | 0.815 | 0.810 | 0.005 | - | - | 0.920 | 0.955 | 0.196 | 1.42x | 19.4/28.8/31.4% | 2.1/6.0% | 3 |

> catch-up-hours=: misdecodes 17

> catch-up-hours=02-06: decode_failures 49

> catch-up-hours=00-08: decode_failures 50

### `SF-hops-flat` - hops-apart  `--scenario alpine`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.793 | 0.791 | 0.002 | - | - | 0.919 | 0.919 | 0.183 | 1.27x | 17.8/25.5/27.7% | 1.8/5.1% | 3 |
| 2 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 3 | 1 | 0.826 | 0.792 | 0.033 | - | - | 0.947 | 0.967 | 0.202 | 1.31x | 18.2/25.8/28.2% | 1.9/5.3% | 3 |
| 4 | 1 | 0.823 | 0.795 | 0.029 | - | - | 0.915 | 0.947 | 0.184 | 1.33x | 18.9/26.6/28.8% | 1.9/5.4% | 3 |

> hops-apart=3: decode_failures 15

> hops-apart=4: decode_failures 25

### `SF-hops-spread` - hops-apart  `--scenario alpine`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.793 | 0.791 | 0.002 | - | - | 0.919 | 0.919 | 0.183 | 1.27x | 17.8/25.5/27.7% | 1.8/5.1% | 3 |
| 2 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 3 | 1 | 0.826 | 0.792 | 0.033 | - | - | 0.947 | 0.967 | 0.202 | 1.31x | 18.2/25.8/28.2% | 1.9/5.3% | 3 |
| 4 | 1 | 0.823 | 0.795 | 0.029 | - | - | 0.915 | 0.947 | 0.184 | 1.33x | 18.9/26.6/28.8% | 1.9/5.4% | 3 |
| 5 | 1 | 0.811 | 0.797 | 0.014 | - | - | 0.776 | 0.951 | 0.191 | 1.29x | 18.2/25.6/27.7% | 1.9/5.1% | 3 |

> hops-apart=3: decode_failures 15

> hops-apart=4: decode_failures 25

> hops-apart=5: decode_failures 25

### `SF-jitter-global` - advert-jitter-s  `--scenario alpine`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.809 | 0.800 | 0.008 | - | - | 0.941 | 0.944 | 0.196 | 1.29x | 18.0/25.9/28.0% | 1.9/5.2% | 3 |
| 30 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 120 | 1 | 0.804 | 0.796 | 0.008 | - | - | 0.942 | 0.944 | 0.208 | 1.31x | 18.4/26.0/28.3% | 1.9/5.2% | 3 |
| 600 | 1 | 0.799 | 0.792 | 0.008 | - | - | 0.931 | 0.932 | 0.189 | 1.30x | 18.2/25.9/28.2% | 1.9/5.2% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario alpine`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.809 | 0.800 | 0.008 | - | - | 0.941 | 0.944 | 0.196 | 1.29x | 18.0/25.9/28.0% | 1.9/5.2% | 3 |
| 30 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 120 | 1 | 0.804 | 0.796 | 0.008 | - | - | 0.942 | 0.944 | 0.208 | 1.31x | 18.4/26.0/28.3% | 1.9/5.2% | 3 |
| 600 | 1 | 0.799 | 0.792 | 0.008 | - | - | 0.931 | 0.932 | 0.189 | 1.30x | 18.2/25.9/28.2% | 1.9/5.2% | 3 |

### `SF-place-flat` - place  `--scenario alpine`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.807 | 0.797 | 0.010 | - | - | 0.588 | 0.862 | 0.210 | 1.30x | 18.3/25.8/27.9% | 1.9/5.1% | 3 |
| routers | 1 | 0.791 | 0.788 | 0.003 | - | - | 0.926 | 0.926 | 0.170 | 1.30x | 18.1/25.9/28.2% | 1.9/5.3% | 3 |
| alternate-routers | 1 | 0.791 | 0.788 | 0.003 | - | - | 0.930 | 0.930 | 0.182 | 1.31x | 18.3/26.0/28.2% | 1.9/5.3% | 3 |
| beside-router | 1 | 0.791 | 0.789 | 0.002 | - | - | 0.930 | 0.930 | 0.213 | 1.30x | 18.2/25.8/28.0% | 1.9/5.2% | 3 |
| random-clients | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.843 | 0.945 | 0.256 | 1.31x | 18.3/26.1/28.3% | 2.0/5.2% | 3 |
| hops-apart | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |

> place=spread: decode_failures 18

> place=random-clients: decode_failures 36

### `SF-place-spread` - place  `--scenario alpine`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.807 | 0.797 | 0.010 | - | - | 0.588 | 0.862 | 0.210 | 1.30x | 18.3/25.8/27.9% | 1.9/5.1% | 3 |
| routers | 1 | 0.791 | 0.788 | 0.003 | - | - | 0.926 | 0.926 | 0.170 | 1.30x | 18.1/25.9/28.2% | 1.9/5.3% | 3 |
| alternate-routers | 1 | 0.791 | 0.788 | 0.003 | - | - | 0.930 | 0.930 | 0.182 | 1.31x | 18.3/26.0/28.2% | 1.9/5.3% | 3 |
| beside-router | 1 | 0.791 | 0.789 | 0.002 | - | - | 0.930 | 0.930 | 0.213 | 1.30x | 18.2/25.8/28.0% | 1.9/5.2% | 3 |
| random-clients | 1 | 0.806 | 0.795 | 0.011 | - | - | 0.843 | 0.945 | 0.256 | 1.31x | 18.3/26.1/28.3% | 2.0/5.2% | 3 |
| hops-apart | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |

> place=spread: decode_failures 18

> place=random-clients: decode_failures 36

### `SF-provide-transport` - provide-transport  `--scenario alpine`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| broadcast | 1 | 0.827 | 0.787 | 0.039 | - | - | 0.938 | 0.939 | 0.263 | 1.38x | 19.1/27.2/29.5% | 2.0/5.5% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario alpine`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| heard | 1 | 0.809 | 0.799 | 0.010 | - | - | 0.945 | 0.945 | 0.208 | 1.30x | 18.2/25.8/28.0% | 1.9/5.2% | 3 |

> replay-ordering=heard: misdecodes 18

### `SF-replay-order-broadcast` - replay-ordering  `--scenario alpine`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.827 | 0.787 | 0.039 | - | - | 0.938 | 0.939 | 0.263 | 1.38x | 19.1/27.2/29.5% | 2.0/5.5% | 3 |
| heard | 1 | 0.830 | 0.789 | 0.041 | - | - | 0.937 | 0.939 | 0.270 | 1.41x | 19.6/27.7/30.0% | 2.1/5.6% | 3 |

> replay-ordering=heard: misdecodes 8

### `SF-resolve` - resolve  `--scenario alpine`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| enum | 1 | 0.802 | 0.792 | 0.010 | - | - | 0.935 | 0.937 | 0.197 | 1.29x | 18.1/25.9/28.2% | 1.8/5.3% | 3 |
| hybrid | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |

### `SF-servers-allrouters` - servers  `--scenario alpine`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.791 | 0.788 | 0.003 | - | - | 0.926 | 0.926 | 0.170 | 1.30x | 18.1/25.9/28.2% | 1.9/5.3% | 3 |
| 6 | 1 | 0.803 | 0.792 | 0.010 | - | - | 0.942 | 0.945 | 0.210 | 1.33x | 18.8/26.8/29.1% | 1.9/5.4% | 6 |

### `SF-servers-flat` - servers  `--scenario alpine`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.800 | 0.797 | 0.003 | - | - | 0.914 | 0.916 | 0.187 | 1.28x | 18.0/25.6/27.7% | 1.9/5.2% | 2 |
| 3 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 5 | 1 | 0.808 | 0.795 | 0.013 | - | - | 0.954 | 0.955 | 0.202 | 1.33x | 18.5/26.7/29.0% | 2.0/5.4% | 5 |
| 8 | 1 | 0.813 | 0.790 | 0.023 | - | - | 0.973 | 0.973 | 0.174 | 1.39x | 18.9/27.7/30.0% | 2.0/5.5% | 8 |

> servers=5: misdecodes 1

### `SF-servers-spread` - servers  `--scenario alpine`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.800 | 0.797 | 0.003 | - | - | 0.914 | 0.916 | 0.187 | 1.28x | 18.0/25.6/27.7% | 1.9/5.2% | 2 |
| 3 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 5 | 1 | 0.808 | 0.795 | 0.013 | - | - | 0.954 | 0.955 | 0.202 | 1.33x | 18.5/26.7/29.0% | 2.0/5.4% | 5 |
| 8 | 1 | 0.813 | 0.790 | 0.023 | - | - | 0.973 | 0.973 | 0.174 | 1.39x | 18.9/27.7/30.0% | 2.0/5.5% | 8 |

> servers=5: misdecodes 1

### `SF-signed` - signed  `--scenario alpine`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| True | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario alpine`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.811 | 0.800 | 0.010 | - | - | 0.942 | 0.947 | 0.209 | 1.22x | 17.1/23.9/25.9% | 1.8/4.7% | 3 |
| 1 | 1 | 0.821 | 0.811 | 0.010 | - | - | 0.954 | 0.955 | 0.207 | 1.23x | 17.2/24.0/26.3% | 1.8/4.8% | 3 |
| 2 | 1 | 0.812 | 0.802 | 0.010 | - | - | 0.933 | 0.938 | 0.214 | 1.20x | 16.7/23.6/25.5% | 1.7/4.7% | 3 |
| 4 | 1 | 0.807 | 0.798 | 0.009 | - | - | 0.935 | 0.939 | 0.226 | 1.20x | 16.9/23.7/25.8% | 1.8/4.7% | 3 |

### `SF-width` - short-id-bits  `--scenario alpine`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.803 | 0.793 | 0.010 | - | - | 0.936 | 0.938 | 0.202 | 1.29x | 18.1/25.7/27.9% | 1.9/5.2% | 3 |
| 24 | 1 | 0.800 | 0.791 | 0.009 | - | - | 0.936 | 0.937 | 0.197 | 1.29x | 17.9/25.6/27.8% | 1.8/5.2% | 3 |
| 32 | 1 | 0.803 | 0.795 | 0.009 | - | - | 0.939 | 0.940 | 0.204 | 1.31x | 18.3/26.1/28.2% | 1.9/5.3% | 3 |
| 64 | 1 | 0.804 | 0.794 | 0.010 | - | - | 0.936 | 0.938 | 0.197 | 1.31x | 18.2/26.2/28.4% | 1.9/5.3% | 3 |

### `SF-window-size` - window-size  `--scenario alpine`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.800 | 0.791 | 0.008 | - | - | 0.941 | 0.943 | 0.199 | 1.38x | 18.9/27.5/29.8% | 2.1/5.5% | 3 |
| 16 | 1 | 0.804 | 0.796 | 0.008 | - | - | 0.943 | 0.944 | 0.195 | 1.34x | 18.6/26.6/28.9% | 1.9/5.3% | 3 |
| 32 | 1 | 0.803 | 0.794 | 0.009 | - | - | 0.934 | 0.938 | 0.191 | 1.29x | 18.2/25.7/27.9% | 1.9/5.2% | 3 |

> window-size=8: misdecodes 119

> window-size=16: misdecodes 50

> window-size=32: misdecodes 22

### `TH-congestion` - no-congestion-scaling  `--scenario alpine`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.941 | 0.939 | 0.003 | - | - | 0.990 | 0.990 | 0.608 | 2.13x | 19.8/39.2/43.3% | 1.5/5.3% | 3 |
| True | 1 | 0.704 | 0.693 | 0.011 | - | - | 0.854 | 0.862 | 0.378 | 5.68x | 52.2/75.4/79.4% | 4.2/12.7% | 3 |

> no-congestion-scaling=False: misdecodes 1

> no-congestion-scaling=True: queue drops 13.6% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 80

### `TH-congestion-input` - congestion-input  `--scenario alpine`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.495 | 0.485 | 0.009 | - | - | 0.747 | 0.749 | 0.064 | 4.60x | 15.1/32.5/39.8% | 1.5/5.5% | 3 |
| truesize | 1 | 0.531 | 0.522 | 0.010 | - | - | 0.790 | 0.791 | 0.067 | 3.34x | 10.5/25.9/32.0% | 1.0/4.5% | 3 |

> congestion-input=hotstore: decode_failures 2

> congestion-input=truesize: decode_failures 2

### `TH-congestion-mode` - congestion-mode  `--scenario alpine`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.951 | 0.950 | 0.002 | - | - | 0.994 | 0.994 | 0.634 | 1.99x | 18.7/36.9/40.8% | 1.4/4.9% | 3 |
| adaptive | 1 | 0.941 | 0.939 | 0.003 | - | - | 0.990 | 0.990 | 0.608 | 2.13x | 19.8/39.2/43.3% | 1.5/5.3% | 3 |

> congestion-mode=adaptive: misdecodes 1

