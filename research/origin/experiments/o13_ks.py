#!/usr/bin/env python3
"""o13_ks.py -- research/origin, round 4, node O13: is the Kochen-Specker sphere tower's re-preparation law
realizable by an InstAvail protocol with ancillas?

The law along a unit vector n, on the token's completed body (the Bloch ball): F^n_s(X) = tr(P X) P with
P = Pi^n_s = (1 + s n.sigma)/2, s = +1, -1.  Exact arithmetic only (sympy radicals; Z[zeta_N][1/2] with integer
coordinates over a power of two, as in o12_angle.py).  No floating point enters any decision.

Checks (S0 in NOTES-O13, written 2026-10-11T04:50:02Z, addendum 04:53:08Z, before run 1):
  K1 over the test axes, Pi^n_+ is submonomial exactly for n = z and n = -z.
  K2 the Choi matrix of F^n_+ has rank 1 and equals Pi^T (x) Pi; that of F^n_+ + F^n_- has rank 2.
  K3 with U_n the SU(2) matrix taking |0> to |n+>, conj(U_n) . conj(P_s) . conj(U_n^dagger) = F^n_s on all four
     matrix units, for every test axis.
  K4 the rank-one Lueders selectors on the configuration basis equal F^z_+ and F^z_- (the native readout).
  K5 (unitary conjugation only) at pi/4 the axes U z over the level-one classes are exactly the six octahedral axes;
     at pi/8 more than 100 distinct axes U z appear within the first 3000 classes.
  PC1 Pi^z_+ is submonomial; PC2 K3 at n = x.                                     (each expected True)
  CC1 the submonomial test accepts Pi^x_+; CC2 the construction with U_n^dagger in place of U_n reproduces the law
  along (3/5, 4/5, 0); CC3 the Choi rank of F^n_+ + F^n_- is 1; CC4 (4/5, 0, 3/5) is a unitary conjugate of z at
  pi/4.                                                                          (each expected False)

Decision rule (fixed before run 1):
  VERDICT O13-KS-LAW-NEEDS-A-COHERENT-MEMBER-PER-AXIS  if K1-K5 hold, PC1-PC2 are True and CC1-CC4 are False;
  VERDICT VOID                                         if any countercontrol is True or any positive control False;
  VERDICT UNDECIDED                                    otherwise.
"""

from math import gcd

import sympy as sp

R = sp.Rational
I = sp.I
XS = sp.Symbol('x')
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -I], [I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
UNITS = [sp.Matrix(2, 2, lambda a, b, i=i, j=j: 1 if (a, b) == (i, j) else 0) for i in range(2) for j in range(2)]
AXES = [('z', (0, 0, 1)), ('-z', (0, 0, -1)), ('x', (1, 0, 0)), ('y', (0, 1, 0)),
        ('(4/5,0,3/5)', (R(4, 5), 0, R(3, 5))), ('(3/5,4/5,0)', (R(3, 5), R(4, 5), 0)),
        ('(2/3,1/3,2/3)', (R(2, 3), R(1, 3), R(2, 3))), ('(0,3/5,4/5)', (0, R(3, 5), R(4, 5)))]


def zero(M):
    return all(sp.simplify(e) == 0 for e in M)


def proj(n, s):
    return (sp.eye(2) + s * (n[0] * SX + n[1] * SY + n[2] * SZ)) / 2


def submonomial(M):
    nz = [[sp.simplify(M[a, b]) != 0 for b in range(2)] for a in range(2)]
    return all(sum(row) <= 1 for row in nz) and all(sum(nz[a][b] for a in range(2)) <= 1 for b in range(2))


def ks(n, s):
    P = proj(n, s)
    return lambda X: (P * X).trace() * P


def kron(A, B):
    return sp.Matrix(4, 4, lambda r, c: A[r // 2, c // 2] * B[r % 2, c % 2])


def choi(F):
    C = sp.zeros(4, 4)
    for k, E in enumerate(UNITS):
        C += kron(E, F(E))
    return C


def U_of(n):
    a = sp.sqrt((1 + sp.sympify(n[2])) / 2)
    if a == 0:
        return sp.Matrix([[0, -1], [1, 0]])
    b = (n[0] + I * n[1]) / (2 * a)
    return sp.Matrix([[a, -sp.conjugate(b)], [b, a]])


P0 = sp.Matrix([[1, 0], [0, 0]])
P1 = sp.Matrix([[0, 0], [0, 1]])


def construction(U, s):
    P = P0 if s == 1 else P1
    Pi = U * P * U.H
    return lambda X: Pi * X * Pi


def same_map(F, G):
    return all(zero(sp.expand(F(E) - G(E))) for E in UNITS)


class Ring:
    """Z[zeta_N][1/2], exact (as in o12_angle.py)."""

    def __init__(self, N):
        self.N = N
        coeffs = sp.Poly(sp.cyclotomic_poly(N, XS), XS).all_coeffs()
        self.d = len(coeffs) - 1
        self.phi = [int(c) for c in reversed(coeffs)]
        self.pw = []
        v = [0] * self.d
        v[0] = 1
        for _ in range(N):
            self.pw.append(tuple(v))
            top = v[-1]
            w = [0] + v[:-1]
            if top:
                for i in range(self.d):
                    w[i] -= top * self.phi[i]
            v = w

    def norm(self, c, e):
        c = list(c)
        while e > 0 and all(x % 2 == 0 for x in c):
            c = [x // 2 for x in c]
            e -= 1
        if all(x == 0 for x in c):
            e = 0
        return (tuple(c), e)

    def zeta(self, j):
        return (self.pw[j % self.N], 0)

    def const(self, n):
        v = [0] * self.d
        v[0] = n
        return self.norm(v, 0)

    def add(self, a, b):
        (ca, ea), (cb, eb) = a, b
        e = max(ea, eb)
        return self.norm([x * (1 << (e - ea)) + y * (1 << (e - eb)) for x, y in zip(ca, cb)], e)

    def neg(self, a):
        return (tuple(-x for x in a[0]), a[1])

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def half(self, a):
        return self.norm(a[0], a[1] + 1)

    def mul(self, a, b):
        (ca, ea), (cb, eb) = a, b
        d = self.d
        prod = [0] * (2 * d - 1)
        for i, x in enumerate(ca):
            if x:
                for j, y in enumerate(cb):
                    if y:
                        prod[i + j] += x * y
        res = [0] * d
        for k, cf in enumerate(prod):
            if cf:
                p = self.pw[k % self.N]
                for i in range(d):
                    if p[i]:
                        res[i] += cf * p[i]
        return self.norm(res, ea + eb)

    def conj(self, a):
        ca, e = a
        res = [0] * self.d
        for i, x in enumerate(ca):
            if x:
                p = self.pw[(-i) % self.N]
                for k in range(self.d):
                    if p[k]:
                        res[k] += x * p[k]
        return self.norm(res, e)

    def I(self):
        return self.zeta(self.N // 4)

    def mm(self, A, B):
        out = []
        for i in range(2):
            row = []
            for j in range(2):
                acc = self.const(0)
                for k in range(2):
                    acc = self.add(acc, self.mul(A[i][k], B[k][j]))
                row.append(acc)
            out.append(row)
        return out

    def dag(self, A):
        return [[self.conj(A[j][i]) for j in range(2)] for i in range(2)]

    def to_sympy(self, a):
        ca, e = a
        z = sp.exp(2 * sp.pi * I / self.N)
        return sum(c * z ** i for i, c in enumerate(ca)) / 2 ** e


def ring_gates(N, k):
    Rg = Ring(N)
    c = Rg.half(Rg.add(Rg.zeta(k), Rg.zeta(-k)))
    s = Rg.half(Rg.mul(Rg.neg(Rg.I()), Rg.sub(Rg.zeta(k), Rg.zeta(-k))))
    one, zer = Rg.const(1), Rg.const(0)
    rot = [[c, Rg.neg(s)], [s, c]]
    S = [[one, zer], [zer, Rg.I()]]
    X = [[zer, one], [one, zer]]
    Z = [[one, zer], [zer, Rg.const(-1)]]
    return Rg, rot, S, X, Z


def axes_by_bfs(N, k, cap):
    Rg, rot, S, X, Z = ring_gates(N, k)

    def key(G):
        Gd = Rg.dag(G)
        a = Rg.mm(Rg.mm(G, X), Gd)
        b = Rg.mm(Rg.mm(G, Z), Gd)
        return (a[0][0], a[0][1], a[1][0], a[1][1], b[0][0], b[0][1], b[1][0], b[1][1])

    one = [[Rg.const(1), Rg.const(0)], [Rg.const(0), Rg.const(1)]]
    seen = {key(one)}
    axes = {(Rg.const(1), Rg.const(0))}
    frontier = [one]
    closed = True
    while frontier:
        nxt = []
        for G in frontier:
            for g in (rot, S, X):
                H = Rg.mm(G, g)
                kH = key(H)
                if kH not in seen:
                    seen.add(kH)
                    nxt.append(H)
                    axes.add((kH[4], kH[6]))
                    if len(seen) >= cap:
                        return Rg, len(seen), axes, False
        frontier = nxt
    return Rg, len(seen), axes, closed


def main():
    out = []
    # K1, PC1, CC1
    sub = {name: submonomial(proj(n, 1)) for name, n in AXES}
    out.append('K1 submonomial Pi^n_+: ' + ', '.join('%s %s' % (name, sub[name]) for name, _ in AXES))
    k1 = all(sub[name] == (name in ('z', '-z')) for name, _ in AXES)
    pc1 = sub['z']
    cc1 = sub['x']
    # K2, CC3
    k2 = True
    cc3 = False
    for name, n in AXES:
        Cp = choi(ks(n, 1))
        Pi = proj(n, 1)
        k2 = k2 and Cp.rank() == 1 and zero(Cp - kron(Pi.T, Pi))
        Ct = choi(lambda X, n=n: ks(n, 1)(X) + ks(n, -1)(X))
        rk = Ct.rank()
        k2 = k2 and rk == 2
        cc3 = cc3 or rk == 1
    out.append('K2 Choi rank one and equal to Pi^T (x) Pi for F^n_+, rank two for the sum, every test axis: %s' % k2)
    # K3, PC2, CC2
    k3 = True
    for name, n in AXES:
        U = U_of(n)
        unit = zero(U.H * U - sp.eye(2))
        ok_n = unit and all(same_map(construction(U, s), ks(n, s)) for s in (1, -1))
        out.append('K3 %s: U unitary %s, construction = law %s' % (name, unit, ok_n))
        k3 = k3 and ok_n
    pc2 = all(same_map(construction(U_of((1, 0, 0)), s), ks((1, 0, 0), s)) for s in (1, -1))
    n_cc2 = (R(3, 5), R(4, 5), 0)
    Uw = U_of(n_cc2).H
    cc2 = all(same_map(construction(Uw, s), ks(n_cc2, s)) for s in (1, -1))
    # K4
    k4 = same_map(lambda X: P0 * X * P0, ks((0, 0, 1), 1)) and same_map(lambda X: P1 * X * P1, ks((0, 0, 1), -1))
    out.append('K4 rank-one Lueders selectors on the configuration basis = F^z_+, F^z_-: %s' % k4)
    # K5, CC4
    R8, n8, axes4, closed4 = axes_by_bfs(8, 1, 5000)
    octa = {(R8.const(1), R8.const(0)), (R8.const(-1), R8.const(0)), (R8.const(0), R8.const(1)),
            (R8.const(0), R8.const(-1)), (R8.const(0), R8.I()), (R8.const(0), R8.neg(R8.I()))}
    k5a = closed4 and n8 == 24 and axes4 == octa
    out.append('K5 pi/4: classes %d, closed %s, axes %d, equal to the six octahedral axes %s' % (
        n8, closed4, len(axes4), axes4 == octa))
    cc4 = False
    for (az, ab) in axes4:
        nz = sp.nsimplify(sp.simplify(R8.to_sympy(az)))
        nb = sp.simplify(R8.to_sympy(ab))
        if sp.simplify(nz - R(3, 5)) == 0 and sp.simplify(nb - R(4, 5)) == 0:
            cc4 = True
    R16, n16, axes8, closed8 = axes_by_bfs(16, 1, 3000)
    k5b = (not closed8) and len(axes8) > 100
    out.append('K5 pi/8: classes reached %d, closed %s, distinct axes %d' % (n16, closed8, len(axes8)))
    k5 = k5a and k5b
    pc = {'PC1': pc1, 'PC2': pc2}
    cc = {'CC1': cc1, 'CC2': cc2, 'CC3': cc3, 'CC4': cc4}
    ok = {'K1': k1, 'K2': k2, 'K3': k3, 'K4': k4, 'K5': k5}
    for name in sorted(pc):
        out.append('%s %s' % (name, pc[name]))
    for name in sorted(cc):
        out.append('%s %s' % (name, cc[name]))
    for name in sorted(ok):
        out.append('%s %s' % (name, ok[name]))
    if any(cc.values()) or not all(pc.values()):
        verdict = 'VOID'
    elif all(ok.values()):
        verdict = 'O13-KS-LAW-NEEDS-A-COHERENT-MEMBER-PER-AXIS'
    else:
        verdict = 'UNDECIDED'
    out.append('VERDICT %s' % verdict)
    print('\n'.join(out))


if __name__ == '__main__':
    main()
