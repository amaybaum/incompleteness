/-
  OIBridge/DynamicsGlue.lean — the dynamics glue between the discrete permutation sector
  and the continuous coherent carrier: G1 forces monomial sampled dynamics, and G1 plus
  ergodicity pins the preparation carrier datum B.

  PHASE THREE, ROUND THIRTEEN. The F22 audit isolated the missing existence object as the
  generic-flow carrier datum `B` beyond the permutation shadow; this round identifies the
  missing DYNAMICS condition behind it. The formal layers were genuinely separate: the
  overlap identity ties the coherent branch functional to the classical trajectory
  functional at the level of visible numbers (G0, `intersection_consistent`), while the
  preparation theorems test `p ∈ BΔ` on an abstract `(V, E)` carrier — nothing said that
  some `U_τ = e^{-iHτ}` of that carrier IS the sampled substratum permutation. The glue
  hierarchy, named and separated:

    G0 — observable glue: the coherent and permutation descriptions assign the same
         visible branch probabilities. TOO WEAK to fix `B`: probe F22's two generic
         carriers agree on everything G0-level fixes and disagree on feasibility.

    G1 — diagonal-sector dynamics glue (`DiagonalSectorGlue`): at a physical sampling
         time τ, `U_τ diag(w) U_τ† = P_φ diag(w) P_φ†` for every real diagonal `w` —
         the coherent dynamics does not merely reproduce visible numbers; on the whole
         classical diagonal sector it EXTENDS the substratum permutation.

  §A — G1 IS EXACTLY MONOMIALITY. `diagonalGlue_forces_monomial`: G1 alone — no
  unitarity hypothesis — forces `U_τ = D · P_φ` with `D` a unimodular diagonal: testing
  the glue on the rank-one diagonal indicators makes every column of `U_τ` a phase times
  a coordinate vector, `U_τ|s⟩ = e^{iθ_s}|φ(s)⟩`, with unimodularity falling out of the
  same dyads. `glue_of_monomial` is the converse, so `diagonalGlue_iff_monomial`: the
  sampled coherent dynamics extends the classical diagonal dynamics IFF it is a phased
  permutation.

  §B — G1 PINS THE CARRIER DATUM. For a phased permutation the stationary diagonal is
  still orbit-constant (`monomial_conj_apply`, `diag_invariant_pow`), so the cycle-fibre
  machinery of round twelve applies verbatim (`diag_invariant_freq_readout`): on an
  ergodic shell EVERY `U_τ`-stationary PSD trace-one state reads out exactly the uniform
  counting marginal (`monomial_ergodic_readout_unique`), and every normalized
  eigenvector of `U_τ` has fibre overlaps exactly `m_i / N`
  (`phasedCycle_columnModuli`) — the phases wind around the cycle but cannot move a
  modulus, whatever the logarithm branch and whatever the spectral degeneracies, so no
  simple-spectrum hypothesis is needed anywhere. The capstone:

      ┌────────────────────────────────────────────────────────────────────┐
      │  G1 + ergodic shell  ⟹  physical-flow SRC, with canonical B:      │
      │  every coherent flow genuinely extending the classical diagonal    │
      │  dynamics reads the shell as its counting marginal — existence     │
      │  and uniqueness, independent of phases and logarithm branch.       │
      └────────────────────────────────────────────────────────────────────┘

  (`ergodicShell_SRC_of_dynamicsGlue`.) The countercontrol stands on the other side:
  observable agreement alone does not force SRC — F22's opposite-feasibility carriers
  are both G0-compatible and both fail G1 (probe F24 exhibits the failing indicator).

      ┌────────────────────────────────────────────────────────────────────┐
      │  Observable agreement alone does not force SRC;                    │
      │  diagonal-sector dynamics glue does.                               │
      └────────────────────────────────────────────────────────────────────┘

  THE AUDIT QUESTION, now one line: does OI require G1, or only G0? If a coherent
  completion is a genuine extension of the same classical state dynamics, G1 is the
  natural reading and preparation existence is closed positively for ergodic shells,
  with `B` a theorem. If only observer-visible branch probabilities must agree, G1 is
  additional structure and the F22 underdetermination remains real. That named
  alternative — not a formula for `B_phys` — is the remaining existence premise.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.CycleFibreHull

namespace OIBridge
namespace DynamicsGlue

open Complex Matrix CoherentLift CycleFibreHull
open scoped ComplexOrder

local notation "conj'" => (starRingEnd ℂ)

variable {S I : Type*} [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I]

/-! ### Section A — G1 is exactly monomiality -/

/-- **G1, the diagonal-sector dynamics glue**: at the sampled time, the coherent dynamics
agrees with the substratum permutation on the WHOLE classical diagonal sector, not merely
on visible branch probabilities. -/
def DiagonalSectorGlue (U : Matrix S S ℂ) (φ : Equiv.Perm S) : Prop :=
  ∀ w : S → ℝ, U * Matrix.diagonal (fun s => ((w s : ℝ) : ℂ)) * Uᴴ
    = permMatrix φ * Matrix.diagonal (fun s => ((w s : ℝ) : ℂ)) * (permMatrix φ)ᴴ

omit [Fintype I] [DecidableEq I] in
/-- Entry form of a conjugated diagonal. -/
theorem conj_diag_entry (U : Matrix S S ℂ) (f : S → ℂ) (x y : S) :
    (U * Matrix.diagonal f * Uᴴ) x y = ∑ a, U x a * f a * conj' (U y a) := by
  rw [Matrix.mul_apply]
  refine Finset.sum_congr rfl fun a _ => ?_
  rw [Matrix.mul_diagonal, Matrix.conjTranspose_apply, Complex.star_def]

omit [Fintype I] [DecidableEq I] in
/-- **G1 FORCES MONOMIAL SAMPLED DYNAMICS.** Testing the glue on the rank-one diagonal
indicators alone — no unitarity hypothesis — forces every column of `U` to be a
unimodular phase times a coordinate vector: `U = D · P_φ` with `D` a unimodular
diagonal. -/
theorem diagonalGlue_forces_monomial (U : Matrix S S ℂ) (φ : Equiv.Perm S)
    (hglue : DiagonalSectorGlue U φ) :
    ∃ d : S → ℂ, (∀ x, d x * conj' (d x) = 1)
      ∧ U = Matrix.diagonal d * permMatrix φ := by
  have hcol : ∀ s x y : S, U x s * conj' (U y s)
      = if x = y then (if x = φ s then (1 : ℂ) else 0) else 0 := by
    intro s x y
    have h := congrFun (congrFun (hglue fun t => if t = s then 1 else 0) x) y
    rw [conj_diag_entry, permMatrix_conj_diagonal] at h
    simp only [apply_ite (fun r : ℝ => (r : ℂ)), Complex.ofReal_one,
      Complex.ofReal_zero] at h
    rw [Finset.sum_congr rfl (fun a _ => by
      rw [mul_ite, mul_one, mul_zero, ite_mul, zero_mul]) ,
      Finset.sum_ite_eq_of_mem' Finset.univ s
        (fun a => U x a * conj' (U y a)) (Finset.mem_univ s)] at h
    rw [h, Matrix.diagonal_apply]
    by_cases hxy : x = y
    · rw [if_pos hxy, if_pos hxy]
      by_cases hxs : x = φ s
      · rw [if_pos hxs, if_pos (by rw [hxs, Equiv.symm_apply_apply])]
      · rw [if_neg hxs, if_neg (fun h0 => hxs (by rw [← (Equiv.symm_apply_eq φ).mp h0]))]
    · rw [if_neg hxy, if_neg hxy]
  have hunit : ∀ s, U (φ s) s * conj' (U (φ s) s) = 1 := by
    intro s
    have h0 := hcol s (φ s) (φ s)
    rwa [if_pos rfl, if_pos rfl] at h0
  have hzero : ∀ s x, x ≠ φ s → U x s = 0 := by
    intro s x hx
    have h1 := hcol s x (φ s)
    by_cases hxy : x = φ s
    · exact absurd hxy hx
    · rw [if_neg hxy] at h1
      have h2 : conj' (U (φ s) s) ≠ 0 := by
        intro h0
        have h3 := hunit s
        rw [h0, mul_zero] at h3
        exact one_ne_zero h3.symm
      rcases mul_eq_zero.mp h1 with h | h
      · exact h
      · exact absurd h h2
  refine ⟨fun x => U x (φ.symm x), fun x => ?_, ?_⟩
  · have h0 := hunit (φ.symm x)
    rwa [Equiv.apply_symm_apply] at h0
  · ext x s
    rw [Matrix.diagonal_mul, permMatrix]
    show U x s = U x (φ.symm x) * (if φ s = x then 1 else 0)
    by_cases hxs : φ s = x
    · rw [if_pos hxs, mul_one]
      congr 1
      rw [← hxs, Equiv.symm_apply_apply]
    · rw [if_neg hxs, mul_zero]
      exact hzero s x fun h0 => hxs h0.symm

omit [Fintype I] [DecidableEq I] in
/-- The entry form of a monomial conjugation. -/
theorem monomial_conj_apply (d : S → ℂ) (φ : Equiv.Perm S) (Y : Matrix S S ℂ) (x y : S) :
    ((Matrix.diagonal d * permMatrix φ) * Y * (Matrix.diagonal d * permMatrix φ)ᴴ) x y
      = d x * conj' (d y) * Y (φ.symm x) (φ.symm y) := by
  have hassoc : (Matrix.diagonal d * permMatrix φ) * Y
        * (Matrix.diagonal d * permMatrix φ)ᴴ
      = Matrix.diagonal d * (permMatrix φ * Y * (permMatrix φ)ᴴ)
        * (Matrix.diagonal d)ᴴ := by
    rw [Matrix.conjTranspose_mul]
    noncomm_ring
  rw [hassoc, Matrix.diagonal_conjTranspose, Matrix.mul_diagonal, Matrix.diagonal_mul,
    permMatrix_conj_apply, Pi.star_apply, Complex.star_def]
  ring

omit [Fintype I] [DecidableEq I] in
/-- **THE CONVERSE: monomial dynamics satisfies the glue.** With `glue_forces_monomial`,
G1 is EXACTLY monomiality. -/
theorem glue_of_monomial (d : S → ℂ) (φ : Equiv.Perm S)
    (hd : ∀ x, d x * conj' (d x) = 1) :
    DiagonalSectorGlue (Matrix.diagonal d * permMatrix φ) φ := by
  intro w
  ext x y
  rw [monomial_conj_apply, permMatrix_conj_diagonal, Matrix.diagonal_apply,
    Matrix.diagonal_apply]
  by_cases hxy : x = y
  · subst hxy
    rw [if_pos rfl, if_pos rfl]
    linear_combination ((w (φ.symm x) : ℝ) : ℂ) * hd x
  · rw [if_neg (fun h0 => hxy (φ.symm.injective h0)), if_neg hxy, mul_zero]

omit [Fintype I] [DecidableEq I] in
/-- **G1 ⟺ MONOMIAL.** The sampled coherent dynamics extends the classical diagonal
dynamics if and only if it is a phased permutation. -/
theorem diagonalGlue_iff_monomial (U : Matrix S S ℂ) (φ : Equiv.Perm S) :
    DiagonalSectorGlue U φ
      ↔ ∃ d : S → ℂ, (∀ x, d x * conj' (d x) = 1)
          ∧ U = Matrix.diagonal d * permMatrix φ := by
  constructor
  · exact diagonalGlue_forces_monomial U φ
  · rintro ⟨d, hd, rfl⟩
    exact glue_of_monomial d φ hd

omit [Fintype I] [DecidableEq I] in
/-- A phased permutation is unitary. -/
theorem monomial_unitary (d : S → ℂ) (φ : Equiv.Perm S)
    (hd : ∀ x, d x * conj' (d x) = 1) :
    (Matrix.diagonal d * permMatrix φ) * (Matrix.diagonal d * permMatrix φ)ᴴ = 1 := by
  rw [Matrix.conjTranspose_mul]
  calc Matrix.diagonal d * permMatrix φ * ((permMatrix φ)ᴴ * (Matrix.diagonal d)ᴴ)
      = Matrix.diagonal d * (permMatrix φ * (permMatrix φ)ᴴ) * (Matrix.diagonal d)ᴴ := by
        noncomm_ring
    _ = Matrix.diagonal d * (Matrix.diagonal d)ᴴ := by
        rw [permMatrix_unitary, Matrix.mul_one]
    _ = 1 := by
        rw [Matrix.diagonal_conjTranspose, Matrix.diagonal_mul_diagonal]
        rw [show (fun x => d x * star d x) = fun _ => (1 : ℂ) from
          funext fun x => hd x]
        exact Matrix.diagonal_one

/-! ### Section B — G1 pins the carrier datum -/

omit [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- Orbit constancy propagates through powers, for any orbit-invariant function. -/
theorem diag_invariant_pow (φ : Equiv.Perm S) (g : S → ℂ)
    (hg : ∀ s, g (φ s) = g s) (k : ℕ) (s : S) : g ((φ ^ k) s) = g s := by
  induction k with
  | zero => rw [pow_zero]; rfl
  | succ k ih =>
      rw [pow_succ', Equiv.Perm.mul_apply, hg]
      exact ih

omit [DecidableEq S] [Fintype I] in
/-- The cycle-fibre readout identity from diagonal orbit-invariance alone: the general
core that both the permutation and the phased-permutation carriers feed. -/
theorem diag_invariant_freq_readout (φ : Equiv.Perm S) (vis : S → I) (ρ : Matrix S S ℂ)
    (hdiag : ∀ s, ρ (φ s) (φ s) = ρ s s) (i : I) :
    ∑ s, (ρ s s).re * freq φ vis i s = ∑ s, if vis s = i then (ρ s s).re else 0 := by
  have hpow : ∀ (k : ℕ) (s : S), ρ ((φ ^ k) s) ((φ ^ k) s) = ρ s s :=
    fun k s => diag_invariant_pow φ (fun t => ρ t t) hdiag k s
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
    have hdd := hpow k (((φ ^ k)⁻¹ : Equiv.Perm S) t)
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

omit [Fintype I] in
/-- **UNDER G1, THE ERGODIC READOUT IS PINNED.** Every PSD trace-one state stationary
under a phased permutation of a transitive shell reads out exactly the uniform counting
marginal — independent of the phases, hence of the logarithm branch and of any spectral
degeneracy. -/
theorem monomial_ergodic_readout_unique [Nonempty S] (d : S → ℂ) (φ : Equiv.Perm S)
    (vis : S → I) (hd : ∀ x, d x * conj' (d x) = 1)
    (htrans : ∀ s t : S, ∃ k : ℕ, (φ ^ k) s = t) (ρ : Matrix S S ℂ)
    (hpsd : ρ.PosSemidef) (htr : Matrix.trace ρ = 1)
    (hstat : (Matrix.diagonal d * permMatrix φ) * ρ
      * (Matrix.diagonal d * permMatrix φ)ᴴ = ρ) (i : I) :
    Matrix.trace (fiberProj vis i * ρ) = ((countMarginal vis i : ℝ) : ℂ) := by
  have hdiag : ∀ s, ρ (φ s) (φ s) = ρ s s := by
    intro s
    have h2 := congrFun (congrFun hstat (φ s)) (φ s)
    rw [monomial_conj_apply, Equiv.symm_apply_apply, hd (φ s), one_mul] at h2
    exact h2.symm
  have hfr := diag_invariant_freq_readout φ vis ρ hdiag i
  have hconst : (∑ s, (ρ s s).re * freq φ vis i s)
      = (∑ s, (ρ s s).re) * countMarginal vis i := by
    rw [Finset.sum_mul]
    exact Finset.sum_congr rfl fun s _ => by
      rw [transitive_freq_eq_countMarginal φ vis htrans i s]
  rw [hconst] at hfr
  have hsum : (∑ s, (ρ s s).re) = 1 := by
    have h1 : Matrix.trace ρ = ((∑ s, (ρ s s).re : ℝ) : ℂ) := by
      rw [Matrix.trace]
      push_cast
      exact Finset.sum_congr rfl fun s _ => psd_diag_real ρ hpsd s
    rw [htr] at h1
    exact_mod_cast h1.symm
  rw [hsum, one_mul] at hfr
  have hgoal : (∑ s, if vis s = i then ρ s s else 0)
      = ((∑ s, if vis s = i then (ρ s s).re else 0 : ℝ) : ℂ) := by
    push_cast
    refine Finset.sum_congr rfl fun s _ => ?_
    by_cases hc : vis s = i
    · rw [if_pos hc, if_pos hc]
      exact psd_diag_real ρ hpsd s
    · rw [if_neg hc, if_neg hc, Complex.ofReal_zero]
  rw [fiberProj_trace, hgoal, hfr]

omit [Fintype I] in
/-- **THE COLUMN-MODULI THEOREM.** Every normalized eigenvector of a phased transitive
permutation has fibre overlaps exactly `m_i / N`: the phases wind around the cycle but
cannot move a modulus. The eigenvalue equation is `d x · v(φ⁻¹ x) = μ · v(x)`, which is
`(D P_φ) *ᵥ v = μ • v` read entrywise; no simple-spectrum hypothesis is needed. -/
theorem phasedCycle_columnModuli [Nonempty S] (d : S → ℂ) (φ : Equiv.Perm S)
    (vis : S → I) (hd : ∀ x, d x * conj' (d x) = 1)
    (htrans : ∀ s t : S, ∃ k : ℕ, (φ ^ k) s = t)
    (v : S → ℂ) (μ : ℂ) (hv : ∀ x : S, d x * v (φ.symm x) = μ * v x)
    (hnorm : (∑ s, v s * conj' (v s)) = 1) (i : I) :
    (∑ s, if vis s = i then v s * conj' (v s) else 0)
      = ((countMarginal vis i : ℝ) : ℂ) := by
  have hμ : μ * conj' μ = 1 := by
    have h1 : (∑ p, v (φ.symm p) * conj' (v (φ.symm p))) = 1 :=
      (Equiv.sum_comp (φ.symm : Equiv.Perm S) fun s => v s * conj' (v s)).trans hnorm
    have h2 : (∑ p, (d p * v (φ.symm p)) * conj' (d p * v (φ.symm p)))
        = ∑ p, v (φ.symm p) * conj' (v (φ.symm p)) := by
      refine Finset.sum_congr rfl fun p _ => ?_
      rw [map_mul]
      linear_combination (v (φ.symm p) * conj' (v (φ.symm p))) * hd p
    have h3 : (∑ p, (d p * v (φ.symm p)) * conj' (d p * v (φ.symm p)))
        = (μ * conj' μ) * ∑ p, v p * conj' (v p) := by
      rw [Finset.mul_sum]
      refine Finset.sum_congr rfl fun p _ => ?_
      rw [hv p, map_mul]
      ring
    rw [h2, h1] at h3
    rw [hnorm, mul_one] at h3
    exact h3.symm
  have hentry : ∀ p q, Matrix.vecMulVec v (star v) p q = v p * conj' (v q) := by
    intro p q
    rw [Matrix.vecMulVec_apply, Pi.star_apply, Complex.star_def]
  have hpsd : (Matrix.vecMulVec v (star v)).PosSemidef :=
    Matrix.posSemidef_vecMulVec_self_star v
  have htr : Matrix.trace (Matrix.vecMulVec v (star v)) = 1 := by
    rw [Matrix.trace]
    rw [Finset.sum_congr rfl fun s _ => by rw [Matrix.diag_apply, hentry]]
    exact hnorm
  have hstat : (Matrix.diagonal d * permMatrix φ) * Matrix.vecMulVec v (star v)
      * (Matrix.diagonal d * permMatrix φ)ᴴ = Matrix.vecMulVec v (star v) := by
    ext p q
    rw [monomial_conj_apply, hentry, hentry]
    have hp := hv p
    have hq := hv q
    calc d p * conj' (d q) * (v (φ.symm p) * conj' (v (φ.symm q)))
        = (d p * v (φ.symm p)) * conj' (d q * v (φ.symm q)) := by
          rw [map_mul]; ring
      _ = (μ * v p) * conj' (μ * v q) := by rw [hp, hq]
      _ = (μ * conj' μ) * (v p * conj' (v q)) := by rw [map_mul]; ring
      _ = v p * conj' (v q) := by rw [hμ, one_mul]
  have hread := monomial_ergodic_readout_unique d φ vis hd htrans _ hpsd htr hstat i
  rw [fiberProj_trace] at hread
  rw [← hread]
  refine Finset.sum_congr rfl fun s _ => ?_
  by_cases hc : vis s = i
  · rw [if_pos hc, if_pos hc, hentry]
  · rw [if_neg hc, if_neg hc]

omit [Fintype I] in
/-- **`ergodicShell_SRC_of_dynamicsGlue` — the capstone.** G1 plus an ergodic shell
closes physical-flow SRC with a CANONICAL carrier datum: any sampled coherent dynamics
genuinely extending the classical diagonal dynamics admits the classical shell ensemble
as a stationary representation reading out the uniform counting marginal, and EVERY
stationary representation reads out exactly that marginal — existence and uniqueness,
independent of the phases and of the logarithm branch. Observable agreement alone (G0)
does not force this: the F22 carriers are G0-compatible with opposite feasibility. -/
theorem ergodicShell_SRC_of_dynamicsGlue [Nonempty S] (U : Matrix S S ℂ)
    (φ : Equiv.Perm S) (vis : S → I)
    (htrans : ∀ s t : S, ∃ k : ℕ, (φ ^ k) s = t)
    (hglue : DiagonalSectorGlue U φ) :
    (∃ ρ : Matrix S S ℂ, ρ.PosSemidef ∧ Matrix.trace ρ = 1
        ∧ U * ρ * Uᴴ = ρ
        ∧ ∀ i, Matrix.trace (fiberProj vis i * ρ) = ((countMarginal vis i : ℝ) : ℂ))
    ∧ ∀ ρ : Matrix S S ℂ, ρ.PosSemidef → Matrix.trace ρ = 1
        → U * ρ * Uᴴ = ρ
        → ∀ i, Matrix.trace (fiberProj vis i * ρ) = ((countMarginal vis i : ℝ) : ℂ) := by
  obtain ⟨d, hd, rfl⟩ := diagonalGlue_forces_monomial U φ hglue
  have hN : (0 : ℝ) < (Fintype.card S : ℝ) := Nat.cast_pos.mpr Fintype.card_pos
  constructor
  · refine ⟨Matrix.diagonal fun _ => (((Fintype.card S : ℝ)⁻¹ : ℝ) : ℂ), ?_, ?_, ?_, ?_⟩
    · exact Matrix.posSemidef_diagonal_iff.mpr fun s =>
        Complex.zero_le_real.mpr (inv_nonneg.mpr hN.le)
    · rw [Matrix.trace_diagonal, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
      push_cast
      rw [mul_inv_cancel₀ (by exact_mod_cast hN.ne' : ((Fintype.card S : ℂ)) ≠ 0)]
    · ext x y
      rw [monomial_conj_apply, Matrix.diagonal_apply, Matrix.diagonal_apply]
      by_cases hxy : x = y
      · subst hxy
        rw [if_pos rfl, if_pos rfl]
        linear_combination (((Fintype.card S : ℝ)⁻¹ : ℝ) : ℂ) * hd x
      · rw [if_neg (fun h0 => hxy (φ.symm.injective h0)), if_neg hxy, mul_zero]
    · intro i
      rw [fiberProj_trace]
      simp only [Matrix.diagonal_apply_eq]
      rw [← Finset.sum_filter, Finset.sum_const, nsmul_eq_mul, countMarginal]
      push_cast
      ring
  · exact fun ρ h1 h2 h3 i =>
      monomial_ergodic_readout_unique d φ vis hd htrans ρ h1 h2 h3 i

#print axioms conj_diag_entry
#print axioms diagonalGlue_forces_monomial
#print axioms monomial_conj_apply
#print axioms glue_of_monomial
#print axioms diagonalGlue_iff_monomial
#print axioms monomial_unitary
#print axioms diag_invariant_pow
#print axioms diag_invariant_freq_readout
#print axioms monomial_ergodic_readout_unique
#print axioms phasedCycle_columnModuli
#print axioms ergodicShell_SRC_of_dynamicsGlue

end DynamicsGlue
end OIBridge
