"""Charts rendered as a side effect of a run, not as a separate step afterwards.

Rendering by hand meant figures lagged the numbers, and twice in one day a number was withdrawn
after a figure had been made from it. A chart that is produced by the same call that produced the
JSON cannot drift from it, and it carries the transport commit in its own footer so it can never be
read against the wrong code.

Every per-node quantity is drawn as a distribution with the worst node marked, because a bar at the
mean is exactly the picture that hid the stranded nodes.

**SVG, written by hand, no dependency.** This drew with matplotlib until the charts turned out to be
the only reason anything here needed a third-party package - which meant CI, where every unattended
run happens, produced no charts at all. The shapes drawn are range bars, a dash, a dot and a
rectangle; a plotting library is not required to place those, and an SVG is smaller than the PNG it
replaces, scales, and can be read as text in a diff. `figures.py`, `figures3.py`, `diagram.py` and
`knowledge.render()` are hand-run tools and still use matplotlib.

Called automatically by campaign.main() and sweep.run_block(); suppress with --no-charts.
"""

import os
import subprocess
from xml.sax.saxutils import escape

INK = "#1b1b1b"
MUTED = "#8a8a8a"
ACCENT = "#B4472A"
COOL = "#2E5E7E"
WARN = "#B8860B"
GRID = "#e3e3e0"
BG = "#FCFCFA"

FONT = "ui-sans-serif, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"

# Panel geometry, in SVG user units. The panel is the plot area; the margins hold the axis labels,
# the tick labels and the title.
PANEL_W, PANEL_H = 470, 300
PAD_L, PAD_R, PAD_T, PAD_B = 62, 26, 46, 78


def _nice_ceiling(value):
    """Round an axis top up to something a reader can divide by five in their head.

    A flat 1.15x headroom gives tops like 1.15 and tick labels like 0.92.
    """
    if value <= 0:
        return 1.0
    for step in (0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10, 25, 50, 100, 250, 500, 1000):
        if value <= step * 5:
            return step * 5
    return value


def version_pin():
    """`sim <version> - <commit>`, for a figure footer. Both, for the reason sfpp/version.py gives."""
    from .version import SIM_VERSION

    return f"sim {SIM_VERSION} - {transport_pin()}"


def transport_pin():
    """Return the short SHA of the code producing this run, for the chart footer and the report."""
    try:
        return (
            subprocess.run(
                ["git", "rev-parse", "--short", "HEAD"],
                capture_output=True,
                text=True,
                cwd=os.path.dirname(os.path.abspath(__file__)),
            ).stdout.strip()
            or "unknown"
        )
    except Exception:
        return "unknown"


class Panel:
    """One set of axes: a value scale on y, evenly spaced categories on x."""

    def __init__(self, x0, title, labels, lo=None, hi=None, ylabel="", nice=False):
        self.x0 = x0
        self.title = title
        self.labels = list(labels)
        self.ylabel = ylabel
        self.lo = 0.0 if lo is None else lo
        self.hi = 1.0 if hi is None else hi
        if self.hi <= self.lo:
            # A flat series still has to draw. Give it a band rather than dividing by zero.
            self.hi = self.lo + 1.0
        # Only where the top came from the data. A share axis is 0 to 1 because that is what a share
        # is, and rounding it to 1.25 would put a ceiling above the only value it can reach.
        if nice:
            self.hi = _nice_ceiling(self.hi)
        self.parts = []

    @property
    def plot_left(self):
        return self.x0 + PAD_L

    @property
    def plot_width(self):
        return PANEL_W - PAD_L - PAD_R

    def x(self, i):
        """Centre of category i."""
        n = max(1, len(self.labels))
        return self.plot_left + self.plot_width * (i + 0.5) / n

    def y(self, value):
        span = self.hi - self.lo
        clamped = max(self.lo, min(self.hi, value))
        return PAD_T + (PANEL_H - PAD_T - PAD_B) * (1 - (clamped - self.lo) / span)

    def band_width(self):
        return self.plot_width / max(1, len(self.labels))

    # --- primitives -------------------------------------------------------------------------
    def rect(self, x, y, w, h, fill, opacity=1.0):
        self.parts.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{max(0.0, w):.1f}" '
            f'height="{max(0.0, h):.1f}" fill="{fill}" opacity="{opacity:g}" />'
        )

    def line(self, x1, y1, x2, y2, stroke, width=1.0):
        self.parts.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke}" stroke-width="{width:g}" />'
        )

    def dot(self, x, y, fill, r=4.0):
        self.parts.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:g}" fill="{fill}" />'
        )

    def text(
        self, x, y, s, size=9, fill=MUTED, anchor="middle", rotate=None, weight="normal"
    ):
        transform = f' transform="rotate({rotate} {x:.1f} {y:.1f})"' if rotate else ""
        self.parts.append(
            f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size:g}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}"{transform}>{escape(str(s))}</text>'
        )

    # --- furniture --------------------------------------------------------------------------
    def frame(self, ticks=5):
        """Grid lines, value ticks, category labels, title and y-axis label."""
        top, bottom = PAD_T, PANEL_H - PAD_B
        for i in range(ticks + 1):
            value = self.lo + (self.hi - self.lo) * i / ticks
            y = self.y(value)
            self.line(self.plot_left, y, self.plot_left + self.plot_width, y, GRID, 0.8)
            self.text(
                self.plot_left - 8,
                y + 3,
                (
                    f"{value:.2f}".rstrip("0").rstrip(".")
                    if self.hi <= 1.5
                    else f"{value:.0f}"
                ),
                size=8.5,
                anchor="end",
            )
        self.line(self.plot_left, top, self.plot_left, bottom, GRID, 1.0)
        self.line(
            self.plot_left, bottom, self.plot_left + self.plot_width, bottom, GRID, 1.0
        )
        # Rotate only when the labels would collide. The matplotlib original rotated
        # unconditionally, which on a three-category panel tips long names into the panel beside it.
        widest = max((len(str(x)) for x in self.labels), default=0) * 4.9
        rotate = widest > self.band_width() * 0.92
        for i, label in enumerate(self.labels):
            if rotate:
                self.text(
                    self.x(i), bottom + 14, label, size=8.5, anchor="end", rotate=-20
                )
            else:
                self.text(self.x(i), bottom + 15, label, size=8.5, anchor="middle")
        self.text(
            self.x0 + PAD_L, PAD_T - 16, self.title, size=10.5, fill=INK, anchor="start"
        )
        if self.ylabel:
            cx, cy = self.x0 + 16, (top + bottom) / 2
            self.text(cx, cy, self.ylabel, size=9, rotate=-90)

    # --- marks ------------------------------------------------------------------------------
    def spread(self, dists, highlight=None):
        """Range min-max, an inner p10-p90 band, the mean as a dash, the worst node as a dot."""
        w = self.band_width()
        for i, d in enumerate(dists):
            if not d:
                continue
            colour = ACCENT if (highlight and self.labels[i] == highlight) else COOL
            cx = self.x(i)
            self.rect(
                cx - 3.5,
                self.y(d["max"]),
                7,
                self.y(d["min"]) - self.y(d["max"]),
                colour,
                0.28,
            )
            self.rect(
                cx - 3.5,
                self.y(d["p90"]),
                7,
                self.y(d["p10"]) - self.y(d["p90"]),
                colour,
                0.55,
            )
            self.line(
                cx - w * 0.16,
                self.y(d["mean"]),
                cx + w * 0.16,
                self.y(d["mean"]),
                colour,
                2,
            )
            # The worst node, always marked: a bar at the mean is the picture that hid it.
            self.dot(cx, self.y(d["min"]), ACCENT)

    def bars(self, values, colours, offset=0.0, width_frac=0.66):
        bottom = PANEL_H - PAD_B
        w = self.band_width() * width_frac
        for i, v in enumerate(values):
            if v is None:
                continue
            cx = self.x(i) + offset * self.band_width()
            self.rect(
                cx - w / 2,
                self.y(v),
                w,
                bottom - self.y(v),
                colours[i] if isinstance(colours, list) else colours,
            )

    def stacked(self, layers, colours, offset=0.0, width_frac=0.66):
        """Bars of several layers, each sitting on the sum of the ones below it.

        For quantities that add up to something meaningful - two delivery paths to one reach -
        rather than for two measurements that merely share an axis, which `bars` puts side by side.
        """
        bottom = PANEL_H - PAD_B
        w = self.band_width() * width_frac
        base = [0.0] * len(layers[0])
        for layer, colour in zip(layers, colours):
            for i, v in enumerate(layer):
                if not v:
                    continue
                cx = self.x(i) + offset * self.band_width()
                top = self.y(base[i] + v)
                self.rect(cx - w / 2, top, w, self.y(base[i]) - top, colour)
                base[i] += v

    def legend(self, entries):
        x = self.plot_left + 6
        for label, colour in entries:
            self.rect(x, PAD_T + 4, 9, 9, colour)
            self.text(x + 13, PAD_T + 12, label, size=8.5, anchor="start")
            x += 16 + len(label) * 5.4


def _series_line(panel, points, colour, width=1.6, dashed=False):
    """A line through (x_index, value) pairs, skipping gaps rather than bridging them.

    A gap is a bin with no denominator; a bridge would draw a trend through no measurement.
    """
    previous = None
    for index, value in points:
        if value is None:
            previous = None
            continue
        if previous is not None:
            dash = ' stroke-dasharray="3 2"' if dashed else ""
            panel.parts.append(
                f'<line x1="{panel.x(previous[0]):.1f}" y1="{panel.y(previous[1]):.1f}" '
                f'x2="{panel.x(index):.1f}" y2="{panel.y(value):.1f}" stroke="{colour}" '
                f'stroke-width="{width}" stroke-linecap="round"{dash}/>'
            )
        previous = (index, value)


def _night_bands(panel, hours_of_day, count):
    """Shade the small hours, so a diurnal trough reads as night rather than as a dip.

    Drawn under everything: it separates "the mesh got quieter" from "it was 4am".
    """
    top, bottom = PAD_T, PANEL_H - PAD_B
    for index, hour in enumerate(hours_of_day):
        if hour is None or not (hour < 6 or hour >= 22):
            continue
        half = panel.band_width() / 2.0
        panel.parts.append(
            f'<rect x="{panel.x(index) - half:.1f}" y="{top}" '
            f'width="{panel.band_width():.1f}" height="{bottom - top}" '
            f'fill="{MUTED}" opacity="0.08"/>'
        )


def render_series(report, out_dir, label="run"):
    """Reception and load over simulated time, or None when the run carried no series.

    Two panels on one x axis: a reception dip under a utilisation peak is congestion, alone it is not.
    """
    series = report.get("series")
    if not series or not series.get("reception"):
        return None
    os.makedirs(out_dir, exist_ok=True)
    rows = series["reception"]
    load = series.get("load") or []
    hours = [r["hour_of_day"] for r in rows]
    # One label every few bins; 72 of them overlap into a grey smear.
    step = max(1, len(rows) // 8)
    labels = [
        (f"{r['hour_of_day']:.0f}h" if i % step == 0 else "") for i, r in enumerate(rows)
    ]

    classes = sorted({name for r in rows for name in r["by_class"]})
    # Text first and archived, matching every other output's ordering, then the rest.
    classes.sort(key=lambda n: (n != "text", n))
    palette = [ACCENT, "#2E5E7E", "#4E86A8", "#7FB0CB", "#B5D2E2"]

    reception = Panel(
        0,
        "reception rate per bin, by class",
        labels,
        lo=0.0,
        hi=1.0,
        ylabel="received / (sent x peers)",
    )
    _night_bands(reception, hours, len(rows))
    reception.frame()
    for colour, name in zip(palette, classes):
        _series_line(
            reception,
            [
                (i, (r["by_class"].get(name) or {}).get("rate"))
                for i, r in enumerate(rows)
            ],
            colour,
        )
    reception.legend(list(zip(classes, palette)))

    panels = [reception]
    if load:
        util = Panel(
            PANEL_W,
            "channel utilisation and collisions per bin",
            labels[: len(load)],
            lo=0.0,
            hi=100.0,
            ylabel="chutil %, and collisions scaled",
        )
        _night_bands(util, hours[: len(load)], len(load))
        util.frame()
        _series_line(util, [(i, r["chutil_p90"]) for i, r in enumerate(load)], ACCENT)
        _series_line(
            util, [(i, r["chutil_median"]) for i, r in enumerate(load)], "#2E5E7E"
        )
        # Collisions on the same axis, scaled to its top, because the shape is the point and a second
        # y axis on a 470px panel is unreadable. The legend says it is scaled rather than a percentage.
        peak = max((r["lost_to_collision"] for r in load), default=0) or 1
        _series_line(
            util,
            [(i, 100.0 * r["lost_to_collision"] / peak) for i, r in enumerate(load)],
            MUTED,
            width=1.2,
            dashed=True,
        )
        util.legend(
            [
                ("chutil p90 %", ACCENT),
                ("chutil median %", "#2E5E7E"),
                (f"collisions (peak {peak:,})", MUTED),
            ]
        )
        panels.append(util)

    hours_total = rows[-1]["hours"] if rows else 0
    doc = _document(
        panels,
        f"{label}: reception over {hours_total:.0f} simulated hours, "
        f"{series['bin_s'] // 60} min bins - shaded 22:00-06:00",
        f"{version_pin()} - seed {report.get('seed')} - "
        f"{report.get('opts', {}).get('nodes')} nodes",
    )
    path = os.path.join(out_dir, f"{label}-series.svg")
    with open(path, "w") as f:
        f.write(doc)
    return path


def _document(panels, suptitle, footer):
    """Lay the panels side by side and wrap them in one SVG."""
    width = PANEL_W * len(panels)
    height = PANEL_H + 34
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" font-family="{FONT}">',
        f'<rect width="{width}" height="{height}" fill="{BG}" />',
        f'<text x="14" y="20" font-size="11.5" fill="{INK}" font-weight="600">{escape(suptitle)}</text>',
    ]
    for p in panels:
        out.append(f'<g transform="translate(0 26)">{"".join(p.parts)}</g>')
    out.append(
        f'<text x="{width - 12}" y="{height - 8}" font-size="7.5" fill="{MUTED}" '
        f'text-anchor="end">{escape(footer)}</text>'
    )
    out.append("</svg>")
    return "\n".join(out)


def render_run(report, out_dir, label="run"):
    """One scenario: per-class reception spread, airtime share, and what only an archive delivered."""
    os.makedirs(out_dir, exist_ok=True)
    by = report.get("by_class") or {}
    s = report.get("sfpp") or {}
    order = sorted(by, key=lambda k: (not by[k].get("archived"), k))

    reception = Panel(
        0,
        "Reception per node, by class - red dot is the worst node",
        order,
        0,
        1,
        "share of that class received",
    )
    reception.frame()
    reception.spread([by[k].get("per_node_reception") for k in order], highlight="text")
    panels = [reception]

    shares = [by[k]["airtime_share"] for k in order]
    airtime = Panel(
        PANEL_W,
        "Share of channel airtime, by class",
        order,
        0,
        max(shares or [1]) * 1.15 or 1,
        "fraction of airtime",
        nice=True,
    )
    airtime.frame()
    airtime.bars(shares, [ACCENT if k == "text" else COOL for k in order])
    panels.append(airtime)

    if s.get("structurally_unreachable"):
        only = Panel(
            PANEL_W * 2,
            f"Only an archive could deliver these - {s.get('nodes_with_zero_delivered')} of "
            f"{s.get('nodes_measured')} nodes got none",
            ["unreachable", "delivered anyway", "share delivered"],
            0,
            1,
            "share of all text",
        )
        only.frame()
        only.spread(
            [
                s["structurally_unreachable"],
                s["delivered_though_unreachable"],
                s["per_node_share_of_unreachable_delivered"],
            ]
        )
        panels.append(only)

    mesh = report.get("mesh") or {}
    opts = report.get("opts") or {}
    doc = _document(
        panels,
        f"{label} - {opts.get('topology', 'uniform')}, {mesh.get('nodes')} nodes, "
        f"diameter {mesh.get('diameter') or 'FRAGMENTED'}, protocol {opts.get('protocol', 'sr')}",
        f"{version_pin()} · seed {report.get('seed')} · {opts.get('hours')} h",
    )
    path = os.path.join(out_dir, f"{label}.svg")
    with open(path, "w") as f:
        f.write(doc)
    return path


def render_block(reports, out_dir, name):
    """One arm: the swept value against text reach (mean and worst node) and archive airtime."""
    os.makedirs(out_dir, exist_ok=True)
    arms = {}
    for r in reports:
        arms.setdefault(str(r.get("value", "-")), []).append(r)
    labels = list(arms)
    # Split by how the text arrived, because they are two different claims: the flood delivering
    # more, and an archive replaying what the flood never carried. Stacked rather than side by
    # side - they sum to the reach the run reports, and the total is what a user holds.
    def mean_of(pick):
        return [sum(pick(g) for g in arms[k]) / len(arms[k]) for k in labels]

    total_reach = mean_of(lambda g: g["baseline"]["text_reception_mean"])
    # Per report, not per cell: a cell can hold seeds from either side of the split landing, and
    # taking a missing figure as zero would drag the mean down rather than fall back. A report
    # without the split reads its total as first chance - right for every protocol with no replay
    # path, and what that figure already showed for the rest.
    on_air = mean_of(
        lambda g: g["baseline"].get("text_on_air_mean", g["baseline"]["text_reception_mean"])
    )
    overheard = [max(0.0, total_reach[i] - on_air[i]) for i in range(len(labels))]
    worst_reach = [
        min(g["baseline"]["text_reception_min"] for g in arms[k]) for k in labels
    ]
    air = [
        100
        * sum((g.get("sfpp") or {}).get("sr_airtime_share", 0) for g in arms[k])
        / len(arms[k])
        for k in labels
    ]

    reach = Panel(
        0,
        "Text reach - first chance, replay, worst node",
        labels,
        0,
        1,
        "share of text received",
    )
    reach.frame()
    reach.stacked(
        [on_air, overheard], [COOL, WARN], offset=-0.19, width_frac=0.34
    )
    reach.bars(worst_reach, ACCENT, offset=0.19, width_frac=0.34)
    reach.legend(
        [("on air", COOL), ("overheard replay", WARN), ("worst node", ACCENT)]
    )

    airtime = Panel(
        PANEL_W,
        "Reconciliation's share of channel airtime",
        labels,
        0,
        max(air or [1]) * 1.15 or 1,
        "% of airtime",
        nice=True,
    )
    airtime.frame()
    airtime.bars(air, WARN)

    doc = _document(
        [reach, airtime],
        f"{name} - arm `{reports[0].get('arm', 'value')}`, {len(arms[labels[0]])} seeds per cell",
        f"{version_pin()}",
    )
    path = os.path.join(out_dir, f"{name}.svg")
    with open(path, "w") as f:
        f.write(doc)
    return path


def auto(reports, out_json, kind="run"):
    """Render beside the JSON that produced it. Never raises - a chart must not fail a run."""
    try:
        base = os.path.dirname(os.path.abspath(out_json)) if out_json else "."
        figs = os.path.join(base, "figures")
        name = os.path.basename(out_json or "run").replace(".json", "")
        if kind == "block" and len(reports) > 1:
            return render_block(reports, figs, name)
        written = render_run(reports[0], figs, name)
        # The series chart is an extra beside the run's own, not a replacement: it only exists when
        # the run was asked to sample, and a run without it must render exactly as before.
        extra = render_series(reports[0], figs, name)
        return f"{written}, {extra}" if extra else written
    except Exception as exc:
        print(f"  (chart skipped: {type(exc).__name__}: {exc})")
        return None
