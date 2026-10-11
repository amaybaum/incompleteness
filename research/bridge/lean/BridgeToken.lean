/-
  OIBridge/BridgeToken.lean — design module of the research thread `research/bridge`
  (round 5, nodes B19 and B18). Not certified. Built on a disposable dev branch only; not for merge.

  Every statement here is about operational availability in the kernel's protocols (`InstAvail`,
  `availExt`); none is about the invariance of a pair cone.

    §A  (B19) pair availability is token availability. For a context-stable, label-invariant
        architecture, `PairAvailAt 𝓘 arch U n ↔ TokenAvailAt 𝓘 arch U n` at every level
        (`pairAvail_iff_tokenAvail`). token ⇒ pair (`pairAvail_of_tokenAvail`): the spectator rule
        (`instAvail_spectator`: context stability and label invariance) adjoins token A, and the
        transport rule (`instAvail_transport`: label invariance) relabels along the associator; the
        reindexed `1 ⊗ (U ⊗ 1ₙ)` is `(1 ⊗ U) ⊗ 1ₙ` entrywise (`reindex_assoc_tokOp`). pair ⇒ token
        (`tokenAvail_of_pairAvail`, label invariance only): the transport rule moves token A to the
        last factor (`toEnd`, `reindex_toEnd_pairOp`) and the discard rule (`InstAvail.discard`,
        `m = 2`) removes it, the discard of `conj (V ⊗ 1)` over a uniformly attached ancilla being
        `conj V` (`discard_two`, the kernel's `discard_tensorOf_one`).
    §B  (B18) the layer-flow chain without `SubstratumAvail`. The kernel's isolation identity
        (`gateFlow_isolation`, LiftAudit.lean:660) writes the transition flow on a chosen pair as
        `diagonal (phaseFun) · G · (D · G · D)`, `G` the executable layer flow and `D` a diagonal of
        signs. For an involution without fixed points the phase diagonal is a unimodular scalar
        (`diagonal_phaseFun_free`), which conjugation discards (`conjChannel_smul`); the sign
        diagonal is a product of squares of the quarter phases of `DerivedOI` (`signDiag_insert`,
        `signDiag_avail_of_phases`), the products available by the bind rule (`avail_conj_mul`). So
        `phaseFree_of_layerFlowExecutable_free` (sign diagonals and exchanges available ⇒ an
        executable fixed-point-free layer flow gives phase-free richness) and its `DerivedOI` form
        `phaseFree_of_layerFlowExecutable_derivedOI`; then the kernel's `control_of_phaseFree` and
        `derivedOI_qm_iff_phaseFree` give `control_of_layerFlowExecutable_derivedOI` and
        `derivedOI_qm_iff_layerFlowExecutable_free` — the analogue of LiftAudit.lean:812 with
        `SubstratumAvail` replaced by the fixed-point-free hypothesis. FM's instances: on the token
        carrier `Fin 2` with the exchange, and on the pair carrier `Fin 2 × Fin 2` with the exchange
        of the second token, an executable layer flow would give composite unitary control, hence
        both token operators (`layerFlow_supplies_token`) and both pair operators
        (`layerFlow_supplies_pair`), and exact QM (`latticeTheory_token_qm_iff_layerFlow`,
        `latticeTheory_pair_qm_iff_layerFlow`); in FM both sides of each biconditional are false
        (`latticeTheory_token_not_layerFlow`, `latticeTheory_pair_not_layerFlow`).

  Nothing here sources an operation, a pair cone, (A) or the transfer clause; no statement uses
  `SubstratumAvail`, `diagonal_avail` or `DrivesElementary`.

  Kernel check (dev branch):  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.BridgeAvailFull
import OIBridge.MinimalRepertoire
import OIBridge.LiftAudit
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace OIBridge
namespace BridgeToken

open Matrix MonoidalCompletion InterventionLocality StructuralClosure SubstratumInterface
  SubstratumInterfaceAudit MicroReversibility BridgeAvail BridgeAvailFull OperationalAssembly
  ReferenceExtension SpectatorBridge AncillaClosure RouteB

/-! ### §A — (B19) pair availability is token availability -/

section PairToken

variable {𝓘 : ImplementationClass} (arch : Architecture 𝓘)

/-- The associator, from the spectator carrier `Fin 2 × (Fin 2 × Fin n)` to the pair carrier
`(Fin 2 × Fin 2) × Fin n`. -/
def assocPair (n : ℕ) : Fin 2 × (Fin 2 × Fin n) ≃ (Fin 2 × Fin 2) × Fin n :=
  (Equiv.prodAssoc (Fin 2) (Fin 2) (Fin n)).symm

theorem assocPair_symm_apply (n : ℕ) (p : (Fin 2 × Fin 2) × Fin n) :
    (assocPair n).symm p = (p.1.1, (p.1.2, p.2)) := by
  first
  | rfl
  | simp [assocPair]

/-- The reindexed `1 ⊗ (U ⊗ 1ₙ)` is `(1 ⊗ U) ⊗ 1ₙ`. -/
theorem reindex_assoc_tokOp (U : Matrix (Fin 2) (Fin 2) ℂ) (n : ℕ) :
    Matrix.reindex (assocPair n) (assocPair n)
        (tensorOf (1 : Matrix (Fin 2) (Fin 2) ℂ) (tokOp U n)) = pairOp U n := by
  ext ⟨⟨a, b⟩, k⟩ ⟨⟨a', b'⟩, k'⟩
  simp only [Matrix.reindex_apply, Matrix.submatrix_apply, assocPair_symm_apply, pairOp, tokOp,
    tensorOf_apply]
  first
  | ring
  | (rw [mul_assoc])
  | simp [mul_assoc]

/-- **TOKEN ⇒ PAIR**: for a context-stable, label-invariant architecture, a token operator
available on the token alone is available on the pair (the spectator rule, then the transport rule
along the associator). -/
theorem pairAvail_of_tokenAvail (hc : ContextStable 𝓘) (hl : LabelInvariant 𝓘)
    {U : Matrix (Fin 2) (Fin 2) ℂ} {n : ℕ} (h : TokenAvailAt 𝓘 arch U n) :
    PairAvailAt 𝓘 arch U n := by
  have h1 : InstAvail 𝓘 (Fin 2 × Fin n) Unit (fun _ => conjChannel (tokOp U n)) := h
  have h2 := instAvail_spectator hc hl (Fin 2) h1
  have h3 := instAvail_transport hl h2 ((Fin 2 × Fin 2) × Fin n) (assocPair n)
  show InstAvail 𝓘 ((Fin 2 × Fin 2) × Fin n) Unit (fun _ => conjChannel (pairOp U n))
  first
  | simpa only [amplRefL_conjChannel, transport_conjChannel, reindex_assoc_tokOp] using h3
  | (have e3 : (fun _ : Unit => transport (assocPair n)
        (amplRefL (Fin 2) (conjChannel (tokOp U n))))
        = fun _ : Unit => conjChannel (pairOp U n) := by
       funext _
       rw [amplRefL_conjChannel, transport_conjChannel, reindex_assoc_tokOp]
     rw [← e3]
     exact h3)

/-- The relabelling of the pair carrier that moves token A to the last factor. -/
def toEnd (n : ℕ) : (Fin 2 × Fin 2) × Fin n ≃ (Fin 2 × Fin n) × Fin 2 where
  toFun p := ((p.1.2, p.2), p.1.1)
  invFun q := ((q.2, q.1.1), q.1.2)
  left_inv := fun ⟨⟨_, _⟩, _⟩ => rfl
  right_inv := fun ⟨⟨_, _⟩, _⟩ => rfl

theorem toEnd_symm_apply (n : ℕ) (q : (Fin 2 × Fin n) × Fin 2) :
    (toEnd n).symm q = ((q.2, q.1.1), q.1.2) := rfl

/-- The relabelled `(1 ⊗ U) ⊗ 1ₙ` is `(U ⊗ 1ₙ) ⊗ 1₂`. -/
theorem reindex_toEnd_pairOp (U : Matrix (Fin 2) (Fin 2) ℂ) (n : ℕ) :
    Matrix.reindex (toEnd n) (toEnd n) (pairOp U n)
      = tensorOf (tokOp U n) (1 : Matrix (Fin 2) (Fin 2) ℂ) := by
  ext ⟨⟨b, k⟩, a⟩ ⟨⟨b', k'⟩, a'⟩
  simp only [Matrix.reindex_apply, Matrix.submatrix_apply, toEnd_symm_apply, pairOp, tokOp,
    tensorOf_apply]
  first
  | ring
  | simp [mul_assoc, mul_comm, mul_left_comm]

/-- The discard of `conj (V ⊗ 1₂)` over a uniformly attached two-level ancilla is `conj V`
(the kernel's `discard_tensorOf_one` at `m + 1 = 2`). -/
theorem discard_two {n : ℕ} (V : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ) :
    discardWith (A := Fin 2 × Fin n) 2 (uniformAttach 2)
        (conjChannel (tensorOf V (1 : Matrix (Fin 2) (Fin 2) ℂ))) = conjChannel V := by
  first
  | exact MinimalRepertoire.discard_tensorOf_one (m := 1) V
  | (rw [discardWith_uniform_conjChannel]
     have hc : ∀ f e : Fin 2,
         conjChannel (ancBlock (tensorOf V (1 : Matrix (Fin 2) (Fin 2) ℂ)) f e)
           = if f = e then conjChannel V else 0 := by
       intro f e
       rw [MinimalRepertoire.ancBlock_tensorOf_one]
       split_ifs <;> simp [MinimalRepertoire.conjChannel_zero]
     simp only [hc, Fintype.sum_prod_type, Finset.sum_ite_eq, Finset.mem_univ, if_true,
       Finset.sum_const, Finset.card_univ, Fintype.card_fin]
     rw [← Nat.cast_smul_eq_nsmul ℂ, smul_smul,
       inv_mul_cancel₀ (by norm_num : ((2 : ℕ) : ℂ) ≠ 0), one_smul])

/-- **PAIR ⇒ TOKEN**: for a label-invariant class, a token operator available on the pair is
available on the token alone (the transport rule moving token A to the last factor, then the discard
rule). Context stability is not used. -/
theorem tokenAvail_of_pairAvail (hl : LabelInvariant 𝓘) {U : Matrix (Fin 2) (Fin 2) ℂ} {n : ℕ}
    (h : PairAvailAt 𝓘 arch U n) : TokenAvailAt 𝓘 arch U n := by
  have h1 : InstAvail 𝓘 ((Fin 2 × Fin 2) × Fin n) Unit (fun _ => conjChannel (pairOp U n)) := h
  have h2 := instAvail_transport hl h1 ((Fin 2 × Fin n) × Fin 2) (toEnd n)
  have h2' : InstAvail 𝓘 ((Fin 2 × Fin n) × Fin 2) Unit
      (fun _ => conjChannel (tensorOf (tokOp U n) (1 : Matrix (Fin 2) (Fin 2) ℂ))) := by
    first
    | simpa only [transport_conjChannel, reindex_toEnd_pairOp] using h2
    | (have e2 : (fun _ : Unit => transport (toEnd n) (conjChannel (pairOp U n)))
          = fun _ : Unit => conjChannel (tensorOf (tokOp U n) (1 : Matrix (Fin 2) (Fin 2) ℂ)) := by
         funext _
         rw [transport_conjChannel, reindex_toEnd_pairOp]
       rw [← e2]
       exact h2)
  have h3 := InstAvail.discard (𝓘 := 𝓘) (by norm_num : (0 : ℕ) < 2) h2'
  show InstAvail 𝓘 (Fin 2 × Fin n) Unit (fun _ => conjChannel (tokOp U n))
  first
  | simpa only [discard_two] using h3
  | (have e3 : (fun _ : Unit => discardWith (A := Fin 2 × Fin n) 2 (uniformAttach 2)
        (conjChannel (tensorOf (tokOp U n) (1 : Matrix (Fin 2) (Fin 2) ℂ))))
        = fun _ : Unit => conjChannel (tokOp U n) := by
       funext _
       rw [discard_two]
     rw [← e3]
     exact h3)

/-- **PAIR AVAILABILITY IS TOKEN AVAILABILITY** for a context-stable, label-invariant
architecture, at every level. -/
theorem pairAvail_iff_tokenAvail (hc : ContextStable 𝓘) (hl : LabelInvariant 𝓘)
    (U : Matrix (Fin 2) (Fin 2) ℂ) (n : ℕ) : PairAvailAt 𝓘 arch U n ↔ TokenAvailAt 𝓘 arch U n :=
  ⟨tokenAvail_of_pairAvail arch hl, pairAvail_of_tokenAvail arch hc hl⟩

end PairToken

/-! ### §B — (B18) the layer-flow chain without `SubstratumAvail` -/

section LayerFlow

open LiftAudit

variable {S : Type} [Fintype S] [DecidableEq S]

/-- The sign diagonal of a set of configurations: `−1` on the set, `1` elsewhere. -/
def signDiag {T : Type} [DecidableEq T] (F : Finset T) : Matrix T T ℂ :=
  Matrix.diagonal fun p => if p ∈ F then -1 else 1

theorem signDiag_empty {T : Type} [DecidableEq T] : signDiag (∅ : Finset T) = 1 := by
  unfold signDiag
  rw [← Matrix.diagonal_one]
  congr 1
  first
  | done
  | (funext p
     show (if p ∈ (∅ : Finset T) then (-1 : ℂ) else 1) = 1
     rw [if_neg (Finset.notMem_empty p)])

/-- Adjoining a configuration to the sign set multiplies by the square of its quarter phase. -/
theorem signDiag_insert {T : Type} [Fintype T] [DecidableEq T] {F : Finset T} {p : T} (hp : p ∉ F) :
    signDiag (insert p F) = LieRankSource.phaseGate p * LieRankSource.phaseGate p * signDiag F := by
  unfold signDiag LieRankSource.phaseGate
  simp only [Matrix.diagonal_mul_diagonal]
  congr 1
  funext q
  by_cases hq : q = p
  · subst hq
    first
    | simp [hp, Complex.I_mul_I]
    | (show (if q ∈ insert q F then (-1 : ℂ) else 1)
          = (if q = q then Complex.I else 1) * (if q = q then Complex.I else 1)
            * (if q ∈ F then -1 else 1)
       rw [if_pos (Finset.mem_insert_self q F), if_pos rfl, if_neg hp, Complex.I_mul_I, mul_one])
  · have hpq : ¬ p = q := fun h => hq h.symm
    first
    | simp [Finset.mem_insert, hq, hpq]
    | (show (if q ∈ insert p F then (-1 : ℂ) else 1)
          = (if p = q then Complex.I else 1) * (if p = q then Complex.I else 1)
            * (if q ∈ F then -1 else 1)
       rw [if_neg hpq, one_mul, one_mul]
       congr 1
       simp [Finset.mem_insert, hq])

/-- The fourth power of a quarter phase is the identity. -/
theorem phaseGate_fourth {T : Type} [Fintype T] [DecidableEq T] (a : T) :
    LieRankSource.phaseGate a * LieRankSource.phaseGate a
        * (LieRankSource.phaseGate a * LieRankSource.phaseGate a) = 1 := by
  unfold LieRankSource.phaseGate
  simp only [Matrix.diagonal_mul_diagonal]
  rw [← Matrix.diagonal_one]
  congr 1
  funext p
  split_ifs <;> first | norm_num [Complex.I_mul_I] | simp [Complex.I_mul_I]

/-- **THE SIGN DIAGONALS ARE AVAILABLE WHEREVER THE QUARTER PHASES ARE**: by induction over the
sign set, each step the square of a quarter phase, composed by the bind rule (`avail_conj_mul`); the
empty sign set is the fourth power of one quarter phase. -/
theorem signDiag_avail_of_phases (T : FiniteOperationalTheory S) (hph : PhasesAvailable T) (n : ℕ)
    (a₀ : S × Fin n) (F : Finset (S × Fin n)) :
    T.availExt n Unit (fun _ => conjChannel (signDiag F)) := by
  induction F using Finset.induction_on with
  | empty =>
    rw [signDiag_empty]
    have h1 := hph n a₀
    have h2 := avail_conj_mul T n (avail_conj_mul T n h1 h1) (avail_conj_mul T n h1 h1)
    rwa [phaseGate_fourth] at h2
  | insert p F hp ih =>
    rw [signDiag_insert hp]
    exact avail_conj_mul T n (avail_conj_mul T n (hph n p) (hph n p)) ih

theorem signFun_pm (τ : Equiv.Perm S) (e : S ≃ Fin (Fintype.card S)) (a z : S) :
    signFun τ e a z = 1 ∨ signFun τ e a z = -1 := by
  unfold signFun
  split_ifs <;> first | exact Or.inl rfl | exact Or.inr rfl

/-- The configurations where the kernel's sign `signFun` is `−1`. -/
def signSet (τ : Equiv.Perm S) (e : S ≃ Fin (Fintype.card S)) (a : S) : Finset S :=
  Finset.univ.filter fun z => τ z ≠ z ∧ ¬ (z = a ∨ z = τ a) ∧ e z < e (τ z)

/-- The kernel's sign diagonal is the sign diagonal of its sign set. -/
theorem diagonal_signFun_eq (τ : Equiv.Perm S) (e : S ≃ Fin (Fintype.card S)) (a : S) :
    Matrix.diagonal (signFun τ e a) = signDiag (signSet τ e a) := by
  unfold signDiag
  congr 1
  funext z
  show signFun τ e a z = if z ∈ signSet τ e a then -1 else 1
  by_cases hz : z ∈ signSet τ e a
  · have hc : τ z ≠ z ∧ ¬ (z = a ∨ z = τ a) ∧ e z < e (τ z) := (Finset.mem_filter.mp hz).2
    rw [if_pos hz]
    unfold signFun
    rw [if_pos hc]
  · have hc : ¬ (τ z ≠ z ∧ ¬ (z = a ∨ z = τ a) ∧ e z < e (τ z)) :=
      fun h => hz (Finset.mem_filter.mpr ⟨Finset.mem_univ z, h⟩)
    rw [if_neg hz]
    unfold signFun
    rw [if_neg hc]

/-- For an involution without fixed points the kernel's phase diagonal is a unimodular scalar. -/
theorem diagonal_phaseFun_free {τ : Equiv.Perm S} (hfree : ∀ z, τ z ≠ z) (s : ℝ) (a : S) :
    Matrix.diagonal (phaseFun τ s) = phaseFun τ s a • (1 : Matrix S S ℂ) := by
  have hval : ∀ z, phaseFun τ s z = phaseFun τ s a := by
    intro z
    unfold phaseFun
    rw [if_neg (hfree z), if_neg (hfree a)]
  ext i j
  rw [Matrix.diagonal_apply, Matrix.smul_apply, Matrix.one_apply, hval i]
  split_ifs <;> simp

theorem phaseFun_mul_star {τ : Equiv.Perm S} (s : ℝ) (a : S) :
    phaseFun τ s a * star (phaseFun τ s a) = 1 := by
  rw [mul_comm]
  exact phaseFun_star s a

/-- **PHASE-FREE RICHNESS FROM AN EXECUTABLE FIXED-POINT-FREE LAYER FLOW**, with the sign diagonals
and the exchanges available and nothing else at a general angle: the kernel's isolation identity,
its phase a unimodular scalar that conjugation discards, its sign diagonal a sign set. -/
theorem phaseFree_of_layerFlowExecutable_free (T : FiniteOperationalTheory S)
    (hsign : ∀ (n : ℕ), (S × Fin n) → ∀ F : Finset (S × Fin n),
      T.availExt n Unit (fun _ => conjChannel (signDiag F)))
    (hswap : ∀ (n : ℕ) (a b : S × Fin n),
      T.availExt n Unit (fun _ => conjChannel (CoherentLift.permMatrix (Equiv.swap a b))))
    {σ : Equiv.Perm S} (hσ : ∀ x, σ (σ x) = x) (hfree : ∀ x, σ x ≠ x)
    (hex : LayerFlowExecutable T σ) : MinimalRepertoire.PhaseFreeRichness T := by
  intro n hn
  obtain ⟨a, -, -⟩ := (Fintype.one_lt_card_iff (α := S × Fin n)).mp (by omega)
  set τ := levelPerm σ n with hτdef
  have hτ : ∀ p, τ (τ p) = p := levelPerm_involutive hσ n
  have hτfree : ∀ p, τ p ≠ p := by
    intro p h
    rw [hτdef, levelPerm_apply] at h
    exact hfree p.1 (congrArg Prod.fst h)
  have ha : τ a ≠ a := hτfree a
  refine ⟨⟨a, τ a, ha.symm, fun t => ?_⟩, fun p q _ => hswap n p q⟩
  have hπ : Real.pi * (t / Real.pi) = t := mul_div_cancel₀ _ Real.pi_ne_zero
  have hD := hsign n a (signSet τ (Fintype.equivFin (S × Fin n)) a)
  have hG := hex n (t / Real.pi)
  have hunit : phaseFun τ (t / Real.pi) a * star (phaseFun τ (t / Real.pi) a) = 1 :=
    phaseFun_mul_star (t / Real.pi) a
  rw [← hπ, ← gateFlow_isolation hτ ha (Fintype.equivFin (S × Fin n)) (t / Real.pi),
    diagonal_phaseFun_free hτfree (t / Real.pi) a, Matrix.smul_mul, Matrix.one_mul, Matrix.smul_mul,
    conjChannel_smul, hunit, one_smul, diagonal_signFun_eq]
  exact avail_conj_mul T n hG (avail_conj_mul T n (avail_conj_mul T n hD hG) hD)

/-- **THE `DerivedOI` FORM**: the quarter phases and the exchanges of `DerivedOI` supply the sign
diagonals and the exchanges. -/
theorem phaseFree_of_layerFlowExecutable_derivedOI (T : FiniteOperationalTheory S)
    (hd : DerivedOI T) {σ : Equiv.Perm S} (hσ : ∀ x, σ (σ x) = x) (hfree : ∀ x, σ x ≠ x)
    (hex : LayerFlowExecutable T σ) : MinimalRepertoire.PhaseFreeRichness T :=
  phaseFree_of_layerFlowExecutable_free T
    (fun n a₀ F => signDiag_avail_of_phases T hd.2.2.2.1 n a₀ F) hd.2.2.1 hσ hfree hex

/-- **CONTROL FROM AN EXECUTABLE FIXED-POINT-FREE LAYER FLOW UNDER `DerivedOI`**, through the
kernel's `control_of_phaseFree` with the closure `DerivedOI` carries. -/
theorem control_of_layerFlowExecutable_derivedOI [Nonempty S] (T : FiniteOperationalTheory S)
    (hd : DerivedOI T) {σ : Equiv.Perm S} (hσ : ∀ x, σ (σ x) = x) (hfree : ∀ x, σ x ≠ x)
    (hex : LayerFlowExecutable T σ) : HasCompositeUnitaryControl T :=
  MinimalRepertoire.control_of_phaseFree T (RouteB.DerivedOI.closure hd)
    (phaseFree_of_layerFlowExecutable_derivedOI T hd hσ hfree hex)

/-- **THE ENDPOINT WITHOUT `SubstratumAvail`**: under `DerivedOI`, exact quantum mechanics is exactly
the executability of one fixed-point-free layer involution. -/
theorem derivedOI_qm_iff_layerFlowExecutable_free [Nonempty S] (T : FiniteOperationalTheory S)
    (hd : DerivedOI T) {σ : Equiv.Perm S} (hσ : ∀ x, σ (σ x) = x) (hfree : ∀ x, σ x ≠ x) :
    LevelOneSeam.ExactAllFiniteEndomorphicQuantumOps T ↔ LayerFlowExecutable T σ :=
  ⟨fun hqm => layerFlowExecutable_of_control T
      (PhysicalCharacterization.physical_of_exactAll T hqm).2.2.1 hσ,
    fun hex => (derivedOI_qm_iff_phaseFree hd).mpr
      (phaseFree_of_layerFlowExecutable_derivedOI T hd hσ hfree hex)⟩

/-! FM's instances. -/

theorem latticeTheory_phaseFree_of_layerFlow {σ : Equiv.Perm S} (hσ : ∀ x, σ (σ x) = x)
    (hfree : ∀ x, σ x ≠ x) (hex : LayerFlowExecutable (latticeTheory S) σ) :
    MinimalRepertoire.PhaseFreeRichness (latticeTheory S) :=
  phaseFree_of_layerFlowExecutable_derivedOI _ (latticeTheory_derivedOI S) hσ hfree hex

theorem latticeTheory_control_of_layerFlow [Nonempty S] {σ : Equiv.Perm S}
    (hσ : ∀ x, σ (σ x) = x) (hfree : ∀ x, σ x ≠ x)
    (hex : LayerFlowExecutable (latticeTheory S) σ) : HasCompositeUnitaryControl (latticeTheory S) :=
  control_of_layerFlowExecutable_derivedOI _ (latticeTheory_derivedOI S) hσ hfree hex

theorem latticeTheory_qm_iff_layerFlowExecutable [Nonempty S] {σ : Equiv.Perm S}
    (hσ : ∀ x, σ (σ x) = x) (hfree : ∀ x, σ x ≠ x) :
    LevelOneSeam.ExactAllFiniteEndomorphicQuantumOps (latticeTheory S)
      ↔ LayerFlowExecutable (latticeTheory S) σ :=
  derivedOI_qm_iff_layerFlowExecutable_free _ (latticeTheory_derivedOI S) hσ hfree

theorem swap01_involutive (x : Fin 2) :
    Equiv.swap (0 : Fin 2) 1 (Equiv.swap (0 : Fin 2) 1 x) = x :=
  Equiv.swap_apply_self 0 1 x

theorem swap01_free (x : Fin 2) : Equiv.swap (0 : Fin 2) 1 x ≠ x := by
  fin_cases x <;> first | decide | simp [Equiv.swap_apply_def] | simp

/-- The exchange of the second token on the pair carrier. -/
def pairSwap : Equiv.Perm (Fin 2 × Fin 2) :=
  (Equiv.refl (Fin 2)).prodCongr (Equiv.swap (0 : Fin 2) 1)

theorem pairSwap_apply (p : Fin 2 × Fin 2) : pairSwap p = (p.1, Equiv.swap (0 : Fin 2) 1 p.2) := rfl

theorem pairSwap_involutive (p : Fin 2 × Fin 2) : pairSwap (pairSwap p) = p := by
  obtain ⟨a, b⟩ := p
  show (a, Equiv.swap (0 : Fin 2) 1 (Equiv.swap (0 : Fin 2) 1 b)) = (a, b)
  rw [Equiv.swap_apply_self]

theorem pairSwap_free (p : Fin 2 × Fin 2) : pairSwap p ≠ p := by
  intro h
  rw [pairSwap_apply] at h
  exact swap01_free p.2 (congrArg Prod.snd h)

/-- **THE TOKEN CARRIER**: an executable layer flow of the exchange would give FM composite unitary
control on `Fin 2`. -/
theorem latticeTheory_token_control_of_layerFlow
    (hex : LayerFlowExecutable (latticeTheory (Fin 2)) (Equiv.swap (0 : Fin 2) 1)) :
    HasCompositeUnitaryControl (latticeTheory (Fin 2)) :=
  latticeTheory_control_of_layerFlow swap01_involutive swap01_free hex

/-- …hence both token operators at every level — the conclusion itself. -/
theorem layerFlow_supplies_token
    (hex : LayerFlowExecutable (latticeTheory (Fin 2)) (Equiv.swap (0 : Fin 2) 1)) (n : ℕ) :
    TokenAvailAt latticeClass latticeClass_arch zPh n
      ∧ TokenAvailAt latticeClass latticeClass_arch uJ n := by
  have h := latticeTheory_token_control_of_layerFlow hex
  constructor
  · unfold TokenAvailAt
    exact h n _ (tokOp_isometry zPh_unitary n)
  · unfold TokenAvailAt
    exact h n _ (tokOp_isometry uJ_unitary n)

/-- **THE PAIR CARRIER**: an executable layer flow of the second token's exchange would give FM
composite unitary control on `Fin 2 × Fin 2`. -/
theorem latticeTheory_pair_control_of_layerFlow
    (hex : LayerFlowExecutable (latticeTheory (Fin 2 × Fin 2)) pairSwap) :
    HasCompositeUnitaryControl (latticeTheory (Fin 2 × Fin 2)) :=
  latticeTheory_control_of_layerFlow pairSwap_involutive pairSwap_free hex

/-- …hence both pair operators at every level. -/
theorem layerFlow_supplies_pair
    (hex : LayerFlowExecutable (latticeTheory (Fin 2 × Fin 2)) pairSwap) (n : ℕ) :
    PairAvailAt latticeClass latticeClass_arch zPh n
      ∧ PairAvailAt latticeClass latticeClass_arch uJ n :=
  pairAvail_of_control (latticeTheory_pair_control_of_layerFlow hex) n

/-- The biconditional of I2.34 for FM on the token carrier, without `SubstratumAvail`. -/
theorem latticeTheory_token_qm_iff_layerFlow :
    LevelOneSeam.ExactAllFiniteEndomorphicQuantumOps (latticeTheory (Fin 2))
      ↔ LayerFlowExecutable (latticeTheory (Fin 2)) (Equiv.swap (0 : Fin 2) 1) :=
  latticeTheory_qm_iff_layerFlowExecutable swap01_involutive swap01_free

/-- The biconditional of I2.34 for FM on the pair carrier, without `SubstratumAvail`. -/
theorem latticeTheory_pair_qm_iff_layerFlow :
    LevelOneSeam.ExactAllFiniteEndomorphicQuantumOps (latticeTheory (Fin 2 × Fin 2))
      ↔ LayerFlowExecutable (latticeTheory (Fin 2 × Fin 2)) pairSwap :=
  latticeTheory_qm_iff_layerFlowExecutable pairSwap_involutive pairSwap_free

/-- Consistency: in FM both sides of each biconditional are false. -/
theorem latticeTheory_token_not_layerFlow :
    ¬ LayerFlowExecutable (latticeTheory (Fin 2)) (Equiv.swap (0 : Fin 2) 1) :=
  latticeTheory_not_layerFlowExecutable (swap01_free 0)

theorem latticeTheory_pair_not_layerFlow :
    ¬ LayerFlowExecutable (latticeTheory (Fin 2 × Fin 2)) pairSwap :=
  latticeTheory_not_layerFlowExecutable (pairSwap_free (0, 0))

end LayerFlow

#print axioms assocPair_symm_apply
#print axioms reindex_assoc_tokOp
#print axioms pairAvail_of_tokenAvail
#print axioms toEnd_symm_apply
#print axioms reindex_toEnd_pairOp
#print axioms discard_two
#print axioms tokenAvail_of_pairAvail
#print axioms pairAvail_iff_tokenAvail
#print axioms signDiag_empty
#print axioms signDiag_insert
#print axioms phaseGate_fourth
#print axioms signDiag_avail_of_phases
#print axioms signFun_pm
#print axioms diagonal_signFun_eq
#print axioms diagonal_phaseFun_free
#print axioms phaseFun_mul_star
#print axioms phaseFree_of_layerFlowExecutable_free
#print axioms phaseFree_of_layerFlowExecutable_derivedOI
#print axioms control_of_layerFlowExecutable_derivedOI
#print axioms derivedOI_qm_iff_layerFlowExecutable_free
#print axioms latticeTheory_phaseFree_of_layerFlow
#print axioms latticeTheory_control_of_layerFlow
#print axioms latticeTheory_qm_iff_layerFlowExecutable
#print axioms swap01_involutive
#print axioms swap01_free
#print axioms pairSwap_apply
#print axioms pairSwap_involutive
#print axioms pairSwap_free
#print axioms latticeTheory_token_control_of_layerFlow
#print axioms layerFlow_supplies_token
#print axioms latticeTheory_pair_control_of_layerFlow
#print axioms layerFlow_supplies_pair
#print axioms latticeTheory_token_qm_iff_layerFlow
#print axioms latticeTheory_pair_qm_iff_layerFlow
#print axioms latticeTheory_token_not_layerFlow
#print axioms latticeTheory_pair_not_layerFlow

end BridgeToken
end OIBridge
