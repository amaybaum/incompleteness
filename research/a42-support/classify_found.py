"""Classify every stored leaf outside the 18 census subspaces: orbit classes under gauge x stabilizer x sign
(canonical form = lexicographically least gauge-normal image), and for one representative per class: support of the
stored representative, exact minimal support over gauge (minsupp.py), exact straightness by the Laurent identity
(no tables), membership in the 34-member stabilizer closure and in the matching-complete family, the det/trace
invariant sum(E) = 0 mod 16, and the act-37 generic structure search (candidates and exact structures, every shape,
both forms) which does not depend on the within-class matching."""
import sys, pickle, time, collections, json
import numpy as np
from lib42 import *
from minsupp_milp import min_support_milp
from complete42 import complete_members
t0 = time.time()
X = np.concatenate([np.array([x for R, x in pickle.load(open(f, 'rb'))['nond']]).reshape(-1, 256) for f in sys.argv[2:]])
out = sys.argv[1]
PERMS = np.array([np.argsort(np.array(p)) for p, s_ in elems]); SIGNS = np.array([s_ for p, s_ in elems])
def canon(flat):
    imgs = flat[PERMS] * SIGNS[:, None]
    imgs = np.concatenate([imgs, -imgs]).reshape(-1, 16, 16)
    imgs = imgs - imgs[:, :, :1] - imgs[:, :1, :] + imgs[:, :1, :1]
    f = imgs.reshape(-1, 256); o = np.lexsort(f.T[::-1]); return tuple(int(v) for v in f[o[0]])
classes = {}
for k in range(len(X)):
    c = canon(X[k])
    if c not in classes: classes[c] = []
    classes[c].append(k)
print('leaves', len(X), 'orbit classes', len(classes), '%.0fs' % (time.time() - t0), flush=True)
clo = pickle.load(open('closure.pkl', 'rb'))
fall = None
def entry_fn(E):
    def ent(i, j):
        p, q, r = SIGE[i][j]; return (E[i][j], p, q, r)
    return ent
def search_generic(E, m, n):
    ent = entry_fn(E)
    ratio = [[[gen_div(ent(i, s), ent(i, s0)) for s in range(16)] for s0 in range(16)] for i in range(16)]
    return structures(ent, gen_div, gen_mul, lambda x: x == GEN_ONE, m, n, ratio)
rows = []
for c, ks in classes.items():
    k = min(ks, key=lambda k: (int((X[k] != 0).sum()), tuple(X[k])))
    E = X[k].reshape(16, 16).tolist(); ET = [list(r) for r in zip(*E)]
    sup = support(E)
    minsup, Estar, mst, mdb, mob = min_support_milp(E)
    gen = {('col',) + mn: tuple(len(x) for x in search_generic(E, *mn)) for mn in SHAPES}
    gen.update({('row',) + mn: tuple(len(x) for x in search_generic(ET, *mn)) for mn in SHAPES})
    v = X[k]
    inclo = any(not (M @ v).any() for _, _, M in clo)
    infall = None if fall is None else any(not (M @ v).any() for *_, M in fall)
    cm = complete_members(v)
    rec = {'members': len(ks), 'complete_members': cm, 'support_stored': sup, 'min_support_over_gauge': minsup, 'milp_status': mst, 'milp_dual_bound_zeros': mdb, 'straight_exact': straight_direct(E),
           'sum_mod16': int(v.sum()) % 16, 'in_closure34': inclo,
           'generic_candidates_all_zero': all(x == (0, 0) for x in gen.values()), 'generic': {'%s %dx%d' % kk: vv for kk, vv in gen.items()},
           'representative': E}
    rows.append(rec)
    print(json.dumps({kk: vv for kk, vv in rec.items() if kk not in ('representative', 'generic')}), '%.0fs' % (time.time() - t0), flush=True)
json.dump(rows, open(out, 'w'), indent=0)
