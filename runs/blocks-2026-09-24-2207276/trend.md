# Sweep blocks-2026-09-24-2207276

- **sim version** `1.6.1`
- **transport** `4195f52`
- **ground** ridge
- **seed base** 2207276 · seeds 2207276
- **blocks** 87 run
- **compute** 11.7 h of simulator time across every cell
- **generated** 2026-09-24T09:09:35+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>88 warnings</summary>

- AD-siting: siting-mix=local-typical: decode_failures 26
- AD-siting: siting-mix=basement-heavy: decode_failures 2
- AD-siting: slower: 3.73 s per simulated hour against 1.32 over 34 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- BL-control: protocol=sr: decode_failures 1
- DB-hotstore-stress: max-num-nodes=10: decode_failures 55
- DB-hotstore-stress: max-num-nodes=120: decode_failures 45
- DB-hotstore-stress: max-num-nodes=250: decode_failures 27
- DB-warm: warm-num-nodes=0: decode_failures 97
- DB-warm: warm-num-nodes=25: decode_failures 97
- DB-warm: warm-num-nodes=100: decode_failures 97
- DB-warm: warm-num-nodes=2000: decode_failures 97
- DG-burst: burst-loss=0.2: decode_failures 42
- DG-burst: burst-loss=0.3: decode_failures 37
- DG-loss: extra-loss=0.2: decode_failures 1
- DG-outage: burst-loss=0.1: decode_failures 42
- DG-outage: burst-loss=0.2: decode_failures 23
- DG-outage: burst-loss=0.3: decode_failures 24
- FW-mixed: legacy-fraction=0.5: decode_failures 3
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 6
- LD-chatty: broadcast-interval-s=300: decode_failures 25
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 97
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 17.4% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 93
- MS-density: nodes=120: misdecodes 1
- MS-density: nodes=150: misdecodes 2
- MS-hopscale: nodes=120: decode_failures 75
- MS-hopscale: nodes=250: decode_failures 30
- MS-hopscale: nodes=500: decode_failures 53
- MS-oversubscribed: nodes=120: decode_failures 1
- MS-oversubscribed: nodes=250: decode_failures 45
- MS-oversubscribed: nodes=500: decode_failures 12
- MS-size: nodes=90: decode_failures 2
- MS-size: nodes=120: decode_failures 75
- MS-size: slower: 7.99 s per simulated hour against 3.4 over 34 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- MS-topology: topology=corridor: decode_failures 16
- PR-repeats-busy: extra-repeats=False: misdecodes 1
- RF-preset: preset=LONG_MODERATE: decode_failures 11
- RF-txpower: tx-power=14: decode_failures 5
- RT-adopt: no-adopt-hop-recommendation=False: misdecodes 1
- RT-hoplimit: hop-limit=3: decode_failures 5
- RT-hopspread: hop-limit=3: decode_failures 5
- RT-spread: hop-spread=False: decode_failures 5
- SF-bucket-mode: bucket-mode=global: misdecodes 42
- SF-bucket-mode: bucket-mode=time: misdecodes 25
- SF-bucket-mode: bucket-mode=window: misdecodes 24
- SF-bucket-time: time-bucket-s=600: misdecodes 126
- SF-bucket-time: time-bucket-s=1800: misdecodes 25
- SF-bucket-time: time-bucket-s=3600: misdecodes 9
- SF-cadence: trigger=interval: misdecodes 9
- SF-cadence: trigger=interval: decode_failures 3
- SF-cadence: trigger=aimd: misdecodes 3
- SF-cadence: trigger=bucket+interval: misdecodes 12
- SF-capacity-local: capacity=4: decode_failures 94
- SF-capacity-local: capacity=8: decode_failures 59
- SF-capacity-local: capacity=16: decode_failures 2
- SF-capacity: capacity=4: decode_failures 94
- SF-capacity: capacity=8: decode_failures 59
- SF-capacity: capacity=16: decode_failures 2
- SF-capacity-window: capacity=8: misdecodes 20
- SF-capacity-window: capacity=8: decode_failures 40
- SF-capacity-window: capacity=16: misdecodes 18
- SF-capacity-window: capacity=16: decode_failures 2
- SF-capacity-window: capacity=32: misdecodes 24
- SF-catchup: catch-up-hours=: misdecodes 12
- SF-catchup: catch-up-hours=02-06: decode_failures 26
- SF-catchup: catch-up-hours=00-08: decode_failures 27
- SF-hops-flat: hops-apart=3: decode_failures 1
- SF-hops-flat: hops-apart=4: decode_failures 32
- SF-hops-spread: hops-apart=3: decode_failures 1
- SF-hops-spread: hops-apart=4: decode_failures 32
- SF-hops-spread: hops-apart=5: decode_failures 31
- SF-place-flat: place=spread: decode_failures 21
- SF-place-flat: place=random-clients: decode_failures 8
- SF-place-spread: place=spread: decode_failures 21
- SF-place-spread: place=random-clients: decode_failures 8
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 6
- SF-replay-order: replay-ordering=heard: misdecodes 11
- SF-servers-allrouters: servers=6: decode_failures 20
- SF-servers-allrouters: slower: 4.9 s per simulated hour against 1.85 over 34 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- SF-window-size: window-size=8: misdecodes 117
- SF-window-size: window-size=16: misdecodes 48
- SF-window-size: window-size=32: misdecodes 24
- TH-congestion-input: congestion-input=hotstore: decode_failures 45
- TH-congestion-input: congestion-input=truesize: decode_failures 59
- TH-congestion-input: slower: 32.7 s per simulated hour against 10.8 over 34 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- TH-congestion-mode: congestion-mode=adaptive: misdecodes 1
- TH-congestion: no-congestion-scaling=False: misdecodes 1
- TH-congestion: no-congestion-scaling=True: decode_failures 72

</details>

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `TH-congestion-input` | 32.7 | 10.8 | 3.02x | 34 |
| `AD-siting` | 3.73 | 1.32 | 2.82x | 34 |
| `SF-servers-allrouters` | 4.9 | 1.85 | 2.65x | 34 |
| `MS-size` | 7.99 | 3.4 | 2.35x | 34 |
| `DG-burst` | 7.62 | 5.01 | 1.52x | 34 |
| `SF-cadence` | 5.18 | 3.41 | 1.52x | 34 |
| `AD-amplify-worst` | 1.19 | 1.79 | 0.67x | 34 |
| `RF-stretch-duct` | 1.26 | 1.96 | 0.64x | 34 |
| `MS-stretch` | 1.28 | 2 | 0.64x | 34 |
| `TH-congestion` | 10.5 | 17.1 | 0.61x | 34 |
| `DM-mode` | 1.93 | 3.17 | 0.61x | 34 |
| `SF-signed` | 1.04 | 1.74 | 0.60x | 34 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text on air` is the broadcast reach in the same cells - first chance only, so an archive replaying an object cannot be credited with it - and an arm buying its measure while that falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text on air | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.976 | 0.976 | 0.827 → 0.834 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.949 | 0.949 | 0.807 → 0.831 | 1.1x bytes_on_air | up | 3 |
| `RF-preset-turbo` | preset | **held** | 0.117 → 0.949 | 0.831 | 0.058 → 0.831 | 9.1x sr_airtime | up | 5 |
| `RF-txpower` | tx-power | **held** | 0.140 → 0.949 | 0.809 | 0.074 → 0.831 | 9.5x sr_airtime | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.104 → 0.889 | 0.785 | 0.098 → 0.767 | 1.2e+02x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **held** | 0.180 → 0.942 | 0.761 | 0.079 → 0.797 | 6x sr_bytes | down | 3 |
| `MS-stretch` | stretch | **held** | 0.211 → 0.949 | 0.737 | 0.140 → 0.831 | 5.9x sr_airtime | down | 4 |
| `MS-siting` | siting-mix | **text** | 0.230 → 0.966 | 0.736 | 0.230 → 0.965 | 6.7x sr_airtime | up | 4 |
| `RF-bw500` | preset | **held** | 0.163 → 0.874 | 0.711 | 0.124 → 0.762 | 6x advert_bytes | up | 3 |
| `RF-preset` | preset | **held** | 0.332 → 0.955 | 0.623 | 0.266 → 0.831 | 7.6x sr_airtime | up | 3 |
| `RF-eu-presets` | preset | **held** | 0.332 → 0.949 | 0.617 | 0.266 → 0.831 | 5.4x sr_bytes | up | 4 |
| `MS-hopscale` | nodes | **text** | 0.294 → 0.842 | 0.548 | 0.288 → 0.831 | 11x sr_bytes | down | 4 |
| `MS-oversubscribed` | nodes | **text** | 0.295 → 0.724 | 0.429 | 0.289 → 0.713 | 4.7x bytes_on_air | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.488 → 0.842 | 0.353 | 0.469 → 0.831 | 2.1x sr_bytes | down | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.566 → 0.916 | 0.351 | 0.552 → 0.912 | 8.1x sr_airtime | down | 3 |
| `MS-topology` | topology | **text** | 0.562 → 0.899 | 0.337 | 0.525 → 0.893 | 2.8x sr_bytes | up | 4 |
| `MS-density` | nodes | **text** | 0.620 → 0.955 | 0.336 | 0.602 → 0.953 | 5x sr_airtime | up | 5 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.536 → 0.870 | 0.334 | 0.515 → 0.862 | 6.7x sr_airtime | down | 3 |
| `DG-burst` | burst-loss | **text** | 0.516 → 0.842 | 0.326 | 0.488 → 0.831 | 2.2x sr_bytes | down | 4 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.356 → 0.668 | 0.312 | 0.352 → 0.661 | 2.2x sr_airtime | up | 2 |
| `RT-hoplimit` | hop-limit | **text** | 0.661 → 0.938 | 0.277 | 0.622 → 0.937 | 3.2x sr_bytes | up | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.431 → 0.692 | 0.261 | 0.284 → 0.444 | 5.6x sr_airtime | up | 3 |
| `RT-hopspread` | hop-limit | **text** | 0.661 → 0.884 | 0.222 | 0.622 → 0.877 | 2.2x sr_bytes | up | 3 |
| `SF-place-flat` | place | **held** | 0.751 → 0.962 | 0.211 | 0.822 → 0.835 | 3.1x sr_bytes | up | 6 |
| `SF-place-spread` | place | **held** | 0.751 → 0.962 | 0.211 | 0.822 → 0.835 | 3.1x sr_bytes | up | 6 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.734 → 0.940 | 0.206 | 0.719 → 0.936 | 3.8x sr_airtime | down | 2 |
| `SC-signing` | signature-policy | **held** | 0.753 → 0.949 | 0.195 | 0.665 → 0.831 | 1.5x sr_airtime | down | 3 |
| `MS-size` | nodes | **text** | 0.656 → 0.842 | 0.186 | 0.638 → 0.831 | 6.2x sr_bytes | down | 5 |
| `RT-spread` | hop-spread | **text** | 0.661 → 0.842 | 0.180 | 0.622 → 0.831 | 2.1x sr_bytes | up | 2 |
| `RF-noise` | noise-profile | **text** | 0.677 → 0.842 | 0.164 | 0.666 → 0.831 | 1.4x sr_bytes | down | 4 |
| `DG-loss` | extra-loss | **text** | 0.687 → 0.842 | 0.154 | 0.669 → 0.831 | 1.5x sr_bytes | down | 4 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.842 → 0.964 | 0.122 | 0.831 → 0.959 | 1.5x sr_airtime | up | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.842 → 0.962 | 0.120 | 0.831 → 0.960 | 1.5x sr_airtime | up | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.762 → 0.876 | 0.114 | 0.747 → 0.869 | 2x sr_airtime | up | 4 |
| `DB-platform` | platform-mix | **text** | 0.762 → 0.876 | 0.114 | 0.748 → 0.869 | 2.1x sr_airtime | down | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.759 → 0.869 | 0.111 | 0.619 → 0.727 | 1.5x sr_airtime | down | 2 |
| `LD-interval` | broadcast-interval-s | **text** | 0.785 → 0.895 | 0.110 | 0.770 → 0.889 | 5.2x sr_airtime | up | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.881 → 0.976 | 0.094 | 0.818 → 0.834 | 2.3x sr_bytes | down | 5 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.856 → 0.949 | 0.093 | 0.826 → 0.831 | 25x sr_airtime | down | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.835 → 0.922 | 0.087 | 0.823 → 0.913 | 1.6x bytes_on_air | up | 3 |
| `SF-cadence` | trigger | **held** | 0.880 → 0.949 | 0.068 | 0.794 → 0.831 | 13x advert_bytes | down | 4 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.820 → 0.883 | 0.064 | 0.804 → 0.873 | 2.3x bytes_on_air | down | 4 |
| `SF-hops-flat` | hops-apart | **held** | 0.915 → 0.976 | 0.060 | 0.818 → 0.834 | 2.3x sr_bytes | up | 4 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.782 → 0.842 | 0.060 | 0.764 → 0.831 | 1.5x sr_airtime | down | 4 |
| `AD-flooding` | role-mix | **text** | 0.810 → 0.867 | 0.057 | 0.797 → 0.859 | 2.2x bytes_on_air | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.810 → 0.867 | 0.057 | 0.797 → 0.859 | 2.2x bytes_on_air | up | 3 |
| `FW-mixed` | legacy-fraction | **text** | 0.831 → 0.883 | 0.052 | 0.816 → 0.869 | 2.2x bytes_on_air | down | 4 |
| `FW-versions` | profile | **text** | 0.842 → 0.892 | 0.050 | 0.831 → 0.886 | 3.4x bytes_on_air | down | 5 |
| `AD-badrouters` | role-placement | **held** | 0.892 → 0.942 | 0.050 | 0.743 → 0.797 | 1.1x sr_bytes | down | 3 |
| `SF-servers-flat` | servers | **held** | 0.916 → 0.958 | 0.041 | 0.816 → 0.832 | 6.7x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.916 → 0.958 | 0.041 | 0.816 → 0.832 | 6.7x sr_bytes | up | 4 |
| `MS-router-late` | router-late-fraction | **held** | 0.908 → 0.949 | 0.040 | 0.831 → 0.846 | 1.3x bytes_on_air | down | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.842 → 0.881 | 0.039 | 0.831 → 0.874 | 3.4x bytes_on_air | down | 2 |
| `FW-firmware` | profile | **held** | 0.949 → 0.983 | 0.035 | 0.831 → 0.865 | 3.3x bytes_on_air | down | 2 |
| `SF-catchup` | catch-up-hours | **text** | 0.810 → 0.839 | 0.030 | 0.794 → 0.833 | 9x advert_bytes | up | 3 |
| `TH-congestion-input` | congestion-input | **held** | 0.681 → 0.710 | 0.029 | 0.444 → 0.468 | 1.5x sr_airtime | up | 2 |
| `MS-roles-fav` | role-mix | **held** | 0.945 → 0.971 | 0.026 | 0.825 → 0.840 | 1.2x sr_airtime | down | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.845 → 0.868 | 0.023 | 0.835 → 0.859 | 1.1x sr_airtime | up | 2 |
| `DM-mode` | dm-mode | **held** | 0.905 → 0.926 | 0.021 | 0.791 → 0.801 | 1.2x sr_airtime | up | 3 |
| `LD-diurnal` | diurnal | **text** | 0.842 → 0.862 | 0.020 | 0.831 → 0.854 | 1.3x sr_bytes | down | 3 |
| `SF-provide-transport` | provide-transport | **text** | 0.842 → 0.862 | 0.020 | 0.824 → 0.831 | 2.9x sr_airtime | up | 2 |
| `MS-roles` | role-mix | **text** | 0.810 → 0.830 | 0.020 | 0.797 → 0.821 | 1.2x sr_bytes | down | 2 |
| `SF-capacity-window` | capacity | **held** | 0.928 → 0.947 | 0.019 | 0.824 → 0.828 | 2.1x advert_bytes | up | 3 |
| `SF-sr-retries` | sr-retries | **held** | 0.935 → 0.954 | 0.019 | 0.825 → 0.835 | 1.1x sr_bytes | down | 4 |
| `AD-worst` | role-placement | **text** | 0.833 → 0.849 | 0.016 | 0.821 → 0.843 | 1.3x sr_bytes | down | 2 |
| `SF-servers-allrouters` | servers | **held** | 0.962 → 0.977 | 0.015 | 0.814 → 0.835 | 2.6x sr_bytes | up | 2 |
| `SF-resolve` | resolve | **held** | 0.934 → 0.949 | 0.015 | 0.822 → 0.831 | 5.9x advert_bytes | = | 3 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.935 → 0.949 | 0.013 | 0.815 → 0.831 | 2.6x advert_bytes | up | 4 |
| `SF-capacity` | capacity | **held** | 0.935 → 0.949 | 0.013 | 0.822 → 0.831 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.935 → 0.949 | 0.013 | 0.822 → 0.831 | 5.3x advert_bytes | up | 5 |
| `SF-advert-transport` | advert-transport | **held** | 0.936 → 0.949 | 0.012 | 0.826 → 0.831 | 2.2x sr_airtime | down | 2 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.912 → 0.923 | 0.011 | 0.798 → 0.803 | 1.1x sr_airtime | down | 2 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.938 → 0.949 | 0.011 | 0.823 → 0.831 | 1.1x sr_bytes | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.938 → 0.949 | 0.011 | 0.823 → 0.831 | 1.1x sr_bytes | down | 4 |
| `RT-hopassign` | hop-assign | **text** | 0.832 → 0.842 | 0.010 | 0.822 → 0.831 | 1.4x sr_airtime | down | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.931 → 0.940 | 0.009 | 0.926 → 0.936 | 1.2x sr_airtime | down | 2 |
| `SF-window-size` | window-size | **held** | 0.939 → 0.947 | 0.009 | 0.820 → 0.826 | 4x advert_bytes | up | 3 |
| `PR-repeats` | extra-repeats | **held** | 0.940 → 0.949 | 0.009 | 0.829 → 0.831 | 1.1x sr_airtime | down | 2 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.829 → 0.838 | 0.008 | 0.814 → 0.826 | 5.3x advert_bytes | up | 3 |
| `SF-width` | short-id-bits | **text** | 0.834 → 0.842 | 0.008 | 0.823 → 0.831 | 3.1x advert_bytes | down | 4 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.940 → 0.947 | 0.007 | 0.936 → 0.943 | 1x sr_airtime | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.940 → 0.946 | 0.006 | 0.823 → 0.824 | 1.1x sr_bytes | down | 2 |
| `SF-replay-order` | replay-ordering | **held** | 0.949 → 0.952 | 0.004 | 0.827 → 0.831 | 1.2x sr_bytes | up | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.940 → 0.943 | 0.003 | 0.936 → 0.939 | 1x sr_airtime | up | 2 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.923 → 0.926 | 0.003 | 0.801 → 0.803 | 1.2x sr_airtime | down | 2 |

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
| none | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| sprinkled | 1 | 0.927 | 0.912 | 0.015 | - | - | 0.969 | 0.972 | 0.579 | 1.09x | 17.4/21.8/26.0% | 1.5/4.8% | 3 |
| arms-race | 1 | 0.962 | 0.960 | 0.002 | - | - | 0.996 | 0.997 | 0.830 | 1.04x | 21.3/25.8/27.6% | 1.4/5.4% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario ridge`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 0.1 | 1 | 0.900 | 0.891 | 0.009 | - | - | 0.981 | 0.982 | 0.704 | 1.12x | 16.7/20.5/23.4% | 1.6/4.8% | 3 |
| 0.3 | 1 | 0.964 | 0.959 | 0.005 | - | - | 0.998 | 0.999 | 0.595 | 0.91x | 22.2/25.9/28.1% | 0.9/5.5% | 3 |

### `AD-badrouters` - role-placement  `--scenario ridge`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.810 | 0.797 | 0.013 | - | - | 0.942 | 0.946 | 0.590 | 1.16x | 13.7/19.0/21.4% | 1.9/4.5% | 3 |
| inverse | 1 | 0.770 | 0.753 | 0.017 | - | - | 0.912 | 0.916 | 0.533 | 1.07x | 12.6/15.7/17.6% | 1.9/3.3% | 3 |
| random | 1 | 0.762 | 0.743 | 0.019 | - | - | 0.892 | 0.893 | 0.452 | 1.09x | 12.4/16.3/20.1% | 1.8/4.0% | 3 |

### `AD-flooding` - role-mix  `--scenario ridge`

*Every node rebroadcasting everything, against a real role census.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.810 | 0.797 | 0.013 | - | - | 0.942 | 0.946 | 0.590 | 1.16x | 13.7/19.0/21.4% | 1.9/4.5% | 3 |
| all-routers | 1 | 0.867 | 0.859 | 0.009 | - | - | 0.923 | 0.923 | 0.708 | 2.55x | 27.5/33.4/36.9% | 4.2/4.7% | 3 |

### `AD-nomute` - role-mix  `--scenario ridge`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 1 | 0.810 | 0.797 | 0.013 | - | - | 0.942 | 0.946 | 0.590 | 1.16x | 13.7/19.0/21.4% | 1.9/4.5% | 3 |
| no-mute | 1 | 0.823 | 0.812 | 0.011 | - | - | 0.949 | 0.952 | 0.610 | 1.25x | 14.8/18.2/21.4% | 2.0/4.5% | 3 |
| all-routers | 1 | 0.867 | 0.859 | 0.009 | - | - | 0.923 | 0.923 | 0.708 | 2.55x | 27.5/33.4/36.9% | 4.2/4.7% | 3 |

### `AD-siting` - siting-mix  `--scenario ridge`

*Siting against a real role census, including a basement-heavy mesh.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.810 | 0.797 | 0.013 | - | - | 0.942 | 0.946 | 0.590 | 1.16x | 13.7/19.0/21.4% | 1.9/4.5% | 3 |
| local-typical | 1 | 0.478 | 0.463 | 0.015 | - | - | 0.705 | 0.721 | 0.000 | 1.17x | 10.1/19.5/26.5% | 1.9/4.8% | 3 |
| basement-heavy | 1 | 0.080 | 0.079 | 0.002 | - | - | 0.180 | 0.259 | 0.000 | 0.53x | 1.8/6.5/13.2% | 0.5/3.1% | 3 |

> siting-mix=local-typical: decode_failures 26

> siting-mix=basement-heavy: decode_failures 2

> slower: 3.73 s per simulated hour against 1.32 over 34 prior run(s) - 2.8x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `AD-worst` - role-placement  `--scenario ridge`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 1 | 0.849 | 0.843 | 0.006 | - | - | 0.977 | 0.977 | 0.109 | 2.36x | 15.8/28.8/34.2% | 1.8/5.7% | 3 |
| inverse | 1 | 0.833 | 0.821 | 0.013 | - | - | 0.984 | 0.985 | 0.168 | 2.26x | 14.8/25.0/30.7% | 1.8/3.5% | 3 |

### `BL-control` - protocol  `--scenario ridge`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.827 | 0.827 | 0.000 | - | - | 0 | 0.000 | 0.556 | 1.26x | 15.0/21.1/22.9% | 1.9/4.7% | 3 |
| sr | 1 | 0.857 | 0.834 | 0.023 | - | - | 0.976 | 0.976 | 0.587 | 1.30x | 15.3/21.9/23.5% | 2.0/4.8% | 3 |

> protocol=sr: decode_failures 1

### `DB-hotstore` - max-num-nodes  `--scenario ridge`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.762 | 0.747 | 0.015 | - | - | 0.839 | 0.839 | 0.606 | 2.86x | 33.0/49.5/56.0% | 4.0/9.2% | 3 |
| 100 | 1 | 0.876 | 0.869 | 0.007 | - | - | 0.929 | 0.930 | 0.727 | 1.49x | 17.3/27.1/30.8% | 2.0/4.9% | 3 |
| 120 | 1 | 0.876 | 0.869 | 0.007 | - | - | 0.929 | 0.930 | 0.727 | 1.49x | 17.3/27.1/30.8% | 2.0/4.9% | 3 |
| 250 | 1 | 0.876 | 0.869 | 0.007 | - | - | 0.929 | 0.930 | 0.727 | 1.49x | 17.3/27.1/30.8% | 2.0/4.9% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario ridge`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 1 | 0.292 | 0.284 | 0.008 | - | - | 0.431 | 0.473 | 0.123 | 11.35x | 36.7/59.1/72.9% | 3.9/10.0% | 3 |
| 120 | 1 | 0.458 | 0.444 | 0.015 | - | - | 0.681 | 0.689 | 0.170 | 4.56x | 14.8/28.3/38.2% | 1.5/5.2% | 3 |
| 250 | 1 | 0.457 | 0.442 | 0.015 | - | - | 0.692 | 0.698 | 0.170 | 4.47x | 14.5/27.1/36.7% | 1.5/5.0% | 3 |

> max-num-nodes=10: decode_failures 55

> max-num-nodes=120: decode_failures 45

> max-num-nodes=250: decode_failures 27

### `DB-platform` - platform-mix  `--scenario ridge`

*The board mix, which decides each node's hot-store size.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.876 | 0.869 | 0.007 | - | - | 0.929 | 0.930 | 0.727 | 1.49x | 17.3/27.1/30.8% | 2.0/4.9% | 3 |
| baymesh-2026-08 | 1 | 0.876 | 0.869 | 0.007 | - | - | 0.929 | 0.930 | 0.727 | 1.49x | 17.3/27.1/30.8% | 2.0/4.9% | 3 |
| constrained | 1 | 0.762 | 0.748 | 0.014 | - | - | 0.833 | 0.835 | 0.597 | 2.85x | 33.2/49.6/55.8% | 3.9/9.2% | 3 |

### `DB-warm` - warm-num-nodes  `--scenario ridge`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.740 | 0.727 | 0.013 | - | - | 0.869 | 0.893 | 0.481 | 5.48x | 58.0/72.9/77.9% | 4.1/12.2% | 3 |
| 25 | 1 | 0.740 | 0.727 | 0.013 | - | - | 0.869 | 0.893 | 0.481 | 5.48x | 58.0/72.9/77.9% | 4.1/12.2% | 3 |
| 100 | 1 | 0.740 | 0.727 | 0.013 | - | - | 0.869 | 0.893 | 0.481 | 5.48x | 58.0/72.9/77.9% | 4.1/12.2% | 3 |
| 2000 | 1 | 0.740 | 0.727 | 0.013 | - | - | 0.869 | 0.893 | 0.481 | 5.48x | 58.0/72.9/77.9% | 4.1/12.2% | 3 |

> warm-num-nodes=0: decode_failures 97

> warm-num-nodes=25: decode_failures 97

> warm-num-nodes=100: decode_failures 97

> warm-num-nodes=2000: decode_failures 97

### `DG-burst` - burst-loss  `--scenario ridge`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 0.1 | 1 | 0.726 | 0.707 | 0.019 | - | - | 0.888 | 0.893 | 0.470 | 1.20x | 14.3/20.2/22.6% | 1.9/4.4% | 3 |
| 0.2 | 1 | 0.630 | 0.600 | 0.029 | - | - | 0.847 | 0.868 | 0.410 | 1.10x | 13.1/18.8/21.4% | 1.7/4.0% | 3 |
| 0.3 | 1 | 0.516 | 0.488 | 0.028 | - | - | 0.711 | 0.793 | 0.290 | 1.00x | 12.2/17.0/19.5% | 1.6/3.4% | 3 |

> burst-loss=0.2: decode_failures 42

> burst-loss=0.3: decode_failures 37

### `DG-loss` - extra-loss  `--scenario ridge`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 0.1 | 1 | 0.792 | 0.778 | 0.013 | - | - | 0.915 | 0.916 | 0.545 | 1.32x | 15.6/21.9/24.1% | 2.0/4.7% | 3 |
| 0.2 | 1 | 0.745 | 0.727 | 0.018 | - | - | 0.902 | 0.903 | 0.477 | 1.35x | 16.2/22.1/24.6% | 2.1/4.6% | 3 |
| 0.3 | 1 | 0.687 | 0.669 | 0.019 | - | - | 0.858 | 0.866 | 0.394 | 1.34x | 16.1/21.9/24.4% | 2.1/4.3% | 3 |

> extra-loss=0.2: decode_failures 1

### `DG-outage` - burst-loss  `--scenario ridge`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 0.1 | 1 | 0.727 | 0.709 | 0.018 | - | - | 0.904 | 0.925 | 0.487 | 1.19x | 14.1/19.9/22.5% | 1.9/4.5% | 3 |
| 0.2 | 1 | 0.603 | 0.579 | 0.023 | - | - | 0.795 | 0.850 | 0.328 | 1.12x | 13.5/19.1/21.7% | 1.7/4.3% | 3 |
| 0.3 | 1 | 0.488 | 0.469 | 0.019 | - | - | 0.618 | 0.774 | 0.304 | 1.03x | 12.6/17.1/19.9% | 1.6/3.1% | 3 |

> burst-loss=0.1: decode_failures 42

> burst-loss=0.2: decode_failures 23

> burst-loss=0.3: decode_failures 24

### `DM-mode` - dm-mode  `--scenario ridge`

*How a DM escalates to flooding.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 1 | 0.791 | 0.791 | 0.000 | - | - | 0.905 | 0.907 | 0.510 | 1.68x | 19.5/28.1/30.9% | 2.5/6.3% | 3 |
| directed-with-late-flood | 1 | 0.801 | 0.801 | 0.000 | - | - | 0.926 | 0.929 | 0.518 | 1.52x | 17.9/25.6/28.2% | 2.3/5.9% | 3 |
| m4-early-flood | 1 | 0.798 | 0.798 | 0.000 | - | - | 0.920 | 0.925 | 0.532 | 1.51x | 17.7/25.6/28.2% | 2.3/5.9% | 3 |

### `FW-firmware` - profile  `--scenario ridge`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 1 | 0.874 | 0.865 | 0.010 | - | - | 0.983 | 0.985 | 0.422 | 0.70x | 8.3/11.2/12.6% | 1.1/1.9% | 3 |
| 2.8 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |

### `FW-mixed` - legacy-fraction  `--scenario ridge`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 0.25 | 1 | 0.837 | 0.831 | 0.006 | - | - | 0.959 | 0.959 | 0.557 | 1.16x | 13.2/20.1/23.8% | 1.6/4.6% | 3 |
| 0.5 | 1 | 0.883 | 0.869 | 0.013 | - | - | 0.962 | 0.972 | 0.602 | 0.98x | 12.9/16.3/19.7% | 1.5/4.0% | 3 |
| 0.75 | 1 | 0.831 | 0.816 | 0.015 | - | - | 0.966 | 0.968 | 0.310 | 0.83x | 10.3/12.8/13.9% | 1.3/3.1% | 3 |

> legacy-fraction=0.5: decode_failures 3

### `FW-mixed-26` - legacy-fraction  `--scenario ridge`

*The same with the older share on 2.6.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 0.25 | 1 | 0.836 | 0.830 | 0.006 | - | - | 0.943 | 0.945 | 0.527 | 1.14x | 13.0/19.5/23.6% | 1.6/4.5% | 3 |
| 0.5 | 1 | 0.883 | 0.873 | 0.011 | - | - | 0.966 | 0.970 | 0.561 | 0.96x | 12.6/15.9/19.9% | 1.4/4.0% | 3 |
| 0.75 | 1 | 0.820 | 0.804 | 0.016 | - | - | 0.955 | 0.956 | 0.275 | 0.80x | 10.2/12.6/13.3% | 1.2/3.1% | 3 |

### `FW-signing-cost` - profile-flag  `--scenario ridge`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 1 | 0.881 | 0.874 | 0.007 | - | - | 0.969 | 0.970 | 0.572 | 0.68x | 8.3/12.2/13.8% | 1.0/2.8% | 3 |
| signing=true | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |

### `FW-versions` - profile  `--scenario ridge`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 1 | 0.874 | 0.866 | 0.008 | - | - | 0.985 | 0.986 | 0.383 | 0.70x | 8.8/11.9/14.0% | 1.0/2.3% | 3 |
| 2.5 | 1 | 0.872 | 0.864 | 0.008 | - | - | 0.975 | 0.977 | 0.406 | 0.73x | 9.2/12.3/14.5% | 1.1/2.4% | 3 |
| 2.6 | 1 | 0.880 | 0.872 | 0.008 | - | - | 0.982 | 0.982 | 0.410 | 0.71x | 9.0/12.4/14.5% | 1.0/2.5% | 3 |
| 2.7 | 1 | 0.892 | 0.886 | 0.006 | - | - | 0.986 | 0.987 | 0.420 | 0.69x | 8.8/12.8/15.0% | 0.9/3.0% | 3 |
| 2.8 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |

### `LD-chatty` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval driven down to three times its default rate.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.870 | 0.862 | 0.008 | - | - | 0.959 | 0.960 | 0.599 | 0.88x | 10.3/14.6/16.0% | 1.3/3.4% | 3 |
| 900 | 1 | 0.785 | 0.770 | 0.015 | - | - | 0.900 | 0.903 | 0.523 | 2.02x | 23.6/33.3/36.3% | 3.1/7.5% | 3 |
| 300 | 1 | 0.536 | 0.515 | 0.021 | - | - | 0.678 | 0.706 | 0.337 | 4.44x | 49.0/64.6/68.3% | 7.0/14.7% | 3 |

> broadcast-interval-s=300: decode_failures 25

### `LD-chatty-hops` - broadcast-interval-s  `--scenario ridge`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 1 | 0.916 | 0.912 | 0.004 | - | - | 0.974 | 0.974 | 0.671 | 1.00x | 12.1/15.7/17.0% | 1.5/3.5% | 3 |
| 900 | 1 | 0.853 | 0.845 | 0.008 | - | - | 0.933 | 0.934 | 0.647 | 2.25x | 26.5/35.8/38.2% | 3.4/7.8% | 3 |
| 300 | 1 | 0.566 | 0.552 | 0.014 | - | - | 0.692 | 0.701 | 0.395 | 4.96x | 55.1/69.0/72.6% | 7.9/15.8% | 3 |

> broadcast-interval-s=300: decode_failures 6

### `LD-diurnal` - diurnal  `--scenario ridge`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 1 | 0.862 | 0.854 | 0.009 | - | - | 0.958 | 0.959 | 0.582 | 1.23x | 14.4/20.3/22.2% | 1.9/4.7% | 3 |
| sinusoid | 1 | 0.860 | 0.851 | 0.009 | - | - | 0.960 | 0.964 | 0.574 | 1.19x | 13.9/19.7/21.5% | 1.7/4.5% | 3 |
| commuter | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario ridge`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 1 | 0.785 | 0.770 | 0.015 | - | - | 0.900 | 0.903 | 0.523 | 2.02x | 23.6/33.3/36.3% | 3.1/7.5% | 3 |
| 3600 | 1 | 0.870 | 0.862 | 0.008 | - | - | 0.959 | 0.960 | 0.599 | 0.88x | 10.3/14.6/16.0% | 1.3/3.4% | 3 |
| 10800 | 1 | 0.881 | 0.875 | 0.007 | - | - | 0.964 | 0.965 | 0.604 | 0.61x | 7.1/10.1/10.9% | 0.9/2.3% | 3 |
| 43200 | 1 | 0.895 | 0.889 | 0.006 | - | - | 0.978 | 0.978 | 0.609 | 0.44x | 5.1/7.3/8.0% | 0.6/1.7% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario ridge`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 0.25 | 1 | 0.831 | 0.820 | 0.011 | - | - | 0.939 | 0.940 | 0.549 | 1.38x | 16.1/23.1/25.3% | 2.1/5.2% | 3 |
| 1.0 | 1 | 0.816 | 0.803 | 0.013 | - | - | 0.921 | 0.921 | 0.526 | 1.49x | 17.5/25.1/27.6% | 2.3/5.7% | 3 |
| 4.0 | 1 | 0.782 | 0.764 | 0.017 | - | - | 0.906 | 0.908 | 0.531 | 1.84x | 21.8/30.7/34.5% | 2.9/7.1% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario ridge`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.740 | 0.727 | 0.013 | - | - | 0.869 | 0.893 | 0.481 | 5.48x | 58.0/72.9/77.9% | 4.1/12.2% | 3 |
| 1.0 | 1 | 0.631 | 0.619 | 0.012 | - | - | 0.759 | 0.793 | 0.405 | 6.36x | 63.8/75.8/80.2% | 4.8/13.8% | 3 |

> traceroute-per-hour=0.0: decode_failures 97

> traceroute-per-hour=1.0: queue drops 17.4% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 93

### `MS-density` - nodes  `--scenario ridge`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.620 | 0.602 | 0.018 | - | - | 0.805 | 0.812 | 0.086 | 1.20x | 16.6/25.9/31.4% | 2.6/6.6% | 3 |
| 60 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 90 | 1 | 0.928 | 0.924 | 0.003 | - | - | 0.994 | 0.995 | 0.598 | 1.46x | 17.4/23.2/26.0% | 1.3/4.9% | 3 |
| 120 | 1 | 0.940 | 0.936 | 0.004 | - | - | 0.994 | 0.994 | 0.685 | 1.95x | 22.1/35.7/40.0% | 1.3/5.0% | 3 |
| 150 | 1 | 0.955 | 0.953 | 0.002 | - | - | 0.998 | 0.998 | 0.707 | 2.55x | 27.7/37.4/41.8% | 1.3/5.5% | 3 |

> nodes=120: misdecodes 1

> nodes=150: misdecodes 2

### `MS-hopscale` - nodes  `--scenario ridge`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 120 | 1 | 0.710 | 0.699 | 0.010 | - | - | 0.823 | 0.836 | 0.302 | 2.15x | 14.8/20.8/24.3% | 1.5/4.8% | 3 |
| 250 | 1 | 0.462 | 0.448 | 0.015 | - | - | 0.682 | 0.685 | 0.164 | 4.89x | 15.9/29.7/40.1% | 1.6/5.5% | 3 |
| 500 | 1 | 0.294 | 0.288 | 0.006 | - | - | 0.516 | 0.517 | 0.102 | 10.04x | 17.9/29.6/46.0% | 1.7/6.7% | 3 |

> nodes=120: decode_failures 75

> nodes=250: decode_failures 30

> nodes=500: decode_failures 53

### `MS-oversubscribed` - nodes  `--scenario ridge`

*Mesh size against a store that has to hold it, over a full day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 1 | 0.724 | 0.713 | 0.011 | - | - | 0.836 | 0.842 | 0.325 | 2.02x | 13.9/19.4/22.3% | 1.4/4.3% | 3 |
| 250 | 1 | 0.458 | 0.444 | 0.015 | - | - | 0.681 | 0.689 | 0.170 | 4.56x | 14.8/28.3/38.2% | 1.5/5.2% | 3 |
| 500 | 1 | 0.295 | 0.289 | 0.006 | - | - | 0.518 | 0.519 | 0.098 | 9.31x | 16.7/27.5/42.1% | 1.6/5.9% | 3 |

> nodes=120: decode_failures 1

> nodes=250: decode_failures 45

> nodes=500: decode_failures 12

### `MS-roles` - role-mix  `--scenario ridge`

*The legacy default role census against a real mesh's.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.830 | 0.821 | 0.009 | - | - | 0.960 | 0.961 | 0.578 | 1.30x | 15.1/22.0/24.0% | 2.0/5.0% | 3 |
| baymesh-2026-08 | 1 | 0.810 | 0.797 | 0.013 | - | - | 0.942 | 0.946 | 0.590 | 1.16x | 13.7/19.0/21.4% | 1.9/4.5% | 3 |

### `MS-roles-fav` - role-mix  `--scenario ridge`

*The same with router favourites on.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 1 | 0.835 | 0.825 | 0.010 | - | - | 0.971 | 0.975 | 0.575 | 1.32x | 15.3/22.2/24.4% | 2.0/5.1% | 3 |
| baymesh-2026-08 | 1 | 0.849 | 0.840 | 0.009 | - | - | 0.945 | 0.947 | 0.670 | 1.28x | 15.4/21.2/24.2% | 2.1/4.6% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario ridge`

*The share of nodes on ROUTER_LATE.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 0.05 | 1 | 0.842 | 0.832 | 0.010 | - | - | 0.932 | 0.933 | 0.548 | 1.36x | 16.4/24.1/28.2% | 1.9/4.9% | 3 |
| 0.1 | 1 | 0.852 | 0.842 | 0.011 | - | - | 0.936 | 0.938 | 0.646 | 1.48x | 18.2/27.7/30.7% | 2.0/4.8% | 3 |
| 0.2 | 1 | 0.855 | 0.846 | 0.009 | - | - | 0.908 | 0.909 | 0.591 | 1.63x | 20.4/29.2/32.7% | 2.2/4.8% | 3 |

### `MS-siting` - siting-mix  `--scenario ridge`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| local-typical | 1 | 0.515 | 0.508 | 0.007 | - | - | 0.717 | 0.720 | 0.000 | 1.25x | 11.2/19.0/24.7% | 1.8/4.8% | 3 |
| event | 1 | 0.230 | 0.230 | 0.000 | - | - | 0.322 | 0.324 | 0.000 | 1.41x | 7.3/15.9/23.3% | 2.1/4.9% | 3 |
| backbone | 1 | 0.966 | 0.965 | 0.001 | - | - | 0.996 | 0.998 | 0.516 | 1.03x | 25.7/31.4/32.8% | 1.3/5.4% | 3 |

### `MS-size` - nodes  `--scenario ridge`

*Mesh size with density held constant - the area grows with the node count.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 1 | 0.803 | 0.794 | 0.009 | - | - | 0.926 | 0.930 | 0.453 | 1.21x | 22.0/28.0/33.8% | 2.6/7.4% | 3 |
| 60 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 90 | 1 | 0.770 | 0.754 | 0.017 | - | - | 0.879 | 0.887 | 0.000 | 1.51x | 14.1/19.3/23.3% | 1.4/4.6% | 3 |
| 120 | 1 | 0.710 | 0.699 | 0.010 | - | - | 0.823 | 0.836 | 0.302 | 2.15x | 14.8/20.8/24.3% | 1.5/4.8% | 3 |
| 150 | 1 | 0.656 | 0.638 | 0.017 | - | - | 0.816 | 0.816 | 0.263 | 2.75x | 15.7/22.3/29.2% | 1.6/4.7% | 3 |

> nodes=90: decode_failures 2

> nodes=120: decode_failures 75

> slower: 7.99 s per simulated hour against 3.4 over 34 prior run(s) - 2.3x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `MS-stretch` - stretch  `--scenario ridge`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 1.25 | 1 | 0.496 | 0.488 | 0.008 | - | - | 0.710 | 0.712 | 0.249 | 1.47x | 13.0/20.1/22.5% | 2.2/5.0% | 3 |
| 1.5 | 1 | 0.356 | 0.352 | 0.004 | - | - | 0.584 | 0.587 | 0.000 | 1.33x | 10.3/16.6/21.0% | 1.9/4.9% | 3 |
| 2.0 | 1 | 0.141 | 0.140 | 0.001 | - | - | 0.211 | 0.215 | 0.000 | 0.88x | 5.0/7.9/9.1% | 1.5/2.4% | 3 |

### `MS-topology` - topology  `--scenario ridge`

*The shape of the mesh, at fixed node count and seed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| clustered | 1 | 0.861 | 0.858 | 0.003 | - | - | 0.939 | 0.940 | 0.000 | 1.14x | 22.1/29.5/31.2% | 1.7/5.4% | 3 |
| corridor | 1 | 0.562 | 0.525 | 0.037 | - | - | 0.776 | 0.794 | 0.200 | 1.29x | 15.9/19.0/22.5% | 1.8/5.0% | 3 |
| hub | 1 | 0.899 | 0.893 | 0.006 | - | - | 0.985 | 0.985 | 0.473 | 1.25x | 23.9/33.5/35.2% | 1.8/5.4% | 3 |

> topology=corridor: decode_failures 16

### `PR-crladder` - coding-rate-ladder  `--scenario ridge`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.801 | 0.801 | 0.000 | - | - | 0.926 | 0.929 | 0.518 | 1.52x | 17.9/25.6/28.2% | 2.3/5.9% | 3 |
| True | 1 | 0.803 | 0.803 | 0.000 | - | - | 0.923 | 0.926 | 0.509 | 1.55x | 18.0/26.3/28.8% | 2.4/6.1% | 3 |

### `PR-dmmode-cr` - dm-mode  `--scenario ridge`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 1 | 0.803 | 0.803 | 0.000 | - | - | 0.923 | 0.926 | 0.509 | 1.55x | 18.0/26.3/28.8% | 2.4/6.1% | 3 |
| m4-early-flood | 1 | 0.798 | 0.798 | 0.000 | - | - | 0.912 | 0.920 | 0.518 | 1.54x | 17.9/26.0/28.7% | 2.3/6.0% | 3 |

### `PR-protocol` - protocol  `--scenario ridge`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.827 | 0.827 | 0.000 | - | - | 0 | 0.000 | 0.556 | 1.26x | 15.0/21.1/22.9% | 1.9/4.7% | 3 |
| chain | 1 | 0.812 | 0.807 | 0.005 | - | - | 0.870 | 0.932 | 0.529 | 1.43x | 16.6/24.7/27.2% | 2.2/5.6% | 3 |
| sr | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |

### `PR-repeats` - extra-repeats  `--scenario ridge`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| True | 1 | 0.839 | 0.829 | 0.010 | - | - | 0.940 | 0.942 | 0.606 | 1.29x | 15.1/21.5/23.6% | 2.0/4.8% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario ridge`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.940 | 0.936 | 0.004 | - | - | 0.994 | 0.994 | 0.685 | 1.95x | 22.1/35.7/40.0% | 1.3/5.0% | 3 |
| True | 1 | 0.943 | 0.939 | 0.004 | - | - | 0.995 | 0.995 | 0.680 | 1.92x | 21.8/34.8/39.1% | 1.3/4.8% | 3 |

> extra-repeats=False: misdecodes 1

### `RF-bw500` - preset  `--scenario ridge`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 1 | 0.124 | 0.124 | 0.000 | - | - | 0.163 | 0.163 | 0.000 | 0.04x | 0.2/0.4/0.5% | 0.1/0.1% | 3 |
| MEDIUM_TURBO | 1 | 0.412 | 0.409 | 0.003 | - | - | 0.664 | 0.665 | 0.000 | 0.24x | 1.9/3.2/4.1% | 0.4/1.0% | 3 |
| LONG_TURBO | 1 | 0.770 | 0.762 | 0.009 | - | - | 0.874 | 0.875 | 0.462 | 1.21x | 11.4/17.0/19.4% | 1.8/4.2% | 3 |

### `RF-duct` - duct-per-hour  `--scenario ridge`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 0.25 | 1 | 0.835 | 0.823 | 0.012 | - | - | 0.938 | 0.939 | 0.584 | 1.23x | 15.9/22.2/24.1% | 1.8/4.9% | 3 |
| 1.0 | 1 | 0.922 | 0.913 | 0.008 | - | - | 0.980 | 0.981 | 0.791 | 0.83x | 19.2/23.6/24.1% | 1.0/4.6% | 3 |

### `RF-eu-presets` - preset  `--scenario ridge`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.266 | 0.266 | 0.000 | - | - | 0.332 | 0.332 | 0.000 | 0.12x | 0.8/1.5/1.7% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| LITE_FAST | 1 | 0.761 | 0.736 | 0.025 | - | - | 0.926 | 0.926 | 0.395 | 0.93x | 10.0/15.1/16.3% | 1.4/3.6% | 3 |
| NARROW_SLOW | 1 | 0.800 | 0.780 | 0.021 | - | - | 0.947 | 0.947 | 0.387 | 1.19x | 13.4/17.8/19.7% | 1.8/4.4% | 3 |

### `RF-noise` - noise-profile  `--scenario ridge`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| temporal | 1 | 0.715 | 0.697 | 0.018 | - | - | 0.852 | 0.855 | 0.401 | 1.22x | 14.1/20.3/22.4% | 1.9/4.4% | 3 |
| transient | 1 | 0.827 | 0.816 | 0.011 | - | - | 0.929 | 0.930 | 0.557 | 1.29x | 15.1/21.7/23.6% | 2.0/4.9% | 3 |
| periodic | 1 | 0.677 | 0.666 | 0.012 | - | - | 0.790 | 0.792 | 0.467 | 1.18x | 13.9/19.6/21.6% | 1.8/4.2% | 3 |

### `RF-preset` - preset  `--scenario ridge`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 1 | 0.266 | 0.266 | 0.000 | - | - | 0.332 | 0.332 | 0.000 | 0.12x | 0.8/1.5/1.7% | 0.2/0.5% | 3 |
| LONG_FAST | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| LONG_MODERATE | 1 | 0.849 | 0.831 | 0.018 | - | - | 0.955 | 0.980 | 0.719 | 3.10x | 42.8/54.1/60.1% | 4.4/12.1% | 3 |

> preset=LONG_MODERATE: decode_failures 11

### `RF-preset-turbo` - preset  `--scenario ridge`

*Presets from the fastest the firmware ships to the slow end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| EXTRA_SHORT_TURBO | 1 | 0.058 | 0.058 | 0.000 | - | - | 0.117 | 0.118 | 0.000 | 0.01x | 0.0/0.1/0.1% | 0.0/0.0% | 3 |
| SHORT_TURBO | 1 | 0.124 | 0.124 | 0.000 | - | - | 0.163 | 0.163 | 0.000 | 0.04x | 0.2/0.4/0.5% | 0.1/0.1% | 3 |
| LONG_FAST | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| LONG_TURBO | 1 | 0.770 | 0.762 | 0.009 | - | - | 0.874 | 0.875 | 0.462 | 1.21x | 11.4/17.0/19.4% | 1.8/4.2% | 3 |
| EXTRA_LONG_TURBO | 1 | 0.811 | 0.798 | 0.013 | - | - | 0.925 | 0.928 | 0.482 | 1.79x | 19.3/28.4/30.5% | 2.7/6.5% | 3 |

### `RF-pulse` - noise-pulse-interval-ms  `--scenario ridge`

*How often the periodic emitter fires.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 1 | 0.780 | 0.767 | 0.013 | - | - | 0.889 | 0.894 | 0.539 | 1.25x | 14.8/21.3/23.2% | 1.9/4.6% | 3 |
| 10000 | 1 | 0.677 | 0.666 | 0.012 | - | - | 0.790 | 0.792 | 0.467 | 1.18x | 13.9/19.6/21.6% | 1.8/4.2% | 3 |
| 4000 | 1 | 0.395 | 0.389 | 0.006 | - | - | 0.465 | 0.504 | 0.229 | 0.99x | 12.1/16.1/18.1% | 1.6/3.0% | 3 |
| 2000 | 1 | 0.098 | 0.098 | 0.000 | - | - | 0.104 | 0.162 | 0.046 | 0.71x | 8.9/11.8/13.5% | 1.1/1.9% | 3 |

### `RF-stretch-duct` - duct-per-hour  `--scenario ridge`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 1 | 0.356 | 0.352 | 0.004 | - | - | 0.584 | 0.587 | 0.000 | 1.33x | 10.3/16.6/21.0% | 1.9/4.9% | 3 |
| 1.0 | 1 | 0.668 | 0.661 | 0.006 | - | - | 0.788 | 0.789 | 0.286 | 0.87x | 14.4/18.5/20.1% | 1.2/4.2% | 3 |

### `RF-txpower` - tx-power  `--scenario ridge`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 22 | 1 | 0.388 | 0.383 | 0.005 | - | - | 0.601 | 0.601 | 0.000 | 1.33x | 10.5/16.0/18.7% | 2.1/4.9% | 3 |
| 17 | 1 | 0.126 | 0.126 | 0.000 | - | - | 0.159 | 0.161 | 0.000 | 0.82x | 4.1/8.7/10.5% | 1.3/3.3% | 3 |
| 14 | 1 | 0.075 | 0.074 | 0.001 | - | - | 0.140 | 0.148 | 0.000 | 0.62x | 3.0/4.9/6.0% | 1.1/1.8% | 3 |

> tx-power=14: decode_failures 5

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario ridge`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.940 | 0.936 | 0.004 | - | - | 0.994 | 0.994 | 0.685 | 1.95x | 22.1/35.7/40.0% | 1.3/5.0% | 3 |
| True | 1 | 0.931 | 0.926 | 0.005 | - | - | 0.988 | 0.988 | 0.650 | 2.32x | 25.9/40.1/44.8% | 1.5/5.5% | 3 |

> no-adopt-hop-recommendation=False: misdecodes 1

### `RT-favourites` - favourite-routers  `--scenario ridge`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.845 | 0.835 | 0.009 | - | - | 0.934 | 0.935 | 0.604 | 1.35x | 16.0/23.9/27.3% | 1.9/5.0% | 3 |
| True | 1 | 0.868 | 0.859 | 0.009 | - | - | 0.942 | 0.943 | 0.655 | 1.37x | 15.9/24.2/27.4% | 2.0/4.9% | 3 |

### `RT-hopassign` - hop-assign  `--scenario ridge`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| random | 1 | 0.832 | 0.822 | 0.011 | - | - | 0.956 | 0.957 | 0.574 | 1.30x | 15.4/21.4/23.3% | 1.9/4.7% | 3 |

### `RT-hoplimit` - hop-limit  `--scenario ridge`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.661 | 0.622 | 0.039 | - | - | 0.785 | 0.789 | 0.291 | 1.01x | 12.4/17.2/19.4% | 1.4/4.0% | 3 |
| 7 | 1 | 0.884 | 0.877 | 0.006 | - | - | 0.950 | 0.951 | 0.662 | 1.48x | 17.4/23.8/25.8% | 2.2/5.2% | 3 |
| 15 | 1 | 0.938 | 0.937 | 0.001 | - | - | 0.971 | 0.971 | 0.746 | 1.47x | 17.4/23.1/25.1% | 2.2/5.0% | 3 |
| 32 | 1 | 0.924 | 0.923 | 0.001 | - | - | 0.963 | 0.963 | 0.723 | 1.48x | 17.4/23.4/25.4% | 2.2/5.1% | 3 |

> hop-limit=3: decode_failures 5

### `RT-hopspread` - hop-limit  `--scenario ridge`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.661 | 0.622 | 0.039 | - | - | 0.785 | 0.789 | 0.291 | 1.01x | 12.4/17.2/19.4% | 1.4/4.0% | 3 |
| 5 | 1 | 0.833 | 0.817 | 0.017 | - | - | 0.922 | 0.923 | 0.520 | 1.31x | 15.8/21.3/23.4% | 2.0/4.9% | 3 |
| 7 | 1 | 0.884 | 0.877 | 0.006 | - | - | 0.950 | 0.951 | 0.662 | 1.48x | 17.4/23.8/25.8% | 2.2/5.2% | 3 |

> hop-limit=3: decode_failures 5

### `RT-rebroadcast` - rebroadcast-mode  `--scenario ridge`

*The rebroadcast mode - what a node relays.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| KNOWN_ONLY | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| CORE_PORTNUMS_ONLY | 1 | 0.826 | 0.826 | 0.000 | - | - | 0.856 | 0.937 | 0.539 | 1.27x | 15.0/21.1/23.0% | 1.9/4.7% | 3 |

### `RT-spread` - hop-spread  `--scenario ridge`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.661 | 0.622 | 0.039 | - | - | 0.785 | 0.789 | 0.291 | 1.01x | 12.4/17.2/19.4% | 1.4/4.0% | 3 |
| True | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |

> hop-spread=False: decode_failures 5

### `SC-signing` - signature-policy  `--scenario ridge`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| BALANCED | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| STRICT | 1 | 0.665 | 0.665 | 0.000 | - | - | 0.753 | 0.757 | 0.396 | 1.42x | 16.9/23.4/25.7% | 2.2/5.2% | 3 |

### `SF-advert-transport` - advert-transport  `--scenario ridge`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| dm | 1 | 0.839 | 0.826 | 0.013 | - | - | 0.936 | 0.937 | 0.568 | 1.28x | 14.8/21.5/23.6% | 2.0/4.9% | 3 |

### `SF-bucket-mode` - bucket-mode  `--scenario ridge`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 1 | 0.829 | 0.815 | 0.014 | - | - | 0.935 | 0.940 | 0.562 | 1.31x | 15.4/21.9/23.9% | 2.0/5.0% | 3 |
| local | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| time | 1 | 0.832 | 0.821 | 0.011 | - | - | 0.938 | 0.941 | 0.519 | 1.32x | 15.3/22.2/24.2% | 2.0/5.0% | 3 |
| window | 1 | 0.840 | 0.826 | 0.014 | - | - | 0.947 | 0.949 | 0.579 | 1.28x | 15.1/21.4/23.5% | 2.0/4.8% | 3 |

> bucket-mode=global: misdecodes 42

> bucket-mode=time: misdecodes 25

> bucket-mode=window: misdecodes 24

### `SF-bucket-time` - time-bucket-s  `--scenario ridge`

*Width of the time bucket, when buckets are cut by the clock.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 1 | 0.829 | 0.814 | 0.015 | - | - | 0.940 | 0.943 | 0.551 | 1.43x | 16.5/24.2/26.4% | 2.1/5.6% | 3 |
| 1800 | 1 | 0.832 | 0.821 | 0.011 | - | - | 0.938 | 0.941 | 0.519 | 1.32x | 15.3/22.2/24.2% | 2.0/5.0% | 3 |
| 3600 | 1 | 0.838 | 0.826 | 0.011 | - | - | 0.939 | 0.943 | 0.584 | 1.28x | 14.9/21.4/23.4% | 1.9/4.8% | 3 |

> time-bucket-s=600: misdecodes 126

> time-bucket-s=1800: misdecodes 25

> time-bucket-s=3600: misdecodes 9

### `SF-cadence` - trigger  `--scenario ridge`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| interval | 1 | 0.819 | 0.806 | 0.013 | - | - | 0.923 | 0.932 | 0.544 | 1.64x | 19.2/28.6/32.1% | 2.5/7.1% | 3 |
| aimd | 1 | 0.830 | 0.827 | 0.003 | - | - | 0.880 | 0.949 | 0.562 | 1.29x | 15.1/21.7/23.8% | 1.9/4.9% | 3 |
| bucket+interval | 1 | 0.810 | 0.794 | 0.016 | - | - | 0.921 | 0.921 | 0.540 | 1.66x | 19.3/28.6/32.4% | 2.6/7.1% | 3 |

> trigger=interval: misdecodes 9

> trigger=interval: decode_failures 3

> trigger=aimd: misdecodes 3

> trigger=bucket+interval: misdecodes 12

### `SF-capacity` - capacity  `--scenario ridge`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.836 | 0.824 | 0.012 | - | - | 0.936 | 0.942 | 0.573 | 1.28x | 14.9/21.7/23.7% | 1.9/4.9% | 3 |
| 8 | 1 | 0.839 | 0.825 | 0.013 | - | - | 0.947 | 0.948 | 0.584 | 1.28x | 15.0/21.6/23.5% | 1.9/4.9% | 3 |
| 16 | 1 | 0.832 | 0.822 | 0.010 | - | - | 0.935 | 0.937 | 0.551 | 1.28x | 14.9/21.5/23.6% | 1.9/4.8% | 3 |
| 32 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 50 | 1 | 0.838 | 0.827 | 0.011 | - | - | 0.942 | 0.946 | 0.580 | 1.29x | 15.3/21.7/23.5% | 2.0/4.9% | 3 |

> capacity=4: decode_failures 94

> capacity=8: decode_failures 59

> capacity=16: decode_failures 2

### `SF-capacity-local` - capacity  `--scenario ridge`

*Sketch capacity under local numbering and the later defaults.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 1 | 0.836 | 0.824 | 0.012 | - | - | 0.936 | 0.942 | 0.573 | 1.28x | 14.9/21.7/23.7% | 1.9/4.9% | 3 |
| 8 | 1 | 0.839 | 0.825 | 0.013 | - | - | 0.947 | 0.948 | 0.584 | 1.28x | 15.0/21.6/23.5% | 1.9/4.9% | 3 |
| 16 | 1 | 0.832 | 0.822 | 0.010 | - | - | 0.935 | 0.937 | 0.551 | 1.28x | 14.9/21.5/23.6% | 1.9/4.8% | 3 |
| 32 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 50 | 1 | 0.838 | 0.827 | 0.011 | - | - | 0.942 | 0.946 | 0.580 | 1.29x | 15.3/21.7/23.5% | 2.0/4.9% | 3 |

> capacity=4: decode_failures 94

> capacity=8: decode_failures 59

> capacity=16: decode_failures 2

### `SF-capacity-window` - capacity  `--scenario ridge`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.838 | 0.828 | 0.010 | - | - | 0.928 | 0.944 | 0.569 | 1.30x | 15.3/21.7/23.8% | 1.9/4.9% | 3 |
| 16 | 1 | 0.837 | 0.824 | 0.013 | - | - | 0.938 | 0.941 | 0.558 | 1.27x | 15.0/21.2/23.2% | 1.9/4.8% | 3 |
| 32 | 1 | 0.840 | 0.826 | 0.014 | - | - | 0.947 | 0.949 | 0.579 | 1.28x | 15.1/21.4/23.5% | 2.0/4.8% | 3 |

> capacity=8: misdecodes 20

> capacity=8: decode_failures 40

> capacity=16: misdecodes 18

> capacity=16: decode_failures 2

> capacity=32: misdecodes 24

### `SF-catchup` - catch-up-hours  `--scenario ridge`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 1 | 0.810 | 0.794 | 0.016 | - | - | 0.921 | 0.921 | 0.540 | 1.66x | 19.3/28.6/32.4% | 2.6/7.1% | 3 |
| 02-06 | 1 | 0.835 | 0.829 | 0.007 | - | - | 0.912 | 0.949 | 0.578 | 1.30x | 15.2/21.9/24.0% | 1.9/5.0% | 3 |
| 00-08 | 1 | 0.839 | 0.833 | 0.007 | - | - | 0.915 | 0.951 | 0.564 | 1.36x | 15.7/23.2/25.5% | 2.0/5.4% | 3 |

> catch-up-hours=: misdecodes 12

> catch-up-hours=02-06: decode_failures 26

> catch-up-hours=00-08: decode_failures 27

### `SF-hops-flat` - hops-apart  `--scenario ridge`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.821 | 0.818 | 0.003 | - | - | 0.915 | 0.915 | 0.540 | 1.28x | 15.2/21.6/23.3% | 2.0/4.8% | 3 |
| 2 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 3 | 1 | 0.857 | 0.834 | 0.023 | - | - | 0.976 | 0.976 | 0.587 | 1.30x | 15.3/21.9/23.5% | 2.0/4.8% | 3 |
| 4 | 1 | 0.856 | 0.823 | 0.033 | - | - | 0.957 | 0.986 | 0.559 | 1.32x | 15.6/21.9/23.8% | 2.0/5.0% | 3 |

> hops-apart=3: decode_failures 1

> hops-apart=4: decode_failures 32

### `SF-hops-spread` - hops-apart  `--scenario ridge`

*How many hops apart the archives are, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.821 | 0.818 | 0.003 | - | - | 0.915 | 0.915 | 0.540 | 1.28x | 15.2/21.6/23.3% | 2.0/4.8% | 3 |
| 2 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 3 | 1 | 0.857 | 0.834 | 0.023 | - | - | 0.976 | 0.976 | 0.587 | 1.30x | 15.3/21.9/23.5% | 2.0/4.8% | 3 |
| 4 | 1 | 0.856 | 0.823 | 0.033 | - | - | 0.957 | 0.986 | 0.559 | 1.32x | 15.6/21.9/23.8% | 2.0/5.0% | 3 |
| 5 | 1 | 0.844 | 0.820 | 0.024 | - | - | 0.881 | 0.974 | 0.570 | 1.30x | 15.2/21.5/23.4% | 1.9/4.9% | 3 |

> hops-apart=3: decode_failures 1

> hops-apart=4: decode_failures 32

> hops-apart=5: decode_failures 31

### `SF-jitter-global` - advert-jitter-s  `--scenario ridge`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.839 | 0.826 | 0.013 | - | - | 0.943 | 0.944 | 0.557 | 1.29x | 15.1/21.6/23.6% | 2.0/4.9% | 3 |
| 30 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 120 | 1 | 0.834 | 0.823 | 0.011 | - | - | 0.940 | 0.941 | 0.563 | 1.29x | 15.2/21.8/23.8% | 2.0/4.9% | 3 |
| 600 | 1 | 0.835 | 0.824 | 0.011 | - | - | 0.938 | 0.939 | 0.552 | 1.31x | 15.5/21.8/24.0% | 2.0/5.0% | 3 |

### `SF-jitter-local` - advert-jitter-s  `--scenario ridge`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 1 | 0.839 | 0.826 | 0.013 | - | - | 0.943 | 0.944 | 0.557 | 1.29x | 15.1/21.6/23.6% | 2.0/4.9% | 3 |
| 30 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 120 | 1 | 0.834 | 0.823 | 0.011 | - | - | 0.940 | 0.941 | 0.563 | 1.29x | 15.2/21.8/23.8% | 2.0/4.9% | 3 |
| 600 | 1 | 0.835 | 0.824 | 0.011 | - | - | 0.938 | 0.939 | 0.552 | 1.31x | 15.5/21.8/24.0% | 2.0/5.0% | 3 |

### `SF-place-flat` - place  `--scenario ridge`

*Where the archives sit, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.854 | 0.825 | 0.029 | - | - | 0.751 | 0.943 | 0.535 | 1.31x | 15.2/21.8/23.7% | 2.0/4.9% | 3 |
| routers | 1 | 0.854 | 0.835 | 0.019 | - | - | 0.962 | 0.977 | 0.546 | 1.28x | 15.4/21.5/23.0% | 1.9/4.9% | 3 |
| alternate-routers | 1 | 0.833 | 0.823 | 0.010 | - | - | 0.958 | 0.958 | 0.540 | 1.29x | 15.2/21.9/23.9% | 2.0/4.9% | 3 |
| beside-router | 1 | 0.840 | 0.822 | 0.017 | - | - | 0.954 | 0.954 | 0.533 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| random-clients | 1 | 0.847 | 0.830 | 0.017 | - | - | 0.904 | 0.916 | 0.552 | 1.30x | 15.7/21.3/23.1% | 1.9/4.7% | 3 |
| hops-apart | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |

> place=spread: decode_failures 21

> place=random-clients: decode_failures 8

### `SF-place-spread` - place  `--scenario ridge`

*Where the archives sit, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 1 | 0.854 | 0.825 | 0.029 | - | - | 0.751 | 0.943 | 0.535 | 1.31x | 15.2/21.8/23.7% | 2.0/4.9% | 3 |
| routers | 1 | 0.854 | 0.835 | 0.019 | - | - | 0.962 | 0.977 | 0.546 | 1.28x | 15.4/21.5/23.0% | 1.9/4.9% | 3 |
| alternate-routers | 1 | 0.833 | 0.823 | 0.010 | - | - | 0.958 | 0.958 | 0.540 | 1.29x | 15.2/21.9/23.9% | 2.0/4.9% | 3 |
| beside-router | 1 | 0.840 | 0.822 | 0.017 | - | - | 0.954 | 0.954 | 0.533 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| random-clients | 1 | 0.847 | 0.830 | 0.017 | - | - | 0.904 | 0.916 | 0.552 | 1.30x | 15.7/21.3/23.1% | 1.9/4.7% | 3 |
| hops-apart | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |

> place=spread: decode_failures 21

> place=random-clients: decode_failures 8

### `SF-provide-transport` - provide-transport  `--scenario ridge`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| broadcast | 1 | 0.862 | 0.824 | 0.038 | - | - | 0.946 | 0.949 | 0.631 | 1.35x | 15.6/22.7/24.7% | 2.1/5.1% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario ridge`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| heard | 1 | 0.841 | 0.827 | 0.014 | - | - | 0.952 | 0.954 | 0.581 | 1.29x | 15.1/21.8/23.8% | 2.0/4.9% | 3 |

> replay-ordering=heard: misdecodes 11

### `SF-replay-order-broadcast` - replay-ordering  `--scenario ridge`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 1 | 0.862 | 0.824 | 0.038 | - | - | 0.946 | 0.949 | 0.631 | 1.35x | 15.6/22.7/24.7% | 2.1/5.1% | 3 |
| heard | 1 | 0.858 | 0.823 | 0.036 | - | - | 0.940 | 0.942 | 0.627 | 1.33x | 15.4/22.6/24.6% | 2.0/5.1% | 3 |

> replay-ordering=heard: misdecodes 6

### `SF-resolve` - resolve  `--scenario ridge`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| enum | 1 | 0.833 | 0.822 | 0.011 | - | - | 0.934 | 0.943 | 0.566 | 1.26x | 14.7/21.3/23.3% | 1.9/4.8% | 3 |
| hybrid | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |

### `SF-servers-allrouters` - servers  `--scenario ridge`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 1 | 0.854 | 0.835 | 0.019 | - | - | 0.962 | 0.977 | 0.546 | 1.28x | 15.4/21.5/23.0% | 1.9/4.9% | 3 |
| 6 | 1 | 0.849 | 0.814 | 0.035 | - | - | 0.977 | 0.982 | 0.554 | 1.33x | 15.6/22.5/24.4% | 2.0/5.1% | 6 |

> servers=6: decode_failures 20

> slower: 4.9 s per simulated hour against 1.85 over 34 prior run(s) - 2.7x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `SF-servers-flat` - servers  `--scenario ridge`

*How many archives the mesh has, under a flat hop limit.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.838 | 0.832 | 0.006 | - | - | 0.916 | 0.921 | 0.570 | 1.28x | 15.0/21.6/23.4% | 1.9/4.7% | 2 |
| 3 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 5 | 1 | 0.833 | 0.816 | 0.017 | - | - | 0.952 | 0.953 | 0.535 | 1.32x | 15.3/22.1/24.1% | 2.0/5.0% | 5 |
| 8 | 1 | 0.840 | 0.820 | 0.021 | - | - | 0.958 | 0.959 | 0.546 | 1.35x | 15.5/22.8/25.0% | 2.0/5.2% | 8 |

### `SF-servers-spread` - servers  `--scenario ridge`

*How many archives the mesh has, under real per-node hop limits.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 1 | 0.838 | 0.832 | 0.006 | - | - | 0.916 | 0.921 | 0.570 | 1.28x | 15.0/21.6/23.4% | 1.9/4.7% | 2 |
| 3 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 5 | 1 | 0.833 | 0.816 | 0.017 | - | - | 0.952 | 0.953 | 0.535 | 1.32x | 15.3/22.1/24.1% | 2.0/5.0% | 5 |
| 8 | 1 | 0.840 | 0.820 | 0.021 | - | - | 0.958 | 0.959 | 0.546 | 1.35x | 15.5/22.8/25.0% | 2.0/5.2% | 8 |

### `SF-signed` - signed  `--scenario ridge`

*Whether the advert carries its 66-byte signature.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| True | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |

### `SF-sr-retries` - sr-retries  `--scenario ridge`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 1 | 0.842 | 0.832 | 0.010 | - | - | 0.940 | 0.941 | 0.560 | 1.23x | 14.5/20.3/22.3% | 1.8/4.7% | 3 |
| 1 | 1 | 0.847 | 0.835 | 0.013 | - | - | 0.954 | 0.954 | 0.574 | 1.21x | 14.3/20.1/22.1% | 1.8/4.6% | 3 |
| 2 | 1 | 0.839 | 0.829 | 0.010 | - | - | 0.935 | 0.936 | 0.560 | 1.22x | 14.3/20.3/22.3% | 1.8/4.6% | 3 |
| 4 | 1 | 0.835 | 0.825 | 0.011 | - | - | 0.935 | 0.940 | 0.559 | 1.22x | 14.3/20.2/22.1% | 1.8/4.7% | 3 |

### `SF-width` - short-id-bits  `--scenario ridge`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 1 | 0.835 | 0.824 | 0.011 | - | - | 0.945 | 0.946 | 0.568 | 1.29x | 15.1/21.7/23.7% | 2.0/4.9% | 3 |
| 24 | 1 | 0.837 | 0.825 | 0.012 | - | - | 0.943 | 0.946 | 0.557 | 1.29x | 15.2/21.6/23.6% | 1.9/4.9% | 3 |
| 32 | 1 | 0.842 | 0.831 | 0.010 | - | - | 0.949 | 0.949 | 0.571 | 1.30x | 15.3/21.8/23.7% | 2.0/4.9% | 3 |
| 64 | 1 | 0.834 | 0.823 | 0.011 | - | - | 0.943 | 0.945 | 0.551 | 1.29x | 15.1/21.6/23.6% | 2.0/4.9% | 3 |

### `SF-window-size` - window-size  `--scenario ridge`

*Objects in the sliding window, when buckets are windowed.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 1 | 0.832 | 0.820 | 0.012 | - | - | 0.939 | 0.940 | 0.546 | 1.34x | 15.4/22.7/24.8% | 2.0/5.1% | 3 |
| 16 | 1 | 0.834 | 0.822 | 0.012 | - | - | 0.939 | 0.942 | 0.562 | 1.31x | 15.2/22.1/24.1% | 2.0/5.0% | 3 |
| 32 | 1 | 0.840 | 0.826 | 0.014 | - | - | 0.947 | 0.949 | 0.579 | 1.28x | 15.1/21.4/23.5% | 2.0/4.8% | 3 |

> window-size=8: misdecodes 117

> window-size=16: misdecodes 48

> window-size=32: misdecodes 24

### `TH-congestion` - no-congestion-scaling  `--scenario ridge`

*The firmware's node-count interval scaling, on against off.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 1 | 0.940 | 0.936 | 0.004 | - | - | 0.994 | 0.994 | 0.685 | 1.95x | 22.1/35.7/40.0% | 1.3/5.0% | 3 |
| True | 1 | 0.734 | 0.719 | 0.014 | - | - | 0.863 | 0.882 | 0.483 | 5.49x | 58.0/72.9/77.8% | 4.0/12.1% | 3 |

> no-congestion-scaling=False: misdecodes 1

> no-congestion-scaling=True: decode_failures 72

### `TH-congestion-input` - congestion-input  `--scenario ridge`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 1 | 0.458 | 0.444 | 0.015 | - | - | 0.681 | 0.689 | 0.170 | 4.56x | 14.8/28.3/38.2% | 1.5/5.2% | 3 |
| truesize | 1 | 0.483 | 0.468 | 0.015 | - | - | 0.710 | 0.722 | 0.180 | 3.28x | 10.4/21.1/28.9% | 1.1/4.1% | 3 |

> congestion-input=hotstore: decode_failures 45

> congestion-input=truesize: decode_failures 59

> slower: 32.7 s per simulated hour against 10.8 over 34 prior run(s) - 3.0x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `TH-congestion-mode` - congestion-mode  `--scenario ridge`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | seeds | text | on air | overheard | DM | admin | held | union | worst node | demand | chutil p50/p90/max | airutil p50/max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 1 | 0.947 | 0.943 | 0.004 | - | - | 0.995 | 0.995 | 0.698 | 1.88x | 21.3/33.5/37.7% | 1.2/4.7% | 3 |
| adaptive | 1 | 0.940 | 0.936 | 0.004 | - | - | 0.994 | 0.994 | 0.685 | 1.95x | 22.1/35.7/40.0% | 1.3/5.0% | 3 |

> congestion-mode=adaptive: misdecodes 1

