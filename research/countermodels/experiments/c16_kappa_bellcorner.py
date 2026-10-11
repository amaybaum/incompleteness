# c16_kappa_bellcorner.py -- research/countermodels node C16 (round 3, closing review): the Bell corner c = 2 of the
# rank-one obstruction, and the kappa node with G16.
# DECISION RULE (fixed before the first run, 2026-10-11T01:32:52Z by date -u; predictions in NOTES-C16 S0, 01:31Z):
#  Exact arithmetic only (Fractions, Gaussian rationals; guard EX: no float in any recorded value). Vectors are in the
#  computational basis (|00>, |01>, |10>, |11>), unnormalized. f1 = (1,1,0,0), f2 = (1,-1,0,0), f3 = (0,0,1,1),
#  f4 = (0,0,1,-1) are sqrt2 times |0+>, |0->, |1+>, |1->. G_kappa = closure <U(x) (|x| = 1), CNOT, Z(x)I, I(x)Z, T> with
#  U(x) = I + (x - 1) f4 f4^dag / 2 and T = entrywise complex conjugation (the transpose of the density matrix).
#  D0  with F = (f1 f2 f3 f4): F^dag G F / 2 equals diag(1,1,1,x) for G = U(x), x = (3+4i)/5; diag(1,1,1,-1) for CNOT;
#      diag(1,1,-1,-1) for Z(x)I; the permutation matrix of (12)(34) for I(x)Z; U(x) is unitary; and the polarization
#      B(u, v) = (det(u + v) - det u - det v)/2 of det Psi(v) = v00 v11 - v01 v10 has the matrix
#      [[0,0,0,-1],[0,0,1,0],[0,1,0,0],[-1,0,0,0]] on F (so det(a f1 + b f2 + c f3 + d f4) = 2(bc - ad)).
#  K1  orbit: h0 = (6,2,0,0), e = (0,0,1,-1), h0' = (6,-2,0,0), e' = (0,0,1,1); S = {h0 + x e} u {h0' + x e'} (|x| = 1).
#      For y in {(3+4i)/5, (5-12i)/13}: U(y) fixes h0, h0', e' and maps e to y e; CNOT and Z(x)I fix h0, h0', CNOT maps
#      e to -e and fixes e', Z(x)I maps e to -e and e' to -e'; I(x)Z maps h0 <-> h0' and e <-> e'; h0, e, h0', e' are
#      real. By linearity S is invariant under every generator (and U(y)^-1 = U(conj y)), hence under G_kappa
#      (continuity, S closed); S is the orbit of h = h0 + e = (6, 2, 1, -1) [W].
#  K2  <h0|e> = <h0|e'> = <h0'|e> = <h0'|e'> = <e|e'> = 0; |h0|^2 = |h0'|^2 = 40, |e|^2 = |e'|^2 = 2, <h0|h0'> = 32. So
#      on S |v|^2 = 42; within a circle |<v|v'>| >= 40 - 2 = 38, across circles <v|v'> = 32: every squared overlap is
#      >= s_min = 32^2/42^2 = 256/441 > 0 (no orthogonal pair), the within-circle minimum is 38^2/42^2.
#  K3  det h0 = det e = det h0' = det e' = 0, B(h0, e) = -4, B(h0', e') = 4: det(h0 + x e) = -8x, det(h0' + x e') = 8x,
#      so D = |det Psi|^2/|v|^4 = 64/42^2 on all of S (unreachable). H1 at c = 103/100: 1 - 4D <= (2/c - 1)^2 (exact;
#      equivalent to c lambda_max <= 1, lambda_max = (1 + sqrt(1 - 4D))/2).
#  K4  (CC) c^2 s_min >= 4(c - 1) (hence for every pair) and pairings 4 - 2c + c^2 s_min > 0.
#  K5  d = I - c P_h is not PSD (Faddeev-LeVerrier signs), so K_kappa != Q3.
#  K6  consequence check of Theorem S' (necessary, not a proof) on the cross pair h_j = h, h_k = h0' + e': the C11 X1
#      construction (far cap edge t_e = the largest multiple of 10^-9 with t_e^2 < T2, and t_e/2): v in cap_j, and
#      y = P_v + lam d_k with <y, d_j> = 0, lam > 0 is PSD.
#  RECORD z = E00/2 - (c/8) table(P_h) at c = 103/100, with pauliW(z) = d/8 checked exactly.
#  BC1 computational basis: B on the basis vectors is nonzero only on {|00>,|11>} (1/2) and {|01>,|10>} (-1/2);
#      CNOT(|00> + w|11>) = |00> + w|10> and CNOT(|01> + w|10>) = |01> + w|11> have det identically 0 (both parts have
#      det 0 and B = 0 between them).
#  BC2 case B basis of C13 (b1 = (2,3)(x)(2,-1+2i), b2 = CNOT b1, b3 = |0>(x)(1+2i, 2), b4 = (10, -5+10i, -6-12i,
#      -6-12i)): pairwise orthogonal; det b1 = det b3 = 0; det b2 != 0, det b4 != 0.
#  BC3 C1 = {f1 + x f4}, C2 = {f2 + x f3}: U(y) maps f4 to y f4 and fixes f1, f2, f3; CNOT and Z(x)I keep each circle
#      (f4 -> -f4; f3, f4 -> -f3, -f4); I(x)Z maps f1 <-> f2, f3 <-> f4; T fixes the real f's; det f_k = 0,
#      B(f1, f4) = -1, B(f2, f3) = 1, |f_k|^2 = 2, so every point has |det|^2/|v|^4 = 4/16 = 1/4 (Bell type).
#  CC1 S2 contrast: g = (Rz(pi) (x) Rx(pi))(I(x)Z), Rz(pi) = diag(-i, i), Rx(pi) = -iX, is in the S2 group with G16, and
#      <h|g h> = 0 exactly.
#  CC2 at c = 26/25 H1 fails on S: 1 - 4D > (2/c - 1)^2.
#  CC3 r = f1 + f2 + f3 + i f4 = (2, 0, 1+i, 1-i): det r != 0 and det(U(-i) r) = 0.
#  CC4 c' = 5/4 on the cross pair: (CC) fails (c'^2 s_min < 4(c' - 1)); at the far cap edge t_e(c'): s(h_k, v) < 1 - 1/c',
#      y = P_v + lam d_k (d's at c'): <y, d_j> = 0, <y, d_k> > 0, and x = the v-orthogonal part of h_k has x^dag y x < 0.
#  VERDICT C16-KAPPA-BELLCORNER-EXACT iff every CHECK passes and every COUNTERCONTROL behaves as stated; else NO VERDICT.
#  Verdict text is generated from the measured values.
from math import isqrt
from fractions import Fraction as Fr

RES = []
def rec(kind, cid, ok, text, detail=''):
    ok = bool(ok); RES.append(ok)
    print('%s %-4s %s %s%s' % (kind, cid, 'PASS' if ok else 'FAIL', text, (' -- ' + detail) if detail else ''))

# ---------- Gaussian rationals (as in c11_octahedral.py)
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
def V(*xs): return [x if isinstance(x, GQ) else GQ(x) for x in xs]
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
def det(v): return v[0] * v[3] - v[1] * v[2]
def Bf(u, v): return (det(vadd(u, v)) - det(u) - det(v)) / 2
def vadd(u, v): return [u[t] + v[t] for t in range(len(u))]
def vsc(c, v): return [c * x for x in v]
def veq(u, v): return all(u[t] == v[t] for t in range(len(u)))
def outer(u, v): return [[u[i] * v[j].conj() for j in range(len(v))] for i in range(len(u))]
def proj(v):   # P_v = v v^dag / |v|^2
    n = n2v(v); return [[x / n for x in r] for r in outer(v, v)]
def hip(A, B): return tr(mmul(A, B))   # trace pairing <A, B> = tr(AB) for Hermitian A, B
def isreal(x): return x.i == 0
def meq(A, B): return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))
def dvec(v, c): return madd(eye(4), mscale(GQ(-c), proj(v)))
def charpoly_e(A):   # Faddeev-LeVerrier: returns e1..e4 (e_k = (-1)^k c_{4-k}); PSD iff all e_k >= 0 (Hermitian A)
    n = 4; I4 = eye(n); Mk = [[ZERO] * n for _ in range(n)]; ck = ONE; coeffs = [ONE]
    for k in range(1, n + 1):
        Mk = madd(mmul(A, Mk), mscale(ck, I4))
        ck = GQ(Fr(-1, k)) * tr(mmul(A, Mk))
        coeffs.append(ck)
    return [coeffs[k] * (1 if k % 2 == 0 else -1) for k in range(1, n + 1)]
def psd(A):
    e = charpoly_e(A); return all(isreal(x) and x.r >= 0 for x in e), e
def geo(hj, hk, c):   # far cap-edge parameter and direction (as in c11_octahedral.py X1)
    kap = ipv(hj, hk)
    uu = [hk[q] - (kap / n2v(hj)) * hj[q] for q in range(4)]
    w = [kap.conj() * x for x in uu]
    T2 = (c - 1) * n2v(hj) / n2v(w)
    te = Fr(isqrt(T2.numerator * 10 ** 18 // T2.denominator), 10 ** 9)
    while te * te >= T2: te -= Fr(1, 10 ** 9)
    return te, w
def vpt(hj, w, t): return [hj[q] - GQ(t) * w[q] for q in range(4)]

# ---------- Paulis and tables (as in c11_octahedral.py)
s0 = M([[1, 0], [0, 1]]); sx = M([[0, 1], [1, 0]]); sy = M([[0, GQ(0, -1)], [II, 0]]); sz = M([[1, 0], [0, -1]])
SIG = [s0, sx, sy, sz]
SS = [[kron(SIG[m], SIG[n]) for n in range(4)] for m in range(4)]
def pW(w): return [[sum((GQ(w[m][n]) * SS[m][n][i][j] for m in range(4) for n in range(4) if w[m][n] != 0), ZERO) / 4 for j in range(4)] for i in range(4)]
SSP = [[[(i, j, SS[m][n][j][i]) for i in range(4) for j in range(4) if not SS[m][n][j][i].iszero()] for n in range(4)] for m in range(4)]
def table(A):   # entries tr(A s_m(x)s_n)
    t = [[sum((A[i][j] * val for i, j, val in SSP[m][n]), ZERO) for n in range(4)] for m in range(4)]
    assert all(isreal(x) for r in t for x in r), 'non-real table'
    return [[x.r for x in r] for r in t]

# ---------- the kappa group's generators
f1, f2, f3, f4 = V(1, 1, 0, 0), V(1, -1, 0, 0), V(0, 0, 1, 1), V(0, 0, 1, -1)
F = [[f1[i], f2[i], f3[i], f4[i]] for i in range(4)]
def Ux(x): return madd(eye(4), mscale((x - 1) / 2, outer(f4, f4)))
CNOT = M([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
ZI = M([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
IZ = M([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]])
def Tc(v): return [x.conj() for x in v]
def diag(*xs): return [[(xs[i] if isinstance(xs[i], GQ) else GQ(xs[i])) if i == j else ZERO for j in range(4)] for i in range(4)]
x0 = GQ(Fr(3, 5), Fr(4, 5))
def inB(G): return mscale(GQ(Fr(1, 2)), mmul(mmul(dag(F), G), F))
P1234 = M([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
U0 = Ux(x0)
d0_gen = (meq(inB(U0), diag(1, 1, 1, x0)) and meq(inB(CNOT), diag(1, 1, 1, -1)) and meq(inB(ZI), diag(1, 1, -1, -1))
          and meq(inB(IZ), P1234) and meq(mmul(dag(U0), U0), eye(4)))
fs = [f1, f2, f3, f4]
Bmat = [[Bf(fs[i], fs[j]) for j in range(4)] for i in range(4)]
d0_B = meq(Bmat, M([[0, 0, 0, -1], [0, 0, 1, 0], [0, 1, 0, 0], [-1, 0, 0, 0]]))
rec('CHECK', 'D0', d0_gen and d0_B,
    'in the basis (|0+>, |0->, |1+>, |1->): U(x) = diag(1,1,1,x), CNOT = diag(1,1,1,-1), Z(x)I = diag(1,1,-1,-1), I(x)Z = (12)(34); U(x) unitary; det = 2(bc - ad) on F',
    'B on F = %s' % [[str(x) for x in r] for r in Bmat])

# ---------- K1: the orbit S
h0, e, h0p, ep = V(6, 2, 0, 0), V(0, 0, 1, -1), V(6, -2, 0, 0), V(0, 0, 1, 1)
h = vadd(h0, e)
ys = [GQ(Fr(3, 5), Fr(4, 5)), GQ(Fr(5, 13), Fr(-12, 13))]
k1 = True
for y in ys:
    Uy = Ux(y)
    k1 &= veq(mv(Uy, h0), h0) and veq(mv(Uy, h0p), h0p) and veq(mv(Uy, ep), ep) and veq(mv(Uy, e), vsc(y, e))
    k1 &= meq(mmul(Uy, Ux(y.conj())), eye(4))
k1 &= veq(mv(CNOT, h0), h0) and veq(mv(CNOT, h0p), h0p) and veq(mv(CNOT, e), vsc(-1, e)) and veq(mv(CNOT, ep), ep)
k1 &= veq(mv(ZI, h0), h0) and veq(mv(ZI, h0p), h0p) and veq(mv(ZI, e), vsc(-1, e)) and veq(mv(ZI, ep), vsc(-1, ep))
k1 &= veq(mv(IZ, h0), h0p) and veq(mv(IZ, h0p), h0) and veq(mv(IZ, e), ep) and veq(mv(IZ, ep), e)
k1 &= all(isreal(x) for v in (h0, e, h0p, ep) for x in v)
rec('CHECK', 'K1', k1, 'S = {(6,2,x,-x)} u {(6,-2,x,x)} is invariant under U(y), CNOT, Z(x)I, I(x)Z and T: the orbit of h = (6, 2, 1, -1) under kappa with G16 is two circles')

# ---------- K2: overlaps
orth = all(ipv(a, b).iszero() for a, b in [(h0, e), (h0, ep), (h0p, e), (h0p, ep), (e, ep)])
nh0, ne, hh = n2v(h0), n2v(e), ipv(h0, h0p)
k2 = orth and nh0 == 40 and n2v(h0p) == 40 and ne == 2 and n2v(ep) == 2 and hh == GQ(32)
nS = nh0 + ne
smin = hh.n2() / (nS * nS)
s_in = (nh0 - ne) ** 2 / (nS * nS)
k2 = k2 and nS == 42 and smin > 0 and s_in > smin
# exact spot values on the circles (x = 1, -1, i, (3+4i)/5): overlaps equal the closed forms
pts = [GQ(1), GQ(-1), II, GQ(Fr(3, 5), Fr(4, 5))]
spot = True
for xa in pts:
    for xb in pts:
        va, vb, vbp = vadd(h0, vsc(xa, e)), vadd(h0, vsc(xb, e)), vadd(h0p, vsc(xb, ep))
        spot &= ipv(va, vb) == GQ(40) + GQ(2) * xa.conj() * xb and ipv(va, vbp) == GQ(32)
        spot &= ovl(va, vb) >= s_in and ovl(va, vbp) == smin
k2 = k2 and spot
rec('CHECK', 'K2', k2, 'no orthogonal pair on S: within a circle |<v|v\'>| >= 38, across circles <v|v\'> = 32, |v|^2 = 42',
    's_min %s, within-circle minimum %s' % (smin, s_in))

# ---------- K3: det and H1
c = Fr(103, 100)
k3 = (det(h0).iszero() and det(e).iszero() and det(h0p).iszero() and det(ep).iszero()
      and Bf(h0, e) == GQ(-4) and Bf(h0p, ep) == GQ(4))
D = Fr(64) / (nS * nS)
spotD = all((det(vadd(h0, vsc(xa, e))).n2() / n2v(vadd(h0, vsc(xa, e))) ** 2 == D) and
            (det(vadd(h0p, vsc(xa, ep))).n2() / n2v(vadd(h0p, vsc(xa, ep))) ** 2 == D) for xa in pts)
h1 = 1 - 4 * D <= (2 / c - 1) ** 2
k3 = k3 and spotD and D > 0 and h1
rec('CHECK', 'K3', k3, 'det(h0 + x e) = -8x, det(h0\' + x e\') = 8x: |det Psi|^2 = D on all of S (unreachable); H1 at c = 103/100',
    'D %s, 1 - 4D %s <= (2/c - 1)^2 %s' % (D, 1 - 4 * D, (2 / c - 1) ** 2))

# ---------- K4: (CC) and pairings
k4 = c * c * smin >= 4 * (c - 1) and 4 - 2 * c + c * c * smin > 0
rec('CHECK', 'K4', k4, '(CC) c^2 s >= 4(c - 1) for every pair (s >= s_min) and every pairing positive',
    'c^2 s_min %s vs 4(c - 1) %s' % (c * c * smin, 4 * (c - 1)))

# ---------- K5: the defect is not PSD
dh = dvec(h, c)
okd, ed = psd(dh)
rec('CHECK', 'K5', not okd, 'd = I - c P_h is not PSD (K_kappa != Q3)', 'e1..e4 %s' % ed)

# ---------- K6: consequence check of S' on the cross pair
hj, hk = h, vadd(h0p, ep)
te, w = geo(hj, hk, c)
k6 = True; k6rec = []
for t in (te, te / 2):
    v = vpt(hj, w, t)
    dj, dk = dvec(hj, c), dvec(hk, c)
    G = hip(dj, dk).r
    lam = -hip(proj(v), dj).r / G
    y = madd(proj(v), mscale(GQ(lam), dk))
    okp, ey = psd(y)
    k6 &= ovl(hj, v) > 1 / c and hip(y, dj).iszero() and lam > 0 and okp
    k6rec.append('t=%s: s(h_j,v)-1/c=%s, s(h_k,v)=%s vs 1-1/c=%s, PSD %s' % (t, ovl(hj, v) - 1 / c, ovl(hk, v), 1 - 1 / c, okp))
rec('CHECK', 'K6', k6, 'S\' consequence holds on the cross pair at the far cap edge and the midpoint', '; '.join(k6rec))

# ---------- RECORD the table
Th = table(proj(h))
z = [[(Fr(1, 2) if (m, n) == (0, 0) else Fr(0)) - c / 8 * Th[m][n] for n in range(4)] for m in range(4)]
zok = meq(pW(z), mscale(GQ(Fr(1, 8)), dh))
print('RECORD z = E00/2 - (c/8) T_h, h = (6, 2, 1, -1), c = 103/100 (pauliW(z) = d/8: %s): %s' % (zok, [[str(x) for x in r] for r in z]))

# ---------- BC1: computational basis
E = [V(*[1 if t == k else 0 for t in range(4)]) for k in range(4)]
Bc = [[Bf(E[i], E[j]) for j in range(4)] for i in range(4)]
bc1 = meq(Bc, M([[0, 0, 0, Fr(1, 2)], [0, 0, Fr(-1, 2), 0], [0, Fr(-1, 2), 0, 0], [Fr(1, 2), 0, 0, 0]]))
for (p, q) in [(0, 3), (1, 2)]:
    a, b = mv(CNOT, E[p]), mv(CNOT, E[q])
    bc1 &= det(a).iszero() and det(b).iszero() and Bf(a, b).iszero()
rec('CHECK', 'BC1', bc1, 'computational basis: B nonzero only on {00,11} and {01,10}; CNOT carries both Bell circles to products (det identically 0): no Bell-type orbit for T^3 x| D4')

# ---------- BC2: case B basis of C13
def kron2(u, v): return [u[i] * v[j] for i in range(2) for j in range(2)]
def CNOTv(v): return [v[0], v[1], v[3], v[2]]
b1 = kron2(V(2, 3), V(2, GQ(-1, 2))); b2 = CNOTv(b1); b3 = kron2(V(1, 0), V(GQ(1, 2), 2)); b4 = V(10, GQ(-5, 10), GQ(-6, -12), GQ(-6, -12))
bs = [b1, b2, b3, b4]
bc2 = all(ipv(bs[i], bs[j]).iszero() for i in range(4) for j in range(i + 1, 4))
bc2 &= det(b1).iszero() and det(b3).iszero() and not det(b2).iszero() and not det(b4).iszero()
rec('CHECK', 'BC2', bc2, 'case B basis: orthogonal; products exactly b1, b3 (b2 = CNOT b1 and b4 entangled): no pair of product eigenlines survives (12)')

# ---------- BC3: C1 u C2 for kappa with G16
bc3 = True
for y in ys:
    Uy = Ux(y)
    bc3 &= veq(mv(Uy, f4), vsc(y, f4)) and veq(mv(Uy, f1), f1) and veq(mv(Uy, f2), f2) and veq(mv(Uy, f3), f3)
bc3 &= veq(mv(CNOT, f1), f1) and veq(mv(CNOT, f2), f2) and veq(mv(CNOT, f3), f3) and veq(mv(CNOT, f4), vsc(-1, f4))
bc3 &= veq(mv(ZI, f1), f1) and veq(mv(ZI, f2), f2) and veq(mv(ZI, f3), vsc(-1, f3)) and veq(mv(ZI, f4), vsc(-1, f4))
bc3 &= veq(mv(IZ, f1), f2) and veq(mv(IZ, f2), f1) and veq(mv(IZ, f3), f4) and veq(mv(IZ, f4), f3)
bc3 &= all(det(f).iszero() for f in fs) and Bf(f1, f4) == GQ(-1) and Bf(f2, f3) == GQ(1)
bell = all(det(vadd(f1, vsc(xa, f4))).n2() / n2v(vadd(f1, vsc(xa, f4))) ** 2 == Fr(1, 4) and
           det(vadd(f2, vsc(xa, f3))).n2() / n2v(vadd(f2, vsc(xa, f3))) ** 2 == Fr(1, 4) for xa in pts)
bc3 &= bell
rec('CHECK', 'BC3', bc3, 'C1 = {f1 + x f4}, C2 = {f2 + x f3} are Bell-type circles invariant under the kappa generators, I(x)Z swapping them: the c = 2 orbit for kappa with G16 is C1 u C2 (K_T)')

# ---------- CC1: the S2 torus gives an orthogonal partner
mI = GQ(0, -1)
Rz = M([[mI, 0], [0, II]]); Rx = mscale(mI, sx)
g = mmul(kron(Rz, Rx), IZ)
gh = mv(g, h)
cc1 = ipv(h, gh).iszero() and veq(gh, V(2, -6, 1, 1))
rec('COUNTERCONTROL', 'CC1', cc1, 'S2 contrast: (Rz(pi) (x) Rx(pi))(I(x)Z) h = (2, -6, 1, 1) is orthogonal to h (the torus decides)',
    '<h|g h> = %s' % ipv(h, gh))

# ---------- CC2: the H1 window is real
c2 = Fr(26, 25)
cc2 = 1 - 4 * D > (2 / c2 - 1) ** 2
rec('COUNTERCONTROL', 'CC2', cc2, 'at c = 26/25 H1 fails on S', '1 - 4D %s > (2/c - 1)^2 %s' % (1 - 4 * D, (2 / c2 - 1) ** 2))

# ---------- CC3: a reachable entangled state
r = V(2, 0, GQ(1, 1), GQ(1, -1))
r_ok = veq(r, vadd(vadd(f1, f2), vadd(f3, vsc(II, f4))))
Ur = mv(Ux(GQ(0, -1)), r)
cc3 = r_ok and not det(r).iszero() and det(Ur).iszero()
rec('COUNTERCONTROL', 'CC3', cc3, 'r = (2, 0, 1+i, 1-i) is entangled and U(-i) r is a product (the unreachability test is not vacuous)',
    'det r = %s, U(-i) r = %s' % (det(r), Ur))

# ---------- CC4: sharpness at the pair level
cp = Fr(5, 4)
viol = cp * cp * smin < 4 * (cp - 1)
tc, wc = geo(hj, hk, cp)
v = vpt(hj, wc, tc)
cc4 = False; cc4rec = ''
if ovl(hj, v) > 1 / cp and ovl(hk, v) < 1 - 1 / cp:
    dj, dk = dvec(hj, cp), dvec(hk, cp)
    G = hip(dj, dk).r
    lam = -hip(proj(v), dj).r / G
    y = madd(proj(v), mscale(GQ(lam), dk))
    xv = [hk[q] - (ipv(v, hk) / n2v(v)) * v[q] for q in range(4)]
    xyx = ipv(xv, mv(y, xv))
    cc4 = viol and hip(y, dj).iszero() and hip(y, dk).r > 0 and lam > 0 and isreal(xyx) and xyx.r < 0
    cc4rec = 't=%s, s(h_j,v)-1/c\'=%s, s(h_k,v)=%s < 1-1/c\'=%s, x^dag y x=%s' % (tc, ovl(hj, v) - 1 / cp, ovl(hk, v), 1 - 1 / cp, xyx.r)
rec('COUNTERCONTROL', 'CC4', cc4, 'c\' = 5/4 violates (CC) on the cross pair; exact y in K({d_j,d_k})* \\ K({d_j,d_k})', cc4rec)

# ---------- EX and verdict
def nofloat(x):
    if isinstance(x, float): return False
    if isinstance(x, (list, tuple)): return all(nofloat(y) for y in x)
    return True
rec('CHECK', 'EX', nofloat([smin, s_in, D, c, te, tc, z]), 'no float in any recorded value')
nf = sum(1 for q in RES if not q)
print('summary: %d checks, %d failed' % (len(RES), nf))
if nf == 0:
    print('VERDICT C16-KAPPA-BELLCORNER-EXACT: under kappa with G16 the orbit of h = (6, 2, 1, -1) is two circles with '
          'squared overlaps >= %s (no orthogonal pair) and |det Psi|^2 = %s throughout; at c = %s H1 and (CC) hold: an '
          'explicit invariant exotic cone with a continuum of non-PSD extreme rays given Theorem S\'; the Bell corner c = 2: '
          'no Bell-type orbit for T^3 x| D4 or case B, and C1 u C2 (K_T) for kappa with G16' % (smin, D, c))
else:
    print('NO VERDICT')
