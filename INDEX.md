# SF++ sweep explorer

1 scheduled run(s) rolled up, 86 block(s). Open `index.html` for the filterable page; this file is the same data in a diff-readable form.

- **latest** `blocks-2026-08-22-5434544` on rolling ground, seed base `5434544`
- **transport** `0553092`
- **sim version** `1.4.0`, excluding 11 superseded run(s) from every metric below

## What moves a delivery measure

| block | arm | measure | spread | run-to-run sd | text spread | price | runs |
| --- | --- | --- | --: | --: | --: | --- | --: |
| `Q-control` | protocol | **held** | 0.988 | · | 0.010 | 1x bytes_on_air | 1 |
| `Q-protocol` | protocol | **held** | 0.985 | · | 0.013 | 1.2x bytes_on_air | 1 |
| `F-txpower` | tx-power | **held** | 0.839 | · | 0.804 | 9x sr_airtime | 1 |
| `X-pulse` | noise-pulse-interval-ms | **held** | 0.779 | · | 0.702 | 1e+02x sr_airtime | 1 |
| `X-siting` | siting-mix | **held** | 0.759 | · | 0.750 | 10x sr_bytes | 1 |
| `X-stretch` | stretch | **text** | 0.753 | · | 0.753 | 4.3x advert_bytes | 1 |
| `P-bw500` | preset | **held** | 0.734 | · | 0.659 | 5.1x sr_airtime | 1 |
| `R-siting` | siting-mix | **text** | 0.662 | · | 0.662 | 4.1x sr_airtime | 1 |
| `R-hopscale` | nodes | **held** | 0.579 | · | 0.566 | 8.2x sr_bytes | 1 |
| `P-eu-presets` | preset | **text** | 0.512 | · | 0.512 | 2x sr_airtime | 1 |
| `P-preset` | preset | **text** | 0.512 | · | 0.512 | 2.3x sr_airtime | 1 |
| `R-oversubscribed` | nodes | **held** | 0.510 | · | 0.452 | 4.8x bytes_on_air | 1 |
| `Q-topology` | topology | **text** | 0.380 | · | 0.380 | 2x sr_bytes | 1 |
| `X-chatty-hops` | broadcast-interval-s | **text** | 0.345 | · | 0.345 | 9.2x sr_airtime | 1 |
| `X-chatty` | broadcast-interval-s | **text** | 0.345 | · | 0.345 | 9.8x sr_airtime | 1 |
| `F-outage` | burst-loss | **text** | 0.328 | · | 0.328 | 1.8x sr_bytes | 1 |
| `F-burst` | burst-loss | **text** | 0.288 | · | 0.288 | 2x sr_bytes | 1 |
| `X-stretch-duct` | duct-per-hour | **text** | 0.287 | · | 0.287 | 1.7x sr_airtime | 1 |
| `R-hotstore-stress` | max-num-nodes | **held** | 0.286 | · | 0.218 | 4.6x sr_airtime | 1 |
| `P-congestion` | no-congestion-scaling | **text** | 0.247 | · | 0.247 | 5x sr_airtime | 1 |
| `F-hoplimit` | hop-limit | **text** | 0.209 | · | 0.209 | 2x sr_bytes | 1 |
| `K-hopspread` | hop-limit | **text** | 0.198 | · | 0.198 | 1.9x sr_bytes | 1 |
| `K-size` | nodes | **text** | 0.158 | · | 0.158 | 6.7x sr_bytes | 1 |
| `K-spread` | hop-spread | **text** | 0.152 | · | 0.152 | 1.8x sr_bytes | 1 |
| `X-noise` | noise-profile | **text** | 0.150 | · | 0.150 | 1.6x sr_bytes | 1 |
| `K-density` | nodes | **text** | 0.147 | · | 0.147 | 5.5x sr_airtime | 1 |
| `F-flooding` | role-mix | **text** | 0.132 | · | 0.132 | 2.6x sr_bytes | 1 |
| `X-nomute` | role-mix | **text** | 0.132 | · | 0.132 | 2.6x sr_bytes | 1 |
| `R-signing` | signature-policy | **text** | 0.122 | · | 0.122 | 1.2x sr_airtime | 1 |
| `R-hotstore` | max-num-nodes | **text** | 0.100 | · | 0.100 | 2.2x sr_airtime | 1 |
| `F-loss` | extra-loss | **text** | 0.100 | · | 0.100 | 1.4x sr_bytes | 1 |
| `R-platform` | platform-mix | **text** | 0.099 | · | 0.099 | 2.3x sr_airtime | 1 |
| `R-roles` | role-mix | **text** | 0.096 | · | 0.096 | 1.6x sr_bytes | 1 |
| `X-badrouters` | role-placement | **text** | 0.090 | · | 0.090 | 1.8x sr_bytes | 1 |
| `R-roles-fav` | role-mix | **text** | 0.088 | · | 0.088 | 1.4x sr_bytes | 1 |
| `X-amplify-worst` | amplify-worst | **text** | 0.088 | · | 0.088 | 1.6x sr_bytes | 1 |
| `D-cadence` | trigger | **held** | 0.079 | · | 0.019 | 13x advert_bytes | 1 |
| `Q-interval` | broadcast-interval-s | **text** | 0.077 | · | 0.077 | 4.8x sr_airtime | 1 |
| `R-rebroadcast` | rebroadcast-mode | **held** | 0.076 | · | 0.004 | 19x sr_airtime | 1 |
| `R-traceroute-small` | traceroute-per-hour | **text** | 0.071 | · | 0.071 | 1.3x sr_airtime | 1 |
| `X-amplifiers` | amplifier-mix | **text** | 0.071 | · | 0.071 | 2.5x sr_bytes | 1 |
| `X-duct` | duct-per-hour | **text** | 0.067 | · | 0.067 | 1.6x bytes_on_air | 1 |
| `G-place` | place | **text** | 0.054 | · | 0.054 | 3.6x sr_bytes | 1 |
| `N-place` | place | **text** | 0.054 | · | 0.054 | 3.6x sr_bytes | 1 |
| `R-traceroute` | traceroute-per-hour | **text** | 0.052 | · | 0.052 | 1.5x sr_airtime | 1 |
| `P-catchup` | catch-up-hours | **held** | 0.040 | · | 0.018 | 9.4x advert_bytes | 1 |
| `X-worst` | role-placement | **text** | 0.039 | · | 0.039 | 1.1x sr_bytes | 1 |
| `R-signing-cost` | profile-flag | **text** | 0.038 | · | 0.038 | 3.3x bytes_on_air | 1 |
| `R-mixed-26` | legacy-fraction | **text** | 0.038 | · | 0.038 | 2.2x bytes_on_air | 1 |
| `R-versions` | profile | **text** | 0.036 | · | 0.036 | 3.3x bytes_on_air | 1 |
| `L-provide` | provide-transport | **text** | 0.035 | · | 0.035 | 3.4x sr_airtime | 1 |
| `R-mixed` | legacy-fraction | **text** | 0.034 | · | 0.034 | 2.1x bytes_on_air | 1 |
| `R-congestion-input` | congestion-input | **text** | 0.034 | · | 0.034 | 1.4x sr_airtime | 1 |
| `G-hops` | hops-apart | **held** | 0.034 | · | 0.019 | 3.2x sr_bytes | 1 |
| `N-hops` | hops-apart | **held** | 0.034 | · | 0.022 | 3.2x sr_bytes | 1 |
| `J-wincap` | capacity | **held** | 0.031 | · | 0.001 | 2x advert_bytes | 1 |
| `R-firmware` | profile | **text** | 0.031 | · | 0.031 | 3.2x bytes_on_air | 1 |
| `P-diurnal` | diurnal | **text** | 0.024 | · | 0.024 | 1.3x sr_bytes | 1 |
| `R-routerlate` | router-late-fraction | **text** | 0.022 | · | 0.022 | 1.6x sr_bytes | 1 |
| `G-servers` | servers | **held** | 0.022 | · | 0.008 | 5.4x sr_bytes | 1 |
| `N-servers` | servers | **held** | 0.022 | · | 0.008 | 5.4x sr_bytes | 1 |
| `R-srretries` | sr-retries | **text** | 0.017 | · | 0.017 | 1.2x sr_bytes | 1 |
| `R-favourites` | favourite-routers | **text** | 0.014 | · | 0.014 | 1.1x sr_bytes | 1 |
| `J-timewin` | time-bucket-s | **text** | 0.014 | · | 0.014 | 5.3x advert_bytes | 1 |
| `R-dmmode` | dm-mode | **held** | 0.012 | · | 0.003 | 1.2x sr_airtime | 1 |
| `J-window` | window-size | **text** | 0.011 | · | 0.011 | 5.2x advert_bytes | 1 |
| `R-dmmode-cr` | dm-mode | **text** | 0.011 | · | 0.011 | 1.1x sr_airtime | 1 |
| `E-capacity` | capacity | **held** | 0.011 | · | 0.007 | 5.3x advert_bytes | 1 |
| `M-capacity` | capacity | **held** | 0.011 | · | 0.007 | 5.3x advert_bytes | 1 |
| `J-bucketmode` | bucket-mode | **text** | 0.010 | · | 0.010 | 2.6x advert_bytes | 1 |
| `G-allrouters` | servers | **text** | 0.010 | · | 0.010 | 2.9x sr_bytes | 1 |
| `E-width` | short-id-bits | **text** | 0.009 | · | 0.009 | 3.1x advert_bytes | 1 |
| `R-adopt` | no-adopt-hop-recommendation | **text** | 0.009 | · | 0.009 | 1.2x sr_airtime | 1 |
| `Q-hopassign` | hop-assign | **held** | 0.008 | · | 0.001 | 1.2x sr_airtime | 1 |
| `D-resolve` | resolve | **text** | 0.008 | · | 0.008 | 5.7x advert_bytes | 1 |
| `D-jitter` | advert-jitter-s | **held** | 0.007 | · | 0.007 | 1.1x sr_airtime | 1 |
| `M-jitter` | advert-jitter-s | **held** | 0.007 | · | 0.007 | 1.1x sr_airtime | 1 |
| `R-crladder` | coding-rate-ladder | **text** | 0.004 | · | 0.004 | 1.1x sr_airtime | 1 |
| `M-replayorder` | replay-ordering | **text** | 0.003 | · | 0.003 | 1x sr_bytes | 1 |
| `R-repeats` | extra-repeats | **held** | 0.003 | · | 0.000 | 1x bytes_on_air | 1 |
| `L-advert` | advert-transport | **text** | 0.002 | · | 0.002 | 2.5x sr_airtime | 1 |
| `M-combined` | replay-ordering | **held** | 0.002 | · | 0.001 | 1.1x sr_airtime | 1 |
| `R-congestion-mode` | congestion-mode | **text** | 0.002 | · | 0.002 | 1.1x sr_bytes | 1 |
| `R-repeats-busy` | extra-repeats | **text** | 0.001 | · | 0.001 | 1x sr_airtime | 1 |
| `E-signed` | signed | **held** | 0.000 | · | 0.000 | 1.4x advert_bytes | 1 |
| `R-warm` | warm-num-nodes | **held** | 0.000 | · | 0.000 | · | 1 |

## Runs

| run | ground | seed base | blocks | missing | warnings |
| --- | --- | --- | --: | --: | --: |
| [`blocks-2026-08-22-5434544`](runs/blocks-2026-08-22-5434544/trend.md) | rolling | `5434544` | 86 | 1 | 105 |
