"""P4 — does closedness transfer from the factors, and what does the completion of a product tower give?

Usage: python3 -I p4_transfer.py <CompositeDimension.lean> <maxlen>

Decision rule (fixed before the first run): verdict TRANSFER-FAILS-EXACT iff all checks pass:
  4.1 a non-closed locally tomographic composite on two closed (compact) balls:
      Om' = SEP-slice  union  relint(jointStates).  Ingredients:
      a  pairVal a b idW = sum_mu a_mu b_mu (symbolic)                                     [X]
      b  idW is on the relative boundary of jointStates: the product of sharp effects at x and -x has
         value (1 - |x|^2)/4 = 0 on |x| = 1, and value 1/4 at the centre prodState 0 0          [X]
      c  idW is not separable: the singlet functional s = (w00 - w11 - w22 - w33)/4 equals (1 - x.y)/4 on
         every product (symbolic), and s(idW) = -1/2                                          [X]
      d  idW = lim_{t->0} ((1-t) idW + t prodState 0 0), the segment points lying in relint   [X] identity; [L]
  4.2 the completion of a product tower is the minimal body, which is closed and not cnot-invariant:
      f = w00 - w11 + w22 - w33 equals 1 - x1y1 + x2y2 - x3y3 >= 0 on products (symbolic) and f(phiW) = -2,
      phiW = cnot(prodState xplus z3)                                                          [X]
  4.3 prod_mem over a completed factor needs the joint closure (3/5 tower of AC): no reduced word of length
      <= maxlen in R_x, R_z (cos = 3/5) sends e_z to -e_z (exact enumeration), while some word of length
      <= maxlen sends e_z within squared distance 1/25 of -e_z                                 [X]; [P] AC N2.3
  4.4 reverse direction: the dictionary rho_of is a real-linear bijection W 3 -> Herm(4), so Q3 (preimage
      of the closed PSD cone) is closed                                                          [X]+[L]
Otherwise TRANSFER-CHECK-FAILED.
"""
import itertools
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp  # noqa: E402
from fractions import Fraction as Fr  # noqa: E402
from dlib import Checks, parse_tables, cnot_fun, prod_W, pairval, sharpVec, rho_of  # noqa: E402

C = Checks('P4 transfer')
tabs = parse_tables(sys.argv[1])
maxlen = int(sys.argv[2])

idW = sp.eye(4)
a = sp.Matrix(sp.symbols('a0:4'))
b = sp.Matrix(sp.symbols('b0:4'))
C.check('4.1a pairVal a b idW = sum a_mu b_mu', sp.expand(pairval(a, b, idW) - sum(a[i] * b[i] for i in range(4))) == 0)
x = sp.symbols('x1:4')
y = sp.symbols('y1:4')
v = pairval(sharpVec(list(x)), sharpVec([-t for t in x]), idW)
C.check('4.1b value of sharp(x) (x) sharp(-x) on idW is (1-|x|^2)/4; at the centre it is 1/4',
        sp.expand(v - (1 - sum(t * t for t in x)) / 4) == 0
        and pairval(sharpVec(list(x)), sharpVec([-t for t in x]), prod_W([0, 0, 0], [0, 0, 0])) == sp.Rational(1, 4))
s = lambda w: (w[0, 0] - w[1, 1] - w[2, 2] - w[3, 3]) / 4  # noqa: E731
C.check('4.1c singlet functional: (1 - x.y)/4 on products, -1/2 on idW',
        sp.expand(s(prod_W(list(x), list(y))) - (1 - sum(x[i] * y[i] for i in range(3))) / 4) == 0
        and s(idW) == sp.Rational(-1, 2))
C.note('[W] Lor a, b (a0 >= |a vec|) give a0 b0 + a.b >= 0 (Cauchy-Schwarz), so idW in maxCone; idW 0 0 = 1.')
t = sp.symbols('t')
seg = (1 - t) * idW + t * prod_W([0, 0, 0], [0, 0, 0])
C.check('4.1d segment from idW to the centre: entries affine in t, equal to idW at t = 0',
        seg.subs(t, 0) == idW and seg[0, 0] == 1)
C.note('[W]+[L] centre in relint(jointStates) (pairVal a b (e00 + delta) >= a0 b0 (1 - 2|delta|) on Lor pairs);')
C.note('    line-segment principle: (1-t) idW + t e00 in relint for t in (0,1].  So idW in cl(Om\') \\ Om\'.')
C.note('    Om\' is convex (segment principle), contains the products, lies in maxBody: a PreComposite; on the')
C.note('    coordinate model its lt field is modelData_ext (CompositeInterface.lean:740) -- a Composite on two')
C.note('    compact balls whose body is not closed.')

xplus, z3 = [1, 0, 0], [0, 0, 1]
phiW = cnot_fun(tabs, prod_W(xplus, z3))
f = lambda w: w[0, 0] - w[1, 1] + w[2, 2] - w[3, 3]  # noqa: E731
C.check('4.2 f = 1 - x1y1 + x2y2 - x3y3 on products, f(phiW) = -2',
        sp.expand(f(prod_W(list(x), list(y))) - (1 - x[0] * y[0] + x[1] * y[1] - x[2] * y[2])) == 0
        and f(phiW) == -2)
C.note('[W] completion of the product tower (preparations P_A x P_B, effects E_A x E_B, product table) is')
C.note('    cl conv prodState(chartBody_A x chartBody_B) = minBody of the completed factors: compact (bilinear')
C.note('    image of compacts, Caratheodory), closed, and by 4.2 not invariant under the gate.')

# 4.3 the 3/5 tower
c5, s5 = Fr(3, 5), Fr(4, 5)


def mat(rows):
    return tuple(tuple(r) for r in rows)


Rx = mat([[1, 0, 0], [0, c5, -s5], [0, s5, c5]])
Rz = mat([[c5, -s5, 0], [s5, c5, 0], [0, 0, 1]])


def T(M):
    return mat([[M[j][i] for j in range(3)] for i in range(3)])


def mul(A, B):
    return mat([[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)])


letters = {'x': Rx, 'X': T(Rx), 'z': Rz, 'Z': T(Rz)}
inv = {'x': 'X', 'X': 'x', 'z': 'Z', 'Z': 'z'}
frontier = [('', ((Fr(0),), (Fr(0),), (Fr(1),)))]  # store image of e_z as column
seen_anti = False
best = None
count = 0
level = [('', (Fr(0), Fr(0), Fr(1)))]
for L in range(1, maxlen + 1):
    nxt = []
    for w, vct in level:
        for l, M in letters.items():
            if w and inv[l] == w[-1]:
                continue
            nv = tuple(sum(M[i][k] * vct[k] for k in range(3)) for i in range(3))
            nxt.append((w + l, nv))
            count += 1
            if nv == (Fr(0), Fr(0), Fr(-1)):
                seen_anti = True
            d2 = nv[0] ** 2 + nv[1] ** 2 + (nv[2] + 1) ** 2
            if best is None or d2 < best[0]:
                best = (d2, w + l)
    level = nxt
C.check('4.3a no reduced word of length <= %d sends e_z to -e_z' % maxlen, not seen_anti, '%d words' % count)
C.check('4.3b some word sends e_z within squared distance 1/25 of -e_z', best[0] < Fr(1, 25),
        'best %s = %s (display %.5f)' % (best[1], best[0], float(best[0])))
u = sp.symbols('u1:4')
vv = sp.symbols('v1:4')
val43 = pairval(sharpVec([0, 0, -1]), sharpVec([0, 0, 1]), prod_W(list(u), list(vv)))
C.check('4.3c sharp(-e_z) (x) sharp(e_z) on prodState u v = (1 - u3)(1 + v3)/4 (= 1 on balls iff u = -e_z, v = e_z)',
        sp.expand(val43 - (1 - u[2]) * (1 + vv[2]) / 4) == 0)
C.note('[W] values <= 1 on products of balls; a convex combination equal to 1 forces every component to have')
C.note('    u = -e_z.  So prodState(-e_z, e_z) is in conv{prodState(W e_z, W\' e_z)} only if -e_z is in the orbit.')
C.note('[P] AC N2.1-N2.3: the group is free, so torsion-free, and a rotation sending e_z to -e_z is an involution;')
C.note('    so -e_z is never in the orbit, but is in its closure (density).  prodState(-e_z, e_z) is a pure')
C.note('    product (4.3c), hence absent from conv{prodState(W e_z, W\' e_z)}, present in its')
C.note('    closure: prod_mem over the completed factor ball holds for the closed hull only.')

# 4.4 reverse direction
basis = []
for m in range(4):
    for n in range(4):
        E = sp.zeros(4, 4)
        E[m, n] = 1
        R = rho_of(E)
        basis.append([sp.re(z) for z in R] + [sp.im(z) for z in R])
C.check('4.4 rho_of maps the 16 basis vectors of W 3 to R-independent Hermitian matrices', sp.Matrix(basis).rank() == 16
        and all(rho_of(sp.Matrix(4, 4, lambda i, j: 1 if (i, j) == (m, n) else 0)).is_hermitian
                for m in range(4) for n in range(4)))
C.note('[L] the PSD cone is closed; Q3 = rho_of^-1(PSD) is closed; QM states = closure of Gaussian-rational states.')

C.summary('TRANSFER-FAILS-EXACT', 'TRANSFER-CHECK-FAILED')
