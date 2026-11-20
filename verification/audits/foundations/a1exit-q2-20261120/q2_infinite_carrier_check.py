#!/usr/bin/env python3
"""A1-EXIT Q2: SM Theorem 1a on one infinite carrier, in exact rational arithmetic.

A witness, not a proof: the proof of Theorem 1a is the ring identity checked by the Lean kernel
(verification/lean/OI_Structural_Core.lean, MZ.mz_identity and MZ.kernel_equivariant). This script checks
that the state-applied display of SM Theorem 1a holds on an infinite carrier with an infinite-rank
projection and an infinite symmetry group, where no finite-dimensional linear algebra is available, and
that its countercontrols fail as they must.

Carrier S = Z x {0,1}; bijection phi(n,0) = (n+1,1), phi(n,1) = (n-1,0); U f = f o phi on all real
functions of S (represented lazily as memoized callables with Fraction values). Symmetry group: the
translations (n,b) -> (n+k,b) and the reflection rho(n,b) = (-n,1-b), both commuting with phi; R_g f =
f o g^-1. Projection P f(n,b) = (f(n,0) + f(n,1))/2 (equivariant, idempotent, infinite rank).
Countercontrol projection P' f(n,b) = f(n,0) (idempotent, translation equivariant, not rho equivariant).

The initial observable x0 is unbounded and not summable. Checks are evaluated on a finite window of
points; every value is exact. Exit status 0 iff every check and countercontrol behaves as required.
Standard library only:  python3 -I q2_infinite_carrier_check.py
"""
import sys
from fractions import Fraction as Fr
from functools import lru_cache

W, T = 6, 6                       # window |n| <= W, times t <= T, kernels m <= T
PTS = [(n, b) for n in range(-W, W + 1) for b in (0, 1)]


def fn(g):
    return lru_cache(maxsize=None)(g)


def phi(x):
    n, b = x
    return (n + 1, 1) if b == 0 else (n - 1, 0)


def U(f):
    return fn(lambda x: f(phi(x)))


def P(f):
    return fn(lambda x: (f((x[0], 0)) + f((x[0], 1))) / 2)


def Pbad(f):
    return fn(lambda x: f((x[0], 0)))


def compl(Pr):
    return lambda f: fn(lambda x: f(x) - Pr(f)(x))


def add(f, g):
    return fn(lambda x: f(x) + g(x))


def rho(x):
    return (-x[0], 1 - x[1])          # an involution, so R_rho f = f o rho


def tr(k):
    return lambda f: fn(lambda x: f((x[0] - k, x[1])))


def R_rho(f):
    return fn(lambda x: f(rho(x)))


def comp(*ops):
    def h(f):
        for op in reversed(ops):
            f = op(f)
        return f
    return h


def power(op, m):
    def h(f):
        for _ in range(m):
            f = op(f)
        return f
    return h


def eq(f, g):
    return all(f(x) == g(x) for x in PTS)


x0 = fn(lambda x: Fr(x[0] ** 3 + 7 * x[1] * x[0] - 2 * x[1] + 1) + Fr((-1) ** (x[0] % 2), 3))
probe = [x0, fn(lambda x: Fr(x[0] ** 2 * (1 + x[1]))), fn(lambda x: Fr(1 if x[0] % 3 == 0 else -x[1]))]


def blocks(Pr):
    Q = compl(Pr)
    return comp(Pr, U, Pr), comp(Pr, U, Q), comp(Q, U, Pr), comp(Q, U, Q), Q


def display_holds(Pr, drop_memory=False):
    A, B, C, D, Q = blocks(Pr)
    traj = [x0]
    for _ in range(T + 1):
        traj.append(U(traj[-1]))
    p = [Pr(x) for x in traj]
    q0 = Q(x0)
    for t in range(T):
        rhs = add(A(p[t]), B(power(D, t)(q0)))
        if not drop_memory:
            for s in range(t):
                rhs = add(rhs, comp(B, power(D, t - 1 - s), C)(p[s]))
        if not eq(p[t + 1], rhs):
            return False
    return True


def kernels_commute(Pr, R):
    A, B, C, D, Q = blocks(Pr)
    return all(eq(comp(B, power(D, m), C, R)(f), comp(R, B, power(D, m), C)(f))
               for m in range(T + 1) for f in probe)


results = {}
results['inputs: U commutes with rho and translations'] = all(
    eq(U(R(f)), R(U(f))) for R in (R_rho, tr(1), tr(-3)) for f in probe)
results['inputs: P idempotent, commutes with rho and translations'] = all(
    eq(P(P(f)), P(f)) for f in probe) and all(eq(P(R(f)), R(P(f))) for R in (R_rho, tr(1)) for f in probe)
results['inputs: P x0 nonzero at both window edges'] = all(P(x0)((n, 0)) != 0 for n in (-W, W))
results['Theorem 1a display, equivariant P'] = display_holds(P)
results['Theorem 1a kernels commute with rho and translations'] = all(
    kernels_commute(P, R) for R in (R_rho, tr(1), tr(2)))
results["control: display also holds for the non-equivariant P'"] = display_holds(Pbad)
results["control: P' is idempotent and translation equivariant"] = all(
    eq(Pbad(Pbad(f)), Pbad(f)) and eq(Pbad(tr(1)(f)), tr(1)(Pbad(f))) for f in probe)
# Countercontrols: each must come out False.
counter = {
    'countercontrol: display without the memory sum': display_holds(P, drop_memory=True),
    "countercontrol: P' kernels commute with rho": kernels_commute(Pbad, R_rho),
}

ok = all(results.values()) and not any(counter.values())
for k, v in results.items():
    print('%-6s %s' % ('PASS' if v else 'FAIL', k))
for k, v in counter.items():
    print('%-6s %s' % ('PASS' if not v else 'FAIL',
                       k + (' (fails, as required)' if not v else ' (holds: countercontrol vacuous)')))
print('q2_infinite_carrier_check:', 'PASS' if ok else 'FAIL')
sys.exit(0 if ok else 1)
