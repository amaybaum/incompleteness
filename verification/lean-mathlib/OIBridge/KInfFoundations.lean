/-
  OIBridge/KInfFoundations.lean — round KINF-2: the field-neutral vocabulary of the pre-quantum
  operational completion, corrected, and the elementary lemmas that vocabulary supports.

  Nothing in this module mentions ℂ, a matrix carrier, or the substratum, except §F, which is a
  statement of the imported qubit kinematics. It fixes definitions over a real normed space `V`
  and proves small logical facts. It sources nothing: the module does not derive drivability,
  supporting effects, singleton faces or copy naturality from any OI construction, and it
  contains no reconstruction theorem.

  The corrections to the vocabulary of round KINF-1, which halted:
    * an effect is *proper* on `Ω` when some state gives it a value below one, tested on `Ω`;
      supporting-effect completeness and singleton faces quantify over proper effects only, so the
      unit effect may stay available and changes neither (§B′, `…_insert_iff`);
    * the boundary is read in `Ω` alone (`IsBoundaryState`), not in the topology of `V`, so a body
      that is not full-dimensional in `V` is not excluded for a reason of dimension; an open body
      has no boundary state, so K∞-1 is stated for compact convex bodies;
    * elementary drivability is a group flow of automorphisms of `Ω`, with `J` an automorphism of
      `Ω` and the off-axis clause compared on `Ω` (§C).

  Proved here.
    §A  the state body of a finite observer stage is compact and lies on the unit hyperplane;
    §B′ L1–L3: non-proper effects, and the boundary states certain effects pick out;
    §C′ the semantic controls for drivability: the unit ball of `ℝ³` is drivable (rotations about
        one axis, the half-turn, the cyclic permutation of the axes); the classical bit `[-1, 1]`
        and a one-point body are not;
    §D  Lemma C, `relStrictConvex_of_supporting_singleton`, and its converse,
        `singletonFaces_of_relStrictConvex`: given (SEC), singleton faces are equivalent to
        relative strict convexity of the body, each direction proved separately;
        `relStrictConvex_of_strictConvex`; Lemma D;
    §D′ the semantic controls for (SF) and (SEC): singleton faces hold on every closed ball of a
        strictly convex space with any effect family, and fail on the sup-norm square with its
        full effects; (SEC) holds on the segment `[-1, 1]` with its full effects and fails with
        the unit alone;
    §E  Lemma B and the finite-preparation bound; §E′ Theorem F2;
    §F  the qubit certain face, a theorem of the imported matrix kinematics;
    §G  `KInf1`, hypothesis K∞-1, stated as a definition; it holds for the ball with its full
        effects and fails for the ball with the unit effect alone, so it is a proposition about
        the effect family. It is proved for no physical family.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.Analysis.Convex.Gauge
import Mathlib.Analysis.Convex.Strict
import Mathlib.Analysis.Convex.StrictConvexSpace
import Mathlib.Analysis.Convex.Topology
import Mathlib.Analysis.Normed.Module.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
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

/-- An effect is proper on `Ω` when some state gives it a value below one. The unit effect, and
every effect identically one on `Ω`, is not proper. Properness is tested on `Ω`, not on `V`. -/
def IsProperOn (Ω : Set V) (e : V →ᵃ[ℝ] ℝ) : Prop :=
  ∃ y ∈ Ω, e y < 1

/-- A boundary state of `Ω`, read in `Ω` alone: some state `y` is such that no extension of the
segment from `y` through `x` beyond `x` stays in `Ω`. -/
def IsBoundaryState (Ω : Set V) (x : V) : Prop :=
  x ∈ Ω ∧ ∃ y ∈ Ω, ∀ ε : ℝ, 0 < ε → x + ε • (x - y) ∉ Ω

/-- Supporting-effect completeness (SEC) relative to a family `avail` of available functionals:
every boundary state of `Ω` is certain for some proper available effect. -/
def SupportingEffectComplete (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  ∀ x, IsBoundaryState Ω x → ∃ e ∈ avail, IsEffectOn Ω e ∧ IsProperOn Ω e ∧ e x = 1

/-- Singleton faces (SF): every proper available effect is certain on at most one state. -/
def SingletonFaces (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  ∀ e ∈ avail, IsEffectOn Ω e → IsProperOn Ω e → (certainFace Ω e).Subsingleton

/-- Relative strict convexity: every point strictly between two distinct states is a state and
is not a boundary state. -/
def RelStrictConvex (Ω : Set V) : Prop :=
  ∀ x ∈ Ω, ∀ y ∈ Ω, x ≠ y → ∀ a b : ℝ, 0 < a → 0 < b → a + b = 1 →
    a • x + b • y ∈ Ω ∧ ¬ IsBoundaryState Ω (a • x + b • y)

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


/-! ### §B′ — proper effects and boundary states -/

/-- The point `x + ε • (x - y)` as an affine combination of `x` and `y`. -/
theorem extension_eq (x y : V) (ε : ℝ) : x + ε • (x - y) = (1 + ε) • x + (-ε) • y := by
  rw [smul_sub, add_smul, one_smul, neg_smul]
  abel

/-- **L1.** An effect identically one on `Ω` is not proper on `Ω`. -/
theorem not_isProperOn_of_eq_one {Ω : Set V} {e : V →ᵃ[ℝ] ℝ} (h : ∀ y ∈ Ω, e y = 1) :
    ¬ IsProperOn Ω e := by
  rintro ⟨y, hy, hlt⟩
  rw [h y hy] at hlt
  exact lt_irrefl _ hlt

/-- The unit effect is not proper on any body. -/
theorem not_isProperOn_const_one (Ω : Set V) : ¬ IsProperOn Ω (AffineMap.const ℝ V (1 : ℝ)) :=
  not_isProperOn_of_eq_one (fun _ _ => rfl)

/-- **L2.** An effect certain at a state that is not a boundary state is one on all of `Ω`. -/
theorem eq_one_of_certain_of_not_boundary {Ω : Set V} {e : V →ᵃ[ℝ] ℝ} {x : V}
    (he : IsEffectOn Ω e) (hx : x ∈ Ω) (hnb : ¬ IsBoundaryState Ω x) (hone : e x = 1) :
    ∀ y ∈ Ω, e y = 1 := by
  intro y hy
  have hext : ∃ ε : ℝ, 0 < ε ∧ x + ε • (x - y) ∈ Ω := by
    by_contra hno
    exact hnb ⟨hx, y, hy, fun ε hε hmem => hno ⟨ε, hε, hmem⟩⟩
  obtain ⟨ε, hε, hmem⟩ := hext
  have hval := (he _ hmem).2
  rw [extension_eq, affine_combo e x y (1 + ε) (-ε) (by ring), hone] at hval
  have hy1 := (he y hy).2
  have h2 : 1 ≤ e y := by
    by_contra h
    nlinarith [mul_pos hε (sub_pos.mpr (not_le.mp h))]
  linarith

/-- **L3.** A proper effect certain at a state picks out a boundary state. -/
theorem isBoundaryState_of_certain_proper {Ω : Set V} {e : V →ᵃ[ℝ] ℝ} {x : V}
    (he : IsEffectOn Ω e) (hp : IsProperOn Ω e) (hx : x ∈ Ω) (hone : e x = 1) :
    IsBoundaryState Ω x := by
  by_contra hnb
  exact not_isProperOn_of_eq_one (eq_one_of_certain_of_not_boundary he hx hnb hone) hp

/-- **L6.** Making a non-proper effect available changes neither (SEC) nor (SF). -/
theorem supportingEffectComplete_insert_iff {Ω : Set V} {avail : Set (V →ᵃ[ℝ] ℝ)}
    {u : V →ᵃ[ℝ] ℝ} (hu : ¬ IsProperOn Ω u) :
    SupportingEffectComplete Ω (insert u avail) ↔ SupportingEffectComplete Ω avail := by
  constructor
  · intro h x hx
    obtain ⟨e, he, heff, hp, hone⟩ := h x hx
    rcases he with he | he
    · exact absurd (he ▸ hp) hu
    · exact ⟨e, he, heff, hp, hone⟩
  · intro h x hx
    obtain ⟨e, he, heff, hp, hone⟩ := h x hx
    exact ⟨e, Set.mem_insert_of_mem u he, heff, hp, hone⟩

theorem singletonFaces_insert_iff {Ω : Set V} {avail : Set (V →ᵃ[ℝ] ℝ)}
    {u : V →ᵃ[ℝ] ℝ} (hu : ¬ IsProperOn Ω u) :
    SingletonFaces Ω (insert u avail) ↔ SingletonFaces Ω avail := by
  constructor
  · intro h e he
    exact h e (Set.mem_insert_of_mem u he)
  · intro h e he heff hp
    rcases he with he | he
    · exact absurd (he ▸ hp) hu
    · exact h e he heff hp

/-! ### §C — elementary drivability and copy naturality -/

/-- Elementary drivability of a body `Ω`, stated without a field: a continuous one-parameter
group of affine automorphisms of `V` preserving `Ω`, on which a distinguished involution of `Ω`
(the NOT) lies, together with an automorphism `J` of `Ω` whose conjugate of some flow member
agrees on `Ω` with no flow member. -/
structure ElementaryDrivability (Ω : Set V) where
  flow : ℝ → V ≃ᵃ[ℝ] V
  flow_zero : flow 0 = AffineEquiv.refl ℝ V
  flow_add : ∀ s t, flow (s + t) = (flow t).trans (flow s)
  flow_continuous : Continuous fun q : ℝ × V => flow q.1 q.2
  flow_preserves : ∀ t, ∀ x ∈ Ω, flow t x ∈ Ω
  t₀ : ℝ
  N_involutive : ∀ x ∈ Ω, flow t₀ (flow t₀ x) = x
  N_moves : ∃ x ∈ Ω, flow t₀ x ≠ x
  J : V ≃ᵃ[ℝ] V
  J_preserves : ∀ x ∈ Ω, J x ∈ Ω
  J_symm_preserves : ∀ x ∈ Ω, J.symm x ∈ Ω
  J_off_axis : ∃ t, ∀ s, ∃ x ∈ Ω, J (flow t (J.symm x)) ≠ flow s x

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


/-! ### §C′ — drivability holds on the ball and fails on the bit -/

/-- The Euclidean unit ball of `ℝ³`, cut out by its quadratic form. -/
def ball3 : Set (Fin 3 → ℝ) := {v | v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2 ≤ 1}

theorem mem_ball3 (v : Fin 3 → ℝ) : v ∈ ball3 ↔ v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2 ≤ 1 := Iff.rfl

theorem vec3_ext {v w : Fin 3 → ℝ} (h0 : v 0 = w 0) (h1 : v 1 = w 1) (h2 : v 2 = w 2) :
    v = w := by
  funext i
  fin_cases i
  exacts [h0, h1, h2]

/-- The ball is convex. -/
theorem ball3_convex : Convex ℝ ball3 := by
  intro x hx y hy a b ha hb hab
  rw [mem_ball3] at hx hy ⊢
  simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]
  obtain rfl : b = 1 - a := by linarith
  nlinarith [mul_nonneg (mul_nonneg ha hb) (sq_nonneg (x 0 - y 0)),
    mul_nonneg (mul_nonneg ha hb) (sq_nonneg (x 1 - y 1)),
    mul_nonneg (mul_nonneg ha hb) (sq_nonneg (x 2 - y 2)),
    mul_le_mul_of_nonneg_left hx ha, mul_le_mul_of_nonneg_left hy hb]

/-- The ball is compact. -/
theorem ball3_isCompact : IsCompact ball3 := by
  have hcl : IsClosed ball3 :=
    isClosed_le (f := fun v : Fin 3 → ℝ => v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2) (g := fun _ => (1 : ℝ))
      (by fun_prop) continuous_const
  have hsub : ball3 ⊆ Metric.closedBall (0 : Fin 3 → ℝ) 1 := by
    intro v hv
    rw [mem_ball3] at hv
    rw [Metric.mem_closedBall, dist_zero_right, pi_norm_le_iff_of_nonneg zero_le_one]
    intro i
    have h1 : v i ^ 2 ≤ ∑ j, v j ^ 2 :=
      Finset.single_le_sum (f := fun j => v j ^ 2) (fun j _ => sq_nonneg (v j))
        (Finset.mem_univ i)
    simp only [Fin.sum_univ_three] at h1
    rw [Real.norm_eq_abs, abs_le]
    constructor <;> nlinarith
  exact Metric.isCompact_of_isClosed_isBounded hcl (Metric.isBounded_closedBall.subset hsub)

/-- The rotation of `ℝ³` by the angle `t` about the third axis. -/
noncomputable def rotFun (t : ℝ) (v : Fin 3 → ℝ) : Fin 3 → ℝ :=
  ![Real.cos t * v 0 - Real.sin t * v 1, Real.sin t * v 0 + Real.cos t * v 1, v 2]

theorem rotFun_apply (t : ℝ) (v : Fin 3 → ℝ) :
    rotFun t v 0 = Real.cos t * v 0 - Real.sin t * v 1 ∧
      rotFun t v 1 = Real.sin t * v 0 + Real.cos t * v 1 ∧ rotFun t v 2 = v 2 :=
  ⟨rfl, rfl, rfl⟩

theorem rotFun_zero (v : Fin 3 → ℝ) : rotFun 0 v = v := by
  obtain ⟨a0, a1, a2⟩ := rotFun_apply 0 v
  apply vec3_ext
  · rw [a0, Real.cos_zero, Real.sin_zero]; ring
  · rw [a1, Real.cos_zero, Real.sin_zero]; ring
  · exact a2

theorem rotFun_add (s t : ℝ) (v : Fin 3 → ℝ) : rotFun s (rotFun t v) = rotFun (s + t) v := by
  obtain ⟨a0, a1, a2⟩ := rotFun_apply s (rotFun t v)
  obtain ⟨b0, b1, b2⟩ := rotFun_apply t v
  obtain ⟨c0, c1, c2⟩ := rotFun_apply (s + t) v
  apply vec3_ext
  · rw [a0, b0, b1, c0, Real.cos_add, Real.sin_add]; ring
  · rw [a1, b0, b1, c1, Real.cos_add, Real.sin_add]; ring
  · rw [a2, b2, c2]

/-- A rotation preserves the ball. -/
theorem rotFun_mem_ball3 (t : ℝ) {v : Fin 3 → ℝ} (hv : v ∈ ball3) : rotFun t v ∈ ball3 := by
  obtain ⟨a0, a1, a2⟩ := rotFun_apply t v
  rw [mem_ball3, a0, a1, a2]
  have key : (Real.cos t * v 0 - Real.sin t * v 1) ^ 2 +
      (Real.sin t * v 0 + Real.cos t * v 1) ^ 2 + v 2 ^ 2 = v 0 ^ 2 + v 1 ^ 2 + v 2 ^ 2 := by
    linear_combination (v 0 ^ 2 + v 1 ^ 2) * Real.sin_sq_add_cos_sq t
  rw [key]
  exact hv

/-- The rotation by `t`, as a linear map. -/
noncomputable def rotLin (t : ℝ) : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) where
  toFun := rotFun t
  map_add' v w := by
    obtain ⟨a0, a1, a2⟩ := rotFun_apply t (v + w)
    obtain ⟨b0, b1, b2⟩ := rotFun_apply t v
    obtain ⟨c0, c1, c2⟩ := rotFun_apply t w
    apply vec3_ext <;> simp only [Pi.add_apply, a0, a1, a2, b0, b1, b2, c0, c1, c2] <;> ring
  map_smul' r v := by
    obtain ⟨a0, a1, a2⟩ := rotFun_apply t (r • v)
    obtain ⟨b0, b1, b2⟩ := rotFun_apply t v
    apply vec3_ext <;>
      simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply, a0, a1, a2, b0, b1, b2] <;> ring

/-- The rotation by `t`, as a linear equivalence with inverse the rotation by `-t`. -/
noncomputable def rotEquiv (t : ℝ) : (Fin 3 → ℝ) ≃ₗ[ℝ] (Fin 3 → ℝ) :=
  { rotLin t with
    invFun := rotFun (-t)
    left_inv := fun v => by
      show rotFun (-t) (rotFun t v) = v
      rw [rotFun_add, neg_add_cancel, rotFun_zero]
    right_inv := fun v => by
      show rotFun t (rotFun (-t) v) = v
      rw [rotFun_add, add_neg_cancel, rotFun_zero] }

/-- The rotation by `t`, as an affine automorphism of `ℝ³`. -/
noncomputable def rot3 (t : ℝ) : (Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ) := (rotEquiv t).toAffineEquiv

theorem rot3_apply (t : ℝ) (v : Fin 3 → ℝ) : rot3 t v = rotFun t v := rfl

/-- The cyclic permutation of the coordinates, `(x, y, z) ↦ (z, x, y)`. -/
noncomputable def cycEquiv : (Fin 3 → ℝ) ≃ₗ[ℝ] (Fin 3 → ℝ) where
  toFun v := ![v 2, v 0, v 1]
  invFun v := ![v 1, v 2, v 0]
  map_add' v w := by apply vec3_ext <;> rfl
  map_smul' r v := by apply vec3_ext <;> rfl
  left_inv v := by apply vec3_ext <;> rfl
  right_inv v := by apply vec3_ext <;> rfl

/-- The cyclic permutation, as an affine automorphism of `ℝ³`. -/
noncomputable def cyc3 : (Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ) := cycEquiv.toAffineEquiv

theorem cyc3_apply (v : Fin 3 → ℝ) : cyc3 v 0 = v 2 ∧ cyc3 v 1 = v 0 ∧ cyc3 v 2 = v 1 :=
  ⟨rfl, rfl, rfl⟩

theorem cyc3_symm_apply (v : Fin 3 → ℝ) :
    cyc3.symm v 0 = v 1 ∧ cyc3.symm v 1 = v 2 ∧ cyc3.symm v 2 = v 0 :=
  ⟨rfl, rfl, rfl⟩

theorem cyc3_mem_ball3 {v : Fin 3 → ℝ} (hv : v ∈ ball3) : cyc3 v ∈ ball3 := by
  obtain ⟨c0, c1, c2⟩ := cyc3_apply v
  rw [mem_ball3, c0, c1, c2]
  rw [mem_ball3] at hv
  linarith

theorem cyc3_symm_mem_ball3 {v : Fin 3 → ℝ} (hv : v ∈ ball3) : cyc3.symm v ∈ ball3 := by
  obtain ⟨c0, c1, c2⟩ := cyc3_symm_apply v
  rw [mem_ball3, c0, c1, c2]
  rw [mem_ball3] at hv
  linarith

/-- **Positive control for drivability.** The ball is drivable: the rotations about the third
axis form the flow, the half-turn is the NOT, and the cyclic permutation of the axes carries the
flow off itself on the ball. -/
noncomputable def ball3Drive : ElementaryDrivability ball3 where
  flow := rot3
  flow_zero := AffineEquiv.ext fun v => by rw [rot3_apply, rotFun_zero, AffineEquiv.refl_apply]
  flow_add s t := AffineEquiv.ext fun v => by
    simp only [AffineEquiv.trans_apply, rot3_apply, rotFun_add]
  flow_continuous := by
    refine continuous_pi fun i => ?_
    fin_cases i
    · show Continuous fun q : ℝ × (Fin 3 → ℝ) => Real.cos q.1 * q.2 0 - Real.sin q.1 * q.2 1
      fun_prop
    · show Continuous fun q : ℝ × (Fin 3 → ℝ) => Real.sin q.1 * q.2 0 + Real.cos q.1 * q.2 1
      fun_prop
    · show Continuous fun q : ℝ × (Fin 3 → ℝ) => q.2 2
      fun_prop
  flow_preserves t _ hv := rotFun_mem_ball3 t hv
  t₀ := Real.pi
  N_involutive x _ := by
    simp only [rot3_apply]
    obtain ⟨a0, a1, a2⟩ := rotFun_apply Real.pi (rotFun Real.pi x)
    obtain ⟨b0, b1, b2⟩ := rotFun_apply Real.pi x
    apply vec3_ext
    · rw [a0, b0, b1, Real.cos_pi, Real.sin_pi]; ring
    · rw [a1, b0, b1, Real.cos_pi, Real.sin_pi]; ring
    · rw [a2, b2]
  N_moves := ⟨![1, 0, 0], by show (1 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2 ≤ 1; norm_num, fun h => by
    have h0 : rot3 Real.pi ![1, 0, 0] 0 = (![1, 0, 0] : Fin 3 → ℝ) 0 := congrFun h 0
    change Real.cos Real.pi * 1 - Real.sin Real.pi * 0 = 1 at h0
    rw [Real.cos_pi, Real.sin_pi] at h0
    norm_num at h0⟩
  J := cyc3
  J_preserves _ hv := cyc3_mem_ball3 hv
  J_symm_preserves _ hv := cyc3_symm_mem_ball3 hv
  J_off_axis := ⟨Real.pi, fun s => ⟨![0, 0, 1],
    by show (0 : ℝ) ^ 2 + 0 ^ 2 + 1 ^ 2 ≤ 1; norm_num, fun h => by
      have h2 : cyc3 (rot3 Real.pi (cyc3.symm ![0, 0, 1])) 2 = rot3 s ![0, 0, 1] 2 :=
        congrFun h 2
      change Real.sin Real.pi * 0 + Real.cos Real.pi * 1 = 1 at h2
      rw [Real.sin_pi, Real.cos_pi] at h2
      norm_num at h2⟩⟩

/-- The ball is drivable. -/
theorem ball3_drivable : Nonempty (ElementaryDrivability ball3) := ⟨ball3Drive⟩

/-- An affine automorphism of the line is `x ↦ g 0 + g.linear 1 * x`. -/
theorem affineEquiv_real_apply (g : ℝ ≃ᵃ[ℝ] ℝ) (x : ℝ) : g x = g 0 + g.linear 1 * x := by
  have h := g.map_vadd 0 x
  simp only [vadd_eq_add, add_zero] at h
  have hl : g.linear x = g.linear 1 * x := by
    have := map_smul g.linear x (1 : ℝ)
    simp only [smul_eq_mul, mul_one] at this
    rw [this, mul_comm]
  rw [h, hl, add_comm]

/-- Two mutually inverse affine maps of the line that both preserve `[-1, 1]` are `±` the
identity. -/
theorem bit_aux {a b c d : ℝ} (h1 : -1 ≤ a + b * 1 ∧ a + b * 1 ≤ 1)
    (h2 : -1 ≤ a + b * -1 ∧ a + b * -1 ≤ 1) (h3 : -1 ≤ c + d * 1 ∧ c + d * 1 ≤ 1)
    (h4 : -1 ≤ c + d * -1 ∧ c + d * -1 ≤ 1) (h5 : a + b * (c + d * 0) = 0)
    (h6 : a + b * (c + d * 1) = 1) : a = 0 ∧ b * b = 1 := by
  obtain ⟨h1l, h1u⟩ := h1
  obtain ⟨h2l, h2u⟩ := h2
  obtain ⟨h3l, h3u⟩ := h3
  obtain ⟨h4l, h4u⟩ := h4
  have hbd : b * d = 1 := by linear_combination h6 - h5
  have hab : a ^ 2 + b ^ 2 ≤ 1 := by
    nlinarith [mul_nonneg (by linarith : (0 : ℝ) ≤ 1 - (a + b)) (by linarith : (0 : ℝ) ≤ 1 + (a + b)),
      mul_nonneg (by linarith : (0 : ℝ) ≤ 1 - (a - b)) (by linarith : (0 : ℝ) ≤ 1 + (a - b))]
  have hcd : c ^ 2 + d ^ 2 ≤ 1 := by
    nlinarith [mul_nonneg (by linarith : (0 : ℝ) ≤ 1 - (c + d)) (by linarith : (0 : ℝ) ≤ 1 + (c + d)),
      mul_nonneg (by linarith : (0 : ℝ) ≤ 1 - (c - d)) (by linarith : (0 : ℝ) ≤ 1 + (c - d))]
  have hbd2 : b ^ 2 * d ^ 2 = 1 := by rw [← mul_pow, hbd]; norm_num
  have hb : 1 ≤ b ^ 2 := by
    nlinarith [mul_nonneg (sq_nonneg b) (by nlinarith [sq_nonneg c] : (0 : ℝ) ≤ 1 - d ^ 2)]
  have ha2 : a ^ 2 ≤ 0 := by linarith
  have ha : a = 0 := (pow_eq_zero_iff two_ne_zero).mp (le_antisymm ha2 (sq_nonneg a))
  exact ⟨ha, by nlinarith [sq_nonneg a]⟩

/-- **Negative control for drivability.** The classical bit `[-1, 1]` is not drivable: the flow
member at half the NOT's parameter is `±` the identity on the line, so the NOT, its square, is
the identity and moves nothing. -/
theorem not_drivable_Icc : IsEmpty (ElementaryDrivability (Set.Icc (-1 : ℝ) 1)) := by
  refine ⟨fun D => ?_⟩
  obtain ⟨x, -, hmove⟩ := D.N_moves
  have hinv : ∀ y, D.flow (D.t₀ / 2) (D.flow (-(D.t₀ / 2)) y) = y := by
    intro y
    have h1 := congrArg (fun f : ℝ ≃ᵃ[ℝ] ℝ => f y) (D.flow_add (D.t₀ / 2) (-(D.t₀ / 2)))
    simp only [AffineEquiv.trans_apply, add_neg_cancel, D.flow_zero,
      AffineEquiv.refl_apply] at h1
    exact h1.symm
  have hsq : D.flow D.t₀ x = D.flow (D.t₀ / 2) (D.flow (D.t₀ / 2) x) := by
    have h1 := congrArg (fun f : ℝ ≃ᵃ[ℝ] ℝ => f x) (D.flow_add (D.t₀ / 2) (D.t₀ / 2))
    simp only [AffineEquiv.trans_apply, add_halves] at h1
    exact h1
  have hp : (1 : ℝ) ∈ Set.Icc (-1 : ℝ) 1 := ⟨by norm_num, le_rfl⟩
  have hm : (-1 : ℝ) ∈ Set.Icc (-1 : ℝ) 1 := ⟨le_rfl, by norm_num⟩
  have hh := affineEquiv_real_apply (D.flow (D.t₀ / 2))
  have hk := affineEquiv_real_apply (D.flow (-(D.t₀ / 2)))
  have e1 := D.flow_preserves (D.t₀ / 2) 1 hp
  have e2 := D.flow_preserves (D.t₀ / 2) (-1) hm
  have e3 := D.flow_preserves (-(D.t₀ / 2)) 1 hp
  have e4 := D.flow_preserves (-(D.t₀ / 2)) (-1) hm
  have i0 := hinv 0
  have i1 := hinv 1
  rw [hh 1, Set.mem_Icc] at e1
  rw [hh (-1), Set.mem_Icc] at e2
  rw [hk 1, Set.mem_Icc] at e3
  rw [hk (-1), Set.mem_Icc] at e4
  rw [hk 0, hh] at i0
  rw [hk 1, hh] at i1
  obtain ⟨ha, hb⟩ := bit_aux e1 e2 e3 e4 i0 i1
  apply hmove
  rw [hsq, hh (D.flow (D.t₀ / 2) x), hh x, ha]
  linear_combination x * hb

/-- A one-point body is not drivable: nothing on it can move. -/
theorem not_drivable_singleton (x : V) : IsEmpty (ElementaryDrivability ({x} : Set V)) := by
  refine ⟨fun D => ?_⟩
  obtain ⟨y, hy, hmove⟩ := D.N_moves
  rw [Set.mem_singleton_iff] at hy
  subst hy
  exact hmove (D.flow_preserves D.t₀ y (Set.mem_singleton y))

/-! ### §D — Lemma C, its converse, and Lemma D -/

/-- **Lemma C (L4).** A convex body with supporting-effect completeness and singleton faces is
relatively strictly convex. -/
theorem relStrictConvex_of_supporting_singleton {Ω : Set V} {avail : Set (V →ᵃ[ℝ] ℝ)}
    (hconv : Convex ℝ Ω) (hSEC : SupportingEffectComplete Ω avail)
    (hSF : SingletonFaces Ω avail) : RelStrictConvex Ω := by
  intro x hx y hy hxy a b ha hb hab
  refine ⟨hconv hx hy ha.le hb.le hab, fun hbd => ?_⟩
  obtain ⟨e, he, heff, hprop, hone⟩ := hSEC _ hbd
  rw [affine_combo e x y a b hab] at hone
  have hex := (heff x hx).2
  have hey := (heff y hy).2
  have hx1 : e x = 1 := by nlinarith
  have hy1 : e y = 1 := by nlinarith
  exact hxy (hSF e he heff hprop ⟨hx, hx1⟩ ⟨hy, hy1⟩)

/-- **L5, the converse.** A relatively strictly convex body has singleton faces for every
effect family. -/
theorem singletonFaces_of_relStrictConvex {Ω : Set V} (avail : Set (V →ᵃ[ℝ] ℝ))
    (h : RelStrictConvex Ω) : SingletonFaces Ω avail := by
  intro e _ heff hprop x hx y hy
  by_contra hxy
  have hz := h x hx.1 y hy.1 hxy (1 / 2) (1 / 2) (by norm_num) (by norm_num) (by norm_num)
  have hzone : e ((1 / 2 : ℝ) • x + (1 / 2 : ℝ) • y) = 1 := by
    rw [affine_combo e x y _ _ (by norm_num), hx.2, hy.2]
    norm_num
  exact not_isProperOn_of_eq_one (eq_one_of_certain_of_not_boundary heff hz.1 hz.2 hzone) hprop

/-- A point of the interior of `Ω`, in the topology of `V`, is not a boundary state. -/
theorem not_isBoundaryState_of_mem_interior {Ω : Set V} {z : V} (hint : z ∈ interior Ω) :
    ¬ IsBoundaryState Ω z := by
  rintro ⟨_, w, _, hout⟩
  have hnhds : Ω ∈ nhds z := mem_interior_iff_mem_nhds.mp hint
  have hcont : Continuous fun ε : ℝ => z + ε • (z - w) :=
    continuous_const.add (continuous_id.smul continuous_const)
  have hev : ∀ᶠ ε in nhds (0 : ℝ), z + ε • (z - w) ∈ Ω := by
    have ht := hcont.tendsto 0
    simp only [zero_smul, add_zero] at ht
    exact ht hnhds
  obtain ⟨δ, hδ, hball⟩ := Metric.eventually_nhds_iff.mp hev
  refine hout (δ / 2) (by linarith) (hball ?_)
  rw [Real.dist_eq, sub_zero, abs_of_pos (by linarith)]
  linarith

/-- **L7.** A strictly convex body, in the topology of `V`, is relatively strictly convex. -/
theorem relStrictConvex_of_strictConvex {Ω : Set V} (h : StrictConvex ℝ Ω) :
    RelStrictConvex Ω := by
  intro x hx y hy hxy a b ha hb hab
  have hint := h hx hy hxy ha hb hab
  exact ⟨interior_subset hint, not_isBoundaryState_of_mem_interior hint⟩

/-- An open body has no boundary state, so (SEC) holds on it for every family. This is why the
premises of K∞-1 carry compactness. -/
theorem supportingEffectComplete_of_isOpen {Ω : Set V} (hΩ : IsOpen Ω)
    (avail : Set (V →ᵃ[ℝ] ℝ)) : SupportingEffectComplete Ω avail := by
  intro x hx
  exact absurd hx (not_isBoundaryState_of_mem_interior (by rw [hΩ.interior_eq]; exact hx.1))

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

/-! ### §D′ — the semantic controls -/

/-- **L8, positive control.** On a closed ball of a strictly convex space, singleton faces hold
for every effect family, the full effects included. -/
theorem singletonFaces_closedBall [StrictConvexSpace ℝ V] (x : V) (r : ℝ)
    (avail : Set (V →ᵃ[ℝ] ℝ)) : SingletonFaces (Metric.closedBall x r) avail :=
  singletonFaces_of_relStrictConvex avail
    (relStrictConvex_of_strictConvex (strictConvex_closedBall ℝ x r))

/-- The affine functional `t ↦ a + b t` on `ℝ`. -/
noncomputable def affR (a b : ℝ) : ℝ →ᵃ[ℝ] ℝ :=
  AffineMap.const ℝ ℝ a + (b • LinearMap.id : ℝ →ₗ[ℝ] ℝ).toAffineMap

theorem affR_apply (a b t : ℝ) : affR a b t = a + b * t := by
  simp [affR]

/-- The state `1` of the segment `[-1, 1]` is a boundary state. -/
theorem isBoundaryState_Icc_one : IsBoundaryState (Set.Icc (-1 : ℝ) 1) 1 := by
  refine ⟨⟨by norm_num, le_rfl⟩, -1, ⟨le_rfl, by norm_num⟩, fun ε hε h => ?_⟩
  have h2 := h.2
  simp only [smul_eq_mul] at h2
  linarith

/-- **L10, negative control.** With the unit effect alone, (SEC) fails on the segment. -/
theorem not_supportingEffectComplete_unit :
    ¬ SupportingEffectComplete (Set.Icc (-1 : ℝ) 1) {AffineMap.const ℝ ℝ (1 : ℝ)} := by
  intro h
  obtain ⟨e, he, -, hp, -⟩ := h 1 isBoundaryState_Icc_one
  rw [Set.mem_singleton_iff] at he
  subst he
  exact not_isProperOn_const_one _ hp

/-- **Positive control for (SEC).** With its full effects, the segment `[-1, 1]` has
supporting-effect completeness. -/
theorem supportingEffectComplete_Icc :
    SupportingEffectComplete (Set.Icc (-1 : ℝ) 1) (fullEffects (Set.Icc (-1 : ℝ) 1)) := by
  rintro x ⟨⟨hx1, hx2⟩, y, ⟨hy1, hy2⟩, hout⟩
  rcases eq_or_lt_of_le hx2 with h1 | h1
  · have heff : IsEffectOn (Set.Icc (-1 : ℝ) 1) (affR (1 / 2) (1 / 2)) := by
      intro t ht
      rw [affR_apply]
      constructor <;> linarith [ht.1, ht.2]
    refine ⟨affR (1 / 2) (1 / 2), heff, heff, ⟨-1, ⟨le_rfl, by norm_num⟩, ?_⟩, ?_⟩
    · rw [affR_apply]; norm_num
    · rw [affR_apply, h1]; norm_num
  rcases eq_or_lt_of_le hx1 with h2 | h2
  · have heff : IsEffectOn (Set.Icc (-1 : ℝ) 1) (affR (1 / 2) (-1 / 2)) := by
      intro t ht
      rw [affR_apply]
      constructor <;> linarith [ht.1, ht.2]
    refine ⟨affR (1 / 2) (-1 / 2), heff, heff, ⟨1, ⟨by norm_num, le_rfl⟩, ?_⟩, ?_⟩
    · rw [affR_apply]; norm_num
    · rw [affR_apply, ← h2]; norm_num
  exfalso
  have hm : 0 < min (1 - x) (x + 1) := lt_min (by linarith) (by linarith)
  apply hout (min (1 - x) (x + 1) / 4) (by positivity)
  have hle1 := min_le_left (1 - x) (x + 1)
  have hle2 := min_le_right (1 - x) (x + 1)
  simp only [smul_eq_mul]
  constructor <;> nlinarith

/-- The effect `v ↦ (1 + v 0)/2` on the plane. -/
noncomputable def squareEdgeEffect : (Fin 2 → ℝ) →ᵃ[ℝ] ℝ :=
  AffineMap.const ℝ (Fin 2 → ℝ) (1 / 2 : ℝ) +
    ((1 / 2 : ℝ) • (LinearMap.proj 0 : (Fin 2 → ℝ) →ₗ[ℝ] ℝ)).toAffineMap

theorem squareEdgeEffect_apply (v : Fin 2 → ℝ) : squareEdgeEffect v = 1 / 2 + v 0 / 2 := by
  simp [squareEdgeEffect]
  ring

/-- **L9, negative control.** The square (the unit ball of the sup norm on the plane) does not
have singleton faces with its full effects: one edge effect is certain on a whole edge. -/
theorem not_singletonFaces_square :
    ¬ SingletonFaces (Metric.closedBall (0 : Fin 2 → ℝ) 1)
      (fullEffects (Metric.closedBall (0 : Fin 2 → ℝ) 1)) := by
  have hcoord : ∀ v ∈ Metric.closedBall (0 : Fin 2 → ℝ) 1, |v 0| ≤ 1 := by
    intro v hv
    rw [Metric.mem_closedBall, dist_zero_right] at hv
    have := norm_le_pi_norm v 0
    rw [Real.norm_eq_abs] at this
    linarith
  have hmem : ∀ v : Fin 2 → ℝ, |v 0| ≤ 1 → |v 1| ≤ 1 →
      v ∈ Metric.closedBall (0 : Fin 2 → ℝ) 1 := by
    intro v h0 h1
    rw [Metric.mem_closedBall, dist_zero_right, pi_norm_le_iff_of_nonneg zero_le_one]
    intro i
    fin_cases i
    · simpa [Real.norm_eq_abs] using h0
    · simpa [Real.norm_eq_abs] using h1
  have heff : IsEffectOn (Metric.closedBall (0 : Fin 2 → ℝ) 1) squareEdgeEffect := by
    intro v hv
    rw [squareEdgeEffect_apply]
    have := abs_le.mp (hcoord v hv)
    constructor <;> linarith [this.1, this.2]
  intro h
  have hp : IsProperOn (Metric.closedBall (0 : Fin 2 → ℝ) 1) squareEdgeEffect :=
    ⟨0, Metric.mem_closedBall_self zero_le_one, by rw [squareEdgeEffect_apply]; norm_num⟩
  have hA : (![1, 1] : Fin 2 → ℝ) ∈
      certainFace (Metric.closedBall (0 : Fin 2 → ℝ) 1) squareEdgeEffect :=
    ⟨hmem _ (by simp) (by simp), by rw [squareEdgeEffect_apply]; norm_num⟩
  have hB : (![1, -1] : Fin 2 → ℝ) ∈
      certainFace (Metric.closedBall (0 : Fin 2 → ℝ) 1) squareEdgeEffect :=
    ⟨hmem _ (by simp) (by simp), by rw [squareEdgeEffect_apply]; norm_num⟩
  have hne := h squareEdgeEffect heff heff hp hA hB
  have := congrFun hne 1
  norm_num at this

/-- The square is not relatively strictly convex: L5 with `not_singletonFaces_square`. -/
theorem not_relStrictConvex_square :
    ¬ RelStrictConvex (Metric.closedBall (0 : Fin 2 → ℝ) 1) := fun h =>
  not_singletonFaces_square (singletonFaces_of_relStrictConvex _ h)

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
theorem FiniteStage.exposed_le_card (S : FiniteStage)
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
facet. The response effects are stated as functions on `Fin N → ℝ`, without the
affine-map structure of §B, since the bound needs only the form `∑ cᵢ pᵢ`. -/

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


/-! ### §G — hypothesis K∞-1, as a statement, and its controls -/

/-- **Hypothesis K∞-1**, stated and not proved: a compact convex body admitting an elementary
drive has supporting-effect completeness relative to the available effects. This is the
field-neutral Naimark step. Compactness enters because an open body has no boundary state
(`supportingEffectComplete_of_isOpen`). The module proves K∞-1 for no physical family; it is an
open target. -/
def KInf1 (Ω : Set V) (avail : Set (V →ᵃ[ℝ] ℝ)) : Prop :=
  IsCompact Ω → Convex ℝ Ω → Nonempty (ElementaryDrivability Ω) →
    SupportingEffectComplete Ω avail

/-- What K∞-1 buys when it holds: with singleton faces, a compact convex drivable body is
relatively strictly convex. -/
theorem relStrictConvex_of_kInf1 {Ω : Set V} {avail : Set (V →ᵃ[ℝ] ℝ)}
    (hcomp : IsCompact Ω) (hconv : Convex ℝ Ω) (hK : KInf1 Ω avail)
    (hD : Nonempty (ElementaryDrivability Ω)) (hSF : SingletonFaces Ω avail) :
    RelStrictConvex Ω :=
  relStrictConvex_of_supporting_singleton hconv (hK hcomp hconv hD) hSF

/-- The effect `v ↦ (1 + u · v)/2` on `ℝ³`. -/
noncomputable def ballEffect (u : Fin 3 → ℝ) : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ :=
  AffineMap.const ℝ (Fin 3 → ℝ) (1 / 2 : ℝ) +
    ((1 / 2 : ℝ) • (u 0 • LinearMap.proj 0 + u 1 • LinearMap.proj 1 + u 2 • LinearMap.proj 2 :
      (Fin 3 → ℝ) →ₗ[ℝ] ℝ)).toAffineMap

theorem ballEffect_apply (u v : Fin 3 → ℝ) :
    ballEffect u v = 1 / 2 + (u 0 * v 0 + u 1 * v 1 + u 2 * v 2) / 2 := by
  simp [ballEffect] <;> ring

/-- A step from a state of the ball off its sphere, by a sixteenth of the gap, stays in it. -/
theorem ball3_extend {x0 x1 x2 y0 y1 y2 ε : ℝ} (hx : x0 ^ 2 + x1 ^ 2 + x2 ^ 2 ≤ 1)
    (hy : y0 ^ 2 + y1 ^ 2 + y2 ^ 2 ≤ 1) (hε : 0 < ε)
    (hε' : 16 * ε = 1 - (x0 ^ 2 + x1 ^ 2 + x2 ^ 2)) :
    (x0 + ε * (x0 - y0)) ^ 2 + (x1 + ε * (x1 - y1)) ^ 2 + (x2 + ε * (x2 - y2)) ^ 2 ≤ 1 := by
  have hT : (x0 - y0) ^ 2 + (x1 - y1) ^ 2 + (x2 - y2) ^ 2 ≤ 4 := by
    nlinarith [sq_nonneg (x0 + y0), sq_nonneg (x1 + y1), sq_nonneg (x2 + y2)]
  have hS : x0 * (x0 - y0) + x1 * (x1 - y1) + x2 * (x2 - y2) ≤ 2 := by
    nlinarith [sq_nonneg (x0 + y0), sq_nonneg (x1 + y1), sq_nonneg (x2 + y2)]
  have hε1 : ε ≤ 1 / 16 := by nlinarith [sq_nonneg x0, sq_nonneg x1, sq_nonneg x2]
  have h1 := mul_le_mul_of_nonneg_left hS hε.le
  have h2 := mul_le_mul_of_nonneg_left hT (mul_nonneg hε.le hε.le)
  have h3 := mul_le_mul_of_nonneg_left hε1 hε.le
  nlinarith [h1, h2, h3]

/-- **Positive control for (SEC) on a drivable body.** The ball has supporting-effect
completeness with its full effects: a boundary state lies on the unit sphere, and the effect
`v ↦ (1 + x · v)/2` is a proper effect certain there. -/
theorem supportingEffectComplete_ball3 : SupportingEffectComplete ball3 (fullEffects ball3) := by
  rintro x ⟨hx, y, hy, hout⟩
  rw [mem_ball3] at hx hy
  have hsph : x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2 = 1 := by
    by_contra hne
    have hlt := lt_of_le_of_ne hx hne
    apply hout ((1 - (x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2)) / 16) (by linarith)
    rw [mem_ball3]
    simp only [Pi.add_apply, Pi.smul_apply, Pi.sub_apply, smul_eq_mul]
    exact ball3_extend hx hy (by linarith) (by ring)
  have heff : IsEffectOn ball3 (ballEffect x) := by
    intro v hv
    rw [mem_ball3] at hv
    rw [ballEffect_apply]
    constructor <;> nlinarith [sq_nonneg (x 0 - v 0), sq_nonneg (x 1 - v 1),
      sq_nonneg (x 2 - v 2), sq_nonneg (x 0 + v 0), sq_nonneg (x 1 + v 1), sq_nonneg (x 2 + v 2)]
  refine ⟨ballEffect x, heff, heff, ⟨0, ?_, ?_⟩, ?_⟩
  · rw [mem_ball3]; norm_num
  · rw [ballEffect_apply]; norm_num
  · rw [ballEffect_apply]; linear_combination hsph / 2

/-- **K∞-1 holds non-vacuously** for the ball with its full effects: the ball is compact, convex
and drivable, and has supporting-effect completeness. -/
theorem kInf1_ball3_full : KInf1 ball3 (fullEffects ball3) :=
  fun _ _ _ => supportingEffectComplete_ball3

/-- The state `(1, 0, 0)` of the ball is a boundary state. -/
theorem isBoundaryState_ball3 : IsBoundaryState ball3 ![1, 0, 0] := by
  refine ⟨by show (1 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2 ≤ 1; norm_num, ![-1, 0, 0],
    by show (-1 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2 ≤ 1; norm_num, fun ε hε h => ?_⟩
  change (1 + ε * (1 - -1)) ^ 2 + (0 + ε * (0 - 0)) ^ 2 + (0 + ε * (0 - 0)) ^ 2 ≤ 1 at h
  nlinarith

/-- **K∞-1 fails** for the ball with the unit effect alone: the ball is compact, convex and
drivable, and its boundary state `(1, 0, 0)` is certain for no proper available effect. So K∞-1
is a proposition about the effect family, not a consequence of the body. -/
theorem not_kInf1_ball3_unit : ¬ KInf1 ball3 {AffineMap.const ℝ (Fin 3 → ℝ) (1 : ℝ)} := by
  intro hK
  obtain ⟨e, he, -, hp, -⟩ := hK ball3_isCompact ball3_convex ball3_drivable _ isBoundaryState_ball3
  rw [Set.mem_singleton_iff] at he
  subst he
  exact not_isProperOn_const_one _ hp

end KInfFoundations
end OIBridge

#print axioms OIBridge.KInfFoundations.FiniteStage.states_isCompact
#print axioms OIBridge.KInfFoundations.FiniteStage.states_isClosed
#print axioms OIBridge.KInfFoundations.FiniteStage.states_convex
#print axioms OIBridge.KInfFoundations.FiniteStage.states_unit
#print axioms OIBridge.KInfFoundations.affine_combo
#print axioms OIBridge.KInfFoundations.affine_reflect
#print axioms OIBridge.KInfFoundations.convex_affine_le
#print axioms OIBridge.KInfFoundations.extension_eq
#print axioms OIBridge.KInfFoundations.not_isProperOn_of_eq_one
#print axioms OIBridge.KInfFoundations.not_isProperOn_const_one
#print axioms OIBridge.KInfFoundations.eq_one_of_certain_of_not_boundary
#print axioms OIBridge.KInfFoundations.isBoundaryState_of_certain_proper
#print axioms OIBridge.KInfFoundations.supportingEffectComplete_insert_iff
#print axioms OIBridge.KInfFoundations.singletonFaces_insert_iff
#print axioms OIBridge.KInfFoundations.copyNatural_refl_iff
#print axioms OIBridge.KInfFoundations.copyNatural_iff_apply
#print axioms OIBridge.KInfFoundations.mem_ball3
#print axioms OIBridge.KInfFoundations.vec3_ext
#print axioms OIBridge.KInfFoundations.ball3_convex
#print axioms OIBridge.KInfFoundations.ball3_isCompact
#print axioms OIBridge.KInfFoundations.rotFun_apply
#print axioms OIBridge.KInfFoundations.rotFun_zero
#print axioms OIBridge.KInfFoundations.rotFun_add
#print axioms OIBridge.KInfFoundations.rotFun_mem_ball3
#print axioms OIBridge.KInfFoundations.rot3_apply
#print axioms OIBridge.KInfFoundations.cyc3_apply
#print axioms OIBridge.KInfFoundations.cyc3_symm_apply
#print axioms OIBridge.KInfFoundations.cyc3_mem_ball3
#print axioms OIBridge.KInfFoundations.cyc3_symm_mem_ball3
#print axioms OIBridge.KInfFoundations.ball3_drivable
#print axioms OIBridge.KInfFoundations.affineEquiv_real_apply
#print axioms OIBridge.KInfFoundations.bit_aux
#print axioms OIBridge.KInfFoundations.not_drivable_Icc
#print axioms OIBridge.KInfFoundations.not_drivable_singleton
#print axioms OIBridge.KInfFoundations.relStrictConvex_of_supporting_singleton
#print axioms OIBridge.KInfFoundations.singletonFaces_of_relStrictConvex
#print axioms OIBridge.KInfFoundations.not_isBoundaryState_of_mem_interior
#print axioms OIBridge.KInfFoundations.relStrictConvex_of_strictConvex
#print axioms OIBridge.KInfFoundations.supportingEffectComplete_of_isOpen
#print axioms OIBridge.KInfFoundations.card_le_two_of_centrallySymmetric
#print axioms OIBridge.KInfFoundations.card_le_two_of_centrallySymmetric_full
#print axioms OIBridge.KInfFoundations.singletonFaces_closedBall
#print axioms OIBridge.KInfFoundations.affR_apply
#print axioms OIBridge.KInfFoundations.isBoundaryState_Icc_one
#print axioms OIBridge.KInfFoundations.not_supportingEffectComplete_unit
#print axioms OIBridge.KInfFoundations.supportingEffectComplete_Icc
#print axioms OIBridge.KInfFoundations.squareEdgeEffect_apply
#print axioms OIBridge.KInfFoundations.not_singletonFaces_square
#print axioms OIBridge.KInfFoundations.not_relStrictConvex_square
#print axioms OIBridge.KInfFoundations.eq_closedBall_of_frontier_subset_sphere
#print axioms OIBridge.KInfFoundations.exists_vertex_of_certain
#print axioms OIBridge.KInfFoundations.exposed_mem_range
#print axioms OIBridge.KInfFoundations.exposed_ncard_le
#print axioms OIBridge.KInfFoundations.FiniteStage.exposed_le_card
#print axioms OIBridge.KInfFoundations.response_eq_one_forces
#print axioms OIBridge.KInfFoundations.mem_of_classicallyExposed
#print axioms OIBridge.KInfFoundations.exists_zero_of_classicallyExposed
#print axioms OIBridge.KInfFoundations.classical_exposed_ncard_le
#print axioms OIBridge.KInfFoundations.qubit_certain_face
#print axioms OIBridge.KInfFoundations.relStrictConvex_of_kInf1
#print axioms OIBridge.KInfFoundations.ballEffect_apply
#print axioms OIBridge.KInfFoundations.ball3_extend
#print axioms OIBridge.KInfFoundations.supportingEffectComplete_ball3
#print axioms OIBridge.KInfFoundations.kInf1_ball3_full
#print axioms OIBridge.KInfFoundations.isBoundaryState_ball3
#print axioms OIBridge.KInfFoundations.not_kInf1_ball3_unit
