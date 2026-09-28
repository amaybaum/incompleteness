"""Track B act 35 -- the exact-computation probe of the Diţă-hull round (frozen with the control plane).

Everything here is exact arithmetic over the Gaussian rationals in Python integers and fractions:
ranks by fraction-free elimination, invariants of fourth-root matrices as Gaussian integers. numpy
is used only in the two enumerations at the end: the grid action of the matrix-induced isometries,
where classes are identified by a distance that is zero or at least 1/5 on the finite set
concerned, and the stabilizers, in integer exponent arithmetic on fourth-root matrices, exact. The probe asserts the preregistered values and exits 1 on any mismatch;
it certifies nothing on its own beyond the arithmetic it replays.

Objects (acts 24-34, numbers as in the landed Lean):
  F4(z)      (1/2) [[1,1,1,1],[1,z,-1,-z],[1,-1,1,-1],[1,-z,-1,z]]
  circle r   U_r(z)[i,j] = F4(z)[pi_r i, tau_r j], with act 33's table R of nine (pi, tau)
  dita       H[(a,b),(c,d)] = X[a,c] * D[c,b] * Y_c[b,d]   (index (a,b) -> 4a+b)
  defect     16^2 - rank(L) - 31, L the real linear system  sum_k (R_ik - R_jk) H_ik conj(H_jk) = 0, i<j
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
def fourth_root_exponents(H):
    """the exponent matrix E with H = i^E entrywise, or None when some entry is not a fourth root of unity"""
    E = []
    for row in H:
        r = []
        for x in row:
            if x not in ROOTS: return None
            r.append(ROOTS.index(x))
        E.append(r)
    return E
def profile_of_exponents(E):
    """the four-row profile of H = i^E: each term H_pk conj(H_qk) H_rk conj(H_tk) is i^(E_pk - E_qk + E_rk - E_tk), so the
    sum over k is (n0 - n2) + (n1 - n3) i with n_j the number of k at residue j, and its squared modulus is the integer
    (n0 - n2)^2 + (n1 - n3)^2; returned as the same Fraction values the Gaussian-rational path produces"""
    vals = []
    for a, b, c, d in itertools.combinations(range(16), 4):
        trip = []
        for (p, q, r, t) in ((a, b, c, d), (a, c, b, d), (a, b, d, c)):
            n = [0, 0, 0, 0]
            for k in range(16): n[(E[p][k] - E[q][k] + E[r][k] - E[t][k]) & 3] += 1
            trip.append(Fr((n[0] - n[2]) ** 2 + (n[1] - n[3]) ** 2))
        vals.append(tuple(sorted(trip)))
    return tuple(sorted(vals))
def profile(H):
    """the four-row profile: for each 4-subset of rows the sorted triple of |sum_k H_ak conj(H_bk) H_ck conj(H_dk)|^2
    over the three ways of choosing which two rows are conjugated, as a multiset over the subsets
    (entries scaled by 4). Invariant under row and column permutations, phases and conjugation;
    the transpose gives the column profile, so the census invariant carries both.
    A matrix of fourth roots of unity takes the integer exponent-count path; any other matrix the
    Gaussian-rational path below."""
    E = fourth_root_exponents(H)
    if E is not None: return profile_of_exponents(E)
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
print('== 1. the defect strata (exact ranks) ==')
z = G(Fr(3, 5), Fr(4, 5)); w = G(Fr(5, 13), Fr(12, 13))
PH = [G(Fr(3, 5), Fr(4, 5)), G(Fr(5, 13), Fr(12, 13)), G(Fr(8, 17), Fr(15, 17)), G(Fr(7, 25), Fr(24, 25)), G(Fr(20, 29), Fr(21, 29)), G(Fr(12, 37), Fr(35, 37)), G(Fr(9, 41), Fr(40, 41)), G(Fr(28, 53), Fr(45, 53)), G(Fr(11, 61), Fr(60, 61))]
D9 = unitD(); k = 0
for c in range(1, 4):
    for b in range(1, 4): D9[c][b] = PH[k]; k += 1
Dw = unitD(); Dw[1] = [ONE, I_, ONE, -I_]
Dr = unitD(); Dr[3][3] = G(-1)
H4H4 = kron(circle(0, ONE), circle(0, ONE)); H4F4 = kron(circle(0, ONE), circle(0, I_)); F4F4 = kron(circle(0, I_), circle(0, I_))
H34 = dita(circle(0, I_), [circle(0, I_ if c % 2 == 0 else -I_) for c in range(4)], unitD())
HW = dita(circle(0, I_), [circle(0, I_)] * 4, Dw)
HR = dita(circle(0, ONE), [circle(0, ONE)] * 4, Dr)
SIG = kron(F4(z), F4(w))
DIT = dita(F4(z), [F4(w)] * 4, D9)
for name, H, want in (('H4⊗H4, the vertex-vertex point', H4H4, 105), ('H4⊗F4, vertex times Fourier', H4F4, 73), ('F4⊗F4', F4F4, 57),
                      ("act 34's witness H (Y_c = F4(±i), D = 1)", H34, 57), ('the twisted point Hw (D[1,:] = (1,i,1,-i))', HW, 49),
                      ('the second real class Hr (D[3][3] = -1)', HR, 105), ('Σ at z=(3+4i)/5, w=(5+12i)/13', SIG, 49),
                      ('Diţă point, nine distinct rational twists', DIT, 17)):
    check('defect of %s' % name, defect(H), want)
# controls: the gauge directions are null directions; a non-unitary matrix is refused
rows = defect_rows(F4F4)
check('the 31 phase directions lie in the null space at F4⊗F4', all(sum(r[i] * v[i] for i in range(256)) == 0 for r in rows for v in gauge_rows()) and rank_int(gauge_rows()) == 31, True)
bad = [row[:] for row in F4F4]; bad[0][0] = -bad[0][0]
try:
    defect(bad); refused = False
except AssertionError:
    refused = True
check('a sign-flipped F4⊗F4 is refused as non-unitary', refused, True)
print('  (%.0fs)' % (time.time() - t0))

print('== 2. the open modulus: hull tangent rank against the defect at the rational Σ point ==')
def expo(pi, tau): return [[1 if (pi[a] % 2 == 1 and tau[c] % 2 == 1) else 0 for c in range(4)] for a in range(4)]
vecs = [v[:] for v in gauge_rows()]
ex = expo(ID4, ID4)
def flat(v): return [x for r in v for x in r]
vecs.append(flat([[ex[i // 4][j // 4] for j in range(16)] for i in range(16)]))
for c in range(4): vecs.append(flat([[ex[i % 4][j % 4] if j // 4 == c else 0 for j in range(16)] for i in range(16)]))
for a in range(4): vecs.append(flat([[ex[i % 4][j % 4] if i // 4 == a else 0 for j in range(16)] for i in range(16)]))
for c in range(4):
    for b in range(4): vecs.append(flat([[1 if (j // 4 == c and i % 4 == b) else 0 for j in range(16)] for i in range(16)]))
for a in range(4):
    for d in range(4): vecs.append(flat([[1 if (i // 4 == a and j % 4 == d) else 0 for j in range(16)] for i in range(16)]))
hull_rank = rank_int(vecs) - 31
check('tangent rank of the two hulls modulo phases at the Σ point', hull_rank, 26)
DEF_SIG = defect_rows(SIG)
def in_defect_space(v): return all(sum(r_k * v_k for r_k, v_k in zip(r, v)) == 0 for r in DEF_SIG)
check('every hull tangent lies in the defect space at the Σ point (each of the %d tangent and gauge vectors against each of the %d defect equations)' % (len(vecs), len(DEF_SIG)), all(in_defect_space(v) for v in vecs), True)
check('a single-entry phase direction is not in the defect space at the Σ point (control)', in_defect_space([1] + [0] * 255), False)
print('  the frozen countercontrol of the open modulus: hull tangent rank %d != defect %d at the Σ point (both exact)' % (hull_rank, defect(SIG)))
check('the hulls do not exhaust the defect space (26 < 49)', hull_rank < defect(SIG), True)

print('== 3. the census: fourth-root points of the column hull off the Kronecker locus ==')
CENSUS = [{"X":[0,3],"Y":[[5,1],[7,1],[1,2],[1,0]],"D":[[0,0,0,0],[0,3,3,1],[0,1,0,0],[0,1,2,2]],"defect":41},{"X":[8,0],"Y":[[3,1],[3,0],[1,3],[7,3]],"D":[[0,0,0,0],[0,2,1,2],[0,0,3,1],[0,3,0,1]],"defect":51},{"X":[5,0],"Y":[[8,3],[5,0],[4,3],[0,3]],"D":[[0,0,0,0],[0,0,0,2],[0,1,1,2],[0,0,1,1]],"defect":55},{"X":[7,1],"Y":[[3,0],[8,1],[2,0],[4,0]],"D":[[0,0,0,0],[0,0,3,2],[0,1,1,2],[0,3,1,2]],"defect":39},{"X":[5,2],"Y":[[2,2],[1,0],[6,3],[0,0]],"D":[[0,0,0,0],[0,1,3,1],[0,0,3,1],[0,1,0,3]],"defect":59},{"X":[2,1],"Y":[[7,1],[1,0],[3,1],[6,0]],"D":[[0,0,0,0],[0,3,2,0],[0,3,3,2],[0,3,0,3]],"defect":33},{"X":[4,3],"Y":[[1,3],[0,3],[4,2],[7,3]],"D":[[0,0,0,0],[0,0,3,3],[0,1,1,1],[0,2,3,3]],"defect":27},{"X":[3,1],"Y":[[7,3],[7,1],[5,2],[0,2]],"D":[[0,0,0,0],[0,2,1,2],[0,2,2,0],[0,0,1,2]],"defect":53},{"X":[3,0],"Y":[[0,2],[5,2],[3,0],[7,1]],"D":[[0,0,0,0],[0,2,0,3],[0,2,3,0],[0,0,2,3]],"defect":67},{"X":[8,3],"Y":[[8,0],[3,0],[8,0],[4,2]],"D":[[0,0,0,0],[0,2,1,2],[0,1,0,0],[0,2,3,2]],"defect":47},{"X":[3,0],"Y":[[3,0],[3,1],[1,3],[4,1]],"D":[[0,0,0,0],[0,0,1,3],[0,0,3,2],[0,2,1,3]],"defect":47},{"X":[0,2],"Y":[[2,3],[6,3],[2,3],[1,1]],"D":[[0,0,0,0],[0,3,2,1],[0,2,3,1],[0,0,2,1]],"defect":45},{"X":[0,2],"Y":[[2,2],[1,1],[5,0],[4,3]],"D":[[0,0,0,0],[0,1,2,0],[0,3,3,2],[0,0,2,1]],"defect":53},{"X":[2,0],"Y":[[7,2],[3,3],[1,2],[6,2]],"D":[[0,0,0,0],[0,1,3,3],[0,2,0,2],[0,2,3,1]],"defect":63},{"X":[7,0],"Y":[[8,0],[6,3],[1,2],[6,1]],"D":[[0,0,0,0],[0,1,2,2],[0,3,3,1],[0,1,1,0]],"defect":53},{"X":[1,1],"Y":[[7,0],[5,1],[8,0],[3,1]],"D":[[0,0,0,0],[0,2,0,2],[0,1,0,1],[0,2,3,1]],"defect":37},{"X":[3,2],"Y":[[2,0],[7,1],[7,2],[7,1]],"D":[[0,0,0,0],[0,0,0,1],[0,1,0,0],[0,0,2,1]],"defect":51},{"X":[6,3],"Y":[[6,0],[0,2],[3,3],[8,0]],"D":[[0,0,0,0],[0,0,2,3],[0,0,3,3],[0,1,1,2]],"defect":37},{"X":[0,3],"Y":[[8,2],[3,3],[6,3],[2,0]],"D":[[0,0,0,0],[0,2,3,3],[0,0,1,0],[0,1,1,2]],"defect":33},{"X":[8,0],"Y":[[6,2],[3,3],[0,1],[7,0]],"D":[[0,0,0,0],[0,1,0,2],[0,1,1,3],[0,1,1,1]],"defect":55}]
kron_inv = {}
for nm, X, Ys in (('H4⊗H4', circle(0, ONE), [circle(0, ONE)] * 4), ('H4⊗F4', circle(0, ONE), [circle(0, I_)] * 4),
                  ('F4⊗H4', circle(0, I_), [circle(0, ONE)] * 4), ('F4⊗F4', circle(0, I_), [circle(0, I_)] * 4)):
    H = dita(X, Ys, unitD()); kron_inv[nm] = (profile2(H), haagerup(H), defect(H))
check('the four Kronecker fourth-root points give three invariant triples (the swap identifies the middle two)', len(set(kron_inv.values())), 3)
seen = {}
for n_, c in enumerate(CENSUS):
    X = circle(c['X'][0], ROOTS[c['X'][1]]); Ys = [circle(r, ROOTS[zz]) for r, zz in c['Y']]
    D = [[ROOTS[c['D'][cc][b]] for b in range(4)] for cc in range(4)]
    H = dita(X, Ys, D)
    d = defect(H); inv = (profile2(H), haagerup(H), d)
    if d != c['defect']: fails.append('census %d defect %d != %d' % (n_, d, c['defect']))
    if inv in kron_inv.values(): fails.append('census %d coincides with a Kronecker class' % n_)
    seen.setdefault(inv, []).append(n_)
check('census points with the preregistered exact defects', all('census %d defect' % n_ not in ' '.join(fails) for n_ in range(len(CENSUS))), True)
check('census points pairwise distinct by (profile pair, Haagerup set, defect)', len(seen), len(CENSUS))
check('no census point shares its triple with a Kronecker class', all(inv not in kron_inv.values() for inv in seen), True)
print('  defects: %s' % sorted(c['defect'] for c in CENSUS))
print('  (%.0fs)' % (time.time() - t0))

print("== 4. act 34's witness, the twisted point and the two real classes ==")
rho = [4 * c + (d if c % 2 == 0 else {0: 0, 1: 3, 2: 2, 3: 1}[d]) for c in range(4) for d in range(4)]
check("act 34's witness is exactly F4⊗F4 with the columns relabelled by ρ", all(H34[i][j] == F4F4[i][rho[j]] for i in range(16) for j in range(16)), True)
check("act 34's witness has the invariant triple of F4⊗F4", (profile2(H34), haagerup(H34), defect(H34)) == kron_inv['F4⊗F4'], True)
check('the twisted point Hw has a different profile pair from F4⊗F4', profile2(HW) != profile2(F4F4), True)
check('the profile values of F4⊗F4 (squared) are {0, 256}', pvalues(F4F4), {0, 256})
check('the profile of Hw contains the value 64', 64 in pvalues(HW), True)
check('Sylvester H4⊗H4: profile values {0, 256}', pvalues(H4H4), {0, 256})
check('the second real class: profile values {0, 64, 256}', pvalues(HR), {0, 64, 256})
check('the second real class is real', all(x.b == 0 for row in HR for x in row), True)
check('the second real class has the defect of Sylvester (the defect does not separate them)', defect(HR), 105)
# invariance controls: a product relabelling, conjugation and transpose leave the triple of a census point unchanged
X = circle(CENSUS[0]['X'][0], ROOTS[CENSUS[0]['X'][1]]); Ys = [circle(r, ROOTS[zz]) for r, zz in CENSUS[0]['Y']]
D = [[ROOTS[CENSUS[0]['D'][cc][b]] for b in range(4)] for cc in range(4)]
H0 = dita(X, Ys, D); inv0 = (profile2(H0), haagerup(H0), defect(H0))
pi = [4 * ((a + 1) % 4) + ((b + 2) % 4) for a in range(4) for b in range(4)]; tau = [4 * ((c + 3) % 4) + ((d + 1) % 4) for c in range(4) for d in range(4)]
H1 = relabel(H0, pi, tau, cj=True, tr=True)
check('the triple is invariant under a product relabelling with conjugation and transpose', (profile2(H1), haagerup(H1), defect(H1)), inv0)
print('  (%.0fs)' % (time.time() - t0))

print("== 5. the matrix-induced part of act 33's group on the eighth-root grid (numerical identification of exact classes) ==")
import numpy as np
V1 = [0, 2, 4, 2, 0, 3, 4, 5, 0]; V2 = [1, 3, 5, 5, 4, 1, 3, 1, 2]
def F4n(zz): return 0.5 * np.array([[1, 1, 1, 1], [1, zz, -1, -zz], [1, -1, 1, -1], [1, -zz, -1, zz]], dtype=complex)
def Un(r, zz):
    pi_, tau_ = R[r]; F = F4n(zz); return np.array([[F[pi_[i], tau_[j]] for j in range(4)] for i in range(4)])
def inner(U, Up):
    W = U * np.conj(Up); A = W.T @ np.conj(W); return np.trace(A @ A @ A)
def dist2(U, Up): return (inner(U, U) + inner(Up, Up) - 2 * inner(U, Up).real).real
K = 8
def key(r, kk):
    if kk == 0: return ('v', V1[r])
    if kk == K // 2: return ('v', V2[r])
    return (r, kk)
grid = sorted({key(r, kk) for r in range(9) for kk in range(K)}, key=str); gidx = {g: n for n, g in enumerate(grid)}
zk = lambda kk: np.exp(2j * np.pi * kk / K)
def U_of(g):
    if g[0] == 'v':
        return Un(V1.index(g[1]), 1) if g[1] in V1 else Un(V2.index(g[1]), -1)
    return Un(g[0], zk(g[1]))
Ugrid = {g: U_of(g) for g in grid}
check('the grid has 60 classes', len(grid), 60)
mind = min(dist2(Ugrid[g], Ugrid[h]) for g in grid for h in grid if g != h)
check('distinct grid classes are at squared distance at least 1/5 (the eighth-root neighbours sit at 3(1 - cos 45°)/4)', mind > 0.2, True)
def locate(U):
    for g, Ug in Ugrid.items():
        if dist2(U, Ug) < 1e-8: return g
    raise AssertionError('off the grid')
def perm_of(op): return tuple(gidx[locate(op(Ugrid[g]))] for g in grid)
ops = {'pi=(01)': lambda U: U[np.ix_(swap(0, 1), ID4)], 'pi=(0123)': lambda U: U[np.ix_((1, 2, 3, 0), ID4)],
       'tau=(01)': lambda U: U[np.ix_(ID4, swap(0, 1))], 'tau=(0123)': lambda U: U[np.ix_(ID4, (1, 2, 3, 0))],
       'conj': lambda U: np.conj(U), 'transpose': lambda U: U.T}
P = {n: perm_of(op) for n, op in ops.items()}
def comp(p, q): return tuple(p[i] for i in q)
def closure(gens):
    start = tuple(range(60)); seen = {start}; frontier = [start]
    while frontier:
        nxt = []
        for p in frontier:
            for g in gens:
                r = comp(g, p)
                if r not in seen: seen.add(r); nxt.append(r)
        frontier = nxt
    return seen
rel = closure([P[n] for n in P if n.startswith('pi') or n.startswith('tau')]); relc = closure([P[n] for n in P if n != 'transpose']); mat = closure(list(P.values()))
check('relabellings alone: 576 grid permutations', len(rel), 576)
check('relabellings and conjugation: 1152', len(relc), 1152)
check('relabellings, conjugation and transpose: 2304', len(mat), 2304)
edges = [(V1[r], V2[r]) for r in range(9)]
def circle_of(u, v):
    for s in range(9):
        if {V1[s], V2[s]} == {u, v}: return s
autos = [nu for nu in itertools.permutations(range(6)) if all(circle_of(nu[u], nu[v]) is not None for u, v in edges)]
def a33(nu, eps):
    img = []
    for g in grid:
        if g[0] == 'v': img.append(gidx[('v', nu[g[1]])]); continue
        r, kk = g; s = circle_of(nu[V1[r]], nu[V2[r]]); k2 = kk if eps[r] else (-kk) % K
        img.append(gidx[key(s, k2)] if nu[V1[r]] == V1[s] else gidx[key(s, (k2 + K // 2) % K)])
    return tuple(img)
idn = tuple(range(6))
ker = [e for e in itertools.product([True, False], repeat=9) if a33(idn, e) in mat]
img = [nu for nu in autos if any(a33(nu, e) in mat for e in itertools.product([True, False], repeat=9))]
check('image of the matrix-induced subgroup in Aut(K3,3)', len(img), 72)
check('kernel of the matrix-induced subgroup: conjugation-bit patterns', len(ker), 32)
check("index of the matrix-induced subgroup in act 33's group", 36864 // len(mat), 16)
check('a single-circle conjugation bit is not matrix-induced', a33(idn, tuple(r != 0 for r in range(9))) in mat, False)
check('the global conjugation (all bits) is matrix-induced', a33(idn, (False,) * 9) in mat, True)
print('  (%.0fs)' % (time.time() - t0))

print('== 6. stabilizers in the extendable group G_ext (product relabellings, swap, conjugation, transpose; order 2654208) ==')
def expo_matrix(H):
    """the exponent matrix E with H = i^E entrywise (H scaled by 4), for a matrix whose entries are fourth roots of unity; exact"""
    E = []
    for row in H:
        r = []
        for x in row:
            assert x in ROOTS, 'entry is not a fourth root of unity'
            r.append(ROOTS.index(x))
        E.append(r)
    return np.array(E, dtype=np.int64)
def dephase_e(E):
    """divide each row by its first entry and then each column by its first entry, on exponents mod 4; exact"""
    E = E - E[..., :, :1]
    E = E - E[..., :1, :]
    return E % 4
S4 = list(itertools.permutations(range(4)))
def prod_perm(p, q): return [4 * p[a] + q[b] for a in range(4) for b in range(4)]
SW = [4 * b + a for a in range(4) for b in range(4)]
col_perms = np.array([prod_perm(t1, t2) for t1 in S4 for t2 in S4])
def stabilizer(E0):
    """the number of elements of G_ext fixing the dephased class of i^E0; integer exponent arithmetic throughout"""
    c0 = dephase_e(E0); count = 0
    for sw in (False, True):
        for cj in (False, True):
            for tr in (False, True):
                E1 = E0.copy()
                if sw: E1 = E1[np.ix_(SW, SW)]
                if cj: E1 = (-E1) % 4
                if tr: E1 = E1.T
                for p1 in S4:
                    for p2 in S4:
                        B = E1[prod_perm(p1, p2), :][:, col_perms]; B = np.transpose(B, (1, 0, 2))
                        B = dephase_e(B)
                        count += int((B == c0).all(axis=(1, 2)).sum())
    return count
STAB_F4F4, STAB_HW = stabilizer(expo_matrix(F4F4)), stabilizer(expo_matrix(HW))
check('stabilizer of F4⊗F4 (exact exponent arithmetic)', STAB_F4F4, 8192)
check('stabilizer of the twisted point Hw (exact exponent arithmetic)', STAB_HW, 128)
# the independent control: the orbit of each dephased class under G_ext by breadth-first search over generators,
# and |orbit| * |stabilizer| = |G_ext| = 2654208
def blockperm(p, q): return [4 * p[a] + q[b] for a in range(4) for b in range(4)]
T4, C4 = (1, 0, 2, 3), (1, 2, 3, 0)
ROWG = [blockperm(T4, ID4), blockperm(C4, ID4), blockperm(ID4, T4), blockperm(ID4, C4)]
def orbit_size(E0):
    s0 = dephase_e(E0); seen = {s0.tobytes()}; frontier = [s0]
    while frontier:
        nxt = []
        for E in frontier:
            imgs = [E[g, :] for g in ROWG] + [E[:, g] for g in ROWG] + [E[np.ix_(SW, SW)], (-E) % 4, E.T.copy()]
            for F in imgs:
                F = dephase_e(F); k = F.tobytes()
                if k not in seen: seen.add(k); nxt.append(F)
        frontier = nxt
    return len(seen)
ORB_F4F4, ORB_HW = orbit_size(expo_matrix(F4F4)), orbit_size(expo_matrix(HW))
check('orbit of F4⊗F4 under G_ext by breadth-first search (control)', ORB_F4F4, 324)
check('orbit of Hw under G_ext by breadth-first search (control)', ORB_HW, 20736)
check('orbit times stabilizer equals |G_ext| at both points (control)', (ORB_F4F4 * STAB_F4F4, ORB_HW * STAB_HW), (2654208, 2654208))
print('  (%.0fs)' % (time.time() - t0))

print()
if fails:
    print('dita_defect_probe: FAILED (%d): %s' % (len(fails), fails)); sys.exit(1)
print('dita_defect_probe: OK -- defect strata 105/73/57/49 on the stratum and 17 on the hull, hull tangent rank 26 against defect 49, %d census points off the Kronecker locus, act 34\'s witness a relabelled stratum point, the matrix-induced subgroup of order 2304' % len(CENSUS))
