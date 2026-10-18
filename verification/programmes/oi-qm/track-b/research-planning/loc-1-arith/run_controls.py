"""Run every LOC-1 arithmetic control on synthetic inputs: cyclo16, the S16 layer (K-arith-16) and the replay
arithmetic, plus the cross-check of the two arithmetics through written vectors.

    python3 -I -B run_controls.py          fast suite, for local runs (seconds, a few tens of KB of temp)
    python3 -I -B run_controls.py --full   the larger randomized and exhaustive suite, run in CI

No target object is evaluated.  Exit status 0 iff every control passes.
"""
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def step(args):
    r = subprocess.run([sys.executable, "-I", "-B"] + args, cwd=HERE, capture_output=True, text=True)
    sys.stdout.write(r.stdout)
    return r.returncode == 0


def main(argv):
    full = ["--full"] if "--full" in argv else []
    ok = True
    ok &= step(["cyclo16.py", "--self-test"] + full)
    ok &= step(["replay_cyclo16.py", "--self-test"] + full)
    with tempfile.TemporaryDirectory() as d:
        v = os.path.join(d, "vectors.json")
        ok &= step(["cyclo16.py", "--emit-vectors", v])
        ok &= step(["replay_cyclo16.py", "--check-vectors", v])
    ok &= step(["s16_layer.py", "--self-test"] + full)
    print("LOC-1 arithmetic controls (%s): %s" % ("full" if full else "fast", "ALL PASS" if ok else "FAILURE"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
