"""Step E2: component test, corrected: at a random rational point u of each hull's tangent, dim {v in Def : B(u,v) = 0}."""
import pickle, time, random
from lib36 import *
random.seed(362)
t0 = time.time()
A = pickle.load(open('stepA.pkl', 'rb')); LN = A['LN']
B = pickle.load(open('stepB.pkl', 'rb')); Tb, Rb = B['Tb'], B['Rb']
E = pickle.load(open('stepE.pkl', 'rb')) if os.path.exists('stepE.pkl') else None
D2 = pickle.load(open('stepD2.pkl', 'rb')); results = [r for r in D2['results'] if r[3]]
def Q(v, w):
    out = []
    for (i, j) in PAIRS:
        re = 0; im = 0; ci = i * N; cj = j * N
        for k, (a, b) in enumerate(C_SIG[(i, j)]):
            p = (v[ci + k] - v[cj + k]) * (w[ci + k] - w[cj + k])
            if p: re += a * p; im += b * p
        out.append(re); out.append(im)
    return out
def Bc(v, w):
    q = Q(v, w); return [dot(l, q) for l in LN]
Def = Tb + Rb
def combo(vecs):
    co = [random.randint(-3, 3) for _ in vecs]
    return [sum(c * v[mm] for c, v in zip(co, vecs)) for mm in range(256)]
names = ['%s %s' % (k, cp[:2]) for (k, cp, rows, ok, vecs) in results]
for nm, (k, cp, rows, ok, vecs) in zip(names, results):
    dimo = rank(GAUGE + vecs) - 31
    for trial in range(2):
        u = combo(vecs)
        assert all(dot(r, u) == 0 for r in DF)
        rows_ = [Bc(u, e) for e in Def]
        rk = rank(rows_, 64)
        print('  %-40s trial %d: rank of B(u,.) on Def = %2d -> dim T_u Q = %2d, dim T_o = %2d: %s' % (nm, trial, rk, 49 - rk, dimo, 'COMPONENT (T_u Q = T_o)' if 49 - rk == dimo else 'T_u Q exceeds T_o by %d' % (49 - rk - dimo)))
u = combo(Def); print('generic u in Def: rank of B(u,.) = %d' % rank([Bc(u, e) for e in Def], 64))
print('done (%.0fs)' % (time.time() - t0))
