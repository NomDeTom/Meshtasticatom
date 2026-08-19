# Sweep blocks-2026-08-19-2455835

- **transport** `a803f49`
- **ground** ridge
- **seed base** 2455835 · seeds 2455835
- **blocks** 2 run
- **compute** 0.1 h of simulator time across every cell
- **generated** 2026-08-19T15:23:42+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.2) - `moved` names which one this block travels in. `text` is the broadcast reach in the same cells, so an arm buying its measure while `text` falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text | dir | cells |
| --- | --- | --- | --- | --: | --- | :-: | --: |
| `D-resolve` | resolve | **held** | 0.857 → 0.861 | 0.004 | 0.632 → 0.635 | = | 3 |
| `E-signed` | signed | **text** | 0.632 → 0.632 | 0.000 | 0.632 → 0.632 | = | 2 |

## Every block

### `D-resolve` - resolve  `--scenario ridge`

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| sketch | 0.632 | - | - | 0.857 | 0.861 | 0.000 | 1.81x | 36.0/37.5% | 8.3% | 3 |
| enum | 0.635 | - | - | 0.861 | 0.874 | 0.000 | 1.80x | 35.4/37.3% | 8.5% | 3 |
| hybrid | 0.632 | - | - | 0.857 | 0.861 | 0.000 | 1.81x | 36.0/37.5% | 8.3% | 3 |

### `E-signed` - signed  `--scenario ridge`

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| False | 0.632 | - | - | 0.857 | 0.861 | 0.000 | 1.81x | 36.0/37.5% | 8.3% | 3 |
| True | 0.632 | - | - | 0.857 | 0.861 | 0.000 | 1.81x | 36.0/37.5% | 8.3% | 3 |

