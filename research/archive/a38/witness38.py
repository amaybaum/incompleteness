"""Choose the kernel witness identity for each of the 18 census structures (column and row forms) on the witness arc.
Prefer a proportionality witness with rational entries, |k| = 1 and positive sign; fall back to a rectangle (rank-type)
witness; t2-column has no rational |k| = 1 witness and takes the non-rational proportionality identity."""
import sys, json, pickle; sys.path.insert(0, 'a38')
from lib38c import *
E = pickle.load(open('a38/witness1.pkl', 'rb'))
def sgn(i, j): return 1 if SIGE[i][j][0] == 0 else -1
def rational(P): return all(SIGE[a][b][1] == 0 and SIGE[a][b][2] == 0 and SIGE[a][b][0] % 2 == 0 for a, b in P)
def forced_list(s, tr):
    (m, n), cp, rows = s
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    def T(i, j): return (j, i) if tr else (i, j)
    out = []
    for b in range(n):
        for a in range(m):
            for a2 in range(m):
                if a2 == a: continue
                for c in range(m):
                    for d in range(n):
                        for d2 in range(n):
                            if d2 == d: continue
                            out.append(('prop', [T(row[(a, b)], col[(c, d)]), T(row[(a2, b)], col[(c, d2)]), T(row[(a, b)], col[(c, d2)]), T(row[(a2, b)], col[(c, d)])]))
    for a in range(m):
        for a2 in range(m):
            if a2 == a: continue
            for b in range(n):
                for b2 in range(n):
                    if b2 == b: continue
                    for j in range(16):
                        out.append(('rank', [T(row[(a, b)], j), T(row[(a2, b2)], j), T(row[(a, b2)], j), T(row[(a2, b)], j)]))
    return out
WIT = {}
for s in CENSUS9:
    for tr in (False, True):
        key = NAMES9[s] + ('_row' if tr else '_col')
        best = None
        for kind, P in forced_list(s, tr):
            e1 = E[P[0][0]][P[0][1]] + E[P[1][0]][P[1][1]]; e2 = E[P[2][0]][P[2][1]] + E[P[3][0]][P[3][1]]
            if abs(e1 - e2) != 1: continue
            rat = rational(P)
            sg = sgn(*P[0]) * sgn(*P[1]) if rat else 0
            cand = (0 if rat else 1, 0 if kind == 'prop' else 1, 0 if sg == 1 else 1, sorted(P), kind, P, (e1, e2), sg)
            if best is None or cand[:4] < best[:4]: best = cand
        assert best is not None, key
        rat, _, _, _, kind, P, e, sg = best
        rec = {'kind': kind, 'p': P, 'e': list(e), 'rational': rat == 0}
        if rat == 0:
            rec['sign'] = sg; rec['coef'] = (16 // sg) if e[0] > e[1] else (-16 // sg)
        else:
            # the identity reads c u^{e1} = c u^{e2} with c = prod of the two SIG entries / 16 (monomial i^p z^q w^r)
            m1 = SIGE[P[0][0]][P[0][1]]; m2 = SIGE[P[1][0]][P[1][1]]
            rec['monomial'] = [(m1[0] + m2[0]) % 4, m1[1] + m2[1], m1[2] + m2[2]]
            m3 = SIGE[P[2][0]][P[2][1]]; m4 = SIGE[P[3][0]][P[3][1]]
            assert rec['monomial'] == [(m3[0] + m4[0]) % 4, m3[1] + m4[1], m3[2] + m4[2]]
        WIT[key] = rec
        print(key, rec)
json.dump(WIT, open('a38/witness38.json', 'w'), indent=1, sort_keys=True)
# check each witness identity is forced and reads as stated: evaluate both sides symbolically on the arc
for key, w in WIT.items():
    P = [tuple(p) for p in w['p']]; ent = entry_fn(E)
    l = gen_mul(ent(*P[0]), ent(*P[1])); r = gen_mul(ent(*P[2]), ent(*P[3]))
    assert l[1:] == r[1:] and abs(l[0] - r[0]) == 1 and [l[0], r[0]] == w['e'], (key, l, r)
print('all 18 witness identities: same constant monomial, u-exponents differ by one')
