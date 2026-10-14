# Thread A — the exact finite target statement for F1, and its hypothesis list, pinned at M

**Base.** M = `5bfdaba61b535e2fff83d8ba68e73a1b9dbc5dc5` (merge of #844). Every `file:line` is at M, read by grep in a
detached worktree at M; Lean paths are under `verification/lean-mathlib/OIBridge/` unless a path is given. ROADMAP =
`verification/ROADMAP.md` at M; PROGRAMME = `verification/programmes/oi-qm/PROGRAMME.md` at M. Lean was not compiled
here. A [K] label rests on the module being in the M aggregate (`OIBridge.lean`) under its landed round's receipt
(`verification/receipts/*.json`). For example, `OI-PAIR-MAXCONE-1.json` has `"status": "complete"`, E `6a7696a0`, and
its exact-head run 38253938894 is the one the receipt records.

**Labels.** [K] kernel theorem or definition at M; [D] design module on a disposable/research branch, not certified
(branch and run as recorded there, not re-run here); [W] written argument; [X] exact computation (where it lives is
given); [U] unsourced. Status words in table (b):

- *derived*: a [K] theorem from OI objects at M;
- *conditional*: a [K] theorem from other rows of the table;
- *introduced*: a named kernel predicate at M that is assumed and has no source theorem;
- *no predicate*: no kernel object at M (ROADMAP's GAP);
- *Independent-verdict*: a countermodel or no-go shows the resource does not follow from the stated OI architecture
  (PROGRAMME §6:551–553).

This is research only. It changes no status and proposes no manuscript text. The research ledger
(`origin/research/equivalence:research/equivalence/LEDGER.md`, base 9f9f8257) served only as a map. Every citation
below was re-located at M.

***

## (a) The target statement

### a.1 What has to move from the premises to the conclusion

The certified finite characterizations all take complex matrix kinematics as given in their types:

- `oiPlus_iff_qm` CarrierGeneralOIPlus.lean:207, over `FiniteOperationalTheory A` (OperationalAssembly.lean:594),
  whose operations act on `Matrix A A ℂ`.
- `genTheory_qm_of_quantumArchitecture` SubstratumSource.lean:136, over an `ImplementationClass`
  (ImplementationLocality.lean:244), a predicate on `Matrix S S ℂ` at every finite `S`.
- `typed_determined_iff` TypedCompletion.lean:850, over a `TypedOperationalTheory` (:165).

F1 (PROGRAMME §5:519–523, "`OI + explicitly justified physical conditions <-> target QM`") is reached only when the
kinematics is in the conclusion. The target below therefore has its premises over field-neutral objects (the K-route
vocabulary) and its conclusion over the matrix objects.

### a.2 Objects

- **𝒬, the target theory: finite, typed, exact operational QM.**
  - Typed form: a `TypedOperationalTheory 𝒯` with `𝒯.ShadowQuantum` (TypedCompletion.lean:291). By
    `typed_determined_iff` [K] :850, this holds iff `availT S S' (Fin m) F ↔ IsTypedKrausInstrument F` (:448) for all
    nonempty finite `S, S'`.
  - Endomorphic and composite form: `ExactAllFiniteEndomorphicQuantumOps` LevelOneSeam.lean:186. This is
    `ExactFiniteEndomorphicQuantumOps` (KrausSoundness.lean:134) together with `ExactCompositeQuantumOps`
    (AncillaClosure.lean:364): every positive composite `A × Fin (k+1)` carries exactly the Kraus instruments.
  - The full theory exists: `fullClass` (ImplementationLocality.lean:374), `fullClass_quantumArchitecture` [K]
    SubstratumSource.lean:151, `shadowQuantum_of_typed` [K] TypedCompletion.lean:838.
  - **Scope of 𝒬:** finite carriers; typed, i.e. rectangular Kraus; operational availability; composites included as
    system × ancilla of every finite size. Excluded: quasilocal, continuum and continuous time (see (e)).
- **𝔒, an OI observer model. No bundled kernel object at M (missing link M0).** The components that exist at M:
  - per system type τ, a `DirectedStages` (StageCompletion.lean:63) of `FiniteStage`s (KInfFoundations.lean:63);
  - its completed `body` (StageCompletion.lean:141), a `CompletionChart` (CompletionAction.lean:144) and the
    `chartBody` (:166);
  - available tests, a set of affine functionals on the chart;
  - reversible operation data, pairs of `OpDatum` (:46) with `AffineRespect` (:58) that `Undoes` each other (:325),
    whose induced family is `G τ := {inducedEquiv …}` (:333);
  - for a pair of types, a `Composite` (CompositeInterface.lean:243) and a pair cone `K ⊆ W 3` (CompositeDimension.lean:97).

  Missing at M:
  - a type system with ⊗;
  - any structure with ≥ 3 tokens (ROADMAP K2 :1010–1018; the ledger's "no structure with three or more tokens" holds at M);
  - typed operations between types;
  - field-neutral attach, discard and readout;
  - an isomorphism notion `OpIso 𝔒 𝒯`.
- **ℛ, an OI realization.**
  - A `Substratum` (SubstratumInterfaceAudit.lean:60) with `A1 := Finite Conf` (:84) through `A5` (:102), and the
    adopted `A6Cov` (BackgroundIndependence.lean:131, identically true by `a6cov_all` :161).
  - An observation map `Obs`, an ensemble `μ`, and a protocol menu.
  - The induced observer model `observerOf ℛ` has no kernel object (missing link M1). The only observer theory
    built from a substratum at M is the configuration-level `permTheory` (SubstratumInterfaceAudit.lean:606), which is
    a matrix-level `FiniteOperationalTheory`, not a `DirectedStages`.

### a.3 F1-fin — statement

Let **Hyp** be the conjunction of rows H0–H28 of table (b), with the elementary-scoped rows quantified over the types τ
with `Elem τ`.

**(→) Forward.** For every OI realization ℛ and every admissible `(Obs, μ)`:

> Hyp(observerOf ℛ) ⟹ ∃ 𝒯 : TypedOperationalTheory, 𝒯.ShadowQuantum ∧ OpIso(observerOf ℛ, 𝒯).

Here `OpIso` assigns a finite carrier `S_τ` to each type with `S_{τ⊗σ} ≃ S_τ × S_σ`, and identifies:

- `chartBody` with the density matrices on `ℂ^{S_τ}`, affinely;
- the available tests with `{ρ ↦ tr(Eρ) : 0 ≤ E ≤ 1}`;
- the available typed instruments with `𝒯.availT`.

In particular each elementary type has chart dimension 3 and is affinely the Bloch ball.

**(←) Backward, operational.** The full typed quantum theory 𝒬, read as an observer model `obs(𝒬)`, satisfies Hyp, and
`OpIso(obs(𝒬), 𝒬)` holds.

**(←) Backward, OI-realization.** For every finite horizon N there is an OI realization ℛ_N with
`OpIso_{≤N}(observerOf ℛ_N, 𝒬)` and Hyp(observerOf ℛ_N).

- It is stated finite-horizon because the all-time form is already refuted at the rooted-law level:
  `qStar_not_subset_pper` [K] QuantumRepresentationT2.lean:169 gives a fixed-basis Born family on `Fin 2` outside
  `PPer`, and `PPer` is exactly the OI-realizable class (`finiteRootedRealizable_iff_pper` [K]
  RootedClassificationAllTime.lean:192).
- At the law level the finite-horizon form holds: `finite_horizon_equivalence` [K] Equivalence.lean:459 (S ⇔ D ⇔ Q_fb).
- No theorem treats the operational repertoire.

Read as an equivalence: the class {observerOf ℛ : Hyp} equals, up to `OpIso`, the class of finite typed QM theories.
Each direction needs its own witness (§A.34), and **neither exists at M**.

**Register sub-target F1-reg.** Types are k-token registers of one elementary type, and the carriers are `Fin (2^k)`.
It drops H26 and is strictly weaker than F1-fin. It is the natural first closable form, since every certified
composite theorem at M is about tokens of the one elementary type.

### a.4 Lean-style sketch over kernel objects at M (new objects marked `-- NEW`)

```lean
import OIBridge   -- aggregate at M
open OIBridge StageCompletion CompletionAction KInfFoundations OrbitGeneration OrbitNormalization
open TransitiveBody DenseOrbit EffectSpace SharpTests CompositeDimension CompositeInterface K1Bridge K2Guard
open EqvK2Schema EqvK2Block EqvK2MaxCone ImplementationLocality SubstratumSource TypedCompletion

structure ObserverModel where                                  -- NEW (M0)
  Typ   : Type
  Elem  : Typ → Prop                                           -- NEW (H4: elementary-system scope)
  D     : Typ → DirectedStages                                 -- StageCompletion.lean:63
  C     : ∀ τ, CompletionChart (D τ)                           -- CompletionAction.lean:144
  avail : ∀ τ, Set ((Fin (C τ).d → ℝ) →ᵃ[ℝ] ℝ)                 -- tests in chart coordinates
  ops   : ∀ τ, Set (OpDatum (D τ) × OpDatum (D τ))             -- :46, each pair AffineRespect (:58) + Undoes (:325)
  prod  : Typ → Typ → Typ                                      -- NEW
  comp  : ∀ τ σ, Composite (chartBody (C τ)) (chartBody (C σ)) (PairV τ σ)   -- CompositeInterface.lean:243
  K     : ∀ τ σ, Set (W 3)                                     -- pair cone, once M4 identifies PairV with W 3
  availT : TypedAvail Typ                                      -- NEW (H28): typed operations between types

def OIRealization := SubstratumInterfaceAudit.Substratum × ObsData × Ensemble × Menu   -- NEW packaging
def observerOf : OIRealization → ObserverModel                                       -- NEW (M1)
structure OpIso (𝔒 : ObserverModel) (𝒯 : TypedOperationalTheory) : Type             -- NEW (M0)

structure Hyp (𝔒 : ObserverModel) : Prop where                -- rows of table (b)
  scInf  : ∀ τ, SCInf (𝔒.D τ)                                                    -- H1  :78
  rank   : ∀ τ, FiniteRank (body (𝔒.D τ))                                        -- H2  :299
  bin    : ∀ τ, 𝔒.Elem τ → Nonempty (BinaryVisible (𝔒.D τ))                      -- H3  :244
  drive  : ∀ τ, 𝔒.Elem τ → Nonempty (ElementaryDrivability (chartBody (𝔒.C τ)))  -- H7  KInfFoundations:264
  trans  : ∀ τ, 𝔒.Elem τ → BoundaryTransitive (chartBody (𝔒.C τ)) (G 𝔒 τ)       -- H8  OrbitGeneration:79
  v4     : ∀ τ, 𝔒.Elem τ → ∃ r, SeedOrbitAvailable (G 𝔒 τ) r (𝔒.avail τ)        -- H11 OrbitGeneration:74
  not_   : ∀ τ, 𝔒.Elem τ → ∃ z N, IsNot (normalized τ) z N                         -- H15 CompositeDimension:210
  gate   : ∀ τ, 𝔒.Elem τ → ∃ z N T, NativeGateOf (normalized τ) (navail τ) z N T   -- H17 K1Bridge:49
  pairH1 : ∀ τ σ, ∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ 𝔒.K τ σ          -- H20
  cnotI  : ∀ τ σ, ∀ ω ∈ 𝔒.K τ σ, cnot ω ∈ 𝔒.K τ σ                                -- H23 CompositeDimension:775
  aMiss  : ∀ τ σ t, ∀ ω ∈ 𝔒.K τ σ, actT (rotLin t) ω ∈ 𝔒.K τ σ ∧ actT cycEquiv ω ∈ 𝔒.K τ σ  -- H24
  -- … every remaining row of table (b)

theorem F1_fin_forward (ℛ : OIRealization) (h : Hyp (observerOf ℛ)) :
    ∃ 𝒯 : TypedOperationalTheory, 𝒯.ShadowQuantum ∧ Nonempty (OpIso (observerOf ℛ) 𝒯)   -- NEW
theorem F1_fin_backward_op : Hyp (obsModel fullTyped) ∧ Nonempty (OpIso (obsModel fullTyped) fullTyped)  -- NEW
theorem F1_fin_backward_OI (N : ℕ) :
    ∃ ℛ, Hyp (observerOf ℛ) ∧ Nonempty (OpIsoUpTo N (observerOf ℛ) fullTyped)          -- NEW

/- Forward skeleton: the [K] links in order, with the missing ones marked.
  per elementary τ:
    ⟨C⟩      := exists_completionChart hne h.rank                     -- CompletionAction.lean:154
    hG       := preservesBody_inducedEquiv …                          -- CompletionAction.lean:352 (H6)
    ⟨A, hA⟩  := chartBody_eq_eball hd hG (h.trans τ)                  -- TransitiveBody.lean:651
    hyp      := hypotheses_tr A hG hSeed (h.trans τ) hV4             -- OrbitNormalization.lean:295
    hcone    := maxConeOf_avail_eq hd hyp.1 hyp.2.1 hyp.2.2.1 hyp.2.2.2 hE   -- EffectSpace.lean:572
    hd3      := three_of_nativeGateOf_of_two_le h2 hE … hN hT          -- K2Guard.lean:253  ⇒ C.d = 3
  per pair (after M3, M4):
    hK       := pairCone_eq_Q3_of_sharp_available hH1 hadd hsmul hvalid hsharp hH2 hA  -- EqvK2MaxCone.lean:204
    -- Q3 = {ω | (dict ω).PosSemidef} (EqvK2Schema.lean:239); dictEquiv : W 3 ≃ₗ[ℝ] Herm(ℂ²⊗ℂ²) (:216)
  registers / all carriers:  hq : QuantumArchitecture 𝓘 := ?Kn        -- MISSING (M6, M7)
  matrix endpoint:  genTheory_qm_of_quantumArchitecture hq            -- SubstratumSource.lean:136
  typed endpoint:   typed_determined_iff                               -- TypedCompletion.lean:850
  identification:   OpIso (observerOf ℛ) 𝒯 := ?id                     -- MISSING (M7) -/
```

### a.5 Composites and Bell correlations — what the target includes, and what covers correlations

**The target includes composites.** It must, for two reasons:

- PROGRAMME §2 B (:52–56) puts composites inside "quantum operational repertoire".
- The certified endpoint `ExactAllFiniteEndomorphicQuantumOps` already carries `ExactCompositeQuantumOps` on every
  `A × Fin (k+1)`. Dropping composites would make the target weaker than the theorem it is meant to source.

**On the QM side, correlations are a consequence of the target, not a premise.**

- Exactness on a composite carrier makes every Kraus instrument available. That includes entangled preparations,
  through `pureSeedPrep_available_of_swap` OperationalAssembly.lean:675, and local instruments, through `withSpectator`
  and `InertSpectatorCompositionality` (SpectatorBridge.lean:223). So the bipartite quantum correlation set, up to
  Tsirelson, is realized [W, standard].
- At the K2 level the conclusion `K = Q3` contains the Bell table: `cnot (prodState xplus z3) = phiW` [K]
  CompositeDimension.lean:1222, and `phiW` is not a product [K] :1232.

**On the premise side, nothing derives correlations.**

- The entangling content enters through rows H23 (CNOT invariance of the pair cone), H17/H18 (the native gate, the
  entangling clause) and H24. All are introduced.
- ROADMAP :1018: "K2 does not discharge H-Bell."

**On the OI-realization side (the (←OI) direction and M1 for composites), the result is a constraint, not a theorem.**

- Every finite Bell record, read as one rooted law of the joint outcome carrier, has some finite reversible
  realization [K] (`finite_horizon_equivalence`). That realization carries no two-wing spatial structure.
- With spatially separated wings, Main.md's Bell ceiling [W] (papers/Main.md:362–371) applies: deterministic dynamics,
  local setting interventions, readout before the cones meet and one setting-independent ensemble give |S| ≤ 2.
- So an origin map M1 that yields spatially local composites with Q3 pair cones must relinquish ontic parameter
  independence or measurement independence. The manuscripts adopt preparation-indexed state-dependent adjacency
  (Main.md:394), which is unsourced.
- H-Bell (no-signalling and Ollivier–Ricci stability of that graph family, ROADMAP :954–969) is a further,
  gravity-side condition outside this finite target.

**My view.** The finite target covers Bell correlations operationally, by exactness, conditional on the introduced
composite rows. It does not cover their physical realization by the substratum. A Bell-inclusive claim is either
stated non-spatially (the joint record as one finite law) or carries ontic parameter dependence as an additional named
premise. Thread E should decide which reading the owner wants.

***

## (b) The hypothesis table

Abbreviations: Trans(G) := `BoundaryTransitive`; nchart := the chart body after `chartBody_eq_eball` and
`hypotheses_tr`. "Consumed by" names the [K] theorem at M whose hypothesis it is, or the missing link (M#) that would
consume it.

| id | hypothesis (precise) | kernel object at M | status | evidence | consumed by |
|---|---|---|---|---|---|
| H0 | **Origin.** `observerOf ℛ` is defined for each OI realization ℛ and each admissible `(Obs, μ)`. The target quantifies over admissible `(Obs, μ)`; it does not select one. | no predicate | no predicate | ROADMAP SOI row :69 OPEN; `ensemble_underdetermined` [K] StochasticInterface.lean:118 (the invariant ensemble is not unique under A5); PT-STAGE-1 is only a draft (`origin/draft/pt-stage-1`, no design module) | M1 |
| H1 | SC∞: every stage map carries the table, `∀ i j (h : i ≤ j), (D.map h).Consistent` | `SCInf` StageCompletion.lean:78 | introduced | CMP-1 states it and proves it for no OI construction (only `bitTower_scInf` :401 on a control tower) | `val_eq_at` :117, `sharpSeed_completion` :224, `perfectlyDistinguishable_visible` :274 |
| H2 | Finite rank: `FiniteDimensional ℝ (affineSpan ℝ (body D)).direction` | `FiniteRank` StageCompletion.lean:299 | introduced | [W]+[X] (research archive, not re-run): automatic for finite Ω, fails on an infinite carrier | `exists_completionChart` CompletionAction.lean:154 |
| H3 | ELEM-bin, on elementary types: a carried binary visible test | `BinaryVisible` StageCompletion.lean:244 | introduced | necessary, not sufficient, for the elementary scope (ROADMAP :1022–1025) | `perfectlyDistinguishable_visible` :274 |
| H4 | Elementary scope: a field-neutral predicate `Elem τ` that scopes H3, H7–H18 | none | no predicate | ROADMAP :1024 "not yet formalized". **Required for (←):** the qutrit body fails SingletonFaces (exact, kn census §4); it is not an ellipsoid, so it fails Trans by `exists_affine_image_eq_eball` [K] TransitiveBody.lean:602 [W] | scopes H3, H7–H18; M9 |
| H5 | K∞-Act: a family of `OpDatum` pairs `(S, T)` with `AffineRespect` and mutual `Undoes` | `OpDatum` CompletionAction.lean:46, `AffineRespect` :58, `Undoes` :325 | introduced | the existence form is trivial (identity datum); content is relative to the family. `not_stagePreserving_of_infiniteOrderOn` [K] CompositionOrder.lean:378 (a drive's generator must cross stages) | `inducedEquiv` :333, `preservesBody_inducedEquiv` :352 |
| H6 | Body preservation of `G τ` (the induced equivalences, or words in them) | `PreservesBody` OrbitGeneration.lean:69 | conditional on H5 | [K] `preservesBody_inducedEquiv` :352; `preservesBody_words` OrbitNormalization.lean:79 | `chartBody_eq_eball` TransitiveBody.lean:651; `maxConeOf_avail_eq` EffectSpace.lean:572 |
| H7 | K∞-Drive: `Nonempty (ElementaryDrivability (chartBody C))` (continuous one-parameter group of body automorphisms, an involution on it, and an off-axis `J`) | `ElementaryDrivability` KInfFoundations.lean:264 | introduced; **Independent-verdict flag** (see (d)) | no source. A drive's flow is not Trans: `not_boundaryTransitive_flow` [K] OrbitGeneration.lean:620. No drive on finite-orbit bodies: `isEmpty_drivability_of_finite_orbits` [K] OrbitNormalization.lean:124 | no certified link of the chain consumes it directly; it enters as H24 (pair level) and as I5 (matrix level) |
| H8 | K∞-Trans: `BoundaryTransitive (chartBody C) (G τ)`, or the weaker `DenseBoundaryOrbit` | OrbitGeneration.lean:79; DenseOrbit.lean:53 | introduced | not implied by H7 [K] :620. Strictly weaker dense form: `not_boundaryTransitive_ratRefl` [K] DenseOrbit.lean:398 | `chartBody_eq_eball` :651 / `chartBody_eq_eball_of_dense` DenseOrbit.lean:209; `maxConeOf_avail_eq` :572 / `_of_dense` :243; K1 selectors |
| H9 | Sharp stage test: some stage i and preparations x0, x1 with `p(v0 i) x0 = 1`, `p(v1 i) x1 = 1` | a hypothesis of `perfectlyDistinguishable_visible` StageCompletion.lean:274 | introduced | — | H10 |
| H10 | K∞-Seed: `SharpSeed` on the normalized chart body | `SharpSeed` OrbitGeneration.lean:65 | conditional on H1, H3, H9 | [K] components: `perfectlyDistinguishable_visible` :274 → `sharpSeed_of_perfectlyDistinguishable` OrbitGeneration.lean:129; `sharpSeed_completion` :224; `sharpSeed_restrict` OrbitNormalization.lean:427; `sharpSeed_tr` :242. Composite [D] `exists_sharpSeed_eball_of_stage` (`origin/draft/kinf-seed-1`; research run 38083519826) | `maxConeOf_avail_eq` :572; `sharpFamily_subset_avail` :374 |
| H11 | K∞-V4: `SeedOrbitAvailable (G τ) r (avail τ)`, i.e. every transport of the seed is an available test | OrbitGeneration.lean:74 | introduced | body preservation of a transport does not supply it (ROADMAP :1038) | `maxConeOf_avail_eq` :572 |
| H12 | K∞-Geom, elementary-scoped: `SingletonFaces` / `RelStrictConvex` | KInfFoundations.lean:139 / :144 | introduced | listed by ROADMAP :1043; **consumed by no certified link of the chain at M** (TRB-1 uses H8). False for QM at level ≥ 3 (kn census §4, exact), so H4 is mandatory | `relStrictConvex_of_supporting_singleton` :575 (side route only) |
| H13 | Effect soundness: `EffectsOn (eball d) avail` | EffectSpace.lean:567 | conditional, for `avail` = transported stage effects ∪ seed orbit | [K] components: `stageEffects_isEffectOn` StageCompletion.lean:193, `isEffectOn_restrict` OrbitNormalization.lean:423, `isEffectOn_tr` :217, `isEffectOn_seedTransport` OrbitGeneration.lean:94 (given H6). One composite statement [W] | `maxConeOf_avail_eq` :572; `dim_of_nativeGateOf` K1Bridge.lean:128 |
| H14 | `2 ≤ d`, equivalently two sharp tests (`HasTwoSharpTests`) | SharpTests.lean:41, `hasTwoSharpTests_iff` [K] :155 | introduced | `two_le_not_implied` [K] :197 | `three_of_nativeGateOf_of_two_le` K2Guard.lean:253 |
| H15 | A NOT: `IsNot (eball d) z N` (unit axis, involution, body-preserving, flips z) | CompositeDimension.lean:210 | introduced | — | K1Bridge.lean:128, :138; K2Guard.lean:253 |
| H16 | K∞-Copy: the two copies' NOTs agree (one `N` in `relT` and `relC`), or the candidate weakening, type covariance | `CopyNatural` KInfFoundations.lean:284; built into `NativeGateOf` K1Bridge.lean:49 | introduced | without it, d = 5 countermodels exist (NB-1 probe, exact, CI replay). Type covariance [D] (`origin/draft/kinf-copy-1`; research run 38083519826) | the selectors above |
| H17 | Native gate on the available cone: `NativeGateOf (eball d) avail z N T` (frame, two-sided positivity on `maxConeOf avail`, `relT`, `relC`) | K1Bridge.lean:49 | introduced | instance at d = 3: `nativeGate_cnot` [K] CompositeDimension.lean:1160. No theorem identifies a native gate with `cnot` (M3b) | K1Bridge.lean:128, :138; K2Guard.lean:253 |
| H18 | Entangling clause `EntanglingOf` (the alternative to H14 for d = 3) | K1Bridge.lean:64 | introduced | `entangling_cnot` [K] CompositeDimension.lean:1380 | `three_of_nativeGateOf` K1Bridge.lean:138 |
| H19 | Local tomography of the two-token composite, plus its product form on the carrier `W d` | `LocallyTomographic` CompositeInterface.lean:235, `Composite.lt` :243; carrier `W` CompositeDimension.lean:97 | introduced (LT field); the identification with `W d` has no predicate (M4) | only `pairing_injective` [K] :478. Control: `not_locallyTomographic_paddedBall3` [K] :912 | DIM-1 / K1 (the carrier `W d` is in their types); EqvK2MaxCone (`W 3`) |
| H20 | Pair H1: `∀ x y ∈ eball 3, prodState x y ∈ K` (product preparations) | hypothesis `hH1` of EqvK2MaxCone.lean:153, :204 | introduced | MAXCONE-1 result: "product preparation and cone realization … retain their source obligations" | `pairCone_eq_Q3_of_*` |
| H21 | Cone closure: `ω, η ∈ K → ω + η ∈ K`; `c ≥ 0 → c•ω ∈ K` | `hadd`, `hsmul` of EqvK2MaxCone.lean:153 | introduced | controls (written, MAXCONE-1 preregistration): density states fail scaling; the rank-{0,1,2,4} family fails addition | `Q3_subset_of_products_cone_block` :107 |
| H22 | Pair validity `K ⊆ maxConeOf avail`, with `sharpFamily 3 ⊆ avail` | `hvalid`, `hsharp` of EqvK2MaxCone.lean:204 | `hvalid` introduced; `hsharp` conditional on H6, H8, H10, H11 | `sharpFamily_subset_avail` [K] EffectSpace.lean:374; `maxCone_bound_of_sharp_available` [K] EqvK2MaxCone.lean:194 | `subset_Q3_of_maxCone_block` :116 |
| H23 | Pair H2: `∀ ω ∈ K, cnot ω ∈ K` | `hH2` of EqvK2MaxCone.lean:153 | introduced | necessity side: `Q3_cnot` [K] EqvK2Generation.lean:503. The orientation guard `no_candidateCone_cnot_reflY` [K] K2Guard.lean:143 excludes adding an orientation-reversing local action | `blockInvariant_of_drive` EqvK2Generation.lean:426 |
| H24 | A_miss: `∀ t, ∀ ω ∈ K, actT (rotLin t) ω ∈ K ∧ actT cycEquiv ω ∈ K`, invariance under one token's full rotation flow and cyclic map | `hA` of EqvK2MaxCone.lean:153 | introduced; **Independent-verdict flag** (continuous local control; see (d)) | necessity side: `Q3_aMiss` [K] EqvK2Converse.lean:174, `driveInvariant_of_eq_Q3` [K] EqvK2MaxCone.lean:165. The full-flow form is load-bearing (research [W]+[X]) | `blockInvariant_of_drive` :426 |
| H25 | Multi-token composition (k ≥ 3), with consistency across groupings (FCC) | none | no predicate | no structure with ≥ 3 tokens at M. KT4 theorem only at [D] (`FourCopyHeadline`, run 37948419430); KT4-PREM-1 certified the premise audit (receipt), not the theorem. Draft `origin/draft/ktoken-maxcone-1` | M6a |
| H26 | Subspace/compression principle: every type is a subsystem of a register (for carriers that are not of size 2^k) | none (field-neutral) | no predicate | kn census §2. At matrix level, inside an `Architecture` with `ContextStable` and `LabelInvariant`, compression is [D] `compress_mem`, `drivesElementary_of_pow` (`origin/draft/kn-desc-1`; runs 38090116254, 38457070337 as that draft records them) | M6c–d |
| H27 | Operation dictionary: the observer's reversible operations and instruments on registers form an `ImplementationClass` 𝓘 with `InstAvail` = the observer's availability (state, test and operation identification) | none | no predicate | ROADMAP K2/K3: "physical state/test identification" open. No map from field-neutral objects to `ImplementationClass` (kn census §1: no import edge either way) | M6b, M7 |
| H28 | Typed operational closure at field-neutral level: id, coarse-graining, feed-forward bind, relabelling, attaching a uniformly mixed factor, discard, spectator-independent readout | fields of `TypedOperationalTheory` TypedCompletion.lean:165 (matrix level only) | no predicate (field-neutral) | the readout form is derived at matrix level (`readout_is_localLuders` OperationalAssembly.lean:658) | M7 |

**Intermediate objects F1 must derive, not assume.** Assuming them puts the kinematics back in the premises; the
statement then is K3 (ROADMAP :979), not F1.

| id | object | kernel | flag |
|---|---|---|---|
| I1–I4 | `Architecture` 𝓘, `ContextStable`, `LabelInvariant`, `DaggerStable` | ImplementationLocality.lean:506, :359, :364; MicroscopicReversibility.lean:216 | none |
| I5 | `DrivesElementary` 𝓘: transition flows, swaps and quarter phases admissible at every carrier | SubstratumSource.lean:77 | **Independent at the substratum class:** `substratum_residual` [K] StructuralClosure.lean:383 |
| I6 | `QuantumArchitecture` 𝓘 | SubstratumSource.lean:86 | not satisfied by the substratum class: `substratum_residual` [K] StructuralClosure.lean:383 |
| I7 | d = 3; `K = Q3`; ball ≅ Bloch ball | K2Guard.lean:253; EqvK2MaxCone.lean:153; EqvK2Schema.lean:216 | conditional |

**Counts (H0–H28, 29 rows).**

| status | count | rows |
|---|---|---|
| derived | 0 | — |
| conditional | 3 | H6, H10, H13; plus the `hsharp` half of H22 |
| introduced | 20 | H1, H2, H3, H5, H7, H8, H9, H11, H12, H14, H15, H16, H17, H18, H19, H20, H21, H22 (`hvalid`), H23, H24 |
| no predicate | 6 | H0, H4, H25, H26, H27, H28 |
| Independent-verdict flags | 2 rows | H7, H24, plus intermediate I5 and the conclusion-level flag in (d) |

- H14 and H18 are alternatives: one of the two is needed.
- No row has a source theorem from an OI object at M.
- No row has a justification recorded as a theorem. The only motivation on record is ROADMAP :1087–1091, "A research
  direction, unproved" [U], which names three separate candidates for H12, H7 and H16 and is not one principle.
- So F1 is **not completed by naming C**, as owner correction (2) requires.

***

## (c) The chain — proved links and missing links

The forward chain:

```
ℛ ─M1─▶ 𝔒 ─P1─▶ chart ─P3─▶ G body-preserving ─P5─▶ chartBody ≅ eball d ─P6─▶ hypotheses on eball d
  ─P7─▶ maxConeOf avail = maxCone ─P8─▶ d = 3 ─(M3, M4)─P9─▶ K = Q3 ≅ PSD(ℂ²⊗ℂ²) [P10]
  ─M6─▶ QuantumArchitecture 𝓘 ─P11─▶ ExactAll(genTheory 𝓘) ─(M7) P12─▶ typed QM ≅ Ops(𝔒)
```

### Proved links, [K] at M

| link | theorem(s) | content |
|---|---|---|
| P1 | `exists_completionChart` CompletionAction.lean:154; `chartBody_isCompact` TransitiveBody.lean:109; `chartBody_interior_nonempty` :121 | nonempty body + FiniteRank ⇒ chart; the chart body is compact and convex with interior |
| P2 | `sharpSeed_completion` StageCompletion.lean:224; `perfectlyDistinguishable_visible` :274; `sharpSeed_of_perfectlyDistinguishable` OrbitGeneration.lean:129; `sharpSeed_restrict` OrbitNormalization.lean:427 | SC∞ + a sharp stage test ⇒ a sharp seed (H10) |
| P3 | `preservesBody_inducedEquiv` CompletionAction.lean:352 | K∞-Act ⇒ body-preserving affine equivalences (H6) |
| P5 | `chartBody_eq_eball` TransitiveBody.lean:651, via `exists_affine_image_eq_eball` :602; dense form `chartBody_eq_eball_of_dense` DenseOrbit.lean:209 | PreservesBody + Trans ⇒ ∃ affine A, A '' chartBody = eball d |
| P6 | `hypotheses_tr` OrbitNormalization.lean:295 | transports PreservesBody, SharpSeed, Trans and V4 along A |
| P7 | `maxConeOf_avail_eq` EffectSpace.lean:572; `sharpFamily_subset_avail` :374; dense form DenseOrbit.lean:243 | 0 < d, H6, H10, H8, H11, H13 ⇒ `maxConeOf avail = maxCone (eball d)` |
| P8 | `dim_of_nativeGateOf` K1Bridge.lean:128 (d ∈ {1,3}); `three_of_nativeGateOf` :138; `three_of_nativeGateOf_of_two_le` K2Guard.lean:253; dense form DenseOrbit.lean:317; DIM-1 core `dim_of_nativeGate` CompositeDimension.lean:2723 | the dimension selector, d = 3 |
| P9 | `pairCone_eq_Q3_of_drive_maxCone` EqvK2MaxCone.lean:153; `pairCone_eq_Q3_of_sharp_available` :204. Separate converse witnesses: `driveInvariant_of_eq_Q3` :165, `pairCone_eq_Q3_iff_drive_maxCone` :174 (iff relative to H20–H22) | H20–H24 ⇒ `K = Q3` |
| P10 | `Q3` EqvK2Schema.lean:239; `dictEquiv` :216 (`W 3 ≃ₗ[ℝ] selfAdjoint (Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)`) | **the complex structure first appears here**, at the pair |
| P11 | `genTheory_qm_of_quantumArchitecture` SubstratumSource.lean:136 | QuantumArchitecture ⇒ ExactAll |
| P11′ | `qm_generated_by_quantumArchitecture` :161; `fullClass_quantumArchitecture` :151 | matrix-level converse |
| P12 | `typed_determined_iff` TypedCompletion.lean:850; `typed_determined_of_oiPlusElem` :859 | the typed endpoint |
| P13 | `oiPlus_iff_qm` CarrierGeneralOIPlus.lean:207, with directions :191 / :198 | the matrix-level characterization the target sources |

**Elementary instances for the converse, [K].**

- `ball3_drivable` KInfFoundations.lean:490
- `boundaryTransitive_fullAut3` OrbitGeneration.lean:537; `boundaryTransitive_fullAut` EffectSpace.lean:337
- `sharpEff_sharpSeed` :118
- `kInf1_ball3_full` KInfFoundations.lean:1076; `qubit_certain_face` :995
- `nativeGate_cnot` CompositeDimension.lean:1160; `entangling_cnot` :1380
- `Q3_cnot` EqvK2Generation.lean:503; `Q3_aMiss` EqvK2Converse.lean:174

### Missing links (no theorem at M)

- **M0. Definitions.** `ObserverModel` (types, ⊗, stages, charts, tests, operation data, composites, typed operations),
  `OpIso 𝔒 𝒯`, and `obs(𝒬)`. Everything else is stated over these.
- **M1. Origin.**
  - What is missing: `observerOf : OIRealization → ObserverModel`, building `DirectedStages` from
    `(𝒮, Obs, μ, menu)` with SC∞.
  - At M, the only `DirectedStages` values are controls: `badD` StageCompletion.lean:342, `bitTower` :393, `midD`
    CompletionAction.lean:404.
- **M2. Sourcing.**
  - What is missing: `Hyp(observerOf ℛ)` for the introduced rows, which is the content of K∞, K1 and K2-sourcing.
  - Obstruction on record (see (d), R1b): for the passive finite-Ω protocol tower, H7 fails.
- **M3. Normalization of the pair data.**
  - (a) Under A from P5, the drive's flow must be conjugate to `rotLin (ω t)` with ω ≠ 0, and the flow, J and the gate
    must generate the block group `blockInvariant_of_drive` needs. Alternatively, restate P9 for an arbitrary drive flow
    and off-axis J.
  - (b) The observer's native gate T (H17) must equal `cnot` up to local body automorphisms, so that H23 is about the
    observer's gate. Alternatively, restate P9 for T.
  - No uniqueness theorem for native gates exists at M (searched: CompositeDimension, RelcSelect*, ParityNot, OddChar).
- **M4. Composite carrier.**
  - What is missing: a `LocallyTomographic` `Composite` of two copies of `eball d` admits an injective linear map into
    `W d` that intertwines `prodState`/`prodEff` with `CompositeDimension.prodState`/`prodEffVal`. The observer's K is
    then the cone over the image of the composite body.
  - At M there is only `pairing_injective` CompositeInterface.lean:478.
- **M5. One-token dictionary.** `eball 3 ≅ D(ℂ²)` by `x ↦ ½(1 + x·σ)` (`tokMat`, EqvK2Schema.lean) with tests
  identified as effects. [W] elementary; not stated as a theorem. The pair version is P10.
- **M6. Kₙ.**
  - (a) k-token cones are `PSD((ℂ²)^{⊗k})`, from pair `Q3` and H25.
  - (b) An `ImplementationClass` 𝓘 on the registers `Fin (2^k)` built from the token operations (flow, J, gate), with
    I1–I4 and `DrivesElementaryAt (Fin (2^k))`.
  - (c) Compression to every finite carrier. This is [D] KN-DESC-1 (`drivesElementary_of_pow`,
    `quantumArchitecture_iff_pow`, `origin/draft/kn-desc-1`). Owner correction (1): this lives inside the matrix
    framework. Its imports are `SubstratumSource` and `LiftAudit`, and its surface is over `ImplementationClass` with
    `Architecture`, `ContextStable` and `LabelInvariant`. Certifying it would discharge only the carrier quantifier of
    I5 **after** M6b exists. It closes neither Kₙ nor F1.
  - (d) H26 for types that are not registers.
- **M7. Identification.**
  - What is missing: Ops(𝔒) = `genTheory 𝓘` (`InstAvail`, ImplementationLocality.lean:268; `genTheory` :852) under
    the carrier identification, and the typed lift (H28) to a `TypedOperationalTheory`.
  - With M7, P11 and P12 then give the conclusion. **That assembly step is proved.**
- **M8. Converse, operational.** `obs(𝒬) ⊨ Hyp`.
  - Only the elementary [K] instances above exist.
  - The general case needs M0, and needs H4 to scope H3, H8, H12 and H15–H18. Without H4 the converse is false: the
    qutrit body is not an ellipsoid and fails SingletonFaces.
- **M9. Converse, OI-realization.** A finite-horizon OI realization of the operational repertoire of 𝒬.
  - At the law level it holds: [K] Equivalence.lean:459.
  - At the rooted-law level the all-time form is false: [K] QuantumRepresentationT2.lean:169.
  - For the repertoire, nothing exists.
  - Spatial composites are constrained by the Bell ceiling [W] (Main.md:362–371).
  - Under R1b, M9 fails for every passive finite-Ω origin.

***

## (d) F1 retirement check (PROGRAMME §5:511)

The rule: "F1 is retired when any arc returns an Independent verdict in the sense of §6 on a resource that F1 requires —
a countermodel showing the resource does not follow from the OI axioms then in force."

**R1 — FLAG. Continuous off-diagonal control, dense unitary control and phases.**

1. *The resource is required by every F1 target with exact QM in its conclusion* ([K] chain):
   - `physical_of_exactAll` PhysicalCharacterization.lean:301 gives `HasCompositeUnitaryControl`
     (OperationalAssembly.lean:665).
   - `elementary_of_control` LieRankSource.lean:517 then gives `ElementaryTransitionRichness` (:436), whose third
     conjunct is `PhasesAvailable` (RouteB.lean:128).
   - `DenseUnitaryControl` (DiscreteCompletion.lean:45) is immediate from full control, taking V = U and c = 1 [W].
2. *Independent verdicts relative to the presently stated architecture* ([K]):
   - `frozen_sourcing_verdict` FrozenSourcing.lean:318: `¬ PhasesAvailable ∧ ¬ DenseUnitaryControl ∧ ¬ DerivedOI`
     for `permTheory (Fin 2)`.
   - `nonnegBounded_verdict` :327 gives the same for every theory inside the invariant.
   - `sourcing_rule_independent` :295: the verdict does not move with the rule.
   - `substratum_residual` StructuralClosure.lean:383: the substratum class is Architecture, ContextStable,
     LabelInvariant and DaggerStable, with `¬ DrivesElementary` and a non-QM generated theory.
   - ROADMAP :1497–1498 records "The source of phases" and "Dense/nonclassical operational control from the presently
     stated architecture" as **INDEPENDENT**.
3. *The record cuts both ways.*
   - Against retirement: PROGRAMME's retirement text was added at `9c28cd24` (2026-09-08), one day after FrozenSourcing
     landed at `e7c780dc` (2026-09-07). It still calls this resource the "standing candidate" (:511). §3.2 (:82) calls
     the shortfall "a sourcing boundary, not … a proof that OI forbids", and §3.12 (:218) keeps open "whether a deeper
     OI condition sources" it.
   - Scope of FrozenSourcing: by its own text, "the scope is the presently stated one". A6 had no predicate at its
     freeze. At M, `A6Cov` exists and is identically true (`a6cov_all`), so "its content is the covariant interface and
     not a constraint" (ROADMAP :65).
   - Reading: on its face, §6's definition (:553) is met for any F1 whose "OI" is the presently stated architecture.
     The programme text treats the antecedent as not met.
   - **Owner adjudication is required.** Either F1 is retired relative to the stated architecture and the control/phase
     resource is named as an additional principle (F2/F3, which is what H7, H24 and I5 already are in content), or
     "OI axioms then in force" is formally re-scoped to an extended observer-level OI on which no Independent verdict
     has yet been returned. Thread A does not resolve this.

**R1b — FLAG (candidate, uncertified). K∞-Drive (H7) at the stage-tower interface.**

- NG1 ([W]+[X]; `origin/research/archive` `4dc0321c`, `research/archive/oistage/RESULT.md` §6, base `0f2687b7`, not
  re-run here) states:
  - every posterior of the passive protocol tower over a finite Ω is `(μ∘σ⁻¹)·1_C` normalized;
  - so there are finitely many preparation vectors, and the body is a polytope with a finite automorphism group;
  - so there is no drive. The last step is [K]: `isEmpty_drivability_of_finite_orbits` OrbitNormalization.lean:124.
- A1 is `Finite Conf` (SubstratumInterfaceAudit.lean:84). If NG1 holds and M1 is the passive protocol tower, then:
  - Hyp(observerOf ℛ) is unsatisfiable for every A1-substratum;
  - (→) is vacuous;
  - (←OI) fails.
- F1-fin would then need an origin outside the stated architecture: invasive observation or irreversible steps, named
  only in the research archive's SA ledger. That is again an added principle.
- Supporting [K] fact: `finiteOrderOn_of_stagePreserving` CompositionOrder.lean:348.

**R2 — related, not separately retiring.** Two further INDEPENDENT entries bound candidate *mechanisms* for H7, H24 and
I5, not a separate required resource:

- "Executable intermediate layer flow": FlowEndpoint.lean `onesTheory_not_qm` :205.
- "The presently stated observer-level lift": `configurationLevel_not_layerFlowExecutable` LiftAudit.lean:183;
  `stochastic_not_layerFlowExecutable` LiftSource.lean:262.

**No flag.**

- The remaining field-neutral rows (H1–H6, H8–H23 other than the above) have only hypothesis-versus-hypothesis
  separations: `not_boundaryTransitive_flow`, `two_le_not_implied`, `cone_eq_fails_axis` K1Bridge.lean:157, the NB-1
  d = 5/7 maps, and research Ω₄ [D]. These are not hypothesis-versus-OI countermodels.
- `ensemble_underdetermined` is negative only for *selecting* μ. The target quantifies over μ, so this is not a trigger.
- The Bell ceiling [W] excludes one realization class (local, measurement-independent, deterministic). It does not
  exclude the resource. Not a trigger.

***

## (e) Out of scope, and why

- **P0, the relative evolution** (ROADMAP queue row :63; acts 11–45).
  - Excluded by owner correction (3). The target fixes *which operations are available*, and its conclusion makes every
    unitary available. It selects no history.
  - ROADMAP :1107: "orthogonal to `P0`: a complete operational reconstruction would not by itself select a unique
    quantum history".
  - P0 is neither a hypothesis nor a conclusion here, and no P0 verdict is used.
- **Continuum, infinite-dimensional and quasilocal (H-∞, L3-conv).**
  - The target is finite-carrier only.
  - `continuous_extension_not_unique` [K] RegionLimit.lean:296: discrete dynamics does not fix continuous time.
  - Infinite-support instruments, the CT3 generator and the choice of Hilbert representation are set aside with
    reasons at ROADMAP :1520 ff.
  - Level III's `canon_unique` (QuasilocalCharacterization.lean:359) is a uniqueness theorem, not a converse.
- **Hidden ontology.** The target is operational. Hidden priors, `PPer`/`C_OI`, P-indivisibility, C4 discharge, the
  stochastic interface beyond H0, and Track B (the Barandes correspondence) enter only through M1 and M9. They are not
  conclusions.
- **Spatial Bell realization and H-Bell.** The gravity/Ollivier–Ricci condition is outside the finite target (see a.5).
- **Parallel tracks.** Lemma 24.1, the BG classification debt (PROGRAMME §8:593 ff, "neither advances nor blocks"),
  A6/H-link carrier identification, and manuscripts.
