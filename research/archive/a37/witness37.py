"""For each of the eight other classes: a witness identity H p1 * H p2 = H p3 * H p4 forced by the Dita form at that
class's index maps, with all four SIG entries in {+1, -1} (scaled) so the constants are rational, and with the
u-exponent sums {1, 0}; both proportionality-type and rank-one-type quadruples are searched."""
import itertools, json
exec(open('a37/measure37.py', encoding='utf-8').read().split("E_cand = {}")[0])
B = json.load(open('a37/props37.json'))
CL = [('k1', 4, 4), ('k2', 4, 4), ('k3', 4, 4), ('k4', 4, 4), ('e1', 8, 2), ('e2', 8, 2), ('t2', 2, 8), ('t3', 2, 8)]
src = open('a37/build37.py').read()
exec(src[src.index('CLASSES = ['):src.index('FROZEN = ')])
def sig_val(i, j):
    p, q, r = SIGE[i][j]
    return (p, q, r)
def rational(i, j):
    p, q, r = SIGE[i][j]; return q == 0 and r == 0 and p % 2 == 0     # entry is +1 or -1
def sign(i, j): return 1 if SIGE[i][j][0] == 0 else -1
out = {}
for name, m, n, cp, rows in CLASSES:
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    found = None
    # proportionality type: rows (a,b),(a',b) same class b; columns (c,d),(c,d') same block c
    for b in range(n):
        for a, a2 in itertools.permutations(range(m), 2):
            for c in range(m):
                for d, d2 in itertools.permutations(range(n), 2):
                    p1, p2, p3, p4 = (row[(a, b)], col[(c, d)]), (row[(a2, b)], col[(c, d2)]), (row[(a, b)], col[(c, d2)]), (row[(a2, b)], col[(c, d)])
                    if not all(rational(*p) for p in (p1, p2, p3, p4)): continue
                    e1 = WE[p1[0]][p1[1]] + WE[p2[0]][p2[1]]; e2 = WE[p3[0]][p3[1]] + WE[p4[0]][p4[1]]
                    if {e1, e2} == {0, 1}:
                        found = ('prop', p1, p2, p3, p4, e1, e2); break
                if found: break
            if found: break
        if found: break
    if not found:
        for a in range(1, m):
            for b in range(1, n):
                for c in range(m):
                    j = col[(c, 0)]
                    p1, p2, p3, p4 = (row[(a, b)], j), (row[(0, 0)], j), (row[(a, 0)], j), (row[(0, b)], j)
                    if not all(rational(*p) for p in (p1, p2, p3, p4)): continue
                    e1 = WE[p1[0]][p1[1]] + WE[p2[0]][p2[1]]; e2 = WE[p3[0]][p3[1]] + WE[p4[0]][p4[1]]
                    if {e1, e2} == {0, 1}:
                        found = ('rank1', p1, p2, p3, p4, e1, e2); break
                if found: break
            if found: break
    assert found, name
    kind, p1, p2, p3, p4, e1, e2 = found
    s12 = sign(*p1) * sign(*p2); s34 = sign(*p3) * sign(*p4); assert s12 == s34
    # key: (s12/16) u^e1 = (s34/16) u^e2 ; coefficient c with c*(LHS-RHS) = u - 1
    coef = 16 * s12 if e1 == 1 else -16 * s12
    out[name] = {'kind': kind, 'p': [p1, p2, p3, p4], 'e': [e1, e2], 'sign': s12, 'coef': coef}
    print(name, kind, 'positions', p1, p2, p3, p4, 'exponent sums', e1, e2, 'sign', s12, 'linear_combination coefficient', coef)
json.dump(out, open('a37/witness37.json', 'w'), indent=1)
