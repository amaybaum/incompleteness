"""EQ-B / B6 (QB2): continuous reversibility gives pure-state transitivity, not boundary transitivity.

K-infinity-Trans (BoundaryTransitive) <=> PureTrans (transitive on extreme points) AND BP (every boundary state is
extreme), for compact convex bodies with interior: => by TRB-1's boundary purity
(extreme_of_isBoundaryState_of_transitive) and extreme points being boundary states; <= trivially.
Exact facts checked here:
  Q1 qutrit (complex QT, PU(3) transitive on pure states): rho = diag(1,1,0)/2 is a state, annihilated by the
     nonzero effect |2><2| (so not interior), and is the midpoint of two distinct pure states (not extreme):
     complex QT satisfies continuous reversibility and violates BP beyond the elementary system.
  Q2 the Caratheodory orbitope C = conv{(cos t, sin t, cos 2t, sin 2t)} with the SO(2) action rot(p) + rot(2p):
     (a) the action carries the curve to itself and is transitive on it (exact at rational points);
     (b) the curve lies on the sphere |v|^2 = 2, so every curve point is extreme; extreme points of C = the curve;
     (c) C has interior in R^4 (five rational curve points affinely independent);
     (d) m = (0,0,1,0) = (g(0) + g(pi))/2 is a boundary point (v3 <= 1 on C, v3(m) = 1) and is not extreme,
         so no body-preserving family is boundary transitive on C (kernel not_boundaryTransitive_of_nonextreme_boundary);
     (e) capacity >= 3: the Fejer effects e_i(v) = (3 + 4 <(v1,v2), u_i> + 2 <(v3,v4), u_i^(2)>)/9 at the three
         cube-root directions are nonnegative on C (|1 + w + w^2|^2 identity), sum to 1, and e_i(g_j) = delta_ij:
         C is not an elementary (capacity-two) body, so it is not a countermodel inside the elementary scope.
  Q3 the drive control: on ball3 the flow family rot3 has BP (the ball) and fails PureTrans (kernel
     not_boundaryTransitive_flow) — the other independent direction, recorded from the kernel.
Run: python3 -I -B b6_qb2.py
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from blib import *   # noqa: E402
import sympy as sp   # noqa: E402

checks = []


def chk(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)


def curve(c, s):
    return [c, s, c * c - s * s, 2 * c * s]


def rot_act(cp, sp_):
    """rot(p) (+) rot(2p) with cos p = cp, sin p = sp_."""
    c2, s2 = cp * cp - sp_ * sp_, 2 * cp * sp_
    return [[cp, -sp_, 0, 0], [sp_, cp, 0, 0], [0, 0, c2, -s2], [0, 0, s2, c2]]


def main():
    # ---------------- Q1 qutrit
    rho = [[Fr(1, 2), 0, 0], [0, Fr(1, 2), 0], [0, 0, Fr(0)]]
    E2 = [[0, 0, 0], [0, 0, 0], [0, 0, Fr(1)]]
    tr = lambda A: sum(A[i][i] for i in range(3))
    mul = lambda A, B: [[sum(Fr(A[i][k]) * Fr(B[k][j]) for k in range(3)) for j in range(3)] for i in range(3)]
    p0 = [[Fr(1), 0, 0], [0, 0, 0], [0, 0, 0]]
    p1 = [[0, 0, 0], [0, Fr(1), 0], [0, 0, 0]]
    chk("Q1 qutrit: rho = diag(1,1,0)/2 has trace 1 and tr(E2 rho) = 0 for the nonzero effect E2 = |2><2| "
        "(a boundary state)", tr(rho) == 1 and tr(mul(E2, rho)) == 0)
    chk("Q1 qutrit: rho = (|0><0| + |1><1|)/2, the midpoint of two distinct pure states (not extreme)",
        all(rho[i][j] == (Fr(p0[i][j]) + Fr(p1[i][j])) / 2 for i in range(3) for j in range(3)))

    # ---------------- Q2 Caratheodory orbitope
    pts = [(Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(-1), Fr(0)), (Fr(0), Fr(-1)), (Fr(3, 5), Fr(4, 5)),
           (Fr(-5, 13), Fr(12, 13)), (Fr(8, 17), Fr(-15, 17))]
    P = [curve(c, s) for (c, s) in pts]
    ok_a = True
    for (cp, spp) in ((Fr(3, 5), Fr(4, 5)), (Fr(-7, 25), Fr(24, 25))):
        Rm = rot_act(cp, spp)
        for (c, s) in pts:
            img = matvec(Rm, curve(c, s))
            # angle addition: (c, s) * (cp, spp)
            cn, sn = c * cp - s * spp, s * cp + c * spp
            if img != curve(cn, sn):
                ok_a = False
    chk("Q2(a) the SO(2) action rot(p)+rot(2p) maps g(t) to g(t+p) (exact at rational angles)", ok_a)
    chk("Q2(b) every curve point lies on the sphere |v|^2 = 2 (hence is extreme)",
        all(sum(t * t for t in v) == 2 for v in P))
    diffs = [[P[k][i] - P[0][i] for i in range(4)] for k in range(1, 5)]
    chk("Q2(c) five rational curve points are affinely independent (C has interior in R^4)", rank(diffs) == 4)
    m = [(P[0][i] + P[2][i]) / 2 for i in range(4)]
    chk("Q2(d) m = (g(0)+g(pi))/2 = (0,0,1,0); v3 = cos 2t <= 1 on the curve with v3(m) = 1 (boundary, not extreme)",
        m == [0, 0, 1, 0] and all(v[2] <= 1 for v in P))
    # (e) Fejer effects (symbolic, exact with sqrt(3))
    t = sp.symbols("t", real=True)
    w = sp.exp(sp.I * t)
    fej = sp.simplify(sp.expand(sp.Abs(1 + w + w ** 2) ** 2).rewrite(sp.cos))
    ident = sp.simplify(sp.expand((3 + 4 * sp.cos(t) + 2 * sp.cos(2 * t)) - (1 + w + w ** 2) * (1 + 1 / w + 1 / w ** 2)))
    chk("Q2(e) identity 3 + 4cos a + 2cos 2a = |1 + e^{ia} + e^{2ia}|^2 (so the Fejer effects are >= 0 on C)",
        sp.simplify(ident.rewrite(sp.exp)) == 0)
    th = [0, 2 * sp.pi / 3, 4 * sp.pi / 3]
    v1, v2, v3, v4 = sp.symbols("v1 v2 v3 v4", real=True)

    def eff(ti):
        return (3 + 4 * (v1 * sp.cos(ti) + v2 * sp.sin(ti)) + 2 * (v3 * sp.cos(2 * ti) + v4 * sp.sin(2 * ti))) / 9
    effs = [eff(ti) for ti in th]
    chk("Q2(e) the three Fejer effects sum to the unit functional", sp.simplify(sum(effs) - 1) == 0)
    gpts = [[sp.cos(tj), sp.sin(tj), sp.cos(2 * tj), sp.sin(2 * tj)] for tj in th]
    okd = True
    for i in range(3):
        for j in range(3):
            val = sp.nsimplify(sp.simplify(effs[i].subs({v1: gpts[j][0], v2: gpts[j][1], v3: gpts[j][2], v4: gpts[j][3]})))
            if val != (1 if i == j else 0):
                okd = False
    chk("Q2(e) e_i(g(2 pi j/3)) = delta_ij: three perfectly distinguishable states (capacity >= 3)", okd)
    # value of e_0 on a general curve point is (3 + 4 cos t + 2 cos 2t)/9 in [0, 1]
    e0t = sp.simplify(effs[0].subs({v1: sp.cos(t), v2: sp.sin(t), v3: sp.cos(2 * t), v4: sp.sin(2 * t)}))
    chk("Q2(e) e_0 on the curve equals (3 + 4cos t + 2cos 2t)/9", sp.simplify(e0t - (3 + 4 * sp.cos(t) + 2 * sp.cos(2 * t)) / 9) == 0)

    nfail = sum(1 for _, ok in checks if not ok)
    print(f"b6_qb2: {len(checks) - nfail}/{len(checks)} checks PASS")
    print("VERDICT", "B6-GREEN" if nfail == 0 else "B6-RED")
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
