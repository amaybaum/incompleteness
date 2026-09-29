# A42 research: is support 48 minimal for a non-Diţă straight line through SIG?

Read-only, disposable research thread (Track B, OI→QM). Branch `claude/a42-support-research`, base D41 =
`78ea3c39004e97aad027ee6153051c6d372bdd55`. Nothing here is a certificate or a governed round.

## Verdict

**No, support 48 is not minimal.** There is a non-Diţă straight line through SIG with a representative of support
**40**, and act 38's own witness has a representative of support **44**. The value 48 is the support of act 38's
{0,1} representative, and the minimum over the gauge orbit is lower. The upper bounds (40, 44) are exact: these
representatives are written down and verified. That 40 and 44 are the orbit minima of those two classes rests on a
HiGHS integer-programme optimality certificate, which is floating point.

Whether 40 is the global minimum is settled only inside a stated domain. The **minimum is exactly 40 among classes
whose minimal-support representative has entries in {−1, 0, 1}**. That rests on the exhaustive exact searches below,
subject to the one open row (NOZERO_STATUS). For arbitrary integer entries the exclusion is proved only for s ≤ 19,
and for s ≤ 23 when the minimal representative has a zero line.

### Per-support table (s = orbit-minimal support, defined below)

| s | result | domain | layer |
|---|---|---|---|
| 1–15 | **excluded** (no straight line at all apart from gauge) | all integer E | proof (Lemma U) + exact table cross-check |
| 16–19 | **excluded** (every straight line is Diţă) | all integer E | Lemmas CV, RS, M, M1 + exhaustive exact R-span check |
| 20–23 | **excluded** if the min representative has a zero row or column; open otherwise | all integer E | Lemma RS (every row set with LB ≤ 23 is dead) |
| 16–39 | **excluded** | D1: min representative in {−1,0,1} | exhaustive exact DFS (zero-line case) + SAT (other cases), N18 test |
| 16–47, s ∉ 16Z | no {0,1} representative exists | D01: {0,1} representatives | Lemma P |
| 16, 32 | **excluded** | D01 | exhaustive enumeration (12 808 leaves, all N18-Diţă) |
| **40** | **found**: E40 below (and 2 048+ further D1 leaves in 192 orbit classes) | D1 | exact straightness; generic search 0 candidates in every shape and form; outside all 20 structures under all labellings |
| 41–43, 45–47 | not determined (not needed for the verdict) | — | — |
| **44** | **found**: act 38's witness class (min representative has entries −2..1) | general integers | exact representative of support 44; minimality by HiGHS |

"Excluded" means that every straight line in the stated domain with that support is Diţă. The exclusions are
N18 exclusions (defined below), so they hold for every Diţă notion. The witnesses are generic-search witnesses, so
they are non-Diţă under every notion.

### The support-40 witness

    E40[(a,b),(c,d)] = −[b = 0][c = 0]  +  [a = 2][b odd][d even]  −  [a even][c odd][d = 0]
                     =        −P        +          Q               −          T

P (4×4), Q (2×8) and T (8×2) are straight rectangles of support 16. Q and T overlap in the four cells
rows {9, 11} × columns {4, 12}, where they cancel, so |supp E40| = 48 − 8 = 40. Entries lie in {−1, 0, 1}, and
ΣE40 = −16 ≡ 0 (mod 16), as Lemma D requires. `witness42.py` / `witness42.json` measure the following:

- **Straight:** exact Laurent identity with Gaussian rationals (`straight_direct`) and the exact subset tables.
- **Generic search:** act 37's structure search on the monomial entries at a free u returns (candidates, exact) =
  (0, 0) for 4×4, 8×2 and 2×8, in both the column and the row form. The candidate count does not depend on label
  matchings, so no Diţă structure of any shape, with any index maps and any labelling, holds identically.
- **Complete test** (20 structures, all labellings, relaxed): member of none. **N18:** member of none.
- **Pieces:** P, Q, T each lie in several structures. −P+Q lies in t2-row only, −P−T in t1-col only, and Q−T in
  t1-row and t2-col. The triple lies in none. Every xP + yQ + zT with |x|, |y|, |z| ≤ 2 is straight. This is the same
  three-rectangle pattern as act 38's A + B + C, but the pieces are arranged to overlap.
- **Orbit-minimal support:** 40 (HiGHS optimal, dual bound 216 zeros).

The budget-47 zero-row runs, now quarantined, found N18-non-member leaves only at support 40. The rerun for the row sets 0x1f1f, 0x555f, 0x5a5f and 0x5b5b (`found1.pkl`) gives
8 192 leaves in 192 orbit classes. FOUND_CLASS_SUMMARY

### The act-38 witness at support 44

In the representative below, rows 7 and 15 are shifted by −1 and columns 2 and 8 are adjusted, so the representative
has 44 nonzero entries with values −2..1 (`minsupp_milp.py`, HiGHS optimal). The D2 control search in {−2..2}
(below) finds the same orbit class at support 44.

     0  0 -1  0  0  0  0  0 -1  0  0  0  0  0  0  0
     0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
     0  0 -1  0  0  0  0  0 -1  0  0  0  0  0  0  0
     0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
     0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
     0  0 -1  0  0  0  0  0 -1  0  0  0  0  0  0  0
     0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
    -1 -1 -2 -1  0  0  0  0 -2 -1 -1 -1  0  0  0  0
     0  1 -1  0  0  1  0  0 -1  1  0  0  0  1  0  0
     0  1  0  0  0  1  0  0  0  1  0  0  0  1  0  0
     0  1 -1  0  0  1  0  0 -1  1  0  0  0  1  0  0
     0  1  0  0  0  1  0  0  0  1  0  0  0  1  0  0
     0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
     0  0 -1  0  0  0  0  0 -1  0  0  0  0  0  0  0
     0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
    -1 -1 -2 -1  0  0  0  0 -2 -1 -1 -1  0  0  0  0

The two three-parameter families, act 38's xA + yB + zC and this thread's −xP + yQ − zT, were scanned over
|x|, |y|, |z| ≤ 2 with all coefficients nonzero and the member outside every complete structure
(`family_scan.py`). Their orbit-minimal supports measured so far are only 40 and 44. FAMILY_SUMMARY

### Why act 38 saw nothing below 48

Act 38's census ran over {0,1} matrices. By Lemma P a {0,1} straight line has support 16·rank(SIG∘E), so the
supports available in that domain are 16, 32 and 48. All support-16 and support-32 {0,1} straight lines are Diţă:
12 808 leaves, every one in N18 (`dfs01.py`). A non-Diţă class of smaller support must use entries outside {0,1},
as E40 does (entries −1 and +1).

## Objects, domain, group action, support

- SIG = F4(z) ⊗ F4(w), with z = (3+4i)/5 and w = (5+12i)/13, index (a,b) ↦ 4a+b, and unimodular entries (scaled
  by 4). It is loaded verbatim from the landed probe head `verification/lean/dita_arc_exclusivity_probe.py`
  (`lib42.py`).
- **Straight line:** an integer matrix E ∈ Z^{16×16} such that H(u) = SIG ∘ u^E is complex Hadamard for every
  unit u. Equivalently, by coefficient extraction in H H* = 16 I: for every row pair (i, i′) and every integer d,
  Σ_{k : E_ik − E_i′k = d} SIG_ik conj(SIG_i′k) = 0. In words, every level set of every row difference vanishes.
  This is tested two ways: with exact subset tables (Gaussian integers × 65), and independently with exact Gaussian
  rationals (`straight_direct`).
- **Group G** acting on exponent matrices, generated by three kinds of element:
  - gauge, E ↦ E + α1ᵀ + 1βᵀ with α, β ∈ Z¹⁶;
  - the 1024-element stabilizer of SIG from act 36, acting as signed position permutations
    (σE)[p(t)] = s·E[t]. Here s = −1 exactly for the elements that conjugate, and 512 of the elements transpose.
    Every element fixes SIG up to dephasing, so straightness is preserved (`lemmas42.py` L3, all 1024 elements);
  - the global sign, E ↦ −E.
- **Support.** s(E) is the least number of nonzero entries over the G-orbit.
  - **Lemma O:** s(E) = min_{α,β} #{(i,j) : E_ij + α_i + β_j ≠ 0}. This holds because stabilizer elements and the
    sign are signed permutations of the 256 positions and map the gauge subspace to itself.
  - A representative attaining s(E) is a **min representative**. In it, 0 is a most frequent value of every row and
    every column, since otherwise shifting that line would lower the support. This **mode-0** condition is used only
    as a necessary filter.
- **Domains:**
  - D1: classes having a min representative with entries in {−1, 0, 1};
  - D01: classes having a {0,1} representative (act 38's domain);
  - general integers, where a lemma closes the case.
  - D2 = {−2..2} is implemented (`dfsR3.py`) but was run only as a control, not as a sweep.

## The Diţă notion

- **N18:** act 38's test. E lies in one of the 18 relaxed census subspaces L_S. The strict subspaces are contained
  in the relaxed ones, and the relaxed equations annihilate gauge (both checked). Every L_S is a genuine Diţă
  structure of SIG, so N18-membership implies Diţă under every notion.
- **Ncomplete:** the complete notion requested by the coordinator. It covers 20 structures (the 18 plus the fifth
  4×4 structure in both forms) under every valid label matching, relaxed form (`complete42.py`). The code reuses
  `matchlib41.py` and `fifth41.json` verbatim from the census thread. The valid matchings are recomputed here at SIG
  with exact arithmetic: 8, 64, 8, 8, 4, 4, 128, 128, 128, 8 per structure, the same in both forms. This matches the
  census thread's count of 20 structures.
- **Ngeneric:** act 37's `structures` search at a free u. Zero candidates in every shape and form means that no Diţă
  structure holds identically under any notion.

**Reading rule.** Every exclusion here is an N18 exclusion, which is the strongest kind: each line in the excluded
set lies in one of the 18 subspaces, so it is Diţă under Ncomplete as well. Every witness is an Ngeneric witness and
is also checked outside Ncomplete. The earlier exclusions therefore stand unchanged under the complete notion; none
needed re-checking beyond confirming N18 ⊂ Ncomplete.

**Independent observation, consistent with the census thread's F1.** The 18 subspaces are not closed under the
stabilizer. Transporting them by all 1024 elements gives 34 distinct subspaces (`closure.py`, deduplicated by
reduced echelon form modulo two primes). The extra subspaces are census partitions with a non-sorted label matching,
each an exact relaxed Diţă structure of SIG (`matching.py`). Consequence for method: N18 non-membership is not
orbit-invariant, so every decisive N18 search here runs over all row sets without symmetry reduction. The
existence-only SAT runs use symmetry, which is legitimate because straightness is invariant.

## Pruning lemmas (each stated, proved or checked exactly)

Notation: for a representative E, Z = its set of zero rows, R = the rest (r = |R|), msize(i, Z) = least size of a
nonempty column set K with Σ_{k∈K} SIG_ik conj(SIG_zk) = 0 for every z ∈ Z (exact tables, `cvsize.py`), and
LB(R) = Σ_{i∈R} msize(i, Z).

- **VS (pair structure).** For each of the 120 row pairs the vanishing column sets are: antipodally balanced sets
  (columns with pair product v matched with columns with −v) for 88 pairs (64 of type 4|4+4|4, 24 of type 8|8), and for
  the 32 remaining pairs balanced sets plus 32 exceptional sets (from relations like z + w = 2(1 + zw)). Minimal
  vanishing sets have sizes 2 and 6 only (`pairtypes.py`, `lemmas42.py` L1). Hence no level set of a row difference is
  a singleton. Used by the SAT encoding and by G1/M1.
- **CV (common vanishing).** If z is a zero row, every level set of E_i equals a level set of E_i − E_z and so
  vanishes for the pair (i, z). A nonzero row i is therefore a labelled packing of sets that vanish against every zero
  row; every such set is a disjoint union of minimal ones (difference of two vanishing sets vanishes).
- **U (uncertainty; general integers).** Each nonzero level set K of a nonzero row satisfies |K| ≥ 16/r; hence every
  representative of every straight line that is not gauge-trivial has at least 16 nonzero entries. Proof: v = 1_K∘SIG_i
  is orthogonal to the rows SIG_z, z ∈ Z (Lemma CV), so its coordinate vector in the orthonormal basis SIG/4 has at most
  r nonzero entries; the basis matrix is unitary with all entries of modulus 1/4, and Donoho–Stark
  (‖x‖₂ ≤ √|supp ŷ|·‖ŷ‖_∞ ≤ √|supp ŷ|·¼‖x‖₁ ≤ ¼√(|supp ŷ||supp x|)‖x‖₂) gives |K|·r ≥ 16. Summing over the r nonzero
  rows, |supp E| ≥ r·⌈16/r⌉ ≥ 16 (r = 16 included; r = 1 forces a constant row, i.e. gauge-trivial, since 1_K∘SIG_i ∈
  span(SIG_i) forces K = ∅ or all columns). Exact cross-check: msize(i, Z) ≥ ⌈16/(16−|Z|)⌉ for all 16·2¹⁵ pairs
  (`lemmas42.py` L2).
- **LB.** |supp E| ≥ LB(R) for the exact zero-row set; the searches enumerate only row sets with LB(R) ≤ budget.
- **P (projection; {0,1} representatives).** For E ∈ {0,1}^{16×16}, U(u) = (SIG∘u^E)SIG*/16 = (I − Q) + uQ with
  Q = (SIG∘E)SIG*/16. U(u) unitary for all u ⇔ Q(I − Q*) = 0 and its adjoint ⇔ Q is an orthogonal projection. Then
  rank Q = tr Q = Σ_i (row sum of E_i)/16 = |supp E|/16. So a {0,1} straight line has support 16·rank(SIG∘E) ∈ 16Z.
  Checked exactly (rank over Q(i)) on A, B, C, the act-38 witness and all 12 808 {0,1} leaves (`lemmas42.py` L4).
- **D (determinant; general integers).** det(SIG∘u^E) is a Laurent polynomial of constant modulus on the circle, hence
  c·u^δ, and δ = tr((SIG∘E)SIG⁻¹) = ΣE/16. So ΣE ≡ 0 (mod 16) for every straight line (checked on every classified
  leaf: `sum_mod16` = 0). Not used for pruning.
- **G1 ({0,1}, support-1 row).** If a {0,1} straight line has a row e_k then column k is all ones (else the level set
  {k} of value −1 in E_i − e_k is a singleton, contradicting VS); subtracting that column (gauge) gives a {0,1} straight
  line of support s − 16 with a zero row.
- **RS (row-set span; general integers).** By CV, a straight line with zero-row set exactly Z lies in
  W_R = ⊕_{i∈R} span{1_K : K vanishes for row i against every z ∈ Z}. If W_R lies in one census subspace L_S, every
  straight line (any integer values) with that zero-row set is Diţă. Exhaustive over all 65 390 row sets with r ≥ 2 and
  LB(R) ≤ 77 (`spanAll.py`): 13 922 dead; the smallest LB of a live row set is 24, and all 50 row sets with LB < 24
  (LB = 16) are dead.
- **M (minimum line; no zero line).** Let m be the least support of a row or column of a min representative. m ≥ 3
  forces s ≥ 48; m = 2 forces s ≥ 32. Two rows of support 1, v e_k and v′ e_k′, are equal, or have k ≠ k′, v′ = −v and
  {k, k′} antipodal for the pair (VS); so the support-1 rows take at most two vector values.
- **M1 (general integers, s ≤ 19).** If m = 1 and s ≤ 19, at least 13 rows have support 1, so one vector value v e_k
  is carried by a set C of at least 7 rows; E′ = E − 1(v e_k)ᵀ (gauge) has C among its zero rows and support at most
  (s − |C|) + (16 − |C|) ≤ 21 < 24, so by RS it is Diţă.
- **NS (subtree Diţă pruning).** At a DFS node, if for some census subspace every free row's candidates contribute the
  same vector to the subspace's equations and fixed part + contributions = 0, every leaf below lies in L_S; the subtree
  is skipped. Sound by linearity. Countercontrol: dropping the "= 0" clause loses every witness leaf at budget 48.
- **O (orbit support = gauge support)**: see the section on support.
- **Transposition.** SIG is symmetric and the census contains both forms of each structure (the row form is the column
  form applied to Eᵀ), so straightness, N18, Ncomplete and support are transpose-invariant; a min representative with a
  zero column but no zero row is handled as its transpose.

## Searches (all exact; floats nowhere in a verdict)

| run | case | space | result |
|---|---|---|---|
| `m0all_b39_first13` + `m0all_b39_part2` (`dfsR2.py`) | min rep has a zero row, r ≤ 13 nonzero rows | D1; every row set R (no symmetry) with r ≥ 2 and LB(R) ≤ 39 and r ≤ 13: 2 814 + 2 680 = 5 494 row sets; mode-0; Lemmas CV, LB, NS | 2.33 M nodes, 228 374 subtrees pruned by NS; **0 leaves outside N18** |
| `sat_hr39` (`sat_hr.py`) | zero row, r ≥ 14 (the 104 remaining row sets) | D1; row 0 zero (WLOG), ≥ 14 nonzero rows and columns (WLOG by transposition), mode-0, s ≤ 39 | **UNSAT**: no straight line at all |
| `sat_m1_39` / `sat_cubes39` | no zero row and no zero column (m ≥ 1) | D1; row 0 a minimum line, of support ≤ 2 (WLOG); every line nonzero; mode-0; s ≤ 39 | NOZERO_RESULT |
| `sat_nd39` (`sat_nondita.py`) | all cases at once, as a cross-check | D1; straight + mode-0 + s ≤ 39 + outside all 18 subspaces; no symmetry | SATND39_RESULT |
| `dfs01` zero / two | D01 | {0,1} representatives with s ≤ 47 and a zero row; all rows of support ≥ 2 with s ≤ 32; support-1 rows by Lemma G1 | 12 520 + 288 leaves, all in N18; supports 16 and 32 only (Lemma P on every leaf) |
| `spanAll_77` (`spanAll.py`) | general integers, zero row | every row set with r ≥ 2 and LB ≤ 77 (65 390) | 13 922 dead; every row set with LB < 24 is dead |

Case split for D1 at s ≤ 39. Let m be the least support of a line (row or column) of the min representative.

- m ≥ 3 would give s ≥ 48, so it cannot occur.
- m = 0: there is a zero line, and by transposition a zero row. This case is covered by the DFS for r ≤ 13 and by
  `sat_hr39` for r ≥ 14. A min representative with more zero columns than zero rows is transposed first; its transpose
  has r ≤ 13 and is covered by the all-row-set DFS.
- m ∈ {1, 2}: covered by `sat_m1_39` / `sat_cubes39`.

Transposition preserves straightness, D1 and N18, because SIG is symmetric and the census contains both forms of
each structure.

## Controls (preregistered in PREREG.md; status measured)

- **C1:** the budget-48 DFS on the act-38 witness's row set returns 8 192 leaves, all N18-non-members, and the
  witness itself is among them (`ctrl_wit48`). **Green.** The budget-40 SAT with the non-Diţă constraint returns a
  support-40 straight line outside N18 (`sat_nd40`). **Green:** the encoding can see the witness regime.
- **C2:** the budget-16 D1 search over every row set returns 896 leaves, including A, B, C and −A, all in N18
  (`ctrl16.py`). The D01 enumeration contains A, B and C, and all its support-16 leaves are in N18. **Green.**
- **C3 countercontrols:**
  - The broken NS rule (drop the "= 0" test) turns C1's 8 192 witness leaves into 0 (`ctrl_wit48_broken`).
    **Green:** the pruning visibly changes results when broken.
  - A with one entry removed is rejected by the tables, by `straight_direct` and by the SAT encoding. **Green.**
  - The regime SATs are satisfiable when the budget is raised: `sat_m1_64` finds a support-64 straight line with no
    zero line, and `sat_hr64` finds one at r ≥ 14. Both were checked by `straight_direct`. **Green:** the UNSATs are
    not vacuous encodings.
- **C4:** the found leaves were rechecked exactly with `straight_direct`: 20 random leaves of C1 and every classified
  orbit class of the support-40 set. **Green.**
- **D2 control:** the {−2..2} search on the act-38 witness's minimal row set at budget 44 returns 32 768 leaves in
  1 024 orbit classes (supports 40 and 44), including the act-38 witness's class (`ctrl_wit44_k2`). **Green.**
- **Lemma checks** (`lemmas42.py`, all PASS): L1 (minimal vanishing sizes {2, 6}), L2 (msize ≥ ⌈16/r⌉ on all
  16·2¹⁵ pairs), L3 (stabilizer), L4 (Lemma P on 12 812 matrices).

## Provenance and quarantine

Processes that were stopped by hand, crashed or were superseded are listed with hash, size and mtime in
`quarantine/MANIFEST.txt`, their content untouched, and no verdict uses them. There were two MemoryError crashes of
the budget-47 DFS; the fix was byte-keyed dedup of equation contributions. The budget-47 SAT and DFS runs were
stopped as too slow, and so were the exact branch-and-bound min support and the first classification. The one range
whose killed log a verdict would otherwise have relied on (m0all_b39 indices 0–2 818) was **rerun** as
`m0all_b39_first13`. On the reported container restart: in this container the four live processes at that point
(`m0all_b39_part2`, `sat_m1_39`, `sat_nondita 39`, `classify_found`) were still running with continuous logs. Their
PIDs and elapsed times were unchanged, so none of them was restarted.

## What a native round could freeze

- **Kernel (Lean):**
  - E40's realizability identity: for every row pair, the level-set sums vanish. These are 120 pairs of finite
    Gaussian-rational identities, the same shape as act 38's realizability lemma.
  - For each of the 20 structures, a witness identity excluding it on the arc, as in act 38 item 3 but with E40.
  - Lemma P and Lemma D are short algebraic proofs that could be kernel-checked.
  - Lemma U (Donoho–Stark) is kernel-feasible, but only worth it if the general-integer bound s ≥ 16 is to be
    published.
- **Probe (exact computation):**
  - the generic structure search on E40 (0 candidates everywhere);
  - the D1 exhaustive exclusion for s ≤ 39 (DFS + SAT; the UNSAT results would need DRAT proof logging for a
    certificate-grade freeze, since the SAT solver's answer is not otherwise checked);
  - the R-span table;
  - the orbit-minimal support 40, which needs an exact lower-bound argument in place of HiGHS. The exact
    branch-and-bound `minsupp.py` exists but was too slow here.
- **Not freezable yet:**
  - "40 is minimal over all integers" is open for 20 ≤ s ≤ 39 outside D1 (entries ≥ 2 in absolute value in every
    min representative), and for 20 ≤ s ≤ 23 in the no-zero-line case.
  - The supports 41–43 and 45–47 are undetermined.

## Caveats

- The D1 exclusion is exhaustive over its precisely defined space. Outside it (min representatives needing |entry|
  ≥ 2), "none found" has not been searched beyond the D2 control, and is **not** claimed.
- The UNSAT verdicts rest on CaDiCaL 1.5.3 (via python-sat) without proof logging, and on the CNF encoding, whose
  vanishing clauses come from the exact pair-structure lemma VS (checked against the exact tables for every pair).
  The zero-row case, the bulk of the space, rests on the independent numpy DFS, which does not use SAT.
- The orbit minima 40 and 44 rest on HiGHS optimality, which is floating point. The attained values are exact.
- These results say nothing about act 38's frozen claims, which concern its own witness and remain as landed. They
  bear only on a "minimal support" statement, if one is ever drafted: act 38's {0,1} support of 48 is not the
  orbit-minimal support of its class (44), and the least support of a non-Diţă class is ≤ 40.
