"""EQ5-PREM q1 — Part A.  Exact evaluation of the A1 predicates (independent preparation, regrouping invariance,
TokProdState, TokenCoherent) on the KT(4)-minus-tok data of every EQ4-SOURCE countermodel (re-derived here from
SOURCE's definitions, in this thread's own code), on the new antipodal model M_th, on the token-coherent control M_sig,
and on the separation models PAD1, PAD2, PAD3, SEPB.  Research only; nothing here is adopted.

Usage:  python3 -I -B q1_tok_models.py <base>/verification/lean-mathlib/OIBridge <mathlib4 root> <eq5>/inputs

Conventions (base, package f0d37906, Mathlib v4.33.0):
 - pair tables T (4 x 4, index 0 = unit, 1,2,3 = x,y,z; first index = first token of the pair); flat chart index of
   (m, n) is n + 4 m (finProdFinEquiv); pairBody K = flat normalized tables of K.
 - COMP-1 coordinate model at dA = dB = 16: carrier C = 17 x 17 arrays; hom x = (1, x); pState x y = hom x (x) hom y;
   an affine functional e on Fin 16 -> R is (c, l), coeff e = (c, l); pEff e f w = sum coeff_e[m] coeff_f[n] w[m][n];
   tabCoord a b = (0, unit vector at 4a + b).
 - four-token tables Z[a][b][c][d] (tokens 0,1,2,3); iota: W4 -> C copies the (00) block into the hom row/column;
   pi reads the 16 x 16 block; R Z[a][b][c][d] = Z[a][c][b][d]; sigma = iota R pi + (id - iota pi).
 - pair-level twists on the second token of a pair: rho = actT reflY, signs s = (1, 1, -1, 1); theta = actT (-id),
   signs t = (1, -1, -1, -1); tau = token exchange of a pair (tabT).
 - KT(4) data: PA : PreComposite (pairBody K01) (pairBody K23) V; PB : PreComposite (pairBody K02) (pairBody K13) V.
   The A-table of a point w is TA(w)[a,b,c,d] = PA.prodEff (tabCoord a b) (tabCoord c d) w; the B-table (token order) is
   TB(w)[a,b,c,d] = PB.prodEff (tabCoord a c) (tabCoord b d) w.  tok (TokenCoherent) at w: TA(w) = TB(w).
   For token Bloch vectors x0..x3: pA(x) = PA.prodState (flat(x0 (x) x1)) (flat(x2 (x) x3)); pB(x) = PB.prodState
   (flat(x0 (x) x2)) (flat(x1 (x) x3)); H(x)[a,b,c,d] = hom x0 [a] hom x1 [b] hom x2 [c] hom x3 [d].

The predicates (A1; each is a predicate on the KT(4) data):
 TPS   TokProdState: pA(x) = pB(x) for all x (symbolic Bloch vectors).
 IP1BA first-order independent preparation, A reading B: the single-token entries of TA(pB(x)) equal those of H(x)
       (index patterns with exactly one nonzero index), all x.     IP1AB: the same for TB(pA(x)).
 IPBA  full independent preparation, A reading B: TA(pB(x)) = H(x), all x.   IPAB: TB(pA(x)) = H(x).
 STMC  single-token marginal coherence on the body: TA(w) and TB(w) agree on the patterns with at most one nonzero index,
       for all w in the body.
 tok   TokenCoherent on PA's body.
 ONE   the one-body field (by construction in every model; recorded).
 RIL   relabelling covariance: an affine automorphism Phi of V with Phi(Omega) = Omega, Phi o PA.prodState =
       PB.prodState and PB.prodEff e f o Phi = PA.prodEff e f (requires pairBody K01 = pairBody K02 and
       pairBody K23 = pairBody K13; N/A otherwise).
 OLTI  operation-level token identity for local rotations: for each token t and rotation R, the affine map Gamma of V
       that A-covariance forces (R on token t of every A product) also implements R on token t of every B product.
 LTA, LTB  local tomography of PA, PB on the body (exact part: TA, resp. TB, is injective on the linear span of the body;
       the passage from effect agreement to table agreement is the landed exists_effect_rescale, CI:148, written).
 A predicate HOLDS when every listed difference vanishes identically on its domain (symbolic); it FAILS when an explicit
 point of the domain (in the body) gives a nonzero exact difference; N/A is printed with its reason.

DECISION RULE (fixed before the first run; rules, not expected numbers):
 K  transcription: CI:582 hom = Fin.cons 1 x; CI:602-603 coeff = Fin.cons (e 0) (linear coefficients); CI:633 pState;
    CI:637 pEffLin; K2G:47 reflY signs (1, -1, 1); package :240-241 flatW, :247 tabCoord via finProdFinEquiv,
    :253-257 TokenCoherent with (tabCoord a b)(tabCoord c d) for PA and (tabCoord a c)(tabCoord b d) for PB;
    Mathlib Logic/Equiv/Fin/Basic.lean finProdFinEquiv toFun x.2 + n * x.1.  All must hold.
 V  validity layer (exact; all must hold): for every model, PA and PB satisfy prodEff_apply on symbolic chart points and
    symbolic affine functionals; sigma o sigma = id on the 289 basis vectors and sigma o iota = iota o R (symbolic);
    rho, theta, tau and Psi_mf are involutions; the cross value PB.prodEff E F (PA.prodState X Y) equals fourVal X Y Et
    (twist Ft) for M_sig (no twist), M_tw (rho), M_th (theta) and equals fourVal X Y (tabT Et) Ft for M_T (symbolic);
    the anchor sum's cross values are e(x0) f(y0) and E(L0) F(L0'); the 2 x 2 Pauli facts used for M_th and OLTI:
    sigma_y sigma_mu^T sigma_y = t_mu sigma_mu with t = (1, -1, -1, -1), and Ad(diag(1, i)), Ad(sigma_x) act on (X, Y, Z)
    as Rz90 and Rx180 (exact).
 C  controls (all must hold): in M_sig every predicate HOLDS (TPS, IP1BA, IP1AB, IPBA, IPAB, STMC, tok, RIL, OLTI, LTA,
    LTB); in each SOURCE countermodel (the anchor sum, evaluated on two explicit members: ANCc with every anchor at the
    pair-body centre and ANCz with every anchor at the +z product; its symbolic-anchor form ANC enters only the identity
    checks V1 and V3) and in M_rho, M_tw, M_id, M_T and M_th, tok FAILS and TPS FAILS.
 S  separations (each model must realize its stated pattern): PAD1: IP1BA, IPBA, TPS HOLD, tok FAILS, LTA FAILS;
    PAD2: tok HOLDS, TPS FAILS, LTA FAILS; PAD3: STMC HOLDS, IP1BA HOLDS, tok FAILS, LTA FAILS; SEPB: IP1BA HOLDS, LTA
    HOLDS, tok FAILS, and some PA product effect of token effects is negative at some PB product (so no common body
    exists); M_tw and M_th: IP1BA holds at tokens 0, 1, 2 and fails at token 3.
 REFUTATION (printed only if K, V, C, S all pass): a candidate implication "P => G" (G in {tok, TPS}) is REFUTED by a
    model M of KT(4)-minus-tok (the anchor sum through either member, M_rho, M_tw, M_id, M_T, M_th) iff P HOLDS and G
    FAILS in M.  A candidate SURVIVES iff it is refuted by none.
 VERDICT Q1-PART-A-MODELS-EXACT iff every K, V, C and S check passes; otherwise VERDICT NOT RENDERED.  Exact arithmetic
 only (sympy integers, rationals, symbols, and the exact imaginary unit for the 2 x 2 Pauli facts); a float anywhere
 aborts.  No timing in stdout.
"""
import itertools
import os
import re
import sys

import sympy as sp

LEAN = sys.argv[1]
MLROOT = sys.argv[2]
INPUTS = sys.argv[3]
CHECKS = []


def check(name, cond, detail=None):
    ok = bool(cond)
    CHECKS.append((name, ok))
    line = ("PASS " if ok else "FAIL ") + name
    if detail is not None:
        line += "  [" + str(detail) + "]"
    print(line)
    sys.stdout.flush()
    return ok


def note(text):
    print("NOTE " + text)
    sys.stdout.flush()


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def zero(e):
    return sp.expand(e) == 0


def no_float(*objs):
    for o in objs:
        if isinstance(o, float):
            return False
        if isinstance(o, (list, tuple)):
            if not no_float(*o):
                return False
        elif isinstance(o, dict):
            if not no_float(*o.values()):
                return False
        elif isinstance(o, sp.Basic) and o.atoms(sp.Float):
            return False
    return True


R4 = range(4)
N16 = range(16)
N17 = range(17)
I4 = list(itertools.product(R4, R4, R4, R4))
Z0, O1 = sp.Integer(0), sp.Integer(1)

# ===================================================================== K: transcription controls
CI = read(os.path.join(LEAN, "CompositeInterface.lean")).split("\n")
K2G = read(os.path.join(LEAN, "K2Guard.lean"))
PKG = read(os.path.join(INPUTS, "FourCopyPackage.lean")).split("\n")
MLF = read(os.path.join(MLROOT, "Mathlib/Logic/Equiv/Fin/Basic.lean"))
k_ci = (CI[581].strip() == "def hom (x : Fin d → ℝ) : Fin (d + 1) → ℝ := Fin.cons 1 x"
        and CI[601].strip() == "def coeff (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) : Fin (d + 1) → ℝ :="
        and CI[602].strip() == "Fin.cons (e 0) fun i => e.linear (fun j => if i = j then 1 else 0)"
        and CI[632].strip() == "def pState (x : Fin dA → ℝ) (y : Fin dB → ℝ) : Carrier dA dB := fun μ ν => hom x μ * hom y ν"
        and CI[636].strip() == "toFun ω := ∑ μ, ∑ ν, coeff e μ * coeff f ν * ω μ ν")
refl_txt = re.search(r"def reflY[^\n]*\n\s*toFun x := fun i => \(!\[([^\]]*)\]", K2G).group(1).replace(" ", "")
k_pkg = (PKG[239].strip() == "def flatW (ω : W 3) : Fin 16 → ℝ := fun i =>"
         and PKG[240].strip() == "ω ((@finProdFinEquiv 4 4).symm i).1 ((@finProdFinEquiv 4 4).symm i).2"
         and PKG[246].strip() == "def tabCoord (μ ν : Fin 4) : (Fin 16 → ℝ) →ᵃ[ℝ] ℝ := coord (@finProdFinEquiv 4 4 (μ, ν))"
         and PKG[255].strip() == "∀ a b c d : Fin 4, ∀ ω ∈ PA.Ω,"
         and PKG[256].strip() == "PA.prodEff (tabCoord a b) (tabCoord c d) ω = PB.prodEff (tabCoord a c) (tabCoord b d) ω")
k_ml = re.search(r"def finProdFinEquiv : Fin m × Fin n ≃ Fin \(m \* n\) where\n\s*toFun x :=\n\s*⟨x\.2 \+ n \* x\.1,", MLF)
check("K transcription: COMP-1 hom, coeff, pState, pEffLin (CI:582, 602-603, 633, 637); reflY signs (K2G:47); package "
      "flatW, tabCoord, TokenCoherent (:240-241, :247, :256-257); Mathlib finProdFinEquiv = x.2 + n * x.1",
      k_ci and refl_txt == "1,-1,1" and k_pkg and k_ml is not None, "reflY = (%s)" % refl_txt)

S_RHO = [1, 1, -1, 1]      # homogenized signs of reflY
S_TH = [1, -1, -1, -1]     # homogenized signs of -id

# ===================================================================== carrier machinery
def hom16(x):
    return [O1] + list(x)


def pState(x, y):
    hx, hy = hom16(x), hom16(y)
    return [[hx[m] * hy[n] for n in N17] for m in N17]


def coeff(e):
    return [e[0]] + list(e[1])


def pEff(e, f, w):
    ce, cf = coeff(e), coeff(f)
    return sp.expand(sum(ce[m] * cf[n] * w[m][n] for m in N17 if ce[m] != 0 for n in N17 if cf[n] != 0))


def evalA(e, x):
    return e[0] + sum(e[1][i] * x[i] for i in N16)


def tc(a, b):
    return (Z0, [O1 if i == 4 * a + b else Z0 for i in N16])


def flat(T):
    return [T[m][n] for m in R4 for n in R4]


def h3(x):
    return [O1] + list(x)


def ps3(x, y):
    hx, hy = h3(x), h3(y)
    return [[hx[m] * hy[n] for n in R4] for m in R4]


def cadd(u, v):
    return [[u[m][n] + v[m][n] for n in N17] for m in N17]


def csub(u, v):
    return [[u[m][n] - v[m][n] for n in N17] for m in N17]


def cscale(c, u):
    return [[c * u[m][n] for n in N17] for m in N17]


def ceq(u, v):
    return all(zero(u[m][n] - v[m][n]) for m in N17 for n in N17)


def iota(Z):
    V = [[Z0] * 17 for _ in N17]
    for a, b, c, d in I4:
        V[1 + 4 * a + b][1 + 4 * c + d] = Z[(a, b, c, d)]
    for c, d in itertools.product(R4, R4):
        V[0][1 + 4 * c + d] = Z[(0, 0, c, d)]
    for a, b in itertools.product(R4, R4):
        V[1 + 4 * a + b][0] = Z[(a, b, 0, 0)]
    V[0][0] = Z[(0, 0, 0, 0)]
    return V


def piV(V):
    return {(a, b, c, d): V[1 + 4 * a + b][1 + 4 * c + d] for a, b, c, d in I4}


def Rg(Z):
    return {(a, b, c, d): Z[(a, c, b, d)] for a, b, c, d in I4}


def lift(F):
    """the carrier map iota F pi + (id - iota pi) of a linear map F of W4"""
    def g(V):
        Z = piV(V)
        return cadd(csub(V, iota(Z)), iota(F(Z)))
    return g


sigma = lift(Rg)


def psi_mf(Z):
    return {I: (S_RHO[I[3]] * Z[I] if I[:3] != (0, 0, 0) else Z[I]) for I in I4}


Psi_c = lift(psi_mf)


def twistT(signs, x):           # actT of a diagonal sign map on a flat pair vector (second token)
    return [x[i] * signs[i % 4] for i in N16]


def comp_twistT(e, signs):      # e o twistT
    return (e[0], [e[1][i] * signs[i % 4] for i in N16])


TAU = [4 * (k % 4) + k // 4 for k in N16]


def tau_f(x):
    return [x[TAU[i]] for i in N16]


def comp_tau(e):
    return (e[0], [e[1][TAU[i]] for i in N16])


def prodA(X, Y):
    return {(a, b, c, d): X[a][b] * Y[c][d] for a, b, c, d in I4}


def fourVal(X, Y, E, F):
    return sp.expand(sum(X[a][b] * Y[c][d] * E[a][c] * F[b][d] for a, b, c, d in I4))


def table_of(e):                # an affine functional on the normalized slice, read as a table
    t = [[e[1][4 * m + n] for n in R4] for m in R4]
    t[0][0] = t[0][0] + e[0]
    return t


def tabT(A):
    return [[A[n][m] for n in R4] for m in R4]


def actTsigns(signs, T):
    return [[signs[n] * T[m][n] for n in R4] for m in R4]


def sym_aff(name):
    return (sp.Symbol(name + "c"), [sp.Symbol("%s%d" % (name, i)) for i in N16])


def sym_vec(name):
    return [sp.Symbol("%s%d" % (name, i)) for i in N16]


def sym_ntab(name):
    return [[O1 if (m, n) == (0, 0) else sp.Symbol("%s%d%d" % (name, m, n)) for n in R4] for m in R4]


E00 = flat(ps3([0, 0, 0], [0, 0, 0]))          # the centre of every pair body (flat table of prodState 0 0)

# ===================================================================== the models
# Each model: kind ("C": carrier C; "CC": C x C; "CR": C x R), A/B state maps on flat pair vectors, A/B effect maps
# (affine functionals e, f; point w), and the A/B tables of a point.
MODELS = {}


def model(name, kind, Ast, Bst, Aef, Bef, TA, TB):
    MODELS[name] = dict(kind=kind, Ast=Ast, Bst=Bst, Aef=Aef, Bef=Bef, TA=TA, TB=TB)


def TA_C(w):
    return {(a, b, c, d): w[1 + 4 * a + b][1 + 4 * c + d] for a, b, c, d in I4}


def TB_from(w, signs_d=None, swap02=False):
    out = {}
    for a, b, c, d in I4:
        m = 1 + (4 * c + a if swap02 else 4 * a + c)
        v = w[m][1 + 4 * b + d]
        out[(a, b, c, d)] = v * (signs_d[d] if signs_d else 1)
    return out


# M_sig: token-coherent control
model("M_sig", "C",
      lambda X, Y: pState(X, Y), lambda L, Lp: sigma(pState(L, Lp)),
      lambda e, f, w: pEff(e, f, w), lambda E, F, w: pEff(E, F, sigma(w)),
      TA_C, lambda w: TB_from(sigma(w)))
# M_rho: no regrouping; PB.prodState L L' = pState L (rho L'); PB.prodEff E F = pEff E (F o rho)
model("M_rho", "C",
      lambda X, Y: pState(X, Y), lambda L, Lp: pState(L, twistT(S_RHO, Lp)),
      lambda e, f, w: pEff(e, f, w), lambda E, F, w: pEff(E, comp_twistT(F, S_RHO), w),
      TA_C, lambda w: TB_from(w, S_RHO))
# M_tw: genuine regrouping with token 3's chart reflected
model("M_tw", "C",
      lambda X, Y: pState(X, Y), lambda L, Lp: sigma(pState(L, twistT(S_RHO, Lp))),
      lambda e, f, w: pEff(e, f, w), lambda E, F, w: pEff(E, comp_twistT(F, S_RHO), sigma(w)),
      TA_C, lambda w: TB_from(sigma(w), S_RHO))
# M_th (new): genuine regrouping with token 3's chart inverted (antipodal map, central in O(3))
model("M_th", "C",
      lambda X, Y: pState(X, Y), lambda L, Lp: sigma(pState(L, twistT(S_TH, Lp))),
      lambda e, f, w: pEff(e, f, w), lambda E, F, w: pEff(E, comp_twistT(F, S_TH), sigma(w)),
      TA_C, lambda w: TB_from(sigma(w), S_TH))
# M_id: PB = PA (uniform Q3)
model("M_id", "C",
      lambda X, Y: pState(X, Y), lambda L, Lp: pState(L, Lp),
      lambda e, f, w: pEff(e, f, w), lambda E, F, w: pEff(E, F, w),
      TA_C, lambda w: TB_from(w))
# M_T: pair 02 read token-exchanged through sigma (EQ4-F f1 W4 completed)
model("M_T", "C",
      lambda X, Y: pState(X, Y), lambda L, Lp: sigma(pState(tau_f(L), Lp)),
      lambda e, f, w: pEff(e, f, w), lambda E, F, w: pEff(comp_tau(E), F, sigma(w)),
      TA_C, lambda w: TB_from(sigma(w), None, swap02=True))
# SEPB: separate bodies, PB twisted by the STMC-respecting Psi_mf (one_body dropped)
model("SEPB", "C",
      lambda X, Y: pState(X, Y), lambda L, Lp: Psi_c(sigma(pState(L, Lp))),
      lambda e, f, w: pEff(e, f, w), lambda E, F, w: pEff(E, F, sigma(Psi_c(w))),
      TA_C, lambda w: TB_from(sigma(Psi_c(w))))

# anchor sum (C x C); generic anchors (symbolic) and the centred member (anchors at the body centres)
def make_anchor(name, x0, y0, L0, L0p):
    a0, b0 = pState(L0, L0p), pState(x0, y0)
    model(name, "CC",
          lambda X, Y: (pState(X, Y), a0), lambda L, Lp: (b0, pState(L, Lp)),
          lambda e, f, w: pEff(e, f, w[0]), lambda E, F, w: pEff(E, F, w[1]),
          lambda w: TA_C(w[0]), lambda w: TB_from(w[1]))
    MODELS[name]["anchors"] = (x0, y0, L0, L0p)


make_anchor("ANC", sym_vec("p"), sym_vec("q"), sym_vec("r"), sym_vec("t"))
make_anchor("ANCc", E00, E00, E00, E00)
ZZ = flat(ps3([0, 0, 1], [0, 0, 1]))
make_anchor("ANCz", ZZ, ZZ, ZZ, ZZ)


# padding models (C x R)
def padded(name, w0, w1, b_height):
    delta = csub(w1, w0) if w1 is not None else None

    def Beff(E, F, w):
        v = w[0] if delta is None else cadd(w[0], cscale(w[1], delta))
        return pEff(E, F, sigma(v))

    def TB(w):
        v = w[0] if delta is None else cadd(w[0], cscale(w[1], delta))
        return TB_from(sigma(v))

    model(name, "CR",
          lambda X, Y: (pState(X, Y), Z0), lambda L, Lp: (sigma(pState(L, Lp)), sp.Integer(b_height)),
          lambda e, f, w: pEff(e, f, w[0]), Beff, lambda w: TA_C(w[0]), TB)
    MODELS[name]["w0"] = w0


ZP0 = prodA(ps3([0, 0, 1], [0, 0, 1]), ps3([0, 0, 1], [0, 0, 1]))       # all four tokens +z
ZP1 = prodA(ps3([1, 0, 0], [1, 0, 0]), ps3([1, 0, 0], [1, 0, 0]))       # all four tokens +x
PHIW = [[sp.Integer([1, 1, -1, 1][i]) if i == j else Z0 for j in R4] for i in R4]
ZM0 = prodA(ps3([0, 0, 0], [0, 0, 0]), ps3([0, 0, 0], [0, 0, 0]))       # all four tokens maximally mixed
ZM1 = prodA(PHIW, ps3([0, 0, 0], [0, 0, 0]))                            # Phi+ on tokens 0,1; mixed on 2,3
padded("PAD1", iota(ZP0), iota(ZP1), 0)
padded("PAD2", None, None, 1)
padded("PAD3", iota(ZM0), iota(ZM1), 0)

# ===================================================================== V: validity layer
xv, yv = sym_vec("x"), sym_vec("y")
ea, fa = sym_aff("e"), sym_aff("f")
ok_eval = {}
for nm, M in MODELS.items():
    a_ok = zero(M["Aef"](ea, fa, M["Ast"](xv, yv)) - evalA(ea, xv) * evalA(fa, yv))
    b_ok = zero(M["Bef"](ea, fa, M["Bst"](xv, yv)) - evalA(ea, xv) * evalA(fa, yv))
    ok_eval[nm] = a_ok and b_ok
check("V1 prodEff_apply for PA and PB in every model (symbolic chart points, symbolic affine functionals)",
      all(ok_eval.values()), ", ".join("%s:%s" % (k, "ok" if v else "FAIL") for k, v in ok_eval.items()))

inv_ok = True
for k in range(289):
    Vk = [[O1 if 17 * m + n == k else Z0 for n in N17] for m in N17]
    if not ceq(sigma(sigma(Vk)), Vk) or not ceq(Psi_c(Psi_c(Vk)), Vk):
        inv_ok = False
        break
Zs = {I: sp.Symbol("Z%d%d%d%d" % I) for I in I4}
sig_iota = ceq(sigma(iota(Zs)), iota(Rg(Zs)))
tw_inv = (twistT(S_RHO, twistT(S_RHO, xv)) == xv and twistT(S_TH, twistT(S_TH, xv)) == xv and tau_f(tau_f(xv)) == xv)
check("V2 sigma and Psi_c are involutions on all 289 basis vectors; sigma o iota = iota o R (symbolic); rho, theta, "
      "tau are involutions", inv_ok and sig_iota and tw_inv)

Xn, Yn = sym_ntab("X"), sym_ntab("Y")
Ea, Fa = sym_aff("E"), sym_aff("F")
cv = {}
cv["M_sig"] = zero(MODELS["M_sig"]["Bef"](Ea, Fa, pState(flat(Xn), flat(Yn)))
                   - fourVal(Xn, Yn, table_of(Ea), table_of(Fa)))
cv["M_tw"] = zero(MODELS["M_tw"]["Bef"](Ea, Fa, pState(flat(Xn), flat(Yn)))
                  - fourVal(Xn, Yn, table_of(Ea), actTsigns(S_RHO, table_of(Fa))))
cv["M_th"] = zero(MODELS["M_th"]["Bef"](Ea, Fa, pState(flat(Xn), flat(Yn)))
                  - fourVal(Xn, Yn, table_of(Ea), actTsigns(S_TH, table_of(Fa))))
cv["M_T"] = zero(MODELS["M_T"]["Bef"](Ea, Fa, pState(flat(Xn), flat(Yn)))
                 - fourVal(Xn, Yn, tabT(table_of(Ea)), table_of(Fa)))
# the A-side cross values: PA.prodEff e f (PB.prodState L L') = fourVal et ft L (twist L')
Ln, Lpn = sym_ntab("L"), sym_ntab("M")
cv["M_th(A)"] = zero(pEff(ea, fa, MODELS["M_th"]["Bst"](flat(Ln), flat(Lpn)))
                     - fourVal(table_of(ea), table_of(fa), Ln, actTsigns(S_TH, Lpn)))
an = MODELS["ANC"]
x0, y0, L0, L0p = an["anchors"]
cv["ANC"] = (zero(an["Aef"](ea, fa, an["Bst"](xv, yv)) - evalA(ea, x0) * evalA(fa, y0))
             and zero(an["Bef"](ea, fa, an["Ast"](xv, yv)) - evalA(ea, L0) * evalA(fa, L0p)))
check("V3 cross values: M_sig fourVal X Y Et Ft; M_tw fourVal X Y Et (rho Ft); M_th fourVal X Y Et (theta Ft) and "
      "fourVal et ft L (theta L'); M_T fourVal X Y (tabT Et) Ft; anchor sum e(x0) f(y0), E(L0) F(L0') (symbolic)",
      all(cv.values()), ", ".join("%s:%s" % (k, "ok" if v else "FAIL") for k, v in cv.items()))

# 2 x 2 Pauli facts (exact; sympy's I is the exact imaginary unit)
I_ = sp.I
SIG = [sp.Matrix([[1, 0], [0, 1]]), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I_], [I_, 0]]),
       sp.Matrix([[1, 0], [0, -1]])]
p_th = all(sp.simplify(SIG[2] * SIG[mu].T * SIG[2] - S_TH[mu] * SIG[mu]) == sp.zeros(2, 2) for mu in R4)
Uz = sp.Matrix([[1, 0], [0, I_]])
Ux = SIG[1]
RZ90 = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
RX180 = [[1, 0, 0], [0, -1, 0], [0, 0, -1]]


def ad_is(U, R):
    for k in range(3):
        lhs = sp.simplify(U * SIG[k + 1] * U.H)
        rhs = sum((R[j][k] * SIG[j + 1] for j in range(3)), sp.zeros(2, 2))
        if sp.simplify(lhs - rhs) != sp.zeros(2, 2):
            return False
    return True


check("V4 Pauli facts: sigma_y sigma_mu^T sigma_y = t_mu sigma_mu, t = (1,-1,-1,-1) (theta = Ad(sigma_y) o transpose, "
      "so actT(-id) maps twin = PT_2(Q3) onto Q3); Ad(diag(1,i)) = Rz90 and Ad(sigma_x) = Rx180 on (X, Y, Z)",
      p_th and ad_is(Uz, RZ90) and ad_is(Ux, RX180))

# ===================================================================== predicates
hb = [[sp.Symbol("h%d%d" % (t, i)) for i in range(3)] for t in R4]
HX = {(a, b, c, d): h3(hb[0])[a] * h3(hb[1])[b] * h3(hb[2])[c] * h3(hb[3])[d] for a, b, c, d in I4}
SINGLE = {0: [(i, 0, 0, 0) for i in (1, 2, 3)], 1: [(0, i, 0, 0) for i in (1, 2, 3)],
          2: [(0, 0, i, 0) for i in (1, 2, 3)], 3: [(0, 0, 0, i) for i in (1, 2, 3)]}
LE1 = [I for I in I4 if sum(1 for k in I if k != 0) <= 1]


def pA_of(M, xs):
    return M["Ast"](flat(ps3(xs[0], xs[1])), flat(ps3(xs[2], xs[3])))


def pB_of(M, xs):
    return M["Bst"](flat(ps3(xs[0], xs[2])), flat(ps3(xs[1], xs[3])))


def point_eq(M, u, v):
    if M["kind"] == "C":
        return ceq(u, v)
    if M["kind"] == "CC":
        return ceq(u[0], v[0]) and ceq(u[1], v[1])
    return ceq(u[0], v[0]) and zero(u[1] - v[1])


def tab_diff(t1, t2, idx):
    return [I for I in idx if not zero(t1[I] - t2[I])]


RESULTS = {}


def record(nm, pred, val, why=None):
    RESULTS.setdefault(nm, {})[pred] = (val, why)


# the explicit pure product points used for failures (rational unit vectors)
PURE = [[[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 1, 0]],
        [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, -1]],
        [[0, 0, 1], [1, 0, 0], [0, 1, 0], [1, 0, 0]]]
SUBS = [{hb[t][i]: sp.Integer(P[t][i]) for t in R4 for i in range(3)} for P in PURE]


def eval_products(M):
    pA = pA_of(M, hb)
    pB = pB_of(M, hb)
    TApB, TBpA = M["TA"](pB), M["TB"](pA)
    tps = point_eq(M, pA, pB)
    ip1ba_tok = {t: not tab_diff(TApB, HX, SINGLE[t]) for t in R4}
    ip1ab_tok = {t: not tab_diff(TBpA, HX, SINGLE[t]) for t in R4}
    ipba = not tab_diff(TApB, HX, I4)
    ipab = not tab_diff(TBpA, HX, I4)
    return tps, ip1ba_tok, ip1ab_tok, ipba, ipab


for nm in ["M_sig", "ANCc", "ANCz", "M_rho", "M_tw", "M_id", "M_T", "M_th", "SEPB", "PAD1", "PAD2", "PAD3"]:
    M = MODELS[nm]
    tps, i1ba, i1ab, ipba, ipab = eval_products(M)
    record(nm, "TPS", tps)
    record(nm, "IP1BA", all(i1ba.values()), "tokens failing: %s" % [t for t in R4 if not i1ba[t]])
    record(nm, "IP1AB", all(i1ab.values()), "tokens failing: %s" % [t for t in R4 if not i1ab[t]])
    record(nm, "IPBA", ipba)
    record(nm, "IPAB", ipab)
    M["ip1ba_tok"] = i1ba

# --------------------------------------------------------------------- tok, STMC and LT on the bodies
iotaZ = iota(Zs)


def on_points(M, pts, idx):
    """list of (point label, failing patterns) over the given body points"""
    out = []
    for lab, w in pts:
        bad = tab_diff(M["TA"](w), M["TB"](w), idx)
        out.append((lab, bad))
    return out


def body_eval(M, gens_sym, idx):
    """HOLDS iff the difference vanishes identically on every symbolic generator (the generators span, or generate,
    the body); otherwise FAILS at the first explicit pure four-token A-product (a body point of every model) with a
    nonzero exact difference; N/A (None) if no listed witness is found."""
    if all(not tab_diff(M["TA"](g), M["TB"](g), idx) for g in gens_sym):
        return True, "holds on every generator"
    for k, P in enumerate(PURE):
        w = pA_of(M, P)
        bad = tab_diff(M["TA"](w), M["TB"](w), idx)
        if bad:
            I = bad[0]
            return False, "pure A-product %d, index %s, difference %s" % (k, I, sp.expand(M["TA"](w)[I] - M["TB"](w)[I]))
    return None, "symbolically nonzero; no listed witness"


A_GEN = lambda M: M["Ast"](flat(Xn), flat(Yn))          # noqa: E731  (A-product of symbolic normalized pair tables)
B_GEN = lambda M: M["Bst"](flat(Ln), flat(Lpn))         # noqa: E731
for nm in ["M_sig", "M_tw", "M_th", "M_T"]:                # body iota(B4): iota(W4) spans it
    for pred, idx in (("tok", I4), ("STMC", LE1)):
        v, why = body_eval(MODELS[nm], [iotaZ], idx)
        record(nm, pred, v, why)
for nm in ["M_rho", "M_id"]:                               # body: the hull of A-products
    for pred, idx in (("tok", I4), ("STMC", LE1)):
        v, why = body_eval(MODELS[nm], [A_GEN(MODELS[nm])], idx)
        record(nm, pred, v, why)
for nm in ["ANCc", "ANCz"]:                                # body: the hull of A-products and B-products
    for pred, idx in (("tok", I4), ("STMC", LE1)):
        v, why = body_eval(MODELS[nm], [A_GEN(MODELS[nm]), B_GEN(MODELS[nm])], idx)
        record(nm, pred, v, why)
for pred, idx in (("tok", I4), ("STMC", LE1)):             # SEPB: PA's own body, the hull of A-products
    v, why = body_eval(MODELS["SEPB"], [A_GEN(MODELS["SEPB"])], idx)
    record("SEPB", pred, v, why)


# padding models: body = hull of A-products, B-products (symbolic normalized pair tables) and (w0, 1)
def pad_gens(M, extra):
    g = [("A-product", M["Ast"](flat(Xn), flat(Yn))), ("B-product", M["Bst"](flat(Ln), flat(Lpn)))]
    if extra:
        g.append(("(w0, 1)", (M["w0"], O1)))
    return g


for nm, extra in (("PAD1", True), ("PAD2", False), ("PAD3", True)):
    M = MODELS[nm]
    for pred, idx in (("tok", I4), ("STMC", LE1)):
        res = on_points(M, pad_gens(M, extra), idx)
        fails = [(lab, bad[:2]) for lab, bad in res if bad]
        record(nm, pred, not fails, "failing generators: %s" % fails if fails else "holds on every generator")


def lt_A_iota(M):
    """TA restricted to iota(W4) is the identity table map (injective)"""
    T = M["TA"](iotaZ)
    return all(zero(T[I] - Zs[I]) for I in I4)


def lt_B_iota(M):
    """TB restricted to iota(W4) is a signed permutation of the coordinates (injective)"""
    T = M["TB"](iotaZ)
    seen = set()
    for I in I4:
        e = sp.expand(T[I])
        syms = e.free_symbols
        if len(syms) != 1:
            return False
        s = next(iter(syms))
        if sp.expand(e / s) not in (1, -1) or s in seen:
            return False
        seen.add(s)
    return len(seen) == 256


for nm in ["M_sig", "M_rho", "M_tw", "M_th", "M_id", "M_T", "SEPB"]:
    M = MODELS[nm]
    # every body of these models lies in iota(W4): A-products and B-products of normalized pair tables are iota of
    # four-token tables (checked on symbolic normalized pair tables)
    gA, gB = A_GEN(M), B_GEN(M)
    in_span = ceq(gA, iota(M["TA"](gA))) and ceq(gB, iota(M["TA"](gB)))
    record(nm, "LTA", in_span and lt_A_iota(M), "TA is the identity on iota(W4); body in iota(W4): %s" % in_span)
    record(nm, "LTB", in_span and lt_B_iota(M), "TB is a signed permutation on iota(W4)")
# anchor sum and padding: explicit pairs of distinct body points with equal A-readings
for nm in ["ANCc", "ANCz"]:
    anc = MODELS[nm]
    pt2 = anc["Bst"](E00, flat(ps3([0, 0, 1], [0, 0, 1])))      # (b0, a product)
    pt3 = anc["Bst"](E00, E00)
    same_A = all(zero(anc["TA"](pt2)[I] - anc["TA"](pt3)[I]) for I in I4) and not ceq(pt2[1], pt3[1])
    record(nm, "LTA", not same_A, "two B-products with equal A-readings and different points")
for nm in ["PAD1", "PAD3"]:
    M = MODELS[nm]
    w0 = M["w0"]
    p0, p1 = (w0, Z0), (w0, O1)
    eqA = all(zero(M["TA"](p0)[I] - M["TA"](p1)[I]) for I in I4)
    record(nm, "LTA", not eqA, "(w0, 0) and (w0, 1) are body points with equal A-readings")
M2 = MODELS["PAD2"]
q0 = M2["Ast"](flat(ps3([0, 0, 1], [0, 0, 1])), flat(ps3([0, 0, 1], [0, 0, 1])))
q1 = M2["Bst"](flat(ps3([0, 0, 1], [0, 0, 1])), flat(ps3([0, 0, 1], [0, 0, 1])))
eqA2 = all(zero(M2["TA"](q0)[I] - M2["TA"](q1)[I]) for I in I4) and not zero(q0[1] - q1[1])
record("PAD2", "LTA", not eqA2, "pA(z,z,z,z) and pB(z,z,z,z) differ and have equal A-readings")


# --------------------------------------------------------------------- RIL: relabelling covariance
def tau1(w):       # token exchange on the first slot of the carrier
    return [[w[0][n] for n in N17]] + [[w[1 + TAU[k]][n] for n in N17] for k in N16]


def check_RIL(M, Phi):
    st = point_eq(M, Phi(M["Ast"](flat(Xn), flat(Yn))), M["Bst"](flat(Xn), flat(Yn)))
    if M["kind"] == "C":
        wsym = [[sp.Symbol("v%d_%d" % (m, n)) for n in N17] for m in N17]
    else:
        wsym = ([[sp.Symbol("v%d_%d" % (m, n)) for n in N17] for m in N17],
                [[sp.Symbol("u%d_%d" % (m, n)) for n in N17] for m in N17])
    ef = zero(M["Bef"](ea, fa, Phi(wsym)) - M["Aef"](ea, fa, wsym))
    return st and ef


ril = {}
ril["M_sig"] = check_RIL(MODELS["M_sig"], sigma)
ril["M_id"] = check_RIL(MODELS["M_id"], lambda w: w)
ril["M_T"] = check_RIL(MODELS["M_T"], lambda w: sigma(tau1(w)))
ril["ANCc"] = check_RIL(MODELS["ANCc"], lambda w: (w[1], w[0]))
ril["ANCz"] = check_RIL(MODELS["ANCz"], lambda w: (w[1], w[0]))
for k, v in ril.items():
    record(k, "RIL", v, "Phi = %s; body preservation: %s" % (
        {"M_sig": "sigma", "M_id": "id", "M_T": "sigma o tau_1", "ANCc": "swap of the components",
         "ANCz": "swap of the components"}[k],
        {"M_sig": "sigma(iota B4) = iota(R B4) = iota B4 [W: R permutes tensor factors]",
         "M_id": "trivial", "M_T": "tau_1 and sigma permute tensor factors of iota B4 [W]",
         "ANCc": "the swap exchanges the two generating sets (a0 = b0)",
         "ANCz": "the swap exchanges the two generating sets (a0 = b0)"}[k]))
for k in ["M_rho", "M_tw", "M_th"]:
    record(k, "RIL", None, "N/A as stated: pairBody K23 = Q3 differs from pairBody K13 = twin (q3 t4)")


# --------------------------------------------------------------------- OLTI: operation-level token identity
def rhat(R):
    return [[O1, Z0, Z0, Z0]] + [[Z0] + [sp.Integer(R[i][j]) for j in range(3)] for i in range(3)]


def act_index(Rh, x, pos):
    """apply the homogenized map Rh to the first (pos 0) or second (pos 1) token index of a flat pair vector"""
    T = [[x[4 * m + n] for n in R4] for m in R4]
    if pos == 0:
        T2 = [[sum(Rh[m][k] * T[k][n] for k in R4) for n in R4] for m in R4]
    else:
        T2 = [[sum(Rh[n][k] * T[m][k] for k in R4) for n in R4] for m in R4]
    return flat(T2)


A_POS = {0: (0, 0), 1: (0, 1), 2: (1, 0), 3: (1, 1)}    # token -> (slot of PA, index in the pair)
B_POS = {0: (0, 0), 2: (0, 1), 1: (1, 0), 3: (1, 1)}    # token -> (slot of PB, index in the pair)


def gammaA(t, Rh):
    slot, pos = A_POS[t]

    def g(w):
        out = [row[:] for row in w]
        if slot == 0:
            for n in N17:
                col = [w[1 + k][n] for k in N16]
                new = act_index(Rh, col, pos)
                for k in N16:
                    out[1 + k][n] = new[k]
        else:
            for m in N17:
                new = act_index(Rh, [w[m][1 + k] for k in N16], pos)
                for k in N16:
                    out[m][1 + k] = new[k]
        return out
    return g


def gammaB(t, Rh):         # the same action in PB's layout (used for the second component of the anchor sum)
    slot, pos = B_POS[t]
    return gammaA({(0, 0): 0, (0, 1): 1, (1, 0): 2, (1, 1): 3}[(slot, pos)], Rh)


def olti(M, Rs):
    Lsym, Lpsym = flat(Ln), flat(Lpn)
    Xs_, Ys_ = flat(Xn), flat(Yn)
    for t in R4:
        for R in Rs:
            Rh = rhat(R)
            if M["kind"] == "C":
                G = gammaA(t, Rh)
            else:
                GA, GB = gammaA(t, Rh), gammaB(t, Rh)
                G = (lambda GA, GB: (lambda w: (GA(w[0]), GB(w[1]))))(GA, GB)
            sa, pa = A_POS[t]
            Xt = act_index(Rh, Xs_, pa) if sa == 0 else Xs_
            Yt = act_index(Rh, Ys_, pa) if sa == 1 else Ys_
            if not point_eq(M, G(M["Ast"](Xs_, Ys_)), M["Ast"](Xt, Yt)):
                return False, "A-covariance fails (token %d)" % t
            sb, pb = B_POS[t]
            Lt = act_index(Rh, Lsym, pb) if sb == 0 else Lsym
            Lpt = act_index(Rh, Lpsym, pb) if sb == 1 else Lpsym
            if not point_eq(M, G(M["Bst"](Lsym, Lpsym)), M["Bst"](Lt, Lpt)):
                return False, "B-covariance fails at token %d for R = %s" % (t, R)
    return True, "A- and B-covariance hold for every token and every listed rotation"


R35Z = [[sp.Rational(3, 5), sp.Rational(-4, 5), 0], [sp.Rational(4, 5), sp.Rational(3, 5), 0], [0, 0, 1]]
R35X = [[1, 0, 0], [0, sp.Rational(3, 5), sp.Rational(-4, 5)], [0, sp.Rational(4, 5), sp.Rational(3, 5)]]
ROTS = [RZ90, RX180, R35Z, R35X]
for nm in ["M_sig", "M_rho", "M_tw", "M_th", "M_id", "M_T", "ANCc", "ANCz"]:
    ok, why = olti(MODELS[nm], ROTS)
    record(nm, "OLTI", ok, why)
for nm in [k for k in MODELS if k != "ANC"]:
    record(nm, "ONE", True if nm != "SEPB" else False,
           "by construction" if nm != "SEPB" else "separate bodies (one_body dropped)")

# ===================================================================== report
PREDS = ["ONE", "RIL", "OLTI", "STMC", "IP1BA", "IP1AB", "IPBA", "IPAB", "TPS", "tok", "LTA", "LTB"]


def fmt(v):
    return {True: "HOLDS", False: "FAILS", None: "N/A"}[v]


for nm in ["M_sig", "ANCc", "ANCz", "M_rho", "M_tw", "M_id", "M_T", "M_th", "PAD1", "PAD2", "PAD3", "SEPB"]:
    for p in PREDS:
        if p in RESULTS.get(nm, {}):
            v, why = RESULTS[nm][p]
            print("RESULT %-5s %-5s %-5s%s" % (nm, p, fmt(v), ("  (" + why + ")") if why else ""))


def res(nm, p):
    return RESULTS.get(nm, {}).get(p, (None, None))[0]


# C controls
ctrl_sig = all(res("M_sig", p) is True for p in ["TPS", "IP1BA", "IP1AB", "IPBA", "IPAB", "STMC", "tok", "RIL", "OLTI",
                                                   "LTA", "LTB"])
check("C1 control M_sig: every predicate HOLDS", ctrl_sig)
CM = ["ANCc", "ANCz", "M_rho", "M_tw", "M_id", "M_T", "M_th"]
check("C2 every SOURCE countermodel and M_th: tok FAILS and TPS FAILS",
      all(res(m, "tok") is False and res(m, "TPS") is False for m in CM),
      ", ".join("%s:tok=%s,TPS=%s" % (m, fmt(res(m, "tok")), fmt(res(m, "TPS"))) for m in CM))
# S separations
check("S1 PAD1: IP1BA, IPBA, TPS HOLD; tok FAILS; LTA FAILS",
      res("PAD1", "IP1BA") is True and res("PAD1", "IPBA") is True and res("PAD1", "TPS") is True
      and res("PAD1", "tok") is False and res("PAD1", "LTA") is False)
check("S2 PAD2: tok HOLDS; TPS FAILS; LTA FAILS",
      res("PAD2", "tok") is True and res("PAD2", "TPS") is False and res("PAD2", "LTA") is False)
check("S3 PAD3: STMC HOLDS; IP1BA HOLDS; tok FAILS; LTA FAILS",
      res("PAD3", "STMC") is True and res("PAD3", "IP1BA") is True and res("PAD3", "tok") is False
      and res("PAD3", "LTA") is False)
# SEPB: an explicit negative PA product effect (of token effects) at a pure PB product
gz_dn = (sp.Rational(1, 2), [0, 0, sp.Rational(-1, 2)])     # token effect (1 - z)/2, zero at +z
gy_dn = (sp.Rational(1, 2), [0, sp.Rational(-1, 2), 0])     # token effect (1 - y)/2
uu = (O1, [0, 0, 0])


def pair_eff(g, gp):            # the pair effect g (x) g' as an affine functional on the flat chart
    hg, hgp = [g[0]] + list(g[1]), [gp[0]] + list(gp[1])
    return (Z0, [sp.Integer(1) * hg[m] * hgp[n] for m in R4 for n in R4])


SE = MODELS["SEPB"]
wpb = pB_of(SE, [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 1, 0]])
neg = SE["Aef"](pair_eff(gz_dn, uu), pair_eff(uu, gy_dn), wpb)
check("S4 SEPB: IP1BA HOLDS, LTA HOLDS, tok FAILS, and PA.prodEff (t(z-, u)) (t(u, y-)) at pB(z, z, z, y) is "
      "negative (no common body)",
      res("SEPB", "IP1BA") is True and res("SEPB", "LTA") is True and res("SEPB", "tok") is False and neg < 0,
      "value = %s" % neg)
tw_tok = MODELS["M_tw"]["ip1ba_tok"]
th_tok = MODELS["M_th"]["ip1ba_tok"]
check("S5 M_tw and M_th: IP1BA holds at tokens 0, 1, 2 and fails at token 3",
      all(tw_tok[t] for t in (0, 1, 2)) and not tw_tok[3] and all(th_tok[t] for t in (0, 1, 2)) and not th_tok[3])
check("F no float entered any checked quantity", no_float(neg, [RESULTS[k][p][1] for k in RESULTS for p in RESULTS[k]
                                                                if isinstance(RESULTS[k][p][1], sp.Basic)]))

nfail = sum(1 for _, ok in CHECKS if not ok)
if nfail == 0:
    CANDS = ["ONE", "RIL", "OLTI", "STMC", "IP1BA", "IP1AB", "IPBA", "IPAB", "TPS"]
    MM = {"ANC": ["ANCc", "ANCz"], "M_rho": ["M_rho"], "M_tw": ["M_tw"], "M_id": ["M_id"], "M_T": ["M_T"],
          "M_th": ["M_th"]}
    for c in CANDS:
        for G in ["tok", "TPS"]:
            if c == G:
                continue
            ref = [m for m, mem in MM.items() if any(res(x, c) is True and res(x, G) is False for x in mem)]
            print("REFUTATION %-5s => %-3s : %s" % (c, G, ("REFUTED by " + ", ".join(ref)) if ref else "SURVIVES"))
print("--- q1_tok_models: %d/%d checks pass" % (len(CHECKS) - nfail, len(CHECKS)))
print("VERDICT Q1-PART-A-MODELS-EXACT" if nfail == 0 else "VERDICT NOT RENDERED")
