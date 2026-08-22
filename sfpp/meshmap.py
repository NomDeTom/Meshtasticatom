"""An SVG map of a run's actual mesh: where the nodes are, what role each has, which hold archives.

Hand-written SVG with no plotting dependency, for the reason `autochart.py` and `diagram.py` give:
matplotlib is the only heavy dependency this tree has, every CI job installs PyYAML and nothing else,
and the sweeps pass `--no-charts` precisely to avoid it. A map that cannot be drawn in CI is a map
nobody sees.

`diagram.py` already draws a mesh, and does not replace this: it builds its own synthetic topology to
check what a placement strategy does to a shape. This draws the mesh a *run* actually had, which needs
four things that one does not - roles, a non-square extent, co-located nodes, and some way to draw
2000+ links without the picture turning into a grey rectangle.

Usage:
    from .meshmap import mesh_svg
    mesh_svg(campaign, "figures/mesh.svg")
"""

import math

from .diagram import BG, INK, LINK, MUTED, SERVER, svg_header

# Roles, as the marks that distinguish them. A role is a *rule about relaying*, so the shapes are
# ordered by how much a node relays: a filled square relays everything, a hollow dot relays nothing.
ROLE_MARKS = {
    "ROUTER": ("square", "#2E5E7E", "relays everything, infrastructure"),
    "ROUTER_LATE": ("square-open", "#4E86A8", "relays late, only when still needed"),
    "CLIENT_BASE": ("diamond", "#7FB0CB", "relays, favoured by routers"),
    "CLIENT": ("circle", "#B5D2E2", "relays"),
    "CLIENT_MUTE": ("circle-open", "#DCE9F1", "never relays"),
}
UNKNOWN_ROLE = ("circle", "#F0F0F0", "role not modelled")
# A link whose margin over sensitivity is under this many dB is one a little fading removes. Same
# threshold `link_quality.fragile` uses, so the map and the report agree on the word.
FRAGILE_DB = 5.0
FRAGILE = "#B4472A"
W, H = 900, 780


def _extent(nodes):
    """The bounding box of where the nodes actually are, not the area they were drawn in.

    Scaling by --area would squeeze a corridor or a real snapshot into a corner of an empty square.
    """
    xs = [n.x for n in nodes]
    ys = [n.y for n in nodes]
    return min(xs), min(ys), max(xs), max(ys)


def _stacks(nodes, tolerance=1.0):
    """{(x, y) rounded: [node index]} - which nodes share a position.

    Batumi is 92 nodes on 55 coordinates, so drawn literally a third of the mesh is invisible.
    """
    groups = {}
    for i, n in enumerate(nodes):
        key = (round(n.x / tolerance), round(n.y / tolerance))
        groups.setdefault(key, []).append(i)
    return groups


def _fan(count, index, radius=7.0):
    """Offset for one node of a co-located stack, on a small circle around the true position.

    A deliberate lie about position, captioned as one: a count badge would hide the roles.
    """
    if count == 1:
        return 0.0, 0.0
    angle = 2 * math.pi * index / count
    spread = radius * (1 + 0.55 * (count > 8))
    return spread * math.cos(angle), spread * math.sin(angle)


def _mark(shape, cx, cy, r, fill, stroke, width=0.9):
    if shape == "square":
        return (
            f'<rect x="{cx - r:.1f}" y="{cy - r:.1f}" width="{2 * r:.1f}" '
            f'height="{2 * r:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'
        )
    if shape == "square-open":
        return (
            f'<rect x="{cx - r:.1f}" y="{cy - r:.1f}" width="{2 * r:.1f}" '
            f'height="{2 * r:.1f}" fill="{BG}" stroke="{fill}" stroke-width="{width + 0.7}"/>'
        )
    if shape == "diamond":
        pts = f"{cx:.1f},{cy - r:.1f} {cx + r:.1f},{cy:.1f} {cx:.1f},{cy + r:.1f} {cx - r:.1f},{cy:.1f}"
        return f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'
    if shape == "circle-open":
        return (
            f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{BG}" '
            f'stroke="{fill}" stroke-width="{width + 0.7}"/>'
        )
    return (
        f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="{width}"/>'
    )


# What a stored map may cost. A 92-node Batumi is 1915 links and 17 kB of JSON; the cap only bites
# on meshes far larger than anything a snapshot holds, and drops are counted rather than hidden.
MAX_STORED_LINKS = 6000
# Positions are stored in decametres from the extent's corner. At 900 px across 20 km one pixel is
# some 25 m, so 10 m is already below the ink; keeping metres would double the payload for nothing.
POSITION_UNIT_M = 10


def mesh_data(campaign, max_links=MAX_STORED_LINKS):
    """One run's mesh as points and links, for a page to draw rather than an image to ship.

    Split in two on purpose. `geometry` is decided by the radio - positions and which pairs close a
    budget - so two cells that differ only in what the nodes *do* share one, and a digest can hold it
    once. `overlay` is per cell: unlocking roles rewrites every mark on the map without moving a
    single link. See `mesh_svg` for the same picture drawn server-side.
    """
    mesh = campaign.mesh
    nodes = mesh.nodes
    x0, y0, x1, y1 = _extent(nodes)
    span_x, span_y = max(x1 - x0, 1.0), max(y1 - y0, 1.0)
    sensitivity = float(campaign.conf.current_preset["sensitivity"])

    pts = []
    for n in nodes:
        pts.append(round((n.x - x0) / POSITION_UNIT_M))
        pts.append(round((n.y - y0) / POSITION_UNIT_M))

    links, total, dropped = [], 0, 0
    for i, peers in enumerate(mesh.neighbours):
        for j in peers:
            if j <= i:
                continue  # each undirected pair once
            total += 1
            if len(links) // 3 >= max_links:
                dropped += 1
                continue
            # The weaker direction, matching the drawn map: a link a reader is told exists has to
            # close in both, and the margin shown is the one that fails first.
            margin = min(mesh.rssi[i][j], mesh.rssi[j][i]) - sensitivity
            # Floored, not rounded, so the stored dB is a lower bound on the real one: a link is
            # never shown stronger than it measured. That also makes the drawn fragile set exact
            # rather than nearly right - `floor(m) < 5` holds precisely when `m < 5`, where rounding
            # promoted every 4.5-to-5 dB link out of the class and lost 70 of Batumi's 415.
            links += [i, j, max(0, min(63, math.floor(margin)))]

    roles = list(ROLE_MARKS)
    role_of = []
    for n in nodes:
        role = getattr(n, "role", None) or "CLIENT"
        role_of.append(roles.index(role) if role in roles else len(roles))
    return {
        "geometry": {
            "n": len(nodes),
            "unit_m": POSITION_UNIT_M,
            "extent_km": [round(span_x / 1000, 2), round(span_y / 1000, 2)],
            "sensitivity": round(sensitivity, 1),
            "preset": campaign.conf.MODEM_PRESET,
            "fragile_db": FRAGILE_DB,
            "pts": pts,
            "links": links,
            "links_total": total,
            "links_dropped": dropped,
        },
        "overlay": {
            # `roles` travels with the overlay that uses it, so a reader of one cell needs nothing
            # else to name a mark. Index len(roles) is meshmap's UNKNOWN_ROLE.
            "roles": roles,
            "role_of": role_of,
            "servers": sorted(getattr(campaign, "servers", {}) or {}),
            "designated": sorted(getattr(campaign, "designated", []) or []),
        },
    }


def mesh_svg(campaign, path, max_links=2500):
    """Draw one run's mesh, returning the counts it drew so a caller can record the claim.

    Two passes - every link faint, the fragile ones over the top - since 2000 equal links are a smear.
    """
    mesh = campaign.mesh
    nodes = mesh.nodes
    x0, y0, x1, y1 = _extent(nodes)
    pad, top, bottom = 54, 74, 96
    span_x, span_y = max(x1 - x0, 1.0), max(y1 - y0, 1.0)
    # One scale for both axes, so the picture is not a stretched version of the geometry.
    scale = min((W - 2 * pad) / span_x, (H - top - bottom) / span_y)
    ox = pad + ((W - 2 * pad) - span_x * scale) / 2
    oy = top + ((H - top - bottom) - span_y * scale) / 2

    def sx(x):
        return ox + (x - x0) * scale

    def sy(y):
        # SVG y grows downward; the mesh's does not.
        return oy + (span_y - (y - y0)) * scale

    servers = set(getattr(campaign, "servers", {}) or {})
    designated = set(getattr(campaign, "designated", []) or [])
    stacks = _stacks(nodes)
    place = {}
    for members in stacks.values():
        for k, i in enumerate(members):
            dx, dy = _fan(len(members), k)
            place[i] = (sx(nodes[i].x) + dx, sy(nodes[i].y) + dy)

    sensitivity = float(campaign.conf.current_preset["sensitivity"])
    drawn, fragile_drawn, skipped = 0, 0, 0
    faint, weak = [], []
    for i, peers in enumerate(mesh.neighbours):
        for j in peers:
            if j <= i:
                continue  # each undirected pair once
            if drawn >= max_links:
                skipped += 1
                continue
            ax, ay = place[i]
            bx, by = place[j]
            margin = min(mesh.rssi[i][j], mesh.rssi[j][i]) - sensitivity
            if margin < FRAGILE_DB:
                weak.append(
                    f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}" '
                    f'stroke="{FRAGILE}" stroke-width="0.8" opacity="0.45"/>'
                )
                fragile_drawn += 1
            else:
                alpha = 0.06 + 0.16 * min(1.0, margin / 25.0)
                faint.append(
                    f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}" '
                    f'stroke="{LINK}" stroke-width="0.7" opacity="{alpha:.2f}"/>'
                )
            drawn += 1

    scenario = (getattr(campaign.opts, "scenario", None) or "flat").strip() or "flat"
    mirror = int(getattr(campaign.opts, "mirror", 1) or 1)
    title = f"{len(nodes)} nodes, {len(servers)} archive(s) - {scenario}" + (
        f" x{mirror}" if mirror > 1 else ""
    )
    parts = [svg_header(W, H, title)]
    parts.append(
        f'<text x="24" y="54" font-size="11.5" fill="{MUTED}">'
        f"{campaign.conf.MODEM_PRESET} &#183; sensitivity {sensitivity:.1f} dBm &#183; "
        f"{span_x / 1000:.1f} x {span_y / 1000:.1f} km &#183; "
        f"a link is drawn where the budget closes; red is under {FRAGILE_DB:.0f} dB of margin</text>"
    )
    parts += faint
    parts += weak

    roles_seen = {}
    for i, node in enumerate(nodes):
        role = getattr(node, "role", None) or "CLIENT"
        shape, colour, _ = ROLE_MARKS.get(role, UNKNOWN_ROLE)
        roles_seen[role] = roles_seen.get(role, 0) + 1
        cx, cy = place[i]
        if i in servers:
            continue
        # A designated-but-archiveless node is the `--protocol none` control: same node, same place,
        # no archive. Ringed rather than filled, so the control is visible as a control.
        if i in designated:
            parts.append(
                f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="11" fill="none" '
                f'stroke="{SERVER}" stroke-width="1.6" stroke-dasharray="3 2"/>'
            )
        parts.append(_mark(shape, cx, cy, 5.5, colour, MUTED))

    for rank, i in enumerate(sorted(servers)):
        cx, cy = place[i]
        role = getattr(nodes[i], "role", None) or "CLIENT"
        shape, _, _ = ROLE_MARKS.get(role, UNKNOWN_ROLE)
        # Outside the role mark rather than replacing it: an archive on a router and one on a
        # muted client are different deployments, and one red dot cannot tell them apart.
        parts.append(
            f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="11.5" fill="none" '
            f'stroke="{SERVER}" stroke-width="2.4"/>'
        )
        parts.append(_mark(shape, cx, cy, 5.5, SERVER, "#FFFFFF", 1.1))
        parts.append(
            f'<text x="{cx:.1f}" y="{cy - 15:.1f}" font-size="10" font-weight="700" '
            f'fill="{SERVER}" text-anchor="middle">{rank + 1}</text>'
        )

    # Legend: only the roles this mesh actually has, so a uniform mesh does not carry five entries.
    ly = H - 62
    parts.append(
        f'<text x="{pad}" y="{ly - 12}" font-size="11.5" fill="{INK}">'
        f"role, by how much the node relays</text>"
    )
    lx = pad
    for role, (shape, colour, _) in ROLE_MARKS.items():
        if role not in roles_seen:
            continue
        parts.append(_mark(shape, lx + 6, ly + 6, 5.5, colour, MUTED))
        parts.append(
            f'<text x="{lx + 17}" y="{ly + 10}" font-size="10.5" fill="{MUTED}">'
            f"{role} {roles_seen[role]}</text>"
        )
        lx += 26 + 7.0 * len(role)
    parts.append(
        f'<circle cx="{lx + 6}" cy="{ly + 6}" r="8" fill="none" stroke="{SERVER}" stroke-width="2"/>'
        f'<text x="{lx + 19}" y="{ly + 10}" font-size="10.5" fill="{MUTED}">archive</text>'
    )

    stacked = sum(len(m) for m in stacks.values() if len(m) > 1)
    notes = [f"{drawn} link(s) drawn", f"{fragile_drawn} fragile"]
    if stacked:
        # Said out loud, because the positions of those nodes are not where the map puts them.
        notes.append(
            f"{stacked} node(s) share a position with another and are fanned out to be visible"
        )
    if skipped:
        notes.append(f"{skipped} link(s) not drawn (over {max_links})")
    parts.append(
        f'<text x="{W - 24}" y="{H - 26}" font-size="10.5" fill="{MUTED}" text-anchor="end">'
        f"{' &#183; '.join(notes)}</text>"
    )
    parts.append("</svg>")
    with open(path, "w") as f:
        f.write("".join(parts))
    return {
        "nodes": len(nodes),
        "links_drawn": drawn,
        "links_skipped": skipped,
        "fragile_drawn": fragile_drawn,
        "servers": len(servers),
        "roles": dict(sorted(roles_seen.items())),
        "stacked_nodes": stacked,
        "extent_km": [round(span_x / 1000, 2), round(span_y / 1000, 2)],
    }
