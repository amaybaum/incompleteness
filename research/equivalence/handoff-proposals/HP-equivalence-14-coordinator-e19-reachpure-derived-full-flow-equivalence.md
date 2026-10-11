# HP-equivalence-14 — to the coordinator (research/overview): E19 closed — `ReachPure` is a theorem; given H1 and H3, `K = Q3` iff the gate and the clause's two operations (research only)

From `research/equivalence`, round 5 (node E19, under the owner's round-5 directions), base L = `9f9f8257`. Nothing
here is certified; every statement is in the invariance reading.

1. **`ReachPure` derived** (R-E19.4; NOTES-E19 §3). The gate (H2) and one copy's rotations about the third axis at
   every angle with its cyclic permutation (A_miss) give invariance under the block-diagonal `SU(2) × SU(2)` by exact
   finite words — no closure, density or continuity, and neither H1 nor H3 (`blockInvariant_of_drive`); S6's
   reachability statement is a theorem about the drive words (`reachPure`). Design run 38134245361 (dev `f0c36cf9`,
   Mathlib bridge job 114454742595: Build success, 12/12 prints standard). Label: CONJECTURE (design run).
2. **The full-flow equivalence, each direction its own theorem** (§A.34). Sufficiency: H1 ∧ H2 ∧ H3 ∧ A_miss ⇒
   `K = Q3` (`pairCone_eq_Q3_of_drive_exact`); necessity: `Q3` is invariant under the gate and the clause
   (`Q3_cnot`, `Q3_aMiss`); together, given H1 and H3, `K = Q3 ↔ (H2 ∧ A_miss)` (`pairCone_eq_Q3_iff_drive_exact`).
   The block form: given H1 and H3, `K = Q3 ↔ BlockInvariant` (`pairCone_eq_Q3_iff_block`, run 38132266383).
   Label: CONJECTURE (design runs).
3. **The circularity check, closed.** The forcing conditions do not contain the conclusion: H2 and A_miss mention no
   positivity, no `Q3`, no pure state and no reachability; the transitivity of the generated group on pure states
   modulo products is proved. Each hypothesis is load-bearing with an exact witness (R-E19.6). Exact generation and the
   closure/density steps are kept apart: the full-flow form uses no closure; the one-irrational-angle form needs (i) `K`
   closed (from H3), (ii) continuity, (iv) the closure lemma — all [D] — and DENSE(θ₀) [L] (R-E19.5).
4. **Classification of the hypotheses** (stage-6 inventory): H1 the products clause of I3.43 (assumed); H2, H3, A_miss
   introduced (I3.148, I3.149, I3.165 with I3.150/I3.153); `ReachPure` not a hypothesis. Forms: OI + {H2, H3, A_miss}
   ⇒ K = Q3; OI + {H3} ⇒ (K = Q3 ↔ (H2 ∧ A_miss)).
5. **Bearing on the decisive outcome (A)–(D)** at the scope of pair cones over two copies of `eball 3`: not (A) — the
   drive is not derived here; the drive H2 ∧ A_miss is necessary and sufficient for `Q3` given H1 and H3, so (B)
   against (C) is the drive's source (O14, B20); (D) for the finite-order parts (`K384`, `K768`, `KC`), nothing about
   extensions supplying an infinite-order rotation.
6. **Draft S6 revised** (`preregistration-drafts/S6-k2-schema-pair-cone.md`): statement, premise list, six decision
   cells, earned reading and non-inference rule, the countercontrol family on `theorem_Sprime_ineq` with its
   hypotheses checked exactly (R-E19.1), checkpoints `C0″`, `C0‴` met. Proposal: the S6 draft is ready for owner review
   in this form; a round would also have to settle how the two bridge-thread declarations §H.6 uses (`cnotMat`,
   `dict_cnot`) enter the frozen surface.

**May not be assumed:** that S6 or any preregistration became a round; that the design modules are certified; that
H2, H3 or A_miss is an OI premise or is sourced; that invariance gives availability; that the finite-order
insufficiency extends to OI with continuous control.
