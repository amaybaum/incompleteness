# c7_circle.py -- research/countermodels node C7 (round 2), prediction 5 of NOTES-C7 S0: the full-circle Bell surgery.
# DECISION RULE (fixed before the first run, 2026-10-10T23:02Z by date -u):
#  Exact arithmetic (sympy Rational, exact Gaussian rationals; guard EX: no Float). Abstract orthonormal coordinates
#  (e0, e1, e2, e3) are identified with (psi_1, psi_2, psi_3, psi_4) of c2_structure.py; W = span(psi_1, psi_3),
#  Pperp = P_{psi_2} + P_{psi_4}, sz = P_{psi_1} - P_{psi_3}, sx = psi_1 psi_3^dag + psi_3 psi_1^dag.
#  Z_circ = {d_g = I - 2 g g^dag : g = cos(th) psi_1 + sin(th) psi_3} (a full Bell circle); d_g = Pperp - n.(sz, sx) with
#  n = (cos 2th, sin 2th); cone Z_circ = {t Pperp - a sz - b sx : t >= |(a, b)|}; Z_circ* = {y : tr(y Pperp) >=
#  |(tr(y sz), tr(y sx))|}; K(Z_circ)* contains (Q3 + cone Z_circ) n Z_circ*.
#  The two tables y1, y2 below were found by a numerical search in the scratchpad (minimizing <y1, y2> over pairs in
#  K(Z_circ)*; not evidence), rounded to rationals: y_i = v_i v_i^dag + t_i (Pperp - n_i.(sz, sx)) + I/1000 with n_i a
#  rational point of the unit circle. Checks:
#  B1 every g on the circle is maximally entangled (reduced state I/2, symbolic in th); (I_W + n.sigma)/2 is a rank-one
#      projector for |n| = 1 (so t (Pperp - n.sigma) = t d_g with g on the circle, a member of cone Z_circ).
#  B2 |n_i|^2 = 1 exactly; t_i >= 0; v_i v_i^dag and I/1000 PSD (so y_i in Q3 + cone Z_circ).
#  B3 y_i in Z_circ*: tr(y_i Pperp) > 0 and tr(y_i Pperp)^2 - tr(y_i sz)^2 - tr(y_i sx)^2 > 0 (exact).
#  B4 tr(y1 y2) < 0.  Then K(Z_circ)* is not self-positive, so K(Z_circ) is not self-dual ([W] NOTES-C7 W5).
#  B5 transfer: U with U psi_1 = b+, U psi_3 = -i b-, U psi_2 = |0+>, U psi_4 = |1-> -- b+- = (|0-> +- |1+>)/sqrt2 -- is
#      unitary and maps cos(th) psi_1 + sin(th) psi_3 to cos(th) b+ - i sin(th) b-, which equals, up to the phase
#      e^{i phi/2}, C2(e^{i phi}) = (|0-> + e^{i phi} |1+>)/sqrt2 with phi = 2 th (symbolic in th); and the gate flow
#      U(x) = I + (x - 1)|1-><1-| fixes every C2(w) (symbolic). So K(Z_C2) = Ad(U) K(Z_circ) is also not self-dual.
#  CC1 countercontrol: Q3 is self-dual, so its dual is self-positive; y1, y2 are not both PSD (exact: the 2x2 compression
#      of one of them to W has negative determinant), as a cone with self-positive dual could not contain them both.
#  CC2 countercontrol: without the shift I/1000 the pair still pairs negatively but B3 may be tight; recorded only.
#  VERDICT C7-CIRCLE-EXACT iff B1-B5, CC1 and EX pass; text generated from the measurements.
import sympy as sp
from sympy import Matrix, Rational as Q, I, eye, zeros, sqrt, expand, conjugate, cos, sin, symbols, kronecker_product as kron

R_ = []
def rec(kind, cid, ok, text, detail=""):
    ok = bool(ok); R_.append(ok)
    print(f"{kind} {cid:<4} {'PASS' if ok else 'FAIL'} {text}" + (f" -- {detail}" if detail else ""))

I2 = eye(2); SXp = Matrix([[0, 1], [1, 0]]); SYp = Matrix([[0, -I], [I, 0]]); SZp = Matrix([[1, 0], [0, -1]])
SG = [I2, SXp, SYp, SZp]; KR = {(m, n): kron(SG[m], SG[n]) for m in range(4) for n in range(4)}
def pauliW(w): return sum((w[m, n] * KR[(m, n)] for m in range(4) for n in range(4) if w[m, n] != 0), zeros(4, 4)) / 4
def E(m, n): B = zeros(4, 4); B[m, n] = 1; return B
def zdef(s1, s2): return (E(0, 0) + s1 * E(1, 3) + s2 * E(2, 2) - s1 * s2 * E(3, 1)) / 4
SS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def negvec(w):
    v = (pauliW(w) + eye(4) / 8).nullspace()[0]; return v / sqrt(expand((v.H * v)[0]))
PSI = [sp.simplify(negvec(zdef(*s))) for s in SS]
PsiM = Matrix.hstack(*PSI)
def red_A(g):
    rho = g * g.H; return Matrix(2, 2, lambda i, j: sum(rho[2 * i + k, 2 * j + k] for k in range(2)))

th = symbols('th', real=True)
gth = cos(th) * PSI[0] + sin(th) * PSI[2]
b1 = sp.simplify(red_A(gth) - eye(2) / 2) == zeros(2, 2)
nz, nx = symbols('nz nx', real=True)
Pn = (sp.diag(1, 0, 1, 0) + nz * sp.diag(1, 0, -1, 0) + nx * (E(0, 2) + E(2, 0))) / 2
proj = sp.expand(Pn * Pn - Pn).subs(nx ** 2, 1 - nz ** 2)
b1 = b1 and sp.simplify(proj) == zeros(4, 4) and sp.simplify(Pn.trace()) == 1
rec("CHECK", "B1", b1, "cos(th) psi_1 + sin(th) psi_3 maximally entangled for all th; (I_W + n.sigma)/2 a rank-one projector when |n| = 1")

Pperp = sp.diag(0, 1, 0, 1); Sz = sp.diag(1, 0, -1, 0); Sx = E(0, 2) + E(2, 0)
data = [
    ([Q(39, 100), Q(41, 125) - 47 * I / 1000, Q(61, 125), Q(53, 1000) - 173 * I / 500], Q(189, 1000),
     (Q(-15088121, 17088121), Q(-8022000, 17088121))),
    ([Q(53, 1000), Q(41, 125) - 47 * I / 1000, Q(-311, 500), Q(53, 1000) - 173 * I / 500], Q(189, 1000),
     (Q(10971, 114029), Q(113500, 114029))),
]
ys = []; okB2 = True; okB3 = True; marg = []
for v, t, (a_, b_) in data:
    vv = Matrix(v)
    y = vv * vv.H + t * (Pperp - a_ * Sz - b_ * Sx) + eye(4) / 1000
    ys.append(y)
    okB2 = okB2 and (a_ ** 2 + b_ ** 2 == 1) and t >= 0
    yP = expand((y * Pperp).trace()); yz = expand((y * Sz).trace()); yx = expand((y * Sx).trace())
    m2 = expand(yP ** 2 - yz ** 2 - yx ** 2)
    marg.append(m2)
    okB3 = okB3 and yP > 0 and m2 > 0
rec("CHECK", "B2", okB2, "|n_i| = 1 exactly, t_i = 189/1000 >= 0; y_i = v v^dag + t_i d_{g_i} + I/1000 in Q3 + cone Z_circ")
rec("CHECK", "B3", okB3, "y_1, y_2 in Z_circ* strictly (tr(y Pperp)^2 - |(tr y sz, tr y sx)|^2 > 0)", "margins^2 %s" % [sp.nsimplify(m) for m in marg])
p12 = expand((ys[0] * ys[1]).trace())
rec("CHECK", "B4", p12 < 0, "tr(y1 y2) < 0: K(Z_circ)* is not self-positive, so K(Z_circ) is not self-dual", "tr(y1 y2) = %s" % p12)

b0 = Matrix([1, 1, 0, 0]) / sqrt(2); b3_ = Matrix([0, 0, 1, -1]) / sqrt(2)   # |0+>, |1->
k0m = Matrix([1, -1, 0, 0]) / sqrt(2); k1p = Matrix([0, 0, 1, 1]) / sqrt(2)        # |0->, |1+>
bp = (k0m + k1p) / sqrt(2); bm = (k0m - k1p) / sqrt(2)
Uimg = Matrix.hstack(bp, b0, -I * bm, b3_)            # images of psi_1, psi_2, psi_3, psi_4
U = Uimg * PsiM.H
unit = sp.simplify(U * U.H) == eye(4)
img = U * gth
phi = 2 * th
c2 = (k0m + sp.exp(I * phi) * k1p) / sqrt(2)
match = sp.simplify(sp.expand(img * sp.exp(I * th) - c2, complex=True)) == zeros(4, 1)
x_ = symbols('x_')
Ux = eye(4) + (x_ - 1) * (Matrix([0, 0, 1, -1]) / sqrt(2)) * (Matrix([0, 0, 1, -1]) / sqrt(2)).H   # |1-> = (|10> - |11>)/sqrt2
fix = sp.simplify(Ux * c2 - c2) == zeros(4, 1)
rec("CHECK", "B5", unit and match and fix,
    "U unitary maps the circle onto C2 (e^{i th} U g_th = C2(e^{2 i th})); U(x) fixes every C2(w): K(Z_C2) = Ad(U) K(Z_circ) not self-dual")

qv = [expand(Matrix([[y[0, 0], y[0, 2]], [y[2, 0], y[2, 2]]]).det()) for y in ys]   # det of the W-compression
rec("COUNTERCONTROL", "CC1", any(d < 0 for d in qv),
    "at least one of y1, y2 is not PSD (negative determinant of its 2x2 compression to W), so they are not both in Q3", "W-dets %s" % qv)

y0 = [ys[i] - eye(4) / 1000 for i in range(2)]
p0 = expand((y0[0] * y0[1]).trace())
print("RECORD CC2 unshifted pairing %s" % p0)

recorded = [p12, p0] + marg + qv
rec("CHECK", "EX", not any(sp.sympify(t).has(sp.Float) for t in recorded), "no Float in any recorded value")

nfail = R_.count(False)
print("summary: %d checks, %d failed" % (len(R_), nfail))
if nfail == 0:
    print("VERDICT C7-CIRCLE-EXACT: the full Bell-circle surgery K(Z_circ) is not self-dual (two members of its dual pair to "
          "%s); the same holds for the kappa-fixed circle C2 by the unitary transfer" % p12)
else:
    print("NO VERDICT")
