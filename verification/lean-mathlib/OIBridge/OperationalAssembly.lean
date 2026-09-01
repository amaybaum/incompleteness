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

  §E — OPERATIONAL CLOSURE (round 25b). A PER-CARRIER availability notion cannot express
  the three cross-carrier joins the reconstruction consumes: that a native ancilla readout
  EXISTS, that independently prepared parts compose to a PRODUCT, and that a circuit on
  `A × Fin n` with the ancilla forgotten defines an operation on `A` alone.
  `FiniteOperationalTheory` carries an availability family for the system AND for every
  finite ancilla extension, with six closure rules: identity, classical coarse-graining on
  each carrier, GENERAL INSTRUMENT COMPOSITION (`availExt_bind` — feed-forward, which is
  what round twenty-one's measure-then-reset seed derivation actually uses), independent
  product preparation, native basis readout, and ancilla discard.

  The readout is deliberately NOT postulated as `id_A ⊗ ℒ_k`. It is postulated only to
  exist and to be spectator-independent, and `readout_is_localLuders` DERIVES the form from
  §B. That is the payoff of the §B theorem: the local readout branch is earned by
  composition, not assumed. `ptraceAnc_localLuders` then shows discard-after-readout is
  exactly the `k`-th ancilla block — round twenty's `sysBlock`, on the nose.

  `circuit_available` assembles the skeleton: prepare a pure ancilla, run any composite
  unitary (from `HasCompositeUnitaryControl`, which is family-level in the ancilla size —
  control on `A` says nothing about `A × Fin n`), read the ancilla, discard it; the closure
  rules alone deliver an available outcome family ON THE SYSTEM. `circuit_branch` computes
  each branch as the corresponding ancilla block.

  WHAT IS NOT HERE. The generic normalized-Kraus Stinespring instantiation of that
  skeleton, the derivation of full finite-instrument availability, and the structured
  standard-completion predicate are the remaining items; none is asserted. Note that
  PURIFICATION AND UHLMANN UNIQUENESS ARE NOT USED and will not be: instrument availability
  needs pure seed, Stinespring, unitary control and local readout only, so the boundary for
  that particular theorem is finite isometry extension alone. The project's global boundary
  remains exactly four items and no more: compact Lie integration, finite isometry
  extension, PSD square-root/factorization, and finite Uhlmann/Schmidt uniqueness.

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

/-! ### Section E — the operational closure structure (round 25b) -/

omit [Fintype A] [DecidableEq A] [Fintype B] [DecidableEq B] in
theorem tensorOf_add_left (ρ σ : Matrix A A ℂ) (τ : Matrix B B ℂ) :
    tensorOf (ρ + σ) τ = tensorOf ρ τ + tensorOf σ τ := by
  ext p q
  simp only [tensorOf_apply, Matrix.add_apply]
  ring

omit [Fintype A] [DecidableEq A] [Fintype B] [DecidableEq B] in
theorem tensorOf_smul_left (c : ℂ) (ρ : Matrix A A ℂ) (τ : Matrix B B ℂ) :
    tensorOf (c • ρ) τ = c • tensorOf ρ τ := by
  ext p q
  simp only [tensorOf_apply, Matrix.smul_apply, smul_eq_mul]
  ring

/-- The partial trace over the ancilla factor. -/
def ptraceAnc (n : ℕ) (M : Matrix (A × Fin n) (A × Fin n) ℂ) : Matrix A A ℂ :=
  Matrix.of fun s t => ∑ e : Fin n, M (s, e) (t, e)

omit [Fintype A] [DecidableEq A] [Fintype B] [DecidableEq B] in
@[simp] theorem ptraceAnc_apply (n : ℕ) (M : Matrix (A × Fin n) (A × Fin n) ℂ) (s t : A) :
    ptraceAnc n M s t = ∑ e : Fin n, M (s, e) (t, e) := rfl

omit [Fintype A] [DecidableEq A] in
/-- **DISCARD AFTER READOUT IS EXACTLY THE ANCILLA BLOCK.** Tracing out the ancilla after
the local Lüders readout keeping outcome `k` returns precisely the `k`-th ancilla block —
which is round twenty's `sysBlock`. So "read the ancilla, then forget it" is not an extra
approximation: it is block extraction, on the nose. -/
theorem ptraceAnc_localLuders (n : ℕ) (k : Fin n)
    (M : Matrix (A × Fin n) (A × Fin n) ℂ) :
    ptraceAnc n (localLuders k M) = Matrix.of fun s t => M (s, k) (t, k) := by
  ext s t
  rw [ptraceAnc_apply, Finset.sum_eq_single k]
  · rw [localLuders_apply, if_pos ⟨rfl, rfl⟩]
    rfl
  · intro e _ he
    rw [localLuders_apply, if_neg]
    rintro ⟨h1, -⟩
    exact he h1
  · intro hc
    exact absurd (Finset.mem_univ _) hc

/-- Run a composite operation on an independently prepared pure ancilla, then discard the
ancilla: the operation this induces on the system alone. -/
def discardMap (n : ℕ) (k₀ : Fin n)
    (Φ : Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ) :
    Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ where
  toFun ρ := ptraceAnc n (Φ (tensorOf ρ (Matrix.single k₀ k₀ 1)))
  map_add' ρ σ := by
    ext s t
    show ∑ e : Fin n, (Φ (tensorOf (ρ + σ) (Matrix.single k₀ k₀ 1))) (s, e) (t, e) = _
    rw [tensorOf_add_left, map_add]
    simp [Matrix.add_apply, Finset.sum_add_distrib]
  map_smul' c ρ := by
    ext s t
    show ∑ e : Fin n, (Φ (tensorOf (c • ρ) (Matrix.single k₀ k₀ 1))) (s, e) (t, e) = _
    rw [tensorOf_smul_left, map_smul]
    simp [Matrix.smul_apply, Finset.mul_sum]


/-- **A FINITE OPERATIONAL THEORY over a fixed system `A`.** A per-carrier availability
notion cannot express the three cross-carrier joins the reconstruction actually consumes:
that a native ancilla readout EXISTS, that independently prepared parts compose to a
PRODUCT, and that a circuit on `A × Fin n` with the ancilla forgotten defines an operation
on `A` alone. This structure carries an availability family for the system AND for every
finite ancilla extension, together with the closure rules relating them.

The readout is deliberately NOT postulated in the form `id_A ⊗ ℒ_k`. It is postulated only
to exist and to be spectator-independent; `readout_is_localLuders` then DERIVES the form
from `mapSpectatorIndependent_iff_localLuders`. That is the whole point of the round-25
theorem: the local readout branch is earned, not assumed.

DELIBERATELY ABSENT: parallel extension of a SYSTEM operation to the composite. The
circuit below never lifts a system operation — its composite unitary comes from
composite-dimension control — so the rule is not included rather than added unused. -/
structure FiniteOperationalTheory (A : Type*) [Fintype A] [DecidableEq A] where
  /-- Available finite outcome families of operations on the SYSTEM. -/
  avail : ∀ (O : Type) [Fintype O] [DecidableEq O],
    (O → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ) → Prop
  /-- Available finite outcome families on the system extended by an `n`-level ANCILLA. -/
  availExt : ∀ (n : ℕ) (O : Type) [Fintype O] [DecidableEq O],
    (O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ) → Prop
  /-- Doing nothing is available. -/
  avail_id : avail Unit (fun _ => LinearMap.id)
  /-- CLASSICAL COARSE-GRAINING of the outcome label, on the system. -/
  avail_coarse : ∀ (O O' : Type) [Fintype O] [DecidableEq O] [Fintype O'] [DecidableEq O']
      (F : O → Matrix A A ℂ →ₗ[ℂ] Matrix A A ℂ) (f : O → O'), avail O F →
    avail O' (fun a => ∑ j ∈ Finset.univ.filter (fun j => f j = a), F j)
  /-- CLASSICAL COARSE-GRAINING on the extended carrier. -/
  availExt_coarse : ∀ (n : ℕ) (O O' : Type) [Fintype O] [DecidableEq O] [Fintype O']
      [DecidableEq O']
      (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
      (f : O → O'), availExt n O F →
    availExt n O' (fun a => ∑ j ∈ Finset.univ.filter (fun j => f j = a), F j)
  /-- GENERAL INSTRUMENT COMPOSITION (feed-forward): run `F`, then run an
  outcome-dependent instrument `G a`. The joint outcome set is the product. This is the
  standard closure rule, and it is what round twenty-one's measure-then-reset seed
  derivation actually uses. -/
  availExt_bind : ∀ (n : ℕ) (O O' : Type) [Fintype O] [DecidableEq O] [Fintype O']
      [DecidableEq O']
      (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
      (G : O → O' → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ]
        Matrix (A × Fin n) (A × Fin n) ℂ),
    availExt n O F → (∀ a, availExt n O' (G a)) →
      availExt n (O × O') (fun c => (G c.1 c.2).comp (F c.1))
  /-- INDEPENDENT PRODUCT PREPARATION, as a clause of the theory. -/
  prep : ∀ n : ℕ, Fin n → Matrix A A ℂ → Matrix (A × Fin n) (A × Fin n) ℂ
  prep_isProduct : ∀ (n : ℕ) (k₀ : Fin n) (ρ : Matrix A A ℂ),
    prep n k₀ ρ = tensorOf ρ (Matrix.single k₀ k₀ 1)
  /-- NATIVE FINITE BASIS READOUT of the ancilla: some outcome family is available whose
  branches are spectator-independent over the rank-one Lüders selectors. Its FORM is not
  postulated — see `readout_is_localLuders`. -/
  readout : ∀ n : ℕ, Fin n →
    Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ
  readout_avail : ∀ n : ℕ, availExt n (Fin n) (readout n)
  readout_local : ∀ (n : ℕ) (k : Fin n),
    MapSpectatorIndependent (ludersLift k) (readout n k)
  /-- ANCILLA DISCARD. A circuit on the extended carrier, run on an independently prepared
  ancilla and then forgotten, defines an available operation family on the system alone.
  This is the cross-carrier rule the per-carrier structure could not express. -/
  availExt_discard : ∀ (n : ℕ) (k₀ : Fin n) (O : Type) [Fintype O] [DecidableEq O]
      (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ),
    availExt n O F → avail O (fun a => discardMap n k₀ (F a))

/-- **THE READOUT FORM IS DERIVED, NOT POSTULATED.** A theory's native ancilla readout is
assumed only to exist and to be spectator-independent; the round-25 uniqueness theorem
then forces it to be exactly `id_A ⊗ ℒ_k`. -/
theorem readout_is_localLuders (T : FiniteOperationalTheory A) (n : ℕ) (k : Fin n) :
    T.readout n k = localLuders k :=
  (mapSpectatorIndependent_iff_localLuders k _).mp (T.readout_local n k)

/-- The discard rule's product form is licensed by the theory's preparation clause. -/
theorem discardMap_eq_prep (T : FiniteOperationalTheory A) (n : ℕ) (k₀ : Fin n)
    (Φ : Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ)
    (ρ : Matrix A A ℂ) :
    discardMap n k₀ Φ ρ = ptraceAnc n (Φ (T.prep n k₀ ρ)) := by
  rw [T.prep_isProduct]
  rfl

/-- **COMPOSITE-DIMENSION CONTROL.** Universal unitary control on EVERY finite ancilla
extension, not merely on the system: a control premise on `A` says nothing whatever about
unitaries on `A × Fin n`, so the assembly's control hypothesis must be family-level. -/
def HasCompositeUnitaryControl (T : FiniteOperationalTheory A) : Prop :=
  ∀ (n : ℕ) (U : Matrix (A × Fin n) (A × Fin n) ℂ), Uᴴ * U = 1 →
    T.availExt n Unit (fun _ => conjChannel U)

/-- **THE CIRCUIT IS AVAILABLE.** Prepare an `n`-level ancilla in a pure basis state, run
any composite unitary, read the ancilla in its fixed basis, and discard it: the closure
rules alone deliver an available outcome family on the SYSTEM, indexed by the ancilla
outcome. No Kraus family, no Stinespring, no purification and no Uhlmann uniqueness is
used — this is the circuit skeleton the generic assembly will instantiate. -/
theorem circuit_available (T : FiniteOperationalTheory A)
    (hctrl : HasCompositeUnitaryControl T) (n : ℕ) (k₀ : Fin n)
    (U : Matrix (A × Fin n) (A × Fin n) ℂ) (hU : Uᴴ * U = 1) :
    T.avail (Fin n) (fun k => discardMap n k₀ ((localLuders k).comp (conjChannel U))) := by
  have h2 := T.availExt_bind n Unit (Fin n) (fun _ => conjChannel U)
    (fun _ => T.readout n) (hctrl n U hU) (fun _ => T.readout_avail n)
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
  exact T.availExt_discard n k₀ (Fin n) _ h3

/-- **AND ITS BRANCHES ARE THE ANCILLA BLOCKS.** Each branch of that circuit is exactly the
`k`-th ancilla block of the conjugated prepared state — round twenty's `sysBlock`. With `U`
taken to be a Stinespring dilation of a normalized Kraus family this is `K_k ρ K_k†`, which
is the one remaining step of the generic assembly. -/
theorem circuit_branch (n : ℕ) (k₀ k : Fin n)
    (U : Matrix (A × Fin n) (A × Fin n) ℂ) (ρ : Matrix A A ℂ) :
    discardMap n k₀ ((localLuders k).comp (conjChannel U)) ρ
      = Matrix.of fun s t =>
          (U * tensorOf ρ (Matrix.single k₀ k₀ 1) * Uᴴ) (s, k) (t, k) := by
  show ptraceAnc n (localLuders k (conjChannel U
    (tensorOf ρ (Matrix.single k₀ k₀ 1)))) = _
  rw [ptraceAnc_localLuders]
  rfl

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
#print axioms tensorOf_add_left
#print axioms ptraceAnc_localLuders
#print axioms readout_is_localLuders
#print axioms discardMap_eq_prep
#print axioms circuit_available
#print axioms circuit_branch

end OperationalAssembly
end OIBridge
