# The Diţă locus of H3(u₁, u₂, u₃) = SIG ∘ u₁^A u₂^B u₃^C in the three-torus — read-only measurement at D = 08a7707d

This is a measurement, separate from A39: it is not part of A39's freeze, and A39 neither consumes nor asserts it. Its purpose is to seed the next structural round.

The whole measurement is exact, with no sampling in the derivation. Scripts: `flats.py`, `locus39.py`, `locus39b.py` and `locus39_controls.py` (scratchpad `a39/`). Every object comes from act 38's landed probe head.

## Method

**Characters.** Every entry of H3 is a monomial `i^p z^q w^r u₁^a u₂^b u₃^c`, with `(a, b, c)` taken from A, B, C.
- Each proportionality condition and each rank-one condition of a Diţă structure (fixed shape, fixed index maps, fixed orientation) is a **character equation** `u^k = c`. Here `k ∈ Z³`, and `c ∈ ⟨i, z, w⟩ ≅ Z/4 × Z²`, which is free modulo roots of unity because z and w are quotients of distinct Gaussian primes by their conjugates.
- The solution set of finitely many such equations is a **flat**: a lattice Λ ≤ Z³ together with a character χ on Λ. It is stored in canonical HNF form. Intersection, containment and the component count (gcd of maximal minors) are all exact.
- Containment is exact on solution sets: a character is constant on a flat iff it lies in Λ, by Pontryagin duality.

**Pair-block loci.**
- For every orientation, every block size n ∈ {2, 4, 8}, every n-subset of columns and every row pair, the locus where the pair is proportional on the subset is either ∅, T³, or one of **320 distinct proper flats** (by dimension: 80 of dim 0, 172 of dim 1, 68 of dim 2).
- The closure of these 320 flats under intersection has **9944 flats** (8480 of dim 0, 1396 of dim 1, 68 of dim 2).

**Why candidates at generic points suffice.**
- At any point u, the pattern of proportional pairs is the pattern at a generic point of F_u. F_u is the intersection of the base loci through u, so it lies in the closure.
- Rows in different classes are never proportional on a block, because the Y factors are flat unitary. Class sizes are therefore exact.
- So every structure admitted anywhere on T³ is a proportionality candidate at a generic point of some closure flat.
- Candidates were found once per distinct containment pattern: 9945 patterns, giving **46 distinct candidates** over both orientations and the shapes 4×4, 8×2 and 2×8.
- Each candidate was then given its exact locus as a flat:
  - **strict**: proportionality and rank-one;
  - **relaxed**: proportionality and rank-one up to the row factor, i.e. up to diagonal equivalence.

## Result

**Strict = relaxed for every one of the 46 candidates.** Diagonal equivalence enlarges nothing, anywhere on T³.

**16 candidates have empty locus.** For these, proportionality holds somewhere but rank-one never does:
- column 4×4: 6;
- column 8×2: 1;
- row 4×4: 7;
- row 8×2: 2.

**30 structures have a nonempty locus.** Every equation is a coordinate condition `uₖ = ±1`, and every nonempty locus is a single coset (one component):

| locus | structures |
| --- | --- |
| u₁ = 1 | column 2×8 — blocks by parity of d, classes (0,2)(1,3)(4,6)(5,7)(8,10)(9,11)(12,14)(13,15): the census `t2` column form |
| u₁ = −1 | column 2×8 — blocks by parity of d, classes (0,2)(1,3)(4,6)(5,15)(7,13)(8,10)(9,11)(12,14): act 38's `M_COL` |
| u₂ = 1 | column 2×8 `t1` (act 36's frozen class); row 2×8 `t3` |
| u₃ = 1 | row 2×8 `t1` |
| u₃ = −1 | row 2×8 — blocks (0,1,2,3,8,9,10,11)/(4,…,15), classes (0,2)(1,9)(3,11)(4,12)(5,13)(6,14)(7,15)(8,10): act 38's `M_ROW` |
| u₁ = −1, u₂ = 1 | column 2×8 |
| u₁ = −1, u₃ = 1 | row 4×4 |
| u₁ = 1, u₂ = 1 | column 2×8, column 4×4 |
| u₁ = 1, u₃ = −1 | column 4×4 |
| u₁ = 1, u₃ = 1 | column 4×4, row 4×4 |
| u₂ = 1, u₃ = −1 | row 2×8 |
| u₂ = 1, u₃ = 1 | row 2×8, row 4×4 ×2, row 8×2 |
| (−1, 1, 1) | row 4×4, row 8×2 |
| (1, 1, −1) | column 4×4 ×2, column 8×2 ×2 |
| (1, 1, 1) | column 4×4 ×2, column 8×2 ×2, row 4×4, row 8×2 |

**The Diţă locus is exactly the union of five coordinate 2-subtori:**

    Dita(H3) = {u₁ = 1} ∪ {u₁ = −1} ∪ {u₂ = 1} ∪ {u₃ = 1} ∪ {u₃ = −1}

Every lower-dimensional locus lies inside one of these five. So H3(u) admits a Diţă structure of some shape, index map and orientation, strictly or up to diagonal equivalence, **iff** at least one of the following holds:
- u₁ ∈ {±1};
- u₂ = 1;
- u₃ ∈ {±1}.

The complement is open and dense in T³, and every point in it is realizable (by A39) and non-Diţă.

## Structural reading (for the next round to test, not asserted here)

- **The escape is genuinely three-parameter.** Each pair subfamily lies entirely inside the locus:
  - (B, C) is the face u₁ = 1, with structure t2;
  - (A, C) is the face u₂ = 1, with structures t1 and t3;
  - (A, B) is the face u₃ = 1, with structure t1.

  A point escapes only when all three pieces are switched on, with u₁, u₃ ∉ {±1} and u₂ ≠ 1.
- **A38's two exceptional structures at u = −1 are not isolated in T³.** They are the diagonal traces of the whole 2-tori {u₁ = −1} (column, `M_COL`) and {u₃ = −1} (row, `M_ROW`). On the diagonal these meet only at (−1, −1, −1).
- **Asymmetry.** {u₂ = −1} is not in the locus. The B-piece has no −1 face, while A and C each do.

## Controls (all pass; `locus39_controls.py`)

- The diagonal restriction u₁ = u₂ = u₃ gives exactly the points u = 1 and u = −1, which is act 38's exceptional set.
- At (1, 1, 1) the count is 18 structures, act 38's census.
- At (−1, −1, −1) the count is 2 structures: one 2×8 in each orientation, `M_COL` and `M_ROW`.
- **Independent control.** Act 36's numeric exhaustive search with factor unitarity (`dita_orientations`) was run on the exact Gaussian-rational matrix H3 at 17 points. It shares no code with the flat calculus. At every point it finds exactly the predicted set of structures (orientation, shape, blocks and classes all match).

| point | structures found | notes |
| --- | --- | --- |
| generic (u₅, u₁₇, u₂₉) | 0 | |
| generic (u₂₅, i, u₅) | 0 | |
| u₁ = 1 face | 1 | |
| u₁ = −1 face | 1 | |
| u₂ = 1 face | 2 | |
| **u₂ = −1** | 0 | predicted outside the locus |
| u₃ = 1 face | 1 | |
| u₃ = −1 face | 1 | |
| **u₁ = i** | 0 | predicted outside the locus |
| (1, u₂₉, −1) | 3 | |
| (u₂₉, 1, 1) | 7 | |
| (−1, 1, u₂₅) | 4 | |
| (1, 1, 1) | 18 | |
| (−1, −1, −1) | 2 | |
| (−1, 1, 1) | 12 | |
| (1, 1, −1) | 12 | |
| (1, −1, 1) | 4 | |

## Skepticism notes (§A.31)

- **Exhaustiveness rests on the closure argument, not on the 17-point control.**
  - The closure argument covers every point: any u has pattern(u) = pattern(F_u), with F_u in the closure.
  - It depends on two things: the exact class-size condition (orthogonality of the unitary Y factors), and exact containment for flats.
  - flats.py's `_hnf` and meet were stress-tested over 2622 random cases before use.
- **A later kernel round would need its own proofs.**
  - Existence: exhibit a Diţă form on each of the five subtori. This is kernel-provable by reconstruction, as A38 did at u = −1.
  - Exclusion off the union: on A38's precedent, this sits in the exact-computation layer.
  - Nothing here is kernel-certified.

