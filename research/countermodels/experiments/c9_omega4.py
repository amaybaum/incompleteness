# c9_omega4.py -- research/countermodels node C9 (round 2): the single-system analogue of extreme-ray transitivity on
# HO-7's body Omega_4 = {(x, s) in R^3 x R : |x|^4 + s^4 <= 1} and on the ball.
# DECISION RULE (fixed before the first run, 2026-10-10T22:53Z by date -u; predictions in NOTES-C9 S0):
#  Exact arithmetic only (sympy, symbolic or Rational; the guard EX checks that no Float occurs). Lines are CHECK <id>
#  PASS/FAIL or COUNTERCONTROL <id> PASS/FAIL (a case where the stated property must fail). VERDICT C9-OMEGA4-EXACT iff
#  all pass, otherwise NO VERDICT; the verdict text is generated from the measured values.
#  A1  det Hess N = 2304 s^2 |x|^6 for N = |x|^4 + s^4 (symbolic).
#  A2  chain rule for the Hessian determinant under a linear substitution: det Hess(N o A)(w) = det(A)^2 (det Hess N)(A w),
#      checked symbolically for a generic rational A (the [W] identity used in NOTES-C9 W1).
#  A3  the factorization ingredients: the Hessian of |x|^2 has rank 3 (a quadratic form that factors into linear forms
#      has rank <= 2, so |x|^2 is irreducible over R); for an invertible A the form |B x + b s|^2 (first three rows of
#      A) has rank 3; sympy's factor_list of |x|^2 over Q(i) returns one factor.
#  A4  every listed element of O(3) x Z2 (rational orthogonal matrices from the Cayley transform, and the sign of s)
#      preserves N symbolically.
#  CC1 countercontrols: a rational rotation mixing x1 and s, the scaling (x, s) -> (x, 2s) and a shear in x
#      (a non-orthogonal B) do not preserve N.
#  O1  orbit invariant: N o g = N and s^2 o g = s^2 for g in O(3) x Z2 (so s^4 is constant on orbits); two boundary
#      points with different s^4 exist on dBoundary at rational s^2 with |x|^4 = 1 - s^4 (exact).
#  F1  c* on Omega_4 and on the 4-ball: the gradient of N (resp. |x|^2 + s^2) is nonzero on the boundary (symbolic:
#      grad N = (4|x|^2 x, 4 s^3) vanishes only at 0), so the supporting hyperplane at each boundary point is unique and
#      c* = 1 (the exposed face of the effect cone is one ray).
#  CC2 the cylinder {|x| <= 1, |s| <= 1} at the edge point (e1, 1): two independent supporting functionals (c* = 2).
#  CC3 Q3 (d = 4) at the pure state |0><0|: the effects vanishing on it form PSD(|0>^perp), span dimension 9.
#  S1  rank of the second fundamental form = rank of Hess N restricted to the tangent space grad N^perp:
#      3 at a generic boundary point, 2 on the equator s = 0, 0 at the poles x = 0 (exact, at representative points:
#      generic (a, 0, 0, b) with a^4 + b^4 = 1 treated symbolically in a, b > 0); the 4-ball: 3 everywhere.
#  P1  the polar body: on the axes the support function of Omega_4 is |y| (t = 0) and |t| (y = 0), and the polar's
#      boundary function phi(y, t) = (|y|^(4/3) + |t|^(4/3))^(3/4) has a second t-derivative at (y, t) = (1, 0+) that is
#      unbounded (symbolic limit oo), while Hess N is bounded near every boundary point of Omega_4 ([W] W4: a linear
#      isomorphism preserves C^2 smoothness of the boundary).
import sympy as sp
from sympy import Matrix, Rational as Q, symbols, eye, zeros, sqrt, expand, simplify

R_ = []
def rec(kind, cid, ok, text, detail=""):
    ok = bool(ok); R_.append(ok)
    print(f"{kind} {cid:<5} {'PASS' if ok else 'FAIL'} {text}" + (f" -- {detail}" if detail else ""))

x1, x2, x3, s = symbols('x1 x2 x3 s', real=True)
X = Matrix([x1, x2, x3]); W = Matrix([x1, x2, x3, s])
r2 = x1 ** 2 + x2 ** 2 + x3 ** 2
N = r2 ** 2 + s ** 4
HN = sp.hessian(N, (x1, x2, x3, s))
dH = sp.factor(HN.det())
rec("CHECK", "A1", expand(dH - 2304 * s ** 2 * r2 ** 3) == 0, "det Hess N = 2304 s^2 |x|^6", "%s" % dH)

A = Matrix([[2, -1, 0, 1], [1, 3, 1, 0], [0, 1, 1, -2], [1, 0, 2, 1]])
NA = N.subs(dict(zip((x1, x2, x3, s), list(A * W))), simultaneous=True)
lhs = sp.hessian(NA, (x1, x2, x3, s)).det()
rhs = A.det() ** 2 * dH.subs(dict(zip((x1, x2, x3, s), list(A * W))), simultaneous=True)
rec("CHECK", "A2", expand(lhs - rhs) == 0 and A.det() != 0, "det Hess(N o A) = det(A)^2 (det Hess N) o A for a generic rational A",
    "det A = %s" % A.det())

rank_r2 = sp.hessian(r2, (x1, x2, x3)).rank()
form = (A[:3, :] * W).T * (A[:3, :] * W)
rank_form = sp.hessian(form[0], (x1, x2, x3, s)).rank()
fl = sp.factor_list(r2, gaussian=True)
rec("CHECK", "A3", rank_r2 == 3 and rank_form == 3 and len(fl[1]) == 1 and fl[1][0][1] == 1,
    "|x|^2 has rank 3 (irreducible over R); |B x + b s|^2 has rank 3 for invertible A; one factor over Q(i)",
    "ranks %d, %d" % (rank_r2, rank_form))

def cayley(a, b, c):
    S_ = Matrix([[0, -c, b], [c, 0, -a], [-b, a, 0]])
    return (eye(3) - S_) * (eye(3) + S_).inv()
Os = [cayley(Q(1, 2), Q(1, 3), Q(-2, 5)), cayley(Q(3), Q(-1), Q(1, 7)), Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]]), -eye(3)]
okA4 = True
for O_ in Os:
    for sg in (1, -1):
        G = sp.diag(O_, sg)
        okA4 = okA4 and (O_.T * O_ == eye(3)) and expand(N.subs(dict(zip((x1, x2, x3, s), list(G * W))), simultaneous=True) - N) == 0
rec("CHECK", "A4", okA4, "eight listed elements of O(3) x Z2 (Cayley rationals, a reflection, -I; both signs of s) preserve N")

c_, s_ = Q(3, 5), Q(4, 5)
Mix = Matrix([[c_, 0, 0, -s_], [0, 1, 0, 0], [0, 0, 1, 0], [s_, 0, 0, c_]])
Scl = sp.diag(1, 1, 1, 2)
Bno = sp.diag(Matrix([[1, 1, 0], [0, 1, 0], [0, 0, 1]]), 1)
def preserves(G): return expand(N.subs(dict(zip((x1, x2, x3, s), list(G * W))), simultaneous=True) - N) == 0
rec("COUNTERCONTROL", "CC1", not preserves(Mix) and not preserves(Scl) and not preserves(Bno),
    "an x1-s rotation (cos = 3/5), the scaling s -> 2s and a shear in x do not preserve N")

sa2, sb2 = Q(1, 4), Q(3, 4)          # s^2 values; |x|^4 = 1 - s^4
pa = (1 - sa2 ** 2, sa2 ** 2); pb = (1 - sb2 ** 2, sb2 ** 2)   # (|x|^4, s^4) on the boundary
okO1 = all(expand((s ** 2).subs(s, (sp.diag(O_, sg) * W)[3]) - s ** 2) == 0 for O_ in Os for sg in (1, -1)) \
    and pa[0] + pa[1] == 1 and pb[0] + pb[1] == 1 and pa[1] != pb[1]
rec("CHECK", "O1", okO1, "s^2 (hence s^4) is invariant under O(3) x Z2; boundary points with s^4 = 1/16 and 9/16 lie in different orbits",
    "(|x|^4, s^4) = %s, %s" % (pa, pb))

gN = Matrix([sp.diff(N, v) for v in (x1, x2, x3, s)])
okF1 = expand(gN[3] - 4 * s ** 3) == 0 and all(expand(gN[i] - 4 * r2 * X[i]) == 0 for i in range(3)) \
    and expand((gN.T * W)[0] - 4 * N) == 0
rec("CHECK", "F1", okF1, "grad N = (4|x|^2 x, 4 s^3), <grad N, w> = 4 N(w) = 4 on the boundary: nonzero there, unique supporting hyperplane, c* = 1; ball: grad = 2w, the same")

# cylinder edge (e1, 1): supporting functionals of {|x| <= 1, |s| <= 1} at that point are cone{(e1, 0), (0, 1)}
f1 = Matrix([1, 0, 0, 0]); f2 = Matrix([0, 0, 0, 1]); pt = Matrix([1, 0, 0, 1])
okCC2 = (f1.T * pt)[0] == 1 and (f2.T * pt)[0] == 1 and Matrix.hstack(f1, f2).rank() == 2
rec("COUNTERCONTROL", "CC2", okCC2, "cylinder edge (e1, 1): two independent supporting functionals (|x| <= 1 and s <= 1 both tight): c* = 2")

# Q3, d = 4: effects e >= 0 with tr(e |0><0|) = 0 are PSD on |0>^perp: basis of Herm(|0>^perp)
basis = []
for i in range(1, 4):
    for j in range(i, 4):
        Mr = zeros(4, 4); Mr[i, j] = 1; Mr[j, i] = 1; basis.append(Mr)
        if i != j:
            Mi = zeros(4, 4); Mi[i, j] = sp.I; Mi[j, i] = -sp.I; basis.append(Mi)
vecs = Matrix([[sp.re(B[a, b]) for a in range(4) for b in range(4)] + [sp.im(B[a, b]) for a in range(4) for b in range(4)] for B in basis])
rec("COUNTERCONTROL", "CC3", vecs.rank() == 9 and all(B[0, 0] == 0 for B in basis),
    "Q3 (d = 4) at |0><0|: the vanishing effects span Herm(|0>^perp), dimension 9 = (d - 1)^2")

def sff_rank(Hm, g):
    # rank of Hm restricted to g^perp
    T = Matrix.hstack(*[v for v in Matrix([list(g)]).nullspace()])
    return (T.T * Hm * T).rank(simplify=True)
a, b = symbols('a b', positive=True)
Hgen = HN.subs({x1: a, x2: 0, x3: 0, s: b}); ggen = gN.subs({x1: a, x2: 0, x3: 0, s: b})
Heq = HN.subs({x1: 1, x2: 0, x3: 0, s: 0}); geq = gN.subs({x1: 1, x2: 0, x3: 0, s: 0})
Hpo = HN.subs({x1: 0, x2: 0, x3: 0, s: 1}); gpo = gN.subs({x1: 0, x2: 0, x3: 0, s: 1})
rg, re_, rp = sff_rank(Hgen, ggen), sff_rank(Heq, geq), sff_rank(Hpo, gpo)
Hball = sp.hessian(r2 + s ** 2, (x1, x2, x3, s)); gball = Matrix([2 * x1, 2 * x2, 2 * x3, 2 * s])
rb = [sff_rank(Hball, gball.subs(pnt)) for pnt in ({x1: 1, x2: 0, x3: 0, s: 0}, {x1: 0, x2: 0, x3: 0, s: 1}, {x1: Q(3, 5), x2: 0, x3: 0, s: Q(4, 5)})]
rec("CHECK", "S1", (rg, re_, rp) == (3, 2, 0) and rb == [3, 3, 3],
    "rank of the second fundamental form: Omega_4 generic 3, equator 2, poles 0; 4-ball 3 at every listed point",
    "Omega_4 %s, ball %s" % ((rg, re_, rp), rb))

y, t = symbols('y t', positive=True)
phi = (y ** Q(4, 3) + t ** Q(4, 3)) ** Q(3, 4)
lim = sp.limit(sp.diff(phi, t, 2).subs(y, 1), t, 0, '+')
hb = [sp.Abs(e) for e in HN.subs({x1: 1, x2: 0, x3: 0, s: 0})]
rec("CHECK", "P1", lim == sp.oo and phi.subs(t, 0) == y and all(e.is_finite for e in hb),
    "the polar's boundary function has d^2/dt^2 -> oo at (1, 0+) while Hess N is finite on the boundary of Omega_4",
    "limit %s" % lim)

recorded = [dH, lhs - rhs, rank_r2, rank_form, rg, re_, rp, lim] + list(pa) + list(pb) + rb
rec("CHECK", "EX", not any(sp.sympify(v).has(sp.Float) for v in recorded), "no Float in any recorded value")

nfail = R_.count(False)
print("summary: %d checks, %d failed" % (len(R_), nfail))
if nfail == 0:
    print("VERDICT C9-OMEGA4-EXACT: det Hess N = %s forces Aut(Omega_4) = O(3) x Z2; orbits on the boundary are the level "
          "sets of s^4 (not transitive); c* = 1 at every pure state (smooth boundary), as for the ball; second fundamental "
          "form ranks %s (generic, equator, poles) against %s on the ball" % (dH, (rg, re_, rp), rb[0]))
else:
    print("NO VERDICT")
