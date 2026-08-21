import random

import numpy as np

from lib import phy
from lib.link_model import calculate_link_budget
from lib.point import Point


def node_antenna_height(node):
    """Return antenna height above ground, falling back to legacy Point.z."""
    return getattr(node, "antennaHeight", getattr(node, "antenna_height", node.position.z))

def find_random_position(conf, node_configs) -> (float, float):
    """Pick a random (x, y) for the next node.

    Inside the area, in range of at least one existing node, and no closer than MINDIST to any.

    Both tests are evaluated per candidate. They used to be flags declared outside the loop and
    never reset, so the first MINDIST rejection set `foundMin` False permanently and no later
    candidate could be accepted - the search then span to its 1000-try limit and returned
    `position.x` with `position` still None. And `foundMax` was sticky the other way: once any
    candidate had been in range of something, a later one could be accepted on the strength of a
    different candidate's reachability.
    """
    tries = 0
    while True:
        posx = random.random()*conf.XSIZE+conf.OX-conf.XSIZE/2
        posy = random.random()*conf.YSIZE+conf.OY-conf.YSIZE/2
        pos_candidate = Point(posx, posy, conf.HM)
        if not node_configs:
            return max(-conf.XSIZE/2, pos_candidate.x), max(-conf.YSIZE/2, pos_candidate.y)

        far_enough = True
        in_range = False
        for n in node_configs:
            dist = n.position.euclidean_distance(pos_candidate)
            if dist < conf.MINDIST:
                far_enough = False
                break
            pathLoss = phy.estimate_path_loss(conf, dist, conf.FREQ)
            rssi = conf.PTX + 2*conf.GL - pathLoss
            # At least one node should be able to reach it
            if rssi >= phy.effective_sensitivity(conf):
                in_range = True
        if far_enough and in_range:
            return max(-conf.XSIZE/2, pos_candidate.x), max(-conf.YSIZE/2, pos_candidate.y)

        tries += 1
        if tries > 1000:
            raise RuntimeError(
                "Could not find a location to place the node after 1000 tries. Try increasing "
                "XSIZE/YSIZE or decreasing MINDIST."
            )

def calc_dist(x0, x1, y0, y1, z0=0, z1=0):
    return np.sqrt(((abs(x0-x1))**2)+((abs(y0-y1))**2)+((abs(z0-z1)**2)))

def setup_asymmetric_links(conf, nodes):
    """Populate conf.LINK_OFFSET: a shadowing term per path, plus a radio offset per direction.

    Physical path loss is reciprocal - the channel between two antennas is the same channel
    travelling either way - so shadowing is drawn once per unordered pair and applied to both
    directions. Real link asymmetry comes from the hardware: different transmit power, different
    antenna, a different noise floor at each end. That is a per-node, per-direction term.

    This used to be one Gaussian per *directed* pair, applied to the path. It attributed to the
    channel what belongs to the radio, so the asymmetry moved when the geometry moved and stayed
    put when the hardware did - and at a 2 dB standard deviation it was the only stochastic element
    in the whole budget, three to five times narrower than measured outdoor UHF shadowing, which
    left link existence a near-deterministic function of distance.
    """
    shadowRng = random.Random(f"{conf.SEED}:shadowing")
    radioRng = random.Random(f"{conf.SEED}:radio-offset")
    conf.LINK_OFFSET = {}
    totalPairs = 0
    symmetricLinks = 0
    asymmetricLinks = 0
    noLinks = 0

    tx_offset = [0.0] * conf.NR_NODES
    rx_offset = [0.0] * conf.NR_NODES
    if conf.MODEL_ASYMMETRIC_LINKS:
        for i in range(conf.NR_NODES):
            tx_offset[i] = radioRng.gauss(0.0, conf.MODEL_RADIO_ASYMMETRY_STDDEV)
            rx_offset[i] = radioRng.gauss(0.0, conf.MODEL_RADIO_ASYMMETRY_STDDEV)

    for i in range(conf.NR_NODES):
        for b in range(i + 1, conf.NR_NODES):
            if conf.MODEL_ASYMMETRIC_LINKS:
                shadow = shadowRng.gauss(conf.MODEL_SHADOWING_MEAN, conf.MODEL_SHADOWING_STDDEV)
            else:
                shadow = 0.0
            # An offset is added to the path loss, so a radio that transmits harder or hears
            # better subtracts from it.
            conf.LINK_OFFSET[(i, b)] = shadow - tx_offset[i] - rx_offset[b]
            conf.LINK_OFFSET[(b, i)] = shadow - tx_offset[b] - rx_offset[i]

    for a in range(conf.NR_NODES):
        for b in range(conf.NR_NODES):
            if a != b:
                # The same directed budget MeshPacket will use, so the summary graph cannot
                # be more optimistic about a link than delivery turns out to be.
                nodeA = nodes[a]
                nodeB = nodes[b]
                budgetAB = calculate_link_budget(conf, nodeA, nodeB, conf.LINK_OFFSET[(a, b)])
                budgetBA = calculate_link_budget(conf, nodeB, nodeA, conf.LINK_OFFSET[(b, a)])

                sensitivity = phy.effective_sensitivity(conf)
                canAhearB = (budgetAB.rssi_dbm >= sensitivity)
                canBhearA = (budgetBA.rssi_dbm >= sensitivity)

                totalPairs += 1
                if canAhearB and canBhearA:
                    symmetricLinks += 1
                elif canAhearB or canBhearA:
                    asymmetricLinks += 1
                else:
                    noLinks += 1

    return totalPairs, symmetricLinks, asymmetricLinks, noLinks
