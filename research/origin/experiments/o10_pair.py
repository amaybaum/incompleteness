"""o10_pair.py -- research/origin, round 3, node O10: HO-9's constraint carried to the pair, with HO-13's target.

QUESTION. (a) Does a re-preparing token law carry, on ONE token, the two operations HO-13 names -- J = cyc3 and one
infinite-order rotation about the frame axis -- with the exact witness (1, 1/2)? Is the Kochen-Specker tower's own
stage-crossing datum (cos a = 3/5) a frame-axis rotation of the completed body? (b) Form the composite of two such
tokens: can any re-preparing law on the PAIR realize a candidate pair cone (which contains phiW = cnot(prodState
xplus z3), S_CHSH = 14/5 at HO-3's settings)? Product re-preparation is Bell-local (HO-3 item 3, HO-9 item 6); the new
cases are correlated preparations through joint substratum maps and cross-token (correlated) re-preparation.

TOKENS. Sphere tower (O6-I): hidden direction lambda in S^2; readout along u: outcome sgn(u.lambda), then lambda is
re-sampled from rho_{+-u}(lambda) = (+-u.lambda)^+ / pi; tower states are Bloch vectors psi in the ball with
P(+u | psi) = (1 + psi.u)/2 (O6 K7). Circle tower (O6-I): the same on S^1, body the disk. Frame axis: e_z (the
kernel's third coordinate: rot3 rotates about it, cyc3 = (x, y, z) -> (z, x, y)).
SETTINGS (HO-3 item 2): a0 = e_x, a1 = e_z, b0 = (4/5, 0, 3/5), b1 = (4/5, 0, -3/5).

CHECKS.
 A1  the kernel's cyc3 (KInfFoundations.lean:425, cyc3_apply :427) as a matrix J: orthogonal, det 1, order 3,
     J e_z = e_x; R = R_z(theta0) (rotFun of ball3Drive, :449, cos 3/5, sin 4/5): orthogonal, det 1, R e_z = e_z,
     e^{i theta0} = (3+4i)/5 with minimal polynomial 5x^2 - 6x + 5, not monic over Z (infinite order); R^k != 1 for
     k <= 200 (sanity).
 A2  sphere tower: for R in {J, R_z(theta0)}, psi.(R^T lambda) = (R psi).lambda identically (symbolic), so the
     cosine density rho_psi o R^-1 = rho_{R psi}: the rotation acts on the body as psi -> R psi.
 A3  witness for J with the tower's frame dephasing D(psi) = psi_z e_z (observe-and-forget of the z readout:
     outcome +- with probability (1 +- psi_z)/2, re-prepared at +-e_z): (P_coh, P_deph) = (1, 1/2); J e_z = e_x is
     pure (unit) and z-balanced; D equals the projection on the frame axis, and the frame face {P(+z) = 1} of the
     ball is {e_z} (psi_z = 1 and |psi| <= 1 force psi = e_z): not memory erasure.
 A4  R_z(theta0) commutes with D: P_coh = P_deph for the seeds e_z, e_x, (3/5, 0, 4/5), (2/3, 2/3, 1/3).
 A5  O6-I's sphere datum g = R_z(a), cos a = 3/5 (o6_tower K7), equals R_z(theta0): a frame-axis rotation. Circle
     tower: g = R(a) maps the frame point e_1 to (3/5, 4/5) (P(+0) = 4/5); the orthogonal 2x2 matrices fixing e_1
     are exactly diag(1, 1), diag(1, -1); R(2 pi/3) gives P(+0) = 1/4; R(pi/2) is balanced and of order 4.
 A6  J R_z(theta0) J^-1 = R_x(theta0) exactly; it fixes e_x and has the trace of R_z(theta0) (infinite order).
 B1  product law: over the 16 deterministic sign patterns S in {-2, 2}; each pattern is realized by rational
     Kochen-Specker directions; b0 + b1 = (8/5, 0, 0), b0 - b1 = (0, 0, 6/5); products of tower states reach
     S = 8/5 at r = s = e_x (the maximum over products, by Cauchy-Schwarz).
 B2  joint substratum bijection (controlled rotation): lambda_A uniform, lambda_B ~ rho_{C lambda_A},
     C = diag(1, -1, 1): E[sgn(e_z.lambda) lambda] = (0, 0, 1/2) for lambda uniform on S^2 (symbolic integral), hence
     E(u, v) = u^T C v / 2 and the table (1, 0; 0, C/2); S = 7/5; the partial transpose of its density matrix
     (1/4) sum omega_{mu nu} sigma_mu (x) sigma_nu has eigenvalues {-1/8, 3/8, 3/8, 3/8}: entangled, Bell-local.
 B3  cnot(prodState xplus z3) from the kernel's tables sgn, pc, pt (CompositeDimension.lean:741-758) is
     diag(1, 1, -1, 1) = phiW (:1220-1222); its density matrix is |Phi+><Phi+| (rank one, PSD); S(phiW) = 14/5 > 2.
 B4  collapse law: reading A along u with outcome a re-prepares A at a u and B at
     psi_B = (s + a C^T u)/(1 + a r.u): symbolic in r, s, C, u, v, a, b, the A-then-B statistics and the B-then-A
     statistics both equal (1 + a r.u + b s.v + a b u^T C v)/4, and B's marginal does not depend on u; for phiW
     psi_B = a C u, S = 14/5, and psi_B(+, e_x) = e_x != e_z = psi_B(+, e_z) (B's re-prepared state depends on A's
     setting at a fixed outcome).
 B5  forced form: the B-state psi that reproduces the table's conditional statistics for v = e_x, e_y, e_z
     (b = +1) is unique and equals (s + a C^T u)/(1 + a r.u); the b = -1 conditions then hold.
 B6  a law whose re-preparation of B uses only A's outcome and the pre-readout hidden state cannot realize phiW:
     the required conditional states at (+, e_x), (+, e_z) are the distinct pure states e_x, e_z; on the octant
     partition of the uniform hidden direction the two conditions force f = e_x on the four octants with x > 0 and
     f = e_z on the four with z > 0 (an average of vectors of the unit ball equal to a unit vector forces each to
     equal it), and two octants carry both: infeasible; their measure is 1/4.
 B7  a setting-free law exceeding 2 off the table space: lambda_A uniform, B re-prepared by the sign pattern of
     (x, z): S = 12/5 exactly, B's marginal Bloch vector 0 for both settings; the bilinear fit C_b of the four
     correlators has C_b^T C_b with characteristic polynomial p, p(1) = -17/50 < 0: a singular value above 1, while
     every table of the maximal cone has |u^T C v| <= 1: no table carries these correlators.
 B8  disguise of the collapse law: phiW and the uncorrelated state (0 marginals, C = 0) admit the same hidden
     marginals (both uniform) and require different laws at (+, e_x): e_x versus 0; after any readout the pair's
     statistics factorize (A at a u, B at psi_B), so from products the law with local operations reaches only
     mixtures of products and phiW needs cnot as a given pair operation.
DECISION RULE (fixed before the first run; the verdict is generated from the measured booleans):
  TOKEN := A1 and A2 and A3 and A4 and A5 and A6.   PRODUCT_OBSTRUCTION := B1 and B2 and B3.
  CROSS_TOKEN := B4 and B5 and B6 and B7 and B8.
  VERDICT VOID if any countercontrol is True.
  VERDICT TOKEN-REALIZED-PAIR-ONLY-BY-THE-CONE-OWN-LAW iff TOKEN and PRODUCT_OBSTRUCTION and CROSS_TOKEN;
    otherwise VERDICT MIXED with the failing items listed.
COUNTERCONTROLS (must be False):
  CC1 the maximum of |S| over deterministic tables in which B's outcome may depend on A's setting is <= 2;
  CC2 R_z(pi/2) passes the infinite-order certificate;
  CC3 the required conditional states at (+, e_x) and (+, e_z) coincide;
  CC4 the product state xplus (x) z3 has |S| > 2;
  CC5 the partial transpose of the table (1, 0; 0, C/2) has no negative eigenvalue;
  CC6 under the collapse law B's marginal for phiW depends on A's setting.

Run: python3 -I -B o10_pair.py > o10_pair.out 2> o10_pair.err; echo "exit $?" >> o10_pair.err
"""

from fractions import Fraction as F
from itertools import product
import sympy as sp

RES = {}
CC = {}
print("== o10_pair ==")
print()


def mat(rows):
    return tuple(tuple(F(x) for x in r) for r in rows)


def mmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)) for i in range(n))


def mvec(A, v):
    return tuple(sum(A[i][k] * v[k] for k in range(len(v))) for i in range(len(A)))


def tr(A):
    return tuple(tuple(A[j][i] for j in range(len(A))) for i in range(len(A[0])))


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


I3 = mat([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
EX, EY, EZ = (F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(0), F(0), F(1))


def cyc3(v):
    """cyc3_apply: (cyc3 v) 0 = v 2, (cyc3 v) 1 = v 0, (cyc3 v) 2 = v 1."""
    return (v[2], v[0], v[1])


J = tr(tuple(cyc3(e) for e in (EX, EY, EZ)))   # columns are the images of the basis vectors
CA, SA = F(3, 5), F(4, 5)


def Rz(c, s):
    """rotFun t v = (cos t v0 - sin t v1, sin t v0 + cos t v1, v2)."""
    return mat([[c, -s, 0], [s, c, 0], [0, 0, 1]])


R = Rz(CA, SA)

print("-- A: one token")
x = sp.symbols("x")
J2 = mmul(J, J)
J3 = mmul(J2, J)
a1_J = mmul(tr(J), J) == I3 and det3(J) == 1 and J3 == I3 and J != I3 and J2 != I3 and mvec(J, EZ) == EX
minpoly = sp.Poly(sp.minimal_polynomial(sp.Rational(3, 5) + sp.I * sp.Rational(4, 5), x), x)
monic_int = minpoly.LC() == 1 and all(cf.is_integer for cf in minpoly.all_coeffs())
Rk = I3
order_free = True
for k in range(1, 201):
    Rk = mmul(Rk, R)
    order_free = order_free and Rk != I3
a1_R = mmul(tr(R), R) == I3 and det3(R) == 1 and mvec(R, EZ) == EZ and not monic_int and order_free
RES["A1"] = a1_J and a1_R
mp = sp.minimal_polynomial(sp.I, x)
CC["CC2"] = not (sp.Poly(mp, x).LC() == 1 and all(cf.is_integer for cf in sp.Poly(mp, x).all_coeffs()))
print(f"A1  J = cyc3 = {[list(map(str, r)) for r in J]}: orthogonal, det 1, order 3, J e_z = e_x: {a1_J}; "
      f"R_z(theta0) orthogonal, det 1, fixes e_z; minimal polynomial of (3+4i)/5: {sp.Poly(minpoly, x).as_expr()} "
      f"(monic over Z: {monic_int}); R^k != 1 for k <= 200: {order_free}  -> {RES['A1']}")

lam = sp.symbols("l1 l2 l3", real=True)
psi = sp.symbols("p1 p2 p3", real=True)


def smat(M):
    return sp.Matrix([[sp.Rational(e.numerator, e.denominator) for e in r] for r in M])


a2 = True
for M in (J, R):
    Ms = smat(M)
    lhs = (sp.Matrix(psi).T * (Ms.T * sp.Matrix(lam)))[0]
    rhs = ((Ms * sp.Matrix(psi)).T * sp.Matrix(lam))[0]
    a2 = a2 and sp.expand(lhs - rhs) == 0
RES["A2"] = a2
print(f"A2  psi.(R^T lambda) = (R psi).lambda for R = J, R_z(theta0) (symbolic): {a2}  -> {RES['A2']}")


def deph(v):
    """observe-and-forget of the z readout on the tower: (1+v_z)/2 e_z + (1-v_z)/2 (-e_z) = v_z e_z."""
    pz = (1 + v[2]) / 2
    return tuple(pz * a + (1 - pz) * (-a) for a in EZ)


def pz_plus(v):
    return (1 + v[2]) / 2


Jinv = tr(J)
mid = mvec(J, EZ)
p_coh = pz_plus(mvec(Jinv, mid))
p_deph = pz_plus(mvec(Jinv, deph(mid)))
proj_ok = all(deph(v) == (F(0), F(0), v[2]) for v in [EX, EY, EZ, (F(3, 5), F(0), F(4, 5)), (F(1, 3), F(2, 3), F(2, 3))])
a3 = (p_coh, p_deph) == (1, F(1, 2)) and dot(mid, mid) == 1 and pz_plus(mid) == F(1, 2) and proj_ok
RES["A3"] = a3
print(f"A3  seed e_z, J, [frame dephasing], J^-1, read z: (P_coh, P_deph) = ({p_coh}, {p_deph}); J e_z = {mid} pure and "
      f"z-balanced; dephasing = projection on the frame axis: {proj_ok}  -> {RES['A3']}")

seeds = [EZ, EX, (F(3, 5), F(0), F(4, 5)), (F(2, 3), F(2, 3), F(1, 3))]
Rinv = tr(R)
a4 = all(pz_plus(mvec(Rinv, mvec(R, s))) == pz_plus(mvec(Rinv, deph(mvec(R, s)))) for s in seeds)
RES["A4"] = a4
print(f"A4  R_z(theta0) sandwich: P_coh = P_deph for 4 seeds: {a4}  -> {RES['A4']}")

g_sphere = Rz(CA, SA)                     # o6_tower K7: G = Rz(CA, SA)
g_circle = mat([[CA, -SA], [SA, CA]])
e1 = (F(1), F(0))
img = tuple(sum(g_circle[i][k] * e1[k] for k in range(2)) for i in range(2))
p_after = (1 + img[0]) / 2
q12, q22 = sp.symbols("q12 q22", real=True)
# an orthogonal 2x2 matrix fixing e_1 has first column e_1; its second column (q12, q22) is a unit vector
# orthogonal to e_1:
sol = sp.solve([sp.Eq(1 * q12 + 0 * q22, 0), sp.Eq(q12 ** 2 + q22 ** 2, 1)], [q12, q22], dict=True)
sol_set = sorted((d[q12], d[q22]) for d in sol)
fix_e1 = []
for sgn_ in (1, -1):
    Q = mat([[1, 0], [0, sgn_]])
    fix_e1.append(tuple(sum(Q[i][k] * e1[k] for k in range(2)) for i in range(2)) == e1)
p_r3 = (1 + F(-1, 2)) / 2   # R(2 pi/3) maps e_1 to (cos 2pi/3, sin 2pi/3) = (-1/2, sqrt(3)/2)
rq = mat([[0, -1], [1, 0]])
rq2 = tuple(tuple(sum(rq[i][k] * rq[k][j] for k in range(2)) for j in range(2)) for i in range(2))
rq4 = tuple(tuple(sum(rq2[i][k] * rq2[k][j] for k in range(2)) for j in range(2)) for i in range(2))
order4 = rq4 == mat([[1, 0], [0, 1]]) and rq2 != mat([[1, 0], [0, 1]]) and rq != mat([[1, 0], [0, 1]])
p_rq = (1 + rq[0][0]) / 2
a5 = (g_sphere == R and mvec(g_sphere, EZ) == EZ and img == (F(3, 5), F(4, 5)) and p_after == F(4, 5)
      and sol_set == [(0, -1), (0, 1)] and all(fix_e1) and p_r3 == F(1, 4) and p_rq == F(1, 2) and order4)
RES["A5"] = a5
print(f"A5  sphere datum g = R_z(theta0): {g_sphere == R}, fixes e_z: {mvec(g_sphere, EZ) == EZ}; circle datum maps e_1 to "
      f"{img} (P(+0) = {p_after}); O(2) fixing e_1 = {{diag(1, 1), diag(1, -1)}}; R(2pi/3): P(+0) = {p_r3}; R(pi/2): "
      f"P(+0) = {p_rq}, order 4: {order4}  -> {RES['A5']}")


def Rx(c, s):
    return mat([[1, 0, 0], [0, c, -s], [0, s, c]])


conj = mmul(mmul(J, R), Jinv)
a6 = conj == Rx(CA, SA) and mvec(conj, EX) == EX and sum(conj[i][i] for i in range(3)) == sum(R[i][i] for i in range(3))
RES["A6"] = a6
print(f"A6  J R_z(theta0) J^-1 = R_x(theta0): {conj == Rx(CA, SA)}; fixes e_x, trace {sum(conj[i][i] for i in range(3))} "
      f"= trace of R_z(theta0)  -> {RES['A6']}")
print()

# -----------------------------------------------------------------------------------------------------------------
print("-- B: the pair")
A0, A1s = EX, EZ
B0, B1 = (F(4, 5), F(0), F(3, 5)), (F(4, 5), F(0), F(-3, 5))


def chsh_from_E(E):
    return E(A0, B0) + E(A0, B1) + E(A1s, B0) - E(A1s, B1)


vals = set()
for p0, p1, q0, q1 in product((1, -1), repeat=4):
    vals.add(p0 * q0 + p0 * q1 + p1 * q0 - p1 * q1)


def sgn(t):
    return 1 if t > 0 else -1 if t < 0 else 0


realized = True
for p0, p1, q0, q1 in product((1, -1), repeat=4):
    lamA = (F(3, 5) * p0, F(0), F(4, 5) * p1)
    if (p0, p1) != (sgn(dot(A0, lamA)), sgn(dot(A1s, lamA))):
        realized = False
    cand = {(1, 1): EX, (-1, -1): (F(-1), F(0), F(0)), (1, -1): EZ, (-1, 1): (F(0), F(0), F(-1))}[(q0, q1)]
    if (q0, q1) != (sgn(dot(B0, cand)), sgn(dot(B1, cand))):
        realized = False
sums = tuple(a + b for a, b in zip(B0, B1)) == (F(8, 5), F(0), F(0)) and \
    tuple(a - b for a, b in zip(B0, B1)) == (F(0), F(0), F(6, 5))


def E_prod(r, s):
    return lambda u, v: dot(r, u) * dot(s, v)


s_prod = chsh_from_E(E_prod(EX, EX))
b1 = vals == {-2, 2} and realized and sums and s_prod == F(8, 5)
RES["B1"] = b1
s_cc4 = chsh_from_E(E_prod(EX, EZ))
CC["CC4"] = abs(s_cc4) > 2
best_signal = max(
    (p0 * qa0 + p0 * qa1 + p1 * qb0 - p1 * qb1)
    for p0, p1, qa0, qa1, qb0, qb1 in product((1, -1), repeat=6))
CC["CC1"] = best_signal <= 2
print(f"B1  deterministic patterns: S in {sorted(vals)}; all 16 realized by rational KS directions: {realized}; "
      f"b0 + b1, b0 - b1 as stated: {sums}; S on the product e_x (x) e_x: {s_prod}  -> {RES['B1']}")

th, ph = sp.symbols("theta phi", real=True)
vecs = [sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)]
avg = []
for comp in vecs:
    up = sp.integrate(sp.integrate(comp * sp.sin(th), (th, 0, sp.pi / 2)), (ph, 0, 2 * sp.pi))
    dn = sp.integrate(sp.integrate(comp * sp.sin(th), (th, sp.pi / 2, sp.pi)), (ph, 0, 2 * sp.pi))
    avg.append(sp.simplify((up - dn) / (4 * sp.pi)))
avg_ok = avg == [0, 0, sp.Rational(1, 2)]
Cm = mat([[1, 0, 0], [0, -1, 0], [0, 0, 1]])


def E_werner(u, v):
    return dot(mvec(Cm, u), v) / 2   # E(u, v) = (C u / 2).v


s_w = chsh_from_E(E_werner)

PAULI = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]


def kron(A, B):
    K = sp.zeros(A.rows * B.rows, A.cols * B.cols)
    for i in range(A.rows):
        for j in range(A.cols):
            for k in range(B.rows):
                for l_ in range(B.cols):
                    K[i * B.rows + k, j * B.cols + l_] = A[i, j] * B[k, l_]
    return K


def dict_M(omega):
    M = sp.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            if omega[mu][nu] != 0:
                M += sp.Rational(omega[mu][nu].numerator, omega[mu][nu].denominator) * kron(PAULI[mu], PAULI[nu])
    return M / 4


def ptrans_B(M):
    P = sp.zeros(4, 4)
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    P[2 * a + b, 2 * c + d] = M[2 * a + d, 2 * c + b]
    return P


omega_w = [[F(1), F(0), F(0), F(0)], [F(0), F(1, 2), F(0), F(0)], [F(0), F(0), F(-1, 2), F(0)],
           [F(0), F(0), F(0), F(1, 2)]]
Mw = dict_M(omega_w)
ev_w = sp.Matrix(ptrans_B(Mw)).eigenvals()
ev_list = sorted(sum(([k] * m for k, m in ev_w.items()), []))
b2 = avg_ok and s_w == F(7, 5) and ev_list == [sp.Rational(-1, 8), sp.Rational(3, 8), sp.Rational(3, 8),
                                                 sp.Rational(3, 8)]
RES["B2"] = b2
CC["CC5"] = min(ev_list) >= 0
print(f"B2  E[sgn(e_z.lambda) lambda] over the uniform sphere = {avg}; table (1, 0; 0, C/2): S = {s_w}; partial "
      f"transpose eigenvalues {ev_list}  -> {RES['B2']}")

# kernel tables (CompositeDimension.lean:741-758)
PC = {(0, 0): 0, (0, 1): 0, (0, 2): 3, (0, 3): 3, (1, 0): 1, (1, 1): 1, (1, 2): 2, (1, 3): 2,
      (2, 0): 2, (2, 1): 2, (2, 2): 1, (2, 3): 1, (3, 0): 3, (3, 1): 3, (3, 2): 0, (3, 3): 0}
PT = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3, (1, 0): 1, (1, 1): 0, (1, 2): 3, (1, 3): 2,
      (2, 0): 1, (2, 1): 0, (2, 2): 3, (2, 3): 2, (3, 0): 0, (3, 1): 1, (3, 2): 2, (3, 3): 3}


def SGN(mu, nu):
    return -1 if (mu, nu) in ((1, 3), (2, 2)) else 1


def cnot(omega):
    return [[SGN(mu, nu) * omega[PC[(mu, nu)]][PT[(mu, nu)]] for nu in range(4)] for mu in range(4)]


def hom(v):
    return (F(1),) + tuple(v)


def prod_state(xv, yv):
    hx, hy = hom(xv), hom(yv)
    return [[hx[mu] * hy[nu] for nu in range(4)] for mu in range(4)]


phiW = cnot(prod_state(EX, EZ))
diag_ok = phiW == [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]]
Mphi = dict_M([[F(e) for e in r] for r in phiW])
phi_plus = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)
proj_ok = sp.simplify(Mphi - phi_plus * phi_plus.T) == sp.zeros(4, 4)
rank1 = Mphi.rank() == 1


def E_table(omega):
    return lambda u, v: sum(u[i] * omega[i + 1][j + 1] * v[j] for i in range(3) for j in range(3))


s_phi = chsh_from_E(E_table(phiW))
b3 = diag_ok and proj_ok and rank1 and s_phi == F(14, 5)
RES["B3"] = b3
print(f"B3  cnot(prodState xplus z3) from the kernel tables = diag(1, 1, -1, 1): {diag_ok}; density matrix = "
      f"|Phi+><Phi+| (rank one): {proj_ok and rank1}; S(phiW) = {s_phi}  -> {RES['B3']}")

r = sp.Matrix(sp.symbols("r1 r2 r3", real=True))
s = sp.Matrix(sp.symbols("s1 s2 s3", real=True))
Cs = sp.Matrix(3, 3, sp.symbols("c11 c12 c13 c21 c22 c23 c31 c32 c33", real=True))
u = sp.Matrix(sp.symbols("u1 u2 u3", real=True))
v = sp.Matrix(sp.symbols("v1 v2 v3", real=True))
a, b = sp.symbols("a b", real=True)
target = (1 + a * (r.T * u)[0] + b * (s.T * v)[0] + a * b * (u.T * Cs * v)[0]) / 4
pA = (1 + a * (r.T * u)[0]) / 2
psiB = (s + a * Cs.T * u) / (1 + a * (r.T * u)[0])
pAB = pA * (1 + b * (psiB.T * v)[0]) / 2
pB = (1 + b * (s.T * v)[0]) / 2
psiA = (r + b * Cs * v) / (1 + b * (s.T * v)[0])
pBA = pB * (1 + a * (psiA.T * u)[0]) / 2
seq_ok = sp.simplify(pAB - target) == 0 and sp.simplify(pBA - target) == 0
nosig = sp.simplify(pAB.subs(a, 1) + pAB.subs(a, -1) - pB) == 0
phiC = mat([[1, 0, 0], [0, -1, 0], [0, 0, 1]])


def psiB_phi(av, uv):
    return tuple(av * x_ for x_ in mvec(tr(phiC), uv))


def E_collapse(uv, vv):
    tot = F(0)
    for av in (1, -1):
        for bv in (1, -1):
            pa = F(1, 2)
            pb = (1 + bv * dot(psiB_phi(av, uv), vv)) / 2
            tot += av * bv * pa * pb
    return tot


s_coll = chsh_from_E(E_collapse)
pdep = psiB_phi(1, EX) == EX and psiB_phi(1, EZ) == EZ and EX != EZ
margB = {}
for uv in (A0, A1s):
    margB[uv] = tuple(sum(F(1, 2) * x_ for x_ in comps) for comps in zip(psiB_phi(1, uv), psiB_phi(-1, uv)))
CC["CC6"] = margB[A0] != margB[A1s]
b4 = seq_ok and nosig and s_coll == F(14, 5) and pdep
RES["B4"] = b4
print(f"B4  collapse law: A-then-B and B-then-A statistics = the table's bilinear form (symbolic): {seq_ok}; no-signaling: "
      f"{nosig}; S(phiW) = {s_coll}; psi_B(+, e_x) = {psiB_phi(1, EX)}, psi_B(+, e_z) = {psiB_phi(1, EZ)}: {pdep}  "
      f"-> {RES['B4']}")

pp = sp.Matrix(sp.symbols("q1 q2 q3", real=True))
eqs = []
for vv in (sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0]), sp.Matrix([0, 0, 1])):
    lhs = pA * (1 + (pp.T * vv)[0]) / 2
    rhs = target.subs({v[0]: vv[0], v[1]: vv[1], v[2]: vv[2], b: 1})
    eqs.append(sp.Eq(lhs, rhs))
solq = sp.solve(eqs, list(pp), dict=True)
uniq = len(solq) == 1 and all(sp.simplify(solq[0][pp[i]] - psiB[i]) == 0 for i in range(3))
minus_ok = True
if uniq:
    for vv in (sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0]), sp.Matrix([0, 0, 1])):
        lhs = pA * (1 - (sp.Matrix([solq[0][pp[i]] for i in range(3)]).T * vv)[0]) / 2
        rhs = target.subs({v[0]: vv[0], v[1]: vv[1], v[2]: vv[2], b: -1})
        minus_ok = minus_ok and sp.simplify(lhs - rhs) == 0
RES["B5"] = uniq and minus_ok
print(f"B5  the B-state reproducing the conditional statistics is unique and equals (s + a C^T u)/(1 + a r.u): {uniq}; "
      f"b = -1 conditions hold: {minus_ok}  -> {RES['B5']}")

req_x = psiB_phi(1, EX)
req_z = psiB_phi(1, EZ)
pure = dot(req_x, req_x) == 1 and dot(req_z, req_z) == 1
CC["CC3"] = req_x == req_z
octants = list(product((1, -1), repeat=3))
on_x = [o for o in octants if o[0] == 1]
on_z = [o for o in octants if o[2] == 1]
both = [o for o in octants if o[0] == 1 and o[2] == 1]
measure_both = F(len(both), 8)
# an average of vectors in the unit ball equal to a unit vector e forces each vector to equal e:
# e.avg = 1 and e.f_i <= |f_i| <= 1 give e.f_i = 1 for all i, and then |f_i - e|^2 = |f_i|^2 - 2 e.f_i + 1 <= 0.
forced_x = {o: req_x for o in on_x}
forced_z = {o: req_z for o in on_z}
conflict = [o for o in both if forced_x[o] != forced_z[o]]
b6 = pure and req_x != req_z and len(on_x) == 4 and len(on_z) == 4 and len(both) == 2 and \
    measure_both == F(1, 4) and conflict == both
RES["B6"] = b6
print(f"B6  required conditional states at (+, e_x), (+, e_z): {req_x}, {req_z} (pure, distinct: {pure and req_x != req_z}); "
      f"octants forced to e_x: {len(on_x)}, to e_z: {len(on_z)}, both: {len(both)} (uniform measure {measure_both}); "
      f"conflicting octants: {len(conflict)}  -> {RES['B6']}")


def f_quad(av, pattern):
    """B's re-prepared Bloch vector after A's outcome av, given the sign pattern (A0, A1) of lambda_A."""
    A0v, A1v = pattern
    if A0v == A1v:
        return tuple(av * x_ for x_ in B0)
    if av == A0v:
        return tuple(av * x_ for x_ in EX)
    return tuple(av * x_ for x_ in EZ)


def E_quad(uv, vv):
    idx = 0 if uv == A0 else 1
    tot = F(0)
    for pattern in product((1, -1), repeat=2):
        av = pattern[idx]
        tot += F(1, 4) * av * dot(f_quad(av, pattern), vv)
    return tot


s_quad = chsh_from_E(E_quad)
mB = {}
for k, uv in enumerate((A0, A1s)):
    tot = [F(0)] * 3
    for pattern in product((1, -1), repeat=2):
        fv = f_quad(pattern[k], pattern)
        tot = [t + F(1, 4) * c for t, c in zip(tot, fv)]
    mB[k] = tuple(tot)
nosig_q = mB[0] == mB[1] == (F(0), F(0), F(0))
Ex0, Ex1, Ez0, Ez1 = E_quad(A0, B0), E_quad(A0, B1), E_quad(A1s, B0), E_quad(A1s, B1)
# fit u^T C_b v on the x-z plane: b0 = (4/5, 3/5), b1 = (4/5, -3/5) in (x, z)
cxx = (Ex0 + Ex1) / F(8, 5)
cxz = (Ex0 - Ex1) / F(6, 5)
czx = (Ez0 + Ez1) / F(8, 5)
czz = (Ez0 - Ez1) / F(6, 5)
Cb = ((cxx, cxz), (czx, czz))
CtC = tuple(tuple(sum(Cb[k][i] * Cb[k][j] for k in range(2)) for j in range(2)) for i in range(2))
p_at_1 = 1 - (CtC[0][0] + CtC[1][1]) + (CtC[0][0] * CtC[1][1] - CtC[0][1] * CtC[1][0])
b7 = s_quad == F(12, 5) and nosig_q and Cb == ((F(9, 10), F(3, 10)), (F(2, 5), F(4, 5))) and p_at_1 == F(-17, 50)
RES["B7"] = b7
print(f"B7  octant-pattern law: S = {s_quad}; B's marginal for both settings {mB[0]}, {mB[1]}; correlators "
      f"{Ex0}, {Ex1}, {Ez0}, {Ez1}; bilinear fit C_b = {[[str(c) for c in row] for row in Cb]}; p(1) = {p_at_1}  "
      f"-> {RES['B7']}")

law_phi = psiB_phi(1, EX)
law_uncorr = (F(0), F(0), F(0))
marg_phi = (tuple(phiW[i][0] for i in range(1, 4)), tuple(phiW[0][j] for j in range(1, 4)))
same_marginals = marg_phi == ((0, 0, 0), (0, 0, 0))   # the uncorrelated state has r = s = 0 by definition
post = True
for av in (1, -1):
    for uv in (A0, A1s):
        psi_b = psiB_phi(av, uv)
        for u2 in (A0, A1s, EY):
            for v2 in (B0, B1, EY):
                joint = {(a2, b2): (1 + a2 * av * dot(uv, u2)) * (1 + b2 * dot(psi_b, v2)) / 4
                         for a2 in (1, -1) for b2 in (1, -1)}
                ma = {a2: joint[(a2, 1)] + joint[(a2, -1)] for a2 in (1, -1)}
                mb = {b2: joint[(1, b2)] + joint[(-1, b2)] for b2 in (1, -1)}
                post = post and all(joint[(a2, b2)] == ma[a2] * mb[b2] for a2 in (1, -1) for b2 in (1, -1))
b8 = same_marginals and law_phi != law_uncorr and post
RES["B8"] = b8
print(f"B8  laws at (+, e_x): phiW -> {law_phi}, uncorrelated state -> {law_uncorr} (same hidden marginals); "
      f"post-readout statistics factorize: {post}  -> {RES['B8']}")
print()

print("-- countercontrols (must be False)")
for k in sorted(CC):
    print(f"{k}  {'CC-OK (False as required)' if not CC[k] else 'CC-FAILED (True)'}")
print()
for k in sorted(RES):
    print(f"  {k}: {RES[k]}")

TOKEN = all(RES[k] for k in ("A1", "A2", "A3", "A4", "A5", "A6"))
PRODUCT_OBSTRUCTION = RES["B1"] and RES["B2"] and RES["B3"]
CROSS_TOKEN = all(RES[k] for k in ("B4", "B5", "B6", "B7", "B8"))
if any(CC.values()):
    print("VERDICT VOID: a countercontrol is True: " + ", ".join(k for k in sorted(CC) if CC[k]))
elif TOKEN and PRODUCT_OBSTRUCTION and CROSS_TOKEN:
    print("VERDICT TOKEN-REALIZED-PAIR-ONLY-BY-THE-CONE-OWN-LAW: the sphere tower carries J = cyc3 and its own")
    print("  stage-crossing datum R_z(theta0) on one token with the exact witness (the circle tower carries neither);")
    print("  every pair law re-preparing each token only keeps |S| <= 2 (non-separable tables included), so phiW and")
    print("  cnot are out of reach; a cross-token law realizes phiW only if it takes the first readout's setting, and")
    print("  then it is forced to be the table's own conditioning rule, which reads the correlation block and needs")
    print("  cnot given.")
else:
    failing = [k for k in sorted(RES) if not RES[k]]
    print("VERDICT MIXED: failing items " + ", ".join(failing))
