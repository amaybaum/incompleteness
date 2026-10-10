import OIBridge.DitaLocalEscape

/-!
# Act 39 — the three-parameter realizable family through the product-embedded stratum point

Act 38 exhibited an exponent matrix `E = A + B + C` with entries in `{0, 1}`, three disjoint pieces, for
which the arc `SIG ∘ u^E` through the certified rational stratum point `SIG = F₄(z) ⊗ F₄(w)`,
`z = (3+4i)/5`, `w = (5+12i)/13`, is a complex Hadamard matrix at every unit `u`. This module states the
three-parameter family `H3 u₁ u₂ u₃ = SIG ∘ u₁^A u₂^B u₃^C` realizable on the whole torus: for all units
`u₁, u₂, u₃`, `H3 u₁ u₂ u₃` is a flat unitary, its Gram family is realizable, and its feature vector lies
in the product normalized set. It also states the family through the stratum point, `H3 1 1 1 = SIG`,
and its diagonal equal to act 38's arc, `H3 u u u = Hu u`. It says nothing about which points of the
torus admit a Diţă structure.

The module carries no definition. Every theorem prints its axioms.
-/

namespace OIBridge
namespace DitaTorus

open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted
  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries
  OrbitGeometryRigidity OrbitIsometryGroup ProductStratum DitaHull DitaHierarchy DitaArcExclusivity DitaLocalEscape

theorem a39_shared_conj_half :
    star (1 / 2 : ℂ) = 1 / 2 := by
  first
  | (simp [Complex.ext_iff, Complex.star_def]; norm_num)
  | simp [Complex.ext_iff, Complex.star_def]
  | norm_num [Complex.ext_iff, Complex.star_def]
#print axioms a39_shared_conj_half

theorem a39_shared_conj_half_ring :
    (starRingEnd ℂ) (1 / 2 : ℂ) = 1 / 2 := by
  first
  | exact a39_shared_conj_half
  | (simp [Complex.ext_iff]; norm_num)
  | simp [Complex.ext_iff]
  | norm_num [Complex.ext_iff]
#print axioms a39_shared_conj_half_ring

theorem a39_shared_conj_two :
    star (2 : ℂ) = 2 := by
  first
  | (simp [Complex.ext_iff, Complex.star_def]; norm_num)
  | simp [Complex.ext_iff, Complex.star_def]
  | norm_num [Complex.ext_iff, Complex.star_def]
#print axioms a39_shared_conj_two

theorem a39_shared_conj_two_ring :
    (starRingEnd ℂ) (2 : ℂ) = 2 := by
  first
  | exact a39_shared_conj_two
  | (simp [Complex.ext_iff]; norm_num)
  | simp [Complex.ext_iff]
  | norm_num [Complex.ext_iff]
#print axioms a39_shared_conj_two_ring

theorem a39_shared_inv_of_unit :
    ∀ x : ℂ, star x * x = 1 → star x = x⁻¹ := by
  intro x h
  exact eq_inv_of_mul_eq_one_left h
#print axioms a39_shared_inv_of_unit

theorem a39_shared_ne_zero_of_unit :
    ∀ x : ℂ, star x * x = 1 → x ≠ 0 := by
  intro x h hx
  rw [hx, mul_zero] at h
  exact zero_ne_one h
#print axioms a39_shared_ne_zero_of_unit

theorem a39_shared_row_core_00_0 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), d) k) = if ((0 : Fin 4), (0 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_00_0

theorem a39_shared_row_core_00_1 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), d) k) = if ((0 : Fin 4), (0 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_00_1

theorem a39_shared_row_core_00_2 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), d) k) = if ((0 : Fin 4), (0 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_00_2

theorem a39_shared_row_core_00_3 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), d) k) = if ((0 : Fin 4), (0 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_00_3

theorem a39_shared_row_core_00 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) j k) = if ((0 : Fin 4), (0 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a39_shared_row_core_00_0 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_00_1 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_00_2 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_00_3 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
#print axioms a39_shared_row_core_00

theorem a39_shared_row_core_01_0 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), d) k) = if ((0 : Fin 4), (1 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_01_0

theorem a39_shared_row_core_01_1 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), d) k) = if ((0 : Fin 4), (1 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_01_1

theorem a39_shared_row_core_01_2 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), d) k) = if ((0 : Fin 4), (1 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_01_2

theorem a39_shared_row_core_01_3 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), d) k) = if ((0 : Fin 4), (1 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_01_3

theorem a39_shared_row_core_01 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) j k) = if ((0 : Fin 4), (1 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a39_shared_row_core_01_0 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_01_1 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_01_2 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_01_3 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
#print axioms a39_shared_row_core_01

theorem a39_shared_row_core_02_0 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), d) k) = if ((0 : Fin 4), (2 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_02_0

theorem a39_shared_row_core_02_1 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), d) k) = if ((0 : Fin 4), (2 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_02_1

theorem a39_shared_row_core_02_2 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), d) k) = if ((0 : Fin 4), (2 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_02_2

theorem a39_shared_row_core_02_3 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), d) k) = if ((0 : Fin 4), (2 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_02_3

theorem a39_shared_row_core_02 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) j k) = if ((0 : Fin 4), (2 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a39_shared_row_core_02_0 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_02_1 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_02_2 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_02_3 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
#print axioms a39_shared_row_core_02

theorem a39_shared_row_core_03_0 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), d) k) = if ((0 : Fin 4), (3 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_03_0

theorem a39_shared_row_core_03_1 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), d) k) = if ((0 : Fin 4), (3 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_03_1

theorem a39_shared_row_core_03_2 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), d) k) = if ((0 : Fin 4), (3 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_03_2

theorem a39_shared_row_core_03_3 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), d) k) = if ((0 : Fin 4), (3 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_03_3

theorem a39_shared_row_core_03 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) j k) = if ((0 : Fin 4), (3 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a39_shared_row_core_03_0 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_03_1 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_03_2 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_03_3 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
#print axioms a39_shared_row_core_03

theorem a39_shared_row_core_10_0 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), d) k) = if ((1 : Fin 4), (0 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_10_0

theorem a39_shared_row_core_10_1 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), d) k) = if ((1 : Fin 4), (0 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_10_1

theorem a39_shared_row_core_10_2 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), d) k) = if ((1 : Fin 4), (0 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_10_2

theorem a39_shared_row_core_10_3 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), d) k) = if ((1 : Fin 4), (0 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_10_3

theorem a39_shared_row_core_10 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) j k) = if ((1 : Fin 4), (0 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a39_shared_row_core_10_0 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_10_1 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_10_2 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_10_3 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
#print axioms a39_shared_row_core_10

theorem a39_shared_row_core_11_0 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), d) k) = if ((1 : Fin 4), (1 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_11_0

theorem a39_shared_row_core_11_1 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), d) k) = if ((1 : Fin 4), (1 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_11_1

theorem a39_shared_row_core_11_2 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), d) k) = if ((1 : Fin 4), (1 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_11_2

theorem a39_shared_row_core_11_3 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), d) k) = if ((1 : Fin 4), (1 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_11_3

theorem a39_shared_row_core_11 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) j k) = if ((1 : Fin 4), (1 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a39_shared_row_core_11_0 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_11_1 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_11_2 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_11_3 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
#print axioms a39_shared_row_core_11

theorem a39_shared_row_core_12_0 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), d) k) = if ((1 : Fin 4), (2 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_12_0

theorem a39_shared_row_core_12_1 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), d) k) = if ((1 : Fin 4), (2 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_12_1

theorem a39_shared_row_core_12_2 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), d) k) = if ((1 : Fin 4), (2 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_12_2

theorem a39_shared_row_core_12_3 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), d) k) = if ((1 : Fin 4), (2 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_12_3

theorem a39_shared_row_core_12 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) j k) = if ((1 : Fin 4), (2 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a39_shared_row_core_12_0 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_12_1 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_12_2 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_12_3 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
#print axioms a39_shared_row_core_12

theorem a39_shared_row_core_13_0 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), d) k) = if ((1 : Fin 4), (3 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_13_0

theorem a39_shared_row_core_13_1 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), d) k) = if ((1 : Fin 4), (3 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_13_1

theorem a39_shared_row_core_13_2 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), d) k) = if ((1 : Fin 4), (3 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_13_2

theorem a39_shared_row_core_13_3 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), d) k) = if ((1 : Fin 4), (3 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_13_3

theorem a39_shared_row_core_13 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) j k) = if ((1 : Fin 4), (3 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a39_shared_row_core_13_0 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_13_1 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_13_2 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_13_3 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
#print axioms a39_shared_row_core_13

theorem a39_shared_row_core_20_0 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), d) k) = if ((2 : Fin 4), (0 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_20_0

theorem a39_shared_row_core_20_1 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), d) k) = if ((2 : Fin 4), (0 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_20_1

theorem a39_shared_row_core_20_2 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), d) k) = if ((2 : Fin 4), (0 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_20_2

theorem a39_shared_row_core_20_3 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), d) k) = if ((2 : Fin 4), (0 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_20_3

theorem a39_shared_row_core_20 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) j k) = if ((2 : Fin 4), (0 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a39_shared_row_core_20_0 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_20_1 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_20_2 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_20_3 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
#print axioms a39_shared_row_core_20

theorem a39_shared_row_core_21_0 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), d) k) = if ((2 : Fin 4), (1 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_21_0

theorem a39_shared_row_core_21_1 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), d) k) = if ((2 : Fin 4), (1 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_21_1

theorem a39_shared_row_core_21_2 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), d) k) = if ((2 : Fin 4), (1 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_21_2

theorem a39_shared_row_core_21_3 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), d) k) = if ((2 : Fin 4), (1 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_21_3

theorem a39_shared_row_core_21 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) j k) = if ((2 : Fin 4), (1 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a39_shared_row_core_21_0 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_21_1 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_21_2 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_21_3 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
#print axioms a39_shared_row_core_21

theorem a39_shared_row_core_22_0 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), d) k) = if ((2 : Fin 4), (2 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_22_0

theorem a39_shared_row_core_22_1 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), d) k) = if ((2 : Fin 4), (2 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_22_1

theorem a39_shared_row_core_22_2 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), d) k) = if ((2 : Fin 4), (2 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_22_2

theorem a39_shared_row_core_22_3 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), d) k) = if ((2 : Fin 4), (2 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_22_3

theorem a39_shared_row_core_22 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) j k) = if ((2 : Fin 4), (2 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a39_shared_row_core_22_0 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_22_1 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_22_2 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_22_3 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
#print axioms a39_shared_row_core_22

theorem a39_shared_row_core_23_0 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), d) k) = if ((2 : Fin 4), (3 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_23_0

theorem a39_shared_row_core_23_1 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), d) k) = if ((2 : Fin 4), (3 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_23_1

theorem a39_shared_row_core_23_2 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), d) k) = if ((2 : Fin 4), (3 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_23_2

theorem a39_shared_row_core_23_3 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), d) k) = if ((2 : Fin 4), (3 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_23_3

theorem a39_shared_row_core_23 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) j k) = if ((2 : Fin 4), (3 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a39_shared_row_core_23_0 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_23_1 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_23_2 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_23_3 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
#print axioms a39_shared_row_core_23

theorem a39_shared_row_core_30_0 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), d) k) = if ((3 : Fin 4), (0 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_30_0

theorem a39_shared_row_core_30_1 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), d) k) = if ((3 : Fin 4), (0 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_30_1

theorem a39_shared_row_core_30_2 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), d) k) = if ((3 : Fin 4), (0 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_30_2

theorem a39_shared_row_core_30_3 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), d) k) = if ((3 : Fin 4), (0 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_30_3

theorem a39_shared_row_core_30 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) j k) = if ((3 : Fin 4), (0 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a39_shared_row_core_30_0 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_30_1 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_30_2 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_30_3 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
#print axioms a39_shared_row_core_30

theorem a39_shared_row_core_31_0 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), d) k) = if ((3 : Fin 4), (1 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_31_0

theorem a39_shared_row_core_31_1 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), d) k) = if ((3 : Fin 4), (1 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_31_1

theorem a39_shared_row_core_31_2 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), d) k) = if ((3 : Fin 4), (1 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_31_2

theorem a39_shared_row_core_31_3 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), d) k) = if ((3 : Fin 4), (1 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_31_3

theorem a39_shared_row_core_31 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) j k) = if ((3 : Fin 4), (1 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a39_shared_row_core_31_0 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_31_1 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_31_2 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_31_3 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
#print axioms a39_shared_row_core_31

theorem a39_shared_row_core_32_0 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), d) k) = if ((3 : Fin 4), (2 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_32_0

theorem a39_shared_row_core_32_1 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), d) k) = if ((3 : Fin 4), (2 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_32_1

theorem a39_shared_row_core_32_2 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), d) k) = if ((3 : Fin 4), (2 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_32_2

theorem a39_shared_row_core_32_3 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), d) k) = if ((3 : Fin 4), (2 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_32_3

theorem a39_shared_row_core_32 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) j k) = if ((3 : Fin 4), (2 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a39_shared_row_core_32_0 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_32_1 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_32_2 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_32_3 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
#print axioms a39_shared_row_core_32

theorem a39_shared_row_core_33_0 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), d) k) = if ((3 : Fin 4), (3 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_33_0

theorem a39_shared_row_core_33_1 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), d) k) = if ((3 : Fin 4), (3 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_33_1

theorem a39_shared_row_core_33_2 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), d) k) = if ((3 : Fin 4), (3 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_33_2

theorem a39_shared_row_core_33_3 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), d) k) = if ((3 : Fin 4), (3 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  have hsz : star z = z⁻¹ := a39_shared_inv_of_unit z hz
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have h0z : z ≠ 0 := a39_shared_ne_zero_of_unit z hz
  have hsw : star w = w⁻¹ := a39_shared_inv_of_unit w hw
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have h0w : w ≠ 0 := a39_shared_ne_zero_of_unit w hw
  have hs1 : star u₁ = u₁⁻¹ := a39_shared_inv_of_unit u₁ h1
  have hs1' : (starRingEnd ℂ) u₁ = u₁⁻¹ := hs1
  have h01 : u₁ ≠ 0 := a39_shared_ne_zero_of_unit u₁ h1
  have hs2 : star u₂ = u₂⁻¹ := a39_shared_inv_of_unit u₂ h2
  have hs2' : (starRingEnd ℂ) u₂ = u₂⁻¹ := hs2
  have h02 : u₂ ≠ 0 := a39_shared_ne_zero_of_unit u₂ h2
  have hs3 : star u₃ = u₃⁻¹ := a39_shared_inv_of_unit u₃ h3
  have hs3' : (starRingEnd ℂ) u₃ = u₃⁻¹ := hs3
  have h03 : u₃ ≠ 0 := a39_shared_ne_zero_of_unit u₃ h3
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hs1, hs2, hs3, hsz', hsw', hs1', hs2', hs3', a39_shared_conj_half, a39_shared_conj_half_ring, a39_shared_conj_two, a39_shared_conj_two_ring, map_ofNat] <;> (try simp only [a39_shared_conj_two, a39_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a39_shared_row_core_33_3

theorem a39_shared_row_core_33 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) j k) = if ((3 : Fin 4), (3 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a39_shared_row_core_33_0 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_33_1 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_33_2 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
  · exact a39_shared_row_core_33_3 z w u₁ u₂ u₃ hz hw h1 h2 h3 d
#print axioms a39_shared_row_core_33

theorem a39_shared_rowblock_core_0 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ (b : Fin 4) (j : Fin 4 × Fin 4), ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((0 : Fin 4), b) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) j k) = if ((0 : Fin 4), b) = j then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 b j
  fin_cases b
  · exact a39_shared_row_core_00 z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  · exact a39_shared_row_core_01 z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  · exact a39_shared_row_core_02 z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  · exact a39_shared_row_core_03 z w u₁ u₂ u₃ hz hw h1 h2 h3 j
#print axioms a39_shared_rowblock_core_0

theorem a39_shared_rowblock_core_1 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ (b : Fin 4) (j : Fin 4 × Fin 4), ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((1 : Fin 4), b) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) j k) = if ((1 : Fin 4), b) = j then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 b j
  fin_cases b
  · exact a39_shared_row_core_10 z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  · exact a39_shared_row_core_11 z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  · exact a39_shared_row_core_12 z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  · exact a39_shared_row_core_13 z w u₁ u₂ u₃ hz hw h1 h2 h3 j
#print axioms a39_shared_rowblock_core_1

theorem a39_shared_rowblock_core_2 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ (b : Fin 4) (j : Fin 4 × Fin 4), ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((2 : Fin 4), b) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) j k) = if ((2 : Fin 4), b) = j then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 b j
  fin_cases b
  · exact a39_shared_row_core_20 z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  · exact a39_shared_row_core_21 z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  · exact a39_shared_row_core_22 z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  · exact a39_shared_row_core_23 z w u₁ u₂ u₃ hz hw h1 h2 h3 j
#print axioms a39_shared_rowblock_core_2

theorem a39_shared_rowblock_core_3 :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ (b : Fin 4) (j : Fin 4 × Fin 4), ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ((3 : Fin 4), b) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) j k) = if ((3 : Fin 4), b) = j then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 b j
  fin_cases b
  · exact a39_shared_row_core_30 z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  · exact a39_shared_row_core_31 z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  · exact a39_shared_row_core_32 z w u₁ u₂ u₃ hz hw h1 h2 h3 j
  · exact a39_shared_row_core_33 z w u₁ u₂ u₃ hz hw h1 h2 h3 j
#print axioms a39_shared_rowblock_core_3

theorem a39_shared_rows_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ i j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) i k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) j k) = if i = j then (1 : ℂ) else 0 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 i j
  obtain ⟨a, b⟩ := i
  fin_cases a
  · exact a39_shared_rowblock_core_0 z w u₁ u₂ u₃ hz hw h1 h2 h3 b j
  · exact a39_shared_rowblock_core_1 z w u₁ u₂ u₃ hz hw h1 h2 h3 b j
  · exact a39_shared_rowblock_core_2 z w u₁ u₂ u₃ hz hw h1 h2 h3 b j
  · exact a39_shared_rowblock_core_3 z w u₁ u₂ u₃ hz hw h1 h2 h3 b j
#print axioms a39_shared_rows_core

theorem a39_shared_unitary_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3
  rw [Matrix.mem_unitaryGroup_iff]
  ext i j
  rw [Matrix.mul_apply, Matrix.one_apply]
  simp only [Matrix.star_apply]
  exact a39_shared_rows_core z w u₁ u₂ u₃ hz hw h1 h2 h3 i j
#print axioms a39_shared_unitary_core

theorem a39_shared_flat_core :
    ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → ∀ i j, ‖(Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) i j‖ = 1 / 4 := by
  intro z w u₁ u₂ u₃ hz hw h1 h2 h3 i j
  have hz1 := a35_shared_half z hz i.1 j.1
  have hw1 := a35_shared_half w hw i.2 j.2
  simp only [Matrix.of_apply] at hz1 hw1 ⊢
  rw [norm_mul, norm_mul, norm_mul, norm_mul, hz1, hw1, norm_pow, norm_pow, norm_pow, a35_shared_norm_of_unit u₁ h1, a35_shared_norm_of_unit u₂ h2, a35_shared_norm_of_unit u₃ h3, one_pow, one_pow, one_pow]
  norm_num
#print axioms a39_shared_flat_core

theorem a39_shared_real_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ z w u₁ u₂ u₃ : ℂ, star z * z = 1 → star w * w = 1 → star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 → (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) i k) ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u₁ ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u₂ ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u₃ ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) i k) ∈ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) G ∧ featureVec G = x} := by
  intro Γ₀ hΓ₀ z w u₁ u₂ u₃ hz hw h1 h2 h3
  have hU := a39_shared_unitary_core z w u₁ u₂ u₃ hz hw h1 h2 h3
  have hF := a39_shared_flat_core z w u₁ u₂ u₃ hz hw h1 h2 h3
  have hR := a35_shared_gram_realizable Γ₀ hΓ₀ _ hU hF
  exact ⟨hU, hF, hR, ⟨_, hR, rfl⟩⟩
#print axioms a39_shared_real_core

theorem a39_shared_base_core :
    (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * 1 ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * 1 ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * 1 ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) := by
  ext i j
  simp only [Matrix.of_apply, one_pow, mul_one]
#print axioms a39_shared_base_core

theorem a39_shared_diag_core :
    ∀ u : ℂ, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ (if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) * u ^ (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) * u ^ (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) := by
  intro u
  ext i j
  simp only [Matrix.of_apply]
  rw [pow_add, pow_add]
  ring
#print axioms a39_shared_diag_core

theorem a39_shared_realizable :
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
  ∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →
    H3 u₁ u₂ u₃ ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖H3 u₁ u₂ u₃ i j‖ = 1 / 4)
    ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (H3 u₁ u₂ u₃)) ∧ featureVec (gram (H3 u₁ u₂ u₃)) ∈ N := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u₁ u₂ u₃ h1 h2 h3
  exact a39_shared_real_core Γ₀ hΓ₀ _ _ u₁ u₂ u₃ a36_shared_z_unit a36_shared_w_unit h1 h2 h3
#print axioms a39_shared_realizable

theorem a39_control_base :
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
  H3 1 1 1 = SIG := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a39_shared_base_core
#print axioms a39_control_base

theorem a39_control_diagonal :
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
  ∀ u : ℂ, H3 u u u = Hu u := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a39_shared_diag_core
#print axioms a39_control_diagonal
end DitaTorus
end OIBridge
