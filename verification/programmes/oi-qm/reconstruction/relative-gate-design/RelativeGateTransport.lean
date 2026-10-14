/-
  RelativeGateTransport.lean — design draft for KINF-COPY-1 (#822). Not a module of any tree,
  not compiled, not a round.

  `NativeGate2Of Ω avail z NC NT T` is #822's `NativeGate2 Ω z NC NT T` with `maxCone Ω` replaced
  by `maxConeOf avail` in exactly the two positivity clauses, as K1-BRIDGE-1's `NativeGateOf` is
  DIM-1's `NativeGate`. With `NC = NT` it is `NativeGateOf` (§A).

  §B, the transport. Each direction has its own hypothesis and its own theorem:
    relative → maximal needs `maxConeOf avail ⊆ maxCone Ω` (`nativeGate2_of_cone_subset`);
    maximal → relative needs `maxCone Ω ⊆ maxConeOf avail` (`nativeGate2Of_of_cone_superset`),
      which effect soundness alone gives (`maxCone_subset_maxConeOf`).
  With the cone equality both hold (`nativeGate2Of_iff_of_cone_eq`, one theorem per direction).
  §C, the relative conjugacy results: #822's `nativeGate2_conj` and `nativeGate_of_conj` through
  the cone equality, giving `NativeGate2Of` and K1-BRIDGE-1's `NativeGateOf` for the conjugated gate.
  §D, the relative selectors: under K1-BRIDGE-1's hypotheses (EFF-1's `maxConeOf_avail_eq`) or
  KTRANS-DENSE-1's (`maxConeOf_avail_eq_of_dense`), #822's selectors hold for `NativeGate2Of`;
  `dim_of_nativeGate2Of_conj_of_orbit` uses only the inclusion that the selector consumes, so it
  carries neither `0 < d` (from `pos_of_isNot`) nor effect soundness.
  §E, `CopyNatural` (KINF-2) gives #822's `hcov` for linear maps that are the coercions of affine
  equivalences.
  §F, the positive control at `d = 3` and the kernel half of the countercontrol.

  No new dimension argument: every selector here is #822's selector, hence DIM-1's
  `dim_of_nativeGate`, applied to the output of a transport that only rewrites positivity clauses.

  Compilation (design evidence only): on a disposable branch from M = 5bfdaba6, add
  `verification/lean-mathlib/OIBridge/CopyCovariance.lean` as blob fb9c73fe (commit 8c92343e, built
  in run 38091534622) and this file as `OIBridge/RelativeGateTransport.lean`; append
  `import OIBridge.CopyCovariance` and `import OIBridge.RelativeGateTransport` after
  `import OIBridge.EqvK2MaxCone` in `OIBridge.lean`; dispatch `verify.yml` on the branch head. The
  release gate fails at `lean-manuscript` (two unregistered modules) unless census entries are added.

  Steps marked `-- [unsure]` are ones whose elaboration was not checked against a compiler.
-/
import OIBridge.CopyCovariance

namespace OIBridge
namespace RelativeGateTransport

open Set KInfFoundations OrbitGeneration TransitiveBody CompositeDimension CompositeInterface
open EffectSpace K1Bridge DenseOrbit CopyCovariance

variable {d : ℕ}

/-! ### §A — the relative two-NOT hypotheses -/

/-- #822's `NativeGate2` relative to a family `avail` of available test functionals: the frame,
the two NOT relations with `NC` on the control copy and `NT` on the target copy, and, in place of
`maxCone Ω`, two-sided positivity on the cone of the products of the family. -/
structure NativeGate2Of (Ω : Set (Fin d → ℝ)) (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ))
    (z : Fin d → ℝ) (NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (T : W d ≃ₗ[ℝ] W d) : Prop where
  frame : ∀ a b : Fin 2,
    T (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))
  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, T (prodState x y) ∈ maxConeOf avail
  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, T.symm (prodState x y) ∈ maxConeOf avail
  relT : ∀ ω, actT NT (T (actT NT ω)) = T ω
  relC : ∀ ω, actC NC (T (actC NC ω)) = actT NT (T ω)

theorem nativeGate2Of_of_nativeGateOf {Ω : Set (Fin d → ℝ)}
    {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {T : W d ≃ₗ[ℝ] W d} (hT : NativeGateOf Ω avail z N T) : NativeGate2Of Ω avail z N N T :=
  ⟨hT.frame, hT.posFwd, hT.posInv, hT.relT, hT.relC⟩

theorem nativeGateOf_of_nativeGate2Of {Ω : Set (Fin d → ℝ)}
    {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {T : W d ≃ₗ[ℝ] W d} (hT : NativeGate2Of Ω avail z N N T) : NativeGateOf Ω avail z N T :=
  ⟨hT.frame, hT.posFwd, hT.posInv, hT.relT, hT.relC⟩

/-! ### §B — the transport, one theorem per direction -/

section Transport

variable {Ω : Set (Fin d → ℝ)} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)} {z : Fin d → ℝ}
  {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}

/-- **Relative to maximal.** The family's cone inside the maximal cone carries the relative
two-NOT hypotheses to #822's. -/
theorem nativeGate2_of_cone_subset (h : maxConeOf avail ⊆ maxCone Ω)
    (hT : NativeGate2Of Ω avail z NC NT T) : NativeGate2 Ω z NC NT T where
  frame := hT.frame
  posFwd := fun x hx y hy => h (hT.posFwd x hx y hy)
  posInv := fun x hx y hy => h (hT.posInv x hx y hy)
  relT := hT.relT
  relC := hT.relC

/-- **Maximal to relative.** The maximal cone inside the family's cone carries #822's two-NOT
hypotheses to the relative ones. -/
theorem nativeGate2Of_of_cone_superset (h : maxCone Ω ⊆ maxConeOf avail)
    (hT : NativeGate2 Ω z NC NT T) : NativeGate2Of Ω avail z NC NT T where
  frame := hT.frame
  posFwd := fun x hx y hy => h (hT.posFwd x hx y hy)
  posInv := fun x hx y hy => h (hT.posInv x hx y hy)
  relT := hT.relT
  relC := hT.relC

/-- The one-NOT form of `nativeGate2Of_of_cone_superset`: the converse direction of K1-BRIDGE-1's
`nativeGate_of_cone_eq`, with its own hypothesis. -/
theorem nativeGateOf_of_cone_superset {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (h : maxCone Ω ⊆ maxConeOf avail) (hT : NativeGate Ω z N T) : NativeGateOf Ω avail z N T where
  frame := hT.frame
  posFwd := fun x hx y hy => h (hT.posFwd x hx y hy)
  posInv := fun x hx y hy => h (hT.posInv x hx y hy)
  relT := hT.relT
  relC := hT.relC

/-- Effect soundness alone puts the maximal cone inside the family's cone: the second half of
EFF-1's `maxConeOf_avail_eq`, isolated. -/
theorem maxCone_subset_maxConeOf (hE : EffectsOn Ω avail) : maxCone Ω ⊆ maxConeOf avail := by
  rw [← maxConeOf_fullEffects]
  exact maxConeOf_anti fun e he => hE e he

/-- The cone equality, relative to maximal (K1-BRIDGE-1's proof pattern). -/
theorem nativeGate2_of_cone_eq (h : maxConeOf avail = maxCone Ω)
    (hT : NativeGate2Of Ω avail z NC NT T) : NativeGate2 Ω z NC NT T where
  frame := hT.frame
  posFwd := fun x hx y hy => by
    have hp := hT.posFwd x hx y hy
    rwa [h] at hp
  posInv := fun x hx y hy => by
    have hp := hT.posInv x hx y hy
    rwa [h] at hp
  relT := hT.relT
  relC := hT.relC

/-- The cone equality, maximal to relative. -/
theorem nativeGate2Of_of_cone_eq (h : maxConeOf avail = maxCone Ω)
    (hT : NativeGate2 Ω z NC NT T) : NativeGate2Of Ω avail z NC NT T where
  frame := hT.frame
  posFwd := fun x hx y hy => by
    have hp := hT.posFwd x hx y hy
    rwa [← h] at hp
  posInv := fun x hx y hy => by
    have hp := hT.posInv x hx y hy
    rwa [← h] at hp
  relT := hT.relT
  relC := hT.relC

/-- The one-NOT form of `nativeGate2Of_of_cone_eq`. -/
theorem nativeGateOf_of_cone_eq {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (h : maxConeOf avail = maxCone Ω) (hT : NativeGate Ω z N T) : NativeGateOf Ω avail z N T where
  frame := hT.frame
  posFwd := fun x hx y hy => by
    have hp := hT.posFwd x hx y hy
    rwa [← h] at hp
  posInv := fun x hx y hy => by
    have hp := hT.posInv x hx y hy
    rwa [← h] at hp
  relT := hT.relT
  relC := hT.relC

/-- Under the cone equality the relative and maximal two-NOT hypotheses agree. Forward:
`nativeGate2_of_cone_eq`; backward: `nativeGate2Of_of_cone_eq`. -/
theorem nativeGate2Of_iff_of_cone_eq (h : maxConeOf avail = maxCone Ω) :
    NativeGate2Of Ω avail z NC NT T ↔ NativeGate2 Ω z NC NT T :=
  ⟨nativeGate2_of_cone_eq h, nativeGate2Of_of_cone_eq h⟩

end Transport

/-! ### §C — #822's conjugacy results for the relative form -/

section Conjugacy

variable {Ω : Set (Fin d → ℝ)} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)} {z : Fin d → ℝ}
  {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}

/-- **Conjugation on the target copy, relative form.** #822's `nativeGate2_conj` between the two
directions of the transport. -/
theorem nativeGate2Of_conj (hcone : maxConeOf avail = maxCone Ω)
    (hT : NativeGate2Of Ω avail z NC NT T) {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ Ω, g x ∈ Ω) (hhΩ : ∀ x ∈ Ω, h x ∈ Ω) (hgz : g z = z) :
    NativeGate2Of Ω avail z NC (h ∘ₗ NT ∘ₗ g)
      (actTEq g h hgh hhg ≪≫ₗ T ≪≫ₗ actTEq h g hhg hgh) :=
  nativeGate2Of_of_cone_eq hcone
    (nativeGate2_conj (nativeGate2_of_cone_eq hcone hT) hgh hhg hgΩ hhΩ hgz)

/-- **Type covariance gives K1-BRIDGE-1's relative native gate.** #822's `nativeGate_of_conj`
between the two directions of the transport. -/
theorem nativeGateOf_of_conj (hcone : maxConeOf avail = maxCone Ω)
    (hT : NativeGate2Of Ω avail z NC NT T) {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ Ω, g x ∈ Ω) (hhΩ : ∀ x ∈ Ω, h x ∈ Ω) (hgz : g z = z)
    (hcov : ∀ x, NT (g x) = g (NC x)) :
    NativeGateOf Ω avail z NC (actTEq g h hgh hhg ≪≫ₗ T ≪≫ₗ actTEq h g hhg hgh) :=
  nativeGateOf_of_cone_eq hcone
    (nativeGate_of_conj (nativeGate2_of_cone_eq hcone hT) hgh hhg hgΩ hhΩ hgz hcov)

end Conjugacy

/-! ### §D — the relative selectors -/

section Bridge

variable {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ}
  {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}

/-- **The selector under type covariance, relative to the available family.** K1-BRIDGE-1's
hypotheses give EFF-1's cone equality; the transport and #822's `dim_of_nativeGate2_conj` give
`d ∈ {1, 3}`. -/
theorem dim_of_nativeGate2Of_conj (hd : 0 < d) (hE : EffectsOn (eball d) avail)
    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)
    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail)
    {z : Fin d → ℝ} {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z NC) (hT : NativeGate2Of (eball d) avail z NC NT T)
    {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d)
    (hgz : g z = z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 1 ∨ d = 3 :=
  dim_of_nativeGate2_conj hN
    (nativeGate2_of_cone_eq (maxConeOf_avail_eq hd hG hP1 hK hV4 hE) hT)
    hgh hhg hgΩ hhΩ hgz hcov

/-- **Three under type covariance and `2 ≤ d`, relative form.** #822's
`three_of_nativeGate2_conj_of_two_le` through the transport. -/
theorem three_of_nativeGate2Of_conj_of_two_le (hd : 2 ≤ d) (hE : EffectsOn (eball d) avail)
    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)
    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail)
    {z : Fin d → ℝ} {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z NC) (hT : NativeGate2Of (eball d) avail z NC NT T)
    {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d)
    (hgz : g z = z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 3 :=
  three_of_nativeGate2_conj_of_two_le hd hN
    (nativeGate2_of_cone_eq (maxConeOf_avail_eq (by omega) hG hP1 hK hV4 hE) hT)
    hgh hhg hgΩ hhΩ hgz hcov

/-- **A conjugator reversing the corner axis, relative form.** #822's
`dim_of_nativeGate2_conj_neg` through the transport. -/
theorem dim_of_nativeGate2Of_conj_neg (hd : 0 < d) (hE : EffectsOn (eball d) avail)
    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)
    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail)
    {z : Fin d → ℝ} {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z NC) (hT : NativeGate2Of (eball d) avail z NC NT T)
    {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d)
    (hgz : g z = -z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 1 ∨ d = 3 :=
  dim_of_nativeGate2_conj_neg hN
    (nativeGate2_of_cone_eq (maxConeOf_avail_eq hd hG hP1 hK hV4 hE) hT)
    hgh hhg hgΩ hhΩ hgz hcov

/-- **The relative selector under a dense boundary orbit.** KTRANS-DENSE-1's cone equality in place
of EFF-1's. -/
theorem dim_of_nativeGate2Of_conj_dense (hd : 0 < d) (hE : EffectsOn (eball d) avail)
    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)
    (hK : DenseBoundaryOrbit (eball d) G) (hV4 : SeedOrbitAvailable G r avail)
    {z : Fin d → ℝ} {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z NC) (hT : NativeGate2Of (eball d) avail z NC NT T)
    {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d)
    (hgz : g z = z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 1 ∨ d = 3 :=
  dim_of_nativeGate2_conj hN
    (nativeGate2_of_cone_eq (maxConeOf_avail_eq_of_dense hd hG hP1 hK hV4 hE) hT)
    hgh hhg hgΩ hhΩ hgz hcov

/-- The inclusion the selector consumes: the first half of EFF-1's `maxConeOf_avail_eq`, isolated
(the same two steps as its proof). It uses neither effect soundness nor anything about `avail`
beyond K∞-V4. -/
theorem maxConeOf_subset_maxCone_of_orbit (hd : 0 < d) (hG : PreservesBody (eball d) G)
    (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G)
    (hV4 : SeedOrbitAvailable G r avail) : maxConeOf avail ⊆ maxCone (eball d) :=
  (maxConeOf_anti (sharpFamily_subset_avail hG hP1 hK hV4)).trans
    (maxConeOf_sharp_subset_maxCone hd)

/-- **The relative selector with only the inclusion it consumes.** No `0 < d` (DIM-1's
`pos_of_isNot`) and no effect soundness. -/
theorem dim_of_nativeGate2Of_conj_of_orbit (hG : PreservesBody (eball d) G)
    (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G)
    (hV4 : SeedOrbitAvailable G r avail)
    {z : Fin d → ℝ} {NC NT : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}
    (hN : IsNot (eball d) z NC) (hT : NativeGate2Of (eball d) avail z NC NT T)
    {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ eball d, g x ∈ eball d) (hhΩ : ∀ x ∈ eball d, h x ∈ eball d)
    (hgz : g z = z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 1 ∨ d = 3 :=
  dim_of_nativeGate2_conj hN
    (nativeGate2_of_cone_subset
      (maxConeOf_subset_maxCone_of_orbit (pos_of_isNot hN) hG hP1 hK hV4) hT)
    hgh hhg hgΩ hhΩ hgz hcov

end Bridge

/-! ### §E — copy naturality gives `hcov` -/

/-- KINF-2's `CopyNatural eC eT eg` (the NOT of the target copy is the conjugate of the NOT of the
control copy under the identification `eg`) gives #822's `hcov` for the linear maps that are the
coercions of `eC`, `eT` and `eg`. Only this direction is stated. -/
theorem hcov_of_copyNatural {NC NT g : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {eC eT eg : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)} (hC : ∀ x, eC x = NC x)
    (hT : ∀ x, eT x = NT x) (hg : ∀ x, eg x = g x) (hnat : CopyNatural eC eT eg) :
    ∀ x, NT (g x) = g (NC x) := by
  intro x
  have hx := (copyNatural_iff_apply eC eT eg).1 hnat x
  calc NT (g x) = eT (eg x) := by rw [hg x, hT (g x)]
    _ = eg (eC x) := hx  -- [unsure] defeq of the normed-space and Pi instance paths
    _ = g (NC x) := by rw [hC x, hg (NC x)]

/-! ### §F — controls -/

/-- **Positive control.** At `d = 3`, with the sharp family and the unit under the full
automorphism family (EFF-1's `not_fullEffects_of_orbit`), every hypothesis of
`dim_of_nativeGate2Of_conj` holds for #822's swapped gate, whose two NOTs differ. -/
theorem swapped_relative_hyps :
    ∃ (G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))) (r : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ),
      EffectsOn (eball 3) (sharpUnitFamily 3) ∧ PreservesBody (eball 3) G ∧
      SharpSeed (eball 3) r ∧ BoundaryTransitive (eball 3) G ∧
      SeedOrbitAvailable G r (sharpUnitFamily 3) ∧ IsNot (eball 3) z3 nflip ∧
      NativeGate2Of (eball 3) (sharpUnitFamily 3) z3 nflip (swap01 ∘ₗ nflip ∘ₗ swap01)
        (actTEq swap01 swap01 swap01_swap01 swap01_swap01 ≪≫ₗ cnot ≪≫ₗ
          actTEq swap01 swap01 swap01_swap01 swap01_swap01) ∧
      swap01 ∘ₗ nflip ∘ₗ swap01 ≠ nflip ∧
      (∀ x, (swap01 ∘ₗ nflip ∘ₗ swap01) (swap01 x) = swap01 (nflip x)) := by
  obtain ⟨hG, hP1, hK, hV4, -, hE, -, -⟩ := not_fullEffects_of_orbit (d := 3) (by norm_num)
  -- [unsure] the seed witness `_` is solved from `hP1`; if not, name it `sharpEff (axisVec _)`
  exact ⟨fullAut 3, _, hE, hG, hP1, hK, hV4, isNot_nflip,
    nativeGate2Of_of_cone_eq (maxConeOf_avail_eq (by norm_num) hG hP1 hK hV4 hE)
      swapped_nativeGate2,
    swapped_not_ne, fun x => by simp only [LinearMap.comp_apply, swap01_swap01]⟩

/-- The positive control drives the relative selector (route A: transport, then #822's selector). -/
example : (3 : ℕ) = 1 ∨ (3 : ℕ) = 3 := by
  obtain ⟨G, r, hE, hG, hP1, hK, hV4, hN, hT, -, hcov⟩ := swapped_relative_hyps
  exact dim_of_nativeGate2Of_conj (by norm_num) hE hG hP1 hK hV4 hN hT swap01_swap01
    swap01_swap01 (fun _ hx => swap01_mem hx) (fun _ hx => swap01_mem hx) swap01_z3 hcov

/-- The positive control drives K1-BRIDGE-1's landed relative selector (route B: the relative
reduction `nativeGateOf_of_conj`, then `dim_of_nativeGateOf`). -/
example : (3 : ℕ) = 1 ∨ (3 : ℕ) = 3 := by
  obtain ⟨G, r, hE, hG, hP1, hK, hV4, hN, hT, -, hcov⟩ := swapped_relative_hyps
  exact K1Bridge.dim_of_nativeGateOf (by norm_num) hE hG hP1 hK hV4 hN
    (nativeGateOf_of_conj (maxConeOf_avail_eq (by norm_num) hG hP1 hK hV4 hE) hT swap01_swap01
      swap01_swap01 (fun _ hx => swap01_mem hx) (fun _ hx => swap01_mem hx) swap01_z3 hcov)

/- **Countercontrol, kernel half.** Effect soundness alone does not give the cone equality that
`nativeGate2_of_cone_eq` consumes: K1-BRIDGE-1's landed `cone_eq_fails_axis`, cited, not restated.
The conclusion-level half (a gate that is relative native-gate data for `axisFamily` and is not
`NativeGate` data) is the exact probe `relgate_counter.py`; its kernel statement would be
`NativeGateOf (eball 3) axisFamily z3 nflip T_S ∧ ¬ NativeGate (eball 3) z3 nflip T_S`, with
`T_S = cnot` followed by `diag(2, 1, 1)` on both copies. -/
example : EffectsOn (eball 3) axisFamily ∧ maxConeOf axisFamily ≠ maxCone (eball 3) :=
  cone_eq_fails_axis

end RelativeGateTransport
end OIBridge

#print axioms OIBridge.RelativeGateTransport.nativeGate2_of_cone_subset
#print axioms OIBridge.RelativeGateTransport.nativeGate2Of_of_cone_superset
#print axioms OIBridge.RelativeGateTransport.maxCone_subset_maxConeOf
#print axioms OIBridge.RelativeGateTransport.nativeGate2Of_iff_of_cone_eq
#print axioms OIBridge.RelativeGateTransport.nativeGate2Of_conj
#print axioms OIBridge.RelativeGateTransport.nativeGateOf_of_conj
#print axioms OIBridge.RelativeGateTransport.dim_of_nativeGate2Of_conj
#print axioms OIBridge.RelativeGateTransport.three_of_nativeGate2Of_conj_of_two_le
#print axioms OIBridge.RelativeGateTransport.dim_of_nativeGate2Of_conj_neg
#print axioms OIBridge.RelativeGateTransport.dim_of_nativeGate2Of_conj_dense
#print axioms OIBridge.RelativeGateTransport.dim_of_nativeGate2Of_conj_of_orbit
#print axioms OIBridge.RelativeGateTransport.hcov_of_copyNatural
#print axioms OIBridge.RelativeGateTransport.swapped_relative_hyps
