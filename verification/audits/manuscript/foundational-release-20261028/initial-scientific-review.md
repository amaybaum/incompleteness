# Independent scientific/source review: foundational #982 + #992

Reviewed immutable commit: `a2be1e4573662d1331f2560ea06c2d8ed10bcd73` (tree `d8e95e610452fe018851fe14553c97a703c7db5b`), comprising #982 `20ca05fe` plus #992. Review performed read-only against the Git objects and a dedicated worktree. No repository files, branches or reviews were changed by this reviewer.

**Verdict: REVISE for integrated foundational source acceptance. ACCEPT the narrow #992 ancillary/regress correction.**

The blockers below are surviving stronger claims, not defects in the successful recovered theorems. Repair the summaries and their generated mirrors to the strongest proved scope. Preserve the Lean endpoints, written results and countercontrols.

## What checks out

1. **#992 correction.** `book/ch03-structural-realism.md:218,220` and FULL remove the claimed proof terminating the deeper-substratum regress. The positive replacement follows directly from Substratum Theorem 24(iii): with independently prepared normalized rho_D and exactly tensor-product dynamics, partial trace factors and the ancillary trace remains one. Finite and well-defined trace-class infinite ancillary cases are correctly separated from finite recurrence and coupled accessible-time approximations. The correction does not weaken any theorem, infer arbitrary hidden-state opacity, or claim complete gauge classification.
2. **SC-45 observational carriers.** Substratum:255–284 distinguishes fixed-interface coherent channels, rooted populations and an unclassified all-partitions comparison. A single hidden permutation preserves the uniform hidden state and disappears under partial trace; a visible-fibre-dependent hidden permutation preserves rooted counts but can change coherences; an arbitrary full-state relabelling can change even populations. The explicit swap/full-state-relabelling example has the stated matrices.
3. **SC-44 rigidity.** Substratum Proposition 24.2:298–304 preserves all corresponding block-word traces and the full block-span premise, and supplies the two directional Lean witnesses. I inspected `WT2gen_oneSided`, `blockSpanning_of_wordTracesEqual`, `WT3_spanning_iff` and the consumed necessity endpoint in the Git objects. Equality of separate visible channels is not treated as the missing word-trace hypothesis. Pair C is correctly kept as a counterexample. No local Lean build was performed.
4. **Theorem 23.** Its actual statement and proof at Substratum:189–203 retain the selected nearest-neighbor cubic branch, H-link single copy, octahedral representation, amplitude-scale and matter hypotheses, H-slope/horizon assumptions, and H-Bell. They prove branch-relative outputs without an inverse physical selector or complete microscopic orbit classification.
5. **Propositions 24.3–24.4.** Their written proofs support minimal linear word realization and the passive finite-permutation predictive quotient under the stated reachability/observability, full-support and known-state-bound hypotheses. The finite-length filtration proof is valid; on the passive quotient distinct future traces are separated by B−1 readouts and length-B data reconstruct successors and priors. The coordinate-indicator/ray argument makes the relevant similarity a permutation. These are written mathematical results, not new Lean certificates or a complete physical gauge theorem.
6. **Proposition 24.5.** The actual finite record-fibre theorem and partition-refinement proof at Substratum:352–365 are sound on the known-model/preparation/record hypotheses. The full-carrier N−1 bound does not assume preparation support is invariant. The current-hidden singleton criterion correctly uses the recorded current visible coordinate. The ledger entry remains `GAP`, `checks=[]`, with explicit written-proof status. The swap and cyclic-store examples correctly separate predictive memory from posterior state uncertainty.
7. **Recovered gauge mathematics.** SM Theorem 5, Proposition 14a, Theorem 15 and Proposition 15a have distinct, useful conclusions: conditional U(3)×U(2)×U(1) stabilizer; explicit correlated two-torus quotient; complete selected-family anomaly classification including the neutral-Q branch; faithful selected charged-family image with Z6 kernel. The algebra in their displayed proofs is consistent. The compact-charge strengthening is a written argument invoking the stated exponent-three theorem, not a claimed universal native Lean result.

## Blocking source inconsistencies and precise repair scope

### B1. Physical SM group still identified with the intermediate commutant/stabilizer

Authoritative anchors: SM:340–344 and :577–612; book ch05:119–135. The intermediate generic stabilizer has Lie dimension 14 and three central U(1) directions; the SM Lie algebra has dimension 12 and one central direction. A scalar coupling M=mu I6 has full U(6) commutant. The strict commutant of the multiplicity-free cubic-group action is U(1)^3, while its generated block algebra has unitary group U(3)×U(2)×U(1). None is simply the physical direct-product SM group. The selected correlated quotient and charged action are essential additional steps; their physical selection and complete global data remain open.

Concrete surviving sites:

- `book/glossary.md:75` (FULL:6648) calls the physical group the "unique commutant" conditional only on H-link.
- `book/ch04-methodology.md:118` (FULL:1205) equates SU(3)×SU(2)×U(1) with the unitary bicommutant / generic condensate stabilizer, omitting the two discarded central directions and H-cust/charged-action premises.
- `book/ch05-gauge-structure.md:101` switches from the corrected condensate Sigma back to eigenspaces of the coupling M and says gauge and masses are encoded in that same matrix.
- `papers/Explainer.md:830,838–842` retains the old M/mass/gauge story and calls the displayed U(3)×U(2)×U(1) group the SM group; :854 says hypercharge is automatic and no further empirical input is needed, even as the corrected anchors retain carrier/action/quotient/chirality obligations.
- `papers/Substratum.md:390,410` and `book/ch02-substratum.md:193` (FULL:837) still identify the SM group with the coupling-matrix commutant.
- `papers/SM.md:476,487,495` continues to say first-principles forcing / complete gauge-sector closure; :495's three diagonal singlets are not by themselves a construction selecting the one physical hypercharge gauge field.

Repair: retain the exact cubic decomposition and conditional generic stabilizer, then state the constructive quotient and selected faithful action with their actual premises. State a gauge Lie algebra or covering presentation when that is what is meant; do not silently identify different global groups. Propagate into TeX/PDF/FULL. Do not delete the quotient or stabilizer recoveries.

### B2. Fixed-family anomaly result still promoted to unconditional uniqueness or matter selection

Authoritative anchor: SM Theorem 15:591–604. Even on the stipulated five-representation family, `(a,u,d,l,e)=(0,1,-1,0,0)` satisfies all four nontrivial displayed anomaly coefficients and is not a rescaling of the SM ray. The nonzero-a clause (or the actual neutral-neutrino/Higgs charge premise) excludes it; numerical normalization is a convention/physical charge identification. Anomaly cancellation does not select the family among all fundamental/singlet spectra.

Concrete surviving sites:

- `papers/SM.md:458,462` (Theorem 10 and proof) calls the hypercharge assignment the sole consistent completion without nonzero-a/normalization hypotheses.
- `papers/SM.md:476` says matter content and its representations are uniquely derived rather than supplied by a selected charged action. This directly contradicts :587–612 and the current carrier/physical-status paragraphs.
- `book/appendix-b-derivations.md:18,227,229,472` retains overly broad uniqueness statements. In particular B.5.1 at :229 quantifies merely over fundamental/singlet fermions, whereas its actual proof fixes the SM family at :232 and chooses neutral-neutrino normalization at :261. Its repaired conclusion at :276–278 correctly states those premises and the exception; assert-then-qualify does not repair the theorem statement.
- `book/glossary.md:9,89` (and FULL) says unique numerical charges with no free parameters.
- `papers/Explainer.md:854` repeats automatic unique hypercharge without the premises.
- `papers/Substratum.md:165`, `papers/Juno.md:88`, `book/ch04-methodology.md:190`, and the Higgs-charge summary `book/ch06-matter-content.md:44` need explicit inherited fixed-family/nonzero-branch/normalization scope where they claim uniqueness or physical charges.
- `papers/SM.md:557` already says "given ... observed family" and "in the sense stated there"; preserve that conditional success, but making the nonzero branch explicit would avoid the remaining "landing uniquely" ambiguity.

Repair: qualify the actual broad statement B.5.1 to the family and neutral-neutrino/EM normalization used by its valid proof; preserve the stronger complete branch classification in SM Theorem 15 and its compact-charge strengthening. Keep input charge normalization distinct from the algebraic charge ratios. Update any canonical fingerprints/coverage only where the statement is actually changed; never promote written algebra into Lean certification.

### B3. Methodology still claims completed classification and universal state opacity/computational impossibility

Authoritative anchors: Substratum:193–203, :255–304, :352–365 and the correctly narrowed Methodology:453, :499–507.

- `papers/Methodology.md:455` says there is a foundational programme in which all three reconstruction/classification steps "are carried out", two lines after :453 calls the selector and classification unfinished. Replace completion by partial instantiation of the programme.
- `papers/Methodology.md:461` asserts that no embedded observer can recover information removed by its current trace-out. P24.5 and the exact swap show that retained records can recover the complete current state in a proper visible/hidden model.
- `papers/Methodology.md:469` asserts predicting the observer's future requires a computer at least as large as the whole system. Proper embedding alone proves no such lower bound; simple known reversible models have a predictable readout, and retained records may identify the current state. Replace by resource/access-conditioned examples or a precisely cited applicable impossibility theorem, preserving the distinction between factual uncertainty and gauge redundancy.
- `papers/Methodology.md:529,541,547` again treats substrate-only inability to compute representative-dependent quantities as general, and equates invariance with derivability, although :501 only proves that a carrier-restricted procedure cannot infer two different Q values from an identical outcome law and :507 explicitly rejects the computability converse. Propagate that actual conditional operational conclusion through these synthesis/audit summaries.

These are manuscript claims, not preserved historical evidence; they must agree with the new strongest record-fibre and scoped-equivalence results. No new universal no-go is needed.

## Positive supplement: preserve the strongest Pair C obstruction without an infinite-ancilla overreach

The existing Lean `ST4_pairC` quantifies over finite nonempty ancillary D. Substratum:280 permits well-defined infinite trace-class ancillary states, while :286 says the balanced trace invariant survives decoupled enlargement. A finite normalized matrix trace alone would not justify an arbitrary infinite-D chain. However, a simple stronger operator certificate closes this concern, without weakening the result:

For Pair C use the balanced word
`w0 = B00 B10 B01 B00* B01* B10*`
and its visible swap `w1`. Direct exact multiplication of the source permutation matrices gives:

- Pair C: `w0 = diag(1,0,0)`, `w1 = 0`.
- Pair C-prime: `w0 = 0`, `w1 = 0`.

A hidden-unitary conjugation conjugates each word. An independent decoupled unitary ancilla replaces a balanced word by `word tensor I_D`. Nonzero versus zero is preserved for any nonempty ancillary Hilbert space, finite or infinite, and visible swapping just exchanges the pair of statuses. Hence `(one nonzero, one zero)` cannot become `(both zero)` through any finite chain of the stated restricted moves and inverses. This is a written algebraic extension beyond the finite-D Lean statement, not an additional Lean certificate. It assumes the stated tensor-product/unitary moves, not arbitrary new operations or all-partitions equivalence. Adding this short operator argument would make the broad restricted chain claim fully explicit.

The independent small integer/rational control `exact_controls.py` records these four operator products, the neutral-Q anomaly counterexample, the standard anomaly solution, the two Lie dimensions and the swap's four singleton two-reading fibres. `python -I` and `python -I -O` produce byte-identical JSON with explicit failure guards. This supplements the proof, not a universal computational certification.

## Release boundary

This is an independent scientific/source review of the stated target and its load-bearing propagation, not certification of all physical claims in the repository, a local full-history release attestation, an exhaustive gauge classification, or a new Lean compiler run. No weakening/removal of the successful recoveries is recommended. After B1–B3 are repaired, re-review the exact resulting diff and verify regenerated publications and exact-head CI. #980/#981 remain separate provenance records. No merge is authorized.
