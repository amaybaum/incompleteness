# SC-44, phase 1: repair the mathematical statement of Lemma 24.1

**State:** DRAFT, lemma-only source change; not independently reviewed, not CI-verified, not merge-ready.

**Branch:** `corpus/sc44-lemma241-core`, created from `main` on 2026-10-28.
**First source-edit commit:** `f9af9d2df3efec14669d1a19778b53bc83988e68`.
**Changed manuscript:** `papers/Substratum.md`, the block from "**Completeness of the generators (conditional)**" to before "**The gauge hierarchy**".

## Claim-level correction

- **Original wording (main, Substratum §4, former Lemma 24.1).** Equal uniform-hidden-prior visible channel families `Φ_t` at every t imply a hidden partial-isometry intertwiner of the generating bijections up to exactly decoupled deep-sector enlargement; its three-part claimed proof imported Stinespring/GNS minimal dilation uniqueness.
- **Defect.** The family of single-time channels does not determine a simultaneous unitary intertwiner of the generating dynamics, even under the manuscript's proposed minimality reading. The kernel's `ST3_pairC` supplies two six-state permutation systems, both with trivial hidden commutants, equal channel families for all t, and different full-unitary traces (2 versus 0). `ST4_pairC` rules out the tested decoupled-enlargement/hidden-relabelling variant. Thus the previous lemma is false as stated; the completeness proof using it is not valid.
- **Replacement.** The false Lemma 24.1 is retired from the scientific exposition; a distinct *Proposition 24.2* states the already proved restricted theorem: on a fixed same-sized carrier, `BlockSpanning U` plus `WordTracesEqual U U'` implies `HiddenConjugate U U'`; the converse holds, and the condition transfers spanning to U'. This is already Lean-proved in `OIBridge/WordTraceSufficiency.lean`: `WT3_spanning_iff`, `WT2gen_oneSided`, `blockSpanning_of_wordTracesEqual`, and `WT1_transfer`. The necessity lemma `trace_wordEval_hiddenConjugate` is in `OIBridge/SemigroupTransfer.lean`.
- **Downstream.** Theorem 24 and Theorem 23's completeness-dependent uniqueness claims, Substratum §4 steps/conclusion, synthesis, Structure, Methodology, Complexity and book chapters have unresolved stale references; **phase 1 does not claim to fix them**. SC-43's turtles discussion and Introduction r32 must cite the corrected status, not the false old route. SC-44 phase 2 must correct all dependent statements and mirrors with an independently audited site inventory.

## Exact evidence and limits

- `ST3_pairC` (Lean): equal families; no unitary conjugacy; traces 2 and 0.
- `pairC_wordTraces` (Lean): the counterexample's block-word traces differ, so it is outside the strengthened hypothesis.
- `ST4_pairC` (Lean): the decoupled-enlargement control at its precise frozen scope.
- `WT3_spanning_iff` (Lean): equivalence between same-carrier hidden conjugacy and equal all-word traces **on the block-spanning class**. The stronger one-sided `WT2gen_oneSided` justifies that a single spanning hypothesis suffices.
- All Lean declarations and frozen research records were consumed unchanged. This phase does **not** introduce a new Lean theorem, run Lean, or assert fresh axiom-check/CI results.

## Still open (not entailed by the repaired lemma)

1. Whether the actual chosen observables include all block-word traces rather than just transition laws or single-time channels. The 24.1B control plane is frozen, but its manuscript determination is not a result until execution is reviewed.
2. Whether the physical class satisfies block spanning; 24.1C separately controls the relation to `HiddenCommutantTrivial`.
3. Whether a general non-spanning algebra has a spatial implementing unitary (WT2 general undecided in 24.1A).
4. Which hidden/visible relabellings generator (i) permits. A complex hidden unitary does not automatically equal a finite-set permutation.
5. The effect of requiring observables to agree across all partitions, and of coherent/multi-time observable information, on the proposed four-family completeness.

## Phase-1 review / reproduction gate

- Re-read the exact theorem statements and hypotheses in the two Lean modules; confirm the manuscript makes no stronger inference from them.
- Check that the old false proof and its final square were removed from Substratum §4 and the counterexample and negative control are quoted at their proved scope.
- Do **not** call completeness proved, refuted, or restored. Do **not** close SC-44 on the strength of the new lemma alone.
- Re-run the applicable release gate, citation/coverage checks, and Lean axiom check on the exact final SC-44 head, with independent ACCEPT; none has been run as part of this drafting step.
- In phase 2, reconcile the dependent approximately 15 false statements and approximately 30 stale statements, all mirrors, SC-43, and r32; require independent review and exact-head green CI before any merge proposal.

**Merge authorization:** none. Publication blocker for #918.

## Writer revision and review handoff (2026-10-28)

The initial lemma-only draft at `1576a261` was submitted for an independent review. Subsequent writer changes made on this same **unmerged draft branch**:

- `72f03633c144671b9a0d172e211ad8a6373934e5`: separate the false old Lemma 24.1 from the valid statement renamed **Proposition 24.2**, restore the admissible time-reversal and global-phase remarks and scoped structural observations, remove revision-history / process voice from the paper, and replace the *direct* semigroup-transfer premises in Substratum's Theorem 23, Lemma 23.0, and synthesis with the **open** generator-exhaustiveness premise.
- `c0d70d5832aff0c4a5faf933d27f710796737e5f`: initially marked the frozen research families `current` in the Lean-manuscript census. That change was **reverted** at `cdd95c8b4365bcf1fd609955b6b9ba09f62a570a` after CI showed the `R7-WTS` guard requires their `kernel-only` classification. The original registry blob `89a44bbc1fff815d624fd5c4d272c9b60c856199` is restored; existing Lean identifiers are cited in the manuscript without renaming the frozen research family.

Writer's read-only structural checks on the new sources (not a release-gate substitute):
- No scientific-manuscript occurrence of the retired label `Lemma 24.1`; `Proposition 24.2` appears with separate citations for both Lean directions.
- Each of `WT2gen_oneSided`, `WT3_spanning_iff`, `blockSpanning_of_wordTracesEqual`, `trace_wordEval_hiddenConjugate`, `ST3_pairC`, `ST4_pairC`, and `pairC_wordTraces` is present in the corresponding committed Lean source.
- The proof declarations cited by Proposition 24.2 and by the counterexample are present in the unchanged Lean modules. Their historical research census disposition remains `kernel-only`; the new canonical manuscript statement is tracked separately in the coverage ledger. No independent verdict, successful full release-gate run, generated TeX/PDF or exact-head CI verification is claimed.

**Outstanding reviewer tasks:** compare the manuscript statement to the exact Lean quantifiers and proof direction; check whether Theorem 24(i)'s very broad state-relabeling language needs separate narrowing; validate the old auxiliary Step 3 and retained time-reversal claim at their exact scopes; verify the direct internal dependencies and corpus mirrors; regenerate `.tex` and PDF; run the manuscript census, coverage, release gate and Lean axiom checks on the final head; and independently review the resulting exact commit. The roughly 15 false and 35 stale external sites remain a separate propagation phase. This unit is not merge-ready.

## Latest writer corrections and CI diagnosis

- `652343d2f76ebdef1d221c454d7ff1d87f5092f1`: reformulated the open generator-exhaustiveness question without hitting the architecture guard's forbidden unqualified phrase. The old theorem statement is still not a proven full-gauge soundness result; SC-45 #979 / PR #981 is its separate source-correction unit.
- `f0c9ba4c402b02ef757e0ef50cd3d0e5e3b3ce76`: corrected coverage ledger fingerprints for Theorem 23, Lemma 23.0 and Theorem 24; retired the untrue canonical `SUBSTRATUM:L-24.1` entry and inserted `SUBSTRATUM:P-24.2` as K3, citing both kernel directions. Exact-head review of this ledger change is still required.
- Initial verify run 40640986014 on `83b00491` found failure in (a) the staleness check because source Markdown changed but TeX/PDF were not rebuilt; (b) architecture check due to unqualified 'families exhaust' phrase; (c) coverage check because the renamed/changed canonical statements were not updated; (d) `R7-WTS` guard because the frozen research family was changed from `kernel-only` to `current`. Items (b)–(d) have source corrections on later heads, pending fresh CI. **Staleness remains unresolved**; the canonical `./build.sh Substratum` must be run on the current branch and the generated `papers/Substratum.tex` and `papers/Substratum.pdf` committed before the release gate can pass. Do not hand-edit the TeX hash stamp or claim the PDF is current.
- Recheck current SC-44 exact head, not the original `83b00491` run. The existence of pre-existing kernel certificates does not substitute for a completed check on the new combined tree.
