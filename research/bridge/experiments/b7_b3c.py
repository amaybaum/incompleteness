#!/usr/bin/env python3
"""b7_b3c.py -- node B7 of research/bridge: Conjecture B3.C, the open cases.

DECISION RULE (fixed 2026-10-10T22:26:50Z, from `date -u` immediately before writing; before run 1).

Setting (NOTES-B7 §1). H is a compact group of unitary and antiunitary conjugations of the pair with
cnot in H and abelian identity component T. By claim (D) [A] (archive pt/Z/RESULT.md §0 (D), §1.0),
H leaves an exotic invariant cone iff some pure state lies outside R(H) = H.P (P = pure products).
The open cases are: T with four distinct eigenlines of which exactly 1, 2 or 3 are products, and
2-tori with a 2-dimensional eigenspace. All arithmetic is exact (Fractions, Gaussian rationals;
sympy for one symbolic identity). Work is in the CZ frame: the local Hadamard on the target maps
CNOT to CZ = diag(1, 1, 1, -1) (check X0); products and moduli are invariant under local unitaries.

Checks (each PASS/FAIL):
  X0  (I (x) Had) CNOT (I (x) Had) = CZ exactly.
  X1  For each four-eigenline instance (I1: 1 product, CZ fixing every line; I2: 2 products, CZ
      fixing every line; I3: 0 products, CZ swapping a pair; I4: 1 product, CZ swapping the
      product line with a non-product line; controls I5 grid, I6 non-grid product basis, I7 Bell
      basis): orthonormal, CZ permutes the lines up to a factor, product count as designed, and
      the S4-orbit of m(eps, r) = ((1 - eps) at one vertex, eps * r on the others in every order)
      avoids mu(P) by the certificate of NOTES-B7 Lemma 2: at a non-product vertex k,
      eps < |det C_k|^2; at a product vertex k = a(x)b, with w_k = a'(x)b' and omega_j = <phi_j|w_k>,
      sqrt(q_max) - sqrt(q_a) - sqrt(q_b) > sqrt(eps) for q_i = |omega_tau(i)|^2 r_i (certified with
      exact rational bounds on the square roots). (eta, eta', eps) is taken from the fixed list
      PARAMS in order; r = (1 - eta - eta', eta, eta'); the first triple certifying all 24 (k, tau)
      is reported; an instance passes iff some triple certifies it.
  X2  Countercontrol (non-vacuity of the certificate): at every product vertex of every instance,
      an explicit product state near the vertex has |<w_k|p>|^2 <= eps_p^2 and FAILS the
      certificate for every tau.
  X3  Exactly three product lines never occur: for every orthonormal triple of product vectors
      drawn from the finite family FAMILY (x) FAMILY, the orthocomplement is a product; the family
      contains at least one such triple.
  X4  Degenerate 2-torus, E not entirely product (D1): E = span{f1, f2} contains exactly two
      product directions (binary quadratic with nonzero discriminant, not identically zero); CZ is
      in T = {diag(a, a, b, c)}; the state sqrt(1-eps) f1 + sqrt(eps) f3 with eps = 1/10 is outside
      T.P because eps < |det C(f1)|^2.
  X5  Degenerate 2-torus, E entirely product (D2): for every product (x|0>+y|1>)(x)v the invariant
      rho = |c_10|^2/(|c_10|^2+|c_11|^2) equals g(u) = |u_0|^2/|u|^2 (symbolic identity, sympy);
      the target state has |u|^2 = 1/2, rho = 1/2, g(u0) = 9/25, and 1/2 is not in {9/25, 16/25}.
  X6  Consistency of the tangent moment image: for every product vertex, exact points u of
      L_k = phi_k-perp intersect w_k-perp satisfy Heron(|omega_j|^2 m_j(u)) >= 0.

VERDICT B7-B3C-EXACT iff X0-X6 all PASS; otherwise VERDICT B7-FAILED with the failing ids. A failure
of X1 on an open-case instance (I1, I2, I4) is recorded as a gap in the written argument, not
repaired by changing PARAMS after the run.
"""
from fractions import Fraction as Fr
from itertools import permutations, combinations, product
from math import isqrt
import sys

import sympy as sp

PASS, FAIL = [], []


def check(cid, ok, msg):
    print(f"{cid:5s} {'PASS' if ok else 'FAIL'}  {msg}")
    (PASS if ok else FAIL).append(cid)


class G:
    """Gaussian rational a + b i with Fraction parts."""
    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re, self.im = Fr(re), Fr(im)

    def __add__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        return G(o) - self

    def __neg__(self):
        return G(-self.re, -self.im)

    def __mul__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def conj(self):
        return G(self.re, -self.im)

    def abs2(self):
        return self.re * self.re + self.im * self.im

    def iszero(self):
        return self.re == 0 and self.im == 0

    def __eq__(self, o):
        o = o if isinstance(o, G) else G(o)
        return self.re == o.re and self.im == o.im

    def __repr__(self):
        return f"({self.re}{'+' if self.im >= 0 else '-'}{abs(self.im)}i)"


def V(*xs):
    return [x if isinstance(x, G) else G(x) for x in xs]


def ip(u, v):
    s = G(0)
    for a, b in zip(u, v):
        s = s + a.conj() * b
    return s


def n2(u):
    return ip(u, u).re


def kron(a, b):
    return [a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]]


def det2(phi):
    return phi[0] * phi[3] - phi[1] * phi[2]


def is_prod(phi):
    return det2(phi).iszero()


def perp2(a):
    return [-(a[1].conj()), a[0].conj()]


def factor(phi):
    """phi = alpha (x) beta up to a scalar (phi a product)."""
    rows = [[phi[0], phi[1]], [phi[2], phi[3]]]
    cols = [[phi[0], phi[2]], [phi[1], phi[3]]]
    beta = next(r for r in rows if not (r[0].iszero() and r[1].iszero()))
    alpha = next(c for c in cols if not (c[0].iszero() and c[1].iszero()))
    return alpha, beta


def mod2(phi_j, w):
    """|<phi_j|w>|^2 / (|phi_j|^2 |w|^2), exact."""
    return ip(phi_j, w).abs2() / (n2(phi_j) * n2(w))


def sqrt_lo_hi(q, S=10 ** 15):
    q = Fr(q)
    assert q >= 0
    n, d = q.numerator, q.denominator
    m = n * d * S * S
    r = isqrt(m)
    lo = Fr(r, d * S)
    hi = lo if r * r == m else Fr(r + 1, d * S)
    return lo, hi


def heron(q1, q2, q3):
    return 2 * (q1 * q2 + q2 * q3 + q3 * q1) - (q1 * q1 + q2 * q2 + q3 * q3)


CZ = [G(1), G(1), G(1), G(-1)]


def cz(u):
    return [c * x for c, x in zip(CZ, u)]


def parallel(u, v):
    """u = lambda v for some lambda != 0 (exact)."""
    i = next(k for k in range(4) if not v[k].iszero())
    if u[i].iszero():
        return False
    # lambda = u_i / v_i ; compare u_k v_i = u_i v_k for all k
    return all((u[k] * v[i] - u[i] * v[k]).iszero() for k in range(4))


PARAMS = [(Fr(1, 400), Fr(1, 100), Fr(1, 10 ** 6)),
          (Fr(1, 900), Fr(1, 200), Fr(1, 10 ** 8)),
          (Fr(1, 2500), Fr(1, 600), Fr(1, 10 ** 10))]


def vertex_data(B):
    data = []
    for k, phi in enumerate(B):
        if is_prod(phi):
            a, b = factor(phi)
            w = kron(perp2(a), perp2(b))
            assert ip(w, phi).iszero()
            om = {j: mod2(B[j], w) for j in range(4) if j != k}
            assert sum(om.values()) == 1
            data.append(("prod", a, b, w, om))
        else:
            data.append(("ent", det2(phi).abs2() / n2(phi) ** 2))
    return data


def cert_pair(data, k, tau, r, eps):
    d = data[k]
    if d[0] == "ent":
        return eps < d[1]
    om = d[4]
    qs = sorted([om[tau[i]] * r[i] for i in range(3)], reverse=True)
    lo_max = sqrt_lo_hi(qs[0])[0]
    hi_a = sqrt_lo_hi(qs[1])[1]
    hi_b = sqrt_lo_hi(qs[2])[1]
    hi_e = sqrt_lo_hi(eps)[1]
    return lo_max - hi_a - hi_b - hi_e > 0


def certify(B):
    data = vertex_data(B)
    for (eta, eta2, eps) in PARAMS:
        r = (1 - eta - eta2, eta, eta2)
        ok = True
        for k in range(4):
            others = [j for j in range(4) if j != k]
            for tau in permutations(others):
                if not cert_pair(data, k, tau, r, eps):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return (eta, eta2, eps), data
    return None, data


def orthonormal_up_to_norm(B):
    return all(ip(B[i], B[j]).iszero() for i in range(4) for j in range(4) if i < j)


def cz_permutes(B):
    for u in B:
        cu = cz(u)
        if not any(parallel(cu, v) for v in B):
            return False
    return True


# ---------------- X0 ----------------
s2 = sp.sqrt(2)
Had = sp.Matrix([[1, 1], [1, -1]]) / s2
I2 = sp.eye(2)
CNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
IH = sp.kronecker_product(I2, Had)
lhs = sp.simplify(IH * CNOT * IH)
check("X0", lhs == sp.diag(1, 1, 1, -1), "(I(x)Had) CNOT (I(x)Had) = diag(1,1,1,-1) = CZ")

# ---------------- instances ----------------
# I4: phi_+ = (a0, a1) (x) (1, 5/3) with a0 = 2+2i, a1 = 1+4i (|a0|^2 = 8, |a1|^2 = 17);
# the V+ and V- weights of phi_+ are equal (425/9 each), so CZ phi_+ is orthogonal to phi_+.
a0, a1 = G(2, 2), G(1, 4)
phiP = kron([a0, a1], [G(1), G(Fr(5, 3))])
phiM = cz(phiP)
f = [phiP[0], phiP[1], phiP[2], G(0)]
g1 = V(5, -3, 0, 0)                        # orthogonal to f in V+ (a product)
# g2 orthogonal to f and g1 in V+: g2 = (3, 5, y, 0) with <g2|f> = 0
# <g2|f> = 3 a0 + 5 (5 a0 / 3) + conj(y) a1 = (34/3) a0 + conj(y) a1 = 0
# conj(y) = -(34/3) a0 / a1 ; a0 / a1 = a0 conj(a1) / 17
ratio = a0 * a1.conj() * G(Fr(1, 17))
ybar = G(Fr(-34, 3)) * ratio
g2 = [G(3), G(5), ybar.conj(), G(0)]
assert ip(g2, f).iszero() and ip(g1, f).iszero() and ip(g1, g2).iszero()
# rotate within span{g1, g2} (norms differ: rescale g1 to |g2|^2 by a rational factor when possible;
# use the unnormalized rotation h1 = |g2|^2 g1 + |g1|^2 ... kept exact by orthogonality)
n1, n2g = n2(g1), n2(g2)
h1 = [G(n2g) * x + G(n1) * y for x, y in zip(g1, g2)]    # orthogonal to h2 below
h2 = [G(n2g) * x - G(n2g) * y for x, y in zip(g1, g2)]
# <h1|h2> = n2g*n2g*n1 - n1*n2g*n2g = 0
assert ip(h1, h2).iszero()

INST = {
    "I1": ([V(1, 2, 2, 0), V(2, 1, -2, 0), V(2, -2, 1, 0), V(0, 0, 0, 1)], 1, "type I, open case"),
    "I2": ([V(1, 0, 0, 0), V(0, 3, 4, 0), V(0, -4, 3, 0), V(0, 0, 0, 1)], 2, "type I, open case"),
    "I3": ([V(1, 2, 2, 3), V(1, 2, 2, -3), V(2, 1, -2, 0), V(2, -2, 1, 0)], 0, "type II, (P3)"),
    "I4": ([phiP, phiM, h1, h2], 1, "type II, open case: CZ swaps the product line"),
    "I5": ([V(1, 0, 0, 0), V(0, 1, 0, 0), V(0, 0, 1, 0), V(0, 0, 0, 1)], 4, "control, grid"),
    "I6": ([V(1, 0, 0, 0), V(0, 1, 0, 0), V(0, 0, 1, 1), V(0, 0, 1, -1)], 4, "control, non-grid"),
    "I7": ([V(1, 0, 0, 1), V(1, 0, 0, -1), V(0, 1, 1, 0), V(0, 1, -1, 0)], 0, "control, Bell"),
}

DATA = {}
for name, (B, nprod, note) in INST.items():
    on = orthonormal_up_to_norm(B)
    czp = cz_permutes(B)
    cnt = sum(1 for u in B if is_prod(u))
    par, data = certify(B)
    DATA[name] = (B, data)
    ok = on and czp and cnt == nprod and par is not None
    pstr = "none" if par is None else f"eta={par[0]}, eta'={par[1]}, eps={par[2]}"
    check(f"X1{name}", ok, f"{note}: orthogonal={on}, CZ permutes lines={czp}, products={cnt} "
          f"(designed {nprod}), certified by {pstr}")
    if name == "I4":
        prodlines = [i for i, u in enumerate(B) if is_prod(u)]
        print(f"      I4: product line(s) {prodlines}; CZ maps line 0 to line 1 "
              f"(parallel={parallel(cz(B[0]), B[1])}); line 1 product={is_prod(B[1])}")

# ---------------- X2 countercontrol ----------------
t = Fr(1, 10)
cc, ss = (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)
x2ok, x2n = True, 0
for name, (B, data) in DATA.items():
    for k in range(4):
        if data[k][0] != "prod":
            continue
        _, a, b, w, om = data[k]
        pa = [G(cc) * a[0] + G(ss) * perp2(a)[0], G(cc) * a[1] + G(ss) * perp2(a)[1]]
        pb = [G(cc) * b[0] + G(ss) * perp2(b)[0], G(cc) * b[1] + G(ss) * perp2(b)[1]]
        p = kron(pa, pb)
        m = [mod2(B[j], p) for j in range(4)]
        assert sum(m) == 1
        eps_p = 1 - m[k]
        wp = mod2(w, p)
        if not wp <= eps_p * eps_p:
            x2ok = False
        others = [j for j in range(4) if j != k]
        for tau in permutations(others):
            r = tuple(m[tau[i]] / eps_p for i in range(3))
            if cert_pair(data, k, tau, r, eps_p):
                x2ok = False
        x2n += 1
check("X2", x2ok and x2n > 0, f"{x2n} product vertices: an explicit product near each vertex has "
      f"|<w|p>|^2 <= eps^2 and fails the certificate for all 6 orders")

# ---------------- X3 exactly three product lines never occur ----------------
FAMILY = [V(1, 0), V(0, 1), V(1, 1), V(1, -1), V(3, 4), V(4, -3), [G(1), G(0, 1)], [G(1), G(0, -1)]]
prods = []
for a, b in product(FAMILY, FAMILY):
    p = kron(a, b)
    if not any(parallel(p, q) for q in prods):
        prods.append(p)


def null3(rows):
    """exact z with <r_i|z> = 0 for three rows (via signed 3x3 minors of conj(rows))."""
    A = [[x.conj() for x in r] for r in rows]

    def det3(M):
        return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
                - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
                + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    z = []
    for l in range(4):
        M = [[A[i][c] for c in range(4) if c != l] for i in range(3)]
        z.append(det3(M) * G((-1) ** l))
    return z


ntrip, x3ok = 0, True
for tri in combinations(prods, 3):
    if all(ip(tri[i], tri[j]).iszero() for i in range(3) for j in range(3) if i < j):
        z = null3(tri)
        assert all(ip(u, z).iszero() for u in tri) and n2(z) > 0
        ntrip += 1
        if not is_prod(z):
            x3ok = False
check("X3", x3ok and ntrip > 0, f"{len(prods)} product directions, {ntrip} orthogonal triples; "
      f"every orthocomplement is a product")

# ---------------- X4 degenerate 2-torus, E not entirely product ----------------
f1, f2, f3, f4 = V(1, 2, 2, 0), V(2, 1, -2, 0), V(2, -2, 1, 0), V(0, 0, 0, 1)
# det(x f1 + y f2) = A x^2 + Bc x y + C y^2 ; read off from three evaluations
d_x = det2(f1)
d_y = det2(f2)
d_xy = det2([u + v for u, v in zip(f1, f2)])
A_, C_ = d_x, d_y
Bc = d_xy - d_x - d_y
disc = Bc * Bc - G(4) * A_ * C_
notzero = not (A_.iszero() and Bc.iszero() and C_.iszero())
cz_in_T = all(parallel(cz(u), u) for u in (f1, f2, f3, f4)) and \
    cz(f1) == f1 and cz(f2) == f2 and cz(f3) == f3 and cz(f4) == [-x for x in f4]
detf1 = det2(f1).abs2() / n2(f1) ** 2
eps4 = Fr(1, 10)
check("X4", notzero and not disc.iszero() and cz_in_T and eps4 < detf1,
      f"det on E = {A_} x^2 + {Bc} xy + {C_} y^2, discriminant {disc} (two product directions); "
      f"CZ = diag(1,1,1,-1) in T; eps = 1/10 < |det C(f1)|^2 = {detf1}")

# ---------------- X5 degenerate 2-torus, E entirely product ----------------
xr, xi, yr, yi, v0r, v0i, v1r, v1i = sp.symbols("xr xi yr yi v0r v0i v1r v1i", real=True)
x_ = xr + sp.I * xi
y_ = yr + sp.I * yi
v0 = v0r + sp.I * v0i
v1 = v1r + sp.I * v1i


def ab2(z):
    return sp.expand(z * sp.conjugate(z))


u0c, u1c = x_ * v0, x_ * v1
c10, c11 = y_ * v0, y_ * v1
ident = sp.expand(ab2(c10) * (ab2(u0c) + ab2(u1c)) - ab2(u0c) * (ab2(c10) + ab2(c11)))
g_target = Fr(9, 25)
rho0 = Fr(1, 2)
check("X5", ident == 0 and rho0 not in (g_target, 1 - g_target),
      "rho = g(u) identically on products (x|0>+y|1>)(x)v; target |u|^2 = 1/2, rho = 1/2, "
      "g(u0) = 9/25 for u0 = (3,4)/5; 1/2 not in {9/25, 16/25}")

# ---------------- X6 tangent moment image consistency ----------------
x6ok, x6n = True, 0
coeffs = [(G(1), G(0)), (G(0), G(1)), (G(1), G(1)), (G(1), G(-2)), (G(3), G(0, 4)), (G(2, 1), G(-1, 3))]
for name, (B, data) in DATA.items():
    for k in range(4):
        if data[k][0] != "prod":
            continue
        _, a, b, w, om = data[k]
        e1 = kron(a, perp2(b))
        e2 = kron(perp2(a), b)
        for (s1, s2_) in coeffs:
            u = [s1 * p + s2_ * q for p, q in zip(e1, e2)]
            assert ip(w, u).iszero() and ip(B[k], u).iszero()
            m = {j: mod2(B[j], u) for j in range(4) if j != k}
            assert sum(m.values()) == 1
            qs = [om[j] * m[j] for j in m]
            if heron(*qs) < 0:
                x6ok = False
            x6n += 1
check("X6", x6ok and x6n > 0, f"{x6n} exact tangent points: Heron(|omega_j|^2 m_j) >= 0 at each")

print()
print(f"PASS {len(PASS)}  FAIL {len(FAIL)}")
if FAIL:
    print("VERDICT B7-FAILED " + " ".join(FAIL))
else:
    print("VERDICT B7-B3C-EXACT")
sys.exit(0)
