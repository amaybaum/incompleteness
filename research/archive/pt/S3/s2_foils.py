#!/usr/bin/env python3
"""S3 node S3.2 (pair-level principles) -- the single-pair chart obstruction and the two uniform foils.

Run: python3 -I -B s2_foils.py <OIB>   (OIB = ../base/verification/lean-mathlib/OIBridge, read-only)

DECISION RULES (fixed before the first run; rules, not expected numbers):
  R1. One PASS/FAIL line per check. [identity] = exact sympy polynomial identity in the named symbols;
      [witness] = exact rational value or exact matrix equality at stated tables; [enumerate] = exhaustive over a
      named finite set; [countercontrol] = a mutated object that must fail the property its sibling check asserts.
  R2. A VERDICT line prints only if every check (countercontrols included) passes; otherwise
      'S2-FOILS: FAILED -- <ids>' and exit 1.
  R3. Exact arithmetic only. No floating point, randomness or timing in stdout.
  R4. A route-refuting model is reported only with every membership it uses either checked here exactly or
      reduced, in a NOTE [written], to identities checked here and to named standard facts.
  R5. The IE1-failure search for K_gen* scans a fixed finite list (the 24 octahedral rotations on either token,
      the 36 ordered pairs of axis points); it reports the first witness found in list order, or FAIL if none.

Objects: Q3 = {w : pauliW w PSD}; twin = actT reflY Q3; SEP = cone of products prodState x y (x, y in the ball);
K_gen = SEP + cnot SEP (thread A's native closure, thread C's K_c); K_gen* = dualW K_gen = maxCone n cnot(maxCone).
"""
import re
import sys
from itertools import permutations, product
from pathlib import Path

import sympy as sp

Q = sp.Rational
iu = sp.I
R4 = range(4)
CHECKS = []


def chk(cid, name, ok, kind, detail=''):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}" + (f" -- {detail}" if detail else ''), flush=True)


def note(cid, text):
    print(f"NOTE [written] {cid}  -- {text}", flush=True)


def section(t):
    print()
    print(f"== {t}", flush=True)


def ex(v):
    return sp.expand(v)


def zero(v):
    return ex(v) == 0


def mzero(M):
    return all(ex(v) == 0 for v in M)


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


def ipW(E, X):
    return sum(E[m, n] * X[m, n] for m in R4 for n in R4)


def fourVal(X, Y, E, F):
    return sum(X[a, b] * Y[c, d] * E[a, c] * F[b, d] for a, b, c, d in product(R4, repeat=4))


def g2(e, f, L, Lp):
    return sum(e[a, b] * f[c, d] * L[a, c] * Lp[b, d] for a, b, c, d in product(R4, repeat=4))


def symtab(nm):
    return sp.Matrix(4, 4, lambda m, n: sp.Symbol(f'{nm}{m}{n}', real=True))


S = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -iu], [iu, 0]]), sp.Matrix([[1, 0], [0, -1]])]
SS = [[sp.kronecker_product(S[m], S[n]) for n in R4] for m in R4]
CNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])


def pauliW(w):
    out = sp.zeros(4, 4)
    for m in R4:
        for n in R4:
            if w[m, n] != 0:
                out += w[m, n] * SS[m][n]
    return out / 4


def dag(M):
    return M.conjugate().T


def rho1(x):
    return (S[0] + sum((x[i] * S[i + 1] for i in range(3)), sp.zeros(2, 2))) / 2


def coords(M):
    """the table w with pauliW w = M (Hermitian 4x4), via tr(s_m (x) s_n M)."""
    return sp.Matrix(4, 4, lambda m, n: ex((SS[m][n] * M).trace()))


reflY = sp.diag(1, -1, 1)
phiW = sp.diag(1, 1, -1, 1)
idW = sp.eye(4)
sing4 = sp.diag(1, -1, -1, -1)
E00 = sp.zeros(4, 4)
E00[0, 0] = 1
xplus, z3 = [1, 0, 0], [0, 0, 1]
Lp = actT(reflY, sing4)

# ================================================================================================================
section('S0  transcription (read-only)')
OIB = Path(sys.argv[1]).resolve()
CD = (OIB / 'CompositeDimension.lean').read_text(encoding='utf-8')
msg = re.search(r'^def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) '
                r'then -1 else 1$', CD, re.M)
neg_src = {(int(msg.group(1)), int(msg.group(2))), (int(msg.group(3)), int(msg.group(4)))} if msg else None
chk('S0.sgn', 'landed sgn is -1 exactly at (1,3) and (2,2)', neg_src == NEG, 'source')
chk('S0.phiW', 'landed phiW = diag(1,1,-1,1)',
    'def phiW : W 3 := fun μ ν => if μ = ν then (if μ = 2 then -1 else 1) else 0' in CD, 'source')
W, Wp = symtab('w'), symtab('v')
chk('D1', 'pauliW (cnot w) = CNOT pauliW(w) CNOT^dagger, symbolic w (cnot is conjugation by CNOT)',
    mzero(pauliW(cnot(W)) - CNOT * pauliW(W) * dag(CNOT)), 'identity')
chk('D2', 'cnot is an ipW-orthogonal involution: cnot(cnot w) = w and ipW(cnot w)(cnot v) = ipW w v, symbolic',
    mzero(cnot(cnot(W)) - W) and zero(ipW(cnot(W), cnot(Wp)) - ipW(W, Wp)), 'identity')
xs = [sp.Symbol(f'x{i}', real=True) for i in range(3)]
ys = [sp.Symbol(f'y{i}', real=True) for i in range(3)]
chk('D3', 'pauliW (prodState x y) = rho(x) (x) rho(y), symbolic x, y', mzero(
    pauliW(prodState(xs, ys)) - sp.kronecker_product(rho1(xs), rho1(ys))), 'identity')
chk('D4', 'ipW E X = 4 tr(pauliW E pauliW X), symbolic (the Euclidean pairing is the trace pairing)',
    zero(ipW(W, Wp) - 4 * (pauliW(W) * pauliW(Wp)).trace()), 'identity')
note('D.W', 'by D4 and the self-duality of the PSD cone (landed JordanClassification psd_iff_trace_nonneg, for complex '
     'matrices; Mathlib PosSemidef), dualW Q3 = Q3. By D3 every product lies in Q3; by D1 cnot maps Q3 onto Q3. '
     'Hence K_gen <= Q3 = dualW Q3 <= dualW K_gen = K_gen*.')

# ================================================================================================================
section('S1  the single-pair chart obstruction (per-pair principles cannot exclude the mixed assignment)')
chk('C1', 'actT reflY is ipW-orthogonal and an involution, symbolic',
    zero(ipW(actT(reflY, W), actT(reflY, Wp)) - ipW(W, Wp)) and mzero(actT(reflY, actT(reflY, W)) - W), 'identity')
chk('C2', 'actT reflY (prodState x y) = prodState x (reflY y), symbolic: it maps SEP onto SEP',
    mzero(actT(reflY, prodState(xs, ys)) - prodState(xs, list(reflY * sp.Matrix(ys)))), 'identity')
a_s = [sp.Symbol(f'a{i}', real=True) for i in R4]
b_s = [sp.Symbol(f'b{i}', real=True) for i in R4]
chk('C3', 'a^T (actT reflY w) b = a^T w (homMap reflY b), symbolic, and homMap reflY preserves the Lorentz form: '
    'actT reflY maps maxCone onto maxCone',
    zero((sp.Matrix(a_s).T * actT(reflY, W) * sp.Matrix(b_s))[0, 0]
         - (sp.Matrix(a_s).T * W * (homMap(reflY) * sp.Matrix(b_s)))[0, 0])
    and zero(((homMap(reflY) * sp.Matrix(b_s)).T * sp.diag(1, -1, -1, -1) * (homMap(reflY) * sp.Matrix(b_s))
              - sp.Matrix(b_s).T * sp.diag(1, -1, -1, -1) * sp.Matrix(b_s))[0, 0]), 'identity')
cnotTw = (lambda w: actT(reflY, cnot(actT(reflY, w))))
chk('C4', 'cnotTw = actT reflY . cnot . actT reflY is the N-CLASS gate with locals (I, reflY, I, reflY), symbolic',
    mzero(cnotTw(W) - actC(sp.eye(3), actT(reflY, cnot(actC(sp.eye(3), actT(reflY, W)))))), 'identity')
chk('C5', 'ipW F (actT reflY w) = ipW (actT reflY F) w, symbolic: dualW twin = actT reflY (dualW Q3) = twin',
    zero(ipW(W, actT(reflY, Wp)) - ipW(actT(reflY, W), Wp)), 'identity')
note('C.W', 'let P be any predicate of the data of ONE pair (its cone, its gate, its four locals) that is invariant '
     'under transport by the ipW-orthogonal, SEP- and maxCone-preserving involution actT reflY (cone K -> its image, '
     'gate N -> actT reflY . N . actT reflY, locals transformed by the chart rule). Self-duality K = dualW K, its two '
     'halves, homogeneity, symmetric-cone (Jordan) structure, closedness, admissibility and gate invariance are all '
     'such predicates (C1-C5). Then P(Q3, cnot, I, I, I, I) iff P(twin, cnotTw, I, reflY, I, reflY). The model '
     'M_tok = (Q3, Q3, Q3, twin) with gates (cnot, cnot, cnot, cnotTw) therefore satisfies every conjunction of such '
     'predicates that the quantum data M_Q satisfy, while FCC fails there at -1/8 (s1 A3). No conjunction of '
     'chart-invariant single-pair predicates implies FCC. This complements AUDIT-C\'s narrowed B3 (three-pair '
     'conditions on cones and gate maps): for one pair, conditions may read the locals as well.')

# ================================================================================================================
section('S2  uniform K_gen: K_gen <= K_gen* (one half of self-duality), and FCC fails')
E0 = sp.zeros(4, 4)
E0[0, 0], E0[1, 3], E0[2, 2] = 1, 1, -1
x1, x2, x3 = xs
y1, y2, y3 = ys
chk('G1', 'hom x^T E0 hom y = 1 + x1 y3 - x2 y2, symbolic (x = (x1, x2, x3), y = (y1, y2, y3))',
    zero((hom(xs).T * E0 * hom(ys))[0, 0] - (1 + x1 * y3 - x2 * y2)), 'identity')
chk('G2', 'Lagrange: (x1^2 + x2^2)(y3^2 + y2^2) - (x1 y3 - x2 y2)^2 = (x1 y2 + x2 y3)^2, symbolic',
    zero((x1 ** 2 + x2 ** 2) * (y3 ** 2 + y2 ** 2) - (x1 * y3 - x2 * y2) ** 2 - (x1 * y2 + x2 * y3) ** 2), 'identity')
chk('G3', 'cnot E0 = E0', cnot(E0) == E0, 'witness')
note('G.W', 'by G1, G2 |x1 y3 - x2 y2| <= |x||y| <= 1 on the ball, so E0 is nonnegative on every product (E0 in '
     'dualW SEP); by D2 and G3, ipW E0 (cnot p) = ipW (cnot E0) p = ipW E0 p >= 0; hence E0 lies in K_gen*.')
psi = sp.Matrix([1, -1, -1, -1]) / 2
G = coords(psi * psi.T)
chk('G4', 'pauliW G = psi psi^T for psi = (1,-1,-1,-1)/2 (G in Q3, rank one) and ipW E0 G = -1 (E0 not in Q3)',
    mzero(pauliW(G) - psi * psi.T) and ipW(E0, G) == -1 and (psi.T * psi)[0, 0] == 1, 'witness', f'G = {G.tolist()}')
vg = fourVal(phiW, phiW, E0, G)
chk('G5', 'famI for uniform K_gen: fourVal phiW phiW E0 G = -1 (phiW = cnot(prodState xplus z3) in K_gen; E0, G in '
    'K_gen*)', vg == -1 and cnot(prodState(xplus, z3)) == phiW, 'witness', f'value {vg}')
chk('G5c', 'countercontrol: with E00 in place of E0 the value is > 0', fourVal(phiW, phiW, E00, G) > 0,
    'countercontrol', f'value {fourVal(phiW, phiW, E00, G)}')
note('G5.W', 'uniform K_gen with cnot gates and identity locals satisfies hcls (cnot is its own N-CLASS form), hadm '
     '(products in SEP; K_gen <= Q3 <= maxCone; a convex cone), hcl (thread A, audited: K_gen closed) and hgate '
     '(cnot K_gen = K_gen by D2); it satisfies K_gen <= K_gen* (D.W) and fails FCC (G5). So "uniformity + K <= '
     'dualW K + the pair hypotheses" does not imply FCC: route refuted (this is thread C\'s K7, recomputed here '
     'with independent code).')

# ================================================================================================================
section('S3  uniform K_gen* (the dual foil): dualW(K_gen*) <= K_gen* (the other half), and FCC fails')
vgs = fourVal(E0, G, phiW, phiW)
chk('H1', 'famI for uniform K_gen*: fourVal E0 G phiW phiW = -1 (E0 in K_gen* and G in Q3 <= K_gen* as STATES; phiW in '
    'K_gen <= dualW(K_gen*) as effects)', vgs == -1, 'witness', f'value {vgs}')
chk('H1c', 'countercontrol: with E00 in place of E0 the value is > 0', fourVal(E00, G, phiW, phiW) > 0,
    'countercontrol', f'value {fourVal(E00, G, phiW, phiW)}')
chk('H2', 'phiW G phiW^T = G (G is invariant under the full reflection; so fourVal X G phiW phiW = ipW X G)',
    phiW * G * phiW.T == G and zero(fourVal(W, G, phiW, phiW) - ipW(W, G)), 'identity')
note('H.W', 'K_gen* = dualW K_gen is a closed convex cone; it contains Q3 (D.W) hence every product; it lies in '
     'dualW SEP = maxCone since SEP <= K_gen; cnot maps it onto itself (D2 and cnot K_gen = K_gen). So uniform K_gen* '
     'with cnot gates and identity locals satisfies hcls, hadm, hcl, hgate. dualW(K_gen*) = closure(K_gen) <= Q3 <= '
     'K_gen* (Q3 closed): K_gen* satisfies the half "every effect is a state". FCC fails (H1). So "uniformity + '
     'dualW K <= K + the pair hypotheses" does not imply FCC: route refuted. NEW foil (from above).')


def octahedral():
    out = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            M = sp.zeros(3, 3)
            for i in range(3):
                M[i, perm[i]] = signs[i]
            if M.det() == 1:
                out.append(M)
    return out


OCT = octahedral()
chk('H3', 'the octahedral rotation group has 24 elements, each a rotation (orthogonal, det 1)',
    len(OCT) == 24 and all(M.T * M == sp.eye(3) and M.det() == 1 for M in OCT), 'enumerate')
AX = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
found = None
for side in ('C', 'T'):
    for k, R in enumerate(OCT):
        wR = actC(R, E0) if side == 'C' else actT(R, E0)
        cw = cnot(wR)
        for xa in AX:
            for ya in AX:
                val = (hom(xa).T * cw * hom(ya))[0, 0]
                if val < 0:
                    found = (side, k, R, xa, ya, val)
                    break
            if found:
                break
        if found:
            break
    if found:
        break
if found:
    side, k, R, xa, ya, val = found
    chk('H4', 'IE1 fails for K_gen*: for an octahedral rotation R, act R E0 (E0 in K_gen*) pairs negatively with the '
        'K_gen element cnot(prodState x y): ipW (act R E0) (cnot p) = hom x^T cnot(act R E0) hom y < 0',
        val < 0 and zero(ipW(actC(R, E0) if side == 'C' else actT(R, E0), cnot(prodState(xa, ya))) - val), 'witness',
        f'side {side}, R = {R.tolist()}, x = {xa}, y = {ya}, value {val}')
else:
    chk('H4', 'IE1 fails for K_gen* (no witness in the scanned list)', False, 'witness')
chk('H4c', 'countercontrol: the identity rotation gives no negative value on the scanned list (E0 itself is in K_gen*)',
    all((hom(xa).T * cnot(E0) * hom(ya))[0, 0] >= 0 for xa in AX for ya in AX), 'countercontrol')

# ================================================================================================================
section('S4  incomparability: state-state cross positivity, the effect-state half, and FCC')
v_max = fourVal(idW, idW, phiW, Lp)
chk('M1', 'uniform maxCone: fourVal idW idW phiW L\' = ipW phiW L\' = -2 with idW, phiW, L\' in maxCone (states of four '
    'pairs whose A- and B-products have negative overlap)', v_max == -2 and zero(fourVal(idW, idW, W, Wp) - ipW(W, Wp)),
    'witness', f'value {v_max}')
chk('M2', 'membership in maxCone: a^T idW b = a.b, a^T L\' b = a0 b0 - a1 b1 + a2 b2 - a3 b3, a^T phiW b = '
    'a0 b0 + a1 b1 - a2 b2 + a3 b3, symbolic (each >= 0 on Lor x Lor by Cauchy-Schwarz on the tails)',
    zero((sp.Matrix(a_s).T * idW * sp.Matrix(b_s))[0, 0] - sum(a_s[i] * b_s[i] for i in R4))
    and zero((sp.Matrix(a_s).T * Lp * sp.Matrix(b_s))[0, 0]
             - (a_s[0] * b_s[0] - a_s[1] * b_s[1] + a_s[2] * b_s[2] - a_s[3] * b_s[3]))
    and zero((sp.Matrix(a_s).T * phiW * sp.Matrix(b_s))[0, 0]
             - (a_s[0] * b_s[0] + a_s[1] * b_s[1] - a_s[2] * b_s[2] + a_s[3] * b_s[3])), 'identity')
note('M.W', 'uniform maxCone satisfies FCC (landed KT4-PREM-1 F4-F6 and note F.max: the dual of maxCone is SEP and '
     'L is self-dual) and the half dualW K <= K (dualW maxCone = SEP <= maxCone), but no four-token cone containing '
     'both groupings\' products has nonnegative overlaps (M1). So state-state cross positivity (SSCP) is not implied '
     'by FCC; uniform K_gen (S2) satisfies SSCP (K_gen <= Q3 and FCC for uniform Q3 with Q3 = dualW Q3) and fails '
     'FCC. SSCP and FCC are incomparable on admissible closed cones.')
x0s = [sp.Symbol(f'p{i}', real=True) for i in range(3)]
x1s = [sp.Symbol(f'q{i}', real=True) for i in range(3)]
x2s = [sp.Symbol(f'r{i}', real=True) for i in range(3)]
x3s = [sp.Symbol(f's{i}', real=True) for i in range(3)]
Es, Fs = symtab('E'), symtab('F')
chk('M3', 'fourVal (prodState x0 x1) (prodState x2 x3) E F = ipW E (prodState x0 x2) * ipW F (prodState x1 x3), and the '
    'famII analogue, symbolic (FCC for uniform SEP: both factors >= 0 for E, F in dualW SEP)',
    zero(fourVal(prodState(x0s, x1s), prodState(x2s, x3s), Es, Fs)
         - ipW(Es, prodState(x0s, x2s)) * ipW(Fs, prodState(x1s, x3s)))
    and zero(g2(Es, Fs, prodState(x0s, x2s), prodState(x1s, x3s))
             - ipW(Es, prodState(x0s, x1s)) * ipW(Fs, prodState(x2s, x3s))), 'identity')
chk('M4', 'idW is not in SEP: ipW sing4 idW = -2 with sing4 in maxCone = dualW SEP (s1 I3); idW in maxCone (M2)',
    ipW(sing4, idW) == -2, 'witness')
note('M4.W', 'uniform SEP satisfies FCC (M3, bilinear extension over the generators) and fails "dualW K <= K" (M4). '
     'The M_tok cones satisfy "dualW K <= K" at every pair (Q3, twin self-dual) and fail FCC (s1 A3). So the half '
     '"every effect is a state" and FCC are incomparable on admissible closed cones. SSCP together with it implies '
     'FCC directly: for E in dualW K02 <= K02 and F in dualW K13 <= K13, famI is the overlap of an A-product with the '
     'B-product prodB E F (s1 B2.7).')

# ================================================================================================================
print()
failed = [c[0] for c in CHECKS if not c[2]]
print('kinds: ' + ', '.join(f"{k} {sum(1 for c in CHECKS if c[1] == k)}"
                            for k in ('identity', 'witness', 'enumerate', 'source', 'countercontrol')), flush=True)
if failed:
    print(f"S2-FOILS: FAILED -- {len(failed)} of {len(CHECKS)}: {', '.join(failed)}", flush=True)
    sys.exit(1)
print(f'VERDICT S2-FOILS-EXACT -- {len(CHECKS)} checks', flush=True)
