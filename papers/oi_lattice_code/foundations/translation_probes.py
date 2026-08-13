#!/usr/bin/env python3
# translation_probes.py — b84 (2026-08-13)
# Two exact certifications supporting Main §2.3 and §3.1:
#  (A) P-divisibility => TV-monotonicity, but NOT conversely. Witnesses verified
#      exactly: a stochastic pair (T(1,0), T(2,0)) whose unique divisor
#      Lambda = T(1,0)^-1 T(2,0) has a negative entry (no stochastic divisor)
#      while d(p(t),q(t)) is non-increasing for EVERY pair p,q.
#  (B) the framework's own marginalized bijections realize doubly stochastic
#      one-step matrices that are NOT unistochastic (necessary direction of the
#      3x3 row-orthogonality criterion) — so the bare T = |U|^2 form cannot
#      cover the class and the ancilla-dilated form is required.
# Exact throughout (Fractions; sympy only for the sqrt triangle test).
import sys
from fractions import Fraction as F
from itertools import permutations
import sympy as sp

def inv(M, n):
    A = [r[:] + [F(1 if i == j else 0) for j in range(n)] for i, r in enumerate(M)]
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None: return None
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]; A[c] = [v / pv for v in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]; A[r] = [a - f * b for a, b in zip(A[r], A[c])]
    return [r[n:] for r in A]

def mm(A, B, n):
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def stochastic(M, n):
    return all(sum(M[i]) == 1 and all(x >= 0 for x in M[i]) for i in range(n))

def tv_monotone_all_pq(L, n):
    """d non-increasing for EVERY p,q  <=>  ||row_i(L) - row_j(L)||_1 <= 2 for all i<j
    (the extreme points of the zero-sum l1 ball are +-(delta_i - delta_j))."""
    return all(sum(abs(L[i][k] - L[j][k]) for k in range(n)) <= 2
               for i in range(n) for j in range(i + 1, n))

fail = 0

# ---- (A) the converse fails: exact witnesses -------------------------------
print("== (A) P-divisible => TV-monotone; the converse FAILS ==")
W = [
    ("n=2 (strict contraction)", 2,
     [[F(0), F(1)], [F(1, 2), F(1, 2)]],
     [[F(4, 5), F(1, 5)], [F(1), F(0)]]),
    ("n=3 (doubly stochastic; two directions saturate)", 3,
     [[F(2,7), F(2,7), F(3,7)], [F(4,7), F(5,14), F(1,14)], [F(1,7), F(5,14), F(1,2)]],
     [[F(5,14), F(2,7), F(5,14)], [F(2,7), F(5,14), F(5,14)], [F(5,14), F(5,14), F(2,7)]]),
]
for name, n, T1, T2 in W:
    assert stochastic(T1, n) and stochastic(T2, n), "witness must be a stochastic pair"
    Ti = inv(T1, n)
    assert Ti is not None, "T(1,0) must be invertible (divisor unique)"
    L = mm(Ti, T2, n)
    neg = min(L[i][j] for i in range(n) for j in range(n))
    mono = tv_monotone_all_pq(L, n)
    ok = (neg < 0) and mono
    print(f"  {name}: min Lambda = {neg}  no-stochastic-divisor={neg < 0}  TV-monotone(all p,q)={mono}  -> {'SEPARATION' if ok else 'FAIL'}")
    if not ok: fail += 1
# forward direction: any stochastic Lambda is TV-contractive (spot-certified)
for L in ([[F(1,3), F(2,3)], [F(3,4), F(1,4)]], [[F(1,2), F(1,4), F(1,4)], [F(0), F(1), F(0)], [F(1,3), F(1,3), F(1,3)]]):
    n = len(L)
    if not tv_monotone_all_pq(L, n): fail += 1; print("  FAIL: stochastic divisor not TV-contractive")
print("  forward direction (stochastic divisor => TV-contractive): certified on samples")

# ---- (B) realizable but non-unistochastic ---------------------------------
print("== (B) framework-realizable doubly stochastic matrices that are NOT unistochastic ==")
nV, nH = 3, 2
def marg(perm, k):
    N = nV * nH; p = list(range(N))
    for _ in range(k): p = [perm[x] for x in p]
    T = [[F(0)] * nV for _ in range(nV)]
    for i in range(nV):
        for h in range(nH): T[i][p[i * nH + h] // nH] += F(1, nH)
    return T
def unistochastic3_necessary(B):
    """row-orthogonality: three complex numbers of moduli sqrt(B_1k B_2k) must
    close a triangle. Violation => NOT unistochastic (necessary direction only)."""
    m = [sp.sqrt(sp.Rational(B[0][k]) * sp.Rational(B[1][k])) for k in range(3)]
    a, b, c = m
    return bool(sp.simplify(a <= b + c) and sp.simplify(b <= a + c) and sp.simplify(c <= a + b))
seen, nonuni = {}, []
for perm in permutations(range(nV * nH)):
    T = marg(perm, 1); key = tuple(tuple(r) for r in T)
    if key in seen: continue
    ds = all(sum(T[i][j] for i in range(nV)) == 1 for j in range(nV))
    seen[key] = ds
    if ds and not unistochastic3_necessary(T): nonuni.append(key)
print(f"  distinct one-step matrices: {len(seen)}; all doubly stochastic: {all(seen.values())}")
print(f"  doubly stochastic but NOT unistochastic: {len(nonuni)}")
if len(nonuni) == 0 or not all(seen.values()): fail += 1
else:
    print("  witness:", [[str(x) for x in r] for r in nonuni[0]])
print()
print("translation_probes:", "ALL CHECKS PASS" if fail == 0 else f"{fail} FAILURE(S)")
sys.exit(1 if fail else 0)
