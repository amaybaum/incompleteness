"""Coordinator audit of act 40 under every within-class matching (read-only; the frozen probe's own functions)."""
import itertools, sys, time
exec(open('probe_head.py', encoding='utf-8').read())
t1 = time.time()
def group_conds(OR, form, mn, cp, rows, b, sb, relaxed):
    Km, Cm = OR[form]; m, n = mn
    def ent(i, j): return (Km[i][j], Cm[i][j])
    def div(x, y): return (ksub(x[0], y[0]), vsub(x[1], y[1]))
    r0 = lambda a: rows[0][a]; rb = lambda a: rows[b][sb[a]]
    lam = lambda R, a, c: div(ent(R(a), cp[c][0]), ent(R(0), cp[c][0]))
    out = []
    for a in range(m):
        for c in range(m):
            if not relaxed: out.append(div(lam(rb, a, c), lam(r0, a, c)))
            elif c > 0: out.append(div(div(lam(rb, a, c), lam(r0, a, c)), div(lam(rb, a, 0), lam(r0, a, 0))))
    return out
def prop_conds(OR, form, mn, cp, rows):
    Km, Cm = OR[form]; m, n = mn
    def ent(i, j): return (Km[i][j], Cm[i][j])
    def div(x, y): return (ksub(x[0], y[0]), vsub(x[1], y[1]))
    return [div(div(ent(i, j), ent(g[0], j)), div(ent(i, bl[0]), ent(g[0], bl[0]))) for g in rows for i in g[1:] for bl in cp for j in bl[1:]]
def add_all(F, conds):
    try:
        for k, c in conds:
            if not any(k):
                if c != V0: return None
                continue
            F = F.add(k, vsub(V0, c))
        return F
    except Empty: return None
def all_loci(key, relaxed):
    form, mn, cp, rows = key; m, n = mn
    Pf = add_all(TORUS, prop_conds(OR, form, mn, cp, rows))
    if Pf is None: return set(), 0
    per = []
    for b in range(1, n):
        L = {}
        for sb in itertools.permutations(range(m)):
            F = add_all(Pf, group_conds(OR, form, mn, cp, rows, b, sb, relaxed))
            if F is not None: L.setdefault(F, []).append(sb)
        per.append(L)
    out = {Pf: 1}
    for L in per:
        nxt = {}
        for F, cnt in out.items():
            for G_, sbs in L.items():
                H_ = meet_or_none(F, G_)
                if H_ is not None: nxt[H_] = nxt.get(H_, 0) + cnt * len(sbs)
        out = nxt
    return set(out), sum(out.values())
res = {}
for key in CANDS:
    res[key] = (all_loci(key, False), all_loci(key, True))
print('audit time %.0fs' % (time.time() - t1))
sorted_strict = {k: solve(conditions(OR, *k, False)) for k in CANDS}
# 1. the sorted labelling is among the enumerated ones
print('sorted locus reproduced as one matching locus:', all(sorted_strict[k] is None or sorted_strict[k] in res[k][0][0] for k in CANDS))
ne_s = [k for k in CANDS if res[k][0][0]]; ne_r = [k for k in CANDS if res[k][1][0]]
print('candidates with nonempty strict / relaxed locus (all matchings):', len(ne_s), len(ne_r), ' sorted-only strict:', sum(1 for v in sorted_strict.values() if v is not None))
allS = set().union(*(res[k][0][0] for k in CANDS)); allR = set().union(*(res[k][1][0] for k in CANDS))
print('distinct flats strict / relaxed:', len(allS), len(allR))
def maximal(fl):
    return sorted((F for F in fl if not any(G_ != F and G_.contains(F) for G_ in fl)), key=lambda F: F.B)
for nm, fl in (('strict', allS), ('relaxed', allR)):
    mx = maximal(fl)
    print(nm, 'maximal:', [F.show() for F in mx])
    print(nm, 'non-coordinate flats:', sorted(F.show() for F in fl if not all(sorted(map(abs, k)) == [0, 0, 1] and v in (V0, (2, 0, 0)) for k, v in F.B)))
FACES5 = [Flat([((1,0,0),(2,0,0))]), Flat([((1,0,0),V0)]), Flat([((0,1,0),V0)]), Flat([((0,0,1),(2,0,0))]), Flat([((0,0,1),V0)])]
for nm, fl in (('strict', allS), ('relaxed', allR)):
    print(nm, 'every flat inside one of the five faces:', all(any(Fc.contains(F) for Fc in FACES5) for F in fl), ' each face attained:', all(Fc in fl for Fc in FACES5))
def count_at(u, idx):
    return sum(1 for k in CANDS if any(on_flat(F, u) for F in res[k][idx][0]))
for nm, u in (('(1,1,1)', (ONE, ONE, ONE)), ('(-1,-1,-1)', (G(-1), G(-1), G(-1)))):
    print('structures at', nm, 'strict', count_at(u, 0), 'relaxed', count_at(u, 1))
