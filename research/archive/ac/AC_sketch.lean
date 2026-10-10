/-
  AC_sketch.lean — UNCOMPILED SKETCH (no Lean toolchain in this environment). Off-repo research
  material for thread AC. Not a kernel statement, not frozen, not proposed for landing. Names are
  illustrative. Every `sorry` marks a step argued in AC-LEDGER.md §3 (written) and not checked.

  Purpose: state the closure-invariant ("dense-orbit") weakening of the transitivity premise that
  TRB-1 (`eq_qBall_of_boundaryTransitive`, TransitiveBody.lean:457) and EFF-1
  (`maxConeOf_avail_eq`, EffectSpace.lean:572) actually consume, so that a COUNTABLE raw operation
  family can feed them without any topological closure of the family.

  Directions (§A.34): only `boundaryTransitive → denseBoundaryOrbit` is claimed as an implication
  (one line). The converse is FALSE for countable families (EffectSpace.lean:858 with the 3/5
  rotation pair; probe P1 F9). No equivalence is displayed.
-/
import OIBridge.TransitiveBody
import OIBridge.EffectSpace

namespace OIBridge
namespace ACSketch

open Set KInfFoundations OrbitGeneration TransitiveBody InvariantInnerProduct EffectSpace
  CompositeDimension

variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-- DENSE-COVER: every boundary state is a limit of images of `x₀` under members of `G`.
The closure is taken in `V` only; no topology on the operation type `V ≃ᵃ[ℝ] V` is needed.
It is the closure-invariant analogue of `CoversBoundaryFrom` (OrbitGeneration.lean:83). -/
def DenseBoundaryOrbit (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) (x₀ : V) : Prop :=
  IsBoundaryState Ω x₀ ∧
    ∀ y, IsBoundaryState Ω y → y ∈ closure ((fun g : V ≃ᵃ[ℝ] V => g x₀) '' G)

/-- One direction only: exact transitivity gives the dense cover (`subset_closure`). -/
theorem denseBoundaryOrbit_of_transitive {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)} {x₀ : V}
    (hK : BoundaryTransitive Ω G) (hx₀ : IsBoundaryState Ω x₀) : DenseBoundaryOrbit Ω G x₀ :=
  ⟨hx₀, fun y hy => by
    obtain ⟨g, hg, rfl⟩ := hK x₀ y hx₀ hy
    exact subset_closure ⟨g, hg, rfl⟩⟩

variable {d : ℕ}

/-- `qnorm Ω` is continuous (a quadratic form in finitely many coordinates). -/
theorem continuous_qnorm (Ω : Set (Fin d → ℝ)) : Continuous (qnorm Ω) := by
  sorry -- `Continuous.dotProduct` / `Continuous.matrix_mulVec` style; finite sums of products

/-- **Constancy on the boundary from a dense orbit.** The level set of the continuous invariant
`v ↦ qnorm Ω (v - centroid Ω)` through `x₀` is closed and contains the orbit
(`qnorm_sub_centroid_apply`, TransitiveBody.lean:362), hence its closure. -/
theorem boundary_qnorm_const_of_dense {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)
    (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}
    (hG : PreservesBody Ω G) {x₀ : Fin d → ℝ} (hD : DenseBoundaryOrbit Ω G x₀) :
    ∀ y, IsBoundaryState Ω y →
      qnorm Ω (y - centroid Ω) = qnorm Ω (x₀ - centroid Ω) := by
  intro y hy
  have hcl : IsClosed {v : Fin d → ℝ | qnorm Ω (v - centroid Ω) = qnorm Ω (x₀ - centroid Ω)} :=
    isClosed_eq ((continuous_qnorm Ω).comp (continuous_id.sub continuous_const)) continuous_const
  have hsub : (fun g : (Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ) => g x₀) '' G ⊆
      {v | qnorm Ω (v - centroid Ω) = qnorm Ω (x₀ - centroid Ω)} := by
    rintro _ ⟨g, hg, rfl⟩
    exact qnorm_sub_centroid_apply hc hi hG hg x₀
  exact closure_minimal hsub hcl (hD.2 y hy)

/-- The centroid is interior. If it were a boundary state, constancy would force
`qnorm (x₀ - c) = qnorm (c - c) = 0`, so every boundary state would equal `c`
(`qnorm_pos`, TransitiveBody.lean:335), while the ray lemma (`exists_boundary_ray`) gives two
distinct boundary states along `±e`. Same skeleton as `centroid_mem_interior` (TB:427), with the
dense cover in place of the fixed-point argument. -/
theorem centroid_mem_interior_of_dense (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)
    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty)
    {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} (hG : PreservesBody Ω G) {x₀ : Fin d → ℝ}
    (hD : DenseBoundaryOrbit Ω G x₀) : centroid Ω ∈ interior Ω := by
  sorry

/-- **The ball from a dense orbit.** TRB-1's conclusion with `DenseBoundaryOrbit` in place of
`BoundaryTransitive`. The rest of the proof of `eq_qBall_of_boundaryTransitive` (TB:457) uses only
the constancy `hR` and the interior centroid, so it transfers verbatim. -/
theorem eq_qBall_of_denseBoundaryOrbit (hd : 0 < d) {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)
    (hconv : Convex ℝ Ω) (hi : (interior Ω).Nonempty)
    {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))} (hG : PreservesBody Ω G) {x₀ : Fin d → ℝ}
    (hD : DenseBoundaryOrbit Ω G x₀) : ∃ R : ℝ, 0 < R ∧ Ω = qBall Ω R := by
  sorry

/-- **The cone from a dense seed orbit.** EFF-1's `maxConeOf_avail_eq` with the dense cover of
the seed's certain state in place of `BoundaryTransitive`. (⊇) is EFF-1's own argument from
`hE`. (⊆): each available transport `seedTransport r g` is `sharpEff (g u)`
(`seedTransport_mem_sharpFamily`, EffectSpace.lean:362); `(b, b') ↦ prodEffVal (sharpEff b)
(sharpEff b') ω` is continuous (bilinear in `sharpVec`, affine in `b`); nonnegativity on a dense
set of pairs of the sphere passes to every pair; then `maxConeOf_sharpFamily` (:549). -/
theorem maxConeOf_avail_eq_of_dense (hd : 0 < d) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}
    {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}
    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)
    {u : Fin d → ℝ} (hu : u ∈ eball d) (hu1 : r u = 1)
    (hD : DenseBoundaryOrbit (eball d) G u)
    (hV4 : SeedOrbitAvailable G r avail) (hE : EffectsOn (eball d) avail) :
    maxConeOf avail = maxCone (eball d) := by
  sorry

/-- Countercontrols that must fail the hypotheses (recorded; exact in probes P1, P4):
  * `G` = the free group of the 3/5 rotation pair on `eball 3`: `DenseBoundaryOrbit` holds
    (written: closure is SO(3)), `BoundaryTransitive` fails (EffectSpace.lean:858; P1 F9:
    `-e_z` is never reached, torsion-freeness).
  * the cylinder `B² × [-1,1]` with `R_z(θ)` and `z ↦ -z`: orbits are dense only in circles;
    the invariant form is `a(x²+y²) + b z²`, not constant on the boundary (P4 C3).
  * the cube with the octahedral rotations: the invariant form is pinned (P4 C2b) but orbits are
    finite; neither hypothesis holds and the cube is not a ball.
  * `conv (G • e_z)` for the 3/5 group (not closed): preserved by every raw member and not by the
    closure element `R_x(π)` (it would need `-e_z`, an extreme point of the ball absent from the
    countable orbit; P1 F9). Compactness of `Ω` is load-bearing for closure-invariance. -/
theorem countercontrols_recorded : True := trivial

end ACSketch
end OIBridge
