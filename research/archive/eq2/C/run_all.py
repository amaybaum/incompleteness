"""EQ2-C replay: run every script of this thread twice (python3 -I -B), write the canonical outputs <name>.out, the
second run into replay/<name>.out, and require byte-identical outputs and exit code 0. Prior-thread scripts this
thread relies on are replayed read-only through replay_prior.py and compared with their own recorded outputs.
Writes replay.log (sha256 prefixes of every script, helper and output). Exit 0 iff everything matches.
usage (from scratchpad/eq2/C):  python3 -I -B run_all.py
"""
import hashlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.abspath(os.path.join(HERE, "..", ".."))
BASE_OIB = os.path.join(SP, "eq", "base", "verification", "lean-mathlib", "OIBridge")

OWN = [("c1_cite", ["c1_cite.py", BASE_OIB]),
       ("c2a_c7b", ["c2a_c7b.py"]),
       ("c2b_drive_lift", ["c2b_drive_lift.py"]),
       ("c2c_typecov", ["c2c_typecov.py"]),
       ("c2d_relc_split", ["c2d_relc_split.py"]),
       ("c3_bp", ["c3_bp.py"]),
       ("c3_fr", ["c3_fr.py"]),
       ("c3_ops", ["c3_ops.py"])]
PRIOR = [("prior_oistage_checks", os.path.join(SP, "oistage", "oistage_checks.py"), os.path.join(SP, "oistage", "out.txt")),
         ("prior_qa2_towers", os.path.join(SP, "eq", "A", "qa2_towers.py"), os.path.join(SP, "eq", "A", "qa2_towers.out")),
         ("prior_qa3_l2tower", os.path.join(SP, "eq", "A", "qa3_l2tower.py"), os.path.join(SP, "eq", "A", "qa3_l2tower.out")),
         ("prior_opact_checks", os.path.join(SP, "opact", "opact_checks.py"), os.path.join(SP, "opact", "out.txt"))]
HELPERS = ["c_common.py", "replay_prior.py", "run_all.py", os.path.join("vendor_bal", "relt_common.py"),
           os.path.join("vendor_bal", "relt_lsig.py"), os.path.join("vendor_bal", "bal_gates.py")]


def sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:16]


def run(argv, out_path):
    with open(out_path, "wb") as fh:
        p = subprocess.run([sys.executable, "-I", "-B"] + argv, cwd=HERE, stdout=fh, stderr=subprocess.STDOUT)
    return p.returncode


os.makedirs(os.path.join(HERE, "replay"), exist_ok=True)
log = []
ok_all = True
for name, argv in OWN:
    out1 = os.path.join(HERE, name + ".out")
    out2 = os.path.join(HERE, "replay", name + ".out")
    e1 = run(argv, out1)
    e2 = run(argv, out2)
    same = open(out1, "rb").read() == open(out2, "rb").read()
    last = open(out1, encoding="utf-8").read().strip().split("\n")
    verdict = next((ln for ln in reversed(last) if ln.startswith(name + ":")), "?")
    ok = e1 == 0 and e2 == 0 and same
    ok_all &= ok
    log.append(f"{name:22s} script {sha(os.path.join(HERE, argv[0]))} output {sha(out1)} exit {e1}/{e2} "
               f"replay={'identical' if same else 'DIFFERS'}  {verdict}")
for name, script, recorded in PRIOR:
    out1 = os.path.join(HERE, "replay_prior_out", name + ".out")
    os.makedirs(os.path.dirname(out1), exist_ok=True)
    e1 = run(["replay_prior.py", script], out1)
    same = open(out1, "rb").read() == open(recorded, "rb").read()
    ok = e1 == 0 and same
    ok_all &= ok
    log.append(f"{name:22s} script {sha(script)} output {sha(out1)} exit {e1} "
               f"vs-recorded={'identical' if same else 'DIFFERS'}  ({os.path.relpath(recorded, SP)})")
for h in HELPERS:
    log.append(f"helper {h:28s} {sha(os.path.join(HERE, h))}")
log.append("run_all: " + ("OK" if ok_all else "FAILED"))
with open(os.path.join(HERE, "replay.log"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(log) + "\n")
print("\n".join(log))
sys.exit(0 if ok_all else 1)
