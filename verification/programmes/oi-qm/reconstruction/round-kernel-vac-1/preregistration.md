# KERNEL-VAC-1 — read/write-source repair or retirement

**DRAFT / NOT FROZEN / NOT EXECUTED.** Accountable Issue: #1188. Writer:
Codex. Designated independent reviewer: Claude; the initial review is ACCEPT
WITH CHANGES and this revision awaits its focused delta check. Drafting
snapshot `D`: `d4d0a07091926641dd3ee844807f41dae8a51d89`. This document is
the proposed control plane, not a kernel result or an owner designation.

## Authority and goal

The owner's direct task message of 2026-11-17 states:

> I recommend Codex writes and Claude independently reviews each new unit.
> Start #1188 first, prepare #1055 as the next bounded assignment, and retain
> #1358's existing authorization without duplicating it. Separate writers or
> independent sessions would be needed for genuine parallel scientific work.

Codex relayed this instruction at #1188 comment 6946076300. The direct-message
time of day is not available. The start instruction is applied only to
reversible pre-F drafting and ordinary draft-PR checks. It is not approval of
this proposed execution design. F designation and execution require the
owner's own recorded decisions; the relayed start instruction does not cover
them. Freeze, kernel execution, workflow dispatch, E designation and merge
remain separately gated. No execution artifact is changed by this drafting
checkpoint.

**Goal link (§A.47):** #1188 serves #1169 by deciding whether the invalid
read/write-source evidence can be replaced by a witnessed, conditional
monomial-source no-go, or must be withdrawn without that replacement. Known
unsupported evidence is corrected before further claims rely on it. Either
outcome is useful; neither supplies a physical apparatus, derives a Born rule,
or establishes OI–QM equivalence. The physical-source gate remains NOT PASSED.
#1055 is the proposed next assignment and #1358 remains queued separately.

## V3 declaration

```v3-round
round KERNEL-VAC-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-kernel-vac-1/
```

```v3-governed-paths
execution M verification/audits/operational/completion-assumption-audit.md
execution M verification/lean/bohr_frequency_probe.py
execution M verification/lean/edge_rigidity_probe.py
execution M verification/lean-manuscript-census.json
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-mathlib/OIBridge/ReadWriteControl.lean
execution A verification/lean-mathlib/OIBridge/ReadWriteNonvacuity.lean
execution M verification/lean-mathlib/OIBridge/RouteB.lean
execution M verification/programmes/substratum/route-b-audit.md
execution M verification/programmes/substratum/source-audit.md
record AM verification/programmes/oi-qm/reconstruction/round-kernel-vac-1/
record A verification/receipts/KERNEL-VAC-1.json
```

These are proposed permissions for a future F, not present execution
authorization. Before F, only this preregistration and its `amendments/` may
change, through single-parent commits from D. No incoming main merge is
permitted before E. No manuscript, generated publication, workflow, existing
receipt, seal, legacy manifest, or historical review is in the execution set.

## Source inventory and evidential boundary

All file references in this section refer to D on main. The Issue and PR
numbers record provenance and responsibility; the following source bodies
support the description. The scan used `ReadWriteSourced` and
`readWriteSourced_(monomialSource|not_control|not_qm)` across the tree, followed
by source-context reading and inspection of the related no-go statements.

| Source | What it supplies | Disposition proposed for execution |
|---|---|---|
| `verification/lean-mathlib/OIBridge/ReadWriteControl.lean`, Outcome | The predicate quantifies over every matrix representative of an available conjugation and demands exact equality with a permutation matrix. The two no-go corollaries use `Fin 2`. | Preserve the old declarations and proof terms; correct their description and mark their evidential limitation. Put only the defect control and the existing-predicate non-vacuity witness, with necessary proof lemmas, in the new module. |
| `verification/lean-mathlib/OIBridge/OperationalAssembly.lean`, `FiniteOperationalTheory` | The actual availability, composition and preparation fields that a proposed witness must satisfy. | Read-only. Do not weaken the theory structure to make a witness fit. |
| `verification/programmes/oi-qm/reconstruction/drafts/tune-1-20261111/TUNE-1-STEP1.md`, B.2 | Existing paper argument: the identity channel admits a non-permutation global-phase representative, defeating the predicate on a nonempty carrier. It explicitly lacks kernel formalization. | Preserve unchanged; use as the source of the proposed kernel control, not as an already checked kernel result. |
| `verification/lean-mathlib/OIBridge/SubstratumInterface.lean`, `IsMonomial`, `MonomialSource` and its two no-go lemmas | The existing predicate admits arbitrary complex diagonal weights rather than exact equality to a permutation. `monomialSource_not_control` and `monomialSource_not_qm` already prove the conditional `Fin 2` conclusions. | Reuse the predicate and theorems unchanged; establish their non-vacuity with the named witness below. No scalar-permutation successor is needed. |
| `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean`, `permClass`, `permTheory`, `permTheory_avail_conj` and `permTheory_sourcedOI` | `permTheory A` is the existing `genTheory permClass permClass_arch A`; its theory structure and specified operations already have kernel definitions/proofs. Its existing no-control result does not itself prove `MonomialSource`. | The sole witness candidate is `permTheory (Fin 2)`. Reuse its structure; prove the missing `MonomialSource` property without changing its operations. No physical availability or native producer is inferred. |
| `verification/lean-mathlib/OIBridge/StructuralClosure.lean`, Residual | `substratumGen_not_control`, `substratumGen_not_qm` concern the specified generated theory on `Fin 2`; `substratumClass_not_drivesElementary` concerns the specified implementation class. | Existing scoped replacement support; no stronger carrier, source or physical conclusion. |
| `verification/programmes/substratum/source-audit.md`, read/write row and third entry | Still uses the disputed family to support a broad no-go and empirical-addition wording. | Replace the affected inference with the exact supported class/interface result; do not infer universal impossibility or a uniquely necessary new physical law. |
| `verification/programmes/substratum/route-b-audit.md`, The question | Still cites the disputed family. Its separate Route B proof is not invalidated merely by that citation. | Repair the citation and its immediate scope; preserve the independently supported Route B result. |
| `verification/audits/operational/completion-assumption-audit.md`, What remains open, item 2 | Still pairs the disputed result with `substratumClass_not_drivesElementary`. | Keep the latter's exact class scope and remove the former as substantive support. |
| `verification/lean-mathlib/OIBridge/RouteB.lean`, opening description | Residual disputed citation, not a use of that theorem in the target proof. | Description-only correction. |
| `verification/lean/bohr_frequency_probe.py`, F73; `verification/lean/edge_rigidity_probe.py`, round-63 guards | Existing numeric controls and declaration-presence checks name the old family. | Retain the controls and declarations; qualify misleading explanatory text and, if needed, add checks for the correction. Do not weaken a passing condition. |
| `verification/audits/manuscript/intro-corpus-audit-20261026/` retained reports and reviews | Historical axiom/compilation evidence names the old implications. Compilation does not establish satisfiability of their antecedent. | Preserve actual bytes and review verdicts; explain the distinction in this round's result. |
| Quarter-phase, MINACC and TUNE records | Already warn about, or explicitly avoid using, the disputed family. | Preserve; a search hit is not automatically a correction target. |

The earlier reader-facing correction is already on main through #1242, merge
`7d6e593448d3cb1db90dba05275d326732586d38`. Reopening that completed diff is
not part of this round. The current exact-identifier scan found no residual
hit in `papers/` or `book/`; this is not a claim that every paraphrase has
already been independently audited. Before F, review the final citation map
against the maintained corpus. If another substantive publication defect is
found, stop scope expansion and record its separate disposition; do not edit
an undeclared manuscript or silently add its PDF to the execution set.

The proposed execution files are neither entries in D's 303-entry legacy
manifest nor beneath its closed namespaces. They are outside the 54 native
record directories identified by the existing receipts' control-plane paths.
Those membership checks do not certify receipt history. Full-history legacy
and V3 checks remain release-gate obligations; the local partial/shallow store
cannot certify them. No historical record, receipt or manifest is proposed
for modification.

## Ordered execution design — only after F and execution authorization

### 1. Kernel control before repair

Formalize the recorded phase-representative contradiction first, with the
minimal compulsory target
`∀ T : FiniteOperationalTheory (Fin 2), ¬ ReadWriteSourced T`.
State the level-one availability derivation from the actual theory fields;
do not assume availability merely from matrix admissibility. Exhibit the
identity channel's phase-equivalent representative and check its failure to
be a permutation. Use the original predicate unchanged.

The generic source declaration has no `Nonempty A` assumption. A generalized
control must state it explicitly; an empty carrier and the `n = 0` extension
must not be silently treated as the nonempty case. The compulsory `Fin 2`
control is enough to assess the existing two no-go corollaries. Failure to
formalize this control is a STOP, not a passed defect certificate.

### 2. Witness the existing `MonomialSource`; introduce no new predicate

The sole non-vacuity target is
`SubstratumInterface.MonomialSource (SubstratumInterfaceAudit.permTheory (Fin 2))`.
`IsMonomial` already permits arbitrary complex diagonal weights, so the
identity's global phase does not present the exact-permutation defect. The
existing `MonomialSource` definition and both no-go theorems are retained
unchanged. No scalar-permutation predicate, new theory or duplicate no-go
corollary is proposed. Retain `ReadWriteSourced` unchanged as well, so the
defect control continues to name the original predicate.

The required obligations are:

1. Prove the named `MonomialSource` target in the kernel, for every extension
   level `n` and every matrix representative quantified over by the existing
   definition, including `n = 0`. Do not weaken the target to available
   isometries or selected representatives. A `ReadWriteFamily` witness or the
   already-proved absence of control is not a proof of this target.
2. Reuse `permTheory (Fin 2)` as the concrete `FiniteOperationalTheory`.
   Trace its existing availability, coarse-graining, composition and
   preparation obligations through `genTheory` and `permClass_arch`; no new
   derivation of already-proved structure fields is required. Do not assume
   `MonomialSource`, drop identity availability, change the theory's fields or
   operations, or use the old vacuous antecedent to obtain the witness. This
   is a mathematical theory witness, not a physically realized native source.
3. Repoint the affected conditional claims to the existing
   `monomialSource_not_control` and `monomialSource_not_qm`, with the new
   witness establishing that their hypothesis is inhabited on `Fin 2`.
   Reuse their proofs and preserve their exact scope as specified below.

`ReadWriteNonvacuity.lean` will hold the defect control and the witness, with
only the proof lemmas needed for those two targets. The intended new-file
name replaces the earlier plan's `ReadWriteSourceRepair.lean`; no existing
file is renamed. The proof statements, dependencies and witness need
independent review; a successful build alone is insufficient. If this named
witness is not established, take the retirement branch below. No second
witness, replacement predicate or physical-source candidate is included.

### 3. Repair or retire authority

**REPAIRED:** the defect control and all three obligations above pass. This
repairs the evidence chain by retiring the old antecedent as substantive
support and reusing the witnessed `MonomialSource` implications; it does not
repair or rename `ReadWriteSourced` itself. No native OI apparatus is thereby
shown to realize `permTheory`.

**RETIRED AS EVIDENCE:** the defect control passes, but the named witness is not
established within the bound below. Retain the old implication declarations
for historical and guard compatibility; withdraw their use as substantive
evidence in the mutable dependents. Existing `MonomialSource` implications
remain conditional, without a claim that this unit established their
non-vacuity. Use independently supported results for the specified generated
theory or implementation class only at their proved scope. Record whether
the witness target is refuted, unproved or merely unfinished. A budget stop
does not show that `MonomialSource` is empty or that a repair is impossible.

**STOPPED:** the defect control, permitted-path boundary, preservation,
verification or review requirements cannot be met. Follow V3 S12 if already
frozen; do not manufacture E or label an incomplete repair successful.

Retirement here means retirement of evidential authority only. It does not
remove declaration reachability, historical review evidence or physical files.
No deletion, renaming, mechanical code stripping or change to existing proof
terms is planned. If such a transformation becomes necessary, stop before it:
§A.39's exact edit ledger, independent preservation checker and pre-freeze
execution-tree evidence would need separate preparation and authorization.

**Mandatory closeout scope (R2):** every corrected use of the surviving
monomial-source no-go must say what its theorem proves:

> A theory whose available composite conjugations are all monomial has no
> composite unitary control on `Fin 2`, because control would make the
> non-monomial `rot` available.

Its existing QM corollary excludes `ExactAllFiniteEndomorphicQuantumOps` for
that same theory under that same hypothesis. This is not a result that
read/write interaction in general cannot supply QM. The witness establishes
one mathematical instance; it does not show that every native observer
interface satisfies `MonomialSource`, or that every admissible monomial
matrix is an available operation. The closeout review must reject any edit
that drops the hypothesis, changes the carrier or promotes this statement
into a universal physical impossibility claim.

## Scope, resources and preservation

Proposed execution budget for owner review: one defect control and the sole
named `permTheory (Fin 2)` witness for the existing `MonomialSource`; at most
three substantive execution checkpoints (control, witness disposition,
citation/registry closeout). No new predicate is in scope.
Diagnostic fixes within those checkpoints must address the same obligations,
not add candidates or expand theorem scope. The writer records consumed
checkpoints and unresolved obligations in the result. If this bound is
insufficient, stop and report it; no automatic extension is permitted.

Lean and the heavy release suite run in ordinary CI under §A.40, using the
repository's pinned toolchain and existing job limits. No local full Mathlib
build, numerical experiment, parameter search, new workflow or special launch
is part of drafting. Automatic draft-PR CI is permitted and is not an F/E
attestation. Any later exact-head dispatch, including its attempt, must be
explicitly authorized and recorded; a rerun is never silently substituted for
a failed attempt. There is no numerical research budget in this unit.

For publication-facing kernel additions, update
`verification/lean-manuscript-census.json` in the same execution commit and
wire the new module into `OIBridge.lean`. Retain existing theorems and guards,
including the R7-SUB/R7-SRCP publication boundaries. No inference here promotes
the kernel-only `permTheory_not_control` or `obs_not_control` to a manuscript
claim. Mathematical operator admissibility is not physical branch availability.

The three audit corrections and two module descriptions must map each edited
assertion to the defect or a precise surviving theorem. F73/round-63 text may
be qualified, but scientific sample definitions and executable controls remain
unchanged. If a change to an actual guard is unavoidable, freeze and review
the exact proposed change before execution; no post-F weakening is permitted.

## Invariants and measured checkpoints (§A.41)

| Invariant | Required checkpoint/evidence |
|---|---|
| One writer; isolated record; one PR from D | Verify open-PR changed paths, clean worktree and single-parent D-to-head control-plane delta before publication and again before F. |
| Original defect tested | Kernel declaration for the original predicate on `Fin 2`; exact statement and `#print axioms` report included in the compiled new module. |
| Existing hypothesis is inhabited and not assumption-driven | Kernel proof of `MonomialSource (permTheory (Fin 2))` at all extension levels, with the existing theory fields intact; independent statement/dependency inspection and successful kernel checks. |
| Historical semantics retained | Compare old declarations and proof terms with D; retain reviews, legacy bytes, existing native records, memory-swap and interpolation controls. |
| No stale scientific citation or widened no-go | Repeat identifier and contextual corpus searches; list remaining occurrences by role, map each replacement to the actual theorem/carrier/interface, and enforce the mandatory R2 scope sentence. |
| Registry and import coverage | Same-commit census disposition and root import; `tools/lean_manuscript_census.py` plus CI Mathlib/axiom gate. |
| No fabricated protocol certification | Exact F/E owner records and authorized `workflow_dispatch` run identities; PR synthetic-merge CI is never substituted. |
| Recorded computational verdicts are structured | Read host run/job/step identities and conclusions, and checker exit statuses; do not infer a pass from an omitted log line (§A.44). |
| Durable supporting evidence | Control, witness if accepted, reused theorem sources, corrected scope and result are reachable through the round; trace every off-main support reference under §A.42. |

## Verification, review and next gate

Drafting checks: whitespace/diff scope, artifact placement, V3 parser and its
self-test/conformance corpus. Ordinary PR CI supplies the unchanged repository
release checks; its green result would certify the draft integration only.
Do not run the new kernel control or witness proof before execution authorization.

The independent non-author pre-F review by Claude at
`da4f2ca71050764bb99a8834247a1aa5ce87e99b` is ACCEPT WITH CHANGES
(#1359 comment 6946402519, 2026-11-17T11:12:22Z). Its R1 requires reuse of
`MonomialSource` with the named `permTheory (Fin 2)` witness; R2 requires the
explicit conditional `Fin 2` scope. This revision implements those changes
in the proposed design and awaits the reviewer's focused delta check. That
review reference is provenance; the scientific source descriptions above
are checked against the named files at D. The original reviewed commit and
review are preserved. No author-side disposition is independent acceptance.

Claude's independent pre-F review must check the availability derivation target,
nonempty and zero-dimensional scope, satisfiability requirement, path and
preservation inventory, repair/retire criteria, proposed budget and support
tracing. The writer's source reading is not that review. Resolve blocking
findings on this draft; keep every checkpoint reachable. No second model's
acceptance is substituted for the assigned review without an owner decision.

After the focused acceptance, present the exact proposed F and execution
design for the owner's own recorded decisions. Hold the branch at that commit
while any authorized F-attestation dispatch runs; designate F only after all
its jobs pass. Then
execute linearly under the approved scope. E requires the same exact-head
attestation and owner designation. Reconcile only after E (or S12 withdrawal),
generate the receipt with `tools/v3_receipt.py`, and require
`tools/v3_verifier.py --verify-round Q` to report `VERDICT  HOLDS`.

The execution result will report the full commit, changed files, theorem and
axiom identities, citation disposition, checks, attempts, limitations and
unresolved obligations. Claude reviews the exact execution checkpoint before
the owner considers landing. No merge approval is requested by this draft.
