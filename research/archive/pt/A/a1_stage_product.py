#!/usr/bin/env python3
"""Thread A (PAIR-COMP), node A1: the stage-level product of two directed systems of one-ball stages,
and the variants that add native-gate images. Exact arithmetic only (fractions.Fraction, sympy
Rationals for symbolic identities). Run as:  python3 -I -B a1_stage_product.py

Objects (conventions transcribed from CompositeDimension.lean / K2Guard.lean at L = 9f9f8257, as in the
landed probe kt4_prem1_probe.py: tables W 3 indexed 0..3, index 0 the unit; hom x = (1, x);
prodState x y = hom x hom y^T; pairVal a b w = a^T w b; ehom e = (e(0), linear coefficients);
cnot w (m, n) = sgn(m, n) w(pc(m, n), pt(m, n)); actT R w = w homMap(R)^T; reflY = diag(1, -1, 1)).
The script re-checks its transcription of sgn/pc/pt/phiW/idW/chainW/reflY against the base sources
(read-only) before using them.

One-ball directed system D1 (a finite instance): index i in {0, 1, 2, 3} (a chain); stage i has the
first np(i) points of a fixed list of rational points of the closed unit ball and the first ne(i)
effects of a fixed list of rational affine effects of the ball (the unit first); table e(x); stage
maps are inclusions. The narrow product D1 x D1 has index (i, j) with the product order, preparations
P_i x P_j, effects E_i x E_j (product labels), table e(x) f(y), stage maps the product inclusions.

DECISION RULES (fixed before the first run; read as rules, not expected numbers):
  R1 STAGE-VALID: a finite stage is valid iff every table entry lies in [0, 1] and the unit label
     reads 1 at every preparation (exact).
  R2 PRODUCT-LAWS: the narrow product passes iff (a) every product stage (i, j), i, j <= 3, is valid
     (R1); (b) for every comparable chain (i, j) <= (k, l) <= (m, n) of the product index set the
     composite of the inclusion maps equals the inclusion map, on effects and on preparations;
     (c) unit_map: the unit label is sent to the unit label; (d) SC-infinity: for every
     (i, j) <= (k, l), the table at (k, l) of the images equals the table at (i, j), entrywise.
  R3 TAB-PRODUCT: for every product label (e, f) and product preparation (x, y) of the largest stage,
     e(x) f(y) = pairVal(ehom e, ehom f, prodState x y) exactly; and the symbolic identity
     pairVal(a, b, prodState x y) = (a.hom x)(b.hom y) holds for symbolic a, b, x, y.
  R4 CNOT-CLOSURE-VALID: the stages whose preparations are P x P together with cnot(prodState x y)
     are valid (R1) at every product stage, the table of a gate image being
     pairVal(ehom e, ehom f, cnot(prodState x y)); and cnot . cnot = id on a symbolic table (so the
     closure under cnot adds exactly one image per product and terminates).
  R5 REFL-GATE-CLOSURE-INVALID: for the N-CLASS gate N = actT reflY . cnot (B = reflY, other locals
     the identity), the N-orbit of prodState xplus z3 contains a table with a strictly negative
     value at a product label of two valid one-ball effects (exact witness), so no stage system
     closed under N has valid tables. Countercontrol C5: the same label on the cnot-orbit of the
     same product is >= 0.
  R6 SPAN: the 16 product labels built from the four effects {unit, (1+x1)/2, (1+x2)/2, (1+x3)/2}
     have a coefficient matrix [ehom(e_a)_m ehom(e_b)_n] of rank 16 (the read-out of tables from
     16 labels is well defined). Countercontrol C6: the labels built from {unit, (1+x3)/2, (1-x3)/2}
     have rank < 16.
  R7 RANK: the product-state tables of the largest stage span a linear space of dimension 16
     (affine dimension 15): the completed body of the narrow product has finite rank.
  Countercontrol C2: a mutated stage map that sends one effect label to a different label breaks
     SC-infinity (R2(d) must fail for it).
  VERDICT: printed iff every check above passes and every countercontrol gives its required
  (opposite) verdict; otherwise the script prints 'VERDICT: not rendered' and exits 1.
Everything printed is deterministic; no timing.
"""
import re
import sys
from fractions import Fraction as Fr
from itertools import product
from pathlib import Path

import sympy as sp

R4 = range(4)
CHECKS = []


def chk(cid, name, ok, kind, detail=''):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}" + (f" -- {detail}" if detail else ''), flush=True)


# ------------------------------------------------------------------------------------------------
# transcription (checked against the base below)
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
NEG = {(1, 3), (2, 2)}

BASE = Path(__file__).resolve().parent.parent / 'base' / 'verification' / 'lean-mathlib' / 'OIBridge'
CD = (BASE / 'CompositeDimension.lean').read_text(encoding='utf-8')
KG = (BASE / 'K2Guard.lean').read_text(encoding='utf-8')

print('== S0 transcription of the landed tables (base at L, read-only)')
msg = re.search(r'^def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) '
                r'then -1 else 1$', CD, re.M)
neg_src = {(int(msg.group(1)), int(msg.group(2))), (int(msg.group(3)), int(msg.group(4)))} if msg else None
chk('S0.sgn', 'sgn is -1 exactly at (1, 3) and (2, 2)', neg_src == NEG, 'source')


def lean_table(nm):
    mm = re.search(rf'^def {nm} : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n){{4}})', CD, re.M)
    if not mm:
        return None
    T = [[None] * 4 for _ in R4]
    for a, b, v in re.findall(r'\|\s*(\d),\s*(\d)\s*=>\s*(\d)', mm.group(1)):
        T[int(a)][int(b)] = int(v)
    return T


chk('S0.pc', 'pc table', lean_table('pc') == PC, 'source')
chk('S0.pt', 'pt table', lean_table('pt') == PT, 'source')
chk('S0.phiW', 'phiW = diag(1, 1, -1, 1)',
    'def phiW : W 3 := fun μ ν => if μ = ν then (if μ = 2 then -1 else 1) else 0' in CD, 'source')
chk('S0.reflY', 'reflY = diag(1, -1, 1)', 'toFun x := fun i => (![1, -1, 1] : Fin 3 → ℝ) i * x i' in KG, 'source')
chk('S0.idW', 'idW = identity table',
    'def idW : W 3 := ![![1, 0, 0, 0], ![0, 1, 0, 0], ![0, 0, 1, 0], ![0, 0, 0, 1]]' in KG, 'source')
chk('S0.chainW', 'chainW table',
    'def chainW : W 3 := ![![1, 0, 0, 1], ![1, 0, 0, -1], ![0, 0, 0, 0], ![0, 0, 0, 0]]' in KG, 'source')
chk('S0.cnotPS', 'landed cnot_prodState_mem_maxCone and cnot_prodState_xplus_z3 are present',
    'theorem cnot_prodState_mem_maxCone' in CD and 'theorem cnot_prodState_xplus_z3' in CD, 'source')


# ------------------------------------------------------------------------------------------------
# exact table calculus with Fractions
def sgn(m, n):
    return -1 if (m, n) in NEG else 1


def cnot(w):
    return [[sgn(m, n) * w[PC[m][n]][PT[m][n]] for n in R4] for m in R4]


def hom(x):
    return [Fr(1)] + [Fr(v) for v in x]


def homMap(R):
    M = [[Fr(0)] * 4 for _ in R4]
    M[0][0] = Fr(1)
    for i in range(3):
        for j in range(3):
            M[i + 1][j + 1] = Fr(R[i][j])
    return M


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in R4) for j in R4] for i in R4]


def tr(A):
    return [[A[j][i] for j in R4] for i in R4]


def actT(R, w):
    return mul(w, tr(homMap(R)))


def prodState(x, y):
    a, b = hom(x), hom(y)
    return [[a[i] * b[j] for j in R4] for i in R4]


def pairVal(a, b, w):
    return sum(a[m] * w[m][n] * b[n] for m in R4 for n in R4)


reflY = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]
xplus, z3 = [1, 0, 0], [0, 0, 1]
phiW = [[Fr(v) for v in r] for r in [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]]]
idW = [[Fr(int(i == j)) for j in R4] for i in R4]
chainW = [[Fr(v) for v in r] for r in [[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]]]

# one-ball data: rational points of the closed ball (sphere points first), rational effects
F = Fr
POINTS = [[1, 0, 0], [0, 0, 1], [0, 1, 0], [-1, 0, 0], [0, 0, -1], [0, -1, 0],
          [F(3, 5), F(4, 5), 0], [0, F(3, 5), F(4, 5)], [F(4, 5), 0, F(3, 5)], [F(2, 3), F(2, 3), F(1, 3)],
          [F(-2, 3), F(1, 3), F(2, 3)], [0, 0, 0], [F(1, 2), 0, 0], [F(1, 3), F(-1, 3), F(1, 3)]]


def eff(a0, a):              # the affine functional x -> a0 + a.x, stored as its ehom vector
    return [F(a0)] + [F(v) for v in a]


EFFECTS = [eff(1, [0, 0, 0]),                         # the unit
           eff(F(1, 2), [F(1, 2), 0, 0]), eff(F(1, 2), [0, F(1, 2), 0]), eff(F(1, 2), [0, 0, F(1, 2)]),
           eff(F(1, 2), [F(-1, 2), 0, 0]), eff(F(1, 2), [0, F(-1, 2), 0]), eff(F(1, 2), [0, 0, F(-1, 2)]),
           eff(F(1, 2), [F(3, 10), F(2, 5), 0]), eff(F(1, 2), [F(1, 3), F(1, 3), F(1, 6)]),
           eff(F(1, 2), [0, F(1, 8), F(-1, 8)]), eff(F(1, 4), [F(1, 8), F(-1, 8), F(1, 8)])]


def evalEff(e, x):
    return e[0] + sum(e[i + 1] * F(x[i]) for i in range(3))


def is_ball(x):
    return sum(F(v) ** 2 for v in x) <= 1


def is_effect(e):            # |a| <= min(a0, 1 - a0)  <=>  e is an effect on the ball
    n2 = sum(v * v for v in e[1:])
    return e[0] >= 0 and e[0] <= 1 and n2 <= e[0] ** 2 and n2 <= (1 - e[0]) ** 2


def npts(i):
    return 5 + 3 * i


def neff(i):
    return 4 + 2 * i


IDX = range(4)

print()
print('== S1 the one-ball stages')
chk('A1.0a', 'the listed points lie in the closed unit ball', all(is_ball(x) for x in POINTS), 'enumerate',
    f'{len(POINTS)} points')
chk('A1.0b', 'the listed affine functionals are effects of the ball (|a| <= min(a0, 1 - a0)); the first is the unit',
    all(is_effect(e) for e in EFFECTS) and EFFECTS[0] == eff(1, [0, 0, 0]), 'enumerate', f'{len(EFFECTS)} effects')
ok1 = all(0 <= evalEff(e, x) <= 1 for i in IDX for e in EFFECTS[:neff(i)] for x in POINTS[:npts(i)])
ok1 = ok1 and all(evalEff(EFFECTS[0], x) == 1 for x in POINTS)
chk('A1.0c', 'R1 for every one-ball stage i <= 3 (values in [0,1], unit reads 1)', ok1, 'enumerate')


# ------------------------------------------------------------------------------------------------
print()
print('== S2 the narrow product D1 x D1 (product preparations, product labels, inclusions)')


def stage_prod(i, j):
    P = [(x, y) for x in POINTS[:npts(i)] for y in POINTS[:npts(j)]]
    E = [(a, b) for a in range(neff(i)) for b in range(neff(j))]
    return P, E


def p_prod(lab, prep):
    (a, b), (x, y) = lab, prep
    return evalEff(EFFECTS[a], x) * evalEff(EFFECTS[b], y)


def valid(P, E, pfun, unit_lab):
    ok = all(0 <= pfun(e, x) <= 1 for e in E for x in P)
    return ok and all(pfun(unit_lab, x) == 1 for x in P)


okA = all(valid(*stage_prod(i, j), p_prod, (0, 0)) for i in IDX for j in IDX)
chk('A1.1', 'R2(a): every product stage (i, j), i, j <= 3, is valid', okA, 'enumerate', '16 stages')


def le(p, q):
    return p[0] <= q[0] and p[1] <= q[1]


def mapE(p, q, lab):          # inclusion of labels (indices into the fixed lists)
    assert le(p, q)
    return lab


def mapP(p, q, prep):
    assert le(p, q)
    return prep


pairs = [(i, j) for i in IDX for j in IDX]
okC = True
okU = True
okSC = True
for p in pairs:
    for q in pairs:
        if not le(p, q):
            continue
        Pp, Ep = stage_prod(*p)
        Pq, Eq = stage_prod(*q)
        okU = okU and mapE(p, q, (0, 0)) == (0, 0)
        okC = okC and all(mapE(p, q, e) in Eq for e in Ep) and all(mapP(p, q, x) in Pq for x in Pp)
        okSC = okSC and all(p_prod(mapE(p, q, e), mapP(p, q, x)) == p_prod(e, x) for e in Ep for x in Pp)
        for r in pairs:
            if le(q, r):
                okC = okC and all(mapE(q, r, mapE(p, q, e)) == mapE(p, r, e) for e in Ep)
                okC = okC and all(mapP(q, r, mapP(p, q, x)) == mapP(p, r, x) for x in Pp)
chk('A1.2', 'R2(b): inclusions land in the larger stage and compose (comp_E, comp_P), all chains', okC, 'enumerate')
chk('A1.3', 'R2(c): unit_map', okU, 'enumerate')
chk('A1.4', 'R2(d): SC-infinity for every comparable pair of product stages', okSC, 'enumerate')


def mapE_bad(p, q, lab):      # countercontrol: send label (1, 0) to (4, 0) when p != q
    if p != q and lab == (1, 0):
        return (4, 0)
    return lab


okSC_bad = True
for p in pairs:
    for q in pairs:
        if le(p, q):
            Pp, Ep = stage_prod(*p)
            okSC_bad = okSC_bad and all(p_prod(mapE_bad(p, q, e), x) == p_prod(e, x) for e in Ep for x in Pp)
chk('C2', 'countercontrol: a stage map sending the label (1,0) to (4,0) breaks SC-infinity', not okSC_bad,
    'countercontrol')

# ------------------------------------------------------------------------------------------------
print()
print('== S3 TAB on the narrow product')
Pmax, Emax = stage_prod(3, 3)
okTab = all(p_prod(lab, prep) == pairVal(EFFECTS[lab[0]], EFFECTS[lab[1]], prodState(*prep))
            for lab in Emax for prep in Pmax)
chk('A1.5', 'R3: e(x) f(y) = pairVal(ehom e, ehom f, prodState x y) at every label and preparation of stage (3,3)',
    okTab, 'enumerate', f'{len(Emax)} labels x {len(Pmax)} preparations')
asym = sp.symbols('a0:4', real=True)
bsym = sp.symbols('b0:4', real=True)
xsym = sp.symbols('x0:3', real=True)
ysym = sp.symbols('y0:3', real=True)
hx = [1] + list(xsym)
hy = [1] + list(ysym)
lhs = sum(asym[m] * hx[m] * hy[n] * bsym[n] for m in R4 for n in R4)
rhs = sum(asym[m] * hx[m] for m in R4) * sum(bsym[n] * hy[n] for n in R4)
chk('A1.6', 'R3: pairVal(a, b, prodState x y) = (a.hom x)(b.hom y), symbolic (landed prodEffVal_prodState)',
    sp.expand(lhs - rhs) == 0, 'identity')

# ------------------------------------------------------------------------------------------------
print()
print('== S4 closing the product stages under the native gate cnot')


def p_tab(lab, w):
    return pairVal(EFFECTS[lab[0]], EFFECTS[lab[1]], w)


okG = True
nimg = 0
for i in IDX:
    for j in IDX:
        P, E = stage_prod(i, j)
        imgs = [cnot(prodState(x, y)) for (x, y) in P]
        nimg += len(imgs)
        okG = okG and all(0 <= p_tab(e, w) <= 1 for e in E for w in imgs) and all(p_tab((0, 0), w) == 1 for w in imgs)
chk('A1.7', 'R4: the cnot images of the product preparations have valid tables at every stage', okG, 'enumerate',
    f'{nimg} gate images')
W = sp.Matrix(4, 4, lambda m, n: sp.Symbol(f'w{m}{n}', real=True))


def cnot_sym(w):
    return sp.Matrix(4, 4, lambda m, n: sgn(m, n) * w[PC[m][n], PT[m][n]])


chk('A1.8', 'R4: cnot . cnot = id on a symbolic table (closure under cnot adds one image per product)',
    (cnot_sym(cnot_sym(W)) - W).applyfunc(sp.expand) == sp.zeros(4, 4), 'identity')

# ------------------------------------------------------------------------------------------------
print()
print('== S5 closing under the N-CLASS gate N = actT reflY . cnot (M_D\'s N_13)')


def Ngate(w):
    return actT(reflY, cnot(w))


o0 = prodState(xplus, z3)
o1 = Ngate(o0)
o2 = Ngate(o1)
sNX = eff(F(1, 2), [F(-1, 2), 0, 0])       # sharpEff ![-1, 0, 0]
sNZ = eff(F(1, 2), [0, 0, F(-1, 2)])       # sharpEff ![0, 0, -1]
v2 = pairVal(sNX, sNZ, o2)
chk('A1.9', 'R5: N(prodState xplus z3) = idW, N(idW) = chainW, and the sharp pair (-e1, -e3) reads -1/2 on N^2',
    o1 == idW and o2 == chainW and is_effect(sNX) and is_effect(sNZ) and v2 == F(-1, 2), 'witness', f'value {v2}')
c0, c1, c2 = o0, cnot(o0), cnot(cnot(o0))
vc = [pairVal(sNX, sNZ, w) for w in (c0, c1, c2)]
chk('C5', 'countercontrol: on the cnot-orbit of the same product the same label reads >= 0',
    c1 == phiW and c2 == o0 and min(vc) >= 0, 'countercontrol', f'values {[str(v) for v in vc]}')

# ------------------------------------------------------------------------------------------------
print()
print('== S6 the read-out of tables from product labels, and the rank of the completed body')
BASIS = [EFFECTS[0], EFFECTS[1], EFFECTS[2], EFFECTS[3]]
M16 = sp.Matrix(16, 16, lambda r, c: sp.Rational(BASIS[r // 4][c // 4] * BASIS[r % 4][c % 4]))
rk16 = M16.rank()
chk('A1.10', 'R6: the 16 product labels of {unit, (1+x_j)/2} have coefficient rank 16', rk16 == 16, 'witness',
    f'rank {rk16}')
ZEFF = [EFFECTS[0], EFFECTS[3], EFFECTS[6]]
MZ = sp.Matrix(9, 16, lambda r, c: sp.Rational(ZEFF[r // 3][c // 4] * ZEFF[r % 3][c % 4]))
rkZ = MZ.rank()
chk('C6', 'countercontrol: the labels of {unit, (1+x3)/2, (1-x3)/2} have rank < 16', rkZ < 16, 'countercontrol',
    f'rank {rkZ}')
tabs = sp.Matrix([[sp.Rational(v) for row in prodState(x, y) for v in row] for (x, y) in Pmax])
rkP = tabs.rank()
chk('A1.11', 'R7: the product-state tables of stage (3,3) span 16 dimensions (affine dimension 15)', rkP == 16,
    'witness', f'rank {rkP}')

# ------------------------------------------------------------------------------------------------
print()
kinds = {}
for _, k, _ in CHECKS:
    kinds[k] = kinds.get(k, 0) + 1
print('kinds: ' + ', '.join(f'{k} {v}' for k, v in sorted(kinds.items())))
failed = [c for c, _, ok in CHECKS if not ok]
if failed:
    print(f'a1_stage_product: FAILED -- {len(failed)} of {len(CHECKS)}: {", ".join(failed)}')
    print('VERDICT: not rendered')
    sys.exit(1)
print(f'a1_stage_product: OK -- {len(CHECKS)} checks')
print('VERDICT A1: the narrow stage-level product of two one-ball directed systems is a directed system '
      'of finite stages with SC-infinity and bi-affine product tables (on the instance checked); closing it '
      'under cnot keeps the tables valid; closing it under the N-CLASS gate actT reflY . cnot does not '
      '(value -1/2); 16 product labels read out the table; the completed body has finite rank (15).')
