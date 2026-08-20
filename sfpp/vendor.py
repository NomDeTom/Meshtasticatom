"""Where the vendored Meshtasticator tree is, in either layout this transport is used from.

Two layouts exist and both are legitimate. In the firmware repo `sfpp/` and `meshtasticator/` are
siblings under `sim/`, so the vendored tree is a directory beside this one. In the Meshtasticator
repo the vendored tree *is* the repository: `lib/` and `presets/` sit beside `sfpp/` with no
`meshtasticator/` directory in the path at all.

Resolving by looking for `lib/phy.py` rather than by a fixed relative path means one file works
under both, which is what keeps the two copies mergeable. A hard-coded `parents[1] /
"meshtasticator"` would have to be edited on every sync, and an edit on every sync is a conflict on
every sync.
"""

import os
import sys
from pathlib import Path

# Ordered by specificity: a sibling `meshtasticator/` wins over the parent directory, so a checkout
# that somehow has both is read the way the firmware repo means it.
_CANDIDATES = ("meshtasticator", "")


def find_vendor_root():
    """Locate the directory holding the vendored `lib/` package."""
    here = Path(__file__).resolve().parent
    for name in _CANDIDATES:
        candidate = here.parent / name if name else here.parent
        if (candidate / "lib" / "phy.py").is_file():
            return candidate
    raise ImportError(
        f"no vendored Meshtasticator tree beside {here}: looked for lib/phy.py in "
        + ", ".join(
            str(here.parent / n) if n else str(here.parent) for n in _CANDIDATES
        )
    )


VENDOR_ROOT = find_vendor_root()
PRESET_ROOT = VENDOR_ROOT / "presets"

# Map payloads, SRTM tiles and clutter grids, shared with loraMesh.py's own fetches.
# SFPP_SCENARIO_CACHE overrides it, so two CI jobs cannot race to write one mirrored CSV.
CACHE_ROOT = Path(os.environ.get("SFPP_SCENARIO_CACHE", VENDOR_ROOT / "cache"))


def ensure_on_path():
    """Put the vendored tree on `sys.path` so `import lib.phy` resolves. Idempotent."""
    root = str(VENDOR_ROOT)
    if root not in sys.path:
        sys.path.insert(0, root)
    return root
