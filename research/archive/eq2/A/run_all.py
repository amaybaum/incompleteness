"""EQ2-A replay: re-run every exact probe with `python3 -I -B` and require byte-identical stdout.
Usage (from anywhere): python3 -I -B run_all.py <base OIBridge dir> <eqreview dir>
Writes only into ./replay/ next to this script.  Also replays the coordinator's review_pass2.py (prior work, the
n = 7 tree-generation check this thread does not re-implement) against its recorded output."""
import hashlib
import os
import subprocess
import sys

here = os.path.dirname(os.path.abspath(__file__))
base, eqreview = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
cd, k2 = os.path.join(base, "CompositeDimension.lean"), os.path.join(base, "K2Guard.lean")
probes = [("a1_pauli_twin", [cd, k2]), ("a2_universality", []), ("a2b_chart_steps", []), ("a3_bridge", []),
          ("a4_coupling", [cd, k2]), ("a4b_twisted_hull", []),
          ("a4c_twisted_selfduality", []), ("a4d_orbit_extension", []), ("a5_pertype", [cd, k2])]
os.makedirs(os.path.join(here, "replay"), exist_ok=True)


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()[:16]


ok_all = True
for name, args in probes:
    out_path = os.path.join(here, "replay", name + ".out")
    with open(out_path, "wb") as fo:
        r = subprocess.run([sys.executable, "-I", "-B", os.path.join(here, name + ".py")] + args, stdout=fo,
                           stderr=subprocess.DEVNULL, cwd=os.path.join(here, "replay"))
    rec = os.path.join(here, name + ".out")
    same = open(out_path, "rb").read() == open(rec, "rb").read()
    ok_all = ok_all and same and r.returncode == 0
    print(f"{name}: exit {r.returncode}, script {sha(os.path.join(here, name + '.py'))}, output {sha(rec)}, "
          f"replay {'identical' if same else 'DIFFERS'}")
rp = os.path.join(eqreview, "review_pass2.py")
out_path = os.path.join(here, "replay", "review_pass2.out")
with open(out_path, "wb") as fo:
    r = subprocess.run([sys.executable, "-I", "-B", rp], stdout=fo, stderr=subprocess.DEVNULL,
                       cwd=os.path.join(here, "replay"))
same = open(out_path, "rb").read() == open(os.path.join(eqreview, "review_pass2.out"), "rb").read()
ok_all = ok_all and same and r.returncode == 0
print(f"review_pass2 (prior, coordinator): exit {r.returncode}, script {sha(rp)}, replay "
      f"{'identical to the recorded output' if same else 'DIFFERS'}")
print("run_all: " + ("OK" if ok_all else "FAILED"))
sys.exit(0 if ok_all else 1)
