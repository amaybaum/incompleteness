import OIBridge.DitaArcExclusivity

/-!
# Act 38 — a genuine non-Diţă local escape at the product-embedded stratum point

Acts 36 and 37 ran an exact arc of realizable classes through the certified rational stratum point
`SIG = F₄(z) ⊗ F₄(w)`, `z = (3+4i)/5`, `w = (5+12i)/13`, and found it exclusive to its frozen `2 × 8` Diţă
class: an arc that lies in one Diţă hull at every parameter. This module states, for one explicit
exponent matrix `E = A + B + C` in `{0, 1}` and the arc `Hu u = SIG ∘ u^E`: that `Hu u` is a flat unitary
— a complex Hadamard matrix, realizable — at every unit `u`; that for each of the nine Diţă factorization
classes of `SIG` — four `4 × 4`, two `8 × 2` and three `2 × 8`, the complete census of the stratum point's
Diţă structures modulo its stabilizer — a Diţă form of `Hu u` at that class's index maps, in either
orientation, forces `u = 1`; and, as the corollary, that every neighbourhood of `SIG` contains a
realizable matrix admitting none of the eighteen forms. The exact-computation layer carries the
exhaustive complement: at every unit `u ∉ {1, −1}`, no index maps whatever admit a Diţă form of `Hu u`,
and at `u = −1` exactly one `2 × 8` structure per orientation does.

The module carries no definition. Every theorem prints its axioms.
-/

namespace OIBridge
namespace DitaLocalEscape

open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality OrbitLawRigidityTwisted
  OrbitLawNaturalityFactorization OrbitLawGaps OrbitGeometrySelector OrbitGeometryIsometries
  OrbitGeometryRigidity OrbitIsometryGroup ProductStratum DitaHull DitaHierarchy DitaArcExclusivity

theorem a38_shared_conj_half :
    star (1 / 2 : ℂ) = 1 / 2 := by
  first
  | (simp [Complex.ext_iff, Complex.star_def]; norm_num)
  | simp [Complex.ext_iff, Complex.star_def]
  | norm_num [Complex.ext_iff, Complex.star_def]
#print axioms a38_shared_conj_half

theorem a38_shared_conj_half_ring :
    (starRingEnd ℂ) (1 / 2 : ℂ) = 1 / 2 := by
  first
  | exact a38_shared_conj_half
  | (simp [Complex.ext_iff]; norm_num)
  | simp [Complex.ext_iff]
  | norm_num [Complex.ext_iff]
#print axioms a38_shared_conj_half_ring

theorem a38_shared_conj_two :
    star (2 : ℂ) = 2 := by
  first
  | (simp [Complex.ext_iff, Complex.star_def]; norm_num)
  | simp [Complex.ext_iff, Complex.star_def]
  | norm_num [Complex.ext_iff, Complex.star_def]
#print axioms a38_shared_conj_two

theorem a38_shared_conj_two_ring :
    (starRingEnd ℂ) (2 : ℂ) = 2 := by
  first
  | exact a38_shared_conj_two
  | (simp [Complex.ext_iff]; norm_num)
  | simp [Complex.ext_iff]
  | norm_num [Complex.ext_iff]
#print axioms a38_shared_conj_two_ring

theorem a38_shared_inv_of_unit :
    ∀ x : ℂ, star x * x = 1 → star x = x⁻¹ := by
  intro x h
  exact eq_inv_of_mul_eq_one_left h
#print axioms a38_shared_inv_of_unit

theorem a38_shared_ne_zero_of_unit :
    ∀ x : ℂ, star x * x = 1 → x ≠ 0 := by
  intro x h hx
  rw [hx, mul_zero] at h
  exact zero_ne_one h
#print axioms a38_shared_ne_zero_of_unit

theorem a38_shared_row_core_00_0 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), d) k) = if ((0 : Fin 4), (0 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_00_0

theorem a38_shared_row_core_00_1 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), d) k) = if ((0 : Fin 4), (0 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_00_1

theorem a38_shared_row_core_00_2 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), d) k) = if ((0 : Fin 4), (0 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_00_2

theorem a38_shared_row_core_00_3 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), d) k) = if ((0 : Fin 4), (0 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_00_3

theorem a38_shared_row_core_00 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) j k) = if ((0 : Fin 4), (0 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u hz hw hu j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a38_shared_row_core_00_0 z w u hz hw hu d
  · exact a38_shared_row_core_00_1 z w u hz hw hu d
  · exact a38_shared_row_core_00_2 z w u hz hw hu d
  · exact a38_shared_row_core_00_3 z w u hz hw hu d
#print axioms a38_shared_row_core_00

theorem a38_shared_row_core_01_0 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), d) k) = if ((0 : Fin 4), (1 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_01_0

theorem a38_shared_row_core_01_1 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), d) k) = if ((0 : Fin 4), (1 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_01_1

theorem a38_shared_row_core_01_2 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), d) k) = if ((0 : Fin 4), (1 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_01_2

theorem a38_shared_row_core_01_3 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), d) k) = if ((0 : Fin 4), (1 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_01_3

theorem a38_shared_row_core_01 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) j k) = if ((0 : Fin 4), (1 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u hz hw hu j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a38_shared_row_core_01_0 z w u hz hw hu d
  · exact a38_shared_row_core_01_1 z w u hz hw hu d
  · exact a38_shared_row_core_01_2 z w u hz hw hu d
  · exact a38_shared_row_core_01_3 z w u hz hw hu d
#print axioms a38_shared_row_core_01

theorem a38_shared_row_core_02_0 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), d) k) = if ((0 : Fin 4), (2 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_02_0

theorem a38_shared_row_core_02_1 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), d) k) = if ((0 : Fin 4), (2 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_02_1

theorem a38_shared_row_core_02_2 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), d) k) = if ((0 : Fin 4), (2 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_02_2

theorem a38_shared_row_core_02_3 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), d) k) = if ((0 : Fin 4), (2 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_02_3

theorem a38_shared_row_core_02 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) j k) = if ((0 : Fin 4), (2 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u hz hw hu j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a38_shared_row_core_02_0 z w u hz hw hu d
  · exact a38_shared_row_core_02_1 z w u hz hw hu d
  · exact a38_shared_row_core_02_2 z w u hz hw hu d
  · exact a38_shared_row_core_02_3 z w u hz hw hu d
#print axioms a38_shared_row_core_02

theorem a38_shared_row_core_03_0 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), d) k) = if ((0 : Fin 4), (3 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_03_0

theorem a38_shared_row_core_03_1 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), d) k) = if ((0 : Fin 4), (3 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_03_1

theorem a38_shared_row_core_03_2 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), d) k) = if ((0 : Fin 4), (3 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_03_2

theorem a38_shared_row_core_03_3 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), d) k) = if ((0 : Fin 4), (3 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_03_3

theorem a38_shared_row_core_03 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) j k) = if ((0 : Fin 4), (3 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u hz hw hu j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a38_shared_row_core_03_0 z w u hz hw hu d
  · exact a38_shared_row_core_03_1 z w u hz hw hu d
  · exact a38_shared_row_core_03_2 z w u hz hw hu d
  · exact a38_shared_row_core_03_3 z w u hz hw hu d
#print axioms a38_shared_row_core_03

theorem a38_shared_row_core_10_0 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), d) k) = if ((1 : Fin 4), (0 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_10_0

theorem a38_shared_row_core_10_1 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), d) k) = if ((1 : Fin 4), (0 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_10_1

theorem a38_shared_row_core_10_2 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), d) k) = if ((1 : Fin 4), (0 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_10_2

theorem a38_shared_row_core_10_3 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), d) k) = if ((1 : Fin 4), (0 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_10_3

theorem a38_shared_row_core_10 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) j k) = if ((1 : Fin 4), (0 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u hz hw hu j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a38_shared_row_core_10_0 z w u hz hw hu d
  · exact a38_shared_row_core_10_1 z w u hz hw hu d
  · exact a38_shared_row_core_10_2 z w u hz hw hu d
  · exact a38_shared_row_core_10_3 z w u hz hw hu d
#print axioms a38_shared_row_core_10

theorem a38_shared_row_core_11_0 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), d) k) = if ((1 : Fin 4), (1 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_11_0

theorem a38_shared_row_core_11_1 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), d) k) = if ((1 : Fin 4), (1 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_11_1

theorem a38_shared_row_core_11_2 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), d) k) = if ((1 : Fin 4), (1 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_11_2

theorem a38_shared_row_core_11_3 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), d) k) = if ((1 : Fin 4), (1 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_11_3

theorem a38_shared_row_core_11 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) j k) = if ((1 : Fin 4), (1 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u hz hw hu j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a38_shared_row_core_11_0 z w u hz hw hu d
  · exact a38_shared_row_core_11_1 z w u hz hw hu d
  · exact a38_shared_row_core_11_2 z w u hz hw hu d
  · exact a38_shared_row_core_11_3 z w u hz hw hu d
#print axioms a38_shared_row_core_11

theorem a38_shared_row_core_12_0 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), d) k) = if ((1 : Fin 4), (2 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_12_0

theorem a38_shared_row_core_12_1 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), d) k) = if ((1 : Fin 4), (2 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_12_1

theorem a38_shared_row_core_12_2 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), d) k) = if ((1 : Fin 4), (2 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_12_2

theorem a38_shared_row_core_12_3 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), d) k) = if ((1 : Fin 4), (2 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_12_3

theorem a38_shared_row_core_12 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) j k) = if ((1 : Fin 4), (2 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u hz hw hu j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a38_shared_row_core_12_0 z w u hz hw hu d
  · exact a38_shared_row_core_12_1 z w u hz hw hu d
  · exact a38_shared_row_core_12_2 z w u hz hw hu d
  · exact a38_shared_row_core_12_3 z w u hz hw hu d
#print axioms a38_shared_row_core_12

theorem a38_shared_row_core_13_0 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), d) k) = if ((1 : Fin 4), (3 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_13_0

theorem a38_shared_row_core_13_1 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), d) k) = if ((1 : Fin 4), (3 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_13_1

theorem a38_shared_row_core_13_2 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), d) k) = if ((1 : Fin 4), (3 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_13_2

theorem a38_shared_row_core_13_3 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), d) k) = if ((1 : Fin 4), (3 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_13_3

theorem a38_shared_row_core_13 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) j k) = if ((1 : Fin 4), (3 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u hz hw hu j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a38_shared_row_core_13_0 z w u hz hw hu d
  · exact a38_shared_row_core_13_1 z w u hz hw hu d
  · exact a38_shared_row_core_13_2 z w u hz hw hu d
  · exact a38_shared_row_core_13_3 z w u hz hw hu d
#print axioms a38_shared_row_core_13

theorem a38_shared_row_core_20_0 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), d) k) = if ((2 : Fin 4), (0 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_20_0

theorem a38_shared_row_core_20_1 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), d) k) = if ((2 : Fin 4), (0 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_20_1

theorem a38_shared_row_core_20_2 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), d) k) = if ((2 : Fin 4), (0 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_20_2

theorem a38_shared_row_core_20_3 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), d) k) = if ((2 : Fin 4), (0 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_20_3

theorem a38_shared_row_core_20 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) j k) = if ((2 : Fin 4), (0 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u hz hw hu j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a38_shared_row_core_20_0 z w u hz hw hu d
  · exact a38_shared_row_core_20_1 z w u hz hw hu d
  · exact a38_shared_row_core_20_2 z w u hz hw hu d
  · exact a38_shared_row_core_20_3 z w u hz hw hu d
#print axioms a38_shared_row_core_20

theorem a38_shared_row_core_21_0 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), d) k) = if ((2 : Fin 4), (1 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_21_0

theorem a38_shared_row_core_21_1 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), d) k) = if ((2 : Fin 4), (1 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_21_1

theorem a38_shared_row_core_21_2 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), d) k) = if ((2 : Fin 4), (1 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_21_2

theorem a38_shared_row_core_21_3 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), d) k) = if ((2 : Fin 4), (1 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_21_3

theorem a38_shared_row_core_21 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) j k) = if ((2 : Fin 4), (1 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u hz hw hu j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a38_shared_row_core_21_0 z w u hz hw hu d
  · exact a38_shared_row_core_21_1 z w u hz hw hu d
  · exact a38_shared_row_core_21_2 z w u hz hw hu d
  · exact a38_shared_row_core_21_3 z w u hz hw hu d
#print axioms a38_shared_row_core_21

theorem a38_shared_row_core_22_0 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), d) k) = if ((2 : Fin 4), (2 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_22_0

theorem a38_shared_row_core_22_1 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), d) k) = if ((2 : Fin 4), (2 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_22_1

theorem a38_shared_row_core_22_2 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), d) k) = if ((2 : Fin 4), (2 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_22_2

theorem a38_shared_row_core_22_3 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), d) k) = if ((2 : Fin 4), (2 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_22_3

theorem a38_shared_row_core_22 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) j k) = if ((2 : Fin 4), (2 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u hz hw hu j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a38_shared_row_core_22_0 z w u hz hw hu d
  · exact a38_shared_row_core_22_1 z w u hz hw hu d
  · exact a38_shared_row_core_22_2 z w u hz hw hu d
  · exact a38_shared_row_core_22_3 z w u hz hw hu d
#print axioms a38_shared_row_core_22

theorem a38_shared_row_core_23_0 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), d) k) = if ((2 : Fin 4), (3 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_23_0

theorem a38_shared_row_core_23_1 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), d) k) = if ((2 : Fin 4), (3 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_23_1

theorem a38_shared_row_core_23_2 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), d) k) = if ((2 : Fin 4), (3 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_23_2

theorem a38_shared_row_core_23_3 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), d) k) = if ((2 : Fin 4), (3 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_23_3

theorem a38_shared_row_core_23 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) j k) = if ((2 : Fin 4), (3 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u hz hw hu j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a38_shared_row_core_23_0 z w u hz hw hu d
  · exact a38_shared_row_core_23_1 z w u hz hw hu d
  · exact a38_shared_row_core_23_2 z w u hz hw hu d
  · exact a38_shared_row_core_23_3 z w u hz hw hu d
#print axioms a38_shared_row_core_23

theorem a38_shared_row_core_30_0 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), d) k) = if ((3 : Fin 4), (0 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_30_0

theorem a38_shared_row_core_30_1 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), d) k) = if ((3 : Fin 4), (0 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_30_1

theorem a38_shared_row_core_30_2 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), d) k) = if ((3 : Fin 4), (0 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_30_2

theorem a38_shared_row_core_30_3 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), d) k) = if ((3 : Fin 4), (0 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_30_3

theorem a38_shared_row_core_30 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), (0 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) j k) = if ((3 : Fin 4), (0 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u hz hw hu j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a38_shared_row_core_30_0 z w u hz hw hu d
  · exact a38_shared_row_core_30_1 z w u hz hw hu d
  · exact a38_shared_row_core_30_2 z w u hz hw hu d
  · exact a38_shared_row_core_30_3 z w u hz hw hu d
#print axioms a38_shared_row_core_30

theorem a38_shared_row_core_31_0 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), d) k) = if ((3 : Fin 4), (1 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_31_0

theorem a38_shared_row_core_31_1 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), d) k) = if ((3 : Fin 4), (1 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_31_1

theorem a38_shared_row_core_31_2 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), d) k) = if ((3 : Fin 4), (1 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_31_2

theorem a38_shared_row_core_31_3 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), d) k) = if ((3 : Fin 4), (1 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_31_3

theorem a38_shared_row_core_31 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), (1 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) j k) = if ((3 : Fin 4), (1 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u hz hw hu j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a38_shared_row_core_31_0 z w u hz hw hu d
  · exact a38_shared_row_core_31_1 z w u hz hw hu d
  · exact a38_shared_row_core_31_2 z w u hz hw hu d
  · exact a38_shared_row_core_31_3 z w u hz hw hu d
#print axioms a38_shared_row_core_31

theorem a38_shared_row_core_32_0 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), d) k) = if ((3 : Fin 4), (2 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_32_0

theorem a38_shared_row_core_32_1 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), d) k) = if ((3 : Fin 4), (2 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_32_1

theorem a38_shared_row_core_32_2 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), d) k) = if ((3 : Fin 4), (2 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_32_2

theorem a38_shared_row_core_32_3 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), d) k) = if ((3 : Fin 4), (2 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_32_3

theorem a38_shared_row_core_32 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), (2 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) j k) = if ((3 : Fin 4), (2 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u hz hw hu j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a38_shared_row_core_32_0 z w u hz hw hu d
  · exact a38_shared_row_core_32_1 z w u hz hw hu d
  · exact a38_shared_row_core_32_2 z w u hz hw hu d
  · exact a38_shared_row_core_32_3 z w u hz hw hu d
#print axioms a38_shared_row_core_32

theorem a38_shared_row_core_33_0 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), d) k) = if ((3 : Fin 4), (3 : Fin 4)) = ((0 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_33_0

theorem a38_shared_row_core_33_1 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), d) k) = if ((3 : Fin 4), (3 : Fin 4)) = ((1 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_33_1

theorem a38_shared_row_core_33_2 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), d) k) = if ((3 : Fin 4), (3 : Fin 4)) = ((2 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_33_2

theorem a38_shared_row_core_33_3 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ d : Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), d) k) = if ((3 : Fin 4), (3 : Fin 4)) = ((3 : Fin 4), d) then (1 : ℂ) else 0 := by
  intro z w u hz hw hu d
  have hsz : star z = z⁻¹ := a38_shared_inv_of_unit z hz
  have hsw : star w = w⁻¹ := a38_shared_inv_of_unit w hw
  have hsu : star u = u⁻¹ := a38_shared_inv_of_unit u hu
  have hsz' : (starRingEnd ℂ) z = z⁻¹ := hsz
  have hsw' : (starRingEnd ℂ) w = w⁻¹ := hsw
  have hsu' : (starRingEnd ℂ) u = u⁻¹ := hsu
  have hz0 : z ≠ 0 := a38_shared_ne_zero_of_unit z hz
  have hw0 : w ≠ 0 := a38_shared_ne_zero_of_unit w hw
  have hu0 : u ≠ 0 := a38_shared_ne_zero_of_unit u hu
  fin_cases d <;> simp (config := { decide := true }) [Fintype.sum_prod_type, Fin.sum_univ_four, Matrix.of_apply, hsz, hsw, hsu, hsz', hsw', hsu', a38_shared_conj_half, a38_shared_conj_half_ring, a38_shared_conj_two, a38_shared_conj_two_ring, map_ofNat] <;> (try simp only [a38_shared_conj_two, a38_shared_conj_two_ring]) <;> (try field_simp) <;> ring
#print axioms a38_shared_row_core_33_3

theorem a38_shared_row_core_33 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), (3 : Fin 4)) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) j k) = if ((3 : Fin 4), (3 : Fin 4)) = j then (1 : ℂ) else 0 := by
  intro z w u hz hw hu j
  obtain ⟨c, d⟩ := j
  fin_cases c
  · exact a38_shared_row_core_33_0 z w u hz hw hu d
  · exact a38_shared_row_core_33_1 z w u hz hw hu d
  · exact a38_shared_row_core_33_2 z w u hz hw hu d
  · exact a38_shared_row_core_33_3 z w u hz hw hu d
#print axioms a38_shared_row_core_33

theorem a38_shared_rowblock_core_0 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ (b : Fin 4) (j : Fin 4 × Fin 4), ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), b) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) j k) = if ((0 : Fin 4), b) = j then (1 : ℂ) else 0 := by
  intro z w u hz hw hu b j
  fin_cases b
  · exact a38_shared_row_core_00 z w u hz hw hu j
  · exact a38_shared_row_core_01 z w u hz hw hu j
  · exact a38_shared_row_core_02 z w u hz hw hu j
  · exact a38_shared_row_core_03 z w u hz hw hu j
#print axioms a38_shared_rowblock_core_0

theorem a38_shared_rowblock_core_1 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ (b : Fin 4) (j : Fin 4 × Fin 4), ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), b) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) j k) = if ((1 : Fin 4), b) = j then (1 : ℂ) else 0 := by
  intro z w u hz hw hu b j
  fin_cases b
  · exact a38_shared_row_core_10 z w u hz hw hu j
  · exact a38_shared_row_core_11 z w u hz hw hu j
  · exact a38_shared_row_core_12 z w u hz hw hu j
  · exact a38_shared_row_core_13 z w u hz hw hu j
#print axioms a38_shared_rowblock_core_1

theorem a38_shared_rowblock_core_2 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ (b : Fin 4) (j : Fin 4 × Fin 4), ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), b) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) j k) = if ((2 : Fin 4), b) = j then (1 : ℂ) else 0 := by
  intro z w u hz hw hu b j
  fin_cases b
  · exact a38_shared_row_core_20 z w u hz hw hu j
  · exact a38_shared_row_core_21 z w u hz hw hu j
  · exact a38_shared_row_core_22 z w u hz hw hu j
  · exact a38_shared_row_core_23 z w u hz hw hu j
#print axioms a38_shared_rowblock_core_2

theorem a38_shared_rowblock_core_3 :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ (b : Fin 4) (j : Fin 4 × Fin 4), ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((3 : Fin 4), b) k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) j k) = if ((3 : Fin 4), b) = j then (1 : ℂ) else 0 := by
  intro z w u hz hw hu b j
  fin_cases b
  · exact a38_shared_row_core_30 z w u hz hw hu j
  · exact a38_shared_row_core_31 z w u hz hw hu j
  · exact a38_shared_row_core_32 z w u hz hw hu j
  · exact a38_shared_row_core_33 z w u hz hw hu j
#print axioms a38_shared_rowblock_core_3

theorem a38_shared_rows_core :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ i j : Fin 4 × Fin 4, ∑ k, (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) i k * star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) j k) = if i = j then (1 : ℂ) else 0 := by
  intro z w u hz hw hu i j
  obtain ⟨a, b⟩ := i
  fin_cases a
  · exact a38_shared_rowblock_core_0 z w u hz hw hu b j
  · exact a38_shared_rowblock_core_1 z w u hz hw hu b j
  · exact a38_shared_rowblock_core_2 z w u hz hw hu b j
  · exact a38_shared_rowblock_core_3 z w u hz hw hu b j
#print axioms a38_shared_rows_core

theorem a38_shared_unitary_core :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ := by
  intro z w u hz hw hu
  rw [Matrix.mem_unitaryGroup_iff]
  ext i j
  rw [Matrix.mul_apply, Matrix.one_apply]
  simp only [Matrix.star_apply]
  exact a38_shared_rows_core z w u hz hw hu i j
#print axioms a38_shared_unitary_core

theorem a38_shared_flat_core :
    ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → ∀ i j, ‖(Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) i j‖ = 1 / 4 := by
  intro z w u hz hw hu i j
  have hz1 := a35_shared_half z hz i.1 j.1
  have hw1 := a35_shared_half w hw i.2 j.2
  simp only [Matrix.of_apply] at hz1 hw1 ⊢
  rw [norm_mul, norm_mul, hz1, hw1, norm_pow, a35_shared_norm_of_unit u hu, one_pow]
  norm_num
#print axioms a38_shared_flat_core

theorem a38_shared_real_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ z w u : ℂ, star z * z = 1 → star w * w = 1 → star u * u = 1 → (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖(Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) i j‖ = 1 / 4) ∧ RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) i k) ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, z, -1, -z; 1, -1, 1, -1; 1, -z, -1, z] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, w, -1, -w; 1, -1, 1, -1; 1, -w, -1, w] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) i k) ∈ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) G ∧ featureVec G = x} := by
  intro Γ₀ hΓ₀ z w u hz hw hu
  have hU := a38_shared_unitary_core z w u hz hw hu
  have hF := a38_shared_flat_core z w u hz hw hu
  have hR := a35_shared_gram_realizable Γ₀ hΓ₀ _ hU hF
  exact ⟨hU, hF, hR, ⟨_, hR, rfl⟩⟩
#print axioms a38_shared_real_core

theorem a38_shared_excl_core_k1 :
    ∀ u : ℂ, star u * u = 1 → ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2))) → u = 1) ∧ ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2))ᵀ) → u = 1) := by
  intro u hu
  refine ⟨?_, ?_⟩
  · rintro ⟨X, Y, D, -, -, -, h⟩
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) := by
      rw [h]
      simp only [Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod])
      (try ring)
    simp (config := { decide := true }) [Matrix.of_apply] at key
    first
    | linear_combination (16 : ℂ) * key
    | exact key
    | (ring_nf at key; linear_combination (16 : ℂ) * key)
  · rintro ⟨X, Y, D, -, -, -, h⟩
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (1 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) := by
      rw [h]
      simp only [Matrix.transpose_apply, Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod])
      (try ring)
    simp (config := { decide := true }) [Matrix.of_apply] at key
    first
    | linear_combination (16 : ℂ) * key
    | exact key
    | (ring_nf at key; linear_combination (16 : ℂ) * key)
#print axioms a38_shared_excl_core_k1

theorem a38_shared_excl_core_k2 :
    ∀ u : ℂ, star u * u = 1 → ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2) (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2))) → u = 1) ∧ ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2) (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2))ᵀ) → u = 1) := by
  intro u hu
  refine ⟨?_, ?_⟩
  · rintro ⟨X, Y, D, -, -, -, h⟩
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (3 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (3 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) := by
      rw [h]
      simp only [Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod])
      (try ring)
    simp (config := { decide := true }) [Matrix.of_apply] at key
    first
    | linear_combination (-16 : ℂ) * key
    | exact key
    | (ring_nf at key; linear_combination (-16 : ℂ) * key)
  · rintro ⟨X, Y, D, -, -, -, h⟩
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (3 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (3 : Fin 4)) := by
      rw [h]
      simp only [Matrix.transpose_apply, Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod])
      (try ring)
    simp (config := { decide := true }) [Matrix.of_apply] at key
    first
    | linear_combination (-16 : ℂ) * key
    | exact key
    | (ring_nf at key; linear_combination (-16 : ℂ) * key)
#print axioms a38_shared_excl_core_k2

theorem a38_shared_excl_core_k3 :
    ∀ u : ℂ, star u * u = 1 → ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2) (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2))) → u = 1) ∧ ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2) (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2))ᵀ) → u = 1) := by
  intro u hu
  refine ⟨?_, ?_⟩
  · rintro ⟨X, Y, D, -, -, -, h⟩
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (2 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (2 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) := by
      rw [h]
      simp only [Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod])
      (try ring)
    simp (config := { decide := true }) [Matrix.of_apply] at key
    first
    | linear_combination (16 : ℂ) * key
    | exact key
    | (ring_nf at key; linear_combination (16 : ℂ) * key)
  · rintro ⟨X, Y, D, -, -, -, h⟩
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (1 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) := by
      rw [h]
      simp only [Matrix.transpose_apply, Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod])
      (try ring)
    simp (config := { decide := true }) [Matrix.of_apply] at key
    first
    | linear_combination (16 : ℂ) * key
    | exact key
    | (ring_nf at key; linear_combination (16 : ℂ) * key)
#print axioms a38_shared_excl_core_k3

theorem a38_shared_excl_core_k4 :
    ∀ u : ℂ, star u * u = 1 → ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2) (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2))) → u = 1) ∧ ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2) (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2))ᵀ) → u = 1) := by
  intro u hu
  refine ⟨?_, ?_⟩
  · rintro ⟨X, Y, D, -, -, -, h⟩
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (1 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) := by
      rw [h]
      simp only [Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod])
      (try ring)
    simp (config := { decide := true }) [Matrix.of_apply] at key
    first
    | linear_combination (16 : ℂ) * key
    | exact key
    | (ring_nf at key; linear_combination (16 : ℂ) * key)
  · rintro ⟨X, Y, D, -, -, -, h⟩
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) := by
      rw [h]
      simp only [Matrix.transpose_apply, Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod])
      (try ring)
    simp (config := { decide := true }) [Matrix.of_apply] at key
    first
    | linear_combination (16 : ℂ) * key
    | exact key
    | (ring_nf at key; linear_combination (16 : ℂ) * key)
#print axioms a38_shared_excl_core_k4

theorem a38_shared_excl_core_e1 :
    ∀ u : ℂ, star u * u = 1 → ((∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 8 × Fin 2 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2) (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2))) → u = 1) ∧ ((∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 8 × Fin 2 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2) (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2))ᵀ) → u = 1) := by
  intro u hu
  refine ⟨?_, ?_⟩
  · rintro ⟨X, Y, D, -, -, -, h⟩
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) := by
      rw [h]
      simp only [Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod])
      (try ring)
    simp (config := { decide := true }) [Matrix.of_apply] at key
    first
    | linear_combination (16 : ℂ) * key
    | exact key
    | (ring_nf at key; linear_combination (16 : ℂ) * key)
  · rintro ⟨X, Y, D, -, -, -, h⟩
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (3 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) := by
      rw [h]
      simp only [Matrix.transpose_apply, Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod])
      (try ring)
    simp (config := { decide := true }) [Matrix.of_apply] at key
    first
    | linear_combination (-16 : ℂ) * key
    | exact key
    | (ring_nf at key; linear_combination (-16 : ℂ) * key)
#print axioms a38_shared_excl_core_e1

theorem a38_shared_excl_core_e2 :
    ∀ u : ℂ, star u * u = 1 → ((∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 8 × Fin 2 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2) (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2))) → u = 1) ∧ ((∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 8 × Fin 2 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2) (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2))ᵀ) → u = 1) := by
  intro u hu
  refine ⟨?_, ?_⟩
  · rintro ⟨X, Y, D, -, -, -, h⟩
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (1 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) := by
      rw [h]
      simp only [Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod])
      (try ring)
    simp (config := { decide := true }) [Matrix.of_apply] at key
    first
    | linear_combination (16 : ℂ) * key
    | exact key
    | (ring_nf at key; linear_combination (16 : ℂ) * key)
  · rintro ⟨X, Y, D, -, -, -, h⟩
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) := by
      rw [h]
      simp only [Matrix.transpose_apply, Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod])
      (try ring)
    simp (config := { decide := true }) [Matrix.of_apply] at key
    first
    | linear_combination (16 : ℂ) * key
    | exact key
    | (ring_nf at key; linear_combination (16 : ℂ) * key)
#print axioms a38_shared_excl_core_e2

theorem a38_shared_excl_core_t1 :
    ∀ u : ℂ, star u * u = 1 → ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2)))) → u = 1) ∧ ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2)))ᵀ) → u = 1) := by
  intro u hu
  refine ⟨?_, ?_⟩
  · rintro ⟨X, Y, D, -, -, -, h⟩
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) := by
      rw [h]
      simp only [Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod])
      (try ring)
    simp (config := { decide := true }) [Matrix.of_apply] at key
    first
    | linear_combination (16 : ℂ) * key
    | exact key
    | (ring_nf at key; linear_combination (16 : ℂ) * key)
  · rintro ⟨X, Y, D, -, -, -, h⟩
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (1 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (0 : Fin 4)) := by
      rw [h]
      simp only [Matrix.transpose_apply, Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod])
      (try ring)
    simp (config := { decide := true }) [Matrix.of_apply] at key
    first
    | linear_combination (16 : ℂ) * key
    | exact key
    | (ring_nf at key; linear_combination (16 : ℂ) * key)
#print axioms a38_shared_excl_core_t1

theorem a38_shared_excl_core_t2 :
    ∀ u : ℂ, star u * u = 1 → ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2))) → u = 1) ∧ ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2))ᵀ) → u = 1) := by
  intro u hu
  refine ⟨?_, ?_⟩
  · rintro ⟨X, Y, D, -, -, -, h⟩
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (1 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (3 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (1 : Fin 4)) ((1 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (3 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) := by
      rw [h]
      simp only [Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod])
      (try ring)
    simp (config := { decide := true }) [Matrix.of_apply] at key
    have h2 : (3 / 5 + (4 / 5) * Complex.I) * (u - 1) = 0 := by
      first
      | linear_combination (16 : ℂ) * key
      | (ring_nf at key; linear_combination (16 : ℂ) * key)
    rcases mul_eq_zero.1 h2 with h3 | h3
    · exfalso
      revert h3
      first
      | (norm_num [Complex.ext_iff])
      | (simp [Complex.ext_iff]; norm_num)
    · linear_combination h3
  · rintro ⟨X, Y, D, -, -, -, h⟩
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((1 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4)) := by
      rw [h]
      simp only [Matrix.transpose_apply, Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod])
      (try ring)
    simp (config := { decide := true }) [Matrix.of_apply] at key
    first
    | linear_combination (16 : ℂ) * key
    | exact key
    | (ring_nf at key; linear_combination (16 : ℂ) * key)
#print axioms a38_shared_excl_core_t2

theorem a38_shared_excl_core_t3 :
    ∀ u : ℂ, star u * u = 1 → ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2) (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2))) → u = 1) ∧ ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2) (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2))ᵀ) → u = 1) := by
  intro u hu
  refine ⟨?_, ?_⟩
  · rintro ⟨X, Y, D, -, -, -, h⟩
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (2 : Fin 4)) ((1 : Fin 4), (1 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (2 : Fin 4)) ((0 : Fin 4), (0 : Fin 4)) := by
      rw [h]
      simp only [Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod])
      (try ring)
    simp (config := { decide := true }) [Matrix.of_apply] at key
    first
    | linear_combination (16 : ℂ) * key
    | exact key
    | (ring_nf at key; linear_combination (16 : ℂ) * key)
  · rintro ⟨X, Y, D, -, -, -, h⟩
    have key : (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (3 : Fin 4)) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((2 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (1 : Fin 4)) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) ((0 : Fin 4), (0 : Fin 4)) ((2 : Fin 4), (3 : Fin 4)) := by
      rw [h]
      simp only [Matrix.transpose_apply, Matrix.of_apply]
      (try simp (config := { decide := true }) [a36_shared_div, a36_shared_mod])
      (try ring)
    simp (config := { decide := true }) [Matrix.of_apply] at key
    first
    | linear_combination (-16 : ℂ) * key
    | exact key
    | (ring_nf at key; linear_combination (-16 : ℂ) * key)
#print axioms a38_shared_excl_core_t3

theorem a38_shared_base_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * 1 ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) ∧ ((Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖(Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c : Fin 4, ((Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖(Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (fun (_ : Fin 4) (_ : Fin 4) => (1 : ℂ)) j.1 i.2 * (fun (_ : Fin 4) => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c)) j.1 i.2 j.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2)) := by
  intro Γ₀ hΓ₀
  have hf : ∀ (t : ℂ), star t * t = 1 → ((Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, t, -1, -t; 1, -1, 1, -1; 1, -t, -1, t] a c) ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖(Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, t, -1, -t; 1, -1, 1, -1; 1, -t, -1, t] a c) a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) := by
    intro t ht
    refine ⟨(a35_shared_f4_flat Γ₀ hΓ₀ t ht).1, ?_⟩
    intro a c
    have h := a35_shared_half t ht a c
    simp only [Matrix.of_apply] at h ⊢
    rw [h]
    norm_num [Fintype.card_fin]
  have hA : ∀ p q : Fin 4, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] p q = p := by
    intro p q; fin_cases p <;> fin_cases q <;> rfl
  have hB : ∀ p q : Fin 4, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] p q = q := by
    intro p q; fin_cases p <;> fin_cases q <;> rfl
  refine ⟨?_, hf _ a36_shared_z_unit, fun _ => hf _ a36_shared_w_unit, ?_⟩
  · ext i j
    simp only [Matrix.of_apply, one_pow, mul_one]
  · ext i j
    simp only [Matrix.of_apply, hA, hB, mul_one]
#print axioms a38_shared_base_core

theorem a38_shared_pow_sub_one :
    ∀ (u : ℂ) (n : ℕ), ‖u‖ = 1 → ‖u ^ n - 1‖ ≤ n * ‖u - 1‖ := by
  intro u n hu
  induction n with
  | zero => simp
  | succ n ih =>
    have e : u ^ (n + 1) - 1 = u ^ n * (u - 1) + (u ^ n - 1) := by ring
    rw [e]
    calc ‖u ^ n * (u - 1) + (u ^ n - 1)‖ ≤ ‖u ^ n * (u - 1)‖ + ‖u ^ n - 1‖ := norm_add_le _ _
      _ = ‖u - 1‖ + ‖u ^ n - 1‖ := by rw [norm_mul, norm_pow, hu, one_pow, one_mul]
      _ ≤ ‖u - 1‖ + n * ‖u - 1‖ := by linarith
      _ = ((n + 1 : ℕ) : ℝ) * ‖u - 1‖ := by push_cast; ring
#print axioms a38_shared_pow_sub_one

theorem a38_shared_ew_le :
    ∀ i j : Fin 4 × Fin 4, ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) ≤ 3 := by
  intro i j
  split_ifs <;> norm_num
#print axioms a38_shared_ew_le

theorem a38_shared_cayley_core :
    ∀ t : ℝ, 0 < t → star ((1 + (t : ℂ) * Complex.I) / (1 - (t : ℂ) * Complex.I)) * ((1 + (t : ℂ) * Complex.I) / (1 - (t : ℂ) * Complex.I)) = 1 ∧ ((1 + (t : ℂ) * Complex.I) / (1 - (t : ℂ) * Complex.I)) ≠ 1 ∧ ‖((1 + (t : ℂ) * Complex.I) / (1 - (t : ℂ) * Complex.I)) - 1‖ ≤ 2 * t := by
  intro t ht
  have h1 : (1 : ℂ) - (t : ℂ) * Complex.I ≠ 0 := by
    intro h
    have h' := congrArg Complex.re h
    simp at h'
  have h2 : (1 : ℂ) + (t : ℂ) * Complex.I ≠ 0 := by
    intro h
    have h' := congrArg Complex.re h
    simp at h'
  refine ⟨?_, ?_, ?_⟩
  · have hc1 : (starRingEnd ℂ) (1 + (t : ℂ) * Complex.I) = 1 - (t : ℂ) * Complex.I := by
      rw [map_add, map_one, map_mul, Complex.conj_ofReal, Complex.conj_I]
      ring
    have hc2 : (starRingEnd ℂ) (1 - (t : ℂ) * Complex.I) = 1 + (t : ℂ) * Complex.I := by
      rw [map_sub, map_one, map_mul, Complex.conj_ofReal, Complex.conj_I]
      ring
    rw [Complex.star_def, map_div₀, hc1, hc2, div_mul_div_comm, div_eq_one_iff_eq (mul_ne_zero h2 h1)]
    ring
  · intro h
    rw [div_eq_iff h1] at h
    have h' := congrArg Complex.im h
    simp at h'
    linarith
  · have e : ((1 + (t : ℂ) * Complex.I) / (1 - (t : ℂ) * Complex.I)) - 1 = (2 * (t : ℂ) * Complex.I) / (1 - (t : ℂ) * Complex.I) := by
      field_simp
      ring
    have hI : ‖Complex.I‖ = 1 := by
      first
      | exact Complex.norm_I
      | simp
      | norm_num
    rw [e, norm_div, norm_mul, norm_mul, hI, mul_one]
    have hn : 1 ≤ ‖(1 : ℂ) - (t : ℂ) * Complex.I‖ := by
      have h : |((1 : ℂ) - (t : ℂ) * Complex.I).re| ≤ ‖(1 : ℂ) - (t : ℂ) * Complex.I‖ := by
        first
        | exact Complex.abs_re_le_norm _
        | (rw [Complex.norm_eq_abs]; exact Complex.abs_re_le_abs _)
      simpa using h
    have h2n : ‖(2 : ℂ)‖ = 2 := by norm_num
    have htn : ‖(t : ℂ)‖ = t := by rw [Complex.norm_real, Real.norm_eq_abs, abs_of_pos ht]
    rw [h2n, htn]
    have hpos : 0 < ‖(1 : ℂ) - (t : ℂ) * Complex.I‖ := by linarith
    first
    | (rw [div_le_iff hpos]; nlinarith)
    | (rw [div_le_iff₀ hpos]; nlinarith)
#print axioms a38_shared_cayley_core

theorem a38_shared_escape_core :
    ∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) → ∀ ε : ℝ, 0 < ε → ∃ u : ℂ, star u * u = 1 ∧ u ≠ 1 ∧ ‖u - 1‖ < ε ∧ (∀ i j, ‖(Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) i j - (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j‖ < ε) ∧ RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) i k) ∧ featureVec (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => star ((Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) i j) * (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) i k) ∈ {x : EuclideanSpace ℂ (((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4)) × ((Fin 4 × Fin 4) × (Fin 4 × Fin 4) × (Fin 4 × Fin 4))) | ∃ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, RealizableGram (Fin 1 × Fin 1) (Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) G ∧ featureVec G = x} ∧ ¬ (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2))) ∧ ¬ (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2, ![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2))ᵀ) ∧ ¬ (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2) (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2))) ∧ ¬ (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] i.1 i.2) (![![0, 1, 0, 1], ![2, 3, 2, 3], ![0, 1, 0, 1], ![2, 3, 2, 3]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2))ᵀ) ∧ ¬ (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2) (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2))) ∧ ¬ (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2, ![![0, 1, 2, 3], ![2, 3, 0, 1], ![0, 1, 2, 3], ![2, 3, 0, 1]] i.1 i.2) (![![0, 1, 0, 1], ![2, 3, 2, 3], ![1, 0, 1, 0], ![3, 2, 3, 2]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![2, 2, 3, 3], ![2, 2, 3, 3]] j.1 j.2))ᵀ) ∧ ¬ (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2) (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2))) ∧ ¬ (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 4) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 4) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] i.1 i.2) (![![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3], ![0, 1, 2, 3]] j.1 j.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![2, 2, 2, 2], ![3, 3, 3, 3]] j.1 j.2))ᵀ) ∧ ¬ (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 8 × Fin 2 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2) (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2))) ∧ ¬ (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 8 × Fin 2 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] i.1 i.2, ![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] i.1 i.2) (![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] j.1 j.2, ![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] j.1 j.2))ᵀ) ∧ ¬ (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 8 × Fin 2 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2) (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2))) ∧ ¬ (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 8 × Fin 2 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 1, 2, 3], ![0, 1, 2, 3], ![4, 5, 6, 7], ![4, 5, 6, 7]] i.1 i.2, ![![0, 0, 0, 0], ![1, 1, 1, 1], ![0, 0, 0, 0], ![1, 1, 1, 1]] i.1 i.2) (![![0, 1, 2, 3], ![4, 5, 6, 7], ![0, 1, 2, 3], ![4, 5, 6, 7]] j.1 j.2, ![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] j.1 j.2))ᵀ) ∧ ¬ (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2)))) ∧ ¬ (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (@Fin.divNat 2 2 i.1, @finProdFinEquiv 2 4 (@Fin.modNat 2 2 i.1, i.2)) (@Fin.modNat 2 2 j.1, @finProdFinEquiv 2 4 (@Fin.divNat 2 2 j.1, j.2)))ᵀ) ∧ ¬ (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2))) ∧ ¬ (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1], ![0, 0, 1, 1]] i.1 i.2, ![![0, 1, 0, 1], ![2, 3, 2, 3], ![4, 5, 4, 5], ![6, 7, 6, 7]] i.1 i.2) (![![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1], ![0, 1, 0, 1]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2))ᵀ) ∧ ¬ (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2) (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2))) ∧ ¬ (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), (X ∈ Matrix.unitaryGroup (Fin 2) ℂ ∧ ∀ a₁ c₁, ‖X a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 2) : ℝ)) ∧ (∀ c, (Y c ∈ Matrix.unitaryGroup (Fin 8) ℂ ∧ ∀ a₁ c₁, ‖Y c a₁ c₁‖ ^ 2 = 1 / (Fintype.card (Fin 8) : ℝ))) ∧ (∀ c b, ‖D c b‖ = 1) ∧ (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (3 / 5 + (4 / 5) * Complex.I), -1, -(3 / 5 + (4 / 5) * Complex.I); 1, -1, 1, -1; 1, -(3 / 5 + (4 / 5) * Complex.I), -1, (3 / 5 + (4 / 5) * Complex.I)] a c) i.1 j.1 * (Matrix.of fun a c : Fin 4 => (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, (5 / 13 + (12 / 13) * Complex.I), -1, -(5 / 13 + (12 / 13) * Complex.I); 1, -1, 1, -1; 1, -(5 / 13 + (12 / 13) * Complex.I), -1, (5 / 13 + (12 / 13) * Complex.I)] a c) i.2 j.2) i j * u ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0))) = (Matrix.of fun i j : Fin 4 × Fin 4 => (Matrix.of fun i j : Fin 2 × Fin 8 => X i.1 j.1 * D j.1 i.2 * Y j.1 i.2 j.2) (![![0, 0, 0, 0], ![0, 0, 0, 0], ![1, 1, 1, 1], ![1, 1, 1, 1]] i.1 i.2, ![![0, 1, 2, 3], ![4, 5, 6, 7], ![2, 3, 0, 1], ![6, 7, 4, 5]] i.1 i.2) (![![0, 1, 0, 1], ![1, 0, 1, 0], ![0, 1, 0, 1], ![1, 0, 1, 0]] j.1 j.2, ![![0, 0, 1, 1], ![2, 2, 3, 3], ![4, 4, 5, 5], ![6, 6, 7, 7]] j.1 j.2))ᵀ) := by
  intro Γ₀ hΓ₀ ε hε
  obtain ⟨hu, hne, hb⟩ := a38_shared_cayley_core (ε / 8) (by linarith)
  have hR := a38_shared_real_core Γ₀ hΓ₀ _ _ _ a36_shared_z_unit a36_shared_w_unit hu
  refine ⟨_, hu, hne, ?_, ?_, hR.2.2.1, hR.2.2.2, fun h => hne ((a38_shared_excl_core_k1 _ hu).1 h), fun h => hne ((a38_shared_excl_core_k1 _ hu).2 h), fun h => hne ((a38_shared_excl_core_k2 _ hu).1 h), fun h => hne ((a38_shared_excl_core_k2 _ hu).2 h), fun h => hne ((a38_shared_excl_core_k3 _ hu).1 h), fun h => hne ((a38_shared_excl_core_k3 _ hu).2 h), fun h => hne ((a38_shared_excl_core_k4 _ hu).1 h), fun h => hne ((a38_shared_excl_core_k4 _ hu).2 h), fun h => hne ((a38_shared_excl_core_e1 _ hu).1 h), fun h => hne ((a38_shared_excl_core_e1 _ hu).2 h), fun h => hne ((a38_shared_excl_core_e2 _ hu).1 h), fun h => hne ((a38_shared_excl_core_e2 _ hu).2 h), fun h => hne ((a38_shared_excl_core_t1 _ hu).1 h), fun h => hne ((a38_shared_excl_core_t1 _ hu).2 h), fun h => hne ((a38_shared_excl_core_t2 _ hu).1 h), fun h => hne ((a38_shared_excl_core_t2 _ hu).2 h), fun h => hne ((a38_shared_excl_core_t3 _ hu).1 h), fun h => hne ((a38_shared_excl_core_t3 _ hu).2 h)⟩
  · linarith
  · intro i j
    have hz1 := a35_shared_half _ a36_shared_z_unit i.1 j.1
    have hw1 := a35_shared_half _ a36_shared_w_unit i.2 j.2
    have hn1 := a35_shared_norm_of_unit _ hu
    have h1 := a38_shared_pow_sub_one ((1 + ((ε / 8 : ℝ) : ℂ) * Complex.I) / (1 - ((ε / 8 : ℝ) : ℂ) * Complex.I)) ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) hn1
    have h2 : ((((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) : ℕ) : ℝ) ≤ 3 := by exact_mod_cast a38_shared_ew_le i j
    have h3 : ((((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) : ℕ) : ℝ) * ‖((1 + ((ε / 8 : ℝ) : ℂ) * Complex.I) / (1 - ((ε / 8 : ℝ) : ℂ) * Complex.I)) - 1‖ ≤ 3 * ‖((1 + ((ε / 8 : ℝ) : ℂ) * Complex.I) / (1 - ((ε / 8 : ℝ) : ℂ) * Complex.I)) - 1‖ := mul_le_mul_of_nonneg_right h2 (norm_nonneg _)
    simp only [Matrix.of_apply] at hz1 hw1 ⊢
    rw [show ∀ x y : ℂ, x * y - x = x * (y - 1) from fun x y => by ring, norm_mul, norm_mul, hz1, hw1]
    linarith [norm_nonneg (((1 + ((ε / 8 : ℝ) : ℂ) * Complex.I) / (1 - ((ε / 8 : ℝ) : ℂ) * Complex.I)) ^ ((if i.1.val % 2 = 1 ∧ i.2 = 3 ∧ j.1.val % 2 = 1 then 1 else 0) + (if i.1 = 2 ∧ j.2 = 1 then 1 else 0) + (if (i.1.val + i.2.val) % 2 = 1 ∧ ((j.1 = 0 ∧ j.2 = 2) ∨ (j.1 = 2 ∧ j.2 = 0)) then 1 else 0)) - 1)]
#print axioms a38_shared_escape_core

theorem a38_shared_realizable :
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
  ∀ u : ℂ, star u * u = 1 →
    Hu u ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖Hu u i j‖ = 1 / 4)
    ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (Hu u)) ∧ featureVec (gram (Hu u)) ∈ N := by
  intro Γ₀ hΓ₀
  dsimp only
  intro u hu
  exact a38_shared_real_core Γ₀ hΓ₀ _ _ u a36_shared_z_unit a36_shared_w_unit hu
#print axioms a38_shared_realizable

theorem a38_shared_excl_k1 :
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
  ∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditak1 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditak1 X Y D)ᵀ) → u = 1) := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a38_shared_excl_core_k1
#print axioms a38_shared_excl_k1

theorem a38_shared_excl_k2 :
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
  ∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditak2 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditak2 X Y D)ᵀ) → u = 1) := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a38_shared_excl_core_k2
#print axioms a38_shared_excl_k2

theorem a38_shared_excl_k3 :
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
  ∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditak3 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditak3 X Y D)ᵀ) → u = 1) := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a38_shared_excl_core_k3
#print axioms a38_shared_excl_k3

theorem a38_shared_excl_k4 :
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
  ∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditak4 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditak4 X Y D)ᵀ) → u = 1) := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a38_shared_excl_core_k4
#print axioms a38_shared_excl_k4

theorem a38_shared_excl_e1 :
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
  ∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditae1 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditae1 X Y D)ᵀ) → u = 1) := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a38_shared_excl_core_e1
#print axioms a38_shared_excl_e1

theorem a38_shared_excl_e2 :
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
  ∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditae2 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditae2 X Y D)ᵀ) → u = 1) := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a38_shared_excl_core_e2
#print axioms a38_shared_excl_e2

theorem a38_shared_excl_t1 :
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
  ∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = dita28 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (dita28 X Y D)ᵀ) → u = 1) := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a38_shared_excl_core_t1
#print axioms a38_shared_excl_t1

theorem a38_shared_excl_t2 :
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
  ∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditat2 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditat2 X Y D)ᵀ) → u = 1) := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a38_shared_excl_core_t2
#print axioms a38_shared_excl_t2

theorem a38_shared_excl_t3 :
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
  ∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditat3 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditat3 X Y D)ᵀ) → u = 1) := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a38_shared_excl_core_t3
#print axioms a38_shared_excl_t3

theorem a38_c_local_escape :
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
  ∀ ε : ℝ, 0 < ε → ∃ u : ℂ, star u * u = 1 ∧ u ≠ 1 ∧ ‖u - 1‖ < ε ∧ (∀ i j, ‖Hu u i j - SIG i j‖ < ε)
    ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (Hu u)) ∧ featureVec (gram (Hu u)) ∈ N
    ∧ ¬ (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditak1 X Y D)
    ∧ ¬ (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditak1 X Y D)ᵀ)
    ∧ ¬ (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditak2 X Y D)
    ∧ ¬ (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditak2 X Y D)ᵀ)
    ∧ ¬ (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditak3 X Y D)
    ∧ ¬ (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditak3 X Y D)ᵀ)
    ∧ ¬ (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditak4 X Y D)
    ∧ ¬ (∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditak4 X Y D)ᵀ)
    ∧ ¬ (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditae1 X Y D)
    ∧ ¬ (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditae1 X Y D)ᵀ)
    ∧ ¬ (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditae2 X Y D)
    ∧ ¬ (∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditae2 X Y D)ᵀ)
    ∧ ¬ (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = dita28 X Y D)
    ∧ ¬ (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (dita28 X Y D)ᵀ)
    ∧ ¬ (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditat2 X Y D)
    ∧ ¬ (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditat2 X Y D)ᵀ)
    ∧ ¬ (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditat3 X Y D)
    ∧ ¬ (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditat3 X Y D)ᵀ) := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a38_shared_escape_core Γ₀ hΓ₀
#print axioms a38_c_local_escape

theorem a38_control_base :
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
  Hu 1 = SIG ∧ flg (F4 z) ∧ (∀ c : Fin 4, flg (F4 w)) ∧ SIG = ditak1 (F4 z) (fun _ => F4 w) (fun _ _ => (1 : ℂ)) := by
  intro Γ₀ hΓ₀
  dsimp only
  exact a38_shared_base_core Γ₀ hΓ₀
#print axioms a38_control_base

theorem a38_witness :
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
  (∀ u : ℂ, star u * u = 1 →
    Hu u ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖Hu u i j‖ = 1 / 4)
    ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (Hu u)) ∧ featureVec (gram (Hu u)) ∈ N)
  ∧ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditak1 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditak1 X Y D)ᵀ) → u = 1))
  ∧ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditak2 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditak2 X Y D)ᵀ) → u = 1))
  ∧ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditak3 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditak3 X Y D)ᵀ) → u = 1))
  ∧ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditak4 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditak4 X Y D)ᵀ) → u = 1))
  ∧ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditae1 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditae1 X Y D)ᵀ) → u = 1))
  ∧ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditae2 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditae2 X Y D)ᵀ) → u = 1))
  ∧ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = dita28 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (dita28 X Y D)ᵀ) → u = 1))
  ∧ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditat2 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditat2 X Y D)ᵀ) → u = 1))
  ∧ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditat3 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditat3 X Y D)ᵀ) → u = 1)) := by
  intro Γ₀ hΓ₀
  dsimp only
  exact ⟨fun u hu => a38_shared_real_core Γ₀ hΓ₀ _ _ u a36_shared_z_unit a36_shared_w_unit hu, a38_shared_excl_core_k1, a38_shared_excl_core_k2, a38_shared_excl_core_k3, a38_shared_excl_core_k4, a38_shared_excl_core_e1, a38_shared_excl_core_e2, a38_shared_excl_core_t1, a38_shared_excl_core_t2, a38_shared_excl_core_t3⟩
#print axioms a38_witness

theorem a38_c_exclusive :
    (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
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
  ¬ (∀ u : ℂ, star u * u = 1 →
    Hu u ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖Hu u i j‖ = 1 / 4)
    ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (Hu u)) ∧ featureVec (gram (Hu u)) ∈ N)
  ∨ ¬ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditak1 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditak1 X Y D)ᵀ) → u = 1))
  ∨ ¬ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditak2 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditak2 X Y D)ᵀ) → u = 1))
  ∨ ¬ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditak3 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditak3 X Y D)ᵀ) → u = 1))
  ∨ ¬ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditak4 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditak4 X Y D)ᵀ) → u = 1))
  ∨ ¬ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditae1 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditae1 X Y D)ᵀ) → u = 1))
  ∨ ¬ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditae2 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditae2 X Y D)ᵀ) → u = 1))
  ∨ ¬ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = dita28 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (dita28 X Y D)ᵀ) → u = 1))
  ∨ ¬ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditat2 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditat2 X Y D)ᵀ) → u = 1))
  ∨ ¬ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditat3 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditat3 X Y D)ᵀ) → u = 1))) → ¬ (∀ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ), Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)) →
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
  (∀ u : ℂ, star u * u = 1 →
    Hu u ∈ Matrix.unitaryGroup (Fin 4 × Fin 4) ℂ ∧ (∀ i j, ‖Hu u i j‖ = 1 / 4)
    ∧ RealizableGram (Fin 1 × Fin 1) Γ (gram (Hu u)) ∧ featureVec (gram (Hu u)) ∈ N)
  ∧ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditak1 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditak1 X Y D)ᵀ) → u = 1))
  ∧ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditak2 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditak2 X Y D)ᵀ) → u = 1))
  ∧ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditak3 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditak3 X Y D)ᵀ) → u = 1))
  ∧ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditak4 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 4) (Fin 4) ℂ) (Y : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (D : Fin 4 → Fin 4 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditak4 X Y D)ᵀ) → u = 1))
  ∧ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditae1 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditae1 X Y D)ᵀ) → u = 1))
  ∧ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditae2 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 8) (Fin 8) ℂ) (Y : Fin 8 → Matrix (Fin 2) (Fin 2) ℂ) (D : Fin 8 → Fin 2 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditae2 X Y D)ᵀ) → u = 1))
  ∧ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = dita28 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (dita28 X Y D)ᵀ) → u = 1))
  ∧ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditat2 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditat2 X Y D)ᵀ) → u = 1))
  ∧ (∀ u : ℂ, star u * u = 1 →
    ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditat3 X Y D) → u = 1)
    ∧ ((∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = (ditat3 X Y D)ᵀ) → u = 1))) := by
  intro hN hR
  have h := hN _ rfl
  have r := hR _ rfl
  dsimp only at h r
  rcases h with h | h | h | h | h | h | h | h | h | h
  · exact h r.1
  · exact h r.2.1
  · exact h r.2.2.1
  · exact h r.2.2.2.1
  · exact h r.2.2.2.2.1
  · exact h r.2.2.2.2.2.1
  · exact h r.2.2.2.2.2.2.1
  · exact h r.2.2.2.2.2.2.2.1
  · exact h r.2.2.2.2.2.2.2.2.1
  · exact h r.2.2.2.2.2.2.2.2.2
#print axioms a38_c_exclusive
end DitaLocalEscape
end OIBridge
