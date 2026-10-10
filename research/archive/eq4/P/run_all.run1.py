"""EQ4-P replay harness (research only).  Re-runs every exact probe p1..p10 with `python3 -I -B` into replay/ and
compares the new stdout with the recorded .out byte for byte.

Usage:  python3 -I -B run_all.py <base>/verification/lean-mathlib/OIBridge

DECISION RULE (fixed before the first run): print `VERDICT RUN-ALL-OK` iff every probe exits 0, writes nothing to
stderr, and its stdout equals the recorded `<probe>.out` byte for byte; otherwise `VERDICT NOT RENDERED`.  Each replay's
stdout and stderr are kept in replay/<probe>.out and replay/<probe>.err, with sha256 (first 16 hex) printed for the
script, the recorded output and the replayed output.  Every `python3 -I` run gets a fresh hash seed, so identical
replays also test determinism.
"""
import hashlib
import os
import subprocess
import sys

BASE = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
PROBES = ["p1_e1_triangle", "p2_teleport", "p3_crossing_calculus", "p4_e3_directions", "p5_generation",
          "p6_five_token_model", "p7_wall_reduction", "p8_coloring", "p9_purification", "p10_c1_maximality"]
os.makedirs(os.path.join(HERE, "replay"), exist_ok=True)


def h16(data):
    return hashlib.sha256(data).hexdigest()[:16]


all_ok = True
for name in PROBES:
    script = os.path.join(HERE, name + ".py")
    rec = open(os.path.join(HERE, name + ".out"), "rb").read()
    proc = subprocess.run([sys.executable, "-I", "-B", script, BASE], cwd=HERE, capture_output=True)
    open(os.path.join(HERE, "replay", name + ".out"), "wb").write(proc.stdout)
    open(os.path.join(HERE, "replay", name + ".err"), "wb").write(proc.stderr)
    same = proc.stdout == rec
    ok = proc.returncode == 0 and proc.stderr == b"" and same
    all_ok &= ok
    print("%-22s script %s  recorded %s  replay %s  exit %d  stderr %s  identical %s"
          % (name, h16(open(script, "rb").read()), h16(rec), h16(proc.stdout), proc.returncode,
             "empty" if proc.stderr == b"" else "NONEMPTY", same), flush=True)
print("library eq4_lib.py %s" % h16(open(os.path.join(HERE, "eq4_lib.py"), "rb").read()))
print("VERDICT RUN-ALL-OK" if all_ok else "VERDICT NOT RENDERED")
