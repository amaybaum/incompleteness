# Independent exact checks bearing on ch07:126 s2, ch18:148 (R12), ch07:137.
from fractions import Fraction as Fr
import math
# (1) Page's exact mean entanglement entropy for Haar pure states on C^m (x) C^n, m<=n:
#     S(m,n) = sum_{k=n+1}^{mn} 1/k - (m-1)/(2n)   [Page 1993]
def S_page(m, n):
    return sum(Fr(1, k) for k in range(n+1, m*n+1)) - Fr(m-1, 2*n)
for m in (2, 4, 8, 16, 32):
    s = S_page(m, m)
    print("m=n=%2d  S_Page-ln m = %+.10f   (large-dim form ln m - m/2n gives -0.5)" % (m, float(s) - math.log(m)))
# mean deficit at fixed m, growing n: ~ m/(2n): polynomial in the dimension n, not exponential
for n in (4, 16, 64, 256):
    print("m=4,n=%3d  ln m - S_Page = %.6f   m/(2n) = %.6f" % (n, math.log(4) - float(S_page(4, n)), 4/(2*n)))
# (2) Page-time fraction under dM/dt = -a M^{-p} / M^2, S_BH ~ M^2, beta = 1 (turnover at M0/sqrt 2):
#     M^{3+p} decreases linearly in t  =>  t_P/t_evap = 1 - 2^{-(3+p)/2}
for p in (Fr(0), Fr(1, 2), Fr(1)):
    print("p=%s  t_P/t_evap = %.8f" % (p, 1 - 2 ** (-(3 + float(p)) / 2)))
# (3) beta formula: t_P/t_evap = 1 - (beta/(1+beta))^{3/2}
for b in (Fr(1), Fr(4, 3), Fr(14847, 10000)):
    print("beta=%s  t_P/t_evap = %.6f" % (b, 1 - (float(b) / (1 + float(b))) ** 1.5))
