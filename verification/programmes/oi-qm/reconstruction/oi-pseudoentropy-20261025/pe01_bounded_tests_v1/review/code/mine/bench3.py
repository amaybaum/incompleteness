import sys, time
sys.path.insert(0, sys.argv[1])
import numpy as np
from pe01 import observers as O, embedded as E, shard as S
n = int(sys.argv[2]); Kb = int(sys.argv[3]); nobs = int(sys.argv[4]); fam = sys.argv[5]
famlist, prim, sib, extra = S.named_for(n, fam)
allg = famlist + extra
named = [prim] + ([sib] if sib is not None else []) + list(range(len(famlist), len(allg)))
obs = O.passive_m3()
obs = obs.subset(np.arange(obs.n) < nobs, "bench")
t = time.time()
sw = E.Sweep(obs, allg, [Kb if gi in named else 0 for gi in range(len(allg))], list(range(len(famlist))), [prim], Kb, "pred",
             {"passive": np.ones(obs.n, bool)}, window_cap={prim: Kb}, chunk=4096).run()
dt = time.time() - t
print("m3 n=%d %s family=%d obs=%d K<=%d: %.1fs -> full 306432 obs: %.0f s" % (n, fam, len(famlist), nobs, Kb, dt, dt * 306432 / nobs))
