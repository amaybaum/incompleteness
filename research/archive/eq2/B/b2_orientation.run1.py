"""B2 (node N1, continued) -- orientation classes of the native control gates, cone compatibility, the converse, an
independent cross-check, and the exact KAK identities for cnot.

From B1: every CtrlGate at d = 3 with u o G = u is, up to conjugation by a rotation pair, F(s) o actT(O) with s one of
8 sign patterns and O in O(3), O z3 = z3. Representatives: O = I and O = reflY (the two components of O(2) (+) 1; the
rest differ by target z-rotations, which lie in L).
Decision rule (fixed before the run):
  * a representative is reported CONE-COMPATIBLE only by an exact identity G = l1 o c o l2 with l1, l2 in the
    Pauli-sign subgroup P of L (actC D actT D', D, D' diagonal of determinant +1) and c in {cnot, T cnot, cnot',
    T cnot'}, each of which preserves Q3 or R_B Q3 by an exact dictionary identity;
  * it is reported EXCLUDED only by an exact word w in G^(+-1) and P with w(product) outside maxCone (a negative
    pairing with two sharp effects);
  * the verdict needs all 16 representatives decided, the converse controls, and the cross-check of an independent
    gate from EQ-E's quantum family landing on an admissible pattern of B1.
Usage: python3 -I -B b2_orientation.py <base>/verification/lean-mathlib/OIBridge/CompositeDimension.lean
"""
import sys
import os
import itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eq2b_lib import *  # noqa

rep = Report("B2 orientation classes, cone compatibility, converse")
CNOT = parse_kernel_cnot(sys.argv[1])[0]
NT = homMap(NFLIP)
hz, hmz = hom(Z3), hom([0, 0, -1])
X4 = zeros(4, 4); X4[0][1] = X4[1][0] = Fr(1)
J4 = zeros(4, 4); J4[3][2] = Fr(1); J4[2][3] = Fr(-1)


def fam(a, a2, b1, b2):
    """The B1 family (same construction, rebuilt here): corner columns from the corner forms with M0 = I, tangent
    columns Gt(lift e_x (x) Y) = a lift e_x (x) X Y + b2 lift e_y (x) J Y, Gt(lift e_y (x) Y) = b1 lift e_x (x) J Y +
    a2 lift e_y (x) X Y."""
    M = zeros(16, 16)
    ex, ey = lift([1, 0, 0]), lift([0, 1, 0])
    for l in range(4):
        Y = [Fr(1) if k == l else Fr(0) for k in range(4)]
        cz, cmz = tens(hz, Y), tens(hmz, mvec(NT, Y))
        XY, JY = mvec(X4, Y), mvec(J4, Y)
        cols = {0: [(cz[m][n] + cmz[m][n]) / 2 for (m, n) in IDX], 3: [(cz[m][n] - cmz[m][n]) / 2 for (m, n) in IDX],
                1: vec(madd(tens(ex, XY), tens(ey, JY), a, b2)), 2: vec(madd(tens(ex, JY), tens(ey, XY), b1, a2))}
        for kap, col in cols.items():
            for r in range(16):
                M[r][4 * kap + l] = col[r]
    return M


def frame(Gm, z=Z3):
    zz = [list(map(F, z)), [-F(t) for t in z]]
    return all(apply(Gm, prodState(zz[a], zz[b])) == prodState(zz[a], zz[(a + b) % 2]) for a in (0, 1) for b in (0, 1))


def relC(Gm, N=NFLIP):
    return meq(mmul(mmul(actC(N), Gm), actC(N)), mmul(actT(N), Gm))


rep.check("0.1 control: the rebuilt family gives the parsed kernel cnot at (1, 1, -1, 1)", meq(fam(1, 1, -1, 1), CNOT))

# ---------------------------------------------------------------- the four reference gates and the converse controls
TMAP = transpose_map()


def ptB(R):
    """Partial transpose on copy B: (a b, a' b') -> (a b', a' b), index 2a + b."""
    return [[R[2 * (r // 2) + (c % 2)][2 * (c // 2) + (r % 2)] for c in range(4)] for r in range(4)]


PTB = superop(lambda w: w_of_rho(ptB(rho_of_w(w))))
rep.check("A.1 [M] T = R_A R_B is the transpose rho -> rho^T, R_B is the partial transpose on copy B, and kernel cnot is "
          "Ad(CNOT): the dictionary identities are exact",
          meq(TT, TMAP) and meq(RB, PTB) and meq(CNOT, conj_map(CNOT_U)))
CN2 = mmul(mmul(RB, CNOT), RB)            # cnot' = R_B cnot R_B
REF = {"cnot": CNOT, "T cnot": mmul(TT, CNOT), "cnot'": CN2, "T cnot'": mmul(TT, CN2)}
rep.check("A.2 cnot commutes with T; cnot' = R_B cnot R_B = R_A cnot R_A; T cnot' = R_B (T cnot) R_B",
          meq(mmul(TT, CNOT), mmul(CNOT, TT)) and meq(CN2, mmul(mmul(RA, CNOT), RA))
          and meq(REF["T cnot'"], mmul(mmul(RB, REF["T cnot"]), RB)))
rep.check("A.3 the four reference gates are CtrlGates at (z3, nflip) and preserve u", all(
    frame(Gm) and relC(Gm) and Gm[0] == [Fr(1)] + [Fr(0)] * 15 for Gm in REF.values()))
rep.note("A.4 [M + L] Q3 := {w : rho(w) PSD}. cnot = Ad(CNOT) and T = transpose preserve Q3 (U rho U^dag and rho^T are "
         "PSD for PSD rho); hence cnot and T cnot preserve Q3, and cnot', T cnot' preserve R_B Q3 = R_B(Q3).")

# local rotations act as Ad of local unitaries: a polynomial identity in the quaternion q, certified on a unisolvent set
QS = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1), (0, 1, 1, 0),
      (0, 1, 0, 1), (0, 0, 1, 1), (1, 2, -1, 3), (2, -1, 1, 1), (3, 1, 4, -1)]
mono = [[F(q[i]) * F(q[j]) for i in range(4) for j in range(i, 4)] for q in QS]
ok_id = True
for q in QS:
    n2 = qnorm2(q)
    U = su2_of_quat(q)
    ok_id &= meq(mscale(actT(rot_from_quat(q)), n2), conj_map(kron(I2, U)))
    ok_id &= meq(mscale(actC(rot_from_quat(q)), n2), conj_map(kron(U, I2)))
rep.check("A.5 [M] |q|^2 actT R(q) = Ad(I (x) U_q) and |q|^2 actC R(q) = Ad(U_q (x) I) at 13 quaternions whose quadratic "
          "monomials have rank 10: both sides are quadratic forms in q, so the identity holds for every q", ok_id
          and rank(mono, 10) == 10)
rep.note("A.6 [L] every R in SO(3) is R(q) for some q (Euler-Rodrigues); so L = actC SO(3) o actT SO(3) preserves Q3 "
         "and R_B Q3 (R_B normalizes L).")

# ---------------------------------------------------------------- Part B: the 16 representatives
SO_DIAG = [diag3(1, 1, 1), diag3(1, -1, -1), diag3(-1, 1, -1), diag3(-1, -1, 1)]
PGRP = [mmul(actC(D), actT(Dp)) for D in SO_DIAG for Dp in SO_DIAG]
rep.check("B.0 the Pauli-sign group P has 16 distinct elements, each local with determinant +1 factors (inside L)",
          len({tuple(flat(g)) for g in PGRP}) == 16)
ADMISSIBLE = [s for s in itertools.product((1, -1), repeat=4) if s[0] * s[2] + s[1] * s[3] == 0]
SHARP = [[Fr(1, 2)] + [Fr(-1, 2) * F(sg) if k == i else Fr(0) for k in range(3)] for i in range(3) for sg in (1, -1)]
PRODS = [prodState([1, 0, 0], Z3), prodState(Z3, [1, 0, 0]), prodState([1, 0, 0], [1, 0, 0]),
         prodState([0, 1, 0], Z3), prodState([1, 0, 0], [0, 1, 0])]


def exclusion_witness(Gm):
    Gi = minv(Gm)
    words = [("G G", [Gm, Gm]), ("G^-1 G^-1", [Gi, Gi])]
    words += [(f"G p{k} G", [Gm, PGRP[k], Gm]) for k in range(16)]
    words += [(f"G^-1 p{k} G", [Gi, PGRP[k], Gm]) for k in range(16)]
    for name, ws in words:
        W = ws[0]
        for m in ws[1:]:
            W = mmul(W, m)
        for pi, p in enumerate(PRODS):
            w = apply(W, p)
            for e in SHARP:
                for f in SHARP:
                    v = pairVal(e, f, w)
                    if v < 0:
                        return (name, pi, e, f, v)
    return None


reps = {}
for s in ADMISSIBLE:
    for oname, O in (("I", I3), ("reflY", REFLY)):
        reps[(s, oname)] = mmul(fam(*s), actT(O))
compatible, excluded = {}, {}
for key, Gm in reps.items():
    hit = None
    for cname, C in REF.items():
        for i1, L1 in enumerate(PGRP):
            for i2, L2 in enumerate(PGRP):
                if meq(mmul(mmul(L1, C), L2), Gm):
                    hit = (cname, i1, i2)
                    break
            if hit:
                break
        if hit:
            break
    if hit:
        compatible[key] = hit
    else:
        excluded[key] = exclusion_witness(Gm)
rep.check("B.1 all 16 representatives are CtrlGates at (z3, nflip) with u o G = u", all(
    frame(Gm) and relC(Gm) and Gm[0] == [Fr(1)] + [Fr(0)] * 15 for Gm in reps.values()))
rep.check(f"B.2 exactly 8 representatives are l1 o c o l2 with l1, l2 in P and c a reference gate ({len(compatible)} found)",
          len(compatible) == 8)
for key, hit in sorted(compatible.items(), key=lambda kv: str(kv[0])):
    rep.note(f"compatible: pattern {key[0]}, O = {key[1]}: = p{hit[1]} o {hit[0]} o p{hit[2]}")
classes = {}
for key, hit in compatible.items():
    classes.setdefault(hit[0], []).append(key)
rep.check("B.3 each of the four reference gates represents exactly two of them (cnot, T cnot -> Q3; cnot', T cnot' -> "
          "R_B Q3)", sorted(len(v) for v in classes.values()) == [2, 2, 2, 2] and len(classes) == 4)
rep.check("B.4 each of the other 8 has an exact word in G^(+-1) and P sending a product outside maxCone (no candidate cone "
          "is invariant under G and L)", len(excluded) == 8 and all(w is not None and w[4] < 0 for w in excluded.values()))
for key, w in sorted(excluded.items(), key=lambda kv: str(kv[0])):
    rep.note(f"excluded: pattern {key[0]}, O = {key[1]}: word {w[0]} on product #{w[1]}, effects "
             f"{[str(c) for c in w[2]]} (x) {[str(c) for c in w[3]]}: value {w[4]}")
chainA = mmul(mmul(RA, CNOT), mmul(RA, CNOT))
chainB = mmul(mmul(RB, CNOT), mmul(RB, CNOT))
p0 = prodState([1, 0, 0], Z3)
eX, eZ = [Fr(1, 2), Fr(1, 2), 0, 0], [Fr(1, 2), 0, 0, Fr(1, 2)]
vA = pairVal(eX, eZ, apply(chainA, p0))
vB = pairVal(eX, eZ, apply(chainB, p0))
rep.check("B.5 the landed chain for both one-copy reflections: (R_A cnot)^2 and (R_B cnot)^2 send prodState xplus z3 to "
          "a vector with value -1/2 on sharp(-e1) (x) sharp(-e3) (K2Guard chain_value K2G:134 for R_B; R_A new)",
          vA == Fr(-1, 2) and vB == Fr(-1, 2), f"{vA}, {vB}")

# ---------------------------------------------------------------- Part C: cross-check with an independent quantum gate
u = G(Fr(3, 5), Fr(4, 5))
Uu = cmul(CNOT_U, [[G(1), G(0), G(0), G(0)], [G(0), G(1), G(0), G(0)], [G(0), G(0), u, G(0)], [G(0), G(0), G(0), u.conj()]])
Gu = conj_map(Uu)
Nu = [[Fr(-7, 25), Fr(24, 25), Fr(0)], [Fr(24, 25), Fr(7, 25), Fr(0)], [Fr(0), Fr(0), Fr(-1)]]
rep.check("C.1 [M] the EQ-E gate CNOT diag(1, 1, u, conj u), u = (3+4i)/5, with its common NOT N_u (EQ-E s6) is a CtrlGate "
          "at (z3, N_u) with u o G = u", frame(Gu) and relC(Gu, Nu) and Gu[0] == [Fr(1)] + [Fr(0)] * 15)
R = rot_axis(2, Fr(3, 5), Fr(4, 5))
Lam, LamI = mmul(actC(R), actT(R)), mmul(actC(tr(R)), actT(tr(R)))
Gp = mmul(mmul(LamI, Gu), Lam)
# Gp(hom z (x) Y) = hom z (x) M0 Y: read M0 from the mu = 0 row (hom z has entry 1 at mu = 0)
M0 =[[apply(Gp, tens(hz, [Fr(1) if k == l else Fr(0) for k in range(4)]))[0][j] for l in range(4)] for j in range(4)]
corner_ok = all(apply(Gp, tens(hz, [Fr(1) if k == l else Fr(0) for k in range(4)])) == tens(hz, [M0[j][l] for j in range(4)])
                for l in range(4))
O3 = [[M0[i + 1][j + 1] for j in range(3)] for i in range(3)]
orthO = m3mul(O3, tr(O3)) == I3 and M0[0] == [1, 0, 0, 0] and [M0[i][0] for i in range(4)] == [1, 0, 0, 0]
Gt = mmul(Gp, actT(tr(O3)))
hit = [s for s in ADMISSIBLE if meq(fam(*s), Gt)]
rep.check("C.2 rotating N_u's axis (3/5, 4/5, 0) to e_x gives a CtrlGate at (z3, nflip) whose corner map is M0 = 1 (+) O, O "
          "orthogonal with O z = z, and Gt = G' o actT(O)^-1 is one of B1's 8 admissible patterns",
          frame(Gp) and relC(Gp) and corner_ok and orthO and [O3[i][2] for i in range(3)] == [0, 0, 1] and len(hit) == 1,
          f"pattern {hit}, O = {[[str(c) for c in r] for r in O3]}")
SU = cm([[1, 0], [0, G(0, 1)]])
Gs = mmul(conj_map(kron(SU, I2)), CNOT)
rels = [relC(Gs, m3mul(m3mul(rot_axis(2, c, s_), NFLIP), tr(rot_axis(2, c, s_))))
        for (c, s_) in [(1, 0), (0, 1), (Fr(3, 5), Fr(4, 5)), (Fr(-4, 5), Fr(3, 5)), (-1, 0)]]
rep.check("C.3 countercontrol (one-directional classification): (S (x) I) CNOT = actC(R_z(pi/2)) o cnot has the frame but "
          "fails relC for the five horizontal pi-rotations tried, so l1 o cnot o l2 need not be a CtrlGate (EQ-E s6 finds no "
          "NOT pair at all)", frame(Gs) and not any(rels))

# ---------------------------------------------------------------- Part D: KAK identities for the group form
c_, s_ = Fr(7, 25), Fr(24, 25)            # cos(theta), sin(theta) with cos(theta/2) = 4/5, sin(theta/2) = 3/5
UXX = cadd(cm([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]), SIG2[(1, 1)], G(Fr(4, 5)), G(0, Fr(-3, 5)))
lhs = mmul(mmul(CNOT, actC(rot_axis(0, c_, s_))), CNOT)
rep.check("D.1 [M] cnot o actC(R_x(theta)) o cnot = Ad(exp(-i theta XX/2)) at cos(theta/2) = 4/5 (exact; CNOT (X (x) I) "
          "CNOT = X (x) X)", meq(lhs, conj_map(UXX)))
Rz90 = rot_axis(2, 0, 1)
Ry90 = rot_axis(1, 0, 1)
LYY = mmul(actC(Rz90), actT(Rz90))
LZZ = mmul(actC(Ry90), actT(Ry90))
UYY = cadd(cm([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]), SIG2[(2, 2)], G(Fr(4, 5)), G(0, Fr(-3, 5)))
UZZ = cadd(cm([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]), SIG2[(3, 3)], G(Fr(4, 5)), G(0, Fr(-3, 5)))
rep.check("D.2 [M] the YY and ZZ factors are local-rotation conjugates of the XX factor: L_YY (lhs) L_YY^-1 = "
          "Ad(exp(-i theta YY/2)) with L_YY = actC R_z(pi/2) actT R_z(pi/2), and likewise ZZ with R_y(pi/2) (exact)",
          meq(mmul(mmul(LYY, lhs), minv(LYY)), conj_map(UYY)) and meq(mmul(mmul(minv(LZZ), lhs), LZZ), conj_map(UZZ)))
XX, YY, ZZ = SIG2[(1, 1)], SIG2[(2, 2)], SIG2[(3, 3)]
rep.check("D.3 XX, YY, ZZ commute pairwise (so exp(-i(a XX + b YY + c ZZ)) factorizes)",
          all(cmul(P, Q) == cmul(Q, P) for P, Q in [(XX, YY), (XX, ZZ), (YY, ZZ)]))
rep.note("D.4 [L, unverified] KAK (Khaneja-Glaser 2001; Kraus-Cirac 2001): every U in SU(4) is (A (x) B) exp(-i(a XX + "
         "b YY + c ZZ)) (C (x) D). With D.1-D.3 every Ad U is a word in L and cnot L cnot, so <L, cnot L cnot> = "
         "Ad(SU(4)) exactly; the twisted case is its R_B conjugate.")
rep.verdict("ORIENTATION-CLASSES: of the 16 representatives, 8 are p o c o p' with c in {cnot, T cnot} (Q3) or {cnot', "
            "T cnot'} (R_B Q3), and 8 have an exact word leaving maxCone; the EQ-E quantum gate lands on an admissible "
            "pattern; the KAK factors of the group form are words in L and cnot L cnot")
