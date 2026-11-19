# A1-02 — Measured P6 reciprocity in Lean

**Status.** Draft formalization of the accepted conditional theorem.

**Authority.** On 2026-11-16 owner amaybaum replied “Proceed” in the A1-02
worker session for the scoped formalization. Codex is the sole writer.
[Owner authorization on #1169](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6914517462)

**Goal link (§A.47).** #1169, priority 2. Check the conditional mathematical
reciprocity input to Stage 2(f) of P12(b).

**Source pin.** Main at `0283ba315e8c8a8f1465a91eea8613f9aa213ab5` contains the
accepted P6 paper from #1318 at `9ca4a168d7aacaa3d542f862181c9eb49fc584f3`.
Post-merge CI passed. At activation no open PR changed the census file or
claimed the A1-02 module. [Landing verification](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6915492953)

| Paper step | Declarations in `OIBridge.MeasuredReciprocity` |
| --- | --- |
| P6 §§2–3, one normalized law and matching endpoint masses at all lags | `reciprocal_flux` |
| P6 §3, weighted comparison and equal positive roots | `weighted_transition_reciprocity`, `transition_reciprocity_of_equal_roots`, `transition_reciprocity_iff_of_pos_flux` |
| P6 §3, zero paired flux with positive denominators | `transitions_eq_zero_of_zero_flux` |
| P6 §§2–4, common product law and equal positive root masses | `common_hidden_root_mass`, `common_hidden_law_reciprocity` |
| P6 §4, measured quotient equals the existing finite count divided by the hidden cardinality | `finite_uniform_transition_eq_count`, `finite_uniform_reciprocity` |

The measured result takes a measurable carrier, finite discrete visible
labels, a bimeasurable bijection, a cut-compatible reversal, and a single
normalized law invariant under both maps. In the product case the hidden
law is invariant under hidden reversal. Invariance of the joint law under
the dynamics remains a hypothesis. A zero-mass root has no positive
witness for `transition`. The finite product specialization uses
nonempty visible and hidden sets for the uniform probability law.
The original `Reciprocity.theorem_19` and its counting interface remain in
their original module and manuscript census family.

**Reproduction.** From `verification/lean-mathlib` with Lean 4.33.0, run
`lake --rehash build OIBridge.MeasuredReciprocity` after setting up the
pinned Mathlib dependency. The module emits axiom reports for the result
declarations. From the repository root run
`python3 tools/lean_manuscript_census.py`.

**Checkpoint verification.** The focused build and census check pass
locally. All eight result declarations report only `propext`,
`Classical.choice` and `Quot.sound`. The draft PR tracks the exact
published revision and its ordinary CI.

**Physical source.** NOT PASSED. The kernel statements are conditional on
the law and the reversal hypotheses. Physical law selection remains open
under Q6. The use in P12(b) still requires the same declared carrier and
cut.
