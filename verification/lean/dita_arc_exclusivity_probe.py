"""Track B act 37 -- the exact-computation probe of the arc-exclusivity round (frozen with the control plane).

Everything asserted is exact arithmetic: Gaussian rationals in Python integers and fractions for the numeric
searches, and an exact monomial calculus for the symbolic ones, in which every entry of SIG o u^W is a monomial
i^p z^q w^r u^k and every point of the unit circle that the analysis singles out is named canonically as
zeta z^s w^t. The probe asserts the preregistered values and exits 1 on any mismatch; it certifies nothing on its
own beyond the arithmetic it replays. Its first part is act 36's probe head, verbatim, for the shared objects and
act 36's structure search, exhaustive over column blocks and row classes and testing each partition structure at the
sorted alignment (the rows of each row class in sorted order). The censuses over every index map are act 41's probes
verification/lean/dita_index_map_probe.py and verification/lean/dita_index_map_independent.py.

Objects (acts 24-36, numbers as in the landed Lean):
  F4(z)      (1/2) [[1,1,1,1],[1,z,-1,-z],[1,-1,1,-1],[1,-z,-1,z]]           (scaled by 2 here)
  SIG        F4(z) ⊗ F4(w), z = (3+4i)/5, w = (5+12i)/13, index (a,b) -> 4a+b (scaled by 4: unimodular entries)
  W          [a even][c even]·([b = 1] + [d = 1]) on the entry ((a,b),(c,d))
  Pu(u)      SIG ∘ u^W; P = Pu(u60), u60 = (60+i)/(60-i) = (3599+120i)/3601; the second point Pu(u5), u5 = (3+4i)/5
"""
import itertools, json, sys, time
from fractions import Fraction as Fr
from math import gcd

# ---- exact Gaussian rationals -----------------------------------------------------------------
class G:
    __slots__ = ('a', 'b')
    def __init__(s, a, b=0): s.a = Fr(a); s.b = Fr(b)
    def __mul__(s, o): return G(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a)
    def __add__(s, o): return G(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return G(s.a - o.a, s.b - o.b)
    def __neg__(s): return G(-s.a, -s.b)
    def conj(s): return G(s.a, -s.b)
    def __eq__(s, o): return s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b))
    def norm2(s): return s.a * s.a + s.b * s.b
    def key(s): return (s.a, s.b)
ZERO, ONE, I_ = G(0), G(1), G(0, 1)
ROOTS = [ONE, I_, G(-1), -I_]

def F4(z):
    m = G(-1)
    return [[ONE, ONE, ONE, ONE], [ONE, z, m, -z], [ONE, m, ONE, m], [ONE, -z, m, z]]   # scaled by 2
def swap(a, b):
    p = list(range(4)); p[a], p[b] = p[b], p[a]; return tuple(p)
ID4 = (0, 1, 2, 3)
R = [(ID4, ID4), (ID4, swap(2, 3)), (ID4, swap(1, 2)), (swap(2, 3), ID4), (swap(2, 3), swap(2, 3)),
     (swap(2, 3), swap(1, 2)), (swap(1, 2), ID4), (swap(1, 2), swap(2, 3)), (swap(1, 2), swap(1, 2))]
def circle(r, z):
    pi, tau = R[r]; F = F4(z)
    return [[F[pi[i]][tau[j]] for j in range(4)] for i in range(4)]
def dita(X, Ys, D):
    return [[X[i // 4][j // 4] * D[j // 4][i % 4] * Ys[j // 4][i % 4][j % 4] for j in range(16)] for i in range(16)]   # scaled by 4
def unitD(): return [[ONE] * 4 for _ in range(4)]
def kron(X, Y): return dita(X, [Y] * 4, unitD())

def is_unitary16(H):
    """H scaled by 4: H H^* = 16 I."""
    for i in range(16):
        for j in range(16):
            s = ZERO
            for k in range(16): s = s + H[i][k] * H[j][k].conj()
            if s != (G(16) if i == j else ZERO): return False
    return True

# ---- exact rank and defect --------------------------------------------------------------------
def rank_int(rows):
    M = [r[:] for r in rows]; m = len(M); n = len(M[0]); r = 0
    for c in range(n):
        p = None
        for i in range(r, m):
            if M[i][c] != 0: p = i; break
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        piv = M[r][c]
        for i in range(r + 1, m):
            if M[i][c] != 0:
                f = M[i][c]
                M[i] = [piv * x - f * y for x, y in zip(M[i], M[r])]
                g = 0
                for x in M[i]:
                    if x: g = gcd(g, x)
                if g > 1: M[i] = [x // g for x in M[i]]
        r += 1
        if r == m: break
    return r
def defect_rows(H):
    n = 16; rows = []
    for i in range(n):
        for j in range(i + 1, n):
            re = [Fr(0)] * (n * n); im = [Fr(0)] * (n * n)
            for k in range(n):
                c = H[i][k] * H[j][k].conj()
                re[i * n + k] += c.a; re[j * n + k] -= c.a; im[i * n + k] += c.b; im[j * n + k] -= c.b
            for v in (re, im):
                den = 1
                for x in v: den = den * x.denominator // gcd(den, x.denominator)
                rows.append([int(x * den) for x in v])
    return rows
def defect(H):
    assert is_unitary16(H), 'defect of a non-unitary matrix is not defined here'
    return 256 - rank_int(defect_rows(H)) - 31
def gauge_rows():
    out = []
    for i in range(16):
        v = [0] * 256
        for k in range(16): v[i * 16 + k] = 1
        out.append(v)
        v = [0] * 256
        for k in range(16): v[k * 16 + i] = 1
        out.append(v)
    return out

# ---- exact invariants of fourth-root matrices -------------------------------------------------
def haagerup(H):
    s = set()
    for i, k in itertools.combinations(range(16), 2):
        for j, l in itertools.combinations(range(16), 2):
            s.add((H[i][j] * H[k][l] * (H[i][l] * H[k][j]).conj()).key())
    return frozenset(s)
def profile(H):
    """the four-row profile: for each 4-subset of rows the sorted triple of |sum_k H_ak conj(H_bk) H_ck conj(H_dk)|^2
    over the three ways of choosing which two rows are conjugated, as a multiset over the subsets
    (entries scaled by 4). Invariant under row and column permutations, phases and conjugation;
    the transpose gives the column profile, so the census invariant carries both."""
    vals = []
    for a, b, c, d in itertools.combinations(range(16), 4):
        trip = []
        for (p, q, r, t) in ((a, b, c, d), (a, c, b, d), (a, b, d, c)):
            s = ZERO
            for k in range(16): s = s + H[p][k] * H[q][k].conj() * H[r][k] * H[t][k].conj()
            trip.append(s.norm2())
        vals.append(tuple(sorted(trip)))
    return tuple(sorted(vals))
def profile2(H):
    """the transpose-symmetrized profile: the unordered pair of the row profile and the column profile."""
    HT = [[H[j][i] for j in range(16)] for i in range(16)]
    return tuple(sorted((profile(H), profile(HT))))
def pvalues(H):
    return set(x for trip in profile(H) for x in trip)
def relabel(H, pi, tau, cj=False, tr=False):
    Hh = [[H[pi[i]][tau[j]] for j in range(16)] for i in range(16)]
    if cj: Hh = [[x.conj() for x in row] for row in Hh]
    if tr: Hh = [[Hh[j][i] for j in range(16)] for i in range(16)]
    return Hh

fails = []
def check(name, got, want):
    ok = got == want
    print('  %s  %-70s %s' % ('PASS' if ok else 'FAIL', name, got if ok else '%s (expected %s)' % (got, want)))
    if not ok: fails.append(name)
t0 = time.time()
N16 = 16
PAIRS = [(i, j) for i in range(N16) for j in range(i + 1, N16)]
z = G(Fr(3, 5), Fr(4, 5)); w = G(Fr(5, 13), Fr(12, 13))
SIG = kron(F4(z), F4(w))
def gpow(u, k):
    r = ONE
    for _ in range(abs(k)): r = r * (u if k > 0 else u.conj())
    return r
U60 = G(Fr(3599, 3601), Fr(120, 3601))
W = [((1 if (i % 4) == 1 else 0) + (1 if (j % 4) == 1 else 0)) if ((i // 4) % 2 == 0 and (j // 4) % 2 == 0) else 0 for i in range(16) for j in range(16)]
P = [[SIG[i][j] * gpow(U60, W[i * 16 + j]) for j in range(16)] for i in range(16)]

def is_unitary_s(M, s):
    k = len(M)
    for i in range(k):
        for j in range(k):
            t = ZERO
            for l in range(k): t = t + M[i][l] * M[j][l].conj()
            if t != (G(s) if i == j else ZERO): return False
    return True
def ratio_table(H):
    """RT[i][s0][s] = the key of H[i][s] · conj(H[i][s0]): the 4096 products every subset's proportionality keys are
    drawn from, computed once per matrix instead of once per subset"""
    return [[[(H[i][s] * H[i][s0].conj()).key() for s in range(16)] for s0 in range(16)] for i in range(16)]
def prop_partition(RT, S):
    keys = {}
    for i in range(16):
        r = RT[i][S[0]]
        keys.setdefault(tuple(r[s] for s in S), []).append(i)
    return sorted(tuple(v) for v in keys.values())
def dita_orientations(H, m, n):
    good = {}; RT = ratio_table(H)
    for S in itertools.combinations(range(16), n):
        Pp = prop_partition(RT, S)
        if all(len(cl) == m for cl in Pp): good[S] = Pp
    parts = []
    def rec(rem, chosen):
        if not rem: parts.append(tuple(chosen)); return
        first = min(rem)
        for S in good:
            if first in S and set(S) <= rem: rec(rem - set(S), chosen + [S])
    rec(set(range(16)), [])
    out = []
    for cp in parts:
        cls = {i: tuple(next(ci for ci, cl in enumerate(good[S]) if i in cl) for S in cp) for i in range(16)}
        groups = {}
        for i in range(16): groups.setdefault(cls[i], []).append(i)
        rows = sorted(tuple(v) for v in groups.values())
        if not all(len(g) == m for g in rows): continue
        col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}
        row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
        lam = {}; Y = []
        for c in range(m):
            Yc = []
            for b in range(n):
                i0 = row[(0, b)]; base = [H[i0][col[(c, d)]] for d in range(n)]; Yc.append(base)
                for a in range(m): lam[(a, b, c)] = H[row[(a, b)]][col[(c, 0)]] * base[0].conj()
            Y.append(Yc)
        rank1 = all(lam[(a, b, c)] == lam[(a, 0, c)] * lam[(0, b, c)] for a in range(m) for b in range(n) for c in range(m))
        X = [[lam[(a, 0, c)] for c in range(m)] for a in range(m)]
        out.append((cp, rows, rank1 and is_unitary_s(X, m) and all(is_unitary_s(Yc, n) for Yc in Y), X, Y))
    return out
S4 = list(itertools.permutations(range(4)))
def deph(M):
    n = len(M); M = [[M[i][j] * M[i][0].conj() for j in range(n)] for i in range(n)]
    return [[M[i][j] * M[0][j].conj() for j in range(n)] for i in range(n)]
def key(M): return tuple(x.key() for r in M for x in r)
print("== 0. act 36's stabilizer of SIG in G_ext, replayed for the census ==")
X4, Y4 = F4(z), F4(w)
def relabel(M, pi, tau): return [[M[pi[i]][tau[j]] for j in range(4)] for i in range(4)]
def conj4(M): return [[x.conj() for x in r] for r in M]
def tr4(M): return [list(c) for c in zip(*M)]
kX, kY = key(deph(X4)), key(deph(Y4))
def stab_pairs(A, target): return [(pi, tau) for pi in S4 for tau in S4 if key(deph(relabel(A, pi, tau))) == target]
ops = {}
for sw in (0, 1):
    for cj in (0, 1):
        for tr in (0, 1):
            A, B = (Y4, X4) if sw else (X4, Y4)
            if cj: A, B = conj4(A), conj4(B)
            if tr: A, B = tr4(A), tr4(B)
            ops[(sw, cj, tr)] = (stab_pairs(A, kX), stab_pairs(B, kY))
check('factor stabilizer products without factor exchange and with it', ([len(a) * len(b) for k, (a, b) in ops.items() if k[0] == 0], [len(a) * len(b) for k, (a, b) in ops.items() if k[0] == 1]), ([256] * 4, [0] * 4))
order = sum(len(a) * len(b) for a, b in ops.values())
check('stabilizer order', order, 1024)
def action(op, g1, g2):
    sw, cj, tr = op; (p1, t1), (p2, t2) = g1, g2
    perm = [0] * 256; sign = -1 if cj else 1
    for i in range(16):
        for j in range(16):
            a, b, c, d = i // 4, i % 4, j // 4, j % 4
            if sw: a, b, c, d = b, a, d, c
            if tr: a, b, c, d = c, d, a, b
            i2 = 4 * p1.index(a) + p2.index(b); j2 = 4 * t1.index(c) + t2.index(d)
            perm[i * 16 + j] = i2 * 16 + j2
    return (tuple(perm), sign)
elems = [action(op, g1, g2) for op, (A, B) in ops.items() for g1 in A for g2 in B]
# ---- A37: the exact monomial calculus on the arc ---------------------------------------------
# Every entry of SIG is i^p z^q w^r, so every entry of H(u) = SIG o u^W is i^p z^q w^r u^k with k = W(i, j). A Dita
# structure (column blocks, row classes, and an alignment of the rows within row classes) is admitted at
# u iff finitely many monomial equations hold: the row
# proportionality on every block and the rank-one condition on the block ratios. Each equation u^k = i^p z^q w^r has,
# for k != 0, exactly |k| unit solutions u = zeta z^(-q/k) w^(-r/k), zeta a root of unity; z = (2+i)/(2-i) and
# w = (3+2i)/(3-2i) are multiplicatively independent modulo roots of unity (distinct Gaussian primes), so the triple
# (angle of zeta in turns mod 1, s, t) with u = zeta z^s w^t names a point exactly, and monomials at a point are
# compared exactly as such triples.
F4E = [[(0, 0), (0, 0), (0, 0), (0, 0)], [(0, 0), (0, 1), (2, 0), (2, 1)], [(0, 0), (2, 0), (0, 0), (2, 0)], [(0, 0), (2, 1), (2, 0), (0, 1)]]
SIGE = [[None] * 16 for _ in range(16)]
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                (p1, q), (p2, r) = F4E[a][c], F4E[b][d]
                SIGE[4 * a + b][4 * c + d] = ((p1 + p2) % 4, q, r)
def val(p, q, r):
    out = ONE
    for _ in range(p): out = out * I_
    for _ in range(q): out = out * z
    for _ in range(r): out = out * w
    return out
WE = [[W[i * 16 + j] for j in range(16)] for i in range(16)]
GEN_ONE = (0, 0, 0, 0)
def gen_entry(i, j): p, q, r = SIGE[i][j]; return (WE[i][j], p, q, r)
def gen_div(m1, m2): return (m1[0] - m2[0], (m1[1] - m2[1]) % 4, m1[2] - m2[2], m1[3] - m2[3])
def gen_mul(m1, m2): return (m1[0] + m2[0], (m1[1] + m2[1]) % 4, m1[2] + m2[2], m1[3] + m2[3])
def solutions(m):
    """the unit solutions of u^k i^p z^q w^r = 1 as canonical points, or 'all' / 'none'"""
    k, p, q, r = m
    if k == 0: return 'all' if (p % 4 == 0 and q == 0 and r == 0) else 'none'
    return frozenset(((Fr(-p, 4) + n_) / k % 1, Fr(-q, k), Fr(-r, k)) for n_ in range(abs(k)))
def at_point(m, pt):
    k, p, q, r = m; ang, s, t = pt
    return ((Fr(p, 4) + k * ang) % 1, q + k * s, r + k * t)
PT_ONE = (Fr(0), Fr(0), Fr(0))
def show_pt(pt): return 'zeta(%s) z^%s w^%s' % (pt[0], pt[1], pt[2])
def gaussian_value(pt):
    """the Gaussian-rational value of a canonical point, when it has one: integer s, t and an angle in quarter turns"""
    ang, s, t = pt
    if s.denominator != 1 or t.denominator != 1 or (ang * 4).denominator != 1: return None
    v = ONE
    for _ in range(int(ang * 4) % 4): v = v * I_
    zz = z if s >= 0 else z.conj(); ww = w if t >= 0 else w.conj()
    for _ in range(abs(int(s))): v = v * zz
    for _ in range(abs(int(t))): v = v * ww
    return v

def structures(ent, div, mul, is_one, m, n, ratio):
    """the Dita structure search (act 36's, section 2), exhaustive over column blocks and row classes and testing the
    rank-one condition at the sorted alignment, on a matrix of monomials: ent(i, j) the entry, ratio[i][s0][s]
    = ent(i, s) / ent(i, s0) precomputed, div/mul/is_one the monomial operations; returns (candidates, exact) as lists of
    (column blocks, row classes); unitarity of the factors is not tested here (it follows from that of H(u)) and is
    checked separately by the numeric control"""
    good = {}
    for S in itertools.combinations(range(16), n):
        keys = {}
        for i in range(16):
            r0 = ratio[i][S[0]]
            keys.setdefault(tuple(r0[s] for s in S), []).append(i)
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
        lam = {(a, b, c): div(ent(row[(a, b)], col[(c, 0)]), ent(row[(0, b)], col[(c, 0)])) for a in range(m) for b in range(n) for c in range(m)}
        if all(is_one(div(lam[(a, b, c)], mul(lam[(a, 0, c)], lam[(0, b, c)]))) for a in range(m) for b in range(n) for c in range(m)):
            exact.append((cp, rows))
    return cands, exact
def gen_search(m, n):
    ratio = [[[gen_div(gen_entry(i, s), gen_entry(i, s0)) for s in range(16)] for s0 in range(16)] for i in range(16)]
    return structures(gen_entry, gen_div, gen_mul, lambda x: x == GEN_ONE, m, n, ratio)
def point_search(pt, m, n):
    ent = [[at_point(gen_entry(i, j), pt) for j in range(16)] for i in range(16)]
    def div3(a, b): return ((a[0] - b[0]) % 1, a[1] - b[1], a[2] - b[2])
    def mul3(a, b): return ((a[0] + b[0]) % 1, a[1] + b[1], a[2] + b[2])
    ratio = [[[div3(ent[i][s], ent[i][s0]) for s in range(16)] for s0 in range(16)] for i in range(16)]
    return structures(lambda i, j: ent[i][j], div3, mul3, lambda x: x == PT_ONE, m, n, ratio)
SHAPES = ((4, 4), (8, 2), (2, 8))
FROZEN_BLOCKS = ((0, 1, 2, 3, 8, 9, 10, 11), (4, 5, 6, 7, 12, 13, 14, 15))
FROZEN_CLASSES = ((0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15))
def exact_set(res):
    """the exact structures of a search result over the three shapes, as a set of (shape, blocks, classes)"""
    return set((mn, cp, tuple(rows)) for mn, (cands, exact) in res.items() for cp, rows in exact)
FROZEN_ONLY = {((2, 8), FROZEN_BLOCKS, FROZEN_CLASSES)}

print('== 1. the census at the sorted alignment: the Diţă partition structures of the stratum point with the rows of each row class in sorted order, and their partition orbits under the stabilizer ==')
check('symbolic SIG equals the numeric SIG entrywise (i^p z^q w^r)', all(val(*SIGE[i][j]) == SIG[i][j] for i in range(16) for j in range(16)), True)
check('SIG is symmetric; W is symmetric', (SIG == [list(c) for c in zip(*SIG)], WE == [list(c) for c in zip(*WE)]), (True, True))
SIGT = [list(c) for c in zip(*SIG)]
def twist(H, cp, rows, X, Y, m, n):
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    D = [[None] * n for _ in range(m)]
    for c in range(m):
        for b in range(n):
            x = X[0][c] * Y[c][b][0]; h = H[row[(0, b)]][col[(c, 0)]]; nx = x.norm2(); q = h * x.conj(); D[c][b] = G(q.a / nx, q.b / nx)
    ok = all(H[row[(a, b)]][col[(c, d)]] == X[a][c] * D[c][b] * Y[c][b][d] for a in range(m) for b in range(n) for c in range(m) for d in range(n))
    return D, ok
facts = []
for (m, n) in SHAPES:
    for kind, H in (('column', SIG), ('row', SIGT)):
        for cp, rows, ok, X, Y in dita_orientations(H, m, n):
            if not ok: continue
            D, dok = twist(H, cp, rows, X, Y, m, n)
            facts.append((kind, (m, n), tuple(cp), tuple(rows), dok, all(x == ONE for r in D for x in r)))
check('exact partition structures of SIG at the sorted alignment by shape and form: 4x4, 8x2, 2x8, each column and row', tuple(sum(1 for f in facts if f[1] == mn and f[0] == k) for mn in SHAPES for k in ('column', 'row')), (4, 4, 2, 2, 3, 3))
check('every sorted-alignment partition structure reconstructs SIG exactly from its factors, with trivial twist', all(f[4] and f[5] for f in facts), True)
check('the column-form and row-form sorted-alignment partition structures coincide as index sets (SIG symmetric)', sorted((mn, cp, rows) for k, mn, cp, rows, _, _ in facts if k == 'column') == sorted((mn, cp, rows) for k, mn, cp, rows, _, _ in facts if k == 'row'), True)
def perm_pair(e):
    p, s_ = e
    rp = [p[i * 16] // 16 for i in range(16)]; cq = [p[j] % 16 for j in range(16)]
    if all(p[i * 16 + j] == rp[i] * 16 + cq[j] for i in range(16) for j in range(16)): return 'product', tuple(rp), tuple(cq)
    psi = [p[i * 16] % 16 for i in range(16)]; phi = [p[j] // 16 for j in range(16)]
    assert all(p[i * 16 + j] == phi[j] * 16 + psi[i] for i in range(16) for j in range(16))
    return 'transposed', tuple(psi), tuple(phi)
def canon(kind, mn, cp, rows):
    return (kind, mn, tuple(sorted(tuple(sorted(b)) for b in cp)), tuple(sorted(tuple(sorted(r)) for r in rows)))
def transport(kind, mn, cp, rows, e):
    """a structure carried through a stabilizer element: a product element sends entry (i, j) to (rp i, cq j), a transposed
    one to (phi j, psi i) and exchanges the column and row forms"""
    form, f1, f2 = perm_pair(e)
    if form == 'product':
        rp, cq = f1, f2
        if kind == 'column': return canon('column', mn, [[cq[j] for j in b] for b in cp], [[rp[i] for i in r] for r in rows])
        return canon('row', mn, [[rp[i] for i in b] for b in cp], [[cq[j] for j in r] for r in rows])
    psi, phi = f1, f2
    if kind == 'column': return canon('row', mn, [[phi[j] for j in b] for b in cp], [[psi[i] for i in r] for r in rows])
    return canon('column', mn, [[psi[i] for i in b] for b in cp], [[phi[j] for j in r] for r in rows])
keyset = {canon(k, mn, cp, rows): idx for idx, (k, mn, cp, rows, _, _) in enumerate(facts)}
orbits = []; seen = set()
for idx, (k, mn, cp, rows, _, _) in enumerate(facts):
    if idx in seen: continue
    orb = set(keyset[transport(k, mn, cp, rows, e)] for e in elems); seen |= orb; orbits.append(sorted(orb))
check('the stabilizer (order 1024, with transposition) permutes the 18 partition structures admitted at the sorted alignment; partition-orbit count and sizes', (len(orbits), sorted(len(o) for o in orbits)), (9, [2] * 9))
check('each partition orbit of the sorted-alignment restriction pairs a partition structure with its own transpose and identifies nothing else', all(len(set(facts[i][1:4] for i in o)) == 1 and set(facts[i][0] for i in o) == {'column', 'row'} for o in orbits), True)
fro = [i for i, f in enumerate(facts) if f[1] == (2, 8) and f[2] == FROZEN_BLOCKS and f[3] == FROZEN_CLASSES]
check('the frozen 2x8 class is one orbit: column and row forms of the frozen blocks and classes', sorted(fro) in orbits, True)
OTHERS = sorted(set((f[1], f[2], f[3]) for f in facts if f[0] == 'column' and not (f[1] == (2, 8) and f[2] == FROZEN_BLOCKS)), key=lambda x: (SHAPES.index(x[0]), x[1]))
check('the other partition orbits of the sorted-alignment restriction: four 4x4, two 8x2, two 2x8', [mn for mn, _, _ in OTHERS], [(4, 4)] * 4 + [(8, 2)] * 2 + [(2, 8)] * 2)
print('  (%.0fs)' % (time.time() - t0))

print('== 2. the arc: symmetric, and the frozen class persistent; the named point and the second point ==')
U5 = G(Fr(3, 5), Fr(4, 5))
def Pu(u): return [[SIG[i][j] * gpow(u, W[i * 16 + j]) for j in range(16)] for i in range(16)]
P5 = Pu(U5)
check('Pu(1) = SIG; P = Pu(u60); both P and Pu(u5) unitary and symmetric', (Pu(ONE) == SIG, Pu(U60) == P, is_unitary16(P), is_unitary16(P5), P == [list(c) for c in zip(*P)], P5 == [list(c) for c in zip(*P5)]), (True, True, True, True, True, True))
def numeric_exact(H):
    return {mn: [(tuple(cp), tuple(rows)) for cp, rows, ok, X, Y in dita_orientations(H, *mn) if ok] for mn in SHAPES}
NE_P, NE_P5 = numeric_exact(P), numeric_exact(P5)
check('at the sorted alignment P admits exactly the frozen 2x8 partition structure (column form; the row form is the same by symmetry)', NE_P, {(4, 4): [], (8, 2): [], (2, 8): [(FROZEN_BLOCKS, FROZEN_CLASSES)]})
check('at the sorted alignment Pu(u5) admits exactly the frozen 2x8 partition structure', NE_P5, {(4, 4): [], (8, 2): [], (2, 8): [(FROZEN_BLOCKS, FROZEN_CLASSES)]})
print('  (%.0fs)' % (time.time() - t0))

print('== 3. the generic arc point, and the obstruction monomial of each other named index map of the sorted-alignment census ==')
gen = {mn: gen_search(*mn) for mn in SHAPES}
check('partition structures at a generic u (u a free symbol): (candidates, exact at the sorted alignment) by shape', tuple((len(c), len(e)) for c, e in gen.values()), ((1, 0), (1, 0), (1, 1)))
check('the one exact generic partition structure at the sorted alignment is the frozen 2x8 partition structure', exact_set(gen), FROZEN_ONLY)
def conditions(m, n, cp, rows):
    """every monomial condition the structure imposes: (kind, positions, monomial); 'prop' rows (a,b),(0,b) on columns
    (c,d),(c,0); 'rank1' the rank-one identity at (a, b, c)"""
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    out = []
    for c in range(m):
        for b in range(n):
            for a in range(m):
                for d in range(1, n):
                    i, i2, j, j0 = row[(a, b)], row[(0, b)], col[(c, d)], col[(c, 0)]
                    out.append(('prop', (i, i2, j, j0), gen_div(gen_div(gen_entry(i, j), gen_entry(i2, j)), gen_div(gen_entry(i, j0), gen_entry(i2, j0)))))
    lam = {(a, b, c): gen_div(gen_entry(row[(a, b)], col[(c, 0)]), gen_entry(row[(0, b)], col[(c, 0)])) for a in range(m) for b in range(n) for c in range(m)}
    for a in range(m):
        for b in range(n):
            for c in range(m):
                out.append(('rank1', (a, b, c), gen_div(lam[(a, b, c)], gen_mul(lam[(a, 0, c)], lam[(0, b, c)]))))
    return out
obs = []
for mn, cp, rows in OTHERS:
    nonid = [x for x in conditions(mn[0], mn[1], cp, rows) if x[2] != GEN_ONE]
    obs.append((len(nonid), sorted(set(x[2][0] for x in nonid)), sorted(set(x[2][1:] for x in nonid))))
check('each of the eight other named index maps of the sorted-alignment census imposes non-identity conditions, all of the form u^k = 1 with k in {-1, 1}', all(nn > 0 and set(ks) <= {-1, 1} and cs == [(0, 0, 0)] for nn, ks, cs in obs), True)
check('their counts of non-identity conditions', [nn for nn, _, _ in obs], [20, 4, 36, 24, 40, 8, 20, 20])
check('the frozen class imposes no non-identity condition (persistence, replayed)', sum(1 for x in conditions(2, 8, FROZEN_BLOCKS, FROZEN_CLASSES) if x[2] != GEN_ONE), 0)
# the kernel's witness identities: four positions with H p1 H p2 = H p3 H p4 forced by the Dita form, all four SIG
# entries in {1, -1} and u-exponent sums {0, 1}
WIT = {"e1": {"coef": 16, "e": [1, 0], "kind": "prop", "p": [[0, 1], [4, 3], [0, 3], [4, 1]], "sign": 1}, "e2": {"coef": -16, "e": [0, 1], "kind": "rank1", "p": [[5, 0], [0, 0], [1, 0], [4, 0]], "sign": 1}, "k1": {"coef": -16, "e": [0, 1], "kind": "prop", "p": [[0, 0], [4, 1], [0, 1], [4, 0]], "sign": 1}, "k2": {"coef": -16, "e": [0, 1], "kind": "rank1", "p": [[3, 0], [0, 0], [2, 0], [1, 0]], "sign": 1}, "k3": {"coef": -16, "e": [0, 1], "kind": "prop", "p": [[0, 0], [6, 9], [0, 9], [6, 0]], "sign": 1}, "k4": {"coef": -16, "e": [0, 1], "kind": "prop", "p": [[0, 0], [1, 4], [0, 4], [1, 0]], "sign": 1}, "t2": {"coef": 16, "e": [1, 0], "kind": "prop", "p": [[1, 0], [3, 4], [1, 4], [3, 0]], "sign": 1}, "t3": {"coef": -16, "e": [0, 1], "kind": "rank1", "p": [[11, 0], [0, 0], [10, 0], [1, 0]], "sign": 1}}
def witness_ok(mn, cp, rows, wit):
    m, n = mn; col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    p1, p2, p3, p4 = [tuple(x) for x in wit['p']]
    # the identity is forced: same class/block pairing (prop) or the rank-one quadruple (rank1)
    rc = {v: k for k, v in row.items()}; cc = {v: k for k, v in col.items()}
    if wit['kind'] == 'prop':
        forced = rc[p1[0]][1] == rc[p2[0]][1] == rc[p3[0]][1] == rc[p4[0]][1] and cc[p1[1]][0] == cc[p2[1]][0] == cc[p3[1]][0] == cc[p4[1]][0] and p3 == (p1[0], p2[1]) and p4 == (p2[0], p1[1])
    else:
        (a, b), (a0, b0) = rc[p1[0]], rc[p2[0]]
        forced = a0 == 0 and b0 == 0 and rc[p3[0]] == (a, 0) and rc[p4[0]] == (0, b) and p1[1] == p2[1] == p3[1] == p4[1] and cc[p1[1]][1] == 0
    rational = all(SIGE[i][j][1] == 0 and SIGE[i][j][2] == 0 and SIGE[i][j][0] % 2 == 0 for i, j in (p1, p2, p3, p4))
    sgn = lambda i, j: 1 if SIGE[i][j][0] == 0 else -1
    e1 = WE[p1[0]][p1[1]] + WE[p2[0]][p2[1]]; e2 = WE[p3[0]][p3[1]] + WE[p4[0]][p4[1]]
    return forced and rational and sgn(*p1) * sgn(*p2) == sgn(*p3) * sgn(*p4) and {e1, e2} == {0, 1} and [e1, e2] == wit['e']
check('the kernel witness identity of each of the eight other named index maps is forced by its Diţă form, has rational entries and exponent sums {0, 1}', all(witness_ok(mn, cp, rows, WIT[nm]) for (mn, cp, rows), nm in zip(OTHERS, ('k1', 'k2', 'k3', 'k4', 'e1', 'e2', 't2', 't3'))), True)
print('  (%.0fs)' % (time.time() - t0))

print('== 4. the candidate exceptional set: every point where an extra proportionality, or the sorted-alignment rank-one condition of a generic candidate, appears ==')
def cond(i, i2, j, j0): return gen_div(gen_div(gen_entry(i, j), gen_entry(i2, j)), gen_div(gen_entry(i, j0), gen_entry(i2, j0)))
E_cand = {}
for n in (4, 2, 8):
    for B in itertools.combinations(range(16), n):
        j0 = B[0]
        for i, i2 in itertools.combinations(range(16), 2):
            sets = None; generic = True
            for j in B[1:]:
                s_ = solutions(cond(i, i2, j, j0))
                if s_ == 'all': continue
                generic = False
                if s_ == 'none': sets = frozenset(); break
                sets = s_ if sets is None else (sets & s_)
                if not sets: break
            if not generic and sets:
                for pt in sets: E_cand[pt] = E_cand.get(pt, 0) + 1
def rank1_points(m, n, cp, rows):
    pts = None
    for kind, idx, mm in conditions(m, n, cp, rows):
        if kind != 'rank1': continue
        s_ = solutions(mm)
        if s_ == 'all': continue
        if s_ == 'none': return frozenset()
        pts = s_ if pts is None else pts & s_
    return pts if pts is not None else 'all'
E_rank = set()
for mn, (cands, exact) in gen.items():
    for cp, rows in cands:
        if (cp, rows) in exact: continue
        pts = rank1_points(mn[0], mn[1], cp, rows)
        E_rank |= set(pts)
E_all = sorted(set(E_cand) | E_rank, key=lambda p: (p[1], p[2], p[0]))
check('the generic 4x4 and 8x2 candidates satisfy the rank-one condition at the sorted alignment at u = 1 only', E_rank, {PT_ONE})
EXPECTED_E = ["zeta(0) z^-1 w^-1", "zeta(1/2) z^-1 w^-1", "zeta(0) z^-1 w^0", "zeta(1/2) z^-1 w^0", "zeta(0) z^-1 w^1", "zeta(1/2) z^-1 w^1", "zeta(0) z^-1/2 w^-1/2", "zeta(1/4) z^-1/2 w^-1/2", "zeta(1/2) z^-1/2 w^-1/2", "zeta(3/4) z^-1/2 w^-1/2", "zeta(0) z^-1/2 w^0", "zeta(1/4) z^-1/2 w^0", "zeta(1/2) z^-1/2 w^0", "zeta(3/4) z^-1/2 w^0", "zeta(0) z^0 w^-1", "zeta(1/2) z^0 w^-1", "zeta(0) z^0 w^0", "zeta(1/2) z^0 w^0", "zeta(0) z^0 w^1", "zeta(1/2) z^0 w^1"]
check('the candidate exceptional set of the sorted-alignment calculus, exactly (twenty points)', [show_pt(p) for p in E_all], EXPECTED_E)
check('twelve of the candidates are Gaussian rational, eight are square roots outside Q(i)', sum(1 for p in E_all if gaussian_value(p) is not None), 12)
print('  (%.0fs)' % (time.time() - t0))

print('== 5. the search at the sorted alignment at every candidate point: the exceptional set at the sorted alignment ==')
sym = {}
for pt in E_all:
    sym[pt] = {mn: point_search(pt, *mn) for mn in SHAPES}
exact_E = [pt for pt in E_all if exact_set(sym[pt]) != FROZEN_ONLY]
check('at u = 1 the search at the sorted alignment returns eighteen partition structures: (candidates, exact) by shape', tuple((len(c), len(e)) for c, e in sym[PT_ONE].values()), ((5, 4), (3, 2), (3, 3)))
check('at u = -1 the proportionality candidates are those of u = 1, but at the sorted alignment only the frozen 2x8 partition structure is exact', (tuple((len(c), len(e)) for c, e in sym[(Fr(1, 2), Fr(0), Fr(0))].values()), exact_set(sym[(Fr(1, 2), Fr(0), Fr(0))]) == FROZEN_ONLY), (((5, 0), (3, 0), (3, 1)), True))
check('at every candidate point other than u = 1, exactly the frozen 2x8 partition structure is admitted at the sorted alignment', [show_pt(p) for p in exact_E], ['zeta(0) z^0 w^0'])
check('the exceptional set at the sorted alignment is {1}: outside the candidates the partition structure is the generic one, at the candidates the search decides', exact_E, [PT_ONE])
print('  (%.0fs)' % (time.time() - t0))

print('== 6. controls ==')
agree = []
for pt in E_all:
    uv = gaussian_value(pt)
    if uv is None: continue
    Hu = Pu(uv)
    if not is_unitary16(Hu): agree.append((show_pt(pt), 'not unitary')); continue
    num = {mn: (len(o), sum(1 for x in o if x[2])) for mn in SHAPES for o in [dita_orientations(Hu, *mn)]}
    if any(num[mn] != (len(sym[pt][mn][0]), len(sym[pt][mn][1])) for mn in SHAPES): agree.append((show_pt(pt), num))
check('the numeric search (with factor unitarity) agrees with the symbolic one at all twelve Gaussian-rational candidates, both at the sorted alignment', agree, [])
# genuine deformations: each of the eight other named index maps, with one twist phase moved off 1, gives a point of its hull off SIG
def hull_point(mn, cp, rows, phase):
    m, n = mn
    for f in facts:
        if f[0] == 'column' and f[1] == mn and f[2] == cp and f[3] == rows: break
    for cp_, rows_, ok, X, Y in dita_orientations(SIG, m, n):
        if ok and tuple(cp_) == cp and tuple(rows_) == rows: break
    D = [[ONE] * n for _ in range(m)]; D[m - 1][n - 1] = phase
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    H = [[None] * 16 for _ in range(16)]
    for a in range(m):
        for b in range(n):
            for c in range(m):
                for d in range(n): H[row[(a, b)]][col[(c, d)]] = X[a][c] * D[c][b] * Y[c][b][d]
    return H
deform = []
for mn, cp, rows in OTHERS:
    H = hull_point(mn, cp, rows, U5)
    found = [(tuple(cp_), tuple(rows_)) for cp_, rows_, ok, X, Y in dita_orientations(H, *mn) if ok]
    deform.append((is_unitary16(H), H != SIG, (cp, rows) in found))
check('a genuine deformation at each of the eight other named index maps (one twist phase u5): unitary, off SIG, and found by the search at the sorted alignment at its own partition structure', deform, [(True, True, True)] * 8)
check('the row-form search on P^T = P returns the column-form result (transpose invariance)', numeric_exact([list(c) for c in zip(*P)]) == NE_P, True)
# equivalence invariance: transport P by three stabilizer elements and compare the search with the transported structure
def apply_matrix(e, H):
    p, s_ = e; out = [[None] * 16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            i2, j2 = divmod(p[i * 16 + j], 16); out[i2][j2] = H[i][j] if s_ == 1 else H[i][j].conj()
    return out
picks = [elems[k] for k in (1, len(elems) // 3, len(elems) - 1)]
equiv = []
for e in picks:
    HP = apply_matrix(e, P); found = numeric_exact(HP)
    want = transport('column', (2, 8), FROZEN_BLOCKS, FROZEN_CLASSES, e)
    got = set(canon('column', mn, cp, rows) for mn, lst in found.items() for cp, rows in lst)
    # a transposed element sends the column form to the row form of the image, whose column-form search sees the same index sets
    equiv.append((len(got), canon('column', want[1], want[2], want[3]) in got))
check('the membership classifier commutes with three stabilizer elements (product, transposed, conjugating): the transported frozen 2x8 partition structure is the one found at the sorted alignment', equiv, [(1, True)] * 3)
# a deliberately perturbed index map: the frozen blocks with one column moved between blocks are not admitted at generic u nor at P
pb = ((0, 1, 2, 3, 8, 9, 10, 12), (4, 5, 6, 7, 11, 13, 14, 15))
def admitted_generic(m, n, cp, rows): return all(x[2] == GEN_ONE for x in conditions(m, n, cp, rows))
check('a perturbed index map (columns 11 and 12 exchanged between the frozen blocks) is admitted neither at generic u nor at P', (admitted_generic(2, 8, pb, FROZEN_CLASSES), (pb, FROZEN_CLASSES) in NE_P[(2, 8)]), (False, False))
check('the frozen index maps themselves are admitted at generic u (control of the control)', admitted_generic(2, 8, FROZEN_BLOCKS, FROZEN_CLASSES), True)
print('  (%.0fs)' % (time.time() - t0))

print()
if fails:
    print('dita_arc_exclusivity_probe: FAILED (%d): %s' % (len(fails), fails)); sys.exit(1)
print('dita_arc_exclusivity_probe: OK -- at the certified stratum point SIG, with the rows of each row class in sorted order, the eighteen Diţă partition structures found form nine partition orbits under the stabilizer with transposition; along the symmetric arc Pu(u) = SIG∘u^W the frozen 2x8 partition structure persists identically, each of the eight other named index maps is admitted only where u = 1, the candidate exceptional set of the sorted-alignment monomial calculus has twenty points, and the search at the sorted alignment at each of them finds only the frozen 2x8 partition structure away from u = 1: the exceptional set at the sorted alignment is {1}')
