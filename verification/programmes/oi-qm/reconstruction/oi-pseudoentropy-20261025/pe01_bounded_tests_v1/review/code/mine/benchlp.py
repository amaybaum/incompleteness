import sys, time
sys.path.insert(0, sys.argv[1])
import numpy as np
from pe01 import observers as O, embedded as E, shard as S, lp, generators as G
n = 6; K = 31
gens = G.family("filt", n)
obs = O.all_observers(2)
t = time.time()
sw = E.Sweep(obs, gens, [K] * len(gens), list(range(len(gens))), [], None, "det", {"all": np.ones(obs.n, bool)}, lp_cap=K, chunk=2048)
sw.k0cap = None
sw.run()
t1 = time.time()
Cf, Z, den = S.lp_tables(sw, obs, K, gens[0].M)
pats = lp.sign_patterns(len(gens))
for s in pats[:3]:
    t2 = time.time()
    r = lp.randomized_k0(Cf, Z, den, gens[0].M, s)
    print("pattern", s, "value", r["value"], "iterations", r["iterations"], "cuts", r["cuts"], "%.1fs" % (time.time() - t2))
print("sweep %.1fs; patterns per K: %d; K range: %d" % (t1 - t, len(pats), K + 1))
