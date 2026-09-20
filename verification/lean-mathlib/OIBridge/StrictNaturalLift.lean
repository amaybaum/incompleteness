import OIBridge.OrbitGeometryRigidity

/-!
# Act 27: the single-carrier gauge lemmas

The configuration is `Fin 4`, `Fin 1`, anchor `0`, and the uniform visible
matrix with entries `1 / 4`. All predicates are consumed from the pinned
modules. This module introduces no top-level definition.

The initial module commit contains shared lemmas only. The class-map targets
are executed in their separately ordered verdict commits.
-/

namespace OIBridge
namespace StrictNaturalLift

open Matrix DilationChoice CoherentLiftGauge TwoSidedGauge GramTrajectorySelection
  RepresentativeNaturality OrbitLawRigidityTwisted OrbitGeometryIsometries

theorem a27_shared_fibreGram_entry
    (U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) (i j k : Fin 4) :
    FibreGram (0 : Fin 1) U i j k = star (U (i, 0) (j, 0)) * U (i, 0) (k, 0) := by
  simpa only [Fin.sum_univ_one] using fibreGram_apply (0 : Fin 1) U i j k

theorem a27_shared_weak_diagonal (c : Fin 4 → ℂ) (hc : ∀ j, ‖c j‖ = 1) :
    WeakAnchorStabilizer (0 : Fin 1)
      (Matrix.diagonal fun p : Fin 4 × Fin 1 => c p.1) := by
  have h := (weak_diagonal_phase (a₀ := (0 : Fin 1)) c hc).1
  have heq : (Matrix.diagonal fun p : Fin 4 × Fin 1 => if p.2 = 0 then c p.1 else 1) =
      Matrix.diagonal (fun p : Fin 4 × Fin 1 => c p.1) := by
    congr 1
    funext p
    simp [Subsingleton.elim p.2 (0 : Fin 1)]
  rw [heq] at h
  exact h

theorem a27_shared_weak_one :
    WeakAnchorStabilizer (0 : Fin 1) (1 : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) := by
  simpa only [Matrix.diagonal_one] using a27_shared_weak_diagonal (fun _ => 1) (fun _ => by simp)

theorem a27_shared_left_diagonal (c : Fin 4 → ℂ) (hc : ∀ j, ‖c j‖ = 1) :
    LeftFibreGroup (Matrix.diagonal fun p : Fin 4 × Fin 1 => c p.1) := by
  refine ⟨(a27_shared_weak_diagonal c hc).1, ?_⟩
  intro p q hpq
  exact Matrix.diagonal_apply_ne _ (fun h => hpq (congrArg Prod.fst h))

theorem a27_shared_weak_shape (K : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) :
    WeakAnchorStabilizer (0 : Fin 1) K ↔
      ∃ c : Fin 4 → ℂ, (∀ j, ‖c j‖ = 1) ∧
        K = Matrix.diagonal (fun p : Fin 4 × Fin 1 => c p.1) := by
  constructor
  · rintro ⟨hK, c, hc⟩
    refine ⟨c, weak_anchor_coeff_norm_one hK hc, ?_⟩
    ext p q
    obtain ⟨j, a⟩ := q
    have ha : a = 0 := Subsingleton.elim _ _
    subst a
    rw [hc, Matrix.diagonal_apply]
    split_ifs with hp
    · subst p; rfl
    · rfl
  · rintro ⟨c, hc, rfl⟩
    exact a27_shared_weak_diagonal c hc

theorem a27_shared_left_shape (L : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) :
    LeftFibreGroup L ↔
      ∃ c : Fin 4 → ℂ, (∀ j, ‖c j‖ = 1) ∧
        L = Matrix.diagonal (fun p : Fin 4 × Fin 1 => c p.1) := by
  constructor
  · intro hL
    let c : Fin 4 → ℂ := fun i => L (i, 0) (i, 0)
    have hc : ∀ p j, L p (j, 0) = if p = (j, 0) then c j else 0 := by
      intro p j
      by_cases hp : p = (j, 0)
      · subst p; simp [c]
      · rw [if_neg hp]
        apply hL.2
        intro h
        apply hp
        exact Prod.ext h (Subsingleton.elim _ _)
    exact (a27_shared_weak_shape L).mp ⟨hL.1, c, hc⟩
  · rintro ⟨c, hc, rfl⟩
    exact a27_shared_left_diagonal c hc

theorem a27_shared_left_mul
    {L M : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ}
    (hL : LeftFibreGroup L) (hM : LeftFibreGroup M) : LeftFibreGroup (L * M) := by
  obtain ⟨c, hc, rfl⟩ := (a27_shared_left_shape L).mp hL
  obtain ⟨d, hd, rfl⟩ := (a27_shared_left_shape M).mp hM
  rw [Matrix.diagonal_mul_diagonal]
  exact a27_shared_left_diagonal (fun i => c i * d i)
    (fun i => by rw [norm_mul, hc, hd, one_mul])

theorem a27_shared_left_star
    {L : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ}
    (hL : LeftFibreGroup L) : LeftFibreGroup Lᴴ := by
  obtain ⟨c, hc, rfl⟩ := (a27_shared_left_shape L).mp hL
  rw [Matrix.diagonal_conjTranspose]
  exact a27_shared_left_diagonal (fun i => star (c i)) (fun i => by simpa using hc i)

theorem a27_shared_weak_star
    {K : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ}
    (hK : WeakAnchorStabilizer (0 : Fin 1) K) : WeakAnchorStabilizer (0 : Fin 1) Kᴴ := by
  obtain ⟨c, hc, rfl⟩ := (a27_shared_weak_shape K).mp hK
  rw [Matrix.diagonal_conjTranspose]
  exact a27_shared_weak_diagonal (fun i => star (c i)) (fun i => by simpa using hc i)

theorem a27_shared_left_admissible_iff
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (_hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    {L : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ} (hL : LeftFibreGroup L)
    (U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) :
    AdmissibleDilationAt Γ₀ (0 : Fin 1) (L * U) ↔
      AdmissibleDilationAt Γ₀ (0 : Fin 1) U := by
  have hLL : Lᴴ * L = 1 := by
    simpa only [Matrix.star_eq_conjTranspose] using Matrix.mem_unitaryGroup_iff'.mp hL.1
  constructor
  · intro h
    have h' := left_preserves_admissible (a27_shared_left_star hL) h
    simpa only [← Matrix.mul_assoc, hLL, Matrix.one_mul] using h'
  · exact left_preserves_admissible hL

theorem a27_shared_right_admissible_iff
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (_hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    {K : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ}
    (hK : WeakAnchorStabilizer (0 : Fin 1) K)
    (U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) :
    AdmissibleDilationAt Γ₀ (0 : Fin 1) (U * K) ↔
      AdmissibleDilationAt Γ₀ (0 : Fin 1) U := by
  have hKK : K * Kᴴ = 1 := by
    simpa only [Matrix.star_eq_conjTranspose] using Matrix.mem_unitaryGroup_iff.mp hK.1
  constructor
  · intro h
    have h' := weak_preserves_admissible h (a27_shared_weak_star hK)
    simpa only [Matrix.mul_assoc, hKK, Matrix.mul_one] using h'
  · exact fun h => weak_preserves_admissible h hK

theorem a27_shared_admissible_shape
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    (U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) :
    AdmissibleDilationAt Γ₀ (0 : Fin 1) U ↔
      U ∈ Matrix.unitaryGroup (Fin 4 × Fin 1) ℂ ∧
        ∀ i j, ‖U (i, 0) (j, 0)‖ ^ 2 = (1 / 4 : ℝ) := by
  constructor
  · intro h
    exact ⟨h.1, fun i j => by simpa [hΓ₀, Fin.sum_univ_one] using (h.2 i j).symm⟩
  · rintro ⟨hU, h⟩
    exact ⟨hU, fun i j => by simpa [hΓ₀, Fin.sum_univ_one] using (h i j).symm⟩

theorem a27_shared_admissible_entry_ne_zero
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    {U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ}
    (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U) (p q : Fin 4 × Fin 1) : U p q ≠ 0 := by
  obtain ⟨i, a⟩ := p
  obtain ⟨j, b⟩ := q
  have ha : a = 0 := Subsingleton.elim _ _
  have hb : b = 0 := Subsingleton.elim _ _
  subst a
  subst b
  intro hzero
  have h := OrbitGeometrySelector.realizable_entry_ne_zero
    (A := Fin 1) (by simp) Γ₀ (by intro i j; norm_num [hΓ₀])
    (FibreGram (0 : Fin 1) U) (sh1_necessity hU) i j j
  apply h
  simp only [a27_shared_fibreGram_entry, hzero, star_zero, mul_zero]

theorem a27_shared_same_gram
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    {U U' : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ}
    (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U)
    (_hU' : AdmissibleDilationAt Γ₀ (0 : Fin 1) U')
    (hG : FibreGram (0 : Fin 1) U = FibreGram (0 : Fin 1) U') :
    ∃ L : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ, LeftFibreGroup L ∧ U' = L * U := by
  classical
  have hrows : ∀ i : Fin 4, ∃ c : ℂ, ‖c‖ = 1 ∧ ∀ j, U' (i, 0) (j, 0) = c * U (i, 0) (j, 0) := by
    intro i
    apply rows_phase (fun j => U (i, 0) (j, 0)) (fun j => U' (i, 0) (j, 0))
    · intro j k
      simpa only [a27_shared_fibreGram_entry] using congrArg (fun G => G i j k) hG
    · exact fun j => a27_shared_admissible_entry_ne_zero Γ₀ hΓ₀ hU (i, 0) (j, 0)
  choose c hc hrow using hrows
  refine ⟨Matrix.diagonal (fun p : Fin 4 × Fin 1 => c p.1), a27_shared_left_diagonal c hc, ?_⟩
  ext p q
  obtain ⟨i, a⟩ := p
  obtain ⟨j, b⟩ := q
  have ha : a = 0 := Subsingleton.elim _ _
  have hb : b = 0 := Subsingleton.elim _ _
  subst a
  subst b
  simpa only [Matrix.diagonal_mul] using hrow i j

theorem a27_shared_realizable_of_equiv
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (_hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    {G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ}
    (hG : RealizableGram (Fin 1) Γ₀ G) (h : GramPhaseEquiv G G') :
    RealizableGram (Fin 1) Γ₀ G' := by
  obtain ⟨U, hU, hUG⟩ := sh1_sufficiency (0 : Fin 1) hG
  obtain ⟨c, hc, hphase⟩ := h
  obtain ⟨hK, hKcol⟩ := weak_diagonal_phase (a₀ := (0 : Fin 1)) c hc
  have hUK := weak_preserves_admissible hU hK
  have hEq : FibreGram (0 : Fin 1)
      (U * Matrix.diagonal (fun p : Fin 4 × Fin 1 => if p.2 = 0 then c p.1 else 1)) = G' := by
    funext i j k
    rw [fibreGram_mul_weak_apply hKcol, hUG, hphase]
  rw [← hEq]
  exact sh1_necessity hUK

theorem a27_shared_phase_coeff_eq
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    {U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ}
    (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U)
    (d d' k k' : Fin 4 → ℂ)
    (h : Matrix.diagonal (fun p : Fin 4 × Fin 1 => d p.1) * U *
        Matrix.diagonal (fun p : Fin 4 × Fin 1 => k p.1) =
      Matrix.diagonal (fun p : Fin 4 × Fin 1 => d' p.1) * U *
        Matrix.diagonal (fun p : Fin 4 × Fin 1 => k' p.1)) :
    ∀ i j, d i * k j = d' i * k' j := by
  intro i j
  have e := congrArg (fun M => M (i, 0) (j, 0)) h
  simp only [Matrix.diagonal_mul, Matrix.mul_diagonal] at e
  apply mul_right_cancel₀ (a27_shared_admissible_entry_ne_zero Γ₀ hΓ₀ hU (i, 0) (j, 0))
  calc
    (d i * k j) * U (i, 0) (j, 0) = d i * U (i, 0) (j, 0) * k j := by ring
    _ = d' i * U (i, 0) (j, 0) * k' j := e
    _ = (d' i * k' j) * U (i, 0) (j, 0) := by ring

/-- Equal phase representations act equally on every target matrix. -/
theorem a27_shared_transport_eq
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    {U D D' K K' : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ}
    (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U)
    (hD : LeftFibreGroup D) (hD' : LeftFibreGroup D')
    (hK : WeakAnchorStabilizer (0 : Fin 1) K)
    (hK' : WeakAnchorStabilizer (0 : Fin 1) K')
    (h : D * U * K = D' * U * K')
    (W : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) : D * W * K = D' * W * K' := by
  obtain ⟨d, hd, rfl⟩ := (a27_shared_left_shape D).mp hD
  obtain ⟨d', hd', rfl⟩ := (a27_shared_left_shape D').mp hD'
  obtain ⟨k, hk, rfl⟩ := (a27_shared_weak_shape K).mp hK
  obtain ⟨k', hk', rfl⟩ := (a27_shared_weak_shape K').mp hK'
  have e := a27_shared_phase_coeff_eq Γ₀ hΓ₀ hU d d' k k' h
  ext p q
  simp only [Matrix.diagonal_mul, Matrix.mul_diagonal]
  calc
    d p.1 * W p q * k q.1 = (d p.1 * k q.1) * W p q := by ring
    _ = (d' p.1 * k' q.1) * W p q := by rw [e]
    _ = d' p.1 * W p q * k' q.1 := by ring

/-- The common phase is the complete stabilizer of an admissible base dilation. -/
theorem a27_shared_torsor
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    {U D D' K K' : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ}
    (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U)
    (hD : LeftFibreGroup D) (hD' : LeftFibreGroup D')
    (hK : WeakAnchorStabilizer (0 : Fin 1) K)
    (hK' : WeakAnchorStabilizer (0 : Fin 1) K') :
    D * U * K = D' * U * K' ↔
      ∃ u : ℂ, ‖u‖ = 1 ∧ D' = u • D ∧ K' = u⁻¹ • K := by
  constructor
  · intro h
    obtain ⟨d, hd, rfl⟩ := (a27_shared_left_shape D).mp hD
    obtain ⟨d', hd', rfl⟩ := (a27_shared_left_shape D').mp hD'
    obtain ⟨k, hk, rfl⟩ := (a27_shared_weak_shape K).mp hK
    obtain ⟨k', hk', rfl⟩ := (a27_shared_weak_shape K').mp hK'
    have e := a27_shared_phase_coeff_eq Γ₀ hΓ₀ hU d d' k k' h
    have hk0 : k 0 ≠ 0 := by intro hz; have := hk 0; simp [hz] at this
    have hk'0 : k' 0 ≠ 0 := by intro hz; have := hk' 0; simp [hz] at this
    have hd'0 : d' 0 ≠ 0 := by intro hz; have := hd' 0; simp [hz] at this
    have ed : ∀ i, d' i = (k 0 / k' 0) * d i := by
      intro i
      rw [div_mul_eq_mul_div, eq_div_iff hk'0]
      calc
        d' i * k' 0 = d i * k 0 := (e i 0).symm
        _ = k 0 * d i := mul_comm _ _
    have ek : ∀ j, k' j = (k 0 / k' 0)⁻¹ * k j := by
      intro j
      rw [inv_div, div_mul_eq_mul_div, eq_div_iff hk0]
      apply mul_left_cancel₀ hd'0
      linear_combination -(k 0) * e 0 j + (k j) * e 0 0
    refine ⟨k 0 / k' 0, by rw [norm_div, hk, hk', div_self one_ne_zero], ?_, ?_⟩
    · ext p q
      by_cases hpq : p = q
      · subst q; simpa [Matrix.diagonal_apply, Matrix.smul_apply] using ed p.1
      · simp [hpq, Matrix.smul_apply]
    · ext p q
      by_cases hpq : p = q
      · subst q; simpa [Matrix.diagonal_apply, Matrix.smul_apply] using ek p.1
      · simp [hpq, Matrix.smul_apply]
  · rintro ⟨u, hu, rfl, rfl⟩
    have hn : u ≠ 0 := by intro hz; simp [hz] at hu
    simp only [Matrix.smul_mul, Matrix.mul_smul, smul_smul,
      inv_mul_cancel₀ hn, one_smul]

#print axioms a27_shared_fibreGram_entry
#print axioms a27_shared_weak_diagonal
#print axioms a27_shared_weak_one
#print axioms a27_shared_left_diagonal
#print axioms a27_shared_weak_shape
#print axioms a27_shared_left_shape
#print axioms a27_shared_left_mul
#print axioms a27_shared_left_star
#print axioms a27_shared_weak_star
#print axioms a27_shared_left_admissible_iff
#print axioms a27_shared_right_admissible_iff
#print axioms a27_shared_admissible_shape
#print axioms a27_shared_admissible_entry_ne_zero
#print axioms a27_shared_same_gram
#print axioms a27_shared_realizable_of_equiv
#print axioms a27_shared_phase_coeff_eq
#print axioms a27_shared_transport_eq
#print axioms a27_shared_torsor

/-!
## A27-0

The section below is the universal target, at the frozen configuration. The section indexed by
classes and the exact-tuple witnesses are both chosen inside the proof.

> **THE CLAUSE, carried at this mention — the A27-0 module section.**
> Act 27 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**
-/

theorem a27_0_strict_lift
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    (f : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ))
    (hf : ∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (f G))
    (hdesc : ∀ G G', RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ G' →
      GramPhaseEquiv G G' → GramPhaseEquiv (f G) (f G')) :
    ∃ (Φ₀ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ))
      (Ψ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ →
        Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      (∀ G, RealizableGram (Fin 1) Γ₀ G → GramPhaseEquiv (Φ₀ G) (f G)) ∧
      (∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (Φ₀ G)) ∧
      (∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
        FibreGram (0 : Fin 1) (Ψ U) = Φ₀ (FibreGram (0 : Fin 1) U)) ∧
      (∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
        AdmissibleDilationAt Γ₀ (0 : Fin 1) (Ψ U)) ∧
      StrictNatural (0 : Fin 1) Ψ := by
  classical
  let T := Fin 4 → Matrix (Fin 4) (Fin 4) ℂ
  let M := Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ
  let R := {G : T // RealizableGram (Fin 1) Γ₀ G}
  let s : Setoid R := {
    r := fun G H => GramPhaseEquiv G.val H.val
    iseqv := ⟨fun G => gramPhaseEquiv_refl G.val,
      fun h => gramPhaseEquiv_symm h, fun h h' => gramPhaseEquiv_trans h h'⟩ }
  let Q := Quotient s
  choose S hS hSG using fun (ω : Q) =>
    sh1_sufficiency (0 : Fin 1) (Quotient.out ω).property
  let fbar : Q → Q := Quotient.lift
    (fun G : R => Quotient.mk s (⟨f G.val, hf G.val G.property⟩ : R))
    (fun G H h => Quotient.sound (hdesc G.val H.val G.property H.property h))
  have hfbar (G : R) : fbar (Quotient.mk s G) =
      Quotient.mk s (⟨f G.val, hf G.val G.property⟩ : R) := rfl
  let q (U : M) (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U) : Q :=
    Quotient.mk s (⟨FibreGram (0 : Fin 1) U, sh1_necessity hU⟩ : R)
  have hqS (ω : Q) : q (S ω) (hS ω) = ω := by
    calc
      q (S ω) (hS ω) = Quotient.mk s (Quotient.out ω) :=
        congrArg (Quotient.mk s) (Subtype.ext (hSG ω))
      _ = ω := Quotient.out_eq ω
  have hdecomp (U : M) (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U) :
      ∃ D K : M, LeftFibreGroup D ∧ WeakAnchorStabilizer (0 : Fin 1) K ∧
        U = D * S (q U hU) * K := by
    apply (twoSided_slice_iff (hS (q U hU)).1 hU.1).mpr
    exact Quotient.exact (hqS (q U hU))
  choose D K hD hK hrepr using hdecomp
  let Ψ : M → M := fun U => if hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U then
    D U hU * S (fbar (q U hU)) * K U hU else U
  have htransport (U : M) (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U)
      (ω : Q) (D₀ K₀ : M) (hD₀ : LeftFibreGroup D₀)
      (hK₀ : WeakAnchorStabilizer (0 : Fin 1) K₀)
      (hq : q U hU = ω) (he : U = D₀ * S ω * K₀) :
      Ψ U = D₀ * S (fbar ω) * K₀ := by
    have e := (hrepr U hU).symm.trans he
    rw [hq] at e
    dsimp only [Ψ]
    rw [dif_pos hU, hq]
    obtain ⟨z, hz, hDz, hKz⟩ :=
      (a27_shared_torsor Γ₀ hΓ₀ (hS ω) (hD U hU) hD₀ (hK U hU) hK₀).mp e
    have hn : z ≠ 0 := by intro hzero; simp [hzero] at hz
    rw [hDz, hKz]
    simp only [M, Matrix.smul_mul, Matrix.mul_smul, smul_smul, inv_mul_cancel₀ hn, one_smul]
  have hΨ (U : M) (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U) :
      AdmissibleDilationAt Γ₀ (0 : Fin 1) (Ψ U) := by
    dsimp only [Ψ]
    rw [dif_pos hU]
    exact weak_preserves_admissible
      (left_preserves_admissible (hD U hU) (hS (fbar (q U hU)))) (hK U hU)
  have hstrict : StrictNatural (0 : Fin 1) Ψ := by
    constructor
    · intro L U hL
      by_cases hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U
      · have hLU := left_preserves_admissible hL hU
        have hq : q (L * U) hLU = q U hU := by
          apply Quotient.sound
          show GramPhaseEquiv (FibreGram (0 : Fin 1) (L * U)) (FibreGram (0 : Fin 1) U)
          have he : FibreGram (0 : Fin 1) (L * U) = FibreGram (0 : Fin 1) U :=
            funext fun i => fibreGram_left_mul hL (0 : Fin 1) U i
          rw [he]
          exact gramPhaseEquiv_refl _
        calc
          Ψ (L * U) = (L * D U hU) * S (fbar (q U hU)) * K U hU :=
            htransport (L * U) hLU (q U hU) (L * D U hU) (K U hU)
              (a27_shared_left_mul hL (hD U hU)) (hK U hU) hq
              (by simpa only [M, Matrix.mul_assoc] using congrArg (fun X => L * X) (hrepr U hU))
          _ = L * Ψ U := by simp only [Ψ, dif_pos hU, M, Matrix.mul_assoc]
      · have hLU : ¬ AdmissibleDilationAt Γ₀ (0 : Fin 1) (L * U) :=
          fun h => hU ((a27_shared_left_admissible_iff Γ₀ hΓ₀ hL U).mp h)
        simp only [Ψ, dif_neg hU, dif_neg hLU]
    · intro U K₀ hK₀
      by_cases hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U
      · have hUK := weak_preserves_admissible hU hK₀
        have hq : q (U * K₀) hUK = q U hU := by
          apply Quotient.sound
          show GramPhaseEquiv (FibreGram (0 : Fin 1) (U * K₀)) (FibreGram (0 : Fin 1) U)
          simpa only [Matrix.one_mul] using gramPhaseEquiv_symm
            (gramPhaseEquiv_of_twoSided (U := U) one_leftFibreGroup hK₀)
        calc
          Ψ (U * K₀) = D U hU * S (fbar (q U hU)) * (K U hU * K₀) :=
            htransport (U * K₀) hUK (q U hU) (D U hU) (K U hU * K₀)
              (hD U hU) (weak_mul (hK U hU) hK₀) hq
              (by simpa only [M, Matrix.mul_assoc] using congrArg (fun X => X * K₀) (hrepr U hU))
          _ = Ψ U * K₀ := by simp only [Ψ, dif_pos hU, M, Matrix.mul_assoc]
      · have hUK : ¬ AdmissibleDilationAt Γ₀ (0 : Fin 1) (U * K₀) :=
          fun h => hU ((a27_shared_right_admissible_iff Γ₀ hΓ₀ hK₀ U).mp h)
        simp only [Ψ, dif_neg hU, dif_neg hUK]
  have hqΨ (U : M) (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U) :
      q (Ψ U) (hΨ U hU) = fbar (q U hU) := by
    calc
      q (Ψ U) (hΨ U hU) = q (S (fbar (q U hU))) (hS (fbar (q U hU))) := by
        apply Quotient.sound
        show GramPhaseEquiv (FibreGram (0 : Fin 1) (Ψ U))
          (FibreGram (0 : Fin 1) (S (fbar (q U hU))))
        simpa only [Ψ, dif_pos hU] using gramPhaseEquiv_symm
          (gramPhaseEquiv_of_twoSided (U := S (fbar (q U hU))) (hD U hU) (hK U hU))
      _ = fbar (q U hU) := hqS _
  choose Uₜ hUₜ hGₜ using fun (G : T) (hG : RealizableGram (Fin 1) Γ₀ G) =>
    sh1_sufficiency (0 : Fin 1) hG
  let Φ₀ : T → T := fun G => if hG : RealizableGram (Fin 1) Γ₀ G then
    FibreGram (0 : Fin 1) (Ψ (Uₜ G hG)) else G
  refine ⟨Φ₀, Ψ, ?_, ?_, ?_, hΨ, hstrict⟩
  · intro G hG
    have hqU : q (Uₜ G hG) (hUₜ G hG) = Quotient.mk s (⟨G, hG⟩ : R) :=
      congrArg (Quotient.mk s) (Subtype.ext (hGₜ G hG))
    have he := hqΨ (Uₜ G hG) (hUₜ G hG)
    rw [hqU, hfbar] at he
    have hp : GramPhaseEquiv (FibreGram (0 : Fin 1) (Ψ (Uₜ G hG))) (f G) :=
      Quotient.exact he
    simpa only [Φ₀, dif_pos hG] using hp
  · intro G hG
    dsimp only [Φ₀]
    rw [dif_pos hG]
    exact sh1_necessity (hΨ (Uₜ G hG) (hUₜ G hG))
  · intro U hU
    have hF := sh1_necessity hU
    obtain ⟨L, hL, he⟩ := a27_shared_same_gram Γ₀ hΓ₀ hU
      (hUₜ (FibreGram (0 : Fin 1) U) hF) (hGₜ (FibreGram (0 : Fin 1) U) hF).symm
    dsimp only [Φ₀]
    rw [dif_pos hF, he, hstrict.1 L U hL]
    exact (funext fun i => fibreGram_left_mul hL (0 : Fin 1) (Ψ U) i).symm

#print axioms a27_0_strict_lift


/-!
## A27-H: four instantiations as class maps

Each conclusion allows the tuple representative supplied by A27-0. No statement
here asserts a strict lift of a specified tuple formula.

> **THE CLAUSE, carried at this mention — the A27-H module section.**
> Act 27 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**
-/

theorem a27_h_relabel_lift
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    (π τ : Equiv.Perm (Fin 4)) :
    ∃ (Φ₀ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ))
      (Ψ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ →
        Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      (∀ G, RealizableGram (Fin 1) Γ₀ G →
        GramPhaseEquiv (Φ₀ G) (fun i => (G (π i)).submatrix τ τ)) ∧
      (∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (Φ₀ G)) ∧
      (∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
        FibreGram (0 : Fin 1) (Ψ U) = Φ₀ (FibreGram (0 : Fin 1) U)) ∧
      (∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
        AdmissibleDilationAt Γ₀ (0 : Fin 1) (Ψ U)) ∧
      StrictNatural (0 : Fin 1) Ψ := by
  exact a27_0_strict_lift Γ₀ hΓ₀ (fun G i => (G (π i)).submatrix τ τ)
    (fun G hG => relabel2_realizable Γ₀ (by intros; simp [hΓ₀]) π τ G hG)
    (fun _ _ _ _ h => relabel2_gramPhaseEquiv π τ h)

theorem a27_h_conj_lift
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))) :
    ∃ (Φ₀ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ))
      (Ψ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ →
        Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      (∀ G, RealizableGram (Fin 1) Γ₀ G →
        GramPhaseEquiv (Φ₀ G) (fun i => Matrix.of fun j k => star (G i j k))) ∧
      (∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (Φ₀ G)) ∧
      (∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
        FibreGram (0 : Fin 1) (Ψ U) = Φ₀ (FibreGram (0 : Fin 1) U)) ∧
      (∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
        AdmissibleDilationAt Γ₀ (0 : Fin 1) (Ψ U)) ∧
      StrictNatural (0 : Fin 1) Ψ := by
  exact a27_0_strict_lift Γ₀ hΓ₀ (fun G i => Matrix.of fun j k => star (G i j k))
    (fun G hG => OrbitGeometrySelector.realizable_conj Γ₀ G hG)
    (fun _ _ _ _ h => OrbitGeometrySelector.conj_gramPhaseEquiv h)

/-- The transpose class is independent of the exact-tuple witness. -/
theorem a27_h_transpose_class
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    {U U' : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ}
    (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U)
    (hU' : AdmissibleDilationAt Γ₀ (0 : Fin 1) U')
    (h : GramPhaseEquiv (FibreGram (0 : Fin 1) U) (FibreGram (0 : Fin 1) U')) :
    GramPhaseEquiv (FibreGram (0 : Fin 1) Uᵀ) (FibreGram (0 : Fin 1) U'ᵀ) := by
  obtain ⟨W, hW, hWG, hUW⟩ := transpose_descends (0 : Fin 1)
    (fun y => Subsingleton.elim y 0) Γ₀ (0 : Fin 1) U hU (FibreGram (0 : Fin 1) U') h
  exact gramPhaseEquiv_trans hUW (transpose_single_valued (0 : Fin 1)
    (fun y => Subsingleton.elim y 0) Γ₀ (by intro i j; norm_num [hΓ₀])
    (0 : Fin 1) W U' hW hU' hWG)

theorem a27_h_transpose_lift
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))) :
    ∃ (Φ₀ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ))
      (Ψ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ →
        Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      (∀ G (hG : RealizableGram (Fin 1) Γ₀ G), GramPhaseEquiv (Φ₀ G)
        (FibreGram (0 : Fin 1) (Classical.choose (sh1_sufficiency (0 : Fin 1) hG))ᵀ)) ∧
      (∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (Φ₀ G)) ∧
      (∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
        FibreGram (0 : Fin 1) (Ψ U) = Φ₀ (FibreGram (0 : Fin 1) U)) ∧
      (∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
        AdmissibleDilationAt Γ₀ (0 : Fin 1) (Ψ U)) ∧
      StrictNatural (0 : Fin 1) Ψ := by
  classical
  let F : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) :=
    fun G => if hG : RealizableGram (Fin 1) Γ₀ G then
      FibreGram (0 : Fin 1) (Classical.choose (sh1_sufficiency (0 : Fin 1) hG))ᵀ else G
  have hreal : ∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (F G) := by
    intro G hG
    dsimp only [F]
    rw [dif_pos hG]
    exact sh1_necessity (transpose_admissible (0 : Fin 1) (fun y => Subsingleton.elim y 0)
      Γ₀ (by intro i j; simp [hΓ₀]) (0 : Fin 1) _
      (Classical.choose_spec (sh1_sufficiency (0 : Fin 1) hG)).1)
  have hdesc : ∀ G G', RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ G' →
      GramPhaseEquiv G G' → GramPhaseEquiv (F G) (F G') := by
    intro G G' hG hG' h
    dsimp only [F]
    rw [dif_pos hG, dif_pos hG']
    apply a27_h_transpose_class Γ₀ hΓ₀
      (Classical.choose_spec (sh1_sufficiency (0 : Fin 1) hG)).1
      (Classical.choose_spec (sh1_sufficiency (0 : Fin 1) hG')).1
    simpa only [(Classical.choose_spec (sh1_sufficiency (0 : Fin 1) hG)).2,
      (Classical.choose_spec (sh1_sufficiency (0 : Fin 1) hG')).2] using h
  obtain ⟨Φ₀, Ψ, hclass, hR, hE, hA, hN⟩ := a27_0_strict_lift Γ₀ hΓ₀ F hreal hdesc
  refine ⟨Φ₀, Ψ, ?_, hR, hE, hA, hN⟩
  intro G hG
  simpa only [F, dif_pos hG] using hclass G hG

theorem a27_h_transpose_conj_lift
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))) :
    ∃ (Φ₀ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ))
      (Ψ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ →
        Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      (∀ G (hG : RealizableGram (Fin 1) Γ₀ G), GramPhaseEquiv (Φ₀ G)
        (FibreGram (0 : Fin 1) (Classical.choose (sh1_sufficiency (0 : Fin 1)
          (OrbitGeometrySelector.realizable_conj Γ₀ G hG)))ᵀ)) ∧
      (∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (Φ₀ G)) ∧
      (∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
        FibreGram (0 : Fin 1) (Ψ U) = Φ₀ (FibreGram (0 : Fin 1) U)) ∧
      (∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
        AdmissibleDilationAt Γ₀ (0 : Fin 1) (Ψ U)) ∧
      StrictNatural (0 : Fin 1) Ψ := by
  classical
  let C : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) :=
    fun G i => Matrix.of fun j k => star (G i j k)
  let F : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) :=
    fun G => if hG : RealizableGram (Fin 1) Γ₀ (C G) then
      FibreGram (0 : Fin 1) (Classical.choose (sh1_sufficiency (0 : Fin 1) hG))ᵀ else C G
  have hC (G) (hG : RealizableGram (Fin 1) Γ₀ G) : RealizableGram (Fin 1) Γ₀ (C G) :=
    OrbitGeometrySelector.realizable_conj Γ₀ G hG
  have hreal : ∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (F G) := by
    intro G hG
    dsimp only [F]
    rw [dif_pos (hC G hG)]
    exact sh1_necessity (transpose_admissible (0 : Fin 1) (fun y => Subsingleton.elim y 0)
      Γ₀ (by intro i j; simp [hΓ₀]) (0 : Fin 1) _
      (Classical.choose_spec (sh1_sufficiency (0 : Fin 1) (hC G hG))).1)
  have hdesc : ∀ G G', RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ G' →
      GramPhaseEquiv G G' → GramPhaseEquiv (F G) (F G') := by
    intro G G' hG hG' h
    dsimp only [F]
    rw [dif_pos (hC G hG), dif_pos (hC G' hG')]
    apply a27_h_transpose_class Γ₀ hΓ₀
      (Classical.choose_spec (sh1_sufficiency (0 : Fin 1) (hC G hG))).1
      (Classical.choose_spec (sh1_sufficiency (0 : Fin 1) (hC G' hG'))).1
    simpa only [(Classical.choose_spec (sh1_sufficiency (0 : Fin 1) (hC G hG))).2,
      (Classical.choose_spec (sh1_sufficiency (0 : Fin 1) (hC G' hG'))).2] using
      OrbitGeometrySelector.conj_gramPhaseEquiv h
  obtain ⟨Φ₀, Ψ, hclass, hR, hE, hA, hN⟩ := a27_0_strict_lift Γ₀ hΓ₀ F hreal hdesc
  refine ⟨Φ₀, Ψ, ?_, hR, hE, hA, hN⟩
  intro G hG
  simpa only [F, dif_pos (hC G hG)] using hclass G hG

#print axioms a27_h_relabel_lift
#print axioms a27_h_conj_lift
#print axioms a27_h_transpose_class
#print axioms a27_h_transpose_lift
#print axioms a27_h_transpose_conj_lift

/-!
## A27-T: the specified relabelling formula

This conclusion concerns `StrictNatural` only. The given formula already has
act 20's twisted-natural lift; no failure of `TwistedNatural` or L4n is asserted.
The frozen witnesses are H(1), the phases (1, 1, 1, I), and coordinate (2, 2, 0).
-/

theorem a27_t_relabel_no_strict_lift
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))) :
    ¬ ∃ Ψ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ →
        Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ,
      StrictNatural (0 : Fin 1) Ψ ∧
      ∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
        FibreGram (0 : Fin 1) (Ψ U) =
          RelabelTransition (Equiv.swap (2 : Fin 4) 3) (FibreGram (0 : Fin 1) U) := by
  classical
  rintro ⟨Ψ, hN, hLift⟩
  let U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ := Matrix.of fun p q =>
    (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1
  have hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U :=
    OrbitLawGaps.hadamard_z_admissible Γ₀ hΓ₀ (1 : ℂ) (by simp)
  let c : Fin 4 → ℂ := ![1, 1, 1, Complex.I]
  have hc : ∀ j, ‖c j‖ = 1 := by intro j; fin_cases j <;> simp [c]
  let K : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ :=
    Matrix.diagonal fun p => if p.2 = 0 then c p.1 else 1
  have hK : WeakAnchorStabilizer (0 : Fin 1) K := (weak_diagonal_phase c hc).1
  have hKcol : ∀ p j, K p (j, 0) = if p = (j, 0) then c j else 0 :=
    (weak_diagonal_phase c hc).2
  have hUK := weak_preserves_admissible hU hK
  have he := congrArg (fun G => G (2 : Fin 4) 2 0) (hLift (U * K) hUK)
  rw [hN.2 U K hK, fibreGram_mul_weak_apply hKcol, hLift U hU] at he
  simp only [RelabelTransition, Matrix.submatrix_apply] at he
  rw [fibreGram_mul_weak_apply hKcol] at he
  change star (c 2) * FibreGram (0 : Fin 1) U 3 3 0 * c 0 =
    star (c 3) * FibreGram (0 : Fin 1) U 3 3 0 * c 0 at he
  rw [a27_shared_fibreGram_entry] at he
  change star (1 : ℂ) * (star ((1 / 2 : ℂ) * 1) * ((1 / 2 : ℂ) * 1)) * 1 =
    star Complex.I * (star ((1 / 2 : ℂ) * 1) * ((1 / 2 : ℂ) * 1)) * 1 at he
  norm_num [Complex.ext_iff] at he

#print axioms a27_t_relabel_no_strict_lift



/-- **A27-1-REVERSIBLE.** One fixed section supplies both lifts and their exact inverses.
The six rung conjuncts are stated on their frozen domains.

> **THE CLAUSE, carried at this mention — the A27-1 module section.**
> Act 27 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
> none. A law that survives every condition this freeze names is a law that survives **those**
> conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
> nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
> physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
> the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
> to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
> **No law gains physical status by surviving, no carrier and no principle is adopted as the physical
> one, and nothing here derives, recognises or approaches quantum evolution.**
-/
theorem a27_1_reversible_lift
    (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    (f : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ))
    (hf : ∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (f G))
    (hdesc : ∀ G G', RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ G' →
      GramPhaseEquiv G G' → GramPhaseEquiv (f G) (f G'))
    (hinj : ∀ G G', RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ G' →
      GramPhaseEquiv (f G) (f G') → GramPhaseEquiv G G')
    (hsurj : ∀ G', RealizableGram (Fin 1) Γ₀ G' →
      ∃ G, RealizableGram (Fin 1) Γ₀ G ∧ GramPhaseEquiv (f G) G') :
    ∃ (Φ₀ Φ₀' : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ))
      (Ψ Ψ' : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ →
        Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      ((∀ G, RealizableGram (Fin 1) Γ₀ G → GramPhaseEquiv (Φ₀ G) (f G)) ∧
       (∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (Φ₀ G)) ∧
       (∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
         FibreGram (0 : Fin 1) (Ψ U) = Φ₀ (FibreGram (0 : Fin 1) U)) ∧
       (∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
         AdmissibleDilationAt Γ₀ (0 : Fin 1) (Ψ U)) ∧
       StrictNatural (0 : Fin 1) Ψ) ∧
      (((∀ G, RealizableGram (Fin 1) Γ₀ G → GramPhaseEquiv (Φ₀' (Φ₀ G)) G) ∧
        (∀ G, RealizableGram (Fin 1) Γ₀ G → GramPhaseEquiv (Φ₀ (Φ₀' G)) G)) ∧
       (∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (Φ₀' G)) ∧
       (∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
         FibreGram (0 : Fin 1) (Ψ' U) = Φ₀' (FibreGram (0 : Fin 1) U)) ∧
       (∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U →
         AdmissibleDilationAt Γ₀ (0 : Fin 1) (Ψ' U)) ∧
       StrictNatural (0 : Fin 1) Ψ') ∧
      (∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U → Ψ' (Ψ U) = U) ∧
      (∀ U, AdmissibleDilationAt Γ₀ (0 : Fin 1) U → Ψ (Ψ' U) = U) ∧
      EvolvesTotally (Fin 1) (fun _ : ℕ => Γ₀) (fun _ : ℕ => Φ₀) ∧
      PreservesAdmissible (Fin 1) (fun _ : ℕ => Γ₀) (fun _ : ℕ => Φ₀) ∧
      (∃ Φ₁ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
        ∀ t : ℕ, (fun _ : ℕ => Φ₀) t = Φ₁) ∧
      Reversible (Fin 1) (fun _ : ℕ => Γ₀) (fun _ : ℕ => Φ₀) ∧
      (∀ t : ℕ, ∀ G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ,
        GramPhaseEquiv G G' → GramPhaseEquiv ((fun _ : ℕ => Φ₀) t G) ((fun _ : ℕ => Φ₀) t G')) ∧
      (∀ t : ℕ, ∃ Ψₜ αL αR : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ →
          Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ,
        (∀ U, AdmissibleDilationAt ((fun _ : ℕ => Γ₀) t) (0 : Fin 1) U →
          FibreGram (0 : Fin 1) (Ψₜ U) = (fun _ : ℕ => Φ₀) t (FibreGram (0 : Fin 1) U)) ∧
        (∀ U, AdmissibleDilationAt ((fun _ : ℕ => Γ₀) t) (0 : Fin 1) U →
          AdmissibleDilationAt ((fun _ : ℕ => Γ₀) (t + 1)) (0 : Fin 1) (Ψₜ U)) ∧
        TwistedNatural (0 : Fin 1) αL αR Ψₜ) := by
  classical
  let T := Fin 4 → Matrix (Fin 4) (Fin 4) ℂ
  let M := Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ
  let R := {G : T // RealizableGram (Fin 1) Γ₀ G}
  let s : Setoid R := {
    r := fun G H => GramPhaseEquiv G.val H.val
    iseqv := ⟨fun G => gramPhaseEquiv_refl G.val,
      fun h => gramPhaseEquiv_symm h, fun h h' => gramPhaseEquiv_trans h h'⟩ }
  let Q := Quotient s
  choose S hS hSG using fun (ω : Q) =>
    sh1_sufficiency (0 : Fin 1) (Quotient.out ω).property
  let fbar : Q → Q := Quotient.lift
    (fun G : R => Quotient.mk s (⟨f G.val, hf G.val G.property⟩ : R))
    (fun G H h => Quotient.sound (hdesc G.val H.val G.property H.property h))
  have hfbar (G : R) : fbar (Quotient.mk s G) =
      Quotient.mk s (⟨f G.val, hf G.val G.property⟩ : R) := rfl
  let q (U : M) (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U) : Q :=
    Quotient.mk s (⟨FibreGram (0 : Fin 1) U, sh1_necessity hU⟩ : R)
  have hqS (ω : Q) : q (S ω) (hS ω) = ω := by
    calc
      q (S ω) (hS ω) = Quotient.mk s (Quotient.out ω) :=
        congrArg (Quotient.mk s) (Subtype.ext (hSG ω))
      _ = ω := Quotient.out_eq ω
  have hdecomp (U : M) (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U) :
      ∃ D K : M, LeftFibreGroup D ∧ WeakAnchorStabilizer (0 : Fin 1) K ∧
        U = D * S (q U hU) * K := by
    apply (twoSided_slice_iff (hS (q U hU)).1 hU.1).mpr
    exact Quotient.exact (hqS (q U hU))
  choose D K hD hK hrepr using hdecomp
  let Ψ : (Q → Q) → M → M := fun g U => if hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U then
    D U hU * S (g (q U hU)) * K U hU else U
  have htransport (g : Q → Q) (U : M) (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U)
      (ω : Q) (D₀ K₀ : M) (hD₀ : LeftFibreGroup D₀)
      (hK₀ : WeakAnchorStabilizer (0 : Fin 1) K₀)
      (hq : q U hU = ω) (he : U = D₀ * S ω * K₀) :
      (Ψ g) U = D₀ * S (g ω) * K₀ := by
    have e := (hrepr U hU).symm.trans he
    rw [hq] at e
    dsimp only [Ψ]
    rw [dif_pos hU, hq]
    obtain ⟨z, hz, hDz, hKz⟩ :=
      (a27_shared_torsor Γ₀ hΓ₀ (hS ω) (hD U hU) hD₀ (hK U hU) hK₀).mp e
    have hn : z ≠ 0 := by intro hzero; simp [hzero] at hz
    rw [hDz, hKz]
    simp only [M, Matrix.smul_mul, Matrix.mul_smul, smul_smul, inv_mul_cancel₀ hn, one_smul]
  have hΨ (g : Q → Q) (U : M) (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U) :
      AdmissibleDilationAt Γ₀ (0 : Fin 1) ((Ψ g) U) := by
    dsimp only [Ψ]
    rw [dif_pos hU]
    exact weak_preserves_admissible
      (left_preserves_admissible (hD U hU) (hS (g (q U hU)))) (hK U hU)
  have hstrict (g : Q → Q) : StrictNatural (0 : Fin 1) (Ψ g) := by
    constructor
    · intro L U hL
      by_cases hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U
      · have hLU := left_preserves_admissible hL hU
        have hq : q (L * U) hLU = q U hU := by
          apply Quotient.sound
          show GramPhaseEquiv (FibreGram (0 : Fin 1) (L * U)) (FibreGram (0 : Fin 1) U)
          have he : FibreGram (0 : Fin 1) (L * U) = FibreGram (0 : Fin 1) U :=
            funext fun i => fibreGram_left_mul hL (0 : Fin 1) U i
          rw [he]
          exact gramPhaseEquiv_refl _
        calc
          (Ψ g) (L * U) = (L * D U hU) * S (g (q U hU)) * K U hU :=
            htransport g (L * U) hLU (q U hU) (L * D U hU) (K U hU)
              (a27_shared_left_mul hL (hD U hU)) (hK U hU) hq
              (by simpa only [M, Matrix.mul_assoc] using congrArg (fun X => L * X) (hrepr U hU))
          _ = L * (Ψ g) U := by simp only [Ψ, dif_pos hU, M, Matrix.mul_assoc]
      · have hLU : ¬ AdmissibleDilationAt Γ₀ (0 : Fin 1) (L * U) :=
          fun h => hU ((a27_shared_left_admissible_iff Γ₀ hΓ₀ hL U).mp h)
        simp only [Ψ, dif_neg hU, dif_neg hLU]
    · intro U K₀ hK₀
      by_cases hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U
      · have hUK := weak_preserves_admissible hU hK₀
        have hq : q (U * K₀) hUK = q U hU := by
          apply Quotient.sound
          show GramPhaseEquiv (FibreGram (0 : Fin 1) (U * K₀)) (FibreGram (0 : Fin 1) U)
          simpa only [Matrix.one_mul] using gramPhaseEquiv_symm
            (gramPhaseEquiv_of_twoSided (U := U) one_leftFibreGroup hK₀)
        calc
          (Ψ g) (U * K₀) = D U hU * S (g (q U hU)) * (K U hU * K₀) :=
            htransport g (U * K₀) hUK (q U hU) (D U hU) (K U hU * K₀)
              (hD U hU) (weak_mul (hK U hU) hK₀) hq
              (by simpa only [M, Matrix.mul_assoc] using congrArg (fun X => X * K₀) (hrepr U hU))
          _ = (Ψ g) U * K₀ := by simp only [Ψ, dif_pos hU, M, Matrix.mul_assoc]
      · have hUK : ¬ AdmissibleDilationAt Γ₀ (0 : Fin 1) (U * K₀) :=
          fun h => hU ((a27_shared_right_admissible_iff Γ₀ hΓ₀ hK₀ U).mp h)
        simp only [Ψ, dif_neg hU, dif_neg hUK]
  have hqΨ (g : Q → Q) (U : M) (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U) :
      q ((Ψ g) U) (hΨ g U hU) = g (q U hU) := by
    calc
      q ((Ψ g) U) (hΨ g U hU) = q (S (g (q U hU))) (hS (g (q U hU))) := by
        apply Quotient.sound
        show GramPhaseEquiv (FibreGram (0 : Fin 1) ((Ψ g) U))
          (FibreGram (0 : Fin 1) (S (g (q U hU))))
        simpa only [Ψ, dif_pos hU] using gramPhaseEquiv_symm
          (gramPhaseEquiv_of_twoSided (U := S (g (q U hU))) (hD U hU) (hK U hU))
      _ = g (q U hU) := hqS _
  choose Uₜ hUₜ hGₜ using fun (G : T) (hG : RealizableGram (Fin 1) Γ₀ G) =>
    sh1_sufficiency (0 : Fin 1) hG
  let Φ : (Q → Q) → T → T := fun g G => if hG : RealizableGram (Fin 1) Γ₀ G then
    FibreGram (0 : Fin 1) (Ψ g (Uₜ G hG)) else G
  have hΦvalue (g : Q → Q) (G : T) (hG : RealizableGram (Fin 1) Γ₀ G) :
      Φ g G = FibreGram (0 : Fin 1) (Ψ g (Uₜ G hG)) := dif_pos hG
  have hΦ (g : Q → Q) (G : T) (hG : RealizableGram (Fin 1) Γ₀ G) :
      RealizableGram (Fin 1) Γ₀ (Φ g G) := by
    rw [hΦvalue g G hG]
    exact sh1_necessity (hΨ g (Uₜ G hG) (hUₜ G hG))
  have hExact (g : Q → Q) (U : M) (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U) :
      FibreGram (0 : Fin 1) (Ψ g U) = Φ g (FibreGram (0 : Fin 1) U) := by
    have hF := sh1_necessity hU
    obtain ⟨L, hL, he⟩ := a27_shared_same_gram Γ₀ hΓ₀ hU
      (hUₜ (FibreGram (0 : Fin 1) U) hF) (hGₜ (FibreGram (0 : Fin 1) U) hF).symm
    dsimp only [Φ]
    rw [dif_pos hF, he, (hstrict g).1 L U hL]
    exact (funext fun i => fibreGram_left_mul hL (0 : Fin 1) (Ψ g U) i).symm
  have hClass (G : T) (hG : RealizableGram (Fin 1) Γ₀ G) :
      GramPhaseEquiv (Φ fbar G) (f G) := by
    have hqU : q (Uₜ G hG) (hUₜ G hG) = Quotient.mk s (⟨G, hG⟩ : R) :=
      congrArg (Quotient.mk s) (Subtype.ext (hGₜ G hG))
    have he := hqΨ fbar (Uₜ G hG) (hUₜ G hG)
    rw [hqU, hfbar] at he
    have hp : GramPhaseEquiv (FibreGram (0 : Fin 1) (Ψ fbar (Uₜ G hG))) (f G) :=
      Quotient.exact he
    simpa only [Φ, dif_pos hG] using hp
  have hfi : Function.Injective fbar := by
    intro ω ω'
    refine Quotient.inductionOn₂ ω ω' ?_
    intro G G' he
    exact Quotient.sound (hinj G.val G'.val G.property G'.property (Quotient.exact he))
  have hfs : Function.Surjective fbar := by
    intro ω
    refine Quotient.inductionOn ω ?_
    intro G'
    obtain ⟨G, hG, h⟩ := hsurj G'.val G'.property
    exact ⟨Quotient.mk s (⟨G, hG⟩ : R), Quotient.sound h⟩
  let e : Q ≃ Q := Equiv.ofBijective fbar ⟨hfi, hfs⟩
  have hgf (ω : Q) : e.symm (fbar ω) = ω := e.symm_apply_apply ω
  have hfg (ω : Q) : fbar (e.symm ω) = ω := e.apply_symm_apply ω
  have hLeft (U : M) (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U) :
      Ψ e.symm (Ψ fbar U) = U := by
    calc
      Ψ e.symm (Ψ fbar U) = D U hU * S (e.symm (fbar (q U hU))) * K U hU :=
        htransport e.symm (Ψ fbar U) (hΨ fbar U hU) (fbar (q U hU))
          (D U hU) (K U hU) (hD U hU) (hK U hU) (hqΨ fbar U hU)
          (by simp only [Ψ, dif_pos hU])
      _ = U := by rw [hgf]; exact (hrepr U hU).symm
  have hRight (U : M) (hU : AdmissibleDilationAt Γ₀ (0 : Fin 1) U) :
      Ψ fbar (Ψ e.symm U) = U := by
    calc
      Ψ fbar (Ψ e.symm U) = D U hU * S (fbar (e.symm (q U hU))) * K U hU :=
        htransport fbar (Ψ e.symm U) (hΨ e.symm U hU) (e.symm (q U hU))
          (D U hU) (K U hU) (hD U hU) (hK U hU) (hqΨ e.symm U hU)
          (by simp only [Ψ, dif_pos hU])
      _ = U := by rw [hfg]; exact (hrepr U hU).symm
  have hLeftTuple (G : T) (hG : RealizableGram (Fin 1) Γ₀ G) :
      Φ e.symm (Φ fbar G) = G := by
    rw [hΦvalue fbar G hG, ← hExact e.symm _ (hΨ fbar _ (hUₜ G hG)),
      hLeft _ (hUₜ G hG), hGₜ G hG]
  have hRightTuple (G : T) (hG : RealizableGram (Fin 1) Γ₀ G) :
      Φ fbar (Φ e.symm G) = G := by
    rw [hΦvalue e.symm G hG, ← hExact fbar _ (hΨ e.symm _ (hUₜ G hG)),
      hRight _ (hUₜ G hG), hGₜ G hG]
  have hGlobalDesc (G G' : T) (h : GramPhaseEquiv G G') :
      GramPhaseEquiv (Φ fbar G) (Φ fbar G') := by
    by_cases hG : RealizableGram (Fin 1) Γ₀ G
    · have hG' := a27_shared_realizable_of_equiv Γ₀ hΓ₀ hG h
      exact gramPhaseEquiv_trans (hClass G hG)
        (gramPhaseEquiv_trans (hdesc G G' hG hG' h) (gramPhaseEquiv_symm (hClass G' hG')))
    · have hG' : ¬ RealizableGram (Fin 1) Γ₀ G' := fun hG' =>
        hG (a27_shared_realizable_of_equiv Γ₀ hΓ₀ hG' (gramPhaseEquiv_symm h))
      simpa only [Φ, dif_neg hG, dif_neg hG'] using h
  have hRev : Reversible (Fin 1) (fun _ : ℕ => Γ₀) (fun _ : ℕ => Φ fbar) := by
    constructor
    · intro t G G' hG hG' he
      exact hinj G G' hG hG' (gramPhaseEquiv_trans (gramPhaseEquiv_symm (hClass G hG))
        (gramPhaseEquiv_trans he (hClass G' hG')))
    · intro t G' hG'
      obtain ⟨G, hG, he⟩ := hsurj G' hG'
      exact ⟨G, hG, gramPhaseEquiv_trans (hClass G hG) he⟩
  have hTotal : EvolvesTotally (Fin 1) (fun _ : ℕ => Γ₀) (fun _ : ℕ => Φ fbar) := by
    intro G₀ hG₀
    refine ⟨fun t => (Φ fbar)^[t] G₀, ?_, ?_, gramPhaseEquiv_refl G₀⟩
    · intro t
      induction t with
      | zero => exact hG₀
      | succ n ih =>
        change RealizableGram (Fin 1) Γ₀ ((Φ fbar)^[n + 1] G₀)
        rw [Function.iterate_succ_apply']
        exact hΦ fbar _ ih
    · intro t
      change GramPhaseEquiv ((Φ fbar)^[t + 1] G₀) (Φ fbar ((Φ fbar)^[t] G₀))
      rw [Function.iterate_succ_apply']
      exact gramPhaseEquiv_refl _
  refine ⟨Φ fbar, Φ e.symm, Ψ fbar, Ψ e.symm,
    ⟨hClass, hΦ fbar, hExact fbar, hΨ fbar, hstrict fbar⟩,
    ⟨⟨?_, ?_⟩, hΦ e.symm, hExact e.symm, hΨ e.symm, hstrict e.symm⟩,
    hLeft, hRight, hTotal, (fun _ => hΦ fbar), ⟨Φ fbar, fun _ => rfl⟩,
    hRev, (fun _ => hGlobalDesc), ?_⟩
  · intro G hG
    rw [hLeftTuple G hG]
    exact gramPhaseEquiv_refl G
  · intro G hG
    rw [hRightTuple G hG]
    exact gramPhaseEquiv_refl G
  · intro t
    exact ⟨Ψ fbar, id, id, hExact fbar, hΨ fbar, rnt1_strict_imp_twisted (hstrict fbar)⟩

#print axioms a27_1_reversible_lift

end StrictNaturalLift
end OIBridge
