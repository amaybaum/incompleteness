"""Exact check of every intermediate statement of the replacement route in RelcSelectBlock.lean
(gt_center_two_ctrl, hcen, hext, h0, phi_lift_minus_ctrl, actT_slice_ctrl) on the d = 3 gates of
the REL-C thread: cnot (GateRel, positive), G_R (relC only, positive) and the countercontrol KG
(frame + relC, not positive).  Reuses relc/relc_probe.py's exact (Fraction) carrier."""
import os, sys
from fractions import Fraction as Fr
sys.path.insert(0, "/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/relc")
import relc_probe as P

n, Z, N = 4, P.Z3, P.NFLIP
H = P.homMap(N)
e = lambda mu: [Fr(int(i == mu)) for i in range(n)]
h0 = P.hom([0, 0, 0])
add = lambda a, b: [x + y for x, y in zip(a, b)]
sub = lambda a, b: [x - y for x, y in zip(a, b)]
smul = lambda s, a: [s * x for x in a]
mv = lambda M, v: [sum(M[i][j] * v[j] for j in range(n)) for i in range(n)]
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
wadd = lambda A, B: [[x + y for x, y in zip(r, s)] for r, s in zip(A, B)]
wsmul = lambda s, A: [[s * x for x in r] for r in A]
us = [e(2), e(3), [0, 0, Fr(3, 5), Fr(4, 5)]]           # unit, head 0, in E- of homMap nflip
cs = [[1, 0, 0], [0, 1, 0], [Fr(3, 5), Fr(-4, 5), 0], [Fr(1, 2), Fr(1, 3), 0]]  # c perp z3, |c| <= 1
assert all(dot(u, u) == 1 and u[0] == 0 and mv(H, u) == smul(-1, u) for u in us)
assert all(sum(Fr(x) ** 2 for x in c) <= 1 and Fr(c[2]) == 0 for c in cs)
KG = P.KG_factory()
def KGinv(w):
    o = [list(r) for r in w]; o[1][1], o[2][2] = o[2][2], o[1][1]; return P.cnot(o)
results = {}
for name, G, Gi in (("cnot", P.cnot, P.cnot), ("G_R", P.GR, P.GR_inv), ("KG", KG, KGinv)):
    Mf, Mi = P.corner_maps(G, Gi, Z)
    Phi = lambda a, c, f, t: P.Phi(G, Mi, a, c, f, t)
    s1 = all(P.eq(wsmul(2, G(P.tens(h0, mv(Mi, t)))),
                  wadd(P.tens(P.hom(Z), t), P.tens(P.hom([-x for x in Z]), mv(H, t)))) for t in map(e, range(n)))
    s2 = s3 = s4 = s5 = True
    for c in cs:
        for u in us:
            f = sub(h0, u)
            s2 &= all(P.pairVal(e(m), f, G(P.tens(h0, mv(Mi, f)))) == dot(e(m), P.hom(Z)) for m in range(n))
            s3 &= all(Phi(e(m), c, f, f) == -2 * Phi(e(m), c, u, h0) for m in range(n))
            F = lambda a: P.pairVal(a, f, G(P.tens(P.hom(c), mv(Mi, f))))
            s4 &= F(P.hom([-x for x in Z])) == 0
            s5 &= all(Phi(e(m), c, u, h0) == 0 for m in range(n))
    s6 = all(P.eq(P.actT(N, G(P.tens(P.lift(c), mv(Mi, h0)))), G(P.tens(P.lift(c), mv(Mi, h0)))) for c in cs)
    results[name] = (s1, s2, s3, s4, s5, s6)
    print(f"{name:5s} gt_center_two={s1} hcen={s2} hext={s3} F(hom -z)=0:{s4} "
          f"Phi(.;u,h0)=0:{s5} actT_slice={s6}")
ctrl_pos = all(all(results[g]) for g in ("cnot", "G_R"))
ctrl_neg = results["KG"][0] and results["KG"][1] and not results["KG"][2] and not results["KG"][5]
print("controls: positive gates satisfy every step:", "PASS" if ctrl_pos else "FAIL")
print("countercontrol KG (not positive): centre steps hold, positivity-derived step and conclusion fail:",
      "PASS" if ctrl_neg else "FAIL")
if ctrl_pos and ctrl_neg:
    print("VERDICT: each intermediate statement of the replacement route holds on cnot and G_R; on KG the "
          "chain breaks at the positivity-derived identity hext and the conclusion fails")
sys.exit(0 if ctrl_pos and ctrl_neg else 1)
