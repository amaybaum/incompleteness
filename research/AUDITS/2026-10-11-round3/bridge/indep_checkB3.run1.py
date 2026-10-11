#!/usr/bin/env python3
"""indep_checkB3.py -- coordinator's independent check of research/bridge round 3 (nodes B10-B13).

Written from the thread's claims (NOTES-B10..B13, RESULTS rows B10-1..B13-2, HP-7..HP-10) and from the kernel's own
definitions at L = 9f9f8257 (CompositeDimension.lean: `sgn`/`pc`/`pt`/`cnotFun` :741-:758, `homMap` :112, `actT` :198,
`actC` :201, `nflip` :797, `tens` :1450; KInfFoundations.lean: `rotFun` :351, `cycEquiv` :416), transcribed here.
Reads nothing from the thread's scripts, outputs or modules.  Exact arithmetic throughout (sympy Rational, Fraction,
own Gaussian-rational and Q(sqrt5) classes).  Conventions: tables 4x4 with the control index first; pauliW(w) =
1/4 sum w_{mu nu} sigma_mu (x) sigma_nu; tab(M)_{mu nu} = tr(T_{mu nu} M); actT N w = w hom(N)^T, actC N w = hom(N) w
(the kernel's homMap: v -> (v0, N(tail v))); Z_F = the four Bell-type defects z(s1,s2) = (E00 + s1 E13 + s2 E22 -
s1 s2 E31)/4 of the stage-4 record (as in the coordinator's round-1/2 checks), psi_s the unit vector in the kernel of
pauliW(z_s) + I/8.

DECISION RULE (fixed before run 1): VERDICT INDEP-B3-FIXED iff X1..X4 all PASS; otherwise VERDICT INDEP-B3-OPEN with
the failing ids.  Each check is a conjunction of the assertions in its docstring.

  X1  B11 (D1)/(D2) against the kernel's definitions: the kernel's `cnotFun` (sgn, pc, pt tables) equals Ad(CNOT) through
      the dictionary on all 16 basis tables; actT (rotZ c s) = Ad(1 (x) diag(1, c + i s)) and actC = Ad(diag (x) 1) at the
      circle points (3/5, 4/5), (-5/13, 12/13) and symbolically on c^2 + s^2 = 1; the kernel's `nflip` = diag(1,-1,-1)
      gives Ad(1 (x) X) / Ad(X (x) 1); countercontrol: at (c, s) = (0, 0) the phase conjugation does not fix sigma_0;
      tens/prodState law pauliW(prodState x y) = rho(x) (x) rho(y).
  X2  B10: nflip on either token permutes Z_F (T1) and is a signed permutation of the 16 coordinates; R_z(pi) on the
      target permutes Z_F (T6, V4); actT R_z(theta0), cos theta0 = 3/5, carries some defect of Z_F to a table pairing
      negatively with a certified member of K(Z_F) (T4's content: (A) fails); 2 cos theta0 = 6/5 is not an algebraic
      integer; tr(actT R_z(theta0)) = 64/5 on W 3 and tr(cnot o actT R_z(theta0)) = 16/5 (T7, B12 U4); the groups
      G_n = <CNOT, 1 (x) diag(1, w_n), 1 (x) X>, w_n = exp(2 pi i/2^n), have orders 16, 64, 256, 1024 modulo phase and
      G_n <= G_{n+1} (T8); the Lie closure of {1 (x) Z} under Ad(CNOT), Ad(1 (x) X) and commutators is span{1 (x) Z, Z (x) Z}
      (dimension 2, abelian), and with Ad(1 (x) U_J) it has dimension 6 = span{1 (x) X, 1 (x) Y, 1 (x) Z, Z (x) X, Z (x) Y, Z (x) Z},
      every element commuting with Z (x) 1 (T9, B12 U6); the 3-4-5 rotation's Bloch image is a rotation with trace 11/25
      about the y axis (T10).
  X3  B12: table-group orders <cnot, actT J> = 48 (integer traces; E(3,0) fixed), <cnot, actT J, actT S, actT nflip> = 384
      = <cnot, actT S, actT J>, the two-qubit Clifford group <cnot, actC J, actT J, actC S, actT S> has order 11520, the
      stabiliser of E(3,0) in it is the 384 group and E(3,0)'s orbit has 30 elements (U1, U2); the G1-orbit of the 36
      octahedral product rays has 60 rays whose tables span 16 dimensions (U3); for m = 1..24 the minimal polynomial of
      -1 - sin(2 pi/m) is monic over Z exactly for m in {1, 2, 4} (control: 2 cos(2 pi/m) monic for all m; countercontrol:
      cos(2 pi/m) monic exactly for m in {1, 2, 4}) (U5, V1); |<J, R_z(pi)>| = 12, |<J, R_z(pi/2)>| = 24; with
      u = (phi - 1, phi, 1)/2 the group <J, R_z(pi), 2 u u^T - 1> has order 60 and its only z-axis rotations are 1 and
      R_z(pi) (V2, V3); phi0 = (1, 2, 3i, -1+i)/4 is (P0 (x) U0 + P1 (x) U1)(a (x) |0>) with a = (sqrt5, sqrt11)/4, and no
      element of the 384 group carries phi0's table to a product table (U6); the word-length stage Lambda_1 =
      G1 . (Lambda_0 u R Lambda_0 u R^{-1} Lambda_0), R = 1 (x) diag(1, (3+4i)/5), has 588 rays, R Lambda_0 is not inside
      Lambda_0 and R Lambda_1 is not inside Lambda_1 (U7).
  X4  B13 controls: prodDet(1,2,3,5) = -1 and prodDet(CNOT(1,2,3,5)) = -7; the polarisation identity
      prodDet(x + t y) = prodDet x + prodCross(x,y) t + prodDet(y) t^2 (symbolic); a quadratic in t with three distinct
      roots is zero (instance); for two unitaries (1 and CNOT) the line v + n w with v = 0, w = (1,2,3,5) has a common
      non-root among n in {0,..,4} (2|s| + 1 = 5 points).
"""
import sys
import itertools
from fractions import Fraction as Fr
import sympy as sp
from sympy import Matrix, Rational as R, I, eye, zeros, sqrt, simplify, expand, symbols, kronecker_product as kron, pi, cos, sin

results = {}

# ---------------------------------------------------------------- shared sympy machinery (tables, dictionary)
I2 = eye(2); SX = Matrix([[0, 1], [1, 0]]); SY = Matrix([[0, -I], [I, 0]]); SZ = Matrix([[1, 0], [0, -1]])
SG = [I2, SX, SY, SZ]
KR = {(m, n): kron(SG[m], SG[n]) for m in range(4) for n in range(4)}


def pauliW(w):
    return sum((w[m, n] * KR[(m, n)] for m in range(4) for n in range(4) if w[m, n] != 0), zeros(4, 4)) / 4


def tab(M):
    out = zeros(4, 4)
    for m in range(4):
        for n in range(4):
            e = expand((KR[(m, n)] * M).trace())
            if not e.is_Rational:
                e = sp.nsimplify(simplify(e))
            out[m, n] = e
    return out


def ipW(a, b):
    return expand(sum(a[i, j] * b[i, j] for i in range(4) for j in range(4)))


def E(m, n):
    B = zeros(4, 4); B[m, n] = 1; return B


def homMap(N):  # kernel: homMap N v = (v 0, N (tail v))
    M = eye(4)
    for i in range(3):
        for j in range(3):
            M[i + 1, j + 1] = N[i, j]
    return M


def actT(N, w):
    return w * homMap(N).T


def actC(N, w):
    return homMap(N) * w


def prodState(x, y):
    return Matrix([1] + list(x)) * Matrix([1] + list(y)).T


CNOT = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

# kernel gate transcribed from CompositeDimension.lean:741-758 at L
SGN = {(1, 3): -1, (2, 2): -1}
PC = {(0, 0): 0, (0, 1): 0, (0, 2): 3, (0, 3): 3, (1, 0): 1, (1, 1): 1, (1, 2): 2, (1, 3): 2,
      (2, 0): 2, (2, 1): 2, (2, 2): 1, (2, 3): 1, (3, 0): 3, (3, 1): 3, (3, 2): 0, (3, 3): 0}
PT = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3, (1, 0): 1, (1, 1): 0, (1, 2): 3, (1, 3): 2,
      (2, 0): 1, (2, 1): 0, (2, 2): 3, (2, 3): 2, (3, 0): 0, (3, 1): 1, (3, 2): 2, (3, 3): 3}


def cnotFun(w):
    return Matrix(4, 4, lambda m, n: SGN.get((m, n), 1) * w[PC[(m, n)], PT[(m, n)]])


NFLIP = sp.diag(1, -1, -1)                      # kernel nflip: x -> (x0, -x1, -x2)


def rotZ(c, s):
    return Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])  # kernel rotFun


CYC = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])  # kernel cycEquiv: (x, y, z) -> (z, x, y), i.e. e0 -> e1 -> e2 -> e0
UJ = (I2 - I * (SX + SY + SZ)) / 2
SGATE = sp.diag(1, I)


def zdef(s1, s2):
    return (E(0, 0) + s1 * E(1, 3) + s2 * E(2, 2) - s1 * s2 * E(3, 1)) / 4


SS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
ZF = {s: zdef(*s) for s in SS}


def vec(M):
    return tuple(M[i, j] for i in range(4) for j in range(4))


def norm2(v):
    return expand((v.H * v)[0])


def ovl2(a, v):
    c = (a.H * v)[0]
    return expand(c * sp.conjugate(c))


def negvec(w):
    v = (pauliW(w) + eye(4) / 8).nullspace()[0]
    return v / sqrt(norm2(v))


PSI = {s: negvec(ZF[s]) for s in SS}


def lin16(f):
    """16x16 matrix of a linear table map f (columns = images of the basis tables)."""
    M = zeros(16, 16)
    for m in range(4):
        for n in range(4):
            img = f(E(m, n))
            for m2 in range(4):
                for n2 in range(4):
                    M[4 * m2 + n2, 4 * m + n] = img[m2, n2]
    return M


# ---------------------------------------------------------------- X1
def X1():
    ok = True
    # kernel cnotFun = Ad(CNOT) on all basis tables
    a1 = all(cnotFun(E(m, n)) == tab(CNOT * pauliW(E(m, n)) * CNOT.H) for m in range(4) for n in range(4))
    ok &= a1
    # the kernel's cnot is an involution and a signed permutation
    ok &= all(cnotFun(cnotFun(E(m, n))) == E(m, n) for m in range(4) for n in range(4))
    # rotZ at rational circle points, both tokens
    a2 = True
    for (c, s) in ((R(3, 5), R(4, 5)), (R(-5, 13), R(12, 13))):
        U = sp.diag(1, c + s * I)
        for m in range(4):
            for n in range(4):
                w = E(m, n)
                a2 &= actT(rotZ(c, s), w) == tab(kron(I2, U) * pauliW(w) * kron(I2, U).H)
                a2 &= actC(rotZ(c, s), w) == tab(kron(U, I2) * pauliW(w) * kron(U, I2).H)
    ok &= a2
    # symbolic on the circle
    c, s = symbols('c s', real=True)
    U = sp.diag(1, c + s * I)
    a3 = True
    for m in range(4):
        for n in range(4):
            w = E(m, n)
            lhs = actT(rotZ(c, s), w)
            rhs = kron(I2, U) * pauliW(w) * kron(I2, U).H
            rhs_tab = Matrix(4, 4, lambda i, j: expand((KR[(i, j)] * rhs).trace()).subs(s ** 2, 1 - c ** 2))
            a3 &= simplify(lhs - rhs_tab) == zeros(4, 4)
    ok &= a3
    # nflip
    a4 = all(actT(NFLIP, E(m, n)) == tab(kron(I2, SX) * pauliW(E(m, n)) * kron(I2, SX).H) and
             actC(NFLIP, E(m, n)) == tab(kron(SX, I2) * pauliW(E(m, n)) * kron(SX, I2).H)
             for m in range(4) for n in range(4))
    ok &= a4
    # countercontrol at (0, 0)
    U0 = sp.diag(1, 0)
    ok &= (U0 * I2 * U0.H) != I2
    # product law
    a5 = True
    for x, y in (((R(1, 2), R(1, 3), 0), (0, R(2, 5), R(-1, 2))), ((1, 0, 0), (0, 0, 1)), ((R(3, 5), 0, R(4, 5)), (R(-1, 2), R(1, 2), 0))):
        rho = lambda v: (I2 + v[0] * SX + v[1] * SY + v[2] * SZ) / 2
        a5 &= pauliW(prodState(x, y)) == kron(rho(x), rho(y))
    ok &= a5
    results['X1'] = bool(ok)
    print(f"X1 kernel cnotFun = Ad(CNOT) {a1}; actT/actC rotZ = Ad(phase) at rational points {a2}, symbolic {a3}; nflip {a4}; "
          f"countercontrol at (0,0); product law {a5}: {'PASS' if ok else 'FAIL'}")


# ---------------------------------------------------------------- X2
def is_signed_perm(M16):
    for j in range(16):
        col = [M16[i, j] for i in range(16)]
        nz = [x for x in col if x != 0]
        if len(nz) != 1 or abs(nz[0]) != 1:
            return False
    return True


def X2():
    ok = True
    ZSET = set(vec(ZF[s]) for s in SS)
    permZ = lambda f: set(vec(f(ZF[s])) for s in SS) == ZSET
    t1 = permZ(lambda w: actT(NFLIP, w)) and permZ(lambda w: actC(NFLIP, w))
    t1 &= is_signed_perm(lin16(lambda w: actT(NFLIP, w))) and is_signed_perm(lin16(lambda w: actC(NFLIP, w)))
    ok &= t1
    t6 = permZ(lambda w: actT(rotZ(-1, 0), w))
    ok &= t6
    # certified members of K(Z_F): pure states of Q3 n Z_F* (|<psi_t|v>|^2 <= |v|^2/2) and the defects
    GSET = [0, 1, -1, I, -I, 1 + I, 1 - I, 2]
    def psi_comb(co):
        return sum((cc * PSI[s] for cc, s in zip(co, SS)), zeros(4, 1))
    def in_A(v):
        n = norm2(v)
        return n != 0 and all(ovl2(PSI[t], v) <= n / 2 for t in SS)
    pool = []
    for co in itertools.product(GSET, repeat=4):
        v = psi_comb(list(co))
        if in_A(v):
            pool.append(tab(v * v.H))
        if len(pool) >= 120:
            break
    pool += list(ZF.values())
    Rth = rotZ(R(3, 5), R(4, 5))
    negs = [(s, simplify(ipW(actT(Rth, ZF[s]), y))) for s in SS for y in pool if simplify(ipW(actT(Rth, ZF[s]), y)) < 0]
    t4 = len(negs) > 0
    ok &= t4
    # positive control: the V4 element R_z(pi) pairs nonnegatively with the pool on every defect image
    t6b = all(simplify(ipW(actT(rotZ(-1, 0), ZF[s]), y)) >= 0 for s in SS for y in pool)
    ok &= t6b
    # T7: 2 cos theta0 = 6/5 not an algebraic integer; traces
    x = symbols('x')
    mp = sp.minimal_polynomial(R(6, 5), x)
    ok &= sp.Poly(mp, x).LC() != 1
    A = lin16(lambda w: actT(Rth, w))
    Cm = lin16(cnotFun)
    tr1 = A.trace(); tr2 = (Cm * A).trace()
    ok &= tr1 == R(64, 5) and tr2 == R(16, 5)
    ok &= homMap(Rth).trace() == R(16, 5)
    # T8: G_n orders modulo phase
    def monomial_closure(n):
        mod = 2 ** n
        def norm(el):
            perm, ph = el
            p0 = ph[0]
            return (perm, tuple((p - p0) % mod for p in ph))
        def comp(a, b):  # a after b
            pa, fa = a; pb, fb = b
            return norm((tuple(pa[pb[j]] for j in range(4)), tuple((fb[j] + fa[pb[j]]) % mod for j in range(4))))
        gens = [norm(((0, 1, 3, 2), (0, 0, 0, 0))), norm(((0, 1, 2, 3), (0, 1, 0, 1))), norm(((1, 0, 3, 2), (0, 0, 0, 0)))]
        ident = norm(((0, 1, 2, 3), (0, 0, 0, 0)))
        seen = {ident}; frontier = [ident]
        while frontier:
            new = []
            for g in frontier:
                for h in gens:
                    k = comp(h, g)
                    if k not in seen:
                        seen.add(k); new.append(k)
            frontier = new
        return seen
    orders = {}
    groups = {}
    for n in range(1, 5):
        G = monomial_closure(n)
        orders[n] = len(G); groups[n] = G
    t8 = all(orders[n] == 4 ** (n + 1) for n in range(1, 5))
    # inclusion G_n <= G_{n+1}: re-encode phases of G_n in units of 2^{n+1}
    for n in range(1, 4):
        lifted = {(perm, tuple(2 * p for p in ph)) for perm, ph in groups[n]}
        t8 &= lifted <= groups[n + 1]
    ok &= t8
    # T9 / U6: Lie closures
    def herm_closure(gens, conj):
        def vecr(M):
            return [sp.re(M[i, j]) for i in range(4) for j in range(4)] + [sp.im(M[i, j]) for i in range(4) for j in range(4)]
        basis = list(gens)
        while True:
            cand = list(basis)
            for g in conj:
                for Bm in basis:
                    cand.append(simplify(g * Bm * g.H))
            for A_ in basis:
                for B_ in basis:
                    cand.append(simplify(I * (A_ * B_ - B_ * A_)))
            Mv = Matrix([vecr(simplify(C)) for C in cand])
            rk = Mv.rank()
            if rk == len(basis):
                return basis
            # extract an independent subset
            newb = []
            rows = []
            for C in cand:
                rows.append(vecr(simplify(C)))
                if Matrix(rows).rank() == len(newb) + 1:
                    newb.append(simplify(C))
                else:
                    rows.pop()
            basis = newb
    ZB = kron(I2, SZ)
    L2 = herm_closure([ZB], [CNOT, kron(I2, SX)])
    t9 = len(L2) == 2
    span_target = Matrix([[sp.re(M[i, j]) for i in range(4) for j in range(4)] + [sp.im(M[i, j]) for i in range(4) for j in range(4)]
                          for M in (kron(I2, SZ), kron(SZ, SZ))])
    t9 &= Matrix.vstack(span_target, Matrix([[sp.re(M[i, j]) for i in range(4) for j in range(4)] + [sp.im(M[i, j]) for i in range(4) for j in range(4)] for M in L2])).rank() == 2
    t9 &= all(simplify(A_ * B_ - B_ * A_) == zeros(4, 4) for A_ in L2 for B_ in L2)
    L6 = herm_closure([ZB], [CNOT, kron(I2, SX), kron(I2, UJ)])
    t9 &= len(L6) == 6
    tgt6 = [kron(I2, SX), kron(I2, SY), kron(I2, SZ), kron(SZ, SX), kron(SZ, SY), kron(SZ, SZ)]
    rows6 = Matrix([[sp.re(M[i, j]) for i in range(4) for j in range(4)] + [sp.im(M[i, j]) for i in range(4) for j in range(4)] for M in tgt6 + L6])
    t9 &= rows6.rank() == 6
    ZA = kron(SZ, I2)
    t9 &= all(simplify(ZA * B_ - B_ * ZA) == zeros(4, 4) for B_ in L6)
    t9 &= any(simplify(A_ * B_ - B_ * A_) != zeros(4, 4) for A_ in L6 for B_ in L6)
    ok &= t9
    # T10: the 3-4-5 rotation's Bloch image
    U345 = Matrix([[R(3, 5), R(-4, 5)], [R(4, 5), R(3, 5)]])
    Rb = zeros(3, 3)
    for k in range(3):
        img = simplify(U345 * SG[k + 1] * U345.H)
        for j in range(3):
            Rb[j, k] = simplify((SG[j + 1] * img).trace() / 2)
    t10 = Rb.trace() == R(11, 25) and Rb * Matrix([0, 1, 0]) == Matrix([0, 1, 0]) and simplify(Rb.T * Rb - eye(3)) == zeros(3, 3) and Rb.det() == 1
    ok &= t10
    results['X2'] = bool(ok)
    print(f"X2 B10: nflip permutes Z_F on both tokens (signed perms) {t1}; R_z(pi) permutes Z_F {t6} and pairs >= 0 {t6b}; "
          f"R_z(theta0) excluded with {len(negs)} negative pairings (e.g. {negs[0] if negs else None}); 6/5 not an algebraic "
          f"integer; traces {tr1}, {tr2}; G_n orders {orders} with inclusions {t8}; Lie closures dim {len(L2)} (abelian), "
          f"{len(L6)} (non-abelian, commuting with Z(x)1) {t9}; 3-4-5 Bloch trace {Rb.trace()} {t10}: {'PASS' if ok else 'FAIL'}")


# ---------------------------------------------------------------- Gaussian rationals and Q(sqrt5) for X3
class GQ:
    __slots__ = ('a', 'b')

    def __init__(self, a, b=0):
        self.a = a if isinstance(a, Fr) else Fr(a)
        self.b = b if isinstance(b, Fr) else Fr(b)

    def __add__(self, o): return GQ(self.a + o.a, self.b + o.b)
    def __sub__(self, o): return GQ(self.a - o.a, self.b - o.b)
    def __mul__(self, o): return GQ(self.a * o.a - self.b * o.b, self.a * o.b + self.b * o.a)
    def __neg__(self): return GQ(-self.a, -self.b)
    def conj(self): return GQ(self.a, -self.b)
    def norm2(self): return self.a * self.a + self.b * self.b

    def __truediv__(self, o):
        n = o.norm2(); p = self * o.conj()
        return GQ(p.a / n, p.b / n)

    def iszero(self): return self.a == 0 and self.b == 0
    def __eq__(self, o): return self.a == o.a and self.b == o.b
    def __hash__(self): return hash((self.a, self.b))


Z0 = GQ(0); ONE = GQ(1); IU = GQ(0, 1)


def gmat(rows): return [[x if isinstance(x, GQ) else GQ(x) for x in r] for r in rows]
def gmul(A, B): return [[sum((A[i][k] * B[k][j] for k in range(len(B))), Z0) for j in range(len(B[0]))] for i in range(len(A))]
def gadj(A): return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]
def gvec(A, v): return tuple(sum((A[i][k] * v[k] for k in range(len(v))), Z0) for i in range(len(A)))
def gkron(A, B):
    m, n, p, q = len(A), len(A[0]), len(B), len(B[0])
    return [[A[i // p][j // q] * B[i % p][j % q] for j in range(n * q)] for i in range(m * p)]
def gtrace(A): return sum((A[i][i] for i in range(len(A))), Z0)
def gnorm2(v): return sum(x.norm2() for x in v)
def ginner(u, v): return sum((u[i].conj() * v[i] for i in range(len(u))), Z0)


def ray(v):
    for x in v:
        if not x.iszero():
            return tuple((y / x).a for y in v) + tuple((y / x).b for y in v)
    raise ValueError


def unray(key):
    n = len(key) // 2
    return tuple(GQ(key[i], key[n + i]) for i in range(n))


gI2 = gmat([[1, 0], [0, 1]]); gX = gmat([[0, 1], [1, 0]]); gY = [[Z0, -IU], [IU, Z0]]; gZ = gmat([[1, 0], [0, -1]])
gPAULI = [gI2, gX, gY, gZ]
gS = [[ONE, Z0], [Z0, IU]]
half = GQ(Fr(1, 2))
gUJ = [[half * (ONE - IU), half * (-ONE - IU)], [half * (ONE - IU), half * (ONE + IU)]]
gCNOT = gmat([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
gRth = [[ONE, Z0], [Z0, GQ(Fr(3, 5), Fr(4, 5))]]
gRthInv = [[ONE, Z0], [Z0, GQ(Fr(3, 5), Fr(-4, 5))]]
gTT = [[gkron(gPAULI[m], gPAULI[n]) for n in range(4)] for m in range(4)]


def table_action(U):
    Ud = gadj(U)
    perm = [None] * 16; sign = [None] * 16
    for m in range(4):
        for n in range(4):
            C = gmul(gmul(U, gTT[m][n]), Ud)
            hits = []
            for m2 in range(4):
                for n2 in range(4):
                    t = gtrace(gmul(gTT[m2][n2], C))
                    if not t.iszero():
                        hits.append((m2, n2, GQ(t.a / 4, t.b / 4)))
            assert len(hits) == 1 and hits[0][2].b == 0 and abs(hits[0][2].a) == 1
            perm[4 * m + n] = 4 * hits[0][0] + hits[0][1]
            sign[4 * m + n] = int(hits[0][2].a)
    return (tuple(perm), tuple(sign))


def compose(g, h):
    pg, sg = g; ph, sh = h
    return (tuple(pg[ph[i]] for i in range(16)), tuple(sg[ph[i]] * sh[i] for i in range(16)))


def closure(gens):
    ident = (tuple(range(16)), tuple([1] * 16))
    seen = {ident}; frontier = [ident]
    while frontier:
        new = []
        for g in frontier:
            for s_ in gens:
                h = compose(s_, g)
                if h not in seen:
                    seen.add(h); new.append(h)
        frontier = new
    return seen


def orbit_rays(gens, starts):
    seen = set(ray(v) for v in starts)
    frontier = list(seen)
    while frontier:
        new = []
        for key in frontier:
            w = unray(key)
            for U in gens:
                k2 = ray(gvec(U, w))
                if k2 not in seen:
                    seen.add(k2); new.append(k2)
        frontier = new
    return seen


def apply_signed(g, tvec):  # table as 16-tuple of Fractions under the signed permutation
    out = [Fr(0)] * 16
    for i in range(16):
        out[g[0][i]] += g[1][i] * tvec[i]
    return tuple(out)


def table_of_ray(v):  # tab(v v^H) / |v|^2 as 16 Fractions, control index first
    n = gnorm2(v)
    P = [[v[i] * v[j].conj() for j in range(4)] for i in range(4)]
    out = []
    for m in range(4):
        for n_ in range(4):
            t = gtrace(gmul(gTT[m][n_], P))
            assert t.b == 0
            out.append(t.a / n)
    return tuple(out)


class Q5:
    __slots__ = ('a', 'b')

    def __init__(self, a, b=0):
        self.a = a if isinstance(a, Fr) else Fr(a); self.b = b if isinstance(b, Fr) else Fr(b)

    def __add__(self, o): return Q5(self.a + o.a, self.b + o.b)
    def __sub__(self, o): return Q5(self.a - o.a, self.b - o.b)
    def __mul__(self, o): return Q5(self.a * o.a + 5 * self.b * o.b, self.a * o.b + self.b * o.a)
    def __eq__(self, o): return self.a == o.a and self.b == o.b
    def __hash__(self): return hash((self.a, self.b))


def q5mat(rows): return [[x if isinstance(x, Q5) else Q5(x) for x in r] for r in rows]
def q5mul(A, B): return [[sum((A[i][k] * B[k][j] for k in range(3)), Q5(0)) for j in range(3)] for i in range(3)]
def q5key(A): return tuple((A[i][j].a, A[i][j].b) for i in range(3) for j in range(3))


def q5closure(gens):
    ident = q5mat([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    seen = {q5key(ident): ident}; frontier = [ident]
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                k = q5mul(h, g)
                kk = q5key(k)
                if kk not in seen:
                    seen[kk] = k; new.append(k)
        frontier = new
    return seen


def X3():
    ok = True
    g_cnot = table_action(gCNOT)
    g_tJ = table_action(gkron(gI2, gUJ)); g_tS = table_action(gkron(gI2, gS)); g_tX = table_action(gkron(gI2, gX))
    g_cJ = table_action(gkron(gUJ, gI2)); g_cS = table_action(gkron(gS, gI2))
    G48 = closure([g_cnot, g_tJ])
    G1 = closure([g_cnot, g_tJ, g_tS, g_tX])
    G384 = closure([g_cnot, g_tS, g_tJ])
    Cl = closure([g_cnot, g_cJ, g_tJ, g_cS, g_tS])
    E30 = 12
    stab = {g for g in Cl if g[0][E30] == E30 and g[1][E30] == 1}
    orbE = {(g[0][E30], g[1][E30]) for g in Cl}
    u1 = len(G48) == 48 and all(g[0][E30] == E30 and g[1][E30] == 1 for g in G48)
    u1 &= all(isinstance(sum(g[1][i] for i in range(16) if g[0][i] == i), int) for g in G48)
    u2 = len(G1) == 384 and G1 == G384 and len(Cl) == 11520 and stab == G384 and len(orbE) == 30
    ok &= u1 and u2
    # U3: the 60 stabilizer states
    octa = [(ONE, Z0), (Z0, ONE), (ONE, ONE), (ONE, -ONE), (ONE, IU), (ONE, -IU)]
    prods = [tuple(a[i // 2] * b[i % 2] for i in range(4)) for a in octa for b in octa]
    gens1 = [gCNOT, gkron(gI2, gS), gkron(gI2, gUJ), gkron(gI2, gX)]
    L0 = orbit_rays(gens1, prods)
    u3 = len(L0) == 60 and len(set(ray(p) for p in prods)) == 36
    tabs = [table_of_ray(unray(k)) for k in L0]
    u3 &= Matrix([[sp.Rational(x) for x in t] for t in tabs]).rank() == 16
    ok &= u3
    # U5/V1: algebraic-integer certificate
    x = symbols('x')
    monic_sin = {m: sp.Poly(sp.minimal_polynomial(-1 - sin(2 * pi / m), x), x).LC() == 1 for m in range(1, 25)}
    monic_2cos = {m: sp.Poly(sp.minimal_polynomial(2 * cos(2 * pi / m), x), x).LC() == 1 for m in range(1, 25)}
    monic_cos = {m: sp.Poly(sp.minimal_polynomial(cos(2 * pi / m), x), x).LC() == 1 for m in range(1, 25)}
    u5 = {m for m, v in monic_sin.items() if v} == {1, 2, 4} and all(monic_2cos.values()) and {m for m, v in monic_cos.items() if v} == {1, 2, 4}
    # trace identity tr(J R_z(phi)) = -sin phi (kernel orientation J = cycEquiv) symbolically
    ph = symbols('phi', real=True)
    u5 &= simplify((CYC * rotZ(cos(ph), sin(ph))).trace() + sin(ph)) == 0
    ok &= u5
    # V3: orders 12 and 24 (integer matrices)
    def int_closure(gens):
        ident = eye(3)
        seen = {tuple(ident)}; frontier = [ident]
        while frontier:
            new = []
            for g in frontier:
                for h in gens:
                    k = h * g
                    kk = tuple(k)
                    if kk not in seen:
                        seen.add(kk); new.append(k)
            frontier = new
        return seen
    n12 = len(int_closure([CYC, rotZ(-1, 0)]))
    n24 = len(int_closure([CYC, rotZ(0, 1)]))
    v3 = n12 == 12 and n24 == 24
    ok &= v3
    # V2: the icosahedral group in Q(sqrt5)
    phi_ = Q5(Fr(1, 2), Fr(1, 2))
    u = [phi_ - Q5(1), phi_, Q5(1)]
    u = [Q5(Fr(1, 2)) * c for c in u]
    Ru = [[(Q5(2) * u[i] * u[j]) - (Q5(1) if i == j else Q5(0)) for j in range(3)] for i in range(3)]
    Jq = q5mat([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    Rpi = q5mat([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])
    G60 = q5closure([Jq, Rpi, Ru])
    v2 = len(G60) == 60
    zrots = [A for A in G60.values() if A[0][2] == Q5(0) and A[1][2] == Q5(0) and A[2][0] == Q5(0) and A[2][1] == Q5(0) and A[2][2] == Q5(1)]
    v2 &= len(zrots) == 2
    ok &= v2
    # U6: phi0 from a product by a block-diagonal unitary; unreachable by the 384 group
    phi0 = Matrix([1, 2, 3 * I, -1 + I]) / 4
    cvec = Matrix([1, 2]) / sqrt(5); dvec = Matrix([3 * I, -1 + I]) / sqrt(11)
    U0 = Matrix.hstack(cvec, Matrix([-2, 1]) / sqrt(5))
    U1 = Matrix.hstack(dvec, Matrix([-(1 - I).conjugate() * 0 + (1 + I), 3 * I]) / sqrt(11))
    u6 = simplify(U0.H * U0 - I2) == zeros(2, 2) and simplify(U1.H * U1 - I2) == zeros(2, 2)
    P0 = sp.diag(1, 0); P1 = sp.diag(0, 1)
    Ublk = kron(P0, U0) + kron(P1, U1)
    avec = Matrix([sqrt(5), sqrt(11)]) / 4
    u6 &= simplify(Ublk * kron(avec, Matrix([1, 0])) - phi0) == zeros(4, 1)
    gphi0 = (GQ(1), GQ(2), GQ(0, 3), GQ(-1, 1))
    t0 = table_of_ray(gphi0)
    def is_product_table(t):
        return t[0] == 1 and sum(t[4 * m] ** 2 for m in range(1, 4)) == 1
    reach = sum(1 for g in G384 if is_product_table(apply_signed(g, t0)))
    u6 &= reach == 0
    # control: a product ray is reached (by the identity)
    u6 &= is_product_table(table_of_ray(prods[0]))
    ok &= u6
    # U7: word-length stage Lambda_1
    RL0 = {ray(gvec(gkron(gI2, gRth), unray(k))) for k in L0}
    RiL0 = {ray(gvec(gkron(gI2, gRthInv), unray(k))) for k in L0}
    S1 = L0 | RL0 | RiL0
    L1 = orbit_rays(gens1, [unray(k) for k in S1])
    RL1 = {ray(gvec(gkron(gI2, gRth), unray(k))) for k in L1}
    u7 = len(L1) == 588 and not (RL0 <= L0) and not (RL1 <= L1)
    ok &= u7
    results['X3'] = bool(ok)
    print(f"X3 B12: |<cnot,actT J>| = {len(G48)} {u1}; G1 {len(G1)} = <cnot,actT S,actT J> {G1 == G384}; Clifford {len(Cl)}, "
          f"Stab(E(3,0)) {len(stab)}, orbit {len(orbE)} {u2}; stabilizer states {len(L0)} (tables rank 16) {u3}; "
          f"-1-sin(2pi/m) monic for m in {sorted(m for m, v in monic_sin.items() if v)} {u5}; orders 12/24: {n12}/{n24}; "
          f"icosahedral {len(G60)} with {len(zrots)} z-rotations {v2}; phi0 block-diagonal reach, 384-group reach {reach} {u6}; "
          f"|Lambda_1| = {len(L1)} {u7}: {'PASS' if ok else 'FAIL'}")


# ---------------------------------------------------------------- X4
def X4():
    ok = True
    def prodDet(v): return v[0] * v[3] - v[1] * v[2]
    def prodCross(x_, y_): return x_[0] * y_[3] + y_[0] * x_[3] - x_[1] * y_[2] - y_[1] * x_[2]
    ctl = Matrix([1, 2, 3, 5])
    ok &= prodDet(ctl) == -1 and prodDet(CNOT * ctl) == -7
    t = symbols('t')
    xs = Matrix(symbols('x0:4')); ys = Matrix(symbols('y0:4'))
    ok &= expand(prodDet(xs + t * ys) - (prodDet(xs) + prodCross(xs, ys) * t + prodDet(ys) * t ** 2)) == 0
    a, b, c = symbols('a b c')
    sol = sp.solve([a + b * 1 + c * 1, a + b * 2 + c * 4, a + b * 3 + c * 9], [a, b, c])
    ok &= sol == {a: 0, b: 0, c: 0}
    w = Matrix([1, 2, 3, 5])
    fs = [lambda v: prodDet(v), lambda v: prodDet(CNOT * v)]
    nonroot = [n for n in range(5) if all(f(n * w) != 0 for f in fs)]
    ok &= len(nonroot) >= 1
    results['X4'] = bool(ok)
    print(f"X4 B13 controls: prodDet -1/-7, polarisation identity, three-root lemma instance, common non-root at n in {nonroot}: "
          f"{'PASS' if ok else 'FAIL'}")


if __name__ == '__main__':
    for fn in (X1, X2, X3, X4):
        fn(); sys.stdout.flush()
    fails = [k for k, v in results.items() if not v]
    n = sum(1 for v in results.values() if v)
    print(f"{n}/{len(results)} PASS")
    print("VERDICT INDEP-B3-FIXED" if not fails else f"VERDICT INDEP-B3-OPEN {fails}")
