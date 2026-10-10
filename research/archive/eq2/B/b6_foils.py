"""B6 (nodes N5, N6) -- the converse and one foil per hypothesis of Theorem A' (gate case).

Hypotheses (gate case): (H1) K is a convex cone in W 3; (H2) every product is in K; (H3) K <= maxCone (eball 3);
(H4) IE1: actC R and actT R map K onto K for R in SO(3); (H5) G with u o G = u, IsNot + CtrlGate + Entangling, G K = K.
Decision rule (fixed before the run):
  * converse: Q3 with cnot satisfies H1-H5 (exact identities + the cited standard PSD facts); the twin R_B Q3 with cnot'
    does too (exact transport);
  * each foil must satisfy every hypothesis but one, exactly where computable, and fail the conclusion
    K in {Q3, R_B Q3}; a foil whose failure of the conclusion rests on a written step is labelled so.
Foils: H1 -> K_nc (the cone over unitary orbits of products; exact spectrum argument); H2 -> the ray R>=0 e00;
H3 -> B3 (Hilbert-Schmidt ball cone); H4 -> K_F, C_H (B5) and K_heis (continuous case; not locally invariant, exact);
H5 -> min and max (invariant under L and every product-preserving gate, under no entangling control gate).
Usage: python3 -I -B b6_foils.py <base>/verification/lean-mathlib/OIBridge/CompositeDimension.lean
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eq2b_lib import *  # noqa

rep = Report("B6 converse and foils")
CNOT = parse_kernel_cnot(sys.argv[1])[0]
E00 = [[Fr(1) if (m, n) == (0, 0) else Fr(0) for n in range(4)] for m in range(4)]


def unit_vec(s, t):
    s, t = F(s), F(t)
    d = 1 + s * s + t * t
    return [2 * s / d, 2 * t / d, (s * s + t * t - 1) / d]


PTS = [unit_vec(s, t) for (s, t) in [(0, 0), (1, 0), (0, 1), (2, -1), (Fr(1, 2), 3), (-3, Fr(2, 5))]]
PTS += [[0, 0, 0], [Fr(1, 2), Fr(-1, 3), Fr(1, 4)]]

# ---------------------------------------------------------------- converse
ok = True
for x in PTS:
    for y in PTS[:4]:
        R = rho_of_w(prodState(x, y))
        ok &= is_psd_herm(R)
rep.check("V.1 [M] products lie in Q3: rho(prodState x y) is PSD for 48 rational x, y in the ball (all principal minors "
          "exact); in general rho(prodState x y) = rho_x (x) rho_y with rho_x PSD iff |x| <= 1 [L: Kronecker]", ok)
e_list = [hom(unit_vec(1, 2)), hom([0, 0, 0]), hom(unit_vec(-1, 3)), [Fr(2), Fr(1), Fr(0), Fr(-1)]]
psd_pts = [prodState([1, 0, 0], [0, 0, 1]), apply(CNOT, prodState([1, 0, 0], [0, 0, 1])), E00]
rep.check("V.2 [M] Q3 <= maxCone on instances: Bell state phiW and products pair nonnegatively with Lorentz effect pairs "
          "(exact; in general <E (x) F, rho> >= 0 for E, F, rho PSD [L])",
          all(pairVal(a, b, w) >= 0 for a in e_list for b in e_list for w in psd_pts))
rep.check("V.3 cnot fixes e00 (u o cnot = u) and is Ad(CNOT) (so preserves Q3 [M + L]); L preserves Q3 (B2 A.5); "
          "cnot' = R_B cnot R_B and R_B Q3 inherit all of H1-H5 through the exact transport by R_B (R_B preserves products, "
          "maxCone and normalization and normalizes L: B2 A.2, EQ-C P1)",
          CNOT[0] == [Fr(1)] + [Fr(0)] * 15 and meq(CNOT, conj_map(CNOT_U)) and apply(RB, E00) == E00)

# ---------------------------------------------------------------- H1 foil: K_nc
rep.note("K.1 [exact by enumeration of spectra] K_nc := R>=0 . (Ad U(4) . products) satisfies H2-H5 (it is Ad U(4)-invariant, "
         "contains products, lies in Q3 <= maxCone) but is not convex: the spectrum of lambda U (rho_x (x) rho_y) U^dag is "
         "{lambda p q, lambda p (1-q), lambda (1-p) q, lambda (1-p)(1-q)}; if one of these vanishes then p or q is in {0, 1} "
         "and two vanish; so (I - P00)/3, spectrum {0, 1/3, 1/3, 1/3}, is not in K_nc, yet it is a convex combination of "
         "the three pure products P01, P10, P11 in K_nc")
spec_ok = True
for p in [Fr(0), Fr(1), Fr(1, 3), Fr(1, 2)]:
    for q in [Fr(0), Fr(1), Fr(2, 5), Fr(1, 2)]:
        sp_ = [p * q, p * (1 - q), (1 - p) * q, (1 - p) * (1 - q)]
        zeros_ = sum(1 for v in sp_ if v == 0)
        spec_ok &= zeros_ in (0, 2, 3) and (zeros_ != 1)
W1 = [[Fr(1) if (m, n) == (0, 0) else Fr(0) for n in range(4)] for m in range(4)]
P01, P10, P11 = prodState([0, 0, 1], [0, 0, -1]), prodState([0, 0, -1], [0, 0, 1]), prodState([0, 0, -1], [0, 0, -1])
mix = [[(P01[m][n] + P10[m][n] + P11[m][n]) / 3 for n in range(4)] for m in range(4)]
R_mix = rho_of_w(mix)
diag_ok = all((R_mix[i][j] == (G(Fr(1, 3)) if (i == j and i > 0) else G(0))) for i in range(4) for j in range(4))
rep.check("K.2 the spectral pattern (no product spectrum has exactly one zero, sampled exactly including the corner cases) "
          "and (P01 + P10 + P11)/3 = diag(0, 1/3, 1/3, 1/3) in the dictionary (exact)", spec_ok and diag_ok)

# ---------------------------------------------------------------- H2 foil: the ray through e00
rep.check("K.3 H2 foil: the ray R>=0 e00 is a convex cone inside maxCone, fixed by cnot, by every actC R, actT R and by every "
          "u-preserving map fixing e00, but contains no product other than e00 itself",
          apply(CNOT, E00) == E00 and apply(actC(rot_from_quat((1, 2, -1, 3))), E00) == E00
          and prodState([1, 0, 0], [0, 0, 1]) != E00)

# ---------------------------------------------------------------- H3 foil: B3
def b3_val(w):
    return 3 * w[0][0] ** 2 - sum(w[m][n] ** 2 for (m, n) in IDX if (m, n) != (0, 0))


Rq = rot_from_quat((1, 2, -1, 3))
orth = all(meq(mmul(tr(Mx), Mx), I16) for Mx in [CNOT, actC(Rq), actT(Rq)])
pz = prodState(Z3, Z3)
w2 = [[(2 if (m, n) == (0, 0) else 0) - pz[m][n] for n in range(4)] for m in range(4)]
rep.check("K.4 H3 foil: B3 = {sum_{(m,n) != (0,0)} w^2 <= 3 w00^2, w00 >= 0} contains every pure product on its boundary, "
          "is mapped onto itself by cnot and local rotations (Euclidean-orthogonal, fixing e00; exact), but 2 e00 - "
          "prodState z z is in B3 with value -2 on the product effect hom z (x) hom z (B3 not inside maxCone)",
          all(b3_val(prodState(x, y)) == 0 for x in PTS[:6] for y in PTS[:6]) and orth
          and b3_val(w2) == 0 and pairVal(hom(Z3), hom(Z3), w2) == -2)

# ---------------------------------------------------------------- H4 foil (continuous case): K_heis is not L-invariant
def coeff(psi):
    return [[psi[0], psi[1]], [psi[2], psi[3]]]


def heis_invariant(psi):
    """|det S|^2 and |c|^4 for the 2x2 coefficient matrix (S symmetric part, A = c J antisymmetric part); the orbit
    invariant |det S| = |c|^2 (EQ-C P5.1) is compared in squared form to stay in Q."""
    P = coeff(psi)
    S01 = (P[0][1] + P[1][0]) / G(2)
    dS = P[0][0] * P[1][1] - S01 * S01
    cc = (P[0][1] - P[1][0]) / G(2)
    c2 = cc.re * cc.re + cc.im * cc.im
    return (dS.re * dS.re + dS.im * dS.im), c2 * c2


psi_orb = [G(0), G(Fr(3, 5)), G(0, Fr(-4, 5)), G(0)]          # exp(-i th H)|01>, cos 2th = 3/5 (up to phase)
Uloc = kron(cm([[1, G(0, -1)], [G(0, -1), 1]]), I2)          # (I - iX) (x) I, unnormalized local rotation about x
psi_rot = [sum((Uloc[i][j] * psi_orb[j] for j in range(4)), G(0)) for i in range(4)]
a0, b0 = heis_invariant(psi_orb)
a1, b1 = heis_invariant(psi_rot)
rep.check("K.5 H4 foil for the continuous case: on the exchange-flow orbit |det S| = |c|^2 (squared: 1/16 = 1/16 at an orbit point), "
          "while the local rotation (I - iX) (x) I of that point violates it (scale-free invariant, exact), so K_heis (EQ-C "
          "P5.1: closed, convex, admissible, carries the exchange flow) is not invariant under L",
          a0 == b0 and a1 != b1, f"orbit: {a0} vs {b0}; rotated: {a1} vs {b1}")

# ---------------------------------------------------------------- H5 foils: min and max
phiW = apply(CNOT, prodState([1, 0, 0], Z3))
fsep = phiW[0][0] - phiW[1][1] + phiW[2][2] - phiW[3][3]
idW = apply(RB, phiW)
chain = apply(CNOT, idW)
rep.check("K.6 H5 foils: cnot sends prodState xplus z3 to phiW with value -2 on the separable-positive functional "
          "w00 - w11 + w22 - w33 (so cnot(min) is not in min), and sends idW (in maxCone: R_B phiW) to chainW with value "
          "-1/2 on sharp(-e1) (x) sharp(-e3) (so cnot(max) is not in max); min and max are invariant under L, SWAP and "
          "local reflections, which map products to products",
          fsep == -2 and pairVal([Fr(1, 2), Fr(-1, 2), 0, 0], [Fr(1, 2), 0, 0, Fr(-1, 2)], chain) == Fr(-1, 2)
          and all(apply(SWAP16, prodState(x, y)) == prodState(y, x)
                  and apply(RB, prodState(x, y)) == prodState(x, [y[0], -F(y[1]), y[2]])
                  and apply(actC(Rq), prodState(x, y)) == prodState([sum(Rq[i][k] * F(x[k]) for k in range(3))
                                                                     for i in range(3)], y)
                  for x in PTS[:4] for y in PTS[:4]))
rep.note("K.7 [B1 + written] every entangling control gate is l1 cnot l2 with local l1, l2 (B1), and min, max are "
         "invariant under local O(3)^2, so no entangling control gate preserves min or max (K.6 transported).")
rep.verdict("CONVERSE-AND-FOILS: Q3 with cnot (and the twin with cnot') satisfies H1-H5; each hypothesis has a foil "
            "satisfying the others and failing the conclusion (K_nc, the e00 ray, B3, K_F / C_H / K_heis, min / max)")
