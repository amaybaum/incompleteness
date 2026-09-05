import OIBridge.LiftAudit

/-!
# The substratum-interface audit — the smallest faithful substrate-to-observer interface

The preregistered pass of `SUBSTRATUM-INTERFACE-AUDIT.md`. One arrow, `𝒮 ⟶ T_obs(𝒮)`: a
substratum carrying the manuscript substrate data, the axioms A1–A6 as predicates of it, and the
finite operational theory an embedded observer with read and write access to its visible
configurations obtains from it, by sourcing theorems and by nothing else.

* **Q1, faithful substrate representation** (Section A): `Substratum` is built from the kernel's
  second-order rule `Rule`, its phase-space map `leapEquiv`, and lattice translations; A1, A2,
  A5 are stated outright, A3 with the degree as a parameter and in family form, A4 with the gauge
  as a parameter; A6 is a gap and has no predicate. The manuscripts' discrete wave rule is an
  instance, `waveSubstratum`, and satisfies A1–A5 as stated.
* **Q2, observer sourcing** (Sections B, C, E): the write access, the read-write families at
  every level, generates the least architecture containing the exchanges, identified as
  `permClass`, the scaled partial permutation matrices, canonical by `permClass_le_of_exchanges`.
  The sourced theory `permTheory` and the observer theory `obsTheory 𝒮 = permTheory (Conf 𝒮)`
  carry the substratum's update and layers, the read-write operators, the exchanges, embedded
  observation and reversible implementation locality. They carry no quarter phase and no sign
  diagonal: every conjugation by a scaled partial permutation preserves matrices with
  nonnegative real entries (`PreservesNonneg`), and no non-scalar diagonal unitary does.
* **Q3, baseline comparison** (Section D): `SourcedOI`, the conjuncts of `DerivedOI` other than
  the phases, holds for the sourced theory and for quantum mechanics, and under it quantum
  mechanics is exactly phase-free richness; `DerivedOI` and `SubstratumAvail` both fail for the
  sourced theory, the gap being exactly `PhasesAvailable`. On the two-state carrier the sourced
  theory realizes the sealed OI core and lacks the falsifier.

Nothing here asks an executability question; no intermediate-time unitary enters any
availability. The observer theory depends on the substratum only through its configuration
space (`obsTheory_rule_independent`): configuration-level sourcing consumes nothing of A3–A6.
-/

namespace OIBridge
namespace SubstratumInterfaceAudit

open Complex Matrix CoherentLift SpectatorBridge OperationalAssembly AncillaClosure
open MonoidalCompletion InterventionLocality MicroReversibility PrimitiveSource LieRankSource
open DiagonalTheory SubstratumInterface StructuralClosure ReadWriteControl MinimalRepertoire
open LevelOneSeam PhysicalCharacterization RouteB ManuscriptAxioms OIRealization
open SecondOrderLayer
open OIBridge.SecondOrderCircuit (leap leapEquiv shear shearEquiv swapEquiv swapLayer curOf
  leap_apply curOf_apply)
open OIBridge.LiftAudit (levelPerm levelPerm_apply SubstratumAvail)

open scoped ComplexOrder

/-! ### Section A — Q1: the substratum and the axioms as predicates -/

section Substratum

/-- **A SUBSTRATUM**: a site type with lattice translations, an additive alphabet, and a
finite-range second-order rule. The configuration space is the phase-space form `ι → V × V`
and the dynamics is the kernel's phase-space map `leapEquiv`. The structure carries no
operational notion. -/
structure Substratum where
  ι : Type
  V : Type
  [decι : DecidableEq ι]
  [addι : AddCommGroup ι]
  [addV : AddCommGroup V]
  R : Rule ι V

attribute [instance] Substratum.decι Substratum.addι Substratum.addV

/-- A lattice translation acting on site-indexed data. -/
def shiftBy {ι α : Type} [AddCommGroup ι] (v : ι) (s : ι → α) : ι → α := fun i => s (i - v)

namespace Substratum

variable (𝒮 : Substratum)

/-- The configuration space: the phase-space form of the second-order rule. -/
abbrev Conf : Type := 𝒮.ι → 𝒮.V × 𝒮.V

/-- The dynamics `φ`: the phase-space map `(p, c) ↦ (c, F c − p)`. -/
def φ : 𝒮.Conf ≃ 𝒮.Conf := leapEquiv 𝒮.R.F

/-- **(A1) FINITENESS**: the configuration space is finite. -/
def A1 : Prop := Finite 𝒮.Conf

/-- **(A2) DETERMINISM**: the dynamics is a bijection. -/
def A2 : Prop := Function.Bijective 𝒮.φ

/-- **(A3) BOUNDED COUPLING DEGREE**, with the degree as a parameter: every site reads at most
`D` sites. -/
def A3 (D : ℕ) : Prop := ∀ i, (𝒮.R.N i).card ≤ D

/-- **(A4) CENTER INDEPENDENCE, EXACT FORM**: the rule commutes with every translation. -/
def A4Exact : Prop := ∀ (v : 𝒮.ι) (c : 𝒮.ι → 𝒮.V), 𝒮.R.F (shiftBy v c) = shiftBy v (𝒮.R.F c)

/-- **(A4) CENTER INDEPENDENCE UP TO GAUGE**, with the gauge as a parameter: the dynamics
commutes with every translation up to an element of `G`. -/
def A4 (G : Subgroup (Equiv.Perm 𝒮.Conf)) : Prop :=
  ∀ v : 𝒮.ι, ∃ g ∈ G, ∀ x : 𝒮.Conf, 𝒮.φ (shiftBy v x) = g (shiftBy v (𝒮.φ x))

/-- **(A5) LINEARITY**: the rule is additive over the alphabet. -/
def A5 : Prop := ∀ c c' : 𝒮.ι → 𝒮.V, 𝒮.R.F (c + c') = 𝒮.R.F c + 𝒮.R.F c'

/-- **A2 HOLDS FOR EVERY SUBSTRATUM OF THE STRUCTURE**: bijectivity is automatic for the
second-order form. -/
theorem a2_every_substratum : 𝒮.A2 := 𝒮.φ.bijective

/-- **A1 HOLDS UNDER FINITENESS OF THE SITES AND THE ALPHABET.** -/
theorem a1_of_finite [Finite 𝒮.ι] [Finite 𝒮.V] : 𝒮.A1 := by
  show Finite 𝒮.Conf
  infer_instance

/-- **A3 IS VACUOUS AT ONE FINITE LATTICE**: the number of sites is a bound. The content is the
family form. -/
theorem a3_of_fintype [Fintype 𝒮.ι] : 𝒮.A3 (Fintype.card 𝒮.ι) := fun _ => Finset.card_le_univ _

/-- **THE EXACT FORM OF A4 IS A4 WITH TRIVIAL GAUGE.** -/
theorem a4_of_exact (h : 𝒮.A4Exact) : 𝒮.A4 ⊥ := by
  intro v
  refine ⟨1, Subgroup.one_mem _, fun x => ?_⟩
  rw [Equiv.Perm.one_apply]
  funext i
  have hcur : curOf (shiftBy v x) = shiftBy v (curOf x) := rfl
  show leap 𝒮.R.F (shiftBy v x) i = leap 𝒮.R.F x (i - v)
  rw [leap_apply, leap_apply, hcur, h]
  rfl

end Substratum

/-- **A3 IN FAMILY FORM**: one degree bounds every member of a family of substrata. -/
def A3Family (𝒮 : ℕ → Substratum) : Prop := ∃ D, ∀ L, (𝒮 L).A3 D

end Substratum

/-! ### Section A, continued — the manuscripts' discrete wave rule as an instance -/

section Wave

variable (d L q : ℕ)

/-- The unit step along axis `k`, forward or backward. -/
def dir (p : Fin d × Bool) : Fin d → ZMod L :=
  if p.2 then Pi.single p.1 1 else -Pi.single p.1 1

theorem dir_flip (p : Fin d × Bool) : dir d L (p.1, !p.2) = -dir d L p := by
  rcases p with ⟨k, b⟩
  cases b <;> simp [dir]

/-- The `2d` axis neighbours of a site. -/
def nbrs (i : Fin d → ZMod L) : Finset (Fin d → ZMod L) :=
  Finset.univ.image fun p => i + dir d L p

theorem mem_nbrs_symm {i j : Fin d → ZMod L} (h : j ∈ nbrs d L i) : i ∈ nbrs d L j := by
  obtain ⟨p, -, rfl⟩ := Finset.mem_image.mp h
  refine Finset.mem_image.mpr ⟨(p.1, !p.2), Finset.mem_univ _, ?_⟩
  rw [dir_flip]
  abel

/-- **THE DISCRETE WAVE RULE** of `[SM §4.1]`: `α` times the sum over the axis neighbours. -/
def waveF (α : ZMod q) (c : (Fin d → ZMod L) → ZMod q) (i : Fin d → ZMod L) : ZMod q :=
  α * ∑ p : Fin d × Bool, c (i + dir d L p)

/-- The wave rule as a finite-range second-order rule. -/
def waveRule (α : ZMod q) : Rule (Fin d → ZMod L) (ZMod q) where
  F := waveF d L q α
  N := nbrs d L
  infl := nbrs d L
  dep i c c' h := by
    unfold waveF
    congr 1
    exact Finset.sum_congr rfl fun p _ =>
      h _ (Finset.mem_image.mpr ⟨p, Finset.mem_univ _, rfl⟩)
  mem_infl _ _ h := mem_nbrs_symm d L h

/-- **THE WAVE SUBSTRATUM**: the manuscripts' rule on a finite cubic torus with alphabet
`ℤ/qℤ`. -/
def waveSubstratum (α : ZMod q) : Substratum where
  ι := Fin d → ZMod L
  V := ZMod q
  R := waveRule d L q α

variable (α : ZMod q)

/-- **THE WAVE SUBSTRATUM SATISFIES A1** for a finite torus and alphabet. -/
theorem waveSubstratum_A1 [NeZero L] [NeZero q] : (waveSubstratum d L q α).A1 := by
  show Finite ((Fin d → ZMod L) → ZMod q × ZMod q)
  infer_instance

/-- **THE WAVE SUBSTRATUM SATISFIES A2.** -/
theorem waveSubstratum_A2 : (waveSubstratum d L q α).A2 :=
  Substratum.a2_every_substratum _

/-- **THE WAVE SUBSTRATUM SATISFIES A3 WITH DEGREE `2d`.** -/
theorem waveSubstratum_A3 : (waveSubstratum d L q α).A3 (2 * d) := by
  intro i
  show (nbrs d L i).card ≤ 2 * d
  refine Finset.card_image_le.trans ?_
  simp [mul_comm]

/-- **THE WAVE SUBSTRATUM SATISFIES THE EXACT FORM OF A4**: the rule commutes with every
translation of the torus. -/
theorem waveSubstratum_A4Exact : (waveSubstratum d L q α).A4Exact := by
  intro (v : Fin d → ZMod L) (c : (Fin d → ZMod L) → ZMod q)
  funext (i : Fin d → ZMod L)
  show waveF d L q α (shiftBy v c) i = waveF d L q α c (i - v)
  unfold waveF shiftBy
  congr 1
  exact Finset.sum_congr rfl fun p _ => by rw [add_sub_right_comm]

/-- **THE WAVE SUBSTRATUM SATISFIES A5**: the rule is additive. -/
theorem waveSubstratum_A5 : (waveSubstratum d L q α).A5 := by
  intro (c : (Fin d → ZMod L) → ZMod q) (c' : (Fin d → ZMod L) → ZMod q)
  funext (i : Fin d → ZMod L)
  show waveF d L q α (c + c') i = waveF d L q α c i + waveF d L q α c' i
  unfold waveF
  rw [← mul_add, ← Finset.sum_add_distrib]
  rfl

end Wave

/-! ### Section B — Q2: the sourced class, the least architecture containing the exchanges -/

section PermClass

variable {S : Type}

/-- **A SCALED PARTIAL PERMUTATION**, elementwise: at most one nonzero entry per row and per
column, all nonzero entries equal. This is the operator shape of a configuration bijection
restricted to a subset with one overall amplitude. -/
def IsScaledPartialPerm (K : Matrix S S ℂ) : Prop :=
  IsSubmonomial K ∧ ∃ c : ℂ, ∀ i j, K i j ≠ 0 → K i j = c

/-- **THE SOURCED CLASS**: the scaled partial permutation matrices, at every carrier. -/
def permClass : ImplementationClass := fun _ _ _ K => IsScaledPartialPerm K

variable [Fintype S] [DecidableEq S]

/-- **THE FACTORED FORM**: a scalar times a permutation matrix times a `0/1` diagonal. -/
theorem scaledPartialPerm_iff (K : Matrix S S ℂ) :
    IsScaledPartialPerm K ↔ ∃ (c : ℂ) (σ : Equiv.Perm S) (A : Finset S),
      K = c • (permMatrix σ * Matrix.diagonal (fun s => if s ∈ A then 1 else 0)) := by
  constructor
  · rintro ⟨hsub, c, hc⟩
    obtain ⟨σ, d, hK⟩ := submonomial_monomial hsub
    refine ⟨c, σ, Finset.univ.filter (fun s => d s ≠ 0), ?_⟩
    have hKj : ∀ j, K (σ j) j = d j := fun j => by rw [hK, monomial_entry, if_pos rfl]
    rw [hK]
    ext i j
    rw [Matrix.smul_apply, monomial_entry, monomial_entry, smul_eq_mul]
    by_cases hij : σ j = i
    · rw [if_pos hij, if_pos hij]
      by_cases hd : d j = 0
      · simp [hd]
      · have hc' := hc _ _ (by rw [hKj]; exact hd)
        rw [hKj] at hc'
        simp [hc']
    · rw [if_neg hij, if_neg hij, mul_zero]
  · rintro ⟨c, σ, A, rfl⟩
    refine ⟨submonomial_smul c (monomial_submonomial ⟨σ, _, rfl⟩), c, fun i j h => ?_⟩
    rw [Matrix.smul_apply, monomial_entry, smul_eq_mul] at h ⊢
    by_cases hij : σ j = i
    · rw [if_pos hij] at h ⊢
      by_cases hA : j ∈ A
      · rw [if_pos hA, mul_one]
      · rw [if_neg hA, mul_zero] at h
        exact absurd rfl h
    · rw [if_neg hij, mul_zero] at h
      exact absurd rfl h

omit [Fintype S] in
theorem scaled_one_aux : IsScaledPartialPerm (1 : Matrix S S ℂ) := by
  classical
  refine ⟨?_, 1, fun i j h => ?_⟩
  · exact ⟨fun i j j' h1 h2 => by
        rw [Matrix.one_apply] at h1 h2
        exact (of_ite_ne_zero h1).symm.trans (of_ite_ne_zero h2),
      fun i i' j h1 h2 => by
        rw [Matrix.one_apply] at h1 h2
        exact (of_ite_ne_zero h1).trans (of_ite_ne_zero h2).symm⟩
  · rw [Matrix.one_apply] at h ⊢
    rw [if_pos (of_ite_ne_zero h)]

omit [DecidableEq S] in
/-- **PRODUCTS**: a nonzero entry of `K * L` is the product of the two selected entries. -/
theorem scaled_mul {K L : Matrix S S ℂ} (hK : IsScaledPartialPerm K)
    (hL : IsScaledPartialPerm L) : IsScaledPartialPerm (K * L) := by
  obtain ⟨hK1, c, hc⟩ := hK
  obtain ⟨hL1, c', hc'⟩ := hL
  refine ⟨submonomial_mul hK1 hL1, c * c', fun i j h => ?_⟩
  obtain ⟨k, hk1, hk2⟩ := mul_entry_ne_zero h
  rw [Matrix.mul_apply, Finset.sum_eq_single k, hc _ _ hk1, hc' _ _ hk2]
  · intro k' _ hk'
    by_cases h1 : K i k' = 0
    · rw [h1, zero_mul]
    · exact absurd (hK1.1 _ _ _ h1 hk1) hk'
  · intro h
    exact absurd (Finset.mem_univ k) h

omit [Fintype S] [DecidableEq S] in
theorem scaled_smul (a : ℂ) {K : Matrix S S ℂ} (hK : IsScaledPartialPerm K) :
    IsScaledPartialPerm (a • K) := by
  obtain ⟨hK1, c, hc⟩ := hK
  refine ⟨submonomial_smul a hK1, a * c, fun i j h => ?_⟩
  rw [Matrix.smul_apply, smul_eq_mul] at h ⊢
  rw [hc _ _ (mul_ne_zero_iff.mp h).2]

theorem scaled_diagonal_indicator (p : S → Prop) [DecidablePred p] :
    IsScaledPartialPerm (Matrix.diagonal fun s => if p s then (1 : ℂ) else 0) := by
  refine ⟨submonomial_diagonal _, 1, fun i j h => ?_⟩
  rw [Matrix.diagonal_apply] at h ⊢
  have hij := of_ite_ne_zero h
  rw [if_pos hij] at h ⊢
  rw [if_pos (of_ite_ne_zero h)]

omit [Fintype S] [DecidableEq S] in
theorem scaled_block {m : ℕ} {K : Matrix (S × Fin m) (S × Fin m) ℂ}
    (hK : IsScaledPartialPerm K) (f e : Fin m) : IsScaledPartialPerm (ancBlock K f e) := by
  obtain ⟨hK1, c, hc⟩ := hK
  exact ⟨submonomial_block hK1 f e, c, fun i j h => hc _ _ h⟩

theorem scaled_tensor_one {R : Type} [Fintype R] [DecidableEq R] {K : Matrix S S ℂ}
    (hK : IsScaledPartialPerm K) : IsScaledPartialPerm (tensorOf (1 : Matrix R R ℂ) K) := by
  obtain ⟨hK1, c, hc⟩ := hK
  refine ⟨submonomial_tensor_one hK1, c, fun p q h => ?_⟩
  obtain ⟨h1, h2⟩ := tensor_one_entry_ne_zero h
  rw [tensorOf_apply, hc _ _ h2, h1, Matrix.one_apply_eq, one_mul]

omit [Fintype S] [DecidableEq S] in
theorem scaled_reindex {S' : Type} [Fintype S'] [DecidableEq S'] (e : S ≃ S')
    {K : Matrix S S ℂ} (hK : IsScaledPartialPerm K) : IsScaledPartialPerm (Matrix.reindex e e K) := by
  obtain ⟨hK1, c, hc⟩ := hK
  refine ⟨submonomial_reindex e hK1, c, fun p q h => ?_⟩
  rw [Matrix.reindex_apply, Matrix.submatrix_apply] at h ⊢
  exact hc _ _ h

omit [Fintype S] [DecidableEq S] in
theorem scaled_conjTranspose {K : Matrix S S ℂ} (hK : IsScaledPartialPerm K) :
    IsScaledPartialPerm Kᴴ := by
  obtain ⟨hK1, c, hc⟩ := hK
  refine ⟨submonomial_conjTranspose hK1, star c, fun i j h => ?_⟩
  rw [Matrix.conjTranspose_apply] at h ⊢
  rw [hc _ _ (star_ne_zero.mp h)]

/-- **THE SOURCED CLASS IS AN ARCHITECTURE.** -/
theorem permClass_arch : Architecture permClass where
  one := fun _ _ _ => scaled_one_aux
  mul := fun _ _ _ _ _ hK hL => scaled_mul hK hL
  smul := fun _ _ _ a _ hK => scaled_smul a hK
  proj := fun _ _ _ _ _ => scaled_diagonal_indicator _
  block := fun _ _ _ _ _ f e hK => scaled_block hK f e

/-- **THE SOURCED CLASS IS CONTEXT-STABLE.** -/
theorem permClass_contextStable : ContextStable permClass :=
  fun _ _ _ _ _ _ _ hK => scaled_tensor_one hK

/-- **THE SOURCED CLASS IS LABEL-INVARIANT.** -/
theorem permClass_labelInvariant : LabelInvariant permClass :=
  fun _ _ _ _ _ _ e _ hK => scaled_reindex e hK

/-- **THE SOURCED CLASS IS DAGGER-STABLE**: the reversal of a scaled partial permutation is one. -/
theorem permClass_daggerStable : DaggerStable permClass :=
  fun _ _ _ _ hK => scaled_conjTranspose hK

/-- **EVERY PERMUTATION MATRIX IS IN THE SOURCED CLASS.** -/
theorem permClass_permMatrix (σ : Equiv.Perm S) : permClass S (permMatrix σ) := by
  refine ⟨monomial_submonomial (monomial_permMatrix σ), 1, fun i j h => ?_⟩
  rw [permMatrix] at h ⊢
  rw [if_pos (of_ite_ne_zero h)]

/-- **EVERY READ-WRITE OPERATOR IS IN THE SOURCED CLASS.** -/
theorem permClass_readWrite {a b : S} (F : ReadWriteFamily a b) (l : ℝ) :
    permClass S (readWriteOperator F l) := by
  rw [readWriteOperator_eq_perm]
  exact permClass_permMatrix _

/-- **THE SOURCED CLASS LIES IN THE SUBSTRATUM CLASS**: a scaled partial permutation is monomial. -/
theorem permClass_le_substratum (K : Matrix S S ℂ) (h : permClass S K) : substratumClass S K :=
  submonomial_monomial h.1

/-- Flip the ancilla bit of every configuration in `B`, an involution of `S × Fin 2`. -/
def flipOn (B : Finset S) : Equiv.Perm (S × Fin 2) where
  toFun p := if p.1 ∈ B then (p.1, if p.2 = 0 then 1 else 0) else p
  invFun p := if p.1 ∈ B then (p.1, if p.2 = 0 then 1 else 0) else p
  left_inv p := by
    by_cases h : p.1 ∈ B
    · simp only [h, if_true]
      rcases p with ⟨s, k⟩
      fin_cases k <;> rfl
    · simp [h]
  right_inv p := by
    by_cases h : p.1 ∈ B
    · simp only [h, if_true]
      rcases p with ⟨s, k⟩
      fin_cases k <;> rfl
    · simp [h]

omit [Fintype S] in
/-- **THE FIRST ANCILLA BLOCK OF THE FLIP IS THE INDICATOR OF THE COMPLEMENT.** -/
theorem ancBlock_flipOn (B : Finset S) :
    ancBlock (permMatrix (flipOn B)) 0 0
      = Matrix.diagonal (fun s => if s ∈ B then (0 : ℂ) else 1) := by
  ext s t
  rw [ancBlock, Matrix.of_apply, permMatrix, Matrix.diagonal_apply]
  by_cases ht : t ∈ B
  · have h1 : flipOn B (t, 0) = (t, 1) := by simp [flipOn, ht]
    rw [h1, if_neg (by simp)]
    by_cases hst : s = t
    · subst hst
      simp [ht]
    · rw [if_neg hst]
  · have h1 : flipOn B (t, 0) = (t, 0) := by simp [flipOn, ht]
    rw [h1]
    by_cases hst : s = t
    · subst hst
      simp [ht]
    · simp [hst, Ne.symm hst]

/-- **THE SOURCED CLASS IS THE LEAST ARCHITECTURE CONTAINING THE EXCHANGES**: every architecture
in which the exchange of any two configurations is admissible at every carrier contains every
scaled partial permutation — the permutations by swap induction, the `0/1` diagonals as ancilla
blocks of permutations, the scalars and products by closure. The class is canonical, not chosen. -/
theorem permClass_le_of_exchanges {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hex : ∀ (S : Type) [Fintype S] [DecidableEq S] (a b : S), 𝓘 S (permMatrix (Equiv.swap a b))) :
    ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), permClass S K → 𝓘 S K := by
  have hperm : ∀ (S : Type) [Fintype S] [DecidableEq S] (σ : Equiv.Perm S), 𝓘 S (permMatrix σ) := by
    intro S _ _ σ
    induction σ using Equiv.Perm.swap_induction_on with
    | one => rw [permMatrix_one']; exact arch.one S
    | swap_mul f x y hxy ih => rw [permMatrix_mul']; exact arch.mul S _ _ (hex S x y) ih
  intro S _ _ K hK
  obtain ⟨c, σ, A, rfl⟩ := (scaledPartialPerm_iff K).mp hK
  refine arch.smul S c _ (arch.mul S _ _ (hperm S σ) ?_)
  have hb := arch.block S 2 _ 0 0 (hperm (S × Fin 2) (flipOn Aᶜ))
  rw [ancBlock_flipOn] at hb
  have hfun : (fun s => if s ∈ Aᶜ then (0 : ℂ) else 1) = fun s => if s ∈ A then 1 else 0 := by
    funext s
    simp [Finset.mem_compl]
  rw [hfun] at hb
  exact hb

/-- **A BIJECTION-LEVEL ARCHITECTURE**: every admissible operator is a scaled partial
permutation — the shape of every sourcing that supplies only configuration bijections. -/
def BijectionLevel (𝓘 : ImplementationClass) : Prop :=
  ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), 𝓘 S K → permClass S K

theorem permClass_bijectionLevel : BijectionLevel permClass := fun _ _ _ _ h => h

/-- A bijection-level architecture is configuration-level. -/
theorem bijectionLevel_configurationLevel {𝓘 : ImplementationClass} (h : BijectionLevel 𝓘) :
    ConfigurationLevel 𝓘 :=
  fun S _ _ K hK => permClass_le_substratum K (h S K hK)

end PermClass

/-! ### Section C — Q2: the sourced theory carries no phase -/

section Nonneg

variable {S : Type} [Fintype S] [DecidableEq S]

/-- **PRESERVING NONNEGATIVE ENTRIES**: a map sending every matrix with nonnegative real entries
to one with nonnegative real entries. -/
def PreservesNonneg (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  ∀ X : Matrix S S ℂ, (∀ p q, 0 ≤ X p q) → ∀ p q, 0 ≤ Φ X p q

/-- **A CONJUGATION BY A SCALED PARTIAL PERMUTATION PRESERVES NONNEGATIVE ENTRIES**: each term
of `K X Kᴴ` is `K p k · star (K q l) · X k l`, and the first two factors are `0` or `|c|²`. -/
theorem preservesNonneg_conj_of_scaled {K : Matrix S S ℂ} (h : IsScaledPartialPerm K) :
    PreservesNonneg (conjChannel K) := by
  obtain ⟨-, c, hc⟩ := h
  intro X hX p q
  rw [conjChannel_apply, Matrix.mul_apply]
  refine Finset.sum_nonneg fun l _ => ?_
  rw [Matrix.mul_apply, Matrix.conjTranspose_apply, Finset.sum_mul]
  refine Finset.sum_nonneg fun k _ => ?_
  have hpair : 0 ≤ K p k * star (K q l) := by
    by_cases h1 : K p k = 0
    · rw [h1, zero_mul]
    by_cases h2 : K q l = 0
    · rw [h2, star_zero, mul_zero]
    rw [hc _ _ h1, hc _ _ h2, Complex.star_def, Complex.mul_conj]
    exact Complex.zero_le_real.mpr (Complex.normSq_nonneg c)
  calc (0 : ℂ) ≤ (K p k * star (K q l)) * X k l := mul_nonneg hpair (hX k l)
    _ = K p k * X k l * star (K q l) := by ring

omit [Fintype S] [DecidableEq S] in
theorem preservesNonneg_sum {ι : Type} (s : Finset ι) (Φ : ι → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)
    (h : ∀ i ∈ s, PreservesNonneg (Φ i)) : PreservesNonneg (∑ i ∈ s, Φ i) := by
  intro X hX p q
  rw [LinearMap.sum_apply, Matrix.sum_apply]
  exact Finset.sum_nonneg fun i hi => h i hi X hX p q

/-- **AN OPERATION REALIZED BY A BIJECTION-LEVEL CLASS PRESERVES NONNEGATIVE ENTRIES.** -/
theorem preservesNonneg_of_realized {𝓘 : ImplementationClass} (hb : BijectionLevel 𝓘)
    {Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : Realized 𝓘 S Φ) : PreservesNonneg Φ := by
  obtain ⟨ι, _, K, rfl, hadm⟩ := h
  exact preservesNonneg_sum _ _ fun i _ => preservesNonneg_conj_of_scaled (hb S _ (hadm i))

/-- **A DIAGONAL CONJUGATION PRESERVING NONNEGATIVE ENTRIES HAS PAIRWISE NONNEGATIVE WEIGHTS**:
apply it to the matrix unit at `(p, q)`. -/
theorem diagonal_nonneg_of_preservesNonneg {d : S → ℂ}
    (h : PreservesNonneg (conjChannel (Matrix.diagonal d))) (p q : S) : 0 ≤ d p * star (d q) := by
  have hX : ∀ i j, (0 : ℂ) ≤ Matrix.single p q (1 : ℂ) i j := by
    intro i j
    by_cases hij : p = i ∧ q = j
    · obtain ⟨rfl, rfl⟩ := hij
      rw [Matrix.single_apply_same]
      exact zero_le_one
    · rw [Matrix.single_apply_of_ne _ _ _ _ _ hij]
  have := h _ hX p q
  rw [conjChannel_apply, Matrix.diagonal_conjTranspose, Matrix.mul_diagonal, Matrix.diagonal_mul,
    Matrix.single_apply_same, mul_one, Pi.star_apply] at this
  exact this

/-- **THE QUARTER PHASE DOES NOT PRESERVE NONNEGATIVE ENTRIES**: on the pair `(a, 0), (a, 1)` of
the second level its weight product is `i`. -/
theorem phaseGate_not_preservesNonneg (a : S) :
    ¬ PreservesNonneg (conjChannel (phaseGate ((a, (0 : Fin 2)) : S × Fin 2))) := by
  intro h
  have := diagonal_nonneg_of_preservesNonneg (d := fun p => if (a, (0 : Fin 2)) = p then Complex.I else 1)
    h (a, 0) (a, 1)
  simp only [if_true, show ((a, (0 : Fin 2)) = (a, 1)) ↔ False by simp, if_false, star_one,
    mul_one] at this
  rw [Complex.nonneg_iff] at this
  simp at this

/-- **A SIGN DIAGONAL DOES NOT PRESERVE NONNEGATIVE ENTRIES.** -/
theorem sign_not_preservesNonneg {d : S → ℂ} {p q : S} (hp : d p = 1) (hq : d q = -1) :
    ¬ PreservesNonneg (conjChannel (Matrix.diagonal d)) := by
  intro h
  have := diagonal_nonneg_of_preservesNonneg h p q
  rw [hp, hq, one_mul, star_neg, star_one, Complex.nonneg_iff] at this
  norm_num at this

variable {A : Type} [Fintype A] [DecidableEq A]

/-- **NO BIJECTION-LEVEL CLASS GENERATES THE QUARTER PHASES**: on any nonempty carrier, the
quarter phase at the second level is unavailable in the generated theory. -/
theorem bijectionLevel_not_phasesAvailable [Nonempty A] {𝓘 : ImplementationClass}
    (arch : Architecture 𝓘) (hb : BijectionLevel 𝓘) : ¬ PhasesAvailable (genTheory 𝓘 arch A) := by
  intro hp
  have hav := hp 2 (Classical.arbitrary A, 0)
  exact phaseGate_not_preservesNonneg _ (preservesNonneg_of_realized hb (hav.1 ()))

/-- **A DIAGONAL CONJUGATION AVAILABLE IN THE THEORY OF A BIJECTION-LEVEL CLASS HAS PAIRWISE
NONNEGATIVE WEIGHTS**: a diagonal unitary available in it is a global phase. -/
theorem bijectionLevel_diagonal_only_scalar {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hb : BijectionLevel 𝓘) {n : ℕ} {d : A × Fin n → ℂ}
    (hav : (genTheory 𝓘 arch A).availExt n Unit (fun _ => conjChannel (Matrix.diagonal d))) :
    ∀ p q, 0 ≤ d p * star (d q) :=
  diagonal_nonneg_of_preservesNonneg (preservesNonneg_of_realized hb (hav.1 ()))

end Nonneg

/-! ### Section D — the sourced theory and Q3: the baseline comparison -/

section Sourced

variable {A : Type} [Fintype A] [DecidableEq A]

/-- **THE SOURCED THEORY**: the theory the sourced class generates. -/
noncomputable abbrev permTheory (A : Type) [Fintype A] [DecidableEq A] :
    FiniteOperationalTheory A :=
  genTheory permClass permClass_arch A

/-- A scaled-partial-permutation isometry's conjugation is available in the sourced theory. -/
theorem permTheory_avail_conj {n : ℕ} {V : Matrix (A × Fin n) (A × Fin n) ℂ}
    (hV : permClass (A × Fin n) V) (hiso : Vᴴ * V = 1) :
    (permTheory A).availExt n Unit (fun _ => conjChannel V) :=
  SubstratumSource.genTheory_avail_conj permClass_arch hV hiso

/-- **THE SOURCED CLOSURE, `SourcedOI`**: the conjuncts of `DerivedOI` other than the phases —
reversible implementation locality, embedded observation, and the availability at every level
of the exchanges and the read-write operators. -/
def SourcedOI (T : FiniteOperationalTheory A) : Prop :=
  ReversibleImplementationLocality T ∧ EmbeddedObservation T
    ∧ ExchangesAvailable T ∧ ReadWriteAvailable T

/-- **`DerivedOI` IS `SourcedOI` WITH THE PHASES**, by definition. -/
theorem derivedOI_iff_sourcedOI_phases (T : FiniteOperationalTheory A) :
    DerivedOI T ↔ SourcedOI T ∧ PhasesAvailable T := by
  constructor
  · rintro ⟨h1, h2, h3, h4, h5⟩
    exact ⟨⟨h1, h2, h3, h5⟩, h4⟩
  · rintro ⟨⟨h1, h2, h3, h5⟩, h4⟩
    exact ⟨h1, h2, h3, h4, h5⟩

theorem sourcedOI_of_derivedOI {T : FiniteOperationalTheory A} (h : DerivedOI T) : SourcedOI T :=
  ((derivedOI_iff_sourcedOI_phases T).mp h).1

/-- **QUANTUM MECHANICS SATISFIES THE SOURCED CLOSURE.** -/
theorem sourcedOI_of_qm [Nonempty A] (T : FiniteOperationalTheory A)
    (h : ExactAllFiniteEndomorphicQuantumOps T) : SourcedOI T :=
  sourcedOI_of_derivedOI (derivedOI_of_qm T h)

/-- **THE EXCHANGES ARE THE READ-WRITE OPERATORS OF THE MEMORY-SWAP FAMILIES**: the write access
supplies exactly the exchanges. -/
theorem exchanges_of_readWrite {T : FiniteOperationalTheory A} (h : ReadWriteAvailable T) :
    ExchangesAvailable T := by
  intro n a b
  have hav := h n a b (memorySwap a b) 1
  have hop : readWriteOperator (memorySwap a b) 1 = permMatrix (Equiv.swap a b) := by
    rw [readWriteOperator_eq_perm]
    simp [memorySwap]
  rwa [hop] at hav

/-- **UNDER THE SOURCED CLOSURE, QUANTUM MECHANICS IS EXACTLY PHASE-FREE RICHNESS**: the
equivalence of `RouteB` uses implementation locality and embedded observation only, and no
phase. -/
theorem sourcedOI_qm_iff_phaseFree [Nonempty A] {T : FiniteOperationalTheory A} (h : SourcedOI T) :
    ExactAllFiniteEndomorphicQuantumOps T ↔ PhaseFreeRichness T :=
  ⟨fun hqm => ((oiPlusMin_iff_qm T).mpr hqm).2.1,
    fun hpf => (oiPlusMin_iff_qm T).mp ⟨implementationLocality_of_reversible h.1, hpf, h.2.1⟩⟩

/-- **THE SOURCED THEORY SATISFIES THE SOURCED CLOSURE** on every carrier. -/
theorem permTheory_sourcedOI : SourcedOI (permTheory A) :=
  ⟨genTheory_reversibleImplementationLocality permClass permClass_arch permClass_contextStable
      permClass_labelInvariant permClass_daggerStable,
    genTheory_embeddedObservation permClass permClass_arch permClass_labelInvariant,
    fun _ a b => permTheory_avail_conj (permClass_permMatrix (Equiv.swap a b)) (permMatrix_isometry _),
    fun _ _ _ F l => permTheory_avail_conj (permClass_readWrite F l)
      (by rw [readWriteOperator_eq_perm]; exact permMatrix_isometry _)⟩

/-- **THE SOURCED THEORY CARRIES NO QUARTER PHASE.** -/
theorem permTheory_not_phasesAvailable [Nonempty A] : ¬ PhasesAvailable (permTheory A) :=
  bijectionLevel_not_phasesAvailable permClass_arch permClass_bijectionLevel

/-- **A DIAGONAL UNITARY AVAILABLE IN THE SOURCED THEORY IS A GLOBAL PHASE**: its weights have
pairwise nonnegative products. -/
theorem permTheory_diagonal_only_scalar {n : ℕ} {d : A × Fin n → ℂ}
    (hav : (permTheory A).availExt n Unit (fun _ => conjChannel (Matrix.diagonal d))) :
    ∀ p q, 0 ≤ d p * star (d q) :=
  bijectionLevel_diagonal_only_scalar permClass_arch permClass_bijectionLevel hav

/-- **NO SIGN DIAGONAL IS AVAILABLE IN THE SOURCED THEORY.** -/
theorem permTheory_no_sign {n : ℕ} {d : A × Fin n → ℂ} {p q : A × Fin n} (hp : d p = 1)
    (hq : d q = -1) : ¬ (permTheory A).availExt n Unit (fun _ => conjChannel (Matrix.diagonal d)) :=
  fun hav => sign_not_preservesNonneg hp hq (preservesNonneg_of_realized permClass_bijectionLevel (hav.1 ()))

/-- **THE SOURCED THEORY FAILS `DerivedOI`**: the phases are the failing conjunct. -/
theorem permTheory_not_derivedOI [Nonempty A] : ¬ DerivedOI (permTheory A) :=
  fun h => permTheory_not_phasesAvailable h.2.2.2.1

/-- **THE SUBSTRATUM'S AVAILABILITY INCLUDES THE PHASES.** -/
theorem substratumAvail_phasesAvailable {T : FiniteOperationalTheory A} (hsub : SubstratumAvail T) :
    PhasesAvailable T :=
  fun n a => hsub n Unit _ (substratumTheory_derivedOI.2.2.2.1 n a)

/-- **THE SOURCED THEORY FAILS `SubstratumAvail`.** -/
theorem permTheory_not_substratumAvail [Nonempty A] : ¬ SubstratumAvail (permTheory A) :=
  fun h => permTheory_not_phasesAvailable (substratumAvail_phasesAvailable h)

/-- **THE SOURCED THEORY LIES INSIDE THE SUBSTRATUM THEORY**: every available family is available
there. The gap is one-directional. -/
theorem permTheory_availExt_le_substratum {n : ℕ} {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (hF : (permTheory A).availExt n O F) : (substratumTheory A).availExt n O F :=
  configurationLevel_availExt_le permClass_arch
    (bijectionLevel_configurationLevel permClass_bijectionLevel) F hF

/-- **THE SOURCED THEORY HAS NO COMPOSITE UNITARY CONTROL**: control would supply the phases. -/
theorem permTheory_not_control [Nonempty A] : ¬ HasCompositeUnitaryControl (permTheory A) :=
  fun h => permTheory_not_phasesAvailable (phasesAvailable_of_control h)

/-- **THE SOURCED THEORY FAILS PHASE-FREE RICHNESS.** -/
theorem permTheory_not_phaseFree [Nonempty A] : ¬ PhaseFreeRichness (permTheory A) :=
  fun h => permTheory_not_control
    (control_of_phaseFree _ (closure_of_embeddedObservation permTheory_sourcedOI.2.1) h)

/-- **THE SOURCED THEORY IS NOT QUANTUM MECHANICS.** -/
theorem permTheory_not_qm [Nonempty A] : ¬ ExactAllFiniteEndomorphicQuantumOps (permTheory A) :=
  fun h => permTheory_not_control (physical_of_exactAll _ h).2.2.1

end Sourced

/-! ### Section D, continued — the two-state carrier: the sealed OI core needs no phase -/

section TwoState

open IndependenceCensus CoherentExtension

/-- **A TRANSPORTED PERMUTATION OF THE CORE IS AVAILABLE IN THE SOURCED THEORY**: the relabelled
permutation matrix is a scaled partial permutation and an isometry. -/
theorem permTheory_relabel (g : Equiv.Perm Core) :
    (permTheory (Fin 2)).availExt 4 Unit
      (fun _ => transport coreIdx (correlationExtension g (onesCorr Core))) := by
  rw [correlationExtension_ones_eq_conjChannel, transport_conjChannel]
  exact permTheory_avail_conj
    (permClass_labelInvariant _ _ coreIdx _ (permClass_permMatrix g))
    (reindex_isometry _ _ (permMatrix_isometry g))

/-- **THE SOURCED THEORY REALIZES THE SEALED OI CORE**: the passive step and the control are
transported permutations, the readout is the native readout, and the comb is the classical comb.
No phase is used. -/
theorem permTheory_realizesSealedOICore : RealizesSealedOICore (permTheory (Fin 2)) :=
  ⟨core_isC1C4, permTheory_relabel sigmaPerm, permTheory_relabel tauPerm,
    fun r => by rw [readVisible_eq_localLuders, readout_is_localLuders],
    by rw [readVisible_family_eq (permTheory (Fin 2))]; exact readout_relabel_available _,
    fun steps w => realizedFold_diagonal steps w⟩

/-- **THE FALSIFIER IS UNAVAILABLE IN THE SOURCED THEORY**, through its inclusion in the
substratum theory. -/
theorem permTheory_falsifierUnavailable : FalsifierUnavailable (permTheory (Fin 2)) :=
  fun h => substratumTheory_falsifierUnavailable (permTheory_availExt_le_substratum _ h)

/-- **THE SOURCED TWO-STATE THEORY**: the sourced closure with the sealed core, the falsifier
unavailable, and no quarter phase. -/
theorem permTheory_twoState :
    SourcedOI (permTheory (Fin 2)) ∧ RealizesSealedOICore (permTheory (Fin 2))
      ∧ FalsifierUnavailable (permTheory (Fin 2)) ∧ ¬ PhasesAvailable (permTheory (Fin 2)) :=
  ⟨permTheory_sourcedOI, permTheory_realizesSealedOICore, permTheory_falsifierUnavailable,
    permTheory_not_phasesAvailable⟩

end TwoState

/-! ### Section E — the observer theory of a substratum, and the sourcing theorems -/

section Observer

variable (𝒮 : Substratum) [Fintype 𝒮.ι] [Fintype 𝒮.V] [DecidableEq 𝒮.V]

/-- **THE OBSERVER THEORY OF A SUBSTRATUM**: the sourced theory on its configuration space,
under the finiteness A1 supplies. -/
noncomputable abbrev obsTheory : FiniteOperationalTheory 𝒮.Conf :=
  permTheory 𝒮.Conf

/-- **THE OBSERVER THEORY IS THE SOURCED THEORY ON THE CONFIGURATION SPACE**: the rule does not
occur in it. -/
theorem obsTheory_eq_permTheory : obsTheory 𝒮 = permTheory 𝒮.Conf := rfl

/-- **THE OBSERVER THEORY DOES NOT DEPEND ON THE RULE**: two substrata on the same sites and
alphabet have the same observer theory, whatever their rules. Configuration-level sourcing
consumes nothing of A3–A6. -/
theorem obsTheory_rule_independent (ι V : Type) [DecidableEq ι] [AddCommGroup ι] [AddCommGroup V]
    [Fintype ι] [Fintype V] [DecidableEq V] (R R' : Rule ι V) :
    obsTheory { ι := ι, V := V, R := R } = obsTheory { ι := ι, V := V, R := R' } := rfl

omit [DecidableEq 𝒮.V] in
/-- **A1 FOR THE OBSERVER THEORY'S SUBSTRATUM.** -/
theorem obs_a1 : 𝒮.A1 := Substratum.a1_of_finite 𝒮

/-- **SOURCING — THE SUBSTRATUM'S OWN UPDATE IS AVAILABLE** at every level, the ancilla a
spectator: a substrate fact, the bijectivity of `φ`, made an availability by the theorem. -/
theorem obs_dynamics_avail (n : ℕ) :
    (obsTheory 𝒮).availExt n Unit (fun _ => conjChannel (permMatrix (levelPerm 𝒮.φ n))) :=
  permTheory_avail_conj (permClass_permMatrix _) (permMatrix_isometry _)

/-- **SOURCING — THE INVERSE UPDATE IS AVAILABLE** (A2 reversibility as an operation). -/
theorem obs_dynamics_inv_avail (n : ℕ) :
    (obsTheory 𝒮).availExt n Unit (fun _ => conjChannel (permMatrix (levelPerm 𝒮.φ.symm n))) :=
  permTheory_avail_conj (permClass_permMatrix _) (permMatrix_isometry _)

/-- **SOURCING — THE SHEAR LAYER AT TIME ONE IS AVAILABLE.** -/
theorem obs_shear_avail (n : ℕ) :
    (obsTheory 𝒮).availExt n Unit
      (fun _ => conjChannel (permMatrix (levelPerm (shearEquiv 𝒮.R.F) n))) :=
  permTheory_avail_conj (permClass_permMatrix _) (permMatrix_isometry _)

/-- **SOURCING — THE SWAP LAYER AT TIME ONE IS AVAILABLE.** -/
theorem obs_swap_avail (n : ℕ) :
    (obsTheory 𝒮).availExt n Unit
      (fun _ => conjChannel (permMatrix (levelPerm (swapEquiv : 𝒮.Conf ≃ 𝒮.Conf) n))) :=
  permTheory_avail_conj (permClass_permMatrix _) (permMatrix_isometry _)

/-- **SOURCING — THE READ-WRITE OPERATORS ARE AVAILABLE** at every level. -/
theorem obs_readWriteAvailable : ReadWriteAvailable (obsTheory 𝒮) :=
  permTheory_sourcedOI.2.2.2

/-- **SOURCING — THE EXCHANGES ARE AVAILABLE** at every level. -/
theorem obs_exchangesAvailable : ExchangesAvailable (obsTheory 𝒮) :=
  permTheory_sourcedOI.2.2.1

/-- **SOURCING — EMBEDDED OBSERVATION**, from label invariance. -/
theorem obs_embeddedObservation : EmbeddedObservation (obsTheory 𝒮) :=
  permTheory_sourcedOI.2.1

/-- **SOURCING — REVERSIBLE IMPLEMENTATION LOCALITY**, from the closures. -/
theorem obs_reversibleImplementationLocality : ReversibleImplementationLocality (obsTheory 𝒮) :=
  permTheory_sourcedOI.1

/-- **THE OBSERVER THEORY SATISFIES THE SOURCED CLOSURE.** -/
theorem obs_sourcedOI : SourcedOI (obsTheory 𝒮) := permTheory_sourcedOI

/-- **A DIAGONAL UNITARY AVAILABLE IN THE OBSERVER THEORY IS A GLOBAL PHASE.** -/
theorem obs_diagonal_avail_only_scalar {n : ℕ} {d : 𝒮.Conf × Fin n → ℂ}
    (hav : (obsTheory 𝒮).availExt n Unit (fun _ => conjChannel (Matrix.diagonal d))) :
    ∀ p q, 0 ≤ d p * star (d q) :=
  permTheory_diagonal_only_scalar hav

/-- **THE OBSERVER THEORY LIES INSIDE THE SUBSTRATUM THEORY.** -/
theorem obs_availExt_le_substratum {n : ℕ} {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix (𝒮.Conf × Fin n) (𝒮.Conf × Fin n) ℂ →ₗ[ℂ] Matrix (𝒮.Conf × Fin n) (𝒮.Conf × Fin n) ℂ)
    (hF : (obsTheory 𝒮).availExt n O F) : (substratumTheory 𝒮.Conf).availExt n O F :=
  permTheory_availExt_le_substratum F hF

variable [Nonempty 𝒮.V]

/-- **THE OBSERVER THEORY CARRIES NO QUARTER PHASE.** -/
theorem obs_not_phasesAvailable : ¬ PhasesAvailable (obsTheory 𝒮) :=
  permTheory_not_phasesAvailable

/-- **THE OBSERVER THEORY FAILS `DerivedOI`.** -/
theorem obs_not_derivedOI : ¬ DerivedOI (obsTheory 𝒮) := permTheory_not_derivedOI

/-- **THE OBSERVER THEORY FAILS `SubstratumAvail`.** -/
theorem obs_not_substratumAvail : ¬ SubstratumAvail (obsTheory 𝒮) := permTheory_not_substratumAvail

/-- **THE OBSERVER THEORY HAS NO COMPOSITE UNITARY CONTROL.** -/
theorem obs_not_control : ¬ HasCompositeUnitaryControl (obsTheory 𝒮) := permTheory_not_control

/-- **THE OBSERVER THEORY FAILS PHASE-FREE RICHNESS.** -/
theorem obs_not_phaseFree : ¬ PhaseFreeRichness (obsTheory 𝒮) := permTheory_not_phaseFree

/-- **THE OBSERVER THEORY IS NOT QUANTUM MECHANICS.** -/
theorem obs_not_qm : ¬ ExactAllFiniteEndomorphicQuantumOps (obsTheory 𝒮) := permTheory_not_qm

/-- **UNDER THE SOURCED BASELINE, QUANTUM MECHANICS IS EXACTLY PHASE-FREE RICHNESS** for the
observer theory: the comparison the next round starts from. -/
theorem obs_qm_iff_phaseFree :
    ExactAllFiniteEndomorphicQuantumOps (obsTheory 𝒮) ↔ PhaseFreeRichness (obsTheory 𝒮) :=
  sourcedOI_qm_iff_phaseFree (obs_sourcedOI 𝒮)

end Observer

#print axioms Substratum.a2_every_substratum
#print axioms Substratum.a1_of_finite
#print axioms Substratum.a3_of_fintype
#print axioms Substratum.a4_of_exact
#print axioms dir_flip
#print axioms mem_nbrs_symm
#print axioms waveSubstratum_A1
#print axioms waveSubstratum_A2
#print axioms waveSubstratum_A3
#print axioms waveSubstratum_A4Exact
#print axioms waveSubstratum_A5
#print axioms scaledPartialPerm_iff
#print axioms scaled_one_aux
#print axioms scaled_mul
#print axioms scaled_smul
#print axioms scaled_diagonal_indicator
#print axioms scaled_block
#print axioms scaled_tensor_one
#print axioms scaled_reindex
#print axioms scaled_conjTranspose
#print axioms permClass_arch
#print axioms permClass_contextStable
#print axioms permClass_labelInvariant
#print axioms permClass_daggerStable
#print axioms permClass_permMatrix
#print axioms permClass_readWrite
#print axioms permClass_le_substratum
#print axioms ancBlock_flipOn
#print axioms permClass_le_of_exchanges
#print axioms permClass_bijectionLevel
#print axioms bijectionLevel_configurationLevel
#print axioms preservesNonneg_conj_of_scaled
#print axioms preservesNonneg_sum
#print axioms preservesNonneg_of_realized
#print axioms diagonal_nonneg_of_preservesNonneg
#print axioms phaseGate_not_preservesNonneg
#print axioms sign_not_preservesNonneg
#print axioms bijectionLevel_not_phasesAvailable
#print axioms bijectionLevel_diagonal_only_scalar
#print axioms permTheory_avail_conj
#print axioms derivedOI_iff_sourcedOI_phases
#print axioms sourcedOI_of_derivedOI
#print axioms sourcedOI_of_qm
#print axioms exchanges_of_readWrite
#print axioms sourcedOI_qm_iff_phaseFree
#print axioms permTheory_sourcedOI
#print axioms permTheory_not_phasesAvailable
#print axioms permTheory_diagonal_only_scalar
#print axioms permTheory_no_sign
#print axioms permTheory_not_derivedOI
#print axioms substratumAvail_phasesAvailable
#print axioms permTheory_not_substratumAvail
#print axioms permTheory_availExt_le_substratum
#print axioms permTheory_not_control
#print axioms permTheory_not_phaseFree
#print axioms permTheory_not_qm
#print axioms permTheory_relabel
#print axioms permTheory_realizesSealedOICore
#print axioms permTheory_falsifierUnavailable
#print axioms permTheory_twoState
#print axioms obsTheory_eq_permTheory
#print axioms obsTheory_rule_independent
#print axioms obs_a1
#print axioms obs_dynamics_avail
#print axioms obs_dynamics_inv_avail
#print axioms obs_shear_avail
#print axioms obs_swap_avail
#print axioms obs_readWriteAvailable
#print axioms obs_exchangesAvailable
#print axioms obs_embeddedObservation
#print axioms obs_reversibleImplementationLocality
#print axioms obs_sourcedOI
#print axioms obs_not_phasesAvailable
#print axioms obs_diagonal_avail_only_scalar
#print axioms obs_not_derivedOI
#print axioms obs_not_substratumAvail
#print axioms obs_availExt_le_substratum
#print axioms obs_not_control
#print axioms obs_not_phaseFree
#print axioms obs_not_qm
#print axioms obs_qm_iff_phaseFree

end SubstratumInterfaceAudit
end OIBridge
