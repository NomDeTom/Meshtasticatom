# Sweep design-2026-08-19-1524961

- **transport** `7b53cc8`
- **ground** batumi
- **seed base** 1524961 · seeds 1524961
- **blocks** 1 run
- **compute** 2.4 h of simulator time across every cell
- **generated** 2026-08-20T00:11:04+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>21 warnings</summary>

- batumi-none: archive=off: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget
- batumi-none: archive=random-any x2: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget
- batumi-none: archive=random-any x3: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget
- batumi-none: archive=random-any x3: misdecodes 2
- batumi-none: archive=random-any x3: decode_failures 10
- batumi-none: archive=random-any x6: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget
- batumi-none: archive=random-any x6: queue drops 13.7% of transmissions - airtime here is measured through a cap
- batumi-none: archive=random-any x6: decode_failures 190
- batumi-none: archive=spread x2: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget
- batumi-none: archive=spread x2: decode_failures 4
- batumi-none: archive=spread x3: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget
- batumi-none: archive=spread x3: decode_failures 13
- batumi-none: archive=spread x6: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget
- batumi-none: archive=spread x6: decode_failures 172
- batumi-none: archive=beside-router x2: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget
- batumi-none: archive=beside-router x2: decode_failures 17
- batumi-none: archive=beside-router x3: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget
- batumi-none: archive=beside-router x3: decode_failures 52
- batumi-none: archive=beside-router x6: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget
- batumi-none: archive=beside-router x6: 6 archives requested, 4 placed - group on the placed count
- batumi-none: archive=beside-router x6: decode_failures 15

</details>

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.2) - `moved` names which one this block travels in. `text` is the broadcast reach in the same cells, so an arm buying its measure while `text` falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `batumi-none` | archive | **held** | 0 → 0.853 | 0.853 | 0.620 → 0.808 | 1.2x bytes_on_air | up | 10 |

## Every block

### `batumi-none` - archive  `--scenario batumi`

*the 92-node Batumi snapshot on its own ground, at the shipped defaults; nothing changed - the mesh as the firmware ships it. Crossed against the archive off and at every placement and count.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| off | 0.808 | 0.879 | 0.810 | 0 | 0.000 | 0.353 | 1.31x | 58.3/61.0% | 9.3% | 3 |
| random-any x2 | 0.794 | 0.865 | 0.857 | 0.850 | 0.850 | 0.346 | 1.31x | 57.7/60.5% | 9.3% | 2 |
| random-any x3 | 0.723 | 0.876 | 0.747 | 0.812 | 0.820 | 0.277 | 1.43x | 62.3/64.6% | 9.8% | 3 |
| random-any x6 | 0.620 | 0.810 | 0.688 | 0.644 | 0.757 | 0.162 | 1.61x | 67.7/69.5% | 10.9% | 6 |
| spread x2 | 0.794 | 0.879 | 0.793 | 0.394 | 0.587 | 0.348 | 1.33x | 58.6/61.4% | 9.4% | 2 |
| spread x3 | 0.799 | 0.887 | 0.843 | 0.367 | 0.630 | 0.340 | 1.32x | 58.0/60.9% | 9.3% | 3 |
| spread x6 | 0.773 | 0.845 | 0.803 | 0.576 | 0.870 | 0.252 | 1.48x | 63.6/66.3% | 10.5% | 6 |
| beside-router x2 | 0.795 | 0.872 | 0.824 | 0.844 | 0.858 | 0.340 | 1.35x | 59.3/62.1% | 9.5% | 2 |
| beside-router x3 | 0.770 | 0.867 | 0.789 | 0.853 | 0.889 | 0.312 | 1.42x | 62.3/64.8% | 9.9% | 3 |
| beside-router x6 | 0.759 | 0.856 | 0.772 | 0.851 | 0.886 | 0.301 | 1.44x | 63.1/65.5% | 10.1% | 4 |

> archive=off: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget

> archive=random-any x2: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget

> archive=random-any x3: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget

> archive=random-any x3: misdecodes 2

> archive=random-any x3: decode_failures 10

> archive=random-any x6: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget

> archive=random-any x6: queue drops 13.7% of transmissions - airtime here is measured through a cap

> archive=random-any x6: decode_failures 190

> archive=spread x2: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget

> archive=spread x2: decode_failures 4

> archive=spread x3: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget

> archive=spread x3: decode_failures 13

> archive=spread x6: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget

> archive=spread x6: decode_failures 172

> archive=beside-router x2: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget

> archive=beside-router x2: decode_failures 17

> archive=beside-router x3: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget

> archive=beside-router x3: decode_failures 52

> archive=beside-router x6: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget

> archive=beside-router x6: 6 archives requested, 4 placed - group on the placed count

> archive=beside-router x6: decode_failures 15

