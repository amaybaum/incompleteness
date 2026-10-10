"""EQ4-P replay harness for the exact-arithmetic explorations (research only).  Re-runs x3, x4, x6, x8, x10-x15 with
`python3 -I -B` and their recorded arguments into replay/ and compares stdout with the recorded output byte for byte.
(x5 is excluded: it was stopped by hand in a non-terminating regress, so it has no complete recorded output.  The
floating-point explorations x1, x2, x7, x9, x16 are not replayed; their hashes are recorded in NOTES.)

Usage:  python3 -I -B run_x.py

DECISION RULE (fixed before the first run): print `VERDICT RUN-X-OK` iff every listed exploration exits 0, writes
nothing to stderr, and its stdout equals the recorded output byte for byte; otherwise `VERDICT NOT RENDERED`.  The
verdict concerns replay determinism only; the explorations remain leads, not evidence.
"""
import hashlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = [("x3_sector_search", ["kappa"], "x3_sector_search.kappa.out"),
        ("x4_sector_dfs", ["300"], "x4_sector_dfs.out"),
        ("x6_sector_family", [], "x6_sector_family.out"),
        ("x8_sector_limit", ["60"], "x8_sector_limit.out"),
        ("x10_e2_contraction", [], "x10_e2_contraction.out"),
        ("x11_KA_networks", [], "x11_KA_networks.out"),
        ("x12_c1_sector", [], "x12_c1_sector.out"),
        ("x13_c1_greedy", ["8"], "x13_c1_greedy.out"),
        ("x14_c1_dfs", ["120"], "x14_c1_dfs.out"),
        ("x15_Ktw_tests", [], "x15_Ktw_tests.out")]
os.makedirs(os.path.join(HERE, "replay"), exist_ok=True)


def h16(data):
    return hashlib.sha256(data).hexdigest()[:16]


all_ok = True
for name, args, rec_name in RUNS:
    script = os.path.join(HERE, name + ".py")
    rec = open(os.path.join(HERE, rec_name), "rb").read()
    proc = subprocess.run([sys.executable, "-I", "-B", script] + args, cwd=HERE, capture_output=True)
    open(os.path.join(HERE, "replay", rec_name), "wb").write(proc.stdout)
    open(os.path.join(HERE, "replay", name + ".err"), "wb").write(proc.stderr)
    same = proc.stdout == rec
    ok = proc.returncode == 0 and proc.stderr == b"" and same
    all_ok &= ok
    print("%-20s script %s  recorded %s  replay %s  exit %d  stderr %s  identical %s"
          % (name, h16(open(script, "rb").read()), h16(rec), h16(proc.stdout), proc.returncode,
             "empty" if proc.stderr == b"" else "NONEMPTY", same), flush=True)
print("VERDICT RUN-X-OK" if all_ok else "VERDICT NOT RENDERED")
