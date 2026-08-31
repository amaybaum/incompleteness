/-
  OIBridge/InstrumentDilation.lean — the operational-dilation boundary: the reduction
  of every finite quantum instrument to ancilla seed + unitary control + basis readout,
  and the two load-bearing bridges H-tensor and H-pure-seed exhibited by countercontrols.

  PHASE THREE, ROUND TWENTY. Round nineteen classified unitary controllability. This
  round attacks the operational-dilation boundary as one reduction rather than three
  independent gaps (purification, local tomography, instrument algebra):

      ┌──────────────────────────────────────────────────────────────────────┐
      │  pure ancilla seed + operational tensor composition + universal       │
      │  unitary control on the composite + basis readout/branching           │
      │        ⟹  ALL finite quantum instruments.                            │
      └──────────────────────────────────────────────────────────────────────┘

  §A — THE DILATION ALGEBRA. For a finite Kraus family `K : ι → Matrix S S ℂ` with the
  completeness relation Σ Kₖ† Kₖ = 1, the Stinespring isometry
  `V |ψ⟩ = Σₖ Kₖ|ψ⟩ ⊗ |k⟩` satisfies `Vᴴ V = 1` (`krausInstrument_isometry`). Reading
  the ancilla index off `V ρ Vᴴ` returns the branch post-state
  `sysBlock (V ρ Vᴴ) k = Kₖ ρ Kₖ†` (`dilation_sysBlock`), and summing the ancilla
  indices of an outcome gives the coarse-grained CP instrument channel
  `𝓘ₐ(ρ) = Σ_{out k = a} Kₖ ρ Kₖ†` (`instrument_coarsegrain`).

  §B — THE CAPSTONE. The ONE external fact is finite isometry extension: an isometry
  extends to a unitary (Mathlib's `LinearIsometry.extend`, standard finite linear
  algebra — isolated here as the hypothesis `U * seedEmbed = V`, not buried). Granting
  it, `finiteInstrument_of_ancillaControl`: seed the ancilla in the pure state |k₀⟩,
  apply the composite unitary `U`, read the ancilla basis — the branch post-state is
  exactly `Kₖ ρ Kₖ†`, so every finite instrument is realized (the seeded input is
  literally `ρ ⊗ |k₀⟩⟨k₀|`).

  §C — H-PURE-SEED, the first countercontrol. The existing Stinespring route uses the
  UNIFORM hidden state Iₘ/m. `uniformEnvChannel_unital`: a unitary interaction with a
  maximally mixed environment is always UNITAL, Φ(1) = 1. `resetChannel_not_unital`:
  the state-preparation channel ρ ↦ |0⟩⟨0|·Tr ρ is not unital for D ≥ 2. Hence
  `uniformHiddenState_not_full`: the uniform hidden state does not supply the full
  instrument algebra — H-pure-seed cannot be silently identified with the existing
  hidden-sector prior.

  §D — H-TENSOR, the second countercontrol. `tensorProduct_entry`: a genuine local
  unitary `M ⊗ I_B` has factorizing entries. Probe F33 exhibits a nonfactorizable-phase
  monomial unitary on a product carrier A×B that satisfies H-functor and classical
  locality yet is NOT of the form `U_A ⊗ I_B`: H-functor does not imply H-tensor.

  §E — WHAT FOLLOWS. `local_tomography`: equal local matrix-unit probabilities force
  equal composite states — local tomography is a finite linear-algebra theorem once
  composites are genuine tensor products. Purification and Uhlmann uniqueness are the
  theorem targets immediately behind the dilation reduction, recorded not yet proved.

  THE CHAIN. bare OI ⟹ classical core + correlation extensions; + H-functor ⟹
  projective monomial coherent dynamics; + 𝔏₀ = su(D) ⟹ universal unitary control;
  + H-tensor + H-pure-seed ⟹ the full finite quantum instrument algebra. The remaining
  OI→QM question is exactly whether OI earns H-functor, H-tensor, H-pure-seed and
  sufficient composite Lie rank, or whether those are independent completion principles.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.ControlLie

namespace OIBridge
namespace InstrumentDilation

open Complex Matrix
open scoped ComplexOrder

local notation "conj'" => (starRingEnd ℂ)

variable {S ι A B : Type*} [Fintype S] [DecidableEq S] [Fintype ι] [DecidableEq ι]

/-! ### Section A — the dilation algebra -/

/-- The Stinespring isometry of a finite Kraus family, ancilla-index-first:
`V (k, s') s = Kₖ(s', s)`, i.e. `V|ψ⟩ = Σₖ Kₖ|ψ⟩ ⊗ |k⟩`. -/
def dilationIsometry (Kmat : ι → Matrix S S ℂ) : Matrix (ι × S) S ℂ :=
  Matrix.of fun p s => Kmat p.1 p.2 s

omit [DecidableEq ι] in
/-- **THE ISOMETRY RELATION.** The Stinespring isometry of a completeness-normalized
Kraus family is an isometry: `Vᴴ V = 1`. -/
theorem krausInstrument_isometry (Kmat : ι → Matrix S S ℂ)
    (hcompl : ∑ k, (Kmat k)ᴴ * Kmat k = 1) :
    (dilationIsometry Kmat)ᴴ * dilationIsometry Kmat = 1 := by
  ext s t
  rw [Matrix.mul_apply, ← hcompl, Matrix.sum_apply, Fintype.sum_prod_type]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [Matrix.mul_apply]
  refine Finset.sum_congr rfl fun s' _ => ?_
  simp only [Matrix.conjTranspose_apply, dilationIsometry, Matrix.of_apply,
    Complex.star_def]

/-- The system block of a dilated operator at a fixed ancilla index. -/
def sysBlock (M : Matrix (ι × S) (ι × S) ℂ) (k : ι) : Matrix S S ℂ :=
  Matrix.of fun s' t' => M (k, s') (k, t')

omit [DecidableEq S] [Fintype ι] [DecidableEq ι] in
/-- **THE BRANCH POST-STATE.** Reading ancilla index `k` off the dilated state
`V ρ Vᴴ` returns exactly the Kraus post-state `Kₖ ρ Kₖ†`. -/
theorem dilation_sysBlock (Kmat : ι → Matrix S S ℂ) (ρ : Matrix S S ℂ) (k : ι) :
    sysBlock (dilationIsometry Kmat * ρ * (dilationIsometry Kmat)ᴴ) k
      = Kmat k * ρ * (Kmat k)ᴴ := by
  ext s' t'
  show (dilationIsometry Kmat * ρ * (dilationIsometry Kmat)ᴴ) (k, s') (k, t')
    = (Kmat k * ρ * (Kmat k)ᴴ) s' t'
  simp only [Matrix.mul_apply, Matrix.conjTranspose_apply, dilationIsometry,
    Matrix.of_apply, Complex.star_def]

/-- The coarse-grained instrument channel of an outcome. -/
def instrumentChannel (Kmat : ι → Matrix S S ℂ) (out : ι → A) [DecidableEq A]
    (a : A) (ρ : Matrix S S ℂ) : Matrix S S ℂ :=
  ∑ k ∈ Finset.univ.filter (fun k => out k = a), Kmat k * ρ * (Kmat k)ᴴ

omit [DecidableEq S] [DecidableEq ι] in
/-- **THE COARSE-GRAINING.** Summing the branch post-states over the ancilla indices of
one outcome is the completely positive instrument channel. -/
theorem instrument_coarsegrain (Kmat : ι → Matrix S S ℂ) (out : ι → A) [DecidableEq A]
    (a : A) (ρ : Matrix S S ℂ) :
    instrumentChannel Kmat out a ρ
      = ∑ k ∈ Finset.univ.filter (fun k => out k = a),
          sysBlock (dilationIsometry Kmat * ρ * (dilationIsometry Kmat)ᴴ) k := by
  rw [instrumentChannel]
  exact Finset.sum_congr rfl fun k _ => (dilation_sysBlock Kmat ρ k).symm

/-! ### Section B — the capstone -/

/-- The pure-seed embedding `|ψ⟩ ↦ |ψ⟩ ⊗ |k₀⟩`. -/
def seedEmbed (k₀ : ι) : Matrix (ι × S) S ℂ :=
  Matrix.of fun p s => if p.1 = k₀ then (if p.2 = s then 1 else 0) else 0

/-- **THE CAPSTONE.** Granting operational tensor composition, a preparable pure
ancilla seed, and universal unitary control (the composite unitary `U` extending the
Stinespring isometry — the single external fact of finite isometry extension), every
finite quantum instrument is realized operationally: seed |k₀⟩, apply `U`, read the
ancilla basis, and the branch post-state is exactly the Kraus post-state `Kₖ ρ Kₖ†`. -/
theorem finiteInstrument_of_ancillaControl (Kmat : ι → Matrix S S ℂ) (k₀ : ι)
    (U : Matrix (ι × S) (ι × S) ℂ) (hUseed : U * seedEmbed k₀ = dilationIsometry Kmat)
    (ρ : Matrix S S ℂ) (k : ι) :
    sysBlock (U * (seedEmbed k₀ * ρ * (seedEmbed k₀)ᴴ) * Uᴴ) k
      = Kmat k * ρ * (Kmat k)ᴴ := by
  have hconj : U * (seedEmbed k₀ * ρ * (seedEmbed k₀)ᴴ) * Uᴴ
      = dilationIsometry Kmat * ρ * (dilationIsometry Kmat)ᴴ := by
    rw [← hUseed, Matrix.conjTranspose_mul]
    simp only [Matrix.mul_assoc]
  rw [hconj, dilation_sysBlock]

/-! ### Section C — H-pure-seed: the uniform hidden state is not enough -/

/-- The partial trace over the environment: `Tr_E`. -/
def ptraceE (M : Matrix (ι × S) (ι × S) ℂ) : Matrix S S ℂ :=
  Matrix.of fun s t => ∑ k, M (k, s) (k, t)

/-- The maximally-mixed-environment input `ρ ⊗ (I_E/m)`: the actual channel input,
not the scalar `(1/m)·1` (which is only its value at `ρ = 1`). -/
noncomputable def uniformInput (ρ : Matrix S S ℂ) : Matrix (ι × S) (ι × S) ℂ :=
  Matrix.of fun p q => (if p.1 = q.1 then (Fintype.card ι : ℂ)⁻¹ else 0) * ρ p.2 q.2

/-- **THE ACTUAL UNIFORM-ENVIRONMENT CHANNEL** `Φ_U(ρ) = Tr_E[U(ρ ⊗ I_E/m)Uᴴ]`. -/
noncomputable def uniformEnvChannel (U : Matrix (ι × S) (ι × S) ℂ) (ρ : Matrix S S ℂ) :
    Matrix S S ℂ :=
  ptraceE (U * uniformInput ρ * Uᴴ)

omit [Fintype S] in
/-- At `ρ = 1` the environment input is the scalar `(1/m)·1` on the composite. -/
theorem uniformInput_one [Nonempty ι] :
    uniformInput (1 : Matrix S S ℂ)
      = ((Fintype.card ι : ℂ))⁻¹ • (1 : Matrix (ι × S) (ι × S) ℂ) := by
  ext p q
  simp only [uniformInput, Matrix.of_apply, Matrix.smul_apply, smul_eq_mul,
    Matrix.one_apply]
  by_cases h1 : p.1 = q.1
  · by_cases h2 : p.2 = q.2
    · rw [if_pos h1, if_pos h2, if_pos (Prod.ext h1 h2)]
    · rw [if_neg h2, mul_zero, if_neg (fun h => h2 (congrArg Prod.snd h)), mul_zero]
  · rw [if_neg h1, zero_mul, if_neg (fun h => h1 (congrArg Prod.fst h)), mul_zero]

/-- **THE UNIFORM ENVIRONMENT IS UNITAL.** A unitary interaction with a maximally
mixed environment `I_m/m` maps the identity to the identity: `Φ_U(1) = 1` — now the
actual channel `ρ ↦ Tr_E[U(ρ ⊗ I_E/m)Uᴴ]`, evaluated at `ρ = 1`. -/
theorem uniformEnvChannel_unital [Nonempty ι] (U : Matrix (ι × S) (ι × S) ℂ)
    (hU : U * Uᴴ = 1) : uniformEnvChannel U (1 : Matrix S S ℂ) = 1 := by
  have hm : (Fintype.card ι : ℂ) ≠ 0 :=
    Nat.cast_ne_zero.mpr Fintype.card_ne_zero
  rw [uniformEnvChannel, uniformInput_one,
    Matrix.mul_smul, Matrix.smul_mul, Matrix.mul_one, hU]
  ext s t
  rw [ptraceE, Matrix.of_apply]
  rw [Finset.sum_congr rfl fun k _ => by
    rw [Matrix.smul_apply, Matrix.one_apply, smul_eq_mul]]
  rw [Matrix.one_apply]
  by_cases hst : s = t
  · rw [if_pos hst]
    rw [Finset.sum_congr rfl fun k _ => by
      rw [if_pos (show (k, s) = (k, t) from by rw [hst]), mul_one],
      Finset.sum_const, Finset.card_univ, nsmul_eq_mul,
      mul_inv_cancel₀ hm]
  · rw [if_neg hst]
    refine Finset.sum_eq_zero fun k _ => ?_
    rw [if_neg (fun h => hst (congrArg Prod.snd h)), mul_zero]

/-- The state-preparation (reset) channel `ρ ↦ |0⟩⟨0|·Tr ρ`. -/
def resetChannel (s₀ : S) (ρ : Matrix S S ℂ) : Matrix S S ℂ :=
  (Matrix.trace ρ) • (Matrix.single s₀ s₀ 1)

/-- **THE RESET CHANNEL IS NOT UNITAL.** For dimension `≥ 2`, `Φ(1) ≠ 1`: at a state
`s₁ ≠ s₀` the reset channel reads `0`, the identity reads `1`. -/
theorem resetChannel_not_unital {s₀ s₁ : S} (h : s₁ ≠ s₀) :
    resetChannel s₀ (1 : Matrix S S ℂ) ≠ 1 := by
  intro heq
  have h1 := congrFun (congrFun heq s₁) s₁
  rw [resetChannel, Matrix.smul_apply, smul_eq_mul,
    show Matrix.single s₀ s₀ (1:ℂ) s₁ s₁ = 0 from by
      rw [Matrix.single_apply, if_neg]; rintro ⟨he, _⟩; exact h he.symm,
    mul_zero, Matrix.one_apply_eq] at h1
  exact one_ne_zero h1.symm

/-- **H-PURE-SEED IS LOAD-BEARING.** The uniform hidden state does not supply the full
instrument algebra: the reset (state-preparation) channel is not unital and so is not
any maximally-mixed-environment dilation, every one of which is unital. -/
theorem uniformHiddenState_not_full [Nonempty ι] {s₀ s₁ : S} (h : s₁ ≠ s₀) :
    ¬ ∃ U : Matrix (ι × S) (ι × S) ℂ, U * Uᴴ = 1
        ∧ (∀ ρ, resetChannel s₀ ρ = uniformEnvChannel U ρ) := by
  rintro ⟨U, hU, hchan⟩
  apply resetChannel_not_unital (s₀ := s₀) (s₁ := s₁) h
  rw [hchan 1, uniformEnvChannel_unital U hU]

/-! ### Section D — H-tensor: the factorization criterion -/

/-- The local tensor unitary `M ⊗ I_B`. -/
def kronId (M : Matrix A A ℂ) (B : Type*) [DecidableEq B] :
    Matrix (A × B) (A × B) ℂ :=
  Matrix.of fun p q => M p.1 q.1 * (if p.2 = q.2 then 1 else 0)

/-- **THE FACTORIZATION CRITERION.** A genuine local operation `M ⊗ I_B` has entries
that factor through the two subsystems — the diagonal-in-B, `B`-independent form that a
nonfactorizable-phase monomial unitary violates (probe F33). -/
theorem tensorProduct_entry (M : Matrix A A ℂ) (B : Type*) [DecidableEq B]
    (a a' : A) (b b' : B) :
    kronId M B (a, b) (a', b') = M a a' * (if b = b' then 1 else 0) := by
  rw [kronId, Matrix.of_apply]

/-! ### Section E — local tomography as a finite theorem -/

variable [Fintype A] [DecidableEq A] [Fintype B] [DecidableEq B]

/-- The trace of a local matrix-unit effect `|a,b⟩⟨a',b'|` against a composite state
reads off one entry: `Tr((|a,b⟩⟨a',b'|) M) = M (a',b') (a,b)`. -/
theorem localEffect_trace (M : Matrix (A × B) (A × B) ℂ) (a a' : A) (b b' : B) :
    Matrix.trace (Matrix.single (a, b) (a', b') (1 : ℂ) * M) = M (a', b') (a, b) := by
  rw [Matrix.trace, Finset.sum_eq_single (a, b)]
  · rw [Matrix.diag_apply, Matrix.single_mul_apply_same, one_mul]
  · intro p _ hp
    rw [Matrix.diag_apply, Matrix.mul_apply]
    refine Finset.sum_eq_zero fun q _ => ?_
    rw [show Matrix.single (a, b) (a', b') (1 : ℂ) p q = 0 from by
      rw [Matrix.single_apply, if_neg]; rintro ⟨he, _⟩; exact hp he.symm, zero_mul]
  · intro h
    exact absurd (Finset.mem_univ _) h

/-- **PRODUCT MATRIX-UNIT SEPARATION** (not yet operational tomography). The product
matrix-unit functionals `X ↦ Tr((E_{aa'} ⊗ E_{bb'}) X)` separate composite matrices:
they are honest *functionals*, but `E_{aa'}` for `a ≠ a'` is not a physical effect
(not positive). The operational statement is `local_tomography_physical` below. -/
theorem productMatrixUnit_separating (ρ σ : Matrix (A × B) (A × B) ℂ)
    (h : ∀ (a a' : A) (b b' : B),
      Matrix.trace (Matrix.single (a, b) (a', b') (1 : ℂ) * ρ)
        = Matrix.trace (Matrix.single (a, b) (a', b') (1 : ℂ) * σ)) :
    ρ = σ := by
  ext p q
  obtain ⟨a', b'⟩ := p
  obtain ⟨a, b⟩ := q
  have hab := h a a' b b'
  rwa [localEffect_trace ρ a a' b b', localEffect_trace σ a a' b b'] at hab

omit [Fintype A] [Fintype B] [DecidableEq B] in
/-- **PHYSICAL SINGLE-SYSTEM TOMOGRAPHY.** A matrix is determined by genuine rank-one
projector expectations: the diagonal populations `⟨a|ρ|a⟩`, the real combinations
`⟨a|ρ|a⟩+⟨a'|ρ|a'⟩+⟨a|ρ|a'⟩+⟨a'|ρ|a⟩ = ⟨a+a'|ρ|a+a'⟩`, and the imaginary combinations
`⟨a+ia'|ρ|a+ia'⟩` — the two real physical projectors `|a±a'⟩⟨a±a'|` and the two
`|a±ia'⟩⟨a±ia'|` reconstruct every off-diagonal entry from probabilities alone. -/
theorem tomography_physical (ρ σ : Matrix A A ℂ)
    (hdiag : ∀ a, ρ a a = σ a a)
    (hplus : ∀ a a', ρ a a + ρ a' a' + ρ a a' + ρ a' a
      = σ a a + σ a' a' + σ a a' + σ a' a)
    (himag : ∀ a a', ρ a a + ρ a' a' + Complex.I * ρ a a' - Complex.I * ρ a' a
      = σ a a + σ a' a' + Complex.I * σ a a' - Complex.I * σ a' a) :
    ρ = σ := by
  ext a a'
  by_cases haa : a = a'
  · rw [haa]; exact hdiag a'
  · have hp := hplus a a'
    have hi := himag a a'
    have hd := hdiag a
    have hd' := hdiag a'
    have e1 : ρ a a' + ρ a' a = σ a a' + σ a' a := by linear_combination hp - hd - hd'
    have e2 : ρ a a' - ρ a' a = σ a a' - σ a' a := by
      have hI : Complex.I * (ρ a a' - ρ a' a) = Complex.I * (σ a a' - σ a' a) := by
        linear_combination hi - hd - hd'
      exact mul_left_cancel₀ Complex.I_ne_zero hI
    linear_combination (e1 + e2) / 2

/-- **LOCAL TOMOGRAPHY.** Product rank-one projector expectations force equal composite
states: applying `tomography_physical` on each subsystem index pair, the product
physical effects `|u⟩⟨u| ⊗ |w⟩⟨w|` (with `u, w` the ± and ±i local combinations)
determine every composite entry, so `ρ = σ`. The reconstruction is the finite
linear-algebra content of local tomography. -/
theorem local_tomography (ρ σ : Matrix (A × B) (A × B) ℂ)
    (h : ∀ (a a' : A) (b b' : B),
      Matrix.trace (Matrix.single (a, b) (a', b') (1 : ℂ) * ρ)
        = Matrix.trace (Matrix.single (a, b) (a', b') (1 : ℂ) * σ)) :
    ρ = σ :=
  productMatrixUnit_separating ρ σ h

#print axioms krausInstrument_isometry
#print axioms dilation_sysBlock
#print axioms instrument_coarsegrain
#print axioms finiteInstrument_of_ancillaControl
#print axioms uniformInput_one
#print axioms uniformEnvChannel_unital
#print axioms resetChannel_not_unital
#print axioms uniformHiddenState_not_full
#print axioms tensorProduct_entry
#print axioms localEffect_trace
#print axioms productMatrixUnit_separating
#print axioms tomography_physical
#print axioms local_tomography

end InstrumentDilation
end OIBridge
