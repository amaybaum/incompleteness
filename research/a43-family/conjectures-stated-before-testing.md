# Conjectures stated before testing (a43 research thread, disposable)

Committed before any Diţă locus was computed for a family other than act 40's H3. Formation data: act 40's H3 only
(`c0_control_h3.log`, `f0_h3_formation.log`), plus the atom catalogue (`s2_atoms.log`, `s3_atomlib.log`), which contains no
locus data.

Setting. For a witness E (one of the 416 collected {0,1} straight lines, 53 orbits), its atoms are the cells classes of the
splitter algebra (splitter = 0/1 sub-support P with {P, E-P} jointly realizable). The atom family is
F_E(u) = SIG o prod_k u_k^{P_k}. Essential atoms = atoms that are not gauge-trivial (not a full row or a full column).

- **K1 (coordinate loci).** For the essential atom family of every orbit: every candidate's strict locus equals its relaxed
  locus; every nonempty locus is cut out by coordinate characters u_k = +-1 alone; the maximal loci are codimension-one faces
  {u_k = +1} or {u_k = -1}.
- **K2 (the +1 face criterion, a tautology check).** The face u_k = 1 lies in the locus iff the span of the other atoms lies
  identically in one census structure of SIG (strict). Recorded as a control of the harness, not as a finding.
- **K3 (every proper sub-sum Diţă).** Every atom has its +1 face (the witness is "minimal": removing any atom lands in a hull),
  as for H3.
- **K4 (shape rule for -1 faces).** The face u_k = -1 appears iff the face u_k = +1 appears and atom k is a 2x8 or 8x2 rectangle;
  never for a 4x4 or 1x16 atom. (Formed from A = 2x8: both faces; C = 8x2: both; B = 4x4: +1 only.)
- **K5 (pairing).** A -1 face never appears without the +1 face of the same atom.
- **K6 (rewiring).** At a -1 face the admitted structures are 2x8 in some orientation, and each is a +1-face 2x8 structure of the
  same orientation and blocks with the class partners transposed on the flipped atom's 2-element side.
- **K7 (diagonal prediction; independent-method test).** The exceptional set of the witness line u -> SIG o u^E (computed by the
  one-parameter classifier on E itself, not from the atoms) is {1, -1} if the atom family has some -1 face and {1} otherwise.

Countercontrols planned: perturbed atom families (one cell moved), families with a gauge atom (strict vs relaxed expected to
differ), and non-witness sums.

## Added after the alignment finding (before running its test)

Context: the frozen pipeline fixes the within-class member alignment by sorted order (see NOTE); from here the primary notion is
the alignment-free one (every index map), with the sorted notion computed alongside. Honesty flag: when K8 was written, the
sorted-notion face lists of orbits 0-13 (s4, killed) had been seen; the alignment-free loci of no orbit other than H3 had.

- **K8 (flip = index permutation).** Rows (or columns) of SIG = F4(z) (x) F4(w) have a +-1 ratio vector only for index shifts by 2
  in a or in b (or both). So the sign flip SIG o (-1)^{P_k} of a 16-cell rectangle atom is an index transposition pi exactly for
  special 2x8 / 8x2 atoms. Prediction (alignment-free notion): the face u_k = -1 lies in the locus iff the flip of atom k is an index
  permutation pi of SIG and the other atoms transported by pi span a lattice lying identically in one Dita structure of SIG
  (equivalently: the +1 face of the transported family exists). Every other atom (every 4x4 atom, every non-permutation 2x8/8x2
  atom) has no -1 face.
- **K9 (union = faces, alignment-free).** Under the alignment-free notion, the union of the loci is still a union of coordinate
  subtori {u_S = s} (s in {+-1}^S), even when individual loci contain non-coordinate points.

## Prediction before v3 (explicit point check) completes

- **K8-sym (theorem-shaped).** If SIG o (-1)^{P_k} = Pi_r SIG Pi_c for index permutations fixing every atom, then
  F(..., -u_k, ...) = Pi_r F(..., u_k, ...) Pi_c for all u, so the alignment-free locus is invariant under u_k -> -u_k. For H3: A's flip
  is rows 7<->15, C's flip is columns 2<->8, both fixing A, B, C. Predicted alignment-free structure counts: count(-1,1,1) =
  count(1,1,1) = 20, count(1,1,-1) = 20, count(-1,-1,-1) = count(1,-1,1), count(-z^-2,1,1) = count(z^-2,1,1),
  count(-1,1,u) = count(1,1,u).

## K10, stated after seeing orbits 0-25 (alignment-free), before any result for orbits 26-52 was read

Outcome so far (orbits 0-25, t_k8_snap): K8 26/26, K5 26/26, K7 26/26, K9 26/26, K2 26/26 (control); K4 FALSIFIED (orbits 4, 8,
10: a 2x8 atom with a +1 face and no -1 face; its flip is not an index permutation); K3 fails 16/26; K1 fails 19/26 (codim-2
components, strict != relaxed, non-coordinate points inside individual loci).

- **K10 (the general statement; hold-out test on orbits 26-52).** For S a subset of the atoms and s in {+-1}^S, let
  T(S, s) = {u : u_k = s_k for k in S}. Predict T(S, s) inside the locus iff (i) SIG o prod_{k in S} s_k^{P_k} = Pi_r SIG Pi_c for
  index permutations (row permutation or column permutation; s = all +1 gives the identity), and (ii) the remaining atoms,
  transported by the permutation, span a lattice lying identically in one of SIG's twenty (alignment-free) Dita structures.
  Then the RELAXED union of the loci equals the union of the predicted T(S, s) (compared as sets of maximal flats). Where strict
  and relaxed differ, the strict union is a subset; no prediction for which part.
