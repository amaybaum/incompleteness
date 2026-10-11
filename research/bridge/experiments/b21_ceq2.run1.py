#!/usr/bin/env python3
"""b21_ceq2.py -- node B21 of research/bridge (round 5), S0 addendum: no orbit of the tower's closure
G = T^2 . {1, CNOT, X_B, CNOT X_B} (B10-4; b21_torus T1) consists of maximally entangled states, so no G-invariant
rank-one defect set with H1 and a self-dual surgery has an orbit at c = 2 (claim G4). Exact arithmetic (sympy symbols;
Python integers for the exhaustive search; Gaussian rationals for the torus samples).

DECISION RULE (fixed 2026-10-11T10:19:09Z, from `date -u` immediately before writing; before run 1).

Basis |00>, |01>, |10>, |11> (control first); CNOT; X_B = I (x) X; T^2 = {U(u, v) = diag(e^{iu}, e^{-iu}, e^{iv}, e^{-iv})}.
For h in C^4 reshaped as the 2 x 2 matrix [[h00, h01], [h10, h11]], D(h) = h00 h11 - h01 h10; with N = |h|^2,
h is maximally entangled iff 4 |D(h)|^2 = N^2, and a product iff D(h) = 0. A defect I - c P_h at c = 2 pairs
nonnegatively with every product state iff h is maximally entangled.

CHECKS
  Q1  computed from the 4 x 4 matrices, symbolically in the eight real coordinates of h and in u, v:
      |D(U(u,v) h)|^2      = |h00 h11|^2 + |h01 h10|^2 - 2 Re(e^{2i(u-v)} h00 h11 conj(h01 h10)),
      |D(U(u,v) CNOT h)|^2 = |h00 h10|^2 + |h01 h11|^2 - 2 Re(e^{2i(u+v)} h00 h10 conj(h01 h11)).
  Q2  the algebraic core of the case analysis, symbolically in moduli a, b, p, q: 1 - a^2 - b^2 = -(a - b)^2 + (1 - 2ab),
      so a^2 + b^2 + p^2 + q^2 = 1 with ab = 1/2 gives p^2 + q^2 = -(a - b)^2 (hence p = q = 0, a = b).
  Q3  the four Bell states Phi+-, Psi+-: maximally entangled; each CNOT image an exact product (D = 0, an explicit
      factorization); the defect I - 2 P_{CNOT h} pairs to -1 with the product projector P_{CNOT h}.
  Q4  countercontrol (CNOT load-bearing): the orbit of Phi+ under T^2 . <X_B> is maximally entangled at the 64
      Gaussian-rational torus points {+-1, +-i, (3 +- 4i)/5, (4 +- 3i)/5}^2 (both components), exactly.
  Q5  exhaustive control, Python integers: over every nonzero h with Gaussian-integer components of real and imaginary
      parts in {-2, ..., 2} (25^4 - 1 vectors), the number whose whole G-orbit is maximally entangled -- by Q1, exactly
      the h with h00 h11 conj(h01 h10) = 0, 4(|h00 h11|^2 + |h01 h10|^2) = N^2, h00 h10 conj(h01 h11) = 0 and
      4(|h00 h10|^2 + |h01 h11|^2) = N^2 (X_B is local and normalizes T^2) -- is 0; countercontrol: the number meeting
      the first two conditions alone (the orbit under T^2 . <X_B>, no CNOT) is positive.

VERDICT B21-CEQ2-EXACT iff Q1-Q5 all PASS; otherwise VERDICT B21-CEQ2-FAILED followed by the failing ids.
Run from experiments/:  python3 -I -B b21_ceq2.py > b21_ceq2.out 2> b21_ceq2.err
"""
import itertools
import sys

import sympy as sp

I = sp.I
RESULTS = []


def record(name, ok, msg):
    RESULTS.append((name, bool(ok)))
    print('[%s] %s: %s' % ('PASS' if ok else 'FAIL', name, msg))


def cnot():
    return sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])


def xb():
    return sp.Matrix([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])


def torus(eu, ev):
    """U(u, v) from the unit complex numbers eu = e^{iu}, ev = e^{iv} (inverse = conjugate)."""
    return sp.diag(eu, sp.conjugate(eu), ev, sp.conjugate(ev))


def det2(h):
    return h[0] * h[3] - h[1] * h[2]


def q1():
    xs = sp.symbols('x0:8', real=True)
    u, v = sp.symbols('u v', real=True)
    h = sp.Matrix([xs[0] + I * xs[1], xs[2] + I * xs[3], xs[4] + I * xs[5], xs[6] + I * xs[7]])
    U = sp.diag(sp.exp(I * u), sp.exp(-I * u), sp.exp(I * v), sp.exp(-I * v))
    ok = True
    for label, vec, A, B, ph in (('U h', U * h, h[0] * h[3], h[1] * h[2], sp.exp(2 * I * (u - v))),
                                 ('U CNOT h', U * cnot() * h, h[0] * h[2], h[1] * h[3], sp.exp(2 * I * (u + v)))):
        D = det2(vec)
        lhs = sp.expand(D * sp.conjugate(D))
        rhs = sp.expand(A * sp.conjugate(A) + B * sp.conjugate(B)
                        - (ph * A * sp.conjugate(B) + sp.conjugate(ph * A * sp.conjugate(B))))
        diff = sp.simplify(sp.expand(sp.expand_complex(lhs - rhs)))
        ok = ok and diff == 0
    record('Q1', ok, '|D(U h)|^2 and |D(U CNOT h)|^2 from the matrices equal the two modulus formulas, symbolically')


def q2():
    a, b, p, q = sp.symbols('a b p q', nonnegative=True)
    core = sp.expand((1 - a**2 - b**2) - (-(a - b)**2 + (1 - 2 * a * b)))
    # with the constraints substituted: p^2 + q^2 = 1 - a^2 - b^2 and ab = 1/2
    pq = sp.expand((1 - a**2 - b**2).subs(b, sp.Rational(1, 2) / a) - (-(a - sp.Rational(1, 2) / a)**2))
    ok = core == 0 and sp.simplify(pq) == 0
    record('Q2', ok, '1 - a^2 - b^2 = -(a - b)^2 + (1 - 2ab) identically; at ab = 1/2, p^2 + q^2 = -(a - b)^2')


def q3():
    s = sp.sqrt(2)
    bells = {'Phi+': [1, 0, 0, 1], 'Phi-': [1, 0, 0, -1], 'Psi+': [0, 1, 1, 0], 'Psi-': [0, 1, -1, 0]}
    ok = True
    parts = []
    for name, comps in bells.items():
        h = sp.Matrix(comps) / s
        N = sp.simplify((h.H * h)[0])
        maxent = sp.simplify(4 * sp.Abs(det2(h))**2 - N**2) == 0
        g = cnot() * h
        prod = sp.simplify(det2(g)) == 0
        # explicit factorization g = x (x) y
        if g[0] != 0 or g[1] != 0:
            x = sp.Matrix([1, sp.simplify(g[2] / g[0]) if g[0] != 0 else sp.simplify(g[3] / g[1])])
            y = sp.Matrix([g[0], g[1]])
        else:
            x = sp.Matrix([0, 1])
            y = sp.Matrix([g[2], g[3]])
        kron = sp.Matrix([x[0] * y[0], x[0] * y[1], x[1] * y[0], x[1] * y[1]])
        fact = sp.simplify(kron - g) == sp.zeros(4, 1)
        P = (g * g.H) / sp.simplify((g.H * g)[0])
        d = sp.eye(4) - 2 * P
        pairing = sp.simplify((d * P).trace())
        ok = ok and maxent and prod and fact and pairing == -1
        parts.append('%s: maxent %s, CNOT image product %s (factorized %s), pairing %s' % (name, maxent, prod, fact, pairing))
    record('Q3', ok, '; '.join(parts))


def q4():
    pts = [sp.Integer(1), sp.Integer(-1), I, -I, (3 + 4 * I) / 5, (3 - 4 * I) / 5, (4 + 3 * I) / 5, (4 - 3 * I) / 5]
    h = sp.Matrix([1, 0, 0, 1])
    N = 2
    ok = True
    count = 0
    for eu, ev in itertools.product(pts, repeat=2):
        U = torus(eu, ev)
        for g in (U * h, U * xb() * h):
            val = sp.expand(4 * det2(g) * sp.conjugate(det2(g)))
            ok = ok and sp.simplify(val - N**2) == 0
            count += 1
    cn = sp.simplify(det2(cnot() * h)) == 0
    record('Q4', ok and cn, 'Phi+ under T^2 . <X_B>: 4|D|^2 = N^2 at all %d sampled orbit points %s; its CNOT image a product %s'
           % (count, ok, cn))


def q5():
    vals = [complex(a, b) for a in range(-2, 3) for b in range(-2, 3)]
    gi = [(a, b) for a in range(-2, 3) for b in range(-2, 3)]

    def mul(x, y):
        return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])

    def conj(x):
        return (x[0], -x[1])

    def n2(x):
        return x[0] * x[0] + x[1] * x[1]

    full, local, total = 0, 0, 0
    for h00, h01, h10, h11 in itertools.product(gi, repeat=4):
        N = n2(h00) + n2(h01) + n2(h10) + n2(h11)
        if N == 0:
            continue
        total += 1
        A, B = mul(h00, h11), mul(h01, h10)
        c1 = mul(A, conj(B)) == (0, 0) and 4 * (n2(A) + n2(B)) == N * N
        if not c1:
            continue
        local += 1
        A2, B2 = mul(h00, h10), mul(h01, h11)
        c2 = mul(A2, conj(B2)) == (0, 0) and 4 * (n2(A2) + n2(B2)) == N * N
        if c2:
            full += 1
    del vals
    record('Q5', full == 0 and local > 0 and total == 25**4 - 1,
           'over %d nonzero Gaussian-integer h: whole G-orbit maximally entangled %d; T^2 . <X_B>-orbit (no CNOT) '
           'maximally entangled %d' % (total, full, local))


def main():
    q1()
    q2()
    q3()
    q4()
    q5()
    npass = sum(1 for _, ok in RESULTS if ok)
    nfail = len(RESULTS) - npass
    print()
    print('PASS %d  FAIL %d' % (npass, nfail))
    if nfail == 0:
        print('VERDICT B21-CEQ2-EXACT')
    else:
        print('VERDICT B21-CEQ2-FAILED ' + ' '.join(n for n, ok in RESULTS if not ok))


if __name__ == '__main__':
    main()
    sys.exit(0)
