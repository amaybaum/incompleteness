"""Track B act 41 -- the independent computation of the index-map round (frozen with the control plane).

At each of the round's forty-two named test cases: act 36's exhaustive partition search on the exact matrix, then every
alignment of every partition structure counted by a matching search of its own, strictly with factor unitarity and up
to diagonal equivalence. It uses neither act 40's flat calculus nor its candidate enumeration, and imports nothing from
the round's production probe. Its first part is act 38's probe head, verbatim, as act 40 carried it, with act 40's
family and exact points. It prints its measurements as one canonical JSON object and replays them against the round's
measurements.json when that file is present; the measured values are not pass conditions.
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
# structure (column blocks, row classes) is admitted at u iff finitely many monomial equations hold: the row
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
    """the exhaustive Dita structure search (act 36's, section 2) on a matrix of monomials: ent(i, j) the entry, ratio[i][s0][s]
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

# ---- A38: the witness exponent matrix and its arc ---------------------------------------------
# The exponent matrix E = A + B + C on the entry ((a,b),(c,d)), rows i = 4a+b and columns j = 4c+d:
#   A = [a odd][b = 3][c odd],  B = [a = 2][d = 1],  C = [a+b odd][(c,d) in {(0,2),(2,0)}]
# and the arc H(u) = SIG o u^E. Every entry of H(u) is i^p z^q w^r u^k with k = E(i, j) in {0, 1}; the monomial calculus
# of act 37 applies verbatim with E in place of W.
def EA(i, j): a, b, c, d = i // 4, i % 4, j // 4, j % 4; return 1 if (a % 2 == 1 and b == 3 and c % 2 == 1) else 0
def EB(i, j): a, b, c, d = i // 4, i % 4, j // 4, j % 4; return 1 if (a == 2 and d == 1) else 0
def EC(i, j): a, b, c, d = i // 4, i % 4, j // 4, j % 4; return 1 if ((a + b) % 2 == 1 and (c, d) in ((0, 2), (2, 0))) else 0
EE = [[EA(i, j) + EB(i, j) + EC(i, j) for j in range(16)] for i in range(16)]
EW = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]]
ET = [list(c) for c in zip(*EE)]
SIGT = [list(c) for c in zip(*SIG)]
def Hu(u, E=EE): return [[SIG[i][j] * gpow(u, E[i][j]) for j in range(16)] for i in range(16)]
def ent_of(E):
    def ent(i, j): p, q, r = SIGE[i][j]; return (E[i][j], p, q, r)
    return ent
def gen_search_E(E, m, n):
    ent = ent_of(E)
    ratio = [[[gen_div(ent(i, s), ent(i, s0)) for s in range(16)] for s0 in range(16)] for i in range(16)]
    return structures(ent, gen_div, gen_mul, lambda x: x == GEN_ONE, m, n, ratio)
def point_search_E(E, pt, m, n):
    ent0 = ent_of(E)
    ent = [[at_point(ent0(i, j), pt) for j in range(16)] for i in range(16)]
    def div3(a, b): return ((a[0] - b[0]) % 1, a[1] - b[1], a[2] - b[2])
    def mul3(a, b): return ((a[0] + b[0]) % 1, a[1] + b[1], a[2] + b[2])
    return structures(lambda i, j: ent[i][j], div3, mul3, lambda x: x == PT_ONE, m, n, ratio=[[[div3(ent[i][s], ent[i][s0]) for s in range(16)] for s0 in range(16)] for i in range(16)]), ent
def relaxed_at_point(ent, m, n, cp, rows):
    """the diagonal-equivalence form of a proportionality candidate at a point: lambda(a,b,c)/lambda(a,0,c) independent of c"""
    def div3(a, b): return ((a[0] - b[0]) % 1, a[1] - b[1], a[2] - b[2])
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    lam = {(a, b, c): div3(ent[row[(a, b)]][col[(c, 0)]], ent[row[(0, b)]][col[(c, 0)]]) for a in range(m) for b in range(n) for c in range(m)}
    return all(div3(lam[(a, b, c)], lam[(a, 0, c)]) == div3(lam[(a, b, 0)], lam[(a, 0, 0)]) for a in range(m) for b in range(n) for c in range(m))
def level_sets(v):
    out = {}
    for k, x in enumerate(v): out.setdefault(x, []).append(k)
    return out



PA = [[EA(i, j) for j in range(16)] for i in range(16)]
PB = [[EB(i, j) for j in range(16)] for i in range(16)]
PC = [[EC(i, j) for j in range(16)] for i in range(16)]
def H3(u1, u2, u3): return [[SIG[i][j] * gp(u1, PA[i][j]) * gp(u2, PB[i][j]) * gp(u3, PC[i][j]) for j in range(16)] for i in range(16)]
def gp(u, k):
    out = ONE
    for _ in range(k): out = out * u
    return out
TESTU = [G(Fr(3, 5), Fr(4, 5)), G(Fr(8, 17), Fr(15, 17)), G(Fr(20, 29), Fr(21, 29)), I_, G(Fr(7, 25), Fr(24, 25))]
PTS = [('generic', (TESTU[0], TESTU[1], TESTU[2])), ('generic', (TESTU[4], I_, TESTU[0])), ('u1 = 1', (ONE, TESTU[0], TESTU[1])),
       ('u1 = -1', (G(-1), TESTU[0], TESTU[1])), ('u2 = 1', (TESTU[0], ONE, TESTU[1])), ('u2 = -1, absent', (TESTU[0], G(-1), TESTU[1])),
       ('u3 = 1', (TESTU[0], TESTU[1], ONE)), ('u3 = -1', (TESTU[0], TESTU[1], G(-1))), ('u1 = i, absent', (I_, TESTU[0], TESTU[1])),
       ('(1, u, -1)', (ONE, TESTU[2], G(-1))), ('(u, 1, 1)', (TESTU[2], ONE, ONE)), ('(-1, 1, u)', (G(-1), ONE, TESTU[4])),
       ('(1, 1, 1)', (ONE, ONE, ONE)), ('(-1, -1, -1)', (G(-1), G(-1), G(-1))), ('(-1, 1, 1)', (G(-1), ONE, ONE)),
       ('(1, 1, -1)', (ONE, ONE, G(-1))), ('(1, -1, 1)', (ONE, G(-1), ONE))]

# ---- A41: the forty-two named test cases (role, matrix); the definition of H is shared, nothing else --------------
import hashlib, os
A41_RECORD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'programmes', 'oi-qm', 'track-b', 'act-41-index-map-semantics', 'measurements.json')
def a41_Pu(u): return [[SIG[i][j] * gpow(u, W[i * 16 + j]) for j in range(16)] for i in range(16)]
def a41_gval_pt(ang, s, t):
    v = ONE
    for _ in range(int(ang * 4) % 4): v = v * I_
    for _ in range(abs(s)): v = v * (z if s > 0 else z.conj())
    for _ in range(abs(t)): v = v * (w if t > 0 else w.conj())
    return v
A41_U60 = G(Fr(3599, 3601), Fr(120, 3601)); A41_U5 = G(Fr(3, 5), Fr(4, 5))
A41_ACT38_PTS = [(Fr(0), -1, -1), (Fr(1, 2), -1, -1), (Fr(0), -1, 0), (Fr(1, 2), -1, 0), (Fr(0), -1, 1), (Fr(1, 2), -1, 1), (Fr(0), 0, -1),
                 (Fr(1, 2), 0, -1), (Fr(0), 0, 0), (Fr(1, 4), 0, 0), (Fr(1, 2), 0, 0), (Fr(3, 4), 0, 0), (Fr(0), 0, 1), (Fr(1, 2), 0, 1),
                 (Fr(0), 1, -1), (Fr(1, 2), 1, -1), (Fr(0), 1, 0), (Fr(1, 2), 1, 0), (Fr(0), 1, 1), (Fr(1, 2), 1, 1)]
# each case: (role, family, parameter); family 'H3' (u1, u2, u3), 'Pu' (act 36's arc, u), 'Hu' (act 38's arc, u)
A41_CASES = [('SIG', 'H3', (ONE, ONE, ONE)), ('Pu(-1)', 'Pu', G(-1)), ('P = Pu(u60)', 'Pu', A41_U60), ('Pu(u5)', 'Pu', A41_U5), ('Hu(-1)', 'Hu', G(-1))]
A41_CASES += [('act40 %02d %s' % (i, nm), 'H3', u) for i, (nm, u) in enumerate(PTS)]
A41_CASES += [('act38 zeta(%s) z^%d w^%d' % (a, s, t), 'Hu', a41_gval_pt(a, s, t)) for a, s, t in A41_ACT38_PTS]
def a41_matrix(fam, par):
    if fam == 'H3': return H3(*par)
    if fam == 'Pu': return a41_Pu(par)
    return H3(par, par, par)
def a41_key(H): return tuple(x.key() for r in H for x in r)
print('== A41-I1. the named test cases, and their coincidences ==')
A41_MATS = [(role, a41_matrix(fam, par)) for role, fam, par in A41_CASES]
a41_groups = {}
for role, H in A41_MATS: a41_groups.setdefault(a41_key(H), []).append(role)
A41_COINCIDE = sorted(sorted(v) for v in a41_groups.values() if len(v) > 1)
print('  %d named test cases, %d distinct matrices' % (len(A41_MATS), len(a41_groups)))

print('== A41-I2. the independent computation: act 36\'s partition search, then every alignment by matching ==')
def a41_matchings(allowed):
    m = len(allowed); cnt = 0
    def rec(a, used):
        nonlocal cnt
        if a == m: cnt += 1; return
        for r in allowed[a]:
            if r not in used: used.add(r); rec(a + 1, used); used.discard(r)
    rec(0, set()); return cnt
def a41_valid_alignments(H, m, n, cp, rows, relaxed):
    col0 = [cp[c][0] for c in range(m)]
    lam0 = [[H[rows[0][a]][col0[c]] * H[rows[0][0]][col0[c]].conj() for c in range(m)] for a in range(m)]
    if not relaxed and not is_unitary_s(lam0, m): return 0
    per_b = []
    for b in range(1, n):
        d = {}
        for r0 in rows[b]:
            allowed = [[r0]]
            for a in range(1, m):
                ok = []
                for r in rows[b]:
                    lb = [H[r][col0[c]] * H[r0][col0[c]].conj() for c in range(m)]
                    good = all(lb[c] == lam0[a][c] for c in range(m)) if not relaxed else all(lb[c] * lam0[a][0] == lam0[a][c] * lb[0] for c in range(1, m))
                    if good: ok.append(r)
                allowed.append(ok)
            k = a41_matchings(allowed)
            if k: d[r0] = k
        per_b.append(d)
    if any(not d for d in per_b): return 0
    total = 0
    for combo in itertools.product(*[sorted(d) for d in per_b]):
        refs = [rows[0][0]] + list(combo)
        if not relaxed and not all(is_unitary_s([[H[r][cp[c][dd]] for dd in range(n)] for r in refs], n) for c in range(m)): continue
        k = 1
        for b, r0 in enumerate(combo): k *= per_b[b][r0]
        total += k
    return total
def a41_census(H):
    out = {}; HT = [list(c) for c in zip(*H)]
    for relaxed in (False, True):
        res = []
        for form, M in (('column', H), ('row', HT)):
            for (m, n) in ((4, 4), (8, 2), (2, 8)):
                for cp, rws, ok, _, _ in dita_orientations(M, m, n):
                    k = a41_valid_alignments(M, m, n, cp, rws, relaxed)
                    if k: res.append([form, [m, n], sorted(map(sorted, cp)), sorted(map(sorted, rws)), k])
        out['relaxed' if relaxed else 'strict'] = sorted(res)
    return out
A41_RES = {}; a41_done = {}
for role, H in A41_MATS:
    k = a41_key(H)
    if k not in a41_done: a41_done[k] = a41_census(H)
    A41_RES[role] = a41_done[k]
    r = A41_RES[role]
    print('  %-34s strict %2d (alignments %4d)  relaxed %2d (alignments %4d)' % (role, len(r['strict']), sum(x[4] for x in r['strict']), len(r['relaxed']), sum(x[4] for x in r['relaxed'])))
# control: the census at a coinciding case computed afresh equals the shared one
a41_recheck = all(a41_census(dict(A41_MATS)[g[1]]) == A41_RES[g[0]] for g in A41_COINCIDE)
check('control: at every coincidence of named test cases, a fresh computation at the second role equals the first', a41_recheck, True)
# control: at the sorted alignment alone this path reproduces act 40's sorted counts at its seventeen points
a41_sorted17 = []
for i, (nm, u) in enumerate(PTS):
    H = H3(*u); HT = [list(c) for c in zip(*H)]; n_ = 0
    for form, M in (('column', H), ('row', HT)):
        for mn in ((4, 4), (8, 2), (2, 8)): n_ += sum(1 for o in dita_orientations(M, *mn) if o[2])
    a41_sorted17.append(n_)
check('the sorted control: act 36\'s search at the sorted alignment reproduces act 40\'s seventeen recorded counts', a41_sorted17, [0, 0, 1, 1, 2, 0, 1, 1, 0, 3, 7, 4, 18, 2, 12, 12, 4])
print('  (%.0fs)' % (time.time() - t0))
A41_OBJ = {'cases': A41_RES, 'coincidences': A41_COINCIDE, 'distinct_matrices': len(a41_groups), 'n_cases': len(A41_MATS)}
A41_JSON = json.dumps(A41_OBJ, sort_keys=True, separators=(',', ':'))
print('A41-MEASUREMENTS independent ' + A41_JSON)
print('A41-SHA256 independent ' + hashlib.sha256(A41_JSON.encode()).hexdigest())
a41_mode = 'MEASURED'
if os.path.exists(A41_RECORD):
    rec = json.load(open(A41_RECORD, encoding='utf-8'))
    check('replay: the measurement equals the committed measurements.json, elementwise', json.loads(A41_JSON) == rec.get('independent'), True)
    a41_mode = 'REPLAYED'
print()
if fails:
    print('dita_index_map_independent: FAILED (%d): %s' % (len(fails), fails)); sys.exit(1)
print('dita_index_map_independent: OK -- %s: %d named test cases, %d distinct matrices' % (a41_mode, len(A41_MATS), len(a41_groups)))
