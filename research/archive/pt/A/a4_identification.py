#!/usr/bin/env python3
"""Thread A (PAIR-COMP), nodes A3/A4: exact instances for the identification principle ID and for the
local-tomography bookkeeping. Exact arithmetic only. Run as:  python3 -I -B a4_identification.py

(1) The per-cone system D_K (the converse half of "ID <=> hcl relative to hadm", written argument W-A4.2):
    for a closed admissible cone K, stage n has as preparations the first n points of a countable dense subset
    of K's normalized slice and as labels the product labels of a fixed finite list of one-ball effects; the
    table is pairVal(ehom e, ehom f, q). The exact layer checks, for finite lists of certified members of three
    closed admissible cones (Q3, maxCone, K_gen), that every table entry lies in [0, 1], the unit reads 1, and
    the 16 basis labels read back the table (the read-out T inverts the label map on tables).
(2) The padded system D_pad: preparations (q, h), q a product table, h in {0, 1}; labels: the product labels and
    one joint label 'h' reading h. It has finite rank, its product-label read-out does not separate its
    states (local tomography fails), and its read-out image is the set of the q's: the closedness argument
    W-A3.1 does not use local tomography.
(3) The landed Q2 fact that local tomography does not give closedness: on the normalized slice of any cone
    inside maxCone the four product-effect values of e, 1 - e and f, 1 - f sum to 1 (landed probe I1,
    re-checked here symbolically), which with the landed minComposite argument makes the slice of the
    non-closed K_cl a COMP-1 Composite (with lt).

DECISION RULES (fixed before the first run; rules, not expected numbers):
  R1 D_K INSTANCES: for each listed table q with its stated certificate of membership (Q3: pauliW q is a
     rank-one projector, or q = E00, or q is a product state or a cnot image of one (landed D1, D5, D6),
     or a listed convex combination of these; maxCone: q = idW with the identity pairVal a b idW = a.b
     (landed M_max.3) or a member of Q3; K_gen: products and cnot images), q_00 = 1, and every product
     label of the effect list reads a value in [0, 1] with the unit reading 1; and the 16 basis labels read
     back q exactly.
  R2 D_pad: (a) every table entry of the padded stages lies in [0, 1], unit 1; (b) local tomography fails:
     two preparations with equal values on every product label and different values on the joint label;
     (c) finite rank: the value vectors of all padded preparations have rank equal to (rank on the product
     labels) + 1; (d) the read-out of each padded preparation is its q.
  R3 I1: for symbolic w with w_00 = 1 and symbolic a, b, pairVal a b w + pairVal (u - a) b w + pairVal a (u - b) w +
     pairVal (u - a) (u - b) w = 1, u = (1, 0, 0, 0).
  COUNTERCONTROLS: C1 a table outside maxCone (chainW, landed) produces a negative entry on the label list
     (the [0, 1] check of R1 is not vacuous); C2 for D_pad, with the joint label removed the two preparations
     of R2(b) have equal value vectors (the joint label is what separates them); C3 without w_00 = 1 the sum of
     R3 is w_00, not 1 (landed probe X4).
  VERDICT: printed iff all checks and countercontrols pass; otherwise 'VERDICT: not rendered', exit 1.
Deterministic output; no timing.
"""
import re
import sys
from pathlib import Path

import sympy as sp

R4 = range(4)
CHECKS = []


def chk(cid, name, ok, kind, detail=''):
    ok = bool(ok)
    CHECKS.append((cid, kind, ok))
    print(f"{'PASS' if ok else 'FAIL'} {cid}  [{kind}] {name}" + (f" -- {detail}" if detail else ''), flush=True)


def note(cid, text):
    print(f'NOTE [written] {cid}  -- {text}', flush=True)


PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
NEG = {(1, 3), (2, 2)}
BASE = Path(__file__).resolve().parent.parent / 'base' / 'verification' / 'lean-mathlib' / 'OIBridge'
CD = (BASE / 'CompositeDimension.lean').read_text(encoding='utf-8')
KG = (BASE / 'K2Guard.lean').read_text(encoding='utf-8')
msg = re.search(r'^def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) '
                r'then -1 else 1$', CD, re.M)
neg_src = {(int(msg.group(1)), int(msg.group(2))), (int(msg.group(3)), int(msg.group(4)))} if msg else None


def lean_table(nm):
    mm = re.search(rf'^def {nm} : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n){{4}})', CD, re.M)
    if not mm:
        return None
    T = [[None] * 4 for _ in R4]
    for a, b, v in re.findall(r'\|\s*(\d),\s*(\d)\s*=>\s*(\d)', mm.group(1)):
        T[int(a)][int(b)] = int(v)
    return T


print('== S0 transcription')
chk('S0.tables', 'sgn, pc, pt, phiW, idW, chainW transcribed from the base', neg_src == NEG
    and lean_table('pc') == PC and lean_table('pt') == PT
    and 'def phiW : W 3 := fun μ ν => if μ = ν then (if μ = 2 then -1 else 1) else 0' in CD
    and 'def idW : W 3 := ![![1, 0, 0, 0], ![0, 1, 0, 0], ![0, 0, 1, 0], ![0, 0, 0, 1]]' in KG
    and 'def chainW : W 3 := ![![1, 0, 0, 1], ![1, 0, 0, -1], ![0, 0, 0, 0], ![0, 0, 0, 0]]' in KG, 'source')


def sgn(m, n):
    return -1 if (m, n) in NEG else 1


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: sgn(m, n) * w[PC[m][n], PT[m][n]])


def hom(x):
    return sp.Matrix([1] + list(x))


def homMap(R):
    M = sp.zeros(4, 4)
    M[0, 0] = 1
    M[1:4, 1:4] = R
    return M


def actT(R, w):
    return w * homMap(R).T


def prodState(x, y):
    return hom(x) * hom(y).T


def pairVal(a, b, w):
    return (sp.Matrix(a).T * w * sp.Matrix(b))[0, 0]


iu = sp.I
S = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -iu], [iu, 0]]), sp.Matrix([[1, 0], [0, -1]])]


def pauliW(w):
    out = sp.zeros(4, 4)
    for m in R4:
        for n in R4:
            if w[m, n] != 0:
                out += w[m, n] * sp.kronecker_product(S[m], S[n])
    return out / 4


def rank1_projector(w):
    P = pauliW(w)
    return (P - P.H).applyfunc(sp.expand) == sp.zeros(4, 4) and (P * P - P).applyfunc(sp.expand) == sp.zeros(4, 4) \
        and P.rank() == 1


Q = sp.Rational
phiW = sp.diag(1, 1, -1, 1)
idW = sp.eye(4)
chainW = sp.Matrix([[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]])
E00 = sp.zeros(4, 4)
E00[0, 0] = 1
RH = sp.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
Tpsi = actT(RH, phiW)


def eff(a0, a):
    return [Q(a0)] + [Q(v) for v in a]


EFFECTS = [eff(1, [0, 0, 0]), eff(Q(1, 2), [Q(1, 2), 0, 0]), eff(Q(1, 2), [0, Q(1, 2), 0]),
           eff(Q(1, 2), [0, 0, Q(1, 2)]), eff(Q(1, 2), [Q(-1, 2), 0, 0]), eff(Q(1, 2), [0, Q(-1, 2), 0]),
           eff(Q(1, 2), [0, 0, Q(-1, 2)]), eff(Q(1, 2), [Q(3, 10), Q(2, 5), 0]),
           eff(Q(1, 2), [Q(1, 3), Q(1, 3), Q(1, 6)]), eff(Q(1, 4), [Q(1, 8), Q(-1, 8), Q(1, 8)])]
BAS = EFFECTS[:4]
M16 = sp.Matrix(16, 16, lambda r, c: BAS[r // 4][c // 4] * BAS[r % 4][c % 4])
M16inv = M16.inv()


def labels_ok(q):
    vals = [pairVal(e, f, q) for e in EFFECTS for f in EFFECTS]
    return all(0 <= v <= 1 for v in vals) and pairVal(EFFECTS[0], EFFECTS[0], q) == 1


def readout(q):
    v = sp.Matrix([pairVal(BAS[r // 4], BAS[r % 4], q) for r in range(16)])
    w = M16inv * v
    return sp.Matrix(4, 4, lambda i, j: w[4 * i + j])


x1, x2, x3 = [1, 0, 0], [0, Q(3, 5), Q(4, 5)], [Q(2, 3), Q(-2, 3), Q(1, 3)]
prods = [prodState(x1, x2), prodState(x2, x3), prodState(x3, x1), prodState([0, 0, 0], x2)]
cnots = [cnot(p) for p in prods]
Q3_list = [('product', p) for p in prods] + [('cnot image', c) for c in cnots] + \
    [('rank-one', phiW), ('rank-one', Tpsi), ('E00', E00), ('mixture', (phiW + Tpsi) / 2),
     ('mixture', (prods[0] + cnots[1] + E00) / 3)]
MAX_list = [('idW', idW), ('mixture', (idW + E00) / 2), ('mixture', (idW + phiW) / 2)]
GEN_list = [('product', p) for p in prods] + [('cnot image', c) for c in cnots] + [('mixture', (prods[1] + cnots[2]) / 2)]


def certified_Q3(kind, q):
    if kind == 'rank-one':
        return rank1_projector(q)
    if kind == 'E00':
        return q == E00
    return kind in ('product', 'cnot image', 'mixture')


print()
print('== S1 instances of D_K (R1)')
okQ = all(certified_Q3(k, q) and q[0, 0] == 1 and labels_ok(q) and readout(q) == q for k, q in Q3_list)
chk('A4.1', 'R1: K = Q3, 13 certified normalized members: label values in [0,1], unit 1, read-out exact', okQ, 'sample')
asym = sp.symbols('a0:4', real=True)
bsym = sp.symbols('b0:4', real=True)
id_ok = sp.expand(pairVal(asym, bsym, idW) - sum(asym[i] * bsym[i] for i in R4)) == 0
okM = id_ok and all(q[0, 0] == 1 and labels_ok(q) and readout(q) == q for k, q in MAX_list)
chk('A4.2', 'R1: K = maxCone, idW (pairVal a b idW = a.b) and two mixtures: label values in [0,1], unit 1, read-out '
    'exact', okM, 'sample')
okG = all(q[0, 0] == 1 and labels_ok(q) and readout(q) == q for k, q in GEN_list)
chk('A4.3', 'R1: K = K_gen, products, cnot images and a mixture: label values in [0,1], unit 1, read-out exact', okG,
    'sample')
vneg = min(pairVal(e, f, chainW) for e in EFFECTS for f in EFFECTS)
chk('C1', 'countercontrol: chainW (outside maxCone) has a negative label value on the same list', vneg < 0,
    'countercontrol', f'minimum {vneg}')
note('A4.W1', 'the general construction (written, W-A4.2): for a closed K that contains the products, lies in maxCone '
     'and is a convex cone, its normalized slice S is compact (landed design lemma abs_le_one_of_maxCone bounds it, '
     'closedness of K closes it) and convex; take a countable dense Q in S; stage n has preparations q_1..q_n and '
     'the product labels of finitely many effects including the four basis effects; values lie in [0,1] because '
     'S lies in the normalized maxCone (as R1 checks on instances). The completion body is Psi(cl conv Q) = Psi(S) '
     '(Psi is an injective linear map out of a finite-dimensional space, hence a closed embedding), so the system '
     'has finite rank, its read-out image is S, and the cone over S is K.')

print()
print('== S2 the padded system D_pad (R2)')
pad = [(q, h) for q in prods for h in (0, 1)]


def pad_vals(p, with_h=True):
    q, h = p
    v = [pairVal(e, f, q) for e in EFFECTS for f in EFFECTS]
    return v + [h] if with_h else v


okPa = all(all(0 <= v <= 1 for v in pad_vals(p)) and pairVal(EFFECTS[0], EFFECTS[0], p[0]) == 1 for p in pad)
chk('A4.4', 'R2(a): the padded stage is valid (values in [0,1], unit 1)', okPa, 'enumerate', f'{len(pad)} preparations')
p0, p1 = pad[0], pad[1]
same_prod = pad_vals(p0, False) == pad_vals(p1, False)
chk('A4.5', 'R2(b): (q, 0) and (q, 1) agree on every product label and differ on the joint label: local tomography '
    'fails', same_prod and pad_vals(p0)[-1] != pad_vals(p1)[-1], 'witness')
rk_all = sp.Matrix([pad_vals(p) for p in pad]).rank()
rk_prod = sp.Matrix([pad_vals(p, False) for p in pad]).rank()
chk('A4.6', 'R2(c): rank of the padded value vectors = rank on product labels + 1 (finite rank)', rk_all == rk_prod + 1,
    'witness', f'ranks {rk_all} and {rk_prod}')
chk('A4.7', 'R2(d): the read-out of each padded preparation is its product table', all(readout(p[0]) == p[0] for p in pad),
    'enumerate')
chk('C2', 'countercontrol: with the joint label removed the two preparations of A4.5 have equal value vectors',
    pad_vals(p0, False) == pad_vals(p1, False) and pad_vals(p0) != pad_vals(p1), 'countercontrol')
note('A4.W2', 'D_pad (with a dense set of product preparations in place of the four listed) has a completed body of '
     'finite rank whose read-out image is the normalized slice of SEP, which is compact: the shadow is closed. Local '
     'tomography fails (A4.5). So the closedness argument W-A3.1 (finite rank and a continuous read-out) does not use '
     'local tomography; local tomography is used only where the read-out is required to be injective, i.e. where the '
     'completed state space itself is identified with a subset of W 3.')

print()
print('== S3 the landed I1 identity (R3)')
W = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f'w{i}{j}', real=True))
Wn = W.copy()
Wn[0, 0] = 1
u = [1, 0, 0, 0]
am = [u[i] - asym[i] for i in R4]
bm = [u[i] - bsym[i] for i in R4]
tot = pairVal(asym, bsym, Wn) + pairVal(am, bsym, Wn) + pairVal(asym, bm, Wn) + pairVal(am, bm, Wn)
chk('A4.8', 'R3: on w with w_00 = 1 the four product-effect values of e, 1-e and f, 1-f sum to 1 (landed probe I1)',
    sp.expand(tot - 1) == 0, 'identity')
tot0 = pairVal(asym, bsym, W) + pairVal(am, bsym, W) + pairVal(asym, bm, W) + pairVal(am, bm, W)
chk('C3', 'countercontrol: without w_00 = 1 the sum is w_00 (landed probe X4)', sp.expand(tot0 - W[0, 0]) == 0
    and sp.expand(tot0 - 1) != 0, 'countercontrol')
note('A4.W3', 'with the landed result note Q2 (I1W): the normalized slice of K_cl is convex, contains the products, lies '
     'in maxCone, so (A4.8) every product of effects takes values in [0,1] on it; with the coordinate-model data and the '
     'lt argument of the landed minComposite/maxComposite (prodEff_eq_of_eff_eq with modelData_ext) it is a COMP-1 '
     'Composite, local tomography included, whose body is not closed. So K2 in the form "the pair is a coordinate-model '
     'Composite in W 3" does not give hcl.')

print()
kinds = {}
for _, k, _ in CHECKS:
    kinds[k] = kinds.get(k, 0) + 1
print('kinds: ' + ', '.join(f'{k} {v}' for k, v in sorted(kinds.items())))
failed = [c for c, _, ok in CHECKS if not ok]
if failed:
    print(f'a4_identification: FAILED -- {len(failed)} of {len(CHECKS)}: {", ".join(failed)}')
    print('VERDICT: not rendered')
    sys.exit(1)
print(f'a4_identification: OK -- {len(CHECKS)} checks')
print('VERDICT A4: on the instances checked, members of the closed admissible cones Q3, maxCone and K_gen are valid '
      'preparations of a product-label pair system whose read-out returns them (the exact layer of the converse half '
      'of ID <=> hcl); the padded system has finite rank, fails local tomography, and reads out product tables (the '
      'closedness argument does not consume local tomography); and the landed I1 identity holds.')
