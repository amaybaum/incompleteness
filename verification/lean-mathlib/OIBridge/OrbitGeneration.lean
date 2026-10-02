/-
  OIBridge/OrbitGeneration.lean — DRAFT (Thread L, research only; not in the repository and not
  kernel-checked). The reduced orbit-generation theorem for one sharp readout, in the
  field-neutral vocabulary of `KInfFoundations`.

  The three inputs are named hypotheses, stated as propositions and never proved here:
    * P1, `SharpSeed Ω r`: the seed `r` is an effect on `Ω` taking the value one at a state and
      the value zero at a state;
    * V4′, `SeedOrbitAvailable G r avail`: every transport `r ∘ g⁻¹`, `g ∈ G`, is available;
    * K∞-R, `BoundaryTransitive Ω G`: the members of `G` carry any boundary state of `Ω` to any
      other;
  together with the premise on `G` that every statement below needs and that none of the three
  names: `PreservesBody Ω G`, each member and its inverse map `Ω` into `Ω`. `G` is a set of
  affine automorphisms of `V`; no group structure, linearity or centrality is used.

  Proved here (when kernel-checked).
    §B  transport of effects, proper effects and sharp seeds along a member of `G`;
        a perfectly distinguishing pair on `Fin 2` yields a sharp seed;
    §B′ the flow members and `J` of an elementary drive satisfy `PreservesBody`;
    §C  the general-body form: a proper seed, `PreservesBody`, the covering of the boundary from
        the seed's certain state (`CoversBoundaryFrom`) and V4′ give (SEC); boundary
        transitivity and a sharp seed give the covering;
    §D  on `ball3`: an effect with the values one and zero is `ballEffect u` with `|u|² = 1`,
        so the normalization `(1 + u · x)/2` is forced by sharpness;
    §E  the reduced orbit-generation theorem
          PreservesBody + P1 + K∞-R  ⟹  {r ∘ g⁻¹ : g ∈ G} = {ballEffect b : |b|² = 1},
        V4′ adds only that this family is available; (SEC) and `KInf1` on the ball follow;
    §F  the family is exactly the hypothesis of `NativeGateBall.lorentz_of_effects` at `p = 3`;
    §G  controls: the hypotheses are jointly satisfiable (all affine automorphisms of the ball,
        through Householder reflections); without K∞-R the rotation flow of `ball3Drive` gives
        one effect only; without the zero value of P1 the orbit misses the family entirely
        while (SEC) still holds; the sup-norm sphere is not the index set of the family.

  Kernel check (after landing):  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.KInfFoundations
import OIBridge.NativeGateBall

namespace OIBridge
namespace OrbitGeneration

open Set KInfFoundations

variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-! ### §A — transport and the named hypotheses -/

/-- Transport of an affine functional along an affine automorphism: `e ↦ e ∘ g⁻¹`. -/
noncomputable def seedTransport (e : V →ᵃ[ℝ] ℝ) (g : V ≃ᵃ[ℝ] V) : V →ᵃ[ℝ] ℝ :=
  e.comp g.symm.toAffineMap

theorem seedTransport_apply (e : V →ᵃ[ℝ] ℝ) (g : V ≃ᵃ[ℝ] V) (x : V) :
    seedTransport e g x = e (g.symm x) := rfl

theorem seedTransport_apply_apply (e : V →ᵃ[ℝ] ℝ) (g : V ≃ᵃ[ℝ] V) (x : V) :
    seedTransport e g (g x) = e x := by
  rw [seedTransport_apply, AffineEquiv.symm_apply_apply]

/-- The seed orbit `{r ∘ g⁻¹ : g ∈ G}`. -/
def seedOrbit (G : Set (V ≃ᵃ[ℝ] V)) (r : V →ᵃ[ℝ] ℝ) : Set (V →ᵃ[ℝ] ℝ) :=
  {f | ∃ g ∈ G, f = seedTransport r g}

/-- **P1, the sharp seed**: an effect on `Ω` with the value one at a state and the value zero at a
state. -/
def SharpSeed (Ω : Set V) (r : V →ᵃ[ℝ] ℝ) : Prop :=
  IsEffectOn Ω r ∧ (∃ x ∈ Ω, r x = 1) ∧ (∃ y ∈ Ω, r y = 0)

/-- Every member of `G` is an automorphism of `Ω`: it and its inverse map `Ω` into `Ω`. -/
def PreservesBody (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop :=
  ∀ g ∈ G, ∀ x ∈ Ω, g x ∈ Ω ∧ g.symm x ∈ Ω

/-- **V4′, seed-orbit availability**: every transport of the seed along a member of `G` is
available. -/
def SeedOrbitAvailable (G : Set (V ≃ᵃ[ℝ] V)) (r : V →ᵃ[ℝ] ℝ) (avail : Set (V →ᵃ[ℝ] ℝ)) :
    Prop :=
  ∀ g ∈ G, seedTransport r g ∈ avail

/-- **K∞-R, boundary transitivity**: a member of `G` carries any boundary state to any other. -/
def BoundaryTransitive (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop :=
  ∀ x y, IsBoundaryState Ω x → IsBoundaryState Ω y → ∃ g ∈ G, g x = y

/-- COVER: every boundary state is the image of `x₀` under a member of `G`. -/
def CoversBoundaryFrom (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) (x₀ : V) : Prop :=
  ∀ y, IsBoundaryState Ω y → ∃ g ∈ G, g x₀ = y

/-- The pairing of an affine functional `e` with the homogeneous vector `(x0, v)`:
`x0 · e 0 + e.linear v`, written through the values of `e`. -/
def conePair (e : V →ᵃ[ℝ] ℝ) (x0 : ℝ) (v : V) : ℝ :=
  x0 * e 0 + (e v - e 0)

/-! ### §B — transport of effects and of sharp seeds -/

/-- **H1.** Transport along a map whose inverse preserves `Ω` keeps an effect an effect. -/
theorem isEffectOn_seedTransport {Ω : Set V} {e : V →ᵃ[ℝ] ℝ} {g : V ≃ᵃ[ℝ] V}
    (he : IsEffectOn Ω e) (hg : ∀ x ∈ Ω, g.symm x ∈ Ω) : IsEffectOn Ω (seedTransport e g) := by
  intro x hx
  rw [seedTransport_apply]
  exact he _ (hg x hx)

/-- Transport along a map preserving `Ω` keeps a proper effect proper. -/
theorem isProperOn_seedTransport {Ω : Set V} {e : V →ᵃ[ℝ] ℝ} {g : V ≃ᵃ[ℝ] V}
    (hp : IsProperOn Ω e) (hg : ∀ x ∈ Ω, g x ∈ Ω) : IsProperOn Ω (seedTransport e g) := by
  obtain ⟨y, hy, hlt⟩ := hp
  exact ⟨g y, hg y hy, by rw [seedTransport_apply_apply]; exact hlt⟩

/-- Transport along an automorphism of `Ω` keeps a sharp seed sharp. -/
theorem sharpSeed_seedTransport {Ω : Set V} {r : V →ᵃ[ℝ] ℝ} {g : V ≃ᵃ[ℝ] V}
    (hr : SharpSeed Ω r) (hg : ∀ x ∈ Ω, g x ∈ Ω ∧ g.symm x ∈ Ω) :
    SharpSeed Ω (seedTransport r g) := by
  obtain ⟨he, ⟨x, hx, h1⟩, ⟨y, hy, h0⟩⟩ := hr
  refine ⟨isEffectOn_seedTransport he (fun z hz => (hg z hz).2), ⟨g x, (hg x hx).1, ?_⟩,
    ⟨g y, (hg y hy).1, ?_⟩⟩
  · rw [seedTransport_apply_apply, h1]
  · rw [seedTransport_apply_apply, h0]

/-- A sharp seed is proper. -/
theorem sharpSeed_isProperOn {Ω : Set V} {r : V →ᵃ[ℝ] ℝ} (hr : SharpSeed Ω r) :
    IsProperOn Ω r := by
  obtain ⟨-, -, ⟨y, hy, h0⟩⟩ := hr
  exact ⟨y, hy, by rw [h0]; norm_num⟩

/-- The state at which a sharp seed is certain is a boundary state (L3). -/
theorem sharpSeed_certain_isBoundaryState {Ω : Set V} {r : V →ᵃ[ℝ] ℝ} (hr : SharpSeed Ω r)
    {x : V} (hx : x ∈ Ω) (h1 : r x = 1) : IsBoundaryState Ω x :=
  isBoundaryState_of_certain_proper hr.1 (sharpSeed_isProperOn hr) hx h1

/-- P1 in the vocabulary of `PerfectlyDistinguishable`: the first effect of a perfectly
distinguishing pair is a sharp seed. -/
theorem sharpSeed_of_perfectlyDistinguishable {Ω : Set V} {x : Fin 2 → V}
    {e : Fin 2 → V →ᵃ[ℝ] ℝ} (h : PerfectlyDistinguishable Ω x e) : SharpSeed Ω (e 0) := by
  obtain ⟨hx, he, hsum, hdiag⟩ := h
  refine ⟨he 0, ⟨x 0, hx 0, hdiag 0⟩, ⟨x 1, hx 1, ?_⟩⟩
  have h := hsum (x 1) (hx 1)
  rw [Fin.sum_univ_two, hdiag 1] at h
  linarith

/-- V4′ places the whole seed orbit in the available family. -/
theorem seedOrbit_subset {G : Set (V ≃ᵃ[ℝ] V)} {r : V →ᵃ[ℝ] ℝ} {avail : Set (V →ᵃ[ℝ] ℝ)}
    (hV4 : SeedOrbitAvailable G r avail) : seedOrbit G r ⊆ avail := by
  rintro f ⟨g, hg, rfl⟩
  exact hV4 g hg

/-- The seed orbit is available relative to itself. -/
theorem seedOrbitAvailable_self (G : Set (V ≃ᵃ[ℝ] V)) (r : V →ᵃ[ℝ] ℝ) :
    SeedOrbitAvailable G r (seedOrbit G r) :=
  fun g hg => ⟨g, hg, rfl⟩

/-! ### §B′ — `PreservesBody` for the generators of an elementary drive -/

theorem drive_flow_symm_apply {Ω : Set V} (D : ElementaryDrivability Ω) (t : ℝ) (x : V) :
    (D.flow t).symm x = D.flow (-t) x := by
  have h : D.flow t (D.flow (-t) x) = x := by
    have h1 := congrArg (fun f : V ≃ᵃ[ℝ] V => f x) (D.flow_add t (-t))
    simp only [AffineEquiv.trans_apply, add_neg_cancel, D.flow_zero,
      AffineEquiv.refl_apply] at h1
    exact h1.symm
  calc (D.flow t).symm x = (D.flow t).symm (D.flow t (D.flow (-t) x)) := by rw [h]
    _ = D.flow (-t) x := AffineEquiv.symm_apply_apply _ _

/-- The flow members and `J` of an elementary drive are automorphisms of `Ω`. -/
theorem preservesBody_drive {Ω : Set V} (D : ElementaryDrivability Ω) :
    PreservesBody Ω (Set.range D.flow ∪ {D.J}) := by
  rintro g (⟨t, rfl⟩ | hg) x hx
  · exact ⟨D.flow_preserves t x hx,
      by rw [drive_flow_symm_apply]; exact D.flow_preserves (-t) x hx⟩
  · rw [Set.mem_singleton_iff] at hg
    subst hg
    exact ⟨D.J_preserves x hx, D.J_symm_preserves x hx⟩

/-! ### §C — the general body: (SEC) from a covering orbit -/

/-- **H2, general body.** A proper effect certain at `x₀`, transported along automorphisms of `Ω`
whose images of `x₀` cover the boundary, with every transport available, gives (SEC). -/
theorem supportingEffectComplete_of_cover {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)}
    {r : V →ᵃ[ℝ] ℝ} {avail : Set (V →ᵃ[ℝ] ℝ)} {x₀ : V}
    (hG : PreservesBody Ω G) (he : IsEffectOn Ω r) (hp : IsProperOn Ω r) (hx₀ : r x₀ = 1)
    (hcov : CoversBoundaryFrom Ω G x₀) (hV4 : SeedOrbitAvailable G r avail) :
    SupportingEffectComplete Ω avail := by
  intro y hy
  obtain ⟨g, hg, rfl⟩ := hcov y hy
  exact ⟨seedTransport r g, hV4 g hg,
    isEffectOn_seedTransport he (fun z hz => (hG g hg z hz).2),
    isProperOn_seedTransport hp (fun z hz => (hG g hg z hz).1),
    by rw [seedTransport_apply_apply, hx₀]⟩

/-- Boundary transitivity gives the covering from any boundary state. -/
theorem coversBoundaryFrom_of_transitive {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)} {x₀ : V}
    (hK : BoundaryTransitive Ω G) (hx₀ : IsBoundaryState Ω x₀) : CoversBoundaryFrom Ω G x₀ :=
  fun y hy => hK x₀ y hx₀ hy

/-- P1 + K∞-R + V4′ + `PreservesBody` give (SEC) on any body. -/
theorem supportingEffectComplete_of_sharp_transitive {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)}
    {r : V →ᵃ[ℝ] ℝ} {avail : Set (V →ᵃ[ℝ] ℝ)} (hG : PreservesBody Ω G)
    (hP1 : SharpSeed Ω r) (hK : BoundaryTransitive Ω G)
    (hV4 : SeedOrbitAvailable G r avail) : SupportingEffectComplete Ω avail := by
  have hp := sharpSeed_isProperOn hP1
  obtain ⟨he, ⟨x, hx, h1⟩, -⟩ := hP1
  exact supportingEffectComplete_of_cover hG he hp h1
    (coversBoundaryFrom_of_transitive hK (isBoundaryState_of_certain_proper he hp hx h1)) hV4

/-! ### §D — the ball: sharpness forces the directional normalization -/

/-- The directional family `{v ↦ (1 + b · v)/2 : |b|² = 1}`, indexed by the quadratic form that
defines `ball3` (not by the sup-norm sphere of `Fin 3 → ℝ`). -/
def directionalFamily : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ) :=
  {e | ∃ b : Fin 3 → ℝ, b 0 ^ 2 + b 1 ^ 2 + b 2 ^ 2 = 1 ∧ e = ballEffect b}

theorem neg_mem_ball3 {v : Fin 3 → ℝ} (hv : v ∈ ball3) : -v ∈ ball3 := by
  rw [mem_ball3] at hv ⊢
  have e : ∀ x : ℝ, (-x) ^ 2 = x ^ 2 := fun x => by ring
  rw [Pi.neg_apply, Pi.neg_apply, Pi.neg_apply, e, e, e]
  exact hv

theorem ballEffect_self {b : Fin 3 → ℝ} (hb : b 0 ^ 2 + b 1 ^ 2 + b 2 ^ 2 = 1) :
    ballEffect b b = 1 := by
  rw [ballEffect_apply]
  linear_combination hb / 2

theorem ballEffect_neg_self {b : Fin 3 → ℝ} (hb : b 0 ^ 2 + b 1 ^ 2 + b 2 ^ 2 = 1) :
    ballEffect b (-b) = 0 := by
  rw [ballEffect_apply, Pi.neg_apply, Pi.neg_apply, Pi.neg_apply]
  linear_combination (-1 / 2 : ℝ) * hb

theorem ballEffect_isEffectOn {b : Fin 3 → ℝ} (hb : b 0 ^ 2 + b 1 ^ 2 + b 2 ^ 2 = 1) :
    IsEffectOn ball3 (ballEffect b) := by
  intro v hv
  rw [mem_ball3] at hv
  rw [ballEffect_apply]
  constructor <;> nlinarith [sq_nonneg (b 0 - v 0), sq_nonneg (b 1 - v 1),
    sq_nonneg (b 2 - v 2), sq_nonneg (b 0 + v 0), sq_nonneg (b 1 + v 1), sq_nonneg (b 2 + v 2)]

/-- Every member of the directional family is a sharp seed on the ball. -/
theorem ballEffect_sharp {b : Fin 3 → ℝ} (hb : b 0 ^ 2 + b 1 ^ 2 + b 2 ^ 2 = 1) :
    SharpSeed ball3 (ballEffect b) :=
  ⟨ballEffect_isEffectOn hb, ⟨b, (mem_ball3 b).mpr hb.le, ballEffect_self hb⟩,
    ⟨-b, neg_mem_ball3 ((mem_ball3 b).mpr hb.le), ballEffect_neg_self hb⟩⟩

/-- A point of the unit sphere is a boundary state of the ball. -/
theorem isBoundaryState_ball3_of_sphere {b : Fin 3 → ℝ}
    (hb : b 0 ^ 2 + b 1 ^ 2 + b 2 ^ 2 = 1) : IsBoundaryState ball3 b :=
  sharpSeed_certain_isBoundaryState (ballEffect_sharp hb) ((mem_ball3 b).mpr hb.le)
    (ballEffect_self hb)

/-- A boundary state of the ball lies on the unit sphere (the argument of
`supportingEffectComplete_ball3`). -/
theorem sphere_of_isBoundaryState_ball3 {x : Fin 3 → ℝ} (h : IsBoundaryState ball3 x) :
    x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2 = 1 := by
  obtain ⟨hx, y, hy, hout⟩ := h
  rw [mem_ball3] at hx hy
  by_contra hne
  have hlt := lt_of_le_of_ne hx hne
  apply hout ((1 - (x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2)) / 16) (by linarith)
  rw [mem_ball3]
  simp only [Pi.add_apply, Pi.smul_apply, Pi.sub_apply, smul_eq_mul]
  exact ball3_extend hx hy (by linarith) (by ring)

/-- An affine functional on `ℝ³` in coordinates. -/
theorem affine3_apply (r : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ) (v : Fin 3 → ℝ) :
    r v = r 0 + v 0 * r.linear ![1, 0, 0] + v 1 * r.linear ![0, 1, 0] +
      v 2 * r.linear ![0, 0, 1] := by
  have hv : v = v 0 • (![1, 0, 0] : Fin 3 → ℝ) + v 1 • ![0, 1, 0] + v 2 • ![0, 0, 1] := by
    apply vec3_ext <;> simp
  have hl : r.linear v = v 0 * r.linear ![1, 0, 0] + v 1 * r.linear ![0, 1, 0] +
      v 2 * r.linear ![0, 0, 1] := by
    have h := congrArg r.linear hv
    rw [map_add, map_add, map_smul, map_smul, map_smul, smul_eq_mul, smul_eq_mul,
      smul_eq_mul] at h
    exact h
  have hd : r v = r.linear v + r 0 := by
    have h := congrFun (AffineMap.decomp r) v
    rw [Pi.add_apply] at h
    exact h
  rw [hd, hl]
  ring

/-- **Sharpness forces the normalization.** On the ball, an effect with the value one at `u` and
the value zero at some state is `ballEffect u`, and `u` lies on the unit sphere. -/
theorem ball3_sharp_eq {r : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ} (he : IsEffectOn ball3 r) {u w : Fin 3 → ℝ}
    (hu : u ∈ ball3) (hw : w ∈ ball3) (h1 : r u = 1) (h0 : r w = 0) :
    u 0 ^ 2 + u 1 ^ 2 + u 2 ^ 2 = 1 ∧ r = ballEffect u := by
  obtain ⟨c, a0, a1, a2, hr⟩ : ∃ c a0 a1 a2 : ℝ, ∀ v : Fin 3 → ℝ,
      r v = c + v 0 * a0 + v 1 * a1 + v 2 * a2 := ⟨_, _, _, _, affine3_apply r⟩
  have F1 : c + u 0 * a0 + u 1 * a1 + u 2 * a2 = 1 := (hr u).symm.trans h1
  have F3 : c + w 0 * a0 + w 1 * a1 + w 2 * a2 = 0 := (hr w).symm.trans h0
  have F2 : 0 ≤ c + -u 0 * a0 + -u 1 * a1 + -u 2 * a2 := by
    have h := (he (-u) (neg_mem_ball3 hu)).1
    rw [hr, Pi.neg_apply, Pi.neg_apply, Pi.neg_apply] at h
    exact h
  have F4 : c + -w 0 * a0 + -w 1 * a1 + -w 2 * a2 ≤ 1 := by
    have h := (he (-w) (neg_mem_ball3 hw)).2
    rw [hr, Pi.neg_apply, Pi.neg_apply, Pi.neg_apply] at h
    exact h
  have hc : c = 1 / 2 := by linarith
  -- the test point `p = 4 k a`, `k = 1 / (1 + 4 |a|²)`, which lies in the ball
  obtain ⟨A, hA⟩ : ∃ A : ℝ, A = a0 ^ 2 + a1 ^ 2 + a2 ^ 2 := ⟨_, rfl⟩
  have hA0 : 0 ≤ A := by rw [hA]; positivity
  have hD : (0 : ℝ) < 1 + 4 * A := by linarith
  obtain ⟨k, hk⟩ : ∃ k : ℝ, (1 + 4 * A) * k = 1 := ⟨_, mul_inv_cancel₀ hD.ne'⟩
  have hp : (![4 * a0 * k, 4 * a1 * k, 4 * a2 * k] : Fin 3 → ℝ) ∈ ball3 := by
    show (4 * a0 * k) ^ 2 + (4 * a1 * k) ^ 2 + (4 * a2 * k) ^ 2 ≤ 1
    have h16 : 16 * A ≤ (1 + 4 * A) ^ 2 := by nlinarith [sq_nonneg (1 - 4 * A)]
    have e1 : (4 * a0 * k) ^ 2 + (4 * a1 * k) ^ 2 + (4 * a2 * k) ^ 2 = 16 * A * k ^ 2 := by
      rw [hA]; ring
    have e2 : (1 + 4 * A) ^ 2 * k ^ 2 = 1 := by rw [← mul_pow, hk, one_pow]
    rw [e1]
    nlinarith [mul_le_mul_of_nonneg_right h16 (sq_nonneg k)]
  have F5 : c + 4 * a0 * k * a0 + 4 * a1 * k * a1 + 4 * a2 * k * a2 ≤ 1 := by
    have h := (he _ hp).2
    rw [hr] at h
    exact h
  have hA14 : A ≤ 1 / 4 := by
    have h4 : 4 * k * A ≤ 1 / 2 := by
      have e : c + 4 * a0 * k * a0 + 4 * a1 * k * a1 + 4 * a2 * k * a2 = c + 4 * k * A := by
        rw [hA]; ring
      linarith
    have h5 : 4 * k * A * (1 + 4 * A) = 4 * A := by linear_combination (4 * A) * hk
    nlinarith [mul_le_mul_of_nonneg_right h4 hD.le]
  have hU : u 0 ^ 2 + u 1 ^ 2 + u 2 ^ 2 ≤ 1 := (mem_ball3 u).mp hu
  have hdot : u 0 * a0 + u 1 * a1 + u 2 * a2 = 1 / 2 := by linarith
  have hS : (2 * a0 - u 0) ^ 2 + (2 * a1 - u 1) ^ 2 + (2 * a2 - u 2) ^ 2 =
      4 * A - 4 * (u 0 * a0 + u 1 * a1 + u 2 * a2) + (u 0 ^ 2 + u 1 ^ 2 + u 2 ^ 2) := by
    rw [hA]; ring
  have hS0 : (2 * a0 - u 0) ^ 2 + (2 * a1 - u 1) ^ 2 + (2 * a2 - u 2) ^ 2 ≤ 0 := by
    rw [hS, hdot]; linarith
  have q0 := sq_nonneg (2 * a0 - u 0)
  have q1 := sq_nonneg (2 * a1 - u 1)
  have q2 := sq_nonneg (2 * a2 - u 2)
  have z0 : 2 * a0 - u 0 = 0 := (pow_eq_zero_iff two_ne_zero).mp (by linarith)
  have z1 : 2 * a1 - u 1 = 0 := (pow_eq_zero_iff two_ne_zero).mp (by linarith)
  have z2 : 2 * a2 - u 2 = 0 := (pow_eq_zero_iff two_ne_zero).mp (by linarith)
  refine ⟨by linarith, ?_⟩
  apply AffineMap.ext
  intro v
  rw [hr v, ballEffect_apply, hc]
  linear_combination (v 0 / 2) * z0 + (v 1 / 2) * z1 + (v 2 / 2) * z2

/-- Every sharp seed on the ball belongs to the directional family. -/
theorem sharpSeed_ball3_mem_directional {f : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ} (hf : SharpSeed ball3 f) :
    f ∈ directionalFamily := by
  obtain ⟨he, ⟨u, hu, h1⟩, ⟨w, hw, h0⟩⟩ := hf
  obtain ⟨hs, heq⟩ := ball3_sharp_eq he hu hw h1 h0
  exact ⟨u, hs, heq⟩

/-! ### §E — the reduced orbit-generation theorem -/

/-- **The reduced orbit-generation theorem.** Under `PreservesBody`, P1 and K∞-R, the transports
of the seed are exactly the directional effects `(1 + b · x)/2`, `|b|² = 1`. -/
theorem seedOrbit_ball3_eq {G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))}
    {r : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ} (hG : PreservesBody ball3 G) (hP1 : SharpSeed ball3 r)
    (hK : BoundaryTransitive ball3 G) : seedOrbit G r = directionalFamily := by
  ext f
  constructor
  · rintro ⟨g, hg, rfl⟩
    exact sharpSeed_ball3_mem_directional (sharpSeed_seedTransport hP1 (hG g hg))
  · rintro ⟨b, hb, rfl⟩
    obtain ⟨he, ⟨u, hu, h1⟩, ⟨w, hw, h0⟩⟩ := hP1
    obtain ⟨hsu, -⟩ := ball3_sharp_eq he hu hw h1 h0
    obtain ⟨g, hg, hgu⟩ := hK u b (isBoundaryState_ball3_of_sphere hsu)
      (isBoundaryState_ball3_of_sphere hb)
    refine ⟨g, hg, ?_⟩
    have hT : IsEffectOn ball3 (seedTransport r g) :=
      isEffectOn_seedTransport he (fun z hz => (hG g hg z hz).2)
    obtain ⟨-, hTeq⟩ := ball3_sharp_eq hT (hG g hg u hu).1 (hG g hg w hw).1
      (by rw [seedTransport_apply_apply, h1]) (by rw [seedTransport_apply_apply, h0])
    rw [hTeq, hgu]

/-- With V4′, every directional effect is available, in the exact form `lorentz_of_effects`
quantifies over: `b : Fin 3 → ℝ` with `∑ j, b j ^ 2 = 1`. -/
theorem ballEffect_mem_avail {G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))}
    {r : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ} {avail : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ)}
    (hG : PreservesBody ball3 G) (hP1 : SharpSeed ball3 r) (hK : BoundaryTransitive ball3 G)
    (hV4 : SeedOrbitAvailable G r avail) :
    ∀ b : Fin 3 → ℝ, (∑ j, b j ^ 2) = 1 → ballEffect b ∈ avail := by
  intro b hb
  rw [Fin.sum_univ_three] at hb
  have hmem : ballEffect b ∈ seedOrbit G r := by
    rw [seedOrbit_ball3_eq hG hP1 hK]
    exact ⟨b, hb, rfl⟩
  exact seedOrbit_subset hV4 hmem

/-- (SEC) on the ball from P1, V4′, K∞-R and `PreservesBody`. -/
theorem supportingEffectComplete_ball3_of_orbit {G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))}
    {r : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ} {avail : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ)}
    (hG : PreservesBody ball3 G) (hP1 : SharpSeed ball3 r) (hK : BoundaryTransitive ball3 G)
    (hV4 : SeedOrbitAvailable G r avail) : SupportingEffectComplete ball3 avail :=
  supportingEffectComplete_of_sharp_transitive hG hP1 hK hV4

/-- K∞-1 for the ball, relative to any family containing the seed orbit. -/
theorem kInf1_ball3_of_orbit {G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))}
    {r : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ} {avail : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ)}
    (hG : PreservesBody ball3 G) (hP1 : SharpSeed ball3 r) (hK : BoundaryTransitive ball3 G)
    (hV4 : SeedOrbitAvailable G r avail) : KInf1 ball3 avail :=
  fun _ _ _ => supportingEffectComplete_ball3_of_orbit hG hP1 hK hV4

/-! ### §F — the family is the hypothesis of `lorentz_of_effects` -/

theorem conePair_ballEffect (b v : Fin 3 → ℝ) (x0 : ℝ) :
    conePair (ballEffect b) x0 v = (x0 + (b 0 * v 0 + b 1 * v 1 + b 2 * v 2)) / 2 := by
  unfold conePair
  rw [ballEffect_apply, ballEffect_apply]
  simp only [Pi.zero_apply, mul_zero, add_zero]
  ring

/-- **The bridge.** A homogeneous vector `(x0, v)` on which every transport of the seed pairs
nonnegatively lies in the Lorentz cone, through `NativeGateBall.lorentz_of_effects` at `p = 3`. -/
theorem lorentz_of_seedOrbit {G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))}
    {r : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ} (hG : PreservesBody ball3 G) (hP1 : SharpSeed ball3 r)
    (hK : BoundaryTransitive ball3 G) (x0 : ℝ) (v : Fin 3 → ℝ)
    (h : ∀ e ∈ seedOrbit G r, 0 ≤ conePair e x0 v) :
    0 ≤ x0 ∧ (∑ j, v j ^ 2) ≤ x0 ^ 2 := by
  refine NativeGateBall.lorentz_of_effects 3 (by norm_num) x0 v (fun b hb => ?_)
  rw [Fin.sum_univ_three] at hb
  rw [Fin.sum_univ_three]
  have hmem : ballEffect b ∈ seedOrbit G r := by
    rw [seedOrbit_ball3_eq hG hP1 hK]
    exact ⟨b, hb, rfl⟩
  have h2 := h _ hmem
  rw [conePair_ballEffect] at h2
  linarith

/-- The bridge stated on the available family, through V4′. -/
theorem lorentz_of_available {G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))}
    {r : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ} {avail : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ)}
    (hG : PreservesBody ball3 G) (hP1 : SharpSeed ball3 r) (hK : BoundaryTransitive ball3 G)
    (hV4 : SeedOrbitAvailable G r avail) (x0 : ℝ) (v : Fin 3 → ℝ)
    (h : ∀ e ∈ avail, 0 ≤ conePair e x0 v) :
    0 ≤ x0 ∧ (∑ j, v j ^ 2) ≤ x0 ^ 2 :=
  lorentz_of_seedOrbit hG hP1 hK x0 v (fun e he => h e (seedOrbit_subset hV4 he))

/-! ### §G — controls -/

theorem ez_sphere :
    (![0, 0, 1] : Fin 3 → ℝ) 0 ^ 2 + (![0, 0, 1] : Fin 3 → ℝ) 1 ^ 2 +
      (![0, 0, 1] : Fin 3 → ℝ) 2 ^ 2 = 1 := by
  show (0 : ℝ) ^ 2 + 0 ^ 2 + 1 ^ 2 = 1
  norm_num

/-! #### Positive control: all affine automorphisms of the ball -/

/-- The Householder reflection along `d`, with `k` standing for `1 / |d|²`. -/
noncomputable def hhFun (d : Fin 3 → ℝ) (k : ℝ) (v : Fin 3 → ℝ) : Fin 3 → ℝ :=
  fun i => v i - 2 * k * (d 0 * v 0 + d 1 * v 1 + d 2 * v 2) * d i

theorem hhFun_dot (d : Fin 3 → ℝ) (k : ℝ) (hk : (d 0 ^ 2 + d 1 ^ 2 + d 2 ^ 2) * k = 1)
    (v : Fin 3 → ℝ) :
    d 0 * hhFun d k v 0 + d 1 * hhFun d k v 1 + d 2 * hhFun d k v 2 =
      -(d 0 * v 0 + d 1 * v 1 + d 2 * v 2) := by
  simp only [hhFun]
  linear_combination (-2 * (d 0 * v 0 + d 1 * v 1 + d 2 * v 2)) * hk

theorem hhFun_hhFun (d : Fin 3 → ℝ) (k : ℝ) (hk : (d 0 ^ 2 + d 1 ^ 2 + d 2 ^ 2) * k = 1)
    (v : Fin 3 → ℝ) : hhFun d k (hhFun d k v) = v := by
  have key := hhFun_dot d k hk v
  funext i
  show hhFun d k v i - 2 * k * (d 0 * hhFun d k v 0 + d 1 * hhFun d k v 1 +
    d 2 * hhFun d k v 2) * d i = v i
  rw [key]
  simp only [hhFun]
  ring

theorem hhFun_normSq (d : Fin 3 → ℝ) (k : ℝ) (hk : (d 0 ^ 2 + d 1 ^ 2 + d 2 ^ 2) * k = 1)
    (v : Fin 3 → ℝ) :
    hhFun d k v 0 ^ 2 + hhFun d k v 1 ^ 2 + hhFun d k v 2 ^ 2 = v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2 := by
  simp only [hhFun]
  linear_combination (4 * k * (d 0 * v 0 + d 1 * v 1 + d 2 * v 2) ^ 2) * hk

/-- The reflection along `u − w` carries the unit vector `u` to the unit vector `w`. -/
theorem hhFun_swap (u w : Fin 3 → ℝ) (k : ℝ) (hu : u 0 ^ 2 + u 1 ^ 2 + u 2 ^ 2 = 1)
    (hw : w 0 ^ 2 + w 1 ^ 2 + w 2 ^ 2 = 1)
    (hk : ((u 0 - w 0) ^ 2 + (u 1 - w 1) ^ 2 + (u 2 - w 2) ^ 2) * k = 1) :
    hhFun (fun i => u i - w i) k u = w := by
  funext i
  simp only [hhFun]
  linear_combination (-(u i - w i)) * hk + (-(u i - w i) * k) * hu + ((u i - w i) * k) * hw

noncomputable def hhLin (d : Fin 3 → ℝ) (k : ℝ) : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) where
  toFun := hhFun d k
  map_add' v w := by
    funext i
    simp only [hhFun, Pi.add_apply]
    ring
  map_smul' c v := by
    funext i
    simp only [hhFun, Pi.smul_apply, smul_eq_mul, RingHom.id_apply]
    ring

noncomputable def hhEquiv (d : Fin 3 → ℝ) (k : ℝ)
    (hk : (d 0 ^ 2 + d 1 ^ 2 + d 2 ^ 2) * k = 1) : (Fin 3 → ℝ) ≃ₗ[ℝ] (Fin 3 → ℝ) :=
  { hhLin d k with
    invFun := hhFun d k
    left_inv := fun v => by
      show hhFun d k (hhFun d k v) = v
      exact hhFun_hhFun d k hk v
    right_inv := fun v => by
      show hhFun d k (hhFun d k v) = v
      exact hhFun_hhFun d k hk v }

/-- The Householder reflection, as an affine automorphism of `ℝ³`. -/
noncomputable def hh3 (d : Fin 3 → ℝ) (k : ℝ) (hk : (d 0 ^ 2 + d 1 ^ 2 + d 2 ^ 2) * k = 1) :
    (Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ) :=
  (hhEquiv d k hk).toAffineEquiv

theorem hh3_apply (d : Fin 3 → ℝ) (k : ℝ) (hk : (d 0 ^ 2 + d 1 ^ 2 + d 2 ^ 2) * k = 1)
    (v : Fin 3 → ℝ) : hh3 d k hk v = hhFun d k v := rfl

theorem hh3_symm_apply (d : Fin 3 → ℝ) (k : ℝ) (hk : (d 0 ^ 2 + d 1 ^ 2 + d 2 ^ 2) * k = 1)
    (v : Fin 3 → ℝ) : (hh3 d k hk).symm v = hhFun d k v := by
  have h : hh3 d k hk (hh3 d k hk v) = v := by
    rw [hh3_apply, hh3_apply, hhFun_hhFun d k hk]
  calc (hh3 d k hk).symm v = (hh3 d k hk).symm (hh3 d k hk (hh3 d k hk v)) := by rw [h]
    _ = hh3 d k hk v := AffineEquiv.symm_apply_apply _ _
    _ = hhFun d k v := hh3_apply d k hk v

theorem hhFun_mem_ball3 (d : Fin 3 → ℝ) (k : ℝ) (hk : (d 0 ^ 2 + d 1 ^ 2 + d 2 ^ 2) * k = 1)
    {v : Fin 3 → ℝ} (hv : v ∈ ball3) : hhFun d k v ∈ ball3 := by
  rw [mem_ball3] at hv ⊢
  rw [hhFun_normSq d k hk v]
  exact hv

/-- All affine automorphisms of the ball. -/
def fullAut3 : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)) :=
  {g | ∀ x ∈ ball3, g x ∈ ball3 ∧ g.symm x ∈ ball3}

theorem preservesBody_fullAut3 : PreservesBody ball3 fullAut3 := fun _ hg => hg

theorem refl_mem_fullAut3 : AffineEquiv.refl ℝ (Fin 3 → ℝ) ∈ fullAut3 := fun x hx =>
  ⟨by rw [AffineEquiv.refl_apply]; exact hx,
    by rw [AffineEquiv.symm_refl, AffineEquiv.refl_apply]; exact hx⟩

theorem hh3_mem_fullAut3 (d : Fin 3 → ℝ) (k : ℝ) (hk : (d 0 ^ 2 + d 1 ^ 2 + d 2 ^ 2) * k = 1) :
    hh3 d k hk ∈ fullAut3 := fun x hx =>
  ⟨by rw [hh3_apply]; exact hhFun_mem_ball3 d k hk hx,
    by rw [hh3_symm_apply]; exact hhFun_mem_ball3 d k hk hx⟩

/-- **Positive control for K∞-R.** The affine automorphisms of the ball act transitively on its
boundary. -/
theorem boundaryTransitive_fullAut3 : BoundaryTransitive ball3 fullAut3 := by
  intro u w hu hw
  have hu1 := sphere_of_isBoundaryState_ball3 hu
  have hw1 := sphere_of_isBoundaryState_ball3 hw
  by_cases huw : u = w
  · exact ⟨AffineEquiv.refl ℝ _, refl_mem_fullAut3, by rw [AffineEquiv.refl_apply, huw]⟩
  · have hq : (u 0 - w 0) ^ 2 + (u 1 - w 1) ^ 2 + (u 2 - w 2) ^ 2 ≠ 0 := by
      intro h0
      apply huw
      have q0 := sq_nonneg (u 0 - w 0)
      have q1 := sq_nonneg (u 1 - w 1)
      have q2 := sq_nonneg (u 2 - w 2)
      have z0 : u 0 - w 0 = 0 := (pow_eq_zero_iff two_ne_zero).mp (by linarith)
      have z1 : u 1 - w 1 = 0 := (pow_eq_zero_iff two_ne_zero).mp (by linarith)
      have z2 : u 2 - w 2 = 0 := (pow_eq_zero_iff two_ne_zero).mp (by linarith)
      exact vec3_ext (by linarith) (by linarith) (by linarith)
    obtain ⟨k, hk⟩ : ∃ k : ℝ, ((u 0 - w 0) ^ 2 + (u 1 - w 1) ^ 2 + (u 2 - w 2) ^ 2) * k = 1 :=
      ⟨_, mul_inv_cancel₀ hq⟩
    refine ⟨hh3 (fun i => u i - w i) k hk, hh3_mem_fullAut3 (fun i => u i - w i) k hk, ?_⟩
    rw [hh3_apply]
    exact hhFun_swap u w k hu1 hw1 hk

/-- **The hypotheses are jointly satisfiable**: with all automorphisms of the ball and the seed
`(1 + z)/2`, the seed orbit is the directional family. -/
theorem seedOrbit_fullAut3 : seedOrbit fullAut3 (ballEffect ![0, 0, 1]) = directionalFamily :=
  seedOrbit_ball3_eq preservesBody_fullAut3 (ballEffect_sharp ez_sphere)
    boundaryTransitive_fullAut3

/-! #### Negative control N1: the rotation flow alone (K∞-R absent) -/

theorem rot3_symm_apply (t : ℝ) (x : Fin 3 → ℝ) : (rot3 t).symm x = rot3 (-t) x := by
  have h : rot3 t (rot3 (-t) x) = x := by
    rw [rot3_apply, rot3_apply, rotFun_add, add_neg_cancel, rotFun_zero]
  calc (rot3 t).symm x = (rot3 t).symm (rot3 t (rot3 (-t) x)) := by rw [h]
    _ = rot3 (-t) x := AffineEquiv.symm_apply_apply _ _

/-- The flow of `ball3Drive` consists of automorphisms of the ball. -/
theorem preservesBody_flow : PreservesBody ball3 (Set.range rot3) := by
  rintro _ ⟨t, rfl⟩ x hx
  exact ⟨rotFun_mem_ball3 t hx, by rw [rot3_symm_apply]; exact rotFun_mem_ball3 (-t) hx⟩

theorem seedTransport_rot3_ez (t : ℝ) :
    seedTransport (ballEffect ![0, 0, 1]) (rot3 t) = ballEffect ![0, 0, 1] := by
  apply AffineMap.ext
  intro v
  rw [seedTransport_apply, rot3_symm_apply, rot3_apply, ballEffect_apply, ballEffect_apply,
    (rotFun_apply (-t) v).2.2]
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons, Matrix.cons_val_two,
    Matrix.tail_cons]
  ring

/-- Along the flow alone, the orbit of the seed `(1 + z)/2` is that one effect. -/
theorem seedOrbit_flow :
    seedOrbit (Set.range rot3) (ballEffect ![0, 0, 1]) = {ballEffect ![0, 0, 1]} := by
  ext f
  constructor
  · rintro ⟨_, ⟨t, rfl⟩, rfl⟩
    exact seedTransport_rot3_ez t
  · intro hf
    rw [Set.mem_singleton_iff] at hf
    subst hf
    exact ⟨rot3 0, ⟨0, rfl⟩, (seedTransport_rot3_ez 0).symm⟩

theorem ballEffect_ex_ne_ez : ballEffect ![1, 0, 0] ≠ ballEffect ![0, 0, 1] := by
  intro h
  have h1 : ballEffect ![1, 0, 0] ![1, 0, 0] = ballEffect ![0, 0, 1] ![1, 0, 0] := by rw [h]
  rw [ballEffect_apply, ballEffect_apply] at h1
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons, Matrix.cons_val_two,
    Matrix.tail_cons] at h1
  norm_num at h1

/-- **N1.** With the flow alone the orbit is a proper subset of the directional family. -/
theorem not_seedOrbit_flow_eq :
    seedOrbit (Set.range rot3) (ballEffect ![0, 0, 1]) ≠ directionalFamily := by
  intro h
  have hmem : ballEffect ![1, 0, 0] ∈ seedOrbit (Set.range rot3) (ballEffect ![0, 0, 1]) := by
    rw [h]
    exact ⟨![1, 0, 0], by show (1 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2 = 1; norm_num, rfl⟩
  rw [seedOrbit_flow] at hmem
  exact ballEffect_ex_ne_ez hmem

/-- K∞-R is not implied by P1 and `PreservesBody`: the flow of `ball3Drive` satisfies both with
the seed `(1 + z)/2`, and is not boundary transitive. -/
theorem not_boundaryTransitive_flow : ¬ BoundaryTransitive ball3 (Set.range rot3) := fun hK =>
  not_seedOrbit_flow_eq (seedOrbit_ball3_eq preservesBody_flow (ballEffect_sharp ez_sphere) hK)

/-! #### Negative control N2: an unsharp seed (the zero value of P1 absent) -/

/-- The effect `v ↦ 3/4 + z/4`: certain at the north pole, proper, never zero on the ball. -/
noncomputable def unsharpSeed : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ :=
  AffineMap.const ℝ (Fin 3 → ℝ) (3 / 4 : ℝ) +
    ((1 / 4 : ℝ) • (LinearMap.proj 2 : (Fin 3 → ℝ) →ₗ[ℝ] ℝ)).toAffineMap

theorem unsharpSeed_apply (v : Fin 3 → ℝ) : unsharpSeed v = 3 / 4 + v 2 / 4 := by
  simp [unsharpSeed] <;> ring

theorem unsharpSeed_bounds {v : Fin 3 → ℝ} (hv : v ∈ ball3) :
    1 / 2 ≤ unsharpSeed v ∧ unsharpSeed v ≤ 1 := by
  rw [mem_ball3] at hv
  rw [unsharpSeed_apply]
  constructor <;> nlinarith [sq_nonneg (v 0), sq_nonneg (v 1), sq_nonneg (v 2 + 1),
    sq_nonneg (v 2 - 1)]

theorem unsharpSeed_isEffectOn : IsEffectOn ball3 unsharpSeed := fun _ hv =>
  ⟨by linarith [(unsharpSeed_bounds hv).1], (unsharpSeed_bounds hv).2⟩

theorem unsharpSeed_certain : unsharpSeed ![0, 0, 1] = 1 := by
  rw [unsharpSeed_apply]
  show (3 : ℝ) / 4 + 1 / 4 = 1
  norm_num

theorem unsharpSeed_isProperOn : IsProperOn ball3 unsharpSeed :=
  ⟨![0, 0, -1], by show (0 : ℝ) ^ 2 + 0 ^ 2 + (-1) ^ 2 ≤ 1; norm_num,
    by rw [unsharpSeed_apply]; show (3 : ℝ) / 4 + -1 / 4 < 1; norm_num⟩

theorem not_sharpSeed_unsharp : ¬ SharpSeed ball3 unsharpSeed := by
  rintro ⟨-, -, ⟨y, hy, h0⟩⟩
  have := (unsharpSeed_bounds hy).1
  linarith

/-- Every transport of the unsharp seed along automorphisms of the ball misses the directional
family. -/
theorem unsharp_seedOrbit_disjoint {G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))}
    (hG : PreservesBody ball3 G) : ∀ f ∈ seedOrbit G unsharpSeed, f ∉ directionalFamily := by
  rintro f ⟨g, hg, rfl⟩ ⟨b, hb, heq⟩
  have hbm : b ∈ ball3 := (mem_ball3 b).mpr hb.le
  have h1 : seedTransport unsharpSeed g (-b) = ballEffect b (-b) := by rw [heq]
  rw [seedTransport_apply, ballEffect_neg_self hb] at h1
  have h2 := (unsharpSeed_bounds (hG g hg (-b) (neg_mem_ball3 hbm)).2).1
  linarith

/-- **N2.** Without the zero value, the orbit is not the directional family, for every group of
automorphisms, the transitive one included. -/
theorem not_seedOrbit_unsharp_eq {G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))}
    (hG : PreservesBody ball3 G) : seedOrbit G unsharpSeed ≠ directionalFamily := by
  intro h
  have hmem : ballEffect ![0, 0, 1] ∈ seedOrbit G unsharpSeed := by
    rw [h]
    exact ⟨_, ez_sphere, rfl⟩
  exact unsharp_seedOrbit_disjoint hG _ hmem ⟨_, ez_sphere, rfl⟩

/-- **N2, (SEC) side.** The unsharp seed still gives (SEC): (SEC) needs a proper certain seed,
the directional family needs the zero value as well. -/
theorem supportingEffectComplete_unsharp :
    SupportingEffectComplete ball3 (seedOrbit fullAut3 unsharpSeed) :=
  supportingEffectComplete_of_cover preservesBody_fullAut3 unsharpSeed_isEffectOn
    unsharpSeed_isProperOn unsharpSeed_certain
    (coversBoundaryFrom_of_transitive boundaryTransitive_fullAut3
      (isBoundaryState_ball3_of_sphere ez_sphere))
    (seedOrbitAvailable_self fullAut3 unsharpSeed)

/-! #### Negative control N4: the index set is the quadratic-form sphere -/

/-- `(1, 1, 1)` lies on the unit sphere of the sup norm of `Fin 3 → ℝ`. -/
theorem cubeCorner_mem_sphere : (![1, 1, 1] : Fin 3 → ℝ) ∈ Metric.sphere (0 : Fin 3 → ℝ) 1 := by
  rw [mem_sphere_zero_iff_norm]
  apply le_antisymm
  · rw [pi_norm_le_iff_of_nonneg zero_le_one]
    intro i
    fin_cases i <;> simp
  · have h := norm_le_pi_norm (![1, 1, 1] : Fin 3 → ℝ) 0
    simpa using h

/-- **N4.** The directional effect indexed by that point is not an effect on the ball. -/
theorem not_isEffectOn_ballEffect_cubeCorner : ¬ IsEffectOn ball3 (ballEffect ![1, 1, 1]) := by
  intro h
  have hm : (![3 / 5, 4 / 5, 0] : Fin 3 → ℝ) ∈ ball3 := by
    show (3 / 5 : ℝ) ^ 2 + (4 / 5) ^ 2 + 0 ^ 2 ≤ 1
    norm_num
  have h2 := (h _ hm).2
  rw [ballEffect_apply] at h2
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons, Matrix.cons_val_two,
    Matrix.tail_cons] at h2
  norm_num at h2

/-! ### The verdict -/

/-- The reduced orbit-generation theorem with its consumers and controls, together. -/
theorem orbit_generation_core :
    (∀ (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) (r : V →ᵃ[ℝ] ℝ) (avail : Set (V →ᵃ[ℝ] ℝ)) (x₀ : V),
      PreservesBody Ω G → IsEffectOn Ω r → IsProperOn Ω r → r x₀ = 1 →
      CoversBoundaryFrom Ω G x₀ → SeedOrbitAvailable G r avail →
      SupportingEffectComplete Ω avail) ∧
    (∀ (G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))) (r : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ),
      PreservesBody ball3 G → SharpSeed ball3 r → BoundaryTransitive ball3 G →
      seedOrbit G r = directionalFamily) ∧
    (∀ (G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))) (r : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ)
      (avail : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ)),
      PreservesBody ball3 G → SharpSeed ball3 r → BoundaryTransitive ball3 G →
      SeedOrbitAvailable G r avail →
      ∀ b : Fin 3 → ℝ, (∑ j, b j ^ 2) = 1 → ballEffect b ∈ avail) ∧
    (∀ (G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ))) (r : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ)
      (avail : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ)),
      PreservesBody ball3 G → SharpSeed ball3 r → BoundaryTransitive ball3 G →
      SeedOrbitAvailable G r avail → ∀ (x0 : ℝ) (v : Fin 3 → ℝ),
      (∀ e ∈ avail, 0 ≤ conePair e x0 v) → 0 ≤ x0 ∧ (∑ j, v j ^ 2) ≤ x0 ^ 2) ∧
    seedOrbit fullAut3 (ballEffect ![0, 0, 1]) = directionalFamily ∧
    ¬ BoundaryTransitive ball3 (Set.range rot3) ∧
    (∀ G : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)), PreservesBody ball3 G →
      seedOrbit G unsharpSeed ≠ directionalFamily) ∧
    SupportingEffectComplete ball3 (seedOrbit fullAut3 unsharpSeed) ∧
    ¬ IsEffectOn ball3 (ballEffect ![1, 1, 1]) := by
  refine ⟨?_, ?_, ?_, ?_, seedOrbit_fullAut3, not_boundaryTransitive_flow, ?_,
    supportingEffectComplete_unsharp, not_isEffectOn_ballEffect_cubeCorner⟩
  · intro Ω G r avail x₀ hG he hp hx₀ hcov hV4
    exact supportingEffectComplete_of_cover hG he hp hx₀ hcov hV4
  · intro G r hG hP1 hK
    exact seedOrbit_ball3_eq hG hP1 hK
  · intro G r avail hG hP1 hK hV4
    exact ballEffect_mem_avail hG hP1 hK hV4
  · intro G r avail hG hP1 hK hV4 x0 v h
    exact lorentz_of_available hG hP1 hK hV4 x0 v h
  · intro G hG
    exact not_seedOrbit_unsharp_eq hG

end OrbitGeneration
end OIBridge

#print axioms OIBridge.OrbitGeneration.seedTransport_apply
#print axioms OIBridge.OrbitGeneration.seedTransport_apply_apply
#print axioms OIBridge.OrbitGeneration.isEffectOn_seedTransport
#print axioms OIBridge.OrbitGeneration.isProperOn_seedTransport
#print axioms OIBridge.OrbitGeneration.sharpSeed_seedTransport
#print axioms OIBridge.OrbitGeneration.sharpSeed_isProperOn
#print axioms OIBridge.OrbitGeneration.sharpSeed_certain_isBoundaryState
#print axioms OIBridge.OrbitGeneration.sharpSeed_of_perfectlyDistinguishable
#print axioms OIBridge.OrbitGeneration.seedOrbit_subset
#print axioms OIBridge.OrbitGeneration.seedOrbitAvailable_self
#print axioms OIBridge.OrbitGeneration.drive_flow_symm_apply
#print axioms OIBridge.OrbitGeneration.preservesBody_drive
#print axioms OIBridge.OrbitGeneration.supportingEffectComplete_of_cover
#print axioms OIBridge.OrbitGeneration.coversBoundaryFrom_of_transitive
#print axioms OIBridge.OrbitGeneration.supportingEffectComplete_of_sharp_transitive
#print axioms OIBridge.OrbitGeneration.neg_mem_ball3
#print axioms OIBridge.OrbitGeneration.ballEffect_self
#print axioms OIBridge.OrbitGeneration.ballEffect_neg_self
#print axioms OIBridge.OrbitGeneration.ballEffect_isEffectOn
#print axioms OIBridge.OrbitGeneration.ballEffect_sharp
#print axioms OIBridge.OrbitGeneration.isBoundaryState_ball3_of_sphere
#print axioms OIBridge.OrbitGeneration.sphere_of_isBoundaryState_ball3
#print axioms OIBridge.OrbitGeneration.affine3_apply
#print axioms OIBridge.OrbitGeneration.ball3_sharp_eq
#print axioms OIBridge.OrbitGeneration.sharpSeed_ball3_mem_directional
#print axioms OIBridge.OrbitGeneration.seedOrbit_ball3_eq
#print axioms OIBridge.OrbitGeneration.ballEffect_mem_avail
#print axioms OIBridge.OrbitGeneration.supportingEffectComplete_ball3_of_orbit
#print axioms OIBridge.OrbitGeneration.kInf1_ball3_of_orbit
#print axioms OIBridge.OrbitGeneration.conePair_ballEffect
#print axioms OIBridge.OrbitGeneration.lorentz_of_seedOrbit
#print axioms OIBridge.OrbitGeneration.lorentz_of_available
#print axioms OIBridge.OrbitGeneration.ez_sphere
#print axioms OIBridge.OrbitGeneration.hhFun_dot
#print axioms OIBridge.OrbitGeneration.hhFun_hhFun
#print axioms OIBridge.OrbitGeneration.hhFun_normSq
#print axioms OIBridge.OrbitGeneration.hhFun_swap
#print axioms OIBridge.OrbitGeneration.hh3_apply
#print axioms OIBridge.OrbitGeneration.hh3_symm_apply
#print axioms OIBridge.OrbitGeneration.hhFun_mem_ball3
#print axioms OIBridge.OrbitGeneration.preservesBody_fullAut3
#print axioms OIBridge.OrbitGeneration.refl_mem_fullAut3
#print axioms OIBridge.OrbitGeneration.hh3_mem_fullAut3
#print axioms OIBridge.OrbitGeneration.boundaryTransitive_fullAut3
#print axioms OIBridge.OrbitGeneration.seedOrbit_fullAut3
#print axioms OIBridge.OrbitGeneration.rot3_symm_apply
#print axioms OIBridge.OrbitGeneration.preservesBody_flow
#print axioms OIBridge.OrbitGeneration.seedTransport_rot3_ez
#print axioms OIBridge.OrbitGeneration.seedOrbit_flow
#print axioms OIBridge.OrbitGeneration.ballEffect_ex_ne_ez
#print axioms OIBridge.OrbitGeneration.not_seedOrbit_flow_eq
#print axioms OIBridge.OrbitGeneration.not_boundaryTransitive_flow
#print axioms OIBridge.OrbitGeneration.unsharpSeed_apply
#print axioms OIBridge.OrbitGeneration.unsharpSeed_bounds
#print axioms OIBridge.OrbitGeneration.unsharpSeed_isEffectOn
#print axioms OIBridge.OrbitGeneration.unsharpSeed_certain
#print axioms OIBridge.OrbitGeneration.unsharpSeed_isProperOn
#print axioms OIBridge.OrbitGeneration.not_sharpSeed_unsharp
#print axioms OIBridge.OrbitGeneration.unsharp_seedOrbit_disjoint
#print axioms OIBridge.OrbitGeneration.not_seedOrbit_unsharp_eq
#print axioms OIBridge.OrbitGeneration.supportingEffectComplete_unsharp
#print axioms OIBridge.OrbitGeneration.cubeCorner_mem_sphere
#print axioms OIBridge.OrbitGeneration.not_isEffectOn_ballEffect_cubeCorner
#print axioms OIBridge.OrbitGeneration.orbit_generation_core
