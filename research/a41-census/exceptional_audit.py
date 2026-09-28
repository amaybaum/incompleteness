"""Gem-finding follow-up: act 38's exceptional-set search (its section 4) repeated with every label matching. At each of
the forty candidate points, each form and shape, every proportionality candidate of H(u) = SIG o u^E (E the act-38
witness) is tested for the strict and the relaxed rank-one condition under all matchings (exact point calculus)."""
import itertools, json
from lib41 import *
from matchlib import valid_per_group, n_matchings
def cond_E(ent, i, i2, j, j0): return gen_div(gen_div(ent(i, j), ent(i2, j)), gen_div(ent(i, j0), ent(i2, j0)))
E_cand = {}
for form, E in (('column', EE), ('row', ET)):
    ent = ent_of(E)
    for n in (4, 2, 8):
        for Bk in itertools.combinations(range(16), n):
            j0 = Bk[0]
            for i, i2 in itertools.combinations(range(16), 2):
                sets = None; generic = True
                for j in Bk[1:]:
                    s_ = solutions(cond_E(ent, i, i2, j, j0))
                    if s_ == 'all': continue
                    generic = False
                    if s_ == 'none': sets = frozenset(); break
                    sets = s_ if sets is None else (sets & s_)
                    if not sets: break
                if not generic and sets:
                    for pt in sets: E_cand[pt] = E_cand.get(pt, 0) + 1
E_all = sorted(E_cand, key=lambda p: (p[1], p[2], p[0]))
print('candidate points', len(E_all), flush=True)
def div3(a, b): return ((a[0] - b[0]) % 1, a[1] - b[1], a[2] - b[2])
out = []
for pt in E_all:
    for form, E in (('column', EE), ('row', ET)):
        for mn in SHAPES:
            (c_, x_), ent = point_search_E(E, pt, *mn)
            H = lambda i, j: ent[i][j]
            for cp, rows in c_:
                vs = n_matchings(valid_per_group(H, cp, rows, False, div3)); vr = n_matchings(valid_per_group(H, cp, rows, True, div3))
                if vs or vr:
                    out.append({'point': show_pt(pt), 'form': form, 'shape': mn, 'blocks': cp, 'groups': rows, 'sorted_exact': (cp, rows) in x_,
                                'strict_matchings': vs, 'relaxed_matchings': vr})
pts = sorted(set(o['point'] for o in out))
print('points with a structure under some matching (strict or relaxed):', pts)
for o in out:
    if not o['sorted_exact']: print('  missed by the sorted search:', o)
print('structures found at u=1 by form/shape:', {(f, mn): sum(1 for o in out if o['point'] == 'zeta(0) z^0 w^0' and o['form'] == f and tuple(o['shape']) == mn) for f in ('column', 'row') for mn in SHAPES})
json.dump(out, open('exceptional_audit.json', 'w'), default=list, indent=0)
