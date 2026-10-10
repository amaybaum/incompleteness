"""EQ2-A replay of the floating-point explorations (they certify nothing; replayed only for the determinism record).
Usage (from anywhere): python3 -I -B run_explorations.py
Runs every x*.py exploration (and the kept run-1 variant of x2) in parallel with `python3 -I -B`, writes stdout to
./replay/<name>.out, and compares it byte-for-byte with the recorded output.  The recorded x3 output was produced as
`... > out 2>&1; echo "exit=$?" >> out`, so its final `exit=0` line is removed before the comparison."""
import hashlib
import os
import subprocess
import sys

here = os.path.dirname(os.path.abspath(__file__))
jobs = [("x1_twisted_selfdual_float", "x1_twisted_selfdual_float.out"),
        ("x2_twisted_cutting_plane_float", "x2_twisted_cutting_plane_float.out"),
        ("x2_twisted_cutting_plane_float.run1", "x2_twisted_cutting_plane_float.run1.out"),
        ("x3_twisted_selfdual_twirled_float", "x3_twisted_selfdual_twirled_float.out")]
os.makedirs(os.path.join(here, "replay"), exist_ok=True)


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()[:16]


procs = []
for name, rec in jobs:
    fo = open(os.path.join(here, "replay", name + ".out"), "wb")
    p = subprocess.Popen([sys.executable, "-I", "-B", os.path.join(here, name + ".py")], stdout=fo,
                         stderr=subprocess.DEVNULL, cwd=os.path.join(here, "replay"))
    procs.append((name, rec, p, fo))
ok_all = True
for name, rec, p, fo in procs:
    rc = p.wait()
    fo.close()
    got = open(os.path.join(here, "replay", name + ".out"), "rb").read()
    want = open(os.path.join(here, rec), "rb").read()
    if want.endswith(b"exit=0\n"):
        want = want[: -len(b"exit=0\n")]
    same = got == want
    ok_all = ok_all and same and rc == 0
    print(f"{name}: exit {rc}, script {sha(os.path.join(here, name + '.py'))}, recorded output {sha(os.path.join(here, rec))}, "
          f"replay {'identical' if same else 'DIFFERS'}")
print("run_explorations: " + ("OK" if ok_all else "FAILED"))
sys.exit(0 if ok_all else 1)
