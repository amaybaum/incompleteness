"""Track B act 39 -- the exact-computation probe of the three-parameter realizability round (frozen with the control plane).

Everything asserted is exact arithmetic: Gaussian rationals in Python integers and fractions, and, for the symbolic form of the
identity, integer counts of the monomials z^q w^r. The probe asserts the preregistered values and exits 1 on any mismatch; it
certifies nothing on its own beyond the arithmetic it replays. Its first part is act 38's probe head, verbatim: act 36's
objects and structure search (exhaustive over column blocks and row classes, each partition structure tested at the
sorted alignment), act 36's stabilizer, act 37's monomial calculus, and act 38's pieces A, B, C and E.

Objects (acts 24-39, numbers as in the landed Lean):
  SIG        F4(z) ⊗ F4(w), z = (3+4i)/5, w = (5+12i)/13, index (a,b) -> 4a+b (scaled by 4: unimodular entries)
  A, B, C    [a odd][b = 3][c odd], [a = 2][d = 1], [a+b odd][(c,d) in {(0,2),(2,0)}] on the entry ((a,b),(c,d))
  H3         SIG o u1^A u2^B u3^C, the three-parameter family; its diagonal is act 38's arc SIG o u^(A+B+C)
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


# ---- A39: the three-parameter family H3(u1, u2, u3) = SIG o u1^A u2^B u3^C ------------------------------------------
# A, B, C are act 38's three pieces (EA, EB, EC above); H3 is a flat unitary on the whole torus iff, for every ordered row
# pair (r, s), the columns grouped by the joint difference triple (A_rj - A_sj, B_rj - B_sj, C_rj - C_sj) have pair sums
# sum SIG_rj conj(SIG_sj) equal to 16 [r = s] on the zero triple and 0 on every other triple.
PA = [[EA(i, j) for j in range(16)] for i in range(16)]
PB = [[EB(i, j) for j in range(16)] for i in range(16)]
PC = [[EC(i, j) for j in range(16)] for i in range(16)]
def madd(*Ms): return [[sum(M[i][j] for M in Ms) for j in range(16)] for i in range(16)]
def gp(u, k):
    out = ONE
    for _ in range(k): out = out * u
    return out
def H3(u1, u2, u3): return [[SIG[i][j] * gp(u1, PA[i][j]) * gp(u2, PB[i][j]) * gp(u3, PC[i][j]) for j in range(16)] for i in range(16)]
def Hu(u): return [[SIG[i][j] * gp(u, EE[i][j]) for j in range(16)] for i in range(16)]
def joint_gate(mats, symbolic):
    """(joint level sets checked, failures) for the multivariate identity of SIG o prod u_k^{M_k}"""
    n = 0; bad = []
    for r in range(16):
        for s in range(16):
            groups = {}
            for j in range(16):
                groups.setdefault(tuple(M[r][j] - M[s][j] for M in mats), []).append(j)
            for t, js in groups.items():
                n += 1
                zero = r == s and not any(t)
                if symbolic:
                    cnt = {}
                    for j in js:
                        a1, q1, r1 = SIGE[r][j]; a2, q2, r2 = SIGE[s][j]
                        cnt[(q1 - q2, r1 - r2)] = cnt.get((q1 - q2, r1 - r2), 0) + (1 if (a1 - a2) % 4 == 0 else -1)
                    got = {k: v for k, v in cnt.items() if v}
                    if got != ({(0, 0): 16} if zero else {}): bad.append((r, s, t))
                else:
                    tot = ZERO
                    for j in js: tot = tot + SIG[r][j] * SIG[s][j].conj()
                    if tot != (G(16) if zero else ZERO): bad.append((r, s, t))
    return n, bad

print('== 1. the three pieces ==')
check("A + B + C is act 38's exponent matrix E; the pieces take values in {0, 1} and are disjoint", (madd(PA, PB, PC) == EE, all(PA[i][j] + PB[i][j] + PC[i][j] <= 1 and min(PA[i][j], PB[i][j], PC[i][j]) >= 0 for i in range(16) for j in range(16))), (True, True))
supp = lambda M: (sorted(i for i in range(16) if any(M[i])), sorted(j for j in range(16) if any(M[i][j] for i in range(16))), sum(map(sum, M)))
check('rows, columns and support of A, B and C', (supp(PA), supp(PB), supp(PC)), (([7, 15], [4, 5, 6, 7, 12, 13, 14, 15], 16), ([8, 9, 10, 11], [1, 5, 9, 13], 16), ([1, 3, 4, 6, 9, 11, 12, 14], [2, 8], 16)))
TRIPLES = sorted(set(tuple(M[r][j] - M[s][j] for M in (PA, PB, PC)) for r in range(16) for s in range(16) for j in range(16)))
check('the joint difference triples occurring over all ordered row pairs', TRIPLES, [(-1, 0, 0), (-1, 1, 0), (0, -1, 0), (0, 0, -1), (0, 0, 0), (0, 0, 1), (0, 1, 0), (1, -1, 0), (1, 0, 0)])
print('  (%.0fs)' % (time.time() - t0))

print('== 2. realizability on the three-torus: the joint level-set identity ==')
n3, b3 = joint_gate([PA, PB, PC], False)
check('exact Gaussian rationals: joint level sets over the 256 ordered row pairs, and failures', (n3, len(b3)), (552, 0))
n3s, b3s = joint_gate([PA, PB, PC], True)
check('monomial by monomial in z and w, symbolic units (the form of the kernel proof): joint level sets, and failures', (n3s, len(b3s)), (552, 0))
print('  (%.0fs)' % (time.time() - t0))

print('== 3. controls ==')
check('the family passes through the stratum point: H3(1, 1, 1) = SIG', H3(ONE, ONE, ONE) == SIG, True)
U5 = G(Fr(3, 5), Fr(4, 5)); U17 = G(Fr(8, 17), Fr(15, 17)); MINUS = G(-1)
check("its diagonal is act 38's arc: H3(u, u, u) = SIG o u^E at u = u5, u60, -1 and i", [H3(u, u, u) == Hu(u) for u in (U5, U60, MINUS, I_)], [True] * 4)
TRIPS = [(U5, w, U17), (I_, MINUS, U60), (z, w.conj(), z.conj()), (U17, U5, I_)]
check('H3 is exactly unitary at four Gaussian-rational points of the torus off the diagonal', [is_unitary16(H3(*t)) for t in TRIPS], [True] * 4)
check('and is not unitary at a non-unit parameter (u1 = 2): the unit hypothesis is used', is_unitary16(H3(G(2), ONE, ONE)), False)
subs = [('E, one variable', [EE]), ('A', [PA]), ('B', [PB]), ('C', [PC]), ('(A, B)', [PA, PB]), ('(A, C)', [PA, PC]), ('(B, C)', [PB, PC]), ('(A + B, C)', [madd(PA, PB), PC])]
res = [(nm,) + joint_gate(ms, False)[:1] + (len(joint_gate(ms, False)[1]),) for nm, ms in subs]
check('the subfamilies, each in its own variables: joint level sets and failures', [(nm, k, f) for nm, k, f in res], [('E, one variable', 512, 0), ('A', 312, 0), ('B', 352, 0), ('C', 384, 0), ('(A, B)', 424, 0), ('(A, C)', 440, 0), ('(B, C)', 480, 0), ('(A + B, C)', 536, 0)])
Cp = [r[:] for r in PC]; Cp[1][2] = 1 - Cp[1][2]
check('a countercontrol: one entry of C flipped, the joint identity fails (failures) and H3 is not unitary at (u5, w, (8+15i)/17)', (len(joint_gate([PA, PB, Cp], False)[1]), is_unitary16([[SIG[i][j] * gp(U5, PA[i][j]) * gp(w, PB[i][j]) * gp(U17, Cp[i][j]) for j in range(16)] for i in range(16)])), (60, False))
# the joint test is strictly stronger than the line tests: on the diagonal x = y = z the triples (1, -1, 0) and (0, 0, 0)
# project to the same integer, so the one-variable identity alone does not see their separate cancellation
merged = sorted(set(t for t in TRIPLES if sum(t) == 0 and any(t)))
check('the joint triples the diagonal projection merges with the zero triple (a line test cannot separate them)', merged, [(-1, 1, 0), (1, -1, 0)])
mset = []
for r in range(16):
    for s_ in range(16):
        for t in merged:
            js = [j for j in range(16) if (PA[r][j] - PA[s_][j], PB[r][j] - PB[s_][j], PC[r][j] - PC[s_][j]) == t]
            if js:
                tot = ZERO
                for j in js: tot = tot + SIG[r][j] * SIG[s_][j].conj()
                mset.append((r, s_, t, len(js), tot == ZERO))
check('each merged joint level set cancels on its own: their number, their column counts, and whether every one sums to zero', (len(mset), sorted(set(x[3] for x in mset)), all(x[4] for x in mset)), (16, [2], True))
print('  (%.0fs)' % (time.time() - t0))

print()
if fails:
    print('dita_torus_probe: FAILED (%d): %s' % (len(fails), fails)); sys.exit(1)
print('dita_torus_probe: OK -- the three-parameter family SIG o u1^A u2^B u3^C through the certified stratum point, A, B, C '
      "act 38's three pieces: every joint level set of every ordered row pair cancels exactly, 552 of them, and monomial by monomial "
      'in z and w, so the family is a complex Hadamard matrix on the whole three-torus; it passes through SIG at (1, 1, 1) and its '
      "diagonal is act 38's arc")
