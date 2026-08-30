/-
  OIBridge/TwoByTwoNoGo.lean — phase three, round 4: the exact (2,2) one-slot no-go.

  THE STATEMENT THIS FILE PROVES, at one explicit rational witness carrier:

      preparation feasible  +  global intervention feasible
          ⇏  visible-local CPTP coherent lift.

  The carrier is the (2,2) ancilla-marginal shape with the exact rational orthogonal
  eigenbasis `V0 = G02(3/5)·G23(5/13)·G01(3/5)` (Givens rotations with Pythagorean
  angles), spectrum `E0 = (0,1,3,7)` (all gap differences distinct, decided over ℚ),
  stationary preparation `ρ0 = V0·diag(1/2,1/4,1/8,1/8)·V0ᵀ` — preparation-feasible by
  construction — and the classical transposition action, whose branch table `tp0` IS
  globally reachable: the transposed marginal lies in the spectral-readout polytope, and
  probe F16 exhibits the global witness exactly. The three theorems:

    * `twoByTwo_affine_rigidity` — trace preservation + stationarity of the intervened
      state + the block readout determine the visible Choi operator UNIQUELY: sixteen
      exact `linear_combination` certificates, one per entry, over the eighteen scalar
      constraint equations. No positivity enters — the affine constraints alone are rigid
      at this shape.
    * `twoByTwo_nonCP` — the unique candidate `J0` is not positive semidefinite: the
      explicit rational vector `v0 = (1,−1,−1,−1)` gives `v0† J0 v0 = −449600/76287 < 0`.
      A symbolic certificate — no floating eigenvalue enters.
    * `twoByTwo_no_local_lift` — assembled against the named predicate: NO visible-local
      CPTP instrument realizes `TwoTimeCoherentLift V0 E0 rho0 tp0`. The proof runs the
      round-3 reduction (`two_time_forces_stationary`, with the gap condition decided
      over ℚ and readout completeness checked entrywise), converts the Kraus family to
      its Choi matrix (`krausChoi_psd`, `krausChoi_tp`, `chApply_krausChoi`), and
      collides rigidity with non-positivity.

  Probe F16 recomputes the unique solution, the certificates, the negativity witness and
  the global-feasibility witness independently in exact rational arithmetic.
-/
import OIBridge.CoherentLift

/- This file is a machine-generated certificate: the entry-evaluation lemmas and the
eighteen constraint expansions share uniform simp sets, so most invocations carry
arguments some sibling needs and they do not. The unused-simp-args linter would emit
hundreds of cosmetic warnings on that shared structure; nothing else is suppressed. -/
set_option linter.unusedSimpArgs false

namespace OIBridge
namespace TwoByTwoNoGo

open Complex Matrix CoherentLift
open scoped ComplexOrder

/-- The eigenvector table: visible index, ancilla index, mode — the exact carrier
`G02(3/5)·G23(5/13)·G01(3/5)`, rows the composite configurations `s = 2·i + x`. -/
noncomputable def Vtab : Fin 2 → Fin 2 → Fin 4 → ℂ :=
  ![![![((9 : ℂ) / 25), (-(12 : ℂ) / 25), (-(4 : ℂ) / 13), ((48 : ℂ) / 65)],
     ![((4 : ℂ) / 5), ((3 : ℂ) / 5), (0 : ℂ), (0 : ℂ)]],
   ![![((12 : ℂ) / 25), (-(16 : ℂ) / 25), ((3 : ℂ) / 13), (-(36 : ℂ) / 65)],
     ![(0 : ℂ), (0 : ℂ), ((12 : ℂ) / 13), ((5 : ℂ) / 13)]]]

/-- The eigenvector matrix on the composite carrier. -/
noncomputable def V0 : Matrix (Fin 2 × Fin 2) (Fin 4) ℂ := fun p a => Vtab p.1 p.2 a

/-- The spectrum, over ℤ so the gap condition is decidable by kernel evaluation. -/
def E0q : Fin 4 → ℤ := ![0, 1, 3, 7]

/-- The spectrum over ℝ. -/
noncomputable def E0 : Fin 4 → ℝ := fun a => ((E0q a : ℤ) : ℝ)

/-- The stationary preparation `V0·diag(1/2,1/4,1/8,1/8)·V0ᵀ`, tabulated exactly. -/
noncomputable def rhotab : Fin 2 → Fin 2 → Fin 2 → Fin 2 → ℂ :=
  ![![![![((253 : ℂ) / 1250), ((9 : ℂ) / 125)], ![((129 : ℂ) / 1250), (0 : ℂ)]],
      ![![((9 : ℂ) / 125), ((41 : ℂ) / 100)], ![((12 : ℂ) / 125), (0 : ℂ)]]],
     ![![![((129 : ℂ) / 1250), ((12 : ℂ) / 125)], ![((1313 : ℂ) / 5000), (0 : ℂ)]],
      ![![(0 : ℂ), (0 : ℂ)], ![(0 : ℂ), ((1 : ℂ) / 8)]]]]

/-- The preparation as a matrix. -/
noncomputable def rho0 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ :=
  fun p q => rhotab p.1 p.2 q.1 q.2

/-- The classical branch table of the transposition action: the σ-permuted marginal. -/
noncomputable def tp0 : Fin 2 → ℝ := ![969/2500, 1531/2500]

/-- The unique Choi candidate the affine constraints force (index `(out, in)`). -/
noncomputable def J0tab : Fin 2 → Fin 2 → Fin 2 → Fin 2 → ℂ :=
  ![![![![((6599 : ℂ) / 76287), ((17422 : ℂ) / 25429)], ![((28100 : ℂ) / 76287), ((18404 : ℂ) / 25429)]],
      ![![((17422 : ℂ) / 25429), ((114086 : ℂ) / 228861)], ![(-(7025 : ℂ) / 25429), (-(92168 : ℂ) / 76287)]]],
     ![![![((28100 : ℂ) / 76287), (-(7025 : ℂ) / 25429)], ![((69688 : ℂ) / 76287), (-(17422 : ℂ) / 25429)]],
      ![![((18404 : ℂ) / 25429), (-(92168 : ℂ) / 76287)], ![(-(17422 : ℂ) / 25429), ((114775 : ℂ) / 228861)]]]]

/-- The unique Choi candidate. -/
noncomputable def J0 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ :=
  fun s t => J0tab s.1 s.2 t.1 t.2

/-- The negativity witness. -/
noncomputable def v0 : Fin 2 × Fin 2 → ℂ := fun s => ![![1, -1], ![-1, -1]] s.1 s.2

/-! Entry evaluation lemmas, one per table entry, so every later expansion fires on
closed terms and never depends on vector-notation matching. -/

lemma V_e000 : Vtab 0 0 0 = ((9 : ℂ) / 25) := by
  simp only [Vtab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma V_e001 : Vtab 0 0 1 = (-(12 : ℂ) / 25) := by
  simp only [Vtab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma V_e002 : Vtab 0 0 2 = (-(4 : ℂ) / 13) := by
  simp only [Vtab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma V_e003 : Vtab 0 0 3 = ((48 : ℂ) / 65) := by
  simp only [Vtab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma V_e010 : Vtab 0 1 0 = ((4 : ℂ) / 5) := by
  simp only [Vtab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma V_e011 : Vtab 0 1 1 = ((3 : ℂ) / 5) := by
  simp only [Vtab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma V_e012 : Vtab 0 1 2 = (0 : ℂ) := by
  simp only [Vtab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma V_e013 : Vtab 0 1 3 = (0 : ℂ) := by
  simp only [Vtab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma V_e100 : Vtab 1 0 0 = ((12 : ℂ) / 25) := by
  simp only [Vtab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma V_e101 : Vtab 1 0 1 = (-(16 : ℂ) / 25) := by
  simp only [Vtab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma V_e102 : Vtab 1 0 2 = ((3 : ℂ) / 13) := by
  simp only [Vtab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma V_e103 : Vtab 1 0 3 = (-(36 : ℂ) / 65) := by
  simp only [Vtab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma V_e110 : Vtab 1 1 0 = (0 : ℂ) := by
  simp only [Vtab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma V_e111 : Vtab 1 1 1 = (0 : ℂ) := by
  simp only [Vtab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma V_e112 : Vtab 1 1 2 = ((12 : ℂ) / 13) := by
  simp only [Vtab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma V_e113 : Vtab 1 1 3 = ((5 : ℂ) / 13) := by
  simp only [Vtab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma R_e0000 : rhotab 0 0 0 0 = ((253 : ℂ) / 1250) := by
  simp only [rhotab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma R_e0001 : rhotab 0 0 0 1 = ((9 : ℂ) / 125) := by
  simp only [rhotab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma R_e0010 : rhotab 0 0 1 0 = ((129 : ℂ) / 1250) := by
  simp only [rhotab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma R_e0011 : rhotab 0 0 1 1 = (0 : ℂ) := by
  simp only [rhotab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma R_e0100 : rhotab 0 1 0 0 = ((9 : ℂ) / 125) := by
  simp only [rhotab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma R_e0101 : rhotab 0 1 0 1 = ((41 : ℂ) / 100) := by
  simp only [rhotab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma R_e0110 : rhotab 0 1 1 0 = ((12 : ℂ) / 125) := by
  simp only [rhotab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma R_e0111 : rhotab 0 1 1 1 = (0 : ℂ) := by
  simp only [rhotab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma R_e1000 : rhotab 1 0 0 0 = ((129 : ℂ) / 1250) := by
  simp only [rhotab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma R_e1001 : rhotab 1 0 0 1 = ((12 : ℂ) / 125) := by
  simp only [rhotab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma R_e1010 : rhotab 1 0 1 0 = ((1313 : ℂ) / 5000) := by
  simp only [rhotab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma R_e1011 : rhotab 1 0 1 1 = (0 : ℂ) := by
  simp only [rhotab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma R_e1100 : rhotab 1 1 0 0 = (0 : ℂ) := by
  simp only [rhotab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma R_e1101 : rhotab 1 1 0 1 = (0 : ℂ) := by
  simp only [rhotab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma R_e1110 : rhotab 1 1 1 0 = (0 : ℂ) := by
  simp only [rhotab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma R_e1111 : rhotab 1 1 1 1 = ((1 : ℂ) / 8) := by
  simp only [rhotab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma J_e0000 : J0tab 0 0 0 0 = ((6599 : ℂ) / 76287) := by
  simp only [J0tab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma J_e0001 : J0tab 0 0 0 1 = ((17422 : ℂ) / 25429) := by
  simp only [J0tab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma J_e0010 : J0tab 0 0 1 0 = ((28100 : ℂ) / 76287) := by
  simp only [J0tab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma J_e0011 : J0tab 0 0 1 1 = ((18404 : ℂ) / 25429) := by
  simp only [J0tab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma J_e0100 : J0tab 0 1 0 0 = ((17422 : ℂ) / 25429) := by
  simp only [J0tab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma J_e0101 : J0tab 0 1 0 1 = ((114086 : ℂ) / 228861) := by
  simp only [J0tab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma J_e0110 : J0tab 0 1 1 0 = (-(7025 : ℂ) / 25429) := by
  simp only [J0tab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma J_e0111 : J0tab 0 1 1 1 = (-(92168 : ℂ) / 76287) := by
  simp only [J0tab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma J_e1000 : J0tab 1 0 0 0 = ((28100 : ℂ) / 76287) := by
  simp only [J0tab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma J_e1001 : J0tab 1 0 0 1 = (-(7025 : ℂ) / 25429) := by
  simp only [J0tab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma J_e1010 : J0tab 1 0 1 0 = ((69688 : ℂ) / 76287) := by
  simp only [J0tab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma J_e1011 : J0tab 1 0 1 1 = (-(17422 : ℂ) / 25429) := by
  simp only [J0tab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma J_e1100 : J0tab 1 1 0 0 = ((18404 : ℂ) / 25429) := by
  simp only [J0tab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma J_e1101 : J0tab 1 1 0 1 = (-(92168 : ℂ) / 76287) := by
  simp only [J0tab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma J_e1110 : J0tab 1 1 1 0 = (-(17422 : ℂ) / 25429) := by
  simp only [J0tab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

lemma J_e1111 : J0tab 1 1 1 1 = ((114775 : ℂ) / 228861) := by
  simp only [J0tab, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]

set_option maxHeartbeats 4000000 in
/-- **`twoByTwo_affine_rigidity`.** Trace preservation, stationarity of the intervened
state, and the block readout determine the visible Choi operator uniquely at this
carrier: the affine constraint system is RIGID — its solution set is the single point
`J0`, before any positivity is imposed. Sixteen exact rational certificates. -/
theorem twoByTwo_affine_rigidity (J : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
    (hTP : ∀ i i' : Fin 2, ∑ o : Fin 2, J (o, i) (o, i') = if i = i' then 1 else 0)
    (hW : ∀ a b : Fin 4, a ≠ b →
      (V0ᴴ * CoherentLift.chApply J rho0 * V0 : Matrix (Fin 4) (Fin 4) ℂ) a b = 0)
    (hread : ∀ j : Fin 2, Matrix.trace (CoherentLift.readProj
      (Prod.fst : Fin 2 × Fin 2 → Fin 2) j * CoherentLift.chApply J rho0)
      = ((tp0 j : ℝ) : ℂ)) :
    J = J0 := by
  have eTP00 := hTP 0 0
  simp only [Fin.sum_univ_two] at eTP00
  norm_num at eTP00
  have eTP01 := hTP 0 1
  simp only [Fin.sum_univ_two] at eTP01
  norm_num at eTP01
  have eTP10 := hTP 1 0
  simp only [Fin.sum_univ_two] at eTP10
  norm_num at eTP10
  have eTP11 := hTP 1 1
  simp only [Fin.sum_univ_two] at eTP11
  norm_num at eTP11
  have eW01 := hW 0 1 (by decide)
  simp only [CoherentLift.chApply, V0, rho0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type, Fin.sum_univ_four, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, R_e0000, R_e0001, R_e0010, R_e0011, R_e0100, R_e0101, R_e0110, R_e0111, R_e1000, R_e1001, R_e1010, R_e1011, R_e1100, R_e1101, R_e1110, R_e1111, star_div₀, star_ofNat, star_neg, star_zero, star_one] at eW01
  have eW02 := hW 0 2 (by decide)
  simp only [CoherentLift.chApply, V0, rho0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type, Fin.sum_univ_four, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, R_e0000, R_e0001, R_e0010, R_e0011, R_e0100, R_e0101, R_e0110, R_e0111, R_e1000, R_e1001, R_e1010, R_e1011, R_e1100, R_e1101, R_e1110, R_e1111, star_div₀, star_ofNat, star_neg, star_zero, star_one] at eW02
  have eW03 := hW 0 3 (by decide)
  simp only [CoherentLift.chApply, V0, rho0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type, Fin.sum_univ_four, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, R_e0000, R_e0001, R_e0010, R_e0011, R_e0100, R_e0101, R_e0110, R_e0111, R_e1000, R_e1001, R_e1010, R_e1011, R_e1100, R_e1101, R_e1110, R_e1111, star_div₀, star_ofNat, star_neg, star_zero, star_one] at eW03
  have eW10 := hW 1 0 (by decide)
  simp only [CoherentLift.chApply, V0, rho0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type, Fin.sum_univ_four, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, R_e0000, R_e0001, R_e0010, R_e0011, R_e0100, R_e0101, R_e0110, R_e0111, R_e1000, R_e1001, R_e1010, R_e1011, R_e1100, R_e1101, R_e1110, R_e1111, star_div₀, star_ofNat, star_neg, star_zero, star_one] at eW10
  have eW12 := hW 1 2 (by decide)
  simp only [CoherentLift.chApply, V0, rho0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type, Fin.sum_univ_four, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, R_e0000, R_e0001, R_e0010, R_e0011, R_e0100, R_e0101, R_e0110, R_e0111, R_e1000, R_e1001, R_e1010, R_e1011, R_e1100, R_e1101, R_e1110, R_e1111, star_div₀, star_ofNat, star_neg, star_zero, star_one] at eW12
  have eW13 := hW 1 3 (by decide)
  simp only [CoherentLift.chApply, V0, rho0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type, Fin.sum_univ_four, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, R_e0000, R_e0001, R_e0010, R_e0011, R_e0100, R_e0101, R_e0110, R_e0111, R_e1000, R_e1001, R_e1010, R_e1011, R_e1100, R_e1101, R_e1110, R_e1111, star_div₀, star_ofNat, star_neg, star_zero, star_one] at eW13
  have eW20 := hW 2 0 (by decide)
  simp only [CoherentLift.chApply, V0, rho0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type, Fin.sum_univ_four, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, R_e0000, R_e0001, R_e0010, R_e0011, R_e0100, R_e0101, R_e0110, R_e0111, R_e1000, R_e1001, R_e1010, R_e1011, R_e1100, R_e1101, R_e1110, R_e1111, star_div₀, star_ofNat, star_neg, star_zero, star_one] at eW20
  have eW21 := hW 2 1 (by decide)
  simp only [CoherentLift.chApply, V0, rho0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type, Fin.sum_univ_four, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, R_e0000, R_e0001, R_e0010, R_e0011, R_e0100, R_e0101, R_e0110, R_e0111, R_e1000, R_e1001, R_e1010, R_e1011, R_e1100, R_e1101, R_e1110, R_e1111, star_div₀, star_ofNat, star_neg, star_zero, star_one] at eW21
  have eW23 := hW 2 3 (by decide)
  simp only [CoherentLift.chApply, V0, rho0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type, Fin.sum_univ_four, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, R_e0000, R_e0001, R_e0010, R_e0011, R_e0100, R_e0101, R_e0110, R_e0111, R_e1000, R_e1001, R_e1010, R_e1011, R_e1100, R_e1101, R_e1110, R_e1111, star_div₀, star_ofNat, star_neg, star_zero, star_one] at eW23
  have eW30 := hW 3 0 (by decide)
  simp only [CoherentLift.chApply, V0, rho0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type, Fin.sum_univ_four, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, R_e0000, R_e0001, R_e0010, R_e0011, R_e0100, R_e0101, R_e0110, R_e0111, R_e1000, R_e1001, R_e1010, R_e1011, R_e1100, R_e1101, R_e1110, R_e1111, star_div₀, star_ofNat, star_neg, star_zero, star_one] at eW30
  have eW31 := hW 3 1 (by decide)
  simp only [CoherentLift.chApply, V0, rho0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type, Fin.sum_univ_four, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, R_e0000, R_e0001, R_e0010, R_e0011, R_e0100, R_e0101, R_e0110, R_e0111, R_e1000, R_e1001, R_e1010, R_e1011, R_e1100, R_e1101, R_e1110, R_e1111, star_div₀, star_ofNat, star_neg, star_zero, star_one] at eW31
  have eW32 := hW 3 2 (by decide)
  simp only [CoherentLift.chApply, V0, rho0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fintype.sum_prod_type, Fin.sum_univ_four, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, R_e0000, R_e0001, R_e0010, R_e0011, R_e0100, R_e0101, R_e0110, R_e0111, R_e1000, R_e1001, R_e1010, R_e1011, R_e1100, R_e1101, R_e1110, R_e1111, star_div₀, star_ofNat, star_neg, star_zero, star_one] at eW32
  have eR0 := hread 0
  simp only [CoherentLift.chApply, CoherentLift.readProj, V0, rho0, tp0, Matrix.trace, Matrix.diag_apply, Matrix.diagonal_mul, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two, R_e0000, R_e0001, R_e0010, R_e0011, R_e0100, R_e0101, R_e0110, R_e0111, R_e1000, R_e1001, R_e1010, R_e1011, R_e1100, R_e1101, R_e1110, R_e1111, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons] at eR0
  norm_num at eR0
  have eR1 := hread 1
  simp only [CoherentLift.chApply, CoherentLift.readProj, V0, rho0, tp0, Matrix.trace, Matrix.diag_apply, Matrix.diagonal_mul, Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_two, R_e0000, R_e0001, R_e0010, R_e0011, R_e0100, R_e0101, R_e0110, R_e0111, R_e1000, R_e1001, R_e1010, R_e1011, R_e1100, R_e1101, R_e1110, R_e1111, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons] at eR1
  norm_num at eR1
  ext p q
  fin_cases p <;> fin_cases q
  · show J ((0 : Fin 2), (0 : Fin 2)) ((0 : Fin 2), (0 : Fin 2)) = J0tab 0 0 0 0
    rw [J_e0000]
    linear_combination (-(26830679 : ℂ) / 40050675) * eTP00
      + (-(376489 : ℂ) / 3814350) * eTP01
      + (-(79480357 : ℂ) / 240304050) * eTP10
      + (-(32786746 : ℂ) / 40050675) * eTP11
      + (-(7175 : ℂ) / 25429) * eW01
      + ((918800 : ℂ) / 991731) * eW02
      + (-(111041785 : ℂ) / 62479053) * eW03
      + (-(33305075 : ℂ) / 19224324) * eW10
      + (-(53517325 : ℂ) / 62479053) * eW12
      + ((39114520 : ℂ) / 26776737) * eW13
      + (-(19801640 : ℂ) / 26776737) * eW20
      + ((7820380 : ℂ) / 62479053) * eW21
      + ((27880775 : ℂ) / 19224324) * eW23
      + (-(49704080 : ℂ) / 62479053) * eW30
      + ((3100880 : ℂ) / 991731) * eW31
      + ((310000 : ℂ) / 76287) * eR0
  · show J ((0 : Fin 2), (0 : Fin 2)) ((0 : Fin 2), (1 : Fin 2)) = J0tab 0 0 0 1
    rw [J_e0001]
    linear_combination ((8519486 : ℂ) / 13350225) * eTP00
      + ((1429763 : ℂ) / 635725) * eTP01
      + ((16467119 : ℂ) / 40050675) * eTP10
      + ((16397539 : ℂ) / 13350225) * eTP11
      + ((3264725 : ℂ) / 406864) * eW01
      + ((2489525 : ℂ) / 991731) * eW02
      + (-(51864110 : ℂ) / 20826351) * eW03
      + ((71448575 : ℂ) / 25632432) * eW10
      + ((15373825 : ℂ) / 83305404) * eW12
      + (-(46014955 : ℂ) / 8925579) * eW13
      + (-(72480895 : ℂ) / 8925579) * eW20
      + ((823326485 : ℂ) / 83305404) * eW21
      + ((36803975 : ℂ) / 3204054) * eW23
      + (-(18088780 : ℂ) / 20826351) * eW30
      + ((1131955 : ℂ) / 330577) * eW31
      + (-(77500 : ℂ) / 25429) * eR0
  · show J ((0 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (0 : Fin 2)) = J0tab 0 0 1 0
    rw [J_e0010]
    linear_combination ((434905 : ℂ) / 1602027) * eTP00
      + ((94390 : ℂ) / 76287) * eTP01
      + ((384970 : ℂ) / 4806081) * eTP10
      + ((1172645 : ℂ) / 1602027) * eTP11
      + ((180000 : ℂ) / 25429) * eW01
      + ((5870720 : ℂ) / 991731) * eW02
      + (-(875274025 : ℂ) / 249916212) * eW03
      + ((4339375 : ℂ) / 4806081) * eW10
      + ((20850035 : ℂ) / 19224324) * eW12
      + (-(11717600 : ℂ) / 2059749) * eW13
      + (-(125696000 : ℂ) / 26776737) * eW20
      + ((285832000 : ℂ) / 62479053) * eW21
      + ((29680625 : ℂ) / 4806081) * eW23
      + ((20056000 : ℂ) / 62479053) * eW30
      + ((3584000 : ℂ) / 991731) * eW31
      + (-(125000 : ℂ) / 76287) * eR0
  · show J ((0 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (1 : Fin 2)) = J0tab 0 0 1 1
    rw [J_e0011]
    linear_combination (-(241921 : ℂ) / 10680180) * eTP00
      + ((250733 : ℂ) / 127145) * eTP01
      + ((1260674 : ℂ) / 8010135) * eTP10
      + ((2884351 : ℂ) / 10680180) * eTP11
      + ((1558625 : ℂ) / 305148) * eW01
      + ((1710945 : ℂ) / 330577) * eW02
      + (-(5095455175 : ℂ) / 333221616) * eW03
      + ((8375125 : ℂ) / 6408108) * eW10
      + ((860540045 : ℂ) / 333221616) * eW12
      + (-(96055775 : ℂ) / 8925579) * eW13
      + (-(71817740 : ℂ) / 8925579) * eW20
      + ((205590955 : ℂ) / 20826351) * eW21
      + ((19439225 : ℂ) / 1602027) * eW23
      + (-(45700400 : ℂ) / 20826351) * eW30
      + ((1646900 : ℂ) / 330577) * eW31
      + ((31250 : ℂ) / 25429) * eR0
  · show J ((0 : Fin 2), (1 : Fin 2)) ((0 : Fin 2), (0 : Fin 2)) = J0tab 0 1 0 0
    rw [J_e0100]
    linear_combination ((8519486 : ℂ) / 13350225) * eTP00
      + ((1429763 : ℂ) / 635725) * eTP01
      + ((16467119 : ℂ) / 40050675) * eTP10
      + ((16397539 : ℂ) / 13350225) * eTP11
      + ((5807625 : ℂ) / 406864) * eW01
      + ((1677475 : ℂ) / 330577) * eW02
      + (-(180026270 : ℂ) / 20826351) * eW03
      + (-(88754125 : ℂ) / 25632432) * eW10
      + ((175576525 : ℂ) / 83305404) * eW12
      + (-(87209935 : ℂ) / 8925579) * eW13
      + (-(95366995 : ℂ) / 8925579) * eW20
      + ((663123785 : ℂ) / 83305404) * eW21
      + ((36803975 : ℂ) / 3204054) * eW23
      + ((110073380 : ℂ) / 20826351) * eW30
      + ((2657695 : ℂ) / 330577) * eW31
      + (-(77500 : ℂ) / 25429) * eR0
  · show J ((0 : Fin 2), (1 : Fin 2)) ((0 : Fin 2), (1 : Fin 2)) = J0tab 0 1 0 1
    rw [J_e0101]
    linear_combination ((86345527 : ℂ) / 120152025) * eTP00
      + (-(11919943 : ℂ) / 11443050) * eTP01
      + ((218892341 : ℂ) / 720912150) * eTP10
      + ((76820798 : ℂ) / 120152025) * eTP11
      + (-(1675625 : ℂ) / 305148) * eW01
      + (-(10363300 : ℂ) / 2975193) * eW02
      + ((1082006585 : ℂ) / 187437159) * eW03
      + ((84115625 : ℂ) / 28836486) * eW10
      + ((139275950 : ℂ) / 187437159) * eW12
      + ((133844380 : ℂ) / 80330211) * eW13
      + ((496069900 : ℂ) / 80330211) * eW20
      + (-(927557675 : ℂ) / 187437159) * eW21
      + (-(484924375 : ℂ) / 57672972) * eW23
      + ((15172960 : ℂ) / 187437159) * eW30
      + (-(23779060 : ℂ) / 2975193) * eW31
      + (-(507500 : ℂ) / 228861) * eR0
  · show J ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (0 : Fin 2)) = J0tab 0 1 1 0
    rw [J_e0110]
    linear_combination (-(10922101 : ℂ) / 10680180) * eTP00
      + ((250733 : ℂ) / 127145) * eTP01
      + (-(9419506 : ℂ) / 8010135) * eTP10
      + ((2884351 : ℂ) / 10680180) * eTP11
      + ((1367175 : ℂ) / 101716) * eW01
      + ((4253845 : ℂ) / 330577) * eW02
      + (-(2222486755 : ℂ) / 333221616) * eW03
      + (-(45025775 : ℂ) / 6408108) * eW10
      + (-(3892140055 : ℂ) / 333221616) * eW12
      + (-(112838915 : ℂ) / 8925579) * eW13
      + (-(102332540 : ℂ) / 8925579) * eW20
      + ((152190055 : ℂ) / 20826351) * eW21
      + ((19439225 : ℂ) / 1602027) * eW23
      + ((125182480 : ℂ) / 20826351) * eW30
      + ((3681220 : ℂ) / 330577) * eW31
      + ((31250 : ℂ) / 25429) * eR0
  · show J ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2)) = J0tab 0 1 1 1
    rw [J_e0111]
    linear_combination (-(7132442 : ℂ) / 8010135) * eTP00
      + (-(1547996 : ℂ) / 381435) * eTP01
      + (-(6313508 : ℂ) / 24030405) * eTP10
      + (-(19231378 : ℂ) / 8010135) * eTP11
      + (-(590400 : ℂ) / 25429) * eW01
      + (-(13397120 : ℂ) / 991731) * eW02
      + ((1743038585 : ℂ) / 124958106) * eW03
      + (-(14233150 : ℂ) / 4806081) * eW10
      + ((109137785 : ℂ) / 124958106) * eW12
      + ((549072440 : ℂ) / 26776737) * eW13
      + ((412282880 : ℂ) / 26776737) * eW20
      + (-(937528960 : ℂ) / 62479053) * eW21
      + (-(97352450 : ℂ) / 4806081) * eW23
      + (-(65783680 : ℂ) / 62479053) * eW30
      + (-(11755520 : ℂ) / 991731) * eW31
      + ((410000 : ℂ) / 76287) * eR0
  · show J ((1 : Fin 2), (0 : Fin 2)) ((0 : Fin 2), (0 : Fin 2)) = J0tab 1 0 0 0
    rw [J_e1000]
    linear_combination ((434905 : ℂ) / 1602027) * eTP00
      + ((81490 : ℂ) / 76287) * eTP01
      + ((1197670 : ℂ) / 4806081) * eTP10
      + ((1172645 : ℂ) / 1602027) * eTP11
      + ((180000 : ℂ) / 25429) * eW01
      + ((2380000 : ℂ) / 991731) * eW02
      + (-(241133500 : ℂ) / 62479053) * eW03
      + ((4339375 : ℂ) / 4806081) * eW10
      + ((24642500 : ℂ) / 62479053) * eW12
      + (-(93188000 : ℂ) / 26776737) * eW13
      + (-(31446560 : ℂ) / 26776737) * eW20
      + ((101216035 : ℂ) / 19224324) * eW21
      + ((29680625 : ℂ) / 4806081) * eW23
      + ((169483975 : ℂ) / 249916212) * eW30
      + ((107200 : ℂ) / 76287) * eW31
      + (-(125000 : ℂ) / 76287) * eR0
  · show J ((1 : Fin 2), (0 : Fin 2)) ((0 : Fin 2), (1 : Fin 2)) = J0tab 1 0 0 1
    rw [J_e1001]
    linear_combination (-(10922101 : ℂ) / 10680180) * eTP00
      + ((291994 : ℂ) / 381435) * eTP01
      + ((244799 : ℂ) / 8010135) * eTP10
      + ((2884351 : ℂ) / 10680180) * eTP11
      + ((1558625 : ℂ) / 305148) * eW01
      + ((7359500 : ℂ) / 2975193) * eW02
      + (-(45882700 : ℂ) / 20826351) * eW03
      + ((8375125 : ℂ) / 6408108) * eW10
      + (-(18875125 : ℂ) / 20826351) * eW12
      + (-(25018100 : ℂ) / 8925579) * eW13
      + (-(9557225 : ℂ) / 8925579) * eW20
      + (-(1155097175 : ℂ) / 333221616) * eW21
      + ((19439225 : ℂ) / 1602027) * eW23
      + ((514556125 : ℂ) / 333221616) * eW30
      + ((3857375 : ℂ) / 2975193) * eW31
      + ((31250 : ℂ) / 25429) * eR0
  · show J ((1 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (0 : Fin 2)) = J0tab 1 0 1 0
    rw [J_e1010]
    linear_combination ((66881354 : ℂ) / 40050675) * eTP00
      + ((376489 : ℂ) / 3814350) * eTP01
      + ((79480357 : ℂ) / 240304050) * eTP10
      + ((32786746 : ℂ) / 40050675) * eTP11
      + ((7175 : ℂ) / 25429) * eW01
      + (-(918800 : ℂ) / 991731) * eW02
      + ((111041785 : ℂ) / 62479053) * eW03
      + ((33305075 : ℂ) / 19224324) * eW10
      + ((53517325 : ℂ) / 62479053) * eW12
      + (-(39114520 : ℂ) / 26776737) * eW13
      + ((19801640 : ℂ) / 26776737) * eW20
      + (-(7820380 : ℂ) / 62479053) * eW21
      + (-(27880775 : ℂ) / 19224324) * eW23
      + ((49704080 : ℂ) / 62479053) * eW30
      + (-(3100880 : ℂ) / 991731) * eW31
      + (-(310000 : ℂ) / 76287) * eR0
  · show J ((1 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (1 : Fin 2)) = J0tab 1 0 1 1
    rw [J_e1011]
    linear_combination (-(8519486 : ℂ) / 13350225) * eTP00
      + (-(794038 : ℂ) / 635725) * eTP01
      + (-(16467119 : ℂ) / 40050675) * eTP10
      + (-(16397539 : ℂ) / 13350225) * eTP11
      + (-(3264725 : ℂ) / 406864) * eW01
      + (-(2489525 : ℂ) / 991731) * eW02
      + ((51864110 : ℂ) / 20826351) * eW03
      + (-(71448575 : ℂ) / 25632432) * eW10
      + (-(15373825 : ℂ) / 83305404) * eW12
      + ((46014955 : ℂ) / 8925579) * eW13
      + ((72480895 : ℂ) / 8925579) * eW20
      + (-(823326485 : ℂ) / 83305404) * eW21
      + (-(36803975 : ℂ) / 3204054) * eW23
      + ((18088780 : ℂ) / 20826351) * eW30
      + (-(1131955 : ℂ) / 330577) * eW31
      + ((77500 : ℂ) / 25429) * eR0
  · show J ((1 : Fin 2), (1 : Fin 2)) ((0 : Fin 2), (0 : Fin 2)) = J0tab 1 1 0 0
    rw [J_e1100]
    linear_combination (-(241921 : ℂ) / 10680180) * eTP00
      + ((266858 : ℂ) / 127145) * eTP01
      + ((244799 : ℂ) / 8010135) * eTP10
      + ((2884351 : ℂ) / 10680180) * eTP11
      + ((1367175 : ℂ) / 101716) * eW01
      + ((1947900 : ℂ) / 330577) * eW02
      + (-(216765580 : ℂ) / 20826351) * eW03
      + (-(45025775 : ℂ) / 6408108) * eW10
      + ((34525775 : ℂ) / 20826351) * eW12
      + (-(79944740 : ℂ) / 8925579) * eW13
      + (-(78215525 : ℂ) / 8925579) * eW20
      + ((3597582925 : ℂ) / 333221616) * eW21
      + ((19439225 : ℂ) / 1602027) * eW23
      + (-(2358412295 : ℂ) / 333221616) * eW30
      + ((1050195 : ℂ) / 330577) * eW31
      + ((31250 : ℂ) / 25429) * eR0
  · show J ((1 : Fin 2), (1 : Fin 2)) ((0 : Fin 2), (1 : Fin 2)) = J0tab 1 1 0 1
    rw [J_e1101]
    linear_combination (-(7132442 : ℂ) / 8010135) * eTP00
      + (-(1336436 : ℂ) / 381435) * eTP01
      + (-(19641788 : ℂ) / 24030405) * eTP10
      + (-(19231378 : ℂ) / 8010135) * eTP11
      + (-(590400 : ℂ) / 25429) * eW01
      + (-(7806400 : ℂ) / 991731) * eW02
      + ((790917880 : ℂ) / 62479053) * eW03
      + (-(14233150 : ℂ) / 4806081) * eW10
      + (-(80827400 : ℂ) / 62479053) * eW12
      + ((305656640 : ℂ) / 26776737) * eW13
      + ((261333440 : ℂ) / 26776737) * eW20
      + (-(1604265335 : ℂ) / 124958106) * eW21
      + (-(97352450 : ℂ) / 4806081) * eW23
      + ((29635465 : ℂ) / 124958106) * eW30
      + (-(2740120 : ℂ) / 991731) * eW31
      + ((410000 : ℂ) / 76287) * eR0
  · show J ((1 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (0 : Fin 2)) = J0tab 1 1 1 0
    rw [J_e1110]
    linear_combination (-(8519486 : ℂ) / 13350225) * eTP00
      + (-(1429763 : ℂ) / 635725) * eTP01
      + ((23583556 : ℂ) / 40050675) * eTP10
      + (-(16397539 : ℂ) / 13350225) * eTP11
      + (-(5807625 : ℂ) / 406864) * eW01
      + (-(1677475 : ℂ) / 330577) * eW02
      + ((180026270 : ℂ) / 20826351) * eW03
      + ((88754125 : ℂ) / 25632432) * eW10
      + (-(175576525 : ℂ) / 83305404) * eW12
      + ((87209935 : ℂ) / 8925579) * eW13
      + ((95366995 : ℂ) / 8925579) * eW20
      + (-(663123785 : ℂ) / 83305404) * eW21
      + (-(36803975 : ℂ) / 3204054) * eW23
      + (-(110073380 : ℂ) / 20826351) * eW30
      + (-(2657695 : ℂ) / 330577) * eW31
      + ((77500 : ℂ) / 25429) * eR0
  · show J ((1 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2)) = J0tab 1 1 1 1
    rw [J_e1111]
    linear_combination (-(86345527 : ℂ) / 120152025) * eTP00
      + ((11919943 : ℂ) / 11443050) * eTP01
      + (-(218892341 : ℂ) / 720912150) * eTP10
      + ((43331227 : ℂ) / 120152025) * eTP11
      + ((1675625 : ℂ) / 305148) * eW01
      + ((10363300 : ℂ) / 2975193) * eW02
      + (-(1082006585 : ℂ) / 187437159) * eW03
      + (-(84115625 : ℂ) / 28836486) * eW10
      + (-(139275950 : ℂ) / 187437159) * eW12
      + (-(133844380 : ℂ) / 80330211) * eW13
      + (-(496069900 : ℂ) / 80330211) * eW20
      + ((927557675 : ℂ) / 187437159) * eW21
      + ((484924375 : ℂ) / 57672972) * eW23
      + (-(15172960 : ℂ) / 187437159) * eW30
      + ((23779060 : ℂ) / 2975193) * eW31
      + ((507500 : ℂ) / 228861) * eR0

/-- **`twoByTwo_nonCP`.** The unique candidate fails positivity, by the explicit rational
vector `v0 = (1,−1,−1,−1)`: `v0† J0 v0 = −449600/76287 < 0`. Symbolic — no floating
eigenvalue enters the certificate. -/
theorem twoByTwo_nonCP : ¬ J0.PosSemidef := by
  intro hpsd
  have h := hpsd.dotProduct_mulVec_nonneg v0
  rw [show star v0 ⬝ᵥ (J0 *ᵥ v0) = ((-449600 / 76287 : ℝ) : ℂ) from by
    simp only [dotProduct, Matrix.mulVec, J0, v0, Fintype.sum_prod_type,
      Fin.sum_univ_two, Pi.star_apply, Matrix.cons_val_zero, Matrix.cons_val_one,
      Matrix.head_cons, star_neg, star_one, J_e0000, J_e0001, J_e0010, J_e0011, J_e0100, J_e0101, J_e0110, J_e0111, J_e1000, J_e1001, J_e1010, J_e1011, J_e1100, J_e1101, J_e1110, J_e1111]
    norm_num] at h
  rw [Complex.zero_le_real] at h
  norm_num at h

set_option maxHeartbeats 2000000 in
/-- **THE EXACT (2,2) NO-GO, assembled against the named predicate.** At this witness
carrier — preparation feasible by construction, classical action globally reachable
(probe F16) — NO visible-local CPTP instrument realizes the one-slot lift: rigidity
forces the Kraus family's Choi matrix to be `J0`, which is not positive semidefinite. -/
theorem twoByTwo_no_local_lift :
    ¬ CoherentLift.TwoTimeCoherentLift V0 E0 rho0 tp0 := by
  rintro ⟨κ, K, hK, hbranch⟩
  set X := ∑ k, (CoherentLift.vlift (K k) : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
    * rho0 * (CoherentLift.vlift (K k))ᴴ with hX
  have hgap : ∀ a b c d : Fin 4, a ≠ b → c ≠ d → E0 b - E0 a = E0 d - E0 c
      → a = c ∧ b = d := by
    have hq : ∀ a b c d : Fin 4, a ≠ b → c ≠ d → E0q b - E0q a = E0q d - E0q c
        → a = c ∧ b = d := by decide
    intro a b c d hab hcd h
    refine hq a b c d hab hcd ?_
    have h' : ((E0q b : ℤ) : ℝ) - ((E0q a : ℤ) : ℝ)
        = ((E0q d : ℤ) : ℝ) - ((E0q c : ℤ) : ℝ) := h
    exact_mod_cast h'
  have hreadC : ∀ a b : Fin 4, a ≠ b → ∃ j : Fin 2,
      (V0ᴴ * CoherentLift.readProj (Prod.fst : Fin 2 × Fin 2 → Fin 2) j * V0
        : Matrix (Fin 4) (Fin 4) ℂ) b a ≠ 0 := by
    intro a b hab
    refine ⟨0, ?_⟩
    fin_cases a <;> fin_cases b
    · exact absurd rfl hab
    · show (V0ᴴ * CoherentLift.readProj (Prod.fst : Fin 2 × Fin 2 → Fin 2) 0 * V0
          : Matrix (Fin 4) (Fin 4) ℂ) (1 : Fin 4) (0 : Fin 4) ≠ 0
      simp only [CoherentLift.readProj, V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.diagonal_apply, Fintype.sum_prod_type, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Prod.mk.injEq]
      norm_num
    · show (V0ᴴ * CoherentLift.readProj (Prod.fst : Fin 2 × Fin 2 → Fin 2) 0 * V0
          : Matrix (Fin 4) (Fin 4) ℂ) (2 : Fin 4) (0 : Fin 4) ≠ 0
      simp only [CoherentLift.readProj, V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.diagonal_apply, Fintype.sum_prod_type, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Prod.mk.injEq]
      norm_num
    · show (V0ᴴ * CoherentLift.readProj (Prod.fst : Fin 2 × Fin 2 → Fin 2) 0 * V0
          : Matrix (Fin 4) (Fin 4) ℂ) (3 : Fin 4) (0 : Fin 4) ≠ 0
      simp only [CoherentLift.readProj, V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.diagonal_apply, Fintype.sum_prod_type, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Prod.mk.injEq]
      norm_num
    · show (V0ᴴ * CoherentLift.readProj (Prod.fst : Fin 2 × Fin 2 → Fin 2) 0 * V0
          : Matrix (Fin 4) (Fin 4) ℂ) (0 : Fin 4) (1 : Fin 4) ≠ 0
      simp only [CoherentLift.readProj, V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.diagonal_apply, Fintype.sum_prod_type, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Prod.mk.injEq]
      norm_num
    · exact absurd rfl hab
    · show (V0ᴴ * CoherentLift.readProj (Prod.fst : Fin 2 × Fin 2 → Fin 2) 0 * V0
          : Matrix (Fin 4) (Fin 4) ℂ) (2 : Fin 4) (1 : Fin 4) ≠ 0
      simp only [CoherentLift.readProj, V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.diagonal_apply, Fintype.sum_prod_type, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Prod.mk.injEq]
      norm_num
    · show (V0ᴴ * CoherentLift.readProj (Prod.fst : Fin 2 × Fin 2 → Fin 2) 0 * V0
          : Matrix (Fin 4) (Fin 4) ℂ) (3 : Fin 4) (1 : Fin 4) ≠ 0
      simp only [CoherentLift.readProj, V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.diagonal_apply, Fintype.sum_prod_type, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Prod.mk.injEq]
      norm_num
    · show (V0ᴴ * CoherentLift.readProj (Prod.fst : Fin 2 × Fin 2 → Fin 2) 0 * V0
          : Matrix (Fin 4) (Fin 4) ℂ) (0 : Fin 4) (2 : Fin 4) ≠ 0
      simp only [CoherentLift.readProj, V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.diagonal_apply, Fintype.sum_prod_type, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Prod.mk.injEq]
      norm_num
    · show (V0ᴴ * CoherentLift.readProj (Prod.fst : Fin 2 × Fin 2 → Fin 2) 0 * V0
          : Matrix (Fin 4) (Fin 4) ℂ) (1 : Fin 4) (2 : Fin 4) ≠ 0
      simp only [CoherentLift.readProj, V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.diagonal_apply, Fintype.sum_prod_type, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Prod.mk.injEq]
      norm_num
    · exact absurd rfl hab
    · show (V0ᴴ * CoherentLift.readProj (Prod.fst : Fin 2 × Fin 2 → Fin 2) 0 * V0
          : Matrix (Fin 4) (Fin 4) ℂ) (3 : Fin 4) (2 : Fin 4) ≠ 0
      simp only [CoherentLift.readProj, V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.diagonal_apply, Fintype.sum_prod_type, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Prod.mk.injEq]
      norm_num
    · show (V0ᴴ * CoherentLift.readProj (Prod.fst : Fin 2 × Fin 2 → Fin 2) 0 * V0
          : Matrix (Fin 4) (Fin 4) ℂ) (0 : Fin 4) (3 : Fin 4) ≠ 0
      simp only [CoherentLift.readProj, V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.diagonal_apply, Fintype.sum_prod_type, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Prod.mk.injEq]
      norm_num
    · show (V0ᴴ * CoherentLift.readProj (Prod.fst : Fin 2 × Fin 2 → Fin 2) 0 * V0
          : Matrix (Fin 4) (Fin 4) ℂ) (1 : Fin 4) (3 : Fin 4) ≠ 0
      simp only [CoherentLift.readProj, V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.diagonal_apply, Fintype.sum_prod_type, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Prod.mk.injEq]
      norm_num
    · show (V0ᴴ * CoherentLift.readProj (Prod.fst : Fin 2 × Fin 2 → Fin 2) 0 * V0
          : Matrix (Fin 4) (Fin 4) ℂ) (2 : Fin 4) (3 : Fin 4) ≠ 0
      simp only [CoherentLift.readProj, V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Matrix.diagonal_apply, Fintype.sum_prod_type, Fin.sum_univ_two, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Prod.mk.injEq]
      norm_num
    · exact absurd rfl hab
  have hstat : ∀ a b : Fin 4, a ≠ b →
      (V0ᴴ * X * V0 : Matrix (Fin 4) (Fin 4) ℂ) a b = 0 := by
    intro a b hab
    exact CoherentLift.two_time_forces_stationary V0 X E0
      (fun j => CoherentLift.readProj (Prod.fst : Fin 2 × Fin 2 → Fin 2) j)
      (fun j => ((tp0 j : ℝ) : ℂ)) hgap hreadC (fun j t => hbranch j t) hab
  have hVV : V0 * V0ᴴ = 1 := by
    ext p q
    fin_cases p <;> fin_cases q
    · show (V0 * V0ᴴ : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((0 : Fin 2), (0 : Fin 2)) ((0 : Fin 2), (0 : Fin 2))
          = (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((0 : Fin 2), (0 : Fin 2)) ((0 : Fin 2), (0 : Fin 2))
      simp only [V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fin.sum_univ_four, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Matrix.one_apply, Prod.mk.injEq]
      norm_num
    · show (V0 * V0ᴴ : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((0 : Fin 2), (0 : Fin 2)) ((0 : Fin 2), (1 : Fin 2))
          = (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((0 : Fin 2), (0 : Fin 2)) ((0 : Fin 2), (1 : Fin 2))
      simp only [V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fin.sum_univ_four, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Matrix.one_apply, Prod.mk.injEq]
      norm_num
    · show (V0 * V0ᴴ : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((0 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (0 : Fin 2))
          = (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((0 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (0 : Fin 2))
      simp only [V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fin.sum_univ_four, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Matrix.one_apply, Prod.mk.injEq]
      norm_num
    · show (V0 * V0ᴴ : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((0 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (1 : Fin 2))
          = (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((0 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (1 : Fin 2))
      simp only [V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fin.sum_univ_four, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Matrix.one_apply, Prod.mk.injEq]
      norm_num
    · show (V0 * V0ᴴ : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((0 : Fin 2), (1 : Fin 2)) ((0 : Fin 2), (0 : Fin 2))
          = (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((0 : Fin 2), (1 : Fin 2)) ((0 : Fin 2), (0 : Fin 2))
      simp only [V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fin.sum_univ_four, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Matrix.one_apply, Prod.mk.injEq]
      norm_num
    · show (V0 * V0ᴴ : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((0 : Fin 2), (1 : Fin 2)) ((0 : Fin 2), (1 : Fin 2))
          = (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((0 : Fin 2), (1 : Fin 2)) ((0 : Fin 2), (1 : Fin 2))
      simp only [V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fin.sum_univ_four, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Matrix.one_apply, Prod.mk.injEq]
      norm_num
    · show (V0 * V0ᴴ : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (0 : Fin 2))
          = (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (0 : Fin 2))
      simp only [V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fin.sum_univ_four, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Matrix.one_apply, Prod.mk.injEq]
      norm_num
    · show (V0 * V0ᴴ : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2))
          = (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((0 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2))
      simp only [V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fin.sum_univ_four, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Matrix.one_apply, Prod.mk.injEq]
      norm_num
    · show (V0 * V0ᴴ : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((1 : Fin 2), (0 : Fin 2)) ((0 : Fin 2), (0 : Fin 2))
          = (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((1 : Fin 2), (0 : Fin 2)) ((0 : Fin 2), (0 : Fin 2))
      simp only [V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fin.sum_univ_four, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Matrix.one_apply, Prod.mk.injEq]
      norm_num
    · show (V0 * V0ᴴ : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((1 : Fin 2), (0 : Fin 2)) ((0 : Fin 2), (1 : Fin 2))
          = (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((1 : Fin 2), (0 : Fin 2)) ((0 : Fin 2), (1 : Fin 2))
      simp only [V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fin.sum_univ_four, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Matrix.one_apply, Prod.mk.injEq]
      norm_num
    · show (V0 * V0ᴴ : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((1 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (0 : Fin 2))
          = (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((1 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (0 : Fin 2))
      simp only [V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fin.sum_univ_four, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Matrix.one_apply, Prod.mk.injEq]
      norm_num
    · show (V0 * V0ᴴ : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((1 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (1 : Fin 2))
          = (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((1 : Fin 2), (0 : Fin 2)) ((1 : Fin 2), (1 : Fin 2))
      simp only [V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fin.sum_univ_four, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Matrix.one_apply, Prod.mk.injEq]
      norm_num
    · show (V0 * V0ᴴ : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((1 : Fin 2), (1 : Fin 2)) ((0 : Fin 2), (0 : Fin 2))
          = (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((1 : Fin 2), (1 : Fin 2)) ((0 : Fin 2), (0 : Fin 2))
      simp only [V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fin.sum_univ_four, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Matrix.one_apply, Prod.mk.injEq]
      norm_num
    · show (V0 * V0ᴴ : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((1 : Fin 2), (1 : Fin 2)) ((0 : Fin 2), (1 : Fin 2))
          = (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((1 : Fin 2), (1 : Fin 2)) ((0 : Fin 2), (1 : Fin 2))
      simp only [V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fin.sum_univ_four, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Matrix.one_apply, Prod.mk.injEq]
      norm_num
    · show (V0 * V0ᴴ : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((1 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (0 : Fin 2))
          = (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((1 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (0 : Fin 2))
      simp only [V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fin.sum_univ_four, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Matrix.one_apply, Prod.mk.injEq]
      norm_num
    · show (V0 * V0ᴴ : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((1 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2))
          = (1 : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ)
          ((1 : Fin 2), (1 : Fin 2)) ((1 : Fin 2), (1 : Fin 2))
      simp only [V0, Matrix.mul_apply, Matrix.conjTranspose_apply, Fin.sum_univ_four, V_e000, V_e001, V_e002, V_e003, V_e010, V_e011, V_e012, V_e013, V_e100, V_e101, V_e102, V_e103, V_e110, V_e111, V_e112, V_e113, star_div₀, star_ofNat, star_neg, star_zero, star_one, Matrix.one_apply, Prod.mk.injEq]
      norm_num
  have hread0 : ∀ j : Fin 2, Matrix.trace (CoherentLift.readProj
      (Prod.fst : Fin 2 × Fin 2 → Fin 2) j * X) = ((tp0 j : ℝ) : ℂ) := by
    intro j
    have h := hbranch j 0
    rwa [CoherentLift.umat_zero V0 E0 hVV, Matrix.conjTranspose_one, one_mul, mul_one] at h
  have happ : CoherentLift.chApply (CoherentLift.krausChoi K) rho0 = X := by
    rw [CoherentLift.chApply_krausChoi K rho0, hX]
  have hJ : CoherentLift.krausChoi K = J0 := by
    refine twoByTwo_affine_rigidity _ (CoherentLift.krausChoi_tp K hK) ?_ ?_
    · intro a b hab
      rw [happ]
      exact hstat a b hab
    · intro j
      rw [happ]
      exact hread0 j
  exact twoByTwo_nonCP (hJ ▸ CoherentLift.krausChoi_psd K)

#print axioms twoByTwo_affine_rigidity
#print axioms twoByTwo_nonCP
#print axioms twoByTwo_no_local_lift

end TwoByTwoNoGo
end OIBridge
