"""probe7: the constants the A35 freeze carries, and the pure-Python exact-rank runtime.
(a) Bareiss exact rank (Python ints) timing at the fourth-root points and Gaussian-rational points
(b) RELAB: indices where the swapped-carrier relabelling of F4(i)⊗F4(i) violates the cross-ratio identity
(c) REAL2: the second real class: a 4-row witness sum, profile vs Sylvester, cross-ratio obstruction
(d) the witness as a hull point with varying Y_c, its cross value
(e) a deterministic census list of fourth-root Diţă points with exact invariants
(f) the exact hull tangent rank at the Gaussian-rational Σ point"""
import numpy as np, itertools, sys, time, json
from fractions import Fraction as Fr
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from lib35 import *

# ---- exact Gaussian-rational arithmetic and Bareiss rank ------------------------------------------
class G:
    __slots__ = ('a', 'b')
    def __init__(s, a, b=0): s.a = Fr(a); s.b = Fr(b)
    def __mul__(s, o): return G(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a)
    def conj(s): return G(s.a, -s.b)
    def __neg__(s): return G(-s.a, -s.b)
    def __add__(s, o): return G(s.a + o.a, s.b + o.b)
def rank_int(rows):
    """exact rank of an integer matrix (list of lists of ints) by fraction-free Gaussian elimination."""
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
                for x in M[i]: g = gcd(g, x) if x else g
                if g > 1: M[i] = [x // g for x in M[i]]
        r += 1
        if r == m: break
    return r
from math import gcd
def defect_system_int(H):
    """H: list of lists of G with a common denominator cleared: scale rows to integers."""
    n = len(H); rows = []
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
def defect_exact_G(H):
    n = len(H)
    return n * n - rank_int(defect_system_int(H)) - (2 * n - 1)
def F4G(z):
    one, m = G(1), G(-1)
    return [[one, one, one, one], [one, z, m, -z], [one, m, one, m], [one, -z, m, z]]
def ditaG(X, Ys, D):
    return [[X[i // 4][j // 4] * D[j // 4][i % 4] * Ys[j // 4][i % 4][j % 4] for j in range(16)] for i in range(16)]
I_ = G(0, 1); ONE = G(1)
def circleG(r, z):
    pi, tau = R[r]; F = F4G(z)
    return [[F[pi[i]][tau[j]] for j in range(4)] for i in range(4)]
def unitD(): return [[ONE] * 4 for _ in range(4)]

t0 = time.time()
print('== (a) exact defects, pure Python ==')
for name, X, Ys, D in (('H4⊗H4', circleG(0, ONE), [circleG(0, ONE)] * 4, unitD()),
                       ('F4⊗F4', circleG(0, I_), [circleG(0, I_)] * 4, unitD()),
                       ('H4⊗F4', circleG(0, ONE), [circleG(0, I_)] * 4, unitD()),
                       ('A34 witness (Y_c = F4(±i))', circleG(0, I_), [circleG(0, I_ if c % 2 == 0 else -I_) for c in range(4)], unitD())):
    t1 = time.time(); print('  %-28s defect %3d  (%.1fs)' % (name, defect_exact_G(ditaG(X, Ys, D)), time.time() - t1))
z = G(Fr(3, 5), Fr(4, 5)); w = G(Fr(5, 13), Fr(12, 13))
t1 = time.time(); print('  %-28s defect %3d  (%.1fs)' % ('Σ rational point', defect_exact_G(ditaG(F4G(z), [F4G(w)] * 4, unitD())), time.time() - t1))
ph = [G(Fr(3, 5), Fr(4, 5)), G(Fr(5, 13), Fr(12, 13)), G(Fr(8, 17), Fr(15, 17)), G(Fr(7, 25), Fr(24, 25)), G(Fr(20, 29), Fr(21, 29)), G(Fr(12, 37), Fr(35, 37)), G(Fr(9, 40), Fr(40, 41)) if False else G(Fr(9, 41), Fr(40, 41)), G(Fr(28, 53), Fr(45, 53)), G(Fr(11, 61), Fr(60, 61))]
D9 = unitD(); k = 0
for c in range(1, 4):
    for b in range(1, 4):
        D9[c][b] = ph[k]; k += 1
t1 = time.time(); print('  %-28s defect %3d  (%.1fs)' % ('Diţă, nine rational phases', defect_exact_G(ditaG(F4G(z), [F4G(w)] * 4, D9)), time.time() - t1))
# a cheaper Diţă point: fourth-root factors, twist phases powers of (3+4i)/5
p5 = G(Fr(3, 5), Fr(4, 5)); pw = [ONE]
for _ in range(9): pw.append(pw[-1] * p5)
D5 = unitD(); k = 1
for c in range(1, 4):
    for b in range(1, 4):
        D5[c][b] = pw[k]; k += 1
t1 = time.time(); print('  %-28s defect %3d  (%.1fs)' % ('Diţă, twists (3+4i)^k/5^k', defect_exact_G(ditaG(circleG(0, I_), [circleG(0, I_)] * 4, D5)), time.time() - t1))
# second real class
Dr = unitD(); Dr[3][3] = G(-1)
t1 = time.time(); Hr = ditaG(circleG(0, ONE), [circleG(0, ONE)] * 4, Dr); print('  %-28s defect %3d  (%.1fs)' % ('second real class', defect_exact_G(Hr), time.time() - t1))

print('== (b) RELAB ==')
Fi = F4(1j); P = kron(Fi, Fi)
sig = list(range(16)); sig[1], sig[4] = sig[4], sig[1]   # swap carrier points (0,1) <-> (1,0): indices 1 and 4
Pr = P[np.ix_(sig, sig)]
def gram(H): return np.conj(H)[:, :, None] * H[:, None, :]
Gp = gram(Pr)
def cross_val(Gm, a, b, bp, c, cp, d):
    return Gm[4 * a + b, 4 * c + d, 4 * cp + d] * Gm[4 * a + bp, 4 * cp + d, 4 * c + d]
found = None
for a, b, bp, c, cp, d in itertools.product(range(4), repeat=6):
    if b == bp or c == cp: continue
    v = cross_val(Gp, a, b, bp, c, cp, d)
    if abs(v - 1 / 256) > 1e-9: found = (a, b, bp, c, cp, d, v * 256); break
print('  relabelled F4⊗F4 (rows+cols swap 1<->4): first violating (a,b,b\',c,c\',d) and 256*value:', found)
print('  sigma_residual of the relabelled point: %.3f; of the point: %.1e' % (sigma_residual(Pr), sigma_residual(P)))
# is Pr equal (up to phases) to a Kronecker product with the swapped pairing? no need.

print('== (c) REAL2 ==')
H4 = F4(1); Drn = np.ones((4, 4)); Drn[3, 3] = -1
Hrn = dita(H4, [H4] * 4, Drn)
assert np.allclose(Hrn.imag, 0) and is_unitary(Hrn)
Hs = Hrn.real * 4
ws = None
for a, b, c, d in itertools.combinations(range(16), 4):
    s = int(round(np.sum(Hs[a] * Hs[b] * Hs[c] * Hs[d])))
    if abs(s) == 8: ws = (a, b, c, d, s); break
print('  first 4-row subset of the second real class with |sum| = 8 (scaled entries ±1):', ws)
sy = kron(H4, H4).real * 4
vals = sorted({abs(int(round(np.sum(sy[a] * sy[b] * sy[c] * sy[d])))) for a, b, c, d in itertools.combinations(range(16), 4)})
print('  Sylvester 4-row |sums| take the values', vals, '; second class:', sorted({abs(int(round(np.sum(Hs[a] * Hs[b] * Hs[c] * Hs[d])))) for a, b, c, d in itertools.combinations(range(16), 4)}))
Gr = gram(Hrn); found = None
for a, b, bp, c, cp, d in itertools.product(range(4), repeat=6):
    if b == bp or c == cp: continue
    v = cross_val(Gr, a, b, bp, c, cp, d)
    if abs(v - 1 / 256) > 1e-9: found = (a, b, bp, c, cp, d, v * 256); break
print('  second real class: first violating cross indices and 256*value:', found)

print('== (d) witness ==')
Hw34 = np.array([[0.25 * F4(1j)[i // 4, j // 4] * F4(1j if (j // 4) % 2 == 0 else -1j)[i % 4, j % 4] * 4 for j in range(16)] for i in range(16)])
Hw = dita(Fi, [F4(1j if c % 2 == 0 else -1j) for c in range(4)], np.ones((4, 4)))
print('  A34 H == dita(F4(i), Y_c = F4(±i), D = 1):', np.allclose(Hw34, Hw), '; 256 * cross value at (0,1,0,0,1,1):', np.round(cross_val(gram(Hw), 0, 1, 0, 0, 1, 1) * 256, 6))

print('== (e) census list ==')
rng = np.random.default_rng(3535)
roots = np.array([1, 1j, -1, -1j]); rootsG = [ONE, I_, G(-1), -I_]
kron_inv = {}
for nm, X, Ys in (('H4⊗H4', circleG(0, ONE), [circleG(0, ONE)] * 4), ('H4⊗F4', circleG(0, ONE), [circleG(0, I_)] * 4), ('F4⊗H4', circleG(0, I_), [circleG(0, ONE)] * 4), ('F4⊗F4', circleG(0, I_), [circleG(0, I_)] * 4)):
    Hn = np.array([[complex(float(x.a), float(x.b)) for x in row] for row in ditaG(X, Ys, unitD())]) / 4
    kron_inv[nm] = (profile(Hn), haagerup_set(Hn), defect_exact_G(ditaG(X, Ys, unitD())))
census = []; seen = set(); tries = 0
while len(census) < 20 and tries < 200:
    tries += 1
    rX, zX = int(rng.integers(0, 9)), int(rng.integers(0, 4))
    rY = [int(x) for x in rng.integers(0, 9, 4)]; zY = [int(x) for x in rng.integers(0, 4, 4)]
    bits = [[0] * 4 for _ in range(4)]
    for c in range(1, 4):
        for b in range(1, 4): bits[c][b] = int(rng.integers(0, 4))
    X = circleG(rX, rootsG[zX]); Ys = [circleG(rY[c], rootsG[zY[c]]) for c in range(4)]
    D = [[rootsG[bits[c][b]] for b in range(4)] for c in range(4)]
    HG = ditaG(X, Ys, D)
    Hn = np.array([[complex(float(x.a), float(x.b)) for x in row] for row in HG]) / 4
    assert is_unitary(Hn)
    d = defect_exact_G(HG)
    inv = (profile(Hn), haagerup_set(Hn), d)
    if inv in seen or inv in kron_inv.values(): continue
    seen.add(inv)
    census.append({'X': [rX, zX], 'Y': [[rY[c], zY[c]] for c in range(4)], 'D': bits, 'defect': d,
                   'haagerup': sorted(list(x) for x in inv[1]), 'profile_values': sorted(set(inv[0]))})
print('  %d distinct census points in %d tries; defects %s' % (len(census), tries, [c['defect'] for c in census]))
print('  Kronecker fourth-root classes:', {k: v[2] for k, v in kron_inv.items()}, '(%.0fs)' % (time.time() - t0))
json.dump(census, open(__file__.rsplit('/', 1)[0] + '/census35.json', 'w'), indent=1)

print('== (f) exact hull tangent rank at the rational Σ point ==')
# tangent directions as integer 16x16 matrices: gauge (32), X's z-exponent pattern, Y_c's, D[c,b] and E[a,d] indicators, Y_a's (row)
def expo(pi, tau):  # d arg F4(z)[pi a, tau c] / d theta = 1 where the entry carries z or -z (rows 1,3 & cols 1,3 of the unrelabelled matrix)
    return [[1 if (pi[a] % 2 == 1 and tau[c] % 2 == 1) else 0 for c in range(4)] for a in range(4)]
vecs = []
for i in range(16):
    v = [[0] * 16 for _ in range(16)]
    for k in range(16): v[i][k] = 1
    vecs.append(v)
    v = [[0] * 16 for _ in range(16)]
    for k in range(16): v[k][i] = 1
    vecs.append(v)
ex = expo(ID4, ID4)
vecs.append([[ex[i // 4][j // 4] for j in range(16)] for i in range(16)])           # X parameter
for c in range(4): vecs.append([[ex[i % 4][j % 4] if j // 4 == c else 0 for j in range(16)] for i in range(16)])   # Y_c (column construction)
for a in range(4): vecs.append([[ex[i % 4][j % 4] if i // 4 == a else 0 for j in range(16)] for i in range(16)])   # Y_a (row construction)
for c in range(4):
    for b in range(4): vecs.append([[1 if (j // 4 == c and i % 4 == b) else 0 for j in range(16)] for i in range(16)])
for a in range(4):
    for d in range(4): vecs.append([[1 if (i // 4 == a and j % 4 == d) else 0 for j in range(16)] for i in range(16)])
rows = [[x for r in v for x in r] for v in vecs]
rk = rank_int(rows); rk_g = rank_int(rows[:32])
print('  rank of gauge + Σ + both hulls: %d; gauge alone: %d; hull tangent rank modulo phases: %d' % (rk, rk_g, rk - rk_g))
print('(%.0fs)' % (time.time() - t0))
