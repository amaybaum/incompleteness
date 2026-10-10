#!/usr/bin/env python3
"""b7b_generic.py -- node B7 of research/bridge, robustness check: the moment-orbit certificate of
NOTES-B7 Lemma 2 on generated exact bases (not hand-picked).

DECISION RULE (fixed 2026-10-10T22:58:57Z, from `date -u` immediately before writing; before run 1).

Bases of C^2 (x) C^2 with Gaussian-rational entries, exactly orthonormal, are generated
deterministically from Cayley transforms U = (I - A)(I + A)^-1 of skew-Hermitian A with small
Gaussian-integer entries (A taken from a fixed list, no randomness):
  G0[k] (k = 0..3): columns of a 4x4 Cayley unitary (generic: no product line expected);
  G1[k] (k = 0..3): W (1 (+) V3) e_j with W = A2 (x) B2 (2x2 Cayley unitaries) and V3 a 3x3 Cayley
          unitary: one product line W e_1 = a (x) b;
  G2[k] (k = 0..3): {a (x) b, a' (x) c, x a (x) b' + y a' (x) c', -conj(y) a (x) b' + conj(x) a' (x) c'}
          with a' = a-perp, b' = b-perp, c' = c-perp and (x, y) the first column of a 2x2 Cayley
          unitary: two product lines.
Checks:
  Z1  every basis is exactly orthonormal and has the designed number of product lines (det of the
      2x2 coefficient matrix);
  Z2  every basis is certified by Lemma 2 (same certificate as b7_b3c.py X1) with some triple of
      the fixed list PARAMS2 (first success reported);
  Z3  countercontrol at every product vertex of every basis: an explicit product near the vertex
      has |<w|p>|^2 <= eps^2 and fails the certificate in all six orders.
VERDICT B7B-GENERIC-EXACT iff Z1-Z3 all PASS. A Z2 failure would mean only that the fixed parameter
list missed a valid r for that basis (Lemma 1 guarantees one exists); it is reported, not repaired
after the run.
"""
from fractions import Fraction as Fr
from itertools import permutations
from math import isqrt
import sys

PASS, FAIL = [], []


def check(cid, ok, msg):
    print(f"{cid:4s} {'PASS' if ok else 'FAIL'}  {msg}")
    (PASS if ok else FAIL).append(cid)


class G:
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

    def inv(self):
        n = self.abs2()
        return G(self.re / n, -self.im / n)

    def iszero(self):
        return self.re == 0 and self.im == 0


def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum((A[i][k] * B[k][j] for k in range(m)), G(0)) for j in range(p)] for i in range(n)]


def inverse(M):
    n = len(M)
    A = [row[:] + [G(1) if i == j else G(0) for j in range(n)] for i, row in enumerate(M)]
    for c in range(n):
        piv = next(r for r in range(c, n) if not A[r][c].iszero())
        A[c], A[piv] = A[piv], A[c]
        iv = A[c][c].inv()
        A[c] = [x * iv for x in A[c]]
        for r in range(n):
            if r != c and not A[r][c].iszero():
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [row[n:] for row in A]


def cayley(Aentries):
    """U = (I - A)(I + A)^-1 for skew-Hermitian A built from upper-triangle Gaussian integers."""
    n = len(Aentries)
    A = [[G(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i < j:
                A[i][j] = Aentries[i][j]
                A[j][i] = -(Aentries[i][j].conj())
            elif i == j:
                A[i][i] = G(0, Aentries[i][i].im)
    I_ = [[G(1) if i == j else G(0) for j in range(n)] for i in range(n)]
    ImA = [[I_[i][j] - A[i][j] for j in range(n)] for i in range(n)]
    IpA = [[I_[i][j] + A[i][j] for j in range(n)] for i in range(n)]
    return matmul(ImA, inverse(IpA))


def col(U, j):
    return [U[i][j] for i in range(len(U))]


def ip(u, v):
    return sum((a.conj() * b for a, b in zip(u, v)), G(0))


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
    rows = [[phi[0], phi[1]], [phi[2], phi[3]]]
    cols = [[phi[0], phi[2]], [phi[1], phi[3]]]
    beta = next(r for r in rows if not (r[0].iszero() and r[1].iszero()))
    alpha = next(c for c in cols if not (c[0].iszero() and c[1].iszero()))
    return alpha, beta


def mod2(u, w):
    return ip(u, w).abs2() / (n2(u) * n2(w))


def sqrt_lo_hi(q, S=10 ** 15):
    q = Fr(q)
    n, d = q.numerator, q.denominator
    m = n * d * S * S
    r = isqrt(m)
    lo = Fr(r, d * S)
    return lo, (lo if r * r == m else Fr(r + 1, d * S))


PARAMS2 = [(Fr(1, 400), Fr(1, 100), Fr(1, 10 ** 6)), (Fr(1, 900), Fr(1, 200), Fr(1, 10 ** 8)),
           (Fr(1, 2500), Fr(1, 600), Fr(1, 10 ** 10)), (Fr(1, 1000), Fr(7, 1000), Fr(1, 10 ** 8)),
           (Fr(1, 3000), Fr(1, 1100), Fr(1, 10 ** 10))]


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
    return sqrt_lo_hi(qs[0])[0] - sqrt_lo_hi(qs[1])[1] - sqrt_lo_hi(qs[2])[1] - sqrt_lo_hi(eps)[1] > 0


def certify(B):
    data = vertex_data(B)
    for (eta, eta2, eps) in PARAMS2:
        r = (1 - eta - eta2, eta, eta2)
        if all(cert_pair(data, k, tau, r, eps) for k in range(4)
               for tau in permutations([j for j in range(4) if j != k])):
            return (eta, eta2, eps), data
    return None, data


# deterministic generator data (no randomness)
A2LIST = [[[G(0, 1), G(1, 2)], [None, G(0, -1)]], [[G(0, 2), G(-1, 1)], [None, G(0, 1)]],
          [[G(0, 0), G(2, -1)], [None, G(0, 3)]], [[G(0, 1), G(3, 1)], [None, G(0, 2)]],
          [[G(0, -2), G(1, 3)], [None, G(0, 1)]], [[G(0, 3), G(-2, 1)], [None, G(0, 0)]]]
A3LIST = [[[G(0, 1), G(1, 1), G(2, -1)], [None, G(0, -1), G(1, 2)], [None, None, G(0, 2)]],
          [[G(0, 2), G(-1, 1), G(1, 0)], [None, G(0, 1), G(2, 1)], [None, None, G(0, -1)]],
          [[G(0, 0), G(1, -2), G(1, 1)], [None, G(0, 3), G(-1, 1)], [None, None, G(0, 1)]],
          [[G(0, 1), G(2, 2), G(-1, 1)], [None, G(0, 2), G(1, -1)], [None, None, G(0, -2)]]]
A4LIST = [[[G(0, 1), G(1, 1), G(2, -1), G(0, 1)], [None, G(0, -1), G(1, 2), G(1, 0)],
           [None, None, G(0, 2), G(-1, 1)], [None, None, None, G(0, 1)]],
          [[G(0, 2), G(-1, 1), G(1, 0), G(2, 1)], [None, G(0, 1), G(2, 1), G(0, -1)],
           [None, None, G(0, -1), G(1, 1)], [None, None, None, G(0, 3)]],
          [[G(0, 0), G(1, -2), G(1, 1), G(-1, 2)], [None, G(0, 3), G(-1, 1), G(2, 0)],
           [None, None, G(0, 1), G(1, -1)], [None, None, None, G(0, -2)]],
          [[G(0, 1), G(2, 2), G(-1, 1), G(1, 3)], [None, G(0, 2), G(1, -1), G(0, 1)],
           [None, None, G(0, -2), G(2, -1)], [None, None, None, G(0, 1)]]]


def fill(Al):
    n = len(Al)
    return [[Al[i][j] if (j >= i and Al[i][j] is not None) else G(0) for j in range(n)] for i in range(n)]


U2 = [cayley(fill(A)) for A in A2LIST]
U3 = [cayley(fill(A)) for A in A3LIST]
U4 = [cayley(fill(A)) for A in A4LIST]

BASES = []
for k in range(4):
    BASES.append((f"G0[{k}]", [col(U4[k], j) for j in range(4)], 0))
for k in range(4):
    A2, B2, V3 = U2[k], U2[(k + 1) % 6], U3[k]
    W = [[A2[i // 2][m // 2] * B2[i % 2][m % 2] for m in range(4)] for i in range(4)]
    V = [[G(1) if (i == 0 and j == 0) else (G(0) if (i == 0 or j == 0) else V3[i - 1][j - 1])
          for j in range(4)] for i in range(4)]
    WV = matmul(W, V)
    BASES.append((f"G1[{k}]", [col(WV, j) for j in range(4)], 1))
for k in range(4):
    a, b, c = col(U2[k], 0), col(U2[(k + 2) % 6], 0), col(U2[(k + 3) % 6], 0)
    xy = col(U2[(k + 4) % 6], 0)
    x_, y_ = xy[0], xy[1]
    ap, bp, cp = perp2(a), perp2(b), perp2(c)
    v3 = [x_ * s + y_ * t for s, t in zip(kron(a, bp), kron(ap, cp))]
    v4 = [-(y_.conj()) * s + x_.conj() * t for s, t in zip(kron(a, bp), kron(ap, cp))]
    BASES.append((f"G2[{k}]", [kron(a, b), kron(ap, c), v3, v4], 2))

z1 = z2 = z3 = True
t = Fr(1, 10)
cc, ss = (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)
nvert = 0
for name, B, nprod in BASES:
    orth = all(ip(B[i], B[j]).iszero() for i in range(4) for j in range(4) if i < j)
    unit = all(n2(u) == 1 for u in B)
    cnt = sum(1 for u in B if is_prod(u))
    if not (orth and unit and cnt == nprod):
        z1 = False
    par, data = certify(B)
    if par is None:
        z2 = False
    pstr = "none" if par is None else f"eta={par[0]}, eta'={par[1]}, eps={par[2]}"
    print(f"     {name}: orthonormal={orth and unit}, product lines={cnt} (designed {nprod}), certified by {pstr}")
    for k in range(4):
        if data[k][0] != "prod":
            continue
        _, a, b, w, om = data[k]
        pa = [G(cc) * a[0] + G(ss) * perp2(a)[0], G(cc) * a[1] + G(ss) * perp2(a)[1]]
        pb = [G(cc) * b[0] + G(ss) * perp2(b)[0], G(cc) * b[1] + G(ss) * perp2(b)[1]]
        p = kron(pa, pb)
        m = [mod2(B[j], p) for j in range(4)]
        eps_p = 1 - m[k]
        if not mod2(w, p) <= eps_p * eps_p:
            z3 = False
        for tau in permutations([j for j in range(4) if j != k]):
            r = tuple(m[tau[i]] / eps_p for i in range(3))
            if cert_pair(data, k, tau, r, eps_p):
                z3 = False
        nvert += 1
check("Z1", z1, f"{len(BASES)} generated bases exactly orthonormal with the designed product-line counts")
check("Z2", z2, "every generated basis certified by Lemma 2 with a triple of PARAMS2")
check("Z3", z3 and nvert > 0, f"countercontrol at {nvert} product vertices: explicit nearby products fail")
print()
print(f"PASS {len(PASS)}  FAIL {len(FAIL)}")
print("VERDICT B7B-GENERIC-EXACT" if not FAIL else "VERDICT B7B-FAILED " + " ".join(FAIL))
sys.exit(0)
