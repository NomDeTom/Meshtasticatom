# SF++ sweep explorer

7 scheduled run(s) rolled up, 103 block(s). Open `index.html` for the filterable page; this file is the same data in a diff-readable form.

- **latest** `matrix-2026-08-24` on batumi ground, seed base `None`
- **transport** `591429c`
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
| `Q-control` | protocol | **held** | 0.963 | 0.026 | 0.029 | 1.1x bytes_on_air | 4 |
| `Q-protocol` | protocol | **held** | 0.951 | 0.030 | 0.018 | 1.2x bytes_on_air | 4 |
| `X-pulse` | noise-pulse-interval-ms | **held** | 0.770 | 0.010 | 0.662 | 1.4e+02x sr_airtime | 4 |
| `F-txpower` | tx-power | **held** | 0.769 | 0.095 | 0.728 | 3.8x advert_bytes | 4 |
| `X-siting` | siting-mix | **held** | 0.723 | 0.086 | 0.661 | 6.4x advert_bytes | 4 |
| `R-siting` | siting-mix | **text** | 0.696 | 0.106 | 0.696 | 5x sr_airtime | 4 |
| `X-stretch` | stretch | **text** | 0.695 | 0.059 | 0.695 | 3.4x sr_airtime | 4 |
| `P-bw500` | preset | **text** | 0.559 | 0.099 | 0.559 | 1.9x sr_bytes | 4 |
| `P-eu-presets` | preset | **text** | 0.524 | 0.077 | 0.524 | 2.3x sr_airtime | 4 |
| `P-preset` | preset | **text** | 0.524 | 0.077 | 0.524 | 3.2x sr_airtime | 4 |
| `R-hopscale` | nodes | **held** | 0.502 | 0.061 | 0.511 | 8.9x sr_bytes | 4 |
| `R-oversubscribed` | nodes | **held** | 0.458 | 0.038 | 0.424 | 4.6x bytes_on_air | 4 |
| `Q-topology` | topology | **text** | 0.390 | 0.076 | 0.390 | 2.6x sr_airtime | 4 |
| `X-stretch-duct` | duct-per-hour | **text** | 0.340 | 0.079 | 0.340 | 2x sr_airtime | 4 |
| `X-chatty-hops` | broadcast-interval-s | **text** | 0.340 | 0.018 | 0.340 | 9.4x sr_airtime | 4 |
| `X-chatty` | broadcast-interval-s | **text** | 0.337 | 0.021 | 0.337 | 7.5x sr_airtime | 4 |
| `F-outage` | burst-loss | **text** | 0.325 | 0.020 | 0.325 | 2.6x sr_bytes | 4 |
| `K-density` | nodes | **text** | 0.321 | 0.194 | 0.321 | 8.9x sr_airtime | 4 |
| `F-burst` | burst-loss | **text** | 0.299 | 0.011 | 0.299 | 2.3x sr_bytes | 4 |
| `R-hotstore-stress` | max-num-nodes | **held** | 0.276 | 0.017 | 0.208 | 5.1x sr_airtime | 4 |
| `P-congestion` | no-congestion-scaling | **text** | 0.233 | 0.031 | 0.233 | 4.8x sr_airtime | 4 |
| `F-hoplimit` | hop-limit | **text** | 0.230 | 0.019 | 0.230 | 1.4x bytes_on_air | 4 |
| `K-hopspread` | hop-limit | **text** | 0.215 | 0.017 | 0.215 | 1.3x bytes_on_air | 4 |
| `batumi-x4-SHORT_FAST` | placement | **held** | 0.215 | · | 0.056 | 1.1x bytes_on_air | 1 |
| `batumi-x4-LITE_FAST` | placement | **held** | 0.178 | · | 0.079 | 1.1x bytes_on_air | 1 |
| `K-spread` | hop-spread | **text** | 0.162 | 0.016 | 0.162 | 1.3x advert_bytes | 4 |
| `X-noise` | noise-profile | **held** | 0.159 | 0.012 | 0.164 | 1.4x sr_airtime | 4 |
| `batumi-x4-LONG_FAST` | placement | **held** | 0.145 | · | 0.098 | 1.1x bytes_on_air | 1 |
| `batumi-x1-SHORT_FAST` | placement | **held** | 0.141 | · | 0.087 | 1.1x bytes_on_air | 1 |
| `K-size` | nodes | **text** | 0.140 | 0.032 | 0.140 | 7.5x sr_bytes | 4 |
| `F-flooding` | role-mix | **text** | 0.139 | 0.031 | 0.139 | 2.5x bytes_on_air | 4 |
| `X-nomute` | role-mix | **text** | 0.139 | 0.031 | 0.139 | 2.5x bytes_on_air | 4 |
| `N-hops` | hops-apart | **held** | 0.137 | 0.103 | 0.031 | 2.9x sr_bytes | 4 |
| `F-loss` | extra-loss | **text** | 0.130 | 0.021 | 0.130 | 1.5x sr_bytes | 4 |
| `R-signing` | signature-policy | **text** | 0.128 | 0.021 | 0.128 | 1.3x sr_airtime | 4 |
| `G-hops` | hops-apart | **held** | 0.126 | 0.098 | 0.030 | 2.9x sr_bytes | 4 |
| `X-amplify-worst` | amplify-worst | **text** | 0.122 | 0.037 | 0.122 | 2x sr_bytes | 4 |
| `R-hotstore` | max-num-nodes | **text** | 0.120 | 0.014 | 0.120 | 2.2x sr_airtime | 4 |
| `X-amplifiers` | amplifier-mix | **text** | 0.117 | 0.061 | 0.117 | 1.3x sr_airtime | 4 |
| `R-platform` | platform-mix | **text** | 0.113 | 0.011 | 0.113 | 2.2x sr_airtime | 4 |
| `Q-interval` | broadcast-interval-s | **text** | 0.108 | 0.022 | 0.108 | 5.6x sr_airtime | 4 |
| `G-place` | place | **held** | 0.108 | 0.069 | 0.038 | 5.8x sr_bytes | 4 |
| `N-place` | place | **held** | 0.108 | 0.069 | 0.038 | 5.8x sr_bytes | 4 |
| `X-duct` | duct-per-hour | **text** | 0.088 | 0.029 | 0.088 | 1.4x bytes_on_air | 4 |
| `R-roles` | role-mix | **text** | 0.085 | 0.025 | 0.085 | 1.4x sr_bytes | 4 |
| `R-roles-fav` | role-mix | **text** | 0.068 | 0.025 | 0.068 | 1.3x sr_bytes | 4 |
| `R-traceroute-small` | traceroute-per-hour | **text** | 0.067 | 0.006 | 0.067 | 1.3x sr_airtime | 4 |
| `X-badrouters` | role-placement | **text** | 0.067 | 0.037 | 0.067 | 1.2x sr_bytes | 4 |
| `R-mixed` | legacy-fraction | **text** | 0.062 | 0.027 | 0.062 | 2x bytes_on_air | 4 |
| `D-cadence` | trigger | **held** | 0.061 | 0.017 | 0.030 | 18x sr_bytes | 4 |
| `R-traceroute` | traceroute-per-hour | **text** | 0.054 | 0.011 | 0.054 | 1.4x sr_airtime | 4 |
| `R-rebroadcast` | rebroadcast-mode | **held** | 0.050 | 0.021 | 0.004 | 22x sr_airtime | 4 |
| `R-mixed-26` | legacy-fraction | **held** | 0.043 | 0.024 | 0.060 | 2.1x bytes_on_air | 4 |
| `R-congestion-input` | congestion-input | **held** | 0.035 | 0.011 | 0.034 | 1.5x sr_airtime | 4 |
| `R-versions` | profile | **text** | 0.029 | 0.019 | 0.029 | 3.4x bytes_on_air | 4 |
| `R-firmware` | profile | **text** | 0.028 | 0.021 | 0.028 | 3.4x bytes_on_air | 4 |
| `R-routerlate` | router-late-fraction | **text** | 0.027 | 0.024 | 0.027 | 1.4x bytes_on_air | 4 |
| `L-provide` | provide-transport | **text** | 0.027 | 0.008 | 0.027 | 2.5x sr_airtime | 4 |
| `P-catchup` | catch-up-hours | **text** | 0.027 | 0.007 | 0.027 | 13x sr_bytes | 4 |
| `X-worst` | role-placement | **text** | 0.026 | 0.012 | 0.026 | 1.6x sr_bytes | 4 |
| `G-servers` | servers | **held** | 0.024 | 0.012 | 0.010 | 6.9x sr_bytes | 4 |
| `N-servers` | servers | **held** | 0.024 | 0.012 | 0.010 | 6.9x sr_bytes | 4 |
| `R-signing-cost` | profile-flag | **held** | 0.024 | 0.017 | 0.040 | 3.2x bytes_on_air | 4 |
| `J-wincap` | capacity | **held** | 0.021 | 0.013 | 0.005 | 1.9x advert_bytes | 4 |
| `R-favourites` | favourite-routers | **text** | 0.020 | 0.013 | 0.020 | 1.1x sr_bytes | 4 |
| `R-dmmode` | dm-mode | **text** | 0.018 | 0.011 | 0.018 | 1.3x sr_airtime | 4 |
| `Q-hopassign` | hop-assign | **held** | 0.018 | 0.014 | 0.007 | 1.1x sr_airtime | 4 |
| `R-srretries` | sr-retries | **held** | 0.018 | 0.011 | 0.013 | 1.2x sr_bytes | 4 |
| `E-capacity` | capacity | **held** | 0.013 | 0.006 | 0.009 | 5.3x advert_bytes | 4 |
| `M-capacity` | capacity | **held** | 0.013 | 0.006 | 0.009 | 5.3x advert_bytes | 4 |
| `P-diurnal` | diurnal | **held** | 0.013 | 0.011 | 0.019 | 1.4x sr_bytes | 4 |
| `J-window` | window-size | **text** | 0.012 | 0.003 | 0.012 | 6.3x advert_bytes | 4 |
| `E-width` | short-id-bits | **held** | 0.011 | 0.003 | 0.011 | 3.2x advert_bytes | 4 |
| `J-timewin` | time-bucket-s | **held** | 0.011 | 0.006 | 0.011 | 5.4x advert_bytes | 4 |
| `J-bucketmode` | bucket-mode | **text** | 0.011 | 0.002 | 0.011 | 3.3x advert_bytes | 4 |
| `D-jitter` | advert-jitter-s | **held** | 0.009 | 0.003 | 0.006 | 1.1x sr_airtime | 4 |
| `M-jitter` | advert-jitter-s | **held** | 0.009 | 0.003 | 0.006 | 1.1x sr_airtime | 4 |
| `D-resolve` | resolve | **held** | 0.009 | 0.008 | 0.009 | 5.7x advert_bytes | 4 |
| `R-dmmode-cr` | dm-mode | **text** | 0.008 | 0.005 | 0.008 | 1.1x sr_bytes | 4 |
| `R-crladder` | coding-rate-ladder | **text** | 0.007 | 0.003 | 0.007 | 1.1x sr_airtime | 4 |
| `R-adopt` | no-adopt-hop-recommendation | **text** | 0.006 | 0.002 | 0.006 | 1.2x sr_airtime | 4 |
| `M-replayorder` | replay-ordering | **text** | 0.006 | 0.005 | 0.006 | 1.2x sr_bytes | 4 |
| `L-advert` | advert-transport | **text** | 0.005 | 0.003 | 0.005 | 2.7x sr_airtime | 4 |
| `R-repeats` | extra-repeats | **held** | 0.003 | 0.002 | 0.001 | 1.1x sr_bytes | 4 |
| `G-allrouters` | servers | **held** | 0.003 | 0.003 | 0.006 | 2.8x sr_bytes | 4 |
| `R-congestion-mode` | congestion-mode | **text** | 0.002 | 0.002 | 0.002 | 1x bytes_on_air | 4 |
| `M-combined` | replay-ordering | **text** | 0.002 | 0.002 | 0.002 | 1.1x sr_bytes | 4 |
| `R-repeats-busy` | extra-repeats | **text** | 0.001 | 0.000 | 0.001 | 1x sr_bytes | 4 |
| `E-signed` | signed | **held** | 0.000 | 0.000 | 0.000 | 1.4x advert_bytes | 4 |
| `R-warm` | warm-num-nodes | **held** | 0.000 | 0.000 | 0.000 | · | 4 |

## Runs

| run | ground | seed base | blocks | missing | warnings |
| --- | --- | --- | --: | --: | --: |
| [`matrix-2026-08-24`](runs/matrix-2026-08-24/trend.md) | batumi | `None` | 2 | 0 | 119 |
| [`matrix-2026-08-22`](runs/matrix-2026-08-22/trend.md) | batumi | `None` | 2 | 0 | 121 |
| [`design-2026-08-22-8785397`](runs/design-2026-08-22-8785397/trend.md) | batumi | `8785397` | 13 | 0 | 641 |
| [`blocks-2026-08-25-6335397`](runs/blocks-2026-08-25-6335397/trend.md) | rolling | `6335397` | 86 | 1 | 98 |
| [`blocks-2026-08-24-2366879`](runs/blocks-2026-08-24-2366879/trend.md) | ridge | `2366879` | 86 | 1 | 90 |
| [`blocks-2026-08-23-9481139`](runs/blocks-2026-08-23-9481139/trend.md) | valleys | `9481139` | 86 | 1 | 83 |
| [`blocks-2026-08-22-5434544`](runs/blocks-2026-08-22-5434544/trend.md) | rolling | `5434544` | 86 | 1 | 105 |
