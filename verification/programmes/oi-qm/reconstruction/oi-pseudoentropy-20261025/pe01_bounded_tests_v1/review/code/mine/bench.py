import sys, time
sys.path.insert(0, sys.argv[1])
import numpy as np
from pe01 import generators as G, observers as O, embedded as E, shard as S
n = int(sys.argv[2]); Kb = int(sys.argv[3]); nobs = int(sys.argv[4])
famlist, prim, sib, extra = S.named_for(n, "clk")
allg = famlist + extra
obs = O.all_observers(2)
obs = obs.subset(np.arange(obs.n) < nobs, "bench")
subs = {"all": np.ones(obs.n, bool), "passive": obs.passive.copy()}
kcap1 = [Kb if gi == prim else 0 for gi in range(len(allg))]
t = time.time()
sw = E.Sweep(obs, allg, kcap1, list(range(len(famlist))), [prim], Kb, "det", subs, window_cap={prim: Kb}, chunk=2048).run()
dt = time.time() - t
print("n=%d family=%d obs=%d K<=%d: %.1fs  -> per (obs*K) %.3g s" % (n, len(famlist), nobs, Kb, dt, dt / (nobs * (Kb + 1))))
t = time.time()
kcap1 = [4 * Kb if gi == prim else 0 for gi in range(len(allg))]
sw = E.Sweep(obs, allg, kcap1, list(range(len(famlist))), [prim], None, "det", subs, window_cap={prim: 4*Kb}, chunk=2048).run()
dt2 = time.time() - t
print("  K1+windows only, prim to K<=%d (family runs to 0): %.1fs" % (4 * Kb, dt2))
