#!/usr/bin/env python3
"""Exact within-window divisibility check for the T3 CausalReadback countermodel.

The companion discovery probe verifies that the finite reversible b51 realization
with rooted family I -> B_3/4 -> B_5/8 satisfies the frozen W/S/R parent on the
audited horizon K=2. This probe checks the additional decisive fact: that same
rooted family is P-divisible WITHIN K=2.

Therefore CausalReadback alone cannot imply P-indivisibility within the same
audited window, and no observable child that is both implied by CausalReadback
and sufficient for PIndivisibleWithin K can exist universally on that window.

This does NOT address the separate finite-recurrence/global-horizon route: a
finite reversible realization may later return its rooted map to the identity,
and that longer-horizon question is deliberately left outside this probe.
"""

from fractions import Fraction as F


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)]
            for i in range(2)]


def row_stochastic(M):
    return all(x >= 0 for row in M for x in row) and all(sum(row, F(0)) == 1 for row in M)


I = [[F(1), F(0)], [F(0), F(1)]]
B34 = [[F(3, 4), F(1, 4)], [F(1, 4), F(3, 4)]]
B58 = [[F(5, 8), F(3, 8)], [F(3, 8), F(5, 8)]]

assert row_stochastic(I)
assert row_stochastic(B34)
assert row_stochastic(B58)

# Every required factorization within K=2 has an explicit stochastic bridge.
assert mm(I, B34) == B34      # Gamma_1 = Gamma_0 * B34
assert mm(I, B58) == B58      # Gamma_2 = Gamma_0 * B58
assert mm(B34, B34) == B58    # Gamma_2 = Gamma_1 * B34

print("T3 window closure: I -> B_3/4 -> B_5/8 is exactly P-DIVISIBLE WITHIN K=2.")
print("Explicit bridge at 1->2: B_3/4; B_3/4 * B_3/4 = B_5/8.")
print("Therefore CausalReadback does NOT imply PIndivisibleWithin the same audited window.")
print("No same-window C4cr child can be both implied by CausalReadback and sufficient for P-indivisibility.")
print("Global finite-recurrence divisibility is a separate question, not decided here.")
