"""P1 (node N1) -- the one-copy relabelling R_B = actT reflY and what it transports.

Decision rule (fixed before the run): the relabelling no-go is rendered only if every transport fact
below holds exactly AND the controls hold (R_B does not commute with SWAP; Q3 != R_B(Q3)).
Usage: python3 -I p1_relabel.py <path to CompositeDimension.lean>
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eqclib import *  # noqa

rep = Report("P1 relabelling")
CD = sys.argv[1]
CN, pc, pt, neg = parse_kernel_cnot(CD)
rep.note(f"parsed kernel cnot: sgn = -1 at {sorted(neg)}")

# --- 1.1 the parsed kernel cnot is Ad(CNOT_{A->B}) in the Pauli dictionary (re-verification of k2d/K2C P1)
CNOTU = cmat([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
rep.check("1.1 kernel cnot == Ad(CNOT, control = copy A) in Pauli coordinates", CN == conj_unitary(CNOTU))
CNOTBA = cmat([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])
rep.check("1.1c countercontrol: kernel cnot != Ad(CNOT, control = copy B)", CN != conj_unitary(CNOTBA))

RB = actT_mat(REFLY)
RA = actC_mat(REFLY)
# --- 1.2 R_B maps products to products: R_B prodState x y = prodState x (reflY y)
ok = True
for (s1, t1, s2, t2) in [(0, 0, 1, 2), (Fr(1, 3), 2, -1, Fr(1, 2)), (5, -2, Fr(2, 7), 3), (0, 1, 0, 0)]:
    x, y = unit_vector(s1, t1), unit_vector(s2, t2)
    ry = [y[0], -y[1], y[2]]
    ok &= apply(RB, prodState(x, y)) == prodState(x, ry)
    xi = [x[0] / 2, x[1] / 3, 0]  # interior points too
    ok &= apply(RB, prodState(xi, y)) == prodState(xi, ry)
rep.check("1.2 R_B (prodState x y) = prodState x (reflY y) (pure and mixed instances)", ok)
# --- 1.3 R_B^T maps product effects to product effects: pairVal a b (R_B w) = pairVal a (H b) w
H = homMap(REFLY)
ok = True
import random
rnd = random.Random(20261008)
for _ in range(20):
    w = [[Fr(rnd.randint(-9, 9), rnd.randint(1, 5)) for _ in range(4)] for _ in range(4)]
    a = [Fr(rnd.randint(-9, 9), rnd.randint(1, 5)) for _ in range(4)]
    b = [Fr(rnd.randint(-9, 9), rnd.randint(1, 5)) for _ in range(4)]
    Hb = [sum(H[k][l] * b[k] for k in range(4)) for l in range(4)]
    ok &= pairVal(a, b, apply(RB, w)) == pairVal(a, Hb, w)
rep.check("1.3 pairVal a b (R_B w) = pairVal a (homMap reflY^T b) w on 20 rational instances "
          "(the identity is linear in w, a, b; homMap reflY is the diagonal (1,1,-1,1))", ok)
rep.check("1.3b homMap reflY is diagonal (so the identity holds for all a, b, w by linearity)",
          all(H[i][j] == 0 for i in range(4) for j in range(4) if i != j))
# --- 1.4 R_B normalizes local SO(3): R_B actT R R_B = actT (reflY R reflY), det = +1
ok = True
for q in [(1, 2, 3, 4), (2, -1, 0, 5), (1, 1, 1, 1), (3, 0, -2, 1)]:
    a, b, c, d = map(Fr, q)
    n2 = a * a + b * b + c * c + d * d
    R = [[(a*a+b*b-c*c-d*d)/n2, 2*(b*c-a*d)/n2, 2*(b*d+a*c)/n2],
         [2*(b*c+a*d)/n2, (a*a-b*b+c*c-d*d)/n2, 2*(c*d-a*b)/n2],
         [2*(b*d-a*c)/n2, 2*(c*d+a*b)/n2, (a*a-b*b-c*c+d*d)/n2]]
    RR = [[REFLY[i][i] * R[i][j] * REFLY[j][j] for j in range(3)] for i in range(3)]
    ok &= matmul(matmul(RB, actT_mat(R)), RB) == actT_mat(RR)
    ok &= det_frac(RR) == 1 and det_frac(R) == 1
    ok &= matmul(matmul(RB, actC_mat(R)), RB) == actC_mat(R)
rep.check("1.4 R_B actT R R_B = actT (reflY R reflY) with det +1; R_B commutes with actC R (4 rotations)", ok)
# --- 1.5 R_B commutes with actC nflip and actT nflip; R_B fixes the corner products
TN, CNf = actT_mat(NFLIP), actC_mat(NFLIP)
rep.check("1.5 R_B commutes with actT nflip and actC nflip",
          matmul(RB, TN) == matmul(TN, RB) and matmul(RB, CNf) == matmul(CNf, RB))
z = [0, 0, 1]
mz = [0, 0, -1]
corners = [z, mz]
rep.check("1.5b R_B fixes the four corner products prodState (+-z) (+-z)",
          all(apply(RB, prodState(p, q)) == prodState(p, q) for p in corners for q in corners))
# --- 1.6 cnot' := R_B cnot R_B satisfies frame, relT, relC; is entangling on prodState xplus z3
CP = matmul(matmul(RB, CN), RB)
frame = all(apply(CP, prodState(corners[a], corners[b])) == prodState(corners[a], corners[(a + b) % 2])
            for a in range(2) for b in range(2))
rep.check("1.6a cnot' frame: cnot'(z_a (x) z_b) = z_a (x) z_{a+b}", frame)
rep.check("1.6b cnot' relT: actT N cnot' actT N = cnot'", matmul(matmul(TN, CP), TN) == CP)
rep.check("1.6c cnot' relC: actC N cnot' actC N = actT N cnot'", matmul(matmul(CNf, CP), CNf) == matmul(TN, CP))
rep.check("1.6d cnot' is an involution and cnot' != cnot", matmul(CP, CP) == eye(16) and CP != CN)
xplus = [1, 0, 0]
phiW = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]]
idW = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
phiW = [[Fr(v) for v in r] for r in phiW]
idW = [[Fr(v) for v in r] for r in idW]
rep.check("1.6e cnot (prodState xplus z3) = phiW (CD:1222) and cnot'(prodState xplus z3) = idW = R_B phiW",
          apply(CN, prodState(xplus, z)) == phiW and apply(CP, prodState(xplus, z)) == idW
          and apply(RB, phiW) == idW)
rep.note("1.6f cnot' carries the CtrlGate data (frame 1.6a, relC 1.6c); its two-sided positivity on products "
         "is transported from nativeGate_cnot by 1.2-1.3 (written: R_B preserves products and maxCone); its "
         "entangling image idW is extreme in jointStates because R_B is a linear automorphism of jointStates "
         "and phiW is extreme (entangling_cnot, CD:1380) (written)")

# --- 1.7 Q3 != R_B(Q3): phiW in Q3 (rank-one projector) and idW = R_B phiW not in Q3 (singlet value -1/2)
rp = rho_of_w(phiW)
rep.check("1.7a rho(phiW) is a projector of trace 1 (so phiW in Q3)", cmul(rp, rp) == rp and ctrace(rp) == G(1))
ri = rho_of_w(idW)
v = [G(0), G(1), G(-1), G(0)]
val = G(0)
for i in range(4):
    for j in range(4):
        val = val + v[i].conj() * ri[i][j] * v[j]
rep.check("1.7b rho(idW) = SWAP/2 has singlet value v^dag rho v = -1 for |v|^2 = 2 (eigenvalue -1/2)",
          val == G(-1), str(val))
# --- 1.8 R_B does not commute with SWAP; SWAP R_B SWAP = R_A; R_A R_B = T (global transpose) preserves Q3
rep.check("1.8a SWAP R_B SWAP = R_A and R_A != R_B (R_B does not commute with SWAP)",
          matmul(matmul(SWAP16, RB), SWAP16) == RA and RA != RB)
SWU = cmat([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
rep.check("1.8b SWAP16 = Ad(SWAP unitary) in the dictionary (so SWAP preserves Q3)", SWAP16 == conj_unitary(SWU))


def transpose_map(w):
    R = rho_of_w(w)
    return w_of_rho([[R[j][i] for j in range(4)] for i in range(4)])


TT = superop_matrix(transpose_map)
rep.check("1.8c R_A R_B = T, the global transpose rho -> rho^T in the dictionary (preserves PSD)",
          matmul(RA, RB) == TT)
rep.check("1.8d hence SWAP(R_B Q3) = R_A Q3 = R_B (R_B R_A) Q3 = R_B T Q3 = R_B Q3: identity R_B R_A = T",
          matmul(RB, RA) == TT)
# --- 1.9 Pi_B := actT(-I) = R_B actT(R_y(pi)); Pi_B SWAP Pi_B = Pi_AB SWAP
PB, PA = actT_mat(MINUS), actC_mat(MINUS)
rep.check("1.9a Pi_B = R_B actT(R_y(pi)) with R_y(pi) = diag(-1,1,-1) a rotation",
          PB == matmul(RB, actT_mat(RYPI)) and det_frac(RYPI) == 1)
rep.check("1.9b Pi_B SWAP Pi_B = (Pi_A Pi_B) SWAP", matmul(matmul(PB, SWAP16), PB) == matmul(matmul(PA, PB), SWAP16))
rep.verdict("RELABELLING-TRANSPORT-EXACT: R_B is a one-copy affine relabelling that preserves products, "
            "maxCone, normalization, the local SO(3)^2, the corners and both NOT lifts, carries cnot to the "
            "native/control gate cnot' and Q3 to R_B(Q3) != Q3; it fails to commute only with SWAP, and "
            "R_B(Q3) is nevertheless SWAP-invariant")
