/-
  OIBridge/BridgeDictionary.lean — design module of the research thread `research/bridge`
  (round 3, node B11). Not certified. Built on the disposable branch `dev-bridge/r3-dict` only;
  not for merge. The round-2 draft of this module (node B9) did not build; this version replaces
  it.

  The two-token dictionary of handoff HO-6, at the table level of DIM-1's pair carrier `W 3`, in
  the kernel's own tensor `tensorOf` (MonoidalCompletion.lean), the operation `ContextStable` uses:
    `tokMat v = ½ Σ v_μ σ_μ`        one token's homogenized vector as a 2 × 2 complex matrix;
    `dict ω = ¼ Σ ω_μν σ_μ ⊗ σ_ν`   a pair table as a 4 × 4 complex matrix.

  Proved here:
    §A  (D1) the product law `dict (tens X Y) = tensorOf (tokMat X) (tokMat Y)` (`dict_tens`), hence
        `dict (prodState x y) = tensorOf (tokMat (hom x)) (tokMat (hom y))` (`dict_prodState`);
    §B  (D2) the gate: `dict (cnot ω) = cnotMat * dict ω * cnotMat`, with
        `cnotMat = |0⟩⟨0| ⊗ 1 + |1⟩⟨1| ⊗ X` (`dict_cnot`);
    §C  (D2) the monomial images. `rotZ c s` is the rotation of the ball by `(c, s)` about the third
        axis; at `(c, s) = (cos t, sin t)` it is the kernel's `rotLin t` (`rotZ_cos_sin`).
        `zPhase c s = diag(1, c + i s)`. On the unit circle the two local actions are intertwined with
        conjugation by the idle extensions: `dict (actT (rotZ c s) ω) = Ad(1 ⊗ zPhase c s) (dict ω)`
        (`dict_actT_rotZ`) and `dict (actC (rotZ c s) ω) = Ad(zPhase c s ⊗ 1) (dict ω)`
        (`dict_actC_rotZ`). The NOT: `dict (actT nflip ω) = Ad(1 ⊗ X) (dict ω)`,
        `dict (actC nflip ω) = Ad(X ⊗ 1) (dict ω)` (`dict_actT_nflip`, `dict_actC_nflip`). The unit
        circle enters only through the one-token identities `zPhase_pauli0` and `zPhase_pauli3`; the
        pair identities follow from the generic conjugation formulas `conj_dict_right`,
        `conj_dict_left` (Mathlib's Kronecker algebra);
    §D  the certified `substratumClass_contextStable` at the pair carrier
        (`monomial_extension_admissible`); the transfer clause `TransferClause` as a definition; and
        its pull-back to the phase rotations: on a cone `K` satisfying the clause for the substratum
        class, every rotated table `actT (rotZ c s) ω`, `ω ∈ K`, `c² + s² = 1`, has the dictionary image
        of a member of `K` (`transfer_phase`);
    §E  controls: the circle hypothesis is satisfiable at the rational point `(3/5, 4/5)`
        (`dict_actT_rotZ_345`), and it is load-bearing: off the circle the phase conjugation does not
        fix the identity (`zPhase_pauli0_counter`).

  The dictionary is a comparison and construction tool. Nothing here is a premise about a pair cone,
  and nothing sources the transfer clause. `transfer_phase` concludes equality of dictionary images;
  injectivity of the dictionary is not proved here.

  Kernel check (dev branch):  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.CompositeDimension
import OIBridge.MonoidalCompletion
import OIBridge.ImplementationLocality
import OIBridge.StructuralClosure
import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Module

namespace OIBridge
namespace BridgeDictionary

open CompositeDimension MonoidalCompletion InterventionLocality StructuralClosure KInfFoundations
open SubstratumInterface Matrix
open scoped Kronecker

/-! ### The dictionary -/

/-- The Pauli matrices `σ₀ = 1, σ₁ = X, σ₂ = Y, σ₃ = Z`. -/
noncomputable def pauli : Fin 4 → Matrix (Fin 2) (Fin 2) ℂ :=
  ![1, !![0, 1; 1, 0], !![0, -Complex.I; Complex.I, 0], !![1, 0; 0, -1]]

/-- One token's homogenized vector as a 2 × 2 complex matrix: `v ↦ ½ Σ v_μ σ_μ`. -/
noncomputable def tokMat (v : HVec 3) : Matrix (Fin 2) (Fin 2) ℂ :=
  ∑ μ : Fin 4, ((v μ : ℂ) / 2) • pauli μ

/-- The two-token dictionary: `ω ↦ ¼ Σ ω_μν σ_μ ⊗ σ_ν`. -/
noncomputable def dict (ω : W 3) : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ :=
  ∑ μ : Fin 4, ∑ ν : Fin 4, ((ω μ ν : ℂ) / 4) • tensorOf (pauli μ) (pauli ν)

/-- The kernel's tensor is Mathlib's Kronecker product. -/
theorem tensorOf_eq_kron (XA XB : Matrix (Fin 2) (Fin 2) ℂ) : tensorOf XA XB = XA ⊗ₖ XB := rfl

/-! ### §A — (D1) the product law -/

/-- **The product law of the dictionary.** -/
theorem dict_tens (X Y : HVec 3) : dict (tens X Y) = tensorOf (tokMat X) (tokMat Y) := by
  ext ⟨i, j⟩ ⟨k, l⟩
  simp only [dict, tokMat, tens_apply, Matrix.sum_apply, Matrix.smul_apply, tensorOf_apply,
    smul_eq_mul, Complex.ofReal_mul]
  simp only [Fin.sum_univ_four]
  ring

/-- The product states of the ball go to Kronecker products of one-token matrices. -/
theorem dict_prodState (x y : Fin 3 → ℝ) :
    dict (prodState x y) = tensorOf (tokMat (hom x)) (tokMat (hom y)) :=
  dict_tens (hom x) (hom y)

/-! ### §B — (D2) the gate -/

/-- The projector `|0⟩⟨0|`. -/
noncomputable def projZero : Matrix (Fin 2) (Fin 2) ℂ := Matrix.diagonal ![1, 0]

/-- The projector `|1⟩⟨1|`. -/
noncomputable def projOne : Matrix (Fin 2) (Fin 2) ℂ := Matrix.diagonal ![0, 1]

/-- The controlled NOT on `ℂ² ⊗ ℂ²`, control first: `|0⟩⟨0| ⊗ 1 + |1⟩⟨1| ⊗ X`. -/
noncomputable def cnotMat : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ :=
  tensorOf projZero 1 + tensorOf projOne (pauli 1)

set_option maxHeartbeats 8000000 in
/-- **(D2), the gate.** The kernel's `d = 3` gate is conjugation by the controlled NOT. -/
theorem dict_cnot (ω : W 3) : dict (cnot ω) = cnotMat * dict ω * cnotMat := by
  ext ⟨i, j⟩ ⟨k, l⟩
  fin_cases i <;> fin_cases j <;> fin_cases k <;> fin_cases l <;>
    simp only [dict, cnotMat, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two,
      Fin.sum_univ_four, Matrix.sum_apply, Matrix.add_apply, Matrix.smul_apply, smul_eq_mul,
      tensorOf_apply] <;>
    simp +decide [cnot_apply, cnotFun, cnotFun_apply, sgn, pc, pt, pauli, projZero, projOne,
      Matrix.one_apply, Matrix.diagonal_apply] <;>
    ring

/-! ### §C — (D2) the monomial images -/

/-- The rotation of the ball by `(c, s)` about the third axis. -/
def rotZ (c s : ℝ) : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) where
  toFun x := ![c * x 0 - s * x 1, s * x 0 + c * x 1, x 2]
  map_add' x y := by
    first
    | (apply vec3_ext <;> simp <;> ring1)
    | (funext m; fin_cases m <;> simp <;> ring1)
  map_smul' r x := by
    first
    | (apply vec3_ext <;> simp <;> ring1)
    | (funext m; fin_cases m <;> simp <;> ring1)

/-- At `(cos t, sin t)` it is the kernel's rotation `rotLin t` (the flow of `ball3Drive`). -/
theorem rotZ_cos_sin (t : ℝ) : rotZ (Real.cos t) (Real.sin t) = rotLin t := by
  apply LinearMap.ext
  intro x
  apply vec3_ext <;> first | rfl | simp [rotZ, rotLin, rotFun]

theorem homMap_rotZ_zero (c s : ℝ) (v : HVec 3) :
    homMap (rotZ c s) v (0 : Fin 4) = v (0 : Fin 4) := by
  first | rfl | simp [homMap, rotZ]

theorem homMap_rotZ_one (c s : ℝ) (v : HVec 3) :
    homMap (rotZ c s) v (1 : Fin 4) = c * v (1 : Fin 4) - s * v (2 : Fin 4) := by
  first | rfl | (simp [homMap, rotZ, Matrix.vecTail] <;> ring1)

theorem homMap_rotZ_two (c s : ℝ) (v : HVec 3) :
    homMap (rotZ c s) v (2 : Fin 4) = s * v (1 : Fin 4) + c * v (2 : Fin 4) := by
  first | rfl | (simp [homMap, rotZ, Matrix.vecTail] <;> ring1)

theorem homMap_rotZ_three (c s : ℝ) (v : HVec 3) :
    homMap (rotZ c s) v (3 : Fin 4) = v (3 : Fin 4) := by
  first | rfl | simp [homMap, rotZ, Matrix.vecTail]

theorem homMap_nflip_zero' (v : HVec 3) : homMap nflip v (0 : Fin 4) = v (0 : Fin 4) := by
  first | rfl | exact homMap_nflip_zero v

theorem homMap_nflip_one' (v : HVec 3) : homMap nflip v (1 : Fin 4) = v (1 : Fin 4) := by
  first | exact homMap_nflip_one v | (show 1 * v 1 = v 1; ring1)

theorem homMap_nflip_two' (v : HVec 3) : homMap nflip v (2 : Fin 4) = -v (2 : Fin 4) := by
  first | exact homMap_nflip_two v | (show -1 * v 2 = -v 2; ring1)

theorem homMap_nflip_three' (v : HVec 3) : homMap nflip v (3 : Fin 4) = -v (3 : Fin 4) := by
  first | exact homMap_nflip_three v | (show -1 * v 3 = -v 3; ring1)

/-- The phase `diag(1, c + i s)`: a monomial one-token operator, unitary on the unit circle. -/
noncomputable def zPhase (c s : ℝ) : Matrix (Fin 2) (Fin 2) ℂ :=
  Matrix.diagonal ![1, (c : ℂ) + (s : ℂ) * Complex.I]

/-- The adjoint of `zPhase c s`, written out. -/
noncomputable def zPhaseD (c s : ℝ) : Matrix (Fin 2) (Fin 2) ℂ :=
  Matrix.diagonal ![1, (c : ℂ) - (s : ℂ) * Complex.I]

theorem zPhase_conjTranspose (c s : ℝ) : (zPhase c s)ᴴ = zPhaseD c s := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [zPhase, zPhaseD, Matrix.conjTranspose_apply, Matrix.diagonal_apply] <;> ring1

/-- `σ₀` under the phase: fixed exactly on the unit circle. -/
theorem zPhase_pauli0 (c s : ℝ) (h : c ^ 2 + s ^ 2 = 1) :
    zPhase c s * pauli 0 * (zPhase c s)ᴴ = pauli 0 := by
  have hc : (c : ℂ) ^ 2 + (s : ℂ) ^ 2 = 1 := by exact_mod_cast h
  rw [zPhase_conjTranspose]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [zPhase, zPhaseD, pauli, Matrix.mul_apply, Fin.sum_univ_two, Matrix.diagonal_apply,
      Matrix.one_apply] <;>
    first
    | ring1
    | linear_combination hc - (s : ℂ) ^ 2 * Complex.I_sq
    | linear_combination -hc + (s : ℂ) ^ 2 * Complex.I_sq
    | linear_combination hc
    | linear_combination -hc
    | linear_combination hc + (s : ℂ) ^ 2 * Complex.I_sq
    | linear_combination -hc - (s : ℂ) ^ 2 * Complex.I_sq

/-- `σ₁` under the phase: `c σ₁ + s σ₂` (no circle needed). -/
theorem zPhase_pauli1 (c s : ℝ) :
    zPhase c s * pauli 1 * (zPhase c s)ᴴ = (c : ℂ) • pauli 1 + (s : ℂ) • pauli 2 := by
  rw [zPhase_conjTranspose]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [zPhase, zPhaseD, pauli, Matrix.mul_apply, Fin.sum_univ_two, Matrix.diagonal_apply] <;>
    first
    | ring1
    | linear_combination (s : ℂ) * Complex.I_sq
    | linear_combination -(s : ℂ) * Complex.I_sq
    | linear_combination (c : ℂ) * Complex.I_sq
    | linear_combination -(c : ℂ) * Complex.I_sq

/-- `σ₂` under the phase: `−s σ₁ + c σ₂` (no circle needed). -/
theorem zPhase_pauli2 (c s : ℝ) :
    zPhase c s * pauli 2 * (zPhase c s)ᴴ = (-(s : ℂ)) • pauli 1 + (c : ℂ) • pauli 2 := by
  rw [zPhase_conjTranspose]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [zPhase, zPhaseD, pauli, Matrix.mul_apply, Fin.sum_univ_two, Matrix.diagonal_apply] <;>
    first
    | ring1
    | linear_combination (s : ℂ) * Complex.I_sq
    | linear_combination -(s : ℂ) * Complex.I_sq
    | linear_combination (c : ℂ) * Complex.I_sq
    | linear_combination -(c : ℂ) * Complex.I_sq

/-- `σ₃` under the phase: fixed exactly on the unit circle. -/
theorem zPhase_pauli3 (c s : ℝ) (h : c ^ 2 + s ^ 2 = 1) :
    zPhase c s * pauli 3 * (zPhase c s)ᴴ = pauli 3 := by
  have hc : (c : ℂ) ^ 2 + (s : ℂ) ^ 2 = 1 := by exact_mod_cast h
  rw [zPhase_conjTranspose]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [zPhase, zPhaseD, pauli, Matrix.mul_apply, Fin.sum_univ_two, Matrix.diagonal_apply] <;>
    first
    | ring1
    | linear_combination hc - (s : ℂ) ^ 2 * Complex.I_sq
    | linear_combination -hc + (s : ℂ) ^ 2 * Complex.I_sq
    | linear_combination hc
    | linear_combination -hc
    | linear_combination hc + (s : ℂ) ^ 2 * Complex.I_sq
    | linear_combination -hc - (s : ℂ) ^ 2 * Complex.I_sq

/-- The NOT `X = σ₁` on the four Pauli matrices: `σ₀, σ₁` fixed, `σ₂, σ₃` negated. -/
theorem x_pauli0 : pauli 1 * pauli 0 * (pauli 1)ᴴ = pauli 0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [pauli, Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply,
      Matrix.one_apply] <;> first | rfl | ring1

theorem x_pauli1 : pauli 1 * pauli 1 * (pauli 1)ᴴ = pauli 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [pauli, Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply] <;>
    first | rfl | ring1

theorem x_pauli2 : pauli 1 * pauli 2 * (pauli 1)ᴴ = (-1 : ℂ) • pauli 2 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [pauli, Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply] <;>
    first | rfl | ring1

theorem x_pauli3 : pauli 1 * pauli 3 * (pauli 1)ᴴ = (-1 : ℂ) • pauli 3 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [pauli, Matrix.mul_apply, Fin.sum_univ_two, Matrix.conjTranspose_apply] <;>
    first | rfl | ring1

/-- **Conjugation by an idle extension on the target, term by term.** -/
theorem conj_dict_right (U : Matrix (Fin 2) (Fin 2) ℂ) (ω : W 3) :
    tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) U * dict ω *
        (tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) U)ᴴ =
      ∑ μ : Fin 4, ∑ ν : Fin 4, ((ω μ ν : ℂ) / 4) • tensorOf (pauli μ) (U * pauli ν * Uᴴ) := by
  simp only [dict, tensorOf_eq_kron, Finset.mul_sum, Finset.sum_mul, Matrix.mul_smul,
    Matrix.smul_mul, Matrix.conjTranspose_kronecker, Matrix.conjTranspose_one,
    ← Matrix.mul_kronecker_mul, Matrix.one_mul, Matrix.mul_one]

/-- **Conjugation by an idle extension on the control, term by term.** -/
theorem conj_dict_left (U : Matrix (Fin 2) (Fin 2) ℂ) (ω : W 3) :
    tensorOf U (1 : Matrix (Fin 2) (Fin 2) ℂ) * dict ω *
        (tensorOf U (1 : Matrix (Fin 2) (Fin 2) ℂ))ᴴ =
      ∑ μ : Fin 4, ∑ ν : Fin 4, ((ω μ ν : ℂ) / 4) • tensorOf (U * pauli μ * Uᴴ) (pauli ν) := by
  simp only [dict, tensorOf_eq_kron, Finset.mul_sum, Finset.sum_mul, Matrix.mul_smul,
    Matrix.smul_mul, Matrix.conjTranspose_kronecker, Matrix.conjTranspose_one,
    ← Matrix.mul_kronecker_mul, Matrix.one_mul, Matrix.mul_one]

set_option maxHeartbeats 4000000 in
/-- **(D2), the phase rotation on the target.** On the unit circle, the target action of the
rotation about the third axis is conjugation by the idle extension `1 ⊗ diag(1, c + i s)`. -/
theorem dict_actT_rotZ (c s : ℝ) (h : c ^ 2 + s ^ 2 = 1) (ω : W 3) :
    dict (actT (rotZ c s) ω) =
      tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) (zPhase c s) * dict ω *
        (tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) (zPhase c s))ᴴ := by
  rw [conj_dict_right]
  simp only [dict, Fin.sum_univ_four, actT, homMap_rotZ_zero, homMap_rotZ_one, homMap_rotZ_two,
    homMap_rotZ_three, zPhase_pauli0 c s h, zPhase_pauli1, zPhase_pauli2, zPhase_pauli3 c s h,
    tensorOf_eq_kron, Matrix.kronecker_add, Matrix.kronecker_smul, Complex.ofReal_sub,
    Complex.ofReal_add, Complex.ofReal_mul]
  module

set_option maxHeartbeats 4000000 in
/-- **(D2), the phase rotation on the control.** -/
theorem dict_actC_rotZ (c s : ℝ) (h : c ^ 2 + s ^ 2 = 1) (ω : W 3) :
    dict (actC (rotZ c s) ω) =
      tensorOf (zPhase c s) (1 : Matrix (Fin 2) (Fin 2) ℂ) * dict ω *
        (tensorOf (zPhase c s) (1 : Matrix (Fin 2) (Fin 2) ℂ))ᴴ := by
  rw [conj_dict_left]
  simp only [dict, Fin.sum_univ_four, actC, homMap_rotZ_zero, homMap_rotZ_one, homMap_rotZ_two,
    homMap_rotZ_three, zPhase_pauli0 c s h, zPhase_pauli1, zPhase_pauli2, zPhase_pauli3 c s h,
    tensorOf_eq_kron, Matrix.add_kronecker, Matrix.smul_kronecker, Complex.ofReal_sub,
    Complex.ofReal_add, Complex.ofReal_mul]
  module

set_option maxHeartbeats 4000000 in
/-- **(D2), the NOT on the target.** -/
theorem dict_actT_nflip (ω : W 3) :
    dict (actT nflip ω) =
      tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) (pauli 1) * dict ω *
        (tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) (pauli 1))ᴴ := by
  rw [conj_dict_right]
  simp only [dict, Fin.sum_univ_four, actT, homMap_nflip_zero', homMap_nflip_one',
    homMap_nflip_two', homMap_nflip_three', x_pauli0, x_pauli1, x_pauli2, x_pauli3,
    tensorOf_eq_kron, Matrix.kronecker_smul, Complex.ofReal_neg]
  module

set_option maxHeartbeats 4000000 in
/-- **(D2), the NOT on the control.** -/
theorem dict_actC_nflip (ω : W 3) :
    dict (actC nflip ω) =
      tensorOf (pauli 1) (1 : Matrix (Fin 2) (Fin 2) ℂ) * dict ω *
        (tensorOf (pauli 1) (1 : Matrix (Fin 2) (Fin 2) ℂ))ᴴ := by
  rw [conj_dict_left]
  simp only [dict, Fin.sum_univ_four, actC, homMap_nflip_zero', homMap_nflip_one',
    homMap_nflip_two', homMap_nflip_three', x_pauli0, x_pauli1, x_pauli2, x_pauli3,
    tensorOf_eq_kron, Matrix.smul_kronecker, Complex.ofReal_neg]
  module

/-! ### §D — the certified context stability at the pair carrier, and the transfer clause -/

/-- **The certified spectator theorem at the pair carrier**: the idle extension of a monomial
one-token operator is admissible on `Fin 2 × Fin 2` (`substratumClass_contextStable`). -/
theorem monomial_extension_admissible (U : Matrix (Fin 2) (Fin 2) ℂ)
    (hU : substratumClass (Fin 2) U) :
    substratumClass (Fin 2 × Fin 2) (tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) U) :=
  substratumClass_contextStable (Fin 2) (Fin 2) U hU

/-- **The M→P transfer clause** (a design statement, not a premise of anything here): for every
admissible unitary `U` on one token and every `ω ∈ K`, conjugation of `dict ω` by the idle
extension `tensorOf 1 U` is the dictionary image of a member of `K`. -/
def TransferClause (𝓘 : ImplementationClass) (K : Set (W 3)) : Prop :=
  ∀ U : Matrix (Fin 2) (Fin 2) ℂ, 𝓘 (Fin 2) U → Uᴴ * U = 1 →
    ∀ ω ∈ K, ∃ ω' ∈ K,
      dict ω' = tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) U * dict ω *
        (tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) U)ᴴ

/-- The phase is in the substratum class (a diagonal operator is monomial). -/
theorem zPhase_monomial (c s : ℝ) : substratumClass (Fin 2) (zPhase c s) := by
  first
  | exact monomial_diagonal _
  | (show IsMonomial (zPhase c s); exact monomial_diagonal _)

/-- The phase is unitary on the unit circle. -/
theorem zPhase_unitary (c s : ℝ) (h : c ^ 2 + s ^ 2 = 1) : (zPhase c s)ᴴ * zPhase c s = 1 := by
  have hc : (c : ℂ) ^ 2 + (s : ℂ) ^ 2 = 1 := by exact_mod_cast h
  rw [zPhase_conjTranspose]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [zPhase, zPhaseD, Matrix.mul_apply, Fin.sum_univ_two, Matrix.diagonal_apply,
      Matrix.one_apply] <;>
    first
    | ring1
    | linear_combination hc - (s : ℂ) ^ 2 * Complex.I_sq
    | linear_combination -hc + (s : ℂ) ^ 2 * Complex.I_sq
    | linear_combination hc
    | linear_combination -hc

/-- **The transfer clause pulls back to the phase rotations.** On a pair cone satisfying the clause
for the substratum class, every table rotated on the target by a point of the unit circle has the
dictionary image of a member of the cone. -/
theorem transfer_phase {K : Set (W 3)} (hT : TransferClause substratumClass K) (c s : ℝ)
    (h : c ^ 2 + s ^ 2 = 1) {ω : W 3} (hω : ω ∈ K) :
    ∃ ω' ∈ K, dict ω' = dict (actT (rotZ c s) ω) := by
  obtain ⟨ω', hω', heq⟩ := hT (zPhase c s) (zPhase_monomial c s) (zPhase_unitary c s h) ω hω
  exact ⟨ω', hω', heq.trans (dict_actT_rotZ c s h ω).symm⟩

/-! ### §E — controls -/

/-- **Positive control**: the circle hypothesis holds at the rational point `(3/5, 4/5)`. -/
theorem dict_actT_rotZ_345 (ω : W 3) :
    dict (actT (rotZ (3 / 5) (4 / 5)) ω) =
      tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) (zPhase (3 / 5) (4 / 5)) * dict ω *
        (tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) (zPhase (3 / 5) (4 / 5)))ᴴ :=
  dict_actT_rotZ (3 / 5) (4 / 5) (by norm_num) ω

/-- **Countercontrol**: off the unit circle the phase conjugation does not fix `σ₀`, so the circle
hypothesis of `zPhase_pauli0` (and of the intertwinings) is load-bearing. -/
theorem zPhase_pauli0_counter : zPhase 0 0 * pauli 0 * (zPhase 0 0)ᴴ ≠ pauli 0 := by
  intro heq
  have h11 := congrFun (congrFun heq 1) 1
  simp [zPhase, pauli, Matrix.mul_apply, Fin.sum_univ_two, Matrix.diagonal_apply,
    Matrix.conjTranspose_apply, Matrix.one_apply] at h11

#print axioms dict_tens
#print axioms dict_prodState
#print axioms dict_cnot
#print axioms rotZ_cos_sin
#print axioms zPhase_conjTranspose
#print axioms zPhase_pauli0
#print axioms zPhase_pauli1
#print axioms zPhase_pauli2
#print axioms zPhase_pauli3
#print axioms conj_dict_right
#print axioms conj_dict_left
#print axioms dict_actT_rotZ
#print axioms dict_actC_rotZ
#print axioms dict_actT_nflip
#print axioms dict_actC_nflip
#print axioms monomial_extension_admissible
#print axioms zPhase_unitary
#print axioms transfer_phase
#print axioms dict_actT_rotZ_345
#print axioms zPhase_pauli0_counter

end BridgeDictionary
end OIBridge
