# SF++ sweep explorer

9 scheduled run(s) rolled up, 119 block(s). Open `index.html` for the filterable page; this file is the same data in a diff-readable form.

- **latest** `matrix-2026-08-29-1024` on batumi ground, seed base `None`
- **transport** `4195f52`
- **sim version** `1.6.1`, excluding 24 superseded run(s) from every metric below

## What moves a delivery measure

| block | arm | measure | spread | run-to-run sd | text spread | price | runs |
| --- | --- | --- | --: | --: | --: | --- | --: |
| `batumi-legacy-50-hop-scaling-80` | archive | **held** | 0.998 | · | 0.047 | 1.3x bytes_on_air | 1 |
| `batumi-legacy-50-m4-early-flood` | archive | **held** | 0.998 | · | 0.034 | 1.4x bytes_on_air | 1 |
| `batumi-legacy-50-extra-repeats` | archive | **held** | 0.998 | · | 0.035 | 1.4x bytes_on_air | 1 |
| `batumi-legacy-50-favourite-routers` | archive | **held** | 0.998 | · | 0.036 | 1.4x bytes_on_air | 1 |
| `batumi-legacy-50-congestion-40` | archive | **held** | 0.998 | · | 0.035 | 1.4x bytes_on_air | 1 |
| `batumi-legacy-50-hop-scaling-40` | archive | **held** | 0.998 | · | 0.035 | 1.4x bytes_on_air | 1 |
| `batumi-legacy-50-none` | archive | **held** | 0.998 | · | 0.035 | 1.4x bytes_on_air | 1 |
| `batumi-legacy-50-coding-rate-ladder` | archive | **held** | 0.998 | · | 0.036 | 1.3x bytes_on_air | 1 |
| `batumi-legacy-50-hop-scaling-60` | archive | **held** | 0.997 | · | 0.045 | 1.3x bytes_on_air | 1 |
| `batumi-legacy-50-hop-limit-15` | archive | **held** | 0.995 | · | 0.048 | 1.3x bytes_on_air | 1 |
| `batumi-legacy-50-hop-limit-7` | archive | **held** | 0.995 | · | 0.048 | 1.3x bytes_on_air | 1 |
| `batumi-legacy-50-congestion-60` | archive | **held** | 0.991 | · | 0.080 | 1.3x bytes_on_air | 1 |
| `batumi-short-fast-extra-repeats` | archive | **held** | 0.980 | · | 0.008 | 1.1x bytes_on_air | 1 |
| `batumi-short-fast-hop-limit-15` | archive | **held** | 0.980 | · | 0.004 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-hop-limit-7` | archive | **held** | 0.980 | · | 0.004 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-congestion-60` | archive | **held** | 0.979 | · | 0.008 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-favourite-routers` | archive | **held** | 0.979 | · | 0.006 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-coding-rate-ladder` | archive | **held** | 0.978 | · | 0.006 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-m4-early-flood` | archive | **held** | 0.977 | · | 0.004 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-congestion-40` | archive | **held** | 0.977 | · | 0.008 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-hop-scaling-40` | archive | **held** | 0.977 | · | 0.008 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-none` | archive | **held** | 0.977 | · | 0.008 | 1.2x bytes_on_air | 1 |
| `batumi-short-fast-congestion-80` | archive | **held** | 0.976 | · | 0.007 | 1.1x bytes_on_air | 1 |
| `batumi-short-fast-hop-scaling-60` | archive | **held** | 0.972 | · | 0.007 | 1.1x bytes_on_air | 1 |
| `batumi-short-fast-hop-scaling-80` | archive | **held** | 0.971 | · | 0.005 | 1.1x bytes_on_air | 1 |
| `BL-control` | protocol | **held** | 0.943 | 0.054 | 0.006 | 1.1x bytes_on_air | 4 |
| `PR-protocol` | protocol | **held** | 0.943 | 0.050 | 0.014 | 1.2x bytes_on_air | 4 |
| `batumi-legacy-50-congestion-80` | archive | **held** | 0.836 | · | 0.137 | 1.1x bytes_on_air | 1 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.757 | 0.020 | 0.631 | 88x sr_airtime | 4 |
| `RF-preset-turbo` | preset | **text** | 0.751 | 0.088 | 0.735 | 5.8x sr_bytes | 4 |
| `MS-siting` | siting-mix | **text** | 0.747 | 0.243 | 0.748 | 1.9x sr_bytes | 4 |
| `RF-txpower` | tx-power | **text** | 0.736 | 0.086 | 0.721 | 5.3x sr_airtime | 4 |
| `AD-siting` | siting-mix | **text** | 0.703 | 0.099 | 0.693 | 11x sr_bytes | 4 |
| `MS-stretch` | stretch | **text** | 0.698 | 0.072 | 0.684 | 3.3x sr_airtime | 4 |
| `RF-bw500` | preset | **text** | 0.585 | 0.085 | 0.577 | 3.6x sr_bytes | 4 |
| `RF-preset` | preset | **text** | 0.568 | 0.048 | 0.552 | 2.3x sr_airtime | 4 |
| `RF-eu-presets` | preset | **text** | 0.566 | 0.047 | 0.552 | 2.3x sr_airtime | 4 |
| `MS-hopscale` | nodes | **text** | 0.538 | 0.099 | 0.525 | 10x sr_bytes | 4 |
| `MS-topology` | topology | **text** | 0.411 | 0.078 | 0.425 | 3.2x sr_bytes | 4 |
| `MS-oversubscribed` | nodes | **text** | 0.408 | 0.095 | 0.399 | 5.1x sr_bytes | 4 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.350 | 0.019 | 0.357 | 16x sr_airtime | 4 |
| `RF-stretch-duct` | duct-per-hour | **held** | 0.343 | 0.096 | 0.370 | 2.7x sr_bytes | 4 |
| `DG-outage` | burst-loss | **text** | 0.323 | 0.021 | 0.331 | 2x sr_bytes | 4 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.318 | 0.030 | 0.319 | 11x sr_airtime | 4 |
| `MS-density` | nodes | **text** | 0.309 | 0.075 | 0.322 | 5.6x sr_airtime | 4 |
| `DG-burst` | burst-loss | **text** | 0.300 | 0.006 | 0.319 | 2.1x sr_bytes | 4 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.255 | 0.113 | 0.182 | 6.1x sr_airtime | 4 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.219 | 0.024 | 0.227 | 4.4x sr_airtime | 4 |
| `RT-hoplimit` | hop-limit | **text** | 0.215 | 0.076 | 0.248 | 1.8x sr_bytes | 4 |
| `batumi-x4-SHORT_FAST` | placement | **held** | 0.215 | · | 0.001 | 1.1x bytes_on_air | 1 |
| `batumi-x4-LONG_FAST` | placement | **held** | 0.209 | · | 0.021 | 1.2x bytes_on_air | 1 |
| `RT-hopspread` | hop-limit | **text** | 0.192 | 0.059 | 0.219 | 1.7x sr_bytes | 4 |
| `MS-size` | nodes | **text** | 0.185 | 0.010 | 0.175 | 4.5x sr_airtime | 4 |
| `batumi-x4-LITE_FAST` | placement | **held** | 0.183 | · | 0.011 | 1.1x bytes_on_air | 1 |
| `SF-place-flat` | place | **held** | 0.183 | 0.183 | 0.010 | 2.4x sr_bytes | 4 |
| `SF-place-spread` | place | **held** | 0.183 | 0.183 | 0.010 | 2.4x sr_bytes | 4 |
| `RF-noise` | noise-profile | **held** | 0.173 | 0.016 | 0.159 | 1.3x sr_bytes | 4 |
| `RT-spread` | hop-spread | **text** | 0.146 | 0.035 | 0.167 | 1.6x sr_bytes | 4 |
| `AD-flooding` | role-mix | **text** | 0.126 | 0.061 | 0.136 | 2.5x bytes_on_air | 4 |
| `AD-nomute` | role-mix | **text** | 0.126 | 0.061 | 0.136 | 2.5x bytes_on_air | 4 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.121 | 0.090 | 0.133 | 3x sr_bytes | 4 |
| `DB-hotstore` | max-num-nodes | **text** | 0.115 | 0.027 | 0.115 | 2.6x sr_airtime | 4 |
| `batumi-x1-SHORT_FAST` | placement | **held** | 0.114 | · | 0.004 | 1.1x bytes_on_air | 1 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.106 | 0.074 | 0.116 | 1.5x bytes_on_air | 4 |
| `SC-signing` | signature-policy | **held** | 0.106 | 0.019 | 0.102 | 1.3x sr_airtime | 4 |
| `RF-duct` | duct-per-hour | **text** | 0.100 | 0.074 | 0.106 | 1.4x bytes_on_air | 4 |
| `DG-loss` | extra-loss | **held** | 0.100 | 0.016 | 0.138 | 1.3x sr_bytes | 4 |
| `DB-platform` | platform-mix | **held** | 0.099 | 0.024 | 0.116 | 3x sr_airtime | 4 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.095 | 0.033 | 0.005 | 28x sr_airtime | 4 |
| `LD-interval` | broadcast-interval-s | **text** | 0.090 | 0.024 | 0.102 | 5.1x sr_airtime | 4 |
| `AD-badrouters` | role-placement | **held** | 0.086 | 0.113 | 0.078 | 1.2x sr_bytes | 4 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.068 | 0.013 | 0.067 | 1.3x sr_airtime | 4 |
| `SF-cadence` | trigger | **held** | 0.064 | 0.012 | 0.031 | 13x advert_bytes | 4 |
| `MS-roles-fav` | role-mix | **text** | 0.063 | 0.034 | 0.067 | 1.1x sr_airtime | 4 |
| `MS-roles` | role-mix | **text** | 0.062 | 0.037 | 0.065 | 1.2x bytes_on_air | 4 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.056 | 0.031 | 0.063 | 2.2x bytes_on_air | 4 |
| `FW-mixed` | legacy-fraction | **text** | 0.051 | 0.030 | 0.060 | 2.1x bytes_on_air | 4 |
| `batumi-x1-LITE_FAST` | placement | **held** | 0.050 | · | 0.007 | 1.1x bytes_on_air | 1 |
| `SF-capacity-window` | capacity | **held** | 0.047 | 0.039 | 0.009 | 2.3x advert_bytes | 4 |
| `FW-signing-cost` | profile-flag | **text** | 0.040 | 0.020 | 0.045 | 3.4x bytes_on_air | 4 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.039 | 0.009 | 0.047 | 1.6x sr_airtime | 4 |
| `FW-versions` | profile | **held** | 0.035 | 0.031 | 0.067 | 3.2x bytes_on_air | 4 |
| `TH-congestion-input` | congestion-input | **held** | 0.035 | 0.009 | 0.030 | 1.4x sr_airtime | 4 |
| `FW-firmware` | profile | **held** | 0.029 | 0.029 | 0.054 | 3.1x bytes_on_air | 4 |
| `SF-catchup` | catch-up-hours | **held** | 0.028 | 0.020 | 0.032 | 9.4x advert_bytes | 4 |
| `SF-hops-spread` | hops-apart | **text** | 0.023 | 0.011 | 0.011 | 2.6x sr_bytes | 4 |
| `MS-router-late` | router-late-fraction | **held** | 0.023 | 0.016 | 0.022 | 1.3x bytes_on_air | 4 |
| `SF-hops-flat` | hops-apart | **text** | 0.023 | 0.011 | 0.010 | 2.6x sr_bytes | 4 |
| `RT-hopassign` | hop-assign | **text** | 0.022 | 0.020 | 0.024 | 1x sr_airtime | 4 |
| `SF-capacity` | capacity | **held** | 0.021 | 0.011 | 0.011 | 5.4x advert_bytes | 4 |
| `SF-capacity-local` | capacity | **held** | 0.021 | 0.011 | 0.011 | 5.4x advert_bytes | 4 |
| `batumi-x1-LONG_FAST` | placement | **held** | 0.021 | · | 0.010 | 1.2x bytes_on_air | 1 |
| `SF-servers-allrouters` | servers | **held** | 0.019 | 0.033 | 0.003 | 2.6x sr_bytes | 4 |
| `SF-servers-flat` | servers | **text** | 0.018 | 0.012 | 0.013 | 7x sr_bytes | 4 |
| `SF-servers-spread` | servers | **text** | 0.018 | 0.012 | 0.013 | 7x sr_bytes | 4 |
| `RT-favourites` | favourite-routers | **text** | 0.017 | 0.014 | 0.017 | 1.1x sr_bytes | 4 |
| `LD-diurnal` | diurnal | **text** | 0.016 | 0.009 | 0.017 | 1.3x sr_bytes | 4 |
| `SF-sr-retries` | sr-retries | **held** | 0.016 | 0.019 | 0.012 | 1.2x sr_bytes | 4 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.016 | 0.010 | 0.013 | 5.4x advert_bytes | 4 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.013 | 0.011 | 0.008 | 1.1x sr_airtime | 4 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.013 | 0.006 | 0.010 | 1x sr_airtime | 4 |
| `SF-provide-transport` | provide-transport | **held** | 0.012 | 0.013 | 0.009 | 2.5x sr_airtime | 4 |
| `DM-mode` | dm-mode | **text** | 0.012 | 0.006 | 0.012 | 1.2x sr_airtime | 4 |
| `SF-width` | short-id-bits | **held** | 0.011 | 0.003 | 0.010 | 3.1x advert_bytes | 4 |
| `PR-repeats` | extra-repeats | **text** | 0.011 | 0.010 | 0.011 | 1.1x sr_bytes | 4 |
| `AD-worst` | role-placement | **held** | 0.008 | 0.007 | 0.027 | 1.1x sr_airtime | 4 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.008 | 0.002 | 0.009 | 1.2x sr_airtime | 4 |
| `PR-crladder` | coding-rate-ladder | **held** | 0.007 | 0.003 | 0.007 | 1.1x sr_bytes | 4 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.007 | 0.002 | 0.008 | 1x sr_bytes | 4 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.007 | 0.002 | 0.008 | 1x sr_bytes | 4 |
| `SF-resolve` | resolve | **held** | 0.007 | 0.006 | 0.005 | 5.8x advert_bytes | 4 |
| `SF-bucket-mode` | bucket-mode | **text** | 0.006 | 0.002 | 0.008 | 3.2x advert_bytes | 4 |
| `SF-replay-order` | replay-ordering | **text** | 0.006 | 0.003 | 0.005 | 1x sr_airtime | 4 |
| `SF-window-size` | window-size | **text** | 0.006 | 0.004 | 0.010 | 5.9x advert_bytes | 4 |
| `SF-advert-transport` | advert-transport | **held** | 0.005 | 0.005 | 0.005 | 3.1x sr_airtime | 4 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.004 | 0.002 | 0.005 | 1.1x bytes_on_air | 4 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.002 | 0.001 | 0.003 | 1x sr_bytes | 4 |
| `DB-warm` | warm-num-nodes | **held** | 0.000 | 0.000 | 0.000 | · | 4 |
| `SF-signed` | signed | **held** | 0.000 | 0.000 | 0.000 | 1.4x advert_bytes | 4 |

## Runs

| run | ground | seed base | blocks | missing | warnings |
| --- | --- | --- | --: | --: | --: |
| [`matrix-2026-08-29-1024`](runs/matrix-2026-08-29-1024/trend.md) | batumi | `None` | 2 | 0 | 145 |
| [`matrix-2026-08-28-1538`](runs/matrix-2026-08-28-1538/trend.md) | batumi | `None` | 2 | 0 | 161 |
| [`matrix-2026-08-27-1436`](runs/matrix-2026-08-27-1436/trend.md) | batumi | `None` | 2 | 0 | 148 |
| [`design-2026-08-28-7079084`](runs/design-2026-08-28-7079084/trend.md) | batumi | `7079084` | 13 | 0 | 652 |
| [`design-2026-08-27-3750778`](runs/design-2026-08-27-3750778/trend.md) | batumi | `3750778` | 13 | 0 | 637 |
| [`blocks-2026-08-30-4551590`](runs/blocks-2026-08-30-4551590/trend.md) | coastal | `4551590` | 87 | 0 | 117 |
| [`blocks-2026-08-29-3120871`](runs/blocks-2026-08-29-3120871/trend.md) | alpine | `3120871` | 87 | 0 | 89 |
| [`blocks-2026-08-28-4161552`](runs/blocks-2026-08-28-4161552/trend.md) | ridge | `4161552` | 87 | 0 | 83 |
| [`blocks-2026-08-27-3444599`](runs/blocks-2026-08-27-3444599/trend.md) | flat | `3444599` | 87 | 0 | 109 |
