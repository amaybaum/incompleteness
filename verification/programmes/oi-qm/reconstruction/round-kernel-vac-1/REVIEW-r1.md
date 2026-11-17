# KERNEL-VAC-1 — independent execution review r1

**Verdict: ACCEPT WITH SCOPE LIMITS for the source, dependency and preservation review of the exact scientific head below. No blocking finding. Final-head ordinary CI remains pending at this review's observation; this is not a completed REPAIRED disposition, an E designation, an attestation, a receipt or merge authority.**

Reviewer: worker C, independent non-author. Writer: worker A. Review date: 2026-11-17; final CI observation approximately 15:26 UTC. The reviewer neither supplied candidate proof code nor edited the execution branch or scientific files, and ran no Lean, numerical experiment or new investigation.

## Identity and authority

- Goal: [#1188](https://github.com/amaybaum/incompleteness/issues/1188); guiding draft [#1359](https://github.com/amaybaum/incompleteness/pull/1359).
- Reviewed scientific head H: `51114a5ef99dec889e842083b17f61efdbd9b9dd`; tree `166dcfc219274f10ce988c8544b9be1671266441`.
- Frozen F: `0c706277ae7f65ca9c09b91978839003640b07d1`; D: `d4d0a07091926641dd3ee844807f41dae8a51d89`.
- Directly checked single-parent chain: F → `c478b77386fffa6e1eebb93a2d2c6091d26d9139` → `be9c84422eefe85e4d086c5cceb261719948563f` → H. These are the three substantive checkpoints; the budget is exhausted, with no implicit extension.
- The frozen `round-kernel-vac-1/preregistration.md` was read and remains blob `ca98ba0ab4bdaff1dd04e107f62c63fed92ec49a`. Its historical draft/queue prose is not a new authorization state. Current rules were read; `AGENTS.md` remains blob `3c1788a3926455cf540aa25c344bbff0b1e7f7c5`.
- The [execution-approval record](https://github.com/amaybaum/incompleteness/pull/1359#issuecomment-6951772438) was inspected. It relays the owner's approval of the bounded handoff, SHA256 `43a9ae55263d9abd92e84345aca8a3107db45c483d49d151a20a5081d5c6c6d6`; it is not an independently owner-authored GitHub comment or coordinator self-authorization. The separate [F designation record](https://github.com/amaybaum/incompleteness/pull/1359#issuecomment-6951338117) and reported formal F run are distinguished from this execution review.

## Statement and dependency findings

**Checkpoint 1 — original-predicate defect: PASS, including compiler/axiom readback.** The theorem is the required `∀ T : FiniteOperationalTheory (Fin 2), ¬ ReadWriteSourced T`. The proof derives actual level-one identity-channel availability using the theory's readout availability, local-Lüders identity and coarse-graining fields. It does not substitute admissibility, an unrelated system-level identity field or an assumed available map for that obligation. `Complex.I • 1` represents this same channel, while its diagonal imaginary part excludes equality to every exact permutation matrix. The contradiction is on the concrete nonempty `Fin 2 × Fin 1` carrier; it is not an empty-carrier contradiction.

The unchanged source predicate quantifies over every representative of an available conjugation. This is exactly the defect tested. The existing phase-invariance lemma's actual hypothesis and its import path through the existing bridge modules were inspected. The original predicate and its implication proofs are preserved, with their evidential authority withdrawn rather than a new meaning assigned to their identifiers.

**Checkpoint 2 — sole witness: PASS, including compiler/axiom readback.** The statement is exactly `SubstratumInterface.MonomialSource (SubstratumInterfaceAudit.permTheory (Fin 2))`. It quantifies over all natural-number levels, including zero, and all matrix representatives `V` of an actually available conjugation. There is no added isometry, normalization, rank, chosen-representative or `Nonempty` restriction.

I independently inspected the existing `permTheory = genTheory permClass permClass_arch` definition, the generated theory fields, `Realized`, and `realized_of_instAvail`. The last lemma closes actual `InstAvail` using the existing architecture, including its readout, coarse-graining, feed-forward and discard cases. The witness reuses these obligations rather than postulating them. Every realized Kraus matrix satisfies the existing class's row and column sparsity. Matrix-unit evaluation transfers the vanishing cross-products to the arbitrary representative `V`, giving both sparsity directions. The existing finite extension lemma `submonomial_monomial` has no `Nonempty` requirement and covers the empty level as well. Zero and rank-deficient representatives are included conditionally on realization; this does not assert their physical availability.

The added lemmas are tied to those two obligations. There is no new source predicate, theory, target axiom, duplicate no-go theorem or physical premise. The checkpoint-1 control body is byte-identical within the completed module. The module's final blob, `6b0d61109ebb1a6fcf614927f0963624e1a7b175`, is identical at checkpoint 2 and H.

**Checkpoint 3 — scope and citations: PASS as the bounded closeout.** The surviving statement is conditional: if a theory's available composite conjugations are monomial, it has no composite unitary control **on `Fin 2`**, since such control would make the non-monomial `rot` available. The unchanged QM corollary concerns that same theory under that same hypothesis. The sole witness establishes a mathematical instance, not a native physical producer or a universal obstruction to read/write interaction, and not a uniquely necessary empirical addition.

- `ReadWriteControl.lean` now distinguishes the vacuous antecedent from the surviving implication. Its description no longer attributes an unassumed continuity property to `ReadWriteFamily`.
- `RouteB.lean` and the route-B audit point to the actual specified implementation-class and generated-`Fin 2` results. Those independent proofs are unchanged.
- The source and completion-assumption audits withdraw the old implication's substantive evidential role and retain the stated class/theory hypotheses. The available-to-monomial implication is not reversed into availability of every monomial matrix.
- F73's explanation and the edge-probe comments state the limited evidential role of declaration checks. They do not claim that detecting old names validates the new proof. Existing passing conditions remain intact.
- The root import was added with the new module at checkpoint 1. Census updates accompany the module and witness commits; the new family remains kernel-only, with no new manuscript anchor or promotion. The old family's note does not misidentify an unchanged predicate with a different statement.
- `RESULT.md` accurately presents a candidate awaiting exact-head CI/review and preserves the distinction between refuted, unproved and unfinished outcomes. Checkpoint-2 CI being pending at that record's preparation is a historical statement; the later independent readback appears below.

**Known residual, outside this frozen correction:** F72's older explanation overstates the monomial-source conditional as a statement about finite bijective dynamics alone and omits the explicit `Fin 2` scope. Its bytes remain unchanged, and `RESULT.md` explicitly records it for a separate scope decision. This review does not endorse that wording or certify all related publication prose. Leaving this identified out-of-scope residual does not authorize another scientific checkpoint.

## Independent preservation and scope checks

I compared committed F and H content directly, independently of the writer's preservation snapshot:

1. Non-comment Lean bytes are identical in `ReadWriteControl.lean` and `RouteB.lean`; original declarations, proof terms, theory definitions and controls are preserved.
2. The entire Python AST of `edge_rigidity_probe.py` is identical. The entire AST of `bohr_frequency_probe.py` is identical after masking only the single F73 explanatory argument. Samples, predicates, declaration-presence tests and executable R7-SUB/R7-SRCP boundaries remain unchanged. The full F72 check-call source bytes are identical.
3. F-to-H changes comprise exactly the ten allowed execution paths, with the prescribed add/modify kinds, plus three new round records: `checkpoint-1.md`, `checkpoint-2.md` and `RESULT.md`. Checkpoint 3 itself changes nine files. There are no deletions or unlisted paths.
4. The frozen preregistration is byte-identical. No workflow, manuscript, book, historical review, legacy/native record, receipt or other control-plane file is changed. The three execution commits have the stated single-parent chain, without incoming-main integration.
5. The complete new module has eight theorem declarations and corresponding axiom reports. The first five control proofs are preserved when the three witness lemmas are added. `git diff --check F H` passes.
6. A direct exact-identifier search of the available committed Markdown manuscripts under `papers/` and `book/` found no occurrence of `ReadWriteSourced` or the three `readWriteSourced_*` implication names. This is not a paraphrase census or a review of PDF content. A broader search encountered unavailable binary objects in this partial checkout, so I do not independently certify a binary/all-format absence claim. The changed support chains and identified historical roles were inspected; no off-main B/C research result was imported as support.

The ten execution paths are the new `ReadWriteNonvacuity.lean`, root `OIBridge.lean`, `ReadWriteControl.lean`, `RouteB.lean`, `lean-manuscript-census.json`, `bohr_frequency_probe.py`, `edge_rigidity_probe.py`, `completion-assumption-audit.md`, `route-b-audit.md` and `source-audit.md`, at their exact preregistered repository paths.

## Independent CI evidence and limits

Counts below are **workflow-job objects**, not counts of check-runs. All three ordinary runs use the `pull_request` event and attempt 1; none is an E attestation.

| Scientific head | Independently observed evidence | Limit |
|---|---|---|
| Checkpoint 1 `c478b77386fffa6e1eebb93a2d2c6091d26d9139` | [Run 44110577759](https://github.com/amaybaum/incompleteness/actions/runs/44110577759) completed success: 27 jobs, 26 success and the expected A42 exclusion skip. [Mathlib job 134134724953](https://github.com/amaybaum/incompleteness/actions/runs/44110577759/job/134134724953) Build, Release gate and all later required steps succeeded. Full job log shows the new module built and five reports using only the standard three axioms. | Establishes the control at this head. |
| Checkpoint 2 `be9c84422eefe85e4d086c5cceb261719948563f` | [Run 44111955933](https://github.com/amaybaum/incompleteness/actions/runs/44111955933) completed success: 27 jobs, 26 success and the expected A42 exclusion skip. [Mathlib job 134139665158](https://github.com/amaybaum/incompleteness/actions/runs/44111955933/job/134139665158) Build, Release gate and later required steps succeeded. The complete log includes the built module and all eight standard-axiom reports. | Establishes the completed module at this head. Its identical blob at H is a source-identity fact, not transfer of the whole CI verdict. |
| H `51114a5ef99dec889e842083b17f61efdbd9b9dd` | [Run 44113022884](https://github.com/amaybaum/incompleteness/actions/runs/44113022884) remains in progress with null conclusion. [Mathlib job 134143451997](https://github.com/amaybaum/incompleteness/actions/runs/44113022884/job/134143451997) has Build in progress, Release gate and later steps pending at the final read. | **No final-head compiler, Release-gate or complete CI success is claimed by this artifact.** |

The expected Mathlib step for marking an out-of-policy KTRANS axiom report was skipped on the completed checkpoint jobs, with the required axiom gate succeeding. The independently read reports are:

`localLuders_one_eq_id`, `levelOne_id_available`, `quarterPhase_conjChannel`, `quarterPhase_not_perm`, `readWriteSourced_fin2_impossible`, `conjChannel_single_entry`, `monomial_of_realized_permClass`, `permTheory_fin2_monomialSource`.

Each report contains exactly `[propext, Classical.choice, Quot.sound]`; the first five occur at checkpoint 1 and all eight at checkpoint 2. Reports were read from the complete logs, including multiline output, not inferred from a green badge. Minor unused-variable/simp-argument lint warnings do not change those conclusions.

The F formal-run report (run 44099752053, 41 successful jobs) is carried forward from the authorization/coordinator evidence; I did not independently reread that run's entire validation in this execution review. Writer-local artifact/census/V3 check claims, including its stated V3 conformance timeout, are not represented here as reviewer-executed checks. Full-history validation is a CI responsibility in this partial local checkout. This review checks the bounded changed proof/dependency and citation chains; it is not a new audit of every unchanged imported theorem.

## Disposition and retention boundary

The exact scientific head passes this independent source/dependency/preservation review. The required remaining observation is successful ordinary CI on the final head, separately recorded with its exact identity; a later review-retention child likewise requires its own ordinary CI. Any failure must be assessed on its actual evidence rather than inferred away from an earlier green run.

No fourth substantive checkpoint, second witness, expanded producer search, premise adoption or E action is approved here. If the frozen STOP/withdrawal conditions are reached, the prescribed S12 handling applies: the withdrawal child restores execution paths to F while preserving the required round/result records; it does not turn a failed or unfinished candidate into E. This review does not implement withdrawal, authorize reconciliation, designate E, issue a native receipt or authorize merge.

I preapprove **byte-for-byte retention of this artifact only** as `verification/programmes/oi-qm/reconstruction/round-kernel-vac-1/REVIEW-r1.md` in a record-only child of H. That child must name H as the reviewed scientific head and must not change any scientific/source byte or frozen record. No status substitution or other file edit is preapproved by this artifact. Retaining the review is not another substantive scientific checkpoint, does not enlarge this verdict, and does not transfer previous-head CI. Its exact delta and subsequent CI can be verified separately.
