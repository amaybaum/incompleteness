/-
  OIBridge/BridgeReach.lean — design module of the research thread `research/bridge`
  (round 3, node B13). Not certified. Built on the disposable branch `dev-bridge/r3-reach` only;
  not for merge.

  The reachability theorem B7-1 of the thread (NOTES-B7): every compact group of unitary and
  antiunitary conjugations of the pair `ℂ² ⊗ ℂ²` whose identity component is abelian misses some
  pure state with its orbit of pure products.

  Stated here (definitions, not proved):
    §B  `ReachUnitary`: closed subgroups `H` of `U(4)` with commutative identity component.
        `ReachAnti`: the same with an antiunitary coset `H κ`, `κ = K ∘ conj`, under the two
        conditions that make `H ∪ H κ` a group (`K conj(h) K* ∈ H`, `K conj(K) ∈ H`).
        The conclusion: a vector `v ≠ 0` that no element of the group carries to a product.

  Proved here:
    §A  products have vanishing coefficient determinant (`prodDet_kron2`); the determinant is
        quadratic along lines (`prodDet_add_smul`); conjugation fixes natural-number parameters
        (`conjV_add_natSmul`);
    §C  the avoidance lemma: finitely many functions on pair vectors, each nonzero somewhere and
        quadratic along every line `v + n w` (`n : ℕ`), have a common non-root (`exists_avoid`);
    §D  the finite case of both statements: for a finite subgroup `H` (and any `K`) the conclusion
        holds, with no hypothesis on the identity component or on `K` (`reachUnitary_finite`,
        `reachAnti_finite`); hence each statement reduces to its infinite subgroups
        (`reachUnitary_of_infinite`, `reachAnti_of_infinite`);
    §E  controls: an explicit vector avoids products under `1` and `CNOT` (`ctl_cnot_witness`,
        `ctl_avoids`); the zero matrix is quadratic along lines and has no non-root
        (`ctl_counter_zero`); two complementary step functions, each nonzero somewhere, have no
        common non-root (`ctl_counter_step`).

  Nothing here proves B7-1 for subgroups of positive dimension (NOTES-B7 §1, §2, §4).

  Kernel check (dev branch):  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.LinearAlgebra.UnitaryGroup
import Mathlib.Analysis.Complex.Basic
import Mathlib.Topology.Instances.Matrix
import Mathlib.Topology.Connected.Basic
import Mathlib.Combinatorics.Pigeonhole
import Mathlib.Tactic.LinearCombination

namespace OIBridge
namespace BridgeReach

open Matrix

noncomputable section

/-! ### §A — pair vectors, products and the coefficient determinant -/

/-- A pair vector `ψ (a, b)`, `a` the first token. -/
abbrev PVec : Type := Fin 2 × Fin 2 → ℂ

/-- Pair matrices. -/
abbrev M4 : Type := Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ

/-- The unitary group of the pair. -/
abbrev U4 : Type := ↥(Matrix.unitaryGroup (Fin 2 × Fin 2) ℂ)

/-- The determinant of the coefficient matrix of a pair vector. -/
def prodDet (v : PVec) : ℂ := v (0, 0) * v (1, 1) - v (0, 1) * v (1, 0)

/-- The polarization of `prodDet`. -/
def prodCross (x y : PVec) : ℂ :=
  x (0, 0) * y (1, 1) + y (0, 0) * x (1, 1) - x (0, 1) * y (1, 0) - y (0, 1) * x (1, 0)

/-- The product vector `a ⊗ b`. -/
def kron2 (a b : Fin 2 → ℂ) : PVec := fun ij => a ij.1 * b ij.2

/-- Entrywise complex conjugation, the antiunitary part of a conjugation. -/
def conjV (v : PVec) : PVec := fun ij => (starRingEnd ℂ) (v ij)

/-- `|00⟩ + |11⟩`. -/
def bellV : PVec := fun ij => if ij.1 = ij.2 then 1 else 0

/-- `v` avoids products under the map `g`: `g v` is no product `a ⊗ b`. -/
def AvoidsProducts (v : PVec) (g : PVec → PVec) : Prop := ∀ a b : Fin 2 → ℂ, g v ≠ kron2 a b

theorem prodDet_kron2 (a b : Fin 2 → ℂ) : prodDet (kron2 a b) = 0 := by
  show a 0 * b 0 * (a 1 * b 1) - a 0 * b 1 * (a 1 * b 0) = 0
  ring

theorem avoids_of_prodDet {v : PVec} {g : PVec → PVec} (h : prodDet (g v) ≠ 0) :
    AvoidsProducts v g := by
  intro a b hab
  apply h
  rw [hab]
  exact prodDet_kron2 a b

theorem prodDet_add_smul (x y : PVec) (t : ℂ) :
    prodDet (x + t • y) = prodDet x + prodCross x y * t + prodDet y * t ^ 2 := by
  simp only [prodDet, prodCross, Pi.add_apply, Pi.smul_apply, smul_eq_mul]
  ring

theorem conjV_add_natSmul (v w : PVec) (n : ℕ) :
    conjV (v + (n : ℂ) • w) = conjV v + (n : ℂ) • conjV w := by
  funext ij
  first
  | (simp only [conjV, Pi.add_apply, Pi.smul_apply, smul_eq_mul, map_add, map_mul,
      map_natCast]; done)
  | (simp [conjV]; done)

theorem conjV_conjV (v : PVec) : conjV (conjV v) = v := by
  funext ij
  first
  | (simp only [conjV, starRingEnd_self_apply]; done)
  | (simp [conjV]; done)

theorem prodDet_bellV : prodDet bellV = 1 := by
  first
  | (simp [prodDet, bellV]; done)
  | (simp +decide [prodDet, bellV]; done)
  | (norm_num [prodDet, bellV]; done)

theorem prodDet_zero : prodDet 0 = 0 := by
  simp [prodDet]

/-! ### §B — the statement of B7-1 -/

/-- The identity component of `H` is commutative. -/
def IdCompComm (H : Subgroup U4) : Prop :=
  ∀ x ∈ connectedComponent (1 : H), ∀ y ∈ connectedComponent (1 : H), x * y = y * x

/-- **B7-1, unitary groups** (statement only): every closed subgroup of `U(4)` with commutative
identity component misses a pure state with its orbit of pure products. -/
def ReachUnitary : Prop :=
  ∀ H : Subgroup U4, IsClosed (H : Set U4) → IdCompComm H →
    ∃ v : PVec, v ≠ 0 ∧ ∀ h ∈ H, AvoidsProducts v (fun u => (h : M4) *ᵥ u)

/-- **B7-1, groups with an antiunitary coset** (statement only). `H ∪ H κ`, `κ = K ∘ conj`, is a
group under the two coset conditions; no element of it carries `v` to a product. -/
def ReachAnti : Prop :=
  ∀ (H : Subgroup U4) (K : U4), IsClosed (H : Set U4) → IdCompComm H →
    (∀ h ∈ H, ∃ h' ∈ H,
      (h' : M4) = (K : M4) * Matrix.map (h : M4) (starRingEnd ℂ) * star (K : M4)) →
    (∃ h ∈ H, (h : M4) = (K : M4) * Matrix.map (K : M4) (starRingEnd ℂ)) →
    ∃ v : PVec, v ≠ 0 ∧ ∀ h ∈ H, AvoidsProducts v (fun u => (h : M4) *ᵥ u) ∧
      AvoidsProducts v (fun u => ((h : M4) * (K : M4)) *ᵥ conjV u)

/-! ### §C — the avoidance lemma -/

/-- `f` is quadratic along every line `v + n w`, `n : ℕ`. -/
def QuadAlong (f : PVec → ℂ) : Prop :=
  ∀ v w : PVec, ∃ b : ℂ, ∀ n : ℕ,
    f (v + (n : ℂ) • w) = f v + b * (n : ℂ) + f w * (n : ℂ) ^ 2

/-- A quadratic with three distinct roots has vanishing constant and leading coefficients. -/
theorem quad_eq_zero_of_three {a b c t₁ t₂ t₃ : ℂ} (h12 : t₁ ≠ t₂) (h13 : t₁ ≠ t₃)
    (h23 : t₂ ≠ t₃) (e₁ : a + b * t₁ + c * t₁ ^ 2 = 0) (e₂ : a + b * t₂ + c * t₂ ^ 2 = 0)
    (e₃ : a + b * t₃ + c * t₃ ^ 2 = 0) : a = 0 ∧ c = 0 := by
  have k₁ : (t₁ - t₂) * (b + c * (t₁ + t₂)) = 0 := by linear_combination e₁ - e₂
  have k₂ : (t₁ - t₃) * (b + c * (t₁ + t₃)) = 0 := by linear_combination e₁ - e₃
  have l₁ : b + c * (t₁ + t₂) = 0 := (mul_eq_zero.mp k₁).resolve_left (sub_ne_zero.mpr h12)
  have l₂ : b + c * (t₁ + t₃) = 0 := (mul_eq_zero.mp k₂).resolve_left (sub_ne_zero.mpr h13)
  have k₃ : (t₂ - t₃) * c = 0 := by linear_combination l₁ - l₂
  have hc : c = 0 := (mul_eq_zero.mp k₃).resolve_left (sub_ne_zero.mpr h23)
  have hb : b = 0 := by linear_combination l₁ - (t₁ + t₂) * hc
  have ha : a = 0 := by linear_combination e₁ - t₁ * hb - t₁ ^ 2 * hc
  exact ⟨ha, hc⟩

/-- **Avoidance.** Finitely many functions on pair vectors, each nonzero somewhere and quadratic
along every line, have a common non-root. -/
theorem exists_avoid {ι : Type*} [DecidableEq ι] (f : ι → PVec → ℂ) (hq : ∀ i, QuadAlong (f i))
    (hn : ∀ i, ∃ w, f i w ≠ 0) (s : Finset ι) : ∃ v : PVec, ∀ i ∈ s, f i v ≠ 0 := by
  induction s using Finset.induction_on with
  | empty => exact ⟨0, by simp⟩
  | insert j s _ ih =>
    obtain ⟨v, hv⟩ := ih
    obtain ⟨w, hw⟩ := hn j
    by_contra hcon
    push_neg at hcon
    have hc : ∀ n : ℕ, ∃ i, i ∈ insert j s ∧ f i (v + (n : ℂ) • w) = 0 := fun n => hcon _
    choose g hg using hc
    have hbound : (insert j s).card * 2 < (Finset.range (2 * (insert j s).card + 1)).card := by
      rw [Finset.card_range]
      omega
    obtain ⟨i, hi, hlt⟩ := Finset.exists_lt_card_fiber_of_mul_lt_card_of_maps_to
      (s := Finset.range (2 * (insert j s).card + 1)) (t := insert j s) (f := g) (n := 2)
      (fun n _ => (hg n).1) hbound
    obtain ⟨n₁, n₂, n₃, h₁, h₂, h₃, h12, h13, h23⟩ := Finset.two_lt_card_iff.mp hlt
    have r₁ : f i (v + (n₁ : ℂ) • w) = 0 := by
      have hr := (hg n₁).2
      rwa [(Finset.mem_filter.mp h₁).2] at hr
    have r₂ : f i (v + (n₂ : ℂ) • w) = 0 := by
      have hr := (hg n₂).2
      rwa [(Finset.mem_filter.mp h₂).2] at hr
    have r₃ : f i (v + (n₃ : ℂ) • w) = 0 := by
      have hr := (hg n₃).2
      rwa [(Finset.mem_filter.mp h₃).2] at hr
    obtain ⟨b, hb⟩ := hq i v w
    have e₁ : f i v + b * (n₁ : ℂ) + f i w * (n₁ : ℂ) ^ 2 = 0 := (hb n₁).symm.trans r₁
    have e₂ : f i v + b * (n₂ : ℂ) + f i w * (n₂ : ℂ) ^ 2 = 0 := (hb n₂).symm.trans r₂
    have e₃ : f i v + b * (n₃ : ℂ) + f i w * (n₃ : ℂ) ^ 2 = 0 := (hb n₃).symm.trans r₃
    have d12 : (n₁ : ℂ) ≠ (n₂ : ℂ) := by exact_mod_cast h12
    have d13 : (n₁ : ℂ) ≠ (n₃ : ℂ) := by exact_mod_cast h13
    have d23 : (n₂ : ℂ) ≠ (n₃ : ℂ) := by exact_mod_cast h23
    have hz := quad_eq_zero_of_three d12 d13 d23 e₁ e₂ e₃
    rcases Finset.mem_insert.mp hi with h | h
    · rw [h] at hz
      exact hw hz.2
    · exact hv i h hz.1

/-! ### §D — the finite case -/

theorem quadAlong_mulVec (U : M4) : QuadAlong (fun v => prodDet (U *ᵥ v)) := by
  intro v w
  refine ⟨prodCross (U *ᵥ v) (U *ᵥ w), fun n => ?_⟩
  show prodDet (U *ᵥ (v + (n : ℂ) • w)) =
    prodDet (U *ᵥ v) + prodCross (U *ᵥ v) (U *ᵥ w) * (n : ℂ) + prodDet (U *ᵥ w) * (n : ℂ) ^ 2
  rw [Matrix.mulVec_add, Matrix.mulVec_smul]
  exact prodDet_add_smul _ _ _

theorem quadAlong_mulVec_conj (U : M4) : QuadAlong (fun v => prodDet (U *ᵥ conjV v)) := by
  intro v w
  refine ⟨prodCross (U *ᵥ conjV v) (U *ᵥ conjV w), fun n => ?_⟩
  show prodDet (U *ᵥ conjV (v + (n : ℂ) • w)) =
    prodDet (U *ᵥ conjV v) + prodCross (U *ᵥ conjV v) (U *ᵥ conjV w) * (n : ℂ) +
      prodDet (U *ᵥ conjV w) * (n : ℂ) ^ 2
  rw [conjV_add_natSmul, Matrix.mulVec_add, Matrix.mulVec_smul]
  exact prodDet_add_smul _ _ _

theorem exists_ne_zero_of_mul_star {M : M4} (hM : M * star M = 1) :
    ∃ w : PVec, prodDet (M *ᵥ w) ≠ 0 := by
  refine ⟨star M *ᵥ bellV, ?_⟩
  rw [Matrix.mulVec_mulVec, hM, Matrix.one_mulVec, prodDet_bellV]
  exact one_ne_zero

theorem exists_ne_zero_of_mul_star_conj {M : M4} (hM : M * star M = 1) :
    ∃ w : PVec, prodDet (M *ᵥ conjV w) ≠ 0 := by
  refine ⟨conjV (star M *ᵥ bellV), ?_⟩
  rw [conjV_conjV, Matrix.mulVec_mulVec, hM, Matrix.one_mulVec, prodDet_bellV]
  exact one_ne_zero

/-- **The finite case, unitary groups.** -/
theorem reachUnitary_finite (H : Subgroup U4) (hfin : (H : Set U4).Finite) :
    ∃ v : PVec, v ≠ 0 ∧ ∀ h ∈ H, AvoidsProducts v (fun u => (h : M4) *ᵥ u) := by
  classical
  obtain ⟨v, hv⟩ := exists_avoid (fun (g : U4) (u : PVec) => prodDet ((g : M4) *ᵥ u))
    (fun g => quadAlong_mulVec (g : M4))
    (fun g => exists_ne_zero_of_mul_star (Matrix.mem_unitaryGroup_iff.mp g.2))
    (insert 1 hfin.toFinset)
  refine ⟨v, ?_, ?_⟩
  · intro h0
    apply hv 1 (Finset.mem_insert_self _ _)
    simp [h0, prodDet]
  · intro h hh
    exact avoids_of_prodDet (hv h (Finset.mem_insert_of_mem (hfin.mem_toFinset.mpr hh)))

/-- **The finite case, groups with an antiunitary coset.** No coset condition is needed. -/
theorem reachAnti_finite (H : Subgroup U4) (K : U4) (hfin : (H : Set U4).Finite) :
    ∃ v : PVec, v ≠ 0 ∧ ∀ h ∈ H, AvoidsProducts v (fun u => (h : M4) *ᵥ u) ∧
      AvoidsProducts v (fun u => ((h : M4) * (K : M4)) *ᵥ conjV u) := by
  classical
  obtain ⟨v, hv⟩ := exists_avoid
    (Sum.elim (fun (g : U4) (u : PVec) => prodDet ((g : M4) *ᵥ u))
      (fun (g : U4) (u : PVec) => prodDet (((g : M4) * (K : M4)) *ᵥ conjV u)))
    (fun i => by
      cases i with
      | inl g => exact quadAlong_mulVec (g : M4)
      | inr g => exact quadAlong_mulVec_conj ((g : M4) * (K : M4)))
    (fun i => by
      cases i with
      | inl g => exact exists_ne_zero_of_mul_star (Matrix.mem_unitaryGroup_iff.mp g.2)
      | inr g =>
        have hgK : ((g : M4) * (K : M4)) * star ((g : M4) * (K : M4)) = 1 :=
          Matrix.mem_unitaryGroup_iff.mp (g * K).2
        exact exists_ne_zero_of_mul_star_conj hgK)
    (insert (Sum.inl 1) (hfin.toFinset.image Sum.inl ∪ hfin.toFinset.image Sum.inr))
  refine ⟨v, ?_, ?_⟩
  · intro h0
    apply hv (Sum.inl 1) (Finset.mem_insert_self _ _)
    simp [h0, prodDet]
  · intro h hh
    have hm : h ∈ hfin.toFinset := hfin.mem_toFinset.mpr hh
    refine ⟨avoids_of_prodDet ?_, avoids_of_prodDet ?_⟩
    · exact hv (Sum.inl h)
        (Finset.mem_insert_of_mem (Finset.mem_union_left _ (Finset.mem_image_of_mem _ hm)))
    · exact hv (Sum.inr h)
        (Finset.mem_insert_of_mem (Finset.mem_union_right _ (Finset.mem_image_of_mem _ hm)))

/-- `ReachUnitary` reduces to its infinite closed subgroups. -/
theorem reachUnitary_of_infinite
    (hinf : ∀ H : Subgroup U4, IsClosed (H : Set U4) → IdCompComm H → (H : Set U4).Infinite →
      ∃ v : PVec, v ≠ 0 ∧ ∀ h ∈ H, AvoidsProducts v (fun u => (h : M4) *ᵥ u)) :
    ReachUnitary := by
  intro H hc hid
  by_cases hfin : (H : Set U4).Finite
  · exact reachUnitary_finite H hfin
  · exact hinf H hc hid hfin

/-- `ReachAnti` reduces to its infinite closed subgroups. -/
theorem reachAnti_of_infinite
    (hinf : ∀ (H : Subgroup U4) (K : U4), IsClosed (H : Set U4) → IdCompComm H →
      (∀ h ∈ H, ∃ h' ∈ H,
        (h' : M4) = (K : M4) * Matrix.map (h : M4) (starRingEnd ℂ) * star (K : M4)) →
      (∃ h ∈ H, (h : M4) = (K : M4) * Matrix.map (K : M4) (starRingEnd ℂ)) →
      (H : Set U4).Infinite →
      ∃ v : PVec, v ≠ 0 ∧ ∀ h ∈ H, AvoidsProducts v (fun u => (h : M4) *ᵥ u) ∧
        AvoidsProducts v (fun u => ((h : M4) * (K : M4)) *ᵥ conjV u)) :
    ReachAnti := by
  intro H K hc hid h1 h2
  by_cases hfin : (H : Set U4).Finite
  · exact reachAnti_finite H K hfin
  · exact hinf H K hc hid h1 h2 hfin

/-! ### §E — controls -/

/-- `CNOT` on pair vectors: `(CNOT ψ)(a, b) = ψ(a, b ⊕ a)`. -/
def cnotV (v : PVec) : PVec :=
  fun ij => ![![v (0, 0), v (0, 1)], ![v (1, 1), v (1, 0)]] ij.1 ij.2

/-- The explicit vector `(1, 2, 3, 5)`. -/
def ctlV : PVec := fun ij => ![![(1 : ℂ), 2], ![3, 5]] ij.1 ij.2

/-- **Positive control**: the coefficient determinants of `ctlV` and of `CNOT ctlV`. -/
theorem ctl_cnot_witness : prodDet ctlV = -1 ∧ prodDet (cnotV ctlV) = -7 := by
  constructor <;> norm_num [prodDet, ctlV, cnotV]

/-- **Positive control**: `ctlV` avoids products under `1` and under `CNOT`. -/
theorem ctl_avoids : AvoidsProducts ctlV (fun u => u) ∧ AvoidsProducts ctlV cnotV := by
  refine ⟨avoids_of_prodDet ?_, avoids_of_prodDet ?_⟩
  · show prodDet ctlV ≠ 0
    rw [ctl_cnot_witness.1]
    norm_num
  · show prodDet (cnotV ctlV) ≠ 0
    rw [ctl_cnot_witness.2]
    norm_num

/-- **Countercontrol**: the zero matrix is quadratic along lines and has no non-root, so the
hypothesis `∃ w, f w ≠ 0` of `exists_avoid` (unitarity, in §D) is load-bearing. -/
theorem ctl_counter_zero : QuadAlong (fun v => prodDet ((0 : M4) *ᵥ v)) ∧
    ∀ v : PVec, prodDet ((0 : M4) *ᵥ v) = 0 :=
  ⟨quadAlong_mulVec 0, fun v => by rw [Matrix.zero_mulVec, prodDet_zero]⟩

/-- Two complementary step functions. -/
def stepF (b : Bool) (v : PVec) : ℂ :=
  if 0 < (v (0, 0)).re then (if b then 1 else 0) else (if b then 0 else 1)

/-- **Countercontrol**: each step function is nonzero somewhere, and the two have no common
non-root, so the quadratic hypothesis of `exists_avoid` is load-bearing. -/
theorem ctl_counter_step : (∀ b, ∃ w, stepF b w ≠ 0) ∧
    ¬ ∃ v : PVec, ∀ b ∈ ({true, false} : Finset Bool), stepF b v ≠ 0 := by
  constructor
  · intro b
    cases b
    · exact ⟨0, by simp [stepF]⟩
    · exact ⟨1, by simp [stepF]⟩
  · rintro ⟨v, hv⟩
    by_cases h : 0 < (v (0, 0)).re
    · exact hv false (by simp) (by simp [stepF, h])
    · exact hv true (by simp) (by simp [stepF, h])

end

#print axioms prodDet_kron2
#print axioms avoids_of_prodDet
#print axioms prodDet_add_smul
#print axioms conjV_add_natSmul
#print axioms conjV_conjV
#print axioms prodDet_bellV
#print axioms prodDet_zero
#print axioms quad_eq_zero_of_three
#print axioms exists_avoid
#print axioms quadAlong_mulVec
#print axioms quadAlong_mulVec_conj
#print axioms exists_ne_zero_of_mul_star
#print axioms exists_ne_zero_of_mul_star_conj
#print axioms reachUnitary_finite
#print axioms reachAnti_finite
#print axioms reachUnitary_of_infinite
#print axioms reachAnti_of_infinite
#print axioms ctl_cnot_witness
#print axioms ctl_avoids
#print axioms ctl_counter_zero
#print axioms ctl_counter_step

end BridgeReach
end OIBridge
