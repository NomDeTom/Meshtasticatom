"""A noise floor that moves, because a real one does.

The thermal floor is theory: kTB plus a receiver's noise figure is what the band would be with
nothing in it, and it is a *lower bound*, not a description. A real receiver sits in whatever the
band is doing - other spectrum users, switching supplies, a neighbour's LED lighting, the diurnal
cycle - so the floor is a distribution with a median well above thermal and several decibels of
spread, varying by site and by hour.

That matters for more than realism. Every threshold in this simulator is derived from the floor:
what a receiver can decode, what its CAD detects, and what SNR it reports. Collapsing a varying
quantity to one constant and then using it as a hard cut turns a link that is up at 3 a.m. and down
at 6 p.m. into a link that either exists or does not - which removes exactly the marginal, flickering
connectivity that decides whether a mesh holds together.

It also bears on the packaged Batumi observations. Their scatter is 8.11 dB with no distance trend,
and a floor moving by several decibels over the observation window would put most of that scatter in
the receiver's band rather than in the path. An observation at -20.75 dB SNR is then a link measured
at a quiet moment, not an impossible one.

Values are hashed on `(seed, bucket)` rather than drawn from a stream, so a run is reproducible and
adding or removing a query cannot shift anything else - the pattern TRAPS names for the physics.
"""

import hashlib
import math
import struct


class NoiseFloor:
    """One receiver's noise floor over time, in dBm.

    A median with log-normal spread, correlated over `tau_msec` so the band drifts rather than
    flickering per packet, and clamped below by the thermal floor: nothing can be quieter than the
    receiver's own noise. `sigma_db = 0` gives back a constant floor exactly.
    """

    INTERPOLATION_VARIANCE_CORRECTION = math.sqrt(1.5)

    def __init__(self, median_dbm, sigma_db, tau_msec, thermal_floor_dbm, seed):
        self.median_dbm = float(median_dbm)
        self.sigma_db = max(0.0, float(sigma_db))
        self.tau_msec = max(1.0, float(tau_msec))
        self.thermal_floor_dbm = float(thermal_floor_dbm)
        self.seed = int(seed) & 0xFFFFFFFF

    def _gauss(self, bucket):
        """A standard normal for this bucket, from a hash rather than a stream."""
        digest = hashlib.blake2b(
            struct.pack("<IQ", self.seed, bucket & 0xFFFFFFFFFFFFFFFF), digest_size=8
        ).digest()
        # Two uniforms out of one digest, then Box-Muller. Nudged off zero so log() is finite.
        high, low = struct.unpack("<II", digest)
        u1 = (high + 0.5) / 4294967296.0
        u2 = (low + 0.5) / 4294967296.0
        return math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)

    def level_at(self, now_msec):
        """The floor at this instant, interpolated between correlated bucket values."""
        if self.sigma_db <= 0.0:
            return max(self.median_dbm, self.thermal_floor_dbm)

        position = now_msec / self.tau_msec
        bucket = math.floor(position)
        blend = position - bucket
        # Linear interpolation between neighbouring buckets: continuous in time, so a frame does
        # not straddle a step change in the band it is being received in.
        offset = self._gauss(bucket) * (1.0 - blend) + self._gauss(bucket + 1) * blend
        # Interpolating two independent normals costs variance - ((1-b)^2 + b^2) averages to 2/3 -
        # so scale it back, or a caller asking for 4 dB of spread would measure 3.3.
        offset *= self.INTERPOLATION_VARIANCE_CORRECTION
        return max(self.median_dbm + offset * self.sigma_db, self.thermal_floor_dbm)

    def median_level(self):
        """The floor with its variation removed, for reporting and for a static comparison."""
        return max(self.median_dbm, self.thermal_floor_dbm)


# The reception threshold is evaluated once per packet, at construction. That is only sound while
# the band moves slowly compared with a frame: a correlation time of tens of seconds against frames
# of tens or hundreds of milliseconds. Below this the band would change materially *during* a frame
# and the single sample would be wrong, so it is refused rather than silently approximated. Model
# pulsed or bursty interference with lib/interference.py, which is evaluated over the frame's own
# interval.
MIN_TAU_MSEC = 10_000.0


def build(conf, node_id):
    """One node's noise floor, from the run's config.

    Seeded off the run's seed through its own constant, so the band is reproducible without being
    correlated with anything else the seed decides.
    """
    from lib.phy import thermal_noise_floor

    # kTB alone, with no noise figure. The bound here is physics - a band cannot be quieter than
    # thermal - and the receiver's own noise figure is already inside the preset's sensitivity, so
    # bounding at kTB+NF would count it twice and raise the default floor by 5.2 dB. Which is worth
    # noting on its own: the default NOISE_LEVEL of -119.25 dBm implies a 0.8 dB noise figure at
    # 250 kHz, so it is not a measured band but a figure back-derived from the sensitivity table.
    sigma = getattr(conf, "NOISE_SIGMA_DB", 0.0)
    tau = getattr(conf, "NOISE_TAU_MSEC", 60_000.0)
    if sigma > 0.0 and tau < MIN_TAU_MSEC:
        raise ValueError(
            f"NOISE_TAU_MSEC of {tau} is shorter than {MIN_TAU_MSEC:.0f} ms: the reception "
            "threshold is sampled once per packet, so a band moving this fast would change during "
            "a frame. Model fast interference with lib/interference.py instead."
        )
    return NoiseFloor(
        conf.NOISE_LEVEL,
        sigma,
        tau,
        thermal_noise_floor(conf.current_preset["bw"], noise_figure_db=0.0),
        (conf.SEED ^ 0x4E4F4953) + node_id,
    )
