import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from fractions import Fraction as Fr
from search import observers, tables, counts, chi_hits, windows
from indep import gen
n=5; N=64
obs = observers(2); s0,s1,f = tables('clk',5)
H, chis = chi_hits(counts(2, obs, s0, s1, f, n, 7), 2)
ab, sg = windows(H, N, 7)
oi, ci = np.nonzero(ab)
canon = {}
for o, c in zip(oi, ci):
    w = [Fr(int(H[t, o, c]), N) - Fr(1, 2) for t in range(4, 8)]
    kind = 'pos' if all(x > 0 for x in w) else 'neg' if all(x < 0 for x in w) else 'mixed'
    r0, r1, a = obs[o]
    # canonical form under relabeling of memory states fixing v0 = 0
    best = None
    for p in itertools.permutations([1, 2, 3]):
        P = (0,) + p; Pi = [P.index(i) for i in range(4)]
        key = (tuple(P[r0[Pi[v]]] for v in range(4)), tuple(P[r1[Pi[v]]] for v in range(4)), tuple(a[Pi[v]] for v in range(4)), tuple(chis[c][Pi[v]] for v in range(4)))
        best = key if best is None or key < best else best
    canon.setdefault((best, kind), []).append((int(o), int(c), [str(x) for x in w]))
for (k, kind), lst in sorted(canon.items(), key=lambda z: z[0][1]):
    print(kind, 'canonical', k, 'members', len(lst), lst[0])
# readout at each K' with its own trigger constant (3-bit clock), same rho, a, chi
phi, sig, ff = gen('clk', 5, True)
rho = ([1,0,2,3],[0,2,3,1]); a=[1,0,0,1]; chi=[0,0,0,0]
for Kp in range(4, 8):
    tot = Fr(0)
    for x0 in (0,1):
        for h0 in range(32):
            x,h,v,clk,out = x0,h0,0,0,0
            for t in range(Kp):
                v = rho[x][v]; x ^= a[v]; x,h = phi(x,h); clk = (clk+1) % 8
                if clk == Kp: out ^= int(chi[v] == x)
            tot += Fr(out, 64)
    print('trigger', Kp, 'Pr[out=1]-1/2 =', tot - Fr(1,2))
