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

end OIBridge.SecondOrderDrive
