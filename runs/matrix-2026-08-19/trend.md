# Sweep matrix-2026-08-19

- **transport** `7b53cc8`
- **ground** batumi
- **seed base** drawn per block · seeds 7
- **blocks** 1 run
- **compute** 1.8 h of simulator time across every cell
- **generated** 2026-08-19T23:40:19+00:00

## Gates - held

- OK `silent_losses` and the at-rest audit are zero in every cell
- OK no node reports channel utilisation above 100%
- OK every run that asked for ground recorded some

<details><summary>15 warnings</summary>

- batumi-x1-SHORT_FAST: placement=baseline: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget
- batumi-x1-SHORT_FAST: placement=random-any x2: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget
- batumi-x1-SHORT_FAST: placement=random-any x4: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget
- batumi-x1-SHORT_FAST: placement=random-any x8: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget
- batumi-x1-SHORT_FAST: placement=random-any x8: decode_failures 5
- batumi-x1-SHORT_FAST: placement=beside-router x2: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget
- batumi-x1-SHORT_FAST: placement=beside-router x4: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget
- batumi-x1-SHORT_FAST: placement=beside-router x8: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget
- batumi-x1-SHORT_FAST: placement=beside-router x8: 8 archives requested, 4 placed - group on the placed count
- batumi-x1-SHORT_FAST: placement=routers x2: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget
- batumi-x1-SHORT_FAST: placement=routers x4: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget
- batumi-x1-SHORT_FAST: placement=routers x4: decode_failures 140
- batumi-x1-SHORT_FAST: placement=routers x8: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget
- batumi-x1-SHORT_FAST: placement=routers x8: 8 archives requested, 4 placed - group on the placed count
- batumi-x1-SHORT_FAST: placement=routers x8: decode_failures 140

</details>

## What moved a delivery measure

Ranked by how far the arm moves whichever success it moves most. The four measures have four denominators and are **not comparable to each other** (README §7.2) - `moved` names which one this block travels in. `text` is the broadcast reach in the same cells, so an arm buying its measure while `text` falls is paying in the currency the mesh exists to spend.

| block | arm | moved | low → high | spread | text | price | dir | cells |
| --- | --- | --- | --- | --: | --- | --- | :-: | --: |
| `batumi-x1-SHORT_FAST` | placement | **held** | 0.766 → 0.952 | 0.186 | 0.774 → 0.877 | 1.1x bytes_on_air | up | 10 |

## Every block

### `batumi-x1-SHORT_FAST` - placement  `--preset SHORT_FAST --mirror 1`

*the 92-node Batumi snapshot on its own ground, on SHORT_FAST, the fast end of what deployed meshes run: least airtime per packet and the least range per hop, so the mesh is quiet but sparser. Crossed against the archive off and at every placement and count, so the capping of the role-bounded placements is visible rather than hidden.*

| value | text | DM | admin | held | union | worst node | demand | chutil p90/max | airutil max | placed |
| --- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| baseline | 0.774 | 0.827 | 0.761 | - | - | 0.176 | 0.35x | 7.7/16.3% | 2.0% | - |
| random-any x2 | 0.784 | 0.827 | 0.742 | 0.766 | 0.767 | 0.178 | 0.35x | 7.7/16.4% | 2.0% | 2 |
| random-any x4 | 0.838 | 0.831 | 0.721 | 0.933 | 0.934 | 0.230 | 0.36x | 8.0/16.8% | 2.1% | 4 |
| random-any x8 | 0.877 | 0.824 | 0.732 | 0.942 | 0.942 | 0.208 | 0.37x | 8.3/17.1% | 2.1% | 8 |
| beside-router x2 | 0.779 | 0.833 | 0.744 | 0.942 | 0.942 | 0.199 | 0.35x | 7.8/16.3% | 2.0% | 2 |
| beside-router x4 | 0.817 | 0.832 | 0.713 | 0.952 | 0.952 | 0.220 | 0.36x | 8.0/16.7% | 2.1% | 4 |
| beside-router x8 | 0.817 | 0.832 | 0.713 | 0.952 | 0.952 | 0.220 | 0.36x | 8.0/16.7% | 2.1% | 4 |
| routers x2 | 0.775 | 0.827 | 0.728 | 0.936 | 0.936 | 0.176 | 0.35x | 7.7/16.2% | 2.0% | 2 |
| routers x4 | 0.843 | 0.828 | 0.739 | 0.916 | 0.942 | 0.228 | 0.36x | 8.0/16.6% | 2.1% | 4 |
| routers x8 | 0.843 | 0.828 | 0.739 | 0.916 | 0.942 | 0.228 | 0.36x | 8.0/16.6% | 2.1% | 4 |

> placement=baseline: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget

> placement=random-any x2: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget

> placement=random-any x4: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget

> placement=random-any x8: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget

> placement=random-any x8: decode_failures 5

> placement=beside-router x2: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget

> placement=beside-router x4: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget

> placement=beside-router x8: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget

> placement=beside-router x8: 8 archives requested, 4 placed - group on the placed count

> placement=routers x2: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget

> placement=routers x4: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget

> placement=routers x4: decode_failures 140

> placement=routers x8: 15 pair(s) beyond the fit's 23.2 km envelope - those fell back to the raw budget

> placement=routers x8: 8 archives requested, 4 placed - group on the placed count

> placement=routers x8: decode_failures 140

