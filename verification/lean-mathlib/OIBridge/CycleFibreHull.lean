/-
  OIBridge/CycleFibreHull.lean — the F22 findings frozen as kernel theorems: the
  cycle-fibre hull, the log-branch invariance of projector overlaps, and the ergodic-shell
  representation.

  PHASE THREE, ROUND TWELVE. Probe F22 ran the substratum coherent-existence test's first
  stage exactly; this file proves the general theorems behind its geometry, so the
  stage-one verdict rests on kernel statements rather than on one carrier's arithmetic.

  §A — THE CYCLE-FIBRE HULL. For a permutation carrier `permMatrix φ` with visible fibre
  projectors `fiberProj vis i`, the stationary visible-readout set is EXACTLY the convex
  hull of the orbit fibre-ratio points `r_i^(α) = |C_α ∩ P_i| / |C_α|`:

      stationary readouts  =  conv { r^(α) : α an orbit of φ }.

  Both directions are proved. `stationary_readout_hull`: every PSD trace-one state
  commuting with the carrier reads out a convex combination of the orbit frequency
  vectors `freq φ vis · s` (constant on orbits — `freq_shift`, `freq_pow` — and equal to
  the `r^(α)`), the weights being the state's own diagonal.  `hull_readout_achieved`:
  every such convex combination is the readout of an explicit stationary diagonal state,
  the orbit average of the weights.  `no_representation_outside_hull` is the necessity
  face: a preparation profile outside the hull has NO stationary representation on that
  carrier — feasibility at the permutation layer is decided by cycle-fibre combinatorics
  and nothing else, and it is non-tautological.

  §B — THE ERGODIC SHELL. On a shell where the dynamics acts transitively the orbit
  frequencies collapse to the counting marginal (`transitive_freq_eq_countMarginal`, via
  the unconditional mass count `freq_sum_card`), so `p_i = |C ∩ P_i| / |C|` is the UNIQUE
  stationary readout (`ergodicShell_readout_unique`), and `ergodicShell_SRC` packages the
  OI result: a finite invariant shell on which the reversible dynamics acts transitively
  has a permutation-level coherent stationary representation — the uniform state, which
  is the classical shell ensemble itself — whose visible readout is precisely its uniform
  counting marginal; and every stationary representation on that shell reads out exactly
  that marginal. Uniform shell counting is automatically coherently representable at the
  permutation level: the correlated shell assignment is not the preparation obstruction
  there. `cycle_eigenvector_overlap` is the DFT identity in readout form: every
  normalized eigenvector of a transitive permutation carrier has fibre overlaps exactly
  `m_i / N` — no root-of-unity arithmetic enters, only the uniqueness theorem applied to
  the eigenvector's own dyad.

  §C — THE LOG-BRANCH INVARIANCE. Changing the logarithm branch of a finite carrier's
  interpolation shifts eigenvalues by `2π`-multiples but cannot move the eigenvectors of
  a simple-spectrum block: any two unitary diagonalizations of the same matrix with the
  same injective eigenvalue labels differ by a diagonal phase
  (`simple_spectrum_column_moduli`), so every diagonal-readout overlap
  `⟨a|P|a⟩ = Σ_s P_ss |V_sa|²` is branch-independent
  (`permLogBranch_projOverlap_invariant`). The carrier datum `B` that preparation
  feasibility consumes is canonical on nondegenerate permutation blocks; what remains
  underdetermined beyond the permutation shadow is the generic-flow `B` itself — the
  named missing premise the F22 audit isolated, which no theorem here can supply.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.CoherentLift
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Analysis.Complex.Order

namespace OIBridge
namespace CycleFibreHull

open Complex Matrix CoherentLift
open scoped ComplexOrder

local notation "conj'" => (starRingEnd ℂ)

variable {S I : Type*} [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I]

/-! ### Section A₀ — the objects -/

/-- The visible fibre projector: the diagonal indicator of `vis⁻¹(i)`. -/
def fiberProj (vis : S → I) (i : I) : Matrix S S ℂ :=
  Matrix.diagonal fun s => if vis s = i then 1 else 0

/-- The orbit frequency of fibre `i` along the `φ`-orbit of `s`, over one full period:
the cycle fibre ratio `r_i^(α)` of the cycle through `s`. -/
noncomputable def freq (φ : Equiv.Perm S) (vis : S → I) (i : I) (s : S) : ℝ :=
  (∑ k ∈ Finset.range (orderOf φ), if vis ((φ ^ k) s) = i then (1 : ℝ) else 0)
    / (orderOf φ : ℝ)

/-- The uniform counting marginal of the fibres. -/
noncomputable def countMarginal (vis : S → I) (i : I) : ℝ :=
  ((Finset.univ.filter fun s => vis s = i).card : ℝ) / (Fintype.card S : ℝ)

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- A window sum is shift-invariant when the endpoints agree. -/
theorem sum_range_shift {M : Type*} [AddCommGroup M] (f : ℕ → M) (L : ℕ) (hf : f L = f 0) :
    ∑ k ∈ Finset.range L, f (k + 1) = ∑ k ∈ Finset.range L, f k := by
  have h1 := Finset.sum_range_succ' f L
  have h2 := Finset.sum_range_succ f L
  rw [hf] at h2
  exact add_right_cancel (h1.symm.trans h2)

omit [Fintype S] [DecidableEq S] [Fintype I] in
/-- Orbit frequencies are constant along the orbit: one step. -/
theorem freq_shift (φ : Equiv.Perm S) (vis : S → I) (i : I) (s : S) :
    freq φ vis i (φ s) = freq φ vis i s := by
  unfold freq
  congr 1
  calc ∑ k ∈ Finset.range (orderOf φ), (if vis ((φ ^ k) (φ s)) = i then (1 : ℝ) else 0)
      = ∑ k ∈ Finset.range (orderOf φ), (if vis ((φ ^ (k + 1)) s) = i then (1 : ℝ) else 0) :=
        Finset.sum_congr rfl fun k _ => by rw [pow_succ, Equiv.Perm.mul_apply]
    _ = ∑ k ∈ Finset.range (orderOf φ), (if vis ((φ ^ k) s) = i then (1 : ℝ) else 0) :=
        sum_range_shift (fun k => if vis ((φ ^ k) s) = i then (1 : ℝ) else 0) _
          (by rw [pow_orderOf_eq_one, pow_zero])

omit [Fintype S] [DecidableEq S] [Fintype I] in
/-- Orbit frequencies are constant along the orbit: any power. -/
theorem freq_pow (φ : Equiv.Perm S) (vis : S → I) (i : I) (s : S) (k : ℕ) :
    freq φ vis i ((φ ^ k) s) = freq φ vis i s := by
  induction k with
  | zero => rw [pow_zero]; rfl
  | succ k ih =>
      rw [pow_succ', Equiv.Perm.mul_apply, freq_shift]
      exact ih

omit [DecidableEq S] in
/-- The frequencies at a point form a probability vector. -/
theorem freq_sum_one (φ : Equiv.Perm S) (vis : S → I) (s : S) :
    ∑ i, freq φ vis i s = 1 := by
  unfold freq
  rw [← Finset.sum_div, Finset.sum_comm]
  rw [Finset.sum_congr rfl fun k _ =>
    Finset.sum_ite_eq_of_mem Finset.univ (vis ((φ ^ k) s)) (fun _ => (1 : ℝ))
      (Finset.mem_univ _)]
  rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul, mul_one]
  exact div_self (Nat.cast_ne_zero.mpr (orderOf_pos φ).ne')

omit [DecidableEq S] [Fintype I] in
/-- The total mass of a fibre across all orbits is its cardinality: summing the orbit
frequency over the whole space counts the fibre. No stationarity enters. -/
theorem freq_sum_card (φ : Equiv.Perm S) (vis : S → I) (i : I) :
    ∑ s, freq φ vis i s = ((Finset.univ.filter fun s => vis s = i).card : ℝ) := by
  unfold freq
  rw [← Finset.sum_div, Finset.sum_comm]
  rw [Finset.sum_congr rfl fun k _ =>
    Equiv.sum_comp ((φ ^ k : Equiv.Perm S)) (fun t => if vis t = i then (1 : ℝ) else 0)]
  rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul, Finset.sum_boole]
  rw [mul_comm, mul_div_assoc]
  rw [div_self (Nat.cast_ne_zero.mpr (orderOf_pos φ).ne'), mul_one]

omit [Fintype I] in
/-- The fibre readout of a matrix is the fibre-restricted diagonal sum. -/
theorem fiberProj_trace (vis : S → I) (i : I) (ρ : Matrix S S ℂ) :
    Matrix.trace (fiberProj vis i * ρ) = ∑ s, if vis s = i then ρ s s else 0 := by
  rw [Matrix.trace]
  refine Finset.sum_congr rfl fun s _ => ?_
  rw [Matrix.diag_apply, fiberProj, Matrix.diagonal_mul, ite_mul, one_mul, zero_mul]

omit [Fintype I] in
/-- The diagonal of a stationary state is constant along the orbits. -/
theorem stationary_diag_pow (φ : Equiv.Perm S) (ρ : Matrix S S ℂ)
    (hstat : permMatrix φ * ρ * (permMatrix φ)ᴴ = ρ) (k : ℕ) (s : S) :
    ρ ((φ ^ k) s) ((φ ^ k) s) = ρ s s := by
  induction k with
  | zero => rw [pow_zero]; rfl
  | succ k ih =>
      have h2 := congrFun (congrFun hstat (φ ((φ ^ k) s))) (φ ((φ ^ k) s))
      rw [permMatrix_conj_apply, Equiv.symm_apply_apply] at h2
      rw [pow_succ', Equiv.Perm.mul_apply]
      exact h2.symm.trans ih

/-! ### Section A — the cycle-fibre hull -/

omit [Fintype I] in
/-- The real core of the hull theorem: for a stationary state, weighting the orbit
frequencies by the state's diagonal reproduces the fibre-restricted diagonal mass. -/
theorem stationary_freq_readout (φ : Equiv.Perm S) (vis : S → I) (ρ : Matrix S S ℂ)
    (hstat : permMatrix φ * ρ * (permMatrix φ)ᴴ = ρ) (i : I) :
    ∑ s, (ρ s s).re * freq φ vis i s = ∑ s, if vis s = i then (ρ s s).re else 0 := by
  have hbridge : ∀ k : ℕ,
      (∑ s, if vis ((φ ^ k) s) = i then (ρ s s).re else 0)
        = ∑ s, if vis s = i then (ρ s s).re else 0 := by
    intro k
    have hre := Equiv.sum_comp ((φ ^ k : Equiv.Perm S))
      (fun t => if vis t = i then
        (ρ (((φ ^ k)⁻¹ : Equiv.Perm S) t) (((φ ^ k)⁻¹ : Equiv.Perm S) t)).re else 0)
    simp only [Equiv.Perm.inv_def, Equiv.symm_apply_apply] at hre
    rw [hre]
    refine Finset.sum_congr rfl fun t _ => ?_
    have hdd := stationary_diag_pow φ ρ hstat k (((φ ^ k)⁻¹ : Equiv.Perm S) t)
    rw [Equiv.Perm.inv_def, Equiv.apply_symm_apply] at hdd
    rw [← hdd]
  calc ∑ s, (ρ s s).re * freq φ vis i s
      = ∑ s, (∑ k ∈ Finset.range (orderOf φ),
          if vis ((φ ^ k) s) = i then (ρ s s).re else 0) / (orderOf φ : ℝ) := by
        refine Finset.sum_congr rfl fun s _ => ?_
        rw [freq, mul_div_assoc', Finset.mul_sum]
        congr 1
        exact Finset.sum_congr rfl fun k _ => by rw [mul_ite, mul_one, mul_zero]
    _ = (∑ k ∈ Finset.range (orderOf φ), ∑ s,
          if vis ((φ ^ k) s) = i then (ρ s s).re else 0) / (orderOf φ : ℝ) := by
        rw [← Finset.sum_div, Finset.sum_comm]
    _ = (∑ _k ∈ Finset.range (orderOf φ), ∑ s,
          if vis s = i then (ρ s s).re else 0) / (orderOf φ : ℝ) := by
        rw [Finset.sum_congr rfl fun k _ => hbridge k]
    _ = ∑ s, if vis s = i then (ρ s s).re else 0 := by
        rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul, mul_comm, mul_div_assoc,
          div_self (Nat.cast_ne_zero.mpr (orderOf_pos φ).ne'), mul_one]

omit [Fintype S] [DecidableEq S] [Fintype I] in
/-- The diagonal entries of a PSD matrix are their own real parts. -/
theorem psd_diag_real (ρ : Matrix S S ℂ) (hpsd : ρ.PosSemidef) (s : S) :
    ρ s s = (((ρ s s).re : ℝ) : ℂ) := by
  obtain ⟨hre, him⟩ := Complex.nonneg_iff.mp (hpsd.diag_nonneg (i := s))
  exact Complex.ext (by rw [Complex.ofReal_re]) (by rw [Complex.ofReal_im, ← him])

omit [Fintype I] in
/-- **THE CYCLE-FIBRE HULL, necessity direction.** Every PSD trace-one state commuting
with the permutation carrier reads out a CONVEX COMBINATION of the orbit fibre-ratio
vectors: the weights are the state's own diagonal, and the readout on every fibre is the
correspondingly weighted average of the orbit frequencies. The stationary readout set is
contained in `conv { r^(α) }`. -/
theorem stationary_readout_hull (φ : Equiv.Perm S) (vis : S → I) (ρ : Matrix S S ℂ)
    (hpsd : ρ.PosSemidef) (htr : Matrix.trace ρ = 1)
    (hstat : permMatrix φ * ρ * (permMatrix φ)ᴴ = ρ) :
    ∃ w : S → ℝ, (∀ s, 0 ≤ w s) ∧ (∑ s, w s) = 1 ∧
      ∀ i, Matrix.trace (fiberProj vis i * ρ)
        = ((∑ s, w s * freq φ vis i s : ℝ) : ℂ) := by
  refine ⟨fun s => (ρ s s).re,
    fun s => (Complex.nonneg_iff.mp (hpsd.diag_nonneg (i := s))).1, ?_, ?_⟩
  · have h1 : Matrix.trace ρ = ((∑ s, (ρ s s).re : ℝ) : ℂ) := by
      rw [Matrix.trace]
      push_cast
      exact Finset.sum_congr rfl fun s _ => psd_diag_real ρ hpsd s
    rw [htr] at h1
    exact_mod_cast h1.symm
  · intro i
    rw [fiberProj_trace]
    rw [show ((∑ s, (fun s => (ρ s s).re) s * freq φ vis i s : ℝ) : ℂ)
        = ((∑ s, (ρ s s).re * freq φ vis i s : ℝ) : ℂ) from rfl]
    rw [stationary_freq_readout φ vis ρ hstat i]
    push_cast
    refine Finset.sum_congr rfl fun s _ => ?_
    by_cases hc : vis s = i
    · rw [if_pos hc, if_pos hc]
      exact psd_diag_real ρ hpsd s
    · rw [if_neg hc, if_neg hc, Complex.ofReal_zero]

omit [Fintype I] in
/-- **THE CYCLE-FIBRE HULL, achievability direction.** Every convex combination of the
orbit frequency vectors IS the readout of an explicit stationary state: the diagonal
state whose entries are the orbit averages of the weights. Together with
`stationary_readout_hull`, the stationary readout set is EXACTLY `conv { r^(α) }`. -/
theorem hull_readout_achieved (φ : Equiv.Perm S) (vis : S → I) (w : S → ℝ)
    (hw : ∀ s, 0 ≤ w s) (hsum : (∑ s, w s) = 1) :
    ∃ ρ : Matrix S S ℂ, ρ.PosSemidef ∧ Matrix.trace ρ = 1
      ∧ permMatrix φ * ρ * (permMatrix φ)ᴴ = ρ
      ∧ ∀ i, Matrix.trace (fiberProj vis i * ρ)
          = ((∑ s, w s * freq φ vis i s : ℝ) : ℂ) := by
  have hLpos : (0 : ℝ) < (orderOf φ : ℝ) := Nat.cast_pos.mpr (orderOf_pos φ)
  set d : S → ℝ :=
    fun s => (∑ k ∈ Finset.range (orderOf φ), w ((φ⁻¹ ^ k) s)) / (orderOf φ : ℝ)
    with hd
  have hdinv : ∀ s, d (φ s) = d s := by
    intro s
    rw [hd]
    show (∑ k ∈ Finset.range (orderOf φ), w ((φ⁻¹ ^ k) (φ s))) / (orderOf φ : ℝ)
      = (∑ k ∈ Finset.range (orderOf φ), w ((φ⁻¹ ^ k) s)) / (orderOf φ : ℝ)
    congr 1
    calc ∑ k ∈ Finset.range (orderOf φ), w ((φ⁻¹ ^ k) (φ s))
        = ∑ k ∈ Finset.range (orderOf φ), w ((φ⁻¹ ^ (k + 1)) (φ s)) :=
          (sum_range_shift (fun k => w ((φ⁻¹ ^ k) (φ s))) _ (by
            rw [inv_pow, pow_orderOf_eq_one, inv_one, pow_zero])).symm
      _ = ∑ k ∈ Finset.range (orderOf φ), w ((φ⁻¹ ^ k) s) :=
          Finset.sum_congr rfl fun k _ => by
            rw [pow_succ, Equiv.Perm.mul_apply, Equiv.Perm.inv_def,
              Equiv.symm_apply_apply]
  have hdnn : ∀ s, 0 ≤ d s := fun s =>
    div_nonneg (Finset.sum_nonneg fun k _ => hw _) hLpos.le
  refine ⟨Matrix.diagonal fun s => ((d s : ℝ) : ℂ), ?_, ?_, ?_, ?_⟩
  · exact Matrix.posSemidef_diagonal_iff.mpr fun s => Complex.zero_le_real.mpr (hdnn s)
  · rw [Matrix.trace_diagonal]
    have hds : (∑ s, d s) = 1 := by
      rw [hd]
      show (∑ s, (∑ k ∈ Finset.range (orderOf φ), w ((φ⁻¹ ^ k) s)) / (orderOf φ : ℝ)) = 1
      rw [← Finset.sum_div, Finset.sum_comm]
      rw [Finset.sum_congr rfl fun k _ => Equiv.sum_comp ((φ⁻¹ ^ k : Equiv.Perm S)) w]
      rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul, hsum, mul_one]
      exact div_self hLpos.ne'
    exact_mod_cast hds
  · rw [permMatrix_conj_diagonal]
    congr 1
    funext s
    have h0 := hdinv (φ.symm s)
    rw [Equiv.apply_symm_apply] at h0
    exact_mod_cast h0.symm
  · intro i
    rw [fiberProj_trace]
    have hreal : (∑ s, if vis s = i then d s else 0) = ∑ t, w t * freq φ vis i t := by
      rw [hd]
      show (∑ s, if vis s = i then
          (∑ k ∈ Finset.range (orderOf φ), w ((φ⁻¹ ^ k) s)) / (orderOf φ : ℝ) else 0)
        = ∑ t, w t * freq φ vis i t
      rw [Finset.sum_congr rfl fun s _ =>
        show (if vis s = i then
            (∑ k ∈ Finset.range (orderOf φ), w ((φ⁻¹ ^ k) s)) / (orderOf φ : ℝ) else 0)
          = (∑ k ∈ Finset.range (orderOf φ),
              if vis s = i then w ((φ⁻¹ ^ k) s) else 0) / (orderOf φ : ℝ) from by
          by_cases hc : vis s = i
          · rw [if_pos hc]
            congr 1
            exact Finset.sum_congr rfl fun k _ => (if_pos hc).symm
          · rw [if_neg hc, Finset.sum_congr rfl fun k _ => if_neg hc,
              Finset.sum_const, smul_zero, zero_div]]
      rw [← Finset.sum_div, Finset.sum_comm]
      have hk : ∀ k ∈ Finset.range (orderOf φ),
          (∑ s, if vis s = i then w ((φ⁻¹ ^ k) s) else 0)
            = ∑ t, if vis ((φ ^ k) t) = i then w t else 0 := by
        intro k _
        rw [← Equiv.sum_comp ((φ ^ k : Equiv.Perm S))
          (fun s => if vis s = i then w ((φ⁻¹ ^ k) s) else 0)]
        refine Finset.sum_congr rfl fun t _ => ?_
        rw [show ((φ⁻¹ ^ k : Equiv.Perm S)) ((φ ^ k) t) = t from by
          rw [inv_pow, Equiv.Perm.inv_def]
          exact Equiv.symm_apply_apply (φ ^ k) t]
      rw [Finset.sum_congr rfl hk, Finset.sum_comm, Finset.sum_div]
      refine Finset.sum_congr rfl fun t _ => ?_
      rw [freq, mul_div_assoc', Finset.mul_sum]
      congr 1
      exact Finset.sum_congr rfl fun k _ => by rw [mul_ite, mul_one, mul_zero]
    rw [← hreal]
    push_cast
    refine Finset.sum_congr rfl fun s _ => ?_
    by_cases hc : vis s = i
    · rw [if_pos hc, if_pos hc, Matrix.diagonal_apply_eq]
    · rw [if_neg hc, if_neg hc, Complex.ofReal_zero]

omit [Fintype I] in
/-- **THE NECESSITY FACE.** A preparation profile outside the cycle-fibre hull admits NO
stationary representation on the permutation carrier: feasibility at the permutation
layer is decided by cycle-fibre combinatorics and nothing else. -/
theorem no_representation_outside_hull (φ : Equiv.Perm S) (vis : S → I) (p : I → ℝ)
    (hout : ¬ ∃ w : S → ℝ, (∀ s, 0 ≤ w s) ∧ (∑ s, w s) = 1
      ∧ ∀ i, p i = ∑ s, w s * freq φ vis i s) :
    ¬ ∃ ρ : Matrix S S ℂ, ρ.PosSemidef ∧ Matrix.trace ρ = 1
      ∧ permMatrix φ * ρ * (permMatrix φ)ᴴ = ρ
      ∧ ∀ i, Matrix.trace (fiberProj vis i * ρ) = ((p i : ℝ) : ℂ) := by
  rintro ⟨ρ, hpsd, htr, hstat, hread⟩
  obtain ⟨w, hw, hsum, hhull⟩ := stationary_readout_hull φ vis ρ hpsd htr hstat
  refine hout ⟨w, hw, hsum, fun i => ?_⟩
  have h1 := (hread i).symm.trans (hhull i)
  exact_mod_cast h1

/-! ### Section B — the ergodic shell -/

omit [Fintype S] [DecidableEq S] [Fintype I] in
/-- On a transitive carrier the orbit frequencies are globally constant. -/
theorem transitive_freq_const (φ : Equiv.Perm S) (vis : S → I)
    (htrans : ∀ s t : S, ∃ k : ℕ, (φ ^ k) s = t) (i : I) (s t : S) :
    freq φ vis i s = freq φ vis i t := by
  obtain ⟨k, hk⟩ := htrans t s
  rw [← hk, freq_pow]

omit [DecidableEq S] [Fintype I] in
/-- On a transitive carrier every orbit frequency IS the counting marginal — the readout
form of the DFT identity `B_ia = m_i / N`, with no root of unity in sight. -/
theorem transitive_freq_eq_countMarginal [Nonempty S] (φ : Equiv.Perm S) (vis : S → I)
    (htrans : ∀ s t : S, ∃ k : ℕ, (φ ^ k) s = t) (i : I) (s : S) :
    freq φ vis i s = countMarginal vis i := by
  have hN : (0 : ℝ) < (Fintype.card S : ℝ) := Nat.cast_pos.mpr Fintype.card_pos
  have hsum := freq_sum_card φ vis i
  rw [Finset.sum_congr rfl fun t _ => transitive_freq_const φ vis htrans i t s] at hsum
  rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul] at hsum
  rw [countMarginal, ← hsum, mul_comm, mul_div_assoc, div_self hN.ne', mul_one]

omit [Fintype I] in
/-- On a transitive carrier the counting marginal is the UNIQUE stationary readout: the
collapse `p_i = |C ∩ P_i| / |C|`. -/
theorem ergodicShell_readout_unique [Nonempty S] (φ : Equiv.Perm S) (vis : S → I)
    (htrans : ∀ s t : S, ∃ k : ℕ, (φ ^ k) s = t) (ρ : Matrix S S ℂ)
    (hpsd : ρ.PosSemidef) (htr : Matrix.trace ρ = 1)
    (hstat : permMatrix φ * ρ * (permMatrix φ)ᴴ = ρ) (i : I) :
    Matrix.trace (fiberProj vis i * ρ) = ((countMarginal vis i : ℝ) : ℂ) := by
  obtain ⟨w, _, hsum, hhull⟩ := stationary_readout_hull φ vis ρ hpsd htr hstat
  rw [hhull i]
  congr 1
  calc ∑ s, w s * freq φ vis i s
      = ∑ s, w s * countMarginal vis i :=
        Finset.sum_congr rfl fun s _ => by
          rw [transitive_freq_eq_countMarginal φ vis htrans i s]
    _ = (∑ s, w s) * countMarginal vis i := by rw [← Finset.sum_mul]
    _ = countMarginal vis i := by rw [hsum, one_mul]

omit [Fintype I] in
/-- **`ergodicShell_SRC` — the ergodic-shell representation.** A finite invariant shell
on which the reversible dynamics acts transitively has a permutation-level coherent
stationary representation — the uniform state, which is the classical shell ensemble
itself — whose visible readout is precisely its uniform counting marginal; and every
stationary representation on that shell reads out exactly that marginal. Uniform shell
counting is automatically coherently representable at the permutation level: the
correlated shell assignment is not the preparation obstruction there. -/
theorem ergodicShell_SRC [Nonempty S] (φ : Equiv.Perm S) (vis : S → I)
    (htrans : ∀ s t : S, ∃ k : ℕ, (φ ^ k) s = t) :
    (∃ ρ : Matrix S S ℂ, ρ.PosSemidef ∧ Matrix.trace ρ = 1
        ∧ permMatrix φ * ρ * (permMatrix φ)ᴴ = ρ
        ∧ ∀ i, Matrix.trace (fiberProj vis i * ρ) = ((countMarginal vis i : ℝ) : ℂ))
    ∧ ∀ ρ : Matrix S S ℂ, ρ.PosSemidef → Matrix.trace ρ = 1
        → permMatrix φ * ρ * (permMatrix φ)ᴴ = ρ
        → ∀ i, Matrix.trace (fiberProj vis i * ρ) = ((countMarginal vis i : ℝ) : ℂ) := by
  have hN : (0 : ℝ) < (Fintype.card S : ℝ) := Nat.cast_pos.mpr Fintype.card_pos
  constructor
  · refine ⟨Matrix.diagonal fun _ => (((Fintype.card S : ℝ)⁻¹ : ℝ) : ℂ), ?_, ?_, ?_, ?_⟩
    · exact Matrix.posSemidef_diagonal_iff.mpr fun s =>
        Complex.zero_le_real.mpr (inv_nonneg.mpr hN.le)
    · rw [Matrix.trace_diagonal, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
      push_cast
      rw [mul_inv_cancel₀ (by exact_mod_cast hN.ne' : ((Fintype.card S : ℂ)) ≠ 0)]
    · rw [permMatrix_conj_diagonal]
    · intro i
      rw [fiberProj_trace]
      simp only [Matrix.diagonal_apply_eq]
      rw [← Finset.sum_filter, Finset.sum_const, nsmul_eq_mul, countMarginal]
      push_cast
      ring
  · exact fun ρ h1 h2 h3 => ergodicShell_readout_unique φ vis htrans ρ h1 h2 h3

omit [Fintype I] in
/-- **THE DFT IDENTITY IN READOUT FORM.** Every normalized eigenvector of a transitive
permutation carrier has fibre overlaps exactly `m_i / N`: the eigenvector's own dyad is a
stationary state, and the uniqueness theorem does the rest — no root-of-unity arithmetic.
The eigenvalue equation is taken in entry form, `v(φ⁻¹ p) = μ · v(p)`, which is
`permMatrix φ *ᵥ v = μ • v` read entrywise. -/
theorem cycle_eigenvector_overlap [Nonempty S] (φ : Equiv.Perm S) (vis : S → I)
    (htrans : ∀ s t : S, ∃ k : ℕ, (φ ^ k) s = t)
    (v : S → ℂ) (μ : ℂ) (hv : ∀ p : S, v (φ.symm p) = μ * v p)
    (hnorm : (∑ s, v s * conj' (v s)) = 1) (i : I) :
    (∑ s, if vis s = i then v s * conj' (v s) else 0)
      = ((countMarginal vis i : ℝ) : ℂ) := by
  have hμ : μ * conj' μ = 1 := by
    have h1 : (∑ p, v (φ.symm p) * conj' (v (φ.symm p))) = 1 :=
      (Equiv.sum_comp (φ.symm : Equiv.Perm S) fun s => v s * conj' (v s)).trans hnorm
    have h2 : (∑ p, v (φ.symm p) * conj' (v (φ.symm p)))
        = (μ * conj' μ) * ∑ p, v p * conj' (v p) := by
      rw [Finset.mul_sum]
      refine Finset.sum_congr rfl fun p _ => ?_
      rw [hv p, map_mul]
      ring
    rw [h2, hnorm, mul_one] at h1
    exact h1
  have hentry : ∀ p q, Matrix.vecMulVec v (star v) p q = v p * conj' (v q) := by
    intro p q
    rw [Matrix.vecMulVec_apply, Pi.star_apply, Complex.star_def]
  have hpsd : (Matrix.vecMulVec v (star v)).PosSemidef :=
    Matrix.posSemidef_vecMulVec_self_star v
  have htr : Matrix.trace (Matrix.vecMulVec v (star v)) = 1 := by
    rw [Matrix.trace]
    rw [Finset.sum_congr rfl fun s _ => by rw [Matrix.diag_apply, hentry]]
    exact hnorm
  have hstat : permMatrix φ * Matrix.vecMulVec v (star v) * (permMatrix φ)ᴴ
      = Matrix.vecMulVec v (star v) := by
    ext p q
    rw [permMatrix_conj_apply, hentry, hentry, hv p, hv q, map_mul]
    linear_combination (v p * conj' (v q)) * hμ
  have hread := ergodicShell_readout_unique φ vis htrans _ hpsd htr hstat i
  rw [fiberProj_trace] at hread
  rw [← hread]
  refine Finset.sum_congr rfl fun s _ => ?_
  by_cases hc : vis s = i
  · rw [if_pos hc, if_pos hc, hentry]
  · rw [if_neg hc, if_neg hc]

/-! ### Section C — the log-branch invariance -/

omit [Fintype I] [DecidableEq I] in
/-- A matrix commuting with an injectively labelled diagonal has vanishing off-diagonal
entries — the complex-spectrum commutant step. -/
theorem commutant_entry_zero {lam : S → ℂ} (hinj : Function.Injective lam)
    {Z : Matrix S S ℂ} (hcomm : Matrix.diagonal lam * Z = Z * Matrix.diagonal lam)
    {a b : S} (hab : a ≠ b) : Z a b = 0 := by
  have h := congrFun (congrFun hcomm a) b
  rw [Matrix.diagonal_mul, Matrix.mul_diagonal] at h
  have h2 : (lam a - lam b) * Z a b = 0 := by linear_combination h
  rcases mul_eq_zero.mp h2 with h' | h'
  · exact absurd (hinj (by linear_combination h')) hab
  · exact h'

omit [Fintype I] [DecidableEq I] in
/-- **SIMPLE SPECTRUM PINS THE COLUMN MODULI.** Two unitary diagonalizations of the same
matrix with the same injective eigenvalue labels differ by a diagonal phase, so the
moduli of every eigenvector entry agree. -/
theorem simple_spectrum_column_moduli {V W : Matrix S S ℂ} {lam : S → ℂ}
    (hV : Vᴴ * V = 1) (hW : Wᴴ * W = 1) (hinj : Function.Injective lam)
    (h : V * Matrix.diagonal lam * Vᴴ = W * Matrix.diagonal lam * Wᴴ) (s a : S) :
    W s a * conj' (W s a) = V s a * conj' (V s a) := by
  have hV' : V * Vᴴ = 1 := mul_eq_one_comm.mp hV
  have hcomm : Matrix.diagonal lam * (Vᴴ * W) = (Vᴴ * W) * Matrix.diagonal lam := by
    have h1 : Vᴴ * (V * Matrix.diagonal lam * Vᴴ) * W
        = Vᴴ * (W * Matrix.diagonal lam * Wᴴ) * W := by rw [h]
    calc Matrix.diagonal lam * (Vᴴ * W)
        = (Vᴴ * V) * Matrix.diagonal lam * (Vᴴ * W) := by rw [hV, Matrix.one_mul]
      _ = Vᴴ * (V * Matrix.diagonal lam * Vᴴ) * W := by noncomm_ring
      _ = Vᴴ * (W * Matrix.diagonal lam * Wᴴ) * W := h1
      _ = (Vᴴ * W) * Matrix.diagonal lam * (Wᴴ * W) := by noncomm_ring
      _ = (Vᴴ * W) * Matrix.diagonal lam := by rw [hW, Matrix.mul_one]
  have hZunit : (Vᴴ * W)ᴴ * (Vᴴ * W) = 1 := by
    calc (Vᴴ * W)ᴴ * (Vᴴ * W)
        = Wᴴ * (V * Vᴴ) * W := by
          rw [Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose]
          noncomm_ring
      _ = 1 := by rw [hV', Matrix.mul_one, hW]
  have hz : ∀ c : S, conj' ((Vᴴ * W) c c) * (Vᴴ * W) c c = 1 := by
    intro c
    have h1 := congrFun (congrFun hZunit c) c
    rw [Matrix.mul_apply, Matrix.one_apply_eq] at h1
    rw [Finset.sum_eq_single c
      (fun k _ hk => by
        rw [show (Vᴴ * W) k c = 0 from commutant_entry_zero hinj hcomm hk, mul_zero])
      (fun hc => absurd (Finset.mem_univ c) hc)] at h1
    rw [Matrix.conjTranspose_apply, Complex.star_def] at h1
    exact h1
  have hWV : W = V * Matrix.diagonal fun c => (Vᴴ * W) c c := by
    have hZd : Vᴴ * W = Matrix.diagonal fun c => (Vᴴ * W) c c := by
      ext x y
      by_cases hxy : x = y
      · subst hxy
        rw [Matrix.diagonal_apply_eq]
      · rw [Matrix.diagonal_apply_ne _ hxy]
        exact commutant_entry_zero hinj hcomm hxy
    calc W = (V * Vᴴ) * W := by rw [hV', Matrix.one_mul]
      _ = V * (Vᴴ * W) := by rw [Matrix.mul_assoc]
      _ = V * Matrix.diagonal fun c => (Vᴴ * W) c c := by conv_lhs => rw [hZd]
  have hentry : W s a = V s a * (Vᴴ * W) a a := by
    have h0 := congrFun (congrFun hWV s) a
    rw [Matrix.mul_diagonal] at h0
    exact h0
  rw [hentry, map_mul]
  linear_combination (V s a * conj' (V s a)) * hz a

omit [Fintype I] [DecidableEq I] in
/-- **`permLogBranch_projOverlap_invariant`.** Changing the logarithm branch of a finite
carrier's interpolation shifts the eigenvalue labels by `2π`-multiples but leaves the
eigenprojectors of a simple-spectrum block unchanged: any two branches diagonalize the
same block with the same labels, so every diagonal-readout overlap
`⟨a|P|a⟩ = Σ_s P_ss |V_sa|²` — the carrier datum `B` that preparation feasibility
consumes — is branch-independent. -/
theorem permLogBranch_projOverlap_invariant {V W : Matrix S S ℂ} {lam : S → ℂ}
    (hV : Vᴴ * V = 1) (hW : Wᴴ * W = 1) (hinj : Function.Injective lam)
    (h : V * Matrix.diagonal lam * Vᴴ = W * Matrix.diagonal lam * Wᴴ)
    (P : S → ℂ) (a : S) :
    ∑ s, P s * (W s a * conj' (W s a)) = ∑ s, P s * (V s a * conj' (V s a)) :=
  Finset.sum_congr rfl fun s _ => by
    rw [simple_spectrum_column_moduli hV hW hinj h s a]

#print axioms sum_range_shift
#print axioms freq_shift
#print axioms freq_pow
#print axioms freq_sum_one
#print axioms freq_sum_card
#print axioms fiberProj_trace
#print axioms stationary_diag_pow
#print axioms stationary_freq_readout
#print axioms psd_diag_real
#print axioms stationary_readout_hull
#print axioms hull_readout_achieved
#print axioms no_representation_outside_hull
#print axioms transitive_freq_const
#print axioms transitive_freq_eq_countMarginal
#print axioms ergodicShell_readout_unique
#print axioms ergodicShell_SRC
#print axioms cycle_eigenvector_overlap
#print axioms commutant_entry_zero
#print axioms simple_spectrum_column_moduli
#print axioms permLogBranch_projOverlap_invariant

end CycleFibreHull
end OIBridge
