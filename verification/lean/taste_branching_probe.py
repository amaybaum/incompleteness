#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OIBridge/TasteBranching.lean.

[SM] Theorem 8 (taste branching): under the cubic group O, 4 = 1 + 3 -- one singlet taste pair
and three axis pairs in a single orbit.

THE CARRIER SUBTLETY IS THE POINT, per the manuscript's own remark. On the corner labels a
rotation acts only through its axis permutation (sign flips are trivial on {0, pi} components), so
the label action on the three axis pairs is the S3 permutation representation, which is A1 + E --
reducible. The irreducible T1 of "three triplet tastes" is the SIGNED vector representation, the
gamma^j carrier of Theorem 9. T3 below verifies both characters over the full rotation group: the
unsigned character has norm 2 (two irreducibles) and contains the trivial once; the signed
character has norm 1 (irreducible) and contains the trivial not at all. That distinction is what
the Lean file kernel-proves as `axis_rep_reducible` against `irreducible_rhoT`.

The rotation group here is built INDEPENDENTLY of the Lean route: the 24 integer 3x3 matrices with
entries in {0, +-1}, orthogonal, det +1 -- not via S4 conjugation -- so agreement is a check, not
an echo.

  T1  the 8 corners pair under eta <-> 1 - eta into exactly 4 pairs: {000,111} and three axis pairs.
  T2  all 24 rotations fix the singlet pair and permute the three axis pairs; the induced axis
      permutations are exactly S3 (hence transitivity, and the branching is 4 = 1 + 3 with no
      further split at pair level).
  T3  THE CARRIER CHECK: over the 24 rotations, the unsigned axis-permutation character has
      <chi, chi> = 2 and <chi, 1> = 1 (A1 + E), while the signed vector character has
      <chi, chi> = 1 and <chi, 1> = 0 (irreducible T1); they differ, e.g. at a face 180-degree
      rotation, where unsigned gives 3 and signed gives -1.
  T4  lint.

Usage:  python3 taste_branching_probe.py
"""
import itertools
import os
import re
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
BRIDGE = os.path.abspath(os.path.join(HERE, '..', 'lean-mathlib'))

CHECKS = []


def check(tag, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {tag}: {msg}")


# ---------------------------------------------------------------- the rotation group, from scratch
def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def rotations():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            M = [[0] * 3 for _ in range(3)]
            for r in range(3):
                M[r][perm[r]] = signs[r]
            if det3(M) == 1:
                out.append((perm, signs, tuple(map(tuple, M))))
    return out


ROTS = rotations()

# ---------------------------------------------------------------- T1  the pairing
corners = list(itertools.product((0, 1), repeat=3))
pairs = set()
for eta in corners:
    m = tuple(1 - x for x in eta)
    pairs.add(frozenset((eta, m)))
pairs = sorted(pairs, key=lambda p: sorted(p))
singlet = frozenset(((0, 0, 0), (1, 1, 1)))
axis_pairs = {j: frozenset((tuple(1 if k == j else 0 for k in range(3)),
                            tuple(0 if k == j else 1 for k in range(3)))) for j in range(3)}
ok1 = len(pairs) == 4 and singlet in pairs
ok1 &= all(axis_pairs[j] in pairs for j in range(3))
check("T1", ok1,
      "the 8 Brillouin-zone corners pair under eta <-> 1 - eta into exactly four taste pairs: the "
      "singlet {000, 111} and the three axis pairs, nothing else")

# ---------------------------------------------------------------- T2  the branching
def corner_act(perm, eta):
    """Labels transform by the axis permutation alone: component j of the image reads eta at the
    axis the rotation carries to j; signs act trivially on {0, pi}."""
    out = [0] * 3
    for r in range(3):
        out[r] = eta[perm[r]]
    return tuple(out)


ok2 = True
axis_perms = set()
for perm, signs, M in ROTS:
    img_singlet = frozenset(corner_act(perm, e) for e in singlet)
    ok2 &= img_singlet == singlet
    ax_map = []
    for j in range(3):
        img = frozenset(corner_act(perm, e) for e in axis_pairs[j])
        hits = [k for k in range(3) if img == axis_pairs[k]]
        ok2 &= len(hits) == 1
        ax_map.append(hits[0])
    axis_perms.add(tuple(ax_map))
ok2 &= len(axis_perms) == 6                               # the full S3: transitive and then some
ok2 &= all(any(am[j] == k for am in axis_perms) for j in range(3) for k in range(3))
check("T2", ok2,
      "all 24 rotations (built independently as integer orthogonal matrices of determinant one) "
      "fix the singlet pair and permute the three axis pairs, and the induced axis permutations "
      "are the full S3 -- so the orbit structure is exactly 1 + 3. Lean's `singlet_fixed`, "
      "`cornerAct_axisCorner`, `axis_transitive`")

# ---------------------------------------------------------------- T3  the carrier check
ok3 = True
chi_unsigned = []
chi_signed = []
witness = None
for perm, signs, M in ROTS:
    cu = sum(1 for j in range(3) if perm[j] == j)          # unsigned: axes fixed as axes
    cs = M[0][0] + M[1][1] + M[2][2]                       # signed: the vector character
    chi_unsigned.append(Fraction(cu))
    chi_signed.append(Fraction(cs))
    if cu == 3 and cs == -1 and witness is None:
        witness = (perm, signs)                            # a face 180-degree rotation
norm_u = sum(x * x for x in chi_unsigned) / 24
norm_s = sum(x * x for x in chi_signed) / 24
triv_u = sum(chi_unsigned) / 24
triv_s = sum(chi_signed) / 24
ok3 &= norm_u == 2 and triv_u == 1                         # A1 + E: two irreducibles, one trivial
ok3 &= norm_s == 1 and triv_s == 0                         # T1: irreducible, no trivial part
ok3 &= witness is not None
check("T3", ok3,
      f"THE CARRIER CHECK, over all 24 rotations in exact rationals: the unsigned "
      f"axis-permutation character has <chi,chi> = {norm_u} and <chi,1> = {triv_u} -- two "
      f"irreducibles containing the trivial once, i.e. A1 + E, REDUCIBLE -- while the signed "
      f"vector character has <chi,chi> = {norm_s} and <chi,1> = {triv_s}, irreducible T1. They "
      f"differ at the face 180-degree rotation {witness[0]}, signs {witness[1]}: unsigned 3, "
      f"signed -1. Lean's `axis_rep_reducible` against `irreducible_rhoT` is this distinction, "
      f"kernel-proved")

# ---------------------------------------------------------------- T4  lint
src = open(os.path.join(BRIDGE, 'OIBridge', 'TasteBranching.lean'), encoding='utf-8').read()
root = open(os.path.join(BRIDGE, 'OIBridge.lean'), encoding='utf-8').read()
body = src[src.index('namespace OIBridge'):]

NAMES = ('axisAct_mul', 'cornerAct_mate', 'singlet_fixed', 'cornerAct_axisCorner',
         'axis_transitive', 'corners_exhausted', 'axisRep_fixes_allOnes',
         'axis_rep_reducible', 'theorem_8')
ok4 = 'import OIBridge.TasteBranching' in root
ok4 &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', body) is None
ok4 &= re.search(r'(?m)^axiom ', body) is None
ok4 &= all(f'theorem {n}' in src for n in NAMES)
ok4 &= all(f'#print axioms {n}' in src for n in NAMES)
ok4 &= 'native_decide' not in body
# the triplet carrier must be the ALREADY-KERNEL-PROVED rhoT, cited, not re-proved or asserted
ok4 &= 'irreducible_rhoT' in src
ok4 &= 'Representation.IsIrreducible rhoT' in src
# and the reducibility of the unsigned action must be a NEGATIVE statement about a genuine rep
ok4 &= '¬ Representation.IsIrreducible axisRep' in src
check("T4", ok4,
      f"LINT. The file is imported by OIBridge.lean so CI builds it; no `sorry`, no `axiom`, no "
      f"`native_decide`; all {len(NAMES)} named results print their axiom dependencies. The "
      f"triplet carrier clause cites the already-kernel-proved `irreducible_rhoT` rather than "
      f"asserting it, and the manuscript remark's distinction is a genuine negative theorem "
      f"`¬ IsIrreducible axisRep`, not prose")

print()
print('     [scope] Settled in Lean: [SM] Theorem 8 as its own theorem -- the equivariant pairing,')
print('     the fixed singlet pair, the transitive action on the three axis pairs, exhaustion of')
print('     the Brillouin zone, the irreducibility of the signed triplet carrier (rhoT, reused')
print('     from the QuarterTurn round), and the REDUCIBILITY of the unsigned label action, which')
print("     is the manuscript remark made kernel-precise. NOT settled: Theorem 9's gamma^j")
print('     construction itself, and the C2(T1) = 2 Casimir input to the Koide chain, which the')
print('     remark flags as a separate load-bearing identification.')
print()
print("taste_branching_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
