# A40 pre-freeze design and measurement — at D = b271b1df (no F)

Target (owner, verbatim in intent): H₃(u₁,u₂,u₃) admits a Diţă structure — every admissible shape, index map
and orientation, including diagonal equivalence — iff u₁ ∈ {±1} ∨ u₂ = 1 ∨ u₃ ∈ {±1}; frozen as a two-layer package:
kernel ⇐ (whole-face existence) and kernel exclusions at the named maps; exact probe ⇒ (global exhaustion).

## 1. Runtime (single-threaded, clean start, this container)

| pipeline | phase | time |
| --- | --- | --- |
| old (closure) | base pair-block loci (320) | 14 s |
| | closure under intersection (9944 flats) | 47 s |
| | 9945 containment patterns | ~15 s |
| | candidate search per pattern (46 candidates) | 636 s |
| | strict + relaxed loci | < 1 s |
| | **total** | **≈ 737 s** (peak RSS 34 MB / 76 MB) |
| new (clique enumeration, no closure) | pair-block loci per block + clique partitions + exact covers (46 candidates) | 16 s |
| | strict + relaxed loci, union reduction | < 1 s |
| | flat-calculus self-tests | 5 s |
| | controls (diagonal; act 37's census of the eighteen structures at the stratum point (1, 1, 1) — not the {0, 1} exponent census, which is neither used nor computed; M_COL/M_ROW at (−1, −1, −1); absent face u₂ = −1; A39 pair faces) | < 1 s |
| | kernel replay (20 named witnesses, 15 face factorizations) | 1 s |
| | independent control: act 36's exhaustive structure search in exact Gaussian rationals (no floating point), 17 exact points | ~98 s |
| | countercontrol (full classification of a perturbed family) | ~19 s |
| | **probe total** | **≈ 141 s**, peak RSS ~30 MB |

The two completeness methods return the **identical** 46-candidate set.

## 2. Completeness argument used by the probe (replaces the closure)

A Diţă structure (column blocks cp, row classes P, shape m×n) admitted at u: rows of one class are proportional on every
block and rows of different classes are not (the Y factors are flat unitary), so the class partition is the same on every
block and every within-class pair's proportionality locus on every block contains u. Hence (cp, P) has a nonempty joint
proportionality locus. The probe enumerates, per block S, the partitions of the rows into cliques of size m with a common
point, and per partition the exact column covers by m blocks with a common point: every admitted structure is among the
results. The exact strict and relaxed loci then decide. (The 9944-flat closure is an alternative internal method; it is
recorded here as design evidence and agrees exactly.)

## 3. Flat calculus hardening (embedded in the probe, not imported)

Random systems: canonical form idempotent, generator-order independent, every generator holds; meet symmetric and
associative; meet contained in both and equal to F iff G ⊇ F. Hand systems (satisfiable / unsatisfiable / containment
direction). Independent reconstruction: explicit Gaussian-rational points on unit-pivot flats satisfy every original
equation exactly, and moving u₁ off a flat that constrains it is detected.

## 4. Kernel design

- X = ((1+i)/2)·[[1,1],[1,−1]], D = 2/((1+i)(1+i)) (= −i), Y_c = ((1+i)/4)·(class-representative rows of 4H₃ on
  block c): on all five faces the ratio to the class representative is exactly the 2×2 Fourier sign pattern; the free
  units live only in Y. All scalars are Gaussian rational; unitarity of Y_c reduces to 8×8 monomial row identities.
- Named exclusions: each of the 20 named structures has single four-position witnesses with coordinate characters that
  generate its proportionality locus exactly; kernel statement = "Diţă form at those maps ⇒ those coordinate equations".

## 5. Kernel rehearsal (disposable branch claude/a40-dev from D; design evidence only)

| run | head | module | outcome |
| --- | --- | --- | --- |
| 36430858292 | a2357372 | v0, literal-Y faces | header polluted by generator output — no elaboration |
| 36431692617 | 03d28272 | v1, literal-Y faces (240 theorems, 1.2 MB) | red after **56 min** of bridge build: too heavy; 9 exclusions with a residual `True ∨ u = 0` from simp on an entry equation |
| 36439639584 | e4266bf4 | v2, generic face lemma per structure | red, **9 min** build; exclusions as before |
| 36440020816 | 76a5c98c | v3, generic lemma with concrete-row relations | red, 9 min; same |
| 36441143645 | ea12762c | v4, entries evaluated on the left only; faces last | red, ~9 min: **all 20 named exclusions and their frozen theorems clean; all 40 face relation lemmas clean**; the generic face lemma fails in two steps (no `1 + i ≠ 0` in context for field_simp; the block-unitarity rewrite pattern) |
| 36442265583 … 36448890710 | e601ab8f … 653c0ace | v5–v9, generic-lemma repairs | red; block unitarity, D value and D norm repaired; the per-row identities (M(i) = (XDY)(i)) still failed on two artifacts: `ring` falls back to `ring_nf` without failing, and the class-representative index left unreduced by simp |
| 36450535104 | 5eec100c | v10, explicit κ cancellation | red; the same row identities (the factor κ²κ⁻² sits in positions no rewrite matched) |
| **36451750208** | **f34feea0** | **v11, each row identity by a definitional `show` to its class representative plus one scalar lemma ((1+i)/2 · s · 2/(1+i)² · ((1+i)·m) = s·m)** | **green, all eight jobs: 199/199 theorems clean ([propext, Classical.choice, Quot.sound]), gate lean-axioms 5251 (= 5052 + 199), no sorry; bridge 12m01s** |
| **36453414586** | **d6d95cda** | **v12, the intended frozen form: `--verdict` output without design options (no `set_option`, one `#print axioms` per theorem, as the landed A39 module); module blob 0d42d28e** | **green, all eight jobs; gate lean-axioms 5251 named results, no sorry; every axioms line seen reads [propext, Classical.choice, Quot.sound]; v3-receipts 15 hold; legacy 303 intact** |

Remaining module warnings are cosmetic and match the landed A39 module's pattern (unused `let` binder names in the frozen statements).

## 6. Kernel countercontrol (disposable branch claude/a40-counter; never landed)

Two perturbations, predicted before the run from the probe's exact monomial calculus and the module's dependency closure:

- **absent face**: the u₂ = +1 face's proof with u₂ := −1 (same t1 structure, column form). Exact prediction: of the eight
  partner-row relations, 0–3 fail (the ratio is not a block sign pattern) and 4–7 still hold; the u₂ = +1 control holds all eight.
- **exclusion**: in the named exclusion (k1, column form) the two witness conclusions' values are flipped (u₂ = −1, u₃ = −1
  in place of +1); the cancellation must fail.

Predicted red set (transitive closure of dependents in the module): exactly 9 of 199 — face_2p_rel0–3, face_2p_core, the frozen
face_2p, excl_k1_c_core, the frozen excl_k1_c, and a40_classified; the other 190 clean.

| run | head | base | outcome |
| --- | --- | --- | --- |
| 36450749717 | 7dacbc0f | v10 (face cores already red) | differential exactly as predicted: newly red face_2p_rel0–3, excl_k1_c(_core); rel4–7 and the other 19 exclusions clean |
| **36452360434** | **c3821642** | **v11** | **red set exactly the predicted 9; 190 clean** |

## 7. Probe placement

Measured on a disposable branch from D (claude/a40-probe, run 36453264799, eight jobs green), the probe alone in its own shard:
**1m24.6s wall, 84.5 s user, peak RSS 33 MB, job 1m32s**; cumulative section times 3 / 15 / 15 / 15 / 15 / 16 / 72 / 84 s
(sections 1–6 ≈ 16 s; the independent exact structure search ≈ 56 s; the countercontrol ≈ 12 s). For comparison in the same run:
A38 escape shard 4m41s, core A 2m40s, core B 2m46s, A36 2m07s, foundations 1m34s, Mathlib bridge 8m51s (12m01s on the
uncached v11 build).

Recommendation: an own shard, `Numerical probes / A40 locus`, added to the `probes` aggregator's `needs` and its result check.
Either placement stays off the critical path (the bridge dominates), but an own shard keeps each round's probe independently
attributable and leaves the A38 shard's recorded timing unchanged; appending to the A38 shard would make it ≈ 6m10s.
