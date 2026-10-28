# Sweep blocks-2026-10-28-1347235

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** alpine
- **seed base** 1347235 · seeds 1347235
- **blocks** 87 run
- **compute** 10.3 h of simulator time across every cell
- **generated** 2026-10-28T10:03:24+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>87 warnings</summary>

- AD-siting: siting-mix=basement-heavy: decode_failures 3
- DB-hotstore-stress: max-num-nodes=10: decode_failures 37
- DB-hotstore-stress: max-num-nodes=120: decode_failures 2
- DB-hotstore-stress: max-num-nodes=250: decode_failures 2
- DB-warm: warm-num-nodes=0: decode_failures 108
- DB-warm: warm-num-nodes=25: decode_failures 108
- DB-warm: warm-num-nodes=100: decode_failures 108
- DB-warm: warm-num-nodes=2000: decode_failures 108
- DG-burst: burst-loss=0.1: decode_failures 1
- DG-burst: burst-loss=0.2: decode_failures 38
- DG-burst: burst-loss=0.3: decode_failures 14
- DG-loss: extra-loss=0.3: decode_failures 19
- DG-outage: burst-loss=0.1: decode_failures 42
- DG-outage: burst-loss=0.2: decode_failures 25
- DG-outage: burst-loss=0.3: decode_failures 30
- DM-mode: dm-mode=flood-only: decode_failures 7
- FW-mixed-26: legacy-fraction=0.25: decode_failures 12
- FW-mixed: legacy-fraction=0.25: decode_failures 1
- FW-versions: profile=2.6: decode_failures 3
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 16
- LD-chatty: broadcast-interval-s=300: decode_failures 18
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 108
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 103
- MS-density: nodes=40: decode_failures 7
- MS-hopscale: nodes=500: decode_failures 125
- MS-oversubscribed: nodes=250: decode_failures 2
- MS-oversubscribed: nodes=500: decode_failures 68
- MS-siting: faster: 0.775 s per simulated hour against 1.81 over 67 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- MS-size: nodes=40: decode_failures 20
- MS-stretch: stretch=1.25: decode_failures 17
- MS-stretch: stretch=2.0: decode_failures 8
- MS-topology: topology=corridor: decode_failures 24
- PR-crladder: coding-rate-ladder=True: decode_failures 37
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 37
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 29
- PR-dmmode-cr: slower: 12.2 s per simulated hour against 2.57 over 68 prior run(s) - 4.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-bw500: preset=SHORT_TURBO: decode_failures 6
- RF-noise: noise-profile=temporal: decode_failures 3
- RF-preset: preset=LONG_MODERATE: decode_failures 2
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 6
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 3
- RF-txpower: tx-power=22: decode_failures 10
- RF-txpower: tx-power=14: decode_failures 2
- RT-hoplimit: hop-limit=3: decode_failures 11
- RT-hopspread: hop-limit=3: decode_failures 11
- RT-spread: hop-spread=False: decode_failures 11
- SF-bucket-mode: bucket-mode=global: misdecodes 41
- SF-bucket-mode: bucket-mode=time: misdecodes 22
- SF-bucket-mode: bucket-mode=window: misdecodes 16
- SF-bucket-time: time-bucket-s=600: misdecodes 109
- SF-bucket-time: time-bucket-s=1800: misdecodes 22
- SF-bucket-time: time-bucket-s=3600: misdecodes 6
- SF-bucket-time: time-bucket-s=3600: decode_failures 3
- SF-cadence: trigger=interval: misdecodes 7
- SF-cadence: trigger=interval: decode_failures 3
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=aimd: decode_failures 4
- SF-cadence: trigger=bucket+interval: misdecodes 16
- SF-capacity-local: capacity=4: decode_failures 85
- SF-capacity-local: capacity=8: decode_failures 49
- SF-capacity: capacity=4: decode_failures 85
- SF-capacity: capacity=8: decode_failures 49
- SF-capacity-window: capacity=8: misdecodes 7
- SF-capacity-window: capacity=8: decode_failures 92
- SF-capacity-window: capacity=16: misdecodes 20
- SF-capacity-window: capacity=16: decode_failures 10
- SF-capacity-window: capacity=32: misdecodes 16
- SF-catchup: catch-up-hours=: misdecodes 16
- SF-catchup: catch-up-hours=02-06: misdecodes 1
- SF-catchup: catch-up-hours=02-06: decode_failures 43
- SF-catchup: catch-up-hours=00-08: decode_failures 43
- SF-hops-flat: hops-apart=4: decode_failures 32
- SF-hops-spread: hops-apart=4: decode_failures 32
- SF-hops-spread: hops-apart=5: decode_failures 3
- SF-place-flat: place=spread: decode_failures 5
- SF-place-flat: place=random-clients: decode_failures 25
- SF-place-spread: place=spread: decode_failures 5
- SF-place-spread: place=random-clients: decode_failures 25
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 7
- SF-replay-order: replay-ordering=heard: misdecodes 11
- SF-servers-flat: servers=8: misdecodes 1
- SF-servers-spread: servers=8: misdecodes 1
- SF-window-size: window-size=8: misdecodes 116
- SF-window-size: window-size=16: misdecodes 42
- SF-window-size: window-size=32: misdecodes 16
- TH-congestion-input: congestion-input=hotstore: decode_failures 2
- TH-congestion: no-congestion-scaling=True: decode_failures 112

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `PR-dmmode-cr` | 12.2 | 2.57 | 4.75x | 68 |
| `RT-spread` | 4.06 | 2.15 | 1.88x | 68 |
| `RT-hopspread` | 3.69 | 2.03 | 1.82x | 68 |
| `MS-topology` | 3.28 | 1.9 | 1.73x | 68 |
| `PR-crladder` | 4.74 | 2.77 | 1.71x | 68 |
| `RT-hoplimit` | 2.91 | 1.75 | 1.67x | 68 |
| `SF-cadence` | 5.41 | 3.61 | 1.50x | 68 |
| `FW-signing-cost` | 1 | 1.55 | 0.65x | 68 |
| `PR-repeats` | 1.02 | 1.6 | 0.64x | 68 |
| `RF-noise` | 3.05 | 4.93 | 0.62x | 68 |
| `RF-preset-turbo` | 0.943 | 1.53 | 0.62x | 64 |
| `SF-jitter-local` | 1.1 | 1.78 | 0.62x | 68 |
| `AD-flooding` | 1.49 | 2.46 | 0.60x | 68 |
| `MS-density` | 1.94 | 3.22 | 0.60x | 68 |
| `RF-duct` | 1.04 | 1.74 | 0.60x | 68 |
| `SC-signing` | 1.05 | 1.76 | 0.60x | 68 |
| `RF-bw500` | 1.16 | 1.95 | 0.59x | 68 |
| `RT-favourites` | 0.932 | 1.64 | 0.57x | 68 |
| `AD-amplifiers` | 0.891 | 1.59 | 0.56x | 68 |
| `RF-stretch-duct` | 1.02 | 1.82 | 0.56x | 68 |
| `LD-interval` | 0.723 | 1.31 | 0.55x | 68 |
| `RF-pulse` | 0.871 | 1.61 | 0.54x | 68 |
| `PR-repeats-busy` | 1.96 | 3.63 | 0.54x | 68 |
| `MS-siting` | 0.775 | 1.81 | 0.43x | 67 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.919 | 0.919 | 0.722 → 0.727 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.908 | 0.908 | 0.717 → 0.727 | 1.2x bytes_on_air | up | 3 |
| `AD-siting` | siting-mix | **held** | 0.058 → 0.949 | 0.890 | 0.013 → 0.714 | 22x advert_bytes | down | 3 |
| `MS-siting` | siting-mix | **text** | 0.154 → 0.950 | 0.796 | 0.149 → 0.949 | 3.5x sr_airtime | up | 4 |
| `RF-preset-turbo` | preset | **held** | 0.125 → 0.908 | 0.782 | 0.037 → 0.725 | 8.5x advert_bytes | up | 5 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.086 → 0.856 | 0.770 | 0.076 → 0.676 | 1.6e+02x sr_airtime | down | 4 |
| `RF-txpower` | tx-power | **held** | 0.197 → 0.908 | 0.710 | 0.060 → 0.725 | 4.9x advert_bytes | down | 4 |
| `MS-stretch` | stretch | **held** | 0.223 → 0.908 | 0.685 | 0.100 → 0.725 | 6.9x sr_airtime | down | 4 |
| `RF-bw500` | preset | **held** | 0.312 → 0.847 | 0.534 | 0.140 → 0.629 | 2.8x advert_bytes | up | 3 |
| `SF-place-flat` | place | **held** | 0.404 → 0.917 | 0.514 | 0.718 → 0.725 | 11x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.404 → 0.917 | 0.514 | 0.718 → 0.725 | 11x sr_bytes | up | 6 |
| `MS-topology` | topology | **held** | 0.513 → 0.998 | 0.484 | 0.530 → 0.958 | 2.3x sr_airtime | up | 4 |
| `RF-eu-presets` | preset | **text** | 0.269 → 0.737 | 0.468 | 0.266 → 0.725 | 2.4x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.269 → 0.737 | 0.468 | 0.266 → 0.725 | 2.4x sr_airtime | up | 3 |
| `MS-hopscale` | nodes | **held** | 0.462 → 0.908 | 0.445 | 0.304 → 0.725 | 8.7x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **text** | 0.317 → 0.688 | 0.371 | 0.310 → 0.679 | 4.9x bytes_on_air | down | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.232 → 0.592 | 0.361 | 0.229 → 0.589 | 3x sr_airtime | up | 2 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.521 → 0.867 | 0.346 | 0.507 → 0.864 | 9.9x sr_airtime | down | 3 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.445 → 0.772 | 0.327 | 0.430 → 0.763 | 10x sr_airtime | down | 3 |
| `MS-density` | nodes | **text** | 0.631 → 0.953 | 0.321 | 0.587 → 0.949 | 4.8x advert_bytes | up | 5 |
| `RT-hoplimit` | hop-limit | **text** | 0.584 → 0.900 | 0.316 | 0.538 → 0.898 | 2.5x sr_bytes | up | 4 |
| `DG-outage` | burst-loss | **text** | 0.446 → 0.737 | 0.291 | 0.420 → 0.725 | 2x sr_bytes | down | 4 |
| `DG-burst` | burst-loss | **text** | 0.463 → 0.737 | 0.274 | 0.431 → 0.725 | 1.9x sr_bytes | down | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.343 → 0.605 | 0.262 | 0.311 → 0.515 | 6.1x sr_airtime | up | 3 |
| `RT-hopspread` | hop-limit | **text** | 0.584 → 0.840 | 0.256 | 0.538 → 0.834 | 2x sr_bytes | up | 3 |
| `MS-size` | nodes | **held** | 0.675 → 0.930 | 0.255 | 0.635 → 0.770 | 4.3x advert_bytes | up | 5 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.734 → 0.929 | 0.196 | 0.724 → 0.924 | 4.1x sr_airtime | down | 2 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.737 → 0.925 | 0.188 | 0.725 → 0.922 | 1.9x sr_bytes | up | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.737 → 0.904 | 0.168 | 0.725 → 0.899 | 1.5x sr_bytes | up | 3 |
| `RF-noise` | noise-profile | **held** | 0.747 → 0.908 | 0.160 | 0.567 → 0.725 | 1.6x sr_bytes | down | 4 |
| `AD-badrouters` | role-placement | **held** | 0.793 → 0.949 | 0.155 | 0.599 → 0.714 | 1.4x sr_bytes | down | 3 |
| `RT-spread` | hop-spread | **text** | 0.584 → 0.737 | 0.153 | 0.538 → 0.725 | 1.9x sr_bytes | up | 2 |
| `DG-loss` | extra-loss | **text** | 0.602 → 0.737 | 0.135 | 0.581 → 0.725 | 1.5x sr_bytes | down | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.737 → 0.856 | 0.119 | 0.725 → 0.847 | 1.3x sr_bytes | up | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.693 → 0.800 | 0.107 | 0.676 → 0.794 | 5.4x sr_airtime | up | 4 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.737 → 0.843 | 0.106 | 0.725 → 0.831 | 2.3x bytes_on_air | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.804 → 0.908 | 0.104 | 0.725 → 0.726 | 31x sr_airtime | down | 3 |
| `FW-mixed` | legacy-fraction | **text** | 0.737 → 0.840 | 0.103 | 0.725 → 0.829 | 2.2x bytes_on_air | up | 4 |
| `DB-hotstore` | max-num-nodes | **text** | 0.718 → 0.812 | 0.094 | 0.707 → 0.806 | 2.1x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.718 → 0.812 | 0.094 | 0.707 → 0.806 | 2.1x sr_airtime | down | 3 |
| `SC-signing` | signature-policy | **text** | 0.652 → 0.737 | 0.085 | 0.652 → 0.725 | 1.1x sr_airtime | down | 3 |
| `FW-versions` | profile | **text** | 0.737 → 0.822 | 0.085 | 0.725 → 0.807 | 3.3x bytes_on_air | down | 5 |
| `FW-firmware` | profile | **text** | 0.737 → 0.814 | 0.078 | 0.725 → 0.801 | 3.2x bytes_on_air | down | 2 |
| `SF-cadence` | trigger | **held** | 0.832 → 0.908 | 0.076 | 0.698 → 0.725 | 14x advert_bytes | down | 4 |
| `SF-capacity-window` | capacity | **held** | 0.840 → 0.910 | 0.070 | 0.718 → 0.730 | 1.9x sr_bytes | up | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.729 → 0.798 | 0.069 | 0.719 → 0.790 | 1.2x sr_bytes | up | 2 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.674 → 0.728 | 0.053 | 0.664 → 0.718 | 1.2x sr_airtime | down | 2 |
| `RT-hopassign` | hop-assign | **text** | 0.687 → 0.737 | 0.050 | 0.672 → 0.725 | 1.1x sr_bytes | down | 2 |
| `MS-roles` | role-mix | **text** | 0.729 → 0.775 | 0.046 | 0.714 → 0.765 | 1.2x bytes_on_air | down | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.605 → 0.646 | 0.041 | 0.514 → 0.545 | 1.5x sr_airtime | up | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.737 → 0.778 | 0.041 | 0.725 → 0.771 | 3.3x bytes_on_air | down | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.699 → 0.737 | 0.038 | 0.682 → 0.725 | 1.3x sr_airtime | down | 4 |
| `SF-catchup` | catch-up-hours | **held** | 0.858 → 0.896 | 0.037 | 0.698 → 0.724 | 9.1x advert_bytes | down | 3 |
| `SF-hops-flat` | hops-apart | **text** | 0.725 → 0.762 | 0.037 | 0.719 → 0.725 | 5.3x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **text** | 0.725 → 0.762 | 0.037 | 0.715 → 0.725 | 5.3x sr_bytes | up | 5 |
| `MS-roles-fav` | role-mix | **text** | 0.785 → 0.822 | 0.037 | 0.775 → 0.813 | 1.1x bytes_on_air | down | 2 |
| `AD-flooding` | role-mix | **text** | 0.729 → 0.763 | 0.035 | 0.714 → 0.754 | 2.3x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.729 → 0.763 | 0.035 | 0.714 → 0.754 | 2.3x bytes_on_air | up | 3 |
| `SF-provide-transport` | provide-transport | **text** | 0.737 → 0.768 | 0.031 | 0.707 → 0.725 | 3.3x sr_airtime | up | 2 |
| `LD-diurnal` | diurnal | **held** | 0.908 → 0.935 | 0.027 | 0.725 → 0.749 | 1.2x advert_bytes | down | 3 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.854 → 0.880 | 0.026 | 0.690 → 0.695 | 1x advert_bytes | down | 2 |
| `AD-worst` | role-placement | **text** | 0.826 → 0.851 | 0.025 | 0.813 → 0.844 | 1.2x sr_bytes | down | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.906 → 0.929 | 0.023 | 0.712 → 0.720 | 2.8x sr_bytes | up | 2 |
| `SF-sr-retries` | sr-retries | **held** | 0.904 → 0.922 | 0.019 | 0.720 → 0.727 | 1.1x sr_bytes | up | 4 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.723 → 0.739 | 0.017 | 0.711 → 0.729 | 5.3x advert_bytes | up | 3 |
| `SF-window-size` | window-size | **held** | 0.903 → 0.919 | 0.016 | 0.717 → 0.724 | 6.1x advert_bytes | down | 3 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.727 → 0.742 | 0.015 | 0.716 → 0.730 | 3.4x advert_bytes | down | 4 |
| `MS-router-late` | router-late-fraction | **held** | 0.893 → 0.908 | 0.015 | 0.722 → 0.727 | 1.3x bytes_on_air | down | 4 |
| `SF-capacity` | capacity | **held** | 0.907 → 0.920 | 0.013 | 0.718 → 0.727 | 5.4x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.907 → 0.920 | 0.013 | 0.718 → 0.727 | 5.4x advert_bytes | up | 5 |
| `SF-servers-flat` | servers | **held** | 0.908 → 0.920 | 0.012 | 0.717 → 0.725 | 6.1x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.908 → 0.920 | 0.012 | 0.717 → 0.725 | 6.1x sr_bytes | up | 4 |
| `SF-replay-order` | replay-ordering | **held** | 0.908 → 0.919 | 0.012 | 0.725 → 0.726 | 1.2x sr_bytes | up | 2 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.908 → 0.918 | 0.011 | 0.719 → 0.725 | 1.1x sr_bytes | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.908 → 0.918 | 0.011 | 0.719 → 0.725 | 1.1x sr_bytes | down | 4 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.690 → 0.701 | 0.010 | 0.690 → 0.701 | 1.1x sr_bytes | up | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.899 → 0.908 | 0.008 | 0.720 → 0.725 | 2.8x sr_airtime | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.922 → 0.929 | 0.008 | 0.915 → 0.924 | 1.2x sr_airtime | down | 2 |
| `SF-width` | short-id-bits | **text** | 0.730 → 0.737 | 0.007 | 0.718 → 0.725 | 3.1x advert_bytes | up | 4 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.768 → 0.775 | 0.007 | 0.707 → 0.708 | 1.1x sr_airtime | up | 2 |
| `DM-mode` | dm-mode | **held** | 0.880 → 0.886 | 0.006 | 0.695 → 0.700 | 1.1x sr_airtime | up | 3 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.929 → 0.934 | 0.004 | 0.924 → 0.929 | 1.1x sr_airtime | down | 2 |
| `SF-resolve` | resolve | **text** | 0.733 → 0.737 | 0.003 | 0.721 → 0.725 | 5.7x advert_bytes | = | 3 |
| `PR-repeats` | extra-repeats | **held** | 0.908 → 0.910 | 0.003 | 0.725 → 0.727 | 1x sr_airtime | up | 2 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.996 → 0.997 | 0.002 | 0.924 → 0.926 | 1x sr_bytes | up | 2 |

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
| none | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| sprinkled | 1 | 0.845 | 0.838 | 0.006 | - | - | 0.966 | 0.968 | 0.000 | 1.23x | 15.2/21.9/26.2% | 1.9/5.2% | 3 |
| arms-race | 1 | 0.925 | 0.922 | 0.003 | - | - | 0.980 | 0.980 | 0.000 | 1.15x | 20.7/26.8/29.3% | 1.4/5.5% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario alpine`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 0.1 | 1 | 0.768 | 0.759 | 0.010 | - | - | 0.874 | 0.876 | 0.000 | 1.21x | 15.8/20.5/23.9% | 1.7/5.3% | 3 |
| 0.3 | 1 | 0.904 | 0.899 | 0.005 | - | - | 0.984 | 0.985 | 0.753 | 1.16x | 17.1/23.3/28.3% | 1.6/4.9% | 3 |

### `AD-badrouters` - role-placement  `--scenario alpine`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.729 | 0.714 | 0.015 | - | - | 0.949 | 0.950 | 0.000 | 1.11x | 14.4/19.0/23.3% | 1.7/5.8% | 3 |
| inverse | 1 | 0.666 | 0.643 | 0.023 | - | - | 0.905 | 0.909 | 0.000 | 1.17x | 13.2/16.9/20.1% | 1.9/3.8% | 3 |
| random | 1 | 0.618 | 0.599 | 0.019 | - | - | 0.793 | 0.799 | 0.000 | 1.18x | 12.5/19.4/25.7% | 1.9/5.2% | 3 |

### `AD-flooding` - role-mix  `--scenario alpine`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.729 | 0.714 | 0.015 | - | - | 0.949 | 0.950 | 0.000 | 1.11x | 14.4/19.0/23.3% | 1.7/5.8% | 3 |
| all-routers | 1 | 0.763 | 0.754 | 0.010 | - | - | 0.921 | 0.924 | 0.000 | 2.53x | 26.8/35.7/41.0% | 4.2/5.5% | 3 |

### `AD-nomute` - role-mix  `--scenario alpine`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.729 | 0.714 | 0.015 | - | - | 0.949 | 0.950 | 0.000 | 1.11x | 14.4/19.0/23.3% | 1.7/5.8% | 3 |
| no-mute | 1 | 0.758 | 0.747 | 0.012 | - | - | 0.941 | 0.945 | 0.000 | 1.31x | 15.7/20.3/23.5% | 2.0/6.0% | 3 |
| all-routers | 1 | 0.763 | 0.754 | 0.010 | - | - | 0.921 | 0.924 | 0.000 | 2.53x | 26.8/35.7/41.0% | 4.2/5.5% | 3 |

### `AD-siting` - siting-mix  `--scenario alpine`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.729 | 0.714 | 0.015 | - | - | 0.949 | 0.950 | 0.000 | 1.11x | 14.4/19.0/23.3% | 1.7/5.8% | 3 |
| local-typical | 1 | 0.610 | 0.603 | 0.007 | - | - | 0.823 | 0.824 | 0.000 | 1.21x | 12.6/19.5/24.4% | 2.0/5.3% | 3 |
| basement-heavy | 1 | 0.013 | 0.013 | 0.000 | - | - | 0.058 | 0.078 | 0.000 | 0.25x | 0.2/2.5/4.3% | 0.2/1.4% | 3 |

> siting-mix=basement-heavy: decode_failures 3

### `AD-worst` - role-placement  `--scenario alpine`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.851 | 0.844 | 0.007 | - | - | 0.958 | 0.958 | 0.000 | 2.29x | 17.1/26.1/34.1% | 1.7/5.5% | 3 |
| inverse | 1 | 0.826 | 0.813 | 0.013 | - | - | 0.963 | 0.965 | 0.000 | 2.18x | 15.2/23.1/31.1% | 1.7/3.2% | 3 |

### `BL-control` - protocol  `--scenario alpine`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.727 | 0.727 | 0.000 | - | - | 0 | 0.000 | 0.000 | 1.26x | 14.7/20.7/24.1% | 1.8/5.5% | 3 |
| sr | 1 | 0.748 | 0.722 | 0.025 | - | - | 0.919 | 0.921 | 0.000 | 1.30x | 15.1/21.7/24.9% | 1.9/5.8% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario alpine`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.718 | 0.707 | 0.011 | - | - | 0.848 | 0.848 | 0.000 | 2.76x | 33.7/44.5/51.4% | 4.0/9.6% | 3 |
| 100 | 1 | 0.812 | 0.806 | 0.006 | - | - | 0.909 | 0.912 | 0.000 | 1.48x | 18.6/24.3/28.0% | 2.0/5.3% | 3 |
| 120 | 1 | 0.812 | 0.806 | 0.006 | - | - | 0.909 | 0.912 | 0.000 | 1.48x | 18.6/24.3/28.0% | 2.0/5.3% | 3 |
| 250 | 1 | 0.812 | 0.806 | 0.006 | - | - | 0.909 | 0.912 | 0.000 | 1.48x | 18.6/24.3/28.0% | 2.0/5.3% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario alpine`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.314 | 0.311 | 0.004 | - | - | 0.343 | 0.351 | 0.119 | 11.50x | 41.1/56.4/72.3% | 4.0/11.0% | 3 |
| 120 | 1 | 0.525 | 0.514 | 0.011 | - | - | 0.605 | 0.606 | 0.188 | 4.26x | 15.8/23.8/33.8% | 1.5/4.8% | 3 |
| 250 | 1 | 0.525 | 0.515 | 0.011 | - | - | 0.605 | 0.607 | 0.181 | 4.19x | 15.5/23.0/33.2% | 1.5/4.6% | 3 |

> max-num-nodes=10: decode_failures 37

> max-num-nodes=120: decode_failures 2

> max-num-nodes=250: decode_failures 2

### `DB-platform` - platform-mix  `--scenario alpine`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.812 | 0.806 | 0.006 | - | - | 0.909 | 0.912 | 0.000 | 1.48x | 18.6/24.3/28.0% | 2.0/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.812 | 0.806 | 0.006 | - | - | 0.909 | 0.912 | 0.000 | 1.48x | 18.6/24.3/28.0% | 2.0/5.3% | 3 |
| constrained | 1 | 0.718 | 0.707 | 0.011 | - | - | 0.848 | 0.848 | 0.000 | 2.76x | 33.7/44.5/51.4% | 4.0/9.6% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario alpine`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.728 | 0.718 | 0.010 | - | - | 0.873 | 0.944 | 0.509 | 5.63x | 50.6/66.0/75.0% | 4.0/12.3% | 3 |
| 25 | 1 | 0.728 | 0.718 | 0.010 | - | - | 0.873 | 0.944 | 0.509 | 5.63x | 50.6/66.0/75.0% | 4.0/12.3% | 3 |
| 100 | 1 | 0.728 | 0.718 | 0.010 | - | - | 0.873 | 0.944 | 0.509 | 5.63x | 50.6/66.0/75.0% | 4.0/12.3% | 3 |
| 2000 | 1 | 0.728 | 0.718 | 0.010 | - | - | 0.873 | 0.944 | 0.509 | 5.63x | 50.6/66.0/75.0% | 4.0/12.3% | 3 |

> warm-num-nodes=0: decode_failures 108

> warm-num-nodes=25: decode_failures 108

> warm-num-nodes=100: decode_failures 108

> warm-num-nodes=2000: decode_failures 108

### `DG-burst` - burst-loss  `--scenario alpine`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 0.1 | 1 | 0.655 | 0.633 | 0.022 | - | - | 0.893 | 0.893 | 0.000 | 1.22x | 14.5/20.3/23.5% | 1.8/5.4% | 3 |
| 0.2 | 1 | 0.563 | 0.532 | 0.030 | - | - | 0.804 | 0.827 | 0.000 | 1.16x | 14.1/19.5/22.5% | 1.7/4.8% | 3 |
| 0.3 | 1 | 0.463 | 0.431 | 0.032 | - | - | 0.718 | 0.769 | 0.000 | 1.05x | 13.3/18.0/20.9% | 1.6/4.2% | 3 |

> burst-loss=0.1: decode_failures 1

> burst-loss=0.2: decode_failures 38

> burst-loss=0.3: decode_failures 14

### `DG-loss` - extra-loss  `--scenario alpine`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 0.1 | 1 | 0.705 | 0.690 | 0.015 | - | - | 0.900 | 0.908 | 0.000 | 1.36x | 16.2/22.3/25.6% | 2.0/5.7% | 3 |
| 0.2 | 1 | 0.652 | 0.633 | 0.019 | - | - | 0.864 | 0.867 | 0.000 | 1.39x | 16.7/23.0/26.6% | 2.2/5.4% | 3 |
| 0.3 | 1 | 0.602 | 0.581 | 0.021 | - | - | 0.812 | 0.840 | 0.000 | 1.44x | 17.6/23.8/27.8% | 2.2/5.2% | 3 |

> extra-loss=0.3: decode_failures 19

### `DG-outage` - burst-loss  `--scenario alpine`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 0.1 | 1 | 0.646 | 0.627 | 0.019 | - | - | 0.847 | 0.876 | 0.000 | 1.23x | 14.6/20.6/23.7% | 1.8/5.3% | 3 |
| 0.2 | 1 | 0.532 | 0.510 | 0.021 | - | - | 0.769 | 0.824 | 0.000 | 1.16x | 14.3/19.0/22.4% | 1.7/4.9% | 3 |
| 0.3 | 1 | 0.446 | 0.420 | 0.026 | - | - | 0.640 | 0.742 | 0.000 | 1.08x | 13.4/18.2/21.6% | 1.6/4.0% | 3 |

> burst-loss=0.1: decode_failures 42

> burst-loss=0.2: decode_failures 25

> burst-loss=0.3: decode_failures 30

### `DM-mode` - dm-mode  `--scenario alpine`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.695 | 0.695 | 0.000 | - | - | 0.884 | 0.894 | 0.000 | 1.68x | 19.6/27.5/31.8% | 2.3/7.1% | 3 |
| directed-with-late-flood | 1 | 0.695 | 0.695 | 0.000 | - | - | 0.880 | 0.887 | 0.000 | 1.55x | 18.3/25.4/29.4% | 2.2/6.9% | 3 |
| m4-early-flood | 1 | 0.700 | 0.700 | 0.000 | - | - | 0.886 | 0.897 | 0.000 | 1.55x | 18.2/25.5/29.6% | 2.2/6.9% | 3 |

> dm-mode=flood-only: decode_failures 7

### `FW-firmware` - profile  `--scenario alpine`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.814 | 0.801 | 0.014 | - | - | 0.977 | 0.979 | 0.478 | 0.71x | 8.0/10.3/11.9% | 1.2/2.0% | 3 |
| 2.8 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario alpine`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 0.25 | 1 | 0.821 | 0.803 | 0.018 | - | - | 0.975 | 0.979 | 0.550 | 1.07x | 12.4/18.6/21.4% | 1.7/4.5% | 3 |
| 0.5 | 1 | 0.840 | 0.823 | 0.018 | - | - | 0.972 | 0.972 | 0.240 | 0.99x | 12.4/17.3/18.9% | 1.5/4.2% | 3 |
| 0.75 | 1 | 0.834 | 0.829 | 0.005 | - | - | 0.927 | 0.928 | 0.433 | 0.85x | 10.2/13.4/16.1% | 1.3/3.5% | 3 |

> legacy-fraction=0.25: decode_failures 1

### `FW-mixed-26` - legacy-fraction  `--scenario alpine`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 0.25 | 1 | 0.818 | 0.801 | 0.016 | - | - | 0.977 | 0.985 | 0.521 | 1.09x | 12.6/19.0/22.1% | 1.7/4.6% | 3 |
| 0.5 | 1 | 0.843 | 0.825 | 0.018 | - | - | 0.972 | 0.972 | 0.236 | 0.98x | 12.2/17.4/19.2% | 1.6/4.2% | 3 |
| 0.75 | 1 | 0.836 | 0.831 | 0.005 | - | - | 0.933 | 0.935 | 0.428 | 0.82x | 10.2/13.6/16.4% | 1.3/3.5% | 3 |

> legacy-fraction=0.25: decode_failures 12

### `FW-signing-cost` - profile-flag  `--scenario alpine`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.778 | 0.771 | 0.007 | - | - | 0.931 | 0.934 | 0.000 | 0.70x | 8.5/12.3/14.4% | 0.9/3.4% | 3 |
| signing=true | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |

### `FW-versions` - profile  `--scenario alpine`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.819 | 0.804 | 0.015 | - | - | 0.974 | 0.975 | 0.458 | 0.73x | 8.5/11.2/13.2% | 1.1/2.6% | 3 |
| 2.5 | 1 | 0.813 | 0.797 | 0.017 | - | - | 0.969 | 0.974 | 0.429 | 0.75x | 8.5/11.2/13.1% | 1.2/2.7% | 3 |
| 2.6 | 1 | 0.815 | 0.801 | 0.013 | - | - | 0.973 | 0.982 | 0.453 | 0.70x | 8.3/10.9/13.0% | 1.1/2.6% | 3 |
| 2.7 | 1 | 0.822 | 0.807 | 0.014 | - | - | 0.979 | 0.980 | 0.480 | 0.71x | 8.6/11.3/13.6% | 1.1/3.1% | 3 |
| 2.8 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |

> profile=2.6: decode_failures 3

### `LD-chatty` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.772 | 0.763 | 0.009 | - | - | 0.940 | 0.943 | 0.000 | 0.87x | 10.2/14.5/17.0% | 1.2/4.0% | 3 |
| 900 | 1 | 0.693 | 0.676 | 0.017 | - | - | 0.888 | 0.891 | 0.000 | 2.07x | 24.0/33.7/38.7% | 3.0/9.0% | 3 |
| 300 | 1 | 0.445 | 0.430 | 0.015 | - | - | 0.665 | 0.718 | 0.000 | 4.93x | 52.0/67.9/72.8% | 7.5/16.3% | 3 |

> broadcast-interval-s=300: decode_failures 18

### `LD-chatty-hops` - broadcast-interval-s  `--scenario alpine`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.867 | 0.864 | 0.004 | - | - | 0.970 | 0.972 | 0.000 | 0.91x | 10.6/14.4/17.0% | 1.3/3.7% | 3 |
| 900 | 1 | 0.793 | 0.783 | 0.009 | - | - | 0.929 | 0.931 | 0.000 | 2.20x | 25.4/34.7/40.0% | 3.2/8.9% | 3 |
| 300 | 1 | 0.521 | 0.507 | 0.013 | - | - | 0.701 | 0.742 | 0.000 | 5.07x | 53.6/68.4/73.8% | 7.8/17.1% | 3 |

> broadcast-interval-s=300: decode_failures 16

### `LD-diurnal` - diurnal  `--scenario alpine`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.760 | 0.749 | 0.012 | - | - | 0.934 | 0.936 | 0.000 | 1.21x | 14.4/20.2/23.5% | 1.7/5.5% | 3 |
| sinusoid | 1 | 0.759 | 0.748 | 0.012 | - | - | 0.935 | 0.936 | 0.000 | 1.16x | 13.8/19.3/22.5% | 1.6/5.2% | 3 |
| commuter | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.693 | 0.676 | 0.017 | - | - | 0.888 | 0.891 | 0.000 | 2.07x | 24.0/33.7/38.7% | 3.0/9.0% | 3 |
| 3600 | 1 | 0.772 | 0.763 | 0.009 | - | - | 0.940 | 0.943 | 0.000 | 0.87x | 10.2/14.5/17.0% | 1.2/4.0% | 3 |
| 10800 | 1 | 0.784 | 0.778 | 0.006 | - | - | 0.942 | 0.943 | 0.000 | 0.54x | 6.3/8.9/10.4% | 0.8/2.5% | 3 |
| 43200 | 1 | 0.800 | 0.794 | 0.006 | - | - | 0.947 | 0.947 | 0.000 | 0.37x | 4.3/6.1/7.2% | 0.5/1.7% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario alpine`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 0.25 | 1 | 0.725 | 0.714 | 0.011 | - | - | 0.900 | 0.902 | 0.000 | 1.34x | 16.0/22.3/25.8% | 1.9/6.0% | 3 |
| 1.0 | 1 | 0.723 | 0.711 | 0.012 | - | - | 0.902 | 0.905 | 0.000 | 1.44x | 16.9/23.7/27.6% | 2.0/6.6% | 3 |
| 4.0 | 1 | 0.699 | 0.682 | 0.016 | - | - | 0.893 | 0.894 | 0.000 | 1.75x | 20.6/28.9/34.0% | 2.5/8.4% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario alpine`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.728 | 0.718 | 0.010 | - | - | 0.873 | 0.944 | 0.509 | 5.63x | 50.6/66.0/75.0% | 4.0/12.3% | 3 |
| 1.0 | 1 | 0.674 | 0.664 | 0.011 | - | - | 0.836 | 0.927 | 0.468 | 6.20x | 54.8/69.3/77.1% | 4.3/13.9% | 3 |

> traceroute-per-hour=0.0: decode_failures 108

> traceroute-per-hour=1.0: decode_failures 103

### `MS-density` - nodes  `--scenario alpine`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.631 | 0.587 | 0.044 | - | - | 0.823 | 0.909 | 0.304 | 1.06x | 13.8/20.7/23.7% | 2.6/5.4% | 3 |
| 60 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 90 | 1 | 0.890 | 0.887 | 0.003 | - | - | 0.980 | 0.980 | 0.523 | 1.54x | 16.2/26.0/28.5% | 1.4/4.9% | 3 |
| 120 | 1 | 0.929 | 0.924 | 0.005 | - | - | 0.996 | 0.996 | 0.676 | 2.00x | 18.8/28.6/33.7% | 1.3/5.2% | 3 |
| 150 | 1 | 0.953 | 0.949 | 0.003 | - | - | 0.996 | 0.996 | 0.732 | 2.54x | 25.3/38.1/45.2% | 1.2/5.6% | 3 |

> nodes=40: decode_failures 7

### `MS-hopscale` - nodes  `--scenario alpine`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 120 | 1 | 0.683 | 0.675 | 0.009 | - | - | 0.756 | 0.759 | 0.194 | 2.08x | 14.4/18.7/24.0% | 1.4/5.2% | 3 |
| 250 | 1 | 0.519 | 0.509 | 0.010 | - | - | 0.600 | 0.601 | 0.182 | 4.63x | 17.1/25.4/35.9% | 1.6/5.2% | 3 |
| 500 | 1 | 0.310 | 0.304 | 0.006 | - | - | 0.462 | 0.466 | 0.118 | 10.02x | 19.0/28.3/48.5% | 1.8/6.2% | 3 |

> nodes=500: decode_failures 125

### `MS-oversubscribed` - nodes  `--scenario alpine`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.688 | 0.679 | 0.009 | - | - | 0.766 | 0.766 | 0.203 | 1.91x | 13.1/17.3/22.0% | 1.3/4.7% | 3 |
| 250 | 1 | 0.525 | 0.514 | 0.011 | - | - | 0.605 | 0.606 | 0.188 | 4.26x | 15.8/23.8/33.8% | 1.5/4.8% | 3 |
| 500 | 1 | 0.317 | 0.310 | 0.006 | - | - | 0.470 | 0.477 | 0.128 | 9.24x | 17.5/26.2/45.2% | 1.6/5.6% | 3 |

> nodes=250: decode_failures 2

> nodes=500: decode_failures 68

### `MS-roles` - role-mix  `--scenario alpine`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.775 | 0.765 | 0.010 | - | - | 0.953 | 0.954 | 0.000 | 1.34x | 15.7/22.4/25.9% | 1.9/6.0% | 3 |
| baymesh-2026-08 | 1 | 0.729 | 0.714 | 0.015 | - | - | 0.949 | 0.950 | 0.000 | 1.11x | 14.4/19.0/23.3% | 1.7/5.8% | 3 |

### `MS-roles-fav` - role-mix  `--scenario alpine`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.822 | 0.813 | 0.009 | - | - | 0.953 | 0.954 | 0.000 | 1.40x | 16.0/22.4/25.7% | 1.9/5.6% | 3 |
| baymesh-2026-08 | 1 | 0.785 | 0.775 | 0.010 | - | - | 0.943 | 0.944 | 0.000 | 1.24x | 16.2/20.6/25.0% | 2.0/5.3% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario alpine`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 0.05 | 1 | 0.732 | 0.723 | 0.009 | - | - | 0.902 | 0.903 | 0.000 | 1.39x | 17.2/23.7/28.1% | 1.8/5.7% | 3 |
| 0.1 | 1 | 0.732 | 0.722 | 0.011 | - | - | 0.898 | 0.900 | 0.000 | 1.48x | 18.1/26.0/31.6% | 1.9/5.5% | 3 |
| 0.2 | 1 | 0.737 | 0.727 | 0.010 | - | - | 0.893 | 0.894 | 0.000 | 1.66x | 20.2/31.2/39.3% | 2.0/5.4% | 3 |

### `MS-siting` - siting-mix  `--scenario alpine`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| local-typical | 1 | 0.596 | 0.593 | 0.003 | - | - | 0.798 | 0.799 | 0.000 | 1.28x | 13.6/20.5/24.2% | 1.7/5.3% | 3 |
| event | 1 | 0.154 | 0.149 | 0.005 | - | - | 0.365 | 0.370 | 0.000 | 0.94x | 5.0/10.3/15.6% | 1.5/4.0% | 3 |
| backbone | 1 | 0.950 | 0.949 | 0.001 | - | - | 0.983 | 0.984 | 0.428 | 1.11x | 22.9/30.4/33.4% | 1.5/5.3% | 3 |

> faster: 0.775 s per simulated hour against 1.81 over 67 prior run(s) - 2.3x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `MS-size` - nodes  `--scenario alpine`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.777 | 0.770 | 0.007 | - | - | 0.675 | 0.883 | 0.181 | 1.20x | 20.7/25.2/28.7% | 2.9/6.9% | 3 |
| 60 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 90 | 1 | 0.725 | 0.720 | 0.005 | - | - | 0.930 | 0.932 | 0.402 | 1.57x | 13.2/19.1/22.9% | 1.5/4.6% | 3 |
| 120 | 1 | 0.683 | 0.675 | 0.009 | - | - | 0.756 | 0.759 | 0.194 | 2.08x | 14.4/18.7/24.0% | 1.4/5.2% | 3 |
| 150 | 1 | 0.647 | 0.635 | 0.012 | - | - | 0.736 | 0.737 | 0.338 | 2.68x | 15.1/21.5/32.2% | 1.6/5.4% | 3 |

> nodes=40: decode_failures 20

### `MS-stretch` - stretch  `--scenario alpine`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 1.25 | 1 | 0.468 | 0.451 | 0.017 | - | - | 0.663 | 0.677 | 0.000 | 1.31x | 10.6/14.9/18.9% | 1.8/4.3% | 3 |
| 1.5 | 1 | 0.232 | 0.229 | 0.003 | - | - | 0.397 | 0.397 | 0.000 | 1.18x | 7.6/12.9/19.9% | 1.8/4.7% | 3 |
| 2.0 | 1 | 0.101 | 0.100 | 0.001 | - | - | 0.223 | 0.254 | 0.000 | 0.69x | 3.2/6.5/9.2% | 1.0/2.9% | 3 |

> stretch=1.25: decode_failures 17

> stretch=2.0: decode_failures 8

### `MS-topology` - topology  `--scenario alpine`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| clustered | 1 | 0.960 | 0.958 | 0.002 | - | - | 0.998 | 0.999 | 0.204 | 1.04x | 23.3/29.7/33.2% | 1.1/5.5% | 3 |
| corridor | 1 | 0.550 | 0.530 | 0.020 | - | - | 0.513 | 0.567 | 0.193 | 1.48x | 15.4/20.3/25.5% | 2.2/5.1% | 3 |
| hub | 1 | 0.928 | 0.919 | 0.009 | - | - | 0.967 | 0.967 | 0.814 | 1.20x | 20.5/34.6/36.2% | 1.8/5.4% | 3 |

> topology=corridor: decode_failures 24

### `PR-crladder` - coding-rate-ladder  `--scenario alpine`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.695 | 0.695 | 0.000 | - | - | 0.880 | 0.887 | 0.000 | 1.55x | 18.3/25.4/29.4% | 2.2/6.9% | 3 |
| True | 1 | 0.690 | 0.690 | 0.000 | - | - | 0.854 | 0.894 | 0.000 | 1.55x | 18.2/25.5/29.6% | 2.2/6.9% | 3 |

> coding-rate-ladder=True: decode_failures 37

### `PR-dmmode-cr` - dm-mode  `--scenario alpine`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.690 | 0.690 | 0.000 | - | - | 0.854 | 0.894 | 0.000 | 1.55x | 18.2/25.5/29.6% | 2.2/6.9% | 3 |
| m4-early-flood | 1 | 0.701 | 0.701 | 0.000 | - | - | 0.860 | 0.899 | 0.000 | 1.54x | 18.1/25.4/29.5% | 2.2/6.9% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 37

> dm-mode=m4-early-flood: decode_failures 29

> slower: 12.2 s per simulated hour against 2.57 over 68 prior run(s) - 4.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `PR-protocol` - protocol  `--scenario alpine`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.727 | 0.727 | 0.000 | - | - | 0 | 0.000 | 0.000 | 1.26x | 14.7/20.7/24.1% | 1.8/5.5% | 3 |
| chain | 1 | 0.723 | 0.717 | 0.006 | - | - | 0.840 | 0.916 | 0.000 | 1.50x | 17.6/24.8/29.0% | 2.1/6.5% | 3 |
| sr | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |

### `PR-repeats` - extra-repeats  `--scenario alpine`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| True | 1 | 0.738 | 0.727 | 0.011 | - | - | 0.910 | 0.916 | 0.000 | 1.31x | 15.4/21.7/25.2% | 1.9/5.9% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario alpine`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.929 | 0.924 | 0.005 | - | - | 0.996 | 0.996 | 0.676 | 2.00x | 18.8/28.6/33.7% | 1.3/5.2% | 3 |
| True | 1 | 0.930 | 0.926 | 0.004 | - | - | 0.997 | 0.997 | 0.706 | 2.03x | 19.1/28.6/33.7% | 1.4/5.1% | 3 |

### `RF-bw500` - preset  `--scenario alpine`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.143 | 0.140 | 0.004 | - | - | 0.312 | 0.330 | 0.000 | 0.04x | 0.2/0.4/0.5% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.355 | 0.352 | 0.003 | - | - | 0.585 | 0.588 | 0.000 | 0.24x | 1.6/3.2/4.9% | 0.3/1.1% | 3 |
| LONG_TURBO | 1 | 0.643 | 0.629 | 0.014 | - | - | 0.847 | 0.849 | 0.000 | 1.19x | 12.3/15.9/20.4% | 1.7/5.2% | 3 |

> preset=SHORT_TURBO: decode_failures 6

### `RF-duct` - duct-per-hour  `--scenario alpine`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 0.25 | 1 | 0.780 | 0.769 | 0.011 | - | - | 0.931 | 0.934 | 0.036 | 1.16x | 16.0/22.1/25.2% | 1.5/5.5% | 3 |
| 1.0 | 1 | 0.856 | 0.847 | 0.009 | - | - | 0.954 | 0.957 | 0.107 | 1.00x | 19.1/24.3/27.4% | 1.2/5.3% | 3 |

### `RF-eu-presets` - preset  `--scenario alpine`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.269 | 0.266 | 0.003 | - | - | 0.516 | 0.519 | 0.000 | 0.12x | 0.7/1.6/2.2% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| LITE_FAST | 1 | 0.657 | 0.642 | 0.015 | - | - | 0.886 | 0.894 | 0.000 | 0.95x | 10.8/14.7/20.3% | 1.3/4.4% | 3 |
| NARROW_SLOW | 1 | 0.703 | 0.691 | 0.012 | - | - | 0.896 | 0.898 | 0.000 | 1.19x | 13.5/17.7/23.0% | 1.6/5.5% | 3 |

### `RF-noise` - noise-profile  `--scenario alpine`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| temporal | 1 | 0.629 | 0.606 | 0.023 | - | - | 0.868 | 0.870 | 0.000 | 1.30x | 15.2/21.0/24.4% | 1.9/5.7% | 3 |
| transient | 1 | 0.725 | 0.712 | 0.013 | - | - | 0.900 | 0.904 | 0.000 | 1.28x | 15.1/21.1/24.4% | 1.8/5.8% | 3 |
| periodic | 1 | 0.579 | 0.567 | 0.012 | - | - | 0.747 | 0.749 | 0.000 | 1.21x | 14.3/20.0/22.9% | 1.8/5.1% | 3 |

> noise-profile=temporal: decode_failures 3

### `RF-preset` - preset  `--scenario alpine`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.269 | 0.266 | 0.003 | - | - | 0.516 | 0.519 | 0.000 | 0.12x | 0.7/1.6/2.2% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| LONG_MODERATE | 1 | 0.717 | 0.701 | 0.016 | - | - | 0.812 | 0.814 | 0.356 | 3.23x | 41.1/57.5/62.3% | 4.6/11.6% | 3 |

> preset=LONG_MODERATE: decode_failures 2

### `RF-preset-turbo` - preset  `--scenario alpine`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.038 | 0.037 | 0.001 | - | - | 0.125 | 0.133 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.143 | 0.140 | 0.004 | - | - | 0.312 | 0.330 | 0.000 | 0.04x | 0.2/0.4/0.5% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| LONG_TURBO | 1 | 0.643 | 0.629 | 0.014 | - | - | 0.847 | 0.849 | 0.000 | 1.19x | 12.3/15.9/20.4% | 1.7/5.2% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.709 | 0.697 | 0.011 | - | - | 0.881 | 0.886 | 0.000 | 1.63x | 19.6/24.0/29.5% | 2.2/7.6% | 3 |

> preset=SHORT_TURBO: decode_failures 6

### `RF-pulse` - noise-pulse-interval-ms  `--scenario alpine`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.690 | 0.676 | 0.014 | - | - | 0.856 | 0.860 | 0.000 | 1.26x | 14.9/21.0/24.3% | 1.8/5.5% | 3 |
| 10000 | 1 | 0.579 | 0.567 | 0.012 | - | - | 0.747 | 0.749 | 0.000 | 1.21x | 14.3/20.0/22.9% | 1.8/5.1% | 3 |
| 4000 | 1 | 0.359 | 0.354 | 0.005 | - | - | 0.436 | 0.515 | 0.000 | 1.07x | 13.1/17.7/20.5% | 1.7/3.8% | 3 |
| 2000 | 1 | 0.076 | 0.076 | 0.000 | - | - | 0.086 | 0.167 | 0.000 | 0.72x | 9.4/12.4/14.5% | 1.1/2.1% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 3

### `RF-stretch-duct` - duct-per-hour  `--scenario alpine`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.232 | 0.229 | 0.003 | - | - | 0.397 | 0.397 | 0.000 | 1.18x | 7.6/12.9/19.9% | 1.8/4.7% | 3 |
| 1.0 | 1 | 0.592 | 0.589 | 0.004 | - | - | 0.707 | 0.707 | 0.409 | 0.95x | 11.7/16.1/20.5% | 1.4/4.2% | 3 |

### `RF-txpower` - tx-power  `--scenario alpine`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 22 | 1 | 0.316 | 0.309 | 0.007 | - | - | 0.544 | 0.566 | 0.000 | 1.30x | 9.1/15.0/22.5% | 1.9/4.4% | 3 |
| 17 | 1 | 0.130 | 0.127 | 0.003 | - | - | 0.281 | 0.288 | 0.000 | 0.79x | 3.9/8.4/10.4% | 1.2/2.9% | 3 |
| 14 | 1 | 0.062 | 0.060 | 0.001 | - | - | 0.197 | 0.213 | 0.000 | 0.49x | 1.5/4.6/6.7% | 0.6/2.2% | 3 |

> tx-power=22: decode_failures 10

> tx-power=14: decode_failures 2

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario alpine`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.929 | 0.924 | 0.005 | - | - | 0.996 | 0.996 | 0.676 | 2.00x | 18.8/28.6/33.7% | 1.3/5.2% | 3 |
| True | 1 | 0.922 | 0.915 | 0.006 | - | - | 0.995 | 0.995 | 0.667 | 2.35x | 22.0/32.2/37.8% | 1.7/5.8% | 3 |

### `RT-favourites` - favourite-routers  `--scenario alpine`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.729 | 0.719 | 0.011 | - | - | 0.903 | 0.905 | 0.000 | 1.32x | 16.2/22.7/26.3% | 1.8/5.8% | 3 |
| True | 1 | 0.798 | 0.790 | 0.008 | - | - | 0.904 | 0.907 | 0.000 | 1.37x | 16.2/22.3/25.1% | 1.9/5.3% | 3 |

### `RT-hopassign` - hop-assign  `--scenario alpine`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| random | 1 | 0.687 | 0.672 | 0.015 | - | - | 0.876 | 0.877 | 0.000 | 1.32x | 15.3/22.1/25.3% | 1.9/5.6% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario alpine`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.584 | 0.538 | 0.045 | - | - | 0.850 | 0.867 | 0.000 | 1.16x | 13.9/19.7/22.9% | 1.8/4.9% | 3 |
| 7 | 1 | 0.840 | 0.834 | 0.006 | - | - | 0.960 | 0.961 | 0.000 | 1.44x | 16.6/22.7/26.3% | 2.0/5.8% | 3 |
| 15 | 1 | 0.899 | 0.897 | 0.002 | - | - | 0.961 | 0.961 | 0.000 | 1.46x | 16.9/22.8/26.6% | 2.0/5.6% | 3 |
| 32 | 1 | 0.900 | 0.898 | 0.002 | - | - | 0.966 | 0.966 | 0.000 | 1.46x | 16.9/22.8/26.6% | 2.0/5.6% | 3 |

> hop-limit=3: decode_failures 11

### `RT-hopspread` - hop-limit  `--scenario alpine`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.584 | 0.538 | 0.045 | - | - | 0.850 | 0.867 | 0.000 | 1.16x | 13.9/19.7/22.9% | 1.8/4.9% | 3 |
| 5 | 1 | 0.738 | 0.722 | 0.016 | - | - | 0.938 | 0.940 | 0.000 | 1.32x | 15.3/21.5/24.9% | 1.9/5.9% | 3 |
| 7 | 1 | 0.840 | 0.834 | 0.006 | - | - | 0.960 | 0.961 | 0.000 | 1.44x | 16.6/22.7/26.3% | 2.0/5.8% | 3 |

> hop-limit=3: decode_failures 11

### `RT-rebroadcast` - rebroadcast-mode  `--scenario alpine`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| KNOWN_ONLY | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.726 | 0.726 | 0.000 | - | - | 0.804 | 0.924 | 0.000 | 1.26x | 14.8/20.8/24.3% | 1.8/5.5% | 3 |

### `RT-spread` - hop-spread  `--scenario alpine`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.584 | 0.538 | 0.045 | - | - | 0.850 | 0.867 | 0.000 | 1.16x | 13.9/19.7/22.9% | 1.8/4.9% | 3 |
| True | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |

> hop-spread=False: decode_failures 11

### `SC-signing` - signature-policy  `--scenario alpine`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| BALANCED | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| STRICT | 1 | 0.652 | 0.652 | 0.000 | - | - | 0.841 | 0.842 | 0.000 | 1.38x | 16.0/22.6/26.3% | 2.0/6.1% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario alpine`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| dm | 1 | 0.732 | 0.720 | 0.012 | - | - | 0.899 | 0.903 | 0.000 | 1.26x | 14.9/20.8/24.2% | 1.8/5.7% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario alpine`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.742 | 0.730 | 0.013 | - | - | 0.916 | 0.919 | 0.000 | 1.31x | 15.5/21.7/25.3% | 1.9/5.8% | 3 |
| local | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| time | 1 | 0.727 | 0.716 | 0.011 | - | - | 0.912 | 0.913 | 0.000 | 1.32x | 15.5/21.8/25.2% | 1.9/5.9% | 3 |
| window | 1 | 0.729 | 0.719 | 0.010 | - | - | 0.903 | 0.908 | 0.000 | 1.29x | 15.2/21.4/24.8% | 1.8/5.8% | 3 |

> bucket-mode=global: misdecodes 41

> bucket-mode=time: misdecodes 22

> bucket-mode=window: misdecodes 16

### `SF-bucket-time` - time-bucket-s  `--scenario alpine`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.723 | 0.711 | 0.012 | - | - | 0.908 | 0.911 | 0.000 | 1.47x | 16.9/24.2/28.1% | 2.1/6.6% | 3 |
| 1800 | 1 | 0.727 | 0.716 | 0.011 | - | - | 0.912 | 0.913 | 0.000 | 1.32x | 15.5/21.8/25.2% | 1.9/5.9% | 3 |
| 3600 | 1 | 0.739 | 0.729 | 0.011 | - | - | 0.914 | 0.915 | 0.000 | 1.31x | 15.5/21.7/25.2% | 1.8/5.8% | 3 |

> time-bucket-s=600: misdecodes 109

> time-bucket-s=1800: misdecodes 22

> time-bucket-s=3600: misdecodes 6

> time-bucket-s=3600: decode_failures 3

### `SF-cadence` - trigger  `--scenario alpine`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| interval | 1 | 0.715 | 0.699 | 0.015 | - | - | 0.888 | 0.898 | 0.000 | 1.76x | 19.7/28.9/33.7% | 2.6/7.8% | 3 |
| aimd | 1 | 0.726 | 0.723 | 0.003 | - | - | 0.832 | 0.920 | 0.000 | 1.32x | 15.5/21.7/25.4% | 1.9/5.7% | 3 |
| bucket+interval | 1 | 0.713 | 0.698 | 0.014 | - | - | 0.896 | 0.898 | 0.000 | 1.79x | 20.2/29.6/34.4% | 2.7/7.9% | 3 |

> trigger=interval: misdecodes 7

> trigger=interval: decode_failures 3

> trigger=aimd: misdecodes 3

> trigger=aimd: decode_failures 4

> trigger=bucket+interval: misdecodes 16

### `SF-capacity` - capacity  `--scenario alpine`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.740 | 0.727 | 0.014 | - | - | 0.909 | 0.915 | 0.000 | 1.28x | 15.1/21.2/24.7% | 1.8/5.8% | 3 |
| 8 | 1 | 0.735 | 0.723 | 0.012 | - | - | 0.920 | 0.921 | 0.000 | 1.30x | 15.3/21.6/25.0% | 1.8/5.9% | 3 |
| 16 | 1 | 0.730 | 0.718 | 0.013 | - | - | 0.907 | 0.910 | 0.000 | 1.30x | 15.3/21.7/25.2% | 1.8/5.8% | 3 |
| 32 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 50 | 1 | 0.736 | 0.724 | 0.012 | - | - | 0.920 | 0.921 | 0.000 | 1.30x | 15.3/21.5/24.9% | 1.8/5.8% | 3 |

> capacity=4: decode_failures 85

> capacity=8: decode_failures 49

### `SF-capacity-local` - capacity  `--scenario alpine`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.740 | 0.727 | 0.014 | - | - | 0.909 | 0.915 | 0.000 | 1.28x | 15.1/21.2/24.7% | 1.8/5.8% | 3 |
| 8 | 1 | 0.735 | 0.723 | 0.012 | - | - | 0.920 | 0.921 | 0.000 | 1.30x | 15.3/21.6/25.0% | 1.8/5.9% | 3 |
| 16 | 1 | 0.730 | 0.718 | 0.013 | - | - | 0.907 | 0.910 | 0.000 | 1.30x | 15.3/21.7/25.2% | 1.8/5.8% | 3 |
| 32 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 50 | 1 | 0.736 | 0.724 | 0.012 | - | - | 0.920 | 0.921 | 0.000 | 1.30x | 15.3/21.5/24.9% | 1.8/5.8% | 3 |

> capacity=4: decode_failures 85

> capacity=8: decode_failures 49

### `SF-capacity-window` - capacity  `--scenario alpine`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.724 | 0.718 | 0.006 | - | - | 0.840 | 0.905 | 0.000 | 1.30x | 15.2/21.3/24.9% | 1.8/5.6% | 3 |
| 16 | 1 | 0.742 | 0.730 | 0.012 | - | - | 0.910 | 0.917 | 0.000 | 1.28x | 15.1/21.2/24.7% | 1.8/5.7% | 3 |
| 32 | 1 | 0.729 | 0.719 | 0.010 | - | - | 0.903 | 0.908 | 0.000 | 1.29x | 15.2/21.4/24.8% | 1.8/5.8% | 3 |

> capacity=8: misdecodes 7

> capacity=8: decode_failures 92

> capacity=16: misdecodes 20

> capacity=16: decode_failures 10

> capacity=32: misdecodes 16

### `SF-catchup` - catch-up-hours  `--scenario alpine`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.713 | 0.698 | 0.014 | - | - | 0.896 | 0.898 | 0.000 | 1.79x | 20.2/29.6/34.4% | 2.7/7.9% | 3 |
| 02-06 | 1 | 0.732 | 0.724 | 0.007 | - | - | 0.858 | 0.917 | 0.000 | 1.33x | 15.6/22.0/25.7% | 1.9/6.0% | 3 |
| 00-08 | 1 | 0.726 | 0.718 | 0.008 | - | - | 0.865 | 0.912 | 0.000 | 1.40x | 16.1/23.2/27.2% | 1.9/6.3% | 3 |

> catch-up-hours=: misdecodes 16

> catch-up-hours=02-06: misdecodes 1

> catch-up-hours=02-06: decode_failures 43

> catch-up-hours=00-08: decode_failures 43

### `SF-hops-flat` - hops-apart  `--scenario alpine`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.725 | 0.722 | 0.002 | - | - | 0.908 | 0.908 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.6% | 3 |
| 2 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 3 | 1 | 0.748 | 0.722 | 0.025 | - | - | 0.919 | 0.921 | 0.000 | 1.30x | 15.1/21.7/24.9% | 1.9/5.8% | 3 |
| 4 | 1 | 0.762 | 0.719 | 0.043 | - | - | 0.893 | 0.915 | 0.000 | 1.32x | 15.4/22.4/25.1% | 1.9/5.9% | 3 |

> hops-apart=4: decode_failures 32

### `SF-hops-spread` - hops-apart  `--scenario alpine`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.725 | 0.722 | 0.002 | - | - | 0.908 | 0.908 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.6% | 3 |
| 2 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 3 | 1 | 0.748 | 0.722 | 0.025 | - | - | 0.919 | 0.921 | 0.000 | 1.30x | 15.1/21.7/24.9% | 1.9/5.8% | 3 |
| 4 | 1 | 0.762 | 0.719 | 0.043 | - | - | 0.893 | 0.915 | 0.000 | 1.32x | 15.4/22.4/25.1% | 1.9/5.9% | 3 |
| 5 | 1 | 0.759 | 0.715 | 0.043 | - | - | 0.903 | 0.913 | 0.000 | 1.31x | 15.3/21.8/25.0% | 1.9/5.9% | 3 |

> hops-apart=4: decode_failures 32

> hops-apart=5: decode_failures 3

### `SF-jitter-global` - advert-jitter-s  `--scenario alpine`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.733 | 0.721 | 0.012 | - | - | 0.918 | 0.919 | 0.000 | 1.29x | 15.3/21.3/24.7% | 1.8/5.8% | 3 |
| 30 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 120 | 1 | 0.732 | 0.719 | 0.013 | - | - | 0.908 | 0.912 | 0.000 | 1.29x | 15.1/21.1/24.6% | 1.8/5.8% | 3 |
| 600 | 1 | 0.735 | 0.723 | 0.012 | - | - | 0.908 | 0.912 | 0.000 | 1.30x | 15.3/21.3/24.8% | 1.8/5.8% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario alpine`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.733 | 0.721 | 0.012 | - | - | 0.918 | 0.919 | 0.000 | 1.29x | 15.3/21.3/24.7% | 1.8/5.8% | 3 |
| 30 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 120 | 1 | 0.732 | 0.719 | 0.013 | - | - | 0.908 | 0.912 | 0.000 | 1.29x | 15.1/21.1/24.6% | 1.8/5.8% | 3 |
| 600 | 1 | 0.735 | 0.723 | 0.012 | - | - | 0.908 | 0.912 | 0.000 | 1.30x | 15.3/21.3/24.8% | 1.8/5.8% | 3 |

### `SF-place-flat` - place  `--scenario alpine`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.720 | 0.719 | 0.001 | - | - | 0.404 | 0.890 | 0.000 | 1.27x | 14.8/21.0/24.4% | 1.8/5.5% | 3 |
| routers | 1 | 0.727 | 0.720 | 0.007 | - | - | 0.906 | 0.908 | 0.000 | 1.29x | 15.1/21.3/24.7% | 1.8/5.7% | 3 |
| alternate-routers | 1 | 0.727 | 0.722 | 0.006 | - | - | 0.903 | 0.905 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.7% | 3 |
| beside-router | 1 | 0.734 | 0.725 | 0.009 | - | - | 0.917 | 0.917 | 0.000 | 1.28x | 15.0/21.3/24.8% | 1.8/5.5% | 3 |
| random-clients | 1 | 0.745 | 0.718 | 0.026 | - | - | 0.868 | 0.903 | 0.000 | 1.30x | 15.2/22.1/25.1% | 1.8/5.6% | 3 |
| hops-apart | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |

> place=spread: decode_failures 5

> place=random-clients: decode_failures 25

### `SF-place-spread` - place  `--scenario alpine`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.720 | 0.719 | 0.001 | - | - | 0.404 | 0.890 | 0.000 | 1.27x | 14.8/21.0/24.4% | 1.8/5.5% | 3 |
| routers | 1 | 0.727 | 0.720 | 0.007 | - | - | 0.906 | 0.908 | 0.000 | 1.29x | 15.1/21.3/24.7% | 1.8/5.7% | 3 |
| alternate-routers | 1 | 0.727 | 0.722 | 0.006 | - | - | 0.903 | 0.905 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.7% | 3 |
| beside-router | 1 | 0.734 | 0.725 | 0.009 | - | - | 0.917 | 0.917 | 0.000 | 1.28x | 15.0/21.3/24.8% | 1.8/5.5% | 3 |
| random-clients | 1 | 0.745 | 0.718 | 0.026 | - | - | 0.868 | 0.903 | 0.000 | 1.30x | 15.2/22.1/25.1% | 1.8/5.6% | 3 |
| hops-apart | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |

> place=spread: decode_failures 5

> place=random-clients: decode_failures 25

### `SF-provide-transport` - provide-transport  `--scenario alpine`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| broadcast | 1 | 0.768 | 0.707 | 0.061 | - | - | 0.900 | 0.903 | 0.000 | 1.41x | 16.5/23.0/26.7% | 2.0/6.0% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario alpine`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| heard | 1 | 0.739 | 0.726 | 0.013 | - | - | 0.919 | 0.920 | 0.000 | 1.29x | 15.3/21.3/24.8% | 1.8/5.8% | 3 |

> replay-ordering=heard: misdecodes 11

### `SF-replay-order-broadcast` - replay-ordering  `--scenario alpine`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.768 | 0.707 | 0.061 | - | - | 0.900 | 0.903 | 0.000 | 1.41x | 16.5/23.0/26.7% | 2.0/6.0% | 3 |
| heard | 1 | 0.775 | 0.708 | 0.067 | - | - | 0.903 | 0.909 | 0.000 | 1.41x | 16.6/23.1/26.7% | 2.0/6.0% | 3 |

> replay-ordering=heard: misdecodes 7

### `SF-resolve` - resolve  `--scenario alpine`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| enum | 1 | 0.733 | 0.721 | 0.013 | - | - | 0.908 | 0.915 | 0.000 | 1.28x | 15.1/21.2/24.6% | 1.8/5.8% | 3 |
| hybrid | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |

### `SF-servers-allrouters` - servers  `--scenario alpine`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.727 | 0.720 | 0.007 | - | - | 0.906 | 0.908 | 0.000 | 1.29x | 15.1/21.3/24.7% | 1.8/5.7% | 3 |
| 6 | 1 | 0.736 | 0.712 | 0.025 | - | - | 0.929 | 0.933 | 0.000 | 1.32x | 15.5/21.8/25.3% | 1.9/6.0% | 6 |

### `SF-servers-flat` - servers  `--scenario alpine`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.729 | 0.724 | 0.005 | - | - | 0.908 | 0.911 | 0.000 | 1.29x | 15.2/21.2/24.8% | 1.8/5.7% | 2 |
| 3 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 5 | 1 | 0.735 | 0.722 | 0.013 | - | - | 0.919 | 0.919 | 0.000 | 1.34x | 15.7/22.1/25.5% | 1.9/6.0% | 5 |
| 8 | 1 | 0.737 | 0.717 | 0.020 | - | - | 0.920 | 0.921 | 0.000 | 1.37x | 15.8/23.1/26.4% | 1.9/6.1% | 8 |

> servers=8: misdecodes 1

### `SF-servers-spread` - servers  `--scenario alpine`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.729 | 0.724 | 0.005 | - | - | 0.908 | 0.911 | 0.000 | 1.29x | 15.2/21.2/24.8% | 1.8/5.7% | 2 |
| 3 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 5 | 1 | 0.735 | 0.722 | 0.013 | - | - | 0.919 | 0.919 | 0.000 | 1.34x | 15.7/22.1/25.5% | 1.9/6.0% | 5 |
| 8 | 1 | 0.737 | 0.717 | 0.020 | - | - | 0.920 | 0.921 | 0.000 | 1.37x | 15.8/23.1/26.4% | 1.9/6.1% | 8 |

> servers=8: misdecodes 1

### `SF-signed` - signed  `--scenario alpine`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| True | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario alpine`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.730 | 0.720 | 0.010 | - | - | 0.904 | 0.911 | 0.000 | 1.20x | 14.0/19.6/22.9% | 1.7/5.4% | 3 |
| 1 | 1 | 0.739 | 0.727 | 0.011 | - | - | 0.919 | 0.920 | 0.000 | 1.19x | 13.9/19.6/22.8% | 1.6/5.3% | 3 |
| 2 | 1 | 0.740 | 0.726 | 0.014 | - | - | 0.922 | 0.923 | 0.000 | 1.17x | 13.9/19.4/22.7% | 1.7/5.3% | 3 |
| 4 | 1 | 0.734 | 0.722 | 0.012 | - | - | 0.906 | 0.911 | 0.000 | 1.18x | 14.1/19.5/22.8% | 1.7/5.3% | 3 |

### `SF-width` - short-id-bits  `--scenario alpine`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.733 | 0.722 | 0.011 | - | - | 0.908 | 0.912 | 0.000 | 1.30x | 15.3/21.6/25.0% | 1.8/5.8% | 3 |
| 24 | 1 | 0.730 | 0.718 | 0.012 | - | - | 0.906 | 0.914 | 0.000 | 1.30x | 15.3/21.3/24.9% | 1.8/5.8% | 3 |
| 32 | 1 | 0.737 | 0.725 | 0.012 | - | - | 0.908 | 0.913 | 0.000 | 1.29x | 15.2/21.3/24.8% | 1.8/5.8% | 3 |
| 64 | 1 | 0.733 | 0.721 | 0.012 | - | - | 0.913 | 0.917 | 0.000 | 1.30x | 15.4/21.5/25.0% | 1.8/5.8% | 3 |

### `SF-window-size` - window-size  `--scenario alpine`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.729 | 0.717 | 0.013 | - | - | 0.909 | 0.909 | 0.000 | 1.38x | 16.2/22.7/26.4% | 1.9/6.0% | 3 |
| 16 | 1 | 0.737 | 0.724 | 0.013 | - | - | 0.919 | 0.920 | 0.000 | 1.28x | 15.1/21.0/24.4% | 1.8/5.7% | 3 |
| 32 | 1 | 0.729 | 0.719 | 0.010 | - | - | 0.903 | 0.908 | 0.000 | 1.29x | 15.2/21.4/24.8% | 1.8/5.8% | 3 |

> window-size=8: misdecodes 116

> window-size=16: misdecodes 42

> window-size=32: misdecodes 16

### `TH-congestion` - no-congestion-scaling  `--scenario alpine`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.929 | 0.924 | 0.005 | - | - | 0.996 | 0.996 | 0.676 | 2.00x | 18.8/28.6/33.7% | 1.3/5.2% | 3 |
| True | 1 | 0.734 | 0.724 | 0.010 | - | - | 0.872 | 0.951 | 0.512 | 5.64x | 51.2/66.3/75.2% | 3.9/12.3% | 3 |

> no-congestion-scaling=True: decode_failures 112

### `TH-congestion-input` - congestion-input  `--scenario alpine`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.525 | 0.514 | 0.011 | - | - | 0.605 | 0.606 | 0.188 | 4.26x | 15.8/23.8/33.8% | 1.5/4.8% | 3 |
| truesize | 1 | 0.557 | 0.545 | 0.012 | - | - | 0.646 | 0.647 | 0.195 | 3.15x | 11.7/18.5/26.0% | 1.1/3.9% | 3 |

> congestion-input=hotstore: decode_failures 2

### `TH-congestion-mode` - congestion-mode  `--scenario alpine`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.934 | 0.929 | 0.004 | - | - | 0.998 | 0.998 | 0.680 | 1.89x | 17.9/26.9/31.7% | 1.3/4.9% | 3 |
| adaptive | 1 | 0.929 | 0.924 | 0.005 | - | - | 0.996 | 0.996 | 0.676 | 2.00x | 18.8/28.6/33.7% | 1.3/5.2% | 3 |

