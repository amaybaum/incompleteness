# P-LEDGER — Thread P: an observer-native non-classicality principle for `2 ≤ d`

Status: one depth-first pass, complete. Read-only. Nothing here is kernel-checked, frozen or adopted.
No premise is adopted as established. No ROADMAP or manuscript wording is proposed.

## 0. Base, scope, evidence layers

- **Base.** `06b6f94e479bc19a28979c72316823cbdd0fb62b`, read in `scratchpad/wt-06b` (`git rev-parse HEAD` checked;
  `git status --porcelain` empty at the end). Paths below are relative to `verification/lean-mathlib/OIBridge/`
  unless they say otherwise.
- **Writes.** Only `scratchpad/pthread/`. No git write, no CI, no GitHub. No Lean toolchain was run.
- **Evidence layers (kept distinct).**
  `[K]` a kernel identifier at the base, with file:line. `[K-ℂ]` the same, in the ℂ matrix half.
  `[X]` an exact probe in `pthread/` (Fraction / sympy, no float used as evidence), replayed byte-identically.
  `[W]` a written argument here, not kernel-checked. `[S]` an uncompiled Lean sketch
  (`RecordIncompleteness.sketch.lean`). `[L]` literature, not re-proved. `[P]` prior off-repo notes, used as data.
- **Read for context.** `twole/TWOLE-LEDGER.md`, `sa/SA-LEDGER.md`, `oistage/RESULT.md` (also via SA),
  `k2d/K2-LEDGER.md` §1–2. `quotient/`, `rank/`, `opact/`, `drive/` RESULT notes were not needed beyond what SA
  re-verified. Kernel read: `SharpTests` (all), `KInfFoundations` §A–C and §Classical, `OrbitGeneration` §A,
  `StageCompletion` §A–E, `CompletionAction` §A–C, `TransitiveBody` §A/§E/§F′ statements, `EffectSpace` §A,
  `K1Bridge` §A–B, `K2Guard` header, `CompositeDimension` `IsNot`/`NativeGate`/`Entangling`/selectors,
  `PassiveObservation` N1, `CentralObservation` header, `InternalObserver` header, `PassiveIndependence` header.
  Manuscript: `papers/Main.md` lines 28, 40, 540, 570, 590, 630, 750.

### Landed facts re-verified at the base `[K]`
- `HasTwoSharpTests` SharpTests:41; `hasTwoSharpTests_iff` :156; `eq_or_compl_one` :86; `not_sharpSeed_zero` :72;
  `two_le_load_bearing_relative` :188; `two_le_not_implied` :199. As in the brief.
- `SharpSeed` OrbitGeneration:65; `seedTransport` :50 with `seedTransport_apply_apply` :55;
  `sharpSeed_seedTransport` :107.
- `CompletionChart.d` CompletionAction:145 is the dimension of the affine span of the completion body
  (`hspan` :151); `chartBody_eq_eball` TransitiveBody:651 produces `eball C.d` with **the same `d`**.
- `two_le_of_entangling` and `three_of_nativeGateOf_of_two_le` K2Guard:253 (header lines 18–24): the landed
  selector consumes its entangling clause only to exclude `d = 1`. Entangling (a composite premise) is therefore
  already a landed *conditional* source of `2 ≤ d`; this thread looks for a single-system one.

## 1. Inventory of the observer vocabulary (step 1)

| notion | formal (kernel) | file:line | field | prose / research only |
|---|---|---|---|---|
| stage: preparations, effects, table, unit | `FiniteStage` | KInfFoundations:63 | ℝ | |
| directed stages, forward maps, SC∞ | `StageMap`, `DirectedStages`, `SCInf` | StageCompletion:53/63/78 | ℝ | |
| completion value, preparation vector, body | `val`, `prepVec`, `body`, `coord`, `stageEffects` | SC:98/135/141/157/176 | ℝ | |
| binary visible test | `BinaryVisible` | SC:244 | ℝ | vacuous as stated (SA §2.3) |
| finite predictive dimension | `FiniteRank`; `CompletionChart.d` | SC:299; CA:144 | ℝ | |
| operations on preparations | `OpDatum`, `AffineRespect`, `Undoes`, `inducedEquiv` | CA:46/58/325/333 | ℝ | |
| effects on a body, certain face, boundary state | `IsEffectOn`, `certainFace`, `IsBoundaryState`, `fullEffects` | KF:116/120/130/149 | ℝ | |
| perfectly distinguishable family (a "readout context") | `PerfectlyDistinguishable` | KF:154 | ℝ | |
| pure state | `Ω.extremePoints ℝ` (Mathlib), used in `Entangling` | CompositeDimension:229 | ℝ | |
| classical body | `simplex N`, `ClassicallyExposed` | KF:889/894 | ℝ | |
| sharp test, transport, availability, transitivity | `SharpSeed`, `seedTransport`, `SeedOrbitAvailable`, `BoundaryTransitive` | OG:65/50/74/79 | ℝ | |
| passive instrument, separating, branch scalar | `IsPassiveInstrument`, `SeparatesStates`, `passive_branch_scalar`, `no_complete_passive_observation` | PassiveObservation:203/208/215/259 | **ℂ** | |
| passive reads only the center | `central_classification`, `complete_passive_iff_injective`, `injective_iff_commutative` | CentralObservation:433/567/580 | ℂ | |
| record, internal observer, writing a record | `Records`, `IsInternalObserver`, `recordInstr_writes`, `recordInstr_not_passive` | InternalObserver:63/68/272/290 | ℂ | |
| passive incompleteness of a theory | `PassivelyIncomplete`, `passivelyIncomplete_of_card`, `passive_nondiscriminating` | PassiveIndependence:74/80/269 | ℂ | |
| classical substratum observation | `trajProb`, `actWord`, `itiSetoid`, `unif`, … (SA §1.1 table) | PQ/OQ/CQ/CM/RT/SOL | none | |
| protocol tower PT (stages built from the substratum) | — | — | — | **research only** (oistage, SA §2.1) |
| instrument / branch maps on a field-neutral body, observe-and-forget = idle | — | — | — | **research only** (SA P-H "statement sketch only"; oistage NG2) |
| joint readout, measure-and-prepare, re-preparation, disturbance | — | — | — | **not formal anywhere field-neutral** |
| the visible-factor requirement | — | SC header lines 11–14 says this vocabulary "cannot state" it | — | prose |
| incompleteness thesis | — | Main.md:28 (hidden sector marginalized), :40 (diagonal: an embedded representation cannot close over the whole; Gödel, Wolpert), :570 (passive incompleteness, theory-insensitive), :590 (incompleteness forces hidden memory) | — | prose |

**Finding of step 1.** Every "instrument" notion (passivity, records, separation, disturbance) is formal only
in the ℂ half. Its field-neutral counterpart is research-only. So any observer-native P that speaks of
readouts with post-measurement states needs one new field-neutral definition (`PassiveReadout`, §6), or must
restrict itself to effects plus preparations (`ReconstructingRecord`, §6), which uses only landed types.

## 2. Productivity test (fixed before the probes, §A.31)

A result is a gem iff it is strictly stronger than "2 ≤ d is unsourced" AND it either (i) decides a candidate's
(a)/(b)/(c) with a witness or countermodel, or (ii) exposes an assumption hidden in the target, in the brief or in
a candidate. Below that: record-only.

## 3. Node 0 — what `HasTwoSharpTests` says on a general body (decisive first branch)

**N0.1 (`[W]` + `[X]` P1).** For every compact convex body Ω, `HasTwoSharpTests Ω ⇔ dim aff Ω ≥ 2`.
- (⇐) Two non-proportional linear functionals on the direction space, each normalised by its min and max on Ω,
  are sharp seeds. If `f = e` or `f = 1 − e` on Ω, the linear parts are proportional. Contradiction.
- (⇒) A point has no sharp seed. On a segment an affine effect with values 0 and 1 is `t` or `1 − t`.
- Exact P1: witnesses on the trit, the 4-simplex, the square, the Spekkens octahedron and the pyramid; none on
  the segment (exhaustive). **The classical trit `simplex 3` satisfies `HasTwoSharpTests`**
  (`e` = coordinate 2, `f` = coordinate 1).
- Kernel consequence (`[W]`, kernel-cheap): on the chart body, compact by `chartBody_isCompact` TB:109,
  `HasTwoSharpTests (chartBody C) ↔ 2 ≤ C.d` holds **before** TRB-1's ball. `2 ≤ d` is literally "the observer's
  completed body has predictive (affine) dimension at least two". That is already observer vocabulary
  (`FiniteRank`'s dimension), and it is a pure relabeling.

**N0.2 — the brief's G4 boundary, corrected (hidden assumption).** "A classical joint distribution traced out
gives a simplex, where `HasTwoSharpTests` fails" is true **only for the two-vertex simplex** (the bit). It needs
the capacity-two elementary scope (SA's unlanded `ElemScope`). A classical observer with complete access to a
three-valued variable satisfies `HasTwoSharpTests`. So `HasTwoSharpTests` carries **no non-classical content**.
Its classical failure is a scope artefact.

**N0.3 — the classical countermodel class must be named (hidden assumption in requirement (a)).**
- Beltrametti–Bugajski `[L]`: ontic states are the pure states, and the responses are the affine effects
  evaluated there. This is a classical hidden-variable model whose observer-level body is the ball, with every
  QM statistic, sequential ones included, when its update is invasive.
- Hence **no operational premise satisfied by finite QM fails for every classical hidden-variable observer**.
  G4's "no principle satisfied by every classical HV observer can source it" is true, and for a stronger
  reason than G4 gives.
- Requirement (a) is meaningful only relative to a named class. This thread uses four classes:

| class of classical observer | body | example (layer) |
|---|---|---|
| C-complete: full access to the ontic variable | a simplex | Δ_n `[X]` P2 |
| C-PT: OI's own landed classical architecture (finite carrier, reversible step, permutation menu, prefix-closed protocol effects, passive reads) | **a simplex** (NG1-S, §5) | P4 T0, R0–R7 `[X]`; proof `[W]` |
| C-restricted: classical with epistemically restricted, non-joint readouts | a non-simplex polytope is possible | square (P4 C1), Spekkens octahedron (P2) `[X]` |
| C-invasive ψ-ontic | the QM ball itself | Beltrametti–Bugajski `[L]` |

## 4. Candidate families, depth-first (step 2)

Three strata appear on general compact convex finite-dimensional bodies. All are exact on the six test bodies
(P2), with strictness witnesses.

- **D** (dimension ≥ 2): `HasTwoSharpTests`; "rank ≥ 2"; G4 stated with boundary states.
- **S** (non-simplex): PI, NRR, INCOMP, EXTDEC (pure = extreme), the multi-outcome complete-readout negation,
  "some readout cannot be implemented passively", and generalized non-contextuality failure under no-restriction.
- **N** (irreducible cone): NIWD.
- **B** (no binary readout injective on pure states): PBIN.

Inclusions: N∧(≥2 states) ⊊ S, B ⊊ S, S ⊊ D.
- Triangle: in D, not in S.
- Pyramid over a square: in S, not in N.
- Square: in S and N, not in B.
- N and B are incomparable. The square is in N and not in B. A pyramid over a disc is in B and not in N
  (`[W]` only, no exact disc).

**On `eball d` every candidate below collapses to `2 ≤ d`** (NIWD needs a sharp seed to exclude d = 0).

| node | candidate P (observer statement) | stratum | (a) classical | (b) on `eball d` | (c) qubit | (d) | verdict |
|---|---|---|---|---|---|---|---|
| N1 | **NRR — record incompleteness**: no readout whose record, followed by re-preparation from the record, returns every preparation | S | fails on every simplex `[X]` P2; on every C-PT body `[W]`+`[X]` P4; holds on C-restricted `[X]` and C-invasive `[L]` | ⇔ `2 ≤ d` `[W]`, `[X]` d = 0,1,2,3 (P2), `[S]` proof plan from landed lemmas | holds: `[X]` P3 Q3, via eball 3; `[K-ℂ]` through PI | yes | **rank 1** |
| N2 | **PI — passive incompleteness**: no passive readout (observe-and-forget = idle) separates the preparations | S | as N1 | ⇔ `2 ≤ d` `[W]`, `[X]` P2 | `[K-ℂ]` `no_complete_passive_observation` PO:259 for CP readouts; `[X]` positive maps via eball 3 | yes | **rank 1** (instrument form of N1; PI ⇒ NRR on every body `[W]`) |
| N3 | **NIWD**: every passive readout has a state-independent outcome law | N | fails on every simplex and on every body with a classical superselection (pyramid) `[X]` | with `SharpSeed`: ⇔ `2 ≤ d` `[W]`, `[X]` P2 (only scalars keep ±e_i as eigenvectors, d = 2, 3) | `[K-ℂ]` `passive_branch_scalar` PO:215; `[X]` Choi(id) has rank 1 (P3 Q2) | yes | rank 2: needs a seed at d = 0; strictly stronger than needed |
| N4 | **INCOMP**: two binary readouts with no joint four-outcome readout | S (with all body effects; Plávala 2016 `[L]`) | simplices: product joint readout `[X]`; non-simplices: incompatible pair `[X]`; the Spekkens incompatible pair is not a classical response (value 2 at an ontic vertex) `[X]` | ⇔ `2 ≤ d` `[W]`; witness: forced g₁₁ = 1/4 + (x₁+x₂)/4 takes −1/10 at (−3/5, −4/5) `[X]` | `[X]` forced G₁₁ has eigenvalue (1 − √2)/4 < 0 (P3 Q4) | yes | rank 3: needs a joint-readout notion that is not in the kernel |
| N5 | **EXTDEC**: some preparation is a mixture of pure preparations in two ways | S (Bauer/Choquet, finite dim `[L]`) | `[X]` P2 | ⇔ `2 ≤ d`: centre = ½(±e₁) = ½(±e₂) `[W]` | yes | yes ("pure" = extreme) | rank 4. **G4's boundary-state wording is stratum D** (relabeling): the trit centre is ⅓v₁ + ⅔m₂₃ in three ways |
| N6 | **PBIN** (step 3 / item iv): no binary readout's outcome probability identifies the pure preparation | B | fails on **every polytope**, hence on every finite stage and every C-PT body `[X]` P2 | ⇔ `2 ≤ d` `[W]`: e(w) = e(−w) for unit w ⊥ v | `[X]` P3 Q5 | yes | rank 5: implies uncountably many pure states (a countable set always has an injective functional), so it is a continuity axiom (Hardy) in disguise. Completion-only: false at every finite stage |
| N7 | item (iv), multi-outcome: no readout context is deterministic and separating on the pure preparations | S | fails on simplices (complete context exists) `[X]` | ⇔ `2 ≤ d` `[W]` | yes | yes | equivalent to N1/N2; NRR is cleaner (needs no notion of "pure") |
| N7′ | item (iv), binary deterministic: no sharp test is deterministic and separating on pure states | ≠ S | **holds on the trit** (no binary test separates 3 vertices) | with seed ⇔ `2 ≤ d` | yes | yes | **rejected**: fails (a); binary is load-bearing the wrong way |
| N8 | disturbance (ii), weak: some readout disturbs some other readout | — | classical invasive readouts exist | — | — | yes | **rejected**: (a) fails trivially |
| N8′ | disturbance, strong: some readout has no passive implementation | S | `[W]` block argument | ⇔ `2 ≤ d` | yes | yes | equivalent to N2 |
| N9 | Kochen–Specker contextuality | — | — | — | **fails**: the qubit has a KS/Bell non-contextual model `[L]` | — | **rejected** (c) |
| N9′ | generalized (Spekkens) contextuality = non-simplex-embeddability | S with all effects; strictly stronger with realised effects (excludes Spekkens) `[L]` (Schmid et al. 2021) | yes | ⇔ `2 ≤ d` with all effects | yes (Spekkens 2005) `[L]` | **no**: it quantifies over ontological models or embeddings into a hidden simplex | rank 6: not observer vocabulary |
| N10 | drive: an elementary drivability datum exists | — | — | `ElementaryDrivability (eball 1)` is empty `[W]` (Aut = {±id}, so a continuous flow is trivial and N cannot move; analogue of `not_drivable_Icc` KF:529 `[K]`) | yes | no (dynamics) | side route; K∞-Drive is itself unsourced (SA) |
| N0 | rank ≥ 2 / `HasTwoSharpTests` / G4 with boundary states | D | **holds on the trit** | literal | yes | yes | **relabeling** |

## 5. NG1-S — OI's own classical observers have simplex bodies (NEW)

**Claim (`[W]`).** Take a finite carrier, a full-support μ, a step φ, a menu of permutations, passive
observation, and effects given by all protocol records (prefix closed). Then every stage body, and the completion
body, is a **simplex**. Its vertices are the images of the classes of the finest record partition F.

**Proof.**
1. Pullback.
   - For a word w with state map π, the record partition of "w then σ′" refines π*P_{σ′}.
   - So π*F is coarser than F. It has the same number of classes, because π is a bijection.
   - Hence π*F = F, and every protocol permutes the F-classes.
2. Joint readability.
   - π_w⁻¹ is a word, by finite order.
   - "σ₁, then π_{σ₁}⁻¹, then σ₂" reads P_{σ₁} ∨ P_{σ₂}.
   - So F is the record partition of one protocol, and the class indicators are effects.
3. Every effect is a union of F-classes.
   - So prepVec = R′ ∘ q, with R′ : Δ_classes → values linear and injective by step 2.
   - Posteriors map to points of Δ_classes.
   - Class-concentrated posteriors are realised: after the joint protocol, by step 1.
   - So the body is R′(Δ_classes).

**Exact `[X]` P4.**
- T0, and eight seeded random towers R0–R7 (N = 3..5, with and without a menu): every stage body is a simplex
  under a brute-force barycentric search that is independent of the partition argument.
- Affine dimension = #classes − 1. The class images are affinely independent and realised.
- Countercontrol C1: two classical bits read only one at a time (not prefix closed). The body is a **square**,
  not a simplex. Adding the joint read gives a simplex (C1b). So joint readability, which comes from prefix
  closure plus inverse words, is load-bearing.

**Relation to prior notes.**
- It strengthens oistage/SA NG1 from "polytope" to "simplex". This is consistent with SA's P4 (rank |Ω|) and
  P2 (the Z3 triangle).
- With `not_boundaryTransitive_of_nonextreme_boundary` TB:301 `[K]`, which applies because a simplex of
  dimension ≥ 2 has non-extreme boundary states, every C-PT body with a boundary-transitive family has dimension ≤ 1.
- So **`2 ≤ d` in any form is incompatible with finite passive PT together with K∞-Trans**. Any P (rank ≥ 2
  included) needs the same source regime SA §3.2 identified: invasive observation (E1), a step irreversible on
  the body (E2), or an infinite carrier.

## 6. The best candidate, precisely (step 4)

**P = record incompleteness (NRR), stated on the observer's completed body `Ω` with its available effects.**

    ReconstructingRecord Ω avail :=
      ∃ k (e : Fin k → V →ᵃ[ℝ] ℝ) (y : Fin k → V),
        (∀ i, e i ∈ avail) ∧ (∀ i, IsEffectOn Ω (e i)) ∧ (∀ i, y i ∈ Ω) ∧
        (∀ x ∈ Ω, ∑ i, e i x = 1) ∧ (∀ x ∈ Ω, ∑ i, e i x • y i = x)
    RecordIncomplete Ω avail := ¬ ReconstructingRecord Ω avail

In words: no single readout's record, followed by re-preparation from the record, returns every preparation.
It uses only landed types (`IsEffectOn`, affine maps, sets).

**Its instrument form is PI.** `PassiveReadout` is the homogeneous pairs (eᵢ, bᵢ), with
bᵢ(x) ∈ eᵢ(x)·Ω, ∑eᵢ = 1 and ∑bᵢ(x) = x. PI says no passive readout separates. PI ⇒ NRR on every body
(measure-and-prepare branches; `[W]`, `[S]`). NRR ⇒ PI on compact finite-dimensional bodies (both ⇔ non-simplex;
`[W]`).

**Kernel-ready statements (`[S]`, `RecordIncompleteness.sketch.lean`).**
- `recordIncomplete_eball_iff : RecordIncomplete (eball d) (fullEffects (eball d)) ↔ 2 ≤ d`. The two directions
  have separate witnesses (§A.34):
  - (→) by `reconstructingRecord_zero` (unit readout) and `reconstructingRecord_one` (`sharpEff (±z1)`,
    re-prepare ±z1);
  - (←) by `not_reconstructingRecord_of_two_le`, which needs one lemma: a convex combination of ball points equal
    to a unit vector has each positively weighted point equal to it. It uses only the points ±e₀ and ±e₁, and
    `affine_combo` KF:164.
- `two_le_of_recordIncomplete`: P relative to `avail`, together with the selector's landed hypotheses
  (`EffectsOn`, `PreservesBody`, `SharpSeed`, `BoundaryTransitive`, `SeedOrbitAvailable`), gives `2 ≤ d`. The plan
  uses only landed lemmas:
  - d = 0: `not_sharpSeed_zero`;
  - d = 1: `sharpSeed_eq_sharpEff`, `isBoundaryState_eball_of_sphere`, the transitivity witness g with g u = −u,
    `sharpSeed_seedTransport`, `seedTransport_apply_apply` (so f(−u) = r(u) = 1), `sharpEff_neg_self` and
    `eq_or_compl_one`. Together these give f = 1 − r on the states, and `![r, f]` with `![u, −u]` reconstructs.
  - Then `three_of_nativeGateOf_of_two_le` K2Guard:253 gives d = 3.
- Controls:
  - `not_recordIncomplete_one`: the d = 1 relative countermodel `two_le_load_bearing_relative` violates P;
  - `trit_separates`: `HasTwoSharpTests (simplex 3) ∧ ReconstructingRecord (simplex 3) (fullEffects _)`.

**The implication chain (b), each link labelled.**

| link | statement | status |
|---|---|---|
| L0 | OI supplies P on the completed elementary body | **conjectural, and obstructed** in the landed classical regime: NG1-S (§5) makes every C-PT body a simplex, which violates P |
| L1 | P on `body D` transports to `chartBody C` along the chart (an affine bijection of the affine span; `chart_coordsOf` CA:175, `coordsOf_chart` CA:178) | `[W]`, kernel-cheap, not landed |
| L2 | `chartBody C` is an affine image of `eball C.d` under PreservesBody + BoundaryTransitive (K∞-Trans, a premise) | `[K]` `chartBody_eq_eball` TB:651 |
| L3 | P transports along the affine equivalence A; effects become `e ∘ A⁻¹`, states `A y` | `[W]`, kernel-cheap |
| L4 | P on `eball d` ⇒ `2 ≤ d`, absolutely (fullEffects) or relative to the selector hypotheses | `[S]` from landed lemmas; `[X]` d = 0..3 |
| L5 | `2 ≤ d` ⇔ `HasTwoSharpTests (eball d)` | `[K]` `hasTwoSharpTests_iff` SharpTests:156 |
| L6 | with `IsNot` and `NativeGateOf`, d = 3 | `[K]` K2Guard:253 |

**Exact relation to `HasTwoSharpTests` (why P is not a relabeling).**
- On `eball d` the two are equivalent (L4 + L5). Any proposition equivalent to `2 ≤ d` is.
- On general bodies they differ:
  - `HasTwoSharpTests` ⇔ dim ≥ 2 (stratum D);
  - P ⇔ non-simplex (stratum S);
  - P ⇒ `HasTwoSharpTests`, strictly: the trit is a witness, `[X]` P1 + P2.
- In vocabulary: `HasTwoSharpTests` counts sharp binary tests up to complementation. P says nothing about
  counting. It says the identity operation is never "read, then re-prepare from the record". It fails on every
  simplex, so on every C-complete and C-PT observer. `HasTwoSharpTests` fails only on the bit.

## 7. Relation to OI's incompleteness thesis

The manuscripts carry three incompleteness statements. None of them yields P.

1. **Hidden-sector incompleteness** (Main.md:28, :590, :750): the embedded observer marginalises over a sector it
   cannot read.
   - Exact countermodel `[X]` P4 T0: a visible bit and two hidden bits that the step cycles. Every effect is
     constant on hidden fibres, so the hidden sector is permanently unreadable. Yet the body is a segment, and the
     visible readout with re-preparation **reconstructs every preparation**.
   - The thesis holds and P fails. The thesis is about the *ontic* state; P is about the observer's *own reduced
     body*.
2. **The diagonal form** (Main.md:40): an embedded representation cannot close over the whole that contains it.
   Wolpert's limits apply to classical devices `[L]`. So the diagonal holds for C-complete observers, where P
   fails. It cannot imply P.
3. **Passive incompleteness** (Main.md:570; `[K-ℂ]` PO:259, CentralObservation:567/580, PassiveIndependence:80/269).
   - This is P's instrument form (N2), stated in ℂ.
   - The corpus records it as **theory-insensitive and non-discriminating**: it holds for every theory on a full
     matrix algebra. Its direction is noncommutativity ⇒ PI. The corpus says it is "not evidence for a hidden
     ontology" and does not say QM rests on it.
   - Field-neutrally, PI is exactly non-simplicity, the body-level analogue of `injective_iff_commutative`
     (simplex ↔ commutative).
   - Using PI as a premise for `2 ≤ d` reverses the corpus's stated direction. That is not circular (no ℂ is
     presupposed), but it is a new premise, not a consequence of the thesis.

**Verdict on step 3's question.** "No single readout context is complete" is OI-flavoured, and it is precisely
the corpus's passive incompleteness made field-neutral. It is a *second* incompleteness, about records rather
than the hidden sector. OI's thesis as stated does not imply it, and OI's landed classical architecture violates
it (NG1-S). Naming it as an OI premise would be an addition, and should be named as a non-classicality input
(as TWO-LE G4 asked).

## 8. Gem-finding passes and classification (step 5)

| id | finding | class | layer |
|---|---|---|---|
| G-P1 | `HasTwoSharpTests` ⇔ affine dim ≥ 2 on every compact convex body. On the chart body it is `2 ≤ C.d` before TRB-1. The classical trit satisfies it. | **NEW** | `[W]` + `[X]` P1 |
| G-P2 | The brief's G4 boundary ("the simplex fails it") holds only under the capacity-two scope. Without it, `HasTwoSharpTests` has no non-classical content. | **NEW** (assumption watch) | `[X]` P1 |
| G-P3 | Requirement (a) needs a named classical class: Beltrametti–Bugajski satisfies every operational premise QM satisfies. Four classes are tabulated (§3). | **NEW** (assumption watch) | `[L]` + `[X]` |
| G-P4 | NG1-S: OI's finite prefix-closed passive towers have **simplex** bodies, which strengthens NG1. So `2 ≤ d` (any form) is inconsistent with C-PT + K∞-Trans, and every P needs E1, E2 or an infinite carrier. | **NEW** | `[W]` + `[X]` P4 (8 toys + countercontrol) |
| G-P5 | Four strata D ⊋ S ⊋ {N, B} on general bodies, all collapsing to `2 ≤ d` on the ball; exact strictness witnesses. | ELABORATING | `[X]` P2 |
| G-P6 | **Skeptical, the favourable reading defeated.** The fragment of P that the chain consumes is the binary record {r, transported r} at d = 1, i.e. "the body is not a segment". With a seed, that is "dim ≠ 1", which the classical trit satisfies. Every non-simplex body of dimension ≥ 2 is already excluded or admitted by K∞-Trans, and every classical body of dimension ≥ 2 is excluded by TB:301 (simplices have non-extreme boundary). So P's non-classical surplus is **never load-bearing** in the current chain. (a) is satisfiable, but satisfying it is not what makes P work. The criterion that discriminates among candidates is sourceability, not classical failure. | **NEW** | `[W]` (proof plan of `two_le_of_recordIncomplete` uses only k = 2 at d = 1) |
| G-P7 | No-restriction is load-bearing for every body-level P. Restricted classical models (Spekkens octahedron, C1 square) satisfy S and N only through effects that are not classical responses (exact: value 2 at an ontic vertex) or through missing joint reads. The absolute ball statement uses `fullEffects` (EFF-1 needs `MixingClosed`). The relative form needs only the seed orbit (V4). | NEW (assumption watch) | `[X]` P2, P4 C1 |
| G-P8 | Formulation hazards. (i) Binary vs multi-outcome: the binary-deterministic version holds on the trit (N7′ rejected). (ii) "Pure" must be extreme, not boundary (G4 wording is stratum D). (iii) d = 0: NIWD needs a seed; NRR and PI do not. (iv) Branches must stay homogeneous pairs (eᵢ, bᵢ): if 0 ∈ Ω, eᵢ(x)·y loses normalisation. (v) PBIN is false at every finite stage. Whether PI or NRR at the stages passes to the completion is not established, so P is stated on the completion body. (vi) S ⇔ non-simplex uses finite dimension (FiniteRank); infinite-dimensional bodies were not examined. | ELABORATING | `[W]`, `[X]` |
| G-P9 | OI's hidden-sector incompleteness does not imply record incompleteness (T0). | CONFIRMING (of Main.md:570's "not evidence for a hidden ontology"), sharpened with an exact field-neutral countermodel | `[X]` P4 T0 |
| G-P10 | The ℂ kernel already proves the qubit side of N2/N3 (`passive_branch_scalar`, `no_complete_passive_observation`). | POSITIVE | `[K-ℂ]`, `[X]` P3 Q2 |
| G-P11 | Entangling (K2Guard) is the existing landed conditional source of `2 ≤ d`. Single-system candidates replace a composite premise with an equally unsourced single-system one. | CONFIRMING | `[K]` |

**Fixed point.** Not reached. Pass 1 (G-P1/2), pass 2 (G-P3/4) and pass 3 (G-P6/7) each produced NEW items. A
fourth pass is where E1 belongs: does an invasive field-neutral tower with FiniteRank give a non-simplex body?
Not attempted.

## 9. Probe log

Environment: Python 3.11.15, sympy 1.14.0.

Commands, from `pthread/`:

    python3 -I <script> > <out>
    python3 -I <script> > <rerun>
    cmp <out> <rerun>

`-I` is safe here: scripts add their own directory to `sys.path` explicitly, and all helper modules are written in
this thread. Hashes are the first 16 hex digits of sha256.

| probe | script | output | result | replay |
|---|---|---|---|---|
| P1 HTST vs dimension | `p1_htst_dimension.py` 20f03636eff6d169 | `p1_out.txt` 2765abda4d300a54 | `ALL-PASS 9/9` | identical |
| P2 strata on bodies, eball, incompatibility | `p2_body_classes.py` 663132c21d96af67 | `p2_out.txt` 5eea0be839c745ff | `ALL-PASS 47/47` | identical |
| P3 qubit (sympy) | `p3_qubit.py` 1daa9e219db6630c | `p3_out.txt` 85df8c45b86628ec | `ALL-PASS 12/12` | identical |
| P4 classical towers, NG1-S | `p4_classical_towers.py` 4790db779762a831 | `p4_out.txt` 0731967d4afda25e | `ALL-PASS 21/21` (about 2.5 min) | identical |
| helpers | `plib.py` a319c807b1592a79, `bodies.py` 89b049a197be3d95 | — | — | — |
| sketch | `RecordIncompleteness.sketch.lean` | — | uncompiled | — |

**Defects found in my own probes, kept rather than hidden.**
- **P2 v1** (`p2_body_classes.v1.py` 40396a7ffb942b12, `p2_out.v1.txt` 938ebfbd9809ab9f): 2 FAILs.
  - NIWD was tested as "solution space of dimension 1". That is wrong for bodies that are not full-dimensional in
    their ambient coordinates: the Spekkens octahedron sits in the hyperplane Σv = 1 of ℝ⁴. The corrected test is
    "a single eigenvalue block".
  - The sharp-test search range ±1/2 missed the octahedron's 0/1 effects (coefficient 2).
  - Both are fixed. The corrected run adds the check that the octahedron's incompatible pair is not a classical
    response.
- **P4 v1** (`p4_classical_towers.v1.py` 9d4d03318c4dfc9f; output to terminal only, not saved): `SOME-FAIL 20/21`.
  - R5's partition prediction failed at preparation horizon 3: affine dimension 3 against 5 classes. The
    brute-force simplex test passed.
  - This is a finite-horizon artefact: three-step preparations cannot pin every class when vis = [0,0,0,0,1].
  - The corrected script grows Lp up to 5. R5 is realised at Lp = 4, and the simplex test passes at every horizon
    tried.
- **P2:** the eball 0 line was `chk(..., True)` (vacuous); replaced by an actual reconstruction computation before the final run (output bytes unchanged, script hash updated).
- **P3:** a vacuous check (`1 < 2`) was replaced before the final run by sympy's exact relational
  `(1 − √2)/4 < 0`.
- `__pycache__/` is a byproduct of importing the helpers. It is harmless.

## 10. What this thread does not decide

- Whether any OI construction supplies P, or any other premise implying `2 ≤ d`. L0 is open, and in the landed
  classical regime it is obstructed (NG1-S).
- Whether an invasive (E1) or body-irreversible (E2) field-neutral tower yields a non-simplex body of finite rank.
- Whether stage-level PI or NRR passes to the completion.
- Anything about infinite-dimensional bodies, K2, or composites beyond citing K2Guard's Entangling route.
- Every negative result is scoped to the construction tested: finite prefix-closed passive protocol towers, and
  the six test bodies. None says that no observer-level extension can supply P.
