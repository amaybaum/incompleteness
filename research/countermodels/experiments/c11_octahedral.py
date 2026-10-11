# c11_octahedral.py -- research/countermodels node C11 (round 3): G384 = <cnot, actT Rz(pi/2), actT cyc3> (HO-14 v1);
# Bell-type defects excluded; an explicit invariant exotic cone by a rank-one orbit surgery (Theorem S' of NOTES-C11).
# DECISION RULE (fixed before the first run, 2026-10-11T00:16:53Z by date -u; first drafted 00:13:49Z and revised before any
# run -- the cap-edge construction of X1/CC1 and the charpoly helper; predictions in NOTES-C11 S0, 00:11:33Z):
#  Exact arithmetic only: int, fractions.Fraction, Gaussian rationals GQ (pairs of Fractions); sympy only for the polynomial
#  identity of B1 (expand == 0). Guard EX: no float in any recorded value.
#  Conventions: tables 4x4, index 0 the unit; pW(w) = (1/4) sum w_mn s_m(x)s_n; table(A)_mn = tr(A s_m(x)s_n); cnot = the
#  kernel's signed permutation (SGN, PC, PT), compared with the Lean text at L (D0); actT(N) w = w Hom(N)^T with
#  Rz90 = [[0,-1,0],[1,0,0],[0,0,1]], cyc3 = [[0,0,1],[1,0,0],[0,1,0]]. Vectors in C^4 = control (x) target, basis
#  |00>,|01>,|10>,|11>; Psi(v) = [[v0, v1], [v2, v3]]; det(v) = v0 v3 - v1 v2. A ray is a nonzero vector up to scalars;
#  canonical form = v / (first nonzero entry). Overlap s(u, v) = |<u|v>|^2 / (|u|^2 |v|^2) (rational).
#  D0  PC, PT, SGN equal the Lean text of verification/lean-mathlib/OIBridge/CompositeDimension.lean at L.
#  G1  closure of {cnot, actT Rz90, actT cyc3} as signed permutations of the 16 coordinates: order 384; each fixes E00.
#  G2  unitary lift: CNOT, I(x)S (S = diag(1, i)), I(x)UJ (UJ = (I - i(X+Y+Z))/2), Gaussian rational. Ad(U) w :=
#      table(U pW(w) U^dag) equals cnot, actT Rz90, actT cyc3 on the 16 basis tables. Closure of the matrix group; its
#      classes modulo {1, i, -1, -i} number 384, and Ad maps them bijectively onto the G1 group.
#  G3  every lifted element is block diagonal in the control basis, U = P0(x)A + P1(x)B, and B A^dag = omega P with
#      omega in {1, i, -1, -i}, P in {I, X, Y, Z}; A modulo {1, i, -1, -i} takes 24 values; the pairs (class of A, omega P)
#      are 384 distinct (24 * 16).
#  B1  symbolic: for g = |0>a + |1>b (a, b in C^2, 8 real symbols), C_P g = |0>a + |1>Pb and
#      sum_{P in X,Y,Z} |det(C_P g)|^2 - (|a|^2 |b|^2 + |<a|b>|^2) expands to 0. C_X = CNOT, C_Y = (I(x)S) CNOT (I(x)S)^dag,
#      C_Z = (I(x)UJ^2) CNOT (I(x)UJ^2)^dag are lifted elements (in the closure of G2) with block form (I, X), (I, Y), (I, Z).
#  B2  instances (Bell vectors C2(1) ~ (1,-1,1,1), the four Z_F cap vectors psi_s ~ (1, s1 s2, s1, -s2), Phi+ ~ (1,0,0,1),
#      C1(i) ~ (1, 1, i, -i)): each is maximally entangled; the three ratios |det(C_P g)|^2/|g|^4 sum to 1/4; for the P with the
#      smallest ratio (<= 1/12) a product p of Pauli eigenvectors (x, y in {(1,0),(0,1),(1,1),(1,-1),(1,i),(1,-i)}) has
#      s(C_P g, p) > 1/2, so the defect I - 2P_{C_P g} pairs < 0 with the pure product P_p (record the value 1 - 2 s).
#  Q1  phi0 = (1, 2, 3i, -1+i) (HO-14; |phi0|^2 = 16): images under the 384 classes: every |det|^2/|v|^4 > 0; record the
#      minimum (predicted 5/256); 384 distinct rays; some image k has <phi0|v_k> = 0 (orthogonal pair). Let s_max = the
#      largest overlap of phi0 with another ray of its orbit, d_min the minimal det ratio. Checks: (i) 1 - 4 d_min >= 0 and
#      the H1 window bound c <= 1/m (m = (1 + sqrt(1 - 4 d_min))/2) lies below 1/s_max: (2 s_max - 1)^2 < 1 - 4 d_min when
#      2 s_max - 1 > 0 (rational); (ii) for c in {517/512, 101/100}: y = P_phi0 + lam d_k, lam = (c - 1)/(4 - 2c) (d_l =
#      I - c P_l, l over the orbit): <y, d_0> = 0, <y, d_l> > 0 for all other l, h_k^dag y h_k < 0 (exact).
#  X1  h* = (10, 2-2i, -1-3i, 3-i) (|h*|^2 = 128), c* = 401/400: orbit rays (predicted 192); closed under the three
#      generators; for every orbit ray: det ratio d_k > 0 and 1 - 4 d_k <= (2/c* - 1)^2 (equivalent to c* lambda_max <= 1:
#      H1 for the defect, [W] operator-norm bound); pairwise overlaps s_jk: min s (predicted 25/2048) > 0, (CC)
#      c*^2 s_jk >= 4(c* - 1) for every pair, pairings 4 - 2c* + c*^2 s_jk > 0; d* = I - c* P_h* has eigenvalue 1 - c* < 0.
#      Consequence check of Theorem S' (necessary condition, not a proof of it): for the min-overlap pair (j, k), the
#      geodesic away from h_k, v(t) = h_j - t w, w = conj(<h_j|h_k>) (h_k - (<h_j|h_k>/|h_j|^2) h_j) (w orthogonal to h_j,
#      |<h_k|v(t)>| decreasing in t), cap_j = {t^2 < T2}, T2 = (c - 1)|h_j|^2/|w|^2; t_e = the largest multiple of 10^-9
#      with t_e^2 < T2 (far cap edge) and t_m = t_e/2: at both points y = P_v + lam d_k with <y, d_j> = 0, lam > 0, is PSD
#      (Faddeev-LeVerrier charpoly: e1..e4 >= 0, exact).
#  CC1 c' = 301/300 on the same pair: (CC) fails (c'^2 s < 4(c' - 1)); at the far cap edge t_e(c'): s(h_k, v) < 1 - 1/c', and
#      y = P_v + lam d_k (d's at c'): <y, d_j> = 0, <y, d_k> > 0, and x = the v-orthogonal part of h_k has x^dag y x < 0
#      (the two-defect surgery K({d_j, d_k}) at c' is not self-dual).
#  CC2 under <cnot> alone C2(1) is fixed (CNOT C2(1) ~ C2(1)), so its orbit stays Bell-type: the exclusion needs C_Y or C_Z.
#  CC3 c = 2 (Bell): for distinct non-orthogonal Bell rays C1(1), C1(i) the (CC) inequality c^2 s >= 4(c - 1) fails
#      (s = 1/2); for Z_F all cross pairings <d_s, d_t> (s != t) vanish (Theorem S's case; (CC) vacuous).
#  VERDICT C11-OCTAHEDRAL-EXACT iff every CHECK passes and every COUNTERCONTROL behaves as stated; else NO VERDICT.
#  Verdict text is generated from the measured values.
import re, itertools
from math import isqrt
from fractions import Fraction as Fr
import sympy as sp

RES = []
def rec(kind, cid, ok, text, detail=''):
    ok = bool(ok); RES.append(ok)
    print('%s %-4s %s %s%s' % (kind, cid, 'PASS' if ok else 'FAIL', text, (' -- ' + detail) if detail else ''))

# ---------- Gaussian rationals
class GQ:
    __slots__ = ('r', 'i')
    def __init__(self, r, i=0):
        self.r = r if isinstance(r, Fr) else Fr(r); self.i = i if isinstance(i, Fr) else Fr(i)
    def __add__(s, o): o = o if isinstance(o, GQ) else GQ(o); return GQ(s.r + o.r, s.i + o.i)
    __radd__ = __add__
    def __sub__(s, o): o = o if isinstance(o, GQ) else GQ(o); return GQ(s.r - o.r, s.i - o.i)
    def __rsub__(s, o): return GQ(o) - s
    def __neg__(s): return GQ(-s.r, -s.i)
    def __mul__(s, o):
        o = o if isinstance(o, GQ) else GQ(o); return GQ(s.r * o.r - s.i * o.i, s.r * o.i + s.i * o.r)
    __rmul__ = __mul__
    def conj(s): return GQ(s.r, -s.i)
    def n2(s): return s.r * s.r + s.i * s.i
    def __truediv__(s, o):
        if not isinstance(o, GQ): o = GQ(o)
        d = o.n2(); t = s * o.conj(); return GQ(t.r / d, t.i / d)
    def iszero(s): return s.r == 0 and s.i == 0
    def __eq__(s, o): o = o if isinstance(o, GQ) else GQ(o); return s.r == o.r and s.i == o.i
    def __hash__(s): return hash((s.r, s.i))
    def __repr__(s):
        if s.i == 0: return str(s.r)
        return '(%s%s%si)' % (s.r, '+' if s.i >= 0 else '-', abs(s.i))
ZERO, ONE, II = GQ(0), GQ(1), GQ(0, 1)
def M(rows): return [[x if isinstance(x, GQ) else GQ(x) for x in r] for r in rows]
def mmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum((A[i][t] * B[t][j] for t in range(k)), ZERO) for j in range(m)] for i in range(n)]
def dag(A): return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]
def kron(A, B):
    return [[A[i // len(B)][j // len(B[0])] * B[i % len(B)][j % len(B[0])] for j in range(len(A[0]) * len(B[0]))] for i in range(len(A) * len(B))]
def madd(A, B): return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mscale(c, A): return [[c * x for x in r] for r in A]
def eye(n): return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]
def tr(A): return sum((A[i][i] for i in range(len(A))), ZERO)
def mv(A, v): return [sum((A[i][t] * v[t] for t in range(len(v))), ZERO) for i in range(len(A))]
def ipv(u, v): return sum((u[t].conj() * v[t] for t in range(len(u))), ZERO)   # <u|v>
def n2v(v): return sum((x.n2() for x in v), Fr(0))
def ovl(u, v): return ipv(u, v).n2() / (n2v(u) * n2v(v))
def detr(v): return (v[0] * v[3] - v[1] * v[2]).n2() / n2v(v) ** 2       # |det Psi|^2 / |v|^4
def canon(v):
    k = next(t for t in range(4) if not v[t].iszero()); a = v[k]
    return tuple((x / a) for x in v)
def outer(u, v): return [[u[i] * v[j].conj() for j in range(len(v))] for i in range(len(u))]
def proj(v):   # P_v = v v^dag / |v|^2
    n = n2v(v); return [[x / n for x in r] for r in outer(v, v)]
def hip(A, B): return tr(mmul(A, B))   # trace pairing <A, B> = tr(AB) for Hermitian A, B
def isreal(x): return x.i == 0

# ---------- Paulis and the table dictionary
s0 = M([[1, 0], [0, 1]]); sx = M([[0, 1], [1, 0]]); sy = M([[0, GQ(0, -1)], [II, 0]]); sz = M([[1, 0], [0, -1]])
SIG = [s0, sx, sy, sz]
SS = [[kron(SIG[m], SIG[n]) for n in range(4)] for m in range(4)]
def pW(w): return [[sum((GQ(w[m][n]) * SS[m][n][i][j] for m in range(4) for n in range(4) if w[m][n] != 0), ZERO) / 4 for j in range(4)] for i in range(4)]
SSP = [[[(i, j, SS[m][n][j][i]) for i in range(4) for j in range(4) if not SS[m][n][j][i].iszero()] for n in range(4)] for m in range(4)]
def table(A):   # entries tr(A s_m(x)s_n) = sum_ij A_ij (s_m(x)s_n)_ji over the four nonzero entries of each Pauli product
    t = [[sum((A[i][j] * val for i, j, val in SSP[m][n]), ZERO) for n in range(4)] for m in range(4)]
    assert all(isreal(x) for r in t for x in r), 'non-real table'
    return [[x.r for x in r] for r in t]
def Eb(m, n): w = [[0] * 4 for _ in range(4)]; w[m][n] = 1; return w
BASIS = [Eb(m, n) for m in range(4) for n in range(4)]

# ---------- D0, G1: the signed-permutation group
SGN = lambda m, n: -1 if (m, n) in [(1, 3), (2, 2)] else 1
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
src = open('../../../verification/lean-mathlib/OIBridge/CompositeDimension.lean', encoding='utf-8').read()
def lean_table(name):
    blk = re.search(r'def %s : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n){4})' % name, src).group(1)
    tab = [[None] * 4 for _ in range(4)]
    for a, b, v in re.findall(r'(\d), (\d) => (\d)', blk): tab[int(a)][int(b)] = int(v)
    return tab
sgn_ok = re.search(r'def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = 1 ∧ ν = 3\) ∨ \(μ = 2 ∧ ν = 2\) then -1 else 1', src) is not None
rec('CHECK', 'D0', lean_table('pc') == PC and lean_table('pt') == PT and sgn_ok, 'PC, PT, SGN equal the Lean text (CompositeDimension.lean:741-755 at L)')

def cnotT(w): return [[SGN(m, n) * w[PC[m][n]][PT[m][n]] for n in range(4)] for m in range(4)]
def Hom(N): H = [[1, 0, 0, 0]] + [[0] + list(r) for r in N]; return H
def actT(N): Hm = Hom(N); return lambda w: [[sum(w[m][k] * Hm[n][k] for k in range(4)) for n in range(4)] for m in range(4)]
Rz90 = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
cyc3 = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
def as_sp(f):   # signed permutation: image of basis E_mn -> (index, sign)
    out = []
    for b in BASIS:
        w = f(b); nz = [(m * 4 + n, w[m][n]) for m in range(4) for n in range(4) if w[m][n] != 0]
        assert len(nz) == 1 and nz[0][1] in (1, -1); out.append(nz[0])
    return tuple(out)
def compose(p, q):  # (p o q): apply q first
    return tuple((p[i][0], p[i][1] * s) for (i, s) in q)
gens_sp = [as_sp(cnotT), as_sp(actT(Rz90)), as_sp(actT(cyc3))]
idsp = tuple((i, 1) for i in range(16))
GRP = {idsp}; fr = [idsp]
while fr:
    nf = []
    for a in fr:
        for g in gens_sp:
            b = compose(g, a)
            if b not in GRP: GRP.add(b); nf.append(b)
    fr = nf
fixE00 = all(p[0] == (0, 1) for p in GRP)
rec('CHECK', 'G1', len(GRP) == 384 and fixE00, 'closure of {cnot, actT Rz(pi/2), actT cyc3} as signed permutations of the 16 coordinates', 'order %d; every element fixes E00: %s' % (len(GRP), fixE00))

# ---------- G2: unitary lift
P0 = M([[1, 0], [0, 0]]); P1 = M([[0, 0], [0, 1]])
CNOT = madd(kron(P0, s0), kron(P1, sx))
S = M([[1, 0], [0, II]])
UJ = mscale(GQ(Fr(1, 2)), madd(s0, mscale(GQ(0, -1), madd(madd(sx, sy), sz))))
uni = all(mmul(U, dag(U)) == eye(2) for U in (S, UJ))
def Ad_sp(U):
    out = []
    for b in BASIS:
        w = table(mmul(mmul(U, pW(b)), dag(U)))
        nz = [(m * 4 + n, w[m][n]) for m in range(4) for n in range(4) if w[m][n] != 0]
        if len(nz) != 1 or nz[0][1] not in (1, -1): return None
        out.append((nz[0][0], int(nz[0][1])))
    return tuple(out)
GU = [CNOT, kron(s0, S), kron(s0, UJ)]
lift_ok = uni and [Ad_sp(U) for U in GU] == gens_sp
def mkey(U): return tuple((x.r, x.i) for r in U for x in r)
SCAL = [ONE, II, GQ(-1), GQ(0, -1)]
def ckey(U):   # class key modulo {1, i, -1, -i}
    return min(mkey(mscale(c, U)) for c in SCAL)
MAT = {mkey(eye(4)): eye(4)}; fr = [eye(4)]
while fr:
    nf = []
    for A in fr:
        for g in GU:
            B = mmul(g, A); k = mkey(B)
            if k not in MAT: MAT[k] = B; nf.append(B)
    fr = nf
CLS = {}
for U in MAT.values():
    CLS.setdefault(ckey(U), U)
ELEM = list(CLS.values())
adimgs = [Ad_sp(U) for U in ELEM]
bij = all(a is not None and a in GRP for a in adimgs) and len(set(adimgs)) == len(ELEM) == 384
rec('CHECK', 'G2', lift_ok and bij, 'Ad(CNOT), Ad(I(x)S), Ad(I(x)UJ) are cnot, actT Rz90, actT cyc3; the lifted group has 384 classes mod {1,i,-1,-i}, mapped bijectively onto G1',
    'matrix group order %d, classes %d' % (len(MAT), len(ELEM)))

# ---------- G3: block structure
PAUL = [('I', s0), ('X', sx), ('Y', sy), ('Z', sz)]
OMP = [(c, nm, mscale(c, P)) for c in SCAL for nm, P in PAUL]
blockok = True; Acls = set(); pairs = set()
for U in ELEM:
    if any(not U[i][j].iszero() for i in range(2) for j in range(2, 4)) or any(not U[i][j].iszero() for i in range(2, 4) for j in range(2)):
        blockok = False; break
    A = [r[:2] for r in U[:2]]; B = [r[2:] for r in U[2:]]
    BA = mmul(B, dag(A))
    hit = [(c, nm) for c, nm, Pm in OMP if Pm == BA]
    if len(hit) != 1: blockok = False; break
    ka = min(tuple((x.r, x.i) for r in mscale(c, A) for x in r) for c in SCAL)
    Acls.add(ka); pairs.add((ka, hit[0][0].r, hit[0][0].i, hit[0][1]))
rec('CHECK', 'G3', blockok and len(Acls) == 24 and len(pairs) == 384, 'every element is P0(x)A + P1(x)omega P A (block diagonal in the control basis)',
    '%d classes of A, %d distinct (A, omega P) pairs' % (len(Acls), len(pairs)))

# ---------- B1: the identity
ar = sp.symbols('a0r a0i a1r a1i b0r b0i b1r b1i', real=True)
a = [ar[0] + sp.I * ar[1], ar[2] + sp.I * ar[3]]; b = [ar[4] + sp.I * ar[5], ar[6] + sp.I * ar[7]]
spP = {'X': sp.Matrix([[0, 1], [1, 0]]), 'Y': sp.Matrix([[0, -sp.I], [sp.I, 0]]), 'Z': sp.Matrix([[1, 0], [0, -1]])}
def ab2(x): return sp.expand(x * sp.conjugate(x))
tot = 0
for nm, Pm in spP.items():
    pb = Pm * sp.Matrix(b)
    tot += ab2(a[0] * pb[1] - a[1] * pb[0])
na = ab2(a[0]) + ab2(a[1]); nb = ab2(b[0]) + ab2(b[1]); iab = sp.conjugate(a[0]) * b[0] + sp.conjugate(a[1]) * b[1]
ident = sp.expand(tot - (na * nb + ab2(iab))) == 0
CY = mmul(mmul(kron(s0, S), CNOT), dag(kron(s0, S)))
UJ2 = mmul(UJ, UJ)
CZ = mmul(mmul(kron(s0, UJ2), CNOT), dag(kron(s0, UJ2)))
def blockform(U, Pn):
    A = [r[:2] for r in U[:2]]; B = [r[2:] for r in U[2:]]
    return A == s0 and B == dict(PAUL)[Pn] and all(U[i][j].iszero() for i in range(2) for j in range(2, 4))
inG = all(ckey(U) in CLS for U in (CNOT, CY, CZ))
rec('CHECK', 'B1', ident and inG and blockform(CNOT, 'X') and blockform(CY, 'Y') and blockform(CZ, 'Z'),
    'sum_{P=X,Y,Z} |det(C_P g)|^2 = |a|^2|b|^2 + |<a|b>|^2 (polynomial identity); C_X = CNOT, C_Y, C_Z are elements of G384')

# ---------- B2: instances
CP = {'X': CNOT, 'Y': CY, 'Z': CZ}
def V(*xs): return [x if isinstance(x, GQ) else GQ(x) for x in xs]
bells = {'C2(1)': V(1, -1, 1, 1), 'psi(++)': V(1, 1, 1, -1), 'psi(+-)': V(1, -1, 1, 1), 'psi(-+)': V(1, -1, -1, -1), 'psi(--)': V(1, 1, -1, 1),
         'Phi+': V(1, 0, 0, 1), 'C1(i)': V(1, 1, II, GQ(0, -1))}
loc = [V(1, 0), V(0, 1), V(1, 1), V(1, -1), V(1, II), V(1, GQ(0, -1))]
prods = [V(x[0] * y[0], x[0] * y[1], x[1] * y[0], x[1] * y[1]) for x in loc for y in loc]
b2ok = True; b2rec = []
for nm, g in bells.items():
    me = detr(g) == Fr(1, 4)
    rat = {p: detr(mv(CP[p], g)) for p in 'XYZ'}
    ssum = sum(rat.values()) == Fr(1, 4)
    pmin = min('XYZ', key=lambda p: rat[p])
    u = mv(CP[pmin], g)
    best = max(ovl(u, p) for p in prods)
    ok = me and ssum and rat[pmin] <= Fr(1, 12) and best > Fr(1, 2)
    b2ok &= ok
    b2rec.append('%s: ratios X %s Y %s Z %s; C_%s image pairs %s with a product' % (nm, rat['X'], rat['Y'], rat['Z'], pmin, 1 - 2 * best))
rec('CHECK', 'B2', b2ok, 'every listed Bell vector g: sum of ratios 1/4, some C_P g has ratio <= 1/12, and I - 2P_{C_P g} pairs < 0 with a pure product', '; '.join(b2rec))

# ---------- orbit helper
def orbit_rays(h):
    rays = {}
    for U in ELEM:
        v = mv(U, h); k = canon(v)
        if k not in rays: rays[k] = list(k)
    return list(rays.values())

# ---------- Q1: phi0
phi0 = V(1, 2, GQ(0, 3), GQ(-1, 1))
orb0 = orbit_rays(phi0)
dets0 = [detr(v) for v in orb0]
dmin0 = min(dets0)
c0 = canon(phi0)
others = [v for v in orb0 if tuple(v) != c0]
ovs0 = [ovl(phi0, v) for v in others]
orthk = [v for v in others if ipv(phi0, v).iszero()]
smax0 = max(ovs0)
win_ok = (1 - 4 * dmin0 >= 0) and ((2 * smax0 - 1 <= 0) or ((2 * smax0 - 1) ** 2 < 1 - 4 * dmin0))
wit_ok = True; witrec = []
if orthk:
    hk = orthk[0]
    for c in (Fr(517, 512), Fr(101, 100)):
        lam = (c - 1) / (4 - 2 * c)
        def dl(v): return madd(eye(4), mscale(GQ(-c), proj(v)))
        y = madd(proj(phi0), mscale(GQ(lam), dl(hk)))
        p0 = hip(y, dl(phi0))
        pl = [hip(y, dl(v)) for v in others]
        neg = mv(y, hk); qv = ipv(hk, neg)
        okc = p0.iszero() and all(isreal(x) and x.r > 0 for x in pl) and isreal(qv) and qv.r < 0
        wit_ok &= okc
        witrec.append('c=%s: <y,d_0>=%s, min <y,d_l>=%s, h_k^dag y h_k/|h_k|^2=%s' % (c, p0, min(x.r for x in pl), qv.r / n2v(hk)))
rec('CHECK', 'Q1', all(d > 0 for d in dets0) and len(orb0) == 384 and len(orthk) >= 1 and win_ok and wit_ok,
    'phi0: unreachable, 384 distinct rays, an orthogonal pair in its orbit; the window c <= 1/m lies below 1/s_max; exact witnesses in K* \\ K',
    'min det ratio %s, s_max %s, orthogonal partners %d; %s' % (dmin0, smax0, len(orthk), '; '.join(witrec)))

# ---------- X1: the explicit cone
hstar = V(10, GQ(2, -2), GQ(-1, -3), GQ(3, -1))
cst = Fr(401, 400)
orbs = orbit_rays(hstar)
keys = set(tuple(v) for v in orbs)
closed = all(canon(mv(U, v)) in keys for U in GU for v in orbs)
detsS = [detr(v) for v in orbs]
h1 = all(d > 0 for d in detsS) and all(1 - 4 * d <= (2 / cst - 1) ** 2 for d in detsS)
nS = len(orbs)
svals = {}
for j in range(nS):
    for k in range(j + 1, nS):
        svals[(j, k)] = ovl(orbs[j], orbs[k])
smin = min(svals.values()); smaxS = max(svals.values())
cc_ok = all(cst * cst * s >= 4 * (cst - 1) for s in svals.values())
pair_pos = all(4 - 2 * cst + cst * cst * s > 0 for s in svals.values())
dmin = min(detsS)
# consequence check at the min-overlap pair
(j0, k0) = min(svals, key=lambda t: svals[t])
hj, hk = orbs[j0], orbs[k0]
def dvec(v, c): return madd(eye(4), mscale(GQ(-c), proj(v)))
def charpoly_e(A):   # Faddeev-LeVerrier: p(x) = x^4 + c3 x^3 + c2 x^2 + c1 x + c0; returns e1..e4 (e_k = (-1)^k c_{4-k})
    n = 4; I4 = eye(n); Mk = [[ZERO] * n for _ in range(n)]; ck = ONE; coeffs = [ONE]
    for k in range(1, n + 1):
        Mk = madd(mmul(A, Mk), mscale(ck, I4))
        ck = GQ(Fr(-1, k)) * tr(mmul(A, Mk))
        coeffs.append(ck)
    return [coeffs[k] * (1 if k % 2 == 0 else -1) for k in range(1, n + 1)]
def psd(A):
    e = charpoly_e(A); return all(isreal(x) and x.r >= 0 for x in e), e
def geo(hj, hk, c):   # far cap-edge parameter and direction (see X1)
    kap = ipv(hj, hk)
    uu = [hk[q] - (kap / n2v(hj)) * hj[q] for q in range(4)]
    w = [kap.conj() * x for x in uu]
    T2 = (c - 1) * n2v(hj) / n2v(w)
    te = Fr(isqrt(T2.numerator * 10 ** 18 // T2.denominator), 10 ** 9)
    while te * te >= T2: te -= Fr(1, 10 ** 9)
    return te, w
def vpt(hj, w, t): return [hj[q] - GQ(t) * w[q] for q in range(4)]
te, w = geo(hj, hk, cst)
cons_ok = True; consrec = []
for t in (te, te / 2):
    v = vpt(hj, w, t)
    dj, dk = dvec(hj, cst), dvec(hk, cst)
    G = hip(dj, dk).r
    lam = -hip(proj(v), dj).r / G
    y = madd(proj(v), mscale(GQ(lam), dk))
    okp, e = psd(y)
    cons_ok &= ovl(hj, v) > 1 / cst and hip(y, dj).iszero() and lam > 0 and okp
    consrec.append('t=%s: s(h_j,v)-1/c*=%s, s(h_k,v)=%s vs 1-1/c*=%s, PSD %s' % (t, ovl(hj, v) - 1 / cst, ovl(hk, v), 1 - 1 / cst, okp))
consrec = '; '.join(consrec)
dst = dvec(hstar, cst); okd, ed = psd(dst)
rec('CHECK', 'X1', nS == 192 and closed and h1 and smin > 0 and cc_ok and pair_pos and not okd and cons_ok,
    'h*: unreachable G384-orbit of 192 rays, H1 at c* = 401/400, all pairs satisfy (CC) and pair positively, d* not PSD; S\' consequence holds at the far cap edge',
    'rays %d, closed %s, min det ratio %s, min overlap %s, max overlap %s, (CC) %s; %s' % (nS, closed, dmin, smin, smaxS, cc_ok, consrec))
Th = table(proj(hstar))
zst = [[(Fr(1, 2) if (m, n) == (0, 0) else Fr(0)) - cst / 8 * Th[m][n] for n in range(4)] for m in range(4)]
print('RECORD z* = E00/2 - (c*/8) T_h* (pauliW(z*) = d*/8): %s' % [[str(x) for x in r] for r in zst])

# ---------- CC1: sharpness at the pair level
cp = Fr(301, 300)
viol = cp * cp * smin < 4 * (cp - 1)
tc, wc = geo(hj, hk, cp)
v = vpt(hj, wc, tc)
cc1 = False; cc1rec = ''
if ovl(hj, v) > 1 / cp and ovl(hk, v) < 1 - 1 / cp:
    dj, dk = dvec(hj, cp), dvec(hk, cp)
    G = hip(dj, dk).r
    lam = -hip(proj(v), dj).r / G
    y = madd(proj(v), mscale(GQ(lam), dk))
    x = [hk[q] - (ipv(v, hk) / n2v(v)) * v[q] for q in range(4)]
    xyx = ipv(x, mv(y, x))
    cc1 = viol and hip(y, dj).iszero() and hip(y, dk).r > 0 and lam > 0 and isreal(xyx) and xyx.r < 0
    cc1rec = 't=%s, s(h_j,v)-1/c\'=%s, s(h_k,v)=%s < 1-1/c\'=%s, x^dag y x=%s' % (tc, ovl(hj, v) - 1 / cp, ovl(hk, v), 1 - 1 / cp, xyx.r)
rec('COUNTERCONTROL', 'CC1', cc1, 'c\' = 301/300 violates (CC) on the min-overlap pair; exact y in K({d_j,d_k})* \\ K({d_j,d_k})', cc1rec)

# ---------- CC2, CC3
c21 = bells['C2(1)']
cc2 = canon(mv(CNOT, c21)) == canon(c21)
rec('COUNTERCONTROL', 'CC2', cc2, 'under <cnot> alone C2(1) is fixed (Bell-type orbit): the exclusion needs C_Y or C_Z')
s_c1 = ovl(V(1, 1, 1, -1), bells['C1(i)'])
zf = [bells['psi(++)'], bells['psi(+-)'], bells['psi(-+)'], bells['psi(--)']]
cross0 = all(hip(dvec(zf[a_], 2), dvec(zf[b_], 2)).iszero() for a_ in range(4) for b_ in range(4) if a_ != b_)
cc3 = (2 * 2 * s_c1 < 4 * (2 - 1)) and s_c1 > 0 and cross0
rec('COUNTERCONTROL', 'CC3', cc3, 'c = 2: C1(1), C1(i) (s = %s) fail (CC) (C4.1); Z_F cross pairings all 0 (Theorem S, CC vacuous)' % s_c1)

# ---------- EX guard
def nofloat(x):
    if isinstance(x, float): return False
    if isinstance(x, (list, tuple)): return all(nofloat(y) for y in x)
    if isinstance(x, GQ): return isinstance(x.r, Fr) and isinstance(x.i, Fr)
    return True
ex = nofloat([dmin0, smax0, smin, smaxS, dmin, list(svals.values())[:50], detsS, dets0])
rec('CHECK', 'EX', ex, 'no float in any recorded value')
nf = sum(1 for r in RES if not r)
print('summary: %d checks, %d failed' % (len(RES), nf))
if nf == 0:
    print('VERDICT C11-OCTAHEDRAL-EXACT: G384 has order %d; every Bell-type defect leaves maxCone under some element (sum identity 1/4); '
          'phi0 (min det ratio %s) has an orthogonal partner in its orbit, so its orbit surgeries fail; h* = (10, 2-2i, -1-3i, 3-i) has a '
          'G384-orbit of %d rays with min det ratio %s and min overlap %s, and at c* = %s every pair satisfies (CC): K(G384 d*) is an explicit '
          'G384-invariant exotic cone given Theorem S\'' % (len(GRP), dmin0, nS, dmin, smin, cst))
else:
    print('NO VERDICT')
