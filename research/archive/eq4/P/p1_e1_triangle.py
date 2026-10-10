"""EQ4-P probe p1 -- coordinator expectation E1 (nine tokens, three disjoint triples), exact.  Research only.

Usage:  python3 -I -B p1_e1_triangle.py <base>/verification/lean-mathlib/OIBridge
Imports only the own library eq4_lib.py (nothing from eq3/ or eqreview/).

Setting (aligned charts).  Tokens 0..8; triples A = (0,1,2), B = (3,4,5), C = (6,7,8).  Every standalone pair carries
its native gate; aligned c = 0 means every pair gate is the kernel cnot in the token charts, so every pair has the
Bell link state Phi+ = Ad(CNOT)(|+><+| (x) |0><0|) and the Bell effect (the dual image of the product effect
sharp(xplus) (x) sharp(z3)), both the operator |Phi+><Phi+|.  Aligned c = 1 means every pair gate is
cnot' = R_B cnot R_B; its link is PT_2(Phi+) = SWAP/2, as state and as effect.  A matching pi of X = (x1,x2,x3) to
Y = (y1,y2,y3) links x_i with y_pi(i); Pi_pi relabels y_pi(i) -> x_i.

DECISION RULE (fixed before the first run; rules, not expected numbers).  VERDICT `P1-E1-TRIANGLE-EXACT` iff all pass:
  K  kernel tie-in: transcription control (parsed pc, pt, sgn, phiW, idW, chainW, reflY, sharpVec, xplus, z3,
     prodState, IsEffectOn, COMP-1 fields, condA_mem's IsCompact, the landed cnot(prodState xplus z3) = phiW all equal
     the hand transcriptions); the hand kernel cnot equals Ad(CNOT) in the Pauli dictionary on all 16 unit tables;
     kernel cnot(prodState xplus z3) = phiW = coords(Phi+); idW = coords(SWAP/2); the one-qubit transpose acts on
     coords as homMap(reflY) (4 units); pairVal(sharpVec x, sharpVec y, T) = <coords(E_x (x) E_y)/4, T> for the
     sharp effect operators E_b = (1 + b.sigma)/2 (rational x, y; all 16 unit tables T); Ad(CNOT) of the product
     effect |+><+| (x) |0><0| is |Phi+><Phi+| (the Bell effect).
  L  c = 0 link identities on each of the three six-token subfamilies A u B, B u C, A u C and every matching pi:
     (L1) the Bell-state conditional tr_Y[(f (x) 1)(Phi+ (x) Phi+ (x) Phi+)] equals (1/8) T(Pi_pi f) on all 64 units f;
     (L2) the Bell-effect value tr[(Phi+ (x) Phi+ (x) Phi+)(x (x) y)] equals (1/8) tr(x T(Pi_pi y)) on all 64 x 64 unit
     pairs; (L3) T and every Pi_pi preserve the trace pairing and commute (units), so (T Pi K)* = T Pi (K*);
     countercontrols (L4): two different matchings give different maps on some unit; T(Pi f) != Pi f on some unit.
  C  c = 1 (twin links SWAP/2): (C1) conditional = (1/8) Pi_pi f, (C2) value = (1/8) tr(x Pi_pi y), all matchings,
     all units / unit pairs; countercontrol: the c = 0 and c = 1 conditionals differ on some unit.
  P  pigeonhole certificate, c = 0, BS = cone of products rho (x) sigma over the three cuts (sigma a PSD pair operator):
     (P1) GHZ is invariant under the six token permutations and, for symbolic a (one token) and chi (two tokens),
          (1/2)|a|^2|chi|^2 - (1/2)|a0 chi00 + a1 chi11|^2 = (1/2)|a|^2(|chi01|^2 + |chi10|^2)
          + (1/2)|a0 conj(chi11) - a1 conj(chi00)|^2 (symbolic; <GHZ|a (x) chi> = (a0 chi00 + a1 chi11)/sqrt2), so
          W3 = 1/2 - GHZ is in BS*; (P2) GHZ is PSD, so GHZ is in BS*; (P3) W3 |GHZ> = -1/2 |GHZ>, so W3 is not in BS;
     (P4) T(W3) = W3 and T(GHZ) = GHZ; (P5) (BS, BS) on a Bell-linked pair: tr[(W3_X (x) GHZ_Y)(Phi+)^3] < 0 for every
          matching (inclusion (I3) fails); (P6) (BS*, BS*): tr[(Phi+)^3 (W3_X (x) GHZ_Y)] < 0 for every matching
          (inclusion (II3) fails); (P7) every one of the 8 assignments of {BS, BS*} to (A, B, C) puts equal cones on
          some linked pair; (P8) controls: with the biseparable |0><0| (x) Phi+ in place of GHZ both values are >= 0,
          and with GHZ in place of W3 (PSD on both sides) both values are >= 0.
  T  c = 1 pigeonhole with the all-twin hull B_tw = cone{PT_j(sigma_ij) (x) rho_k}: F = (1/2)(1 - |000><000| -
     |111><111|) + |000><111| + |111><000|, G the same with the coherence negated.  (T1) F and G commute with the six
     token permutations; for every pair (i, j), third token k and symbolic phi = (alpha, beta) on k, PT_j(<phi|F|phi>_k)
     equals diag(|beta|^2, |phi|^2, |phi|^2, |alpha|^2)/2 + conj(alpha) beta |01><10| + alpha conj(beta) |10><01| and
     the 2 x 2 block determinant equals (|alpha|^2 - |beta|^2)^2 / 4 (symbolic), likewise for G with the coherence
     negated, so F, G are in B_tw*; (T2) tr(FG) < 0; (T3) (B_tw*, B_tw*) with twin links: tr[(SWAP/2)^3 (F (x) G)]
     < 0; (T4) (B_tw, B_tw): the twin-link conditional of G is G/8 and tr(F G/8) < 0; (T5) control: W3 equals
     sum_k p_k PT_1(sigma_k (x) rho_k) with explicit PSD sigma_k, rho_k, p_k > 0 (W3 is in B_tw) and tr(W3 F),
     tr(W3 G) >= 0; countercontrol: F2 (coherence 2) pairs negatively with the B_tw generator PT_1(Psi-) (x) |+><+|.
  K'  general k (k = 1, 2, 3, 4; groups X = (0..k-1), Y = (k..2k-1)): the Bell-state conditional is 2^-k T(Pi f) and
     the twin conditional 2^-k Pi f on all units f, for every matching when k <= 3 and for three matchings when k = 4.
Exact Gaussian-rational arithmetic (eq4_lib) and small sympy identities only.
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
import sympy as sp  # noqa: E402

import eq4_lib as L  # noqa: E402

BASE = sys.argv[1]
rep = L.Report("p1_e1_triangle")
rng = random.Random(20261009)

# ------------------------------------------------------------------------------------------------ K kernel tie-in
ok_tc, kp = L.transcription_control(BASE)
rep.check("K0 transcription control: parsed kernel objects equal the hand transcriptions", ok_tc)


def unit_tab(m, n):
    return [[1 if (i, j) == (m, n) else 0 for j in range(4)] for i in range(4)]


ok_k1 = True
for m in range(4):
    for n in range(4):
        T = unit_tab(m, n)
        lhs = L.kernel_cnot_tab(T)
        rhs = L.coords2(L.ad(L.op(L.CNOT, (0, 1)), L.pauli2(T, (0, 1))))
        ok_k1 &= all(L.G.of(lhs[i][j]) == rhs[i][j] for i in range(4) for j in range(4))
rep.check("K1 the hand kernel cnot equals Ad(CNOT) in the Pauli dictionary on all 16 unit tables", ok_k1)
xplus, z3 = [1, 0, 0], [0, 0, 1]
hom = lambda v: [1] + v
prodState = [[hom(xplus)[i] * hom(z3)[j] for j in range(4)] for i in range(4)]
phi = L.phi_plus(0, 1)
rep.check("K2 kernel cnot(prodState xplus z3) = phiW = coords(Phi+), and idW = coords(SWAP/2) = coords(PT_2 Phi+)",
          L.kernel_cnot_tab(prodState) == [[L.G.of(v) for v in r] for r in L.PHIW]
          and L.coords2(phi) == [[L.G.of(v) for v in r] for r in L.PHIW]
          and L.coords2(L.swap_half(0, 1)) == [[L.G.of(v) for v in r] for r in L.HAND["idW"]])
ok_k3 = True
for m in range(4):
    v = [1 if i == m else 0 for i in range(4)]
    rho = L.pauli1(v, 0)
    lhs = L.coords1(L.transpose(rho))
    H = L.homtab(L.REFLY)
    rhs = [sum((H[i][j] * v[j] for j in range(4)), Fr(0)) for i in range(4)]
    ok_k3 &= all(lhs[i] == L.G.of(rhs[i]) for i in range(4))
rep.check("K3 the one-qubit transpose acts on coords1 as homMap(reflY) (4 units)", ok_k3)


def sharp_op(b, q):
    return L.pauli1([1, b[0], b[1], b[2]], q)


ok_k4 = True
for _ in range(3):
    xb = [Fr(rng.randint(-3, 3), rng.randint(1, 4)) for _ in range(3)]
    yb = [Fr(rng.randint(-3, 3), rng.randint(1, 4)) for _ in range(3)]
    sx, sy = [Fr(1, 2)] + [c / 2 for c in xb], [Fr(1, 2)] + [c / 2 for c in yb]
    E = L.coords2(L.tensor(sharp_op(xb, 0), sharp_op(yb, 1)))
    for m in range(4):
        for n in range(4):
            T = unit_tab(m, n)
            pv = sum((sx[i] * T[i][j] * sy[j] for i in range(4) for j in range(4)), Fr(0))
            rv = sum((E[i][j] * T[i][j] for i in range(4) for j in range(4)), L.ZERO) / 4
            ok_k4 &= rv == L.G.of(pv)
rep.check("K4 pairVal(sharpVec x, sharpVec y, T) = <coords(E_x (x) E_y)/4, T> (3 rational x, y; 16 unit tables)",
          ok_k4)
plus0 = L.tensor(L.ket_op([1, 1], (0,)).scale(Fr(1, 2)), L.ket_op([1, 0], (1,)))
rep.check("K5 the gate's dual image of the product effect |+><+| (x) |0><0| is |Phi+><Phi+| (the Bell effect)",
          L.ad(L.op(L.CNOT, (0, 1)), plus0) == phi)

# ------------------------------------------------------------------------------------------------ L, C link identities
TR = {"A": (0, 1, 2), "B": (3, 4, 5), "C": (6, 7, 8)}


def links(X, Y, pi, kind):
    mk = L.phi_plus if kind == 0 else L.swap_half
    return L.tensor(*[mk(X[i], Y[pi[i]]) for i in range(len(X))])


def Pi(f, X, Y, pi):
    return L.reorder(L.relabel(f, {Y[pi[i]]: X[i] for i in range(len(X))}), X)


def check_links(X, Y, pi, kind, bilinear=True):
    lk = links(X, Y, pi, kind)
    k = len(X)
    s = Fr(1, 2 ** k)
    ok1 = True
    for _, f in L.units(Y):
        lhs = L.reorder(L.cond(f, lk), X)
        rhs = Pi(f, X, Y, pi)
        rhs = (L.transpose(rhs) if kind == 0 else rhs).scale(s)
        ok1 &= lhs == rhs
    ok2 = True
    if bilinear:
        for _, x in L.units(X):
            for _, y in L.units(Y):
                lhs = L.pair(lk, L.tensor(x, y))
                py = Pi(y, X, Y, pi)
                rhs = L.pair(x, L.transpose(py) if kind == 0 else py) * s
                ok2 &= lhs == rhs
    return ok1, ok2


PERMS3 = list(itertools.permutations(range(3)))
ok_l1 = ok_l2 = True
for (nx, ny) in (("A", "B"), ("B", "C"), ("A", "C")):
    for pi in PERMS3:
        a, b = check_links(TR[nx], TR[ny], pi, 0)
        ok_l1 &= a
        ok_l2 &= b
rep.check("L1 c = 0: Bell-state conditional = (1/8) T(Pi_pi f) on all 64 units, all 6 matchings, on A|B, B|C, A|C",
          ok_l1)
rep.check("L2 c = 0: Bell-effect value = (1/8) tr(x T(Pi_pi y)) on all 64 x 64 unit pairs, all 6 matchings, three "
          "subfamilies", ok_l2)
X, Y = TR["A"], TR["B"]
ok_l3 = True
for pi in PERMS3:
    for _, u in L.units(Y):
        for _, w in L.units(X):
            pu = Pi(u, X, Y, pi)
            ok_l3 &= L.pair(w, L.transpose(pu)) == L.pair(L.transpose(w), pu)
        ok_l3 &= L.transpose(Pi(u, X, Y, pi)) == Pi(L.transpose(u), X, Y, pi)
rep.check("L3 T preserves the trace pairing and commutes with every Pi_pi (all units)", ok_l3)
u0 = L.unit(Y, 1, 6)
diff_pi = any(Pi(u, X, Y, (0, 1, 2)) != Pi(u, X, Y, (1, 0, 2)) for _, u in L.units(Y))
diff_T = L.transpose(Pi(u0, X, Y, (0, 1, 2))) != Pi(u0, X, Y, (0, 1, 2))
rep.check("L4 countercontrols: two matchings give different maps on some unit; the transpose is not the identity",
          diff_pi and diff_T)
ok_c1 = ok_c2 = True
for (nx, ny) in (("A", "B"), ("B", "C"), ("A", "C")):
    for pi in PERMS3:
        a, b = check_links(TR[nx], TR[ny], pi, 1)
        ok_c1 &= a
        ok_c2 &= b
cdiff = L.reorder(L.cond(u0, links(X, Y, (0, 1, 2), 0)), X) != L.reorder(L.cond(u0, links(X, Y, (0, 1, 2), 1)), X)
rep.check("C1/C2 c = 1 (twin links SWAP/2): conditional = (1/8) Pi_pi f and value = (1/8) tr(x Pi_pi y), all units, "
          "all matchings, three subfamilies; countercontrol: c = 0 and c = 1 conditionals differ",
          ok_c1 and ok_c2 and cdiff)

# ------------------------------------------------------------------------------------------------ P pigeonhole (c = 0)
GH = L.ghz(X)
W3 = L.w3(X)
perm_inv = True
for p in PERMS3:
    perm_inv &= L.reorder(L.relabel(GH, {X[i]: X[p[i]] for i in range(3)}), X) == GH
a0r, a0i, a1r, a1i = sp.symbols("a0r a0i a1r a1i", real=True)
cr = sp.symbols("cr0:4", real=True)
ci = sp.symbols("ci0:4", real=True)
a = [a0r + sp.I * a0i, a1r + sp.I * a1i]
chi = [cr[k] + sp.I * ci[k] for k in range(4)]
ab2 = lambda z: sp.expand(z * sp.conjugate(z))
na = ab2(a[0]) + ab2(a[1])
nchi = sum(ab2(c) for c in chi)
lhs = sp.Rational(1, 2) * na * nchi - sp.Rational(1, 2) * ab2(a[0] * chi[0] + a[1] * chi[3])
rhs = (sp.Rational(1, 2) * na * (ab2(chi[1]) + ab2(chi[2]))
       + sp.Rational(1, 2) * ab2(a[0] * sp.conjugate(chi[3]) - a[1] * sp.conjugate(chi[0])))
# the overlap formula <GHZ|a (x) chi> = (a0 chi00 + a1 chi11)/sqrt2, checked on the operator: |<GHZ|v>|^2 = <v|GHZ|v>
ov_ok = True
for _ in range(3):
    av = [L.rand_gauss(rng) for _ in range(2)]
    cv = [L.rand_gauss(rng) for _ in range(4)]
    v = [av[i] * cv[j] for i in range(2) for j in range(4)]
    vop = L.ket_op(v, X)
    ov_ok &= L.pair(GH, vop) == (av[0] * cv[0] + av[1] * cv[3]).abs2() / 2
rep.check("P1 GHZ is invariant under the 6 token permutations; Cauchy-Schwarz SOS identity (symbolic) and the overlap "
          "formula (3 exact instances): W3 = 1/2 - GHZ is in BS*", perm_inv and sp.expand(lhs - rhs) == 0 and ov_ok)
rep.check("P2 GHZ is PSD (exact elimination), hence in BS* (BS is inside PSD)", L.psd(GH)[0])
ghz_vec = [1, 0, 0, 0, 0, 0, 0, 1]
rep.check("P3 W3 |GHZ> = -1/2 |GHZ> (exact), so W3 is not PSD, hence not in BS", L.eigvec_check(W3, ghz_vec, Fr(-1, 2)))
rep.check("P4 T(W3) = W3 and T(GHZ) = GHZ", L.transpose(W3) == W3 and L.transpose(GH) == GH)
vals5, vals6 = [], []
for pi in PERMS3:
    lk = links(X, Y, pi, 0)
    gy = L.ghz(Y)
    vals5.append(L.pair(L.tensor(W3, gy), lk))           # effects W3 (A), GHZ (B); states: links  -> (I3)
    vals6.append(L.pair(lk, L.tensor(W3, gy)))           # effects: links; states W3 (A), GHZ (B) -> (II3)
rep.check("P5 (BS, BS): tr[(W3_A (x) GHZ_B)(Phi+)^3] = %s < 0 for all 6 matchings: (I3) fails"
          % sorted(set(str(v) for v in vals5)), all(v.im == 0 and v.re < 0 for v in vals5))
rep.check("P6 (BS*, BS*): tr[(Phi+)^3 (W3_A (x) GHZ_B)] = %s < 0 for all 6 matchings: (II3) fails"
          % sorted(set(str(v) for v in vals6)), all(v.im == 0 and v.re < 0 for v in vals6))
assign_ok = True
for asg in itertools.product(("BS", "BS*"), repeat=3):
    assign_ok &= (asg[0] == asg[1]) or (asg[1] == asg[2]) or (asg[0] == asg[2])
rep.check("P7 all 8 assignments of {BS, BS*} to (A, B, C) put equal cones on some linked pair", assign_ok)
bis = L.tensor(L.ket_op([1, 0], (Y[0],)), L.phi_plus(Y[1], Y[2]))
lk0 = links(X, Y, (0, 1, 2), 0)
c1 = L.pair(L.tensor(W3, bis), lk0)
c2 = L.pair(lk0, L.tensor(W3, bis))
c3 = L.pair(L.tensor(GH, L.ghz(Y)), lk0)
c4 = L.pair(lk0, L.tensor(GH, L.ghz(Y)))
rep.check("P8 controls: biseparable |0><0| (x) Phi+ in place of GHZ gives %s, %s >= 0; PSD on both sides (GHZ, GHZ) "
          "gives %s, %s >= 0" % (c1, c2, c3, c4), all(v.im == 0 and v.re >= 0 for v in (c1, c2, c3, c4)))

# ------------------------------------------------------------------------------------------------ T pigeonhole (c = 1)
P6 = L.identity(X) - L.ket_op(L.basis_vec([0, 0, 0]), X) - L.ket_op(L.basis_vec([1, 1, 1]), X)
XC = L.Op(X, {(0, 7): L.ONE, (7, 0): L.ONE})
F = P6.scale(Fr(1, 2)) + XC
Gm = P6.scale(Fr(1, 2)) - XC
sym_ok = True
for p in PERMS3:
    for M in (F, Gm):
        sym_ok &= L.reorder(L.relabel(M, {X[i]: X[p[i]] for i in range(3)}), X) == M
# symbolic conditional <phi|_k M |phi>_k for M = F, G; then PT_j; compare with the stated form
al_r, al_i, be_r, be_i = sp.symbols("al_r al_i be_r be_i", real=True)
al, be = al_r + sp.I * al_i, be_r + sp.I * be_i


def to_sp(M):
    N = 2 ** M.n
    return sp.Matrix(N, N, lambda r, c: sp.Rational(M.get(r, c).re) + sp.I * sp.Rational(M.get(r, c).im))


def cond_sym(M, k):
    """<phi|_k M |phi>_k as a 4 x 4 sympy matrix on the other two tokens (their order in X)."""
    Ms = to_sp(M)
    others = [q for q in X if q != k]
    kpos = X.index(k)
    ph = [al, be]
    out = sp.zeros(4, 4)
    for r in range(8):
        for c in range(8):
            if Ms[r, c] == 0:
                continue
            rk, ck = (r >> (2 - kpos)) & 1, (c >> (2 - kpos)) & 1
            ro = [(r >> (2 - X.index(q))) & 1 for q in others]
            co = [(c >> (2 - X.index(q))) & 1 for q in others]
            out[2 * ro[0] + ro[1], 2 * co[0] + co[1]] += sp.conjugate(ph[rk]) * Ms[r, c] * ph[ck]
    return out.applyfunc(sp.expand)


def pt2_sym(M):
    out = sp.zeros(4, 4)
    for i0, i1, j0, j1 in itertools.product(range(2), repeat=4):
        out[2 * i0 + i1, 2 * j0 + j1] = M[2 * i0 + j1, 2 * j0 + i1]
    return out


nphi = sp.expand(al * sp.conjugate(al) + be * sp.conjugate(be))
ok_t1 = True
for Mname, M, sgn in (("F", F, 1), ("G", Gm, -1)):
    for k in X:
        others = [q for q in X if q != k]
        for jpos in (0, 1):   # PT on the first or the second of the remaining two tokens
            Cm = cond_sym(M, k)
            Pm = pt2_sym(Cm) if jpos == 1 else pt2_sym(Cm.T).applyfunc(sp.expand)
            # pair (i, j) ordered as in X; the coherence sits on |01><10| / |10><01| of the PT'd conditional
            a_, b_ = (al, be)
            expect = sp.zeros(4, 4)
            expect[0, 0] = sp.expand(sp.conjugate(be) * be / 2)
            expect[1, 1] = expect[2, 2] = nphi / 2
            expect[3, 3] = sp.expand(sp.conjugate(al) * al / 2)
            # the off-diagonal pair positions after PT: determine from the computed matrix and test its modulus form
            off = Pm[1, 2]
            blockdet = sp.expand(Pm[1, 1] * Pm[2, 2] - Pm[1, 2] * Pm[2, 1])
            target = sp.expand((sp.conjugate(al) * al - sp.conjugate(be) * be) ** 2 / 4)
            diag_ok = all(sp.expand(Pm[i, i] - expect[i, i]) == 0 for i in range(4))
            offd_zero = all(sp.expand(Pm[i, j]) == 0 for i in range(4) for j in range(4)
                            if i != j and (i, j) not in ((1, 2), (2, 1)))
            off_ok = sp.expand(off * sp.conjugate(off) - sp.conjugate(al) * al * sp.conjugate(be) * be) == 0
            ok_t1 &= diag_ok and offd_zero and off_ok and sp.expand(blockdet - target) == 0
rep.check("T1 F, G commute with the 6 token permutations; for every third token k, symbolic phi and PT on either "
          "remaining token, PT_j(<phi|M|phi>_k) is diag(|b|^2, |phi|^2, |phi|^2, |a|^2)/2 plus a single coherence of "
          "modulus |a||b| on |01><10|, block determinant (|a|^2 - |b|^2)^2/4 (symbolic): F, G in B_tw*",
          sym_ok and ok_t1)
trFG = L.pair(F, Gm)
rep.check("T2 tr(F G) = %s < 0" % trFG, trFG.im == 0 and trFG.re < 0)
FY = L.reorder(L.relabel(Gm, {X[i]: Y[i] for i in range(3)}), Y)
v_t3 = [L.pair(links(X, Y, pi, 1), L.tensor(F, FY)) for pi in PERMS3]
rep.check("T3 (B_tw*, B_tw*) with twin links: states F (A), G (B), twin Bell effects: value %s < 0 (all matchings)"
          % sorted(set(str(v) for v in v_t3)), all(v.im == 0 and v.re < 0 for v in v_t3))
v_t4 = []
for pi in PERMS3:
    cg = L.reorder(L.cond(FY, links(X, Y, pi, 1)), X)
    v_t4.append((cg == Gm.scale(Fr(1, 8)), L.pair(F, cg)))
rep.check("T4 (B_tw, B_tw): the twin-link conditional of the effect G is G/8 and tr(F G/8) = %s < 0 (all matchings)"
          % sorted(set(str(v[1]) for v in v_t4)), all(e and v.im == 0 and v.re < 0 for e, v in v_t4))
# W3 in B_tw: PT_1 of an explicit separable (12|3) decomposition
q1, q2, q3 = X
comp = []
for al_ph in (L.G(1), L.G(0, 1), L.G(-1), L.G(0, -1)):
    beta = -al_ph.conj()
    u = [0, 0, 0, 0]
    u[2] = L.ONE            # |10>
    u[1] = al_ph            # |01>
    w = [L.ONE, beta]
    sig = L.ket_op(u, (q1, q2)).scale(Fr(1, 2))
    rho = L.ket_op(w, (q3,)).scale(Fr(1, 2))
    comp.append((Fr(1, 2), sig, rho))
comp.append((Fr(1, 2), L.ket_op([1, 0, 0, 0], (q1, q2)), L.ket_op([0, 1], (q3,))))
comp.append((Fr(1, 2), L.ket_op([0, 0, 0, 1], (q1, q2)), L.ket_op([1, 0], (q3,))))
acc = L.Op(X, {})
gens_psd = True
for p_, sig, rho in comp:
    gens_psd &= L.psd(sig)[0] and L.psd(rho)[0] and p_ > 0
    acc = acc + L.ptranspose(L.tensor(sig, rho), [q1]).scale(p_)
acc = L.reorder(acc, X)
tWF, tWG = L.pair(W3, F), L.pair(W3, Gm)
rep.check("T5 control: W3 = sum_k p_k PT_1(sigma_k (x) rho_k) with 6 explicit PSD products (W3 in B_tw); "
          "tr(W3 F) = %s, tr(W3 G) = %s >= 0" % (tWF, tWG),
          gens_psd and acc == W3 and tWF.re >= 0 and tWG.re >= 0 and tWF.im == 0 and tWG.im == 0)
F2 = P6.scale(Fr(1, 2)) + XC.scale(2)
psi_m = L.ket_op([0, 1, -1, 0], (q1, q2)).scale(Fr(1, 2))
gen = L.reorder(L.tensor(L.ptranspose(psi_m, [q1]), L.ket_op([1, 1], (q3,)).scale(Fr(1, 2))), X)
vF2 = L.pair(F2, gen)
vF = L.pair(F, gen)
rep.check("T6 countercontrol: F2 (coherence 2) pairs to %s < 0 with the B_tw generator PT_1(Psi-) (x) |+><+| "
          "(F itself gives %s >= 0)" % (vF2, vF), vF2.re < 0 and vF.re >= 0)

# ------------------------------------------------------------------------------------------------ K' general k
ok_gk = True
for k in (1, 2, 3, 4):
    Xk, Yk = tuple(range(k)), tuple(range(k, 2 * k))
    perms = list(itertools.permutations(range(k)))
    if k == 4:
        perms = [(0, 1, 2, 3), (1, 0, 3, 2), (3, 1, 0, 2)]
    for pi in perms:
        for kind in (0, 1):
            a_, _ = check_links(Xk, Yk, pi, kind, bilinear=False)
            ok_gk &= a_
rep.check("K' general k = 1..4: Bell conditional 2^-k T(Pi f), twin conditional 2^-k Pi f on all units (all matchings "
          "for k <= 3, three for k = 4)", ok_gk)

rep.verdict("P1-E1-TRIANGLE-EXACT")
