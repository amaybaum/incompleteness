import OIBridge.DitaTorus

/-!
# Act 40 — the Diţă locus of the three-parameter family: the kernel layer

Act 39 proved the family `H3 u₁ u₂ u₃ = SIG ∘ u₁^A u₂^B u₃^C` through the certified rational stratum point
`SIG = F₄(z) ⊗ F₄(w)`, `z = (3+4i)/5`, `w = (5+12i)/13`, realizable at every point of the three-torus. This
module states the kernel layer of act 40's classification of the points of the torus at which `H3` admits a
Diţă structure. On each of the five coordinate faces `u₁ = 1`, `u₁ = −1`, `u₂ = 1`, `u₃ = 1`, `u₃ = −1`, and at
every point of the face, `H3` (or its transpose) is an explicit strict Diţă product `dita X Y D` of a named shape
and index map, with `X` and every `Y c` flat unitary and `‖D c b‖ = 1`. For each of twenty named index maps — act
37's nine classes in both orientations and act 38's two maps `M_COL` and `M_ROW` — a strict Diţă form of `H3` at
that map forces the named coordinate equations. The module does not state that the five faces exhaust the
points admitting a Diţă structure: that converse, over every shape, index map and orientation and up to
diagonal equivalence, is certified by the round's exact-computation probe, not by the kernel.

The module carries no definition. Every theorem prints its axioms.
-/

namespace OIBridge
namespace DitaTorusLocus

open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted
  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries
  OrbitGeometryRigidity OrbitIsometryGroup ProductStratum DitaHull DitaHierarchy DitaArcExclusivity DitaLocalEscape DitaTorus

theorem a40_shared_inv_of_unit :
    ∀ x : ℂ, star x * x = 1 → star x = x⁻¹ := by
  intro x h
  exact eq_inv_of_mul_eq_one_left h
#print axioms a40_shared_inv_of_unit

theorem a40_shared_ne_zero_of_unit :
    ∀ x : ℂ, star x * x = 1 → x ≠ 0 := by
  intro x h hx
  rw [hx, mul_zero] at h
  exact zero_ne_one h
#print axioms a40_shared_ne_zero_of_unit

theorem a40_shared_k2 :
    (1 + Complex.I) / 2 * star ((1 + Complex.I) / 2) = 1 / 2 := by
  first
  | (apply Complex.ext <;> simp [Complex.star_def] <;> norm_num)
  | (apply Complex.ext <;> simp [Complex.conj_re, Complex.conj_im] <;> norm_num)
  | (simp [Complex.ext_iff, Complex.star_def]; norm_num)
  | (rw [Complex.ext_iff]; simp; norm_num)
#print axioms a40_shared_k2

theorem a40_shared_k8 :
    (1 + Complex.I) / 4 * star ((1 + Complex.I) / 4) = 1 / 8 := by
  first
  | (apply Complex.ext <;> simp [Complex.star_def] <;> norm_num)
  | (apply Complex.ext <;> simp [Complex.conj_re, Complex.conj_im] <;> norm_num)
  | (simp [Complex.ext_iff, Complex.star_def]; norm_num)
  | (rw [Complex.ext_iff]; simp; norm_num)
#print axioms a40_shared_k8

theorem a40_shared_k2sq :
    ‖(1 + Complex.I) / 2‖ ^ 2 = 1 / 2 := by
  have e : ‖(1 + Complex.I) / 2‖ ^ 2 = Complex.normSq ((1 + Complex.I) / 2) := by
    first
    | exact Complex.sq_norm _
    | exact Complex.sq_abs _
    | simp [Complex.sq_abs]
    | (rw [← Complex.normSq_eq_norm_sq])
  rw [e]
  first
  | (simp [Complex.normSq_apply]; norm_num)
  | (rw [Complex.normSq_apply]; simp; norm_num)
  | norm_num [Complex.normSq_apply]
#print axioms a40_shared_k2sq

theorem a40_shared_k8sq :
    ‖(1 + Complex.I) / 4‖ ^ 2 = 1 / 8 := by
  have e : ‖(1 + Complex.I) / 4‖ ^ 2 = Complex.normSq ((1 + Complex.I) / 4) := by
    first
    | exact Complex.sq_norm _
    | exact Complex.sq_abs _
    | simp [Complex.sq_abs]
    | (rw [← Complex.normSq_eq_norm_sq])
  rw [e]
  first
  | (simp [Complex.normSq_apply]; norm_num)
  | (rw [Complex.normSq_apply]; simp; norm_num)
  | norm_num [Complex.normSq_apply]
#print axioms a40_shared_k8sq

theorem a40_shared_one_add_I :
    (1 + Complex.I) ≠ 0 := by
  intro h
  have := congrArg Complex.re h
  simp at this
#print axioms a40_shared_one_add_I

theorem a40_shared_dval :
    (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I)) = -Complex.I := by
  have h := a40_shared_one_add_I
  rw [div_eq_iff (mul_ne_zero h h)]
  first
  | linear_combination (Complex.I + 2) * Complex.I_sq
  | linear_combination (-(Complex.I + 2)) * Complex.I_sq
  | (ring_nf; rw [Complex.I_sq]; ring)
  | (apply Complex.ext <;> simp <;> norm_num)
#print axioms a40_shared_dval

theorem a40_shared_fpe :
    ∀ (a : Fin 2) (b : Fin 4), @finProdFinEquiv 2 4 (a, b) = ![![(0 : Fin 8), 1, 2, 3], ![4, 5, 6, 7]] a b := by
  decide
#print axioms a40_shared_fpe

theorem a40_shared_dnorm :
    ‖(2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))‖ = 1 := by
  rw [a40_shared_dval, norm_neg, Complex.norm_I]
#print axioms a40_shared_dnorm

theorem a40_shared_scaled_unitary2 :
    ∀ M : Matrix (Fin 2) (Fin 2) ℂ, (∀ b b' : Fin 2, ∑ d : Fin 2, M b d * star (M b' d) = if b = b' then (2 : ℂ) else 0) → (Matrix.of fun b d : Fin 2 => (1 + Complex.I) / 2 * M b d) ∈ Matrix.unitaryGroup (Fin 2) ℂ := by
  intro M hM
  rw [Matrix.mem_unitaryGroup_iff]
  ext b b'
  rw [Matrix.mul_apply, Matrix.one_apply]
  simp only [Matrix.star_apply, Matrix.of_apply]
  have e : ∀ d, (1 + Complex.I) / 2 * M b d * star ((1 + Complex.I) / 2 * M b' d) = ((1 + Complex.I) / 2 * star ((1 + Complex.I) / 2)) * (M b d * star (M b' d)) := by
    intro d
    rw [star_mul']
    ring
  simp only [e, ← Finset.mul_sum, hM b b', a40_shared_k2]
  split_ifs <;> norm_num
#print axioms a40_shared_scaled_unitary2

theorem a40_shared_scaled_unitary8 :
    ∀ M : Matrix (Fin 8) (Fin 8) ℂ, (∀ b b' : Fin 8, ∑ d : Fin 8, M b d * star (M b' d) = if b = b' then (8 : ℂ) else 0) → (Matrix.of fun b d : Fin 8 => (1 + Complex.I) / 4 * M b d) ∈ Matrix.unitaryGroup (Fin 8) ℂ := by
  intro M hM
  rw [Matrix.mem_unitaryGroup_iff]
  ext b b'
  rw [Matrix.mul_apply, Matrix.one_apply]
  simp only [Matrix.star_apply, Matrix.of_apply]
  have e : ∀ d, (1 + Complex.I) / 4 * M b d * star ((1 + Complex.I) / 4 * M b' d) = ((1 + Complex.I) / 4 * star ((1 + Complex.I) / 4)) * (M b d * star (M b' d)) := by
    intro d
    rw [star_mul']
    ring
  simp only [e, ← Finset.mul_sum, hM b b', a40_shared_k8]
  split_ifs <;> norm_num
#print axioms a40_shared_scaled_unitary8

theorem a40_shared_x_flat :
    ((Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖(Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) := by
  refine ⟨?_, ?_⟩
  · apply a40_shared_scaled_unitary2
    intro b b'
    fin_cases b <;> fin_cases b' <;> simp [Fin.sum_univ_two] <;> norm_num
  · intro a c
    simp only [Matrix.of_apply]
    rw [norm_mul, mul_pow, a40_shared_k2sq]
    fin_cases a <;> fin_cases c <;> simp
#print axioms a40_shared_x_flat

theorem a40_shared_excl_k1_c_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2))) → u₂ = 1 ∧ u₃ = 1 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3
  have h0z : z ≠ 0 := a40_shared_ne_zero_of_unit z hz
  have h0w : w ≠ 0 := a40_shared_ne_zero_of_unit w hw
  have h01 : u₁ ≠ 0 := a40_shared_ne_zero_of_unit u₁ h1
  have h02 : u₂ ≠ 0 := a40_shared_ne_zero_of_unit u₂ h2
  have h03 : u₃ ≠ 0 := a40_shared_ne_zero_of_unit u₃ h3
  rintro ⟨X, Y, D, -, -, -, h⟩
  refine ⟨?_, ?_⟩
  · have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * (u₂)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) := by
      rw [h]
      simp only [Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
      (try ring)
    rw [e0, e1, e2, e3] at key
    have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
    have h5 : (1 : ℂ) * (u₂ - 1) = 0 := by linear_combination (-16 : ℂ) * key
    rcases mul_eq_zero.1 h5 with h6 | h6
    · exact absurd h6 hC
    · linear_combination h6
  · have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) = ((1 / 4 : ℂ) * (u₃)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) := by
      rw [h]
      simp only [Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
      (try ring)
    rw [e0, e1, e2, e3] at key
    have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
    have h5 : (1 : ℂ) * (u₃ - 1) = 0 := by linear_combination (-16 : ℂ) * key
    rcases mul_eq_zero.1 h5 with h6 | h6
    · exact absurd h6 hC
    · linear_combination h6
#print axioms a40_shared_excl_k1_c_core

theorem a40_shared_excl_k1_r_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2))ᵀ) → u₁ = 1 ∧ u₃ = 1 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3
  have h0z : z ≠ 0 := a40_shared_ne_zero_of_unit z hz
  have h0w : w ≠ 0 := a40_shared_ne_zero_of_unit w hw
  have h01 : u₁ ≠ 0 := a40_shared_ne_zero_of_unit u₁ h1
  have h02 : u₂ ≠ 0 := a40_shared_ne_zero_of_unit u₂ h2
  have h03 : u₃ ≠ 0 := a40_shared_ne_zero_of_unit u₃ h3
  rintro ⟨X, Y, D, -, -, -, h⟩
  refine ⟨?_, ?_⟩
  · have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * (z)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * (z * u₁)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) := by
      rw [h]
      simp only [Matrix.transpose_apply, Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
      (try ring)
    rw [e0, e1, e2, e3] at key
    have hC : (z : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
    have h5 : (z : ℂ) * (u₁ - 1) = 0 := by linear_combination (-16 : ℂ) * key
    rcases mul_eq_zero.1 h5 with h6 | h6
    · exact absurd h6 hC
    · linear_combination h6
  · have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * (u₃)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) := by
      rw [h]
      simp only [Matrix.transpose_apply, Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
      (try ring)
    rw [e0, e1, e2, e3] at key
    have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
    have h5 : (1 : ℂ) * (u₃ - 1) = 0 := by linear_combination (-16 : ℂ) * key
    rcases mul_eq_zero.1 h5 with h6 | h6
    · exact absurd h6 hC
    · linear_combination h6
#print axioms a40_shared_excl_k1_r_core

theorem a40_shared_excl_k2_c_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2) (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2))) → u₂ = 1 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3
  have h0z : z ≠ 0 := a40_shared_ne_zero_of_unit z hz
  have h0w : w ≠ 0 := a40_shared_ne_zero_of_unit w hw
  have h01 : u₁ ≠ 0 := a40_shared_ne_zero_of_unit u₁ h1
  have h02 : u₂ ≠ 0 := a40_shared_ne_zero_of_unit u₂ h2
  have h03 : u₃ ≠ 0 := a40_shared_ne_zero_of_unit u₃ h3
  rintro ⟨X, Y, D, -, -, -, h⟩
  have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (3 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * (u₂)) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (3 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (3 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (3 : Fin 4)) := by
    rw [h]
    simp only [Matrix.of_apply]
    (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
    (try ring)
  rw [e0, e1, e2, e3] at key
  have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
  have h5 : (1 : ℂ) * (u₂ - 1) = 0 := by linear_combination (16 : ℂ) * key
  rcases mul_eq_zero.1 h5 with h6 | h6
  · exact absurd h6 hC
  · linear_combination h6
#print axioms a40_shared_excl_k2_c_core

theorem a40_shared_excl_k2_r_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2) (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2))ᵀ) → u₂ = 1 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3
  have h0z : z ≠ 0 := a40_shared_ne_zero_of_unit z hz
  have h0w : w ≠ 0 := a40_shared_ne_zero_of_unit w hw
  have h01 : u₁ ≠ 0 := a40_shared_ne_zero_of_unit u₁ h1
  have h02 : u₂ ≠ 0 := a40_shared_ne_zero_of_unit u₂ h2
  have h03 : u₃ ≠ 0 := a40_shared_ne_zero_of_unit u₃ h3
  rintro ⟨X, Y, D, -, -, -, h⟩
  have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * (u₂)) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (3 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (3 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (3 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (3 : Fin 4)) := by
    rw [h]
    simp only [Matrix.transpose_apply, Matrix.of_apply]
    (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
    (try ring)
  rw [e0, e1, e2, e3] at key
  have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
  have h5 : (1 : ℂ) * (u₂ - 1) = 0 := by linear_combination (16 : ℂ) * key
  rcases mul_eq_zero.1 h5 with h6 | h6
  · exact absurd h6 hC
  · linear_combination h6
#print axioms a40_shared_excl_k2_r_core

theorem a40_shared_excl_k3_c_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2) (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2))) → u₂ = 1 ∧ u₃ = 1 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3
  have h0z : z ≠ 0 := a40_shared_ne_zero_of_unit z hz
  have h0w : w ≠ 0 := a40_shared_ne_zero_of_unit w hw
  have h01 : u₁ ≠ 0 := a40_shared_ne_zero_of_unit u₁ h1
  have h02 : u₂ ≠ 0 := a40_shared_ne_zero_of_unit u₂ h2
  have h03 : u₃ ≠ 0 := a40_shared_ne_zero_of_unit u₃ h3
  rintro ⟨X, Y, D, -, -, -, h⟩
  refine ⟨?_, ?_⟩
  · have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * (u₂)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (1 : Fin 4)) := by
      rw [h]
      simp only [Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
      (try ring)
    rw [e0, e1, e2, e3] at key
    have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
    have h5 : (1 : ℂ) * (u₂ - 1) = 0 := by linear_combination (-16 : ℂ) * key
    rcases mul_eq_zero.1 h5 with h6 | h6
    · exact absurd h6 hC
    · linear_combination h6
  · have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (2 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (2 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) = ((1 / 4 : ℂ) * (u₃)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (2 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (2 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) := by
      rw [h]
      simp only [Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
      (try ring)
    rw [e0, e1, e2, e3] at key
    have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
    have h5 : (1 : ℂ) * (u₃ - 1) = 0 := by linear_combination (-16 : ℂ) * key
    rcases mul_eq_zero.1 h5 with h6 | h6
    · exact absurd h6 hC
    · linear_combination h6
#print axioms a40_shared_excl_k3_c_core

theorem a40_shared_excl_k3_r_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2) (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2))ᵀ) → u₁ = 1 ∧ u₂ = 1 ∧ u₃ = 1 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3
  have h0z : z ≠ 0 := a40_shared_ne_zero_of_unit z hz
  have h0w : w ≠ 0 := a40_shared_ne_zero_of_unit w hw
  have h01 : u₁ ≠ 0 := a40_shared_ne_zero_of_unit u₁ h1
  have h02 : u₂ ≠ 0 := a40_shared_ne_zero_of_unit u₂ h2
  have h03 : u₃ ≠ 0 := a40_shared_ne_zero_of_unit u₃ h3
  rintro ⟨X, Y, D, -, -, -, h⟩
  refine ⟨?_, ?_, ?_⟩
  · have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (3 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (2 : Fin 4)) = ((1 / 4 : ℂ) * (z)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (3 : Fin 4)) ((1 : Fin 4), (2 : Fin 4)) = ((1 / 4 : ℂ) * (z * u₁)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (3 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (2 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (3 : Fin 4)) ((1 : Fin 4), (2 : Fin 4)) := by
      rw [h]
      simp only [Matrix.transpose_apply, Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
      (try ring)
    rw [e0, e1, e2, e3] at key
    have hC : (z : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
    have h5 : (z : ℂ) * (u₁ - 1) = 0 := by linear_combination (-16 : ℂ) * key
    rcases mul_eq_zero.1 h5 with h6 | h6
    · exact absurd h6 hC
    · linear_combination h6
  · have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * (w * u₂)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (3 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (3 : Fin 4)) = ((1 / 4 : ℂ) * (w)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (3 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (3 : Fin 4)) := by
      rw [h]
      simp only [Matrix.transpose_apply, Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
      (try ring)
    rw [e0, e1, e2, e3] at key
    have hC : (w : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
    have h5 : (w : ℂ) * (u₂ - 1) = 0 := by linear_combination (16 : ℂ) * key
    rcases mul_eq_zero.1 h5 with h6 | h6
    · exact absurd h6 hC
    · linear_combination h6
  · have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (1 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * (u₃)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (1 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) := by
      rw [h]
      simp only [Matrix.transpose_apply, Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
      (try ring)
    rw [e0, e1, e2, e3] at key
    have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
    have h5 : (1 : ℂ) * (u₃ - 1) = 0 := by linear_combination (-16 : ℂ) * key
    rcases mul_eq_zero.1 h5 with h6 | h6
    · exact absurd h6 hC
    · linear_combination h6
#print axioms a40_shared_excl_k3_r_core

theorem a40_shared_excl_k4_c_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2) (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2))) → u₁ = 1 ∧ u₃ = 1 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3
  have h0z : z ≠ 0 := a40_shared_ne_zero_of_unit z hz
  have h0w : w ≠ 0 := a40_shared_ne_zero_of_unit w hw
  have h01 : u₁ ≠ 0 := a40_shared_ne_zero_of_unit u₁ h1
  have h02 : u₂ ≠ 0 := a40_shared_ne_zero_of_unit u₂ h2
  have h03 : u₃ ≠ 0 := a40_shared_ne_zero_of_unit u₃ h3
  rintro ⟨X, Y, D, -, -, -, h⟩
  refine ⟨?_, ?_⟩
  · have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * (z)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * (z * u₁)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) := by
      rw [h]
      simp only [Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
      (try ring)
    rw [e0, e1, e2, e3] at key
    have hC : (z : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
    have h5 : (z : ℂ) * (u₁ - 1) = 0 := by linear_combination (-16 : ℂ) * key
    rcases mul_eq_zero.1 h5 with h6 | h6
    · exact absurd h6 hC
    · linear_combination h6
  · have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * (u₃)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) := by
      rw [h]
      simp only [Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
      (try ring)
    rw [e0, e1, e2, e3] at key
    have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
    have h5 : (1 : ℂ) * (u₃ - 1) = 0 := by linear_combination (-16 : ℂ) * key
    rcases mul_eq_zero.1 h5 with h6 | h6
    · exact absurd h6 hC
    · linear_combination h6
#print axioms a40_shared_excl_k4_c_core

theorem a40_shared_excl_k4_r_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2) (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2))ᵀ) → u₂ = 1 ∧ u₃ = 1 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3
  have h0z : z ≠ 0 := a40_shared_ne_zero_of_unit z hz
  have h0w : w ≠ 0 := a40_shared_ne_zero_of_unit w hw
  have h01 : u₁ ≠ 0 := a40_shared_ne_zero_of_unit u₁ h1
  have h02 : u₂ ≠ 0 := a40_shared_ne_zero_of_unit u₂ h2
  have h03 : u₃ ≠ 0 := a40_shared_ne_zero_of_unit u₃ h3
  rintro ⟨X, Y, D, -, -, -, h⟩
  refine ⟨?_, ?_⟩
  · have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * (u₂)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) := by
      rw [h]
      simp only [Matrix.transpose_apply, Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
      (try ring)
    rw [e0, e1, e2, e3] at key
    have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
    have h5 : (1 : ℂ) * (u₂ - 1) = 0 := by linear_combination (-16 : ℂ) * key
    rcases mul_eq_zero.1 h5 with h6 | h6
    · exact absurd h6 hC
    · linear_combination h6
  · have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) = ((1 / 4 : ℂ) * (u₃)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) := by
      rw [h]
      simp only [Matrix.transpose_apply, Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
      (try ring)
    rw [e0, e1, e2, e3] at key
    have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
    have h5 : (1 : ℂ) * (u₃ - 1) = 0 := by linear_combination (-16 : ℂ) * key
    rcases mul_eq_zero.1 h5 with h6 | h6
    · exact absurd h6 hC
    · linear_combination h6
#print axioms a40_shared_excl_k4_r_core

theorem a40_shared_excl_e1_c_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 8 × Fin 2 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2) (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2))) → u₂ = 1 ∧ u₃ = 1 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3
  have h0z : z ≠ 0 := a40_shared_ne_zero_of_unit z hz
  have h0w : w ≠ 0 := a40_shared_ne_zero_of_unit w hw
  have h01 : u₁ ≠ 0 := a40_shared_ne_zero_of_unit u₁ h1
  have h02 : u₂ ≠ 0 := a40_shared_ne_zero_of_unit u₂ h2
  have h03 : u₃ ≠ 0 := a40_shared_ne_zero_of_unit u₃ h3
  rintro ⟨X, Y, D, -, -, -, h⟩
  refine ⟨?_, ?_⟩
  · have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (3 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * (u₂)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (3 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (3 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (3 : Fin 4)) := by
      rw [h]
      simp only [Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
      (try ring)
    rw [e0, e1, e2, e3] at key
    have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
    have h5 : (1 : ℂ) * (u₂ - 1) = 0 := by linear_combination (16 : ℂ) * key
    rcases mul_eq_zero.1 h5 with h6 | h6
    · exact absurd h6 hC
    · linear_combination h6
  · have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) = ((1 / 4 : ℂ) * (u₃)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) := by
      rw [h]
      simp only [Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
      (try ring)
    rw [e0, e1, e2, e3] at key
    have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
    have h5 : (1 : ℂ) * (u₃ - 1) = 0 := by linear_combination (-16 : ℂ) * key
    rcases mul_eq_zero.1 h5 with h6 | h6
    · exact absurd h6 hC
    · linear_combination h6
#print axioms a40_shared_excl_e1_c_core

theorem a40_shared_excl_e1_r_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 8 × Fin 2 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2) (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2))ᵀ) → u₁ = 1 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3
  have h0z : z ≠ 0 := a40_shared_ne_zero_of_unit z hz
  have h0w : w ≠ 0 := a40_shared_ne_zero_of_unit w hw
  have h01 : u₁ ≠ 0 := a40_shared_ne_zero_of_unit u₁ h1
  have h02 : u₂ ≠ 0 := a40_shared_ne_zero_of_unit u₂ h2
  have h03 : u₃ ≠ 0 := a40_shared_ne_zero_of_unit u₃ h3
  rintro ⟨X, Y, D, -, -, -, h⟩
  have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * (z)) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * (z * u₁)) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) := by
    rw [h]
    simp only [Matrix.transpose_apply, Matrix.of_apply]
    (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
    (try ring)
  rw [e0, e1, e2, e3] at key
  have hC : (z : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
  have h5 : (z : ℂ) * (u₁ - 1) = 0 := by linear_combination (-16 : ℂ) * key
  rcases mul_eq_zero.1 h5 with h6 | h6
  · exact absurd h6 hC
  · linear_combination h6
#print axioms a40_shared_excl_e1_r_core

theorem a40_shared_excl_e2_c_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 8 × Fin 2 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2) (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2))) → u₃ = 1 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3
  have h0z : z ≠ 0 := a40_shared_ne_zero_of_unit z hz
  have h0w : w ≠ 0 := a40_shared_ne_zero_of_unit w hw
  have h01 : u₁ ≠ 0 := a40_shared_ne_zero_of_unit u₁ h1
  have h02 : u₂ ≠ 0 := a40_shared_ne_zero_of_unit u₂ h2
  have h03 : u₃ ≠ 0 := a40_shared_ne_zero_of_unit u₃ h3
  rintro ⟨X, Y, D, -, -, -, h⟩
  have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * (u₃)) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) := by
    rw [h]
    simp only [Matrix.of_apply]
    (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
    (try ring)
  rw [e0, e1, e2, e3] at key
  have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
  have h5 : (1 : ℂ) * (u₃ - 1) = 0 := by linear_combination (-16 : ℂ) * key
  rcases mul_eq_zero.1 h5 with h6 | h6
  · exact absurd h6 hC
  · linear_combination h6
#print axioms a40_shared_excl_e2_c_core

theorem a40_shared_excl_e2_r_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 8 × Fin 2 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2) (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2))ᵀ) → u₂ = 1 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3
  have h0z : z ≠ 0 := a40_shared_ne_zero_of_unit z hz
  have h0w : w ≠ 0 := a40_shared_ne_zero_of_unit w hw
  have h01 : u₁ ≠ 0 := a40_shared_ne_zero_of_unit u₁ h1
  have h02 : u₂ ≠ 0 := a40_shared_ne_zero_of_unit u₂ h2
  have h03 : u₃ ≠ 0 := a40_shared_ne_zero_of_unit u₃ h3
  rintro ⟨X, Y, D, -, -, -, h⟩
  have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * (u₂)) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) := by
    rw [h]
    simp only [Matrix.transpose_apply, Matrix.of_apply]
    (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
    (try ring)
  rw [e0, e1, e2, e3] at key
  have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
  have h5 : (1 : ℂ) * (u₂ - 1) = 0 := by linear_combination (-16 : ℂ) * key
  rcases mul_eq_zero.1 h5 with h6 | h6
  · exact absurd h6 hC
  · linear_combination h6
#print axioms a40_shared_excl_e2_r_core

theorem a40_shared_excl_t1_c_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2)))) → u₂ = 1 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3
  have h0z : z ≠ 0 := a40_shared_ne_zero_of_unit z hz
  have h0w : w ≠ 0 := a40_shared_ne_zero_of_unit w hw
  have h01 : u₁ ≠ 0 := a40_shared_ne_zero_of_unit u₁ h1
  have h02 : u₂ ≠ 0 := a40_shared_ne_zero_of_unit u₂ h2
  have h03 : u₃ ≠ 0 := a40_shared_ne_zero_of_unit u₃ h3
  rintro ⟨X, Y, D, -, -, -, h⟩
  have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * (u₂)) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) := by
    rw [h]
    simp only [Matrix.of_apply]
    (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
    (try ring)
  rw [e0, e1, e2, e3] at key
  have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
  have h5 : (1 : ℂ) * (u₂ - 1) = 0 := by linear_combination (-16 : ℂ) * key
  rcases mul_eq_zero.1 h5 with h6 | h6
  · exact absurd h6 hC
  · linear_combination h6
#print axioms a40_shared_excl_t1_c_core

theorem a40_shared_excl_t1_r_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2)))ᵀ) → u₃ = 1 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3
  have h0z : z ≠ 0 := a40_shared_ne_zero_of_unit z hz
  have h0w : w ≠ 0 := a40_shared_ne_zero_of_unit w hw
  have h01 : u₁ ≠ 0 := a40_shared_ne_zero_of_unit u₁ h1
  have h02 : u₂ ≠ 0 := a40_shared_ne_zero_of_unit u₂ h2
  have h03 : u₃ ≠ 0 := a40_shared_ne_zero_of_unit u₃ h3
  rintro ⟨X, Y, D, -, -, -, h⟩
  have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * (u₃)) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) := by
    rw [h]
    simp only [Matrix.transpose_apply, Matrix.of_apply]
    (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
    (try ring)
  rw [e0, e1, e2, e3] at key
  have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
  have h5 : (1 : ℂ) * (u₃ - 1) = 0 := by linear_combination (-16 : ℂ) * key
  rcases mul_eq_zero.1 h5 with h6 | h6
  · exact absurd h6 hC
  · linear_combination h6
#print axioms a40_shared_excl_t1_r_core

theorem a40_shared_excl_t2_c_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2))) → u₁ = 1 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3
  have h0z : z ≠ 0 := a40_shared_ne_zero_of_unit z hz
  have h0w : w ≠ 0 := a40_shared_ne_zero_of_unit w hw
  have h01 : u₁ ≠ 0 := a40_shared_ne_zero_of_unit u₁ h1
  have h02 : u₂ ≠ 0 := a40_shared_ne_zero_of_unit u₂ h2
  have h03 : u₃ ≠ 0 := a40_shared_ne_zero_of_unit u₃ h3
  rintro ⟨X, Y, D, -, -, -, h⟩
  have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * (z)) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * (z * u₁)) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) := by
    rw [h]
    simp only [Matrix.of_apply]
    (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
    (try ring)
  rw [e0, e1, e2, e3] at key
  have hC : (z : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
  have h5 : (z : ℂ) * (u₁ - 1) = 0 := by linear_combination (-16 : ℂ) * key
  rcases mul_eq_zero.1 h5 with h6 | h6
  · exact absurd h6 hC
  · linear_combination h6
#print axioms a40_shared_excl_t2_c_core

theorem a40_shared_excl_t2_r_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2))ᵀ) → u₂ = 1 ∧ u₃ = 1 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3
  have h0z : z ≠ 0 := a40_shared_ne_zero_of_unit z hz
  have h0w : w ≠ 0 := a40_shared_ne_zero_of_unit w hw
  have h01 : u₁ ≠ 0 := a40_shared_ne_zero_of_unit u₁ h1
  have h02 : u₂ ≠ 0 := a40_shared_ne_zero_of_unit u₂ h2
  have h03 : u₃ ≠ 0 := a40_shared_ne_zero_of_unit u₃ h3
  rintro ⟨X, Y, D, -, -, -, h⟩
  refine ⟨?_, ?_⟩
  · have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * (u₂)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (3 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (3 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (3 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (3 : Fin 4)) := by
      rw [h]
      simp only [Matrix.transpose_apply, Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
      (try ring)
    rw [e0, e1, e2, e3] at key
    have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
    have h5 : (1 : ℂ) * (u₂ - 1) = 0 := by linear_combination (16 : ℂ) * key
    rcases mul_eq_zero.1 h5 with h6 | h6
    · exact absurd h6 hC
    · linear_combination h6
  · have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) = ((1 / 4 : ℂ) * (u₃)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) := by
      rw [h]
      simp only [Matrix.transpose_apply, Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
      (try ring)
    rw [e0, e1, e2, e3] at key
    have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
    have h5 : (1 : ℂ) * (u₃ - 1) = 0 := by linear_combination (-16 : ℂ) * key
    rcases mul_eq_zero.1 h5 with h6 | h6
    · exact absurd h6 hC
    · linear_combination h6
#print axioms a40_shared_excl_t2_r_core

theorem a40_shared_excl_t3_c_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2) (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2))) → u₁ = 1 ∧ u₂ = 1 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3
  have h0z : z ≠ 0 := a40_shared_ne_zero_of_unit z hz
  have h0w : w ≠ 0 := a40_shared_ne_zero_of_unit w hw
  have h01 : u₁ ≠ 0 := a40_shared_ne_zero_of_unit u₁ h1
  have h02 : u₂ ≠ 0 := a40_shared_ne_zero_of_unit u₂ h2
  have h03 : u₃ ≠ 0 := a40_shared_ne_zero_of_unit u₃ h3
  rintro ⟨X, Y, D, -, -, -, h⟩
  refine ⟨?_, ?_⟩
  · have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * (z * w)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (3 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (3 : Fin 4)) ((1 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * (z * w * u₁)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (3 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (3 : Fin 4)) ((1 : Fin 4), (1 : Fin 4)) := by
      rw [h]
      simp only [Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
      (try ring)
    rw [e0, e1, e2, e3] at key
    have hC : (z * w : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
    have h5 : (z * w : ℂ) * (u₁ - 1) = 0 := by linear_combination (-16 : ℂ) * key
    rcases mul_eq_zero.1 h5 with h6 | h6
    · exact absurd h6 hC
    · linear_combination h6
  · have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (2 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (2 : Fin 4)) ((1 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * (u₂)) := by
      conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
      first
      | ring
      | (simp; ring)
      | norm_num
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (2 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (2 : Fin 4)) ((1 : Fin 4), (1 : Fin 4)) := by
      rw [h]
      simp only [Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
      (try ring)
    rw [e0, e1, e2, e3] at key
    have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
    have h5 : (1 : ℂ) * (u₂ - 1) = 0 := by linear_combination (-16 : ℂ) * key
    rcases mul_eq_zero.1 h5 with h6 | h6
    · exact absurd h6 hC
    · linear_combination h6
#print axioms a40_shared_excl_t3_c_core

theorem a40_shared_excl_t3_r_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2) (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2))ᵀ) → u₂ = 1 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3
  have h0z : z ≠ 0 := a40_shared_ne_zero_of_unit z hz
  have h0w : w ≠ 0 := a40_shared_ne_zero_of_unit w hw
  have h01 : u₁ ≠ 0 := a40_shared_ne_zero_of_unit u₁ h1
  have h02 : u₂ ≠ 0 := a40_shared_ne_zero_of_unit u₂ h2
  have h03 : u₃ ≠ 0 := a40_shared_ne_zero_of_unit u₃ h3
  rintro ⟨X, Y, D, -, -, -, h⟩
  have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * (u₂)) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (3 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (3 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (3 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (3 : Fin 4)) := by
    rw [h]
    simp only [Matrix.transpose_apply, Matrix.of_apply]
    (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
    (try ring)
  rw [e0, e1, e2, e3] at key
  have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
  have h5 : (1 : ℂ) * (u₂ - 1) = 0 := by linear_combination (16 : ℂ) * key
  rcases mul_eq_zero.1 h5 with h6 | h6
  · exact absurd h6 hC
  · linear_combination h6
#print axioms a40_shared_excl_t3_r_core

theorem a40_shared_excl_mc_c_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2))) → u₁ = -1 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3
  have h0z : z ≠ 0 := a40_shared_ne_zero_of_unit z hz
  have h0w : w ≠ 0 := a40_shared_ne_zero_of_unit w hw
  have h01 : u₁ ≠ 0 := a40_shared_ne_zero_of_unit u₁ h1
  have h02 : u₂ ≠ 0 := a40_shared_ne_zero_of_unit u₂ h2
  have h03 : u₃ ≠ 0 := a40_shared_ne_zero_of_unit u₃ h3
  rintro ⟨X, Y, D, -, -, -, h⟩
  have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * (z)) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (3 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (3 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * (-(z * u₁))) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (3 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (3 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) := by
    rw [h]
    simp only [Matrix.of_apply]
    (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
    (try ring)
  rw [e0, e1, e2, e3] at key
  have hC : (z : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
  have h5 : (z : ℂ) * (u₁ - (-1)) = 0 := by linear_combination (16 : ℂ) * key
  rcases mul_eq_zero.1 h5 with h6 | h6
  · exact absurd h6 hC
  · linear_combination h6
#print axioms a40_shared_excl_mc_c_core

theorem a40_shared_excl_mr_r_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2))ᵀ) → u₃ = -1 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3
  have h0z : z ≠ 0 := a40_shared_ne_zero_of_unit z hz
  have h0w : w ≠ 0 := a40_shared_ne_zero_of_unit w hw
  have h01 : u₁ ≠ 0 := a40_shared_ne_zero_of_unit u₁ h1
  have h02 : u₂ ≠ 0 := a40_shared_ne_zero_of_unit u₂ h2
  have h03 : u₃ ≠ 0 := a40_shared_ne_zero_of_unit u₃ h3
  rintro ⟨X, Y, D, -, -, -, h⟩
  have e0 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e1 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e2 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) = ((1 / 4 : ℂ) * 1) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have e3 : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) = ((1 / 4 : ℂ) * (-(u₃))) := by
    conv_lhs => simp (config := { decide := true }) [Matrix.of_apply]
    first
    | ring
    | (simp; ring)
    | norm_num
  have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) := by
    rw [h]
    simp only [Matrix.transpose_apply, Matrix.of_apply]
    (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
    (try ring)
  rw [e0, e1, e2, e3] at key
  have hC : (1 : ℂ) ≠ 0 := by simp [h0z, h0w, h01, h02, h03]
  have h5 : (1 : ℂ) * (u₃ - (-1)) = 0 := by linear_combination (16 : ℂ) * key
  rcases mul_eq_zero.1 h5 with h6 | h6
  · exact absurd h6 hC
  · linear_combination h6
#print axioms a40_shared_excl_mr_r_core

theorem a40_shared_k1 :
    (1 + Complex.I) * star (1 + Complex.I) = 2 := by
  first
  | (apply Complex.ext <;> simp [Complex.star_def] <;> norm_num)
  | (apply Complex.ext <;> simp [Complex.conj_re, Complex.conj_im] <;> norm_num)
  | (simp [Complex.ext_iff, Complex.star_def]; norm_num)
  | (rw [Complex.ext_iff]; simp; norm_num)
#print axioms a40_shared_k1

theorem a40_shared_ones :
    ∀ c : Fin 2, ![(1 : ℂ), 1] c = 1 := by
  intro c
  fin_cases c <;> rfl
#print axioms a40_shared_ones

theorem a40_shared_scal :
    ∀ s m : ℂ, (1 + Complex.I) / 2 * s * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * m) = s * m := by
  intro s m
  have e : (1 + Complex.I) / 2 * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * (1 + Complex.I) = 1 := by
    rw [a40_shared_dval]
    linear_combination (-(Complex.I + 2) / 2) * Complex.I_sq
  calc (1 + Complex.I) / 2 * s * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * m)
      = ((1 + Complex.I) / 2 * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * (1 + Complex.I)) * (s * m) := by ring
    _ = s * m := by rw [e, one_mul]
#print axioms a40_shared_scal

theorem a40_shared_f0 :
    ∀ c : Fin 2, ![![(1 : ℂ), 1], ![1, -1]] 0 c = 1 := by
  intro c
  fin_cases c <;> rfl
#print axioms a40_shared_f0

theorem a40_shared_f1 :
    ∀ c : Fin 2, ![![(1 : ℂ), 1], ![1, -1]] 1 c = ![(1 : ℂ), -1] c := by
  intro c
  fin_cases c <;> rfl
#print axioms a40_shared_f1

theorem a40_shared_k1sq :
    ‖(1 + Complex.I)‖ ^ 2 = 2 := by
  have e : ‖(1 + Complex.I)‖ ^ 2 = Complex.normSq ((1 + Complex.I)) := by
    first
    | exact Complex.sq_norm _
    | exact Complex.sq_abs _
    | simp [Complex.sq_abs]
    | (rw [← Complex.normSq_eq_norm_sq])
  rw [e]
  first
  | (simp [Complex.normSq_apply]; norm_num)
  | (rw [Complex.normSq_apply]; simp; norm_num)
  | norm_num [Complex.normSq_apply]
#print axioms a40_shared_k1sq

theorem a40_shared_gen_t2_split :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ x y : Fin 4 × Fin 4, ∑ k, M x k * star (M y k) = ∑ d : Fin 8, M x ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) * star (M y ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d)) + ∑ d : Fin 8, M x ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) * star (M y ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d)) := by
  intro M x y
  simp only [Fintype.sum_prod_type, Fin.sum_univ_four, Fin.sum_univ_eight]
  first
  | (simp; ring)
  | ring
  | (simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons, Matrix.cons_val']; ring)
#print axioms a40_shared_gen_t2_split

theorem a40_shared_gen_t2_col :
    ∀ j : Fin 4 × Fin 4, (![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2) = j := by
  intro j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> first | rfl | decide | (simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
#print axioms a40_shared_gen_t2_col

theorem a40_shared_gen_t2_sig0 :
    ∀ d : Fin 8, (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) = 1 := by
  intro d
  fin_cases d <;> simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe]
#print axioms a40_shared_gen_t2_sig0

theorem a40_shared_gen_t2_sig1 :
    ∀ d : Fin 8, (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) = -1 := by
  intro d
  fin_cases d <;> simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe]
#print axioms a40_shared_gen_t2_sig1

theorem a40_shared_gen_t2_reps :
    ∀ b b' : Fin 8, ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b = (![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b' ↔ b = b') ∧ (![((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b ≠ (![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b' := by
  intro b b'
  fin_cases b <;> fin_cases b' <;> decide
#print axioms a40_shared_gen_t2_reps

theorem a40_shared_gen_t2_row0 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (0 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((0 : Fin 4), (0 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t2_col j]
  show M ((0 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_t2_row0

theorem a40_shared_gen_t2_row1 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (1 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((0 : Fin 4), (1 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t2_col j]
  show M ((0 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_t2_row1

theorem a40_shared_gen_t2_row2 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((0 : Fin 4), (0 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (2 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((0 : Fin 4), (2 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t2_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * M ((0 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_t2_row2

theorem a40_shared_gen_t2_row3 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((0 : Fin 4), (1 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (3 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((0 : Fin 4), (3 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t2_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * M ((0 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_t2_row3

theorem a40_shared_gen_t2_row4 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (0 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((1 : Fin 4), (0 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t2_col j]
  show M ((1 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_t2_row4

theorem a40_shared_gen_t2_row5 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (1 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((1 : Fin 4), (1 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t2_col j]
  show M ((1 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_t2_row5

theorem a40_shared_gen_t2_row6 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((1 : Fin 4), (0 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (2 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((1 : Fin 4), (2 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t2_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * M ((1 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_t2_row6

theorem a40_shared_gen_t2_row7 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((1 : Fin 4), (1 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (3 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((1 : Fin 4), (3 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t2_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * M ((1 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_t2_row7

theorem a40_shared_gen_t2_row8 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (0 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((2 : Fin 4), (0 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t2_col j]
  show M ((2 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((2 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_t2_row8

theorem a40_shared_gen_t2_row9 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (1 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((2 : Fin 4), (1 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t2_col j]
  show M ((2 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((2 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_t2_row9

theorem a40_shared_gen_t2_row10 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((2 : Fin 4), (0 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (2 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((2 : Fin 4), (2 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t2_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * M ((2 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((2 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_t2_row10

theorem a40_shared_gen_t2_row11 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((2 : Fin 4), (1 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (3 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((2 : Fin 4), (3 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t2_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * M ((2 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((2 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_t2_row11

theorem a40_shared_gen_t2_row12 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (0 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((3 : Fin 4), (0 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t2_col j]
  show M ((3 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((3 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_t2_row12

theorem a40_shared_gen_t2_row13 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (1 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((3 : Fin 4), (1 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t2_col j]
  show M ((3 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((3 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_t2_row13

theorem a40_shared_gen_t2_row14 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((3 : Fin 4), (0 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (2 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((3 : Fin 4), (2 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t2_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * M ((3 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((3 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_t2_row14

theorem a40_shared_gen_t2_row15 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((3 : Fin 4), (1 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (3 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((3 : Fin 4), (3 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t2_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * M ((3 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((3 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_t2_row15

theorem a40_shared_gen_t2 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, M ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ → (∀ i j, ‖M i j‖ = 1 / 4) → (∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((0 : Fin 4), (0 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((0 : Fin 4), (1 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((1 : Fin 4), (0 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((1 : Fin 4), (1 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((2 : Fin 4), (0 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((2 : Fin 4), (1 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((3 : Fin 4), (0 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((3 : Fin 4), (1 : Fin 4)) j) → ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ M = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) := by
  intro M hU hF r0 r1 r2 r3 r4 r5 r6 r7
  have hI : (1 + Complex.I) ≠ 0 := a40_shared_one_add_I
  have hrel : ∀ (b : Fin 8) (j : Fin 4 × Fin 4), M ((![((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) j := by
    intro b j
    fin_cases b
    · exact r0 j
    · exact r1 j
    · exact r2 j
    · exact r3 j
    · exact r4 j
    · exact r5 j
    · exact r6 j
    · exact r7 j
  have hrows : ∀ i j, ∑ k, M i k * star (M j k) = if i = j then (1 : ℂ) else 0 := by
    intro i j
    have h := congrFun (congrFun (Matrix.mem_unitaryGroup_iff.mp hU) i) j
    rw [Matrix.mul_apply, Matrix.one_apply] at h
    simpa only [Matrix.star_apply] using h
  have hblk0 : ∀ b b' : Fin 8, 2 * ∑ d : Fin 8, M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) * star (M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b') ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d)) = if b = b' then (1 : ℂ) else 0 := by
    intro b b'
    have e1 := a40_shared_gen_t2_split M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b')
    have e2 := a40_shared_gen_t2_split M ((![((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b')
    rw [hrows] at e1 e2
    have h0 : ∀ d : Fin 8, M ((![((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) = M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) := fun d => by rw [hrel b, a40_shared_gen_t2_sig0 d, one_mul]
    have h1 : ∀ d : Fin 8, M ((![((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) = -M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) := fun d => by rw [hrel b, a40_shared_gen_t2_sig1 d, neg_one_mul]
    simp only [h0, h1, neg_mul, Finset.sum_neg_distrib] at e2
    have hr := a40_shared_gen_t2_reps b b'
    rw [if_neg hr.2] at e2
    simp only [hr.1] at e1
    first
    | linear_combination -e1 - e2
    | linear_combination e1 + e2
    | linear_combination -e1 + e2
    | linear_combination e1 - e2
  have hblk1 : ∀ b b' : Fin 8, 2 * ∑ d : Fin 8, M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) * star (M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b') ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d)) = if b = b' then (1 : ℂ) else 0 := by
    intro b b'
    have e1 := a40_shared_gen_t2_split M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b')
    have e2 := a40_shared_gen_t2_split M ((![((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b')
    rw [hrows] at e1 e2
    have h0 : ∀ d : Fin 8, M ((![((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) = M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) := fun d => by rw [hrel b, a40_shared_gen_t2_sig0 d, one_mul]
    have h1 : ∀ d : Fin 8, M ((![((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) = -M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) := fun d => by rw [hrel b, a40_shared_gen_t2_sig1 d, neg_one_mul]
    simp only [h0, h1, neg_mul, Finset.sum_neg_distrib] at e2
    have hr := a40_shared_gen_t2_reps b b'
    rw [if_neg hr.2] at e2
    simp only [hr.1] at e1
    first
    | linear_combination -e1 + e2
    | linear_combination e1 - e2
    | linear_combination -e1 - e2
    | linear_combination e1 + e2
  have i0 := a40_shared_gen_t2_row0 M
  have i1 := a40_shared_gen_t2_row1 M
  have i2 := a40_shared_gen_t2_row2 M r0
  have i3 := a40_shared_gen_t2_row3 M r1
  have i4 := a40_shared_gen_t2_row4 M
  have i5 := a40_shared_gen_t2_row5 M
  have i6 := a40_shared_gen_t2_row6 M r2
  have i7 := a40_shared_gen_t2_row7 M r3
  have i8 := a40_shared_gen_t2_row8 M
  have i9 := a40_shared_gen_t2_row9 M
  have i10 := a40_shared_gen_t2_row10 M r4
  have i11 := a40_shared_gen_t2_row11 M r5
  have i12 := a40_shared_gen_t2_row12 M
  have i13 := a40_shared_gen_t2_row13 M
  have i14 := a40_shared_gen_t2_row14 M r6
  have i15 := a40_shared_gen_t2_row15 M r7
  have hblk : ∀ (c : Fin 2) (b b' : Fin 8), 2 * ∑ d : Fin 8, M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d) * star (M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b') ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) = if b = b' then (1 : ℂ) else 0 := by
    intro c
    fin_cases c
    · exact hblk0
    · exact hblk1
  refine ⟨(Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c), (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)), (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))), a40_shared_x_flat, ?_, fun _ _ => a40_shared_dnorm, ?_⟩
  · intro c
    refine ⟨?_, ?_⟩
    · rw [Matrix.mem_unitaryGroup_iff]
      ext b b'
      rw [Matrix.mul_apply, Matrix.one_apply]
      simp only [Matrix.star_apply, Matrix.of_apply]
      calc _ = ((1 + Complex.I) * star (1 + Complex.I)) * ∑ d : Fin 8, M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d) * star (M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b') ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) := by
            rw [Finset.mul_sum]
            exact Finset.sum_congr rfl (fun d _ => by (try simp only [star_mul']); ring)
        _ = _ := by rw [a40_shared_k1]; exact hblk c b b'
    · intro b d
      simp only [Matrix.of_apply]
      rw [norm_mul, mul_pow, a40_shared_k1sq, hF]
      norm_num
  · ext i j
    obtain ⟨a, bb⟩ := i
    fin_cases a <;> fin_cases bb
    · exact i0 j
    · exact i1 j
    · exact i2 j
    · exact i3 j
    · exact i4 j
    · exact i5 j
    · exact i6 j
    · exact i7 j
    · exact i8 j
    · exact i9 j
    · exact i10 j
    · exact i11 j
    · exact i12 j
    · exact i13 j
    · exact i14 j
    · exact i15 j
#print axioms a40_shared_gen_t2

theorem a40_shared_gen_mc_split :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ x y : Fin 4 × Fin 4, ∑ k, M x k * star (M y k) = ∑ d : Fin 8, M x ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) * star (M y ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d)) + ∑ d : Fin 8, M x ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) * star (M y ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d)) := by
  intro M x y
  simp only [Fintype.sum_prod_type, Fin.sum_univ_four, Fin.sum_univ_eight]
  first
  | (simp; ring)
  | ring
  | (simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons, Matrix.cons_val']; ring)
#print axioms a40_shared_gen_mc_split

theorem a40_shared_gen_mc_col :
    ∀ j : Fin 4 × Fin 4, (![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2) = j := by
  intro j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> first | rfl | decide | (simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
#print axioms a40_shared_gen_mc_col

theorem a40_shared_gen_mc_sig0 :
    ∀ d : Fin 8, (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) = 1 := by
  intro d
  fin_cases d <;> simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe]
#print axioms a40_shared_gen_mc_sig0

theorem a40_shared_gen_mc_sig1 :
    ∀ d : Fin 8, (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) = -1 := by
  intro d
  fin_cases d <;> simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe]
#print axioms a40_shared_gen_mc_sig1

theorem a40_shared_gen_mc_reps :
    ∀ b b' : Fin 8, ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b = (![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b' ↔ b = b') ∧ (![((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b ≠ (![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b' := by
  intro b b'
  fin_cases b <;> fin_cases b' <;> decide
#print axioms a40_shared_gen_mc_reps

theorem a40_shared_gen_mc_row0 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (0 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((0 : Fin 4), (0 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mc_col j]
  show M ((0 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_mc_row0

theorem a40_shared_gen_mc_row1 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (1 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((0 : Fin 4), (1 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mc_col j]
  show M ((0 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_mc_row1

theorem a40_shared_gen_mc_row2 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((0 : Fin 4), (0 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (2 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((0 : Fin 4), (2 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mc_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * M ((0 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_mc_row2

theorem a40_shared_gen_mc_row3 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((0 : Fin 4), (1 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (3 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((0 : Fin 4), (3 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mc_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * M ((0 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_mc_row3

theorem a40_shared_gen_mc_row4 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (0 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((1 : Fin 4), (0 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mc_col j]
  show M ((1 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_mc_row4

theorem a40_shared_gen_mc_row5 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (1 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((1 : Fin 4), (1 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mc_col j]
  show M ((1 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_mc_row5

theorem a40_shared_gen_mc_row6 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((1 : Fin 4), (0 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (2 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((1 : Fin 4), (2 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mc_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * M ((1 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_mc_row6

theorem a40_shared_gen_mc_row7 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (3 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((1 : Fin 4), (3 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mc_col j]
  show M ((1 : Fin 4), (3 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (3 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_mc_row7

theorem a40_shared_gen_mc_row8 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (0 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((2 : Fin 4), (0 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mc_col j]
  show M ((2 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((2 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_mc_row8

theorem a40_shared_gen_mc_row9 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (1 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((2 : Fin 4), (1 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mc_col j]
  show M ((2 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((2 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_mc_row9

theorem a40_shared_gen_mc_row10 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((2 : Fin 4), (0 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (2 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((2 : Fin 4), (2 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mc_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * M ((2 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((2 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_mc_row10

theorem a40_shared_gen_mc_row11 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((2 : Fin 4), (1 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (3 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((2 : Fin 4), (3 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mc_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * M ((2 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((2 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_mc_row11

theorem a40_shared_gen_mc_row12 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (0 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((3 : Fin 4), (0 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mc_col j]
  show M ((3 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((3 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_mc_row12

theorem a40_shared_gen_mc_row13 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (1 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((1 : Fin 4), (3 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (1 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((3 : Fin 4), (1 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mc_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * M ((1 : Fin 4), (3 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (3 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_mc_row13

theorem a40_shared_gen_mc_row14 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((3 : Fin 4), (0 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (2 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((3 : Fin 4), (2 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mc_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * M ((3 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((3 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_mc_row14

theorem a40_shared_gen_mc_row15 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((1 : Fin 4), (1 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (3 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) ((3 : Fin 4), (3 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mc_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * M ((1 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_mc_row15

theorem a40_shared_gen_mc :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, M ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ → (∀ i j, ‖M i j‖ = 1 / 4) → (∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((0 : Fin 4), (0 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((0 : Fin 4), (1 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((1 : Fin 4), (0 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((1 : Fin 4), (1 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (1 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((1 : Fin 4), (3 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((2 : Fin 4), (0 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((2 : Fin 4), (1 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((3 : Fin 4), (0 : Fin 4)) j) → ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ M = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) := by
  intro M hU hF r0 r1 r2 r3 r4 r5 r6 r7
  have hI : (1 + Complex.I) ≠ 0 := a40_shared_one_add_I
  have hrel : ∀ (b : Fin 8) (j : Fin 4 × Fin 4), M ((![((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) j := by
    intro b j
    fin_cases b
    · exact r0 j
    · exact r1 j
    · exact r2 j
    · exact r3 j
    · exact r4 j
    · exact r5 j
    · exact r6 j
    · exact r7 j
  have hrows : ∀ i j, ∑ k, M i k * star (M j k) = if i = j then (1 : ℂ) else 0 := by
    intro i j
    have h := congrFun (congrFun (Matrix.mem_unitaryGroup_iff.mp hU) i) j
    rw [Matrix.mul_apply, Matrix.one_apply] at h
    simpa only [Matrix.star_apply] using h
  have hblk0 : ∀ b b' : Fin 8, 2 * ∑ d : Fin 8, M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) * star (M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b') ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d)) = if b = b' then (1 : ℂ) else 0 := by
    intro b b'
    have e1 := a40_shared_gen_mc_split M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b')
    have e2 := a40_shared_gen_mc_split M ((![((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b')
    rw [hrows] at e1 e2
    have h0 : ∀ d : Fin 8, M ((![((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) = M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) := fun d => by rw [hrel b, a40_shared_gen_mc_sig0 d, one_mul]
    have h1 : ∀ d : Fin 8, M ((![((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) = -M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) := fun d => by rw [hrel b, a40_shared_gen_mc_sig1 d, neg_one_mul]
    simp only [h0, h1, neg_mul, Finset.sum_neg_distrib] at e2
    have hr := a40_shared_gen_mc_reps b b'
    rw [if_neg hr.2] at e2
    simp only [hr.1] at e1
    first
    | linear_combination -e1 - e2
    | linear_combination e1 + e2
    | linear_combination -e1 + e2
    | linear_combination e1 - e2
  have hblk1 : ∀ b b' : Fin 8, 2 * ∑ d : Fin 8, M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) * star (M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b') ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d)) = if b = b' then (1 : ℂ) else 0 := by
    intro b b'
    have e1 := a40_shared_gen_mc_split M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b')
    have e2 := a40_shared_gen_mc_split M ((![((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b')
    rw [hrows] at e1 e2
    have h0 : ∀ d : Fin 8, M ((![((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) = M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) := fun d => by rw [hrel b, a40_shared_gen_mc_sig0 d, one_mul]
    have h1 : ∀ d : Fin 8, M ((![((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) = -M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) := fun d => by rw [hrel b, a40_shared_gen_mc_sig1 d, neg_one_mul]
    simp only [h0, h1, neg_mul, Finset.sum_neg_distrib] at e2
    have hr := a40_shared_gen_mc_reps b b'
    rw [if_neg hr.2] at e2
    simp only [hr.1] at e1
    first
    | linear_combination -e1 + e2
    | linear_combination e1 - e2
    | linear_combination -e1 - e2
    | linear_combination e1 + e2
  have i0 := a40_shared_gen_mc_row0 M
  have i1 := a40_shared_gen_mc_row1 M
  have i2 := a40_shared_gen_mc_row2 M r0
  have i3 := a40_shared_gen_mc_row3 M r1
  have i4 := a40_shared_gen_mc_row4 M
  have i5 := a40_shared_gen_mc_row5 M
  have i6 := a40_shared_gen_mc_row6 M r2
  have i7 := a40_shared_gen_mc_row7 M
  have i8 := a40_shared_gen_mc_row8 M
  have i9 := a40_shared_gen_mc_row9 M
  have i10 := a40_shared_gen_mc_row10 M r5
  have i11 := a40_shared_gen_mc_row11 M r6
  have i12 := a40_shared_gen_mc_row12 M
  have i13 := a40_shared_gen_mc_row13 M r4
  have i14 := a40_shared_gen_mc_row14 M r7
  have i15 := a40_shared_gen_mc_row15 M r3
  have hblk : ∀ (c : Fin 2) (b b' : Fin 8), 2 * ∑ d : Fin 8, M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d) * star (M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b') ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) = if b = b' then (1 : ℂ) else 0 := by
    intro c
    fin_cases c
    · exact hblk0
    · exact hblk1
  refine ⟨(Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c), (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)), (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))), a40_shared_x_flat, ?_, fun _ _ => a40_shared_dnorm, ?_⟩
  · intro c
    refine ⟨?_, ?_⟩
    · rw [Matrix.mem_unitaryGroup_iff]
      ext b b'
      rw [Matrix.mul_apply, Matrix.one_apply]
      simp only [Matrix.star_apply, Matrix.of_apply]
      calc _ = ((1 + Complex.I) * star (1 + Complex.I)) * ∑ d : Fin 8, M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d) * star (M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b') ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (2 : Fin 4))], ![((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) := by
            rw [Finset.mul_sum]
            exact Finset.sum_congr rfl (fun d _ => by (try simp only [star_mul']); ring)
        _ = _ := by rw [a40_shared_k1]; exact hblk c b b'
    · intro b d
      simp only [Matrix.of_apply]
      rw [norm_mul, mul_pow, a40_shared_k1sq, hF]
      norm_num
  · ext i j
    obtain ⟨a, bb⟩ := i
    fin_cases a <;> fin_cases bb
    · exact i0 j
    · exact i1 j
    · exact i2 j
    · exact i3 j
    · exact i4 j
    · exact i5 j
    · exact i6 j
    · exact i7 j
    · exact i8 j
    · exact i9 j
    · exact i10 j
    · exact i11 j
    · exact i12 j
    · exact i13 j
    · exact i14 j
    · exact i15 j
#print axioms a40_shared_gen_mc

theorem a40_shared_gen_t1_split :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ x y : Fin 4 × Fin 4, ∑ k, M x k * star (M y k) = ∑ d : Fin 8, M x ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) * star (M y ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d)) + ∑ d : Fin 8, M x ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) * star (M y ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d)) := by
  intro M x y
  simp only [Fintype.sum_prod_type, Fin.sum_univ_four, Fin.sum_univ_eight]
  first
  | (simp; ring)
  | ring
  | (simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons, Matrix.cons_val']; ring)
#print axioms a40_shared_gen_t1_split

theorem a40_shared_gen_t1_col :
    ∀ j : Fin 4 × Fin 4, (![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) (@Fin.modNat 2 2 j.1) (@finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2)) = j := by
  intro j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> first | rfl | decide | (simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
#print axioms a40_shared_gen_t1_col

theorem a40_shared_gen_t1_sig0 :
    ∀ d : Fin 8, (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) = 1 := by
  intro d
  fin_cases d <;> simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe]
#print axioms a40_shared_gen_t1_sig0

theorem a40_shared_gen_t1_sig1 :
    ∀ d : Fin 8, (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) = -1 := by
  intro d
  fin_cases d <;> simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe]
#print axioms a40_shared_gen_t1_sig1

theorem a40_shared_gen_t1_reps :
    ∀ b b' : Fin 8, ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b = (![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b' ↔ b = b') ∧ (![((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b ≠ (![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b' := by
  intro b b'
  fin_cases b <;> fin_cases b' <;> decide
#print axioms a40_shared_gen_t1_reps

theorem a40_shared_gen_t1_row0 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (0 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) ((0 : Fin 4), (0 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t1_col j]
  show M ((0 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (@Fin.modNat 2 2 j.1) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_t1_row0

theorem a40_shared_gen_t1_row1 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (1 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) ((0 : Fin 4), (1 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t1_col j]
  show M ((0 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (@Fin.modNat 2 2 j.1) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_t1_row1

theorem a40_shared_gen_t1_row2 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (2 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) ((0 : Fin 4), (2 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t1_col j]
  show M ((0 : Fin 4), (2 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (@Fin.modNat 2 2 j.1) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (2 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_t1_row2

theorem a40_shared_gen_t1_row3 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (3 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) ((0 : Fin 4), (3 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t1_col j]
  show M ((0 : Fin 4), (3 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (@Fin.modNat 2 2 j.1) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (3 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_t1_row3

theorem a40_shared_gen_t1_row4 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (0 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) ((1 : Fin 4), (0 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t1_col j]
  show M ((1 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (@Fin.modNat 2 2 j.1) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_t1_row4

theorem a40_shared_gen_t1_row5 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (1 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) ((1 : Fin 4), (1 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t1_col j]
  show M ((1 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (@Fin.modNat 2 2 j.1) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_t1_row5

theorem a40_shared_gen_t1_row6 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (2 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) ((1 : Fin 4), (2 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t1_col j]
  show M ((1 : Fin 4), (2 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (@Fin.modNat 2 2 j.1) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (2 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_t1_row6

theorem a40_shared_gen_t1_row7 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (3 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) ((1 : Fin 4), (3 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t1_col j]
  show M ((1 : Fin 4), (3 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (@Fin.modNat 2 2 j.1) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (3 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_t1_row7

theorem a40_shared_gen_t1_row8 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (0 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * M ((0 : Fin 4), (0 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (0 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) ((2 : Fin 4), (0 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t1_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1) * M ((0 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (@Fin.modNat 2 2 j.1) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_t1_row8

theorem a40_shared_gen_t1_row9 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (1 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * M ((0 : Fin 4), (1 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (1 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) ((2 : Fin 4), (1 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t1_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1) * M ((0 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (@Fin.modNat 2 2 j.1) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_t1_row9

theorem a40_shared_gen_t1_row10 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * M ((0 : Fin 4), (2 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (2 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) ((2 : Fin 4), (2 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t1_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1) * M ((0 : Fin 4), (2 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (@Fin.modNat 2 2 j.1) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (2 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_t1_row10

theorem a40_shared_gen_t1_row11 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * M ((0 : Fin 4), (3 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (3 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) ((2 : Fin 4), (3 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t1_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1) * M ((0 : Fin 4), (3 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (@Fin.modNat 2 2 j.1) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (3 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_t1_row11

theorem a40_shared_gen_t1_row12 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (0 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * M ((1 : Fin 4), (0 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (0 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) ((3 : Fin 4), (0 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t1_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1) * M ((1 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (@Fin.modNat 2 2 j.1) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_t1_row12

theorem a40_shared_gen_t1_row13 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (1 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * M ((1 : Fin 4), (1 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (1 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) ((3 : Fin 4), (1 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t1_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1) * M ((1 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (@Fin.modNat 2 2 j.1) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_t1_row13

theorem a40_shared_gen_t1_row14 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * M ((1 : Fin 4), (2 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (2 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) ((3 : Fin 4), (2 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t1_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1) * M ((1 : Fin 4), (2 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (@Fin.modNat 2 2 j.1) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (2 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_t1_row14

theorem a40_shared_gen_t1_row15 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * M ((1 : Fin 4), (3 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (3 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) ((3 : Fin 4), (3 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_t1_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1) * M ((1 : Fin 4), (3 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (@Fin.modNat 2 2 j.1) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (3 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_t1_row15

theorem a40_shared_gen_t1 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, M ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ → (∀ i j, ‖M i j‖ = 1 / 4) → (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (0 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * M ((0 : Fin 4), (0 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (1 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * M ((0 : Fin 4), (1 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * M ((0 : Fin 4), (2 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * M ((0 : Fin 4), (3 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (0 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * M ((1 : Fin 4), (0 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (1 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * M ((1 : Fin 4), (1 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * M ((1 : Fin 4), (2 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * M ((1 : Fin 4), (3 : Fin 4)) j) → ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ M = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) := by
  intro M hU hF r0 r1 r2 r3 r4 r5 r6 r7
  have hI : (1 + Complex.I) ≠ 0 := a40_shared_one_add_I
  have hrel : ∀ (b : Fin 8) (j : Fin 4 × Fin 4), M ((![((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) j := by
    intro b j
    fin_cases b
    · exact r0 j
    · exact r1 j
    · exact r2 j
    · exact r3 j
    · exact r4 j
    · exact r5 j
    · exact r6 j
    · exact r7 j
  have hrows : ∀ i j, ∑ k, M i k * star (M j k) = if i = j then (1 : ℂ) else 0 := by
    intro i j
    have h := congrFun (congrFun (Matrix.mem_unitaryGroup_iff.mp hU) i) j
    rw [Matrix.mul_apply, Matrix.one_apply] at h
    simpa only [Matrix.star_apply] using h
  have hblk0 : ∀ b b' : Fin 8, 2 * ∑ d : Fin 8, M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) * star (M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b') ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d)) = if b = b' then (1 : ℂ) else 0 := by
    intro b b'
    have e1 := a40_shared_gen_t1_split M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b')
    have e2 := a40_shared_gen_t1_split M ((![((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b')
    rw [hrows] at e1 e2
    have h0 : ∀ d : Fin 8, M ((![((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) = M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) := fun d => by rw [hrel b, a40_shared_gen_t1_sig0 d, one_mul]
    have h1 : ∀ d : Fin 8, M ((![((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) = -M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) := fun d => by rw [hrel b, a40_shared_gen_t1_sig1 d, neg_one_mul]
    simp only [h0, h1, neg_mul, Finset.sum_neg_distrib] at e2
    have hr := a40_shared_gen_t1_reps b b'
    rw [if_neg hr.2] at e2
    simp only [hr.1] at e1
    first
    | linear_combination -e1 - e2
    | linear_combination e1 + e2
    | linear_combination -e1 + e2
    | linear_combination e1 - e2
  have hblk1 : ∀ b b' : Fin 8, 2 * ∑ d : Fin 8, M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) * star (M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b') ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d)) = if b = b' then (1 : ℂ) else 0 := by
    intro b b'
    have e1 := a40_shared_gen_t1_split M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b')
    have e2 := a40_shared_gen_t1_split M ((![((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b')
    rw [hrows] at e1 e2
    have h0 : ∀ d : Fin 8, M ((![((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) = M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) := fun d => by rw [hrel b, a40_shared_gen_t1_sig0 d, one_mul]
    have h1 : ∀ d : Fin 8, M ((![((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) = -M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) := fun d => by rw [hrel b, a40_shared_gen_t1_sig1 d, neg_one_mul]
    simp only [h0, h1, neg_mul, Finset.sum_neg_distrib] at e2
    have hr := a40_shared_gen_t1_reps b b'
    rw [if_neg hr.2] at e2
    simp only [hr.1] at e1
    first
    | linear_combination -e1 + e2
    | linear_combination e1 - e2
    | linear_combination -e1 - e2
    | linear_combination e1 + e2
  have i0 := a40_shared_gen_t1_row0 M
  have i1 := a40_shared_gen_t1_row1 M
  have i2 := a40_shared_gen_t1_row2 M
  have i3 := a40_shared_gen_t1_row3 M
  have i4 := a40_shared_gen_t1_row4 M
  have i5 := a40_shared_gen_t1_row5 M
  have i6 := a40_shared_gen_t1_row6 M
  have i7 := a40_shared_gen_t1_row7 M
  have i8 := a40_shared_gen_t1_row8 M r0
  have i9 := a40_shared_gen_t1_row9 M r1
  have i10 := a40_shared_gen_t1_row10 M r2
  have i11 := a40_shared_gen_t1_row11 M r3
  have i12 := a40_shared_gen_t1_row12 M r4
  have i13 := a40_shared_gen_t1_row13 M r5
  have i14 := a40_shared_gen_t1_row14 M r6
  have i15 := a40_shared_gen_t1_row15 M r7
  have hblk : ∀ (c : Fin 2) (b b' : Fin 8), 2 * ∑ d : Fin 8, M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d) * star (M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b') ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) = if b = b' then (1 : ℂ) else 0 := by
    intro c
    fin_cases c
    · exact hblk0
    · exact hblk1
  refine ⟨(Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c), (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)), (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))), a40_shared_x_flat, ?_, fun _ _ => a40_shared_dnorm, ?_⟩
  · intro c
    refine ⟨?_, ?_⟩
    · rw [Matrix.mem_unitaryGroup_iff]
      ext b b'
      rw [Matrix.mul_apply, Matrix.one_apply]
      simp only [Matrix.star_apply, Matrix.of_apply]
      calc _ = ((1 + Complex.I) * star (1 + Complex.I)) * ∑ d : Fin 8, M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d) * star (M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b') ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) := by
            rw [Finset.mul_sum]
            exact Finset.sum_congr rfl (fun d _ => by (try simp only [star_mul']); ring)
        _ = _ := by rw [a40_shared_k1]; exact hblk c b b'
    · intro b d
      simp only [Matrix.of_apply]
      rw [norm_mul, mul_pow, a40_shared_k1sq, hF]
      norm_num
  · ext i j
    obtain ⟨a, bb⟩ := i
    fin_cases a <;> fin_cases bb
    · exact i0 j
    · exact i1 j
    · exact i2 j
    · exact i3 j
    · exact i4 j
    · exact i5 j
    · exact i6 j
    · exact i7 j
    · exact i8 j
    · exact i9 j
    · exact i10 j
    · exact i11 j
    · exact i12 j
    · exact i13 j
    · exact i14 j
    · exact i15 j
#print axioms a40_shared_gen_t1

theorem a40_shared_gen_mr_split :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ x y : Fin 4 × Fin 4, ∑ k, M x k * star (M y k) = ∑ d : Fin 8, M x ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) * star (M y ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d)) + ∑ d : Fin 8, M x ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) * star (M y ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d)) := by
  intro M x y
  simp only [Fintype.sum_prod_type, Fin.sum_univ_four, Fin.sum_univ_eight]
  first
  | (simp; ring)
  | ring
  | (simp only [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons, Matrix.cons_val']; ring)
#print axioms a40_shared_gen_mr_split

theorem a40_shared_gen_mr_col :
    ∀ j : Fin 4 × Fin 4, (![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2) = j := by
  intro j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> first | rfl | decide | (simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe])
#print axioms a40_shared_gen_mr_col

theorem a40_shared_gen_mr_sig0 :
    ∀ d : Fin 8, (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) = 1 := by
  intro d
  fin_cases d <;> simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe]
#print axioms a40_shared_gen_mr_sig0

theorem a40_shared_gen_mr_sig1 :
    ∀ d : Fin 8, (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) = -1 := by
  intro d
  fin_cases d <;> simp (config := { decide := true }) [a36_shared_div, a36_shared_mod, a40_shared_fpe]
#print axioms a40_shared_gen_mr_sig1

theorem a40_shared_gen_mr_reps :
    ∀ b b' : Fin 8, ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b = (![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b' ↔ b = b') ∧ (![((0 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (2 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b ≠ (![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b' := by
  intro b b'
  fin_cases b <;> fin_cases b' <;> decide
#print axioms a40_shared_gen_mr_reps

theorem a40_shared_gen_mr_row0 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (0 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)) ((0 : Fin 4), (0 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mr_col j]
  show M ((0 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_mr_row0

theorem a40_shared_gen_mr_row1 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (1 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)) ((0 : Fin 4), (1 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mr_col j]
  show M ((0 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_mr_row1

theorem a40_shared_gen_mr_row2 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * M ((0 : Fin 4), (0 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (2 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)) ((0 : Fin 4), (2 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mr_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * M ((0 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_mr_row2

theorem a40_shared_gen_mr_row3 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (3 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)) ((0 : Fin 4), (3 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mr_col j]
  show M ((0 : Fin 4), (3 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (3 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_mr_row3

theorem a40_shared_gen_mr_row4 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (0 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)) ((1 : Fin 4), (0 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mr_col j]
  show M ((1 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_mr_row4

theorem a40_shared_gen_mr_row5 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (1 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)) ((1 : Fin 4), (1 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mr_col j]
  show M ((1 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_mr_row5

theorem a40_shared_gen_mr_row6 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (2 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)) ((1 : Fin 4), (2 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mr_col j]
  show M ((1 : Fin 4), (2 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (2 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_mr_row6

theorem a40_shared_gen_mr_row7 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((1 : Fin 4), (3 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)) ((1 : Fin 4), (3 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mr_col j]
  show M ((1 : Fin 4), (3 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (3 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_mr_row7

theorem a40_shared_gen_mr_row8 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, ∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (0 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)) ((2 : Fin 4), (0 : Fin 4)) j := by
  intro M j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mr_col j]
  show M ((2 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 0 (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((2 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f0, one_mul]
#print axioms a40_shared_gen_mr_row8

theorem a40_shared_gen_mr_row9 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (1 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * M ((0 : Fin 4), (1 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (1 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)) ((2 : Fin 4), (1 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mr_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * M ((0 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_mr_row9

theorem a40_shared_gen_mr_row10 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * M ((2 : Fin 4), (0 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (2 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)) ((2 : Fin 4), (2 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mr_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * M ((2 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((2 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_mr_row10

theorem a40_shared_gen_mr_row11 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * M ((0 : Fin 4), (3 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (3 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)) ((2 : Fin 4), (3 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mr_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * M ((0 : Fin 4), (3 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((0 : Fin 4), (3 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_mr_row11

theorem a40_shared_gen_mr_row12 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (0 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * M ((1 : Fin 4), (0 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (0 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)) ((3 : Fin 4), (0 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mr_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * M ((1 : Fin 4), (0 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (0 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_mr_row12

theorem a40_shared_gen_mr_row13 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (1 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * M ((1 : Fin 4), (1 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (1 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)) ((3 : Fin 4), (1 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mr_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * M ((1 : Fin 4), (1 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (1 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_mr_row13

theorem a40_shared_gen_mr_row14 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * M ((1 : Fin 4), (2 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (2 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)) ((3 : Fin 4), (2 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mr_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * M ((1 : Fin 4), (2 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (2 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_mr_row14

theorem a40_shared_gen_mr_row15 :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * M ((1 : Fin 4), (3 : Fin 4)) j) → ∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (3 : Fin 4)) j = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => (Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c) i.1 j.1 * (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) j.1 i.2 * (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) j.1 i.2 j.2) (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)) ((3 : Fin 4), (3 : Fin 4)) j := by
  intro M r j
  simp only [Matrix.of_apply]
  rw [a40_shared_gen_mr_col j]
  rw [r j]
  show ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * M ((1 : Fin 4), (3 : Fin 4)) j = (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] 1 (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2) * ((2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))) * ((1 + Complex.I) * M ((1 : Fin 4), (3 : Fin 4)) j)
  rw [a40_shared_scal, a40_shared_f1]
#print axioms a40_shared_gen_mr_row15

theorem a40_shared_gen_mr :
    ∀ M : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, M ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ → (∀ i j, ‖M i j‖ = 1 / 4) → (∀ j : Fin 4 × Fin 4, M ((0 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * M ((0 : Fin 4), (0 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (1 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * M ((0 : Fin 4), (1 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * M ((0 : Fin 4), (3 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (0 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * M ((1 : Fin 4), (0 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (1 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * M ((1 : Fin 4), (1 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * M ((1 : Fin 4), (2 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((3 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * M ((1 : Fin 4), (3 : Fin 4)) j) → (∀ j : Fin 4 × Fin 4, M ((2 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * M ((2 : Fin 4), (0 : Fin 4)) j) → ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ M = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)) := by
  intro M hU hF r0 r1 r2 r3 r4 r5 r6 r7
  have hI : (1 + Complex.I) ≠ 0 := a40_shared_one_add_I
  have hrel : ∀ (b : Fin 8) (j : Fin 4 × Fin 4), M ((![((0 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (2 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) j := by
    intro b j
    fin_cases b
    · exact r0 j
    · exact r1 j
    · exact r2 j
    · exact r3 j
    · exact r4 j
    · exact r5 j
    · exact r6 j
    · exact r7 j
  have hrows : ∀ i j, ∑ k, M i k * star (M j k) = if i = j then (1 : ℂ) else 0 := by
    intro i j
    have h := congrFun (congrFun (Matrix.mem_unitaryGroup_iff.mp hU) i) j
    rw [Matrix.mul_apply, Matrix.one_apply] at h
    simpa only [Matrix.star_apply] using h
  have hblk0 : ∀ b b' : Fin 8, 2 * ∑ d : Fin 8, M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) * star (M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b') ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d)) = if b = b' then (1 : ℂ) else 0 := by
    intro b b'
    have e1 := a40_shared_gen_mr_split M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b')
    have e2 := a40_shared_gen_mr_split M ((![((0 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (2 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b')
    rw [hrows] at e1 e2
    have h0 : ∀ d : Fin 8, M ((![((0 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (2 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) = M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) := fun d => by rw [hrel b, a40_shared_gen_mr_sig0 d, one_mul]
    have h1 : ∀ d : Fin 8, M ((![((0 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (2 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) = -M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) := fun d => by rw [hrel b, a40_shared_gen_mr_sig1 d, neg_one_mul]
    simp only [h0, h1, neg_mul, Finset.sum_neg_distrib] at e2
    have hr := a40_shared_gen_mr_reps b b'
    rw [if_neg hr.2] at e2
    simp only [hr.1] at e1
    first
    | linear_combination -e1 - e2
    | linear_combination e1 + e2
    | linear_combination -e1 + e2
    | linear_combination e1 - e2
  have hblk1 : ∀ b b' : Fin 8, 2 * ∑ d : Fin 8, M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) * star (M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b') ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d)) = if b = b' then (1 : ℂ) else 0 := by
    intro b b'
    have e1 := a40_shared_gen_mr_split M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b')
    have e2 := a40_shared_gen_mr_split M ((![((0 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (2 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b')
    rw [hrows] at e1 e2
    have h0 : ∀ d : Fin 8, M ((![((0 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (2 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) = M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 0 d) := fun d => by rw [hrel b, a40_shared_gen_mr_sig0 d, one_mul]
    have h1 : ∀ d : Fin 8, M ((![((0 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (2 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) = -M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) 1 d) := fun d => by rw [hrel b, a40_shared_gen_mr_sig1 d, neg_one_mul]
    simp only [h0, h1, neg_mul, Finset.sum_neg_distrib] at e2
    have hr := a40_shared_gen_mr_reps b b'
    rw [if_neg hr.2] at e2
    simp only [hr.1] at e1
    first
    | linear_combination -e1 + e2
    | linear_combination e1 - e2
    | linear_combination -e1 - e2
    | linear_combination e1 + e2
  have i0 := a40_shared_gen_mr_row0 M
  have i1 := a40_shared_gen_mr_row1 M
  have i2 := a40_shared_gen_mr_row2 M r0
  have i3 := a40_shared_gen_mr_row3 M
  have i4 := a40_shared_gen_mr_row4 M
  have i5 := a40_shared_gen_mr_row5 M
  have i6 := a40_shared_gen_mr_row6 M
  have i7 := a40_shared_gen_mr_row7 M
  have i8 := a40_shared_gen_mr_row8 M
  have i9 := a40_shared_gen_mr_row9 M r1
  have i10 := a40_shared_gen_mr_row10 M r7
  have i11 := a40_shared_gen_mr_row11 M r2
  have i12 := a40_shared_gen_mr_row12 M r3
  have i13 := a40_shared_gen_mr_row13 M r4
  have i14 := a40_shared_gen_mr_row14 M r5
  have i15 := a40_shared_gen_mr_row15 M r6
  have hblk : ∀ (c : Fin 2) (b b' : Fin 8), 2 * ∑ d : Fin 8, M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d) * star (M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b') ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) = if b = b' then (1 : ℂ) else 0 := by
    intro c
    fin_cases c
    · exact hblk0
    · exact hblk1
  refine ⟨(Matrix.of fun a c : Fin 2 => (1 + Complex.I) / 2 * ![![(1 : ℂ), 1], ![1, -1]] a c), (fun c : Fin 2 => Matrix.of fun b d : Fin 8 => (1 + Complex.I) * M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)), (fun (_ : Fin 2) (_ : Fin 8) => (2 : ℂ) / ((1 + Complex.I) * (1 + Complex.I))), a40_shared_x_flat, ?_, fun _ _ => a40_shared_dnorm, ?_⟩
  · intro c
    refine ⟨?_, ?_⟩
    · rw [Matrix.mem_unitaryGroup_iff]
      ext b b'
      rw [Matrix.mul_apply, Matrix.one_apply]
      simp only [Matrix.star_apply, Matrix.of_apply]
      calc _ = ((1 + Complex.I) * star (1 + Complex.I)) * ∑ d : Fin 8, M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b) ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d) * star (M ((![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4))] : Fin 8 → Fin 4 × Fin 4) b') ((![![((0 : Fin 4), (0 : Fin 4)), ((0 : Fin 4), (1 : Fin 4)), ((0 : Fin 4), (2 : Fin 4)), ((0 : Fin 4), (3 : Fin 4)), ((2 : Fin 4), (0 : Fin 4)), ((2 : Fin 4), (1 : Fin 4)), ((2 : Fin 4), (2 : Fin 4)), ((2 : Fin 4), (3 : Fin 4))], ![((1 : Fin 4), (0 : Fin 4)), ((1 : Fin 4), (1 : Fin 4)), ((1 : Fin 4), (2 : Fin 4)), ((1 : Fin 4), (3 : Fin 4)), ((3 : Fin 4), (0 : Fin 4)), ((3 : Fin 4), (1 : Fin 4)), ((3 : Fin 4), (2 : Fin 4)), ((3 : Fin 4), (3 : Fin 4))]] : Fin 2 → Fin 8 → Fin 4 × Fin 4) c d)) := by
            rw [Finset.mul_sum]
            exact Finset.sum_congr rfl (fun d _ => by (try simp only [star_mul']); ring)
        _ = _ := by rw [a40_shared_k1]; exact hblk c b b'
    · intro b d
      simp only [Matrix.of_apply]
      rw [norm_mul, mul_pow, a40_shared_k1sq, hF]
      norm_num
  · ext i j
    obtain ⟨a, bb⟩ := i
    fin_cases a <;> fin_cases bb
    · exact i0 j
    · exact i1 j
    · exact i2 j
    · exact i3 j
    · exact i4 j
    · exact i5 j
    · exact i6 j
    · exact i7 j
    · exact i8 j
    · exact i9 j
    · exact i10 j
    · exact i11 j
    · exact i12 j
    · exact i13 j
    · exact i14 j
    · exact i15 j
#print axioms a40_shared_gen_mr

theorem a40_shared_face_1p_rel0 :
    ∀ z w u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * 1 ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * 1 ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) j := by
  intro z w u₂ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_1p_rel0

theorem a40_shared_face_1p_rel1 :
    ∀ z w u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * 1 ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * 1 ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) j := by
  intro z w u₂ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_1p_rel1

theorem a40_shared_face_1p_rel2 :
    ∀ z w u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * 1 ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * 1 ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) j := by
  intro z w u₂ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_1p_rel2

theorem a40_shared_face_1p_rel3 :
    ∀ z w u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * 1 ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * 1 ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) j := by
  intro z w u₂ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_1p_rel3

theorem a40_shared_face_1p_rel4 :
    ∀ z w u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * 1 ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * 1 ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) j := by
  intro z w u₂ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_1p_rel4

theorem a40_shared_face_1p_rel5 :
    ∀ z w u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * 1 ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * 1 ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (1 : Fin 4)) j := by
  intro z w u₂ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_1p_rel5

theorem a40_shared_face_1p_rel6 :
    ∀ z w u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * 1 ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * 1 ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (0 : Fin 4)) j := by
  intro z w u₂ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_1p_rel6

theorem a40_shared_face_1p_rel7 :
    ∀ z w u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * 1 ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * 1 ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (1 : Fin 4)) j := by
  intro z w u₂ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_1p_rel7

theorem a40_shared_face_1p_core :
    ∀ z w u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * 1 ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) := by
  intro z w u₂ u₃ hz hw ha hb
  exact a40_shared_gen_t2 _ (a39_shared_unitary_core z w 1 u₂ u₃ hz hw (by norm_num) ha hb) (a39_shared_flat_core z w 1 u₂ u₃ hz hw (by norm_num) ha hb) (a40_shared_face_1p_rel0 z w u₂ u₃ hz hw ha hb) (a40_shared_face_1p_rel1 z w u₂ u₃ hz hw ha hb) (a40_shared_face_1p_rel2 z w u₂ u₃ hz hw ha hb) (a40_shared_face_1p_rel3 z w u₂ u₃ hz hw ha hb) (a40_shared_face_1p_rel4 z w u₂ u₃ hz hw ha hb) (a40_shared_face_1p_rel5 z w u₂ u₃ hz hw ha hb) (a40_shared_face_1p_rel6 z w u₂ u₃ hz hw ha hb) (a40_shared_face_1p_rel7 z w u₂ u₃ hz hw ha hb)
#print axioms a40_shared_face_1p_core

theorem a40_shared_face_1m_rel0 :
    ∀ z w u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * (-1) ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * (-1) ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) j := by
  intro z w u₂ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_1m_rel0

theorem a40_shared_face_1m_rel1 :
    ∀ z w u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * (-1) ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * (-1) ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) j := by
  intro z w u₂ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_1m_rel1

theorem a40_shared_face_1m_rel2 :
    ∀ z w u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * (-1) ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * (-1) ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) j := by
  intro z w u₂ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_1m_rel2

theorem a40_shared_face_1m_rel3 :
    ∀ z w u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * (-1) ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * (-1) ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) j := by
  intro z w u₂ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_1m_rel3

theorem a40_shared_face_1m_rel4 :
    ∀ z w u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * (-1) ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (1 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * (-1) ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) j := by
  intro z w u₂ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_1m_rel4

theorem a40_shared_face_1m_rel5 :
    ∀ z w u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * (-1) ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * (-1) ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) j := by
  intro z w u₂ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_1m_rel5

theorem a40_shared_face_1m_rel6 :
    ∀ z w u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * (-1) ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * (-1) ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (1 : Fin 4)) j := by
  intro z w u₂ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_1m_rel6

theorem a40_shared_face_1m_rel7 :
    ∀ z w u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * (-1) ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * (-1) ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (0 : Fin 4)) j := by
  intro z w u₂ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_1m_rel7

theorem a40_shared_face_1m_core :
    ∀ z w u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * (-1) ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)) := by
  intro z w u₂ u₃ hz hw ha hb
  exact a40_shared_gen_mc _ (a39_shared_unitary_core z w (-1) u₂ u₃ hz hw (by norm_num) ha hb) (a39_shared_flat_core z w (-1) u₂ u₃ hz hw (by norm_num) ha hb) (a40_shared_face_1m_rel0 z w u₂ u₃ hz hw ha hb) (a40_shared_face_1m_rel1 z w u₂ u₃ hz hw ha hb) (a40_shared_face_1m_rel2 z w u₂ u₃ hz hw ha hb) (a40_shared_face_1m_rel3 z w u₂ u₃ hz hw ha hb) (a40_shared_face_1m_rel4 z w u₂ u₃ hz hw ha hb) (a40_shared_face_1m_rel5 z w u₂ u₃ hz hw ha hb) (a40_shared_face_1m_rel6 z w u₂ u₃ hz hw ha hb) (a40_shared_face_1m_rel7 z w u₂ u₃ hz hw ha hb)
#print axioms a40_shared_face_1m_core

theorem a40_shared_face_2p_rel0 :
    ∀ z w u₁ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * 1 ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * 1 ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) j := by
  intro z w u₁ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_2p_rel0

theorem a40_shared_face_2p_rel1 :
    ∀ z w u₁ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * 1 ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (1 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * 1 ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) j := by
  intro z w u₁ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_2p_rel1

theorem a40_shared_face_2p_rel2 :
    ∀ z w u₁ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * 1 ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * 1 ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (2 : Fin 4)) j := by
  intro z w u₁ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_2p_rel2

theorem a40_shared_face_2p_rel3 :
    ∀ z w u₁ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * 1 ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * 1 ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (3 : Fin 4)) j := by
  intro z w u₁ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_2p_rel3

theorem a40_shared_face_2p_rel4 :
    ∀ z w u₁ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * 1 ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (0 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * 1 ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) j := by
  intro z w u₁ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_2p_rel4

theorem a40_shared_face_2p_rel5 :
    ∀ z w u₁ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * 1 ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (1 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * 1 ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) j := by
  intro z w u₁ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_2p_rel5

theorem a40_shared_face_2p_rel6 :
    ∀ z w u₁ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * 1 ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * 1 ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (2 : Fin 4)) j := by
  intro z w u₁ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_2p_rel6

theorem a40_shared_face_2p_rel7 :
    ∀ z w u₁ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * 1 ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * 1 ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) j := by
  intro z w u₁ u₃ hz hw ha hb j
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_2p_rel7

theorem a40_shared_face_2p_core :
    ∀ z w u₁ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₃ * u₃ = 1 → ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * 1 ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))) := by
  intro z w u₁ u₃ hz hw ha hb
  exact a40_shared_gen_t1 _ (a39_shared_unitary_core z w u₁ 1 u₃ hz hw ha (by norm_num) hb) (a39_shared_flat_core z w u₁ 1 u₃ hz hw ha (by norm_num) hb) (a40_shared_face_2p_rel0 z w u₁ u₃ hz hw ha hb) (a40_shared_face_2p_rel1 z w u₁ u₃ hz hw ha hb) (a40_shared_face_2p_rel2 z w u₁ u₃ hz hw ha hb) (a40_shared_face_2p_rel3 z w u₁ u₃ hz hw ha hb) (a40_shared_face_2p_rel4 z w u₁ u₃ hz hw ha hb) (a40_shared_face_2p_rel5 z w u₁ u₃ hz hw ha hb) (a40_shared_face_2p_rel6 z w u₁ u₃ hz hw ha hb) (a40_shared_face_2p_rel7 z w u₁ u₃ hz hw ha hb)
#print axioms a40_shared_face_2p_core

theorem a40_shared_face_3p_rel0 :
    ∀ z w u₁ u₂ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * 1 ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((2 : Fin 4), (0 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * 1 ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((0 : Fin 4), (0 : Fin 4)) j := by
  intro z w u₁ u₂ hz hw ha hb j
  simp only [Matrix.transpose_apply]
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_3p_rel0

theorem a40_shared_face_3p_rel1 :
    ∀ z w u₁ u₂ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * 1 ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((2 : Fin 4), (1 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * 1 ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((0 : Fin 4), (1 : Fin 4)) j := by
  intro z w u₁ u₂ hz hw ha hb j
  simp only [Matrix.transpose_apply]
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_3p_rel1

theorem a40_shared_face_3p_rel2 :
    ∀ z w u₁ u₂ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * 1 ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((2 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * 1 ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((0 : Fin 4), (2 : Fin 4)) j := by
  intro z w u₁ u₂ hz hw ha hb j
  simp only [Matrix.transpose_apply]
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_3p_rel2

theorem a40_shared_face_3p_rel3 :
    ∀ z w u₁ u₂ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * 1 ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((2 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * 1 ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((0 : Fin 4), (3 : Fin 4)) j := by
  intro z w u₁ u₂ hz hw ha hb j
  simp only [Matrix.transpose_apply]
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_3p_rel3

theorem a40_shared_face_3p_rel4 :
    ∀ z w u₁ u₂ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * 1 ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((3 : Fin 4), (0 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * 1 ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((1 : Fin 4), (0 : Fin 4)) j := by
  intro z w u₁ u₂ hz hw ha hb j
  simp only [Matrix.transpose_apply]
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_3p_rel4

theorem a40_shared_face_3p_rel5 :
    ∀ z w u₁ u₂ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * 1 ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((3 : Fin 4), (1 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * 1 ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((1 : Fin 4), (1 : Fin 4)) j := by
  intro z w u₁ u₂ hz hw ha hb j
  simp only [Matrix.transpose_apply]
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_3p_rel5

theorem a40_shared_face_3p_rel6 :
    ∀ z w u₁ u₂ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * 1 ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((3 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * 1 ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((1 : Fin 4), (2 : Fin 4)) j := by
  intro z w u₁ u₂ hz hw ha hb j
  simp only [Matrix.transpose_apply]
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_3p_rel6

theorem a40_shared_face_3p_rel7 :
    ∀ z w u₁ u₂ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * 1 ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((3 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (@Fin.modNat 2 2 j.1)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * 1 ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((1 : Fin 4), (3 : Fin 4)) j := by
  intro z w u₁ u₂ hz hw ha hb j
  simp only [Matrix.transpose_apply]
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_3p_rel7

theorem a40_shared_face_3p_core :
    ∀ z w u₁ u₂ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * 1 ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2)))ᵀ := by
  intro z w u₁ u₂ hz hw ha hb
  obtain ⟨X, Y, D, h1, h2, h3, h4⟩ := a40_shared_gen_t1 _ (transpose_unitary (a39_shared_unitary_core z w u₁ u₂ 1 hz hw ha hb (by norm_num))) (fun i j => by rw [Matrix.transpose_apply]; exact a39_shared_flat_core z w u₁ u₂ 1 hz hw ha hb (by norm_num) j i) (a40_shared_face_3p_rel0 z w u₁ u₂ hz hw ha hb) (a40_shared_face_3p_rel1 z w u₁ u₂ hz hw ha hb) (a40_shared_face_3p_rel2 z w u₁ u₂ hz hw ha hb) (a40_shared_face_3p_rel3 z w u₁ u₂ hz hw ha hb) (a40_shared_face_3p_rel4 z w u₁ u₂ hz hw ha hb) (a40_shared_face_3p_rel5 z w u₁ u₂ hz hw ha hb) (a40_shared_face_3p_rel6 z w u₁ u₂ hz hw ha hb) (a40_shared_face_3p_rel7 z w u₁ u₂ hz hw ha hb)
  exact ⟨X, Y, D, h1, h2, h3, by rw [← h4, Matrix.transpose_transpose]⟩
#print axioms a40_shared_face_3p_core

theorem a40_shared_face_3m_rel0 :
    ∀ z w u₁ u₂ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * (-1) ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((0 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * (-1) ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((0 : Fin 4), (0 : Fin 4)) j := by
  intro z w u₁ u₂ hz hw ha hb j
  simp only [Matrix.transpose_apply]
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_3m_rel0

theorem a40_shared_face_3m_rel1 :
    ∀ z w u₁ u₂ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * (-1) ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((2 : Fin 4), (1 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * (-1) ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((0 : Fin 4), (1 : Fin 4)) j := by
  intro z w u₁ u₂ hz hw ha hb j
  simp only [Matrix.transpose_apply]
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_3m_rel1

theorem a40_shared_face_3m_rel2 :
    ∀ z w u₁ u₂ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * (-1) ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((2 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * (-1) ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((0 : Fin 4), (3 : Fin 4)) j := by
  intro z w u₁ u₂ hz hw ha hb j
  simp only [Matrix.transpose_apply]
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_3m_rel2

theorem a40_shared_face_3m_rel3 :
    ∀ z w u₁ u₂ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * (-1) ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((3 : Fin 4), (0 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * (-1) ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((1 : Fin 4), (0 : Fin 4)) j := by
  intro z w u₁ u₂ hz hw ha hb j
  simp only [Matrix.transpose_apply]
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_3m_rel3

theorem a40_shared_face_3m_rel4 :
    ∀ z w u₁ u₂ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * (-1) ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((3 : Fin 4), (1 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * (-1) ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((1 : Fin 4), (1 : Fin 4)) j := by
  intro z w u₁ u₂ hz hw ha hb j
  simp only [Matrix.transpose_apply]
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_3m_rel4

theorem a40_shared_face_3m_rel5 :
    ∀ z w u₁ u₂ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * (-1) ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((3 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * (-1) ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((1 : Fin 4), (2 : Fin 4)) j := by
  intro z w u₁ u₂ hz hw ha hb j
  simp only [Matrix.transpose_apply]
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_3m_rel5

theorem a40_shared_face_3m_rel6 :
    ∀ z w u₁ u₂ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * (-1) ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((3 : Fin 4), (3 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * (-1) ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((1 : Fin 4), (3 : Fin 4)) j := by
  intro z w u₁ u₂ hz hw ha hb j
  simp only [Matrix.transpose_apply]
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_3m_rel6

theorem a40_shared_face_3m_rel7 :
    ∀ z w u₁ u₂ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → ∀ j : Fin 4 × Fin 4, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * (-1) ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((2 : Fin 4), (2 : Fin 4)) j = (fun j : Fin 4 × Fin 4 => ![(1 : ℂ), -1] (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2)) j * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * (-1) ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))ᵀ ((2 : Fin 4), (0 : Fin 4)) j := by
  intro z w u₁ u₂ hz hw ha hb j
  simp only [Matrix.transpose_apply]
  obtain ⟨c, d⟩ := j
  fin_cases c <;> fin_cases d <;> simp (config := { decide := true }) [Matrix.of_apply, a36_shared_div, a36_shared_mod, a40_shared_fpe] <;> first | done | ring | tauto | (field_simp; ring)
#print axioms a40_shared_face_3m_rel7

theorem a40_shared_face_3m_core :
    ∀ z w u₁ u₂ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * (-1) ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2))ᵀ := by
  intro z w u₁ u₂ hz hw ha hb
  obtain ⟨X, Y, D, h1, h2, h3, h4⟩ := a40_shared_gen_mr _ (transpose_unitary (a39_shared_unitary_core z w u₁ u₂ (-1) hz hw ha hb (by norm_num))) (fun i j => by rw [Matrix.transpose_apply]; exact a39_shared_flat_core z w u₁ u₂ (-1) hz hw ha hb (by norm_num) j i) (a40_shared_face_3m_rel0 z w u₁ u₂ hz hw ha hb) (a40_shared_face_3m_rel1 z w u₁ u₂ hz hw ha hb) (a40_shared_face_3m_rel2 z w u₁ u₂ hz hw ha hb) (a40_shared_face_3m_rel3 z w u₁ u₂ hz hw ha hb) (a40_shared_face_3m_rel4 z w u₁ u₂ hz hw ha hb) (a40_shared_face_3m_rel5 z w u₁ u₂ hz hw ha hb) (a40_shared_face_3m_rel6 z w u₁ u₂ hz hw ha hb) (a40_shared_face_3m_rel7 z w u₁ u₂ hz hw ha hb)
  exact ⟨X, Y, D, h1, h2, h3, by rw [← h4, Matrix.transpose_transpose]⟩
#print axioms a40_shared_face_3m_core

theorem a40_shared_face_1p :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₂ u₃ : ℂ, star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 1 u₂ u₃ = ditat2 X Y D := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₂ u₃ ha hb
  exact a40_shared_face_1p_core _ _ u₂ u₃ a36_shared_z_unit a36_shared_w_unit ha hb
#print axioms a40_shared_face_1p

theorem a40_shared_face_1m :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₂ u₃ : ℂ, star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 (-1) u₂ u₃ = ditamc X Y D := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₂ u₃ ha hb
  exact a40_shared_face_1m_core _ _ u₂ u₃ a36_shared_z_unit a36_shared_w_unit ha hb
#print axioms a40_shared_face_1m

theorem a40_shared_face_2p :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₃ : ℂ, star u₁ * u₁ = 1 → star u₃ * u₃ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ 1 u₃ = dita28 X Y D := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₃ ha hb
  exact a40_shared_face_2p_core _ _ u₁ u₃ a36_shared_z_unit a36_shared_w_unit ha hb
#print axioms a40_shared_face_2p

theorem a40_shared_face_3p :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ 1 = (dita28 X Y D)ᵀ := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ ha hb
  exact a40_shared_face_3p_core _ _ u₁ u₂ a36_shared_z_unit a36_shared_w_unit ha hb
#print axioms a40_shared_face_3p

theorem a40_shared_face_3m :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 →
    ∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ (-1) = (ditamr X Y D)ᵀ := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ ha hb
  exact a40_shared_face_3m_core _ _ u₁ u₂ a36_shared_z_unit a36_shared_w_unit ha hb
#print axioms a40_shared_face_3m

theorem a40_shared_excl_k1_c :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak1 X Y D) → u₂ = 1 ∧ u₃ = 1 := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ u₃ h1 h2 h3
  exact a40_shared_excl_k1_c_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3
#print axioms a40_shared_excl_k1_c

theorem a40_shared_excl_k1_r :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak1 X Y D)ᵀ) → u₁ = 1 ∧ u₃ = 1 := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ u₃ h1 h2 h3
  exact a40_shared_excl_k1_r_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3
#print axioms a40_shared_excl_k1_r

theorem a40_shared_excl_k2_c :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak2 X Y D) → u₂ = 1 := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ u₃ h1 h2 h3
  exact a40_shared_excl_k2_c_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3
#print axioms a40_shared_excl_k2_c

theorem a40_shared_excl_k2_r :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak2 X Y D)ᵀ) → u₂ = 1 := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ u₃ h1 h2 h3
  exact a40_shared_excl_k2_r_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3
#print axioms a40_shared_excl_k2_r

theorem a40_shared_excl_k3_c :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak3 X Y D) → u₂ = 1 ∧ u₃ = 1 := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ u₃ h1 h2 h3
  exact a40_shared_excl_k3_c_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3
#print axioms a40_shared_excl_k3_c

theorem a40_shared_excl_k3_r :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak3 X Y D)ᵀ) → u₁ = 1 ∧ u₂ = 1 ∧ u₃ = 1 := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ u₃ h1 h2 h3
  exact a40_shared_excl_k3_r_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3
#print axioms a40_shared_excl_k3_r

theorem a40_shared_excl_k4_c :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditak4 X Y D) → u₁ = 1 ∧ u₃ = 1 := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ u₃ h1 h2 h3
  exact a40_shared_excl_k4_c_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3
#print axioms a40_shared_excl_k4_c

theorem a40_shared_excl_k4_r :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditak4 X Y D)ᵀ) → u₂ = 1 ∧ u₃ = 1 := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ u₃ h1 h2 h3
  exact a40_shared_excl_k4_r_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3
#print axioms a40_shared_excl_k4_r

theorem a40_shared_excl_e1_c :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditae1 X Y D) → u₂ = 1 ∧ u₃ = 1 := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ u₃ h1 h2 h3
  exact a40_shared_excl_e1_c_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3
#print axioms a40_shared_excl_e1_c

theorem a40_shared_excl_e1_r :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditae1 X Y D)ᵀ) → u₁ = 1 := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ u₃ h1 h2 h3
  exact a40_shared_excl_e1_r_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3
#print axioms a40_shared_excl_e1_r

theorem a40_shared_excl_e2_c :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditae2 X Y D) → u₃ = 1 := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ u₃ h1 h2 h3
  exact a40_shared_excl_e2_c_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3
#print axioms a40_shared_excl_e2_c

theorem a40_shared_excl_e2_r :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditae2 X Y D)ᵀ) → u₂ = 1 := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ u₃ h1 h2 h3
  exact a40_shared_excl_e2_r_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3
#print axioms a40_shared_excl_e2_r

theorem a40_shared_excl_t1_c :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = dita28 X Y D) → u₂ = 1 := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ u₃ h1 h2 h3
  exact a40_shared_excl_t1_c_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3
#print axioms a40_shared_excl_t1_c

theorem a40_shared_excl_t1_r :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (dita28 X Y D)ᵀ) → u₃ = 1 := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ u₃ h1 h2 h3
  exact a40_shared_excl_t1_r_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3
#print axioms a40_shared_excl_t1_r

theorem a40_shared_excl_t2_c :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditat2 X Y D) → u₁ = 1 := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ u₃ h1 h2 h3
  exact a40_shared_excl_t2_c_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3
#print axioms a40_shared_excl_t2_c

theorem a40_shared_excl_t2_r :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditat2 X Y D)ᵀ) → u₂ = 1 ∧ u₃ = 1 := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ u₃ h1 h2 h3
  exact a40_shared_excl_t2_r_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3
#print axioms a40_shared_excl_t2_r

theorem a40_shared_excl_t3_c :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditat3 X Y D) → u₁ = 1 ∧ u₂ = 1 := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ u₃ h1 h2 h3
  exact a40_shared_excl_t3_c_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3
#print axioms a40_shared_excl_t3_c

theorem a40_shared_excl_t3_r :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditat3 X Y D)ᵀ) → u₂ = 1 := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ u₃ h1 h2 h3
  exact a40_shared_excl_t3_r_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3
#print axioms a40_shared_excl_t3_r

theorem a40_shared_excl_mc_c :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = ditamc X Y D) → u₁ = -1 := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ u₃ h1 h2 h3
  exact a40_shared_excl_mc_c_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3
#print axioms a40_shared_excl_mc_c

theorem a40_shared_excl_mr_r :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
  let R : Fin 9 → Equiv.Perm (Fin 4) × Equiv.Perm (Fin 4) := ![((1 : Equiv.Perm (Fin 4)), (1 : Equiv.Perm (Fin 4))), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (2 : Fin 4) 3), ((1 : Equiv.Perm (Fin 4)), Equiv.swap (1 : Fin 4) 2), (Equiv.swap (2 : Fin 4) 3, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (2 : Fin 4) 3, Equiv.swap (1 : Fin 4) 2), (Equiv.swap (1 : Fin 4) 2, (1 : Equiv.Perm (Fin 4))), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (2 : Fin 4) 3), (Equiv.swap (1 : Fin 4) 2, Equiv.swap (1 : Fin 4) 2)]
  let tup : Fin 9 → ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) := fun r z i =>
    (FibreGram (0 : Fin 1) (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] p.1 q.1)) ((R r).1 i)).submatrix (R r).2 (R r).2
  let pt : Fin 9 → ℂ → EuclideanSpace ℂ ((Fin 4 × Fin 4 × Fin 4) × (Fin 4 × Fin 4 × Fin 4)) := fun r z => featureVec (tup r z)
  let v₁ : Fin 9 → Fin 6 := ![0, 2, 4, 2, 0, 3, 4, 5, 0]
  let v₂ : Fin 9 → Fin 6 := ![1, 3, 5, 5, 4, 1, 3, 1, 2]
  let prod : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun X Y i => Matrix.of fun j k => X i.1 j.1 k.1 * Y i.2 j.2 k.2
  let S : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ X Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ X ∧ RealizableGram (Fin 1) Γ₀ Y ∧ featureVec (prod X Y) = x}
  let tor : Fin 9 → Fin 9 → Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := fun r s => {x | ∃ z w : ℂ, star z * z = 1 ∧ star w * w = 1 ∧ x = featureVec (prod (tup r z) (tup s w))}
  let adj : Fin 9 → Fin 9 → Prop := fun r r' => r ≠ r' ∧ (v₁ r = v₁ r' ∨ v₁ r = v₂ r' ∨ v₂ r = v₁ r' ∨ v₂ r = v₂ r')
  let μ : Fin 9 → Fin 9 → ℂ := fun r r' => if v₁ r = v₁ r' ∨ v₁ r = v₂ r' then (1 : ℂ) else -1
  let Γ : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ := Matrix.of fun i j => Γ₀ i.1 j.1 * Γ₀ i.2 j.2
  let N : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) Γ G ∧ featureVec G = x}
  let gram : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) := fun H i => Matrix.of fun j k => star (H i j) * H i k
  let fl : Matrix (Fin 4) (Fin 4) ℂ → Prop := fun X => X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a c : Fin 4, ‖X a c‖ = 1 / 2
  let dita : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let ditaT : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let Δc : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ c, fl (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ featureVec (gram (dita X Y D)) = x}
  let Δr : Set (EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)))) := {x | ∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (E : Fin 4 → Fin 4 → ℂ), fl X ∧ (∀ a, fl (Y a)) ∧ (∀ a d, ‖E a d‖ = 1) ∧ featureVec (gram (ditaT X Y E)) = x}
  let F4 : ℂ → Matrix (Fin 4) (Fin 4) ℂ := fun z => Matrix.of fun a c => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c
  let dg : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y D => Matrix.of fun i j => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2
  let dgT : ∀ {α β : Type}, Matrix α α ℂ → (α → Matrix β β ℂ) → (α → β → ℂ) → Matrix (α × β) (α × β) ℂ := fun X Y E => Matrix.of fun i j => X i.1 j.1 * E i.1 j.2 * Y i.1 i.2 j.2
  let flg : ∀ {α : Type} [Fintype α] [DecidableEq α], Matrix α α ℂ → Prop := fun {α : Type} [Fintype α] [DecidableEq α] (X : Matrix α α ℂ) => X ∈ Matrix.unitaryGroup α ℂ ∧ ∀ a c, ‖X a c‖ ^ 2 = 1 / (Fintype.card α : ℝ)
  let r28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2))
  let c28 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2))
  let dita28 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r28 i) (c28 j)
  let r82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (@finProdFinEquiv 4 2 (i.1, @Fin.divNat 2 2 i.2), @Fin.modNat 2 2 i.2)
  let c82 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (@finProdFinEquiv 4 2 (j.1, @Fin.divNat 2 2 j.2), @Fin.modNat 2 2 j.2)
  let dita82 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (r82 i) (c82 j)
  let z : ℂ := 3 / 5 + (4 / 5) * Complex.I
  let w : ℂ := 5 / 13 + (12 / 13) * Complex.I
  let SIG : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Matrix.of fun i j => F4 z i.1 j.1 * F4 w i.2 j.2
  let Wt : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => if i.1.val % 2 = 0 ∧ j.1.val % 2 = 0 then (if i.2 = 1 then 1 else 0) + (if j.2 = 1 then 1 else 0) else 0
  let Pu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Wt i j
  let u₆₀ : ℂ := 3599 / 3601 + (120 / 3601) * Complex.I
  let P : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := Pu u₆₀
  let rk1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2)
  let ck1 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)
  let ditak1 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk1 i) (ck1 j)
  let rk2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2)
  let ck2 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak2 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk2 i) (ck2 j)
  let rk3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2)
  let ck3 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2)
  let ditak3 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk3 i) (ck3 j)
  let rk4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2)
  let ck4 : Fin 4 × Fin 4 → Fin 4 × Fin 4 := fun j => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2)
  let ditak4 : Matrix (Fin 4) (Fin 4) ℂ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Fin 4 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rk4 i) (ck4 j)
  let re1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2)
  let ce1 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2)
  let ditae1 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re1 i) (ce1 j)
  let re2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun i => (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2)
  let ce2 : Fin 4 × Fin 4 → Fin 8 × Fin 2 := fun j => (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2)
  let ditae2 : Matrix (Fin 8) (Fin 8) ℂ → (Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) → (Fin 8 → Fin 2 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (re2 i) (ce2 j)
  let rt2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2)
  let ct2 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat2 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt2 i) (ct2 j)
  let rt3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2)
  let ct3 : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditat3 : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rt3 i) (ct3 j)
  let Ew : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let Hu : ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u => Matrix.of fun i j => SIG i j * u ^ Ew i j
  let Ea : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0)
  let Eb : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if i.1 = 2 ∧ j.2 = 1 then 1 else 0)
  let Ec : Fin 4 × Fin 4 → Fin 4 × Fin 4 → ℕ := fun i j => (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)
  let H3 : ℂ → ℂ → ℂ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun u₁ u₂ u₃ => Matrix.of fun i j => SIG i j * u₁ ^ Ea i j * u₂ ^ Eb i j * u₃ ^ Ec i j
  let rmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 1], ![0, 0, 1, 0], ![0, 0, 1, 1], ![0, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 4], ![5, 6, 5, 6], ![7, 4, 7, 3]] i.1 i.2)
  let cmc : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2)
  let ditamc : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmc i) (cmc j)
  let rmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun i => (![![0, 0, 1, 0], ![0, 0, 0, 0], ![0, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 0, 2], ![3, 4, 5, 6], ![7, 1, 7, 2], ![3, 4, 5, 6]] i.1 i.2)
  let cmr : Fin 4 × Fin 4 → Fin 2 × Fin 8 := fun j => (![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] j.1 j.2)
  let ditamr : Matrix (Fin 2) (Fin 2) ℂ → (Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) → (Fin 2 → Fin 8 → ℂ) → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun X Y D => Matrix.of fun i j => dg X Y D (rmr i) (cmr j)
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ H3 u₁ u₂ u₃ = (ditamr X Y D)ᵀ) → u₃ = -1 := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ u₃ h1 h2 h3
  exact a40_shared_excl_mr_r_core _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3
#print axioms a40_shared_excl_mr_r

end DitaTorusLocus
end OIBridge
