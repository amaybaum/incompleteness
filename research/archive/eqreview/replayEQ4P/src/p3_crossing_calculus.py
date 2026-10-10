"""EQ4-P probe p3 -- coordinator expectation E2 (the crossing-constraint calculus), exact.  Research only.

Usage:  python3 -I -B p3_crossing_calculus.py <base>/verification/lean-mathlib/OIBridge
Imports only the own library eq4_lib.py.

Setting.  A family S = A u B = C u D with P = A n C, Q = A n D, R = B n C, U = B n D.  States x on C = P u R and y on
D = Q u U (a product under C|D), effects e on A and f on B (a product under A|B).  KT gives tr[(e (x) f)(x (x) y)] >= 0.
Link map of x read from R to P:  Lam_x(g) = tr_R[(g_R (x) 1) x]; claimed Choi matrix PT_R(x) ("with transposes").

DECISION RULE (fixed before the first run; rules, not expected numbers).  VERDICT `P3-CROSSING-CALCULUS-EXACT` iff all:
  K  transcription control.
  E  (E1) for random exact Hermitian x (on P u R), Choi(Lam_x) = PT_R(x) on all input units (3 instances, |R| = 1, 2);
     (E2) the conditional tr_B[(f (x) 1)(x (x) y)] equals (Lam_x (x) Lam_y)(f), computed independently from the Choi
     matrix PT_R(x) (x) PT_U(y), on all units f of B, for random exact x, y and each crossing type
     (|P|,|Q|,|R|,|U|) = (1,1,1,2) [5 tokens], (1,1,1,3), (1,1,2,2), (2,1,1,2), (1,2,1,2) [6 tokens];
     (E3) value = tr[e (Lam_x (x) Lam_y)(f)] on 2 random exact (e, f) per type.  Countercontrol: the Choi matrix x
     itself (no partial transpose) gives a different map on some unit for a random x.
  M  one empty intersection (Q empty, A = P inside C): tr[(e (x) f)(x (x) y)] = tr[f (cond_A(e; x) (x) y)] on 3 random
     exact instances (5 tokens), so the constraint factors through the conditional state of C's subfamily and B's
     product (written argument in NOTES).
  U  uniform corollary: (U1) Choi(Lam_y o T_U) = y on all units, random exact y (|U| = 1, 2); (U2) with Bell links x
     between P and R (|P| = |R| = m) and f = T(g): cond = 2^-m (rename R->P (x) Phi_y)(g), Phi_y the map with Choi y,
     on all units g, for (n, a, b) = (3, 2, 2) [6 tokens], (4, 1, 2) [7 tokens], (2, 2, 1) [5 tokens], (3, 1, 2)
     [5 tokens]; (U3) twin links and f = g (c = 1): cond = 2^-m (rename (x) Lam_y)(g) with Choi(Lam_y) = PT_U(y), same
     cases; countercontrol: the c = 0 and c = 1 maps differ on some unit.
  G  general-chart 3|3 links: with link states H_Ri = pauli(homMap R_i) on (i, 3 + i), R_i rational in O(3) (mixed
     determinants), the conditional of every unit f on (3,4,5) equals (1/8)(M_R0 (x) M_R1 (x) M_R2)(f renamed),
     M_R the one-token map with coordinate action homMap(R) (two triples of R's).
  T  teleportation for k = 2 (four tokens) and k = 4 (six tokens): Bell state on (z,q), Bell effect on (z,p): the
     conditional of every unit y on {p} u S is (1/4) y(p -> q).
"""
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
import eq4_lib as L  # noqa: E402

BASE = sys.argv[1]
rep = L.Report("p3_crossing_calculus")
rng = random.Random(20261009 + 3)
rep.check("K0 transcription control", L.transcription_control(BASE)[0])


def rand_small(qs):
    """sparse-ish random exact Hermitian operator (keeps the 6-token checks fast)."""
    N = 2 ** len(qs)
    d = {}
    for r in range(N):
        for c in range(r, N):
            if rng.random() < (0.5 if N > 8 else 1.0):
                v = L.rand_gauss(rng)
                if r == c:
                    v = L.G(v.re)
                d[(r, c)] = v
                d[(c, r)] = v.conj()
    return L.Op(qs, d)


# ------------------------------------------------------------------------------------------------ E general identity
ok_e1 = True
for (P, R) in (((0,), (1,)), ((0, 1), (2,)), ((0,), (1, 2))):
    x = rand_small(P + R)
    J = L.choi(lambda g, x=x, R=R: L.lam(x, R, g), R, P)
    ok_e1 &= J == L.reorder(L.ptranspose(x, R), R + P)
rep.check("E1 Choi(Lam_x) = PT_R(x) on all input units (|P|,|R|) = (1,1), (2,1), (1,2), random exact x", ok_e1)

TYPES = [((0,), (1,), (2,), (3, 4)), ((0,), (1,), (2,), (3, 4, 5)), ((0,), (1,), (2, 3), (4, 5)),
         ((0, 1), (2,), (3,), (4, 5)), ((0,), (1, 2), (3,), (4, 5))]
ok_e2 = ok_e3 = True
cc_e = False
for (P, Q, R, U) in TYPES:
    x = rand_small(P + R)
    y = rand_small(Q + U)
    X = L.tensor(x, y)
    J = L.tensor(L.reorder(L.ptranspose(x, R), R + P), L.reorder(L.ptranspose(y, U), U + Q))
    J = L.reorder(J, R + U + P + Q)
    Jbad = L.reorder(L.tensor(L.reorder(x, R + P), L.reorder(y, U + Q)), R + U + P + Q)
    for _, f in L.units(R + U):
        lhs = L.reorder(L.cond(f, X), P + Q)
        rhs = L.apply_choi(J, R + U, P + Q, f)
        ok_e2 &= lhs == rhs
        if not cc_e and L.apply_choi(Jbad, R + U, P + Q, f) != rhs:
            cc_e = True
    for _ in range(2):
        e = rand_small(P + Q)
        f = rand_small(R + U)
        val = L.pair(L.tensor(e, f), X)
        ok_e3 &= val == L.pair(e, L.apply_choi(J, R + U, P + Q, f))
rep.check("E2 conditional = (Lam_x (x) Lam_y)(f) via the Choi matrix PT_R(x) (x) PT_U(y), all units f, crossing types "
          "(1,1,1,2), (1,1,1,3), (1,1,2,2), (2,1,1,2), (1,2,1,2)", ok_e2)
rep.check("E3 value = tr[e (Lam_x (x) Lam_y)(f)] (2 random exact (e, f) per type); countercontrol: the Choi matrix "
          "without partial transposes gives a different map", ok_e3 and cc_e)

# ------------------------------------------------------------------------------------------------ M one empty intersection
ok_m = True
for _ in range(3):
    A_, R_, U_ = (0, 1), (2,), (3, 4)
    x = rand_small(A_ + R_)
    y = rand_small(U_)
    e = rand_small(A_)
    f = rand_small(R_ + U_)
    val = L.pair(L.tensor(e, f), L.tensor(x, y))
    condR = L.cond(e, x)
    ok_m &= val == L.pair(f, L.tensor(condR, y))
rep.check("M one empty intersection (Q empty): tr[(e (x) f)(x (x) y)] = tr[f (cond_A(e; x) (x) y)] (3 random exact)",
          ok_m)


# ------------------------------------------------------------------------------------------------ U uniform corollary
def bell_links(Ps, Rs, kind):
    mk = L.phi_plus if kind == 0 else L.swap_half
    return L.tensor(*[mk(Ps[i], Rs[i]) for i in range(len(Ps))])


ok_u1 = True
for (Qs, Us) in (((0,), (1,)), ((0, 1), (2,)), ((0,), (1, 2))):
    y = rand_small(Qs + Us)
    J = L.choi(lambda h, y=y, Us=Us: L.lam(y, Us, L.transpose(h)), Us, Qs)
    ok_u1 &= J == L.reorder(y, Us + Qs)
rep.check("U1 Choi(Lam_y o T_U) = y on all input units (random exact y; |U| = 1, 2)", ok_u1)
CASES = [((0,), (1, 2), (3,), (4, 5)), ((0, 1), (2, 3), (4, 5), (6,)), ((0,), (1,), (2,), (3, 4)),
         ((0,), (1, 2), (3,), (4,))]
ok_u2 = ok_u3 = True
cc_u = False
for (Ps, Qs, Rs, Us) in CASES:
    y = rand_small(Qs + Us)
    m = len(Ps)
    ren = {Rs[i]: Ps[i] for i in range(m)}
    for kind in (0, 1):
        X = L.tensor(bell_links(Ps, Rs, kind), y)
        for _, g in L.units(Rs + Us):
            f = L.transpose(g) if kind == 0 else g
            lhs = L.reorder(L.cond(f, X), Ps + Qs)
            # rename R -> P on the R part, map U -> Q by Phi (c = 0: Choi y; c = 1: Choi PT_U(y))
            Jy = L.reorder(y, Us + Qs) if kind == 0 else L.reorder(L.ptranspose(y, Us), Us + Qs)
            Jfull = L.reorder(L.tensor(L.reorder(L.tensor(*[L.Op((Rs[i], Ps[i]),
                                                                 {(a * 2 + a, b * 2 + b): L.ONE
                                                                  for a in range(2) for b in range(2)})
                                                            for i in range(m)]), tuple(Rs) + tuple(Ps)),
                                           Jy), Rs + Us + Ps + Qs)
            # the identity channel R_i -> P_i has Choi sum_ab |a><b| (x) |a><b| (unnormalized), as built above
            rhs = L.apply_choi(Jfull, Rs + Us, Ps + Qs, g).scale(Fr(1, 2 ** m))
            if kind == 0:
                ok_u2 &= lhs == rhs
            else:
                ok_u3 &= lhs == rhs
        if kind == 0:
            X1 = L.tensor(bell_links(Ps, Rs, 1), y)
            for _, g in L.units(Rs + Us):
                if L.reorder(L.cond(L.transpose(g), X), Ps + Qs) != L.reorder(L.cond(g, X1), Ps + Qs):
                    cc_u = True
                    break
rep.check("U2 c = 0: Bell links and f = T(g): cond = 2^-m (rename (x) Phi_y)(g), Choi(Phi_y) = y, all units g; "
          "(n,a,b) = (3,2,2), (4,1,2), (2,2,1), (3,1,2)", ok_u2)
rep.check("U3 c = 1: twin links and f = g: cond = 2^-m (rename (x) Lam_y)(g), Choi(Lam_y) = PT_U(y), same cases; "
          "countercontrol: the c = 0 and c = 1 maps differ", ok_u3 and cc_u)


# ------------------------------------------------------------------------------------------------ G general-chart links
def rot_of(qq):
    w = qq[0]
    return L.quat_rot(qq[1] / w, qq[2] / w, qq[3] / w)


def local_map_apply(H, qtok, Y):
    others = tuple(x_ for x_ in Y.qs if x_ != qtok)
    Yr = L.reorder(Y, (qtok,) + others)
    out = L.Op((qtok,) + others, {})
    for i in range(2):
        for j in range(2):
            cu = L.coords1(L.unit((qtok,), i, j))
            img = L.pauli1([sum((L.G.of(H[r][c]) * cu[c] for c in range(4)), L.ZERO) for r in range(4)], qtok)
            out = out + L.tensor(img, L.cond(L.unit((qtok,), j, i), Yr))
    return L.reorder(out, Y.qs)


QS = [(Fr(1), Fr(1, 2), Fr(-1, 3), Fr(2, 5)), (Fr(1), Fr(-2, 3), Fr(1, 4), Fr(1, 2)),
      (Fr(1), Fr(1, 3), Fr(1, 3), Fr(-1, 2))]
ok_g = True
for dets in ((-1, 1, -1), (1, 1, -1)):
    Rs_ = [rot_of(QS[i]) if dets[i] == 1 else L.mat_mul(rot_of(QS[i]), L.REFLY) for i in range(3)]
    lk = L.tensor(*[L.pauli2(L.homtab(Rs_[i]), (i, 3 + i)) for i in range(3)])
    for _, f in L.units((3, 4, 5)):
        lhs = L.reorder(L.cond(f, lk), (0, 1, 2))
        rhs = L.reorder(L.relabel(f, {3: 0, 4: 1, 5: 2}), (0, 1, 2))
        for i in range(3):
            rhs = local_map_apply(L.homtab(Rs_[i]), i, rhs)
        ok_g &= lhs == rhs.scale(Fr(1, 8))
rep.check("G general-chart 3|3 links: conditional = (1/8)(M_R0 (x) M_R1 (x) M_R2)(f renamed) on all 64 units, two "
          "mixed-determinant triples of rational O(3) matrices", ok_g)

# ------------------------------------------------------------------------------------------------ T teleportation, k=2,4
ok_t = True
for (z, p, q, S) in ((3, 0, 2, (1,)), (5, 0, 4, (1, 2, 3))):
    for _, y in L.units((p,) + S):
        lhs = L.reorder(L.cond(L.phi_plus(z, p), L.tensor(L.phi_plus(z, q), y)), (q,) + S)
        ok_t &= lhs == L.reorder(L.relabel(y, {p: q}), (q,) + S).scale(Fr(1, 4))
rep.check("T teleportation for k = 2 (4 tokens) and k = 4 (6 tokens): conditional = (1/4) y(p -> q), all units", ok_t)

rep.verdict("P3-CROSSING-CALCULUS-EXACT")
