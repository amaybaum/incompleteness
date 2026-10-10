# ---- section 7: Boolean carriers defined in the repository (hull and stratum membership) -------------------------------
print('== section 7: act 35 hull membership and act 34 stratum membership (necessary conditions, exact)')
def gdiv(x, y): n = y.norm2(); c = x * y.conj(); return G(c.a / n, c.b / n)
def col_hull_necessary(H):
    """necessary conditions for D1 H D2 to be act 35's column construction X[a,c] D[c,b] Y_c[b,d] at the product index
    (row (a,b) -> 4a+b, column (c,d) -> 4c+d): rows of each class b proportional on each block c, and
    lambda(a,b,c)/lambda(a,0,c) independent of c (act 38 Hazard 5's relaxed form)"""
    for b in range(4):
        for c in range(4):
            for a, a2 in itertools.combinations(range(4), 2):
                for d, d2 in itertools.combinations(range(4), 2):
                    r, r2, s, s2 = 4 * a + b, 4 * a2 + b, 4 * c + d, 4 * c + d2
                    if H[r][s] * H[r2][s2] != H[r][s2] * H[r2][s]: return False
    lam = {(a, b, c): gdiv(H[4 * a + b][4 * c], H[b][4 * c]) for a in range(4) for b in range(4) for c in range(4)}
    return all(lam[(a, b, c)] * lam[(a, 0, 0)] == lam[(a, b, 0)] * lam[(a, 0, c)]
               for a in range(4) for b in range(4) for c in range(4))
def transpose(H): return [list(c) for c in zip(*H)]
hull_col = {n: col_hull_necessary(H3(u)) for n, u in PTS.items()}
hull_row = {n: col_hull_necessary(transpose(H3(u))) for n, u in PTS.items()}
print('   column-hull necessary conditions hold at:', [n for n, v in hull_col.items() if v])
print('   row-hull necessary conditions hold at:   ', [n for n, v in hull_row.items() if v])
check('control: SIG satisfies the column-hull conditions (a product is a column construction with D = 1)', hull_col['SIG(1,1,1)'], True)
fc = next((n for n in list(PTS)[:7] if not hull_col[n]), None); fr = next((n for n in list(PTS)[:7] if not hull_row[n]), None)
check('column-hull membership: exhibited collision, face point %s and off-face O1 both fail the necessary conditions' % fc,
      (fc is not None, hull_col['O1(v1,v2,v3)']), (True, False))
check('row-hull membership: exhibited collision, face point %s and off-face O1 both fail the necessary conditions' % fr,
      (fr is not None, hull_row['O1(v1,v2,v3)']), (True, False))
check('stratum membership: F1- (in L) and O1 (off L) both fail act 35 identity, hence both off the product stratum',
      (vals['F1-(-1,v2,v3)'], vals['O1(v1,v2,v3)']), (False, False))

# ---- section 8: the toy coordinate u1 and the distance to SIG -----------------------------------------------------------
print('== section 8: the toy u1 and exact collisions of the distance to SIG')
u, v = (V1, ONE, V3), (V1, V2, V3)
check('toy u1 separates a cross-boundary pair ((1,v2,v3) vs (v1,v2,v3)) but collides ((v1,1,v3) in L, (v1,v2,v3) off L)',
      (PTS['F1+(1,v2,v3)'][0] != PTS['O1(v1,v2,v3)'][0], in_L(u), in_L(v), u[0] == v[0]), (True, True, False, True))
# symmetries of the exponent distribution under signed permutations of the three axes
syms = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        def T(m, perm=perm, sg=sg):
            out = [0, 0, 0]
            for k in range(3): out[perm[k]] = sg[k] * m[k]
            return tuple(out)
        if all(NM[T(m)] == c for m, c in NM.items()): syms.append((perm, sg))
print('   signed axis permutations preserving the exponent distribution:', syms)
# exhaustive exact search over the 64 points with coordinates in {1, i, -1, -i}, then a wider grid
def dist_collisions(grid):
    table = {}
    for u in itertools.product(grid, repeat=3):
        table.setdefault(dist2(u), []).append(u)
    return [(val, us) for val, us in table.items() if any(in_L(x) for x in us) and any(not in_L(x) for x in us)]
col4 = dist_collisions([ONE, I_, MONE, -I_])
print('   fourth-root grid: %d cross-boundary collisions of d' % len(col4))
exhibit = None
if col4:
    val, us = col4[0]
    a = next(x for x in us if in_L(x)); b = next(x for x in us if not in_L(x)); exhibit = (a, b, val)
else:
    colw = dist_collisions([ONE, I_, MONE, -I_, V1, V1.conj(), -V1, -V1.conj()])
    print('   wider grid: %d cross-boundary collisions of d' % len(colw))
    if colw:
        val, us = colw[0]
        a = next(x for x in us if in_L(x)); b = next(x for x in us if not in_L(x)); exhibit = (a, b, val)
if exhibit:
    a, b, val = exhibit
    check('distance to SIG: exhibited exact collision %s in L, %s off L, 16^6 d^2 = %s at both' % (a, b, val),
          (in_L(a), in_L(b), dist2(a) == dist2(b)), (True, False, True))
else:
    print('   distance to SIG: no exact collision exhibited on the grids; non-detection rests on the topological lemma')
