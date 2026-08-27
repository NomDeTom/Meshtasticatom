# SF++ sweep explorer

1 scheduled run(s) rolled up, 87 block(s). Open `index.html` for the filterable page; this file is the same data in a diff-readable form.

- **latest** `blocks-2026-08-27-3444599` on flat ground, seed base `3444599`
- **transport** `4195f52`
- **sim version** `1.6.1`, excluding 24 superseded run(s) from every metric below

## What moves a delivery measure

| block | arm | measure | spread | run-to-run sd | text spread | price | runs |
| --- | --- | --- | --: | --: | --: | --- | --: |
| `BL-control` | protocol | **held** | 0.933 | · | 0.002 | 1.1x bytes_on_air | 1 |
| `PR-protocol` | protocol | **held** | 0.923 | · | 0.007 | 1.2x bytes_on_air | 1 |
| `MS-siting` | siting-mix | **text** | 0.872 | · | 0.872 | 4x advert_bytes | 1 |
| `AD-siting` | siting-mix | **held** | 0.781 | · | 0.628 | 8x advert_bytes | 1 |
| `RF-pulse` | noise-pulse-interval-ms | **held** | 0.763 | · | 0.555 | 1.6e+02x sr_airtime | 1 |
| `RF-txpower` | tx-power | **held** | 0.690 | · | 0.623 | 7x sr_bytes | 1 |
| `MS-hopscale` | nodes | **held** | 0.686 | · | 0.504 | 7.1x bytes_on_air | 1 |
| `RF-preset-turbo` | preset | **held** | 0.684 | · | 0.631 | 8x sr_bytes | 1 |
| `MS-stretch` | stretch | **held** | 0.634 | · | 0.595 | 5x sr_airtime | 1 |
| `MS-oversubscribed` | nodes | **held** | 0.612 | · | 0.420 | 3.9x bytes_on_air | 1 |
| `RF-eu-presets` | preset | **held** | 0.573 | · | 0.506 | 5.5x sr_bytes | 1 |
| `RF-preset` | preset | **held** | 0.573 | · | 0.506 | 7.9x sr_bytes | 1 |
| `RF-bw500` | preset | **text** | 0.549 | · | 0.536 | 8x sr_bytes | 1 |
| `RF-stretch-duct` | duct-per-hour | **text** | 0.428 | · | 0.426 | 3.4x sr_airtime | 1 |
| `MS-topology` | topology | **text** | 0.419 | · | 0.422 | 2.6x sr_bytes | 1 |
| `MS-density` | nodes | **text** | 0.368 | · | 0.386 | 4.5x advert_bytes | 1 |
| `SF-place-flat` | place | **held** | 0.361 | · | 0.014 | 3.1x sr_bytes | 1 |
| `SF-place-spread` | place | **held** | 0.361 | · | 0.014 | 3.1x sr_bytes | 1 |
| `DG-outage` | burst-loss | **held** | 0.350 | · | 0.326 | 1.6x sr_airtime | 1 |
| `LD-chatty` | broadcast-interval-s | **held** | 0.346 | · | 0.313 | 9.6x sr_airtime | 1 |
| `LD-chatty-hops` | broadcast-interval-s | **text** | 0.330 | · | 0.329 | 7.9x sr_airtime | 1 |
| `DG-burst` | burst-loss | **text** | 0.301 | · | 0.303 | 1.6x sr_bytes | 1 |
| `RT-hoplimit` | hop-limit | **text** | 0.292 | · | 0.319 | 2.2x sr_bytes | 1 |
| `RT-hopspread` | hop-limit | **text** | 0.248 | · | 0.263 | 1.7x sr_bytes | 1 |
| `AD-flooding` | role-mix | **text** | 0.213 | · | 0.238 | 2.4x bytes_on_air | 1 |
| `AD-nomute` | role-mix | **text** | 0.213 | · | 0.238 | 2.4x bytes_on_air | 1 |
| `AD-amplify-worst` | amplify-worst | **held** | 0.201 | · | 0.209 | 1.6x sr_bytes | 1 |
| `AD-amplifiers` | amplifier-mix | **text** | 0.199 | · | 0.234 | 2.5x sr_bytes | 1 |
| `MS-size` | nodes | **text** | 0.199 | · | 0.170 | 6x sr_bytes | 1 |
| `TH-congestion` | no-congestion-scaling | **text** | 0.187 | · | 0.199 | 3.4x sr_airtime | 1 |
| `RF-noise` | noise-profile | **held** | 0.172 | · | 0.154 | 1.6x sr_bytes | 1 |
| `RF-duct` | duct-per-hour | **text** | 0.168 | · | 0.183 | 1.6x sr_bytes | 1 |
| `DG-loss` | extra-loss | **text** | 0.159 | · | 0.157 | 1.4x sr_bytes | 1 |
| `SF-hops-spread` | hops-apart | **held** | 0.158 | · | 0.014 | 3.5x sr_bytes | 1 |
| `RT-spread` | hop-spread | **text** | 0.156 | · | 0.156 | 1.2x sr_bytes | 1 |
| `DB-hotstore` | max-num-nodes | **text** | 0.138 | · | 0.124 | 2.2x sr_airtime | 1 |
| `DB-platform` | platform-mix | **text** | 0.137 | · | 0.127 | 2.2x sr_airtime | 1 |
| `FW-versions` | profile | **text** | 0.136 | · | 0.161 | 3x bytes_on_air | 1 |
| `SF-hops-flat` | hops-apart | **held** | 0.134 | · | 0.014 | 3.1x sr_bytes | 1 |
| `RT-rebroadcast` | rebroadcast-mode | **held** | 0.134 | · | 0.008 | 35x sr_airtime | 1 |
| `SC-signing` | signature-policy | **text** | 0.126 | · | 0.089 | 1.3x sr_airtime | 1 |
| `MS-roles-fav` | role-mix | **held** | 0.124 | · | 0.127 | 1.2x advert_bytes | 1 |
| `MS-roles` | role-mix | **held** | 0.120 | · | 0.128 | 1.3x bytes_on_air | 1 |
| `FW-firmware` | profile | **text** | 0.119 | · | 0.140 | 2.9x bytes_on_air | 1 |
| `LD-interval` | broadcast-interval-s | **text** | 0.115 | · | 0.132 | 5.1x sr_airtime | 1 |
| `SF-servers-flat` | servers | **held** | 0.103 | · | 0.013 | 9x sr_bytes | 1 |
| `SF-servers-spread` | servers | **held** | 0.103 | · | 0.013 | 9x sr_bytes | 1 |
| `SF-capacity-window` | capacity | **held** | 0.103 | · | 0.011 | 3.7x sr_bytes | 1 |
| `DB-hotstore-stress` | max-num-nodes | **text** | 0.101 | · | 0.100 | 3.6x sr_airtime | 1 |
| `SF-cadence` | trigger | **held** | 0.080 | · | 0.031 | 14x advert_bytes | 1 |
| `LD-traceroute-small` | traceroute-per-hour | **text** | 0.077 | · | 0.078 | 1.3x sr_bytes | 1 |
| `FW-mixed-26` | legacy-fraction | **text** | 0.067 | · | 0.089 | 2.1x bytes_on_air | 1 |
| `SF-provide-transport` | provide-transport | **text** | 0.062 | · | 0.002 | 4.2x sr_airtime | 1 |
| `FW-signing-cost` | profile-flag | **text** | 0.054 | · | 0.061 | 3.2x bytes_on_air | 1 |
| `FW-mixed` | legacy-fraction | **text** | 0.052 | · | 0.079 | 2x bytes_on_air | 1 |
| `SF-catchup` | catch-up-hours | **held** | 0.051 | · | 0.035 | 8.9x advert_bytes | 1 |
| `LD-traceroute` | traceroute-per-hour | **text** | 0.045 | · | 0.054 | 1.4x sr_airtime | 1 |
| `AD-badrouters` | role-placement | **held** | 0.040 | · | 0.014 | 1.4x sr_bytes | 1 |
| `SF-capacity` | capacity | **held** | 0.037 | · | 0.013 | 5.4x advert_bytes | 1 |
| `SF-capacity-local` | capacity | **held** | 0.037 | · | 0.013 | 5.4x advert_bytes | 1 |
| `MS-router-late` | router-late-fraction | **text** | 0.035 | · | 0.034 | 1.3x bytes_on_air | 1 |
| `DM-mode` | dm-mode | **held** | 0.034 | · | 0.011 | 1.2x sr_bytes | 1 |
| `LD-diurnal` | diurnal | **held** | 0.029 | · | 0.025 | 1.3x sr_bytes | 1 |
| `RT-hopassign` | hop-assign | **text** | 0.028 | · | 0.023 | 1.1x sr_airtime | 1 |
| `PR-dmmode-cr` | dm-mode | **held** | 0.027 | · | 0.017 | 1.1x sr_bytes | 1 |
| `TH-congestion-input` | congestion-input | **text** | 0.027 | · | 0.026 | 2.1x sr_airtime | 1 |
| `PR-repeats` | extra-repeats | **text** | 0.025 | · | 0.026 | 1.1x sr_bytes | 1 |
| `SF-bucket-time` | time-bucket-s | **held** | 0.019 | · | 0.013 | 5.4x advert_bytes | 1 |
| `SF-replay-order` | replay-ordering | **held** | 0.017 | · | 0.004 | 1.1x sr_bytes | 1 |
| `SF-replay-order-broadcast` | replay-ordering | **held** | 0.014 | · | 0.010 | 1.1x sr_bytes | 1 |
| `SF-sr-retries` | sr-retries | **text** | 0.014 | · | 0.016 | 1.2x sr_bytes | 1 |
| `SF-advert-transport` | advert-transport | **text** | 0.013 | · | 0.010 | 2.2x sr_airtime | 1 |
| `AD-worst` | role-placement | **text** | 0.012 | · | 0.016 | 1.1x sr_bytes | 1 |
| `SF-bucket-mode` | bucket-mode | **held** | 0.011 | · | 0.008 | 3.2x advert_bytes | 1 |
| `RT-favourites` | favourite-routers | **text** | 0.010 | · | 0.010 | 1.1x sr_airtime | 1 |
| `SF-width` | short-id-bits | **text** | 0.010 | · | 0.009 | 3.1x advert_bytes | 1 |
| `SF-jitter-global` | advert-jitter-s | **held** | 0.009 | · | 0.010 | 1x sr_bytes | 1 |
| `SF-jitter-local` | advert-jitter-s | **held** | 0.009 | · | 0.010 | 1x sr_bytes | 1 |
| `PR-crladder` | coding-rate-ladder | **text** | 0.009 | · | 0.009 | 1.1x sr_airtime | 1 |
| `RT-adopt` | no-adopt-hop-recommendation | **text** | 0.008 | · | 0.008 | 1.2x sr_airtime | 1 |
| `TH-congestion-mode` | congestion-mode | **text** | 0.007 | · | 0.008 | 1.1x sr_airtime | 1 |
| `PR-repeats-busy` | extra-repeats | **held** | 0.005 | · | 0.003 | 1x sr_bytes | 1 |
| `SF-resolve` | resolve | **text** | 0.004 | · | 0.002 | 5.7x advert_bytes | 1 |
| `SF-window-size` | window-size | **text** | 0.004 | · | 0.012 | 4.8x advert_bytes | 1 |
| `SF-servers-allrouters` | servers | **text** | 0.004 | · | 0.003 | 2.6x sr_bytes | 1 |
| `DB-warm` | warm-num-nodes | **held** | 0.000 | · | 0.000 | · | 1 |
| `SF-signed` | signed | **held** | 0.000 | · | 0.000 | 1.4x advert_bytes | 1 |

## Runs

| run | ground | seed base | blocks | missing | warnings |
| --- | --- | --- | --: | --: | --: |
| [`blocks-2026-08-27-3444599`](runs/blocks-2026-08-27-3444599/trend.md) | flat | `3444599` | 87 | 0 | 109 |
