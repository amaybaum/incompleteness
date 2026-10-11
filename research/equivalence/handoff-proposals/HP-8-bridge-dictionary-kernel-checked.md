# HP-8 — to the bridge thread: the two-token dictionary kernel-checked in a design run, and the `dict_tens` fix corrected (research only)

From `research/equivalence`, round 3 (node E11; NOTES-E11; R-E11.1–R-E11.4), base L = `9f9f8257`. Nothing here is
certified; every [D] item is a design run on a disposable branch, not a round.

**Statements.**
1. **The dictionary, built.** With `BridgeDictionary.lean`'s definitions `pauli`, `tokMat`, `dict` verbatim (read at
   `origin/research/bridge` `3686049e`, sha256 `e4b60411…`), the design module `EqvK2Schema` proves: the product law
   `dict_tens : dict (tens X Y) = tensorOf (tokMat X) (tokMat Y)` and `dict_prodState`; real linearity (`dict_add`,
   `dict_smul`, `dictLin`, `dict_sum`); Hermiticity; the pairing `trace_dict_mul : tr (dict ω · dict η) = ipW ω η / 4`
   and `ipW_eq_trace`; completeness `dict_complete4 : Σ tr(T_μν H) • T_μν = 4 • H`; injectivity; and the linear
   equivalence `dictEquiv : W 3 ≃ₗ[ℝ] selfAdjoint (Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)`. All 22 prints of the module
   are `[propext, Classical.choice, Quot.sound]`. Label: CONJECTURE (design run). Evidence: [D] run 38101580750 on
   `dev-equivalence/k2-schema` `aabc649e`, Mathlib bridge job 114358419270 (Build success, 3644 jobs; EqvK2Schema.lean:453–474;
   gate red only at `lean-manuscript`; `lean-axioms` 5882, no `sorry`); the text is `research/equivalence/lean/EqvK2Schema.lean`
   (blob `659ae36c`).
2. **The recorded `dict_tens` fix does not elaborate as written.** NOTES-B9 §4's fix ("full expansion, then `ring`") fails
   in Lean v4.33.0 / Mathlib v4.33.0: `simp` expands the inner matrix-valued sums with `Fin.sum_univ_four` before
   `Matrix.sum_apply` can distribute the entry, leaving `(A + B + …) (i, j) (k, l)`. Adding `Matrix.add_apply` (and, for
   traces, `Matrix.trace_add`) to the `simp only` list closes it; `dict_add`, written that way, built in both runs.
   Label: CONJECTURE (two design runs). Evidence: [D] run 38099025197 (job 114350890660; errors at `dict_tens` 105:87,
   `dict_smul` 122:67, `trace_dict_mul` 167:64, `dict_coordOf` 235:2; the failed text kept as
   `lean/EqvK2Schema.run38099025197.lean`) and run 38101580750 (the four lists changed, nothing else).

**Proposal.** The bridge's `BridgeDictionary.lean` can converge onto these statements and proofs (or import the design
module's text), so that one dictionary serves the SPEC side (HO-12's (D1)–(D2)) and the K2 schema.

**May not be assumed:** that any of this is certified at L; that the K2 schema built in the same module
(`pairCone_eq_Q3_of_drive`) is more than CONDITIONAL on H2, H3, A_miss and `ReachPure` (L4), none sourced; anything
about more than two tokens.
