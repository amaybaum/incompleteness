# Reconstruction round PRESERVE-INDUCT-1 — conditional preservation by protocol induction: PREREGISTRATION

**Status: native V3 control-plane record of round PRESERVE-INDUCT-1.**
Its standing is set by the owner's designations and the round's receipt, not
by this text: only the owner designates F, after every condition under
"Conditions for F" below holds and F's exact-head checks pass (AGENTS §A.39),
and an instruction to proceed with design is not F. A linked staging branch
carries the predicted execution files: the two adopted modules, the probe and
its independent check, the root import, the census families and the workflow
edits. The adopted modules are first built at their adopted paths by the
predicted-tree run (condition 3).

**Provenance.** #831 (https://github.com/amaybaum/incompleteness/pull/831)
reconstructed this round's draft from the owner's quoted item B (primitive
preservation extends to built operations), the research criteria and the
kernel constructors. Its head is `65b85147f85aa01770e0e60551152bc5f1d9ef29`.
The branch `wip/preserve-induct-1-controls` drafted `controls.py` and the
control section. Neither chain's commits are imported into this control plane.

```v3-round
round PRESERVE-INDUCT-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-preserve-induct-1/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-preserve-induct-1/
record AM verification/receipts/PRESERVE-INDUCT-1.json
execution A verification/lean-mathlib/OIBridge/PreservationInduction.lean
execution A verification/lean-mathlib/OIBridge/PreservationInductionInstances.lean
execution A verification/lean/preserve_induct1_probe.py
execution A verification/lean/preserve_induct1_indep_check.py
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
```

D: `ec36234cb98a30ecb4681e118ff9ccb82e19aa6d`, main after #877 (owner decision of
2026-10-19). Between the earlier design base `501331f5` and D, main changed only
`AGENTS.md`. D carries the evidence archive's research-build entries, which reached
main with #860: the historical retention rows below name them, and the release
gate's `evidence-retention` step judges this record's citations of them at F and
at every later commit. Before F, the control-plane delta contains only this
preregistration and review amendments. Manuscripts, built artifacts, ROADMAP,
other kernel modules, the evidence archive and other rounds' records are
outside this round's edit scope.

## Question

Fix an independently specified family of unnormalized preparation cones C_S
on every finite matrix carrier, separately from an implementation class 𝓘.
Do explicit preservation assumptions for the primitive steps, readout,
uniform attachment and discard imply branchwise preservation for every
family built by `InstAvail`?

## Research builds and the theorem budget

The research sources are `PreservationInduction.lean` and
`ResearchInstances.lean` in `preservation-induction-design/`, on the research
branch `research/preservation-induction-design-20261013`, cited as provenance.
They are not reachable from D; the evidence archive retains both source
commits under `objects/`. The research record (`result.md` there) describes
the design, and its two exact scripts are the ancestors of this round's exact
layer. The core source, SHA256
`f7a92732416f0d403ae68e8cc682f51ca8a0bf73742f6c83c92eb04d15571e51`, has five
named theorems and the six definitions listed below.
The source
compiled at `e684897da41b1c3d066b880194c9beb87a19b7ad`, workflow run
[38450187534](https://github.com/amaybaum/incompleteness/actions/runs/38450187534).
Its job 115478781754 had every step `success`. The archive's expected result of
that build is pinned as the `core-build` row below. It records build success
with no failure marker and the reports of the workflow's library targets, and
it records the core's own four axiom reports as a gap: the research workflow
ran `lean` directly on the design file, whose reports its extractor does not
read. Those four reports, described in the research record as containing only
`propext`, `Classical.choice` and `Quot.sound`, are therefore attributed
provenance, and this round establishes them again at E.

The six core definitions are:

1. `CarrierConeFamily`: a set C_S of matrices for each finite carrier S,
   specified independently of availability.
2. `AdditiveClosure`: exactly zero membership and addition closure for each
   C_S. Real scaling, Hermiticity, convexity, closedness and normalization are
   not used by the induction. No minimality is claimed.
3. `PreservesCarrier`: for an endomorphism Φ, X∈C_S implies Φ(X)∈C_S.
4. `PrimitivePreservation`: two distinct fields: each admitted isometric
   conjugation preserves C_S, and each branch of an admitted native register
   readout preserves C_S. A nontrivial projection is not an isometry.
5. `UniformAttachPreservation`: for m>0, `uniformAttach m` sends C_S into
   C_(S×Fin m). It attaches I/m, not a pure ancilla.
6. `AncillaDiscardPreservation`: for m>0, `ptraceAnc m` sends the composite
   cone C_(S×Fin m) into C_S.

The headline, with implicit carrier and outcome instances and the
implementation-class binder suppressed in this display, is:

```lean
theorem instAvail_preserves
    (C : CarrierConeFamily) (hC : AdditiveClosure C)
    (hPrim : PrimitivePreservation 𝓘 C)
    (hAttach : UniformAttachPreservation C)
    (hDiscard : AncillaDiscardPreservation C)
    (h : InstAvail 𝓘 S O F) :
    ∀ a, PreservesCarrier C S (F a)
```

The proof is one induction on the `InstAvail` derivation, one arm per
constructor (Induction route, below). `finite_sum_mem` gives the coarse arm
from `AdditiveClosure` alone, and the discard arm uses the attachment and
discard premises together on the enlarged carrier, with its own induction
hypothesis there.

The core also contains `finite_sum_mem`, `instAvail_sum_preserves`, summing
the unnormalized branches, and `instAvail_spectator_preserves`, which applies
the headline on the joint carrier to `instAvail_spectator`; its additional
premises are exactly the context and label hypotheses. Then
`instAvail_transport_preserves` proves preservation of the cone assigned to
the destination carrier. It does not identify that cone with a reindexing of
the original cone; that would need a separate preparation-covariance premise.
No iff, minimal-premise result, reconstruction theorem or physical source is
part of the headline.

The instance source, SHA256
`54b1451e1788fe6b71ca28eb81d2e9031abf1f78ee92d471bfddd73256044c65`,
compiled at `febfe5e2668d3c000ec1d4ce7e4041f4feabd3c3`, workflow run
[38454439833](https://github.com/amaybaum/incompleteness/actions/runs/38454439833).
Its job 115493410133 had every step `success`; the build is pinned as the `instance-build`
row. That build's expected result records the core and instance design
files' ten reports as a gap in the same way, and they are established again at
E. Neither historical build is a native execution, and the predicted-tree run
cannot verify either retroactively.

The instance module adds four definitions and abbreviations, `quantumCone`,
`classicalCone`, `classicalClass` and `attachBlock`, and nineteen named
theorems: `classicalCone_iff`, `quantum_additive`, `quantum_conj`,
`quantum_primitive`, `attachBlock_apply`, `uniformAttach_eq_blocks`,
`quantum_attach`, `ptraceAnc_eq_blocks`, `quantum_discard`,
`quantum_instAvail`, `quantum_fullClass`, `classical_additive`,
`classical_conj`, `classical_primitive`, `classical_attach`,
`classical_discard`, `classical_readProj`, `classical_instAvail` and
`classical_native_readout`. Two anonymous examples check the classical
inventory's context stability and label invariance. The two-module surface is
ten definitions and abbreviations, twenty-four named theorems and those two
examples; no physical source is imported.

## Status of the premises

The proof is induction on the availability derivation. It is a conditional
soundness theorem, not a source for any preservation premise or a new
compatibility principle. C_S is not defined as a reachable closure, the
general statement does not identify C_S with PSD, and the validity theorem on
PSD is not used as though it identified an arbitrary physical cone.

The five constructors are exactly `op`, `readout`, `coarse`, `bind`, `discard`
in `ImplementationLocality.lean:268`. `ContextStable` (:359) and
`LabelInvariant` (:364) concern inventory membership and do not say that the
independently given cone is preserved. The availability theorems
`instAvail_transport` (:644), `instAvail_spectator` (:789) and
`instAvail_withSpectator` (:820) serve conditional corollaries; none
discharges state preservation by itself.

## Adoption: modules, root import and census

- **Modules.** `OIBridge/PreservationInduction.lean` is the core source and
  `OIBridge/PreservationInductionInstances.lean` the instance source, with
  exactly these changes: the namespace `OIBridge.PreservationInductionDesign`
  becomes `OIBridge.PreservationInduction` (`NS` in `controls.py`); the import
  `ResearchDesign.PreservationInduction` becomes
  `OIBridge.PreservationInduction`; each module header is rewritten; and the
  core's comment line about a design build is removed. Every import other than
  that one, every `open` line, declaration, proof, example and print is
  byte-identical to the research source. No statement is changed or
  strengthened, so the same proofs are expected to elaborate at the adopted
  paths; the first build there, in the predicted-tree run, is the check.
- **Root import.** `import OIBridge.PreservationInduction` and
  `import OIBridge.PreservationInductionInstances`, directly after the last
  import line of `OIBridge.lean` at D.
- **Census (§A.35).** Two families appended to
  `verification/lean-manuscript-census.json` at D (`FAMILIES` in
  `controls.py`): the core as conditional preservation of an independently
  given carrier cone family, and the instances as positive semidefinite and
  nonnegative diagonal comparisons. Both are `kernel-only`, with no manuscript
  and so no anchor. Both modules are new, so no supersession entry is due.
  The census tool passes on the design tree.

## Induction route

| Constructor at D | Preservation step |
|---|---|
| `op` | the admitted-isometry field of `PrimitivePreservation` on the same carrier |
| `readout` | its separate readout field on every branch of the reindexed register projection |
| `coarse` | every summand lies in C_S by induction; finite-addition closure handles the fibre, an empty fibre via zero |
| `bind` | the first induction hypothesis on X, then the outcome-dependent continuation hypothesis on its output |
| `discard` | attach uniformly into C_(S×Fin m), induction on the enlarged carrier, partial trace back into C_S; m>0 |

`uniformAttach` is `OperationalAssembly.lean:492`, `ptraceAnc` :453 and
`discardWith` :515, partial trace composed with the operation and
preparation. `instAvail_trace` (`ImplementationLocality.lean:317`) is an
aggregate normalization theorem; trace preservation does not prove membership
in an arbitrary cone.

## The exact layer: probe and independent check

`verification/lean/preserve_induct1_probe.py` interprets the five
constructors with exact SymPy 1.14.0 matrices, checks positive
semidefiniteness through every principal minor and prints `SYMPY 1.14.0`.
`verification/lean/preserve_induct1_indep_check.py` is a second
implementation: rational complex arithmetic from the standard library, Kraus
paths instead of a protocol tree, and neither SymPy nor the probe imported,
which it checks. Both run the same protocol on the same five inputs, and both
print the digest `a1f82e289ba07a4c60dd6b56396dcdf7c0c217b2ff49a8d779f1c4e923842ea9` of the full sample manifest, every entry of every
final branch; the research scripts reached the same digest. Each prints one
`PASS` or `FAIL` line per code with its count, `checks: N, failures: 0`, and a
final line, and exits 1 on any failure.

- **Probe codes** (127 checks): `CONSTRUCTORS`, `ISOMETRY`, `READOUT`, `ATTACH`, `AGGREGATE`, `EMPTY`, `NONVACUOUS`, `BRANCH-PSD`, `BRANCH-DIAG`, `RELABEL`, `COUNTER-HADAMARD`, `COUNTER-READOUT`, `COUNTER-DISCARD`, `MANIFEST`, `MUTATION-RULE`.
- **Independent codes** (47 checks): `I-TRACE`, `I-EMPTY`, `I-PSD`, `I-DIAG`, `I-HADAMARD`, `I-READOUT`, `I-DISCARD`, `I-SEPARATE`, `I-MANIFEST`.
- **Mutation runs.** The seven boolean guards of the research script are
  replaced by eight mutation runs. Each run evaluates the faithful step and
  the mutated step separately, and the mutation is rejected only when its
  named check holds on the faithful step (an exact `True`) and fails on the
  mutated one (an exact `False`, or that check's own violation raised by the
  evaluator). A run that raises any other exception, or returns anything but a
  bool, is undecided: a crash is not a rejection. The probe prints one
  `REJECTED`, `SURVIVED` or `UNDECIDED` line per run and
  `mutations: R rejected, S survived, U undecided`, and fails unless exactly
  eight distinct runs exist, all eight ran and all eight are rejected.
  `MUTATION-RULE` checks that reading on its own cases (an exact `True` holds;
  an exact `False` and the named violation fail; a crash, another check's
  violation and a non-bool value are undecided) and that exactly eight distinct
  runs exist. The runs:
  `readout-as-isometry: op-isometry`, `aggregate-for-branch: branch-cone`, `discard-enlarged-premise-dropped: branch-cone`, `labels-as-cone-transport: branch-cone`, `availability-as-source: branch-cone`, `pure-for-uniform: attach-cone`, `empty-fibre-dropped: empty-fibre`, `discard-omits-sum: aggregate-trace`.

**The ninth governed path.** `verification/lean/preserve_induct1_indep_check.py`
is the ninth entry of the governed-path block. Its exact content is named and
pinned here before F; C2 checks every row against the file at `E`, and
`candidate` against a candidate tree.

| property | value |
| --- | --- |
| path | `verification/lean/preserve_induct1_indep_check.py` |
| governed entry | `execution A verification/lean/preserve_induct1_indep_check.py` |
| blob | `b2e3f1782f475d6526e5084ba0037d6cabb2eead` |
| sha256 | `7cd1e8192817a37d56111ceae2ca2c7f52a770a9e586e1a602140153c0e9c8ba` |
| bytes | `7202` |
| imports | `dataclasses`, `fractions`, `hashlib`, `json`, `sys` |
| codes | `I-TRACE`, `I-EMPTY`, `I-PSD`, `I-DIAG`, `I-HADAMARD`, `I-READOUT`, `I-DISCARD`, `I-SEPARATE`, `I-MANIFEST` |
| checks | `47` |
| final line | `preserve_induct1_indep_check: OK -- 47 checks` |
| stdout sha256 | `4031a930ff47634992177e42bcc59455b922d217a0b221d0d83f98159226e72f` |

The comparisons the codes cover:

- **Quantum:** PSD, with isometric conjugations, register projections,
  uniform attachment and partial trace (`BRANCH-PSD`, `I-PSD`). The Lean
  instance establishes the premises on every finite carrier for any inventory.
- **Classical:** nonnegative diagonal states with monomial operations and
  coordinate readouts, including a genuinely outcome-dependent continuation
  (`BRANCH-DIAG`, `I-DIAG`). The Lean source proves projector admission for
  reindexed register readouts; it does not claim every classical stochastic
  instrument is available.
- **Operation countercontrol:** a diagonal state taken outside the diagonal
  cone by an available Hadamard conjugation (`COUNTER-HADAMARD`,
  `I-HADAMARD`, mutation `availability-as-source`).
- **Readout countercontrol:** nonnegative multiples of I are preserved by
  isometric conjugation, uniform attachment and partial trace, and a
  coordinate readout sends I to a nonscalar projector (`COUNTER-READOUT`,
  `I-READOUT`, mutations `readout-as-isometry` and `aggregate-for-branch`).
- **Constructor coverage:** every constructor, an empty coarse fibre, nested
  bind and discard, positive-size ancillas and a nontrivial relabelling
  (`CONSTRUCTORS`, `EMPTY`, `RELABEL`), with no vacuous positive
  (`NONVACUOUS`).
- **Conditional scope:** the bridge compatibility research record
  (`bridge-compatibility-audit/`, on main since #820) reports exact,
  uniformly available depth-one failures for the cones K_B and K(Z_F). They
  diagnose the missing premise source. No family extending either cone is
  claimed to satisfy the premises, and no decision here rests on that record.

These certify the recorded finite examples only. Universal claims rest on the
kernel proofs; finite checks do not upgrade them, a mutation does not prove a
premise necessary, and the round claims no minimality of its premise package.

## Decision rules and earned reading

Q-CORE reads the Lean layer only and the exact layer is read only by Q-EXACT
(owner recommendation 1):

- `PRESERVE-INDUCT-CORE-PROVED`: every required static control passes; the
  axiom report of `instAvail_preserves` and the six Lean positive-instance
  reports lie within `propext`, `Classical.choice` and `Quot.sound`. No probe
  output is read.
- `PRESERVE-INDUCT-COROLLARIES-PROVED`: Q-CORE's conditions, and the three
  corollary reports likewise, every extra premise displayed. No probe output
  is read.
- `PRESERVE-INDUCT-EXACT-CHECKED`: every required static control passes; the
  probe and the independent check pass by their frozen rules, agree on the
  manifest digest and replay byte for byte, and every frozen mutation run is
  rejected, none surviving or undecided. No axiom report is read.
- Otherwise the unresolved or halted result is recorded through the native
  lifecycle, with no successful token printed over a failed required control.

**Earned reading, only when all three cells are positive:** supplied
primitive state-preservation, attachment/discard and zero/additive-closure
premises propagate to every finite `InstAvail` derivation. This reduces a
protocol-closure proof to a finite list of constructor obligations. It does
**not** establish a finite list of concrete physical operators generating 𝓘.

**Non-inference rule:** the theorem sources no primitive preservation,
context stability, label/cone covariance, state-space identification, flow,
gate, test validity or quantum inclusion. It does not close K2 or P0 and is
not a substitute for the bridge audit's physical-source and disguise tests.
It supplies no part of the extension that the `P1 — F2` row lists as open
(ROADMAP :1125–1129 at D): the compatible state transformations named there
are assumed by the `op`, `readout`, attachment and discard premises. The
inventory constrains which cones can satisfy the premises: `fullClass` admits
every isometry, and the diagonal cone fails its `op` premise, since an admitted
Hadamard conjugation takes a diagonal state outside it (`COUNTER-HADAMARD`,
`I-HADAMARD`). That belongs to the assumption audit and is not a success for
sourcing compatibility. No manuscript or ROADMAP change is licensed here.

## Controls, verdict interface and invariants

`controls.py` is on the staging branch. The control plane at `F` holds only
this file and `amendments/` (spec `S2`), so `controls.py` enters with the first
execution commit, at the blob pinned below. Neither it nor any other file of
the round names the research builds' run numbers, which the evidence archive
admits only in this record while its citations are pending (R13): `controls.py`
reads them from the archive and from this file.

**Stages.**
1. `S1`: `controls.py` at its pinned blob and `F`'s exact-head run under
   `evidence/f-run/`, with the predicted-tree expected result if it is
   record-relative.
2. The two modules, the probe and the independent check at their pinned
   blobs; the workflow, import and census edits.
3. The result note, candidate `E`.

**Static controls.** `controls.py check E --freeze F` runs all fourteen at
`E`. With `--stage S1` it runs C1, C2 (for `controls.py` only), P, R, A, G and
T at the first execution commit. Any other stage or argument is refused.
`controls.py candidate X` runs the ten that need no `F` (C2, S1, S2, S3, S4
for the module headers, W, I, J, A and G) on the candidate execution tree of a
commit X, against the preregistration at X. It is the executor's check of the
predicted tree before F and of a candidate before E; it is not an input of
`verdict`, and the workflow does not run it.

| code | measures |
| --- | --- |
| C1 | the preregistration at `E` is the one at `F`, and names this `D`, the round declaration, and the citation of `65b85147` with the link to #831 |
| C2 | the five frozen execution blobs below at `E` (at `S1`, `controls.py`'s); no pin pending; at `E`, every row of the ninth governed path's table against the file |
| S1 | each module equals its block in the frozen statement-surface section: imports, namespace and `open` lines, the declarations in order with their statements (a definition's whole text), the two examples, the prints; no `sorry`, `admit`, `native_decide`, `axiom`, `implemented_by` or `extern` |
| S2 | the landed objects below at their pinned lines, with `D`'s blobs at `E`; the cited span below with its pinned digest at `D` and `D`'s blob at `E`; every line citation in this file's prose is one of those pinned lines or spans |
| S3 | the core module mentions no PSD, Hermiticity, convexity, closedness, trace, reachability or iff; `AdditiveClosure` has exactly the fields `zero_mem` and `add_mem`, and `PrimitivePreservation` exactly `op` and `readout`; `instAvail_preserves` is one induction on the derivation with the arms `op`, `readout`, `coarse`, `bind`, `discard` in that order; the corollaries apply `instAvail_preserves`, the latter two to `instAvail_spectator` and `instAvail_transport`; no research import or namespace remains; no preparation family is defined through `InstAvail` |
| S4 | both module headers and the result note are present, without the excluded phrases frozen in `controls.py` (`PHRASES`) |
| W | `verify.yml` at `E` is `D`'s with the frozen splices (`SPLICES`), each anchored once; they install SymPy as `sympy==1.14.0` and name it in no other form |
| I | `OIBridge.lean` at `E` is `D`'s with the two import lines directly after its last import line |
| J | the census at `E` is `D`'s with the frozen families appended |
| P | the three retention rows: a historical row an archived expected result, a digest or a recorded gap, the predicted-tree row a digest; every digest row's file present at `E` with that digest, and a file outside the record directory present at `D` and unchanged at `E`; no row pending |
| R | the record directory holds exactly this file, `controls.py`, the record-relative files the digest rows name, a non-empty `evidence/f-run/`, `amendments/` if present, and at `E` the result note |
| A | the archive's research-build entries and retained commits that await this round name this file; each run is cited free-standing on exactly its recorded line and on no other line, with its full head beside it and no other head; the recorded line's text, and line 68's, has its pinned digest (the text of that line at #831's head `65b85147`); no other file outside the archive names the run; the recorded lines are 69 and 127 |
| G | the governed-path block equals the nine entries above; every change from `D` is authorized under spec `S7`; the receipt is absent; the legacy manifest is unchanged |
| T | `delta(D, F)` is this file and `amendments/`, drafted by single-parent commits from `D`, none of them #831's `5f614d60` or `65b85147`; the execution after `F` is non-empty and linear, and `F` is an ancestor of `E` |

**Design parameters.** `controls.py` sets `NS`, `SPLICES` (six splices: the
probe shard job before the Act 42 comment, checked out with `fetch-depth: 0`
because the self-test reads `D`; its entry in the aggregate's `needs`,
environment, echo and test lines; and a final step of the required bridge job
that prints the ten axiom reports again with `lake env lean`, so the verdict
reads them from that step's block), `FAMILIES` and `PROBE_SPEC` (the codes, counts,
final lines and stdout digests of both scripts, the eight mutation runs, the
manifest digest and the SymPy pin). With any of them `None` the controls that
depend on it fail closed.

**The bridge-job step fails closed.** It runs under `set -euo pipefail`,
first prints `preserve_induct1 axioms: step at <SHA>` with the checked-out
commit (`git rev-parse HEAD`), tees both modules' output into one log, and ends
with `controls.py axioms` on that log. The gate exits 1 unless each of the ten
printed names is reported exactly once in `NS`, within `propext`,
`Classical.choice` and `Quot.sound`, no other name of `NS` is reported, and the
log carries no `sorryAx`, `Lean.ofReduceBool` or `Lean.trustCompiler`; an empty
or unreadable log fails. It ends with `preserve_induct1 axioms: OK -- 10
reports` on success and `preserve_induct1 axioms: FAILED` otherwise. A failure
of the step fails the required `Mathlib bridge` check.

**How `verdict` reads the bridge log.** Q-CORE and Q-COR read the reports only
from that step's block of E's served bridge-job log, its timestamps removed:
from the step's one marker line to the next step header (`##[group]Run`) or
the job's cleanup. The marker must name E's full SHA. The archive's one whole
served job log (`bg3/design-116831668411.log`) carries the head SHA after the
checkout's `git log -1 --format=%H`, but the archive keeps its served bridge
logs as 5000-line tails without the checkout section, so the step prints the
SHA itself; a checkout line, where the log carries one, must name E as well.
The block must carry exactly one OK line of the gate, after its last report,
no `##[error]` line and none of the three tokens, and each read report exactly
once; the log must carry no FAILED line of the gate. The Build step's copies of
the reports and the release gate's summaries lie outside the block and are not
read, so the gate's 60-character summary of `lean_axiom_check` plays no part.

**Prints**, as in the research design. Core: `instAvail_preserves`,
`instAvail_sum_preserves`, `instAvail_spectator_preserves`,
`instAvail_transport_preserves`. Instances: `quantum_instAvail`,
`classical_instAvail`, `quantum_attach`, `quantum_discard`,
`classical_readProj`, `classical_native_readout`. No printed name contains a
prime, so the archive's extractor reads every report of E's run. Lean wraps a
long report across lines; `verdict` and `axioms` read a served job log without
each line's leading timestamp, as the archive's extractor does, so a wrapped
report parses whole.

**S2's landed objects at D.** Each line was read at `D` = `ec36234c`; the
self-test reads them there through git, and S2 requires them at `E`.

| object | location |
| --- | --- |
| `ImplementationClass` | `ImplementationLocality.lean:244` |
| `readProj` | `ImplementationLocality.lean:256` |
| `InstAvail` | `ImplementationLocality.lean:268` |
| `instAvail_trace` | `ImplementationLocality.lean:317` |
| `ContextStable` | `ImplementationLocality.lean:359` |
| `LabelInvariant` | `ImplementationLocality.lean:364` |
| `fullClass` | `ImplementationLocality.lean:374` |
| `instAvail_transport` | `ImplementationLocality.lean:644` |
| `instAvail_spectator` | `ImplementationLocality.lean:789` |
| `instAvail_withSpectator` | `ImplementationLocality.lean:820` |
| `ptraceAnc` | `OperationalAssembly.lean:453` |
| `uniformAttach` | `OperationalAssembly.lean:492` |
| `discardWith` | `OperationalAssembly.lean:515` |
| `conjChannel` | `MonoidalCompletion.lean:360` |
| `amplRefL` | `ReferenceExtension.lean:131` |
| `transport` | `SpectatorBridge.lean:348` |
| `substratumClass` | `StructuralClosure.lean:180` |
| `substratumClass_contextStable` | `StructuralClosure.lean:261` |
| `substratumClass_labelInvariant` | `StructuralClosure.lean:275` |

**Pinned line citations.** The span this file cites outside the landed
objects, this file's own two run citations and line 68 (the full head beside
the first), each by the sha256 of its text (a span's lines joined by newlines
with a final newline; a single line without its newline). Lines 68, 69 and 127
are byte-identical to those lines of
#831's head `65b85147`, where the evidence archive recorded the pending
citations; they are neither moved nor rewritten.

| cited text | lines | sha256 |
| --- | --- | --- |
| `verification/ROADMAP.md` at `D` | 1125–1129 | `bfcc4fd0c5ebc02e2f9d65c99b52eb3d899f33d8e19c47be00dafa2e32305e50` |
| this file | 68 | `b49b3e674845d1cbb2616d0133c7e599b166466138c701e6dc73d80c55a14ea2` |
| this file | 69 | `2892155d251408c8f5da1ab66639303103de9a7fae97d56309eaef697c7af473` |
| this file | 127 | `bf84b537a746956779fd48b78843c1d0226f516c8a201c9b2ddc5ca2c2f1a8e3` |

**Frozen execution blobs.** C2 checks these. A different blob at `S1` or at
`E` is a deviation from the frozen design, not a repair: it is recorded in
the result note, and the round halts. The module blobs are pinned before
their first build at the adopted paths; if the predicted-tree build requires
an edit, the edit and its pins change here before `F`.

| path | blob |
| --- | --- |
| `verification/programmes/oi-qm/reconstruction/round-preserve-induct-1/controls.py` | `208801fcb4b96808c8f9a3d5c7175bcf79d38981` |
| `verification/lean-mathlib/OIBridge/PreservationInduction.lean` | `a40464f53afb97c7489210b78bee485f0d65fbb2` |
| `verification/lean-mathlib/OIBridge/PreservationInductionInstances.lean` | `13b786c7bae8944fda62e50b13e80ca1574b9a0e` |
| `verification/lean/preserve_induct1_probe.py` | `0333a734b61ce72943ccf9505fc256167d1d3ca6` |
| `verification/lean/preserve_induct1_indep_check.py` | `b2e3f1782f475d6526e5084ba0037d6cabb2eead` |

**Verdict.** `controls.py verdict E --freeze F --axioms <E's exact-head bridge-job
log, as served>` prints one token per cell:

| cell | positive | otherwise | rule as implemented |
| --- | --- | --- | --- |
| Q-CORE | `PRESERVE-INDUCT-CORE-PROVED` | `PRESERVE-INDUCT-CORE-NOT-ESTABLISHED` | the static controls pass; the final bridge step's block is read alone (its marker names E, one OK line of the gate after its last report, no FAILED line in the log, no `##[error]` line and no `sorryAx`, `Lean.ofReduceBool` or `Lean.trustCompiler` in the block); there the report of `instAvail_preserves` and the six Lean positive-instance reports each appear once and lie within `propext`, `Classical.choice` and `Quot.sound`; no probe output is read |
| Q-COR | `PRESERVE-INDUCT-COROLLARIES-PROVED` | `PRESERVE-INDUCT-COROLLARIES-NOT-ESTABLISHED` | Q-CORE's conditions, measured again, and the three corollary reports |
| Q-EXACT | `PRESERVE-INDUCT-EXACT-CHECKED` | `PRESERVE-INDUCT-EXACT-NOT-ESTABLISHED` | the probe and the independent check at their blobs at `E`, each run alone with `python3 -I -B`: exit 0, empty standard error, no `FAIL`, every frozen code, the frozen check count with no failures, the frozen final line and stdout sha256 (the byte replay); the probe's `SYMPY 1.14.0` line; every frozen mutation run `REJECTED`, exactly once each, the summary `mutations: 8 rejected, 0 survived, 0 undecided` and no `SURVIVED` or `UNDECIDED` line; both print the frozen manifest digest |

Q-CORE and Q-COR read no probe output, and Q-EXACT reads no axiom report;
the static controls gate all three. If any of the fourteen fails or is not
reported, `verdict` prints the failed controls, runs no probe and reads no
axiom report; every cell prints its `NOT-ESTABLISHED` token, the round prints
`PRESERVE-INDUCT-1-NOT-READ`, and the exit status is 1. Otherwise each cell
prints by its own rule and the round prints `PRESERVE-INDUCT-1-READ`. The
full earned reading is printed only when all three cells are positive.

**Self-test.** `controls.py --self-test` runs in the probe shard at every
later commit, so it reads no file of the working tree but `controls.py` and
this file. The historical objects it cites are read at `D` through git: the
landed objects on their pinned lines, the cited span with its digest, and the
archive's pending citations with their run heads, against which it checks
control A's rule on this file, including the pinned text of lines 68, 69 and 127.
When `D` is not in the repository's history it fails closed. The candidate
execution tree is tested separately, by `candidate` before F and by `check` at
`E`. The self-test also checks this file's tables against `controls.py` and
every prose line citation against the pinned lines; runs mutation controls on
S1 and S3 over a synthetic fixture; drives the probe rule with crashed,
surviving and repeated mutation runs; drives the bridge job's axiom gate with
clean, missing, repeated, dirty and unexpected reports; drives `verdict` with
injected static results and the cells' separation, and over served bridge logs
with each rule of the final step's block broken (the reviewer's log, whose gate
printed FAILED over clean Build-step copies; no OK line, two, or one before the
last report; a FAILED line elsewhere; the step or the checkout at another
commit; no marker or two; an error line, a token or a repeated report in the
block), and with dirty copies outside the block left unread; drives `verdict` end to end
through the real `check()` on an in-memory `D`, `F` and `E`, unmutated, with
each control's record call removed and with each control's inputs absent; and
drives `candidate` on the same fixture. In every failing case `verdict` must
fail, name the control, print no positive token and never run the probe. The
fixture is synthetic, never compiled and no evidence for any theorem.

**Invariants and their checkpoints (§A.41).**

| invariant (where this file asserts it) | checkpoint |
| --- | --- |
| before `F` the control-plane delta is this file and its amendments | T at `S1` and `E`; `G9` under `v3_verifier --verify-round Q` |
| the drafting chain is a new linear branch from the finalized `D` that cites `65b85147` and links #831 and imports none of #831's commits (owner decision of 2026-10-17) | C1; T; reviewers check that #831 is closed as superseded once the replacement exists |
| the archive's pending citations of this record stay as recorded: each run on its recorded line only, that line's text as at #831's head, its head beside it, no other file naming it (D; R13 and O10) | A at `S1` and `E`; `candidate`; the release gate's `evidence-retention` step at `F`, `E` and `Q`; the self-test's check against the archive at `D` |
| every line this file cites (landed objects, the ROADMAP span) is pinned, verified at `D` and matched exactly | S2 at `E`; `candidate`; the self-test, reading `D` |
| the self-test's historical fixture is read at `D`, so no change to the working tree alters it; the candidate tree is tested separately | the self-test (`D` present, fail closed otherwise); `candidate`; C1–T at `E` |
| execution starts from the frozen control plane; `controls.py`, the modules, the probe and the independent check are the frozen ones | C1; C2 at `S1` and `E` |
| no manuscript, built artifact, ROADMAP, other kernel module, archive file or other round's record changes | G at `S1` and `E`; S2 |
| the preparation family is specified independently: not a reachable closure, not PSD in the general statement | S3 |
| the induction uses only zero and addition closure, and readout is a field separate from the isometric step | S1; S3 |
| the proof is one induction over the five constructors | S3; the kernel build at `E` |
| the corollaries' extra premises are exactly those displayed, and transport preserves the destination carrier's cone without identifying it with a reindexing | S1; S3 |
| the adoption changes only the namespace, the research import, the headers and one comment | S1 against the frozen surface; S3 (no research mark); the staging branch's diff against the research sources |
| the root import and census entries | I; J; the release gate's `lean-manuscript` step at `E` |
| every declaration elaborates within `propext`, `Classical.choice` and `Quot.sound`, with no `sorryAx` | the exact-head run at `E`, every job `success`; the ten reports read by `verdict --axioms` from the bridge job's final step |
| the exact layer covers every constructor, an empty coarse fibre, nested bind and discard, positive-size ancillas and a nontrivial relabelling, without vacuous positives, and rejects the frozen mutations | the probe's frozen codes and mutation runs, read by Q-EXACT; the probe shard green at `E` |
| a mutation counts as rejected only on an exact faithful `True` and mutated `False` or the named violation; a crash or a non-bool result is undecided and fails; exactly eight runs exist and ran | the probe's `MUTATION-RULE` code, its run count and summary line, read by Q-EXACT; the self-test's probe-rule cases |
| the ninth governed path has exactly the content named in its table | C2 at `E`; `candidate`; the self-test's table check against the pins and `PROBE_SPEC` |
| the bridge-job step fails closed on a missing, repeated or dirty report | `controls.py axioms` in that step; W; the self-test's axiom-gate cases; the bridge job green at `E` |
| the Lean cells read only the final bridge step's block of E's log, bound to E, with one OK line after its last report and no FAILED line | `verdict`'s step rule; the self-test's served-log cases, including the reviewer's log |
| a separate arithmetic implementation and a byte replay are kept; SymPy is pinned to 1.14.0 | Q-EXACT (the independent codes, both stdout digests, the shared manifest digest, the `SYMPY 1.14.0` line); W (`sympy==1.14.0`) |
| Q-CORE reads the static controls, the universal theorem's report and the positive-instance reports only; Q-EXACT alone reads the exact layer | the self-test's `verdict` separation cases |
| the full earned reading only when all three cells are positive | the earned-reading line printed by `verdict`; owner review of the result note |
| the workflow runs the probe, the independent check and `controls.py --self-test` | W; the exact-head run at `E` |
| no positive token over a failed or unreported required control | the self-test's `verdict` regression and end-to-end cases |
| the result note asserts no source, closure or implication beyond the earned reading | S4; owner review of the result note |
| the historical builds stay attributed provenance for what their expected results do not carry, and the predicted-tree run establishes results for its own tree only (owner recommendation 3) | P and R at `S1` and `E`; reviewers check each pin and that no claim about the historical builds rests on the predicted-tree run |
| `F`'s exact-head run is retained by the first execution commit (§A.42 item 2) | R at `S1`; reviewers check that it names `F`'s run, job and digest |
| `E`'s exact-head run reaches `main` through its own evidence-retention pull request before reconciliation, and the receipt names each retained file's digest | reviewer check of that pull request and of the receipt's candidate entry for `E`; `evidence-retention` at `Q` |
| the native receipt holds; the legacy records are untouched | `v3_verifier --verify-round Q`; `legacy_records_check.py` at every stage commit and at `Q`; G |

## Owner recommendations (not decisions)

1. Q-CORE requires the static controls, the universal theorem's report and the
   Lean positive-instance reports; the exact layer stays in Q-EXACT. The full
   earned reading requires every advertised cell to pass.
2. The probe may depend on SymPy 1.14.0, pinned explicitly, with the workflow
   installing `sympy==1.14.0`. The separate arithmetic implementation and the
   byte replay are kept.
3. The two historical builds are retained where recoverable; where they are
   not, the gap is recorded and the builds stay attributed provenance. The
   predicted-tree run establishes results only for its own tree.
4. `controls.py` stays on the staging branch until execution.

## Owner decision (2026-10-17): the replacement drafting pull request

- It is a new linear branch from the finalized D, carrying the revised
  control-plane text (this file and `amendments/`).
- It cites #831's head `65b85147f85aa01770e0e60551152bc5f1d9ef29` and links
  #831 (https://github.com/amaybaum/incompleteness/pull/831).
- #831 stays open until the replacement pull request exists, and is then
  closed as superseded.
- #831's commits (`5f614d60`, `65b85147`) are not imported into the new
  drafting chain.

## Owner decisions (2026-10-19)

1. D = `ec36234cb98a30ecb4681e118ff9ccb82e19aa6d`, re-cut before F with the
   anchors revalidated there: the D paragraph and `D` in `controls.py`; the
   landed-object lines, the ROADMAP span, the splice anchors, the import and
   census bases, the archive's pending citations and the frozen blobs, all
   read at that commit.
2. The fail-closed extra step in the required bridge job is approved: the
   bridge-job paragraph above, the sixth splice and `controls.py axioms`.
3. The ninth governed path is approved, with its exact content named and
   pinned before F: the ninth-path table above, checked by C2.
4. The seven boolean guards are replaced by eight mutation runs, and crashes do
   not count as kills: the mutation-run rule above, `MUTATION-RULE` and the
   probe rule of Q-EXACT.
5. Citation positions are pinned on verified source lines and matched exactly;
   cited lines are neither moved nor rewritten: the pinned-line table, A and S2.
6. The inherited self-test reads its historical cited objects at `D`, and the
   candidate execution tree is tested separately: the self-test paragraph and
   `candidate`.
7. The re-cut on D is authorized as design. A predicted-tree dispatch, the F
   designation and any replacement of #831's head each need their own owner
   authorization. The recovered design on `501331f5` (`267824a1`, `1f988909`,
   `895d984bfae1abd1a5bb4196d2c75022a15c8c64`) is kept unchanged under its
   preserve ref as provenance.

## Conditions for F

The owner designates F only when all of these hold:

1. The adopted modules are reviewed against the research sources.
2. `controls.py candidate` passes on the predicted execution tree: the staging
   branch's tree with this file and `controls.py`, less the result note.
3. That tree is built in every event mode used to certify `E`, by a dispatch
   the owner authorizes, with every job `success`. A proof edit it needs
   changes the module bytes and their pins here.
4. That run's expected result is retained and the `predicted-tree` row below
   is pinned; P fails on a pending row.
5. The replacement drafting pull request carries this file at F, and F's
   exact-head checks pass.

**Retained evidence (§A.42).** Each row is a structured expected result in the
form of §A.42 item 1. A historical row names `archive` when the expected
result is the one the evidence archive holds for that build: `controls.py`
finds it by its digest among the archive entries whose pending citation awaits
this file on the row's line (69 for `core-build`, 127 for `instance-build`),
and requires it present at `D` and unchanged at `E`. The predicted-tree row
names a record-relative file committed by the first execution commit and
carries a digest. `F` is not designated with a pending row.

| row | file | sha256 |
| --- | --- | --- |
| `core-build` | archive | `8dfbeb2b950d3474e239c3398cd3cb76fc75aae22ef1b7c8942729883f41bba1` |
| `instance-build` | archive | `647c69f0cadc7dd89e77d0b189eeabeab28e63ee77837818a8ec18d0c16b27e0` |
| `predicted-tree` | `evidence/predicted-tree/results.json` | `d3508cad6339a5c32d0359868ab460d57d6550f45df4167878ff0164e8ae86fb` |

After an owner designation of an exact, all-green F, the linear execution,
E/reconciliation and receipt process of AGENTS §A.39 follows. This file
claims no execution, receipt or certification.

## The statement surface (frozen at F)

The module blocks below are the surfaces S1 compares: each module's code with
blank lines and proofs removed, every statement kept.

```lean
import OIBridge.ImplementationLocality
namespace OIBridge.PreservationInduction
open Matrix InterventionLocality OperationalAssembly ReferenceExtension MonoidalCompletion SpectatorBridge
abbrev CarrierConeFamily :=
  ∀ (S : Type) [Fintype S] [DecidableEq S], Set (Matrix S S ℂ)
structure AdditiveClosure (C : CarrierConeFamily) : Prop where
  zero_mem : ∀ (S : Type) [Fintype S] [DecidableEq S], (0 : Matrix S S ℂ) ∈ C S
  add_mem : ∀ (S : Type) [Fintype S] [DecidableEq S] (X Y : Matrix S S ℂ),
    X ∈ C S → Y ∈ C S → X + Y ∈ C S
def PreservesCarrier (C : CarrierConeFamily) (S : Type) [Fintype S] [DecidableEq S]
    (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  ∀ X, X ∈ C S → Φ X ∈ C S
structure PrimitivePreservation (𝓘 : ImplementationClass) (C : CarrierConeFamily) : Prop where
  op : ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ),
    𝓘 S K → Kᴴ * K = 1 → PreservesCarrier C S (conjChannel K)
  readout : ∀ (S T : Type) [Fintype S] [DecidableEq S] [Fintype T] [DecidableEq T]
    (m : ℕ) (e : T × Fin m ≃ S),
    (∀ k, 𝓘 S (Matrix.reindex e e (readProj T m k))) →
    ∀ k, PreservesCarrier C S (conjChannel (Matrix.reindex e e (readProj T m k)))
def UniformAttachPreservation (C : CarrierConeFamily) : Prop :=
  ∀ (S : Type) [Fintype S] [DecidableEq S] (m : ℕ), 0 < m →
    ∀ X, X ∈ C S → uniformAttach m X ∈ C (S × Fin m)
def AncillaDiscardPreservation (C : CarrierConeFamily) : Prop :=
  ∀ (S : Type) [Fintype S] [DecidableEq S] (m : ℕ), 0 < m →
    ∀ X, X ∈ C (S × Fin m) → ptraceAnc m X ∈ C S
theorem finite_sum_mem (C : CarrierConeFamily) (hC : AdditiveClosure C)
    {S : Type} [Fintype S] [DecidableEq S] {ι : Type} (s : Finset ι)
    (X : ι → Matrix S S ℂ) (hX : ∀ i ∈ s, X i ∈ C S) :
    (∑ i ∈ s, X i) ∈ C S :=
theorem instAvail_preserves (C : CarrierConeFamily) (hC : AdditiveClosure C)
    {𝓘 : ImplementationClass} (hPrim : PrimitivePreservation 𝓘 C)
    (hAttach : UniformAttachPreservation C) (hDiscard : AncillaDiscardPreservation C)
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail 𝓘 S O F) :
    ∀ a, PreservesCarrier C S (F a) :=
theorem instAvail_sum_preserves (C : CarrierConeFamily) (hC : AdditiveClosure C)
    {𝓘 : ImplementationClass} (hPrim : PrimitivePreservation 𝓘 C)
    (hAttach : UniformAttachPreservation C) (hDiscard : AncillaDiscardPreservation C)
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail 𝓘 S O F) :
    PreservesCarrier C S (∑ a, F a) :=
theorem instAvail_spectator_preserves (C : CarrierConeFamily) (hC : AdditiveClosure C)
    {𝓘 : ImplementationClass} (hPrim : PrimitivePreservation 𝓘 C)
    (hAttach : UniformAttachPreservation C) (hDiscard : AncillaDiscardPreservation C)
    (hc : ContextStable 𝓘) (hl : LabelInvariant 𝓘)
    (R : Type) [Fintype R] [DecidableEq R]
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail 𝓘 S O F) :
    ∀ a, PreservesCarrier C (R × S) (amplRefL R (F a)) :=
theorem instAvail_transport_preserves (C : CarrierConeFamily) (hC : AdditiveClosure C)
    {𝓘 : ImplementationClass} (hPrim : PrimitivePreservation 𝓘 C)
    (hAttach : UniformAttachPreservation C) (hDiscard : AncillaDiscardPreservation C)
    (hl : LabelInvariant 𝓘)
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail 𝓘 S O F)
    (S' : Type) [Fintype S'] [DecidableEq S'] (e : S ≃ S') :
    ∀ a, PreservesCarrier C S' (transport e (F a)) :=
#print axioms instAvail_preserves
#print axioms instAvail_sum_preserves
#print axioms instAvail_spectator_preserves
#print axioms instAvail_transport_preserves
end OIBridge.PreservationInduction
```

```lean
import OIBridge.PreservationInduction
import OIBridge.StructuralClosure
namespace OIBridge.PreservationInduction
open Matrix InterventionLocality OperationalAssembly MonoidalCompletion
open CompositeSoundness DimensionalCountermodel SubstratumInterface StructuralClosure
open scoped ComplexOrder
abbrev quantumCone : CarrierConeFamily := fun _ _ _ => {X | X.PosSemidef}
abbrev classicalCone : CarrierConeFamily := fun _ _ _ =>
  {X | X.PosSemidef ∧ ∃ d, X = Matrix.diagonal d}
abbrev classicalClass : ImplementationClass := substratumClass
theorem classicalCone_iff {S : Type} [Fintype S] [DecidableEq S]
    (X : Matrix S S ℂ) :
    X ∈ classicalCone S ↔ ∃ d, (∀ i, 0 ≤ d i) ∧ X = Matrix.diagonal d :=
theorem quantum_additive : AdditiveClosure quantumCone :=
theorem quantum_conj {S : Type} [Fintype S] [DecidableEq S] (K : Matrix S S ℂ) :
    PreservesCarrier quantumCone S (conjChannel K) :=
theorem quantum_primitive (𝓘 : ImplementationClass) :
    PrimitivePreservation 𝓘 quantumCone :=
def attachBlock {S : Type} [Fintype S] [DecidableEq S] (m : ℕ)
    (e : Fin m) (X : Matrix S S ℂ) : Matrix (S × Fin m) (S × Fin m) ℂ :=
  let P := Matrix.diagonal (fun p : S × Fin m => if p.2 = e then (1 : ℂ) else 0)
  P * X.submatrix Prod.fst Prod.fst * Pᴴ
theorem attachBlock_apply {S : Type} [Fintype S] [DecidableEq S] (m : ℕ)
    (e : Fin m) (X : Matrix S S ℂ) (p q : S × Fin m) :
    attachBlock m e X p q = if p.2 = e ∧ q.2 = e then X p.1 q.1 else 0 :=
theorem uniformAttach_eq_blocks {S : Type} [Fintype S] [DecidableEq S]
    (m : ℕ) (X : Matrix S S ℂ) :
    uniformAttach m X = (m : ℂ)⁻¹ • ∑ e : Fin m, attachBlock m e X :=
theorem quantum_attach : UniformAttachPreservation quantumCone :=
theorem ptraceAnc_eq_blocks {S : Type} [Fintype S] [DecidableEq S]
    (m : ℕ) (X : Matrix (S × Fin m) (S × Fin m) ℂ) :
    ptraceAnc m X = ∑ e : Fin m, X.submatrix (fun s => (s, e)) (fun s => (s, e)) :=
theorem quantum_discard : AncillaDiscardPreservation quantumCone :=
theorem quantum_instAvail {𝓘 : ImplementationClass}
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail 𝓘 S O F) :
    ∀ a, PreservesCarrier quantumCone S (F a) :=
theorem quantum_fullClass
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail fullClass S O F) :
    ∀ a, PreservesCarrier quantumCone S (F a) :=
theorem classical_additive : AdditiveClosure classicalCone :=
theorem classical_conj {S : Type} [Fintype S] [DecidableEq S]
    (K : Matrix S S ℂ) (hK : classicalClass S K) :
    PreservesCarrier classicalCone S (conjChannel K) :=
theorem classical_primitive : PrimitivePreservation classicalClass classicalCone :=
theorem classical_attach : UniformAttachPreservation classicalCone :=
theorem classical_discard : AncillaDiscardPreservation classicalCone :=
theorem classical_readProj {S T : Type} [Fintype S] [DecidableEq S]
    [Fintype T] [DecidableEq T] (m : ℕ) (e : T × Fin m ≃ S) (k : Fin m) :
    classicalClass S (Matrix.reindex e e (readProj T m k)) :=
theorem classical_instAvail
    {S : Type} [Fintype S] [DecidableEq S] {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : InstAvail classicalClass S O F) :
    ∀ a, PreservesCarrier classicalCone S (F a) :=
theorem classical_native_readout {S T : Type} [Fintype S] [DecidableEq S]
    [Fintype T] [DecidableEq T] (m : ℕ) (e : T × Fin m ≃ S) :
    ∀ k, PreservesCarrier classicalCone S
      (conjChannel (Matrix.reindex e e (readProj T m k))) :=
example : ContextStable classicalClass :=
example : LabelInvariant classicalClass :=
#print axioms quantum_instAvail
#print axioms classical_instAvail
#print axioms quantum_attach
#print axioms quantum_discard
#print axioms classical_readProj
#print axioms classical_native_readout
end OIBridge.PreservationInduction
```
