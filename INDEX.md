# SF++ sweep explorer

1 scheduled run(s) rolled up, 87 block(s). Open `index.html` for the filterable page; this file is the same data in a diff-readable form.

- **latest** `blocks-2026-08-21-1395205` on rolling ground, seed base `1395205`
- **transport** `17a0d62`
- **sim version** `1.2.0`, excluding 7 superseded run(s) from every metric below

## What moves a delivery measure

| block | arm | measure | spread | run-to-run sd | text spread | price | runs |
| --- | --- | --- | --: | --: | --: | --- | --: |
| `Q-control` | protocol | **held** | 0.949 | · | 0.047 | 1x bytes_on_air | 1 |
| `R-siting` | siting-mix | **text** | 0.900 | · | 0.900 | 14x sr_airtime | 1 |
| `Q-protocol` | protocol | **held** | 0.832 | · | 0.023 | 1.1x bytes_on_air | 1 |
| `X-siting` | siting-mix | **held** | 0.748 | · | 0.540 | 20x sr_bytes | 1 |
| `F-preset-turbo` | preset | **held** | 0.697 | · | 0.634 | 25x sr_bytes | 1 |
| `P-preset` | preset | **held** | 0.669 | · | 0.542 | 6.8x sr_airtime | 1 |
| `X-pulse` | noise-pulse-interval-ms | **held** | 0.663 | · | 0.566 | 92x sr_airtime | 1 |
| `R-hopscale` | nodes | **held** | 0.644 | · | 0.528 | 7.4x bytes_on_air | 1 |
| `F-txpower` | tx-power | **text** | 0.629 | · | 0.629 | 3.8x advert_bytes | 1 |
| `Q-topology` | topology | **held** | 0.626 | · | 0.504 | 5.3x sr_airtime | 1 |
| `X-stretch` | stretch | **text** | 0.589 | · | 0.589 | 3x advert_bytes | 1 |
| `P-eu-presets` | preset | **held** | 0.579 | · | 0.491 | 3.4x sr_airtime | 1 |
| `K-size` | nodes | **held** | 0.507 | · | 0.392 | 2.9x sr_bytes | 1 |
| `X-chatty-hops` | broadcast-interval-s | **held** | 0.399 | · | 0.322 | 14x sr_airtime | 1 |
| `P-bw500` | preset | **text** | 0.396 | · | 0.396 | 4.9x sr_bytes | 1 |
| `X-stretch-duct` | duct-per-hour | **text** | 0.390 | · | 0.390 | 2.5x sr_airtime | 1 |
| `F-hoplimit` | hop-limit | **text** | 0.374 | · | 0.374 | 2.5x sr_airtime | 1 |
| `R-oversubscribed` | nodes | **held** | 0.359 | · | 0.250 | 3.6x bytes_on_air | 1 |
| `K-density` | nodes | **text** | 0.345 | · | 0.345 | 6.5x sr_airtime | 1 |
| `F-flooding` | role-mix | **text** | 0.323 | · | 0.323 | 2.3x bytes_on_air | 1 |
| `X-nomute` | role-mix | **text** | 0.323 | · | 0.323 | 2.3x bytes_on_air | 1 |
| `F-outage` | burst-loss | **text** | 0.307 | · | 0.307 | 2.2x sr_bytes | 1 |
| `K-hopspread` | hop-limit | **text** | 0.301 | · | 0.301 | 2x sr_airtime | 1 |
| `N-hops` | hops-apart | **held** | 0.301 | · | 0.053 | 3.2x sr_bytes | 1 |
| `F-burst` | burst-loss | **text** | 0.299 | · | 0.299 | 1.9x sr_bytes | 1 |
| `G-place` | place | **held** | 0.298 | · | 0.046 | 3.1x sr_bytes | 1 |
| `N-place` | place | **held** | 0.298 | · | 0.046 | 3.1x sr_bytes | 1 |
| `X-badrouters` | role-placement | **held** | 0.298 | · | 0.229 | 2.6x sr_bytes | 1 |
| `X-chatty` | broadcast-interval-s | **held** | 0.292 | · | 0.285 | 10x sr_airtime | 1 |
| `K-spread` | hop-spread | **held** | 0.288 | · | 0.201 | 1.5x sr_airtime | 1 |
| `X-amplifiers` | amplifier-mix | **text** | 0.237 | · | 0.237 | 2.6x sr_bytes | 1 |
| `R-roles` | role-mix | **text** | 0.227 | · | 0.227 | 1.5x sr_airtime | 1 |
| `X-amplify-worst` | amplify-worst | **text** | 0.226 | · | 0.226 | 1.9x sr_bytes | 1 |
| `R-roles-fav` | role-mix | **text** | 0.219 | · | 0.219 | 1.4x sr_airtime | 1 |
| `P-congestion` | no-congestion-scaling | **text** | 0.201 | · | 0.201 | 4.2x sr_airtime | 1 |
| `X-noise` | noise-profile | **held** | 0.201 | · | 0.163 | 1.4x sr_airtime | 1 |
| `X-duct` | duct-per-hour | **text** | 0.162 | · | 0.162 | 1.3x sr_airtime | 1 |
| `R-mixed` | legacy-fraction | **held** | 0.140 | · | 0.068 | 2.1x bytes_on_air | 1 |
| `F-loss` | extra-loss | **text** | 0.137 | · | 0.137 | 1.2x sr_bytes | 1 |
| `G-hops` | hops-apart | **held** | 0.135 | · | 0.053 | 3.2x sr_bytes | 1 |
| `R-hotstore-stress` | max-num-nodes | **held** | 0.129 | · | 0.079 | 4x sr_airtime | 1 |
| `R-mixed-26` | legacy-fraction | **held** | 0.120 | · | 0.069 | 2.1x bytes_on_air | 1 |
| `Q-interval` | broadcast-interval-s | **text** | 0.113 | · | 0.113 | 7x sr_airtime | 1 |
| `R-hotstore` | max-num-nodes | **held** | 0.096 | · | 0.084 | 2.2x sr_airtime | 1 |
| `R-platform` | platform-mix | **held** | 0.096 | · | 0.084 | 2.2x sr_airtime | 1 |
| `R-versions` | profile | **text** | 0.089 | · | 0.089 | 3.1x bytes_on_air | 1 |
| `R-signing` | signature-policy | **text** | 0.087 | · | 0.087 | 1.3x sr_airtime | 1 |
| `R-firmware` | profile | **text** | 0.084 | · | 0.084 | 3.1x bytes_on_air | 1 |
| `G-allrouters` | servers | **held** | 0.076 | · | 0.041 | 2.2x advert_bytes | 1 |
| `R-signing-cost` | profile-flag | **held** | 0.070 | · | 0.050 | 3.4x bytes_on_air | 1 |
| `R-traceroute-small` | traceroute-per-hour | **held** | 0.066 | · | 0.046 | 1.5x sr_airtime | 1 |
| `R-traceroute` | traceroute-per-hour | **held** | 0.040 | · | 0.039 | 1.5x sr_airtime | 1 |
| `R-congestion-input` | congestion-input | **held** | 0.038 | · | 0.024 | 2.1x sr_airtime | 1 |
| `D-cadence` | trigger | **held** | 0.037 | · | 0.014 | 15x advert_bytes | 1 |
| `J-timewin` | time-bucket-s | **held** | 0.033 | · | 0.008 | 5.3x advert_bytes | 1 |
| `R-routerlate` | router-late-fraction | **held** | 0.033 | · | 0.024 | 1.3x bytes_on_air | 1 |
| `R-rebroadcast` | rebroadcast-mode | **held** | 0.030 | · | 0.003 | 6.8x sr_airtime | 1 |
| `G-servers` | servers | **held** | 0.030 | · | 0.005 | 6.4x sr_bytes | 1 |
| `N-servers` | servers | **held** | 0.030 | · | 0.005 | 6.4x sr_bytes | 1 |
| `D-jitter` | advert-jitter-s | **held** | 0.030 | · | 0.013 | 1.1x sr_airtime | 1 |
| `M-jitter` | advert-jitter-s | **held** | 0.030 | · | 0.013 | 1.1x sr_airtime | 1 |
| `Q-hopassign` | hop-assign | **held** | 0.029 | · | 0.016 | 1.2x sr_airtime | 1 |
| `P-diurnal` | diurnal | **text** | 0.026 | · | 0.026 | 1.2x advert_bytes | 1 |
| `R-favourites` | favourite-routers | **text** | 0.026 | · | 0.026 | 1.2x sr_airtime | 1 |
| `R-dmmode` | dm-mode | **held** | 0.025 | · | 0.019 | 1.4x sr_airtime | 1 |
| `R-crladder` | coding-rate-ladder | **held** | 0.021 | · | 0.005 | 1.3x sr_airtime | 1 |
| `J-bucketmode` | bucket-mode | **held** | 0.019 | · | 0.008 | 5x advert_bytes | 1 |
| `L-provide` | provide-transport | **text** | 0.018 | · | 0.018 | 2.9x sr_airtime | 1 |
| `J-window` | window-size | **held** | 0.018 | · | 0.003 | 6.3x advert_bytes | 1 |
| `E-capacity` | capacity | **held** | 0.018 | · | 0.012 | 5.1x advert_bytes | 1 |
| `M-capacity` | capacity | **held** | 0.018 | · | 0.012 | 5.1x advert_bytes | 1 |
| `R-repeats` | extra-repeats | **held** | 0.018 | · | 0.012 | 1x sr_bytes | 1 |
| `R-srretries` | sr-retries | **text** | 0.015 | · | 0.015 | 1.1x sr_airtime | 1 |
| `R-dmmode-cr` | dm-mode | **held** | 0.015 | · | 0.008 | 1.2x sr_bytes | 1 |
| `J-wincap` | capacity | **held** | 0.014 | · | 0.007 | 2.1x advert_bytes | 1 |
| `X-worst` | role-placement | **text** | 0.014 | · | 0.014 | 1.1x sr_bytes | 1 |
| `E-width` | short-id-bits | **text** | 0.012 | · | 0.012 | 3.1x advert_bytes | 1 |
| `P-catchup` | catch-up-hours | **text** | 0.011 | · | 0.011 | 9.2x advert_bytes | 1 |
| `R-congestion-mode` | congestion-mode | **text** | 0.009 | · | 0.009 | 1.1x sr_airtime | 1 |
| `R-repeats-busy` | extra-repeats | **text** | 0.008 | · | 0.008 | 1x sr_airtime | 1 |
| `M-replayorder` | replay-ordering | **held** | 0.007 | · | 0.003 | 1.1x sr_bytes | 1 |
| `D-resolve` | resolve | **text** | 0.006 | · | 0.006 | 5.7x advert_bytes | 1 |
| `L-advert` | advert-transport | **held** | 0.006 | · | 0.003 | 2.3x sr_airtime | 1 |
| `M-combined` | replay-ordering | **held** | 0.005 | · | 0.002 | 1x sr_airtime | 1 |
| `R-adopt` | no-adopt-hop-recommendation | **text** | 0.003 | · | 0.003 | 1.2x sr_airtime | 1 |
| `E-signed` | signed | **held** | 0.000 | · | 0.000 | 1.4x advert_bytes | 1 |
| `R-warm` | warm-num-nodes | **held** | 0.000 | · | 0.000 | · | 1 |

## Runs

| run | ground | seed base | blocks | missing | warnings |
| --- | --- | --- | --: | --: | --: |
| [`blocks-2026-08-21-1395205`](runs/blocks-2026-08-21-1395205/trend.md) | rolling | `1395205` | 87 | 0 | 85 |
