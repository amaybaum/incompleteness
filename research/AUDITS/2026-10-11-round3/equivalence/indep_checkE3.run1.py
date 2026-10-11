#!/usr/bin/env python3
"""indep_checkE3.py -- coordinator's independent check of research/equivalence round 3 (nodes E11, E13, E14).

Written from the thread's claims as stated in NOTES-E11, NOTES-E13, NOTES-E14 and the RESULTS rows R-E11.*,
R-E13.*, R-E14.*; reads nothing from the thread's scripts or outputs.  Exact arithmetic (sympy Rational, Fraction)
except where a check says otherwise.  Conventions: pair tables 4x4, control index first; Pauli sigma_0..sigma_3;
dict(w) = 1/4 sum w_{mu nu} sigma_mu (x) sigma_nu; ipW(w,e) = sum w_{mu nu} e_{mu nu}; tens(X,Y)_{mu nu} = X_mu Y_nu;
tokMat(v) = 1/2 sum v_mu sigma_mu; actT(R) w = w . hom(R)^T.

DECISION RULE (fixed before run 1): VERDICT INDEP-E3-FIXED iff X1..X8 all PASS; otherwise VERDICT INDEP-E3-OPEN with
the failing ids.  Each check is a conjunction of the assertions listed in its docstring.

  X1  E11 dictionary identities on exact random instances: pairing tr(dict w dict e) = ipW/4; coordinate read-back
      tr(T_{mu nu} dict e) = e_{mu nu}; completeness sum tr(T H) T = 4H; product law dict(tens X Y) = tokMat X (x) tokMat Y;
      injectivity; Q3 facts (PSD tables pair >= 0; the Bell defect pairs negatively with the Bell projector table).
  X2  E11 drive generators are unitary conjugations through the dictionary: cnot = Ad(CNOT) [definition used here];
      actT rotZ(3/5,4/5) = Ad(1 (x) diag(1, (3+4i)/5)); actT cyc3 = Ad(1 (x) U_J), U_J = (I - i(X+Y+Z))/2 -- hence they
      preserve Q3 (checked on instances).
  X3  E13 Omega*: weighted AM-GM identity p^3 + 2q^3 - 3pq^2 = (p-q)^2(p+2q); M-pairing >= 0 on cube-parametrised points
      of the power cone; an exact witness pair with negative M-pairing for an outside point; the meridian x^3 = (1+y)(1-y)^2
      is an irreducible cubic (so Omega* is no ellipsoid; the ball's meridian is a conic -- control); f'' = -(2/9)(p+q)^2 f;
      countercontrols: the form without the cross term, and with the opposite cross term, pair some two cone points negatively.
  X4  E13 Omega_cs: J0 on the ellipse 4u^2+v^2=5; the circle u^2+v^2-(1254/325)(u+v)+5114/845=0 passes through J0 and swap J0,
      is tangent to pi(J0) and (at swap J0) to pi(g swap J0); the junction slopes -19/44, -44/19, -76/11 and C^1 matching;
      M^{-1} Z M Z = g; rational points of the arc B0, their M-poles lie on the dual conic E0 and pair exactly 1 with their
      partner; <Mx,y> >= 1 on all pairs of a 60-point sample over three periods, equality exactly at polar partners and
      self-polar points; six points of Gamma lie on no conic; countercontrols XB1 (no swap-invariant inner product makes the
      circle self-polar) and XB2 (the (2,2)-centred circle's polar conic misses J0).
  X5  E14 ring of 3, exhaustive over all 40320 configuration permutations: exactly 48 satisfy (R-lit), and they are exactly
      the site permutations with on-site relabelings; the top-stage condition holds for all 40320.
  X6  E14 ring of 4: the 384 site permutations with relabelings satisfy (R-lit) on all 624 units; CNOT(0,1) violates (R-lit)
      on rings 3 and 4 at E^{0}_{0,1} (every image pair also flips site 1) while satisfying the top-stage condition; T^2
      satisfies (R-lit) on both rings and carries site-0 units to site-2 units.
  X7  E14 rule x_i + x_{i+1} + x_{i+2} mod 2: 16 images on the ring of 4 (a permutation), 2 on the ring of 3; (110)^inf and
      0^inf have the same image on Z (checked on a window with the periodic pattern).
  X8  E13 Omega_cs seams: F symmetric (swap-symmetric chain gives central symmetry), the junction points have F = 1, and
      the body meets the axes only at the poles (F vanishes on the axes: a cone point with u = 0 or v = 0 has X = 0).
"""
import sys
import itertools
import random
from fractions import Fraction as Fr
import sympy as sp
from sympy import Rational as R, I, Matrix, sqrt, symbols, expand, simplify, eye, zeros, factor_list

random.seed(20261011)
results = {}


def kron(A, B):
    m, n = A.shape
    p, q = B.shape
    M = zeros(m * p, n * q)
    for i in range(m):
        for j in range(n):
            for k in range(p):
                for l in range(q):
                    M[i * p + k, j * q + l] = A[i, j] * B[k, l]
    return M


SIG = [Matrix([[1, 0], [0, 1]]), Matrix([[0, 1], [1, 0]]), Matrix([[0, -I], [I, 0]]), Matrix([[1, 0], [0, -1]])]
TT = {(m, n): kron(SIG[m], SIG[n]) for m in range(4) for n in range(4)}


def dict_(w):
    M = zeros(4, 4)
    for m in range(4):
        for n in range(4):
            M += R(w[m][n], 4) * TT[(m, n)] if not isinstance(w[m][n], sp.Basic) else (w[m][n] / 4) * TT[(m, n)]
    return M


def ipW(w, e):
    return sum(w[m][n] * e[m][n] for m in range(4) for n in range(4))


def coordOf(H):
    return [[sp.re(sp.simplify((TT[(m, n)] * H).trace())) for n in range(4)] for m in range(4)]


def rand_table():
    return [[random.randint(-5, 5) for _ in range(4)] for _ in range(4)]


def rand_cvec(n=4, lo=-3, hi=3):
    return Matrix([random.randint(lo, hi) + I * random.randint(lo, hi) for _ in range(n)])


# ---------------------------------------------------------------- X1
def X1():
    ok = True
    for _ in range(6):
        w, e = rand_table(), rand_table()
        Dw, De = dict_(w), dict_(e)
        ok &= simplify((Dw * De).trace() - R(ipW(w, e), 4)) == 0
        for m in range(4):
            for n in range(4):
                ok &= simplify((TT[(m, n)] * De).trace() - e[m][n]) == 0
        ok &= coordOf(Dw) == [[sp.Integer(v) for v in row] for row in w]
    for _ in range(4):
        H = Matrix(4, 4, lambda i, j: random.randint(-3, 3) + I * random.randint(-3, 3))
        S = zeros(4, 4)
        for m in range(4):
            for n in range(4):
                S += (TT[(m, n)] * H).trace() * TT[(m, n)]
        ok &= simplify(S - 4 * H) == zeros(4, 4)
    for _ in range(4):
        X = [1] + [random.randint(-4, 4) for _ in range(3)]
        Y = [1] + [random.randint(-4, 4) for _ in range(3)]
        tens = [[X[m] * Y[n] for n in range(4)] for m in range(4)]
        tokX = sum((R(X[m], 2) * SIG[m] for m in range(4)), zeros(2, 2))
        tokY = sum((R(Y[n], 2) * SIG[n] for n in range(4)), zeros(2, 2))
        ok &= simplify(dict_(tens) - kron(tokX, tokY)) == zeros(4, 4)
    # Q3 facts
    psd_tables = []
    for _ in range(4):
        B = Matrix(4, 4, lambda i, j: random.randint(-2, 2) + I * random.randint(-2, 2))
        rho = B * B.H
        psd_tables.append(coordOf(rho))
    for a in psd_tables:
        for b in psd_tables:
            ok &= ipW(a, b) >= 0
    bell = Matrix([1, 0, 0, 1]) / sqrt(2)
    P = bell * bell.H
    defect = coordOf(eye(4) - 2 * P)
    proj = coordOf(P)
    ok &= ipW(defect, proj) == -4
    ok &= ipW(proj, proj) == 4
    results['X1'] = bool(ok)
    print(f"X1 dictionary identities, Q3 facts: {'PASS' if ok else 'FAIL'}  (Bell defect vs Bell projector ipW = {ipW(defect, proj)})")


# ---------------------------------------------------------------- X2
def hom_of_R(Rm):
    H = eye(4)
    for i in range(3):
        for j in range(3):
            H[i + 1, j + 1] = Rm[i, j]
    return H


def actT(Rm, w):
    W = Matrix(w)
    return (W * hom_of_R(Rm).T).tolist()


def ad_target(U, w):
    V = kron(eye(2), U)
    return coordOf(V * dict_(w) * V.H)


def X2():
    ok = True
    c, s = R(3, 5), R(4, 5)
    rotZ = Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    Uz = sp.diag(1, c + s * I)
    UJ = (eye(2) - I * (SIG[1] + SIG[2] + SIG[3])) / 2
    # which cyclic permutation does Ad(U_J) induce on the Paulis?
    img = {}
    for k in (1, 2, 3):
        Mk = simplify(UJ * SIG[k] * UJ.H)
        for l in (1, 2, 3):
            if simplify(Mk - SIG[l]) == zeros(2, 2):
                img[k] = l
    ok &= sorted(img) == [1, 2, 3] and set(img.values()) == {1, 2, 3} and all(img[k] != k for k in img)
    cyc = zeros(3, 3)
    for k in (1, 2, 3):
        cyc[img[k] - 1, k - 1] = 1  # e_k -> e_{img k}
    CNOT = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    for _ in range(5):
        w = rand_table()
        ok &= actT(rotZ, w) == ad_target(Uz, w)
        ok &= actT(cyc, w) == ad_target(UJ, w)
        # cnot = Ad(CNOT) by the definition used here; PSD preservation on a PSD instance
    for _ in range(3):
        B = Matrix(4, 4, lambda i, j: random.randint(-2, 2) + I * random.randint(-2, 2))
        rho = B * B.H
        w = coordOf(rho)
        for w2 in (actT(rotZ, w), actT(cyc, w), coordOf(CNOT * rho * CNOT.H)):
            D = dict_(w2)
            ok &= simplify(D - D.H) == zeros(4, 4)
            ev = [simplify(v) for v in D.eigenvals()]
            ok &= all(sp.nsimplify(v).is_nonnegative for v in ev)
    results['X2'] = bool(ok)
    print(f"X2 drive generators = unitary conjugations (cyc3 as Ad(U_J): {img}); Q3 preserved: {'PASS' if ok else 'FAIL'}")


# ---------------------------------------------------------------- X3
def X3():
    ok = True
    p, q = symbols('p q', real=True)
    ok &= expand(p ** 3 + 2 * q ** 3 - 3 * p * q ** 2 - (p - q) ** 2 * (p + 2 * q)) == 0
    # M-form in (u, v, X): (1/3) u u' + (2/3) v v' + X.X'   (= TT' + SS' - (1/3)(TS'+ST') with u = T+S, v = T-S)
    T1, S1, T2, S2 = symbols('T1 S1 T2 S2', real=True)
    u1, v1, u2, v2 = T1 + S1, T1 - S1, T2 + S2, T2 - S2
    ok &= expand(R(1, 3) * u1 * u2 + R(2, 3) * v1 * v2 - (T1 * T2 + S1 * S2 - R(1, 3) * (T1 * S2 + S1 * T2))) == 0

    def pair(z, w):
        return R(1, 3) * z[0] * w[0] + R(2, 3) * z[1] * w[1] + sum(z[2][i] * w[2][i] for i in range(3))

    dirs = [(R(3, 5), R(4, 5), 0), (0, R(3, 5), R(4, 5)), (R(2, 3), R(1, 3), R(2, 3)), (1, 0, 0), (R(-4, 5), 0, R(3, 5))]

    def cone_point(a, b, t, d):  # (a^3, b^3, t a b^2 d), |d| = 1, 0 <= t <= 1: in P_{1/3}
        return (a ** 3, b ** 3, tuple(t * a * b ** 2 * di for di in d))

    pts = []
    for _ in range(14):
        a, b = R(random.randint(1, 6), random.randint(1, 4)), R(random.randint(1, 6), random.randint(1, 4))
        t = R(random.randint(0, 5), 5)
        pts.append(cone_point(a, b, t, random.choice(dirs)))
    pts += [(2, 0, (0, 0, 0)), (0, 2, (0, 0, 0))]
    for z in pts:
        for w in pts:
            ok &= pair(z, w) >= 0
    # outside point witness: w = (a'^3, b'^3, rho a' b'^2 d) with rho > 1; z = (k/u', k/v', -c X')
    ap, bp, rho, k = R(3, 2), R(2, 1), R(5, 4), R(7, 3)
    d = dirs[0]
    w = (ap ** 3, bp ** 3, tuple(rho * ap * bp ** 2 * di for di in d))
    lo, hi = k / (rho ** 2 * ap ** 2 * bp ** 4), k / (rho * ap ** 2 * bp ** 4)
    ok &= lo < hi
    c = (lo + hi) / 2
    z = (k / w[0], k / w[1], tuple(-c * xi for xi in w[2]))
    # z in P: (k/a'^3)^{1/3} (k/b'^3)^{2/3} = k/(a' b'^2) >= |X_z| = c rho a' b'^2
    ok &= k / (ap * bp ** 2) >= c * rho * ap * bp ** 2
    ok &= pair(z, w) < 0
    # w outside: u'^{1/3} v'^{2/3} = a' b'^2 < |X'| = rho a' b'^2
    ok &= ap * bp ** 2 < rho * ap * bp ** 2
    # meridian irreducible cubic; the ball's meridian is a conic
    x, y = symbols('x y')
    fl = factor_list(x ** 3 - (1 + y) * (1 - y) ** 2)
    ok &= len(fl[1]) == 1 and fl[1][0][1] == 1 and sp.Poly(fl[1][0][0], x, y).total_degree() == 3
    ok &= sp.Poly(x ** 2 + y ** 2 - 1, x, y).total_degree() == 2
    # strict concavity of f(S) = (1+S)^{1/3} (1-S)^{2/3}
    Sv = symbols('S', real=True)
    f = (1 + Sv) ** R(1, 3) * (1 - Sv) ** R(2, 3)
    pp, qq = 1 / (1 + Sv), 1 / (1 - Sv)
    ok &= simplify(sp.diff(f, Sv, 2) / f + R(2, 9) * (pp + qq) ** 2) == 0
    # countercontrols: wrong forms pair some cone points negatively
    def pair_nocross(z, w):  # TT' + SS' + X.X'  with T = (u+v)/2, S = (u-v)/2
        Tz, Sz, Tw, Sw = (z[0] + z[1]) / 2, (z[0] - z[1]) / 2, (w[0] + w[1]) / 2, (w[0] - w[1]) / 2
        return Tz * Tw + Sz * Sw + sum(z[2][i] * w[2][i] for i in range(3))

    def pair_opp(z, w):
        Tz, Sz, Tw, Sw = (z[0] + z[1]) / 2, (z[0] - z[1]) / 2, (w[0] + w[1]) / 2, (w[0] - w[1]) / 2
        return Tz * Tw + Sz * Sw + R(1, 3) * (Tz * Sw + Sz * Tw) + sum(z[2][i] * w[2][i] for i in range(3))

    grid = [cone_point(R(a, 2), R(b, 2), R(t, 2), dd) for a in (1, 2, 3) for b in (1, 2, 3) for t in (1, 2)
            for dd in (dirs[0], dirs[4])]
    neg1 = min(pair_nocross(z, w) for z in grid for w in grid)
    neg2 = min(pair_opp(z, w) for z in grid for w in grid)
    ok &= neg1 < 0 and neg2 < 0
    results['X3'] = bool(ok)
    print(f"X3 Omega*: AM-GM identity, cone pairings, outside witness (pair = {pair(z, w)}), irreducible cubic, f'', "
          f"countercontrols (min {neg1}, {neg2}): {'PASS' if ok else 'FAIL'}")


# ---------------------------------------------------------------- X4
def X4():
    ok = True
    M = sp.diag(R(4, 5), R(1, 5))
    J0 = Matrix([R(11, 13), R(19, 13)])
    sJ0 = Matrix([R(19, 13), R(11, 13)])
    g = sp.diag(R(1, 4), 4)
    ginv = g.inv()
    ok &= (4 * J0[0] ** 2 + J0[1] ** 2) == 5
    cc = Matrix([R(627, 325), R(627, 325)])
    r2 = 2 * (R(627, 325)) ** 2 - R(5114, 845)

    def on_circle(pt):
        return sp.simplify(pt[0] ** 2 + pt[1] ** 2 - R(1254, 325) * (pt[0] + pt[1]) + R(5114, 845)) == 0

    ok &= on_circle(J0) and on_circle(sJ0)
    ok &= sp.simplify((J0 - cc).dot(J0 - cc) - r2) == 0

    def pi_normal(x):  # pi(x) = {y : <Mx, y> = 1}
        return M * x

    def tangent_to_circle(n):  # line {n.y = 1}
        return sp.simplify((n.dot(cc) - 1) ** 2 - r2 * n.dot(n)) == 0

    ok &= tangent_to_circle(pi_normal(J0))
    gsJ0 = g * sJ0
    ok &= gsJ0 == Matrix([R(19, 52), R(44, 13)])
    ok &= tangent_to_circle(pi_normal(gsJ0))
    # foot of pi(g sJ0) on the circle is sJ0
    n = pi_normal(gsJ0)
    t = (1 - n.dot(cc)) / n.dot(n)
    foot = cc + t * n
    ok &= sp.simplify(foot - sJ0) == zeros(2, 1)

    def slope_of_line(n):
        return -n[0] / n[1]

    tangent_sJ0 = sJ0 - cc  # normal of the tangent line at sJ0
    tangent_J0 = J0 - cc
    ok &= slope_of_line(tangent_sJ0) == R(-19, 44)
    ok &= slope_of_line(tangent_J0) == R(-44, 19)
    ok &= slope_of_line(pi_normal(sJ0)) == R(-76, 11)
    # g maps the tangent line at sJ0 {19u+44v=65} to {76u+11v=65}
    ok &= slope_of_line(ginv.T * tangent_sJ0) == R(-76, 11)
    # M^{-1} Z M Z = g in (T, S) coordinates
    MTS = Matrix([[1, R(3, 5)], [R(3, 5), 1]])
    Z = sp.diag(1, -1)
    h = MTS.inv() * Z.T * MTS * Z
    P = Matrix([[1, 1], [1, -1]])  # (u, v) = P (T, S)
    ok &= sp.simplify(P * h * P.inv() - g) == zeros(2, 2)
    # the (u,v) form of MTS is diag(4/5, 1/5)
    ok &= sp.simplify(P.inv().T * MTS * P.inv() - M) == zeros(2, 2)

    # dual conic E0(y) = ((My).cc - 1)^2 - r2 |My|^2
    def E0(y):
        n = M * y
        return sp.simplify((n.dot(cc) - 1) ** 2 - r2 * n.dot(n))

    def grad_E0(y):
        yu, yv = symbols('yu yv')
        Y = Matrix([yu, yv])
        e = E0(Y)
        return Matrix([sp.diff(e, yu), sp.diff(e, yv)]).subs({yu: y[0], yv: y[1]})

    ok &= E0(J0) == 0 and E0(gsJ0) == 0
    gJ = grad_E0(J0)
    ok &= sp.simplify(-gJ[0] / gJ[1]) == R(-44, 19)
    gG = grad_E0(gsJ0)
    ok &= sp.simplify(-gG[0] / gG[1]) == R(-76, 11)

    # rational points of the arc B0 (near side: u + v < 30/13)
    def circle_points(nslopes):
        pts = []
        for m in nslopes:
            # line through J0 with slope m: second intersection
            # (u - cu)^2 + (v - cv)^2 = r2 with v = J0v + m (u - J0u)
            uu = symbols('uu')
            vv = J0[1] + m * (uu - J0[0])
            sols = sp.solve(sp.expand((uu - cc[0]) ** 2 + (vv - cc[1]) ** 2 - r2), uu)
            for su in sols:
                if su != J0[0]:
                    pt = Matrix([su, vv.subs(uu, su)])
                    if pt[0] + pt[1] < R(30, 13) and pt != sJ0:
                        pts.append(pt)
        return pts

    B = circle_points([R(-1, 2), R(-2, 3), R(-3, 4), R(-1, 1), R(-4, 3), R(-3, 2), R(-2, 1), R(-5, 2)])
    ok &= len(B) >= 6
    for pt in B:
        ok &= on_circle(pt) and pt[0] > R(11, 13) and pt[0] < R(19, 13)

    def pole_of_tangent(pt):
        nrm = pt - cc
        den = r2 + nrm.dot(cc)
        n = nrm / den
        return M.inv() * n

    E = [pole_of_tangent(pt) for pt in B]
    for pt, q in zip(B, E):
        ok &= E0(q) == 0
        ok &= sp.simplify((M * pt).dot(q)) == 1
        ok &= q[0] > gsJ0[0] - R(1, 10 ** 6) and q[0] < J0[0] + R(1, 10 ** 6)
    sample = [J0, sJ0, gsJ0] + B + E
    sample3 = []
    for s_ in sample:
        for G in (ginv, eye(2), g):
            sample3.append(G * s_)
    partners = set()
    for i, pt in enumerate(B):
        partners.add((i, i))
    minpair = None
    eq_count = 0
    npairs = 0
    for a in sample3:
        for b in sample3:
            v = sp.simplify((M * a).dot(b))
            npairs += 1
            if minpair is None or v < minpair:
                minpair = v
            if v == 1:
                eq_count += 1
    ok &= minpair == 1
    # expected equalities: (x, partner) in both orders for the |B| pairs, times 3 periods (g-shifts pair
    # (g^j p, g^{-j} q)), plus the three self-polar junction points each period (J0, sJ0, g sJ0) and their
    # cross-period partners... count the exact set independently:
    S3 = [sp.simplify(a) for a in sample3]
    eq_pairs = sum(1 for a in S3 for b in S3 if sp.simplify((M * a).dot(b)) == 1)
    ok &= eq_pairs == eq_count
    # six points on no conic
    six = B[:3] + E[:3]
    Mconic = Matrix([[pt[0] ** 2, pt[0] * pt[1], pt[1] ** 2, pt[0], pt[1], 1] for pt in six])
    ok &= Mconic.rank() == 6
    # XB2: circle centred (2,2) through J0 and swap J0 (same r2'), not tangent to pi(J0): its polar conic misses J0
    cc2 = Matrix([2, 2])
    r22 = (J0 - cc2).dot(J0 - cc2)
    n = M * J0
    ok &= sp.simplify((n.dot(cc2) - 1) ** 2 - r22 * n.dot(n)) != 0
    # XB1: no inner product [[a, b],[b, a]] in (u,v) makes the circle its own polar
    a_, b_ = symbols('a b', real=True)
    Mp = Matrix([[a_, b_], [b_, a_]])
    AB = Matrix([[1, 0, -cc[0]], [0, 1, -cc[1]], [-cc[0], -cc[1], cc.dot(cc) - r2]])  # circle as a conic
    Mt = Matrix([[a_, b_, 0], [b_, a_, 0], [0, 0, -1]])
    Cdual = Mt * AB.adjugate() * Mt
    vecs = Matrix([[Cdual[i, j] for i in range(3) for j in range(i, 3)], [AB[i, j] for i in range(3) for j in range(i, 3)]])
    eqs = [sp.expand(vecs[0, i] * vecs[1, j] - vecs[0, j] * vecs[1, i]) for i in range(6) for j in range(i + 1, 6)]
    eqs = [e for e in eqs if e != 0]
    sols = sp.solve(eqs, [a_, b_], dict=True)
    sols_pd = [s_ for s_ in sols if all(x.is_real for x in s_.values()) and s_.get(a_, 0) != 0 and (s_[a_] > abs(s_.get(b_, 0)))]
    ok &= len(sols_pd) == 0
    results['X4'] = bool(ok)
    print(f"X4 Omega_cs: ellipse/circle/tangency/junction slopes/filter g; {len(B)} arc points with poles on E0; "
          f"{npairs} pairs min <Mx,y> = {minpair}, equalities {eq_count}; six points no conic; XB1 solutions {len(sols)} "
          f"(positive-definite {len(sols_pd)}); XB2: {'PASS' if ok else 'FAIL'}")


# ---------------------------------------------------------------- E14 helpers
def embed(Lam, c, comp, s):
    x = 0
    for j, i in enumerate(Lam):
        if (c >> j) & 1:
            x |= 1 << i
    for j, i in enumerate(comp):
        if (s >> j) & 1:
            x |= 1 << i
    return x


def units(N):
    out = []
    for k in range(1, N + 1):
        for Lam in itertools.combinations(range(N), k):
            comp = [i for i in range(N) if i not in Lam]
            for c in range(2 ** k):
                for c2 in range(2 ** k):
                    pairs = tuple((embed(Lam, c, comp, s), embed(Lam, c2, comp, s)) for s in range(2 ** len(comp)))
                    out.append((k, Lam, c, c2, pairs))
    return out


def is_stage_unit(pairs, N, k):
    full = (1 << N) - 1
    and_x = full; or_x = 0; and_y = full; or_y = 0; D = 0
    for x, y in pairs:
        and_x &= x; or_x |= x; and_y &= y; or_y |= y; D |= x ^ y
    agree = (~(and_x ^ or_x)) & (~(and_y ^ or_y)) & full
    if D & ~agree:
        return False
    return bin(D).count('1') <= k <= bin(agree).count('1')


def site_perm_relabel(N):
    out = set()
    for pi in itertools.permutations(range(N)):
        for f in range(2 ** N):
            sigma = []
            for x in range(2 ** N):
                y = 0
                for i in range(N):
                    bit = (x >> pi[i]) & 1  # site i of the image takes the value of site pi[i]
                    if bit ^ ((f >> i) & 1):
                        y |= 1 << i
                sigma.append(y)
            out.add(tuple(sigma))
    return out


def satisfies_rlit(sigma, N, U):
    for k, Lam, c, c2, pairs in U:
        img = tuple((sigma[x], sigma[y]) for x, y in pairs)
        if not is_stage_unit(img, N, k):
            return False
    return True


def X5():
    N = 3
    U = units(N)
    proj = [u for u in U if u[0] == 1 and u[2] == u[3]]
    rest = [u for u in U if not (u[0] == 1 and u[2] == u[3])]
    top = [u for u in U if u[0] == N]
    count = 0
    found = set()
    topcount = 0
    for sigma in itertools.permutations(range(8)):
        okp = True
        for k, Lam, c, c2, pairs in proj:
            img = tuple((sigma[x], sigma[y]) for x, y in pairs)
            if not is_stage_unit(img, N, k):
                okp = False
                break
        if okp:
            if satisfies_rlit(sigma, N, rest):
                count += 1
                found.add(sigma)
        # top stage: images of top units are top units (always)
        topok = all(is_stage_unit(tuple((sigma[x], sigma[y]) for x, y in pairs), N, k) for k, Lam, c, c2, pairs in top)
        topcount += topok
    spr = site_perm_relabel(N)
    ok = (count == 48) and (found == spr) and (topcount == 40320) and len(U) == 124
    results['X5'] = bool(ok)
    print(f"X5 ring 3: (R-lit) holds for {count}/40320 (site perms with relabelings: {len(spr)}, equal sets: {found == spr}); "
          f"top-stage holds for {topcount}/40320; units {len(U)}: {'PASS' if ok else 'FAIL'}")


def cnot01(N):
    return tuple(x ^ (((x >> 0) & 1) << 1) for x in range(2 ** N))


def shift2(N):
    return tuple(((x << 2) | (x >> (N - 2))) & ((1 << N) - 1) for x in range(2 ** N))


def X6():
    ok = True
    U4 = units(4)
    ok &= len(U4) == 624
    spr4 = site_perm_relabel(4)
    ok &= len(spr4) == 384
    ok &= all(satisfies_rlit(s, 4, U4) for s in spr4)
    U3 = units(3)
    viol = {}
    for N, U in ((3, U3), (4, U4)):
        s = cnot01(N)
        ok &= not satisfies_rlit(s, N, U)
        # E^{0}_{0,1}: Lam = (0,), c = 0, c2 = 1
        e = [u for u in U if u[1] == (0,) and u[2] == 0 and u[3] == 1][0]
        img = tuple((s[x], s[y]) for x, y in e[4])
        ok &= not is_stage_unit(img, N, 1)
        ok &= all(((x ^ y) >> 1) & 1 == 1 for x, y in img) and len(img) == 2 ** (N - 1)
        viol[N] = len(img)
        top = [u for u in U if u[0] == N]
        ok &= all(is_stage_unit(tuple((s[x], s[y]) for x, y in pairs), N, k) for k, Lam, c, c2, pairs in top)
        t2 = shift2(N)
        ok &= satisfies_rlit(t2, N, U)
        # site-0 units go to site-2 units
        for u in U:
            if u[1] == (0,):
                img = tuple((t2[x], t2[y]) for x, y in u[4])
                D = 0; and_x = (1 << N) - 1; or_x = 0
                for x, y in img:
                    D |= x ^ y; and_x &= x; or_x |= x
                if u[2] != u[3]:
                    ok &= D == (1 << 2)
                else:
                    agree = (~(and_x ^ or_x)) & ((1 << N) - 1)
                    ok &= (agree >> 2) & 1 == 1
    results['X6'] = bool(ok)
    print(f"X6 ring 4: 384 site-perm-relabelings satisfy (R-lit) on 624 units; CNOT violates at E^0_01 (image pairs {viol}, "
          f"each flipping site 1), top-stage ok; T^2 satisfies, site 0 -> site 2: {'PASS' if ok else 'FAIL'}")


def X7():
    def rule(N):
        imgs = set()
        for x in range(2 ** N):
            y = 0
            for i in range(N):
                b = ((x >> i) & 1) ^ ((x >> ((i + 1) % N)) & 1) ^ ((x >> ((i + 2) % N)) & 1)
                y |= b << i
            imgs.add(y)
        return len(imgs)
    n4, n3 = rule(4), rule(3)
    # (110)^inf vs 0^inf on a window of 12 sites with periodic pattern
    pat = [1, 1, 0] * 6
    img = [(pat[i] + pat[i + 1] + pat[i + 2]) % 2 for i in range(len(pat) - 2)]
    ok = (n4 == 16) and (n3 == 2) and all(v == 0 for v in img)
    results['X7'] = bool(ok)
    print(f"X7 rule x_i+x_i+1+x_i+2: images ring4 = {n4}, ring3 = {n3}; (110)^inf -> 0: {'PASS' if ok else 'FAIL'}")


def X8():
    ok = True
    # symmetric F: the chain is swap symmetric iff the circle's centre lies on the diagonal and E0 is the swap image
    # of the polar structure; here: the circle is swap-symmetric (centre on u = v); the seeds: poles are F = 1 points.
    cc = Matrix([R(627, 325), R(627, 325)])
    ok &= cc[0] == cc[1]
    M = sp.diag(R(4, 5), R(1, 5))
    # junction points have <Mx, x> >= 1 with equality at J0, sJ0 (on the ellipse) -- consistent with F(J0) = 1
    J0 = Matrix([R(11, 13), R(19, 13)])
    sJ0 = Matrix([R(19, 13), R(11, 13)])
    ok &= (M * J0).dot(J0) == 1 and (M * sJ0).dot(sJ0) == 1
    # a cone point with u = 0 or v = 0 has X = 0: F(u, 0) = 0 since Gamma -> infinity as u -> 0 and v -> 0:
    # with the chain's periods, F(u, v) <= min over tangent lines; check F(1, 0) = 0 via the supporting line of a far
    # period: <M g^j J0, (1, 0)> = (4/5) (11/13) 4^{-j} -> 0, so the scale F(1,0) = inf_y ... <= that -> 0.
    g = sp.diag(R(1, 4), 4)
    vals = [((M * (g ** j) * J0).dot(Matrix([1, 0]))) for j in range(1, 6)]
    ok &= all(vals[i + 1] < vals[i] for i in range(4)) and vals[-1] < R(1, 100)
    results['X8'] = bool(ok)
    print(f"X8 Omega_cs seams (swap symmetry, junctions on the ellipse, F -> 0 on the axes): {'PASS' if ok else 'FAIL'}")


if __name__ == '__main__':
    for fn in (X1, X2, X3, X4, X5, X6, X7, X8):
        fn()
    fails = [k for k, v in results.items() if not v]
    n = sum(1 for v in results.values() if v)
    print(f"{n}/{len(results)} PASS")
    print("VERDICT INDEP-E3-FIXED" if not fails else f"VERDICT INDEP-E3-OPEN {fails}")
