# Thread G — does the finite target need #821's transport of an actual stage test?

**Base.** M = `5bfdaba61b535e2fff83d8ba68e73a1b9dbc5dc5`. Kernel `file:line` references are read in a detached worktree at M
(`scratchpad/threads/wt-G`), under `verification/lean-mathlib/OIBridge/` unless another path is given.

Other objects read:
- #821: `origin/draft/kinf-seed-1`, head `9fd622dd`, D = `dee3b5ae`; its preregistration is cited as P821:line.
- The #821 design blob `b6369153` (`StageSeed.lean`).
- The step-4 design at `origin/ccr-ac945020-v97mrh`, `PairInterfaceDesign.lean`, blob `5200a263`, cited as PID:line.
- Threads A, D and E (scratchpad), and PT-STAGE-1 (`origin/draft/pt-stage-1`).

Lean was not compiled here, because there is no local Mathlib cache.

**Labels.** [K] kernel at M · [D] compiled design (branch, commit and run as stated) · [W] written argument made here
· [X] exact computation · [U] unsourced.

This is research only. It changes no status. Correctness bands are unchanged: this is consistency-axis work.

***

## 0. Answer

1. **#821's frozen surface touches no hypothesis of `sharpFamily_subset_avail` in its availability reading.**
   - Theorem 1's output is a `SharpSeed`. That is a chart-body property, and it is free on the ball.
   - The round never mentions `avail` (P821:118: "proves nothing about their availability").
2. **The connection the owner points to exists only as a composite that #821 does not freeze.**
   - The composite takes #821's seed as the base point of V4 (H11).
   - With that base point, "a sharp test is available" becomes a consequence of three things:
     - a sharp stage test;
     - "stage tests are available";
     - "available reversible operations carry available tests to available tests" (`hclose`).
   - The content moves into `hclose`. It is not reduced: given H6 and H8, V4 at the stage seed is equivalent to `hsharp`.
3. **Skeptical finding (NEW).** Read "available" as "carried by a finite stage". Then `hsharp` is false for every
   countably indexed tower, and that covers every `DirectedStages` at M and PT-STAGE-1's `protocolTower` (`ι := ℕ`).
   - `sharpFamily 3` is uncountable.
   - A countable tower carries only countably many tests.
   - The continuum of available sharp tests must therefore come from operations (`hclose`, with `|G| ≥ 𝔠`, which H8
     already forces), or from a limit closure that is assumed nowhere.
   - The dense route (KTRANS-DENSE-1) works with countable test families. But `hsharp` has no dense form.
4. **Need and priority.**
   - The target needs #821's transport only if A's observer model defines `avail` from stage tests (the M1 side).
     Then it is needed for **H11**, not H10.
   - It is necessary there: an unsharp stage test fails. It is not sufficient.
   - It is not needed for:
     - the cone half of step 4;
     - B's matrix route;
     - the bare H10.
   - Priority: below #824 and #822, unless the owner fixes a stage-defined `avail`. In that case #821 must be redrafted
     (§7) before F.

***

## 1. Objects (at M unless marked)

### Stage side

| object | location | content |
|---|---|---|
| `FiniteStage` | KInfFoundations.lean:63 | finite `P`, finite `E`, table `p e x ∈ [0,1]`, unit. Every `e : E` is a test the stage carries; there is no separate availability predicate on stage effects |
| `DirectedStages` | StageCompletion.lean:63 | `ι : Type` (any cardinality), stages, functorial maps |
| `SCInf` | StageCompletion.lean:78 | every forward map carries the table |
| `Label D` | StageCompletion.lean:84 | `Σ i, (D.stage i).E`, the labels of all stage-carried tests |
| `body` | StageCompletion.lean:141 | closed convex hull of the preparation vectors in ℓ^∞(Label D) |
| `coord D a` | StageCompletion.lean:157 | the coordinate functional of a stage test |
| `stageEffects D` | StageCompletion.lean:176 | `range (coord D)`, the completion-level family of stage tests. This is the only stage-derived test family at M |
| `coord_isEffectOn` | StageCompletion.lean:180 | every stage test is an effect on `body`, with no premise |
| `sharpSeed_completion` | StageCompletion.lean:224 | `SCInf` + `p e x1 = 1` + `p e x0 = 0` ⇒ `SharpSeed (body D) (coord D ⟨i, e⟩)` |
| `BinaryVisible` | StageCompletion.lean:244 | a carried binary test `v0`, `v1` |
| `perfectlyDistinguishable_visible` | StageCompletion.lean:274 | A's H9 form |
| `not_scInf_bad` | StageCompletion.lean:350 | control |
| `bitTower` | StageCompletion.lean:393 | the stage tower used as a control, `ι := ℕ` |

### Chart, operations, transport

| object | location | content |
|---|---|---|
| `OpDatum` | CompletionAction.lean:46 | operation datum |
| `AffineRespect` | CompletionAction.lean:58 | respect condition on a datum |
| `Undoes` | CompletionAction.lean:325 | one datum undoes another |
| `CompletionChart` | CompletionAction.lean:144 | chart of the completed body |
| `chartBody` | CompletionAction.lean:166 | the completed body read in the chart |
| `inducedEquiv` | CompletionAction.lean:333 | the affine equivalence an operation datum induces |
| `preservesBody_inducedEquiv` | CompletionAction.lean:352 | the induced equivalences preserve the chart body |
| `isEffectOn_pullback` | CompletionAction.lean:364 | a stage test after an induced map is an *effect*: a geometric statement, not membership |
| `midD` | CompletionAction.lean:404 | control tower, `ι := Bool` |
| `effTr` | OrbitNormalization.lean:159 | transport of an effect along an affine map |
| `sharpSeed_tr` | OrbitNormalization.lean:242 | transport of a sharp seed |
| `seedOrbitAvailable_tr` | OrbitNormalization.lean:285 | transport of V4 |
| `hypotheses_tr` | OrbitNormalization.lean:295 | transport of all four named hypotheses together |
| `effR` | OrbitNormalization.lean:400 | an effect read in the chart |
| `sharpSeed_restrict` | OrbitNormalization.lean:427 | a sharp seed restricted to the chart |

### Orbit side

| object | location | content |
|---|---|---|
| `seedTransport` | OrbitGeneration.lean:49 | `e ∘ g⁻¹` |
| `seedOrbit` | OrbitGeneration.lean:60 | the transports of one seed |
| `SharpSeed` | OrbitGeneration.lean:65 | sharp seed |
| `PreservesBody` | OrbitGeneration.lean:69 | body preservation |
| `SeedOrbitAvailable` | OrbitGeneration.lean:74 | V4 |
| `BoundaryTransitive` | OrbitGeneration.lean:79 | boundary transitivity |
| `seedOrbitAvailable_self` | OrbitGeneration.lean:144 | V4 holds when `avail` is the seed orbit itself |
| `not_seedOrbit_unsharp_eq` | OrbitGeneration.lean:670 | without the zero value, the orbit misses the sharp family for every G |

### Effect side

| object | location | content |
|---|---|---|
| `sharpEff` | EffectSpace.lean:65 | sharp effect along a direction |
| `sharpFamily` | EffectSpace.lean:72 | the sharp effects along unit vectors |
| `sharpEff_sharpSeed` | EffectSpace.lean:118 | every sharp effect is a sharp seed |
| `sharp_eq_of_certain` | EffectSpace.lean:181 | an effect certain at one state and zero at another is sharp |
| `sharpFamily_subset_avail` | EffectSpace.lean:374 | the generation theorem |
| `seedOrbit_eq_sharpFamily` | EffectSpace.lean:401 | under `hG`, `hP1`, `hK`, the seed orbit is the sharp family |
| `maxConeOf` | EffectSpace.lean:411 | the product-test cone of a test family |
| `EffectsOn` | EffectSpace.lean:567 | every member is an effect |
| `maxConeOf_avail_eq` | EffectSpace.lean:572 | the available family determines the cone |
| `not_fullEffects_of_orbit` | EffectSpace.lean:762 | V4 satisfied with a non-mixing-closed family |
| `not_boundaryTransitive_of_countable` | EffectSpace.lean:858 | the unit 2-sphere is uncountable |

### Dense route and pair

| object | location | content |
|---|---|---|
| `DenseBoundaryOrbit` | DenseOrbit.lean:53 | dense form of K∞-Trans |
| `maxConeOf_avail_eq_of_dense` | DenseOrbit.lean:243 | cone equality under a dense boundary orbit |
| `countable_seedOrbit_cone` | DenseOrbit.lean:403 | a countable test family determines `maxCone (eball 3)` |
| `subset_Q3_of_sharp_products_block` | EqvK2MaxCone.lean:186 | upper inclusion from sharp-product tests |
| `maxCone_bound_of_sharp_available` | EqvK2MaxCone.lean:194 | `hvalid` + `hsharp` ⇒ maxCone bound |
| `pairCone_eq_Q3_of_sharp_available` | EqvK2MaxCone.lean:204 | the pair theorem in the available-sharp-test reading |

### Step 4 [D]

`PairInterfaceDesign.lean`, blob `5200a263`, unchanged from `066a69a9` to the session head `4383a150`. Compiled in run
38602502989 (job 115985004293, every step success, including "Check every axiom report").

| object | location |
|---|---|
| `BinaryAvail` | PID:321 |
| `binaryAvail_of_unit` | PID:324 |
| `bPlus`, `bMinus` | PID:340, PID:342 |
| `chsh_attained_of_available` | PID:382 (`hsharp` at :387) |
| `pair_available_eq_Q3_and_chsh` | PID:401 (`hvalid` at :408, `hsharp` at :409) |

***

## 2. Geometric versus availability — classification

"Geometric" means a property of a functional or a family relative to the chart body alone. "Availability" means
membership in a set of tests the observer can perform. "Stage-carried" means the test is an element of some
`(D.stage i).E`.

| object | kind | why (file:line) |
|---|---|---|
| `e : (D.stage i).E` | **stage-carried** (availability in the operational sense) | a field of `FiniteStage` (KInfFoundations.lean:63). Being in `E` is what "the stage carries the test" means; no other predicate exists |
| sharp stage test `p e x1 = 1 ∧ p e x0 = 0` (#821's `h1`, `h0`) | stage-carried, plus an exact table condition | hypothesis form only; no named predicate at M. A's H9 is the stronger BinaryVisible-pair form (StageCompletion.lean:274); H9 ⇒ #821's form via `test` (:244) [W] |
| `stageEffects D` | stage-carried family, completion level | StageCompletion.lean:176. Countable whenever `D.ι` is countable [W] |
| `coord D ⟨i, e⟩`, `effR C.L C.p0 (coord …)`, `effTr A (effR …)` | the same stage test read in completion, chart and normalized coordinates | :157, OrbitNormalization.lean:400, :159. It is the actual test, not a surrogate: its value at `x` is the stage test's value at the completed state `chart (A⁻¹ x)` [W from K] |
| `SCInf`, `FiniteRank`, `CompletionChart`, `chartBody` | structural (stage consistency, chart) | StageCompletion.lean:78, :299; CompletionAction.lean:144, :166 |
| `SharpSeed Ω r` (K∞-Seed, H10) | **geometric** | OrbitGeneration.lean:65: effect on Ω with values 1 and 0. Free on the ball: `sharpEff_sharpSeed` EffectSpace.lean:118 [K] (D §0) |
| `PreservesBody`, `BoundaryTransitive`, `DenseBoundaryOrbit` (H6, H8) | geometric (properties of a family of maps) | OrbitGeneration.lean:69, :79; DenseOrbit.lean:53. Which maps are *available* is K∞-Act (H5), upstream |
| `sharpFamily d`, `seedOrbit G r` | geometric families | EffectSpace.lean:72; OrbitGeneration.lean:60 |
| `SeedOrbitAvailable G r avail` (K∞-V4, H11) | **availability** relative to an arbitrary set | OrbitGeneration.lean:74. Its whole availability content is what `avail` denotes |
| `avail` in EffectSpace, K1Bridge, DenseOrbit, EqvK2MaxCone and PID | **free parameter** | `variable {avail : Set …}` EffectSpace.lean:359; implicit binder at PID:403. No kernel object at M defines a chart-coordinate test set from stage data |
| V4 witnesses at M | geometric sets | `seedOrbit G r` (OrbitGeneration.lean:144, used at EffectSpace.lean:398, DenseOrbit.lean:409, OrbitGeneration.lean:686); `fullEffects (eball 1)` (SharpTests.lean:188, :226); `sharpUnitFamily d` (EffectSpace.lean:765). This is every instantiation found by grep |
| `EffectsOn Ω avail` (H13) | geometric condition on whatever `avail` is | EffectSpace.lean:567 |
| `hvalid : prep ⊆ maxConeOf avail` | validity, relative to `avail` | PID:408; EqvK2MaxCone.lean:194 |
| `hsharp : sharpFamily 3 ⊆ avail` | availability, relative to the free `avail` | PID:409. It is satisfied by `avail := sharpFamily 3` (`Subset.refl`) [W], so it has no content until `avail` is pinned |
| `BinaryAvail avail c` | availability, relative to the free `avail` | PID:321 |
| `HasTwoSharpTests` (H14) | geometric | SharpTests.lean:41 (two `SharpSeed`s) |
| `NativeGateOf Ω avail …` (H17) | geometric gate conditions, with positivity on `maxConeOf avail` | K1Bridge.lean:49 |

**Reading.**
- The kernel's only notion of an available physical test is stage membership (`(D.stage i).E`, `stageEffects`).
- Every consumer of `avail` treats it as an uninterpreted set, and every witness instantiates it geometrically.
- So at M "a sharp test is available" is always an assumption about chart-coordinate functionals. That is the owner's
  point, and it holds in kernel terms.

***

## 3. What #821 transports

**The test transported.** One stage test `e : (D.stage i).E` with `(D.stage i).p e x1 = 1` and
`(D.stage i).p e x0 = 0`, at two preparations of the same stage `i`. It is a single effect: neither BinaryVisible nor
a complementary test is needed.

**Its source.** The finite stage `D.stage i`. It goes through `coord D ⟨i, e⟩` on `body D ⊆ ℓ^∞(Label D)`, the
completion coordinate.

**Its target.** Theorem 1, `sharpSeed_eball_of_stage` (P821 frozen surface; blob `b6369153`):

```lean
SharpSeed (eball C.d) (effTr A (effR C.L C.p0 (coord D ⟨i, e⟩)))
```

That is, the stage test read in the coordinates in which the chart body is the ball.

**Hypotheses of theorem 1.**
- `C : CompletionChart D`;
- `hSC : SCInf D`;
- `h1`, `h0`;
- `A : (Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ)` with `hA : A '' chartBody C = eball C.d`.

Quantifiers: universal over `C`, `i`, `e`, `x1`, `x0` and `A`. There is no `G` and no `avail`.

**Proof.** Three landed lemmas:
1. `sharpSeed_completion` (StageCompletion.lean:224);
2. `sharpSeed_restrict` (OrbitNormalization.lean:427), with `mem_range_of_mem_body`;
3. `sharpSeed_tr` (:242), then a rewrite by `hA`.

**Theorems 2 and 3** (`exists_sharpSeed_eball_of_stage`, `…_dense`).
- They conclude `∃ r, SharpSeed (eball C.d) r`.
- That follows from `hd` alone, so their other hypotheses are idle (D §1(a)).
- They forget which test the seed is. They are therefore useless for any availability reading.

**Availability.** None.
- P821:118: "the round relocates K∞-Seed onto them and proves nothing about their availability."
- `avail`, `V4` and `SeedOrbit` occur nowhere in blob `b6369153`.
- So "available" in #821 means only "carried by stage `i`". It is not the `avail` of EffectSpace, and no map at M
  relates the two.

**Compiled design [D].**
- Run 38091534622: `workflow_dispatch` on `dev-equivalence/split-l3` @ `8c92343e`, based on L = `9f9f8257`.
  - Mathlib bridge job 114328799399: the Build step succeeded and the Release gate step failed (step conclusions
    re-checked here through the Actions API).
  - The log content — `Built OIBridge.StageSeed`, three standard prints, the gate failing only at `lean-manuscript` —
    is as P821's design table and thread D record it. The log download was refused here.
- Earlier: `EqvSeams` §A @ `f5367a7a`, run 38083519826 (job 114305141530, per D).
- Nothing has been built at D or M.
- PR run 38406400225 on `9fd622dd` is a synthetic-merge run of a control-plane-only tree. It is not design evidence.

***

## 4. Does #821 discharge or reduce a hypothesis of `sharpFamily_subset_avail` (availability reading)?

`sharpFamily_subset_avail (hG) (hP1 : SharpSeed (eball d) r) (hK) (hV4 : SeedOrbitAvailable G r avail)`
(EffectSpace.lean:374).

**N1. `hP1` (H10).**
- #821 theorem 1 supplies it for a specific `r`.
- But `hP1` is already supplied on the ball by `sharpEff_sharpSeed (axisVec_sq hd)` [K], with no hypothesis.
- **Verdict: nothing discharged that was not free.** [K]

**N2. `hV4` (H11).** #821 has no `avail`. **Verdict: untouched.** [K + D]

**N3. `hG`, `hK` (H6, H8).** Untouched. #821's theorems 2–3 consume `hT` and do not use it.

**Frozen-surface verdict.** #821 as frozen reduces no hypothesis.

**N4. The composite (not in P821's surface) [W; one-line compositions of K].**
Use `hypotheses_tr A` (OrbitNormalization.lean:295) on the chart-level seed `h2` of #821's proof, then
`sharpFamily_subset_avail`:

```lean
theorem sharpFamily_subset_avail_of_stage {D : DirectedStages} (C : CompletionChart D) (hSC : SCInf D)
    {i : D.ι} {e : (D.stage i).E} {x1 x0 : (D.stage i).P}
    (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0)
    (A : (Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ)) (hA : A '' chartBody C = eball C.d)
    {G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))}
    (hG : PreservesBody (chartBody C) G) (hT : BoundaryTransitive (chartBody C) G)
    {availC : Set ((Fin C.d → ℝ) →ᵃ[ℝ] ℝ)}
    (hV4s : ∀ g ∈ G, seedTransport (effR C.L C.p0 (coord D ⟨i, e⟩)) g ∈ availC) :
    sharpFamily C.d ⊆ effTr A '' availC
```

- This turns H11 into **V4 at the actual stage test**.
- It does not lower the content. By `seedOrbit_eq_sharpFamily` (EffectSpace.lean:401), given `hG`, `hT` and a sharp
  seed, the G-orbit of *any* sharp seed is the whole sharp family.
- So `hV4s` holds iff the sharp family is available (after transport by `A`). The base point changes; what is assumed
  does not.

**N5. The closure form.** This is the only form that turns chart availability into a consequence of stage
availability. Replace `hV4s` by:

```lean
    (hstage : ∀ a : Label D, effR C.L C.p0 (coord D a) ∈ availC)               -- stage tests are available
    (hclose : ∀ g ∈ G, ∀ f ∈ availC, seedTransport f g ∈ availC)              -- test after available operation
```

- Then `hV4s` follows: apply `hclose` to `hstage ⟨i, e⟩`.
- Now every test-side input is a stage object, or an operation acting on one.
- Load-bearing checks:
  - **The sharp stage test is load-bearing** [K]. With `h0` dropped, the orbit misses the sharp family for every G,
    the transitive one included (`not_seedOrbit_unsharp_eq` OrbitGeneration.lean:670).
  - **Mixing cannot replace it** [W from K]. If `sharpEff b = t·e₁ + (1−t)·e₂` (or a sub-convex combination), then
    evaluating at `b` and at `−b` forces each `eᵢ(b) = 1` and `eᵢ(−b) = 0`, so each `eᵢ = sharpEff b` by
    `sharp_eq_of_certain` (EffectSpace.lean:181). Sharp effects are extreme in the effect set, so `MixingClosed` adds
    none.
  - Only a limit closure could, and none is assumed (EffectSpace.lean:37: "No limit closure").

**N6. Skeptical pass on the favourable reading of N5 (§A.31).** Two quantifier and identity checks.

**(a) The identity of "available".**
- #821's "available" is stage membership.
- EffectSpace's `avail` is free.
- N5's `hstage` is the missing map between them, and it has no predicate at M.
- Thread A's H13 reads `avail` as "transported stage effects ∪ seed orbit". **That reading makes H11 definitional**
  (`seedOrbitAvailable_self`, OrbitGeneration.lean:144), which contradicts H11's status "introduced". It also puts the
  orbit into `avail` by fiat, which is exactly the assumption the owner objects to.
- Table (b) has to pick one definition of `avail` and state it.

**(b) Cardinality (NEW).** [W from K]
- *`hsharp` forces `avail` uncountable.* `b ↦ sharpEff b` is injective (`sharpEff b x = ½ + Σ bⱼxⱼ/2`). The unit
  sphere of `Fin 3 → ℝ` is uncountable; this is the argument inside `not_boundaryTransitive_of_countable`
  (EffectSpace.lean:858–870). So `sharpFamily 3 ⊆ avail` implies `¬ avail.Countable`.
- *A countable tower carries countably many tests.*
  - With `D.ι` countable and each `(D.stage i).E` finite (KInfFoundations.lean:63), `Label D` is countable.
  - So `stageEffects D` is countable, and so is its image `effTr A '' (effR C.L C.p0 '' stageEffects D)`.
- *Every tower on record is countable.*
  - `badD` (`ι := Bool`, StageCompletion.lean:342);
  - `bitTower` (`ι := ℕ`, :393);
  - `midD` (`ι := Bool`, CompletionAction.lean:404);
  - PT-STAGE-1's proposed `protocolTower` (`ι := ℕ`, finite stages; `origin/draft/pt-stage-1`, preregistration :75–76).
- **Consequence.** Read `avail` as the stage-carried tests. Then `hsharp`, and V4 under exact H8, is false for every
  tower the corpus has or proposes.
- The continuum must come from somewhere else:
  - from `hclose` with an uncountable G — H8 at d = 3 already forces `|G| ≥ 𝔠` (`not_boundaryTransitive_of_countable`
    [K]), and for a countable tower those operations are not stage-carried;
  - or from an unassumed limit closure.

**(c) The dense route is the countable-compatible one.**
- `countable_seedOrbit_cone` [K] (DenseOrbit.lean:403): a countable test family determines `maxCone (eball 3)`.
- `maxConeOf_avail_eq_of_dense` (:243) needs V4 only along a dense orbit.
- But DenseOrbit's header excludes "EFF-1's availability of every sharp effect", so `hsharp` has no dense form.
- Step 4's cone half uses `hsharp ∧ hvalid` only through `K ⊆ maxConeOf (sharpFamily 3)`
  (`subset_Q3_of_sharp_products_block` EqvK2MaxCone.lean:186, via :194). With a countable `avail` it needs the dense
  bound instead: `prep ⊆ maxConeOf avail ⇒ prep ⊆ maxCone`, by the first inclusion of :243, without `EffectsOn`.

**(d) CHSH.**
- `chsh_attained_of_available` needs the four exact settings `z3`, `xplus`, `bPlus`, `bMinus` (PID:340–342, √2/2
  entries) to be `BinaryAvail`.
- No density premise supplies four specific points. Under dense availability only `sup = 2√2` follows, by continuity
  of `chsh` in the settings [W].

**N4–N6 verdict.**
- #821's transport is the right base point for a stage-sourced H11, and with the composite it is necessary there.
- It reduces H11 only to `hstage ∧ hclose`, and `hclose` carries the content.
- In the strictly stage-carried reading, the exact `hsharp` is unattainable for countable towers.

***

## 5. Which row of A's table it touches, and whether `hsharp` rests on it

**Frozen surface: H10 only.**
- No status changes, because H10 is free on the ball.
- Two corrections for table (b):
  1. H10's [D] citation is `exists_sharpSeed_eball_of_stage`, whose hypotheses are idle. It should be theorem 1,
     `sharpSeed_eball_of_stage`.
  2. In the #821 form H10 needs only the single-effect sharp test (H9′; H9 ⇒ H9′ [W]). So H3 drops out of H10's
     dependency list. H10's dependencies become H1, H2 (chart), H9′ and the ball identification (H6, H8).

**Composite (N4/N5): H11**, and through it the `hsharp` half of H22. Two new rows would be needed, both
*no predicate* at M:
- **H11a**, stage availability `hstage`. This is an M1/M0 definitional link: `ObserverModel.avail τ ⊇` the chart image
  of `stageEffects`.
- **H11b**, operation closure `hclose`, with the G of H8, which must be uncountable at d = 3.

**Does `hsharp` in step 4 / E rest on #821?**
- At PID:409 and in E's H-Corr 3, `hsharp` rests on nothing: `avail` is free and the premise is assumed.
- In A's conditional reading (H22 via `sharpFamily_subset_avail`), it rests on H6, H8, H10 and H11 with *any* seed. The
  free seed suffices, so it does not rest on #821.
- It rests on #821 only once `avail` is pinned to stage data. Then it also rests on H11b and, by N6(b), on an uncountable
  family of available operations.

**If not #821, what would make "a sharp test is available" a consequence of stage availability:**
1. a definition of `avail` from stage data (H11a);
2. operation closure (H11b), or a limit-closure principle (not proposed anywhere);
3. H8 exactly, with `|G| ≥ 𝔠`. Alternatively, the dense route, with step 4 / E restated so that the cone half carries
   the dense bound and the CHSH half carries either `BinaryAvail` of the four settings explicitly or a supremum
   statement.

***

## 6. Verdict on need, and priority relative to #822 and #824

**Not needed for:**
- the cone half of step 4 (PID, EqvK2MaxCone);
- B's route, where `avail` is read through matrix readout projectors (B L6, `InstAvail.readout`) and the base point is
  the register readout that `Architecture.proj` gives;
- the bare H10.

**Needed for** a field-neutral F1 whose `avail τ` is defined from the stages (A's M1). There it is needed for **H11**,
in the composite form of §4 N4/N5.
- It is necessary: an unsharp stage test fails, by `not_seedOrbit_unsharp_eq` [K].
- It is not sufficient: H11b carries the content.
- If A keeps `avail τ` as a primitive field (A §a.4), #821 does not bear on the target at all.

**Relative priority:**
1. **#824 KTRANS-SEP-1.** A kernel separation for H8. Every `hsharp` route needs H8, and N6(b) shows that in exact form
   it forces a continuum of available operations. It bears on the premise that actually carries the availability
   continuum.
2. **#822 KINF-COPY-1.** The only draft that weakens a chain premise (H16). Its reach is DIM-1's absolute selector until
   the relative `NativeGateOf` form is added (D §2).
3. **#821 KINF-SEED-1.** As frozen it reduces nothing. It rises only if the owner fixes a stage-defined `avail`, and then
   only after a redraft (§7).

D's order stands. The reason is refined: the yield is small not because the seed is free, but because the availability
content sits in H11b, which #821 does not touch.

***

## 7. What #821's package would need before F

**Content.**
1. Drop theorems 2–3, or recast them as an explicit countercontrol: `∃ r, SharpSeed (eball C.d) r` follows from `hd`
   alone. A statement with idle hypotheses cannot certify the relocation it is cited for.
2. Add the composite to the frozen surface in both forms:
   - N4, `hV4s`;
   - N5, `hstage` + `hclose` ⇒ `sharpFamily C.d ⊆ effTr A '' availC`.

   Also consider a dense variant, which concludes `maxConeOf (effTr A '' availC) ⊆ maxCone (eball C.d)` under
   `DenseBoundaryOrbit`.
3. Add the scope guard as kernel lemmas, or at least state it in the non-inference rule:
   - `sharpFamily 3 ⊆ avail → ¬ avail.Countable`;
   - `Countable D.ι → (stageEffects D).Countable`.

   The non-inference rule should say that the stage-carried tests of a countable tower cannot contain the sharp family,
   so H11b, not the stage test, carries the continuum.
4. Controls for the composite:
   - `h0` load-bearing (`not_seedOrbit_unsharp_eq`);
   - SC∞ load-bearing (`not_scInf_bad`);
   - `hT` load-bearing (`not_boundaryTransitive_flow` OrbitGeneration.lean:620);
   - `hclose` load-bearing, by the cardinality lemma, for a countable tower;
   - a positive control. No tower at M has a ball chart body, so either the control is at the ball level with
     `availC := seedOrbit`, or the gap is stated.
5. Wording.
   - The licensed ROADMAP sentence (P821 HP-1: "so its remaining content is the stage-level sharp test") overstates the
     result: K∞-Seed has no remaining content on the ball. Suggested: "the seed can be taken to be a sharp stage test
     read in the ball's coordinates (`sharpSeed_eball_of_stage`); V4's availability content is unchanged."
   - The non-inference rule must add that `avail` is not defined and that `hstage` and `hclose` are not sourced.

**Mechanics (from D §1(b), still open at M).**
- Choose the base, D or M. If D is kept, the census goes in `landing.resolved_paths`.
- Fix the header: it contains the forbidden S4 phrase "design module".
- Fix the preamble mismatch between blob `b6369153` (`open … CompositeDimension K2Guard …`, `noncomputable section`)
  and the frozen one-line `open`.
- Add the missing S2 line for `coord` (StageCompletion.lean:157).
- Write `controls.py` with self-test and mutations.
- Build and dispatch the predicted execution tree.
- Run the exact-head `check-run` at `F`.
- The composite in item 2 changes the frozen surface, so the predicted-tree build is a first measurement, not a re-take.

***

## 8. Assumption-watch markers (cross-propagation)

**AW-G1 — `hsharp` presupposes an uncountable available family.** [W from K]
- It applies to:
  - `hsharp` in step 4 (PID:387, :409);
  - E's H-Corr 3;
  - E's Q-down (`C_q ⊆ B_OI` needs uncountably many available settings);
  - A's (→) conclusion "available tests = all effects";
  - B's L6 k-fold `sharpFamilyK ⊆ avail`.
- None of these can be stage-carried over a countable tower.
- Each must name its source of the continuum: H11b, a limit closure, or an uncountable stage index. Otherwise it must be
  restated up to closure (dense availability, `sup` for CHSH).

**AW-G2 — the same cardinality bound holds for operations.** [W]
- `𝒯.ShadowQuantum` makes uncountably many typed instruments available.
- Words over a countable protocol menu (PT-STAGE-1: `Fintype A`) are countable.
- So an exact-QM conclusion needs uncountably many available operations, or a limit closure.
- This shares an ingredient with A's R1 flag (continuous control). No formal map is claimed (§A.34 / bridge rule).

**AW-G3 — `avail` is free in every field-neutral consumer at M.** Any status line saying "the sharp tests are
available" must name the set. "Available" in #821, in EffectSpace and in PID are three uses of one word, with no map
between them at M.

***

## 9. Summary (10 lines)

1. At M, `SharpSeed` is geometric and free on the ball. `avail` is a free set in every consumer, and every V4 witness instantiates it geometrically [K].
2. The only kernel notion of an available physical test is stage membership `(D.stage i).E` / `stageEffects D`. No map ties it to `avail` [K].
3. #821 transports one stage test (`p e x1 = 1`, `p e x0 = 0`) from `D.stage i` through `coord`, `effR` and `effTr A` to `SharpSeed (eball C.d)` of that exact functional, under `SCInf`, a chart and `A '' chartBody C = eball` [D: blob b6369153, run 38091534622 at L; not built at D or M].
4. As frozen it touches only H10, which is free, so it discharges nothing. Theorems 2–3 have idle hypotheses. It never mentions availability (P821:118).
5. The composite (not frozen) makes #821's seed the base point of H11. Given H6 and H8, "V4 at the stage seed" ⟺ `hsharp`, so the content is not reduced (EffectSpace.lean:401) [W from K].
6. Chart availability becomes a consequence of stage availability only via `hstage` ∧ `hclose` (test-after-operation closure). Neither has a predicate at M. The sharp stage test is necessary (N2 control, :670) but not sufficient.
7. NEW: `hsharp` forces an uncountable `avail`. Every tower on record (badD, bitTower, midD, protocolTower) is countable, so its stage-carried tests are too. The continuum must come from operations (`|G| ≥ 𝔠`, forced by H8) or from an unassumed limit closure [W from K :858].
8. The dense route accepts countable tests for the cone (DenseOrbit.lean:403). `hsharp` and exact CHSH settings have no dense form, so step 4 / E must name the continuum's source or be restated with a dense bound and `sup`.
9. Need: none for the cone half, B's matrix route or bare H10. For H11 it is needed only if A defines `avail` from stages (M1). Table (b) should fix `avail`'s definition, cite theorem 1 and add rows H11a and H11b.
10. Priority: #824 > #822 > #821. Before F, #821 needs theorems 2–3 dropped, the N4/N5 composites plus the cardinality guard and controls added, the HP-1 wording narrowed, and D's mechanical items done.
