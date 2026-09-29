"""Populate supports 41-47: members of the two three-parameter straight families (act 38's xA+yB+zC and this
thread's -xP+yQ-zT), |x|,|y|,|z| <= 2, that are straight (exact) and outside every complete structure (20 structures,
all labellings); their minimal support over gauge (HiGHS, attained value exact) and the act-37 generic search on one
member per support value."""
import itertools, json, numpy as np
from lib42 import *
from complete42 import complete_members
from minsupp_milp import min_support_milp
from witness42 import P, Q, T, search_generic
fams = {'ABC': (A38, B38, C38), 'PQT': ([[-v for v in r] for r in P], Q, [[-v for v in r] for r in T])}
best = {}
for fn, (U, V, W_) in fams.items():
    for x, y, z in itertools.product(range(-2, 3), repeat=3):
        if 0 in (x, y, z): continue
        E = [[x * U[i][j] + y * V[i][j] + z * W_[i][j] for j in range(16)] for i in range(16)]
        if complete_members(np.array(E).reshape(256)): continue
        assert straight_direct(E)
        s, Es, st, db, ob = min_support_milp(E)
        print(fn, (x, y, z), 'min support', s, st, flush=True)
        if s not in best: best[s] = (fn, (x, y, z), Es.tolist(), st)
out = {}
for s in sorted(best):
    fn, c, Es, st = best[s]; ET = [list(r) for r in zip(*Es)]
    gen = [len(r) for mn in SHAPES for r in search_generic(Es, *mn)] + [len(r) for mn in SHAPES for r in search_generic(ET, *mn)]
    out[s] = {'family': fn, 'coeffs': c, 'milp_status': st, 'generic_all_zero': not any(gen), 'straight_exact': straight_direct(Es),
              'complete_members': complete_members(np.array(Es).reshape(256)), 'representative': Es}
    print(s, {k: v for k, v in out[s].items() if k != 'representative'}, flush=True)
json.dump(out, open('family_scan.json', 'w'), indent=0)
