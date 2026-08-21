"""External, non-Meshtastic occupancy of the channel, as a state rather than a coin flip.

A foreign transmitter holds the channel for the length of its frame. It was modelled as an
independent draw at every point of use: `is_channel_active` drew once per CAD check, and
`check_collision` drew again, separately, per packet per receiver. Two consequences, both wrong in
the same direction:

- **It could not block, only delay.** Independent draws with no holding time mean a transmitter
  retrying its CAD finds the channel clear within a few attempts by construction, however high the
  level. Real interference occupies the air for milliseconds at a time.
- **The two ends disagreed.** A transmitter's CAD could see a clear channel while, in the same
  instant, its frame was destroyed by "external interference" at a receiver - because interference
  was not a property of anything, so there was nothing for both to observe.

Here it is a schedule of busy stretches, drawn once per node from its own stream, so a node's CAD and
a reception at that same node consult the same channel. Per node rather than per mesh because
interference is local: the noise floor at a receiver is what destroys a frame, and the noise floor at
a transmitter is what its CAD detects. They are different places and, on a mesh spanning kilometres,
different conditions.

The long-run busy share is `INTERFERENCE_LEVEL`, exactly, at every value including both endpoints.
"""

import bisect
import random


class ExternalInterference:
    """Busy stretches on one node's channel, as an alternating renewal process.

    Busy and idle holding times are exponential with a mean of `mean_busy_ms`, scaled so the
    long-run busy share is `level`. Endpoints are handled by construction rather than by the
    arithmetic: 0.0 is never busy and 1.0 is always busy, so the level is a control that works
    rather than one that only shifts the middle.
    """

    def __init__(self, level, horizon_ms, mean_busy_ms, seed):
        self.level = float(level)
        self.always_busy = self.level >= 1.0
        self._starts = []
        self._ends = []
        if self.always_busy or self.level <= 0.0 or horizon_ms <= 0 or mean_busy_ms <= 0:
            return

        rng = random.Random(seed)
        # A busy mean of B and a duty of L wants an idle mean of B * (1 - L) / L.
        mean_idle_ms = mean_busy_ms * (1.0 - self.level) / self.level
        now = rng.expovariate(1.0 / mean_idle_ms)
        while now < horizon_ms:
            end = now + rng.expovariate(1.0 / mean_busy_ms)
            self._starts.append(now)
            self._ends.append(end)
            now = end + rng.expovariate(1.0 / mean_idle_ms)

    def is_busy(self, t):
        """Whether a foreign transmitter holds the channel at this instant."""
        if self.always_busy:
            return True
        if not self._starts:
            return False
        index = bisect.bisect_right(self._starts, t) - 1
        return index >= 0 and t < self._ends[index]

    def overlaps(self, start, end):
        """Whether any busy stretch overlaps [start, end) - i.e. whether a frame is jammed."""
        if self.always_busy:
            return end > start
        if not self._starts or end <= start:
            return False
        # The last stretch beginning before `end`; anything earlier ends earlier still, except
        # that stretches never overlap each other, so one candidate is enough.
        index = bisect.bisect_left(self._starts, end) - 1
        return index >= 0 and self._ends[index] > start

    def overlap_ms(self, start, end):
        """How many milliseconds of [start, end) a foreign transmitter held."""
        if end <= start:
            return 0.0
        if self.always_busy:
            return end - start
        if not self._starts:
            return 0.0
        total = 0.0
        index = max(0, bisect.bisect_right(self._starts, start) - 1)
        while index < len(self._starts) and self._starts[index] < end:
            total += max(0.0, min(self._ends[index], end) - max(self._starts[index], start))
            index += 1
        return total

    def busy_share(self, horizon_ms):
        """The realised busy share over [0, horizon_ms), for asserting the level means what it says."""
        if self.always_busy:
            return 1.0
        if horizon_ms <= 0:
            return 0.0
        busy = sum(
            min(end, horizon_ms) - min(start, horizon_ms)
            for start, end in zip(self._starts, self._ends)
        )
        return busy / horizon_ms


def build(conf, seed, node_id):
    """One node's interference schedule, from the run's config.

    The holding time defaults to the airtime of a full frame on the configured preset: the most
    likely foreign occupant of a LoRa channel is another LoRa frame.
    """
    from lib.phy import airtime

    mean_busy_ms = getattr(conf, "INTERFERENCE_MEAN_BUSY_MS", None)
    if mean_busy_ms is None:
        preset = conf.current_preset
        mean_busy_ms = airtime(conf, preset["sf"], preset["cr"], conf.PACKETLENGTH, preset["bw"])
    # Seeded off the run's seed but through its own constant, so the field is reproducible without
    # being correlated with anything else the seed decides.
    return ExternalInterference(
        conf.INTERFERENCE_LEVEL,
        conf.SIMTIME,
        mean_busy_ms,
        (seed ^ 0x494E5446) + node_id,
    )
