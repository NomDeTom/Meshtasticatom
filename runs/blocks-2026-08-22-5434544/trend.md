# Sweep blocks-2026-08-22-5434544

- **sim version** `1.4.0`
- **transport** `0553092`
- **ground** rolling
- **seed base** 5434544 · seeds 5434544
- **blocks** 86 run, 1 missing
- **compute** 13.5 h of simulator time across every cell
- **generated** 2026-08-22T05:20:11+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>105 warnings</summary>

- SF-cadence: trigger=interval: misdecodes 11
- SF-cadence: trigger=interval: decode_failures 14
- SF-cadence: trigger=aimd: misdecodes 1
- SF-cadence: trigger=aimd: decode_failures 1
- SF-cadence: trigger=bucket+interval: misdecodes 12
- SF-capacity: capacity=4: decode_failures 102
- SF-capacity: capacity=8: decode_failures 62
- SF-capacity: capacity=16: decode_failures 3
- DG-burst: burst-loss=0.1: decode_failures 54
- DG-burst: burst-loss=0.2: decode_failures 42
- DG-burst: burst-loss=0.3: decode_failures 37
- AD-flooding: role-mix=baymesh-2026-08: decode_failures 29
- RT-hoplimit: hop-limit=3: decode_failures 1
- DG-loss: extra-loss=0.2: decode_failures 1
- DG-loss: extra-loss=0.3: decode_failures 1
- DG-outage: burst-loss=0.1: decode_failures 31
- DG-outage: burst-loss=0.2: decode_failures 42
- DG-outage: burst-loss=0.3: decode_failures 31
- RF-txpower: tx-power=22: decode_failures 8
- RF-txpower: tx-power=17: decode_failures 6
- SF-hops-flat: hops-apart=3: misdecodes 1
- SF-hops-flat: hops-apart=4: decode_failures 35
- SF-place-flat: place=spread: decode_failures 2
- SF-bucket-mode: bucket-mode=global: misdecodes 32
- SF-bucket-mode: bucket-mode=time: misdecodes 11
- SF-bucket-mode: bucket-mode=window: misdecodes 18
- SF-bucket-time: time-bucket-s=600: misdecodes 112
- SF-bucket-time: time-bucket-s=1800: misdecodes 11
- SF-bucket-time: time-bucket-s=3600: misdecodes 5
- SF-capacity-window: capacity=8: misdecodes 18
- SF-capacity-window: capacity=8: decode_failures 56
- SF-capacity-window: capacity=16: misdecodes 17
- SF-capacity-window: capacity=16: decode_failures 2
- SF-capacity-window: capacity=32: misdecodes 18
- SF-window-size: window-size=8: misdecodes 157
- SF-window-size: window-size=16: misdecodes 72
- SF-window-size: window-size=32: misdecodes 18
- MS-density: nodes=150: decode_failures 5
- RT-hopspread: hop-limit=3: decode_failures 1
- RT-spread: hop-spread=False: decode_failures 1
- SF-capacity-local: capacity=4: decode_failures 102
- SF-capacity-local: capacity=8: decode_failures 62
- SF-capacity-local: capacity=16: decode_failures 3
- SF-replay-order-broadcast: replay-ordering=heard: misdecodes 9
- SF-replay-order: replay-ordering=heard: misdecodes 10
- SF-hops-spread: hops-apart=3: misdecodes 1
- SF-hops-spread: hops-apart=4: decode_failures 35
- SF-hops-spread: hops-apart=5: decode_failures 25
- SF-place-spread: place=spread: decode_failures 2
- RF-bw500: preset=SHORT_TURBO: decode_failures 5
- RF-bw500: preset=LONG_TURBO: decode_failures 1
- SF-catchup: catch-up-hours=: misdecodes 12
- SF-catchup: catch-up-hours=02-06: decode_failures 40
- SF-catchup: catch-up-hours=00-08: decode_failures 41
- TH-congestion: no-congestion-scaling=True: queue drops 15.4% of transmissions - airtime here is measured through a cap
- TH-congestion: no-congestion-scaling=True: decode_failures 105
- RF-eu-presets: preset=SHORT_FAST: decode_failures 1
- RF-eu-presets: preset=NARROW_SLOW: decode_failures 47
- RF-preset: preset=SHORT_FAST: decode_failures 1
- RF-preset: preset=LONG_MODERATE: decode_failures 5
- BL-control: protocol=sr: misdecodes 1
- TH-congestion-input: congestion-input=hotstore: decode_failures 1
- TH-congestion-mode: congestion-mode=static: misdecodes 1
- PR-crladder: coding-rate-ladder=False: decode_failures 1
- PR-crladder: coding-rate-ladder=True: decode_failures 2
- PR-dmmode-cr: dm-mode=directed-with-late-flood: decode_failures 2
- PR-dmmode-cr: dm-mode=m4-early-flood: decode_failures 9
- DM-mode: dm-mode=directed-with-late-flood: decode_failures 1
- MS-hopscale: nodes=250: decode_failures 2
- MS-hopscale: nodes=500: decode_failures 151
- DB-hotstore-stress: max-num-nodes=10: decode_failures 92
- DB-hotstore-stress: max-num-nodes=120: decode_failures 1
- MS-oversubscribed: nodes=250: decode_failures 1
- MS-oversubscribed: nodes=500: decode_failures 49
- DB-platform: platform-mix=constrained: decode_failures 3
- RT-rebroadcast: rebroadcast-mode=CORE_PORTNUMS_ONLY: decode_failures 2
- MS-roles: role-mix=baymesh-2026-08: decode_failures 29
- SC-signing: signature-policy=STRICT: decode_failures 4
- MS-siting: siting-mix=local-typical: decode_failures 3
- LD-traceroute-small: traceroute-per-hour=0.0: queue drops 16.2% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=0.0: decode_failures 98
- LD-traceroute-small: traceroute-per-hour=1.0: queue drops 25.1% of transmissions - airtime here is measured through a cap
- LD-traceroute-small: traceroute-per-hour=1.0: decode_failures 86
- FW-versions: profile=2.6: decode_failures 2
- DB-warm: warm-num-nodes=0: queue drops 16.2% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=0: decode_failures 98
- DB-warm: warm-num-nodes=25: queue drops 16.2% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=25: decode_failures 98
- DB-warm: warm-num-nodes=100: queue drops 16.2% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=100: decode_failures 98
- DB-warm: warm-num-nodes=2000: queue drops 16.2% of transmissions - airtime here is measured through a cap
- DB-warm: warm-num-nodes=2000: decode_failures 98
- AD-badrouters: role-placement=degree: decode_failures 29
- LD-chatty-hops: broadcast-interval-s=300: queue drops 12.3% of transmissions - airtime here is measured through a cap
- LD-chatty-hops: broadcast-interval-s=300: decode_failures 38
- LD-chatty: broadcast-interval-s=300: decode_failures 29
- RF-noise: noise-profile=temporal: decode_failures 37
- AD-nomute: role-mix=baymesh-2026-08: decode_failures 29
- RF-pulse: noise-pulse-interval-ms=4000: decode_failures 5
- AD-siting: siting-mix=uniform: decode_failures 29
- AD-siting: siting-mix=local-typical: decode_failures 22
- RF-stretch-duct: duct-per-hour=0.0: decode_failures 7
- MS-stretch: stretch=1.25: decode_failures 23
- MS-stretch: stretch=1.5: decode_failures 7
- MS-stretch: stretch=2.0: decode_failures 2

</details>

Blocks that produced no JSON (their job failed, timed out, or was cancelled): `RF-preset-turbo`

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.3) - `moved` names which one this block travels in. `text` is the broadcast reach in the same cells, so an arm buying its measure while `text` falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `BL-control` | protocol | **held** | 0 → 0.988 | 0.988 | 0.879 → 0.889 | 1x bytes_on_air | up | 2 |
| `PR-protocol` | protocol | **held** | 0 → 0.985 | 0.985 | 0.867 → 0.879 | 1.2x bytes_on_air | up | 3 |
| `RF-txpower` | tx-power | **held** | 0.146 → 0.985 | 0.839 | 0.075 → 0.879 | 9x sr_airtime | down | 4 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.153 → 0.932 | 0.779 | 0.127 → 0.828 | 1e+02x sr_airtime | down | 4 |
| `AD-siting` | siting-mix | **held** | 0.163 → 0.922 | 0.759 | 0.045 → 0.795 | 10x sr_bytes | down | 3 |
| `MS-stretch` | stretch | **text** | 0.126 → 0.879 | 0.753 | 0.126 → 0.879 | 4.3x advert_bytes | down | 4 |
| `RF-bw500` | preset | **held** | 0.217 → 0.951 | 0.734 | 0.150 → 0.809 | 5.1x sr_airtime | up | 3 |
| `MS-siting` | siting-mix | **text** | 0.317 → 0.978 | 0.662 | 0.317 → 0.978 | 4.1x sr_airtime | up | 4 |
| `MS-hopscale` | nodes | **held** | 0.407 → 0.985 | 0.579 | 0.313 → 0.879 | 8.2x sr_bytes | down | 4 |
| `RF-eu-presets` | preset | **text** | 0.367 → 0.879 | 0.512 | 0.367 → 0.879 | 2x sr_airtime | up | 4 |
| `RF-preset` | preset | **text** | 0.367 → 0.879 | 0.512 | 0.367 → 0.879 | 2.3x sr_airtime | up | 3 |
| `MS-oversubscribed` | nodes | **held** | 0.413 → 0.923 | 0.510 | 0.317 → 0.768 | 4.8x bytes_on_air | down | 3 |
| `MS-topology` | topology | **text** | 0.570 → 0.950 | 0.380 | 0.570 → 0.950 | 2x sr_bytes | up | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.591 → 0.936 | 0.345 | 0.591 → 0.936 | 9.2x sr_airtime | down | 3 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.561 → 0.906 | 0.345 | 0.561 → 0.906 | 9.8x sr_airtime | down | 3 |
| `DG-outage` | burst-loss | **text** | 0.551 → 0.879 | 0.328 | 0.551 → 0.879 | 1.8x sr_bytes | down | 4 |
| `DG-burst` | burst-loss | **text** | 0.591 → 0.879 | 0.288 | 0.591 → 0.879 | 2x sr_bytes | down | 4 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.472 → 0.759 | 0.287 | 0.472 → 0.759 | 1.7x sr_airtime | up | 2 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.643 → 0.928 | 0.286 | 0.340 → 0.557 | 4.6x sr_airtime | up | 3 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.714 → 0.961 | 0.247 | 0.714 → 0.961 | 5x sr_airtime | down | 2 |
| `RT-hoplimit` | hop-limit | **text** | 0.727 → 0.936 | 0.209 | 0.727 → 0.936 | 2x sr_bytes | up | 4 |
| `RT-hopspread` | hop-limit | **text** | 0.727 → 0.926 | 0.198 | 0.727 → 0.926 | 1.9x sr_bytes | up | 3 |
| `MS-size` | nodes | **text** | 0.721 → 0.879 | 0.158 | 0.721 → 0.879 | 6.7x sr_bytes | down | 5 |
| `RT-spread` | hop-spread | **text** | 0.727 → 0.879 | 0.152 | 0.727 → 0.879 | 1.8x sr_bytes | up | 2 |
| `RF-noise` | noise-profile | **text** | 0.729 → 0.879 | 0.150 | 0.729 → 0.879 | 1.6x sr_bytes | down | 4 |
| `MS-density` | nodes | **text** | 0.818 → 0.965 | 0.147 | 0.818 → 0.965 | 5.5x sr_airtime | up | 5 |
| `AD-flooding` | role-mix | **text** | 0.795 → 0.927 | 0.132 | 0.795 → 0.927 | 2.6x sr_bytes | up | 2 |
| `AD-nomute` | role-mix | **text** | 0.795 → 0.927 | 0.132 | 0.795 → 0.927 | 2.6x sr_bytes | up | 3 |
| `SC-signing` | signature-policy | **text** | 0.757 → 0.879 | 0.122 | 0.757 → 0.879 | 1.2x sr_airtime | down | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.816 → 0.917 | 0.100 | 0.816 → 0.917 | 2.2x sr_airtime | up | 4 |
| `DG-loss` | extra-loss | **text** | 0.779 → 0.879 | 0.100 | 0.779 → 0.879 | 1.4x sr_bytes | down | 4 |
| `DB-platform` | platform-mix | **text** | 0.818 → 0.917 | 0.099 | 0.818 → 0.917 | 2.3x sr_airtime | down | 3 |
| `MS-roles` | role-mix | **text** | 0.795 → 0.891 | 0.096 | 0.795 → 0.891 | 1.6x sr_bytes | down | 2 |
| `AD-badrouters` | role-placement | **text** | 0.783 → 0.872 | 0.090 | 0.783 → 0.872 | 1.8x sr_bytes | up | 3 |
| `MS-roles-fav` | role-mix | **text** | 0.813 → 0.901 | 0.088 | 0.813 → 0.901 | 1.4x sr_bytes | down | 2 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.879 → 0.967 | 0.088 | 0.879 → 0.967 | 1.6x sr_bytes | up | 3 |
| `SF-cadence` | trigger | **held** | 0.907 → 0.985 | 0.079 | 0.860 → 0.879 | 13x advert_bytes | down | 4 |
| `LD-interval` | broadcast-interval-s | **text** | 0.843 → 0.920 | 0.077 | 0.843 → 0.920 | 4.8x sr_airtime | up | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.909 → 0.985 | 0.076 | 0.879 → 0.883 | 19x sr_airtime | down | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.635 → 0.706 | 0.071 | 0.635 → 0.706 | 1.3x sr_airtime | down | 2 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.879 → 0.950 | 0.071 | 0.879 → 0.950 | 2.5x sr_bytes | up | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.879 → 0.947 | 0.067 | 0.879 → 0.947 | 1.6x bytes_on_air | up | 3 |
| `SF-place-flat` | place | **text** | 0.866 → 0.921 | 0.054 | 0.866 → 0.921 | 3.6x sr_bytes | down | 6 |
| `SF-place-spread` | place | **text** | 0.866 → 0.921 | 0.054 | 0.866 → 0.921 | 3.6x sr_bytes | down | 6 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.832 → 0.885 | 0.052 | 0.832 → 0.885 | 1.5x sr_airtime | down | 4 |
| `SF-catchup` | catch-up-hours | **held** | 0.937 → 0.978 | 0.040 | 0.860 → 0.878 | 9.4x advert_bytes | down | 3 |
| `AD-worst` | role-placement | **text** | 0.782 → 0.821 | 0.039 | 0.782 → 0.821 | 1.1x sr_bytes | down | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.879 → 0.917 | 0.038 | 0.879 → 0.917 | 3.3x bytes_on_air | down | 2 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.879 → 0.917 | 0.038 | 0.879 → 0.917 | 2.2x bytes_on_air | up | 4 |
| `FW-versions` | profile | **text** | 0.879 → 0.916 | 0.036 | 0.879 → 0.916 | 3.3x bytes_on_air | down | 5 |
| `SF-provide-transport` | provide-transport | **text** | 0.879 → 0.914 | 0.035 | 0.879 → 0.914 | 3.4x sr_airtime | up | 2 |
| `FW-mixed` | legacy-fraction | **text** | 0.879 → 0.913 | 0.034 | 0.879 → 0.913 | 2.1x bytes_on_air | up | 4 |
| `TH-congestion-input` | congestion-input | **text** | 0.547 → 0.582 | 0.034 | 0.547 → 0.582 | 1.4x sr_airtime | up | 2 |
| `SF-hops-flat` | hops-apart | **held** | 0.955 → 0.988 | 0.034 | 0.871 → 0.889 | 3.2x sr_bytes | up | 4 |
| `SF-hops-spread` | hops-apart | **held** | 0.955 → 0.988 | 0.034 | 0.871 → 0.893 | 3.2x sr_bytes | up | 5 |
| `SF-capacity-window` | capacity | **held** | 0.955 → 0.986 | 0.031 | 0.882 → 0.883 | 2x advert_bytes | up | 3 |
| `FW-firmware` | profile | **text** | 0.879 → 0.910 | 0.031 | 0.879 → 0.910 | 3.2x bytes_on_air | down | 2 |
| `LD-diurnal` | diurnal | **text** | 0.879 → 0.903 | 0.024 | 0.879 → 0.903 | 1.3x sr_bytes | down | 3 |
| `MS-router-late` | router-late-fraction | **text** | 0.878 → 0.900 | 0.022 | 0.878 → 0.900 | 1.6x sr_bytes | up | 4 |
| `SF-servers-flat` | servers | **held** | 0.971 → 0.993 | 0.022 | 0.879 → 0.887 | 5.4x sr_bytes | up | 4 |
| `SF-servers-spread` | servers | **held** | 0.971 → 0.993 | 0.022 | 0.879 → 0.887 | 5.4x sr_bytes | up | 4 |
| `SF-sr-retries` | sr-retries | **text** | 0.865 → 0.882 | 0.017 | 0.865 → 0.882 | 1.2x sr_bytes | down | 4 |
| `RT-favourites` | favourite-routers | **text** | 0.881 → 0.895 | 0.014 | 0.881 → 0.895 | 1.1x sr_bytes | up | 2 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.873 → 0.887 | 0.014 | 0.873 → 0.887 | 5.3x advert_bytes | up | 3 |
| `DM-mode` | dm-mode | **held** | 0.963 → 0.976 | 0.012 | 0.842 → 0.844 | 1.2x sr_airtime | down | 3 |
| `SF-window-size` | window-size | **text** | 0.876 → 0.887 | 0.011 | 0.876 → 0.887 | 5.2x advert_bytes | up | 3 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.838 → 0.849 | 0.011 | 0.838 → 0.849 | 1.1x sr_airtime | down | 2 |
| `SF-capacity` | capacity | **held** | 0.975 → 0.986 | 0.011 | 0.879 → 0.886 | 5.3x advert_bytes | up | 5 |
| `SF-capacity-local` | capacity | **held** | 0.975 → 0.986 | 0.011 | 0.879 → 0.886 | 5.3x advert_bytes | up | 5 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.879 → 0.889 | 0.010 | 0.879 → 0.889 | 2.6x advert_bytes | down | 4 |
| `SF-servers-allrouters` | servers | **text** | 0.866 → 0.876 | 0.010 | 0.866 → 0.876 | 2.9x sr_bytes | up | 2 |
| `SF-width` | short-id-bits | **text** | 0.879 → 0.888 | 0.009 | 0.879 → 0.888 | 3.1x advert_bytes | up | 4 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.952 → 0.961 | 0.009 | 0.952 → 0.961 | 1.2x sr_airtime | down | 2 |
| `RT-hopassign` | hop-assign | **held** | 0.985 → 0.994 | 0.008 | 0.879 → 0.880 | 1.2x sr_airtime | up | 2 |
| `SF-resolve` | resolve | **text** | 0.879 → 0.887 | 0.008 | 0.879 → 0.887 | 5.7x advert_bytes | = | 3 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.981 → 0.988 | 0.007 | 0.878 → 0.885 | 1.1x sr_airtime | down | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.981 → 0.988 | 0.007 | 0.878 → 0.885 | 1.1x sr_airtime | down | 4 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.844 → 0.849 | 0.004 | 0.844 → 0.849 | 1.1x sr_airtime | up | 2 |
| `SF-replay-order` | replay-ordering | **text** | 0.879 → 0.882 | 0.003 | 0.879 → 0.882 | 1x sr_bytes | up | 2 |
| `PR-repeats` | extra-repeats | **held** | 0.985 → 0.989 | 0.003 | 0.879 → 0.879 | 1x bytes_on_air | up | 2 |
| `SF-advert-transport` | advert-transport | **text** | 0.877 → 0.879 | 0.002 | 0.877 → 0.879 | 2.5x sr_airtime | down | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.983 → 0.986 | 0.002 | 0.914 → 0.916 | 1.1x sr_airtime | up | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.961 → 0.963 | 0.002 | 0.961 → 0.963 | 1.1x sr_bytes | down | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.960 → 0.961 | 0.001 | 0.960 → 0.961 | 1x sr_airtime | down | 2 |

### Moved no delivery measure

Not the same as having done nothing: several arms hold delivery flat by design and differ in what they spend. Three ways of reconciling the same two sets had better agree on what is held; where they differ is the price.

| block | arm | price | cells |
| --- | --- | --- | --: |
| `SF-signed` | signed | 1.4x advert_bytes | 2 |
| `DB-warm` | warm-num-nodes | - | 4 |

## Every block

### `SF-cadence` - trigger  `--scenario rolling`

*When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| bucket | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| interval | 0.864 | - | - | 0.973 | 0.983 | 0.654 | 1.80x | 35.6/39.5% | 7.3% | 3 |
| aimd | 0.874 | - | - | 0.907 | 0.985 | 0.663 | 1.38x | 27.8/30.6% | 5.3% | 3 |
| bucket+interval | 0.860 | - | - | 0.978 | 0.978 | 0.659 | 1.85x | 36.4/40.4% | 7.3% | 3 |

> trigger=interval: misdecodes 11

> trigger=interval: decode_failures 14

> trigger=aimd: misdecodes 1

> trigger=aimd: decode_failures 1

> trigger=bucket+interval: misdecodes 12

### `SF-jitter-global` - advert-jitter-s  `--scenario rolling`

*Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.883 | - | - | 0.988 | 0.989 | 0.648 | 1.34x | 27.3/30.2% | 5.3% | 3 |
| 30 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 120 | 0.885 | - | - | 0.986 | 0.987 | 0.670 | 1.34x | 27.3/30.1% | 5.3% | 3 |
| 600 | 0.878 | - | - | 0.981 | 0.982 | 0.674 | 1.34x | 27.3/30.2% | 5.3% | 3 |

### `SF-resolve` - resolve  `--scenario rolling`

*How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| enum | 0.887 | - | - | 0.986 | 0.990 | 0.674 | 1.34x | 27.2/30.4% | 5.4% | 3 |
| hybrid | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |

### `SF-capacity` - capacity  `--scenario rolling`

*How many differences one sketch can decode before it fails and the exchange escalates.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 0.879 | - | - | 0.975 | 0.985 | 0.672 | 1.34x | 27.3/30.5% | 5.3% | 3 |
| 8 | 0.886 | - | - | 0.977 | 0.986 | 0.680 | 1.33x | 27.2/30.3% | 5.3% | 3 |
| 16 | 0.881 | - | - | 0.983 | 0.986 | 0.679 | 1.33x | 27.2/30.0% | 5.2% | 3 |
| 32 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 50 | 0.884 | - | - | 0.986 | 0.988 | 0.673 | 1.35x | 27.4/30.2% | 5.2% | 3 |

> capacity=4: decode_failures 102

> capacity=8: decode_failures 62

> capacity=16: decode_failures 3

### `SF-signed` - signed  `--scenario rolling`

*Whether the advert carries its 66-byte signature.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| True | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |

### `SF-width` - short-id-bits  `--scenario rolling`

*Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 16 | 0.883 | - | - | 0.984 | 0.986 | 0.682 | 1.33x | 27.1/29.9% | 5.2% | 3 |
| 24 | 0.880 | - | - | 0.990 | 0.991 | 0.656 | 1.31x | 26.5/29.4% | 5.2% | 3 |
| 32 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 64 | 0.888 | - | - | 0.991 | 0.992 | 0.674 | 1.36x | 27.5/30.4% | 5.3% | 3 |

### `DG-burst` - burst-loss  `--scenario rolling`

*The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 0.1 | 0.790 | - | - | 0.934 | 0.962 | 0.568 | 1.29x | 26.2/29.5% | 4.9% | 3 |
| 0.2 | 0.705 | - | - | 0.912 | 0.940 | 0.475 | 1.20x | 24.6/28.3% | 4.6% | 3 |
| 0.3 | 0.591 | - | - | 0.801 | 0.891 | 0.363 | 1.11x | 23.1/26.6% | 4.0% | 3 |

> burst-loss=0.1: decode_failures 54

> burst-loss=0.2: decode_failures 42

> burst-loss=0.3: decode_failures 37

### `AD-flooding` - role-mix  `--scenario rolling`

*Every node rebroadcasting everything, against a real role census.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 0.795 | - | - | 0.922 | 0.945 | 0.361 | 1.16x | 26.2/29.6% | 5.4% | 3 |
| all-routers | 0.927 | - | - | 0.990 | 0.992 | 0.739 | 2.81x | 44.4/48.9% | 5.3% | 3 |

> role-mix=baymesh-2026-08: decode_failures 29

### `RT-hoplimit` - hop-limit  `--scenario rolling`

*Hop limits past anything a release ships, to find where more hops stop helping.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.727 | - | - | 0.965 | 0.971 | 0.388 | 1.06x | 22.9/26.7% | 4.7% | 3 |
| 7 | 0.926 | - | - | 0.980 | 0.983 | 0.784 | 1.53x | 29.9/32.5% | 5.6% | 3 |
| 15 | 0.936 | - | - | 0.984 | 0.986 | 0.822 | 1.58x | 30.4/32.9% | 5.6% | 3 |
| 32 | 0.932 | - | - | 0.981 | 0.982 | 0.818 | 1.57x | 30.3/32.8% | 5.6% | 3 |

> hop-limit=3: decode_failures 1

### `DG-loss` - extra-loss  `--scenario rolling`

*A flat loss floor on every reception - degradation spread evenly across every bucket.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 0.1 | 0.860 | - | - | 0.984 | 0.984 | 0.624 | 1.43x | 28.8/32.3% | 5.4% | 3 |
| 0.2 | 0.817 | - | - | 0.962 | 0.971 | 0.584 | 1.47x | 29.0/33.1% | 5.3% | 3 |
| 0.3 | 0.779 | - | - | 0.943 | 0.958 | 0.510 | 1.49x | 29.7/34.2% | 5.2% | 3 |

> extra-loss=0.2: decode_failures 1

> extra-loss=0.3: decode_failures 1

### `DG-outage` - burst-loss  `--scenario rolling`

*Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 0.1 | 0.774 | - | - | 0.925 | 0.965 | 0.594 | 1.27x | 25.9/29.0% | 4.9% | 3 |
| 0.2 | 0.667 | - | - | 0.843 | 0.934 | 0.460 | 1.19x | 24.7/27.8% | 4.8% | 3 |
| 0.3 | 0.551 | - | - | 0.737 | 0.884 | 0.315 | 1.13x | 23.5/26.8% | 4.1% | 3 |

> burst-loss=0.1: decode_failures 31

> burst-loss=0.2: decode_failures 42

> burst-loss=0.3: decode_failures 31

### `RF-txpower` - tx-power  `--scenario rolling`

*Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 22 | 0.486 | - | - | 0.657 | 0.670 | 0.000 | 1.33x | 17.4/22.4% | 4.7% | 3 |
| 17 | 0.138 | - | - | 0.203 | 0.231 | 0.000 | 0.95x | 8.6/10.5% | 3.1% | 3 |
| 14 | 0.075 | - | - | 0.146 | 0.148 | 0.000 | 0.59x | 5.3/9.3% | 2.7% | 3 |

> tx-power=22: decode_failures 8

> tx-power=17: decode_failures 6

### `SF-servers-allrouters` - servers  `--scenario rolling`

*Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.866 | - | - | 0.952 | 0.952 | 0.664 | 1.32x | 27.3/29.8% | 5.2% | 3 |
| 6 | 0.876 | - | - | 0.960 | 0.960 | 0.663 | 1.36x | 28.2/30.9% | 5.4% | 6 |

### `SF-hops-flat` - hops-apart  `--scenario rolling`

*How many hops apart the archives are placed, under a flat hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.871 | - | - | 0.955 | 0.955 | 0.661 | 1.33x | 27.2/29.9% | 5.2% | 3 |
| 2 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 3 | 0.889 | - | - | 0.988 | 0.990 | 0.675 | 1.35x | 27.4/30.2% | 5.3% | 3 |
| 4 | 0.887 | - | - | 0.955 | 0.983 | 0.671 | 1.36x | 27.4/30.3% | 5.3% | 3 |

> hops-apart=3: misdecodes 1

> hops-apart=4: decode_failures 35

### `SF-place-flat` - place  `--scenario rolling`

*Where the archives sit, under a flat hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 0.921 | - | - | 0.979 | 0.982 | 0.660 | 1.39x | 27.8/30.6% | 5.4% | 3 |
| routers | 0.866 | - | - | 0.952 | 0.952 | 0.664 | 1.32x | 27.3/29.8% | 5.2% | 3 |
| alternate-routers | 0.874 | - | - | 0.948 | 0.948 | 0.677 | 1.35x | 27.7/30.3% | 5.2% | 3 |
| beside-router | 0.877 | - | - | 0.964 | 0.964 | 0.680 | 1.34x | 27.6/30.4% | 5.3% | 3 |
| random-clients | 0.898 | - | - | 0.984 | 0.988 | 0.686 | 1.34x | 27.0/29.9% | 5.1% | 3 |
| hops-apart | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |

> place=spread: decode_failures 2

### `SF-servers-flat` - servers  `--scenario rolling`

*How many archives the mesh has, under a flat hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 0.880 | - | - | 0.971 | 0.976 | 0.682 | 1.33x | 27.1/29.8% | 5.2% | 2 |
| 3 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 5 | 0.885 | - | - | 0.993 | 0.993 | 0.671 | 1.36x | 27.4/30.2% | 5.2% | 5 |
| 8 | 0.887 | - | - | 0.990 | 0.992 | 0.656 | 1.41x | 28.7/31.7% | 5.5% | 8 |

### `SF-bucket-mode` - bucket-mode  `--scenario rolling`

*What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| global | 0.889 | - | - | 0.986 | 0.991 | 0.681 | 1.37x | 27.7/30.6% | 5.3% | 3 |
| local | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| time | 0.887 | - | - | 0.990 | 0.991 | 0.685 | 1.37x | 27.7/30.7% | 5.3% | 3 |
| window | 0.883 | - | - | 0.986 | 0.991 | 0.662 | 1.35x | 27.4/30.4% | 5.3% | 3 |

> bucket-mode=global: misdecodes 32

> bucket-mode=time: misdecodes 11

> bucket-mode=window: misdecodes 18

### `SF-bucket-time` - time-bucket-s  `--scenario rolling`

*Width of the time bucket, when buckets are cut by the clock.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 600 | 0.873 | - | - | 0.983 | 0.987 | 0.658 | 1.53x | 30.6/33.7% | 5.9% | 3 |
| 1800 | 0.887 | - | - | 0.990 | 0.991 | 0.685 | 1.37x | 27.7/30.7% | 5.3% | 3 |
| 3600 | 0.885 | - | - | 0.983 | 0.986 | 0.679 | 1.35x | 27.3/30.1% | 5.2% | 3 |

> time-bucket-s=600: misdecodes 112

> time-bucket-s=1800: misdecodes 11

> time-bucket-s=3600: misdecodes 5

### `SF-capacity-window` - capacity  `--scenario rolling`

*Sketch capacity under windowed buckets rather than counted ones.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 0.883 | - | - | 0.955 | 0.987 | 0.659 | 1.33x | 27.2/30.1% | 5.2% | 3 |
| 16 | 0.882 | - | - | 0.983 | 0.990 | 0.664 | 1.33x | 27.1/29.9% | 5.2% | 3 |
| 32 | 0.883 | - | - | 0.986 | 0.991 | 0.662 | 1.35x | 27.4/30.4% | 5.3% | 3 |

> capacity=8: misdecodes 18

> capacity=8: decode_failures 56

> capacity=16: misdecodes 17

> capacity=16: decode_failures 2

> capacity=32: misdecodes 18

### `SF-window-size` - window-size  `--scenario rolling`

*Objects in the sliding window, when buckets are windowed.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 8 | 0.876 | - | - | 0.987 | 0.988 | 0.658 | 1.47x | 29.3/32.3% | 5.7% | 3 |
| 16 | 0.887 | - | - | 0.992 | 0.995 | 0.673 | 1.39x | 28.1/31.0% | 5.4% | 3 |
| 32 | 0.883 | - | - | 0.986 | 0.991 | 0.662 | 1.35x | 27.4/30.4% | 5.3% | 3 |

> window-size=8: misdecodes 157

> window-size=16: misdecodes 72

> window-size=32: misdecodes 18

### `MS-density` - nodes  `--scenario rolling`

*The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 0.818 | - | - | 0.942 | 0.953 | 0.658 | 1.56x | 34.7/36.0% | 7.0% | 3 |
| 60 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 90 | 0.956 | - | - | 0.998 | 0.998 | 0.828 | 1.57x | 27.5/31.4% | 5.0% | 3 |
| 120 | 0.961 | - | - | 0.999 | 0.999 | 0.785 | 2.00x | 37.5/41.8% | 5.4% | 3 |
| 150 | 0.965 | - | - | 0.999 | 0.999 | 0.886 | 2.59x | 47.7/55.2% | 5.4% | 3 |

> nodes=150: decode_failures 5

### `RT-hopspread` - hop-limit  `--scenario rolling`

*One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.727 | - | - | 0.965 | 0.971 | 0.388 | 1.06x | 22.9/26.7% | 4.7% | 3 |
| 5 | 0.879 | - | - | 0.982 | 0.984 | 0.699 | 1.41x | 28.0/31.1% | 5.4% | 3 |
| 7 | 0.926 | - | - | 0.980 | 0.983 | 0.784 | 1.53x | 29.9/32.5% | 5.6% | 3 |

> hop-limit=3: decode_failures 1

### `MS-size` - nodes  `--scenario rolling`

*Mesh size with density held constant - the area grows with the node count.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 40 | 0.836 | - | - | 0.940 | 0.942 | 0.339 | 1.43x | 31.2/37.5% | 7.4% | 3 |
| 60 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 90 | 0.841 | - | - | 0.985 | 0.986 | 0.330 | 1.66x | 21.1/25.0% | 5.4% | 3 |
| 120 | 0.766 | - | - | 0.916 | 0.918 | 0.423 | 2.13x | 21.5/25.7% | 4.8% | 3 |
| 150 | 0.721 | - | - | 0.921 | 0.921 | 0.147 | 2.81x | 25.2/29.4% | 6.1% | 3 |

### `RT-spread` - hop-spread  `--scenario rolling`

*A uniform hop limit against per-node limits of 3-7 assigned by centrality.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.727 | - | - | 0.965 | 0.971 | 0.388 | 1.06x | 22.9/26.7% | 4.7% | 3 |
| True | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |

> hop-spread=False: decode_failures 1

### `SF-advert-transport` - advert-transport  `--scenario rolling`

*Whether an archive advertises by broadcast or by DM to each known peer.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| broadcast | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| dm | 0.877 | - | - | 0.983 | 0.986 | 0.662 | 1.33x | 27.2/30.3% | 5.4% | 3 |

### `SF-provide-transport` - provide-transport  `--scenario rolling`

*Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| dm | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| broadcast | 0.914 | - | - | 0.983 | 0.988 | 0.748 | 1.46x | 29.6/32.4% | 5.7% | 3 |

### `SF-capacity-local` - capacity  `--scenario rolling`

*Sketch capacity under local numbering and the later defaults.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 4 | 0.879 | - | - | 0.975 | 0.985 | 0.672 | 1.34x | 27.3/30.5% | 5.3% | 3 |
| 8 | 0.886 | - | - | 0.977 | 0.986 | 0.680 | 1.33x | 27.2/30.3% | 5.3% | 3 |
| 16 | 0.881 | - | - | 0.983 | 0.986 | 0.679 | 1.33x | 27.2/30.0% | 5.2% | 3 |
| 32 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 50 | 0.884 | - | - | 0.986 | 0.988 | 0.673 | 1.35x | 27.4/30.2% | 5.2% | 3 |

> capacity=4: decode_failures 102

> capacity=8: decode_failures 62

> capacity=16: decode_failures 3

### `SF-replay-order-broadcast` - replay-ordering  `--scenario rolling`

*The same, with replays broadcast - the combination the replay header exists for.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 0.914 | - | - | 0.983 | 0.988 | 0.748 | 1.46x | 29.6/32.4% | 5.7% | 3 |
| heard | 0.916 | - | - | 0.986 | 0.988 | 0.760 | 1.45x | 29.3/32.1% | 5.6% | 3 |

> replay-ordering=heard: misdecodes 9

### `SF-jitter-local` - advert-jitter-s  `--scenario rolling`

*Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.883 | - | - | 0.988 | 0.989 | 0.648 | 1.34x | 27.3/30.2% | 5.3% | 3 |
| 30 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 120 | 0.885 | - | - | 0.986 | 0.987 | 0.670 | 1.34x | 27.3/30.1% | 5.3% | 3 |
| 600 | 0.878 | - | - | 0.981 | 0.982 | 0.674 | 1.34x | 27.3/30.2% | 5.3% | 3 |

### `SF-replay-order` - replay-ordering  `--scenario rolling`

*Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| tip | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| heard | 0.882 | - | - | 0.984 | 0.987 | 0.664 | 1.36x | 27.8/30.6% | 5.4% | 3 |

> replay-ordering=heard: misdecodes 10

### `SF-hops-spread` - hops-apart  `--scenario rolling`

*How many hops apart the archives are, under real per-node hop limits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.871 | - | - | 0.955 | 0.955 | 0.661 | 1.33x | 27.2/29.9% | 5.2% | 3 |
| 2 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 3 | 0.889 | - | - | 0.988 | 0.990 | 0.675 | 1.35x | 27.4/30.2% | 5.3% | 3 |
| 4 | 0.887 | - | - | 0.955 | 0.983 | 0.671 | 1.36x | 27.4/30.3% | 5.3% | 3 |
| 5 | 0.893 | - | - | 0.963 | 0.987 | 0.664 | 1.36x | 27.8/30.6% | 5.4% | 3 |

> hops-apart=3: misdecodes 1

> hops-apart=4: decode_failures 35

> hops-apart=5: decode_failures 25

### `SF-place-spread` - place  `--scenario rolling`

*Where the archives sit, under real per-node hop limits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| spread | 0.921 | - | - | 0.979 | 0.982 | 0.660 | 1.39x | 27.8/30.6% | 5.4% | 3 |
| routers | 0.866 | - | - | 0.952 | 0.952 | 0.664 | 1.32x | 27.3/29.8% | 5.2% | 3 |
| alternate-routers | 0.874 | - | - | 0.948 | 0.948 | 0.677 | 1.35x | 27.7/30.3% | 5.2% | 3 |
| beside-router | 0.877 | - | - | 0.964 | 0.964 | 0.680 | 1.34x | 27.6/30.4% | 5.3% | 3 |
| random-clients | 0.898 | - | - | 0.984 | 0.988 | 0.686 | 1.34x | 27.0/29.9% | 5.1% | 3 |
| hops-apart | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |

> place=spread: decode_failures 2

### `SF-servers-spread` - servers  `--scenario rolling`

*How many archives the mesh has, under real per-node hop limits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 0.880 | - | - | 0.971 | 0.976 | 0.682 | 1.33x | 27.1/29.8% | 5.2% | 2 |
| 3 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 5 | 0.885 | - | - | 0.993 | 0.993 | 0.671 | 1.36x | 27.4/30.2% | 5.2% | 5 |
| 8 | 0.887 | - | - | 0.990 | 0.992 | 0.656 | 1.41x | 28.7/31.7% | 5.5% | 8 |

### `RF-bw500` - preset  `--scenario rolling`

*Spreading factor with bandwidth held at 500 kHz, where North America is heading.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_TURBO | 0.150 | - | - | 0.217 | 0.240 | 0.000 | 0.04x | 0.4/0.5% | 0.2% | 3 |
| MEDIUM_TURBO | 0.513 | - | - | 0.734 | 0.734 | 0.000 | 0.30x | 4.3/5.9% | 1.2% | 3 |
| LONG_TURBO | 0.809 | - | - | 0.951 | 0.956 | 0.507 | 1.33x | 24.1/27.2% | 5.1% | 3 |

> preset=SHORT_TURBO: decode_failures 5

> preset=LONG_TURBO: decode_failures 1

### `SF-catchup` - catch-up-hours  `--scenario rolling`

*The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
|  | 0.860 | - | - | 0.978 | 0.978 | 0.659 | 1.85x | 36.4/40.4% | 7.3% | 3 |
| 02-06 | 0.877 | - | - | 0.937 | 0.984 | 0.674 | 1.40x | 28.3/31.3% | 5.5% | 3 |
| 00-08 | 0.878 | - | - | 0.946 | 0.987 | 0.680 | 1.48x | 29.5/32.8% | 5.8% | 3 |

> catch-up-hours=: misdecodes 12

> catch-up-hours=02-06: decode_failures 40

> catch-up-hours=00-08: decode_failures 41

### `TH-congestion` - no-congestion-scaling  `--scenario rolling`

*The firmware's node-count interval scaling, on against off.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.961 | - | - | 0.999 | 0.999 | 0.785 | 2.00x | 37.5/41.8% | 5.4% | 3 |
| True | 0.714 | - | - | 0.802 | 0.908 | 0.549 | 5.50x | 74.9/79.1% | 13.1% | 3 |

> no-congestion-scaling=True: queue drops 15.4% of transmissions - airtime here is measured through a cap

> no-congestion-scaling=True: decode_failures 105

### `LD-diurnal` - diurnal  `--scenario rolling`

*Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flat | 0.903 | - | - | 0.991 | 0.993 | 0.702 | 1.25x | 25.4/27.9% | 4.9% | 3 |
| sinusoid | 0.886 | - | - | 0.989 | 0.991 | 0.670 | 1.23x | 25.0/27.4% | 4.8% | 3 |
| commuter | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |

### `RF-eu-presets` - preset  `--scenario rolling`

*The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 0.367 | - | - | 0.547 | 0.554 | 0.000 | 0.15x | 1.9/2.6% | 0.6% | 3 |
| LONG_FAST | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| LITE_FAST | 0.828 | - | - | 0.960 | 0.962 | 0.538 | 1.05x | 21.3/23.1% | 4.2% | 3 |
| NARROW_SLOW | 0.840 | - | - | 0.947 | 0.960 | 0.590 | 1.33x | 26.8/29.3% | 5.3% | 3 |

> preset=SHORT_FAST: decode_failures 1

> preset=NARROW_SLOW: decode_failures 47

### `RF-preset` - preset  `--scenario rolling`

*The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| SHORT_FAST | 0.367 | - | - | 0.547 | 0.554 | 0.000 | 0.15x | 1.9/2.6% | 0.6% | 3 |
| LONG_FAST | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| LONG_MODERATE | 0.833 | - | - | 0.951 | 0.957 | 0.638 | 3.45x | 67.4/70.1% | 11.8% | 3 |

> preset=SHORT_FAST: decode_failures 1

> preset=LONG_MODERATE: decode_failures 5

### `BL-control` - protocol  `--scenario rolling`

*The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.879 | - | - | 0 | 0.000 | 0.678 | 1.33x | 27.1/29.7% | 5.1% | 3 |
| sr | 0.889 | - | - | 0.988 | 0.990 | 0.675 | 1.35x | 27.4/30.2% | 5.3% | 3 |

> protocol=sr: misdecodes 1

### `RT-hopassign` - hop-assign  `--scenario rolling`

*Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| centrality | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| random | 0.880 | - | - | 0.994 | 0.995 | 0.688 | 1.34x | 27.2/30.0% | 5.2% | 3 |

### `LD-interval` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval - the denominator every SF++ airtime share is quoted against.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 900 | 0.843 | - | - | 0.977 | 0.981 | 0.608 | 2.13x | 42.5/47.0% | 8.2% | 3 |
| 3600 | 0.906 | - | - | 0.995 | 0.996 | 0.677 | 0.89x | 18.3/20.0% | 3.5% | 3 |
| 10800 | 0.913 | - | - | 0.995 | 0.995 | 0.697 | 0.61x | 12.3/13.4% | 2.4% | 3 |
| 43200 | 0.920 | - | - | 0.996 | 0.997 | 0.714 | 0.45x | 9.2/9.9% | 1.8% | 3 |

### `PR-protocol` - protocol  `--scenario rolling`

*Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.879 | - | - | 0 | 0.000 | 0.678 | 1.33x | 27.1/29.7% | 5.1% | 3 |
| chain | 0.867 | - | - | 0.911 | 0.987 | 0.680 | 1.54x | 31.0/34.2% | 5.9% | 3 |
| sr | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |

### `MS-topology` - topology  `--scenario rolling`

*The shape of the mesh, at fixed node count and seed.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| clustered | 0.911 | - | - | 0.956 | 0.957 | 0.591 | 1.18x | 28.0/30.3% | 5.3% | 3 |
| corridor | 0.570 | - | - | 0.708 | 0.719 | 0.423 | 1.19x | 20.0/23.6% | 4.9% | 3 |
| hub | 0.950 | - | - | 0.977 | 0.978 | 0.850 | 1.15x | 36.6/37.1% | 5.6% | 3 |

### `RT-adopt` - no-adopt-hop-recommendation  `--scenario rolling`

*The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.961 | - | - | 0.999 | 0.999 | 0.785 | 2.00x | 37.5/41.8% | 5.4% | 3 |
| True | 0.952 | - | - | 0.998 | 0.999 | 0.767 | 2.39x | 42.6/46.8% | 6.1% | 3 |

### `TH-congestion-input` - congestion-input  `--scenario rolling`

*Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| hotstore | 0.547 | - | - | 0.918 | 0.920 | 0.176 | 4.55x | 28.6/39.3% | 5.8% | 3 |
| truesize | 0.582 | - | - | 0.942 | 0.942 | 0.176 | 3.41x | 23.1/31.8% | 4.8% | 3 |

> congestion-input=hotstore: decode_failures 1

### `TH-congestion-mode` - congestion-mode  `--scenario rolling`

*Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| static | 0.963 | - | - | 0.999 | 0.999 | 0.812 | 1.90x | 34.9/38.8% | 5.1% | 3 |
| adaptive | 0.961 | - | - | 0.999 | 0.999 | 0.785 | 2.00x | 37.5/41.8% | 5.4% | 3 |

> congestion-mode=static: misdecodes 1

### `PR-crladder` - coding-rate-ladder  `--scenario rolling`

*Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.844 | - | - | 0.964 | 0.984 | 0.647 | 1.67x | 33.8/37.4% | 6.6% | 3 |
| True | 0.849 | - | - | 0.964 | 0.982 | 0.643 | 1.68x | 34.1/37.7% | 6.7% | 3 |

> coding-rate-ladder=False: decode_failures 1

> coding-rate-ladder=True: decode_failures 2

### `DM-mode` - dm-mode  `--scenario rolling`

*How a DM escalates to flooding.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| flood-only | 0.842 | - | - | 0.976 | 0.983 | 0.631 | 1.87x | 37.5/41.0% | 7.2% | 3 |
| directed-with-late-flood | 0.844 | - | - | 0.964 | 0.984 | 0.647 | 1.67x | 33.8/37.4% | 6.6% | 3 |
| m4-early-flood | 0.843 | - | - | 0.963 | 0.980 | 0.646 | 1.67x | 33.9/37.4% | 6.6% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 1

### `PR-dmmode-cr` - dm-mode  `--scenario rolling`

*DM escalation with the coding-rate ladder already on, since both spend the same retry budget.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| directed-with-late-flood | 0.849 | - | - | 0.964 | 0.982 | 0.643 | 1.68x | 34.1/37.7% | 6.7% | 3 |
| m4-early-flood | 0.838 | - | - | 0.965 | 0.982 | 0.635 | 1.67x | 33.9/37.4% | 6.7% | 3 |

> dm-mode=directed-with-late-flood: decode_failures 2

> dm-mode=m4-early-flood: decode_failures 9

### `RT-favourites` - favourite-routers  `--scenario rolling`

*Router-like nodes favouriting each other, so relays between them keep their hop limit.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.881 | - | - | 0.985 | 0.987 | 0.691 | 1.49x | 32.4/36.7% | 5.4% | 3 |
| True | 0.895 | - | - | 0.983 | 0.984 | 0.719 | 1.53x | 33.0/37.3% | 5.3% | 3 |

### `FW-firmware` - profile  `--scenario rolling`

*The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy | 0.910 | - | - | 0.991 | 0.992 | 0.674 | 0.75x | 12.8/15.4% | 2.0% | 3 |
| 2.8 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |

### `MS-hopscale` - nodes  `--scenario rolling`

*How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 60 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 120 | 0.766 | - | - | 0.916 | 0.918 | 0.423 | 2.13x | 21.5/25.7% | 4.8% | 3 |
| 250 | 0.546 | - | - | 0.918 | 0.918 | 0.163 | 4.83x | 30.7/42.2% | 6.2% | 3 |
| 500 | 0.313 | - | - | 0.407 | 0.428 | 0.046 | 10.27x | 31.5/50.5% | 5.7% | 3 |

> nodes=250: decode_failures 2

> nodes=500: decode_failures 151

### `DB-hotstore` - max-num-nodes  `--scenario rolling`

*The modelled MAX_NUM_NODES - the size of the hot store.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 0.816 | - | - | 0.949 | 0.955 | 0.629 | 3.19x | 62.3/68.5% | 10.1% | 3 |
| 100 | 0.917 | - | - | 0.990 | 0.992 | 0.743 | 1.61x | 34.3/38.8% | 5.3% | 3 |
| 120 | 0.917 | - | - | 0.990 | 0.992 | 0.743 | 1.61x | 34.3/38.8% | 5.3% | 3 |
| 250 | 0.917 | - | - | 0.990 | 0.992 | 0.743 | 1.61x | 34.3/38.8% | 5.3% | 3 |

### `DB-hotstore-stress` - max-num-nodes  `--scenario rolling`

*The store size against a fixed 250-node mesh, so eviction is constant.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 10 | 0.340 | - | - | 0.643 | 0.698 | 0.131 | 11.79x | 59.9/70.8% | 10.9% | 3 |
| 120 | 0.547 | - | - | 0.918 | 0.920 | 0.176 | 4.55x | 28.6/39.3% | 5.8% | 3 |
| 250 | 0.557 | - | - | 0.928 | 0.929 | 0.172 | 4.41x | 27.7/37.9% | 5.6% | 3 |

> max-num-nodes=10: decode_failures 92

> max-num-nodes=120: decode_failures 1

### `FW-mixed` - legacy-fraction  `--scenario rolling`

*A mesh part-way through upgrading, the older share on 2.5.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 0.25 | 0.909 | - | - | 0.991 | 0.991 | 0.605 | 1.17x | 23.3/26.1% | 4.7% | 3 |
| 0.5 | 0.904 | - | - | 0.991 | 0.993 | 0.636 | 0.94x | 16.6/20.3% | 3.7% | 3 |
| 0.75 | 0.913 | - | - | 0.990 | 0.992 | 0.731 | 0.90x | 16.4/18.0% | 2.5% | 3 |

### `FW-mixed-26` - legacy-fraction  `--scenario rolling`

*The same with the older share on 2.6.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 0.25 | 0.904 | - | - | 0.980 | 0.980 | 0.633 | 1.15x | 23.2/25.7% | 4.6% | 3 |
| 0.5 | 0.896 | - | - | 0.988 | 0.990 | 0.625 | 0.97x | 17.1/21.1% | 3.9% | 3 |
| 0.75 | 0.917 | - | - | 0.991 | 0.995 | 0.746 | 0.87x | 16.2/18.1% | 2.4% | 3 |

### `MS-oversubscribed` - nodes  `--scenario rolling`

*Mesh size against a store that has to hold it, over a full day.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 120 | 0.768 | - | - | 0.923 | 0.927 | 0.425 | 1.99x | 19.9/24.0% | 4.4% | 3 |
| 250 | 0.547 | - | - | 0.918 | 0.920 | 0.176 | 4.55x | 28.6/39.3% | 5.8% | 3 |
| 500 | 0.317 | - | - | 0.413 | 0.431 | 0.050 | 9.46x | 28.7/45.9% | 5.2% | 3 |

> nodes=250: decode_failures 1

> nodes=500: decode_failures 49

### `DB-platform` - platform-mix  `--scenario rolling`

*The board mix, which decides each node's hot-store size.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.917 | - | - | 0.990 | 0.992 | 0.743 | 1.61x | 34.3/38.8% | 5.3% | 3 |
| baymesh-2026-08 | 0.917 | - | - | 0.990 | 0.992 | 0.743 | 1.61x | 34.3/38.8% | 5.3% | 3 |
| constrained | 0.818 | - | - | 0.941 | 0.952 | 0.619 | 3.18x | 62.1/68.3% | 10.0% | 3 |

> platform-mix=constrained: decode_failures 3

### `RT-rebroadcast` - rebroadcast-mode  `--scenario rolling`

*The rebroadcast mode - what a node relays.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| ALL | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| KNOWN_ONLY | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| CORE_PORTNUMS_ONLY | 0.883 | - | - | 0.909 | 0.993 | 0.668 | 1.29x | 26.3/28.9% | 5.0% | 3 |

> rebroadcast-mode=CORE_PORTNUMS_ONLY: decode_failures 2

### `PR-repeats` - extra-repeats  `--scenario rolling`

*The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| True | 0.879 | - | - | 0.989 | 0.991 | 0.670 | 1.39x | 28.2/31.0% | 5.4% | 3 |

### `PR-repeats-busy` - extra-repeats  `--scenario rolling`

*The same, on a mesh busy enough for the suppression thresholds to be deciding it.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.961 | - | - | 0.999 | 0.999 | 0.785 | 2.00x | 37.5/41.8% | 5.4% | 3 |
| True | 0.960 | - | - | 0.998 | 0.999 | 0.795 | 2.04x | 37.9/42.2% | 5.4% | 3 |

### `MS-roles` - role-mix  `--scenario rolling`

*The legacy default role census against a real mesh's.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 0.891 | - | - | 0.986 | 0.988 | 0.712 | 1.37x | 27.7/30.6% | 5.3% | 3 |
| baymesh-2026-08 | 0.795 | - | - | 0.922 | 0.945 | 0.361 | 1.16x | 26.2/29.6% | 5.4% | 3 |

> role-mix=baymesh-2026-08: decode_failures 29

### `MS-roles-fav` - role-mix  `--scenario rolling`

*The same with router favourites on.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| legacy-default | 0.901 | - | - | 0.979 | 0.983 | 0.709 | 1.41x | 28.4/30.9% | 5.3% | 3 |
| baymesh-2026-08 | 0.813 | - | - | 0.934 | 0.939 | 0.409 | 1.31x | 30.6/34.0% | 5.4% | 3 |

### `MS-router-late` - router-late-fraction  `--scenario rolling`

*The share of nodes on ROUTER_LATE.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 0.05 | 0.878 | - | - | 0.985 | 0.986 | 0.654 | 1.49x | 32.6/37.6% | 5.3% | 3 |
| 0.1 | 0.896 | - | - | 0.990 | 0.991 | 0.679 | 1.60x | 34.4/40.6% | 5.3% | 3 |
| 0.2 | 0.900 | - | - | 0.987 | 0.987 | 0.700 | 1.83x | 41.6/47.5% | 5.3% | 3 |

### `SC-signing` - signature-policy  `--scenario rolling`

*The receive-side signature policy - what a node does with an unsigned packet.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| COMPATIBLE | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| BALANCED | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| STRICT | 0.757 | - | - | 0.875 | 0.884 | 0.569 | 1.47x | 29.5/32.4% | 5.6% | 3 |

> signature-policy=STRICT: decode_failures 4

### `FW-signing-cost` - profile-flag  `--scenario rolling`

*Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| signing=false | 0.917 | - | - | 0.992 | 0.994 | 0.716 | 0.73x | 15.9/17.6% | 3.1% | 3 |
| signing=true | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |

### `MS-siting` - siting-mix  `--scenario rolling`

*Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| local-typical | 0.640 | - | - | 0.801 | 0.809 | 0.000 | 1.43x | 25.0/31.3% | 5.4% | 3 |
| event | 0.317 | - | - | 0.462 | 0.463 | 0.000 | 1.31x | 15.6/21.1% | 4.8% | 3 |
| backbone | 0.978 | - | - | 0.999 | 1.000 | 0.857 | 1.11x | 34.9/38.3% | 5.6% | 3 |

> siting-mix=local-typical: decode_failures 3

### `SF-sr-retries` - sr-retries  `--scenario rolling`

*Retries per addressed reconciliation hop, to find where delivery stops improving.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 0.882 | - | - | 0.980 | 0.988 | 0.667 | 1.26x | 25.6/28.1% | 4.9% | 3 |
| 1 | 0.882 | - | - | 0.985 | 0.986 | 0.673 | 1.27x | 25.8/28.3% | 4.9% | 3 |
| 2 | 0.873 | - | - | 0.980 | 0.980 | 0.646 | 1.27x | 25.8/28.5% | 4.9% | 3 |
| 4 | 0.865 | - | - | 0.978 | 0.979 | 0.644 | 1.26x | 25.7/28.2% | 4.9% | 3 |

### `LD-traceroute` - traceroute-per-hour  `--scenario rolling`

*Route discoveries per node per hour - whether traceroute learning pays for its own airtime.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 0.25 | 0.885 | - | - | 0.985 | 0.987 | 0.676 | 1.42x | 28.9/32.1% | 5.6% | 3 |
| 1.0 | 0.867 | - | - | 0.983 | 0.987 | 0.655 | 1.60x | 32.1/35.7% | 6.1% | 3 |
| 4.0 | 0.832 | - | - | 0.964 | 0.970 | 0.606 | 2.00x | 40.8/45.8% | 7.9% | 3 |

### `LD-traceroute-small` - traceroute-per-hour  `--scenario rolling`

*The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.706 | - | - | 0.780 | 0.900 | 0.549 | 5.55x | 75.0/79.2% | 13.2% | 3 |
| 1.0 | 0.635 | - | - | 0.724 | 0.858 | 0.476 | 6.16x | 77.3/80.3% | 14.6% | 3 |

> traceroute-per-hour=0.0: queue drops 16.2% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=0.0: decode_failures 98

> traceroute-per-hour=1.0: queue drops 25.1% of transmissions - airtime here is measured through a cap

> traceroute-per-hour=1.0: decode_failures 86

### `FW-versions` - profile  `--scenario rolling`

*The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2.4 | 0.908 | - | - | 0.992 | 0.992 | 0.661 | 0.75x | 13.7/17.6% | 2.1% | 3 |
| 2.5 | 0.910 | - | - | 0.986 | 0.988 | 0.666 | 0.74x | 13.4/17.1% | 2.1% | 3 |
| 2.6 | 0.913 | - | - | 0.986 | 0.992 | 0.632 | 0.73x | 13.5/17.6% | 2.1% | 3 |
| 2.7 | 0.916 | - | - | 0.988 | 0.989 | 0.684 | 0.78x | 16.6/20.9% | 3.2% | 3 |
| 2.8 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |

> profile=2.6: decode_failures 2

### `DB-warm` - warm-num-nodes  `--scenario rolling`

*The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0 | 0.706 | - | - | 0.780 | 0.900 | 0.549 | 5.55x | 75.0/79.2% | 13.2% | 3 |
| 25 | 0.706 | - | - | 0.780 | 0.900 | 0.549 | 5.55x | 75.0/79.2% | 13.2% | 3 |
| 100 | 0.706 | - | - | 0.780 | 0.900 | 0.549 | 5.55x | 75.0/79.2% | 13.2% | 3 |
| 2000 | 0.706 | - | - | 0.780 | 0.900 | 0.549 | 5.55x | 75.0/79.2% | 13.2% | 3 |

> warm-num-nodes=0: queue drops 16.2% of transmissions - airtime here is measured through a cap

> warm-num-nodes=0: decode_failures 98

> warm-num-nodes=25: queue drops 16.2% of transmissions - airtime here is measured through a cap

> warm-num-nodes=25: decode_failures 98

> warm-num-nodes=100: queue drops 16.2% of transmissions - airtime here is measured through a cap

> warm-num-nodes=100: decode_failures 98

> warm-num-nodes=2000: queue drops 16.2% of transmissions - airtime here is measured through a cap

> warm-num-nodes=2000: decode_failures 98

### `AD-amplifiers` - amplifier-mix  `--scenario rolling`

*Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| sprinkled | 0.898 | - | - | 0.952 | 0.954 | 0.656 | 1.24x | 25.3/27.9% | 5.2% | 3 |
| arms-race | 0.950 | - | - | 0.983 | 0.984 | 0.857 | 1.02x | 26.6/28.3% | 5.3% | 3 |

### `AD-amplify-worst` - amplify-worst  `--scenario rolling`

*A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 0.1 | 0.924 | - | - | 0.987 | 0.990 | 0.674 | 1.20x | 26.0/30.4% | 5.3% | 3 |
| 0.3 | 0.967 | - | - | 0.998 | 0.998 | 0.887 | 0.99x | 25.9/30.2% | 5.0% | 3 |

### `AD-badrouters` - role-placement  `--scenario rolling`

*Where the router roles land - on the best-connected nodes, the worst, or at random.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 0.795 | - | - | 0.922 | 0.945 | 0.361 | 1.16x | 26.2/29.6% | 5.4% | 3 |
| inverse | 0.783 | - | - | 0.965 | 0.968 | 0.543 | 1.08x | 19.2/22.3% | 3.3% | 3 |
| random | 0.872 | - | - | 0.967 | 0.971 | 0.394 | 1.16x | 21.5/25.1% | 4.5% | 3 |

> role-placement=degree: decode_failures 29

### `LD-chatty` - broadcast-interval-s  `--scenario rolling`

*The device broadcast interval driven down to three times its default rate.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 0.906 | - | - | 0.995 | 0.996 | 0.677 | 0.89x | 18.3/20.0% | 3.5% | 3 |
| 900 | 0.843 | - | - | 0.977 | 0.981 | 0.608 | 2.13x | 42.5/47.0% | 8.2% | 3 |
| 300 | 0.561 | - | - | 0.709 | 0.873 | 0.343 | 4.54x | 74.3/79.5% | 15.7% | 3 |

> broadcast-interval-s=300: decode_failures 29

### `LD-chatty-hops` - broadcast-interval-s  `--scenario rolling`

*The same, with every node on a flat hop limit of 7 so nothing damps the flood.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3600 | 0.936 | - | - | 0.987 | 0.987 | 0.822 | 1.01x | 19.4/21.1% | 3.6% | 3 |
| 900 | 0.868 | - | - | 0.955 | 0.955 | 0.740 | 2.51x | 46.9/51.1% | 8.7% | 3 |
| 300 | 0.591 | - | - | 0.699 | 0.815 | 0.477 | 4.98x | 75.3/80.0% | 16.0% | 3 |

> broadcast-interval-s=300: queue drops 12.3% of transmissions - airtime here is measured through a cap

> broadcast-interval-s=300: decode_failures 38

### `RF-duct` - duct-per-hour  `--scenario rolling`

*Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 0.25 | 0.903 | - | - | 0.988 | 0.992 | 0.727 | 1.14x | 26.0/28.7% | 5.0% | 3 |
| 1.0 | 0.947 | - | - | 0.993 | 0.996 | 0.834 | 0.86x | 28.5/30.2% | 4.8% | 3 |

### `RF-noise` - noise-profile  `--scenario rolling`

*The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| none | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| temporal | 0.811 | - | - | 0.942 | 0.965 | 0.494 | 1.40x | 28.4/30.8% | 5.5% | 3 |
| transient | 0.878 | - | - | 0.985 | 0.987 | 0.674 | 1.36x | 27.5/30.4% | 5.3% | 3 |
| periodic | 0.729 | - | - | 0.843 | 0.846 | 0.523 | 1.27x | 25.3/28.4% | 4.7% | 3 |

> noise-profile=temporal: decode_failures 37

### `AD-nomute` - role-mix  `--scenario rolling`

*The role census: a real mesh's mix, the same without muted clients, and everything a router.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baymesh-2026-08 | 0.795 | - | - | 0.922 | 0.945 | 0.361 | 1.16x | 26.2/29.6% | 5.4% | 3 |
| no-mute | 0.893 | - | - | 0.982 | 0.986 | 0.704 | 1.27x | 24.9/27.6% | 5.2% | 3 |
| all-routers | 0.927 | - | - | 0.990 | 0.992 | 0.739 | 2.81x | 44.4/48.9% | 5.3% | 3 |

> role-mix=baymesh-2026-08: decode_failures 29

### `RF-pulse` - noise-pulse-interval-ms  `--scenario rolling`

*How often the periodic emitter fires.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 30000 | 0.828 | - | - | 0.932 | 0.936 | 0.621 | 1.32x | 26.9/29.8% | 5.0% | 3 |
| 10000 | 0.729 | - | - | 0.843 | 0.846 | 0.523 | 1.27x | 25.3/28.4% | 4.7% | 3 |
| 4000 | 0.486 | - | - | 0.558 | 0.621 | 0.309 | 1.09x | 21.8/24.9% | 3.6% | 3 |
| 2000 | 0.127 | - | - | 0.153 | 0.231 | 0.060 | 0.74x | 15.4/18.1% | 2.1% | 3 |

> noise-pulse-interval-ms=4000: decode_failures 5

### `AD-siting` - siting-mix  `--scenario rolling`

*Siting against a real role census, including a basement-heavy mesh.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.795 | - | - | 0.922 | 0.945 | 0.361 | 1.16x | 26.2/29.6% | 5.4% | 3 |
| local-typical | 0.666 | - | - | 0.791 | 0.836 | 0.000 | 1.26x | 24.8/30.4% | 5.3% | 3 |
| basement-heavy | 0.045 | - | - | 0.163 | 0.164 | 0.000 | 0.35x | 4.5/8.7% | 2.1% | 3 |

> siting-mix=uniform: decode_failures 29

> siting-mix=local-typical: decode_failures 22

### `MS-stretch` - stretch  `--scenario rolling`

*Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1.0 | 0.879 | - | - | 0.985 | 0.987 | 0.679 | 1.36x | 27.6/30.5% | 5.3% | 3 |
| 1.25 | 0.705 | - | - | 0.902 | 0.938 | 0.196 | 1.36x | 20.3/23.8% | 5.3% | 3 |
| 1.5 | 0.472 | - | - | 0.706 | 0.736 | 0.000 | 1.34x | 17.9/21.0% | 5.2% | 3 |
| 2.0 | 0.126 | - | - | 0.247 | 0.249 | 0.000 | 0.85x | 7.7/9.9% | 2.4% | 3 |

> stretch=1.25: decode_failures 23

> stretch=1.5: decode_failures 7

> stretch=2.0: decode_failures 2

### `RF-stretch-duct` - duct-per-hour  `--scenario rolling`

*Ducting on a stretched mesh, where the long links it creates are the ones that were missing.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.472 | - | - | 0.706 | 0.736 | 0.000 | 1.34x | 17.9/21.0% | 5.2% | 3 |
| 1.0 | 0.759 | - | - | 0.881 | 0.884 | 0.509 | 0.95x | 23.0/25.9% | 4.8% | 3 |

> duct-per-hour=0.0: decode_failures 7

### `AD-worst` - role-placement  `--scenario rolling`

*Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| degree | 0.821 | - | - | 0.948 | 0.949 | 0.000 | 2.31x | 27.2/37.0% | 5.7% | 3 |
| inverse | 0.782 | - | - | 0.940 | 0.942 | 0.000 | 2.26x | 23.6/34.4% | 3.4% | 3 |

