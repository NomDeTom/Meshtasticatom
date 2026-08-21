#!/usr/bin/env python3
from enum import Enum
import logging
import math
import random

import simpy

from lib.common import find_random_position
from lib.config import Config
from lib.dcr import choose_dynamic_coding_rate
from lib.discrete_event_sim_components import SimulationState, SimulationDataTracking
from lib.dtp import choose_dynamic_tx_power
from lib.geo import valid_lat_lon
from lib.interference import build as interference_for
from lib.noise import build as noise_floor_for
from lib.link_model import calculate_link_budget
from lib.mac import set_transmit_delay, get_retransmission_msec
from lib.phy import check_collision, effective_sensitivity, is_channel_active, airtime
from lib.packet import NODENUM_BROADCAST, MeshPacket, MeshMessage
from lib.point import Point
from lib.radio_loss import estimate_snr
from lib.terrain import NODE_Z_REFERENCE_SEA_LEVEL, apply_terrain_altitude

logger = logging.getLogger(__name__)

# roles taken from the protobuf config meshtastic/config.proto in https://github.com/meshtastic/protobufs
# deprecated roles are included for simulation utility
class MESHTASTIC_ROLE(Enum):
    CLIENT = 'CLIENT'
    CLIENT_MUTE = 'CLIENT_MUTE'
    ROUTER = 'ROUTER'
    ROUTER_CLIENT = 'ROUTER_CLIENT'
    REPEATER = 'REPEATER'
    TRACKER = 'TRACKER'
    SENSOR = 'SENSOR'
    TAK = 'TAK'
    CLIENT_HIDDEN = 'CLIENT_HIDDEN'
    LOST_AND_FOUND = 'LOST_AND_FOUND'
    TAK_TRACKER = 'TAK_TRACKER'
    ROUTER_LATE = 'ROUTER_LATE'
    CLIENT_BASE = 'CLIENT_BASE'

class MeshNodeStats:
    """Statistics, monitoring, and data tracking only relevant to and entirely
    internal to a single particular node
    """

    def __init__(self, nodeid: int):
        self.nodeid = nodeid

        self.packetsHeard = 0
        self.packetsRebroadcast = 0

    def get_stats_dictionary(self) -> dict:
        """Return dictionary holding all internal data
        (may not need this)
        """
        data = {
            "nodeid": self.nodeid,
            "packetsHeard": self.packetsHeard,
            "packetsRebroadcast": self.packetsRebroadcast,
        }
        return data

class NodeConfig:
    """Specific configuration for a node
    """
    def __init__(self, node_id: int, position: Point, period: int, tx_power: int = 30, freq: float = 902e6, role: MESHTASTIC_ROLE = MESHTASTIC_ROLE.CLIENT, antenna_gain: float = 0, hop_limit: int = 3, neighbor_info: bool = False, antenna_height=None, absolute_altitude=None):
        """Initial configuration of a node.

        `period` is the mean message interval; `antenna_height` is above local ground.
        """
        self.node_id = node_id
        self.position = position.copy() # make sure we keep our own point
        self.period = period
        self.tx_power = tx_power
        self.freq = freq
        self.role = role
        self.antenna_gain = antenna_gain
        self.hop_limit = hop_limit
        self.neighbor_info = neighbor_info
        self.antenna_height = position.z if antenna_height is None else antenna_height
        self.absolute_altitude = absolute_altitude

    @classmethod
    def from_gen_scenario_output(cls, node_id: int, node_dict: {}, period: int, tx_power: int, freq: float):
        """Build a NodeConfig from one entry of gen_scenario's output.

        Iterate that function's keys and pass the values indexed by each one.
        """
        nd = node_dict
        position = Point(nd['x'], nd['y'], nd['z'])

        # roles
        isRouter = nd['isRouter']
        isRepeater = nd['isRepeater']
        isClientMute = nd['isClientMute']

        # sanity check that only one role is set
        if (isRouter and isRepeater) or \
           (isRepeater and isClientMute) or \
           (isClientMute and isRouter):
           raise Exception(f"invalid combination of roles: {nd}")

        if isRouter:
            role = MESHTASTIC_ROLE.ROUTER
        elif isRepeater:
            role = MESHTASTIC_ROLE.REPEATER
        elif isClientMute:
            role = MESHTASTIC_ROLE.CLIENT_MUTE
        else:
            role = MESHTASTIC_ROLE.CLIENT

        antenna_height = nd.get("antennaHeight", nd["z"])
        absolute_altitude = nd.get("absoluteAltitude")
        return NodeConfig(node_id, position, period, tx_power, freq, role, nd['antennaGain'], nd['hopLimit'], nd['neighborInfo'], antenna_height, absolute_altitude)

    def compute_rssi_and_pathloss_to(self, rx_nodeconf, conf: Config) -> (float, float):
        """RSSI at `rx_nodeconf` and the path loss along the way, with this node transmitting.

        Returns them as a pair.
        """
        if self.node_id == rx_nodeconf.node_id:
            raise ValueError(f"Calculating rssi/pathloss between identical nodes is invalid. Node ID {self.node_id}")

        offset = getattr(conf, "LINK_OFFSET", {}).get((self.node_id, rx_nodeconf.node_id), 0)
        budget = calculate_link_budget(conf, self, rx_nodeconf, offset, tx_power_dbm=self.tx_power)
        return budget.rssi_dbm, budget.calibrated_path_loss_db


def node_configs_from_yaml(raw_config, period: int, tx_power: int = 30, freq: float = 902e6) -> list[NodeConfig]:
    """Convert saved node YAML into NodeConfig objects.

    Both shapes: the GUI's plain map, and a scenario file wrapping it under `nodes`.
    """
    if isinstance(raw_config, dict) and "nodes" in raw_config:
        node_map = raw_config["nodes"]
    else:
        node_map = raw_config

    if not isinstance(node_map, dict):
        raise ValueError("node YAML must be a node map or an object with a 'nodes' map")

    configs = []
    for sim_node_id, node_dict in enumerate(node_map.values()):
        configs.append(NodeConfig.from_gen_scenario_output(sim_node_id, node_dict, period, tx_power, freq))
    return configs


def origin_from_yaml(raw_config):
    """Return `(lat, lon)` origin metadata from wrapped scenario YAML if present."""
    if not isinstance(raw_config, dict):
        return None

    origin = raw_config.get("origin")
    if not isinstance(origin, dict) or "lat" not in origin or "lon" not in origin:
        return None

    try:
        lat = float(origin["lat"])
        lon = float(origin["lon"])
    except (TypeError, ValueError) as err:
        raise ValueError("origin.lat and origin.lon must be finite numbers") from err

    if not math.isfinite(lat) or not math.isfinite(lon):
        raise ValueError("origin.lat and origin.lon must be finite numbers")
    if not valid_lat_lon(lat, lon):
        raise ValueError("origin.lat and origin.lon must be valid latitude/longitude degrees")

    return lat, lon

def packet_is_rx_candidate(packet, rx_node_id: int, capture_model_enabled: bool) -> bool:
    """Return whether a packet should enter the receiver-side RF timeline.

    Capture mode admits one more band - detectable but undecodable - as interference energy.
    """
    if capture_model_enabled:
        return packet.detectedByN[rx_node_id]
    return packet.sensedByN[rx_node_id]


class MeshNode:
    """Class containing all the particular state of a MeshNode, references to necessary
    external resources like the simpy env, and process functions for simulation
    """
    def __init__(self, conf, sim_state: SimulationState, data_tracking: SimulationDataTracking, nodeConfig: NodeConfig):
        """Create a MeshNode: node-specific state, its sim processes, and its links to the run.

        `sim_state` is the run's mutable state; `data_tracking` only observes it.
        """
        self.conf = conf

        # Holds the repeated rssi/pathloss computation. Role, period and the rest could
        # move in here too rather than being bound as member variables.
        self.node_conf = nodeConfig

        self.nodeid = self.node_conf.node_id

        # set up internal RNGs
        # Each stream is seeded off the run's seed *and* the node id, so a seed sweep resamples
        # what a node does rather than replaying one realisation of it. These were
        # random.Random(self.nodeid): the mobility assignment - which nodes move, whether they have
        # GPS, which of the three speeds they draw, and every step of the walk - was byte-identical
        # at every seed, and so was each node's sequence of message gaps.
        self.moveRng = random.Random(f"{self.conf.SEED}:{self.nodeid}:move")
        self.nodeRng = random.Random(f"{self.conf.SEED}:{self.nodeid}:traffic")
        self.rebroadcastRng = random.Random(f"{self.conf.SEED}:{self.nodeid}:rebroadcast")
        # This node's own external channel occupancy, drawn once for the run: interference is local,
        # and the noise at a receiver is a different condition from the noise at a transmitter.
        self.interference = interference_for(self.conf, self.conf.SEED, self.nodeid)
        # The band this receiver sits in. Constant unless the scenario asks for spread, and never
        # quieter than the thermal floor for the preset's bandwidth.
        self.noiseFloor = noise_floor_for(self.conf, self.nodeid)

        # require the user to specify a node configuration now, including position
        self.position = self.node_conf.position # explicitly use position in node_conf
        self.role = self.node_conf.role
        self.hopLimit = self.node_conf.hop_limit
        self.antennaGain = self.node_conf.antenna_gain
        self.antennaHeight = self.node_conf.antenna_height
        self.absolute_altitude = self.node_conf.absolute_altitude
        self.period = self.node_conf.period

        # using this more like a struct than a proper object.
        self.my_stats = MeshNodeStats(self.nodeid)

        self.packetIdSeq = sim_state.packetIdSeq
        self.connectivity_map = sim_state.connectivity_map
        self.baseline_pathloss_matrix = sim_state.baseline_pathloss_matrix
        self.env = sim_state.env
        self.bc_pipe = sim_state.bc_pipe
        self.nodes = sim_state.nodes
        self.packetsAtN = sim_state.packetsAtN
        self.packets = sim_state.packets

        self.delays = data_tracking.delays
        self.messages = data_tracking.messages

        self.nrPacketsSent = 0
        # message id -> the time it was last heard. Bounded like PacketHistory, evicting the
        # oldest: an unbounded history suppresses a duplicate of a message a device would long
        # since have forgotten.
        self.timesReceived = {}
        self.lastHeard = {}
        # message id -> an event a reliable send is waiting on, so an ACK ends the wait rather
        # than being noticed after the retransmission deadline has already elapsed.
        self.ackSignal = {}
        # How many receptions are in flight. This was an append-only list of booleans whose end of
        # reception cleared whichever True it found first, so a packet that collided at the start
        # released a slot it never took - 941 of 8727 releases in a ten-minute thirty-node run
        # found nothing outstanding, and the ones that found a live reception cleared it.
        self.receptionsInFlight = 0
        self.isTransmitting = False
        self.usefulPackets = 0
        # Split out because an ACK is unicast and an application broadcast is not: mixing them
        # gives a reach figure whose denominator counts receivers the ACK never addressed.
        self.usefulAppPackets = 0
        self.txAirUtilization = 0
        self.dcrTxByCr = {5: 0, 6: 0, 7: 0, 8: 0}
        self.dcrAirtimeByCr = {5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0}
        self.dtpTxByPower = {}
        self.dtpTxByCrPower = {}
        self.dtpDetectedByTx = 0
        self.dtpSensedByTx = 0
        self.dtpTxCount = 0
        self.droppedByDelay = 0
        self.droppedByChannelUtil = 0
        self.deferredByChannelUtil = 0
        self.channelUtilDeferralMsec = 0.0
        self.rebroadcastPackets = 0
        self.isMoving = False
        self.gpsEnabled = False

        # Track last broadcast position/time
        self.lastBroadcastPosition = self.position.copy()
        self.lastBroadcastTime = 0

        # AirTime's two rings, and they measure different things. channelUtilization is every
        # millisecond of audible air over the last 60 s - ours and everyone else's, decoded or not,
        # which is what src/airtime.h calls "% of the last 60s busy, all three types" and what the
        # contention window is sized from. utilizationTx is our own transmissions over the last
        # hour, which is what a duty cycle binds against. Charging own transmit time to the first
        # ring and reading it where the firmware reads channel utilisation understated the figure by
        # an order of magnitude: 3.8% mean where the audible air was 43%.
        self.channelUtilization = [0.0] * self.conf.CHANNEL_UTILIZATION_PERIODS
        self.channelUtilizationIndex = 0
        self.channelUtilizationEpoch = 0.0
        # A radio has one energy detector, so overlapping signals are one busy stretch. This is how
        # far into the future the channel is already known busy; anything inside it is not charged
        # again. Without it two overlapping receptions bill the node twice and the figure runs past
        # 100% of wall-clock, which was measured at 117.5%.
        self.senseUntil = 0.0
        self.utilizationTx = [0.0] * self.conf.UTILIZATION_TX_PERIODS
        self.utilizationTxIndex = 0
        self.utilizationTxEpoch = 0.0
        if not self.is_repeater:  # repeaters don't generate messages themselves
            self.env.process(self.generate_message())
        self.env.process(self.receive(self.bc_pipe.get_output_conn()))
        self.transmitter = simpy.Resource(self.env, 1)

        # start mobility if enabled
        if self.conf.MOVEMENT_ENABLED and self.moveRng.random() <= self.conf.APPROX_RATIO_NODES_MOVING:
            self.isMoving = True
            if self.moveRng.random() <= self.conf.APPROX_RATIO_OF_NODES_MOVING_W_GPS_ENABLED:
                self.gpsEnabled = True

            # Randomly assign a movement speed
            possibleSpeeds = [
                self.conf.WALKING_METERS_PER_MIN,  # e.g.,  96 m/min
                self.conf.BIKING_METERS_PER_MIN,   # e.g., 390 m/min
                self.conf.DRIVING_METERS_PER_MIN   # e.g., 1500 m/min
            ]
            self.movementStepSize = self.moveRng.choice(possibleSpeeds)

            self.env.process(self.move_node())

    @property
    def is_router(self):
        return self.role == MESHTASTIC_ROLE.ROUTER

    @property
    def is_repeater(self):
        return self.role == MESHTASTIC_ROLE.REPEATER

    @property
    def is_client_mute(self):
        return self.role == MESHTASTIC_ROLE.CLIENT_MUTE

    def _ring_add(self, ring, index, epoch, period_ms, now, ms):
        """Add `ms` to the bucket `now` falls in, zeroing every bucket crossed since the last write.

        AirTime::syncNow, as a ring indexed by uptime phase: crossing into a bucket clears it, so a
        quiet stretch decays the window by real elapsed time rather than leaving stale airtime in it.
        """
        elapsed = int((now - epoch) // period_ms)
        if elapsed > 0:
            if elapsed >= len(ring):
                ring = [0.0] * len(ring)
                index = 0
            else:
                for _ in range(elapsed):
                    index = (index + 1) % len(ring)
                    ring[index] = 0.0
            epoch += elapsed * period_ms
        ring[index] += ms
        return ring, index, epoch

    def sense_busy(self, start, end):
        """Charge the channel-busy time this radio could actually observe over [start, end].

        The union of busy stretches, not their sum. Returns the millisecond charged.
        """
        charged = max(0.0, end - max(start, self.senseUntil))
        if end > self.senseUntil:
            self.senseUntil = end
        # Unconditional, even at zero: the call is also how the ring is rolled forward, so a quiet
        # stretch decays the window instead of leaving a stale bucket in it.
        (
            self.channelUtilization,
            self.channelUtilizationIndex,
            self.channelUtilizationEpoch,
        ) = self._ring_add(
            self.channelUtilization,
            self.channelUtilizationIndex,
            self.channelUtilizationEpoch,
            self.conf.TEN_SECONDS_INTERVAL,
            end,
            charged,
        )
        return charged

    def log_tx_airtime(self, now, ms):
        """AirTime's second ring: our own transmissions only, per minute over the last hour."""
        (
            self.utilizationTx,
            self.utilizationTxIndex,
            self.utilizationTxEpoch,
        ) = self._ring_add(
            self.utilizationTx,
            self.utilizationTxIndex,
            self.utilizationTxEpoch,
            self.conf.ONE_MIN_INTERVAL,
            now,
            ms,
        )

    def channel_utilization_percent(self) -> float:
        """AirTime::channelUtilizationPercent - the share of the last 60 s the channel was busy.

        Every millisecond of audible air, ours and everyone else's, decoded or not. Bounded by 100
        because the charge is a union: this is the figure the contention window is sized from.
        """
        self.sense_busy(self.env.now, self.env.now)  # roll the ring forward before reading it
        window_ms = self.conf.CHANNEL_UTILIZATION_PERIODS * self.conf.TEN_SECONDS_INTERVAL
        return (sum(self.channelUtilization) / window_ms) * 100.0

    def utilization_tx_percent(self) -> float:
        """AirTime::utilizationTXPercent - the share of the last hour we spent transmitting."""
        self.log_tx_airtime(self.env.now, 0.0)
        window_ms = self.conf.UTILIZATION_TX_PERIODS * self.conf.ONE_MIN_INTERVAL
        return (sum(self.utilizationTx) / window_ms) * 100.0

    def move_node(self):
        while True:

            # Pick a random direction and distance
            angle = 2 * math.pi * self.moveRng.random()
            distance = self.movementStepSize * self.moveRng.random()

            # Compute new position
            dx = distance * math.cos(angle)
            dy = distance * math.sin(angle)

            leftBound = self.conf.OX - self.conf.XSIZE / 2
            rightBound = self.conf.OX + self.conf.XSIZE / 2
            bottomBound = self.conf.OY - self.conf.YSIZE / 2
            topBound = self.conf.OY + self.conf.YSIZE / 2

            # Then in moveNode:
            new_x = min(max(self.position.x + dx, leftBound), rightBound)
            new_y = min(max(self.position.y + dy, bottomBound), topBound)

            # Update node’s position
            self.position.update_xy(new_x, new_y)
            if (
                self.conf.TERRAIN_ENABLED
                and self.conf.TERRAIN_GRID is not None
                and self.conf.NODE_Z_REFERENCE == NODE_Z_REFERENCE_SEA_LEVEL
            ):
                apply_terrain_altitude(self.conf.TERRAIN_GRID, self)

            # Moving changes who this node reaches, so its own entry is rebuilt and it is
            # added to or removed from the entries of the nodes it gained or lost.
            if self.conf.ENABLE_CONNECTIVITY_MAP:
                # may need to deepcopy if we put more complex things in here
                old_reachable_set = self.connectivity_map[self.nodeid].copy()
                new_reachable_set = set()
                for rx_node in self.nodes:
                    if rx_node.nodeid == self.nodeid:
                        continue # skip self

                    (rssi, pl) = self.node_conf.compute_rssi_and_pathloss_to(rx_node.node_conf, self.conf)

                    # compare with extra margin (set based on 10-node standard test)
                    if rssi + self.conf.CONNECTIVITY_MAP_RSSI_MARGIN > effective_sensitivity(self.conf):
                        new_reachable_set.add(rx_node.nodeid)

                    # cache path loss (it is symmetric, and static until one of the nodes moves)
                    self.baseline_pathloss_matrix[self.nodeid][rx_node.nodeid] = pl
                    self.baseline_pathloss_matrix[rx_node.nodeid][self.nodeid] = pl

                # calculate set differences to detect added and removed nodes
                lost_nodes = old_reachable_set.difference(new_reachable_set)
                gained_nodes = new_reachable_set.difference(old_reachable_set)

                logger.debug(f"{self.env.now:.3f} node {self.nodeid} moved. Connectivity change: -{len(lost_nodes)}, +{len(gained_nodes)}.")
                # TODO: -0, +0 case is very common. Skip what we can in this case.
                # update this node's connectivity map
                self.connectivity_map[self.nodeid] = new_reachable_set
                # add ourself to the connectivity map of every node we gained
                for node_id in gained_nodes:
                    self.connectivity_map[node_id].add(self.nodeid)
                # remove ourself from the connectivity map of every node we lost
                for node_id in lost_nodes:
                    self.connectivity_map[node_id].discard(self.nodeid)

                # connectivity map updated!

            if self.gpsEnabled:
                distanceTraveled = self.position.euclidean_distance(self.lastBroadcastPosition)
                logger.debug(f"{self.env.now:.3f} node {self.nodeid} checks last broadcast position distance: {distanceTraveled} from {self.lastBroadcastPosition} to {self.position}")
                timeElapsed = self.env.now - self.lastBroadcastTime
                if distanceTraveled >= self.conf.SMART_POSITION_DISTANCE_THRESHOLD and timeElapsed >= self.conf.SMART_POSITION_DISTANCE_MIN_TIME:
                    currentUtil = self.channel_utilization_percent()
                    if currentUtil < 25.0:
                        self.send_packet(NODENUM_BROADCAST, "POSITION")
                        self.lastBroadcastPosition.update_xy(self.position.x, self.position.y)
                        self.lastBroadcastTime = self.env.now
                    else:
                        logger.debug(f"{self.env.now:.3f} node {self.nodeid} SKIPS POSITION broadcast (util={currentUtil:.1f}% > 25%)")

            # Wait until next move
            nextMove = self.get_next_time(self.conf.ONE_MIN_INTERVAL)
            if nextMove >= 0:
                yield self.env.timeout(nextMove)
            else:
                break

    def send_packet(self, destId, type=""):
        """We have created a new message and wish to send it to the network
        """
        # increment the shared counter
        messageSeq = self.packetIdSeq.get()
        self.messages.append(MeshMessage(self.nodeid, destId, self.env.now, messageSeq))
        p = MeshPacket(self.conf, self.nodes, self.nodeid, destId, self.nodeid, self.conf.PACKETLENGTH, messageSeq, self.env.now, True, False, None, self.env.now, self.connectivity_map, self.baseline_pathloss_matrix)
        p.transmission_started_event = self.env.event()
        logger.debug(f"{self.env.now:.3f} Node {self.nodeid} generated {type} message {p.seq} to {destId}")
        self.packets.append(p)
        self.env.process(self.transmit(p))
        return p

    def get_next_time(self, period):
        nextGen = self.nodeRng.expovariate(1.0 / float(period))
        # do not generate message near the end of the simulation (otherwise flooding cannot finish in time)
        if self.env.now+nextGen + self.hopLimit * airtime(self.conf, self.conf.current_preset["sf"], self.conf.current_preset["cr"], self.conf.PACKETLENGTH, self.conf.current_preset["bw"]) < self.conf.SIMTIME:
            return nextGen
        return -1
    

    def release_reception(self, packet):
        """End of reception: give back the slot this packet took, if it took one."""
        if packet.rxStartedAtN[self.nodeid]:
            packet.rxStartedAtN[self.nodeid] = False
            self.receptionsInFlight = max(0, self.receptionsInFlight - 1)

    def _remember_packet(self, seq):
        """Record this message id in a bounded history, evicting the oldest as PacketHistory does."""
        self.lastHeard[seq] = self.env.now
        limit = self.conf.PACKET_HISTORY_MAX
        while len(self.lastHeard) > limit:
            oldest = min(self.lastHeard, key=self.lastHeard.get)
            del self.lastHeard[oldest]
            self.timesReceived.pop(oldest, None)

    def was_seen_recently(self, packet, ownTransmit=False):
        if packet.seq not in self.timesReceived:
            # First time we know about this packet
            self.timesReceived[packet.seq] = 0 if ownTransmit else 1
            if not ownTransmit:
                self.usefulPackets += 1
                if not packet.isAck and packet.destId in (NODENUM_BROADCAST, self.nodeid):
                    # Only a node the message was addressed to counts as reached. Overhearing a
                    # DM meant for someone else is not delivery, and pushes reach past 100%.
                    self.usefulAppPackets += 1
        else:
            self.timesReceived[packet.seq] += 0 if ownTransmit else 1
        self._remember_packet(packet.seq)


    def perhaps_cancel_dupe(self, packet):
        # Cancel if we've already seen this sequence number
        if packet.seq in self.timesReceived:
            return self.timesReceived[packet.seq] > 2 if self.is_router or self.is_repeater else self.timesReceived[packet.seq] > 1
        return False

    def latest_retry_timer_packet(self, packet):
        """Return the newest queued/generated retry attempt for this message."""
        candidates = [
            packetSent
            for packetSent in self.packets
            if packetSent.origTxNodeId == self.nodeid and packetSent.seq == packet.seq
        ]
        if not candidates:
            return packet
        return min(candidates, key=lambda packetSent: packetSent.retransmissions)

    def wait_for_retry_timer_airtime(self, packet):
        """Wait until DCR has selected the airtime used by the retry timer."""
        while self.conf.DCR_ENABLED and packet in self.packets and not packet.retryTimerAirtimeReady:
            started_event = getattr(packet, "transmission_started_event", None)
            if started_event is not None and not started_event.triggered:
                yield started_event
                continue
            yield self.env.timeout(1)

    def is_tx_allowed_channel_util(self):
        """AirTime::isTxAllowedChannelUtil - may this node originate periodic traffic right now?

        The threshold is 40%, or 25% for the polite roles, against the 60 s channel-busy share.
        """
        if not self.conf.CHANNEL_UTIL_TX_GATE_ENABLED:
            return True
        limit = (
            self.conf.CHANNEL_UTIL_POLITE_TX_LIMIT_PERCENT
            if self.conf.CHANNEL_UTIL_TX_GATE_POLITE
            else self.conf.CHANNEL_UTIL_TX_LIMIT_PERCENT
        )
        return self.channel_utilization_percent() < limit

    def signal_ack(self, seq):
        """Wake a reliable send waiting on this message id.

        The retransmission timer is a deadline, not a sleep: the firmware's pending list stops
        retransmitting the moment an ACK arrives, and the application that queued the message was
        never waiting on either.
        """
        signal = self.ackSignal.get(seq)
        if signal is not None and not signal.triggered:
            signal.succeed()

    def generate_message(self):
        """The application's own timer. Nothing downstream of it may hold it up.

        The reliable send runs as its own process, because this loop used to sit inside it: every
        message stalled its node for a full retransmission timeout - about 7.4 s at LONG_FAST -
        before the loop even looked to see whether the implicit ACK had already arrived. Offered
        load came out 8.9% under nominal on a five-node mesh and 16.9% under on a sixty-node one,
        so the load fell as the mesh grew, which is a feedback the firmware does not have.
        """
        while True:
            # Returns -1 if we don't make it before the sim ends
            nextGen = self.get_next_time(self.period)
            if nextGen < 0:
                # do not send this message anymore, since it is close to the end of the simulation
                break
            yield self.env.timeout(nextGen)

            if self.conf.DMs:
                destId = self.nodeRng.choice([i for i in range(0, len(self.nodes)) if i != self.nodeid])
            else:
                destId = NODENUM_BROADCAST

            # A shut channel-utilisation gate *delays* the send; it does not discard it.
            # PositionModule returns RUNONCE_INTERVAL before it updates lastGpsSend, and
            # DeviceTelemetry calls setLastSentToMesh only inside its successful branch - so the
            # interval stays elapsed and the message goes out as soon as the channel clears. One
            # pending send and no backlog: the next interval is measured from when this one
            # actually left, which is what not updating lastGpsSend amounts to.
            waited = 0.0
            while not self.is_tx_allowed_channel_util():
                if self.env.now + self.conf.CHANNEL_UTIL_TX_RETRY_MSEC >= self.conf.SIMTIME:
                    # The run ends before the channel clears. This is the only case that loses a
                    # message, and it is an artefact of a finite run rather than of the gate.
                    self.droppedByChannelUtil += 1
                    break
                yield self.env.timeout(self.conf.CHANNEL_UTIL_TX_RETRY_MSEC)
                waited += self.conf.CHANNEL_UTIL_TX_RETRY_MSEC
            else:
                if waited:
                    self.deferredByChannelUtil += 1
                    self.channelUtilDeferralMsec += waited
                    logger.debug(
                        f"{self.env.now:.3f} Node {self.nodeid} sends {waited:.0f} ms late: "
                        f"the channel was over the limit"
                    )
                p = self.send_packet(destId)
                if p.wantAck:
                    self.env.process(self.reliable_send(p))

    def reliable_send(self, p):
        """ReliableRouter: retransmit until the message is acknowledged or the budget runs out."""
        destId = p.destId
        signal = self.env.event()
        self.ackSignal[p.seq] = signal
        try:
            while True:
                retry_timer_packet = self.latest_retry_timer_packet(p)
                yield from self.wait_for_retry_timer_airtime(retry_timer_packet)
                if retry_timer_packet not in self.packets:
                    break
                retransmissionMsec = get_retransmission_msec(self, retry_timer_packet)
                # A deadline raced against the ACK, not a sleep taken before looking for it.
                yield self.env.timeout(retransmissionMsec) | signal
                if signal.triggered:
                    logger.debug(f"{self.env.now:.3f} Node {self.nodeid} received ACK on generated message with seq. nr. {p.seq}")
                    break

                minRetransmissions = p.maxRetransmissions
                for packetSent in self.packets:
                    if packetSent.origTxNodeId == self.nodeid and packetSent.seq == p.seq:
                        if packetSent.retransmissions < minRetransmissions:
                            minRetransmissions = packetSent.retransmissions
                if minRetransmissions > 0:  # generate new packet with same sequence number
                    pNew = MeshPacket(self.conf, self.nodes, self.nodeid, p.destId, self.nodeid, p.packetLen, p.seq, p.genTime, p.wantAck, False, None, self.env.now, self.connectivity_map, self.baseline_pathloss_matrix)
                    pNew.transmission_started_event = self.env.event()
                    pNew.retransmissions = minRetransmissions - 1
                    logger.debug(f"{self.env.now:.3f} Node {self.nodeid} wants to retransmit its generated packet to {destId} with seq.nr. {p.seq} minRetransmissions {minRetransmissions}")
                    self.packets.append(pNew)
                    self.env.process(self.transmit(pNew))
                    p = pNew
                else:
                    logger.debug(f"{self.env.now:.3f} Node {self.nodeid} reliable send of {p.seq} failed.")
                    break
        finally:
            self.ackSignal.pop(p.seq, None)

    def transmit(self, packet):
        with self.transmitter.request() as request:
            yield request

            # listen-before-talk from src/mesh/RadioLibInterface.cpp
            txTime = set_transmit_delay(self, packet)
            logger.debug(f"{self.env.now:.3f} Node {self.nodeid} schedules tx. Picked wait time {txTime}")
            yield self.env.timeout(txTime)

            # wait when currently receiving or transmitting, or channel is active
            while self.receptionsInFlight or self.isTransmitting or is_channel_active(self, self.env):
                logger.debug(f"{self.env.now:.3f} Node {self.nodeid} delaying tx: busy Tx-ing {self.isTransmitting=} or Rx-ing {self.receptionsInFlight=}, else channel busy!")
                txTime = set_transmit_delay(self, packet)
                yield self.env.timeout(txTime)
            logger.debug(f"{self.env.now:.3f} Node {self.nodeid} ends waiting for scheduled tx")

            # check if you received an ACK for this message in the meantime
            self.was_seen_recently(packet, ownTransmit=True)
            if not self.perhaps_cancel_dupe(packet):  # if you did not receive an ACK for this message in the meantime
                # Firmware DCR runs very late too: after queue/LBT waiting, but
                # before airtime accounting and packet start/end timestamps.
                decision = choose_dynamic_coding_rate(self, packet)
                if decision.cr != packet.cr:
                    packet.set_coding_rate(decision.cr)
                packet.retryTimerAirtimeReady = True
                logger.debug(
                    f"{self.env.now:.3f} Node {self.nodeid} DCR selected CR 4/{packet.cr} for packet {packet.seq}: {decision.reason}"
                )
                if hasattr(packet, "transmission_started_event") and not packet.transmission_started_event.triggered:
                    packet.transmission_started_event.succeed(packet)

                power_decision = choose_dynamic_tx_power(self, packet)
                if power_decision.tx_power_dbm != packet.txpow:
                    packet.set_tx_power(power_decision.tx_power_dbm)
                logger.debug(
                    f"{self.env.now:.3f} Node {self.nodeid} DTP selected {packet.txpow} dBm for packet {packet.seq}: {power_decision.reason}"
                )

                logger.debug(f"{self.env.now:.3f} Node {self.nodeid} started low level send {packet.unique_packet_seq} for msg {packet.seq} hopLimit {packet.hopLimit} original Tx {packet.origTxNodeId}")
                self.nrPacketsSent += 1
                packet.startTime = self.env.now
                packet.endTime = self.env.now + packet.timeOnAir
                rx_node_ids = packet.detected_node_ids if self.conf.CAPTURE_COLLISION_MODEL_ENABLED else packet.sensed_node_ids
                for rx_node_id in rx_node_ids:
                    collision = check_collision(self.conf, self.env, packet, rx_node_id, self.packetsAtN)
                    if self.conf.CAPTURE_COLLISION_MODEL_ENABLED:
                        # Even a packet that cannot be decoded is still RF
                        # energy on the channel and may jam later packets.
                        self.packetsAtN[rx_node_id].append(packet)
                    elif collision == 0:
                        self.packetsAtN[rx_node_id].append(packet)
                self.txAirUtilization += packet.timeOnAir
                self.log_tx_airtime(packet.endTime, packet.timeOnAir)
                # Every radio that could detect this transmission spends that stretch with a busy
                # channel, whether or not it decodes the frame - energy detection does not care.
                # Charged from here, once, rather than in each receiver's own path: a receiver below
                # the demodulation threshold never reaches that path, and a receiver that collided
                # reached it twice.
                self.sense_busy(packet.startTime, packet.endTime)
                for rx_node_id in packet.detected_node_ids:
                    self.nodes[rx_node_id].sense_busy(packet.startTime, packet.endTime)
                self.dcrTxByCr[packet.cr] = self.dcrTxByCr.get(packet.cr, 0) + 1
                self.dcrAirtimeByCr[packet.cr] = self.dcrAirtimeByCr.get(packet.cr, 0.0) + packet.timeOnAir
                self.dtpTxByPower[packet.txpow] = self.dtpTxByPower.get(packet.txpow, 0) + 1
                cr_power_key = f"{packet.cr}@{packet.txpow}"
                self.dtpTxByCrPower[cr_power_key] = self.dtpTxByCrPower.get(cr_power_key, 0) + 1
                self.dtpDetectedByTx += sum(1 for detected in packet.detectedByN if detected)
                self.dtpSensedByTx += sum(1 for sensed in packet.sensedByN if sensed)
                self.dtpTxCount += 1
                self.bc_pipe.put(packet) # queue for nodes to receive packet
                self.isTransmitting = True
                yield self.env.timeout(packet.timeOnAir)
                self.isTransmitting = False
            else:  # received ACK: abort transmit, remove from packets generated
                logger.debug(f"{self.env.now:.3f} Node {self.nodeid} in the meantime received ACK, abort packet with seq. nr {packet.unique_packet_seq} for msg {packet.seq}")
                if hasattr(packet, "transmission_started_event") and not packet.transmission_started_event.triggered:
                    packet.transmission_started_event.succeed(packet)
                self.packets.remove(packet)

    def receive(self, in_pipe):
        while True:
            p = yield in_pipe.get()
            packet_log_id = getattr(p, "unique_packet_seq", p.seq)

            logger.debug(f"{self.env.now:.3f} Node {self.nodeid} fetches packet {packet_log_id} for msg {p.seq} from {p.txNodeId} from bc_pipe: sensed: {p.sensedByN[self.nodeid]} collided: {p.collidedAtN[self.nodeid]} on air: {p.onAirToN[self.nodeid]}")

            if self.conf.CAPTURE_COLLISION_MODEL_ENABLED:
                if p.sensedByN[self.nodeid] and p.onAirToN[self.nodeid]:
                    p.onAirToN[self.nodeid] = False
                    if not self.isTransmitting and not p.collidedAtN[self.nodeid]:
                        logger.debug(f"{self.env.now:.3f} Node {self.nodeid} started receiving packet {packet_log_id} for msg {p.seq} from {p.txNodeId}")
                        p.rxStartedAtN[self.nodeid] = True
                        self.receptionsInFlight += 1
                    elif self.isTransmitting:
                        logger.debug(f"{self.env.now:.3f} Node {self.nodeid} could not lock packet {p.seq}.")
                        p.sensedByN[self.nodeid] = False
                    else:
                        logger.debug(f"{self.env.now:.3f} Node {self.nodeid} could not lock packet {packet_log_id} for msg {p.seq}.")
                    continue

                if p.sensedByN[self.nodeid]:
                    self.release_reception(p)
                    if p.collidedAtN[self.nodeid]:
                        logger.debug(f"{self.env.now:.3f} Node {self.nodeid} could not decode packet {packet_log_id}.")
                        continue
                    if p.phyLostAtN[self.nodeid]:
                        logger.debug(f"{self.env.now:.3f} Node {self.nodeid} lost packet {packet_log_id} for msg {p.seq} to weak-link PHY errors.")
                        continue
                    p.receivedAtN[self.nodeid] = True
                    logger.debug(f"{self.env.now:.3f} Node {self.nodeid} received packet {packet_log_id} for msg {p.seq} with delay {round(self.env.now - p.genTime, 2)}")
                    self.handle_received_packet(p)
                continue

            if p.sensedByN[self.nodeid] and p.onAirToN[self.nodeid]:  # start of reception
                if p.collidedAtN[self.nodeid]:
                    # This packet collided, so we can sense it but not decode
                    # it. Mark it as no-longer on air and leave further
                    # processing to the end-of-transmission branch.
                    p.onAirToN[self.nodeid] = False
                elif not self.isTransmitting:
                    logger.debug(f"{self.env.now:.3f} Node {self.nodeid} started receiving packet {packet_log_id} for msg {p.seq} from {p.txNodeId}")
                    p.onAirToN[self.nodeid] = False
                    p.rxStartedAtN[self.nodeid] = True
                    self.receptionsInFlight += 1
                else:  # if you were currently transmitting, you could not have sensed it
                    logger.debug(f"{self.env.now:.3f} Node {self.nodeid} was transmitting, so could not receive packet {packet_log_id} for msg {p.seq}")
                    p.sensedByN[self.nodeid] = False
                    p.onAirToN[self.nodeid] = False
            elif p.sensedByN[self.nodeid]:  # end of reception
                self.release_reception(p)
                # begin receiving packet fine, but a collision begins before we finish receiving.
                if p.collidedAtN[self.nodeid]:
                    logger.debug(f"{self.env.now:.3f} Node {self.nodeid} could not decode packet {packet_log_id}.")
                    continue
                if p.phyLostAtN[self.nodeid]:
                    logger.debug(f"{self.env.now:.3f} Node {self.nodeid} lost packet {packet_log_id} for msg {p.seq} to weak-link PHY errors.")
                    continue
                p.receivedAtN[self.nodeid] = True
                logger.debug(f"{self.env.now:.3f} Node {self.nodeid} received packet {packet_log_id} for msg {p.seq} with delay {round(self.env.now - p.genTime, 2)}") # TODO: better way to calculate delay for log
                self.handle_received_packet(p)

    def handle_received_packet(self, p):
        """Handle decoded MeshPacket after RX PHY/collision checks pass."""
        self.delays.append(self.env.now - p.genTime)

        # Update history of received packets
        self.was_seen_recently(p)

        # check if implicit ACK for own generated message
        if p.origTxNodeId == self.nodeid:
            if p.isAck:
                logger.debug(f"Node {self.nodeid} received real ACK on generated message.")
            else:
                logger.debug(f"Node {self.nodeid} received implicit ACK on message sent.")
            p.ackReceived = True
            self.signal_ack(p.seq)
            return

        ackReceived = False
        realAckReceived = False
        for sentPacket in self.packets:
            # check if ACK for message you currently have in queue
            if sentPacket.txNodeId == self.nodeid and sentPacket.seq == p.seq:
                logger.debug(f"{self.env.now:.3f} Node {self.nodeid} received implicit ACK for message in queue.")
                ackReceived = True
                sentPacket.ackReceived = True
                self.signal_ack(sentPacket.seq)
            # check if real ACK for message sent
            if sentPacket.origTxNodeId == self.nodeid and p.isAck and sentPacket.seq == p.requestId:
                logger.debug(f"{self.env.now:.3f} Node {self.nodeid} received real ACK.")
                realAckReceived = True
                sentPacket.ackReceived = True
                self.signal_ack(sentPacket.seq)

        # send real ACK if you are the destination and you did not yet send the ACK
        if p.wantAck and p.destId == self.nodeid and not any(pA.requestId == p.seq for pA in self.packets):
            logger.debug(f"{self.env.now:.3f} Node {self.nodeid} sends a flooding ACK.")
            messageSeq = self.packetIdSeq.get()
            self.messages.append(MeshMessage(self.nodeid, p.origTxNodeId, self.env.now, messageSeq))
            pAck = MeshPacket(self.conf, self.nodes, self.nodeid, p.origTxNodeId, self.nodeid, self.conf.ACKLENGTH, messageSeq, self.env.now, False, True, p.seq, self.env.now, self.connectivity_map, self.baseline_pathloss_matrix)
            pAck.priorHopRssi = p.rssiAtN[self.nodeid]
            pAck.priorHopSnr = estimate_snr(self.conf, pAck.priorHopRssi)
            self.packets.append(pAck)
            self.env.process(self.transmit(pAck))
        # Rebroadcasting Logic for received message. This is a broadcast or a DM not meant for us.
        elif not p.destId == self.nodeid and not ackReceived and not realAckReceived and p.hopLimit > 0:
            self.my_stats.packetsHeard += 1 # packets which could potentially be rebroadcast
            # FloodingRouter: rebroadcast received packet
            if self.conf.SELECTED_ROUTER_TYPE == self.conf.ROUTER_TYPE.MANAGED_FLOOD:
                if not self.is_client_mute:
                    logger.debug(f"{self.env.now:.3f} Node {self.nodeid} schedules rebroadcast for received packet {p.unique_packet_seq} for msg {p.seq}")
                    self.my_stats.packetsRebroadcast += 1
                    pNew = MeshPacket(self.conf, self.nodes, p.origTxNodeId, p.destId, self.nodeid, p.packetLen, p.seq, p.genTime, p.wantAck, False, None, self.env.now, self.connectivity_map, self.baseline_pathloss_matrix)
                    pNew.hopLimit = p.hopLimit - 1
                    pNew.priorHopRssi = p.rssiAtN[self.nodeid]
                    pNew.priorHopSnr = estimate_snr(self.conf, pNew.priorHopRssi)
                    self.packets.append(pNew)
                    self.env.process(self.transmit(pNew))
        else:
            self.droppedByDelay += 1

    def get_stats(self) -> MeshNodeStats:
        """Get internally-tracked statistics/data. Only valid after the sim ends.
        """
        return self.my_stats

def default_generate_node_list(conf: Config) -> [NodeConfig]:
    """Randomly choose node configurations for a run, from the config's node count."""
    # need to identically match RNG usage right now to pass the discrete sim
    # test. If we want to change the reference test, do that in a smaller change.

    node_configs = []

    # replicate default 'no prior config' setup:
    for i in range(conf.NR_NODES):
        # no specified node config, randomly generate one
        # get node's position
        x, y = find_random_position(conf, node_configs)
        z = conf.HM
        position = Point(x, y, z)

        # role
        isRouter = conf.router

        # map misc. booleans into single role
        if isRouter:
            role = MESHTASTIC_ROLE.ROUTER
        else:
            role = MESHTASTIC_ROLE.CLIENT

        # make NodeConfig object to pass to MeshNode constructor
        node_configs.append(NodeConfig(i, position, conf.PERIOD, conf.PTX, conf.FREQ, role))

    return node_configs
