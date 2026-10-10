"""Replay every EQ-E script and compare its output byte for byte with the recorded .out file.
Usage: PYTHONDONTWRITEBYTECODE=1 python3 run_all.py   (from scratchpad/eq/E).  Exit 0 iff every script exits 0 and
every output replays exactly."""
import subprocess, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = ["s5_pauli_adapter", "s4_not_pairs", "s6_gate_class", "s1_stage_act", "s3_scope_qutrit",
           "s7_k2_composite", "s8_one_model", "qe2_graph"]
env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
bad = 0
for s in SCRIPTS:
    args = [sys.executable] + (["-I"] if s == "qe2_graph" else []) + [os.path.join(HERE, s + ".py")]
    p = subprocess.run(args, cwd=HERE, env=env, capture_output=True, text=True, timeout=3600)
    out = p.stdout + p.stderr
    rec = open(os.path.join(HERE, s + ".out")).read()
    same = (out == rec)
    print("%-18s exit=%d replay=%s" % (s, p.returncode, "EXACT" if same else "DIFFERS"))
    bad += (p.returncode != 0) + (not same)
print("run_all: %s" % ("OK" if bad == 0 else "FAILED (%d)" % bad))
sys.exit(0 if bad == 0 else 1)
