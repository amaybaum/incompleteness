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

  §E/§F — WHAT FOLLOWS. Two statements, kept apart on purpose.
  `productMatrixUnit_local_separating` says equal local MATRIX-UNIT functionals force
  equal composite states; those functionals are not physical effects, so that is
  separation, not tomography. `local_tomography_physical` is the operational statement:
  equal probabilities for every PRODUCT rank-one effect `|u⟩⟨u| ⊗ |v⟩⟨v|` force equal
  composite states, proved by running complex polarization
  (`eq_zero_of_form_vanishes`) once on each factor — no entangled effect and no matrix
  unit is used anywhere. Purification and Uhlmann uniqueness are the theorem targets
  immediately behind the dilation reduction, recorded not yet proved.

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

/-- **PRODUCT MATRIX-UNIT LOCAL SEPARATION** (still not operational tomography). Identical
to `productMatrixUnit_separating`, recorded under the name the composite statement used to
carry. Its hypothesis is equality against `E_{aa'} ⊗ E_{bb'}`, which are FUNCTIONALS and
not physical effects; the operational statement is `local_tomography_physical` below. -/
theorem productMatrixUnit_local_separating (ρ σ : Matrix (A × B) (A × B) ℂ)
    (h : ∀ (a a' : A) (b b' : B),
      Matrix.trace (Matrix.single (a, b) (a', b') (1 : ℂ) * ρ)
        = Matrix.trace (Matrix.single (a, b) (a', b') (1 : ℂ) * σ)) :
    ρ = σ :=
  productMatrixUnit_separating ρ σ h

/-! ### Section F — physical local tomography -/

omit [Fintype A] [DecidableEq A] [Fintype B] [DecidableEq B] in
/-- The sesquilinear form of a matrix, expanded. -/
theorem form_expand {P : Type*} [Fintype P] (M : Matrix P P ℂ) (x y : P → ℂ) :
    star x ⬝ᵥ M.mulVec y = ∑ u, ∑ v, conj' (x u) * M u v * y v := by
  rw [dotProduct]
  refine Finset.sum_congr rfl fun u _ => ?_
  rw [Pi.star_apply, Complex.star_def, Matrix.mulVec, dotProduct, Finset.mul_sum]
  exact Finset.sum_congr rfl fun v _ => by ring

omit [Fintype A] [DecidableEq A] [Fintype B] [DecidableEq B] in
/-- **COMPLEX POLARIZATION.** Over `ℂ` a sesquilinear form that vanishes on every vector
has zero matrix — no Hermiticity assumption is needed. The `x + y` and `x + iy` probes are
exactly the `±` and `±i` physical rank-one effects of `tomography_physical`, here in
basis-free form. -/
theorem eq_zero_of_form_vanishes {P : Type*} [Fintype P] [DecidableEq P]
    (M : Matrix P P ℂ) (h : ∀ x : P → ℂ, star x ⬝ᵥ M.mulVec x = 0) : M = 0 := by
  have hbil : ∀ x y : P → ℂ,
      star x ⬝ᵥ M.mulVec y + star y ⬝ᵥ M.mulVec x = 0 := by
    intro x y
    have hxy := h (x + y)
    rw [Matrix.mulVec_add, star_add, add_dotProduct, dotProduct_add, dotProduct_add,
      h x, h y] at hxy
    linear_combination hxy
  have hcross : ∀ x y : P → ℂ, star x ⬝ᵥ M.mulVec y = 0 := by
    intro x y
    have h1 := hbil x y
    have h2 := hbil x (Complex.I • y)
    rw [Matrix.mulVec_smul, dotProduct_smul, star_smul, smul_dotProduct,
      Complex.star_def, Complex.conj_I, smul_eq_mul, smul_eq_mul] at h2
    have h3 : star x ⬝ᵥ M.mulVec y = star y ⬝ᵥ M.mulVec x := by
      have := mul_left_cancel₀ Complex.I_ne_zero
        (show Complex.I * (star x ⬝ᵥ M.mulVec y)
          = Complex.I * (star y ⬝ᵥ M.mulVec x) by linear_combination h2)
      exact this
    linear_combination (h1 + h3) / 2
  ext p q
  rw [Matrix.zero_apply, ← CoherentExtension.form_basis M p q]
  exact hcross _ _

/-- The product rank-one effect `|u⟩⟨u| ⊗ |v⟩⟨v|` — a genuine physical effect, unlike a
matrix unit. -/
def prodProj (u : A → ℂ) (v : B → ℂ) : Matrix (A × B) (A × B) ℂ :=
  Matrix.of fun p q => (u p.1 * conj' (u q.1)) * (v p.2 * conj' (v q.2))

/-- The product vector `u ⊗ v`. -/
def prodVec (u : A → ℂ) (v : B → ℂ) : A × B → ℂ := fun p => u p.1 * v p.2

omit [DecidableEq A] [DecidableEq B] in
/-- The expectation of a product rank-one effect is the sesquilinear form at `u ⊗ v`. -/
theorem prodProj_trace (u : A → ℂ) (v : B → ℂ) (D : Matrix (A × B) (A × B) ℂ) :
    Matrix.trace (prodProj u v * D)
      = star (prodVec u v) ⬝ᵥ D.mulVec (prodVec u v) := by
  rw [form_expand, Matrix.trace]
  rw [show (∑ p, (prodProj u v * D).diag p)
      = ∑ p, ∑ q, conj' (prodVec u v q) * D q p * prodVec u v p from
    Finset.sum_congr rfl fun p _ => by
      rw [Matrix.diag_apply, Matrix.mul_apply]
      refine Finset.sum_congr rfl fun q _ => ?_
      show (u p.1 * conj' (u q.1)) * (v p.2 * conj' (v q.2)) * D q p
        = conj' (u q.1 * v q.2) * D q p * (u p.1 * v p.2)
      rw [map_mul]
      ring]
  exact Finset.sum_comm

omit [DecidableEq A] [DecidableEq B] in
/-- Reordering a fourfold finite sum. -/
theorem sum4_reorder (F : A → B → A → B → ℂ) :
    ∑ q1, ∑ q2, ∑ p1, ∑ p2, F q1 q2 p1 p2
      = ∑ q2, ∑ p2, ∑ q1, ∑ p1, F q1 q2 p1 p2 := by
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun q2 _ => ?_
  rw [show (∑ q1, ∑ p1, ∑ p2, F q1 q2 p1 p2)
      = ∑ q1, ∑ p2, ∑ p1, F q1 q2 p1 p2 from
    Finset.sum_congr rfl fun _ _ => Finset.sum_comm]
  exact Finset.sum_comm

/-- The `B`-block form of a composite matrix at a fixed `A`-probe vector. -/
def blockB (D : Matrix (A × B) (A × B) ℂ) (u : A → ℂ) : Matrix B B ℂ :=
  Matrix.of fun q2 p2 => ∑ q1, ∑ p1, conj' (u q1) * D (q1, q2) (p1, p2) * u p1

/-- The `A`-block of a composite matrix at a fixed pair of `B` indices. -/
def blockA (D : Matrix (A × B) (A × B) ℂ) (q2 p2 : B) : Matrix A A ℂ :=
  Matrix.of fun q1 p1 => D (q1, q2) (p1, p2)

omit [DecidableEq A] [Fintype B] [DecidableEq B] in
/-- The `A`-form of a block is the corresponding entry of the `B`-block. -/
theorem blockA_form (D : Matrix (A × B) (A × B) ℂ) (u : A → ℂ) (q2 p2 : B) :
    star u ⬝ᵥ (blockA D q2 p2).mulVec u = blockB D u q2 p2 := by
  rw [form_expand]
  rfl

/-- The `B`-form of the block is the product-vector form of the composite. -/
theorem blockB_form (D : Matrix (A × B) (A × B) ℂ) (u : A → ℂ) (v : B → ℂ) :
    star v ⬝ᵥ (blockB D u).mulVec v
      = star (prodVec u v) ⬝ᵥ D.mulVec (prodVec u v) := by
  rw [form_expand, form_expand]
  rw [show (∑ Q : A × B, ∑ P : A × B,
        conj' (prodVec u v Q) * D Q P * prodVec u v P)
      = ∑ q1, ∑ q2, ∑ p1, ∑ p2,
          conj' (u q1) * conj' (v q2) * D (q1, q2) (p1, p2) * (u p1 * v p2) from by
    rw [Fintype.sum_prod_type]
    refine Finset.sum_congr rfl fun q1 _ => Finset.sum_congr rfl fun q2 _ => ?_
    rw [Fintype.sum_prod_type]
    refine Finset.sum_congr rfl fun p1 _ => Finset.sum_congr rfl fun p2 _ => ?_
    show conj' (u q1 * v q2) * D (q1, q2) (p1, p2) * (u p1 * v p2) = _
    rw [map_mul]]
  rw [sum4_reorder]
  refine Finset.sum_congr rfl fun q2 _ => Finset.sum_congr rfl fun p2 _ => ?_
  show conj' (v q2)
      * (∑ q1, ∑ p1, conj' (u q1) * D (q1, q2) (p1, p2) * u p1) * v p2 = _
  rw [Finset.mul_sum, Finset.sum_mul]
  refine Finset.sum_congr rfl fun q1 _ => ?_
  rw [Finset.mul_sum, Finset.sum_mul]
  refine Finset.sum_congr rfl fun p1 _ => ?_
  ring

/-- **PHYSICAL LOCAL TOMOGRAPHY.** Equal probabilities for every PRODUCT rank-one effect
`|u⟩⟨u| ⊗ |v⟩⟨v|` force equal composite states. Unlike
`productMatrixUnit_local_separating`, whose hypothesis is a family of matrix-unit
FUNCTIONALS rather than physical effects, this is the operational statement: the
reconstruction runs complex polarization twice, once on each factor, so no entangled
effect and no matrix unit is ever used. -/
theorem local_tomography_physical (ρ σ : Matrix (A × B) (A × B) ℂ)
    (h : ∀ (u : A → ℂ) (v : B → ℂ),
      Matrix.trace (prodProj u v * ρ) = Matrix.trace (prodProj u v * σ)) :
    ρ = σ := by
  rw [← sub_eq_zero]
  have hform : ∀ (u : A → ℂ) (v : B → ℂ),
      star (prodVec u v) ⬝ᵥ (ρ - σ).mulVec (prodVec u v) = 0 := by
    intro u v
    rw [← prodProj_trace, Matrix.mul_sub, Matrix.trace_sub, h u v, sub_self]
  -- polarize on the `B` factor first: every `B`-block vanishes
  have hB : ∀ u : A → ℂ, blockB (ρ - σ) u = 0 := fun u =>
    eq_zero_of_form_vanishes _ fun v => by rw [blockB_form]; exact hform u v
  -- then on the `A` factor: every `A`-block vanishes, which is every entry
  have hA : ∀ q2 p2 : B, blockA (ρ - σ) q2 p2 = 0 := fun q2 p2 =>
    eq_zero_of_form_vanishes _ fun u => by
      rw [blockA_form, hB u]
      rfl
  ext P Q
  obtain ⟨p1, p2⟩ := P
  obtain ⟨q1, q2⟩ := Q
  have := congrFun (congrFun (hA p2 q2) p1) q1
  rwa [Matrix.zero_apply] at this ⊢

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
#print axioms productMatrixUnit_local_separating
#print axioms form_expand
#print axioms eq_zero_of_form_vanishes
#print axioms prodProj_trace
#print axioms local_tomography_physical

end InstrumentDilation
end OIBridge
