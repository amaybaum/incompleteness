"""Assumption-watch check for (EM): the compressed channel K = P U P iterated is not the compression
of the iterated dynamics P U^n P. Exact. State space Z_N with phi(z) = z+1 (a permutation, as every
exact substratum step is); coarse variable sigma(z) = [z == 0]; P = conditional expectation onto
functions of sigma under the uniform measure; U = Koopman operator (Uf)(z) = f(phi(z)).
Both operators are written in the basis {1_{sigma=1}, 1_{sigma=0}} of the coarse algebra.
"""
from fractions import Fraction as Fr

def run(N, nmax):
    cls = [1 if z == 0 else 0 for z in range(N)]
    size = {1: 1, 0: N - 1}
    def compress(n):
        # matrix of P U^n restricted to coarse functions: (P U^n 1_B)(A) = mu(A and phi^-n... ) / mu(A)
        M = {}
        for A in (1, 0):
            for B in (1, 0):
                cnt = sum(1 for z in range(N) if cls[z] == A and cls[(z + n) % N] == B)
                M[(A, B)] = Fr(cnt, size[A])
        return [[M[(1, 1)], M[(1, 0)]], [M[(0, 1)], M[(0, 0)]]]
    def mm(X, Y):
        return [[sum(X[i][k] * Y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    K = compress(1)
    Kn = [[Fr(1), Fr(0)], [Fr(0), Fr(1)]]
    rows = []
    for n in range(1, nmax + 1):
        Kn = mm(Kn, K)
        rows.append((n, compress(n), Kn))
    return K, rows

K, rows = run(5, 5)
print('N = 5, K = P U P =', [[str(v) for v in r] for r in K])
diff = False
for n, PUnP, Kn in rows:
    print(f' n={n}: P U^n P = {[[str(v) for v in r] for r in PUnP]}   K^n = {[[str(v) for v in r] for r in Kn]}')
    diff |= PUnP != Kn
print('P U^n P differs from (P U P)^n for some n <= N:', diff)
print('at n = N: P U^N P is the identity (exact recurrence) while K^N is not:',
      rows[-1][1] == [[1, 0], [0, 1]] and rows[-1][2] != [[1, 0], [0, 1]])
