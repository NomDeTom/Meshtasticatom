# Sweep blocks-2026-08-19-9293155

- **transport** `697b138`
- **ground** rolling
- **seed base** 9293155 · seeds 9293155
- **blocks** 5 run
- **compute** 0.7 h of simulator time across every cell
- **generated** 2026-08-19T18:07:37+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>7 warnings</summary>

- F-loss: extra-loss=0.2: decode_failures 1
- F-loss: extra-loss=0.3: decode_failures 16
- G-servers: servers=2: decode_failures 13
- K-hopspread: hop-limit=3: decode_failures 22
- N-hops: hops-apart=3: decode_failures 5
- N-hops: hops-apart=4: decode_failures 17
- N-hops: hops-apart=5: decode_failures 4

</details>

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.2) - `moved` names which one this block travels in. `text` is the broadcast reach in the same cells, so an arm buying its measure while `text` falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text | dir | cells |
| --- | --- | --- | --- | --: | --- | :-: | --: |
| `Q-topology` | topology | **text** | 0.385 → 0.890 | 0.504 | 0.385 → 0.890 | up | 4 |
| `N-hops` | hops-apart | **held** | 0.579 → 0.872 | 0.293 | 0.630 → 0.653 | down | 5 |
| `K-hopspread` | hop-limit | **text** | 0.437 → 0.689 | 0.252 | 0.437 → 0.689 | up | 3 |
| `F-loss` | extra-loss | **held** | 0.716 → 0.872 | 0.156 | 0.498 → 0.639 | down | 4 |
| `G-servers` | servers | **held** | 0.791 → 0.945 | 0.155 | 0.636 → 0.652 | up | 4 |

## Every block

### `F-loss` - extra-loss  `--scenario rolling`

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 0.0 | 0.639 | - | - | 0.872 | 0.874 | 0.116 | 1.81x | 31.9/37.7% | 8.0% | 3 |
| 0.1 | 0.594 | - | - | 0.833 | 0.837 | 0.094 | 1.88x | 32.4/38.4% | 7.7% | 3 |
| 0.2 | 0.561 | - | - | 0.810 | 0.820 | 0.065 | 1.89x | 32.3/38.9% | 7.3% | 3 |
| 0.3 | 0.498 | - | - | 0.716 | 0.775 | 0.047 | 1.90x | 33.0/38.8% | 6.9% | 3 |

> extra-loss=0.2: decode_failures 1

> extra-loss=0.3: decode_failures 16

### `G-servers` - servers  `--scenario rolling`

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 2 | 0.636 | - | - | 0.791 | 0.812 | 0.128 | 1.77x | 31.0/36.7% | 7.8% | 2 |
| 3 | 0.639 | - | - | 0.872 | 0.874 | 0.116 | 1.81x | 31.9/37.7% | 8.0% | 3 |
| 5 | 0.643 | - | - | 0.898 | 0.901 | 0.115 | 1.83x | 32.2/37.9% | 8.1% | 5 |
| 8 | 0.652 | - | - | 0.945 | 0.948 | 0.119 | 1.91x | 33.7/39.7% | 8.3% | 8 |

> servers=2: decode_failures 13

### `K-hopspread` - hop-limit  `--scenario rolling`

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 3 | 0.437 | - | - | 0.654 | 0.687 | 0.110 | 1.55x | 28.4/34.0% | 7.8% | 3 |
| 5 | 0.604 | - | - | 0.801 | 0.802 | 0.142 | 1.75x | 30.0/36.2% | 7.7% | 3 |
| 7 | 0.689 | - | - | 0.846 | 0.851 | 0.182 | 1.99x | 33.4/38.5% | 8.2% | 3 |

> hop-limit=3: decode_failures 22

### `N-hops` - hops-apart  `--scenario rolling`

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| 1 | 0.640 | - | - | 0.868 | 0.869 | 0.125 | 1.82x | 31.7/37.6% | 7.9% | 3 |
| 2 | 0.639 | - | - | 0.872 | 0.874 | 0.116 | 1.81x | 31.9/37.7% | 8.0% | 3 |
| 3 | 0.648 | - | - | 0.667 | 0.839 | 0.123 | 1.81x | 31.9/37.6% | 8.0% | 3 |
| 4 | 0.630 | - | - | 0.579 | 0.896 | 0.117 | 1.81x | 31.2/37.7% | 7.8% | 3 |
| 5 | 0.653 | - | - | 0.639 | 0.859 | 0.131 | 1.79x | 31.3/36.7% | 7.8% | 3 |

> hops-apart=3: decode_failures 5

> hops-apart=4: decode_failures 17

> hops-apart=5: decode_failures 4

### `Q-topology` - topology  `--scenario rolling`

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| uniform | 0.639 | - | - | 0.872 | 0.874 | 0.116 | 1.81x | 31.9/37.7% | 8.0% | 3 |
| clustered | 0.765 | - | - | 0.925 | 0.925 | 0.351 | 1.64x | 49.6/50.7% | 7.9% | 3 |
| corridor | 0.385 | - | - | 0.569 | 0.575 | 0.177 | 1.68x | 31.9/34.5% | 7.3% | 3 |
| hub | 0.890 | - | - | 0.938 | 0.938 | 0.765 | 1.86x | 55.8/57.1% | 8.5% | 3 |

