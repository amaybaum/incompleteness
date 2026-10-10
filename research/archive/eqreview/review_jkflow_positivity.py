"""Independent check (coordinator; own reconstruction) that EQ-B's J/K flow G_t is positive on product states at EVERY t,
at d = 5, i.e. that each G_t maps every product state of eball 5 into maxCone; G_t^{-1} = G_{-t} then gives two-sided
positivity.  Flow blocks as stated in EQ-B's jk.py docstring (rebuilt in review_eqB.py, where G_pi == landed gC5).

Certificate (my reconstruction of EQ-B's W-JK, written so each step is an exact identity or an elementary inequality):
  p = f0 + f_x y_x,  q = f0 y_x + f_x  (E+ = span(e0, e_x)),  u = f_minus, v = y_minus  (E- = homogeneous 2..5, K on E-),
  P = (p+q)/2,  M = (p-q)/2,  omega = (u.v + i u.Kv)/2,
  alpha = <f, Y>, beta = <f, R_t Y>, a' = <f, A_t Y>, b' = <f, B_t Y>  (Y = hom y).
  S1  value = 1/2(1+x_z)(e0+e_z) alpha + 1/2(1-x_z)(e0-e_z) beta + (e_T.x_T) a' + (e_T.J x_T) b'      [identity in c, s]
  S2  alpha beta - a'^2 - b'^2 = (2 - 2c)(P M - |omega|^2)                                          [identity on c^2+s^2=1]
  S3  4(P M - |omega|^2) = (f0^2 - f_x^2 - |u|^2)(1 - y_x^2) + |u|^2 (1 - y_x^2 - |v|^2)
                           + [|u|^2|v|^2 - (u.v)^2 - (u.Kv)^2]                                       [identity]
      each bracket >= 0: f in the Lorentz cone; y in the ball; Bessel for the orthogonal complex structure K.
  S4  4AB - C^2 = [(1-x_z^2)(e0^2-e_z^2) - |x_T|^2|e_T|^2] alpha beta + |x_T|^2|e_T|^2 (alpha beta - a'^2 - b'^2)
                  + (a'^2 + b'^2) Bes_J + ((e_T.x_T) b' - (e_T.J x_T) a')^2                        [identity]
      with A, B the first two terms of S1 and C the last two; A, B >= 0 and 4AB >= C^2 give value >= 0.
Also: alpha, beta >= 0 needs R_t orthogonal on the tail (checked) so that hom(R_t-image) stays in the cone.
"""
import sys
from sympy import Matrix, Rational as R, eye, zeros, symbols, expand, cancel, together
sys.path.insert(0, "/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/bal")
from relt_common import hom, gate_from_fun, apply, pairVal
from bal_gates import cstruct

checks = []


def check(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)
    sys.stdout.flush()


d, n = 5, 6
X = zeros(n, n); X[0, 1] = 1; X[1, 0] = 1
K = cstruct(n, [(2, 5), (3, 4)])
J = cstruct(n, [(1, 2), (3, 4)])
Pp = zeros(n, n); Pp[0, 0] = 1; Pp[1, 1] = 1
Pm = eye(n) - Pp
c, s = symbols("c s")
Rt = Pp + c * Pm + s * K * Pm
At = (1 + c) / 2 * eye(n) + (1 - c) / 2 * X * Pp + s / 2 * K * Pm
Bt = s / 2 * (Pp - X * Pp) + s / 2 * Pm + (1 - c) / 2 * K * Pm
z = Matrix([0, 0, 0, 0, 1])
hz, hm = hom(z), hom(-z)


def G_basis(mu, Y):
    if mu == 0:
        return (hz * Y.T + hm * (Rt * Y).T) / 2
    if mu == d:
        return (hz * Y.T - hm * (Rt * Y).T) / 2
    e = zeros(n, 1); e[mu] = 1
    return e * (At * Y).T + (J * e) * (Bt * Y).T


def G_apply(w):
    out = zeros(n, n)
    for mu in range(n):
        for nu in range(n):
            if w[mu, nu] != 0:
                Y = zeros(n, 1); Y[nu] = 1
                out += w[mu, nu] * G_basis(mu, Y)
    return out


xs = Matrix(symbols("x0:5")); ys = Matrix(symbols("y0:5"))
es = Matrix(symbols("e0:6")); fs = Matrix(symbols("f0:6"))
Y = hom(ys)
val = expand((es.T * G_apply(hom(xs) * Y.T) * fs)[0, 0])
alpha = (fs.T * Y)[0, 0]
beta = (fs.T * Rt * Y)[0, 0]
ap = (fs.T * At * Y)[0, 0]
bp = (fs.T * Bt * Y)[0, 0]
xz, ez = xs[4], es[5]
xT = Matrix([0] + [xs[i] for i in range(4)] + [0])
eT = Matrix([0] + [es[i] for i in range(1, 5)] + [0])
A_ = R(1, 2) * (1 + xz) * (es[0] + ez) * alpha
B_ = R(1, 2) * (1 - xz) * (es[0] - ez) * beta
a1 = (eT.T * xT)[0, 0]
a2 = (eT.T * J * xT)[0, 0]
C_ = a1 * ap + a2 * bp
check("S1 value = A + B + (e_T.x_T) a' + (e_T.J x_T) b'  (identity in c, s)", expand(val - (A_ + B_ + C_)) == 0)

# S2 on the circle: rational parametrization
m = symbols("m")
cm, sm = (1 - m ** 2) / (1 + m ** 2), 2 * m / (1 + m ** 2)
p = fs[0] + fs[1] * ys[0]
q = fs[0] * ys[0] + fs[1]
u = Matrix([fs[i] for i in range(2, 6)])
v = Matrix([ys[i] for i in range(1, 5)])
Km = K.extract([2, 3, 4, 5], [2, 3, 4, 5])
uv = (u.T * v)[0, 0]
uKv = (u.T * Km * v)[0, 0]
PM_minus = (p + q) / 2 * (p - q) / 2 - (uv ** 2 + uKv ** 2) / 4
lhs2 = (alpha * beta - ap ** 2 - bp ** 2).subs({c: cm, s: sm})
rhs2 = (2 - 2 * cm) * PM_minus
check("S2 alpha beta - a'^2 - b'^2 = (2 - 2c)(PM - |omega|^2) on c^2 + s^2 = 1",
      cancel(together(expand(lhs2 - rhs2))) == 0)
u2 = (u.T * u)[0, 0]; v2 = (v.T * v)[0, 0]
s3 = (fs[0] ** 2 - fs[1] ** 2 - u2) * (1 - ys[0] ** 2) + u2 * (1 - ys[0] ** 2 - v2) + (u2 * v2 - uv ** 2 - uKv ** 2)
check("S3 4(PM - |omega|^2) = cone slack (1-y_x^2) + |u|^2 ball slack + Bessel bracket", expand(4 * PM_minus - s3) == 0)
g = v2 * u - uv * v - uKv * (Km * v)
check("S3 Bessel bracket: |v|^2 [|u|^2|v|^2 - (u.v)^2 - (u.Kv)^2] = |g|^2 (K orthogonal complex structure)",
      expand(v2 * (u2 * v2 - uv ** 2 - uKv ** 2) - (g.T * g)[0, 0]) == 0)
xt = Matrix([xs[i] for i in range(4)]); et = Matrix([es[i] for i in range(1, 5)])
Jt = J.extract([1, 2, 3, 4], [1, 2, 3, 4])
xt2 = (xt.T * xt)[0, 0]; et2 = (et.T * et)[0, 0]
besJ = et2 * xt2 - a1 ** 2 - a2 ** 2
gJ = xt2 * et - a1 * xt - a2 * (Jt * xt)
check("S4 Bessel on T: |x_T|^2 Bes_J = |g_J|^2", expand(xt2 * besJ - (gJ.T * gJ)[0, 0]) == 0)
s4 = ((1 - xz ** 2) * (es[0] ** 2 - ez ** 2) - xt2 * et2) * alpha * beta + xt2 * et2 * (alpha * beta - ap ** 2 - bp ** 2) \
    + (ap ** 2 + bp ** 2) * besJ + (a1 * bp - a2 * ap) ** 2
check("S4 4AB - C^2 decomposition (identity in c, s)", expand(4 * A_ * B_ - C_ ** 2 - s4) == 0)
Rtm = Rt.subs({c: cm, s: sm})
tail = Rtm[1:, 1:]
check("R_t is 1 (+) orthogonal on the circle (so alpha, beta >= 0 for f in the cone, y in the ball)",
      Rtm[0, 0] == 1 and Rtm[0, 1:].is_zero_matrix and Rtm[1:, 0].is_zero_matrix
      and (tail.T * tail - eye(5)).applyfunc(lambda e: cancel(e)).is_zero_matrix)
check("J and K are orthogonal complex structures on their blocks",
      (Jt * Jt + eye(4)).is_zero_matrix and (Jt.T * Jt - eye(4)).is_zero_matrix
      and (Km * Km + eye(4)).is_zero_matrix and (Km.T * Km - eye(4)).is_zero_matrix)
npass = sum(1 for _, cc in checks if cc)
print(f"review_jkflow_positivity: {npass}/{len(checks)} checks pass")
sys.exit(0 if npass == len(checks) else 1)
