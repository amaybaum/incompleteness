
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
