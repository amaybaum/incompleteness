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

  THE JOIN, which used to be this entry's recorded delta, is now made inside the Mathlib bridge
  rather than across the two gates: OIBridge/QuarterTurn.lean carries a genuine 24-element group —
  S4 acting by conjugation on its six four-cycles, the six quarter turns — whose image is PROVED to
  be exactly the determinant-+1 antipode-preserving permutations of the six signed links, so the
  name "rotation group" is a theorem there and not a convention. Its fixed-link character is the
  manuscript's own (6, 0, 2, 0, 2), the multiplicities are computed against that derived character,
  the three summands are Subrepresentations with characters T1, E, A1, each irreducible over Q in
  the strict sense — no proper nonzero subrepresentation, reached from dim End = 1 through Maschke,
  since Mathlib carries that implication only for algebraically closed fields — and the terminal
  equivalence is equivariant. The zero-import layer's arithmetic is now a second independent
  witness rather than a load-bearing half.

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
  L6b COUNTERCONTROL for the model: the two-subset action is NOT the six-link one, and carries T2
      where the links carry T1.
  L6c the collision that hid it — same multiset, same sum of squares (72) and cubes (288) — kept as
      a permanent regression control.
  L6d the quarter-turn construction and its ACCEPTANCE GATE: the fixed-point character of S4 acting
      by conjugation on its six four-cycles is the manuscript's (6, 0, 2, 0, 2).
  L6e the representation against that gated action: five orthonormal characters, multiplicities
      24*(1,0,1,1,0), the pointwise split, and self-inner-products 24 giving dim End = 1 over Q.
  L6g COUNTERCONTROL for the Maschke step: an algebra with a one-dimensional endomorphism algebra
      whose module is nonetheless reducible, so `dim End = 1` alone is not irreducibility.
  L6f the NAME certified rather than asserted: 48 antipode-preserving permutations, 24 of them of
      determinant +1, and the image of the action is exactly those 24 — the inversion excluded.
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

# ------------------------------------------------- L6c  why the old evidence was blind
sq_sub = sum(v ** 2 for v in chi_sub.values())
sq_lnk = sum(v ** 2 for v in chi_lnk.values())
cb_sub = sum(v ** 3 for v in chi_sub.values())
cb_lnk = sum(v ** 3 for v in chi_lnk.values())
ok6c = sq_sub == sq_lnk == 72 and cb_sub == cb_lnk == 288
ok6c &= sorted(chi_sub.values()) == sorted(chi_lnk.values())
# the two differing classes both have six elements, which is why the contributions trade places
ok6c &= len([g for g in S4 if cycle_type(g) == (1, 1, 2)]) == 6
ok6c &= len([g for g in S4 if cycle_type(g) == (4,)]) == 6
# a control: the sums DO separate representations in general, so this collision is a fact about
# these two and not a vacuous observation about power sums
chi_reg = {g: (24 if g == (0, 1, 2, 3) else 0) for g in S4}          # the regular representation
ok6c &= sum(v ** 2 for v in chi_reg.values()) != 72
check("L6c", ok6c,
      f"WHY THE PREVIOUS EVIDENCE WAS BLIND, and now a permanent regression control. The two "
      f"characters agree as multisets AND on the aggregate power sums this bridge reports: "
      f"sum(chi^2) = {sq_sub} for both, sum(chi^3) = {cb_sub} for both. The two classes where they "
      f"differ, 6C2' and 6C4, both have six elements, so the contributions simply trade places. So "
      f"neither the old multiset comparison nor the 72/288 certificates could ever have "
      f"distinguished them — and those numbers being right is not evidence that the physical "
      f"representation was right. Lean records all three as `char_multiset_collision`, "
      f"`sum_sq_collision` and `sum_cube_collision`. The control confirms the power sums are not "
      f"vacuous: the regular representation gives a different value")

# ------------------------------------------------- L6d  the quarter-turn construction
# The six four-cycles of S4 ARE the six quarter turns, hence the six oriented axes. S4 acts on them
# by conjugation; the stabilizer is the centralizer C4, so the orbit is S4/C4 with no quotient; and
# q -> q^-1 is the antipode. This is the construction OIBridge/QuarterTurn.lean formalizes.
def inv4(g):
    h = [0] * 4
    for i in range(4):
        h[g[i]] = i
    return tuple(h)


QTs = [g for g in S4 if cycle_type(g) == (4,)]
ok6d = len(QTs) == 6
# conjugation is an action on them, and the stabilizer of each is its centralizer, of order 4
for q in QTs:
    ok6d &= all(cycle_type(cmp4(cmp4(g, q), inv4(g))) == (4,) for g in S4)
    stab = [g for g in S4 if cmp4(cmp4(g, q), inv4(g)) == q]
    ok6d &= len(stab) == 4
    ok6d &= inv4(q) in QTs and inv4(q) != q
# q -> q^-1 is a fixed-point-free involution: the three axes, two orientations each
ok6d &= len({frozenset({q, inv4(q)}) for q in QTs}) == 3
# and conjugation commutes with it, which is what makes every rotation a link symmetry
for q in QTs:
    ok6d &= all(cmp4(cmp4(g, inv4(q)), inv4(g)) == inv4(cmp4(cmp4(g, q), inv4(g))) for g in S4)
# THE GATE: the fixed-point character of this action is the manuscript's (6, 0, 2, 0, 2)
chi_qt = {g: sum(1 for q in QTs if cmp4(cmp4(g, q), inv4(g)) == q) for g in S4}
gate = {}
for g in S4:
    gate.setdefault(cycle_type(g), set()).add(chi_qt[g])
ok6d &= gate == {(1, 1, 1, 1): {6}, (1, 3): {0}, (2, 2): {2}, (1, 1, 2): {0}, (4,): {2}}
ok6d &= all(chi_qt[g] == chi_lnk[g] for g in S4)          # it IS the S4/C4 character
ok6d &= any(chi_qt[g] != chi_sub[g] for g in S4)          # and NOT the two-subset one
check("L6d", ok6d,
      f"THE QUARTER-TURN CONSTRUCTION AND ITS ACCEPTANCE GATE. The {len(QTs)} four-cycles of S4 are "
      f"the six quarter turns, hence the six oriented axes. Conjugation permutes them, each "
      f"stabilizer is the centralizer of order 4 so the orbit is S4/C4 with no quotient "
      f"formalized, and q -> q^-1 is a fixed-point-free involution pairing them into the three "
      f"axes and commuting with the action. THE GATE: the fixed-point character is "
      f"(6, 0, 2, 0, 2) on (E, 8C3, 3C2, 6C2', 6C4) — [SM] Theorem 7's own proof line. It agrees "
      f"with the S4/C4 character everywhere and differs from the two-subset one, so this is the "
      f"correct S4-set. Lean proves the same as `QuarterTurn.character_gate`")

# ------------------------------------------------- L6e  the representation, against the gate
def sgn4(g):
    s = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if g[i] > g[j]:
                s = -s
    return s


def nfix4(g):
    return sum(1 for i in range(4) if g[i] == i)


L2Q = {}
for q in QTs:
    v = q[q[0]]
    ax = 0 if v == 1 else (1 if v == 2 else 2)
    L2Q[(ax, inv4(q)[0] < q[0])] = q
ok6e = len(L2Q) == 6


def act_on_link(g, l):
    q = L2Q[l]
    r = cmp4(cmp4(g, q), inv4(g))
    v = r[r[0]]
    ax = 0 if v == 1 else (1 if v == 2 else 2)
    return (ax, inv4(r)[0] < r[0])


def fix3(g):
    return sum(1 for a in range(3) if act_on_link(g, (a, False))[0] == a)


CH = {'A1': lambda g: 1, 'A2': sgn4, 'E': lambda g: fix3(g) - 1,
      'T1': lambda g: sgn4(g) * (nfix4(g) - 1), 'T2': lambda g: nfix4(g) - 1}
for a in CH:
    for b in CH:
        ip = sum(CH[a](g) * CH[b](g) for g in S4)
        ok6e &= ip == (24 if a == b else 0)
mult = {a: sum(chi_lnk[g] * CH[a](g) for g in S4) for a in CH}
ok6e &= mult == {'A1': 24, 'A2': 0, 'E': 24, 'T1': 24, 'T2': 0}
ok6e &= all(chi_lnk[g] == CH['T1'](g) + CH['E'](g) + CH['A1'](g) for g in S4)
# the odd summand's character from the two fixed-point counts, as charOn_PT reduces it
fixLA = {g: sum(1 for l in L2Q if act_on_link(g, l) == (l[0], not l[1])) for g in S4}
ok6e &= all(chi_lnk[inv4(g)] - fixLA[g] == 2 * CH['T1'](g) for g in S4)
# the label discriminator
c4g = (1, 2, 3, 0)
ok6e &= CH['T1'](c4g) == 1 and CH['T2'](c4g) == -1
# irreducibility: each self-inner-product is 24, so dim End = 1
ok6e &= all(sum(CH[a](g) * CH[a](inv4(g)) for g in S4) == 24 for a in ('T1', 'E', 'A1'))
check("L6e", ok6e,
      f"THE REPRESENTATION, against the gated action. The five S4 characters — A1 = 1, A2 = sign, "
      f"E = fix3 - 1, T1 = sign*(fix4 - 1), T2 = fix4 - 1 — are orthonormal over the 24 elements; "
      f"the multiplicities of the link character are 24*(1,0,1,1,0), so no A2 and no T2; the "
      f"character splits pointwise as T1 + E + A1; and the odd summand's two fixed-point counts "
      f"give 2*T1 exactly, which is the reduction `charOn_PT` performs in Lean. The label "
      f"discriminator: at the four-cycle class T1 = 1 and T2 = -1, so the three-dimensional "
      f"summand is T1. Each self-inner-product is 24, giving dim End = 1 over Q, with no "
      f"complexification — which becomes irreducibility only through Maschke, the step L6g shows "
      f"is load-bearing")

# ------------------------------------------------- L6g  countercontrol for the Maschke step
# `dim End = 1` is an arithmetic fact about characters; irreducibility is a statement about
# subrepresentations. The implication between them is Maschke, and this check shows Maschke is
# load-bearing rather than decorative: an algebra whose module has a one-dimensional endomorphism
# algebra and a proper nonzero invariant subspace at the same time. Nothing about the module is
# wrong; what fails is semisimplicity, which is exactly the hypothesis the new Lean lemma carries.
def nullity(rows, n):
    """Dimension of the solution space of `rows . x = 0`, exactly, over the rationals."""
    m = [list(map(F, r)) for r in rows]
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, len(m)) if m[i][c] != 0), None)
        if p is None:
            continue
        m[r], m[p] = m[p], m[r]
        inv = F(1) / m[r][c]
        m[r] = [inv * v for v in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [a - f * b for a, b in zip(m[i], m[r])]
        piv.append(c)
        r += 1
    return n - len(piv)


def commutant_dim(gens, n):
    """Dimension of {X : X A = A X for every generator A}, for n x n matrices."""
    rows = []
    for A in gens:
        for i in range(n):
            for j in range(n):
                # coefficient of x_{pq} in (XA - AX)_{ij}
                row = [F(0)] * (n * n)
                for q in range(n):
                    row[i * n + q] += F(A[q][j])          # (X A)_{ij} = sum_q x_{iq} A_{qj}
                for p in range(n):
                    row[p * n + j] -= F(A[i][p])          # (A X)_{ij} = sum_p A_{ip} x_{pj}
                rows.append(row)
    return nullity(rows, n * n)


E11 = [[1, 0], [0, 0]]
E12 = [[0, 1], [0, 0]]
E22 = [[0, 0], [0, 1]]
UT = [E11, E12, E22]                       # the upper-triangular algebra acting on k^2
ok6g = commutant_dim(UT, 2) == 1           # one-dimensional endomorphism algebra ...
# ... and yet span(e1) is a proper nonzero invariant subspace: the module is NOT simple
ok6g &= all(A[1][0] == 0 for A in UT)      # every generator maps e1 into span(e1)
# controls that the routine is not degenerate: the full matrix algebra also has commutant k
# (and is simple), while a scalar-only algebra has the whole 4-dimensional commutant
ok6g &= commutant_dim(UT + [[[0, 0], [1, 0]]], 2) == 1
ok6g &= commutant_dim([[[1, 0], [0, 1]]], 2) == 4
# the hypothesis that rescues the implication here: |O| = 24 is invertible in Q, so Maschke applies
ok6g &= F(24) != 0 and F(1) / F(24) * F(24) == 1
check("L6g", ok6g,
      "COUNTERCONTROL FOR THE MASCHKE STEP. `dim End = 1` does NOT by itself give irreducibility. "
      "The upper-triangular 2x2 algebra acting on k^2 has a ONE-dimensional endomorphism algebra — "
      "commuting with E11 and E22 forces a diagonal matrix, and commuting with E12 forces its two "
      "entries equal — and yet span(e1) is a proper nonzero invariant subspace, so the module is "
      "not simple. What fails there is semisimplicity, and that is precisely the hypothesis "
      "`OIBridge/Irreducibility.lean` carries: over Q the group order 24 is invertible, Maschke "
      "gives every subrepresentation an invariant complement, and only then does the projection "
      "onto a summand become an endomorphism that a one-dimensional End can pin down. Controls: "
      "the full matrix algebra also gives commutant dimension 1, and the scalars alone give 4, so "
      "the routine separates cases rather than always reporting 1")

# ------------------------------------------------- L6f  the name is certified, not asserted
# Calling the acting group "the cubic rotation group" is a naming claim, and a wrong naming claim is
# exactly what L6b caught. So it is checked: a signed permutation of the three axes is a rotation iff
# its 3x3 matrix has determinant +1, and the image of the conjugation action is precisely that set.
LINKS = [(a, s) for a in range(3) for s in (False, True)]


def det_link(h):
    col = {}
    for j in range(3):
        ax, sg = h[(j, True)]
        col[j] = (ax, 1 if sg else -1)
    M = [[0] * 3 for _ in range(3)]
    for j in range(3):
        M[col[j][0]][j] = col[j][1]
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


allperm = [dict(zip(LINKS, p)) for p in itertools.permutations(LINKS)]
ok6f = len(allperm) == 720
sym = [h for h in allperm if all(h[(a, not s)] == (h[(a, s)][0], not h[(a, s)][1])
                                 for (a, s) in LINKS)]
rot = [h for h in sym if det_link(h) == 1]
ok6f &= len(sym) == 48 and len(rot) == 24                     # O_h has 48, O has 24
inversion = {l: (l[0], not l[1]) for l in LINKS}
ok6f &= inversion in sym and det_link(inversion) == -1        # -I is in O_h and not in O
image = [{l: act_on_link(g, l) for l in LINKS} for g in S4]
ok6f &= len({tuple(sorted(h.items())) for h in image}) == 24   # faithful
ok6f &= {tuple(sorted(h.items())) for h in image} == {tuple(sorted(h.items())) for h in rot}
# a control: det is not vacuous here — the 24 non-rotations are exactly the other coset
ok6f &= len([h for h in sym if det_link(h) == -1]) == 24
check("L6f", ok6f,
      f"THE NAME IS CERTIFIED, NOT ASSERTED. Of the {len(allperm)} permutations of the six signed "
      f"links, {len(sym)} preserve antipodality — that is O_h — and exactly {len(rot)} of those have "
      f"determinant +1 in the 3x3 signed-permutation matrix, which is the definition of a rotation. "
      f"The image of the conjugation action is faithful and coincides with that 24-element set "
      f"exactly, so the group really is O and not some other index-2 subgroup of O_h, and not O_h "
      f"itself. The concrete separator: the inversion -I preserves antipodality and has determinant "
      f"-1, so it is in O_h and not in the image. Lean proves the same as `QuarterTurn.isRot_iff`, "
      f"`card_sym`, `card_rot` and `antiPerm_not_isRot` — the check whose absence let a group object "
      f"be named for geometry it did not have")

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
for n in ('char_two_subset_ne_link', 'char_multiset_collision', 'sum_sq_collision',
          'sum_cube_collision'):
    ok7 &= f'theorem {n}' in root
ok7 &= 'is NOT the six-link representation' in root
ok7 &= 'A₁ ⊕ E ⊕ T₂' in root
# chiLinkTable is no longer a transcription: it is the character of a real action
ok7 &= 'abbrev chiLinkTable : Perm (Fin 4) → ℤ := QuarterTurn.chiLink' in root
qt = open(os.path.join(BRIDGE, 'OIBridge', 'QuarterTurn.lean'), encoding='utf-8').read()
qtbody = re.sub(r'(?m)--.*$', '', re.sub(r'/-.*?-/', '', qt, flags=re.S))
ok7 &= 'import OIBridge.QuarterTurn' in root
ok7 &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', qtbody) is None
ok7 &= re.search(r'(?m)^axiom ', qtbody) is None
for n in ('card_QT', 'conjHom', 'qtEquivLink_inv', 'sym_linkAct', 'linkAct_injective',
          'character_gate', 'character_values', 'card_sym', 'card_rot', 'isRot_iff',
          'antiPerm_not_isRot', 'theorem_7_link'):
    ok7 &= f'#print axioms {n}' in qt
# THE NAMING GUARD. The acting group must be certified to BE the rotation group rather than merely
# called one -- the failure mode that admitted the two-subset model. The determinant must be tied to
# Mathlib's, so the hand-written expansion cannot drift into a different polynomial.
for n in ('detLink_eq_det', 'card_sym', 'card_rot', 'antiPerm_not_isRot', 'isRot_iff'):
    ok7 &= f'theorem {n}' in qt
dd = qt[qt.index('theorem detLink_eq_det'):]
ok7 &= 'detLink h = (linkMat h).det' in dd[:dd.index(':= by')]
ir = qt[qt.index('theorem isRot_iff'):]
ok7 &= 'IsRot h ↔ ∃ g : Perm (Fin 4), linkAct g = h' in ir[:ir.index(':= by')]
ok7 &= 'def IsRot (h : Perm Link) : Prop := Sym h ∧ detLink h = 1' in qtbody
# and the wrapper must carry that certificate, not leave it to one side
tw = qt[qt.index('theorem theorem_7_link'):]
sig = tw[:tw.index('⟨isRot_iff')]
ok7 &= 'IsRot h ↔ ∃ g : Perm (Fin 4), linkAct g = h' in sig
# THE MASCHKE GUARD. `dim End = 1` is not irreducibility, and the wrapper must claim the latter:
# `Representation.IsIrreducible` is "no proper nonzero subrepresentation", and the implication from
# the endomorphism dimension is Maschke, proved separately and WITHOUT an algebraically closed
# field -- Mathlib carries only the converse, under `[IsAlgClosed k]`.
for n in ('irreducible_rhoT', 'irreducible_rhoE', 'irreducible_rhoA'):
    ok7 &= f'theorem {n} : Representation.IsIrreducible' in qt
    ok7 &= f'#print axioms {n}' in qt
ok7 &= 'Representation.IsIrreducible rhoT ∧ Representation.IsIrreducible rhoE' in sig
irr = open(os.path.join(BRIDGE, 'OIBridge', 'Irreducibility.lean'), encoding='utf-8').read()
irrbody = re.sub(r'(?m)--.*$', '', re.sub(r'/-.*?-/', '', irr, flags=re.S))
ok7 &= 'import OIBridge.Irreducibility' in root and 'import OIBridge.Irreducibility' in qt
ok7 &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', irrbody) is None
ok7 &= re.search(r'(?m)^axiom ', irrbody) is None
ok7 &= 'IsAlgClosed' not in irrbody              # the whole point: no algebraically closed field
for n in ('complementedLattice', 'projMap_equivariant',
          'isIrreducible_of_finrank_intertwiners_eq_one'):
    ok7 &= f'theorem {n}' in irr and f'#print axioms {n}' in irr
mi = irr[irr.index('theorem isIrreducible_of_finrank_intertwiners_eq_one'):]
misig = mi[:mi.index(':= by')]
ok7 &= 'Module.finrank k (IntertwiningMap ρ ρ) = 1' in misig and 'IsIrreducible ρ' in misig
# and Maschke must come from Mathlib's semisimplicity rather than be assumed
ok7 &= 'isSemisimpleRepresentation_iff_isSemisimpleModule_asModule' in irrbody
# the gate must be the pointwise identity, not a spot check
cg = qt[qt.index('theorem character_gate'):]
ok7 &= '∀ g : Perm (Fin 4), (fixLink g : ℤ) = chiLink g' in cg[:cg.index(':= by')]
# and the action must be conjugation on four-cycles, with the inverse as antipode
ok7 &= 'MulAut.conj' in qtbody and 'q ^ 4 = 1 ∧ q ^ 2 ≠ 1' in qtbody
ok7 &= 'theorem qtEquivLink_inv' in qt and 'anti (qtEquivLink q)' in qt
ok7 &= 'native_decide' not in qtbody
# the representation must be built on the GATED action, with a fresh name
for n in ('rhoLinkQT', 'TsubQT', 'EsubQT', 'AsubQT', 'rhoT', 'rhoE', 'rhoA', 'decompEquiv'):
    ok7 &= f'def {n}' in qt
rq = qt[qt.index('def rhoLinkQT'):]
ok7 &= 'permOp (linkAct g⁻¹)' in rq[:rq.index('theorem rhoLinkQT_apply')]
for n in ('irr_orthonormal', 'mult_link', 'character_rhoT_eq', 'character_rhoE_eq',
          'character_rhoA_eq', 'finrank_end_rhoT', 'finrank_end_rhoE', 'finrank_end_rhoA',
          'chiT_c4', 'decompEquiv_equivariant', 'theorem_7_link'):
    ok7 &= f'theorem {n}' in qt
# the terminal wrapper must be an EQUIVARIANT equivalence, not a conjunction of projector facts
de = qt[qt.index('theorem decompEquiv_equivariant'):]
ok7 &= 'decompEquiv (rhoLinkQT g v)' in de[:de.index(':= by')]
ok7 &= 'rhoT g (decompEquiv v).1' in de[:de.index(':= by')]
# T1 must be standard-tensor-sign, not the standard representation
ct = qt[qt.index('def chiT1'):]
ok7 &= 'sgnZ g * ((nfix g : ℤ) - 1)' in ct[:ct.index('def chiT2')]
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
      f"four-fold class, so nothing there can be read as V6; and OIBridge/QuarterTurn.lean builds "
      f"the CORRECT action — conjugation on the six four-cycles, antipode q -> q^-1, faithful, "
      f"every element in `Sym` — whose `character_gate` is the pointwise identity with the "
      f"manuscript's character, so `chiLinkTable` is now derived rather than transcribed; and that "
      f"action's group is certified to BE the rotation group by `isRot_iff`, `card_sym`, `card_rot` "
      f"and `antiPerm_not_isRot`, with `detLink_eq_det` tying the hand-written determinant to "
      f"Mathlib's so the criterion cannot drift, and the certificate is a clause of the wrapper; "
      f"and the wrapper claims `Representation.IsIrreducible` — no proper nonzero subrepresentation "
      f"— not merely `dim End = 1`, with the implication supplied by OIBridge/Irreducibility.lean, "
      f"which mentions no algebraically closed field and takes its semisimplicity from Mathlib's "
      f"Maschke rather than assuming it")

print()
print('     [scope] Settled in Lean: three explicit projectors on the six-link space, idempotent,')
print('     pairwise orthogonal and summing to the identity, commuting with every symmetry of the')
print('     link set; dimensions 3, 2, 1 read off their traces through the IdempotentTrace lemma;')
print('     and the character at a four-fold rotation, 1 for the three-dimensional summand, which')
print('     is T1\'s value and not T2\'s. H-link is the hypothesis of a separate transport theorem.')
print('     THE JOIN IS NOW SETTLED TOO, inside the Mathlib bridge: OIBridge/QuarterTurn.lean acts')
print('     with a genuine 24-element group whose image is proved to be exactly the determinant-+1')
print('     antipode-preserving permutations of the six signed links — the rotation group, named by')
print('     theorem and not by convention — whose fixed-link character is the manuscript\'s own')
print('     (6, 0, 2, 0, 2); the five S4 characters are orthonormal there, the multiplicities are')
print('     24*(1,0,1,1,0) against that DERIVED character, the three summands are Subrepresentations')
print('     with characters T1, E and A1, each IRREDUCIBLE over Q — no proper nonzero')
print('     subrepresentation, not merely dim End = 1: the implication between those two is')
print('     Maschke, proved in OIBridge/Irreducibility.lean without an algebraically closed field,')
print('     which is the direction Mathlib does not carry — and the terminal equivalence')
print('     V6 = T1 + E + A1 is equivariant.')
print('     NOT settled, and recorded separately as the A10 gap: the six-face/six-link equivariant')
print('     identification, and OIBridge.lean\'s Cubic section — whose 72, 288 and 144 are')
print('     statements about the two-subset action, not about these links.')
print()
print("link_decomposition_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
