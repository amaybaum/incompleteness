/-
  OIBridge/AccessibleAlgebra.lean — phase three, round five: the generated accessible
  algebra and the trivial-commutant criterion (milestone C3a).

  THE OBJECT. A coherent completion hands the observer an operator family, not a Hilbert
  space: the block readouts `P_j = |j⟩⟨j| ⊗ I_A` and their Heisenberg conjugates
  `U_t (ℐ_a†(P_j) ⊗ I_A) U_t†` under the carrier propagator, for every time and every
  visible-local intervention in the menu. The generated *-algebra 𝔄_OI of this family is
  the accessible algebra of the completion. C3a asks when 𝔄_OI is the FULL matrix algebra
  M_D(ℂ); by Burnside/double-commutant it suffices that the commutant of the generating
  family is trivial, and that commutant is computed here exactly.

  WHAT IS PROVED.

  Section A — the Dedekind core, reusable form.
    * `gap_coefficient_vanish` — a finite gap-frequency combination vanishing at all times
      has every nondegenerate-gap coefficient zero (character independence + the singleton
      fiber). The zero-target form of the phase-three reduction engine.

  Section B — the eigen-dyad calculus.
    * `dyad`, `mul_dyad`, `dyad_mul`, `dyad_conjugation`, `dyad_conjugation_apply` — the
      rank-one probes `|v_β⟩⟨v_α|` built from carrier columns, and their exact eigenbasis
      conjugation: sandwiching the commutator `[Z, |v_β⟩⟨v_α|]` between `Vᴴ…V` produces
      matrix units against `W = Vᴴ Z V`. This is what turns ONE trace expansion into
      entry-resolved commutant equations.

  Section C — THE GENERATION THEOREM.
    * `accessible_trivial_commutant` — for a unitary carrier with nondegenerate gaps, any
      operator commuting with the full-time Heisenberg orbit `{U_t A_j U_t†}` of a family
      whose eigenbasis matrices `N_j = Vᴴ A_j V` jointly cover every off-diagonal entry
      (∀ a ≠ b ∃ j, N_j[a,b] ≠ 0) is a SCALAR. The completeness hypothesis is LITERALLY
      the readout-completeness condition `hread` of `two_time_necessary`: the same
      alignment datum drives stationarity forcing and algebra generation.
    * `native_menu_generates` — the specialization to the bare block readouts: NO probe is
      needed for generation on a readout-complete carrier. This DEVIATES from the round's
      prior expectation (that removing the complex probe leaves a nontrivial linear
      commutant): probe F17 confirms the native commutant is already trivial on every
      aligned stratum. The complex probe's exclusive content is NOT irreducibility.
    * `complexProbe_trivialCommutant` — the requested named criterion: a single
      visible-local probed readout family `vlift (Gᴴ P_i G)` with eigenbasis-complete
      response makes the commutant trivial. Its role on carriers whose native menu is
      blind at some eigenvector pair: a probe with visible off-diagonal support restores
      completeness (probe F17 exhibits the stratum at shape (3,2)).

  Section D — countercontrol I: the decoupled ancilla.
    * `decoupled_carrier_commutes` / `ancillaPhase_not_scalar` — if every carrier
      eigenvector lies in a single ancilla sector (`hdec`), the ancilla phase
      `diagonal (y ∘ snd)` commutes with the ENTIRE accessible family of EVERY
      visible-local menu — the complex probe included — and is not scalar once `y` is
      nonconstant. Generation is a property of carrier ALIGNMENT (eigenbasis
      completeness), not of menu size; no visible-local instrument sees a decoupled
      ancilla. This is the C3-side face of the locality countercontrol of round three.

  Section E — countercontrol II: the antilinear residue.
    * `real_menu_conjugation_stable` — for a real carrier and a real menu element,
      entrywise conjugation maps each accessible operator to the accessible operator of
      the REFLECTED spectrum: the accessible family of the real menu is stable under the
      antiunitary, so the phase-two ℤ₂ survives generation. Together with
      `accessible_trivial_commutant` this locates the ℤ₂ precisely: it is NOT a linear
      commutant direction (those are all dead), it is the antilinear symmetry of the
      generating set — the Jordan/transpose branch that C3b must close.
    * `probeResp_is_probe_response`, `complexProbe_breaks_conjugation` — an exact unitary
      complex probe whose response is NOT conjugation-fixed: the externally oriented
      reference that breaks the ℤ₂, consistent with phase two's antiunitary invariance.

  WHAT THIS DOES NOT ESTABLISH. Trivial commutant gives 𝔄_OI = M_D(ℂ) via Burnside; the
  double-commutant step itself is not formalized here — C3b consumes the commutant
  computation directly (two completions with identical data will induce a map fixing the
  generating family, and rigidity lives at the level of that family). Nothing here is a
  uniqueness statement about completions: C3b/C3c remain open, and the classification
  target retains the mandatory existence qualifier — some carriers admit NO completion
  (`twoByTwo_no_local_lift`), so any final theorem classifies the completions that exist.
-/
import OIBridge.CoherentLift

namespace OIBridge
namespace AccessibleAlgebra

open Complex Matrix CoherentLift

/-! ### Section A — the Dedekind core, zero-target form -/

variable {Dm : ℕ}

/-- **The vanishing of nondegenerate gap coefficients.** A pair-indexed exponential
combination over the gap frequencies that vanishes at every time has zero coefficient at
every nondegenerate pair: Dedekind independence of the characters plus the singleton fiber
of a distinct-gap spectrum. The reusable core of `two_time_forces_stationary`, stated with
target zero so commutator equations feed it directly. -/
theorem gap_coefficient_vanish (E : Fin Dm → ℝ)
    (hgap : ∀ a b c d : Fin Dm, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (F : Fin Dm × Fin Dm → ℂ)
    (hzero : ∀ t : ℝ, ∑ q : Fin Dm × Fin Dm,
      F q * Complex.exp (Complex.I * ((E q.2 - E q.1 : ℝ) : ℂ) * (t : ℂ)) = 0)
    {a b : Fin Dm} (hab : a ≠ b) : F (a, b) = 0 := by
  have hfib : ∀ t : ℝ, ∑ ω ∈ BohrFrequency.gaps E,
      (∑ q ∈ Finset.univ.filter (fun q : Fin Dm × Fin Dm => E q.2 - E q.1 = ω), F q)
        * Complex.exp (Complex.I * (ω : ℂ) * (t : ℂ)) = 0 := by
    intro t
    rw [← hzero t]
    rw [← Finset.sum_fiberwise_of_maps_to
      (g := fun q : Fin Dm × Fin Dm => E q.2 - E q.1)
      (fun q _ => Finset.mem_image_of_mem _ (Finset.mem_univ q))]
    refine Finset.sum_congr rfl fun ω _ => ?_
    rw [Finset.sum_mul]
    refine Finset.sum_congr rfl fun q hq => ?_
    rw [(Finset.mem_filter.mp hq).2]
  have hc := BohrFrequency.coeffs_eq_zero hfib
  have hmem : (E b - E a : ℝ) ∈ BohrFrequency.gaps E := by
    rw [BohrFrequency.gaps]
    exact Finset.mem_image.mpr ⟨(a, b), Finset.mem_univ _, rfl⟩
  have hval := hc _ hmem
  rw [BohrFrequency.fiber_singleton hgap hab, Finset.sum_singleton] at hval
  exact hval

/-! ### Section B — the eigen-dyad calculus -/

/-- The dyad `|P_•β⟩⟨Q_•α|` of two column families: the rank-one operator carried by the
`β`-th column of `P` against the `α`-th column of `Q`. With `P = Q = V` this is the
eigenvector dyad `|v_β⟩⟨v_α|` of the carrier. -/
def dyad {m₁ m₂ : Type*} (P : Matrix m₁ (Fin Dm) ℂ) (Q : Matrix m₂ (Fin Dm) ℂ)
    (β α : Fin Dm) : Matrix m₁ m₂ ℂ :=
  Matrix.of fun x y => P x β * star (Q y α)

theorem dyad_apply {m₁ m₂ : Type*} (P : Matrix m₁ (Fin Dm) ℂ) (Q : Matrix m₂ (Fin Dm) ℂ)
    (β α : Fin Dm) (x : m₁) (y : m₂) :
    dyad P Q β α x y = P x β * star (Q y α) := rfl

/-- Left multiplication acts on the ket column. -/
theorem mul_dyad {m₀ m₁ m₂ : Type*} [Fintype m₁] (Z : Matrix m₀ m₁ ℂ)
    (P : Matrix m₁ (Fin Dm) ℂ) (Q : Matrix m₂ (Fin Dm) ℂ) (β α : Fin Dm) :
    Z * dyad P Q β α = dyad (Z * P) Q β α := by
  ext p q
  rw [Matrix.mul_apply, dyad_apply, Matrix.mul_apply, Finset.sum_mul]
  refine Finset.sum_congr rfl fun r _ => ?_
  rw [dyad_apply]
  ring

/-- Right multiplication acts on the bra column through the adjoint. -/
theorem dyad_mul {m₁ m₂ m₃ : Type*} [Fintype m₂] (P : Matrix m₁ (Fin Dm) ℂ)
    (Q : Matrix m₂ (Fin Dm) ℂ) (Z : Matrix m₂ m₃ ℂ) (β α : Fin Dm) :
    dyad P Q β α * Z = dyad P (Zᴴ * Q) β α := by
  ext p q
  rw [Matrix.mul_apply, dyad_apply, Matrix.mul_apply, star_sum, Finset.mul_sum]
  refine Finset.sum_congr rfl fun r _ => ?_
  rw [dyad_apply, star_mul', Matrix.conjTranspose_apply, star_star]
  ring

variable {n : Type*} [Fintype n] [DecidableEq n]

omit [DecidableEq n] in
/-- **The eigenbasis conjugation of a dyad commutator.** Sandwiching `[Z, |v_β⟩⟨v_α|]`
between `Vᴴ…V` for a coisometric carrier produces matrix units against `W = Vᴴ Z V`:
the exact bridge from one trace expansion to entry-resolved commutant equations. -/
theorem dyad_conjugation (V : Matrix n (Fin Dm) ℂ) (hV' : Vᴴ * V = 1)
    (Z : Matrix n n ℂ) (β α : Fin Dm) :
    Vᴴ * (Z * dyad V V β α - dyad V V β α * Z) * V
      = dyad (Vᴴ * Z * V) (1 : Matrix (Fin Dm) (Fin Dm) ℂ) β α
        - dyad (1 : Matrix (Fin Dm) (Fin Dm) ℂ) (Vᴴ * Zᴴ * V) β α := by
  rw [Matrix.mul_sub, Matrix.sub_mul]
  congr 1
  · rw [mul_dyad, mul_dyad, dyad_mul, hV', ← Matrix.mul_assoc]
  · rw [dyad_mul, mul_dyad, dyad_mul, hV', ← Matrix.mul_assoc]

omit [DecidableEq n] in
/-- The entry form of `dyad_conjugation`, ready for the coefficient equations. -/
theorem dyad_conjugation_apply (V : Matrix n (Fin Dm) ℂ) (hV' : Vᴴ * V = 1)
    (Z : Matrix n n ℂ) (β α x y : Fin Dm) :
    (Vᴴ * (Z * dyad V V β α - dyad V V β α * Z) * V) x y
      = (Vᴴ * Z * V) x β * (1 : Matrix (Fin Dm) (Fin Dm) ℂ) α y
        - (1 : Matrix (Fin Dm) (Fin Dm) ℂ) x β * (Vᴴ * Z * V) α y := by
  rw [dyad_conjugation V hV' Z β α, Matrix.sub_apply, dyad_apply, dyad_apply,
    ← Matrix.conjTranspose_apply, ← Matrix.conjTranspose_apply, Matrix.conjTranspose_one,
    Matrix.conjTranspose_mul, Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose,
    Matrix.conjTranspose_conjTranspose, ← Matrix.mul_assoc]

/-! ### Section C — the generation theorem -/

/-- **THE TRIVIAL-COMMUTANT CRITERION (C3a).** Let `V` be a unitary carrier with
nondegenerate gaps and `{A_j}` an operator family whose eigenbasis matrices jointly cover
every off-diagonal entry — the SAME readout-completeness datum `hread` that drives
`two_time_necessary`. Then any operator commuting with the full-time Heisenberg orbit
`{U_t A_j U_t†}` is a scalar: the commutant of the accessible family is `ℂ·I`, so the
generated accessible algebra 𝔄_OI is irreducible (and by Burnside, all of `M_D(ℂ)`).

Mechanism: for each eigen-dyad `|v_β⟩⟨v_α|`, cyclicity turns the commutation into the
vanishing of a gap-frequency expansion (`intervened_readout_expansion` with the dyad
commutator as readout); the singleton fibers deliver, at each pair `a ≠ b`,
`N_j[a,b]·(W[b,β]·1[α,a] − 1[b,β]·W[α,a]) = 0`. Choosing `(α,β) = (a,a')` kills every
off-diagonal entry of `W = Vᴴ Z V`; choosing `(α,β) = (a,b)` equalizes the diagonal. -/
theorem accessible_trivial_commutant {ι' : Type*} [NeZero Dm]
    (V : Matrix n (Fin Dm) ℂ) (E : Fin Dm → ℝ) (A : ι' → Matrix n n ℂ)
    (Z : Matrix n n ℂ) (hV : V * Vᴴ = 1) (hV' : Vᴴ * V = 1)
    (hgap : ∀ a b c d : Fin Dm, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hcomplete : ∀ a b : Fin Dm, a ≠ b → ∃ j, (Vᴴ * A j * V) a b ≠ 0)
    (hcomm : ∀ (j : ι') (t : ℝ),
      Matrix.of (BohrFrequency.Umat V E t) * A j * (Matrix.of (BohrFrequency.Umat V E t))ᴴ * Z
        = Z * (Matrix.of (BohrFrequency.Umat V E t) * A j
            * (Matrix.of (BohrFrequency.Umat V E t))ᴴ)) :
    ∃ c : ℂ, Z = c • 1 := by
  have hcoef : ∀ (j : ι') (α β a b : Fin Dm), a ≠ b →
      (Vᴴ * A j * V) a b
        * ((Vᴴ * Z * V) b β * (1 : Matrix (Fin Dm) (Fin Dm) ℂ) α a
          - (1 : Matrix (Fin Dm) (Fin Dm) ℂ) b β * (Vᴴ * Z * V) α a) = 0 := by
    intro j α β a b hab
    have htr : ∀ t : ℝ, Matrix.trace ((Z * dyad V V β α - dyad V V β α * Z)
        * (Matrix.of (BohrFrequency.Umat V E t) * A j
          * (Matrix.of (BohrFrequency.Umat V E t))ᴴ)) = 0 := by
      intro t
      have hc := hcomm j t
      rw [Matrix.sub_mul, Matrix.trace_sub, Matrix.trace_mul_cycle, hc,
        Matrix.trace_mul_cycle, sub_self]
    have hzero : ∀ t : ℝ, ∑ q : Fin Dm × Fin Dm,
        (Vᴴ * A j * V) q.1 q.2
          * (Vᴴ * (Z * dyad V V β α - dyad V V β α * Z) * V) q.2 q.1
          * Complex.exp (Complex.I * ((E q.2 - E q.1 : ℝ) : ℂ) * (t : ℂ)) = 0 := by
      intro t
      rw [← intervened_readout_expansion (Z * dyad V V β α - dyad V V β α * Z) (A j) V E t]
      exact htr t
    have hF := gap_coefficient_vanish E hgap
      (fun q : Fin Dm × Fin Dm => (Vᴴ * A j * V) q.1 q.2
        * (Vᴴ * (Z * dyad V V β α - dyad V V β α * Z) * V) q.2 q.1) hzero hab
    have hF' : (Vᴴ * A j * V) a b
        * (Vᴴ * (Z * dyad V V β α - dyad V V β α * Z) * V) b a = 0 := hF
    rw [dyad_conjugation_apply V hV' Z β α b a] at hF'
    exact hF'
  have hoff : ∀ x y : Fin Dm, x ≠ y → (Vᴴ * Z * V) x y = 0 := by
    intro x y hxy
    obtain ⟨j, hj⟩ := hcomplete y x (Ne.symm hxy)
    have h := hcoef j y y y x (Ne.symm hxy)
    rw [Matrix.one_apply_eq, Matrix.one_apply_ne hxy, mul_one, zero_mul, sub_zero] at h
    exact (mul_eq_zero.mp h).resolve_left hj
  have hdiag : ∀ x y : Fin Dm, (Vᴴ * Z * V) x x = (Vᴴ * Z * V) y y := by
    intro x y
    by_cases hxy : x = y
    · rw [hxy]
    · obtain ⟨j, hj⟩ := hcomplete x y hxy
      have h := hcoef j x y x y hxy
      rw [Matrix.one_apply_eq, Matrix.one_apply_eq, mul_one, one_mul] at h
      exact (sub_eq_zero.mp ((mul_eq_zero.mp h).resolve_left hj)).symm
  obtain ⟨c, hWc⟩ : ∃ c : ℂ, Vᴴ * Z * V = c • (1 : Matrix (Fin Dm) (Fin Dm) ℂ) := by
    refine ⟨(Vᴴ * Z * V) 0 0, ?_⟩
    ext x y
    rw [Matrix.smul_apply, Matrix.one_apply]
    by_cases hxy : x = y
    · rw [if_pos hxy, smul_eq_mul, mul_one]
      subst hxy
      exact hdiag x 0
    · rw [if_neg hxy, smul_zero]
      exact hoff x y hxy
  refine ⟨c, ?_⟩
  calc Z = V * Vᴴ * Z * (V * Vᴴ) := by rw [hV, Matrix.one_mul, Matrix.mul_one]
    _ = V * (Vᴴ * Z * V) * Vᴴ := by simp only [Matrix.mul_assoc]
    _ = V * (c • (1 : Matrix (Fin Dm) (Fin Dm) ℂ)) * Vᴴ := by rw [hWc]
    _ = c • (V * Vᴴ) := by rw [Matrix.mul_smul, Matrix.smul_mul, Matrix.mul_one]
    _ = c • (1 : Matrix n n ℂ) := by rw [hV]

variable {Sv Sa : Type*} [Fintype Sv] [DecidableEq Sv] [Fintype Sa] [DecidableEq Sa]

/-- **Generation without any probe.** On a readout-complete carrier the bare block
readouts already have trivial commutant: the hypothesis is the SAME `hread` consumed by
`two_time_necessary`. Probe F17 verdict: every aligned stratum of the phase-three census
satisfies it, so the native permutation menu generates `M_D(ℂ)` there — the complex
probe is NOT needed for irreducibility. Its exclusive content is the antilinear ℤ₂
(Section E), exactly as phase two's antiunitary invariance demands. -/
theorem native_menu_generates [NeZero Dm]
    (V : Matrix (Sv × Sa) (Fin Dm) ℂ) (E : Fin Dm → ℝ)
    (Z : Matrix (Sv × Sa) (Sv × Sa) ℂ) (hV : V * Vᴴ = 1) (hV' : Vᴴ * V = 1)
    (hgap : ∀ a b c d : Fin Dm, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hread : ∀ a b : Fin Dm, a ≠ b →
      ∃ j : Sv, (Vᴴ * readProj (Prod.fst : Sv × Sa → Sv) j * V) a b ≠ 0)
    (hcomm : ∀ (j : Sv) (t : ℝ),
      Matrix.of (BohrFrequency.Umat V E t) * readProj (Prod.fst : Sv × Sa → Sv) j
          * (Matrix.of (BohrFrequency.Umat V E t))ᴴ * Z
        = Z * (Matrix.of (BohrFrequency.Umat V E t) * readProj (Prod.fst : Sv × Sa → Sv) j
          * (Matrix.of (BohrFrequency.Umat V E t))ᴴ)) :
    ∃ c : ℂ, Z = c • 1 :=
  accessible_trivial_commutant V E
    (fun j : Sv => readProj (Prod.fst : Sv × Sa → Sv) j) Z hV hV' hgap hread hcomm

/-- **`complexProbe_trivialCommutant` (C3a, the named criterion).** A single
visible-local probed readout family — the instrument `G` applied on the visible factor
only, its branch readouts entering through the locality guard `vlift` — has trivial
commutant whenever its eigenbasis response covers every off-diagonal entry. On carriers
whose native menu is blind at some eigenvector pair (F17 exhibits the stratum at (3,2):
two product eigenvectors sharing an ancilla state), a probe with visible off-diagonal
support restores completeness and with it generation. -/
theorem complexProbe_trivialCommutant [NeZero Dm]
    (V : Matrix (Sv × Sa) (Fin Dm) ℂ) (E : Fin Dm → ℝ) (G : Matrix Sv Sv ℂ)
    (Z : Matrix (Sv × Sa) (Sv × Sa) ℂ) (hV : V * Vᴴ = 1) (hV' : Vᴴ * V = 1)
    (hgap : ∀ a b c d : Fin Dm, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hcomplete : ∀ a b : Fin Dm, a ≠ b → ∃ i : Sv,
      (Vᴴ * (vlift (Gᴴ * readProj (id : Sv → Sv) i * G) : Matrix (Sv × Sa) (Sv × Sa) ℂ)
        * V) a b ≠ 0)
    (hcomm : ∀ (i : Sv) (t : ℝ),
      Matrix.of (BohrFrequency.Umat V E t)
          * (vlift (Gᴴ * readProj (id : Sv → Sv) i * G) : Matrix (Sv × Sa) (Sv × Sa) ℂ)
          * (Matrix.of (BohrFrequency.Umat V E t))ᴴ * Z
        = Z * (Matrix.of (BohrFrequency.Umat V E t)
          * (vlift (Gᴴ * readProj (id : Sv → Sv) i * G) : Matrix (Sv × Sa) (Sv × Sa) ℂ)
          * (Matrix.of (BohrFrequency.Umat V E t))ᴴ)) :
    ∃ c : ℂ, Z = c • 1 :=
  accessible_trivial_commutant V E
    (fun i : Sv => (vlift (Gᴴ * readProj (id : Sv → Sv) i * G) : Matrix (Sv × Sa) (Sv × Sa) ℂ))
    Z hV hV' hgap hcomplete hcomm

/-! ### Section D — countercontrol I: the decoupled ancilla -/

/-- Ancilla-block-diagonality: the operator never connects distinct ancilla sectors. -/
def AncillaBlockDiagonal (B : Matrix (Sv × Sa) (Sv × Sa) ℂ) : Prop :=
  ∀ p q : Sv × Sa, p.2 ≠ q.2 → B p q = 0

omit [Fintype Sv] [DecidableEq Sv] [Fintype Sa] in
theorem vlift_ancillaBlockDiagonal (M : Matrix Sv Sv ℂ) :
    AncillaBlockDiagonal (vlift M : Matrix (Sv × Sa) (Sv × Sa) ℂ) := by
  intro p q h
  show M p.1 q.1 * (if p.2 = q.2 then (1 : ℂ) else 0) = 0
  rw [if_neg h, mul_zero]

omit [DecidableEq Sv] in
theorem ancillaBlockDiagonal_mul {B C : Matrix (Sv × Sa) (Sv × Sa) ℂ}
    (hB : AncillaBlockDiagonal B) (hC : AncillaBlockDiagonal C) :
    AncillaBlockDiagonal (B * C) := by
  intro p q h
  rw [Matrix.mul_apply]
  refine Finset.sum_eq_zero fun r _ => ?_
  by_cases hr : p.2 = r.2
  · rw [hC r q (hr ▸ h), mul_zero]
  · rw [hB p r hr, zero_mul]

omit [Fintype Sv] [DecidableEq Sv] [Fintype Sa] [DecidableEq Sa] in
theorem ancillaBlockDiagonal_conjTranspose {B : Matrix (Sv × Sa) (Sv × Sa) ℂ}
    (hB : AncillaBlockDiagonal B) : AncillaBlockDiagonal Bᴴ := by
  intro p q h
  rw [Matrix.conjTranspose_apply, hB q p (Ne.symm h), star_zero]

omit [Fintype Sv] [DecidableEq Sv] [Fintype Sa] [DecidableEq Sa] in
/-- A carrier whose eigenvectors each live in one ancilla sector propagates without
connecting sectors, at every time. -/
theorem umat_ancillaBlockDiagonal (V : Matrix (Sv × Sa) (Fin Dm) ℂ) (E : Fin Dm → ℝ)
    (τ : Fin Dm → Sa) (hdec : ∀ (p : Sv × Sa) (k : Fin Dm), V p k ≠ 0 → p.2 = τ k)
    (t : ℝ) : AncillaBlockDiagonal (Matrix.of (BohrFrequency.Umat V E t)) := by
  intro p q h
  show (∑ k, V p k * Complex.exp (-(Complex.I * (E k : ℂ) * (t : ℂ))) * star (V q k)) = 0
  refine Finset.sum_eq_zero fun k _ => ?_
  by_cases hp : V p k = 0
  · rw [hp, zero_mul, zero_mul]
  · by_cases hq : V q k = 0
    · rw [hq, star_zero, mul_zero]
    · exact absurd ((hdec p k hp).trans (hdec q k hq).symm) h

/-- **THE MENU-INDEPENDENT COUNTERCONTROL.** On a sector-decoupled carrier the ancilla
phase `diagonal (y ∘ snd)` commutes with the whole accessible family of EVERY
visible-local menu — arbitrary `M`, arbitrary time, the complex probe included. The
completeness hypothesis of the generation theorem is therefore not a formality: where it
fails by decoupling, no visible-local instrument whatsoever restores generation. (Via
`readProj_fst_vlift`, the native block readouts are the case `M = readProj id j`.) -/
theorem decoupled_carrier_commutes (V : Matrix (Sv × Sa) (Fin Dm) ℂ) (E : Fin Dm → ℝ)
    (τ : Fin Dm → Sa) (hdec : ∀ (p : Sv × Sa) (k : Fin Dm), V p k ≠ 0 → p.2 = τ k)
    (y : Sa → ℂ) (M : Matrix Sv Sv ℂ) (t : ℝ) :
    (Matrix.of (BohrFrequency.Umat V E t) * vlift M
        * (Matrix.of (BohrFrequency.Umat V E t))ᴴ)
      * Matrix.diagonal (fun p : Sv × Sa => y p.2)
    = Matrix.diagonal (fun p : Sv × Sa => y p.2)
      * (Matrix.of (BohrFrequency.Umat V E t) * vlift M
        * (Matrix.of (BohrFrequency.Umat V E t))ᴴ) := by
  have hABD : AncillaBlockDiagonal (Matrix.of (BohrFrequency.Umat V E t) * vlift M
      * (Matrix.of (BohrFrequency.Umat V E t))ᴴ) :=
    ancillaBlockDiagonal_mul
      (ancillaBlockDiagonal_mul (umat_ancillaBlockDiagonal V E τ hdec t)
        (vlift_ancillaBlockDiagonal M))
      (ancillaBlockDiagonal_conjTranspose (umat_ancillaBlockDiagonal V E τ hdec t))
  ext p q
  simp only [Matrix.mul_diagonal, Matrix.diagonal_mul]
  by_cases h : p.2 = q.2
  · rw [h, mul_comm]
  · rw [hABD p q h, mul_zero, zero_mul]

omit [Fintype Sv] [Fintype Sa] in
/-- The ancilla phase is not scalar once `y` separates two sectors. -/
theorem ancillaPhase_not_scalar [Nonempty Sv] (y : Sa → ℂ) {a b : Sa} (hy : y a ≠ y b) :
    ¬ ∃ c : ℂ, Matrix.diagonal (fun p : Sv × Sa => y p.2)
      = c • (1 : Matrix (Sv × Sa) (Sv × Sa) ℂ) := by
  rintro ⟨c, hc⟩
  obtain ⟨i⟩ := ‹Nonempty Sv›
  have hent : ∀ p : Sv × Sa, Matrix.diagonal (fun p : Sv × Sa => y p.2) p p
      = (c • (1 : Matrix (Sv × Sa) (Sv × Sa) ℂ)) p p := fun p => by rw [hc]
  have ha := hent (i, a)
  have hb := hent (i, b)
  rw [Matrix.diagonal_apply_eq, Matrix.smul_apply, Matrix.one_apply_eq, smul_eq_mul,
    mul_one] at ha hb
  exact hy (ha.trans hb.symm)

/-! ### Section E — countercontrol II: the antilinear residue -/

theorem conjOp_mul {m : Type*} [Fintype m] (B C : Matrix m m ℂ) :
    AntiunitaryInvariance.conjOp (B * C)
      = AntiunitaryInvariance.conjOp B * AntiunitaryInvariance.conjOp C :=
  Matrix.map_mul

theorem conjOp_conjTranspose_swap {m : Type*} (M : Matrix m m ℂ) :
    AntiunitaryInvariance.conjOp Mᴴ = (AntiunitaryInvariance.conjOp M)ᴴ := by
  have h1 := AntiunitaryInvariance.transpose_conjTranspose_eq Mᴴ
  rw [Matrix.conjTranspose_conjTranspose] at h1
  rw [← h1, AntiunitaryInvariance.conjOp_conjTranspose]

/-- **The antilinear symmetry of the real accessible family.** For a real carrier and a
conjugation-fixed menu element, entrywise conjugation carries each accessible operator to
the accessible operator of the reflected spectrum: `Θ(U_t^E A U_t^{E,†}) =
U_t^{−E} A U_t^{−E,†}`. The accessible family of the real menu is Θ-stable, so even
though its LINEAR commutant is trivial (`accessible_trivial_commutant` — generation
holds), the antiunitary ℤ₂ of phase two survives as a symmetry of the generating set:
the transpose branch that C3b's Jordan rigidity must and does retain. A genuinely
complex probe response is not conjugation-fixed (`complexProbe_breaks_conjugation`) and
is exactly what removes it. -/
theorem real_menu_conjugation_stable {n' : Type*} [Fintype n']
    (V : Matrix n' (Fin Dm) ℂ) (E : Fin Dm → ℝ) (A : Matrix n' n' ℂ) (t : ℝ)
    (hVreal : ∀ p a, star (V p a) = V p a)
    (hAreal : AntiunitaryInvariance.conjOp A = A) :
    AntiunitaryInvariance.conjOp (Matrix.of (BohrFrequency.Umat V E t) * A
        * (Matrix.of (BohrFrequency.Umat V E t))ᴴ)
      = Matrix.of (BohrFrequency.Umat V (fun a => -(E a)) t) * A
        * (Matrix.of (BohrFrequency.Umat V (fun a => -(E a)) t))ᴴ := by
  rw [conjOp_mul, conjOp_mul, hAreal, conjOp_conjTranspose_swap,
    ← umat_conjOp_reflect V E t hVreal]

omit [Fintype Sv] [DecidableEq Sv] [Fintype Sa] in
/-- The conjugation acts through the locality guard: real visible instruments stay real
after lifting. -/
theorem conjOp_vlift (M : Matrix Sv Sv ℂ) :
    AntiunitaryInvariance.conjOp (vlift M : Matrix (Sv × Sa) (Sv × Sa) ℂ)
      = vlift (AntiunitaryInvariance.conjOp M) := by
  ext p q
  simp only [AntiunitaryInvariance.conjOp, Matrix.map_apply]
  show star (M p.1 q.1 * (if p.2 = q.2 then (1 : ℂ) else 0))
    = star (M p.1 q.1) * (if p.2 = q.2 then (1 : ℂ) else 0)
  rw [star_mul']
  congr 1
  by_cases h : p.2 = q.2 <;> simp [h]

/-- The oriented probe: a unitary complex instrument on a two-state visible factor. -/
noncomputable def probeG : Matrix (Fin 2) (Fin 2) ℂ :=
  !![((3/5 : ℝ) : ℂ), -((4/5 : ℝ) : ℂ) * Complex.I;
     ((4/5 : ℝ) : ℂ), ((3/5 : ℝ) : ℂ) * Complex.I]

/-- Its branch-0 readout response `Gᴴ P₀ G`. -/
noncomputable def probeResp : Matrix (Fin 2) (Fin 2) ℂ :=
  !![((9/25 : ℝ) : ℂ), -((12/25 : ℝ) : ℂ) * Complex.I;
     ((12/25 : ℝ) : ℂ) * Complex.I, ((16/25 : ℝ) : ℂ)]

/-- The probe is a genuine instrument: `probeG` is unitary. -/
theorem probeG_unitary : probeGᴴ * probeG = 1 := by
  ext i j
  rw [Matrix.mul_apply, Fin.sum_univ_two]
  fin_cases i <;> fin_cases j <;>
    simp [probeG, Matrix.conjTranspose_apply, Complex.ext_iff,
      Complex.mul_re, Complex.mul_im, -Complex.ofReal_div] <;>
    norm_num

/-- The oriented witness is a genuine probed readout: `probeResp = probeGᴴ P₀ probeG`. -/
theorem probeResp_is_probe_response :
    probeResp = probeGᴴ * readProj (id : Fin 2 → Fin 2) 0 * probeG := by
  ext i j
  rw [Matrix.mul_apply, Fin.sum_univ_two]
  fin_cases i <;> fin_cases j <;>
    simp [probeG, probeResp, readProj, Matrix.mul_apply, Matrix.conjTranspose_apply,
      Matrix.diagonal_apply, Complex.ext_iff, Complex.mul_re, Complex.mul_im,
      -Complex.ofReal_div] <;>
    norm_num

/-- **The ℤ₂ breaker.** The complex probe's response is not conjugation-fixed: it is the
externally oriented reference. Removing it restores Θ-stability of the accessible family
(`real_menu_conjugation_stable`), which is the honest content of "removing the complex
probe leaves a nontrivial commutant" — the residue is ANTILINEAR, not a linear commutant
direction. -/
theorem complexProbe_breaks_conjugation :
    AntiunitaryInvariance.conjOp probeResp ≠ probeResp := by
  intro h
  have h01 : AntiunitaryInvariance.conjOp probeResp 0 1 = probeResp 0 1 := by rw [h]
  simp only [AntiunitaryInvariance.conjOp, Matrix.map_apply, probeResp] at h01
  rw [show (!![((9/25 : ℝ) : ℂ), -((12/25 : ℝ) : ℂ) * Complex.I;
      ((12/25 : ℝ) : ℂ) * Complex.I, ((16/25 : ℝ) : ℂ)] : Matrix (Fin 2)
      (Fin 2) ℂ) 0 1 = -((12/25 : ℝ) : ℂ) * Complex.I from by simp] at h01
  have h2 : ((12/25 : ℝ) : ℂ) * Complex.I = -((12/25 : ℝ) : ℂ) * Complex.I := by
    calc ((12/25 : ℝ) : ℂ) * Complex.I
        = (starRingEnd ℂ) (-((12/25 : ℝ) : ℂ) * Complex.I) := by
          rw [map_mul, Complex.conj_I, map_neg, Complex.conj_ofReal]
          ring
      _ = -((12/25 : ℝ) : ℂ) * Complex.I := h01
  have h3 := mul_right_cancel₀ Complex.I_ne_zero h2
  have h4 : (12/25 : ℝ) = -(12/25) := by exact_mod_cast h3
  norm_num at h4

#print axioms gap_coefficient_vanish
#print axioms dyad_conjugation
#print axioms dyad_conjugation_apply
#print axioms accessible_trivial_commutant
#print axioms native_menu_generates
#print axioms complexProbe_trivialCommutant
#print axioms vlift_ancillaBlockDiagonal
#print axioms ancillaBlockDiagonal_mul
#print axioms umat_ancillaBlockDiagonal
#print axioms decoupled_carrier_commutes
#print axioms ancillaPhase_not_scalar
#print axioms conjOp_mul
#print axioms conjOp_vlift
#print axioms real_menu_conjugation_stable
#print axioms probeG_unitary
#print axioms probeResp_is_probe_response
#print axioms complexProbe_breaks_conjugation

end AccessibleAlgebra
end OIBridge
