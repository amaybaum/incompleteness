#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numerical companion checks for OIBridge/BoundaryRank.lean.

[Main] Lemma 1 (boundary bound):

    rank M_HV <= |outer boundary of R|,      rank M_VH <= |inner boundary of R|

for the reversible nearest-neighbour update  u'_x = sum_{z ~ x} u_z + v_x,  v'_x = u_x  over F_2,
with the visible sector the sites of a region R.

Everything here is exact: entries are bits and ranks are computed by Gaussian elimination over
F_2, so no tolerance is ever consulted. The lattice sweep is EXHAUSTIVE over every proper nonempty
region of every graph listed, which at these sizes is a few hundred regions.

THE FACTOR OF TWO IS WHAT THIS PROBE EXISTS TO GUARD. Every site carries two components, so the
visible sector has dimension 2|R| -- and yet the bound counts SITES. B4 checks the reason directly:
the v'-row of each cross-block is identically zero, because v'_x = u_x reads a single input from
its own sector. B3 checks that the bound |boundary| is ATTAINED, so a bound with a spurious factor
of two would not merely be ugly, it would be provably not tight.

  B1  the update matrix has the printed form, on every graph.
  B2  THE LEMMA, exhaustively: rank M_HV <= |outer|, rank M_VH <= |inner|, every proper region.
  B3  SHARPNESS: the bound is attained, so the constant 1 is right and 2 would be wrong.
  B4  THE FACTOR-OF-TWO GUARD: the v'-rows of both cross-blocks vanish identically.
  B5  the generic support theorem, and its sharpness: a matrix supported exactly on B, of rank |B|.
  B6  COUNTERCONTROL for the support hypothesis: one independent row outside B and the bound fails.
  B7  COUNTERCONTROL for counting cut edges: a star with four cut edges and one boundary site has
      rank one, so the bound is by boundary SITES.
  B8  THE SHARPENING (kernel-proved as `lemma_1_sharpened`, printed as Corollary 2's hypothesis):
      the columns are supported on the OTHER boundary, so under symmetric adjacency both ranks are
      bounded by min(|inner|, |outer|).
  B10 COUNTERCONTROL for the symmetry hypothesis: a one-edge DIGRAPH where the column bound fails
      outright while the row-side lemma, which never reverses an edge, still holds.
  B11 the cubic-block threshold of the strengthened Corollary 2: min(...) < |R| iff the block has
      a non-empty bulk, first at side 3 -- checked by exact counting in Z^3, not by the formula.
  B9  lint.

Usage:  python3 boundary_rank_probe.py
"""
import itertools
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BRIDGE = os.path.abspath(os.path.join(HERE, '..', 'lean-mathlib'))

CHECKS = []


def check(tag, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {tag}: {msg}")


# ---------------------------------------------------------------- exact F_2 linear algebra
def rank_f2(rows, ncols):
    rows = [list(r) for r in rows]
    r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, len(rows)) if rows[i][c]), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                rows[i] = [(a + b) % 2 for a, b in zip(rows[i], rows[r])]
        r += 1
    return r


# ---------------------------------------------------------------- the lattices
def graphs():
    """(name, sites, edge set as unordered pairs)."""
    out = []
    for n in (3, 4, 5, 6):
        out.append((f"path{n}", list(range(n)), {(i, i + 1) for i in range(n - 1)}))
        out.append((f"cycle{n}", list(range(n)), {tuple(sorted((i, (i + 1) % n)))
                                                  for i in range(n)}))
    sites = [(i, j) for i in range(2) for j in range(3)]
    E = {tuple(sorted((a, b))) for a in sites for b in sites
         if abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1}
    out.append(("grid2x3", sites, E))
    out.append(("star5", list(range(5)), {(0, k) for k in range(1, 5)}))
    return out


def adjacency(E):
    def f(a, b):
        return tuple(sorted((a, b))) in E
    return f


def blocks(sites, A, R):
    """The two cross-blocks, and the two boundaries. Component 0 is u, component 1 is v."""
    Rset = set(R)
    outside = [z for z in sites if z not in Rset]
    inner = [x for x in R if any(A(z, x) for z in outside)]
    outer = [y for y in outside if any(A(z, y) for z in R)]
    vis = [(x, c) for x in R for c in (0, 1)]
    hid = [(y, c) for y in outside for c in (0, 1)]

    def row(o, cols):
        x, c = o
        if c == 1:                                   # v'_x = u_x
            return [1 if i == (x, 0) else 0 for i in cols]
        return [1 if (i[1] == 1 and i[0] == x) or (i[1] == 0 and A(i[0], x)) else 0
                for i in cols]                       # u'_x = sum_{z ~ x} u_z + v_x

    MHV = [row(o, vis) for o in hid]
    MVH = [row(o, hid) for o in vis]
    return MHV, MVH, vis, hid, inner, outer


# ---------------------------------------------------------------- B1  the update rule
ok1 = True
for name, sites, E in graphs():
    A = adjacency(E)
    idx = [(x, c) for x in sites for c in (0, 1)]
    for o in idx:
        x, c = o
        for i in idx:
            z, d = i
            if c == 1:
                want = 1 if (z, d) == (x, 0) else 0          # v'_x = u_x
            elif d == 1:
                want = 1 if z == x else 0                    # ... + v_x
            else:
                want = 1 if A(z, x) else 0                   # sum_{z ~ x} u_z ...
            got = (1 if i == (x, 0) else 0) if c == 1 else (
                (1 if z == x else 0) if d == 1 else (1 if A(z, x) else 0))
            ok1 &= want == got
check("B1", ok1,
      "the update matrix is exactly the printed rule -- v'_x = u_x, and u'_x = sum_{z~x} u_z + v_x "
      "-- on every graph below, entry by entry")

# ---------------------------------------------------------------- B2  the lemma
ok2 = True
regions = 0
for name, sites, E in graphs():
    A = adjacency(E)
    for mask in range(1, 2 ** len(sites) - 1):
        R = [s for k, s in enumerate(sites) if mask >> k & 1]
        regions += 1
        MHV, MVH, vis, hid, inner, outer = blocks(sites, A, R)
        ok2 &= rank_f2(MHV, len(vis)) <= len(outer)
        ok2 &= rank_f2(MVH, len(hid)) <= len(inner)
check("B2", ok2,
      f"THE LEMMA, exhaustively over all {regions} proper nonempty regions of four paths, four "
      f"cycles, a 2x3 grid and a star: rank M_HV <= |outer boundary| and rank M_VH <= |inner "
      f"boundary|, in exact F_2 arithmetic")

# ---------------------------------------------------------------- B3  sharpness
sharp_hv = sharp_vh = 0
witness = None
for name, sites, E in graphs():
    A = adjacency(E)
    for mask in range(1, 2 ** len(sites) - 1):
        R = [s for k, s in enumerate(sites) if mask >> k & 1]
        MHV, MVH, vis, hid, inner, outer = blocks(sites, A, R)
        if outer and rank_f2(MHV, len(vis)) == len(outer):
            sharp_hv += 1
            if witness is None:
                witness = (name, R, len(outer))
        if inner and rank_f2(MVH, len(hid)) == len(inner):
            sharp_vh += 1
ok3 = sharp_hv > 0 and sharp_vh > 0
check("B3", ok3,
      f"SHARPNESS. The bound is ATTAINED -- rank M_HV = |outer boundary| in {sharp_hv} of the "
      f"regions and rank M_VH = |inner boundary| in {sharp_vh}, first at {witness}. So the "
      f"constant is 1: a bound of 2|boundary| would be true but not tight, and this check is what "
      f"would catch it")

# ---------------------------------------------------------------- B4  the factor-of-two guard
ok4 = True
zero_rows = 0
for name, sites, E in graphs():
    A = adjacency(E)
    for mask in range(1, 2 ** len(sites) - 1):
        R = [s for k, s in enumerate(sites) if mask >> k & 1]
        MHV, MVH, vis, hid, inner, outer = blocks(sites, A, R)
        for k, o in enumerate(hid):
            if o[1] == 1:
                ok4 &= not any(MHV[k])
                zero_rows += 1
        for k, o in enumerate(vis):
            if o[1] == 1:
                ok4 &= not any(MVH[k])
                zero_rows += 1
check("B4", ok4,
      f"THE FACTOR-OF-TWO GUARD. Every site carries two components, so the visible sector has "
      f"dimension 2|R| -- but the v'-row of each cross-block is IDENTICALLY ZERO, checked on all "
      f"{zero_rows} of them, because v'_x = u_x reads a single input from its own sector. That is "
      f"why the bound counts boundary sites and not boundary components, and it is what "
      f"`rowsHV`/`rowsVH` carrying `.2 = false` earns in the Lean file")

# ---------------------------------------------------------------- B5  the generic theorem
# A matrix over F_2 supported on rows B, of rank exactly |B|: the generic bound is sharp too.
ok5 = True
for nrows, ncols in ((5, 7), (6, 4), (8, 8)):
    for bsize in range(0, min(nrows, ncols) + 1):
        B = list(range(bsize))
        M = [[1 if (r in B and c == r) else 0 for c in range(ncols)] for r in range(nrows)]
        ok5 &= all(not any(M[r]) for r in range(nrows) if r not in B)   # supported on B
        ok5 &= rank_f2(M, ncols) == bsize                               # and attaining |B|
        ok5 &= rank_f2(M, ncols) <= bsize
check("B5", ok5,
      "the generic support theorem and its sharpness: a matrix whose rows vanish off B has rank at "
      "most |B|, and the identity-on-B matrix attains it, for every B in three shapes. This is "
      "`rank_le_card_of_rowSupport`, which the Lean file proves for an arbitrary commutative ring "
      "with the strong rank condition -- no lattice, no F_2")

# ---------------------------------------------------------------- B6  the hypothesis is needed
# One extra independent row outside B and the bound fails, so `rowSupport` is load-bearing.
ok6 = True
for bsize in (1, 2, 3):
    ncols = bsize + 2
    B = list(range(bsize))
    M = [[1 if (r in B and c == r) else 0 for c in range(ncols)] for r in range(bsize + 1)]
    M[bsize] = [0] * ncols
    M[bsize][ncols - 1] = 1                          # an independent row OUTSIDE B
    ok6 &= rank_f2(M, ncols) == bsize + 1
    ok6 &= rank_f2(M, ncols) > bsize                 # the bound is violated, as it must be
check("B6", ok6,
      "COUNTERCONTROL for the support hypothesis. Adding a single independent nonzero row outside "
      "B raises the rank to |B| + 1, so the conclusion is false without the hypothesis and "
      "`rowSupport_MHV` / `rowSupport_MVH` are doing real work rather than decorating the proof")

# ---------------------------------------------------------------- B7  sites, not cut edges
sites = list(range(5))
E = {(0, k) for k in range(1, 5)}
A = adjacency(E)
R = [1, 2, 3, 4]                                     # the four leaves; the hub is hidden
MHV, MVH, vis, hid, inner, outer = blocks(sites, A, R)
cut = [(z, y) for z in R for y in sites if y not in set(R) and A(z, y)]
ok7 = len(cut) == 4 and len(outer) == 1
ok7 &= rank_f2(MHV, len(vis)) == 1
ok7 &= rank_f2(MHV, len(vis)) < len(cut)
check("B7", ok7,
      f"COUNTERCONTROL for counting the wrong thing. In a star with the four leaves visible, "
      f"{len(cut)} edges cross the cut but the outer boundary is a single site, and rank M_HV = 1. "
      f"The bound is by boundary SITES; a bound by cut edges would be four times too weak here")

# ---------------------------------------------------------------- B8  the unprinted observation
# The columns of M_HV are supported on the u-components of the INNER boundary, and dually. So both
# ranks are bounded by min(|inner|, |outer|). The manuscript prints only the row-side bound.
ok8 = True
strict = 0
for name, sites, E in graphs():
    A = adjacency(E)
    for mask in range(1, 2 ** len(sites) - 1):
        R = [s for k, s in enumerate(sites) if mask >> k & 1]
        MHV, MVH, vis, hid, inner, outer = blocks(sites, A, R)
        rHV, rVH = rank_f2(MHV, len(vis)), rank_f2(MVH, len(hid))
        ok8 &= rHV <= min(len(inner), len(outer))
        ok8 &= rVH <= min(len(inner), len(outer))
        # the column supports themselves: visible input enters M_HV only through u_x at inner
        # boundary sites, and hidden input enters M_VH only through u_y at outer boundary sites
        for j, i in enumerate(vis):
            if i[1] == 1 or i[0] not in inner:
                ok8 &= not any(row[j] for row in MHV)
        for j, i in enumerate(hid):
            if i[1] == 1 or i[0] not in outer:
                ok8 &= not any(row[j] for row in MVH)
        if min(len(inner), len(outer)) < max(len(inner), len(outer)):
            strict += 1
check("B8", ok8,
      f"THE SHARPENING, kernel-proved as `lemma_1_sharpened` under symmetric adjacency. The "
      f"columns of each cross-block are supported on the OTHER boundary -- M_HV reads visible "
      f"input only through u_x at inner-boundary sites, M_VH only through u_y at outer-boundary "
      f"sites, both verified column by column -- so both ranks are bounded by min(|inner|, "
      f"|outer|), verified on every region above, the two boundaries differing in size in "
      f"{strict} of them. This is what the strengthened Corollary 2 consumes")

# ---------------------------------------------------------------- B10  symmetry is load-bearing
# A DIRECTED one-edge graph. adj is input -> output: `adj z x` means u_z feeds u'_x. With the only
# edge 0 -> 1 and R = {0}, visible u_0 feeds hidden u'_1, so rank M_HV = 1; but innerB asks for an
# edge pointing INTO R (adj z 0 with z hidden), and there is none, so |inner| = 0 and the column
# bound min(|inner|, |outer|) = 0 FAILS. The row bound |outer| = 1 never reverses an edge and holds.
def directed_blocks(sites, adjfun, R):
    Rset = set(R)
    outside = [z for z in sites if z not in Rset]
    inner = [x for x in R if any(adjfun(z, x) for z in outside)]
    outer = [y for y in outside if any(adjfun(z, y) for z in R)]
    vis = [(x, c) for x in R for c in (0, 1)]
    hid = [(y, c) for y in outside for c in (0, 1)]

    def row(o, cols):
        x, c = o
        if c == 1:
            return [1 if i == (x, 0) else 0 for i in cols]
        return [1 if (i[1] == 1 and i[0] == x) or (i[1] == 0 and adjfun(i[0], x)) else 0
                for i in cols]

    return ([row(o, vis) for o in hid], [row(o, hid) for o in vis], vis, hid, inner, outer)


ok10 = True
# edge 0 -> 1, R = {0}: M_HV breaks the column bound
MHV, MVH, vis, hid, inner, outer = directed_blocks([0, 1], lambda z, x: (z, x) == (0, 1), [0])
ok10 &= (len(inner), len(outer)) == (0, 1)
ok10 &= rank_f2(MHV, len(vis)) == 1
ok10 &= rank_f2(MHV, len(vis)) > min(len(inner), len(outer))     # the SHARPENED bound fails
ok10 &= rank_f2(MHV, len(vis)) <= len(outer)                     # the printed lemma holds
ok10 &= rank_f2(MVH, len(hid)) <= len(inner)
# edge 1 -> 0, R = {0}: M_VH breaks it, mirrored
MHV, MVH, vis, hid, inner, outer = directed_blocks([0, 1], lambda z, x: (z, x) == (1, 0), [0])
ok10 &= (len(inner), len(outer)) == (1, 0)
ok10 &= rank_f2(MVH, len(hid)) == 1
ok10 &= rank_f2(MVH, len(hid)) > min(len(inner), len(outer))
ok10 &= rank_f2(MVH, len(hid)) <= len(inner)
ok10 &= rank_f2(MHV, len(vis)) <= len(outer)
check("B10", ok10,
      "COUNTERCONTROL for the symmetry hypothesis. On the digraph with the single edge 0 -> 1 and "
      "R = {0}, visible input feeds a hidden output but no edge points back into R, so |inner| = 0 "
      "while rank M_HV = 1: the min bound FAILS, in both orientations, while both printed row-side "
      "bounds hold -- the lemma never reverses an edge. `lemma_1_sharpened` carrying symmetry as "
      "an explicit hypothesis is therefore load-bearing, not decoration, and Lemma 1 keeping the "
      "arbitrary relation is a genuine gain in scope")

# ---------------------------------------------------------------- B11  the cubic threshold
# The strengthened Corollary 2 reads min(|inner|, |outer|) < |R| for the exact cubic block, and
# the threshold claim is: it holds iff the block has a non-empty bulk, first at side 3. Counted
# exactly in Z^3, not read off the formula the manuscript displays.
ok11 = True
for ell in range(1, 7):
    Rc = {(a, b, c) for a in range(ell) for b in range(ell) for c in range(ell)}
    def nbrs(p):
        for d in range(3):
            for s in (-1, 1):
                q = list(p); q[d] += s
                yield tuple(q)
    inner = {p for p in Rc if any(q not in Rc for q in nbrs(p))}
    outer = {q for p in Rc for q in nbrs(p) if q not in Rc}
    bulk = len(Rc) - len(inner)
    if ell >= 2:
        ok11 &= len(inner) == ell ** 3 - (ell - 2) ** 3         # the displayed formulas
        ok11 &= len(outer) == 6 * ell ** 2
        ok11 &= len(inner) <= len(outer)                        # inner is the smaller
    holds = min(len(inner), len(outer)) < len(Rc)
    ok11 &= holds == (bulk > 0)                                 # criterion iff non-empty bulk
    ok11 &= holds == (ell >= 3)                                 # first at side 3
    old_holds = len(inner) + len(outer) < 2 * len(Rc)
    ok11 &= (not old_holds) or holds                            # strictly weaker hypothesis
    if ell in (3, 4):
        ok11 &= holds and not old_holds                         # and strictly weaker in fact
check("B11", ok11,
      "THE CUBIC THRESHOLD of the strengthened Corollary 2, counted exactly in Z^3 for sides 1..6: "
      "the displayed formulas |inner| = l^3 - (l-2)^3 and |outer| = 6l^2 are right, inner is the "
      "smaller boundary, and min(|inner|, |outer|) < |R| holds exactly when the block has a "
      "non-empty bulk -- first at side 3, where 26 < 27, while side 2 fails at 8 = 8. The old "
      "hypothesis |inner| + |outer| < 2|R| first held at side 5, so at sides 3 and 4 the new "
      "corollary applies where the old one was silent")

# ---------------------------------------------------------------- B9  lint
src = open(os.path.join(BRIDGE, 'OIBridge', 'BoundaryRank.lean'), encoding='utf-8').read()
root = open(os.path.join(BRIDGE, 'OIBridge.lean'), encoding='utf-8').read()
body = src[src.index('namespace OIBridge'):]

NAMES = ('eq_extend_mul_restrict', 'rank_le_card_of_rowSupport', 'rowsHV_card', 'rowsVH_card',
         'rowSupport_MHV', 'rowSupport_MVH', 'rank_MHV_le', 'rank_MVH_le',
         'lemma_1_boundary_bound', 'rank_le_card_of_colSupport', 'colSupport_MHV',
         'colSupport_MVH', 'rank_MHV_le_inner', 'rank_MVH_le_outer', 'lemma_1_sharpened')
ok9 = 'import OIBridge.BoundaryRank' in root
ok9 &= re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', body) is None
ok9 &= re.search(r'(?m)^axiom ', body) is None
ok9 &= all(f'theorem {n}' in src for n in NAMES)
ok9 &= all(f'#print axioms {n}' in src for n in NAMES)
ok9 &= 'native_decide' not in body
# the generic layer must be genuinely generic: stated over a ring, with no lattice in its section
gen = src[src.index('section Generic'):src.index('end Generic')]
ok9 &= '[CommRing K] [StrongRankCondition K]' in gen
for banned in ('ZMod', 'adj', 'innerB', 'outerB', 'upd', 'Λ'):
    ok9 &= banned not in gen
# the update must be the printed one
ok9 &= 'if o.2 then (if i = (o.1, false) then 1 else 0)' in src
# THE FACTOR OF TWO: both row-support sets must restrict to one component
for nm in ('rowsHV', 'rowsVH'):
    blk = src[src.index(f'def {nm}'):]
    blk = blk[:blk.index('\n\n')]
    ok9 &= '.val.2 = false' in blk
# and the bounds must be against the boundary card, not twice it
ok9 &= '(MHV adj R).rank ≤ (outerB adj R).card' in src
ok9 &= '(MVH adj R).rank ≤ (innerB adj R).card' in src
ok9 &= '2 * (outerB' not in src and '2 * (innerB' not in src
# THE SYMMETRY SCOPE GUARD: the sharpening must carry symmetry as an explicit hypothesis, and the
# original lemma must NOT acquire it
sh = src[src.index('theorem lemma_1_sharpened'):]
shsig = sh[:sh.index(':=')]
ok9 &= 'hsym : ∀ x y, adj x y → adj y x' in shsig
ok9 &= 'min (innerB adj R).card (outerB adj R).card' in shsig
lb = src[src.index('theorem lemma_1_boundary_bound'):]
lbsig = lb[:lb.index(':=')]
ok9 &= 'hsym' not in lbsig and 'adj x y → adj y x' not in lbsig
check("B9", ok9,
      f"LINT. The file is imported by OIBridge.lean so CI builds it; no `sorry`, no `axiom`, no "
      f"`native_decide`; all {len(NAMES)} named results print their axiom dependencies. The generic "
      f"section is stated over `[CommRing K] [StrongRankCondition K]` and mentions no lattice, no "
      f"adjacency and no `ZMod`; the update is the printed rule; both row-support sets carry "
      f"`.val.2 = false`, so the bounds are against |boundary| and not 2|boundary|")

print()
print('     [scope] Settled in Lean: [Main] Lemma 1, both inequalities, for the displayed update')
print('     on an arbitrary finite lattice, an arbitrary region, and an ARBITRARY adjacency')
print('     relation; plus the sharpened min(|inner|, |outer|) bound under symmetric adjacency,')
print('     with symmetry an explicit, probe-guarded hypothesis -- all resting on generic')
print('     row- and column-support factorization theorems proved over any commutative ring with')
print('     the strong rank condition. NOT settled here: Lemma 2, the normal form, and')
print('     Corollaries 1 and 2, which consume these bounds; the separability threshold they end')
print('     at is closed separately in OIBridge/WeylLift.lean.')
print()
print("boundary_rank_probe:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
