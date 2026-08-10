#!/usr/bin/env python3
"""b48 verification probes (2026-08-10): machine checks for the two foundational
corrections shipped in incompleteness-2026-08-10-p1-foundational.

Probe 1 — C3 corollary. The pre-correction Main §3.4 corollary asserted
"P-indivisibility across n visible configurations requires m >= n." A
three-visible-state, two-hidden-state bijection with uniform hidden prior
exhibits full distinguishability revival (TV distance 1 -> 0 -> 1) and is
P-indivisible under the corpus's own definition (no matrix L of any kind
satisfies T(1)·L = T(2), since rank T(1) = 2 < 3 = rank T(2) = rank I).
Hence m = 2 < 3 = n: the m >= n inference is refuted. The valid necessity is
the per-process capacity bound m >= 2^{I*} from the data-processing theorem.

Probe 2 — reverse dilation. A uniform-prior bijection marginal preserves the
uniform distribution, hence is doubly stochastic (verified exhaustively for
all 24 bijections on a 2x2 space). The rational row-stochastic matrix
[[1,0],[1,0]] is not doubly stochastic, so the pre-correction lemma statement
("any single one-step stochastic matrix ... exactly when rational") is false
as written; the statement's own Birkhoff-von-Neumann proof covers exactly the
doubly stochastic class, which is the correction shipped.

Both probes exit 0 iff the refutations reproduce.
"""
import itertools, fractions
F = fractions.Fraction

# --- Probe 1 ---
phi = {(0,0):(0,0), (0,1):(0,1), (1,0):(1,0), (1,1):(2,0), (2,0):(1,1), (2,1):(2,1)}
assert sorted(phi.values()) == sorted(phi.keys()), "not a bijection"

def Tk(k):
    T = [[F(0)]*3 for _ in range(3)]
    for v in range(3):
        for h in range(2):
            s = (v, h)
            for _ in range(k):
                s = phi[s]
            T[v][s[0]] += F(1, 2)
    return T

T1, T2 = Tk(1), Tk(2)
assert T1 == [[F(1),F(0),F(0)], [F(0),F(1,2),F(1,2)], [F(0),F(1,2),F(1,2)]]
assert T2 == [[F(1) if i == j else F(0) for j in range(3)] for i in range(3)], "T(2) != I"
# rank argument: rows 1,2 of T1 identical -> rank 2; I has rank 3 -> no L with T1·L = I
assert T1[1] == T1[2], "rows 1,2 of T(1) must coincide (rank drop)"
tv = lambda T: sum(abs(T[1][j] - T[2][j]) for j in range(3)) / 2
assert (tv(T1), tv(T2)) == (F(0), F(1)), "revival 0 -> 1 must occur between steps 1 and 2"
print("Probe 1 OK: P-indivisible (rank obstruction), full revival, m=2 < n=3 -> m>=n refuted")

# --- Probe 2 ---
states = [(v, h) for v in range(2) for h in range(2)]
for perm in itertools.permutations(states):
    mm = dict(zip(states, perm))
    T = [[sum(F(1,2) for h in range(2) if mm[(v,h)][0] == w) for w in range(2)] for v in range(2)]
    assert [sum(T[v][w] for v in range(2)) for w in range(2)] == [F(1), F(1)], \
        "uniform-prior bijection marginal must be doubly stochastic"
Tbad = [[F(1), F(0)], [F(1), F(0)]]
assert [sum(r[j] for r in Tbad) for j in range(2)] != [F(1), F(1)]
print("Probe 2 OK: all 24 bijection marginals doubly stochastic; [[1,0],[1,0]] excluded -> lemma-as-stated refuted")
print("b48 probes: PASS")
