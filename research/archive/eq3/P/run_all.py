"""EQ3-P replay harness (exact probes).  Re-runs every exact probe with `python3 -I -B` into replay/ and compares
stdout byte for byte with the canonical outputs (the last run of each probe).  Prints one line per probe and a final
`run_all: OK` only if every probe exits 0 and every output is identical.
Usage (from scratchpad/eq3/P): python3 -I -B run_all.py <base>/verification/lean-mathlib/OIBridge
"""
import hashlib
import os
import subprocess
import sys

here = os.path.dirname(os.path.abspath(__file__))
oib = sys.argv[1]
CD, K2 = os.path.join(oib, "CompositeDimension.lean"), os.path.join(oib, "K2Guard.lean")
probes = [("p1_four_copy_links.py", [CD, K2]), ("p2_audit_twists_foils.py", [CD, K2]), ("p3_general_links.py", [CD]),
          ("p4_cone_ladder.py", []), ("p5_six_copy.py", [CD]), ("p6_cheap_foils.py", [CD])]
os.makedirs(os.path.join(here, "replay"), exist_ok=True)
ok = True
for script, args in probes:
    out = subprocess.run([sys.executable, "-I", "-B", os.path.join(here, script)] + args, cwd=here,
                         capture_output=True)
    with open(os.path.join(here, "replay", script.replace(".py", ".out")), "wb") as fh:
        fh.write(out.stdout)
    canon = open(os.path.join(here, script.replace(".py", ".out")), "rb").read()
    same = out.stdout == canon
    ok = ok and same and out.returncode == 0 and out.stderr == b""
    print(f"{script}: exit {out.returncode}, stderr {len(out.stderr)} bytes, identical {same}, "
          f"sha {hashlib.sha256(out.stdout).hexdigest()[:16]}")
print("run_all: " + ("OK" if ok else "MISMATCH"))
sys.exit(0 if ok else 1)
