"""probe2c: exact defects at Gaussian-rational non-torsion points, with Fraction arithmetic."""
import sys, time, itertools
from fractions import Fraction as Fr
from sympy import QQ
from sympy.polys.matrices import DomainMatrix
class G:  # Gaussian rational
    __slots__ = ('a', 'b')
    def __init__(s, a, b=0): s.a = Fr(a); s.b = Fr(b)
    def __mul__(s, o): return G(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a)
    def conj(s): return G(s.a, -s.b)
    def __neg__(s): return G(-s.a, -s.b)
def F4g(z):
    one, m = G(1), G(-1)
    return [[one, one, one, one], [one, z, m, -z], [one, m, one, m], [one, -z, m, z]]  # times 1/2, dropped (scale-free rank)
def defect_exact_g(H):
    n = len(H); rows = []
    for i in range(n):
        for j in range(i + 1, n):
            re = [Fr(0)] * (n * n); im = [Fr(0)] * (n * n)
            for k in range(n):
                c = H[i][k] * H[j][k].conj()
                re[i * n + k] += c.a; re[j * n + k] -= c.a; im[i * n + k] += c.b; im[j * n + k] -= c.b
            rows.append(re); rows.append(im)
    M = DomainMatrix([[QQ(x.numerator, x.denominator) for x in r] for r in rows], (len(rows), n * n), QQ)
    return n * n - M.rank() - (2 * n - 1)
z = G(Fr(3, 5), Fr(4, 5)); w = G(Fr(5, 13), Fr(12, 13))
X, Y = F4g(z), F4g(w)
t0 = time.time()
H = [[X[i // 4][j // 4] * Y[i % 4][j % 4] for j in range(16)] for i in range(16)]
print('exact defect at the Σ point z=(3+4i)/5, w=(5+12i)/13: %d (%.0fs)' % (defect_exact_g(H), time.time() - t0))
ph = [G(Fr(3, 5), Fr(4, 5)), G(Fr(5, 13), Fr(12, 13)), G(Fr(8, 17), Fr(15, 17)), G(Fr(7, 25), Fr(24, 25)), G(Fr(20, 29), Fr(21, 29)), G(Fr(12, 37), Fr(35, 37)), G(Fr(9, 41), Fr(40, 41)), G(Fr(28, 53), Fr(45, 53)), G(Fr(11, 61), Fr(60, 61))]
D = [[G(1)] * 4 for _ in range(4)]; k = 0
for c in range(1, 4):
    for b in range(1, 4):
        D[c][b] = ph[k]; k += 1
Hd = [[X[i // 4][j // 4] * D[j // 4][i % 4] * Y[i % 4][j % 4] for j in range(16)] for i in range(16)]
print('exact defect at a Diţă point with nine distinct rational twist phases: %d (%.0fs)' % (defect_exact_g(Hd), time.time() - t0))
# four distinct Ys as well
Ys = [F4g(G(Fr(3, 5), Fr(4, 5))), F4g(G(Fr(5, 13), Fr(12, 13))), F4g(G(Fr(8, 17), Fr(15, 17))), F4g(G(Fr(7, 25), Fr(24, 25)))]
Hd2 = [[X[i // 4][j // 4] * D[j // 4][i % 4] * Ys[j // 4][i % 4][j % 4] for j in range(16)] for i in range(16)]
print('exact defect at a Diţă point with four distinct Y_c and nine twist phases: %d (%.0fs)' % (defect_exact_g(Hd2), time.time() - t0))
