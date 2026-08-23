# SF++ sweep explorer

4 scheduled run(s) rolled up, 101 block(s). Open `index.html` for the filterable page; this file is the same data in a diff-readable form.

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
| `Q-control` | protocol | **held** | 0.967 | 0.030 | 0.015 | 1.1x bytes_on_air | 2 |
| `Q-protocol` | protocol | **held** | 0.965 | 0.029 | 0.012 | 1.2x bytes_on_air | 2 |
| `F-txpower` | tx-power | **held** | 0.847 | 0.012 | 0.751 | 12x sr_airtime | 2 |
| `X-pulse` | noise-pulse-interval-ms | **held** | 0.776 | 0.005 | 0.674 | 95x sr_airtime | 2 |
| `X-siting` | siting-mix | **held** | 0.760 | 0.001 | 0.680 | 7.1x advert_bytes | 2 |
| `X-stretch` | stretch | **text** | 0.714 | 0.056 | 0.714 | 3.4x sr_airtime | 2 |
| `P-bw500` | preset | **held** | 0.639 | 0.134 | 0.597 | 2.4x advert_bytes | 2 |
| `R-siting` | siting-mix | **text** | 0.618 | 0.063 | 0.618 | 3.2x sr_airtime | 2 |
| `R-hopscale` | nodes | **text** | 0.522 | 0.063 | 0.522 | 12x sr_bytes | 2 |
| `P-eu-presets` | preset | **text** | 0.484 | 0.040 | 0.484 | 2.8x sr_airtime | 2 |
| `P-preset` | preset | **text** | 0.484 | 0.040 | 0.484 | 4x sr_airtime | 2 |
| `R-oversubscribed` | nodes | **held** | 0.465 | 0.063 | 0.418 | 5x sr_bytes | 2 |
| `Q-topology` | topology | **text** | 0.353 | 0.037 | 0.353 | 3.1x sr_bytes | 2 |
| `X-chatty` | broadcast-interval-s | **text** | 0.339 | 0.008 | 0.339 | 7.9x sr_airtime | 2 |
| `X-chatty-hops` | broadcast-interval-s | **text** | 0.335 | 0.014 | 0.335 | 7.8x sr_airtime | 2 |
| `F-outage` | burst-loss | **text** | 0.329 | 0.002 | 0.329 | 2.6x sr_bytes | 2 |
| `F-burst` | burst-loss | **text** | 0.298 | 0.014 | 0.298 | 2.5x sr_bytes | 2 |
| `X-stretch-duct` | duct-per-hour | **text** | 0.290 | 0.004 | 0.290 | 1.9x sr_airtime | 2 |
| `R-hotstore-stress` | max-num-nodes | **held** | 0.286 | 0.001 | 0.215 | 6x sr_airtime | 2 |
| `P-congestion` | no-congestion-scaling | **text** | 0.257 | 0.015 | 0.257 | 4.6x sr_airtime | 2 |
| `K-density` | nodes | **text** | 0.250 | 0.146 | 0.250 | 4.4x advert_bytes | 2 |
| `F-hoplimit` | hop-limit | **text** | 0.228 | 0.026 | 0.228 | 2.1x sr_bytes | 2 |
| `K-hopspread` | hop-limit | **text** | 0.212 | 0.019 | 0.212 | 2x sr_bytes | 2 |
| `batumi-x4-LITE_FAST` | placement | **held** | 0.178 | · | 0.079 | 1.1x bytes_on_air | 1 |
| `K-spread` | hop-spread | **text** | 0.157 | 0.007 | 0.157 | 1.9x sr_bytes | 2 |
| `X-noise` | noise-profile | **text** | 0.155 | 0.008 | 0.155 | 1.4x sr_bytes | 2 |
| `K-size` | nodes | **text** | 0.151 | 0.010 | 0.151 | 4.3x advert_bytes | 2 |
| `F-flooding` | role-mix | **text** | 0.145 | 0.017 | 0.145 | 2.5x bytes_on_air | 2 |
| `X-nomute` | role-mix | **text** | 0.145 | 0.017 | 0.145 | 2.5x bytes_on_air | 2 |
| `G-hops` | hops-apart | **held** | 0.144 | 0.156 | 0.017 | 1.9x sr_bytes | 2 |
| `N-hops` | hops-apart | **held** | 0.144 | 0.156 | 0.019 | 1.9x sr_bytes | 2 |
| `batumi-x1-SHORT_FAST` | placement | **held** | 0.141 | · | 0.087 | 1.1x bytes_on_air | 1 |
| `F-loss` | extra-loss | **text** | 0.122 | 0.032 | 0.122 | 1.8x sr_bytes | 2 |
| `G-place` | place | **held** | 0.117 | 0.112 | 0.038 | 3.1x sr_bytes | 2 |
| `N-place` | place | **held** | 0.117 | 0.112 | 0.038 | 3.1x sr_bytes | 2 |
| `R-signing` | signature-policy | **text** | 0.113 | 0.012 | 0.113 | 1.2x sr_airtime | 2 |
| `R-hotstore` | max-num-nodes | **text** | 0.111 | 0.015 | 0.111 | 2.1x sr_airtime | 2 |
| `X-amplify-worst` | amplify-worst | **text** | 0.109 | 0.030 | 0.109 | 1.2x sr_airtime | 2 |
| `R-platform` | platform-mix | **text** | 0.106 | 0.010 | 0.106 | 2.1x sr_airtime | 2 |
| `R-roles` | role-mix | **text** | 0.105 | 0.013 | 0.105 | 1.2x bytes_on_air | 2 |
| `Q-interval` | broadcast-interval-s | **text** | 0.094 | 0.024 | 0.094 | 5.3x sr_airtime | 2 |
| `R-roles-fav` | role-mix | **text** | 0.089 | 0.001 | 0.089 | 1.1x sr_airtime | 2 |
| `X-amplifiers` | amplifier-mix | **text** | 0.084 | 0.019 | 0.084 | 1.3x sr_bytes | 2 |
| `X-duct` | duct-per-hour | **text** | 0.076 | 0.012 | 0.076 | 1.3x bytes_on_air | 2 |
| `R-mixed-26` | legacy-fraction | **text** | 0.069 | 0.045 | 0.069 | 2.1x bytes_on_air | 2 |
| `R-mixed` | legacy-fraction | **text** | 0.065 | 0.043 | 0.065 | 2x bytes_on_air | 2 |
| `R-traceroute-small` | traceroute-per-hour | **held** | 0.062 | 0.008 | 0.065 | 1.3x sr_airtime | 2 |
| `D-cadence` | trigger | **held** | 0.060 | 0.026 | 0.024 | 13x advert_bytes | 2 |
| `R-rebroadcast` | rebroadcast-mode | **held** | 0.055 | 0.030 | 0.003 | 15x sr_airtime | 2 |
| `R-traceroute` | traceroute-per-hour | **text** | 0.047 | 0.007 | 0.047 | 1.4x sr_airtime | 2 |
| `R-signing-cost` | profile-flag | **text** | 0.044 | 0.009 | 0.044 | 3.3x bytes_on_air | 2 |
| `L-provide` | provide-transport | **text** | 0.034 | 0.002 | 0.034 | 2.6x sr_airtime | 2 |
| `R-congestion-input` | congestion-input | **text** | 0.033 | 0.002 | 0.033 | 1.4x sr_airtime | 2 |
| `X-badrouters` | role-placement | **held** | 0.032 | 0.019 | 0.051 | 1.5x sr_bytes | 2 |
| `R-favourites` | favourite-routers | **text** | 0.027 | 0.017 | 0.027 | 1.1x sr_bytes | 2 |
| `P-catchup` | catch-up-hours | **text** | 0.025 | 0.009 | 0.025 | 9.2x advert_bytes | 2 |
| `R-versions` | profile | **text** | 0.022 | 0.021 | 0.022 | 3.3x bytes_on_air | 2 |
| `R-firmware` | profile | **text** | 0.018 | 0.018 | 0.018 | 3.1x bytes_on_air | 2 |
| `R-srretries` | sr-retries | **text** | 0.016 | 0.001 | 0.016 | 1.1x sr_bytes | 2 |
| `P-diurnal` | diurnal | **text** | 0.016 | 0.012 | 0.016 | 1.2x advert_bytes | 2 |
| `J-timewin` | time-bucket-s | **text** | 0.015 | 0.002 | 0.015 | 5.5x advert_bytes | 2 |
| `R-routerlate` | router-late-fraction | **held** | 0.013 | 0.012 | 0.017 | 1.3x bytes_on_air | 2 |
| `E-width` | short-id-bits | **text** | 0.012 | 0.004 | 0.012 | 3.1x advert_bytes | 2 |
| `X-worst` | role-placement | **held** | 0.011 | 0.005 | 0.025 | 1.1x sr_bytes | 2 |
| `G-servers` | servers | **text** | 0.011 | 0.003 | 0.011 | 7.7x sr_bytes | 2 |
| `N-servers` | servers | **text** | 0.011 | 0.003 | 0.011 | 7.7x sr_bytes | 2 |
| `R-dmmode` | dm-mode | **text** | 0.011 | 0.011 | 0.011 | 1.3x sr_airtime | 2 |
| `D-jitter` | advert-jitter-s | **held** | 0.010 | 0.004 | 0.005 | 1.2x sr_airtime | 2 |
| `M-jitter` | advert-jitter-s | **held** | 0.010 | 0.004 | 0.005 | 1.2x sr_airtime | 2 |
| `J-window` | window-size | **held** | 0.010 | 0.006 | 0.010 | 5.2x advert_bytes | 2 |
| `Q-hopassign` | hop-assign | **held** | 0.010 | 0.002 | 0.004 | 1.3x sr_airtime | 2 |
| `E-capacity` | capacity | **held** | 0.009 | 0.002 | 0.005 | 5.3x advert_bytes | 2 |
| `M-capacity` | capacity | **held** | 0.009 | 0.002 | 0.005 | 5.3x advert_bytes | 2 |
| `G-allrouters` | servers | **text** | 0.009 | 0.002 | 0.009 | 2.3x sr_bytes | 2 |
| `J-bucketmode` | bucket-mode | **held** | 0.009 | 0.006 | 0.011 | 2.7x advert_bytes | 2 |
| `R-adopt` | no-adopt-hop-recommendation | **text** | 0.007 | 0.003 | 0.007 | 1.1x bytes_on_air | 2 |
| `R-dmmode-cr` | dm-mode | **held** | 0.004 | 0.005 | 0.007 | 1.2x sr_airtime | 2 |
| `R-congestion-mode` | congestion-mode | **text** | 0.004 | 0.002 | 0.004 | 1.1x sr_airtime | 2 |
| `J-wincap` | capacity | **text** | 0.003 | 0.003 | 0.003 | 2.3x advert_bytes | 2 |
| `R-crladder` | coding-rate-ladder | **held** | 0.003 | 0.004 | 0.004 | 1.1x sr_bytes | 2 |
| `L-advert` | advert-transport | **text** | 0.003 | 0.001 | 0.003 | 2.9x sr_airtime | 2 |
| `M-combined` | replay-ordering | **text** | 0.003 | 0.002 | 0.003 | 1x sr_bytes | 2 |
| `M-replayorder` | replay-ordering | **text** | 0.003 | 0.001 | 0.003 | 1.2x sr_bytes | 2 |
| `D-resolve` | resolve | **held** | 0.002 | 0.003 | 0.006 | 5.7x advert_bytes | 2 |
| `R-repeats-busy` | extra-repeats | **held** | 0.001 | 0.001 | 0.001 | 1x sr_airtime | 2 |
| `R-repeats` | extra-repeats | **text** | 0.001 | 0.001 | 0.001 | 1.1x sr_bytes | 2 |
| `E-signed` | signed | **held** | 0.000 | 0.000 | 0.000 | 1.4x advert_bytes | 2 |
| `R-warm` | warm-num-nodes | **held** | 0.000 | 0.000 | 0.000 | · | 2 |

## Runs

| run | ground | seed base | blocks | missing | warnings |
| --- | --- | --- | --: | --: | --: |
| [`matrix-2026-08-22`](runs/matrix-2026-08-22/trend.md) | batumi | `None` | 2 | 0 | 121 |
| [`design-2026-08-22-8785397`](runs/design-2026-08-22-8785397/trend.md) | batumi | `8785397` | 13 | 0 | 641 |
| [`blocks-2026-08-23-9481139`](runs/blocks-2026-08-23-9481139/trend.md) | valleys | `9481139` | 86 | 1 | 83 |
| [`blocks-2026-08-22-5434544`](runs/blocks-2026-08-22-5434544/trend.md) | rolling | `5434544` | 86 | 1 | 105 |
