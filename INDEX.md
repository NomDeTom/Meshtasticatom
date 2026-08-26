# SF++ sweep explorer

11 scheduled run(s) rolled up, 132 block(s). Open `index.html` for the filterable page; this file is the same data in a diff-readable form.

- **latest** `matrix-2026-08-25` on batumi ground, seed base `None`
- **transport** `591429c`
- **sim version** `1.4.0`, excluding 11 superseded run(s) from every metric below

## What moves a delivery measure

| block | arm | measure | spread | run-to-run sd | text spread | price | runs |
| --- | --- | --- | --: | --: | --: | --- | --: |
| `batumi-hop-limit-15` | archive | **held** | 0.988 | · | 0.067 | 1.3x bytes_on_air | 1 |
| `batumi-hop-limit-7` | archive | **held** | 0.988 | · | 0.067 | 1.3x bytes_on_air | 1 |
| `batumi-m4-early-flood` | archive | **held** | 0.986 | · | 0.067 | 1.2x bytes_on_air | 1 |
| `batumi-congestion-40` | archive | **held** | 0.985 | · | 0.070 | 1.2x bytes_on_air | 1 |
| `batumi-hop-scaling-40` | archive | **held** | 0.985 | · | 0.070 | 1.2x bytes_on_air | 1 |
| `batumi-none` | archive | **held** | 0.985 | · | 0.070 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-coding-rate-ladder` | archive | **held** | 0.985 | · | 0.008 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-m4-early-flood` | archive | **held** | 0.985 | · | 0.008 | 1.2x bytes_on_air | 1 |
| `batumi-extra-repeats` | archive | **held** | 0.985 | · | 0.072 | 1.2x bytes_on_air | 1 |
| `batumi-coding-rate-ladder` | archive | **held** | 0.985 | · | 0.076 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-extra-repeats` | archive | **held** | 0.984 | · | 0.007 | 1.1x bytes_on_air | 1 |
| `batumi-short-fast-congestion-40` | archive | **held** | 0.984 | · | 0.011 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-hop-scaling-40` | archive | **held** | 0.984 | · | 0.011 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-none` | archive | **held** | 0.984 | · | 0.011 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-favourite-routers` | archive | **held** | 0.984 | · | 0.009 | 1.2x bytes_on_air | 1 |
| `batumi-favourite-routers` | archive | **held** | 0.984 | · | 0.077 | 1.3x bytes_on_air | 1 |
| `batumi-short-fast-congestion-60` | archive | **held** | 0.984 | · | 0.010 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-hop-limit-15` | archive | **held** | 0.984 | · | 0.007 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-hop-limit-7` | archive | **held** | 0.984 | · | 0.007 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-congestion-80` | archive | **held** | 0.983 | · | 0.007 | 1.1x bytes_on_air | 1 |
| `batumi-short-fast-hop-scaling-80` | archive | **held** | 0.980 | · | 0.010 | 1.1x bytes_on_air | 1 |
| `batumi-hop-scaling-80` | archive | **held** | 0.979 | · | 0.086 | 1.2x bytes_on_air | 1 |
| `batumi-hop-scaling-60` | archive | **held** | 0.979 | · | 0.086 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-hop-scaling-60` | archive | **held** | 0.979 | · | 0.010 | 1.1x bytes_on_air | 1 |
| `BL-control` | protocol | **held** | 0.967 | 0.024 | 0.026 | 1x bytes_on_air | 5 |
| `batumi-congestion-60` | archive | **held** | 0.963 | · | 0.145 | 1.2x bytes_on_air | 1 |
| `PR-protocol` | protocol | **held** | 0.955 | 0.027 | 0.017 | 1.1x bytes_on_air | 5 |
| `RF-preset-turbo` | preset | **held** | 0.894 | · | 0.793 | 31x sr_bytes | 1 |
| `RF-txpower` | tx-power | **held** | 0.789 | 0.094 | 0.740 | 12x advert_bytes | 5 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.777 | 0.017 | 0.668 | 93x sr_airtime | 5 |
| `AD-siting` | siting-mix | **held** | 0.746 | 0.091 | 0.678 | 10x advert_bytes | 5 |
| `MS-siting` | siting-mix | **text** | 0.722 | 0.108 | 0.722 | 6.9x sr_airtime | 5 |
| `batumi-congestion-80` | archive | **held** | 0.720 | · | 0.125 | 1x bytes_on_air | 1 |
| `MS-stretch` | stretch | **held** | 0.680 | 0.073 | 0.708 | 7.2x sr_bytes | 5 |
| `RF-bw500` | preset | **held** | 0.598 | 0.141 | 0.571 | 7.6x sr_bytes | 5 |
| `RF-preset` | preset | **held** | 0.531 | 0.111 | 0.543 | 7.7x sr_airtime | 5 |
| `RF-eu-presets` | preset | **held** | 0.526 | 0.105 | 0.543 | 7.2x sr_bytes | 5 |
| `MS-hopscale` | nodes | **text** | 0.511 | 0.049 | 0.511 | 12x sr_bytes | 5 |
| `MS-oversubscribed` | nodes | **held** | 0.455 | 0.034 | 0.424 | 4.8x bytes_on_air | 5 |
| `batumi-x4-hop-limit-15` | archive | **held** | 0.431 | · | 0.028 | 1.2x bytes_on_air | 1 |
| `batumi-x4-hop-limit-7` | archive | **held** | 0.431 | · | 0.028 | 1.2x bytes_on_air | 1 |
| `batumi-x4-congestion-40` | archive | **held** | 0.429 | · | 0.029 | 1.2x bytes_on_air | 1 |
| `batumi-x4-hop-scaling-40` | archive | **held** | 0.429 | · | 0.029 | 1.2x bytes_on_air | 1 |
| `batumi-x4-none` | archive | **held** | 0.429 | · | 0.029 | 1.2x bytes_on_air | 1 |
| `batumi-x4-m4-early-flood` | archive | **held** | 0.429 | · | 0.028 | 1.2x bytes_on_air | 1 |
| `batumi-x4-extra-repeats` | archive | **held** | 0.429 | · | 0.030 | 1.2x bytes_on_air | 1 |
| `batumi-x4-favourite-routers` | archive | **held** | 0.428 | · | 0.030 | 1.2x bytes_on_air | 1 |
| `batumi-x4-coding-rate-ladder` | archive | **held** | 0.427 | · | 0.030 | 1.2x bytes_on_air | 1 |
| `batumi-x4-hop-scaling-60` | archive | **held** | 0.415 | · | 0.026 | 1.2x bytes_on_air | 1 |
| `batumi-x4-hop-scaling-80` | archive | **held** | 0.414 | · | 0.027 | 1.2x bytes_on_air | 1 |
| `batumi-x4-congestion-60` | archive | **held** | 0.405 | · | 0.024 | 1.1x bytes_on_air | 1 |
| `batumi-x4-congestion-80` | archive | **held** | 0.364 | · | 0.016 | 1.1x bytes_on_air | 1 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.348 | 0.071 | 0.348 | 3.2x sr_airtime | 5 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.336 | 0.018 | 0.336 | 7.1x sr_airtime | 5 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.335 | 0.019 | 0.335 | 7.6x sr_airtime | 5 |
| `DG-outage` | burst-loss | **text** | 0.329 | 0.020 | 0.329 | 2.3x sr_bytes | 5 |
| `MS-density` | nodes | **text** | 0.309 | 0.170 | 0.309 | 6.5x sr_airtime | 5 |
| `DG-burst` | burst-loss | **text** | 0.303 | 0.014 | 0.303 | 2.5x sr_bytes | 5 |
| `MS-topology` | topology | **held** | 0.288 | 0.173 | 0.395 | 3.5x sr_airtime | 5 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.282 | 0.021 | 0.210 | 6x sr_airtime | 5 |
| `RT-hoplimit` | hop-limit | **text** | 0.237 | 0.022 | 0.237 | 2.4x sr_bytes | 5 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.224 | 0.034 | 0.224 | 3.8x sr_airtime | 5 |
| `RT-hopspread` | hop-limit | **text** | 0.220 | 0.019 | 0.220 | 2.1x sr_bytes | 5 |
| `batumi-x4-SHORT_FAST` | placement | **held** | 0.215 | · | 0.056 | 1.1x bytes_on_air | 1 |
| `SF-hops-spread` | hops-apart | **held** | 0.186 | 0.142 | 0.029 | 2.1x sr_bytes | 5 |
| `batumi-x4-LITE_FAST` | placement | **held** | 0.178 | · | 0.079 | 1.1x bytes_on_air | 1 |
| `RT-spread` | hop-spread | **text** | 0.169 | 0.021 | 0.169 | 1.8x sr_bytes | 5 |
| `RF-noise` | noise-profile | **text** | 0.164 | 0.011 | 0.164 | 1.3x sr_bytes | 5 |
| `SF-hops-flat` | hops-apart | **held** | 0.163 | 0.119 | 0.028 | 2.1x sr_bytes | 5 |
| `batumi-x4-LONG_FAST` | placement | **held** | 0.145 | · | 0.098 | 1.1x bytes_on_air | 1 |
| `batumi-x1-SHORT_FAST` | placement | **held** | 0.141 | · | 0.087 | 1.1x bytes_on_air | 1 |
| `MS-size` | nodes | **text** | 0.139 | 0.028 | 0.139 | 5.6x sr_bytes | 5 |
| `AD-flooding` | role-mix | **text** | 0.136 | 0.028 | 0.136 | 2.4x bytes_on_air | 5 |
| `AD-nomute` | role-mix | **text** | 0.136 | 0.028 | 0.136 | 2.4x bytes_on_air | 5 |
| `DG-loss` | extra-loss | **text** | 0.129 | 0.018 | 0.129 | 1.6x sr_bytes | 5 |
| `SC-signing` | signature-policy | **text** | 0.128 | 0.019 | 0.128 | 1.3x sr_airtime | 5 |
| `DB-hotstore` | max-num-nodes | **text** | 0.123 | 0.013 | 0.123 | 2.1x sr_airtime | 5 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.119 | 0.033 | 0.119 | 1.9x sr_bytes | 5 |
| `DB-platform` | platform-mix | **text** | 0.116 | 0.012 | 0.116 | 2.1x sr_airtime | 5 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.116 | 0.053 | 0.116 | 1.2x bytes_on_air | 5 |
| `LD-interval` | broadcast-interval-s | **text** | 0.105 | 0.020 | 0.105 | 5.6x sr_airtime | 5 |
| `SF-place-flat` | place | **held** | 0.096 | 0.065 | 0.035 | 2.8x sr_bytes | 5 |
| `SF-place-spread` | place | **held** | 0.096 | 0.065 | 0.035 | 2.8x sr_bytes | 5 |
| `RF-duct` | duct-per-hour | **text** | 0.086 | 0.026 | 0.086 | 1.3x bytes_on_air | 5 |
| `MS-roles` | role-mix | **text** | 0.078 | 0.027 | 0.078 | 1.2x bytes_on_air | 5 |
| `AD-badrouters` | role-placement | **text** | 0.066 | 0.032 | 0.066 | 1.7x sr_bytes | 5 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.065 | 0.007 | 0.065 | 1.2x sr_airtime | 5 |
| `FW-mixed` | legacy-fraction | **text** | 0.061 | 0.024 | 0.061 | 2.2x bytes_on_air | 5 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.060 | 0.025 | 0.060 | 2.3x bytes_on_air | 5 |
| `SF-cadence` | trigger | **held** | 0.058 | 0.017 | 0.029 | 14x sr_bytes | 5 |
| `MS-roles-fav` | role-mix | **text** | 0.056 | 0.035 | 0.056 | 1.2x sr_airtime | 5 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.052 | 0.011 | 0.052 | 1.5x sr_airtime | 5 |
| `batumi-x1-LITE_FAST` | placement | **held** | 0.050 | · | 0.025 | 1.1x bytes_on_air | 1 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.049 | 0.019 | 0.004 | 26x sr_airtime | 5 |
| `FW-signing-cost` | profile-flag | **text** | 0.039 | 0.007 | 0.039 | 3.3x bytes_on_air | 5 |
| `TH-congestion-input` | congestion-input | **text** | 0.033 | 0.002 | 0.033 | 1.4x sr_airtime | 5 |
| `AD-worst` | role-placement | **text** | 0.031 | 0.015 | 0.031 | 1.3x sr_bytes | 5 |
| `FW-versions` | profile | **text** | 0.027 | 0.017 | 0.027 | 3.5x bytes_on_air | 5 |
| `SF-catchup` | catch-up-hours | **text** | 0.026 | 0.006 | 0.026 | 10x sr_bytes | 5 |
| `SF-provide-transport` | provide-transport | **text** | 0.025 | 0.008 | 0.025 | 2.1x sr_airtime | 5 |
| `SF-servers-flat` | servers | **held** | 0.022 | 0.012 | 0.010 | 6x sr_bytes | 5 |
| `SF-servers-spread` | servers | **held** | 0.022 | 0.012 | 0.010 | 6x sr_bytes | 5 |
| `batumi-x1-LONG_FAST` | placement | **held** | 0.021 | · | 0.003 | 1.2x bytes_on_air | 1 |
| `MS-router-late` | router-late-fraction | **held** | 0.020 | 0.013 | 0.022 | 1.3x bytes_on_air | 5 |
| `LD-diurnal` | diurnal | **text** | 0.019 | 0.007 | 0.019 | 1.3x sr_bytes | 5 |
| `RT-favourites` | favourite-routers | **text** | 0.019 | 0.012 | 0.019 | 1.2x sr_bytes | 5 |
| `SF-capacity-window` | capacity | **held** | 0.019 | 0.012 | 0.005 | 2x advert_bytes | 5 |
| `DM-mode` | dm-mode | **text** | 0.019 | 0.009 | 0.019 | 1.2x sr_airtime | 5 |
| `SF-sr-retries` | sr-retries | **held** | 0.018 | 0.009 | 0.012 | 1.2x sr_bytes | 5 |
| `FW-firmware` | profile | **held** | 0.016 | 0.013 | 0.024 | 3.3x bytes_on_air | 5 |
| `RT-hopassign` | hop-assign | **text** | 0.015 | 0.019 | 0.015 | 1.3x sr_bytes | 5 |
| `SF-window-size` | window-size | **text** | 0.012 | 0.002 | 0.012 | 5x advert_bytes | 5 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.012 | 0.006 | 0.012 | 5.4x advert_bytes | 5 |
| `SF-width` | short-id-bits | **held** | 0.011 | 0.003 | 0.010 | 3.1x advert_bytes | 5 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.010 | 0.003 | 0.007 | 1.1x sr_airtime | 5 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.010 | 0.003 | 0.007 | 1.1x sr_airtime | 5 |
| `SF-resolve` | resolve | **held** | 0.009 | 0.007 | 0.007 | 5.9x advert_bytes | 5 |
| `SF-capacity` | capacity | **text** | 0.009 | 0.004 | 0.009 | 5.4x advert_bytes | 5 |
| `SF-capacity-local` | capacity | **text** | 0.009 | 0.004 | 0.009 | 5.4x advert_bytes | 5 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.008 | 0.003 | 0.010 | 2.7x advert_bytes | 5 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.007 | 0.003 | 0.007 | 1.1x sr_airtime | 5 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.007 | 0.002 | 0.007 | 1.2x bytes_on_air | 5 |
| `SF-replay-order` | replay-ordering | **text** | 0.005 | 0.004 | 0.005 | 1x sr_bytes | 5 |
| `SF-servers-allrouters` | servers | **held** | 0.005 | 0.005 | 0.006 | 2.5x sr_bytes | 5 |
| `SF-advert-transport` | advert-transport | **text** | 0.005 | 0.003 | 0.005 | 2.8x sr_airtime | 5 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.004 | 0.003 | 0.006 | 1.1x sr_airtime | 5 |
| `PR-repeats` | extra-repeats | **text** | 0.003 | 0.004 | 0.003 | 1.1x sr_airtime | 5 |
| `SF-replay-order-broadcast` | replay-ordering | **text** | 0.003 | 0.002 | 0.003 | 1.1x sr_bytes | 5 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.001 | 0.001 | 0.001 | 1.1x sr_bytes | 5 |
| `TH-congestion-mode` | congestion-mode | **held** | 0.001 | 0.001 | 0.002 | 1.1x sr_airtime | 5 |
| `SF-signed` | signed | **held** | 0.000 | 0.000 | 0.000 | 1.4x advert_bytes | 5 |
| `DB-warm` | warm-num-nodes | **held** | 0.000 | 0.000 | 0.000 | · | 5 |

## Runs

| run | ground | seed base | blocks | missing | warnings |
| --- | --- | --- | --: | --: | --: |
| [`matrix-2026-08-25`](runs/matrix-2026-08-25/trend.md) | batumi | `None` | 2 | 0 | 161 |
| [`matrix-2026-08-24`](runs/matrix-2026-08-24/trend.md) | batumi | `None` | 2 | 0 | 119 |
| [`matrix-2026-08-22`](runs/matrix-2026-08-22/trend.md) | batumi | `None` | 2 | 0 | 121 |
| [`design-2026-08-25-8765439`](runs/design-2026-08-25-8765439/trend.md) | batumi | `8765439` | 13 | 0 | 605 |
| [`design-2026-08-24-4578693`](runs/design-2026-08-24-4578693/trend.md) | batumi | `4578693` | 13 | 0 | 669 |
| [`design-2026-08-22-8785397`](runs/design-2026-08-22-8785397/trend.md) | batumi | `8785397` | 13 | 0 | 641 |
| [`blocks-2026-08-26-7218105`](runs/blocks-2026-08-26-7218105/trend.md) | valleys | `7218105` | 87 | 0 | 73 |
| [`blocks-2026-08-25-6335397`](runs/blocks-2026-08-25-6335397/trend.md) | rolling | `6335397` | 86 | 1 | 98 |
| [`blocks-2026-08-24-2366879`](runs/blocks-2026-08-24-2366879/trend.md) | ridge | `2366879` | 86 | 1 | 90 |
| [`blocks-2026-08-23-9481139`](runs/blocks-2026-08-23-9481139/trend.md) | valleys | `9481139` | 86 | 1 | 83 |
| [`blocks-2026-08-22-5434544`](runs/blocks-2026-08-22-5434544/trend.md) | rolling | `5434544` | 86 | 1 | 105 |
