"""A37 pre-freeze measurement (read-only): the exceptional set of the arc H(u) = SIG o u^W, exactly.

Every entry of SIG = F4(z) x F4(w) is a monomial i^p z^q w^r, so every entry of H(u) is i^p z^q w^r u^k with
k = W(i, j). A Dita structure (column blocks, row classes) is admitted at u iff finitely many monomial equations
hold (row proportionality on every block and the rank-one condition on the block ratios); unitarity of the factors
follows from the unitarity of H(u) and is checked separately as a control. Each monomial equation
u^k = i^p z^q w^r has, for k != 0, exactly |k| unit solutions u = zeta z^(-q/k) w^(-r/k), zeta a root of unity,
and since z = (2+i)/(2-i) and w = (3+2i)/(3-2i) are multiplicatively independent modulo roots of unity (distinct
Gaussian primes), the triple (zeta, s, t) with u = zeta z^s w^t is a canonical exact name for a point.
Monomials at a specialized point are triples (angle of zeta in turns mod 1, s, t) and are compared exactly."""
import itertools, sys, time, collections
from fractions import Fraction as Fr
t0 = time.time()
src = open('a37/probe36.py', encoding='utf-8').read()
exec(src[:src.index("print('== 1.")])                                     # numeric objects for the controls
exec(src[src.index('def is_unitary_s'):src.index('PT = [list(c)')])         # the probe's numeric search (control)

# ---- symbolic entries: (p mod 4, q, r) with value i^p z^q w^r ---------------------------------------------------
F4E = [[(0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), (0, 1), (2, 0), (2, 1)], [(0, 0), (2, 0), (0, 0), (2, 0)], [(0, 0), (2, 1), (2, 0), (0, 1)]]
SIGE = [[None] * 16 for _ in range(16)]
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                (p1, q), (p2, r) = F4E[a][c], F4E[b][d]
                SIGE[4 * a + b][4 * c + d] = ((p1 + p2) % 4, q, r)
def gpow_(x, k):
    out = ONE
    for _ in range(k): out = out * x
    return out
def val(p, q, r): return gpow_(I_, p) * gpow_(z, q) * gpow_(w, r)
assert all(val(*SIGE[i][j]) == SIG[i][j] for i in range(16) for j in range(16)), 'symbolic SIG differs from the numeric SIG'
WE = [[W[i * 16 + j] for j in range(16)] for i in range(16)]
assert WE == [list(c) for c in zip(*WE)], 'W is not symmetric'
print('symbolic SIG matches numeric SIG; W symmetric; W values', sorted(set(W)))

# ---- monomials with the u exponent kept symbolic: (k, p mod 4, q, r); at a point (zeta, s, t): (angle, S, T) ----
def gen_entry(i, j): p, q, r = SIGE[i][j]; return (WE[i][j], p, q, r)
def gen_div(m1, m2): return (m1[0] - m2[0], (m1[1] - m2[1]) % 4, m1[2] - m2[2], m1[3] - m2[3])
def gen_mul(m1, m2): return (m1[0] + m2[0], (m1[1] + m2[1]) % 4, m1[2] + m2[2], m1[3] + m2[3])
GEN_ONE = (0, 0, 0, 0)
def solutions(m):
    """the unit solutions u of the monomial equation u^k i^p z^q w^r = 1, as canonical points, or 'all'/'none'"""
    k, p, q, r = m
    if k == 0: return 'all' if (p % 4 == 0 and q == 0 and r == 0) else 'none'
    pts = set()
    for n in range(abs(k)):
        ang = (Fr(-p, 4) + n) / k       # zeta^k = i^(-p), the k solutions
        pts.add((ang % 1, Fr(-q, k), Fr(-r, k)))
    return frozenset(pts)
def at_point(m, pt):
    k, p, q, r = m; ang, s, t = pt
    return ((Fr(p, 4) + k * ang) % 1, q + k * s, r + k * t)
def is_one_at(m, pt): return at_point(m, pt) == (Fr(0), Fr(0), Fr(0))
def show_pt(pt):
    ang, s, t = pt
    return 'zeta(%s turn) z^%s w^%s' % (ang, s, t)

# ---- M2: proportionality of every row pair on every block, generically and at special points ------------------
def cond(i, i2, j, j0): return gen_div(gen_div(gen_entry(i, j), gen_entry(i2, j)), gen_div(gen_entry(i, j0), gen_entry(i2, j0)))
E_cand = {}                                    # point -> set of (n, block, pair) where a new proportionality appears
generic_pairs = {}                             # n -> {block: set of generically proportional pairs}
for n in (4, 2, 8):
    gp = {}
    for B in itertools.combinations(range(16), n):
        j0 = B[0]; prs = set()
        for i, i2 in itertools.combinations(range(16), 2):
            sets = None; generic = True
            for j in B[1:]:
                s_ = solutions(cond(i, i2, j, j0))
                if s_ == 'all': continue
                generic = False
                if s_ == 'none': sets = frozenset(); break
                sets = s_ if sets is None else (sets & s_)
                if not sets: break
            if generic: prs.add((i, i2))
            elif sets:
                for pt in sets: E_cand.setdefault(pt, set()).add((n, B, (i, i2)))
        gp[B] = prs
    generic_pairs[n] = gp
    print('n=%d: blocks %d; generically proportional pairs on some block: %d; E_cand so far %d points (%.0fs)' % (n, len(gp), sum(len(v) for v in gp.values()), len(E_cand), time.time() - t0))
print('candidate exceptional points (where some row pair becomes proportional on some block):')
for pt in sorted(E_cand, key=lambda p: (p[1], p[2], p[0])):
    print('   %-32s  from %d (n, block, pair) triples' % (show_pt(pt), len(E_cand[pt])))

# ---- the exact structure search on a monomial matrix (generic, or specialized at a point) ---------------------
def search(entry, div, eq_one, m, n):
    """the probe's dita_orientations on a matrix given by entry(i, j) monomials: proportionality classes by exact ratio
    keys, the partition recursion, and the rank-one condition; returns (candidates, exact) as lists of (cp, rows)"""
    good = {}
    for S in itertools.combinations(range(16), n):
        keys = {}
        for i in range(16):
            keys.setdefault(tuple(div(entry(i, s), entry(i, S[0])) for s in S), []).append(i)
        Pp = sorted(tuple(v) for v in keys.values())
        if all(len(cl) == m for cl in Pp): good[S] = Pp
    parts = []
    def rec(rem, chosen):
        if not rem: parts.append(tuple(chosen)); return
        first = min(rem)
        for S in good:
            if first in S and set(S) <= rem: rec(rem - set(S), chosen + [S])
    rec(set(range(16)), [])
    cands, exact = [], []
    for cp in parts:
        cls = {i: tuple(next(ci for ci, cl in enumerate(good[S]) if i in cl) for S in cp) for i in range(16)}
        groups = {}
        for i in range(16): groups.setdefault(cls[i], []).append(i)
        rows = sorted(tuple(v) for v in groups.values())
        if not all(len(g) == m for g in rows): continue
        cands.append((cp, rows))
        col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
        lam = {(a, b, c): div(entry(row[(a, b)], col[(c, 0)]), entry(row[(0, b)], col[(c, 0)])) for a in range(m) for b in range(n) for c in range(m)}
        rank1 = all(eq_one(div(lam[(a, b, c)], gen_mul(lam[(a, 0, c)], lam[(0, b, c)]))) for a in range(m) for b in range(n) for c in range(m))
        if rank1: exact.append((cp, rows))
    return cands, exact
def gen_eq_one(m): return m == GEN_ONE
print('\nstructures admitted at generic u (u a free symbol):')
generic_exact = {}
for (m, n) in ((4, 4), (8, 2), (2, 8)):
    cands, exact = search(gen_entry, gen_div, gen_eq_one, m, n)
    generic_exact[(m, n)] = exact
    print('  %dx%d: candidates %d, exact %d' % (m, n, len(cands), len(exact)))
    for cp, rows in cands: print('     candidate blocks %s classes %s  exact: %s' % (cp, rows, (cp, rows) in exact))
print('(%.0fs)' % (time.time() - t0))
# rank-one failures of generic candidates: the monomial they require, and its solutions -> more candidate points
def rank1_points(m, n, cp, rows):
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    lam = {(a, b, c): gen_div(gen_entry(row[(a, b)], col[(c, 0)]), gen_entry(row[(0, b)], col[(c, 0)])) for a in range(m) for b in range(n) for c in range(m)}
    pts = None
    for a in range(m):
        for b in range(n):
            for c in range(m):
                mm = gen_div(lam[(a, b, c)], gen_mul(lam[(a, 0, c)], lam[(0, b, c)]))
                s_ = solutions(mm)
                if s_ == 'all': continue
                if s_ == 'none': return frozenset()
                pts = s_ if pts is None else pts & s_
    return pts if pts is not None else 'all'
E_rank = {}
for (m, n) in ((4, 4), (8, 2), (2, 8)):
    cands, exact = search(gen_entry, gen_div, gen_eq_one, m, n)
    for cp, rows in cands:
        if (cp, rows) in exact: continue
        pts = rank1_points(m, n, cp, rows)
        print('  generic candidate %dx%d blocks %s: rank-one holds exactly at %s' % (m, n, cp, 'no point' if not pts else ', '.join(show_pt(p) for p in sorted(pts))))
        for p in (pts or ()): E_rank.setdefault(p, set()).add((m, n, cp, tuple(rows)))
E_all = set(E_cand) | set(E_rank)
print('\ncandidate exceptional set: %d points' % len(E_all))

# ---- M4: the exact search at every candidate point --------------------------------------------------------------
FROZEN = ((0, 1, 2, 3, 8, 9, 10, 11), (4, 5, 6, 7, 12, 13, 14, 15))
E_exact = {}
for pt in sorted(E_all, key=lambda p: (p[1], p[2], p[0])):
    entry = lambda i, j, pt=pt: at_point(gen_entry(i, j), pt)
    div = lambda m1, m2: ((m1[0] - m2[0]) % 1, m1[1] - m2[1], m1[2] - m2[2])
    def mul3(m1, m2): return ((m1[0] + m2[0]) % 1, m1[1] + m2[1], m1[2] + m2[2])
    eq1 = lambda m: m == (Fr(0), Fr(0), Fr(0))
    # rank-one check inside search uses gen_mul on 4-tuples; give it the 3-tuple version
    globals()['gen_mul_saved'] = gen_mul
    globals()['gen_mul'] = mul3
    res = {}
    for (m, n) in ((4, 4), (8, 2), (2, 8)):
        cands, exact = search(entry, div, eq1, m, n)
        res[(m, n)] = (len(cands), [(cp, rows) for cp, rows in exact])
    globals()['gen_mul'] = gen_mul_saved
    others = [(mn, cp) for mn, (nc, ex) in res.items() for cp, rows in ex if not (mn == (2, 8) and cp == FROZEN)]
    frozen_ok = any(cp == FROZEN for cp, rows in res[(2, 8)][1])
    E_exact[pt] = (res, others, frozen_ok)
    print('  %-32s  candidates 4x4/8x2/2x8: %d/%d/%d  exact: %d/%d/%d  frozen 2x8 present: %s  other structures: %d' % (
        show_pt(pt), res[(4, 4)][0], res[(8, 2)][0], res[(2, 8)][0], len(res[(4, 4)][1]), len(res[(8, 2)][1]), len(res[(2, 8)][1]), frozen_ok, len(others)))
exact_E = sorted((pt for pt, (res, others, fo) in E_exact.items() if others), key=lambda p: (p[1], p[2], p[0]))
print('\nEXACT exceptional set (points where a structure other than the frozen 2x8 class is admitted): %d' % len(exact_E))
for pt in exact_E: print('   ', show_pt(pt), '->', len(E_exact[pt][1]), 'other structures')
print('(%.0fs)' % (time.time() - t0))

# ---- controls: numeric probe search at Gaussian-rational points of the candidate set ----------------------------
def numeric_point(pt):
    """the Gaussian rational value of a canonical point when it is Gaussian rational: integer s, t and angle in quarters"""
    ang, s, t = pt
    if s.denominator != 1 or t.denominator != 1 or (ang * 4).denominator != 1: return None
    q = int(ang * 4) % 4
    v = gpow_(I_, q)
    zz = z if s >= 0 else z.conj(); ww = w if t >= 0 else w.conj()
    for _ in range(abs(int(s))): v = v * zz
    for _ in range(abs(int(t))): v = v * ww
    return v
print('\ncontrols at Gaussian-rational candidate points (numeric exhaustive search of the certified probe):')
for pt in sorted(E_all, key=lambda p: (p[1], p[2], p[0])):
    uv = numeric_point(pt)
    if uv is None: print('   %-32s  not Gaussian rational; symbolic only' % show_pt(pt)); continue
    Hu = [[SIG[i][j] * gpow(uv, W[i * 16 + j]) for j in range(16)] for i in range(16)]
    assert is_unitary16(Hu)
    counts = {}
    for (m, n) in ((4, 4), (8, 2), (2, 8)):
        o = dita_orientations(Hu, m, n); counts[(m, n)] = (len(o), sum(1 for x in o if x[2]))
    sym = E_exact[pt][0]
    agree = all(counts[mn] == (sym[mn][0], len(sym[mn][1])) for mn in counts)
    print('   %-32s  u = %s  numeric (cand, exact) 4x4 %s 8x2 %s 2x8 %s  agrees with symbolic: %s' % (show_pt(pt), uv.key(), counts[(4, 4)], counts[(8, 2)], counts[(2, 8)], agree))
print('done (%.0fs)' % (time.time() - t0))
