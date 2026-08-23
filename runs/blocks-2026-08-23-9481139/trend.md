# Sweep blocks-2026-08-23-9481139

- **sim version** `1.4.0`
- **transport** `591429c`
- **ground** valleys
- **seed base** 9481139 · seeds 9481139
- **blocks** 86 run, 1 missing
- **compute** 11.7 h of simulator time across every cell
- **generated** 2026-08-23T05:09:29+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>83 warnings</summary>

- D-cadence: trigger=interval: misdecodes 12
- D-cadence: trigger=aimd: misdecodes 3
- D-cadence: trigger=bucket+interval: misdecodes 14
- E-capacity: capacity=4: decode_failures 82
- E-capacity: capacity=8: decode_failures 30
- F-burst: burst-loss=0.2: decode_failures 4
- F-burst: burst-loss=0.3: decode_failures 37
- F-outage: burst-loss=0.1: decode_failures 25
- F-outage: burst-loss=0.2: decode_failures 25
- F-outage: burst-loss=0.3: decode_failures 36
- F-txpower: tx-power=22: decode_failures 14
- F-txpower: tx-power=17: decode_failures 15
- G-hops: hops-apart=4: decode_failures 22
- G-place: place=spread: decode_failures 24
- G-place: place=random-clients: decode_failures 6
- J-bucketmode: bucket-mode=global: misdecodes 26
- J-bucketmode: bucket-mode=time: misdecodes 36
- J-bucketmode: bucket-mode=window: misdecodes 30
- J-timewin: time-bucket-s=600: misdecodes 117
- J-timewin: time-bucket-s=1800: misdecodes 36
- J-timewin: time-bucket-s=3600: misdecodes 10
- J-wincap: capacity=8: misdecodes 28
- J-wincap: capacity=8: decode_failures 17
- J-wincap: capacity=16: misdecodes 28
- J-wincap: capacity=32: misdecodes 30
- J-window: window-size=8: misdecodes 105
- J-window: window-size=16: misdecodes 61
- J-window: window-size=32: misdecodes 30
- K-size: nodes=40: decode_failures 4
- M-capacity: capacity=4: decode_failures 82
- M-capacity: capacity=8: decode_failures 30
- M-combined: replay-ordering=heard: misdecodes 3
- M-replayorder: replay-ordering=heard: misdecodes 23
- N-hops: hops-apart=4: decode_failures 22
- N-hops: hops-apart=5: decode_failures 35
- N-place: place=spread: decode_failures 24
- N-place: place=random-clients: decode_failures 6
- P-bw500: preset=SHORT_TURBO: decode_failures 9
- P-catchup: catch-up-hours=: misdecodes 14
- P-catchup: catch-up-hours=02-06: decode_failures 44
- P-catchup: catch-up-hours=00-08: decode_failures 42
- P-congestion: no-congestion-scaling=True: queue drops 12.6% of transmissions - airtime here is measured through a cap
- P-congestion: no-congestion-scaling=True: decode_failures 61
- P-eu-presets: preset=SHORT_FAST: decode_failures 2
- P-preset: preset=SHORT_FAST: decode_failures 2
- P-preset: preset=LONG_MODERATE: decode_failures 4
- Q-topology: topology=clustered: decode_failures 18
- Q-topology: slower: 3.6 s per simulated hour against 1.67 over 2 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright
- R-congestion-input: congestion-input=hotstore: decode_failures 13
- R-congestion-input: congestion-input=truesize: decode_failures 6
- R-favourites: faster: 0.999 s per simulated hour against 2.08 over 2 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- R-hopscale: nodes=250: decode_failures 22
- R-hopscale: nodes=500: decode_failures 120
- R-hotstore-stress: max-num-nodes=10: decode_failures 105
- R-hotstore-stress: max-num-nodes=120: decode_failures 13
- R-hotstore-stress: max-num-nodes=250: decode_failures 1
- R-oversubscribed: nodes=250: decode_failures 13
- R-oversubscribed: nodes=500: decode_failures 83
- R-siting: siting-mix=local-typical: misdecodes 1
- R-traceroute-small: traceroute-per-hour=0.0: queue drops 13.9% of transmissions - airtime here is measured through a cap
- R-traceroute-small: traceroute-per-hour=0.0: decode_failures 69
- R-traceroute-small: traceroute-per-hour=1.0: queue drops 20.8% of transmissions - airtime here is measured through a cap
- R-traceroute-small: traceroute-per-hour=1.0: decode_failures 62
- R-warm: warm-num-nodes=0: queue drops 13.9% of transmissions - airtime here is measured through a cap
- R-warm: warm-num-nodes=0: decode_failures 69
- R-warm: warm-num-nodes=25: queue drops 13.9% of transmissions - airtime here is measured through a cap
- R-warm: warm-num-nodes=25: decode_failures 69
- R-warm: warm-num-nodes=100: queue drops 13.9% of transmissions - airtime here is measured through a cap
- R-warm: warm-num-nodes=100: decode_failures 69
- R-warm: warm-num-nodes=2000: queue drops 13.9% of transmissions - airtime here is measured through a cap
- R-warm: warm-num-nodes=2000: decode_failures 69
- X-chatty-hops: broadcast-interval-s=300: decode_failures 27
- X-chatty: broadcast-interval-s=300: decode_failures 22
- X-nomute: faster: 1.6 s per simulated hour against 3.91 over 2 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- X-siting: siting-mix=local-typical: misdecodes 1
- X-siting: faster: 1.25 s per simulated hour against 4.06 over 2 prior run(s) - 3.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate
- X-stretch-duct: duct-per-hour=0.0: decode_failures 13
- X-stretch: stretch=1.25: decode_failures 23
- X-stretch: stretch=1.5: decode_failures 13
- X-stretch: stretch=2.0: decode_failures 4
- X-worst: role-placement=degree: decode_failures 108
- X-worst: role-placement=inverse: decode_failures 82
- X-worst: slower: 23.7 s per simulated hour against 2.89 over 2 prior run(s) - 8.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

</details>

Blocks that produced no JSON (their job failed, timed out, or was cancelled): `F-preset-turbo`

## Runtime against this block's own history

Wall-clock seconds per **simulated** hour, against the median of the same block's prior runs in this archive. Normalised because the raw total moves with the seed count and `--hours`; a rate does not. Runner hardware is shared, so read a ratio near 1 as noise and the flagged ones (past 2x either way) as worth a look.

| block | s/sim-h | median | ratio | runs compared |
| --- | --: | --: | --: | --: |
| `X-worst` | 23.7 | 2.89 | 8.18x | 2 |
| `Q-topology` | 3.6 | 1.67 | 2.15x | 2 |
| `X-stretch-duct` | 3.57 | 2.16 | 1.65x | 2 |
| `F-txpower` | 2.57 | 1.61 | 1.59x | 2 |
| `F-burst` | 5.02 | 7.53 | 0.67x | 2 |
| `X-badrouters` | 1.7 | 2.57 | 0.66x | 2 |
| `D-cadence` | 2.38 | 4.13 | 0.58x | 2 |
| `R-roles` | 1.73 | 3.16 | 0.55x | 2 |
| `P-eu-presets` | 2.03 | 3.71 | 0.55x | 2 |
| `G-allrouters` | 2.13 | 4.17 | 0.51x | 2 |
| `F-flooding` | 2.52 | 4.95 | 0.51x | 2 |
| `K-density` | 2.81 | 5.58 | 0.50x | 2 |
| `R-favourites` | 0.999 | 2.08 | 0.48x | 2 |
| `X-nomute` | 1.6 | 3.91 | 0.41x | 2 |
| `X-siting` | 1.25 | 4.06 | 0.31x | 2 |

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text` is the broadcast reach in the same cells, so an arm buying its measure while `text` falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `Q-control` | protocol | **held** | 0 → 0.946 | 0.946 | 0.804 → 0.824 | 1.1x bytes_on_air | up | 2 |
| `Q-protocol` | protocol | **held** | 0 → 0.944 | 0.944 | 0.797 → 0.808 | 1.2x bytes_on_air | up | 3 |
| `F-txpower` | tx-power | **held** | 0.088 → 0.944 | 0.855 | 0.109 → 0.808 | 12x sr_airtime | down | 4 |
| `X-pulse` | noise-pulse-interval-ms | **held** | 0.120 → 0.892 | 0.772 | 0.096 → 0.743 | 95x sr_airtime | down | 4 |
| `X-siting` | siting-mix | **held** | 0.132 → 0.892 | 0.761 | 0.084 → 0.694 | 7.1x advert_bytes | down | 3 |
| `X-stretch` | stretch | **text** | 0.133 → 0.808 | 0.674 | 0.133 → 0.808 | 3.4x sr_airtime | down | 4 |
| `R-siting` | siting-mix | **text** | 0.387 → 0.960 | 0.573 | 0.387 → 0.960 | 3.2x sr_airtime | up | 4 |
| `P-bw500` | preset | **held** | 0.398 → 0.942 | 0.544 | 0.196 → 0.730 | 2.4x advert_bytes | up | 3 |
| `R-hopscale` | nodes | **text** | 0.330 → 0.808 | 0.477 | 0.330 → 0.808 | 12x sr_bytes | down | 4 |
| `P-eu-presets` | preset | **text** | 0.351 → 0.808 | 0.456 | 0.351 → 0.808 | 2.8x sr_airtime | up | 4 |
| `P-preset` | preset | **text** | 0.351 → 0.808 | 0.456 | 0.351 → 0.808 | 4x sr_airtime | up | 3 |
| `R-oversubscribed` | nodes | **held** | 0.496 → 0.917 | 0.421 | 0.334 → 0.718 | 5x sr_bytes | down | 3 |
| `K-density` | nodes | **text** | 0.598 → 0.952 | 0.354 | 0.598 → 0.952 | 4.4x advert_bytes | up | 5 |
| `X-chatty` | broadcast-interval-s | **text** | 0.496 → 0.829 | 0.333 | 0.496 → 0.829 | 7.9x sr_airtime | down | 3 |
| `F-outage` | burst-loss | **text** | 0.477 → 0.808 | 0.331 | 0.477 → 0.808 | 2.6x sr_bytes | down | 4 |
| `Q-topology` | topology | **text** | 0.597 → 0.924 | 0.327 | 0.597 → 0.924 | 3.1x sr_bytes | up | 4 |
| `X-chatty-hops` | broadcast-interval-s | **text** | 0.554 → 0.879 | 0.326 | 0.554 → 0.879 | 7.8x sr_airtime | down | 3 |
| `F-burst` | burst-loss | **text** | 0.500 → 0.808 | 0.307 | 0.500 → 0.808 | 2.5x sr_bytes | down | 4 |
| `X-stretch-duct` | duct-per-hour | **text** | 0.391 → 0.683 | 0.293 | 0.391 → 0.683 | 1.9x sr_airtime | up | 2 |
| `R-hotstore-stress` | max-num-nodes | **held** | 0.612 → 0.899 | 0.287 | 0.312 → 0.524 | 6x sr_airtime | up | 3 |
| `P-congestion` | no-congestion-scaling | **text** | 0.652 → 0.920 | 0.268 | 0.652 → 0.920 | 4.6x sr_airtime | down | 2 |
| `G-hops` | hops-apart | **held** | 0.691 → 0.946 | 0.254 | 0.808 → 0.824 | 1.9x sr_bytes | down | 4 |
| `N-hops` | hops-apart | **held** | 0.691 → 0.946 | 0.254 | 0.808 → 0.824 | 1.9x sr_bytes | down | 5 |
| `F-hoplimit` | hop-limit | **text** | 0.645 → 0.892 | 0.246 | 0.645 → 0.892 | 2.1x sr_bytes | up | 4 |
| `K-hopspread` | hop-limit | **text** | 0.645 → 0.870 | 0.225 | 0.645 → 0.870 | 2x sr_bytes | up | 3 |
| `G-place` | place | **held** | 0.754 → 0.951 | 0.197 | 0.808 → 0.830 | 3.1x sr_bytes | up | 6 |
| `N-place` | place | **held** | 0.754 → 0.951 | 0.197 | 0.808 → 0.830 | 3.1x sr_bytes | up | 6 |
| `K-spread` | hop-spread | **text** | 0.645 → 0.808 | 0.162 | 0.645 → 0.808 | 1.9x sr_bytes | up | 2 |
| `X-noise` | noise-profile | **text** | 0.648 → 0.809 | 0.161 | 0.648 → 0.809 | 1.4x sr_bytes | down | 4 |
| `F-flooding` | role-mix | **text** | 0.694 → 0.851 | 0.157 | 0.694 → 0.851 | 2.5x bytes_on_air | up | 2 |
| `X-nomute` | role-mix | **text** | 0.694 → 0.851 | 0.157 | 0.694 → 0.851 | 2.5x bytes_on_air | up | 3 |
| `F-loss` | extra-loss | **text** | 0.663 → 0.808 | 0.144 | 0.663 → 0.808 | 1.8x sr_bytes | down | 4 |
| `K-size` | nodes | **text** | 0.664 → 0.808 | 0.144 | 0.664 → 0.808 | 4.3x advert_bytes | down | 5 |
| `X-amplify-worst` | amplify-worst | **text** | 0.808 → 0.938 | 0.130 | 0.808 → 0.938 | 1.2x sr_airtime | up | 3 |
| `R-hotstore` | max-num-nodes | **text** | 0.733 → 0.856 | 0.122 | 0.733 → 0.856 | 2.1x sr_airtime | up | 4 |
| `R-roles` | role-mix | **text** | 0.694 → 0.809 | 0.114 | 0.694 → 0.809 | 1.2x bytes_on_air | down | 2 |
| `R-platform` | platform-mix | **text** | 0.743 → 0.856 | 0.113 | 0.743 → 0.856 | 2.1x sr_airtime | down | 3 |
| `Q-interval` | broadcast-interval-s | **text** | 0.755 → 0.866 | 0.111 | 0.755 → 0.866 | 5.3x sr_airtime | up | 4 |
| `R-signing` | signature-policy | **text** | 0.703 → 0.808 | 0.104 | 0.703 → 0.808 | 1.2x sr_airtime | down | 3 |
| `R-mixed-26` | legacy-fraction | **text** | 0.768 → 0.869 | 0.101 | 0.768 → 0.869 | 2.1x bytes_on_air | down | 4 |
| `X-amplifiers` | amplifier-mix | **text** | 0.808 → 0.906 | 0.098 | 0.808 → 0.906 | 1.3x sr_bytes | up | 3 |
| `R-mixed` | legacy-fraction | **text** | 0.759 → 0.855 | 0.095 | 0.759 → 0.855 | 2x bytes_on_air | down | 4 |
| `R-roles-fav` | role-mix | **text** | 0.753 → 0.842 | 0.089 | 0.753 → 0.842 | 1.1x sr_airtime | down | 2 |
| `X-duct` | duct-per-hour | **text** | 0.808 → 0.891 | 0.084 | 0.808 → 0.891 | 1.3x bytes_on_air | up | 3 |
| `R-traceroute-small` | traceroute-per-hour | **held** | 0.704 → 0.772 | 0.068 | 0.586 → 0.645 | 1.3x sr_airtime | down | 2 |
| `R-signing-cost` | profile-flag | **text** | 0.808 → 0.858 | 0.050 | 0.808 → 0.858 | 3.3x bytes_on_air | down | 2 |
| `R-traceroute` | traceroute-per-hour | **text** | 0.765 → 0.808 | 0.042 | 0.765 → 0.808 | 1.4x sr_airtime | down | 4 |
| `D-cadence` | trigger | **held** | 0.902 → 0.944 | 0.042 | 0.778 → 0.808 | 13x advert_bytes | down | 4 |
| `R-favourites` | favourite-routers | **text** | 0.800 → 0.839 | 0.039 | 0.800 → 0.839 | 1.1x sr_bytes | up | 2 |
| `R-rebroadcast` | rebroadcast-mode | **held** | 0.910 → 0.944 | 0.033 | 0.808 → 0.810 | 15x sr_airtime | down | 3 |
| `L-provide` | provide-transport | **text** | 0.808 → 0.840 | 0.032 | 0.808 → 0.840 | 2.6x sr_airtime | up | 2 |
| `P-catchup` | catch-up-hours | **text** | 0.778 → 0.809 | 0.032 | 0.778 → 0.809 | 9.2x advert_bytes | up | 3 |
| `R-congestion-input` | congestion-input | **text** | 0.523 → 0.554 | 0.031 | 0.523 → 0.554 | 1.4x sr_airtime | up | 2 |
| `R-routerlate` | router-late-fraction | **held** | 0.927 → 0.948 | 0.021 | 0.799 → 0.811 | 1.3x bytes_on_air | down | 4 |
| `X-badrouters` | role-placement | **held** | 0.892 → 0.911 | 0.019 | 0.694 → 0.706 | 1.5x sr_bytes | up | 3 |
| `R-dmmode` | dm-mode | **text** | 0.763 → 0.781 | 0.018 | 0.763 → 0.781 | 1.3x sr_airtime | up | 3 |
| `J-timewin` | time-bucket-s | **text** | 0.790 → 0.806 | 0.016 | 0.790 → 0.806 | 5.5x advert_bytes | up | 3 |
| `R-srretries` | sr-retries | **text** | 0.804 → 0.819 | 0.015 | 0.804 → 0.819 | 1.1x sr_bytes | up | 4 |
| `X-worst` | role-placement | **held** | 0.942 → 0.957 | 0.015 | 0.868 → 0.878 | 1.1x sr_bytes | up | 2 |
| `J-window` | window-size | **held** | 0.936 → 0.950 | 0.014 | 0.800 → 0.810 | 5.2x advert_bytes | down | 3 |
| `E-width` | short-id-bits | **text** | 0.801 → 0.815 | 0.014 | 0.801 → 0.815 | 3.1x advert_bytes | down | 4 |
| `D-jitter` | advert-jitter-s | **held** | 0.941 → 0.955 | 0.014 | 0.805 → 0.809 | 1.2x sr_airtime | up | 4 |
| `M-jitter` | advert-jitter-s | **held** | 0.941 → 0.955 | 0.014 | 0.805 → 0.809 | 1.2x sr_airtime | up | 4 |
| `G-servers` | servers | **text** | 0.808 → 0.821 | 0.013 | 0.808 → 0.821 | 7.7x sr_bytes | up | 4 |
| `J-bucketmode` | bucket-mode | **held** | 0.936 → 0.949 | 0.013 | 0.798 → 0.809 | 2.7x advert_bytes | down | 4 |
| `N-servers` | servers | **text** | 0.808 → 0.821 | 0.013 | 0.808 → 0.821 | 7.7x sr_bytes | up | 4 |
| `Q-hopassign` | hop-assign | **held** | 0.944 → 0.955 | 0.011 | 0.808 → 0.815 | 1.3x sr_airtime | up | 2 |
| `G-allrouters` | servers | **text** | 0.809 → 0.817 | 0.008 | 0.809 → 0.817 | 2.3x sr_bytes | down | 2 |
| `E-capacity` | capacity | **held** | 0.939 → 0.946 | 0.007 | 0.806 → 0.810 | 5.3x advert_bytes | up | 5 |
| `M-capacity` | capacity | **held** | 0.939 → 0.946 | 0.007 | 0.806 → 0.810 | 5.3x advert_bytes | up | 5 |
| `P-diurnal` | diurnal | **text** | 0.808 → 0.815 | 0.007 | 0.808 → 0.815 | 1.2x advert_bytes | down | 3 |
| `R-versions` | profile | **text** | 0.800 → 0.808 | 0.007 | 0.800 → 0.808 | 3.3x bytes_on_air | up | 5 |
| `R-dmmode-cr` | dm-mode | **held** | 0.928 → 0.935 | 0.007 | 0.781 → 0.785 | 1.2x sr_airtime | up | 2 |
| `R-crladder` | coding-rate-ladder | **held** | 0.928 → 0.934 | 0.006 | 0.781 → 0.785 | 1.1x sr_bytes | down | 2 |
| `J-wincap` | capacity | **text** | 0.803 → 0.809 | 0.006 | 0.803 → 0.809 | 2.3x advert_bytes | down | 3 |
| `R-congestion-mode` | congestion-mode | **text** | 0.920 → 0.925 | 0.005 | 0.920 → 0.925 | 1.1x sr_airtime | down | 2 |
| `R-adopt` | no-adopt-hop-recommendation | **text** | 0.915 → 0.920 | 0.005 | 0.915 → 0.920 | 1.1x bytes_on_air | down | 2 |
| `R-firmware` | profile | **text** | 0.803 → 0.808 | 0.005 | 0.803 → 0.808 | 3.1x bytes_on_air | up | 2 |
| `D-resolve` | resolve | **held** | 0.939 → 0.944 | 0.004 | 0.804 → 0.808 | 5.7x advert_bytes | = | 3 |
| `M-combined` | replay-ordering | **text** | 0.835 → 0.840 | 0.004 | 0.835 → 0.840 | 1x sr_bytes | down | 2 |
| `L-advert` | advert-transport | **text** | 0.804 → 0.808 | 0.003 | 0.804 → 0.808 | 2.9x sr_airtime | down | 2 |
| `R-repeats-busy` | extra-repeats | **held** | 0.992 → 0.994 | 0.002 | 0.920 → 0.920 | 1x sr_airtime | up | 2 |
| `M-replayorder` | replay-ordering | **text** | 0.808 → 0.809 | 0.002 | 0.808 → 0.809 | 1.2x sr_bytes | up | 2 |
| `R-repeats` | extra-repeats | **text** | 0.808 → 0.809 | 0.002 | 0.808 → 0.809 | 1.1x sr_bytes | up | 2 |

### Moved no delivery measure

Not the same as having done nothing: several arms hold delivery flat by design and differ in what they spend. Three ways of reconciling the same two sets had better agree on what is held; where they differ is the price.

| block | arm | price | cells |
| --- | --- | --- | --: |
| `E-signed` | signed | 1.4x advert_bytes | 2 |
| `R-warm` | warm-num-nodes | - | 4 |

## Every block

### `D-cadence` - trigger  `--scenario valleys`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| interval | 0.782 | - | - | 0.920 | 0.929 | 0.416 | 1.65x | 28.3/31.0% | 7.3% | 3 |
| aimd | 0.801 | - | - | 0.902 | 0.943 | 0.454 | 1.26x | 21.3/23.6% | 5.2% | 3 |
| bucket+interval | 0.778 | - | - | 0.938 | 0.939 | 0.431 | 1.67x | 28.6/31.3% | 7.6% | 3 |

> trigger=interval: misdecodes 12

> trigger=aimd: misdecodes 3

> trigger=bucket+interval: misdecodes 14

### `D-jitter` - advert-jitter-s  `--scenario valleys`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.806 | - | - | 0.941 | 0.942 | 0.447 | 1.26x | 21.1/23.6% | 5.2% | 3 |
| 30 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 120 | 0.805 | - | - | 0.942 | 0.943 | 0.431 | 1.27x | 21.4/23.8% | 5.2% | 3 |
| 600 | 0.809 | - | - | 0.955 | 0.956 | 0.437 | 1.26x | 21.5/23.8% | 5.3% | 3 |

### `D-resolve` - resolve  `--scenario valleys`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| enum | 0.804 | - | - | 0.939 | 0.943 | 0.431 | 1.23x | 21.0/23.3% | 5.3% | 3 |
| hybrid | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |

### `E-capacity` - capacity  `--scenario valleys`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 0.810 | - | - | 0.945 | 0.947 | 0.451 | 1.24x | 21.1/23.5% | 5.3% | 3 |
| 8 | 0.807 | - | - | 0.943 | 0.946 | 0.426 | 1.25x | 21.3/23.6% | 5.2% | 3 |
| 16 | 0.806 | - | - | 0.939 | 0.939 | 0.423 | 1.25x | 21.4/23.7% | 5.2% | 3 |
| 32 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 50 | 0.809 | - | - | 0.946 | 0.947 | 0.426 | 1.24x | 21.0/23.4% | 5.1% | 3 |

> capacity=4: decode_failures 82

> capacity=8: decode_failures 30

### `E-signed` - signed  `--scenario valleys`

*Whether the advert carries its 66-byte signature.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| True | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |

### `E-width` - short-id-bits  `--scenario valleys`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 0.815 | - | - | 0.952 | 0.953 | 0.422 | 1.24x | 20.9/23.4% | 5.2% | 3 |
| 24 | 0.801 | - | - | 0.945 | 0.945 | 0.407 | 1.24x | 21.0/23.4% | 5.2% | 3 |
| 32 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 64 | 0.805 | - | - | 0.941 | 0.942 | 0.431 | 1.25x | 21.2/23.6% | 5.2% | 3 |

### `F-burst` - burst-loss  `--scenario valleys`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 0.1 | 0.708 | - | - | 0.918 | 0.923 | 0.344 | 1.19x | 20.1/22.5% | 4.8% | 3 |
| 0.2 | 0.605 | - | - | 0.855 | 0.883 | 0.253 | 1.09x | 19.2/21.4% | 4.3% | 3 |
| 0.3 | 0.500 | - | - | 0.735 | 0.814 | 0.186 | 1.01x | 17.9/20.2% | 3.9% | 3 |

> burst-loss=0.2: decode_failures 4

> burst-loss=0.3: decode_failures 37

### `F-flooding` - role-mix  `--scenario valleys`

*Every node rebroadcasting everything, against a real role census.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 0.694 | - | - | 0.892 | 0.893 | 0.000 | 1.06x | 20.3/22.9% | 5.5% | 3 |
| all-routers | 0.851 | - | - | 0.951 | 0.952 | 0.637 | 2.62x | 37.1/38.1% | 5.3% | 3 |

### `F-hoplimit` - hop-limit  `--scenario valleys`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.645 | - | - | 0.925 | 0.929 | 0.256 | 0.99x | 17.7/20.2% | 4.6% | 3 |
| 7 | 0.870 | - | - | 0.944 | 0.944 | 0.542 | 1.42x | 22.7/24.7% | 5.3% | 3 |
| 15 | 0.888 | - | - | 0.940 | 0.941 | 0.593 | 1.45x | 23.1/25.1% | 5.4% | 3 |
| 32 | 0.892 | - | - | 0.945 | 0.946 | 0.592 | 1.46x | 23.2/25.2% | 5.4% | 3 |

### `F-loss` - extra-loss  `--scenario valleys`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 0.1 | 0.768 | - | - | 0.928 | 0.932 | 0.358 | 1.30x | 22.0/24.3% | 5.1% | 3 |
| 0.2 | 0.722 | - | - | 0.915 | 0.920 | 0.326 | 1.34x | 22.8/25.1% | 5.0% | 3 |
| 0.3 | 0.663 | - | - | 0.882 | 0.889 | 0.273 | 1.35x | 23.1/25.6% | 4.8% | 3 |

### `F-outage` - burst-loss  `--scenario valleys`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 0.1 | 0.684 | - | - | 0.895 | 0.917 | 0.348 | 1.17x | 19.8/22.2% | 4.7% | 3 |
| 0.2 | 0.595 | - | - | 0.839 | 0.894 | 0.268 | 1.12x | 19.2/21.4% | 4.2% | 3 |
| 0.3 | 0.477 | - | - | 0.699 | 0.786 | 0.193 | 1.06x | 18.4/20.7% | 3.8% | 3 |

> burst-loss=0.1: decode_failures 25

> burst-loss=0.2: decode_failures 25

> burst-loss=0.3: decode_failures 36

### `F-txpower` - tx-power  `--scenario valleys`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 22 | 0.407 | - | - | 0.582 | 0.628 | 0.000 | 1.34x | 15.9/18.3% | 4.8% | 3 |
| 17 | 0.191 | - | - | 0.411 | 0.456 | 0.000 | 1.11x | 11.9/15.4% | 4.0% | 3 |
| 14 | 0.109 | - | - | 0.088 | 0.090 | 0.000 | 0.81x | 7.3/10.1% | 2.8% | 3 |

> tx-power=22: decode_failures 14

> tx-power=17: decode_failures 15

### `G-allrouters` - servers  `--scenario valleys`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.817 | - | - | 0.945 | 0.945 | 0.437 | 1.24x | 21.3/23.7% | 5.3% | 3 |
| 6 | 0.809 | - | - | 0.942 | 0.943 | 0.416 | 1.29x | 22.1/24.5% | 5.6% | 6 |

### `G-hops` - hops-apart  `--scenario valleys`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.812 | - | - | 0.942 | 0.943 | 0.430 | 1.24x | 21.2/23.6% | 5.1% | 3 |
| 2 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 3 | 0.824 | - | - | 0.946 | 0.947 | 0.394 | 1.27x | 21.3/23.8% | 5.3% | 3 |
| 4 | 0.817 | - | - | 0.691 | 0.913 | 0.421 | 1.27x | 21.8/23.8% | 5.3% | 3 |

> hops-apart=4: decode_failures 22

### `G-place` - place  `--scenario valleys`

*Where the archives sit, under a flat hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 0.830 | - | - | 0.754 | 0.957 | 0.438 | 1.26x | 21.5/23.8% | 5.1% | 3 |
| routers | 0.817 | - | - | 0.945 | 0.945 | 0.437 | 1.24x | 21.3/23.7% | 5.3% | 3 |
| alternate-routers | 0.811 | - | - | 0.947 | 0.948 | 0.411 | 1.23x | 21.1/23.4% | 5.1% | 3 |
| beside-router | 0.817 | - | - | 0.951 | 0.952 | 0.442 | 1.25x | 21.4/23.9% | 5.2% | 3 |
| random-clients | 0.830 | - | - | 0.939 | 0.953 | 0.484 | 1.28x | 21.5/23.7% | 5.1% | 3 |
| hops-apart | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |

> place=spread: decode_failures 24

> place=random-clients: decode_failures 6

### `G-servers` - servers  `--scenario valleys`

*How many archives the mesh has, under a flat hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 0.808 | - | - | 0.941 | 0.945 | 0.429 | 1.25x | 21.2/23.6% | 5.2% | 2 |
| 3 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 5 | 0.809 | - | - | 0.948 | 0.950 | 0.425 | 1.29x | 21.7/24.3% | 5.3% | 5 |
| 8 | 0.821 | - | - | 0.951 | 0.953 | 0.389 | 1.32x | 22.0/24.3% | 5.4% | 8 |

### `J-bucketmode` - bucket-mode  `--scenario valleys`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 0.809 | - | - | 0.949 | 0.950 | 0.417 | 1.25x | 21.1/23.5% | 5.2% | 3 |
| local | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| time | 0.798 | - | - | 0.936 | 0.938 | 0.417 | 1.28x | 21.6/24.1% | 5.4% | 3 |
| window | 0.808 | - | - | 0.943 | 0.946 | 0.428 | 1.24x | 20.8/23.2% | 5.1% | 3 |

> bucket-mode=global: misdecodes 26

> bucket-mode=time: misdecodes 36

> bucket-mode=window: misdecodes 30

### `J-timewin` - time-bucket-s  `--scenario valleys`

*Width of the time bucket, when buckets are cut by the clock.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 0.790 | - | - | 0.928 | 0.930 | 0.411 | 1.40x | 23.5/26.2% | 5.9% | 3 |
| 1800 | 0.798 | - | - | 0.936 | 0.938 | 0.417 | 1.28x | 21.6/24.1% | 5.4% | 3 |
| 3600 | 0.806 | - | - | 0.941 | 0.945 | 0.427 | 1.26x | 21.2/23.8% | 5.2% | 3 |

> time-bucket-s=600: misdecodes 117

> time-bucket-s=1800: misdecodes 36

> time-bucket-s=3600: misdecodes 10

### `J-wincap` - capacity  `--scenario valleys`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 0.809 | - | - | 0.941 | 0.949 | 0.426 | 1.24x | 21.1/23.3% | 5.1% | 3 |
| 16 | 0.803 | - | - | 0.939 | 0.939 | 0.430 | 1.24x | 21.1/23.5% | 5.1% | 3 |
| 32 | 0.808 | - | - | 0.943 | 0.946 | 0.428 | 1.24x | 20.8/23.2% | 5.1% | 3 |

> capacity=8: misdecodes 28

> capacity=8: decode_failures 17

> capacity=16: misdecodes 28

> capacity=32: misdecodes 30

### `J-window` - window-size  `--scenario valleys`

*Objects in the sliding window, when buckets are windowed.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 0.810 | - | - | 0.950 | 0.951 | 0.411 | 1.35x | 22.7/25.4% | 5.6% | 3 |
| 16 | 0.800 | - | - | 0.936 | 0.939 | 0.440 | 1.28x | 21.6/24.2% | 5.3% | 3 |
| 32 | 0.808 | - | - | 0.943 | 0.946 | 0.428 | 1.24x | 20.8/23.2% | 5.1% | 3 |

> window-size=8: misdecodes 105

> window-size=16: misdecodes 61

> window-size=32: misdecodes 30

### `K-density` - nodes  `--scenario valleys`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 0.598 | - | - | 0.836 | 0.839 | 0.000 | 1.11x | 23.1/28.3% | 6.3% | 3 |
| 60 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 90 | 0.897 | - | - | 0.983 | 0.984 | 0.674 | 1.53x | 25.5/28.4% | 4.8% | 3 |
| 120 | 0.920 | - | - | 0.992 | 0.994 | 0.694 | 2.16x | 38.7/43.8% | 5.3% | 3 |
| 150 | 0.952 | - | - | 0.999 | 0.999 | 0.652 | 2.50x | 37.4/41.5% | 5.8% | 3 |

### `K-hopspread` - hop-limit  `--scenario valleys`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.645 | - | - | 0.925 | 0.929 | 0.256 | 0.99x | 17.7/20.2% | 4.6% | 3 |
| 5 | 0.808 | - | - | 0.950 | 0.951 | 0.414 | 1.28x | 21.2/23.6% | 5.2% | 3 |
| 7 | 0.870 | - | - | 0.944 | 0.944 | 0.542 | 1.42x | 22.7/24.7% | 5.3% | 3 |

### `K-size` - nodes  `--scenario valleys`

*Mesh size with density held constant - the area grows with the node count.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 0.681 | - | - | 0.847 | 0.865 | 0.000 | 1.15x | 26.4/29.1% | 7.3% | 3 |
| 60 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 90 | 0.772 | - | - | 0.964 | 0.966 | 0.310 | 1.69x | 24.1/27.6% | 5.7% | 3 |
| 120 | 0.715 | - | - | 0.920 | 0.921 | 0.100 | 2.26x | 25.0/29.6% | 4.9% | 3 |
| 150 | 0.664 | - | - | 0.909 | 0.910 | 0.243 | 2.77x | 27.2/34.3% | 5.0% | 3 |

> nodes=40: decode_failures 4

### `K-spread` - hop-spread  `--scenario valleys`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.645 | - | - | 0.925 | 0.929 | 0.256 | 0.99x | 17.7/20.2% | 4.6% | 3 |
| True | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |

### `L-advert` - advert-transport  `--scenario valleys`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| dm | 0.804 | - | - | 0.945 | 0.947 | 0.411 | 1.22x | 20.6/22.9% | 5.2% | 3 |

### `L-provide` - provide-transport  `--scenario valleys`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| broadcast | 0.840 | - | - | 0.947 | 0.949 | 0.461 | 1.31x | 22.1/24.6% | 5.4% | 3 |

### `M-capacity` - capacity  `--scenario valleys`

*Sketch capacity under local numbering and the later defaults.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 0.810 | - | - | 0.945 | 0.947 | 0.451 | 1.24x | 21.1/23.5% | 5.3% | 3 |
| 8 | 0.807 | - | - | 0.943 | 0.946 | 0.426 | 1.25x | 21.3/23.6% | 5.2% | 3 |
| 16 | 0.806 | - | - | 0.939 | 0.939 | 0.423 | 1.25x | 21.4/23.7% | 5.2% | 3 |
| 32 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 50 | 0.809 | - | - | 0.946 | 0.947 | 0.426 | 1.24x | 21.0/23.4% | 5.1% | 3 |

> capacity=4: decode_failures 82

> capacity=8: decode_failures 30

### `M-combined` - replay-ordering  `--scenario valleys`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 0.840 | - | - | 0.947 | 0.949 | 0.461 | 1.31x | 22.1/24.6% | 5.4% | 3 |
| heard | 0.835 | - | - | 0.947 | 0.950 | 0.453 | 1.32x | 22.0/24.5% | 5.4% | 3 |

> replay-ordering=heard: misdecodes 3

### `M-jitter` - advert-jitter-s  `--scenario valleys`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.806 | - | - | 0.941 | 0.942 | 0.447 | 1.26x | 21.1/23.6% | 5.2% | 3 |
| 30 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 120 | 0.805 | - | - | 0.942 | 0.943 | 0.431 | 1.27x | 21.4/23.8% | 5.2% | 3 |
| 600 | 0.809 | - | - | 0.955 | 0.956 | 0.437 | 1.26x | 21.5/23.8% | 5.3% | 3 |

### `M-replayorder` - replay-ordering  `--scenario valleys`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| heard | 0.809 | - | - | 0.944 | 0.944 | 0.426 | 1.25x | 21.1/23.4% | 5.2% | 3 |

> replay-ordering=heard: misdecodes 23

### `N-hops` - hops-apart  `--scenario valleys`

*How many hops apart the archives are, under real per-node hop limits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.812 | - | - | 0.942 | 0.943 | 0.430 | 1.24x | 21.2/23.6% | 5.1% | 3 |
| 2 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 3 | 0.824 | - | - | 0.946 | 0.947 | 0.394 | 1.27x | 21.3/23.8% | 5.3% | 3 |
| 4 | 0.817 | - | - | 0.691 | 0.913 | 0.421 | 1.27x | 21.8/23.8% | 5.3% | 3 |
| 5 | 0.815 | - | - | 0.819 | 0.939 | 0.410 | 1.27x | 21.8/23.8% | 5.2% | 3 |

> hops-apart=4: decode_failures 22

> hops-apart=5: decode_failures 35

### `N-place` - place  `--scenario valleys`

*Where the archives sit, under real per-node hop limits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 0.830 | - | - | 0.754 | 0.957 | 0.438 | 1.26x | 21.5/23.8% | 5.1% | 3 |
| routers | 0.817 | - | - | 0.945 | 0.945 | 0.437 | 1.24x | 21.3/23.7% | 5.3% | 3 |
| alternate-routers | 0.811 | - | - | 0.947 | 0.948 | 0.411 | 1.23x | 21.1/23.4% | 5.1% | 3 |
| beside-router | 0.817 | - | - | 0.951 | 0.952 | 0.442 | 1.25x | 21.4/23.9% | 5.2% | 3 |
| random-clients | 0.830 | - | - | 0.939 | 0.953 | 0.484 | 1.28x | 21.5/23.7% | 5.1% | 3 |
| hops-apart | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |

> place=spread: decode_failures 24

> place=random-clients: decode_failures 6

### `N-servers` - servers  `--scenario valleys`

*How many archives the mesh has, under real per-node hop limits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 0.808 | - | - | 0.941 | 0.945 | 0.429 | 1.25x | 21.2/23.6% | 5.2% | 2 |
| 3 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 5 | 0.809 | - | - | 0.948 | 0.950 | 0.425 | 1.29x | 21.7/24.3% | 5.3% | 5 |
| 8 | 0.821 | - | - | 0.951 | 0.953 | 0.389 | 1.32x | 22.0/24.3% | 5.4% | 8 |

### `P-bw500` - preset  `--scenario valleys`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 0.196 | - | - | 0.398 | 0.456 | 0.000 | 0.05x | 0.6/0.7% | 0.2% | 3 |
| MEDIUM_TURBO | 0.470 | - | - | 0.751 | 0.751 | 0.000 | 0.27x | 3.5/4.5% | 1.1% | 3 |
| LONG_TURBO | 0.730 | - | - | 0.942 | 0.944 | 0.136 | 1.23x | 18.4/19.7% | 4.8% | 3 |

> preset=SHORT_TURBO: decode_failures 9

### `P-catchup` - catch-up-hours  `--scenario valleys`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 0.778 | - | - | 0.938 | 0.939 | 0.431 | 1.67x | 28.6/31.3% | 7.6% | 3 |
| 02-06 | 0.809 | - | - | 0.927 | 0.949 | 0.428 | 1.30x | 21.9/24.4% | 5.6% | 3 |
| 00-08 | 0.805 | - | - | 0.927 | 0.949 | 0.441 | 1.34x | 23.2/25.5% | 6.0% | 3 |

> catch-up-hours=: misdecodes 14

> catch-up-hours=02-06: decode_failures 44

> catch-up-hours=00-08: decode_failures 42

### `P-congestion` - no-congestion-scaling  `--scenario valleys`

*The firmware's node-count interval scaling, on against off.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.920 | - | - | 0.992 | 0.994 | 0.694 | 2.16x | 38.7/43.8% | 5.3% | 3 |
| True | 0.652 | - | - | 0.785 | 0.875 | 0.395 | 5.89x | 74.9/80.2% | 12.5% | 3 |

> no-congestion-scaling=True: queue drops 12.6% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 61

### `P-diurnal` - diurnal  `--scenario valleys`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 0.815 | - | - | 0.945 | 0.946 | 0.404 | 1.14x | 19.3/21.5% | 4.8% | 3 |
| sinusoid | 0.810 | - | - | 0.943 | 0.944 | 0.435 | 1.13x | 18.9/20.8% | 4.6% | 3 |
| commuter | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |

### `P-eu-presets` - preset  `--scenario valleys`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 0.351 | - | - | 0.511 | 0.527 | 0.000 | 0.15x | 1.9/2.4% | 0.6% | 3 |
| LONG_FAST | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| LITE_FAST | 0.739 | - | - | 0.819 | 0.824 | 0.293 | 0.97x | 15.9/17.2% | 3.9% | 3 |
| NARROW_SLOW | 0.772 | - | - | 0.917 | 0.918 | 0.406 | 1.24x | 20.3/23.2% | 5.2% | 3 |

> preset=SHORT_FAST: decode_failures 2

### `P-preset` - preset  `--scenario valleys`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 0.351 | - | - | 0.511 | 0.527 | 0.000 | 0.15x | 1.9/2.4% | 0.6% | 3 |
| LONG_FAST | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| LONG_MODERATE | 0.799 | - | - | 0.915 | 0.917 | 0.411 | 3.43x | 56.7/61.1% | 12.5% | 3 |

> preset=SHORT_FAST: decode_failures 2

> preset=LONG_MODERATE: decode_failures 4

### `Q-control` - protocol  `--scenario valleys`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.804 | - | - | 0 | 0.000 | 0.426 | 1.20x | 20.4/22.7% | 4.9% | 3 |
| sr | 0.824 | - | - | 0.946 | 0.947 | 0.394 | 1.27x | 21.3/23.8% | 5.3% | 3 |

### `Q-hopassign` - hop-assign  `--scenario valleys`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| random | 0.815 | - | - | 0.955 | 0.956 | 0.384 | 1.31x | 22.3/24.5% | 5.5% | 3 |

### `Q-interval` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 0.755 | - | - | 0.913 | 0.914 | 0.413 | 1.95x | 33.1/36.7% | 8.1% | 3 |
| 3600 | 0.829 | - | - | 0.951 | 0.951 | 0.415 | 0.86x | 14.7/16.2% | 3.6% | 3 |
| 10800 | 0.852 | - | - | 0.966 | 0.966 | 0.474 | 0.56x | 9.5/10.3% | 2.3% | 3 |
| 43200 | 0.866 | - | - | 0.978 | 0.978 | 0.443 | 0.39x | 6.7/7.2% | 1.6% | 3 |

### `Q-protocol` - protocol  `--scenario valleys`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.804 | - | - | 0 | 0.000 | 0.426 | 1.20x | 20.4/22.7% | 4.9% | 3 |
| chain | 0.797 | - | - | 0.909 | 0.949 | 0.407 | 1.45x | 24.4/27.1% | 6.0% | 3 |
| sr | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |

### `Q-topology` - topology  `--scenario valleys`

*The shape of the mesh, at fixed node count and seed.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| clustered | 0.897 | - | - | 0.947 | 0.956 | 0.000 | 1.08x | 35.5/37.9% | 5.5% | 3 |
| corridor | 0.597 | - | - | 0.809 | 0.810 | 0.334 | 1.52x | 20.7/23.5% | 4.7% | 3 |
| hub | 0.924 | - | - | 0.971 | 0.971 | 0.000 | 1.20x | 37.0/38.7% | 5.6% | 3 |

> topology=clustered: decode_failures 18

> slower: 3.6 s per simulated hour against 1.67 over 2 prior run(s) - 2.1x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

### `R-adopt` - no-adopt-hop-recommendation  `--scenario valleys`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.920 | - | - | 0.992 | 0.994 | 0.694 | 2.16x | 38.7/43.8% | 5.3% | 3 |
| True | 0.915 | - | - | 0.994 | 0.995 | 0.702 | 2.47x | 43.3/48.9% | 5.7% | 3 |

### `R-congestion-input` - congestion-input  `--scenario valleys`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 0.523 | - | - | 0.899 | 0.903 | 0.195 | 4.66x | 29.4/43.3% | 5.5% | 3 |
| truesize | 0.554 | - | - | 0.928 | 0.929 | 0.216 | 3.59x | 23.9/35.9% | 4.7% | 3 |

> congestion-input=hotstore: decode_failures 13

> congestion-input=truesize: decode_failures 6

### `R-congestion-mode` - congestion-mode  `--scenario valleys`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 0.925 | - | - | 0.993 | 0.994 | 0.739 | 2.05x | 36.8/41.7% | 5.0% | 3 |
| adaptive | 0.920 | - | - | 0.992 | 0.994 | 0.694 | 2.16x | 38.7/43.8% | 5.3% | 3 |

### `R-crladder` - coding-rate-ladder  `--scenario valleys`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.781 | - | - | 0.934 | 0.937 | 0.400 | 1.47x | 25.3/28.0% | 6.3% | 3 |
| True | 0.785 | - | - | 0.928 | 0.932 | 0.439 | 1.46x | 24.9/27.6% | 6.2% | 3 |

### `R-dmmode` - dm-mode  `--scenario valleys`

*How a DM escalates to flooding.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 0.763 | - | - | 0.923 | 0.926 | 0.406 | 1.62x | 27.4/30.5% | 6.6% | 3 |
| directed-with-late-flood | 0.781 | - | - | 0.934 | 0.937 | 0.400 | 1.47x | 25.3/28.0% | 6.3% | 3 |
| m4-early-flood | 0.777 | - | - | 0.927 | 0.930 | 0.431 | 1.48x | 25.3/28.2% | 6.3% | 3 |

### `R-dmmode-cr` - dm-mode  `--scenario valleys`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 0.785 | - | - | 0.928 | 0.932 | 0.439 | 1.46x | 24.9/27.6% | 6.2% | 3 |
| m4-early-flood | 0.781 | - | - | 0.935 | 0.939 | 0.402 | 1.48x | 25.3/28.1% | 6.2% | 3 |

### `R-favourites` - favourite-routers  `--scenario valleys`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.800 | - | - | 0.946 | 0.947 | 0.400 | 1.30x | 23.3/25.8% | 5.1% | 3 |
| True | 0.839 | - | - | 0.943 | 0.943 | 0.476 | 1.42x | 24.4/26.6% | 5.1% | 3 |

> faster: 0.999 s per simulated hour against 2.08 over 2 prior run(s) - 2.1x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `R-firmware` - profile  `--scenario valleys`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 0.803 | - | - | 0.941 | 0.942 | 0.000 | 0.71x | 11.4/13.6% | 2.0% | 3 |
| 2.8 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |

### `R-hopscale` - nodes  `--scenario valleys`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 120 | 0.715 | - | - | 0.920 | 0.921 | 0.100 | 2.26x | 25.0/29.6% | 4.9% | 3 |
| 250 | 0.526 | - | - | 0.901 | 0.902 | 0.208 | 4.98x | 31.6/46.6% | 5.9% | 3 |
| 500 | 0.330 | - | - | 0.502 | 0.523 | 0.087 | 10.03x | 30.7/48.7% | 7.0% | 3 |

> nodes=250: decode_failures 22

> nodes=500: decode_failures 120

### `R-hotstore` - max-num-nodes  `--scenario valleys`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 0.733 | - | - | 0.890 | 0.897 | 0.365 | 2.79x | 47.2/50.5% | 9.8% | 3 |
| 100 | 0.856 | - | - | 0.954 | 0.954 | 0.460 | 1.43x | 25.0/27.2% | 5.2% | 3 |
| 120 | 0.856 | - | - | 0.954 | 0.954 | 0.460 | 1.43x | 25.0/27.2% | 5.2% | 3 |
| 250 | 0.856 | - | - | 0.954 | 0.954 | 0.460 | 1.43x | 25.0/27.2% | 5.2% | 3 |

### `R-hotstore-stress` - max-num-nodes  `--scenario valleys`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 0.312 | - | - | 0.612 | 0.668 | 0.126 | 11.77x | 62.5/75.8% | 10.6% | 3 |
| 120 | 0.523 | - | - | 0.899 | 0.903 | 0.195 | 4.66x | 29.4/43.3% | 5.5% | 3 |
| 250 | 0.524 | - | - | 0.896 | 0.898 | 0.195 | 4.50x | 28.8/41.0% | 5.2% | 3 |

> max-num-nodes=10: decode_failures 105

> max-num-nodes=120: decode_failures 13

> max-num-nodes=250: decode_failures 1

### `R-mixed` - legacy-fraction  `--scenario valleys`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 0.25 | 0.855 | - | - | 0.956 | 0.956 | 0.113 | 1.19x | 21.7/24.5% | 4.5% | 3 |
| 0.5 | 0.809 | - | - | 0.965 | 0.966 | 0.290 | 0.95x | 15.9/18.2% | 3.8% | 3 |
| 0.75 | 0.759 | - | - | 0.933 | 0.933 | 0.000 | 0.86x | 15.5/17.4% | 3.8% | 3 |

### `R-mixed-26` - legacy-fraction  `--scenario valleys`

*The same with the older share on 2.6.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 0.25 | 0.869 | - | - | 0.975 | 0.976 | 0.100 | 1.18x | 21.9/24.9% | 4.6% | 3 |
| 0.5 | 0.814 | - | - | 0.968 | 0.969 | 0.324 | 0.90x | 15.5/17.8% | 3.6% | 3 |
| 0.75 | 0.768 | - | - | 0.935 | 0.935 | 0.000 | 0.83x | 15.5/17.1% | 3.8% | 3 |

### `R-oversubscribed` - nodes  `--scenario valleys`

*Mesh size against a store that has to hold it, over a full day.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 0.718 | - | - | 0.917 | 0.917 | 0.086 | 2.10x | 23.6/27.9% | 4.6% | 3 |
| 250 | 0.523 | - | - | 0.899 | 0.903 | 0.195 | 4.66x | 29.4/43.3% | 5.5% | 3 |
| 500 | 0.334 | - | - | 0.496 | 0.524 | 0.087 | 9.47x | 29.4/45.9% | 6.5% | 3 |

> nodes=250: decode_failures 13

> nodes=500: decode_failures 83

### `R-platform` - platform-mix  `--scenario valleys`

*The board mix, which decides each node's hot-store size.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.856 | - | - | 0.954 | 0.954 | 0.460 | 1.43x | 25.0/27.2% | 5.2% | 3 |
| baymesh-2026-08 | 0.856 | - | - | 0.954 | 0.954 | 0.460 | 1.43x | 25.0/27.2% | 5.2% | 3 |
| constrained | 0.743 | - | - | 0.898 | 0.904 | 0.366 | 2.79x | 47.3/50.5% | 9.8% | 3 |

### `R-rebroadcast` - rebroadcast-mode  `--scenario valleys`

*The rebroadcast mode - what a node relays.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| KNOWN_ONLY | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| CORE_PORTNUMS_ONLY | 0.810 | - | - | 0.910 | 0.947 | 0.412 | 1.22x | 20.8/23.1% | 5.1% | 3 |

### `R-repeats` - extra-repeats  `--scenario valleys`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| True | 0.809 | - | - | 0.944 | 0.944 | 0.428 | 1.27x | 21.4/23.6% | 5.2% | 3 |

### `R-repeats-busy` - extra-repeats  `--scenario valleys`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.920 | - | - | 0.992 | 0.994 | 0.694 | 2.16x | 38.7/43.8% | 5.3% | 3 |
| True | 0.920 | - | - | 0.994 | 0.994 | 0.701 | 2.18x | 38.5/43.6% | 5.2% | 3 |

### `R-roles` - role-mix  `--scenario valleys`

*The legacy default role census against a real mesh's.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 0.809 | - | - | 0.964 | 0.966 | 0.362 | 1.26x | 21.5/24.1% | 5.4% | 3 |
| baymesh-2026-08 | 0.694 | - | - | 0.892 | 0.893 | 0.000 | 1.06x | 20.3/22.9% | 5.5% | 3 |

### `R-roles-fav` - role-mix  `--scenario valleys`

*The same with router favourites on.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 0.842 | - | - | 0.963 | 0.966 | 0.470 | 1.35x | 22.4/24.3% | 5.4% | 3 |
| baymesh-2026-08 | 0.753 | - | - | 0.899 | 0.900 | 0.000 | 1.24x | 23.4/25.6% | 5.4% | 3 |

### `R-routerlate` - router-late-fraction  `--scenario valleys`

*The share of nodes on ROUTER_LATE.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 0.05 | 0.799 | - | - | 0.948 | 0.949 | 0.402 | 1.36x | 25.6/28.0% | 5.2% | 3 |
| 0.1 | 0.811 | - | - | 0.945 | 0.946 | 0.451 | 1.46x | 25.8/28.2% | 5.2% | 3 |
| 0.2 | 0.805 | - | - | 0.927 | 0.928 | 0.422 | 1.62x | 30.0/31.2% | 5.1% | 3 |

### `R-signing` - signature-policy  `--scenario valleys`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| BALANCED | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| STRICT | 0.703 | - | - | 0.853 | 0.855 | 0.317 | 1.37x | 22.9/25.4% | 5.6% | 3 |

### `R-signing-cost` - profile-flag  `--scenario valleys`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 0.858 | - | - | 0.975 | 0.975 | 0.447 | 0.67x | 12.0/13.5% | 3.0% | 3 |
| signing=true | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |

### `R-siting` - siting-mix  `--scenario valleys`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| local-typical | 0.777 | - | - | 0.908 | 0.908 | 0.000 | 1.62x | 27.6/31.8% | 5.4% | 3 |
| event | 0.387 | - | - | 0.530 | 0.533 | 0.000 | 1.50x | 18.5/24.8% | 5.5% | 3 |
| backbone | 0.960 | - | - | 0.993 | 0.993 | 0.544 | 1.08x | 31.6/34.5% | 5.5% | 3 |

> siting-mix=local-typical: misdecodes 1

### `R-srretries` - sr-retries  `--scenario valleys`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 0.804 | - | - | 0.941 | 0.944 | 0.426 | 1.14x | 19.4/21.5% | 4.7% | 3 |
| 1 | 0.817 | - | - | 0.954 | 0.954 | 0.434 | 1.15x | 19.5/21.6% | 4.8% | 3 |
| 2 | 0.817 | - | - | 0.955 | 0.955 | 0.400 | 1.15x | 19.7/21.7% | 4.8% | 3 |
| 4 | 0.819 | - | - | 0.955 | 0.955 | 0.437 | 1.15x | 19.6/21.6% | 4.8% | 3 |

### `R-traceroute` - traceroute-per-hour  `--scenario valleys`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 0.25 | 0.804 | - | - | 0.941 | 0.941 | 0.427 | 1.31x | 22.1/24.7% | 5.4% | 3 |
| 1.0 | 0.791 | - | - | 0.935 | 0.936 | 0.409 | 1.41x | 24.1/26.8% | 6.0% | 3 |
| 4.0 | 0.765 | - | - | 0.919 | 0.924 | 0.392 | 1.77x | 30.8/34.0% | 7.8% | 3 |

### `R-traceroute-small` - traceroute-per-hour  `--scenario valleys`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.645 | - | - | 0.772 | 0.867 | 0.388 | 5.98x | 75.2/80.4% | 12.5% | 3 |
| 1.0 | 0.586 | - | - | 0.704 | 0.823 | 0.356 | 6.50x | 76.8/81.3% | 13.9% | 3 |

> traceroute-per-hour=0.0: queue drops 13.9% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 69

> traceroute-per-hour=1.0: queue drops 20.8% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 62

### `R-versions` - profile  `--scenario valleys`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 0.805 | - | - | 0.950 | 0.950 | 0.000 | 0.71x | 12.7/15.6% | 2.5% | 3 |
| 2.5 | 0.805 | - | - | 0.945 | 0.947 | 0.000 | 0.71x | 12.5/15.1% | 2.5% | 3 |
| 2.6 | 0.800 | - | - | 0.946 | 0.948 | 0.000 | 0.68x | 12.4/15.4% | 2.5% | 3 |
| 2.7 | 0.804 | - | - | 0.943 | 0.944 | 0.000 | 0.68x | 13.1/15.8% | 3.0% | 3 |
| 2.8 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |

### `R-warm` - warm-num-nodes  `--scenario valleys`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 0.645 | - | - | 0.772 | 0.867 | 0.388 | 5.98x | 75.2/80.4% | 12.5% | 3 |
| 25 | 0.645 | - | - | 0.772 | 0.867 | 0.388 | 5.98x | 75.2/80.4% | 12.5% | 3 |
| 100 | 0.645 | - | - | 0.772 | 0.867 | 0.388 | 5.98x | 75.2/80.4% | 12.5% | 3 |
| 2000 | 0.645 | - | - | 0.772 | 0.867 | 0.388 | 5.98x | 75.2/80.4% | 12.5% | 3 |

> warm-num-nodes=0: queue drops 13.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 69

> warm-num-nodes=25: queue drops 13.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 69

> warm-num-nodes=100: queue drops 13.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 69

> warm-num-nodes=2000: queue drops 13.9% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 69

### `X-amplifiers` - amplifier-mix  `--scenario valleys`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| sprinkled | 0.868 | - | - | 0.935 | 0.935 | 0.635 | 1.22x | 23.8/27.6% | 5.2% | 3 |
| arms-race | 0.906 | - | - | 0.940 | 0.940 | 0.607 | 1.02x | 24.9/26.3% | 5.3% | 3 |

### `X-amplify-worst` - amplify-worst  `--scenario valleys`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 0.1 | 0.852 | - | - | 0.992 | 0.993 | 0.443 | 1.26x | 22.0/24.6% | 5.4% | 3 |
| 0.3 | 0.938 | - | - | 0.995 | 0.995 | 0.734 | 1.11x | 24.8/27.0% | 5.2% | 3 |

### `X-badrouters` - role-placement  `--scenario valleys`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 0.694 | - | - | 0.892 | 0.893 | 0.000 | 1.06x | 20.3/22.9% | 5.5% | 3 |
| inverse | 0.706 | - | - | 0.911 | 0.914 | 0.000 | 1.09x | 17.3/20.9% | 3.4% | 3 |
| random | 0.704 | - | - | 0.911 | 0.913 | 0.113 | 1.03x | 18.1/20.8% | 4.2% | 3 |

### `X-chatty` - broadcast-interval-s  `--scenario valleys`

*The device broadcast interval driven down to three times its default rate.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 0.829 | - | - | 0.951 | 0.951 | 0.415 | 0.86x | 14.7/16.2% | 3.6% | 3 |
| 900 | 0.755 | - | - | 0.913 | 0.914 | 0.413 | 1.95x | 33.1/36.7% | 8.1% | 3 |
| 300 | 0.496 | - | - | 0.690 | 0.773 | 0.267 | 4.32x | 64.5/68.8% | 15.6% | 3 |

> broadcast-interval-s=300: decode_failures 22

### `X-chatty-hops` - broadcast-interval-s  `--scenario valleys`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 0.879 | - | - | 0.942 | 0.943 | 0.569 | 0.95x | 15.1/16.4% | 3.5% | 3 |
| 900 | 0.817 | - | - | 0.907 | 0.910 | 0.454 | 2.21x | 35.3/38.7% | 8.4% | 3 |
| 300 | 0.554 | - | - | 0.732 | 0.773 | 0.243 | 4.88x | 68.2/72.7% | 16.9% | 3 |

> broadcast-interval-s=300: decode_failures 27

### `X-duct` - duct-per-hour  `--scenario valleys`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 0.25 | 0.833 | - | - | 0.952 | 0.953 | 0.419 | 1.20x | 21.6/24.0% | 5.2% | 3 |
| 1.0 | 0.891 | - | - | 0.970 | 0.971 | 0.387 | 0.99x | 23.4/24.8% | 5.2% | 3 |

### `X-noise` - noise-profile  `--scenario valleys`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| temporal | 0.710 | - | - | 0.918 | 0.921 | 0.254 | 1.26x | 21.4/24.0% | 5.1% | 3 |
| transient | 0.809 | - | - | 0.945 | 0.946 | 0.458 | 1.27x | 21.1/23.6% | 5.2% | 3 |
| periodic | 0.648 | - | - | 0.785 | 0.790 | 0.290 | 1.17x | 19.6/21.7% | 4.5% | 3 |

### `X-nomute` - role-mix  `--scenario valleys`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 0.694 | - | - | 0.892 | 0.893 | 0.000 | 1.06x | 20.3/22.9% | 5.5% | 3 |
| no-mute | 0.785 | - | - | 0.957 | 0.959 | 0.382 | 1.25x | 20.5/23.6% | 5.3% | 3 |
| all-routers | 0.851 | - | - | 0.951 | 0.952 | 0.637 | 2.62x | 37.1/38.1% | 5.3% | 3 |

> faster: 1.6 s per simulated hour against 3.91 over 2 prior run(s) - 2.4x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `X-pulse` - noise-pulse-interval-ms  `--scenario valleys`

*How often the periodic emitter fires.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 0.743 | - | - | 0.892 | 0.893 | 0.375 | 1.22x | 20.8/23.2% | 5.0% | 3 |
| 10000 | 0.648 | - | - | 0.785 | 0.790 | 0.290 | 1.17x | 19.6/21.7% | 4.5% | 3 |
| 4000 | 0.384 | - | - | 0.492 | 0.537 | 0.122 | 1.00x | 17.1/18.8% | 3.4% | 3 |
| 2000 | 0.096 | - | - | 0.120 | 0.192 | 0.029 | 0.71x | 12.4/13.7% | 1.8% | 3 |

### `X-siting` - siting-mix  `--scenario valleys`

*Siting against a real role census, including a basement-heavy mesh.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.694 | - | - | 0.892 | 0.893 | 0.000 | 1.06x | 20.3/22.9% | 5.5% | 3 |
| local-typical | 0.660 | - | - | 0.852 | 0.853 | 0.000 | 1.30x | 23.5/29.3% | 5.5% | 3 |
| basement-heavy | 0.084 | - | - | 0.132 | 0.144 | 0.000 | 0.53x | 7.3/11.7% | 3.0% | 3 |

> siting-mix=local-typical: misdecodes 1

> faster: 1.25 s per simulated hour against 4.06 over 2 prior run(s) - 3.2x quicker, which is worth a look: a fragmented mesh or an arm that stopped being read both cost less to simulate

### `X-stretch` - stretch  `--scenario valleys`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 0.808 | - | - | 0.944 | 0.944 | 0.439 | 1.25x | 21.1/23.4% | 5.2% | 3 |
| 1.25 | 0.601 | - | - | 0.687 | 0.778 | 0.111 | 1.35x | 17.9/22.8% | 5.0% | 3 |
| 1.5 | 0.391 | - | - | 0.657 | 0.708 | 0.000 | 1.37x | 16.9/22.0% | 5.4% | 3 |
| 2.0 | 0.133 | - | - | 0.315 | 0.378 | 0.000 | 0.86x | 8.4/11.7% | 3.3% | 3 |

> stretch=1.25: decode_failures 23

> stretch=1.5: decode_failures 13

> stretch=2.0: decode_failures 4

### `X-stretch-duct` - duct-per-hour  `--scenario valleys`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.391 | - | - | 0.657 | 0.708 | 0.000 | 1.37x | 16.9/22.0% | 5.4% | 3 |
| 1.0 | 0.683 | - | - | 0.844 | 0.852 | 0.438 | 1.04x | 18.7/22.0% | 4.7% | 3 |

> duct-per-hour=0.0: decode_failures 13

### `X-worst` - role-placement  `--scenario valleys`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 0.878 | - | - | 0.942 | 0.968 | 0.213 | 2.32x | 27.0/35.1% | 5.5% | 3 |
| inverse | 0.868 | - | - | 0.957 | 0.974 | 0.358 | 2.22x | 24.8/32.0% | 3.0% | 3 |

> role-placement=degree: decode_failures 108

> role-placement=inverse: decode_failures 82

> slower: 23.7 s per simulated hour against 2.89 over 2 prior run(s) - 8.2x, and a runtime regression is invisible to `timeout-minutes` until it fails a job outright

