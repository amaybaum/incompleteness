/-
  OIBridge/HiddenCoherence.lean — the fork, settled: exact quantum operations on the visible
  system do NOT force exact quantum operations on the composites.

  PHASE THREE, ROUND TWENTY-EIGHT. Round twenty-seven left one question open and said so:
  does `KrausSound T` imply `KrausSoundExt T`? This file answers NO, by construction — and
  then answers the sharper question, because soundness alone is a weak antecedent.

      ┌────────────────────────────────────────────────────────────────────┐
      │  `krausSound_not_implies_krausSoundExt`:                            │
      │      ∃ T,  KrausSound T  ∧  ¬ KrausSoundExt T.                      │
      │                                                                     │
      │  `exact_not_implies_krausSoundExt`:                                 │
      │      ∃ T,  ExactFiniteEndomorphicQuantumOps T  ∧  ¬ KrausSoundExt T.│
      └────────────────────────────────────────────────────────────────────┘

  READ THE TWO APART. The first is cheap in a way that matters: `hiddenCoherence` is sound
  but very INCOMPLETE — its system availability is nonnegative classical weights times the
  identity, so it does not have all the quantum operations on the system either. A theory
  can fail composite soundness while being poor on the system, which is not the separation
  anyone cares about. The second is the real one: `hiddenCoherenceFull` has EXACTLY the
  finite endomorphic quantum instruments on the system — available ⟺ Kraus-representable,
  by `isKrausFamily_iff` — and still carries a non-quantum composite operation. Only that
  makes "exact system QM" versus "exact composite QM" a genuine separation, and only the
  second theorem licenses the sentence at the top of this file.

  WHY THE ROUND-27 EXPOSURE PRINCIPLE DOES NOT BLOCK THIS. That principle is conditioned on
  a trace violation occurring ON THE REACHABLE STATE `P ρ`. The witness here lives where no
  available preparation goes: the only preparation the theory grants is the uniform
  attachment, whose image is ANCILLA-DIAGONAL, and the surplus acts only on ancilla
  COHERENCES. The hypothesis of `traceWitness_exposed_on_reachable` therefore never fires,
  and `badOp_invisible` proves the point directly — through the available preparation the
  bad map is the identity on the system, on the nose.

  §A — THE BLOCK SCHUR MULTIPLIERS. `blockOp n α γ` multiplies ancilla-diagonal block `k` by
  `γ k` and everything off the ancilla diagonal by `α`. These are closed under composition
  and sums with coefficients multiplying and adding (`blockOp_comp`, `blockOp_sum`), which
  is what makes the closure rules provable rather than hopeful; `LinearMap.id` and every
  local Lüders selector are of this form (`blockOp_one`, `localLuders_eq_blockOp`), so the
  theory keeps its identity and its native readout.

  §B — THE TWO THEORIES. They differ in ONE field and share everything else.

      availExt   = block multipliers whose block weights are nonnegative and sum to one
      prepAvail  = the uniform attachment, and nothing else
      readout    = the local Lüders selectors

      `hiddenCoherence`      avail = nonneg scalars summing to one, times the identity
      `hiddenCoherenceFull`  avail = ALL finite endomorphic Kraus families

  Every closure rule is discharged for both. `scalarAvail_isKraus` proves the scalar
  families really are normalized Kraus instruments, which gives `hiddenCoherence_krausSound`
  AND makes the shared `prepAvail_discard` computation serve both structures: every
  reachable discarded family is scalar (`discard_uniform_scalarAvail`), hence Kraus. The
  full theory then needs only that Kraus families are closed under coarse-graining
  (`isKrausFamily_coarse`), and its exactness is `isKrausFamily_iff` on the nose.

  §C — THE WITNESS. `badOp n = blockOp n 2 1` leaves every ancilla-diagonal block alone and
  DOUBLES every ancilla coherence. It is available (`badOp_availExt`), it is invisible
  through the granted preparation (`badOp_invisible`), and it is not completely positive
  (`badOp_not_cp`: its Choi matrix has the direction `e_{(s,k₀)} - e_{(s,k₁)}` at value
  `-2`), hence not Kraus by round twenty-seven's easy direction. Note it is TRACE-PRESERVING
  OUTRIGHT, not merely on the diagonal: a coherence never contributes to a trace, so
  doubling one changes no trace at all. What it scales is coherence AMPLITUDES, in exactly
  the sector the discard annihilates — which is why round twenty-six's trace identity is
  blind to it everywhere, not just on the reachable image.

  WHAT MAKES THIS LEGITIMATE, and it is worth being explicit. `HasCompositeUnitaryControl`
  is NOT a field of `FiniteOperationalTheory`. This theory withholds precisely the unitaries
  that would rotate the invisible coherence sector into the preparation image, and it is
  entitled to: control richness is a PROPERTY a theory may or may not have, not part of what
  it is to be one. So the countermodel says nothing against the Kraus round — it says that
  composite exactness is a separate axis from system exactness, and must be asked for
  separately rather than buried in a definition.

  WHAT IS STILL OPEN. What extra richness closes the gap. Composite unitary control plainly
  does for this construction — a unitary mixing two ancilla levels carries the coherence
  sector into the diagonal one — but that is not proved here, and whether something weaker
  suffices is not even formulated. Nothing in this file claims a hierarchy; it establishes
  the one separation it names.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.CompositeSoundness

namespace OIBridge
namespace HiddenCoherence

open Complex Matrix CoherentExtension MonoidalCompletion
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness

open scoped ComplexOrder

variable {A : Type*} [Fintype A] [DecidableEq A]

/-! ### Section A — the block Schur multipliers -/

/-- **THE BLOCK MULTIPLIERS.** Multiply the ancilla-diagonal block `k` by `γ k`, and every
entry off the ancilla diagonal by `α`. A Schur multiplier, so linearity is entrywise. -/
def blockOp (n : ℕ) (α : ℂ) (γ : Fin n → ℂ) :
    Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ where
  toFun M := Matrix.of fun p q => (if p.2 = q.2 then γ p.2 else α) * M p q
  map_add' M N := by
    ext p q
    show (if p.2 = q.2 then γ p.2 else α) * (M p q + N p q) = _
    rw [mul_add]
    rfl
  map_smul' c M := by
    ext p q
    show (if p.2 = q.2 then γ p.2 else α) * (c * M p q)
      = c * ((if p.2 = q.2 then γ p.2 else α) * M p q)
    ring

omit [Fintype A] [DecidableEq A] in
@[simp] theorem blockOp_apply (n : ℕ) (α : ℂ) (γ : Fin n → ℂ)
    (M : Matrix (A × Fin n) (A × Fin n) ℂ) (p q : A × Fin n) :
    blockOp n α γ M p q = (if p.2 = q.2 then γ p.2 else α) * M p q := rfl

omit [Fintype A] [DecidableEq A] in
/-- The identity is the constant-one multiplier, so the theory below keeps `avail_id`. -/
theorem blockOp_one (n : ℕ) :
    blockOp (A := A) n 1 (fun _ => 1) = LinearMap.id := by
  refine LinearMap.ext fun M => ?_
  ext p q
  rw [blockOp_apply]
  show (if p.2 = q.2 then (1 : ℂ) else 1) * M p q = M p q
  rw [ite_self, one_mul]

omit [Fintype A] [DecidableEq A] in
/-- **COMPOSITION MULTIPLIES THE COEFFICIENTS.** This is what makes `availExt_bind`
provable: the available set is closed under feed-forward because Schur multipliers compose
entrywise. -/
theorem blockOp_comp (n : ℕ) (α β : ℂ) (γ δ : Fin n → ℂ) :
    (blockOp (A := A) n α γ).comp (blockOp n β δ)
      = blockOp n (α * β) (fun k => γ k * δ k) := by
  refine LinearMap.ext fun M => ?_
  ext p q
  show (if p.2 = q.2 then γ p.2 else α) * ((if p.2 = q.2 then δ p.2 else β) * M p q)
    = (if p.2 = q.2 then γ p.2 * δ p.2 else α * β) * M p q
  rw [← mul_assoc]
  congr 1
  split <;> rfl

omit [Fintype A] [DecidableEq A] in
/-- **SUMS ADD THE COEFFICIENTS.** This is what makes the coarse-graining rules provable. -/
theorem blockOp_sum {ι : Type*} (n : ℕ) (s : Finset ι) (α : ι → ℂ) (γ : ι → Fin n → ℂ) :
    (∑ i ∈ s, blockOp (A := A) n (α i) (γ i))
      = blockOp n (∑ i ∈ s, α i) (fun k => ∑ i ∈ s, γ i k) := by
  refine LinearMap.ext fun M => ?_
  ext p q
  rw [LinearMap.sum_apply, Matrix.sum_apply]
  rw [Finset.sum_congr rfl fun i _ => blockOp_apply n (α i) (γ i) M p q, ← Finset.sum_mul]
  rw [blockOp_apply]
  congr 1
  split <;> rfl

omit [Fintype A] in
/-- The native readout is a block multiplier, so the theory below keeps its readout. -/
theorem localLuders_eq_blockOp (n : ℕ) (k : Fin n) :
    localLuders (A := A) k = blockOp n 0 (fun j => if k = j then 1 else 0) := by
  refine LinearMap.ext fun M => ?_
  ext p q
  rw [localLuders_apply, blockOp_apply]
  by_cases h : p.2 = q.2
  · rw [if_pos h]
    by_cases h2 : k = p.2
    · rw [if_pos h2, one_mul, if_pos ⟨h2.symm, h ▸ h2.symm⟩]
      subst h2
      rw [show ((q.1, p.2) : A × Fin n) = q from Prod.ext rfl h]
    · rw [if_neg h2, zero_mul, if_neg (fun hh => h2 hh.1.symm)]
  · rw [if_neg h, zero_mul, if_neg (fun hh => h (hh.1.trans hh.2.symm))]

/-! ### Section B — the theory -/

/-- Available SYSTEM families: nonnegative weights summing to one, times the identity. -/
def ScalarAvail {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ) : Prop :=
  ∃ w : O → ℝ, (∀ a, 0 ≤ w a) ∧ (∑ a, w a = 1) ∧
    ∀ a, F a = ((w a : ℂ)) • LinearMap.id

/-- Available COMPOSITE families: block multipliers whose block weights are nonnegative and
sum to one over the outcome label. The off-diagonal coefficient `α` is UNCONSTRAINED — that
is where the surplus lives. -/
def BlockAvail (n : ℕ) {O : Type} [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ) :
    Prop :=
  ∃ (α : O → ℂ) (w : O → Fin n → ℝ),
    (∀ a k, 0 ≤ w a k) ∧ (∀ k, ∑ a, w a k = 1) ∧
      ∀ a, F a = blockOp n (α a) (fun k => (w a k : ℂ))

/-- The ONLY preparation the theory grants: the uniform attachment. Its image is
ancilla-diagonal, which is exactly why the surplus stays invisible. -/
def SeedAvail (n : ℕ) (P : Matrix A A ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ) : Prop :=
  0 < n ∧ P = uniformAttach n

/-- The uniform attachment produces no ancilla coherence. -/
theorem uniformAttach_offDiag (n : ℕ) (ρ : Matrix A A ℂ) (p q : A × Fin n)
    (h : ¬ p.2 = q.2) : uniformAttach n ρ p q = 0 := by
  show ρ p.1 q.1 * (((n : ℂ)⁻¹ • (1 : Matrix (Fin n) (Fin n) ℂ)) p.2 q.2) = 0
  rw [Matrix.smul_apply, Matrix.one_apply_ne h, smul_zero, mul_zero]

/-- A block multiplier acting on the uniform attachment sees only its block weights — the
off-diagonal coefficient never touches anything. -/
theorem blockOp_uniformAttach (n : ℕ) (α : ℂ) (γ : Fin n → ℂ) (ρ : Matrix A A ℂ)
    (p q : A × Fin n) :
    blockOp n α γ (uniformAttach n ρ) p q
      = (if p.2 = q.2 then γ p.2 else 0) * uniformAttach n ρ p q := by
  rw [blockOp_apply]
  by_cases h : p.2 = q.2
  · rw [if_pos h, if_pos h]
  · rw [if_neg h, if_neg h, uniformAttach_offDiag n ρ p q h, mul_zero, mul_zero]

/-- **THE FIBREWISE REGROUPING**, used by every coarse-graining rule below. -/
theorem sum_fibers {O O' : Type} [Fintype O] [Fintype O'] [DecidableEq O']
    (f : O → O') (g : O → ℝ) :
    ∑ a' : O', ∑ a ∈ Finset.univ.filter (fun a => f a = a'), g a = ∑ a, g a :=
  Finset.sum_fiberwise_of_maps_to (fun x _ => Finset.mem_univ (f x)) g

/-- **THE SYSTEM SECTOR IS SOUND.** A nonnegative weight family summing to one, times the
identity, IS a normalized Kraus instrument: take `K_k = √(w_k) • 1`. The weights are what
make `∑ K† K = 1` come out. -/
theorem scalarAvail_isKraus {O : Type} [Fintype O] [DecidableEq O]
    {F : O → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ} (h : ScalarAvail F) :
    CompositeSoundness.IsKrausFamily F := by
  obtain ⟨w, hnn, hsum, hF⟩ := h
  have hne : Nonempty O := by
    by_contra hc
    rw [not_nonempty_iff] at hc
    rw [Finset.sum_of_isEmpty] at hsum
    exact absurd hsum (by norm_num)
  obtain ⟨m, hm⟩ := Nat.exists_eq_succ_of_ne_zero (Fintype.card_ne_zero (α := O))
  let e : Fin (m + 1) ≃ O := (Fintype.equivFinOfCardEq hm).symm
  have hstar : ∀ x : ℝ, star ((x : ℝ) : ℂ) = ((x : ℝ) : ℂ) := fun x => by simp
  have hsq : ∀ x : ℝ, 0 ≤ x → (Real.sqrt x : ℂ) * (Real.sqrt x : ℂ) = (x : ℂ) := by
    intro x hx
    rw [← Complex.ofReal_mul, Real.mul_self_sqrt hx]
  refine ⟨m, fun k => (Real.sqrt (w (e k)) : ℂ) • (1 : Matrix A A ℂ), fun k => e k, ?_, ?_⟩
  · have hterm : ∀ k : Fin (m + 1),
        (((Real.sqrt (w (e k)) : ℂ) • (1 : Matrix A A ℂ))ᴴ)
          * ((Real.sqrt (w (e k)) : ℂ) • (1 : Matrix A A ℂ))
          = ((w (e k) : ℂ)) • (1 : Matrix A A ℂ) := by
      intro k
      rw [Matrix.conjTranspose_smul, Matrix.conjTranspose_one, Matrix.smul_mul,
        Matrix.mul_smul, Matrix.one_mul, smul_smul]
      congr 1
      rw [hstar, hsq _ (hnn (e k))]
    rw [Finset.sum_congr rfl fun k _ => hterm k, ← Finset.sum_smul]
    have hs : ∑ k : Fin (m + 1), ((w (e k) : ℂ)) = ((∑ a, w a : ℝ) : ℂ) := by
      rw [Complex.ofReal_sum]
      exact Fintype.sum_equiv e _ _ fun k => rfl
    rw [hs, hsum, Complex.ofReal_one, one_smul]
  · intro a
    have hfil : Finset.univ.filter (fun k : Fin (m + 1) => e k = a) = {e.symm a} := by
      ext k
      simp [Finset.mem_filter, Equiv.eq_symm_apply]
    rw [hfil, Finset.sum_singleton, hF a]
    refine LinearMap.ext fun X => ?_
    show (w a : ℂ) • X
      = (Real.sqrt (w (e (e.symm a))) : ℂ) • (1 : Matrix A A ℂ) * X
          * ((Real.sqrt (w (e (e.symm a))) : ℂ) • (1 : Matrix A A ℂ))ᴴ
    rw [Equiv.apply_symm_apply, Matrix.conjTranspose_smul, Matrix.conjTranspose_one,
      Matrix.smul_mul, Matrix.one_mul, Matrix.mul_smul, Matrix.mul_one, smul_smul]
    congr 1
    rw [hstar, hsq _ (hnn a)]

/-- **KRAUS FAMILIES ARE CLOSED UNDER COARSE-GRAINING.** Relabel the output map; the
fibres regroup. This is what `hiddenCoherenceFull` needs for `avail_coarse`, and it is a
general fact about the representation predicate rather than anything about this theory. -/
theorem isKrausFamily_coarse {S : Type*} {O O' : Type} [Fintype S] [DecidableEq S] [Fintype O]
    [DecidableEq O] [Fintype O'] [DecidableEq O']
    {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : CompositeSoundness.IsKrausFamily F)
    (f : O → O') :
    CompositeSoundness.IsKrausFamily
      (fun a' => ∑ j ∈ Finset.univ.filter (fun j => f j = a'), F j) := by
  obtain ⟨n, K, out, hnorm, hF⟩ := h
  refine ⟨n, K, fun k => f (out k), hnorm, fun a' => ?_⟩
  have key : ∀ y ∈ Finset.univ.filter (fun j => f j = a'),
      (Finset.univ.filter (fun k => f (out k) = a')).filter (fun k => out k = y)
        = Finset.univ.filter (fun k => out k = y) := by
    intro y hy
    rw [Finset.mem_filter] at hy
    ext k
    simp only [Finset.mem_filter, Finset.mem_univ, true_and]
    exact ⟨fun hk => hk.2, fun hk => ⟨by rw [hk, hy.2], hk⟩⟩
  show (∑ j ∈ Finset.univ.filter (fun j => f j = a'), F j)
      = ∑ k ∈ Finset.univ.filter (fun k => f (out k) = a'), conjChannel (K k)
  rw [Finset.sum_congr rfl fun j _ => hF j,
    Finset.sum_congr rfl fun y hy =>
      congrArg (fun t => ∑ k ∈ t, conjChannel (K k)) (key y hy).symm]
  exact Finset.sum_fiberwise_of_maps_to
    (fun k hk => by
      rw [Finset.mem_filter] at hk ⊢
      exact ⟨Finset.mem_univ _, hk.2⟩) _

/-- **EVERY REACHABLE DISCARDED FAMILY IS SCALAR.** Prepare with the uniform attachment, run
an available composite family, discard: what comes out on the system is a nonnegative weight
family times the identity. Shared by both theories below — it is what makes
`prepAvail_discard` a computation rather than a classification. -/
theorem discard_uniform_scalarAvail {n : ℕ} (hn : 0 < n) {O : Type} [Fintype O]
    [DecidableEq O]
    {F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ}
    (hFa : BlockAvail n F) :
    ScalarAvail (fun a => discardWith n (uniformAttach n) (F a)) := by
  obtain ⟨α, w, hnn, hsum, hF⟩ := hFa
  have hn' : (n : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr hn.ne'
  refine ⟨fun a => (n : ℝ)⁻¹ * ∑ e, w a e,
    fun a => mul_nonneg (by positivity) (Finset.sum_nonneg fun e _ => hnn a e), ?_, ?_⟩
  · show ∑ a, (n : ℝ)⁻¹ * ∑ e, w a e = 1
    rw [← Finset.mul_sum, Finset.sum_comm]
    rw [Finset.sum_congr rfl fun e _ => hsum e, Finset.sum_const, Finset.card_univ,
      Fintype.card_fin, nsmul_eq_mul, mul_one, inv_mul_cancel₀ hn']
  · intro a
    refine LinearMap.ext fun ρ => ?_
    ext s t
    have hterm : ∀ e : Fin n,
        blockOp n (α a) (fun k => (w a k : ℂ)) (uniformAttach n ρ) (s, e) (t, e)
          = ((w a e : ℝ) : ℂ) * ((n : ℂ)⁻¹ * ρ s t) := by
      intro e
      rw [blockOp_uniformAttach, if_pos rfl]
      show ((w a e : ℝ) : ℂ)
          * (ρ s t * (((n : ℂ)⁻¹ • (1 : Matrix (Fin n) (Fin n) ℂ)) e e)) = _
      rw [Matrix.smul_apply, Matrix.one_apply_eq, smul_eq_mul, mul_one]
      ring
    show ptraceAnc n (F a (uniformAttach n ρ)) s t
        = ((((n : ℝ)⁻¹ * ∑ e, w a e : ℝ) : ℂ)
            • (LinearMap.id : Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ)) ρ s t
    rw [ptraceAnc_apply, hF a,
      Finset.sum_congr rfl fun e _ => hterm e, ← Finset.sum_mul,
      LinearMap.smul_apply, LinearMap.id_apply, Matrix.smul_apply, smul_eq_mul]
    push_cast
    ring

/-- **THE COUNTERMODEL THEORY.** Quantum on the visible system, with a surplus confined to
the ancilla coherences no available preparation produces. It withholds composite unitary
control, which it is entitled to do: control richness is a property a theory may have, not
part of what it is to be one. -/
noncomputable def hiddenCoherence (A : Type*) [Fintype A] [DecidableEq A] :
    FiniteOperationalTheory A where
  avail := fun _ _ _ F => ScalarAvail F
  availExt := fun n _ _ _ F => BlockAvail n F
  avail_id := ⟨fun _ => 1, fun _ => zero_le_one, by simp, fun _ => by
    rw [Complex.ofReal_one, one_smul]⟩
  avail_coarse := by
    rintro O O' _ _ _ _ F f ⟨w, hnn, hsum, hF⟩
    refine ⟨fun a' => ∑ a ∈ Finset.univ.filter (fun a => f a = a'), w a,
      fun a' => Finset.sum_nonneg fun a _ => hnn a, by rw [sum_fibers f w, hsum], ?_⟩
    intro a'
    show (∑ j ∈ Finset.univ.filter (fun j => f j = a'), F j)
        = (((∑ a ∈ Finset.univ.filter (fun a => f a = a'), w a : ℝ) : ℂ))
            • (LinearMap.id : Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ)
    rw [Finset.sum_congr rfl fun j _ => hF j, ← Finset.sum_smul, ← Complex.ofReal_sum]
  availExt_coarse := by
    rintro n O O' _ _ _ _ F f ⟨α, w, hnn, hsum, hF⟩
    refine ⟨fun a' => ∑ a ∈ Finset.univ.filter (fun a => f a = a'), α a,
      fun a' k => ∑ a ∈ Finset.univ.filter (fun a => f a = a'), w a k,
      fun a' k => Finset.sum_nonneg fun a _ => hnn a k,
      fun k => by rw [sum_fibers f (fun a => w a k)]; exact hsum k, ?_⟩
    intro a'
    have hγ : (fun k => (((∑ a ∈ Finset.univ.filter (fun a => f a = a'), w a k : ℝ)) : ℂ))
        = fun k => ∑ a ∈ Finset.univ.filter (fun a => f a = a'), ((w a k : ℝ) : ℂ) := by
      funext k
      rw [Complex.ofReal_sum]
    show (∑ j ∈ Finset.univ.filter (fun j => f j = a'), F j)
        = blockOp n (∑ a ∈ Finset.univ.filter (fun a => f a = a'), α a)
            (fun k => (((∑ a ∈ Finset.univ.filter (fun a => f a = a'), w a k : ℝ)) : ℂ))
    rw [Finset.sum_congr rfl fun j _ => hF j, blockOp_sum, hγ]
  availExt_bind := by
    rintro n O O' _ _ _ _ F G ⟨α, w, hnn, hsum, hF⟩ hG
    choose β v hvnn hvsum hGeq using hG
    refine ⟨fun c => β c.1 c.2 * α c.1, fun c k => v c.1 c.2 k * w c.1 k,
      fun c k => mul_nonneg (hvnn c.1 c.2 k) (hnn c.1 k), ?_, ?_⟩
    · intro k
      have step : ∀ a : O, ∑ b : O', v a b k * w a k = w a k := by
        intro a
        rw [← Finset.sum_mul, hvsum a k, one_mul]
      show ∑ c : O × O', v c.1 c.2 k * w c.1 k = 1
      rw [Fintype.sum_prod_type, Finset.sum_congr rfl fun a _ => step a]
      exact hsum k
    · intro c
      have h1 : F c.1 = blockOp n (α c.1) (fun k => ((w c.1 k : ℝ) : ℂ)) := hF c.1
      have h2 : G c.1 c.2 = blockOp n (β c.1 c.2) (fun k => ((v c.1 c.2 k : ℝ) : ℂ)) :=
        hGeq c.1 c.2
      have hγ : (fun k => ((v c.1 c.2 k : ℝ) : ℂ) * ((w c.1 k : ℝ) : ℂ))
          = fun k => (((v c.1 c.2 k * w c.1 k : ℝ)) : ℂ) := by
        funext k
        rw [Complex.ofReal_mul]
      show (G c.1 c.2).comp (F c.1)
          = blockOp n (β c.1 c.2 * α c.1)
              (fun k => (((v c.1 c.2 k * w c.1 k : ℝ)) : ℂ))
      rw [h1, h2, blockOp_comp, hγ]
  prepAvail := fun n P => SeedAvail n P
  prepAvail_uniform := fun n => ⟨n.succ_pos, rfl⟩
  prepAvail_post := by
    rintro n P Φ ⟨hn, rfl⟩ ⟨α, w, hnn, hsum, hΦ⟩
    refine ⟨hn, ?_⟩
    have hw : ∀ k, w () k = 1 := fun k => by
      have h := hsum k
      rwa [Fintype.sum_unique] at h
    have hΦ' : Φ = blockOp n (α ()) (fun k => ((w () k : ℝ) : ℂ)) := hΦ ()
    refine LinearMap.ext fun ρ => ?_
    ext p q
    show Φ (uniformAttach n ρ) p q = uniformAttach n ρ p q
    rw [hΦ', blockOp_uniformAttach]
    by_cases h : p.2 = q.2
    · rw [if_pos h, hw p.2, Complex.ofReal_one, one_mul]
    · rw [if_neg h, zero_mul, uniformAttach_offDiag n ρ p q h]
  readout := fun _ k => localLuders k
  readout_avail := by
    intro n
    refine ⟨fun _ => 0, fun a k => if a = k then 1 else 0, fun a k => ?_, fun k => ?_,
      fun a => ?_⟩
    · show (0 : ℝ) ≤ if a = k then 1 else 0
      split <;> norm_num
    · show ∑ a : Fin n, (if a = k then (1 : ℝ) else 0) = 1
      simp
    · have hγ : (fun j => (if a = j then (1 : ℂ) else 0))
          = fun k => (((if a = k then (1 : ℝ) else 0) : ℝ) : ℂ) := by
        funext j
        by_cases h : a = j
        · rw [if_pos h, if_pos h, Complex.ofReal_one]
        · rw [if_neg h, if_neg h, Complex.ofReal_zero]
      show localLuders a
          = blockOp n 0 (fun k => (((if a = k then (1 : ℝ) else 0) : ℝ) : ℂ))
      rw [localLuders_eq_blockOp, hγ]
  readout_local := fun _ k => localLuders_mapSpectatorIndependent k
  prepAvail_discard := by
    rintro n P O _ _ F ⟨hn, rfl⟩ hFa
    exact discard_uniform_scalarAvail hn hFa

/-- **THE THEORY IS SOUND ON THE SYSTEM.** -/
theorem hiddenCoherence_krausSound : KrausSound (hiddenCoherence A) := fun _ _ hF =>
  (isKrausFamily_iff _).mp (scalarAvail_isKraus hF)

/-- **THE STRONGER COUNTERMODEL.** The same theory with the system sector made COMPLETE:
`avail` is now every finite endomorphic Kraus family, so exactly the quantum instruments are
available on the system. Only one field changes and only three need reproving, because
`avail` occurs in exactly those three types. -/
noncomputable def hiddenCoherenceFull (A : Type*) [Fintype A] [DecidableEq A] :
    FiniteOperationalTheory A :=
  { hiddenCoherence A with
    avail := fun _ _ _ F => CompositeSoundness.IsKrausFamily F
    avail_id := scalarAvail_isKraus
      ⟨fun _ => 1, fun _ => zero_le_one, by simp, fun _ => by
        rw [Complex.ofReal_one, one_smul]⟩
    avail_coarse := by
      rintro O O' _ _ _ _ F f hF
      exact isKrausFamily_coarse hF f
    prepAvail_discard := by
      rintro n P O _ _ F ⟨hn, rfl⟩ hFa
      exact scalarAvail_isKraus (discard_uniform_scalarAvail hn hFa) }

/-- **THE SYSTEM SECTOR IS EXACTLY QUANTUM.** Available ⟺ Kraus-representable, on the nose:
this theory is not merely sound on the system, it has every finite endomorphic quantum
instrument and nothing else. -/
theorem hiddenCoherenceFull_exact :
    ExactFiniteEndomorphicQuantumOps (hiddenCoherenceFull A) := fun _ F =>
  isKrausFamily_iff F

/-! ### Section C — the witness -/

/-- **THE SURPLUS.** Leaves every ancilla-diagonal block alone and DOUBLES every ancilla
coherence. -/
def badOp (n : ℕ) :
    Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ :=
  blockOp n 2 (fun _ => 1)

omit [Fintype A] [DecidableEq A] in
/-- It is available: its block weights are the constant one, which sums to one over the
one-element outcome set. -/
theorem badOp_availExt (n : ℕ) : BlockAvail (A := A) n (fun _ : Unit => badOp n) := by
  refine ⟨fun _ => 2, fun _ _ => 1, fun _ _ => zero_le_one, fun k => by simp, fun a => ?_⟩
  have hγ : (fun _ : Fin n => (((1 : ℝ)) : ℂ)) = fun _ : Fin n => (1 : ℂ) := by
    funext k
    rw [Complex.ofReal_one]
  show badOp n = blockOp n 2 (fun _ => (((1 : ℝ)) : ℂ))
  rw [hγ, badOp]

/-- **AND IT IS OPERATIONALLY INVISIBLE.** Through the only preparation the theory grants,
the surplus is the identity on the system, on the nose. This is why round twenty-seven's
exposure principle never fires: its hypothesis is a violation on the REACHABLE state, and
there is none. -/
theorem badOp_invisible (n : ℕ) (hn : 0 < n) :
    discardWith n (uniformAttach n) (badOp (A := A) n) = LinearMap.id := by
  have hn' : (n : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr hn.ne'
  refine LinearMap.ext fun ρ => ?_
  ext s t
  have hterm : ∀ e : Fin n, badOp (A := A) n (uniformAttach n ρ) (s, e) (t, e)
      = (n : ℂ)⁻¹ * ρ s t := by
    intro e
    rw [badOp, blockOp_uniformAttach, if_pos rfl]
    show (1 : ℂ) * (ρ s t * (((n : ℂ)⁻¹ • (1 : Matrix (Fin n) (Fin n) ℂ)) e e)) = _
    rw [Matrix.smul_apply, Matrix.one_apply_eq, smul_eq_mul, mul_one, one_mul]
    ring
  show ptraceAnc n (badOp n (uniformAttach n ρ)) s t
      = (LinearMap.id : Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ) ρ s t
  rw [ptraceAnc_apply, Finset.sum_congr rfl fun e _ => hterm e, Finset.sum_const,
    Finset.card_univ, Fintype.card_fin, nsmul_eq_mul, ← mul_assoc, mul_inv_cancel₀ hn',
    one_mul, LinearMap.id_apply]

omit [Fintype A] in
/-- The Choi entries of the surplus: `1` on a matched ancilla-diagonal pair, `2` on a
matched coherence pair, `0` off the matched pairs. -/
theorem badOp_choi (n : ℕ) (P Q : (A × Fin n) × (A × Fin n)) :
    choiMatrix (badOp (A := A) n) P Q
      = (if P.2.2 = Q.2.2 then 1 else 2) * (if P.1 = P.2 ∧ Q.1 = Q.2 then 1 else 0) := by
  show badOp n (Matrix.single P.1 Q.1 1) P.2 Q.2 = _
  rw [badOp, blockOp_apply, single_entry]

/-- **THE SURPLUS IS NOT COMPLETELY POSITIVE.** Its Choi matrix takes the value `-2` on
`e_{((s,k₀),(s,k₀))} - e_{((s,k₁),(s,k₁))}`: the matched diagonal entries are `1` and the
matched cross terms are `2`, so the form is `1 - 2 - 2 + 1`. Two distinct ancilla levels and
one system level are all it takes. -/
theorem badOp_not_cp (n : ℕ) (s : A) {k₀ k₁ : Fin n} (hk : k₀ ≠ k₁) :
    ¬ IsCompletelyPositive (badOp (A := A) n) := by
  intro h
  have hq := h.dotProduct_mulVec_nonneg
    ((Pi.single (((s, k₀), (s, k₀)) : (A × Fin n) × (A × Fin n)) 1 :
        (A × Fin n) × (A × Fin n) → ℂ)
      - (Pi.single (((s, k₁), (s, k₁)) : (A × Fin n) × (A × Fin n)) 1 :
        (A × Fin n) × (A × Fin n) → ℂ))
  have e1 : choiMatrix (badOp (A := A) n) ((s, k₀), (s, k₀)) ((s, k₀), (s, k₀)) = 1 := by
    rw [badOp_choi, if_pos rfl, if_pos ⟨rfl, rfl⟩, mul_one]
  have e2 : choiMatrix (badOp (A := A) n) ((s, k₀), (s, k₀)) ((s, k₁), (s, k₁)) = 2 := by
    rw [badOp_choi, if_neg hk, if_pos ⟨rfl, rfl⟩, mul_one]
  have e3 : choiMatrix (badOp (A := A) n) ((s, k₁), (s, k₁)) ((s, k₀), (s, k₀)) = 2 := by
    rw [badOp_choi, if_neg (Ne.symm hk), if_pos ⟨rfl, rfl⟩, mul_one]
  have e4 : choiMatrix (badOp (A := A) n) ((s, k₁), (s, k₁)) ((s, k₁), (s, k₁)) = 1 := by
    rw [badOp_choi, if_pos rfl, if_pos ⟨rfl, rfl⟩, mul_one]
  rw [form_of_two_singles, e1, e2, e3, e4,
    show (1 : ℂ) - 2 - 2 + 1 = -2 from by ring, Complex.le_def] at hq
  norm_num at hq

/-- Hence not a Kraus family, by round twenty-seven's easy direction. -/
theorem badOp_not_kraus (n : ℕ) (s : A) {k₀ k₁ : Fin n} (hk : k₀ ≠ k₁) :
    ¬ CompositeSoundness.IsKrausFamily (fun _ : Unit => badOp (A := A) n) := fun h =>
  badOp_not_cp n s hk (krausFamily_cp h ())

/-- **THE THEORY IS NOT SOUND ON THE COMPOSITES.** -/
theorem hiddenCoherence_not_krausSoundExt [Nonempty A] :
    ¬ KrausSoundExt (hiddenCoherence A) := by
  intro h
  obtain ⟨s⟩ := ‹Nonempty A›
  exact badOp_not_kraus 2 s (show (0 : Fin 2) ≠ 1 by decide)
    (h 2 Unit (fun _ => badOp 2) (badOp_availExt 2))

/-- **THE FORK, SETTLED.** Exact quantum operations on the visible system do NOT force exact
quantum operations on the composites. The separation is real, so composite exactness is a
distinct axis and has to be asked for rather than assumed. -/
theorem krausSound_not_implies_krausSoundExt (A : Type*) [Fintype A] [DecidableEq A]
    [Nonempty A] :
    ∃ T : FiniteOperationalTheory A, KrausSound T ∧ ¬ KrausSoundExt T :=
  ⟨hiddenCoherence A, hiddenCoherence_krausSound, hiddenCoherence_not_krausSoundExt⟩

/-- **THE FULL THEORY IS STILL NOT SOUND ON THE COMPOSITES.** Its `availExt` is the same one,
so the same witness works — but now the antecedent is exactness, not mere soundness. -/
theorem hiddenCoherenceFull_not_krausSoundExt [Nonempty A] :
    ¬ KrausSoundExt (hiddenCoherenceFull A) := by
  intro h
  obtain ⟨s⟩ := ‹Nonempty A›
  exact badOp_not_kraus 2 s (show (0 : Fin 2) ≠ 1 by decide)
    (h 2 Unit (fun _ => badOp 2) (badOp_availExt 2))

/-- **THE SEPARATION THAT ACTUALLY MATTERS.** A theory with EXACTLY the finite endomorphic
quantum instruments on the system — available ⟺ Kraus-representable — still carrying a
non-quantum composite operation. Exact system QM does not force composite soundness, so
"exact on the system" and "exact on the composites" are genuinely different statements and
the second has to be asked for. -/
theorem exact_not_implies_krausSoundExt (A : Type*) [Fintype A] [DecidableEq A]
    [Nonempty A] :
    ∃ T : FiniteOperationalTheory A,
      ExactFiniteEndomorphicQuantumOps T ∧ ¬ KrausSoundExt T :=
  ⟨hiddenCoherenceFull A, hiddenCoherenceFull_exact, hiddenCoherenceFull_not_krausSoundExt⟩

#print axioms blockOp_one
#print axioms blockOp_comp
#print axioms blockOp_sum
#print axioms localLuders_eq_blockOp
#print axioms uniformAttach_offDiag
#print axioms blockOp_uniformAttach
#print axioms sum_fibers
#print axioms scalarAvail_isKraus
#print axioms hiddenCoherence_krausSound
#print axioms badOp_availExt
#print axioms badOp_invisible
#print axioms badOp_choi
#print axioms badOp_not_cp
#print axioms badOp_not_kraus
#print axioms hiddenCoherence_not_krausSoundExt
#print axioms isKrausFamily_coarse
#print axioms discard_uniform_scalarAvail
#print axioms hiddenCoherenceFull_exact
#print axioms krausSound_not_implies_krausSoundExt
#print axioms hiddenCoherenceFull_not_krausSoundExt
#print axioms exact_not_implies_krausSoundExt

end HiddenCoherence
end OIBridge
