"""Audit replay of EQ4-P (independent harness; research only).

Copies of the thread's scripts live in src/; each runs with `python3 -I -B` from src/ and its stdout is compared byte for
byte with the thread's recorded output in scratchpad/eq4/P/.  DECISION RULE (fixed before the first run): print
`VERDICT AUDIT-REPLAY-OK` iff every run exits 0 with empty stderr and stdout identical to the recorded file, and the
copied script is byte-identical to the thread's script; otherwise `VERDICT NOT RENDERED`.
"""
import hashlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
THREAD, BASE = sys.argv[1], sys.argv[2]
RUNS = [(p, [BASE], p + ".out") for p in
        ["p1_e1_triangle", "p2_teleport", "p3_crossing_calculus", "p4_e3_directions", "p5_generation",
         "p6_five_token_model", "p7_wall_reduction", "p8_coloring", "p9_purification", "p10_c1_maximality",
         "p11_sector_reduction", "p12_sector_selfdual", "p13_c1_sector"]]
RUNS += [("x3_sector_search", ["kappa"], "x3_sector_search.kappa.out"), ("x4_sector_dfs", ["300"], "x4_sector_dfs.out"),
         ("x6_sector_family", [], "x6_sector_family.out"), ("x8_sector_limit", ["60"], "x8_sector_limit.out"),
         ("x10_e2_contraction", [], "x10_e2_contraction.out"), ("x11_KA_networks", [], "x11_KA_networks.out"),
         ("x12_c1_sector", [], "x12_c1_sector.out"), ("x13_c1_greedy", ["8"], "x13_c1_greedy.out"),
         ("x14_c1_dfs", ["120"], "x14_c1_dfs.out"), ("x15_Ktw_tests", [], "x15_Ktw_tests.out")]


def h16(b):
    return hashlib.sha256(b).hexdigest()[:16]


ok_all = True
lib_same = open(os.path.join(HERE, "src", "eq4_lib.py"), "rb").read() == open(os.path.join(THREAD, "eq4_lib.py"), "rb").read()
ok_all &= lib_same
print("eq4_lib.py copy identical %s  sha %s" % (lib_same, h16(open(os.path.join(HERE, "src", "eq4_lib.py"), "rb").read())))
for name, args, rec in RUNS:
    src = open(os.path.join(HERE, "src", name + ".py"), "rb").read()
    same_src = src == open(os.path.join(THREAD, name + ".py"), "rb").read()
    recorded = open(os.path.join(THREAD, rec), "rb").read()
    proc = subprocess.run([sys.executable, "-I", "-B", os.path.join(HERE, "src", name + ".py")] + args,
                          cwd=os.path.join(HERE, "src"), capture_output=True)
    open(os.path.join(HERE, "out", rec), "wb").write(proc.stdout)
    open(os.path.join(HERE, "out", name + ".err"), "wb").write(proc.stderr)
    same = proc.stdout == recorded
    ok = same_src and proc.returncode == 0 and proc.stderr == b"" and same
    ok_all &= ok
    print("%-22s src %s (copy==thread %s)  recorded %s  replay %s  exit %d  stderr %s  identical %s"
          % (name, h16(src), same_src, h16(recorded), h16(proc.stdout), proc.returncode,
             "empty" if not proc.stderr else "NONEMPTY", same), flush=True)
print("VERDICT AUDIT-REPLAY-OK" if ok_all else "VERDICT NOT RENDERED")
