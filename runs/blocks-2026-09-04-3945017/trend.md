# Sweep blocks-2026-09-04-3945017

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** alpine
- **seed base** 3945017 · seeds 3945017
- **blocks** 87 run
- **compute** 10.9 h of simulator time across every cell
- **generated** 2026-09-04T08:47:51+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>77 warnings</summary>

- DB-hotstore-stress: max-num-nodes=10: decode_failures 48
- DB-hotstore-stress: max-num-nodes=120: decode_failures 56
- DB-hotstore-stress: max-num-nodes=250: decode_failures 42
- DB-warm: warm-num-nodes=0: decode_failures 78
- DB-warm: warm-num-nodes=25: decode_failures 78
- DB-warm: warm-num-nodes=100: decode_failures 78
- DB-warm: warm-num-nodes=2000: decode_failures 78
- DG-burst: burst-loss=0.1: decode_failures 25
- DG-burst: burst-loss=0.2: decode_failures 5
- DG-burst: burst-loss=0.3: decode_failures 28
- DG-outage: burst-loss=0.1: decode_failures 36
- DG-outage: burst-loss=0.2: decode_failures 30
- DG-outage: burst-loss=0.3: decode_failures 35
- FW-mixed-26: legacy-fraction=0.25: decode_failures 32
- FW-mixed-26: slower: 3.68 s per simulated hour against 1.71 over 14 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- FW-mixed: legacy-fraction=0.25: decode_failures 32
- FW-mixed: slower: 4.11 s per simulated hour against 1.68 over 14 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 78
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 11.5% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 94
- MS-density: nodes=40: 3 archives requested, 2 placed - group on the placed count
- MS-hopscale: nodes=250: decode_failures 169
- MS-hopscale: nodes=500: decode_failures 140
- MS-oversubscribed: nodes=250: decode_failures 56
- MS-oversubscribed: nodes=500: decode_failures 101
- MS-siting: siting-mix=event: decode_failures 10
- MS-size: nodes=90: decode_failures 7
- MS-stretch: stretch=1.5: decode_failures 30
- MS-topology: topology=clustered: decode_failures 16
- PR-dmmode-cr: inert: every value of `dm-mode` produced identical numbers - either the flag is not read, or it needs a second flag before it does anything (README §10.4)
- RF-bw500: preset=SHORT_TURBO: decode_failures 5
- RF-bw500: preset=MEDIUM_TURBO: decode_failures 5
- RF-preset-turbo: preset=SHORT_TURBO: decode_failures 5
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 8
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 30
- RF-stretch-duct: duct-per-hour=1.0: decode_failures 28
- RF-stretch-duct: slower: 6.11 s per simulated hour against 2.43 over 14 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- RF-txpower: tx-power=17: decode_failures 3
- RT-adopt: no-adopt-hop-recommendation=True: misdecodes 1
- RT-hoplimit: hop-limit=32: misdecodes 1
- SF-bucket-mode: bucket-mode=global: misdecodes 44
- SF-bucket-mode: bucket-mode=time: misdecodes 28
- SF-bucket-mode: bucket-mode=window: misdecodes 11
- SF-bucket-time: time-bucket-s=600: misdecodes 142
- SF-bucket-time: time-bucket-s=1800: misdecodes 28
- SF-bucket-time: time-bucket-s=3600: misdecodes 14
- SF-cadence: trigger=interval: misdecodes 14
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=aimd: decode_failures 3
- SF-cadence: trigger=bucket+interval: misdecodes 6
- SF-capacity-local: capacity=4: decode_failures 94
- SF-capacity-local: capacity=8: decode_failures 27
- SF-capacity-local: capacity=16: decode_failures 1
- SF-capacity: capacity=4: decode_failures 94
- SF-capacity: capacity=8: decode_failures 27
- SF-capacity: capacity=16: decode_failures 1
- SF-capacity-window: capacity=8: misdecodes 22
- SF-capacity-window: capacity=8: decode_failures 9
- SF-capacity-window: capacity=16: misdecodes 7
- SF-capacity-window: capacity=32: misdecodes 11
- SF-catchup: catch-up-hours=: misdecodes 6
- SF-catchup: catch-up-hours=02-06: decode_failures 32
- SF-catchup: catch-up-hours=00-08: decode_failures 33
- SF-hops-flat: hops-apart=4: decode_failures 3
- SF-hops-spread: hops-apart=4: decode_failures 3
- SF-hops-spread: hops-apart=5: decode_failures 25
- SF-place-flat: place=spread: decode_failures 28
- SF-place-spread: place=spread: decode_failures 28
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 12
- SF-replay-order: replay-ordering=heard: misdecodes 17
- SF-window-size: window-size=8: misdecodes 107
- SF-window-size: window-size=16: misdecodes 34
- SF-window-size: window-size=32: misdecodes 11
- TH-congestion-input: congestion-input=hotstore: decode_failures 56
- TH-congestion-input: congestion-input=truesize: decode_failures 2
- TH-congestion-input: slower: 22.1 s per simulated hour against 10.6 over 14 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- TH-congestion: no-congestion-scaling=True: decode_failures 31

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `RF-stretch-duct` | 6.11 | 2.43 | 2.51x | 14 |
| `FW-mixed` | 4.11 | 1.68 | 2.45x | 14 |
| `FW-mixed-26` | 3.68 | 1.71 | 2.15x | 14 |
| `TH-congestion-input` | 22.1 | 10.6 | 2.09x | 14 |
| `MS-hopscale` | 30.5 | 17.7 | 1.73x | 14 |
| `MS-stretch` | 2.94 | 1.94 | 1.52x | 14 |
| `MS-topology` | 2.74 | 1.82 | 1.50x | 14 |
| `SF-capacity` | 1.16 | 1.75 | 0.66x | 14 |
| `MS-roles` | 1.19 | 1.8 | 0.66x | 14 |
| `FW-firmware` | 1.18 | 1.8 | 0.66x | 14 |
| `RT-spread` | 1.38 | 2.11 | 0.66x | 14 |
| `RF-preset` | 1.94 | 2.97 | 0.65x | 14 |
| `TH-congestion` | 12.1 | 19 | 0.64x | 14 |
| `LD-chatty` | 2.81 | 4.68 | 0.60x | 14 |
| `MS-roles-fav` | 0.949 | 1.76 | 0.54x | 14 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `PR-protocol` | protocol | **held** | 0 → 0.917 | 0.917 | 0.782 → 0.794 | 1.1x bytes_on_air | up | 3 |
| `BL-control` | protocol | **held** | 0 → 0.915 | 0.915 | 0.790 → 0.791 | 1x bytes_on_air | up | 2 |
| `RF-preset-turbo` | preset | **held** | 0.033 → 0.917 | 0.884 | 0.034 → 0.794 | 50x advert_bytes | up | 5 |
| `RF-txpower` | tx-power | **held** | 0.090 → 0.917 | 0.827 | 0.065 → 0.794 | 11x advert_bytes | down | 4 |
| `MS-siting` | siting-mix | **text** | 0.149 → 0.964 | 0.814 | 0.142 → 0.962 | 3x sr_airtime | up | 4 |
| `MS-stretch` | stretch | **held** | 0.118 → 0.917 | 0.798 | 0.090 → 0.794 | 8.4x sr_bytes | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.102 → 0.847 | 0.745 | 0.087 → 0.721 | 1.3e+02x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **held** | 0.117 → 0.852 | 0.735 | 0.041 → 0.731 | 7.8x advert_bytes | down | 3 |
| `MS-density` | nodes | **held** | 0.349 → 0.998 | 0.649 | 0.579 → 0.947 | 35x sr_airtime | up | 5 |
| `RF-bw500` | preset | **held** | 0.270 → 0.901 | 0.631 | 0.158 → 0.728 | 3.5x advert_bytes | up | 3 |
| `RF-eu-presets` | preset | **text** | 0.289 → 0.803 | 0.514 | 0.282 → 0.794 | 2.1x advert_bytes | up | 4 |
| `RF-preset` | preset | **text** | 0.289 → 0.803 | 0.514 | 0.282 → 0.794 | 2.9x sr_airtime | up | 3 |
| `MS-hopscale` | nodes | **text** | 0.307 → 0.803 | 0.496 | 0.304 → 0.794 | 14x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **text** | 0.311 → 0.730 | 0.419 | 0.308 → 0.718 | 4.5x bytes_on_air | down | 3 |
| `MS-topology` | topology | **text** | 0.513 → 0.927 | 0.414 | 0.488 → 0.925 | 1.9x sr_airtime | up | 4 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.379 → 0.719 | 0.340 | 0.363 → 0.696 | 1.6x sr_airtime | up | 2 |
| `DG-burst` | burst-loss | **text** | 0.474 → 0.803 | 0.328 | 0.450 → 0.794 | 2.3x sr_bytes | down | 4 |
| `DG-outage` | burst-loss | **text** | 0.477 → 0.803 | 0.325 | 0.458 → 0.794 | 2.2x sr_bytes | down | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.510 → 0.834 | 0.324 | 0.495 → 0.827 | 8.7x sr_airtime | down | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.574 → 0.883 | 0.309 | 0.563 → 0.880 | 8.3x sr_airtime | down | 3 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.469 → 0.777 | 0.308 | 0.294 → 0.482 | 5.2x sr_airtime | up | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.602 → 0.899 | 0.297 | 0.578 → 0.898 | 1.9x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.602 → 0.865 | 0.263 | 0.578 → 0.861 | 1.6x sr_bytes | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.723 → 0.942 | 0.220 | 0.702 → 0.936 | 3.8x sr_airtime | down | 2 |
| `RT-spread` | hop-spread | **text** | 0.602 → 0.803 | 0.201 | 0.578 → 0.794 | 1.4x sr_bytes | up | 2 |
| `RF-noise` | noise-profile | **text** | 0.614 → 0.803 | 0.189 | 0.605 → 0.794 | 1.4x sr_airtime | down | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.799 → 0.969 | 0.169 | 0.785 → 0.794 | 2.8x sr_bytes | down | 5 |
| `DG-loss` | extra-loss | **text** | 0.642 → 0.803 | 0.160 | 0.627 → 0.794 | 1.6x sr_bytes | down | 4 |
| `SC-signing` | signature-policy | **text** | 0.653 → 0.803 | 0.150 | 0.653 → 0.794 | 1.3x sr_airtime | down | 3 |
| `MS-size` | nodes | **text** | 0.656 → 0.803 | 0.147 | 0.646 → 0.794 | 5.6x sr_bytes | down | 5 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.803 → 0.927 | 0.125 | 0.794 → 0.924 | 1.3x bytes_on_air | up | 3 |
| `AD-amplify-worst` | amplify-worst | **held** | 0.876 → 0.993 | 0.117 | 0.794 → 0.911 | 1.7x sr_bytes | up | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.742 → 0.854 | 0.112 | 0.738 → 0.852 | 2.2x sr_airtime | up | 4 |
| `AD-flooding` | role-mix | **text** | 0.737 → 0.846 | 0.109 | 0.731 → 0.840 | 2.2x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.737 → 0.846 | 0.109 | 0.731 → 0.840 | 2.2x bytes_on_air | up | 3 |
| `SF-place-flat` | place | **held** | 0.840 → 0.946 | 0.106 | 0.785 → 0.794 | 3.3x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.840 → 0.946 | 0.106 | 0.785 → 0.794 | 3.3x sr_bytes | up | 6 |
| `FW-mixed-26` | legacy-fraction | **held** | 0.863 → 0.969 | 0.106 | 0.754 → 0.853 | 2.2x bytes_on_air | up | 4 |
| `MS-roles` | role-mix | **text** | 0.737 → 0.841 | 0.104 | 0.731 → 0.836 | 1.1x bytes_on_air | down | 2 |
| `LD-interval` | broadcast-interval-s | **text** | 0.754 → 0.855 | 0.101 | 0.743 → 0.850 | 5.5x sr_airtime | up | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.803 → 0.901 | 0.098 | 0.794 → 0.895 | 1.4x bytes_on_air | up | 3 |
| `DB-platform` | platform-mix | **text** | 0.756 → 0.854 | 0.097 | 0.753 → 0.852 | 2.1x sr_airtime | down | 3 |
| `FW-mixed` | legacy-fraction | **text** | 0.777 → 0.871 | 0.094 | 0.771 → 0.866 | 2.1x bytes_on_air | up | 4 |
| `MS-roles-fav` | role-mix | **held** | 0.851 → 0.938 | 0.087 | 0.766 → 0.852 | 1.1x sr_airtime | down | 2 |
| `FW-versions` | profile | **text** | 0.803 → 0.877 | 0.075 | 0.794 → 0.872 | 3.2x bytes_on_air | down | 5 |
| `AD-badrouters` | role-placement | **text** | 0.670 → 0.737 | 0.067 | 0.652 → 0.731 | 1.1x sr_bytes | down | 3 |
| `FW-firmware` | profile | **text** | 0.803 → 0.869 | 0.067 | 0.794 → 0.858 | 3.2x bytes_on_air | down | 2 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.852 → 0.917 | 0.065 | 0.791 → 0.794 | 24x sr_airtime | down | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.654 → 0.718 | 0.064 | 0.633 → 0.696 | 1.3x sr_airtime | down | 2 |
| `SF-hops-flat` | hops-apart | **held** | 0.915 → 0.969 | 0.054 | 0.785 → 0.794 | 2.8x sr_bytes | up | 4 |
| `SF-cadence` | trigger | **held** | 0.870 → 0.917 | 0.047 | 0.764 → 0.794 | 14x advert_bytes | down | 4 |
| `TH-congestion-input` | congestion-input | **held** | 0.763 → 0.807 | 0.044 | 0.480 → 0.516 | 1.5x sr_airtime | up | 2 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.760 → 0.803 | 0.042 | 0.750 → 0.794 | 1.5x sr_airtime | down | 4 |
| `MS-router-late` | router-late-fraction | **held** | 0.876 → 0.917 | 0.041 | 0.782 → 0.796 | 1.4x sr_bytes | down | 4 |
| `AD-worst` | role-placement | **text** | 0.723 → 0.762 | 0.039 | 0.711 → 0.755 | 1.1x sr_bytes | down | 2 |
| `FW-signing-cost` | profile-flag | **held** | 0.917 → 0.953 | 0.036 | 0.794 → 0.831 | 3.3x bytes_on_air | down | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.804 → 0.829 | 0.024 | 0.797 → 0.825 | 1.2x sr_bytes | up | 2 |
| `LD-diurnal` | diurnal | **text** | 0.803 → 0.826 | 0.024 | 0.794 → 0.820 | 1.3x sr_bytes | down | 3 |
| `SF-sr-retries` | sr-retries | **held** | 0.923 → 0.947 | 0.023 | 0.796 → 0.801 | 1.2x sr_bytes | down | 4 |
| `DM-mode` | dm-mode | **text** | 0.746 → 0.769 | 0.023 | 0.746 → 0.769 | 1.2x sr_airtime | up | 3 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.907 → 0.930 | 0.023 | 0.781 → 0.795 | 1.2x sr_bytes | up | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.907 → 0.930 | 0.023 | 0.781 → 0.795 | 1.2x sr_bytes | up | 4 |
| `SF-catchup` | catch-up-hours | **text** | 0.774 → 0.794 | 0.020 | 0.764 → 0.788 | 9.3x advert_bytes | up | 3 |
| `SF-window-size` | window-size | **held** | 0.905 → 0.923 | 0.018 | 0.778 → 0.793 | 5.5x advert_bytes | up | 3 |
| `SF-servers-flat` | servers | **text** | 0.787 → 0.803 | 0.016 | 0.772 → 0.794 | 7.4x sr_bytes | down | 4 |
| `SF-servers-spread` | servers | **text** | 0.787 → 0.803 | 0.016 | 0.772 → 0.794 | 7.4x sr_bytes | down | 4 |
| `SF-advert-transport` | advert-transport | **held** | 0.902 → 0.917 | 0.015 | 0.787 → 0.794 | 2.9x sr_airtime | down | 2 |
| `SF-width` | short-id-bits | **held** | 0.912 → 0.927 | 0.015 | 0.783 → 0.796 | 3.1x advert_bytes | up | 4 |
| `SF-capacity` | capacity | **held** | 0.911 → 0.925 | 0.014 | 0.788 → 0.794 | 5.3x advert_bytes | down | 5 |
| `SF-capacity-local` | capacity | **held** | 0.911 → 0.925 | 0.014 | 0.788 → 0.794 | 5.3x advert_bytes | down | 5 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.911 → 0.923 | 0.013 | 0.782 → 0.794 | 3.3x advert_bytes | up | 4 |
| `SF-servers-allrouters` | servers | **held** | 0.936 → 0.945 | 0.009 | 0.784 → 0.787 | 2.4x sr_bytes | up | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.933 → 0.942 | 0.009 | 0.927 → 0.936 | 1.2x sr_airtime | down | 2 |
| `RT-hopassign` | hop-assign | **text** | 0.795 → 0.803 | 0.008 | 0.786 → 0.794 | 1.2x sr_airtime | down | 2 |
| `SF-provide-transport` | provide-transport | **held** | 0.910 → 0.917 | 0.007 | 0.780 → 0.794 | 2.3x sr_airtime | down | 2 |
| `SF-resolve` | resolve | **text** | 0.796 → 0.803 | 0.006 | 0.785 → 0.794 | 5.7x advert_bytes | = | 3 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.761 → 0.767 | 0.006 | 0.761 → 0.767 | 1.1x sr_airtime | down | 2 |
| `SF-capacity-window` | capacity | **held** | 0.923 → 0.929 | 0.006 | 0.792 → 0.795 | 2.1x advert_bytes | down | 3 |
| `PR-repeats` | extra-repeats | **held** | 0.917 → 0.921 | 0.005 | 0.794 → 0.799 | 1.1x sr_bytes | up | 2 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.915 → 0.919 | 0.005 | 0.786 → 0.790 | 5.7x advert_bytes | up | 3 |
| `SF-replay-order` | replay-ordering | **held** | 0.917 → 0.920 | 0.003 | 0.793 → 0.794 | 1.1x sr_bytes | up | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.802 → 0.804 | 0.003 | 0.780 → 0.783 | 1.1x sr_bytes | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.942 → 0.945 | 0.003 | 0.936 → 0.940 | 1.1x sr_airtime | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.942 → 0.944 | 0.002 | 0.936 → 0.938 | 1.1x sr_bytes | up | 2 |

### Moved no delivery measure

Not the same as having done nothing: several arms hold delivery flat by design and differ in what they spend. Three ways of reconciling the same two sets had better agree on what is held; where they differ is the price.

| block | arm | price | cells |
| --- | --- | --- | --: |
| `DB-warm` | warm-num-nodes | - | 4 |
| `PR-dmmode-cr` | dm-mode | - | 2 |
| `SF-signed` | signed | 1.4x advert_bytes | 2 |

## Every block

### `AD-amplifiers` - amplifier-mix  `--scenario alpine`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| sprinkled | 1 | 0.913 | 0.909 | 0.005 | - | - | 0.961 | 0.961 | 0.711 | 1.18x | 17.4/23.2/27.6% | 1.7/5.1% | 3 |
| arms-race | 1 | 0.927 | 0.924 | 0.003 | - | - | 0.964 | 0.965 | 0.576 | 1.12x | 18.1/24.8/28.7% | 1.3/5.2% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario alpine`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 0.1 | 1 | 0.881 | 0.866 | 0.015 | - | - | 0.876 | 0.876 | 0.517 | 1.36x | 17.0/23.0/26.4% | 2.2/5.2% | 3 |
| 0.3 | 1 | 0.919 | 0.911 | 0.008 | - | - | 0.993 | 0.996 | 0.730 | 1.17x | 16.8/23.7/28.8% | 1.7/5.2% | 3 |

### `AD-badrouters` - role-placement  `--scenario alpine`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.737 | 0.731 | 0.006 | - | - | 0.852 | 0.854 | 0.320 | 1.21x | 15.4/21.4/24.4% | 2.1/5.2% | 3 |
| inverse | 1 | 0.670 | 0.652 | 0.018 | - | - | 0.815 | 0.818 | 0.327 | 1.10x | 11.2/17.3/19.7% | 2.0/3.8% | 3 |
| random | 1 | 0.737 | 0.727 | 0.010 | - | - | 0.869 | 0.870 | 0.418 | 1.12x | 12.4/17.2/20.6% | 1.8/4.4% | 3 |

### `AD-flooding` - role-mix  `--scenario alpine`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.737 | 0.731 | 0.006 | - | - | 0.852 | 0.854 | 0.320 | 1.21x | 15.4/21.4/24.4% | 2.1/5.2% | 3 |
| all-routers | 1 | 0.846 | 0.840 | 0.006 | - | - | 0.937 | 0.937 | 0.541 | 2.66x | 29.4/38.9/42.3% | 4.6/5.3% | 3 |

### `AD-nomute` - role-mix  `--scenario alpine`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.737 | 0.731 | 0.006 | - | - | 0.852 | 0.854 | 0.320 | 1.21x | 15.4/21.4/24.4% | 2.1/5.2% | 3 |
| no-mute | 1 | 0.806 | 0.801 | 0.005 | - | - | 0.916 | 0.917 | 0.464 | 1.37x | 15.5/22.1/25.9% | 2.1/5.1% | 3 |
| all-routers | 1 | 0.846 | 0.840 | 0.006 | - | - | 0.937 | 0.937 | 0.541 | 2.66x | 29.4/38.9/42.3% | 4.6/5.3% | 3 |

### `AD-siting` - siting-mix  `--scenario alpine`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.737 | 0.731 | 0.006 | - | - | 0.852 | 0.854 | 0.320 | 1.21x | 15.4/21.4/24.4% | 2.1/5.2% | 3 |
| local-typical | 1 | 0.551 | 0.542 | 0.008 | - | - | 0.765 | 0.766 | 0.000 | 1.17x | 11.2/23.7/27.5% | 1.7/5.3% | 3 |
| basement-heavy | 1 | 0.041 | 0.041 | 0.001 | - | - | 0.117 | 0.119 | 0.000 | 0.42x | 0.8/4.3/6.6% | 0.5/2.3% | 3 |

### `AD-worst` - role-placement  `--scenario alpine`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.762 | 0.755 | 0.007 | - | - | 0.919 | 0.920 | 0.000 | 2.40x | 13.9/27.4/37.2% | 1.9/5.6% | 3 |
| inverse | 1 | 0.723 | 0.711 | 0.012 | - | - | 0.918 | 0.918 | 0.000 | 2.27x | 12.7/23.0/34.0% | 1.8/3.6% | 3 |

### `BL-control` - protocol  `--scenario alpine`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.791 | 0.791 | 0.000 | - | - | 0 | 0.000 | 0.464 | 1.38x | 16.0/22.0/25.6% | 2.0/5.4% | 3 |
| sr | 1 | 0.811 | 0.790 | 0.021 | - | - | 0.915 | 0.920 | 0.457 | 1.40x | 16.3/22.8/26.1% | 2.0/5.4% | 3 |

### `DB-hotstore` - max-num-nodes  `--scenario alpine`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.742 | 0.738 | 0.004 | - | - | 0.824 | 0.825 | 0.509 | 3.12x | 36.1/51.1/58.1% | 4.4/10.4% | 3 |
| 100 | 1 | 0.854 | 0.852 | 0.002 | - | - | 0.921 | 0.922 | 0.609 | 1.62x | 18.7/27.2/31.8% | 2.2/5.3% | 3 |
| 120 | 1 | 0.854 | 0.852 | 0.002 | - | - | 0.921 | 0.922 | 0.609 | 1.62x | 18.7/27.2/31.8% | 2.2/5.3% | 3 |
| 250 | 1 | 0.854 | 0.852 | 0.002 | - | - | 0.921 | 0.922 | 0.609 | 1.62x | 18.7/27.2/31.8% | 2.2/5.3% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario alpine`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.299 | 0.294 | 0.005 | - | - | 0.469 | 0.523 | 0.100 | 11.16x | 37.0/62.6/76.9% | 3.8/11.0% | 3 |
| 120 | 1 | 0.489 | 0.480 | 0.009 | - | - | 0.763 | 0.774 | 0.133 | 4.63x | 14.8/33.1/46.8% | 1.5/5.5% | 3 |
| 250 | 1 | 0.493 | 0.482 | 0.011 | - | - | 0.777 | 0.789 | 0.128 | 4.55x | 14.7/32.0/45.1% | 1.5/5.3% | 3 |

> max-num-nodes=10: decode_failures 48

> max-num-nodes=120: decode_failures 56

> max-num-nodes=250: decode_failures 42

### `DB-platform` - platform-mix  `--scenario alpine`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.854 | 0.852 | 0.002 | - | - | 0.921 | 0.922 | 0.609 | 1.62x | 18.7/27.2/31.8% | 2.2/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.854 | 0.852 | 0.002 | - | - | 0.921 | 0.922 | 0.609 | 1.62x | 18.7/27.2/31.8% | 2.2/5.3% | 3 |
| constrained | 1 | 0.756 | 0.753 | 0.004 | - | - | 0.830 | 0.830 | 0.525 | 3.12x | 36.1/51.1/58.3% | 4.4/10.4% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario alpine`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.718 | 0.696 | 0.023 | - | - | 0.855 | 0.861 | 0.504 | 5.64x | 51.7/70.8/75.5% | 3.6/11.8% | 3 |
| 25 | 1 | 0.718 | 0.696 | 0.023 | - | - | 0.855 | 0.861 | 0.504 | 5.64x | 51.7/70.8/75.5% | 3.6/11.8% | 3 |
| 100 | 1 | 0.718 | 0.696 | 0.023 | - | - | 0.855 | 0.861 | 0.504 | 5.64x | 51.7/70.8/75.5% | 3.6/11.8% | 3 |
| 2000 | 1 | 0.718 | 0.696 | 0.023 | - | - | 0.855 | 0.861 | 0.504 | 5.64x | 51.7/70.8/75.5% | 3.6/11.8% | 3 |

> warm-num-nodes=0: decode_failures 78

> warm-num-nodes=25: decode_failures 78

> warm-num-nodes=100: decode_failures 78

> warm-num-nodes=2000: decode_failures 78

### `DG-burst` - burst-loss  `--scenario alpine`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 0.1 | 1 | 0.692 | 0.675 | 0.016 | - | - | 0.875 | 0.881 | 0.353 | 1.29x | 15.2/21.0/25.0% | 1.9/4.9% | 3 |
| 0.2 | 1 | 0.595 | 0.573 | 0.022 | - | - | 0.828 | 0.832 | 0.245 | 1.20x | 14.4/19.8/24.1% | 1.7/4.4% | 3 |
| 0.3 | 1 | 0.474 | 0.450 | 0.024 | - | - | 0.689 | 0.748 | 0.156 | 1.07x | 13.2/18.5/22.2% | 1.6/3.8% | 3 |

> burst-loss=0.1: decode_failures 25

> burst-loss=0.2: decode_failures 5

> burst-loss=0.3: decode_failures 28

### `DG-loss` - extra-loss  `--scenario alpine`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 0.1 | 1 | 0.760 | 0.750 | 0.010 | - | - | 0.901 | 0.902 | 0.405 | 1.41x | 16.5/22.9/26.7% | 2.1/5.2% | 3 |
| 0.2 | 1 | 0.697 | 0.686 | 0.011 | - | - | 0.864 | 0.865 | 0.313 | 1.45x | 17.3/23.8/28.2% | 2.2/5.1% | 3 |
| 0.3 | 1 | 0.642 | 0.627 | 0.015 | - | - | 0.825 | 0.825 | 0.253 | 1.44x | 17.4/24.1/28.8% | 2.2/4.8% | 3 |

### `DG-outage` - burst-loss  `--scenario alpine`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 0.1 | 1 | 0.684 | 0.672 | 0.013 | - | - | 0.846 | 0.869 | 0.329 | 1.30x | 15.3/21.0/25.0% | 1.9/4.7% | 3 |
| 0.2 | 1 | 0.575 | 0.560 | 0.015 | - | - | 0.745 | 0.817 | 0.248 | 1.20x | 14.3/20.0/24.2% | 1.7/4.6% | 3 |
| 0.3 | 1 | 0.477 | 0.458 | 0.019 | - | - | 0.665 | 0.771 | 0.133 | 1.14x | 13.9/19.1/23.4% | 1.6/4.4% | 3 |

> burst-loss=0.1: decode_failures 36

> burst-loss=0.2: decode_failures 30

> burst-loss=0.3: decode_failures 35

### `DM-mode` - dm-mode  `--scenario alpine`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.746 | 0.746 | 0.000 | - | - | 0.882 | 0.884 | 0.437 | 1.79x | 20.9/29.2/34.1% | 2.6/6.9% | 3 |
| directed-with-late-flood | 1 | 0.767 | 0.767 | 0.000 | - | - | 0.900 | 0.900 | 0.455 | 1.63x | 19.0/26.8/31.2% | 2.3/6.4% | 3 |
| m4-early-flood | 1 | 0.769 | 0.769 | 0.000 | - | - | 0.905 | 0.905 | 0.454 | 1.65x | 19.2/27.1/31.5% | 2.4/6.5% | 3 |

### `FW-firmware` - profile  `--scenario alpine`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.869 | 0.858 | 0.011 | - | - | 0.979 | 0.979 | 0.608 | 0.80x | 9.1/11.8/14.5% | 1.3/2.0% | 3 |
| 2.8 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario alpine`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 0.25 | 1 | 0.777 | 0.771 | 0.006 | - | - | 0.879 | 0.892 | 0.415 | 1.20x | 14.5/20.4/25.7% | 1.8/4.9% | 3 |
| 0.5 | 1 | 0.816 | 0.808 | 0.008 | - | - | 0.939 | 0.942 | 0.328 | 1.09x | 12.7/16.8/20.1% | 1.7/4.1% | 3 |
| 0.75 | 1 | 0.871 | 0.866 | 0.005 | - | - | 0.964 | 0.966 | 0.417 | 0.94x | 11.1/15.5/18.7% | 1.5/3.8% | 3 |

> legacy-fraction=0.25: decode_failures 32

> slower: 4.11 s per simulated hour against 1.68 over 14 prior run(s) - 2.4x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-mixed-26` - legacy-fraction  `--scenario alpine`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 0.25 | 1 | 0.761 | 0.754 | 0.007 | - | - | 0.863 | 0.879 | 0.388 | 1.16x | 13.9/20.0/25.2% | 1.8/4.8% | 3 |
| 0.5 | 1 | 0.812 | 0.804 | 0.008 | - | - | 0.931 | 0.931 | 0.324 | 1.07x | 12.4/16.8/20.1% | 1.7/4.1% | 3 |
| 0.75 | 1 | 0.860 | 0.853 | 0.007 | - | - | 0.969 | 0.971 | 0.435 | 0.89x | 10.5/15.1/18.4% | 1.3/3.9% | 3 |

> legacy-fraction=0.25: decode_failures 32

> slower: 3.68 s per simulated hour against 1.71 over 14 prior run(s) - 2.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `FW-signing-cost` - profile-flag  `--scenario alpine`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.838 | 0.831 | 0.007 | - | - | 0.953 | 0.953 | 0.501 | 0.75x | 9.0/12.7/15.1% | 1.1/3.1% | 3 |
| signing=true | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |

### `FW-versions` - profile  `--scenario alpine`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.859 | 0.848 | 0.011 | - | - | 0.971 | 0.975 | 0.549 | 0.79x | 9.4/12.5/16.1% | 1.3/2.6% | 3 |
| 2.5 | 1 | 0.860 | 0.850 | 0.010 | - | - | 0.975 | 0.977 | 0.527 | 0.80x | 9.5/12.5/16.0% | 1.4/2.5% | 3 |
| 2.6 | 1 | 0.857 | 0.845 | 0.012 | - | - | 0.971 | 0.973 | 0.520 | 0.77x | 9.4/12.6/16.3% | 1.3/2.6% | 3 |
| 2.7 | 1 | 0.877 | 0.872 | 0.005 | - | - | 0.978 | 0.978 | 0.546 | 0.79x | 9.9/13.8/17.0% | 1.3/3.0% | 3 |
| 2.8 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.834 | 0.827 | 0.007 | - | - | 0.944 | 0.946 | 0.517 | 0.90x | 10.3/14.1/16.5% | 1.3/3.4% | 3 |
| 900 | 1 | 0.754 | 0.743 | 0.011 | - | - | 0.884 | 0.886 | 0.430 | 2.18x | 25.1/35.0/40.4% | 3.1/8.4% | 3 |
| 300 | 1 | 0.510 | 0.495 | 0.015 | - | - | 0.643 | 0.643 | 0.245 | 4.79x | 50.8/67.7/74.4% | 7.6/17.4% | 3 |

### `LD-chatty-hops` - broadcast-interval-s  `--scenario alpine`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.883 | 0.880 | 0.003 | - | - | 0.952 | 0.952 | 0.624 | 1.03x | 11.5/15.1/17.4% | 1.5/3.5% | 3 |
| 900 | 1 | 0.823 | 0.818 | 0.006 | - | - | 0.904 | 0.905 | 0.582 | 2.52x | 28.0/37.3/42.8% | 3.7/8.7% | 3 |
| 300 | 1 | 0.574 | 0.563 | 0.011 | - | - | 0.684 | 0.685 | 0.315 | 5.36x | 55.6/70.3/76.7% | 8.3/18.1% | 3 |

### `LD-diurnal` - diurnal  `--scenario alpine`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.826 | 0.820 | 0.006 | - | - | 0.936 | 0.937 | 0.500 | 1.32x | 15.2/20.9/24.5% | 1.9/5.1% | 3 |
| sinusoid | 1 | 0.810 | 0.803 | 0.007 | - | - | 0.931 | 0.932 | 0.463 | 1.27x | 14.6/19.9/23.4% | 1.8/4.8% | 3 |
| commuter | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario alpine`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.754 | 0.743 | 0.011 | - | - | 0.884 | 0.886 | 0.430 | 2.18x | 25.1/35.0/40.4% | 3.1/8.4% | 3 |
| 3600 | 1 | 0.834 | 0.827 | 0.007 | - | - | 0.944 | 0.946 | 0.517 | 0.90x | 10.3/14.1/16.5% | 1.3/3.4% | 3 |
| 10800 | 1 | 0.843 | 0.839 | 0.004 | - | - | 0.947 | 0.949 | 0.528 | 0.60x | 7.0/9.4/11.1% | 0.9/2.3% | 3 |
| 43200 | 1 | 0.855 | 0.850 | 0.005 | - | - | 0.962 | 0.962 | 0.530 | 0.43x | 5.0/6.7/8.0% | 0.6/1.7% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario alpine`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 0.25 | 1 | 0.791 | 0.784 | 0.007 | - | - | 0.908 | 0.909 | 0.464 | 1.45x | 16.7/23.2/27.0% | 2.1/5.6% | 3 |
| 1.0 | 1 | 0.784 | 0.774 | 0.009 | - | - | 0.910 | 0.911 | 0.468 | 1.59x | 18.5/25.7/30.0% | 2.3/6.3% | 3 |
| 4.0 | 1 | 0.760 | 0.750 | 0.010 | - | - | 0.889 | 0.891 | 0.425 | 1.98x | 23.1/32.9/38.0% | 2.9/8.0% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario alpine`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.718 | 0.696 | 0.023 | - | - | 0.855 | 0.861 | 0.504 | 5.64x | 51.7/70.8/75.5% | 3.6/11.8% | 3 |
| 1.0 | 1 | 0.654 | 0.633 | 0.021 | - | - | 0.799 | 0.808 | 0.448 | 6.23x | 56.3/73.7/78.1% | 4.1/13.2% | 3 |

> traceroute-per-hour=0.0: decode_failures 78

> traceroute-per-hour=1.0: queue drops 11.5% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 94

### `MS-density` - nodes  `--scenario alpine`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.579 | 0.579 | 0.000 | - | - | 0.349 | 0.698 | 0.000 | 1.22x | 15.6/22.2/25.1% | 2.9/6.5% | 2 |
| 60 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 90 | 1 | 0.912 | 0.907 | 0.004 | - | - | 0.983 | 0.983 | 0.689 | 1.54x | 16.5/22.8/26.4% | 1.4/4.7% | 3 |
| 120 | 1 | 0.942 | 0.936 | 0.006 | - | - | 0.994 | 0.995 | 0.764 | 2.01x | 19.9/30.7/33.6% | 1.3/5.1% | 3 |
| 150 | 1 | 0.949 | 0.947 | 0.003 | - | - | 0.998 | 0.998 | 0.796 | 2.71x | 27.2/41.1/45.7% | 1.4/5.7% | 3 |

> nodes=40: 3 archives requested, 2 placed - group on the placed count

### `MS-hopscale` - nodes  `--scenario alpine`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 120 | 1 | 0.736 | 0.724 | 0.012 | - | - | 0.893 | 0.893 | 0.381 | 2.28x | 13.8/30.0/36.4% | 1.5/5.4% | 3 |
| 250 | 1 | 0.488 | 0.479 | 0.009 | - | - | 0.743 | 0.767 | 0.126 | 5.01x | 16.1/36.0/50.6% | 1.6/6.1% | 3 |
| 500 | 1 | 0.307 | 0.304 | 0.003 | - | - | 0.486 | 0.550 | 0.065 | 9.90x | 19.7/30.4/41.1% | 1.7/5.8% | 3 |

> nodes=250: decode_failures 169

> nodes=500: decode_failures 140

### `MS-oversubscribed` - nodes  `--scenario alpine`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.730 | 0.718 | 0.011 | - | - | 0.887 | 0.887 | 0.378 | 2.06x | 12.7/27.3/33.0% | 1.4/4.8% | 3 |
| 250 | 1 | 0.489 | 0.480 | 0.009 | - | - | 0.763 | 0.774 | 0.133 | 4.63x | 14.8/33.1/46.8% | 1.5/5.5% | 3 |
| 500 | 1 | 0.311 | 0.308 | 0.003 | - | - | 0.488 | 0.552 | 0.070 | 9.22x | 18.5/28.1/38.4% | 1.5/5.3% | 3 |

> nodes=250: decode_failures 56

> nodes=500: decode_failures 101

### `MS-roles` - role-mix  `--scenario alpine`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.841 | 0.836 | 0.005 | - | - | 0.946 | 0.946 | 0.565 | 1.38x | 15.9/21.9/25.4% | 2.0/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.737 | 0.731 | 0.006 | - | - | 0.852 | 0.854 | 0.320 | 1.21x | 15.4/21.4/24.4% | 2.1/5.2% | 3 |

### `MS-roles-fav` - role-mix  `--scenario alpine`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.855 | 0.852 | 0.003 | - | - | 0.938 | 0.939 | 0.576 | 1.43x | 16.4/22.4/26.2% | 2.1/5.3% | 3 |
| baymesh-2026-08 | 1 | 0.769 | 0.766 | 0.003 | - | - | 0.851 | 0.854 | 0.442 | 1.35x | 17.6/23.8/27.5% | 2.3/5.2% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario alpine`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 0.05 | 1 | 0.804 | 0.796 | 0.007 | - | - | 0.906 | 0.908 | 0.457 | 1.51x | 18.0/25.7/31.6% | 2.1/5.5% | 3 |
| 0.1 | 1 | 0.797 | 0.793 | 0.004 | - | - | 0.880 | 0.880 | 0.511 | 1.58x | 18.8/28.1/33.3% | 2.1/5.2% | 3 |
| 0.2 | 1 | 0.788 | 0.782 | 0.006 | - | - | 0.876 | 0.877 | 0.450 | 1.74x | 22.9/32.5/35.2% | 2.4/5.1% | 3 |

### `MS-siting` - siting-mix  `--scenario alpine`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| local-typical | 1 | 0.617 | 0.606 | 0.011 | - | - | 0.849 | 0.851 | 0.000 | 1.31x | 12.1/24.5/26.5% | 1.9/5.5% | 3 |
| event | 1 | 0.149 | 0.142 | 0.007 | - | - | 0.418 | 0.445 | 0.000 | 1.09x | 3.4/16.5/22.2% | 1.1/5.5% | 3 |
| backbone | 1 | 0.964 | 0.962 | 0.002 | - | - | 0.996 | 0.997 | 0.673 | 1.18x | 22.3/31.3/33.4% | 1.6/5.6% | 3 |

> siting-mix=event: decode_failures 10

### `MS-size` - nodes  `--scenario alpine`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.760 | 0.745 | 0.015 | - | - | 0.863 | 0.863 | 0.553 | 1.41x | 22.0/29.9/33.8% | 3.2/7.2% | 3 |
| 60 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 90 | 1 | 0.799 | 0.785 | 0.013 | - | - | 0.968 | 0.977 | 0.483 | 1.69x | 14.7/22.3/27.1% | 1.6/5.4% | 3 |
| 120 | 1 | 0.736 | 0.724 | 0.012 | - | - | 0.893 | 0.893 | 0.381 | 2.28x | 13.8/30.0/36.4% | 1.5/5.4% | 3 |
| 150 | 1 | 0.656 | 0.646 | 0.010 | - | - | 0.862 | 0.863 | 0.133 | 2.90x | 14.5/32.4/40.7% | 1.5/5.5% | 3 |

> nodes=90: decode_failures 7

### `MS-stretch` - stretch  `--scenario alpine`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 1.25 | 1 | 0.584 | 0.575 | 0.009 | - | - | 0.833 | 0.836 | 0.000 | 1.34x | 13.3/20.2/22.3% | 1.9/4.7% | 3 |
| 1.5 | 1 | 0.379 | 0.363 | 0.016 | - | - | 0.529 | 0.603 | 0.032 | 1.27x | 9.7/15.6/19.8% | 2.1/4.2% | 3 |
| 2.0 | 1 | 0.091 | 0.090 | 0.001 | - | - | 0.118 | 0.120 | 0.000 | 0.76x | 3.0/8.8/14.0% | 1.2/3.5% | 3 |

> stretch=1.5: decode_failures 30

### `MS-topology` - topology  `--scenario alpine`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| clustered | 1 | 0.513 | 0.488 | 0.025 | - | - | 0.575 | 0.944 | 0.130 | 1.06x | 15.9/27.0/28.5% | 1.4/4.8% | 3 |
| corridor | 1 | 0.689 | 0.680 | 0.009 | - | - | 0.899 | 0.902 | 0.289 | 1.34x | 15.2/28.5/31.3% | 1.9/5.4% | 3 |
| hub | 1 | 0.927 | 0.925 | 0.002 | - | - | 0.961 | 0.963 | 0.693 | 1.18x | 25.9/35.3/36.5% | 1.5/5.6% | 3 |

> topology=clustered: decode_failures 16

### `PR-crladder` - coding-rate-ladder  `--scenario alpine`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.767 | 0.767 | 0.000 | - | - | 0.900 | 0.900 | 0.455 | 1.63x | 19.0/26.8/31.2% | 2.3/6.4% | 3 |
| True | 1 | 0.761 | 0.761 | 0.000 | - | - | 0.896 | 0.896 | 0.453 | 1.68x | 19.6/27.6/32.0% | 2.4/6.6% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario alpine`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.761 | 0.761 | 0.000 | - | - | 0.896 | 0.896 | 0.453 | 1.68x | 19.6/27.6/32.0% | 2.4/6.6% | 3 |
| m4-early-flood | 1 | 0.761 | 0.761 | 0.000 | - | - | 0.896 | 0.896 | 0.453 | 1.68x | 19.6/27.6/32.0% | 2.4/6.6% | 3 |

> inert: every value of `dm-mode` produced identical numbers - either the flag is not read, or it needs a second flag before it does anything (README §10.4)

### `PR-protocol` - protocol  `--scenario alpine`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.791 | 0.791 | 0.000 | - | - | 0 | 0.000 | 0.464 | 1.38x | 16.0/22.0/25.6% | 2.0/5.4% | 3 |
| chain | 1 | 0.785 | 0.782 | 0.003 | - | - | 0.872 | 0.913 | 0.476 | 1.56x | 18.2/25.3/29.4% | 2.3/6.1% | 3 |
| sr | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |

### `PR-repeats` - extra-repeats  `--scenario alpine`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| True | 1 | 0.806 | 0.799 | 0.007 | - | - | 0.921 | 0.924 | 0.491 | 1.40x | 16.1/22.4/26.0% | 2.1/5.4% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario alpine`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.942 | 0.936 | 0.006 | - | - | 0.994 | 0.995 | 0.764 | 2.01x | 19.9/30.7/33.6% | 1.3/5.1% | 3 |
| True | 1 | 0.944 | 0.938 | 0.006 | - | - | 0.993 | 0.994 | 0.775 | 2.06x | 20.2/31.1/34.0% | 1.3/5.0% | 3 |

### `RF-bw500` - preset  `--scenario alpine`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.159 | 0.158 | 0.001 | - | - | 0.270 | 0.291 | 0.000 | 0.04x | 0.2/0.5/0.8% | 0.1/0.2% | 3 |
| MEDIUM_TURBO | 1 | 0.402 | 0.389 | 0.013 | - | - | 0.562 | 0.580 | 0.033 | 0.25x | 1.9/3.7/4.6% | 0.3/1.1% | 3 |
| LONG_TURBO | 1 | 0.739 | 0.728 | 0.011 | - | - | 0.901 | 0.901 | 0.208 | 1.35x | 14.1/20.7/23.4% | 2.0/4.9% | 3 |

> preset=SHORT_TURBO: decode_failures 5

> preset=MEDIUM_TURBO: decode_failures 5

### `RF-duct` - duct-per-hour  `--scenario alpine`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 0.25 | 1 | 0.837 | 0.829 | 0.008 | - | - | 0.940 | 0.942 | 0.536 | 1.29x | 17.7/23.5/27.0% | 1.8/5.4% | 3 |
| 1.0 | 1 | 0.901 | 0.895 | 0.006 | - | - | 0.957 | 0.957 | 0.732 | 1.03x | 20.9/26.7/29.1% | 1.3/5.3% | 3 |

### `RF-eu-presets` - preset  `--scenario alpine`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.289 | 0.282 | 0.007 | - | - | 0.453 | 0.457 | 0.000 | 0.14x | 1.0/1.8/2.1% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| LITE_FAST | 1 | 0.752 | 0.745 | 0.006 | - | - | 0.918 | 0.919 | 0.222 | 1.04x | 11.6/17.7/20.1% | 1.5/4.1% | 3 |
| NARROW_SLOW | 1 | 0.754 | 0.745 | 0.009 | - | - | 0.908 | 0.910 | 0.303 | 1.31x | 14.5/22.0/24.7% | 1.9/5.2% | 3 |

### `RF-noise` - noise-profile  `--scenario alpine`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| temporal | 1 | 0.722 | 0.712 | 0.010 | - | - | 0.874 | 0.875 | 0.341 | 1.41x | 16.8/23.0/26.5% | 2.1/5.3% | 3 |
| transient | 1 | 0.793 | 0.783 | 0.010 | - | - | 0.919 | 0.920 | 0.451 | 1.37x | 15.8/22.1/25.6% | 2.0/5.3% | 3 |
| periodic | 1 | 0.614 | 0.605 | 0.009 | - | - | 0.742 | 0.744 | 0.279 | 1.25x | 14.8/20.4/23.8% | 1.8/4.6% | 3 |

### `RF-preset` - preset  `--scenario alpine`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.289 | 0.282 | 0.007 | - | - | 0.453 | 0.457 | 0.000 | 0.14x | 1.0/1.8/2.1% | 0.2/0.6% | 3 |
| LONG_FAST | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| LONG_MODERATE | 1 | 0.770 | 0.751 | 0.019 | - | - | 0.870 | 0.870 | 0.431 | 3.42x | 45.8/57.1/61.5% | 4.8/12.3% | 3 |

### `RF-preset-turbo` - preset  `--scenario alpine`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.034 | 0.034 | 0.000 | - | - | 0.033 | 0.036 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.159 | 0.158 | 0.001 | - | - | 0.270 | 0.291 | 0.000 | 0.04x | 0.2/0.5/0.8% | 0.1/0.2% | 3 |
| LONG_FAST | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| LONG_TURBO | 1 | 0.739 | 0.728 | 0.011 | - | - | 0.901 | 0.901 | 0.208 | 1.35x | 14.1/20.7/23.4% | 2.0/4.9% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.749 | 0.736 | 0.013 | - | - | 0.885 | 0.886 | 0.398 | 1.90x | 20.6/29.3/32.2% | 2.8/7.1% | 3 |

> preset=SHORT_TURBO: decode_failures 5

### `RF-pulse` - noise-pulse-interval-ms  `--scenario alpine`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.728 | 0.721 | 0.007 | - | - | 0.847 | 0.848 | 0.387 | 1.34x | 15.8/21.6/25.2% | 1.9/5.1% | 3 |
| 10000 | 1 | 0.614 | 0.605 | 0.009 | - | - | 0.742 | 0.744 | 0.279 | 1.25x | 14.8/20.4/23.8% | 1.8/4.6% | 3 |
| 4000 | 1 | 0.391 | 0.388 | 0.003 | - | - | 0.467 | 0.516 | 0.141 | 1.09x | 13.1/18.3/21.7% | 1.6/3.7% | 3 |
| 2000 | 1 | 0.087 | 0.087 | 0.000 | - | - | 0.102 | 0.138 | 0.020 | 0.70x | 8.8/12.2/15.7% | 1.1/2.0% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 8

### `RF-stretch-duct` - duct-per-hour  `--scenario alpine`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.379 | 0.363 | 0.016 | - | - | 0.529 | 0.603 | 0.032 | 1.27x | 9.7/15.6/19.8% | 2.1/4.2% | 3 |
| 1.0 | 1 | 0.719 | 0.696 | 0.023 | - | - | 0.784 | 0.816 | 0.509 | 1.08x | 14.5/20.1/22.5% | 1.5/4.5% | 3 |

> duct-per-hour=0.0: decode_failures 30

> duct-per-hour=1.0: decode_failures 28

> slower: 6.11 s per simulated hour against 2.43 over 14 prior run(s) - 2.5x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `RF-txpower` - tx-power  `--scenario alpine`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 22 | 1 | 0.382 | 0.366 | 0.016 | - | - | 0.568 | 0.572 | 0.030 | 1.28x | 9.1/16.4/22.1% | 1.9/4.8% | 3 |
| 17 | 1 | 0.149 | 0.146 | 0.004 | - | - | 0.319 | 0.349 | 0.000 | 0.97x | 4.9/10.2/15.0% | 1.4/3.6% | 3 |
| 14 | 1 | 0.066 | 0.065 | 0.001 | - | - | 0.090 | 0.141 | 0.000 | 0.57x | 2.2/5.0/8.3% | 0.8/2.7% | 3 |

> tx-power=17: decode_failures 3

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario alpine`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.942 | 0.936 | 0.006 | - | - | 0.994 | 0.995 | 0.764 | 2.01x | 19.9/30.7/33.6% | 1.3/5.1% | 3 |
| True | 1 | 0.933 | 0.927 | 0.006 | - | - | 0.991 | 0.991 | 0.750 | 2.34x | 22.8/33.9/36.8% | 1.5/5.6% | 3 |

> no-adopt-hop-recommendation=True: misdecodes 1

### `RT-favourites` - favourite-routers  `--scenario alpine`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.804 | 0.797 | 0.007 | - | - | 0.919 | 0.920 | 0.456 | 1.44x | 17.5/23.7/28.8% | 2.0/5.4% | 3 |
| True | 1 | 0.829 | 0.825 | 0.004 | - | - | 0.916 | 0.916 | 0.521 | 1.52x | 18.2/24.7/29.8% | 2.0/5.4% | 3 |

### `RT-hopassign` - hop-assign  `--scenario alpine`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| random | 1 | 0.795 | 0.786 | 0.009 | - | - | 0.924 | 0.927 | 0.443 | 1.39x | 16.0/21.8/25.4% | 2.0/5.3% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario alpine`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.602 | 0.578 | 0.023 | - | - | 0.775 | 0.777 | 0.185 | 1.06x | 12.7/18.2/21.4% | 1.6/4.5% | 3 |
| 7 | 1 | 0.865 | 0.861 | 0.004 | - | - | 0.935 | 0.936 | 0.602 | 1.51x | 17.2/22.9/26.5% | 2.2/5.4% | 3 |
| 15 | 1 | 0.899 | 0.898 | 0.001 | - | - | 0.953 | 0.953 | 0.702 | 1.55x | 17.2/23.3/26.6% | 2.3/5.4% | 3 |
| 32 | 1 | 0.891 | 0.890 | 0.001 | - | - | 0.944 | 0.945 | 0.702 | 1.55x | 17.3/23.0/26.6% | 2.3/5.4% | 3 |

> hop-limit=32: misdecodes 1

### `RT-hopspread` - hop-limit  `--scenario alpine`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.602 | 0.578 | 0.023 | - | - | 0.775 | 0.777 | 0.185 | 1.06x | 12.7/18.2/21.4% | 1.6/4.5% | 3 |
| 5 | 1 | 0.786 | 0.774 | 0.011 | - | - | 0.902 | 0.902 | 0.429 | 1.36x | 15.8/21.8/24.9% | 1.9/5.3% | 3 |
| 7 | 1 | 0.865 | 0.861 | 0.004 | - | - | 0.935 | 0.936 | 0.602 | 1.51x | 17.2/22.9/26.5% | 2.2/5.4% | 3 |

### `RT-rebroadcast` - rebroadcast-mode  `--scenario alpine`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| KNOWN_ONLY | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.791 | 0.791 | 0.000 | - | - | 0.852 | 0.919 | 0.475 | 1.35x | 15.7/21.6/25.1% | 2.0/5.3% | 3 |

### `RT-spread` - hop-spread  `--scenario alpine`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.602 | 0.578 | 0.023 | - | - | 0.775 | 0.777 | 0.185 | 1.06x | 12.7/18.2/21.4% | 1.6/4.5% | 3 |
| True | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |

### `SC-signing` - signature-policy  `--scenario alpine`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| BALANCED | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| STRICT | 1 | 0.653 | 0.653 | 0.000 | - | - | 0.787 | 0.787 | 0.313 | 1.54x | 17.6/24.4/28.6% | 2.3/5.9% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario alpine`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| dm | 1 | 0.794 | 0.787 | 0.007 | - | - | 0.902 | 0.902 | 0.480 | 1.36x | 15.8/21.8/25.5% | 1.9/5.3% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario alpine`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.791 | 0.782 | 0.008 | - | - | 0.911 | 0.913 | 0.457 | 1.40x | 16.2/22.3/26.1% | 2.0/5.4% | 3 |
| local | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| time | 1 | 0.797 | 0.790 | 0.007 | - | - | 0.915 | 0.917 | 0.471 | 1.42x | 16.5/23.0/26.8% | 2.0/5.5% | 3 |
| window | 1 | 0.801 | 0.793 | 0.008 | - | - | 0.923 | 0.924 | 0.466 | 1.38x | 15.9/22.2/25.8% | 2.0/5.4% | 3 |

> bucket-mode=global: misdecodes 44

> bucket-mode=time: misdecodes 28

> bucket-mode=window: misdecodes 11

### `SF-bucket-time` - time-bucket-s  `--scenario alpine`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.795 | 0.786 | 0.009 | - | - | 0.915 | 0.917 | 0.470 | 1.52x | 18.0/24.4/28.6% | 2.1/5.9% | 3 |
| 1800 | 1 | 0.797 | 0.790 | 0.007 | - | - | 0.915 | 0.917 | 0.471 | 1.42x | 16.5/23.0/26.8% | 2.0/5.5% | 3 |
| 3600 | 1 | 0.796 | 0.788 | 0.008 | - | - | 0.919 | 0.923 | 0.465 | 1.38x | 16.0/22.1/25.8% | 2.0/5.4% | 3 |

> time-bucket-s=600: misdecodes 142

> time-bucket-s=1800: misdecodes 28

> time-bucket-s=3600: misdecodes 14

### `SF-cadence` - trigger  `--scenario alpine`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| interval | 1 | 0.786 | 0.777 | 0.009 | - | - | 0.907 | 0.912 | 0.466 | 1.78x | 21.9/29.1/33.9% | 2.4/7.3% | 3 |
| aimd | 1 | 0.788 | 0.785 | 0.002 | - | - | 0.870 | 0.920 | 0.467 | 1.40x | 16.1/22.4/26.2% | 2.0/5.4% | 3 |
| bucket+interval | 1 | 0.774 | 0.764 | 0.010 | - | - | 0.895 | 0.895 | 0.465 | 1.80x | 22.1/29.3/34.2% | 2.4/7.2% | 3 |

> trigger=interval: misdecodes 14

> trigger=aimd: misdecodes 3

> trigger=aimd: decode_failures 3

> trigger=bucket+interval: misdecodes 6

### `SF-capacity` - capacity  `--scenario alpine`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.802 | 0.793 | 0.009 | - | - | 0.918 | 0.922 | 0.466 | 1.39x | 16.0/22.1/26.0% | 2.0/5.4% | 3 |
| 8 | 1 | 0.802 | 0.792 | 0.011 | - | - | 0.925 | 0.925 | 0.464 | 1.38x | 16.0/22.1/26.0% | 2.0/5.4% | 3 |
| 16 | 1 | 0.795 | 0.788 | 0.007 | - | - | 0.911 | 0.914 | 0.475 | 1.40x | 16.2/22.6/26.2% | 2.0/5.5% | 3 |
| 32 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 50 | 1 | 0.797 | 0.789 | 0.008 | - | - | 0.916 | 0.919 | 0.466 | 1.39x | 16.2/22.3/26.1% | 2.0/5.4% | 3 |

> capacity=4: decode_failures 94

> capacity=8: decode_failures 27

> capacity=16: decode_failures 1

### `SF-capacity-local` - capacity  `--scenario alpine`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.802 | 0.793 | 0.009 | - | - | 0.918 | 0.922 | 0.466 | 1.39x | 16.0/22.1/26.0% | 2.0/5.4% | 3 |
| 8 | 1 | 0.802 | 0.792 | 0.011 | - | - | 0.925 | 0.925 | 0.464 | 1.38x | 16.0/22.1/26.0% | 2.0/5.4% | 3 |
| 16 | 1 | 0.795 | 0.788 | 0.007 | - | - | 0.911 | 0.914 | 0.475 | 1.40x | 16.2/22.6/26.2% | 2.0/5.5% | 3 |
| 32 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 50 | 1 | 0.797 | 0.789 | 0.008 | - | - | 0.916 | 0.919 | 0.466 | 1.39x | 16.2/22.3/26.1% | 2.0/5.4% | 3 |

> capacity=4: decode_failures 94

> capacity=8: decode_failures 27

> capacity=16: decode_failures 1

### `SF-capacity-window` - capacity  `--scenario alpine`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.803 | 0.795 | 0.007 | - | - | 0.924 | 0.928 | 0.468 | 1.39x | 16.0/22.4/26.1% | 2.0/5.4% | 3 |
| 16 | 1 | 0.802 | 0.792 | 0.010 | - | - | 0.929 | 0.930 | 0.464 | 1.39x | 16.1/22.3/26.0% | 2.0/5.4% | 3 |
| 32 | 1 | 0.801 | 0.793 | 0.008 | - | - | 0.923 | 0.924 | 0.466 | 1.38x | 15.9/22.2/25.8% | 2.0/5.4% | 3 |

> capacity=8: misdecodes 22

> capacity=8: decode_failures 9

> capacity=16: misdecodes 7

> capacity=32: misdecodes 11

### `SF-catchup` - catch-up-hours  `--scenario alpine`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.774 | 0.764 | 0.010 | - | - | 0.895 | 0.895 | 0.465 | 1.80x | 22.1/29.3/34.2% | 2.4/7.2% | 3 |
| 02-06 | 1 | 0.792 | 0.787 | 0.006 | - | - | 0.884 | 0.921 | 0.472 | 1.41x | 16.4/22.7/26.6% | 2.0/5.5% | 3 |
| 00-08 | 1 | 0.794 | 0.788 | 0.006 | - | - | 0.894 | 0.916 | 0.464 | 1.46x | 17.3/23.5/27.8% | 2.1/5.8% | 3 |

> catch-up-hours=: misdecodes 6

> catch-up-hours=02-06: decode_failures 32

> catch-up-hours=00-08: decode_failures 33

### `SF-hops-flat` - hops-apart  `--scenario alpine`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.787 | 0.785 | 0.002 | - | - | 0.925 | 0.925 | 0.461 | 1.40x | 16.2/22.5/26.1% | 2.0/5.5% | 3 |
| 2 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 3 | 1 | 0.811 | 0.790 | 0.021 | - | - | 0.915 | 0.920 | 0.457 | 1.40x | 16.3/22.8/26.1% | 2.0/5.4% | 3 |
| 4 | 1 | 0.821 | 0.787 | 0.034 | - | - | 0.969 | 0.975 | 0.488 | 1.43x | 16.7/23.1/26.7% | 2.0/5.7% | 3 |

> hops-apart=4: decode_failures 3

### `SF-hops-spread` - hops-apart  `--scenario alpine`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.787 | 0.785 | 0.002 | - | - | 0.925 | 0.925 | 0.461 | 1.40x | 16.2/22.5/26.1% | 2.0/5.5% | 3 |
| 2 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 3 | 1 | 0.811 | 0.790 | 0.021 | - | - | 0.915 | 0.920 | 0.457 | 1.40x | 16.3/22.8/26.1% | 2.0/5.4% | 3 |
| 4 | 1 | 0.821 | 0.787 | 0.034 | - | - | 0.969 | 0.975 | 0.488 | 1.43x | 16.7/23.1/26.7% | 2.0/5.7% | 3 |
| 5 | 1 | 0.804 | 0.790 | 0.014 | - | - | 0.799 | 0.964 | 0.469 | 1.41x | 16.3/22.8/26.1% | 2.0/5.4% | 3 |

> hops-apart=4: decode_failures 3

> hops-apart=5: decode_failures 25

### `SF-jitter-global` - advert-jitter-s  `--scenario alpine`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.789 | 0.782 | 0.006 | - | - | 0.907 | 0.908 | 0.463 | 1.40x | 16.2/22.5/26.1% | 2.0/5.4% | 3 |
| 30 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 120 | 1 | 0.791 | 0.781 | 0.009 | - | - | 0.911 | 0.913 | 0.463 | 1.38x | 16.0/22.2/25.9% | 2.0/5.4% | 3 |
| 600 | 1 | 0.802 | 0.795 | 0.007 | - | - | 0.930 | 0.930 | 0.466 | 1.39x | 16.3/22.4/26.1% | 2.0/5.5% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario alpine`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.789 | 0.782 | 0.006 | - | - | 0.907 | 0.908 | 0.463 | 1.40x | 16.2/22.5/26.1% | 2.0/5.4% | 3 |
| 30 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 120 | 1 | 0.791 | 0.781 | 0.009 | - | - | 0.911 | 0.913 | 0.463 | 1.38x | 16.0/22.2/25.9% | 2.0/5.4% | 3 |
| 600 | 1 | 0.802 | 0.795 | 0.007 | - | - | 0.930 | 0.930 | 0.466 | 1.39x | 16.3/22.4/26.1% | 2.0/5.5% | 3 |

### `SF-place-flat` - place  `--scenario alpine`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.807 | 0.785 | 0.021 | - | - | 0.840 | 0.924 | 0.477 | 1.41x | 16.4/22.4/26.2% | 2.1/5.4% | 3 |
| routers | 1 | 0.792 | 0.787 | 0.006 | - | - | 0.936 | 0.937 | 0.471 | 1.39x | 16.1/22.5/25.9% | 2.0/5.5% | 3 |
| alternate-routers | 1 | 0.801 | 0.793 | 0.008 | - | - | 0.946 | 0.951 | 0.479 | 1.38x | 16.0/22.3/25.8% | 2.0/5.5% | 3 |
| beside-router | 1 | 0.792 | 0.786 | 0.006 | - | - | 0.936 | 0.938 | 0.475 | 1.40x | 16.1/22.5/26.2% | 2.0/5.4% | 3 |
| random-clients | 1 | 0.790 | 0.788 | 0.002 | - | - | 0.934 | 0.934 | 0.471 | 1.40x | 16.2/22.6/25.9% | 2.0/5.5% | 3 |
| hops-apart | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |

> place=spread: decode_failures 28

### `SF-place-spread` - place  `--scenario alpine`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.807 | 0.785 | 0.021 | - | - | 0.840 | 0.924 | 0.477 | 1.41x | 16.4/22.4/26.2% | 2.1/5.4% | 3 |
| routers | 1 | 0.792 | 0.787 | 0.006 | - | - | 0.936 | 0.937 | 0.471 | 1.39x | 16.1/22.5/25.9% | 2.0/5.5% | 3 |
| alternate-routers | 1 | 0.801 | 0.793 | 0.008 | - | - | 0.946 | 0.951 | 0.479 | 1.38x | 16.0/22.3/25.8% | 2.0/5.5% | 3 |
| beside-router | 1 | 0.792 | 0.786 | 0.006 | - | - | 0.936 | 0.938 | 0.475 | 1.40x | 16.1/22.5/26.2% | 2.0/5.4% | 3 |
| random-clients | 1 | 0.790 | 0.788 | 0.002 | - | - | 0.934 | 0.934 | 0.471 | 1.40x | 16.2/22.6/25.9% | 2.0/5.5% | 3 |
| hops-apart | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |

> place=spread: decode_failures 28

### `SF-provide-transport` - provide-transport  `--scenario alpine`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| broadcast | 1 | 0.802 | 0.780 | 0.022 | - | - | 0.910 | 0.911 | 0.491 | 1.43x | 16.6/23.2/26.8% | 2.1/5.6% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario alpine`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| heard | 1 | 0.801 | 0.793 | 0.007 | - | - | 0.920 | 0.923 | 0.451 | 1.38x | 15.9/22.2/25.9% | 2.0/5.4% | 3 |

> replay-ordering=heard: misdecodes 17

### `SF-replay-order-broadcast` - replay-ordering  `--scenario alpine`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.802 | 0.780 | 0.022 | - | - | 0.910 | 0.911 | 0.491 | 1.43x | 16.6/23.2/26.8% | 2.1/5.6% | 3 |
| heard | 1 | 0.804 | 0.783 | 0.021 | - | - | 0.912 | 0.914 | 0.469 | 1.43x | 16.6/23.3/27.0% | 2.0/5.6% | 3 |

> replay-ordering=heard: misdecodes 12

### `SF-resolve` - resolve  `--scenario alpine`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| enum | 1 | 0.796 | 0.785 | 0.011 | - | - | 0.923 | 0.923 | 0.445 | 1.40x | 16.3/22.5/26.5% | 2.0/5.4% | 3 |
| hybrid | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |

### `SF-servers-allrouters` - servers  `--scenario alpine`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.792 | 0.787 | 0.006 | - | - | 0.936 | 0.937 | 0.471 | 1.39x | 16.1/22.5/25.9% | 2.0/5.5% | 3 |
| 6 | 1 | 0.800 | 0.784 | 0.016 | - | - | 0.945 | 0.948 | 0.458 | 1.41x | 16.3/22.7/26.4% | 2.0/5.7% | 6 |

### `SF-servers-flat` - servers  `--scenario alpine`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.795 | 0.788 | 0.007 | - | - | 0.917 | 0.918 | 0.463 | 1.37x | 15.8/22.0/25.5% | 2.0/5.4% | 2 |
| 3 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 5 | 1 | 0.794 | 0.784 | 0.009 | - | - | 0.915 | 0.916 | 0.446 | 1.43x | 16.7/22.9/26.9% | 2.1/5.5% | 5 |
| 8 | 1 | 0.787 | 0.772 | 0.015 | - | - | 0.927 | 0.928 | 0.458 | 1.45x | 17.0/23.0/27.1% | 2.1/5.6% | 8 |

### `SF-servers-spread` - servers  `--scenario alpine`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.795 | 0.788 | 0.007 | - | - | 0.917 | 0.918 | 0.463 | 1.37x | 15.8/22.0/25.5% | 2.0/5.4% | 2 |
| 3 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 5 | 1 | 0.794 | 0.784 | 0.009 | - | - | 0.915 | 0.916 | 0.446 | 1.43x | 16.7/22.9/26.9% | 2.1/5.5% | 5 |
| 8 | 1 | 0.787 | 0.772 | 0.015 | - | - | 0.927 | 0.928 | 0.458 | 1.45x | 17.0/23.0/27.1% | 2.1/5.6% | 8 |

### `SF-signed` - signed  `--scenario alpine`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| True | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario alpine`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.809 | 0.801 | 0.008 | - | - | 0.947 | 0.948 | 0.455 | 1.32x | 15.2/21.1/24.6% | 1.9/5.0% | 3 |
| 1 | 1 | 0.803 | 0.796 | 0.007 | - | - | 0.923 | 0.923 | 0.475 | 1.34x | 15.5/21.3/24.9% | 2.0/5.1% | 3 |
| 2 | 1 | 0.807 | 0.801 | 0.006 | - | - | 0.936 | 0.937 | 0.460 | 1.33x | 15.3/21.2/24.7% | 1.9/5.1% | 3 |
| 4 | 1 | 0.807 | 0.801 | 0.006 | - | - | 0.936 | 0.937 | 0.460 | 1.33x | 15.3/21.2/24.7% | 1.9/5.1% | 3 |

### `SF-width` - short-id-bits  `--scenario alpine`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.791 | 0.783 | 0.008 | - | - | 0.912 | 0.916 | 0.457 | 1.37x | 15.9/22.0/25.6% | 2.0/5.4% | 3 |
| 24 | 1 | 0.804 | 0.796 | 0.007 | - | - | 0.927 | 0.927 | 0.464 | 1.41x | 16.3/22.5/26.3% | 2.1/5.5% | 3 |
| 32 | 1 | 0.803 | 0.794 | 0.008 | - | - | 0.917 | 0.919 | 0.458 | 1.40x | 16.2/22.5/26.2% | 2.0/5.5% | 3 |
| 64 | 1 | 0.798 | 0.791 | 0.007 | - | - | 0.917 | 0.920 | 0.480 | 1.41x | 16.3/22.5/26.3% | 2.0/5.4% | 3 |

### `SF-window-size` - window-size  `--scenario alpine`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.795 | 0.787 | 0.009 | - | - | 0.915 | 0.915 | 0.466 | 1.43x | 16.6/23.2/26.7% | 2.1/5.6% | 3 |
| 16 | 1 | 0.786 | 0.778 | 0.008 | - | - | 0.905 | 0.908 | 0.454 | 1.38x | 16.1/22.4/26.0% | 2.0/5.4% | 3 |
| 32 | 1 | 0.801 | 0.793 | 0.008 | - | - | 0.923 | 0.924 | 0.466 | 1.38x | 15.9/22.2/25.8% | 2.0/5.4% | 3 |

> window-size=8: misdecodes 107

> window-size=16: misdecodes 34

> window-size=32: misdecodes 11

### `TH-congestion` - no-congestion-scaling  `--scenario alpine`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.942 | 0.936 | 0.006 | - | - | 0.994 | 0.995 | 0.764 | 2.01x | 19.9/30.7/33.6% | 1.3/5.1% | 3 |
| True | 1 | 0.723 | 0.702 | 0.021 | - | - | 0.857 | 0.858 | 0.509 | 5.62x | 51.3/70.8/75.4% | 3.6/11.7% | 3 |

> no-congestion-scaling=True: decode_failures 31

### `TH-congestion-input` - congestion-input  `--scenario alpine`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.489 | 0.480 | 0.009 | - | - | 0.763 | 0.774 | 0.133 | 4.63x | 14.8/33.1/46.8% | 1.5/5.5% | 3 |
| truesize | 1 | 0.526 | 0.516 | 0.010 | - | - | 0.807 | 0.810 | 0.134 | 3.32x | 10.0/26.7/38.1% | 1.0/4.8% | 3 |

> congestion-input=hotstore: decode_failures 56

> congestion-input=truesize: decode_failures 2

> slower: 22.1 s per simulated hour against 10.6 over 14 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `TH-congestion-mode` - congestion-mode  `--scenario alpine`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.945 | 0.940 | 0.005 | - | - | 0.995 | 0.995 | 0.777 | 1.87x | 18.5/28.2/31.1% | 1.2/4.7% | 3 |
| adaptive | 1 | 0.942 | 0.936 | 0.006 | - | - | 0.994 | 0.995 | 0.764 | 2.01x | 19.9/30.7/33.6% | 1.3/5.1% | 3 |

