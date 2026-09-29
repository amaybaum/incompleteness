"""The support-40 non-Dita straight line, stated in closed form and verified exactly.

    E40[(a,b),(c,d)] = - [b = 0][c = 0]  +  [a = 2][b odd][d even]  -  [a even][c odd][d = 0]
                     =      - P               +        Q              -          T
P (4x4), Q (2x8), T (8x2) are support-16 rectangles; Q and T overlap in the 4 cells rows {9, 11} x columns {4, 12},
where they cancel, so |supp E40| = 16 + 16 + 16 - 2*4 = 40.
Checks: straightness (exact Laurent identity, no tables); the act-37 generic structure search (candidate counts, which
do not depend on label matchings) for every shape and both forms; complete membership (20 structures, all matchings);
N18 membership; membership table of the pieces and of their signed sums; the minimal support over gauge (HiGHS
integer programme; the attained value is exact, the optimality rests on the solver certificate); sum(E) mod 16."""
import json, itertools
import numpy as np
from lib42 import *
from classify42 import member_masks, KEYS
from complete42 import complete_members
from minsupp_milp import min_support_milp
def mat(f): return [[f(i // 4, i % 4, j // 4, j % 4) for j in range(16)] for i in range(16)]
P = mat(lambda a, b, c, d: int(b == 0 and c == 0))
Q = mat(lambda a, b, c, d: int(a == 2 and b % 2 == 1 and d % 2 == 0))
T = mat(lambda a, b, c, d: int(a % 2 == 0 and c % 2 == 1 and d == 0))
def lin(x, y, z): return [[-x * P[i][j] + y * Q[i][j] - z * T[i][j] for j in range(16)] for i in range(16)]
E40 = lin(1, 1, 1)
def entry_fn(E):
    def ent(i, j):
        p, q, r = SIGE[i][j]; return (E[i][j], p, q, r)
    return ent
def search_generic(E, m, n):
    ent = entry_fn(E)
    ratio = [[[gen_div(ent(i, s), ent(i, s0)) for s in range(16)] for s0 in range(16)] for i in range(16)]
    return structures(ent, gen_div, gen_mul, lambda x: x == GEN_ONE, m, n, ratio)
out = {}
print('support', support(E40), 'entries', sorted(set(x for r in E40 for x in r)))
out['support'] = support(E40)
out['straight_exact'] = straight_direct(E40); out['straight_tables'] = straight(E40)
ET = [list(r) for r in zip(*E40)]
gen = {('col %dx%d' % mn): [len(x) for x in search_generic(E40, *mn)] for mn in SHAPES}
gen.update({('row %dx%d' % mn): [len(x) for x in search_generic(ET, *mn)] for mn in SHAPES})
out['generic_candidates_exact'] = gen
flat = np.array(E40).reshape(256)
out['complete_members'] = complete_members(flat)
ms, mr = member_masks(flat[None, :]); out['N18_members'] = [KEYS[k] for k in range(18) if (mr[0] >> k) & 1]
s, Es, st, db, ob = min_support_milp(E40)
out['min_support_over_gauge'] = s; out['milp_status'] = st; out['milp_dual_bound_zeros'] = db
out['sum_mod16'] = int(flat.sum()) % 16
table = {}
for nm, (x, y, z) in (('P', (1, 0, 0)), ('Q', (0, 1, 0)), ('T', (0, 0, 1)), ('-P+Q', (1, 1, 0)), ('-P-T', (1, 0, 1)),
                      ('Q-T', (0, 1, 1)), ('-P+Q-T', (1, 1, 1))):
    M = lin(x, y, z)
    table[nm] = {'support': support(M), 'straight': straight_direct(M), 'complete_members': complete_members(np.array(M).reshape(256))}
out['pieces'] = table
fam = all(straight(lin(x, y, z)) for x, y, z in itertools.product(range(-2, 3), repeat=3))
out['all xP+yQ+zT straight for |x|,|y|,|z|<=2'] = fam
for k, v in out.items(): print(k, v)
json.dump(out, open('witness42.json', 'w'), indent=1, default=str)
