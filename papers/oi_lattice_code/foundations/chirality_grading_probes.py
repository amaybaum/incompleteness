#!/usr/bin/env python3
"""b50 preregistered probe — the sublattice grading of the staggered
reconstruction (2026-08-10). Prereg: bundle notes/b50_prereg_* and
b50_variants_* (outcome mapping frozen before this run).

Decides Theorem 13(i)'s identification "even-|eta| corners = left-handed
spinor components" against the standard spin-taste algebra, exactly.

P1  gamma5 Gamma(eta) gamma5 = (-1)^|eta| Gamma(eta) for all 16 eta.
P2  V+ = span{Gamma(eta): |eta| even}; compute dims (d_L, d_R) of the
    spin-chirality subspaces {M in V+ : gamma5 M = -M / +M}.
      (8,0) -> Theorem 13(i) confirmed.  (4,4) -> refuted (grading is
      gamma5 (x) xi5; both spin chiralities on each sublattice).
P3  V+ equals {M : gamma5 M gamma5 = M} exactly (the conjugation-parity
    eigenspace), tying the corner grading to the operator grading.
P4  Visible-sector identity: for every M in V+, gamma5 M = M gamma5
    (left gamma5-action = right gamma5-action on the even subspace).
P5  Lattice sector, L=4 (256 sites): staggered phases eta_mu, antisymmetric
    central-difference D. Exact checks: {D, eps} = 0; even-even and odd-odd
    blocks of D vanish identically; D^2 is sublattice-diagonal and acts
    identically on the two sublattices (Theorem 2's factorization shape).

All arithmetic exact (Gaussian integers via Python complex on integer
lattice; ranks by fraction-free row reduction). Zero tolerance.
"""
from fractions import Fraction as F
import itertools

# --- exact 4x4 gammas (Euclidean, hermitian; entries in {0,+-1,+-i}) ---
def kron(A, B):
    n, m = len(A), len(B)
    return [[A[i//m][j//m] * B[i%m][j%m] for j in range(n*m)] for i in range(n*m)]
I2 = [[1,0],[0,1]]; s1 = [[0,1],[1,0]]; s2 = [[0,-1j],[1j,0]]; s3 = [[1,0],[0,-1]]
g = [kron(s1, I2), kron(s2, s1), kron(s2, s2), kron(s2, s3)]  # g0,g1,g2,g3
def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def anti(A, B):
    C = mm(A,B); D = mm(B,A)
    return [[C[i][j]+D[i][j] for j in range(len(A))] for i in range(len(A))]
for mu in range(4):
    for nu in range(4):
        X = anti(g[mu], g[nu])
        assert all(X[i][j] == (2 if (i==j and mu==nu) else 0) for i in range(4) for j in range(4)), "Clifford check"
g5 = mm(mm(g[0], g[1]), mm(g[2], g[3]))
assert all(mm(g5,g5)[i][j] == (1 if i==j else 0) for i in range(4) for j in range(4))

def Gamma(eta):
    M = [[1 if i==j else 0 for j in range(4)] for i in range(4)]
    for mu in range(4):
        if eta[mu]: M = mm(M, g[mu])
    return M

etas = list(itertools.product((0,1), repeat=4))
# P1
for eta in etas:
    Ge = Gamma(eta); X = mm(mm(g5, Ge), g5); s = (-1)**sum(eta)
    assert all(X[i][j] == s*Ge[i][j] for i in range(4) for j in range(4)), "P1 FAIL"
print("P1  conjugation parity gamma5.Gamma.gamma5 = (-1)^|eta| Gamma : EXACT, all 16")

# exact rank over Gaussian rationals
def rank(rows):
    rows = [[F(z.real if isinstance(z, complex) else z), F(z.imag if isinstance(z, complex) else 0)] and None or None for z in r] if False else rows
    M = [[complex(z) for z in r] for r in rows]
    # fraction-free-ish exact elimination on complex with Fraction parts
    M = [[(F(int(z.real)), F(int(z.imag))) if float(z.real).is_integer() and float(z.imag).is_integer() else (F(z.real), F(z.imag)) for z in row] for row in M]
    def cz(a): return a[0] == 0 and a[1] == 0
    def cmul(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
    def csub(a,b): return (a[0]-b[0], a[1]-b[1])
    def cdiv(a,b):
        d = b[0]*b[0]+b[1]*b[1]
        return ((a[0]*b[0]+a[1]*b[1])/d, (a[1]*b[0]-a[0]*b[1])/d)
    r = 0; nr, nc = len(M), len(M[0])
    for c in range(nc):
        p = next((i for i in range(r, nr) if not cz(M[i][c])), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        for i in range(nr):
            if i != r and not cz(M[i][c]):
                f = cdiv(M[i][c], M[r][c])
                M[i] = [csub(M[i][j], cmul(f, M[r][j])) for j in range(nc)]
        r += 1
    return r

def vec(M): return [M[i][j] for i in range(4) for j in range(4)]
Vp = [vec(Gamma(eta)) for eta in etas if sum(eta) % 2 == 0]
assert rank(Vp) == 8
# P2: dims of {M in V+: g5 M = -+M} == rank of stacked constraint solutions.
# Basis approach: g5 acts on vec by (g5 x I); project basis onto eigenspaces.
def lmul_g5(v):
    M = [[v[4*i+j] for j in range(4)] for i in range(4)]
    X = mm(g5, M); return vec(X)
def rmul_g5(v):
    M = [[v[4*i+j] for j in range(4)] for i in range(4)]
    X = mm(M, g5); return vec(X)
def addv(a,b): return [x+y for x,y in zip(a,b)]
def subv(a,b): return [x-y for x,y in zip(a,b)]
Lplus  = [addv(v, lmul_g5(v)) for v in Vp]   # spans {M in V+: g5M=+M} image
Lminus = [subv(v, lmul_g5(v)) for v in Vp]
d_R, d_L = rank(Lplus), rank(Lminus)
print(f"P2  spin-chirality dims inside even-corner span V+ : (d_L, d_R) = ({d_L}, {d_R})")
verdict_i = "CONFIRMED (8,0)" if (d_L, d_R) == (8, 0) else ("REFUTED (4,4): grading is gamma5(x)xi5" if (d_L, d_R) == (4, 4) else f"UNEXPECTED {(d_L,d_R)} - ABORT")
print(f"    Theorem 13(i) 'even = left-handed' : {verdict_i}")
assert (d_L, d_R) in ((8,0), (4,4)), "unexpected dimension pair - abort per prereg"

# P3: V+ == conjugation-parity +1 eigenspace
conj_basis = []
for eta in etas:
    v = vec(Gamma(eta)); w = lmul_g5(rmul_g5([0]*0 or v))  # g5 M g5
    if w == v: conj_basis.append(v)
assert rank(conj_basis) == 8 and rank(conj_basis + Vp) == 8
print("P3  V+ = {M : g5 M g5 = M} : EXACT (dim 8, spans agree)")

# P4: on V+, left g5-action equals right g5-action
for v in Vp:
    assert lmul_g5(v) == rmul_g5(v), "P4 FAIL"
print("P4  visible-sector identity g5 M = M g5 on V+ : EXACT (spin chirality = taste chirality there)")

# P5: lattice sector, L=4
L = 4; N = L**4
def idx(x): return ((x[0]%L)*L**3 + (x[1]%L)*L**2 + (x[2]%L)*L + (x[3]%L))
D = [[0]*N for _ in range(N)]
for x in itertools.product(range(L), repeat=4):
    i = idx(x)
    for mu in range(4):
        phase = 1 if mu == 0 else (-1)**sum(x[:mu])
        xp = list(x); xp[mu] += 1; xm = list(x); xm[mu] -= 1
        D[i][idx(xp)] += phase; D[i][idx(xm)] -= phase
eps = [(-1)**sum(x) for x in itertools.product(range(L), repeat=4)]
for i in range(N):
    for j in range(N):
        assert eps[i]*D[i][j] + D[i][j]*eps[j] == 0, "P5 anticommutation FAIL"
        if eps[i] == eps[j]: assert D[i][j] == 0, "P5 same-sublattice block FAIL"
D2 = [[sum(D[i][k]*D[k][j] for k in range(N) if D[i][k] and D[k][j]) for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if eps[i] != eps[j]: assert D2[i][j] == 0, "P5 D^2 off-block FAIL"
# sublattice symmetry of D^2: translation by one unit maps even<->odd and must preserve D^2's stencil
def shift(i, mu):
    x = [(i//L**3)%L, (i//L**2)%L, (i//L)%L, i%L]; x[mu] += 1; return idx(x)
for i in range(N):
    for j in range(N):
        assert D2[i][j] == D2[shift(i,3)][shift(j,3)], "P5 sublattice-symmetry FAIL"
print(f"P5  L=4 lattice: {{D,eps}}=0, same-sublattice blocks of D vanish, D^2 sublattice-diagonal and shift-symmetric : EXACT")
print("b50 probe: COMPLETE")
