"""EQ4-P probe p2 -- one-token teleportation crossings: triple-level uniformity inside six tokens, exact.

Usage:  python3 -I -B p2_teleport.py <base>/verification/lean-mathlib/OIBridge
Imports only the own library eq4_lib.py.

Claim under test (found while planning; to be checked, not assumed).  In a five-token family {z, p, q, s, t} take the
two bipartitions zp|qst and zq|pst.  KT on that family makes every product of states x(z,q) (x) y(p,s,t) a state and
every product of effects e(z,p) (x) g(q,s,t) an effect, so tr[(e (x) g)(x (x) y)] >= 0.  With the Bell state on the
standalone pair (z,q) and the Bell effect on the standalone pair (z,p) (both from the native gate), the conditional on
(q,s,t) should be y with token p renamed q (a teleportation).  With closedness and full effects this gives
K_pst <= K_qst (renamed), and the reverse roles give equality.  Three such steps inside six tokens relate the disjoint
triples (0,1,2) and (3,4,5); three steps inside five tokens give token permutations of one triple.

DECISION RULE (fixed before the first run; rules, not expected numbers).  VERDICT `P2-TELEPORT-EXACT` iff all pass:
  K  transcription control.
  A  aligned charts, family (z,p,q,s,t) = (4,0,3,1,2): (A1) with the Bell state Phi+ on (z,q) and the Bell effect Phi+
     on (z,p), cond_(z,p)[Phi+_zp ; Phi+_zq (x) y] = (1/4) y(p -> q) on all 64 units y on (p,s,t); (A2) the reverse
     roles give (1/4) y'(q -> p) on all units y' on (q,s,t); (A3) twin links SWAP/2 on both pairs give (1/4) y(p -> q);
     a mixed pair (one Bell, one twin, either way round) gives (1/4) PT_q(y(p -> q)); (A4) countercontrol: the product
     state |0><0| (x) |0><0| in place of the Bell state does not give (1/4) y(p -> q) on some unit.
  B  six tokens: (B1) the A1 and A2 identities hold for each of the three steps (4,0,3,1,2), (5,1,4,3,2), (0,2,5,3,4);
     their composite maps every unit y on (0,1,2) to (1/64) y(0->3, 1->4, 2->5); (B2) certificate against
     (K012, K345) = (BS*, BS): GHZ is PSD (so in BS* = K012) and W3 = 1/2 - GHZ is in BS* = K345* (Cauchy-Schwarz SOS,
     symbolic, plus the overlap formula); after steps 1-2 the state is GHZ on (3,4,2); the step-3 five-token value
     tr[(Phi+_02 (x) W3_345)(Phi+_05 (x) GHZ_342)] is negative; (B3) c = 1 analogue against (B_tw*, B_tw): twin links,
     the step-3 value with G (in B_tw* = K012, teleported) and the effect F (in B_tw* = K345*) is negative (F, G and
     their membership as in p1 T1); (B4) controls: GHZ teleported and paired with the PSD effect GHZ gives a value >= 0,
     and a biseparable state teleported and paired with W3 gives a value >= 0.
  C  five tokens {0,1,2,3,4}, z = 4: the composite of the teleportations 0->3, 1->0, 3->1 equals the token swap (0 1)
     on every unit of (0,1,2), and 1->3, 2->1, 3->2 equals the swap (1 2) (times 1/64): K012 is S_3-invariant from KT
     on five tokens.
  D  general charts: Bell states H_R = pauli(homMap R) for rational R in O(3) (Euler-Rodrigues rotations, times reflY
     for det -1): (D1) H_R is PSD for every det -1 instance and not PSD for every det +1 instance; (D2) with the state
     link H_R1 on (z,q) and the effect link H_R2 on (z,p), the conditional equals (1/4)(M (x) id)(y(p -> q)), M the
     one-token map with coordinate action homMap(R1^T R2), on all 64 units y (8 (R1, R2) pairs, all four det patterns);
     (D3) for det R1 = det R2 = -1, homMap(R1^T R2) = Ad(U)/n for the explicit rational quaternion
     sigma(conj(q1) q2), sigma(w,x,y,z) = (w,-x,y,-z) (a local unitary); for mixed determinants homMap(R1^T R2) reflY
     is such an Ad(U)/n (a transpose up to a local unitary); (D4) with tau_ij = e_i + e_j + c (mod 2) the parity
     tau_zq + tau_zp equals e_p + e_q for all e in {0,1}^5, c in {0,1}.
Exact Gaussian-rational arithmetic only (eq4_lib), plus one small sympy SOS identity.
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
import sympy as sp  # noqa: E402

import eq4_lib as L  # noqa: E402

BASE = sys.argv[1]
rep = L.Report("p2_teleport")
rng = random.Random(20261009 + 2)
rep.check("K0 transcription control", L.transcription_control(BASE)[0])


def link(kind, a, b):
    return L.phi_plus(a, b) if kind == 0 else L.swap_half(a, b)


def teleport(y, z, p, q, st, kind_state=0, kind_eff=0, state_link=None, eff_link=None):
    """cond_(z,p)[e_zp ; x_zq (x) y], y on (p, s, t); result on (q, s, t)."""
    x = state_link if state_link is not None else link(kind_state, z, q)
    e = eff_link if eff_link is not None else link(kind_eff, z, p)
    return L.reorder(L.cond(e, L.tensor(x, y)), (q,) + tuple(st))


def ren(y, mp, order):
    return L.reorder(L.relabel(y, mp), order)


# ------------------------------------------------------------------------------------------------ A aligned
z, p, q, s, t = 4, 0, 3, 1, 2
ok_a1 = ok_a2 = ok_a3 = True
for _, y in L.units((p, s, t)):
    target = ren(y, {p: q}, (q, s, t)).scale(Fr(1, 4))
    ok_a1 &= teleport(y, z, p, q, (s, t)) == target
    ok_a3 &= teleport(y, z, p, q, (s, t), 1, 1) == target
    ok_a3 &= teleport(y, z, p, q, (s, t), 0, 1) == L.ptranspose(target, [q])
    ok_a3 &= teleport(y, z, p, q, (s, t), 1, 0) == L.ptranspose(target, [q])
for _, y in L.units((q, s, t)):
    ok_a2 &= teleport(y, z, q, p, (s, t)) == ren(y, {q: p}, (p, s, t)).scale(Fr(1, 4))
rep.check("A1 Bell state on (z,q), Bell effect on (z,p): conditional = (1/4) y(p -> q) on all 64 units", ok_a1)
rep.check("A2 reverse roles: conditional = (1/4) y'(q -> p) on all 64 units", ok_a2)
rep.check("A3 twin links on both pairs: (1/4) y(p -> q); one twin and one Bell link (either way round): "
          "(1/4) PT_q(y(p -> q)), all units", ok_a3)
prod = L.tensor(L.ket_op([1, 0], (z,)), L.ket_op([1, 0], (q,)))
cc = any(teleport(y, z, p, q, (s, t), state_link=prod) != ren(y, {p: q}, (q, s, t)).scale(Fr(1, 4))
         for _, y in L.units((p, s, t)))
rep.check("A4 countercontrol: a product link state does not teleport (differs on some unit)", cc)

# ------------------------------------------------------------------------------------------------ B six tokens
STEPS = [(4, 0, 3, (1, 2)), (5, 1, 4, (3, 2)), (0, 2, 5, (3, 4))]
ok_b1 = True
for (z_, p_, q_, st) in STEPS:
    for _, y in L.units((p_,) + st):
        ok_b1 &= teleport(y, z_, p_, q_, st) == ren(y, {p_: q_}, (q_,) + st).scale(Fr(1, 4))
    for _, y in L.units((q_,) + st):
        ok_b1 &= teleport(y, z_, q_, p_, st) == ren(y, {q_: p_}, (p_,) + st).scale(Fr(1, 4))
comp_ok = True
for _, y in L.units((0, 1, 2)):
    y1 = teleport(y, 4, 0, 3, (1, 2))                       # on (3,1,2)
    y1 = L.reorder(y1, (1, 3, 2))
    y2 = teleport(y1, 5, 1, 4, (3, 2))                      # on (4,3,2)
    y2 = L.reorder(y2, (2, 3, 4))
    y3 = teleport(y2, 0, 2, 5, (3, 4))                      # on (5,3,4)
    comp_ok &= L.reorder(y3, (3, 4, 5)) == ren(y, {0: 3, 1: 4, 2: 5}, (3, 4, 5)).scale(Fr(1, 64))
rep.check("B1 each of the three steps satisfies A1 and A2 (all units); the composite maps every unit y on (0,1,2) "
          "to (1/64) y(0->3, 1->4, 2->5)", ok_b1 and comp_ok)
# membership facts for the certificate (small, self-contained re-checks)
a0r, a0i, a1r, a1i = sp.symbols("a0r a0i a1r a1i", real=True)
cr = sp.symbols("cr0:4", real=True)
ci = sp.symbols("ci0:4", real=True)
a = [a0r + sp.I * a0i, a1r + sp.I * a1i]
chi = [cr[k] + sp.I * ci[k] for k in range(4)]
ab2 = lambda w: sp.expand(w * sp.conjugate(w))
na, nchi = ab2(a[0]) + ab2(a[1]), sum(ab2(c) for c in chi)
sos = sp.expand(sp.Rational(1, 2) * na * nchi - sp.Rational(1, 2) * ab2(a[0] * chi[0] + a[1] * chi[3])
                - sp.Rational(1, 2) * na * (ab2(chi[1]) + ab2(chi[2]))
                - sp.Rational(1, 2) * ab2(a[0] * sp.conjugate(chi[3]) - a[1] * sp.conjugate(chi[0]))) == 0
X3 = (3, 4, 5)
GH = L.ghz((0, 1, 2))
perm_inv = all(L.reorder(L.relabel(L.ghz(X3), {X3[i]: X3[pp[i]] for i in range(3)}), X3) == L.ghz(X3)
               for pp in itertools.permutations(range(3)))
ov_ok = True
for _ in range(3):
    av = [L.rand_gauss(rng) for _ in range(2)]
    cv = [L.rand_gauss(rng) for _ in range(4)]
    v = [av[i] * cv[j] for i in range(2) for j in range(4)]
    ov_ok &= L.pair(L.ghz(X3), L.ket_op(v, X3)) == (av[0] * cv[0] + av[1] * cv[3]).abs2() / 2
y1 = L.reorder(teleport(GH, 4, 0, 3, (1, 2)), (1, 3, 2))
y2 = teleport(y1, 5, 1, 4, (3, 2))                          # on (4,3,2)
v_cert = L.pair(L.tensor(L.phi_plus(0, 2), L.w3(X3)), L.tensor(L.phi_plus(0, 5), L.reorder(y2, (2, 3, 4)).scale(16)))
rep.check("B2 (BS*, BS) excluded inside six tokens: GHZ PSD (in BS* = K012); W3 in BS* = K345* (SOS symbolic, GHZ "
          "permutation-invariant, overlap formula on 3 exact instances); after steps 1-2 the state is GHZ on (3,4,2); "
          "step-3 value tr[(Phi+_02 (x) W3_345)(Phi+_05 (x) GHZ_342)] = %s < 0" % v_cert,
          L.psd(GH)[0] and sos and perm_inv and ov_ok
          and L.reorder(y2, (2, 3, 4)).scale(16) == L.ghz((2, 3, 4)) and v_cert.im == 0 and v_cert.re < 0)
# c = 1 analogue: F, G (p1 T1 proves F, G in B_tw*)
P6 = L.identity(X3) - L.ket_op(L.basis_vec([0, 0, 0]), X3) - L.ket_op(L.basis_vec([1, 1, 1]), X3)
XC = L.Op(X3, {(0, 7): L.ONE, (7, 0): L.ONE})
F3 = P6.scale(Fr(1, 2)) + XC
G012 = ren(P6.scale(Fr(1, 2)) - XC, {3: 0, 4: 1, 5: 2}, (0, 1, 2))
g1 = L.reorder(teleport(G012, 4, 0, 3, (1, 2), 1, 1), (1, 3, 2))
g2 = teleport(g1, 5, 1, 4, (3, 2), 1, 1)
v_c1 = L.pair(L.tensor(L.swap_half(0, 2), F3), L.tensor(L.swap_half(0, 5), L.reorder(g2, (2, 3, 4)).scale(16)))
rep.check("B3 c = 1: (B_tw*, B_tw) excluded inside six tokens: twin teleportations carry G to (3,4,2) unchanged; "
          "step-3 value with the effect F on (3,4,5) = %s < 0" % v_c1,
          L.reorder(g2, (2, 3, 4)).scale(16) == ren(G012, {0: 2, 1: 3, 2: 4}, (2, 3, 4))
          and v_c1.im == 0 and v_c1.re < 0)
v_q = L.pair(L.tensor(L.phi_plus(0, 2), L.ghz(X3)), L.tensor(L.phi_plus(0, 5), L.reorder(y2, (2, 3, 4)).scale(16)))
bis = L.tensor(L.ket_op([1, 0], (0,)), L.phi_plus(1, 2))
b1 = L.reorder(teleport(bis, 4, 0, 3, (1, 2)), (1, 3, 2))
b2 = teleport(b1, 5, 1, 4, (3, 2))
v_b = L.pair(L.tensor(L.phi_plus(0, 2), L.w3(X3)), L.tensor(L.phi_plus(0, 5), L.reorder(b2, (2, 3, 4)).scale(16)))
rep.check("B4 controls: GHZ teleported against the PSD effect GHZ gives %s >= 0; the biseparable |0><0| (x) Phi+ "
          "teleported against W3 gives %s >= 0" % (v_q, v_b), v_q.re >= 0 and v_b.re >= 0)

# ------------------------------------------------------------------------------------------------ C five tokens: S_3
ok_c = True
for _, y in L.units((0, 1, 2)):
    a1_ = L.reorder(teleport(y, 4, 0, 3, (1, 2)), (1, 3, 2))           # 0 -> 3 : (3,1,2)
    a2_ = L.reorder(teleport(a1_, 4, 1, 0, (3, 2)), (3, 0, 2))         # 1 -> 0 : (0,3,2)
    a3_ = teleport(a2_, 4, 3, 1, (0, 2))                               # 3 -> 1 : (1,0,2)
    sw01 = ren(y, {0: 1, 1: 0}, (0, 1, 2)).scale(Fr(1, 64))
    ok_c &= L.reorder(a3_, (0, 1, 2)) == sw01
    b1_ = L.reorder(teleport(y, 4, 1, 3, (0, 2)), (2, 0, 3))           # 1 -> 3 : (3,0,2)
    b2_ = L.reorder(teleport(b1_, 4, 2, 1, (0, 3)), (3, 0, 1))         # 2 -> 1 : (1,0,3)
    b3_ = teleport(b2_, 4, 3, 2, (0, 1))                               # 3 -> 2 : (2,0,1)
    sw12 = ren(y, {1: 2, 2: 1}, (0, 1, 2)).scale(Fr(1, 64))
    ok_c &= L.reorder(b3_, (0, 1, 2)) == sw12
rep.check("C five tokens {0,..,4}, z = 4: composites of three teleportations are the token swaps (0 1) and (1 2) on "
          "every unit: K012 is S_3-invariant from KT on five tokens", ok_c)


# ------------------------------------------------------------------------------------------------ D general charts
def qmul(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    return (w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2, w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
            w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2, w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2)


def rot_of(qq):
    w = qq[0]
    return L.quat_rot(qq[1] / w, qq[2] / w, qq[3] / w)


def bell_state(Rm, a_, b_):
    return L.pauli2(L.homtab(Rm), (a_, b_))


def local_map_apply(H, qtok, Y):
    """(M (x) id)(Y) with M the one-token map whose coordinate action is the 4x4 table H, applied on token qtok."""
    others = tuple(x for x in Y.qs if x != qtok)
    Yr = L.reorder(Y, (qtok,) + others)
    out = L.Op((qtok,) + others, {})
    for i in range(2):
        for j in range(2):
            u = L.unit((qtok,), i, j)
            cu = L.coords1(u)
            img = L.pauli1([sum((L.G.of(H[r][c]) * cu[c] for c in range(4)), L.ZERO) for r in range(4)], qtok)
            # <i|_q Y |j>_q block
            blk = L.cond(L.unit((qtok,), j, i), Yr)
            out = out + L.tensor(img, blk)
    return out


QS = [(Fr(1), Fr(1, 2), Fr(-1, 3), Fr(2, 5)), (Fr(1), Fr(-2, 3), Fr(1, 4), Fr(1, 2)),
      (Fr(1), Fr(1, 3), Fr(1, 3), Fr(-1, 2)), (Fr(1), Fr(0), Fr(3, 2), Fr(-1, 5))]
ok_d1 = True
ok_d2 = True
ok_d3 = True
pairs_ = [(0, 1), (2, 3), (1, 2), (3, 0)]
cases = []
for (i1, i2) in pairs_:
    for d1, d2 in ((-1, -1), (1, 1), (-1, 1), (1, -1)):
        R1 = rot_of(QS[i1]) if d1 == 1 else L.mat_mul(rot_of(QS[i1]), L.REFLY)
        R2 = rot_of(QS[i2]) if d2 == 1 else L.mat_mul(rot_of(QS[i2]), L.REFLY)
        cases.append((i1, i2, d1, d2, R1, R2))
cases = cases[:8]
for (i1, i2, d1, d2, R1, R2) in cases:
    for Rm, dd in ((R1, d1), (R2, d2)):
        ok_d1 &= L.det3(Rm) == dd and (L.psd(bell_state(Rm, 0, 1))[0] == (dd == -1))
    Hm = L.homtab(L.mat_mul(L.mat_T(R1), R2))
    for _, y in L.units((p, s, t)):
        lhs = teleport(y, z, p, q, (s, t), state_link=bell_state(R1, z, q), eff_link=bell_state(R2, z, p))
        rhs = L.reorder(local_map_apply(Hm, q, ren(y, {p: q}, (q, s, t))), (q, s, t)).scale(Fr(1, 4))
        ok_d2 &= lhs == rhs
    # D3: explicit rational unitary for the proper part of the induced one-token map
    if d1 == -1 and d2 == -1:      # composition law: sigma(conj(q1) q2)
        qc = (QS[i1][0], -QS[i1][1], -QS[i1][2], -QS[i1][3])
        qq = qmul(qc, QS[i2])
        qq = (qq[0], -qq[1], qq[2], -qq[3])
        target = L.mat_mul(L.mat_T(R1), R2)
    else:
        target = L.mat_mul(L.mat_T(R1), R2)
        if d1 != d2:
            target = L.mat_mul(target, L.REFLY)
        # unnormalized quaternion of a proper rational rotation: (1 + tr, R32 - R23, R13 - R31, R21 - R12)
        tr_ = target[0][0] + target[1][1] + target[2][2]
        qq = (1 + tr_, target[2][1] - target[1][2], target[0][2] - target[2][0], target[1][0] - target[0][1])
    if True:
        w = qq[0]
        okq = w != 0 and L.quat_rot(qq[1] / w, qq[2] / w, qq[3] / w) == [[Fr(x) for x in r] for r in target]
        U = L.op(L.quat_unitary(qq[1] / w, qq[2] / w, qq[3] / w), (0,))
        nU = 1 + (qq[1] / w) ** 2 + (qq[2] / w) ** 2 + (qq[3] / w) ** 2
        Ht = L.homtab(target)
        for m in range(4):
            v = [1 if k == m else 0 for k in range(4)]
            out = [x / nU for x in L.coords1(L.ad(U, L.pauli1(v, 0)))]
            okq &= all(out[r] == L.G.of(Ht[r][m]) for r in range(4))
        ok_d3 &= okq
rep.check("D1 Bell states H_R: PSD for every det -1 instance, not PSD for every det +1 instance (exact elimination)",
          ok_d1)
rep.check("D2 general charts: conditional = (1/4)(M (x) id)(y(p -> q)) with M = homMap(R1^T R2), all 64 units, "
          "8 (R1, R2) pairs covering all four determinant patterns", ok_d2)
rep.check("D3 det R1 = det R2 = -1: homMap(R1^T R2) = Ad(U)/n for the explicit rational quaternion; mixed "
          "determinants: homMap(R1^T R2 reflY) = Ad(U)/n (transpose up to a local unitary)", ok_d3)
ok_d4 = True
for eps in itertools.product(range(2), repeat=5):
    for c in range(2):
        tau = lambda i, j: (eps[i] + eps[j] + c) % 2
        ok_d4 &= (tau(0, 2) + tau(0, 1)) % 2 == (eps[1] + eps[2]) % 2
rep.check("D4 with tau_ij = e_i + e_j + c, tau_zq + tau_zp = e_p + e_q (mod 2) for all e, c", ok_d4)

rep.verdict("P2-TELEPORT-EXACT")
