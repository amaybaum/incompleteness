import OIBridge.SwapLayer

/-!
# The two-piece drive and the order it must run in

`SecondOrderLayer` and `SwapLayer` each supply a strongly continuous one-parameter group of
`*`-automorphisms of the quasilocal algebra: the shear layer `layerQ R t` and the swap layer
`swapQ V t`. The update is the composite of the two layers, so a continuous-time drive for it is a
composite of the two flows. This file settles **which order** the composite runs in, and packages
the composite as a path.

## The order is forced, not chosen

`SecondOrderCircuit` factors the phase-space map as `leap F = swapLayer ∘ shear F`: on
configurations the shear runs first and the swap second. The Heisenberg action reverses that.
`permOp` is a *covariant* homomorphism — `Finsupp.mapDomain` of a composite is the composite of the
`mapDomain`s in the same order — while `heis Φ T = permOpInv Φ * T * permOp Φ` sandwiches `T`
between the two. Multiplying out gives `heis_of_comp`:

  `Φ.φ = S.φ.trans W.φ`  implies  `heis Φ T = heis S (heis W T)`,

so the **swap** Heisenberg map is applied **first** and the shear's second — the opposite of the
configuration-space order. `driveQ` is defined in that order.

Each layer separately is insensitive to this, because each layer's gate is an involution and
`permMat` of an involution is its own inverse; only the composite, which is not an involution,
distinguishes the two orders. That is exactly why the point is worth a theorem rather than a
convention.

## What is claimed here, and what is not

Claimed: for each `t`, `driveQ R t` is an isometric `*`-automorphism of the quasilocal algebra;
`driveQ R 0` is the identity; and `t ↦ driveQ R t A` is norm-continuous for every quasilocal `A`.
So the map at `t = 1` is joined to the identity by a norm-continuous path of automorphisms.

**Not claimed: a group law.** `driveQ R (t + s) = driveQ R t ∘ driveQ R s` does not follow from the
two layers' group laws, because the two layers do not commute; nothing here establishes it and
nothing here should be read as doing so. A continuous path of automorphisms through the identity is
a strictly weaker object than a one-parameter group, and it is the weaker object that is proved.

Likewise, no generator is exhibited: see the note in `SecondOrderLayer` on why `Σ_i h_i` is a
formal sum defining a densely-defined derivation rather than an element of the algebra.

## The endpoints

A layer flow's time-one map is the frozen Heisenberg action of that layer's own dynamics, when it
can be shown so. The tool is `localDyn`: a dynamics supported in one finite region has
`permOp` equal to that region's embedded permutation matrix, so its Heisenberg action is
conjugation by an element of one stage. Together with `heis_eq_of_agree` — two dynamics with the
same restricted configuration and the same off-region agreement relation act the same on that
region's observables — this replaces an all-sites layer, on any one local observable, by a
region-supported dynamics.

That programme is carried out for the swap layer: `swapQ_one_eq_heisQ` identifies `swapQ V 1` with
`heisQ (swapDyn V)`. For **the shear layer** the endpoint is **not identified** here, and no
theorem asserts it. The obstruction is not the method but its input: the region-supported
replacement for the shear must shear at every site of `affected R Λ`, not only of `Λ`, and be read
on a region closed enough to carry it. Nothing below claims `layerQ R 1 = heisQ (shearDyn R)` or
the corresponding statement for `driveQ R 1`.
-/

namespace OIBridge.SecondOrderDrive

open OIBridge.QuasilocalAlgebra OIBridge.RegionTower OIBridge.SecondOrderCircuit
open OIBridge.QuasilocalCharacterization OIBridge.SecondOrderLayer OIBridge.SwapLayer

variable {ι : Type} [DecidableEq ι] {Q : Type} [Fintype Q] [DecidableEq Q] [Nonempty Q]

/-! ### Section A — the Heisenberg action reverses the order of a composite -/

section Order

variable {X S W : ReversibleDynamics ι Q}

/-- **THE PERMUTATION OPERATOR IS COVARIANT.** If the dynamics `X` runs `S` and then `W` on
configurations, its permutation operator is the product in that same order. -/
theorem permOp_of_comp (h : X.φ = S.φ.trans W.φ) : permOp X = permOp W * permOp S := by
  apply Finsupp.lhom_ext
  intro s c
  rw [Module.End.mul_apply, permOp_single, permOp_single, permOp_single, h]
  rfl

/-- **THE INVERSE PERMUTATION OPERATOR IS CONTRAVARIANT**, the inverse of a composite being the
composite of the inverses in the reverse order. -/
theorem permOpInv_of_comp (h : X.φ = S.φ.trans W.φ) : permOpInv X = permOpInv S * permOpInv W := by
  apply Finsupp.lhom_ext
  intro s c
  rw [Module.End.mul_apply, permOpInv_single, permOpInv_single, permOpInv_single, h]
  rfl

/-- **THE ORDER THEOREM.** If the dynamics runs `S` first and `W` second on configurations, then
its Heisenberg action runs `W`'s Heisenberg action first and `S`'s second. The two sandwiching
factors are covariant and contravariant respectively, and the reversal is what survives when they
are multiplied out. -/
theorem heis_of_comp (h : X.φ = S.φ.trans W.φ) (T : Module.End ℂ (Scaffold ι Q)) :
    heis X T = heis S (heis W T) := by
  rw [heis, heis, heis, permOp_of_comp h, permOpInv_of_comp h]
  simp only [mul_assoc]

/-- The order theorem on the local algebra. -/
theorem heisLoc_of_comp (h : X.φ = S.φ.trans W.φ) (a : localAlg ι Q) :
    heisLoc X a = heisLoc S (heisLoc W a) :=
  Subtype.ext (heis_of_comp h a.1)

/-- **THE ORDER THEOREM ON THE QUASILOCAL ALGEBRA.** This is the statement a two-piece drive has to
match: the drive's outermost flow is the one whose configuration map runs *last*. -/
theorem heisQ_of_comp (h : X.φ = S.φ.trans W.φ) (x : Quasilocal ι Q) :
    heisQ X x = heisQ S (heisQ W x) := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq (continuous_heisQ X) ((continuous_heisQ S).comp (continuous_heisQ W))
  · rw [heisQ_coe, heisQ_coe, heisQ_coe, heisLoc_of_comp h]

end Order

/-! ### Section B — the drive -/

section Drive

variable {V : Type} [Fintype V] [DecidableEq V] [Nonempty V] [AddCommGroup V]
variable (R : Rule ι V)

/-- **THE TWO-PIECE DRIVE.** The swap flow runs first and the shear flow second, which is the order
`heisQ_of_comp` forces for a configuration map that shears first and swaps second. -/
noncomputable def driveQ (t : ℝ) (x : Quasilocal ι (V × V)) : Quasilocal ι (V × V) :=
  layerQ R t (swapQ V t x)

theorem driveQ_apply (t : ℝ) (x : Quasilocal ι (V × V)) :
    driveQ R t x = layerQ R t (swapQ V t x) := rfl

/-- **THE PATH STARTS AT THE IDENTITY.** -/
theorem driveQ_zero_time (x : Quasilocal ι (V × V)) : driveQ R 0 x = x := by
  rw [driveQ, swapQ_zero_time, layerQ_zero_time]

theorem driveQ_mul (t : ℝ) (x y : Quasilocal ι (V × V)) :
    driveQ R t (x * y) = driveQ R t x * driveQ R t y := by
  rw [driveQ, swapQ_mul, layerQ_mul, driveQ, driveQ]

theorem driveQ_add (t : ℝ) (x y : Quasilocal ι (V × V)) :
    driveQ R t (x + y) = driveQ R t x + driveQ R t y := by
  rw [driveQ, swapQ_add, layerQ_add, driveQ, driveQ]

theorem driveQ_smul (t : ℝ) (c : ℂ) (x : Quasilocal ι (V × V)) :
    driveQ R t (c • x) = c • driveQ R t x := by
  rw [driveQ, swapQ_smul, layerQ_smul, driveQ]

theorem driveQ_star (t : ℝ) (x : Quasilocal ι (V × V)) :
    driveQ R t (star x) = star (driveQ R t x) := by
  rw [driveQ, swapQ_star, layerQ_star, driveQ]

theorem driveQ_sub (t : ℝ) (x y : Quasilocal ι (V × V)) :
    driveQ R t (x - y) = driveQ R t x - driveQ R t y := by
  rw [driveQ, swapQ_sub, layerQ_sub, driveQ, driveQ]

theorem driveQ_one (t : ℝ) : driveQ R t (1 : Quasilocal ι (V × V)) = 1 := by
  rw [driveQ, swapQ_one, layerQ_one]

/-- **THE DRIVE IS ISOMETRIC**, being a composite of two isometries. -/
theorem norm_driveQ (t : ℝ) (x : Quasilocal ι (V × V)) : ‖driveQ R t x‖ = ‖x‖ := by
  rw [driveQ, norm_layerQ, norm_swapQ]

theorem dist_driveQ (t : ℝ) (x y : Quasilocal ι (V × V)) :
    dist (driveQ R t x) (driveQ R t y) = dist x y := by
  rw [dist_eq_norm, dist_eq_norm, ← driveQ_sub, norm_driveQ]

theorem continuous_driveQ (t : ℝ) : Continuous (driveQ R t) :=
  (continuous_layerQ R t).comp (continuous_swapQ V t)

/-- **EVERY DRIVE MAP IS INVERTIBLE.** The inverse undoes the two pieces in the reverse order:
shear back first, then swap back. -/
theorem driveQ_left_inverse (t : ℝ) (x : Quasilocal ι (V × V)) :
    swapQ V (-t) (layerQ R (-t) (driveQ R t x)) = x := by
  rw [driveQ, layerQ_left_inverse, swapQ_left_inverse]

theorem driveQ_right_inverse (t : ℝ) (x : Quasilocal ι (V × V)) :
    driveQ R t (swapQ V (-t) (layerQ R (-t) x)) = x := by
  rw [driveQ, swapQ_right_inverse, layerQ_right_inverse]

/-- **EACH MAP OF THE PATH IS A `*`-AUTOMORPHISM.** -/
theorem driveQ_bijective (t : ℝ) :
    Function.Bijective (driveQ R t : Quasilocal ι (V × V) → Quasilocal ι (V × V)) :=
  Function.bijective_iff_has_inverse.mpr
    ⟨fun x => swapQ V (-t) (layerQ R (-t) x), driveQ_left_inverse R t, driveQ_right_inverse R t⟩

/-- **THE PATH IS NORM-CONTINUOUS IN TIME.** Neither factor's strong continuity gives this on its
own: the time parameter moves in both slots at once. What closes the gap is that the outer flow is
isometric *uniformly in its own time parameter*, so the inner motion can be estimated at a frozen
outer time and the outer motion at a frozen inner argument. -/
theorem continuous_driveQ_time (x : Quasilocal ι (V × V)) :
    Continuous fun t : ℝ => driveQ R t x := by
  refine continuous_iff_continuousAt.mpr fun t₀ => Metric.continuousAt_iff.mpr fun ε hε => ?_
  obtain ⟨δ₁, hδ₁, h₁⟩ :=
    Metric.continuousAt_iff.mp ((continuous_swapQ_time V x).continuousAt (x := t₀))
      (ε / 2) (by positivity)
  obtain ⟨δ₂, hδ₂, h₂⟩ :=
    Metric.continuousAt_iff.mp
      ((continuous_layerQ_time R (swapQ V t₀ x)).continuousAt (x := t₀)) (ε / 2) (by positivity)
  refine ⟨min δ₁ δ₂, lt_min hδ₁ hδ₂, fun {t} ht => ?_⟩
  have hta : dist t t₀ < δ₁ := lt_of_lt_of_le ht (min_le_left _ _)
  have htb : dist t t₀ < δ₂ := lt_of_lt_of_le ht (min_le_right _ _)
  have e1 : dist (layerQ R t (swapQ V t x)) (layerQ R t (swapQ V t₀ x)) < ε / 2 := by
    rw [dist_layerQ]
    exact h₁ hta
  have e2 : dist (layerQ R t (swapQ V t₀ x)) (layerQ R t₀ (swapQ V t₀ x)) < ε / 2 := h₂ htb
  calc dist (driveQ R t x) (driveQ R t₀ x)
      ≤ dist (layerQ R t (swapQ V t x)) (layerQ R t (swapQ V t₀ x))
          + dist (layerQ R t (swapQ V t₀ x)) (layerQ R t₀ (swapQ V t₀ x)) := dist_triangle _ _ _
    _ < ε / 2 + ε / 2 := add_lt_add e1 e2
    _ = ε := add_halves ε

/-- **THE UPDATE IS JOINED TO THE IDENTITY BY A CONTINUOUS PATH OF `*`-AUTOMORPHISMS.** The three
clauses are the whole claim: the path starts at the identity, every point of it is an isometric
`*`-automorphism of the quasilocal algebra, and it is norm-continuous in the parameter. No group
law and no generator are asserted. -/
theorem driveQ_isContinuousPath :
    driveQ R 0 = (id : Quasilocal ι (V × V) → Quasilocal ι (V × V)) ∧
      (∀ t : ℝ, Function.Bijective (driveQ R t : Quasilocal ι (V × V) → Quasilocal ι (V × V)) ∧
        (∀ x y, driveQ R t (x * y) = driveQ R t x * driveQ R t y) ∧
        (∀ x y, driveQ R t (x + y) = driveQ R t x + driveQ R t y) ∧
        (∀ x, driveQ R t (star x) = star (driveQ R t x)) ∧
        (∀ x, ‖driveQ R t x‖ = ‖x‖)) ∧
      (∀ x : Quasilocal ι (V × V), Continuous fun t : ℝ => driveQ R t x) :=
  ⟨funext (driveQ_zero_time R),
    fun t => ⟨driveQ_bijective R t, driveQ_mul R t, driveQ_add R t, driveQ_star R t,
      norm_driveQ R t⟩,
    continuous_driveQ_time R⟩

end Drive

/-! ### Section C — the update as a finite-range reversible dynamics -/

section Dynamics

variable {V : Type} [Fintype V] [DecidableEq V] [Nonempty V] [AddCommGroup V]

/-- **THE SWAP LAYER'S COUPLING DATA.** A swap gate occupies one site, so both cones are
singletons. -/
def swapFiniteRange (V : Type) [Fintype V] [DecidableEq V] [Nonempty V] [AddCommGroup V] :
    FiniteRange (swapLayer : (ι → V × V) → (ι → V × V)) where
  nbhd i := {i}
  local_dep i := by
    intro s s' h
    have hi : s i = s' i := h i (Finset.mem_singleton_self i)
    show swapLayer s i = swapLayer s' i
    rw [swapLayer_apply, swapLayer_apply, hi]
  infl i := {i}
  mem_infl i j hij := by
    rw [Finset.mem_singleton] at hij
    subst hij
    exact Finset.mem_singleton_self _

/-- **THE SWAP LAYER AS A REVERSIBLE DYNAMICS.** It is its own inverse, so both range proofs are
the same one. -/
def swapDyn (V : Type) [Fintype V] [DecidableEq V] [Nonempty V] [AddCommGroup V] :
    ReversibleDynamics ι (V × V) where
  φ := swapEquiv
  G := swapFiniteRange V
  G' := swapFiniteRange V

variable (R : Rule ι V)

/-- The influence set of the shear and of the whole update: a site influences itself and whatever
the rule says it influences. -/
def stepInfl (i : ι) : Finset ι := insert i (R.infl i)

omit [Fintype V] [DecidableEq V] [Nonempty V] [AddCommGroup V] in
theorem mem_stepInfl_of_mem_gateRegion {i j : ι} (h : i ∈ gateRegion R j) : j ∈ stepInfl R i := by
  rcases Finset.mem_insert.mp h with h | h
  · subst h
    exact Finset.mem_insert_self _ _
  · exact Finset.mem_insert_of_mem (R.mem_infl j i h)

/-- **THE SHEAR LAYER'S COUPLING DATA.** A shear at site `i` reads the current slice on `N i` and
the previous slice at `i`, so its neighbourhood is the gate region. -/
def shearFiniteRange : FiniteRange (shear R.F : (ι → V × V) → (ι → V × V)) where
  nbhd := gateRegion R
  local_dep i := by
    intro s s' h
    have hi : s i = s' i := h i (Finset.mem_insert_self i (R.N i))
    have hF : R.F (curOf s) i = R.F (curOf s') i :=
      R.dep i _ _ fun j hj => by
        rw [curOf_apply, curOf_apply, h j (Finset.mem_insert_of_mem hj)]
    show shear R.F s i = shear R.F s' i
    rw [shear_apply, shear_apply, hF, hi]
  infl := stepInfl R
  mem_infl _ _ h := mem_stepInfl_of_mem_gateRegion R h

/-- **THE SHEAR LAYER AS A REVERSIBLE DYNAMICS.** -/
def shearDyn : ReversibleDynamics ι (V × V) where
  φ := shearEquiv R.F
  G := shearFiniteRange R
  G' := shearFiniteRange R

/-- **THE UPDATE'S COUPLING DATA.** The one-step map reads the same sites as the shear: the swap
that follows it is on-site. -/
def leapFiniteRange : FiniteRange (leap R.F : (ι → V × V) → (ι → V × V)) where
  nbhd := gateRegion R
  local_dep i := by
    intro s s' h
    have hi : s i = s' i := h i (Finset.mem_insert_self i (R.N i))
    have hF : R.F (curOf s) i = R.F (curOf s') i :=
      R.dep i _ _ fun j hj => by
        rw [curOf_apply, curOf_apply, h j (Finset.mem_insert_of_mem hj)]
    show leap R.F s i = leap R.F s' i
    rw [leap_apply, leap_apply, hF, hi]
  infl := stepInfl R
  mem_infl _ _ h := mem_stepInfl_of_mem_gateRegion R h

/-- **THE INVERSE STEP'S COUPLING DATA.** The inverse runs the two layers in the other order, so it
reads the *previous* slice on `N i` — the same sites, a different component. -/
def leapSymmFiniteRange :
    FiniteRange (fun x : ι → V × V => shear R.F (swapLayer x)) where
  nbhd := gateRegion R
  local_dep i := by
    intro s s' h
    have hi : s i = s' i := h i (Finset.mem_insert_self i (R.N i))
    have hF : R.F (curOf (swapLayer s)) i = R.F (curOf (swapLayer s')) i :=
      R.dep i _ _ fun j hj => by
        rw [curOf_apply, curOf_apply, swapLayer_apply, swapLayer_apply,
          h j (Finset.mem_insert_of_mem hj)]
    show shear R.F (swapLayer s) i = shear R.F (swapLayer s') i
    rw [shear_apply, shear_apply, hF, swapLayer_apply, swapLayer_apply, hi]
  infl := stepInfl R
  mem_infl _ _ h := mem_stepInfl_of_mem_gateRegion R h

/-- **THE UPDATE AS A FINITE-RANGE REVERSIBLE DYNAMICS.** Reversibility is not assumed: it comes
from the depth-two factorization, which exhibits the inverse as the two layers in the other
order. -/
def ruleDynamics : ReversibleDynamics ι (V × V) where
  φ := leapEquiv R.F
  G := leapFiniteRange R
  G' := leapSymmFiniteRange R

/-- **THE DYNAMICS FACTORS**, on the nose, as the shear followed by the swap. -/
theorem ruleDynamics_comp :
    (ruleDynamics R).φ = (shearDyn R).φ.trans (swapDyn V).φ := rfl

/-- **THE UPDATE'S HEISENBERG ACTION RUNS THE SWAP FIRST.** The order theorem of Section A applied
to the update's own factorization: this is the shape any two-piece drive for `heisQ` has to have,
and it is the shape `driveQ` has. -/
theorem heisQ_ruleDynamics (x : Quasilocal ι (V × V)) :
    heisQ (ruleDynamics R) x = heisQ (shearDyn R) (heisQ (swapDyn V) x) :=
  heisQ_of_comp (ruleDynamics_comp R) x

end Dynamics

/-! ### Section D — a dynamics supported in one finite region, and stabilization -/

section Localized

variable (Λ : Finset ι) (σ : Conf Λ Q ≃ Conf Λ Q)

/-- The configuration map of a dynamics that acts inside one finite region and reads nothing
outside it. -/
def localConf (s : ι → Q) : ι → Q := patch Λ s (σ (glob Λ s))

variable {Λ σ}

theorem localConf_apply_of_mem {i : ι} (hi : i ∈ Λ) (s : ι → Q) :
    localConf Λ σ s i = σ (glob Λ s) ⟨i, hi⟩ := patch_apply_of_mem hi

theorem localConf_apply_of_not_mem {i : ι} (hi : i ∉ Λ) (s : ι → Q) :
    localConf Λ σ s i = s i := patch_apply_of_not_mem hi

/-- **THE REGION SEES EXACTLY THE PERMUTATION.** -/
theorem glob_localConf (s : ι → Q) : glob Λ (localConf Λ σ s) = σ (glob Λ s) :=
  glob_patch _ _ _

theorem patch_patch (s : ι → Q) (f g : Conf Λ Q) :
    patch Λ (patch Λ s f) g = patch Λ s g := by
  funext i
  by_cases hi : i ∈ Λ
  · rw [patch_apply_of_mem hi, patch_apply_of_mem hi]
  · rw [patch_apply_of_not_mem hi, patch_apply_of_not_mem hi, patch_apply_of_not_mem hi]

theorem localConf_localConf (s : ι → Q) : localConf Λ σ.symm (localConf Λ σ s) = s := by
  rw [localConf, localConf, glob_patch, Equiv.symm_apply_apply, patch_patch, patch_glob]

variable (Λ σ)

/-- The region-supported map as an equivalence of global configurations. -/
def localEquiv : (ι → Q) ≃ (ι → Q) where
  toFun := localConf Λ σ
  invFun := localConf Λ σ.symm
  left_inv _ := localConf_localConf _
  right_inv s := by
    have h := localConf_localConf (Λ := Λ) (σ := σ.symm) s
    rwa [Equiv.symm_symm] at h

/-- **A REGION-SUPPORTED MAP HAS FINITE RANGE**, both cones being the region itself at the sites
it touches and singletons elsewhere. -/
def localFiniteRange : FiniteRange (localConf Λ σ) where
  nbhd i := if i ∈ Λ then Λ else {i}
  local_dep i := by
    intro s s' h
    show localConf Λ σ s i = localConf Λ σ s' i
    by_cases hi : i ∈ Λ
    · rw [if_pos hi] at h
      have hg : glob Λ s = glob Λ s' := funext fun u => h u.1 u.2
      rw [localConf_apply_of_mem hi, localConf_apply_of_mem hi, hg]
    · rw [if_neg hi] at h
      rw [localConf_apply_of_not_mem hi, localConf_apply_of_not_mem hi,
        h i (Finset.mem_singleton_self i)]
  infl i := if i ∈ Λ then Λ else {i}
  mem_infl i j hij := by
    by_cases hj : j ∈ Λ
    · rw [if_pos hj] at hij
      rw [if_pos hij]
      exact hj
    · rw [if_neg hj, Finset.mem_singleton] at hij
      subst hij
      rw [if_neg hj]
      exact Finset.mem_singleton_self _

/-- **A DYNAMICS SUPPORTED IN ONE FINITE REGION.** -/
def localDyn : ReversibleDynamics ι Q where
  φ := localEquiv Λ σ
  G := localFiniteRange Λ σ
  G' := localFiniteRange Λ σ.symm

/-- **THE PERMUTATION OPERATOR OF A REGION-SUPPORTED DYNAMICS IS A LOCAL OPERATOR**, namely the
embedded permutation matrix of the region's permutation. This is the bridge between the scaffold
picture, where the dynamics permutes global configurations, and the algebra picture, where it is
conjugation by an element of one region's stage. -/
theorem permOp_localDyn : permOp (localDyn Λ σ) = emb Λ (permMat σ) := by
  apply Finsupp.lhom_ext
  intro s c
  rw [permOp_single, emb_single, Finset.sum_eq_single (σ (glob Λ s))]
  · rw [permMat_apply, if_pos rfl, one_smul, Finsupp.smul_single, smul_eq_mul, mul_one]
    rfl
  · intro f _ hf
    rw [permMat_apply, if_neg (Ne.symm hf), zero_smul]
  · intro h
    exact absurd (Finset.mem_univ (σ (glob Λ s))) h

theorem permOpInv_localDyn : permOpInv (localDyn Λ σ) = emb Λ (permMat σ.symm) := by
  apply Finsupp.lhom_ext
  intro s c
  rw [permOpInv_single, emb_single, Finset.sum_eq_single (σ.symm (glob Λ s))]
  · rw [permMat_apply, if_pos rfl, one_smul, Finsupp.smul_single, smul_eq_mul, mul_one]
    rfl
  · intro f _ hf
    rw [permMat_apply, if_neg (Ne.symm hf), zero_smul]
  · intro h
    exact absurd (Finset.mem_univ (σ.symm (glob Λ s))) h

/-- **THE HEISENBERG ACTION OF A REGION-SUPPORTED DYNAMICS IS LOCAL CONJUGATION.** -/
theorem heis_localDyn (T : Module.End ℂ (Scaffold ι Q)) :
    heis (localDyn Λ σ) T = emb Λ (permMat σ.symm) * T * emb Λ (permMat σ) := by
  rw [heis, permOp_localDyn, permOpInv_localDyn]

theorem heisLoc_localDyn (a : localAlg ι Q) :
    heisLoc (localDyn Λ σ) a = ofM Λ (permMat σ.symm) * a * ofM Λ (permMat σ) :=
  Subtype.ext (heis_localDyn Λ σ a.1)

theorem heisQ_localDyn (x : Quasilocal ι Q) :
    heisQ (localDyn Λ σ) x = stage Λ (permMat σ.symm) * x * stage Λ (permMat σ) := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq (continuous_heisQ _)
      ((continuous_const.mul continuous_id).mul continuous_const)
  · rw [heisQ_coe, heisLoc_localDyn, UniformSpace.Completion.coe_mul,
      UniformSpace.Completion.coe_mul, stage_apply, stage_apply]

variable {Λ σ}

/-- **STABILIZATION AT THE SCAFFOLD LEVEL.** Two dynamics with the same effect on a region — the
same restricted configuration, and the same off-region agreement relation — have the same
Heisenberg action on that region's observables. This is what lets a layer over all sites be
replaced, on any one local observable, by a dynamics supported in a finite region. -/
theorem heis_eq_of_agree {Φ Ψ : ReversibleDynamics ι Q}
    (hglob : ∀ t : ι → Q, glob Λ (Φ.φ t) = glob Λ (Ψ.φ t))
    (hoff : ∀ t s : ι → Q, AgreeOffG Λ (Φ.φ t) (Φ.φ s) ↔ AgreeOffG Λ (Ψ.φ t) (Ψ.φ s))
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    heis Φ (emb Λ X) = heis Ψ (emb Λ X) := by
  apply ext_of_kerOf
  funext t s
  rw [kerOf_heis, kerOf_heis]
  simp only [kerOf_emb]
  by_cases h : AgreeOffG Λ (Φ.φ t) (Φ.φ s)
  · rw [kern_of_agree _ h, kern_of_agree _ ((hoff t s).mp h), hglob t, hglob s]
  · rw [kern_of_not_agree _ h, kern_of_not_agree _ fun hc => h ((hoff t s).mpr hc)]

end Localized

/-! ### Section E — the swap layer's endpoint -/

section SwapEndpoint

variable {V : Type} [Fintype V] [DecidableEq V] [Nonempty V] [AddCommGroup V]

/-- The on-site exchange read on a whole region. -/
def regionSwap (V : Type) [Fintype V] [DecidableEq V] [Nonempty V] [AddCommGroup V]
    (Λ : Finset ι) : Conf Λ (V × V) ≃ Conf Λ (V × V) where
  toFun f := fun u => ((f u).2, (f u).1)
  invFun f := fun u => ((f u).2, (f u).1)
  left_inv _ := rfl
  right_inv _ := rfl

theorem regionSwap_involutive (Λ : Finset ι) (f : Conf Λ (V × V)) :
    regionSwap V Λ (regionSwap V Λ f) = f := rfl

theorem regionSwap_symm (Λ : Finset ι) : (regionSwap V Λ).symm = regionSwap V Λ := rfl

theorem swapEquivAt_eq_regionSwap (i : ι) : swapEquivAt V i = regionSwap V {i} :=
  Equiv.ext fun _ => rfl

/-- **THE REGION SWAPS COMPOSE.** Two disjoint regions' swaps multiply to the swap of their
union, which is what makes the finite gate product a single region's permutation matrix. -/
theorem qGate_regionSwap_union {Λ₁ Λ₂ : Finset ι} (hd : Disjoint Λ₁ Λ₂) :
    qGate Λ₁ (regionSwap V Λ₁) * qGate Λ₂ (regionSwap V Λ₂)
      = qGate (Λ₁ ∪ Λ₂) (regionSwap V (Λ₁ ∪ Λ₂)) := by
  have h₁ : Λ₁ ⊆ Λ₁ ∪ Λ₂ := Finset.subset_union_left
  have h₂ : Λ₂ ⊆ Λ₁ ∪ Λ₂ := Finset.subset_union_right
  have hσ : (extPerm h₂ (regionSwap V Λ₂)).trans (extPerm h₁ (regionSwap V Λ₁))
      = regionSwap V (Λ₁ ∪ Λ₂) := by
    refine Equiv.ext fun G => funext fun u => ?_
    show extConf h₁ (regionSwap V Λ₁) (extConf h₂ (regionSwap V Λ₂) G) u = _
    by_cases hu : (u : ι) ∈ Λ₁
    · have hu₂ : (u : ι) ∉ Λ₂ := Finset.disjoint_left.mp hd hu
      rw [extConf_apply, dif_pos hu]
      show (((extConf h₂ (regionSwap V Λ₂) G) ⟨(u : ι), h₁ hu⟩).2,
        ((extConf h₂ (regionSwap V Λ₂) G) ⟨(u : ι), h₁ hu⟩).1) = _
      rw [extConf_apply, dif_neg hu₂]
      rfl
    · have hu₂ : (u : ι) ∈ Λ₂ := by
        rcases Finset.mem_union.mp u.2 with h | h
        · exact absurd h hu
        · exact h
      rw [extConf_apply, dif_neg hu, extConf_apply, dif_pos hu₂]
      rfl
  rw [qGate_extPerm h₁, qGate_extPerm h₂, qGate, qGate, qGate, ← map_mul, permMat_mul, hσ]

/-- **THE SWAP LAYER'S TIME-ONE UNITARY IS ONE REGION'S PERMUTATION MATRIX.** The finite product of
on-site gates over `Λ` is the permutation matrix of the swap of the whole of `Λ`. -/
theorem swapU_one_eq_qGate (Λ : Finset ι) :
    swapU V Λ 1 = qGate Λ (regionSwap V Λ) := by
  classical
  refine Finset.induction_on Λ ?_ ?_
  · rw [swapU_empty, qGate]
    have hid : regionSwap V (∅ : Finset ι) = Equiv.refl _ :=
      Equiv.ext fun f => funext fun u => absurd u.2 (Finset.notMem_empty _)
    rw [hid, permMat_refl, map_one]
  · intro a s ha ih
    have hd : Disjoint ({a} : Finset ι) s := Finset.disjoint_singleton_left.mpr ha
    rw [Finset.insert_eq, swapU_union V hd, ih, swapU_singleton,
      unit_one (swapGate_isGate V a).1, SwapLayer.swapGate, swapEquivAt_eq_regionSwap,
      qGate_regionSwap_union hd]

/-- The swap layer and the region-supported swap have the same effect on a region. -/
theorem glob_swapLayer (Λ : Finset ι) (t : ι → V × V) :
    glob Λ (swapLayer t) = regionSwap V Λ (glob Λ t) := rfl

theorem agreeOffG_swapLayer (Λ : Finset ι) (t s : ι → V × V) :
    AgreeOffG Λ (swapLayer t) (swapLayer s) ↔ AgreeOffG Λ t s := by
  constructor
  · intro h i hi
    have := h i hi
    rw [swapLayer_apply, swapLayer_apply, Prod.mk.injEq] at this
    exact Prod.ext this.2 this.1
  · intro h i hi
    rw [swapLayer_apply, swapLayer_apply, h i hi]

/-- **THE SWAP LAYER'S HEISENBERG ACTION IS LOCAL CONJUGATION ON EVERY REGION.** -/
theorem heis_swapDyn_emb (Λ : Finset ι) (X : Matrix (Conf Λ (V × V)) (Conf Λ (V × V)) ℂ) :
    heis (swapDyn V) (emb Λ X) = heis (localDyn Λ (regionSwap V Λ)) (emb Λ X) := by
  refine heis_eq_of_agree (fun t => ?_) (fun t s => ?_) X
  · show glob Λ (swapLayer t) = glob Λ (localConf Λ (regionSwap V Λ) t)
    rw [glob_localConf]
    rfl
  · show AgreeOffG Λ (swapLayer t) (swapLayer s) ↔
      AgreeOffG Λ (localConf Λ (regionSwap V Λ) t) (localConf Λ (regionSwap V Λ) s)
    rw [agreeOffG_swapLayer]
    constructor
    · intro h i hi
      rw [localConf_apply_of_not_mem hi, localConf_apply_of_not_mem hi]
      exact h i hi
    · intro h i hi
      have := h i hi
      rwa [localConf_apply_of_not_mem hi, localConf_apply_of_not_mem hi] at this

/-- **THE SWAP LAYER'S ENDPOINT.** At time one the swap flow is exactly the Heisenberg action of
the swap dynamics on the quasilocal algebra. The identification is made on staged local
observables, where both sides are conjugation by the same region's permutation matrix, and
extended by continuity. -/
theorem swapQ_one_eq_heisQ (x : Quasilocal ι (V × V)) :
    swapQ V 1 x = heisQ (swapDyn V) x := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq (continuous_swapQ V 1) (continuous_heisQ _)
  · obtain ⟨Λ, X, rfl⟩ := exists_ofM a
    have hstar : star (qGate Λ (regionSwap V Λ)) = qGate Λ (regionSwap V Λ) :=
      (localGate_isGate (regionSwap_involutive (V := V) Λ)).2
    rw [← stage_apply, swapQ_stage, swapAct, swapU_one_eq_qGate, hstar]
    have h1 : heisQ (swapDyn V) (stage Λ X)
        = heisQ (localDyn Λ (regionSwap V Λ)) (stage Λ X) := by
      rw [stage_apply, heisQ_coe, heisQ_coe]
      exact congrArg _ (Subtype.ext (heis_swapDyn_emb Λ X))
    rw [h1, heisQ_localDyn, regionSwap_symm, qGate]

end SwapEndpoint

end OIBridge.SecondOrderDrive

namespace OIBridge.SecondOrderDrive

#print axioms permOp_of_comp
#print axioms permOpInv_of_comp
#print axioms heis_of_comp
#print axioms heisLoc_of_comp
#print axioms heisQ_of_comp
#print axioms driveQ_apply
#print axioms driveQ_zero_time
#print axioms driveQ_mul
#print axioms driveQ_add
#print axioms driveQ_smul
#print axioms driveQ_star
#print axioms driveQ_sub
#print axioms driveQ_one
#print axioms norm_driveQ
#print axioms dist_driveQ
#print axioms continuous_driveQ
#print axioms driveQ_left_inverse
#print axioms driveQ_right_inverse
#print axioms driveQ_bijective
#print axioms continuous_driveQ_time
#print axioms driveQ_isContinuousPath
#print axioms mem_stepInfl_of_mem_gateRegion
#print axioms ruleDynamics_comp
#print axioms heisQ_ruleDynamics
#print axioms patch_patch
#print axioms glob_localConf
#print axioms localConf_localConf
#print axioms permOp_localDyn
#print axioms permOpInv_localDyn
#print axioms heis_localDyn
#print axioms heisLoc_localDyn
#print axioms heisQ_localDyn
#print axioms heis_eq_of_agree
#print axioms regionSwap_involutive
#print axioms swapEquivAt_eq_regionSwap
#print axioms qGate_regionSwap_union
#print axioms swapU_one_eq_qGate
#print axioms agreeOffG_swapLayer
#print axioms heis_swapDyn_emb
#print axioms swapQ_one_eq_heisQ

end OIBridge.SecondOrderDrive
