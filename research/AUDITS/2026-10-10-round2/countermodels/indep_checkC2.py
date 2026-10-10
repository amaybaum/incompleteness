#!/usr/bin/env python3
"""Coordinator's independent check of the research/countermodels thread's round-2 exact claims (branch head e6d42cab;
NOTES-C7, C8, C9, C10).  Own table-level code (conventions of indep_checkC.py: tables 4x4, index 0 the unit, defects
z_s = (E00 + s1 E13 + s2 E22 - s1 s2 E31)/4, psi_s the (-1/8)-eigenvector of pauliW(z_s), real with entries +-1/2;
psi_1..psi_4 = psi_s for s in the order (1,1), (1,-1), (-1,1), (-1,-1); matrix normalization d_g = I - 2 g g^dag,
pairing tr(XY); `psi coordinates` = coordinates in the orthonormal basis psi_1..psi_4; Fix = matrices diagonal in it,
d in R^4; R = {d : d_s <= sum d/2}, O = cone{e_s + e_t}, Circ = {d : sum d/2 >= |d - (sum d/4) 1|}).  Reads nothing.
Run: python3 -I -B indep_checkC2.py
DECISION RULE (fixed before the first run): CONFIRMED/MISMATCH per line; INDEP-C2-FIXED iff all CONFIRMED.
 X0 conventions: psi_s real orthonormal with entries +-1/2; cos t psi_1 + sin t psi_3 is maximally entangled for all t
    (symbolic), as is (3 psi_1 + 4 i psi_2)/5; d_{psi_s} = 8 pauliW(z_s); Circ is an isometric image of the Lorentz cone
    (t, u) -> (t/2) 1 + u with <d, d'> = t t' + <u, u'>, hence self-dual.
 X1 (C7 W1, CC-R) y_d = (-2, 12, 6, 4)/5 lies on the boundary of Circ, its dual ray y_d' = (12, -2, 4, 6)/5 pairs to 0
    with it and has the opposite deviation vector; the profile p = (0, 1, 1/4, 0) of v = psi_2 + psi_3/2 is outside Circ,
    c0 = y_d - p = (-2/5, 7/5, 19/20, 4/5) is interior to Circ; y = P_v + diag(c0) has pi(y) = y_d and
    <psi_2| y |psi_3> = 1/2 (not diagonal), and y_d has a negative entry.  CC-R: for d = (1 - 2 e_s) - p the three facet
    slacks of R at t != s sum to -sum p/2 - p_s (symbolic), so no p >= 0, p != 0 keeps d in R.
 X2 (C7 W3, W4) v = 5 psi_1 + 3 psi_2 + 3 psi_3 + psi_4: profile (25, 9, 9, 1)/44 in Circ, not in O; u = (psi_1 - psi_2 -
    psi_3 + psi_4)/2, w = P_u + diag(-1, 1, 1, 1)/2: pi(w) in Circ, tr(w P_v) = -3, tr(P_u sigma.diag) = 1/2 for all
    coordinate permutations sigma, <diag, sigma diag> in {0, 4}.  y5 = u5 u5^dag + 8 diag(-1, 1, 1, 1), u5 = 3 psi_1 +
    psi_2 + psi_3 + psi_4: pi(y5) = (1, 9, 9, 9), x^dag y5 x = -12 at x = 3 psi_1 - psi_2 - psi_3 - psi_4, the table with
    coefficient 6 is PSD (exact eigenvalues) and with 8 is not; the orbit bound: for every sigma in S4,
    8 (u5^dag (sigma.diag) u5 + (sigma u5)^dag diag (sigma u5)) + 64 <diag, sigma diag> = 160.
 X3 (C7 W5) the Bell-circle certificate: y_i = v_i v_i^dag + (189/1000) d_{g_i} + I/1000 in psi coordinates with
    d_g = Pperp - cos 2t sz - sin 2t sx (checked against I - 2 g g^dag symbolically), n_i = (cos 2t_i, sin 2t_i) unit
    (Pythagorean), tr(y_i d_g) = A_i - B_i cos 2t - C_i sin 2t with A_i > 0 and A_i^2 > B_i^2 + C_i^2 (strict membership
    in Z_circ*), and tr(y1 y2) = -475586012673053754301/30445958586078125000000 < 0.  B5: (psi_1 -+ i psi_3)/sqrt 2 and
    |1+>, |0-> are orthonormal pairs, so a unitary carries the circle onto the C2 circle.
 X4 (C8) the witness construction on my own line triple: g1 = psi_1, g2 = (4 psi_1 + 3 psi_3)/5, g3 = (3 psi_1 - 4 psi_3)/5
    (all maximally entangled; c = 16/25, c3 = 9/25), e = psi_2, eps = 9/10: v = g1 + eps e, lam = (1 - eps^2)/(4c) = 19/256,
    x = g2 - (<g1|g2>/eps) e, y = v v^dag + lam d_2: <y, d_1> = 0, <y, d_2> > 0, <y, d_3> > 0, x^dag y x = -323/20736 < 0,
    <d_k, d_1> = 4 c_k > 0 for k = 2, 3 (so mu = 0 in any decomposition y = q + sum mu_k d_k with q in Q3 n Z*, hence y
    not in K(Z)); y in Q3 + cone Z and in Z*, hence in K(Z)*.  Countercontrols: eps = 1/2 gives <v v^dag, d_2> = -3/100;
    for Z_F every <d_k, d_1> = 0 (k != 1), so the lemma's y would be v v^dag, PSD, and (L3) cannot hold.
 X5 (C9.1) det Hess N = 2304 s^2 |x|^6 for N = |x|^4 + s^4; det Hess(N o A) = det(A)^2 det(Hess N)(A w) on a rational
    instance; the Hessian of |x|^2 has rank 3 (irreducible quadratic form); a rational rotation (3/5, 4/5) in the
    x1 x2-plane and s -> -s preserve N; the shear x1 -> x1 + s, the scaling s -> 2 s and an x1-s rotation do not.
 X6 (C10.1) b1 = C2(1), b2 = C2(-1), b3 = |0+>, b4 = |1->: orthonormal; b1, b2 maximally entangled, b3, b4 products;
    CNOT = I - 2 |1-><1-| is diagonal in this basis (eigenvalues 1, 1, 1, -1); the six weight differences of
    (a, b, a+b, 0) are nonzero forms; the coefficient matrix of b1 has M M^dag = I/2; z = (I - 2 P_{b1})/8 commutes
    with every P_k and with CNOT; the cone C = cone{f, e2, e3, e4, e1+e2, e1+e3, e1+e4}, f = (-1, 1, 1, 1), has exactly
    these seven extreme rays and its facet normals are the same seven vectors (so C* = C), C != R^4_+; R^4_+ n f* has
    extreme rays e2, e3, e4, e1+e2, e1+e3, e1+e4 exactly.  Countercontrols: the product basis |00>, |01>, |1+>, |1-> has
    no entangled member; with c = 5/2 the table I - c P_{b1} pairs negatively with a product state.
"""
import itertools
import sympy as sp
from sympy import Matrix, Rational as Q, I, eye, zeros, sqrt, simplify, expand, conjugate, kronecker_product as kron
from sympy import sin, cos, symbols
R = []
def rec(cid, ok, text, detail=""):
    ok = bool(ok); R.append(ok)
    print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} {text}" + (f" -- {detail}" if detail else ""), flush=True)
I2 = eye(2); SX = Matrix([[0, 1], [1, 0]]); SY = Matrix([[0, -I], [I, 0]]); SZ = Matrix([[1, 0], [0, -1]])
SG = [I2, SX, SY, SZ]; KR = {(m, n): kron(SG[m], SG[n]) for m in range(4) for n in range(4)}
def pauliW(w): return sum((w[m, n] * KR[(m, n)] for m in range(4) for n in range(4) if w[m, n] != 0), zeros(4, 4)) / 4
def tab(M):
    out = zeros(4, 4)
    for m in range(4):
        for n in range(4):
            e = expand((KR[(m, n)] * M).trace())
            if not e.is_Rational: e = sp.nsimplify(simplify(e))
            out[m, n] = e
    return out
def E(m, n): B = zeros(4, 4); B[m, n] = 1; return B
def zdef(s1, s2): return (E(0, 0) + s1 * E(1, 3) + s2 * E(2, 2) - s1 * s2 * E(3, 1)) / 4
SS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]; ZF = {s: zdef(*s) for s in SS}
def negvec(w):
    v = (pauliW(w) + eye(4) / 8).nullspace()[0]; return v / sqrt(expand((v.H * v)[0]))
PSI = [negvec(ZF[s]) for s in SS]                        # psi_1..psi_4 in the computational basis
PSIM = Matrix.hstack(*PSI)                               # columns psi_k; comp = PSIM * (psi coords)
def to_comp(Apsi): return PSIM * Apsi * PSIM.H
def red_A(g):
    rho = g * g.H; return Matrix(2, 2, lambda i, j: sum(rho[2 * i + k, 2 * j + k] for k in range(2)))
def max_ent(g): return expand(red_A(g) - eye(2) / 2 * expand((g.H * g)[0])) == zeros(2, 2)
def diagpsi(d): return Matrix.diag(*d)                   # in psi coordinates
def pi_fix(Apsi): return [Apsi[k, k] for k in range(4)]
def tr(A, B): return expand((A * B).trace())
def in_circ(d, strict=False):
    S = sum(d); m = S / 4; dev = [x - m for x in d]; n2 = sum(x * x for x in dev)
    return (S / 2) ** 2 > n2 if strict else ((S / 2) ** 2 >= n2 and S >= 0)
def in_R(d): S = sum(d); return all(x <= S / 2 for x in d)
def in_O(d): S = sum(d); return all(x >= 0 for x in d) and all(x <= S / 2 for x in d)

print("== X0 conventions")
t = symbols('t', real=True)
ok_psi = all(all(abs(x) == Q(1, 2) and x.is_real for x in p) for p in PSI) and simplify(PSIM.H * PSIM - eye(4)) == zeros(4, 4)
g_t = cos(t) * PSI[0] + sin(t) * PSI[2]
ok_circle = simplify(red_A(g_t) - eye(2) / 2) == zeros(2, 2)
ok_34 = max_ent((3 * PSI[0] + 4 * I * PSI[1]) / 5)
ok_dz = all(simplify(eye(4) - 2 * PSI[k] * PSI[k].H - 8 * pauliW(ZF[SS[k]])) == zeros(4, 4) for k in range(4))
tt, t2, u1, u2, u3, w1, w2, w3 = symbols('tt t2 u1 u2 u3 w1 w2 w3', real=True)
one = Matrix([1, 1, 1, 1]); B3 = Matrix([[1, -1, 0, 0], [1, 1, -2, 0], [1, 1, 1, -3]]).T   # columns: a basis of 1^perp
Bo = Matrix.hstack(*[B3[:, k] / sqrt((B3[:, k].T * B3[:, k])[0]) for k in range(3)])      # orthonormal basis of 1^perp
d1 = (tt / 2) * one + Bo * Matrix([u1, u2, u3]); d2 = (t2 / 2) * one + Bo * Matrix([w1, w2, w3])
ok_iso = simplify((d1.T * d2)[0] - (tt * t2 + u1 * w1 + u2 * w2 + u3 * w3)) == 0 and simplify(Bo.T * one) == zeros(3, 1)
rec('X0', ok_psi and ok_circle and ok_34 and ok_dz and ok_iso,
    'psi_s real orthonormal entries +-1/2; cos t psi_1 + sin t psi_3 maximally entangled (symbolic); (3 psi_1 + 4i psi_2)/5 too; d_{psi_s} = 8 pauliW(z_s); (t, u) -> (t/2) 1 + u is an isometry onto R^4 (Circ = Lorentz cone, self-dual)')

print("== X1 C7 W1 witness and CC-R")
yd = [Q(-2, 5), Q(12, 5), Q(6, 5), Q(4, 5)]; ydp = [Q(12, 5), Q(-2, 5), Q(4, 5), Q(6, 5)]
S = sum(yd); dev = [x - S / 4 for x in yd]; devp = [x - sum(ydp) / 4 for x in ydp]
bdry = (S / 2) ** 2 == sum(x * x for x in dev) and S > 0
dual0 = sum(a * b for a, b in zip(yd, ydp)) == 0 and all(a == -b for a, b in zip(dev, devp)) and in_circ(ydp)
p = [0, 1, Q(1, 4), 0]; c0 = [a - b for a, b in zip(yd, p)]
v = PSI[1] + PSI[2] / 2
prof_v = [expand(abs((PSI[k].H * v)[0]) ** 2) for k in range(4)]
y = PSIM.H * (v * v.H) * PSIM + diagpsi(c0)              # in psi coordinates
ok_w1 = (prof_v == p and (not in_circ(p)) and in_circ(c0, strict=True) and c0 == [Q(-2, 5), Q(7, 5), Q(19, 20), Q(4, 5)]
         and pi_fix(y) == yd and y[1, 2] == Q(1, 2) and min(yd) < 0)
ps = symbols('p1 p2 p3 p4', real=True)
slack_ok = True
for s_idx in range(4):
    d = [1 - 2 * (k == s_idx) - ps[k] for k in range(4)]; Sd = sum(d)
    slacks = [Sd / 2 - d[k] for k in range(4) if k != s_idx]
    slack_ok = slack_ok and expand(sum(slacks) + sum(ps) / 2 + ps[s_idx]) == 0
ok_R = in_R([1, -1, 1, 1]) and all(in_R([1 - 2 * (k == 0) for k in range(4)]) for _ in [0])
rec('X1', ok_w1 and slack_ok and ok_R,
    'y_d on the boundary of Circ, dual ray y_d\' pairs to 0 with opposite deviation; p outside Circ, c0 interior; y = P_v + diag(c0): pi(y) = y_d, <psi_2|y|psi_3> = 1/2, y_d has a negative entry; CC-R slack identity -sum p/2 - p_s',
    'profile of v %s, c0 %s' % ([str(x) for x in prof_v], [str(x) for x in c0]))

print("== X2 C7 W3, W4 numbers")
v5 = 5 * PSI[0] + 3 * PSI[1] + 3 * PSI[2] + PSI[3]
Pv = PSIM.H * (v5 * v5.H) * PSIM
prof5 = [Pv[k, k] / tr(Pv, eye(4)) for k in range(4)]
u = (PSI[0] - PSI[1] - PSI[2] + PSI[3]) / 2
Pu = PSIM.H * (u * u.H) * PSIM
dg = diagpsi([-1, 1, 1, 1])
w = Pu + dg / 2
ok_w3 = (prof5 == [Q(25, 44), Q(9, 44), Q(9, 44), Q(1, 44)] and in_circ(prof5) and not in_O(prof5)
         and in_circ(pi_fix(w)) and tr(w, Pv) == -3 and expand((u.H * u)[0]) == 1)
perm_ok = True; pair_set = set()
for perm in itertools.permutations(range(4)):
    Pm = zeros(4, 4)
    for i in range(4): Pm[perm[i], i] = 1
    sdg = Pm * dg * Pm.T
    perm_ok = perm_ok and tr(Pu, sdg) == Q(1, 2)
    pair_set.add(tr(dg, sdg))
ok_w3 = ok_w3 and perm_ok and pair_set == {0, 4}
u5 = 3 * PSI[0] + PSI[1] + PSI[2] + PSI[3]
U5 = PSIM.H * (u5 * u5.H) * PSIM                          # psi coordinates
y5 = U5 + 8 * dg; y6 = U5 + 6 * dg
x5 = PSIM.H * (3 * PSI[0] - PSI[1] - PSI[2] - PSI[3])
val = expand((x5.H * y5 * x5)[0])
ev6 = y6.eigenvals(); ev8 = y5.eigenvals()
psd6 = all(simplify(k) >= 0 for k in ev6); npsd8 = any(simplify(k) < 0 for k in ev8)
orbit_ok = True
u5c = PSIM.H * u5
for perm in itertools.permutations(range(4)):
    Pm = zeros(4, 4)
    for i in range(4): Pm[perm[i], i] = 1
    sdg = Pm * dg * Pm.T; su = Pm * u5c
    val160 = 8 * (expand((u5c.H * sdg * u5c)[0]) + expand((su.H * dg * su)[0])) + 64 * tr(dg, sdg)
    orbit_ok = orbit_ok and val160 == 160
rec('X2', ok_w3 and pi_fix(y5) == [1, 9, 9, 9] and val == -12 and psd6 and npsd8 and orbit_ok,
    'profile (25, 9, 9, 1)/44 in Circ \\ O; pi(w) in Circ; tr(w P_v) = -3; tr(P_u sigma.diag) = 1/2, <diag, sigma diag> in {0, 4}; pi(y5) = (1, 9, 9, 9), x^dag y5 x = -12, coefficient 6 PSD and 8 not; orbit bound 160 for all 24 permutations',
    'eigenvalues at 6: %s; at 8: %s' % ({str(k): m for k, m in ev6.items()}, {str(k): m for k, m in ev8.items()}))

print("== X3 C7 W5 Bell-circle certificate")
Pperp = diagpsi([0, 1, 0, 1]); sz = diagpsi([1, 0, -1, 0]); sx = E(0, 2) + E(2, 0)
gt = Matrix([cos(t), 0, sin(t), 0])                      # psi coordinates of cos t psi_1 + sin t psi_3
ok_dg = simplify(eye(4) - 2 * gt * gt.T - (Pperp - cos(2 * t) * sz - sin(2 * t) * sx)) == zeros(4, 4)
V = [Matrix([Q(39, 100), Q(41, 125) - 47 * I / 1000, Q(61, 125), Q(53, 1000) - 173 * I / 500]),
     Matrix([Q(53, 1000), Q(41, 125) - 47 * I / 1000, Q(-311, 500), Q(53, 1000) - 173 * I / 500])]
NV = [(Q(-15088121, 17088121), Q(-8022000, 17088121)), (Q(10971, 114029), Q(113500, 114029))]
tcoef = Q(189, 1000)
ys = []; strict = True; margins = []
for vi, ni in zip(V, NV):
    assert ni[0] ** 2 + ni[1] ** 2 == 1
    dgi = Pperp - ni[0] * sz - ni[1] * sx
    yi = vi * vi.H + tcoef * dgi + eye(4) / 1000
    yi = yi.applyfunc(expand); ys.append(yi)
    A = tr(yi, Pperp); B = tr(yi, sz); C = tr(yi, sx)
    strict = strict and A > 0 and A ** 2 - B ** 2 - C ** 2 > 0
    margins.append(A ** 2 - B ** 2 - C ** 2)
p12 = tr(ys[0], ys[1])
target = Q(-475586012673053754301, 30445958586078125000000)
herm = all(yi.H == yi for yi in ys)
pm = [(PSI[0] - I * PSI[2]) / sqrt(2), (PSI[0] + I * PSI[2]) / sqrt(2)]
ket0m = kron(Matrix([1, 0]), Matrix([1, -1]) / sqrt(2)); ket1p = kron(Matrix([0, 1]), Matrix([1, 1]) / sqrt(2))
b5 = (simplify((pm[0].H * pm[1])[0]) == 0 and all(simplify((q.H * q)[0] - 1) == 0 for q in pm)
      and simplify((ket0m.H * ket1p)[0]) == 0 and all(simplify((q.H * q)[0] - 1) == 0 for q in (ket0m, ket1p)))
rec('X3', ok_dg and herm and strict and p12 == target and p12 < 0 and b5,
    'd_g = Pperp - cos 2t sz - sin 2t sx; y_1, y_2 Hermitian, strictly in Z_circ* (A > 0, A^2 > B^2 + C^2); tr(y1 y2) equals the thread\'s value and is negative; B5 orthonormal pairs',
    'tr(y1 y2) = %s; margins %s' % (p12, [str(m) for m in margins]))

print("== X4 C8 witness construction on a line triple")
g1 = PSI[0]; g2 = (4 * PSI[0] + 3 * PSI[2]) / 5; g3 = (3 * PSI[0] - 4 * PSI[2]) / 5; e = PSI[1]
def dB(g): return eye(4) - 2 * g * g.H
ok_me = all(max_ent(g) for g in (g1, g2, g3)) and all(expand((g.H * g)[0]) == 1 for g in (g1, g2, g3))
c = expand(abs((g1.H * g2)[0]) ** 2); c3 = expand(abs((g1.H * g3)[0]) ** 2)
eps = Q(9, 10); lam = (1 - eps ** 2) / (4 * c)
vv = g1 + eps * e; x = g2 - ((g1.H * g2)[0] / eps) * e
yy = (vv * vv.H + lam * dB(g2)).applyfunc(expand)
d1, d2, d3 = dB(g1), dB(g2), dB(g3)
L1 = tr(yy, d1) == 0; L2 = tr(yy, d2) > 0 and tr(yy, d3) > 0
L3 = expand((x.H * yy * x)[0]); pair1 = (tr(d2, d1), tr(d3, d1))
cc_eps = (expand(((g1 + e / 2) * (g1 + e / 2).H * d2).trace()) == Q(-3, 100))
cc_ZF = all(tr(dB(PSI[k]), dB(PSI[0])) == 0 for k in range(1, 4))
rec('X4', ok_me and c == Q(16, 25) and c3 == Q(9, 25) and lam == Q(19, 256) and L1 and L2 and L3 == Q(-323, 20736)
    and pair1 == (4 * c, 4 * c3) and cc_eps and cc_ZF and expand((vv.H * x)[0]) == 0,
    'c = 16/25, c3 = 9/25, lam = 19/256; <y, d_1> = 0, <y, d_2>, <y, d_3> > 0, x^dag y x = -323/20736, <d_k, d_1> = 4 c_k > 0: y in K(Z)* \\ K(Z); countercontrols eps = 1/2 (-3/100) and Z_F (all <d_k, d_1> = 0)',
    '<y,d_2> = %s, <y,d_3> = %s' % (tr(yy, d2), tr(yy, d3)))

print("== X5 C9.1 Hessian determinant and automorphisms")
x1, x2, x3, s = symbols('x1 x2 x3 s', real=True)
Nf = (x1 ** 2 + x2 ** 2 + x3 ** 2) ** 2 + s ** 4
Hs = sp.hessian(Nf, (x1, x2, x3, s))
detH = sp.factor(Hs.det())
ok_det = expand(detH - 2304 * s ** 2 * (x1 ** 2 + x2 ** 2 + x3 ** 2) ** 3) == 0
A = Matrix([[1, 0, 0, 1], [0, 2, 1, 0], [0, 0, 1, 0], [0, 0, 0, 3]])     # a rational linear map
wv = Matrix([x1, x2, x3, s]); Aw = A * wv
NA = Nf.subs(dict(zip((x1, x2, x3, s), list(Aw))), simultaneous=True)
lhs = sp.hessian(NA, (x1, x2, x3, s)).det()
rhs = A.det() ** 2 * detH.subs(dict(zip((x1, x2, x3, s), list(Aw))), simultaneous=True)
ok_chain = expand(lhs - rhs) == 0
rank_q = sp.hessian(x1 ** 2 + x2 ** 2 + x3 ** 2, (x1, x2, x3)).rank() == 3
rot = Matrix([[Q(3, 5), Q(-4, 5), 0, 0], [Q(4, 5), Q(3, 5), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]); flip = Matrix.diag(1, 1, 1, -1)
def pres(M): return expand(Nf.subs(dict(zip((x1, x2, x3, s), list(M * wv))), simultaneous=True) - Nf) == 0
shear = Matrix([[1, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]); scal = Matrix.diag(1, 1, 1, 2)
rot_xs = Matrix([[Q(3, 5), 0, 0, Q(-4, 5)], [0, 1, 0, 0], [0, 0, 1, 0], [Q(4, 5), 0, 0, Q(3, 5)]])
rec('X5', ok_det and ok_chain and rank_q and pres(rot) and pres(flip) and not pres(shear) and not pres(scal) and not pres(rot_xs),
    'det Hess N = 2304 s^2 |x|^6; chain rule det Hess(N o A) = det(A)^2 det Hess N (A w) on an instance; |x|^2 rank 3; O(3) x Z2 instances preserve N; shear, scaling, x1-s rotation do not',
    'det Hess N = %s' % detH)

print("== X6 C10.1 the case and its slice")
k0, k1 = Matrix([1, 0]), Matrix([0, 1]); kp, km = Matrix([1, 1]) / sqrt(2), Matrix([1, -1]) / sqrt(2)
def C2(wv_): return (kron(k0, km) + wv_ * kron(k1, kp)) / sqrt(2)
b = [C2(1), C2(-1), kron(k0, kp), kron(k1, km)]
Bm = Matrix.hstack(*b)
ortho = simplify(Bm.H * Bm - eye(4)) == zeros(4, 4)
ent = max_ent(b[0]) and max_ent(b[1])
def is_product_table(g): return tab(g * g.H).rank() == 1
prods = is_product_table(b[2]) and is_product_table(b[3])
CNOT = kron(Matrix([[1, 0], [0, 0]]), I2) + kron(Matrix([[0, 0], [0, 1]]), SX)
ok_cnot = simplify(CNOT - (eye(4) - 2 * b[3] * b[3].H)) == zeros(4, 4)
Cb = simplify(Bm.H * CNOT * Bm)
ok_diag = Cb == Matrix.diag(1, 1, 1, -1)
al, be = symbols('alpha beta', real=True)
wts = [al, be, al + be, 0]
ok_simple = all(expand(wts[i] - wts[j]) != 0 for i in range(4) for j in range(i + 1, 4))
Mco = Matrix(2, 2, lambda i, j: b[0][2 * i + j])
ok_schmidt = simplify(Mco * Mco.H - eye(2) / 2) == zeros(2, 2)
zt = (eye(4) - 2 * b[0] * b[0].H) / 8
Pk = [bk * bk.H for bk in b]
ok_fix = all(simplify(zt * P - P * zt) == zeros(4, 4) for P in Pk) and simplify(zt * CNOT - CNOT * zt) == zeros(4, 4)
def facets_of_rays(rays):
    """facet normals (primitive integer, inward) of cone{rays} in R^4 (rays spanning R^4)"""
    out = set()
    for trip in itertools.combinations(rays, 3):
        M = Matrix([list(r) for r in trip])
        if M.rank() != 3: continue
        nvec = M.nullspace()[0]
        nvec = nvec / sp.gcd(list(nvec)) if all(x.is_integer for x in nvec) else nvec
        vals = [sum(a * c for a, c in zip(nvec, r)) for r in rays]
        if all(v >= 0 for v in vals): out.add(tuple(nvec))
        elif all(v <= 0 for v in vals): out.add(tuple(-nvec))
    return {tuple(x / sp.gcd([abs(y) for y in n if y != 0]) for x in n) for n in out}
def extreme_rays_of_ineqs(ineqs):
    """extreme rays (primitive integer) of {d : a.d >= 0 for a in ineqs} in R^4"""
    out = set()
    for trip in itertools.combinations(ineqs, 3):
        M = Matrix([list(a) for a in trip])
        if M.rank() != 3: continue
        r = M.nullspace()[0]
        vals = [sum(a * c for a, c in zip(ai, r)) for ai in ineqs]
        if all(v >= 0 for v in vals): out.add(tuple(r))
        elif all(v <= 0 for v in vals): out.add(tuple(-r))
    return {tuple(x / sp.gcd([abs(y) for y in n if y != 0]) for x in n) for n in out}
f = (-1, 1, 1, 1); e_ = lambda k: tuple(1 if i == k else 0 for i in range(4))
gens = [f, e_(1), e_(2), e_(3), tuple(a + b_ for a, b_ in zip(e_(0), e_(1))), tuple(a + b_ for a, b_ in zip(e_(0), e_(2))), tuple(a + b_ for a, b_ in zip(e_(0), e_(3)))]
GS = {tuple(Q(x) for x in g) for g in gens}
facets = facets_of_rays([tuple(Q(x) for x in g) for g in gens])
self_dual = facets == GS
ext_C = extreme_rays_of_ineqs(list(facets))
ext_ok = ext_C == GS
sub = extreme_rays_of_ineqs([tuple(Q(x) for x in e_(k)) for k in range(4)] + [tuple(Q(x) for x in f)])
sub_ok = sub == {g for g in GS if g != tuple(Q(x) for x in f)}
not_orthant = not all(x >= 0 for x in f)
prod_basis = [kron(k0, k0), kron(k0, k1), kron(k1, kp), kron(k1, km)]
cc1 = all(is_product_table(g) for g in prod_basis)
xy = kron(k0, km)                                        # |<b1|0->|^2 = 1/2
cc2 = expand((xy.H * (eye(4) - Q(5, 2) * b[0] * b[0].H) * xy)[0]) < 0 and expand((xy.H * (eye(4) - 2 * b[0] * b[0].H) * xy)[0]) == 0
rec('X6', ortho and ent and prods and ok_cnot and ok_diag and ok_simple and ok_schmidt and ok_fix and self_dual and ext_ok and sub_ok and not_orthant and cc1 and cc2,
    'basis orthonormal, two Bell and two product members; CNOT = I - 2|1-><1-| diagonal (1,1,1,-1); simple spectrum; M M^dag = I/2; z fixed by H0 and CNOT; slice cone: 7 extreme rays = 7 facet normals (self-dual), != R^4_+; R^4_+ n f* has the six predicted rays; countercontrols hold',
    'facets %s' % sorted([str(x) for x in facets]))

print("SUMMARY %d/%d CONFIRMED" % (sum(R), len(R)))
print("INDEP-C2-FIXED" if all(R) else "INDEP-C2-MISMATCH")
