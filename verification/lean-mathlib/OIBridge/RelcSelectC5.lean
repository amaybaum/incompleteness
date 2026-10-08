/-
  OIBridge/RelcSelectC5.lean — design module for round RELC-SELECT-1 (UNBUILT DRAFT: no local Lean
  toolchain was available when it was written; it has not been compiled).

  The control relation is not replaced by the target relation, the frame and two-sided positivity.
  At `d = 5`, two copies of `eball 5` carry the NOT `nC5 = diag(1, −1, −1, −1, −1)` with axis `z5`
  and a gate `gC5` with `gC5 ∘ gC5 = id` that satisfies `NativeGate`'s frame, target relation,
  forward positivity and inverse positivity, and fails its control relation. So DIM-1's selector
  conclusion `d = 1 ∨ d = 3` does not follow from those four fields and `IsNot` alone
  (`relT_not_dimension_selecting`).

  The gate is round NB-1's `d = 5` J/K map (control `C5` of NB-1; the `d = 5` member of the REL-T
  family `C_d`). In homogeneous indices `u = 0, x = 1, y = 2, w₁ = 3, w₂ = 4, z = 5` it is the
  signed permutation of the thirty-six entries with
    `G(u ⊗ t) = u ⊗ P₊t + z ⊗ P₋t`,  `G(z ⊗ t) = z ⊗ P₊t + u ⊗ P₋t`,
    `G(c ⊗ t) = c ⊗ X P₊t + J c ⊗ K P₋t`  for `c ∈ {x, y, w₁, w₂}`,
  where `P₊`, `P₋` project onto `⟨u, x⟩` and `⟨y, w₁, w₂, z⟩`, `X` exchanges `u ↔ x`, and
  `J : x ↦ y ↦ −x, w₁ ↦ w₂ ↦ −w₁`, `K : y ↦ z ↦ −y, w₁ ↦ w₂ ↦ −w₁`.

  Positivity is proved directly, without NB-1's reduction to the complex CNOT. The value of a product
  effect `e ⊗ f` on the image of a product state `x ⊗ y` is exactly (`prodEffVal_gC5_prodState`)
    `(e₀ + x₄e₅) p + (e₅ + x₄e₀) m + s₁ α + s₂ β`,
  with `p ± m = ⟨f, hom y⟩, ⟨f, homMap nC5 (hom y)⟩`, `α, β` the target pairings through `X` and `K`,
  and `s₁, s₂` the control pairings through the identity and `J`. Two Bessel inequalities for the
  orthogonal complex structures `J`, `K` (four-square identities, `selC5_besselJ`, `selC5_besselK`),
  Cauchy–Schwarz and the bound `u² ≤ AB ⇒ 0 ≤ A + B + 2u` (`selC5_mix`) give nonnegativity
  (`selC5_target`, `selC5_core`). Inverse positivity is the same statement, since `gC5.symm = gC5`.
-/
import OIBridge.OddChar

namespace OIBridge
namespace RelcSelect

open KInfFoundations TransitiveBody NativeGateBall CompositeDimension EffectSpace ParityNot

/-! ### §A — the NOT `nC5` -/

/-- The sign class of a homogeneous index at `d = 5` for `nC5`: every index but `0` and `1`. -/
def oddC5 : Fin 6 → Bool
  | 0 => false | 1 => false | 2 => true | 3 => true | 4 => true | 5 => true

/-- The signs of `nC5` on the five coordinates. -/
def cC5 (j : Fin 5) : ℝ := if oddC5 j.succ then -1 else 1

/-- The NOT of `eball 5` fixing the first coordinate and inverting the other four. -/
def nC5 : (Fin 5 → ℝ) →ₗ[ℝ] (Fin 5 → ℝ) := diagSign cC5

theorem cC5_sq (j : Fin 5) : cC5 j ^ 2 = 1 := by
  unfold cC5
  split_ifs <;> norm_num

theorem homMap_nC5_sign (v : HVec 5) (μ : Fin (5 + 1)) :
    homMap nC5 v μ = (if oddC5 μ then -1 else 1) * v μ := by
  show homMap (diagSign cC5) v μ = _
  rw [homMap_diagSign]
  congr 1
  refine Fin.cases ?_ (fun j => ?_) μ
  · simp [oddC5]
  · rw [Matrix.cons_val_succ]
    rfl

/-- `nC5` is a NOT of `eball 5` with the landed axis `z5`. -/
theorem isNot_nC5 : IsNot (eball 5) z5 nC5 where
  unit := z5_unit
  invol x := by
    funext i
    show cC5 i * (cC5 i * x i) = x i
    rw [← mul_assoc, ← sq, cC5_sq, one_mul]
  preserves x hx := by
    rw [mem_eball] at hx ⊢
    have h : ∀ j, (nC5 x j) ^ 2 = x j ^ 2 := fun j => by
      show (cC5 j * x j) ^ 2 = x j ^ 2
      rw [mul_pow, cC5_sq, one_mul]
    rw [Finset.sum_congr rfl fun j _ => h j]
    exact hx
  flips := by
    funext i
    show cC5 i * z5 i = -z5 i
    fin_cases i <;> simp +decide [cC5, z5]

/-! ### §B — the gate `gC5` -/

/-- The sign of `gC5` at an index pair: `−1` on `{x, w₁} × {w₂, z}` and `{y, w₂} × {y, w₁}`. -/
def sgnC5 (μ ν : Fin 6) : ℝ :=
  if ((μ = 1 ∨ μ = 3) ∧ (ν = 4 ∨ ν = 5)) ∨ ((μ = 2 ∨ μ = 4) ∧ (ν = 2 ∨ ν = 3)) then -1 else 1

/-- The control index read by `gC5` at an index pair (`J` on the target-odd columns, the corner
exchange `u ↔ z` on the target-odd columns of the corner rows). -/
def pcC5 : Fin 6 → Fin 6 → Fin 6
  | 0, 0 => 0 | 0, 1 => 0 | 0, 2 => 5 | 0, 3 => 5 | 0, 4 => 5 | 0, 5 => 5
  | 1, 0 => 1 | 1, 1 => 1 | 1, 2 => 2 | 1, 3 => 2 | 1, 4 => 2 | 1, 5 => 2
  | 2, 0 => 2 | 2, 1 => 2 | 2, 2 => 1 | 2, 3 => 1 | 2, 4 => 1 | 2, 5 => 1
  | 3, 0 => 3 | 3, 1 => 3 | 3, 2 => 4 | 3, 3 => 4 | 3, 4 => 4 | 3, 5 => 4
  | 4, 0 => 4 | 4, 1 => 4 | 4, 2 => 3 | 4, 3 => 3 | 4, 4 => 3 | 4, 5 => 3
  | 5, 0 => 5 | 5, 1 => 5 | 5, 2 => 0 | 5, 3 => 0 | 5, 4 => 0 | 5, 5 => 0

/-- The target index read by `gC5` at an index pair (identity on the corner rows; `X` and `K` on
the tangent rows). -/
def ptC5 : Fin 6 → Fin 6 → Fin 6
  | 0, 0 => 0 | 0, 1 => 1 | 0, 2 => 2 | 0, 3 => 3 | 0, 4 => 4 | 0, 5 => 5
  | 1, 0 => 1 | 1, 1 => 0 | 1, 2 => 5 | 1, 3 => 4 | 1, 4 => 3 | 1, 5 => 2
  | 2, 0 => 1 | 2, 1 => 0 | 2, 2 => 5 | 2, 3 => 4 | 2, 4 => 3 | 2, 5 => 2
  | 3, 0 => 1 | 3, 1 => 0 | 3, 2 => 5 | 3, 3 => 4 | 3, 4 => 3 | 3, 5 => 2
  | 4, 0 => 1 | 4, 1 => 0 | 4, 2 => 5 | 4, 3 => 4 | 4, 4 => 3 | 4, 5 => 2
  | 5, 0 => 0 | 5, 1 => 1 | 5, 2 => 2 | 5, 3 => 3 | 5, 4 => 4 | 5, 5 => 5

/-- The `d = 5` J/K gate as a function: a signed permutation of the thirty-six entries. -/
def gC5Fun (ω : W 5) : W 5 := fun μ ν => sgnC5 μ ν * ω (pcC5 μ ν) (ptC5 μ ν)

theorem gC5Fun_apply (ω : W 5) (μ ν : Fin 6) :
    gC5Fun ω μ ν = sgnC5 μ ν * ω (pcC5 μ ν) (ptC5 μ ν) := rfl

theorem pcC5_pcC5 : ∀ μ ν : Fin 6, pcC5 (pcC5 μ ν) (ptC5 μ ν) = μ := by decide

theorem ptC5_ptC5 : ∀ μ ν : Fin 6, ptC5 (pcC5 μ ν) (ptC5 μ ν) = ν := by decide

theorem sgnC5_mul_sgnC5 : ∀ μ ν : Fin 6, sgnC5 μ ν * sgnC5 (pcC5 μ ν) (ptC5 μ ν) = 1 := by
  intro μ ν
  fin_cases μ <;> fin_cases ν <;> simp +decide [sgnC5]

/-- The target index read by `gC5` has the sign class of the target index written. -/
theorem oddC5_ptC5 : ∀ μ ν : Fin 6, oddC5 (ptC5 μ ν) = oddC5 ν := by decide

theorem gC5Fun_gC5Fun (ω : W 5) : gC5Fun (gC5Fun ω) = ω := by
  funext μ ν
  rw [gC5Fun_apply, gC5Fun_apply, pcC5_pcC5, ptC5_ptC5, ← mul_assoc, sgnC5_mul_sgnC5, one_mul]

/-- The `d = 5` J/K gate as a linear equivalence of the joint carrier; it is its own inverse. -/
def gC5 : W 5 ≃ₗ[ℝ] W 5 where
  toFun := gC5Fun
  invFun := gC5Fun
  map_add' ω₁ ω₂ := by
    funext μ ν
    simp only [gC5Fun_apply, Pi.add_apply, mul_add]
  map_smul' c ω := by
    funext μ ν
    simp only [gC5Fun_apply, Pi.smul_apply, smul_eq_mul, RingHom.id_apply]
    ring
  left_inv := gC5Fun_gC5Fun
  right_inv := gC5Fun_gC5Fun

theorem gC5_apply (ω : W 5) : gC5 ω = gC5Fun ω := rfl

theorem gC5_symm_apply (ω : W 5) : gC5.symm ω = gC5Fun ω := rfl

/-! ### §C — the frame, the target relation, and the failure of the control relation -/

/-- **The frame.** `gC5` acts as the controlled NOT on the corners `±z5`. -/
theorem gC5_frame (a b : Fin 2) :
    gC5 (prodState (corner z5 a) (corner z5 b)) = prodState (corner z5 a) (corner z5 (a + b)) := by
  fin_cases a <;> fin_cases b <;> funext μ ν <;> fin_cases μ <;> fin_cases ν <;>
    simp +decide [gC5_apply, gC5Fun_apply, sgnC5, pcC5, ptC5, prodState_apply, corner_zero,
      corner_one, z5]

/-- **The target relation.** `(I ⊗ nC5) gC5 (I ⊗ nC5) = gC5`. -/
theorem gC5_relT (ω : W 5) : actT nC5 (gC5 (actT nC5 ω)) = gC5 ω := by
  funext μ ν
  have hodd := oddC5_ptC5 μ ν
  simp only [actT_apply, homMap_nC5_sign, gC5_apply, gC5Fun_apply, hodd]
  split_ifs <;> ring

/-- The control side of the relation at the entry `(w₂, w₂)` of the image of the matrix unit at
`(w₁, w₁)`. -/
theorem gC5_relC_lhs : actC nC5 (gC5 (actC nC5 (OddChar.entW 3 3))) 4 4 = 1 := by
  simp +decide [actC_apply, homMap_nC5_sign, gC5_apply, gC5Fun_apply, sgnC5, pcC5, ptC5, oddC5,
    OddChar.entW]

/-- The target side of the relation at the same entry. -/
theorem gC5_relC_rhs : actT nC5 (gC5 (OddChar.entW 3 3)) 4 4 = -1 := by
  simp +decide [actT_apply, homMap_nC5_sign, gC5_apply, gC5Fun_apply, sgnC5,
    OddChar.entW]

/-- **The control relation fails.** -/
theorem gC5_not_relC : ¬ ∀ ω, actC nC5 (gC5 (actC nC5 ω)) = actT nC5 (gC5 ω) := by
  intro h
  have h44 := congrFun (congrFun (h (OddChar.entW 3 3)) 4) 4
  rw [gC5_relC_lhs, gC5_relC_rhs] at h44
  norm_num at h44

/-! ### §D — the real inequalities -/

/-- Cauchy–Schwarz in five variables (Lagrange's identity). -/
theorem selC5_cs (a0 a1 a2 a3 a4 b0 b1 b2 b3 b4 : ℝ) :
    (a0 * b0 + a1 * b1 + a2 * b2 + a3 * b3 + a4 * b4) ^ 2
      ≤ (a0 ^ 2 + a1 ^ 2 + a2 ^ 2 + a3 ^ 2 + a4 ^ 2) * (b0 ^ 2 + b1 ^ 2 + b2 ^ 2 + b3 ^ 2 + b4 ^ 2) := by
  have hid : (a0 ^ 2 + a1 ^ 2 + a2 ^ 2 + a3 ^ 2 + a4 ^ 2) * (b0 ^ 2 + b1 ^ 2 + b2 ^ 2 + b3 ^ 2 + b4 ^ 2)
      - (a0 * b0 + a1 * b1 + a2 * b2 + a3 * b3 + a4 * b4) ^ 2
      = (a0 * b1 - a1 * b0) ^ 2 + (a0 * b2 - a2 * b0) ^ 2 + (a0 * b3 - a3 * b0) ^ 2
        + (a0 * b4 - a4 * b0) ^ 2 + (a1 * b2 - a2 * b1) ^ 2 + (a1 * b3 - a3 * b1) ^ 2
        + (a1 * b4 - a4 * b1) ^ 2 + (a2 * b3 - a3 * b2) ^ 2 + (a2 * b4 - a4 * b2) ^ 2
        + (a3 * b4 - a4 * b3) ^ 2 := by ring
  have h0 : 0 ≤ (a0 * b1 - a1 * b0) ^ 2 + (a0 * b2 - a2 * b0) ^ 2 + (a0 * b3 - a3 * b0) ^ 2
        + (a0 * b4 - a4 * b0) ^ 2 + (a1 * b2 - a2 * b1) ^ 2 + (a1 * b3 - a3 * b1) ^ 2
        + (a1 * b4 - a4 * b1) ^ 2 + (a2 * b3 - a3 * b2) ^ 2 + (a2 * b4 - a4 * b2) ^ 2
        + (a3 * b4 - a4 * b3) ^ 2 := by positivity
  linarith

/-- Cauchy–Schwarz in two variables. -/
theorem selC5_cauchy2 (s1 s2 a b : ℝ) :
    (s1 * a + s2 * b) ^ 2 ≤ (s1 ^ 2 + s2 ^ 2) * (a ^ 2 + b ^ 2) := by
  have hid : (s1 ^ 2 + s2 ^ 2) * (a ^ 2 + b ^ 2) - (s1 * a + s2 * b) ^ 2 = (s1 * b - s2 * a) ^ 2 := by
    ring
  linarith [sq_nonneg (s1 * b - s2 * a)]

/-- Bessel for the complex structure `J b = (−b₁, b₀, −b₃, b₂)`: the four-square identity leaves
two squares. -/
theorem selC5_besselJ (a0 a1 a2 a3 b0 b1 b2 b3 : ℝ) :
    (a0 * b0 + a1 * b1 + a2 * b2 + a3 * b3) ^ 2 + (a1 * b0 - a0 * b1 + a3 * b2 - a2 * b3) ^ 2
      ≤ (a0 ^ 2 + a1 ^ 2 + a2 ^ 2 + a3 ^ 2) * (b0 ^ 2 + b1 ^ 2 + b2 ^ 2 + b3 ^ 2) := by
  have hid : (a0 ^ 2 + a1 ^ 2 + a2 ^ 2 + a3 ^ 2) * (b0 ^ 2 + b1 ^ 2 + b2 ^ 2 + b3 ^ 2)
      - ((a0 * b0 + a1 * b1 + a2 * b2 + a3 * b3) ^ 2 + (a1 * b0 - a0 * b1 + a3 * b2 - a2 * b3) ^ 2)
      = (-a0 * b2 + a1 * b3 + a2 * b0 - a3 * b1) ^ 2 + (-a0 * b3 - a1 * b2 + a2 * b1 + a3 * b0) ^ 2 := by
    ring
  linarith [sq_nonneg (-a0 * b2 + a1 * b3 + a2 * b0 - a3 * b1),
    sq_nonneg (-a0 * b3 - a1 * b2 + a2 * b1 + a3 * b0)]

/-- Bessel for the complex structure `K b = (−b₃, −b₂, b₁, b₀)`. -/
theorem selC5_besselK (a0 a1 a2 a3 b0 b1 b2 b3 : ℝ) :
    (a0 * b0 + a1 * b1 + a2 * b2 + a3 * b3) ^ 2 + (a3 * b0 + a2 * b1 - a1 * b2 - a0 * b3) ^ 2
      ≤ (a0 ^ 2 + a1 ^ 2 + a2 ^ 2 + a3 ^ 2) * (b0 ^ 2 + b1 ^ 2 + b2 ^ 2 + b3 ^ 2) := by
  have hid : (a0 ^ 2 + a1 ^ 2 + a2 ^ 2 + a3 ^ 2) * (b0 ^ 2 + b1 ^ 2 + b2 ^ 2 + b3 ^ 2)
      - ((a0 * b0 + a1 * b1 + a2 * b2 + a3 * b3) ^ 2 + (a3 * b0 + a2 * b1 - a1 * b2 - a0 * b3) ^ 2)
      = (-a0 * b1 + a1 * b0 - a2 * b3 + a3 * b2) ^ 2 + (-a0 * b2 + a1 * b3 + a2 * b0 - a3 * b1) ^ 2 := by
    ring
  linarith [sq_nonneg (-a0 * b1 + a1 * b0 - a2 * b3 + a3 * b2),
    sq_nonneg (-a0 * b2 + a1 * b3 + a2 * b0 - a3 * b1)]

/-- `u² ≤ AB` with `A, B ≥ 0` gives `0 ≤ A + B + 2u` (AM–GM). -/
theorem selC5_mix (A B u : ℝ) (hA : 0 ≤ A) (hB : 0 ≤ B) (hu : u ^ 2 ≤ A * B) :
    0 ≤ A + B + 2 * u := by
  have hid : (A + B) ^ 2 - (2 * u) ^ 2 = (A - B) ^ 2 + 4 * (A * B - u ^ 2) := by ring
  have h1 : (2 * u) ^ 2 ≤ (A + B) ^ 2 := by linarith [sq_nonneg (A - B)]
  have h2 := (abs_le_of_sq_le_sq' h1 (add_nonneg hA hB)).1
  linarith

/-- The target side: `p ± m ≥ 0` and `α² + β² ≤ p² − m²`. -/
theorem selC5_target (f0 f1 f2 f3 f4 f5 y0 y1 y2 y3 y4 : ℝ) (hf0 : 0 ≤ f0)
    (hf : f1 ^ 2 + f2 ^ 2 + f3 ^ 2 + f4 ^ 2 + f5 ^ 2 ≤ f0 ^ 2)
    (hy : y0 ^ 2 + y1 ^ 2 + y2 ^ 2 + y3 ^ 2 + y4 ^ 2 ≤ 1) :
    0 ≤ (f0 + f1 * y0) + (f2 * y1 + f3 * y2 + f4 * y3 + f5 * y4) ∧
      0 ≤ (f0 + f1 * y0) - (f2 * y1 + f3 * y2 + f4 * y3 + f5 * y4) ∧
      (f0 * y0 + f1) ^ 2 + (f5 * y1 + f4 * y2 - f3 * y3 - f2 * y4) ^ 2
        ≤ (f0 + f1 * y0) ^ 2 - (f2 * y1 + f3 * y2 + f4 * y3 + f5 * y4) ^ 2 := by
  have hFY : (f1 ^ 2 + f2 ^ 2 + f3 ^ 2 + f4 ^ 2 + f5 ^ 2) * (y0 ^ 2 + y1 ^ 2 + y2 ^ 2 + y3 ^ 2 + y4 ^ 2)
      ≤ f0 ^ 2 := by
    calc (f1 ^ 2 + f2 ^ 2 + f3 ^ 2 + f4 ^ 2 + f5 ^ 2) * (y0 ^ 2 + y1 ^ 2 + y2 ^ 2 + y3 ^ 2 + y4 ^ 2)
        ≤ f0 ^ 2 * 1 := mul_le_mul hf hy (by positivity) (sq_nonneg _)
      _ = f0 ^ 2 := mul_one _
  have h1 := selC5_cs f1 f2 f3 f4 f5 y0 y1 y2 y3 y4
  have h2 := selC5_cs f1 f2 f3 f4 f5 y0 (-y1) (-y2) (-y3) (-y4)
  have hplus : (f1 * y0 + f2 * y1 + f3 * y2 + f4 * y3 + f5 * y4) ^ 2 ≤ f0 ^ 2 := le_trans h1 hFY
  have hminus : (f1 * y0 - (f2 * y1 + f3 * y2 + f4 * y3 + f5 * y4)) ^ 2 ≤ f0 ^ 2 := by
    have e1 : f1 * y0 + f2 * -y1 + f3 * -y2 + f4 * -y3 + f5 * -y4
        = f1 * y0 - (f2 * y1 + f3 * y2 + f4 * y3 + f5 * y4) := by ring
    have e2 : y0 ^ 2 + (-y1) ^ 2 + (-y2) ^ 2 + (-y3) ^ 2 + (-y4) ^ 2
        = y0 ^ 2 + y1 ^ 2 + y2 ^ 2 + y3 ^ 2 + y4 ^ 2 := by ring
    rw [e1, e2] at h2
    exact le_trans h2 hFY
  have hp := (abs_le_of_sq_le_sq' hplus hf0).1
  have hm := (abs_le_of_sq_le_sq' hminus hf0).1
  refine ⟨by linarith, by linarith, ?_⟩
  have hK := selC5_besselK f2 f3 f4 f5 y1 y2 y3 y4
  have hF : f2 ^ 2 + f3 ^ 2 + f4 ^ 2 + f5 ^ 2 ≤ f0 ^ 2 - f1 ^ 2 := by linarith
  have hY : y1 ^ 2 + y2 ^ 2 + y3 ^ 2 + y4 ^ 2 ≤ 1 - y0 ^ 2 := by linarith
  have hFY' : (f2 ^ 2 + f3 ^ 2 + f4 ^ 2 + f5 ^ 2) * (y1 ^ 2 + y2 ^ 2 + y3 ^ 2 + y4 ^ 2)
      ≤ (f0 ^ 2 - f1 ^ 2) * (1 - y0 ^ 2) :=
    mul_le_mul hF hY (by positivity)
      (by linarith [sq_nonneg f2, sq_nonneg f3, sq_nonneg f4, sq_nonneg f5])
  have hid : (f0 + f1 * y0) ^ 2 - (f0 * y0 + f1) ^ 2 = (f0 ^ 2 - f1 ^ 2) * (1 - y0 ^ 2) := by ring
  linarith

/-- The control side, abstracted: the two control pairings `s₁, s₂` bounded jointly. -/
theorem selC5_ctrl (e0 e5 x4 p m s1 s2 al be : ℝ) (he0 : 0 ≤ e0) (he5 : e5 ^ 2 ≤ e0 ^ 2)
    (hx4 : x4 ^ 2 ≤ 1) (hpm : 0 ≤ p + m) (hmp : 0 ≤ p - m)
    (hab : al ^ 2 + be ^ 2 ≤ p ^ 2 - m ^ 2)
    (hs : s1 ^ 2 + s2 ^ 2 ≤ (e0 ^ 2 - e5 ^ 2) * (1 - x4 ^ 2)) :
    0 ≤ (e0 + x4 * e5) * p + (e5 + x4 * e0) * m + s1 * al + s2 * be := by
  obtain ⟨he5l, he5u⟩ := abs_le_of_sq_le_sq' he5 he0
  have hx4' : x4 ^ 2 ≤ 1 ^ 2 := by rw [one_pow]; exact hx4
  obtain ⟨hx4l, hx4u⟩ := abs_le_of_sq_le_sq' hx4' zero_le_one
  have hA : 0 ≤ (1 + x4) * (e0 + e5) * (p + m) :=
    mul_nonneg (mul_nonneg (by linarith) (by linarith)) hpm
  have hB : 0 ≤ (1 - x4) * (e0 - e5) * (p - m) :=
    mul_nonneg (mul_nonneg (by linarith) (by linarith)) hmp
  have hc := selC5_cauchy2 s1 s2 al be
  have hd : (s1 ^ 2 + s2 ^ 2) * (al ^ 2 + be ^ 2)
      ≤ (e0 ^ 2 - e5 ^ 2) * (1 - x4 ^ 2) * (p ^ 2 - m ^ 2) :=
    mul_le_mul hs hab (by positivity) (mul_nonneg (by linarith) (by linarith))
  have hprod : (e0 ^ 2 - e5 ^ 2) * (1 - x4 ^ 2) * (p ^ 2 - m ^ 2)
      = ((1 + x4) * (e0 + e5) * (p + m)) * ((1 - x4) * (e0 - e5) * (p - m)) := by ring
  have hmix := selC5_mix _ _ (s1 * al + s2 * be) hA hB (le_trans (le_trans hc hd) (le_of_eq hprod))
  have hsum : (1 + x4) * (e0 + e5) * (p + m) + (1 - x4) * (e0 - e5) * (p - m)
        + 2 * (s1 * al + s2 * be)
      = 2 * ((e0 + x4 * e5) * p + (e5 + x4 * e0) * m + s1 * al + s2 * be) := by ring
  linarith

/-- **The core inequality** in the coordinates of the value identity. -/
theorem selC5_core (e0 e1 e2 e3 e4 e5 x0 x1 x2 x3 x4 p m al be : ℝ) (he0 : 0 ≤ e0)
    (he : e1 ^ 2 + e2 ^ 2 + e3 ^ 2 + e4 ^ 2 + e5 ^ 2 ≤ e0 ^ 2)
    (hx : x0 ^ 2 + x1 ^ 2 + x2 ^ 2 + x3 ^ 2 + x4 ^ 2 ≤ 1)
    (hpm : 0 ≤ p + m) (hmp : 0 ≤ p - m) (hab : al ^ 2 + be ^ 2 ≤ p ^ 2 - m ^ 2) :
    0 ≤ (e0 + x4 * e5) * p + (e5 + x4 * e0) * m
      + (e1 * x0 + e2 * x1 + e3 * x2 + e4 * x3) * al
      + (e2 * x0 - e1 * x1 + e4 * x2 - e3 * x3) * be := by
  have hS := selC5_besselJ e1 e2 e3 e4 x0 x1 x2 x3
  have hE : e1 ^ 2 + e2 ^ 2 + e3 ^ 2 + e4 ^ 2 ≤ e0 ^ 2 - e5 ^ 2 := by linarith
  have hX : x0 ^ 2 + x1 ^ 2 + x2 ^ 2 + x3 ^ 2 ≤ 1 - x4 ^ 2 := by linarith
  have hEX : (e1 ^ 2 + e2 ^ 2 + e3 ^ 2 + e4 ^ 2) * (x0 ^ 2 + x1 ^ 2 + x2 ^ 2 + x3 ^ 2)
      ≤ (e0 ^ 2 - e5 ^ 2) * (1 - x4 ^ 2) :=
    mul_le_mul hE hX (by positivity)
      (by linarith [sq_nonneg e1, sq_nonneg e2, sq_nonneg e3, sq_nonneg e4])
  have he5 : e5 ^ 2 ≤ e0 ^ 2 := by
    linarith [sq_nonneg e1, sq_nonneg e2, sq_nonneg e3, sq_nonneg e4]
  have hx4 : x4 ^ 2 ≤ 1 := by
    linarith [sq_nonneg x0, sq_nonneg x1, sq_nonneg x2, sq_nonneg x3]
  exact selC5_ctrl e0 e5 x4 p m (e1 * x0 + e2 * x1 + e3 * x2 + e4 * x3)
    (e2 * x0 - e1 * x1 + e4 * x2 - e3 * x3) al be he0 he5 hx4 hpm hmp hab (le_trans hS hEX)

/-! ### §E — two-sided positivity of `gC5` -/

theorem selC5_lor {v : HVec 5} (hv : Lor v) :
    0 ≤ v 0 ∧ v 1 ^ 2 + v 2 ^ 2 + v 3 ^ 2 + v 4 ^ 2 + v 5 ^ 2 ≤ v 0 ^ 2 := by
  obtain ⟨h0, h⟩ := hv
  rw [Fin.sum_univ_five] at h
  exact ⟨h0, h⟩

/-- **The value identity.** The pairing of two effects with the image of a product state. -/
theorem prodEffVal_gC5_prodState (e f : (Fin 5 → ℝ) →ᵃ[ℝ] ℝ) (x y : Fin 5 → ℝ) :
    prodEffVal e f (gC5 (prodState x y))
      = (ehom e 0 + x 4 * ehom e 5) * (ehom f 0 + ehom f 1 * y 0)
        + (ehom e 5 + x 4 * ehom e 0)
          * (ehom f 2 * y 1 + ehom f 3 * y 2 + ehom f 4 * y 3 + ehom f 5 * y 4)
        + (ehom e 1 * x 0 + ehom e 2 * x 1 + ehom e 3 * x 2 + ehom e 4 * x 3)
          * (ehom f 0 * y 0 + ehom f 1)
        + (ehom e 2 * x 0 - ehom e 1 * x 1 + ehom e 4 * x 2 - ehom e 3 * x 3)
          * (ehom f 5 * y 1 + ehom f 4 * y 2 - ehom f 3 * y 3 - ehom f 2 * y 4) := by
  simp only [prodEffVal, pairVal, gC5_apply, gC5Fun_apply, prodState_apply, sum_univ_six']
  simp +decide [sgnC5, pcC5, ptC5]
  ring

theorem gC5_prodEffVal_nonneg {e f : (Fin 5 → ℝ) →ᵃ[ℝ] ℝ} (he : IsEffectOn (eball 5) e)
    (hf : IsEffectOn (eball 5) f) {x y : Fin 5 → ℝ} (hx : x ∈ eball 5) (hy : y ∈ eball 5) :
    0 ≤ prodEffVal e f (gC5 (prodState x y)) := by
  obtain ⟨he0, ha⟩ := selC5_lor (lor_ehom he)
  obtain ⟨hf0, hb⟩ := selC5_lor (lor_ehom hf)
  rw [mem_eball, Fin.sum_univ_five] at hx hy
  obtain ⟨hP, hQ, hPQ⟩ := selC5_target (ehom f 0) (ehom f 1) (ehom f 2) (ehom f 3) (ehom f 4)
    (ehom f 5) (y 0) (y 1) (y 2) (y 3) (y 4) hf0 hb hy
  have hC := selC5_core (ehom e 0) (ehom e 1) (ehom e 2) (ehom e 3) (ehom e 4) (ehom e 5)
    (x 0) (x 1) (x 2) (x 3) (x 4) _ _ _ _ he0 ha hx hP hQ hPQ
  rw [prodEffVal_gC5_prodState]
  linarith

/-- **Forward positivity.** -/
theorem gC5_posFwd :
    ∀ x ∈ eball 5, ∀ y ∈ eball 5, gC5 (prodState x y) ∈ maxCone (eball 5) := by
  intro x hx y hy
  show ∀ e f, IsEffectOn (eball 5) e → IsEffectOn (eball 5) f →
    0 ≤ prodEffVal e f (gC5 (prodState x y))
  intro e f he hf
  exact gC5_prodEffVal_nonneg he hf hx hy

/-- **Inverse positivity**: `gC5.symm` is `gC5`. -/
theorem gC5_posInv :
    ∀ x ∈ eball 5, ∀ y ∈ eball 5, gC5.symm (prodState x y) ∈ maxCone (eball 5) := by
  intro x hx y hy
  rw [gC5_symm_apply]
  exact gC5_posFwd x hx y hy

/-! ### §F — the separation -/

/-- **relT, the frame and two-sided positivity do not give relC** at `d = 5`. -/
theorem c5_sep :
    IsNot (eball 5) z5 nC5 ∧
      (∀ a b : Fin 2,
        gC5 (prodState (corner z5 a) (corner z5 b)) = prodState (corner z5 a) (corner z5 (a + b))) ∧
      (∀ ω, actT nC5 (gC5 (actT nC5 ω)) = gC5 ω) ∧
      (∀ x ∈ eball 5, ∀ y ∈ eball 5, gC5 (prodState x y) ∈ maxCone (eball 5)) ∧
      (∀ x ∈ eball 5, ∀ y ∈ eball 5, gC5.symm (prodState x y) ∈ maxCone (eball 5)) ∧
      ¬ (∀ ω, actC nC5 (gC5 (actC nC5 ω)) = actT nC5 (gC5 ω)) :=
  ⟨isNot_nC5, gC5_frame, gC5_relT, gC5_posFwd, gC5_posInv, gC5_not_relC⟩

theorem not_nativeGate_gC5 : ¬ NativeGate (eball 5) z5 nC5 gC5 :=
  fun hG => gC5_not_relC hG.relC

/-- **Without the control relation the selector fails**: `IsNot`, the frame, two-sided
positivity and the target relation do not force `d = 1 ∨ d = 3`. -/
theorem relT_not_dimension_selecting :
    ¬ ∀ (d : ℕ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d),
      IsNot (eball d) z N →
      (∀ a b : Fin 2,
        G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))) →
      (∀ x ∈ eball d, ∀ y ∈ eball d, G (prodState x y) ∈ maxCone (eball d)) →
      (∀ x ∈ eball d, ∀ y ∈ eball d, G.symm (prodState x y) ∈ maxCone (eball d)) →
      (∀ ω, actT N (G (actT N ω)) = G ω) →
      d = 1 ∨ d = 3 := by
  intro h
  have h5 := h 5 z5 nC5 gC5 isNot_nC5 gC5_frame gC5_posFwd gC5_posInv gC5_relT
  omega

end RelcSelect
end OIBridge

#print axioms OIBridge.RelcSelect.isNot_nC5
#print axioms OIBridge.RelcSelect.gC5_frame
#print axioms OIBridge.RelcSelect.gC5_relT
#print axioms OIBridge.RelcSelect.gC5_not_relC
#print axioms OIBridge.RelcSelect.selC5_target
#print axioms OIBridge.RelcSelect.selC5_core
#print axioms OIBridge.RelcSelect.prodEffVal_gC5_prodState
#print axioms OIBridge.RelcSelect.gC5_posFwd
#print axioms OIBridge.RelcSelect.gC5_posInv
#print axioms OIBridge.RelcSelect.c5_sep
#print axioms OIBridge.RelcSelect.not_nativeGate_gC5
#print axioms OIBridge.RelcSelect.relT_not_dimension_selecting
