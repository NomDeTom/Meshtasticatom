"""Dynamic Coding Rate policy for Meshtasticator experiments.

The firmware idea is to choose LoRa coding rate very late, after queueing and
listen-before-talk. The simulator mirrors that shape: this module changes only
the packet's physical CR and resulting airtime immediately before low-level
transmit.

With the default PHY model this is mostly an airtime/collision-pressure study.
When the empirical PHY-loss model is enabled, the selected CR also changes the
payload decode probability near weak-link edges.
"""

from dataclasses import dataclass

from lib.packet import NODENUM_BROADCAST


CR_SLIM = 5
CR_NORMAL = 6
CR_ROBUST = 7
CR_RESCUE = 8


@dataclass(frozen=True)
class DcrDecision:
    cr: int
    reason: str


def _clamp_cr(cr: int, min_cr: int, max_cr: int) -> int:
    return max(min_cr, min(max_cr, cr))


def _score_to_cr(score: int) -> int:
    if score <= 0:
        return CR_SLIM
    if score == 1:
        return CR_NORMAL
    if score == 2:
        return CR_ROBUST
    return CR_RESCUE


def _selected_region_duty_limit(conf) -> float | None:
    """Return a legal duty-cycle limit only where the region has one.

    Congestion and regulatory pressure are separate signals; do not invent the second.
    """
    duty_cycle = conf.REGION.get("duty_cycle", 100)
    if 0 < duty_cycle < 100:
        return float(duty_cycle)
    return None


def _node_queue_depth(node) -> int:
    """Best-effort count of packets waiting behind the current transmitter slot."""
    return len(getattr(node.transmitter, "queue", []))


def _current_channel_utilization_percent(node) -> float:
    """Return rolling channel utilization including the active 10-second bucket."""
    completed_util = node.channel_utilization_percent()
    current_bucket_airtime = max(0.0, node.txAirUtilization - node.prevTxAirUtilization)
    current_bucket_util = (
        current_bucket_airtime
        / (node.conf.CHANNEL_UTILIZATION_PERIODS * node.conf.TEN_SECONDS_INTERVAL)
        * 100.0
    )
    return completed_util + current_bucket_util


def classify_channel_pressure(node) -> tuple[str, float, int]:
    """Classify local channel pressure. The thresholds are congestion, not legal limits."""
    util = _current_channel_utilization_percent(node)
    queue_depth = _node_queue_depth(node)

    if util >= node.conf.DCR_CONGESTED_UTIL_PERCENT or queue_depth >= node.conf.DCR_CONGESTED_QUEUE_DEPTH:
        return "congested", util, queue_depth

    if util >= node.conf.DCR_BUSY_UTIL_PERCENT or queue_depth >= node.conf.DCR_BUSY_QUEUE_DEPTH:
        return "busy", util, queue_depth

    if util <= node.conf.DCR_IDLE_UTIL_PERCENT and queue_depth <= 1:
        return "idle", util, queue_depth

    return "normal", util, queue_depth


def _base_packet_score(packet) -> tuple[int, list[str]]:
    """Approximate packet classes from the fields this simulator has.

    No portnums or app priority here, so ACKs are the only visible control class.
    """
    if packet.isAck:
        return 1, ["control_ack"]

    # First attempts stay compact; retry and context signals are what justify the FEC.
    return 0, ["user"]


def _retry_score(node, packet, pressure: str, util: float) -> tuple[int, list[str]]:
    attempt = max(0, getattr(packet, "maxRetransmissions", 0) - packet.retransmissions)
    if attempt == 0:
        return 0, []

    if pressure in ("busy", "congested"):
        return 0, [f"retry_{attempt}_no_fec_bump_channel_{pressure}"]

    duty_limit = _selected_region_duty_limit(node.conf)
    if duty_limit is not None and util >= duty_limit:
        return 0, [f"retry_{attempt}_no_fec_bump_duty_limit"]

    # Retries after quiet loss are the deliberate spend: CR6 normally, CR8 on a final
    # quiet retry when the airtime budget allows it.
    final_retry = packet.retransmissions <= 1
    return (3 if final_retry else 1), [f"retry_{attempt}_quiet_loss"]


def _relay_score(packet) -> tuple[int, list[str]]:
    if packet.txNodeId == packet.origTxNodeId:
        return 0, []

    score = -1
    reasons = ["generic_relay"]

    if packet.hopLimit <= 1:
        # Last-hop relay may be the final useful chance for this packet, but it
        # still should not jump to CR8 without retry/link evidence.
        score += 2
        reasons.append("last_hop")

    return score, reasons


def _cr8_budget_allows(node, packet, candidate_cr: int) -> bool:
    if candidate_cr != CR_RESCUE:
        return True

    candidate_airtime = packet.airtime_for_cr(candidate_cr)
    cr8_airtime = node.dcrAirtimeByCr.get(CR_RESCUE, 0.0) + candidate_airtime
    total_airtime = node.txAirUtilization + candidate_airtime

    if total_airtime <= 0:
        return True

    return (cr8_airtime / total_airtime * 100.0) <= node.conf.DCR_CR8_AIRTIME_LIMIT_PERCENT


def choose_dynamic_coding_rate(node, packet) -> DcrDecision:
    """Choose a per-packet CR using only information the simulator already has."""
    if not node.conf.DCR_ENABLED:
        return DcrDecision(packet.cr, "dcr_off")

    score, reasons = _base_packet_score(packet)
    pressure, util, queue_depth = classify_channel_pressure(node)

    if pressure == "idle":
        # Idle air is reserve, not permission to fatten every first attempt.
        reasons.append("idle_no_first_attempt_bump")
    elif pressure == "busy":
        score -= 1
    elif pressure == "congested":
        score -= 2
    reasons.append(f"channel_{pressure}")

    retry_delta, retry_reasons = _retry_score(node, packet, pressure, util)
    score += retry_delta
    reasons.extend(retry_reasons)

    relay_delta, relay_reasons = _relay_score(packet)
    score += relay_delta
    reasons.extend(relay_reasons)

    min_cr = max(node.conf.DCR_MIN_CR, node.conf.DCR_USER_MIN_CR)
    if (
        not packet.isAck
        and getattr(packet, "destId", NODENUM_BROADCAST) != NODENUM_BROADCAST
        and packet.txNodeId != packet.origTxNodeId
        and pressure not in ("busy", "congested")
    ):
        # Addressed directly and already relayed once is real header-level context,
        # worth more than the thinnest CR while local air is quiet.
        min_cr = max(min_cr, CR_NORMAL)
        reasons.append("direct_relay_min_cr")

    if packet.isAck:
        # ACKs are tiny and important, but should still not become CR8 storms.
        min_cr = max(min_cr, CR_NORMAL)

    cr = _clamp_cr(_score_to_cr(score), min_cr, node.conf.DCR_MAX_CR)

    if not _cr8_budget_allows(node, packet, cr):
        cr = _clamp_cr(CR_ROBUST, min_cr, node.conf.DCR_MAX_CR)
        reasons.append("cr8_budget_clamp")

    reasons.append(f"util={util:.1f}")
    reasons.append(f"queue={queue_depth}")
    return DcrDecision(cr, ",".join(reasons))
