#!/usr/bin/env python3
"""Thread B (PAIR-ACT), script b2_sources -- candidate sources of hgate (B2), restricted idle extension (B3), and the
certified-premise checklist behind the INDEPENDENT label.  Research only.

Exact arithmetic only (sympy); no floating point, no randomness, no time-dependence in stdout.
Run as:  python3 -I -B b2_sources.py <pt-root>   (reads base/ Lean sources only)

PARTS
  S0  [source]   transcription of the landed tables; the landed definitions read below (ball3, eball, NativeGate, CtrlGate,
                 GateRel, Entangling, NativeGateOf, CandidateCone, maxBody, ball3MaxComposite, ball3MinComposite,
                 JointReversible, PreservesBody, OpDatum, no_candidateCone_cnot_reflY) with file:line.
  S1  the native-gate premises (K1 inputs) for the four gates cnot, g_D = actT reflY . cnot, g_pre = cnot . actT reflY,
      g_Tw = actT reflY . cnot . actT reflY, all with DIM-1's NOT nflip and axis z3:
        frame [enumerate, the 4 corner pairs], relT and relC [identity], forward and inverse positivity on product
        states [identity reducing to the landed cnot_prodState_mem_maxCone and the actT reflY-invariance of maxCone],
        Entangling [witness: the image of the pure product (xplus, z3), its table rank; extremality by a written step].
  S2  admissible invariant cones: g_D and g_pre have none (an exact two-step chain leaves maxCone from a product
      state); cnot and g_Tw have one (Q3, twin) [identity D1 and the chart Dpt].
  S3  the certified-premise checklist for the countermodels M_max = (maxCone, cnot) and M_D13 = (Q3, g_D): one line per
      certified premise bearing on a pair cone or a pair gate, with the check or citation that the model satisfies it.
  S4  candidate sources of hgate and of the weaker clauses: what is derived, what is refuted, by which model.
  S5  restricted idle extension (B3).

DECISION RULE (fixed before the first run)
  Each check prints PASS or FAIL; it passes iff its exact identity/value/text comparison holds; a countercontrol passes
  iff the mutated object fails.  VERDICT lines print only if every check passed, with text generated from the checks.
  Otherwise 'b2_sources: NO VERDICT' and exit 1.
"""
import re
import sys
from itertools import product
from pathlib import Path

import sympy as sp

Q = sp.Rational
iu = sp.I
R4 = range(4)
CHECKS = {}
ORDER = []


def chk(cid, name, ok, kind, detail=''):
    ok = bool(ok)
    assert cid not in CHECKS, cid
    CHECKS[cid] = (kind, ok)
    ORDER.append(cid)
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}" + (f" -- {detail}" if detail else ''), flush=True)


def section(t):
    print()
    print(f'== {t}', flush=True)


def z(v):
    return sp.cancel(sp.together(sp.expand(v))) == 0


def mzero(M):
    return all(z(v) for v in M)


if len(sys.argv) != 2:
    print('usage: b2_sources.py <pt-root>')
    sys.exit(2)
ROOT = Path(sys.argv[1]).resolve()
LB = ROOT / 'base' / 'verification' / 'lean-mathlib' / 'OIBridge'

PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
NEG = {(1, 3), (2, 2)}


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: (-1 if (m, n) in NEG else 1) * w[PC[m][n], PT[m][n]])


def hom(x):
    return sp.Matrix([1] + list(x))


def homMap(R):
    M = sp.zeros(4, 4)
    M[0, 0] = 1
    M[1:4, 1:4] = sp.Matrix(R)
    return M


def actC(R, w):
    return homMap(R) * w


def actT(R, w):
    return w * homMap(R).T


def prodState(x, y):
    return hom(x) * hom(y).T


def pairVal(a, b, w):
    return (sp.Matrix(a).T * w * sp.Matrix(b))[0, 0]


def ipW(E, X):
    return sum(E[m, n] * X[m, n] for m in R4 for n in R4)


S = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -iu], [iu, 0]]), sp.Matrix([[1, 0], [0, -1]])]
SS = [[sp.kronecker_product(S[m], S[n]) for n in R4] for m in R4]


def pauliW(w):
    out = sp.zeros(4, 4)
    for m in R4:
        for n in R4:
            if w[m, n] != 0:
                out += w[m, n] * SS[m][n]
    return out / 4


def is_psd(M):
    from itertools import combinations
    if not mzero(M - M.conjugate().T):
        return False
    n = M.shape[0]
    for k in range(1, n + 1):
        for idx in combinations(range(n), k):
            d = sp.expand(M.extract(list(idx), list(idx)).det())
            if sp.im(d) != 0 or sp.re(d) < 0:
                return False
    return True


phiW = sp.diag(1, 1, -1, 1)
idW = sp.eye(4)
chainW = sp.Matrix([[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]])
reflY = sp.diag(1, -1, 1)
nflip = sp.diag(1, -1, -1)
I3 = sp.eye(3)
xplus = [1, 0, 0]
z3 = [0, 0, 1]
SHARP_NEGX = [Q(1, 2), Q(-1, 2), 0, 0]
SHARP_NEGZ = [Q(1, 2), 0, 0, Q(-1, 2)]
W = sp.Matrix(4, 4, lambda m, n: sp.Symbol(f'w{m}{n}', real=True))
xs = [sp.Symbol(f'x{i}', real=True) for i in range(3)]
ys = [sp.Symbol(f'y{i}', real=True) for i in range(3)]
a4 = [sp.Symbol(f'a{i}', real=True) for i in range(4)]
b4 = [sp.Symbol(f'b{i}', real=True) for i in range(4)]

GATES = {
    'cnot': (lambda w: cnot(w), lambda w: cnot(w)),
    'g_D': (lambda w: actT(reflY, cnot(w)), lambda w: cnot(actT(reflY, w))),
    'g_pre': (lambda w: cnot(actT(reflY, w)), lambda w: actT(reflY, cnot(w))),
    'g_Tw': (lambda w: actT(reflY, cnot(actT(reflY, w))), lambda w: actT(reflY, cnot(actT(reflY, w)))),
}

# ===============================================================================================================
section('S0  the landed definitions read here (file:line at L)')
SRC = {p.stem: p.read_text(encoding='utf-8') for p in sorted(LB.glob('*.lean'))}


def where(pattern, files=None):
    for f in (files or sorted(SRC)):
        for i, ln in enumerate(SRC[f].split('\n'), 1):
            if re.search(pattern, ln):
                return f'{f}.lean:{i}'
    return None


LOCS = {
    'IsNot': where(r'^structure IsNot '),
    'isNot_nflip': where(r'^theorem isNot_nflip '),
    'NativeGate': where(r'^structure NativeGate '),
    'nativeGate_cnot': where(r'^theorem nativeGate_cnot '),
    'cnot_prodState_mem_maxCone': where(r'^theorem cnot_prodState_mem_maxCone '),
    'Entangling': where(r'^def Entangling '),
    'entangling_cnot': where(r'^theorem entangling_cnot '),
    'maxCone': where(r'^def maxCone '),
    'jointStates': where(r'^def jointStates '),
    'CtrlGate': where(r'^structure CtrlGate '),
    'ctrlGate_of_nativeGate': where(r'^theorem ctrlGate_of_nativeGate '),
    'GateRel': where(r'^(?:def|structure) GateRel '),
    'gateRel_cnot': where(r'^theorem gateRel_cnot '),
    'NativeGateOf': where(r'^structure NativeGateOf '),
    'EntanglingOf': where(r'^def EntanglingOf '),
    'nativeGate_of_cone_eq': where(r'^theorem nativeGate_of_cone_eq '),
    'maxConeOf_avail_eq': where(r'^theorem maxConeOf_avail_eq '),
    'CandidateCone': where(r'^def CandidateCone '),
    'prodState_mem_maxCone': where(r'^theorem prodState_mem_maxCone '),
    'no_candidateCone_cnot_reflY': where(r'^theorem no_candidateCone_cnot_reflY '),
    'PreComposite': where(r'^structure PreComposite '),
    'Composite': where(r'^structure Composite '),
    'maxBody': where(r'^def maxBody '),
    'minBody': where(r'^def minBody '),
    'ball3MinComposite': where(r'^def ball3MinComposite '),
    'ball3MaxComposite': where(r'^def ball3MaxComposite '),
    'JointReversible': where(r'^abbrev JointReversible '),
    'PreservesBody': where(r'^def PreservesBody '),
    'OpDatum': where(r'^structure OpDatum '),
    'preservesBody_inducedEquiv': where(r'^theorem preservesBody_inducedEquiv '),
    'body_isClosed': where(r'^theorem body_isClosed '),
    'ball3': where(r'^def ball3 '),
    'eball': where(r'^def eball '),
}
chk('S0.locs', 'every landed identifier used in the checklist resolves at L', all(LOCS.values()), 'source',
    '; '.join(f'{k} {v}' for k, v in LOCS.items()))
CD, KG, CI = SRC['CompositeDimension'], SRC['K2Guard'], SRC['CompositeInterface']
ok_tab = ('def sgn (μ ν : Fin 4) : ℝ := if (μ = 1 ∧ ν = 3) ∨ (μ = 2 ∧ ν = 2) then -1 else 1' in CD
          and 'def phiW : W 3 := fun μ ν => if μ = ν then (if μ = 2 then -1 else 1) else 0' in CD
          and 'toFun x := fun i => (![1, -1, 1] : Fin 3 → ℝ) i * x i' in KG
          and 'toFun x := fun i => (![1, -1, -1] : Fin 3 → ℝ) i * x i' in CD
          and 'def z3 : Fin 3 → ℝ := ![0, 0, 1]' in CD and 'def xplus : Fin 3 → ℝ := ![1, 0, 0]' in CD)
chk('S0.tabs', 'landed sgn, phiW, reflY = diag(1,-1,1), nflip = diag(1,-1,-1), z3, xplus match the transcription', ok_tab,
    'source')
chk('S0.nat', 'NativeGate fields: frame on the corners, posFwd and posInv on product states INTO maxCone, relT, relC '
    '(two-sided positivity is relative to maxCone, not to any pair cone)',
    'posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω' in CD
    and 'posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone Ω' in CD
    and 'relT : ∀ ω, actT N (G (actT N ω)) = G ω' in CD
    and 'relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)' in CD, 'source')
chk('S0.ball', 'ball3 = {v | v0^2 + v1^2 + v2^2 <= 1} and eball d = {x | sum x_j^2 <= 1}: the same set at d = 3 '
    '(Fin.sum_univ_three)', 'def ball3 : Set (Fin 3 → ℝ) := {v | v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2 ≤ 1}' in SRC['KInfFoundations']
    and 'def eball (d : ℕ) : Set (Fin d → ℝ) := {x | ∑ j, x j ^ 2 ≤ 1}' in SRC['TransitiveBody'], 'source')
chk('S0.comp', 'ball3MaxComposite = maxComposite ball3_isCompact ball3_isCompact (body: maxBody of the coordinate model) '
    'and ball3MinComposite = minComposite (body: the convex hull of the products)',
    'def ball3MaxComposite : Composite ball3 ball3 (Carrier 3 3) :=\n  maxComposite ball3_isCompact ball3_isCompact' in CI
    and 'def ball3MinComposite : Composite ball3 ball3 (Carrier 3 3) :=\n  minComposite ball3_isCompact ball3_isCompact' in CI
    and 'toPreComposite := (modelData dA dB).maxPre ΩA ΩB' in CI, 'source')
chk('S0.jr', 'JointReversible G := PreservesBody P.Omega G, and PreservesBody asks g x and g.symm x in the body: a '
    'predicate, asserted of no pair gate at L', 'abbrev JointReversible (G : Set (V ≃ᵃ[ℝ] V)) : Prop := PreservesBody P.Ω G'
    in CI and 'def PreservesBody (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop :=\n  ∀ g ∈ G, ∀ x ∈ Ω, g x ∈ Ω ∧ g.symm x ∈ Ω'
    in SRC['OrbitGeneration'], 'source')
chk('S0.opd', 'OpDatum: tau maps each stage preparation into the completed body (mem_body); no DirectedStages value for '
    'a pair of systems is declared at L (only badD, bitTower, midD)',
    'mem_body : ∀ x, τ x ∈ body D' in SRC['CompletionAction']
    and sorted(set(re.findall(r'^(?:noncomputable )?def (\w+) : DirectedStages', '\n'.join(SRC.values()), re.M)))
    == ['badD', 'bitTower', 'midD'], 'source',
    str(sorted(set(re.findall(r'^(?:noncomputable )?def (\w+) : DirectedStages', '\n'.join(SRC.values()), re.M)))))

# ===============================================================================================================
section('S1  the native-gate premises for the four gates (same NOT nflip, axis z3)')
corner = {0: z3, 1: [0, 0, -1]}
for g, (G, Gi) in GATES.items():
    ok_frame = all(G(prodState(corner[a], corner[b])) == prodState(corner[a], corner[(a + b) % 2])
                   for a in (0, 1) for b in (0, 1))
    ok_relT = mzero(actT(nflip, G(actT(nflip, W))) - G(W))
    ok_relC = mzero(actC(nflip, G(actC(nflip, W))) - actT(nflip, G(W)))
    ok_inv = mzero(Gi(G(W)) - W) and mzero(G(Gi(W)) - W)
    chk(f'K1.{g}', f'{g}: frame on the four corner pairs, relT and relC with nflip, two-sided inverse',
        ok_frame and ok_relT and ok_relC and ok_inv, 'identity', f'frame {ok_frame}, relT {ok_relT}, relC {ok_relC}')
# positivity reductions: every image of a product is actT reflY^(e) cnot (prodState x y') with y' = y or reflY y
yR = list(reflY * sp.Matrix(ys))
red = {
    'cnot': (cnot(prodState(xs, ys)), cnot(prodState(xs, ys))),
    'g_D': (actT(reflY, cnot(prodState(xs, ys))), cnot(prodState(xs, yR))),
    'g_pre': (cnot(prodState(xs, yR)), actT(reflY, cnot(prodState(xs, ys)))),
    'g_Tw': (actT(reflY, cnot(prodState(xs, yR))), actT(reflY, cnot(prodState(xs, yR)))),
}
ok_pos = all(mzero(GATES[g][0](prodState(xs, ys)) - red[g][0]) and mzero(GATES[g][1](prodState(xs, ys)) - red[g][1])
             for g in GATES)
chk('K1.pos', 'forward and inverse images of prodState x y under the four gates are cnot (prodState x y\'), y\' in {y, '
    'reflY y}, possibly followed by actT reflY (symbolic); with the landed cnot_prodState_mem_maxCone, |reflY y| = |y| '
    'and the actT reflY-invariance of maxCone (next check) every gate has posFwd and posInv', ok_pos, 'identity')
Rg = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'R{i}{j}', real=True))
rb = homMap(reflY) * sp.Matrix(b4)
chk('K1.max', 'pairVal a b (actT R w) = pairVal a (homMap R^T b) w (symbolic R), and homMap reflY keeps b0 and the '
    'Lorentz form: actT reflY maps maxCone onto maxCone',
    z(pairVal(a4, b4, actT(Rg, W)) - pairVal(a4, list(homMap(Rg.T) * sp.Matrix(b4)), W))
    and z(rb[0] - b4[0]) and z(rb[0] ** 2 - rb[1] ** 2 - rb[2] ** 2 - rb[3] ** 2
                               - (b4[0] ** 2 - b4[1] ** 2 - b4[2] ** 2 - b4[3] ** 2))
    and z(sum(v ** 2 for v in yR) - sum(v ** 2 for v in ys)), 'identity')
pxz = prodState(xplus, z3)
img = {g: GATES[g][0](pxz) for g in GATES}
chk('K1.ent', 'Entangling: the images of the pure product (xplus, z3) are phiW (cnot, g_pre) and idW = actT reflY phiW '
    '(g_D, g_Tw); each has table rank 4, so none is a product state (rank 1); idW is extreme in the joint states '
    'because actT reflY is a linear involution of W 3 mapping maxCone onto itself and fixing the unit entry, and phiW '
    'is extreme (landed entangling_cnot)',
    img['cnot'] == phiW and img['g_pre'] == phiW and img['g_D'] == idW and img['g_Tw'] == idW
    and actT(reflY, phiW) == idW and phiW.rank() == 4 and idW.rank() == 4 and actT(reflY, W)[0, 0] == W[0, 0], 'witness')
RH = sp.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
bad = lambda w: actT(RH, cnot(w))
chk('K1.cc', 'countercontrol: actT R_H . cnot (R_H swaps the first and third axes) fails the frame (it is detected)',
    not all(bad(prodState(corner[a], corner[b])) == prodState(corner[a], corner[(a + b) % 2])
            for a in (0, 1) for b in (0, 1)), 'countercontrol')

# ===============================================================================================================
section('S2  admissible invariant cones of the four gates')
chk('S2.no', 'g_D and g_pre: two applications take the product state (xplus, z3) to chainW, outside maxCone (value -1/2 '
    'at the sharp effects of -e1, -e3): no cone containing the products and inside maxCone is invariant',
    GATES['g_D'][0](GATES['g_D'][0](pxz)) == chainW and GATES['g_pre'][0](GATES['g_pre'][0](pxz)) == chainW
    and pairVal(SHARP_NEGX, SHARP_NEGZ, chainW) == Q(-1, 2), 'witness')
CNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
ptr = lambda M: sp.Matrix(4, 4, lambda r, c: M[2 * (r // 2) + (c % 2), 2 * (c // 2) + (r % 2)])
chk('S2.yes', 'cnot and g_Tw have admissible invariant cones: pauliW (cnot w) = CNOT pauliW(w) CNOT^dagger (cnot Q3 = '
    'Q3) and pauliW (actT reflY w) is the partial transpose of pauliW(w) (twin = actT reflY Q3, g_Tw twin = twin), '
    'symbolic', mzero(pauliW(cnot(W)) - CNOT * pauliW(W) * CNOT.H) and mzero(pauliW(actT(reflY, W)) - ptr(pauliW(W))),
    'identity')
chk('S2.cc', 'countercontrol: cnot applied twice returns the product state (it does not leave maxCone)',
    cnot(cnot(pxz)) == pxz, 'countercontrol')

# ===============================================================================================================
section('S3  the certified-premise checklist (INDEPENDENT): each certified premise bearing on (K, N), per model')
singlet = sp.Matrix([0, 1, -1, 0])
q_phi = is_psd(pauliW(phiW))
q_idW_neg = (singlet.H * pauliW(idW) * singlet)[0, 0] == -1
idW_in_max = z(pairVal(a4, b4, idW) - sum(a4[i] * b4[i] for i in R4))
chain_out = pairVal(SHARP_NEGX, SHARP_NEGZ, cnot(idW)) == Q(-1, 2)
chk('S3.vio', 'the violations: M_max -- idW in maxCone (pairVal a b idW = a.b >= a0 b0 - |a||b| >= 0) and cnot idW = '
    'chainW outside it; M_D13 -- g_D (xplus, z3) = idW outside Q3 (singlet value -1) with (xplus, z3) in Q3',
    idW_in_max and cnot(idW) == chainW and chain_out and q_idW_neg and img['g_D'] == idW
    and is_psd(pauliW(pxz)), 'witness')
CHECKLIST = [
    ('IsNot (eball 3) z3 nflip', 'K isNot_nflip', 'K isNot_nflip'),
    ('NativeGate (eball 3) z3 nflip N: frame, posFwd, posInv into maxCone, relT, relC', 'K nativeGate_cnot',
     'X K1.g_D, K1.pos, K1.max + K cnot_prodState_mem_maxCone'),
    ('CtrlGate (eball 3) z3 nflip N', 'K ctrlGate_of_nativeGate', 'from NativeGate (K ctrlGate_of_nativeGate)'),
    ('GateRel nflip N (relT, relC)', 'K gateRel_cnot', 'X K1.g_D'),
    ('Entangling (eball 3) N', 'K entangling_cnot', 'X+W K1.ent'),
    ('NativeGateOf / EntanglingOf for an available family whose cone is maxCone (EFF-1)',
     'W: NativeGate + cone equality (K maxConeOf_avail_eq)', 'W: same'),
    ('one common NOT on both copies (K-inf-Copy, open premise)', 'nflip on both copies', 'nflip on both copies'),
    ('CandidateCone K: products in K, K in maxCone', 'K prodState_mem_maxCone; maxCone itself',
     'W: D5, D6, landed D.W (Q3 in maxCone)'),
    ('K is a convex cone, closed', 'W (landed M_max.2W)', 'W (PSD cone)'),
    ('the normalized slice of K is a COMP-1 Composite body in the coordinate model',
     'K ball3MaxComposite (S0.comp, S0.ball)', 'W: PreComposite fields from CandidateCone and convexity; lt as in the '
                                               'landed minComposite/maxComposite (result.md Q2)'),
    ('no candidate cone is invariant under both cnot and actT reflY (K2-GUARD-1)', 'consistent: maxCone is not cnot-'
     'invariant (S3.vio)', 'consistent: Q3 is not actT reflY-invariant (b1_models W2)'),
    ('OPACT-1: an operation datum with an inverse datum preserves the completed body', 'vacuous: no pair directed '
     'system or datum at L (S0.opd)', 'vacuous (S0.opd)'),
    ('the other hypotheses of the four-copy theorem (hcls, hadm, hcl, H) -- design level, not certified',
     'landed M_max (KT4-PREM-1 Q1-MAX, replayed)', 'landed M_D (Q1-MAP, replayed)'),
]
for i, (prem, mmax, md) in enumerate(CHECKLIST, 1):
    print(f'  checklist {i:2d}. {prem}\n      M_max: {mmax}\n      M_D13: {md}')
chk('S3.list', 'the checklist covers every landed declaration of S0 that constrains a pair gate or a pair cone',
    len(CHECKLIST) == 13 and all(LOCS[k] for k in ('IsNot', 'NativeGate', 'CtrlGate', 'GateRel', 'Entangling',
                                                   'NativeGateOf', 'EntanglingOf', 'CandidateCone', 'Composite',
                                                   'no_candidateCone_cnot_reflY', 'OpDatum')), 'source')

# ===============================================================================================================
section('S4  candidate sources (B2): derived, restated or refuted')
# product-only P-ACT2: a datum on a pair system whose preparations are product states must send prodState xplus z3
# into the closed convex hull of the products (the SEP slice); the gate sends it to phiW, which F separates.
F = sp.diag(1, -1, 1, -1)
xv, yv = sp.Matrix(xs), sp.Matrix(ys)
Dp = sp.diag(1, -1, 1)
chk('S4.pact', 'P-ACT2 on a product-only pair system is impossible for cnot: ipW F (prodState x y) = |x - D y|^2/2 + '
    '(1-|x|^2)/2 + (1-|y|^2)/2 >= 0 on products (symbolic) and ipW F phiW = -2 with phiW = cnot (prodState xplus z3)',
    z(ipW(F, prodState(xs, ys)) - ((xv - Dp * yv).dot(xv - Dp * yv) / 2 + (1 - xv.dot(xv)) / 2 + (1 - yv.dot(yv)) / 2))
    and ipW(F, phiW) == -2 and cnot(pxz) == phiW, 'witness')
chk('S4.jr', 'JR (PreservesBody of the normalized slice under {N}) gives hgate: N-CLASS gates fix the unit entry '
    '(symbolic, cnot and actC/actT of orthogonal maps), so N (c w) = c N(w) carries the slice to the cone',
    all(z(GATES[g][0](W)[0, 0] - W[0, 0]) for g in GATES), 'identity')
# GT-COMP: the transported product data satisfy COMP-1's evaluation law (b1_steps D6); prod_mem and prodEff_effect for
# them are SECT's two halves (written; recorded in RESULT)
chk('S4.gt', 'GT-COMP: for the four gates, ipW (N (a b^T)) (N (prodState x y)) = (a.x^)(b.y^), symbolic (transported '
    'evaluation law)', all(z(ipW(GATES[g][0](sp.Matrix(a4) * sp.Matrix(b4).T), GATES[g][0](prodState(xs, ys)))
                             - (sp.Matrix(a4).T * hom(xs))[0, 0] * (sp.Matrix(b4).T * hom(ys))[0, 0]) for g in GATES),
    'identity')

# ===============================================================================================================
section('S5  restricted idle extension (B3)')
M1, M2 = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'M{i}{j}', real=True)), sp.Matrix(3, 3, lambda i, j: sp.Symbol(f'N{i}{j}', real=True))
chk('S5.prod', 'product-level idle extension is an identity of the product data: actC M (actT M\' (prodState x y)) = '
    'prodState (M x) (M\' y), symbolic (it holds in every model and says nothing about entangled tables)',
    mzero(actC(M1, actT(M2, prodState(xs, ys))) - prodState(list(M1 * xv), list(M2 * yv))), 'identity')
chk('S5.gate', 'gate-factor idle extension of the post-local reflection: actT reflY sends phiW (in Q3) to idW (not in '
    'Q3), and the landed chain cnot . actT reflY . cnot takes (xplus, z3) to chainW (K2-GUARD-1)',
    q_phi and actT(reflY, phiW) == idW and q_idW_neg and cnot(actT(reflY, cnot(pxz))) == chainW, 'witness')
m1, m2 = sp.symbols('m1 m2', real=True)
c1, s1 = (1 - m1 ** 2) / (1 + m1 ** 2), 2 * m1 / (1 + m1 ** 2)
c2, s2 = (1 - m2 ** 2) / (1 + m2 ** 2), 2 * m2 / (1 + m2 ** 2)
RZ = sp.Matrix([[c1, -s1, 0], [s1, c1, 0], [0, 0, 1]])
RX = sp.Matrix([[1, 0, 0], [0, c2, -s2], [0, s2, c2]])
chk('S5.comm', 'the commutant of cnot: cnot . actC Rz = actC Rz . cnot and cnot . actT Rx = actT Rx . cnot (symbolic '
    'angles); with the Bell state they give the links: actC Rz (actT Rx phiW) = actC (Rz Rx) phiW',
    mzero(cnot(actC(RZ, W)) - actC(RZ, cnot(W))) and mzero(cnot(actT(RX, W)) - actT(RX, cnot(W)))
    and mzero(actC(RZ, actT(RX, phiW)) - actC(RZ * RX, phiW)), 'identity')
RXc = RX.subs(m2, Q(1, 2))
chk('S5.cc', 'countercontrol: a control-side rotation about the first axis does not commute with cnot (sample angle)',
    not mzero(cnot(actC(RXc, W)) - actC(RXc, cnot(W))), 'countercontrol')

# ===============================================================================================================
print()
kinds = ('identity', 'witness', 'enumerate', 'source', 'countercontrol')
print('kinds: ' + ', '.join(f"{k} {sum(1 for c in ORDER if CHECKS[c][0] == k)}" for k in kinds), flush=True)
failed = [c for c in ORDER if not CHECKS[c][1]]
if failed:
    print(f"b2_sources: NO VERDICT -- {len(failed)} of {len(ORDER)} checks failed: {', '.join(failed)}")
    sys.exit(1)
k1_all = all(CHECKS[f'K1.{g}'][1] for g in GATES) and CHECKS['K1.pos'][1] and CHECKS['K1.ent'][1]
print(f"VERDICT B2-K1: the native-gate premises (frame, relT, relC, two-sided positivity on maxCone, entangling, same NOT) "
      f"hold for all four gates {list(GATES)}: {k1_all}; two of them (g_D, g_pre) have no admissible invariant cone "
      f"(S2.no): {CHECKS['S2.no'][1]}")
print('VERDICT B2-INDEP: M_max = (maxCone, cnot) and M_D13 = (Q3, g_D) satisfy each of the '
      f'{len(CHECKLIST)} checklist premises (S3) and violate hgate (S3.vio)')
print('VERDICT B2-PACT: a product-only pair system admits no operation datum for cnot (S4.pact); JR gives hgate by '
      'scaling (S4.jr); GT-COMP\'s evaluation law holds for the transported data (S4.gt)')
print('VERDICT B3: product-level idle extension is an identity (S5.prod); the post-local reflection factor leaves Q3 '
      '(S5.gate); the commutant extension yields the links only by assuming rotation invariance of K (S5.comm)')
print(f'b2_sources: OK -- {len(ORDER)} checks')
