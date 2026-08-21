import copy
import logging
from typing import TYPE_CHECKING

# probably not necessary, but "Environment" seemed too generic to me
from simpy import Environment as SimpyEnvironment
import numpy as np

from lib.common import setup_asymmetric_links
from lib.config import Config
from lib.discrete_event_sim_components import SimulationState, SimulationDataTracking
from lib.node import MeshNode, NodeConfig

if TYPE_CHECKING:
    from lib.gui import Graph
from lib.packet import MeshPacket
from lib.phy import estimate_path_loss

logger = logging.getLogger(__name__)

BROADCAST_DEST_ID = 0xFFFFFFFF


def count_populations(conf, packets):
    """Separate the things a mesh run counts, which are not interchangeable.

    A transmission is not a message and an ACK is not a broadcast - see docs/metrics.md.
    """
    app_seqs, ack_seqs, originated = set(), set(), set()
    rebroadcasts = retransmissions = 0
    receiver_opportunities = app_receiver_opportunities = 0
    others = max(conf.NR_NODES - 1, 0)

    for packet in packets:
        addressed = others if packet.destId == BROADCAST_DEST_ID else 1
        receiver_opportunities += addressed
        if packet.isAck:
            ack_seqs.add(packet.seq)
        else:
            if packet.seq not in app_seqs:
                app_receiver_opportunities += addressed
            app_seqs.add(packet.seq)
        if packet.txNodeId != packet.origTxNodeId:
            rebroadcasts += 1
        elif packet.seq in originated:
            retransmissions += 1
        else:
            originated.add(packet.seq)

    return {
        "appMessages": len(app_seqs),
        "ackMessages": len(ack_seqs),
        "uniquePacketIds": len(app_seqs | ack_seqs),
        "transmissions": len(packets),
        "rebroadcasts": rebroadcasts,
        "retransmissions": retransmissions,
        "receiverOpportunities": receiver_opportunities,
        "appReceiverOpportunities": app_receiver_opportunities,
    }


class SimulationResults:
    """Everything a run measured, for a reporter to present however it likes.

    Mostly a dictionary with extra features.
    """
    def __init__(self, results: dict):
        """Seed with the run's first-order results. Many keys are assumed to exist."""
        self.results = results.copy() # only a shallow copy

    def __getitem__(self, subscript: str):
        """Subscript access, letting KeyError bubble up to the caller."""
        return self.results[subscript]

    def finalize(self, conf: Config):
        """Derive the second-order results - averages, rates, populations - once a run ends.

        Rates stay raw ratios: 0.5 is 50%. See docs/metrics.md for what each population counts.
        """
        # replicate result enrichment/calculation from loraMesh.py and batchSim.py
        nodes = self.results["nodes"]
        packets = self.results["packets"]
        sent = len(packets)
        self.results["sent"] = sent
        self.results.update(count_populations(conf, packets))
        self.results["potentialReceivers"] = self.results["receiverOpportunities"]

        # TODO: inefficient. Have nodes keep counters for these and just collect them
        self.results["nrCollisions"] = sum([1 for p in packets for n in nodes if p.collidedAtN[n.nodeid] is True])
        self.results["nrSensed"] = sum([1 for p in packets for n in nodes if p.sensedByN[n.nodeid] is True])
        self.results["nrReceived"] = sum([1 for p in packets for n in nodes if p.receivedAtN[n.nodeid] is True])
        self.results["nrPhyLoss"] = sum([
            1
            for p in packets
            for n in nodes
            if n.nodeid < len(getattr(p, "phyLostAtN", []))
            and p.phyLostAtN[n.nodeid] is True
            and p.sensedByN[n.nodeid] is True
            and p.collidedAtN[n.nodeid] is False
        ])
        collision_reasons = {}
        for p in packets:
            for reason in getattr(p, "collisionReasonAtN", []):
                if reason:
                    collision_reasons[reason] = collision_reasons.get(reason, 0) + 1
        self.results["collisionReasons"] = collision_reasons
        terrain_losses = [
            p.terrainLossAtN[n.nodeid]
            for p in packets
            for n in nodes
            if n.nodeid < len(getattr(p, "terrainLossAtN", [])) and p.terrainLossAtN[n.nodeid] > 0
        ]
        self.results["meanTerrainLossDb"] = float(np.nanmean(terrain_losses)) if terrain_losses else 0.0
        self.results["maxTerrainLossDb"] = max(terrain_losses) if terrain_losses else 0.0
        clutter_losses = [
            p.clutterLossAtN[n.nodeid]
            for p in packets
            for n in nodes
            if n.nodeid < len(getattr(p, "clutterLossAtN", [])) and p.clutterLossAtN[n.nodeid] > 0
        ]
        self.results["meanClutterLossDb"] = float(np.nanmean(clutter_losses)) if clutter_losses else 0.0
        self.results["maxClutterLossDb"] = max(clutter_losses) if clutter_losses else 0.0
        self.results["nrUseful"] = sum([n.usefulPackets for n in nodes])
        self.results["uniqueAppDeliveries"] = sum([n.usefulAppPackets for n in nodes])

        self.results["meanDelay"] = np.nanmean(self.results["delays"]) if self.results["delays"] else np.nan

        # various division-by-0 guarded calculations
        if conf.NR_NODES != 0 and conf.SIMTIME != 0:
            self.results["txAirUtilizationRate"] = sum([n.txAirUtilization for n in nodes])/conf.NR_NODES/conf.SIMTIME
        else:
            self.results["txAirUtilizationRate"] = np.nan

        if self.results["nrSensed"] != 0:
            self.results["collisionRate"] = self.results["nrCollisions"]/self.results["nrSensed"]
        else:
            self.results["collisionRate"] = np.nan

        # Reach is application traffic only, over the receivers those messages actually addressed:
        # a broadcast addresses every other node, a DM addresses one, and an ACK is not a message.
        if self.results["appReceiverOpportunities"] > 0:
            self.results["nodeReach"] = (
                self.results["uniqueAppDeliveries"] / self.results["appReceiverOpportunities"]
            )
        else:
            self.results["nodeReach"] = np.nan

        if self.results["nrReceived"] != 0:
            usefulness = self.results["nrUseful"]/self.results["nrReceived"]  # nr of packets that delivered to a packet to a new receiver out of all packets sent
            self.results["usefulness"] = usefulness
        else:
            self.results["usefulness"] = np.nan

        # A channel cannot be busy more than all the time. The figure that used to drive the
        # contention window broke this at 117.5%; reporting it makes the invariant assertable.
        chutil = sorted(n.channel_utilization_percent() for n in nodes)
        if chutil:
            self.results["nodeChannelUtilPercent"] = {
                "mean": float(np.mean(chutil)),
                "p90": chutil[min(len(chutil) - 1, int(0.9 * len(chutil)))],
                "max": chutil[-1],
            }
            self.results["nodeUtilizationTxPercent"] = {
                "mean": float(np.mean([n.utilization_tx_percent() for n in nodes])),
                "max": max(n.utilization_tx_percent() for n in nodes),
            }
        else:
            self.results["nodeChannelUtilPercent"] = {"mean": np.nan, "p90": np.nan, "max": np.nan}
            self.results["nodeUtilizationTxPercent"] = {"mean": np.nan, "max": np.nan}

        self.results["delayDropped"] = sum(n.droppedByDelay for n in nodes)
        self.results["dcrTxByCr"] = {
            cr: sum(getattr(n, "dcrTxByCr", {}).get(cr, 0) for n in nodes)
            for cr in (5, 6, 7, 8)
        }
        self.results["dcrAirtimeByCr"] = {
            cr: sum(getattr(n, "dcrAirtimeByCr", {}).get(cr, 0.0) for n in nodes)
            for cr in (5, 6, 7, 8)
        }
        dtp_tx_count = sum(getattr(n, "dtpTxCount", 0) for n in nodes)
        self.results["dtpTxByPower"] = {}
        self.results["dtpTxByCrPower"] = {}
        for n in nodes:
            for power, count in getattr(n, "dtpTxByPower", {}).items():
                self.results["dtpTxByPower"][power] = self.results["dtpTxByPower"].get(power, 0) + count
            for cr_power, count in getattr(n, "dtpTxByCrPower", {}).items():
                self.results["dtpTxByCrPower"][cr_power] = self.results["dtpTxByCrPower"].get(cr_power, 0) + count
        self.results["dtpMeanDetectedByTx"] = (
            sum(getattr(n, "dtpDetectedByTx", 0) for n in nodes) / dtp_tx_count if dtp_tx_count else 0.0
        )
        self.results["dtpMeanSensedByTx"] = (
            sum(getattr(n, "dtpSensedByTx", 0) for n in nodes) / dtp_tx_count if dtp_tx_count else 0.0
        )

        if self.results["totalPairs"] != 0:
            noLinkRate = self.results["noLinks"] / self.results["totalPairs"]
            self.results["noLinkRate"] = noLinkRate

        if conf.MOVEMENT_ENABLED:
            self.results["movingNodes"] = sum([1 for n in nodes if n.isMoving is True])
            self.results["gpsEnabled"] = sum([1 for n in nodes if n.gpsEnabled is True])

class DiscreteEventSim:
    """Class for a full Discrete Event Simulation. Contains
    simulation config, all necessary state, and sim plumbing.
    """

    def __init__(self, conf: Config, node_configs: [NodeConfig], graph: "Graph | None" = None):
        """Build a run from parse_params' node configurations.

        Passing `graph` turns the GUI on; without it the run is headless.
        """

        # set constant state/initial state from parameters
        self.env = SimpyEnvironment()
        self.conf = copy.deepcopy(conf) # have our own copy so our setup_asymmetric_links doesn't change whatever config we've been passed.
        self.node_configs = node_configs

        # reset MeshPacket class variables
        MeshPacket.seed_asym_rng(self.conf.SEED)
        MeshPacket.reset_packet_counter()

        # internal global state which changes
        self.mutated_state = SimulationState(self.conf, self.env)

        # stats & data tracking
        self.data_tracking = SimulationDataTracking()

        # note: we allow user to specify if graphing will happen or not
        self.graph = graph

        # Always precomputed: the link/no-link counts are reported either way, and they
        # cost the same O(n^2) pass, so only the later map lookups are configurable.
        setup_asymmetric_links(self.conf, self.node_configs)
        self.initialize_connectivity_map()

        # node configs provided, create nodes with them
        for cfg in self.node_configs:
            n = MeshNode(self.conf,
                self.mutated_state,
                self.data_tracking,
                cfg
            )
            self.mutated_state.nodes.append(n)

        if self.graph is not None:
            for n in self.mutated_state.nodes:
                self.graph.add_node(n)

        logger.debug(f"connectivity map: {self.mutated_state.connectivity_map}")

        if self.graph is not None and self.conf.MOVEMENT_ENABLED:
            # Not covered by tests, which never build a GUI. TODO: this could be wired in
            # externally instead, the way batchSim adds its progress process.
            from lib.gui import run_graph_updates

            self.env.process(run_graph_updates(self.env, self.graph, self.mutated_state.nodes, self.conf.ONE_MIN_INTERVAL))
        self.conf.update_router_dependencies()

    def run_simulation(self):
        self.env.run(until=self.conf.SIMTIME)

    def get_env(self) -> SimpyEnvironment:
        """The run's SimPy Environment, for adding processes of your own to it."""
        return self.env

    def get_results(self) -> SimulationResults:
        # TODO: is it possible to add a check that the sim has finished running?

        # expect to use this very soon
        #node_stats = [n.get_stats() for n in self.mutated_state.nodes]

        first_order_results = {
            "packets": self.mutated_state.packets,
            "packetsAtN": self.mutated_state.packetsAtN,
            "packetIdsIssued": self.mutated_state.packetIdSeq.peek(),
            "messages": self.data_tracking.messages,
            "delays": self.data_tracking.delays,
            "totalPairs": self.data_tracking.totalPairs,
            "noLinks": self.data_tracking.noLinks,
            "nodes": self.mutated_state.nodes,
        }
        results = SimulationResults(first_order_results)
        results.finalize(self.conf)

        return results

    def initialize_connectivity_map(self):
        '''use node configs to compute the initial connectivity map for later
        lookups. Also, initialize baseline path loss matrix.
        '''
        for tx_node in self.node_configs:
            # compute the set of all nodes our signal is detectable at
            reachable_node_set = set()
            for rx_node in self.node_configs:
                if tx_node.node_id == rx_node.node_id:
                    continue # skip self

                self.data_tracking.totalPairs += 1

                (rssi, pl) = tx_node.compute_rssi_and_pathloss_to(rx_node, self.conf)

                # compare with extra margin (set based on 10-node standard test)
                if rssi + self.conf.CONNECTIVITY_MAP_RSSI_MARGIN > self.conf.current_preset['sensitivity']:
                    reachable_node_set.add(rx_node.node_id)

                # compute total/no links without margin
                if rssi >= self.conf.current_preset['sensitivity']:
                    self.data_tracking.totalLinks += 1
                else:
                    self.data_tracking.noLinks += 1

                # cache path loss (it is symmetric, and static until one of the nodes moves)
                self.mutated_state.baseline_pathloss_matrix[tx_node.node_id][rx_node.node_id] = pl
                self.mutated_state.baseline_pathloss_matrix[rx_node.node_id][tx_node.node_id] = pl

            self.mutated_state.connectivity_map[tx_node.node_id] = reachable_node_set
