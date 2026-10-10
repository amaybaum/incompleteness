# Thread H — minimal field-neutral vocabulary for Naimark-style transport (read-only; certified main 6d0abf6b)

Line numbers are at `6d0abf6ba5467e0b0c1f5437a03ae6bd22f9c28a`. Abbreviations: KF = KInfFoundations.lean, OA =
OperationalAssembly.lean, NGB = NativeGateBall.lean, Eq = Equivalence.lean, PQ = PassiveQuotient.lean, FE =
FiniteEntropy.lean, MC = MonoidalCompletion.lean, SC = StructuralClosure.lean.

Evidence levels are kept separate:
- **kernel**: a landed identifier;
- **exact**: `h_controls.py` in this directory, run as `OK -- 62 checks, 12 written notes`. The replay is identical
  (`rerun.out`). sha256 `85d9a118…a559605`;
- **written**: an argument stated here;
- **citation**: literature, with theorem numbers not verified.

Nothing here is a kernel result unless it names a landed identifier.

**Outcome class: O-FUNCT.**
- The first arrow the landed vocabulary cannot type is **A**: the body level has no composite.
- A is not irreducible. For the sharp target, the composite, attachment and discard can be eliminated (exact), and
  the composite rule does not matter.
- The native sharp readout exists (the visible readout).
- What is missing is the rule that transports an available effect along an available reversible map, i.e. effect
  functoriality.

***

## 1. Finding

On the 3-ball, an effect that is certain at x and vanishes at some state is forced to be (1 + x·r)/2 (exact).
- "Sharp normalization" is therefore a perfectly distinguishing pair. KF already has the predicate for this,
  `PerfectlyDistinguishable` KF:154 with ι = Fin 2.
- The typed Naimark formula is e(s) = r(D(U(A(s, ρ_R)))). The landed field-neutral vocabulary first fails to type
  it at **A**, because no field-neutral module has a composite of convex bodies.

The composite exists canonically in only one case: a **classical** register, Ω ⊗ Δ_n. A simplex factor makes the
minimal and maximal tensor products equal.
- In that case A, D and r are definable without choice, and r is a barycentric coordinate.
- But every reversible U then permutes blocks of local automorphisms when the system's cone is indecomposable
  (ball, square, polygons, bidisk). So the transported readout is constant (exact instances plus a written proof).

With a **non-classical** register, the composite rule is not canonical: min ⊊ QM ⊊ max for two Bloch balls (exact).
- SWAP preserves all three rules and simply moves the register's sharp seed onto the system.
- CNOT and the interacting ZZ(π/4) gate preserve QM but neither min nor max (exact).
- Even in QM, CNOT-Naimark with a sharp register readout yields exactly the seed composed with a local reversible
  map (exact).

So for the sharp family the register adds nothing beyond relocation. The formula reduces to e_g = r ∘ g⁻¹:
- r is a native sharp seed: the visible readout, sharp by conditioning;
- g ranges over the available reversible maps.

This reduced form *is* typable in KF: an affine map composed with an `AffineEquiv`. On the ball, the words in
`ball3Drive`'s flow and `J` carry one seed to every (1 + b·r)/2 (exact, Euler word in Q(√5)). That family is exactly
what `lorentz_of_effects` (NGB:105) consumes, and it needs no limit closure (D3).

The one thing KF lacks is the link that makes `e ∘ g` available: `avail` is a free parameter (Thread F). That link
is **effect functoriality**: an available reversible operation followed by an available test is an available test.
- It is natively present at the ontic level, where the readout at time k is the visible factor of `step^k`
  (`RevReal.traj` Eq:176).
- It is absent for bodies.

The reversible maps that actually move the readout's axis are K∞-R's off-axis maps. The substratum's own dynamics
fixes the axis (`substratum_residual` SC:383). K∞-R stays a separately named hypothesis and is not assumed here.

***

## 2. Typed formula, arrow by arrow (review protocol item 1)

e_x(s) = r( D( U( A(s, ρ_R) ) ) )

| arrow | domain → codomain | primitive | landed field-neutral (body level) | landed elsewhere | typable now? |
| --- | --- | --- | --- | --- | --- |
| A | Ω_S × Ω_R → Ω_SR, bi-affine, s ↦ s ⊗ ρ_R | 1 (composite) + 2 (attach) | **absent**. KF has one body in one `V`: `FiniteStage` KF:63, `ElementaryDrivability` KF:264, `CopyNatural` KF:284 | ontic, classical: `RevReal` Eq:157 (`V × Hid`, `init` not required to factor), `hiddenExt` PQ:498. Matrix: `tensorOf` MC:193, `uniformAttach` OA:492, `pureAttach` OA:500, `prepAvail` OA:626, `prepAvail_uniform` OA:630 | **no: the first untypable arrow** |
| U | Ω_SR ≃ᵃ Ω_SR, preserving the body | 4 (reversible composite dynamics) | only on a single body: `ElementaryDrivability.flow`/`J` KF:264–276 | ontic: `RevReal.step` (an `Equiv` of `V × Hid`). Matrix: `conjChannel` MC:360, `HasCompositeUnitaryControl` OA:665, `control_of_lieRank` MicroscopicReversibility:114 | no (no composite); yes on one body |
| D | Ω_SR → Ω_R, D = u_S ⊗ id | 4 (discard) | absent. The ingredient it needs, the unit, is landed: `FiniteStage.unit` KF:69 | ontic: `marg` FE:130, `RevReal.law` Eq:180. Matrix: `ptraceAnc` OA:453, `discardWith` OA:515, `prepAvail_discard` OA:649 | no |
| r | Ω_R → [0,1], sharp | 3 (native readout) | predicate only: `PerfectlyDistinguishable` KF:154. No native instance | ontic: the visible factor (`RevReal.traj` Eq:176) and conditioning on a visible value (`quotMeasure_branch` PQ:410). Matrix: `readout` OA:640, `readout_avail` OA:642, with its form derived by `readout_is_localLuders` OA:658 | as a predicate only |

In the reduced form e_g = r ∘ g⁻¹, A and D are the identity, with the register being the system or reached by SWAP:
- the expression **is typable** in KF, as `(e : V →ᵃ[ℝ] ℝ).comp g.toAffineMap` with `g` from `ElementaryDrivability`;
- what cannot be typed is the judgement `e ∘ g ∈ avail`.

**Circularity check (review protocol item 2).**
- **D** uses only the unit effect u_S, the normalization. That is canonical and is not P2: B3 shows the unit is
  insufficient, but it is not quantified over.
- **r** must be the *native visible readout*, defined by the visible partition and its conditioning:
  - ontically, the indicator of `vis = v`;
  - on a body, the stage coordinate e_v with p(e_v, x_v) = 1 and p(e_v, x_v′) = 0.

  It must **not** be chosen from `fullEffects` (KF:149). That choice would quantify over the effect space P2 is meant
  to establish.
- For a classical register, r is the barycentric coordinate, again with no quantification over effects.

The output then *becomes* an effect, and is never assumed to be one (written, one line each):
- e ∘ g is affine;
- 0 ≤ e ∘ g ≤ 1 on Ω because g(Ω) ⊆ Ω (`flow_preserves` KF:269, `J_preserves` KF:274);
- sharpness carries over, since (e ∘ g)(g⁻¹x₀) = 1 and (e ∘ g)(g⁻¹y₀) = 0.

In the register form, (u_S ⊗ r) is an effect on every composite between min and max:
- it is nonnegative by the definition of max;
- it is at most u ⊗ u = 1, because u ⊗ (u − r) ≥ 0.

***

## 3. Per-primitive table (deliverable 1)

| primitive | existing equivalent (identifier, file:line; FN = field-neutral) | definable or axiomatized | theorem that fails without it (countermodel) |
| --- | --- | --- | --- |
| 1. Composition, system + register | ontic FN-classical: `RevReal` Eq:157, `hiddenExt` PQ:498 (product of configuration sets; Main.md:358). Matrix: `A × Fin n` (`availExt` OA:599), `tensorOf` MC:193. **Body level: none** | **Definable canonically only for a simplex register**: Ω ⊗ Δ_n, where min = max. For a non-classical register it is **not canonical**: Bell ∈ QM \ min, SWAP/2 ∈ max \ QM (exact MM.*) | **None for the sharp target.** It can be eliminated: `MM.SWAP_transport_relocates_seed` and `MM.CNOT_Naimark_equals_seed` give seed ∘ g. The classical-register composite is useless: `HYB.*` (L3 ⊕ L3, constant readout) |
| 2. Attachment of a register state | ontic: `RevReal.init` (Eq:157; need not be a product). Matrix: `prepAvail_uniform` OA:630; the pure seed is derived from swap control (`pureSeedPrep_available_of_swap` OA:675) | definable given 1 (s ↦ s ⊗ ρ_R) | none for the sharp target (it is eliminated with 1) |
| 3. Sharp register readout | FN predicate `PerfectlyDistinguishable` KF:154. Ontic FN native: visible factor `RevReal.traj` Eq:176, conditioning `quotMeasure_branch` PQ:410. Matrix: `readout` OA:640 (existence postulated), `readout_is_localLuders` OA:658 (form derived) | **Definable on the body** as the image of the visible readout once P1 exists. Sharp by conditioning; on the ball its face is automatically a singleton (BALL.*). Not axiomatized | Without a seed: (SEC) fails, as `not_kInf1_ball3_unit` KF:1089 shows. With an unsharp seed only, β < 1/2 and `lorentz_of_effects` is not reached: tight SIC has β = 1/4 at best, loose SIC has none (SIC.*). With a classical register readout only, transport is vacuous (HYB.*) |
| 4a. Transport (pullback e ↦ e ∘ g) | KF types `e.comp g` but has **no rule** putting it in `avail` (F: "avail is an unconstrained parameter with no link to the flow"). Ontic FN native along the *dynamics*: `RevReal.traj` Eq:176. Matrix: `availExt_bind` (OA, feed-forward composition), `circuit_available` OA:757 | **The single missing primitive.** As a closure it is definable. Its operational licence ("test after an available reversible operation") has no body-level source | {unit, seed, 1 − seed} on ball3: (1,0,0) (`isBoundaryState_ball3` KF:1080) gets 1/2 from both proper members, so (SEC) fails (`FUNCT.*`). Closing under the drive group restores every (1 + b·r)/2 (`ORB.word_*`) |
| 4b. Discard | ontic: `marg` FE:130. Matrix: `ptraceAnc` OA:453, `discardWith` OA:515, `prepAvail_discard` OA:649 | definable given 1: D = u_S ⊗ id, using only the unit | none for the sharp target (eliminated with 1) |

***

## 4. The decisive test (deliverable 2)

**Full register form.**
- On the ontic level it types completely (`RevReal`, `marg`, the visible factor). It yields only 0/1 response
  effects, which are classical (`CL.*`), so the classical control passes.
- On a fixed realization of the ball it cannot produce a sharp effect, in either realization (`SIC.*`):
  - **tight SIC**: the seed (1 + a₁·r)/2 has response coefficients (2, 0, 0, 0). For the z seed, the coefficient
    is 1/2 + √3/2 (= Main.md:540). The best ontic support has β = 1/4, at the four points −aᵢ;
  - **loose SIC**: no boundary state is supported at all, by KF:899.
- So the body-level construction is independent of the realization, and the ontic one is not.

**Body level.** The first untypable arrow is A. Supplying the only canonical composite (the classical register)
makes transport vacuous. Supplying a non-classical one needs a choice of rule, and that choice turns out to be
irrelevant: see §5.

**Reduced form: a genuine field-neutral candidate for P2.**
- Definition: avail∞ := { e ∘ g⁻¹ : e ∈ Seeds, g ∈ G }, closed under complement. Here:
  - Seeds are the native sharp visible readouts (PD pairs);
  - G is the group generated by an available `ElementaryDrivability` (flow and J).
- On ball3 with one seed (1 + z·r)/2:
  - G = SO(3);
  - avail∞ ⊇ { (1 + b·r)/2 : |b| = 1 }, exact via an Euler word (`ORB.word_*`).

  This is precisely the hypothesis of `lorentz_of_effects`, with sharp normalization β = 1/2 and not just
  support.
- D3 (limit closure) is **not** needed when G contains the continuous flow. It is needed only when G is countable,
  as with the fixed-gate theory (Thread G).

**Gbit / square control: the failing step is COVER, together with the drive antecedent.**
- Aut(square) is D4, of order 8 (exact, over all affine maps). So the square has no drive (F: B5), and every
  composite of squares has finite Aut: min is a polytope, max is polyhedral (written). The construction stated with
  G from a drive is therefore vacuous on the square.
- With the finite Aut used instead:
  - a sharp point seed (2 + r₀ + r₁)/4 covers only the 4 vertices. Edge midpoints get 3/4;
  - an edge seed covers the boundary, but with edge faces, which are the gbit's own effects (KF:716). The singleton
    faces then fail (KF:726);
  - the "directional" family is not even an effect family: (1 + b·r)/2 = 6/5 at (1,1) for b = (3/5, 4/5).
- The ball satisfies COVER: every boundary point is extreme, and the drive's SO(3) is transitive on them.
- Note: on the rebit disk the construction works, because SO(2) is transitive. The disk is excluded only at the
  drive antecedent (F: B6), not by this construction.

**Classification: O-FUNCT.** Effect functoriality is what the landed vocabulary lacks.
- Its *non-trivial* instances need reversible maps that move the native axis. Those are K∞-R (D7–D9).
- They are not implementable on any fixed finite ontic realization (Thread G: H4, `substratum_residual` SC:383).

Pressure test of this favourable reduction:
- The scope is rank-one sharp effects on the ball.
- In QM of dimension d ≥ 4, sharp effects of rank 2 also need coarse-graining closure.
- Unsharp (POVM) effects are where a register is genuinely needed.
- `lorentz_of_effects` consumes neither.

***

## 5. Does the composite rule smuggle QM? (deliverable 3; tensor check)

These are exact over Q(i), in Pauli coordinates (`MM.*`):
- the Bell state is in QM and not in min (partial transpose eigenvalue −1/2);
- SWAP/2 is in max (T = I, so 1 + u·v ≥ 0) and not in QM (eigenvalue −1/2);
- CNOT and ZZ(π/4) map products into QM, but each moves a min element out of min and a max element out of max:
  - CNOT sends SWAP/2 to CNOT₂₁/2, whose product value is −1/2;
  - ZZ moves the partial transpose of a rotated Bell state to a product value of −1/2;
- SWAP maps products to products, so it preserves min, max and QM.

Verdict:
1. **For the sharp target the rule is irrelevant.** SWAP transport works identically in min, max and QM, and an
   entangling transport adds nothing (CNOT-Naimark = seed ∘ g). So composite selection is *not* the first missing
   principle.
2. **Requiring an interacting continuous reversible U does smuggle QM.** It preserves neither min nor max; this is
   exact for CNOT and ZZ.
   - Citation: de la Torre–Masanes–Short–Müller, PRL 109, 090403 (2012). For locally tomographic d-ball composites,
     such a U forces d = 3 and the QM composite.
   - A route that relies on entangling transport is O-MATRIX.
3. **Nothing in OI selects a rule.**
   - NB-1 asks only that G and G⁻¹ send *products* into the max cone (NGB header). That is weaker than preserving
     any composite, and CNOT meets it.
   - K2 (the composite) is OPEN (ROADMAP P1-K).
   - Main.md:628: the graph's causal separation does not establish local tomography or a tensor-product
     instrument category.

***

## 6. Proposed next theorems (candidates only; nothing is frozen)

| id | statement | layer | cost |
| --- | --- | --- | --- |
| H1 | `isEffectOn_comp`: `IsEffectOn Ω e → (∀ x ∈ Ω, g x ∈ Ω) → IsEffectOn Ω (e.comp g.toAffineMap)`; `perfectlyDistinguishable_comp` likewise | Lean | cheap |
| H2 | `def transportedReadout Ω G Seeds := {f \| ∃ e ∈ Seeds, ∃ g ∈ G, f = e.comp g.symm}`; `supportingEffectComplete_of_transport`: if every seed is a proper effect, and **COVER** holds (every boundary x lies in g(certainFace e) for some g ∈ G and e ∈ Seeds), then (SEC). This is F's B9 with a sharp seed | Lean | cheap |
| H3 | `ball3_directional_of_drive`: with G the group generated by `ball3Drive.flow` and `cyc3`, `transportedReadout ball3 G {ballEffect e₂} ∋ ballEffect b` for every unit b | Lean | moderate (Euler / ZXZ decomposition) |
| H4 | `transport_classicalRegister_const`: on Ω ⊗ Δₙ with Ω's cone indecomposable, every reversible U is block-permuting, so r_k ∘ D ∘ U ∘ A(·, δ_{k₀}) is constant | Lean (costly) or written plus exact | costly |
| H5 | the composite-rule facts of §5 | exact (done here) | — |

***

## 7. Dependencies and closing statement (deliverable 4)

**Dependencies.**
- On Thread F: B9, B5, B6, and "avail unconstrained".
- On Thread G: C7a (visible readout supports the poles), H4 (the drive is not ontic), the fixed-gate countability
  result, and C8, which this thread refines. Composites are *not* needed.
- Unsourced premises: P1 (the completion body and its visible-readout image), K∞-R (an available group moving the
  readout axis), and COVER.
- Literature for §5.2: citation level, theorem numbers not verified.

**Minimal vocabulary for the generation theorem.**
- V1, the body: a compact convex body Ω in a finite-dimensional real space (KF types; P1 open).
- V2, the reversible maps: a group G of affine automorphisms of Ω, generated by an `ElementaryDrivability` (KF:264;
  K∞-R hypothesis).
- V3, the seed: a native sharp seed, i.e. an available effect pair perfectly distinguishing two states
  (`PerfectlyDistinguishable` KF:154, ι = Fin 2), sourced as the visible readout.
- V4, effect functoriality: availability is closed under e ↦ e ∘ g for g ∈ G. **This is the single missing
  primitive.**
- V5, covering: G · certainFace(seed) ⊇ the relative boundary (a hypothesis; automatic on the ball).

The theorem does not need any of the following: a composite, attachment, discard, a tensor rule, ℂ, or limit
closure (for continuous G).
