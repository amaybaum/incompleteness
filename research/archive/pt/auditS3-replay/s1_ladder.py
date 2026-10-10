#!/usr/bin/env python3
"""S3 node S3.1 -- associativity versus cross-pairing: exact checks for the ladder.

Run: python3 -I -B s1_ladder.py <OIB>   (OIB = ../base/verification/lean-mathlib/OIBridge, read-only)

DECISION RULES (fixed before the first run; rules, not expected numbers):
  R1. Every check prints one PASS/FAIL line. A check marked [identity] is an exact sympy polynomial identity in
      symbolic tables (universal over the symbols); [enumerate] is exhaustive over the finite set named;
      [witness] is an exact rational value at stated tables; [countercontrol] must give the opposite verdict
      to the favourable check it guards (it PASSES when the mutated object FAILS the property).
  R2. A VERDICT line prints only if every check, countercontrols included, passes. Otherwise the script prints
      'S1-LADDER: FAILED -- <ids>' and exits 1.
  R3. Exact arithmetic only (sympy Rationals / integers). No floating point, no randomness, no timing in stdout.
  R4. The transcription of the landed tables is checked against the landed Lean sources (read-only) before use.
  R5. Scope: identities hold for all real values of their symbols; witnesses hold at the stated tables only.

Conventions (as the landed probe kt4_prem1_probe.py; checked in S0): W 3 tables w[m][n], index 0 the unit;
hom x = (1, x); prodState x y = hom x hom y^T; ipW E X = sum E_mn X_mn; fourVal X Y E F = sum X_ab Y_cd E_ac F_bd
(X on tokens 01, Y on 23, E on 02, F on 13); famII value g2 e f L L' = sum e_ab f_cd L_ac L'_bd.
Four-token tables W4: Om[a][b][c][d], index a on token 0, b on 1, c on 2, d on 3.
  prodA X Y = (X_ab Y_cd), prodB L L' = (L_ac L'_bd); effA e f Om = sum e_ab f_cd Om_abcd;
  effB E F Om = sum E_ac F_bd Om_abcd; the W4 pairing <Om, Om'> = sum Om_abcd Om'_abcd.
"""
import re
import sys
from itertools import permutations, product
from pathlib import Path

import sympy as sp

Q = sp.Rational
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


# ---------------------------------------------------------------- landed tables (transcribed; checked in S0)
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


reflY = sp.diag(1, -1, 1)
phiW = sp.diag(1, 1, -1, 1)
idW = sp.eye(4)
sing4 = sp.diag(1, -1, -1, -1)
xplus, z3 = [1, 0, 0], [0, 0, 1]

# ---------------------------------------------------------------- four-token tables
IDX4 = list(product(R4, repeat=4))


def prodA(X, Y):
    return {(a, b, c, d): X[a, b] * Y[c, d] for a, b, c, d in IDX4}


def prodB(L, Lp):
    return {(a, b, c, d): L[a, c] * Lp[b, d] for a, b, c, d in IDX4}


def effA(e, f, Om):
    return sum(e[a, b] * f[c, d] * Om[(a, b, c, d)] for a, b, c, d in IDX4)


def effB(E, F, Om):
    return sum(E[a, c] * F[b, d] * Om[(a, b, c, d)] for a, b, c, d in IDX4)


def pair4(Om, Om2):
    return sum(Om[k] * Om2[k] for k in IDX4)


def sigma12(Om):
    return {(a, b, c, d): Om[(a, c, b, d)] for a, b, c, d in IDX4}


# ================================================================================================================
section('S0  transcription of the landed tables (read-only)')
OIB = Path(sys.argv[1]).resolve()
CD = (OIB / 'CompositeDimension.lean').read_text(encoding='utf-8')
KG = (OIB / 'K2Guard.lean').read_text(encoding='utf-8')
msg = re.search(r'^def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) '
                r'then -1 else 1$', CD, re.M)
neg_src = {(int(msg.group(1)), int(msg.group(2))), (int(msg.group(3)), int(msg.group(4)))} if msg else None
chk('S0.sgn', 'landed sgn is -1 exactly at (1,3) and (2,2)', neg_src == NEG, 'source')


def lean_table(nm):
    mm = re.search(rf'^def {nm} : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n){{4}})', CD, re.M)
    if not mm:
        return None
    T = [[None] * 4 for _ in R4]
    for a, b, v in re.findall(r'\|\s*(\d),\s*(\d)\s*=>\s*(\d)', mm.group(1)):
        T[int(a)][int(b)] = int(v)
    return T


chk('S0.pc', 'landed pc table', lean_table('pc') == PC, 'source')
chk('S0.pt', 'landed pt table', lean_table('pt') == PT, 'source')
chk('S0.phiW', 'landed phiW = diag(1,1,-1,1)',
    'def phiW : W 3 := fun μ ν => if μ = ν then (if μ = 2 then -1 else 1) else 0' in CD, 'source')
chk('S0.reflY', 'landed reflY = diag(1,-1,1)', 'toFun x := fun i => (![1, -1, 1] : Fin 3 → ℝ) i * x i' in KG,
    'source')
chk('S0.cnot', 'phiW = cnot (prodState xplus z3) (landed cnot_prodState_xplus_z3, recomputed)',
    cnot(prodState(xplus, z3)) == phiW, 'witness')

# ================================================================================================================
section('S1  token orders: which groupings a fixed order makes contiguous (exhaustive)')
PAIRINGS = {'A=01|23': ({0, 1}, {2, 3}), 'B=02|13': ({0, 2}, {1, 3}), 'C=03|12': ({0, 3}, {1, 2})}


def contiguous_pairings(order):
    first, second = set(order[:2]), set(order[2:])
    return sorted(k for k, (p, q) in PAIRINGS.items() if {frozenset(p), frozenset(q)} == {frozenset(first),
                                                                                           frozenset(second)})


orders = list(permutations(range(4)))
counts = [contiguous_pairings(o) for o in orders]
chk('L1', 'each of the 24 linear orders makes exactly one pairing contiguous (two adjacent blocks of two)',
    len(orders) == 24 and all(len(c) == 1 for c in counts), 'enumerate')
chk('L2', 'no linear order makes both A = 01|23 and B = 02|13 contiguous',
    not any(('A=01|23' in c and 'B=02|13' in c) for c in counts), 'enumerate',
    f"orders realizing A: {sum('A=01|23' in c for c in counts)}, B: {sum('B=02|13' in c for c in counts)}")


def crossing(cyc, p, q):
    pos = {t: i for i, t in enumerate(cyc)}
    a, b = sorted(pos[t] for t in p)
    c, d = sorted(pos[t] for t in q)
    return (a < c < b) != (a < d < b)


cyclic = [(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3)]
table = {cyc: sorted(k for k, (p, q) in PAIRINGS.items() if not crossing(cyc, p, q)) for cyc in cyclic}
reps = set()
for o in orders:
    i = o.index(0)
    r = o[i:] + o[:i]
    reps.add(min(r, (r[0],) + tuple(reversed(r[1:]))))
chk('L3', 'the 24 orders give exactly 3 cyclic orders up to rotation and reflection', reps == set(cyclic),
    'enumerate', f'{sorted(reps)}')
chk('L4', 'cyclic order 0-1-3-2 is the only one in which A and B are both non-crossing; C = 03|12 crosses there',
    table[(0, 1, 3, 2)] == ['A=01|23', 'B=02|13'] and all(('A=01|23' in v and 'B=02|13' in v) == (k == (0, 1, 3, 2))
                                                        for k, v in table.items()), 'enumerate', f'{table}')
edges = {frozenset(e) for e in [(0, 1), (1, 3), (3, 2), (2, 0)]}
chk('L5', 'the edges of the cycle 0-1-3-2-0 are exactly the four KT4 pairs 01, 23, 02, 13',
    edges == {frozenset(p) for p in [(0, 1), (2, 3), (0, 2), (1, 3)]}, 'enumerate')
rho = {0: 1, 1: 3, 3: 2, 2: 0}
imgA = {frozenset(rho[t] for t in p) for p in PAIRINGS['A=01|23']}
chk('L6', 'the one-click rotation 0->1->3->2->0 maps the pairs of A onto the pairs of B; the transposition (12) does too',
    imgA == {frozenset(p) for p in PAIRINGS['B=02|13']}
    and {frozenset({0: 0, 1: 2, 2: 1, 3: 3}[t] for t in p) for p in PAIRINGS['A=01|23']}
    == {frozenset(p) for p in PAIRINGS['B=02|13']}, 'enumerate')
chk('L4c', 'countercontrol: in the cyclic order 0-1-2-3, B = 02|13 crosses', 'B=02|13' not in table[(0, 1, 2, 3)],
    'countercontrol')

# ================================================================================================================
section('S2  the four-token table calculus (four-copy local tomography built in, as Lemma B2)')
X, Y, E, F = symtab('X'), symtab('Y'), symtab('E'), symtab('F')
Xp, Yp = symtab('U'), symtab('V')
OmA = prodA(X, Y)
OmB = prodB(X, Y)
chk('B2.1', 'effA e f (prodA X Y) = ipW e X * ipW f Y (open sorry effA_prodA of FourCopyPackage A.2)',
    zero(effA(E, F, OmA) - ipW(E, X) * ipW(F, Y)), 'identity')
chk('B2.2', 'effB E F (prodB L L\') = ipW E L * ipW F L\' (open sorry effB_prodB)',
    zero(effB(E, F, OmB) - ipW(E, X) * ipW(F, Y)), 'identity')
chk('B2.3', 'effB E F (prodA X Y) = fourVal X Y E F (open sorry effB_prodA): the famI form',
    zero(effB(E, F, OmA) - fourVal(X, Y, E, F)), 'identity')
chk('B2.4', 'effA e f (prodB L L\') = g2 e f L L\' (open sorry effA_prodB): the famII form',
    zero(effA(E, F, OmB) - g2(E, F, X, Y)), 'identity')
chk('B2.5', 'W4 pairing, grouping A: <prodA X Y, prodA U V> = ipW X U * ipW Y V',
    zero(pair4(OmA, prodA(Xp, Yp)) - ipW(X, Xp) * ipW(Y, Yp)), 'identity')
chk('B2.6', 'W4 pairing, grouping B: <prodB X Y, prodB U V> = ipW X U * ipW Y V',
    zero(pair4(OmB, prodB(Xp, Yp)) - ipW(X, Xp) * ipW(Y, Yp)), 'identity')
chk('B2.7', 'W4 cross pairing: <prodA X Y, prodB L L\'> = fourVal X Y L L\' (states of A against states of B)',
    zero(pair4(OmA, prodB(E, F)) - fourVal(X, Y, E, F)), 'identity')
chk('B2.8', 'token exchange: sigma12 (prodA L L\') = prodB L L\' (naturality of the exchange of tokens 1, 2 on products)',
    all(zero(sigma12(OmA)[k] - OmB[k]) for k in IDX4), 'identity')
chk('B2.8c', 'countercontrol: the identity map does not carry prodA L L\' to prodB L L\'',
    not all(zero(OmA[k] - OmB[k]) for k in IDX4), 'countercontrol')
chk('B2.3c', 'countercontrol: effA E F (prodA X Y) is not fourVal X Y E F (the cross form needs the other grouping)',
    not zero(effA(E, F, OmA) - fourVal(X, Y, E, F)), 'countercontrol')
note('B2.W', 'Lemma B2 in both directions from B2.1-B2.4: if K4 contains prodA K01 K23 and prodB K02 K13 and every '
     'effA e f (e, f in the duals of K01, K23) and every effB E F is nonnegative on K4, then famI is effB on a prodA '
     '(B2.3) and famII is effA on a prodB (B2.4): FCC. Conversely, given FCC, K4 := {Om : effA e f Om >= 0 and '
     'effB E F Om >= 0 for all dual-cone factors} contains prodA (B2.1 and famI via B2.3) and prodB (B2.2 and famII '
     'via B2.4). So "one four-token cone that is a composite in both groupings" is FCC, each direction by its own '
     'argument (the second is the package\'s exists_kt4Cone_of_fourCopyCoherent).')

# ================================================================================================================
section('S3  ordered associativity is blind to the pairs 02 and 13')
Lp = actT(reflY, sing4)
chk('A1', 'L\' := actT reflY sing4 = diag(1,-1,1,-1) (the twin partner of the singlet table)',
    Lp == sp.diag(1, -1, 1, -1), 'witness')
cnotTw = (lambda w: actT(reflY, cnot(actT(reflY, w))))
chk('A2', 'phiW and L\' are gate images of products: phiW = cnot(prodState xplus z3), '
    'L\' = cnotTw(prodState (-xplus) (-z3)), sing4 = cnot(prodState (-xplus) (-z3))',
    cnot(prodState(xplus, z3)) == phiW and cnot(prodState([-1, 0, 0], [0, 0, -1])) == sing4
    and cnotTw(prodState([-1, 0, 0], [0, 0, -1])) == Lp, 'witness')
v = fourVal(phiW, phiW, phiW / 4, Lp / 4)
chk('A3', 'famI for the cones (Q3, Q3, Q3, twin): fourVal phiW phiW (phiW/4) (L\'/4) = -1/8', v == Q(-1, 8), 'witness',
    f'value {v}')
chk('A3c', 'countercontrol: with phiW/4 (a Q3 effect) in place of L\'/4 the value is 1/4 >= 0',
    fourVal(phiW, phiW, phiW / 4, phiW / 4) == Q(1, 4), 'countercontrol')
note('A.W', 'membership: phiW, sing4 in Q3 and L\' in twin are the landed F7-F9 facts (pauliW phiW, opW(phiW/4) and '
     'opW(actT reflY (L\'/4)) are rank-one projectors); recomputed in s3. An ordered-associative structure for the '
     'order 0,1,2,3 (contiguous bracketings 01|23, 0|123, 012|3 and their sub-bracketings) reads only the tokens, '
     'the pairs 01, 12, 23 and the contiguous blocks: its definition contains no K02 or K13. The quantum chain '
     '(PSD on 2^k qubits at every block; Kronecker products of PSD matrices are PSD) satisfies it with K01 = K23 = '
     'Q3, and K02 = Q3, K13 = twin are admissible, closed and preserved by cnot, cnotTw. A3 then shows: ordered '
     'associativity together with the pair hypotheses does not imply FCC.')

# ================================================================================================================
section('S4  the pair 02 induced by an A-composite: admissible, but the induced pairs need not satisfy FCC')
marg02 = {(a, c): ex(OmA[(a, 0, c, 0)]) for a in R4 for c in R4}
chk('I1', 'the 02-marginal of prodA X Y (unit effects on tokens 1, 3) is (X_a0 Y_c0): a product of the token marginals',
    all(zero(marg02[(a, c)] - X[a, 0] * Y[c, 0]) for a in R4 for c in R4), 'identity')
chk('I1c', 'countercontrol: the product-marginal formula of I1 fails for prodB X Y (its 02-marginal is X Y_00)',
    not all(zero(prodB(X, Y)[(a, 0, c, 0)] - X[a, 0] * Y[c, 0]) for a in R4 for c in R4)
    and all(zero(prodB(X, Y)[(a, 0, c, 0)] - X[a, c] * Y[0, 0]) for a in R4 for c in R4), 'countercontrol')
note('I.W', 'for X, Y in Q3 the columns (X_a0), (Y_c0) are nonnegative multiples of hom(marginal Bloch vector), so the '
     '02-marginals of min_A(Q3, Q3) = cone(prodA Q3 Q3) generate SEP; the induced 02 effect cone (the dual of the '
     'marginal cone) is SEP* = maxCone (landed: maxCone is the set of tables nonnegative on all products a b^T, '
     'a, b in Lor). The same holds for 13. So the A-composite K4 = min_A(Q3, Q3) induces the admissible pairs '
     '(SEP, effects maxCone) on 02 and 13.')
a_s = [sp.Symbol(f'a{i}', real=True) for i in R4]
b_s = [sp.Symbol(f'b{i}', real=True) for i in R4]
pv = (sp.Matrix(a_s).T * idW * sp.Matrix(b_s))[0, 0]
chk('I2', 'idW in maxCone: a^T idW b = a.b, symbolic (>= 0 for a, b in Lor by Cauchy-Schwarz on the tails)',
    zero(pv - sum(a_s[i] * b_s[i] for i in R4)), 'identity')
pv2 = (sp.Matrix(a_s).T * sing4 * sp.Matrix(b_s))[0, 0]
chk('I3', 'sing4 in maxCone: a^T sing4 b = a0 b0 - a1 b1 - a2 b2 - a3 b3, symbolic (>= 0 on Lor x Lor)',
    zero(pv2 - (a_s[0] * b_s[0] - a_s[1] * b_s[1] - a_s[2] * b_s[2] - a_s[3] * b_s[3])), 'identity')
w_ind = fourVal(phiW, phiW, idW, sing4)
chk('I4', 'induced-pair cross value: fourVal phiW phiW idW sing4 = -2 (A-product state; product of induced 02, 13 '
    'effects idW, sing4 in maxCone)', w_ind == -2, 'witness', f'value {w_ind}')
chk('I4c', 'countercontrol: with the product effect prodState z3 z3 in place of sing4 the value is >= 0',
    fourVal(phiW, phiW, idW, prodState(z3, z3)) >= 0, 'countercontrol',
    f'value {fourVal(phiW, phiW, idW, prodState(z3, z3))}')
note('I4.W', 'with I2, I3 (and the tail Cauchy-Schwarz) idW and sing4 lie in maxCone, the induced 02 and 13 effect '
     'cones of K4 = min_A(Q3, Q3); phiW lies in Q3, so prodA phiW phiW lies in K4. By B2.3 the value I4 is the '
     'product effect effB idW sing4 at a state of K4: the product of induced local effects is not an effect of K4. '
     'An A-composite therefore induces admissible pairs on 02 and 13 but does not make them compose (the effect '
     'side of cross-pairing fails). With K4 = PSD16 instead the induced pairs are Q3 and cross-pairing holds; the '
     'difference lies in K4, not in associativity.')

# ================================================================================================================
section('S5  the ladder (written; identities above)')
note('LAD', 'rungs for fixed admissible pair cones, four-token cone K4 in W4: (R1) K4 an A-composite, min_A <= K4 '
     '<= max_A: always satisfiable (K4 = min_A, by B2.1); ordered associativity adds only contiguous blocks (L1, '
     'L2) and never reads K02, K13 (S3). (R2) state-level cross-pairing, min_A u min_B <= K4: always satisfiable '
     '(K4 = cone(min_A u min_B)). (R3) effect-level cross-pairing, K4 <= max_A n max_B: given R2 it is exactly '
     'famI and famII (B2.3, B2.4). R2 and R3 together are FCC (B2.W). Stating R2 or R3 at all needs the token '
     'identification across groupings, i.e. the exchange of tokens 1 and 2 natural on products (B2.8); no fixed '
     'linear order supplies it (L2); in the cyclic order 0-1-3-2 both groupings are non-crossing (L4).')

# ================================================================================================================
print()
failed = [c[0] for c in CHECKS if not c[2]]
print('kinds: ' + ', '.join(f"{k} {sum(1 for c in CHECKS if c[1] == k)}"
                            for k in ('identity', 'witness', 'enumerate', 'source', 'countercontrol')), flush=True)
if failed:
    print(f"S1-LADDER: FAILED -- {len(failed)} of {len(CHECKS)}: {', '.join(failed)}", flush=True)
    sys.exit(1)
print(f'VERDICT S1-LADDER-EXACT -- {len(CHECKS)} checks', flush=True)
