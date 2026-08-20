"""The offered load: what a Meshtastic channel actually carries, not just the part SF++ archives.

Reconciliation cost only means something against the traffic it shares a channel with. A mesh whose
only packets are text messages would make an advert look expensive; a real one is mostly position
and telemetry, and the archived class is a minority of it. Rates below are per node per hour and
sized so text lands at roughly a seventh of originated packets - what a channel looks like with
telemetry on and a normal share of people talking.

Text is the only archived class. Everything else exists to contend for the channel, to be relayed,
and to be missed - which is what the baseline measures.
"""

import hashlib
import math
from dataclasses import dataclass

# Portnums, from mesh.proto.
TEXT_MESSAGE_APP = 1
POSITION_APP = 3
NODEINFO_APP = 4
TELEMETRY_APP = 67

# Role names, as mesh.py spells them. Duplicated rather than imported: this module deliberately does
# not depend on the transport, and they are wire-level strings that cannot change without the
# firmware changing.
CLIENT = "CLIENT"
CLIENT_MUTE = "CLIENT_MUTE"

HASH_SIZE = 16  # SFPP_HASH_SIZE
BROADCAST = 0xFFFFFFFF


@dataclass(frozen=True)
class Class:
    name: str
    portnum: int
    per_hour: float
    mean_bytes: float
    sigma_bytes: float
    node_fraction: float  # share of nodes that emit this class at all
    archived: bool = False
    # Addressed to one peer rather than broadcast. A DM is PKI-encrypted and asks for an ack, so it
    # exercises next-hop routing and the retry ladder where a broadcast exercises the flood.
    directed: bool = False


# Payload sizes are the Data protobuf, which is what airtime is charged on after the 16-byte header.
DEFAULT_MIX = (
    Class("position", POSITION_APP, 4.0, 20, 4, 1.0),
    Class("telemetry", TELEMETRY_APP, 2.0, 24, 6, 1.0),
    Class("nodeinfo", NODEINFO_APP, 1.0, 40, 8, 1.0),
    Class("text", TEXT_MESSAGE_APP, 1.2, 53, 20, 0.4, archived=True),
    # Direct messages. Rate 0 by default: --dm-per-hour turns them on, because every result
    # published before they existed was measured without them and they are not free.
    Class("dm", TEXT_MESSAGE_APP, 0.0, 53, 20, 0.4, directed=True),
)


def message_hash_of(encrypted_bytes, to, frm, packet_id):
    """SHA-256(encrypted || to || from || id) truncated to 16 bytes - recalculateMessageHash()."""
    h = hashlib.sha256()
    h.update(encrypted_bytes)
    h.update(to.to_bytes(4, "little"))
    h.update(frm.to_bytes(4, "little"))
    h.update(packet_id.to_bytes(4, "little"))
    return h.digest()[:HASH_SIZE]


@dataclass
class TextObject:
    """An archived text broadcast, carrying the fields the SF++ store keeps."""

    destination: int
    sender: int
    packet_id: int
    rx_time: int
    root_hash: bytes
    encrypted_bytes: bytes
    message_hash: bytes
    commit_hash: bytes
    payload: str = ""

    @property
    def wire_size(self):
        return len(self.encrypted_bytes)


# Hourly weights, local time, index 0 = midnight. Normalised by the caller so the daily mean matches
# the configured rate whichever shape is chosen - a diurnal curve should move *when* traffic happens,
# not how much of it there is, or the shapes would not be comparable.
#
# `commuter` is the two-peak human pattern: a morning bump, a lull, a larger evening peak and a deep
# overnight trough. `sinusoid` is the single-peak version, kept for comparison. Both are drawn from
# how people behave rather than from a measured feed.
DIURNAL = {
    "flat": [1.0] * 24,
    "sinusoid": [
        1.0 + 0.7 * math.sin((h - 15) / 24.0 * 2 * math.pi) for h in range(24)
    ],
    "commuter": [
        0.25,
        0.18,
        0.14,
        0.12,
        0.15,
        0.30,  # 00-05 overnight trough
        0.70,
        1.30,
        1.55,
        1.20,
        1.00,
        0.95,  # 06-11 morning peak then settle
        1.05,
        1.00,
        0.95,
        1.00,
        1.35,
        1.85,  # 12-17 afternoon into the evening rise
        2.10,
        1.95,
        1.60,
        1.15,
        0.70,
        0.40,  # 18-23 evening peak and decline
    ],
}


def diurnal_weight(shape, hour_of_day):
    weights = DIURNAL[shape]
    return weights[int(hour_of_day) % 24] / (sum(weights) / 24.0)


# Default.h congestionScalingCoefficient, 2.5 and 2.6: the per-node throttle depends on the modem
# preset, and the two shortest presets switch it off entirely rather than throttling at all.
PRESET_THROTTLING_FACTOR = {
    "MEDIUM_SLOW": 0.04,
    "MEDIUM_FAST": 0.02,
    "SHORT_SLOW": 0.01,
    "SHORT_FAST": None,
    "SHORT_TURBO": None,
}
PRESET_THROTTLING_DEFAULT = 0.075

# 2.5 through v2.7.16 shorten intervals on a small mesh instead of leaving them alone. Removed in
# v2.7.17, so the 2.7 profile - which is v2.7.21 - does not have it.
SMALL_MESH_SPEEDUP = ((10, 0.6), (20, 0.7), (30, 0.8))

# No firmware has this mode: busy-ness is mapped onto the same 40-node pivot the throttle
# turns at, as a stated assumption. MODEL.md.
UTILISATION_PIVOT_PERCENT = 40.0
UTILISATION_PIVOT_NODES = 40

# Default.h's literal 40 in `numOnlineNodes > 40`; below it every profile leaves the interval
# alone. A knob rather than a constant because moving it is how the advice gets tested.
CONGESTION_PIVOT = 40


def congestion_coefficient(
    node_count,
    sf,
    bw_hz,
    event_mode=False,
    model="sf_bw",
    preset="LONG_FAST",
    pivot=CONGESTION_PIVOT,
):
    """The firmware's own broadcast-interval scaling, Default.h congestionScalingCoefficient.

    A multiplier on every periodic broadcast interval; three models, one per era - MODEL.md.
    """
    if model == "preset":
        for bound, coefficient in SMALL_MESH_SPEEDUP:
            if node_count <= bound:
                return coefficient
    if node_count <= pivot:
        return 1.0
    if model == "flat":
        throttling_factor = PRESET_THROTTLING_DEFAULT
    elif model == "preset":
        throttling_factor = PRESET_THROTTLING_FACTOR.get(
            preset, PRESET_THROTTLING_DEFAULT
        )
        if throttling_factor is None:
            return 1.0
    else:
        divisor = 25.0 if event_mode else 100.0
        throttling_factor = (2.0**sf) / ((bw_hz / 1000.0) * divisor)
    return 1.0 + (node_count - pivot) * throttling_factor


def observed_senders(mesh, window_ms=7200_000.0):
    """Distinct senders heard recently, mesh-wide.

    Bounded by packet history rather than MAX_NUM_NODES, so hot-store saturation is visible.
    """
    now = mesh.now
    senders = set()
    for node in mesh.nodes:
        for packet_id, when in node.seen.items():
            if now - when > window_ms:
                continue
            record = node.history.get(packet_id)
            if record is not None:
                senders.add(record.sender)
    return len(senders)


class Generator:
    """Schedules every node's originated traffic across the run, then hands it to the mesh.

    Poisson per class per node: synchronised senders would understate collisions. MODEL.md.
    """

    def __init__(
        self,
        mesh,
        rng,
        root_hash,
        mix=DEFAULT_MIX,
        text_scale=1.0,
        congestion_scaling=True,
        congestion_mode="adaptive",
        position_throttle=1,
        telemetry_throttle=1,
        online_cap=120,
        congestion_input="hotstore",
        broadcast_interval_s=None,
        diurnal="flat",
        archive_dms=False,
        start_hour=8.0,
        congestion_pivot=CONGESTION_PIVOT,
    ):
        self.mesh = mesh
        self.rng = rng
        self.root_hash = root_hash
        self.mix = mix
        self.text_scale = text_scale
        preset = mesh.conf.current_preset
        # Device broadcasts stretch with mesh size and user text does not, under whichever era's
        # throttle the mesh's own profile carries. adaptive vs static: MODEL.md.
        profile = mesh.nodes[0].profile if mesh.nodes else None
        self.congestion_mode = congestion_mode if congestion_scaling else "off"
        self.congestion_model = (
            profile.congestion_model if profile is not None else "sf_bw"
        )
        self.preset_name = getattr(mesh.conf, "MODEM_PRESET", "LONG_FAST")
        self.sf = preset["sf"]
        self.bw = preset["bw"]
        self.online_cap = online_cap
        # Which quantity drives the throttle: the firmware's bounded hot store, the unbounded
        # ideal, or measured busy-ness. The arm round four exists to price - MODEL.md.
        self.congestion_input = congestion_input
        # Where the throttle starts. The firmware's 40 is a constant; moving it is the only way to
        # ask whether a mesh should begin throttling sooner or later than it does.
        self.congestion_pivot = congestion_pivot
        # Across every profile present, not just node zero's: candidates must be generated at
        # least as fast as anything later thinned from them. MODEL.md.
        models = {node.profile.congestion_model for node in mesh.nodes} or {
            self.congestion_model
        }
        self.congestion_floor = (
            min(c for _, c in SMALL_MESH_SPEEDUP) if "preset" in models else 1.0
        )
        self.congestion = (
            # getNumOnlineMeshNodes() iterates the hot store, so a node cannot count mesh members it
            # has evicted. The coefficient is bounded by MAX_NUM_NODES, not by mesh size.
            congestion_coefficient(
                (
                    len(mesh.nodes)
                    if congestion_input == "truesize"
                    else min(len(mesh.nodes), online_cap)
                ),
                self.sf,
                self.bw,
                model=self.congestion_model,
                pivot=self.congestion_pivot,
                preset=self.preset_name,
            )
            if congestion_scaling
            else 1.0
        )
        # Region profile multipliers, RegionProfile::positionThrottle / telemetryThrottle. Integer,
        # 1 is neutral, and applied on top of the congestion coefficient.
        self.throttle = {
            "position": max(1, position_throttle),
            "telemetry": max(1, telemetry_throttle),
        }
        # Text follows the clock because a person sends it. Telemetry and nodeinfo do not - a device
        # reports on a timer regardless of the hour. Position sits in between and is treated as
        # human-driven, since a node only has a new position when someone has moved it.
        # One interval for every device-originated class, the way an operator sets it. None keeps the
        # per-class mix. This is the denominator every SF++ airtime share is quoted against, so it
        # deserves to be a knob rather than an assumption.
        self.broadcast_interval_s = broadcast_interval_s
        self.diurnal = diurnal
        self.diurnal_classes = {"text", "position", "dm"}
        self.start_hour = start_hour
        self.emitters = {}
        self.objects = (
            {}
        )  # message_hash -> TextObject, the ground truth for the archive
        self.text_order = (
            []
        )  # message_hash in origination order; the chain counter follows it
        self.originated = {c.name: 0 for c in mix}
        # The denominator for reception-over-time: only the generator knows when it composed
        # something. A bin_ms of 0 leaves it inert, so a run without the series pays nothing.
        self.bin_ms = 0.0
        self.originated_bins = {}
        self.archive_dms = archive_dms
        # packet id -> (sender, target, sent_at). Resolved against whether the target ever saw
        # it, so success is measured at the recipient rather than inferred from the flood.
        self.dm_sent = {}
        self.dm_no_key = 0
        self.dm_no_addressable = 0

        node_count = len(mesh.nodes)
        # Every node that is not router-like: nobody chats from a mast, and CLIENT_MUTE still
        # has a user even though it does not rebroadcast. MODEL.md.
        self.dm_pool = [
            i
            for i, node in enumerate(mesh.nodes)
            if node.role in (CLIENT, CLIENT_MUTE) and node.originates_dm
        ]
        # A node that receives but never starts one: an unattended sensor, a node whose owner reads
        # and never writes. It still relays, and it is still a destination.
        self.dm_targets = [
            i
            for i, node in enumerate(mesh.nodes)
            if node.role in (CLIENT, CLIENT_MUTE)
        ]
        for cls in mix:
            if cls.directed:
                # A class with no rate draws nothing, not even its emitter set: a sample() here
                # would shift every later schedule off the shared stream.
                if cls.per_hour <= 0 or not self.dm_pool:
                    self.emitters[cls.name] = set()
                    continue
                # Only nodes that originate, and only from the DM pool - `node_fraction` then says
                # what share of those actually have someone typing on them.
                pool = self.dm_pool
                count = min(len(pool), max(1, int(round(len(pool) * cls.node_fraction))))
                self.emitters[cls.name] = set(rng.sample(pool, count))
                continue
            count = max(1, int(round(node_count * cls.node_fraction)))
            chosen = rng.sample(range(node_count), count)
            self.emitters[cls.name] = set(chosen)

    def node_congestion(self, node_index):
        """The coefficient this node would apply right now, from its own view of the mesh.

        `congestion_input` chooses what that view is, which is the point of the arm - MODEL.md.
        """
        if self.congestion_mode != "adaptive":
            return self.congestion
        node = self.mesh.nodes[node_index]
        if self.congestion_input == "truesize":
            online = len(self.mesh.nodes)
        elif self.congestion_input == "utilisation":
            busy = node.channel_utilization_percent(self.mesh.now)
            online = int(UTILISATION_PIVOT_NODES * busy / UTILISATION_PIVOT_PERCENT)
        else:
            online = min(node.num_online(self.mesh.now) + 1, self.online_cap)
        return congestion_coefficient(
            online,
            self.sf,
            self.bw,
            model=node.profile.congestion_model,
            preset=self.preset_name,
            pivot=self.congestion_pivot,
            event_mode=node.profile.event_relay_hop_limit is not None,
        )

    def _size(self, cls):
        return max(8, int(self.rng.gauss(cls.mean_bytes, cls.sigma_bytes)))

    def schedule(self, duration_ms):
        """Lay every originated packet onto the mesh's event queue."""
        for cls in self.mix:
            if cls.archived:
                rate = cls.per_hour * self.text_scale
            else:
                # An operator-set interval for every device class, or the per-class mix. Congestion
                # scaling and the region throttle still apply on top of either.
                base = (
                    3600.0 / self.broadcast_interval_s
                    if self.broadcast_interval_s
                    else cls.per_hour
                )
                # adaptive lays candidates down at the most permissive rate and thins at emit
                # time; static divides the rate by one constant. MODEL.md.
                rate = base / self.throttle.get(cls.name, 1)
                rate = (
                    rate / self.congestion_floor
                    if self.congestion_mode == "adaptive"
                    else rate / self.congestion
                )
            if rate <= 0:
                continue
            adaptive = self.congestion_mode == "adaptive" and not cls.archived
            diurnal = self.diurnal != "flat" and cls.name in self.diurnal_classes
            peak = (
                max(DIURNAL[self.diurnal]) / (sum(DIURNAL[self.diurnal]) / 24.0)
                if diurnal
                else 1.0
            )
            # Non-homogeneous Poisson by thinning: generate at peak, keep with weight(t)/peak.
            # The right arrival process, rather than a rescaled uniform one.
            mean_gap_ms = 3600_000.0 / (rate * peak)
            for node in self.emitters[cls.name]:
                t = self.rng.expovariate(1.0 / mean_gap_ms)
                while t < duration_ms:
                    keep = True
                    if diurnal:
                        hour = (self.start_hour + t / 3600_000.0) % 24
                        keep = self.rng.random() < diurnal_weight(self.diurnal, hour) / peak
                    if keep:
                        self._schedule_one(node, cls, t, adaptive=adaptive)
                    t += self.rng.expovariate(1.0 / mean_gap_ms)

    def _schedule_one(self, node, cls, when, adaptive=False):
        size = self._size(cls)

        def emit(node=node, cls=cls, size=size):
            if adaptive:
                # A candidate survives with probability floor/coefficient, so a node whose store
                # says the mesh is large sends proportionally less often.
                if self.rng.random() > self.congestion_floor / self.node_congestion(node):
                    return
            if cls.directed:
                # A fresh peer each time, from those whose keys this node holds - the list the
                # firmware's DM UI shows. Drawing from the whole mesh measures keys, not delivery.
                radio = self.mesh.nodes[node]
                peers = [
                    p
                    for p in self.dm_targets
                    if p != node and radio.knows_key(p)
                ]
                if not peers:
                    # Nobody addressable yet - early in a run, before nodeinfo has spread. A real
                    # outcome, and the reason an operator's first DM on a fresh node fails.
                    self.dm_no_addressable += 1
                    return
                target = self.rng.choice(peers)
                packet = self.mesh.originate(
                    node,
                    cls.portnum,
                    size,
                    kind=cls.name,
                    destination=target,
                    want_ack=True,
                    pki=True,
                    payload=None if self.archive_dms else b"",
                )
                if packet is None:
                    # No key for the peer, so the firmware never composes it. Counted, because an
                    # undeliverable DM is a real outcome and not the same as a lost one.
                    self.dm_no_key += 1
                    return
                self.dm_sent[packet.id] = (node, target, self.mesh.now)
                if self.archive_dms:
                    obj = self._make_object(node, packet.id, size, destination=target)
                    packet.payload = obj.message_hash
                    self.objects[obj.message_hash] = obj
                    self.text_order.append(obj.message_hash)
                self.originated[cls.name] += 1
                self._note_origination(cls.name)
                return
            if cls.archived:
                packet = self.mesh.originate(
                    node, cls.portnum, size, kind=cls.name, payload=None
                )
                if packet is None:
                    return  # the node is offline; nothing was composed, so nothing is archived
                obj = self._make_object(node, packet.id, size)
                packet.payload = obj.message_hash
                self.objects[obj.message_hash] = obj
                self.text_order.append(obj.message_hash)
            else:
                self.mesh.originate(node, cls.portnum, size, kind=cls.name)
            self.originated[cls.name] += 1
            self._note_origination(cls.name)

        self.mesh.at(when, emit)

    def _note_origination(self, name):
        """Which time bin this packet was composed in. Inert unless `bin_ms` was set."""
        if not self.bin_ms:
            return
        slot = self.originated_bins.setdefault(int(self.mesh.now // self.bin_ms), {})
        slot[name] = slot.get(name, 0) + 1

    def _make_object(self, node, packet_id, size, destination=BROADCAST):
        """The object the archive would hold: ciphertext stands in at the same length.

        Length and uniqueness are all the hash needs, and the derivation is the firmware's.
        """
        encrypted = self.rng.randbytes(size)
        return TextObject(
            destination=destination,
            sender=node,
            packet_id=packet_id,
            rx_time=int(self.mesh.now),
            root_hash=self.root_hash,
            encrypted_bytes=encrypted,
            message_hash=message_hash_of(encrypted, destination, node, packet_id),
            commit_hash=b"\x00" * HASH_SIZE,
        )
