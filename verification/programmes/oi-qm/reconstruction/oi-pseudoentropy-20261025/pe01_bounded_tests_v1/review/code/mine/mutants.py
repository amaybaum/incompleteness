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
 "CX-d-last-only": ("pe01/cx.py", "all(exact(a) >= DELTA_CX for a in adv)", "exact(adv[-1]) >= DELTA_CX", "cx"),
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
 "WIN-strict": ("pe01/embedded.py", "ok = 4 * np.abs(2 * ss.astype(np.int32) - M) >= M", "ok = 4 * np.abs(2 * ss.astype(np.int32) - M) > M", "win"),
}

def make(name):
    f, old, new, kind = MUTANTS[name]
    d = ROOT + "/mut/" + name
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
from pe01 import shard as S, cx, ar, params as P, composite as Cm, generators as G, observers as O, embedded as E
ctl = S.Controls()
if kind == "cx":
    r = cx.selftest({str(n): n + 1 for n in range(3, 9)})
    print(json.dumps({"CX_pass": r["pass"], "base": r["base_accepted"], "mutants": {k: (v["refused_on"], v["pass"]) for k, v in r["mutants"].items()}}))
elif kind == "fp":
    g = G.named(4)["G_filt"]
    for m in (1, 2, 3, 4):
        V = 1 << m
        R = np.array([np.roll(np.arange(V), 1), np.arange(V)])
        for K in (0, 1, 3, 4, 7, 8, 15, 31):
            try:
                wt = Cm.Witness(g, m, R, [0] * V, [v & 1 for v in range(V)], K)
                ctl.add("FP", wt.L.footprint() == m + Cm.clock_bits(K) + 1 and wt.L.S == len(wt.phi), "m=%d K=%d" % (m, K))
                c = wt.checks(); ctl.add("EX1", c["EX1"], "m=%d K=%d" % (m, K))
                hits, out1, M = wt.simulate(); ctl.add("IM3", out1 == hits[K], "readout m=%d K=%d" % (m, K))
            except Exception as e:
                ctl.add("CRASH", False, "%s m=%d K=%d" % (type(e).__name__, m, K))
    print(json.dumps({k: (v["pass"], v["failures"][:3]) for k, v in ctl.rec.items()}))
elif kind == "ar":
    r = ar.ar_check(open(PLAN).read(), P.theta)
    print(json.dumps({"AR_pass": r["pass"], "reasons": r["reasons"][:4]}))
elif kind == "th":
    ok, rec = P.th_check(open(A1).read())
    print(json.dumps({"TH_pass": ok, "reasons": rec["reasons"]}))
elif kind == "th_block":
    t = open(A1).read().replace('"8": 9}', '"8": 10}')
    ok, rec = P.th_check(t)
    print(json.dumps({"TH_pass": ok, "reasons": rec["reasons"]}))
elif kind == "im3":
    for fam in ("clk",):
        n = 3
        gens = G.family(fam, n)
        for m in (1, 2):
            obs = O.all_observers(m)
            sw = E.Sweep(obs, gens, [8] * len(gens), list(range(len(gens))), [0], 8, "det", {"all": np.ones(obs.n, bool)}, chunk=2048, im3=Cm.FullState).run()
            ctl.add("IM3", sw.im3_ok, "m=%d %s" % (m, sw.im3_fail[:2]))
    S.embedded_bruteforce(ctl, 3, "clk", 1, 6)
    print(json.dumps({k: (v["pass"], [str(x)[:120] for x in v["failures"][:3]]) for k, v in ctl.rec.items()}))
elif kind == "im6":
    out = S.shard_tape("smoke", ctl)
    print(json.dumps({k: (v["pass"], [str(x)[:100] for x in v["failures"][:3]]) for k, v in ctl.rec.items()}))
elif kind == "win":
    # every control that touches the embedded sweep at small n, plus the window counts they produce
    S.embedded_bruteforce(ctl, 3, "clk", 1, 6); S.embedded_bruteforce(ctl, 4, "clk", 2, 7, nobs=60)
    g = G.make("clk", 4, G.p_n(4)); obs = O.all_observers(1)
    sw = E.Sweep(obs, [g], [20], [0], [0], None, "det", {"all": np.ones(obs.n, bool)}, window_cap={0: 20}, im3=Cm.FullState).run()
    ctl.add("IM3", sw.im3_ok)
    print(json.dumps({"controls": {k: v["pass"] for k, v in ctl.rec.items()}, "windows_clk4_m1": {K: r["count"] for K, r in sw.win[("all", 0)].items()}}))
'''

if __name__ == "__main__":
    open(ROOT + "/mine/driver.py", "w").write(DRIVER)
    names = sys.argv[1:] or list(MUTANTS)
    for nm in names:
        d, kind = make(nm)
        r = subprocess.run([sys.executable, "-I", "-B", ROOT + "/mine/driver.py", d, kind, PLAN, A1], capture_output=True, text=True, timeout=600)
        print(nm, "=>", (r.stdout.strip() or r.stderr.strip()[-400:]))
