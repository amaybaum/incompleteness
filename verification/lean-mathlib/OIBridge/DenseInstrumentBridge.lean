import OIBridge.DiscreteCompletion

/-!
# The quantitative dense-instrument bridge audit — from dense unitary control to dense instruments

The preregistered pass of `DENSE-INSTRUMENT-BRIDGE-AUDIT.md`, read under its scope amendment. The
branch map of the Stinespring circuit is Lipschitz in the unitary with a constant depending only on
the carrier; the shifted theory is rebuilt from identity availability beside the untouched `shift`;
every exact consumption of the circuit is discharged from the closure; and the approximate
Stinespring assembly gives `KrausDense` from `DerivedOI` and `DenseUnitaryControl`. Nothing here is
named "C5"; no continuous pair flow enters any constructive route; dense availability is never
identified with exact availability; no completion statement is made.
-/

namespace OIBridge
namespace DenseInstrumentBridge

open Complex Matrix CoherentLift SpectatorBridge OperationalAssembly AncillaClosure
open StinespringAssembly IsometryExtension ReferenceExtension InterventionLocality
open RouteB KrausSoundness CompositeSoundness StateMixingCoupling DiscreteCompletion
open MonoidalCompletion ReferenceSufficiency
open scoped Matrix.Norms.L2Operator

/-! ### Section A — T2: the calculus of the channel metric -/

section Metric

variable {S : Type} [Fintype S] [DecidableEq S]

/-- The metric predicate is monotone in the tolerance. -/
theorem chanWithin_mono {ε ε' : ℝ} (h : ε ≤ ε') {Φ Ψ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ}
    (hΦ : ChanWithin ε Φ Ψ) : ChanWithin ε' Φ Ψ := fun X =>
  (hΦ X).trans (mul_le_mul_of_nonneg_right h (norm_nonneg _))

/-- **FINITE SUMS ADD THE TOLERANCES**: a sum of `card s` branches each within `ε` is within
`card s · ε`. -/
theorem chanWithin_sum {ι : Type*} (s : Finset ι) {ε : ℝ}
    {F G : ι → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : ∀ i ∈ s, ChanWithin ε (F i) (G i)) :
    ChanWithin (s.card * ε) (∑ i ∈ s, F i) (∑ i ∈ s, G i) := by
  intro X
  rw [LinearMap.sum_apply, LinearMap.sum_apply, ← Finset.sum_sub_distrib]
  calc ‖∑ i ∈ s, (F i X - G i X)‖ ≤ ∑ i ∈ s, ‖F i X - G i X‖ := norm_sum_le _ _
    _ ≤ ∑ i ∈ s, ε * ‖X‖ := Finset.sum_le_sum fun i hi => h i hi X
    _ = s.card * ε * ‖X‖ := by rw [Finset.sum_const, nsmul_eq_mul]; ring

/-- A unit scalar multiple of a unitary is unitary. -/
theorem unitary_unit_smul {c : ℂ} (hc : ‖c‖ = 1) {V : Matrix S S ℂ} (hV : Vᴴ * V = 1) :
    (c • V)ᴴ * (c • V) = 1 := by
  have h1 : star c * c = 1 := by
    rw [mul_comm, Complex.star_def, Complex.mul_conj, Complex.normSq_eq_norm_sq, hc]
    simp
  rw [Matrix.conjTranspose_smul, Matrix.smul_mul, Matrix.mul_smul, smul_smul, h1, one_smul, hV]

end Metric

/-! ### Section B — T1: the norm bounds of the circuit pieces -/

section Norms

variable {S : Type} [Fintype S] [DecidableEq S]

/-- **AN ISOMETRY HAS OPERATOR NORM ONE**, by the C*-identity `‖Eᴴ E‖ = ‖E‖²`. -/
theorem norm_eq_one_of_isometry [Nonempty S] {l : Type} [Fintype l] [DecidableEq l]
    {E : Matrix l S ℂ} (hE : Eᴴ * E = 1) : ‖E‖ = 1 := by
  have h := Matrix.l2_opNorm_conjTranspose_mul_self E
  rw [hE, norm_eq_one_of_unitary (U := (1 : Matrix S S ℂ)) (by simp)] at h
  rcases mul_self_eq_one_iff.mp h.symm with h1 | h1
  · exact h1
  · linarith [norm_nonneg E]

/-- **CONJUGATION BY AN ISOMETRY DOES NOT INCREASE THE NORM.** -/
theorem norm_isometry_conj_le [Nonempty S] {l : Type} [Fintype l] [DecidableEq l]
    {E : Matrix l S ℂ} (hE : Eᴴ * E = 1) (X : Matrix S S ℂ) : ‖E * X * Eᴴ‖ ≤ ‖X‖ := by
  have h1 : ‖E‖ = 1 := norm_eq_one_of_isometry hE
  have h2 : ‖Eᴴ‖ = 1 := by rw [Matrix.l2_opNorm_conjTranspose]; exact h1
  calc ‖E * X * Eᴴ‖ ≤ ‖E * X‖ * ‖Eᴴ‖ := Matrix.l2_opNorm_mul _ _
    _ ≤ ‖E‖ * ‖X‖ * ‖Eᴴ‖ := by gcongr; exact Matrix.l2_opNorm_mul _ _
    _ = ‖X‖ := by rw [h1, h2, one_mul, mul_one]

/-- **COMPRESSION BY AN ISOMETRY DOES NOT INCREASE THE NORM.** -/
theorem norm_isometry_compress_le [Nonempty S] {l : Type} [Fintype l] [DecidableEq l]
    {E : Matrix l S ℂ} (hE : Eᴴ * E = 1) (M : Matrix l l ℂ) : ‖Eᴴ * M * E‖ ≤ ‖M‖ := by
  have h1 : ‖E‖ = 1 := norm_eq_one_of_isometry hE
  have h2 : ‖Eᴴ‖ = 1 := by rw [Matrix.l2_opNorm_conjTranspose]; exact h1
  calc ‖Eᴴ * M * E‖ ≤ ‖Eᴴ * M‖ * ‖E‖ := Matrix.l2_opNorm_mul _ _
    _ ≤ ‖Eᴴ‖ * ‖M‖ * ‖E‖ := by gcongr; exact Matrix.l2_opNorm_mul _ _
    _ = ‖M‖ := by rw [h1, h2, one_mul, mul_one]

end Norms

section Circuit

variable {A : Type} [Fintype A] [DecidableEq A]

/-- The seed embedding is an isometry. -/
theorem esf_gram {n : ℕ} (k₀ : Fin n) : (Esf (A := A) k₀)ᴴ * Esf (A := A) k₀ = 1 := by
  ext s t
  have h1 : ∀ q : A × Fin n, Esf (A := A) k₀ q t = if q = (t, k₀) then 1 else 0 := by
    intro q
    simp only [Esf, Matrix.of_apply, Prod.ext_iff]
    by_cases h2 : q.2 = k₀ <;> by_cases h1 : q.1 = t <;> simp [h1, h2]
  have h2 : ∀ p : A × Fin n, (Esf (A := A) k₀)ᴴ s p = if p = (s, k₀) then 1 else 0 := by
    intro p
    simp only [Matrix.conjTranspose_apply, Esf, Matrix.of_apply, Prod.ext_iff]
    by_cases h2 : p.2 = k₀ <;> by_cases h1 : p.1 = s <;> simp [h1, h2]
  simp only [Matrix.mul_apply, h1, h2, mul_ite, mul_one, mul_zero, Finset.sum_ite_eq',
    Finset.mem_univ, if_true, Matrix.one_apply, Prod.mk.injEq, and_true]
  by_cases hst : s = t
  · subst hst; simp
  · simp [hst, Ne.symm hst]

/-- **THE PARTIAL TRACE IS A SUM OF ISOMETRIC COMPRESSIONS** over the ancilla basis. -/
theorem ptraceAnc_eq_sum (n : ℕ) (M : Matrix (A × Fin n) (A × Fin n) ℂ) :
    ptraceAnc n M = ∑ e : Fin n, (Esf (A := A) e)ᴴ * M * Esf (A := A) e := by
  ext s t
  rw [ptraceAnc_apply, Matrix.sum_apply]
  refine Finset.sum_congr rfl fun e _ => ?_
  have h1 : ∀ q : A × Fin n, Esf (A := A) e q t = if q = (t, e) then 1 else 0 := by
    intro q
    simp only [Esf, Matrix.of_apply, Prod.ext_iff]
    by_cases h2 : q.2 = e <;> by_cases h1 : q.1 = t <;> simp [h1, h2]
  have h2 : ∀ p : A × Fin n, (Esf (A := A) e)ᴴ s p = if p = (s, e) then 1 else 0 := by
    intro p
    simp only [Matrix.conjTranspose_apply, Esf, Matrix.of_apply, Prod.ext_iff]
    by_cases h2 : p.2 = e <;> by_cases h1 : p.1 = s <;> simp [h1, h2]
  simp only [Matrix.mul_apply, h1, h2, mul_ite, mul_one, mul_zero, ite_mul, one_mul, zero_mul,
    Finset.sum_ite_eq', Finset.mem_univ, if_true]

/-- **THE PARTIAL TRACE IS BOUNDED BY THE ANCILLA DIMENSION** in the operator norm. -/
theorem norm_ptraceAnc_le [Nonempty A] (n : ℕ) (M : Matrix (A × Fin n) (A × Fin n) ℂ) :
    ‖ptraceAnc n M‖ ≤ n * ‖M‖ := by
  rw [ptraceAnc_eq_sum]
  calc ‖∑ e : Fin n, (Esf (A := A) e)ᴴ * M * Esf (A := A) e‖
      ≤ ∑ e : Fin n, ‖(Esf (A := A) e)ᴴ * M * Esf (A := A) e‖ := norm_sum_le _ _
    _ ≤ ∑ _e : Fin n, ‖M‖ := Finset.sum_le_sum fun e _ => norm_isometry_compress_le (esf_gram e) M
    _ = n * ‖M‖ := by rw [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]

/-- **THE LOCAL LÜDERS SELECTOR IS A CONTRACTION**: it is conjugation by a projector of norm at
most one. -/
theorem norm_localLuders_le {m : ℕ} (k : Fin m) (X : Matrix (A × Fin m) (A × Fin m) ℂ) :
    ‖localLuders k X‖ ≤ ‖X‖ := by
  rw [localLuders_eq_conjChannel]
  set D : Matrix (A × Fin m) (A × Fin m) ℂ :=
    Matrix.diagonal fun r : A × Fin m => if r.2 = k then (1 : ℂ) else 0 with hDdef
  have hD : ‖D‖ ≤ 1 := by
    rw [hDdef, Matrix.l2_opNorm_diagonal]
    refine (pi_norm_le_iff_of_nonneg zero_le_one).mpr fun r => ?_
    split_ifs <;> simp
  have hDH : ‖Dᴴ‖ ≤ 1 := by rw [Matrix.l2_opNorm_conjTranspose]; exact hD
  show ‖D * X * Dᴴ‖ ≤ ‖X‖
  calc ‖D * X * Dᴴ‖ ≤ ‖D * X‖ * ‖Dᴴ‖ := norm_mul_le _ _
    _ ≤ ‖D‖ * ‖X‖ * ‖Dᴴ‖ := by gcongr; exact norm_mul_le _ _
    _ ≤ 1 * ‖X‖ * 1 := by gcongr
    _ = ‖X‖ := by ring

/-- **THE PURE ATTACHMENT IS ISOMETRIC**: it is conjugation by the seed embedding. -/
theorem norm_pureAttach_le [Nonempty A] {n : ℕ} (k₀ : Fin n) (ρ : Matrix A A ℂ) :
    ‖pureAttach n k₀ ρ‖ ≤ ‖ρ‖ := by
  rw [← esf_conj]
  exact norm_isometry_conj_le (esf_gram k₀) ρ

/-- **THE BRANCH MAP IS LIPSCHITZ IN THE UNITARY**, with the constant `2 (r + 1)` depending only
on the carrier: preparation isometric, conjugation at constant two, readout a contraction, discard
bounded by the ancilla dimension. -/
theorem branch_within [Nonempty A] {r : ℕ} (k₀ k : Fin (r + 1))
    {U V : Matrix (A × Fin (r + 1)) (A × Fin (r + 1)) ℂ} (hU : Uᴴ * U = 1) (hV : Vᴴ * V = 1)
    {δ : ℝ} (h : ‖U - V‖ ≤ δ) :
    ChanWithin (2 * ((r : ℝ) + 1) * δ)
      (discardMap (r + 1) k₀ ((localLuders k).comp (conjChannel U)))
      (discardMap (r + 1) k₀ ((localLuders k).comp (conjChannel V))) := by
  have : Nonempty (A × Fin (r + 1)) := ⟨(Classical.arbitrary A, 0)⟩
  intro X
  have hδ : 0 ≤ δ := (norm_nonneg _).trans h
  set P := pureAttach (r + 1) k₀ X with hP
  have hPn : ‖P‖ ≤ ‖X‖ := norm_pureAttach_le k₀ X
  have hc : ‖conjChannel U P - conjChannel V P‖ ≤ 2 * δ * ‖P‖ := conj_within hU hV h P
  show ‖ptraceAncL (r + 1) (localLuders k (conjChannel U P))
      - ptraceAncL (r + 1) (localLuders k (conjChannel V P))‖ ≤ _
  rw [← map_sub, ← map_sub]
  calc ‖ptraceAncL (r + 1) (localLuders k (conjChannel U P - conjChannel V P))‖
      ≤ ((r + 1 : ℕ) : ℝ) * ‖localLuders k (conjChannel U P - conjChannel V P)‖ :=
        norm_ptraceAnc_le (r + 1) _
    _ ≤ ((r + 1 : ℕ) : ℝ) * ‖conjChannel U P - conjChannel V P‖ := by
        gcongr; exact norm_localLuders_le k _
    _ ≤ ((r + 1 : ℕ) : ℝ) * (2 * δ * ‖P‖) := by gcongr
    _ ≤ ((r + 1 : ℕ) : ℝ) * (2 * δ * ‖X‖) := by gcongr
    _ = 2 * ((r : ℝ) + 1) * δ * ‖X‖ := by push_cast; ring

end Circuit

/-! ### Section C — T3 and T4: the shifted theory from identity availability, and the census -/

section Shifted

variable {A : Type} [Fintype A] [DecidableEq A]

/-- **THE SHIFTED THEORY FROM IDENTITY AVAILABILITY** `T⁽ⁿ⁾` on the carrier `A × Fin n`: the
same fields as `shift`, with the composite identity supplied by `hid` at `U = 1` in place of full
composite unitary control. Control enters `shift` only through that identity, at `avail_id` and at
`prepAvail_uniform`; the readout is inert-spectator compositionality and the discard is iterated
ancilla closure, as before. The existing `shift` is untouched. -/
noncomputable def shiftId (T : FiniteOperationalTheory A)
    (hid : ∀ n, T.availExt n Unit (fun _ => LinearMap.id))
    (hin : InertSpectatorCompositionality T) (hclos : IteratedAncillaClosure T) (n : ℕ) :
    FiniteOperationalTheory (A × Fin n) where
  avail := fun O _ _ F => T.availExt n O F
  availExt := fun m O _ _ F => T.availExt (n * m) O (fun a => transport (shiftIdx A n m) (F a))
  -- composite identity: IDENTITY AVAILABILITY
  avail_id := hid n
  -- coarse-graining: FREE
  avail_coarse := fun O O' _ _ _ _ F f hF => T.availExt_coarse n O O' F f hF
  availExt_coarse := by
    intro m O O' _ _ _ _ F f hF
    have h := T.availExt_coarse (n * m) O O' _ f hF
    show T.availExt (n * m) O' (fun a => transport (shiftIdx A n m)
      (∑ j ∈ Finset.univ.filter (fun j => f j = a), F j))
    simp only [transport_sum]
    exact h
  -- feed-forward: FREE
  availExt_bind := by
    intro m O O' _ _ _ _ F G hF hG
    show T.availExt (n * m) (O × O')
      (fun c => transport (shiftIdx A n m) ((G c.1 c.2).comp (F c.1)))
    simp only [AncillaClosure.transport_comp]
    exact T.availExt_bind (n * m) O O' _ (fun a b => transport (shiftIdx A n m) (G a b)) hF hG
  -- preparations: the uniform attachment followed by available transported interventions
  prepAvail := fun m P => 0 < m ∧ ∃ Φ,
    T.availExt (n * m) Unit (fun _ => transport (shiftIdx A n m) Φ)
      ∧ P = Φ.comp (uniformAttach m)
  -- fresh uniform attachment: DECLARED (the identity is available by IDENTITY AVAILABILITY)
  prepAvail_uniform := fun m =>
    ⟨Nat.succ_pos m, LinearMap.id, by
      rw [transport_id]
      exact hid _, by rw [LinearMap.id_comp]⟩
  -- post-composition: FREE
  prepAvail_post := by
    rintro m P Φ ⟨hm, Ψ, hΨ, rfl⟩ hΦ
    refine ⟨hm, Φ.comp Ψ, ?_, by rw [LinearMap.comp_assoc]⟩
    show T.availExt (n * m) Unit (fun _ => transport (shiftIdx A n m) (Φ.comp Ψ))
    simp only [AncillaClosure.transport_comp]
    exact availExt_comp_unit T _ _ _ hΨ hΦ
  -- readout of the fresh ancilla: the Lüders selector; available by INERT SPECTATORS
  readout := fun _ k => localLuders k
  readout_avail := fun m => availExt_relativeReadout T hin n m
  readout_local := fun _ k => localLuders_mapSpectatorIndependent k
  -- discard of the fresh ancilla back to the composite base: THE CLOSURE RULE
  prepAvail_discard := by
    rintro m P O _ _ F ⟨hm, Φ, hΦ, rfl⟩ hF
    obtain ⟨m', rfl⟩ := Nat.exists_eq_succ_of_ne_zero hm.ne'
    show T.availExt n O (fun a => discardWith (m' + 1) (Φ.comp (uniformAttach (m' + 1))) (F a))
    have hcomp : T.availExt (n * (m' + 1)) O
        (fun a => transport (shiftIdx A n (m' + 1)) ((F a).comp Φ)) := by
      simp only [AncillaClosure.transport_comp]
      exact availExt_comp_family T _ _ _ hΦ hF
    have h := hclos n m' O (fun a => (F a).comp Φ) hcomp
    simpa only [discardWith, LinearMap.comp_assoc] using h

theorem shiftId_avail_iff (T : FiniteOperationalTheory A)
    (hid : ∀ n, T.availExt n Unit (fun _ => LinearMap.id))
    (hin : InertSpectatorCompositionality T) (hclos : IteratedAncillaClosure T) (n : ℕ)
    (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ) :
    (shiftId T hid hin hclos n).avail O F ↔ T.availExt n O F := Iff.rfl

/-- A composite conjugation is available in the shifted theory exactly when its packed form is
available in `T`. -/
theorem shiftId_availExt_conj_iff (T : FiniteOperationalTheory A)
    (hid : ∀ n, T.availExt n Unit (fun _ => LinearMap.id))
    (hin : InertSpectatorCompositionality T) (hclos : IteratedAncillaClosure T) (n m : ℕ)
    (V : Matrix ((A × Fin n) × Fin m) ((A × Fin n) × Fin m) ℂ) :
    (shiftId T hid hin hclos n).availExt m Unit (fun _ => conjChannel V)
      ↔ T.availExt (n * m) Unit (fun _ => conjChannel (Matrix.reindex (shiftIdx A n m)
          (shiftIdx A n m) V)) := by
  show T.availExt (n * m) Unit (fun _ => transport (shiftIdx A n m) (conjChannel V)) ↔ _
  simp only [transport_conjChannel]

/-- **THE CIRCUIT IS AVAILABLE FROM THE AVAILABILITY OF ITS UNITARY**: `circuit_available` with
the one use of composite control replaced by the availability of the unitary actually run. -/
theorem circuit_available_of_avail (T : FiniteOperationalTheory A) (n : ℕ)
    (P : Matrix A A ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ) (hP : T.prepAvail n P)
    (U : Matrix (A × Fin n) (A × Fin n) ℂ) (hUav : T.availExt n Unit (fun _ => conjChannel U)) :
    T.avail (Fin n) (fun k => discardWith n P ((localLuders k).comp (conjChannel U))) := by
  have h2 := T.availExt_bind n Unit (Fin n) (fun _ => conjChannel U)
    (fun _ => T.readout n) hUav (fun _ => T.readout_avail n)
  have h3 := T.availExt_coarse n (Unit × Fin n) (Fin n) _ Prod.snd h2
  have hfilter : ∀ a : Fin n,
      (Finset.univ.filter (fun j : Unit × Fin n => j.2 = a)) = {((), a)} := by
    intro a
    ext ⟨u, b⟩
    simp [Prod.ext_iff]
  have h4 : (fun a : Fin n => ∑ j ∈ Finset.univ.filter (fun j : Unit × Fin n => j.2 = a),
        (T.readout n j.2).comp (conjChannel U))
      = fun a : Fin n => (localLuders a).comp (conjChannel U) := by
    funext a
    rw [hfilter a, Finset.sum_singleton, readout_is_localLuders]
  rw [h4] at h3
  exact T.prepAvail_discard n P (Fin n) _ hP h3

/-- The reindexing of a permutation matrix is the permutation matrix of the conjugated
permutation. -/
theorem reindex_permMatrix {l l' : Type} [Fintype l] [DecidableEq l] [Fintype l'] [DecidableEq l']
    (e : l ≃ l') (σ : Equiv.Perm l) :
    Matrix.reindex e e (permMatrix σ) = permMatrix ((e.symm.trans σ).trans e) := by
  ext i j
  simp only [Matrix.reindex_apply, Matrix.submatrix_apply, permMatrix, Equiv.trans_apply]
  congr 1
  apply propext
  constructor
  · intro h; rw [h, Equiv.apply_symm_apply]
  · intro h; rw [← h, Equiv.symm_apply_apply]

/-- The matrix of a bijection between index types, as a rectangular isometry. -/
def eqvMatrix {l l' : Type} [DecidableEq l'] (e : l ≃ l') : Matrix l' l ℂ :=
  Matrix.of fun i a => if e a = i then 1 else 0

theorem eqvMatrix_apply {l l' : Type} [DecidableEq l'] (e : l ≃ l') (i : l') (a : l) :
    eqvMatrix e i a = if e a = i then 1 else 0 := rfl

theorem eqvMatrix_mul {l l' : Type} [Fintype l] [DecidableEq l] [Fintype l'] [DecidableEq l']
    (e : l ≃ l') (M : Matrix l l ℂ) (i : l') (b : l) : (eqvMatrix e * M) i b = M (e.symm i) b := by
  rw [Matrix.mul_apply, Finset.sum_eq_single (e.symm i)]
  · rw [eqvMatrix_apply, Equiv.apply_symm_apply, if_pos rfl, one_mul]
  · intro a _ ha
    rw [eqvMatrix_apply, if_neg, zero_mul]
    intro h; exact ha (by rw [← h, Equiv.symm_apply_apply])
  · intro h; exact absurd (Finset.mem_univ _) h

theorem mul_eqvMatrix_conjTranspose {l l' : Type} [Fintype l] [DecidableEq l] [Fintype l']
    [DecidableEq l'] (e : l ≃ l') (N : Matrix l' l ℂ) (i j : l') :
    (N * (eqvMatrix e)ᴴ) i j = N i (e.symm j) := by
  rw [Matrix.mul_apply, Finset.sum_eq_single (e.symm j)]
  · rw [Matrix.conjTranspose_apply, eqvMatrix_apply, Equiv.apply_symm_apply, if_pos rfl, star_one,
      mul_one]
  · intro b _ hb
    rw [Matrix.conjTranspose_apply, eqvMatrix_apply, if_neg, star_zero, mul_zero]
    intro h; exact hb (by rw [← h, Equiv.symm_apply_apply])
  · intro h; exact absurd (Finset.mem_univ _) h

theorem eqvMatrix_gram {l l' : Type} [Fintype l] [DecidableEq l] [Fintype l'] [DecidableEq l']
    (e : l ≃ l') : (eqvMatrix e)ᴴ * eqvMatrix e = 1 := by
  ext a b
  rw [Matrix.mul_apply, Finset.sum_eq_single (e a)]
  · rw [Matrix.conjTranspose_apply, eqvMatrix_apply, eqvMatrix_apply, if_pos rfl, star_one,
      one_mul, Matrix.one_apply]
    by_cases h : a = b
    · subst h; simp
    · rw [if_neg, if_neg h]
      intro h'; exact h (e.injective h'.symm)
  · intro i _ hi
    rw [Matrix.conjTranspose_apply, eqvMatrix_apply, if_neg (Ne.symm hi), star_zero, zero_mul]
  · intro h; exact absurd (Finset.mem_univ _) h

/-- **REINDEXING IS CONJUGATION BY THE BIJECTION MATRIX.** -/
theorem reindex_eq_eqvMatrix_conj {l l' : Type} [Fintype l] [DecidableEq l] [Fintype l']
    [DecidableEq l'] (e : l ≃ l') (M : Matrix l l ℂ) :
    Matrix.reindex e e M = eqvMatrix e * M * (eqvMatrix e)ᴴ := by
  ext i j
  rw [Matrix.reindex_apply, Matrix.submatrix_apply, mul_eqvMatrix_conjTranspose, eqvMatrix_mul]

/-- **REINDEXING DOES NOT INCREASE THE OPERATOR NORM.** -/
theorem norm_reindex_le {l l' : Type} [Fintype l] [DecidableEq l] [Fintype l'] [DecidableEq l']
    [Nonempty l] (e : l ≃ l') (M : Matrix l l ℂ) : ‖Matrix.reindex e e M‖ ≤ ‖M‖ := by
  rw [reindex_eq_eqvMatrix_conj]
  exact norm_isometry_conj_le (eqvMatrix_gram e) M

end Shifted

/-! ### Section D — T4 and T5: the exact consumptions discharged from the closure -/

section Census

/-- **THE IDENTITY IS AVAILABLE AT EVERY LEVEL UNDER THE CLOSURE**, from the exchanges alone. -/
theorem id_avail_of_derivedOI {T : FiniteOperationalTheory (Fin 2)} (hd : DerivedOI T) (n : ℕ) :
    T.availExt n Unit (fun _ => LinearMap.id) := by
  have h := one_mem_availSet T hd n
  rwa [mem_availSet, conjChannel_one] at h

/-- **INERT-SPECTATOR COMPOSITIONALITY IS A CONSEQUENCE OF THE CLOSURE** on every nonempty
carrier: implementation locality gives parallel reference extension, which is the same property. -/
theorem inert_of_derivedOI {A : Type} [Fintype A] [DecidableEq A] [Nonempty A]
    {T : FiniteOperationalTheory A} (hd : DerivedOI T) : InertSpectatorCompositionality T :=
  (OIHierarchyGeneral.observationalIndependence_iff_inert T).mp
    (observationalIndependence_of_implementationLocality hd.implementationLocality)

/-- **THE ANCILLA SWAPS ARE AVAILABLE IN THE SHIFTED THEORY**, from the exchanges of `T`: a swap
on the packed carrier is a permutation matrix. -/
theorem shiftId_swap_avail {T : FiniteOperationalTheory (Fin 2)} (hd : DerivedOI T)
    (hid : ∀ n, T.availExt n Unit (fun _ => LinearMap.id))
    (hin : InertSpectatorCompositionality T) (hclos : IteratedAncillaClosure T)
    {n m : ℕ} (hn : 0 < n) (hm : 0 < m) (k k₀ : Fin m) :
    (shiftId T hid hin hclos n).availExt m Unit
      (fun _ => conjChannel (permMatrix (ancSwap (A := Fin 2 × Fin n) m k k₀))) := by
  rw [shiftId_availExt_conj_iff, reindex_permMatrix]
  exact permMatrix_mem_availSet T hd (Nat.mul_pos hn hm) _

/-- **DENSE CONTROL DESCENDS TO THE SHIFTED THEORY**: every unitary on the shifted composite is
approximated, up to a unit scalar, by a unitary whose conjugation is available there. -/
theorem shiftId_approx {T : FiniteOperationalTheory (Fin 2)} (hdense : DenseUnitaryControl T)
    (hid : ∀ n, T.availExt n Unit (fun _ => LinearMap.id))
    (hin : InertSpectatorCompositionality T) (hclos : IteratedAncillaClosure T)
    {n m : ℕ} (hn : 0 < n) (hm : 0 < m)
    (U : Matrix ((Fin 2 × Fin n) × Fin m) ((Fin 2 × Fin n) × Fin m) ℂ) (hU : Uᴴ * U = 1)
    {δ : ℝ} (hδ : 0 < δ) :
    ∃ (V : Matrix ((Fin 2 × Fin n) × Fin m) ((Fin 2 × Fin n) × Fin m) ℂ) (c : ℂ),
      Vᴴ * V = 1 ∧ ‖c‖ = 1
        ∧ (shiftId T hid hin hclos n).availExt m Unit (fun _ => conjChannel V)
        ∧ ‖U - c • V‖ < δ := by
  set e := shiftIdx (Fin 2) n m with he
  have : Nonempty (Fin 2 × Fin (n * m)) := ⟨(0, ⟨0, Nat.mul_pos hn hm⟩)⟩
  obtain ⟨W, c, hW, hc, hav, hclose⟩ :=
    hdense (n * m) (Matrix.reindex e e U) (reindex_isometry e U hU) δ hδ
  have hWW : Matrix.reindex e e (Matrix.reindex e.symm e.symm W) = W := by
    rw [← Matrix.reindex_symm, Equiv.apply_symm_apply]
  refine ⟨Matrix.reindex e.symm e.symm W, c, reindex_isometry e.symm W hW, hc, ?_, ?_⟩
  · rw [shiftId_availExt_conj_iff, hWW]
    exact hav
  · have hsub : U - c • Matrix.reindex e.symm e.symm W
        = Matrix.reindex e.symm e.symm (Matrix.reindex e e U - c • W) := by
      ext p q
      simp only [Matrix.sub_apply, Matrix.smul_apply, Matrix.reindex_apply, Matrix.submatrix_apply,
        Equiv.symm_symm, Equiv.symm_apply_apply]
    rw [hsub]
    exact lt_of_le_of_lt (norm_reindex_le e.symm _) hclose

end Census

/-! ### Section E — T6: the approximate Stinespring assembly -/

section Assembly

/-- **DENSE UNITARY CONTROL GIVES DENSE INSTRUMENTS UNDER THE CLOSURE.** Every finite endomorphic
Kraus instrument at every positive level is approximated, outcome by outcome in the channel metric,
by an available family: the Stinespring unitary of its representation is replaced by an available
approximant, the circuit is run in the shifted theory with every other consumption exact from the
closure, and the branch bound controls the error. The identity, the ancilla swaps, the spectators
and the closure are all derived from `DerivedOI` inside the proof; nothing else is assumed. -/
theorem krausDense_of_denseControl {T : FiniteOperationalTheory (Fin 2)} (hd : DerivedOI T)
    (hdense : DenseUnitaryControl T) : KrausDense T := by
  intro k m F hF ε hε
  obtain ⟨r, K, out, hnorm, rfl⟩ := hF
  have hid := id_avail_of_derivedOI hd
  have hin := inert_of_derivedOI hd
  have hclos := hd.closure
  -- the target Stinespring unitary of the representation
  obtain ⟨U, hU, hUE⟩ := finiteIsometryExtensionSF_discharged (Fin 2 × Fin (k + 1)) r 0 (Vsf K)
    (by rw [vsf_gram]; exact hnorm)
  -- the tolerance on the unitary
  have hC : (0 : ℝ) < 2 * ((r : ℝ) + 1) * ((r : ℝ) + 1) := by positivity
  set δ := ε / (2 * ((r : ℝ) + 1) * ((r : ℝ) + 1)) with hδdef
  have hδ : 0 < δ := div_pos hε hC
  -- the available approximant
  obtain ⟨V, c, hV, hc, hav, hclose⟩ :=
    shiftId_approx hdense hid hin hclos k.succ_pos r.succ_pos U hU hδ
  have hW : (c • V)ᴴ * (c • V) = 1 := unitary_unit_smul hc hV
  have havW : (shiftId T hid hin hclos (k + 1)).availExt (r + 1) Unit
      (fun _ => conjChannel (c • V)) := by
    rw [PairFlowEquivalence.conjChannel_unit_smul hc]
    exact hav
  -- the circuit in the shifted theory, every other consumption exact
  have hswap : ∀ j : Fin (r + 1), (shiftId T hid hin hclos (k + 1)).availExt (r + 1) Unit
      (fun _ => conjChannel (permMatrix (ancSwap (A := Fin 2 × Fin (k + 1)) (r + 1) j 0))) :=
    fun j => shiftId_swap_avail hd hid hin hclos k.succ_pos r.succ_pos j 0
  have hseed := pureSeedPrep_available_of_swap (shiftId T hid hin hclos (k + 1)) r 0 hswap
  have hcirc := circuit_available_of_avail (shiftId T hid hin hclos (k + 1)) (r + 1) _ hseed
    (c • V) havW
  have hT : T.availExt (k + 1) (Fin (r + 1))
      (fun j => discardMap (r + 1) 0 ((localLuders j).comp (conjChannel (c • V)))) := hcirc
  have hG := T.availExt_coarse (k + 1) (Fin (r + 1)) (Fin m) _ out hT
  refine ⟨_, hG, fun a => ?_⟩
  -- the branches of the exact circuit are the Kraus branches
  have hbranch : ∀ j, conjChannel (K j)
      = discardMap (r + 1) 0 ((localLuders j).comp (conjChannel U)) :=
    fun j => (LinearMap.ext fun ρ => stinespringCircuit_branch K 0 j U hUE ρ).symm
  have hF : instrumentBranch K out a = ∑ j ∈ Finset.univ.filter (fun j => out j = a),
      discardMap (r + 1) 0 ((localLuders j).comp (conjChannel U)) :=
    Finset.sum_congr rfl fun j _ => hbranch j
  rw [hF]
  -- each branch within `2 (r + 1) δ`, at most `r + 1` branches per outcome
  have hb : ∀ j ∈ Finset.univ.filter (fun j => out j = a),
      ChanWithin (2 * ((r : ℝ) + 1) * δ)
        (discardMap (r + 1) 0 ((localLuders j).comp (conjChannel U)))
        (discardMap (r + 1) 0 ((localLuders j).comp (conjChannel (c • V)))) :=
    fun j _ => branch_within 0 j hU hW hclose.le
  refine chanWithin_mono ?_ (chanWithin_sum _ hb)
  have hcard : ((Finset.univ.filter (fun j => out j = a)).card : ℝ) ≤ (r : ℝ) + 1 := by
    have h := Finset.card_filter_le (Finset.univ : Finset (Fin (r + 1))) (fun j => out j = a)
    rw [Finset.card_univ, Fintype.card_fin] at h
    exact_mod_cast h
  calc ((Finset.univ.filter (fun j => out j = a)).card : ℝ) * (2 * ((r : ℝ) + 1) * δ)
      ≤ ((r : ℝ) + 1) * (2 * ((r : ℝ) + 1) * δ) := by gcongr
    _ = ε := by rw [hδdef]; field_simp

/-- **DENSE FINITE QUANTUM MECHANICS UNDER THE CLOSURE**, with soundness kept as its own
conjunct: a theory satisfying the closure with dense unitary control may carry a surplus
operation that is not Kraus, so soundness is not a consequence of density. -/
theorem denseFiniteQM_of_denseControl {T : FiniteOperationalTheory (Fin 2)} (hd : DerivedOI T)
    (hdense : DenseUnitaryControl T) (hs : KrausSoundExt T) : DenseFiniteQM T :=
  ⟨hs, krausDense_of_denseControl hd hdense⟩

/-- **ONE FIXED GATE GIVES DENSE INSTRUMENTS**: the closure with one fixed discrete mixing gate at
one angle with `α/π` irrational approximates every finite endomorphic Kraus instrument. -/
theorem krausDense_of_fixedGate {T : FiniteOperationalTheory (Fin 2)} (hd : DerivedOI T) {α : ℝ}
    (hα : Irrational (α / Real.pi)) (hg : FixedGateSourced α T) : KrausDense T :=
  krausDense_of_denseControl hd (denseUnitaryControl_of_fixedGate T hd hα hg)

end Assembly

/-! ### Section F — T7: the endpoints for the canonical theory -/

section Canonical

/-- **THE CANONICAL FIXED-GATE THEORY HAS DENSE INSTRUMENTS** at every angle with `α/π`
irrational. -/
theorem fixedGateTheory_krausDense {α : ℝ} (hα : Irrational (α / Real.pi)) :
    KrausDense (fixedGateTheory α) :=
  krausDense_of_denseControl (fixedGateTheory_derivedOI α) (fixedGateTheory_denseUnitaryControl hα)

/-- **THE CANONICAL FIXED-GATE THEORY IS DENSE FINITE QUANTUM MECHANICS** at every angle with
`α/π` irrational: Kraus-sound, and dense in the finite instruments. It is not exact quantum
mechanics (`fixedGateTheory_not_qm`); density is not exactness. -/
theorem fixedGateTheory_denseFiniteQM {α : ℝ} (hα : Irrational (α / Real.pi)) :
    DenseFiniteQM (fixedGateTheory α) :=
  ⟨fixedGateTheory_krausSoundExt α, fixedGateTheory_krausDense hα⟩

/-- **A CONCRETE WITNESS**: the angle one radian. -/
theorem fixedGateTheory_one_denseFiniteQM : DenseFiniteQM (fixedGateTheory 1) :=
  fixedGateTheory_denseFiniteQM (by rw [one_div]; exact irrational_inv_iff.mpr irrational_pi)

end Canonical

end DenseInstrumentBridge
end OIBridge

#print axioms OIBridge.DenseInstrumentBridge.chanWithin_mono
#print axioms OIBridge.DenseInstrumentBridge.chanWithin_sum
#print axioms OIBridge.DenseInstrumentBridge.unitary_unit_smul
#print axioms OIBridge.DenseInstrumentBridge.norm_eq_one_of_isometry
#print axioms OIBridge.DenseInstrumentBridge.norm_isometry_conj_le
#print axioms OIBridge.DenseInstrumentBridge.norm_isometry_compress_le
#print axioms OIBridge.DenseInstrumentBridge.esf_gram
#print axioms OIBridge.DenseInstrumentBridge.ptraceAnc_eq_sum
#print axioms OIBridge.DenseInstrumentBridge.norm_ptraceAnc_le
#print axioms OIBridge.DenseInstrumentBridge.norm_localLuders_le
#print axioms OIBridge.DenseInstrumentBridge.norm_pureAttach_le
#print axioms OIBridge.DenseInstrumentBridge.branch_within
#print axioms OIBridge.DenseInstrumentBridge.shiftId_avail_iff
#print axioms OIBridge.DenseInstrumentBridge.shiftId_availExt_conj_iff
#print axioms OIBridge.DenseInstrumentBridge.circuit_available_of_avail
#print axioms OIBridge.DenseInstrumentBridge.reindex_permMatrix
#print axioms OIBridge.DenseInstrumentBridge.eqvMatrix_apply
#print axioms OIBridge.DenseInstrumentBridge.eqvMatrix_mul
#print axioms OIBridge.DenseInstrumentBridge.mul_eqvMatrix_conjTranspose
#print axioms OIBridge.DenseInstrumentBridge.eqvMatrix_gram
#print axioms OIBridge.DenseInstrumentBridge.reindex_eq_eqvMatrix_conj
#print axioms OIBridge.DenseInstrumentBridge.norm_reindex_le
#print axioms OIBridge.DenseInstrumentBridge.id_avail_of_derivedOI
#print axioms OIBridge.DenseInstrumentBridge.inert_of_derivedOI
#print axioms OIBridge.DenseInstrumentBridge.shiftId_swap_avail
#print axioms OIBridge.DenseInstrumentBridge.shiftId_approx
#print axioms OIBridge.DenseInstrumentBridge.krausDense_of_denseControl
#print axioms OIBridge.DenseInstrumentBridge.denseFiniteQM_of_denseControl
#print axioms OIBridge.DenseInstrumentBridge.krausDense_of_fixedGate
#print axioms OIBridge.DenseInstrumentBridge.fixedGateTheory_krausDense
#print axioms OIBridge.DenseInstrumentBridge.fixedGateTheory_denseFiniteQM
#print axioms OIBridge.DenseInstrumentBridge.fixedGateTheory_one_denseFiniteQM
