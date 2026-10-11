#!/usr/bin/env python3
"""indep_checkE5.py -- coordinator's independent check of research/equivalence, round 5, node E19 (head 3a46b811).

Reads nothing the thread wrote.  Matrix level, with the conventions of the kernel's dictionary as read at L and in
the bridge audit: basis |00>, |01>, |10>, |11> (first factor = block index = the gate's control); the gate
CNOT = blockdiag(1, X) (the module's `cnotMat_eq` states this form, read as a statement); a token operation acts as
L(U) = 1 (x) U = blockdiag(U, U); the clause's flow at angle t acts as F(w) = L(diag(1, w)), |w| = 1 (every w, since
t ranges over R); the cyclic operation cycEquiv, (x, y, z) -> (z, x, y) on Bloch vectors, acts as L(U_c) with
U_c X U_c^+ = Y, U_c Y U_c^+ = Z, U_c Z U_c^+ = X.  Q3 = the PSD cone; H = blockdiag(SU(2), SU(2)).  Everything is
cone invariance under conjugation; nothing here is availability.

Exact arithmetic: Fractions (own Gaussian-rational class) and sympy (symbolic identities in the angles).

Decision rule (fixed before run 1): VERDICT INDEP-E5-FIXED iff Z1-Z7 all PASS and CC1-CC6 all evaluate False;
otherwise VERDICT INDEP-E5-FAILED <items>.

Z1 the generation words, symbolically for all angles: (a) U_c's cyclic action, U_c^3 = -1 and U_c^+ = -U_c^2;
   (b) Euler: [[p, -conj q], [q, conj p]] = diag(a, conj a) R(c, s) diag(b, conj b) with p = c e^{i f1}, q = s e^{i f2},
   a = e^{i(f1-f2)/2}, b = e^{i(f1+f2)/2}, c = cos B, s = sin B; (c) diag(z, conj z) = z diag(1, conj z^2);
   (d) R(c, s) = U_c^+ diag(c - is, c + is) U_c; (e) the controlled diagonal word
   CNOT L(diag(r, conj r)) CNOT L(diag(conj r, r)) = blockdiag(1, diag(conj r^2, r^2)); (f) the controlled real rotation
   L(U_c)^+ blockdiag(1, diag(c - is, c + is)) L(U_c) = blockdiag(1, R(c, s)); (g) blockdiag(U0, U1) =
   blockdiag(1, U1 U0^+) blockdiag(U0, U0).
Z2 end to end, exactly: for three pairs (U0, U1) in SU(2) x SU(2) built from rational points, the explicit product of
   generator matrices (CNOT, F(w), L(U_c) and its inverse as -L(U_c)^2) given by Z1's words equals
   blockdiag(U0, U1) up to a scalar; every factor is one of the generators.
Z3 necessity (N-gen): conjugation by CNOT, F(w), L(U_c) preserves the characteristic polynomial of 6 exact Hermitian
   matrices (so Q3 is invariant under the gate and the clause at every rational-point angle).
Z4 sufficiency chain: H carries a product to every pure state — for 6 exact pure states psi = (a; b) a product phi and
   h in H with h phi = psi exactly (and the product case); hence products in K and H-invariance put every pure state,
   so Q3, inside K, and H3 gives K = Q3 [W].
Z5 group structure: the determinant ratio rho(blockdiag(A, B)) = det B / det A is -1 on CNOT and 1 on F(w), L(U_c)
   and on H; so the clause's operations lie in U(1) H (G': block invariance gives A_miss) and the gate does not.
Z6 the hypotheses' witnesses (exact instances): -Q3 is invariant under every conjugation and self-dual on the tested
   pairs but misses a product (H1 fails); the half-space {tr >= 0} is invariant and holds products but two of its
   elements pair negatively (H3 fails).
Z7 the finite-order part and the dense form: <CNOT, F(i), L(U_c)> is finite modulo phase (exhaustive closure; order
   printed) and does not contain F((3+4i)/5); (3+4i)/5 has no power 1 up to 1000, and cos theta0 = 3/5 lies outside
   Niven's list {0, +-1/2, +-1}, so theta0/pi is irrational.
Countercontrols (each must evaluate False):
CC1 Z1(e)'s word with the gate replaced by the identity gives a nontrivial controlled phase.
CC2 Z1(d) with U_c replaced by the identity gives R(c, s) at s != 0.
CC3 F((3+4i)/5) lies in <CNOT, F(i), L(U_c)> modulo phase.
CC4 CNOT lies in U(1) H (determinant ratio 1).
CC5 the half-space {tr >= 0} is self-dual on the tested pair.
CC6 -Q3 contains the product state |00><00|.

Run from this directory:  python3 -I -B indep_checkE5.py > indep_checkE5.out 2> indep_checkE5.err
"""
from fractions import Fraction as F

import sympy as sp


# ---------------------------------------------------------------- Gaussian rationals and 4x4 / 2x2 matrices
class GQ:
    __slots__ = ('re', 'im')

    def __init__(self, re=0, im=0):
        self.re = F(re)
        self.im = F(im)

    def __add__(self, o):
        o = gq(o)
        return GQ(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __sub__(self, o):
        o = gq(o)
        return GQ(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        return gq(o) - self

    def __mul__(self, o):
        o = gq(o)
        return GQ(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def __neg__(self):
        return GQ(-self.re, -self.im)

    def conj(self):
        return GQ(self.re, -self.im)

    def n2(self):
        return self.re * self.re + self.im * self.im

    def __truediv__(self, o):
        o = gq(o)
        d = o.n2()
        return self * GQ(o.re / d, -o.im / d)

    def __eq__(self, o):
        o = gq(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def zero(self):
        return self.re == 0 and self.im == 0

    def __repr__(self):
        if self.im == 0:
            return str(self.re)
        if self.re == 0:
            return f'{self.im}i'
        return f'({self.re}{"+" if self.im > 0 else "-"}{abs(self.im)}i)'


def gq(x):
    return x if isinstance(x, GQ) else GQ(x, 0)


ONE, ZERO, I1 = GQ(1), GQ(0), GQ(0, 1)


def mm(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum((A[i][t] * B[t][j] for t in range(k)), GQ(0)) for j in range(m)] for i in range(n)]


def dg(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def eye(n):
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


def scal(z, A):
    return [[gq(z) * x for x in row] for row in A]


def block(A, B):
    M = [[ZERO] * 4 for _ in range(4)]
    for i in range(2):
        for j in range(2):
            M[i][j] = A[i][j]
            M[2 + i][2 + j] = B[i][j]
    return M


def L(U):
    return block(U, U)


def m2(a, b, c, d):
    return [[gq(a), gq(b)], [gq(c), gq(d)]]


def det2(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def eq(A, B):
    return all(x == y for ra, rb in zip(A, B) for x, y in zip(ra, rb))


def proportional(A, B):
    """A = z B for a nonzero scalar z"""
    z = None
    for ra, rb in zip(A, B):
        for x, y in zip(ra, rb):
            if y.zero():
                if not x.zero():
                    return False, None
                continue
            q = x / y
            if z is None:
                z = q
            elif not (q == z):
                return False, None
    return (z is not None and not z.zero()), z


def rp(t):
    if t is None:
        return GQ(-1)
    t = F(t)
    return GQ((1 - t * t) / (1 + t * t), 2 * t / (1 + t * t))


X2 = m2(0, 1, 1, 0)
CNOT = block(eye(2), X2)
Uc = [[GQ(F(1, 2), F(-1, 2)), GQ(F(-1, 2), F(-1, 2))], [GQ(F(1, 2), F(-1, 2)), GQ(F(1, 2), F(1, 2))]]


def Fw(w):
    return L(m2(1, 0, 0, w))


LUc = L(Uc)
LUcInv = scal(-1, mm(LUc, LUc))  # L(U_c)^+ = -L(U_c)^2: a word in the cyclic generator

RESULTS, CCS = {}, {}


def check(name, ok, msg):
    RESULTS[name] = bool(ok)
    print(f'[{"PASS" if ok else "FAIL"}] {name}: {msg}', flush=True)


def cc(name, val, msg):
    CCS[name] = bool(val)
    print(f'[CC] {name} = {bool(val)}: {msg}', flush=True)


# ---------------------------------------------------------------- Z1 symbolic words
f1, f2, Bt, al, rh = sp.symbols('f1 f2 B al rh', real=True)
E = sp.exp
sI = sp.I
sX = sp.Matrix([[0, 1], [1, 0]])
sY = sp.Matrix([[0, -sI], [sI, 0]])
sZ = sp.Matrix([[1, 0], [0, -1]])
sUc = sp.Matrix([[(1 - sI) / 2, (-1 - sI) / 2], [(1 - sI) / 2, (1 + sI) / 2]])


def simp0(M):
    return all(sp.simplify(sp.expand(sp.expand_complex(x).rewrite(sp.cos))) == 0 for x in M)


z1a = simp0(sUc * sX * sUc.H - sY) and simp0(sUc * sY * sUc.H - sZ) and simp0(sUc * sZ * sUc.H - sX)
z1a &= simp0(sUc ** 3 + sp.eye(2)) and simp0(sUc.H + sUc ** 2)
c_, s_ = sp.cos(Bt), sp.sin(Bt)
p_, q_ = c_ * E(sI * f1), s_ * E(sI * f2)
U_s = sp.Matrix([[p_, -sp.conjugate(q_)], [q_, sp.conjugate(p_)]])
a_, b_ = E(sI * (f1 - f2) / 2), E(sI * (f1 + f2) / 2)
R_s = sp.Matrix([[c_, -s_], [s_, c_]])
z1b = simp0(sp.diag(a_, sp.conjugate(a_)) * R_s * sp.diag(b_, sp.conjugate(b_)) - U_s)
z_ = E(sI * al)
z1c = simp0(sp.diag(z_, sp.conjugate(z_)) - z_ * sp.diag(1, sp.conjugate(z_) ** 2))
z1d = simp0(sUc.H * sp.diag(c_ - sI * s_, c_ + sI * s_) * sUc - R_s)
r_ = E(sI * rh)


def sblock(A, B):
    return sp.diag(A, B)


def sL(U):
    return sblock(U, U)


sCNOT = sblock(sp.eye(2), sX)
word_e = sCNOT * sL(sp.diag(r_, sp.conjugate(r_))) * sCNOT * sL(sp.diag(sp.conjugate(r_), r_))
z1e = simp0(word_e - sblock(sp.eye(2), sp.diag(sp.conjugate(r_) ** 2, r_ ** 2)))
word_f = sL(sUc).H * sblock(sp.eye(2), sp.diag(c_ - sI * s_, c_ + sI * s_)) * sL(sUc)
z1f = simp0(word_f - sblock(sp.eye(2), R_s))
A0 = sp.Matrix(2, 2, sp.symbols('a0:4'))
A1 = sp.Matrix(2, 2, sp.symbols('b0:4'))
# (g) with U0 unitary: blockdiag(1, U1 U0^+) blockdiag(U0, U0) = blockdiag(U0, U1 U0^+ U0) = blockdiag(U0, U1)
z1g = simp0(sblock(sp.eye(2), A1 * A0.H) * sblock(A0, A0) - sblock(A0, A1 * A0.H * A0))
check('Z1', z1a and z1b and z1c and z1d and z1e and z1f and z1g,
      f'U_c cyclic X->Y->Z->X, U_c^3 = -1, U_c^+ = -U_c^2: {z1a}; Euler form {z1b}; diag(z, conj z) = z diag(1, conj z^2) '
      f'{z1c}; R(c, s) = U_c^+ diag(c - is, c + is) U_c {z1d}; controlled diagonal word {z1e}; controlled real rotation '
      f'{z1f}; assembly identity (with U0^+ U0 = 1) {z1g}')
word_e_nogate = sL(sp.diag(r_, sp.conjugate(r_))) * sL(sp.diag(sp.conjugate(r_), r_))
cc('CC1', not simp0(word_e_nogate - sp.eye(4)),
   'the controlled-diagonal word with the gate replaced by the identity is not the identity')
cc('CC2', simp0(sp.diag(c_ - sI * s_, c_ + sI * s_) - R_s),
   'without the cyclic lift, diag(c - is, c + is) equals R(c, s) identically')

# ---------------------------------------------------------------- Z2 end to end, exact
def word_local_diag(z):  # L(diag(z, conj z)) = z * F(conj z^2): returns (scalar, factor list)
    return z, [('F', Fw(z.conj() * z.conj()))]


def word_local_rot(cs):  # L(R(c, s)) = L(U_c)^+ L(diag(c - is, c + is)) L(U_c), cs = c + is
    sc, fl = word_local_diag(cs.conj())
    return sc, [('LUcInv', LUcInv)] + fl + [('LUc', LUc)]


def word_ctrl_diag(r):  # blockdiag(1, diag(conj r^2, r^2)) = CNOT L(diag(r, conj r)) CNOT L(diag(conj r, r))
    s1, f1_ = word_local_diag(r)
    s2, f2_ = word_local_diag(r.conj())
    return s1 * s2, [('CNOT', CNOT)] + f1_ + [('CNOT', CNOT)] + f2_


def word_ctrl_rot(rr):  # blockdiag(1, R(c, s)) with c + is = rr^2 (so diag(c - is, c + is) = diag(conj rr^2, rr^2))
    sc, fl = word_ctrl_diag(rr)
    return sc, [('LUcInv', LUcInv)] + fl + [('LUc', LUc)]


def euler_V(ra, rr, rb):
    """V = diag(a, conj a) R(c, s) diag(b, conj b) with a = conj ra^2, b = conj rb^2, c + is = rr^2"""
    a = ra.conj() * ra.conj()
    b = rb.conj() * rb.conj()
    cs = rr * rr
    Rm = m2(cs.re, -cs.im, cs.im, cs.re)
    V = mm(mm(m2(a, 0, 0, a.conj()), Rm), m2(b, 0, 0, b.conj()))
    return V, a, b, cs


def product(factors):
    M = eye(4)
    for _, f in factors:
        M = mm(M, f)
    return M


def word_block(U0parts, Vparts):
    """blockdiag(U0, V U0) = blockdiag(1, V) blockdiag(U0, U0); each from rational points (ra, rr, rb)"""
    ra0, rr0, rb0 = U0parts
    U0, a0, b0, cs0 = euler_V(ra0, rr0, rb0)
    raV, rrV, rbV = Vparts
    V, aV, bV, csV = euler_V(raV, rrV, rbV)
    scal_total = ONE
    facs = []
    # blockdiag(1, V) = ctrl(diag(aV)) ctrl(R) ctrl(diag(bV)); ctrl(diag(a)) needs r with conj r^2 = a: r = raV
    for sc, fl in (word_ctrl_diag(raV), word_ctrl_rot(rrV), word_ctrl_diag(rbV)):
        scal_total = scal_total * sc
        facs += fl
    # blockdiag(U0, U0) = L(diag(a0)) L(R0) L(diag(b0)); L(diag(a)) with a = conj ra^2: z = a ... use word_local_diag(a0)
    for sc, fl in (word_local_diag(a0), word_local_rot(cs0), word_local_diag(b0)):
        scal_total = scal_total * sc
        facs += fl
    U1 = mm(V, U0)
    return U0, U1, scal_total, facs


inst = [((rp(F(1, 2)), rp(F(1, 3)), rp(2)), (rp(F(-1, 3)), rp(F(2, 3)), rp(3))),
        ((rp(3), rp(F(-1, 2)), rp(F(1, 5))), (rp(F(1, 7)), rp(F(3, 2)), rp(F(-2, 5)))),
        ((rp(F(2, 7)), rp(F(5, 3)), rp(F(-1, 4))), (rp(F(4, 3)), rp(F(1, 6)), rp(F(-5, 2))))]
z2, msgs = True, []
for U0p, Vp in inst:
    U0, U1, sc, facs = word_block(U0p, Vp)
    ok_su = det2(U0) == ONE and det2(U1) == ONE and eq(mm(U0, dg(U0)), eye(2)) and eq(mm(U1, dg(U1)), eye(2))
    P = product(facs)
    target = block(U0, U1)
    ok_p, z = proportional(scal(sc, P), target)
    names = {n for n, _ in facs}
    ok_gens = names <= {'CNOT', 'F', 'LUc', 'LUcInv'} and all(
        (n != 'F') or (eq(f, Fw(f[1][1])) and f[1][1].n2() == 1) for n, f in facs)
    z2 &= ok_su and ok_p and ok_gens
    msgs.append(f'{len(facs)} factors, SU(2) pair {ok_su}, product = scalar x blockdiag(U0, U1) {ok_p} (scalar {z}), '
                f'factors among CNOT, F(w) with |w| = 1, L(U_c), -L(U_c)^2: {ok_gens}')
check('Z2', z2, '; '.join(msgs))

# ---------------------------------------------------------------- Z3 necessity: Q3 invariant (characteristic polynomial)
lam = sp.symbols('lam')


def to_sp(M):
    return sp.Matrix([[sp.Rational(x.re.numerator, x.re.denominator) + sp.I * sp.Rational(x.im.numerator, x.im.denominator)
                       for x in row] for row in M])


def herm(seed):
    import random
    rng = random.Random(seed)
    M = [[ZERO] * 4 for _ in range(4)]
    for i in range(4):
        M[i][i] = GQ(rng.randint(-3, 5))
        for j in range(i + 1, 4):
            v = GQ(rng.randint(-3, 3), rng.randint(-3, 3))
            M[i][j] = v
            M[j][i] = v.conj()
    return M


z3 = True
for sd in range(6):
    Hm = herm(100 + sd)
    cp = sp.expand(to_sp(Hm).charpoly(lam).as_expr())
    for G in (CNOT, Fw(rp(F(1, 2))), Fw(rp(F(-3, 7))), LUc):
        Hc = mm(mm(G, Hm), dg(G))
        z3 &= sp.expand(to_sp(Hc).charpoly(lam).as_expr() - cp) == 0
check('Z3', z3, f'characteristic polynomial preserved by CNOT, F(w) (two w) and L(U_c) on 6 exact Hermitian matrices: {z3}')

# ---------------------------------------------------------------- Z4 H carries products to every pure state
def su_from_col(v, nv):
    """the SU(2) matrix [[v0, -conj v1], [v1, conj v0]]/nv, first column v/nv"""
    return [[v[0] / nv, (v[1].conj() * -1) / nv], [v[1] / nv, v[0].conj() / nv]]


pure = [
    ((GQ(3), GQ(0, 4)), (GQ(1, 2), GQ(2)), F(5), F(3)),
    ((GQ(5), GQ(12)), (GQ(0, 3), GQ(4)), F(13), F(5)),
    ((GQ(2, 1), GQ(2, -4)), (GQ(6), GQ(0, 8)), F(5), F(10)),
    ((GQ(1, 0), GQ(0)), (GQ(0), GQ(0, 1)), F(1), F(1)),
    ((GQ(4, 3), GQ(0)), (GQ(0), GQ(3, 4)), F(5), F(5)),
    ((GQ(0), GQ(0)), (GQ(3), GQ(4)), F(0), F(5)),
]
z4, m4 = True, []
for a, b, na, nb in pure:
    psi = [a[0], a[1], b[0], b[1]]
    U0 = su_from_col(a, na) if na != 0 else eye(2)
    U1 = su_from_col(b, nb) if nb != 0 else eye(2)
    h = block(U0, U1)
    phi = [gq(na), ZERO, gq(nb), ZERO]  # (na|0> + nb|1>) (x) |0>: a product
    hp = mm(h, [[x] for x in phi])
    ok = all(hp[i][0] == psi[i] for i in range(4)) and det2(U0) == ONE and det2(U1) == ONE
    # phi is a product: det Psi(phi) = phi0 phi3 - phi1 phi2 = 0
    ok &= (phi[0] * phi[3] - phi[1] * phi[2]).zero()
    z4 &= ok
check('Z4', z4, f'6 pure states (including products and one with a zero block) reached from a product by an element of H: {z4}')

# ---------------------------------------------------------------- Z5 determinant ratio
def rho(M):
    A = [[M[0][0], M[0][1]], [M[1][0], M[1][1]]]
    B = [[M[2][2], M[2][3]], [M[3][2], M[3][3]]]
    off = all(M[i][j].zero() for i in range(4) for j in range(4) if (i < 2) != (j < 2))
    return off, det2(B) / det2(A)


r_cnot = rho(CNOT)
r_f = rho(Fw(rp(F(1, 3))))
r_c = rho(LUc)
U0, U1, _, _ = word_block(*inst[0])
r_h = rho(block(U0, U1))
z5 = r_cnot == (True, GQ(-1)) and r_f == (True, ONE) and r_c == (True, ONE) and r_h == (True, ONE)
check('Z5', z5, f'rho(CNOT) = {r_cnot[1]}, rho(F(w)) = {r_f[1]}, rho(L(U_c)) = {r_c[1]}, rho(blockdiag(U0, U1)) = {r_h[1]}')
cc('CC4', r_cnot[1] == ONE, 'CNOT has determinant ratio 1 (would lie in U(1) H)')

# ---------------------------------------------------------------- Z6 the hypotheses' witnesses
def trace_pair(A, B):
    return sum((A[i][k] * B[k][i] for i in range(4) for k in range(4)), GQ(0)).re


P00 = [[ONE if (i == 0 and j == 0) else ZERO for j in range(4)] for i in range(4)]
# -Q3: conjugation maps -PSD to -PSD (Z3's characteristic polynomials apply to -H as well); self-duality of -Q3 is
# structural ((-Q3)* = -(Q3*) = -Q3); H1 fails: P00 is PSD and nonzero, so P00 is not in -Q3 (its negative is).
negP00 = scal(-1, P00)
negQ3_has_P00 = all(negP00[i][i].re >= 0 for i in range(4))  # P00 in -Q3 iff -P00 is PSD; a PSD matrix has a nonnegative diagonal
# half-space T = {tr >= 0}: invariant (trace), holds products (trace 1), not self-dual: x, y in T with tr(xy) < 0.
xT = [[gq(v) if i == j else ZERO for j, _ in enumerate(range(4))] for i, v in enumerate([1, F(-1, 2), 0, 0])]
yT = [[gq(v) if i == j else ZERO for j, _ in enumerate(range(4))] for i, v in enumerate([0, 1, 0, 0])]
trx = sum((xT[i][i] for i in range(4)), GQ(0)).re
try_ = sum((yT[i][i] for i in range(4)), GQ(0)).re
pxy = trace_pair(xT, yT)
inv_tr = all(sum((mm(mm(G, xT), dg(G))[i][i] for i in range(4)), GQ(0)).re == trx for G in (CNOT, Fw(rp(2)), LUc))
z6 = (not negQ3_has_P00) and trx >= 0 and try_ >= 0 and pxy < 0 and inv_tr and \
    sum((P00[i][i] for i in range(4)), GQ(0)).re == 1
check('Z6', z6, f'-Q3 misses the product |00><00| (H1 fails; invariant and self-dual structurally); half-space: tr x = {trx}, '
                f'tr y = {try_}, tr(xy) = {pxy} < 0 (H3 fails), trace preserved by the generators {inv_tr}, products in it')
cc('CC5', pxy >= 0, 'the tested pair of the half-space pairs nonnegatively')
cc('CC6', negQ3_has_P00, '-Q3 contains |00><00|')

# ---------------------------------------------------------------- Z7 finite-order part; dense form
def normalize(M):
    for row in M:
        for x in row:
            if not x.zero():
                inv = ONE / x
                return tuple(tuple(y * inv for y in r) for r in M)


def closure(gens, cap=50000):
    start = normalize(eye(4))
    seen = {start}
    frontier = [start]
    while frontier:
        nxt = []
        for a in frontier:
            A = [list(r) for r in a]
            for G in gens:
                b = normalize(mm(A, G))
                if b not in seen:
                    seen.add(b)
                    nxt.append(b)
                    if len(seen) > cap:
                        return seen, False
        frontier = nxt
    return seen, True


grp, finite = closure([CNOT, Fw(I1), LUc])
w0 = GQ(F(3, 5), F(4, 5))
has_w0 = normalize(Fw(w0)) in grp
pw, ok_pow = ONE, True
for n in range(1, 1001):
    pw = pw * w0
    if pw == ONE:
        ok_pow = False
        break
niven = F(3, 5) not in {F(0), F(1, 2), F(-1, 2), F(1), F(-1)}
z7 = finite and (not has_w0) and ok_pow and niven
check('Z7', z7, f'<CNOT, F(i), L(U_c)> finite modulo phase: {finite} (order {len(grp)}); F((3+4i)/5) in it: {has_w0}; '
                f'no power of (3+4i)/5 up to 1000 is 1: {ok_pow}; cos theta0 = 3/5 outside Niven list: {niven}')
cc('CC3', has_w0, 'F((3+4i)/5) lies in the finite-order group modulo phase')

fails = [k for k, ok in RESULTS.items() if not ok] + [k for k, v in CCS.items() if v]
print()
print(f'PASS {sum(RESULTS.values())}/{len(RESULTS)}; countercontrols False {sum(1 for v in CCS.values() if not v)}/{len(CCS)}')
print('VERDICT INDEP-E5-FIXED' if not fails else 'VERDICT INDEP-E5-FAILED ' + ' '.join(fails))
