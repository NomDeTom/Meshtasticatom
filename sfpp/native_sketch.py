"""Route Sketch.decode through the vendored C++ instead of the Python transcription.

Decoding is where a sketch costs anything. `Sketch.add` is a handful of XORs against cached odd
powers; `decode` is Berlekamp-Massey and root-finding over GF(2^32), and in Python it was measured
at 62.9% of a 12-hour 150-node run - 75.5 s across 199 calls, about 0.38 s each. The same work is
microseconds in the C++ this module compiles.

199 calls is what makes this worth doing over a pipe. A round trip is tens of microseconds, so the
whole run's IPC is a rounding error against 75.5 s; wrapping `mul` instead - 10.1M calls - would
have spent more on the pipe than it saved.

This is off unless asked for. The Python stays the reference and the fallback, because it is what
check_oracle holds to the firmware and what runs where no compiler is reachable. Enabling it is
therefore a claim about speed only, never about results, and `verify()` is what makes that claim
checkable rather than assumed.

    SFPP_NATIVE_SKETCH=1 python3 -m sfpp.campaign ...
    python3 -m sfpp.native_sketch --scale 1.0      # diff both decoders, exit 1 on any disagreement
"""

import os
import random
import subprocess
import sys
import time

from . import check_oracle, pinsketch

_proc = None
_python_decode = None


def _binary():
    """The compiled oracle, built if it is not already there."""
    root = check_oracle.firmware_root()
    if root is None and not os.path.isfile(
        os.path.join(check_oracle.VENDORED, "PinSketch.cpp")
    ):
        raise RuntimeError("no PinSketch source to compile: neither firmware nor vendored")
    return check_oracle.build_oracle(root)


def start():
    """Bring up the decoder process, or raise. Never falls back quietly.

    A silent fallback would turn "this run was slow" into the only symptom of a broken build, and
    the run would still be reported as native.
    """
    global _proc
    if _proc is not None:
        return _proc
    _proc = subprocess.Popen(
        [_binary()],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
        bufsize=1,
    )
    return _proc


def stop():
    global _proc
    if _proc is not None:
        try:
            _proc.stdin.close()
            _proc.wait(timeout=5)
        except Exception:
            _proc.kill()
        _proc = None


def decode(syndromes):
    """One decode over the pipe. Returns a sorted list, or None where the sketch is not decodable."""
    proc = start()
    proc.stdin.write(
        f"decodesyn {len(syndromes)} {' '.join(str(s) for s in syndromes)}\n"
    )
    proc.stdin.flush()
    line = proc.stdout.readline()
    if not line:
        raise RuntimeError("the native decoder exited mid-run")
    line = line.strip()
    if line == "fail":
        return None
    return [int(x) for x in line.split()] if line else []


def _decode_native(self):
    """Sketch.decode, over the pipe. Same contract: sorted list, [] when empty, None when not."""
    if not self.syndromes:
        return None
    return decode(self.syndromes)


def enable():
    """Swap Sketch.decode for the native one. Idempotent."""
    global _python_decode
    if _python_decode is None:
        _python_decode = pinsketch.Sketch.decode
        pinsketch.Sketch.decode = _decode_native
    return True


def disable():
    global _python_decode
    if _python_decode is not None:
        pinsketch.Sketch.decode = _python_decode
        _python_decode = None


def enabled_by_environment():
    """Honour SFPP_NATIVE_SKETCH, and say so. Anything unset or "0" leaves the Python in place."""
    if os.environ.get("SFPP_NATIVE_SKETCH", "").strip() not in ("", "0"):
        enable()
        return True
    return False


# Cases per capacity, weighted by what a case costs on the Python side rather than evenly. A
# capacity-32 sketch held past its capacity takes 21.6 s to fail to decode in Python and about a
# millisecond in the C++, so an even split would spend the entire budget proving the same thing
# about the largest sketches and never reach a useful sample of the small ones.
PLAN = ((2, 300), (3, 200), (4, 100), (8, 20), (16, 6), (32, 2))


def verify(scale=1.0, seed=20260826):
    """Decode the same sketches both ways and diff, including over-capacity ones.

    Over-capacity is deliberate: a sketch holding more than its capacity usually fails to decode but
    misdecodes to a wrong set at about 1/c!, and a wrapper that agreed only on the clean cases would
    pass a test that never exercised the interesting half. Both sides must agree on the same wrong
    answer, because a misdecode the firmware makes is one the simulator has to make too.
    """
    rng = random.Random(seed)
    py = _python_decode or pinsketch.Sketch.decode
    bad = total = 0
    py_time = native_time = 0.0
    for capacity, count in PLAN:
        count = max(1, int(count * scale))
        for i in range(count):
            members = rng.randrange(0, capacity * 2 + 1)  # sometimes past capacity, on purpose
            sketch = pinsketch.Sketch(capacity)
            for _ in range(members):
                sketch.add(rng.randrange(1, 1 << 32))
            syndromes = list(sketch.syndromes)

            mark = time.perf_counter()
            mine = py(sketch)
            py_time += time.perf_counter() - mark

            mark = time.perf_counter()
            theirs = decode(syndromes)
            native_time += time.perf_counter() - mark

            total += 1
            if mine != theirs:
                bad += 1
                if bad <= 5:
                    print(f"  capacity {capacity}, {members} members, case {i}")
                    print(f"    python {mine}")
                    print(f"    native {theirs}")
        print(f"  capacity {capacity:>2}: {count} cases")
    print(f"\n{total - bad}/{total} decodes agree")
    print(
        f"decode time over those cases: python {py_time:.1f}s, native {native_time:.1f}s"
        + (f"  ({py_time / native_time:.0f}x)" if native_time else "")
    )
    return bad == 0


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    scale = 1.0
    if "--scale" in argv:
        i = argv.index("--scale")
        if i + 1 < len(argv):
            scale = float(argv[i + 1])
    try:
        ok = verify(scale)
    finally:
        stop()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
