"""Mutant harness: copy the package, apply one textual patch, run the targeted check, report."""
import os, shutil, subprocess, sys, json
ROOT = "<scratch>/revpe01code"
SRC = ROOT + "/repo/verification/programmes/oi-qm/reconstruction/oi-pseudoentropy-20261025/pe01_bounded_tests_v1"
PLAN = SRC + "/PLAN.md"
A1 = SRC + "/amendments/A1-owner-decisions.md"

MUTANTS = {
 "BASE-cx": (None, "", "", "cx"),
 "BASE-fp": (None, "", "", "fp"),
 "BASE-ar": (None, "", "", "ar"),
 "BASE-th": (None, "", "", "th"),
 "BASE-im3": (None, "", "", "im3"),
 "BASE-im6": (None, "", "", "im6"),
 "BASE-win": (None, "", "", "win"),
 "CX-f-loosened": ("pe01/cx.py", 'w["footprint"] <= th)', 'w["footprint"] <= th + 1)', "cx"),
 "CX-d-last-only": ("pe01/cx.py", "for a in vals)", "for a in vals[-1:])", "cx"),
 "CX-c-strict-off": ("pe01/cx.py", 'K <= w["K_cx"]', 'K <= w["K_cx"] + 1', "cx"),
 "FP-clock-undercharged": ("pe01/composite.py", "self.c = clock_bits(K)", "self.c = max(clock_bits(K) - 1, 0)", "fp"),
 "FP-out-register-dropped": ("pe01/composite.py", 'self.registers = [("sys", 1), ("mem", m), ("clk", c), ("out", 1)]', 'self.registers = [("sys", 1), ("mem", m), ("clk", c), ("out", 0)]', "fp"),
 "AR-window-floor": ("pe01/ar.py", "K >= Z + W + 1", "K >= Z + W", "ar"),
 "AR-Z-autonomous-only": ("pe01/ar.py", "for cs in range(1 << k1):", "for cs in range(1):", "ar"),
 "AR-Kcx-upper-median": ("pe01/ar.py", "return lo // 2, lo == hi, lo, hi", "return (lo + 1) // 2, lo == hi, lo, hi", "ar"),
 "TH-code-theta-n": ("pe01/params.py", "def theta(n):\n    return n + 1", "def theta(n):\n    return n", "th"),
 "TH-code-m3cap": ("pe01/params.py", "return {7: 15, 8: 31}.get(n, kmax)", "return {7: 15, 8: 63}.get(n, kmax)", "th"),
 "TH-block-edited": (None, '"8": 9}', '"8": 10}', "th_block"),
 "IM3-act-before-rho": ("pe01/embedded.py", "cc = st[\"x\"] ^ self.A[np.arange(self.c)[:, None], v]", "cc = st[\"x\"] ^ self.A[np.arange(self.c)[:, None], st[\"v\"]]", "im3"),
 "IM6-Q-pushforward": ("pe01/embedded.py", "self.Q = self.Q[ar, self.inv[:, 0, :]] + self.Q[ar, self.inv[:, 1, :]]", "self.Q = self.Q[ar, self.inv[:, 0, :]] + self.Q[ar, self.inv[:, 0, :]]", "im6"),
 "WIN-strict": ("pe01/embedded.py", '("abs", 4 * np.abs(d2) >= M)', '("abs", 4 * np.abs(d2) > M)', "win"),
 "WIN-strict-signed": ("pe01/embedded.py", '("signed", 4 * d2 >= M)', '("signed", 4 * d2 > M)', "win"),
 "SIGN-as-abs": ("pe01/embedded.py", '("signed", 4 * d2 >= M)', '("signed", 4 * np.abs(d2) >= M)', "win"),
 "B3W-gray-flip": ("pe01/bclasses.py", "y += 2 * s[j] * D[j]", "y += s[j] * D[j]", "b3wself"),
 "B3W-outside-dropped": ("pe01/bclasses.py", "+ outside * max(0, -M * ssum)", "+ 0", "b3wself"),
 "BASE-b3wself": (None, "", "", "b3wself"),
 "BASE-b3w": (None, "", "", "b3w"),
}

def make(name):
    f, old, new, kind = MUTANTS[name]
    d = ROOT + "/mut2r/" + name
    if os.path.exists(d): shutil.rmtree(d)
    shutil.copytree(SRC, d, ignore=shutil.ignore_patterns("review", "*.md"))
    if f:
        p = d + "/" + f
        t = open(p).read()
        assert t.count(old) == 1, (name, t.count(old))
        open(p, "w").write(t.replace(old, new))
    return d, kind

DRIVER = r'''
import sys, json
sys.path.insert(0, sys.argv[1]); kind = sys.argv[2]; PLAN = sys.argv[3]; A1 = sys.argv[4]
import numpy as np
from pe01 import shard as S, cx, ar, params as P, composite as Cm, generators as G, observers as O, embedded as E, laws as LW, bclasses as B
ctl = S.Controls()
def rep():
    return {k: (v["pass"], [str(x)[:140] for x in v["failures"][:2]]) for k, v in ctl.rec.items()}
if kind == "cx":
    r = cx.selftest({str(n): n + 1 for n in range(3, 9)})
    print(json.dumps({"CX_pass": r["pass"], "failing": [k for k, v in r["mutants"].items() if not v["pass"]], "base": r["base_accepted"]}))
elif kind == "fp":
    g = G.named(4)["G_filt"]
    for m in (1, 2, 3, 4):
        V = 1 << m
        R = np.array([np.roll(np.arange(V), 1), np.arange(V)])
        for K in (0, 1, 3, 4, 7, 8, 15, 31):
            wt = Cm.Witness(g, m, R, [0] * V, [v & 1 for v in range(V)], K)
            ctl.add("FP", wt.L.footprint() == m + Cm.clock_bits_independent(K) + 1 and wt.L.S == len(wt.phi), "m=%d K=%d" % (m, K))
            c = wt.checks(); ctl.add("EX1", c["EX1"], "m=%d K=%d" % (m, K))
            hits, out1, _ = wt.simulate(); ctl.add("IM3", out1 == hits[K], "readout m=%d K=%d" % (m, K))
    print(json.dumps(rep()))
elif kind == "ar":
    r = ar.ar_check(open(PLAN).read())
    print(json.dumps({"AR_pass": r["pass"], "reasons": r["reasons"][:3]}))
elif kind == "th":
    ok, rec = P.th_check(open(A1).read()); print(json.dumps({"TH_pass": ok, "reasons": rec["reasons"][:3]}))
elif kind == "th_block":
    ok, rec = P.th_check(open(A1).read().replace('"8": 9}', '"8": 10}')); print(json.dumps({"TH_pass": ok, "reasons": rec["reasons"][:3]}))
elif kind == "im3":
    gens = G.family("clk", 3)
    for m in (1, 2):
        obs = O.all_observers(m)
        sw = E.Sweep(obs, gens, [8] * len(gens), list(range(len(gens))), [0], 8, "det", {"all": np.ones(obs.n, bool)}, chunk=2048, im3=Cm.FullState).run()
        ctl.add("IM3", sw.im3_ok, "FullState m=%d %s" % (m, sw.im3_fail[:2]))
    S.embedded_bruteforce(ctl, 3, "clk", 1, 6)
    print(json.dumps(rep()))
elif kind == "im6":
    S.shard_tape("smoke", ctl); print(json.dumps(rep()))
elif kind == "win":
    S.embedded_bruteforce(ctl, 3, "clk", 1, 8); S.embedded_bruteforce(ctl, 4, "clk", 1, 14)
    S.pred_bruteforce(ctl, 3, "clk", O.linear_obsset(3), 10, O.linear_prediction_masks(3), "plin m3")
    print(json.dumps(rep()))
elif kind == "b3wself":
    import time; t0 = time.time(); S.b3w_selftest(ctl); print(json.dumps(dict(rep(), seconds=round(time.time() - t0, 1))))
elif kind == "b3w":
    for n, fam in ((3, "clk"), (4, "filt"), (5, "lin")):
        laws = [LW.Law(g, 20) for g in G.family(fam, n)]
        bw = B.b3_window_k0(laws)
        for w_, r in bw["per_w"].items():
            if "avg_brute" in r:
                ctl.add("K0", r["avg"] == r["avg_brute"], "n=%d %s w=%d" % (n, fam, w_))
        ctl.add("K0", bw["stationary"], "stationary")
    print(json.dumps(rep()))
'''

if __name__ == "__main__":
    open(ROOT + "/mine/driver2.py", "w").write(DRIVER)
    names = sys.argv[1:] or list(MUTANTS)
    for nm in names:
        d, kind = make(nm)
        r = subprocess.run([sys.executable, "-I", "-B", ROOT + "/mine/driver2.py", d, kind, PLAN, A1], capture_output=True, text=True, timeout=600)
        print(nm, "=>", (r.stdout.strip() or r.stderr.strip()[-400:]))
