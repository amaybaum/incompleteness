"""Track B act 41 -- the production computation of the index-map round (frozen with the control plane).

Act 40's partition candidates and exact calculus of flats, with every alignment of every partition structure: each
rank-one condition involves one row class and the reference row class, so the alignments are searched row class by row
class, label by label, pruned on the flats. For act 36's arc, act 38's arc and act 39's family it measures loci as unions
over alignments, and at the stratum point the realizing triples, factorization classes and partition orbits under the
frozen action of act 36's stabilizer, with a Burnside cross-check. Its first part is act 40's probe head, verbatim,
through act 40's section 2. It prints its measurements as one canonical JSON object and replays them against the round's
measurements.json when that file is present. Its controls are the sorted-alignment regression values and the checks named
in each section; the measured values are not pass conditions. It imports nothing from the round's independent probe.
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


# ---- A40: the Dita locus of H3(u1, u2, u3) = SIG o u1^A u2^B u3^C in the three-torus --------------------------------
# Entry (i, j) of 4 H3 is the monomial u^k i^p z^q w^r, k = (A, B, C)[i][j], (p, q, r) = SIGE[i][j]. Every condition a Dita
# structure imposes (proportionality within a class on a block, rank one of the block ratios) is a character equation
# u^k = c with k in Z^3 and c in G = <i, z, w> = Z/4 x Z^2 (z, w independent modulo roots of unity), written additively.

# ---- the flat calculus, embedded (no imported helper) -----------------------------------------------------------------
def vadd(a, b): return ((a[0] + b[0]) % 4, a[1] + b[1], a[2] + b[2])
def vsub(a, b): return ((a[0] - b[0]) % 4, a[1] - b[1], a[2] - b[2])
def vmul(n, a): return ((n * a[0]) % 4, n * a[1], n * a[2])
V0 = (0, 0, 0)
class Empty(Exception):
    pass
def _hnf(rows):
    """the canonical row Hermite normal form (positive pivots, entries above pivots reduced) of the system {u^k = v}, values
    carried along; raises Empty on an inconsistent system (a zero character with a nonzero value)"""
    R = [[list(k), v] for k, v in rows]
    basis = []
    for col in range(3):
        while True:
            idx = [t for t in range(len(R)) if R[t][0][col] != 0]
            if len(idx) <= 1: break
            idx.sort(key=lambda t: abs(R[t][0][col]))
            pk, pv = R[idx[0]]
            for t in idx[1:]:
                f = R[t][0][col] // pk[col]
                R[t] = [[a - f * b for a, b in zip(R[t][0], pk)], vsub(R[t][1], vmul(f, pv))]
        idx = [t for t in range(len(R)) if R[t][0][col] != 0]
        if idx:
            k, v = R.pop(idx[0])
            if k[col] < 0: k = [-a for a in k]; v = vmul(-1, v)
            basis.append([k, v])
    for k, v in R:
        if any(k): raise AssertionError('reduction incomplete')
        if v != V0: raise Empty()
    piv = [next(c for c in range(3) if k[c] != 0) for k, v in basis]
    for a in range(len(basis)):
        pc = piv[a]; h = basis[a][0][pc]
        for b in range(a):
            f = basis[b][0][pc] // h
            if f:
                basis[b] = [[x - f * y for x, y in zip(basis[b][0], basis[a][0])], vsub(basis[b][1], vmul(f, basis[a][1]))]
    return tuple((tuple(k), v) for k, v in basis)
class Flat:
    """the solution set in T^3 of a finite consistent character system, stored canonically"""
    __slots__ = ('B',)
    def __init__(self, rows=()): self.B = _hnf(list(rows))
    @staticmethod
    def of(B):
        f = Flat.__new__(Flat); f.B = B; return f
    def __eq__(self, o): return isinstance(o, Flat) and self.B == o.B
    def __hash__(self): return hash(self.B)
    def rank(self): return len(self.B)
    def dim(self): return 3 - len(self.B)
    def meet(self, other): return Flat.of(_hnf(list(self.B) + list(other.B)))
    def add(self, k, v): return Flat.of(_hnf(list(self.B) + [(tuple(k), v)]))
    def reduce(self, k, v):
        k = list(k)
        for bk, bv in self.B:
            pc = next(c for c in range(3) if bk[c] != 0)
            f = k[pc] // bk[pc]
            if f: k = [a - f * b for a, b in zip(k, bk)]; v = vsub(v, vmul(f, bv))
        return (tuple(k), v)
    def holds(self, k, v):
        rk, rv = self.reduce(k, v)
        return not any(rk) and rv == V0
    def contains(self, other): return all(other.holds(k, v) for k, v in self.B)
    def show(self):
        nm = ('u1', 'u2', 'u3')
        def val(v):
            p, q, r = v; s = {0: '1', 1: 'i', 2: '-1', 3: '-i'}[p]
            return s + ('' if not q else ' z^%d' % q) + ('' if not r else ' w^%d' % r)
        return ', '.join('%s = %s' % ('*'.join(('%s^%d' % (nm[t], k[t]) if k[t] != 1 else nm[t]) for t in range(3) if k[t]), val(v)) for k, v in self.B) or 'T^3'
TORUS = Flat()
def meet_or_none(F, G):
    try: return F.meet(G)
    except Empty: return None
def gval(v):
    p, q, r = v; out = ONE
    for _ in range(p % 4): out = out * I_
    for _ in range(abs(q)): out = out * (z if q > 0 else z.conj())
    for _ in range(abs(r)): out = out * (w if r > 0 else w.conj())
    return out
def upow(u, k):
    out = ONE
    for x, e in zip(u, k):
        for _ in range(abs(e)): out = out * (x if e > 0 else x.conj())
    return out
def on_flat(F, u): return F is not None and all(upow(u, k) == gval(v) for k, v in F.B)

print('== 1. the flat calculus: exactness controls ==')
import random
rng = random.Random(40)
def rand_eq(): return (tuple(rng.randint(-2, 2) for _ in range(3)), (rng.randint(0, 3), rng.randint(-2, 2), rng.randint(-2, 2)))
def rand_one():
    while True:
        k, v = rand_eq()
        if any(k): return Flat([(k, v)])
trials = cons = idem = order = sym = assoc = contain = holds_ok = 0
for _ in range(400):
    eqs = [rand_eq() for _ in range(rng.randint(1, 4))]
    try: F = Flat(eqs)
    except Empty: continue
    cons += 1
    idem += Flat(F.B) == F and Flat.of(_hnf(list(F.B) + list(F.B))) == F
    sh = eqs[:]; rng.shuffle(sh); order += Flat(sh) == F
    holds_ok += all(F.holds(k, v) for k, v in eqs)
    Gf = rand_one() if rng.random() < 0.5 else TORUS
    Hf = rand_one() if rng.random() < 0.5 else TORUS
    FG, GF = meet_or_none(F, Gf), meet_or_none(Gf, F)
    sym += FG == GF
    A1 = None if FG is None else meet_or_none(FG, Hf); GH = meet_or_none(Gf, Hf); A2 = None if GH is None else meet_or_none(F, GH)
    assoc += A1 == A2
    contain += FG is None or (F.contains(FG) and Gf.contains(FG) and (FG == F) == Gf.contains(F))
    trials += 1
check('random systems: canonical form idempotent, independent of generator order, every generator holds; meet symmetric and associative; the meet contained in both, and equal to F exactly when G contains F', (idem, order, holds_ok, sym, assoc, contain) == (trials,) * 6 and trials > 200, True)
hand = []
try: Flat([((2, 0, 0), (0, 1, 0)), ((4, 0, 0), (0, 3, 0))]); hand.append('sat')
except Empty: hand.append('empty')
try: Flat([((2, 0, 0), (0, 1, 0)), ((4, 0, 0), (0, 2, 0))]); hand.append('sat')
except Empty: hand.append('empty')
try: Flat([((1, 1, 0), (2, 0, 0)), ((1, 1, 0), V0)]); hand.append('sat')
except Empty: hand.append('empty')
fa = Flat([((1, 1, 0), (1, 0, 0)), ((0, 1, -1), (0, 0, 1))]); fb = Flat([((1, 0, 1), (1, 0, -1)), ((1, 1, 0), (1, 0, 0))])
hand += [fa == fb, fa.holds((1, 0, 1), (1, 0, -1)), fa.holds((1, 0, 1), (1, 0, 1)), Flat([((2, 0, 0), V0)]).contains(Flat([((1, 0, 0), V0)])), Flat([((1, 0, 0), V0)]).contains(Flat([((2, 0, 0), V0)]))]
check('hand systems: u1^2 = z with u1^4 = z^3 empty, with u1^4 = z^2 satisfiable, u1 u2 = -1 with u1 u2 = 1 empty; two presentations of one flat equal; a derived character holds, a wrong one does not; u1^2 = 1 contains u1 = 1 and not conversely', hand, ['empty', 'sat', 'empty', True, True, False, True, False])
# independent reconstruction: flats whose pivots are 1 have explicit Gaussian-rational points (free coordinates chosen as
# Gaussian-rational units, pivots solved); every original equation is re-evaluated in exact arithmetic
UNITS_Q = [G(Fr(3, 5), Fr(4, 5)), G(Fr(8, 17), Fr(15, 17)), G(Fr(20, 29), Fr(21, 29)), G(Fr(7, 25), Fr(24, 25)), I_, G(-1)]
recon = rejected = tested = 0
for _ in range(3000):
    eqs = [rand_eq() for _ in range(rng.randint(1, 3))]
    try: F = Flat(eqs)
    except Empty: continue
    piv = [next(c for c in range(3) if k[c]) for k, v in F.B]
    if any(k[p] != 1 for (k, v), p in zip(F.B, piv)): continue
    u = [rng.choice(UNITS_Q) if c not in piv else None for c in range(3)]
    for (k, v), p in reversed(list(zip(F.B, piv))):
        rest = upow([u[c] if (c > p and k[c]) else ONE for c in range(3)], [k[c] if c > p else 0 for c in range(3)])
        u[p] = gval(v) * rest.conj()
    tested += 1
    recon += all(upow(u, k) == gval(v) for k, v in eqs) and on_flat(F, u)
    if any(k[0] for k, v in F.B):
        bad = [u[0] * G(Fr(3, 5), Fr(4, 5)), u[1], u[2]]
        rejected += not on_flat(F, bad)
    else:
        rejected += 1
check('explicit points reconstructed on the unit-pivot flats among 3000 random systems satisfy every original equation exactly, and moving u1 off the flat is detected whenever the flat constrains u1', (tested > 100, recon == tested, rejected == tested), (True, True, True))
print('  (%.0fs)' % (time.time() - t0))

# ---- act 37's census of SIG's Dita structures and act 38's two exceptional index maps, verbatim from act 38's probe
CLASSES = [(nm, m, n, tuple(tuple(b) for b in cp), tuple(tuple(r) for r in rows)) for nm, m, n, cp, rows in [["k1", 4, 4, [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]], [[0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15]]], ["k2", 4, 4, [[0, 2, 8, 10], [1, 3, 9, 11], [4, 6, 12, 14], [5, 7, 13, 15]], [[0, 2, 8, 10], [1, 3, 9, 11], [4, 6, 12, 14], [5, 7, 13, 15]]], ["k3", 4, 4, [[0, 2, 9, 11], [1, 3, 8, 10], [4, 6, 13, 15], [5, 7, 12, 14]], [[0, 6, 8, 14], [1, 7, 9, 15], [2, 4, 10, 12], [3, 5, 11, 13]]], ["k4", 4, 4, [[0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15]], [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]], ["e1", 8, 2, [[0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11], [12, 14], [13, 15]], [[0, 2, 4, 6, 8, 10, 12, 14], [1, 3, 5, 7, 9, 11, 13, 15]]], ["e2", 8, 2, [[0, 8], [1, 9], [2, 10], [3, 11], [4, 12], [5, 13], [6, 14], [7, 15]], [[0, 1, 2, 3, 8, 9, 10, 11], [4, 5, 6, 7, 12, 13, 14, 15]]], ["t1", 2, 8, [[0, 1, 2, 3, 8, 9, 10, 11], [4, 5, 6, 7, 12, 13, 14, 15]], [[0, 8], [1, 9], [2, 10], [3, 11], [4, 12], [5, 13], [6, 14], [7, 15]]], ["t2", 2, 8, [[0, 2, 4, 6, 8, 10, 12, 14], [1, 3, 5, 7, 9, 11, 13, 15]], [[0, 2], [1, 3], [4, 6], [5, 7], [8, 10], [9, 11], [12, 14], [13, 15]]], ["t3", 2, 8, [[0, 2, 5, 7, 8, 10, 13, 15], [1, 3, 4, 6, 9, 11, 12, 14]], [[0, 10], [1, 11], [2, 8], [3, 9], [4, 14], [5, 15], [6, 12], [7, 13]]]]]
M_COL = (((0, 2, 4, 6, 8, 10, 12, 14), (1, 3, 5, 7, 9, 11, 13, 15)), ((0, 2), (1, 3), (4, 6), (5, 15), (7, 13), (8, 10), (9, 11), (12, 14)))
M_ROW = (((0, 1, 2, 3, 8, 9, 10, 11), (4, 5, 6, 7, 12, 13, 14, 15)), ((0, 2), (1, 9), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15), (8, 10)))
STRUCT_OF = {nm: ((m, n), cp, rows) for nm, m, n, cp, rows in CLASSES}

# ---- the family and its structures ---------------------------------------------------------------------------------
def EA_(i, j): return EA(i, j)
PA = [[EA(i, j) for j in range(16)] for i in range(16)]
PB = [[EB(i, j) for j in range(16)] for i in range(16)]
PC = [[EC(i, j) for j in range(16)] for i in range(16)]
def ksub(a, b): return tuple(x - y for x, y in zip(a, b))
def kadd(a, b): return tuple(x + y for x, y in zip(a, b))
import itertools
PAIRS = list(itertools.combinations(range(16), 2))
SHAPES3 = ((4, 4), (8, 2), (2, 8))
def orientations(KA, KB, KC):
    K = [[(KA[i][j], KB[i][j], KC[i][j]) for j in range(16)] for i in range(16)]
    C = [[SIGE[i][j] for j in range(16)] for i in range(16)]
    return {'column': (K, C), 'row': ([list(c) for c in zip(*K)], [list(c) for c in zip(*C)])}
def enumerate_candidates(OR):
    """every (orientation, shape, column blocks, row classes) whose within-class pairs have, on every block, a common point
    of their proportionality loci; a structure admitted anywhere on T^3 is among them (see the preregistration)"""
    cache = {}
    def pbf(vals):
        if vals in cache: return cache[vals]
        d0, e0 = vals[0]
        try:
            F = TORUS
            for d, e in vals[1:]: F = F.add(ksub(d, d0), vsub(e0, e))
            r = F
        except Empty: r = None
        cache[vals] = r; return r
    cands = {}; stats = {}
    for form, (Km, Cm) in OR.items():
        de = {p: [(ksub(Km[p[0]][j], Km[p[1]][j]), vsub(Cm[p[0]][j], Cm[p[1]][j])) for j in range(16)] for p in PAIRS}
        for m, n in SHAPES3:
            good = {}
            for Sb in itertools.combinations(range(16), n):
                loc = {}
                for p in PAIRS:
                    F = pbf(tuple(sorted(set(de[p][j] for j in Sb))))
                    if F is not None: loc[p] = F
                def rec(rem, classes, F):
                    if not rem: good.setdefault(tuple(classes), []).append((Sb, F)); return
                    i = min(rem)
                    nb = sorted(j for j in rem if j != i and (i, j) in loc)
                    for rest in itertools.combinations(nb, m - 1):
                        cl = (i,) + rest; Gf = F
                        for a, b in itertools.combinations(cl, 2):
                            Gf = meet_or_none(Gf, loc[(a, b)])
                            if Gf is None: break
                        if Gf is None: continue
                        rec(rem - set(cl), classes + [cl], Gf)
                rec(frozenset(range(16)), [], TORUS)
            nb0 = len(cands)
            for P, blocks in good.items():
                def cover(rem, chosen, F):
                    if not rem: cands[(form, (m, n), tuple(sorted(chosen)), P)] = F; return
                    first = min(rem)
                    for Sb, Gf in blocks:
                        if Sb[0] == first and set(Sb) <= rem:
                            Hf = meet_or_none(F, Gf)
                            if Hf is not None: cover(rem - set(Sb), chosen + [Sb], Hf)
                cover(frozenset(range(16)), [], TORUS)
            stats[(form, (m, n))] = len(cands) - nb0
    return cands, stats
def conditions(OR, form, mn, cp, rows, relaxed):
    Km, Cm = OR[form]; m, n = mn
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    def ent(i, j): return (Km[i][j], Cm[i][j])
    def div(x, y): return (ksub(x[0], y[0]), vsub(x[1], y[1]))
    def mul(x, y): return (kadd(x[0], y[0]), vadd(x[1], y[1]))
    out = []
    for c in range(m):
        for b in range(n):
            for a in range(m):
                for d in range(1, n):
                    i, i2, j, j0 = row[(a, b)], row[(0, b)], col[(c, d)], col[(c, 0)]
                    out.append(div(div(ent(i, j), ent(i2, j)), div(ent(i, j0), ent(i2, j0))))
    lam = {(a, b, c): div(ent(row[(a, b)], col[(c, 0)]), ent(row[(0, b)], col[(c, 0)])) for a in range(m) for b in range(n) for c in range(m)}
    for a in range(m):
        for b in range(n):
            for c in range(m):
                if not relaxed: out.append(div(lam[(a, b, c)], mul(lam[(a, 0, c)], lam[(0, b, c)])))
                elif c > 0: out.append(div(div(lam[(a, b, c)], lam[(a, 0, c)]), div(lam[(a, b, 0)], lam[(a, 0, 0)])))
    return out
def solve(conds):
    """the exact solution flat of {u^k c = 1}, or None"""
    try:
        F = TORUS
        for k, c in conds:
            if not any(k):
                if c != V0: return None
                continue
            F = F.add(k, vsub(V0, c))
        return F
    except Empty:
        return None
def classify(KA, KB, KC):
    OR = orientations(KA, KB, KC)
    cands, stats = enumerate_candidates(OR)
    loci = {}
    for key in cands:
        form, mn, cp, rows = key
        loci[key] = (solve(conditions(OR, form, mn, cp, rows, False)), solve(conditions(OR, form, mn, cp, rows, True)))
    return OR, cands, stats, loci
def union_faces(loci):
    """the maximal nonempty strict loci, and whether every nonempty locus lies in one of them"""
    ne = set(F for F in loci.values() if F is not None)
    maximal = sorted((F for F in ne if not any(M2 != F and M2.contains(F) for M2 in ne)), key=lambda F: F.B)
    return maximal, all(any(M.contains(F) for M in maximal) for F in ne)

print('== 2. completeness: every Dita structure admitted anywhere is among the enumerated candidates ==')
OR, CANDS, STATS, LOCI = classify(PA, PB, PC)
check('candidate structures (a common point of the proportionality loci on every block), by orientation and shape', sorted((f, mn, k) for (f, mn), k in STATS.items()), sorted([('column', (4, 4), 13), ('column', (8, 2), 5), ('column', (2, 8), 5), ('row', (4, 4), 13), ('row', (8, 2), 5), ('row', (2, 8), 5)]))
check('in all', len(CANDS), 46)
print('  (%.0fs)' % (time.time() - t0))


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

# ---- A41: the production computation -- act 40's candidates and flats, every alignment ------------------------------
def a41_div(x, y): return (ksub(x[0], y[0]), vsub(x[1], y[1]))
def a41_add_all(F, conds):
    try:
        for k, c in conds:
            if not any(k):
                if c != V0: return None
                continue
            F = F.add(k, vsub(V0, c))
        return F
    except Empty:
        return None
def a41_prop_conds(OR, form, cp, rows):
    Km, Cm = OR[form]
    def ent(i, j): return (Km[i][j], Cm[i][j])
    return [a41_div(a41_div(ent(i, j), ent(g[0], j)), a41_div(ent(i, bl[0]), ent(g[0], bl[0]))) for g in rows for i in g[1:] for bl in cp for j in bl[1:]]
def a41_group_flats(OR, form, cp, rows, b, Pf, relaxed):
    """for row class b >= 1: {flat: [sigma, ...]}, sigma the rows of class b carrying labels 0..m-1, pruned label by label"""
    Km, Cm = OR[form]; m = len(rows[0])
    def ent(i, j): return (Km[i][j], Cm[i][j])
    col0 = [cp[c][0] for c in range(m)]; ref = rows[0]
    def lam(r, r0, c): return a41_div(ent(r, col0[c]), ent(r0, col0[c]))
    out = {}
    for r0 in rows[b]:
        def rec(a, used, sigma, F):
            if a == m: out.setdefault(F, []).append(tuple(sigma)); return
            for r in rows[b]:
                if r in used: continue
                if not relaxed: conds = [a41_div(lam(r, r0, c), lam(ref[a], ref[0], c)) for c in range(m)]
                else: conds = [a41_div(a41_div(lam(r, r0, c), lam(ref[a], ref[0], c)), a41_div(lam(r, r0, 0), lam(ref[a], ref[0], 0))) for c in range(1, m)]
                G_ = a41_add_all(F, conds)
                if G_ is None: continue
                used.add(r); sigma.append(r); rec(a + 1, used, sigma, G_); sigma.pop(); used.discard(r)
        rec(1, {r0}, [r0], Pf)
    return out
class A41Family:
    """the production census of a family: for every partition candidate, the proportionality flat and, per row class,
    the flats of its alignments; loci are unions over alignments"""
    def __init__(self, OR, cands):
        self.OR = OR; self.cands = sorted(cands); self.data = {}
        for key in self.cands:
            form, (m, n), cp, rows = key
            for relaxed in (False, True):
                Pf = a41_add_all(TORUS, a41_prop_conds(OR, form, cp, rows))
                groups = None if Pf is None else [a41_group_flats(OR, form, cp, rows, b, Pf, relaxed) for b in range(1, n)]
                self.data[(key, relaxed)] = (Pf, groups)
    def locus(self, key, relaxed):
        Pf, groups = self.data[(key, relaxed)]
        if Pf is None or any(not g for g in groups): return set()
        cur = {Pf}
        for g in groups:
            nxt = set()
            for F in cur:
                for G_ in g:
                    H_ = meet_or_none(F, G_)
                    if H_ is not None: nxt.add(H_)
            cur = nxt
        return cur
    def at(self, u, relaxed):
        """[(key, valid alignments)] at the point u"""
        out = []
        for key in self.cands:
            Pf, groups = self.data[(key, relaxed)]
            if Pf is None or not on_flat(Pf, u): continue
            M = 1
            for g in groups: M *= sum(len(s) for F, s in g.items() if on_flat(F, u))
            if M: out.append((key, M))
        return out
    def triples(self, u, relaxed):
        """the realizing (orientation, shape, blocks, row classes, threads) at u"""
        out = set()
        for key in self.cands:
            form, (m, n), cp, rows = key
            Pf, groups = self.data[(key, relaxed)]
            if Pf is None or not on_flat(Pf, u): continue
            opts = [[s for F, ss in g.items() if on_flat(F, u) for s in ss] for g in groups]
            for combo in itertools.product(*opts):
                threads = frozenset(frozenset([rows[0][a]] + [combo[b][a] for b in range(n - 1)]) for a in range(m))
                out.add((form, (m, n), frozenset(map(frozenset, cp)), frozenset(map(frozenset, rows)), threads))
        return out
def a41_norm(entries):
    return sorted([form, [m, n], sorted(map(sorted, cp)), sorted(map(sorted, rows)), k] for ((form, (m, n), cp, rows), k) in entries)
A41_ONE3 = (ONE, ONE, ONE)
def a41_pt1(u): return (u, ONE, ONE)
Z16 = [[0] * 16 for _ in range(16)]
t_a41 = time.time()

print('== A41-1. the index-map calculus: the fibres of the projection, and literal index maps at SIG ==')
import math, random as a41_random
def a41_R(m, n): return math.factorial(m) * math.factorial(n) * math.factorial(m) * math.factorial(n) ** m
check('|R(m, n)| for the shapes 4 x 4, 8 x 2, 2 x 8, and the alignment counts (m!)^(n-1)', ([a41_R(4, 4), a41_R(8, 2), a41_R(2, 8)], [24 ** 3, 40320, 2 ** 7]), ([a41_R(4, 4), a41_R(8, 2), a41_R(2, 8)], [math.factorial(4) ** 3, math.factorial(8) ** 1, math.factorial(2) ** 7]))
a41_fib = []
for m, n in ((2, 2), (2, 3), (3, 2), (2, 4), (4, 2)):
    N = m * n; keys = [(a, b) for a in range(m) for b in range(n)]
    rowf = {}; colf = {}
    for p in itertools.permutations(range(N)):
        e = dict(zip(keys, p))
        k = (frozenset(frozenset(e[(a, b)] for a in range(m)) for b in range(n)), frozenset(frozenset(e[(a, b)] for b in range(n)) for a in range(m)))
        rowf[k] = rowf.get(k, 0) + 1
        k2 = frozenset(frozenset(e[(c, d)] for d in range(n)) for c in range(m))
        colf[k2] = colf.get(k2, 0) + 1
    sizes = {r * c for r in rowf.values() for c in colf.values()}
    per_part = {}
    for cl, th in rowf: per_part[cl] = per_part.get(cl, 0) + 1
    a41_fib.append((m, n, sorted(sizes) == [a41_R(m, n)], set(per_part.values()) == {math.factorial(m) ** (n - 1)}))
check('on the carriers of four, six and eight points, every fibre of the projection has |R(m, n)| elements and every partition (m!)^(n-1) alignments', all(x[2] and x[3] for x in a41_fib) and len(a41_fib) == 5, True)
print('  (%.0fs)' % (time.time() - t0))

print('== A41-7. act 39\'s family H3, every alignment (the production census) ==')
FAM_H3 = A41Family(OR, CANDS)
a41_loc = {(k, r): FAM_H3.locus(k, r) for k in FAM_H3.cands for r in (False, True)}
a41_ne = {r: sum(1 for k in FAM_H3.cands if a41_loc[(k, r)]) for r in (False, True)}
a41_sr = all(a41_loc[(k, False)] == a41_loc[(k, True)] for k in FAM_H3.cands)
a41_flats = set().union(*(a41_loc[(k, False)] for k in FAM_H3.cands))
def a41_coord(F): return all(sorted(map(abs, k)) == [0, 0, 1] and v in (V0, (2, 0, 0)) for k, v in F.B)
a41_max = sorted(F.show() for F in a41_flats if not any(G_ != F and G_.contains(F) for G_ in a41_flats))
A41_FIVE = sorted(['u1 = -1', 'u1 = 1', 'u2 = 1', 'u3 = -1', 'u3 = 1'])
a41_h3 = {'candidates': len(FAM_H3.cands), 'nonempty': a41_ne[False], 'nonempty_relaxed': a41_ne[True], 'strict_eq_relaxed': a41_sr,
          'flats': len(a41_flats), 'noncoord': sorted(F.show() for F in a41_flats if not a41_coord(F)), 'maximal': a41_max,
          'five_faces': a41_max == A41_FIVE,
          'at_one': a41_norm(FAM_H3.at(A41_ONE3, False)), 'at_mone': a41_norm(FAM_H3.at((G(-1), G(-1), G(-1)), False))}
print('  candidates %d, nonempty loci %d / %d, strict = relaxed %s, flats %d, maximal %s' % (a41_h3['candidates'], a41_ne[False], a41_ne[True], a41_sr, len(a41_flats), a41_max))
print('  (%.0fs)' % (time.time() - t0))

print('== A41-2. the sorted control: the landed values from the sorted alignment alone ==')
a41_sorted_loci = {k: solve(conditions(OR, *k, False)) for k in CANDS}
check("act 40's sorted census: empty and nonempty loci, all coordinate, the five faces", (sum(1 for v in a41_sorted_loci.values() if v is None), sum(1 for v in a41_sorted_loci.values() if v is not None), all(a41_coord(F) for F in a41_sorted_loci.values() if F is not None), union_faces(a41_sorted_loci)[0] and sorted(F.show() for F in union_faces(a41_sorted_loci)[0])), (16, 30, True, A41_FIVE))
def a41_sorted_at(H):
    HT = [list(c) for c in zip(*H)]; out = []
    for form, M in (('column', H), ('row', HT)):
        for mn in ((4, 4), (8, 2), (2, 8)):
            o = dita_orientations(M, *mn); out.append((form, mn, len(o), sum(1 for x in o if x[2])))
    return out
a41_sS = a41_sorted_at(SIG)
check("act 37's sorted census of SIG: (candidates, exact) per orientation and shape", [(x[2], x[3]) for x in a41_sS], [(5, 4), (3, 2), (3, 3)] * 2)
a41_sM = a41_sorted_at(H3(G(-1), G(-1), G(-1)))
check("act 38's sorted census at u = -1: (candidates, exact) per orientation and shape", [(x[2], x[3]) for x in a41_sM], [(1, 0), (1, 0), (1, 1)] * 2)
print('  (%.0fs)' % (time.time() - t0))

print('== A41-3. the census of the stratum point: alignments, realizing triples, factorization classes, partition orbits ==')
def a41_decomp(perm):
    for t_ in (False, True):
        rp = {}; cp_ = {}; ok = True
        for i in range(16):
            for j in range(16):
                i2, j2 = divmod(perm[i * 16 + j], 16)
                if t_: i2, j2 = j2, i2
                if rp.setdefault(i, i2) != i2 or cp_.setdefault(j, j2) != j2: ok = False; break
            if not ok: break
        if ok: return (t_, rp, cp_)
    raise AssertionError('not a position map')
A41_GRP = [a41_decomp(p) for p, s in elems]
def a41_img(g, x):
    t_, rp, cp_ = g; form, mn, blocks, rcl, threads = x
    colmap, rowmap = (cp_, rp) if form == 'column' else (rp, cp_)
    nf = form if not t_ else ('row' if form == 'column' else 'column')
    return (nf, mn, frozenset(frozenset(colmap[j] for j in B) for B in blocks), frozenset(frozenset(rowmap[i] for i in C) for C in rcl),
            frozenset(frozenset(rowmap[i] for i in T) for T in threads))
def a41_orbits(X, grp, part_only=False):
    X = set((x[:4] + (frozenset(),)) if part_only else x for x in X); seen = set(); n_ = 0
    for x in X:
        if x in seen: continue
        seen |= {a41_img(g, x) for g in grp}; n_ += 1
    closed = all(a41_img(g, x) in X for g in grp for x in X)
    burnside = Fr(sum(sum(1 for x in X if a41_img(g, x) == x) for g in grp), len(grp))
    return n_, closed, burnside
a41_sig = {}
for relaxed in (False, True):
    X = FAM_H3.triples(A41_ONE3, relaxed)
    tf = [g for g in A41_GRP if not g[0]]
    cf, clf, bf = a41_orbits(X, A41_GRP); ct, clt, bt = a41_orbits(X, tf)
    pf, _, bpf = a41_orbits(X, A41_GRP, True); pt, _, bpt = a41_orbits(X, tf, True)
    a41_sig['relaxed' if relaxed else 'strict'] = {'census': a41_norm(FAM_H3.at(A41_ONE3, relaxed)), 'triples': len(X),
        'classes_full': cf, 'classes_tfree': ct, 'porbits_full': pf, 'porbits_tfree': pt, 'closed': clf and clt,
        'burnside_agrees': (bf == cf, bt == ct, bpf == pf, bpt == pt), 'tfree_order': len(tf)}
# the sorted restriction's partition orbits (act 37's nine), as a control
a41_sorted_parts = set()
for form, M in (('column', SIG), ('row', SIGT)):
    for mn in ((4, 4), (8, 2), (2, 8)):
        for cp, rows, ok, _, _ in dita_orientations(M, *mn):
            if ok: a41_sorted_parts.add((form, mn, frozenset(map(frozenset, cp)), frozenset(map(frozenset, rows)), frozenset()))
a41_sig_sorted = {'partitions': len(a41_sorted_parts), 'porbits_full': a41_orbits(a41_sorted_parts, A41_GRP, True)[0]}
check("act 37's eighteen and nine: the sorted-alignment restriction's partition structures and their partition orbits under the full stabilizer", (a41_sig_sorted['partitions'], a41_sig_sorted['porbits_full']), (18, 9))
print('  (%.0fs)' % (time.time() - t0))

print('== A41-5. act 36\'s arc SIG o u^W, every alignment ==')
WM = [[W[i * 16 + j] for j in range(16)] for i in range(16)]
OR_W = orientations(WM, Z16, Z16); CANDS_W, _ = enumerate_candidates(OR_W)
FAM_W = A41Family(OR_W, CANDS_W)
def a41_arc_summary(fam, relaxed):
    ident = []; pts = set()
    for k in fam.cands:
        for F in fam.locus(k, relaxed):
            if F.dim() == 3: ident.append(k)
            else: pts.add(F.show())
    return sorted([k[0], list(k[1]), sorted(map(sorted, k[2])), sorted(map(sorted, k[3]))] for k in set(ident)), sorted(pts)
a41_w = {}
for relaxed in (False, True):
    idn, pts = a41_arc_summary(FAM_W, relaxed)
    a41_w['relaxed' if relaxed else 'strict'] = {'identically': idn, 'exceptional': pts,
        'at1': a41_norm(FAM_W.at(a41_pt1(ONE), relaxed)), 'atm1': a41_norm(FAM_W.at(a41_pt1(G(-1)), relaxed)),
        'P': a41_norm(FAM_W.at(a41_pt1(A41_U60), relaxed)), 'u5': a41_norm(FAM_W.at(a41_pt1(A41_U5), relaxed))}
a41_frozen28 = ['column', [2, 8], sorted(map(sorted, FROZEN_BLOCKS)), sorted(map(sorted, FROZEN_CLASSES))]
a41_w['exclusive'] = [x[:4] for x in a41_w['strict']['identically']] == sorted([a41_frozen28, ['row'] + a41_frozen28[1:]]) and a41_w['strict']['exceptional'] == ['u1 = 1']
print('  strict: identically %d, exceptional %s; relaxed: identically %d, exceptional %s' % (len(a41_w['strict']['identically']), a41_w['strict']['exceptional'], len(a41_w['relaxed']['identically']), a41_w['relaxed']['exceptional']))
print('  (%.0fs)' % (time.time() - t0))

print('== A41-6. act 38\'s arc SIG o u^E, every alignment ==')
OR_E = orientations(EE, Z16, Z16); CANDS_E, _ = enumerate_candidates(OR_E)
FAM_E = A41Family(OR_E, CANDS_E)
a41_e = {}
for relaxed in (False, True):
    idn, pts = a41_arc_summary(FAM_E, relaxed)
    a41_e['relaxed' if relaxed else 'strict'] = {'identically': idn, 'exceptional': pts, 'atm1': a41_norm(FAM_E.at(a41_pt1(G(-1)), relaxed))}
def a41_swap_part(x, rs, cs):
    form, mn, blocks, rcl = x
    if form == 'column': return (form, mn, frozenset(frozenset(cs.get(j, j) for j in B) for B in blocks), frozenset(frozenset(rs.get(i, i) for i in C) for C in rcl))
    return (form, mn, frozenset(frozenset(rs.get(i, i) for i in B) for B in blocks), frozenset(frozenset(cs.get(j, j) for j in C) for C in rcl))
_, k4cp, k4rows = STRUCT_OF['k4']
k4c = ('column', (4, 4), frozenset(map(frozenset, k4cp)), frozenset(map(frozenset, k4rows)))
k4x = a41_swap_part(k4c, {7: 15, 15: 7}, {2: 8, 8: 2})
k4x_row = ('row', (4, 4), k4x[3], k4x[2])
a41_e44 = set((k[0], k[1], frozenset(map(frozenset, k[2])), frozenset(map(frozenset, k[3]))) for k, M in FAM_E.at(a41_pt1(G(-1)), False) if k[1] == (4, 4))
a41_e['m1_k4_exchanged'] = a41_e44 == {k4x, k4x_row}
a41_sig_parts = set((k[0], k[1], frozenset(map(frozenset, k[2])), frozenset(map(frozenset, k[3]))) for k, M in FAM_H3.at(A41_ONE3, False))
a41_e_keys = {(k[0], k[1], frozenset(map(frozenset, k[2])), frozenset(map(frozenset, k[3]))): k for k in FAM_E.cands}
a41_e['sig_only_at_1'] = all(p in a41_e_keys and sorted(F.show() for F in FAM_E.locus(a41_e_keys[p], False)) == ['u1 = 1'] for p in a41_sig_parts)
a41_e['arc_in_some_locus'] = any(F.dim() == 3 for k in FAM_E.cands for r in (False, True) for F in FAM_E.locus(k, r))
# consistency: the diagonal of H3's loci gives the same exceptional points
DIAG = Flat([((1, -1, 0), V0), ((0, 1, -1), V0)])
a41_diag = sorted(set(G_.show() for k in FAM_H3.cands for F in a41_loc[(k, False)] for G_ in [meet_or_none(F, DIAG)] if G_ is not None))
check("control: the diagonal of H3's loci is act 38's arc: the points u = 1 and u = -1", a41_diag, ['u1 = -1, u2 = -1, u3 = -1', 'u1 = 1, u2 = 1, u3 = 1'])
print('  strict exceptional %s, relaxed %s, at u = -1: %d partition structures' % (a41_e['strict']['exceptional'], a41_e['relaxed']['exceptional'], len(a41_e['strict']['atm1'])))
print('  (%.0fs)' % (time.time() - t0))

print('== A41-8. exact reconstruction of every partition structure the sorted alignment misses, at literal index maps ==')
def a41_reconstruct(H, form, m, n, blocks, rcl, threads, relaxed):
    """a literal index map over (blocks, row classes, threads), and H = X Y' (D absorbed) checked entry by entry with
    X and every Y'_c unitary; relaxed: the rows first rescaled by the unit factors the relaxed condition supplies"""
    M = H if form == 'column' else [list(c) for c in zip(*H)]
    blocks = [sorted(B) for B in sorted(map(sorted, blocks))]; rcl = [sorted(C) for C in sorted(map(sorted, rcl))]
    threads = sorted(map(sorted, threads))
    eR = {}
    for a, T in enumerate(threads):
        for b, C in enumerate(rcl):
            (r,) = set(T) & set(C); eR[(a, b)] = r
    eC = {(c, d): blocks[c][d] for c in range(m) for d in range(n)}
    M = [row[:] for row in M]
    if relaxed:
        for b in range(n):
            for a in range(m):
                mu = M[eR[(a, b)]][eC[(0, 0)]] * M[eR[(0, b)]][eC[(0, 0)]].conj() * (M[eR[(a, 0)]][eC[(0, 0)]] * M[eR[(0, 0)]][eC[(0, 0)]].conj()).conj()
                M[eR[(a, b)]] = [x * mu.conj() for x in M[eR[(a, b)]]]
    X = [[M[eR[(a, 0)]][eC[(c, 0)]] * M[eR[(0, 0)]][eC[(c, 0)]].conj() for c in range(m)] for a in range(m)]
    Yp = [[[M[eR[(0, b)]][eC[(c, d)]] for d in range(n)] for b in range(n)] for c in range(m)]
    ident = all(M[eR[(a, b)]][eC[(c, d)]] == X[a][c] * Yp[c][b][d] for a in range(m) for b in range(n) for c in range(m) for d in range(n))
    return ident and is_unitary_s(X, m) and all(is_unitary_s(Yp[c], n) for c in range(m))
a41_added = []
for role, fam, par, famobj in (('SIG', 'H3', A41_ONE3, FAM_H3), ('Hu(-1)', 'Hu', a41_pt1(G(-1)), FAM_E), ('Pu(-1)', 'Pu', a41_pt1(G(-1)), FAM_W)):
    Hm = a41_matrix(fam, par if fam == 'H3' else par[0])
    srt = set()
    for form, M in (('column', Hm), ('row', [list(c) for c in zip(*Hm)])):
        for mn in ((4, 4), (8, 2), (2, 8)):
            for cp, rows, ok, _, _ in dita_orientations(M, *mn):
                if ok: srt.add((form, mn, frozenset(map(frozenset, cp)), frozenset(map(frozenset, rows))))
    for relaxed in (False, True):
        seen = set()
        for x in sorted(famobj.triples(par, relaxed), key=lambda y: (y[0], y[1], sorted(map(sorted, y[2])), sorted(map(sorted, y[4])))):
            p_ = x[:4]
            if p_ in srt or p_ in seen: continue
            seen.add(p_)
            a41_added.append((role, relaxed, x[0], x[1], a41_reconstruct(Hm, x[0], x[1][0], x[1][1], x[2], x[3], x[4], relaxed)))
check('every partition structure the sorted alignment misses at SIG, Hu(-1) and Pu(-1) is reconstructed exactly at a literal index map, with unitary factors', all(x[4] for x in a41_added) and len(a41_added) > 0, True)
# and at SIG, literal index maps over invalid alignments do not reconstruct (forty drawn by a seeded generator)
a41_rng = a41_random.Random(41); a41_neg = 0; a41_negtries = 0
for k in FAM_H3.cands:
    form, (m, n), cp, rows = k
    if not any(on_flat(F, A41_ONE3) for F in a41_loc[(k, False)]) or m == 2: continue
    valid = set(x[4] for x in FAM_H3.triples(A41_ONE3, False) if x[0] == form and x[2] == frozenset(map(frozenset, cp)))
    for _ in range(4):
        perms = [list(rows[b]) for b in range(n)]
        for b in range(1, n): a41_rng.shuffle(perms[b])
        th = frozenset(frozenset(perms[b][a] for b in range(n)) for a in range(m))
        if th in valid: continue
        a41_negtries += 1; a41_neg += not a41_reconstruct(SIG, form, m, n, frozenset(map(frozenset, cp)), frozenset(map(frozenset, rows)), th, False)
check('control: literal index maps over invalid alignments at SIG do not reconstruct', (a41_negtries > 0, a41_neg == a41_negtries), (True, True))
print('  (%.0fs)' % (time.time() - t0))

print('== A41-9p. the production census at the forty-two named test cases ==')
def a41_prod_case(fam, par, relaxed):
    if fam == 'H3': return a41_norm(FAM_H3.at(par, relaxed))
    if fam == 'Pu': return a41_norm(FAM_W.at(a41_pt1(par), relaxed))
    return a41_norm(FAM_E.at(a41_pt1(par), relaxed))
A41_PCASES = {role: {'strict': a41_prod_case(fam, par, False), 'relaxed': a41_prod_case(fam, par, True)} for role, fam, par in A41_CASES}
a41_mk = {}
for role, fam, par in A41_CASES: a41_mk.setdefault(a41_key(a41_matrix(fam, par)), []).append(role)
A41_PCOINC = sorted(sorted(v) for v in a41_mk.values() if len(v) > 1)
check('control: coinciding named test cases have equal production results', all(all(A41_PCASES[r] == A41_PCASES[g[0]] for r in g) for g in A41_PCOINC), True)
print('  (%.0fs)' % (time.time() - t0))

print('== A41-10. the exchange identities ==')
def a41_rswap(H): H = [r[:] for r in H]; H[7], H[15] = H[15], H[7]; return H
def a41_cswap(H): return [[r[8] if j == 2 else r[2] if j == 8 else r[j] for j in range(16)] for r in H]
a41_ex = []
for s in range(3):
    for u in ((TESTU[s], TESTU[s + 1], TESTU[s + 2]), (TESTU[s + 1], TESTU[s + 2], TESTU[s]), (TESTU[s + 2], TESTU[s], TESTU[s + 1]), (I_, TESTU[s], TESTU[s + 2]), (TESTU[s], ONE, I_)):
        a41_ex.append(H3(G(-1) * u[0], u[1], u[2]) == a41_rswap(H3(*u)) and H3(u[0], u[1], G(-1) * u[2]) == a41_cswap(H3(*u)))
check('H3(-u1, u2, u3) is H3 with rows 7 and 15 exchanged, and H3(u1, u2, -u3) with columns 2 and 8 exchanged, at fifteen exact points', (len(a41_ex), all(a41_ex)), (15, True))
def a41_parts_at(u): return set((k[0], k[1], frozenset(map(frozenset, k[2])), frozenset(map(frozenset, k[3]))) for k, M in FAM_H3.at(u, False))
a41_tr = []
for s in range(3):
    up = (ONE, TESTU[s], TESTU[s + 1]); um = (G(-1), TESTU[s], TESTU[s + 1])
    a41_tr.append({a41_swap_part(p, {7: 15, 15: 7}, {}) for p in a41_parts_at(up)} == a41_parts_at(um))
    up = (TESTU[s], TESTU[s + 1], ONE); um = (TESTU[s], TESTU[s + 1], G(-1))
    a41_tr.append({a41_swap_part(p, {}, {2: 8, 8: 2}) for p in a41_parts_at(up)} == a41_parts_at(um))
check('the partition structures on the -1 faces are the exchange images of those on the +1 faces, at three points of each pair', all(a41_tr), True)
print('  (%.0fs)' % (time.time() - t0))

print('== A41-11. countercontrols ==')
a41_full_sig = sum(M for k, M in FAM_H3.at(A41_ONE3, False))
a41_partial = 0
for key in FAM_H3.cands:
    Pf, groups = FAM_H3.data[(key, False)]
    if Pf is None or not on_flat(Pf, A41_ONE3): continue
    rows = key[3]; M = 1
    for b, g in enumerate(groups):
        M *= sum(1 for F, ss in g.items() if on_flat(F, A41_ONE3) for s in ss if b == 0 or tuple(s) == tuple(rows[b + 1]))
    a41_partial += M
check('a partial alignment rule, sorted in every row class but one, gives a different count at SIG than every alignment', a41_partial != a41_full_sig, True)
Cp = [r[:] for r in PC]; Cp[1][2] = 0
OR_C = orientations(PA, PB, Cp); CANDS_C, _ = enumerate_candidates(OR_C)
FAM_C = A41Family(OR_C, CANDS_C)
a41_cf = set().union(*(FAM_C.locus(k, False) for k in FAM_C.cands))
a41_cmax = sorted(F.show() for F in a41_cf if not any(G_ != F and G_.contains(F) for G_ in a41_cf))
check("act 40's perturbed pieces, one entry of C cleared, classified under every alignment: the union is not the five faces", a41_cmax != A41_FIVE, True)
print('  (%.0fs)' % (time.time() - t0))

A41_OBJ = {'cases': A41_PCASES, 'coincidences': A41_PCOINC, 'sig': a41_sig, 'sig_sorted': a41_sig_sorted, 'w': a41_w, 'e': a41_e, 'h3': a41_h3,
           'fibres': [list(x[:2]) + [x[2], x[3]] for x in a41_fib], 'added_reconstructed': [[x[0], x[1], x[2], list(x[3]), x[4]] for x in a41_added],
           'counter_partial': [a41_partial, a41_full_sig], 'counter_perturbed_maximal': a41_cmax}
A41_JSON = json.dumps(A41_OBJ, sort_keys=True, separators=(',', ':'))
print('A41-MEASUREMENTS production ' + A41_JSON)
print('A41-SHA256 production ' + hashlib.sha256(A41_JSON.encode()).hexdigest())
a41_mode = 'MEASURED'
if os.path.exists(A41_RECORD):
    rec = json.load(open(A41_RECORD, encoding='utf-8'))
    check('replay: the measurement equals the committed measurements.json, elementwise', json.loads(A41_JSON) == rec.get('production'), True)
    a41_mode = 'REPLAYED'
print()
if fails:
    print('dita_index_map_probe: FAILED (%d): %s' % (len(fails), fails)); sys.exit(1)
print('dita_index_map_probe: OK -- %s: %d named test cases; H3 %d partition candidates, %d nonempty loci' % (a41_mode, len(A41_PCASES), a41_h3['candidates'], a41_h3['nonempty']))
