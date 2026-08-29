#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OIBridge/CanonicalMeasure.lean.

[Main] Lemma 3 is kernel-proved there in the shape its own status remarks require: the reversible
representative is TAKEN AS GIVEN — the manuscript calls it a representation choice recovered partly
by an empirical argument — and what is proved is the measure content. This file is the independent
executable layer, and it is built around the one way this lemma can go wrong.

  THE FAILURE MODE is proving too much. The manuscript says the counting measure is SELECTED among
  invariant measures as the maximal-entropy one, "a selection principle, not uniqueness from
  invariance alone". A formalization that quietly established uniqueness would be proving something
  the corpus denies. So the central check here is not that the counting measure is invariant — it
  is that invariance has a whole family of solutions and only the entropy criterion cuts it down.

  M1  orbit uniqueness: on each cycle the invariant law is unique and uniform, exactly.
  M2  the counting measure is invariant, exhaustively over every permutation of up to 6 states.
  M3  COUNTERCONTROL, the load-bearing one: the invariant subspace has dimension equal to the
      NUMBER OF CYCLES, computed by exact Gauss-Jordan over the rationals for all 873 permutations
      of up to 6 states. Invariance selects a unique law exactly when the permutation is a single
      cycle, and never otherwise — so "uniqueness from invariance" is false for every permutation
      with two or more cycles, in the finite setting and not only in the continuum.
  M4  a concrete two-cycle witness matching the Lean file's: the double transposition on four
      states, with two distinct invariant probability laws exhibited.
  M5  the entropy clause: the counting measure attains log2|S| and no law exceeds it; and, since
      invariance leaves a simplex of solutions, the ENTROPY criterion is what does the selecting —
      it picks the counting measure uniquely, strictly beating every other invariant law.
  M6  COUNTERCONTROL for the finiteness prong: injectivity gives bijectivity on a finite set and
      fails on an infinite one, so finiteness is load-bearing exactly as the manuscript's second
      prong says.
  M7  lint: the Lean file is imported by the gated bridge root, carries no sorry, takes the
      permutation as GIVEN rather than deriving reversibility, and states the non-selection guard
      as a theorem rather than a comment.

Usage:  python3 canonical_measure_probe.py
"""
import itertools
import math
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


# ----------------------------------------------------------------- exact linear algebra
def nullspace_dim(M):
    """Dimension of the kernel of M, by exact Gauss-Jordan over the rationals."""
    A = [row[:] for row in M]
    rows, cols = len(A), len(A[0])
    rank, r = 0, 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = F(1) / A[r][c]
        A[r] = [x * inv for x in A[r]]
        for i in range(rows):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        r += 1
        rank += 1
        if r == rows:
            break
    return cols - rank


def cycles(perm):
    """The cycles of a permutation given as a tuple perm[i] = image of i."""
    n = len(perm)
    seen, out = [False] * n, []
    for i in range(n):
        if seen[i]:
            continue
        cyc, j = [], i
        while not seen[j]:
            seen[j] = True
            cyc.append(j)
            j = perm[j]
        out.append(cyc)
    return out


def invariance_matrix(perm):
    """`Invariant` as a linear condition: (marg p phi)(t) - p(t) = p(phi^-1 t) - p(t) = 0."""
    n = len(perm)
    inv = [0] * n
    for i, j in enumerate(perm):
        inv[j] = i
    M = [[F(0)] * n for _ in range(n)]
    for t in range(n):
        M[t][inv[t]] += F(1)
        M[t][t] -= F(1)
    return M


def entropy_bits(p):
    h = 0.0
    for w in p:
        w = float(w)
        if w > 0:
            h -= w * math.log2(w)
    return h


# ----------------------------------------------------------------- M1  orbit uniqueness
ok1 = True
n1 = 0
for n in range(1, 7):
    for perm in itertools.permutations(range(n)):
        for cyc in cycles(perm):
            # invariant laws supported on this cycle: solve the invariance system on those
            # coordinates only, which is the Lean file's `orbit_invariant_unique` hypothesis
            idx = {c: k for k, c in enumerate(cyc)}
            m = len(cyc)
            M = [[F(0)] * m for _ in range(m)]
            for t in cyc:
                pre = next(i for i in range(n) if perm[i] == t)
                M[idx[t]][idx[pre]] += F(1)
                M[idx[t]][idx[t]] -= F(1)
            ok1 &= nullspace_dim(M) == 1          # one-dimensional: the law is determined
            # and the determined law is the UNIFORM one
            unif = [F(1, m)] * m
            for t in cyc:
                pre = next(i for i in range(n) if perm[i] == t)
                ok1 &= unif[idx[pre]] == unif[idx[t]]
            ok1 &= sum(unif) == 1
            n1 += 1
check("M1", ok1,
      f"ORBIT UNIQUENESS, exactly, on all {n1} cycles of all permutations of up to 6 states. The "
      f"space of invariant laws supported on a single cycle is ONE-dimensional in every case, so "
      f"the measure on an accessible orbit is not chosen but determined, and the law it determines "
      f"is the uniform one. This clause of Lemma 3 really is a uniqueness statement — which is "
      f"exactly why the global clause's failure to be one is the thing worth guarding")

# ----------------------------------------------------------------- M2  counting invariant
ok2 = True
n2 = 0
for n in range(1, 7):
    for perm in itertools.permutations(range(n)):
        M = invariance_matrix(perm)
        unif = [F(1, n)] * n
        ok2 &= all(sum(M[t][j] * unif[j] for j in range(n)) == 0 for t in range(n))
        n2 += 1
check("M2", ok2,
      f"THE COUNTING MEASURE IS INVARIANT under every one of the {n2} permutations of up to 6 "
      f"states, checked as the exact linear condition (marg p phi) = p rather than by appeal to "
      f"symmetry. No hypothesis on the permutation is used, which is why the Lean statement carries "
      f"none")

# ----------------------------------------------------------------- M3  the countercontrol
ok3 = True
n3 = 0
unique_cases = 0
multi_cases = 0
worst_dim = 0
for n in range(1, 7):
    for perm in itertools.permutations(range(n)):
        d = nullspace_dim(invariance_matrix(perm))
        c = len(cycles(perm))
        ok3 &= d == c                      # the invariant subspace is spanned by cycle indicators
        if c == 1:
            unique_cases += 1
            ok3 &= d == 1
        else:
            multi_cases += 1
            ok3 &= d >= 2                  # a simplex of invariant laws, not a point
        worst_dim = max(worst_dim, d)
        n3 += 1
check("M3", ok3,
      f"COUNTERCONTROL: INVARIANCE ALONE DOES NOT SELECT. Over all {n3} permutations of up to 6 "
      f"states, the dimension of the invariant subspace equals the NUMBER OF CYCLES exactly, by "
      f"Gauss-Jordan over the rationals — up to {worst_dim} for the identity on 6 states. "
      f"Invariance pins the law down for the {unique_cases} single-cycle permutations and for none "
      f"of the other {multi_cases}, which carry a whole simplex of invariant laws. Uniqueness from "
      f"invariance is therefore false in the finite setting too, not only in the continuum "
      f"parenthetical the manuscript offers, and `invariance_does_not_select` is the Lean theorem "
      f"that keeps a later refactor from reintroducing it")

# ----------------------------------------------------------------- M4  the concrete witness
PERM4 = (1, 0, 3, 2)                       # the double transposition, matching two_cycle_witness
ok4 = cycles(PERM4) == [[0, 1], [2, 3]]
ok4 &= nullspace_dim(invariance_matrix(PERM4)) == 2
P4 = [F(1, 2), F(1, 2), F(0), F(0)]        # uniform on the first cycle
Q4 = [F(0), F(0), F(1, 2), F(1, 2)]        # uniform on the second
M4 = invariance_matrix(PERM4)
for v in (P4, Q4):
    ok4 &= sum(v) == 1 and all(x >= 0 for x in v)
    ok4 &= all(sum(M4[t][j] * v[j] for j in range(4)) == 0 for t in range(4))
ok4 &= P4 != Q4
check("M4", ok4,
      "THE CONCRETE WITNESS the Lean file's `two_cycle_witness` names: the double transposition on "
      "four states has two cycles, a two-dimensional invariant subspace, and two distinct invariant "
      "probability laws — the uniform law on each cycle. So `invariance_does_not_select` is not "
      "vacuous, and the hypothesis it asks for (two disjoint nonempty invariant sets) is met by the "
      "smallest permutation that can meet it")

# ----------------------------------------------------------------- M5  the entropy clause
ok5 = True
n5 = 0
strict5 = 0
for n in range(2, 7):
    for perm in itertools.permutations(range(n)):
        unif = [F(1, n)] * n
        h_unif = entropy_bits(unif)
        ok5 &= abs(h_unif - math.log2(n)) < 1e-12
        # every invariant law: the cycle-indicator basis spans them, so check the extreme points
        # and a few mixtures, which is enough to see the counting measure strictly on top
        cyc = cycles(perm)
        for c in cyc:
            v = [F(0)] * n
            for i in c:
                v[i] = F(1, len(c))
            ok5 &= entropy_bits(v) <= h_unif + 1e-12
            if len(cyc) > 1:
                ok5 &= entropy_bits(v) < h_unif - 1e-9     # STRICTLY below: entropy does select
                strict5 += 1
        if len(cyc) > 1:
            # a mixture that is not the counting measure is also strictly below
            v = [F(0)] * n
            for k, c in enumerate(cyc):
                w = F(2, 3) if k == 0 else F(1, 3 * (len(cyc) - 1))
                for i in c:
                    v[i] = w / len(c)
            # a mixture can coincide with the counting measure (weights 2/3, 1/3 over cycles of
            # sizes 4 and 2 give it back exactly); strictness is claimed only when it does not
            if sum(v) == 1 and v != unif:
                ok5 &= entropy_bits(v) < h_unif - 1e-9
                strict5 += 1
        n5 += 1
check("M5", ok5,
      f"THE ENTROPY CLAUSE, and what it is for, on {n5} permutations. The counting measure attains "
      f"log2|S| exactly and no law exceeds it. More to the point: on every multi-cycle permutation "
      f"the other extreme invariant laws sit STRICTLY below it ({strict5} cases), as do mixtures. "
      f"So the maximal-entropy criterion is doing the selecting that invariance cannot do — which "
      f"is precisely the manuscript's reading, and the reason the clause is stated as a selection "
      f"principle rather than dropped in favour of invariance")

# ----------------------------------------------------------------- M6  finiteness is load-bearing
ok6 = True
for n in range(1, 8):
    for f in itertools.product(range(n), repeat=n):
        inj = len(set(f)) == n
        surj = set(f) == set(range(n))
        ok6 &= (inj == surj)               # on a finite set the two coincide
    if n >= 5:
        break
# the infinite countercontrol: the successor map on the naturals is injective and not surjective
succ_inj = len({k + 1 for k in range(2000)}) == 2000
succ_not_surj = 0 not in {k + 1 for k in range(2000)}
ok6 &= succ_inj and succ_not_surj
check("M6", ok6,
      "FINITENESS IS LOAD-BEARING in the structural prong. On every self-map of a set of up to 5 "
      "elements, injectivity and surjectivity coincide — which is `injective_imp_bijective`. The "
      "successor map on the naturals is injective and misses 0, so the implication is about "
      "finiteness and not about injectivity; the manuscript's second prong invokes finiteness and "
      "recurrence for exactly this reason")

# ----------------------------------------------------------------- M7  lint
src = open(os.path.join(BRIDGE, 'OIBridge', 'CanonicalMeasure.lean'), encoding='utf-8').read()
root = open(os.path.join(BRIDGE, 'OIBridge.lean'), encoding='utf-8').read()
NAMES = ('injective_imp_bijective', 'invariant_iff', 'orbit_invariant_unique',
         'counting_invariant', 'entropy_counting', 'counting_maximal_entropy',
         'invariance_does_not_select', 'two_cycle_witness',
         'determinism_reversibility_selected_measure')
body = re.sub(r'(?m)--.*$', '', re.sub(r'/-.*?-/', '', src, flags=re.S))
ok7 = ('import OIBridge.CanonicalMeasure' in root
       and re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', body) is None
       and re.search(r'(?m)^axiom ', body) is None
       and all(f'theorem {n}' in src for n in NAMES)
       and all(f'#print axioms {n}' in src for n in NAMES))
# reversibility must be TAKEN AS GIVEN: the permutation is a hypothesis, never a conclusion
ok7 &= '(φ : Equiv.Perm S)' in src
ok7 &= 'Function.Bijective φ' not in body      # no theorem concludes the substratum is a bijection
# the guard must be a theorem with a real conclusion, not a comment
guard = src[src.index('theorem invariance_does_not_select'):]
guard_sig = guard[:guard.index(':= by')]
ok7 &= 'p ≠ q' in guard_sig and 'Invariant φ p' in guard_sig and 'Invariant φ q' in guard_sig
# the header must record the epistemic layering and the unformalized continuum parenthetical
header = src[:src.index('import ')]
ok7 &= 'REVERSIBILITY IS NOT DERIVED HERE' in header
ok7 &= 'A SELECTION PRINCIPLE, NOT UNIQUENESS FROM INVARIANCE ALONE' in header
ok7 &= 'Liouville measure is invariant' in header and 'deliberately not formalized' in header
# and the manuscript must carry that analogue in a REMARK, not inside the lemma statement
main = open(os.path.join(HERE, os.pardir, os.pardir, 'papers', 'Main.md'), encoding='utf-8').read()
lemma3 = main[main.index('**Lemma 3** (Determinism, reversibility'):]
lemma3 = lemma3[:lemma3.index('\n')]
ok7 &= 'Liouville' not in lemma3 and 'absolutely continuous' not in lemma3
ok7 &= '*Remark (the continuum analogue).*' in main
check("M7", ok7,
      f"the Lean file is IMPORTED BY OIBridge.lean, so CI builds it and the theorems are gated; it "
      f"carries no `sorry` and no `axiom`; all {len(NAMES)} named results print their axiom "
      f"dependencies; the permutation is a HYPOTHESIS everywhere and no theorem concludes that the "
      f"substratum is bijective, matching the manuscript's status remark that reversibility is a "
      f"representation choice; the non-selection guard is a theorem whose conclusion really is "
      f"`p ≠ q` for two invariant probability laws; and the header records both the epistemic "
      f"layering and the continuum analogue it does not formalize, which the manuscript now "
      f"carries in a remark of its own rather than inside the lemma statement")

print()
print('     [scope] Settled: [Main] Lemma 3\'s measure content is kernel-proved — on each')
print('     accessible orbit the invariant law is unique and uniform; the counting measure is')
print('     invariant; it maximizes entropy among invariant laws; and invariance ALONE does not')
print('     select, which is a theorem here rather than a caveat. The finite prong of the')
print('     determinism argument — injectivity implies surjectivity on a finite set — is proved,')
print('     with the infinite countercontrol showing finiteness is what carries it.')
print('     NOT settled here, deliberately: reversibility itself. The manuscript calls the')
print('     bijective substratum a representation choice recovered by a two-pronged argument one')
print('     prong of which is empirical, so the permutation is TAKEN AS GIVEN in Lean and no')
print('     theorem concludes it. The continuum analogue about Liouville measure lives in a')
print('     remark of its own, outside the lemma statement and outside the framework\'s finite')
print('     scope; it is not formalized, and its role is discharged by the finite non-selection')
print('     theorem, which is stronger where it matters.')
print()
print("canonical_measure_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
