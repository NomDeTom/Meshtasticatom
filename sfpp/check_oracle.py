"""Differential test: the Python sketch against the firmware's C++, case for case.

`pinsketch.py` is a transcription of `src/modules/Native/PinSketch.cpp`, not a reimplementation of
it, and the simulator's conclusions are only worth anything if its sketches are the bytes the
firmware would actually put on the air. This compiles the firmware's own source and diffs the two
implementations case for case, rather than asserting properties of the port alone.

The firmware is a separate repository, so its source has to be found:

    MESHTASTIC_FIRMWARE_ROOT=/path/to/firmware python3 -m sfpp.check_oracle

Without it, a sibling checkout is tried (../MeshtasticFirmware, ../firmware). With no firmware
source reachable the check reports that and exits 0 - it is a cross-repository check and a tree
that cannot see the firmware has not failed anything. Pass --require to turn that into a failure,
which is what a CI job that means to run it should do.

Exit code is non-zero on any divergence.
"""

import os
import random
import subprocess
import sys

from . import pinsketch, sketchindex

HERE = os.path.dirname(os.path.abspath(__file__))
ORACLE = os.path.join(HERE, "oracle")

# Where the firmware's PinSketch lives inside a firmware checkout.
FIRMWARE_SOURCE = os.path.join("src", "modules", "Native")


def firmware_root():
    """Find the firmware checkout to compile against, or None if none is reachable."""

    def holds_firmware(root):
        return bool(root) and os.path.isfile(
            os.path.join(root, FIRMWARE_SOURCE, "PinSketch.cpp")
        )

    # An explicit path is answered with itself or with an error, never with somewhere else. The
    # first version fell through to the sibling search when the named path was wrong, so a typo in
    # MESHTASTIC_FIRMWARE_ROOT produced 628 passing checks against a checkout the caller had not
    # asked for - a default silently substituting for a request, which is trap 1 in this tree's
    # own list.
    named = os.environ.get("MESHTASTIC_FIRMWARE_ROOT")
    if named:
        if holds_firmware(named):
            return named
        sys.exit(
            f"MESHTASTIC_FIRMWARE_ROOT={named!r} has no {FIRMWARE_SOURCE}/PinSketch.cpp"
        )

    # A sibling checkout is the usual local arrangement, and was the only one before the move.
    parent = os.path.dirname(os.path.dirname(HERE))
    for root in (
        os.path.join(parent, "MeshtasticFirmware"),
        os.path.join(parent, "firmware"),
    ):
        if holds_firmware(root):
            return root
    return None


def build_oracle(root):
    """Compile the vector generator against the firmware's own PinSketch.cpp."""
    native = os.path.join(root, FIRMWARE_SOURCE)
    cmd = [
        "g++",
        "-O2",
        "-I",
        native,
        "-o",
        ORACLE,
        os.path.join(HERE, "oracle.cpp"),
        os.path.join(native, "PinSketch.cpp"),
    ]
    built = subprocess.run(cmd, capture_output=True, text=True)
    if built.returncode:
        sys.exit(f"oracle did not compile:\n{built.stderr}")
    return ORACLE


class Oracle:
    def __init__(self):
        if not os.path.exists(ORACLE):
            sys.exit(f"oracle not built - see the docstring in {__file__}")
        self.proc = subprocess.Popen(
            [ORACLE],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            bufsize=1,
        )

    def ask(self, line):
        self.proc.stdin.write(line + "\n")
        self.proc.stdin.flush()
        return self.proc.stdout.readline().strip()

    def close(self):
        self.proc.stdin.close()
        self.proc.wait()


failures = []
checks = 0


def check(name, got, want):
    global checks
    checks += 1
    if got == want:
        return
    failures.append(name)
    print(f"  FAIL  {name}\n        python {got!r}\n        c++    {want!r}")


def decoded_str(elements):
    return "fail" if elements is None else " ".join(str(e) for e in elements)


def check_field(oracle, rng):
    print("field arithmetic against the C++")
    values = [1, 2, 3, 0x80000000, 0xFFFFFFFF] + [
        rng.getrandbits(32) for _ in range(40)
    ]
    for a in values:
        for b in values[:8]:
            check(f"mul({a},{b})", str(pinsketch.mul(a, b)), oracle.ask(f"mul {a} {b}"))
        if a:
            check(f"inv({a})", str(pinsketch.inv(a)), oracle.ask(f"inv {a}"))
    print(f"  {checks} field checks")


def check_sketches(oracle, rng):
    print("sketch bytes and decode against the C++")
    for cap in (1, 2, 4, 6, 8, 16, 32):
        for trial in range(12):
            # Sizes straddle the capacity so over-capacity behaviour is compared too, including
            # the ~1/c! misdecodes - those must agree, not merely both be "wrong".
            n = rng.randint(0, cap + 3)
            elements = [rng.getrandbits(32) or 1 for _ in range(n)]
            args = " ".join(str(e) for e in elements)

            s = pinsketch.Sketch(cap)
            for e in elements:
                s.add(e)
            check(
                f"cap={cap} n={n} bytes",
                s.serialize().hex(),
                oracle.ask(f"sketch {cap} {args}"),
            )
            check(
                f"cap={cap} n={n} decode",
                decoded_str(s.decode()),
                oracle.ask(f"decode {cap} {args}"),
            )


def check_differences(oracle, rng):
    print("symmetric difference against the C++")
    for cap in (2, 4, 8, 32):
        for trial in range(10):
            shared = [rng.getrandbits(32) or 1 for _ in range(rng.randint(0, 20))]
            only_a = [rng.getrandbits(32) or 1 for _ in range(rng.randint(0, cap + 2))]
            only_b = [rng.getrandbits(32) or 1 for _ in range(rng.randint(0, cap + 2))]

            a = pinsketch.Sketch(cap)
            for e in shared + only_a:
                a.add(e)
            b = pinsketch.Sketch(cap)
            for e in shared + only_b:
                b.add(e)
            a.merge(b)

            left = shared + only_a
            right = shared + only_b
            args = f"{len(left)} " + " ".join(str(e) for e in left + right)
            check(
                f"cap={cap} diff {len(only_a)}+{len(only_b)}",
                decoded_str(a.decode()),
                oracle.ask(f"diff {cap} {args}"),
            )


def check_truncation():
    """A capacity-c sketch must be a prefix of any larger one - what makes prefix streaming work."""
    print("truncation is exact")
    rng = random.Random(7)
    elements = [rng.getrandbits(32) or 1 for _ in range(20)]
    big = pinsketch.Sketch(32)
    for e in elements:
        big.add(e)
    for cap in (1, 2, 4, 8, 16):
        small = pinsketch.Sketch(cap)
        for e in elements:
            small.add(e)
        cut = big.copy()
        cut.truncate(cap)
        check(f"truncate to {cap}", cut.serialize().hex(), small.serialize().hex())


def check_identifiers():
    """SHA-256 derivations, pinned to literal values so a domain-string change fails loudly."""
    print("identifier derivation")
    import hashlib

    object_id = bytes(range(16))
    digest = hashlib.sha256(object_id).digest()
    check(
        "short id is the first non-zero big-endian word",
        sketchindex.short_id(object_id),
        int.from_bytes(digest[:4], "big"),
    )
    salted = hashlib.sha256(b"sfpp-ck-v3" + object_id).digest()
    check(
        "checksum contribution is 8 big-endian bytes",
        sketchindex.checksum_contribution(object_id),
        int.from_bytes(salted[:8], "big"),
    )
    check("empty object has no short id", sketchindex.short_id(b""), 0)
    check("counter 0 has no bucket", sketchindex.bucket_of(0), None)
    check("counter 1 is bucket 0", sketchindex.bucket_of(1), 0)
    check("counter 32 is bucket 0", sketchindex.bucket_of(32), 0)
    check("counter 33 is bucket 1", sketchindex.bucket_of(33), 1)
    check("bucket 1 covers 33..64", sketchindex.bucket_range(1), (33, 64))


def check_checksum_catches_collision():
    """The load-bearing property: a short-ID collision cancels in the sketch, not in the checksum."""
    print("a short-ID collision cancels in the sketch but not the checksum")
    a = BucketSummaryPair()
    check("colliding pair leaves an empty sketch", a.sketch_empty, True)
    check("colliding pair leaves a non-zero checksum", a.checksum_nonzero, True)


class BucketSummaryPair:
    def __init__(self):
        summary = sketchindex.BucketSummary(capacity=4)
        # Two distinct objects forced to the same short ID, with their own contributions.
        summary.add(0xDEADBEEF, 0x1111111111111111)
        summary.add(0xDEADBEEF, 0x2222222222222222)
        self.sketch_empty = summary.sketch().empty()
        self.checksum_nonzero = summary.checksum != 0


def main(argv=None):
    require = "--require" in (argv if argv is not None else sys.argv[1:])
    root = firmware_root()
    if root is None:
        message = (
            "no Meshtastic firmware checkout found, so the Python sketch cannot be diffed against "
            "the C++ it transcribes. Set MESHTASTIC_FIRMWARE_ROOT to a firmware checkout."
        )
        if require:
            sys.exit(f"FAIL: {message}")
        print(f"SKIP: {message}")
        return 0
    print(f"oracle: compiling against {root}")
    build_oracle(root)

    rng = random.Random(20260816)
    oracle = Oracle()
    try:
        check_field(oracle, rng)
        check_sketches(oracle, rng)
        check_differences(oracle, rng)
    finally:
        oracle.close()
    check_truncation()
    check_identifiers()
    check_checksum_catches_collision()

    print(f"\n{checks - len(failures)}/{checks} checks passed")
    if failures:
        print("failed: " + ", ".join(failures[:10]))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
