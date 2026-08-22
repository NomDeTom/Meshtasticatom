"""Predefined sweeps over the campaign's arms, one block at a time.

Seeds are drawn once per block and shared by every cell in it, so a topology and a traffic schedule
are held fixed while one arm moves. An unpaired comparison across a sweep this noisy would mostly
measure which seed drew a better-connected mesh.

Usage, from sim/:
    python3 -m sfpp.sweep --block D-cadence --out <dir>
    python3 -m sfpp.sweep --list
"""

import argparse
import copy
import json
import os
import random
import statistics
import time
from functools import lru_cache

from . import autochart as AC
from . import report as RP
from .campaign import build_parser, run_once
from .collate import safe_name

# Everything the protocol blocks hold fixed. Servers sit two hops apart, comfortably inside the
# default hop limit, so an advert reaches its peers and the arm under test is what varies.
BASE = [
    "--hours",
    "36",
    "--nodes",
    "60",
    "--place",
    "hops-apart",
    "--hops-apart",
    "2",
    "--servers",
    "3",
    "--capacity",
    "32",
    # Bucket-close, on the D-cadence evidence: it holds more than a five-minute interval for a
    # fourteenth of the airtime, so every later block measures the design as it should be run.
    "--trigger",
    "bucket",
    # The numbering the firmware actually does. A shared counter cannot exist, so no result about
    # bucket agreement is meaningful without this.
    "--bucket-mode",
    "local",
    "--resolve",
    "hybrid",
]

# A retry ladder needs an addressed message and a learned route to act on, so an arm over
# --dm-mode or --coding-rate-ladder without these produces identical rows.
DM_LADDER = ["--dm-transport", "transport", "--traceroute-per-hour", "1"]

# --- how a block is named -----------------------------------------------------------------------
#
# A name is three things at once: the row identity the rolling page tracks a block by across runs, a
# path component (`figures/<block>.svg`, `reports/<block>.txt`, `<block>.json`), and something a
# reader has to place at a glance. The letters below it are rounds - the order the questions were
# asked - which is why F holds both the degradation blocks and, much later, the future-radio ones.
#
# New names carry their domain instead. `<DD>-<subject>[-<qualifier>]`: two-letter uppercase domain,
# lowercase kebab tail. Lowercase tails make two names that differ only in case impossible, which is
# the one collision collate.safe_name cannot resolve for itself. No double dash - explorer.py reads
# `<block>--<label>.svg` as a block's extra figure.
DOMAINS = {
    "BL": "baseline and paired controls: the shipped default on a given mesh",
    "MS": "mesh composition and scale: count, density, area, topology, mirroring, siting, roles",
    "RF": "radio and propagation: path loss, noise, ducting, calibration, presets, power, gain",
    "RT": "routing and reach: hop limits and their assignment, adoption, rebroadcast",
    "DM": "how an addressed message behaves: escalation, transport, acknowledgement. Not how much "
    "of it there is - a DM rate is offered load and belongs in LD",
    "TH": "throttles: what the firmware does to offered load - interval scaling, reach target, the "
    "per-class multipliers",
    "DB": "the node database: hot store cap, warm tier, and the board mix that sizes them",
    "LD": "offered load: what the application asks for before any throttle acts on it, broadcast "
    "and addressed alike - intervals, diurnal shape, DM and traceroute and admin rates",
    "FW": "firmware version mix: which release each node runs, and the proportion running an older one",
    "SC": "security policy: packet signing, and the admin and key rules that will join it",
    "DG": "imposed degradation: loss floors, bursts, outages - a failure applied, not a model",
    "AD": "adversarial meshes: removing what is known to help, one thing at a time",
    "SF": "SF++ archive internals: how the sketch is tuned, not whether to have it",
    "PR": "proposals no release ships, named `PR-<mechanism>-<variant>` so a pair reads as a pair",
}

# The names that predate the scheme. Grandfathered rather than renamed: their trend rows on the
# results branch are the only history there is, and a rename orphans every one of them. Listed
# explicitly so a new name cannot join them by accident - the contract test reads this set.
LEGACY_BLOCKS = frozenset({
    "D-cadence", "D-jitter", "D-resolve", "E-capacity", "E-signed", "E-width", "F-burst",
    "F-flooding", "F-hoplimit", "F-loss", "F-outage", "F-preset-turbo", "F-txpower",
    "G-allrouters", "G-hops", "G-place", "G-servers", "J-bucketmode", "J-timewin", "J-wincap",
    "J-window", "K-density", "K-hopspread", "K-size", "K-spread", "L-advert", "L-provide",
    "M-capacity", "M-combined", "M-jitter", "M-replayorder", "N-hops", "N-place", "N-servers",
    "P-bw500", "P-catchup", "P-congestion", "P-diurnal", "P-eu-presets", "P-preset",
    "Q-control", "Q-hopassign", "Q-interval", "Q-protocol", "Q-topology", "R-adopt",
    "R-congestion-input", "R-congestion-mode", "R-crladder", "R-dmmode", "R-dmmode-cr",
    "R-favourites", "R-firmware", "R-hopscale", "R-hotstore", "R-hotstore-stress", "R-mixed",
    "R-mixed-26", "R-oversubscribed", "R-platform", "R-rebroadcast", "R-repeats",
    "R-repeats-busy", "R-roles",
    "R-roles-fav", "R-routerlate", "R-signing", "R-signing-cost", "R-siting", "R-srretries",
    "R-traceroute", "R-traceroute-small", "R-versions", "R-warm", "X-amplifiers",
    "X-amplify-worst", "X-badrouters", "X-chatty", "X-chatty-hops", "X-duct", "X-noise",
    "X-nomute", "X-pulse", "X-siting", "X-stretch", "X-stretch-duct", "X-worst",
})

BLOCKS = {
    "D-cadence": ("trigger", ["bucket", "interval", "aimd", "bucket+interval"], []),
    "D-resolve": ("resolve", ["sketch", "enum", "hybrid"], []),
    # Sealing follows a global counter, so every server seals at nearly the same moment. If that
    # is why only 46% of bucket-close adverts land, spreading them should show it.
    "D-jitter": ("advert-jitter-s", [1, 30, 120, 600], []),
    "E-capacity": ("capacity", [4, 8, 16, 32, 50], []),
    "E-width": ("short-id-bits", [16, 24, 32, 64], []),
    "E-signed": ("signed", [False, True], []),
    "F-loss": ("extra-loss", [0.0, 0.1, 0.2, 0.3], []),
    # The same loss in 60-second stretches rather than spread evenly: a burst puts a whole
    # bucket's divergence into one bucket and can pass its capacity in a single go.
    "F-burst": ("burst-loss", [0.0, 0.1, 0.2, 0.3], []),
    # A 60-second burst is nothing to a bucket that takes an hour to fill. This is the outage that
    # actually matters to an archive: a node away for half an hour, which is most of a bucket.
    "F-outage": ("burst-loss", [0.0, 0.1, 0.2, 0.3], ["--burst-ms", "1800000"]),
    "G-place": (
        "place",
        [
            "spread",
            "routers",
            "alternate-routers",
            "beside-router",
            "random-clients",
            "hops-apart",
        ],
        [],
    ),
    "G-hops": ("hops-apart", [1, 2, 3, 4], ["--place", "hops-apart"]),
    "G-servers": ("servers", [2, 3, 5, 8], []),
    # There is no canonical counter, so `local` is what the firmware does and `global` is a fiction
    # kept only as an upper bound. `time` and `window` are the two candidates needing no agreement.
    "J-bucketmode": ("bucket-mode", ["global", "local", "time", "window"], []),
    "J-window": ("window-size", [8, 16, 32], ["--bucket-mode", "window"]),
    "J-wincap": ("capacity", [8, 16, 32], ["--bucket-mode", "window"]),
    "J-timewin": ("time-bucket-s", [600, 1800, 3600], ["--bucket-mode", "time"]),
    # Mesh size, with per-node hop limits 3-7 by centrality rather than one value for everyone.
    # Size with density held constant - the area grows with the node count.
    "K-size": ("nodes", [40, 60, 90, 120, 150], ["--hop-spread", "--scale-area"]),
    # The same node counts in a fixed area, so this one is density rather than size. Running both is
    # the only way to say which of the two any effect belongs to.
    "K-density": ("nodes", [40, 60, 90, 120, 150], ["--hop-spread"]),
    # One hop limit for everyone. --no-hop-spread is not optional: with the spread on, --hop-limit
    # is never read and this block produced three identical rows.
    "K-hopspread": ("hop-limit", [3, 5, 7], ["--no-hop-spread"]),
    # Uniform hop limit against per-node 3-7 by centrality, everything else fixed.
    "K-spread": ("hop-spread", [False, True], []),
    # Adverts only other archives can act on; replays every node in earshot can use.
    "L-advert": ("advert-transport", ["broadcast", "dm"], []),
    "L-provide": ("provide-transport", ["dm", "broadcast"], []),
    # Filing a replay by its heard_ago rather than at the receiving tip. The bucket it came from can
    # only converge with the peer's if the object lands where it belongs.
    "M-replayorder": ("replay-ordering", ["tip", "heard"], []),
    # The same, with replays broadcast so bystanders can file them too - the combination the replay
    # header exists for.
    "M-combined": (
        "replay-ordering",
        ["tip", "heard"],
        ["--provide-transport", "broadcast"],
    ),
    # Spreading adverts in time. Under local numbering each server seals its own bucket whenever its
    # own 32nd message lands, so the synchronisation jitter would break is largely absent.
    "M-jitter": ("advert-jitter-s", [1, 30, 120, 600], []),
    "M-capacity": ("capacity", [4, 8, 16, 32, 50], []),
    # Placement under real numbering and per-node hop limits.
    "N-place": (
        "place",
        [
            "spread",
            "routers",
            "alternate-routers",
            "beside-router",
            "random-clients",
            "hops-apart",
        ],
        ["--hop-spread"],
    ),
    "N-hops": (
        "hops-apart",
        [1, 2, 3, 4, 5],
        ["--place", "hops-apart", "--hop-spread"],
    ),
    "N-servers": ("servers", [2, 3, 5, 8], ["--hop-spread"]),
    # Time of day. Text and position follow the clock; device timers do not.
    "P-diurnal": ("diurnal", ["flat", "sinusoid", "commuter"], []),
    # The catch-up window, which only means anything once traffic has a time of day.
    "P-catchup": (
        "catch-up-hours",
        ["", "02-06", "00-08"],
        ["--diurnal", "commuter", "--trigger", "bucket+interval"],
    ),
    # The presets deployed meshes run. Nothing slower than LONG_MODERATE is, past about 30 nodes:
    # a full LONG_SLOW payload holds the channel 14.3 s, so a few packets spend the whole budget.
    "P-preset": ("preset", ["SHORT_FAST", "LONG_FAST", "LONG_MODERATE"], []),
    # North America is heading for 500 kHz across the board. All three of these are BW500, so the arm
    # varies spreading factor with the bandwidth held at where the region is going.
    "P-bw500": ("preset", ["SHORT_TURBO", "MEDIUM_TURBO", "LONG_TURBO"], []),
    # Europe stays on 250 kHz and adds the narrow presets: EU_866 defaults to LITE_FAST and EU_N_868
    # to NARROW_SLOW. A European result that covers only the 250 kHz presets is already incomplete.
    "P-eu-presets": (
        "preset",
        ["SHORT_FAST", "LONG_FAST", "LITE_FAST", "NARROW_SLOW"],
        [],
    ),
    # Congestion scaling on against off, to size what the firmware's own throttling is worth.
    "P-congestion": ("no-congestion-scaling", [False, True], ["--nodes", "120"]),
    # Nothing, the incumbent chain walk, and the sketch - all at one seed, so `none`
    # is a paired baseline and every other cell is a difference rather than a comparison.
    "Q-protocol": ("protocol", ["none", "chain", "sr"], []),
    # The designated-node control: the same nodes in the same places, archive off then on, so what
    # serving costs a node and what reconciliation adds can be separated from where it sits.
    "Q-control": (
        "protocol",
        ["none", "sr"],
        ["--place", "hops-apart", "--hops-apart", "3"],
    ),
    # The denominator: an SF++ airtime share is a share of whatever the mesh broadcasts anyway, so
    # the device interval decides it as much as the protocol does.
    "Q-interval": ("broadcast-interval-s", [900, 3600, 10800, 43200], []),
    # centrality is what operators do; random is the control that separates the hop limit's own
    # effect from the siting of the nodes that happen to have raised it.
    "Q-hopassign": ("hop-assign", ["centrality", "random"], []),
    "Q-topology": (
        "topology",
        ["uniform", "clustered", "corridor", "hub"],
        [],
    ),
    # All six routers as servers, against three of them, against three nodes beside them. Same
    # mesh, same traffic; only who is holding the archive changes.
    "G-allrouters": ("servers", [3, 6], ["--place", "routers"]),
    # What the 2.8 fold-in is worth: same seed, mesh and traffic, only the rules change.
    # --- round four: stress past the node database, and emit tuning numbers ---
    # Mesh size against the store holding it. Above the diagonal is what the throttle cannot see.
    "R-oversubscribed": (
        "nodes",
        [120, 250, 500],
        ["--scale-area", "--hours", "24"],
    ),
    # The same node counts against a deliberately small store, so eviction is constant.
    "R-hotstore-stress": (
        "max-num-nodes",
        [10, 120, 250],
        ["--nodes", "250", "--scale-area", "--hours", "24"],
    ),
    # Which quantity should drive the throttle. hotstore saturates; truesize is the ideal ceiling.
    "R-congestion-input": (
        "congestion-input",
        ["hotstore", "truesize"],
        ["--nodes", "250", "--scale-area", "--hours", "24"],
    ),
    # How many retries an addressed reconciliation hop needs before delivery stops improving. Named
    # for the SF++ retry budget rather than R-repeats, which is the firmware's RepeatScalingModule.
    "R-srretries": ("sr-retries", [0, 1, 2, 4], ["--hours", "24"]),
    "R-firmware": ("profile", ["legacy", "2.8"], []),
    # Every node adopting a hop recommendation derived from what other adopters sent. Needs the
    # trace: a converged mean and an oscillating one look identical at the end of a run.
    "R-adopt": (
        "no-adopt-hop-recommendation",
        [False, True],
        ["--nodes", "120", "--hop-spread", "--trace-interval-s", "1800"],
    ),
    # Roof against basement is 26 dB, wider than most parameters here - so either the largest
    # uncontrolled variable in every other block, or proof they ran on too good a mesh.
    "R-siting": (
        "siting-mix",
        ["uniform", "local-typical", "event", "backbone"],
        [],
    ),
    # How far the firmware's estimator sits from the exhaustive count it approximates, as the mesh
    # outgrows its 128 entries. Reported truth / observed / estimated side by side.
    "R-hopscale": ("nodes", [60, 120, 250, 500], ["--scale-area", "--hop-spread"]),
    # Does traceroute learning pay for its own airtime? Each reply teaches a route for every node
    # beyond the learner, and this tree's corroboration guard refuses a share of what it is told.
    "R-traceroute": ("traceroute-per-hour", [0.0, 0.25, 1.0, 4.0], []),
    # The same, on a mesh whose hot store cannot hold it - where the overflow cache is the only
    # thing that can keep a route for the long tail.
    "R-traceroute-small": (
        "traceroute-per-hour",
        [0.0, 1.0],
        ["--nodes", "120", "--max-num-nodes", "20"],
    ),
    # The retry budget from both ends: a directed attempt to flood sooner, against airtime spent
    # making each attempt likelier to land. Swept together because they trade off the same budget.
    "R-dmmode": (
        "dm-mode",
        ["flood-only", "directed-with-late-flood", "m4-early-flood"],
        DM_LADDER,
    ),
    "R-crladder": ("coding-rate-ladder", [False, True], DM_LADDER),
    "R-dmmode-cr": (
        "dm-mode",
        ["directed-with-late-flood", "m4-early-flood"],
        DM_LADDER + ["--coding-rate-ladder"],
    ),
    # The cheapest rival to the archive: spend one extra relay of a text rather than replicate it
    # afterwards. Measured against the archive in the same arm rather than separately.
    "R-repeats": ("extra-repeats", [False, True], []),
    # The same, on a mesh busy enough for the suppression thresholds to be deciding it.
    "R-repeats-busy": ("extra-repeats", [False, True], ["--nodes", "120"]),
    # 64 bytes on every signable broadcast, against the reliability that buys. Report the share of
    # signable traffic that was actually signed rather than assuming all of it was.
    "R-signing": ("signature-policy", ["COMPATIBLE", "BALANCED", "STRICT"], []),
    # Signing puts 66 bytes on every non-PKI broadcast and each rebroadcast. The only arm that
    # turns it off inside 2.8, so the only way to separate its cost from 2.8's.
    "R-signing-cost": (
        "profile-flag",
        ["signing=false", "signing=true"],
        ["--profile", "2.8"],
    ),
    # Each node throttling on its own online count, against one coefficient for the whole mesh. The
    # firmware does the former; every figure measured here before did the latter.
    "R-congestion-mode": (
        "congestion-mode",
        ["static", "adaptive"],
        ["--nodes", "120"],
    ),
    # What the warm tier is worth on a mesh larger than the hot store: 0 is the pre-2.8 behaviour
    # of forgetting an evicted peer outright, and the rest is how much identity a node keeps.
    "R-warm": (
        "warm-num-nodes",
        [0, 25, 100, 2000],
        ["--nodes", "120", "--max-num-nodes", "20"],
    ),
    # Each series at its final release, stepping the whole rule set at once: what a mesh gained
    # per upgrade, rather than what any one rule is worth.
    "R-versions": ("profile", ["2.4", "2.5", "2.6", "2.7", "2.8"], []),
    # A mesh that has not finished upgrading. The share below runs 2.6 while the rest run 2.8, which
    # is the case the release notes never describe.
    "R-mixed": (
        "legacy-fraction",
        [0.0, 0.25, 0.5, 0.75],
        ["--old-profile", "2.5"],
    ),
    # The same, one series later: 2.6 already has next-hop routing, so this separates "some nodes
    # cannot route" from "some nodes cannot learn a route".
    "R-mixed-26": (
        "legacy-fraction",
        [0.0, 0.25, 0.5, 0.75],
        ["--old-profile", "2.6"],
    ),
    # The mesh nobody would build on purpose. Each arm removes one thing a real deployment has, so
    # a design that only holds up on baymesh-2026-08 with uniform siting shows it here.
    "X-nomute": ("role-mix", ["baymesh-2026-08", "no-mute", "all-routers"], []),
    "X-badrouters": (
        "role-placement",
        ["degree", "inverse", "random"],
        ["--role-mix", "baymesh-2026-08"],
    ),
    "X-siting": (
        "siting-mix",
        ["uniform", "local-typical", "basement-heavy"],
        ["--role-mix", "baymesh-2026-08"],
    ),
    # Everything wrong at once, against everything right, on a mesh dense enough to survive it.
    "X-worst": (
        "role-placement",
        ["degree", "inverse"],
        ["--role-mix", "no-mute", "--siting-mix", "local-typical", "--nodes", "120"],
    ),
    # Separate transmit and receive gain: an amplified node relays into places whose replies never
    # reach it. Watch one_way_links and cancelled_by_weaker_relay, not just reception.
    "X-amplifiers": ("amplifier-mix", ["none", "sprinkled", "arms-race"], []),
    # The field pathology: a PA fitted to exactly the nodes that hear worst.
    "X-amplify-worst": ("amplify-worst", [0.0, 0.1, 0.3], []),
    # Distance as its own variable. Read report["stretch"], quoted against the links at 1.0: the
    # share of live links is not comparable once the worst ones leave the graph.
    "X-stretch": ("stretch", [1.0, 1.25, 1.5, 2.0], []),
    # A noise floor that moves. `periodic` is the adversarial one and the one with real teeth on a
    # slow preset: a frame in flight when the emitter fires is gone regardless of link budget.
    "X-noise": (
        "noise-profile",
        ["none", "temporal", "transient", "periodic"],
        [],
    ),
    # The interferer's period against a fixed preset. The chance of being caught is (airtime + pulse)
    # / interval, so this arm is really asking how long a frame this mesh can afford to send.
    "X-pulse": (
        "noise-pulse-interval-ms",
        [30000, 10000, 4000, 2000],
        ["--noise-profile", "periodic"],
    ),
    # Tropospheric ducting. The reach is not the result - the contention and the routes learned
    # through links that then disappear are.
    "X-duct": ("duct-per-hour", [0.0, 0.25, 1.0], ["--duct-gain-db", "25"]),
    # A mesh stretched past what it can carry, against the duct that briefly makes it work. The
    # adversarial pair: reach that exists for half an hour, gets learned, and then does not.
    "X-stretch-duct": (
        "duct-per-hour",
        [0.0, 1.0],
        ["--stretch", "1.5", "--duct-gain-db", "25"],
    ),
    # Position and telemetry turned up, which is what an operator does when the map looks stale.
    "X-chatty": ("broadcast-interval-s", [3600, 900, 300], []),
    # The same, with the hop limit raised too - the other half of that instinct.
    "X-chatty-hops": (
        "broadcast-interval-s",
        [3600, 900, 300],
        ["--no-hop-spread", "--hop-limit", "7"],
    ),
    # Hop limits past what the 3-bit field can carry. See the manual: above 7 this is a wire-format
    # question as much as a routing one.
    "F-hoplimit": ("hop-limit", [3, 7, 15, 32], ["--no-hop-spread"]),
    # Every node relaying everything, against the roles that exist to stop that.
    "F-flooding": (
        "role-mix",
        ["baymesh-2026-08", "all-routers"],
        ["--rebroadcast-mode", "ALL"],
    ),
    # The turbo corners of the SF/bandwidth curve, including two presets no release has.
    "F-preset-turbo": (
        "preset",
        [
            "EXTRA_SHORT_TURBO",
            "SHORT_TURBO",
            "LONG_FAST",
            "LONG_TURBO",
            "EXTRA_LONG_TURBO",
        ],
        [],
    ),
    # What a polite mesh costs: the region limit is a ceiling, not an obligation.
    "F-txpower": ("tx-power", [30, 22, 17, 14], []),
    # The roles 2.8 added. ROUTER_LATE only speaks when the mesh still needs it, so promoting the
    # spine to it should cut relay airtime without costing reach - which is the claim to test.
    "R-routerlate": ("router-late-fraction", [0.0, 0.05, 0.1, 0.2], []),
    # A hop between two favourited routers is free in 2.8. On a mesh whose diameter already
    # exceeds the hop limit, that is the difference between reaching the far end and not.
    "R-favourites": ("favourite-routers", [False, True], ["--router-fraction", "0.15"]),
    # Everything routing knows is bounded by a small per-board store. Run with its consumers
    # engaged, or nothing reads it and every mix ties.
    "R-platform": (
        "platform-mix",
        ["uniform", "baymesh-2026-08", "constrained"],
        ["--favourite-routers", "--router-fraction", "0.2"],
    ),
    # The same question as one number rather than a board mix, so the trend is readable: 10 is an
    # STM32WL, 120 the nRF52840 default, 250 a 16 MB S3. A 60-node mesh does not fit in the first.
    "R-hotstore": (
        "max-num-nodes",
        [10, 100, 120, 250],
        ["--favourite-routers", "--router-fraction", "0.2"],
    ),
    # Measured role shares - 4% ROUTER, 3% ROUTER_LATE, 16% CLIENT_BASE, 18% CLIENT_MUTE - against
    # the 10%-ROUTER default. Run with and without favourites, which decides the sign of the effect.
    "R-roles": (
        "role-mix",
        ["legacy-default", "baymesh-2026-08"],
        [],
    ),
    "R-roles-fav": (
        "role-mix",
        ["legacy-default", "baymesh-2026-08"],
        ["--favourite-routers"],
    ),
    # What a restrictive rebroadcast mode costs when the store is too small to remember who is who.
    "R-rebroadcast": (
        "rebroadcast-mode",
        ["ALL", "KNOWN_ONLY", "CORE_PORTNUMS_ONLY"],
        ["--platform-mix", "baymesh-2026-08"],
    ),
}


# One sentence per block for a reader of the results: what moved, where the comments above say
# why the block exists. test_mesh holds every block to having one.
DESCRIPTIONS = {
    "D-cadence": "When an archive advertises: on a sealed bucket, a fixed interval, AIMD, or both.",
    "D-resolve": "How two archives settle a disagreement - send a sketch, enumerate, or sketch then fall back. Delivery should not move; what it costs should.",
    "D-jitter": "Spread applied to bucket-close under global numbering, where every archive seals the same bucket at the same moment and fires together.",
    "E-capacity": "How many differences one sketch can decode before it fails and the exchange escalates.",
    "E-width": "Sketch member width. Narrower identifiers collide more often, and a collision cancels in the sketch without cancelling in the checksum.",
    "E-signed": "Whether the advert carries its 66-byte signature.",
    "F-loss": "A flat loss floor on every reception - degradation spread evenly across every bucket.",
    "F-burst": "The same nominal loss delivered in 60-second stretches of deafness, which puts a whole bucket's divergence into one sketch instead of spreading it.",
    "F-outage": "Burst loss at half an hour rather than a minute - most of a bucket, which is the outage that actually matters to an archive.",
    "G-place": "Where the archives sit, under a flat hop limit.",
    "G-hops": "How many hops apart the archives are placed, under a flat hop limit.",
    "G-servers": "How many archives the mesh has, under a flat hop limit.",
    "J-bucketmode": "What defines a bucket: a global counter (a fiction kept as an upper bound), the local count the firmware keeps, a time window, or a sliding window.",
    "J-window": "Objects in the sliding window, when buckets are windowed.",
    "J-wincap": "Sketch capacity under windowed buckets rather than counted ones.",
    "J-timewin": "Width of the time bucket, when buckets are cut by the clock.",
    "K-size": "Mesh size with density held constant - the area grows with the node count.",
    "K-density": "The same node counts in a fixed area, so this is density rather than size. Running both is the only way to say which an effect belongs to.",
    "K-hopspread": "One hop limit for everyone, swept. The per-node spread must be off or --hop-limit is never read.",
    "K-spread": "A uniform hop limit against per-node limits of 3-7 assigned by centrality.",
    "L-advert": "Whether an archive advertises by broadcast or by DM to each known peer.",
    "L-provide": "Whether a replay goes by DM or by broadcast, so bystanders in earshot can file it too.",
    "M-replayorder": "Where a replayed object lands in the receiver's stream: at the tip, or back at its heard_ago.",
    "M-combined": "The same, with replays broadcast - the combination the replay header exists for.",
    "M-jitter": "Advert spread under local numbering, where each archive seals its own bucket on its own count and the synchronisation jitter would break is largely absent.",
    "M-capacity": "Sketch capacity under local numbering and the later defaults.",
    "N-place": "Where the archives sit, under real per-node hop limits.",
    "N-hops": "How many hops apart the archives are, under real per-node hop limits.",
    "N-servers": "How many archives the mesh has, under real per-node hop limits.",
    "P-diurnal": "Time of day. Text, position and DMs follow the clock; telemetry and nodeinfo are device timers and do not.",
    "P-catchup": "The quiet-hours window reconciliation defers to, which only means anything once traffic has a time of day.",
    "P-preset": "The presets deployed meshes actually run: the default, the fast end, and the slow end still in use.",
    "P-bw500": "Spreading factor with bandwidth held at 500 kHz, where North America is heading.",
    "P-eu-presets": "The presets Europe runs, including the narrow ones EU_866 and EU_N_868 default to.",
    "P-congestion": "The firmware's node-count interval scaling, on against off.",
    "Q-protocol": "Nothing, the incumbent chain walk, and the sketch - with `none` a paired baseline, so every other cell is a difference rather than a comparison.",
    "Q-control": "The same nodes in the same places with the archive off then on, separating what serving costs a node from where it sits.",
    "Q-interval": "The device broadcast interval - the denominator every SF++ airtime share is quoted against.",
    "Q-hopassign": "Whether raised hop limits land on central nodes as operators do it, or at random - the control that separates the limit's effect from the siting of the nodes that raised it.",
    "Q-topology": "The shape of the mesh, at fixed node count and seed.",
    "G-allrouters": "Every router as an archive against half of them - same mesh, same traffic, only who holds the archive changes.",
    "R-oversubscribed": "Mesh size against a store that has to hold it, over a full day.",
    "R-hotstore-stress": "The store size against a fixed 250-node mesh, so eviction is constant.",
    "R-congestion-input": "Which quantity drives the throttle: what the firmware can see and which saturates, or the unbounded ideal.",
    "R-srretries": "Retries per addressed reconciliation hop, to find where delivery stops improving.",
    "R-firmware": "The pre-fold-in transport against 2.8 - same seed, same mesh, only the MAC and routing rules change.",
    "R-adopt": "The hop-recommendation feedback loop closed against held open, traced, because a converged mean and an oscillating one look identical at the end.",
    "R-siting": "Where nodes physically are. A roof node and a basement one are 26 dB apart, wider than most parameters here.",
    "R-hopscale": "How far the firmware's hop estimator sits from the exhaustive count it approximates, as the mesh outgrows its 128 entries.",
    "R-traceroute": "Route discoveries per node per hour - whether traceroute learning pays for its own airtime.",
    "R-traceroute-small": "The same on a mesh whose hot store cannot hold it, where the overflow cache is all that keeps a route for the long tail.",
    "R-dmmode": "How a DM escalates to flooding.",
    "R-crladder": "Raising the coding rate on each retransmission - airtime spent to make each attempt likelier to land.",
    "R-dmmode-cr": "DM escalation with the coding-rate ladder already on, since both spend the same retry budget.",
    "R-repeats": "The cheapest rival to an archive: one extra relay of a text rather than replicating it afterwards.",
    "R-repeats-busy": "The same, on a mesh busy enough for the suppression thresholds to be deciding it.",
    "R-signing": "The receive-side signature policy - what a node does with an unsigned packet.",
    "R-signing-cost": "Signing itself, on against off inside 2.8. The only arm that separates 'signing costs reach' from '2.8 costs reach'.",
    "R-congestion-mode": "Each node throttling on its own online count against one coefficient for the whole mesh. The firmware does the former.",
    "R-warm": "The warm tier on a mesh larger than the hot store: 0 is the pre-2.8 behaviour of forgetting an evicted peer outright.",
    "R-versions": "The release series in order, each at its final release - what a mesh gained or lost per upgrade, not what one rule is worth.",
    "R-mixed": "A mesh part-way through upgrading, the older share on 2.5.",
    "R-mixed-26": "The same with the older share on 2.6.",
    "X-nomute": "The role census: a real mesh's mix, the same without muted clients, and everything a router.",
    "X-badrouters": "Where the router roles land - on the best-connected nodes, the worst, or at random.",
    "X-siting": "Siting against a real role census, including a basement-heavy mesh.",
    "X-worst": "Router roles on the worst-connected nodes of an already badly sited mesh - the adversarial case.",
    "X-amplifiers": "Power amplifiers as separate transmit and receive gain, sprinkled or in an arms race.",
    "X-amplify-worst": "A high amplifier fitted to the worst-connected nodes after the links exist - the field pathology where the node nobody could hear is then heard by everyone while still hearing almost nobody.",
    "X-stretch": "Every distance scaled about the centroid: the same nodes in the same arrangement, further apart.",
    "X-noise": "The noise floor: none, a smooth field, episodic bursts, or a regular emitter that wipes whatever is in flight.",
    "X-pulse": "How often the periodic emitter fires.",
    "X-duct": "Tropospheric ducting episodes per hour. Not a free gain - read ducted receptions beside collisions.",
    "X-stretch-duct": "Ducting on a stretched mesh, where the long links it creates are the ones that were missing.",
    "X-chatty": "The device broadcast interval driven down to three times its default rate.",
    "X-chatty-hops": "The same, with every node on a flat hop limit of 7 so nothing damps the flood.",
    "F-hoplimit": "Hop limits past anything a release ships, to find where more hops stop helping.",
    "F-flooding": "Every node rebroadcasting everything, against a real role census.",
    "F-preset-turbo": "Presets from the fastest the firmware ships to the slow end.",
    "F-txpower": "Transmit power in dBm - the region limit is a ceiling an operator may use, not one they must.",
    "R-routerlate": "The share of nodes on ROUTER_LATE.",
    "R-favourites": "Router-like nodes favouriting each other, so relays between them keep their hop limit.",
    "R-platform": "The board mix, which decides each node's hot-store size.",
    "R-hotstore": "The modelled MAX_NUM_NODES - the size of the hot store.",
    "R-roles": "The legacy default role census against a real mesh's.",
    "R-roles-fav": "The same with router favourites on.",
    "R-rebroadcast": "The rebroadcast mode - what a node relays.",
}


def cell_argv(arm, value, extra):
    """The command line for one cell of a block.

    A false arm emits the negation: omitting the flag lands on a default that may be true.
    """
    argv = list(BASE) + list(extra)
    if isinstance(value, bool):
        if value:
            argv.append(f"--{arm}")
        elif _flag_default(arm) is True:
            negation = f"--no-{arm}"
            if negation not in _known_flags():
                raise ValueError(
                    f"--{arm} defaults to true and has no {negation}; "
                    f"a false arm cannot be expressed and would repeat the true one"
                )
            argv.append(negation)
    else:
        argv += [f"--{arm}", str(value)]
    return argv


@lru_cache(maxsize=1)
def _known_flags():
    return {opt for a in build_parser()._actions for opt in a.option_strings}


@lru_cache(maxsize=None)
def _flag_default(arm):
    for action in build_parser()._actions:
        if f"--{arm}" in action.option_strings:
            return action.default
    return None


# Named groups, so a batch is launched by what it asks rather than by which blocks belong
# together. Cheap first within each, so results accumulate instead of waiting on the largest.
BATCHES = {
    # ---- PROPOSED: things that could be adopted, each against its own control ------------------
    # Does this change earn its airtime? Every arm here has a "without it" cell.
    "proposed-archive": ["Q-protocol", "Q-control", "R-srretries"],
    "proposed-relay": [
        "R-repeats",
        "R-repeats-busy",
        "R-crladder",
        "R-dmmode",
        "R-dmmode-cr",
    ],
    "proposed-routing": [
        "R-traceroute",
        "R-traceroute-small",
        "R-adopt",
        "R-favourites",
    ],
    # ---- VERSIONING: what a release is worth, and what a half-upgraded mesh costs -------------
    "versioning": [
        "R-firmware",
        "R-versions",
        "R-mixed",
        "R-mixed-26",
        "R-signing-cost",
        "R-signing",
    ],
    "versioning-hops": ["K-hopspread", "K-spread", "Q-hopassign"],
    # ---- ADVERSARIAL: remove the things known to help, one at a time --------------------------
    # Each arm deletes an improver rather than adding a stressor, so the loss is attributable.
    "adversarial": ["X-nomute", "X-badrouters", "X-siting", "X-worst"],
    "adversarial-radio": ["X-amplifiers", "X-amplify-worst"],
    # Distance, a moving floor, and a duct: the three that decide what a link is worth.
    "propagation": ["X-stretch", "X-noise", "X-pulse", "X-duct", "X-stretch-duct"],
    # Where the deployed meshes are and where the two big regions are going.
    "presets": ["P-preset", "P-bw500", "P-eu-presets"],
    "adversarial-load": ["X-chatty", "X-chatty-hops"],
    # ---- FUTURE: beyond any release, to find where the design stops working -------------------
    "future-hops": ["F-hoplimit", "F-flooding"],
    "future-radio": ["F-preset-turbo", "F-txpower"],
    # ---- CONTROLS: the mesh these are all measured against ------------------------------------
    "shape": ["R-platform", "R-siting", "Q-topology", "K-density", "K-size"],
    "scale": ["R-hotstore", "R-hopscale", "R-hotstore-stress", "R-oversubscribed"],
    "load": ["Q-interval", "P-diurnal", "P-preset", "P-congestion", "P-catchup"],
    "mechanisms": [
        "R-roles",
        "R-roles-fav",
        "R-routerlate",
        "R-rebroadcast",
        "R-congestion-mode",
        "R-warm",
        "R-congestion-input",
    ],
    # ---- ARCHIVE INTERNALS: how the sketch itself is tuned, not whether to have it -------------
    "archive-cadence": ["D-cadence", "D-jitter", "D-resolve", "M-jitter"],
    "archive-sketch": ["E-capacity", "E-width", "E-signed", "M-capacity"],
    "archive-buckets": ["J-bucketmode", "J-window", "J-wincap", "J-timewin"],
    "archive-placement": [
        "G-place",
        "G-hops",
        "G-servers",
        "G-allrouters",
        "N-place",
        "N-hops",
        "N-servers",
    ],
    "archive-transport": ["L-advert", "L-provide", "M-replayorder", "M-combined"],
    "degradation": ["F-loss", "F-burst", "F-outage"],
}


def run_block(name, seeds, out_dir, grid=None):
    arm, values, extra = BLOCKS[name]
    parser = build_parser()
    results = []
    for value in values:
        for seed in seeds:
            argv = cell_argv(arm, value, extra)
            if grid:
                argv += grid
            opts = parser.parse_args(argv)
            started = time.time()
            report = run_once(opts, seed)
            report["block"] = name
            report["arm"] = arm
            report["value"] = value
            report["grid"] = grid or []
            results.append(report)
            print(
                f"  {name} {arm}={value} seed={seed} {time.time() - started:.0f}s",
                flush=True,
            )
            line(report)
    suffix = ""
    if grid:
        # A grid run is a different experiment, not a rerun of the same one, so it gets its own
        # file. Without this the second capacity in a capacity-by-loss sweep overwrites the first.
        suffix = "-" + "-".join(g.lstrip("-") for g in grid).replace(" ", "")
    # --grid is free text and lands in the filename, so the whole stem is sanitised rather than
    # trusted: `--grid "--scenario ../x"` would otherwise write outside the run directory.
    path = os.path.join(out_dir, safe_name(f"{name}{suffix}") + ".json")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w") as f:
        json.dump(results, f, indent=2)
    table(name, arm, values, results)
    reception_table(name, arm, values, results)
    print(f"wrote {path}")
    chart = AC.auto(results, path, kind="block")
    if chart:
        print(f"wrote {chart}")
    # The per-portnum statistics, text first, beside the table - so a block's output is readable
    # without a second command and without anyone having to remember to run one. Written to disk as
    # well as printed: an unattended run's stdout is not always kept, and the block's own directory
    # is where anyone looks afterwards.
    text = RP.report_block(path)
    print(text)
    text_path = os.path.join(out_dir, "reports", safe_name(f"{name}{suffix}") + ".txt")
    os.makedirs(os.path.dirname(text_path), exist_ok=True)
    with open(text_path, "w") as f:
        f.write(text + "\n")
    print(f"wrote {text_path}")
    return results


def line(report):
    s = report.get("sfpp")
    if not s:
        return
    print(
        f"    held {s['held_fraction_mean']:.3f} union {s['union_fraction']:.3f} "
        f"adverts {s['adverts']} moved {s['objects_moved']} "
        f"fail {s['decode_failures']} mis {s['misdecodes']} esc {s['escalations']} "
        f"SRair {s['sr_airtime_share']:.1%} silent {s['silent_losses']}/"
        f"{s['audit_checksum_agrees_sets_differ']}",
        flush=True,
    )


def table(name, arm, values, results):
    """One row per cell, averaged over the block's seeds."""
    print(f"\n=== {name} ===")
    header = (
        f"{arm:>18} | held  union | adverts moved | SRbytes  SRair | "
        f"fail mis esc | silent"
    )
    print(header)
    print("-" * len(header))
    rows = []
    for value in values:
        cells = [r for r in results if r["value"] == value and "sfpp" in r]
        if not cells:
            continue
        g = lambda k: statistics.mean(c["sfpp"][k] for c in cells)  # noqa: E731
        row = {
            "value": value,
            "held": g("held_fraction_mean"),
            "union": g("union_fraction"),
            "adverts": g("adverts"),
            "moved": g("objects_moved"),
            "sr_bytes": g("sr_bytes"),
            "sr_airtime_share": g("sr_airtime_share"),
            "decode_failures": g("decode_failures"),
            "misdecodes": g("misdecodes"),
            "escalations": g("escalations"),
            "silent": g("silent_losses") + g("audit_checksum_agrees_sets_differ"),
            "reception": statistics.mean(
                c["baseline"]["text_reception_mean"] for c in cells
            ),
        }
        rows.append(row)
        print(
            f"{str(value):>18} | {row['held']:.3f} {row['union']:.3f} | "
            f"{row['adverts']:7.0f} {row['moved']:5.0f} | "
            f"{row['sr_bytes']:7.0f} {row['sr_airtime_share']:6.1%} | "
            f"{row['decode_failures']:4.0f} {row['misdecodes']:3.0f} {row['escalations']:3.0f} | "
            f"{row['silent']:.0f}"
        )
    return rows


def reception_table(name, arm, values, results):
    """What each arm did to delivery, read at the tails rather than the mean.

    p10 is the node an arm has to help to be worth its airtime; `all` catches displaced traffic.
    """
    print(f"\n=== {name} - reception ===")
    header = (
        f"{arm:>18} | text p10   med   p90 | all  p10   med   p90 | "
        f"demand  node% | txs     coll"
    )
    print(header)
    print("-" * len(header))
    rows = []
    for value in values:
        cells = [r for r in results if r["value"] == value and "by_class" in r]
        if not cells:
            continue

        def dist(cls, stat, cells=cells):
            got = [
                c["by_class"][cls]["per_node_reception"][stat]
                for c in cells
                if cls in c["by_class"]
            ]
            return statistics.mean(got) if got else float("nan")

        def traffic(key, cells=cells):
            return statistics.mean(c["traffic"][key] for c in cells)

        row = {
            "value": value,
            "text_p10": dist("text", "p10"),
            "text_median": dist("text", "median"),
            "text_p90": dist("text", "p90"),
            "all_p10": dist("all", "p10"),
            "all_median": dist("all", "median"),
            "all_p90": dist("all", "p90"),
            "channel_utilisation": traffic("channel_utilisation"),
            "node_util_median": (
                statistics.mean(
                    c["traffic"]["node_channel_util_percent"]["median"]
                    for c in cells
                    if "node_channel_util_percent" in c["traffic"]
                )
                if any("node_channel_util_percent" in c["traffic"] for c in cells)
                else float("nan")
            ),
            "nodes_receiving_none": statistics.mean(
                c["by_class"]["text"]["nodes_receiving_none"] for c in cells
            ),
            "transmissions": traffic("transmissions"),
            "lost_to_collision": traffic("lost_to_collision"),
        }
        rows.append(row)
        print(
            f"{str(value):>18} | {row['text_p10']:9.3f} {row['text_median']:5.3f} {row['text_p90']:5.3f} | "
            f"{row['all_p10']:8.3f} {row['all_median']:5.3f} {row['all_p90']:5.3f} | "
            f"{row['channel_utilisation']:6.2f} {row['node_util_median']:5.1f}% | "
            f"{row['transmissions']:7.0f} {row['lost_to_collision']:8.0f}"
        )
    return rows


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--block", action="append", help="repeatable; omit with --list")
    ap.add_argument(
        "--batch",
        action="append",
        help="a named group of blocks, repeatable: " + ", ".join(sorted(BATCHES)),
    )
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--seeds", type=int, default=3)
    ap.add_argument(
        "--seed-base", type=int, help="omit to draw random seeds and record them"
    )
    ap.add_argument("--out", default=".")
    # A single quoted string, not nargs: argparse would read the leading "--" of the extra flags
    # as options of this parser rather than payload.
    ap.add_argument(
        "--grid",
        default=None,
        help='extra flags for every cell, quoted: --grid "--capacity 8"',
    )
    opts = ap.parse_args(argv)

    # A batch is a name for a group of blocks; --block and --batch add to the same list, so the two
    # can be mixed and a batch can be extended with one extra block on the command line.
    blocks = list(opts.block or [])
    for batch in opts.batch or []:
        if batch not in BATCHES:
            ap.error(f"unknown batch {batch!r}; known: {', '.join(sorted(BATCHES))}")
        blocks += [b for b in BATCHES[batch] if b not in blocks]

    if opts.list or not blocks:
        for name, (arm, values, grid) in BLOCKS.items():
            suffix = f"   [{' '.join(grid)}]" if grid else ""
            print(f"{name:20} {arm} = {values}{suffix}")
        print()
        for batch, names in sorted(BATCHES.items()):
            print(f"batch {batch:12} {' '.join(names)}")
        return 0

    unknown = [b for b in blocks if b not in BLOCKS]
    if unknown:
        ap.error(f"unknown block(s): {', '.join(unknown)}")

    if opts.seed_base is None:
        seeds = [random.SystemRandom().randrange(1 << 31) for _ in range(opts.seeds)]
    else:
        seeds = [opts.seed_base + i for i in range(opts.seeds)]
    print(f"seeds {seeds}")

    for name in blocks:
        run_block(name, seeds, opts.out, grid=opts.grid.split() if opts.grid else None)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
