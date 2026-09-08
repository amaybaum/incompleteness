#!/usr/bin/env python3
"""Exact full-period witness for recurrence-horizon tightness (Target 3).

This probe implements one finite reversible RootedRealization with V={0,1},
H={0,1,2,3}, one fixed hidden prior, and a permutation of microscopic order 3.
It verifies the frozen T3-A target exactly in rational arithmetic:

  Gamma_0 = I,
  Gamma_1 = B_(7/10),
  Gamma_2 = B_(3/5),
  Gamma_3 = I,

with the full W/S/R1/R2 CausalReadback parent at w=s=1,t=2,
P-divisibility at every K<3, and failure at K=3.  The controlling
readback-return horizon N_CR is therefore exactly 3.
"""

from fractions import Fraction as Q

V = (0, 1)
H = (0, 1, 2, 3)

# One fixed hidden prior, shared by both visible roots.
MU = (Q(1, 2), Q(1, 5), Q(1, 10), Q(1, 5))

# States are indexed by 4*v+h.  The permutation is
#   (0,0) fixed, (1,0) fixed,
#   (0,1)->(0,2)->(1,1)->(0,1),
#   (0,3)->(1,3)->(1,2)->(0,3).
PHI = (0, 2, 5, 7, 4, 1, 3, 6)


def idx(v, h):
    return 4 * v + h


def unpack(i):
    return (i // 4, i % 4)


def step_state(state):
    v, h = state
    return unpack(PHI[idx(v, h)])


def iterate_state(state, t):
    out = state
    for _ in range(t):
        out = step_state(out)
    return out


def rooted_map(t):
    rows = []
    for a in V:
        row = [Q(0), Q(0)]
        for h, weight in zip(H, MU):
            j, _ = iterate_state((a, h), t)
            row[j] += weight
        rows.append(tuple(row))
    return tuple(rows)


def B(p):
    return ((p, 1 - p), (1 - p, p))


I = B(Q(1))
B7 = B(Q(7, 10))
B6 = B(Q(3, 5))
B34 = B(Q(3, 4))


def matmul(A, C):
    return tuple(
        tuple(sum(A[i][k] * C[k][j] for k in V) for j in V)
        for i in V
    )


def row_stochastic(A):
    return all(all(x >= 0 for x in row) and sum(row) == 1 for row in A)


def tv_rows(A):
    return sum(abs(A[0][j] - A[1][j]) for j in V) / 2


def conditional_hidden(root, t, visible_value):
    mass = {h: Q(0) for h in H}
    total = Q(0)
    for h0, weight in zip(H, MU):
        v, h = iterate_state((root, h0), t)
        if v == visible_value:
            mass[h] += weight
            total += weight
    assert total > 0
    return {h: q / total for h, q in mass.items() if q}


def propagate_hidden_law(visible_value, law, dt):
    out = [Q(0), Q(0)]
    for h, weight in law.items():
        v, _ = iterate_state((visible_value, h), dt)
        out[v] += weight
    return tuple(out)


checks = []

# 1. Microscopic reversibility and exact order 3.
checks.append(("permutation", sorted(PHI) == list(range(8))))
checks.append(("prior", sum(MU) == 1 and all(w > 0 for w in MU)))
checks.append(("phi^3=id", all(iterate_state(unpack(i), 3) == unpack(i) for i in range(8))))
checks.append(("order exactly 3", any(iterate_state(unpack(i), 1) != unpack(i) for i in range(8))))

# 2. Full rooted family through the recurrence horizon.
G = tuple(rooted_map(t) for t in range(4))
checks.append(("rooted family", G == (I, B7, B6, I)))
checks.append(("all rows stochastic", all(row_stochastic(A) for A in G)))
checks.append(("strict mixing before return", Q(1) > Q(7, 10) > Q(3, 5) > Q(1, 2)))
checks.append(("no earlier visible identity", G[1] != I and G[2] != I and G[3] == I))

# 3. Full CausalReadback witness at w=s=1, x=0, t=2.
# W: same positive-prior seed h=1 writes the root into different hidden states.
w0 = iterate_state((0, 1), 1)
w1 = iterate_state((1, 1), 1)
checks.append(("W", MU[1] > 0 and w0[1] != w1[1]))

# S: x=0 occurs under both roots at s=1 and the root-conditioned hidden laws differ.
cond0 = conditional_hidden(0, 1, 0)
cond1 = conditional_hidden(1, 1, 0)
checks.append(("S positive overlap", G[1][0][0] > 0 and G[1][1][0] > 0))
checks.append(("S hidden laws differ", cond0 != cond1))
checks.append(("S exact root-0 law", cond0 == {0: Q(5, 7), 2: Q(2, 7)}))
checks.append(("S exact root-1 law", cond1 == {1: Q(2, 3), 3: Q(1, 3)}))

# R1: hold the current visible state x=0 fixed and propagate the two hidden laws one more step.
read0 = propagate_hidden_law(0, cond0, 1)
read1 = propagate_hidden_law(0, cond1, 1)
checks.append(("R1", read0 == (Q(5, 7), Q(2, 7)) and read1 == (Q(2, 3), Q(1, 3)) and read0 != read1))

# R2: actual rooted rows differ at t=2.
checks.append(("R2", G[2][0] != G[2][1]))

# 4. N_CR is exactly 3: a storage witness exists at s=1, and the first later identity return is t=3.
checks.append(("N_CR=3", G[2] != I and G[3] == I))

# 5. P-divisibility on every shorter horizon K<3.
# 0->1 uses B_7/10, 0->2 uses B_3/5, and 1->2 uses B_3/4.
checks.append(("factor 0->1", matmul(G[0], B7) == G[1] and row_stochastic(B7)))
checks.append(("factor 0->2", matmul(G[0], B6) == G[2] and row_stochastic(B6)))
checks.append(("factor 1->2", matmul(G[1], B34) == G[2] and row_stochastic(B34)))
checks.append(("P-divisible for every K<3", all(ok for name, ok in checks if name.startswith("factor "))))

# 6. At K=3 TV revives from 1/5 to 1, so merged #538 implies P-indivisibility.
checks.append(("TV path", tuple(tv_rows(A) for A in G) == (Q(1), Q(2, 5), Q(1, 5), Q(1))))
checks.append(("C4r at (2,3)", tv_rows(G[2]) < tv_rows(G[3])))

# Independent exact factor obstruction on the final step: the unique inverse of B_3/5 is
# [[3,-2],[-2,3]], which is not row-stochastic.
B6_inv = ((Q(3), Q(-2)), (Q(-2), Q(3)))
checks.append(("inverse exact", matmul(B6, B6_inv) == I and matmul(B6_inv, B6) == I))
checks.append(("final factor not stochastic", not row_stochastic(B6_inv)))
checks.append(("P-indivisible at K=3", matmul(G[2], B6_inv) == G[3] and not row_stochastic(B6_inv)))

failed = [name for name, ok in checks if not ok]
for name, ok in checks:
    print(f"{'PASS' if ok else 'FAIL'}  {name}")

if failed:
    raise SystemExit("failed: " + ", ".join(failed))

print(f"ALL PASS ({len(checks)}/{len(checks)})")
print("T3-A: exact full-period tightness witness; N_CR = 3")
