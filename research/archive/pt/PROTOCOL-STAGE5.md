# PT protocol — stage 5: the observer-native origin of off-frame reversible mixing (Q-EX-BRIDGE)

`PROTOCOL.md` (`239dc123…`), amendments 1–2, `PROTOCOL-STAGE2.md`, `PROTOCOL-STAGE2-DS.md`, `PROTOCOL-STAGE3.md`
(`1a649168…`) and `PROTOCOL-STAGE4.md` (`d3da2811…`) govern except where this file differs. Owner's direction
(verbatim, note 7, `OWNER-NOTE7-STAGE4-CLOSE.md`): "Q-EX-BRIDGE: Observer-native origin of off-frame reversible
mixing. The goal should be to determine whether a genuinely observer-native operational principle can justify the
weakest sufficient additional transformation without assuming the desired composite action in disguise. The round
should distinguish three outcomes: Derived: A precise observer-native premise implies the required mixing, without
circular use of extension of operations. Independent: A countermodel satisfies the proposed observer-native premises
but lacks the mixing. Conditional: The bridge works only under another explicitly identified assumption." Kept
separate by the same direction: T/F universal exclusions, H minimality, the Origin targets. Holds unchanged: no
repository change, branch, PR, CI, governed round or publication. Stage 4 is a completed audited result; nothing in
`pt/Y/`, `pt/Z/`, `pt/audit/Y/`, `pt/audit/Z/` or `pt/INTEGRATION-NOTE-STAGE4.md` changes.

## The question Q-EX-BRIDGE
Stage 4 (audited, `pt/INTEGRATION-NOTE-STAGE4.md`): for a closed cone `K ⊆ W 3` with H1–H3 (products in `K`;
`cnot`-invariance, at level (ii) the even class `G16`; `K = dualW K`), each of the following composite-action
principles forces `K = Q3`, and each is INDEPENDENT of H1–H3 plus the certified pair structure at L:
- **(b_S4)** the full rotation group of one token acts on the pair preserving `K` (`actC SO(3)` or `actT SO(3)`);
- **(b_n)** one rotation subgroup of one token about an axis `n` off the native frame's coordinate axes;
- **(b_R1)** one order-3 rotation of one token about (5,1,1);
- **(b_DJ)** the native drive (the flow through the NOT, on the NOT axis) together with the native `J` (`cyc3`,
  `KInfFoundations.lean:449`), both acting on one token of the pair preserving `K` — to be fixed exactly in the
  coordinator's pre-audit: the Lie closure of the flow and its `J`-conjugate, with `cnot`, is the full
  `su(2) ⊕ su(2)`.
Write (b_min) for any one of these. The question: for a candidate observer-native principle `P`, decide the
implication `P ⇒ (b_min)` in one of three outcomes, with the composite action never assumed in disguise.

**Outcomes, defined.**
- **DERIVED(P).** A written proof with exact ingredients [W + X] that `P`, together with the certified structure at
  L (single token: the body, the NOT, `ElementaryDrivability`'s flow and `J`; pair: `W 3`, `NativeGate`, H1–H3)
  implies (b_min) for some sufficient form, where `P` passes the disguise test.
- **INDEPENDENT(P).** An exact structure satisfying `P`'s transcription, H1–H3 and the certified single-token
  structure, whose cone is not `Q3` (the stage-3 cones, the stage-4 seeds, or new ones) — or a kernel theorem
  stating the independence at the matrix level, cited with its scope (matrix carrier; all operations or reversible
  ones only).
- **CONDITIONAL(P; A).** `P ⇒ (b_min)` only together with a named additional assumption `A`, with `A`'s status
  (certified / hypothesis of a certified theorem / manuscript's added principle, file:line / open obligation / new)
  and whether `A` passes the disguise test.
- **Disguise test.** `P` passes iff it is stated without reference to the composite action of single-token
  operations: no "`O ⊗ id` preserves `K`", no idle extension, no IE1/IE2, no frame covariance, no spectator clause
  about the pair cone, no `Q3`/PSD/pure states/reachability. A principle whose content *is* a spectator or
  extension clause (OI⁺'s observational independence, `HasParallelReferenceExtension`; implementation locality's
  spectator clause; structural closure's spectator stability; `LayerFlowExecutable`'s quantification over every
  level) does not pass; the implication through it is CONDITIONAL on it, and the round records at which level the
  manuscript sources that clause (theorem for the substratum class; hypothesis for an extension; open obligation
  K2 in the field-neutral setting). The decisive deliverable is the **dependency chain** with every link's status,
  not a single word.

**The dependency chain to fill.** Each link: certified theorem [K] (file:line) / hypothesis of a certified theorem
(name the theorem) / open obligation (ROADMAP entry) / manuscript's added principle (file:line) / new; and whether
its field-neutral transcription to `W 3` is exact or by analogy.
- L0 — substratum: operations as bijections and monomial operators of configurations; layers act on regions
  (`StructuralClosure.lean:316 substratumClass_structurallyClosed`; `SubstratumInterface.lean`; `Main.md:628`).
- L1 — single-token availability of an off-frame or continuous operation: K∞-Act, K∞-Drive (ROADMAP.md:1014–1022,
  OPEN; `ElementaryDrivability` a hypothesis); at the matrix level the layer flow at intermediate times is not
  sourced by the substratum (`LiftAudit.lean:200 substratumTheory_not_layerFlowExecutable`, `ExecSource.lean:129
  obs_not_layerFlowExecutable`, `ReadWriteControl.lean:174 readWriteSourced_not_qm`).
- L2 — spectator stability, the composite action (b): OI⁺-1 (`ReferenceExtension.lean:447
  HasParallelReferenceExtension`; `CompletedOI.lean:129`, `:131`, `:147`; `GR.md:228`); implementation locality
  supplies it (`ImplementationLocality.lean:370`, `:957 observationalIndependence_of_implementationLocality`;
  `GR.md:244`); the substratum class has it as a theorem and an extension has it as a hypothesis
  (`StructuralClosure.lean:183 StructurallyClosed`, `:365 quantumArchitecture_iff_drives_of_closed`, `:408
  substratum_extension_quantum_iff_drives`; `GR.md:256`); `LayerFlowExecutable` quantifies over every level
  (`LiftAudit.lean:112`; `DerivedQ3.lean:222`); kernel independence results (`CompletedOI.lean:506
  oiPlus_independence`, `ReferenceExtension.lean:507 control_not_implies_parallelReferenceExtension`); the
  field-neutral K2 obligation "local actions compatible with the composite cone" (ROADMAP.md:1001–1005, OPEN); the
  earlier equivalence records (IE1 at KT(4): `pt/inputs/ledgers/EQ3-P-RESULT.md`, `EQ3-AUDIT.md`; premises
  unsourced: `EQ5-SOURCE-RESULT.md`, `EQ5-SOURCE-AUDIT.md`; the certified premise audit
  `pt/base/verification/programmes/oi-qm/reconstruction/round-kt4-prem-1-premise-audit/result.md`;
  `EQ2-SYNTHESIS.md:155–170`).
- L3 — (b_min) ⇒ S4 ⇒ `K = Q3`: stage 4 [W + X], audited.

**Candidate principles** (record; threads may add, never relabel). For each: the exact transcription to the pair
setting, the outcome, the assumption named if CONDITIONAL, the disguise test, the evidence.
- α — OI⁺-1, observational independence (inert spectators).
- β — implementation locality (interventions realized by one protocol from admissible implementation operators;
  admissibility invariant under adjoining an uncoupled spectator).
- γ — structural closure of an implementation class (closed under composition, coarse-graining, ancilla blocks,
  relabelling, adjoint; stable under an uncoupled spectator): theorem for the substratum class, hypothesis for an
  extension.
- δ — layer-flow executability (`LayerFlowExecutable`, ∀ level, ∀ time) and its level-1 restriction; the flow of a
  local involution extended by the identity (`levelPerm σ n`).
- ε — substratum locality: dynamical causal separation of visible regions (`Main.md:628`); the substratum-source
  form's spectator stability (`GR.md:256`).
- ζ — observer recursion / embedded observation (OI⁺-3; `EmbeddedObservation.lean`): the pair as an admissible
  system with its own single-system structure (drivability, transitivity) — countermodel candidates: the stage-3
  cones with their own automorphism tori (`K(Z_F)`: `T³_F`, Z z1).
- η — copy naturality (`KInfFoundations.lean CopyNatural`) and the native-gate relations `relT`, `relC`
  (`CompositeDimension.lean:224–225`): NOT-level consequences only.
- θ — steering, no-signalling, conditional-state admissibility (every conditional state admissible): `maxCone`.
- ι — token exchange (`SWAP`): stage 4 S1.
- κ — the gate's own flow (a one-parameter group through `cnot`, e.g. `exp(−iθ P₁⊗P₋)`): product-diagonal torus.
- λ — four-token composition coherence KT(4) with `tok` (EQ3/EQ4/KT4-PREM-1): IE1 derived, premises unsourced.
- μ — frame covariance of the native gate: ⟺ IE1 given `hgate` (stage 2): fails the disguise test by record.

## Threads
- **Thread D (BRIDGE-DERIVE):** the dependency chain L0–L3 filled with every link's status and the exact kernel or
  manuscript anchor; the field-neutral transcription of α–ε, ζ, λ; derivation attempts for (b_min) from each, with
  the disguise test applied; the matrix-level sourcing map (which spectator clauses are theorems of the substratum
  class, which are hypotheses of an extension, whether `LayerFlowExecutable` at level 1 plus implementation locality
  gives every level); the weakest sufficient added content in both settings (matrix: the smallest hypothesis beyond
  the substratum class and L1; field-neutral: (b) for the drive and `J`, or for one off-frame rotation), and
  whether any principle at L below the OI⁺ layer yields L2.
- **Thread C (BRIDGE-COUNTER):** exact countermodels for the field-neutral transcription of every candidate that
  does not suffice or does not pass (η, θ, ι, κ, ζ, the NOT-only and finite forms of α–δ, λ without `tok`), each
  with the principle verified on the countermodel exactly; the minimal-subset census of the native single-token
  operations idle-extended on one token — {flow}, {J}, {NOT, J}, {flow, NOT}, {flow on both tokens}, {flow, J} —
  deciding exactly which force `Q3` (stage-4 criteria) and which admit countermodels (explicit or seeds); the
  kernel's matrix-level independence and no-go theorems transcribed with their scope; the closure picture: the
  `cnot`-closure of products is not self-dual (stage 2, `pt/S2/RESULT.md`), the closure under `cnot`, flow and `J`
  is `Q3` (exact).
Both threads: depth-first, decisive first (D: the sourcing map of L2, then α–δ; C: the minimal-subset census, then
the countermodels); countercontrols on every decisive check (`Q3` must pass every retention test; the stage-3 cones
must fail every exclusion claimed; every countermodel must satisfy the candidate's transcription exactly).

## Rules
As `PROTOCOL-STAGE3.md` and `PROTOCOL-STAGE4.md` (exact arithmetic; decision rules in headers before the first run;
`python3 -I -B`; byte-identical replays; failed runs kept; evidence levels; no flagged premise inside a derivation
except as the candidate `P` under test, named; `Q3` only as comparison object). Working directories `pt/D/`,
`pt/C/`; `.start_marker` first; the anomaly sweep excludes the sibling directory, `pt/audit/` and
`pt/audit*-replay/`. Read: `pt/Y/`, `pt/Z/`, `pt/audit/Y/`, `pt/audit/Z/`, `pt/INTEGRATION-NOTE-STAGE4.md`, the
stage-1/2/3 records, `pt/inputs/ledgers/`, `pt/base/` (read-only); not `pt/audit/stage3-inputs/OWNER-*`,
`pt/audit/stage4-inputs/OWNER-*`, `pt/audit/stage5-inputs/`, `pt/audit/reviews/`, `pt/audit/aborted-launches/`, nor
the sibling thread. The owner's direction is quoted above in full as far as it governs this round.

## Deliverables (`pt/D/`, `pt/C/`: `NOTES.md`, `RESULT.md`)
0. Answer: the verdict table (candidate / transcription / outcome / assumption named / disguise test / evidence);
   the dependency chain L0–L3 with every link's status; the weakest sufficient added content, in both settings,
   with its relation to OI⁺-1 and to the layer-flow hypothesis; for C, the minimal-subset census.
1. Candidate by candidate, with every exact witness named and every kernel anchor by file:line.
2. Ledger: certified versus added; flagged premises and where they enter (as candidates only).
3. What is not claimed.  4. Evidence log.  5. Integrity.
