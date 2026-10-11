import OIBridge.RouteB
import OIBridge.CentralObservation

/-!
# Origin exclusive — design module of the research thread `research/origin` (round 3, O8)

A design artifact on a disposable branch; it is not part of any governed round and asserts no
status. It states the exclusivity clause of the knowledge-balance readout — no passive readout of
any nontrivial partition is available — in the kernel's vocabulary of passive instruments on an
algebra `⊕ᵢ M_{dᵢ}` (`CentralObservation.IsBlockPassiveInstrument`), and shows that the native
readout of every finite operational theory refutes it on the algebras a classical carrier observes.

* **The native readout is the block pinching of the ancilla values** (`localLuders_eq_blockPinch`,
  `nativeReadout_eq_blockPinch`): `readout_is_localLuders` makes every branch the selector
  `id_A ⊗ ℒ_k`, which is the kernel's `blockPinch` for the labelling by the ancilla value. It is a
  passive instrument on the algebra of the ancilla values (`nativeReadout_blockPassive`) and on the
  configuration (diagonal) algebra (`nativeReadout_blockPassive_diagonal`), and it is repeatable
  (`nativeReadout_repeatable`).
* **The exclusivity clause** (`ExclusiveOn`): every available outcome family that is a passive
  instrument on the algebra has a state-independent outcome law there.
* **The no-go** (`not_exclusiveOn_of_refines`, with the cases `not_exclusiveOn_ancilla`,
  `not_exclusiveOn_diagonal`): in every `FiniteOperationalTheory` over a nonempty system the
  clause fails, at ancilla size two, on every algebra whose blocks do not straddle two ancilla
  values; what it contradicts is `readout_is_localLuders` with the structure field
  `readout_avail`. Hence the clause presupposes a block straddling two ancilla values, a coherence
  between them (`exists_straddle_of_exclusiveOn`).
  **The control** (`exclusiveOn_factor`): on the full matrix algebra of the extended carrier, one
  block, the clause holds in every theory, by OI-N1 (`branch_scalar_on_block`).
* **The substratum theory** (`substratumTheory_hasAncillaSwapControl`, `substratumTheory_pureSeed`,
  `substratumTheory_exclusivity_false`): the ancilla exchanges are monomial, hence available, so
  `pureSeedPrep_available_of_swap` makes every ancilla point mass preparable from the uniform
  ancilla, and the clause fails on both algebras.
* **The classical carrier, any cell** (`passive_repeatable_eq`, `Reach`, `step_eq_mergeInto`,
  `reach_mergeInto`, `reach_collectAt`, `reach_pointMass`): on a finite configuration set with
  every permutation available, a passive repeatable readout of a cell is the restriction to the
  cell, and the readout of any one cell that is neither empty nor everything makes every point mass
  reachable from the uniform state by the pure-seed pattern (read, correct by feed-forward,
  forget).
-/

namespace OIBridge
namespace OriginExclusive

open OperationalAssembly

/-! ### Section A — the native readout is the block pinching of the ancilla values -/

section Native

variable {A : Type} [Fintype A] [DecidableEq A]

/-- A matrix lying in block `j` has no part in another block `i`. -/
theorem blockPart_eq_zero_of_inBlock {S I : Type*} [DecidableEq I] (blk : S → I) {i j : I}
    (hij : i ≠ j) {X : Matrix S S ℂ} (hX : CentralObservation.InBlock blk j X) :
    CentralObservation.blockPart blk i X = 0 := by
  ext s t
  by_cases h : blk s = i ∧ blk t = i
  · rw [CentralObservation.blockPart_apply, if_pos h, Matrix.zero_apply]
    apply hX
    rintro ⟨h1, -⟩
    exact hij (h.1.symm.trans h1)
  · rw [CentralObservation.blockPart_apply, if_neg h, Matrix.zero_apply]

/-- The block parts are orthogonal idempotents. -/
theorem blockPart_blockPart {S I : Type*} [DecidableEq I] (blk : S → I) (i j : I)
    (X : Matrix S S ℂ) :
    CentralObservation.blockPart blk i (CentralObservation.blockPart blk j X)
      = if i = j then CentralObservation.blockPart blk j X else 0 := by
  by_cases hij : i = j
  · subst hij
    rw [if_pos rfl]
    exact CentralObservation.blockPart_eq_of_inBlock blk
      (CentralObservation.blockPart_inBlock blk _ X)
  · rw [if_neg hij]
    exact blockPart_eq_zero_of_inBlock blk hij (CentralObservation.blockPart_inBlock blk j X)

/-- **The local Lüders selector is the block pinching of the ancilla value.** -/
theorem localLuders_eq_blockPinch {n : ℕ} (k : Fin n) :
    localLuders (A := A) k = CentralObservation.blockPinch (Prod.snd : A × Fin n → Fin n) k := by
  refine LinearMap.ext fun X => ?_
  rw [CentralObservation.blockPinch_apply]
  ext ⟨a, i⟩ ⟨b, j⟩
  rw [localLuders_apply, CentralObservation.blockPart_apply]
  by_cases h : i = k ∧ j = k
  · obtain ⟨rfl, rfl⟩ := h
    simp
  · have h' : ¬ (((a, i) : A × Fin n).2 = k ∧ ((b, j) : A × Fin n).2 = k) := h
    rw [if_neg h', if_neg h']

/-- **The native readout of every finite operational theory is the block pinching of the ancilla
values** (`readout_is_localLuders`). -/
theorem nativeReadout_eq_blockPinch (T : FiniteOperationalTheory A) (n : ℕ) :
    T.readout n = CentralObservation.blockPinch (Prod.snd : A × Fin n → Fin n) :=
  funext fun k => (readout_is_localLuders T n k).trans (localLuders_eq_blockPinch k)

/-- **The native readout is a passive instrument on the algebra of the ancilla values.** -/
theorem nativeReadout_blockPassive (T : FiniteOperationalTheory A) (n : ℕ) :
    CentralObservation.IsBlockPassiveInstrument (Prod.snd : A × Fin n → Fin n) (T.readout n) := by
  rw [nativeReadout_eq_blockPinch]
  exact CentralObservation.blockPinch_passive _

/-- **And on the configuration algebra**, the diagonal matrices, which lie inside it. -/
theorem nativeReadout_blockPassive_diagonal (T : FiniteOperationalTheory A) (n : ℕ) :
    CentralObservation.IsBlockPassiveInstrument (id : A × Fin n → A × Fin n) (T.readout n) := by
  refine ⟨(nativeReadout_blockPassive T n).1, fun X hX => (nativeReadout_blockPassive T n).2 X ?_⟩
  intro s t hst
  exact hX s t fun h => hst (congrArg Prod.snd h)

/-- **The native readout is repeatable**: an outcome once read is read again surely. -/
theorem nativeReadout_repeatable (T : FiniteOperationalTheory A) (n : ℕ) (j k : Fin n)
    (X : Matrix (A × Fin n) (A × Fin n) ℂ) :
    T.readout n j (T.readout n k X) = if j = k then T.readout n k X else 0 := by
  rw [nativeReadout_eq_blockPinch, CentralObservation.blockPinch_apply,
    CentralObservation.blockPinch_apply, blockPart_blockPart]

/-! ### Section B — the exclusivity clause, its refutation and its control -/

/-- **The exclusivity clause of the knowledge-balance readout, relative to the algebra
`⊕ᵢ M_{dᵢ}` of a block labelling `blk` of the extended carrier.** Every available outcome family
that is a passive instrument on the algebra has, on that algebra, an outcome law independent of the
state: no passive readout of any nontrivial partition is available. -/
def ExclusiveOn {n : ℕ} {I : Type} [DecidableEq I] (blk : A × Fin n → I)
    (T : FiniteOperationalTheory A) : Prop :=
  ∀ (O : Type) [Fintype O] [DecidableEq O]
    (F : O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] Matrix (A × Fin n) (A × Fin n) ℂ),
    T.availExt n O F → CentralObservation.IsBlockPassiveInstrument blk F →
    ∀ a, ∃ c : ℂ, ∀ ρ : Matrix (A × Fin n) (A × Fin n) ℂ,
      CentralObservation.BlockDiag blk ρ → ((F a) ρ).trace = c * ρ.trace

/-- **The no-go on the algebra of the ancilla values.** In every finite operational theory over a
nonempty system the exclusivity clause fails at ancilla size two: the native readout is available
(`readout_avail`), passive on the algebra (`readout_is_localLuders`), and its outcome `0` has
probability `1` on one pure state of the algebra and `0` on another. -/
theorem not_exclusiveOn_ancilla [Nonempty A] (T : FiniteOperationalTheory A) :
    ¬ ExclusiveOn (Prod.snd : A × Fin 2 → Fin 2) T := by
  intro h
  obtain ⟨c, hc⟩ := h (Fin 2) (T.readout 2) (T.readout_avail 2) (nativeReadout_blockPassive T 2) 0
  obtain ⟨a₀⟩ := (inferInstance : Nonempty A)
  have hin0 : CentralObservation.InBlock (Prod.snd : A × Fin 2 → Fin 2) 0
      (PassiveObservation.pureState ((a₀, 0) : A × Fin 2)) :=
    CentralObservation.pureState_inBlock (Prod.snd : A × Fin 2 → Fin 2) ((a₀, 0) : A × Fin 2)
  have hin1 : CentralObservation.InBlock (Prod.snd : A × Fin 2 → Fin 2) 1
      (PassiveObservation.pureState ((a₀, 1) : A × Fin 2)) :=
    CentralObservation.pureState_inBlock (Prod.snd : A × Fin 2 → Fin 2) ((a₀, 1) : A × Fin 2)
  have h0 := hc _ (CentralObservation.inBlock_blockDiag _ hin0)
  have h1 := hc _ (CentralObservation.inBlock_blockDiag _ hin1)
  rw [nativeReadout_eq_blockPinch, CentralObservation.blockPinch_apply,
    CentralObservation.blockPart_eq_of_inBlock _ hin0, PassiveObservation.pure_trace] at h0
  rw [nativeReadout_eq_blockPinch, CentralObservation.blockPinch_apply,
    blockPart_eq_zero_of_inBlock _ (by decide : (0 : Fin 2) ≠ 1) hin1, Matrix.trace_zero,
    PassiveObservation.pure_trace] at h1
  exact one_ne_zero (h0.trans h1.symm)

/-- **The no-go on the configuration algebra** (the diagonal matrices): the same native readout is
a passive instrument there with the same state-dependent outcome law. -/
theorem not_exclusiveOn_diagonal [Nonempty A] (T : FiniteOperationalTheory A) :
    ¬ ExclusiveOn (id : A × Fin 2 → A × Fin 2) T := by
  intro h
  obtain ⟨c, hc⟩ := h (Fin 2) (T.readout 2) (T.readout_avail 2)
    (nativeReadout_blockPassive_diagonal T 2) 0
  obtain ⟨a₀⟩ := (inferInstance : Nonempty A)
  have hin0 : CentralObservation.InBlock (Prod.snd : A × Fin 2 → Fin 2) 0
      (PassiveObservation.pureState ((a₀, 0) : A × Fin 2)) :=
    CentralObservation.pureState_inBlock (Prod.snd : A × Fin 2 → Fin 2) ((a₀, 0) : A × Fin 2)
  have hin1 : CentralObservation.InBlock (Prod.snd : A × Fin 2 → Fin 2) 1
      (PassiveObservation.pureState ((a₀, 1) : A × Fin 2)) :=
    CentralObservation.pureState_inBlock (Prod.snd : A × Fin 2 → Fin 2) ((a₀, 1) : A × Fin 2)
  have h0 := hc _ (CentralObservation.inBlock_blockDiag _
    (CentralObservation.pureState_inBlock (id : A × Fin 2 → A × Fin 2) ((a₀, 0) : A × Fin 2)))
  have h1 := hc _ (CentralObservation.inBlock_blockDiag _
    (CentralObservation.pureState_inBlock (id : A × Fin 2 → A × Fin 2) ((a₀, 1) : A × Fin 2)))
  rw [nativeReadout_eq_blockPinch, CentralObservation.blockPinch_apply,
    CentralObservation.blockPart_eq_of_inBlock _ hin0, PassiveObservation.pure_trace] at h0
  rw [nativeReadout_eq_blockPinch, CentralObservation.blockPinch_apply,
    blockPart_eq_zero_of_inBlock _ (by decide : (0 : Fin 2) ≠ 1) hin1, Matrix.trace_zero,
    PassiveObservation.pure_trace] at h1
  exact one_ne_zero (h0.trans h1.symm)

/-- **The no-go on every algebra refining the ancilla value.** If no block of the labelling
`blk` contains two configurations with different ancilla values, the native readout is a passive
instrument on the labelling's algebra with a state-dependent outcome law there, so the exclusivity
clause fails on it. `not_exclusiveOn_ancilla` and `not_exclusiveOn_diagonal` are the cases
`Prod.snd` and `id`. -/
theorem not_exclusiveOn_of_refines [Nonempty A] {I : Type} [DecidableEq I]
    (blk : A × Fin 2 → I) (hblk : ∀ s t, blk s = blk t → s.2 = t.2)
    (T : FiniteOperationalTheory A) : ¬ ExclusiveOn blk T := by
  intro h
  have hpass : CentralObservation.IsBlockPassiveInstrument blk (T.readout 2) := by
    refine ⟨(nativeReadout_blockPassive T 2).1, fun X hX => (nativeReadout_blockPassive T 2).2 X ?_⟩
    intro s t hst
    exact hX s t fun h' => hst (hblk s t h')
  obtain ⟨c, hc⟩ := h (Fin 2) (T.readout 2) (T.readout_avail 2) hpass 0
  obtain ⟨a₀⟩ := (inferInstance : Nonempty A)
  have hin0 : CentralObservation.InBlock (Prod.snd : A × Fin 2 → Fin 2) 0
      (PassiveObservation.pureState ((a₀, 0) : A × Fin 2)) :=
    CentralObservation.pureState_inBlock (Prod.snd : A × Fin 2 → Fin 2) ((a₀, 0) : A × Fin 2)
  have hin1 : CentralObservation.InBlock (Prod.snd : A × Fin 2 → Fin 2) 1
      (PassiveObservation.pureState ((a₀, 1) : A × Fin 2)) :=
    CentralObservation.pureState_inBlock (Prod.snd : A × Fin 2 → Fin 2) ((a₀, 1) : A × Fin 2)
  have h0 := hc _ (CentralObservation.inBlock_blockDiag _
    (CentralObservation.pureState_inBlock blk ((a₀, 0) : A × Fin 2)))
  have h1 := hc _ (CentralObservation.inBlock_blockDiag _
    (CentralObservation.pureState_inBlock blk ((a₀, 1) : A × Fin 2)))
  rw [nativeReadout_eq_blockPinch, CentralObservation.blockPinch_apply,
    CentralObservation.blockPart_eq_of_inBlock _ hin0, PassiveObservation.pure_trace] at h0
  rw [nativeReadout_eq_blockPinch, CentralObservation.blockPinch_apply,
    blockPart_eq_zero_of_inBlock _ (by decide : (0 : Fin 2) ≠ 1) hin1, Matrix.trace_zero,
    PassiveObservation.pure_trace] at h1
  exact one_ne_zero (h0.trans h1.symm)

/-- **Exclusivity presupposes coherence between ancilla values.** If the exclusivity clause holds on
the algebra of a labelling, some block of that algebra contains two configurations with different
ancilla values: the observed algebra carries a coherence between ancilla values, which no family of
the monomial classes creates from a configuration-diagonal state. -/
theorem exists_straddle_of_exclusiveOn [Nonempty A] {I : Type} [DecidableEq I]
    (blk : A × Fin 2 → I) (T : FiniteOperationalTheory A) (h : ExclusiveOn blk T) :
    ∃ s t : A × Fin 2, blk s = blk t ∧ s.2 ≠ t.2 := by
  by_contra hne
  refine not_exclusiveOn_of_refines blk (fun s t hst => ?_) T h
  by_contra h'
  exact hne ⟨s, t, hst, h'⟩

/-- **The control: on a factor the clause holds in every theory.** On the full matrix algebra of
the extended carrier (the labelling with one block) every branch of a passive instrument is a scalar
(OI-N1, `branch_scalar_on_block`), so its outcome law is state-independent. -/
theorem exclusiveOn_factor (T : FiniteOperationalTheory A) (n : ℕ) :
    ExclusiveOn (fun _ : A × Fin n => ()) T := by
  intro O _ _ F _ hF a
  obtain ⟨c, hc⟩ := CentralObservation.branch_scalar_on_block (fun _ : A × Fin n => ()) () hF a
  refine ⟨c, fun ρ _ => ?_⟩
  have hin : CentralObservation.InBlock (fun _ : A × Fin n => ()) () ρ :=
    fun _ _ hst => False.elim (hst ⟨rfl, rfl⟩)
  rw [hc ρ hin, Matrix.trace_smul, smul_eq_mul]

/-! ### Section C — the substratum theory -/

/-- **The ancilla exchanges are available in the substratum theory**: they are monomial. -/
theorem substratumTheory_hasAncillaSwapControl :
    HasAncillaSwapControl (RouteB.substratumTheory A) := fun n k k₀ =>
  RouteB.substratumTheory_avail_conj (SubstratumInterface.monomial_permMatrix _)
    (ancSwap_unitary n k k₀)

/-- **Every ancilla point mass is preparable in the substratum theory**, from the uniform ancilla,
by the kernel's pure-seed derivation: read, correct by an exchange, forget. -/
theorem substratumTheory_pureSeed (n : ℕ) (k₀ : Fin (n + 1)) :
    (RouteB.substratumTheory A).prepAvail (n + 1) (pureAttach (n + 1) k₀) :=
  pureSeedPrep_available_of_swap _ n k₀ fun k =>
    substratumTheory_hasAncillaSwapControl (n + 1) k k₀

/-- **The exclusivity clause is false on the stated access.** In the substratum theory the native
readout refutes the clause on the algebra of the ancilla values and on the configuration algebra,
and every ancilla point mass is preparable from the uniform ancilla. -/
theorem substratumTheory_exclusivity_false [Nonempty A] :
    ¬ ExclusiveOn (Prod.snd : A × Fin 2 → Fin 2) (RouteB.substratumTheory A)
      ∧ ¬ ExclusiveOn (id : A × Fin 2 → A × Fin 2) (RouteB.substratumTheory A)
      ∧ ∀ (n : ℕ) (k₀ : Fin (n + 1)),
          (RouteB.substratumTheory A).prepAvail (n + 1) (pureAttach (n + 1) k₀) :=
  ⟨not_exclusiveOn_ancilla _, not_exclusiveOn_diagonal _, substratumTheory_pureSeed⟩

end Native

/-! ### Section D — the classical carrier, any cell -/

section Classical

variable {Ω : Type*} [Fintype Ω] [DecidableEq Ω]

/-- The branch "in the cell `C`" of the cell's readout on the classical carrier. -/
noncomputable def inCell (C : Finset Ω) (w : Ω → ℝ) (x : Ω) : ℝ := if x ∈ C then w x else 0

/-- The branch "not in the cell `C`". -/
noncomputable def outCell (C : Finset Ω) (w : Ω → ℝ) (x : Ω) : ℝ := if x ∈ C then 0 else w x

/-- Transport of a distribution by a permutation of the configurations. -/
noncomputable def pushPerm (σ : Equiv.Perm Ω) (w : Ω → ℝ) (x : Ω) : ℝ := w (σ.symm x)

omit [Fintype Ω] in
theorem inCell_add_outCell (C : Finset Ω) (w : Ω → ℝ) (x : Ω) :
    inCell C w x + outCell C w x = w x := by
  unfold inCell outCell
  split_ifs <;> ring

omit [Fintype Ω] in
/-- **A passive repeatable readout of a cell is the restriction to the cell.** Two branches that
sum to the state (passive), the first vanishing off the cell and the second on it (repeatable: each
reads its outcome surely), are `inCell` and `outCell`. -/
theorem passive_repeatable_eq (C : Finset Ω) {w u v : Ω → ℝ} (hpass : ∀ x, u x + v x = w x)
    (hu : ∀ x, x ∉ C → u x = 0) (hv : ∀ x, x ∈ C → v x = 0) :
    u = inCell C w ∧ v = outCell C w := by
  constructor
  · funext x
    unfold inCell
    by_cases h : x ∈ C
    · rw [if_pos h, ← hpass x, hv x h, add_zero]
    · rw [if_neg h, hu x h]
  · funext x
    unfold outCell
    by_cases h : x ∈ C
    · rw [if_pos h, hv x h]
    · rw [if_neg h, ← hpass x, hu x h, zero_add]

/-- The distributions reachable from the uniform one with every permutation of the configurations
and the readout of the cell `C`, by the kernel's pure-seed pattern: read the cell, apply an
outcome-dependent permutation, forget the outcome. -/
inductive Reach (C : Finset Ω) : (Ω → ℝ) → Prop
  | seed : Reach C fun _ => (Fintype.card Ω : ℝ)⁻¹
  | step (σ τ : Equiv.Perm Ω) {w : Ω → ℝ} :
      Reach C w → Reach C fun x => pushPerm σ (inCell C w) x + pushPerm τ (outCell C w) x

theorem Reach.of_eq {C : Finset Ω} {w w' : Ω → ℝ} (h : Reach C w) (e : w = w') : Reach C w' :=
  e ▸ h

/-- A permutation alone is the pattern with the same correction on both outcomes. -/
theorem reach_pushPerm {C : Finset Ω} (σ : Equiv.Perm Ω) {w : Ω → ℝ} (hw : Reach C w) :
    Reach C (pushPerm σ w) :=
  (Reach.step σ σ hw).of_eq (funext fun x => inCell_add_outCell C w (σ.symm x))

/-- Moving the mass of `y` onto `x`. -/
noncomputable def mergeInto (x y : Ω) (w : Ω → ℝ) (z : Ω) : ℝ :=
  if z = x then w x + w y else if z = y then 0 else w z

omit [Fintype Ω] in
theorem mergeInto_apply_left (x y : Ω) (w : Ω → ℝ) : mergeInto x y w x = w x + w y := by
  simp [mergeInto]

omit [Fintype Ω] in
theorem mergeInto_apply_right {x y : Ω} (h : y ≠ x) (w : Ω → ℝ) : mergeInto x y w y = 0 := by
  simp [mergeInto, h]

omit [Fintype Ω] in
theorem mergeInto_apply_of_ne {x y z : Ω} (hx : z ≠ x) (hy : z ≠ y) (w : Ω → ℝ) :
    mergeInto x y w z = w z := by
  simp [mergeInto, hx, hy]

omit [Fintype Ω] in
/-- A nontrivial cell separates any two configurations after a permutation. -/
theorem exists_perm_sep {C : Finset Ω} (hC : ∃ c, c ∈ C) (hC' : ∃ d, d ∉ C) {x y : Ω}
    (hxy : x ≠ y) : ∃ π : Equiv.Perm Ω, π y ∈ C ∧ π x ∉ C := by
  obtain ⟨c, hc⟩ := hC
  obtain ⟨d, hd⟩ := hC'
  refine ⟨(Equiv.swap y c).trans (Equiv.swap ((Equiv.swap y c) x) d), ?_, ?_⟩
  · rw [Equiv.trans_apply, Equiv.swap_apply_left]
    have hcd : c ≠ d := fun h => hd (h ▸ hc)
    have hcx : c ≠ (Equiv.swap y c) x := by
      intro h
      apply hxy
      have h' := congrArg (Equiv.swap y c) h
      rw [Equiv.swap_apply_self, Equiv.swap_apply_right] at h'
      exact h'.symm
    rw [Equiv.swap_apply_of_ne_of_ne hcx hcd]
    exact hc
  · rw [Equiv.trans_apply, Equiv.swap_apply_left]
    exact hd

omit [Fintype Ω] in
/-- **The step's value at each configuration.** With `π y` in the cell and `π x` outside it, the
step whose outcome "in" is corrected by the exchange of the two images followed by `π⁻¹`, and whose
outcome "out" is corrected by `π⁻¹`, moves the mass of `y` onto `x` and leaves the rest. -/
theorem step_eq_mergeInto {C : Finset Ω} {π : Equiv.Perm Ω} {x y : Ω} (hy : π y ∈ C)
    (hx : π x ∉ C) (w : Ω → ℝ) (z : Ω) :
    pushPerm ((Equiv.swap (π x) (π y)).trans π.symm) (inCell C (pushPerm π w)) z
      + pushPerm π.symm (outCell C (pushPerm π w)) z = mergeInto x y w z := by
  by_cases hzx : z = x
  · subst hzx
    simp [pushPerm, inCell, outCell, mergeInto, Equiv.symm_trans_apply, Equiv.symm_swap,
      Equiv.symm_symm, Equiv.symm_apply_apply, Equiv.swap_apply_left, hy, hx, add_comm]
  · by_cases hzy : z = y
    · subst hzy
      simp [pushPerm, inCell, outCell, mergeInto, Equiv.symm_trans_apply, Equiv.symm_swap,
        Equiv.symm_symm, Equiv.symm_apply_apply, Equiv.swap_apply_right, hy, hx, hzx]
    · have h1 : π z ≠ π x := fun h => hzx (π.injective h)
      have h2 : π z ≠ π y := fun h => hzy (π.injective h)
      by_cases hc : π z ∈ C
      · simp [pushPerm, inCell, outCell, mergeInto, Equiv.symm_trans_apply, Equiv.symm_swap,
          Equiv.symm_symm, Equiv.symm_apply_apply, Equiv.swap_apply_of_ne_of_ne h1 h2, hc, hzx, hzy]
      · simp [pushPerm, inCell, outCell, mergeInto, Equiv.symm_trans_apply, Equiv.symm_swap,
          Equiv.symm_symm, Equiv.symm_apply_apply, Equiv.swap_apply_of_ne_of_ne h1 h2, hc, hzx, hzy]

/-- **One step of the pattern merges any configuration into any other.** Permute so that the cell
holds `y` and not `x`, read the cell, correct the outcome "in" by the exchange of the two images and
the permutation back, correct the outcome "out" by the permutation back, forget the outcome. -/
theorem reach_mergeInto {C : Finset Ω} (hC : ∃ c, c ∈ C) (hC' : ∃ d, d ∉ C) {w : Ω → ℝ}
    (hw : Reach C w) {x y : Ω} (hxy : x ≠ y) : Reach C (mergeInto x y w) := by
  obtain ⟨π, hy, hx⟩ := exists_perm_sep hC hC' hxy
  exact (Reach.step ((Equiv.swap (π x) (π y)).trans π.symm) π.symm (reach_pushPerm π hw)).of_eq
    (funext fun z => step_eq_mergeInto hy hx w z)

/-- The mass of the configurations of `R` collected onto `x₀`. -/
noncomputable def collectAt (x₀ : Ω) (R : Finset Ω) (w : Ω → ℝ) (z : Ω) : ℝ :=
  if z = x₀ then w x₀ + ∑ y ∈ R, w y else if z ∈ R then 0 else w z

omit [Fintype Ω] in
theorem collectAt_apply_self (x₀ : Ω) (R : Finset Ω) (w : Ω → ℝ) :
    collectAt x₀ R w x₀ = w x₀ + ∑ y ∈ R, w y := by
  simp [collectAt]

omit [Fintype Ω] in
theorem collectAt_apply_mem {x₀ z : Ω} {R : Finset Ω} (hz : z ≠ x₀) (hzR : z ∈ R)
    (w : Ω → ℝ) : collectAt x₀ R w z = 0 := by
  simp [collectAt, hz, hzR]

omit [Fintype Ω] in
theorem collectAt_apply_not_mem {x₀ z : Ω} {R : Finset Ω} (hz : z ≠ x₀) (hzR : z ∉ R)
    (w : Ω → ℝ) : collectAt x₀ R w z = w z := by
  simp [collectAt, hz, hzR]

theorem mergeInto_collectAt {x₀ y : Ω} {R : Finset Ω} (hyx : y ≠ x₀) (hyR : y ∉ R)
    (w : Ω → ℝ) : mergeInto x₀ y (collectAt x₀ R w) = collectAt x₀ (insert y R) w := by
  funext z
  by_cases hz : z = x₀
  · subst hz
    rw [mergeInto_apply_left, collectAt_apply_self, collectAt_apply_self,
      collectAt_apply_not_mem hyx hyR, Finset.sum_insert hyR]
    ring
  · by_cases hzy : z = y
    · subst hzy
      rw [mergeInto_apply_right hz, collectAt_apply_mem hz (Finset.mem_insert_self _ _)]
    · rw [mergeInto_apply_of_ne hz hzy]
      by_cases hzR : z ∈ R
      · rw [collectAt_apply_mem hz hzR, collectAt_apply_mem hz (Finset.mem_insert_of_mem hzR)]
      · have hzR' : z ∉ insert y R := by
          rw [Finset.mem_insert]
          rintro (h | h)
          · exact hzy h
          · exact hzR h
        rw [collectAt_apply_not_mem hz hzR, collectAt_apply_not_mem hz hzR']

/-- **Collecting any set of configurations onto `x₀` is reachable.** -/
theorem reach_collectAt {C : Finset Ω} (hC : ∃ c, c ∈ C) (hC' : ∃ d, d ∉ C) (x₀ : Ω)
    (R : Finset Ω) : x₀ ∉ R → ∀ w, Reach C w → Reach C (collectAt x₀ R w) := by
  induction R using Finset.induction_on with
  | empty =>
    intro _ w hw
    refine hw.of_eq (funext fun z => ?_)
    by_cases hz : z = x₀
    · subst hz
      rw [collectAt_apply_self, Finset.sum_empty, add_zero]
    · rw [collectAt_apply_not_mem hz (Finset.notMem_empty z)]
  | insert y R hyR ih =>
    intro hx₀ w hw
    have hyx : y ≠ x₀ := by
      intro h
      apply hx₀
      rw [← h]
      exact Finset.mem_insert_self y R
    have hx₀R : x₀ ∉ R := fun h => hx₀ (Finset.mem_insert_of_mem h)
    rw [← mergeInto_collectAt hyx hyR w]
    exact reach_mergeInto hC hC' (ih hx₀R w hw) (Ne.symm hyx)

theorem collectAt_univ_apply (x₀ : Ω) (w : Ω → ℝ) (z : Ω) :
    collectAt x₀ (Finset.univ.erase x₀) w z = if z = x₀ then ∑ y, w y else 0 := by
  by_cases hz : z = x₀
  · subst hz
    rw [collectAt_apply_self, if_pos rfl, Finset.add_sum_erase _ _ (Finset.mem_univ _)]
  · rw [collectAt_apply_mem hz (Finset.mem_erase.2 ⟨hz, Finset.mem_univ z⟩), if_neg hz]

omit [DecidableEq Ω] in
theorem sum_uniform [Nonempty Ω] : ∑ _y : Ω, (Fintype.card Ω : ℝ)⁻¹ = 1 := by
  rw [Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
  exact mul_inv_cancel₀ (Nat.cast_ne_zero.mpr Fintype.card_ne_zero)

/-- **Every point mass is reachable** with every permutation and the readout of any one cell that is
neither empty nor everything: the generalization, to every finite configuration set and every
nontrivial cell, of the exclusivity no-go of the knowledge-balance toy (one passive readout of any
partition, with the exchanges, restores the simplex). -/
theorem reach_pointMass {C : Finset Ω} (hC : ∃ c, c ∈ C) (hC' : ∃ d, d ∉ C) (x₀ : Ω) :
    Reach C fun z => if z = x₀ then 1 else 0 := by
  have : Nonempty Ω := ⟨x₀⟩
  refine (reach_collectAt hC hC' x₀ (Finset.univ.erase x₀) (Finset.notMem_erase x₀ _) _
    Reach.seed).of_eq (funext fun z => ?_)
  rw [collectAt_univ_apply, sum_uniform]

end Classical

#print axioms blockPart_eq_zero_of_inBlock
#print axioms blockPart_blockPart
#print axioms localLuders_eq_blockPinch
#print axioms nativeReadout_eq_blockPinch
#print axioms nativeReadout_blockPassive
#print axioms nativeReadout_blockPassive_diagonal
#print axioms nativeReadout_repeatable
#print axioms not_exclusiveOn_ancilla
#print axioms not_exclusiveOn_diagonal
#print axioms not_exclusiveOn_of_refines
#print axioms exists_straddle_of_exclusiveOn
#print axioms exclusiveOn_factor
#print axioms substratumTheory_hasAncillaSwapControl
#print axioms substratumTheory_pureSeed
#print axioms substratumTheory_exclusivity_false
#print axioms inCell_add_outCell
#print axioms passive_repeatable_eq
#print axioms Reach.of_eq
#print axioms reach_pushPerm
#print axioms mergeInto_apply_left
#print axioms mergeInto_apply_right
#print axioms mergeInto_apply_of_ne
#print axioms exists_perm_sep
#print axioms step_eq_mergeInto
#print axioms reach_mergeInto
#print axioms collectAt_apply_self
#print axioms collectAt_apply_mem
#print axioms collectAt_apply_not_mem
#print axioms mergeInto_collectAt
#print axioms reach_collectAt
#print axioms collectAt_univ_apply
#print axioms sum_uniform
#print axioms reach_pointMass

end OriginExclusive
end OIBridge
