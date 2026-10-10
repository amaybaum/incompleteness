"""EQ3-P probe p1 -- what KT(4; 01|23, 02|13) gives at two copies: the four-copy link identities, exact.
Research only; base bcbc516f.  Usage (from scratchpad/eq3/P):
  python3 -I -B p1_four_copy_links.py <base>/.../OIBridge/CompositeDimension.lean <base>/.../OIBridge/K2Guard.lean

SETTING (NOTES N1.1).  Four tokens 0..3.  Every pair composite used -- (0,1), (2,3), (0,2), (1,3), lower token first --
has state cone K (a closed convex cone of tables in W 3) and effect cone K* (Euclidean dual: COMP-1 quantifies over
every effect of the factor body).  KT(4; 01|23, 02|13): one four-copy cone K4 is a COMP-1 composite of (01)|(23) and of
(02)|(13).  Products used: states X(01) Y(23) [prod_mem on 01|23] and L(02) L'(13) [prod_mem on 02|13]; effects
E(02) F(13) [prodEff_effect on 02|13] and e(01) f(23) [prodEff_effect on 01|23].

CLAIMS CHECKED (exact; symbolic identities unless stated):
  A1  sum E[m0,m2] F[m1,m3] X[m0,m1] Y[m2,m3] = <X, E.Y.F^T>            (value of family (i))
  A2  conditioning L(02) L'(13) on f(23) leaves the table L.f.L'^T on (0,1)   (family (ii): <e, L.f.L'^T> >= 0)
  A3  operator cross-check of A1 by explicit 4-qubit tensor placement and traces (3 random exact instances)
  B1  landed: cnot(prodState xplus z3) = phiW = Delta (CD:1222); cnot(idW) = chainW (K2G:110)
  B2  cnot is a self-adjoint involution for the Euclidean pairing (so K* is cnot-invariant when K is)
  B3  transposeW commutes with cnot;  B4  Delta.f.Delta = transposeW f;  B5 prodState tables are the product-effect
      tables (<prodState x y, w> = pairVal (hom x) (hom y) w);  B6 pauliW(Delta) = Phi+ and pauliW(transposeW w) =
      pauliW(w)^T (T is the operator transpose)
  C1  the Schmidt-diagonal link: for |a> = (1, u), L_a := cnot(coords(|a><a|) (x) hom z3) = coordsW(CNOT(|a><a| (x)
      |0><0|)CNOT), the state |00> + u|11>; the Bloch vector of |a> is pure (polynomial identity)
  C2  conditional through two such links: L_a.f.L_a'^T = 4 coordsW(Ad(D (x) D')(pauliW(transposeW f))), D = diag(1,u),
      D' = diag(1,u')  [symbolic f (16 symbols), u, u' complex]
  C3  countercontrols: dropping the transpose, or using L_a.f.L_a' (no transpose on the second link), gives a
      different table;  C4  the induced local map is a Lorentz boost (M_D mixes the unit index; not homMap of any N)
  D1  generic factorization D.Circ(w,1).D' = [[p, q], [r, w^2 q r / p]] with d1 = 1, d2' = q, d1' = p/w, d2 = r w/p
  D2  (D (x) D').CNOT.(|+> (x) |b>) has coefficient matrix D.Circ(b).D'
  D3  in tables: with g = cnot(coords(|+><+|) (x) coords(|b><b|)) and f = transposeW g: L_a.f.L_a'^T =
      4 coordsW(|chi><chi|), chi = (D (x) D') CNOT (|+>|b>)  [symbolic u, u', v]
  E1  twin: actT reflY w = w.Delta; cnot' := actT reflY . cnot . actT reflY; cnot'(prodState xplus z3) = idW
  E2  twin filter links cnot'(P_a) = L_a.Delta and L_a.Delta.f.(L_a'.Delta)^T = 4 coordsW(Ad(D (x) D')(pauliW f))
      (no transpose); pauliW(actT reflY w) = PT_2(pauliW w)
  F1  converse control: for PSD operators the family-(i) value is >= 0 (6 random exact instances); for K = Q3 the
      family-(ii) conditional through filter links of a PSD f is PSD (2 instances, exact minors)
DECISION RULE (fixed before the first run): verdict `P1-FOUR-COPY-LINKS-EXACT` iff every check passes, including the
transcription controls (T0), the landed-fact controls (B1) and the countercontrols (C3, C4).  Otherwise VERDICT NOT
RENDERED.  Exact arithmetic only (sympy Rationals, I, real symbols); no solver calls.
"""
import itertools
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp  # noqa: E402
from sympy import I, Matrix, Rational as R, eye, zeros  # noqa: E402

import eq3_lib as L  # noqa: E402

check = L.check
cd_path, k2_path = sys.argv[1], sys.argv[2]
rng = random.Random(20261008)

# ---------------------------------------------------------------- T0 transcription controls
tabs = L.parse_cnot(cd_path)
sgn, pc, pt = tabs
check("T0 parsed cnot tables (sgn, pc, pt) equal the hand transcription",
      {(i, j) for i in range(4) for j in range(4) if sgn[i][j] == -1} == L.HAND_SGN_NEG
      and pc == L.HAND_PC and pt == L.HAND_PT)
phiW = L.parse_phiW(cd_path)
idW, chainW, refl = L.parse_k2guard(k2_path)
check("T0 parsed phiW, idW, chainW, reflY equal the hand transcriptions",
      phiW == L.HAND_PHIW and idW == L.HAND_IDW and chainW == L.HAND_CHAINW and refl == [1, -1, 1])
cnot = L.cnot_from(tabs)
DEL = L.DELTA
check("T0 homMap reflY = diag(1,1,-1,1) = Delta = phiW (as tables)", L.hom_map(L.REFLY) == DEL and phiW == DEL)

# ---------------------------------------------------------------- A table contraction identities
def symtab(name):
    return Matrix(4, 4, lambda m, n: sp.Symbol(f"{name}{m}{n}", real=True))


X, Y, E, F, Lm, Lp, f = (symtab(s) for s in ("x", "y", "E", "F", "l", "k", "f"))
val_i = sp.expand(sum(E[a, c] * F[b, d] * X[a, b] * Y[c, d] for a, b, c, d in itertools.product(range(4), repeat=4)))
check("A1 family (i): sum E[m0,m2] F[m1,m3] X[m0,m1] Y[m2,m3] = <X, E.Y.F^T> (symbolic, 64 symbols)",
      sp.expand(val_i - L.eucl(X, E * Y * F.T)) == 0)
cond = Matrix(4, 4, lambda a, b: sp.expand(sum(Lm[a, c] * Lp[b, d] * f[c, d] for c in range(4) for d in range(4))))
check("A2 family (ii): conditioning L(02) L'(13) on the effect f(23) leaves L.f.L'^T on (0,1) (symbolic)",
      L.zero(cond - Lm * f * Lp.T))


def op_value_i(rX, rY, oE, oF):
    """tr((E_op on (0,2)) (F_op on (1,3)) (rho_X on (0,1)) (rho_Y on (2,3))) by explicit 4-qubit placement."""
    M = L.place([((0, 2), oE), ((1, 3), oF)], 4) * L.place([((0, 1), rX), ((2, 3), rY)], 4)
    return sp.expand(M.trace())


ok = True
for t in range(3):
    rX, rY, oE, oF = (L.rand_herm(rng, 4) for _ in range(4))
    Xt, Yt = L.coordsW(rX), L.coordsW(rY)
    Et, Ft = L.coordsW(oE) / 4, L.coordsW(oF) / 4          # effect tables: E_op = sum E_mn sigma_m (x) sigma_n
    ok = ok and sp.expand(op_value_i(rX, rY, oE, oF) - L.eucl(Xt, Et * Yt * Ft.T)) == 0
check("A3 operator cross-check: explicit 4-qubit trace = <X, E.Y.F^T> with state tables coordsW(rho) and effect tables "
      "coordsW(E_op)/4 (3 random exact Hermitian instances)", ok)

# ---------------------------------------------------------------- B Bell links and the gate
check("B1 landed control: cnot(prodState xplus z3) = phiW (CD:1222) and cnot(idW) = chainW (K2G:110)",
      cnot(L.prod_state(L.XPLUS, L.Z3)) == phiW and cnot(idW) == chainW)
W1, W2 = symtab("p"), symtab("q")
check("B2 cnot is an involution and self-adjoint for the Euclidean pairing (symbolic): K* is cnot-invariant",
      L.zero(cnot(cnot(W1)) - W1) and sp.expand(L.eucl(cnot(W1), W2) - L.eucl(W1, cnot(W2))) == 0)
check("B3 transposeW . cnot = cnot . transposeW (symbolic)", L.zero(L.transposeW(cnot(W1)) - cnot(L.transposeW(W1))))
check("B4 Delta.f.Delta = transposeW f (symbolic)", L.zero(DEL * f * DEL - L.transposeW(f)))
xs, ys = sp.symbols("x0:3", real=True), sp.symbols("y0:3", real=True)
check("B5 <prodState x y, w> = pairVal (hom x) (hom y) w (symbolic): product tables are the product-effect tables",
      sp.expand(L.eucl(L.prod_state(xs, ys), W1) - L.pair_val(L.hom(xs), L.hom(ys), W1)) == 0)
phiplus = Matrix([1, 0, 0, 1]) * Matrix([1, 0, 0, 1]).T / 2
check("B6 Pauli dictionary: pauliW(Delta) = Phi+ and pauliW(transposeW w) = pauliW(w)^T (symbolic w)",
      L.zero(L.pauliW(DEL) - phiplus) and L.zero(L.pauliW(L.transposeW(W1)) - L.pauliW(W1).T))

# ---------------------------------------------------------------- C filter links
ur, ui, vr, vi, wr, wi = sp.symbols("ur ui vr vi wr wi", real=True)
u, up = ur + I * ui, vr + I * vi


def ket_a(z):
    return Matrix([1, z])


def proj(v):
    return (v * v.H).applyfunc(sp.expand)


def P_a(z):
    """Unnormalized product table coords(|a><a|) (x) hom z3, |a> = (1, z)."""
    ca = L.coords1(proj(ket_a(z)))
    hz = L.hom(L.Z3)
    return Matrix(4, 4, lambda m, n: ca[m] * hz[n])


ket0 = Matrix([1, 0])
La = cnot(P_a(u))
rho_link = L.ad(L.CNOT_U, sp.kronecker_product(proj(ket_a(u)), proj(ket0)))
psi_link = Matrix([1, 0, 0, u])
ca = L.coords1(proj(ket_a(u)))
nrm = ca[0]
check("C1 L_a = cnot(coords(|a><a|) (x) hom z3) = coordsW(CNOT(|a><a| (x) |0><0|)CNOT), and that operator is "
      "|psi><psi| with psi = |00> + u|11> (symbolic u)",
      L.zero(La - L.coordsW(rho_link)) and L.zero(rho_link - proj(psi_link)))
check("C1 the Bloch vector of |a> = (1, u) is pure: (2 ur)^2 + (2 ui)^2 + (1 - |u|^2)^2 = (1 + |u|^2)^2, and "
      "coords(|a><a|) = (1 + |u|^2) hom(x(u)) with x(u) = (2ur, 2ui, 1 - |u|^2)/(1 + |u|^2)",
      sp.expand(ca[1] ** 2 + ca[2] ** 2 + ca[3] ** 2 - nrm ** 2) == 0
      and all(sp.expand(c - t) == 0 for c, t in zip(ca, [1 + ur ** 2 + ui ** 2, 2 * ur, 2 * ui, 1 - ur ** 2 - ui ** 2])))
Lap = cnot(P_a(up))
D, Dp = sp.diag(1, u), sp.diag(1, up)
DD = L.kron(D, Dp)
lhs_C2 = (La * f * Lap.T).applyfunc(sp.expand)
rhs_C2 = (4 * L.coordsW(L.ad(DD, L.pauliW(L.transposeW(f))))).applyfunc(sp.expand)
check("C2 L_a.f.L_a'^T = 4 coordsW(Ad(D (x) D')(pauliW(transposeW f))), D = diag(1,u), D' = diag(1,u') "
      "(symbolic f, u, u')", L.zero(lhs_C2 - rhs_C2))
rhs_noT = (4 * L.coordsW(L.ad(DD, L.pauliW(f)))).applyfunc(sp.expand)
check("C3 countercontrol: without the transpose the formula fails (symbolic difference nonzero)",
      not L.zero(lhs_C2 - rhs_noT))
check("C3 countercontrol: L_a.f.L_a' (second link not transposed) differs from L_a.f.L_a'^T (symbolic)",
      not L.zero((La * f * Lap).applyfunc(sp.expand) - lhs_C2))
# induced single-copy map of the link: table of Ad(D) on Pauli coordinates, M_D[m,k] = (1/2) tr(sigma_m D sigma_k D^H)
MD = Matrix(4, 4, lambda m, k: sp.expand((L.PAULI[m] * D * L.PAULI[k] * D.H).trace() / 2))
check("C4 the link acts on copy 0 as M_D (L_a = 2 M_D Delta, symbolic) and M_D is a Lorentz boost: at u = 2, "
      "M_D[0,3] = -3/2 != 0 (it mixes the unit index, so it is not homMap of any N; a filter, not a rotation)",
      L.zero(La - 2 * MD * DEL) and MD.subs({ur: 2, ui: 0})[0, 3] == R(-3, 2))

# ---------------------------------------------------------------- D generic factorization and pure states
p, q, r_, w = sp.symbols("p q r w", nonzero=True)
d1, d2p, d1p, d2 = 1, q, p / w, r_ * w / p
Dm, Circ, Dpm = sp.diag(d1, d2), Matrix([[w, 1], [1, w]]), sp.diag(d1p, d2p)
check("D1 D.Circ(w,1).D' = [[p, q], [r, w^2 q r / p]] with d1 = 1, d2' = q, d1' = p/w, d2 = r w / p (symbolic): every "
      "coefficient matrix with p, q, r, s nonzero is of this form (w^2 = p s / (q r) has a complex root)",
      all(sp.expand(sp.numer(sp.together(t))) == 0
          for t in (Dm * Circ * Dpm - Matrix([[p, q], [r_, w ** 2 * q * r_ / p]]))))
e1, e2, f1, f2, b0, b1 = sp.symbols("e1 e2 f1 f2 b0 b1")
Dg, Dgp = sp.diag(e1, e2), sp.diag(f1, f2)
chi = L.kron(Dg, Dgp) * L.CNOT_U * L.kron(Matrix([1, 1]), Matrix([b0, b1]))
coef = Matrix([[chi[0], chi[1]], [chi[2], chi[3]]])
check("D2 (D (x) D').CNOT.(|+> (x) |b>) has coefficient matrix D.Circ(b).D', Circ(b) = [[b0, b1], [b1, b0]] (symbolic)",
      L.zero(coef - Dg * Matrix([[b0, b1], [b1, b0]]) * Dgp))
vb = wr + I * wi
ketb = Matrix([1, vb])
cplus = L.coords1(proj(Matrix([1, 1])))
cb = L.coords1(proj(ketb))
g_tab = cnot(Matrix(4, 4, lambda m, n: cplus[m] * cb[n]))
check("D3 control: g = cnot(coords|+><+| (x) coords|b><b|) is the table of CNOT(|+><+| (x) |b><b|)CNOT (symbolic b)",
      L.zero(g_tab - L.coordsW(L.ad(L.CNOT_U, sp.kronecker_product(proj(Matrix([1, 1])), proj(ketb))))))
chi_u = (DD * L.CNOT_U * L.kron(Matrix([1, 1]), ketb)).applyfunc(sp.expand)
lhs_D3 = (La * L.transposeW(g_tab) * Lap.T).applyfunc(sp.expand)
check("D3 L_a.(transposeW g).L_a'^T = 4 coordsW(|chi><chi|), chi = (D (x) D') CNOT (|+>|b>) (symbolic u, u', b): the "
      "filtered link conditional of an effect in transposeW(cnot SEP) is a pure state with coefficient D.Circ(b).D'",
      L.zero(lhs_D3 - 4 * L.coordsW(proj(chi_u))))

# ---------------------------------------------------------------- E twin analogue
check("E1 actT reflY w = w.Delta (symbolic)", L.zero(L.actT(L.REFLY, W1) - W1 * DEL))


def cnotp(wt):
    return L.actT(L.REFLY, cnot(L.actT(L.REFLY, wt)))


check("E1 cnot' = actT reflY . cnot . actT reflY sends prodState xplus z3 to idW (twin Bell table)",
      cnotp(L.prod_state(L.XPLUS, L.Z3)) == idW)
check("E2 twin filter links: cnot'(P_a) = L_a.Delta (symbolic u)", L.zero(cnotp(P_a(u)) - La * DEL))
lhs_E2 = (La * DEL * f * (Lap * DEL).T).applyfunc(sp.expand)
rhs_E2 = (4 * L.coordsW(L.ad(DD, L.pauliW(f)))).applyfunc(sp.expand)
check("E2 L_a.Delta.f.(L_a'.Delta)^T = 4 coordsW(Ad(D (x) D')(pauliW f)) -- no transpose (symbolic f, u, u')",
      L.zero(lhs_E2 - rhs_E2))
check("E2 pauliW(actT reflY w) = PT_2(pauliW w) (partial transpose on the second copy; symbolic w)",
      L.zero(L.pauliW(L.actT(L.REFLY, W1)) - L.pt_copy(L.pauliW(W1), 1, 2)))
check("E2 twin Bell link and effect: idW.f.idW^T = f and <X, idW.Y.idW^T> = <X, Y> (so the twin instance gives K* <= K "
      "and K <= K*)", L.zero(idW * f * idW.T - f) and sp.expand(L.eucl(X, idW * Y * idW.T) - L.eucl(X, Y)) == 0)

# ---------------------------------------------------------------- F converse controls (QM satisfies the instance)
okF = True
for t in range(6):
    rX, rY, oE, oF = (L.rand_psd(rng, 4) for _ in range(4))
    v = op_value_i(rX, rY, oE, oF)
    okF = okF and v.is_Rational is True and v >= 0
check("F1 converse control: family-(i) value >= 0 for PSD states and PSD effects (6 random exact instances)", okF)


def is_psd_minors(M):
    n = M.shape[0]
    if not L.zero(M - M.H):
        return False
    for k in range(1, n + 1):
        for idx in itertools.combinations(range(n), k):
            d = sp.expand(M.extract(list(idx), list(idx)).det())
            if not (d.is_Rational and d >= 0):
                return False
    return True


okF2 = True
for (uu, vv) in ((R(2), R(1, 3) + I), (R(-1, 2) + 2 * I, R(3))):
    fop = L.rand_psd(rng, 4, rank=2)
    ft = L.coordsW(fop) / 4                          # effect table of a PSD effect
    c_tab = (cnot(P_a(uu)) * ft * cnot(P_a(vv)).T).applyfunc(sp.expand)
    okF2 = okF2 and is_psd_minors(L.pauliW(c_tab))
check("F1 converse control: for K = Q3 the filter-link conditional of a PSD effect is PSD (2 exact instances, all "
      "principal minors)", okF2)

ok = L.summary("p1_four_copy_links")
print("VERDICT " + ("P1-FOUR-COPY-LINKS-EXACT" if ok else "NOT RENDERED"))
sys.exit(0 if ok else 1)
