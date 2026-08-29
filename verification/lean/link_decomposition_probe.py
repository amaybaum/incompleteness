#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OIBridge/LinkDecomposition.lean.

[SM] Theorem 7: the six signed nearest-neighbour link directions of the simple-cubic lattice
decompose under the cubic ROTATION group O — 24 elements, not the 48-element O_h of Corollary 1a —
as 6 = T1(3) + E(2) + A1(1). The manuscript's own proof runs through the characters at the five
conjugacy classes and then the character inner products.

  WHAT LEAN HAS. Three explicit projectors, idempotent, pairwise orthogonal, summing to the
  identity, each commuting with every symmetry of the link set; dimensions 3, 2, 1 read off their
  traces through the IdempotentTrace lemma; and the character at a four-fold rotation, which is 1
  for the three-dimensional summand — T1's value, not T2's.

  WHAT THE ZERO-IMPORT LAYER ALREADY HAS. The manuscript's proof line is kernel-proved there:
  OI_Gauge_Certificates.chi_consistent (the fixed directed-link count equals chiT + chiE + chiA),
  irr_orthonormal (the five irreducible characters are orthonormal over the 24 rotations, which is
  the irreducibility witness) and mult_V6 (the inner products, 24*(1,0,1,1,0)). L4 and L5 below
  reproduce that arithmetic independently rather than standing in for a gap.

  WHAT IS MISSING is the JOIN: that the zero-import layer's encoding of the 24 rotations is the
  same group as this file's antipode-preserving permutations, that chi6dir is trace (permOp .), and
  hence that the three projector images carry chiT, chiE, chiA and are irreducible. That is this
  entry's recorded ledger delta.

  L1  the projector algebra, exactly: idempotence, pairwise orthogonality, completeness.
  L2  the dimensions 3, 2, 1, computed both as ranks and as traces — the two routes the Lean file
      identifies through trace_eq_finrank_range.
  L3  the rotation group O built explicitly as the signed axis permutations of determinant +1:
      24 elements, every one commuting with the antipode and with all three projectors.
  L4  the character of V6 at each conjugacy class, reproducing the manuscript's proof line
      E: 6, 8C3: 0, 3C2: 2, 6C2': 0, 6C4: 2.
  L5  the character inner products, giving n(A1) = n(E) = n(T1) = 1 and n(A2) = n(T2) = 0 — the
      manuscript's multiplicity computation, independently of the zero-import layer's proof of it.
  L6  COUNTERCONTROL for the label: the three-dimensional summand's character at C4 is +1, so it is
      T1; T2's value there is -1. Checked against the full character table of O.
  L7  lint: the Lean file is imported by the gated bridge root, carries no sorry, uses the ROTATION
      group's discriminant rather than CubicIsotropy's O_h, and keeps H-link as the hypothesis of a
      separate transport theorem with H-cust absent.

Usage:  python3 link_decomposition_probe.py
"""
import itertools
import os
import re
import sys
from fractions import Fraction as F

CHECKS = []


def check(label, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: {msg}", flush=True)


HERE = os.path.dirname(os.path.abspath(__file__))
BRIDGE = os.path.join(HERE, os.pardir, 'lean-mathlib')

# the six links, in the Lean file's order: (axis, sign)
LINKS = [(a, s) for a in range(3) for s in (False, True)]
IDX = {l: i for i, l in enumerate(LINKS)}
N = 6


def anti(l):
    return (l[0], not l[1])


# ----------------------------------------------------------------- exact matrices
def eye(n=N):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
            for i in range(len(A))]


def sub(A, B):
    return [[a - b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def addm(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def smul(c, A):
    return [[c * a for a in ra] for ra in A]


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def rank(A):
    M = [r[:] for r in A]
    r = 0
    for c in range(len(M[0])):
        piv = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = F(1) / M[r][c]
        M[r] = [x * inv for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
        if r == len(M):
            break
    return r


def perm_op(h):
    """The matrix of f |-> f . h, matching the Lean file's `permOp`."""
    return [[F(1) if h(LINKS[j]) == LINKS[i] else F(0) for j in range(N)] for i in range(N)]


ZERO = [[F(0)] * N for _ in range(N)]
CMAT = [[F(1) if anti(LINKS[i]) == LINKS[j] else F(0) for j in range(N)] for i in range(N)]
PT = smul(F(1, 2), sub(eye(), CMAT))
PEVEN = smul(F(1, 2), addm(eye(), CMAT))
PA = [[F(1, 6)] * N for _ in range(N)]
PE = sub(PEVEN, PA)

# ----------------------------------------------------------------- L1  the projector algebra
ok1 = mul(PT, PT) == PT and mul(PE, PE) == PE and mul(PA, PA) == PA
for A, B in ((PT, PE), (PE, PT), (PT, PA), (PA, PT), (PE, PA), (PA, PE)):
    ok1 &= mul(A, B) == ZERO
ok1 &= addm(addm(PT, PE), PA) == eye()
check("L1", ok1,
      "THE PROJECTOR ALGEBRA, exactly in rational arithmetic: all three are idempotent, all six "
      "products of distinct projectors vanish, and the three sum to the identity. That is what "
      "makes the decomposition an internal direct sum rather than a multiplicity count, and it is "
      "`PT_idem`, `PE_idem`, `PA_comp_PA`, the six orthogonality lemmas and `sum_proj`")

# ----------------------------------------------------------------- L2  the dimensions
dims = {'T': (rank(PT), trace(PT)), 'E': (rank(PE), trace(PE)), 'A': (rank(PA), trace(PA))}
ok2 = dims['T'] == (3, F(3)) and dims['E'] == (2, F(2)) and dims['A'] == (1, F(1))
ok2 &= trace(eye()) == F(6) and trace(CMAT) == F(0)
check("L2", ok2,
      f"THE DIMENSIONS 3, 2, 1, by two independent routes that the Lean file identifies through "
      f"`trace_eq_finrank_range`: the rank of each projector and its trace agree, "
      f"{dims['T'][0]}/{dims['T'][1]}, {dims['E'][0]}/{dims['E'][1]}, "
      f"{dims['A'][0]}/{dims['A'][1]}. The two inputs are tr(id) = {trace(eye())} and "
      f"tr(C) = {trace(CMAT)}, the antipodal map having no fixed link")


# ----------------------------------------------------------------- the rotation group O
def signed(sigma, eps):
    """The signed axis permutation (i, s) |-> (sigma i, s xor eps i)."""
    return lambda l: (sigma[l[0]], l[1] != eps[l[0]])


def perm_sign(sigma):
    s = 1
    for i in range(3):
        for j in range(i + 1, 3):
            if sigma[i] > sigma[j]:
                s = -s
    return s


ROT = []
for sigma in itertools.permutations(range(3)):
    for eps in itertools.product((False, True), repeat=3):
        det = perm_sign(sigma) * (-1) ** sum(eps)
        if det == 1:
            ROT.append((sigma, eps))

# ----------------------------------------------------------------- L3  the group
ok3 = len(ROT) == 24
for sigma, eps in ROT:
    h = signed(sigma, eps)
    ok3 &= all(h(anti(l)) == anti(h(l)) for l in LINKS)        # commutes with the antipode
    M = perm_op(h)
    for P in (PT, PE, PA):
        ok3 &= mul(M, P) == mul(P, M)                          # commutes with every projector
    ok3 &= len({h(l) for l in LINKS}) == N                     # is a permutation
check("L3", ok3,
      f"THE ROTATION GROUP O, built explicitly as the signed axis permutations of determinant +1: "
      f"{len(ROT)} elements. Every one commutes with the antipodal map — which is `Sym` in the Lean "
      f"file — and therefore with all three projectors, so all three images are invariant "
      f"subspaces. The Lean file proves this for EVERY antipode-preserving permutation, a group "
      f"containing O, so the decomposition holds a fortiori for O")


# ----------------------------------------------------------------- L4  the character table
def classify(sigma, eps):
    """Conjugacy class of a rotation, by its trace on R^3 and its order."""
    tr3 = sum((1 if not eps[i] else -1) for i in range(3) if sigma[i] == i)
    if tr3 == 3:
        return 'E'
    if tr3 == 0:
        return '8C3'
    if tr3 == -1:
        # C2 about an axis (3C2) or about a face diagonal (6C2')
        return '3C2' if all(sigma[i] == i for i in range(3)) else "6C2'"
    if tr3 == 1:
        return '6C4'
    return '?'


classes = {}
for sigma, eps in ROT:
    classes.setdefault(classify(sigma, eps), []).append((sigma, eps))
SIZES = {'E': 1, '8C3': 8, '3C2': 3, "6C2'": 6, '6C4': 6}
chi6 = {}
for cls, elts in classes.items():
    vals = {len([l for l in LINKS if signed(s, e)(l) == l]) for s, e in elts}
    chi6[cls] = vals.pop() if len(vals) == 1 else None
ok4 = all(len(classes[c]) == SIZES[c] for c in SIZES)
ok4 &= chi6 == {'E': 6, '8C3': 0, '3C2': 2, "6C2'": 0, '6C4': 2}
chi_c2p = chi6["6C2'"]
check("L4", ok4,
      f"THE CHARACTER OF V6 AT EACH CONJUGACY CLASS, reproducing the manuscript's proof line "
      f"exactly: E: {chi6['E']}, 8C3: {chi6['8C3']}, 3C2: {chi6['3C2']}, 6C2': {chi_c2p}, "
      f"6C4: {chi6['6C4']}, with class sizes 1, 8, 3, 6, 6 summing to 24. The character is the "
      f"fixed-link count, which is `trace_permOp` in Lean; the value 6 at the identity and 2 at C4 "
      f"are `trace_id_LV` and `trace_permOp_c4` there")

# ----------------------------------------------------------------- L5  THE DELTA: multiplicities
# the character table of O, in the class order E, 8C3, 3C2, 6C2', 6C4
IRREPS = {'A1': {'E': 1, '8C3': 1, '3C2': 1, "6C2'": 1, '6C4': 1},
          'A2': {'E': 1, '8C3': 1, '3C2': 1, "6C2'": -1, '6C4': -1},
          'E':  {'E': 2, '8C3': -1, '3C2': 2, "6C2'": 0, '6C4': 0},
          'T1': {'E': 3, '8C3': 0, '3C2': -1, "6C2'": -1, '6C4': 1},
          'T2': {'E': 3, '8C3': 0, '3C2': -1, "6C2'": 1, '6C4': -1}}
# the table must itself be a valid orthonormal set, or the multiplicities below prove nothing
ok5 = True
for a in IRREPS:
    for b in IRREPS:
        ip = F(sum(SIZES[c] * IRREPS[a][c] * IRREPS[b][c] for c in SIZES), 24)
        ok5 &= ip == (F(1) if a == b else F(0))
mult = {a: F(sum(SIZES[c] * IRREPS[a][c] * chi6[c] for c in SIZES), 24) for a in IRREPS}
ok5 &= mult == {'A1': F(1), 'A2': F(0), 'E': F(1), 'T1': F(1), 'T2': F(0)}
ok5 &= sum(mult[a] * IRREPS[a]['E'] for a in IRREPS) == 6
check("L5", ok5,
      f"THE MULTIPLICITIES, by character inner products over the 24 elements — the manuscript's own "
      f"proof route, reproduced here independently of the zero-import layer's kernel proof of it "
      f"(chi_consistent, irr_orthonormal, mult_V6). n(A1) = {mult['A1']}, n(E) = "
      f"{mult['E']}, n(T1) = {mult['T1']}, n(A2) = {mult['A2']}, n(T2) = {mult['T2']}, and the "
      f"dimensions reassemble to 3 + 2 + 1 = 6. The character table used is first verified "
      f"orthonormal in its own right, so the multiplicities rest on a checked table rather than a "
      f"quoted one")

# ----------------------------------------------------------------- L6  countercontrol on the label
ok6 = IRREPS['T1']['6C4'] == 1 and IRREPS['T2']['6C4'] == -1
# the Lean file computes the odd summand's character at C4; reproduce it here from the projector
c4 = signed((1, 0, 2), (False, True, False))     # e1 -> e2, e2 -> -e1, e3 -> e3
ok6 &= all(c4(anti(l)) == anti(c4(l)) for l in LINKS)
M4 = perm_op(c4)
chiT = trace(mul(M4, PT))
chiE = trace(mul(M4, PE))
chiA = trace(mul(M4, PA))
ok6 &= (chiT, chiE, chiA) == (F(1), F(0), F(1))
ok6 &= chiT != F(IRREPS['T2']['6C4'])
ok6 &= classify((1, 0, 2), (False, True, False)) == '6C4'
check("L6", ok6,
      f"COUNTERCONTROL FOR THE LABEL. The two three-dimensional irreducibles of O differ exactly at "
      f"the four-fold rotation: T1 has +1 there and T2 has -1. The odd summand's character at the "
      f"quarter turn e1 -> e2, e2 -> -e1 is {chiT}, so it is T1 and not T2 — this is Lean's "
      f"`char_c4_odd`. The other two read {chiE} and {chiA}, which are E's and A1's values. Getting "
      f"this wrong is the one way the decomposition can be right in dimensions and wrong in labels")

# ----------------------------------------------------------------- L6b  the model discrepancy
# The bridge's Cubic.rho acts on the six TWO-ELEMENT SUBSETS of the four body diagonals. Those are
# not the six links: a face of the cube meets every diagonal, so it determines no pair of them.
# The two representations have the same character MULTISET and differ as class functions.
def cycle_type(g):
    seen, t = [False] * 4, []
    for i in range(4):
        if seen[i]:
            continue
        c, j = 0, i
        while not seen[j]:
            seen[j] = True
            c += 1
            j = g[j]
        t.append(c)
    return tuple(sorted(t))


S4 = list(itertools.permutations(range(4)))
subs = [frozenset(c) for c in itertools.combinations(range(4), 2)]
chi_sub = {g: sum(1 for x in subs if frozenset(g[i] for i in x) == x) for g in S4}
# the six links are the cosets of a four-fold rotation subgroup, S4/C4
def cmp4(a, b):
    return tuple(a[b[i]] for i in range(4))


C4, x = [(0, 1, 2, 3)], (1, 2, 3, 0)
while x != (0, 1, 2, 3):
    C4.append(x)
    x = cmp4(x, (1, 2, 3, 0))
cos = []
for g in S4:
    c = frozenset(cmp4(g, h) for h in C4)
    if c not in cos:
        cos.append(c)
chi_lnk = {g: sum(1 for c in cos if frozenset(cmp4(g, h) for h in c) == c) for g in S4}
ok6b = sorted(chi_sub.values()) == sorted(chi_lnk.values())          # same multiset
ok6b &= any(chi_sub[g] != chi_lnk[g] for g in S4)                    # different class function
by_cls = {}
for g in S4:
    by_cls.setdefault(cycle_type(g), set()).add((chi_sub[g], chi_lnk[g]))
ok6b &= by_cls[(1, 1, 2)] == {(2, 0)}          # transpositions = 6C2': manuscript says 0
ok6b &= by_cls[(4,)] == {(0, 2)}               # four-cycles = 6C4: manuscript says 2
ok6b &= by_cls[(1, 1, 1, 1)] == {(6, 6)} and by_cls[(2, 2)] == {(2, 2)}
ok6b &= by_cls[(1, 3)] == {(0, 0)}
# the manuscript's own proof line is the SECOND column
ok6b &= chi_lnk[(0, 1, 2, 3)] == 6 and next(iter(by_cls[(4,)]))[1] == chi6['6C4']
check("L6b", ok6b,
      "THE MODEL DISCREPANCY, found by formalizing and now recorded in Lean as "
      "`char_two_subset_ne_link`. The bridge's `Cubic.rho` acts on the six TWO-ELEMENT SUBSETS of "
      "the four body diagonals; those are the six pairs of opposite edges, not the six links — a "
      "face of the cube meets every diagonal and so determines no pair of them. The two "
      "representations have the SAME character multiset, which is all the old multiset comparison "
      "ever checked, and differ as class functions: at transpositions (6C2') the two-subset "
      "character is 2 where [SM] Theorem 7's is 0, and at four-cycles (6C4) it is 0 where the "
      "manuscript's is 2. So the two-subset model carries T2 where the links carry T1 — the two "
      "three-dimensional irreducibles, swapped. The six links are the coset space S4/C4, which "
      "this section had recorded as a rejected control for having 'the same character'")

# ----------------------------------------------------------------- L7  lint
src = open(os.path.join(BRIDGE, 'OIBridge', 'LinkDecomposition.lean'), encoding='utf-8').read()
root = open(os.path.join(BRIDGE, 'OIBridge.lean'), encoding='utf-8').read()
NAMES = ('trace_permOp', 'PT_idem', 'PE_idem', 'sum_proj', 'finrank_PT', 'finrank_PE',
         'finrank_PA', 'permOp_comp_PT', 'permOp_comp_C_eq', 'charOn_PA', 'charOn_PT',
         'charOn_sum', 'char_c4_odd', 'char_c4_E', 'theorem_7', 'hlink_transport')
body = re.sub(r'(?m)--.*$', '', re.sub(r'/-.*?-/', '', src, flags=re.S))
ok7 = ('import OIBridge.LinkDecomposition' in root
       and re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', body) is None
       and re.search(r'(?m)^axiom ', body) is None
       and all(f'theorem {n}' in src for n in NAMES)
       and all(f'#print axioms {n}' in src for n in NAMES))
# the dimensions must come from the trace lemma, not from ad hoc bases
ok7 &= 'trace_eq_finrank_range' in body
# H-link is a hypothesis of a SEPARATE theorem, and H-cust appears nowhere
ok7 &= 'theorem hlink_transport' in src
tr = src[src.index('theorem hlink_transport'):]
ok7 &= 'H-cust' not in tr and 'H-cust' not in body
tr_sig = tr[:tr.index(':= by')]
ok7 &= 'e : W ≃ₗ[ℚ] LV' in tr_sig
# H-link must be EQUIVARIANT, not a bare linear equivalence: the carrier carries its own action
# and the isomorphism must intertwine it, and the conclusion must transport the projectors and
# their invariance, not only the three dimensions
ok7 &= 'act : Equiv.Perm Link → (W →ₗ[ℚ] W)' in tr_sig
ok7 &= 'permOp h ∘ₗ e.toLinearMap' in tr_sig
ok7 &= 'act h ∘ₗ QT = QT ∘ₗ act h' in tr_sig
ok7 &= 'QT + QE + QA = LinearMap.id' in tr_sig
# the O_h machinery of CubicIsotropy must not be imported into the rotational statement
ok7 &= 'CubicIsotropy' not in body
ok7 &= 'import OIBridge.CubicIsotropy' not in src
# the genuine 24-element group object, and the face/link identification, live in OIBridge.lean
ok7 &= 'namespace LinkJoin' in root
for n in ('faceEquivLink', 'faceEquivLink_op', 'act_op', 'linkHom', 'sym_linkHom',
          'act_injective', 'linkHom_injective', 'rhoLink', 'character_rhoLink',
          'rhoLink_comm_PT', 'character_restrict_PT', 'character_PA_eq_one', 'character_sum'):
    ok7 &= n in root
# the three summands must be bundled as honest Subrepresentations, so that the join is a statement
# about Representation.character and not about a restricted trace that resembles one
for n in ('Tsub', 'Esub', 'Asub', 'rhoT', 'rhoE', 'rhoA'):
    ok7 &= f'def {n}' in root
ok7 &= 'Subrepresentation rhoLink' in root and 'Subrepresentation.toRepresentation' in root
# and the section must NOT claim to be the cubic rotation action on the coordinate links
ok7 &= 'theorem char_two_subset_ne_link' in root
ok7 &= 'is NOT the six-link representation' in root
ok7 &= 'A₁ ⊕ E ⊕ T₂' in root
for n in ('character_rhoT', 'character_rhoE', 'character_rhoA', 'character_rhoA_eq_one',
          'character_rhoLink_eq_sum'):
    ok7 &= f'theorem {n}' in root
ct = root[root.index('theorem character_rhoT'):]
ok7 &= 'rhoT.character g = charOn PT' in ct[:ct.index(':=')]
# THE ORIENTATION GUARD. permOp acts by precomposition and so reverses composition order, which
# means the representation must carry the inverse. Every S4 character here satisfies chi(g^-1) =
# chi(g), so the numbers would come out right even with the orientation wrong and only a pointwise
# statement would notice -- hence a lint check rather than a numeric one.
ok7 &= 'theorem permOp_mul' in src
pm = src[src.index('theorem permOp_mul'):]
ok7 &= 'permOp (h₁ * h₂) = permOp h₂ ∘ₗ permOp h₁' in pm[:pm.index(':= by')]
rl = root[root.index('noncomputable def rhoLink'):]
ok7 &= 'permOp (linkHom g⁻¹)' in rl[:rl.index('theorem rhoLink_apply')]
check("L7", ok7,
      f"the Lean file is IMPORTED BY OIBridge.lean, so CI builds it; it carries no `sorry` and no "
      f"`axiom`; all {len(NAMES)} named results print their axiom dependencies; the dimensions come "
      f"from `trace_eq_finrank_range` rather than from ad hoc bases, so the infrastructure lemma is "
      f"validated in its intended consumer; H-link appears only as the hypothesis of the separate "
      f"`hlink_transport`, and that hypothesis is EQUIVARIANT — the carrier carries its own action, "
      f"the isomorphism intertwines it, and what transports is the projectors and their invariance "
      f"rather than three bare dimensions; H-cust appears nowhere; and `CubicIsotropy` is neither "
      f"imported nor mentioned, so its 48-element O_h cannot be substituted for the 24-element "
      f"rotation group; and OIBridge.lean's LinkJoin is explicitly NOT claimed to be the rotation "
      f"action on the coordinate links — `char_two_subset_ne_link` records in Lean that the "
      f"two-subset model differs from Theorem 7's character at the transpositions and the "
      f"four-fold class, so nothing there can be read as V6")

print()
print('     [scope] Settled in Lean: three explicit projectors on the six-link space, idempotent,')
print('     pairwise orthogonal and summing to the identity, commuting with every symmetry of the')
print('     link set; dimensions 3, 2, 1 read off their traces through the IdempotentTrace lemma;')
print('     and the character at a four-fold rotation, 1 for the three-dimensional summand, which')
print('     is T1\'s value and not T2\'s. H-link is the hypothesis of a separate transport theorem.')
print('     Also settled, in the ZERO-IMPORT layer: the manuscript\'s own proof line — the fixed')
print('     directed-link count equals chiT + chiE + chiA, the five irreducible characters are')
print('     orthonormal over the 24 rotations, and the inner products give 24*(1,0,1,1,0).')
print('     NOT settled, and this entry\'s recorded delta: the JOIN between those two layers —')
print('     that the zero-import encoding of the rotations is this file\'s group, that chi6dir is')
print('     trace(permOp .), and hence that the three projector images carry those characters and')
print('     are irreducible. Also outstanding: the six-face/six-link equivariant identification,')
print('     which OIBridge.lean\'s Cubic section still records as probe-only.')
print()
print("link_decomposition_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
