# Reconstruction round PRESERVE-INDUCT-1 — conditional preservation by protocol induction: PREREGISTRATION (control-plane draft for owner review)

**Status: native V3 control-plane draft for review; not an F candidate.**
This text is the design candidate for the replacement drafting pull request
that the owner decided on 2026-10-17 (below). The linked design branch
`dev/preserve-induct-831-20261018` carries it together with the predicted
execution files: the two adopted modules, the probe and its independent check,
the root import, the census families and the workflow edits. The adopted
modules are unbuilt at their adopted paths. Only the owner designates F, after
the predicted-tree run is retained and pinned and F's exact-head checks pass
(AGENTS §A.39). An instruction to proceed with design is not F.

**Provenance.** #831 (https://github.com/amaybaum/incompleteness/pull/831)
reconstructed this round's draft from the owner's quoted item B (primitive
preservation extends to built operations), the research criteria and the
kernel constructors. Its head is `65b85147f85aa01770e0e60551152bc5f1d9ef29`.
The branch `wip/preserve-induct-1-controls` drafted `controls.py` and the
control section. Neither chain's commits are imported into this draft.

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

D: `501331f58e856019173d7246a8c4de7d4aec752d`, main after #860. It is provisional: under
owner recommendation 4 it is finalized after #829 lands, before F. D must
carry the evidence archive's research-build entries, which reached main with
#860: the historical retention rows below name them, and the release gate's
`evidence-retention` step judges this record's citations of them at F and at
every later commit. Before F, the control-plane delta contains only this
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
[38450187534](https://github.com/amaybaum/incompleteness/actions/runs/38450187534),
job 115478781754, every step `success`. The archive's expected result of
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
[38454439833](https://github.com/amaybaum/incompleteness/actions/runs/38454439833),
job 115493410133, every step `success`, and is pinned as the `instance-build`
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
  strengthened, so the first build at the adopted paths tests the same proofs
  in the same environment (the lakefile sets no Lean options).
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

- **Probe codes** (120 checks): `CONSTRUCTORS`, `ISOMETRY`, `READOUT`, `ATTACH`, `AGGREGATE`, `EMPTY`, `NONVACUOUS`, `BRANCH-PSD`, `BRANCH-DIAG`, `RELABEL`, `COUNTER-HADAMARD`, `COUNTER-READOUT`, `COUNTER-DISCARD`, `MANIFEST`.
- **Independent codes** (47 checks): `I-TRACE`, `I-EMPTY`, `I-PSD`, `I-DIAG`, `I-HADAMARD`, `I-READOUT`, `I-DISCARD`, `I-SEPARATE`, `I-MANIFEST`.
- **Mutations.** Each named wrong step is applied to an evaluation; it is
  rejected when its named check holds on the faithful step and fails on the
  mutated one: `readout-as-isometry: op-isometry`, `aggregate-for-branch: branch-cone`, `discard-enlarged-premise-dropped: branch-cone`, `labels-as-cone-transport: branch-cone`, `availability-as-source: branch-cone`, `pure-for-uniform: attach-cone`, `empty-fibre-dropped: empty-fibre`, `discard-omits-sum: aggregate-trace`.

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
  manifest digest, replay byte for byte and reject every frozen mutation. No
  axiom report is read.
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
are assumed by the `op`, `readout`, attachment and discard premises. With an
excessive inventory such as fullClass, preservation assumptions can already
force quantum inclusion; that is an assumption audit, not a success for
sourcing compatibility. No manuscript or ROADMAP change is licensed here.

## Controls, verdict interface and invariants

`controls.py` is on the design branch. The control plane at `F` holds only
this file and `amendments/` (`S2`), so `controls.py` enters with the first
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

| code | measures |
| --- | --- |
| C1 | the preregistration at `E` is the one at `F`, and names this `D`, the round declaration, and the citation of `65b85147` with the link to #831 |
| C2 | the five frozen execution blobs below at `E` (at `S1`, `controls.py`'s); no pin pending |
| S1 | each module equals its block in the frozen statement-surface section: imports, namespace and `open` lines, the declarations in order with their statements (a definition's whole text), the two examples, the prints; no `sorry`, `admit`, `native_decide`, `axiom`, `implemented_by` or `extern` |
| S2 | the landed objects below at their lines, with `D`'s blobs at `E` |
| S3 | the core module mentions no PSD, Hermiticity, convexity, closedness, trace, reachability or iff; `AdditiveClosure` has exactly the fields `zero_mem` and `add_mem`, and `PrimitivePreservation` exactly `op` and `readout`; `instAvail_preserves` is one induction on the derivation with the arms `op`, `readout`, `coarse`, `bind`, `discard` in that order; the corollaries apply `instAvail_preserves`, the latter two to `instAvail_spectator` and `instAvail_transport`; no research import or namespace remains; no preparation family is defined through `InstAvail` |
| S4 | both module headers and the result note are present, without the excluded phrases frozen in `controls.py` (`PHRASES`) |
| W | `verify.yml` at `E` is `D`'s with the frozen splices (`SPLICES`), each anchored once; they install SymPy as `sympy==1.14.0` and name it in no other form |
| I | `OIBridge.lean` at `E` is `D`'s with the two import lines directly after its last import line |
| J | the census at `E` is `D`'s with the frozen families appended |
| P | the three retention rows: a historical row an archived expected result, a digest or a recorded gap, the predicted-tree row a digest; every digest row's file present at `E` with that digest, and a file outside the record directory present at `D` and unchanged at `E`; no row pending |
| R | the record directory holds exactly this file, `controls.py`, the record-relative files the digest rows name, a non-empty `evidence/f-run/`, `amendments/` if present, and at `E` the result note |
| A | the archive's research-build entries and retained commits that await this round name this file; each run is cited free-standing on exactly its recorded line and on no other line, with its full head beside it and no other head; no other file outside the archive names the run; the recorded lines are 69 and 127 |
| G | the governed-path block equals the nine entries above; every change from `D` is authorized under `S7`; the receipt is absent; the legacy manifest is unchanged |
| T | `delta(D, F)` is this file and `amendments/`, drafted by single-parent commits from `D`, none of them #831's `5f614d60` or `65b85147`; the execution after `F` is non-empty and linear, and `F` is an ancestor of `E` |

**Design parameters.** `controls.py` sets `NS`, `SPLICES` (six splices: the
probe shard job before the Act 42 comment, its entry in the aggregate's
`needs`, environment, echo and test lines, and a final bridge-job step that
prints the ten axiom reports again with `lake env lean` so the verdict can
read them from the log's tail), `FAMILIES` and `PROBE_SPEC` (the codes, counts,
final lines and stdout digests of both scripts, the eight mutations, the
manifest digest and the SymPy pin). With any of them `None` the controls that
depend on it fail closed.

**Prints**, as in the research design. Core: `instAvail_preserves`,
`instAvail_sum_preserves`, `instAvail_spectator_preserves`,
`instAvail_transport_preserves`. Instances: `quantum_instAvail`,
`classical_instAvail`, `quantum_attach`, `quantum_discard`,
`classical_readProj`, `classical_native_readout`. No printed name contains a
prime, so the archive's extractor reads every report of E's run.

**S2's landed objects at D.**

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

**Frozen execution blobs.** C2 checks these. A different blob at `S1` or at
`E` is a deviation from the frozen design, not a repair: it is recorded in
the result note, and the round halts. The module blobs are pinned before
their first build at the adopted paths; if the predicted-tree build requires
an edit, the edit and its pins change here before `F`.

| path | blob |
| --- | --- |
| `verification/programmes/oi-qm/reconstruction/round-preserve-induct-1/controls.py` | `01501ffed7187e87c22d3420d99c8d67707d4590` |
| `verification/lean-mathlib/OIBridge/PreservationInduction.lean` | `a40464f53afb97c7489210b78bee485f0d65fbb2` |
| `verification/lean-mathlib/OIBridge/PreservationInductionInstances.lean` | `13b786c7bae8944fda62e50b13e80ca1574b9a0e` |
| `verification/lean/preserve_induct1_probe.py` | `96eee55baaf5ea1f5d3297a12fd70ede878c8b7c` |
| `verification/lean/preserve_induct1_indep_check.py` | `b2e3f1782f475d6526e5084ba0037d6cabb2eead` |

**Verdict.** `controls.py verdict E --freeze F --axioms <E's exact-head bridge
log>` prints one token per cell:

| cell | positive | otherwise | rule as implemented |
| --- | --- | --- | --- |
| Q-CORE | `PRESERVE-INDUCT-CORE-PROVED` | `PRESERVE-INDUCT-CORE-NOT-ESTABLISHED` | the static controls pass; the report of `instAvail_preserves` and the six Lean positive-instance reports lie within `propext`, `Classical.choice` and `Quot.sound`, and the log carries no `sorryAx`, `Lean.ofReduceBool` or `Lean.trustCompiler`; no probe output is read |
| Q-COR | `PRESERVE-INDUCT-COROLLARIES-PROVED` | `PRESERVE-INDUCT-COROLLARIES-NOT-ESTABLISHED` | Q-CORE's conditions, measured again, and the three corollary reports |
| Q-EXACT | `PRESERVE-INDUCT-EXACT-CHECKED` | `PRESERVE-INDUCT-EXACT-NOT-ESTABLISHED` | the probe and the independent check at their blobs at `E`, each run alone with `python3 -I -B`: exit 0, empty standard error, no `FAIL`, every frozen code, the frozen check count with no failures, the frozen final line and stdout sha256 (the byte replay); the probe's `SYMPY 1.14.0` line and every frozen mutation `REJECTED` with none accepted; both print the frozen manifest digest |

Q-CORE and Q-COR read no probe output, and Q-EXACT reads no axiom report;
the static controls gate all three. If any of the fourteen fails or is not
reported, `verdict` prints the failed controls, runs no probe and reads no
axiom report; every cell prints its `NOT-ESTABLISHED` token, the round prints
`PRESERVE-INDUCT-1-NOT-READ`, and the exit status is 1. Otherwise each cell
prints by its own rule and the round prints `PRESERVE-INDUCT-1-READ`. The
full earned reading is printed only when all three cells are positive.

**Self-test.** `controls.py --self-test` checks this file's tables against
`controls.py`, resolves the landed objects and checks control A's rule on
this file against the archive in its tree (or, once the archive has promoted
the citations, that it maps this file); runs mutation controls on S1 and S3
over a synthetic fixture; drives `verdict` with injected static results and
the cells' separation; and drives `verdict` end to end through the real
`check()` on an in-memory `D`, `F` and `E`, unmutated, with each control's
record call removed and with each control's inputs absent. In every failing
case `verdict` must fail, name the control, print no positive token and never
run the probe. The fixture is synthetic, never compiled and no evidence for
any theorem.

**Invariants and their checkpoints (§A.41).**

| invariant (where this file asserts it) | checkpoint |
| --- | --- |
| before `F` the control-plane delta is this file and its amendments | T at `S1` and `E`; `G9` under `v3_verifier --verify-round Q` |
| the drafting chain is a new linear branch from the finalized `D` that cites `65b85147` and links #831 and imports none of #831's commits (owner decision of 2026-10-17) | C1; T; reviewers check that #831 is closed as superseded once the replacement exists |
| the archive's pending citations of this record stay as recorded: each run on its recorded line only, its head beside it, no other file naming it (D; R13 and O10) | A at `S1` and `E`; the release gate's `evidence-retention` step at `F`, `E` and `Q`; the self-test's live check |
| execution starts from the frozen control plane; `controls.py`, the modules, the probe and the independent check are the frozen ones | C1; C2 at `S1` and `E` |
| no manuscript, built artifact, ROADMAP, other kernel module, archive file or other round's record changes | G at `S1` and `E`; S2 |
| the preparation family is specified independently: not a reachable closure, not PSD in the general statement | S3 |
| the induction uses only zero and addition closure, and readout is a field separate from the isometric step | S1; S3 |
| the proof is one induction over the five constructors | S3; the kernel build at `E` |
| the corollaries' extra premises are exactly those displayed, and transport preserves the destination carrier's cone without identifying it with a reindexing | S1; S3 |
| the adoption changes only the namespace, the research import, the headers and one comment | S1 against the frozen surface; S3 (no research mark); the design branch's diff against the research sources |
| the root import and census entries | I; J; the release gate's `lean-manuscript` step at `E` |
| every declaration elaborates within `propext`, `Classical.choice` and `Quot.sound`, with no `sorryAx` | the exact-head run at `E`, every job `success`; the ten reports read by `verdict --axioms` from the bridge job's final step |
| the exact layer covers every constructor, an empty coarse fibre, nested bind and discard, positive-size ancillas and a nontrivial relabelling, without vacuous positives, and rejects the frozen mutations | the probe's frozen codes and mutations, read by Q-EXACT; the probe shard green at `E` |
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
4. `controls.py` stays on the preparation branch until execution. D is
   finalized after #829 lands.

## Owner decision (2026-10-17): the replacement drafting pull request

- It is a new linear branch from the finalized D, carrying the revised
  control-plane text (this file and `amendments/`).
- It cites #831's head `65b85147f85aa01770e0e60551152bc5f1d9ef29` and links
  #831 (https://github.com/amaybaum/incompleteness/pull/831).
- #831 stays open until the replacement pull request exists, and is then
  closed as superseded.
- #831's commits (`5f614d60`, `65b85147`) are not imported into the new
  drafting chain.

## Design and freeze boundary

Done on the design branch, unbuilt: the adopted module bytes and namespace
(item 2), the root import and census families (item 3), the probe, the
independent check and `controls.py` with their pins (item 4), and the workflow
splices (item 5). Remaining before F:

1. Review the adopted modules against the research sources.
2. Build the predicted execution tree: the design branch's tree with the
   preregistration and `controls.py`, less the result note, in every event
   mode used to certify `E`. Any proof edit it needs changes the module bytes
   and their pins here.
3. Retain that run's expected result and pin the `predicted-tree` row.
4. Finalize D after #829 lands; re-check the splice anchors, the import and
   census bases and the landed-object lines at the final D.
5. Open the replacement drafting pull request, run F's exact-head checks and
   ask the owner for the F designation.

**Retained evidence (§A.42).** Each row is a structured expected result in the
form of §A.42 item 1. A historical row names `archive` when the expected
result is the one the evidence archive holds for that build: `controls.py`
finds it by its digest among the archive entries whose pending citation awaits
this file on the row's line (69 for `core-build`, 127 for `instance-build`),
and requires it present at `D` and unchanged at `E`. The predicted-tree row
names a record-relative file committed by the first execution commit, or an
expected result retained on main before `D`, and carries a digest. `F` is not
designated with a pending row.

| row | file | sha256 |
| --- | --- | --- |
| `core-build` | archive | `8dfbeb2b950d3474e239c3398cd3cb76fc75aae22ef1b7c8942729883f41bba1` |
| `instance-build` | archive | `647c69f0cadc7dd89e77d0b189eeabeab28e63ee77837818a8ec18d0c16b27e0` |
| `predicted-tree` | pending (the expected result of the predicted-tree run, item 2) | pending (a digest is required) |

After an owner designation of an exact, all-green F, the linear execution,
E/reconciliation and receipt process of AGENTS §A.39 follows. No execution,
receipt or certification is claimed by this draft.

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
