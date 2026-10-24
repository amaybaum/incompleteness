# Node 9 mapping audit: G1, G2, C5-P, H-LOC, M1–M5 and model A against the existing kernel results

Read-only. Base `ba5c8d76` (detached worktree, now removed). `KTokenMaxCone.lean` is not in `ba5c8d76`'s ancestry, so
it is cited at `origin/main` `af8c59d6`. No `lake` build was run. Every kernel citation is a source line, and the
axiom status is the one the cited audits record. Tags:
- [K]: kernel statement, `file:line` under `verification/lean-mathlib/OIBridge/`;
- [A]: audit or round record;
- [arg]: my argument, not reviewed;
- [EC]: my exact check, `scratchpad/map/probe/hperm.py` (ℚ(√2) arithmetic, not committed).

An analogy is marked as one. No correspondence below is an identity unless a map is named.

## 1. G1, the sign/phase composition law

**(a) Results.**
- O1 is `PhasesAvailable` (RouteB.lean:128): the quarter phase `phaseGate a` = diag(i at a, 1 elsewhere)
  (LieRankSource.lean:209), at every level.
- The ℤ₂ sign is `diagonal (flipAt b)` = `phaseGate b`² (DerivedQ3.lean:55, :66), obtained from O1 by `flip_avail`
  (:171).
- Under the stated access: `permTheory_not_phasesAvailable_onesFixing` (PhaseSource.lean:104) excludes S;
  `permTheory_no_sign` (SubstratumInterfaceAudit.lean:680) excludes every sign diagonal; and
  `instAvail_unitary_fixes_ones` (InstrumentRealization.lean:398) excludes every available unitary that moves the
  uniform ray, which covers Z and H.
- For every rule, the observer theory is `permTheory` (`obsTheory_rule_independent`, SubstratumInterfaceAudit.lean:779).
- The C5 polarization candidate: the shear's image is S (`siteShearImage`, C5Discovery.lean:192, `_one_eq_phaseGate`
  :252); the swap's image is H (`siteSwapImage` :196); and `gateFlow_half_eq_hsh` (:287) gives H·S·H.

**(b) Does O1 correspond to G1's central-extension signs?** No. G1's admissible class is the real Pauli/real Clifford
class. Under G1's own calibration dictionary (swap ↦ H, couple ↦ CNOT, flips ↦ X, Z), its operational content is H,
CNOT and Paulis. The quarter phase is G1's S-type map p ^= q, which has no lift in the ℤ₂ class (G1-REPORT §1(b), H1).

- **ℤ₂ is weaker than O1 in isolation.** O1 gives the sign flips (`flip_avail`). The converse fails, because real
  Kraus forms are closed under every operation (node 5 clause R, [W, EC]; there is no kernel theorem).
- **On the route through O2, ℤ₂ is all of O1 that is consumed.** Q3's proof (`phaseFree_of_phases_layerFlowExecutable`,
  DerivedQ3.lean:181–205) uses `PhasesAvailable` only through `flip_avail`, as derived-q3-audit's "Where the phase
  hypothesis is consumed" records. The complex structure comes from the gate flow itself.
- **So G1's real signs, plus exchanges, plus O2, plus `SourcedOI`, would reach QM** [arg: restating Q3 with a
  sign-flip hypothesis is one line and is not in the kernel; then `sourcedOI_qm_iff_phaseFree`,
  SubstratumInterfaceAudit.lean:654].
- A real theory cannot contain O2 (the gate flow is complex).

**Does `permTheory_not_phasesAvailable_onesFixing` imply the displayed substratum cannot supply G1?** Not by itself:
it concerns S. The answer is yes, settled, at the availability level (R2), from its invariant together with
`permTheory_no_sign`, configuration-level monomiality (H is not monomial, `hadamard_not_monomial` C5Discovery.lean:162)
and `obsTheory_rule_independent`.

**Does this match G1-REPORT §2's quadratic-update finding?** Only partly, and the kernel is stronger in one direction.
- G1 §2 concerns a cocycle update on F₂ record labels: a classical record automaton, tableau-level, at the level of
  record statistics (R1).
- Suppose a phase cell with a degree-2 update is added as a substratum cell. It is still a configuration bijection, so
  the observer theory of the enlarged substratum is still `permTheory` and has no sign and no H.
- So the quadratic update is a condition for classical reproduction of stabilizer record statistics. It is not a route
  to O1 or to G1's operational content.

**(c) Mismatch.**
- G1 lives in a central extension E of F₂^{2n} acting on record labels, with stabilizer-group states and read rule (c).
- The kernel lives on `Matrix Conf Conf ℂ` with instrument availability.
- G1 is ℤ₂/real; O1 is ℤ₄/complex.
- G1 works at n ≤ 2 systems; O1 is quantified over every level.
- The bridge between them is G1's calibration dictionary (ERT), which is not a kernel map.

**Structural correspondence** [arg, a dictionary and not a theorem]:
- G1's card system (q, p) is the C5 per-site pair V × V.
- G1's swap is the C5 swap layer.
- G1's lift question is the choice of Weil/Clifford lift, which C5 stipulates (shear ↦ S on position 1, swap ↦ H).
- So G1 is the record-level form of C5 candidate 2, with the shear dropped.
- [EC] H on either qubit together with all 24 permutation matrices reaches exactly 24 states from |00⟩ (up to sign),
  with every single-qubit Z/X expectation in {−1, 0, 1}. This is the same count as G1's reachable family. It is a
  count coincidence check, not an automaton equivalence.

## 2. G2 (pure states beyond stabilizer, continuous completion)

**(a) Results.**
- O2: `LayerFlowExecutable` (LiftAudit.lean:112); `uncountableNonMonomialRays_of_layerFlowExecutable`
  (CoherentContinuumSource.lean:163).
- Countability: `countable_not_pairFlowSourced` (PairFlowEquivalence.lean:218); `polC_countable_upToScalar` and
  `polarizedTheoryC_not_layerFlowExecutable` (PolarizationClosure.lean:372, :389).
- Exact vs dense: `fixedGateTheory` (DiscreteCompletion.lean:1926; the stated access plus the quarter phase plus one
  real rotation `rot α`, class `MixR {α}` in StateMixingCoupling.lean); `fixedGateTheory_denseFiniteQM`
  (DenseInstrumentBridge.lean:521, with `KrausDense`/`DenseFiniteQM` at DiscreteCompletion.lean:52, :59);
  `fixedGateTheory_not_qm` (:1948).
- Completion infrastructure: CMP-1's `DirectedStages`, `SCInf` and `body` (StageCompletion.lean:63, :78, :141);
  OPACT-1's `AffineRespect` and `existsUnique_induced` (CompletionAction.lean:58, :258).

**(b) Does O2 correspond to G2?** No. O2 ⟹ G2 through the endpoint (`derivedOI_qm_iff_layerFlowExecutable'`
DerivedQ3.lean:222). G2 ⇏ O2.

- **G2's finite witness needs neither a continuum nor a limit** [EC]. Apply H to two qubits, then one configuration
  exchange |110⟩ ↔ |111⟩ (Toffoli, a single exchange, available in the sourced access: `ExchangesAvailable`,
  `permTheory_sourcedOI` SubstratumInterfaceAudit.lean:660). The result is (|000⟩ + |010⟩ + |100⟩ + |111⟩)/2, whose
  target marginal is exactly diag(3/4, 1/4).
  - This lies in `PolGen` minus the shear: countable, no O2, not QM.
  - At two qubits, H with all 24 permutations stays at {−1, 0, 1}, since every permutation of two bits is affine
    (|AGL(2,2)| = 24 = |S₄|).
  - So Lemma G's 1/4 gap is a property of affine operation rules (Π_ω = ASp(2n, 2), the compatible-records argument's
    "affine symplectic"). It does not need a stabilizer "size" or the continuum.
  - The witness needs a two-qubit purifier. Pur-E with a one-system purifier (M2's same type) is not checked.
- **"Limit along a family": partly duplicates.**
  - For one countable theory on the fixed carrier `Fin 2 × Fin n`, `fixedGateTheory_denseFiniteQM` already gives what
    LIMIT-DESIGN's "stage error → 0 on a finite 𝓔" asks for. The stages are depth-truncations and 𝓔 is made of finite
    Kraus instruments [arg].
  - But that theory stipulates O1 and a postulated real datum (state-mixing-coupling audit). It is a calibration, a
    stronger K-RAT, not an OI construction.
  - LIMIT-DESIGN's declaration 1 (stages, with embeddings preserving each experiment's meaning) restates CMP-1's
    `DirectedStages` + SC∞, and its operations-carried-to-the-completion restates OPACT-1.
- **What LIMIT-DESIGN adds.** None of the following is in DenseFiniteQM, CMP-1 or OPACT-1:
  - comparison against an external target (CMP-1's completion is intrinsic);
  - the P-fin/P-lim distinction;
  - endpoint purity as a separate obligation;
  - essential uniqueness to within the stage error.
- **A nuance** [arg]: on the kernel's fixed ℂ^d carrier, rank-one states form a closed set, so a limit of pure states
  is pure there. LIMIT-DESIGN's warning bites only for menu-relative purity or ℓ^∞-type completions (CMP-1's `body`).

**(c) Mismatch.**
- A1 exact continuum (O2) vs a finite exact witness vs A2 density.
- A fixed ℂ carrier with levels as composites vs card/toy stages without an ambient carrier.
- DenseFiniteQM is about instruments; G2 is about states and purity.

## 3. C5-P (purification)

**(a) Where purification sits.**
- As ambient mathematics only: `purification_unconditional` (BoundaryAudit.lean:106) and `purifier_uniqueness`
  (UhlmannUniqueness.lean:340), facts about ℂ-matrices with no availability.
- The pure seed from a uniform ancilla, readout and feed-forward: `uniform_readout_feedforward_seed`
  (Purification.lean:115); `pureSeedPrep_available` (OperationalAssembly.lean:741).
- The uniform hidden prior's canonical purification as a representation: `purifiedIsometry_apply`
  (SemigroupTransfer.lean:182). The dilation's uniqueness holds per time only (`readingA_perTime` :220), and `ST3_pairC`
  (:749) has equal families with no relating unitary. These are analogous to Pur-U failure modes, nothing more.

**(b) Implied or absent?** It is absent as a premise from every characterization:
- `oiPlusMin_iff_qm` (MinimalRepertoire.lean:569), `OIPlus` and `oiPlus_iff_qm` (CarrierGeneralOIPlus.lean:185, :207),
  `sourcedOI_qm_iff_phaseFree`, `derivedOI_qm_iff_phaseFree` (RouteB.lean:161);
- `circuit_available` (OperationalAssembly.lean:757) states "no purification and no Uhlmann uniqueness is used";
- Main.md:352 puts purification among the continuum-endpoint hypotheses of the cited reconstructions.

Operational C5-P at A1 is a consequence of exact QM [arg: composite control + pure seed + the two ambient theorems,
with the relating unitary available]. No kernel theorem states it. So it is implied by phase-free richness under
`SourcedOI`, and by OI⁺, only via QM, and nothing sources it. Its two halves need different things:
- Pur-E on a finite witness needs only item 2's ingredients.
- Pur-U for every state needs dense or exact unitary control on the purifier [arg].

**(c) Mismatch.** Ambient rank-one purity vs node 9's operational purity relative to Prep(𝓘) and Lemma W.

## 4. H-LOC

**(a) Results.**
- `coherentLiftClass` (LiftSource.lean:143), the D·P_g lifts of configuration permutations, equals `substratumClass`
  (`coherentLiftClass_eq_substratumClass` :164).
- `configurationLevel_not_phaseFree` (ManuscriptAxioms.lean:169).
- `updateLevel_symplectic_inert` (C5Discovery.lean:119).

**(b) Consistent, and not redundant.**
- Under the dictionary, H-LOC's coupling lifts (CNOT·Pauli) and flips are monomial, so they lie in `coherentLiftClass`.
  By `coherentLiftClass_eq_substratumClass`, the selection among them is invisible to every availability predicate.
- Only the swap lift (H·Pauli) is non-monomial.
- This matches H-LOC's own observation that every NBC₃-separating word contains swap_A. The primary new test selects
  among monomial lifts whose differences matter only through H.

**C5 test 1 constrains H-LOC's significance.**
- H-LOC's selector, B1 locality plus longest card agreement, is built from update-level and record-level data.
- Through the stipulated configuration-level sourcing it is inert (`updateLevel_symplectic_inert`,
  `configurationLevel_not_phaseFree`).
- It bears on availability only given a non-configuration-level map (C5 test 8), which neither the corpus nor H-LOC
  supplies.
- Even then, the selected class has no S (no O1), is finite (no O2) and keeps Lemma G's gap. It selects a labelling (a
  Pauli frame) inside the countable polarized family, beside `polarizedTheoryC_derivedOI`/`_not_qm`
  (PolarizationClosure.lean:606, :620). That is calibration of C5 candidate 2's stipulated images.

**(c) Mismatch.** H-LOC is about labelled operations (which group element is "swap"); the kernel's predicates are about
generated classes, and G1-REPORT shows the generated group is choice-independent.

## 5. M1 and the spectator clause

**(a) Results.**
- COMP-1: `PreComposite`, `LocallyTomographic`, `Composite`, `attach`, `minBody` (CompositeInterface.lean:223, :235,
  :243, :253, :267), `margA_attach` (:312), `no_composite_over_paddedPre` (:895), `comp1_core` (:926). Its open item is
  "a source of a composite larger than the minimal body" (result.md, "What stays open").
- OI⁺ observational independence: CarrierGeneralOIPlus.lean:73, :75, :87; GR.md:232.
- `SpectatorIndependent` (MonoidalCompletion.lean:204, classified at :215).

**(b) Status.**
- **M1's bare witness:** node 9's governing question is an instance of COMP-1's open item. A pure ψ with a mixed
  marginal puts the body strictly above `minBody` [arg: it needs the extreme points of `minBody` to be products, which
  is not a COMP-1 theorem]. No kernel result supplies such a composite from OI. Partly mapped; the content is new.
- **The (S) clause:** analogous only. OI⁺ independence is operation-level (availability is unchanged when an untouched
  system is adjoined), and `SpectatorIndependent` is completion-level (id ⊗ Φ_B on products). (S) is about the
  preparation-level purity of ψ ⊗ σ. They share an ingredient; no map takes one to the other. In exact QM, (S) holds
  trivially.

**(c) Mismatch.**
- COMP-1 bodies sit in real charts with product-effect separation (`lt`). Node 9 decides equivalence with interaction
  experiments (Lemma W).
- A G1-real composite fails `lt` (the owner's ρ± = (II ± YY)/4), so it is at most a `PreComposite`.
- COMP-1 has no three-party product, purity or uniqueness.

## 6. M3, M4 and M5

**(a) Results.**
- `pairCone_eq_Q3_iff_drive_maxCone` (EqvK2MaxCone.lean:174; the forward direction :153;
  `maxCone_bound_of_sharp_available` :194), with Q3 the two-qubit PSD tables (EqvK2Schema.lean:239).
- k-token (`origin/main`): `subset_QK_of_maxCone_drive`, `QK_subset_of_products_cone_drive`,
  `kCone_eq_QK_iff_drive_maxCone`, `pairCone_eq_Q3_of_kToken` (KTokenMaxCone.lean:2298, :2311, :2364, :2466).
- The Bell theorem: Main.md:361–371 (deterministic, pointwise cone, common ensemble ⇒ |S| ≤ 2; probe-certified, not
  Lean), branch (a) at :392. Thread results mc-node6 (N1–N5) and mc-node7 (17 readings, none fixing the quantum bound).

**(b) Status.**
- **M4's local branch: settled** by the Main theorem for every model meeting (i)–(iv). Node 9's K-BL already uses it.
- **M1, M4 and M5 at the A1 endpoint: conditional, not deciding node 9's models.** If a model's pair cone met hH1,
  hadd, hsmul, hmax, hH2 and hA, then K = Q3: M1 holds, and M4/M5 take two-qubit QM values. The Tsirelson and POM
  values are literature; there is no CHSH or Tsirelson statement in the Lean kernel (grep).
  - Node 9's models fail hH1: their local body is the diamond or real, not `eball 3`, which needs Y, i.e. complex.
  - They fail hA, the rotation at every real t (Lemma F / O2-like).
  - So the theorem names the premises that would settle M4/M5. It decides nothing finite.
- **M3** is single-system; the pair cone is silent on it. There is no kernel object for preparation contextuality.

**(c) Mismatch.** Exact cones on qubit-power coordinate carriers, with local tomography as a premise (the non-inference
rule), vs finite rational operational models.

## 7. Model A and node 8

- **Node 8's obstruction** (every composite preparation is a mixture of products) is the typed situation "body =
  `minBody`" of COMP-1. It is analogous only: no kernel theorem places OI realizations there. Its operational shadow is
  that monomial classes preserve diagonal states (`preservesDiag_conj_of_monomial`, used in
  `configurationLevel_falsifierUnavailable`, ManuscriptAxioms.lean). From basis seeds they reach only phased basis
  states, whose marginals are pure [arg].
- **The uniform-affine (stabilizer) gap is not in the kernel in any form.**
  - The kernel's invariants are about the uniform ray, not affine supports: `OnesNormal`/`OnesFixing`
    (InstrumentRealization.lean:313, :398) and `NonnegBounded` (FrozenSourcing.lean:65).
  - The kernel's sourced access is non-affine: the exchanges, from `exchanges_of_readWrite`,
    SubstratumInterfaceAudit.lean:642.
  - By item 2's check, the gap is load-bearing on the affine rule Π_ω, not on OI's stated access.

## Summary table

| node-9 item | existing result | status |
|---|---|---|
| G1 ℤ₂ signs vs O1 | `PhasesAvailable`; `flip_avail`; Q3 consumes only the flip | analogous; ℤ₂ weaker than O1 alone, sufficient beside O2 [arg] |
| G1 not supplied by the displayed substratum | `permTheory_no_sign`, ones-ray invariant, `obsTheory_rule_independent` | settled (R2, configuration-level sourcing) |
| G1-REPORT §2 quadratic update | same | partly: true at R1, inert at R2 |
| G1 lift structure | C5 candidate 2 (`siteShearImage`/`siteSwapImage`, PolC) | analogous via the ERT dictionary (record form of candidate 2) |
| G2 finite witness (3/4) | `PolGen` + one exchange | new [EC], countable, no O2 |
| G2 limit (operations) | `fixedGateTheory_denseFiniteQM` | settled as calibration only |
| LIMIT-DESIGN stages and embeddings | CMP-1 `DirectedStages`/SC∞, OPACT-1 | duplicate |
| LIMIT-DESIGN P-fin/P-lim, uniqueness, external target | none | new |
| C5-P | ambient purification and Uhlmann; absent from every characterization | consequence of the endpoint, never sourced |
| H-LOC | `coherentLiftClass_eq_substratumClass`, `updateLevel_symplectic_inert` | consistent; inert without the test-8 map |
| M1 bare witness | COMP-1 open item (> `minBody`) | partly mapped; new content |
| M1 spectator clause (S) | OI⁺ independence, `SpectatorIndependent` | analogous (shared ingredient) |
| M4 local branch | Main.md:361–371 | settled |
| M4/M5 endpoint | pair-cone / k-token theorems | conditional; does not decide finite models |
| M3 | none | new |
| node-8 obstruction | COMP-1 `minBody` | analogous |
| Lemma G gap | none (ones-ray invariants differ) | new, and scoped to affine rules |

## Recommendation

**Stop.**
- Reading G1's ℤ₂ signs as O1, and pursuing a quadratic phase-cell update as a source of phase. Every configuration
  bijection is inert at availability level.
- Enlarging affine families, or seeking a continuum or limit, to beat Lemma G. Non-affinity plus one non-monomial gate
  suffices for the finite witness.
- Re-deriving the following, which are already in the kernel or the corpus:
  - the dense endpoint, stage/SC∞ embeddings and completion action;
  - the countability obstruction;
  - the Bell-local bound.
- H-LOC's n = 3 run (an estimated 20 to 3,000 CPU-hours): consider deferring it. Its outcome selects a frame among
  monomial lifts and has no availability consequence absent a test-8 map. This is an owner call.

**Reuse and cite.**
- `flip_avail` with the Q3 proof.
- `permTheory_no_sign`, `instAvail_unitary_fixes_ones` and `obsTheory_rule_independent`.
- C5 candidate 2 and PolC, as the operational form of G1.
- `fixedGateTheory_denseFiniteQM` as LIMIT-DESIGN's calibration.
- CMP-1 and OPACT-1 for declaration 1.
- COMP-1 `minBody`/`PreComposite` for M1.
- The pair-cone/k-token theorems as M4/M5's A1 endpoint premise list.
- Main.md:361–371 for M4's local branch.
- The ambient purification and Uhlmann theorems for the endpoint statement of C5-P.

**Genuinely new.**
1. An explicit map from node 9's record/card interface to an operational carrier: the S7 / test-8 carrier map. Neither
   the corpus nor the kernel has it.
2. Operational, menu-relative purity: M1's (S), and Pur-U for every state.
3. LIMIT-DESIGN's external-target error, the P-fin/P-lim distinction and uniqueness in the limit.
4. A composite above `minBody` from an OI source (COMP-1's open item).
5. M3 (preparation contextuality).
6. Labelled-lift (frame) selection, as a question in its own right.

## C5 audit: the verdict C reason, and whether node 9 bears on it

**The reason.** Test 8. The corpus states neither a non-bijection-valued coupling nor the polarization map. The
polarization candidate is non-configuration-level and is kernel-proved only at level one (site S, H, and the half-time
swap-flow point). The later polarization-closure audit decided O1 positive for PolC and O2 negative by countability,
and left C unchanged because test 8 is unchanged.

**What node 9 bears on.**
- **G1/ERT/H-LOC** are round-supplied labelling rules for candidate 2's map. They do not supply a corpus map, so test 8
  is unchanged.
- **C-i/emb** is CONFIRMING on test 8 and test 1, and does not reopen C.
  - C-i-a: Main.md:292 partitions the lattice by sites ("both coordinates of a site share its visibility"). This is the
    corpus fact C5 T6 records: Γ_V × Γ_H splits sites, not per-site phase space. So the read/disturb polarization is not
    realized at unchanged positions.
  - C-i-b: the disturbance-free records (passive κ4 readout, visible-only copies made by observer CNOTs, "symplecticity
    never forces a hidden kick") are what configuration-level sourcing yields: copies are permutations, and
    `updateLevel_symplectic_inert` applies.
  - The back-action postulates AP-4/AP-5, PP-1/PP-2 and Π_ω are round-supplied classical record rules. Through the
    stipulated sourcing they are configuration-level and inert for O1/O2 [arg].
- **The G2 finding narrows the target.** The finite witness reduces to test 2 (a non-monomial gate, H, which is
  candidate 2's swap image) together with the already sourced exchanges. It is still subject to test 8.

**Assumption-watch markers.**
- Π_ω's affinity, which carries the whole Lemma G gap.
- G1's calibration dictionary, used as if it were a carrier map.
- Q3's sign-only use of O1, true of the proof but not stated as a theorem.
