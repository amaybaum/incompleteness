#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OIBridge/CubicIsotropy.lean.

[SM] Corollary 1a says cubic symmetry forbids quadratic anisotropy. Formalizing it surfaced a scope
error in the manuscript, which this round repaired: the corollary assumed only a finite SECOND
moment and concluded an O(|k|^4) remainder. Finite second moment gives o(|k|^2) and nothing sharper
— a symmetric kernel can have finite second moment and infinite fourth moment, and its remainder is
then nonanalytic between quadratic and quartic order. The statement is now split into (i) the
o(|k|^2) clause under a second moment, which carries the whole negative content, and (ii) the
O(|k|^4) clause under a fourth moment.

  A1  the ALGEBRAIC CORE, exhaustively: every O_h-invariant symmetric form on R^3 is a multiple of
      the identity, checked over the whole 48-element group by exact rational linear algebra, with
      the invariant subspace's dimension computed to be 1.
  A2  COUNTERCONTROL for the group: drop the sign flips, or drop the permutations, and the
      invariant space is strictly larger. Both generator families are load-bearing.
  A3  the quadratic form of an invariant Q is a multiple of |k|^2 exactly — no anisotropy survives
      at quadratic order.
  A4  COUNTERCONTROL at quartic order: k1^4+k2^4+k3^4 is O_h-invariant and NOT rotationally
      invariant, so the corollary's "need not be rotationally invariant" is exhibited rather than
      asserted. The second independent quartic invariant is checked too.
  A5  clause (ii): a finite-range kernel's symbol has an O(|k|^4) remainder, measured by the
      remainder's ratio to |k|^4 staying bounded as k -> 0.
  A6  THE COUNTERCONTROL THAT MOTIVATED THE REPAIR: a kernel with finite second moment and infinite
      fourth moment whose remainder-to-|k|^4 ratio DIVERGES as k -> 0, while the remainder-to-|k|^2
      ratio still goes to zero. Clause (i) holds on it and clause (ii) fails, which is exactly why
      the two hypotheses cannot be merged.
  A7  lint: the Lean file is imported by the gated bridge root, carries no sorry, proves the
      algebraic core and the quartic countercontrol, and RECORDS the two analytic clauses it does
      not prove rather than letting the algebraic core stand in for the whole corollary.

Usage:  python3 cubic_isotropy_probe.py
"""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

CHECKS = []


def check(label, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: {msg}", flush=True)


HERE = os.path.dirname(os.path.abspath(__file__))
BRIDGE = os.path.join(HERE, os.pardir, 'lean-mathlib')


# ----------------------------------------------------------------- the group O_h
def oh_group():
    """The 48 signed coordinate permutations of R^3, as (sigma, eps) pairs."""
    out = []
    for sigma in itertools.permutations(range(3)):
        for eps in itertools.product((1, -1), repeat=3):
            out.append((sigma, eps))
    return out


OH = oh_group()
SIGNS_ONLY = [(tuple(range(3)), eps) for eps in itertools.product((1, -1), repeat=3)]
PERMS_ONLY = [(sigma, (1, 1, 1)) for sigma in itertools.permutations(range(3))]


def act_on_form(g, Q):
    """(g . Q)[i][j] = eps_i eps_j Q[sigma i][sigma j] -- the action the Lean file uses."""
    sigma, eps = g
    return [[F(eps[i] * eps[j]) * Q[sigma[i]][sigma[j]] for j in range(3)] for i in range(3)]


def invariant_dim(group):
    """Dimension of the space of symmetric 3x3 forms fixed by every element of `group`.

    Solved exactly: stack (g.Q - Q) = 0 over all g, in the six symmetric coordinates."""
    coords = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]

    def basis_form(c):
        Q = [[F(0)] * 3 for _ in range(3)]
        a, b = c
        Q[a][b] = F(1)
        Q[b][a] = F(1)
        return Q

    rows = []
    for g in group:
        images = [act_on_form(g, basis_form(c)) for c in coords]
        for i in range(3):
            for j in range(3):
                rows.append([images[m][i][j] - basis_form(coords[m])[i][j]
                             for m in range(len(coords))])
    return nullspace_dim(rows, len(coords))


def nullspace_dim(rows, ncols):
    A = [r[:] for r in rows]
    rank, r = 0, 0
    for c in range(ncols):
        piv = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = F(1) / A[r][c]
        A[r] = [x * inv for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        r += 1
        rank += 1
        if r == len(A):
            break
    return ncols - rank


# ----------------------------------------------------------------- A1  the algebraic core
d_full = invariant_dim(OH)
ok1 = d_full == 1
# and the invariant really is the identity: check delta is fixed by every group element
DELTA = [[F(1) if i == j else F(0) for j in range(3)] for i in range(3)]
ok1 &= all(act_on_form(g, DELTA) == DELTA for g in OH)
# and any invariant form must be a multiple of delta -- verified on random symmetric forms
import random
rng = random.Random(9091)
for _ in range(200):
    Q = [[F(0)] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(i, 3):
            Q[i][j] = Q[j][i] = F(rng.randint(-4, 4))
    if all(act_on_form(g, Q) == Q for g in OH):
        b = Q[0][0]
        ok1 &= all(Q[i][j] == (b if i == j else F(0)) for i in range(3) for j in range(3))
check("A1", ok1,
      f"THE ALGEBRAIC CORE, exactly: over the whole {len(OH)}-element cubic point group the space of "
      f"invariant symmetric forms on R^3 has dimension {d_full}, computed by Gauss-Jordan over the "
      f"rationals in the six symmetric coordinates. The identity is invariant, and every invariant "
      f"form found among 200 random symmetric forms is a multiple of it. This is "
      f"`ohInvariant_iff`, and it is the whole content of `dim Sym^2(R^3)^{{O_h}} = 1`")

# ----------------------------------------------------------------- A2  countercontrol
d_signs = invariant_dim(SIGNS_ONLY)
d_perms = invariant_dim(PERMS_ONLY)
ok2 = d_signs == 3 and d_perms == 2 and d_full == 1
check("A2", ok2,
      f"COUNTERCONTROL for the GROUP. Sign flips alone leave a {d_signs}-dimensional invariant "
      f"space — they kill the off-diagonal entries but not the anisotropy among the three diagonal "
      f"entries. Permutations alone leave {d_perms} dimensions — they equate the diagonal and the "
      f"off-diagonal entries separately but kill neither. Only the full group gives {d_full}, so "
      f"both generator families in `OhInvariant` are load-bearing and neither can be dropped")

# ----------------------------------------------------------------- A3  quadratic isotropy
ok3 = True
for _ in range(300):
    b = F(rng.randint(-5, 5))
    Q = [[b if i == j else F(0) for j in range(3)] for i in range(3)]
    k = [F(rng.randint(-4, 4)) for _ in range(3)]
    lhs = sum(Q[i][j] * k[i] * k[j] for i in range(3) for j in range(3))
    rhs = b * sum(x ** 2 for x in k)
    ok3 &= lhs == rhs
check("A3", ok3,
      "THE QUADRATIC FORM of an invariant Q is exactly b|k|^2, on 300 random (b, k) pairs in exact "
      "rational arithmetic. That is `quadratic_isotropic`: whatever quadratic spatial structure "
      "survives projection is isotropic. Note what it does NOT say — b may be zero, in which case "
      "no metric arises at that order at all, which is the corollary's own Scope paragraph")

# ----------------------------------------------------------------- A4  quartic countercontrol
def q4a(k):
    return sum(x ** 4 for x in k)


def q4b(k):
    return sum(k[i] ** 2 * k[j] ** 2 for i in range(3) for j in range(i + 1, 3))


def act_vec(g, k):
    sigma, eps = g
    return [F(eps[i]) * k[sigma[i]] for i in range(3)]


ok4 = True
for _ in range(200):
    k = [F(rng.randint(-4, 4)) for _ in range(3)]
    for g in OH:
        ok4 &= q4a(act_vec(g, k)) == q4a(k)      # both quartic invariants are O_h-invariant
        ok4 &= q4b(act_vec(g, k)) == q4b(k)
# and neither is a function of |k|^2: two vectors of equal length, different quartic values
K1 = [F(1), F(0), F(0)]
K2 = [F(3, 5), F(4, 5), F(0)]
ok4 &= sum(x ** 2 for x in K1) == sum(x ** 2 for x in K2)
ok4 &= q4a(K1) != q4a(K2)
ok4 &= q4b(K1) != q4b(K2)
check("A4", ok4,
      f"COUNTERCONTROL AT QUARTIC ORDER. Both independent cubic invariants, sum k_i^4 and "
      f"sum_(i<j) k_i^2 k_j^2, are fixed by all {len(OH)} group elements, and neither is a function "
      f"of |k|^2: the unit vectors (1,0,0) and (3/5,4/5,0) have the same length while "
      f"sum k_i^4 reads {q4a(K1)} against {q4a(K2)}. So exact microscopic rotational symmetry is "
      f"neither assumed nor obtained, and `quartic_not_isotropic` exhibits that rather than the "
      f"corollary merely asserting it")

# ----------------------------------------------------------------- symbols
def cos_rem(x):
    """cos(x) - 1 + x^2/2, computed WITHOUT cancellation.

    Evaluating it as written loses every significant digit once |x| is small: the remainder is
    O(x^4) while the terms are O(1), so at x = 1e-4 the answer is below double precision and the
    measurement becomes noise rather than mathematics. For small |x| the series
    sum_(n>=2) (-1)^n x^(2n)/(2n)! has no cancellation and converges in a few terms; for large |x|
    the naive expression is dominated by x^2/2 and is accurate in relative terms."""
    if abs(x) < 3.0:
        term = x ** 4 / 24.0
        s = 0.0
        for n in range(2, 40):
            s += term
            term *= -(x * x) / ((2 * n + 1) * (2 * n + 2))
            if abs(term) < 1e-300:
                break
        return s
    return math.cos(x) - 1.0 + x * x / 2.0


def remainder(weights, k):
    """The symbol minus its quadratic Taylor polynomial at k = 0, summed term by term."""
    return math.fsum(w * cos_rem(sum(vi * ki for vi, ki in zip(v, k)))
                     for v, w in weights.items())


# ----------------------------------------------------------------- A5  clause (ii)
FINITE_RANGE = {}
for v in itertools.product((-1, 0, 1), repeat=3):
    if v != (0, 0, 0):
        FINITE_RANGE[v] = 1.0
FINITE_RANGE[(0, 0, 0)] = -26.0
ratios5 = []
for e in range(1, 9):
    t = 10.0 ** (-e)
    k = (t, t / 2, t / 3)
    n2 = sum(x ** 2 for x in k)
    ratios5.append(abs(remainder(FINITE_RANGE, k)) / n2 ** 2)
ok5 = max(ratios5) / min(ratios5) < 1.01         # bounded: the O(|k|^4) clause holds
ok5 &= all(r == r for r in ratios5)
check("A5", ok5,
      f"CLAUSE (ii) on a finite-range kernel — the 26 nearest neighbours of the simple cubic "
      f"lattice, which trivially has all moments. The remainder divided by |k|^4 stays in "
      f"[{min(ratios5):.4f}, {max(ratios5):.4f}] over eight decades of |k|, so the remainder really "
      f"is O(|k|^4). Finite range is the hypothesis the corollary names as sufficient")

# ----------------------------------------------------------------- A6  THE repair countercontrol
# A symmetric kernel with FINITE second moment and INFINITE fourth moment. With axis weights
# w(r) = r^-a and displacement r, the second moment is sum r^(2-a) and the fourth is sum r^(4-a),
# so a = 4 separates them: sum r^-2 converges, sum r^0 diverges. (An earlier draft used a = 6,
# which has a finite fourth moment too and so witnessed nothing -- the check caught it.)
RMAX = 200000
A_EXP = 4


def heavy_moment(power):
    """sum over the kernel of w(r) * r^power, with 6 axis directions at each radius."""
    return math.fsum(6.0 * r ** (-A_EXP) * r ** power for r in range(1, RMAX + 1))


m2 = heavy_moment(2)
m4 = heavy_moment(4)
ok6 = m2 < 100.0                                  # second moment converges (sum r^-2)
ok6 &= m4 > 0.5 * RMAX                            # fourth moment grows linearly with the cutoff


def heavy_remainder(t):
    """The remainder at k = (t, 0, 0). Only the two axis-0 displacements have nonzero phase."""
    return math.fsum(2.0 * r ** (-A_EXP) * cos_rem(r * t) for r in range(1, RMAX + 1))


r2, r4, ts = [], [], []
for e in (1, 2, 3):
    t = 10.0 ** (-e)
    n2 = t ** 2
    rem = abs(heavy_remainder(t))
    ts.append(t)
    r2.append(rem / n2)
    r4.append(rem / n2 ** 2)
ok6 &= r2[-1] < r2[0] / 50                        # clause (i) holds: remainder/|k|^2 -> 0
ok6 &= r4[-1] > 50 * r4[0]                        # clause (ii) fails: remainder/|k|^4 diverges
check("A6", ok6,
      f"THE COUNTERCONTROL THAT MOTIVATED THE MANUSCRIPT REPAIR. A symmetric kernel with axis "
      f"weights r^-{A_EXP} out to r = {RMAX} has second moment {m2:.4f} — the convergent sum of "
      f"r^-2 — and fourth moment {m4:.3e}, which is the divergent sum of r^0 and grows linearly "
      f"with the cutoff. On it the remainder divided by |k|^2 falls from {r2[0]:.3e} to "
      f"{r2[-1]:.3e}, so clause (i) holds; but divided by |k|^4 it RISES from {r4[0]:.3e} to "
      f"{r4[-1]:.3e}, growing like 1/|k|, so clause (ii) fails. Finite second moment therefore does "
      f"not give an O(|k|^4) remainder, which is exactly what the corollary used to claim and no "
      f"longer does")

# ----------------------------------------------------------------- A7  lint
src = open(os.path.join(BRIDGE, 'OIBridge', 'CubicIsotropy.lean'), encoding='utf-8').read()
root = open(os.path.join(BRIDGE, 'OIBridge.lean'), encoding='utf-8').read()
NAMES = ('ohInvariant_eq_scalar', 'ohInvariant_scalar', 'ohInvariant_iff', 'quadratic_isotropic',
         'quartic_ohInvariant', 'quartic_not_isotropic')
body = re.sub(r'(?m)--.*$', '', re.sub(r'/-.*?-/', '', src, flags=re.S))
ok7 = ('import OIBridge.CubicIsotropy' in root
       and re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', body) is None
       and re.search(r'(?m)^axiom ', body) is None
       and all(f'theorem {n}' in src for n in NAMES)
       and all(f'#print axioms {n}' in src for n in NAMES))
# the file must RECORD the two analytic clauses it does not prove
header = src[:src.index('import ')]
ok7 &= 'THE TWO CLAUSES ARE NOT INTERCHANGEABLE' in header
ok7 &= 'are NOT proved here' in src
ok7 &= 'coverage ledger records both as this entry' in src
# and the manuscript must carry the repaired, split statement
sm = open(os.path.join(HERE, os.pardir, os.pardir, 'papers', 'SM.md'), encoding='utf-8').read()
cor = sm[sm.index('**Corollary 1a (cubic symmetry FORBIDS quadratic anisotropy).**'):]
cor = cor[:cor.index('**Scope.**')]
ok7 &= 'o(|\\mathbf k|^2)' in cor                       # clause (i) has the honest remainder
ok7 &= 'finite second absolute moment' in cor
ok7 &= 'finite fourth absolute moment' in cor
ok7 &= 'need not be rotationally invariant' in cor
check("A7", ok7,
      f"the Lean file is IMPORTED BY OIBridge.lean, so CI builds it and the theorems are gated; it "
      f"carries no `sorry` and no `axiom`; all {len(NAMES)} named results print their axiom "
      f"dependencies; the header RECORDS the analytic bridge and the quartic refinement as clauses "
      f"it does not prove, so the algebraic core cannot stand in for the whole corollary; and the "
      f"manuscript now carries the split statement, with clause (i) at o(|k|^2) under a finite "
      f"second absolute moment and clause (ii) at O(|k|^4) under a finite fourth one")

print()
print('     [scope] Settled: the ALGEBRAIC CORE of [SM] Corollary 1a is kernel-proved — every')
print('     O_h-invariant symmetric form on R^3 is a multiple of delta, so no anisotropy survives')
print('     at quadratic order — together with the quartic countercontrol showing the surviving')
print('     invariants are not rotationally invariant. Both generator families of the group are')
print('     shown load-bearing: sign flips alone leave 3 dimensions, permutations alone 2.')
print('     NOT settled here, and recorded as this entry\'s ledger delta rather than glossed: the')
print('     ANALYTIC BRIDGE (finite second moment gives an o(|k|^2) remainder, by dominated')
print('     convergence against the second moment) and the QUARTIC REFINEMENT (finite fourth')
print('     moment sharpens it to O(|k|^4)). Both are checked numerically here, including the')
print('     kernel that motivated the manuscript repair: finite second moment, infinite fourth')
print('     moment, remainder/|k|^2 -> 0 but remainder/|k|^4 divergent.')
print()
print("cubic_isotropy_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
