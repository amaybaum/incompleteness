
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
