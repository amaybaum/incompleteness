/-
  OIBridge/FactorUniqueness.lean — two factorizations of the same operator differ by a unitary.

      X : E → H,  Y : F → H  injective, with  X X* = Y Y*
        ⟹  a UNIQUE  W : F → E  with  Y = X W,  and that `W` is unitary.

  WHY THIS FILE EXISTS SEPARATELY. It is the infrastructure step [Structure] Proposition 9.7a needs
  and neither Mathlib nor this corpus had: Mathlib carries no Stinespring theorem, and the Kraus
  uniqueness statement is not really about channels at all. Strip the physics and what remains is a
  fact about two injective maps into a common space with the same `X X*`. Keeping it here, with no
  channel, no Kraus family and no dilation in the statement, is what makes it reusable — the same
  position `IdempotentTrace` occupies for [SM] Theorem 7.

  WHY THE INDEX TYPES ARE DIFFERENT. `E` and `F` are separate spaces, deliberately. The equality of
  Kraus-family cardinalities is a CONSEQUENCE of the theorem — it falls out of `W` being an
  equivalence — and assuming a common index type up front would smuggle it in as a hypothesis. The
  `finrank` corollary below is that consequence, stated once.

  WHAT THE PROOF NEEDS, and what it does not. It needs `range_self_comp_adjoint` and
  `orthogonal_ker`, both already in Mathlib, and finite-dimensionality. It needs no pseudoinverse,
  no determinant, no matrix rank, no spectral theorem, no Cholesky factorization and no positive
  semidefinite library. `X X* = Y Y*` gives `range X = range Y`; `X` injective makes it an
  equivalence onto its range, so `W` is that inverse composed with `Y`; and unitarity is two
  cancellations, on the left by injectivity of `X` and on the right by surjectivity of `X*`.

  THE CONTROLS at the end record what the hypotheses are doing. Injectivity of `X` is what makes
  `W` unique — drop it and every `W` factors the zero map. Injectivity of `Y` is what makes `W`
  injective, and without it no factor can be unitary at all. And the hypothesis is `X X* = Y Y*`,
  not equality of ranges: `Y = 2X` has the same range and a factor of `2`.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.Analysis.InnerProductSpace.Adjoint
import Mathlib.Analysis.InnerProductSpace.LinearMap

namespace OIBridge

namespace FactorUniqueness

open LinearMap

/- Three of the controls below are pure linear algebra and do not use finite-dimensionality; they
are kept under the same section variables because they exist only to delimit the theorem that
does. -/
set_option linter.unusedSectionVars false

variable {𝕜 E F H : Type*} [RCLike 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E]
  [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [FiniteDimensional 𝕜 F]
  [NormedAddCommGroup H] [InnerProductSpace 𝕜 H] [FiniteDimensional 𝕜 H]

local notation "⟪" x ", " y "⟫" => inner 𝕜 x y


/-! ### The two facts the construction rests on

Both are Mathlib's. They are named here only because the argument uses each exactly once and the
naming makes the shape of the proof visible. -/

/-- **Equal `X X*` means equal range.** This is `range_self_comp_adjoint` applied twice, and it is
the only consequence of the hypothesis the construction uses. -/
theorem range_eq_of_comp_adjoint_eq {X : E →ₗ[𝕜] H} {Y : F →ₗ[𝕜] H}
    (h : X ∘ₗ adjoint X = Y ∘ₗ adjoint Y) : range X = range Y := by
  rw [← range_self_comp_adjoint X, h, range_self_comp_adjoint]

/-- **An injective map has a surjective adjoint**, in finite dimensions. This is what lets the
right-hand cancellation go through. -/
theorem surjective_adjoint_of_injective {X : E →ₗ[𝕜] H} (hX : Function.Injective X) :
    Function.Surjective (adjoint X) := by
  rw [← range_eq_top, ← orthogonal_ker, ker_eq_bot.2 hX]
  exact Submodule.bot_orthogonal_eq_top

/-! ### The factor

`X` injective is an equivalence onto its range, and `Y` lands in that range, so there is exactly
one candidate. Nothing about adjoints enters here. -/

/-- The unique map through which `Y` factors, given that `Y`'s range sits inside `X`'s. -/
noncomputable def factor {X : E →ₗ[𝕜] H} {Y : F →ₗ[𝕜] H} (hX : Function.Injective X)
    (hr : range Y ≤ range X) : F →ₗ[𝕜] E :=
  (LinearEquiv.ofInjective X hX).symm.toLinearMap ∘ₗ
    LinearMap.codRestrict (range X) Y fun f => hr ⟨f, rfl⟩

/-- **The factorization.** -/
@[simp] theorem comp_factor {X : E →ₗ[𝕜] H} {Y : F →ₗ[𝕜] H} (hX : Function.Injective X)
    (hr : range Y ≤ range X) : X ∘ₗ factor hX hr = Y := by
  ext f
  exact LinearEquiv.ofInjective_symm_apply (f := X) (h := hX) ⟨Y f, hr ⟨f, rfl⟩⟩

theorem factor_apply {X : E →ₗ[𝕜] H} {Y : F →ₗ[𝕜] H} (hX : Function.Injective X)
    (hr : range Y ≤ range X) (f : F) : X (factor hX hr f) = Y f :=
  congrArg (fun g : F →ₗ[𝕜] H => g f) (comp_factor hX hr)

/-- **Uniqueness**, and it needs only injectivity of `X` — not the adjoint hypothesis. -/
theorem factor_unique {X : E →ₗ[𝕜] H} {Y : F →ₗ[𝕜] H} (hX : Function.Injective X)
    (hr : range Y ≤ range X) {W : F →ₗ[𝕜] E} (hW : X ∘ₗ W = Y) : W = factor hX hr := by
  refine LinearMap.ext fun f => hX ?_
  rw [factor_apply, ← congrArg (fun g : F →ₗ[𝕜] H => g f) hW]
  rfl

theorem factor_injective {X : E →ₗ[𝕜] H} {Y : F →ₗ[𝕜] H} (hX : Function.Injective X)
    (hr : range Y ≤ range X) (hY : Function.Injective Y) :
    Function.Injective (factor hX hr) := by
  intro a b hab
  exact hY (by rw [← factor_apply hX hr a, ← factor_apply hX hr b, hab])

/-! ### Unitarity

Two cancellations. Substituting `Y = X W` into `X X* = Y Y*` gives
`X X* = X (W W*) X*`; injectivity of `X` cancels on the left and surjectivity of `X*` on the
right, leaving `W W* = 1`. Injectivity of `W` then upgrades that to `W* W = 1`. -/

theorem factor_comp_adjoint {X : E →ₗ[𝕜] H} {Y : F →ₗ[𝕜] H} (hX : Function.Injective X)
    (h : X ∘ₗ adjoint X = Y ∘ₗ adjoint Y) :
    letI hr := (range_eq_of_comp_adjoint_eq h).ge
    factor hX hr ∘ₗ adjoint (factor hX hr) = LinearMap.id := by
  set hr := (range_eq_of_comp_adjoint_eq h).ge with hrdef
  set W := factor hX hr with hWdef
  have hY : Y = X ∘ₗ W := (comp_factor hX hr).symm
  -- the left cancellation, pointwise
  have hcancel : ∀ x : H, W (adjoint W (adjoint X x)) = adjoint X x := by
    intro x
    refine hX ?_
    have h1 : X (adjoint X x) = Y (adjoint Y x) :=
      congrArg (fun g : H →ₗ[𝕜] H => g x) h
    have h2 : adjoint Y x = adjoint W (adjoint X x) := by
      rw [hY, adjoint_comp]; rfl
    rw [h1, h2, hY]
    rfl
  -- the right cancellation, by surjectivity of the adjoint
  refine LinearMap.ext fun e => ?_
  obtain ⟨x, rfl⟩ := surjective_adjoint_of_injective hX e
  simpa using hcancel x

theorem adjoint_comp_factor {X : E →ₗ[𝕜] H} {Y : F →ₗ[𝕜] H} (hX : Function.Injective X)
    (hY : Function.Injective Y) (h : X ∘ₗ adjoint X = Y ∘ₗ adjoint Y) :
    letI hr := (range_eq_of_comp_adjoint_eq h).ge
    adjoint (factor hX hr) ∘ₗ factor hX hr = LinearMap.id := by
  set hr := (range_eq_of_comp_adjoint_eq h).ge with hrdef
  set W := factor hX hr with hWdef
  have hinj : Function.Injective W := factor_injective hX hr hY
  have hWW : ∀ e : E, W (adjoint W e) = e :=
    fun e => congrArg (fun g : E →ₗ[𝕜] E => g e) (factor_comp_adjoint hX h)
  refine LinearMap.ext fun f => hinj ?_
  simpa using hWW (W f)

theorem factor_bijective {X : E →ₗ[𝕜] H} {Y : F →ₗ[𝕜] H} (hX : Function.Injective X)
    (hY : Function.Injective Y) (h : X ∘ₗ adjoint X = Y ∘ₗ adjoint Y) :
    letI hr := (range_eq_of_comp_adjoint_eq h).ge
    Function.Bijective (factor hX hr) := by
  set hr := (range_eq_of_comp_adjoint_eq h).ge with hrdef
  refine ⟨factor_injective hX hr hY, fun e => ⟨adjoint (factor hX hr) e, ?_⟩⟩
  exact congrArg (fun g : E →ₗ[𝕜] E => g e) (factor_comp_adjoint hX h)

/-- **The factor is a linear isometry equivalence.** Bundled, because a consumer wanting the
cardinality statement wants an equivalence and not a pair of adjoint identities. -/
noncomputable def factorEquiv {X : E →ₗ[𝕜] H} {Y : F →ₗ[𝕜] H} (hX : Function.Injective X)
    (hY : Function.Injective Y) (h : X ∘ₗ adjoint X = Y ∘ₗ adjoint Y) : F ≃ₗᵢ[𝕜] E :=
  letI hr := (range_eq_of_comp_adjoint_eq h).ge
  (LinearEquiv.ofBijective (factor hX hr) (factor_bijective hX hY h)).isometryOfInner
    (fun a b => by
      have hadj := congrArg (fun g : F →ₗ[𝕜] F => g b) (adjoint_comp_factor hX hY h)
      calc ⟪factor hX hr a, factor hX hr b⟫
          = ⟪a, adjoint (factor hX hr) (factor hX hr b)⟫ := (adjoint_inner_right _ _ _).symm
        _ = ⟪a, b⟫ := by rw [show adjoint (factor hX hr) (factor hX hr b) = b from hadj])

@[simp] theorem factorEquiv_apply {X : E →ₗ[𝕜] H} {Y : F →ₗ[𝕜] H} (hX : Function.Injective X)
    (hY : Function.Injective Y) (h : X ∘ₗ adjoint X = Y ∘ₗ adjoint Y) (f : F) :
    factorEquiv hX hY h f = factor hX (range_eq_of_comp_adjoint_eq h).ge f := rfl

/-! ### The theorem, and its cardinality consequence -/

/-- **Two injective factorizations of the same operator differ by a unique unitary.**

`X X* = Y Y*` with `X`, `Y` injective gives exactly one `W : F → E` with `Y = X W`, and that `W`
is a linear isometry equivalence. The domains `E` and `F` are unrelated in the hypotheses; that
they end up isomorphic is part of the conclusion. -/
theorem existsUnique_unitary_factor {X : E →ₗ[𝕜] H} {Y : F →ₗ[𝕜] H}
    (hX : Function.Injective X) (hY : Function.Injective Y)
    (h : X ∘ₗ adjoint X = Y ∘ₗ adjoint Y) :
    ∃! W : F →ₗ[𝕜] E, X ∘ₗ W = Y ∧ adjoint W ∘ₗ W = LinearMap.id ∧
      W ∘ₗ adjoint W = LinearMap.id := by
  set hr := (range_eq_of_comp_adjoint_eq h).ge with hrdef
  refine ⟨factor hX hr, ⟨comp_factor hX hr, adjoint_comp_factor hX hY h,
    factor_comp_adjoint hX h⟩, ?_⟩
  rintro W ⟨hW, -, -⟩
  exact factor_unique hX hr hW

/-- **Equal cardinality is a consequence, not a hypothesis.** -/
theorem finrank_eq {X : E →ₗ[𝕜] H} {Y : F →ₗ[𝕜] H} (hX : Function.Injective X)
    (hY : Function.Injective Y) (h : X ∘ₗ adjoint X = Y ∘ₗ adjoint Y) :
    Module.finrank 𝕜 F = Module.finrank 𝕜 E :=
  (factorEquiv hX hY h).toLinearEquiv.finrank_eq

/-! ### Controls

Each hypothesis is doing work, and these record which. -/

/-- **Injectivity of `X` is what makes the factor unique.** Without it the zero map is factored by
everything: `X = 0` and `Y = 0` satisfy the adjoint hypothesis, and both `0` and the identity
factor it, so no uniqueness statement survives. -/
theorem factor_not_unique_of_not_injective [Nontrivial E] :
    ∃ X : E →ₗ[𝕜] H, ∃ Y : E →ₗ[𝕜] H, X ∘ₗ adjoint X = Y ∘ₗ adjoint Y ∧
      ∃ W₁ W₂ : E →ₗ[𝕜] E, X ∘ₗ W₁ = Y ∧ X ∘ₗ W₂ = Y ∧ W₁ ≠ W₂ := by
  refine ⟨0, 0, rfl, 0, LinearMap.id, by simp, by simp, ?_⟩
  intro hcon
  obtain ⟨e, he⟩ := exists_ne (0 : E)
  exact he (congrArg (fun g : E →ₗ[𝕜] E => g e) hcon).symm

/-- **Injectivity of `Y` is what makes the factor injective**, and so is not removable: if `Y` is
not injective then NO map factoring it through an injective `X` is injective, hence none is
unitary. The failure is structural rather than a matter of a bad witness — the companion probe
exhibits the witness, a three-member Kraus family for a rank-two channel. -/
theorem factor_not_injective_of_not_injective {X : E →ₗ[𝕜] H} {Y : F →ₗ[𝕜] H}
    (hX : Function.Injective X) (hY : ¬ Function.Injective Y) {W : F →ₗ[𝕜] E}
    (hW : X ∘ₗ W = Y) : ¬ Function.Injective W := by
  intro hWinj
  refine hY fun a b hab => hWinj ?_
  refine hX ?_
  have hXW : ∀ f : F, X (W f) = Y f := fun f => congrArg (fun g : F →ₗ[𝕜] H => g f) hW
  rw [hXW, hXW, hab]

/-- **The hypothesis is `X X* = Y Y*`, not equality of ranges.** Doubling `Y` leaves the range
alone and the factor is multiplication by `2`, which is not unitary. -/
theorem range_eq_insufficient [Nontrivial E] {X : E →ₗ[𝕜] H} (hX : Function.Injective X) :
    range ((2 : 𝕜) • X) = range X ∧
      ∀ W : E →ₗ[𝕜] E, X ∘ₗ W = (2 : 𝕜) • X → adjoint W ∘ₗ W ≠ LinearMap.id := by
  have htwo : (2 : 𝕜) ≠ 0 := two_ne_zero
  constructor
  · refine le_antisymm ?_ ?_
    · rintro _ ⟨e, rfl⟩; exact ⟨(2 : 𝕜) • e, by simp⟩
    · rintro _ ⟨e, rfl⟩; exact ⟨(2 : 𝕜)⁻¹ • e, by simp [smul_smul]⟩
  · intro W hW hcon
    -- the factor is multiplication by `2`, and an isometry would force `4 = 1`
    have hWe : ∀ e : E, W e = (2 : 𝕜) • e := by
      intro e
      refine hX ?_
      have := congrArg (fun g : E →ₗ[𝕜] H => g e) hW
      simpa using this
    obtain ⟨e, he⟩ := exists_ne (0 : E)
    have hiso : ⟪W e, W e⟫ = ⟪e, e⟫ := by
      have hpt : adjoint W (W e) = e := congrArg (fun g : E →ₗ[𝕜] E => g e) hcon
      rw [← adjoint_inner_left W e (W e), hpt]
    rw [hWe] at hiso
    rw [inner_smul_left, inner_smul_right] at hiso
    have h4 : ((4 : 𝕜) - 1) * ⟪e, e⟫ = 0 := by
      have : (starRingEnd 𝕜) 2 * (2 * ⟪e, e⟫) = ⟪e, e⟫ := hiso
      rw [map_ofNat] at this
      linear_combination this
    have hne : (⟪e, e⟫ : 𝕜) ≠ 0 := fun hz => he (inner_self_eq_zero.1 hz)
    rcases mul_eq_zero.1 h4 with hz | hz
    · have : (4 : 𝕜) = 1 := by linear_combination hz
      norm_num at this
    · exact hne hz

/-! ### What these proofs rest on -/

#print axioms range_eq_of_comp_adjoint_eq
#print axioms surjective_adjoint_of_injective
#print axioms comp_factor
#print axioms factor_unique
#print axioms factor_comp_adjoint
#print axioms adjoint_comp_factor
#print axioms existsUnique_unitary_factor
#print axioms finrank_eq
#print axioms factor_not_unique_of_not_injective
#print axioms factor_not_injective_of_not_injective
#print axioms range_eq_insufficient

end FactorUniqueness

end OIBridge
