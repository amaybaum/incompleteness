import sys, time
sys.path.insert(0, sys.argv[1])
from c21_engine import *
rng = SM64(1)
def rmat(k, lo, hi):
    return [[lo + rng.below(hi-lo+1) for _ in range(k)] for _ in range(k)]
N=16
for trial in range(3):
    A, B = rmat(4,-3,3), rmat(4,-3,3)
    sig = rng.shuffle(range(16))
    M = relabel(kron(A,B), sig)
    for rules in ("RWV","RW","R","W",""):
        E = Engine([M], 4, 4, rules=rules)
        t=time.perf_counter(); st, f, s = E.run("exist", budget=2*10**6); t=time.perf_counter()-t
        ok = canonical(sig,4,4,E.order) in [canonical(x,4,4,E.order) for x in f]
        print("planted", trial, rules, st, len(f), s, "sigma* class" , ok, "%.3fs"%t, "%.1fus/tested"%(1e6*t/max(1,s[0])))
# identity: exist
I = [[1 if i==j else 0 for j in range(16)] for i in range(16)]
E = Engine([I],4,4); t=time.perf_counter(); print("identity", E.run("exist"), time.perf_counter()-t)
# transposition
T = [[0]*16 for _ in range(16)]
pi = list(range(16)); pi[0],pi[1]=1,0
for j in range(16): T[pi[j]][j]=1
for rules in ("RWV","R"):
    E = Engine([T],4,4,rules=rules); t=time.perf_counter(); st,f,s=E.run("exist", budget=5*10**6); t=time.perf_counter()-t
    print("transposition", rules, st, len(f), s, "%.3fs"%t, "%.1fus/tested"%(1e6*t/max(1,s[0])))
