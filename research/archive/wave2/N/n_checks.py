"""Thread N (wave 2): exact checks for the ellipsoid / K-infinity-R step.

Exact arithmetic only: sympy rationals, exact radicals and symbolic trigonometry. No floats.
Each check prints its id and OK; any failure raises. Run with PYTHONDONTWRITEBYTECODE=1.
"""
from sympy import (Matrix, Rational as Q, sqrt, symbols, cos, sin, simplify, eye, zeros,
                   pi, trigsimp, expand, solve, Symbol, ceiling, diag, nsimplify)

checks = []


def ok(cid, cond, note=""):
    if bool(cond) is not True:
        raise AssertionError(f"{cid} FAILED {note}")
    checks.append(cid)
    print(f"{cid}  OK  {note}")


def z(M):
    """True iff the symbolic matrix M simplifies to zero, after sin^2+cos^2=1."""
    M = M if hasattr(M, "shape") else Matrix([M])
    return all(simplify(trigsimp(expand(e))) == 0 for e in M)


th, ph, s, t = symbols('theta phi s t', real=True)


def Rz(a):
    return Matrix([[cos(a), -sin(a), 0], [sin(a), cos(a), 0], [0, 0, 1]])


def Rz_cs(c, sn):
    return Matrix([[c, -sn, 0], [sn, c, 0], [0, 0, 1]])


def rot_axis(u, c, sn):
    """Rodrigues rotation about unit vector u with cos c and sin sn (exact entries)."""
    u = Matrix(u)
    K = Matrix([[0, -u[2], u[1]], [u[2], 0, -u[0]], [-u[1], u[0], 0]])
    return eye(3) * c + sn * K + (1 - c) * (u * u.T)


def rot_axis_sym(u, a):
    return rot_axis(u, cos(a), sin(a))


def cayley(w):
    """Cayley transform of the skew matrix of w: a rational rotation for rational w."""
    w = Matrix(w)
    K = Matrix([[0, -w[2], w[1]], [w[2], 0, -w[0]], [-w[1], w[0], 0]])
    return (eye(3) - K).inv() * (eye(3) + K)


def is_SO3(R):
    return simplify(R * R.T - eye(3)) == zeros(3, 3) and simplify(R.det() - 1) == 0


# ---------------------------------------------------------------- X1: the interface algebra
# S = M M^T (positive definite), A = M R M^{-1} with R rational orthogonal.
M = Matrix([[2, 0, 0], [Q(1, 3), 1, 0], [-1, Q(1, 2), 3]])
S = M * M.T
R = cayley([Q(1, 2), Q(-1, 3), Q(2, 5)])
ok("X1.0", is_SO3(R), "Cayley rotation is in SO(3)")
A = M * R * M.inv()
ok("X1.1", A * S * A.T == S, "A S A^T = S (the interface identity)")
ok("X1.2", A.T * S.inv() * A == S.inv(), "equivalently A preserves <u,v> = u^T S^-1 v")
Mi = M.inv()
ok("X1.3", (Mi * A * M) * (Mi * A * M).T == eye(3), "normalization M^-1 A M is orthogonal (IIP -> IIP-N)")
# LDL-type factor: S = L D L^T, M' = L sqrt(D) also normalizes
Ld, Dd = None, None
# (sympy LDL) S = L * D * L.T
Ld, Dd = S.LDLdecomposition()
ok("X1.4", Ld * Dd * Ld.T == S and all(Dd[i, i] > 0 for i in range(3)), "LDL factorization with positive pivots")
Mp = Ld * diag(*[sqrt(Dd[i, i]) for i in range(3)])
Np = simplify(Mp.inv() * A * Mp)
ok("X1.5", simplify(Np * Np.T - eye(3)) == zeros(3, 3), "the LDL factor also normalizes A to an orthogonal matrix")

# ---------------------------------------------------------------- X2: det of a square
g = Matrix(3, 3, symbols('g0:9'))
ok("X2.1", expand((g * g).det() - g.det() ** 2) == 0, "det(Q^2) = det(Q)^2: a flow member is a square, so det = +1")

# ---------------------------------------------------------------- X3: commutants in SO(3)
Rq = Rz_cs(Q(3, 5), Q(4, 5))                     # rotation about e_z, not a half-turn
B = Matrix(3, 3, symbols('b0:9'))
sol = solve(list(B * Rq - Rq * B), list(B), dict=True)[0]
Bc = B.subs(sol)
ok("X3.1", Bc[0, 2] == 0 and Bc[1, 2] == 0 and Bc[2, 0] == 0 and Bc[2, 1] == 0
   and simplify(Bc[0, 0] - Bc[1, 1]) == 0 and simplify(Bc[0, 1] + Bc[1, 0]) == 0,
   "the commutant of a non-half-turn about e_z preserves e_z and acts as a rotation-scaling on e_z-perp")
H1 = diag(-1, -1, 1)
H2 = diag(1, -1, -1)
ok("X3.2", H1 * H2 == H2 * H1 and H2 * Matrix([0, 0, 1]) == Matrix([0, 0, -1]),
   "countercheck: half-turns about orthogonal axes commute and move each other's axis (Klein four-group)")
# A(t/2) is never a half-turn when A(t) != I: a half-turn squares to I.
ok("X3.3", H1 * H1 == eye(3), "a half-turn squares to the identity")

# ---------------------------------------------------------------- X4: J preserving the axis
ez = Matrix([0, 0, 1])
fam = {
    "rotation about e_z": (Rz(ph), 1),
    "reflection in a plane containing e_z": (Matrix([[cos(ph), sin(ph), 0], [sin(ph), -cos(ph), 0], [0, 0, 1]]), -1),
    "half-turn about an axis in e_z-perp": (Matrix([[cos(ph), sin(ph), 0], [sin(ph), -cos(ph), 0], [0, 0, -1]]), -1),
    "rotoreflection (Rz(phi) composed with z -> -z)": (Matrix([[cos(ph), -sin(ph), 0], [sin(ph), cos(ph), 0], [0, 0, -1]]), 1),
}
for k, (Bm, sg) in fam.items():
    ok(f"X4.{k[:12]}", z(Bm * Rz(th) * Bm.inv() - Rz(sg * th)) and z(Bm * ez - Bm[2, 2] * ez),
       f"B e_z = +-e_z ({k}): B Rz(th) B^-1 = Rz({'+' if sg == 1 else '-'}th), a flow member A(+-t)")

# ---------------------------------------------------------------- X5: J moving the axis
cyc = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
conj = cyc * Rz(th) * cyc.inv()
ex = Matrix([1, 0, 0])
ok("X5.1", z(conj * ex - ex) and z(conj - rot_axis_sym([1, 0, 0], th)), "cyc3 Rz(th) cyc3^-1 = Rx(th): axis e_x")
# Rz(s) fixes e_x only when cos s = 1, sin s = 0
ok("X5.2", z((Rz(s) * ex - ex) - Matrix([cos(s) - 1, sin(s), 0])), "Rz(s) e_x - e_x = (cos s - 1, sin s, 0)")
Bg = cayley([1, Q(2, 3), Q(-1, 2)])
b = Bg * ez
ok("X5.3", is_SO3(Bg) and b != ez and b != -ez, "a generic rational J moves e_z off +-e_z")
Cb = Bg * Rz_cs(Q(3, 5), Q(4, 5)) * Bg.inv()
ok("X5.4", simplify(Cb * b - b) == zeros(3, 1) and simplify(Cb * ez - ez) != zeros(3, 1),
   "its conjugate fixes B e_z and moves e_z, so it is no member of the e_z circle")

Jr = Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])   # swaps x and z: det -1
ok("X5.5", Jr.det() == -1 and z(Jr * Rz(th) * Jr.inv() - rot_axis_sym([1, 0, 0], -th)),
   "a reflection J (det -1) moving e_z: J Rz(th) J^-1 = Rx(-th); J_off_axis holds and the words contain det -1 maps (closure O(3), not SO(3))")

# ---------------------------------------------------------------- X6: dimension two (B6)
R2 = lambda a: Matrix([[cos(a), -sin(a)], [sin(a), cos(a)]])
Ref2 = Matrix([[cos(ph), sin(ph)], [sin(ph), -cos(ph)]])
ok("X6.1", z(R2(ph) * R2(th) * R2(ph).inv() - R2(th)), "O(2): rotations conjugate R(th) to R(th)")
ok("X6.2", z(Ref2 * R2(th) * Ref2.inv() - R2(-th)), "O(2): reflections conjugate R(th) to R(-th); J_off_axis fails in dim 2")
ok("X6.3", z(R2(th / 2) * R2(th / 2) - R2(th)), "dim 2: flow members are squares, so lie in SO(2), which is abelian")
# dimension one: O(1) = {+-1}, squares are 1
ok("X6.4", all((x * x) == 1 for x in (1, -1)), "dim 1: every flow member is a square in O(1) = {+-1}, hence 1: flow trivial")

# ---------------------------------------------------------------- X7: words in two circles
a = ez
# alpha = pi/2: Euler zxz, three factors.
Rx = lambda c, sn: rot_axis([1, 0, 0], c, sn)
tgt = cayley([Q(1, 3), Q(1, 4), Q(-1, 2)])
ok("X7.0", is_SO3(tgt), "rational target rotation")
# zxz: tgt = Rz(p1) Rx(p2) Rz(p3); cos p2 = tgt[2,2]
c2 = tgt[2, 2]
s2 = sqrt(1 - c2 ** 2)
# from tgt = Rz(p1) Rx(p2) Rz(p3): tgt[0,2] = sin p1 sin p2, tgt[1,2] = -cos p1 sin p2,
# tgt[2,0] = sin p2 sin p3, tgt[2,1] = sin p2 cos p3
c1, s1 = -tgt[1, 2] / s2, tgt[0, 2] / s2
c3, s3 = tgt[2, 1] / s2, tgt[2, 0] / s2
word = Rz_cs(c1, s1) * Rx(c2, s2) * Rz_cs(c3, s3)
ok("X7.1", simplify(word - tgt) == zeros(3, 3) and simplify(c1**2 + s1**2 - 1) == 0 and simplify(c3**2 + s3**2 - 1) == 0,
   "alpha = pi/2: a rational rotation is an exact 3-factor word Rz Rx Rz (exact radicals)")
# alpha = pi/3: b at 60 degrees from a
bb = Matrix([sqrt(3) / 2, 0, Q(1, 2)])
ok("X7.2", simplify(bb.dot(a) - Q(1, 2)) == 0 and simplify(bb.dot(bb) - 1) == 0, "b is a unit vector at angle pi/3 to a")
Rb = lambda c, sn: rot_axis(bb, c, sn)
Ra = lambda c, sn: rot_axis(a, c, sn)
# reach step: R_b(pi) a is at angle 2 alpha from a: (R_b(pi)a).a = 2(a.b)^2 - 1
ok("X7.3", simplify((Rb(-1, 0) * a).dot(a) - (2 * bb.dot(a) ** 2 - 1)) == 0, "R_b(pi) a . a = 2(a.b)^2 - 1 = cos(2 alpha)")
# odd witness: half-turn about a x b sends a -> -a and b -> -b
axb = a.cross(bb)
nab = axb / sqrt(axb.dot(axb))
Hodd = rot_axis(nab, -1, 0)
ok("X7.4", simplify(Hodd * a + a) == zeros(3, 1) and simplify(Hodd * bb + bb) == zeros(3, 1),
   "half-turn about a x b: a -> -a, b -> -b (unreachable by a..a / b..b words when 2k alpha < pi)")
# even witness: half-turn about a - b sends b -> -a and a -> -b
amb = a - bb
nmb = amb / sqrt(amb.dot(amb))
Hev = rot_axis(nmb, -1, 0)
ok("X7.5", simplify(Hev * bb + a) == zeros(3, 1) and simplify(Hev * a + bb) == zeros(3, 1),
   "half-turn about a - b: b -> -a, a -> -b (unreachable by (ab)^k / (ba)^k when (2k-1) alpha < pi)")
# n = 4 = ceil(pi/alpha)+1 at alpha = pi/3: the extremal Hev is an exact 4-factor word.
# Hev = R_a(pi) R_b(pi) R_a(theta3) R_b(0): solve theta3 from the residual, which must fix a.
resid = simplify((Ra(-1, 0) * Rb(-1, 0)).inv() * Hev)
ok("X7.6", simplify(resid * a - a) == zeros(3, 1), "residual R_b(pi)^-1 R_a(pi)^-1 Hev fixes a")
c3e, s3e = simplify(resid[0, 0]), simplify(resid[1, 0])
ok("X7.7", simplify(Ra(c3e, s3e) - resid) == zeros(3, 3) and simplify(c3e**2 + s3e**2 - 1) == 0,
   f"residual = R_a with cos = {c3e}, sin = {s3e}: Hev = R_a(pi) R_b(pi) R_a(.) (3 factors; padded to 4 with R_b(0))")
# Note: Hev is an odd word a b a here because 2 alpha = 2pi/3 >= angle(a, Hev a) = angle(a,-b) = 2pi/3 (boundary).
ok("X7.8", simplify((Hev * a).dot(a) - cos(2 * pi / 3)) == 0, "angle(a, Hev a) = 2pi/3 = 2 alpha: on the cap boundary")
# Hodd has angle(a, Hodd a) = pi > 2 alpha: not an a..a word of length 3; angle(b, Hodd b) = pi: not b..b of length 3.
ok("X7.9", simplify((Hodd * a).dot(a) + 1) == 0 and simplify((Hodd * bb).dot(bb) + 1) == 0,
   "Hodd: both 3-factor orders excluded at alpha = pi/3 (needs 2 alpha >= pi)")
# Hodd as an exact 4-factor (ab)^2 word: need angle(a, Hodd b) <= 3 alpha = pi: always.
# Construct: Hodd = W R_b(pi) with W in a b a; W a = Hodd R_b(pi) a must be within 2 alpha of a.
W = Hodd * Rb(-1, 0).inv()
Wa = simplify(W * a)
cdot = simplify(Wa.dot(a))
ok("X7.10", simplify(cdot - Q(1, 2)) == 0, "with th4 = pi, angle(a, W a) = pi/3 <= 2 alpha: W lies in the cap reached by a b a")


def decompose_aba(Wm):
    """Exact R_a(p1) R_b(p2) R_a(p3) = Wm, a = e_z, b = bb; returns (cos,sin) triples."""
    wa = simplify(Wm * a)
    ab = bb.dot(a)
    c2 = simplify((wa.dot(a) - ab**2) / (1 - ab**2))   # (R_b(p2) a).a = (a.b)^2 + (1-(a.b)^2) cos p2
    s2 = sqrt(simplify(1 - c2**2))
    v0 = simplify(Rb(c2, s2) * a)
    hx, hy, wx, wy = v0[0], v0[1], wa[0], wa[1]
    nr = simplify(hx**2 + hy**2)
    c1 = simplify((hx * wx + hy * wy) / nr)
    s1 = simplify((hx * wy - hy * wx) / nr)
    res = simplify((Ra(c1, s1) * Rb(c2, s2)).inv() * Wm)
    return (c1, s1), (c2, s2), (simplify(res[0, 0]), simplify(res[1, 0])), res


(c1, s1), (c2, s2), (c3, s3), res = decompose_aba(W)
full = Ra(c1, s1) * Rb(c2, s2) * Ra(c3, s3) * Rb(-1, 0)
ok("X7.11", simplify(res * a - a) == zeros(3, 1) and simplify(full - Hodd) == zeros(3, 3)
   and all(simplify(cc**2 + sn**2 - 1) == 0 for cc, sn in [(c1, s1), (c2, s2), (c3, s3)]),
   f"Hodd = R_a R_b R_a R_b(pi) exactly at alpha = pi/3 (cos p2 = {c2}); 4 factors, while 3 do not suffice (X7.9)")
al = Symbol('alpha', positive=True)
bal = Matrix([sin(al), 0, cos(al)])
Hodd_s = rot_axis(Matrix([0, 1, 0]), -1, 0)          # half-turn about a x b (parallel to e_y)
nm = Matrix([-sin(al), 0, 1 - cos(al)])              # a - b, unnormalized
Hev_s = 2 * (nm * nm.T) / (nm.dot(nm)) - eye(3)      # half-turn about a - b
ok("X7.14", z(Hodd_s * a + a) and z(Hodd_s * bal + bal) and z(simplify(Hev_s * bal + a)) and z(simplify(Hev_s * a + bal)),
   "for every alpha: half-turn about a x b sends a,b to -a,-b; half-turn about a - b sends b -> -a, a -> -b")
for kk in range(2, 7):
    lo, hi = pi / (kk + 1), pi / kk
    ok(f"X7.L{kk}", ceiling(pi / lo) + 1 == kk + 2 and ceiling(pi / (hi * Q(999, 1000))) + 1 == kk + 2,
       f"Lowenthal's interval form (pi/{kk+1} <= alpha < pi/{kk} gives order {kk+2}) agrees with ceil(pi/alpha)+1 at the interval ends")
# The order formula N(alpha) = ceil(pi/alpha) + 1 at sample angles
for (al, N) in [(pi / 2, 3), (pi / 3, 4), (pi / 4, 5), (2 * pi / 5, 4), (pi / 7, 8)]:
    ok(f"X7.N({al})", ceiling(pi / al) + 1 == N and ((N - 1) * al - pi) >= 0 and ((N - 2) * al - pi) < 0,
       f"N({al}) = {N}: (N-1) alpha >= pi > (N-2) alpha")
# cosine doubling (perpendicular-axis route): 1 - (2x^2 - 1) = 2(1 - x)(1 + x) >= 2(1 - x) for x >= 0
x = Symbol('x', real=True)
ok("X7.12", expand((1 - (2 * x**2 - 1)) - 2 * (1 - x) * (1 + x)) == 0, "doubling identity for x -> 2x^2 - 1")
# the conjugated axis: R_b(pi) e_z has z-component 2 b_z^2 - 1
bz = Symbol('bz', real=True)
bv = Matrix([sqrt(1 - bz**2), 0, bz])
ok("X7.13", simplify((rot_axis(bv, -1, 0) * ez)[2] - (2 * bz**2 - 1)) == 0, "z-component of R_b(pi) e_z is 2 b_z^2 - 1")

# ---------------------------------------------------------------- X8: dimension four
def blk(A2, B2):
    Mx = zeros(4, 4)
    Mx[0:2, 0:2] = A2
    Mx[2:4, 2:4] = B2
    return Mx


I2 = eye(2)
F = lambda a_: blk(R2(a_), I2)
Jsw = Matrix([[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]])
ok("X8.1", z(Jsw * F(th) * Jsw.inv() - blk(I2, R2(th))), "B4/bidisk: swap conjugates R(t)+I to I+R(t)")
p = Matrix([0, 0, 1, 0])
ok("X8.2", z(blk(I2, R2(pi / 2)) * p - Matrix([0, 0, 0, 1])) and z(F(s) * p - p),
   "J_off_axis witness at t = pi/2: I+R(pi/2) moves (0,0,1,0), every R(s)+I fixes it")
xs = Matrix(symbols('x1:5', real=True))
mfun = lambda v: (v[0]**2 + v[1]**2) * (v[2]**2 + v[3]**2)
for nm, Gm in [("R+I", F(th)), ("I+R", blk(I2, R2(th))), ("swap", Jsw)]:
    ok(f"X8.3.{nm}", simplify(trigsimp(expand(mfun(Gm * xs) - mfun(xs)))) == 0, f"invariant m = |x12|^2 |x34|^2 preserved by {nm}")
e1 = Matrix([1, 0, 0, 0])
q = Matrix([1, 0, 1, 0]) / sqrt(2)
ok("X8.4", mfun(e1) == 0 and simplify(mfun(q) - Q(1, 4)) == 0 and simplify(q.dot(q) - 1) == 0,
   "e1 and (e1+e3)/sqrt2 are unit vectors with m = 0 and 1/4: the generated group and its closure are not transitive on S^3")
# bidisk boundary contains a segment: (1,0,0,s) for s in [0,1] are boundary states (witness y = (-1,0,0,s))
ss = Symbol('ss', real=True)
eps = Symbol('eps', positive=True)
xpt = Matrix([1, 0, 0, ss])
ypt = Matrix([-1, 0, 0, ss])
ext = xpt + eps * (xpt - ypt)
ok("X8.5", simplify(ext[0]**2 + ext[1]**2 - (1 + 2 * eps)**2) == 0,
   "bidisk: (1,0,0,s) + eps((1,0,0,s) - (-1,0,0,s)) has |x12| = 1 + 2 eps > 1: boundary states along a segment, so not an ellipsoid")
# SO(3)+1 on B4: the fourth coordinate is invariant
cyc4 = blk(Matrix([[0, 0], [1, 0]]), I2)  # placeholder not used
R31 = zeros(4, 4); R31[0:3, 0:3] = Rz(th); R31[3, 3] = 1
C31 = zeros(4, 4); C31[0:3, 0:3] = cyc; C31[3, 3] = 1
e4 = Matrix([0, 0, 0, 1])
ok("X8.6", z(R31.T * e4 - e4) and C31.T * e4 == e4, "B4 with Rz+1, cyc3+1: x4 = <x, e4> is invariant, so e1 and e4 are in different orbits")

# ---------------------------------------------------------------- X9: Hamel model, J_off_axis witness
ok("X9.1", z(rot_axis_sym([1, 0, 0], pi) * ez + ez) and z(Rz(s) * ez - ez),
   "Hamel model (t0 = 1, phi(1) = pi): Rx(pi) e_z = -e_z while every Rz(s) fixes e_z")

# ---------------------------------------------------------------- X10/X11: closedness, convexity
yv = Matrix(symbols('y1:4', real=True))
ok("X11.1", z(Matrix([(Rz(th) * yv).dot(Rz(th) * yv) - yv.dot(yv)])) and (cyc * yv).dot(cyc * yv) == yv.dot(yv),
   "rotations and cyc3 preserve |x|^2, so the shell 1 <= |x| <= 2 is preserved by the ball3Drive maps")
ok("X11.2", (Q(1, 2) * (ez + (-ez))).dot(Q(1, 2) * (ez + (-ez))) == 0,
   "shell: the midpoint of e_z and -e_z is 0, outside the shell; the shell is SO(3)-invariant and not a ball")

# ---------------------------------------------------------------- X12: noncompact cylinder, shear J
Jsh = Matrix([[1, 0, 0], [0, 1, 0], [1, 0, 1]])   # (x,y,z) -> (x, y, z + x)
ok("X12.1", (Jsh - eye(3)) ** 2 == zeros(3, 3) and Jsh != eye(3), "J is unipotent and not the identity: orthogonal for no inner product")
P = Matrix([1, 0, 0])
cnj = Jsh * Rz_cs(0, 1) * Jsh.inv()
ok("X12.2", (cnj * P)[2] == -1, "J Rz(pi/2) J^-1 moves (1,0,0) off the plane z = 0; no Rz(s) does: J_off_axis holds")
ok("X12.3", z((Rz(ph) * Jsh * Rz(-ph) * Matrix([1, 0, 0]))[2] - cos(ph)),
   "the conjugate Rz(ph) J Rz(-ph) shifts z by cos(ph) at (1,0,0): every height is reached, the lateral surface is one orbit")
ok("X12.4", (Jsh * Matrix([symbols('u'), symbols('v'), symbols('w')]))[0:2, 0] == Matrix([symbols('u'), symbols('v')]),
   "J keeps (x,y): it preserves the cylinder x^2 + y^2 <= 1 in both directions")

# ---------------------------------------------------------------- X13: J_off_axis read on V would be too weak
# V = R^4, Omega = ball3 x {0}; flow t (x,w) = (R(t)x + w (R(t) - I) u, w); J (x,w) = (x + w u', w).
u = Matrix([1, 0, 0])
up = Matrix([0, 1, 0])


def flow4(a_):
    Mx = zeros(4, 4)
    Mx[0:3, 0:3] = Rz(a_)
    Mx[0:3, 3] = (Rz(a_) - eye(3)) * u
    Mx[3, 3] = 1
    return Mx


J4 = eye(4)
J4[0:3, 3] = up
ok("X13.1", z(flow4(s) * flow4(t) - flow4(s + t)), "the sheared flow is a one-parameter group on R^4")
xw0 = Matrix(list(symbols('p1:4', real=True)) + [0])
ok("X13.2", z(J4 * flow4(th) * J4.inv() * xw0 - flow4(th) * xw0), "on Omega (w = 0), J flow(t) J^-1 = flow(t): the landed J_off_axis fails")
ok("X13.3", simplify((J4 * flow4(pi / 2) * J4.inv() - flow4(pi / 2))[0:3, 3]) != zeros(3, 1),
   "on V the two differ (in the w-column): an off-axis clause read on V would hold with J acting as the identity on Omega")

print(f"OK -- {len(checks)} checks")
