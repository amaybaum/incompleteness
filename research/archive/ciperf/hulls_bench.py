"""Track B act 41 -- the hull census of the index-map round (frozen with the control plane).

Act 36's 4x4 Dita hulls through the certified stratum point SIG, counted over every valid alignment of every 4x4
partition structure rather than at the sorted alignment alone. Everything is exact arithmetic in Python integers and
fractions. Its first part is act 36's probe head, verbatim, with act 36's second-order form; the census follows. It
prints its measurements as one canonical JSON object and replays them against the round's measurements.json when that
file is present. Its controls are the sorted-alignment regression values; the measured values are not pass conditions.
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
    print('  %s  %-58s %s' % ('PASS' if ok else 'FAIL', name, got if ok else '%s (expected %s)' % (got, want)))
    if not ok: fails.append(name)

t0 = time.time()
import numpy as np
import itertools
import random

def check(name, got, want):
    ok = got == want
    print('  %s  %-70s %s' % ('PASS' if ok else 'FAIL', name, got if ok else '%s (expected %s)' % (got, want)))
    if not ok: fails.append(name)
fails = []
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

# ---- exact linear algebra over Q --------------------------------------------------------------
def rref(rows, ncols):
    M = [[Fr(x) for x in r] for r in rows]; piv = []; r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]; M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]; M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        piv.append(c); r += 1
        if r == len(M): break
    return M[:r], piv
def rank(rows, ncols=None):
    """exact rank: rows of integers go through the fraction-free elimination rank_int (integer cross-multiplication
    with gcd normalization, no rational arithmetic), any other rows through the rational rref"""
    if not rows: return 0
    if (ncols is None or ncols == len(rows[0])) and all(type(x) is int for r in rows for x in r): return rank_int(rows)
    return len(rref(rows, ncols or len(rows[0]))[0])
def intvec(v):
    den = 1
    for x in v: den = den * x.denominator // gcd(den, x.denominator)
    w_ = [int(x * den) for x in v]; g = 0
    for x in w_: g = gcd(g, abs(x))
    return [x // g for x in w_] if g > 1 else w_
def nullspace(rows, ncols):
    Rr, piv = rref(rows, ncols); free = [c for c in range(ncols) if c not in piv]; out = []
    for f in free:
        v = [Fr(0)] * ncols; v[f] = Fr(1)
        for i, p in enumerate(piv): v[p] = -Rr[i][f]
        out.append(intvec(v))
    return out
def transpose(rows): return [list(c) for c in zip(*rows)]
def dot(u, v): return sum(a * b for a, b in zip(u, v))
def cvals(H):
    den = 1; C = {}
    for (i, j) in PAIRS:
        for k in range(N16):
            c = H[i][k] * H[j][k].conj()
            for x in (c.a, c.b): den = den * x.denominator // gcd(den, x.denominator)
    for (i, j) in PAIRS:
        C[(i, j)] = [(int(c.a * den), int(c.b * den)) for c in (H[i][k] * H[j][k].conj() for k in range(N16))]
    return C
def df_rows(C):
    rows = []
    for (i, j) in PAIRS:
        re = [0] * 256; im = [0] * 256
        for k, (a, b) in enumerate(C[(i, j)]):
            re[i * 16 + k] -= b; re[j * 16 + k] += b; im[i * 16 + k] += a; im[j * 16 + k] -= a
        rows.append(re); rows.append(im)
    return rows

print('== 1. the certified point, the named point and the exact line ==')
check('SIG is unitary (scaled)', is_unitary16(SIG), True)
check('u60 is a unit', U60.norm2(), Fr(1))
check('P = SIG ∘ u60^W is unitary (scaled)', is_unitary16(P), True)
C_SIG = cvals(SIG); DF = df_rows(C_SIG)
rkDF = rank(DF, 256)
check('rank DF at SIG', rkDF, 176); check('defect of SIG', 256 - rkDF - 31, 49)
check('defect of P', 256 - rank(df_rows(cvals(P)), 256) - 31, 37)
def straight_line_exact(w_):
    for (i, j) in PAIRS:
        sums = {}
        for k in range(16):
            d = w_[i * 16 + k] - w_[j * 16 + k]; a, b = C_SIG[(i, j)][k]
            s = sums.get(d, (0, 0)); sums[d] = (s[0] + a, s[1] + b)
        if any(s != (0, 0) for s in sums.values()): return False
    return True
check('W is an exact straight line at SIG (every level-set sum of the c_k vanishes, 120 pairs)', straight_line_exact(W), True)
Wbad = W[:]; Wbad[5] += 1
check('a one-entry perturbation of W is not a straight line (control)', straight_line_exact(Wbad), False)
check('W lies in ker DF', all(dot(r, W) == 0 for r in DF), True)
U5 = G(Fr(3, 5), Fr(4, 5))
P5 = [[SIG[i][j] * gpow(U5, W[i * 16 + j]) for j in range(16)] for i in range(16)]
check('the family at u = 1 is SIG entrywise (control)', [[SIG[i][j] * gpow(ONE, W[i * 16 + j]) for j in range(16)] for i in range(16)] == SIG, True)
check('u5 = (3+4i)/5 is a unit; the second frozen point Pu(u5) is unitary (scaled)', (U5.norm2(), is_unitary16(P5)), (Fr(1), True))
check('defect of Pu(u5)', 256 - rank(df_rows(cvals(P5)), 256) - 31, 37)
def gram(H, i, j, k): return H[i][j].conj() * H[i][k]
viol = [(a, b, b2, c, c2, d) for a in range(4) for b in range(4) for b2 in range(4) if b2 != b for c in range(4) for c2 in range(4) if c2 != c for d in range(4)
        if gram(P, 4 * a + b, 4 * c + d, 4 * c2 + d) * gram(P, 4 * a + b2, 4 * c2 + d, 4 * c + d) != G(1)]
check('cross-ratio violations of P over ordered (b,b\'),(c,c\') (identity value 1 scaled)', len(viol), 384)
check('the value at (a,b,b\',c,c\',d) = (0,0,1,0,1,0) is u60 (scaled; u60/256 in the frozen normalization)', gram(P, 0, 0, 4) * gram(P, 1, 4, 0) == U60, True)
print('  (%.0fs)' % (time.time() - t0))

print('== 2. Diţă factorizations by exhaustive search over block structures ==')
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
PT = [list(c) for c in zip(*P)]; SIGT = [list(c) for c in zip(*SIG)]; P5T = [list(c) for c in zip(*P5)]
FROZEN_28_BLOCKS = ((0, 1, 2, 3, 8, 9, 10, 11), (4, 5, 6, 7, 12, 13, 14, 15))
FROZEN_28_CLASSES = [(0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15)]
for (m, n), want_P, want_S in (((4, 4), (1, 0), (5, 4)), ((8, 2), (1, 0), (3, 2)), ((2, 8), (1, 1), (3, 3))):
    for kind, HP, HP5, HS in (('column', P, P5, SIG), ('row', PT, P5T, SIGT)):
        for pname, HX in (('P', HP), ('Pu(u5)', HP5)):
            oP = dita_orientations(HX, m, n)
            check('%s-Diţă %dx%d at %s: (candidates, exact factorizations)' % (kind, m, n, pname), (len(oP), sum(1 for o in oP if o[2])), want_P)
            if (m, n) == (2, 8):
                ex = [o for o in oP if o[2]]
                check('%s-Diţă 2x8 at %s: the frozen blocks and row classes' % (kind, pname), (ex[0][0], ex[0][1]) if ex else None, (FROZEN_28_BLOCKS, FROZEN_28_CLASSES))
        oS = dita_orientations(HS, m, n)
        check('%s-Diţă %dx%d at SIG = Pu(1): (candidates, exact factorizations) (control)' % (kind, m, n), (len(oS), sum(1 for o in oS if o[2])), want_S)
print('  (%.0fs)' % (time.time() - t0))

print('== 3. the first-order census at SIG: gauge, the fixed-pairing hulls, the residual, the cokernel ==')
def gauge_rows():
    out = []
    for i in range(16):
        v = [0] * 256
        for k in range(16): v[i * 16 + k] = 1
        out.append(v)
    for k in range(16):
        v = [0] * 256
        for i in range(16): v[i * 16 + k] = 1
        out.append(v)
    return out
GAUGE = gauge_rows()
def flat(v): return [x for r in v for x in r]
EX = [[1 if (a % 2 == 1 and c % 2 == 1) else 0 for c in range(4)] for a in range(4)]
Tvec = [flat([[EX[i // 4][j // 4] for j in range(16)] for i in range(16)])]
for c in range(4): Tvec.append(flat([[EX[i % 4][j % 4] if j // 4 == c else 0 for j in range(16)] for i in range(16)]))
for a in range(4): Tvec.append(flat([[EX[i % 4][j % 4] if i // 4 == a else 0 for j in range(16)] for i in range(16)]))
for c in range(4):
    for b in range(4): Tvec.append(flat([[1 if (j // 4 == c and i % 4 == b) else 0 for j in range(16)] for i in range(16)]))
for a in range(4):
    for d in range(4): Tvec.append(flat([[1 if (i // 4 == a and j % 4 == d) else 0 for j in range(16)] for i in range(16)]))
Tc = [Tvec[0]] + Tvec[1:5] + Tvec[9:25]; Tr = [Tvec[0]] + Tvec[5:9] + Tvec[25:41]
K = nullspace(DF, 256)
check('dim ker DF', len(K), 80); check('gauge rank', rank(GAUGE), 31)
check('T_c, T_r, T_c + T_r mod gauge', (rank(GAUGE + Tc) - 31, rank(GAUGE + Tr) - 31, rank(GAUGE + Tc + Tr) - 31), (14, 14, 26))
check('R = ker DF / (gauge + T): dim', 80 - rank(GAUGE + Tc + Tr), 23)
LN = nullspace(transpose(DF), 240)
check('coker DF: dim', len(LN), 64)
print('  (%.0fs)' % (time.time() - t0))

print('== 4. every 4x4 Diţă hull through SIG: orientations, factor circles, exact integrability, the span ==')
S4 = list(itertools.permutations(range(4)))
def deph(M):
    n = len(M); M = [[M[i][j] * M[i][0].conj() for j in range(n)] for i in range(n)]
    return [[M[i][j] * M[0][j].conj() for j in range(n)] for i in range(n)]
def key(M): return tuple(x.key() for r in M for x in r)
G4 = []
for i in range(4):
    v = [0] * 16
    for k in range(4): v[i * 4 + k] = 1
    G4.append(v)
for k in range(4):
    v = [0] * 16
    for i in range(4): v[i * 4 + k] = 1
    G4.append(v)
RG4, PG4 = rref(G4, 16)
def reduce_mod_gauge(d):
    v = [Fr(x) for x in d]
    for i, p in enumerate(PG4):
        if v[p] != 0:
            f = v[p]; v = [x - f * y for x, y in zip(v, RG4[i])]
    nz = next((x for x in v if x != 0), None)
    if nz is None: return None
    if nz < 0: v = [-x for x in v]
    return tuple(v)
CIRCLES = {}
def circle_directions(X):
    """memoized on the entries of X: the same factor recurs across the factorizations, and the search over the
    576 relabellings of each candidate Fourier matrix is a function of X alone"""
    kk = key(X)
    if kk not in CIRCLES: CIRCLES[kk] = circle_directions_(X)
    return CIRCLES[kk]
RELABELLINGS = {}
def relabellings(ak):
    """for the unit a: the dephased key of every relabelling (pi, tau) of F4(a), grouped by key in the order of
    S4 × S4; computed once per unit, since the same units recur across the factors"""
    if ak not in RELABELLINGS:
        Fa = F4(G(Fr(ak[0]), Fr(ak[1]))); by_key = {}
        for pi in S4:
            for tau in S4:
                M = [[Fa[pi[i]][tau[j]] for j in range(4)] for i in range(4)]
                by_key.setdefault(key(deph(M)), []).append((pi, tau))
        RELABELLINGS[ak] = by_key
    return RELABELLINGS[ak]
def circle_directions_(X):
    kX = key(deph(X)); dirs = {}; cands = set()
    for i in range(4):
        for j in range(4):
            for i2 in range(4):
                for j2 in range(4): cands.add((X[i][j] * X[i2][j2].conj()).key())
    for ak in cands:
        a = G(Fr(ak[0]), Fr(ak[1]))
        if a.norm2() != 1: continue
        for pi, tau in relabellings(ak).get(kX, ()):
            d = tuple(1 if (pi[i] % 2 == 1 and tau[j] % 2 == 1) else 0 for i in range(4) for j in range(4))
            r = reduce_mod_gauge(d)
            if r is not None and r not in dirs: dirs[r] = d
    return list(dirs.values())
def Q(v, u):
    out = []
    for (i, j) in PAIRS:
        re = 0; im = 0; ci = i * 16; cj = j * 16
        for k, (a, b) in enumerate(C_SIG[(i, j)]):
            p = (v[ci + k] - v[cj + k]) * (u[ci + k] - u[cj + k])
            if p: re += a * p; im += b * p
        out.append(re); out.append(im)
    return out
z240 = [0] * 240
IN_KER = {}
def in_ker_df(v):
    """v in ker DF, exact; memoized on the vector, since the hulls share most of their tangent vectors"""
    t = tuple(v)
    if t not in IN_KER:
        nz = [i for i, x in enumerate(v) if x]
        IN_KER[t] = all(sum(r[i] * v[i] for i in nz) == 0 for r in DF)
    return IN_KER[t]
Q_ZERO = {}
def q_zero(u, v):
    """Q(u, v) == 0, exact; Q is symmetric, so memoized on the unordered pair"""
    a, b = tuple(u), tuple(v)
    k = (a, b) if a <= b else (b, a)
    if k not in Q_ZERO: Q_ZERO[k] = Q(u, v) == z240
    return Q_ZERO[k]

# ---- A41: the 4x4 hull census through SIG under every alignment ---------------------------------------------------
# A 4x4 hull at a realizing index map and a choice of Fourier circle through X and through each Y_c is the family
# SIG o prod_k t_k^{v_k} over its twenty-one generating exponent vectors; as a set of matrices it is determined by the
# rational span of the v_k, and modulo the gauge by that span plus the gauge. Hulls are compared by those spans, exactly.
import hashlib, os
A41_RECORD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'programmes', 'oi-qm', 'track-b', 'act-41-index-map-semantics', 'measurements.json')
print('== A41-H1. every valid alignment of every 4x4 partition structure of SIG, in both orientations ==')
def a41_exact_at(H, cp, rows, m, n):
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    lam = {}; Y = []
    for c in range(m):
        Yc = []
        for b in range(n):
            i0 = row[(0, b)]; base = [H[i0][col[(c, d)]] for d in range(n)]; Yc.append(base)
            for a in range(m): lam[(a, b, c)] = H[row[(a, b)]][col[(c, 0)]] * base[0].conj()
        Y.append(Yc)
    if not all(lam[(a, b, c)] == lam[(a, 0, c)] * lam[(0, b, c)] for a in range(m) for b in range(n) for c in range(m)): return None
    X = [[lam[(a, 0, c)] for c in range(m)] for a in range(m)]
    if not (is_unitary_s(X, m) and all(is_unitary_s(Yc, n) for Yc in Y)): return None
    return X, Y, row, col
def a41_hull_vectors(kind, row, col, xi, etas):
    vecs = []
    v = [0] * 256
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4): v[row[(a, b)] * 16 + col[(c, d)]] = xi[a * 4 + c]
    vecs.append(v)
    for c in range(4):
        v = [0] * 256
        for a in range(4):
            for b in range(4):
                for d in range(4): v[row[(a, b)] * 16 + col[(c, d)]] = etas[c][b * 4 + d]
        vecs.append(v)
    for c in range(4):
        for b in range(4):
            v = [0] * 256
            for a in range(4):
                for d in range(4): v[row[(a, b)] * 16 + col[(c, d)]] = 1
            vecs.append(v)
    if kind == 'row': vecs = [[v[(mm % 16) * 16 + mm // 16] for mm in range(256)] for v in vecs]
    return vecs
A41_SORTED = tuple(range(4))
a41_sorted_agree = True
a41_params = 0; a41_sorted_params = 0; a41_gensets = {}; a41_per = []
for kind, H in (('column', SIG), ('row', SIGT)):
    for cp, rws, ok, _, _ in dita_orientations(H, 4, 4):
        nal = 0; npar = 0; sorted_valid = False
        for s in itertools.product(itertools.permutations(range(4)), repeat=3):
            rows = [rws[0]] + [tuple(rws[b + 1][s[b][a]] for a in range(4)) for b in range(3)]
            r = a41_exact_at(H, cp, rows, 4, 4)
            if r is None: continue
            nal += 1; is_sorted = all(x == A41_SORTED for x in s); sorted_valid = sorted_valid or is_sorted
            X, Y, row, col = r
            dX = circle_directions(X); dY = [circle_directions(Yc) for Yc in Y]
            for choice in itertools.product(dX, *dY):
                vecs = a41_hull_vectors(kind, row, col, choice[0], choice[1:])
                a41_params += 1; npar += 1; a41_sorted_params += is_sorted
                k = frozenset(tuple(v) for v in vecs)
                if k not in a41_gensets: a41_gensets[k] = [vecs, False]
                if is_sorted: a41_gensets[k][1] = True
        a41_per.append([kind, sorted(map(sorted, cp)), sorted(map(sorted, rws)), nal, npar])
        a41_sorted_agree = a41_sorted_agree and (sorted_valid == bool(ok))
check('control: for every 4x4 partition candidate of SIG, the sorted alignment is valid here exactly when act 36\'s search reports it exact', a41_sorted_agree, True)
print('  (%.0fs)' % (time.time() - t0))

print('== A41-H2. distinct hulls, exactly: as matrix families and modulo the gauge ==')
_tb_h2 = time.perf_counter()
def a41_canon(rows_):
    R_, P_ = rref([list(r) for r in rows_], 256)
    return tuple(tuple(r) for r in R_ if any(r))
a41_reps = list(a41_gensets.values())
a41_kmat = [a41_canon(v) for v, s in a41_reps]
a41_kcls = [a41_canon(GAUGE + v) for v, s in a41_reps]
a41_mat = {}; a41_cls = {}
for i, (km, kc) in enumerate(zip(a41_kmat, a41_kcls)):
    a41_mat.setdefault(km, i); a41_cls.setdefault(kc, i)
a41_map = {}
for km, kc in zip(a41_kmat, a41_kcls): a41_map.setdefault(km, set()).add(kc)
a41_bij = all(len(v) == 1 for v in a41_map.values()) and len({next(iter(v)) for v in a41_map.values()}) == len(a41_map) == len(a41_cls)
a41_sorted_mat = len({a41_kmat[i] for i, (v, s) in enumerate(a41_reps) if s}); a41_sorted_cls = len({a41_kcls[i] for i, (v, s) in enumerate(a41_reps) if s})

_t_old_h2 = time.perf_counter() - _tb_h2
# ---- benchmark: an independent integer Gauss-Jordan canonical form (not rank_int, no modular reduction) ----
import collections as _co
_types = _co.Counter(type(x).__name__ for v, s in a41_reps for r in v for x in r) + _co.Counter(type(x).__name__ for r in GAUGE for x in r)
def _gj_canon(rows_, ncols=256):
    M = []
    for r in rows_:
        if any(r):
            assert all(type(x) is int for x in r), 'non-int coefficient'
            M.append(list(r))
    piv = []; r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(M)) if M[i][c]), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        pr = M[r]; a = pr[c]
        for i in range(len(M)):
            if i != r and M[i][c]:
                b = M[i][c]
                row = [a * x - b * y for x, y in zip(M[i], pr)]
                g = 0
                for x in row:
                    if x: g = gcd(g, x)
                if g > 1: row = [x // g for x in row]
                M[i] = row
        piv.append(c); r += 1
        if r == len(M): break
    out = []
    for row, c in zip(M[:r], piv):
        g = 0
        for x in row:
            if x: g = gcd(g, x)
        row = [x // g for x in row]
        if row[c] < 0: row = [-x for x in row]
        out.append(tuple(row))
    return tuple(out)
def _primitive(key):
    out = []
    for row in key:
        den = 1
        for x in row: den = den * x.denominator // gcd(den, x.denominator)
        w_ = [int(x * den) for x in row]; g = 0
        for x in w_:
            if x: g = gcd(g, x)
        w_ = [x // g for x in w_]
        c = next(i for i, x in enumerate(w_) if x)
        if w_[c] < 0: w_ = [-x for x in w_]
        out.append(tuple(w_))
    return tuple(out)
_t0 = time.perf_counter()
_n_mat = [_gj_canon(v) for v, s in a41_reps]
_t_new_mat = time.perf_counter() - _t0
_t0 = time.perf_counter()
_n_cls = [_gj_canon(GAUGE + v) for v, s in a41_reps]
_t_new_cls = time.perf_counter() - _t0
_eq_mat = all(_n_mat[i] == _primitive(a41_kmat[i]) for i in range(len(a41_reps)))
_eq_cls = all(_n_cls[i] == _primitive(a41_kcls[i]) for i in range(len(a41_reps)))
_cnt = (len(set(_n_mat)), len(set(_n_cls)), len(a41_mat), len(a41_cls))
import json as _js
_res = {'reps': len(a41_reps), 'types': dict(_types), 'old_h2_s': _t_old_h2, 'new_mat_s': _t_new_mat, 'new_cls_s': _t_new_cls,
        'keys_equal_mat': _eq_mat, 'keys_equal_cls': _eq_cls, 'distinct_new_mat_new_cls_old_mat_old_cls': _cnt,
        'sorted_new': (len({_n_mat[i] for i, (v, s) in enumerate(a41_reps) if s}), len({_n_cls[i] for i, (v, s) in enumerate(a41_reps) if s})),
        'sorted_old': (a41_sorted_mat, a41_sorted_cls)}
print('H2BENCH', _js.dumps(_res, sort_keys=True))
open(os.path.join(os.environ['BENCH_OUT'], 'h2_bench.json'), 'w').write(_js.dumps(_res, indent=1, sort_keys=True))
sys.exit(0)
print('  (%.0fs)' % (time.time() - t0))
print('== A41-H3. a second equality test: buckets by a reduction modulo a prime, equality within buckets by exact joint rank ==')
A41_P = (1 << 61) - 1
def a41_rref_p(rows_):
    R_ = [[x % A41_P for x in r] for r in rows_]; out = []; col = 0; nr = len(R_)
    piv_rows = []
    for c in range(256):
        pr = next((i for i in range(len(piv_rows), nr) if R_[i][c]), None)
        if pr is None: continue
        k = len(piv_rows); R_[k], R_[pr] = R_[pr], R_[k]
        inv = pow(R_[k][c], A41_P - 2, A41_P); R_[k] = [(x * inv) % A41_P for x in R_[k]]
        for i in range(nr):
            if i != k and R_[i][c]:
                f = R_[i][c]; R_[i] = [(x - f * y) % A41_P for x, y in zip(R_[i], R_[k])]
        piv_rows.append(c)
    return tuple(tuple(r) for r in R_[:len(piv_rows)])
def a41_second_count(with_gauge):
    buckets = {}
    for i, (v, s) in enumerate(a41_reps): buckets.setdefault(a41_rref_p((GAUGE if with_gauge else []) + v), []).append(i)
    n = 0
    for idx in buckets.values():
        reps = []
        for i in idx:
            base = (GAUGE if with_gauge else []) + a41_reps[i][0]; r_i = rank(base)
            if not any(rank(base + a41_reps[j][0]) == r_i == rank((GAUGE if with_gauge else []) + a41_reps[j][0]) for j in reps): reps.append(i)
        n += len(reps)
    return n
a41_second = (a41_second_count(False), a41_second_count(True))
print('  (%.0fs)' % (time.time() - t0))
print('== A41-H4. every distinct hull: tangent dimension, ker DF, the second-order form; the combined span; W ==')
a41_dims = sorted(set(len(k) - 31 for k in a41_cls))
a41_dF = all(all(in_ker_df(v) for v in a41_reps[i][0]) and all(q_zero(u, w) for u in a41_reps[i][0] for w in a41_reps[i][0]) for i in a41_mat.values())
a41_span = rank(GAUGE + [v for i in a41_cls.values() for v in a41_reps[i][0]]) - 31
a41_W = sum(1 for i in a41_cls.values() if rank(GAUGE + a41_reps[i][0] + [list(W)]) == rank(GAUGE + a41_reps[i][0]))
check('the sorted control: the parametrizations at the sorted alignments are act 36\'s 492', a41_sorted_params, 492)
print('  (%.0fs)' % (time.time() - t0))
A41_OBJ = {'params': a41_params, 'sorted_params': a41_sorted_params, 'gensets': len(a41_reps), 'distinct_mat': len(a41_mat),
           'distinct_gauge': len(a41_cls), 'bijection': a41_bij, 'sorted_distinct_mat': a41_sorted_mat, 'sorted_distinct_gauge': a41_sorted_cls,
           'dims': a41_dims, 'dF_ok': a41_dF, 'span': a41_span, 'W_in': a41_W, 'second_test': list(a41_second), 'per_structure': a41_per}
A41_JSON = json.dumps(A41_OBJ, sort_keys=True, separators=(',', ':'))
print('A41-MEASUREMENTS hulls ' + A41_JSON)
print('A41-SHA256 hulls ' + hashlib.sha256(A41_JSON.encode()).hexdigest())
a41_mode = 'MEASURED'
if os.path.exists(A41_RECORD):
    rec = json.load(open(A41_RECORD, encoding='utf-8'))
    check('replay: the measurement equals the committed measurements.json, elementwise', json.loads(A41_JSON) == rec.get('hulls'), True)
    a41_mode = 'REPLAYED'
print()
if fails:
    print('dita_index_map_hulls: FAILED (%d): %s' % (len(fails), fails)); sys.exit(1)
print('dita_index_map_hulls: OK -- %s: %d parametrizations, %d distinct hulls as matrix families, %d modulo the gauge' % (a41_mode, a41_params, len(a41_mat), len(a41_cls)))
