"""P5 -- on an infinite carrier, a bijective substratum step need not induce a reversible operation on the body,
and adding the un-step to the menu can destroy FiniteRank.  Exact arithmetic only.

Omega = Z, phi(n) = n - 1 (bijective), vis(n) = [n = 0], mu(n) = 2^-(n+1) for n >= 0 (memoryless).
(i)  menu {o, i}: the body is the segment [A, D] (A = alive geometric walker, D = walker already past 0);
     FiniteRank holds (rank 2); the idle step W maps A -> A/2 + D/2, D -> D; any affine S with S o W = id on the body
     has S(A) = 2A - D, outside the body: no inverse datum exists, although phi is a bijection of Omega.
(ii) menu {o, i, u} with u = phi^-1: the preparations u^j give P(o^m reads 0^m) = min(1, 2^(j-m)); that matrix has
     full rank N for every N tested, so FiniteRank fails.
"""
from fractions import Fraction as F
import sympy as sp

half = F(1, 2)
# effect family e_m = (o^m, 0^m); a state is the function m -> P(e_m)
A = lambda m: half ** m          # alive geometric: P(T >= m) = 2^-m
D = lambda m: F(1)               # past the visible site: never reads 1
# W(A): with prob 1/2 T = 0 -> moves to -1 (D); else T-1 ~ geometric (A).  Check on e_m via the definition:
def WA(m):   # P(no 1 in m reads after one unobserved step) = sum_n mu(n) [n - 1 not in {0..m-1}]
    return sum(half ** (n + 1) for n in range(0, 200) if not (0 <= n - 1 <= m - 1)) + half ** 200
for m in range(0, 12):
    assert WA(m) == half * A(m) + half * D(m), m
print('(i) W(A) = A/2 + D/2 on effects e_0..e_11: exact')
M = sp.Matrix([[A(m) for m in range(8)], [D(m) for m in range(8)]])
print('(i) rank of {A, D} on e_0..e_7 =', M.rank(), '(affine dim 1: FiniteRank holds)')
# Undoes would force S affine on the segment with S(W A) = A, S(D) = D  =>  S(A) = 2A - D
SA = [2 * A(m) - D(m) for m in range(4)]
print('(i) forced S(A) on e_0..e_3 =', [str(x) for x in SA], '-> value on e_2 is', SA[2], '< 0: S(A) is not a state')
assert SA[2] < 0
# (ii) un-step in the menu
ranks = []
for N in range(1, 11):
    H = sp.Matrix(N, N, lambda j, m: sp.Integer(1) if m <= j else sp.Rational(1, 2 ** (m - j)))
    ranks.append(H.rank())
print('(ii) rank of [P_{u^j}(o^m reads 0^m)]_{j,m<N}, N = 1..10:', ranks)
assert ranks == list(range(1, 11))
print('OK')
