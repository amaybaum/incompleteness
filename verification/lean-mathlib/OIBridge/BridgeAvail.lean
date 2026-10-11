/-
  OIBridge/BridgeAvail.lean — design module of the research thread `research/bridge`
  (round 4, node B14). Not certified. Built on the disposable branch `dev-bridge/r4-avail` only;
  not for merge.

  Availability in context (A), stated in the kernel's operational vocabulary. A token operator `U`
  (2 × 2, acting on the second token) is AVAILABLE ON THE PAIR at level `n` in the theory an
  architecture generates when the one-outcome conjugation by `pairOp U n = (1 ⊗ U) ⊗ 1ₙ` is available
  on the pair carrier `Fin 2 × Fin 2` at level `n` (`PairAvailAt`). By the definition of `genTheory`
  this is `InstAvail` at the carrier `(Fin 2 × Fin 2) × Fin n`: every protocol (`op`, `readout`,
  `coarse`, `bind`, `discard`), with the class's ancilla blocks and relabellings of members at every
  level. `TokenAvailAt` is the same on the token alone (`tokOp U n = U ⊗ 1ₙ`).

  The two token operations, through the two-token dictionary:
    `zPh = diag(1, w)`, `w = 3/5 + (4/5) i` — the operator of `actT R_z(θ₀)`, `cos θ₀ = 3/5`;
    `uJ  = (1 − i(X + Y + Z))/2`           — the operator of `actT J`, `J = cycEquiv`.

  Proved here:
    §A  the operators, their entries and unitarity; the pair and token operators, their isometry, and
        product behaviour (`pairOp_prod`);
    §B  the ray step, by the kernel's `exists_scaled_mem_of_instAvail_unitary`
        (MicroscopicReversibility.lean:251): for an architecture, if a unitary conjugation is
        available at a carrier, a nonzero multiple of its operator is a member of the class there;
    §C  the fourth-root lattice (`QuartLattice`: submonomial, any two nonzero entries with equal fourth
        powers). The stated access `permClass` lies on it (`permClass_quartLattice`), and so does its
        closure with the quarter phase, `MixR ∅`, by induction over the eight constructors of `MixR`,
        ancilla blocks and relabellings included (`mixEmpty_quartLattice`);
    §D  the decision: on the lattice neither operator is available at any positive level, on the
        pair or on the token (`not_pairAvail_zPh_of_lattice`, `not_tokenAvail_zPh_of_lattice`); in
        every submonomial class `uJ` is not (`not_pairAvail_uJ_of_submonomial`,
        `not_tokenAvail_uJ_of_submonomial`); the monomial interface makes `zPh` available at every
        level (`substratum_pairAvail_zPh`, `substratum_tokenAvail_zPh`); the full class makes both
        available (`fullClass_supplies`);
    §E  the two stabilities of `MixR ∅`, by the kernel's proofs for the fixed-gate class
        (DiscreteCompletion.lean:1861, :1890) at `D = ∅`, and `DerivedOI` for its theory
        (`mixEmpty_derivedOI`);
    §F  the countermodels with their kernel facts: the stated access satisfies `SourcedOI` and the
        sealed core and refutes both operations (`statedAccess_obstruction`); with the quarter phase
        it satisfies `DerivedOI` and refutes both (`quarterAccess_obstruction`); the monomial interface
        satisfies `DerivedOICore`, supplies `zPh` and refutes `uJ` (`monomialInterface_split`);
    §G  controls: the NOT is available on the pair in the stated access at every level
        (`statedAccess_pairAvail_nflip`); the quarter phase's pair operator lies on the lattice
        (`quarter_on_lattice`), so the lattice excludes `zPh` by its angle.

  Nothing here sources an operation, a pair cone, (A) or the transfer clause. The pair carrier is the
  kernel's Kronecker composite; no statement here is about a pair cone on `W 3`.

  Kernel check (dev branch):  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.StateMixingCoupling
import OIBridge.MicroscopicReversibility
import OIBridge.ReferenceExtension
import OIBridge.SubstratumInterfaceAudit
import OIBridge.StructuralClosure
import OIBridge.SubstratumSource
import OIBridge.SpectatorBridge
import OIBridge.LieRankSource
import OIBridge.RouteB
import OIBridge.PolarizationClosure
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace OIBridge
namespace BridgeAvail

open Matrix MonoidalCompletion InterventionLocality StructuralClosure SubstratumInterface
  SubstratumInterfaceAudit StateMixingCoupling RouteB OIRealization MicroReversibility

/-! ### §A — the operators -/

/-- The 3-4-5 phase `w = 3/5 + (4/5) i`. -/
noncomputable def w345 : ℂ := 3 / 5 + 4 / 5 * Complex.I

/-- The token operator of `R_z(θ₀)`, `diag(1, w)`, `cos θ₀ = 3/5`. -/
noncomputable def zPh : Matrix (Fin 2) (Fin 2) ℂ := Matrix.diagonal ![1, w345]

/-- The token operator of `J = cycEquiv`: `(1 − i(X + Y + Z))/2`. -/
noncomputable def uJ : Matrix (Fin 2) (Fin 2) ℂ :=
  !![(1 - Complex.I) / 2, (-1 - Complex.I) / 2; (1 - Complex.I) / 2, (1 + Complex.I) / 2]

/-- The token operator of the NOT: the exchange of the two values. -/
noncomputable def nflipU : Matrix (Fin 2) (Fin 2) ℂ :=
  CoherentLift.permMatrix (Equiv.swap (0 : Fin 2) 1)

/-- The quarter phase `diag(1, i)` (the countercontrol of §G). -/
noncomputable def sPh : Matrix (Fin 2) (Fin 2) ℂ := Matrix.diagonal ![1, Complex.I]

/-- The pair operator: `U` on the second token, the first token and an `n`-level ancilla
spectators. -/
noncomputable def pairOp (U : Matrix (Fin 2) (Fin 2) ℂ) (n : ℕ) :
    Matrix ((Fin 2 × Fin 2) × Fin n) ((Fin 2 × Fin 2) × Fin n) ℂ :=
  tensorOf (tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) U) (1 : Matrix (Fin n) (Fin n) ℂ)

/-- The token operator at level `n`: `U` with an `n`-level ancilla spectator. -/
noncomputable def tokOp (U : Matrix (Fin 2) (Fin 2) ℂ) (n : ℕ) :
    Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ :=
  tensorOf U (1 : Matrix (Fin n) (Fin n) ℂ)

/-- **(A) IN THE KERNEL'S VOCABULARY**: the token operator `U` is available on the pair at level
`n` in the theory the architecture generates — instrument realization at the carrier
`(Fin 2 × Fin 2) × Fin n`, by every protocol, with the class's blocks and relabellings of members at
every level. -/
def PairAvailAt (𝓘 : ImplementationClass) (arch : Architecture 𝓘) (U : Matrix (Fin 2) (Fin 2) ℂ)
    (n : ℕ) : Prop :=
  (genTheory 𝓘 arch (Fin 2 × Fin 2)).availExt n Unit (fun _ => conjChannel (pairOp U n))

/-- The token-only form: `U` available on the token alone at level `n`. -/
def TokenAvailAt (𝓘 : ImplementationClass) (arch : Architecture 𝓘) (U : Matrix (Fin 2) (Fin 2) ℂ)
    (n : ℕ) : Prop :=
  (genTheory 𝓘 arch (Fin 2)).availExt n Unit (fun _ => conjChannel (tokOp U n))

/-- `star w = 3/5 − (4/5) i`. -/
theorem w345_star : star w345 = 3 / 5 - 4 / 5 * Complex.I := by
  unfold w345
  rw [Complex.star_def]
  simp only [map_add, map_mul, map_div₀, map_ofNat, Complex.conj_I] <;> ring

/-- `|w|² = 1`. -/
theorem w345_star_mul : star w345 * w345 = 1 := by
  rw [w345_star]
  unfold w345
  linear_combination (-16 / 25 : ℂ) * Complex.I_sq

theorem w345_ne_zero : w345 ≠ 0 := by
  intro h
  have h1 := w345_star_mul
  rw [h, mul_zero] at h1
  exact zero_ne_one h1

/-- `w⁴ = (−527 − 336 i)/625`. -/
theorem w345_pow_four : w345 ^ 4 = -527 / 625 - 336 / 625 * Complex.I := by
  unfold w345
  linear_combination
    (6 * (3 / 5 : ℂ) ^ 2 * (4 / 5) ^ 2 + 4 * (3 / 5) * (4 / 5) ^ 3 * Complex.I
      + (4 / 5) ^ 4 * (Complex.I ^ 2 - 1)) * Complex.I_sq

/-- `w` is not a fourth root of unity. -/
theorem w345_pow_four_ne_one : w345 ^ 4 ≠ 1 := by
  rw [w345_pow_four]
  intro h
  have hI : Complex.I = -24 / 7 := by linear_combination (-625 / 336 : ℂ) * h
  have h2 := Complex.I_sq
  rw [hI] at h2
  norm_num at h2

theorem zPh_00 : zPh 0 0 = 1 := by
  first
  | rfl
  | simp [zPh]

theorem zPh_11 : zPh 1 1 = w345 := by
  first
  | rfl
  | simp [zPh]

theorem zPh_00_ne : zPh 0 0 ≠ 0 := by
  rw [zPh_00]
  exact one_ne_zero

theorem zPh_11_ne : zPh 1 1 ≠ 0 := by
  rw [zPh_11]
  exact w345_ne_zero

theorem zPh_pow_ne : zPh 0 0 ^ 4 ≠ zPh 1 1 ^ 4 := by
  rw [zPh_00, zPh_11, one_pow]
  exact fun h => w345_pow_four_ne_one h.symm

theorem zPh_unitary : zPhᴴ * zPh = 1 := by
  unfold zPh
  rw [Matrix.diagonal_conjTranspose, Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_one]
  refine congrArg Matrix.diagonal (funext fun i => ?_)
  fin_cases i
  · show star (1 : ℂ) * 1 = 1
    rw [star_one, one_mul]
  · show star w345 * w345 = 1
    exact w345_star_mul

theorem uJ_00 : uJ 0 0 = (1 - Complex.I) / 2 := by
  first
  | rfl
  | simp [uJ]

theorem uJ_01 : uJ 0 1 = (-1 - Complex.I) / 2 := by
  first
  | rfl
  | simp [uJ]

theorem uJ_00_ne : uJ 0 0 ≠ 0 := by
  rw [uJ_00]
  intro h
  have hI : Complex.I = 1 := by linear_combination (-2 : ℂ) * h
  have h2 := Complex.I_sq
  rw [hI] at h2
  norm_num at h2

theorem uJ_01_ne : uJ 0 1 ≠ 0 := by
  rw [uJ_01]
  intro h
  have hI : Complex.I = -1 := by linear_combination (-2 : ℂ) * h
  have h2 := Complex.I_sq
  rw [hI] at h2
  norm_num at h2

theorem uJ_star_a : star ((1 - Complex.I) / 2) = (1 + Complex.I) / 2 := by
  rw [Complex.star_def]
  simp only [map_div₀, map_sub, map_one, map_ofNat, Complex.conj_I] <;> ring

theorem uJ_star_b : star ((-1 - Complex.I) / 2) = (-1 + Complex.I) / 2 := by
  rw [Complex.star_def]
  simp only [map_div₀, map_sub, map_neg, map_one, map_ofNat, Complex.conj_I] <;> ring

theorem uJ_star_c : star ((1 + Complex.I) / 2) = (1 - Complex.I) / 2 := by
  rw [Complex.star_def]
  simp only [map_div₀, map_add, map_one, map_ofNat, Complex.conj_I] <;> ring

/-- `uJ` is unitary: entry by entry, `(uJᴴ uJ) i j = Σₖ star (uJ k i) · uJ k j`. -/
theorem uJ_unitary : uJᴴ * uJ = 1 := by
  ext i j
  rw [Matrix.mul_apply, Fin.sum_univ_two]
  fin_cases i <;> fin_cases j
  · show star ((1 - Complex.I) / 2) * ((1 - Complex.I) / 2)
        + star ((1 - Complex.I) / 2) * ((1 - Complex.I) / 2) = 1
    rw [uJ_star_a]
    linear_combination (-1 / 2 : ℂ) * Complex.I_sq
  · show star ((1 - Complex.I) / 2) * ((-1 - Complex.I) / 2)
        + star ((1 - Complex.I) / 2) * ((1 + Complex.I) / 2) = 0
    rw [uJ_star_a]
    ring
  · show star ((-1 - Complex.I) / 2) * ((1 - Complex.I) / 2)
        + star ((1 + Complex.I) / 2) * ((1 - Complex.I) / 2) = 0
    rw [uJ_star_b, uJ_star_c]
    ring
  · show star ((-1 - Complex.I) / 2) * ((-1 - Complex.I) / 2)
        + star ((1 + Complex.I) / 2) * ((1 + Complex.I) / 2) = 1
    rw [uJ_star_b, uJ_star_c]
    linear_combination (-1 / 2 : ℂ) * Complex.I_sq

theorem pairOp_apply_same (U : Matrix (Fin 2) (Fin 2) ℂ) {n : ℕ} (b b' : Fin 2) (k : Fin n) :
    pairOp U n ((0, b), k) ((0, b'), k) = U b b' := by
  simp [pairOp, tensorOf_apply]

theorem tokOp_apply_same (U : Matrix (Fin 2) (Fin 2) ℂ) {n : ℕ} (b b' : Fin 2) (k : Fin n) :
    tokOp U n (b, k) (b', k) = U b b' := by
  simp [tokOp, tensorOf_apply]

theorem pairOp_isometry {U : Matrix (Fin 2) (Fin 2) ℂ} (hU : Uᴴ * U = 1) (n : ℕ) :
    (pairOp U n)ᴴ * pairOp U n = 1 := by
  simp only [pairOp, tensorOf_conjTranspose, tensorOf_mul', Matrix.conjTranspose_one,
    Matrix.one_mul, hU, ReferenceExtension.tensorOf_one_one]

theorem tokOp_isometry {U : Matrix (Fin 2) (Fin 2) ℂ} (hU : Uᴴ * U = 1) (n : ℕ) :
    (tokOp U n)ᴴ * tokOp U n = 1 := by
  simp only [tokOp, tensorOf_conjTranspose, tensorOf_mul', Matrix.conjTranspose_one,
    Matrix.one_mul, hU, ReferenceExtension.tensorOf_one_one]

/-- **(P), PRODUCT BEHAVIOUR**: the pair operator acts on a product `ρ ⊗ σ ⊗ τ` by `U` on the second
factor alone. -/
theorem pairOp_prod (U : Matrix (Fin 2) (Fin 2) ℂ) (n : ℕ) (ρ σ : Matrix (Fin 2) (Fin 2) ℂ)
    (τ : Matrix (Fin n) (Fin n) ℂ) :
    conjChannel (pairOp U n) (tensorOf (tensorOf ρ σ) τ)
      = tensorOf (tensorOf ρ (U * σ * Uᴴ)) τ := by
  simp only [AncillaClosure.conjChannel_apply, pairOp, tensorOf_conjTranspose, tensorOf_mul',
    Matrix.conjTranspose_one, Matrix.one_mul, Matrix.mul_one]

/-! ### §B — the ray step

For an architecture, an available unitary conjugation has a nonzero multiple of its operator in the
class at that carrier: the kernel's `MicroReversibility.exists_scaled_mem_of_instAvail_unitary`
(MicroscopicReversibility.lean:251), used below as it stands. It covers every protocol, since
every branch of every instrument-realized family is a sum of conjugations by members
(`realized_of_instAvail`) and every Kraus operator of a unitary conjugation lies on its ray
(`kraus_of_conj_unitary`). -/

/-! ### §C — the fourth-root lattice -/

/-- Any two nonzero entries have equal fourth powers: their ratio is a fourth root of unity. -/
def QuartEq {T : Type} (K : Matrix T T ℂ) : Prop :=
  ∀ i j k l, K i j ≠ 0 → K k l ≠ 0 → K i j ^ 4 = K k l ^ 4

/-- **A CLASS ON THE FOURTH-ROOT LATTICE**: every member is submonomial with `QuartEq`. -/
def QuartLattice (𝓘 : ImplementationClass) : Prop :=
  ∀ (T : Type) [Fintype T] [DecidableEq T] (K : Matrix T T ℂ), 𝓘 T K → IsSubmonomial K ∧ QuartEq K

theorem quart_of_scaled {T : Type} {K : Matrix T T ℂ} (h : IsScaledPartialPerm K) : QuartEq K := by
  obtain ⟨-, c, -, hc⟩ := h
  exact fun i j k l h1 h2 => by rw [hc i j h1, hc k l h2]

/-- **THE STATED ACCESS LIES ON THE LATTICE**: the nonzero entries of a scaled partial permutation
are all equal. -/
theorem permClass_quartLattice : QuartLattice permClass := by
  intro T _ _ K h
  obtain ⟨hsub, hrest⟩ := (h : IsScaledPartialPerm K)
  exact ⟨hsub, quart_of_scaled ⟨hsub, hrest⟩⟩

/-- A nonzero entry of a submonomial row selects the one term of the product. -/
theorem submonomial_mul_apply {T : Type} [Fintype T] {K L : Matrix T T ℂ} (hK : IsSubmonomial K)
    {i j m : T} (hm : K i m ≠ 0) : (K * L) i j = K i m * L m j := by
  rw [Matrix.mul_apply, Finset.sum_eq_single m]
  · intro m' _ hm'
    by_cases h1 : K i m' = 0
    · rw [h1, zero_mul]
    · exact absurd (hK.1 _ _ _ h1 hm) hm'
  · intro h
    exact absurd (Finset.mem_univ m) h

/-- The quarter phase gate lies on the lattice: its nonzero entries are `1` and `i`. -/
theorem phaseGate_quart {S : Type} [Fintype S] [DecidableEq S] (p : S) :
    QuartEq (LieRankSource.phaseGate p) := by
  have key : ∀ i j, LieRankSource.phaseGate p i j ≠ 0 → LieRankSource.phaseGate p i j ^ 4 = 1 := by
    intro i j h
    by_cases hij : i = j
    · subst hij
      simp only [LieRankSource.phaseGate, Matrix.diagonal_apply_eq]
      split_ifs
      · exact Complex.I_pow_four
      · exact one_pow 4
    · exfalso
      apply h
      simp only [LieRankSource.phaseGate]
      exact Matrix.diagonal_apply_ne _ hij
  exact fun i j k l h1 h2 => by rw [key i j h1, key k l h2]

/-- **THE STATED ACCESS WITH THE QUARTER PHASE LIES ON THE LATTICE**, by induction over the eight
constructors of `MixR ∅`: blocks and relabellings of members at every level included; the datum
constructor is empty at `D = ∅`. -/
theorem mixEmpty_quartLattice : QuartLattice (MixR (∅ : Set ℝ)) := by
  intro T _ _ K h
  induction h with
  | perm K h =>
    obtain ⟨hsub, c, -, hc⟩ := h
    exact ⟨hsub, fun i j k l h1 h2 => by rw [hc i j h1, hc k l h2]⟩
  | phase n p =>
    refine ⟨?_, phaseGate_quart p⟩
    unfold LieRankSource.phaseGate
    exact submonomial_diagonal _
  | mix n θ hθ => exact absurd hθ (Set.notMem_empty θ)
  | mul K L _ _ ihK ihL =>
    refine ⟨submonomial_mul ihK.1 ihL.1, fun i j k l h1 h2 => ?_⟩
    obtain ⟨m, hm1, hm2⟩ := mul_entry_ne_zero h1
    obtain ⟨m', hm1', hm2'⟩ := mul_entry_ne_zero h2
    rw [submonomial_mul_apply ihK.1 hm1, submonomial_mul_apply ihK.1 hm1', mul_pow, mul_pow,
      ihK.2 i m k m' hm1 hm1', ihL.2 m j m' l hm2 hm2']
  | smul a K _ _ ih =>
    refine ⟨submonomial_smul a ih.1, fun i j k l h1 h2 => ?_⟩
    simp only [Matrix.smul_apply, smul_eq_mul] at h1 h2 ⊢
    rw [mul_pow, mul_pow, ih.2 i j k l (mul_ne_zero_iff.mp h1).2 (mul_ne_zero_iff.mp h2).2]
  | proj m k =>
    exact ⟨submonomial_diagonal _, quart_of_scaled (scaled_diagonal_indicator _)⟩
  | block m K f e _ ih =>
    exact ⟨submonomial_block ih.1 f e, fun i j k l h1 h2 => ih.2 (i, f) (j, e) (k, f) (l, e) h1 h2⟩
  | relabel e K _ ih =>
    refine ⟨submonomial_reindex e ih.1, fun i j k l h1 h2 => ?_⟩
    simp only [Matrix.reindex_apply, Matrix.submatrix_apply] at h1 h2 ⊢
    exact ih.2 _ _ _ _ h1 h2

/-! ### §D — the decision -/

/-- Two nonzero diagonal entries with distinct fourth powers exclude `QuartEq` for every nonzero
multiple. -/
theorem not_quart_smul {T : Type} {V : Matrix T T ℂ} {p q : T} {x y : ℂ} (hp : V p p = x)
    (hq : V q q = y) (hx : x ≠ 0) (hy : y ≠ 0) (hxy : x ^ 4 ≠ y ^ 4) {a : ℂ} (ha : a ≠ 0) :
    ¬ QuartEq (a • V) := by
  intro h
  have h1 : (a • V) p p ≠ 0 := by
    rw [Matrix.smul_apply, hp, smul_eq_mul]
    exact mul_ne_zero ha hx
  have h2 : (a • V) q q ≠ 0 := by
    rw [Matrix.smul_apply, hq, smul_eq_mul]
    exact mul_ne_zero ha hy
  have h3 := h p p q q h1 h2
  simp only [Matrix.smul_apply, hp, hq, smul_eq_mul, mul_pow] at h3
  exact hxy (mul_left_cancel₀ (pow_ne_zero 4 ha) h3)

/-- Two nonzero entries in one row exclude submonomiality for every nonzero multiple. -/
theorem not_submonomial_smul {T : Type} {V : Matrix T T ℂ} {p q q' : T} (hqq : q ≠ q')
    (h1 : V p q ≠ 0) (h2 : V p q' ≠ 0) {a : ℂ} (ha : a ≠ 0) : ¬ IsSubmonomial (a • V) := by
  intro h
  apply hqq
  apply h.1 p q q'
  · rw [Matrix.smul_apply, smul_eq_mul]
    exact mul_ne_zero ha h1
  · rw [Matrix.smul_apply, smul_eq_mul]
    exact mul_ne_zero ha h2

/-- **ON THE LATTICE, `R_z(θ₀)` IS NOT AVAILABLE ON THE PAIR** at any positive level. -/
theorem not_pairAvail_zPh_of_lattice {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hL : QuartLattice 𝓘) {n : ℕ} (hn : 0 < n) : ¬ PairAvailAt 𝓘 arch zPh n := by
  intro h
  haveI : Nonempty ((Fin 2 × Fin 2) × Fin n) := ⟨((0, 0), ⟨0, hn⟩)⟩
  have h' : InstAvail 𝓘 ((Fin 2 × Fin 2) × Fin n) Unit (fun _ => conjChannel (pairOp zPh n)) := h
  obtain ⟨a, ha, hmem⟩ := exists_scaled_mem_of_instAvail_unitary arch h'
  exact not_quart_smul (pairOp_apply_same zPh 0 0 ⟨0, hn⟩) (pairOp_apply_same zPh 1 1 ⟨0, hn⟩)
    zPh_00_ne zPh_11_ne zPh_pow_ne ha (hL _ _ hmem).2

/-- **ON THE LATTICE, `R_z(θ₀)` IS NOT AVAILABLE ON THE TOKEN** at any positive level. -/
theorem not_tokenAvail_zPh_of_lattice {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hL : QuartLattice 𝓘) {n : ℕ} (hn : 0 < n) : ¬ TokenAvailAt 𝓘 arch zPh n := by
  intro h
  haveI : Nonempty (Fin 2 × Fin n) := ⟨(0, ⟨0, hn⟩)⟩
  have h' : InstAvail 𝓘 (Fin 2 × Fin n) Unit (fun _ => conjChannel (tokOp zPh n)) := h
  obtain ⟨a, ha, hmem⟩ := exists_scaled_mem_of_instAvail_unitary arch h'
  exact not_quart_smul (tokOp_apply_same zPh 0 0 ⟨0, hn⟩) (tokOp_apply_same zPh 1 1 ⟨0, hn⟩)
    zPh_00_ne zPh_11_ne zPh_pow_ne ha (hL _ _ hmem).2

/-- **IN A SUBMONOMIAL CLASS, `J` IS NOT AVAILABLE ON THE PAIR** at any positive level. -/
theorem not_pairAvail_uJ_of_submonomial {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hS : ∀ (T : Type) [Fintype T] [DecidableEq T] (K : Matrix T T ℂ), 𝓘 T K → IsSubmonomial K)
    {n : ℕ} (hn : 0 < n) : ¬ PairAvailAt 𝓘 arch uJ n := by
  intro h
  haveI : Nonempty ((Fin 2 × Fin 2) × Fin n) := ⟨((0, 0), ⟨0, hn⟩)⟩
  have h' : InstAvail 𝓘 ((Fin 2 × Fin 2) × Fin n) Unit (fun _ => conjChannel (pairOp uJ n)) := h
  obtain ⟨a, ha, hmem⟩ := exists_scaled_mem_of_instAvail_unitary arch h'
  have hne : (((0 : Fin 2), (0 : Fin 2)), (⟨0, hn⟩ : Fin n))
      ≠ (((0 : Fin 2), (1 : Fin 2)), (⟨0, hn⟩ : Fin n)) := by
    intro hc
    have h01 : (0 : Fin 2) = 1 := congrArg (fun x : (Fin 2 × Fin 2) × Fin n => x.1.2) hc
    exact absurd h01 (by decide)
  exact not_submonomial_smul (p := (((0 : Fin 2), (0 : Fin 2)), (⟨0, hn⟩ : Fin n))) hne
    (by rw [pairOp_apply_same]; exact uJ_00_ne) (by rw [pairOp_apply_same]; exact uJ_01_ne)
    ha (hS _ _ hmem)

/-- **IN A SUBMONOMIAL CLASS, `J` IS NOT AVAILABLE ON THE TOKEN** at any positive level. -/
theorem not_tokenAvail_uJ_of_submonomial {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hS : ∀ (T : Type) [Fintype T] [DecidableEq T] (K : Matrix T T ℂ), 𝓘 T K → IsSubmonomial K)
    {n : ℕ} (hn : 0 < n) : ¬ TokenAvailAt 𝓘 arch uJ n := by
  intro h
  haveI : Nonempty (Fin 2 × Fin n) := ⟨(0, ⟨0, hn⟩)⟩
  have h' : InstAvail 𝓘 (Fin 2 × Fin n) Unit (fun _ => conjChannel (tokOp uJ n)) := h
  obtain ⟨a, ha, hmem⟩ := exists_scaled_mem_of_instAvail_unitary arch h'
  have hne : ((0 : Fin 2), (⟨0, hn⟩ : Fin n)) ≠ ((1 : Fin 2), (⟨0, hn⟩ : Fin n)) := by
    intro hc
    have h01 : (0 : Fin 2) = 1 := congrArg Prod.fst hc
    exact absurd h01 (by decide)
  exact not_submonomial_smul (p := ((0 : Fin 2), (⟨0, hn⟩ : Fin n))) hne
    (by rw [tokOp_apply_same]; exact uJ_00_ne) (by rw [tokOp_apply_same]; exact uJ_01_ne)
    ha (hS _ _ hmem)

/-- A Kronecker product of submonomial matrices is submonomial. -/
theorem submonomial_tensorOf {R S : Type} [Fintype R] [DecidableEq R] [Fintype S] [DecidableEq S]
    {A : Matrix R R ℂ} {B : Matrix S S ℂ} (hA : IsSubmonomial A) (hB : IsSubmonomial B) :
    IsSubmonomial (tensorOf A B) := by
  refine ⟨fun p q q' h1 h2 => ?_, fun p p' q h1 h2 => ?_⟩
  · rw [tensorOf_apply] at h1 h2
    obtain ⟨h1a, h1b⟩ := mul_ne_zero_iff.mp h1
    obtain ⟨h2a, h2b⟩ := mul_ne_zero_iff.mp h2
    exact Prod.ext (hA.1 _ _ _ h1a h2a) (hB.1 _ _ _ h1b h2b)
  · rw [tensorOf_apply] at h1 h2
    obtain ⟨h1a, h1b⟩ := mul_ne_zero_iff.mp h1
    obtain ⟨h2a, h2b⟩ := mul_ne_zero_iff.mp h2
    exact Prod.ext (hA.2 _ _ _ h1a h2a) (hB.2 _ _ _ h1b h2b)

theorem zPh_sub : IsSubmonomial zPh := by
  unfold zPh
  exact submonomial_diagonal _

theorem tokOp_zPh_substratum (n : ℕ) : substratumClass (Fin 2 × Fin n) (tokOp zPh n) := by
  show IsMonomial (tokOp zPh n)
  rw [monomial_iff_submonomial]
  unfold tokOp
  exact submonomial_tensorOf zPh_sub submonomial_one

theorem pairOp_zPh_substratum (n : ℕ) :
    substratumClass ((Fin 2 × Fin 2) × Fin n) (pairOp zPh n) := by
  show IsMonomial (pairOp zPh n)
  rw [monomial_iff_submonomial]
  unfold pairOp
  exact submonomial_tensorOf (submonomial_tensorOf submonomial_one zPh_sub) submonomial_one

/-- **THE MONOMIAL INTERFACE SUPPLIES `R_z(θ₀)` ON THE PAIR** at every level: its phase intervention
at the angle `θ₀` is a member of the class. -/
theorem substratum_pairAvail_zPh (n : ℕ) :
    PairAvailAt substratumClass substratumClass_arch zPh n := by
  unfold PairAvailAt
  exact SubstratumSource.genTheory_avail_conj substratumClass_arch (pairOp_zPh_substratum n)
    (pairOp_isometry zPh_unitary n)

theorem substratum_tokenAvail_zPh (n : ℕ) :
    TokenAvailAt substratumClass substratumClass_arch zPh n := by
  unfold TokenAvailAt
  exact SubstratumSource.genTheory_avail_conj substratumClass_arch (tokOp_zPh_substratum n)
    (tokOp_isometry zPh_unitary n)

/-- **THE FULL CLASS SUPPLIES BOTH** on the pair at every level. -/
theorem fullClass_supplies (n : ℕ) :
    PairAvailAt fullClass fullClass_arch zPh n ∧ PairAvailAt fullClass fullClass_arch uJ n := by
  constructor
  · unfold PairAvailAt
    exact SubstratumSource.genTheory_avail_conj fullClass_arch trivial
      (pairOp_isometry zPh_unitary n)
  · unfold PairAvailAt
    exact SubstratumSource.genTheory_avail_conj fullClass_arch trivial
      (pairOp_isometry uJ_unitary n)

/-- **THE STATED ACCESS REFUTES BOTH**, on the pair and on the token, at every positive level. -/
theorem statedAccess_refutes {n : ℕ} (hn : 0 < n) :
    ¬ PairAvailAt permClass permClass_arch zPh n ∧ ¬ PairAvailAt permClass permClass_arch uJ n
      ∧ ¬ TokenAvailAt permClass permClass_arch zPh n
      ∧ ¬ TokenAvailAt permClass permClass_arch uJ n :=
  ⟨not_pairAvail_zPh_of_lattice permClass_arch permClass_quartLattice hn,
    not_pairAvail_uJ_of_submonomial permClass_arch
      (fun T _ _ K h => (permClass_quartLattice T K h).1) hn,
    not_tokenAvail_zPh_of_lattice permClass_arch permClass_quartLattice hn,
    not_tokenAvail_uJ_of_submonomial permClass_arch
      (fun T _ _ K h => (permClass_quartLattice T K h).1) hn⟩

/-- **THE STATED ACCESS WITH THE QUARTER PHASE REFUTES BOTH**, on the pair and on the token, at every
positive level. -/
theorem quarterAccess_refutes {n : ℕ} (hn : 0 < n) :
    ¬ PairAvailAt (MixR ∅) (mixR_arch ∅) zPh n ∧ ¬ PairAvailAt (MixR ∅) (mixR_arch ∅) uJ n
      ∧ ¬ TokenAvailAt (MixR ∅) (mixR_arch ∅) zPh n
      ∧ ¬ TokenAvailAt (MixR ∅) (mixR_arch ∅) uJ n :=
  ⟨not_pairAvail_zPh_of_lattice (mixR_arch ∅) mixEmpty_quartLattice hn,
    not_pairAvail_uJ_of_submonomial (mixR_arch ∅)
      (fun T _ _ K h => (mixEmpty_quartLattice T K h).1) hn,
    not_tokenAvail_zPh_of_lattice (mixR_arch ∅) mixEmpty_quartLattice hn,
    not_tokenAvail_uJ_of_submonomial (mixR_arch ∅)
      (fun T _ _ K h => (mixEmpty_quartLattice T K h).1) hn⟩

/-! ### §E — the two stabilities of `MixR ∅` and `DerivedOI` for its theory -/

section MixEmpty

open PolarizationClosure OperationalAssembly LieRankSource CoherentLift SpectatorBridge
  AncillaClosure

/-- **THE STATED ACCESS WITH THE QUARTER PHASE IS DAGGER-STABLE.** The kernel's proof of
`DiscreteCompletion.mixR_singleton_daggerStable` (DiscreteCompletion.lean:1861) at `D = ∅`, where the
datum case is empty. -/
theorem mixEmpty_daggerStable : DaggerStable (MixR (∅ : Set ℝ)) := by
  intro T _ _ K h
  induction h with
  | perm K h => exact MixR.perm _ (scaled_conjTranspose h)
  | phase n p =>
    rw [phaseGate_conjTranspose']
    exact MixR.mul _ _ (MixR.mul _ _ (MixR.phase n p) (MixR.phase n p)) (MixR.phase n p)
  | mix n θ hθ => exact absurd hθ (Set.notMem_empty θ)
  | mul K L _ _ ihK ihL => rw [Matrix.conjTranspose_mul]; exact MixR.mul _ _ ihL ihK
  | smul a K ha _ ih =>
    rw [Matrix.conjTranspose_smul]
    exact MixR.smul _ _ (by simpa using ha) ih
  | proj m k =>
    rw [Matrix.diagonal_conjTranspose]
    have key : ∀ (U : Type) [Fintype U] [DecidableEq U],
        (star fun r : U × Fin m => if r.2 = k then (1 : ℂ) else 0)
          = fun r => if r.2 = k then (1 : ℂ) else 0 := by
      intro U _ _
      funext r; simp only [Pi.star_apply]; split_ifs <;> simp
    rw [key]
    exact MixR.proj m k
  | block m K f e _ ih => rw [ancBlock_conjTranspose']; exact MixR.block m _ e f ih
  | relabel e K _ ih => rw [Matrix.conjTranspose_reindex]; exact MixR.relabel e _ ih

/-- **THE STATED ACCESS WITH THE QUARTER PHASE IS CONTEXT-STABLE.** The kernel's proof of
`DiscreteCompletion.mixR_singleton_contextStable` (DiscreteCompletion.lean:1890) at `D = ∅`. -/
theorem mixEmpty_contextStable : ContextStable (MixR (∅ : Set ℝ)) := by
  intro R T _ _ _ _ K h
  induction h with
  | perm K h => exact MixR.perm _ (scaled_tensor_one h)
  | phase n p =>
    rw [phaseGate, tensorOf_one_diagonal]
    set e := ctxRelabel R n
    have hmem := phaseIndicator_mem (mixR_arch ∅) (fun n p => MixR.phase n p) (Fintype.card R * n)
      (Finset.univ.filter fun x : Fin 2 × Fin (Fintype.card R * n) => p = (e x).2)
    have heq : (Matrix.diagonal fun q : R × (Fin 2 × Fin n) => if p = q.2 then Complex.I else 1)
        = Matrix.reindex e e (Matrix.diagonal fun x : Fin 2 × Fin (Fintype.card R * n) =>
            if x ∈ (Finset.univ.filter fun x : Fin 2 × Fin (Fintype.card R * n) => p = (e x).2)
            then Complex.I else 1) := by
      rw [Matrix.reindex_apply, Matrix.submatrix_diagonal_equiv]
      congr 1
      funext q
      simp
    rw [heq]
    exact MixR.relabel e _ hmem
  | mix n θ hθ => exact absurd hθ (Set.notMem_empty θ)
  | mul K L _ _ ihK ihL =>
    have key := tensorOf_mul' (1 : Matrix R R ℂ) (1 : Matrix R R ℂ) K L
    rw [Matrix.one_mul] at key
    rw [← key]
    exact MixR.mul _ _ ihK ihL
  | smul a K ha _ ih => rw [tensorOf_smul_right]; exact MixR.smul _ _ ha ih
  | proj m k =>
    rw [tensorOf_one_diagonal]
    exact MixR.perm _ (scaled_diagonal_indicator _)
  | block m K f e _ ih =>
    rw [tensorOf_one_ancBlock]
    exact MixR.block m _ f e (MixR.relabel _ _ ih)
  | relabel e K _ ih => rw [tensorOf_one_reindex]; exact MixR.relabel _ _ ih

/-- **THE STATED ACCESS WITH THE QUARTER PHASE SATISFIES `DerivedOI`** on the two-state carrier, by the
kernel's `derivedOI_of_stated` (StateMixingCoupling.lean:463). -/
theorem mixEmpty_derivedOI : DerivedOI (mixTheoryR (∅ : Set ℝ) (Fin 2)) :=
  derivedOI_of_stated (mixR_arch _) (mixR_labelInvariant _) mixEmpty_daggerStable
    mixEmpty_contextStable (fun _ _ _ K h => MixR.perm K h) (fun n p => MixR.phase n p)

end MixEmpty

/-! ### §F — the countermodels with their kernel facts -/

/-- **THE STATED ACCESS**: its theory satisfies the sourced closure and the sealed OI core
(`permTheory_sourcedOI`, `permTheory_realizesSealedOICore`, kernel), on the token's carrier, and the
sourced closure on the pair carrier; and neither `R_z(θ₀)` nor `J` is available, on the pair or on the
token, at any positive level. -/
theorem statedAccess_obstruction :
    (SourcedOI (permTheory (Fin 2)) ∧ RealizesSealedOICore (permTheory (Fin 2)))
      ∧ SourcedOI (permTheory (Fin 2 × Fin 2))
      ∧ ∀ n : ℕ, 0 < n →
        ¬ PairAvailAt permClass permClass_arch zPh n ∧ ¬ PairAvailAt permClass permClass_arch uJ n
          ∧ ¬ TokenAvailAt permClass permClass_arch zPh n
          ∧ ¬ TokenAvailAt permClass permClass_arch uJ n :=
  ⟨⟨permTheory_sourcedOI, permTheory_realizesSealedOICore⟩, permTheory_sourcedOI,
    fun _ hn => statedAccess_refutes hn⟩

/-- **THE STATED ACCESS WITH THE QUARTER PHASE**: its theory satisfies `DerivedOI`, every
theory-level predicate the kernel derives from the substratum; and neither `R_z(θ₀)` nor `J` is
available, on the pair or on the token, at any positive level. -/
theorem quarterAccess_obstruction :
    DerivedOI (mixTheoryR (∅ : Set ℝ) (Fin 2))
      ∧ ∀ n : ℕ, 0 < n →
        ¬ PairAvailAt (MixR ∅) (mixR_arch ∅) zPh n ∧ ¬ PairAvailAt (MixR ∅) (mixR_arch ∅) uJ n
          ∧ ¬ TokenAvailAt (MixR ∅) (mixR_arch ∅) zPh n
          ∧ ¬ TokenAvailAt (MixR ∅) (mixR_arch ∅) uJ n :=
  ⟨mixEmpty_derivedOI, fun _ hn => quarterAccess_refutes hn⟩

/-- **THE MONOMIAL INTERFACE**: its theory satisfies the closure with the sealed core
(`substratumTheory_derivedOICore`, kernel) and `DerivedOI` on the pair carrier; `R_z(θ₀)` is available
on the pair and on the token at every level, and `J` at no positive level. -/
theorem monomialInterface_split :
    DerivedOICore (substratumTheory (Fin 2)) ∧ DerivedOI (substratumTheory (Fin 2 × Fin 2))
      ∧ ∀ n : ℕ, 0 < n →
        PairAvailAt substratumClass substratumClass_arch zPh n
          ∧ TokenAvailAt substratumClass substratumClass_arch zPh n
          ∧ ¬ PairAvailAt substratumClass substratumClass_arch uJ n
          ∧ ¬ TokenAvailAt substratumClass substratumClass_arch uJ n :=
  ⟨substratumTheory_derivedOICore, substratumTheory_derivedOI, fun n hn =>
    ⟨substratum_pairAvail_zPh n, substratum_tokenAvail_zPh n,
      not_pairAvail_uJ_of_submonomial substratumClass_arch
        (fun _ _ _ _ h => monomial_submonomial h) hn,
      not_tokenAvail_uJ_of_submonomial substratumClass_arch
        (fun _ _ _ _ h => monomial_submonomial h) hn⟩⟩

/-! ### §G — controls -/

theorem one_entries_one {S : Type} [DecidableEq S] :
    ∀ i j, (1 : Matrix S S ℂ) i j ≠ 0 → (1 : Matrix S S ℂ) i j = 1 := by
  intro i j h
  by_cases hij : i = j
  · subst hij
    exact Matrix.one_apply_eq i
  · exact absurd (Matrix.one_apply_ne hij) h

theorem ones_tensorOf {R S : Type} [Fintype R] [DecidableEq R] [Fintype S] [DecidableEq S]
    {A : Matrix R R ℂ} {B : Matrix S S ℂ} (hA : ∀ i j, A i j ≠ 0 → A i j = 1)
    (hB : ∀ i j, B i j ≠ 0 → B i j = 1) :
    ∀ p q, tensorOf A B p q ≠ 0 → tensorOf A B p q = 1 := by
  intro p q h
  rw [tensorOf_apply] at h ⊢
  obtain ⟨ha, hb⟩ := mul_ne_zero_iff.mp h
  rw [hA _ _ ha, hB _ _ hb, one_mul]

theorem nflipU_sub : IsSubmonomial nflipU := by
  unfold nflipU
  exact monomial_submonomial (monomial_permMatrix _)

theorem nflipU_ones : ∀ i j, nflipU i j ≠ 0 → nflipU i j = 1 := by
  intro i j h
  unfold nflipU at h ⊢
  rw [CoherentLift.permMatrix] at h ⊢
  rw [if_pos (of_ite_ne_zero h)]

theorem nflipU_isometry : nflipUᴴ * nflipU = 1 := by
  unfold nflipU
  exact SpectatorBridge.permMatrix_isometry _

theorem pairOp_nflip_permClass (n : ℕ) :
    permClass ((Fin 2 × Fin 2) × Fin n) (pairOp nflipU n) := by
  have hsub : IsSubmonomial (pairOp nflipU n) := by
    unfold pairOp
    exact submonomial_tensorOf (submonomial_tensorOf submonomial_one nflipU_sub) submonomial_one
  have hones : ∀ p q, pairOp nflipU n p q ≠ 0 → pairOp nflipU n p q = 1 := by
    intro p q h
    unfold pairOp at h ⊢
    exact ones_tensorOf (ones_tensorOf one_entries_one nflipU_ones) one_entries_one p q h
  exact ⟨hsub, 1, norm_one.le, hones⟩

/-- **POSITIVE CONTROL**: the NOT is available on the pair in the stated access at every level, so
the predicate is satisfiable there. -/
theorem statedAccess_pairAvail_nflip (n : ℕ) : PairAvailAt permClass permClass_arch nflipU n := by
  unfold PairAvailAt
  exact SubstratumSource.genTheory_avail_conj permClass_arch (pairOp_nflip_permClass n)
    (pairOp_isometry nflipU_isometry n)

theorem quart_of_ones {T : Type} {K : Matrix T T ℂ} (h : ∀ i j, K i j ≠ 0 → K i j = 1) :
    QuartEq K :=
  fun i j k l h1 h2 => by rw [h i j h1, h k l h2]

theorem quart_tensorOf {R S : Type} [Fintype R] [DecidableEq R] [Fintype S] [DecidableEq S]
    {A : Matrix R R ℂ} {B : Matrix S S ℂ} (hA : QuartEq A) (hB : QuartEq B) :
    QuartEq (tensorOf A B) := by
  intro p q p' q' h1 h2
  simp only [tensorOf_apply] at h1 h2 ⊢
  obtain ⟨h1a, h1b⟩ := mul_ne_zero_iff.mp h1
  obtain ⟨h2a, h2b⟩ := mul_ne_zero_iff.mp h2
  rw [mul_pow, mul_pow, hA _ _ _ _ h1a h2a, hB _ _ _ _ h1b h2b]

theorem sPh_quart : QuartEq sPh := by
  have key : ∀ a b : Fin 2, sPh a b ≠ 0 → sPh a b ^ 4 = 1 := by
    intro a b h
    by_cases hab : a = b
    · subst hab
      unfold sPh
      rw [Matrix.diagonal_apply_eq]
      fin_cases a
      · exact one_pow 4
      · exact Complex.I_pow_four
    · exact absurd (Matrix.diagonal_apply_ne ![1, Complex.I] hab) h
  exact fun i j k l h1 h2 => by rw [key i j h1, key k l h2]

/-- **COUNTERCONTROL**: the quarter phase's pair operator lies on the fourth-root lattice, so the
lattice excludes `R_z(θ₀)` by its angle, not every phase. -/
theorem quarter_on_lattice (n : ℕ) : IsSubmonomial (pairOp sPh n) ∧ QuartEq (pairOp sPh n) := by
  have hs : IsSubmonomial sPh := by
    unfold sPh
    exact submonomial_diagonal _
  unfold pairOp
  exact ⟨submonomial_tensorOf (submonomial_tensorOf submonomial_one hs) submonomial_one,
    quart_tensorOf (quart_tensorOf (quart_of_ones one_entries_one) sPh_quart)
      (quart_of_ones one_entries_one)⟩

#print axioms w345_star
#print axioms w345_star_mul
#print axioms w345_ne_zero
#print axioms w345_pow_four
#print axioms w345_pow_four_ne_one
#print axioms zPh_00
#print axioms zPh_11
#print axioms zPh_00_ne
#print axioms zPh_11_ne
#print axioms zPh_pow_ne
#print axioms zPh_unitary
#print axioms uJ_00
#print axioms uJ_01
#print axioms uJ_00_ne
#print axioms uJ_01_ne
#print axioms uJ_star_a
#print axioms uJ_star_b
#print axioms uJ_star_c
#print axioms uJ_unitary
#print axioms pairOp_apply_same
#print axioms tokOp_apply_same
#print axioms pairOp_isometry
#print axioms tokOp_isometry
#print axioms pairOp_prod
#print axioms quart_of_scaled
#print axioms permClass_quartLattice
#print axioms submonomial_mul_apply
#print axioms phaseGate_quart
#print axioms mixEmpty_quartLattice
#print axioms not_quart_smul
#print axioms not_submonomial_smul
#print axioms not_pairAvail_zPh_of_lattice
#print axioms not_tokenAvail_zPh_of_lattice
#print axioms not_pairAvail_uJ_of_submonomial
#print axioms not_tokenAvail_uJ_of_submonomial
#print axioms submonomial_tensorOf
#print axioms zPh_sub
#print axioms tokOp_zPh_substratum
#print axioms pairOp_zPh_substratum
#print axioms substratum_pairAvail_zPh
#print axioms substratum_tokenAvail_zPh
#print axioms fullClass_supplies
#print axioms statedAccess_refutes
#print axioms quarterAccess_refutes
#print axioms mixEmpty_daggerStable
#print axioms mixEmpty_contextStable
#print axioms mixEmpty_derivedOI
#print axioms statedAccess_obstruction
#print axioms quarterAccess_obstruction
#print axioms monomialInterface_split
#print axioms one_entries_one
#print axioms ones_tensorOf
#print axioms nflipU_sub
#print axioms nflipU_ones
#print axioms nflipU_isometry
#print axioms pairOp_nflip_permClass
#print axioms statedAccess_pairAvail_nflip
#print axioms quart_of_ones
#print axioms quart_tensorOf
#print axioms sPh_quart
#print axioms quarter_on_lattice

end BridgeAvail
end OIBridge
