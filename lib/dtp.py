"""Dynamic TX Power policy for Meshtasticator experiments.

DCR changes how long and how redundant a packet is. DTP changes how far the
same packet becomes interference. Keep DTP late and local: configured region
power remains the maximum, and this policy may only lower a packet's temporary
TX power just before it goes on air.
"""

from dataclasses import dataclass

from lib.dcr import CR_RESCUE, classify_channel_pressure
from lib.packet import NODENUM_BROADCAST


@dataclass(frozen=True)
class DtpDecision:
    tx_power_dbm: int
    reason: str


def _configured_step(conf) -> int:
    return max(1, int(getattr(conf, "DTP_POWER_STEP_DB", 3)))


def _quantize_drop(conf, drop_db: int) -> int:
    """Round drops down to the configured radio step, so 4 dB on a 3 dB step becomes 3."""
    drop_db = max(0, min(int(drop_db), int(getattr(conf, "DTP_MAX_POWER_DROP_DB", 12))))
    step = _configured_step(conf)
    return (drop_db // step) * step


def _apply_drop(conf, base_power_dbm: int, drop_db: int) -> int:
    base_power_dbm = int(base_power_dbm)
    selected = base_power_dbm - _quantize_drop(conf, drop_db)
    min_power = getattr(conf, "DTP_MIN_TX_POWER_DBM", None)
    if min_power is not None:
        selected = max(int(min_power), selected)

    # A minimum above PTX must not turn a reduction policy into a boost: PTX is the ceiling.
    return min(base_power_dbm, selected)


def _retry_attempt(node, packet) -> int:
    # The packet's own budget, not a mesh-wide constant: a broadcast and a unicast do not get
    # the same number of attempts.
    return max(0, getattr(packet, "maxRetransmissions", 0) - packet.retransmissions)


def _prior_hop_margin_db(conf, packet) -> float | None:
    """Return the prior hop's decode margin above this preset's sensitivity.

    Absolute LoRa SNR is negative even on clean packets, so a fixed dB threshold would not do.
    """
    prior_rssi = getattr(packet, "priorHopRssi", None)
    if prior_rssi is not None:
        return prior_rssi - conf.current_preset["sensitivity"]

    prior_snr = getattr(packet, "priorHopSnr", None)
    if prior_snr is None:
        return None

    sensitivity_snr = conf.current_preset["sensitivity"] - conf.NOISE_LEVEL
    return prior_snr - sensitivity_snr


def _strong_prior_hop(conf, packet) -> bool:
    margin = _prior_hop_margin_db(conf, packet)
    return margin is not None and margin >= conf.DTP_STRONG_LINK_MARGIN_DB


def _very_strong_prior_hop(conf, packet) -> bool:
    margin = _prior_hop_margin_db(conf, packet)
    return margin is not None and margin >= conf.DTP_VERY_STRONG_LINK_MARGIN_DB


def choose_dynamic_tx_power(node, packet) -> DtpDecision:
    """Choose a temporary per-packet TX power for DTP experiments.

    Deliberately asymmetric by packet role - see docs/configuration.md.
    """
    base_power = int(getattr(packet, "baseTxPower", node.conf.PTX))
    if not node.conf.DTP_ENABLED:
        return DtpDecision(base_power, "dtp_off")

    pressure, util, queue_depth = classify_channel_pressure(node)
    relay = packet.txNodeId != packet.origTxNodeId
    direct = getattr(packet, "destId", NODENUM_BROADCAST) != NODENUM_BROADCAST
    retry_attempt = _retry_attempt(node, packet)
    final_retry = retry_attempt > 0 and packet.retransmissions <= 1
    margin = _prior_hop_margin_db(node.conf, packet)
    strong = _strong_prior_hop(node.conf, packet)
    very_strong = _very_strong_prior_hop(node.conf, packet)
    reasons = [f"channel_{pressure}", f"util={util:.1f}", f"queue={queue_depth}"]
    if margin is not None:
        reasons.append(f"prior_margin={margin:.1f}")

    drop_db = 0

    if final_retry or packet.cr >= CR_RESCUE:
        # A rescue attempt keeps full power: coding rate helps a payload decode, but
        # nothing recovers a preamble pushed under sensitivity.
        reasons.append("max_power_retry_rescue")
    elif packet.isAck:
        if very_strong:
            drop_db = 6 if pressure in ("busy", "congested") else 3
            reasons.append("ack_strong_prior_hop")
        else:
            reasons.append("max_power_ack")
    elif relay:
        reasons.append("relay")
        if direct and not strong:
            # Meshtasticator knows the destination but not a guaranteed next-hop
            # budget. Keep power unless the prior hop was clearly strong.
            reasons.append("max_power_direct_relay_without_strong_link")
        elif packet.hopLimit <= 1 and not strong:
            reasons.append("max_power_last_hop_without_strong_link")
        elif pressure == "congested":
            drop_db = 9
            reasons.append("congested_relay_power_drop")
        elif pressure == "busy":
            drop_db = 6
            reasons.append("busy_relay_power_drop")
        elif strong:
            drop_db = 3
            reasons.append("strong_prior_hop_power_drop")
        else:
            reasons.append("max_power_relay")

        if direct and strong:
            drop_db = min(drop_db or 3, 3)
            reasons.append("direct_relay_cap")
        if packet.hopLimit <= 1 and strong:
            drop_db = min(drop_db or 3, 3)
            reasons.append("last_hop_cap")
    else:
        # An origin packet seeds the flood, and cutting it without topology certainty
        # makes holes rather than removing duplicate overlap.
        reasons.append("max_power_origin")

    selected_power = _apply_drop(node.conf, base_power, drop_db)
    if selected_power < base_power:
        reasons.append(f"drop={base_power - selected_power}dB")
    else:
        reasons.append("drop=0dB")

    return DtpDecision(selected_power, ",".join(reasons))
