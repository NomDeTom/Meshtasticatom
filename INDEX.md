# SF++ sweep explorer

5 scheduled run(s) rolled up, 104 block(s). Open `index.html` for the filterable page; this file is the same data in a diff-readable form.

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
| `BL-control` | protocol | **held** | 0.957 | 0.033 | 0.003 | 1.1x bytes_on_air | 2 |
| `PR-protocol` | protocol | **held** | 0.951 | 0.039 | 0.006 | 1.2x bytes_on_air | 2 |
| `MS-siting` | siting-mix | **text** | 0.859 | 0.018 | 0.861 | 4.5x sr_airtime | 2 |
| `batumi-legacy-50-congestion-80` | archive | **held** | 0.836 | · | 0.137 | 1.1x bytes_on_air | 1 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.768 | 0.008 | 0.621 | 1e+02x sr_airtime | 2 |
| `RF-preset-turbo` | preset | **text** | 0.738 | 0.100 | 0.713 | 3.7x advert_bytes | 2 |
| `RF-txpower` | tx-power | **text** | 0.726 | 0.095 | 0.701 | 3.7x advert_bytes | 2 |
| `MS-stretch` | stretch | **text** | 0.688 | 0.081 | 0.666 | 2.9x sr_airtime | 2 |
| `AD-siting` | siting-mix | **text** | 0.681 | 0.063 | 0.668 | 2.9x advert_bytes | 2 |
| `MS-hopscale` | nodes | **held** | 0.640 | 0.065 | 0.542 | 8.9x sr_bytes | 2 |
| `RF-bw500` | preset | **text** | 0.589 | 0.057 | 0.581 | 2.4x advert_bytes | 2 |
| `RF-eu-presets` | preset | **text** | 0.584 | 0.058 | 0.560 | 3.8x sr_airtime | 2 |
| `RF-preset` | preset | **text** | 0.584 | 0.058 | 0.560 | 3.8x sr_airtime | 2 |
| `MS-oversubscribed` | nodes | **held** | 0.576 | 0.050 | 0.418 | 4.4x sr_bytes | 2 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.412 | 0.023 | 0.411 | 2.7x sr_airtime | 2 |
| `MS-topology` | topology | **text** | 0.392 | 0.039 | 0.401 | 2x sr_airtime | 2 |
| `MS-density` | nodes | **text** | 0.371 | 0.004 | 0.385 | 6x advert_bytes | 2 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.344 | 0.020 | 0.353 | 8.1x sr_airtime | 2 |
| `LD-chatty` | broadcast-interval-s | **text** | 0.341 | 0.018 | 0.335 | 9.4x sr_airtime | 2 |
| `DG-outage` | burst-loss | **text** | 0.335 | 0.007 | 0.338 | 2x sr_bytes | 2 |
| `DG-burst` | burst-loss | **text** | 0.305 | 0.005 | 0.316 | 1.9x sr_bytes | 2 |
| `RT-hoplimit` | hop-limit | **text** | 0.247 | 0.064 | 0.289 | 2.6x sr_bytes | 2 |
| `RT-hopspread` | hop-limit | **text** | 0.219 | 0.042 | 0.252 | 2.3x sr_bytes | 2 |
| `batumi-x4-SHORT_FAST` | placement | **held** | 0.215 | · | 0.001 | 1.1x bytes_on_air | 1 |
| `DB-hotstore-stress` | max-num-nodes | **held** | 0.212 | 0.170 | 0.161 | 6x sr_airtime | 2 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.209 | 0.032 | 0.220 | 5.4x sr_airtime | 2 |
| `batumi-x4-LONG_FAST` | placement | **held** | 0.209 | · | 0.021 | 1.2x bytes_on_air | 1 |
| `SF-place-flat` | place | **held** | 0.200 | 0.227 | 0.010 | 3.8x sr_bytes | 2 |
| `SF-place-spread` | place | **held** | 0.200 | 0.227 | 0.010 | 3.8x sr_bytes | 2 |
| `MS-size` | nodes | **text** | 0.188 | 0.015 | 0.170 | 3.6x sr_airtime | 2 |
| `RF-noise` | noise-profile | **held** | 0.172 | 0.000 | 0.159 | 1.3x sr_bytes | 2 |
| `RT-spread` | hop-spread | **text** | 0.163 | 0.010 | 0.187 | 1.9x sr_bytes | 2 |
| `AD-flooding` | role-mix | **text** | 0.161 | 0.074 | 0.179 | 2.3x bytes_on_air | 2 |
| `AD-nomute` | role-mix | **text** | 0.161 | 0.074 | 0.179 | 2.3x bytes_on_air | 2 |
| `DG-loss` | extra-loss | **text** | 0.144 | 0.022 | 0.147 | 1.6x sr_bytes | 2 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.136 | 0.090 | 0.156 | 1.4x sr_bytes | 2 |
| `DB-hotstore` | max-num-nodes | **text** | 0.121 | 0.025 | 0.118 | 2.1x sr_airtime | 2 |
| `AD-amplify-worst` | amplify-worst | **text** | 0.120 | 0.089 | 0.140 | 1.4x bytes_on_air | 2 |
| `DB-platform` | platform-mix | **text** | 0.118 | 0.026 | 0.119 | 2x sr_airtime | 2 |
| `SC-signing` | signature-policy | **text** | 0.116 | 0.014 | 0.091 | 1.2x sr_airtime | 2 |
| `RF-duct` | duct-per-hour | **text** | 0.111 | 0.081 | 0.123 | 1.6x bytes_on_air | 2 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.108 | 0.037 | 0.006 | 29x sr_airtime | 2 |
| `LD-interval` | broadcast-interval-s | **text** | 0.100 | 0.022 | 0.119 | 5.5x sr_airtime | 2 |
| `SF-hops-spread` | hops-apart | **held** | 0.099 | 0.084 | 0.012 | 2x sr_bytes | 2 |
| `SF-hops-flat` | hops-apart | **held** | 0.087 | 0.067 | 0.012 | 1.8x sr_bytes | 2 |
| `LD-traceroute-small` | traceroute-per-hour | **held** | 0.080 | 0.013 | 0.079 | 1.7x sr_airtime | 2 |
| `MS-roles` | role-mix | **text** | 0.079 | 0.053 | 0.085 | 1.2x bytes_on_air | 2 |
| `FW-versions` | profile | **text** | 0.078 | 0.083 | 0.090 | 3.4x bytes_on_air | 2 |
| `MS-roles-fav` | role-mix | **text** | 0.075 | 0.053 | 0.083 | 1.1x sr_bytes | 2 |
| `SF-servers-flat` | servers | **held** | 0.072 | 0.044 | 0.011 | 6x sr_bytes | 2 |
| `SF-servers-spread` | servers | **held** | 0.072 | 0.044 | 0.011 | 6x sr_bytes | 2 |
| `SF-cadence` | trigger | **held** | 0.067 | 0.019 | 0.033 | 14x sr_bytes | 2 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.062 | 0.008 | 0.075 | 2.2x bytes_on_air | 2 |
| `FW-firmware` | profile | **text** | 0.061 | 0.081 | 0.071 | 3.4x bytes_on_air | 2 |
| `SF-capacity-window` | capacity | **held** | 0.059 | 0.063 | 0.009 | 1.7x advert_bytes | 2 |
| `FW-mixed` | legacy-fraction | **text** | 0.052 | 0.000 | 0.068 | 2.1x bytes_on_air | 2 |
| `batumi-x1-LITE_FAST` | placement | **held** | 0.050 | · | 0.007 | 1.1x bytes_on_air | 1 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.047 | 0.003 | 0.058 | 1.5x sr_airtime | 2 |
| `FW-signing-cost` | profile-flag | **text** | 0.042 | 0.016 | 0.050 | 3.3x bytes_on_air | 2 |
| `SF-provide-transport` | provide-transport | **text** | 0.041 | 0.030 | 0.003 | 2.8x sr_airtime | 2 |
| `RT-hopassign` | hop-assign | **text** | 0.038 | 0.014 | 0.041 | 1.3x sr_bytes | 2 |
| `TH-congestion-input` | congestion-input | **held** | 0.033 | 0.013 | 0.029 | 1.4x sr_airtime | 2 |
| `SF-capacity` | capacity | **held** | 0.027 | 0.014 | 0.012 | 5.3x advert_bytes | 2 |
| `SF-capacity-local` | capacity | **held** | 0.027 | 0.014 | 0.012 | 5.3x advert_bytes | 2 |
| `batumi-x1-LONG_FAST` | placement | **held** | 0.021 | · | 0.010 | 1.2x bytes_on_air | 1 |
| `AD-badrouters` | role-placement | **text** | 0.020 | 0.017 | 0.028 | 1.7x sr_bytes | 2 |
| `DM-mode` | dm-mode | **held** | 0.020 | 0.020 | 0.008 | 1.1x sr_airtime | 2 |
| `SF-catchup` | catch-up-hours | **text** | 0.020 | 0.008 | 0.037 | 9.6x advert_bytes | 2 |
| `PR-repeats` | extra-repeats | **held** | 0.020 | 0.007 | 0.015 | 1x sr_airtime | 2 |
| `LD-diurnal` | diurnal | **text** | 0.019 | 0.011 | 0.018 | 1.3x sr_bytes | 2 |
| `MS-router-late` | router-late-fraction | **held** | 0.017 | 0.004 | 0.020 | 1.3x bytes_on_air | 2 |
| `AD-worst` | role-placement | **text** | 0.017 | 0.007 | 0.021 | 1.1x bytes_on_air | 2 |
| `SF-replay-order` | replay-ordering | **held** | 0.013 | 0.006 | 0.004 | 1x sr_bytes | 2 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.012 | 0.001 | 0.008 | 3.2x advert_bytes | 2 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.012 | 0.003 | 0.007 | 1x sr_bytes | 2 |
| `SF-sr-retries` | sr-retries | **text** | 0.012 | 0.003 | 0.014 | 1.2x sr_bytes | 2 |
| `SF-width` | short-id-bits | **held** | 0.010 | 0.005 | 0.009 | 3.1x advert_bytes | 2 |
| `RT-favourites` | favourite-routers | **text** | 0.010 | 0.001 | 0.008 | 1.1x sr_bytes | 2 |
| `SF-bucket-time` | time-bucket-s | **text** | 0.010 | 0.006 | 0.011 | 5.3x advert_bytes | 2 |
| `PR-dmmode-cr` | dm-mode | **text** | 0.009 | 0.010 | 0.009 | 1x sr_bytes | 2 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.008 | 0.001 | 0.008 | 1x sr_airtime | 2 |
| `SF-advert-transport` | advert-transport | **held** | 0.008 | 0.006 | 0.006 | 2.7x sr_airtime | 2 |
| `SF-window-size` | window-size | **text** | 0.008 | 0.005 | 0.013 | 6x advert_bytes | 2 |
| `SF-jitter-global` | advert-jitter-s | **text** | 0.008 | 0.001 | 0.009 | 1.1x sr_bytes | 2 |
| `SF-jitter-local` | advert-jitter-s | **text** | 0.008 | 0.001 | 0.009 | 1.1x sr_bytes | 2 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.007 | 0.002 | 0.007 | 1.2x sr_airtime | 2 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.006 | 0.001 | 0.007 | 1.1x sr_bytes | 2 |
| `SF-resolve` | resolve | **held** | 0.005 | 0.007 | 0.003 | 5.7x advert_bytes | 2 |
| `SF-servers-allrouters` | servers | **text** | 0.004 | 0.000 | 0.003 | 2.2x sr_bytes | 2 |
| `PR-repeats-busy` | extra-repeats | **text** | 0.003 | 0.001 | 0.004 | 1x sr_bytes | 2 |
| `DB-warm` | warm-num-nodes | **held** | 0.000 | 0.000 | 0.000 | · | 2 |
| `SF-signed` | signed | **held** | 0.000 | 0.000 | 0.000 | 1.4x advert_bytes | 2 |

## Runs

| run | ground | seed base | blocks | missing | warnings |
| --- | --- | --- | --: | --: | --: |
| [`matrix-2026-08-28-1538`](runs/matrix-2026-08-28-1538/trend.md) | batumi | `None` | 2 | 0 | 161 |
| [`matrix-2026-08-27-1436`](runs/matrix-2026-08-27-1436/trend.md) | batumi | `None` | 2 | 0 | 148 |
| [`design-2026-08-27-3750778`](runs/design-2026-08-27-3750778/trend.md) | batumi | `3750778` | 13 | 0 | 637 |
| [`blocks-2026-08-28-4161552`](runs/blocks-2026-08-28-4161552/trend.md) | ridge | `4161552` | 87 | 0 | 83 |
| [`blocks-2026-08-27-3444599`](runs/blocks-2026-08-27-3444599/trend.md) | flat | `3444599` | 87 | 0 | 109 |
