"""probe2b: exact defects at Gaussian-rational non-torsion points: z = (3+4i)/5, w = (5+12i)/13 on Σ,
and a Diţă point with rational unit phases; integer-scaled exact rank over QQ."""
import numpy as np, sys, time, sympy
sys.path.insert(0, '.')
from lib35 import *
from sympy import QQ, I, Rational, Matrix
from sympy.polys.matrices import DomainMatrix
def F4s(z):
    return Matrix([[1, 1, 1, 1], [1, z, -1, -z], [1, -1, 1, -1], [1, -z, -1, z]]) / 2
def kron_s(X, Y):
    n = X.shape[0]; m = Y.shape[0]
    return Matrix(n * m, n * m, lambda i, j: X[i // m, j // m] * Y[i % m, j % m])
def defect_exact_sym(H):
    n = H.shape[0]
    rows = []
    for i in range(n):
        for j in range(i + 1, n):
            c = [H[i, k] * H[j, k].conjugate() for k in range(n)]
            re = [0] * (n * n); im = [0] * (n * n)
            for k in range(n):
                cc = c[k].expand()
                r_, i_ = cc.as_real_imag()
                re[i * n + k] += r_; re[j * n + k] -= r_
                im[i * n + k] += i_; im[j * n + k] -= i_
            rows.append(re); rows.append(im)
    M = DomainMatrix([[QQ.from_sympy(sympy.nsimplify(x)) for x in r] for r in rows], (len(rows), n * n), QQ)
    return n * n - M.rank() - (2 * n - 1)
t0 = time.time()
z = (3 + 4 * I) / 5; w = (5 + 12 * I) / 13
H = kron_s(F4s(z), F4s(w))
print('exact defect at Σ point z=(3+4i)/5, w=(5+12i)/13:', defect_exact_sym(H), '(%.0fs)' % (time.time() - t0))
# Diţă point with rational phases: D[c,b] from the unit Gaussian rationals (3+4i)/5, (5+12i)/13, (8+15i)/17, (7+24i)/25
ph = [(3 + 4 * I) / 5, (5 + 12 * I) / 13, (8 + 15 * I) / 17, (7 + 24 * I) / 25, (20 + 21 * I) / 29, (12 + 35 * I) / 37, (9 + 40 * I) / 41, (28 + 45 * I) / 53, (11 + 60 * I) / 61]
D = [[1] * 4 for _ in range(4)]
k = 0
for c in range(1, 4):
    for b in range(1, 4):
        D[c][b] = ph[k]; k += 1
X = F4s(z); Y = F4s(w)
Hd = Matrix(16, 16, lambda i, j: X[i // 4, j // 4] * D[j // 4][i % 4] * Y[i % 4, j % 4])
print('exact defect at a Diţă point with nine distinct rational twist phases:', defect_exact_sym(Hd), '(%.0fs)' % (time.time() - t0))
