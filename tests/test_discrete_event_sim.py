import random
import unittest

import lib.discrete_event_sim

class TestDiscreteEventSim(unittest.TestCase):
    """A 10-node default run, as if `loraMesh.py 10`, checked against known-good numbers.

    A change that moves them is either a bug or an improvement; decide which, then update these.
    """
    # TODO: add many more tests for SimulationResults, especially finalize method

    def test_simulation_results_finalization(self):
        """finalize() assumes a lot of keys exist and derives a lot from them.

        Mock nodes and packets, since it wants lists of MeshNode and MeshPacket.
        """
        from lib.config import CONFIG
        conf = CONFIG

        # The mocks below are the contract: what finalize() reads off a node and a packet.
        # What it computes from them is in docs/metrics.md; rates may be nan on an empty run.

        class MockNode:
            def __init__(self, nodeid: int):
                self.nodeid = nodeid
                self.usefulPackets = 0
                self.usefulAppPackets = 0
                self.txAirUtilization = 0.0
                self.droppedByDelay = 0
                self.isMoving = False
                self.gpsEnabled = False
                self.dcrTxByCr = {5: 0, 6: 0, 7: 0, 8: 0}
                self.dcrAirtimeByCr = {5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0}
                self.dtpTxByPower = {}
                self.dtpTxByCrPower = {}
                self.dtpDetectedByTx = 0
                self.dtpSensedByTx = 0
                self.dtpTxCount = 0

            def channel_utilization_percent(self):
                return 0.0

            def utilization_tx_percent(self):
                return 0.0

        class MockPacket:
            def __init__(self, num_nodes: int, seq: int = 0):
                self.collidedAtN = [False for _ in range(num_nodes)]
                self.sensedByN = [False for _ in range(num_nodes)]
                self.receivedAtN = [False for _ in range(num_nodes)]
                # An original application broadcast: not an ACK, not relayed by anyone else.
                self.seq = seq
                self.isAck = False
                self.destId = 0xFFFFFFFF
                self.txNodeId = 0
                self.origTxNodeId = 0

        # Three nodes that all hear each other, 10 broadcast messages and 10 packets,
        # on the default config: moving nodes, asymmetric links, no DMs.
        conf.NR_NODES = 3
        mock_nodes = [MockNode(i) for i in range(3)]
        mock_nodes[0].isMoving = True
        mock_nodes[0].gpsEnabled = True
        for n in mock_nodes:
            # just put some non-zero values in there
            n.usefulPackets = 10
            n.usefulAppPackets = 10
            n.txAirUtilization = 1.0

        mock_packets = [MockPacket(3, seq=i) for i in range(10)]
        # all packets were sensed by all nodes, no collisions (fudging it)
        for p in mock_packets:
            for i in range(3):
                p.sensedByN[i] = True
                p.receivedAtN[i] = True

        r = {}
        r['nodes'] = mock_nodes
        r['packets'] = mock_packets
        r['delays'] = [1.0 for _ in range(10)]
        r['packetIdsIssued'] = 10 # ids allocated, messages and ACKs alike

        r['totalPairs'] = 3
        r['noLinks'] = 0

        sim_results = lib.discrete_event_sim.SimulationResults(r)
        sim_results.finalize(conf)

        # test computations done by finalize, sanity checks

        # keys exist AND are specific good values
        self.assertEqual(sim_results['potentialReceivers'], len(mock_packets) * (conf.NR_NODES - 1), "expected calculation of potential receivers (no DMs)")
        self.assertEqual(sim_results['sent'], len(mock_packets), 'expected calculation of sent packets')
        self.assertEqual(sim_results['nrCollisions'], 0, 'expected nr of collisions')
        self.assertEqual(sim_results['nrSensed'], 30, 'expected nr of sensed packets')
        self.assertEqual(sim_results['nrReceived'], 30, 'expected nr of received packets')
        self.assertEqual(sim_results['nrUseful'], 30, 'expected nr of useful packets')
        self.assertEqual(sim_results['meanDelay'], 1.0, 'expected mean delay')
        self.assertEqual(sim_results['collisionRate'], 0, 'expected calculated collisionRate')
        self.assertEqual(sim_results['usefulness'], 1, 'usefulness is created')
        self.assertEqual(sim_results['delayDropped'], 0, 'expected number of delayDropped')
        self.assertEqual(sim_results['dcrTxByCr'], {5: 0, 6: 0, 7: 0, 8: 0}, 'expected DCR histogram')
        self.assertEqual(sim_results['dcrAirtimeByCr'], {5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0}, 'expected DCR airtime histogram')
        self.assertEqual(sim_results['dtpTxByPower'], {}, 'expected DTP power histogram')
        self.assertEqual(sim_results['dtpTxByCrPower'], {}, 'expected DTP CR/power histogram')
        self.assertEqual(sim_results['dtpMeanDetectedByTx'], 0.0, 'expected DTP detected mean')
        self.assertEqual(sim_results['dtpMeanSensedByTx'], 0.0, 'expected DTP sensed mean')

        # keys exist, not currently checking values
        self.assertIsNotNone(sim_results['txAirUtilizationRate'], 'txAirUtilizationRate is created')
        self.assertIsNotNone(sim_results['nodeReach'], 'nodeReach is created')
        #self.assertIsNotNone(sim_results['x'], 'x is created')

        # check rate calculations in [0, 1] (assuming we mocked sane values)
        self.assertLessEqual(0.0, sim_results['noLinkRate'], 'calculated noLinkRate is above or equal to 0')
        self.assertLessEqual(sim_results['noLinkRate'], 1.0, 'calculated noLinkRate is below or equal to 1')

        # expect only 1 moving node with gps enabled
        self.assertEqual(sim_results['movingNodes'], 1, 'expected number of moving nodes')
        self.assertEqual(sim_results['gpsEnabled'], 1, 'expected number of gps enabled nodes')

    def test_connectivity_map_optimization_is_consistent(self):
        from lib.node import default_generate_node_list

        from lib.config import CONFIG
        conf = CONFIG

        all_results = []

        # Both settings of the connectivity-map optimization, which must not change a
        # result. Add a second such axis sparingly: the configurations multiply.
        for enable_optimization in [True, False]:
            # test against optimization being enabled/disabled
            conf.ENABLE_CONNECTIVITY_MAP = enable_optimization

            # crucial!! and perhaps a tad fragile
            random.seed(conf.SEED)

            self.assertEqual(conf.SEED, 44, "expected default seed for rng")

            # imitate parse_params
            conf.NR_NODES = 10
            conf.update_router_dependencies()
            nodeConfig = default_generate_node_list(conf)
            # skipping GUI graphing to speed things up

            # set up sim
            sim = lib.discrete_event_sim.DiscreteEventSim(conf, nodeConfig)
            sim.run_simulation()

            # collect & unpack results for easy copy/paste of asserts
            results = sim.get_results()
            all_results.append(results)

        # Named results only. Comparing MeshPacket objects would need equality on them.
        facets = [
            'potentialReceivers',
            'sent',
            'nrCollisions',
            'nrSensed',
            'nrReceived',
            'nrUseful',
            'meanDelay',
            'txAirUtilizationRate',
            'collisionRate',
            'nodeReach',
            'nrReceived',
            'usefulness',
            'delayDropped',
            'noLinkRate',
            'movingNodes',
            'gpsEnabled',
        ]

        for f in facets:
            self.assertEqual(all_results[0][f], all_results[1][f], f'connectivity map optimization is inconsistent for facet {f}')

    def test_phy_loss_counts_only_sensed_non_collided_copies(self):
        from lib.config import Config

        class MockNode:
            def __init__(self, nodeid: int):
                self.nodeid = nodeid
                self.usefulPackets = 0
                self.usefulAppPackets = 0
                self.txAirUtilization = 0.0
                self.droppedByDelay = 0
                self.isMoving = False
                self.gpsEnabled = False

            def channel_utilization_percent(self):
                return 0.0

            def utilization_tx_percent(self):
                return 0.0

        class MockPacket:
            def __init__(self):
                self.collidedAtN = [False, True, False]
                self.sensedByN = [True, True, False]
                self.receivedAtN = [False, False, False]
                self.phyLostAtN = [True, True, True]
                self.collisionReasonAtN = [None, "capture", None]
                self.terrainLossAtN = [0.0, 0.0, 0.0]
                self.seq = 0
                self.isAck = False
                self.destId = 0xFFFFFFFF
                self.txNodeId = 0
                self.origTxNodeId = 0
                self.clutterLossAtN = [0.0, 0.0, 0.0]

        conf = Config()
        conf.NR_NODES = 3
        sim_results = lib.discrete_event_sim.SimulationResults({
            "nodes": [MockNode(0), MockNode(1), MockNode(2)],
            "packets": [MockPacket()],
            "delays": [],
            "packetIdsIssued": 1,
            "totalPairs": 0,
            "asymmetricLinks": 0,
            "symmetricLinks": 0,
            "noLinks": 0,
        })

        sim_results.finalize(conf)

        self.assertEqual(sim_results["nrPhyLoss"], 1)
        self.assertEqual(sim_results["nrCollisions"], 1)

    # TODO: add default-skip GUI test?
    def test_discrete_sim_ten_nodes(self):
        from lib.node import default_generate_node_list

        from lib.config import CONFIG
        conf = CONFIG

        # crucial!! and perhaps a tad fragile
        random.seed(conf.SEED)

        self.assertEqual(conf.SEED, 44, "expected default seed for rng")

        # imitate parse_params
        conf.NR_NODES = 10
        conf.update_router_dependencies()
        nodeConfig = default_generate_node_list(conf)
        # skipping GUI graphing to speed things up

        # set up sim
        sim = lib.discrete_event_sim.DiscreteEventSim(conf, nodeConfig)
        sim.run_simulation()

        # collect & unpack results for easy copy/paste of asserts
        results = sim.get_results()

        appMessages = results["appMessages"]

        # Known-good numbers. A failure here means a change moved the simulation: decide
        # whether that was the bug or the fix before updating them.
        #
        # Moved by the preamble-lock window fix: it was computed in seconds and compared against
        # milliseconds, so every overlap counted as a timing collision. Collisions fall (220 -> 206),
        # which lets more packets through (2466 -> 2508), which produces more rebroadcasts
        # (786 -> 801) and returns implicit ACKs sooner - so two more application messages get
        # generated, the generator being gated on the retransmission timer. The reliable-broadcast
        # budget also went from three retries to the firmware's two.
        #
        # Moved again by the channel-utilisation unification: the contention window is sized from a
        # 60 s union of audible air rather than a lifetime mean of every sensed packet's full
        # airtime, so the window this ten-node mesh draws from is different and the mean delay
        # follows it (4051 -> 4234 ms).
        #
        # Moved again by decoupling the generator from the reliable send: every message used to
        # stall its node for a retransmission timeout before the loop looked for the ACK, so this
        # mesh was offering about 8% less load than its own PERIOD asks for. 182 -> 197 messages,
        # and everything downstream of the load follows.
        #
        # Moved again by the channel-utilisation TX gate, which the simulator had nowhere and the
        # firmware has in every periodic module: this mesh now declines 16 of its own sends because
        # the channel was over 25% busy, so 197 -> 182 messages. That is self-throttling, not the
        # generator stall it superficially resembles - channelUtilDropped names how many.
        #
        # Moved again by making external interference one channel condition instead of two
        # independent draws. INTERFERENCE_LEVEL 0.05 now means a foreign transmitter really holds
        # this node's channel 5% of the time, and a frame overlapping one destructively is lost:
        # collisions 231 -> 519 on a mesh whose frames are 682 ms long. Under the old model the CAD
        # half deferred transmissions and the reception half was gated off by default, so the
        # channel was busy enough to wait for and never busy enough to break anything.
        self.assertEqual(appMessages, 179, "expected number of application messages created")
        sent = results['sent']
        potentialReceivers = results['potentialReceivers']
        self.assertEqual(sent, 886, "expected number of packets sent")
        self.assertEqual(potentialReceivers, 7974, "expected number of potential receivers")

        nrCollisions = results['nrCollisions']
        self.assertEqual(nrCollisions, 519, "expected number of collisions")
        nrSensed = results['nrSensed']
        self.assertEqual(nrSensed, 3068, "expected number of packets sensed")

        nrReceived = results['nrReceived']
        self.assertEqual(nrReceived, 2546, "expected number of packets received")
        meanDelay = results['meanDelay']
        self.assertEqual(round(meanDelay, 2), 5618.0, "expected rounded delay average")
        txAirUtilizationRate = results['txAirUtilizationRate']
        self.assertEqual(round(txAirUtilizationRate * 100, 2), 3.35, "expected rounded average tx air utilization")

        nodeReach = results['nodeReach']
        self.assertEqual(round(nodeReach*100, 2), 76.16, "expected rounded percentage of nodes reached")

        usefulness = results['usefulness']
        self.assertEqual(round(usefulness*100, 2), 48.19, "expected rounded 'usefulness' percentage")

        delayDropped = results['delayDropped']
        self.assertEqual(delayDropped, 1122, "expected number of packets dropped")
        # default config has both asymmetric links and movement enabled
        noLinkRate = results['noLinkRate']
        self.assertEqual(round(noLinkRate * 100, 2), 55.56, "expected rounded percentage of 'no' links")

        movingNodes = results['movingNodes']
        self.assertEqual(movingNodes, 4, "expected number of moving nodes")

        gpsEnabled = results['gpsEnabled']
        self.assertEqual(gpsEnabled, 1, "expected number of nodes with GPS")

        # The channel-busy share, over the union of audible air. A channel cannot be busy more
        # than all the time, and the figure the contention window used to read hit 117.5%.
        chutil = results['nodeChannelUtilPercent']
        self.assertLessEqual(chutil['max'], 100.0, "a channel cannot be busy more than all the time")
        self.assertEqual(round(chutil['mean'], 2), 15.49, "expected mean channel utilization")
        self.assertEqual(round(chutil['max'], 2), 20.46, "expected busiest node's channel utilization")
        # Own transmissions over the last hour: the other window, and a tenth of the first.
        utilTx = results['nodeUtilizationTxPercent']
        self.assertLess(utilTx['max'], chutil['max'])

        # Sends this mesh declined because the channel was over the polite 25% limit.
        self.assertEqual(results['channelUtilDropped'], 19, "expected sends declined by the tx gate")

    def test_sim_does_not_change_config(self):
        import copy

        from lib.node import default_generate_node_list

        # get default config, set node number
        from lib.config import CONFIG
        conf = CONFIG

        # copied from the 10-node test just because, but not necessary
        random.seed(conf.SEED)

        conf.NR_NODES = 3 # smaller number for speed.
        conf.update_router_dependencies()
        nodeConfig = default_generate_node_list(conf)
        # skipping GUI graphing to speed things up

        # get copy of the config pre-run
        old_conf = copy.deepcopy(conf)

        # set up and run sim
        sim = lib.discrete_event_sim.DiscreteEventSim(conf, nodeConfig)
        sim.run_simulation()

        # go through the full sim lifecycle, to cover everywhere that may touch config
        results = sim.get_results()

        # set difference trick to compare configs
        conf_diff = conf.__dict__.items() ^ old_conf.__dict__.items()
        self.assertEqual(len(conf_diff), 0, "config has not been changed by running a simulation")

if __name__ == '__main__':
    unittest.main()
