#!/usr/bin/env python3
"""Exact channel controls. Decision rule: PREREGISTRATION.md, commit 78aa5b25.

No imported thread code, external input, floating point, or third-party package.
Finite checks are [X]; universal steps in ARGUMENT.md are separately [W].
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import permutations, product
import sys


@dataclass(frozen=True)
class G:
    r: F = F(0)
    i: F = F(0)

    @staticmethod
    def of(x):
        return x if isinstance(x, G) else G(F(x))

    def __add__(self, x):
        x = G.of(x)
        return G(self.r + x.r, self.i + x.i)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.r, -self.i)

    def __sub__(self, x):
        return self + -G.of(x)

    def __rsub__(self, x):
        return G.of(x) + -self

    def __mul__(self, x):
        x = G.of(x)
        return G(self.r*x.r - self.i*x.i, self.r*x.i + self.i*x.r)

    __rmul__ = __mul__

    def conj(self):
        return G(self.r, -self.i)


I = G(F(0), F(1))


def mat(rows):
    return tuple(tuple(G.of(x) for x in row) for row in rows)


def eye(n):
    return mat([[int(i == j) for j in range(n)] for i in range(n)])


def unit(n, i, j):
    return mat([[int(a == i and b == j) for b in range(n)] for a in range(n)])


def add(a, b):
    return tuple(tuple(x+y for x, y in zip(r, s)) for r, s in zip(a, b))


def scale(x, a):
    return tuple(tuple(x*v for v in r) for r in a)


def mul(a, b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))), G())
                       for j in range(len(b[0]))) for i in range(len(a)))


def adj(a):
    return tuple(tuple(a[j][i].conj() for j in range(len(a))) for i in range(len(a[0])))


def kron(a, b):
    return tuple(tuple(a[i][j]*b[k][l] for j in range(len(a[0])) for l in range(len(b[0])))
                 for i in range(len(a)) for k in range(len(b)))


def ad(u, x):
    return mul(mul(u, x), adj(u))


def tr(a):
    return sum((a[i][i] for i in range(len(a))), G())


def msum(xs, n):
    z = scale(0, eye(n))
    for x in xs:
        z = add(z, x)
    return z


def pair(a, b):
    z = tr(mul(a, b))
    assert z.i == 0
    return z.r


X = mat([[0, 1], [1, 0]])
Y = mat([[0, -I], [I, 0]])
Z = mat([[1, 0], [0, -1]])
P = (eye(2), X, Y, Z)
Hraw = mat([[1, 1], [1, -1]])
S = mat([[1, 0], [0, I]])
D = mat([[1, 0], [0, G(F(3, 5), F(4, 5))]])
J = scale(F(1, 2), add(eye(2), scale(-I, msum([X, Y, Z], 2))))
hh = kron(eye(2), kron(Hraw, Hraw))
tof = mat([[int(i == (j ^ 4 if j % 4 == 3 else j)) for j in range(8)] for i in range(8)])
U = scale(F(1, 4), mul(mul(mul(mul(hh, tof), kron(S, eye(4))), tof), hh))
raw = tuple(mat([[U[4*a+j][4*b] for b in range(2)] for a in range(2)]) for j in range(4))
branches = (raw[0],) + tuple(mul(Z, raw[j]) for j in range(1, 4))


def stopped(k, rho, spectator=False, correct=True):
    bs = branches if correct else raw
    if spectator:
        bs = tuple(kron(eye(2), b) for b in bs)
    if k == 0:
        return rho
    success = ad(bs[0], rho)
    failed = msum([ad(b, rho) for b in bs[1:]], len(rho))
    return add(success, stopped(k-1, failed, spectator, correct))


def formula(k, rho, spectator=False):
    p = F(3, 8)**k
    u = kron(eye(2), D) if spectator else D
    return add(scale(1-p, ad(u, rho)), scale(p, rho))


checks = []


def check(name, ok, detail=""):
    checks.append((name, bool(ok)))
    print(f"{name}: {'PASS' if ok else 'FAIL'}" + (f" ({detail})" if detail else ""))


check("U", mul(adj(U), U) == eye(8))
reset = tuple(unit(4, 0, j) for j in range(4))
check("RESET", msum([ad(r, scale(F(1, 4), eye(4))) for r in reset], 4) == unit(4, 0, 0))
check("BRANCH", raw[0] == scale(G(F(3, 4), F(1, 4)), D)
      and mul(adj(raw[0]), raw[0]) == scale(F(5, 8), eye(2))
      and all(mul(adj(b), b) == scale(F(1, 8), eye(2))
              and b == scale(b[0][0], eye(2)) for b in branches[1:]))
check("TP", msum([mul(adj(b), b) for b in branches], 2) == eye(2))
check("TOKEN", all(stopped(k, unit(2, a, b)) == formula(k, unit(2, a, b))
                   for k in range(7) for a, b in product(range(2), repeat=2)), "28 matrix-unit cases")
check("PAIR", all(stopped(k, unit(4, a, b), True) == formula(k, unit(4, a, b), True)
                  for k in range(7) for a, b in product(range(4), repeat=2)), "112 matrix-unit cases")
dict_ok = True
j_ok = mul(adj(J), J) == eye(2)
for k, m, n in product(range(7), range(4), range(4)):
    p = F(3, 8)**k
    a, b = p + (1-p)*F(3, 5), (1-p)*F(4, 5)
    target = (P[0], add(scale(a, X), scale(b, Y)), add(scale(-b, X), scale(a, Y)), Z)[n]
    dict_ok &= stopped(k, scale(F(1, 4), kron(P[m], P[n])), True) == scale(F(1, 4), kron(P[m], target))
for m, n in product(range(4), repeat=2):
    target = P[(0, 2, 3, 1)[n]]
    j_ok &= ad(kron(eye(2), J), scale(F(1, 4), kron(P[m], P[n]))) == scale(F(1, 4), kron(P[m], target))
check("DICT", dict_ok, "112 Pauli table cases")
check("J", j_ok, "16 Pauli table cases")

# Independent defect-cone witnesses. Each dual test is an explicit rank-one PSD matrix.
es = []
psis = []
for s, t in product((-1, 1), repeat=2):
    e = scale(F(1, 16), msum([eye(4), scale(s, kron(X, Z)),
                            scale(t, kron(Y, Y)), scale(-s*t, kron(Z, X))], 4))
    es.append(e)
    proj = scale(F(1, 2), add(eye(4), scale(-8, e)))
    psi = tuple(2*proj[j][0] for j in range(4))
    assert sum((z.conj()*z for z in psi), G()) == G.of(1)
    psis.append(psi)


def proj(v, weight=1):
    return mat([[weight*x*y.conj() for y in v] for x in v])


def mv(u, v):
    return tuple(sum((u[i][j]*v[j] for j in range(len(v))), G()) for i in range(len(u)))


def defect_min(u):
    u = kron(eye(2), u)
    tests = [proj(mv(u, v)) for v in psis]
    for a, b in permutations(range(4), 2):
        for phase in (G.of(1), G.of(-1), I, -I):
            tests.append(proj(tuple(x+phase*y for x, y in zip(psis[a], psis[b])), F(1, 2)))
    dual = [y for y in tests if all(pair(y, e) >= 0 for e in es)]
    return min(pair(y, ad(u, e)) for y in dual for e in es)


d_min, j_min = defect_min(D), defect_min(J)
check("ZF", d_min == F(-1, 10) and j_min == F(-1, 8), f"drive={d_min}, mixer={j_min}")

# The six-test cone: each signed permutation permutes the octahedral tests.
oct_tests = {(0, 0, 0)}
oct_tests = {tuple(sign if j == i else 0 for j in range(3)) for i in range(3) for sign in (-1, 1)}
rots = []
for perm in permutations(range(3)):
    parity = (-1)**sum(perm[i] > perm[j] for i in range(3) for j in range(i+1, 3))
    for signs in product((-1, 1), repeat=3):
        if parity*signs[0]*signs[1]*signs[2] == 1:
            rots.append((perm, signs))
oct_ok = len(rots) == 24 and all({tuple(s[j]*v[p[j]] for j in range(3)) for v in oct_tests} == oct_tests
                               for p, s in rots)
image = (F(1, 4), F(5, 4), F(1))
check("OCT", oct_ok and all(1+sum(v) >= 0 for v in oct_tests)
      and min(1+sum(x*y for x, y in zip(image, v)) for v in oct_tests) == F(-1, 4), "24 actions; failing value=-1/4")

open_ok = True
for k in range(1, 7):
    p = F(3, 8)**k
    a, b = p+(1-p)*F(3, 5), (1-p)*F(4, 5)
    open_ok &= a*a+b*b == 1-F(4, 5)*p*(1-p) and a*a+b*b < 1
check("OPEN", open_ok and F(3, 5)**2+F(4, 5)**2 == 1
      and (F(3, 5), F(4, 5)) != (1, 0), "finite images interior; limiting boundary point excluded")

kappa = F(3, 2)
kp = scale(F(1, 2), add(eye(4), scale(kappa, kron(X, eye(2)))))
km = scale(F(1, 2), add(eye(4), scale(-kappa, kron(X, eye(2)))))
v = (G.of(1), G(), G.of(-1), G())
negative_psd = sum((x.conj()*y for x, y in zip(v, mv(kp, v))), G())
check("KAPPA", pair(kp, km) == F(-5, 4) and negative_psd == G.of(F(-1, 2)), "pair=-5/4; PSD test=-1/2")
check("CC-Z", any(stopped(1, unit(2, a, b), correct=False) != formula(1, unit(2, a, b))
                  for a, b in product(range(2), repeat=2)))
check("CC-OUTCOME", mul(adj(raw[1]), raw[1]) != scale(F(5, 8), eye(2)))


def uniform_channel(rho):
    inp = scale(F(1, 4), kron(rho, eye(4)))
    full = ad(U, inp)
    parts = [mat([[full[4*a+j][4*b+j] for b in range(2)] for a in range(2)]) for j in range(4)]
    return msum([parts[0]] + [ad(Z, x) for x in parts[1:]], 2)


check("CC-RESET", any(uniform_channel(unit(2, a, b)) != formula(1, unit(2, a, b))
                      for a, b in product(range(2), repeat=2)))
check("CC-ID", defect_min(eye(2)) >= 0)
check("CC-CLIFFORD", defect_min(X) >= 0)
failed = [name for name, ok in checks if not ok]
print(f"CHANNEL-CHECK: {'VOID' if failed else 'PASS'}; {len(checks)} checks; 140 matrix-unit cases")
if failed:
    print("Failed: " + ", ".join(failed))
sys.exit(bool(failed))
