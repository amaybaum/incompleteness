"""Controls K1-K4, K6 of PREREGISTRATION.txt.  python3 -I -B controls.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from oi_exact import divisor, div2_closed_form, tv_monotone_all, tv_monotone_roots, identity, matmul
from families import swap22
import itertools, random

ok = True
def check(name, cond):
    global ok
    print(('GREEN ' if cond else 'RED   ') + name)
    ok = ok and cond

I2 = identity(2); J2 = [[F(1, 2)] * 2 for _ in range(2)]
# K1 swap: Gamma_1 = J/2, Gamma_2 = I
M = swap22()
check('K1 swap(2,2): Gamma_1 = J/2, Gamma_2 = I, r = 2', M.Gamma(1) == J2 and M.Gamma(2) == I2 and M.r == 2)
d, cert = divisor(M.Gamma(1), M.Gamma(2))
check('K1 swap(2,2): R1 fails on {0,1,2} with exact Farkas vector ' + str([str(v) for v in cert]), d is False)
# K2
check('K2 (J/2, I) infeasible', divisor(J2, I2)[0] is False)
X = [[F(1, 3), F(2, 3)], [F(3, 4), F(1, 4)]]
check('K2 (I, X) feasible', divisor(I2, X)[0] is True)
# K3 invertible with negative unique divisor
Gs = [[F(3, 4), F(1, 4)], [F(1, 4), F(3, 4)]]
check('K3 (Gs invertible, Gt = I): unique divisor Gs^-1 has negative entries -> infeasible', divisor(Gs, I2)[0] is False)
Q = [[F(2, 3), F(1, 3)], [F(0), F(1)]]
check('K3 (Gs, Gs Q) feasible', divisor(Gs, matmul(Gs, Q))[0] is True)
# 3x3 versions
C = [[F(int((i + 1) % 3 == j)) for j in range(3)] for i in range(3)]
C2 = matmul(C, C)
G1 = [[(C[i][j] + C2[i][j]) / 2 for j in range(3)] for i in range(3)]
check('K3 3x3: Gamma=(C+C^2)/2 -> I infeasible', divisor(G1, identity(3))[0] is False)
check('K3 3x3: Gamma=(C+C^2)/2 -> itself feasible (Lambda=I)', divisor(G1, G1)[0] is True)
# K4: closed form vs LP on random rational 2x2 pairs plus structured ones
random.seed(1)
vals = [F(a, 6) for a in range(7)]
agree = True; cnt = 0
for a, b, c, e in itertools.product(vals, repeat=4):
    Gs_ = [[a, 1 - a], [b, 1 - b]]; Gt_ = [[c, 1 - c], [e, 1 - e]]
    lp = divisor(Gs_, Gt_)[0]; cf = div2_closed_form(Gs_, Gt_)
    cnt += 1
    if lp != cf:
        agree = False; print('  disagree', Gs_, Gt_, lp, cf); break
check(f'K4 nV=2 LP == closed form on all {cnt} pairs with entries in (1/6)Z', agree)
# K6 TV checker
check('K6 (I, J/2, I) flagged non-monotone (all p,q)', tv_monotone_all([I2, J2, I2])[0] is False)
check('K6 (I, J/2, I) flagged non-monotone (roots)', tv_monotone_roots([I2, J2, I2])[0] is False)
check('K6 (I, J/2, J/2) monotone', tv_monotone_all([I2, J2, J2])[0] is True)
I3 = identity(3)
check('K6 3x3 (I, (C+C^2)/2, I) non-monotone', tv_monotone_all([I3, G1, I3])[0] is False)
check('K6 3x3 (I, (C+C^2)/2, (C+C^2)/2) monotone', tv_monotone_all([I3, G1, G1])[0] is True)
# a 3x3 case where roots-monotone holds but all-(p,q) fails would be a sharper control; search small grid
found = None
grid = [F(a, 4) for a in range(5)]
rows = [r for r in itertools.product(grid, repeat=3) if sum(r) == 1]
random.seed(7)
for _ in range(20000):
    A = [list(random.choice(rows)) for _ in range(3)]
    B = [list(random.choice(rows)) for _ in range(3)]
    if tv_monotone_roots([I3, A, B])[0] and not tv_monotone_all([I3, A, B])[0]:
        found = (A, B); break
print('  info: root-monotone but not all-(p,q)-monotone 3x3 example:', found is not None)
print('ALL CONTROLS GREEN' if ok else 'SOME CONTROL RED -- verdicts void')
sys.exit(0 if ok else 1)
