# FRONTIER — the missing arrows, each in its weakest clean theorem form

Base `b7af4852`. Only edges that are **not SEALED** in DEPENDENCY.md appear here. Each entry states the weakest
theorem that would close the arrow, what exists toward it, and its class. "Vocabulary" means the kernel has no
predicate in which to state the arrow; such arrows need a definition before a proof.

Ordering: the single-system state-space leg first (F1–F8), the effect/availability leg (F9–F12), the composite
leg (F13–F17), the identification leg (F18–F21), then the reverse-direction obligations (R1–R5).

***

## A. Single-system state-space leg

**F1 — an OI stage tower.** *Vocabulary + construction.*
`∃ D : DirectedStages` built from a finite reversible substratum with its observer actions (protocol tower PT, or
the lattice cone tower CT), with `SCInf D`. Toward it: `DirectedStages` (SC:63), `SCInf` (SC:78); cone lemmas
`RegionTower.iterate_dependsOnlyOn_ball` (RT:283), `card_fibre` (RT:398). Missing: the packaging, the
action-interleaved cone lemma, `extPerm` transitivity. Class: LEMMA (cheap; OI-STAGE note). Consequence recorded
there (NG1, written): for a finite substratum the body is a polytope, so **no infinite-order automorphism exists**
and every selector below is unsatisfiable at a finite stage.

**F2 — finite rank of the infinite-lattice completion.**
`FiniteRank (body D_CT)`. No theorem, no candidate rule with finite rank and a non-polytope body (OI-STAGE §3
exact ranks). Class: UNKNOWN (the open premise Main.md:542 names).

**F3 — chart-body compactness without `[FiniteDimensional ℝ V]`.** *Adapter.*
`∀ C : CompletionChart D, IsCompact (chartBody C) ∧ (interior (chartBody C)).Nonempty`.
`isCompact_bodyR`/`interior_bodyR_nonempty` (IIP:402/375) need the ambient space finite-dimensional, which
`CSpace D = lp (fun _ => ℝ) ∞` is not. Proof route: `chartBody C = chart⁻¹(body D)` is closed
(`isClosedEmbedding_chart`, CA:189; `body_isClosed`, CA:202) and bounded (an injective linear map from
`Fin d → ℝ` is bounded below; body coordinates lie in `[0,1]`); interior from `affineSpan_gen` (CA:218) and
`Convex.interior_nonempty_iff_affineSpan_eq_top`. Then IIP's `Fin n` form `invariant_inner_product` applies to
`chartBody C` directly. Class: ADAPTER.

**F4 — an AffineRespect operation datum from OI.** *Vocabulary + source.*
For the protocol tower: every OI action `a ∈ A ∪ {idle}` with prefix-closed effect protocols yields
`T_a : OpDatum D` with `AffineRespect T_a` and an inverse datum. Toward it: the label-map argument (OI-STAGE §5,
written + exact A1–A4). Class: LEMMA (conditional on PREFIX-CLOSURE, itself a modelling choice).

**F5 — ORD∞ ⇒ a continuous flow (Route Γ).**
`FiniteRank Ω → IsCompact Ω → (interior Ω).Nonempty → (∃ g ∈ Aut Ω, ∀ m ≥ 1, g ^ m ≠ 1) → ∃ flow : ℝ → Aut Ω,
additive ∧ continuous ∧ nontrivial on Ω`. Proof: closure of ⟨g⟩ in the compact group `Aut(Ω)` is a compact
abelian Lie group of positive dimension (Cartan), whose identity component is a torus. Class: LEMMA (standard;
Cartan not in Mathlib — a one-frequency Kronecker route through `DiscreteCompletion.dense_angles` (DC:518) is the
cheap partial). **Not needed if TRANS is the exact kernel predicate** (see F7).

**F6 — OFF: a non-normalizing second operation.**
`ElementaryDrivability.J_off_axis` is a separate premise: `not_boundaryTransitive_flow` (OG:620) shows one flow
alone is not transitive; Thread N X4 shows (dim 3, IIP) `J_off_axis ⇔ B a ∉ {±a}`. Class: PREMISE (no source).

**F7 — exact TRANS ⇒ boundary purity, ORD∞ and the ellipsoid (the bridge that collapses SELECT's C1/C2).**
Three statements, none in the kernel:
- (a) `BoundaryTransitive Ω G → PreservesBody Ω G → ∀ x, IsBoundaryState Ω x → x ∈ extremePoints ℝ Ω`
  (an affine automorphism of `Ω` and its inverse preserve extreme points; a boundary state in the relative
  interior of a face is not extreme; so if one boundary state is extreme all are — and on a compact convex body
  with interior some boundary state is extreme). Consequence: **`BoundaryTransitive` fails on every polytope of
  dimension ≥ 2**, the Level 3A octahedron included.
- (b) `BoundaryTransitive Ω G → PreservesBody Ω G → 2 ≤ dim Ω → ∃ g ∈ G, ∀ m ≥ 1, g ^ m ≠ 1`
  (the boundary is uncountable, so `G` is uncountable; an uncountable subgroup of `GL(d+1, ℝ)` is not torsion —
  torsion linear groups are locally finite (Schur) with an abelian normal subgroup of bounded index (Jordan),
  hence countable). Consequence: **ORD∞ is derivable from exact TRANS**; only the classical bit (`d = 1`,
  `G = {id, flip}`) survives without an infinite-order element.
- (c) `IsCompact Ω → Convex ℝ Ω → (interior Ω).Nonempty → BoundaryTransitive Ω G → PreservesBody Ω G →
  ∃ c R, Ω = {x | Q(x − c) ≤ R²}` with `Q` the IIP form (`invMatrix Ω`): every boundary state is
  `g x₀` for a `Q`-isometry `g` fixing `c`, so all lie on one `Q`-sphere, and Lemma B
  (`eq_closedBall_of_frontier_subset_sphere`, KF:770, after the LDL normalization of Thread N X1.3–1.5) closes it.
  **No drive and no DIM3 enter.**
Class: LEMMA (cheap for (a) and (c) given IIP-1; (b) needs Schur–Jordan or the closed-subgroup theorem).

**F8 — DIM3 from a single-system principle: {TRANS, EO} ⇒ DIM3.**
Weakest form (Thread R §3): `Convex Ω → IsCompact Ω → FiniteRank Ω → (nontrivial compact automorphism group) →
BoundaryTransitive Ω G → EnergyObservable Ω G → finrank (affineSpan Ω).direction = 3`, where
`EnergyObservable Ω G := ∃ φ : genAlg Ω G →ₗ[ℝ] Obs Ω, Injective φ ∧ ∀ X Y, φ ⁅X, Y⁆ = −(φ Y) ∘ X`. Needs the
definitions `genAlg`, `Obs`, `EnergyObservable` (absent) and, at step 8, the compact rank-1 classification
(citation). Class: LEMMA (citation-level) on UNKNOWN vocabulary. EO itself: PREMISE, unsourced (Thread R §5.4),
and INDEPENDENT of {DRIVE, TRANS, V4′, FR, compact} by the B⁴/Sp(1) exact countermodel.

## B. Effect / availability leg

**F9 — an availability vocabulary on the completed body.** *Vocabulary.*
A record `(eff : Set (W →ᵃ[ℝ] ℝ), trans : Set (W ≃ᵃ[ℝ] W))` on the chart with `SeqClosed` (`e ∈ eff → T ∈ trans
→ e ∘ T ∈ eff`) and `DriveAvailable`. Thread P's candidate `.lean.txt` is uncompiled. Without it V4′
(`SeedOrbitAvailable`, OG:74) is a proposition about an unconstrained set `avail`. Class: vocabulary (cheap).

**F10 — V4′ from SEED-AVAIL ∧ SEQ ∧ TRANS±.**
`r ∈ eff → SeqClosed → (∀ t, flow t ∈ trans) → J ∈ trans → J.symm ∈ trans → SeedOrbitAvailable (words …) r eff`.
Trivial given F9 (Thread P P-4). Class: LEMMA (trivial). Its premises SEQ and TRANS± have no source.

**F11 — LIMCLOSE-C.** *Vocabulary + premise.*
`∀ (T_n : OpDatum D), (∀ n, available T_n) → (∀ a x, T_n.τ x a → τ x a) → available τ`: availability closed under
pointwise probability limits on stage preparations. Used exactly once: to make the flow members obtained in F5
(limits of powers of `g`) *available* operations so that TRANS± in F10 holds for the continuum of `t`. The
sealed matrix witness `fixedGateTheory` (DC: `fixedGateTheory_denseUnitaryControl`, `fixedGateTheory_not_qm`)
shows limit closure does not follow from the rest. Class: PREMISE (INDEPENDENT at matrix level).

**F12 — mixtures of available effects are available; the directional family generates the full effect cone.**
Needed to pass from `directionalFamily` (OG:205) to NB-1's "full self-dual effect cone". Elementary
(every effect on `ball3` is a convex combination of `0`, `1` and sharp directional effects) but no kernel
statement, and operational availability of mixtures is a closure premise (matrix analogue: `avail_coarse`).
Class: LEMMA (geometry) + PREMISE (availability of mixtures).

## C. Composite / G-layer leg

**F13 — composite existence and local tomography, field-neutrally.** *Vocabulary.*
A body `Ω_AB ⊆ V_A ⊗ V_B` with `Ω_A ⊗ Ω_B ⊆ Ω_AB ⊆` the maximal tensor body, product effects separating states.
Absent. `local_tomography_physical` (InstrumentDilation:440) is a theorem *about* `Matrix (A × B) (A × B) ℂ`
and cannot source LT (anti-circularity). Class: PREMISE.

**F14 — existence of a nonlocal reversible `G` with the native CNOT relations.**
Nothing single-system supplies it (`fullAut3`, `ball3Drive` act on one ball). Class: PREMISE. Deletion of the
control-NOT relation: INDEPENDENT (C5, exact). Deletion of `G⁻¹` positivity: UNKNOWN (NB-1 open item).

**F15 — identical-copy covariance (common `N`).**
`CopyNatural N_A N_B e` (KF:284) is defined; no source. Two-NOT countermodels at `d = 5` (NB-1 C2N) and `d = 7`
with both NOTs continuously interpolable (K∞ §6). Class: INDEPENDENT (exact), PREMISE. Candidate weakening
(ROADMAP K∞): type covariance of native inversion; untested.

**F16 — NB-1 for general `d` in the kernel.**
S1 (controlled form), S2 (block structure), S4 value identity are written for all `d` and exact for `d ≤ 7`.
Class: LEMMA (written).

**F17 — K2: the composite is the quantum tensor product; the CP/antiunitary bridge; functoriality of
composition.** ROADMAP K2 OPEN; no governed round. Class: UNKNOWN.

## D. Identification leg

**F18 — Bloch adapter.** `ball3` with `directionalFamily` ≅ qubit density matrices with effects
`0 ≤ E ≤ 1`; drive words `SO(3)` ≅ `U ↦ U·U†` for `U ∈ SU(2)`. Standard; absent. Class: ADAPTER.

**F19 — composite-level drives from the single-system drive.**
`PhaseFreeRichness T` (MR:423) quantifies over every level `A × Fin n`; nothing in the single-system leg supplies
the level-`n` driven pair. `five_way_minimality` (RankGapTheory) shows `HasCompositeUnitaryControl` is
independent of the other four conditions and of the OI core, and `control_of_phaseFree` (MR:529) needs
`IteratedAncillaClosure` at carriers with ≤ 2 states. Class: PREMISE (the (iv)-type condition of GR §3.3 in its
smallest form, GR.md:262–270: one layer flow executable, plus the phase intervention).

**F20 — implementation locality and embedded observation from the field-neutral layer.**
`ImplementationLocality` (IL:370), `EmbeddedObservation` (EmbeddedObservation:123) are matrix-level predicates.
No field-neutral counterpart. Class: PREMISE (OI-plausible: the OI-STAGE tower is label-invariant and
regrouping-invariant by construction, but that is unformalized).

**F21 — orientation.** `operational_orientation_noGo` (OrientationSelection:139) shows the antiunitary branch is
not removable by operational data; GR.md:206–210 names the oriented premise (passivity / `counting_passive`).
Class: PREMISE (ℤ₂^anti remains unless an oriented condition is added). Relative-evolution determination (P0):
OPEN.

## E. Reverse-direction obligations (QM ⇒ premise), kernel-unresolved

**R1** EO for the qubit: hat map `so(3) ≅ ℝ³` equivariant — off-repo exact only.
**R2** ORD∞ and OFF-Γ′ for `ball3Drive`: `rot3 1` has infinite order; `cyc3` does not normalize the circle —
elementary, unlanded (DRIVE G1–G2 exact).
**R3** A QM `DirectedStages`: stages of grid pure states/effects with the trace table, SC∞ by inclusion,
`FiniteRank` (rank 3), phase and Clifford `OpDatum` with `AffineRespect` — DRIVE §1.2–1.4 (written + exact);
only the classical `bitTower` is in the kernel.
**R4** LIMCLOSE-C for QM operations — standard, unlanded.
**R5** NB-1 hypotheses for two qubits (common `N = diag(1,−1,−1)`, CNOT, two-sided positivity) — probe C3, exact,
unlanded.
