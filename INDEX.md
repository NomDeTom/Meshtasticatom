# SF++ sweep explorer

7 scheduled run(s) rolled up, 117 block(s). Open `index.html` for the filterable page; this file is the same data in a diff-readable form.

- **latest** `matrix-2026-08-28-1538` on batumi ground, seed base `None`
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
| `PR-protocol` | protocol | **held** | 0.928 | 0.049 | 0.015 | 1.2x bytes_on_air | 3 |
| `BL-control` | protocol | **held** | 0.928 | 0.055 | 0.005 | 1x bytes_on_air | 3 |
| `MS-siting` | siting-mix | **text** | 0.868 | 0.020 | 0.868 | 8.8x sr_airtime | 3 |
| `batumi-legacy-50-congestion-80` | archive | **held** | 0.836 | · | 0.137 | 1.1x bytes_on_air | 1 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.755 | 0.024 | 0.603 | 2.5e+02x sr_airtime | 3 |
| `RF-preset-turbo` | preset | **held** | 0.743 | 0.079 | 0.700 | 36x sr_bytes | 3 |
| `RF-txpower` | tx-power | **held** | 0.733 | 0.061 | 0.686 | 15x advert_bytes | 3 |
| `AD-siting` | siting-mix | **held** | 0.679 | 0.091 | 0.648 | 6.7x sr_bytes | 3 |
| `MS-stretch` | stretch | **held** | 0.673 | 0.094 | 0.655 | 26x sr_bytes | 3 |
| `RF-eu-presets` | preset | **held** | 0.607 | 0.113 | 0.563 | 5.9x advert_bytes | 3 |
| `RF-preset` | preset | **held** | 0.607 | 0.113 | 0.563 | 5.9x sr_airtime | 3 |
| `MS-hopscale` | nodes | **held** | 0.571 | 0.128 | 0.492 | 9x bytes_on_air | 3 |
| `RF-bw500` | preset | **held** | 0.558 | 0.101 | 0.544 | 6.8x advert_bytes | 3 |
| `MS-oversubscribed` | nodes | **held** | 0.518 | 0.107 | 0.367 | 4.7x bytes_on_air | 3 |
| `MS-topology` | topology | **text** | 0.434 | 0.077 | 0.442 | 2.2x sr_airtime | 3 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.429 | 0.034 | 0.428 | 4x sr_airtime | 3 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.343 | 0.014 | 0.352 | 8.4x sr_airtime | 3 |
| `MS-density` | nodes | **text** | 0.339 | 0.055 | 0.355 | 4.4x advert_bytes | 3 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.335 | 0.020 | 0.322 | 9.2x sr_airtime | 3 |
| `DG-outage` | burst-loss | **text** | 0.321 | 0.025 | 0.327 | 2.1x sr_bytes | 3 |
| `DG-burst` | burst-loss | **text** | 0.302 | 0.006 | 0.317 | 1.9x sr_bytes | 3 |
| `RT-hoplimit` | hop-limit | **text** | 0.249 | 0.045 | 0.285 | 2.1x sr_bytes | 3 |
| `SF-place-flat` | place | **held** | 0.240 | 0.175 | 0.012 | 4.1x sr_bytes | 3 |
| `SF-place-spread` | place | **held** | 0.240 | 0.175 | 0.012 | 4.1x sr_bytes | 3 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.230 | 0.124 | 0.173 | 6.3x sr_airtime | 3 |
| `RT-hopspread` | hop-limit | **text** | 0.219 | 0.030 | 0.249 | 1.8x sr_bytes | 3 |
| `batumi-x4-SHORT_FAST` | placement | **held** | 0.215 | · | 0.001 | 1.1x bytes_on_air | 1 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.211 | 0.023 | 0.219 | 4.5x sr_airtime | 3 |
| `batumi-x4-LONG_FAST` | placement | **held** | 0.209 | · | 0.021 | 1.2x bytes_on_air | 1 |
| `MS-size` | nodes | **text** | 0.186 | 0.011 | 0.171 | 5x sr_bytes | 3 |
| `RF-noise` | noise-profile | **held** | 0.179 | 0.012 | 0.162 | 1.5x sr_bytes | 3 |
| `RT-spread` | hop-spread | **text** | 0.163 | 0.007 | 0.185 | 1.4x sr_bytes | 3 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.155 | 0.071 | 0.169 | 1.2x sr_bytes | 3 |
| `AD-flooding` | role-mix | **text** | 0.144 | 0.060 | 0.155 | 2.4x bytes_on_air | 3 |
| `AD-nomute` | role-mix | **text** | 0.144 | 0.060 | 0.155 | 2.4x bytes_on_air | 3 |
| `DG-loss` | extra-loss | **text** | 0.142 | 0.016 | 0.147 | 1.5x sr_bytes | 3 |
| `SF-hops-spread` | hops-apart | **held** | 0.134 | 0.085 | 0.013 | 3.8x sr_bytes | 3 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.131 | 0.065 | 0.144 | 2.2x sr_bytes | 3 |
| `RF-duct` | duct-per-hour | **text** | 0.126 | 0.063 | 0.134 | 1.4x sr_bytes | 3 |
| `DB-hotstore` | max-num-nodes | **text** | 0.126 | 0.019 | 0.125 | 2x sr_airtime | 3 |
| `DB-platform` | platform-mix | **text** | 0.123 | 0.020 | 0.126 | 2.1x sr_airtime | 3 |
| `SC-signing` | signature-policy | **text** | 0.115 | 0.010 | 0.095 | 1.2x sr_airtime | 3 |
| `AD-badrouters` | role-placement | **held** | 0.109 | 0.127 | 0.100 | 1.6x sr_airtime | 3 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.107 | 0.026 | 0.005 | 26x sr_airtime | 3 |
| `LD-interval` | broadcast-interval-s | **text** | 0.100 | 0.015 | 0.115 | 5x sr_airtime | 3 |
| `SF-hops-flat` | hops-apart | **held** | 0.082 | 0.048 | 0.011 | 3.8x sr_bytes | 3 |
| `FW-versions` | profile | **text** | 0.078 | 0.058 | 0.087 | 3.1x bytes_on_air | 3 |
| `MS-roles-fav` | role-mix | **held** | 0.076 | 0.045 | 0.073 | 1.2x sr_airtime | 3 |
| `SF-servers-flat` | servers | **held** | 0.075 | 0.032 | 0.014 | 11x sr_bytes | 3 |
| `SF-servers-spread` | servers | **held** | 0.075 | 0.032 | 0.014 | 11x sr_bytes | 3 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.071 | 0.015 | 0.070 | 1.4x sr_airtime | 3 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.070 | 0.016 | 0.080 | 2.1x bytes_on_air | 3 |
| `SF-cadence` | trigger | **held** | 0.066 | 0.013 | 0.037 | 16x advert_bytes | 3 |
| `MS-roles` | role-mix | **text** | 0.066 | 0.045 | 0.069 | 1.2x sr_bytes | 3 |
| `FW-mixed` | legacy-fraction | **text** | 0.064 | 0.020 | 0.076 | 2.1x bytes_on_air | 3 |
| `FW-firmware` | profile | **text** | 0.063 | 0.058 | 0.071 | 3x bytes_on_air | 3 |
| `SF-capacity-window` | capacity | **held** | 0.054 | 0.045 | 0.009 | 1.9x sr_bytes | 3 |
| `batumi-x1-LITE_FAST` | placement | **held** | 0.050 | · | 0.007 | 1.1x bytes_on_air | 1 |
| `FW-signing-cost` | profile-flag | **text** | 0.048 | 0.015 | 0.054 | 3.3x bytes_on_air | 3 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.043 | 0.007 | 0.051 | 1.3x sr_airtime | 3 |
| `TH-congestion-input` | congestion-input | **text** | 0.030 | 0.003 | 0.030 | 1.4x sr_airtime | 3 |
| `MS-router-late` | router-late-fraction | **held** | 0.027 | 0.018 | 0.025 | 1.3x bytes_on_air | 3 |
| `RT-hopassign` | hop-assign | **text** | 0.026 | 0.022 | 0.028 | 1.3x sr_bytes | 3 |
| `AD-worst` | role-placement | **text** | 0.026 | 0.017 | 0.031 | 1.1x sr_bytes | 3 |
| `SF-catchup` | catch-up-hours | **text** | 0.025 | 0.011 | 0.039 | 9x advert_bytes | 3 |
| `SF-servers-allrouters` | servers | **held** | 0.024 | 0.038 | 0.003 | 3.8x sr_bytes | 3 |
| `SF-capacity` | capacity | **held** | 0.024 | 0.012 | 0.012 | 5.5x advert_bytes | 3 |
| `SF-capacity-local` | capacity | **held** | 0.024 | 0.012 | 0.012 | 5.5x advert_bytes | 3 |
| `batumi-x1-LONG_FAST` | placement | **held** | 0.021 | · | 0.010 | 1.2x bytes_on_air | 1 |
| `DM-mode` | dm-mode | **held** | 0.020 | 0.014 | 0.012 | 1.2x sr_airtime | 3 |
| `LD-diurnal` | diurnal | **text** | 0.019 | 0.008 | 0.020 | 1.2x sr_airtime | 3 |
| `RT-favourites` | favourite-routers | **text** | 0.019 | 0.016 | 0.019 | 1.2x sr_bytes | 3 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.017 | 0.012 | 0.012 | 5.1x advert_bytes | 3 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.015 | 0.013 | 0.010 | 1.1x sr_bytes | 3 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.015 | 0.005 | 0.012 | 1x sr_airtime | 3 |
| `PR-repeats` | extra-repeats | **text** | 0.014 | 0.010 | 0.014 | 1.1x sr_bytes | 3 |
| `SF-provide-transport` | provide-transport | **held** | 0.013 | 0.015 | 0.010 | 3.5x sr_airtime | 3 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.012 | 0.001 | 0.008 | 3.8x advert_bytes | 3 |
| `SF-sr-retries` | sr-retries | **text** | 0.012 | 0.002 | 0.014 | 1.1x sr_bytes | 3 |
| `SF-replay-order` | replay-ordering | **held** | 0.012 | 0.004 | 0.005 | 1.1x sr_bytes | 3 |
| `SF-width` | short-id-bits | **held** | 0.012 | 0.004 | 0.011 | 3.1x advert_bytes | 3 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.009 | 0.002 | 0.009 | 1.1x sr_airtime | 3 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.008 | 0.001 | 0.009 | 1.1x sr_airtime | 3 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.008 | 0.001 | 0.009 | 1.1x sr_airtime | 3 |
| `SF-advert-transport` | advert-transport | **text** | 0.008 | 0.005 | 0.006 | 2.3x sr_airtime | 3 |
| `SF-resolve` | resolve | **held** | 0.008 | 0.007 | 0.006 | 5.8x advert_bytes | 3 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.008 | 0.002 | 0.009 | 1.2x sr_airtime | 3 |
| `SF-window-size` | window-size | **held** | 0.006 | 0.003 | 0.012 | 5.8x advert_bytes | 3 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.004 | 0.001 | 0.003 | 1x sr_bytes | 3 |
| `TH-congestion-mode` | congestion-mode | **held** | 0.002 | 0.002 | 0.005 | 1.1x sr_airtime | 3 |
| `DB-warm` | warm-num-nodes | **held** | 0.000 | 0.000 | 0.000 | · | 3 |
| `SF-signed` | signed | **held** | 0.000 | 0.000 | 0.000 | 1.4x advert_bytes | 3 |

## Runs

| run | ground | seed base | blocks | missing | warnings |
| --- | --- | --- | --: | --: | --: |
| [`matrix-2026-08-28-1538`](runs/matrix-2026-08-28-1538/trend.md) | batumi | `None` | 2 | 0 | 161 |
| [`matrix-2026-08-27-1436`](runs/matrix-2026-08-27-1436/trend.md) | batumi | `None` | 2 | 0 | 148 |
| [`design-2026-08-28-7079084`](runs/design-2026-08-28-7079084/trend.md) | batumi | `7079084` | 13 | 0 | 652 |
| [`design-2026-08-27-3750778`](runs/design-2026-08-27-3750778/trend.md) | batumi | `3750778` | 13 | 0 | 637 |
| [`blocks-2026-08-29-3120871`](runs/blocks-2026-08-29-3120871/trend.md) | alpine | `3120871` | 87 | 0 | 89 |
| [`blocks-2026-08-28-4161552`](runs/blocks-2026-08-28-4161552/trend.md) | ridge | `4161552` | 87 | 0 | 83 |
| [`blocks-2026-08-27-3444599`](runs/blocks-2026-08-27-3444599/trend.md) | flat | `3444599` | 87 | 0 | 109 |
