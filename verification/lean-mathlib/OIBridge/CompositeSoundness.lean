/-
  OIBridge/CompositeSoundness.lean — the composite-soundness audit: what system-level
  soundness forces on the ancilla-extended sector, and what it does not.

  PHASE THREE, ROUND TWENTY-SEVEN. Round twenty-six proves exactness for the base system's
  `avail`. It says nothing directly about `availExt n` on `A × Fin n`. So the endpoint it
  defines is

      exact finite endomorphic QM ON THE SYSTEM `A`,

  and NOT yet

      the entire system+ancilla operational theory is exactly finite QM.

  That is not a defect in round twenty-six — the theorem says exactly what its definition
  says — but it decides the eventual headline, so this file settles what can be settled.

  §A — THE PREDICATE AT ANY OUTCOME TYPE, and the extended soundness notion.
  `IsKrausFamily` is round twenty-six's representation predicate with the outcome type left
  free, so it can be asked of a composite family; `isKrausFamily_iff` pins it to
  `IsFiniteEndomorphicKrausInstrument` at `Fin m`, so nothing forks. `KrausSoundExt` is the
  composite analogue of `KrausSound`.

  §B — WHAT SYSTEM SOUNDNESS FORCES, FOR FREE. The closure rules already do work:
  `prepAvail_discard` says an available preparation followed by an available composite
  instrument followed by discard is an available SYSTEM instrument, so

      ┌────────────────────────────────────────────────────────────────────┐
      │  `krausSound_exposedComposite`:  system soundness ⟹ every composite  │
      │  process visible through an admissible prepare–operate–discard      │
      │  context has a Kraus representation ON `A`.                         │
      └────────────────────────────────────────────────────────────────────┘

  §C — WHICH SURPLUS STRUCTURE THAT RULES OUT. `discardWith_trace` — discard preserves the
  trace exactly — turns round twenty-six's trace identity into an exposure principle:
  `traceWitness_always_exposed` shows a composite family whose aggregate output trace
  differs from the input's is exposed at EVERY available preparation. So a trace-based
  witness can never hide in the composite sector, and any genuine surplus structure must be
  TRACE-CONSISTENT AND DISCARD-INVISIBLE. That is a sharp constraint on the countermodel
  search, and it is why the cheap candidates do not work.

  §D — THE SECOND REFUTATION TOOL, and the transpose. Round twenty-six had only the trace
  identity, which cannot refute transposition. The EASY direction of the Kraus–CP
  correspondence supplies the missing tool: `conjChannel_cp` and `krausFamily_cp` show every
  Kraus branch is completely positive, by exhibiting the Choi matrix as a sum of
  `vecMulVec w (star w)` terms. NOTE THE DIRECTION — this is Kraus ⟹ CP, which is a
  computation; the converse is the one that needs PSD factorization, and it is NOT used
  here, so the external boundary is untouched. `transposeMap_not_kraus` then retires the
  caveat: transposition is trace-preserving and NOT completely positive, so it is a
  non-quantum operation that the trace test misses and this test catches.
  `exposedComposite_cp` records the consequence for §B.

  WHAT THIS ROUND DOES NOT SETTLE, stated plainly rather than left to inference:
  whether `KrausSound T` implies `KrausSoundExt T`. Neither direction is asserted. §C shows
  why the obvious countermodels fail — a surplus composite operation must be invisible after
  discard at every available preparation, which kills every trace-based witness — and the
  shape a real countermodel must have is now visible: a trace-preserving, non-CP composite
  map whose surplus lives entirely in the ancilla coherences the discard annihilates, in a
  theory whose `availExt` is closed under `availExt_bind` without exposing it. Building that
  is a round of its own, and nothing here claims it exists or that it does not.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.KrausSoundness

namespace OIBridge
namespace CompositeSoundness

open Complex Matrix CoherentExtension MonoidalCompletion
open OperationalAssembly StinespringAssembly KrausSoundness

local notation "conj'" => (starRingEnd ℂ)

open scoped ComplexOrder

variable {A : Type*} [Fintype A] [DecidableEq A]

/-! ### Section A — the predicate at any outcome type -/

/-- **THE REPRESENTATION PREDICATE, OUTCOME TYPE FREE.** Round twenty-six's predicate with
the outcome type unfixed, so it can be asked of a family on the composite carrier. Still an
existential over a normalized square Kraus representation: no CP/Choi classification, and
so no external analytic fact. -/
def IsKrausFamily {S O : Type*} [Fintype S] [DecidableEq S] [Fintype O] [DecidableEq O]
    (F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  ∃ (n : ℕ) (K : Fin (n + 1) → Matrix S S ℂ) (out : Fin (n + 1) → O),
    (∑ k, (K k)ᴴ * K k = 1) ∧
      ∀ a, F a = ∑ k ∈ Finset.univ.filter (fun k => out k = a), conjChannel (K k)

/-- **NOTHING FORKS.** At `Fin m` the free-outcome predicate is round twenty-six's, so the
composite notion is a generalization and not a second definition. -/
theorem isKrausFamily_iff {m : ℕ} (F : Fin m → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ) :
    IsKrausFamily F ↔ IsFiniteEndomorphicKrausInstrument F := by
  constructor
  · rintro ⟨n, K, out, hnorm, hF⟩
    exact ⟨n, K, out, hnorm, funext hF⟩
  · rintro ⟨n, K, out, hnorm, rfl⟩
    exact ⟨n, K, out, hnorm, fun _ => rfl⟩

/-- **COMPOSITE SOUNDNESS.** Every available family on every ancilla extension has a
normalized Kraus representation ON THE COMPOSITE CARRIER. This is strictly stronger than
`KrausSound`, which constrains only the system sector. -/
def KrausSoundExt (T : FiniteOperationalTheory A) : Prop :=
  ∀ (n : ℕ) (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ),
    T.availExt n O F → IsKrausFamily F

/-! ### Section B — what system soundness forces, for free -/

/-- **SYSTEM SOUNDNESS REACHES INTO THE COMPOSITE SECTOR.** An available preparation,
followed by an available composite instrument, followed by discard, is an available SYSTEM
instrument by `prepAvail_discard` — so soundness forces every composite process visible
through an admissible prepare–operate–discard context to have a Kraus representation on `A`.
No new hypothesis: the closure rules already carry it. -/
theorem krausSound_exposedComposite (T : FiniteOperationalTheory A) (hsound : KrausSound T)
    (n m : ℕ) (P : Matrix A A ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (hP : T.prepAvail n P)
    (F : Fin m → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (hF : T.availExt n (Fin m) F) :
    IsFiniteEndomorphicKrausInstrument (fun a => discardWith n P (F a)) :=
  hsound m _ (T.prepAvail_discard n P (Fin m) F hP hF)

/-! ### Section C — which surplus structure that rules out -/

omit [DecidableEq A] in
/-- The partial trace over the ancilla preserves the trace. -/
theorem ptraceAnc_trace (n : ℕ) (M : Matrix (A × Fin n) (A × Fin n) ℂ) :
    (ptraceAnc n M).trace = M.trace := by
  rw [Matrix.trace, Matrix.trace, Fintype.sum_prod_type]
  exact Finset.sum_congr rfl fun s _ => rfl

omit [DecidableEq A] in
/-- **DISCARD IS TRACE-TRANSPARENT.** Forgetting the ancilla changes no trace, so whatever
a composite operation does to the trace is visible on the system. -/
theorem discardWith_trace (n : ℕ)
    (P : Matrix A A ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (Φ : Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (ρ : Matrix A A ℂ) : ((discardWith n P Φ) ρ).trace = (Φ (P ρ)).trace :=
  ptraceAnc_trace n _

/-- A family that does not conserve the trace in the aggregate has no Kraus
representation — round twenty-six's identity, contrapositive. -/
theorem not_kraus_of_trace_ne {m : ℕ} (G : Fin m → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ)
    (ρ : Matrix A A ℂ) (h : ∑ a, ((G a) ρ).trace ≠ ρ.trace) :
    ¬ IsFiniteEndomorphicKrausInstrument G := by
  rintro ⟨n, K, out, hnorm, rfl⟩
  exact h (instrumentBranch_trace K out hnorm ρ)

/-- **A TRACE-BASED WITNESS CAN NEVER HIDE IN THE COMPOSITE SECTOR.** If a composite family
fails aggregate trace conservation as seen through a preparation, then the discarded family
fails it on the system, so system soundness already excludes it. Hence any genuine surplus
composite structure must be TRACE-CONSISTENT and DISCARD-INVISIBLE — which is exactly why
the cheap countermodels to `KrausSound ⟹ KrausSoundExt` do not work. -/
theorem traceWitness_always_exposed (n m : ℕ)
    (P : Matrix A A ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (F : Fin m → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (ρ : Matrix A A ℂ) (h : ∑ a, ((F a) (P ρ)).trace ≠ ρ.trace) :
    ¬ IsFiniteEndomorphicKrausInstrument (fun a => discardWith n P (F a)) := by
  refine not_kraus_of_trace_ne _ ρ ?_
  rwa [Finset.sum_congr rfl fun a _ => discardWith_trace n P (F a) ρ]

/-! ### Section D — the second refutation tool, and the transpose -/

omit [Fintype A] [DecidableEq A] in
/-- A finite sum of positive semidefinite matrices is positive semidefinite. -/
theorem posSemidef_sum {S ι' : Type*} [Fintype S] (s : Finset ι') (M : ι' → Matrix S S ℂ)
    (h : ∀ i ∈ s, (M i).PosSemidef) : (∑ i ∈ s, M i).PosSemidef := by
  classical
  induction s using Finset.induction with
  | empty =>
      rw [Finset.sum_empty]
      exact Matrix.PosSemidef.zero
  | insert x s hx ih =>
      rw [Finset.sum_insert hx]
      exact (h x (Finset.mem_insert_self x s)).add
        (ih fun i hi => h i (Finset.mem_insert_of_mem hi))

omit [Fintype A] [DecidableEq A] in
/-- The Choi matrix is additive in the map, at any carrier. -/
theorem choiMatrix_finsum {S ι' : Type*} [Fintype S] [DecidableEq S] (s : Finset ι')
    (Φ : ι' → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) :
    choiMatrix (∑ i ∈ s, Φ i) = ∑ i ∈ s, choiMatrix (Φ i) := by
  ext p q
  simp [choiMatrix, LinearMap.sum_apply, Matrix.sum_apply]

omit [Fintype A] [DecidableEq A] in
/-- **CONJUGATION IS COMPLETELY POSITIVE**, by exhibiting its Choi matrix as
`vecMulVec w (star w)` with `w (s, a) = V a s`. A computation, not a classification. -/
theorem conjChannel_cp {S : Type*} [Fintype S] [DecidableEq S] (V : Matrix S S ℂ) :
    IsCompletelyPositive (conjChannel V) := by
  have hentry : choiMatrix (conjChannel V)
      = Matrix.vecMulVec (fun p : S × S => V p.2 p.1)
          (star fun p : S × S => V p.2 p.1) := by
    ext p q
    show ((V * Matrix.single p.1 q.1 1 * Vᴴ : Matrix S S ℂ)) p.2 q.2 = _
    rw [Matrix.mul_assoc, Matrix.mul_apply, Finset.sum_eq_single p.1]
    · rw [Matrix.mul_apply, Finset.sum_eq_single q.1]
      · rw [single_entry, if_pos ⟨rfl, rfl⟩, one_mul, Matrix.conjTranspose_apply]
        rfl
      · intro y _ hy
        rw [single_entry, if_neg (fun hh => hy hh.2.symm), zero_mul]
      · intro hc
        exact absurd (Finset.mem_univ _) hc
    · intro x _ hx
      rw [Matrix.mul_apply, Finset.sum_eq_zero fun y _ => by
        rw [single_entry, if_neg (fun hh => hx hh.1.symm), zero_mul], mul_zero]
    · intro hc
      exact absurd (Finset.mem_univ _) hc
  show (choiMatrix (conjChannel V)).PosSemidef
  rw [hentry]
  exact Matrix.posSemidef_vecMulVec_self_star _

omit [Fintype A] [DecidableEq A] in
/-- **EVERY KRAUS BRANCH IS COMPLETELY POSITIVE.** The EASY direction of the Kraus–CP
correspondence: a branch is a finite sum of conjugations, and complete positivity is closed
under sums. The converse — CP gives a Kraus family — is the direction that needs PSD
factorization, and it is NOT used anywhere in this file, so the external boundary is
untouched. -/
theorem krausFamily_cp {S O : Type*} [Fintype S] [DecidableEq S] [Fintype O]
    [DecidableEq O] {F : O → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ} (h : IsKrausFamily F)
    (a : O) : IsCompletelyPositive (F a) := by
  obtain ⟨n, K, out, _, hF⟩ := h
  show (choiMatrix (F a)).PosSemidef
  rw [hF a, choiMatrix_finsum]
  exact posSemidef_sum _ _ fun k _ => conjChannel_cp (K k)

/-- **EVERY OPERATIONALLY EXPOSED COMPOSITE PROCESS IS COMPLETELY POSITIVE.** §B plus the
tool above: in a system-sound theory, the prepare–operate–discard reading of any available
composite instrument is CP on the system. -/
theorem exposedComposite_cp (T : FiniteOperationalTheory A) (hsound : KrausSound T)
    (n m : ℕ) (P : Matrix A A ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (hP : T.prepAvail n P)
    (F : Fin m → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (hF : T.availExt n (Fin m) F) (a : Fin m) :
    IsCompletelyPositive (discardWith n P (F a)) :=
  krausFamily_cp ((isKrausFamily_iff _).mpr
    (krausSound_exposedComposite T hsound n m P hP F hF)) a

/-- Transposition, as a linear map on the matrix algebra. -/
def transposeMap (S : Type*) [Fintype S] [DecidableEq S] :
    Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ where
  toFun X := Xᵀ
  map_add' _ _ := Matrix.transpose_add _ _
  map_smul' _ _ := Matrix.transpose_smul _ _

omit [Fintype A] [DecidableEq A] in
/-- **THE TRACE TEST IS BLIND TO IT.** Transposition preserves the trace exactly, so round
twenty-six's identity cannot refute it — which is why the trace amplifier, and not the
transpose, was the witness there. -/
theorem transposeMap_trace {S : Type*} [Fintype S] [DecidableEq S] (X : Matrix S S ℂ) :
    ((transposeMap S) X).trace = X.trace :=
  Matrix.trace_transpose X

omit [Fintype A] [DecidableEq A] in
/-- The quadratic form of a matrix at a difference of two basis directions, expanded into
its four entries. Proved by evaluating both sums at the supported indices rather than by a
`simp` normal form, so it does not depend on which `Pi.single` lemmas are in scope. -/
theorem form_of_two_singles {ι' : Type*} [Fintype ι'] [DecidableEq ι']
    (C : Matrix ι' ι' ℂ) (p q : ι') :
    star ((Pi.single p 1 : ι' → ℂ) - (Pi.single q 1 : ι' → ℂ)) ⬝ᵥ
        C.mulVec ((Pi.single p 1 : ι' → ℂ) - (Pi.single q 1 : ι' → ℂ))
      = C p p - C p q - C q p + C q q := by
  set v : ι' → ℂ := (Pi.single p 1 : ι' → ℂ) - (Pi.single q 1 : ι' → ℂ) with hvdef
  have hvi : ∀ i, v i = (if i = p then (1 : ℂ) else 0) - (if i = q then (1 : ℂ) else 0) := by
    intro i
    rw [hvdef]
    show (Pi.single p 1 : ι' → ℂ) i - (Pi.single q 1 : ι' → ℂ) i = _
    rw [Pi.single_apply, Pi.single_apply]
  have hstar : ∀ i, star (v i) = v i := by
    intro i
    rw [hvi i]
    by_cases h1 : i = p <;> by_cases h2 : i = q <;> simp [h1, h2]
  have hsel : ∀ f : ι' → ℂ, ∑ i, v i * f i = f p - f q := by
    intro f
    have hterm : ∀ i : ι', v i * f i
        = (if i = p then f i else 0) - (if i = q then f i else 0) := by
      intro i
      rw [hvi i, sub_mul]
      split_ifs <;> ring
    rw [Finset.sum_congr rfl fun i _ => hterm i, Finset.sum_sub_distrib,
      Finset.sum_ite_eq' Finset.univ p f, Finset.sum_ite_eq' Finset.univ q f,
      if_pos (Finset.mem_univ p), if_pos (Finset.mem_univ q)]
  have hmv : ∀ i, C.mulVec v i = C i p - C i q := by
    intro i
    show ∑ j, C i j * v j = _
    have hterm : ∀ j : ι', C i j * v j
        = (if j = p then C i j else 0) - (if j = q then C i j else 0) := by
      intro j
      rw [hvi j, mul_sub]
      split_ifs <;> ring
    rw [Finset.sum_congr rfl fun j _ => hterm j, Finset.sum_sub_distrib,
      Finset.sum_ite_eq' Finset.univ p (fun j => C i j),
      Finset.sum_ite_eq' Finset.univ q (fun j => C i j),
      if_pos (Finset.mem_univ p), if_pos (Finset.mem_univ q)]
  have hd : star v ⬝ᵥ C.mulVec v = ∑ i, v i * (C i p - C i q) :=
    Finset.sum_congr rfl fun i _ => by rw [Pi.star_apply, hstar i, hmv i]
  rw [hd, hsel (fun i => C i p - C i q)]
  ring

omit [Fintype A] [DecidableEq A] in
/-- **BUT POSITIVITY IS NOT.** The Choi matrix of transposition is the swap, and the
direction `e_{(a,b)} - e_{(b,a)}` gives `-2`. Two distinct indices are all that is needed,
so this refutes transposition on every carrier with at least two levels. -/
theorem transposeMap_not_cp {S : Type*} [Fintype S] [DecidableEq S] {a b : S}
    (hab : a ≠ b) : ¬ IsCompletelyPositive (transposeMap S) := by
  intro h
  have hentry : ∀ p q : S × S,
      choiMatrix (transposeMap S) p q = if p.1 = q.2 ∧ q.1 = p.2 then 1 else 0 := by
    intro p q
    show ((Matrix.single p.1 q.1 (1 : ℂ))ᵀ : Matrix S S ℂ) p.2 q.2 = _
    rw [Matrix.transpose_apply, single_entry]
  have hq := h.dotProduct_mulVec_nonneg ((Pi.single ((a, b) : S × S) 1 : S × S → ℂ)
      - (Pi.single ((b, a) : S × S) 1 : S × S → ℂ))
  have e1 : choiMatrix (transposeMap S) ((a, b) : S × S) ((a, b) : S × S) = 0 := by
    rw [hentry]
    exact if_neg fun hh => hab hh.1
  have e2 : choiMatrix (transposeMap S) ((a, b) : S × S) ((b, a) : S × S) = 1 := by
    rw [hentry]
    exact if_pos ⟨rfl, rfl⟩
  have e3 : choiMatrix (transposeMap S) ((b, a) : S × S) ((a, b) : S × S) = 1 := by
    rw [hentry]
    exact if_pos ⟨rfl, rfl⟩
  have e4 : choiMatrix (transposeMap S) ((b, a) : S × S) ((b, a) : S × S) = 0 := by
    rw [hentry]
    exact if_neg fun hh => hab hh.1.symm
  rw [form_of_two_singles, e1, e2, e3, e4] at hq
  rw [show (0 : ℂ) - 1 - 1 + 0 = -2 from by ring] at hq
  rw [Complex.le_def] at hq
  norm_num at hq

omit [Fintype A] [DecidableEq A] in
/-- **THE TRANSPOSE IS NOT A QUANTUM OPERATION**, and now the kernel says so. It is
trace-preserving, so round twenty-six's identity misses it; it is not completely positive,
so the Kraus ⟹ CP direction catches it. Two independent refutation tools, and neither
consumes an external analytic fact. -/
theorem transposeMap_not_kraus {S : Type*} [Fintype S] [DecidableEq S] {a b : S}
    (hab : a ≠ b) : ¬ IsKrausFamily (fun _ : Fin 1 => transposeMap S) := fun h =>
  transposeMap_not_cp hab (krausFamily_cp h 0)

#print axioms isKrausFamily_iff
#print axioms krausSound_exposedComposite
#print axioms ptraceAnc_trace
#print axioms discardWith_trace
#print axioms not_kraus_of_trace_ne
#print axioms traceWitness_always_exposed
#print axioms posSemidef_sum
#print axioms choiMatrix_finsum
#print axioms conjChannel_cp
#print axioms krausFamily_cp
#print axioms exposedComposite_cp
#print axioms transposeMap_trace
#print axioms form_of_two_singles
#print axioms transposeMap_not_cp
#print axioms transposeMap_not_kraus

end CompositeSoundness
end OIBridge
