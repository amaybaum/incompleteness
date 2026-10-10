"""Coordinator pre-check for the EQ4 protocol (research only, base bcbc516f).  Exact; not evidence for the thread,
which must re-derive everything in its own code.  It checks the two claims the protocol will state as the
coordinator's expectations:
  T  (triangle / pigeonhole) for three mutually disjoint triples A, B, C pairwise joined by Bell links, an assignment
     of the cones {BS, BS*} has two triples with the same cone; (BS, BS) fails inclusion (I3) and (BS*, BS*) fails
     inclusion (II3), each with an exact negative six-copy value.
  C  (copy factorization) the CNOT Choi state on tokens (1,2,4,5), (CNOT_12 (x) 1)(Omega_14 (x) Omega_25), equals
     (V (x) id)(psi3) where V: |i> -> |i>|i> is the copy isometry onto tokens (1,4) and psi3 = sum_ij |i>|i+j>|j>
     on (x, 2, 5); the Choi state of V is |000> + |111>.  And the GHZ4-Choi map sends |Phi+>|+> to a GHZ state.
DECISION RULE: VERDICT `EQ4-PRECHECK-EXACT` iff every check passes.
"""
import itertools
import sys
from functools import reduce

import sympy as sp
from sympy import Matrix, Rational as R, eye, zeros

checks = []


def check(name, cond):
    checks.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + name)


def kron(*Ms):
    return reduce(sp.kronecker_product, Ms)


def proj(v):
    return (v * v.H).applyfunc(sp.expand)


B3 = list(itertools.product(range(2), repeat=3))


def i3(b):
    return 4 * b[0] + 2 * b[1] + b[2]


def val_bell_effects(X, Y):
    """tr[(Phi+_{a1 c1} Phi+_{a2 c2} Phi+_{a3 c3})(X_A (x) Y_C)] for normalized Phi+ on each link."""
    s = 0
    for a in B3:
        for b in B3:
            s += X[i3(b), i3(a)] * Y[i3(b), i3(a)]
    return sp.expand(s / 8)


def cond_bell_links(F):
    """Conditional on A of an effect F on C through normalized Phi+ links: F^T / 8."""
    return F.T / 8


ghz = proj(Matrix([1, 0, 0, 0, 0, 0, 0, 1]) / sp.sqrt(2)).applyfunc(sp.nsimplify)
w3 = R(1, 2) * eye(8) - ghz
v_bsbs = sp.expand((w3 * cond_bell_links(ghz)).trace())
v_bsstar = val_bell_effects(w3, ghz)
check("T1 (BS, BS): states of A conditioned through Bell links on the effect GHZ of C (GHZ in BS*), paired with the "
      "effect w3 = 1/2 - GHZ of A (in BS*): value %s < 0, so (I3) fails" % v_bsbs, v_bsbs < 0)
check("T2 (BS*, BS*): states w3 (in BS*) on A and GHZ (in BS*) on C, Bell effects on the three links: value %s < 0, "
      "so (II3) fails" % v_bsstar, v_bsstar < 0)
check("T3 w3 is not PSD (eigenvalue -1/2), GHZ is PSD: both lie in BS*, w3 is not in BS",
      R(-1, 2) in w3.eigenvals() and all(e >= 0 for e in ghz.eigenvals()))

# ------------------------------------------------------------------ C copy factorization (qubit order 1, 2, 4, 5)
CNOT = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])


def ket(bits):
    v = zeros(2 ** len(bits), 1)
    v[int("".join(map(str, bits)), 2)] = 1
    return v


# Omega_14 (x) Omega_25 in order (1, 2, 4, 5): sum_{a,b} |a b a b>
om = sum((ket([a, b, a, b]) for a in range(2) for b in range(2)), zeros(16, 1))
choi = kron(CNOT, eye(4)) * om
# psi3 on (x, 2, 5) and V copying x onto (1, 4): result in order (1, 2, 4, 5) = sum_ij |i, i+j, i, j>
psi3 = {(i, (i + j) % 2, j): 1 for i in range(2) for j in range(2)}
fact = zeros(16, 1)
for (x, t2, t5), c in psi3.items():
    fact += c * ket([x, t2, x, t5])
check("C1 CNOT Choi (CNOT_12 (x) 1)(Omega_14 Omega_25) = (V (x) id)(psi3), V the copy isometry onto (1,4), "
      "psi3 = sum_ij |i>|i+j>|j> on (x, 2, 5)", choi == fact)
V = zeros(4, 2)
V[0, 0] = 1
V[3, 1] = 1
choiV = kron(eye(2), V) * Matrix([1, 0, 0, 1])           # (1 (x) V)|Omega>, order (ref, out1, out2)
check("C2 the Choi vector of the copy isometry is |000> + |111> (unnormalized GHZ)",
      choiV == Matrix([1, 0, 0, 0, 0, 0, 0, 1]))
K = proj(ket([0, 0])) + proj(ket([1, 1]))                  # Kraus of the GHZ4-Choi map on two tokens
phi_plus = Matrix([1, 0, 0, 1])
state = kron(phi_plus, Matrix([1, 1]))                     # |Phi+>_01 |+>_2 (unnormalized), order (0, 1, 2)
out = kron(eye(2), K) * state
check("C3 the map with Kraus |00><00| + |11><11| on tokens (1,2) sends |Phi+>_01|+>_2 to |000> + |111>",
      out == Matrix([1, 0, 0, 0, 0, 0, 0, 1]))
print("--- eq4_precheck: %d/%d" % (sum(checks), len(checks)))
print("VERDICT EQ4-PRECHECK-EXACT" if all(checks) else "VERDICT NOT RENDERED")
