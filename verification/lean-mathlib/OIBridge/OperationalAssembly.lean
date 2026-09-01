/-
  OIBridge/OperationalAssembly.lean — map-level spectator independence, the local Lüders
  selector, independent product preparation, and the common operational structure.

  PHASE THREE, ROUND TWENTY-FIVE (opening items). Round twenty-four's `H_comp` is still a
  REVERSIBLE-operation compositionality principle: its spectator clause is formulated for
  `Equiv.Perm` actions completed by round-seventeen correlation extensions. A Lüders
  selector is not reversible, so that clause cannot by itself deliver `id_S ⊗ ℒ_k` at the
  output of a Stinespring dilation. This file supplies the generic notion the assembly
  actually needs, and keeps three physically distinct ideas apart that it would be easy to
  conflate.

  §A — MAP-LEVEL SPECTATOR INDEPENDENCE. `MapSpectatorIndependent Φ_B Φ_AB` says
  `Φ_AB(X_A ⊗ X_B) = X_A ⊗ Φ_B(X_B)` for ARBITRARY linear maps — no reversibility, no
  correlation-extension form. Round twenty-four's `SpectatorIndependent` is exactly this
  condition for correlation-extension channels (`spectatorIndependent_iff_mapLevel`), so
  the reversible principle becomes a specialization rather than needing to be rewritten.

  §B — THE LOCAL LÜDERS SELECTOR, and where the freedom lives.

      ┌────────────────────────────────────────────────────────────────────┐
      │  `mapSpectatorIndependent_iff_localLuders`:                         │
      │  a composite map is map-spectator-independent over `ℒ_k`  ⟺         │
      │  it IS `id_A ⊗ ℒ_k`.                                                │
      └────────────────────────────────────────────────────────────────────┘

  The proof is by spanning: composite matrix units ARE product matrices
  (`tensorOf_single`), so agreement on products is agreement everywhere. Note what this
  does NOT need — complete positivity is not a hypothesis, which strengthens the result.

  The logical role of composition is then made completely transparent by exhibiting the
  freedom it kills. `blockDephase` is the within-block dephasing selector: a manifestly CP
  map (a sum of rank-one conjugations, `blockDephase_kraus`) with EXACTLY the same action
  on every classical composite state (`blockDephase_classical_eq`), yet it destroys system
  coherence (`blockDephase_ne_localLuders`) and fails map-level spectator independence
  (`blockDephase_not_mapSpectatorIndependent`). So the classical ancilla-readout condition
  alone leaves a correlation freedom across the system indices — the local form of F35 —
  and spectator independence is precisely what removes it.

  §C — INDEPENDENT PRODUCT PREPARATION, kept SEPARATE. Round twenty-one produces the pure
  ancilla `|k₀⟩⟨k₀|` from the uniform state; it does not produce the JOINT state
  `ρ_S ⊗ |k₀⟩⟨k₀|_E`. Parallel composition of OPERATIONS and parallel composition of
  independently prepared STATES are related physical ideas but they are not the same
  predicate, so `ProductPreparation` is its own clause and is not smuggled into `H_comp`.

  §D — THE COMMON OPERATIONAL STRUCTURE. Round twenty-four's `UniversalUnitaryReachability`
  and `FullFiniteInstrumentAvailability` speak through an abstract `avail`, while `HComp`
  speaks about `act`/`corr`. Those are logically disconnected objects, so no honest
  assembly can conjoin them. `FiniteOperationalCompletion` gathers the availability and
  closure rules into ONE object, and the control and richness principles become properties
  of that same structure (`HasUniversalUnitaryControl`, `HasFullFiniteInstruments`).

  SCOPE, STATED UP FRONT. Two guards that the remaining assembly must carry, recorded here
  so they cannot be lost:

    * COMPOSITE-DIMENSION CONTROL. A universal-control premise on `S` says nothing about
      unitaries on `Fin n × S`. The assembly needs control richness on the COMPOSITE
      carrier, quantified over the finite ancilla, not on the system alone.
    * ENDOMORPHIC INSTRUMENTS. The Kraus operators here are square, `S → S`. What the
      assembly will prove is therefore "all finite ENDOMORPHIC instruments on a fixed
      system `S`", not "all finite quantum instruments" without qualification — the latter
      needs rectangular Kraus maps or a dimension-changing encoding.

  WHAT IS NOT HERE. The generic normalized-Kraus Stinespring assembly, the derivation of
  full finite-instrument availability, and the structured standard-completion predicate are
  the remaining items; none is asserted. The external boundary stays exactly four items and
  no more: compact Lie integration, finite isometry extension, PSD square-root/
  factorization, and finite Uhlmann/Schmidt uniqueness.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.MonoidalCompletion

namespace OIBridge
namespace OperationalAssembly

open Complex Matrix CoherentExtension BranchSelector MonoidalCompletion

open scoped ComplexOrder

local notation "conj'" => (starRingEnd ℂ)

variable {A B : Type*} [Fintype A] [DecidableEq A] [Fintype B] [DecidableEq B]

/-! ### Section A — map-level spectator independence -/

/-- **MAP-LEVEL SPECTATOR INDEPENDENCE.** A composite map acts as `id_A ⊗ Φ_B` on every
product input. Stated for ARBITRARY linear maps: no reversibility and no
correlation-extension form is assumed, so it applies to irreversible operations — a Lüders
selector included — which the round-twenty-four clause cannot reach. -/
def MapSpectatorIndependent
    (ΦB : Matrix B B ℂ →ₗ[ℂ] Matrix B B ℂ)
    (ΦAB : Matrix (A × B) (A × B) ℂ →ₗ[ℂ] Matrix (A × B) (A × B) ℂ) : Prop :=
  ∀ (XA : Matrix A A ℂ) (XB : Matrix B B ℂ),
    ΦAB (tensorOf XA XB) = tensorOf XA (ΦB XB)

omit [Fintype A] [DecidableEq A] [Fintype B] [DecidableEq B] in
/-- **The round-twenty-four clause is the reversible specialization.** `H_comp`'s spectator
clause is exactly map-level spectator independence, instantiated at correlation-extension
channels — so the reversible principle is a special case rather than a separate idea. -/
theorem spectatorIndependent_iff_mapLevel
    (CB : Equiv.Perm B → Matrix B B ℂ)
    (C : Equiv.Perm (A × B) → Matrix (A × B) (A × B) ℂ) :
    SpectatorIndependent CB C
      ↔ ∀ g : Equiv.Perm B,
          MapSpectatorIndependent (correlationExtension g (CB g))
            (correlationExtension (spectatorExt g) (C (spectatorExt g))) :=
  Iff.rfl

/-! ### Section B — the local Lüders selector -/

omit [Fintype A] [Fintype B] in
/-- **Composite matrix units ARE product matrices.** This is what makes agreement on
products agreement everywhere. -/
theorem tensorOf_single (a a' : A) (b b' : B) :
    tensorOf (Matrix.single a a' 1) (Matrix.single b b' 1)
      = Matrix.single ((a, b) : A × B) (a', b') 1 := by
  ext p q
  rw [tensorOf_apply, single_entry, single_entry, single_entry]
  by_cases h1 : a = p.1 ∧ a' = q.1
  · by_cases h2 : b = p.2 ∧ b' = q.2
    · rw [if_pos h1, if_pos h2, one_mul,
        if_pos ⟨Prod.ext h1.1 h2.1, Prod.ext h1.2 h2.2⟩]
    · rw [if_pos h1, if_neg h2, one_mul,
        if_neg fun hh => h2 ⟨congrArg Prod.snd hh.1, congrArg Prod.snd hh.2⟩]
  · rw [if_neg h1, zero_mul,
      if_neg fun hh => h1 ⟨congrArg Prod.fst hh.1, congrArg Prod.fst hh.2⟩]

/-- **The local Lüders selector `id_A ⊗ ℒ_k`**: read the `B` factor in the fixed basis,
keep outcome `k`, and leave the `A` factor — including all of its coherence — untouched. -/
def localLuders (k : B) :
    Matrix (A × B) (A × B) ℂ →ₗ[ℂ] Matrix (A × B) (A × B) ℂ where
  toFun X := Matrix.of fun p q => if p.2 = k ∧ q.2 = k then X (p.1, k) (q.1, k) else 0
  map_add' X Y := by
    ext p q
    by_cases h : p.2 = k ∧ q.2 = k <;> simp [h]
  map_smul' c X := by
    ext p q
    by_cases h : p.2 = k ∧ q.2 = k <;> simp [h]

omit [Fintype A] [DecidableEq A] [Fintype B] in
@[simp] theorem localLuders_apply (k : B) (X : Matrix (A × B) (A × B) ℂ) (p q : A × B) :
    localLuders k X p q = if p.2 = k ∧ q.2 = k then X (p.1, k) (q.1, k) else 0 := rfl

omit [Fintype A] [DecidableEq A] [Fintype B] in
/-- The local Lüders selector really is `id_A ⊗ ℒ_k` on products. -/
theorem localLuders_tensor (k : B) (XA : Matrix A A ℂ) (XB : Matrix B B ℂ) :
    localLuders k (tensorOf XA XB) = tensorOf XA (ludersLift k XB) := by
  ext p q
  simp only [localLuders_apply, tensorOf_apply, ludersLift_apply, Matrix.smul_apply,
    smul_eq_mul, single_entry]
  by_cases h : p.2 = k ∧ q.2 = k
  · rw [if_pos h, if_pos ⟨h.1.symm, h.2.symm⟩, mul_one]
  · rw [if_neg h, if_neg fun hh => h ⟨hh.1.symm, hh.2.symm⟩]
    ring

omit [Fintype A] [DecidableEq A] [Fintype B] in
theorem localLuders_mapSpectatorIndependent (k : B) :
    MapSpectatorIndependent (ludersLift k) (localLuders (A := A) k) :=
  localLuders_tensor k

/-- Two composite maps agreeing on every matrix unit are equal. -/
theorem eq_of_agree_on_single
    (Φ Ψ : Matrix (A × B) (A × B) ℂ →ₗ[ℂ] Matrix (A × B) (A × B) ℂ)
    (h : ∀ p q : A × B, Φ (Matrix.single p q 1) = Ψ (Matrix.single p q 1)) : Φ = Ψ := by
  refine LinearMap.ext fun X => ?_
  conv_lhs => rw [Matrix.matrix_eq_sum_single X]
  conv_rhs => rw [Matrix.matrix_eq_sum_single X]
  rw [map_sum, map_sum]
  refine Finset.sum_congr rfl fun p _ => ?_
  rw [map_sum, map_sum]
  refine Finset.sum_congr rfl fun q _ => ?_
  rw [single_eq_smul, map_smul, map_smul, h]

/-- **THE LOCAL LÜDERS UNIQUENESS THEOREM.** A composite map is map-spectator-independent
over the rank-one Lüders selector EXACTLY when it is `id_A ⊗ ℒ_k`. Composite matrix units
are product matrices, so agreement on products is agreement everywhere — and note that
complete positivity is not a hypothesis anywhere, which strengthens the statement: the
ancilla readout is forced by composition alone. -/
theorem mapSpectatorIndependent_iff_localLuders (k : B)
    (Φ : Matrix (A × B) (A × B) ℂ →ₗ[ℂ] Matrix (A × B) (A × B) ℂ) :
    MapSpectatorIndependent (ludersLift k) Φ ↔ Φ = localLuders k := by
  constructor
  · intro h
    refine eq_of_agree_on_single Φ _ fun p q => ?_
    rw [← tensorOf_single p.1 q.1 p.2 q.2, h, ← localLuders_tensor,
      tensorOf_single]
  · rintro rfl
    exact localLuders_mapSpectatorIndependent k

/-! ### Where the freedom lives — the local form of F35 -/

/-- The within-block dephasing selector: it keeps ancilla outcome `k` but destroys every
system coherence. Written as a sum of rank-one Lüders branches on the composite carrier,
which is a Kraus sum, so complete positivity is immediate. -/
noncomputable def blockDephase (k : B) :
    Matrix (A × B) (A × B) ℂ →ₗ[ℂ] Matrix (A × B) (A × B) ℂ :=
  ∑ a : A, ludersLift ((a, k) : A × B)

omit [Fintype B] in
theorem blockDephase_apply (k : B) (X : Matrix (A × B) (A × B) ℂ) :
    blockDephase k X
      = ∑ a : A, X (a, k) (a, k) • Matrix.single ((a, k) : A × B) (a, k) 1 := by
  rw [blockDephase, LinearMap.sum_apply]
  exact Finset.sum_congr rfl fun a _ => ludersLift_apply _ X

omit [Fintype A] [Fintype B] in
/-- The Choi matrix is additive in the map. -/
theorem choiMatrix_sum {ι' : Type*} (s : Finset ι')
    (Φ : ι' → Matrix (A × B) (A × B) ℂ →ₗ[ℂ] Matrix (A × B) (A × B) ℂ) :
    choiMatrix (∑ i ∈ s, Φ i) = ∑ i ∈ s, choiMatrix (Φ i) := by
  ext p q
  simp [choiMatrix, LinearMap.sum_apply, Matrix.sum_apply]

/-- **The surviving freedom is a genuine channel.** `blockDephase` is a Kraus sum of
rank-one branches, hence completely positive. -/
theorem blockDephase_cp (k : B) : IsCompletelyPositive (blockDephase (A := A) k) := by
  show (choiMatrix (blockDephase (A := A) k)).PosSemidef
  rw [blockDephase, choiMatrix_sum]
  exact Finset.sum_induction _ Matrix.PosSemidef (fun _ _ h1 h2 => h1.add h2)
    Matrix.PosSemidef.zero fun a _ => ludersLift_cp _

omit [Fintype A] [DecidableEq A] [Fintype B] [DecidableEq B] in
theorem tensorOf_zero (XA : Matrix A A ℂ) : tensorOf XA (0 : Matrix B B ℂ) = 0 := by
  ext p q
  rw [tensorOf_apply]
  simp

omit [Fintype A] [Fintype B] in
theorem localLuders_classical (k : B) (a₀ : A) (b : B) :
    localLuders k (Matrix.single ((a₀, b) : A × B) (a₀, b) 1)
      = if b = k then Matrix.single ((a₀, k) : A × B) (a₀, k) 1 else 0 := by
  rw [← tensorOf_single a₀ a₀ b b, localLuders_tensor, ludersLift_apply, single_entry]
  by_cases hb : b = k
  · subst hb
    rw [if_pos ⟨rfl, rfl⟩, one_smul, tensorOf_single, if_pos rfl]
  · rw [if_neg fun hh => hb hh.1, zero_smul, tensorOf_zero, if_neg hb]

omit [Fintype B] in
theorem blockDephase_classical (k : B) (a₀ : A) (b : B) :
    blockDephase k (Matrix.single ((a₀, b) : A × B) (a₀, b) 1)
      = if b = k then Matrix.single ((a₀, k) : A × B) (a₀, k) 1 else 0 := by
  rw [blockDephase_apply]
  by_cases hb : b = k
  · subst hb
    rw [if_pos rfl, Finset.sum_eq_single a₀]
    · rw [single_entry, if_pos ⟨rfl, rfl⟩, one_smul]
    · intro a _ ha
      rw [single_entry, if_neg, zero_smul]
      rintro ⟨h1, -⟩
      exact ha (congrArg Prod.fst h1).symm
    · intro hc
      exact absurd (Finset.mem_univ _) hc
  · rw [if_neg hb, Finset.sum_eq_zero]
    intro a _
    rw [single_entry, if_neg, zero_smul]
    rintro ⟨h1, -⟩
    exact hb (congrArg Prod.snd h1)

omit [Fintype B] in
/-- **The freedom is invisible to the classical readout data.** On every classical
composite state, within-block dephasing and the local Lüders selector agree exactly — so
the classical ancilla-readout condition alone cannot distinguish them. -/
theorem blockDephase_classical_eq (k : B) (a₀ : A) (b : B) :
    blockDephase k (Matrix.single ((a₀, b) : A × B) (a₀, b) 1)
      = localLuders k (Matrix.single ((a₀, b) : A × B) (a₀, b) 1) := by
  rw [blockDephase_classical, localLuders_classical]

omit [Fintype B] in
/-- **But the freedom is real.** On a system coherence inside the surviving block,
within-block dephasing gives zero while the local Lüders selector preserves it. -/
theorem blockDephase_ne_localLuders (k : B) {a₀ a₁ : A} (ha : a₀ ≠ a₁) :
    blockDephase (A := A) k ≠ localLuders k := by
  intro heq
  have h := congrFun (congrFun (congrArg (fun Φ => Φ
    (Matrix.single ((a₀, k) : A × B) (a₁, k) 1)) heq) (a₀, k)) (a₁, k)
  rw [blockDephase_apply, Matrix.sum_apply, localLuders_apply, if_pos ⟨rfl, rfl⟩,
    single_entry, if_pos ⟨rfl, rfl⟩] at h
  rw [Finset.sum_eq_zero] at h
  · exact zero_ne_one h
  · intro a _
    rw [Matrix.smul_apply, smul_eq_mul, single_entry, single_entry,
      if_neg (show ¬(((a₀, k) : A × B) = (a, k) ∧ ((a₁, k) : A × B) = (a, k)) from
        fun hh => ha ((congrArg Prod.fst hh.1).trans (congrArg Prod.fst hh.2).symm)),
      zero_mul]

/-- **SPECTATOR INDEPENDENCE IS EXACTLY WHAT KILLS THE FREEDOM.** Within-block dephasing
is a completely positive map with the same classical readout action as the local Lüders
selector, and it fails map-level spectator independence. So composition — not positivity,
and not the classical data — is what forces the ancilla readout to be `id_A ⊗ ℒ_k`. -/
theorem blockDephase_not_mapSpectatorIndependent (k : B) {a₀ a₁ : A} (ha : a₀ ≠ a₁) :
    ¬MapSpectatorIndependent (ludersLift k) (blockDephase (A := A) k) := fun h =>
  blockDephase_ne_localLuders k ha ((mapSpectatorIndependent_iff_localLuders k _).mp h)

/-! ### Section C — independent product preparation -/

/-- **INDEPENDENT PRODUCT PREPARATION.** Preparing `ρ_A` and, separately, `τ_B` makes the
JOINT state the product `ρ_A ⊗ τ_B`. This is a physically distinct clause from spectator
independence of OPERATIONS: parallel composition of operations and parallel composition of
independently prepared states are related ideas but not the same predicate. Round
twenty-one produces the pure ancilla `|k₀⟩⟨k₀|` from the uniform state; it does NOT produce
the joint `ρ_S ⊗ |k₀⟩⟨k₀|_E` that Stinespring consumes, so this clause is named rather than
smuggled into `H_comp`. -/
def ProductPreparation
    (prep : Matrix A A ℂ → Matrix B B ℂ → Matrix (A × B) (A × B) ℂ) : Prop :=
  ∀ (ρ : Matrix A A ℂ) (τ : Matrix B B ℂ), prep ρ τ = tensorOf ρ τ

omit [Fintype A] [DecidableEq A] [Fintype B] [DecidableEq B] in
/-- The tensor preparation satisfies the clause; the content of the clause is that a
completion's ACTUAL joint preparation is this one. -/
theorem tensorOf_productPreparation :
    ProductPreparation (fun (ρ : Matrix A A ℂ) (τ : Matrix B B ℂ) => tensorOf ρ τ) :=
  fun _ _ => rfl


/-! ### Section D — the common operational structure -/

/-- **THE COMMON OPERATIONAL STRUCTURE.** Round twenty-four's control and richness
principles speak through an abstract `avail`, while `H_comp` speaks about `act`/`corr`;
those are logically disconnected objects, so a characterization cannot honestly be
assembled by conjoining predicates on unrelated parameters. This structure gathers the
availability notion together with the closure rules any operational completion must
satisfy — sequential composition, classical coarse-graining of the outcome label, and the
trivial operation — so that the principles become properties of ONE object. -/
structure FiniteOperationalCompletion (S : Type*) [Fintype S] [DecidableEq S] where
  /-- Which finite outcome families of operations are available. -/
  avail : ∀ m : ℕ, (Fin m → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) → Prop
  /-- Doing nothing is available. -/
  avail_id : avail 1 (fun _ => LinearMap.id)
  /-- Availability is closed under SEQUENTIAL composition of deterministic steps. -/
  avail_comp : ∀ Φ Ψ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ,
    avail 1 (fun _ => Φ) → avail 1 (fun _ => Ψ) → avail 1 (fun _ => Φ.comp Ψ)
  /-- Availability is closed under CLASSICAL COARSE-GRAINING of the outcome label. -/
  avail_coarse : ∀ (m m' : ℕ) (F : Fin m → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)
      (f : Fin m → Fin m'), avail m F →
    avail m' (fun a => ∑ j ∈ Finset.univ.filter (fun j => f j = a), F j)

/-- Universal unitary control, as a property of the completion ITSELF. -/
def HasUniversalUnitaryControl {S : Type*} [Fintype S] [DecidableEq S]
    (Ω : FiniteOperationalCompletion S) : Prop :=
  ∀ V : Matrix S S ℂ, Vᴴ * V = 1 → Ω.avail 1 (fun _ => conjChannel V)

/-- Full finite ENDOMORPHIC instrument availability on the fixed system `S`, as a property
of the completion ITSELF. The Kraus operators here are square, so this is precisely "all
finite endomorphic instruments on a fixed system `S`" — NOT "all finite quantum
instruments" without qualification, which would need rectangular Kraus maps or a
dimension-changing encoding. -/
def HasFullFiniteInstruments {S : Type*} [Fintype S] [DecidableEq S]
    (Ω : FiniteOperationalCompletion S) : Prop :=
  ∀ (n m : ℕ) (K : Fin n → Matrix S S ℂ) (out : Fin n → Fin m),
    (∑ k, (K k)ᴴ * K k = 1) → Ω.avail m (instrumentBranch K out)

/-- Instrument availability delivers universal unitary control INSIDE the one structure:
the one-Kraus, one-outcome instrument is exactly a unitary channel. -/
theorem hasFullInstruments_hasUniversalControl {S : Type*} [Fintype S] [DecidableEq S]
    (Ω : FiniteOperationalCompletion S) (h : HasFullFiniteInstruments Ω) :
    HasUniversalUnitaryControl Ω := by
  intro V hV
  have hb := h 1 1 (fun _ => V) (fun _ => 0) (by simpa using hV)
  have heq : instrumentBranch (fun _ : Fin 1 => V) (fun _ => (0 : Fin 1))
      = fun _ => conjChannel V := by
    funext a
    rw [instrumentBranch, Finset.filter_true_of_mem fun k _ => Subsingleton.elim _ _]
    simp
  rwa [heq] at hb

#print axioms spectatorIndependent_iff_mapLevel
#print axioms tensorOf_single
#print axioms localLuders_tensor
#print axioms localLuders_mapSpectatorIndependent
#print axioms eq_of_agree_on_single
#print axioms mapSpectatorIndependent_iff_localLuders
#print axioms blockDephase_apply
#print axioms choiMatrix_sum
#print axioms blockDephase_cp
#print axioms localLuders_classical
#print axioms blockDephase_classical
#print axioms blockDephase_classical_eq
#print axioms blockDephase_ne_localLuders
#print axioms blockDephase_not_mapSpectatorIndependent
#print axioms tensorOf_productPreparation
#print axioms hasFullInstruments_hasUniversalControl

end OperationalAssembly
end OIBridge
