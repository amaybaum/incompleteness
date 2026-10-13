# Reconstruction round PRESERVE-INDUCT-1 — conditional preservation by protocol induction: PREREGISTRATION (reconstructed draft for owner review)

**Status: native V3 control-plane draft for review; not an F candidate.**
No design module, probe, controls implementation or execution exists for this
round. Only the owner designates F after the concrete package and its exact-head
checks are ready under AGENTS §A.39. An instruction to recover a PR is not F.

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

## Proposed definition and theorem budget

The following names and interfaces are proposed, uncompiled and not frozen.
Design runs must settle exact binders, universes and the final statements
before any F candidate. Keep the family on all finite carriers needed by the
discard induction hypothesis, not just on the final two-token carrier.

1. `CarrierConeFamily`: a set C_S of matrices for each finite carrier S,
   specified independently. Hermitian/cone structure can be exposed through
   separately named fields; the induction needs zero and finite-addition closure.
2. `ConeClosure`: zero, addition and nonnegative real scaling for each C_S.
   Record which fields each theorem actually uses. Do not claim every field
   is necessary merely because it is convenient to package them together.
3. `PreservesCarrier`: for an endomorphism Φ, X∈C_S implies Φ(X)∈C_S.
4. `PrimitivePreservation`: two distinct fields: each admitted isometric
   conjugation preserves C_S, and each branch of an admitted native register
   readout preserves C_S. The readout field cannot be folded into the
   isometry field: a nontrivial projection is not an isometry.
5. `UniformAttachPreservation`: for m>0, `uniformAttach m` sends C_S into
   C_(S×Fin m). It attaches I/m, not a pure ancilla.
6. `AncillaDiscardPreservation`: for m>0, `ptraceAnc m` sends the composite
   cone C_(S×Fin m) into C_S.
7. Optional `ConeRelabelling`: explicit compatibility of C_S with matrix
   reindexing. Use it only where a result identifies two differently labelled
   cone spaces; class-level label invariance is not a substitute for this field.

The schematic headline, with those proposed definitions, is:

```lean
theorem instAvail_preserves
    (C : CarrierConeFamily) (hC : ConeClosure C)
    (hPrim : PrimitivePreservation 𝓘 C)
    (hAttach : UniformAttachPreservation C)
    (hDiscard : AncillaDiscardPreservation C)
    (h : InstAvail 𝓘 S O F) :
    ∀ a X, X ∈ C S → F a X ∈ C S
```

Also propose `instAvail_sum_preserves`, summing the unnormalized branches,
and `instAvail_spectator_preserves`, obtained by applying the headline on the
joint carrier to `instAvail_spectator`. Its additional premises are exactly
the existing context/label hypotheses plus the same all-carrier preservation
premises. Transported versions must say whether they preserve the cone
assigned to the new label or additionally identify it with the original cone.
No iff, minimal-premise result, reconstruction theorem or physical source is
part of the proposed headline.

## Written induction route, still uncertified for this round

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

These are design obligations, not saved results. Freeze their concrete
definitions, arithmetic, theorem statements and measured counts only after
they are implemented and green.

- **Quantum comparison:** the independently specified PSD family, with the
  ordinary isometric conjugations, register projections, uniform attachment
  and partial trace. Establish the premise instances and the resulting
  branchwise preservation without defining the general family as PSD.
- **Classical comparison:** nonnegative diagonal cones with monomial
  implementations and coordinate readouts. Verify attachment, discard,
  coarse-graining and a genuinely outcome-dependent continuation.
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
  prospective failures; no mutation count is claimed yet.

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
attachment/discard and cone-closure premises propagate to every finite
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

Before F: resolve the proposed definitions against D; build a research-only
module; settle the theorem surface and proof imports; implement and measure
controls and their independent path; specify exact registry/census/import
and workflow edits; run the predicted executable tree; pin all design files
and parameters in this PR. Those artifacts do not yet exist for this round.

After an owner designation of exact, all-green F, follow the linear execution,
E/reconciliation and receipt process in AGENTS §A.39. No older native control
plane is thawed, and no execution, receipt or certification is claimed by
this recovery draft.
