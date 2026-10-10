# Round `ORD-1` ("composition order") — design, read-only

Drafting snapshot `D` = `7c821261e2537a97b85ab78ae50c6998600bc019` (verified `git log -1` at `scratchpad/wt-r2`). Every
kernel citation below is `identifier` + `file:line` read at `D` in `verification/lean-mathlib/OIBridge/`; Mathlib is the
pinned tag `v4.33.0` with no checkout here, so every Mathlib name is marked **[MV]** (to verify in the design run) unless a
landed module at `D` already uses it, in which case the using site is cited as the verification. Abbreviations: KF
`KInfFoundations`, OG `OrbitGeneration`, ON `OrbitNormalization`, SC `StageCompletion`, CA `CompletionAction`.

Charter (owner, verbatim intent): "ORD∞ composition-closure / finite-order controls; keep TRANS ⇒ ORD∞ explicitly out of
scope." Depends on OPACT-1 and the current operation laws only; branches from exactly `D`; consumes nothing of TRB-1
(no import of `OIBridge.TransitiveBody`, no citation of its theorems; ORD-1 defines its own predicates).

***

## 0. What the round tests, and the fact it must keep visible

```
reversible AffineRespect datum of infinite order   ⟹   every power is a nontrivial AffineRespect datum   (C2; composition law `after` iterated)
reversible AffineRespect datum, stage-preserving   ⟹   finite order on the finite-rank chart body       (D7; DRIVE F-D3)
finite, composition-closed symmetry set            ⟹   no infinite-order member                           (E8)
finite, NOT composition-closed set                 ⟹   may have one: `{rot3 1}`                           (E7c, the countercontrol)
```
ORD∞ genuinely uses composition closure: both D7 and E8 pass through iterated composition. The ball route of the sibling
round uses none (its design §5 H3), and `TRANS ⇒ ORD∞` for composition-closed groups needs Jordan–Schur/Cartan (its §5
H4): ORD-1 states neither, and its guards forbid any transitivity vocabulary in the module (§4, S1).

***

## 1. Landed inputs (the only kernel facts consumed)

| id | statement at `D` | where |
|---|---|---|
| L1 | `structure OpDatum (D) where τ : Prep D → CSpace D; mem_body : ∀ x, τ x ∈ body D` | CA:46–48 |
| L2 | `AffineRespect T := ∀ s c, ∑ c = 0 → ∑ c • prepVec D x = 0 → ∑ c • T.τ x = 0` | CA:58–60 |
| L3 | `CompletionChart D` (`d L p0 Lg hL hLg hspan`); `chartBody C := bodyR C.L C.p0 (body D)`; `gen C x := coordsOf C (prepVec D x)` (so `gen C x = coordsOf C (prepVec D x)` is `rfl`) | CA:144–151, 166, 169 |
| L4 | `coordsOf_mem_chartBody`, `chart_gen`, `affineSpan_gen : affineSpan ℝ (range (gen C)) = ⊤` | CA:184, 181, 218 |
| L5 | `induced C T hT : (Fin C.d → ℝ) →ᵃ[ℝ] _`; `induced_gen : induced C T hT (gen C x) = coordsOf C (T.τ x)`; `induced_unique : (∀ x, Φ (gen C x) = Ψ (gen C x)) → Φ = Ψ` (proof: `AffineMap.ext_on (affineSpan_gen C)`, so that Mathlib name is verified) | CA:277, 281, 254–256 |
| L6 | `after C S T hS : OpDatum D` with `τ x := chart C.L C.p0 (induced C S hS (coordsOf C (T.τ x)))`; `affineRespect_after`; `induced_after : induced C (after C S T hS) _ = (induced C S hS).comp (induced C T hT)` | CA:305–322 |
| L7 | `Undoes C S T hS := ∀ x, (after C S T hS).τ x = prepVec D x`; `comp_eq_id`; `inducedEquiv C hS hT hST hTS`; `inducedEquiv_apply : … w = induced C T hT w` is `rfl`; `preservesBody_inducedEquiv` | CA:325–360 |
| L8 | `prepVec`, `prepVec_mem_body`, `body`, `FiniteRank Ω := FiniteDimensional ℝ (affineSpan ℝ Ω).direction`, `exists_completionChart (hne) (hfr)` | SC:135, 167, 141, 299, CA:154 |
| L9 | `FiniteStage` with instance fields `[fP : Fintype P]` (`attribute [instance]`), `DirectedStages` (`ι`, `stage`, `Prep D := Σ i, (D.stage i).P`) | KF:63–75; SC:63–87 |
| L10 | `ball3`, `rotFun`, `rotFun_zero`, `rotFun_add : rotFun s (rotFun t v) = rotFun (s+t) v`, `rot3 t`, `rot3_apply : rot3 t v = rotFun t v` (`rfl`), `isBoundaryState_ball3 : IsBoundaryState ball3 ![1,0,0]` | KF:311, 351, 359, 366, 411, 413, 1080 |
| L11 | `hh3 d k hk`, `hh3_apply` (`rfl`), `hhFun_hhFun : hhFun d k (hhFun d k v) = v`, `fullAut3`, `hh3_mem_fullAut3`, `preservesBody_flow : PreservesBody ball3 (range rot3)` | OG:499, 503, 451, 521, 530, 574 |
| L12 | `PreservesBody Ω G := ∀ g ∈ G, ∀ x ∈ Ω, g x ∈ Ω ∧ g.symm x ∈ Ω` (consumed only by the optional E9) | OG:69 |
| L13 | `isEmpty_drivability_of_finite_orbits (hfin : ∀ x ∈ Ω, {y \| ∃ g, (∀ z ∈ Ω, g z ∈ Ω ∧ g.symm z ∈ Ω) ∧ g x = y}.Finite) : IsEmpty (ElementaryDrivability Ω)` (cited beside E9, never used) | ON:124–127 |

Not consumed, by design: `BoundaryTransitive` (OG:79), `CoversBoundaryFrom`, `ElementaryDrivability` (KF:264), `SCInf`,
`BinaryVisible`, `SharpSeed`, anything of `InvariantInnerProduct` (not in CA's import closure: CA → SC → ON → OG → KF),
anything of TRB-1, L3B. Import chain check: `OrbitNormalization.lean:36` imports only `OrbitGeneration` from OIBridge.

***

## 2. Definitions — module `OIBridge/CompositionOrder.lean`, namespace `OIBridge.CompositionOrder`

```lean
import OIBridge.CompletionAction
import Mathlib.Data.Real.Pi.Irrational        -- [MV] path; the name `irrational_pi` is used at DenseInstrumentBridge:527
open Set KInfFoundations OrbitGeneration OrbitNormalization StageCompletion CompletionAction

section Order
variable {V : Type*} [AddCommGroup V] [Module ℝ V]        -- no norm, no topology, no field beyond ℝ-module
/-- Infinite order on `Ω`: every positive power moves some state of `Ω`. Iteration is of the underlying function. -/
def InfiniteOrderOn (Ω : Set V) (g : V ≃ᵃ[ℝ] V) : Prop := ∀ m : ℕ, 1 ≤ m → ∃ x ∈ Ω, (⇑g)^[m] x ≠ x
/-- Finite order on `Ω`: some positive power fixes every state of `Ω`. -/
def FiniteOrderOn (Ω : Set V) (g : V ≃ᵃ[ℝ] V) : Prop := ∃ N : ℕ, 1 ≤ N ∧ ∀ x ∈ Ω, (⇑g)^[N] x = x
/-- **ORD∞**: some member of `G` has infinite order on `Ω`. A predicate on a *set*; nothing about closure or transitivity. -/
def OrdInf (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop := ∃ g ∈ G, InfiniteOrderOn Ω g
/-- Composition closure of a set of affine automorphisms. -/
def MulClosed (G : Set (V ≃ᵃ[ℝ] V)) : Prop := ∀ g ∈ G, ∀ h ∈ G, g.trans h ∈ G
/-- `m`-fold composite of an affine self-map, by recursion (no `Monoid` instance of `AffineMap` is used). -/
def affPow (Φ : V →ᵃ[ℝ] V) : ℕ → V →ᵃ[ℝ] V
  | 0 => AffineMap.id ℝ V
  | m + 1 => Φ.comp (affPow Φ m)
end Order

variable {D : DirectedStages}
/-- The identity datum: every preparation to its own preparation vector. -/
def idDatum (D : DirectedStages) : OpDatum D where
  τ := prepVec D
  mem_body := prepVec_mem_body D
/-- **Stage preservation**: each preparation of stage `i` is carried to a preparation vector of the same stage `i`. -/
def StagePreserving (T : OpDatum D) : Prop :=
  ∀ (i : D.ι) (x : (D.stage i).P), ∃ y : (D.stage i).P, T.τ ⟨i, x⟩ = prepVec D ⟨i, y⟩
variable (C : CompletionChart D)
/-- The `m`-fold composite of a datum with itself, through the landed composition law `after`. -/
noncomputable def iterAfter (T : OpDatum D) (hT : AffineRespect T) : ℕ → OpDatum D
  | 0 => idDatum D
  | m + 1 => after C T (iterAfter T hT m) hT      -- `after C S T hS` needs `AffineRespect` of the OUTER datum only (CA:305)
/-- The chart coordinates of the preparations of one stage, as a finset (`Fintype (D.stage i).P` is L9's instance). -/
noncomputable def stageGen (i : D.ι) : Finset (Fin C.d → ℝ) := by
  classical exact Finset.univ.image fun y : (D.stage i).P => gen C ⟨i, y⟩
/-- The Householder reflections of the ball (ORD-1's own set; TRB-1's analogous set is not consumed). -/
def householder3 : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)) := {g | ∃ d k hk, g = hh3 d k hk}
```

`AffineRespect (idDatum D)` is trivially true: unfolding, the hypothesis `∑ c x • prepVec D x = 0` *is* the goal
`∑ c x • (idDatum D).τ x = 0`, so the proof is `fun _ _ _ h => h`. `(⇑g)^[m]` is `Nat.iterate`, written `^[` in 20 landed
modules (e.g. C3Necessity:61), with `Function.iterate_succ_apply'` (Equivalence:278) and `Function.iterate_add_apply`
(OrbitLawRigidityTwisted:339) available. Naming: TRB-1's design also declares `InfiniteOrderOn`/`OrdInf` in
`OIBridge.TransitiveBody`; the two namespaces do not clash, but a later module opening both would. Owner decision §7.1.

***

## 3. Theorem skeleton (signature up to `:=`; route; landed identifiers; cost)

### §B — iteration through the composition law

- **B1** `theorem affineRespect_idDatum : AffineRespect (idDatum D)` — `fun _ _ _ h => h`. **cheap.**
- **B2** `theorem induced_idDatum : induced C (idDatum D) affineRespect_idDatum = AffineMap.id ℝ _` — `induced_unique C`
  with `induced_gen`; the goal `coordsOf C (prepVec D x) = gen C x` is `rfl` (L3). **cheap.**
- **B3** `theorem affineRespect_iterAfter (hT) (m) : AffineRespect (iterAfter C T hT m)` — induction; step is
  `affineRespect_after C hT ih` (L6). **cheap.**
- **B4** `theorem induced_iterAfter (hT) (m) : induced C (iterAfter C T hT m) (affineRespect_iterAfter C hT m) = affPow (induced C T hT) m`
  — induction; base B2; step `induced_after C hT (affineRespect_iterAfter C hT m)` then `rw [ih]`. The `AffineRespect`
  proof term in `induced_after`'s statement differs syntactically from `affineRespect_iterAfter C hT (m+1)`; definitional
  proof irrelevance makes `exact (induced_after …).trans …` typecheck. If `rw` balks, use `show` with the explicit term.
  **cheap/moderate** (term-matching only).
- **B5** `theorem coe_affPow (Φ) (m) : ⇑(affPow Φ m) = (⇑Φ)^[m]` — induction, `Function.iterate_succ'`, `AffineMap.coe_comp`
  [MV, near-certain]. `theorem coe_induced_iterAfter : ⇑(induced C (iterAfter C T hT m) _) = (⇑(induced C T hT))^[m]`. **cheap.**
- **B6** `theorem coe_inducedEquiv (hS hT hST hTS) : ⇑(inducedEquiv C hS hT hST hTS) = ⇑(induced C T hT)` — `funext; rfl`
  (L7 `inducedEquiv_apply` is `rfl`). **cheap.** This is claim (a) of the brief: `induced (iterAfter m) = (induced T)^[m]`.

### §C — an infinite-order datum keeps every power nontrivial (claim (b))

- **C1** `theorem iterate_eq_id_of_fix (hT) (m) (h : ∀ x, (iterAfter C T hT m).τ x = prepVec D x) : (⇑(induced C T hT))^[m] = id`
  — `induced (iterAfter m)` agrees with `AffineMap.id` on every `gen C x` (`induced_gen`, `h`, `rfl` of L3), so equals it
  by `induced_unique` (the step "an affine map of the chart fixing every `gen x` is the identity" = L5, whose proof is
  `AffineMap.ext_on (affineSpan_gen C)`); then B4/B5. **cheap.**
- **C2** `theorem exists_moved_of_infiniteOrderOn (hS hT hST hTS) (h : InfiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS)) :
  ∀ m, 1 ≤ m → AffineRespect (iterAfter C T hT m) ∧ ∃ x, (iterAfter C T hT m).τ x ≠ prepVec D x`
  — first conjunct B3; second by contradiction via C1 and B6 against the moved `w ∈ chartBody C`. **cheap.**

### §D — the composition-closure test proper: stage-preserving + reversible ⇒ finite order (DRIVE F-D3; claim (c))

- **D1** `theorem exists_finset_affineSpan_eq_top {P} [... AddTorsor V P] [FiniteDimensional ℝ V] {s : Set P} (h : affineSpan ℝ s = ⊤) :
  ∃ t : Finset P, ↑t ⊆ s ∧ affineSpan ℝ (↑t : Set P) = ⊤` — the finite-extraction lemma, stated generically (reused by E9).
  Route: `s` nonempty from `h` (`AffineSubspace.nonempty_of_affineSpan_eq_top` [MV]; fallback: if `s = ∅` then
  `affineSpan ℝ ∅ = ⊥` (`AffineSubspace.span_empty` [MV]) and `⊥ ≠ ⊤` for a nonempty `P` (`AffineSubspace.bot_ne_top` [MV])).
  Fix `p ∈ s`; `vectorSpan ℝ s = Submodule.span ℝ ((· -ᵥ p) '' s)` (`vectorSpan_eq_span_vsub_set_right` [MV]) and
  `vectorSpan ℝ s = ⊤` (`AffineSubspace.affineSpan_eq_top_iff_vectorSpan_eq_top_of_nonempty` [MV]). Apply
  `exists_linearIndependent ℝ ((· -ᵥ p) '' s)` — destructuring `⟨b, hb, hspan, hli⟩` verified at OrbitGeometryRigidity:318 —
  and `hli.set_finite_of_isNoetherian` (OrbitReachability:358): `b` is a finite subset of the differences with
  `span ℝ b = ⊤`. Pull back: for each `v ∈ b` choose `q_v ∈ s` with `q_v -ᵥ p = v`; `t := insert p (image q b)` (finite,
  `⊆ s`); `vectorSpan ℝ t ⊇ span ℝ b = ⊤` by `vectorSpan_eq_span_vsub_set_right` again and `Submodule.span_mono`
  (ObservabilityQuotient:275); conclude with the `affineSpan_eq_top_iff_vectorSpan` lemma, `t` nonempty. **moderate**;
  the one Lean-risk node of the round. Fallback if the `vectorSpan` lemma names fail: coefficient route — `Pi.basisFun ℝ (Fin d)`
  (LinkDecomposition:85; note the tag spells `Module.Basis`, OrbitGeometryRigidity:323), each basis vector lies in
  `span ℝ (differences)`, `Submodule.mem_span_finite_of_mem_span` [MV] gives a finite sub-family per vector, union over
  `Fin d`. Either route needs no inner product and no compactness.
- **D2** `theorem nonempty_prep : Nonempty (Prep D)` — from D1's nonemptiness step applied to `affineSpan_gen C`. **cheap** given D1.
- **D3** `theorem exists_gen_finset : ∃ A : Finset (Prep D), affineSpan ℝ ((A.image (gen C) : Finset _) : Set _) = ⊤`
  — D1 on `range (gen C)` with `affineSpan_gen`, then choose preimages. **cheap** given D1.
- **D4** `theorem mapsTo_stageGen (hT) (hsp : StagePreserving T) (i) : ∀ w ∈ stageGen C i, induced C T hT w ∈ stageGen C i`
  — `w = gen C ⟨i,y⟩`; `induced_gen`; `hsp i y = ⟨y', e⟩`; rewrite `T.τ ⟨i,y⟩ = prepVec D ⟨i,y'⟩`; `coordsOf C (prepVec D ⟨i,y'⟩) = gen C ⟨i,y'⟩` (`rfl`). **cheap.**
- **D5** `theorem exists_return {S : Finset α} {f : α → α} (hf : Function.Injective f) (hm : ∀ w ∈ S, f w ∈ S) {w} (hw : w ∈ S) : ∃ p, 0 < p ∧ f^[p] w = w`
  — `Finite.exists_ne_map_eq_of_infinite` on `n ↦ ⟨f^[n] w, _⟩ : ℕ → ↥S` (used at CombRealization:81; the three-case
  template `exists_return` at CombRealization:78–92 is re-derived, not imported); cancel with `Function.iterate_add_apply`
  and `hf.iterate` (`Function.Injective.iterate` [MV]; fallback: induction on `n` with `hf`). **cheap.**
- **D6** `theorem exists_common_period {f : α → α} (A : Finset α) (h : ∀ w ∈ A, ∃ p, 0 < p ∧ f^[p] w = w) : ∃ N, 1 ≤ N ∧ ∀ w ∈ A, f^[N] w = w`
  — `Finset.induction_on`; `N := N₁ * p`, `Function.iterate_mul` [MV] (`f^[m*n] = (f^[m])^[n]`) and `Function.iterate_fixed`
  [MV] (fallback: `Function.IsPeriodicPt.mul_const` / `const_mul` [MV]). **cheap/moderate.**
- **D7 (the F-D3 theorem)** `theorem finiteOrderOn_of_stagePreserving {S T : OpDatum D} (hS : AffineRespect S) (hT : AffineRespect T)
  (hST : Undoes C S T hS) (hTS : Undoes C T S hT) (hsp : StagePreserving T) : FiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS)`
  — `f := ⇑(induced C T hT)`, injective by `comp_eq_id C hS hT hST` (L7; exactly as CA:336 does). D3 gives `A`; for each
  `x ∈ A`, with `x = ⟨i, y⟩`, D4 and D5 on `stageGen C i` give a period of `gen C x`; D6 over `A.image (gen C)` gives `N`;
  `affPow (induced C T hT) N` agrees with `AffineMap.id` on `A.image (gen C)`, so `AffineMap.ext_on (hD3)` gives equality
  of affine maps, hence `f^[N] w = w` for **every** `w` (B5), a fortiori on `chartBody C`; B6 transports to `inducedEquiv`.
  **moderate** (assembly of D1–D6; no new mathematics). Hypothesis list is exactly these six binders plus `C` (guard S3).
- **D8** corollaries, **cheap**: `not_infiniteOrderOn_of_stagePreserving … : ¬ InfiniteOrderOn (chartBody C) (inducedEquiv …)`;
  `not_stagePreserving_of_infiniteOrderOn … (h : InfiniteOrderOn (chartBody C) (inducedEquiv …)) : ¬ StagePreserving T`
  (the design message of DRIVE §3.2: a drive's generator must cross stages).

Why reversibility is load-bearing (not removable): a per-stage constant datum `τ ⟨i,x⟩ := prepVec D ⟨i, y₀ i⟩` is
`StagePreserving` and `AffineRespect` (a constant map is affine) and no positive power of its induced map is the identity
when a stage has two distinct preparation vectors. A kernel instance needs an explicit `CompletionChart` of a concrete
`DirectedStages` (the `L`, `Lg` of an `lp` space by hand) — **hard** for its value; recorded in the result note as a written
countercontrol, and enforced instead by guard S3's literal hypothesis list. Why finite rank is load-bearing: without `C`
there is no chart, and the uniform `N` comes only from the finite spanning set D3; a tower whose stage `n` carries an
`(n+1)`-cycle has every induced-on-stage order but no common one.

### §E — controls (claim (d))

- **E1** `theorem finiteOrderOn_of_not_infiniteOrderOn : ¬ InfiniteOrderOn Ω g → FiniteOrderOn Ω g` and
  `theorem not_infiniteOrderOn_of_finiteOrderOn : FiniteOrderOn Ω g → ¬ InfiniteOrderOn Ω g` — `push_neg` on the
  definitions, two theorems (§A.34); an `iff` may be added citing both. **cheap.**
- **E2** `theorem finiteOrderOn_refl (Ω) : FiniteOrderOn Ω (AffineEquiv.refl ℝ V)` — `N := 1`, `AffineEquiv.refl_apply`. **cheap.**
- **E3** `theorem hh3_hh3 (d k hk) (v) : hh3 d k hk (hh3 d k hk v) = v` (`hh3_apply`, `hhFun_hhFun`, L11);
  `theorem finiteOrderOn_hh3 : FiniteOrderOn ball3 (hh3 d k hk)` — `N := 2`. **cheap.**
- **E4** `theorem not_ordInf_householder3 : ¬ OrdInf ball3 householder3` — every member is an `hh3`, E3, E1. **cheap.**
  ORD-1 does **not** prove that `householder3` is boundary transitive: that is the reflection step of
  `boundaryTransitive_fullAut3` (OG:537) and belongs to the sibling round (its T5(a)); stating it here would put a
  transitivity predicate in this module (guard S1). The result note says so in one sentence.
- **E5** `theorem rot3_one_iterate (m : ℕ) (v) : (⇑(rot3 1))^[m] v = rotFun (m : ℝ) v` — induction; `rot3_apply`,
  `rotFun_add`, `rotFun_zero`, `Nat.cast_succ`, `Function.iterate_succ_apply'`. **cheap.**
- **E6** `theorem infiniteOrderOn_rot3_one : InfiniteOrderOn ball3 (rot3 1)` — witness `![1,0,0] ∈ ball3` (`norm_num`, as
  KF:1081); if `rotFun m ![1,0,0] = ![1,0,0]` then the `0`-coordinate gives `Real.cos m = 1` (`rotFun_apply`), so
  `∃ n : ℤ, n * (2π) = m` (`Real.cos_eq_one_iff` [MV]; fallback via the `1`-coordinate `Real.sin m = 0` and
  `Real.sin_eq_zero_iff` [MV]); `n ≠ 0` since `1 ≤ m`; then `π * (2n) = m` contradicts
  `(irrational_pi.mul_int (by omega)).ne_int m` (`Irrational.mul_int`, `Irrational.ne_int` [MV]; `irrational_pi` verified
  at DenseInstrumentBridge:527; cast normalisation by `push_cast`). **moderate** (two [MV] names, routine real algebra).
- **E7** **cheap**: (a) `ordInf_fullAut3 : OrdInf ball3 fullAut3` with `rot3 1 ∈ fullAut3 := preservesBody_flow _ ⟨1, rfl⟩`
  (`fullAut3` is definitionally the `PreservesBody` set, OG:521–524); (b) `ordInf_flow : OrdInf ball3 (Set.range rot3)`;
  (c) `ordInf_singleton_rot3 : OrdInf ball3 {rot3 1}` — a *finite, not composition-closed* set with ORD∞: the
  countercontrol for E8's closure hypothesis.
- **E8** `theorem not_ordInf_of_finite_of_mulClosed (hG : G.Finite) (hcl : MulClosed G) : ¬ OrdInf Ω G` — for `g ∈ G`
  define `gpow g : ℕ → V ≃ᵃ[ℝ] V` by `gpow 0 := g`, `gpow (n+1) := (gpow n).trans g`; `gpow n ∈ G` by induction with `hcl`;
  `Finite.exists_ne_map_eq_of_infinite (fun n => (⟨gpow g n, _⟩ : ↥G))` with `hG.to_subtype`; equal equivalences have
  equal coercions `(⇑g)^[a+1] = (⇑g)^[b+1]` (`AffineEquiv.trans_apply`, KF:299); cancel `a+1` iterates by injectivity
  (`g.injective`, `Function.iterate_add_apply`) to get `(⇑g)^[b-a] = id`, so `FiniteOrderOn Ω g`; E1. Needs only
  `Finite ↥G`, so `G.Finite` could be weakened to a `[Finite G]` instance; keep `Set.Finite`. **moderate.** Dropping `hcl`
  makes the statement false (E7c), which is the mutation control.
- **E9 (optional)** `theorem finiteOrderOn_of_finite_orbits [NormedAddCommGroup V] [NormedSpace ℝ V] [FiniteDimensional ℝ V]
  {Ω : Set V} (hfin : ∀ x ∈ Ω, {y | ∃ g : V ≃ᵃ[ℝ] V, (∀ z ∈ Ω, g z ∈ Ω ∧ g.symm z ∈ Ω) ∧ g x = y}.Finite)
  (hspan : affineSpan ℝ Ω = ⊤) {g} (hg : ∀ z ∈ Ω, g z ∈ Ω ∧ g.symm z ∈ Ω) : FiniteOrderOn Ω g` — the hypothesis of
  L13 verbatim; D1 on `Ω`, each spanning point's `g`-orbit lies in its finite full-orbit (powers of `g` preserve `Ω`),
  D5/D6, `AffineMap.ext_on`. Pairs the landed "finite orbits ⇒ no drive" (L13) with "finite orbits ⇒ no ORD∞" without
  touching `ElementaryDrivability`. **moderate**; include only if D1 lands cleanly in the design run (it is D1's second consumer).

### §F — the verdict
- `theorem ord1_core : (∀ D C S T hS hT hST hTS, StagePreserving T → FiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS)) ∧
  (∀ D C S T hS hT hST hTS, InfiniteOrderOn (chartBody C) (inducedEquiv …) → ∀ m, 1 ≤ m → ∃ x, (iterAfter C T hT m).τ x ≠ prepVec D x) ∧
  InfiniteOrderOn ball3 (rot3 1) ∧ ¬ OrdInf ball3 householder3 ∧ OrdInf ball3 {rot3 1} ∧
  (∀ Ω G, G.Finite → MulClosed G → ¬ OrdInf Ω G)` — conjunction of D7, C2, E6, E4, E7c, E8. **cheap.**

### Claim (e): the `d = 2` statement — recommendation: **exclude**
The statement would be `MulClosed G ∧ (transitivity on the boundary of a 2-dimensional body) → OrdInf Ω G`. Its proof needs
(i) the invariant inner product (IIP-1, landed) *and* an orthonormalisation of `invMatrix` to read `G` inside `O(2)` — the
same normalisation risk TRB-1 carries as its H1; (ii) uncountability of the boundary-state set of a planar body with interior;
(iii) countability of torsion in `SO(2) ≅ ℝ/ℤ` and the coset argument `G ∩ SO(2)` uncountable (this is where closure is
used); (iv) a nontrivial rotation about the centroid moving a point of `Ω`. Each piece is elementary; together they are
several hundred lines, none reusable by D7/E8, and the theorem itself is the one shape guard S1 exists to exclude from
this module (a transitivity hypothesis with an `OrdInf` conclusion). **Hard** for the round's size, and it would be
typed with `d = 2` while inviting the reading that general `d` is settled. If the owner wants it, it is a follow-up round
after TRB-1 lands (its `exists_affine_image_eq_eball` at `d = 2` collapses (i)–(ii) to the disk), with a header stating
that the general-`d` implication is open (Jordan–Schur/Cartan).

***

## 4. Dependency map and non-claims

```
L1–L2 OpDatum, AffineRespect ─┐
L8 idDatum data               ├─▶ B1–B3 iterAfter is AffineRespect ─▶ B4–B6 induced(iterAfter m) = (induced T)^[m]
L6 after, induced_after ──────┘                                            │
L5 induced_gen, induced_unique ──────────────────────────────▶ C1 ─▶ C2 (infinite order ⇒ every power nontrivial)
L4 affineSpan_gen ─▶ D1 finite spanning subset [Mathlib: exists_linearIndependent, set_finite_of_isNoetherian, vectorSpan] ─▶ D2, D3
L9 Fintype P ─▶ stageGen ─▶ D4 (StagePreserving) ─┐
L7 comp_eq_id (injectivity) ─▶ D5 ─▶ D6 ──────────┴─▶ D7 F-D3 ─▶ D8
L10 rot3, rotFun_add ─▶ E5 ─▶ E6 [Mathlib: cos_eq_one_iff, irrational_pi] ─▶ E7 (fullAut3 via L11 preservesBody_flow; range rot3; {rot3 1})
L11 hh3, hhFun_hhFun ─▶ E3 ─▶ E4 ;  E1, E2 premise-free ;  E8 premise-free (Finite.exists_ne_map_eq_of_infinite) ; E9 ← D1, L12
```
No node depends on: TRB-1, `BoundaryTransitive`/`CoversBoundaryFrom`, a ball theorem, `ElementaryDrivability` or any flow
law (`rot3` enters as single elements and as the set `range rot3`, never through `flow_add`/continuity), `Continuous`,
`IsCompact`, `invMatrix`/IIP-1, `SCInf`, `BinaryVisible`, `SharpSeed`, naturality, L3B.

**ORD-1 does not claim:** TRANS ⇒ ORD∞ in any dimension (not even `d = 2`); ORD∞ ⇒ TRANS; any ball, ellipsoid, dimension or
`d = 3` statement; a drive, a flow or its closure; that any OI construction supplies a reversible datum, `FiniteRank`, a
`CompletionChart` or `StagePreserving`'s negation; that finite order on `chartBody C` says anything about an infinite-rank
body; that `not_ordInf_householder3` is a statement about transitivity. `FiniteRank (body D)` remains the open premise,
entering only through `C` (TRB-1 design §5 H6, same status here).

***

## 5. Semantic guards for `controls.py` (IIP-1 style; each with a mutation control that must fail with its code)

- **N1–N3** as IIP-1: declaration list and kinds in order; every statement up to `:=`, every definition whole, every
  context line frozen; no `sorry`/`admit`/`axiom`/`native_decide`; every frozen `#print axioms` line present. Mutations:
  removed declaration; changed binder; a `sorry`.
- **S1 separation.** The module text contains none of the tokens `BoundaryTransitive`, `CoversBoundaryFrom`, `Trans `,
  `IsBodyGroup`, `TransitiveBody`, `transitive`, `ElementaryDrivability`, `flow`, `Continuous`, `IsCompact`, `invMatrix`,
  `SCInf`, `BinaryVisible`, `SharpSeed`, `centroid`; no `import OIBridge.TransitiveBody` or `InvariantInnerProduct`. Header
  carries "No transitivity, ball, dimension, drive or flow is claimed; TRANS ⇒ ORD∞ is not stated." Mutation: a theorem
  with `BoundaryTransitive` among hypotheses and `OrdInf` in its conclusion; a second mutation: the import line.
- **S2 dimension.** Outside the `§E controls` section (delimited by frozen section-comment lines), no statement mentions
  `3`, `Fin 3`, `ball3`, `rot3`, `hh3`, `fullAut3`, `finrank`, or a hypothesis of the form `C.d = `. Mutation: `3` in D7's
  conclusion.
- **S3 F-D3 hypotheses exactly.** `finiteOrderOn_of_stagePreserving`'s binders are exactly `(C : CompletionChart D)`,
  `{S T : OpDatum D}`, `(hS : AffineRespect S)`, `(hT : AffineRespect T)`, `(hST : Undoes C S T hS)`, `(hTS : Undoes C T S hT)`,
  `(hsp : StagePreserving T)`, and its conclusion is `FiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS)`. Mutations:
  `hST`/`hTS` dropped (the constant-datum countermodel makes it false); `hsp` dropped (E7 makes it false in spirit);
  `SCInf D` added.
- **S4 definitions are what they say.** `InfiniteOrderOn` matches `∀ m : ℕ, 1 ≤ m → ∃ x ∈ Ω, (⇑g)^[m] x ≠ x`; `OrdInf` is
  `∃ g ∈ G, …` (never `∀ g`); `StagePreserving` binds the same `i` on both sides (`⟨i, x⟩` … `prepVec D ⟨i, y⟩`); `idDatum`'s
  `τ` is `prepVec D`; `iterAfter`'s step is `after C T (iterAfter T hT m) hT`. Mutations: `∀ g ∈ G`; `⟨j, y⟩`.
- **S5 closure control.** `not_ordInf_of_finite_of_mulClosed` has both `G.Finite` and `MulClosed G`; `ordInf_singleton_rot3`
  is present with an axiom print. Mutation: `MulClosed G` dropped.
- **S6 controls present.** E1–E8 (and E9 if frozen) are kernel theorems with `#print axioms`, each within
  `[propext, Classical.choice, Quot.sound]`. Mutation: `infiniteOrderOn_rot3_one` removed.
- **S7 one direction per theorem.** E1 is two theorems; any `↔` cites both names. Mutation: one direction removed.
- **I** `OIBridge.lean` is `D`'s with `import OIBridge.CompositionOrder` directly after `import OIBridge.CompletionAction`
  (OIBridge.lean:251). **C** census is `D`'s with one `kernel-only` family inserted directly after the OPACT-1 family.
  TRB-1's design uses the same two anchors; whichever lands second reconciles by merits (§A.39 3), and this is recorded
  in the preregistration so the collision is expected, not an anomaly. **F** as IIP-1.

***

## 6. Anti-circularity and separation audit

- **TRB-1:** not imported, not cited; all predicates are ORD-1's own (`InfiniteOrderOn`, `FiniteOrderOn`, `OrdInf`,
  `MulClosed`, `StagePreserving`, `householder3`). Overlap of *content* with TRB-1's T5(b)(c)/T6 exists by the owner's
  split; the ORD∞ cells (`infiniteOrderOn_rot3_one`, `ordInf_fullAut3`, `ordInf_flow`, `not_ordInf_*`) are ORD-1's charter,
  and TRB-1 can cite them after both land (§7.1).
- **Ball / field / IIP:** none; the module's import closure is CA → SC → ON → OG → KF and never `InvariantInnerProduct`.
- **Flow / continuity:** `rot3` is used as single affine equivalences and `range rot3` as a bare set; `rotFun_add` is a
  trig identity, not a flow axiom; nothing topological is assumed on `G` or `Ω`.
- **Hidden dependences found:** (1) `FiniteRank` enters through `C` and is load-bearing for D7 (the uniform `N` needs the
  finite spanning set); state it as the open premise, not a hypothesis to source. (2) Reversibility (`hST`, `hTS`) is
  load-bearing: only injectivity is used, so a weaker `induced_injective` form exists, but the constant-datum countermodel
  shows it cannot be dropped. (3) `StagePreserving` needs no SC∞, no naturality, no `BinaryVisible`. (4) `Nonempty (Prep D)`
  is derivable from `C` (D2), so no extra hypothesis. (5) `Fintype (D.stage i).P` is L9's instance attribute; `Finset.image`
  needs `DecidableEq (Fin C.d → ℝ)`, taken classically inside `stageGen`. (6) B4 relies on definitional proof irrelevance
  for `AffineRespect` terms. (7) `OrdInf Ω G` says nothing about `G` preserving `Ω`; controls pair it with landed
  `PreservesBody` facts only where the pairing is meaningful (E7a via `fullAut3`'s definition).
- **Nothing in ORD-1 derives or refutes `Trans → OrdInf`;** S1 makes that mechanical.

***

## 7. Freeze boundary, stages, outcomes, design-run checklist

**Frozen at `F`:** the preregistration; `controls.py` embedding the statement surface of `OIBridge/CompositionOrder.lean`
(preamble, every context line, every definition whole, every theorem signature up to `:=`, the `#print axioms` lines);
the import insertion; the census family; the outcome vocabulary. **Not frozen:** proofs (design-run rule of IIP-1: a repair
changes proofs only). **Decided before `F`:** whether E9 and the E1 `iff` corollary are in the surface (yes only if the
design run builds them); claim (e) is not in the surface under any outcome.

**Stages:** C1 `controls.py`; S1 module + import + census (acceptance: `controls.py check S1 --freeze F` passes; exact-head run
green with every printed axiom set within `[propext, Classical.choice, Quot.sound]`); proof-only repairs; S2 result note =
candidate `E`. **Governed paths:** record `verification/programmes/oi-qm/reconstruction/round-ord-1-composition-order/`,
receipt `verification/receipts/ORD-1.json`; execution `A …/OIBridge/CompositionOrder.lean`, `M …/OIBridge.lean`,
`M verification/lean-manuscript-census.json`. No manuscript.

**Outcomes:** `ORD-1-COMPOSITION-ORDER-PROVED` (every frozen theorem built, `controls: OK`, exact-head green at `E`);
`ORD-1-HALTED` (anything else; the result note names the failing check). Neither outcome claims TRANS ⇒ ORD∞, a ball, a
dimension, a drive, or OI sourcing of any datum, `FiniteRank` or `StagePreserving`.

**Design-run checklist (Mathlib names to verify on a disposable branch, read for compilation only):**
`AffineSubspace.nonempty_of_affineSpan_eq_top`, `AffineSubspace.span_empty`, `AffineSubspace.bot_ne_top`,
`vectorSpan_eq_span_vsub_set_right`, `AffineSubspace.affineSpan_eq_top_iff_vectorSpan_eq_top_of_nonempty`,
`Submodule.mem_span_finite_of_mem_span` (fallback), `Function.Injective.iterate`, `Function.iterate_mul`,
`Function.iterate_fixed`, `Function.IsPeriodicPt.mul_const` (fallback), `AffineMap.coe_comp`, `Real.cos_eq_one_iff`,
`Real.sin_eq_zero_iff` (fallback), `Irrational.mul_int`, `Irrational.ne_int`, the import path of `irrational_pi`.
Verified at `D` by landed use: `exists_linearIndependent` (OrbitGeometryRigidity:318), `LinearIndependent.set_finite_of_isNoetherian`
(OrbitReachability:358), `Finite.exists_ne_map_eq_of_infinite` (CombRealization:81), `AffineMap.ext_on` (CA:256),
`Function.iterate_succ_apply'` (Equivalence:278), `Function.iterate_add_apply` (OrbitLawRigidityTwisted:339),
`Finite.injective_iff_bijective` (CanonicalMeasure:64), `irrational_pi` (DenseInstrumentBridge:527), `Submodule.span_mono`
(ObservabilityQuotient:275), `AffineEquiv.trans_apply` (KF:299).

### 7.1 Decisions for the owner
1. Canonical home of `InfiniteOrderOn`/`OrdInf`: ORD-1 (recommended, by charter), with TRB-1 citing after landing, or
   duplicated in both namespaces with a documented equivalence.
2. E9 (finite orbits ⇒ finite order, L13's hypothesis verbatim): in the surface if D1 builds in the design run.
3. Claim (e), `d = 2`: exclude from ORD-1 (recommended, §3 E); if wanted, a follow-up after TRB-1.
4. Whether `householder3` is also frozen as the *transitive* set in TRB-1 (its T5(a)) so the 2 × 2 table has one row from
   each round, or TRB-1 extracts its own reflection set; ORD-1 proves only the ORD∞ cell either way.
