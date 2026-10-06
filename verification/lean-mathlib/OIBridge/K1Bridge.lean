/-
  OIBridge/K1Bridge.lean — round K1-BRIDGE-1: DIM-1's dimension selectors relative to a family of
  available test functionals.

  Round DIM-1 states its native-gate hypotheses with two positivity clauses on the maximal product
  cone `maxCone Ω`, the cone of joint vectors nonnegative on every product of two effects of `Ω`,
  and its entangling clause on the joint states of that cone. Round EFF-1 proved that on the
  coordinate ball `eball d`, for `0 < d`, the cone of the products of any family of available
  functionals is `maxCone (eball d)` once every available functional is an effect and the family
  satisfies OG-1's four named hypotheses — body preservation, K∞-Seed, K∞-Trans and K∞-V4
  (`maxConeOf_avail_eq`).

  This module restates DIM-1's hypotheses relative to the available family and composes the two
  rounds. `NativeGateOf Ω avail z N T` is `NativeGate Ω z N T` with `maxCone Ω` replaced by
  `maxConeOf avail` in the two positivity clauses and nothing else changed; `EntanglingOf Ω avail T`
  is `Entangling Ω T` with the joint states of `maxConeOf avail`. The bridge is the cone equality:
  it carries the relative hypotheses to DIM-1's (`nativeGate_of_cone_eq`, `entangling_of_cone_eq`),
  and the relative selectors `dim_of_nativeGateOf` and `three_of_nativeGateOf` are the cone
  equality, that transport and DIM-1's landed selectors, with no new dimension argument.

  Controls, carried from EFF-1: at `d = 0` the sharp family is empty and the cone equality fails
  (`cone_eq_fails_zero`), so `0 < d` is load-bearing; at `d = 3` the effects of one axis with the
  unit determine a strictly larger cone (`cone_eq_fails_axis`), so the cone equality is not free
  for an arbitrary family and the four hypotheses are load-bearing.

  Body preservation, K∞-Seed, K∞-Trans, K∞-V4, effect soundness (`EffectsOn`), DIM-1's `IsNot` and
  the relative native-gate and entangling hypotheses are premises; nothing here sources any of them
  from any construction. The product form of the composite tests, DIM-1's carrier `W d`, is a
  premise of both rounds and is not addressed. No mixing closure and no unit premise is used. No
  limit closure, no drive, no complex structure and no matrix representation is used or claimed.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.EffectSpace

namespace OIBridge
namespace K1Bridge

open Set KInfFoundations OrbitGeneration TransitiveBody CompositeDimension CompositeInterface
  EffectSpace

variable {d : ℕ}

/-! ### §A — the relative hypotheses -/

/-- DIM-1's native-gate hypotheses relative to a family `avail` of available test functionals: the
frame, the two NOT relations and, in place of `maxCone Ω`, two-sided positivity on the cone of the
products of the family. -/
structure NativeGateOf (Ω : Set (Fin d → ℝ)) (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) (z : Fin d → ℝ)
    (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (T : W d ≃ₗ[ℝ] W d) : Prop where
  frame : ∀ a b : Fin 2,
    T (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))
  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, T (prodState x y) ∈ maxConeOf avail
  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, T.symm (prodState x y) ∈ maxConeOf avail
  relT : ∀ ω, actT N (T (actT N ω)) = T ω
  relC : ∀ ω, actC N (T (actC N ω)) = actT N (T ω)

/-- The joint states relative to the family: the normalized vectors of its product cone. -/
def jointStatesOf (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) : Set (W d) :=
  {ω | ω ∈ maxConeOf avail ∧ ω 0 0 = 1}

/-- DIM-1's entangling clause relative to the family: some pure product input has an image that is
an extreme joint state of the family's cone and is not a product state. -/
def EntanglingOf (Ω : Set (Fin d → ℝ)) (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ))
    (T : W d ≃ₗ[ℝ] W d) : Prop :=
  ∃ x ∈ Ω.extremePoints ℝ, ∃ y ∈ Ω.extremePoints ℝ,
    T (prodState x y) ∈ (jointStatesOf avail).extremePoints ℝ ∧ ¬ IsProduct Ω (T (prodState x y))

/-! ### §B — the bridge: the cone equality carries the relative hypotheses to DIM-1's -/

/-- With the family's cone equal to the maximal cone, the relative native-gate hypotheses are
DIM-1's. -/
theorem nativeGate_of_cone_eq {Ω : Set (Fin d → ℝ)} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}
    {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}
    (h : maxConeOf avail = maxCone Ω) (hT : NativeGateOf Ω avail z N T) :
    NativeGate Ω z N T where
  frame := hT.frame
  posFwd := fun x hx y hy => by
    have hp := hT.posFwd x hx y hy
    rwa [h] at hp
  posInv := fun x hx y hy => by
    have hp := hT.posInv x hx y hy
    rwa [h] at hp
  relT := hT.relT
  relC := hT.relC

/-- With the family's cone equal to the maximal cone, the relative joint states are DIM-1's. -/
theorem jointStatesOf_eq {Ω : Set (Fin d → ℝ)} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}
    (h : maxConeOf avail = maxCone Ω) : jointStatesOf avail = jointStates Ω := by
  unfold jointStatesOf jointStates
  rw [h]

/-- With the family's cone equal to the maximal cone, the relative entangling clause is DIM-1's. -/
theorem entangling_of_cone_eq {Ω : Set (Fin d → ℝ)} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}
    {T : W d ≃ₗ[ℝ] W d} (h : maxConeOf avail = maxCone Ω) (hE : EntanglingOf Ω avail T) :
    Entangling Ω T := by
  obtain ⟨x, hx, y, hy, hext, hnp⟩ := hE
  rw [jointStatesOf_eq h] at hext
  exact ⟨x, hx, y, hy, hext, hnp⟩

section Bridge

variable {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ}
  {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}

/-- On `eball d`, `0 < d`, effect soundness and the four hypotheses carry the relative native-gate
hypotheses to DIM-1's, through EFF-1's cone equality. -/
theorem nativeGate_of_avail (hd : 0 < d) (hE : EffectsOn (eball d) avail)
    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)
    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail)
    {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}
    (hT : NativeGateOf (eball d) avail z N T) : NativeGate (eball d) z N T :=
  nativeGate_of_cone_eq (maxConeOf_avail_eq hd hG hP1 hK hV4 hE) hT

/-- On `eball d`, `0 < d`, effect soundness and the four hypotheses carry the relative entangling
clause to DIM-1's, through EFF-1's cone equality. -/
theorem entangling_of_avail (hd : 0 < d) (hE : EffectsOn (eball d) avail)
    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)
    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail)
    {T : W d ≃ₗ[ℝ] W d} (hEnt : EntanglingOf (eball d) avail T) : Entangling (eball d) T :=
  entangling_of_cone_eq (maxConeOf_avail_eq hd hG hP1 hK hV4 hE) hEnt

/-! ### §C — the relative selectors -/

/-- **The dimension, relative to the available family.** `0 < d`, effect soundness, body
preservation, K∞-Seed, K∞-Trans, K∞-V4, DIM-1's NOT and the relative native-gate hypotheses give
`d ∈ {1, 3}`: EFF-1's cone equality, the transport of §B and DIM-1's `dim_of_nativeGate`. -/
theorem dim_of_nativeGateOf (hd : 0 < d) (hE : EffectsOn (eball d) avail)
    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)
    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail)
    {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T) : d = 1 ∨ d = 3 :=
  dim_of_nativeGate hN (nativeGate_of_avail hd hE hG hP1 hK hV4 hT)

/-- **Three, relative to the available family.** The hypotheses of `dim_of_nativeGateOf` with the
relative entangling clause give `d = 3`: EFF-1's cone equality, the transport of §B and DIM-1's
`three_of_nativeGate`. -/
theorem three_of_nativeGateOf (hd : 0 < d) (hE : EffectsOn (eball d) avail)
    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)
    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail)
    {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T)
    (hEnt : EntanglingOf (eball d) avail T) : d = 3 :=
  three_of_nativeGate hN (nativeGate_of_avail hd hE hG hP1 hK hV4 hT)
    (entangling_of_avail hd hE hG hP1 hK hV4 hEnt)

end Bridge

/-! ### §D — controls, carried from EFF-1 -/

/-- At `d = 0` the sharp family is empty and the cone equality the bridge consumes fails. -/
theorem cone_eq_fails_zero : maxConeOf (sharpFamily 0) ≠ maxCone (eball 0) :=
  maxConeOf_sharpFamily_zero_ne

/-- At `d = 3` the effects of one axis with the unit are effects whose cone is strictly larger than
the maximal cone: the cone equality the bridge consumes is not free for an arbitrary family. -/
theorem cone_eq_fails_axis : EffectsOn (eball 3) axisFamily ∧ maxConeOf axisFamily ≠ maxCone (eball 3) :=
  ⟨fun e he => by
    rcases he with rfl | rfl | rfl
    · exact isEffectOn_unitEff (eball 3)
    · exact sharpEff_isEffectOn (by simp [Fin.sum_univ_succ])
    · exact sharpEff_isEffectOn (by simp [Fin.sum_univ_succ]),
    maxConeOf_axis_ne⟩

/-! ### The verdict -/

/-- The two relative selectors with the two controls, together. -/
theorem k1b_core :
    (∀ (d : ℕ) (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))) (r : (Fin d → ℝ) →ᵃ[ℝ] ℝ)
        (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))
        (T : W d ≃ₗ[ℝ] W d), 0 < d → EffectsOn (eball d) avail → PreservesBody (eball d) G →
        SharpSeed (eball d) r → BoundaryTransitive (eball d) G → SeedOrbitAvailable G r avail →
        IsNot (eball d) z N → NativeGateOf (eball d) avail z N T → d = 1 ∨ d = 3) ∧
    (∀ (d : ℕ) (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))) (r : (Fin d → ℝ) →ᵃ[ℝ] ℝ)
        (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ))
        (T : W d ≃ₗ[ℝ] W d), 0 < d → EffectsOn (eball d) avail → PreservesBody (eball d) G →
        SharpSeed (eball d) r → BoundaryTransitive (eball d) G → SeedOrbitAvailable G r avail →
        IsNot (eball d) z N → NativeGateOf (eball d) avail z N T →
        EntanglingOf (eball d) avail T → d = 3) ∧
    maxConeOf (sharpFamily 0) ≠ maxCone (eball 0) ∧
    (EffectsOn (eball 3) axisFamily ∧ maxConeOf axisFamily ≠ maxCone (eball 3)) :=
  ⟨fun _ _ _ _ _ _ _ hd hE hG hP1 hK hV4 hN hT => dim_of_nativeGateOf hd hE hG hP1 hK hV4 hN hT,
    fun _ _ _ _ _ _ _ hd hE hG hP1 hK hV4 hN hT hEnt =>
      three_of_nativeGateOf hd hE hG hP1 hK hV4 hN hT hEnt,
    cone_eq_fails_zero,
    cone_eq_fails_axis⟩

end K1Bridge
end OIBridge

#print axioms OIBridge.K1Bridge.nativeGate_of_cone_eq
#print axioms OIBridge.K1Bridge.jointStatesOf_eq
#print axioms OIBridge.K1Bridge.entangling_of_cone_eq
#print axioms OIBridge.K1Bridge.nativeGate_of_avail
#print axioms OIBridge.K1Bridge.entangling_of_avail
#print axioms OIBridge.K1Bridge.dim_of_nativeGateOf
#print axioms OIBridge.K1Bridge.three_of_nativeGateOf
#print axioms OIBridge.K1Bridge.cone_eq_fails_zero
#print axioms OIBridge.K1Bridge.cone_eq_fails_axis
#print axioms OIBridge.K1Bridge.k1b_core
