"""P3 -- FiniteRank is not supplied once the carrier is infinite.  Exact arithmetic only.

The landed classical data types (Equiv.Perm S, vis : S -> Bool, a probability weight mu) with the Fintype instance
dropped: S = Z, phi(n) = n - 1 (a bijection), vis(n) = [n = 0], mu(n) = 1/((n+1)(n+2)) for n >= 0 and 0 otherwise.
A walker starting at T ~ mu reaches the visible site at step T and never returns, so the record of o^k is 0^k
exactly when T >= k.  Preparation x_k = (o^k, 0^k); effect e_m = (o^m, 0^m).
val(e_m, x_k) = P(T >= k+m) / P(T >= k) = (k+1)/(k+m+1), because P(T >= j) = 1/(j+1) (telescoping).
The matrix [val(e_m, x_k)] = diag(k+1) * Hilbert, which is nonsingular for every N (Cauchy determinant), so
x_0..x_{N-1} have linearly independent preparation vectors for every N: the completion has no finite rank.
"""
import sympy as sp

n, j = sp.symbols('n j', integer=True, nonnegative=True)
mu = 1 / ((n + 1) * (n + 2))
total = sp.summation(mu, (n, 0, sp.oo))
surv = sp.simplify(sp.summation(mu, (n, j, sp.oo)))
print('sum mu =', total, '; P(T >= j) =', surv)
assert total == 1 and sp.simplify(surv - 1 / (j + 1)) == 0

def val(k, m):
    return sp.Rational(k + 1, k + m + 1)

ranks = []
for N in range(1, 13):
    M = sp.Matrix(N, N, lambda k, m: val(k, m))
    ranks.append(M.rank())
print('rank of [val(e_m, x_k)]_{k,m<N}, N = 1..12:', ranks)
assert ranks == list(range(1, 13))
# Cauchy determinant of the Hilbert matrix, closed form, checked against direct determinants
def hilbert_det_closed(N):
    num = sp.Integer(1)
    den = sp.Integer(1)
    for i in range(N):
        for k in range(N):
            if i < k:
                num *= (k - i) ** 2
            den *= (i + k + 1)
    return num / den
for N in range(1, 9):
    H = sp.Matrix(N, N, lambda a, b: sp.Rational(1, a + b + 1))
    assert H.det() == hilbert_det_closed(N) != 0
print('Hilbert det = Cauchy closed form (nonzero) for N = 1..8: OK')
# BinaryVisible: the visible test (o,{0}),(o,{1}) sums to 1 on every x_k; a sharp pair exists
# P(vis = 1 at first step | x_k) = P(T = k | T >= k) = mu(k) * (k+1) = 1/(k+2)
print('P(first read = 1 | x_k), k = 0..5:', [sp.Rational(1, (k + 1) * (k + 2)) * (k + 1) for k in range(6)])
# sharp pair: after observing a 1 at step k the walker is at -1 forever -> reads 0 with certainty;
# no preparation reads 1 with certainty (P(T = k | T >= k) = 1/(k+2) < 1), so perfectlyDistinguishable_visible's
# hypothesis h1 fails on this tower, while the hypotheses of the tower itself hold.
print('OK -- FiniteRank fails on an infinite-carrier protocol tower over the landed data types')
