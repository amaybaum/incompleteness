/-
  OIBridge/KInfFoundations.lean — round KINF-1: the field-neutral vocabulary of the pre-quantum
  operational completion, and the elementary lemmas that vocabulary supports.

  Nothing in this module mentions ℂ, a matrix carrier, or the substratum. It fixes definitions
  over a real normed space `V` and proves the small logical facts that later rounds cite. It
  sources nothing: the module does not derive drivability, supporting effects, singleton faces
  or copy naturality from any OI construction, and it contains no reconstruction theorem.

  Defined here.
    §A  a finite observer stage: finitely many preparations and effects and a probability table
        with a unit effect; its state body is the convex hull of the preparation vectors.
    §B  effects on a convex body, the certain face of an effect, supporting-effect completeness
        (SEC), singleton faces (SF), full effects, perfect distinguishability, central symmetry.
    §C  elementary drivability: a continuous one-parameter family of affine automorphisms of
        the body, starting at the identity, with a distinguished member `N` and a reversible
        `J` that does not normalize the flow; and copy naturality of two NOTs under a copy
        identification.
    §G  `KInf1`, the statement of hypothesis K∞-1 as a proposition about a body and a family of
        available effects. It is a definition and is proved for nothing here.

  Proved here.
    §A  `states_isCompact`, `states_unit`: the state body of a finite stage is compact and lies
        on the unit hyperplane.
    §D  Lemma C, `strictConvex_of_supporting_singleton`: a closed convex body with (SEC) and (SF)
        is strictly convex.
    §D  Lemma D, `card_le_two_of_centrallySymmetric`: a centrally symmetric body admits at most
        two perfectly distinguishable states, whatever effects are available.
    §E  Lemma B, `eq_closedBall_of_frontier_subset_sphere`: a compact convex body with `0` in
        its interior whose frontier lies on the unit sphere is the closed unit ball.
    §E  the finite-preparation bound, `exposed_mem_range` and `exposed_ncard_le`: every point of
        a finite stage's body exposed by an effect with a singleton certain face is the vector
        of one of its preparations, so at most `|P|` points are exposed.
    §E′ Theorem F2, `classical_exposed_ncard_le`: a body realized on `N` ontic states, meeting
        each coordinate facet in at most one point, has at most `N` points exposed by response
        effects; `response_eq_one_forces` is the step that puts every exposed point on a facet.
    §F  `qubit_certain_face`: for the imported qubit kinematics, the certain face of the effect
        `ρ ↦ ρ 0 0` on density matrices is the single point `|0⟩⟨0|`. This is a theorem of matrix
        kinematics, stated as such.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.Analysis.Convex.Gauge
import Mathlib.Analysis.Convex.Strict
import Mathlib.Analysis.Convex.Topology
import Mathlib.Analysis.Normed.Module.Basic
import Mathlib.Data.Set.Card
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.Trace
import OIBridge.CoherentExtension

namespace OIBridge
namespace KInfFoundations

open Set

/-! ### §A — the finite observer stage -/

/-- A finite observer stage: finitely many preparations `P`, finitely many effects `E`, a
probability table `p e x ∈ [0, 1]`, and a unit effect certain on every preparation. -/
structure FiniteStage where
  P : Type
  E : Type
  [fP : Fintype P]
  [fE : Fintype E]
  p : E → P → ℝ
  unit : E
  nonneg : ∀ e x, 0 ≤ p e x
  le_one : ∀ e x, p e x ≤ 1
  unit_eq : ∀ x, p unit x = 1

attribute [instance] FiniteStage.fP FiniteStage.fE

namespace FiniteStage

variable (S : FiniteStage)

/-- The probability vector of a preparation, indexed by the stage's effects. -/
def vec (x : S.P) : S.E → ℝ := fun e => S.p e x

/-- The state body: the convex hull of the preparation vectors. -/
def states : Set (S.E → ℝ) := convexHull ℝ (Set.range S.vec)

/-- The state body of a finite stage is compact. -/
theorem states_isCompact : IsCompact S.states :=
  (Set.finite_range S.vec).isCompact_convexHull ℝ

/-- The state body of a finite stage is closed. -/
theorem states_isClosed : IsClosed S.states :=
  S.states_isCompact.isClosed

/-- The state body of a finite stage is convex. -/
theorem states_convex : Convex ℝ S.states :=
  convex_convexHull ℝ _

/-- Every state of a finite stage is certain for the unit effect. -/
theorem states_unit : ∀ v ∈ S.states, v S.unit = 1 := by
  have hconv : Convex ℝ {v : S.E → ℝ | v S.unit = 1} := by
    intro v hv w hw a b _ _ hab
    simp only [Set.mem_ofPred_eq, Pi.add_apply, Pi.smul_apply, smul_eq_mul] at hv hw ⊢
    rw [hv, hw]; linarith
  have hsub : Set.range S.vec ⊆ {v : S.E → ℝ | v S.unit = 1} := by
    rintro _ ⟨x, rfl⟩
    exact S.unit_eq x
  exact fun v hv => convexHull_min hsub hconv hv

end FiniteStage

/-! ### §B — effects on a convex body -/

variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V]

/-- An affine functional is an effect on `Ω` when it takes values in `[0, 1]` on `Ω`. -/
def IsEffectOn (Ω : Set V) (e : V →ᵃ[ℝ] ℝ) : Prop :=
  ∀ x ∈ Ω, 0 ≤ e x ∧ e x ≤ 1

/-- The certain face of an effect: the states on which it is certain. -/
def certainFace (Ω : Set V) (e : V →ᵃ[ℝ] ℝ) : Set V :=
  {x ∈ Ω | e x = 1}

/-- Supporting-effect completeness (SEC) relative to a family `avail` of available functionals:
every frontier point of `Ω` is certain for some available effect. -/
def SupportingEffectComplete (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  ∀ x ∈ frontier Ω, ∃ e ∈ avail, IsEffectOn Ω e ∧ e x = 1

/-- Singleton faces (SF): every available effect is certain on at most one state. -/
def SingletonFaces (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  ∀ e ∈ avail, IsEffectOn Ω e → (certainFace Ω e).Subsingleton

/-- The full effect family: every affine functional that is an effect on `Ω`. -/
def fullEffects (Ω : Set V) : Set (V →ᵃ[ℝ] ℝ) :=
  {e | IsEffectOn Ω e}

/-- A finite family of states is perfectly distinguishable by a family of effects when the
effects are effects on `Ω`, sum to the unit on `Ω`, and each is certain on its own state. -/
def PerfectlyDistinguishable (Ω : Set V) {ι : Type} [Fintype ι]
    (x : ι → V) (e : ι → V →ᵃ[ℝ] ℝ) : Prop :=
  (∀ i, x i ∈ Ω) ∧ (∀ i, IsEffectOn Ω (e i)) ∧ (∀ y ∈ Ω, ∑ i, e i y = 1) ∧
    (∀ i, e i (x i) = 1)

/-- Central symmetry of `Ω` about `c`: the reflection `x ↦ c + (c − x)` preserves `Ω`. -/
def CentrallySymmetric (Ω : Set V) (c : V) : Prop :=
  ∀ x ∈ Ω, c + (c - x) ∈ Ω

/-- An affine functional on a convex combination of two points. -/
theorem affine_combo (e : V →ᵃ[ℝ] ℝ) (x y : V) (a b : ℝ) (hab : a + b = 1) :
    e (a • x + b • y) = a * e x + b * e y := by
  have ha : a = 1 - b := by linarith
  subst ha
  rw [← AffineMap.lineMap_apply_module, AffineMap.apply_lineMap,
    AffineMap.lineMap_apply_module, smul_eq_mul, smul_eq_mul]

/-- An affine functional on the reflection of `x` through `c`. -/
theorem affine_reflect (e : V →ᵃ[ℝ] ℝ) (c x : V) :
    e (c + (c - x)) = 2 * e c - e x := by
  have h1 : c + (c - x) = (c - x) +ᵥ c := by rw [vadd_eq_add, add_comm]
  have h2 : e.linear (c -ᵥ x) = e c -ᵥ e x := AffineMap.linearMap_vsub e c x
  simp only [vsub_eq_sub] at h2
  rw [h1, AffineMap.map_vadd, h2, vadd_eq_add]
  ring

/-- The sublevel set of an affine functional is convex. -/
theorem convex_affine_le (e : V →ᵃ[ℝ] ℝ) (m : ℝ) : Convex ℝ {y : V | e y ≤ m} := by
  intro x hx y hy a b ha hb hab
  simp only [Set.mem_ofPred_eq] at hx hy ⊢
  rw [affine_combo e x y a b hab]
  have h1 : 0 ≤ a * (m - e x) := mul_nonneg ha (sub_nonneg.mpr hx)
  have h2 : 0 ≤ b * (m - e y) := mul_nonneg hb (sub_nonneg.mpr hy)
  have h3 : a * m + b * m = m := by rw [← add_mul, hab, one_mul]
  nlinarith [h1, h2, h3]

/-! ### §C — elementary drivability and copy naturality -/

/-- Elementary drivability of a body `Ω`, stated without a field: a continuous one-parameter
family of affine automorphisms of `V` preserving `Ω`, the identity at `0`, on which a
distinguished involution `N` lies, together with a reversible `J` preserving `Ω` whose
conjugation moves the flow off itself. -/
structure ElementaryDrivability (Ω : Set V) where
  flow : ℝ → V ≃ᵃ[ℝ] V
  flow_zero : flow 0 = AffineEquiv.refl ℝ V
  flow_continuous : Continuous fun q : ℝ × V => flow q.1 q.2
  flow_preserves : ∀ t, ∀ x ∈ Ω, flow t x ∈ Ω
  t₀ : ℝ
  N_involutive : ∀ x, flow t₀ (flow t₀ x) = x
  N_moves : ∃ x ∈ Ω, flow t₀ x ≠ x
  J : V ≃ᵃ[ℝ] V
  J_preserves : ∀ x ∈ Ω, J x ∈ Ω
  J_off_axis : ∃ t, ∀ s, (J.symm.trans (flow t)).trans J ≠ flow s

/-- The NOT of an elementary drive: the flow's member at `t₀`. -/
def ElementaryDrivability.N {Ω : Set V} (D : ElementaryDrivability Ω) : V ≃ᵃ[ℝ] V :=
  D.flow D.t₀

/-- Copy naturality: under the identification `e` of copy `A` with copy `B`, the NOT of `B`
is the conjugate of the NOT of `A`. -/
def CopyNatural (N_A N_B : V ≃ᵃ[ℝ] V) (e : V ≃ᵃ[ℝ] V) : Prop :=
  N_B = (e.symm.trans N_A).trans e

/-- Under the identity identification, copy naturality is the equality of the two NOTs. -/
theorem copyNatural_refl_iff (N_A N_B : V ≃ᵃ[ℝ] V) :
    CopyNatural N_A N_B (AffineEquiv.refl ℝ V) ↔ N_B = N_A := by
  unfold CopyNatural
  simp

/-- Copy naturality is the pointwise conjugation identity `N_B (e x) = e (N_A x)`. -/
theorem copyNatural_iff_apply (N_A N_B : V ≃ᵃ[ℝ] V) (e : V ≃ᵃ[ℝ] V) :
    CopyNatural N_A N_B e ↔ ∀ x, N_B (e x) = e (N_A x) := by
  unfold CopyNatural
  constructor
  · intro h x
    rw [h, AffineEquiv.trans_apply, AffineEquiv.trans_apply, AffineEquiv.symm_apply_apply]
  · intro h
    ext y
    rw [AffineEquiv.trans_apply, AffineEquiv.trans_apply]
    have := h (e.symm y)
    rw [AffineEquiv.apply_symm_apply] at this
    exact this

/-! ### §D — Lemma C and Lemma D -/

/-- **Lemma C.** A closed convex body with supporting-effect completeness and singleton faces
is strictly convex. -/
theorem strictConvex_of_supporting_singleton {Ω : Set V} {avail : Set (V →ᵃ[ℝ] ℝ)}
    (hconv : Convex ℝ Ω) (hcl : IsClosed Ω)
    (hSEC : SupportingEffectComplete Ω avail) (hSF : SingletonFaces Ω avail) :
    StrictConvex ℝ Ω := by
  intro x hx y hy hxy a b ha hb hab
  by_contra hint
  have hz : a • x + b • y ∈ Ω := hconv hx hy ha.le hb.le hab
  have hfr : a • x + b • y ∈ frontier Ω := by
    rw [frontier, hcl.closure_eq]
    exact ⟨hz, hint⟩
  obtain ⟨e, he, heff, hone⟩ := hSEC _ hfr
  rw [affine_combo e x y a b hab] at hone
  have hex := (heff x hx).2
  have hey := (heff y hy).2
  have hx1 : e x = 1 := by nlinarith
  have hy1 : e y = 1 := by nlinarith
  exact hxy (hSF e he heff ⟨hx, hx1⟩ ⟨hy, hy1⟩)

/-- **Lemma D.** A centrally symmetric body admits at most two perfectly distinguishable
states, for any family of effects. -/
theorem card_le_two_of_centrallySymmetric {Ω : Set V} {c : V} (hΩ : CentrallySymmetric Ω c)
    (hc : c ∈ Ω) {ι : Type} [Fintype ι] (x : ι → V) (e : ι → V →ᵃ[ℝ] ℝ)
    (hpd : PerfectlyDistinguishable Ω x e) : Fintype.card ι ≤ 2 := by
  obtain ⟨hx, he, hsum, hdiag⟩ := hpd
  have key : ∀ i, (1 / 2 : ℝ) ≤ e i c := by
    intro i
    have h := (he i (c + (c - x i)) (hΩ _ (hx i))).1
    rw [affine_reflect, hdiag i] at h
    linarith
  have hs := Finset.sum_le_sum (fun i (_ : i ∈ (Finset.univ : Finset ι)) => key i)
  rw [hsum c hc, Finset.sum_const, Finset.card_univ, nsmul_eq_mul] at hs
  have : (Fintype.card ι : ℝ) ≤ 2 := by linarith
  exact_mod_cast this

/-- Capacity is not state-geometric on its own: a centrally symmetric body has capacity at
most two even with the full effect family. -/
theorem card_le_two_of_centrallySymmetric_full {Ω : Set V} {c : V}
    (hΩ : CentrallySymmetric Ω c) (hc : c ∈ Ω) {ι : Type} [Fintype ι] (x : ι → V)
    (e : ι → V →ᵃ[ℝ] ℝ) (_ : ∀ i, e i ∈ fullEffects Ω)
    (hpd : PerfectlyDistinguishable Ω x e) : Fintype.card ι ≤ 2 :=
  card_le_two_of_centrallySymmetric hΩ hc x e hpd

/-! ### §E — Lemma B and the finite-exposure bound -/

/-- **Lemma B.** A compact convex body with `0` in its interior whose frontier lies on the
unit sphere is the closed unit ball. -/
theorem eq_closedBall_of_frontier_subset_sphere {Ω : Set V} (hconv : Convex ℝ Ω)
    (hcomp : IsCompact Ω) (h0 : (0 : V) ∈ interior Ω)
    (hfr : frontier Ω ⊆ Metric.sphere (0 : V) 1) : Ω = Metric.closedBall (0 : V) 1 := by
  have hnhds : Ω ∈ nhds (0 : V) := mem_interior_iff_mem_nhds.mp h0
  have habs : Absorbent ℝ Ω := absorbent_nhds_zero hnhds
  have hcl : closure Ω = Ω := hcomp.isClosed.closure_eq
  -- a nonzero vector scaled to gauge one lies on the frontier, hence on the sphere
  have hscale : ∀ x : V, 0 < gauge Ω x → ‖x‖ = gauge Ω x := by
    intro x hg
    have h1 : gauge Ω ((gauge Ω x)⁻¹ • x) = 1 := by
      rw [gauge_smul_of_nonneg (inv_nonneg.mpr hg.le), smul_eq_mul, inv_mul_cancel₀ hg.ne']
    have hfr' : (gauge Ω x)⁻¹ • x ∈ frontier Ω :=
      (gauge_eq_one_iff_mem_frontier hconv hnhds).mp h1
    have hn : ‖(gauge Ω x)⁻¹ • x‖ = 1 := mem_sphere_zero_iff_norm.mp (hfr hfr')
    rw [norm_smul, norm_inv, Real.norm_of_nonneg hg.le, inv_mul_eq_div,
      div_eq_one_iff_eq hg.ne'] at hn
    exact hn
  -- the gauge is positive off zero, since Ω is bounded
  obtain ⟨r, hr⟩ := (Metric.isBounded_iff_subset_closedBall (0 : V)).mp hcomp.isBounded
  have hr' : Ω ⊆ Metric.closedBall (0 : V) (max r 1) :=
    hr.trans (Metric.closedBall_subset_closedBall (le_max_left r 1))
  have hrpos : (0 : ℝ) < max r 1 := lt_of_lt_of_le zero_lt_one (le_max_right r 1)
  have hpos : ∀ x : V, x ≠ 0 → 0 < gauge Ω x := by
    intro x hx
    have hle := le_gauge_of_subset_closedBall habs hrpos.le hr' (x := x)
    exact lt_of_lt_of_le (div_pos (norm_pos_iff.mpr hx) hrpos) hle
  ext x
  rw [Metric.mem_closedBall, dist_zero_right]
  constructor
  · intro hx
    by_cases hx0 : x = 0
    · subst hx0; simp
    · rw [hscale x (hpos x hx0)]
      exact gauge_le_one_of_mem hx
  · intro hx
    by_cases hx0 : x = 0
    · subst hx0; exact mem_of_mem_nhds hnhds
    · rw [hscale x (hpos x hx0)] at hx
      have := (gauge_le_one_iff_mem_closure hconv hnhds).mp hx
      rwa [hcl] at this

/-- The maximum of an effect over a finite stage's body is attained at a preparation: if the
effect is certain on some state, it is certain on some preparation vector. -/
theorem exists_vertex_of_certain {ι : Type} [Fintype ι] (v : ι → V) (e : V →ᵃ[ℝ] ℝ)
    (he : ∀ y ∈ convexHull ℝ (Set.range v), e y ≤ 1) (x : V)
    (hx : x ∈ convexHull ℝ (Set.range v)) (hone : e x = 1) : ∃ k, e (v k) = 1 := by
  by_contra hno
  have hno' : ∀ k, e (v k) ≠ 1 := fun k hk => hno ⟨k, hk⟩
  have hne : (Finset.univ : Finset ι).Nonempty := by
    rcases isEmpty_or_nonempty ι with h | h
    · exfalso
      have : Set.range v = ∅ := Set.range_eq_empty v
      rw [this, convexHull_empty] at hx
      simp at hx
    · exact Finset.univ_nonempty
  set m := Finset.univ.sup' hne (fun k => e (v k)) with hm
  have hlt : m < 1 := by
    rw [hm, Finset.sup'_lt_iff]
    intro k _
    exact lt_of_le_of_ne (he (v k) (subset_convexHull ℝ _ ⟨k, rfl⟩)) (hno' k)
  have hsub : Set.range v ⊆ {y : V | e y ≤ m} := by
    rintro _ ⟨k, rfl⟩
    exact Finset.le_sup' (fun k => e (v k)) (Finset.mem_univ k)
  have := convexHull_min hsub (convex_affine_le e m) hx
  simp only [Set.mem_ofPred_eq] at this
  linarith

/-- **The finite-exposure bound, pointwise.** A point of a finite stage's body exposed by an
effect with singleton certain face is the vector of one of its preparations. -/
theorem exposed_mem_range {ι : Type} [Fintype ι] (v : ι → V) (e : V →ᵃ[ℝ] ℝ)
    (he : ∀ y ∈ convexHull ℝ (Set.range v), e y ≤ 1) (x : V)
    (hface : certainFace (convexHull ℝ (Set.range v)) e = {x}) : x ∈ Set.range v := by
  have hx : x ∈ certainFace (convexHull ℝ (Set.range v)) e := by
    rw [hface]; exact Set.mem_singleton x
  obtain ⟨k, hk⟩ := exists_vertex_of_certain v e he x hx.1 hx.2
  have hk' : v k ∈ certainFace (convexHull ℝ (Set.range v)) e :=
    ⟨subset_convexHull ℝ _ ⟨k, rfl⟩, hk⟩
  rw [hface] at hk'
  exact ⟨k, hk'⟩

/-- The set of points exposed by some effect with a singleton certain face. -/
def exposedPoints (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Set V :=
  {x | ∃ e ∈ avail, IsEffectOn Ω e ∧ certainFace Ω e = {x}}

/-- **The finite-exposure bound, counted.** A finite stage on `ι` exposes at most `|ι|` points,
whatever effects are available. -/
theorem exposed_ncard_le {ι : Type} [Fintype ι] (v : ι → V) (avail : Set (V →ᵃ[ℝ] ℝ)) :
    (exposedPoints (convexHull ℝ (Set.range v)) avail).ncard ≤ Fintype.card ι := by
  have hsub : exposedPoints (convexHull ℝ (Set.range v)) avail ⊆ Set.range v := by
    rintro x ⟨e, _, heff, hface⟩
    exact exposed_mem_range v e (fun y hy => (heff y hy).2) x hface
  calc (exposedPoints (convexHull ℝ (Set.range v)) avail).ncard
      ≤ (Set.range v).ncard := Set.ncard_le_ncard hsub (Set.finite_range v)
    _ = (v '' Set.univ).ncard := by rw [Set.image_univ]
    _ ≤ (Set.univ : Set ι).ncard := Set.ncard_image_le Set.finite_univ
    _ = Fintype.card ι := by rw [Set.ncard_univ, Nat.card_eq_fintype_card]

/-- The finite-exposure bound for a finite stage. -/
theorem FiniteStage.exposed_ncard_le (S : FiniteStage)
    (avail : Set ((S.E → ℝ) →ᵃ[ℝ] ℝ)) :
    (exposedPoints S.states avail).ncard ≤ Fintype.card S.P := by
  unfold FiniteStage.states
  exact KInfFoundations.exposed_ncard_le S.vec avail

/-! ### §E′ — Theorem F2: a finite classical realization exposes at most `N` states

A finite classical realization of a body on `N` ontic states places its states in the
probability simplex on `Fin N` and reads them out with response effects `p ↦ ∑ cᵢ pᵢ`,
`0 ≤ cᵢ ≤ 1`. Such an effect is certain on a state only where the state has a zero coordinate,
unless the effect is the unit; and a body that meets each coordinate facet in at most one point
(a strictly convex body relative to its affine span does) has at most one exposed point per
facet. The response effects are stated as functions on `Fin N → ℝ`, without the affine-map
structure of §B, since the bound needs only the form `∑ cᵢ pᵢ`. -/

section Classical

variable {N : ℕ}

/-- The probability simplex on `N` ontic states. -/
def simplex (N : ℕ) : Set (Fin N → ℝ) :=
  {p | (∀ i, 0 ≤ p i) ∧ ∑ i, p i = 1}

/-- A point of a body in the simplex exposed by a response effect: the response effect with
vector `c ∈ [0, 1]^N` is certain exactly there. -/
def ClassicallyExposed (Ω : Set (Fin N → ℝ)) (x : Fin N → ℝ) : Prop :=
  ∃ c : Fin N → ℝ, (∀ i, 0 ≤ c i ∧ c i ≤ 1) ∧ {p ∈ Ω | ∑ i, c i * p i = 1} = {x}

/-- A response effect certain on a state of the simplex has full response wherever the state
has positive weight. -/
theorem response_eq_one_forces {Ω : Set (Fin N → ℝ)} (hΩ : Ω ⊆ simplex N) {c : Fin N → ℝ}
    (hc : ∀ i, 0 ≤ c i ∧ c i ≤ 1) {x : Fin N → ℝ} (hx : x ∈ Ω)
    (hone : ∑ i, c i * x i = 1) : ∀ i, 0 < x i → c i = 1 := by
  intro i hi
  obtain ⟨hnn, hsum⟩ := hΩ hx
  by_contra hne
  have hci : c i < 1 := lt_of_le_of_ne (hc i).2 hne
  have hlt : c i * x i < x i := by nlinarith
  have hle : ∀ j, c j * x j ≤ x j := fun j => by
    have := (hc j).2
    have := hnn j
    nlinarith
  have : ∑ j, c j * x j < ∑ j, x j :=
    Finset.sum_lt_sum (fun j _ => hle j) ⟨i, Finset.mem_univ i, hlt⟩
  rw [hone, hsum] at this
  exact lt_irrefl _ this

/-- An exposed point lies in the body. -/
theorem mem_of_classicallyExposed {Ω : Set (Fin N → ℝ)} {x : Fin N → ℝ}
    (hx : ClassicallyExposed Ω x) : x ∈ Ω := by
  obtain ⟨c, _, hface⟩ := hx
  have : x ∈ {p ∈ Ω | ∑ i, c i * p i = 1} := by rw [hface]; exact Set.mem_singleton x
  exact this.1

/-- An exposed point of a body with two distinct states has a zero coordinate. -/
theorem exists_zero_of_classicallyExposed {Ω : Set (Fin N → ℝ)} (hΩ : Ω ⊆ simplex N)
    (hnt : ¬ Ω.Subsingleton) {x : Fin N → ℝ} (hx : ClassicallyExposed Ω x) :
    ∃ i, x i = 0 := by
  obtain ⟨c, hc, hface⟩ := hx
  have hxΩ : x ∈ {p ∈ Ω | ∑ i, c i * p i = 1} := by rw [hface]; exact Set.mem_singleton x
  by_contra hno
  have hno' : ∀ i, x i ≠ 0 := fun i hi => hno ⟨i, hi⟩
  have hpos : ∀ i, 0 < x i := fun i => lt_of_le_of_ne ((hΩ hxΩ.1).1 i) (Ne.symm (hno' i))
  have hc1 : ∀ i, c i = 1 := fun i => response_eq_one_forces hΩ hc hxΩ.1 hxΩ.2 i (hpos i)
  apply hnt
  intro p hp q hq
  have hface' : ∀ y ∈ Ω, y ∈ {p ∈ Ω | ∑ i, c i * p i = 1} := by
    intro y hy
    refine ⟨hy, ?_⟩
    simp only [hc1, one_mul]
    exact (hΩ hy).2
  have hp' := hface' p hp
  have hq' := hface' q hq
  rw [hface] at hp' hq'
  exact (Set.mem_singleton_iff.mp hp').trans (Set.mem_singleton_iff.mp hq').symm

/-- **Theorem F2.** A body in the simplex on `N` ontic states that meets each coordinate facet
in at most one point has at most `N` classically exposed points. -/
theorem classical_exposed_ncard_le {Ω : Set (Fin N → ℝ)} (hΩ : Ω ⊆ simplex N)
    (hfacet : ∀ i, (Ω ∩ {p | p i = 0}).Subsingleton) :
    {x | ClassicallyExposed Ω x}.ncard ≤ N := by
  have hsub : {x | ClassicallyExposed Ω x} ⊆ Ω := fun x hx => mem_of_classicallyExposed hx
  by_cases hnt : Ω.Subsingleton
  · rcases Set.eq_empty_or_nonempty {x | ClassicallyExposed Ω x} with h | ⟨x, hx⟩
    · rw [h, Set.ncard_empty]; exact Nat.zero_le N
    · have hN : 1 ≤ N := by
        rcases Nat.eq_zero_or_pos N with h0 | h0
        · subst h0
          have := (hΩ (hsub hx)).2
          simp at this
        · exact h0
      calc {x | ClassicallyExposed Ω x}.ncard ≤ Ω.ncard := Set.ncard_le_ncard hsub hnt.finite
        _ ≤ 1 := (Set.ncard_le_one hnt.finite).mpr (fun a ha b hb => hnt ha hb)
        _ ≤ N := hN
  · obtain ⟨p, hp, q, hq, hpq⟩ : ∃ p ∈ Ω, ∃ q ∈ Ω, p ≠ q := by
      by_contra h
      exact hnt (fun p hp q hq => Classical.byContradiction (fun hne => h ⟨p, hp, q, hq, hne⟩))
    have hN : N ≠ 0 := by
      rintro rfl
      have := (hΩ hp).2
      simp at this
    have : NeZero N := ⟨hN⟩
    classical
    let f : (Fin N → ℝ) → Fin N := fun x =>
      if h : ∃ i, x i = 0 then Classical.choose h else 0
    have hf : ∀ x ∈ {x | ClassicallyExposed Ω x}, x (f x) = 0 := by
      intro x hx
      have h := exists_zero_of_classicallyExposed hΩ hnt hx
      simp only [f, dif_pos h]
      exact Classical.choose_spec h
    have hinj : Set.InjOn f {x | ClassicallyExposed Ω x} := by
      intro x hx y hy hxy
      exact hfacet (f x) ⟨hsub hx, hf x hx⟩ ⟨hsub hy, by rw [hxy]; exact hf y hy⟩
    calc {x | ClassicallyExposed Ω x}.ncard ≤ (Set.univ : Set (Fin N)).ncard :=
          Set.ncard_le_ncard_of_injOn f (fun x _ => Set.mem_univ _) hinj Set.finite_univ
      _ = N := by rw [Set.ncard_univ, Nat.card_eq_fintype_card, Fintype.card_fin]

end Classical

/-! ### §F — the qubit certain face, a theorem of the imported matrix kinematics -/

open Matrix in
open scoped ComplexOrder in
/-- For the qubit kinematics, a density matrix certain for the effect `ρ ↦ ρ 0 0` is `|0⟩⟨0|`:
the certain face of that effect is a single point. This is a statement about complex `2 × 2`
matrices, imported kinematics and not a field-neutral result. -/
theorem qubit_certain_face (ρ : Matrix (Fin 2) (Fin 2) ℂ) (hρ : ρ.PosSemidef)
    (htr : ρ.trace = 1) (h00 : ρ 0 0 = 1) :
    ρ = Matrix.of fun i j => if i = 0 ∧ j = 0 then (1 : ℂ) else 0 := by
  have h11 : ρ 1 1 = 0 := by
    rw [Matrix.trace_fin_two, h00] at htr
    linear_combination htr
  have h10 := OIBridge.CoherentExtension.psd_diag_zero_entry_zero hρ h11 0
  ext i j
  fin_cases i <;> fin_cases j <;> simp [h00, h11, h10.1, h10.2]

/-! ### §G — hypothesis K∞-1, as a statement -/

/-- **Hypothesis K∞-1**, stated and not proved: a body admitting an elementary drive has
supporting-effect completeness relative to the available effects. This is the field-neutral
Naimark step. The module proves it for nothing; it is the round's open target. -/
def KInf1 (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  Nonempty (ElementaryDrivability Ω) → SupportingEffectComplete Ω avail

/-- What K∞-1 buys when it holds: with singleton faces, a closed convex drivable body is
strictly convex. -/
theorem strictConvex_of_kInf1 {Ω : Set V} {avail : Set (V →ᵃ[ℝ] ℝ)}
    (hconv : Convex ℝ Ω) (hcl : IsClosed Ω) (hK : KInf1 Ω avail)
    (hD : Nonempty (ElementaryDrivability Ω)) (hSF : SingletonFaces Ω avail) :
    StrictConvex ℝ Ω :=
  strictConvex_of_supporting_singleton hconv hcl (hK hD) hSF

/-! ### The verdict -/

/-- The round's verdict: Lemma C, Lemma D, Lemma B and the finite-exposure bound, together. -/
theorem kinf1_kernel_core :
    (∀ (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)), Convex ℝ Ω → IsClosed Ω →
      SupportingEffectComplete Ω avail → SingletonFaces Ω avail → StrictConvex ℝ Ω) ∧
    (∀ (Ω : Set V) (c : V), CentrallySymmetric Ω c → c ∈ Ω →
      ∀ (ι : Type) [Fintype ι] (x : ι → V) (e : ι → V →ᵃ[ℝ] ℝ),
        PerfectlyDistinguishable Ω x e → Fintype.card ι ≤ 2) ∧
    (∀ Ω : Set V, Convex ℝ Ω → IsCompact Ω → (0 : V) ∈ interior Ω →
      frontier Ω ⊆ Metric.sphere (0 : V) 1 → Ω = Metric.closedBall (0 : V) 1) ∧
    (∀ (ι : Type) [Fintype ι] (v : ι → V) (avail : Set (V →ᵃ[ℝ] ℝ)),
      (exposedPoints (convexHull ℝ (Set.range v)) avail).ncard ≤ Fintype.card ι) ∧
    (∀ (N : ℕ) (Ω : Set (Fin N → ℝ)), Ω ⊆ simplex N →
      (∀ i, (Ω ∩ {p | p i = 0}).Subsingleton) → {x | ClassicallyExposed Ω x}.ncard ≤ N) := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · intro Ω avail hconv hcl hSEC hSF
    exact strictConvex_of_supporting_singleton hconv hcl hSEC hSF
  · intro Ω c hΩ hc ι _ x e hpd
    exact card_le_two_of_centrallySymmetric hΩ hc x e hpd
  · intro Ω hconv hcomp h0 hfr
    exact eq_closedBall_of_frontier_subset_sphere hconv hcomp h0 hfr
  · intro ι _ v avail
    exact exposed_ncard_le v avail
  · intro N Ω hΩ hfacet
    exact classical_exposed_ncard_le hΩ hfacet

end KInfFoundations
end OIBridge

#print axioms OIBridge.KInfFoundations.FiniteStage.states_isCompact
#print axioms OIBridge.KInfFoundations.FiniteStage.states_unit
#print axioms OIBridge.KInfFoundations.affine_combo
#print axioms OIBridge.KInfFoundations.affine_reflect
#print axioms OIBridge.KInfFoundations.copyNatural_iff_apply
#print axioms OIBridge.KInfFoundations.strictConvex_of_supporting_singleton
#print axioms OIBridge.KInfFoundations.card_le_two_of_centrallySymmetric
#print axioms OIBridge.KInfFoundations.eq_closedBall_of_frontier_subset_sphere
#print axioms OIBridge.KInfFoundations.exposed_mem_range
#print axioms OIBridge.KInfFoundations.exposed_ncard_le
#print axioms OIBridge.KInfFoundations.response_eq_one_forces
#print axioms OIBridge.KInfFoundations.exists_zero_of_classicallyExposed
#print axioms OIBridge.KInfFoundations.classical_exposed_ncard_le
#print axioms OIBridge.KInfFoundations.qubit_certain_face
#print axioms OIBridge.KInfFoundations.strictConvex_of_kInf1
#print axioms OIBridge.KInfFoundations.kinf1_kernel_core
