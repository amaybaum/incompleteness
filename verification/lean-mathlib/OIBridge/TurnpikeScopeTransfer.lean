/-
  OIBridge/TurnpikeScopeTransfer.lean — real-to-integer scope transfer for the turnpike
  classification, and the conditional two-branch theorem with the INTEGER Bekir–Golomb
  classification as its only unproved premise.

  WHY THIS FILE EXISTS. The primary-source audit of Bekir–Golomb 2007 found exactly one
  equivocal point: the paper's polynomial model is integer-presented and never explicitly
  quantifies over real configurations, although the theorem it completes (Piccard 1939) is a
  real-Euclidean statement and its symbolic-exponent argument uses only linear relations.
  Rather than consuming the paper under a real-scope INTERPRETATION, this file removes the gap
  mathematically: a real realization of any fixed gap correspondence yields an INTEGER
  realization of the same correspondence, preserving strict ordering, Golombness, and
  nontriviality. Bekir–Golomb is then consumed in the integer scope its text unambiguously
  uses, and the real classification is derived, not assumed.

  THE TRANSFER. All realization constraints are homogeneous rational-linear: the correspondence
  identities are equalities, the orderings are strict inequalities, and Golombness plus the two
  nontriviality witnesses are inequations. The elementary density argument runs in three steps:

    1. `rational_point` — a real point satisfying finitely many rational strict/nonzero linear
       conditions has a rational point nearby satisfying the same, by choosing each coordinate
       in a small rational window (`exists_rat_btwn`) with an explicit ε/M error budget.
    2. `rational_solutions` — with equality constraints added: the entries of the real solution
       span a finite-dimensional ℚ-subspace of ℝ; expressing the solution in a ℚ-basis of that
       span, each basis coordinate SLICE is itself a rational solution of the equality system
       (linear independence over ℚ), so the real solution is a real combination of rational
       solutions and step 1 applies in the coefficient space.
    3. `exists_int_scaling` — clear denominators; every constraint is homogeneous.

  `integer_realization_of_real_realization` packages the three for a ruler pair with a fixed
  ascending-pair correspondence. `BGIntegerClassification` states the external premise — the
  2007 classification for INTEGER spanning rulers, in the spectral μ-form the wrapper consumes
  (nontrivial homometric Golomb integer pairs exist only at six marks, with gap data realizing
  the exceptional correspondence μ; the μ-form is justified by PiccardBridge, which
  kernel-proves that the paper's exceptional family realizes μ). `spectral_classification_of_BG`
  then derives the REAL spectral classification: the forced correspondence of the real pair is
  transferred to an integer pair, classified there, and the Golomb rigidity of the integer pair
  forces the combinatorial identification ν = relabeled-μ, which transports back to the real
  spectra. `twoBranch_of_BGClassification` composes with `twoBranch_of_spectral_classification`:
  equal transition probabilities + distinct gaps + the INTEGER premise give the two Hamiltonian
  branches over arbitrary real spectra.
-/
import OIBridge.CongruentReconstruction
import Mathlib.Data.Fin.Tuple.Sort

namespace OIBridge
namespace ScopeTransfer

open Finset

/-! ### Step 1: rational points near a real point, under strict and nonzero rational-linear
conditions -/

/-- **Rational approximation preserving finitely many strict/nonzero rational-linear
conditions.** The error budget is uniform: `δ = ε / M` with `ε` the least slack and `M`
dominating every row's absolute coefficient sum. -/
lemma rational_point {σ κs κn : Type*} [Fintype σ] [Fintype κs] [Fintype κn]
    (A : κs → σ → ℚ) (B : κn → σ → ℚ) (e : σ → ℝ)
    (hA : ∀ j, 0 < ∑ t, (A j t : ℝ) * e t)
    (hB : ∀ k, (∑ t, (B k t : ℝ) * e t) ≠ 0) :
    ∃ r : σ → ℚ, (∀ j, 0 < ∑ t, (A j t : ℝ) * (r t : ℝ))
      ∧ ∀ k, (∑ t, (B k t : ℝ) * (r t : ℝ)) ≠ 0 := by
  classical
  set M : ℝ := 1 + (∑ j, ∑ t, |(A j t : ℝ)|) + (∑ k, ∑ t, |(B k t : ℝ)|) with hMdef
  have hAnn : (0 : ℝ) ≤ ∑ j, ∑ t, |(A j t : ℝ)| :=
    Finset.sum_nonneg fun j _ => Finset.sum_nonneg fun t _ => abs_nonneg _
  have hBnn : (0 : ℝ) ≤ ∑ k, ∑ t, |(B k t : ℝ)| :=
    Finset.sum_nonneg fun k _ => Finset.sum_nonneg fun t _ => abs_nonneg _
  have hM1 : 1 ≤ M := by simp only [hMdef]; linarith
  have hM0 : 0 < M := lt_of_lt_of_le one_pos hM1
  have hrowA : ∀ j, ∑ t, |(A j t : ℝ)| ≤ M - 1 := by
    intro j
    have h1 : ∑ t, |(A j t : ℝ)| ≤ ∑ j', ∑ t, |(A j' t : ℝ)| :=
      Finset.single_le_sum (f := fun j' => ∑ t, |(A j' t : ℝ)|)
        (fun j' _ => Finset.sum_nonneg fun t _ => abs_nonneg _) (Finset.mem_univ j)
    simp only [hMdef]; linarith
  have hrowB : ∀ k, ∑ t, |(B k t : ℝ)| ≤ M - 1 := by
    intro k
    have h1 : ∑ t, |(B k t : ℝ)| ≤ ∑ k', ∑ t, |(B k' t : ℝ)| :=
      Finset.single_le_sum (f := fun k' => ∑ t, |(B k' t : ℝ)|)
        (fun k' _ => Finset.sum_nonneg fun t _ => abs_nonneg _) (Finset.mem_univ k)
    simp only [hMdef]; linarith
  -- the least slack, with 1 inserted so the finite set is never empty
  set vals : Finset ℝ := insert 1
    ((Finset.univ.image fun j => ∑ t, (A j t : ℝ) * e t)
      ∪ (Finset.univ.image fun k => |∑ t, (B k t : ℝ) * e t|)) with hvals
  have hvne : vals.Nonempty := ⟨1, Finset.mem_insert_self _ _⟩
  set ε : ℝ := vals.min' hvne with hεdef
  have hε0 : 0 < ε := by
    rw [hεdef, Finset.lt_min'_iff]
    intro y hy
    rcases Finset.mem_insert.mp hy with h | h
    · rw [h]; exact one_pos
    rcases Finset.mem_union.mp h with h | h
    · obtain ⟨j, _, rfl⟩ := Finset.mem_image.mp h; exact hA j
    · obtain ⟨k, _, rfl⟩ := Finset.mem_image.mp h; exact abs_pos.mpr (hB k)
  have hεA : ∀ j, ε ≤ ∑ t, (A j t : ℝ) * e t := fun j =>
    Finset.min'_le _ _ (Finset.mem_insert_of_mem (Finset.mem_union_left _
      (Finset.mem_image_of_mem _ (Finset.mem_univ j))))
  have hεB : ∀ k, ε ≤ |∑ t, (B k t : ℝ) * e t| := fun k =>
    Finset.min'_le _ _ (Finset.mem_insert_of_mem (Finset.mem_union_right _
      (Finset.mem_image_of_mem _ (Finset.mem_univ k))))
  set δ : ℝ := ε / M with hδdef
  have hδ0 : 0 < δ := div_pos hε0 hM0
  have hδM : δ * (M - 1) = ε - δ := by
    rw [hδdef]; field_simp
  -- pick each coordinate in a rational window of width 2δ
  have hpick : ∀ t, ∃ q : ℚ, e t - δ < (q : ℝ) ∧ (q : ℝ) < e t + δ := fun t =>
    exists_rat_btwn (by linarith)
  choose r hr1 hr2 using hpick
  have habs : ∀ t, |(r t : ℝ) - e t| < δ := fun t =>
    abs_sub_lt_iff.mpr ⟨by linarith [hr2 t], by linarith [hr1 t]⟩
  -- the uniform error estimate for any rational row
  have key : ∀ a : σ → ℚ,
      |(∑ t, (a t : ℝ) * (r t : ℝ)) - ∑ t, (a t : ℝ) * e t| ≤ δ * ∑ t, |(a t : ℝ)| := by
    intro a
    rw [← Finset.sum_sub_distrib]
    calc |∑ t, ((a t : ℝ) * (r t : ℝ) - (a t : ℝ) * e t)|
        ≤ ∑ t, |(a t : ℝ) * (r t : ℝ) - (a t : ℝ) * e t| := Finset.abs_sum_le_sum_abs _ _
      _ = ∑ t, |(a t : ℝ)| * |(r t : ℝ) - e t| := by
          refine Finset.sum_congr rfl fun t _ => ?_
          rw [← mul_sub, abs_mul]
      _ ≤ ∑ t, |(a t : ℝ)| * δ :=
          Finset.sum_le_sum fun t _ =>
            mul_le_mul_of_nonneg_left (le_of_lt (habs t)) (abs_nonneg _)
      _ = δ * ∑ t, |(a t : ℝ)| := by rw [← Finset.sum_mul, mul_comm]
  refine ⟨r, fun j => ?_, fun k => ?_⟩
  · have h1 := key (A j)
    have h2 := hrowA j
    have h3 := hεA j
    have h4 : δ * ∑ t, |(A j t : ℝ)| ≤ δ * (M - 1) :=
      mul_le_mul_of_nonneg_left h2 hδ0.le
    have h5 := (abs_le.mp h1).1
    linarith
  · have h1 := key (B k)
    have h2 := hrowB k
    have h3 := hεB k
    have h4 : δ * ∑ t, |(B k t : ℝ)| ≤ δ * (M - 1) :=
      mul_le_mul_of_nonneg_left h2 hδ0.le
    have h5 : |∑ t, (B k t : ℝ) * e t| - |∑ t, (B k t : ℝ) * (r t : ℝ)|
        ≤ |(∑ t, (B k t : ℝ) * (r t : ℝ)) - ∑ t, (B k t : ℝ) * e t| := by
      rw [abs_sub_comm]
      exact abs_sub_abs_le_abs_sub _ _
    have h6 : 0 < |∑ t, (B k t : ℝ) * (r t : ℝ)| := by linarith
    exact abs_pos.mp h6

/-! ### Step 2: rational solutions of a mixed rational-linear system near a real solution -/

/-- **RATIONAL SOLUTIONS ARE DENSE, elementarily.** Any real solution of a rational-linear
system of equalities, strict inequalities, and inequations admits a rational solution of the
same system. The proof needs no polyhedra and no topology: the entries of the real solution
span a finite-dimensional ℚ-subspace of ℝ; in a ℚ-basis of that span, each coordinate slice of
the solution is itself a rational solution of the equality subsystem, so the real solution is a
real combination of rational solutions, and `rational_point` finds rational combination
coefficients preserving the strict conditions. -/
theorem rational_solutions {ι κe κs κn : Type*}
    [Fintype ι] [Fintype κe] [Fintype κs] [Fintype κn]
    (T : κe → ι → ℚ) (U : κs → ι → ℚ) (V : κn → ι → ℚ) (z : ι → ℝ)
    (heq : ∀ k, ∑ i, (T k i : ℝ) * z i = 0)
    (hpos : ∀ j, 0 < ∑ i, (U j i : ℝ) * z i)
    (hne : ∀ k, (∑ i, (V k i : ℝ) * z i) ≠ 0) :
    ∃ q : ι → ℚ, (∀ k, ∑ i, (T k i : ℝ) * (q i : ℝ) = 0)
      ∧ (∀ j, 0 < ∑ i, (U j i : ℝ) * (q i : ℝ))
      ∧ ∀ k, (∑ i, (V k i : ℝ) * (q i : ℝ)) ≠ 0 := by
  classical
  -- the ℚ-span of the solution's entries, and a finite ℚ-basis of it
  set S : Submodule ℚ ℝ := Submodule.span ℚ (Set.range z) with hSdef
  have : FiniteDimensional ℚ S := FiniteDimensional.span_of_finite ℚ (Set.finite_range z)
  set b := Module.finBasis ℚ S with hbdef
  set zv : ι → S := fun i => ⟨z i, Submodule.subset_span (Set.mem_range_self i)⟩ with hzvdef
  set c : ι → Fin (Module.finrank ℚ S) → ℚ := fun i t => b.repr (zv i) t with hcdef
  -- decomposition of each entry along the basis
  have hz : ∀ i, z i = ∑ t, (c i t : ℝ) * ((b t : S) : ℝ) := by
    intro i
    have h1 := b.sum_repr (zv i)
    have h2 : ((∑ t, b.repr (zv i) t • b t : S) : ℝ) = ((zv i : S) : ℝ) := by rw [h1]
    rw [show ((zv i : S) : ℝ) = z i from rfl] at h2
    rw [← h2, AddSubmonoidClass.coe_finsetSum]
    refine (Finset.sum_congr rfl fun t _ => ?_).symm
    rw [SetLike.val_smul, Rat.smul_def]
  -- each basis-coordinate slice is a rational solution of the equality system
  have hslice : ∀ k t, ∑ i, T k i * c i t = 0 := by
    intro k t
    have h0 : (∑ i, T k i • zv i) = (0 : S) := by
      apply Subtype.ext
      rw [AddSubmonoidClass.coe_finsetSum]
      rw [show ((0 : S) : ℝ) = 0 from rfl, ← heq k]
      refine Finset.sum_congr rfl fun i _ => ?_
      rw [SetLike.val_smul, Rat.smul_def]
    have h1 : b.repr (∑ i, T k i • zv i) = ∑ i, T k i • b.repr (zv i) := by
      rw [map_sum]
      exact Finset.sum_congr rfl fun i _ => by rw [map_smul]
    rw [h0, map_zero] at h1
    have h2 := congrArg (fun f => f t) h1.symm
    simpa [Finsupp.finsetSum_apply, Finsupp.smul_apply, smul_eq_mul] using h2
  -- transform each strict/nonzero row into the coefficient space
  set AU : κs → Fin (Module.finrank ℚ S) → ℚ := fun j t => ∑ i, U j i * c i t with hAUdef
  set AV : κn → Fin (Module.finrank ℚ S) → ℚ := fun k t => ∑ i, V k i * c i t with hAVdef
  have hval : ∀ a : ι → ℚ,
      ∑ t, ((∑ i, a i * c i t : ℚ) : ℝ) * ((b t : S) : ℝ) = ∑ i, (a i : ℝ) * z i := by
    intro a
    have h1 : ∀ t, ((∑ i, a i * c i t : ℚ) : ℝ) * ((b t : S) : ℝ)
        = ∑ i, (a i : ℝ) * ((c i t : ℝ) * ((b t : S) : ℝ)) := by
      intro t
      push_cast
      rw [Finset.sum_mul]
      exact Finset.sum_congr rfl fun i _ => by ring
    rw [Finset.sum_congr rfl fun t _ => h1 t, Finset.sum_comm]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [← Finset.mul_sum, ← hz i]
  obtain ⟨r, hrpos, hrne⟩ := rational_point AU AV (fun t => ((b t : S) : ℝ))
    (fun j => by
      show 0 < ∑ t, ((AU j t : ℚ) : ℝ) * ((b t : S) : ℝ)
      simp only [hAUdef]
      rw [hval (U j)]
      exact hpos j)
    (fun k => by
      show (∑ t, ((AV k t : ℚ) : ℝ) * ((b t : S) : ℝ)) ≠ 0
      simp only [hAVdef]
      rw [hval (V k)]
      exact hne k)
  -- assemble the rational solution
  set q : ι → ℚ := fun i => ∑ t, c i t * r t with hqdef
  have hswap : ∀ a : ι → ℚ, (∑ i, a i * q i) = ∑ t, (∑ i, a i * c i t) * r t := by
    intro a
    calc (∑ i, a i * q i) = ∑ i, ∑ t, a i * c i t * r t := by
          refine Finset.sum_congr rfl fun i _ => ?_
          simp only [hqdef]
          rw [Finset.mul_sum]
          exact Finset.sum_congr rfl fun t _ => by ring
      _ = ∑ t, ∑ i, a i * c i t * r t := Finset.sum_comm
      _ = ∑ t, (∑ i, a i * c i t) * r t := by
          exact Finset.sum_congr rfl fun t _ => (Finset.sum_mul _ _ _).symm
  refine ⟨q, fun k => ?_, fun j => ?_, fun k => ?_⟩
  · have h1 : (∑ i, T k i * q i) = 0 := by
      rw [hswap (T k)]
      refine Finset.sum_eq_zero fun t _ => ?_
      rw [hslice k t, zero_mul]
    exact_mod_cast h1
  · have h1 : (0 : ℚ) < ∑ t, AU j t * r t := by exact_mod_cast hrpos j
    have h2 : (0 : ℚ) < ∑ i, U j i * q i := by
      rw [hswap (U j)]
      simpa only [hAUdef] using h1
    exact_mod_cast h2
  · have h1 : (∑ t, AV k t * r t) ≠ 0 := fun h => hrne k (by exact_mod_cast congrArg (fun x : ℚ => (x : ℝ)) h)
    have h2 : (∑ i, V k i * q i) ≠ 0 := by
      rw [hswap (V k)]
      simpa only [hAVdef] using h1
    intro h
    exact h2 (by exact_mod_cast h)

/-! ### Step 3: clearing denominators -/

/-- A rational vector scales by a positive integer to an integer vector. -/
lemma exists_int_scaling {ι : Type*} [Fintype ι] (q : ι → ℚ) :
    ∃ (N : ℕ) (F : ι → ℤ), 0 < N ∧ ∀ i, (F i : ℚ) = (N : ℚ) * q i := by
  classical
  refine ⟨∏ i, (q i).den, fun i => (∏ j ∈ Finset.univ.erase i, ((q j).den : ℤ)) * (q i).num,
    Finset.prod_pos fun i _ => (q i).den_pos, fun i => ?_⟩
  have hsplit : (∏ j, (q j).den) = (q i).den * ∏ j ∈ Finset.univ.erase i, (q j).den :=
    (Finset.mul_prod_erase _ _ (Finset.mem_univ i)).symm
  have hden : ((q i).den : ℚ) * q i = (q i).num := by
    rw [Rat.mul_comm, Rat.mul_den_eq_num]
  push_cast
  have hsplitQ : (∏ j, ((q j).den : ℚ))
      = ((q i).den : ℚ) * ∏ j ∈ Finset.univ.erase i, ((q j).den : ℚ) := by
    exact_mod_cast congrArg (fun n : ℕ => (n : ℚ)) hsplit
  rw [hsplitQ, ← hden]
  ring

/-! ### The four-term signed indicator rows every realization constraint fits into -/

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- A four-term signed indicator row: the linear form `s₁·z i₁ + s₂·z i₂ + s₃·z i₃ + s₄·z i₄`
as a coefficient vector. Two-term forms take `s₃ = s₄ = 0`. -/
def row (s1 s2 s3 s4 : ℚ) (i1 i2 i3 i4 : ι) : ι → ℚ := fun i =>
  s1 * (if i = i1 then 1 else 0) + s2 * (if i = i2 then 1 else 0)
    + s3 * (if i = i3 then 1 else 0) + s4 * (if i = i4 then 1 else 0)

lemma row_eval (z : ι → ℝ) (s1 s2 s3 s4 : ℚ) (i1 i2 i3 i4 : ι) :
    ∑ i, (row s1 s2 s3 s4 i1 i2 i3 i4 i : ℝ) * z i
      = (s1 : ℝ) * z i1 + (s2 : ℝ) * z i2 + (s3 : ℝ) * z i3 + (s4 : ℝ) * z i4 := by
  classical
  have h : ∀ (s : ℚ) (i0 : ι),
      ∑ i, ((s * (if i = i0 then 1 else 0) : ℚ) : ℝ) * z i = (s : ℝ) * z i0 := by
    intro s i0
    rw [Finset.sum_eq_single i0]
    · simp
    · intro i _ hne
      simp [hne]
    · intro h
      exact absurd (Finset.mem_univ i0) h
  have hsplit : ∑ i, (row s1 s2 s3 s4 i1 i2 i3 i4 i : ℝ) * z i
      = (∑ i, ((s1 * (if i = i1 then 1 else 0) : ℚ) : ℝ) * z i)
        + (∑ i, ((s2 * (if i = i2 then 1 else 0) : ℚ) : ℝ) * z i)
        + (∑ i, ((s3 * (if i = i3 then 1 else 0) : ℚ) : ℝ) * z i)
        + (∑ i, ((s4 * (if i = i4 then 1 else 0) : ℚ) : ℝ) * z i) := by
    rw [← Finset.sum_add_distrib, ← Finset.sum_add_distrib, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [row]
    push_cast
    ring
  rw [hsplit, h, h, h, h]

/-! ### The scope transfer for ruler pairs -/

/-- Ascending index pairs — the edges every correspondence acts on. -/
abbrev AscPair (n : ℕ) := {p : Fin n × Fin n // p.1 < p.2}

/-- **INTEGER REALIZATION OF A REAL REALIZATION.** A real ruler pair realizing a fixed
ascending-pair correspondence ν — strictly ordered, Golomb on both sides, and nontrivial
(witnessed failures of translation- and reflection-congruence) — yields an INTEGER ruler pair
realizing the SAME ν with all those properties. Every constraint is a homogeneous rational
four-term linear form, so `rational_solutions` and `exists_int_scaling` close it. -/
theorem integer_realization_of_real_realization {n : ℕ}
    (ν : AscPair n → Fin n × Fin n) (E E' : Fin n → ℝ)
    (hmono : StrictMono E) (hmono' : StrictMono E')
    (hglm : ∀ a b c d : Fin n, a < b → c < d → E b - E a = E d - E c → a = c ∧ b = d)
    (hglm' : ∀ a b c d : Fin n, a < b → c < d → E' b - E' a = E' d - E' c → a = c ∧ b = d)
    (hnu : ∀ p : AscPair n, E' (ν p).2 - E' (ν p).1 = E p.1.2 - E p.1.1)
    {i₀ j₀ : Fin n} (hnt : E' i₀ - E i₀ ≠ E' j₀ - E j₀)
    {i₁ j₁ : Fin n} (hnr : E' i₁ + E i₁.rev ≠ E' j₁ + E j₁.rev) :
    ∃ F F' : Fin n → ℤ, StrictMono F ∧ StrictMono F'
      ∧ (∀ a b c d : Fin n, a < b → c < d → F b - F a = F d - F c → a = c ∧ b = d)
      ∧ (∀ a b c d : Fin n, a < b → c < d → F' b - F' a = F' d - F' c → a = c ∧ b = d)
      ∧ (∀ p : AscPair n, F' (ν p).2 - F' (ν p).1 = F p.1.2 - F p.1.1)
      ∧ F' i₀ - F i₀ ≠ F' j₀ - F j₀
      ∧ F' i₁ + F i₁.rev ≠ F' j₁ + F j₁.rev := by
  classical
  set z : Fin n ⊕ Fin n → ℝ := Sum.elim E E' with hzdef
  -- the equality rows: the ν-identities
  set T : AscPair n → (Fin n ⊕ Fin n) → ℚ := fun p =>
    row 1 (-1) (-1) 1 (.inr (ν p).2) (.inr (ν p).1) (.inl p.1.2) (.inl p.1.1) with hTdef
  -- the strict rows: both orderings, over every ascending pair
  set U : (AscPair n ⊕ AscPair n) → (Fin n ⊕ Fin n) → ℚ := fun j =>
    match j with
    | .inl p => row 1 (-1) 0 0 (.inl p.1.2) (.inl p.1.1) (.inl p.1.1) (.inl p.1.1)
    | .inr p => row 1 (-1) 0 0 (.inr p.1.2) (.inr p.1.1) (.inr p.1.1) (.inr p.1.1)
    with hUdef
  -- the nonzero rows: Golombness of both sides, and the two nontriviality witnesses
  set V : (({x : AscPair n × AscPair n // x.1 ≠ x.2}
        ⊕ {x : AscPair n × AscPair n // x.1 ≠ x.2}) ⊕ (Unit ⊕ Unit))
      → (Fin n ⊕ Fin n) → ℚ := fun k =>
    match k with
    | .inl (.inl x) => row 1 (-1) (-1) 1
        (.inl x.1.1.1.2) (.inl x.1.1.1.1) (.inl x.1.2.1.2) (.inl x.1.2.1.1)
    | .inl (.inr x) => row 1 (-1) (-1) 1
        (.inr x.1.1.1.2) (.inr x.1.1.1.1) (.inr x.1.2.1.2) (.inr x.1.2.1.1)
    | .inr (.inl _) => row 1 (-1) (-1) 1 (.inr i₀) (.inl i₀) (.inr j₀) (.inl j₀)
    | .inr (.inr _) => row 1 1 (-1) (-1) (.inr i₁) (.inl i₁.rev) (.inr j₁) (.inl j₁.rev)
    with hVdef
  have heq : ∀ p, ∑ i, (T p i : ℝ) * z i = 0 := by
    intro p
    simp only [hTdef]
    rw [row_eval]
    simp only [hzdef, Sum.elim_inr, Sum.elim_inl]
    push_cast
    linear_combination hnu p
  have hpos : ∀ j, 0 < ∑ i, (U j i : ℝ) * z i := by
    rintro (p | p) <;>
      · simp only [hUdef]
        rw [row_eval]
        simp only [hzdef, Sum.elim_inr, Sum.elim_inl]
        push_cast
        first
          | linarith [hmono p.2]
          | linarith [hmono' p.2]
  have hne : ∀ k, (∑ i, (V k i : ℝ) * z i) ≠ 0 := by
    rintro ((x | x) | (u | u)) <;>
      · simp only [hVdef]
        rw [row_eval]
        simp only [hzdef, Sum.elim_inr, Sum.elim_inl]
        push_cast
        first
          | · intro h
              exact x.2 (Subtype.ext (Prod.ext
                ((hglm _ _ _ _ x.1.1.2 x.1.2.2 (by linarith)).1.symm ▸ rfl)
                (by simp [(hglm _ _ _ _ x.1.1.2 x.1.2.2 (by linarith)).2])))
          | · intro h
              exact x.2 (Subtype.ext (Prod.ext
                ((hglm' _ _ _ _ x.1.1.2 x.1.2.2 (by linarith)).1.symm ▸ rfl)
                (by simp [(hglm' _ _ _ _ x.1.1.2 x.1.2.2 (by linarith)).2])))
          | · intro h
              exact hnt (by linarith)
          | · intro h
              exact hnr (by linarith)
  obtain ⟨q, hqeq, hqpos, hqne⟩ := rational_solutions T U V z heq hpos hne
  obtain ⟨N, G, hN, hGq⟩ := exists_int_scaling q
  -- a uniform bridge from row facts about q to signed combinations of G
  have hrowq : ∀ (s1 s2 s3 s4 : ℚ) (i1 i2 i3 i4 : Fin n ⊕ Fin n),
      (∑ i, (row s1 s2 s3 s4 i1 i2 i3 i4 i : ℝ) * (q i : ℝ))
        = ((s1 * q i1 + s2 * q i2 + s3 * q i3 + s4 * q i4 : ℚ) : ℝ) := by
    intro s1 s2 s3 s4 i1 i2 i3 i4
    rw [row_eval]
    push_cast
    ring
  have hGcomb : ∀ (s1 s2 s3 s4 : ℚ) (i1 i2 i3 i4 : Fin n ⊕ Fin n),
      (s1 * (G i1 : ℚ) + s2 * (G i2 : ℚ) + s3 * (G i3 : ℚ) + s4 * (G i4 : ℚ))
        = (N : ℚ) * (s1 * q i1 + s2 * q i2 + s3 * q i3 + s4 * q i4) := by
    intro s1 s2 s3 s4 i1 i2 i3 i4
    rw [hGq, hGq, hGq, hGq]
    ring
  have hNQ : (0 : ℚ) < (N : ℚ) := by exact_mod_cast hN
  refine ⟨G ∘ Sum.inl, G ∘ Sum.inr, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · -- StrictMono F
    intro a b hab
    have h1 := hqpos (.inl ⟨(a, b), hab⟩)
    rw [show U (.inl ⟨(a, b), hab⟩)
      = row 1 (-1) 0 0 (.inl b) (.inl a) (.inl a) (.inl a) from rfl, hrowq] at h1
    have h2 : (0 : ℚ) < 1 * q (.inl b) + (-1) * q (.inl a) + 0 * q (.inl a) + 0 * q (.inl a) := by
      exact_mod_cast h1
    have h3 := hGcomb 1 (-1) 0 0 (.inl b) (.inl a) (.inl a) (.inl a)
    have h4 : (0 : ℚ) < 1 * (G (.inl b) : ℚ) + (-1) * (G (.inl a) : ℚ)
        + 0 * (G (.inl a) : ℚ) + 0 * (G (.inl a) : ℚ) := by
      rw [h3]
      exact mul_pos hNQ h2
    have h5 : (G (.inl a) : ℚ) < (G (.inl b) : ℚ) := by linarith
    exact_mod_cast h5
  · -- StrictMono F'
    intro a b hab
    have h1 := hqpos (.inr ⟨(a, b), hab⟩)
    rw [show U (.inr ⟨(a, b), hab⟩)
      = row 1 (-1) 0 0 (.inr b) (.inr a) (.inr a) (.inr a) from rfl, hrowq] at h1
    have h2 : (0 : ℚ) < 1 * q (.inr b) + (-1) * q (.inr a) + 0 * q (.inr a) + 0 * q (.inr a) := by
      exact_mod_cast h1
    have h3 := hGcomb 1 (-1) 0 0 (.inr b) (.inr a) (.inr a) (.inr a)
    have h4 : (0 : ℚ) < 1 * (G (.inr b) : ℚ) + (-1) * (G (.inr a) : ℚ)
        + 0 * (G (.inr a) : ℚ) + 0 * (G (.inr a) : ℚ) := by
      rw [h3]
      exact mul_pos hNQ h2
    have h5 : (G (.inr a) : ℚ) < (G (.inr b) : ℚ) := by linarith
    exact_mod_cast h5
  · -- Golomb F
    intro a b c d hab hcd hFeq
    by_cases hpp : (⟨(a, b), hab⟩ : AscPair n) = ⟨(c, d), hcd⟩
    · have := congrArg Subtype.val hpp
      exact ⟨congrArg Prod.fst this, congrArg Prod.snd this⟩
    · exfalso
      have h1 := hqne (.inl (.inl ⟨(⟨(a, b), hab⟩, ⟨(c, d), hcd⟩), hpp⟩))
      rw [show V (.inl (.inl ⟨(⟨(a, b), hab⟩, ⟨(c, d), hcd⟩), hpp⟩))
        = row 1 (-1) (-1) 1 (.inl b) (.inl a) (.inl d) (.inl c) from rfl, hrowq] at h1
      have h2 : (1 * q (.inl b) + (-1) * q (.inl a) + (-1) * q (.inl d) + 1 * q (.inl c) : ℚ)
          ≠ 0 := fun h => h1 (by exact_mod_cast congrArg (fun x : ℚ => (x : ℝ)) h)
      have h3 := hGcomb 1 (-1) (-1) 1 (.inl b) (.inl a) (.inl d) (.inl c)
      have h4 : (1 * (G (.inl b) : ℚ) + (-1) * (G (.inl a) : ℚ)
          + (-1) * (G (.inl d) : ℚ) + 1 * (G (.inl c) : ℚ)) ≠ 0 := by
        rw [h3]
        exact mul_ne_zero hNQ.ne' h2
      have h5 : (G (.inl b) : ℚ) - G (.inl a) - G (.inl d) + G (.inl c) ≠ 0 := by
        intro h
        exact h4 (by linarith)
      apply h5
      have hQ : (G (.inl b) : ℚ) - G (.inl a) = (G (.inl d) : ℚ) - G (.inl c) := by
        exact_mod_cast hFeq
      linarith
  · -- Golomb F'
    intro a b c d hab hcd hFeq
    by_cases hpp : (⟨(a, b), hab⟩ : AscPair n) = ⟨(c, d), hcd⟩
    · have := congrArg Subtype.val hpp
      exact ⟨congrArg Prod.fst this, congrArg Prod.snd this⟩
    · exfalso
      have h1 := hqne (.inl (.inr ⟨(⟨(a, b), hab⟩, ⟨(c, d), hcd⟩), hpp⟩))
      rw [show V (.inl (.inr ⟨(⟨(a, b), hab⟩, ⟨(c, d), hcd⟩), hpp⟩))
        = row 1 (-1) (-1) 1 (.inr b) (.inr a) (.inr d) (.inr c) from rfl, hrowq] at h1
      have h2 : (1 * q (.inr b) + (-1) * q (.inr a) + (-1) * q (.inr d) + 1 * q (.inr c) : ℚ)
          ≠ 0 := fun h => h1 (by exact_mod_cast congrArg (fun x : ℚ => (x : ℝ)) h)
      have h3 := hGcomb 1 (-1) (-1) 1 (.inr b) (.inr a) (.inr d) (.inr c)
      have h4 : (1 * (G (.inr b) : ℚ) + (-1) * (G (.inr a) : ℚ)
          + (-1) * (G (.inr d) : ℚ) + 1 * (G (.inr c) : ℚ)) ≠ 0 := by
        rw [h3]
        exact mul_ne_zero hNQ.ne' h2
      have h5 : (G (.inr b) : ℚ) - G (.inr a) - G (.inr d) + G (.inr c) ≠ 0 := by
        intro h
        exact h4 (by linarith)
      apply h5
      have hQ : (G (.inr b) : ℚ) - G (.inr a) = (G (.inr d) : ℚ) - G (.inr c) := by
        exact_mod_cast hFeq
      linarith
  · -- the ν-identities
    intro p
    have h1 := hqeq p
    rw [show T p = row 1 (-1) (-1) 1 (.inr (ν p).2) (.inr (ν p).1) (.inl p.1.2) (.inl p.1.1)
      from rfl, hrowq] at h1
    have h2 : (1 * q (.inr (ν p).2) + (-1) * q (.inr (ν p).1)
        + (-1) * q (.inl p.1.2) + 1 * q (.inl p.1.1) : ℚ) = 0 := by
      exact_mod_cast h1
    have h3 := hGcomb 1 (-1) (-1) 1 (.inr (ν p).2) (.inr (ν p).1) (.inl p.1.2) (.inl p.1.1)
    have h4 : (1 * (G (.inr (ν p).2) : ℚ) + (-1) * (G (.inr (ν p).1) : ℚ)
        + (-1) * (G (.inl p.1.2) : ℚ) + 1 * (G (.inl p.1.1) : ℚ)) = 0 := by
      rw [h3, h2, mul_zero]
    have h5 : (G (.inr (ν p).2) : ℚ) - G (.inr (ν p).1) = (G (.inl p.1.2) : ℚ) - G (.inl p.1.1) := by
      linarith
    exact_mod_cast h5
  · -- not a translate
    intro hcon
    have h1 := hqne (.inr (.inl ()))
    rw [show V (.inr (.inl ()))
      = row 1 (-1) (-1) 1 (.inr i₀) (.inl i₀) (.inr j₀) (.inl j₀) from rfl, hrowq] at h1
    have h2 : (1 * q (.inr i₀) + (-1) * q (.inl i₀) + (-1) * q (.inr j₀) + 1 * q (.inl j₀) : ℚ)
        ≠ 0 := fun h => h1 (by exact_mod_cast congrArg (fun x : ℚ => (x : ℝ)) h)
    have h3 := hGcomb 1 (-1) (-1) 1 (.inr i₀) (.inl i₀) (.inr j₀) (.inl j₀)
    have h4 : (1 * (G (.inr i₀) : ℚ) + (-1) * (G (.inl i₀) : ℚ)
        + (-1) * (G (.inr j₀) : ℚ) + 1 * (G (.inl j₀) : ℚ)) ≠ 0 := by
      rw [h3]
      exact mul_ne_zero hNQ.ne' h2
    apply h4
    simp only [Function.comp_apply] at hcon
    have hQ : (G (Sum.inr i₀) : ℚ) - G (Sum.inl i₀) = (G (Sum.inr j₀) : ℚ) - G (Sum.inl j₀) := by
      exact_mod_cast hcon
    linarith
  · -- not a reflection
    intro hcon
    have h1 := hqne (.inr (.inr ()))
    rw [show V (.inr (.inr ()))
      = row 1 1 (-1) (-1) (.inr i₁) (.inl i₁.rev) (.inr j₁) (.inl j₁.rev) from rfl, hrowq] at h1
    have h2 : (1 * q (.inr i₁) + 1 * q (.inl i₁.rev) + (-1) * q (.inr j₁)
        + (-1) * q (.inl j₁.rev) : ℚ) ≠ 0 :=
      fun h => h1 (by exact_mod_cast congrArg (fun x : ℚ => (x : ℝ)) h)
    have h3 := hGcomb 1 1 (-1) (-1) (.inr i₁) (.inl i₁.rev) (.inr j₁) (.inl j₁.rev)
    have h4 : (1 * (G (.inr i₁) : ℚ) + 1 * (G (.inl i₁.rev) : ℚ)
        + (-1) * (G (.inr j₁) : ℚ) + (-1) * (G (.inl j₁.rev) : ℚ)) ≠ 0 := by
      rw [h3]
      exact mul_ne_zero hNQ.ne' h2
    apply h4
    simp only [Function.comp_apply] at hcon
    have hQ : (G (Sum.inr i₁) : ℚ) + G (Sum.inl i₁.rev)
        = (G (Sum.inr j₁) : ℚ) + G (Sum.inl j₁.rev) := by
      exact_mod_cast hcon
    linarith

/-! ### The external premise, and the conditional real classification -/

open HomometricSix in
/-- **THE EXTERNAL INTEGER PREMISE — Bekir–Golomb 2007, in the spectral form this repository
consumes.** Any two strictly increasing INTEGER rulers with distinct internal differences and
equal difference sets that are neither translates nor reflections of one another exist only at
six marks, with gap data realizing the exceptional correspondence μ through explicit
relabelings (the equivalences force `n = 6` with no casts). The μ-form of the exceptional
clause is backed by `PiccardBridge`: the paper's own two-parameter family is kernel-proved to
realize μ this way. This `Prop` is the ONLY unproved input of the reconstruction programme. -/
def BGIntegerClassification : Prop :=
  ∀ (n : ℕ) (F F' : Fin n → ℤ),
    StrictMono F → StrictMono F' →
    (∀ a b c d : Fin n, a < b → c < d → F b - F a = F d - F c → a = c ∧ b = d) →
    (∀ a b c d : Fin n, a < b → c < d → F' b - F' a = F' d - F' c → a = c ∧ b = d) →
    (Finset.image (fun p : AscPair n => F p.1.2 - F p.1.1) Finset.univ
      = Finset.image (fun p : AscPair n => F' p.1.2 - F' p.1.1) Finset.univ) →
    (¬ ∃ c : ℤ, ∀ i, F' i = F i + c) →
    (¬ ∃ c : ℤ, ∀ i, F' i = c - F i.rev) →
    ∃ eS eT : Fin 6 ≃ Fin n, ∀ a b : Fin 6, a < b →
      F' (eT (mu a b).2) - F' (eT (mu a b).1) = F (eS b) - F (eS a)

open HomometricSix in
/-- **THE REAL SPECTRAL CLASSIFICATION, derived.** Given the INTEGER premise: real spectra with
distinct gaps and equal gap sets are translation-congruent, reflection-congruent, or realize the
exceptional correspondence μ — the exact classification premise of
`twoBranch_of_spectral_classification`. The real pair is sorted, its forced gap correspondence
is extracted, the scope transfer produces an integer surrogate with the SAME correspondence, the
premise classifies the surrogate, and the integer pair's Golomb rigidity forces the
combinatorial identification of the correspondence with relabeled μ, which transports back to
the real spectra. -/
theorem spectral_classification_of_BG (hBG : BGIntegerClassification)
    {n : ℕ} (E E' : Fin n → ℝ)
    (hgapE : ∀ a b c d : Fin n, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hgapE' : ∀ a b c d : Fin n, a ≠ b → c ≠ d → E' b - E' a = E' d - E' c → a = c ∧ b = d)
    (hsets : Finset.image (fun q : Fin n × Fin n => E q.2 - E q.1) Finset.univ
      = Finset.image (fun q : Fin n × Fin n => E' q.2 - E' q.1) Finset.univ) :
    (∃ τ : Equiv.Perm (Fin n), ∃ E₀ : ℝ, ∀ a, E' (τ a) = E a + E₀)
    ∨ (∃ τ : Equiv.Perm (Fin n), ∃ E₀ : ℝ, ∀ a, E' (τ a) = -E a + E₀)
    ∨ (∃ eS eT : Fin 6 ≃ Fin n, ∀ a b : Fin 6, a < b →
        E' (eT (mu a b).2) - E' (eT (mu a b).1) = E (eS b) - E (eS a)) := by
  classical
  rcases Nat.eq_zero_or_pos n with hn0 | npos
  · subst hn0
    exact Or.inl ⟨1, 0, fun a => a.elim0⟩
  -- injectivity of both spectra
  have hEinj : Function.Injective E := by
    intro a b hab
    by_contra hne
    exact hne (hgapE a b b a hne (Ne.symm hne) (by rw [hab])).1
  have hE'inj : Function.Injective E' := by
    intro a b hab
    by_contra hne
    exact hne (hgapE' a b b a hne (Ne.symm hne) (by rw [hab])).1
  -- sort both spectra
  set σ : Equiv.Perm (Fin n) := Tuple.sort E with hσdef
  set σ' : Equiv.Perm (Fin n) := Tuple.sort E' with hσ'def
  have hmonoE : StrictMono (E ∘ σ) :=
    (Tuple.monotone_sort E).strictMono_of_injective (hEinj.comp σ.injective)
  have hmonoE' : StrictMono (E' ∘ σ') :=
    (Tuple.monotone_sort E').strictMono_of_injective (hE'inj.comp σ'.injective)
  -- the sorted signed distinct-gap hypotheses, and their ascending forms
  have hgapS : ∀ a b c d : Fin n, a ≠ b → c ≠ d →
      (E ∘ σ) b - (E ∘ σ) a = (E ∘ σ) d - (E ∘ σ) c → a = c ∧ b = d := by
    intro a b c d hab hcd h
    have := hgapE (σ a) (σ b) (σ c) (σ d)
      (fun h' => hab (σ.injective h')) (fun h' => hcd (σ.injective h')) h
    exact ⟨σ.injective this.1, σ.injective this.2⟩
  have hgapS' : ∀ a b c d : Fin n, a ≠ b → c ≠ d →
      (E' ∘ σ') b - (E' ∘ σ') a = (E' ∘ σ') d - (E' ∘ σ') c → a = c ∧ b = d := by
    intro a b c d hab hcd h
    have := hgapE' (σ' a) (σ' b) (σ' c) (σ' d)
      (fun h' => hab (σ'.injective h')) (fun h' => hcd (σ'.injective h')) h
    exact ⟨σ'.injective this.1, σ'.injective this.2⟩
  have hascS : ∀ a b c d : Fin n, a < b → c < d →
      (E ∘ σ) b - (E ∘ σ) a = (E ∘ σ) d - (E ∘ σ) c → a = c ∧ b = d :=
    fun a b c d hab hcd => hgapS a b c d (ne_of_lt hab) (ne_of_lt hcd)
  have hascS' : ∀ a b c d : Fin n, a < b → c < d →
      (E' ∘ σ') b - (E' ∘ σ') a = (E' ∘ σ') d - (E' ∘ σ') c → a = c ∧ b = d :=
    fun a b c d hab hcd => hgapS' a b c d (ne_of_lt hab) (ne_of_lt hcd)
  -- gap-set equality survives sorting
  have himg : ∀ (f : Fin n → ℝ) (τ : Equiv.Perm (Fin n)),
      Finset.image (fun q : Fin n × Fin n => f (τ q.2) - f (τ q.1)) Finset.univ
        = Finset.image (fun q : Fin n × Fin n => f q.2 - f q.1) Finset.univ := by
    intro f τ
    apply Finset.ext
    intro v
    simp only [Finset.mem_image, Finset.mem_univ, true_and]
    constructor
    · rintro ⟨q, rfl⟩
      exact ⟨(τ q.1, τ q.2), rfl⟩
    · rintro ⟨q, rfl⟩
      exact ⟨(τ.symm q.1, τ.symm q.2), by simp⟩
  -- the forced gap correspondence of the sorted pair
  have hforce : ∀ p : AscPair n, ∃ cd : Fin n × Fin n, cd.1 < cd.2
      ∧ (E' ∘ σ') cd.2 - (E' ∘ σ') cd.1 = (E ∘ σ) p.1.2 - (E ∘ σ) p.1.1 := by
    intro p
    have hv : (E ∘ σ) p.1.2 - (E ∘ σ) p.1.1
        ∈ Finset.image (fun q : Fin n × Fin n => (E' ∘ σ') q.2 - (E' ∘ σ') q.1)
            Finset.univ := by
      have h1 : (E ∘ σ) p.1.2 - (E ∘ σ) p.1.1
          ∈ Finset.image (fun q : Fin n × Fin n => E q.2 - E q.1) Finset.univ :=
        Finset.mem_image_of_mem _ (Finset.mem_univ (σ p.1.1, σ p.1.2))
      rw [hsets] at h1
      rw [show (fun q : Fin n × Fin n => (E' ∘ σ') q.2 - (E' ∘ σ') q.1)
        = fun q : Fin n × Fin n => E' (σ' q.2) - E' (σ' q.1) from rfl, himg E' σ']
      exact h1
    obtain ⟨q, _, hq⟩ := Finset.mem_image.mp hv
    have hvpos : 0 < (E ∘ σ) p.1.2 - (E ∘ σ) p.1.1 := sub_pos.mpr (hmonoE p.2)
    rcases lt_trichotomy q.1 q.2 with h | h | h
    · exact ⟨q, h, hq⟩
    · exfalso
      rw [h] at hq
      simp only [sub_self] at hq
      linarith [hq ▸ hvpos]
    · exfalso
      have := hmonoE' h
      linarith [hq]
  choose νf hν1 hν2 using hforce
  -- trichotomy: translate, reflect, or genuinely nontrivial
  by_cases htr : ∃ c : ℝ, ∀ i, (E' ∘ σ') i = (E ∘ σ) i + c
  · obtain ⟨c, hc⟩ := htr
    left
    refine ⟨σ.symm.trans σ', c, fun a => ?_⟩
    have h2 : E' (σ' (σ.symm a)) = E (σ (σ.symm a)) + c := hc (σ.symm a)
    rw [Equiv.apply_symm_apply] at h2
    exact h2
  by_cases hrf : ∃ c : ℝ, ∀ i, (E' ∘ σ') i = c - (E ∘ σ) i.rev
  · obtain ⟨c, hc⟩ := hrf
    right; left
    refine ⟨σ.symm.trans (Fin.revPerm.trans σ'), c, fun a => ?_⟩
    have h2 : E' (σ' ((σ.symm a).rev)) = c - E (σ ((σ.symm a).rev.rev)) := hc ((σ.symm a).rev)
    rw [Fin.rev_rev, Equiv.apply_symm_apply] at h2
    rw [show (σ.symm.trans (Fin.revPerm.trans σ')) a = σ' ((σ.symm a).rev) from rfl, h2]
    ring
  -- nontriviality witnesses
  push Not at htr hrf
  obtain ⟨i₀, hi₀⟩ := htr ((E' ∘ σ') ⟨0, npos⟩ - (E ∘ σ) ⟨0, npos⟩)
  obtain ⟨i₁, hi₁⟩ := hrf ((E' ∘ σ') ⟨0, npos⟩ + (E ∘ σ) (⟨0, npos⟩ : Fin n).rev)
  have hnt : (E' ∘ σ') i₀ - (E ∘ σ) i₀
      ≠ (E' ∘ σ') ⟨0, npos⟩ - (E ∘ σ) ⟨0, npos⟩ := fun h => hi₀ (by linarith)
  have hnr : (E' ∘ σ') i₁ + (E ∘ σ) i₁.rev
      ≠ (E' ∘ σ') ⟨0, npos⟩ + (E ∘ σ) (⟨0, npos⟩ : Fin n).rev := fun h => hi₁ (by linarith)
  -- the scope transfer
  obtain ⟨F, F', hFm, hF'm, hFg, hF'g, hFν, hFnt, hFnr⟩ :=
    integer_realization_of_real_realization νf (E ∘ σ) (E' ∘ σ')
      hmonoE hmonoE' hascS hascS' hν2 hnt hnr
  -- the premise inputs for the integer surrogate
  have hinjF : Function.Injective (fun p : AscPair n => F p.1.2 - F p.1.1) := by
    intro p p' h
    have := hFg p.1.1 p.1.2 p'.1.1 p'.1.2 p.2 p'.2 h
    exact Subtype.ext (Prod.ext this.1 this.2)
  have hinjF' : Function.Injective (fun p : AscPair n => F' p.1.2 - F' p.1.1) := by
    intro p p' h
    have := hF'g p.1.1 p.1.2 p'.1.1 p'.1.2 p.2 p'.2 h
    exact Subtype.ext (Prod.ext this.1 this.2)
  have hFsets : Finset.image (fun p : AscPair n => F p.1.2 - F p.1.1) Finset.univ
      = Finset.image (fun p : AscPair n => F' p.1.2 - F' p.1.1) Finset.univ := by
    apply Finset.eq_of_subset_of_card_le
    · intro v hv
      obtain ⟨p, _, rfl⟩ := Finset.mem_image.mp hv
      exact Finset.mem_image.mpr ⟨⟨νf p, hν1 p⟩, Finset.mem_univ _, hFν p⟩
    · rw [Finset.card_image_of_injective _ hinjF', Finset.card_image_of_injective _ hinjF]
  have hFnottr : ¬ ∃ c : ℤ, ∀ i, F' i = F i + c := by
    rintro ⟨c, hc⟩
    exact hFnt (by rw [hc i₀, hc ⟨0, npos⟩]; ring)
  have hFnorf : ¬ ∃ c : ℤ, ∀ i, F' i = c - F i.rev := by
    rintro ⟨c, hc⟩
    exact hFnr (by rw [hc i₁, hc ⟨0, npos⟩]; ring)
  obtain ⟨eS, eT, hint⟩ := hBG n F F' hFm hF'm hFg hF'g hFsets hFnottr hFnorf
  -- transport the exceptional match back to the real spectra
  right; right
  have key : ∀ a b : Fin 6, a < b →
      (E' ∘ σ') (eT (mu a b).2) - (E' ∘ σ') (eT (mu a b).1)
        = (E ∘ σ) (eS b) - (E ∘ σ) (eS a) := by
    intro a b hab
    have hint' := hint a b hab
    rcases lt_trichotomy (eS a) (eS b) with h | h | h
    · have hFp : F' (νf ⟨(eS a, eS b), h⟩).2 - F' (νf ⟨(eS a, eS b), h⟩).1
          = F (eS b) - F (eS a) := hFν ⟨(eS a, eS b), h⟩
      have hupos : (0 : ℤ) < F (eS b) - F (eS a) := sub_pos.mpr (hFm h)
      have ho : eT (mu a b).1 < eT (mu a b).2 := by
        rcases lt_trichotomy (eT (mu a b).1) (eT (mu a b).2) with h' | h' | h'
        · exact h'
        · exfalso
          rw [h'] at hint'
          simp only [sub_self] at hint'
          omega
        · exfalso
          have := hF'm h'
          omega
      have hpair := hF'g (eT (mu a b).1) (eT (mu a b).2)
        (νf ⟨(eS a, eS b), h⟩).1 (νf ⟨(eS a, eS b), h⟩).2 ho (hν1 ⟨(eS a, eS b), h⟩)
        (by rw [hint', hFp])
      have hEp : (E' ∘ σ') (νf ⟨(eS a, eS b), h⟩).2 - (E' ∘ σ') (νf ⟨(eS a, eS b), h⟩).1
          = (E ∘ σ) (eS b) - (E ∘ σ) (eS a) := hν2 ⟨(eS a, eS b), h⟩
      rw [hpair.1, hpair.2]
      exact hEp
    · exact absurd (eS.injective h) (ne_of_lt hab)
    · have hFp : F' (νf ⟨(eS b, eS a), h⟩).2 - F' (νf ⟨(eS b, eS a), h⟩).1
          = F (eS a) - F (eS b) := hFν ⟨(eS b, eS a), h⟩
      have huneg : F (eS b) - F (eS a) < 0 := sub_neg.mpr (hFm h)
      have ho : eT (mu a b).2 < eT (mu a b).1 := by
        rcases lt_trichotomy (eT (mu a b).2) (eT (mu a b).1) with h' | h' | h'
        · exact h'
        · exfalso
          rw [h'] at hint'
          simp only [sub_self] at hint'
          omega
        · exfalso
          have := hF'm h'
          omega
      have hpair := hF'g (eT (mu a b).2) (eT (mu a b).1)
        (νf ⟨(eS b, eS a), h⟩).1 (νf ⟨(eS b, eS a), h⟩).2 ho (hν1 ⟨(eS b, eS a), h⟩)
        (by omega)
      have hEp : (E' ∘ σ') (νf ⟨(eS b, eS a), h⟩).2 - (E' ∘ σ') (νf ⟨(eS b, eS a), h⟩).1
          = (E ∘ σ) (eS a) - (E ∘ σ) (eS b) := hν2 ⟨(eS b, eS a), h⟩
      rw [hpair.1, hpair.2]
      linarith [hEp]
  exact ⟨eS.trans σ, eT.trans σ', fun a b hab => key a b hab⟩

/-! ### From equal probabilities to equal gap sets, and the final assembly -/

open Complex BohrFrequency in
/-- Equal transition probabilities force equal gap SETS, with nonzero overlaps: the diagonal
frequency amplitude over a nonempty fiber is a sum of positive reals, so a frequency lives in
one gap set iff its shared amplitude is nonzero iff it lives in the other. -/
lemma gaps_eq_of_equal_probabilities {m : ℕ} (hm : 0 < m)
    (V W : Matrix (Fin m) (Fin m) ℂ) (E E' : Fin m → ℝ)
    (hVnz : ∀ i a, V i a ≠ 0) (hWnz : ∀ i a, W i a ≠ 0)
    (hU : ∀ i j : Fin m, ∀ t : ℝ, Umat V E t i j * star (Umat V E t i j)
      = Umat W E' t i j * star (Umat W E' t i j)) :
    Finset.image (fun q : Fin m × Fin m => E q.2 - E q.1) Finset.univ
      = Finset.image (fun q : Fin m × Fin m => E' q.2 - E' q.1) Finset.univ := by
  classical
  have i0 : Fin m := ⟨0, hm⟩
  have hdiag : ∀ (Vv : Fin m → Fin m → ℂ) (Ee : Fin m → ℝ) (ω : ℝ),
      (∀ a, Vv i0 a ≠ 0) →
      (Finset.univ.filter (fun q : Fin m × Fin m => Ee q.2 - Ee q.1 = ω)).Nonempty →
      ampC Vv Ee i0 i0 ω ≠ 0 := by
    intro Vv Ee ω hnz hfib
    rw [ampC]
    have hterm : ∀ q ∈ Finset.univ.filter (fun q : Fin m × Fin m => Ee q.2 - Ee q.1 = ω),
        Vv i0 q.1 * star (Vv i0 q.1) * star (Vv i0 q.2) * Vv i0 q.2
          = ((normSq (Vv i0 q.1) * normSq (Vv i0 q.2) : ℝ) : ℂ) := by
      intro q _
      rw [show Vv i0 q.1 * star (Vv i0 q.1) * star (Vv i0 q.2) * Vv i0 q.2
        = (Vv i0 q.1 * star (Vv i0 q.1)) * (Vv i0 q.2 * star (Vv i0 q.2)) by ring]
      simp only [Complex.star_def]
      rw [Complex.mul_conj, Complex.mul_conj]
      push_cast
      ring
    rw [Finset.sum_congr rfl hterm]
    have hpos : (0 : ℝ)
        < ∑ q ∈ Finset.univ.filter (fun q : Fin m × Fin m => Ee q.2 - Ee q.1 = ω),
          normSq (Vv i0 q.1) * normSq (Vv i0 q.2) :=
      Finset.sum_pos
        (fun q _ => mul_pos (normSq_pos.mpr (hnz q.1)) (normSq_pos.mpr (hnz q.2))) hfib
    intro h0
    apply ne_of_gt hpos
    exact_mod_cast h0
  have hamp := coefficients_by_frequency_determined V W E E' hU i0 i0
  apply Finset.ext
  intro ω
  simp only [Finset.mem_image, Finset.mem_univ, true_and]
  constructor
  · rintro ⟨q, rfl⟩
    have h1 : ampC V E i0 i0 (E q.2 - E q.1) ≠ 0 :=
      hdiag V E _ (fun a => hVnz i0 a) ⟨q, Finset.mem_filter.mpr ⟨Finset.mem_univ q, rfl⟩⟩
    rw [hamp (E q.2 - E q.1)] at h1
    by_contra hnot
    push Not at hnot
    refine h1 (ampC_eq_zero W i0 i0 fun hmem => ?_)
    obtain ⟨q', _, hq'⟩ := Finset.mem_image.mp hmem
    exact hnot q' hq' 
  · rintro ⟨q, rfl⟩
    have h1 : ampC W E' i0 i0 (E' q.2 - E' q.1) ≠ 0 :=
      hdiag W E' _ (fun a => hWnz i0 a) ⟨q, Finset.mem_filter.mpr ⟨Finset.mem_univ q, rfl⟩⟩
    rw [← hamp (E' q.2 - E' q.1)] at h1
    by_contra hnot
    push Not at hnot
    refine h1 (ampC_eq_zero V i0 i0 fun hmem => ?_)
    obtain ⟨q', _, hq'⟩ := Finset.mem_image.mp hmem
    exact hnot q' hq' 

local notation "conj'" => (starRingEnd ℂ)

open Matrix HomometricSix BohrFrequency CongruentReconstruction in
/-- **THE TWO-BRANCH THEOREM, CONDITIONAL ON THE INTEGER CLASSIFICATION ALONE.** Equal
transition probabilities for all times, distinct gaps on both sides, and the INTEGER
Bekir–Golomb classification give the two Hamiltonian branches over arbitrary REAL spectra:
`gaps_eq_of_equal_probabilities` supplies equal gap sets, `spectral_classification_of_BG`
transfers the classification from ℤ to ℝ, and `twoBranch_of_spectral_classification` finishes.
Every step other than `BGIntegerClassification` is kernel-proved. -/
theorem twoBranch_of_BGClassification (hBG : BGIntegerClassification) {m : ℕ} (hm : 3 ≤ m)
    (V W : Matrix (Fin m) (Fin m) ℂ) (E E' : Fin m → ℝ)
    (hV : V * Vᴴ = 1) (hW : W * Wᴴ = 1)
    (hVnz : ∀ i a, V i a ≠ 0) (hWnz : ∀ i c, W i c ≠ 0)
    (hgapV : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hgapW : ∀ a b c d : Fin m, a ≠ b → c ≠ d → E' b - E' a = E' d - E' c → a = c ∧ b = d)
    (hU : ∀ i j : Fin m, ∀ t : ℝ, Umat V E t i j * star (Umat V E t i j)
      = Umat W E' t i j * star (Umat W E' t i j)) :
    (∃ E₀ : ℝ, ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = Matrix.diagonal d * (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ + (E₀ : ℂ) • 1)
    ∨ (∃ E₀ : ℝ, ∃ d : Fin m → ℂ, (∀ i, d i * conj' (d i) = 1) ∧
      W * Matrix.diagonal (fun c => (E' c : ℂ)) * Wᴴ
        = -(Matrix.diagonal d * conjM (V * Matrix.diagonal (fun a => (E a : ℂ)) * Vᴴ)
            * (Matrix.diagonal d)ᴴ) + (E₀ : ℂ) • 1) :=
  CongruentReconstruction.twoBranch_of_spectral_classification hm V W E E'
    hV hW hVnz hWnz hgapV hgapW hU
    (spectral_classification_of_BG hBG E E' hgapV hgapW
      (gaps_eq_of_equal_probabilities (by omega) V W E E' hVnz hWnz hU))

#print axioms rational_point
#print axioms rational_solutions
#print axioms exists_int_scaling
#print axioms integer_realization_of_real_realization
#print axioms spectral_classification_of_BG
#print axioms gaps_eq_of_equal_probabilities
#print axioms twoBranch_of_BGClassification

end ScopeTransfer
end OIBridge
