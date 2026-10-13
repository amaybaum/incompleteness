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

D: `dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4`, current main after #818.
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
`preservation-induction-design/` research directory. Its five named theorems
compiled at `e684897da41b1c3d066b880194c9beb87a19b7ad`, workflow run
[38450187534](https://github.com/amaybaum/incompleteness/actions/runs/38450187534).
The four headline/corollary axiom reports contain only `propext`,
`Classical.choice` and `Quot.sound`. This is research-design evidence, not
native execution. The six core definitions and their names are:

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
[38454439833](https://github.com/amaybaum/incompleteness/actions/runs/38454439833).
The instance source SHA256 is
`54b1451e1788fe6b71ca28eb81d2e9031abf1f78ee92d471bfddd73256044c65`.
All six instance axiom reports contain exactly `propext`, `Classical.choice`
and `Quot.sound`; the four core reports retain the same standard axioms.
The run also replays both exact implementations and passes 303 legacy
records, 46 receipts and artifact placement. The total proposed two-module surface
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
- **Conditional scope:** the two bridge cones K_B and K(Z_F) have their exact
  uniformly available depth-one failures. They diagnose the missing premise
  source; do not claim that a family extending either cone satisfies all the
  primitive/attachment/discard assumptions without supplying that family.
  References are the research record in PR #820 at `1d4606b2` and its
  two independent bridge implementations, not an adopted physical theorem.
- **Mutations:** reject, at named failed checks, conflating readout with
  isometric steps, replacing unnormalized branch preservation by aggregate
  trace preservation, omitting the enlarged-carrier discard obligation,
  transporting inventory labels as though it transported the cone, and
  upgrading the result to a source from availability alone. These are
  native probe obligations; the research record's seven finite wrong-step
  guards are not mutations of the Lean proof and do not establish minimality.

Exact instance calculations need a separate checker or independently
implemented arithmetic path and output replay. Written universal claims
require kernel proofs or explicit written arguments; finite checks do not
upgrade them. Neither a syntactic mutation nor an example violating several
other retained hypotheses proves a premise necessary. The round does not
claim minimality of its premise package.

## Proposed decision rules and earned reading

- `PRESERVE-INDUCT-CORE-PROVED`: the frozen universal branchwise statement
  compiles with only standard axioms and the exact, explicit preservation
  assumptions; all required constructor and positive controls are green.
- `PRESERVE-INDUCT-COROLLARIES-PROVED`: the frozen sum/spectator/transport
  corollaries compile with every extra premise displayed and the same controls.
- `PRESERVE-INDUCT-EXACT-CHECKED`: the independent exact layer and its replay
  agree, all required controls are green and every frozen mutation is rejected.
- Otherwise record the unresolved or halted result through the native
  lifecycle, with no successful token printed over a failed required control.

**Earned reading if proved:** supplied primitive state-preservation,
attachment/discard and zero/additive-closure premises propagate to every finite
`InstAvail` derivation. This reduces a protocol-closure proof to a finite
list of constructor obligations. It does **not** establish a finite list
of concrete physical operators generating 𝓘; such a generation theorem
would be an additional, separate obligation.

**Non-inference rule:** the theorem sources no primitive preservation,
context stability, label/cone covariance, state-space identification, flow,
gate, test validity or quantum inclusion. It does not close K2 or P0 and is
not a substitute for the bridge audit's physical-source/disguise tests.
With an excessive inventory such as fullClass, preservation assumptions can
already force quantum inclusion; that is an assumption audit, not a success
for sourcing compatibility. No manuscript or ROADMAP change is licensed here.

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

The research core and exact layer are available, but these remaining edits
are not yet a concrete, freeze-ready execution package. D remains fixed at
`dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4`.

After an owner designation of exact, all-green F, follow the linear execution,
E/reconciliation and receipt process in AGENTS §A.39. No older native control
plane is thawed, and no execution, receipt or certification is claimed by
this recovery draft.
