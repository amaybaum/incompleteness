# Reconstruction round PRESERVE-INDUCT-1 — conditional preservation by protocol induction: PREREGISTRATION (reconstructed draft for owner review)

**Status: native V3 control-plane draft for review; not an F candidate.**
The separate research design contains a compiled conditional core, compiled
all-carrier quantum/classical premise instances and two independent exact
implementations. Native adoption, the round's
governed probe, and its predicted execution tree remain unspecified. Only the
owner designates F after the concrete package and its exact-head checks are
ready under AGENTS §A.39. An instruction to proceed with design is not F.

**Recovery provenance.** The interrupted discussion reported this draft as
received, but no published branch, commit or PR containing it was found. This
document is a reconstruction from the owner's quoted item B (primitive
preservation extends to built operations), the existing research criteria,
and the exact kernel constructors at D. It is not represented as the original
Claude draft or as a recovered proof. The two other interrupted drafts were
already pushed and are preserved separately without rewriting them.

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
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
```

D: `b96662e6be4f537502c772db369ea32a35b213a8`, current main after #856. It is
provisional: under owner recommendation 4 it is finalized after #829 lands,
before F.
Before F, the control-plane delta contains only this preregistration and
review amendments. The execution edits listed above are prospective; none is
made by publishing this draft. Manuscripts, built artifacts, ROADMAP, adopted
kernel modules and other rounds' records are outside this round's edit scope.

## Question and status of the premises

Fix an independently specified family of unnormalized preparation cones C_S
on every finite matrix carrier, separately from an implementation class 𝓘.
Do explicit preservation assumptions for the primitive steps, readout,
uniform attachment and discard imply branchwise preservation for every
family built by `InstAvail`?

The expected proof is induction on the availability derivation. It is a
conditional soundness theorem, not a source for any preservation premise or
a new compatibility principle. Do not define C_S to be a reachable closure,
do not identify C_S with PSD in the general statement, and do not use the
validity theorem on PSD as though it identified an arbitrary physical cone.

The five constructors are exactly `op`, `readout`, `coarse`, `bind`, `discard`
in `ImplementationLocality.lean:268`. `ContextStable` (:359) and
`LabelInvariant` (:364) concern inventory membership. They do not say that
the independently given cone is preserved. The existing availability
theorems `instAvail_transport` (:644), `instAvail_spectator` (:789) and
`instAvail_withSpectator` (:820) are available for conditional corollaries;
none discharges state preservation by itself.

## Research-design definition and theorem budget

The core source is `PreservationInduction.lean` in the separate
`preservation-induction-design/` research directory, on the research branch
`research/preservation-induction-design-20261013` at
`468e0f79cabb01c215a252721ee65a1ad1301a2f`, which is not reachable from D and
is cited as provenance. Its five named theorems
compiled at `e684897da41b1c3d066b880194c9beb87a19b7ad`, workflow run
[38450187534](https://github.com/amaybaum/incompleteness/actions/runs/38450187534),
job 115478781754, every step `success`. The research record reads the four
headline/corollary axiom reports from that job's log as containing only
`propext`, `Classical.choice` and `Quot.sound`. The log is not yet retained,
and a step's success does not establish a report's contents. The reports enter
this round through the retained expected result pinned below where the log is
recoverable, and otherwise as attributed provenance with the gap recorded
(§A.42; owner recommendation 3).
This is research-design evidence, not native execution. The six core
definitions and their names are:

1. `CarrierConeFamily`: a set C_S of matrices for each finite carrier S,
   specified independently. Hermitian/cone structure can be exposed through
   separately named fields; the induction needs zero and finite-addition closure.
2. `AdditiveClosure`: exactly zero membership and addition closure for each
   C_S. Real scaling, Hermiticity, convexity, topological closedness and trace
   normalization are not used by the induction. No minimality is claimed.
3. `PreservesCarrier`: for an endomorphism Φ, X∈C_S implies Φ(X)∈C_S.
4. `PrimitivePreservation`: two distinct fields: each admitted isometric
   conjugation preserves C_S, and each branch of an admitted native register
   readout preserves C_S. The readout field cannot be folded into the
   isometry field: a nontrivial projection is not an isometry.
5. `UniformAttachPreservation`: for m>0, `uniformAttach m` sends C_S into
   C_(S×Fin m). It attaches I/m, not a pure ancilla.
6. `AncillaDiscardPreservation`: for m>0, `ptraceAnc m` sends the composite
   cone C_(S×Fin m) into C_S.
The headline's compiled interface, with implicit carrier/outcome instances
and implementation-class binder suppressed in this display, is:

```lean
theorem instAvail_preserves
    (C : CarrierConeFamily) (hC : AdditiveClosure C)
    (hPrim : PrimitivePreservation 𝓘 C)
    (hAttach : UniformAttachPreservation C)
    (hDiscard : AncillaDiscardPreservation C)
    (h : InstAvail 𝓘 S O F) :
    ∀ a, PreservesCarrier C S (F a)
```

The core also contains `finite_sum_mem`, `instAvail_sum_preserves`, summing
the unnormalized branches, and `instAvail_spectator_preserves`, obtained by applying the headline on the
joint carrier to `instAvail_spectator`. Its additional premises are exactly
the existing context/label hypotheses plus the same all-carrier preservation
premises. `instAvail_transport_preserves` proves preservation of the cone
assigned to the destination carrier. It does not identify that cone with the
reindexing of the original cone; such an identification would require a
separate explicit preparation-covariance premise outside this definition
budget. Class-level label invariance does not supply that premise.
No iff, minimal-premise result, reconstruction theorem or physical source is
part of the headline.

`ResearchInstances.lean` is the proposed companion adopted module's research
source. It adds four definitions/abbreviations: `quantumCone`,
`classicalCone`, `classicalClass` and `attachBlock`. Its nineteen named
theorems are `classicalCone_iff`, `quantum_additive`, `quantum_conj`,
`quantum_primitive`, `attachBlock_apply`, `uniformAttach_eq_blocks`,
`quantum_attach`, `ptraceAnc_eq_blocks`, `quantum_discard`,
`quantum_instAvail`, `quantum_fullClass`, `classical_additive`,
`classical_conj`, `classical_primitive`, `classical_attach`,
`classical_discard`, `classical_readProj`, `classical_instAvail` and
`classical_native_readout`. Two anonymous examples check the existing
classical inventory's context stability and label invariance. These
instance declarations compiled at
`febfe5e2668d3c000ec1d4ce7e4041f4feabd3c3`, workflow run
[38454439833](https://github.com/amaybaum/incompleteness/actions/runs/38454439833),
job 115493410133, every step `success`.
The instance source SHA256 is
`54b1451e1788fe6b71ca28eb81d2e9031abf1f78ee92d471bfddd73256044c65`.
The research record reads all six instance axiom reports and the four core
reports from that job's log as containing only `propext`, `Classical.choice`
and `Quot.sound`; they enter this round as the core reports do.
The run also replays both exact implementations and passes 303 legacy
records, 46 receipts and artifact placement, on its own tree, whose base is
`dee3b5ae`. The total proposed two-module surface
is ten definitions/abbreviations and twenty-four named theorems, plus those
two inventory examples; no additional physical source is imported.

## Induction route, compiled in research and unexecuted natively

| Constructor at D | Preservation step and checkpoint |
|---|---|
| `op` | Use the admitted-isometry field of `PrimitivePreservation` on the same carrier |
| `readout` | Use its separate readout field on every branch of the actual reindexed register projection |
| `coarse` | Every summand belongs to C_S by induction; finite-addition closure handles the fibre, including an empty fibre via zero |
| `bind` | Apply the first induction hypothesis to X and the outcome-dependent continuation hypothesis to its output |
| `discard` | Attach uniformly into C_(S×Fin m), use induction on that enlarged carrier, then partial trace back into C_S; retain m>0 |

`uniformAttach` is `OperationalAssembly.lean:492`, `ptraceAnc` :453 and
`discardWith` :515. The latter is partial trace composed with the operation
and preparation. `instAvail_trace` (`ImplementationLocality.lean:317`) is a
separate aggregate normalization theorem; trace preservation does not prove
membership in an arbitrary cone.

## Proposed controls and comparisons

The separate research record already supplies 107 primary and 43 independent
exact controls, seven named wrong-step guards, equal full sample-manifest
digests and byte-for-byte stdout replay. These certify the recorded finite
examples only. Their incorporation into a native governed probe, exact
decision-token interface and frozen controls is still a design obligation.

- **Quantum comparison:** the independently specified PSD family, with the
  ordinary isometric conjugations, register projections, uniform attachment
  and partial trace. Establish the premise instances and the resulting
  branchwise preservation without defining the general family as PSD.
  The new research Lean instance establishes the premises on every finite
  carrier for any inventory and explicitly specializes its theorem to
  `fullClass` at the pinned research-only build.
- **Classical comparison:** nonnegative diagonal cones with monomial
  implementations and coordinate readouts. Verify attachment, discard,
  coarse-graining and a genuinely outcome-dependent continuation. The Lean
  source uses PSD-and-diagonal matrices and the existing `substratumClass`
  monomial inventory, proving projector admission for reindexed register
  readouts. It does not claim every real classical stochastic instrument is
  available.
- **Primitive-operation countercontrol:** a diagonal positive state taken
  outside the diagonal cone by an available Hadamard conjugation. Availability
  and trace normalization alone do not fill the operation-preservation field.
- **Readout countercontrol:** the cone of nonnegative multiples of I is
  preserved by isometric conjugations, uniform attachment and partial trace,
  but a native coordinate readout sends I to a nonscalar projector. Check
  the other premise fields before using this as a load-bearing example.
- **Constructor coverage:** the exact instances must include every one of
  the five constructors, an empty coarse fibre, nested bind/discard, a fresh
  positive-size ancilla and nontrivial carrier relabelling. Empty outcome or
  carrier types must not make every positive example vacuous.
- **Conditional scope:** the research record of PR #820 (at `1d4606b2`, not
  reachable from D) reports exact, uniformly available depth-one failures for
  the two bridge cones K_B and K(Z_F), from two independent bridge
  implementations. They diagnose the missing premise source; do not claim
  that a family extending either cone satisfies all the
  primitive/attachment/discard assumptions without supplying that family.
  That record is provenance, not an adopted physical theorem, and this round
  does not rest a decision on it.
- **Mutations:** reject, at named failed checks, conflating readout with
  isometric steps, replacing unnormalized branch preservation by aggregate
  trace preservation, omitting the enlarged-carrier discard obligation,
  transporting inventory labels as though it transported the cone, and
  upgrading the result to a source from availability alone. These are
  native probe obligations; the research record's seven finite wrong-step
  guards are not mutations of the Lean proof and do not establish minimality.

Exact instance calculations need a separate checker or independently
implemented arithmetic path and output replay. Under owner recommendation 2
the probe may depend on SymPy, pinned explicitly to 1.14.0 and installed by
the workflow as `sympy==1.14.0`; the separate arithmetic implementation and
the byte replay are kept, and a standard-library-only probe is not required. Written universal claims
require kernel proofs or explicit written arguments; finite checks do not
upgrade them. Neither a syntactic mutation nor an example violating several
other retained hypotheses proves a premise necessary. The round does not
claim minimality of its premise package.

## Proposed decision rules and earned reading

Under owner recommendation 1, Q-CORE reads the Lean layer only and the exact
probe is read only by Q-EXACT:

- `PRESERVE-INDUCT-CORE-PROVED`: every required static control passes; the
  axiom report of the frozen universal branchwise statement
  (`instAvail_preserves`) and the reports of the Lean positive instances
  compile with only standard axioms, under the exact, explicit preservation
  assumptions. No probe output is read.
- `PRESERVE-INDUCT-COROLLARIES-PROVED`: Q-CORE's conditions, and the frozen
  sum/spectator/transport corollaries compile with only standard axioms and
  every extra premise displayed. No probe output is read.
- `PRESERVE-INDUCT-EXACT-CHECKED`: every required static control passes; the
  independent exact layer and its byte replay agree, all its frozen codes pass
  and every frozen mutation is rejected. No axiom report is read.
- Otherwise record the unresolved or halted result through the native
  lifecycle, with no successful token printed over a failed required control.

**Earned reading, only when all three cells are positive:** supplied primitive state-preservation,
attachment/discard and zero/additive-closure premises propagate to every finite
`InstAvail` derivation. This reduces a protocol-closure proof to a finite
list of constructor obligations. It does **not** establish a finite list
of concrete physical operators generating 𝓘; such a generation theorem
would be an additional, separate obligation.

**Non-inference rule:** the theorem sources no primitive preservation,
context stability, label/cone covariance, state-space identification, flow,
gate, test validity or quantum inclusion. It does not close K2 or P0 and is
not a substitute for the bridge audit's physical-source/disguise tests. It
supplies no part of the extension that the `P1 — F2` row lists as open
(ROADMAP :1124–1128 at D): the compatible state transformations named there
are assumed by the `op`, `readout`, attachment and discard premises for the
primitive steps, not supplied by the theorem.
With an excessive inventory such as fullClass, preservation assumptions can
already force quantum inclusion; that is an assumption audit, not a success
for sourcing compatibility. No manuscript or ROADMAP change is licensed here.

## Controls, verdict interface and invariants (draft, implemented by `controls.py`)

`controls.py` is drafted beside this file on a preparation branch. The control
plane at `F` holds only this file and `amendments/` (`S2`), so `controls.py`
enters with the first execution commit, at the blob pinned below.

**Stages.**
1. `S1`: `controls.py` at its pinned blob, the retained evidence pinned in
   the next section, and `F`'s exact-head run under `evidence/f-run/`.
2. The two modules and the probe at their pinned blobs; the workflow, import
   and census edits.
3. The result note, candidate `E`.

**Static controls.** `controls.py check E --freeze F` runs all thirteen at
`E`. With `--stage S1` it runs C1, C2 (for `controls.py` only), P, R, G and T
at the first execution commit. Any other stage or argument is refused.

| code | measures |
| --- | --- |
| C1 | the preregistration at `E` is the one at `F`, and names this `D`, the round declaration, and the citation of `65b85147` with the link to #831 that the drafting decision requires |
| C2 | the four frozen execution blobs below at `E` (at `S1`, `controls.py`'s); no pin pending |
| S1 | each module equals its block in the frozen statement-surface section: imports, namespace and `open` lines, the declarations in the order named in this file with their statements (a definition's whole text), the two examples, the prints; no `sorry`, `admit`, `native_decide`, `axiom`, `implemented_by` or `extern` |
| S2 | the landed objects below at their lines, with `D`'s blobs at `E` |
| S3 | the core module mentions no PSD, Hermiticity, convexity, closedness, trace, reachability or iff; `AdditiveClosure` has exactly the fields `zero_mem` and `add_mem`, and `PrimitivePreservation` exactly `op` and `readout`; `instAvail_preserves` is one induction on the derivation with the arms `op`, `readout`, `coarse`, `bind`, `discard` in that order; the sum, spectator and transport corollaries apply `instAvail_preserves`, the latter two to `instAvail_spectator` and `instAvail_transport`; no research import or namespace remains; no preparation family is defined through `InstAvail` |
| S4 | both module headers and the result note are present, without the excluded phrases frozen in `controls.py` (`PHRASES`) |
| W | `verify.yml` at `E` is `D`'s with the frozen splices, each anchored once; when the probe spec names SymPy, the splices install it as `sympy==1.14.0` and name it in no other form |
| I | `OIBridge.lean` at `E` is `D`'s with `import OIBridge.PreservationInduction` and `import OIBridge.PreservationInductionInstances` directly after its last import line |
| J | the census at `E` is `D`'s with the frozen families appended |
| P | the three retention rows of the next section: each historical row a digest or a recorded gap, the predicted-tree row a digest; every digest row's file present at `E` with that digest, and a file retained on main outside the record directory present at `D` and unchanged at `E`; no row pending |
| R | the record directory holds exactly this file, `controls.py`, the record-relative files the digest rows name, a non-empty `evidence/f-run/`, `amendments/` if present, and at `E` the result note |
| G | the governed-path block equals the eight entries above; every change from `D` is authorized under `S7` (longest governing entry, status letter in its operations); the receipt is absent; the legacy manifest is present and unchanged |
| T | `delta(D, F)` is this file and `amendments/`, drafted by single-parent commits from `D`, none of them #831's `5f614d60` or `65b85147`; the execution after `F` is non-empty and linear, and `F` is an ancestor of `E` |

**Parameters not yet fixed.** `controls.py` carries four as `None`; while any
is `None`, the controls that depend on it fail. They are `NS`, the adopted
namespace (item 2; S1); `SPLICES`, the workflow edits (item 5; W); `FAMILIES`,
the census families (item 3; J); and `PROBE_SPEC`, the probe's codes, the
separate arithmetic implementation's codes, check count, mutations, final
line, the sha256 of its standard output and its SymPy pin (item 4; Q-EXACT,
and W for the pin). The statement-surface
section (item 2), the frozen blobs below and the retained-evidence pins are
pending in this file. Fixing any of them changes `controls.py` or this file
before `F`.

**Prints**, as in the research design. Core: `instAvail_preserves`,
`instAvail_sum_preserves`, `instAvail_spectator_preserves`,
`instAvail_transport_preserves`. Instances: `quantum_instAvail`,
`classical_instAvail`, `quantum_attach`, `quantum_discard`,
`classical_readProj`, `classical_native_readout`.

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
the result note, and the round halts.

| path | blob |
| --- | --- |
| `verification/programmes/oi-qm/reconstruction/round-preserve-induct-1/controls.py` | pending |
| `verification/lean-mathlib/OIBridge/PreservationInduction.lean` | pending |
| `verification/lean-mathlib/OIBridge/PreservationInductionInstances.lean` | pending |
| `verification/lean/preserve_induct1_probe.py` | pending |

**Verdict.** `controls.py verdict E --freeze F --axioms <E's exact-head bridge
log>` prints one token per cell:

| cell | positive | otherwise | rule as implemented |
| --- | --- | --- | --- |
| Q-CORE | `PRESERVE-INDUCT-CORE-PROVED` | `PRESERVE-INDUCT-CORE-NOT-ESTABLISHED` | the static controls pass; the report of the universal theorem `instAvail_preserves` and the six Lean positive-instance reports lie within `propext`, `Classical.choice` and `Quot.sound`, and the log carries no `sorryAx`, `Lean.ofReduceBool` or `Lean.trustCompiler`; no probe output is read |
| Q-COR | `PRESERVE-INDUCT-COROLLARIES-PROVED` | `PRESERVE-INDUCT-COROLLARIES-NOT-ESTABLISHED` | Q-CORE's conditions, measured again, and the three corollary reports; no probe output is read |
| Q-EXACT | `PRESERVE-INDUCT-EXACT-CHECKED` | `PRESERVE-INDUCT-EXACT-NOT-ESTABLISHED` | the probe blob at `E`, run with `python3 -I -B` and `--self-test`, prints every frozen code (those of the separate arithmetic implementation included), no `FAIL`, the frozen check count with no failures, every frozen mutation rejected, the frozen final line and, where the frozen spec names it, `SYMPY 1.14.0`; its standard output has the frozen sha256 (the byte replay), and its standard error is empty |

Q-CORE and Q-COR read no probe output, and Q-EXACT reads no axiom report
(owner recommendation 1); the static controls gate all three. `verdict` also
prints whether the full earned reading is available: only when all three cells
are positive.

Every positive token is gated on the static controls. If any of the thirteen
fails or is not reported, `verdict` prints the failed controls, runs no probe
and reads no axiom report. Every cell then prints its `NOT-ESTABLISHED`
token, the round prints `PRESERVE-INDUCT-1-NOT-READ`, and the exit status is
1. Otherwise each cell prints by its own rule, reading no other cell's
outcome, and the round prints `PRESERVE-INDUCT-1-READ`. `check` records each
control's outcome only when that control runs; a control that never recorded
one is absent and counts as failed, in `verdict` and in `check`'s exit.

**Self-test.** `controls.py --self-test`:
- checks this file's tables against `controls.py` and resolves the landed
  objects in its tree;
- runs mutation controls on S1 and S3 over a synthetic fixture of the two
  modules;
- drives `verdict` with injected static results: each control failing alone,
  one unreported, one non-bool, the all-clean case, and the cells'
  separation (a failing probe leaves Q-CORE and Q-COR positive; a dirty
  headline or instance report leaves Q-EXACT positive);
- drives `verdict` end to end through the real `check()` on an in-memory
  synthetic `D`, `F` and `E`: unmutated; with each control's record call
  removed from the source; with each control's inputs absent; in the shipped
  state, with the parameters pending; and through `main`, which refuses unknown
  stages and arguments.

In every failing case `verdict` must return failure, name the control, print
no positive token and never run the probe. The self-test freezes its own count
of self-checks. Its fixture is synthetic and never compiled, and is not
evidence for any theorem.

**Invariants and their checkpoints (§A.41).**

| invariant (where this file asserts it) | checkpoint |
| --- | --- |
| before `F` the control-plane delta is this file and its amendments (the paragraph under the governed paths) | T at `S1` and `E`; `G9` under `v3_verifier --verify-round Q` |
| the drafting chain is a new linear branch from the finalized `D` that cites `65b85147` and links #831, and imports none of #831's commits (owner decision of 2026-10-17) | C1 (the citation and link); T (single-parent commits from `D`, neither `5f614d60` nor `65b85147` among them); reviewers check that #831 is closed as superseded once the replacement exists |
| execution starts from the frozen control plane; `controls.py`, the modules and the probe are the frozen ones | C1; C2 at `S1` and `E` |
| no manuscript, built artifact, ROADMAP, adopted kernel module or other round's record changes (the paragraph under the governed paths; non-inference rule) | G at `S1` and `E`; S2 |
| the preparation family is specified independently: not a reachable closure, not PSD in the general statement (Question) | S3 |
| the induction uses only zero and addition closure, and readout is a field separate from the isometric step (budget items 2 and 4) | S1; S3 |
| the proof is one induction over the five constructors (Induction route) | S3; the kernel build at `E` |
| the corollaries' extra premises are exactly those displayed, and transport preserves the destination carrier's cone without identifying it with a reindexing (budget) | S1; S3 |
| the research import paths and namespace are replaced without changing the statements (item 2) | S1; S3 |
| the root import and census entries (item 3) | I; J; the release gate's `lean-manuscript` step at `E` |
| every declaration elaborates within `propext`, `Classical.choice` and `Quot.sound`, with no `sorryAx` | the exact-head run at `E`, every job `success`; the ten reports read by `verdict --axioms` |
| the exact layer covers every constructor, an empty coarse fibre, nested bind/discard, a fresh positive-size ancilla and a nontrivial relabelling, without vacuous positives, and rejects the frozen mutations (Proposed controls) | the probe's frozen codes and mutations (`PROBE_SPEC`, item 4), read by Q-EXACT; the probe shard green at `E` |
| a separate arithmetic implementation and a byte replay are kept; SymPy, if used, is pinned to 1.14.0 (Proposed controls; owner recommendation 2) | Q-EXACT (the separate implementation's codes, the frozen stdout sha256, the `SYMPY 1.14.0` line); W (the `sympy==1.14.0` install) |
| Q-CORE reads the static controls, the universal theorem's report and the positive-instance reports only; Q-EXACT alone reads the probe (decision rules; owner recommendation 1) | `controls.py --self-test`: the `verdict` regression's separation cases (a failing probe leaves Q-CORE and Q-COR positive; a dirty instance or headline report leaves Q-EXACT positive) |
| the full earned reading only when all three cells are positive (earned reading; owner recommendation 1) | the earned-reading line printed by `verdict`; owner review of the result note |
| the workflow runs the probe and `controls.py --self-test` (item 5) | W; the exact-head run at `E` |
| no positive token over a failed or unreported required control (decision rules) | `controls.py --self-test` in the probe shard: the `verdict` regression and the end-to-end cases |
| the result note asserts no source, closure or implication beyond the earned reading (non-inference rule) | S4; owner review of the result note |
| the design evidence is retained by the first execution commit and pinned before `F`; a historical build whose log is unrecoverable is recorded as a gap and stays attributed provenance; the predicted-tree run establishes results for its own tree only (§A.42 items 2 and 4; owner recommendation 3) | P and R at `S1` and `E` (a historical row may name an expected result retained on main before `D`, present at `D` and unchanged at `E`); reviewers check that each pin resolves to retained content, that each gap names what is missing, and that no claim about the historical builds rests on the predicted-tree run |
| `F`'s exact-head run is retained by the first execution commit (§A.42 item 2) | R at `S1` (a non-empty `evidence/f-run/`); reviewers check that it names `F`'s run, job and digest |
| `E`'s exact-head run reaches `main` through its own evidence-retention pull request before reconciliation, and the receipt names each retained file's digest (§A.42 item 2) | reviewer check of that pull request and of the receipt's candidate entry for `E`; `evidence-retention` at `Q` |
| the native receipt holds; the legacy records are untouched | `v3_verifier --verify-round Q`; `legacy_records_check.py` at every stage commit and at `Q`; G |

## Owner recommendations (not decisions)

Recorded as recommendations. None is a decision, a designation or an
execution step.

1. Q-CORE requires the static controls, the universal theorem's report and the
   Lean positive-instance reports; the exact probe stays in Q-EXACT. The full
   earned reading requires every advertised cell to pass.
2. The probe may depend on SymPy 1.14.0, pinned explicitly, with the workflow
   installing `sympy==1.14.0`. The separate arithmetic implementation and the
   byte replay are kept; a standard-library-only probe is not required.
3. The historical builds (`e684897d`, `febfe5e2`; runs 38450187534 and
   38454439833) are retained where recoverable. Where they are not, the gap is
   recorded and the old builds stay attributed provenance. The new
   predicted-tree run establishes results only for its own tree and cannot
   verify the historical logs retroactively.
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

The branch and the pull request are created only after #829 lands and D is
finalized.

Still open before `F`, and not established by the self-test (which checks the
draft checker's own tests): the adopted namespace and module bytes, the two
statement surfaces, the probe specification, the workflow splices, the census
entries, the frozen blobs and the retention rows.

## Design and freeze boundary

Before F, all of the following remain explicit obligations:

1. Review the compiled research core and positive-instance source, retaining
   the core and instance axiom reports and exact source hashes. Any subsequent
   proof edit needs a fresh design compile before it is pinned.
2. Pin the adopted-module byte contents. The prospective core and companion
   paths are listed above; migration must replace temporary research import
   paths and settle the namespace without changing or silently strengthening
   the statements. The current research namespace is
   `OIBridge.PreservationInductionDesign`.
3. Specify the exact root-import and census/registry entries for both
   modules under §A.35, classifying them as conditional preservation and
   quantum/classical comparisons rather than a physical compatibility source.
4. Implement and pin the governed native probe and independent controls,
   using the measured research scripts as design evidence rather than
   claiming they already are the round's execution or verdict protocol.
5. Specify the exact `.github/workflows/verify.yml` edits and how the
   prospective probe checks the bounded execution tree against the actual
   PR head. The research-only workflow is not a permanent native CI job.
6. Generate and check the exact predicted executable tree, including both
   modules, imports, registry entries, probe and workflow. Pin the complete
   design files, controls and parameters in this PR, then run its exact-head
   required checks. No predicted execution commit is supplied by this update.
7. Retain the evidence of the two historical design builds where it is
   recoverable, record each unrecoverable part as a gap, and retain the
   predicted-tree run's expected result; pin the table below. The
   predicted-tree run establishes results only for its own tree and does not
   verify the historical logs retroactively.

**Retained evidence (§A.42).** Each file is a structured expected result in the
form of §A.42 item 1: build success, the `#print axioms` reports, the exact
replays' output lines and the failure markers. Each names its commit, run, job
and recipe, and the digest of the log it is read from. The files are committed
to the record directory by the first execution commit, outside `amendments/`,
together with `F`'s exact-head run under `evidence/f-run/`, and pinned here by
sha256 before `F`. The owner asked for the two historical build logs to be
retained before `F` rather than at it; that is done by the separate CI-evidence
retention work, whose expected results a historical row may name directly: its
file column then gives the repository path of the retained expected result
(`verification/…`, outside the record directory), which must be present at `D`
and unchanged at `E`, and its sha256 column that file's digest. Any other
retained file is record-relative (`evidence/…`). A historical row whose log
cannot be recovered names `none` as its file and carries `gap:` and what is
missing instead of a digest; the claims resting on that build then stay
attributed provenance, the research record's reading. The available
API client returns at most the last 5000 lines of a job log, and job-log
downloads are refused in this environment, so a retained copy says which lines
it covers and claims nothing outside them. At drafting, that client reported
3256 lines for job 115478781754 and 3692 for job 115493410133; this is a
measurement of availability, not retention. The predicted-tree row must carry
a digest. `F` is not designated with a pending row.

| row | file | sha256 |
| --- | --- | --- |
| `core-build-38450187534` | pending (the expected result of the core design build at `e684897d`, job 115478781754) | pending (a digest, or a recorded gap) |
| `instance-build-38454439833` | pending (the expected result of the instance design build at `febfe5e2`, job 115493410133) | pending (a digest, or a recorded gap) |
| `predicted-tree` | pending (the expected result of the design run on the predicted execution tree, item 6) | pending (a digest is required) |

The research core and exact layer are available, but these remaining edits
are not yet a concrete, freeze-ready execution package. D is
`b96662e6be4f537502c772db369ea32a35b213a8`.

After an owner designation of exact, all-green F, follow the linear execution,
E/reconciliation and receipt process in AGENTS §A.39. No older native control
plane is thawed, and no execution, receipt or certification is claimed by
this recovery draft.
