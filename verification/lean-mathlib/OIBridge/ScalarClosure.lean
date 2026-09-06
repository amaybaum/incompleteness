import OIBridge.SubstratumInterfaceAudit

/-!
# The scalar-closure audit — the regression theorem for contractive scalars

The preregistered pass of `SCALAR-CLOSURE-AUDIT.md`. `Architecture.smul` is stated for scalars
of modulus at most one. This file records what that restriction leaves unchanged:

* the availability of every generated theory is `IsGenInstrument` by definition
  (`genTheory_availExt_eq`), so no scalar closure enters it;
* for a class closed under contractive scalars, realization by its scalar hull is realization
  by the class (`realized_scalarHull_iff`): a conjugation by `a • K` with `|a| > 1` is
  `⌊|a|²⌋` conjugations by `K` and one by a contractive multiple of `K`;
* the scalar hull of the migrated sourced class is the class of the first outcome head, the
  uniformly scaled partial permutations with any scalar (`scalarHull_permClass_iff`), and the
  two classes generate the same availability at every level (`permTheory_hull_availExt_iff`).
-/

namespace OIBridge
namespace ScalarClosure

open Complex Matrix CoherentLift SpectatorBridge OperationalAssembly AncillaClosure
open MonoidalCompletion InterventionLocality MicroReversibility LieRankSource
open StructuralClosure SubstratumInterfaceAudit

/-! ### Section A — the generated theory does not consume the scalar closure -/

section Generated

variable {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
variable {A : Type} [Fintype A] [DecidableEq A]

/-- **T1 — THE AVAILABILITY OF A GENERATED THEORY IS THE GENERATED-INSTRUMENT PREDICATE**, by
definition; no scalar closure enters it. -/
theorem genTheory_availExt_eq (n : ℕ) {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ) :
    (genTheory 𝓘 arch A).availExt n O F ↔ IsGenInstrument 𝓘 (A × Fin n) F :=
  Iff.rfl

end Generated

/-! ### Section B — the scalar hull and the regression theorem -/

section Hull

/-- **THE SCALAR HULL** of a class: every scalar multiple of an admissible operator. -/
def scalarHull (𝓘 : ImplementationClass) : ImplementationClass :=
  fun S _ _ K => ∃ (a : ℂ) (K' : Matrix S S ℂ), 𝓘 S K' ∧ K = a • K'

variable {𝓘 : ImplementationClass} {S : Type} [Fintype S] [DecidableEq S]

theorem mem_scalarHull_self {K : Matrix S S ℂ} (h : 𝓘 S K) : scalarHull 𝓘 S K :=
  ⟨1, K, h, (one_smul _ _).symm⟩

theorem realized_mono {𝓙 : ImplementationClass}
    (hle : ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), 𝓘 S K → 𝓙 S K)
    {Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : Realized 𝓘 S Φ) : Realized 𝓙 S Φ := by
  obtain ⟨ι, _, K, rfl, hK⟩ := h
  exact ⟨ι, inferInstance, K, rfl, fun i => hle _ _ (hK i)⟩

/-- A natural multiple of a realized operation is realized: the sum of that many copies. -/
theorem realized_nsmul {Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (N : ℕ) (h : Realized 𝓘 S Φ) :
    Realized 𝓘 S ((N : ℂ) • Φ) := by
  have : (N : ℂ) • Φ = ∑ _i : Fin N, Φ := by
    rw [Finset.sum_const, Finset.card_univ, Fintype.card_fin, ← Nat.cast_smul_eq_nsmul ℂ]
  rw [this]
  exact realized_sum _ _ fun _ _ => h

/-- **A NONNEGATIVE REAL MULTIPLE OF A REALIZED OPERATION IS REALIZED**, for a class closed
under contractive scalars: the integer part as that many copies, the fractional part by
attenuation. -/
theorem realized_real_smul
    (hsmul : ∀ (a : ℂ) (K : Matrix S S ℂ), ‖a‖ ≤ 1 → 𝓘 S K → 𝓘 S (a • K))
    {Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (r : ℝ) (hr : 0 ≤ r) (h : Realized 𝓘 S Φ) :
    Realized 𝓘 S ((r : ℂ) • Φ) := by
  have hsplit : (r : ℂ) • Φ = ((⌊r⌋₊ : ℕ) : ℂ) • Φ + (((r - ⌊r⌋₊ : ℝ)) : ℂ) • Φ := by
    rw [← add_smul]
    congr 1
    push_cast
    ring
  rw [hsplit]
  refine realized_add (realized_nsmul _ h) (realized_smul_nonneg hsmul _ ?_ ?_ h)
  · exact sub_nonneg.mpr (Nat.floor_le hr)
  · have := Nat.lt_floor_add_one r
    linarith

/-- **T3 — REALIZATION BY THE SCALAR HULL IS REALIZATION BY THE CLASS**, for a class closed
under contractive scalars. A conjugation by `a • K` is `|a|²` times the conjugation by `K`. -/
theorem realized_scalarHull_iff
    (hsmul : ∀ (a : ℂ) (K : Matrix S S ℂ), ‖a‖ ≤ 1 → 𝓘 S K → 𝓘 S (a • K))
    (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) :
    Realized (scalarHull 𝓘) S Φ ↔ Realized 𝓘 S Φ := by
  constructor
  · rintro ⟨ι, _, K, rfl, hK⟩
    refine realized_sum _ _ fun i _ => ?_
    obtain ⟨a, K', hK', hKi⟩ := hK i
    rw [hKi, conjChannel_smul, Complex.star_def, Complex.mul_conj]
    exact realized_real_smul hsmul _ (Complex.normSq_nonneg a) (realized_conj hK')
  · exact realized_mono fun _ _ _ _ h => mem_scalarHull_self h

end Hull

/-! ### Section C — the hull of the sourced class, and the same theory -/

section Perm

variable {S : Type} [Fintype S] [DecidableEq S]

omit [Fintype S] [DecidableEq S] in
theorem ancBlock_smul {m : ℕ} (a : ℂ) (K : Matrix (S × Fin m) (S × Fin m) ℂ) (f e : Fin m) :
    ancBlock (a • K) f e = a • ancBlock K f e := by
  ext s t
  simp [ancBlock]

/-- **THE SCALAR HULL OF AN ARCHITECTURE IS AN ARCHITECTURE.** -/
theorem scalarHull_arch {𝓘 : ImplementationClass} (arch : Architecture 𝓘) :
    Architecture (scalarHull 𝓘) where
  one := fun S _ _ => mem_scalarHull_self (arch.one S)
  mul := fun S _ _ K L hK hL => by
    obtain ⟨a, K', hK', rfl⟩ := hK
    obtain ⟨b, L', hL', rfl⟩ := hL
    exact ⟨a * b, K' * L', arch.mul S _ _ hK' hL', by rw [Matrix.smul_mul, Matrix.mul_smul, smul_smul]⟩
  smul := fun S _ _ c K _ hK => by
    obtain ⟨a, K', hK', rfl⟩ := hK
    exact ⟨c * a, K', hK', by rw [smul_smul]⟩
  proj := fun S _ _ m k => mem_scalarHull_self (arch.proj S m k)
  block := fun S _ _ m K f e hK => by
    obtain ⟨a, K', hK', rfl⟩ := hK
    exact ⟨a, ancBlock K' f e, arch.block S m K' f e hK', ancBlock_smul a K' f e⟩

/-- **THE UNIFORMLY SCALED PARTIAL PERMUTATIONS WITH ANY SCALAR**: the class of the first
outcome head of the substratum-interface audit, before the contractive migration. -/
def IsUniformSubmonomial (K : Matrix S S ℂ) : Prop :=
  IsSubmonomial K ∧ ∃ c : ℂ, ∀ i j, K i j ≠ 0 → K i j = c

/-- **THE HULL OF THE SOURCED CLASS IS THE UNRESTRICTED CLASS.** -/
theorem scalarHull_permClass_iff (K : Matrix S S ℂ) :
    scalarHull permClass S K ↔ IsUniformSubmonomial K := by
  constructor
  · rintro ⟨a, K', ⟨hK1, c, -, hc⟩, rfl⟩
    refine ⟨submonomial_smul a hK1, a * c, fun i j h => ?_⟩
    rw [Matrix.smul_apply, smul_eq_mul] at h ⊢
    rw [hc _ _ (mul_ne_zero_iff.mp h).2]
  · rintro ⟨hK1, c, hc⟩
    by_cases hc0 : c = 0
    · refine ⟨0, 1, scaled_one_aux, ?_⟩
      ext i j
      rw [Matrix.smul_apply, zero_smul]
      by_contra hne
      have := hc i j hne
      rw [hc0] at this
      exact hne this
    · refine ⟨c, c⁻¹ • K, ⟨submonomial_smul _ hK1, 1, norm_one.le, fun i j h => ?_⟩, ?_⟩
      · rw [Matrix.smul_apply, smul_eq_mul] at h ⊢
        rw [hc _ _ (mul_ne_zero_iff.mp h).2, inv_mul_cancel₀ hc0]
      · rw [smul_smul, mul_inv_cancel₀ hc0, one_smul]

variable {A : Type} [Fintype A] [DecidableEq A]

/-- **T3 — THE UNRESTRICTED AND THE MIGRATED SOURCED CLASSES GENERATE THE SAME AVAILABILITY** at
every level: the regression theorem for the substratum-interface audit. -/
theorem permTheory_hull_availExt_iff (n : ℕ) {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ) :
    (genTheory (scalarHull permClass) (scalarHull_arch permClass_arch) A).availExt n O F
      ↔ (permTheory A).availExt n O F := by
  rw [genTheory_availExt_eq, genTheory_availExt_eq]
  unfold IsGenInstrument
  refine and_congr (forall_congr' fun a => ?_) Iff.rfl
  exact realized_scalarHull_iff (fun a K ha hK => permClass_arch.smul _ a K ha hK) (F a)

end Perm

#print axioms genTheory_availExt_eq
#print axioms mem_scalarHull_self
#print axioms realized_mono
#print axioms realized_nsmul
#print axioms realized_real_smul
#print axioms realized_scalarHull_iff
#print axioms ancBlock_smul
#print axioms scalarHull_arch
#print axioms scalarHull_permClass_iff
#print axioms permTheory_hull_availExt_iff

end ScalarClosure
end OIBridge
