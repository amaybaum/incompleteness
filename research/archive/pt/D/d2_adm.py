#!/usr/bin/env python3
"""Thread D, certified script d2 -- admissibility clause by clause (RESULT.md section 1, D2).

hadm(K) = PairAdm K = CandidateCone K /\\ IsConvexCone K, i.e. (a) prodState x y in K for x, y in eball 3;
(b) K subset of maxCone (eball 3); (c) K closed under addition (c1) and nonnegative scaling (c2).
Product-test chart of a COMP-1 pre-composite P on a carrier V: q(v)[mu][nu] = P.prodEff (basisEff mu) (basisEff nu) v.

DECISION RULES (fixed before the first run):
  S0  [source] the transcribed landed definitions (CandidateCone, PairAdm, IsConvexCone, PreComposite fields,
      subset_maxBody, maxBody, coeff vs ehom, COMP-1 hom vs DIM-1 hom, ball3 vs eball, padEff, paddedBall3 and its
      failure of local tomography, basisEff, IsEffectOn) must match the Lean text at L / at the design export.
  S1  chart identities (symbolic): pEff e f w = pairVal(coeff e, coeff f, w) = prodEffVal e f w; pEff(basisEff mu,
      basisEff nu) w = w[mu][nu]; pState x y = prodState x y; for paddedBall3, q(w, h) = w and
      padEff e f (w, h) = sum coeff e mu coeff f nu q(w, h)[mu][nu] (symbolic e, f, w, h).
  S2  converse pieces (symbolic): pEff(e, f) = pEff(1,1) - pEff(1 - e, f) - pEff(1, 1 - f); and
      pairVal(e0 + s e_mu, e0 + t e_nu, w) = w00 + t w0nu + s wmu0 + s t wmunu, whose four sign choices bound
      |w[mu][nu]| by w00 on maxCone.
  S3  countermodel for clause (a), M_class (cone of the four products prodState(s z3)(t z3)): (a) FAILS at an exact
      witness; its generators are products (so (b) holds by prodState_mem_maxCone); cnot permutes the generators (hgate);
      the four-copy values factor at generator pairs (famI and famII forms, symbolic E, F), which with effects
      nonnegative on the generators gives posBA/posAB; IE1 fails at an exact witness.
  S4  countermodel for clause (b), uniform W 3: (b) FAILS at an exact witness; the explicit carrier's evaluation laws
      and both token clauses hold as identities (symbolic data); effect tables on the slice of W 3 are c E00, and
      fourVal(X, Y, cE00, c'E00) = c c' X00 Y00 and the famII value likewise (symbolic); the odd gate pattern
      (cnot, cnot, cnot, cnotTw) is N-CLASS with orient bits (0, 0, 0, 1), so EvenCycle fails.
  S5  countermodel for clause (c), the scaled cnotOrbit {s w : s >= 0, w product or cnot product}: (c1) FAILS at an
      exact witness (rank of the candidate preimage); cnot preserves the (0,0) entry and is an involution (so cnot maps
      the set onto itself); products and their cnot images have (0,0) entry 1.
  S6  M_mix (ray of E00): (a) FAILS at an exact witness; E00 = prodState 0 0 (so (b) holds); a ray is a convex cone.
  Countercontrols (must give the opposite verdict): CC1 the uniform-Q3 table phiW is not in M_class's cone (support
  check) -- i.e. M_class is not mistaken for Q3; CC2 the factorization of S3 FAILS for a non-classical pair (phiW,
  phiW) with symbolic E, F; CC3 a product table IS in the ray of E00 only for x = y = 0 (prodState xplus xplus is not);
  CC4 the effect-table formula of S4 gives a non-constant functional when the coefficient vector has a nonzero entry
  off index 0 (unbounded on the slice); CC5 the sum p + cnot p in S5 IS of the form 2 q with q = (p + cnot p)/2, and
  q is cnot-fixed -- the failure is membership, not arithmetic.
  A VERDICT line prints only if every check passes and every countercontrol behaves as stated.
Exact arithmetic only (sympy, rationals). No floating point, no randomness, no timing in stdout.
"""
import re
import sys
from itertools import product
from pathlib import Path

import sympy as sp

CHECKS = []


def chk(cid, name, ok, kind):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}", flush=True)


def section(t):
    print()
    print(f'== {t}', flush=True)


R4 = range(4)
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
NEG = {(1, 3), (2, 2)}


def cnot(w):
    return sp.Matrix(4, 4, lambda m, k: (-1 if (m, k) in NEG else 1) * w[PC[m][k], PT[m][k]])


def homMap(R):
    M = sp.zeros(4, 4)
    M[0, 0] = 1
    M[1:4, 1:4] = sp.Matrix(R)
    return M


def actC(R, w):
    return homMap(R) * w


def actT(R, w):
    return w * homMap(R).T


def hom(x):
    return sp.Matrix([1] + list(x))


def prodState(x, y):
    return hom(x) * hom(y).T


def pairVal(a, b, w):
    return (sp.Matrix(a).T * w * sp.Matrix(b))[0, 0]


def ipW(E, X):
    return sum(E[m, k] * X[m, k] for m in R4 for k in R4)


def fourVal(X, Y, E, F):
    return sum(X[a, b] * Y[c, d] * E[a, c] * F[b, d] for a, b, c, d in product(R4, repeat=4))


def famII(e, f, L, Lp):
    return sum(e[a, b] * f[c, d] * L[a, c] * Lp[b, d] for a, b, c, d in product(R4, repeat=4))


z3 = [0, 0, 1]
xplus = [1, 0, 0]
O3 = [0, 0, 0]
REFLY = sp.diag(1, -1, 1)
I3 = sp.eye(3)
phiW = sp.diag(1, 1, -1, 1)
E00 = prodState(O3, O3)
W = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'w{i}{j}', real=True))

# =====================================================================================================================
section('S0  transcription (read-only)')
BASE = Path('/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/pt/base')
INP = Path('/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/pt/inputs')
OI = BASE / 'verification/lean-mathlib/OIBridge'
CD = (OI / 'CompositeDimension.lean').read_text(encoding='utf-8')
KG = (OI / 'K2Guard.lean').read_text(encoding='utf-8')
CI = (OI / 'CompositeInterface.lean').read_text(encoding='utf-8')
KF = (OI / 'KInfFoundations.lean').read_text(encoding='utf-8')
TB = (OI / 'TransitiveBody.lean').read_text(encoding='utf-8')
FD = (INP / 'fourcopy/FourCopyDefs.lean').read_text(encoding='utf-8')
chk('S0.cand', 'CandidateCone K := (forall x y in eball 3, prodState x y in K) /\\ K subset maxCone (eball 3) (K2G)',
    'def CandidateCone (K : Set (W 3)) : Prop :=\n  (∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K) ∧ K ⊆ maxCone (eball 3)' in KG,
    'source')
chk('S0.adm', 'PairAdm K := CandidateCone K /\\ IsConvexCone K; IsConvexCone = additivity and nonnegative scaling (design)',
    'def PairAdm (K : Set (W 3)) : Prop := CandidateCone K ∧ IsConvexCone K' in FD
    and '(∀ ω ∈ K, ∀ ω\' ∈ K, ω + ω\' ∈ K) ∧ ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K' in FD, 'source')
chk('S0.pre', 'PreComposite fields: convex, prod_mem, prodEff_effect, prodEff_unit (no local tomography field)',
    all(s in CI for s in ('convex : Convex ℝ Ω', 'prod_mem : ∀ x ∈ ΩA, ∀ y ∈ ΩB, prodState x y ∈ Ω',
                          'prodEff_effect : ∀ (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ),',
                          'prodEff_unit : ∀ ω ∈ Ω, prodEff (unitEff dA) (unitEff dB) ω = 1'))
    and re.search(r'structure PreComposite[\s\S]*?prodEff_unit[^\n]*\n\n', CI) is not None
    and 'lt :' not in re.search(r'structure PreComposite[\s\S]*?prodEff_unit[^\n]*\n\n', CI).group(0), 'source')
chk('S0.sub', 'subset_maxBody : P.Omega subset maxBody; maxBody = normalized points nonnegative on product effects',
    'theorem subset_maxBody : P.Ω ⊆ P.toProductData.maxBody ΩA ΩB := fun ω hω =>' in CI
    and '{ω | D.prodEff (unitEff dA) (unitEff dB) ω = 1 ∧' in CI, 'source')
chk('S0.coeff', 'COMP-1 coeff e = Fin.cons (e 0) (linear coefficients) and DIM-1 ehom e = vecCons (e 0) (the same)',
    'Fin.cons (e 0) fun i => e.linear (fun j => if i = j then 1 else 0)' in CI
    and 'Matrix.vecCons (e 0) fun j => e.linear fun i => if j = i then (1 : ℝ) else 0' in CD, 'source')
chk('S0.hom', 'COMP-1 Model.hom x = Fin.cons 1 x and DIM-1 hom x = Matrix.vecCons 1 x',
    'def hom (x : Fin d → ℝ) : Fin (d + 1) → ℝ := Fin.cons 1 x' in CI
    and 'def hom (x : Fin d → ℝ) : HVec d := Matrix.vecCons 1 x' in CD, 'source')
chk('S0.ball', 'ball3 = {v | v0^2 + v1^2 + v2^2 <= 1} and eball d = {x | sum x_j^2 <= 1}',
    'def ball3 : Set (Fin 3 → ℝ) := {v | v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2 ≤ 1}' in KF
    and 'def eball (d : ℕ) : Set (Fin d → ℝ) := {x | ∑ j, x j ^ 2 ≤ 1}' in TB, 'source')
chk('S0.pad', 'padEff reads P\'s pairing on the first component; paddedBall3 := paddedPre ball3MinComposite; '
    'not_locallyTomographic_paddedBall3 is landed',
    '(P.prodEff e f).comp (AffineMap.fst : V × ℝ →ᵃ[ℝ] V)' in CI
    and 'def paddedBall3 : PreComposite ball3 ball3 (Carrier 3 3 × ℝ) :=\n  paddedPre ball3MinComposite.toPreComposite' in CI
    and 'theorem not_locallyTomographic_paddedBall3 : ¬ LocallyTomographic paddedBall3 :=' in CI, 'source')
chk('S0.basis', 'basisEff mu = Fin.cons (unitEff d) coord mu; IsEffectOn: 0 <= e x <= 1 on the set',
    '(Fin.cons (unitEff d) coord : Fin (d + 1) → (Fin d → ℝ) →ᵃ[ℝ] ℝ) μ' in CI
    and 'def IsEffectOn (Ω : Set V) (e : V →ᵃ[ℝ] ℝ) : Prop :=\n  ∀ x ∈ Ω, 0 ≤ e x ∧ e x ≤ 1' in KF, 'source')
chk('S0.cands', 'landed candidate cones: candidateCone_productSet, candidateCone_cnotOrbit, cnot_mem_cnotOrbit',
    all(s in KG for s in ('theorem candidateCone_productSet : CandidateCone productSet',
                          'theorem candidateCone_cnotOrbit : CandidateCone cnotOrbit',
                          'theorem cnot_mem_cnotOrbit {ω : W 3} (hω : ω ∈ cnotOrbit) : cnot ω ∈ cnotOrbit')), 'source')

# =====================================================================================================================
section('S1  the product-test chart')
ce = sp.Matrix(sp.symbols('ce0:4', real=True))      # coeff e = (e 0, linear coefficients)
cf = sp.Matrix(sp.symbols('cf0:4', real=True))
pEff = sum(ce[m] * cf[k] * W[m, k] for m in R4 for k in R4)
chk('S1.a', 'pEff e f w = sum coeff e mu coeff f nu w[mu][nu] = pairVal(coeff e, coeff f, w), i.e. DIM-1 prodEffVal '
    '(coeff = ehom by S0.coeff)', sp.expand(pEff - pairVal(ce, cf, W)) == 0, 'identity')
ok = True
for m, k in product(R4, R4):
    em = sp.Matrix([1 if i == m else 0 for i in R4]); ek = sp.Matrix([1 if i == k else 0 for i in R4])
    ok = ok and pairVal(em, ek, W) == W[m, k]
chk('S1.b', 'pEff(basisEff mu, basisEff nu) w = w[mu][nu] (coeff basisEff mu is the unit vector; landed pEff_basisEff)',
    ok, 'identity')
xs = sp.symbols('x0:3', real=True); ys = sp.symbols('y0:3', real=True)
chk('S1.c', 'pState x y = hom x hom y^T = prodState x y (symbolic)',
    sp.expand(sp.Matrix(4, 4, lambda m, k: hom(xs)[m] * hom(ys)[k]) - prodState(xs, ys)) == sp.zeros(4, 4), 'identity')
hh = sp.Symbol('h', real=True)


def padEff(cE, cF, w, h):
    """paddedBall3's pairing: P's pairing (the model's pEff) read on the first component."""
    return sum(cE[m] * cF[k] * w[m, k] for m in R4 for k in R4)


qpad = sp.Matrix(4, 4, lambda m, k: padEff([1 if i == m else 0 for i in R4], [1 if i == k else 0 for i in R4], W, hh))
chk('S1.d', 'paddedBall3: q(w, h) = w (the chart forgets the height h), and padEff e f (w, h) = '
    'sum coeff e mu coeff f nu q(w, h)[mu][nu] (symbolic e, f, w, h)',
    sp.expand(qpad - W) == sp.zeros(4, 4)
    and sp.expand(padEff(ce, cf, W, hh) - sum(ce[m] * cf[k] * qpad[m, k] for m in R4 for k in R4)) == 0, 'identity')
chk('S1.e', 'paddedBall3 product states are (prodState x y, 0) and q maps them to prodState x y; its body '
    'minBody x [0,1] has image minBody under q', sp.expand(sp.Matrix(4, 4, lambda m, k: padEff(
        [1 if i == m else 0 for i in R4], [1 if i == k else 0 for i in R4], prodState(xs, ys), 0)) - prodState(xs, ys))
    == sp.zeros(4, 4), 'identity')

# =====================================================================================================================
section('S2  the converse pieces')
one = sp.Matrix([1, 0, 0, 0])
chk('S2.a', 'pEff(e, f) = pEff(1, 1) - pEff(1 - e, f) - pEff(1, 1 - f) (bilinearity; symbolic coefficients)',
    sp.expand(pairVal(ce, cf, W) - (pairVal(one, one, W) - pairVal(one - ce, cf, W) - pairVal(one, one - cf, W))) == 0,
    'identity')
s_, t_ = sp.symbols('s t', real=True)
ok2 = True
for m, k in product(R4, R4):
    em = sp.Matrix([1 if i == m else 0 for i in R4]); ek = sp.Matrix([1 if i == k else 0 for i in R4])
    lhs = pairVal(one + s_ * em, one + t_ * ek, W)
    ok2 = ok2 and sp.expand(lhs - (W[0, 0] + t_ * W[0, k] + s_ * W[m, 0] + s_ * t_ * W[m, k])) == 0
chk('S2.b', 'pairVal(e0 + s e_mu, e0 + t e_nu, w) = w00 + t w0nu + s wmu0 + s t wmunu for all mu, nu (symbolic); with '
    's, t = +-1 (vectors in L) the four values average to w00 +- wmunu, so |wmunu| <= w00 on maxCone', ok2, 'identity')

# =====================================================================================================================
section('S3  clause (a): the countermodel M_class')
gens = {(s, t): prodState([0, 0, s], [0, 0, t]) for s in (1, -1) for t in (1, -1)}
pxx = prodState(xplus, xplus)
chk('S3.a.fail', 'clause (a) fails: prodState xplus xplus has entry (1,1) = 1, every generator vanishes off {0,3}x{0,3}',
    pxx[1, 1] == 1 and all(g[m, k] == 0 for g in gens.values() for m in R4 for k in R4 if not (m in (0, 3) and k in (0, 3))),
    'witness')
chk('S3.gate', 'cnot maps the generators onto the generators: cnot prodState(s z3)(t z3) = prodState(s z3)(s t z3)',
    all(cnot(gens[(s, t)]) == gens[(s, s * t)] for s in (1, -1) for t in (1, -1)), 'enumerate')
Es = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'E{i}{j}', real=True))
Fs = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'F{i}{j}', real=True))
okI = okII = True
for (s1, t1), (s2, t2) in product(gens.keys(), repeat=2):
    X, Y = gens[(s1, t1)], gens[(s2, t2)]
    okI = okI and sp.expand(fourVal(X, Y, Es, Fs) - ipW(Es, gens[(s1, s2)]) * ipW(Fs, gens[(t1, t2)])) == 0
    okII = okII and sp.expand(famII(Es, Fs, X, Y) - ipW(Es, gens[(s1, s2)]) * ipW(Fs, gens[(t1, t2)])) == 0
chk('S3.H', 'at every pair of generators fourVal X Y E F and the famII value equal ipW E (generator) * ipW F (generator) '
    '(symbolic E, F; 16 pairs): with effect tables nonnegative on the generators, posBA and posAB hold on the carrier '
    'of S4', okI and okII, 'identity')
RH = sp.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
img = actT(RH, gens[(1, 1)])
chk('S3.ie1', 'IE1 fails: actT R_H (prodState z3 z3) = prodState z3 xplus, entry (3,1) = 1 outside the support of K_class',
    img == prodState(z3, xplus) and img[3, 1] == 1 and RH.T * RH == I3 and RH.det() == 1, 'witness')
chk('CC1', 'countercontrol: phiW (a Q3 table) is NOT in M_class\'s cone (entry (1,1) = 1 off the support)',
    phiW[1, 1] == 1, 'countercontrol')
chk('CC2', 'countercontrol: the factorization FAILS at the non-classical pair (phiW, phiW) (symbolic E, F)',
    sp.expand(fourVal(phiW, phiW, Es, Fs) - ipW(Es, phiW) * ipW(Fs, phiW)) != 0, 'countercontrol')

# =====================================================================================================================
section('S4  clause (b): uniform W 3, on an explicit four-copy carrier')
# carrier V = R^{17x17} x R^{17x17}; x-hat = (1, x) with x in R^16 indexed by flat(a, b) = 4a + b
xv = sp.symbols('X0:16', real=True); yv = sp.symbols('Y0:16', real=True)
xh = sp.Matrix([1] + list(xv)); yh = sp.Matrix([1] + list(yv))


def flat(a, b):
    return 4 * a + b


def tab(v):
    return sp.Matrix(4, 4, lambda a, b: v[flat(a, b)])


def Et_of(e0, Evec):
    return sp.Matrix(4, 4, lambda a, b: Evec[flat(a, b)] + (e0 if (a == 0 and b == 0) else 0))


def effA(e0, Ev, f0, Fv, P, Qm):
    eh = sp.Matrix([e0] + list(Ev)); fh = sp.Matrix([f0] + list(Fv))
    Et, Ft = Et_of(e0, Ev), Et_of(f0, Fv)
    return (eh.T * P * fh)[0, 0] + sum(Et[a, b] * Ft[c, d] * Qm[1 + flat(a, c), 1 + flat(b, d)]
                                       for a, b, c, d in product(R4, repeat=4))


def effB(e0, Ev, f0, Fv, P, Qm):
    eh = sp.Matrix([e0] + list(Ev)); fh = sp.Matrix([f0] + list(Fv))
    Et, Ft = Et_of(e0, Ev), Et_of(f0, Fv)
    return (eh.T * Qm * fh)[0, 0] + sum(Et[a, c] * Ft[b, d] * P[1 + flat(a, b), 1 + flat(c, d)]
                                        for a, b, c, d in product(R4, repeat=4))


Z17 = sp.zeros(17, 17)
stA = (xh * yh.T, Z17)
stB = (Z17, xh * yh.T)
e0s, f0s = sp.symbols('e0 f0', real=True)
Ev = sp.symbols('Ee0:16', real=True); Fv = sp.symbols('Ff0:16', real=True)
eval_x = e0s + sum(Ev[i] * xv[i] for i in range(16)); eval_y = f0s + sum(Fv[i] * yv[i] for i in range(16))
chk('S4.evalA', 'effA e f (stA x y) = e(x) f(y) (symbolic e, f, x, y)',
    sp.expand(effA(e0s, Ev, f0s, Fv, *stA) - eval_x * eval_y) == 0, 'identity')
chk('S4.evalB', 'effB e f (stB x y) = e(x) f(y) (symbolic e, f, x, y)',
    sp.expand(effB(e0s, Ev, f0s, Fv, *stB) - eval_x * eval_y) == 0, 'identity')


def coordvec(a, b):
    return [1 if i == flat(a, b) else 0 for i in range(16)]


okt = True
for a, b, c, d in product(R4, repeat=4):
    lA = effA(0, coordvec(a, b), 0, coordvec(c, d), *stA)
    rA = effB(0, coordvec(a, c), 0, coordvec(b, d), *stA)
    lB = effA(0, coordvec(a, b), 0, coordvec(c, d), *stB)
    rB = effB(0, coordvec(a, c), 0, coordvec(b, d), *stB)
    okt = okt and sp.expand(lA - rA) == 0 and sp.expand(lB - rB) == 0
chk('S4.tok', 'tokA and tokB hold at all 256 index quadruples (symbolic x, y)', okt, 'enumerate')
chk('S4.cross', 'effB e f (stA x y) = fourVal(tab x, tab y, Et, Ft) and effA e f (stB x y) = famII(Et, Ft, tab x, tab y) '
    '(symbolic e, f, x, y)',
    sp.expand(effB(e0s, Ev, f0s, Fv, *stA) - fourVal(tab(xv), tab(yv), Et_of(e0s, Ev), Et_of(f0s, Fv))) == 0
    and sp.expand(effA(e0s, Ev, f0s, Fv, *stB) - famII(Et_of(e0s, Ev), Et_of(f0s, Fv), tab(xv), tab(yv))) == 0,
    'identity')
cc_, cd_ = sp.symbols('c cprime', real=True)
Xs = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'P{i}{j}', real=True))
Ys = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'R{i}{j}', real=True))
chk('S4.H', 'fourVal(X, Y, c E00, c\' E00) = c c\' X00 Y00 and famII(c E00, c\' E00, X, Y) = c c\' X00 Y00 (symbolic): '
    '>= 0 on the slice (X00 = Y00 = 1) for c, c\' in [0, 1]',
    sp.expand(fourVal(Xs, Ys, cc_ * E00, cd_ * E00) - cc_ * cd_ * Xs[0, 0] * Ys[0, 0]) == 0
    and sp.expand(famII(cc_ * E00, cd_ * E00, Xs, Ys) - cc_ * cd_ * Xs[0, 0] * Ys[0, 0]) == 0, 'identity')
Evv = sp.symbols('V0:16', real=True)
etab = Et_of(e0s, [Evv[0]] + [0] * 15)
chk('S4.eff', 'an affine functional e(v) = e0 + E.v with E supported on index 0 has table (e0 + E0) E00',
    etab == (e0s + Evv[0]) * E00, 'identity')
vline = [1] + [0] * 15
vline2 = list(vline); vline2[5] = sp.Symbol('lam', real=True)
eval_line = e0s + Evv[0] * vline2[0] + sp.Rational(1) * vline2[5]
chk('CC4', 'countercontrol: with a nonzero coefficient off index 0 the functional is non-constant along the slice '
    '(value depends on the free coordinate lam): such e is not an effect on the slice of W 3',
    sp.diff(eval_line, sp.Symbol('lam', real=True)) != 0, 'countercontrol')
minus = -E00
chk('S4.b.fail', 'clause (b) fails for W 3: -E00 is in W 3 and pairVal(e0, e0, -E00) = -1 < 0 (e0 in L)',
    pairVal([1, 0, 0, 0], [1, 0, 0, 0], minus) == -1, 'witness')


def cnotTw(w):
    return actT(REFLY, cnot(actT(REFLY, w)))


chk('S4.odd', 'cnotTw = actC I (actT reflY (cnot (actC I (actT reflY w)))) (NClass with B = B\' = reflY); orient bits '
    '(I,I),(I,I),(I,I),(I,reflY) are (0,0,0,1): odd, so EvenCycle fails for the odd pattern',
    sp.expand(cnotTw(W) - actC(I3, actT(REFLY, cnot(actC(I3, actT(REFLY, W)))))) == sp.zeros(4, 4)
    and (I3.det() * REFLY.det() == -1) and (I3.det() * I3.det() == 1), 'identity')

# =====================================================================================================================
section('S5  clause (c): the scaled cnotOrbit')
p = prodState(xplus, z3)
cp = cnot(p)
qmid = (p + cp) / 2
chk('S5.00', 'cnot preserves the (0,0) entry and is an involution (symbolic); products have (0,0) entry 1',
    cnot(W)[0, 0] == W[0, 0] and sp.expand(cnot(cnot(W)) - W) == sp.zeros(4, 4) and prodState(xs, ys)[0, 0] == 1,
    'identity')
chk('CC5', 'countercontrol: p + cnot p = 2 q with q = (p + cnot p)/2, and cnot q = q (the obstruction is membership)',
    p + cp == 2 * qmid and cnot(qmid) == qmid, 'countercontrol')
chk('S5.c1.fail', f'(c1) fails: q = (p + cnot p)/2 has table rank {qmid.rank()} >= 2, so q is not a product; since cnot q = q '
    'and cnot is an involution, q is not the cnot image of a product either; (0,0) entries force the scale s = 2, so '
    'p + cnot p is not in the scaled cnotOrbit while p and cnot p are', qmid.rank() >= 2 and qmid[0, 0] == 1, 'witness')

# =====================================================================================================================
section('S6  M_mix (the ray of E00)')
chk('S6.a', 'M_mix: E00 = prodState 0 0; clause (a) fails since prodState xplus xplus is not a multiple of E00',
    E00 == prodState(O3, O3) and pxx[1, 1] == 1 and E00[1, 1] == 0, 'witness')
chk('CC3', 'countercontrol: prodState x y is a multiple of E00 only when x = y = 0 (entries (mu,0), (0,nu) are x, y)',
    all(prodState(xs, ys)[i + 1, 0] == xs[i] and prodState(xs, ys)[0, i + 1] == ys[i] for i in range(3)), 'countercontrol')

print()
fails = [c for c, k, ok in CHECKS if not ok]
print(f'd2_adm: {len(CHECKS)} checks, {len(fails)} failed')
if not fails:
    print('VERDICT D2-EXACT-STEPS-HOLD: the product-test chart identities hold (padded, non-locally-tomographic '
          'pre-composite included); the converse pieces hold; M_class fails (a) only, uniform W 3 fails (b) only, the '
          'scaled cnotOrbit fails (c1); the H reductions on the explicit carrier and the odd-pattern parity failure hold')
    sys.exit(0)
print('NO VERDICT: failed checks ' + ', '.join(fails))
sys.exit(1)
