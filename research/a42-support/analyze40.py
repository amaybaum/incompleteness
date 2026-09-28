import pickle, numpy as np, collections, sys, time
from lib42 import *
t0 = time.time()
d = pickle.load(open(sys.argv[1], 'rb'))
X = np.array([x for R, x in d['nond']])
clo = pickle.load(open('closure.pkl', 'rb'))
inclo = np.zeros(len(X), dtype=bool); which = collections.Counter()
for k, n, M in clo:
    hit = ~(X @ M.T).any(axis=1)
    inclo |= hit
    if hit.any(): which[(k, n is None)] += int(hit.sum())
print('leaves', len(X), 'in the 34-member stabilizer closure:', int(inclo.sum()), dict(which))
# generic structure search (act-37 monomial calculus, matching-independent candidate count)
def entry_fn(E):
    def ent(i, j):
        p, q, r = SIGE[i][j]; return (E[i][j], p, q, r)
    return ent
def search_generic(E, m, n):
    ent = entry_fn(E)
    ratio = [[[gen_div(ent(i, s), ent(i, s0)) for s in range(16)] for s0 in range(16)] for i in range(16)]
    return structures(ent, gen_div, gen_mul, lambda x: x == GEN_ONE, m, n, ratio)
idx = [k for k in range(len(X)) if not inclo[k]][:3] + [0]
for k in idx:
    E = X[k].reshape(16, 16).tolist(); ET = [list(c) for c in zip(*E)]
    res = {('col', mn): tuple(len(x) for x in search_generic(E, *mn)) for mn in SHAPES}
    res.update({('row', mn): tuple(len(x) for x in search_generic(ET, *mn)) for mn in SHAPES})
    print('leaf', k, 'support', support(E), 'straight_direct', straight_direct(E), 'in closure', bool(inclo[k]), 'generic (candidates, exact):', res, '%.0fs' % (time.time() - t0), flush=True)
