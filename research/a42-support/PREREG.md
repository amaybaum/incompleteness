# A42 support research — decision rule and controls (written before the definitive runs were read)

Chronology, stated plainly: exploratory runs (tooling, timing, the first m = 0 enumeration that was stopped, the
R-span statistics on orbit representatives, the witness control at budget 48 and the broken-pruning countercontrol,
the {0,1} all-rows-support-2 case) were run before this file was written. The definitive runs whose outputs were not
read when this was written: `m0all_b47` (dfsR2, every nonzero-row set, no row symmetry), `sat_m1_47` (no-zero-line
case), `d01_zero` ({0,1} representatives with a zero row), `spanAll_77` (R-span over every row set).

Decision rule, per support s (s = orbit-minimal support, i.e. min over gauge; see NOTE.md):

- EXCLUDED (general integers): s < 16 by Lemma U; further s only where the note's general-integer argument closes
  (R-span over every row set with LB <= the stated bound, plus the no-zero-line reduction).
- EXCLUDED (domain D1 = classes with a minimal-support representative in {-1,0,1}): no leaf of `m0all_b47` lies
  outside all 18 relaxed census subspaces, and `sat_m1_47` is UNSAT (no straight line with no zero line, s <= 47,
  mode-0 lines, row 0 of support <= 2).
- EXCLUDED (domain D01 = classes with a {0,1} representative of support s): Lemma P (s = 16 rank) and every leaf of
  `d01_zero` (budget 47) and `d01_two` (budget 32) lies in some census subspace.
- FOUND: a leaf outside all 18 subspaces with support s <= 47; then verify exactly (straight_direct, generic structure
  search) and compute its exact minimal support.
- NOT REACHED: anything else.

Controls (must pass, or verdicts are void):
- C1 the m = 0 search at budget 48 on the act-38 witness's nonzero-row set returns the witness, classified outside
  all 18 subspaces.
- C2 the searches at budget 16 return rectangles containing A, B, C (up to the search's representative) and classify
  every support-16 leaf inside a census subspace.
- C3 countercontrol: the broken pruning rule (prune on constant equation contributions without the zero-sum test)
  visibly changes C1 (loses the witness); a known non-straight matrix (A with one entry removed) is rejected by the
  tables, by the exact Laurent test and by the SAT encoding; the no-zero-line SAT encoding is satisfiable at budget 64.
- C4 exact recheck (straight_direct, independent of the tables) of every stored leaf outside the census and of a
  sample of the others.
