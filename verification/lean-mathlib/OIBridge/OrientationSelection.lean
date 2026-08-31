/-
  OIBridge/OrientationSelection.lean — C3c bounded exactly: the operational selector no-go,
  the abstract oriented reference, and the two phase-two orientation routes assembled with
  the round-seven classification.

  PHASE THREE, ROUND EIGHT. `sameData_unitary_or_transpose` (JordanClassification) closed
  C3b: any two existing OI-compatible coherent completions with the same complete
  operational data are unitary or transpose (antiunitary) equivalent. C3c is the question
  of which branch is physical. This file draws the boundary of that question exactly, in
  three layers.

  §A — THE SELECTOR NO-GO. The transpose partner ΘR = ({Gᵢᵀ}, {σₖᵀ}) of a completion
  R = ({Gᵢ}, {σₖ}) carries IDENTICAL pairing data (`transpose_data_eq`, phase two's
  `pairing_transpose` instantiated on the classification's data), remains admissible for
  the classification — Hermitian menu, PSD states, full span, separation, unit, full cone
  all transport (`transpose_completion_admissible`) — and sits in the second branch of the
  classification relative to R, realized by the transpose map itself with W = 1
  (`transpose_realizes_second_branch`). The branch is genuinely distinct: the transpose
  map is not the conjugation action of ANY unitary (`transpose_not_inner` — inner maps are
  multiplicative, the transpose is antimultiplicative, and matrix units refuse to commute).
  Hence the no-go: any selector that factors through the operational data assigns the same
  verdict to R and ΘR (`operational_orientation_noGo`; `selector_factorization_invariant`
  is the fully abstract form, covering EVERY Θ-invariant data assignment — circuit strings
  and adaptive instrument sequences included, by phase two's `circuit_invariance` and
  `string_invariance`).

      ┌────────────────────────────────────────────────────────────────────────┐
      │  Full unoriented operational data select QM only up to antiunitary     │
      │  equivalence.                                                          │
      └────────────────────────────────────────────────────────────────────────┘

  This is not a failure of the programme; it is the mathematically correct equivalence
  class. Ordinary quantum mechanics itself treats unitarily and antiunitarily related
  descriptions as one theory until an orientation-sensitive structure is supplied.

  §B — THE ORIENTED REFERENCE. What suffices is a canonically labelled real quantity O
  with O(ΘR) = −O(R) together with an OI-derived O(R) > 0: the transpose partner then
  fails the positivity (`orientedReference_excludes_transpose`), and combined with the
  classification the surviving equivalence is unitary
  (`sameData_unitary_of_orientedReference`). The boundary is sharp in both directions:
  such an O can never factor through Θ-invariant data
  (`oriented_functional_not_data_definable` — it would satisfy O = −O and vanish). The
  oriented datum is provably NOT a function of unoriented operational data; it must be an
  additional, or differently derived, physical condition.

  §C — THE TWO PHYSICAL ROUTES, ASSEMBLED. Phase two supplies exactly such a condition in
  two conditional forms, and this file connects each to the classification:

    * the rate route — `sameData_unitary_of_transitionIdentification`:
      `OperationalTransitionIdentification` (positive `β_E`, `τ_K`) transports the
      classical exchange ordering to the Bohr ordering (`energyOrder_transport`), so one
      classically passive, non-uniform profile refutes the reflected orientation
      (`reflection_excluded_of_transition_identification`); with the named bridge clause —
      the transpose branch reads the shared profile as passive for the REFLECTED Bohr
      order, phase two's `transported_gibbs` alignment `E′∘τ = −E + E₀` — the dichotomy
      resolves to the unitary branch.
    * the state route — `sameData_unitary_of_shellRepresentation`:
      `ShellRepresentationConsistency` supplies a genuine stationary state whose spectral
      populations exist (`shellRepresentation_stationary_profile`, via
      `stationary_spectral_form`); spectral passivity plus non-uniformity refute the
      reflected orientation (`passivity_selector_nonuniform`), and the same bridge clause
      resolves the dichotomy. The state hypotheses of the capstone are verbatim the
      clauses of `ShellRepresentationConsistency`, unpacked so the oriented condition can
      name the state's spectral profile.

  THE AUDIT — one question, answered at the kernel boundary. Can OI's already-derived
  positive classical energy arrow (`counting_passive`: `β_E = ∂S_H/∂E ≥ 0` orients the
  classical profile, exactly) supply the oriented datum without a new postulate? What this
  file fixes: the arrow's classical face IS derived, and its orienting power is exactly
  what §C consumes; but by `oriented_functional_not_data_definable` no Θ-invariant data
  can carry it into the coherent completion — and phase two proved ALL circuit data
  Θ-invariant (`circuit_invariance`, `string_invariance`) with the native primitives
  Θ-fixed pointwise (`readProj_transpose`, `permMatrix_conjOp`,
  `real_menu_conjugation_stable`). The arrow therefore enters the coherent theory ONLY
  through the operational identification the two named premises state — no new postulate
  beyond the coherent lift, and provably not less than it. The terminal forms are exactly
  two:

      OI + coherent-completion conditions                              ⟹  QM / ℤ₂ᵃⁿᵗⁱ
      OI + coherent completion + positive thermodynamic orientation   ⟹  QM

  the second up to ordinary unitary gauge, the first the strongest bare form possible.

  WHAT THIS DOES NOT ESTABLISH. Whether bare OI derives `OperationalTransitionIdentification`
  or `ShellRepresentationConsistency` — the single remaining foundational question, now
  precise. And existence remains governed by the no-go: every statement here is about
  EXISTING OI-compatible completions.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.JordanClassification
import OIBridge.ThermalOrientation
import OIBridge.ShellAssignment
import OIBridge.AntiunitaryInvariance

namespace OIBridge
namespace OrientationSelection

open Complex Matrix JordanClassification ThermalOrientation
open scoped ComplexOrder

variable {n : Type*} [Fintype n] [DecidableEq n]

/-! ### Section A — the transpose partner and the operational selector no-go -/

/-- The transpose as a `ℂ`-linear map on matrices — the map that realizes the second
branch of the classification with `W = 1`. -/
def transposeL : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ where
  toFun X := Xᵀ
  map_add' := Matrix.transpose_add
  map_smul' := Matrix.transpose_smul

omit [DecidableEq n] in
/-- **THE DATA OF THE TRANSPOSE PARTNER ARE THE DATA.** The complete pairing data of the
transposed completion `({Gᵢᵀ}, {σₖᵀ})` coincide, as one function, with the pairing data of
`({Gᵢ}, {σₖ})` — phase two's `pairing_transpose` instantiated on the classification's data
assignment. -/
theorem transpose_data_eq {ι κ : Type*} (G : ι → Matrix n n ℂ) (σ : κ → Matrix n n ℂ) :
    (fun i k => Matrix.trace ((G i)ᵀ * (σ k)ᵀ)) = fun i k => Matrix.trace (G i * σ k) := by
  funext i k
  exact AntiunitaryInvariance.pairing_transpose (G i) (σ k)

/-- **THE ABSTRACT SELECTOR NO-GO.** Any assignment that factors through Θ-invariant data
gives the same value on `R` and `Θ R` — for every data map, every factoring function, and
every codomain. Phase two makes every circuit-data assignment Θ-invariant
(`circuit_invariance`, `string_invariance`), so no selector built from such data can
choose one member of the pair. -/
theorem selector_factorization_invariant {α δ γ : Type*} (Θ : α → α) (data : α → δ)
    (hinv : ∀ R, data (Θ R) = data R) (f : δ → γ) (R : α) :
    f (data (Θ R)) = f (data R) :=
  congrArg f (hinv R)

omit [DecidableEq n] in
/-- **`operational_orientation_noGo` — the boxed no-go.** A proposed selector `S` that
factors only through the complete pairing data assigns the same verdict to a completion
and to its transpose partner: `S(Θ R) = S(R)`. Therefore no such selector can choose the
unitary branch over the transpose branch, and full unoriented operational data select QM
only up to antiunitary equivalence. -/
theorem operational_orientation_noGo {ι κ α : Type*}
    (G : ι → Matrix n n ℂ) (σ : κ → Matrix n n ℂ) (S : (ι → κ → ℂ) → α) :
    S (fun i k => Matrix.trace ((G i)ᵀ * (σ k)ᵀ))
      = S (fun i k => Matrix.trace (G i * σ k)) :=
  congrArg S (transpose_data_eq G σ)

omit [Fintype n] [DecidableEq n] in
/-- Transposition preserves full span: the transposed menu still spans all of `M_D(ℂ)`. -/
theorem transpose_span {ι : Type*} (G : ι → Matrix n n ℂ)
    (hspan : Submodule.span ℂ (Set.range G) = ⊤) :
    Submodule.span ℂ (Set.range fun i => (G i)ᵀ) = ⊤ := by
  rw [Submodule.eq_top_iff']
  intro X
  have hX : Xᵀ ∈ Submodule.span ℂ (Set.range G) := by rw [hspan]; trivial
  have hmap : ∀ Y ∈ Submodule.span ℂ (Set.range G),
      Yᵀ ∈ Submodule.span ℂ (Set.range fun i => (G i)ᵀ) := by
    intro Y hY
    induction hY using Submodule.span_induction with
    | mem x hx =>
        obtain ⟨i, rfl⟩ := hx
        exact Submodule.subset_span ⟨i, rfl⟩
    | zero =>
        rw [Matrix.transpose_zero]
        exact Submodule.zero_mem _
    | add x y _ _ hx hy =>
        rw [Matrix.transpose_add]
        exact Submodule.add_mem _ hx hy
    | smul c x _ hx =>
        rw [Matrix.transpose_smul]
        exact Submodule.smul_mem _ c hx
  have h2 := hmap Xᵀ hX
  rwa [Matrix.transpose_transpose] at h2

omit [DecidableEq n] in
/-- Transposition preserves separation: the transposed state family still separates
operators. -/
theorem transpose_sep {κ : Type*} (σ : κ → Matrix n n ℂ)
    (hsep : ∀ M : Matrix n n ℂ, (∀ k, Matrix.trace (M * σ k) = 0) → M = 0)
    (M : Matrix n n ℂ) (hM : ∀ k, Matrix.trace (M * (σ k)ᵀ) = 0) : M = 0 := by
  have h1 : Mᵀ = 0 := by
    apply hsep
    intro k
    have h2 := AntiunitaryInvariance.pairing_transpose Mᵀ (σ k)
    rw [Matrix.transpose_transpose] at h2
    rw [← h2]
    exact hM k
  calc M = Mᵀᵀ := (Matrix.transpose_transpose M).symm
    _ = 0 := by rw [h1, Matrix.transpose_zero]

omit [Fintype n] [DecidableEq n] in
/-- Transposition preserves the full accessible cone: every PSD matrix is still a nonneg
combination of the transposed states. -/
theorem transpose_cone {κ : Type*} (σ : κ → Matrix n n ℂ)
    (hcone : ∀ τ : Matrix n n ℂ, τ.PosSemidef → ∃ (s : Finset κ) (c : κ → ℝ),
      (∀ k, 0 ≤ c k) ∧ τ = ∑ k ∈ s, c k • σ k)
    (τ : Matrix n n ℂ) (hτ : τ.PosSemidef) :
    ∃ (s : Finset κ) (c : κ → ℝ), (∀ k, 0 ≤ c k) ∧ τ = ∑ k ∈ s, c k • (σ k)ᵀ := by
  obtain ⟨s, c, hc, hτ'⟩ := hcone τᵀ hτ.transpose
  refine ⟨s, c, hc, ?_⟩
  have h2 := congrArg Matrix.transpose hτ'
  rw [Matrix.transpose_transpose, Matrix.transpose_sum] at h2
  simp only [Matrix.transpose_smul] at h2
  exact h2

/-- **THE TRANSPOSE PARTNER IS ADMISSIBLE.** Every structural hypothesis of the
classification transports to the transposed completion: Hermitian menu, PSD states, full
span, separation, the unit, and the full cone. `Θ R` is a completion in exactly the same
class as `R`. -/
theorem transpose_completion_admissible {ι κ : Type*}
    (G : ι → Matrix n n ℂ) (σ : κ → Matrix n n ℂ)
    (hGh : ∀ i, (G i).IsHermitian) (hσp : ∀ k, (σ k).PosSemidef)
    (hspan : Submodule.span ℂ (Set.range G) = ⊤)
    (hsep : ∀ M : Matrix n n ℂ, (∀ k, Matrix.trace (M * σ k) = 0) → M = 0)
    (i₀ : ι) (hone : G i₀ = 1)
    (hcone : ∀ τ : Matrix n n ℂ, τ.PosSemidef → ∃ (s : Finset κ) (c : κ → ℝ),
      (∀ k, 0 ≤ c k) ∧ τ = ∑ k ∈ s, c k • σ k) :
    (∀ i, ((G i)ᵀ).IsHermitian) ∧ (∀ k, ((σ k)ᵀ).PosSemidef)
      ∧ Submodule.span ℂ (Set.range fun i => (G i)ᵀ) = ⊤
      ∧ (∀ M : Matrix n n ℂ, (∀ k, Matrix.trace (M * (σ k)ᵀ) = 0) → M = 0)
      ∧ (G i₀)ᵀ = 1
      ∧ ∀ τ : Matrix n n ℂ, τ.PosSemidef → ∃ (s : Finset κ) (c : κ → ℝ),
          (∀ k, 0 ≤ c k) ∧ τ = ∑ k ∈ s, c k • (σ k)ᵀ :=
  ⟨fun i => (hGh i).transpose, fun k => (hσp k).transpose, transpose_span G hspan,
    transpose_sep σ hsep, by rw [hone, Matrix.transpose_one], transpose_cone σ hcone⟩

/-- **THE TRANSPOSE PARTNER SITS IN THE SECOND BRANCH.** The transpose map itself, with
`W = 1`, is a data-preserving equivalence from `R` onto `Θ R` of exactly the transpose
form the classification names: the second branch is REALIZED between two admissible
completions with identical data. -/
theorem transpose_realizes_second_branch {ι : Type*} (G : ι → Matrix n n ℂ) :
    ∃ (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ) (W : Matrix n n ℂ),
      (∀ i, Φ (G i) = (G i)ᵀ) ∧ Wᴴ * W = 1 ∧ ∀ X : Matrix n n ℂ, Φ X = W * Xᵀ * Wᴴ := by
  refine ⟨transposeL, 1, fun i => rfl, by rw [Matrix.conjTranspose_one, one_mul], fun X => ?_⟩
  show Xᵀ = 1 * Xᵀ * (1 : Matrix n n ℂ)ᴴ
  rw [Matrix.conjTranspose_one, one_mul, mul_one]

/-- **THE TWO BRANCHES ARE DISJOINT.** The transpose map is not the conjugation action of
any unitary: an inner map is multiplicative, the transpose is antimultiplicative, and
already one pair of matrix units refuses to commute. The classification's dichotomy is a
genuine fork, not a relabelling. -/
theorem transpose_not_inner {i j : n} (hij : i ≠ j) :
    ¬ ∃ W : Matrix n n ℂ, Wᴴ * W = 1 ∧ ∀ X : Matrix n n ℂ, Xᵀ = W * X * Wᴴ := by
  rintro ⟨W, hW, hX⟩
  have hcomm : ∀ A B : Matrix n n ℂ, B * A = A * B := by
    intro A B
    have h1 : (Aᵀ * Bᵀ)ᵀ = Aᵀᵀ * Bᵀᵀ := by
      rw [hX (Aᵀ * Bᵀ), hX Aᵀ, hX Bᵀ]
      calc W * (Aᵀ * Bᵀ) * Wᴴ
          = W * Aᵀ * (Wᴴ * W) * Bᵀ * Wᴴ := by rw [hW]; noncomm_ring
        _ = W * Aᵀ * Wᴴ * (W * Bᵀ * Wᴴ) := by noncomm_ring
    rw [Matrix.transpose_mul, Matrix.transpose_transpose, Matrix.transpose_transpose] at h1
    exact h1
  have hc := hcomm (Eu i i) (Eu i j)
  rw [Eu_mul_of_ne i (Ne.symm hij) i, Eu_mul_same] at hc
  exact Eu_ne_zero i j hc.symm

/-! ### Section B — the abstract oriented reference -/

/-- **`orientedReference_excludes_transpose`.** A canonically labelled real quantity that
reverses under the transpose partner and is positive on the completion is strictly
negative on the partner: the antiunitary branch fails the oriented condition. -/
theorem orientedReference_excludes_transpose {α : Type*} (Θ : α → α) (O : α → ℝ)
    (hflip : ∀ R, O (Θ R) = -O R) {R : α} (hpos : 0 < O R) : O (Θ R) < 0 := by
  rw [hflip R]
  linarith

/-- **THE ORIENTED DATUM IS NOT DATA-DEFINABLE.** A quantity that reverses under Θ and is
anywhere nonzero cannot factor through any Θ-invariant data assignment: it would satisfy
`O(R) = −O(R)`. Phase two makes every circuit-data assignment Θ-invariant and the native
primitives Θ-fixed, so the oriented reference is provably an ADDITIONAL condition, not a
consequence of unoriented data. This is the audit's formal boundary. -/
theorem oriented_functional_not_data_definable {α δ : Type*} (Θ : α → α) (data : α → δ)
    (hinv : ∀ R, data (Θ R) = data R) (O : α → ℝ)
    (hflip : ∀ R, O (Θ R) = -O R) {R : α} (hne : O R ≠ 0) :
    ¬ ∃ f : δ → ℝ, ∀ R', O R' = f (data R') := by
  rintro ⟨f, hf⟩
  have h1 : O (Θ R) = O R := by rw [hf (Θ R), hinv R, ← hf R]
  rw [hflip R] at h1
  exact hne (by linarith)

/-- **`sameData_unitary_of_orientedReference` — the oriented classification.** Under the
full hypotheses of `sameData_unitary_or_transpose`, if both completions carry an oriented
reference (two positive reals) that the transpose branch would force to opposite signs,
the equivalence is unitary. The hard physics is confined to producing the two positive
numbers; the exclusion itself is arithmetic. -/
theorem sameData_unitary_of_orientedReference {ι κ : Type*}
    (G₁ G₂ : ι → Matrix n n ℂ) (σ₁ σ₂ : κ → Matrix n n ℂ)
    (hdata : ∀ i k, Matrix.trace (G₁ i * σ₁ k) = Matrix.trace (G₂ i * σ₂ k))
    (hG₁h : ∀ i, (G₁ i).IsHermitian) (hG₂h : ∀ i, (G₂ i).IsHermitian)
    (hσ₁p : ∀ k, (σ₁ k).PosSemidef) (hσ₂p : ∀ k, (σ₂ k).PosSemidef)
    (hspan₁ : Submodule.span ℂ (Set.range G₁) = ⊤)
    (hspan₂ : Submodule.span ℂ (Set.range G₂) = ⊤)
    (hsep₁ : ∀ M : Matrix n n ℂ, (∀ k, Matrix.trace (M * σ₁ k) = 0) → M = 0)
    (hsep₂ : ∀ M : Matrix n n ℂ, (∀ k, Matrix.trace (M * σ₂ k) = 0) → M = 0)
    (i₀ : ι) (hone₁ : G₁ i₀ = 1) (hone₂ : G₂ i₀ = 1)
    (hcone₁ : ∀ τ : Matrix n n ℂ, τ.PosSemidef → ∃ (s : Finset κ) (c : κ → ℝ),
      (∀ k, 0 ≤ c k) ∧ τ = ∑ k ∈ s, c k • σ₁ k)
    (hcone₂ : ∀ τ : Matrix n n ℂ, τ.PosSemidef → ∃ (s : Finset κ) (c : κ → ℝ),
      (∀ k, 0 ≤ c k) ∧ τ = ∑ k ∈ s, c k • σ₂ k)
    (O₁ O₂ : ℝ) (hpos₁ : 0 < O₁) (hpos₂ : 0 < O₂)
    (hflip : ∀ (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ) (W : Matrix n n ℂ),
      (∀ i, Φ (G₁ i) = G₂ i) → Wᴴ * W = 1 → (∀ X, Φ X = W * Xᵀ * Wᴴ) → O₂ = -O₁) :
    ∃ (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ) (W : Matrix n n ℂ),
      (∀ i, Φ (G₁ i) = G₂ i) ∧ Wᴴ * W = 1 ∧ ∀ X, Φ X = W * X * Wᴴ := by
  obtain ⟨Φ, W, hΦ, hW, hbr⟩ := sameData_unitary_or_transpose G₁ G₂ σ₁ σ₂ hdata hG₁h hG₂h
    hσ₁p hσ₂p hspan₁ hspan₂ hsep₁ hsep₂ i₀ hone₁ hone₂ hcone₁ hcone₂
  rcases hbr with h | h
  · exact ⟨Φ, W, hΦ, hW, h⟩
  · exfalso
    have := hflip Φ W hΦ hW h
    linarith

/-! ### Section C — the two phase-two orientation routes, assembled -/

/-- **`shellRepresentation_stationary_profile`.** `ShellRepresentationConsistency` hands
the orientation selectors their object: a genuine state — PSD, trace one, classical
readout — that IS its spectral population profile (`stationary_spectral_form`): the state
is completely determined by the populations the passivity selectors test. -/
theorem shellRepresentation_stationary_profile {m : ℕ}
    (Vm : Matrix (Fin m) (Fin m) ℂ) {E p : Fin m → ℝ}
    (hSRC : ShellAssignment.ShellRepresentationConsistency Vm E p)
    (hV : Vm * Vmᴴ = 1) (hE : Function.Injective E) :
    ∃ ρ : Matrix (Fin m) (Fin m) ℂ, ρ.PosSemidef ∧ Matrix.trace ρ = 1
      ∧ (∀ i, ρ i i = ((p i : ℝ) : ℂ))
      ∧ ρ = Vm * Matrix.diagonal (fun a => (Vmᴴ * ρ * Vm) a a) * Vmᴴ := by
  obtain ⟨ρ, hpsd, htr, hstat, hread⟩ := hSRC
  exact ⟨ρ, hpsd, htr, hread, stationary_spectral_form Vm ρ E hV hE hstat⟩

/-- **`sameData_unitary_of_transitionIdentification` — the rate route resolves the
fork.** Under the classification hypotheses, `OperationalTransitionIdentification` with
positive `β_E, τ_K`, distinct Bohr frequencies, and one classically passive non-uniform
profile force the unitary branch: everything after the named premise is kernel theorem.
The bridge clause is phase two's reflected alignment — if the equivalence were the
transpose branch, the shared profile would read as passive for the REFLECTED Bohr order
(`transported_gibbs`: `E′∘τ = −E + E₀`) — and
`reflection_excluded_of_transition_identification` refutes exactly that. -/
theorem sameData_unitary_of_transitionIdentification {ι κ : Type*}
    (G₁ G₂ : ι → Matrix n n ℂ) (σ₁ σ₂ : κ → Matrix n n ℂ)
    (hdata : ∀ i k, Matrix.trace (G₁ i * σ₁ k) = Matrix.trace (G₂ i * σ₂ k))
    (hG₁h : ∀ i, (G₁ i).IsHermitian) (hG₂h : ∀ i, (G₂ i).IsHermitian)
    (hσ₁p : ∀ k, (σ₁ k).PosSemidef) (hσ₂p : ∀ k, (σ₂ k).PosSemidef)
    (hspan₁ : Submodule.span ℂ (Set.range G₁) = ⊤)
    (hspan₂ : Submodule.span ℂ (Set.range G₂) = ⊤)
    (hsep₁ : ∀ M : Matrix n n ℂ, (∀ k, Matrix.trace (M * σ₁ k) = 0) → M = 0)
    (hsep₂ : ∀ M : Matrix n n ℂ, (∀ k, Matrix.trace (M * σ₂ k) = 0) → M = 0)
    (i₀ : ι) (hone₁ : G₁ i₀ = 1) (hone₂ : G₂ i₀ = 1)
    (hcone₁ : ∀ τ : Matrix n n ℂ, τ.PosSemidef → ∃ (s : Finset κ) (c : κ → ℝ),
      (∀ k, 0 ≤ c k) ∧ τ = ∑ k ∈ s, c k • σ₁ k)
    (hcone₂ : ∀ τ : Matrix n n ℂ, τ.PosSemidef → ∃ (s : Finset κ) (c : κ → ℝ),
      (∀ k, 0 ≤ c k) ∧ τ = ∑ k ∈ s, c k • σ₂ k)
    {m : ℕ} {βE τK : ℝ} (hβ : 0 < βE) (hτ : 0 < τK) {ε ω p : Fin m → ℝ} {E₀ : ℝ}
    (hOTI : OperationalTransitionIdentification βE τK ε ω)
    (hdist : ∀ a b : Fin m, a ≠ b → ω a ≠ ω b)
    (hp : Passive ε p) {a b : Fin m} (hpab : p a ≠ p b)
    (hbridge : (∃ (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ) (W : Matrix n n ℂ),
        (∀ i, Φ (G₁ i) = G₂ i) ∧ Wᴴ * W = 1 ∧ ∀ X, Φ X = W * Xᵀ * Wᴴ) →
      Passive (fun c => -ω c + E₀) p) :
    ∃ (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ) (W : Matrix n n ℂ),
      (∀ i, Φ (G₁ i) = G₂ i) ∧ Wᴴ * W = 1 ∧ ∀ X, Φ X = W * X * Wᴴ := by
  obtain ⟨Φ, W, hΦ, hW, hbr⟩ := sameData_unitary_or_transpose G₁ G₂ σ₁ σ₂ hdata hG₁h hG₂h
    hσ₁p hσ₂p hspan₁ hspan₂ hsep₁ hsep₂ i₀ hone₁ hone₂ hcone₁ hcone₂
  rcases hbr with h | h
  · exact ⟨Φ, W, hΦ, hW, h⟩
  · exact absurd (hbridge ⟨Φ, W, hΦ, hW, h⟩)
      (reflection_excluded_of_transition_identification hβ hτ hOTI hdist hp hpab)

/-- **`sameData_unitary_of_shellRepresentation` — the state route resolves the fork.**
Under the classification hypotheses, one represented stationary state — the clauses are
verbatim those of `ShellRepresentationConsistency`, unpacked so the oriented condition can
name the state's spectral profile, which `shellRepresentation_stationary_profile` shows
determines the state completely — with passive, non-uniform spectral populations forces
the unitary branch: the transpose branch would read the same populations as passive for
the reflected order, and `passivity_selector_nonuniform` refutes that. -/
theorem sameData_unitary_of_shellRepresentation {ι κ : Type*}
    (G₁ G₂ : ι → Matrix n n ℂ) (σ₁ σ₂ : κ → Matrix n n ℂ)
    (hdata : ∀ i k, Matrix.trace (G₁ i * σ₁ k) = Matrix.trace (G₂ i * σ₂ k))
    (hG₁h : ∀ i, (G₁ i).IsHermitian) (hG₂h : ∀ i, (G₂ i).IsHermitian)
    (hσ₁p : ∀ k, (σ₁ k).PosSemidef) (hσ₂p : ∀ k, (σ₂ k).PosSemidef)
    (hspan₁ : Submodule.span ℂ (Set.range G₁) = ⊤)
    (hspan₂ : Submodule.span ℂ (Set.range G₂) = ⊤)
    (hsep₁ : ∀ M : Matrix n n ℂ, (∀ k, Matrix.trace (M * σ₁ k) = 0) → M = 0)
    (hsep₂ : ∀ M : Matrix n n ℂ, (∀ k, Matrix.trace (M * σ₂ k) = 0) → M = 0)
    (i₀ : ι) (hone₁ : G₁ i₀ = 1) (hone₂ : G₂ i₀ = 1)
    (hcone₁ : ∀ τ : Matrix n n ℂ, τ.PosSemidef → ∃ (s : Finset κ) (c : κ → ℝ),
      (∀ k, 0 ≤ c k) ∧ τ = ∑ k ∈ s, c k • σ₁ k)
    (hcone₂ : ∀ τ : Matrix n n ℂ, τ.PosSemidef → ∃ (s : Finset κ) (c : κ → ℝ),
      (∀ k, 0 ≤ c k) ∧ τ = ∑ k ∈ s, c k • σ₂ k)
    {m : ℕ} (Vm ρ : Matrix (Fin m) (Fin m) ℂ) {E : Fin m → ℝ} {E₀ : ℝ}
    (hdist : ∀ a b : Fin m, a ≠ b → E a ≠ E b)
    (hq : Passive E (fun c => ((Vmᴴ * ρ * Vm) c c).re))
    {a b : Fin m}
    (hqab : ((Vmᴴ * ρ * Vm) a a).re ≠ ((Vmᴴ * ρ * Vm) b b).re)
    (hbridge : (∃ (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ) (W : Matrix n n ℂ),
        (∀ i, Φ (G₁ i) = G₂ i) ∧ Wᴴ * W = 1 ∧ ∀ X, Φ X = W * Xᵀ * Wᴴ) →
      Passive (fun c => -E c + E₀) (fun c => ((Vmᴴ * ρ * Vm) c c).re)) :
    ∃ (Φ : Matrix n n ℂ →ₗ[ℂ] Matrix n n ℂ) (W : Matrix n n ℂ),
      (∀ i, Φ (G₁ i) = G₂ i) ∧ Wᴴ * W = 1 ∧ ∀ X, Φ X = W * X * Wᴴ := by
  obtain ⟨Φ, W, hΦ, hW, hbr⟩ := sameData_unitary_or_transpose G₁ G₂ σ₁ σ₂ hdata hG₁h hG₂h
    hσ₁p hσ₂p hspan₁ hspan₂ hsep₁ hsep₂ i₀ hone₁ hone₂ hcone₁ hcone₂
  rcases hbr with h | h
  · exact ⟨Φ, W, hΦ, hW, h⟩
  · exact absurd (hbridge ⟨Φ, W, hΦ, hW, h⟩)
      (passivity_selector_nonuniform hdist hq hqab)

#print axioms transpose_data_eq
#print axioms selector_factorization_invariant
#print axioms operational_orientation_noGo
#print axioms transpose_span
#print axioms transpose_sep
#print axioms transpose_cone
#print axioms transpose_completion_admissible
#print axioms transpose_realizes_second_branch
#print axioms transpose_not_inner
#print axioms orientedReference_excludes_transpose
#print axioms oriented_functional_not_data_definable
#print axioms sameData_unitary_of_orientedReference
#print axioms shellRepresentation_stationary_profile
#print axioms sameData_unitary_of_transitionIdentification
#print axioms sameData_unitary_of_shellRepresentation

end OrientationSelection
end OIBridge
