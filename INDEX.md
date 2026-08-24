# SF++ sweep explorer

5 scheduled run(s) rolled up, 101 block(s). Open `index.html` for the filterable page; this file is the same data in a diff-readable form.

- **latest** `matrix-2026-08-22` on batumi ground, seed base `None`
- **transport** `0553092`
- **sim version** `1.4.0`, excluding 11 superseded run(s) from every metric below

## What moves a delivery measure

| block | arm | measure | spread | run-to-run sd | text spread | price | runs |
| --- | --- | --- | --: | --: | --: | --- | --: |
| `batumi-short-fast-coding-rate-ladder` | archive | **held** | 0.985 | · | 0.008 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-m4-early-flood` | archive | **held** | 0.985 | · | 0.008 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-extra-repeats` | archive | **held** | 0.984 | · | 0.007 | 1.1x bytes_on_air | 1 |
| `batumi-short-fast-congestion-40` | archive | **held** | 0.984 | · | 0.011 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-hop-scaling-40` | archive | **held** | 0.984 | · | 0.011 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-none` | archive | **held** | 0.984 | · | 0.011 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-favourite-routers` | archive | **held** | 0.984 | · | 0.009 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-congestion-60` | archive | **held** | 0.984 | · | 0.010 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-hop-limit-15` | archive | **held** | 0.984 | · | 0.007 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-hop-limit-7` | archive | **held** | 0.984 | · | 0.007 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-congestion-80` | archive | **held** | 0.983 | · | 0.007 | 1.1x bytes_on_air | 1 |
| `batumi-short-fast-hop-scaling-80` | archive | **held** | 0.980 | · | 0.010 | 1.1x bytes_on_air | 1 |
| `batumi-short-fast-hop-scaling-60` | archive | **held** | 0.979 | · | 0.010 | 1.1x bytes_on_air | 1 |
| `Q-control` | protocol | **held** | 0.972 | 0.023 | 0.017 | 1x bytes_on_air | 3 |
| `Q-protocol` | protocol | **held** | 0.963 | 0.021 | 0.017 | 1.2x bytes_on_air | 3 |
| `X-pulse` | noise-pulse-interval-ms | **held** | 0.775 | 0.004 | 0.678 | 1e+02x sr_airtime | 3 |
| `F-txpower` | tx-power | **text** | 0.753 | 0.053 | 0.753 | 7.2x sr_airtime | 3 |
| `X-stretch` | stretch | **text** | 0.720 | 0.041 | 0.720 | 7.3x sr_airtime | 3 |
| `X-siting` | siting-mix | **text** | 0.688 | 0.071 | 0.688 | 2.9x advert_bytes | 3 |
| `R-siting` | siting-mix | **text** | 0.653 | 0.076 | 0.653 | 4.5x sr_airtime | 3 |
| `P-bw500` | preset | **held** | 0.644 | 0.095 | 0.601 | 7.5x sr_bytes | 3 |
| `R-hopscale` | nodes | **text** | 0.531 | 0.047 | 0.531 | 10x sr_bytes | 3 |
| `P-preset` | preset | **held** | 0.513 | 0.134 | 0.534 | 7.5x sr_airtime | 3 |
| `P-eu-presets` | preset | **held** | 0.506 | 0.123 | 0.534 | 4.9x sr_airtime | 3 |
| `R-oversubscribed` | nodes | **held** | 0.457 | 0.047 | 0.419 | 4.5x bytes_on_air | 3 |
| `Q-topology` | topology | **text** | 0.353 | 0.027 | 0.353 | 1.7x sr_bytes | 3 |
| `X-chatty` | broadcast-interval-s | **text** | 0.346 | 0.013 | 0.346 | 11x sr_airtime | 3 |
| `X-chatty-hops` | broadcast-interval-s | **text** | 0.345 | 0.019 | 0.345 | 11x sr_airtime | 3 |
| `F-outage` | burst-loss | **text** | 0.334 | 0.008 | 0.334 | 2.1x sr_bytes | 3 |
| `F-burst` | burst-loss | **text** | 0.301 | 0.012 | 0.301 | 2.5x sr_bytes | 3 |
| `X-stretch-duct` | duct-per-hour | **held** | 0.286 | 0.182 | 0.346 | 14x sr_airtime | 3 |
| `R-hotstore-stress` | max-num-nodes | **held** | 0.284 | 0.005 | 0.212 | 7x sr_airtime | 3 |
| `P-congestion` | no-congestion-scaling | **text** | 0.245 | 0.023 | 0.245 | 3.3x sr_airtime | 3 |
| `K-density` | nodes | **text** | 0.234 | 0.107 | 0.234 | 5.2x sr_airtime | 3 |
| `F-hoplimit` | hop-limit | **text** | 0.225 | 0.019 | 0.225 | 1.6x sr_bytes | 3 |
| `K-hopspread` | hop-limit | **text** | 0.208 | 0.014 | 0.208 | 1.5x bytes_on_air | 3 |
| `batumi-x4-LITE_FAST` | placement | **held** | 0.178 | · | 0.079 | 1.1x bytes_on_air | 1 |
| `X-noise` | noise-profile | **text** | 0.164 | 0.016 | 0.164 | 1.3x sr_airtime | 3 |
| `K-size` | nodes | **text** | 0.155 | 0.010 | 0.155 | 4.9x sr_bytes | 3 |
| `K-spread` | hop-spread | **text** | 0.155 | 0.007 | 0.155 | 1.3x bytes_on_air | 3 |
| `batumi-x1-SHORT_FAST` | placement | **held** | 0.141 | · | 0.087 | 1.1x bytes_on_air | 1 |
| `F-flooding` | role-mix | **text** | 0.129 | 0.029 | 0.129 | 2.4x bytes_on_air | 3 |
| `X-nomute` | role-mix | **text** | 0.129 | 0.029 | 0.129 | 2.4x bytes_on_air | 3 |
| `F-loss` | extra-loss | **text** | 0.128 | 0.025 | 0.128 | 1.5x sr_bytes | 3 |
| `R-signing` | signature-policy | **text** | 0.119 | 0.014 | 0.119 | 1.3x sr_airtime | 3 |
| `G-hops` | hops-apart | **held** | 0.119 | 0.119 | 0.022 | 2.8x sr_bytes | 3 |
| `N-hops` | hops-apart | **held** | 0.119 | 0.119 | 0.023 | 2.8x sr_bytes | 3 |
| `R-hotstore` | max-num-nodes | **text** | 0.118 | 0.016 | 0.118 | 2.2x sr_airtime | 3 |
| `R-platform` | platform-mix | **text** | 0.109 | 0.009 | 0.109 | 2.2x sr_airtime | 3 |
| `X-amplify-worst` | amplify-worst | **text** | 0.106 | 0.022 | 0.106 | 1.7x sr_bytes | 3 |
| `G-place` | place | **held** | 0.103 | 0.083 | 0.033 | 2.3x sr_bytes | 3 |
| `N-place` | place | **held** | 0.103 | 0.083 | 0.033 | 2.3x sr_bytes | 3 |
| `Q-interval` | broadcast-interval-s | **text** | 0.101 | 0.021 | 0.101 | 6.1x sr_airtime | 3 |
| `R-roles` | role-mix | **text** | 0.090 | 0.028 | 0.090 | 1.2x bytes_on_air | 3 |
| `X-amplifiers` | amplifier-mix | **text** | 0.087 | 0.014 | 0.087 | 1.5x sr_bytes | 3 |
| `X-duct` | duct-per-hour | **text** | 0.073 | 0.009 | 0.073 | 1.5x bytes_on_air | 3 |
| `R-roles-fav` | role-mix | **text** | 0.072 | 0.029 | 0.072 | 1.1x bytes_on_air | 3 |
| `R-traceroute-small` | traceroute-per-hour | **held** | 0.065 | 0.007 | 0.065 | 1.2x sr_airtime | 3 |
| `D-cadence` | trigger | **held** | 0.064 | 0.020 | 0.030 | 14x advert_bytes | 3 |
| `X-badrouters` | role-placement | **text** | 0.062 | 0.044 | 0.062 | 1.6x sr_bytes | 3 |
| `R-mixed` | legacy-fraction | **text** | 0.058 | 0.032 | 0.058 | 2.1x bytes_on_air | 3 |
| `R-traceroute` | traceroute-per-hour | **text** | 0.054 | 0.013 | 0.054 | 1.6x sr_airtime | 3 |
| `R-rebroadcast` | rebroadcast-mode | **held** | 0.047 | 0.025 | 0.002 | 10x sr_airtime | 3 |
| `R-signing-cost` | profile-flag | **text** | 0.040 | 0.010 | 0.040 | 3.3x bytes_on_air | 3 |
| `R-mixed-26` | legacy-fraction | **held** | 0.034 | 0.020 | 0.060 | 2.2x bytes_on_air | 3 |
| `R-congestion-input` | congestion-input | **held** | 0.032 | 0.011 | 0.033 | 1.5x sr_airtime | 3 |
| `L-provide` | provide-transport | **text** | 0.028 | 0.010 | 0.028 | 3.1x sr_airtime | 3 |
| `P-catchup` | catch-up-hours | **text** | 0.028 | 0.008 | 0.028 | 9.2x advert_bytes | 3 |
| `X-worst` | role-placement | **text** | 0.025 | 0.014 | 0.025 | 1.1x sr_bytes | 3 |
| `R-favourites` | favourite-routers | **text** | 0.023 | 0.014 | 0.023 | 1.1x sr_bytes | 3 |
| `G-servers` | servers | **held** | 0.023 | 0.014 | 0.011 | 8.3x sr_bytes | 3 |
| `N-servers` | servers | **held** | 0.023 | 0.014 | 0.011 | 8.3x sr_bytes | 3 |
| `J-wincap` | capacity | **held** | 0.018 | 0.014 | 0.004 | 2.2x advert_bytes | 3 |
| `P-diurnal` | diurnal | **text** | 0.017 | 0.009 | 0.017 | 1.2x advert_bytes | 3 |
| `R-versions` | profile | **held** | 0.017 | 0.019 | 0.021 | 3.1x bytes_on_air | 3 |
| `R-dmmode` | dm-mode | **text** | 0.016 | 0.012 | 0.016 | 1.1x sr_airtime | 3 |
| `R-routerlate` | router-late-fraction | **held** | 0.014 | 0.008 | 0.015 | 1.3x bytes_on_air | 3 |
| `E-capacity` | capacity | **held** | 0.013 | 0.007 | 0.009 | 5.3x advert_bytes | 3 |
| `M-capacity` | capacity | **held** | 0.013 | 0.007 | 0.009 | 5.3x advert_bytes | 3 |
| `J-timewin` | time-bucket-s | **held** | 0.013 | 0.006 | 0.014 | 5.3x advert_bytes | 3 |
| `R-srretries` | sr-retries | **held** | 0.013 | 0.005 | 0.013 | 1.1x sr_bytes | 3 |
| `J-bucketmode` | bucket-mode | **text** | 0.011 | 0.002 | 0.011 | 3x advert_bytes | 3 |
| `R-firmware` | profile | **held** | 0.011 | 0.013 | 0.018 | 3.1x bytes_on_air | 3 |
| `J-window` | window-size | **held** | 0.011 | 0.005 | 0.011 | 4.8x advert_bytes | 3 |
| `Q-hopassign` | hop-assign | **held** | 0.011 | 0.002 | 0.006 | 1.1x advert_bytes | 3 |
| `E-width` | short-id-bits | **held** | 0.010 | 0.003 | 0.011 | 3.1x advert_bytes | 3 |
| `R-dmmode-cr` | dm-mode | **text** | 0.009 | 0.005 | 0.009 | 1.1x sr_bytes | 3 |
| `D-resolve` | resolve | **held** | 0.008 | 0.010 | 0.009 | 5.9x advert_bytes | 3 |
| `G-allrouters` | servers | **text** | 0.008 | 0.003 | 0.008 | 2.6x sr_bytes | 3 |
| `R-adopt` | no-adopt-hop-recommendation | **text** | 0.007 | 0.002 | 0.007 | 1.1x bytes_on_air | 3 |
| `D-jitter` | advert-jitter-s | **text** | 0.007 | 0.003 | 0.007 | 1.1x sr_airtime | 3 |
| `M-jitter` | advert-jitter-s | **text** | 0.007 | 0.003 | 0.007 | 1.1x sr_airtime | 3 |
| `M-replayorder` | replay-ordering | **text** | 0.006 | 0.006 | 0.006 | 1.2x sr_bytes | 3 |
| `R-crladder` | coding-rate-ladder | **text** | 0.005 | 0.002 | 0.005 | 1.2x sr_airtime | 3 |
| `L-advert` | advert-transport | **text** | 0.003 | 0.001 | 0.003 | 3.5x sr_airtime | 3 |
| `R-congestion-mode` | congestion-mode | **text** | 0.003 | 0.002 | 0.003 | 1.1x sr_airtime | 3 |
| `R-repeats` | extra-repeats | **held** | 0.003 | 0.002 | 0.001 | 1.1x sr_airtime | 3 |
| `M-combined` | replay-ordering | **held** | 0.002 | 0.002 | 0.002 | 1x sr_bytes | 3 |
| `R-repeats-busy` | extra-repeats | **text** | 0.001 | 0.000 | 0.001 | 1x sr_bytes | 3 |
| `E-signed` | signed | **held** | 0.000 | 0.000 | 0.000 | 1.4x advert_bytes | 3 |
| `R-warm` | warm-num-nodes | **held** | 0.000 | 0.000 | 0.000 | · | 3 |

## Runs

| run | ground | seed base | blocks | missing | warnings |
| --- | --- | --- | --: | --: | --: |
| [`matrix-2026-08-22`](runs/matrix-2026-08-22/trend.md) | batumi | `None` | 2 | 0 | 121 |
| [`design-2026-08-22-8785397`](runs/design-2026-08-22-8785397/trend.md) | batumi | `8785397` | 13 | 0 | 641 |
| [`blocks-2026-08-24-2366879`](runs/blocks-2026-08-24-2366879/trend.md) | ridge | `2366879` | 86 | 1 | 90 |
| [`blocks-2026-08-23-9481139`](runs/blocks-2026-08-23-9481139/trend.md) | valleys | `9481139` | 86 | 1 | 83 |
| [`blocks-2026-08-22-5434544`](runs/blocks-2026-08-22-5434544/trend.md) | rolling | `5434544` | 86 | 1 | 105 |
