# NOTES-O3 — the Continuous Origin

Thread `research/origin`, node O3. Base L = `9f9f8257`. Evidence levels as in NOTES-O1. Script:
`experiments/o3_continuous.py` (11 checks, 4 countercontrols; decision rule in the header before run 1; one
pre-run edit — the closure search depth of C5 raised from 12 to 24 — before any run; green on run 1,
byte-identical on replay).

**Productivity test, fixed before starting (§A.31).** A finding counts only if it locates the one-parameter
family's premise more sharply than "K∞-Drive is open", and either relates the Discrete and Continuous targets
exactly or constrains what any source of the drive must also supply.

## 0. Verdict

1. **Matrix level: the Continuous target reduces to the Discrete one, given the substratum's phase continuum.**
   The substratum class contains every diagonal unitary (its phase interventions, a stipulation of the
   interface: PhaseSource T4, GR.md:260). Conjugating that continuum by one exactly available balanced mixer on a
   moved pair gives the transition flow at every angle, exactly: H·diag(e^{−it}, e^{it})·H = e^{−itX} [X C1a];
   with the gate flow and the quarter phase on three points, the flow on the moved pair with the third point
   fixed [X C1b]. Relative to the baseline the substratum theory satisfies (`DerivedOI ∧ SubstratumAvail`), exact
   finite quantum mechanics is therefore equivalent to each of: one executable layer flow (Q4′, kernel),
   phase-free richness (kernel), and **one exactly available balanced mixer on a moved pair at every level**
   (this thread). The one-parameter family is supplied by the phase continuum; the only missing content is a
   single non-monomial operation per level — the Discrete target — which O1–O2 show is not sourced.
2. **The two targets, exactly.** Continuous ⇒ Discrete always: the drive's member at a quarter of the NOT time
   is a balanced mixer [X C2a], and on any body a continuous flow whose NOT swaps two pure frame states with a
   complemented readout passes through a balanced pure state (intermediate values) [W + X C2b]. Discrete ⇒
   Continuous at the matrix level given the phase continuum (item 1). Discrete ⇏ Continuous with the quarter
   phase only (a balanced mixer and S generate the 24-element rotation group of the cube [X C5]; the kernel's
   fixed-gate theory is not quantum mechanics at any angle) and field-neutrally (the KB-D octahedron's
   reversible group has order 24 [X C4]). So "deliberately weaker" holds exactly where the phase continuum is
   absent.
3. **Field-neutral: a drive through the native NOT needs invasive observation.** If the native readout is
   passive and repeatable — as in every tower built by conditioning a classical substratum — every pure state
   is outcome-deterministic for it (Lemma P), so no drive's NOT can swap two pure frame states of that readout,
   whatever operation data are added (OPS-Γ, LIMCLOSE-C, imported unitaries). The field-neutral Continuous
   Origin therefore needs an observation-side change, not only operation data.
4. **What remains for `oiPlusMin_iff_qm` once a drive is sourced at level one:** its availability at every
   level, which is its spectator extension [X C6], and the structural closure (context stability) of a
   generating class containing it — both the drive's spectator stability, the matrix form of the bridge
   thread's (b). Then `derivedOI_qm_iff_phaseFree` / `sourcedOI_qm_iff_phaseFree` and `oiPlusMin_iff_qm` give
   exact finite quantum mechanics. Given the phase continuum, the spectator content needed reduces to that of
   **one** balanced mixer (§4).

## 1. The premise that supplies the one-parameter family (matrix level)

**Kernel facts at L.**
- `oiPlusMin_iff_qm` [K MinimalRepertoire.lean:569]: `OIPlusMin T ↔ ExactAllFiniteEndomorphicQuantumOps T`, where
  `OIPlusMin = ImplementationLocality ∧ PhaseFreeRichness ∧ EmbeddedObservation` [K :544] and
  `PhaseFreeRichness` asks, at every level with two or more states, for one pair driven at every time by
  `flow (transition a b) t` together with every exchange [K :423].
- Under the closure, quantum mechanics is exactly phase-free richness: `derivedOI_qm_iff_phaseFree`
  [K RouteB.lean:161], and without the phases `sourcedOI_qm_iff_phaseFree` [K SubstratumInterfaceAudit.lean:654];
  the sourced theory satisfies `SourcedOI` (`permTheory_sourcedOI` [K :660]).
- Relative to the substratum's availability, quantum mechanics is exactly the executability of one layer flow:
  `derivedOI_qm_iff_layerFlowExecutable` [K LiftAudit.lean:812], via `phaseFree_of_layerFlowExecutable`
  [K :783], whose isolation identity uses the substratum's diagonal phases (`diagonal_avail` [K :754]).
- The substratum theory satisfies the baseline (`substratumTheory_derivedOI` [K RouteB.lean:290],
  `substratumTheory_substratumAvail` [K LiftAudit.lean:750]) and does not execute any layer flow
  (`substratumTheory_not_layerFlowExecutable` [K :200]).

**New equivalent (T-O3a).** For T with `DerivedOI T ∧ SubstratumAvail T`: exact finite QM ⟺ at every level n ≥ 1
some balanced mixer B_n on a moved pair (a, b) (|⟨a|B_n|a⟩|² = |⟨b|B_n|a⟩|² = 1/2, acting as the identity off
the pair) has its conjugation available.
*Proof.* (⇐) Every balanced 2×2 unitary is B = D₁HD₂ with diagonal unitaries D₁, D₂ [W]. With D_t =
diag(e^{−it}, e^{it}) on (a, b) and 1 elsewhere: D₁†·B·D_t·B†·D₁ = H·D_t·H = the transition flow at angle t on
(a, b) [W; X C1a for H, C1b for the gate flow with S]. No inverse is assumed: B† = E·B·E with E = D₂†D₁† diagonal.
The diagonal factors are available by `diagonal_avail`, products by `avail_conj_mul` [K LiftAudit.lean:770], the
exchanges by `SubstratumAvail`; hence phase-free richness, hence QM by `derivedOI_qm_iff_phaseFree`. (⇒) QM has composite unitary control (`physical_of_exactAll`
[K PhysicalCharacterization.lean:301]), which makes every unitary available, the balanced ones included. ∎ Status: CONDITIONAL ([W] + [X]; the general balanced
B needs the diagonal correction spelled out — every balanced 2×2 unitary is D₁HD₂ with diagonal unitaries D₁, D₂
[W] — no kernel check).
**Reading.** The substratum class already holds a continuous one-parameter group — the phases about the frame
axis, `phaseOperator` [K SubstratumInterface.lean:83] — monomial and coherence-free. What it lacks is one
operation that does not preserve the frame. The Continuous Origin at the matrix level is that operation plus its
spectator form, nothing more.

## 2. Continuous ⇒ Discrete, and the converse

- **C2 [X + W].** `flow (transition a b) (π/4)` = (1 − iX)/√2 is balanced and non-monomial, with the owner's
  witness (1, 1/2) [X C2a]. Field-neutrally, for any `ElementaryDrivability` whose NOT swaps two pure frame states
  of a readout r with r∘N = 1 − r: s ↦ r(flow(s)ω₀) is continuous (`flow_continuous`), equals 1 at s = 0 and 0
  at s = t₀, so some flow member maps ω₀ to a balanced state, which is pure because flow members are body
  automorphisms; the witness then holds with the inverse member and the frame dephasing [W]. Exact on the
  `ball3Drive` geometry [K KInfFoundations.lean:449]: R_z(π/2) maps x+ to y+ (r = 1/2), r∘N = 1 − r for
  N = R_z(π), sandwich (1, 1/2) [X C2b].
- **Discrete ⇏ Continuous.** With the quarter phase only, H and S (or the kernel's `rot(π/4)` and S) generate the
  24-element rotation group of the cube on the Bloch sphere [X C5]: no infinite-order element, no drive; the
  kernel's `fixedGateTheory α` satisfies `DerivedOI` and `FixedGateSourced α` and is not QM at any angle
  [K DiscreteCompletion.lean:1929, 1933, 1948]. Field-neutrally the KB-D toy has a discrete balanced mixer and a
  reversible group of order 24 acting faithfully on its six pure states [X C4]; a polytope has finitely many
  automorphisms, so no drive [W].
- **Irrational angles [X C7 + K].** A fixed mixer at an irrational angle (cos t = 3/5; its powers are never scalar
  up to k = 200, and t/π is irrational by Niven's theorem [L]) gives dense unitary control under `DerivedOI`
  (`denseUnitaryControl_of_fixedGate` [K DiscreteCompletion.lean:1522]) but not exact QM (density is not
  exactness, `fixedGateTheory_not_qm`); it is unbalanced (sandwich (1, 337/625)), so it does not meet the owner's
  exact witness, while the balanced member has finite channel order (4). With the quarter phase only, the exact
  witness and density pull apart; the phase continuum reconciles them (C1).

## 3. Field-neutral: Lemma P and what it forbids

**Lemma P [W].** Let Ω be a convex set of states and r a readout whose native observation is
(i) *repeatable* — after outcome v the state ω_v has r(ω₀) = 1, r(ω₁) = 0 — and
(ii) *passive* — p₀(ω)ω₀ + p₁(ω)ω₁ = ω for every ω (observe-and-forget is the identity).
Then every extreme point of Ω has r ∈ {0, 1}.
*Proof.* An extreme ω with 0 < p₀(ω) < 1 would be the proper mixture p₀ω₀ + p₁ω₁ of two distinct states
(their r-values differ). ∎
**Corollaries.** (P1) No body automorphism maps a pure frame state to a balanced state: no balanced coherent
mixer for the native frame, whatever its source. (P2) No `ElementaryDrivability` whose NOT swaps two pure frame
states of the native readout: the flow would pass through a balanced pure state (§2). (P3) The owner's witness
is impossible for the native frame.
**Where it applies.** Every protocol tower built by conditioning a classical substratum: the native readout is
the visible value, conditioning is repeatable, and observe-and-forget is idle (OI-STAGE A5 [A]) — on the
completed body too, by continuity [W]. Exact illustrations: the classical tower is passive with deterministic
pure states [X C3a]; the KB-D tower and the ball with its Lüders readout are not passive, and both carry
balanced pure states [X C3b, C3c].
**Relation to the corpus.** NG2 (OI-STAGE §7) excludes strictly convex bodies for passive towers with a
reversible step and finite rank; Lemma P needs neither, constrains the native frame rather than the global
shape, and covers every added operation. It is the body-level, single-readout form of
`complete_passive_iff_commutative` (CentralObservation, cited in OI-STAGE) and of the information–disturbance
principle in generalized probabilistic theories [L, e.g. Pfister–Wehner, Nat. Commun. 4, 1851 (2013), not read].
**Consequence for K∞-Drive (assumption-watch marker).** DRIVE's weakest premise OPS-Γ (an infinite-order
AffineRespect datum g and an OFF partner J on a finite-rank completed body [A drive/RESULT.md §2.3]) cannot be met
through the native NOT on any passive OI tower. A field-neutral Continuous Origin must change the observation
law (invasive, record-writing observation of the kind NG2 already required), and the operation data alone cannot
supply it. Together with NG1 (finite substrata give polytopes) and RANK (the lattice completions tested have
growing rank), the field-neutral drive is OPEN with three named needs: finite rank of an infinite-substratum
completion, an infinite-order stage-crossing datum with OFF, and invasive observation.

## 4. What remains for `oiPlusMin_iff_qm` once a drive is sourced

Suppose a premise supplies, at level one (the system carrier), the conjugation by `flow (transition a b) t` for
every t — or, by §1, one balanced mixer on a moved pair.
1. **The drive at every level.** Phase-free richness asks for a driven pair at every level n. The kernel's
   executable form is `LayerFlowExecutable`: the gate flow of `levelPerm σ n = σ × id`, i.e. the level-one flow
   tensored with the identity on the ancilla — exactly its spectator extension [X C6]. Inside `DerivedOI` the
   all-level quantifier is redundant given level one plus `HasParallelReferenceExtension` [A stage 5 D5 N1c]: the
   content is relocated to a spectator clause, not removed.
2. **The theory containing the drive must keep the closure.** `SourcedOI` asks for reversible implementation
   locality (a context-stable, label-invariant, dagger-stable generating class), embedded observation, the
   exchanges and the read-write operators. The exchanges and read-write operators are supplied by the substratum
   (`permTheory_sourcedOI`); embedded observation holds for the generated theory of a label-invariant
   architecture (`genTheory_embeddedObservation` [K ImplementationLocality.lean:904], used in `permTheory_sourcedOI`); context stability of a class
   containing the drive is a hypothesis — a theorem only for the monomial class (`substratumClass_contextStable`
   [K StructuralClosure.lean:261]) [A stage 5, row β].
3. **Reduction to one discrete operation [W].** If the generating class contains the substratum class (whose
   context stability is a theorem) and one balanced mixer B with 1_R ⊗ B admissible for every R, then
   1_R ⊗ flow(t) = (1_R ⊗ B)(1_R ⊗ D_t)(1_R ⊗ B)† with D_t diagonal is admissible by the architecture's product
   closure: the drive's spectator stability follows from the spectator stability of the single discrete mixer.
Then `derivedOI_qm_iff_phaseFree` (or `sourcedOI_qm_iff_phaseFree`) and `oiPlusMin_iff_qm` yield
`ExactAllFiniteEndomorphicQuantumOps T`. **What remains is therefore exactly the spectator stability of the
sourced operation** — the matrix-level form of the bridge thread's (b) (NOTES-O4).

## 5. The minimal added content and its disguise test

| setting | minimal added content (beyond the substratum theory's availability) | disguise test |
|---|---|---|
| matrix, with the phase continuum | one balanced mixer on a moved pair, available with its spectator form at every level (§1, §4) | any instance known at L carries the coherence in its input (O2 G1–G4): FAILED as a source; underived otherwise |
| matrix, kernel's own forms | one executable layer flow (Q4′) / phase-free richness / the state-mixing datum at every angle (`mixTheory_qm` [K StateMixingCoupling.lean:511]) | each is a complex one-parameter unitary group or a postulated datum containing the balanced mixer (§2): FAILED as a source |
| field-neutral | OPS-Γ on a finite-rank completion of an infinite substratum + invasive repeatable observation (Lemma P) | OPS-Γ names no flow, parameter or continuity (DRIVE §6) and passes syntactically; it cannot be met through the native NOT on passive towers; its source is OPEN |

## 6. Classification (§A.31)

- **NEW, O3-N1.** Given the substratum's phase continuum, one exactly available balanced mixer per level is
  equivalent to the Continuous Origin at the matrix level (T-O3a); the owner's "deliberately weaker" holds exactly
  where the continuum is absent (quarter phase only; field-neutral).
- **NEW, O3-N2.** The spectator content that `oiPlusMin_iff_qm` still needs reduces, given the phase continuum, to
  the spectator stability of one discrete operation (§4.3).
- **ELABORATING with cross-propagation, O3-E1.** Lemma P: passive repeatable observation makes the native frame's
  pure states outcome-deterministic; hence no drive through the native NOT on passive towers (assumption-watch
  marker for K∞-Drive/OPS-Γ).
- **CONFIRMING, O3-C1.** Q4′, phase-free richness and the fixed-gate theory's density-without-exactness, as landed.
