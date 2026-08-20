# SF++ sweep explorer

5 scheduled run(s) rolled up, 89 block(s). Open `index.html` for the filterable page; this file is the same data in a diff-readable form.

- **latest** `matrix-2026-08-19` on batumi ground, seed base `None`
- **transport** `7b53cc8`

## What moves a delivery measure

| block | arm | measure | spread | run-to-run sd | text spread | price | runs |
| --- | --- | --- | --: | --: | --: | --- | --: |
| `F-preset-turbo` | preset | **held** | 0.880 | · | 0.678 | 4.7x bytes_on_air | 1 |
| `Q-protocol` | protocol | **held** | 0.880 | · | 0.026 | 1.1x bytes_on_air | 1 |
| `batumi-none` | archive | **held** | 0.853 | · | 0.188 | 1.2x bytes_on_air | 1 |
| `R-siting` | siting-mix | **held** | 0.846 | · | 0.822 | 30x sr_bytes | 1 |
| `F-txpower` | tx-power | **held** | 0.840 | · | 0.669 | 90x sr_bytes | 1 |
| `Q-control` | protocol | **held** | 0.791 | · | 0.012 | 1.1x bytes_on_air | 1 |
| `X-pulse` | noise-pulse-interval-ms | **held** | 0.778 | · | 0.610 | 5.3x bytes_on_air | 1 |
| `X-stretch` | stretch | **held** | 0.762 | · | 0.626 | 8x advert_bytes | 1 |
| `X-siting` | siting-mix | **held** | 0.639 | · | 0.614 | 4.1x sr_bytes | 1 |
| `R-hopscale` | nodes | **held** | 0.590 | · | 0.521 | 8.5x sr_bytes | 1 |
| `P-bw500` | preset | **held** | 0.586 | · | 0.477 | 10x sr_bytes | 1 |
| `X-chatty` | broadcast-interval-s | **held** | 0.510 | · | 0.450 | 25x sr_airtime | 1 |
| `X-chatty-hops` | broadcast-interval-s | **text** | 0.500 | · | 0.500 | 18x sr_airtime | 1 |
| `P-eu-presets` | preset | **text** | 0.486 | · | 0.486 | 2.5x sr_bytes | 1 |
| `Q-topology` | topology | **text** | 0.468 | 0.052 | 0.468 | 2.2x sr_bytes | 2 |
| `P-preset` | preset | **text** | 0.458 | · | 0.458 | 2.4x sr_airtime | 1 |
| `X-stretch-duct` | duct-per-hour | **text** | 0.406 | · | 0.406 | 2.5x sr_airtime | 1 |
| `P-congestion` | no-congestion-scaling | **held** | 0.391 | · | 0.385 | 6.6x sr_airtime | 1 |
| `R-oversubscribed` | nodes | **held** | 0.367 | · | 0.292 | 4x bytes_on_air | 1 |
| `F-hoplimit` | hop-limit | **text** | 0.353 | · | 0.353 | 2.9x sr_bytes | 1 |
| `K-density` | nodes | **held** | 0.331 | · | 0.299 | 6x advert_bytes | 1 |
| `F-outage` | burst-loss | **text** | 0.329 | · | 0.329 | 1.9x sr_bytes | 1 |
| `F-burst` | burst-loss | **text** | 0.279 | · | 0.279 | 1.8x sr_bytes | 1 |
| `K-size` | nodes | **text** | 0.276 | · | 0.276 | 4.3x sr_bytes | 1 |
| `K-hopspread` | hop-limit | **text** | 0.273 | 0.029 | 0.273 | 2.2x sr_bytes | 2 |
| `R-hotstore-stress` | max-num-nodes | **held** | 0.260 | · | 0.114 | 5.5x sr_airtime | 1 |
| `X-noise` | noise-profile | **held** | 0.256 | · | 0.230 | 1.6x sr_airtime | 1 |
| `N-hops` | hops-apart | **held** | 0.243 | 0.070 | 0.024 | 2.6x sr_bytes | 2 |
| `K-spread` | hop-spread | **text** | 0.205 | · | 0.205 | 1.7x sr_bytes | 1 |
| `X-amplify-worst` | amplify-worst | **text** | 0.192 | · | 0.192 | 1.4x sr_airtime | 1 |
| `X-amplifiers` | amplifier-mix | **text** | 0.189 | · | 0.189 | 1.5x sr_bytes | 1 |
| `batumi-x1-SHORT_FAST` | placement | **held** | 0.186 | · | 0.104 | 1.1x bytes_on_air | 1 |
| `G-place` | place | **held** | 0.180 | · | 0.011 | 2.1x sr_bytes | 1 |
| `N-place` | place | **held** | 0.180 | · | 0.011 | 2.1x sr_bytes | 1 |
| `G-allrouters` | servers | **held** | 0.177 | · | 0.055 | 4.9x sr_bytes | 1 |
| `G-hops` | hops-apart | **held** | 0.177 | · | 0.025 | 2.6x sr_bytes | 1 |
| `X-duct` | duct-per-hour | **text** | 0.166 | · | 0.166 | 1.5x bytes_on_air | 1 |
| `Q-interval` | broadcast-interval-s | **text** | 0.163 | · | 0.163 | 6x sr_airtime | 1 |
| `F-loss` | extra-loss | **text** | 0.149 | 0.013 | 0.149 | 1.3x sr_bytes | 2 |
| `R-hotstore` | max-num-nodes | **text** | 0.130 | · | 0.130 | 2.1x sr_airtime | 1 |
| `R-platform` | platform-mix | **text** | 0.130 | · | 0.130 | 2.1x sr_airtime | 1 |
| `G-servers` | servers | **held** | 0.105 | 0.070 | 0.019 | 9.8x sr_bytes | 2 |
| `R-mixed` | legacy-fraction | **text** | 0.093 | · | 0.093 | 1.9x bytes_on_air | 1 |
| `R-signing` | signature-policy | **text** | 0.091 | · | 0.091 | 1.2x sr_airtime | 1 |
| `F-flooding` | role-mix | **text** | 0.089 | · | 0.089 | 2.4x bytes_on_air | 1 |
| `X-nomute` | role-mix | **text** | 0.089 | · | 0.089 | 2.4x bytes_on_air | 1 |
| `R-mixed-26` | legacy-fraction | **text** | 0.086 | · | 0.086 | 1.9x bytes_on_air | 1 |
| `R-firmware` | profile | **text** | 0.082 | · | 0.082 | 3.2x bytes_on_air | 1 |
| `R-versions` | profile | **text** | 0.081 | · | 0.081 | 3.3x bytes_on_air | 1 |
| `R-rebroadcast` | rebroadcast-mode | **held** | 0.069 | · | 0.001 | 13x sr_airtime | 1 |
| `R-signing-cost` | profile-flag | **text** | 0.068 | · | 0.068 | 3.3x bytes_on_air | 1 |
| `R-congestion-input` | congestion-input | **held** | 0.065 | · | 0.037 | 2.2x sr_airtime | 1 |
| `D-cadence` | trigger | **held** | 0.061 | · | 0.045 | 14x advert_bytes | 1 |
| `R-traceroute` | traceroute-per-hour | **text** | 0.056 | · | 0.056 | 1.4x sr_airtime | 1 |
| `R-favourites` | favourite-routers | **text** | 0.056 | · | 0.056 | 1.1x sr_bytes | 1 |
| `R-roles-fav` | role-mix | **held** | 0.055 | · | 0.015 | 1.3x sr_bytes | 1 |
| `N-servers` | servers | **held** | 0.055 | · | 0.021 | 9.8x sr_bytes | 1 |
| `Q-hopassign` | hop-assign | **text** | 0.044 | · | 0.044 | 1.6x sr_airtime | 1 |
| `R-traceroute-small` | traceroute-per-hour | **held** | 0.042 | · | 0.035 | 1.1x sr_bytes | 1 |
| `R-roles` | role-mix | **held** | 0.035 | · | 0.033 | 1.1x sr_bytes | 1 |
| `P-catchup` | catch-up-hours | **text** | 0.034 | · | 0.034 | 9.2x advert_bytes | 1 |
| `R-congestion-mode` | congestion-mode | **held** | 0.033 | · | 0.013 | 1.2x sr_airtime | 1 |
| `E-capacity` | capacity | **held** | 0.032 | · | 0.021 | 5.4x advert_bytes | 1 |
| `M-capacity` | capacity | **held** | 0.032 | · | 0.021 | 5.4x advert_bytes | 1 |
| `L-provide` | provide-transport | **text** | 0.030 | · | 0.030 | 3.1x sr_airtime | 1 |
| `P-diurnal` | diurnal | **text** | 0.030 | · | 0.030 | 1.2x advert_bytes | 1 |
| `J-timewin` | time-bucket-s | **held** | 0.029 | · | 0.021 | 5.1x advert_bytes | 1 |
| `R-srretries` | sr-retries | **held** | 0.028 | · | 0.013 | 1.2x sr_bytes | 1 |
| `R-dmmode-cr` | dm-mode | **held** | 0.023 | · | 0.002 | 1.2x sr_airtime | 1 |
| `X-badrouters` | role-placement | **held** | 0.022 | · | 0.020 | 1.3x sr_bytes | 1 |
| `D-jitter` | advert-jitter-s | **held** | 0.020 | · | 0.012 | 1.1x sr_bytes | 1 |
| `M-jitter` | advert-jitter-s | **held** | 0.020 | · | 0.012 | 1.1x sr_bytes | 1 |
| `R-routerlate` | router-late-fraction | **held** | 0.019 | · | 0.011 | 1.3x bytes_on_air | 1 |
| `R-dmmode` | dm-mode | **held** | 0.018 | · | 0.015 | 1.2x sr_airtime | 1 |
| `X-worst` | role-placement | **held** | 0.014 | · | 0.014 | 1.1x sr_airtime | 1 |
| `R-adopt` | no-adopt-hop-recommendation | **held** | 0.014 | · | 0.013 | 1.1x sr_airtime | 1 |
| `J-wincap` | capacity | **held** | 0.011 | · | 0.007 | 1.8x advert_bytes | 1 |
| `R-crladder` | coding-rate-ladder | **text** | 0.008 | · | 0.008 | 1.1x sr_bytes | 1 |
| `E-width` | short-id-bits | **held** | 0.007 | · | 0.006 | 3.1x advert_bytes | 1 |
| `J-bucketmode` | bucket-mode | **held** | 0.007 | · | 0.007 | 3.9x advert_bytes | 1 |
| `R-repeats` | extra-repeats | **held** | 0.007 | · | 0.003 | 1x sr_airtime | 1 |
| `R-repeats-busy` | extra-repeats | **text** | 0.006 | · | 0.006 | 1.1x sr_bytes | 1 |
| `J-window` | window-size | **text** | 0.006 | · | 0.006 | 6.6x advert_bytes | 1 |
| `D-resolve` | resolve | **held** | 0.006 | 0.003 | 0.005 | 5.7x advert_bytes | 2 |
| `L-advert` | advert-transport | **text** | 0.004 | · | 0.004 | 2x advert_bytes | 1 |
| `M-replayorder` | replay-ordering | **held** | 0.003 | · | 0.003 | 1.1x sr_bytes | 1 |
| `M-combined` | replay-ordering | **held** | 0.003 | · | 0.002 | 1x sr_airtime | 1 |
| `E-signed` | signed | **text** | 0.000 | 0.000 | 0.000 | 1.4x advert_bytes | 2 |
| `R-warm` | warm-num-nodes | **held** | 0.000 | · | 0.000 | · | 1 |

## Runs

| run | ground | seed base | blocks | missing | warnings |
| --- | --- | --- | --: | --: | --: |
| [`matrix-2026-08-19`](runs/matrix-2026-08-19/trend.md) | batumi | `None` | 1 | 0 | 15 |
| [`design-2026-08-19-1524961`](runs/design-2026-08-19-1524961/trend.md) | batumi | `1524961` | 1 | 0 | 21 |
| [`blocks-2026-08-20-3724240`](runs/blocks-2026-08-20-3724240/trend.md) | ridge | `3724240` | 87 | 0 | 110 |
| [`blocks-2026-08-19-9293155`](runs/blocks-2026-08-19-9293155/trend.md) | rolling | `9293155` | 5 | 0 | 7 |
| [`blocks-2026-08-19-2455835`](runs/blocks-2026-08-19-2455835/trend.md) | ridge | `2455835` | 2 | 0 | 0 |
