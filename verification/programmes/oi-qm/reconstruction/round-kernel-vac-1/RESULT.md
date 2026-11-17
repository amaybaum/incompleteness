# KERNEL-VAC-1 — checkpoint 3: repair-or-retire execution disposition

**Status: REPAIRED candidate; final exact-head CI and independent non-author
review pending.** This is an execution result record, not E designation, an
attestation, a native receipt or merge authority. The original source predicate
is not repaired: its evidential use on `Fin 2` is retired, and the existing
monomial-source implications receive the sole preregistered mathematical witness.

## Authority, pins and budget

- Goal: [correctness issue #1188](https://github.com/amaybaum/incompleteness/issues/1188);
  guiding draft [PR #1359](https://github.com/amaybaum/incompleteness/pull/1359).
- D: `d4d0a07091926641dd3ee844807f41dae8a51d89`.
- F: `0c706277ae7f65ca9c09b91978839003640b07d1`;
  [owner designation](https://github.com/amaybaum/incompleteness/pull/1359#issuecomment-6951338117).
  Formal F run [44099752053](https://github.com/amaybaum/incompleteness/actions/runs/44099752053),
  `workflow_dispatch`, attempt 1, passed all 41 jobs at exact F.
- [Execution authorization](https://github.com/amaybaum/incompleteness/pull/1359#issuecomment-6951772438)
  approves the handoff SHA256
  `43a9ae55263d9abd92e84345aca8a3107db45c483d49d151a20a5081d5c6c6d6`.
- Published branch: `round/kernel-vac-1-1188-20261117`; A is the sole scientific
  writer, using its owned isolated worktree. Commits are single-parent children
  of F; no incoming main, control-plane edit or history rewriting occurred.
- The [preregistration](preregistration.md) remains byte-identical, Git blob
  `ca98ba0ab4bdaff1dd04e107f62c63fed92ec49a`; its old draft/queue prose is historical.
- **Three of three substantive checkpoints consumed**: control, sole witness,
  citation/registry closeout. Only diagnostics of these same obligations remain
  in scope. There is no automatic extension or second candidate.

## Exact scientific targets and dependency path

| Checkpoint | Exact target/disposition | Evidence and remaining gate |
|---|---|---|
| 1 — compulsory control | `∀ T : FiniteOperationalTheory (Fin 2), ¬ ReadWriteSourced T` | `ReadWriteNonvacuity.readWriteSourced_fin2_impossible` at `c478b77386fffa6e1eebb93a2d2c6091d26d9139`; ordinary run [44110577759](https://github.com/amaybaum/incompleteness/actions/runs/44110577759) passed; non-author source and compiler/axiom inspection found no blocker. |
| 2 — sole witness | `SubstratumInterface.MonomialSource (SubstratumInterfaceAudit.permTheory (Fin 2))` | `ReadWriteNonvacuity.permTheory_fin2_monomialSource` at `be9c84422eefe85e4d086c5cceb261719948563f`; non-author source/dependency inspection found no blocker; ordinary run [44111955933](https://github.com/amaybaum/incompleteness/actions/runs/44111955933) and its axiom reports are pending at this record's preparation. |
| 3 — closeout | Withdraw old antecedent as substantive evidence; preserve declarations/proofs; repoint only to actual conditional or specified class/theory support | The ten permitted execution paths below and this result; independent review and ordinary CI of the complete published closeout remain pending. |

The [control record](checkpoint-1.md) derives the level-one identity channel's
availability from `readout_avail`, `readout_is_localLuders` and
`availExt_coarse`. `Complex.I • 1` is a representative of that same channel,
but has a diagonal imaginary part impossible for any exact permutation matrix.
The contradiction uses the concrete nonempty `Fin 2 × Fin 1` carrier; it does
not infer an empty-carrier contradiction or assume availability from
admissibility. The original `ReadWriteSourced` is unchanged.

The [witness record](checkpoint-2.md) reuses the unchanged
`permTheory = genTheory permClass permClass_arch`. The existing `genTheory`
supplies the theory's identity, coarse-graining, feed-forward, preparation,
readout and discard fields. `realized_of_instAvail permClass_arch` yields the
finite Kraus representation of the actual available branch. Matrix-unit
evaluation transfers vanishing row/column products of every class member to
**every** representative `V` of the same conjugation. The existing
`submonomial_monomial` then gives `IsMonomial V`.

The exact witness quantifies over **all `n`, including `n = 0`, and all matrix
representatives**. It imposes no isometry, full-rank, normalized-matrix or
`Nonempty` premise. The intermediate sparsity proof also includes zero and
rank-deficient matrices; at the empty carrier its quantified obligations are
empty and the existing finite extension theorem still applies. No replacement
predicate, second theory, duplicate no-go theorem or physical premise is added.

The surviving implication retains the mandatory scope:

> A theory whose available composite conjugations are all monomial has no
> composite unitary control on `Fin 2`, because control would make the
> non-monomial `rot` available.

This is the unchanged `monomialSource_not_control`. The unchanged
`monomialSource_not_qm` excludes `ExactAllFiniteEndomorphicQuantumOps` for that
same theory under that same hypothesis. The witness is one mathematical
instance. It does not derive a native physical source, identify every native
observer interface with this theory, make every monomial matrix available,
or prove that read/write interaction in general cannot supply QM.

## File and citation disposition

Paths below are repository-relative. `A/M` is the F-to-execution change type.

| A/M | Permitted path | Disposition |
|---|---|---|
| A | `verification/lean-mathlib/OIBridge/ReadWriteNonvacuity.lean` | Compulsory control, sole witness, only their proof lemmas and eight axiom reports. |
| M | `verification/lean-mathlib/OIBridge.lean` | Same-commit root import at checkpoint 1. |
| M | `verification/lean-manuscript-census.json` | Same-commit new module family/target updates; old source-family note withdraws the old antecedent's authority. Kernel-only disposition, no new manuscript anchor or promotion. |
| M | `verification/lean-mathlib/OIBridge/ReadWriteControl.lean` | Description/doc-comment corrections only. All declarations and proof terms, memory-swap and interpolation controls retained. |
| M | `verification/lean-mathlib/OIBridge/RouteB.lean` | Opening description only; support is the specified `substratumClass_not_drivesElementary` and generated `Fin 2` theory's `substratumGen_not_control`. Route B proofs unchanged. |
| M | `verification/programmes/substratum/source-audit.md` | Conditional Fin 2 statement, original-predicate retirement, sole mathematical witness, actual class/theory scope. Removes the unsupported general physical and unique-empirical-addition inference. |
| M | `verification/programmes/substratum/route-b-audit.md` | Corrected immediate citation/scope to the specified implementation class and generated `Fin 2` theory. |
| M | `verification/audits/operational/completion-assumption-audit.md` | Retains the independently proved implementation-class result; removes old source implication as substantive support. |
| M | `verification/lean/bohr_frequency_probe.py` | F73 comments and explanation only. Samples, declaration-presence checks and every passing condition retained. F72 is separately recorded below. |
| M | `verification/lean/edge_rigidity_probe.py` | Round-63 explanatory comments only. All executable conditions, including R7-SUB and R7-SRCP, retained. |

The round adds `checkpoint-1.md`, `checkpoint-2.md` and this result as permitted
non-control-plane records. Independent review may be retained as a separate
record. No manuscript, book, generated artifact, workflow, existing historical
review, legacy record, receipt or other native record is edited.

Identifier searches for `ReadWriteSourced` and the three `readWriteSourced_*`
implications found no occurrences in `papers/` or `book/`. This is an exact
identifier finding, not a whole-corpus absence claim about paraphrases.
Remaining verification occurrences have these roles:

- The original module: retained definitions, implications and axiom commands,
  with their evidential limitation explicit. New module: the compulsory defect.
- The three mutable audit notes and Route B description: explicit retirement
  or exact replacement support, rather than substantive use of the antecedent.
- The two probes: compatibility/declaration checks and corrected F73 explanation;
  they do not validate the new proof merely by finding old declaration names.
- `intro-corpus-audit-20261026/unit5-evidence/REVIEW.md` and
  `introduction-repro-ext/results-121598983127-28.json`: preserved historical
  review/compilation evidence, which never proves antecedent satisfiability.
- Quarter-phase-native, quarter-phase-feedback, MINACC and the TUNE-1 step-one
  records: preserved cautions or earlier paper-only defect arguments. The
  frozen preregistration and checkpoint records remain historical evidence.
- Census: explicit scope/disposition, with no manuscript supersession mapping
  falsely identifying the old predicate with a different theorem statement.

Support is in the existing F/D kernel files or in the two reachable execution
commits named above. The unchanged contracts are `OperationalAssembly`,
`ImplementationLocality` (`InterventionLocality` namespace),
`SubstratumInterface`, `SubstratumInterfaceAudit` and `StructuralClosure`.
No off-main support is silently imported from B or C's research branches.

## Preservation and verification

Local static comparisons against F found byte-identical non-comment content
in `ReadWriteControl.lean` and `RouteB.lean`. The full parsed Python AST of
`edge_rigidity_probe.py` is identical. The full parsed Python AST of
`bohr_frequency_probe.py` is identical after replacing only F73's explanation
argument with a common marker; thus its samples and predicates are unchanged.
The entire F72 explanation remains byte-identical. Frozen preregistration hash,
path scope, whitespace, census and artifact-placement checks passed.

V3 self-test passed locally. The local V3 conformance run reached its explicit
30-second bound, so no local corpus verdict is claimed. Full-history legacy
and V3 validation remains the ordinary CI Release gate's responsibility;
the shallow local checkout cannot certify those histories. No local Lean or
Mathlib build, numerical experiment, new workflow, special dispatch or rerun
was performed. Automatic ordinary PR CI is not an F/E attestation.

Checkpoint 1's Mathlib Build/Release and all subsequent required steps passed;
its five new reports use only `[propext, Classical.choice, Quot.sound]`.
The full module requests reports for `localLuders_one_eq_id`,
`levelOne_id_available`, `quarterPhase_conjChannel`, `quarterPhase_not_perm`,
`readWriteSourced_fin2_impossible`, `conjChannel_single_entry`,
`monomial_of_realized_permClass` and `permTheory_fin2_monomialSource`.
Checkpoint 2 and final closeout compiler/axiom/CI outcomes must be read from
structured host jobs/steps and complete logs, not inferred from this record.
Writer checks and successful builds do not substitute for non-author review.

## Residuals, review and next boundary

**Separate residual:** the earlier F72 explanation in
`bohr_frequency_probe.py` broadens the independent monomial-source conditional
to “finite bijective dynamics alone” without its explicit `Fin 2` carrier.
The frozen inventory identifies F73, so F72 remains unchanged and is recorded
for a separate scope decision. This round does not certify the wording of
that older explanation or claim all related publication prose is resolved.

Non-author worker C's control and witness source inspections found no blocker;
the complete checkpoint-3 head still requires its own review of declarations,
dependencies, all-representative/zero-dimensional scope, citation mapping and
preservation. The exact scientific head and any later review-only retention
child must be named separately. That review must precede any owner E decision.

If the named witness is not established within this cap after the control
passes, use **RETIRED AS EVIDENCE** and distinguish refuted, unproved or
unfinished; do not infer that every repair is impossible. Failure of control,
scope, preservation, verification or review invokes **STOPPED** and the frozen
S12 withdrawal requirements, not a fabricated E. There is no authorization
for E attestation dispatch/designation, incoming-main reconciliation,
post-E integration, native receipt generation or merge. Those later decisions
remain outside this execution approval.
