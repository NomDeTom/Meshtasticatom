import logging
import math
import random

logger = logging.getLogger(__name__)

# checked as of 2.8.0 (version.properties), commit 51eadb7, in the meshtastic-firmware repo
NUM_SYM_CAD = 2
NUM_SYM_CAD_24GHZ = 4

# Demodulator floor per spreading factor, from the SX1262 datasheet (rev 2.1, table 13-11). These
# are the numbers the preset sensitivities are built from: a preset's sensitivity is kTB for its
# bandwidth, plus the receiver noise figure, plus the figure below.
REQUIRED_SNR_DB = {6: -5.0, 7: -7.5, 8: -10.0, 9: -12.5, 10: -15.0, 11: -17.5, 12: -20.0}

THERMAL_NOISE_DBM_PER_HZ = -174.0
RECEIVER_NOISE_FIGURE_DB = 6.0


def thermal_noise_floor(bw_hz, noise_figure_db=RECEIVER_NOISE_FIGURE_DB):
    """kTB + NF for one bandwidth. Doubling the bandwidth costs 3 dB."""
    return THERMAL_NOISE_DBM_PER_HZ + 10.0 * math.log10(bw_hz) + noise_figure_db


def required_snr_db(sf):
    """The modem's demodulation floor for this spreading factor."""
    return REQUIRED_SNR_DB[int(sf)]


def effective_sensitivity(conf, preset=None):
    """The weakest signal this receiver can actually decode, given the noise it sits in.

    A preset's sensitivity is a datasheet figure: kTB for its bandwidth, plus a noise figure, plus
    the modem's required SNR. It is therefore a statement about a *thermal* noise floor, and it
    cannot be combined with a measured or fitted noise level without double-counting - raising the
    noise floor by 9.5 dB and keeping the sensitivity says the modem decodes 9.5 dB below its own
    limit. On the packaged Batumi calibration, whose floor is -110.5 dBm, that made LONG_FAST's
    weakest audible link sit 3.5 dB below what SF11 can demodulate, and LONG_SLOW's 6.5 dB below.

    So the threshold is whichever is harder: the datasheet figure, or the noise the receiver is
    actually in plus the SNR the modem needs. A floor quieter than thermal cannot help, because the
    receiver's own noise dominates there.
    """
    preset = preset or conf.current_preset
    datasheet = preset["sensitivity"]
    from_noise = conf.NOISE_LEVEL + required_snr_db(preset["sf"])
    return max(datasheet, from_noise)


def effective_cad_threshold(conf, preset=None):
    """Energy detection reaches below decodability, by the margin the preset table declares."""
    preset = preset or conf.current_preset
    margin = preset["sensitivity"] - preset["cad_threshold"]
    return effective_sensitivity(conf, preset) - margin

#                           CAD duration   +     airPropagationTime+TxRxTurnaround+MACprocessing
def get_current_slot_time(conf): # from RadioInterface::computeSlotTimeMsec
    """Slot time in ms for `conf`'s preset and region.

    Every caller passes the config its run is using; there is no module-level default, because a
    process-wide one silently answered for whichever config was bound last.
    """
    # all times in ms
    sum_prop_turnaround_mac_time = 0.2 + 0.4 + 7
    firmware_bw = conf.current_preset["bw"] / 1000 # convert Hz to KHz to match firmware
    symbol_time = (2.0 ** conf.current_preset["sf"]) / firmware_bw

    if conf.REGION['wide_lora']:
        # currently only 2.4GHz LoRa. `(2 * sf + 3) / 32` is integer division in the firmware, where
        # sf is a uint8_t - so the term is 0 for every legal spreading factor, 2*14+3 being 31.
        # True division here made the 2.4 GHz slot time 13% long at SF7 and 21% at SF12.
        return (NUM_SYM_CAD_24GHZ + (2 * conf.current_preset['sf'] + 3) // 32) * symbol_time + sum_prop_turnaround_mac_time
    else:
        return max(2.25, NUM_SYM_CAD + 0.5) * symbol_time + sum_prop_turnaround_mac_time


def _jammed_by_interference(conf, packet, rx_nodeId):
    """Whether a foreign transmitter held this receiver's channel destructively.

    The receiver's own channel, not a fresh coin flip: the same schedule its CAD consults, so a
    transmitter cannot see a clear channel while its frame is destroyed by interference that, a
    moment ago, did not exist.

    Destructively, not merely at the same time: an overlap costs the frame if it lands on the
    preamble, or if it covers enough of the payload to exhaust the coding gain. Those are the same
    two conditions the capture model applies to a Meshtastic interferer, and applying "any overlap
    at all" here instead would make one millisecond of foreign air worth more than a full
    co-channel frame.
    """
    nodes = getattr(packet, "nodes", None)
    if not nodes:
        return False
    interference = getattr(nodes[rx_nodeId], "interference", None)
    if interference is None:
        return False

    lock_end = min(packet.endTime, packet.startTime + preamble_lock_window_ms(conf, packet))
    if interference.overlaps(packet.startTime, lock_end):
        return True
    covered = interference.overlap_ms(packet.startTime, packet.endTime)
    on_air = packet.endTime - packet.startTime
    if on_air <= 0:
        return False
    return covered / on_air >= conf.COLLISION_PAYLOAD_OVERLAP_LOSS_FRACTION


def check_collision(conf, env, packet, rx_nodeId, packetsAtN):
    if conf.CAPTURE_COLLISION_MODEL_ENABLED:
        return check_capture_collision(conf, packet, rx_nodeId, packetsAtN)

    # Check for collisions at rx_node
    col = 0
    if _jammed_by_interference(conf, packet, rx_nodeId):
        packet.collidedAtN[rx_nodeId] = True

    if packetsAtN[rx_nodeId]:
        for other in packetsAtN[rx_nodeId]:
            if frequency_collision(packet, other) and sf_collision(packet, other):
                if timing_collision(conf, env, packet, other):
                    logger.debug(f'Packet nr. {packet.unique_packet_seq} from {packet.txNodeId} and packet nr. {other.unique_packet_seq} from {other.txNodeId} will collide at node {rx_nodeId}!')
                    c = power_collision(packet, other, rx_nodeId)
                    # mark all the collided packets
                    for p in c:
                        p.collidedAtN[rx_nodeId] = True
                        if p == packet:
                            col = 1
                else:
                    pass  # no timing collision
        return col
    return 0


def check_capture_collision(conf, packet, rx_nodeId, packetsAtN):
    """Check overlap with a capture-aware same-SF collision model.

    Off by default; the legacy binary model is preserved. See docs/radio_model.md.
    """
    col = 0
    if _jammed_by_interference(conf, packet, rx_nodeId):
        mark_collision(packet, rx_nodeId, "external_interference")
        col = 1

    for other in packetsAtN[rx_nodeId]:
        if not intervals_overlap(packet.startTime, packet.endTime, other.startTime, other.endTime):
            continue
        if not frequency_collision(packet, other) or not sf_collision(packet, other):
            continue

        casualties = capture_collision_casualties(conf, packet, other, rx_nodeId)
        if casualties:
            logger.debug(
                f'Packet nr. {packet.seq} from {packet.txNodeId} and packet nr. '
                f'{other.seq} from {other.txNodeId} overlap at node {rx_nodeId}; '
                f'capture casualties {[p.seq for p, _ in casualties]}'
            )
        for casualty, reason in casualties:
            mark_collision(casualty, rx_nodeId, reason)
            if casualty == packet:
                col = 1
    return col


def frequency_collision(p1, p2):
    delta_khz = _frequency_delta_khz(p1, p2)
    p1_bw_khz = _bandwidth_khz(p1)
    p2_bw_khz = _bandwidth_khz(p2)

    if delta_khz <= 120 and (p1_bw_khz == 500 or p2_bw_khz == 500):
        return True
    elif delta_khz <= 60 and (p1_bw_khz == 250 or p2_bw_khz == 250):
        return True
    elif delta_khz <= 30:
        return True
    return False


def _frequency_delta_khz(p1, p2):
    """Return center-frequency separation in kHz, from Hz- or MHz-scale inputs.

    Normalized here so the collision predicate does not depend on caller units.
    """
    delta = abs(p1.freq - p2.freq)
    if max(abs(p1.freq), abs(p2.freq)) > 1e6:
        return delta / 1000.0
    return delta * 1000.0


def _bandwidth_khz(packet):
    """Return LoRa bandwidth in kHz for both Hz and kHz-style packet fields."""
    return packet.bw / 1000.0 if packet.bw > 1000 else packet.bw


def sf_collision(p1, p2):
    return p1.sf == p2.sf


def mark_collision(packet, rx_nodeId, reason):
    packet.collidedAtN[rx_nodeId] = True
    if hasattr(packet, "collisionReasonAtN"):
        packet.collisionReasonAtN[rx_nodeId] = reason


def power_collision(p1, p2, rx_nodeId):
    powerThreshold = 6  # dB
    if abs(p1.rssiAtN[rx_nodeId] - p2.rssiAtN[rx_nodeId]) < powerThreshold:
        # packets are too close to each other, both collide
        # return both packets as casualties
        return (p1, p2)
    elif p1.rssiAtN[rx_nodeId] - p2.rssiAtN[rx_nodeId] < powerThreshold:
        # p2 overpowered p1, return p1 as casualty
        return (p1,)
    # p2 was the weaker packet, return it as a casualty
    return (p2,)


def preamble_lock_window_ms(conf, packet):
    """Approximate the fragile LoRa preamble/header acquisition interval."""
    symbols = max(1, conf.NPREAM - 5)
    return symbols * (2 ** packet.sf) / packet.bw * 1000


def timing_collision(conf, env, p1, p2):
    """Whether the fresh packet `p1` loses its preamble to `p2`, still on air.

    `p1` survives if its acquisition window clears `p2`'s last byte. That window is
    `preamble_lock_window_ms`, the same one the capture model uses - it was computed inline here in
    seconds and compared against milliseconds, which collapsed a 90 ms LONG_FAST window to 0.09 ms
    and made every overlap a collision.
    """
    p1_cs = env.now + preamble_lock_window_ms(conf, p1)
    if p1_cs < p2.endTime:  # p1 collided with p2 and lost
        return True
    return False


def intervals_overlap(start1, end1, start2, end2):
    return max(start1, start2) < min(end1, end2)


def overlap_ms(p1, p2):
    return max(0.0, min(p1.endTime, p2.endTime) - max(p1.startTime, p2.startTime))


def overlaps_preamble_lock(conf, victim, interferer):
    return intervals_overlap(
        victim.startTime,
        min(victim.endTime, victim.startTime + preamble_lock_window_ms(conf, victim)),
        interferer.startTime,
        interferer.endTime,
    )


def packet_survives_overlap(conf, victim, interferer, rx_nodeId):
    """Return whether `victim` survives this one overlapping interferer.

    Capture above the threshold, and a short late tail. See docs/radio_model.md.
    """
    desired_margin_db = victim.rssiAtN[rx_nodeId] - interferer.rssiAtN[rx_nodeId]
    if desired_margin_db >= conf.COLLISION_CAPTURE_THRESHOLD_DB:
        return True

    if overlaps_preamble_lock(conf, victim, interferer):
        return False

    fraction = overlap_ms(victim, interferer) / victim.timeOnAir if victim.timeOnAir > 0 else 1.0
    if fraction >= conf.COLLISION_PAYLOAD_OVERLAP_LOSS_FRACTION:
        return False

    return True


def capture_collision_casualties(conf, p1, p2, rx_nodeId):
    casualties = []
    if _packet_was_decodable_at_rx(p1, rx_nodeId) and not packet_survives_overlap(conf, p1, p2, rx_nodeId):
        casualties.append((p1, "capture_overlap"))
    if _packet_was_decodable_at_rx(p2, rx_nodeId) and not packet_survives_overlap(conf, p2, p1, rx_nodeId):
        casualties.append((p2, "capture_overlap"))
    return casualties


def _packet_was_decodable_at_rx(packet, rx_nodeId):
    """Return whether collision loss is meaningful for this packet.

    A packet under the demodulation threshold jams but was never going to decode.
    """
    sensed_by_node = getattr(packet, "sensedByN", None)
    if sensed_by_node is None:
        return True
    return sensed_by_node[rx_nodeId]


def is_channel_active(node, env):
    """CAD: is this node's channel occupied right now, by anyone?

    The external interferer is a schedule with a holding time, so a busy stretch actually blocks
    rather than being re-rolled away on the next attempt - and it is the same schedule a reception
    at this node is judged against.
    """
    interference = getattr(node, "interference", None)
    if interference is not None and interference.is_busy(env.now):
        return True
    for p in node.packets:
        if p.detectedByN[node.nodeid]:
            # You will miss detecting a packet if it has just started before you could do CAD
            if p.startTime + get_current_slot_time(node.conf) <= env.now <= p.endTime:
                return True
    return False


def airtime(conf, sf, cr, pl, bw):
    """Time on air in ms. `cr` is the coding-rate denominator 5..8, as the firmware stores it.

    The Semtech formula multiplies by that denominator directly - see docs/radio_model.md.
    """
    pl = pl + conf.HEADERLENGTH  # add Meshtastic header length
    H = 0  # implicit header disabled (H=0) or not (H=1)

    Tsym = (2.0 ** sf) / bw
    # Auto LDRO, from RadioLibInterface.h: `.ldrOptimize = (1 << sf) / bw >= 16`. The rule is
    # symbol time, not a bandwidth: SF12/BW62.5 optimizes and SF10/BW125 does not.
    DE = 1 if Tsym * 1000 >= 16 else 0
    if sf == 6:  # can only have implicit header with SF6
        H = 1

    Tpream = (conf.NPREAM + 4.25) * Tsym
    payloadSymbNB = 8 + max(math.ceil((8.0 * pl - 4.0 * sf + 28 + 16 - 20 * H) / (4.0 * (sf - 2 * DE))) * cr, 0)
    Tpayload = payloadSymbNB * Tsym

    return (Tpream + Tpayload) * 1000


def estimate_path_loss(conf, dist, freq, txZ=None, rxZ=None, model=None):
    """Path loss in dB, over metres and MHz, by one of the models in docs/radio_model.md.

    `model` is an integer in [0, 6]; heights and model default to the config's.
    """
    # Two nodes can land on one point, and log(0) is not a path loss. A preset can raise
    # the floor further as a near-field calibration - see docs/configuration.md.
    dist = max(dist, conf.PATH_LOSS_DISTANCE_FLOOR_M)
    if txZ is None:
        txZ = conf.HM
    if rxZ is None:
        rxZ = conf.HM
    if model is None:
        model = conf.MODEL

    # Log-Distance model
    if model == 0:
        Lpl = conf.LPLD0 + 10 * conf.GAMMA * math.log10(dist / conf.D0)

    # Okumura-Hata model
    elif 1 <= model <= 4:
        # small and medium-size cities
        if model == 1:
            ahm = (1.1 * (math.log10(freq) - 6.0) - 0.7) * rxZ - (1.56 * (math.log10(freq) - 6.0) - 0.8)
            C = 0
        # metropolitan areas
        elif model == 2:
            if freq <= 200000000:
                ahm = 8.29 * ((math.log10(1.54 * rxZ)) ** 2) - 1.1
            elif freq >= 400000000:
                ahm = 3.2 * ((math.log10(11.75 * rxZ)) ** 2) - 4.97
            C = 0
        # suburban environments
        elif model == 3:
            ahm = (1.1 * (math.log10(freq) - 6.0) - 0.7) * rxZ - (1.56 * (math.log10(freq) - 6.0) - 0.8)
            C = -2 * ((math.log10(freq) - math.log10(28000000)) ** 2) - 5.4
        # rural area
        elif model == 4:
            ahm = (1.1 * (math.log10(freq) - 6.0) - 0.7) * rxZ - (1.56 * (math.log10(freq) - 6.0) - 0.8)
            C = -4.78 * ((math.log10(freq) - 6.0) ** 2) + 18.33 * (math.log10(freq) - 6.0) - 40.98

        A = 69.55 + 26.16 * (math.log10(freq) - 6.0) - 13.82 * math.log10(txZ) - ahm
        B = 44.9 - 6.55 * math.log10(txZ)
        Lpl = A + B * (math.log10(dist) - 3.0) + C

    # 3GPP model
    elif 5 <= model < 7:
        # Suburban Macro
        if model == 5:
            C = 0  # dB
        # Urban Macro
        elif model == 6:
            C = 3  # dB

        Lpl = (44.9 - 6.55 * math.log10(txZ)) * (math.log10(dist) - 3.0) \
            + 45.5 + (35.46 - 1.1 * rxZ) * (math.log10(freq) - 6.0) \
            - 13.82 * math.log10(rxZ) + 0.7 * rxZ + C
    else:
        raise ValueError(f"unsupported path loss model: {model}")

    # No propagation model may beat free space. Every model here is an empirical fit with a
    # validity range - Okumura-Hata wants a base station 30-200 m up and a mobile 1-10 m up, and
    # this simulator passes antenna heights above local ground for both, usually 1.5 m. Asked far
    # enough outside that range the 3GPP form's linear height terms dominate and it returns a
    # negative loss, i.e. gain: 900 m of antenna height produced +2173 dBm of RSSI.
    return max(Lpl, free_space_path_loss(dist, freq))


def free_space_path_loss(dist, freq):
    """Friis free-space loss in dB, over metres and Hz. The floor under every other model."""
    return 20.0 * math.log10(max(dist, 1e-9)) + 20.0 * math.log10(freq) - 147.55221677811665


def zero_link_budget(conf, dist, tx_gain=None, rx_gain=None):
    """Link margin in dB at `dist`, zero at the range where the preset stops decoding.

    A link has an antenna at each end, so both gains are counted; each defaults to the config's.
    """
    if tx_gain is None:
        tx_gain = conf.GL
    if rx_gain is None:
        rx_gain = conf.GL
    return (
        conf.PTX
        + tx_gain
        + rx_gain
        - estimate_path_loss(conf, dist, conf.FREQ)
        - conf.current_preset["sensitivity"]
    )


def rootFinder(func, x0, args=(), tol=1, maxiter=100):
  """Newton-Raphson root finder."""
  x = x0
  for _ in range(maxiter):
      fx = func(x, *args)
      dfx = (func(x + 1e-6, *args) - fx) / 1e-6
      if dfx == 0:
          print("Warning: could not estimate max. range")
          return x
      x_new = x - fx / dfx
      if abs(x_new - x) < tol:
          return x_new
      x = x_new
  print("Warning: could not estimate max. range")
  return x


def estimate_max_range(conf, tx_gain=None, rx_gain=None):
    """Distance in m at which `conf`'s preset stops decoding, for this pair of antenna gains."""
    return rootFinder(lambda dist: zero_link_budget(conf, dist, tx_gain, rx_gain), 1500)
