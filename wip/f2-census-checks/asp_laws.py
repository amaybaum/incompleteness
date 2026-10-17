#!/usr/bin/env python3
"""asp_laws.py -- audit check C (exact integer/Fraction arithmetic). Decides nothing for any round.

Question: which one-step registered-value laws do E1-admissible classical data produce?  E1-admissible
here means: an affine symplectic map of F_q^{2N} (the only configuration bijections with a CP image,
F2-5 OD-REV at (3,1)), a registered start (every registered current value fixed) and the counting
measure on every hidden coordinate (F2-5 OD-PREP).  Enumerates Sp(2N, 3) for N = 1, 2 by closure from
transvections, and for each element computes T[i][j] = P(registered x' = j | registered x = i).
Translations only relabel outcomes, so linear maps suffice.  Registration patterns: all sites, and at
N = 2 site 1 only (site 2 entirely hidden, counting measure).
Claim tested: every row of every T is the uniform law on an affine coset (entries 0 or 1/q^r).
Control: the group orders must be |Sp(2,3)| = 24 and |Sp(4,3)| = 51840.
"""
from fractions import Fraction
from itertools import product
q = 3

def mat_mul(A, B):
    n = len(A)
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(n)) % q for j in range(n)) for i in range(n))

def omega(N):
    n = 2 * N; J = [[0] * n for _ in range(n)]
    for i in range(N):
        J[i][N + i] = 1; J[N + i][i] = q - 1
    return J

def transvections(N):
    n = 2 * N; J = omega(N); gens = []
    for v in product(range(q), repeat=n):
        if not any(v): continue
        # T_v(z) = z + <z, v> v with <z,v> = z^T J v
        Jv = [sum(J[i][k] * v[k] for k in range(n)) % q for i in range(n)]
        M = tuple(tuple((int(i == j) + v[i] * Jv[j]) % q for j in range(n)) for i in range(n))
        gens.append(M)
    return gens

def group(N):
    gens = transvections(N)
    n = 2 * N
    I = tuple(tuple(int(i == j) for j in range(n)) for i in range(n))
    seen = {I}; frontier = [I]
    while frontier:
        new = []
        for g in frontier:
            for t in gens:
                h = mat_mul(t, g)
                if h not in seen:
                    seen.add(h); new.append(h)
        frontier = new
    return seen

def law(S, N, reg):
    """reg: list of registered site indices; coordinates z = (x_1..x_N, xi_1..xi_N)."""
    n = 2 * N
    hidden = [i for i in range(n) if not (i < N and i in reg)]
    regs = [i for i in reg]
    T = {}
    for xv in product(range(q), repeat=len(regs)):
        row = {}
        for hv in product(range(q), repeat=len(hidden)):
            z = [0] * n
            for i, val in zip(regs, xv): z[i] = val
            for i, val in zip(hidden, hv): z[i] = val
            z2 = [sum(S[i][k] * z[k] for k in range(n)) % q for i in range(n)]
            out = tuple(z2[i] for i in regs)
            row[out] = row.get(out, 0) + Fraction(1, q ** len(hidden))
        T[xv] = row
    return T

def coset_uniform(row, r):
    vals = set(row.values())
    if len(vals) != 1: return False
    (v,) = vals
    s = len(row)
    if v * s != 1: return False
    # support is an affine coset: closed under the affine combinations a + b - c
    pts = list(row)
    S = set(pts)
    return all(tuple((a[i] + b[i] - c[i]) % q for i in range(r)) in S for a in pts for b in pts for c in pts)

ok = True
for N, regs in [(1, [0]), (2, [0, 1]), (2, [0])]:
    G = group(N)
    order_ok = len(G) == {1: 24, 2: 51840}[N]
    shapes = {}
    allok = True
    for S in G:
        T = law(S, N, regs)
        for xv, row in T.items():
            c = coset_uniform(row, len(regs))
            allok &= c
            shapes[len(row)] = shapes.get(len(row), 0) + 1
    print('N=%d registered sites %s: |Sp| = %d (control %s); every row uniform on an affine coset: %s; '
          'support sizes {size: rows} = %s' % (N, [r + 1 for r in regs], len(G), order_ok, allok, dict(sorted(shapes.items()))))
    ok &= order_ok and allok
print('CHECK-C', 'PASS' if ok else 'FAIL', ': E1-admissible classical data give only coset-uniform one-step laws; '
      'e.g. no row (2/3, 1/3, 0) is realizable in this class')
