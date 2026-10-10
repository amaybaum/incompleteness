"""K2C P5 -- the ingredients of the cone-uniqueness argument and its countercontrols, exact.

Decision rule (fixed before running): each item is a separate exact check; the uniqueness ARGUMENT itself is written
([W]) and cites these checks plus literature facts ([L]: Schmidt decomposition, spectral theorem, max product
overlap = largest Schmidt coefficient, unitary orbits preserve spectra).  Verdict UNIQUENESS-INGREDIENTS-EXACT iff
every check passes.

  5.1  one cnot suffices: Schmidt states a|00>+b|11> are cnot images of pure products (symbolic), and a generic
       entangled pure state is actC R_A (actT R_B (cnot (prodState x z3))) (exact rational instance).
  5.2  upper bound (no strictly larger G-invariant set in maxCone): two exact instances of a point of maxCone \\ Q3
       mapped by an explicit word of G (cnot and rational rotations) to a point with a negative product-effect value.
  5.3  convexity is load-bearing: (I - P00)/3 is in Q3 and is not a positive multiple of any unitary image of a
       product state (spectral obstruction).
  5.4  reflections enlarge the group (P4: so(15)); the Hilbert-Schmidt ball cone B3 contains the products, is
       invariant under cnot and local O(3) on both copies, and is NOT inside maxCone (exact witness).
  5.5  the separable cone is invariant under local O(3) and not under cnot (exact witness -2).
  5.6  CP face tests: with the three pi-rotations, the landed chain evaluates all four Choi eigenvalues of a diagonal
       one-copy map (kernel-only chains; Choi spectrum [M]).

Usage: python -I p5_uniqueness.py <CompositeDimension.lean> <K2Guard.lean>
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k2clib import *  # noqa

CD, KG = sys.argv[1], sys.argv[2]
tabs = parse_tables(CD)
reflY = parse_diag_map(KG, 'reflY')
cn = lambda w: cnot_fun(tabs, w)
z3 = (0, 0, 1)
ket = lambda *c: sp.Matrix(c)

# 5.1 Schmidt via one cnot
t = sp.Symbol('t', real=True)
a, b = (1 - t ** 2) / (1 + t ** 2), 2 * t / (1 + t ** 2)
psi = ket(a, 0, 0, b)
xs = (2 * a * b, 0, a ** 2 - b ** 2)
check('5.1a q(|a00+b11><.|) = cnot (prodState (2ab, 0, a^2-b^2) z3), a = (1-t^2)/(1+t^2), b = 2t/(1+t^2)',
      sp.simplify(q_of(psi * psi.H) - cn(prod_W(xs, z3))) == sp.zeros(4, 4))
check('5.1b (2ab, 0, a^2-b^2) is a unit vector', sp.simplify(sum(s ** 2 for s in xs) - 1) == 0)
qA, qB = (1, 2, 0, -1), (2, -1, 1, 1)
nA, nB = sum(s ** 2 for s in qA), sum(s ** 2 for s in qB)
UA, UB = quat_U(qA), quat_U(qB)
RA, RB = quat_R(qA), quat_R(qB)
psi0 = ket(sp.Rational(3, 5), 0, 0, sp.Rational(4, 5))
psiE = kron(UA, UB) * psi0                     # norm^2 = nA nB
x0 = (sp.Rational(24, 25), 0, sp.Rational(-7, 25))
wpsi = sp.expand(q_of(psiE * psiE.H) / (nA * nB))
check('5.1c entangled instance: q(P_psi) = actC R_A (actT R_B (cnot (prodState (24/25,0,-7/25) z3))), rational R_A, R_B',
      wpsi == actC_fun(RA, actT_fun(RB, cn(prod_W(x0, z3)))))

# 5.2 upper bound instances
e00 = sharpVec(z3)
v00 = lambda w: pairval(e00, e00, w)            # prodEffVal (sharpEff z3) (sharpEff z3)
idW = sp.eye(4)
check('5.2a idW (in maxCone, not in Q3; P2.5d, P2.6c): cnot idW has value -1/2 on sharpEff(-e1) (x) sharpEff(-e3)',
      pairval(sharpVec((-1, 0, 0)), sharpVec((0, 0, -1)), cn(idW)) == sp.Rational(-1, 2))
alpha = sp.Rational(16, 25)
wX = alpha * 4 * sp.diag(1, 0, 0, 0) - wpsi          # q(alpha I - P_psi), using q(I) = 4 e00 (checked in 5.2b)
check('5.2b q(alpha I - P_psi) = 4 alpha e00 - q(P_psi)  (q(I) = 4 e00)', sp.expand(q_of(alpha * sp.eye(4)) - 4 * alpha * sp.diag(1, 0, 0, 0)) == sp.zeros(4, 4))
psin = psiE / sp.sqrt(nA * nB)
neg = sp.simplify((psin.H * rho_of(wX) * psin)[0, 0])
check('5.2c alpha I - P_psi (alpha = 16/25 = largest Schmidt coefficient^2) is not PSD: <psi|.|psi> = -9/25', neg == sp.Rational(-9, 25), neg)
Ry = sp.Matrix([[sp.Rational(-7, 25), 0, sp.Rational(-24, 25)], [0, 1, 0], [sp.Rational(24, 25), 0, sp.Rational(-7, 25)]])
check('5.2d R_y in SO(3) and R_y (24/25, 0, -7/25) = z3', Ry.T * Ry == sp.eye(3) and Ry.det() == 1 and Ry * sp.Matrix(x0) == sp.Matrix(z3))
g = lambda w: actC_fun(Ry, cn(actC_fun(RA.T, actT_fun(RB.T, w))))
gw = g(wX)
check('5.2e the word g = actC R_y . cnot . actC R_A^T . actT R_B^T maps P_psi to prodState z3 z3',
      sp.expand(g(wpsi) - prod_W(z3, z3)) == sp.zeros(4, 4))
check('5.2f value of g(alpha I - P_psi) on sharpEff z3 (x) sharpEff z3 = 16/25 - 1 = -9/25 (outside maxCone)',
      v00(gw) == sp.Rational(-9, 25), v00(gw))
# block positivity of alpha I - P_psi on product effects: instances (the general fact is [L])
ok = True
for xx in [(0, 0, 1), (0, 0, -1), (1, 0, 0), (sp.Rational(3, 5), sp.Rational(4, 5), 0), (0, sp.Rational(-3, 5), sp.Rational(4, 5))]:
    for yy in [(0, 0, 1), (0, 1, 0), (sp.Rational(-4, 5), 0, sp.Rational(3, 5)), (sp.Rational(2, 3), sp.Rational(2, 3), sp.Rational(1, 3))]:
        ok = ok and pairval(sharpVec(xx), sharpVec(yy), wX) >= 0
check('5.2g alpha I - P_psi nonnegative on 20 sharp product effects (instances; block-positivity is [L])', ok)

# 5.3 convexity is load-bearing
P00 = sp.diag(1, 0, 0, 0)
r3 = (sp.eye(4) - P00) / 3
w3 = q_of(r3)
good, _ = is_psd_exact(S_of(w3))
check('5.3a (I - P00)/3 in Q3 with spectrum {1/3,1/3,1/3,0} (exactly one zero)', good and r3.eigenvals() == {sp.Rational(1, 3): 3, 0: 1})
aa, bb, s = sp.symbols('aa bb s', real=True)
spec = [s * (1 + aa) * (1 + bb) / 4, s * (1 + aa) * (1 - bb) / 4, s * (1 - aa) * (1 + bb) / 4, s * (1 - aa) * (1 - bb) / 4]
two = (spec[2].subs(aa, 1) == 0 and spec[3].subs(aa, 1) == 0 and spec[1].subs(bb, 1) == 0 and spec[3].subs(bb, 1) == 0)
check('5.3b scaled product spectra s(1+-|x|)(1+-|y|)/4: a zero forces |x| = 1 or |y| = 1, which forces two zeros', two)
sx = sp.symbols('x1:4', real=True)
sy = sp.symbols('y1:4', real=True)
rx = (I2 + sx[0] * SX + sx[1] * SY + sx[2] * SZ) / 2
check('5.3c product spectrum: charpoly rho(x) roots (1 +- |x|)/2 (so rho(x) (x) rho(y) has the spectrum above) [L Kronecker]',
      sp.expand(rx.charpoly(sp.Symbol('l')).as_expr() - (sp.Symbol('l') ** 2 - sp.Symbol('l') + (1 - sum(c ** 2 for c in sx)) / 4)) == 0)

# 5.4 the Hilbert-Schmidt ball cone B3 (invariant under cnot and local O(3); not a candidate)
om = omega_symbols()
nrm = lambda w: sp.expand(sum(w[i, j] ** 2 for i in range(4) for j in range(4)) - w[0, 0] ** 2)
check('5.4a nrm(prodState x y) = |x|^2 + |y|^2 + |x|^2|y|^2  (<= 3 on the ball, = 3 on pure products)',
      sp.expand(nrm(prod_W(sx, sy)) - (sum(c ** 2 for c in sx) + sum(c ** 2 for c in sy) + sum(c ** 2 for c in sx) * sum(c ** 2 for c in sy))) == 0)
check('5.4b cnot fixes w00 and preserves nrm (signed permutation)', cn(om)[0, 0] == om[0, 0] and sp.expand(nrm(cn(om)) - nrm(om)) == 0)
qs = sp.symbols('q0:4', real=True)
R = quat_R(qs)
check('5.4c actT (+-R(q)) and actC (+-R(q)) preserve w00 and nrm (all of O(3), symbolic)',
      all(sp.simplify(nrm(f(M, om)) - nrm(om)) == 0 and f(M, om)[0, 0] == om[0, 0]
          for f in (actT_fun, actC_fun) for M in (R, -R)))
wB = 2 * sp.diag(1, 0, 0, 0) - prod_W(z3, z3)
check('5.4d w = 2 e00 - prodState z3 z3 (= q(I/2 - P00)) has w00 = 1, nrm = 3 (in B3) and value -1/2 on sharpEff z3 (x) sharpEff z3',
      wB[0, 0] == 1 and nrm(wB) == 3 and v00(wB) == sp.Rational(-1, 2))

# 5.5 separable cone: local O(3) yes (P1.6c/d), cnot no
f = lambda w: w[0, 0] - w[1, 1] + w[2, 2] - w[3, 3]
check('5.5 the separable witness f is -2 on cnot (prodState xplus z3)', f(cn(prod_W((1, 0, 0), z3))) == -2)

# 5.6 CP face tests
p0 = prod_W((1, 0, 0), z3)
val = lambda w: pairval(sharpVec((-1, 0, 0)), sharpVec((0, 0, -1)), w)
d = sp.symbols('d1:4', real=True)
D = sp.diag(*d)
choi = rho_of(actT_fun(D, cn(p0)))
evs = set(sp.expand(e) for e in choi.eigenvals().keys())
flips = [sp.eye(3), sp.diag(1, -1, -1), sp.diag(-1, 1, -1), sp.diag(-1, -1, 1)]
vals = set(sp.expand(val(cn(actT_fun(D * F, cn(p0))))) for F in flips)
check('5.6a the chains cnot . actT (D . F) . cnot on p0, F in {id, pi-rotations}, give exactly the four Choi eigenvalues of D',
      vals == evs and len(vals) == 4, sorted(vals, key=str))
nflip = parse_diag_map(CD, 'nflip')
check('5.6b the pi-rotation diag(1,-1,-1) is the kernel nflip; all three F are in SO(3)', flips[1] == nflip and all(F.det() == 1 for F in flips))

nf = summary()
print('VERDICT P5:', 'UNIQUENESS-INGREDIENTS-EXACT' if nf == 0 else 'NOT RENDERED')
sys.exit(nf)
