import logging

from lib.phy import airtime, estimate_path_loss

NODENUM_BROADCAST = 0xFFFFFFFF

logger = logging.getLogger(__name__)

class MeshPacket:
    def __init__(self, conf, nodes, origTxNodeId, destId, txNodeId, plen, seq, genTime, wantAck, isAck, requestId, now, connectivity_map):
        """Create a new packet and calculate which nodes sense and receive it

        Arguments:
        conf -- simulation Config
        nodes -- set of all nodes in the simulation. For calculating which nodes receive the packet
        origTxNodeId -- ID of originating node
        destId -- ID of destination node (specific node or broadcast)
        txNodeId -- ID of currently transmitting node
        plen -- packet length
        seq -- message sequence number
        genTime -- sim time of original packet generation (different from acks/rebroadcasts)
        wantAck -- this packet wants an ACK
        isAck -- this packet is an ACK packet
        requestId -- ID of packet requesting ACK (only valid for ACK packets)
        now -- current sim time when called, always `env.now`
        connectivity_map -- map of nodeid -> set of reachable nodeids
        """
        self.conf = conf
        self.origTxNodeId = origTxNodeId
        self.destId = destId
        self.txNodeId = txNodeId
        self.wantAck = wantAck
        self.isAck = isAck
        self.seq = seq
        self.requestId = requestId
        self.genTime = genTime
        self.now = now
        self.txpow = self.conf.PTX
        self.LplAtN = [0 for _ in range(self.conf.NR_NODES)]
        self.rssiAtN = [0 for _ in range(self.conf.NR_NODES)]
        self.sensedByN = [False for _ in range(self.conf.NR_NODES)]
        self.detectedByN = [False for _ in range(self.conf.NR_NODES)]
        self.collidedAtN = [False for _ in range(self.conf.NR_NODES)]
        self.receivedAtN = [False for _ in range(self.conf.NR_NODES)]
        self.onAirToN = [True for _ in range(self.conf.NR_NODES)]

        # configuration values
        self.sf = self.conf.current_preset["sf"]
        self.cr = self.conf.current_preset["cr"]
        self.bw = self.conf.current_preset["bw"]
        self.freq = self.conf.FREQ
        self.tx_node = next(n for n in nodes if n.nodeid == self.txNodeId)
        # calculate reception at all other nodes
        for rx_node in nodes:
            if rx_node.nodeid == self.txNodeId:
                continue

            # reduce calculations just to plausibly reachable nodes. This is initialized
            # before sim start, and updated whenever a moving node's position is updated,
            # so is always an accurate map of what nodes could (with extra margin) even
            # sense each other.
            if not connectivity_map[self.txNodeId].__contains__(rx_node.nodeid):
                logger.debug(f"skipping {self.txNodeId} -> {rx_node.nodeid} computation. connectivity map: {connectivity_map[self.txNodeId]}")
                continue
                #pass # swap the comments on the pass/continue to skip the optimization, accepting a bit of overhead.

            dist_3d = self.tx_node.position.euclidean_distance(rx_node.position)
            offset = self.conf.LINK_OFFSET[(self.txNodeId, rx_node.nodeid)]
            self.LplAtN[rx_node.nodeid] = estimate_path_loss(self.conf, dist_3d, self.freq, self.tx_node.position.z, rx_node.position.z) + offset
            self.rssiAtN[rx_node.nodeid] = self.txpow + self.tx_node.antennaGain + rx_node.antennaGain - self.LplAtN[rx_node.nodeid]
            if self.rssiAtN[rx_node.nodeid] >= self.conf.current_preset["sensitivity"]:
                self.sensedByN[rx_node.nodeid] = True
            if self.rssiAtN[rx_node.nodeid] >= self.conf.current_preset["cad_threshold"]:
                self.detectedByN[rx_node.nodeid] = True

        self.packetLen = plen
        self.timeOnAir = airtime(self.conf, self.sf, self.cr, self.packetLen, self.bw)
        self.startTime = 0
        self.endTime = 0

        # Routing
        self.retransmissions = self.conf.maxRetransmission
        self.ackReceived = False
        self.hopLimit = self.tx_node.hopLimit


class MeshMessage:
    def __init__(self, origTxNodeId, destId, genTime, seq):
        self.origTxNodeId = origTxNodeId
        self.destId = destId
        self.genTime = genTime
        self.seq = seq
        self.endTime = 0
