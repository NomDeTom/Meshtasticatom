"""Route Sketch.decode through the vendored C++ instead of the Python transcription.

Decoding is where a sketch costs anything. `Sketch.add` is a handful of XORs against cached odd
powers; `decode` is Berlekamp-Massey and root-finding over GF(2^32), and in Python it was measured
at 62.9% of a 12-hour 150-node run - 75.5 s across 199 calls, about 0.38 s each. The same work is
microseconds in the C++ this module compiles.

199 calls is what makes this worth doing over a pipe. A round trip is tens of microseconds, so the
whole run's IPC is a rounding error against 75.5 s; wrapping `mul` instead - 10.1M calls - would
have spent more on the pipe than it saved.

On by default, falling back to the transcription where no compiler or source is reachable. That is
only defensible because the two are the same decoder rather than believed to be: `test_native_sketch`
diffs them on every suite run, and `check_oracle` holds the transcription itself to the firmware. So
a fallback costs speed and nothing else.

The Python stays the reference for both of those checks, and is what a tree without a compiler runs.
Neither path is silent about which it took - the run prints it and `decoder` goes into the report,
because a tree that quietly lost its compiler would otherwise show it only as runs that got slower.

    python3 -m sfpp.campaign ...                   # native where it can be built
    SFPP_NATIVE_SKETCH=0 python3 -m sfpp.campaign  # force the transcription
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
        proc, _proc = _proc, None
        try:
            proc.stdin.close()
            proc.wait(timeout=5)
        except Exception:
            proc.kill()
        finally:
            # Closed explicitly rather than left to the collector: the suite creates and drops this
            # process, and an unclosed pipe there is a ResourceWarning in somebody else's test.
            for pipe in (proc.stdin, proc.stdout):
                try:
                    pipe.close()
                except Exception:
                    pass


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


def activate():
    """Use the C++ decoder if this tree can build one. Returns the sentence a run should print.

    On by default, because the decoders are the same decoder: 628 differential cases and whole-run
    fingerprints say so, and `test_native_sketch` keeps saying so. Falling back therefore costs
    speed and nothing else, which is what makes falling back acceptable here at all - it was not
    acceptable while the two were merely believed to agree.

    Never silent, though. A tree that quietly lost its compiler would show it only as runs that got
    slower, which is the shape of thing this repository has been caught by before, so the reason is
    printed and `decoder` goes into the report.

    SFPP_NATIVE_SKETCH=0 forces the transcription - the only way to run it once a compiler exists,
    and what the paired job uses for its Python arm.
    """
    asked = os.environ.get("SFPP_NATIVE_SKETCH", "").strip()
    if asked == "0":
        return "python (SFPP_NATIVE_SKETCH=0)"
    try:
        start()
    # SystemExit as well as Exception, and deliberately: check_oracle.build_oracle reports a failed
    # compile with sys.exit, which does not inherit from Exception. Catching only Exception meant a
    # tree without a compiler exited here instead of falling back - the one outcome this whole
    # function exists to prevent, and invisible until a machine without g++ ran it.
    except (Exception, SystemExit) as exc:
        first = str(exc).strip().splitlines()[0] if str(exc).strip() else exc.__class__.__name__
        return f"python (no native decoder: {first})"
    enable()
    return "native"


# Cases per capacity, weighted by what a case costs on the Python side rather than evenly. A
# capacity-32 sketch held past its capacity takes 21.6 s to fail to decode in Python and about a
# millisecond in the C++, so an even split would spend the entire budget proving the same thing
# about the largest sketches and never reach a useful sample of the small ones.
PLAN = ((2, 300), (3, 200), (4, 100), (8, 20), (16, 6), (32, 2))


def verify(scale=1.0, seed=20260826, plan=PLAN, report=print):
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
    disagreed = []
    for capacity, count in plan:
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
                disagreed.append((capacity, members, mine, theirs))
                if bad <= 5:
                    report(f"  capacity {capacity}, {members} members, case {i}")
                    report(f"    python {mine}")
                    report(f"    native {theirs}")
        report(f"  capacity {capacity:>2}: {count} cases")
    report(f"\n{total - bad}/{total} decodes agree")
    report(
        f"decode time over those cases: python {py_time:.1f}s, native {native_time:.1f}s"
        + (f"  ({py_time / native_time:.0f}x)" if native_time else "")
    )
    return disagreed


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    scale = 1.0
    if "--scale" in argv:
        i = argv.index("--scale")
        if i + 1 < len(argv):
            scale = float(argv[i + 1])
    try:
        ok = not verify(scale)
    finally:
        stop()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
