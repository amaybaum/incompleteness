import sys, time
sys.path.insert(0, sys.argv[1])
from c21_engine import *
I = [[1 if i==j else 0 for j in range(16)] for i in range(16)]
NI = [r[:] for r in I]; NI[14][15] = 1
for order in ("greedy","nat"):
  for rules in ("RWVP","RWV"):
    E = Engine([NI],4,4,order=order, rules=rules)
    t=time.perf_counter(); st,f,s = E.run("exist", budget=2*10**6); t=time.perf_counter()-t
    print("near-identity", order, rules, st, s, "%.2fs"%t)
rng = SM64(1)
def rmat(k, lo, hi):
    return [[lo + rng.below(hi-lo+1) for _ in range(k)] for _ in range(k)]
for trial in range(3):
    A, B = rmat(4,-2,2), rmat(4,-2,2)
    sig = rng.shuffle(range(16))
    M = relabel(kron(A,B), sig)
    for rules in ("RWVP","RWV"):
        E = Engine([M], 4, 4, rules=rules)
        t=time.perf_counter(); st, f, s = E.run("all", budget=2*10**6); t=time.perf_counter()-t
        ok = canonical(sig,4,4,E.order) in [canonical(x,4,4,E.order) for x in f]
        print("planted", trial, rules, st, len(f), s, ok, "%.3fs"%t)
T = [[0]*16 for _ in range(16)]
lab = SM64(5).shuffle(range(16)); pi = list(range(16)); pi[lab[0]],pi[lab[1]]=lab[1],lab[0]
for j in range(16): T[pi[j]][j]=1
for rules in ("RWVP","RWV"):
    E = Engine([T],4,4,rules=rules); t=time.perf_counter(); st,f,s=E.run("exist", budget=5*10**6); t=time.perf_counter()-t
    print("transposition seeded", rules, st, len(f), s, "%.3fs"%t)
