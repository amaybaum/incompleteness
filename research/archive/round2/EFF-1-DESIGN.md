# Round `EFF-1` ("local-effect reconstruction on the ball") — design, read-only

Drafting snapshot `D` = `afa66d16d7adaffe94fb9bac391e6039c51dad8a` (current `main`, TRB-1's landing, verified
`git rev-parse HEAD`). Every kernel citation below is `identifier` + `file:line`, read at `D` in the detached worktree
`scratchpad/wt-eff1` under `verification/lean-mathlib/OIBridge/`. Mathlib is the pinned tag `v4.33.0`; every Mathlib
name is marked **[V]** when it was found by grep in the local clone `scratchpad/wave2/N/mathlib-v4.33.0` (file:line
given) or is used by a landed module (using site given), and **[MV]** when it still has to be verified in the design
run. Nothing here is landed, governed or committed; no branch, no CI, no file of the repository was changed.

Abbreviations: KF `KInfFoundations`, OG `OrbitGeneration`, ON `OrbitNormalization`, NGB `NativeGateBall`,
SC `StageCompletion`, CA `CompletionAction`, IIP `InvariantInnerProduct`, TB `TransitiveBody`.

Evidence levels used below: **kernel** (landed at `D`), **new** (to be proved by the round; each marked elementary or
not), **written** (an argument given here, not a kernel statement), **reading** (a manuscript-level identification
that no kernel statement makes).

***

## 0. The finding stated up front

The owner's target reads: "the effect space is exactly the family `e_b(r) = (1 + b·r)/2`, `|b| ≤ 1`, the full local
effect space of the qubit". Two things in that sentence do not coincide, and the round must choose which it proves:

- The family `{(1 + b·r)/2 : |b| ≤ 1}` is the set of **unbiased** effects: the affine functionals that are effects on
  the ball and take the value `1/2` at the centre. It is `convexHull ℝ directionalFamily` (§3, E4/E5).
- The **full** effect space of the ball — every affine functional with values in `[0, 1]` on the ball, which is the
  qubit's effect space under the reading `(1 + b·r)/2 ↔ (1 + b·σ)/2` — is strictly larger. It is the set of
  **sub-convex combinations of the unit with one sharp directional effect**, `α·1 + β·(1 + b·r)/2` with `|b| = 1`,
  `α, β ≥ 0`, `α + β ≤ 1`; equivalently `convexHull ℝ ({0, 1} ∪ directionalFamily)` (§3, E2/E3).
- The gap is witnessed by a landed object: OG-1's `unsharpSeed = 3/4 + z/4` (OG:626) is an effect on `ball3`
  (`unsharpSeed_isEffectOn`, OG:640) and is not of the form `(1 + b·r)/2` for any `b` (its value at the centre is
  `3/4`). It is the qubit effect `(3/4)·1 + (1/4)·σ_z`, with eigenvalues `1` and `1/2`.

So "the full local effect space of the qubit" is the sub-convex span, not the `|b| ≤ 1` family. Both are provable
and both are cheap; they need different closure premises (the unbiased family needs convex mixing only; the full space
needs the unit and sub-convex mixing, i.e. the zero effect or complementation as well). Decision 1 in §10.

The second finding: **no limit closure is needed** for either statement under the landed hypotheses. OG-1's
`BoundaryTransitive` is exact transitivity, every sharp directional effect is reached by one transport
(`ballEffect_mem_avail`, OG:369), and the non-sharp effects are finite mixtures. Limit closure becomes load-bearing
only when exact transitivity is replaced by closure-transitivity (a countable repertoire), and the round can carry the
kernel countercontrol that a countable family is never `BoundaryTransitive` on `ball3` (§5, C7).

***

## 1. Inventory of the landed vocabulary the theorem consumes

| id | identifier | statement at `D` | where |
|---|---|---|---|
| L1 | `IsEffectOn Ω e` | `∀ x ∈ Ω, 0 ≤ e x ∧ e x ≤ 1`, `e : V →ᵃ[ℝ] ℝ` | KF:116 |
| L2 | `IsProperOn`, `certainFace`, `IsBoundaryState` | proper: some state gives `e < 1`; boundary state read in `Ω` alone (segment clause) | KF:125, 120, 130 |
| L3 | `SupportingEffectComplete`, `SingletonFaces`, `fullEffects Ω := {e \| IsEffectOn Ω e}` | the effect-side premises of KINF-2; `fullEffects` is the no-restriction family | KF:135, 139, 149 |
| L4 | `ball3 := {v \| v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2 ≤ 1}`, `mem_ball3`, `ball3_convex`, `ball3_isCompact`, `vec3_ext` | the Euclidean unit ball by its quadratic form, not the sup norm | KF:311–335 |
| L5 | `ballEffect u := 1/2 + (u·v)/2`, `ballEffect_apply` | the directional effect, as an `AffineMap` built from `AffineMap.const` and `LinearMap.proj` | KF:1026–1033 |
| L6 | `supportingEffectComplete_ball3`, `kInf1_ball3_full`, `not_kInf1_ball3_unit`, `isBoundaryState_ball3` | (SEC) and K∞-1 for `ball3` with its full effects; fail with the unit alone | KF:1053–1094 |
| L7 | `ElementaryDrivability` (fields `flow`, `flow_add`, `flow_continuous`, `t₀`, `N_involutive`, `J`, `J_off_axis`) | the drive; **not consumed** by this round | KF:264–276 |
| L8 | `seedTransport e g := e.comp g.symm`, `seedOrbit G r := {r ∘ g⁻¹ : g ∈ G}` | transport and orbit | OG:49, 60 |
| L9 | `SharpSeed Ω r := IsEffectOn Ω r ∧ (∃ x ∈ Ω, r x = 1) ∧ (∃ y ∈ Ω, r y = 0)` | **P1, the sharp seed** | OG:65 |
| L10 | `PreservesBody Ω G := ∀ g ∈ G, ∀ x ∈ Ω, g x ∈ Ω ∧ g.symm x ∈ Ω` | **G-AUT, the reversible orbit** (each member and its inverse preserve the body) | OG:69 |
| L11 | `SeedOrbitAvailable G r avail := ∀ g ∈ G, seedTransport r g ∈ avail` | **V4′** | OG:74 |
| L12 | `BoundaryTransitive Ω G := ∀ x y, IsBoundaryState Ω x → IsBoundaryState Ω y → ∃ g ∈ G, g x = y` | **K∞-R, exact all-boundary transitivity** | OG:79 |
| L13 | `CoversBoundaryFrom Ω G x₀ := ∀ y, IsBoundaryState Ω y → ∃ g ∈ G, g x₀ = y` | **boundary covering** from one state; `coversBoundaryFrom_of_transitive` | OG:83, 187 |
| L14 | `directionalFamily := {e \| ∃ b, b 0 ^ 2 + b 1 ^ 2 + b 2 ^ 2 = 1 ∧ e = ballEffect b}` | the sharp directional family — what thread R (`wave2/R/RESULT.md:55,176`) calls the **T0 family**; no kernel identifier is named `T0` | OG:205 |
| L15 | `ballEffect_sharp`, `ballEffect_isEffectOn`, `ballEffect_self`, `ballEffect_neg_self`, `neg_mem_ball3` | every member of the family is a sharp seed on `ball3` | OG:208–236 |
| L16 | `isBoundaryState_ball3_of_sphere`, `sphere_of_isBoundaryState_ball3` | boundary states of `ball3` are the unit sphere, one theorem per direction | OG:239, 246 |
| L17 | `affine3_apply r v : r v = r 0 + v 0 * r.linear ![1,0,0] + …` | an affine functional on `ℝ³` in coordinates | OG:258 |
| L18 | `ball3_sharp_eq (he : IsEffectOn ball3 r) (h1 : r u = 1) (h0 : r w = 0) : \|u\|² = 1 ∧ r = ballEffect u` | sharpness forces the directional normalization | OG:278 |
| L19 | `seedOrbit_ball3_eq (hG) (hP1) (hK) : seedOrbit G r = directionalFamily` | **the reduced orbit-generation theorem** (OG-1's principal) | OG:348 |
| L20 | `ballEffect_mem_avail (hG) (hP1) (hK) (hV4) : ∀ b, (∑ j, b j ^ 2) = 1 → ballEffect b ∈ avail` | **the landed generation half**: every sharp directional effect is available | OG:369 |
| L21 | `supportingEffectComplete_ball3_of_orbit`, `kInf1_ball3_of_orbit`, `lorentz_of_seedOrbit`, `lorentz_of_available` | consumers of L20; the bridge to NGB | OG:382–428 |
| L22 | `fullAut3`, `preservesBody_fullAut3`, `boundaryTransitive_fullAut3`, `seedOrbit_fullAut3`, `hh3` | the positive control family (Householder reflections) | OG:521–561 |
| L23 | `unsharpSeed = 3/4 + z/4`, `unsharpSeed_isEffectOn`, `unsharpSeed_bounds` (`1/2 ≤ · ≤ 1`), `not_sharpSeed_unsharp` | OG-1's N2 control; a biased effect | OG:626–655 |
| L24 | `lorentz_of_effects (p) (hp : 1 ≤ p) (x0) (v) (h : ∀ b, ∑ b j ^ 2 = 1 → 0 ≤ x0 + ∑ b j * v j)` | the Lorentz test over the unit-sphere-indexed family; its proof is the `Real.sqrt` pattern (`r := √(∑ v j ^ 2)`, `b := -v/r`) this round reuses | NGB:105–142 |
| L25 | `words S`, `preservesBody_words` | subgroup closure of a generator set; G-AUT under words | ON:53, 79 |
| L26 | `effTr T e := e ∘ T.symm`, `effTr_apply`, `effTr_comp`, `conjTr`, `isEffectOn_tr`, `hypotheses_tr` | transport of effects, automorphisms and the four named hypotheses along `T : V ≃ᵃ[ℝ] W` | ON:159–302 |
| L27 | `seedOrbit_eq_of_normalization (T) (hT : T '' Ω = ball3) …` | the orbit equality in any coordinates | ON:307 |
| L28 | `chart`, `bodyR`, `effR L p0 e := e.comp (chart L p0)`, `isEffectOn_restrict`, `sharpSeed_restrict`, `hypotheses_restrict` | restriction to an affine chart of the body's span | ON:357–560 |
| L29 | `body D := closure (convexHull ℝ (range (prepVec D)))`, `coord D a`, `stageEffects D := range (coord D)`, `stageEffects_isEffectOn`, `coord_unit_eq_one` | the completion body and its stage-effect interface: **every stage effect is an effect on the body, no premise** | SC:141–211 |
| L30 | `sharpSeed_completion (hSC : SCInf D) …`, `boundary_completion` | the sharp seed on the completion under SC∞ | SC:224, 232 |
| L31 | `CompletionChart D`, `chartBody C := bodyR C.L C.p0 (body D)`, `isEffectOn_pullback` | the chart body; a stage effect read after an induced map is an effect on the chart body | CA:144, 166, 364 |
| L32 | `chartBody_isCompact`, `chartBody_convex`, `chartBody_interior_nonempty` | the completed-chart adapter | TB:109, 80, 121 |
| L33 | `exists_affine_image_eq_eball (hd : 0 < d) (hc) (hconv) (hi) (hG : PreservesBody Ω G) (hT : BoundaryTransitive Ω G) : ∃ A, A '' Ω = eball d` | **the ball theorem of TRB-1** | TB:602 |
| L34 | `chartBody_eq_eball`, `eball d := {x \| ∑ j, x j ^ 2 ≤ 1}`, `eball_three : eball 3 = ball3` | the completed-body form and the `d = 3` identification | TB:651, 518, 671 |
| L35 | `invariant_inner_product`, `invMatrix`, `centroid` | the invariant form behind TB's `A` (`qnorm_eq_sum_sq`, TB:581) | IIP:336, 311, 125 |
| L36 | `ClosureAvail` (ℂ, `FiniteOperationalTheory (Fin 2)`) | the only landed limit-closure predicate; outcome-wise ε-approximation of channels; **not field-neutral, not consumed** | DiscreteCompletion:63 |

Not landed anywhere: a convex-closure or mixing predicate on an effect family; a unit-availability predicate; the
decomposition of an effect on the ball into sharp effects and the unit; a field-neutral limit closure of effects
(thread P, `wave2/P/RESULT.md` §2(b): "LIMIT … deliberately not adopted"); a convexity statement for `fullEffects`.

### What the four phrases of the target mean as landed predicates

| phrase | landed predicate | status |
|---|---|---|
| sharp seed | `SharpSeed ball3 r` (L9); on the completion, `sharpSeed_completion` under SC∞ (L30) | named hypothesis, sourced for no OI construction |
| reversible orbit | `PreservesBody ball3 G` (L10): `G` a set of affine automorphisms, each with its inverse preserving the body; TRB-1's `IsBodyGroup` (TB:223) is the group form and is not needed here | named hypothesis |
| boundary covering | `BoundaryTransitive ball3 G` (L12), or the weaker `CoversBoundaryFrom ball3 G x₀` from the seed's certain state (L13); the generation theorem L19 takes the former, the (SEC) theorem OG:174 the latter | named hypothesis (K∞-R); open per ROADMAP K∞ |
| limit closure | **no landed field-neutral predicate**; the nearest objects are `body D` (the closed convex hull of preparations, a closure on the state side, L29) and `ClosureAvail` (ℂ, L36) | not needed by the theorem under exact transitivity (§4, N4) |
| V4′ | `SeedOrbitAvailable G r avail` (L11); thread P decomposes it as SEED-AVAIL ∧ SEQ ∧ TRANS± with countermodels, none landed | named hypothesis |
| T0 family | `directionalFamily` (L14), the hypothesis set of `lorentz_of_effects` (L24) | kernel |

***

## 2. The theorem, precisely

### 2.1 The effect-space object

Two sets are in play, and the theorem is about their equality:

- `avail : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ)` — the family of available effects, a premise-level object (OG-1 proves things
  *about* `avail` under V4′ and never defines it; CMP-1's result note: the corpus "does not decide which effects the
  completion makes available");
- `fullEffects ball3` (L3) — every affine functional with values in `[0, 1]` on the ball: the no-restriction family.

The "effect space is exactly the family" statement is therefore `avail = fullEffects ball3`, together with the
premise-free description of `fullEffects ball3` in terms of the T0 family. Per §A.34 each equality is two theorems.

### 2.2 The three layers

**Layer I — geometry of the ball's effects (premise-free; new).** Write `unitEffect := AffineMap.const ℝ _ 1`
and, for a family `S`,

```
unitSpan S := {e | ∃ f ∈ S, ∃ α β : ℝ, 0 ≤ α ∧ 0 ≤ β ∧ α + β ≤ 1 ∧ e = α • unitEffect + β • f}.
```

- **E1 (coefficient bounds).** For `e` with `IsEffectOn ball3 e`, writing `c = e 0` and `a_j = e.linear e_j`
  (L17): `0 ≤ c ≤ 1`, `∑ a_j² ≤ c²` and `∑ a_j² ≤ (1 − c)²`.
- **E2 (upper bound, the substantive direction).** `fullEffects ball3 ⊆ unitSpan directionalFamily`: with
  `s = √(∑ a_j²)`, either `s = 0` and `e = c • unitEffect + 0 • ballEffect e_z`, or `b := a / s` lies on the sphere
  and `e = (c − s) • unitEffect + (2 s) • ballEffect b`, with `c − s ≥ 0` and `(c − s) + 2 s = c + s ≤ 1` by E1.
- **E3 (lower bound).** `unitSpan directionalFamily ⊆ fullEffects ball3`: `α + β·(1 + b·v)/2 ∈ [α, α + β] ⊆ [0, 1]`
  by `ballEffect_isEffectOn` (L15).
- **E4 (the owner's family).** `unbiasedFamily := {e | ∃ b, ∑ b_j² ≤ 1 ∧ e = ballEffect b}` equals
  `convexHull ℝ directionalFamily`: `⊆` by the two-point combination
  `ballEffect b = ((1+s)/2) • ballEffect (b/s) + ((1−s)/2) • ballEffect (−b/s)` for `s = |b| > 0` (and
  `ballEffect 0 = (1/2) • ballEffect e_z + (1/2) • ballEffect (−e_z)`); `⊇` because `b ↦ ballEffect b` is affine and
  `ball3` is convex (`ball3_convex`, L4), so the image is convex and contains the sphere's image.
- **E5 (the owner's family is the unbiased slice).** `e ∈ unbiasedFamily ↔ IsEffectOn ball3 e ∧ e 0 = 1/2`, two
  theorems: `→` from E3 with `α = 0`-type bounds (`ballEffect_apply`); `←` from E1 with `c = 1/2`, so
  `∑ a_j² ≤ 1/4` and `e = ballEffect (2a)`.
- **E6 (the gap).** `unitEffect ∉ unbiasedFamily`, `unsharpSeed ∈ fullEffects ball3 ∧ unsharpSeed ∉ unbiasedFamily`
  (value `3/4` at the centre, `unsharpSeed_apply`, OG:630).

**Layer II — generation into `avail` (conditional; new, elementary on top of L20).** With the closure premises

```
MixClosed avail := ∀ e ∈ avail, ∀ f ∈ avail, ∀ α β, 0 ≤ α → 0 ≤ β → α + β ≤ 1 → α • e + β • f ∈ avail
ConvexClosed avail := ∀ e ∈ avail, ∀ f ∈ avail, ∀ α β, 0 ≤ α → 0 ≤ β → α + β = 1 → α • e + β • f ∈ avail
```

- **G1 (full space).** `PreservesBody ball3 G`, `SharpSeed ball3 r`, `BoundaryTransitive ball3 G`,
  `SeedOrbitAvailable G r avail`, `unitEffect ∈ avail`, `MixClosed avail` ⟹ `fullEffects ball3 ⊆ avail`.
  Proof: E2 writes `e = α • unitEffect + β • ballEffect b`; `ballEffect b ∈ avail` by L20; mix.
- **G2 (unbiased family).** The same four OG-1 hypotheses and `ConvexClosed avail` ⟹ `unbiasedFamily ⊆ avail`
  (E4's two-point combination; no unit needed).

**Layer III — the upper bound (premise).** `EffectsOn ball3 avail := ∀ e ∈ avail, IsEffectOn ball3 e`, i.e.
`avail ⊆ fullEffects ball3`. This is the statement "available things are effects on the body"; it is a consistency
premise (thread P's `eff_effect` field), not a theorem, except where the family is the completion's own stage
effects, for which it is the landed `stageEffects_isEffectOn` (L29) transported by `isEffectOn_restrict` (L28) and
`isEffectOn_tr` (L26). With it:

- **U1.** `avail = fullEffects ball3` from G1's hypotheses and `EffectsOn ball3 avail`
  (`Set.Subset.antisymm hE (fullEffects_subset_avail …)`).

So the direction "every effect is a sub-convex combination of a sharp effect with the unit" (the task's (ii)) is
**E2, premise-free geometry**; the direction "every such combination is available" (the task's (i)) is **G1**, which
is L20 plus mixing; and "no extra effects" is **definitional** once `avail ⊆ fullEffects` is granted. There is no
no-restriction *hypothesis*: no-restriction is U1's conclusion, given the mixing premises.

### 2.3 What is landed and what is new

| piece | status | identifier |
|---|---|---|
| the sharp family is exactly the seed orbit | kernel | `seedOrbit_ball3_eq` (L19) |
| every sharp directional effect is available | kernel | `ballEffect_mem_avail` (L20) |
| every effect on `ball3` is a sub-convex combination of the unit and one sharp effect (E2) | new, elementary (`Real.sqrt` pattern of L24, `affine3_apply` L17, `nlinarith`) | `fullEffects_ball3_subset_unitSpan` |
| the converse E3 | new, elementary | `unitSpan_subset_fullEffects_ball3` |
| the unbiased family is the convex hull of the sharp family (E4), and the unbiased slice (E5) | new, elementary | `unbiasedFamily_eq_convexHull`, `mem_unbiased_of_half`, `unbiased_isEffectOn_half` |
| generation of the full space (G1) and of the unbiased family (G2) | new, elementary | `fullEffects_subset_avail`, `unbiasedFamily_subset_avail` |
| the equality U1 | new, trivial from G1 and the premise | `avail_eq_fullEffects` |
| the chart-body form at `d = 3` | new, elementary from L26, L33, L34 | `avail_eq_fullEffects_of_ball` (§6) |
| convexity of `fullEffects Ω` for any `Ω` (used by the positive control) | new, elementary (`Convex.combo_affine_apply` **[V]** AffineMap.lean:945, used at SC:184) | `mixClosed_fullEffects` |

### 2.4 Is convexity/closure of the effect set a premise or derived?

For `avail`, a **premise** (`MixClosed` or `ConvexClosed`): nothing landed gives the available family any closure
beyond V4′ (thread P §1: "nothing anywhere states that … availability is closed under sequential composition", and
likewise under mixing). For `fullEffects ball3`, **derived** (`mixClosed_fullEffects`). The round must not let the
first be read as the second: control C2 (§5) keeps `MixClosed` load-bearing.

***

## 3. Depth-first walk (nodes closed by a check)

Productivity test, fixed before the walk: a node is a gem iff it yields a fact strictly stronger than "the ball's
effects are the convex hull of the sharp ones" and either constrains the frozen statement or exposes a hidden
assumption; otherwise record-only.

- **N1 — what is "the effect space"?** Grep at `D`: `avail` is bound only by `SeedOrbitAvailable` (OG:74) and the
  `avail` arguments of KF's predicates; `fullEffects` is KF:149. Verdict: the theorem is `avail = fullEffects ball3`
  plus a description of `fullEffects ball3`. Closed.
- **N2 — is the owner's family the full qubit effect space?** Check: `unsharpSeed` (OG:626) has `IsEffectOn ball3`
  (OG:640) and value `3/4` at `0`; every `ballEffect b` has value `1/2` at `0` (`ballEffect_apply`). So
  `{ballEffect b : |b| ≤ 1} ⊊ fullEffects ball3`. Verdict: **the target sentence conflates the unbiased slice with
  the full space; NEW** (it changes the frozen statement). Closed by E5/E6.
- **N3 — which direction is landed?** L20 gives `directionalFamily ⊆ avail`. Nothing landed mixes effects. Verdict:
  generation of the sharp family is landed; mixing, the unit and the decomposition are new. Closed.
- **N4 — is limit closure needed?** Under `BoundaryTransitive` every sphere point is `g e_z` for some `g ∈ G`
  exactly (`seedOrbit_ball3_eq`), and E2 is a finite combination. Verdict: **not needed**. It is needed only if the
  hypothesis is weakened to closure-transitivity; thread N's Hamel model and thread P's rational-angle model (E8) are
  the written witnesses; the kernel-cheap witness is C7 (a countable `G` is never `BoundaryTransitive` on `ball3`,
  since the sphere is uncountable). CONFIRMING (thread P's G3), with a new kernel-level control.
- **N5 — hidden dependences.** See §4. The only one that is not a landed theorem is the *meaning* of `b·r` as the
  invariant inner product, which is written, not kernel. ELABORATING.
- **N6 — circularity of the mixing premise.** `MixClosed` and `unitEffect ∈ avail` do not mention the seed orbit or
  the conclusion set; with `avail := fullEffects ball3` they hold (C+) and the conclusion is an identity; with
  `avail := unitSpan (seedOrbit G r)` they hold and the content is E2. Verdict: the premises are not the conclusion
  restated; the content of the full-space statement is E2 (geometry) plus L20. Closed.
- **N7 — skeptic pass on E2 (favorable branch).** Boundary cases: `c = 0` forces `a = 0` and `e = 0 = 0•1 + 0•f`;
  `c = 1` forces `e = 1`; a sharp effect has `c = 1/2, s = 1/2`, so `α = 0, β = 1`, consistent with
  `ball3_sharp_eq`; `unsharpSeed` has `c = 3/4, s = 1/4`, so `e = (1/2)•1 + (1/2)•ballEffect e_z`, which evaluates to
  `3/4 + z/4`. The weights are forced: `β = 2s` is determined by `e.linear`, `α = c − s` by `e 0`. Closed.
- **N8 — does E2 need `d = 3`?** The argument is Cauchy–Schwarz plus a unit vector; it holds on `eball d` for every
  `d ≥ 1` (`Finset.sum_mul_sq_le_sq_mul_sq` **[V]** Algebra/Order/BigOperators/Ring/Finset.lean:159). But its only
  consumer, L20, is stated on `ball3`, and a general-`d` `ballEffect` would be a new definition parallel to KF's.
  Verdict: state at `d = 3` on `ball3` with the landed `ballEffect`; the general form is optional (Decision 3).

Fixed point: a second pass over N2–N8 and a circularity pass (no step imports `avail = fullEffects`, no step uses
NB-1, no step uses a drive) produced no new node.

***

## 4. Hidden dependences

| question | answer | evidence |
|---|---|---|
| Does the result need the invariant inner product to identify `b·r`? | **For the statement on `ball3`: no.** `b·r` is the coordinate dot product of `Fin 3 → ℝ`, the form that defines `ball3` (L4). **For the statement on a completed body: yes, through TRB-1.** The affine `A` with `A '' Ω = eball 3` (L33) is built from `invMatrix Ω` (`qnorm_eq_sum_sq`, TB:581), so in `A`-coordinates the dot product is the invariant form of IIP-1 about the centroid, up to the radius. That `A` is unique up to a Euclidean isometry of `eball 3` (so that `b` is canonical up to rotation) is **written**: it needs "every affine automorphism of `eball d` is orthogonal", which is not landed (it would follow from `invariant_inner_product` applied to `eball d` and `invMatrix (eball d) = λ • 1`, neither stated). | L33, L35; written |
| Does it need `d = 3` other than at the final identification? | Only through the landed objects: `ballEffect`, `directionalFamily`, L18–L20 are `ball3` statements, and the chart-body corollary uses `eball_three` (L34). The decomposition E2 is dimension-free in content (N8). No theorem of the round *derives* `d = 3`; the chart corollary takes `C.d = 3` (or a body in `Fin 3 → ℝ`) as an input — the dimension-selector round's output. | L19, L34 |
| Does it need the drive or any flow? | **No.** Every hypothesis is on a set `G` of affine automorphisms (L10, L12); OG-1 is drive-free. `ElementaryDrivability` (L7) is not consumed; guard S2 forbids the tokens. | OG-1 result note |
| Does ℂ or a matrix representation enter? | **No ℂ.** Real matrices enter only inside TRB-1's proof of L33 (`invMatrix`), behind the statement `∃ A`. The module imports no `Matrix … ℂ` object; guard S1 forbids the token `ℂ`. The identification `(1 + b·r)/2 ↔ (1 + b·σ)/2` with the qubit is a **reading**; the kernel has no map from `ball3` effects to `Matrix (Fin 2) (Fin 2) ℂ` (KF §F's `qubit_certain_face`, KF:995, is a statement of the imported kinematics with no bridge to `ballEffect`). | KF:995; guard S1 |
| Does it need SC∞, `BinaryVisible`, finite rank? | Not on `ball3`. On the completed body: `CompletionChart D` (L31) is data whose existence needs finite rank (CA:154); the sharp seed on the completion needs SC∞ (L30). Both stay named hypotheses, as in CMP-1/TRB-1. | L30, L31 |
| Does it need V4′? | Yes, through L20, for both G1 and G2; C3 shows it load-bearing. Thread P's decomposition of V4′ is not consumed. | L11, L20 |
| Does it need a unit-availability premise? | For the full space, yes (C2b: the unbiased family satisfies every other premise and misses the unit). For the unbiased family, no. On the completion the unit is a stage effect with `coord_unit_eq_one` (L29), so the premise is discharged there once `avail` is defined to contain the stage effects; that definition is not landed. | L29 |
| Does it need limit closure? | No (N4). | — |

***

## 5. Lean feasibility at `v4.33.0`

### 5.1 Per step

| step | elementary? | route | Mathlib names |
|---|---|---|---|
| `unitEffect`, `unitSpan`, `MixClosed`, `ConvexClosed`, `EffectsOn`, `unbiasedFamily` | definitions | over `V` a real normed space (`unitSpan`, `MixClosed`, `EffectsOn`) and `Fin 3 → ℝ` (`unbiasedFamily`); the `Module R (P1 →ᵃ[k] V2)` instance is the anonymous instance **[V]** AffineMap.lean:727 (already exercised by `ballEffect`, KF:1026, which adds and scales affine maps) | — |
| E1 | yes, ~40 lines | `affine3_apply` (L17) gives `c, a0, a1, a2`; `c ∈ [0,1]` at `v = 0`; if `A := ∑ a_j² > 0`, `s := √A`, test `v = a/s` and `v = −a/s` (in `ball3` since `∑ (a_j/s)² = A/s² = 1`): `c + s ≤ 1`, `c − s ≥ 0`; square. | `Real.sqrt_pos` **[V]** Analysis/Real/Sqrt.lean:286, `Real.sq_sqrt` :178, `Real.sqrt_nonneg` :144 (all used at NGB:125–142); `div_pow`, `mul_inv_cancel₀` (NGB:133) |
| E2 | yes, ~50 lines | case `s = 0`: `a = 0` by `Finset.sum_eq_zero_iff_of_nonneg` (NGB:112 pattern), `e = c • unitEffect + 0 • ballEffect e_z`; case `s > 0`: `AffineMap.ext` **[V]** AffineMap.lean:133 and `ballEffect_apply`, `AffineMap.coe_add` :251, `coe_smul` :222, `Pi.add_apply`, `Pi.smul_apply`, `smul_eq_mul`, `AffineMap.const_apply` :174; `field_simp`/`ring` | as listed |
| E3 | yes, ~15 lines | `ballEffect_isEffectOn` (L15), `nlinarith` | — |
| E4 | yes, ~60 lines | `⊆`: explicit two-point `segment`; `⊇`: `convexHull_min` **[V]** Analysis/Convex/Hull.lean:64 with convexity of `unbiasedFamily` from `ball3_convex` and affinity of `b ↦ ballEffect b` (`AffineMap.ext`, `ring`) | `subset_convexHull` :50, `segment_subset_convexHull` :101, `convexHull_pair` :123, `Convex.segment_subset` **[V]** Analysis/Convex/Basic.lean:63, `segment_eq_image'` **[V]** Segment.lean:207 |
| E5 | yes, ~30 lines | `→`: `ballEffect_apply` at `0` and E3-type bounds; `←`: E1 at `c = 1/2`, `b := 2a`, `AffineMap.ext` | — |
| E6 | yes, ~15 lines | `unsharpSeed_apply` (OG:630), `ballEffect_apply`, `norm_num` | — |
| `mixClosed_fullEffects`, `unitEffect_mem_fullEffects` | yes, ~15 lines | `Convex.combo_affine_apply` **[V]** AffineMap.lean:945 (SC:184) does not apply to `α + β ≤ 1` directly; evaluate with `coe_add`/`coe_smul` and `nlinarith` | — |
| G1, G2 | yes, ~20 lines each | E2 (or E4) then `ballEffect_mem_avail` (L20) with `Fin.sum_univ_three` **[V]** Algebra/BigOperators/Fin.lean (`prod_univ_three` :119, additive version used at OG:375) | — |
| U1 | trivial | `Set.Subset.antisymm` | — |
| chart-body form on `Ω : Set (Fin 3 → ℝ)` | yes, ~40 lines | L33 at `d = 3` with `eball_three` (L34) gives `A '' Ω = ball3`; `hypotheses_tr A` (L26) transports the four OG-1 hypotheses; `effTr A unitEffect = unitEffect` (`rfl` up to `AffineMap.ext`), `MixClosed` transports because `effTr A` is linear in `e` (`AffineMap.ext`), `EffectsOn` transports by `isEffectOn_tr` (ON:217); then U1 on `effTr A '' avail` | — |
| C7 (countable control) | yes, ~40 lines | if `BoundaryTransitive ball3 G` with `G` countable, the sphere `⊆ (fun g => g e_z) '' G` is countable (`Set.Countable.image` **[V]** Data/Set/Countable.lean:161, `Countable.mono` :115); the curve `t ↦ ![t, √(1 − t²), 0]` maps `Icc (−1) 1` into the sphere injectively (first coordinate), so `Icc (−1) 1` is countable by `Set.MapsTo.countable_of_injOn` **[V]** :174, contradicting `Real.Icc_countable_iff` **[V]** Analysis/Real/Cardinality.lean:291 | `isBoundaryState_ball3_of_sphere` (L16), `Real.sq_sqrt` |
| C3, C4, C5 (restricted families) | yes, ~20 lines each | membership/non-membership by evaluation at a named point (`![1,0,0]`, `![0,0,1/2]`), `norm_num`, `Matrix.cons_val_*` (OG:604) | — |

Nothing in the round needs a Lie-group, density, Haar or classification fact; nothing needs `convexHull` beyond
Hull.lean's basic API, and the frozen principal statements use `unitSpan` (explicit weights), so the `convexHull`
form E4 is the only place that API enters.

### 5.2 The cheapest provable kernel chain

```
affine3_apply (OG:258) ──▶ E1 ──▶ E2 (fullEffects ball3 ⊆ unitSpan directionalFamily)
ballEffect_isEffectOn (OG:224) ──▶ E3 (⊇)                                   ──▶ fullEffects_ball3_eq
ballEffect_mem_avail (OG:369) + E2 + unitEffect ∈ avail + MixClosed ──▶ G1 ──▶ (with EffectsOn) U1
ballEffect_mem_avail + E4(⊆) + ConvexClosed ──▶ G2
exists_affine_image_eq_eball (TB:602) + eball_three (TB:671) + hypotheses_tr (ON:295) + U1 ──▶ the body form
```

Every arrow is a finite computation on three coordinates or a one-line transport; the only analytic object is
`Real.sqrt` of a nonnegative sum, in the exact pattern of `lorentz_of_effects`.

### 5.3 Controls and countercontrols (each a kernel theorem with its print)

| id | witness on `ball3` | holds | fails | conclusion | shows |
|---|---|---|---|---|---|
| C+ | `avail := fullEffects ball3`, `G := fullAut3`, `r := ballEffect e_z` | all of G1's hypotheses (`seedOrbit_fullAut3` ⊆ `fullEffects` by `ballEffect_isEffectOn`; `mixClosed_fullEffects`; `unitEffect_mem_fullEffects`; `EffectsOn` by definition) | — | `avail = fullEffects ball3` | joint satisfiability |
| C1 | `avail := unitSpan directionalFamily` | same | — | equality holds and is E2/E3 | the premises are not the conclusion restated (N6) |
| C2a | `avail := {unitEffect, 0} ∪ directionalFamily` | V4′, unit, `EffectsOn` | `MixClosed` | `ballEffect ![0,0,1/2] ∈ fullEffects ball3 ∖ avail` | mixing is load-bearing |
| C2b | `avail := unbiasedFamily` (the owner's family) | V4′, `ConvexClosed`, `EffectsOn` | `unitEffect ∈ avail` | `unsharpSeed ∈ fullEffects ball3 ∖ avail` | the unit is load-bearing; the owner's family is a proper subset (E6) |
| C3 | `avail := unitSpan {ballEffect e_z, ballEffect (−e_z)}` (the classical-bit effects embedded in the ball), `G := fullAut3` | unit, `MixClosed`, `EffectsOn`, `SharpSeed`, `BoundaryTransitive` | V4′ (`ballEffect e_x ∉ avail`) | `ballEffect e_x ∈ fullEffects ball3 ∖ avail` | V4′ is load-bearing; a restricted effect space on the ball with a sharp seed and a transitive orbit |
| C4 | `G := {AffineEquiv.refl}`, `avail := unitSpan {ballEffect e_z}` | unit, `MixClosed`, `EffectsOn`, `SharpSeed`, V4′ (`seedTransport r refl = r`) | `BoundaryTransitive` | `ballEffect e_x ∉ avail` | transitivity is load-bearing (drive-free witness; OG-1's `not_boundaryTransitive_flow` is the flow witness and is not re-cited, to keep S2) |
| C5 | `avail := Set.univ` | everything except `EffectsOn` | `EffectsOn` | `2 • unitEffect ∈ avail ∖ fullEffects ball3` | the upper bound is exactly `EffectsOn` |
| C6 | `unsharpSeed` | `IsEffectOn ball3` (OG:640) | `unbiasedFamily` membership | — | E6 |
| C7 | any countable `G` | — | `BoundaryTransitive ball3 G` | — | exact transitivity needs an uncountable repertoire; a countable repertoire would need limit closure, which the round does not adopt |

C2b is the control the owner's wording makes necessary: it is exactly the `|b| ≤ 1` family, it satisfies every
hypothesis of the generation theorem except unit availability, and it is not the full effect space.

### 5.4 Semantic guards for `controls.py` (TRB-1 style; each with a mutation control)

- **N1–N3** as TRB-1: declaration list and kinds in order; every theorem signature up to `:=` and every definition
  whole; preamble and context lines; no `sorry`, `admit`, `axiom`, `native_decide`; every frozen `#print axioms`
  line present.
- **S1 field-neutral.** The tokens `ℂ`, `Complex`, `RCLike`, `conjTranspose`, `ᴴ`, `PosSemidef`, `Matrix`, `trace`,
  `qubit`, `Bloch`, `Pauli`, `σ`, `density` occur nowhere in the module, header included. Mutation: a docstring
  naming the qubit.
- **S2 no drive, no flow.** The tokens `ElementaryDrivability`, `flow`, `Flow`, `rot3`, `rotFun`, `cyc3`,
  `ball3Drive`, `driveWords3`, `J_off_axis`, `t₀` occur nowhere in the module. Mutation: C4 restated with
  `Set.range rot3`.
- **S3 directional witnesses.** `fullEffects_ball3_eq` is proved by `Set.Subset.antisymm` naming
  `fullEffects_ball3_subset_unitSpan` and `unitSpan_subset_fullEffects_ball3`; `unbiasedFamily_eq_convexHull`
  likewise names its two directions; no theorem statement contains `↔` with `fullEffects` or `avail` on one side and
  `unitSpan` or `convexHull` on the other; E5 is two theorems. Mutation: one direction removed.
- **S4 exact hypothesis sets.** `fullEffects_subset_avail` has exactly the binders `PreservesBody ball3 G`,
  `SharpSeed ball3 r`, `BoundaryTransitive ball3 G`, `SeedOrbitAvailable G r avail`, `unitEffect ∈ avail`,
  `MixClosed avail`; `unbiasedFamily_subset_avail` has the four OG-1 hypotheses and `ConvexClosed avail`;
  `avail_eq_fullEffects` adds `EffectsOn ball3 avail` and nothing else; none of them has `LimitClosed`, `closure`,
  `Continuous`, `IsBodyGroup`, `TransBody`, `Countable` among its binders. Mutation: a `LimitClosed` hypothesis added.
- **S5 no sourcing.** Outside `section Controls`, no theorem concludes `SharpSeed`, `SeedOrbitAvailable`,
  `BoundaryTransitive`, `PreservesBody`, `MixClosed`, `ConvexClosed`, `EffectsOn` or `unitEffect ∈ _` without the
  same predicate among its hypotheses; no declaration name or header claims a source for V4′, the seed, transitivity,
  mixing, dimension three or SC∞. Mutation: a theorem `mixClosed_of_seedOrbitAvailable`.
- **S6 dimension.** No theorem has `BoundaryTransitive` among its hypotheses and `finrank`, `C.d`, or `Module.finrank`
  in its conclusion; the only `eball` statement is the body form, whose body lives in `Fin 3 → ℝ` by hypothesis (or
  carries `C.d = 3` as a hypothesis, Decision 4). Mutation: a theorem concluding `C.d = 3`.
- **S7 no limit closure on the spine.** The tokens `LimitClosed`, `closure`, `Tendsto`, `Filter` occur only inside
  `section Controls` (C7) and, if Decision 5 admits it, inside a clearly delimited `section Limit`; no principal
  theorem names them. Mutation: `closure` in G1's statement.
- **S8 controls present.** C+, C1–C7 are theorems with `#print axioms` lines. Mutation: C2b's print removed.
- **S9 the gap is stated.** E6 (`unsharpSeed_not_unbiased`, `unitEffect_not_unbiased`) are theorems with prints.
  Mutation: E6 demoted to a comment.
- **I, C, F** as TRB-1: `OIBridge.lean` is `D`'s with exactly one import line inserted after
  `import OIBridge.TransitiveBody`; the census is `D`'s with exactly one family inserted after the TRB-1 family; the
  preregistration unchanged from `F`, `delta(D, F)` the preregistration alone.

***

## 6. Typed theorem skeleton (signatures up to `:=`)

Module `OIBridge/EffectSpace.lean`, namespace `OIBridge.EffectSpace`.

```lean
import OIBridge.TransitiveBody
import Mathlib.Analysis.Convex.Join                 -- convexHull_pair, convexJoin (E4 only)

namespace OIBridge
namespace EffectSpace

open Set KInfFoundations OrbitGeneration OrbitNormalization TransitiveBody

section Vocabulary
variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-- The unit effect. -/
def unitEffect : V →ᵃ[ℝ] ℝ := AffineMap.const ℝ V (1 : ℝ)
theorem unitEffect_apply (x : V) : unitEffect x = 1
/-- Sub-convex combinations of the unit with one member of `S`. -/
def unitSpan (S : Set (V →ᵃ[ℝ] ℝ)) : Set (V →ᵃ[ℝ] ℝ) :=
  {e | ∃ f ∈ S, ∃ α β : ℝ, 0 ≤ α ∧ 0 ≤ β ∧ α + β ≤ 1 ∧ e = α • unitEffect + β • f}
/-- MIX: an available family closed under sub-convex binary mixtures. -/
def MixClosed (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  ∀ e ∈ avail, ∀ f ∈ avail, ∀ α β : ℝ, 0 ≤ α → 0 ≤ β → α + β ≤ 1 → α • e + β • f ∈ avail
/-- CONV: closure under convex binary mixtures. -/
def ConvexClosed (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  ∀ e ∈ avail, ∀ f ∈ avail, ∀ α β : ℝ, 0 ≤ α → 0 ≤ β → α + β = 1 → α • e + β • f ∈ avail
/-- EFF-ON: every available functional is an effect on `Ω`. -/
def EffectsOn (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop := ∀ e ∈ avail, IsEffectOn Ω e

theorem mixClosed_of_convexClosed_of_zero {avail : Set (V →ᵃ[ℝ] ℝ)} (hc : ConvexClosed avail)
    (h0 : (0 : V →ᵃ[ℝ] ℝ) ∈ avail) : MixClosed avail
theorem unitEffect_mem_fullEffects (Ω : Set V) : unitEffect ∈ fullEffects Ω
theorem mixClosed_fullEffects (Ω : Set V) : MixClosed (fullEffects Ω)
theorem effectsOn_iff_subset {Ω : Set V} {avail : Set (V →ᵃ[ℝ] ℝ)} :
    EffectsOn Ω avail ↔ avail ⊆ fullEffects Ω          -- definitional unfolding, both sides the same set
end Vocabulary

section Ball
/-- The unbiased directional family `{(1 + b·v)/2 : |b|² ≤ 1}`. -/
def unbiasedFamily : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ) :=
  {e | ∃ b : Fin 3 → ℝ, b 0 ^ 2 + b 1 ^ 2 + b 2 ^ 2 ≤ 1 ∧ e = ballEffect b}

-- E1
theorem effect_coeff_bounds {e : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ} (he : IsEffectOn ball3 e) :
    0 ≤ e 0 ∧ e 0 ≤ 1 ∧
      e.linear ![1, 0, 0] ^ 2 + e.linear ![0, 1, 0] ^ 2 + e.linear ![0, 0, 1] ^ 2 ≤ e 0 ^ 2 ∧
      e.linear ![1, 0, 0] ^ 2 + e.linear ![0, 1, 0] ^ 2 + e.linear ![0, 0, 1] ^ 2 ≤ (1 - e 0) ^ 2
-- E2 / E3
theorem fullEffects_ball3_subset_unitSpan : fullEffects ball3 ⊆ unitSpan directionalFamily
theorem unitSpan_subset_fullEffects_ball3 : unitSpan directionalFamily ⊆ fullEffects ball3
theorem fullEffects_ball3_eq : fullEffects ball3 = unitSpan directionalFamily
-- E4
theorem unbiasedFamily_subset_convexHull : unbiasedFamily ⊆ convexHull ℝ directionalFamily
theorem convexHull_directional_subset_unbiased : convexHull ℝ directionalFamily ⊆ unbiasedFamily
theorem unbiasedFamily_eq_convexHull : unbiasedFamily = convexHull ℝ directionalFamily
-- E5
theorem unbiased_isEffectOn_half {e : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ} (h : e ∈ unbiasedFamily) :
    IsEffectOn ball3 e ∧ e 0 = 1 / 2
theorem mem_unbiased_of_half {e : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ} (he : IsEffectOn ball3 e) (h0 : e 0 = 1 / 2) :
    e ∈ unbiasedFamily
-- E6
theorem unitEffect_not_unbiased : unitEffect ∉ unbiasedFamily
theorem unsharpSeed_not_unbiased : unsharpSeed ∉ unbiasedFamily
theorem unsharpSeed_mem_fullEffects : unsharpSeed ∈ fullEffects ball3      -- restates OG:640 in the new vocabulary
end Ball

section Generation
variable {G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))} {r : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ}
  {avail : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ)}
-- G1
theorem fullEffects_subset_avail (hG : PreservesBody ball3 G) (hP1 : SharpSeed ball3 r)
    (hK : BoundaryTransitive ball3 G) (hV4 : SeedOrbitAvailable G r avail)
    (hU : unitEffect ∈ avail) (hM : MixClosed avail) : fullEffects ball3 ⊆ avail
-- G2
theorem unbiasedFamily_subset_avail (hG : PreservesBody ball3 G) (hP1 : SharpSeed ball3 r)
    (hK : BoundaryTransitive ball3 G) (hV4 : SeedOrbitAvailable G r avail)
    (hC : ConvexClosed avail) : unbiasedFamily ⊆ avail
-- U1 (the second direction is the premise `hE`)
theorem avail_eq_fullEffects (hG : PreservesBody ball3 G) (hP1 : SharpSeed ball3 r)
    (hK : BoundaryTransitive ball3 G) (hV4 : SeedOrbitAvailable G r avail)
    (hU : unitEffect ∈ avail) (hM : MixClosed avail) (hE : EffectsOn ball3 avail) :
    avail = fullEffects ball3
end Generation

section Body
variable {Ω : Set (Fin 3 → ℝ)} {G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))}
  {r : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ} {avail : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ)}
theorem effTr_unitEffect (A : (Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)) : effTr A unitEffect = unitEffect
theorem mixClosed_tr (A : (Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)) (hM : MixClosed avail) :
    MixClosed (effTr A '' avail)
theorem effectsOn_tr (A : (Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)) (hE : EffectsOn Ω avail) :
    EffectsOn (A '' Ω) (effTr A '' avail)
/-- The body form: a compact convex body with interior in `ℝ³`, boundary transitive under a reversible
orbit, with a sharp seed whose orbit is available, the unit available, mixing, and available functionals
effects, has the full effect space of the ball in the coordinates of TRB-1's normalization. -/
theorem avail_eq_fullEffects_of_ball (hc : IsCompact Ω) (hconv : Convex ℝ Ω)
    (hi : (interior Ω).Nonempty) (hG : PreservesBody Ω G) (hK : BoundaryTransitive Ω G)
    (hP1 : SharpSeed Ω r) (hV4 : SeedOrbitAvailable G r avail) (hU : unitEffect ∈ avail)
    (hM : MixClosed avail) (hE : EffectsOn Ω avail) :
    ∃ A : (Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ), A '' Ω = ball3 ∧ effTr A '' avail = fullEffects ball3
end Body

section Controls
-- C+ / C1 … C6 as in §5.3, e.g.
theorem avail_fullEffects_control :
    SeedOrbitAvailable fullAut3 (ballEffect ![0, 0, 1]) (fullEffects ball3) ∧
      unitEffect ∈ fullEffects ball3 ∧ MixClosed (fullEffects ball3) ∧ EffectsOn ball3 (fullEffects ball3)
def bitFamily : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ) := unitSpan {ballEffect ![0, 0, 1], ballEffect ![0, 0, -1]}
theorem bitFamily_mixClosed : MixClosed bitFamily
theorem bitFamily_effectsOn : EffectsOn ball3 bitFamily
theorem not_seedOrbitAvailable_bitFamily : ¬ SeedOrbitAvailable fullAut3 (ballEffect ![0, 0, 1]) bitFamily
theorem ballEffect_ex_not_mem_bitFamily : ballEffect ![1, 0, 0] ∉ bitFamily
theorem unbiasedFamily_convexClosed : ConvexClosed unbiasedFamily
theorem seedOrbitAvailable_unbiased : SeedOrbitAvailable fullAut3 (ballEffect ![0, 0, 1]) unbiasedFamily
theorem not_mixClosed_discrete : ¬ MixClosed ({unitEffect, 0} ∪ directionalFamily)
theorem ballEffect_half_not_mem_discrete : ballEffect ![0, 0, 1 / 2] ∉ {unitEffect, 0} ∪ directionalFamily
theorem not_boundaryTransitive_refl : ¬ BoundaryTransitive ball3 {AffineEquiv.refl ℝ (Fin 3 → ℝ)}
theorem not_effectsOn_univ : ¬ EffectsOn ball3 (Set.univ : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ))
-- C7
theorem not_boundaryTransitive_of_countable {G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))}
    (hG : G.Countable) : ¬ BoundaryTransitive ball3 G
end Controls

/-- The verdict: E2/E3, E4, E5, E6, G1, G2, U1, the body form, and the controls, together. -/
theorem eff1_core : … ∧ … := …

end EffectSpace
end OIBridge
```

Statements the preregistration must **not** contain: any `↔` between `avail` and `fullEffects`; any theorem with
`LimitClosed` or `closure` on the generation spine; any theorem concluding a dimension; any theorem naming the qubit.

***

## 7. Dependency map

```
KF: IsEffectOn, fullEffects, ball3, ballEffect, ball3_convex ─────────────────────────────┐
OG: SharpSeed, PreservesBody, SeedOrbitAvailable, BoundaryTransitive, directionalFamily,  │
    affine3_apply, ballEffect_isEffectOn, ballEffect_mem_avail (L20), unsharpSeed ────────┤
ON: effTr, conjTr, hypotheses_tr, isEffectOn_tr ──────────────────────────────────────────┤
TB: exists_affine_image_eq_eball (L33), eball_three (L34) ────────────────────────────────┤
Mathlib: Real.sqrt lemmas, AffineMap.ext/coe_add/coe_smul, convexHull basics, countability ┘
          │
          ▼
  E1 → E2, E3 → fullEffects_ball3_eq            E4, E5, E6 (the owner's family and the gap)
          │                                         │
  L20 + E2 + unit + MixClosed → G1          L20 + E4 + ConvexClosed → G2
          │
  G1 + EffectsOn → U1 ──(hypotheses_tr, L33, L34)──▶ avail_eq_fullEffects_of_ball
          │
  consumers downstream (not this round): lorentz_of_available (OG:422) already takes `avail ⊇ directionalFamily`;
  a composite round (K2) would consume `fullEffects ball3 = unitSpan directionalFamily` as the local effect cone.
```

Not consumed, by design: `ElementaryDrivability`, `words`, `driveWords3`, `rot3`, `IsBodyGroup`, `TransBody`,
`invMatrix` (behind L33's `∃`), `SCInf`, `BinaryVisible`, `FiniteRank`, NB-1's `nb1_kernel_core`, anything of ℂ.

***

## 8. Freeze boundary

- **Governed paths** (`v3-governed-paths`): record `AM verification/programmes/oi-qm/reconstruction/round-eff-1-effect-space/`;
  record `AM verification/receipts/EFF-1.json`; execution `A verification/lean-mathlib/OIBridge/EffectSpace.lean`;
  execution `M verification/lean-mathlib/OIBridge.lean` (one line, `import OIBridge.EffectSpace`, inserted after
  `import OIBridge.TransitiveBody`, which is the last OIBridge import at `D`, `OIBridge.lean:252`); execution
  `M verification/lean-manuscript-census.json` (one family after the TRB-1 family, `status: kernel-only`,
  `manuscript: []`, modules `["EffectSpace"]`). No manuscript, no `ROADMAP.md`, no workflow, no probe.
- **Frozen at `F`:** the preregistration; `controls.py` embedding the statement surface of the module (every
  definition whole, every theorem signature up to `:=`, in order, preamble and context lines, the `#print axioms`
  list), the import insertion, the census family text, the outcome vocabulary. Proofs are not frozen (the design-run
  rule of OG-1/TRB-1: repairs change proofs only).
- **Design runs before `F`**, on a disposable branch, for Mathlib-name verification only: the `[MV]`-free list of
  §5.1 is already grep-verified; the design run confirms elaboration of `α • unitEffect + β • f` through the anonymous `Module` instance on affine maps,
  `Real.Icc_countable_iff`, `Set.MapsTo.countable_of_injOn`, and the `convexHull` API on the affine-map module.
- **Stages:** C1 `controls.py`; S1 the module, the import line and the census family; proof-only repairs; S2 the
  result note (candidate `E`). Exact-head `workflow_dispatch` runs at `F` and `E`, as §A.39 requires.
- **Census family name (proposal):** "the local effect space of the ball — the sub-convex span of the unit and the
  sharp directional family, its generation from a sharp seed under a boundary-transitive reversible orbit with
  mixing, and the unbiased slice (round EFF-1, reconstruction)".

***

## 9. Outcomes (the decision rule, preregistered)

- **`EFF-1-EFFECT-SPACE-PROVED`** — `controls.py check E --freeze F` prints `controls: OK`; the exact-head run at `E`
  is green on every job, the Mathlib bridge building `EffectSpace` with every frozen `#print axioms` within
  `[propext, Classical.choice, Quot.sound]`, the release gate passing. The result note may say exactly: on `ball3`,
  the effects are the sub-convex combinations of the unit with one sharp directional effect, two directions; the
  unbiased family `{(1 + b·r)/2 : |b| ≤ 1}` is the convex hull of the sharp family and the slice of effects with value
  `1/2` at the centre, and is a proper subset of the effect space; under `PreservesBody`, `SharpSeed`,
  `BoundaryTransitive`, V4′, unit availability and mixing, every effect on the ball is available, and with
  `EffectsOn` the available family is exactly the effect space; the same in the TRB-1 coordinates of any compact
  convex boundary-transitive body in `ℝ³`; each premise load-bearing by a named control; a countable family is never
  boundary transitive. It says nothing about the qubit, ℂ, a drive, dimension three for any body not already in
  `ℝ³`, limit closure, or any OI sourcing of the seed, the orbit, V4′, the unit or mixing.
- **`EFF-1-HALTED`** — anything else; the result note names the failing check or job; the round halts under `S12`.

Correctness bands are unchanged by either outcome: the round is consistency-axis work (every hypothesis is a named,
unsourced premise, and the geometry is a retrodiction of the qubit's known effect space).

***

## 10. Decisions for the owner (at most five)

1. **Which family is the target.** (a) The full effect space `fullEffects ball3 = unitSpan directionalFamily` with
   premises unit + `MixClosed` (recommended: it is the qubit's effect space under the reading, and U1 is the
   no-restriction conclusion); (b) the unbiased family `{(1 + b·r)/2 : |b| ≤ 1}` with `ConvexClosed` only, as the
   owner's sentence literally states; (c) both, with E6 recording that (b) is a proper slice of (a) (recommended
   form of (a)). The result note's first sentence depends on this choice.
2. **The shape of the mixing premise.** `MixClosed` (sub-convex, one predicate) versus `ConvexClosed` plus the zero
   effect, versus `ConvexClosed` plus complementation `e ∈ avail → unitEffect − e ∈ avail` (operationally the other
   outcome of the binary test; `unitEffect − ballEffect b = ballEffect (−b)`). The three are interderivable with the
   unit present (`mixClosed_of_convexClosed_of_zero`); the frozen generation theorem names one.
3. **Dimension of the geometry layer.** State E1–E3 on `ball3` with the landed `ballEffect` (recommended, cheapest,
   matches L20 exactly), or additionally on `eball d` with a new `sphereEffect d b` and Cauchy–Schwarz
   (`Finset.sum_mul_sq_le_sq_mul_sq`), at the cost of a parallel definition whose `d = 3` instance must be proved
   equal to `ballEffect`.
4. **The completed-body form.** State it on `Ω : Set (Fin 3 → ℝ)` (as in §6; the chart-body instance with
   `C : CompletionChart D` and `C.d = 3` is then a cast exercise left to the dimension-selector round), or state it
   directly on `chartBody C` with the hypothesis `C.d = 3`, which costs a `Fin C.d`/`Fin 3` transport in the
   statement itself.
5. **Limit closure.** Keep it out entirely (recommended; C7 is the only closure-side statement and it is a
   countercontrol), or admit an optional `section Limit` with a field-neutral `LimitClosed Ω avail` (uniform
   approximation on `Ω`) and the theorem that under closure-transitivity (`∀ x y` on the sphere,
   `y ∈ closure {g x | g ∈ G}`) and `LimitClosed` the sharp family is available — which needs the continuity bound
   `|ballEffect b v − ballEffect b' v| ≤ |b − b'|/2` on the ball and is the first adoption of a D3-type closure in
   the field-neutral vocabulary, which thread P recommended against while D3 stays unadopted.

***

## Owner decisions (2026-10-04)

The narrowing is accepted. OG-1 supplies the directional family (`seedOrbit_ball3_eq`); EFF-1 freezes two logically
separate targets, each its own theorem with its own hypotheses:

1. **Generation / completion.** With an explicitly named convex (sub-convex) mixing closure on the available effects,
   the directional family and the unit generate the whole affine qubit effect family. The mixing closure is a premise
   unless derived elsewhere; it is never read as a theorem of this round.
2. **Upper bound.** Independently, every admissible effect on `ball3` has the form `e(r) = a + v·r` with
   `‖v‖ ≤ min(a, 1 − a)`; no additional effects are admissible. Stated and proved apart from generation.

Limit closure is not part of the frozen surface (exact transitivity makes it unnecessary); the countable-family
control may remain as a control only.
