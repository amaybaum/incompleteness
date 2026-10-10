"""FLOATING POINT, EXPLORATION ONLY, CERTIFIES NOTHING -- determinism record for the float explorations x1, x2.
Re-runs each with `python3 -I -B` into replay/ and compares stdout byte for byte with the recorded output.
Usage (from scratchpad/eq3/P): python3 -I -B run_explorations.py
"""
import hashlib
import os
import subprocess
import sys

here = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(here, "replay"), exist_ok=True)
ok = True
for script in ("x1_slocc_orbit_float.py", "x2_sector_float.py"):
    out = subprocess.run([sys.executable, "-I", "-B", os.path.join(here, script)], cwd=here, capture_output=True)
    with open(os.path.join(here, "replay", script.replace(".py", ".out")), "wb") as fh:
        fh.write(out.stdout)
    canon = open(os.path.join(here, script.replace(".py", ".out")), "rb").read()
    same = out.stdout == canon
    ok = ok and same and out.returncode == 0
    print(f"{script}: exit {out.returncode}, identical {same}, sha {hashlib.sha256(out.stdout).hexdigest()[:16]}")
print("run_explorations: " + ("OK" if ok else "MISMATCH"))
sys.exit(0 if ok else 1)
