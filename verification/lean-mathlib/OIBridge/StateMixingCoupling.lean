import OIBridge.CoherentContinuumSource

/-!
# The state-mixing coupling construction audit — one sourced pair coupling and the completion

The preregistered pass of `STATE-MIXING-COUPLING-AUDIT.md`, read under its scope amendment.
Nothing here is named "C5" or "minimal"; the datum is a postulate, and nothing here derives it.

* T1, the datum: a real mixing angle `θ` on the two values of one site, sourced to the real
  rotation `rot θ = [[cos θ, −sin θ], [sin θ, cos θ]]` and transported to every level with the
  ancilla a spectator (`mixImage n θ`). The class `MixR D` is the closure of the stated access
  (the scaled partial permutations and the quarter phase on any configuration) and the datum at the
  angles of `D` under the architecture operations and relabelling; `MixC` is the class at every
  angle, `mixTheory` its generated theory.
* T2, the resource from the datum: at every angle in `(0, π/2)` the image is non-monomial and
  distinct angles give non-proportional images, so the class has uncountably many non-monomial
  rays at level one (`mixC_uncountableNonMonomialRays`), proved from the datum.
* T3, the bridge: the product of the stated phase gates over any set of configurations is in the
  class (`phaseIndicator_mem`); the lifted site exchange's gate flow is a unit scalar times the
  site shear, the datum at `−πt/2` and the adjoint site shear (`gateFlow_eq_shear_mix`); so the
  theory executes the layer flow (`mixTheory_layerFlowExecutable`), satisfies the closure
  (`mixTheory_derivedOI`), and is exact finite operational quantum mechanics (`mixTheory_qm`),
  with the class-level form under the stated-access containment (`qm_of_mixSourced`).
* T4, the countercontrols: with the datum restricted to a countable set of angles the class is
  countable up to scalar (`mixR_countable_upToScalar`), executes no layer flow and is not quantum
  mechanics (`mixTheoryR_not_qm`); with the datum removed, the bijection-valued replacement, the
  same (`mixTheory_empty_not_qm`); the polarization closure is the cited second witness.
-/

namespace OIBridge
namespace StateMixingCoupling

open Complex Matrix CoherentLift SpectatorBridge OperationalAssembly AncillaClosure
open MonoidalCompletion InterventionLocality MicroReversibility PrimitiveSource LieRankSource
open DiagonalTheory SubstratumInterface StructuralClosure MinimalRepertoire LevelOneSeam
open PhysicalCharacterization RouteB ManuscriptAxioms LiftAudit SubstratumInterfaceAudit
open InstrumentRealization SecondOrderCircuit ExecSource FlowEndpoint DerivedQ3 C5Discovery
open PolarizationClosure CoherentContinuumSource Set

/-! ### Section A — T1: the datum, its sourcing map, and the class -/

section Datum

/-- **THE DATUM**: the real rotation of the two values of one site by the mixing angle `θ`. -/
noncomputable def rot (θ : ℝ) : Matrix (Fin 2) (Fin 2) ℂ :=
  !![(Real.cos θ : ℂ), -(Real.sin θ : ℂ); (Real.sin θ : ℂ), (Real.cos θ : ℂ)]

/-- **THE SOURCING MAP AT LEVEL `n`**: the rotation on the site factor, the identity on the
ancilla factor. -/
noncomputable def mixImage (n : ℕ) (θ : ℝ) : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ :=
  Matrix.of fun p q => if p.2 = q.2 then rot θ p.1 q.1 else 0

/-- **THE CLASS**: the stated access, the scaled partial permutations and the quarter phase on
any configuration at any level, together with the datum at the angles of `D`, closed under the
architecture operations and relabelling. -/
inductive MixR (D : Set ℝ) : ∀ (T : Type) [Fintype T] [DecidableEq T], Matrix T T ℂ → Prop
  | perm {T : Type} [Fintype T] [DecidableEq T] (K : Matrix T T ℂ) (h : permClass T K) : MixR D T K
  | phase (n : ℕ) (p : Fin 2 × Fin n) : MixR D (Fin 2 × Fin n) (phaseGate p)
  | mix (n : ℕ) (θ : ℝ) (hθ : θ ∈ D) : MixR D (Fin 2 × Fin n) (mixImage n θ)
  | mul {T : Type} [Fintype T] [DecidableEq T] (K L : Matrix T T ℂ) :
      MixR D T K → MixR D T L → MixR D T (K * L)
  | smul {T : Type} [Fintype T] [DecidableEq T] (a : ℂ) (K : Matrix T T ℂ) (ha : ‖a‖ ≤ 1) :
      MixR D T K → MixR D T (a • K)
  | proj {T : Type} [Fintype T] [DecidableEq T] (m : ℕ) (k : Fin m) :
      MixR D (T × Fin m) (Matrix.diagonal fun r => if r.2 = k then 1 else 0)
  | block {T : Type} [Fintype T] [DecidableEq T] (m : ℕ) (K : Matrix (T × Fin m) (T × Fin m) ℂ)
      (f e : Fin m) : MixR D (T × Fin m) K → MixR D T (ancBlock K f e)
  | relabel {T T' : Type} [Fintype T] [DecidableEq T] [Fintype T'] [DecidableEq T'] (e : T ≃ T')
      (K : Matrix T T ℂ) : MixR D T K → MixR D T' (Matrix.reindex e e K)

/-- **THE CLASS OF THE STATED ACCESS AND THE DATUM AT EVERY ANGLE.** -/
abbrev MixC : ImplementationClass := MixR Set.univ

theorem mixR_arch (D : Set ℝ) : Architecture (MixR D) where
  one := fun T _ _ => MixR.perm 1 (permClass_arch.one T)
  mul := fun _ _ _ K L hK hL => MixR.mul K L hK hL
  smul := fun _ _ _ a K ha hK => MixR.smul a K ha hK
  proj := fun _ _ _ m k => MixR.proj m k
  block := fun _ _ _ m K f e hK => MixR.block m K f e hK

theorem mixR_labelInvariant (D : Set ℝ) : LabelInvariant (MixR D) :=
  fun _ _ _ _ _ _ e K h => MixR.relabel e K h

theorem mixC_arch : Architecture MixC := mixR_arch Set.univ

theorem mixC_mix (n : ℕ) (θ : ℝ) : MixC (Fin 2 × Fin n) (mixImage n θ) :=
  MixR.mix n θ (Set.mem_univ θ)

theorem mixR_le_mixC (D : Set ℝ) : ∀ (T : Type) [Fintype T] [DecidableEq T] (K : Matrix T T ℂ),
    MixR D T K → MixC T K := by
  intro T _ _ K h
  induction h with
  | perm K h => exact MixR.perm K h
  | phase n p => exact MixR.phase n p
  | mix n θ _ => exact mixC_mix n θ
  | mul K L _ _ ihK ihL => exact MixR.mul K L ihK ihL
  | smul a K ha _ ih => exact MixR.smul a K ha ih
  | proj m k => exact MixR.proj m k
  | block m K f e _ ih => exact MixR.block m K f e ih
  | relabel e K _ ih => exact MixR.relabel e K ih

/-- **THE THEORY OF THE STATED ACCESS AND THE DATUM AT THE ANGLES OF `D`.** -/
noncomputable def mixTheoryR (D : Set ℝ) (S : Type) [Fintype S] [DecidableEq S] :
    FiniteOperationalTheory S :=
  genTheory (MixR D) (mixR_arch D) S

/-- **THE THEORY OF THE STATED ACCESS AND THE DATUM**, at every angle. -/
noncomputable def mixTheory (S : Type) [Fintype S] [DecidableEq S] : FiniteOperationalTheory S :=
  genTheory MixC mixC_arch S

theorem mixImage_apply (n : ℕ) (θ : ℝ) (p q : Fin 2 × Fin n) :
    mixImage n θ p q = if p.2 = q.2 then rot θ p.1 q.1 else 0 := rfl

theorem rot_mul (θ θ' : ℝ) : rot θ * rot θ' = rot (θ + θ') := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [rot, Matrix.mul_apply, Fin.sum_univ_two, Real.cos_add, Real.sin_add] <;> ring

theorem rot_zero : rot 0 = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [rot]

theorem rot_conjTranspose (θ : ℝ) : (rot θ)ᴴ = rot (-θ) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [rot, Matrix.conjTranspose_apply, Real.cos_neg, Real.sin_neg, Complex.conj_ofReal,
      -Complex.ofReal_cos, -Complex.ofReal_sin]

theorem mixImage_eq_tensorOf (n : ℕ) (θ : ℝ) :
    mixImage n θ = tensorOf (rot θ) (1 : Matrix (Fin n) (Fin n) ℂ) := by
  ext p q
  simp only [mixImage_apply, tensorOf_apply, Matrix.one_apply]
  split_ifs <;> simp

theorem mixImage_mul (n : ℕ) (θ θ' : ℝ) : mixImage n θ * mixImage n θ' = mixImage n (θ + θ') := by
  rw [mixImage_eq_tensorOf, mixImage_eq_tensorOf, mixImage_eq_tensorOf, ← rot_mul, tensorOf_mul',
    Matrix.one_mul]

theorem mixImage_zero (n : ℕ) : mixImage n 0 = 1 := by
  ext ⟨x, k⟩ ⟨y, l⟩
  simp only [mixImage_apply, rot_zero, Matrix.one_apply, Prod.mk.injEq]
  by_cases hk : k = l <;> by_cases hx : x = y <;> simp [hk, hx]

theorem mixImage_conjTranspose (n : ℕ) (θ : ℝ) : (mixImage n θ)ᴴ = mixImage n (-θ) := by
  ext p q
  simp only [Matrix.conjTranspose_apply, mixImage_apply]
  by_cases h : p.2 = q.2
  · rw [if_pos h.symm, if_pos h, ← Matrix.conjTranspose_apply, rot_conjTranspose]
  · rw [if_neg (Ne.symm h), if_neg h, star_zero]

/-- **THE IMAGE IS UNITARY** at every level and angle. -/
theorem mixImage_unitary (n : ℕ) (θ : ℝ) : (mixImage n θ)ᴴ * mixImage n θ = 1 := by
  rw [mixImage_conjTranspose, mixImage_mul, neg_add_cancel, mixImage_zero]

end Datum

/-! ### Section B — T2: the necessary resource, from the datum -/

section Resource

theorem rot_apply_00 (θ : ℝ) : rot θ 0 0 = (Real.cos θ : ℂ) := rfl
theorem rot_apply_10 (θ : ℝ) : rot θ 1 0 = (Real.sin θ : ℂ) := rfl

/-- **THE IMAGE IS NON-MONOMIAL** at every angle in `(0, π/2)`: one column has two nonzero
entries. -/
theorem mixImage_not_monomial {n : ℕ} (k : Fin n) {θ : ℝ} (hθ : θ ∈ Ioo (0 : ℝ) (Real.pi / 2)) :
    ¬ IsMonomial (mixImage n θ) := by
  rintro ⟨τ, d, hK⟩
  have hc : (Real.cos θ : ℂ) ≠ 0 := by
    exact_mod_cast (Real.cos_pos_of_mem_Ioo ⟨by linarith [hθ.1, Real.pi_pos], hθ.2⟩).ne'
  have hs : (Real.sin θ : ℂ) ≠ 0 := by
    exact_mod_cast (Real.sin_pos_of_pos_of_lt_pi hθ.1 (by linarith [hθ.2, Real.pi_pos])).ne'
  have h1 : mixImage n θ (0, k) (0, k) = (Real.cos θ : ℂ) := by simp [mixImage_apply, rot_apply_00]
  have h2 : mixImage n θ (1, k) (0, k) = (Real.sin θ : ℂ) := by simp [mixImage_apply, rot_apply_10]
  rw [hK, monomial_entry] at h1 h2
  by_cases hτ : τ (0, k) = (0, k)
  · rw [if_neg (by rw [hτ]; simp)] at h2
    exact hs h2.symm
  · rw [if_neg hτ] at h1
    exact hc h1.symm

/-- **DISTINCT ANGLES IN `(0, π/2)` GIVE NON-PROPORTIONAL IMAGES.** -/
theorem mixImage_not_proportional {n : ℕ} (k : Fin n) {θ θ' : ℝ}
    (hθ : θ ∈ Ioo (0 : ℝ) (Real.pi / 2)) (hθ' : θ' ∈ Ioo (0 : ℝ) (Real.pi / 2)) (hne : θ ≠ θ')
    (c : ℂ) : mixImage n θ ≠ c • mixImage n θ' := by
  intro h
  have e1 := congrFun (congrFun h (0, k)) (0, k)
  have e2 := congrFun (congrFun h (1, k)) (0, k)
  simp only [Matrix.smul_apply, mixImage_apply, if_true, rot_apply_00, rot_apply_10, smul_eq_mul] at e1 e2
  have hsq : ((Real.cos θ : ℂ)) ^ 2 + ((Real.sin θ : ℂ)) ^ 2 = 1 := by
    exact_mod_cast Real.cos_sq_add_sin_sq θ
  have hsq' : ((Real.cos θ' : ℂ)) ^ 2 + ((Real.sin θ' : ℂ)) ^ 2 = 1 := by
    exact_mod_cast Real.cos_sq_add_sin_sq θ'
  have hc2 : c ^ 2 = 1 := by
    have : ((Real.cos θ : ℂ)) ^ 2 + ((Real.sin θ : ℂ)) ^ 2
        = c ^ 2 * (((Real.cos θ' : ℂ)) ^ 2 + ((Real.sin θ' : ℂ)) ^ 2) := by
      rw [e1, e2]; ring
    rw [hsq, hsq', mul_one] at this
    exact this.symm
  have hcpos : 0 < Real.cos θ := Real.cos_pos_of_mem_Ioo ⟨by linarith [hθ.1, Real.pi_pos], hθ.2⟩
  have hcpos' : 0 < Real.cos θ' := Real.cos_pos_of_mem_Ioo ⟨by linarith [hθ'.1, Real.pi_pos], hθ'.2⟩
  have hc : c = 1 ∨ c = -1 := by
    have : (c - 1) * (c + 1) = 0 := by linear_combination hc2
    rcases mul_eq_zero.mp this with h | h
    · left; linear_combination h
    · right; linear_combination h
  rcases hc with rfl | rfl
  · rw [one_mul] at e1
    have : Real.cos θ = Real.cos θ' := by exact_mod_cast e1
    exact hne (Real.injOn_cos ⟨hθ.1.le, by linarith [hθ.2, Real.pi_pos]⟩
      ⟨hθ'.1.le, by linarith [hθ'.2, Real.pi_pos]⟩ this)
  · have : Real.cos θ = -Real.cos θ' := by
      have := e1; rw [neg_one_mul] at this; exact_mod_cast this
    linarith

/-- **T2 — THE CLASS HAS UNCOUNTABLY MANY NON-MONOMIAL RAYS AT LEVEL ONE**, from the datum: the
images at the angles of `(0, π/2)` are non-monomial and pairwise non-proportional. -/
theorem mixC_uncountableNonMonomialRays : UncountableNonMonomialRays MixC (Fin 2 × Fin 1) := by
  rintro ⟨D, hD, hmem⟩
  have hray : ∀ θ : ℝ, ∃ M : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ,
      θ ∈ Ioo (0 : ℝ) (Real.pi / 2) → M ∈ D ∧ ∃ d : ℂ, mixImage 1 θ = d • M := by
    intro θ
    by_cases hθ : θ ∈ Ioo (0 : ℝ) (Real.pi / 2)
    · obtain ⟨c, M, hM, hcM⟩ := hmem _ (mixC_mix 1 θ) (mixImage_not_monomial 0 hθ)
      exact ⟨M, fun _ => ⟨hM, c, hcM⟩⟩
    · exact ⟨0, fun h => absurd h hθ⟩
  choose f hf using hray
  have hinj : InjOn f (Ioo (0 : ℝ) (Real.pi / 2)) := by
    intro θ hθ θ' hθ' hfθ
    by_contra hne
    obtain ⟨-, d, hd⟩ := hf θ hθ
    obtain ⟨-, d', hd'⟩ := hf θ' hθ'
    have hd'0 : d' ≠ 0 := by
      rintro rfl
      have := congrFun (congrFun hd' (0, 0)) (0, 0)
      simp only [zero_smul, Matrix.zero_apply, mixImage_apply, if_true, rot_apply_00] at this
      have hc : (Real.cos θ' : ℂ) ≠ 0 := by
        exact_mod_cast (Real.cos_pos_of_mem_Ioo ⟨by linarith [hθ'.1, Real.pi_pos], hθ'.2⟩).ne'
      exact hc this
    apply mixImage_not_proportional (0 : Fin 1) hθ hθ' hne (d * d'⁻¹)
    rw [hd, hfθ, hd', smul_smul, mul_assoc, inv_mul_cancel₀ hd'0, mul_one]
  have hmaps : MapsTo f (Ioo (0 : ℝ) (Real.pi / 2)) D := fun θ hθ => (hf θ hθ).1
  have hcount : (Ioo (0 : ℝ) (Real.pi / 2)).Countable := hmaps.countable_of_injOn hinj hD
  have := Cardinal.le_aleph0_iff_set_countable.mpr hcount
  rw [Cardinal.mk_Ioo_real (by positivity : (0 : ℝ) < Real.pi / 2)] at this
  exact absurd this (not_le.mpr Cardinal.aleph0_lt_continuum)

end Resource

/-! ### Section C — T3: the bridge -/

section Bridge

/-- **THE PRODUCT OF THE STATED PHASE GATES OVER ANY SET OF CONFIGURATIONS IS IN THE CLASS**, for
any architecture containing the stated access and the phase gates. -/
theorem phaseIndicator_mem {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hph : ∀ (n : ℕ) (p : Fin 2 × Fin n), 𝓘 (Fin 2 × Fin n) (phaseGate p)) (n : ℕ)
    (s : Finset (Fin 2 × Fin n)) :
    𝓘 (Fin 2 × Fin n) (Matrix.diagonal fun p => if p ∈ s then Complex.I else 1) := by
  induction s using Finset.induction_on with
  | empty =>
    have : (Matrix.diagonal fun p : Fin 2 × Fin n => if p ∈ (∅ : Finset (Fin 2 × Fin n)) then Complex.I else 1)
        = 1 := by
      ext i j
      by_cases h : i = j
      · subst h; simp
      · simp [Matrix.diagonal_apply_ne _ h, Matrix.one_apply_ne h]
    rw [this]
    exact arch.one _
  | insert a s ha ih =>
    have : (Matrix.diagonal fun p : Fin 2 × Fin n => if p ∈ insert a s then Complex.I else 1)
        = phaseGate a * Matrix.diagonal fun p => if p ∈ s then Complex.I else 1 := by
      rw [phaseGate, Matrix.diagonal_mul_diagonal]
      congr 1
      funext p
      by_cases hp : p = a
      · subst hp; simp [ha]
      · simp [hp, Ne.symm hp]
    rw [this]
    exact arch.mul _ _ _ (hph n a) ih

/-- **THE SITE SHEAR IS IN THE CLASS**: the product of the stated phase gates over the
configurations with value one. -/
theorem siteShear_mem {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hph : ∀ (n : ℕ) (p : Fin 2 × Fin n), 𝓘 (Fin 2 × Fin n) (phaseGate p)) (n : ℕ) :
    𝓘 (Fin 2 × Fin n) (siteShearImage n) := by
  have := phaseIndicator_mem arch hph n (Finset.univ.filter fun p : Fin 2 × Fin n => p.1 = 1)
  have heq : siteShearImage n
      = Matrix.diagonal fun p : Fin 2 × Fin n =>
          if p ∈ (Finset.univ.filter fun p : Fin 2 × Fin n => p.1 = 1) then Complex.I else 1 := by
    rw [siteShearImage]; congr 1; funext p; simp
  rw [heq]
  exact this

theorem siteShearImage_unitary (n : ℕ) : (siteShearImage n)ᴴ * siteShearImage n = 1 := by
  rw [siteShearImage, Matrix.diagonal_conjTranspose, Matrix.diagonal_mul_diagonal, ← Matrix.diagonal_one]
  congr 1
  funext p
  simp only [Pi.star_apply]
  split_ifs <;> simp [Complex.conj_I]

/-- The entries of the gate flow, in closed form. -/
theorem gateFlow_apply' {S : Type} [Fintype S] [DecidableEq S] (σ : Equiv.Perm S) (t : ℝ) (p q : S) :
    gateFlow σ t p q
      = (if p = q then 1 else 0)
        + (Complex.exp (Real.pi * Complex.I * t) - 1)
          * ((2 : ℂ)⁻¹ * ((if p = q then 1 else 0) - (if σ q = p then 1 else 0))) := by
  simp [gateFlow, unit, proj, permMat, Matrix.add_apply, Matrix.smul_apply, Matrix.sub_apply,
    Matrix.one_apply]

/-- **THE IDENTITY**: the lifted site exchange's gate flow is a unit scalar times the site shear,
the datum at `−πt/2`, and the adjoint site shear. -/
theorem gateFlow_eq_shear_mix (n : ℕ) (t : ℝ) :
    gateFlow (levelPerm (Equiv.swap (0 : Fin 2) 1) n) t
      = Complex.exp (((Real.pi * t / 2 : ℝ) : ℂ) * Complex.I)
          • (siteShearImage n * mixImage n (-(Real.pi * t / 2)) * (siteShearImage n)ᴴ) := by
  set u : ℝ := Real.pi * t / 2 with hu
  have hcsR : Real.cos u ^ 2 + Real.sin u ^ 2 = 1 := Real.cos_sq_add_sin_sq _
  have he : Complex.exp ((u : ℂ) * Complex.I) = (Real.cos u : ℂ) + (Real.sin u : ℂ) * Complex.I := by
    rw [Complex.exp_mul_I, ← Complex.ofReal_cos, ← Complex.ofReal_sin]
  have hE : Complex.exp (Real.pi * Complex.I * t)
      = ((Real.cos u : ℂ) + (Real.sin u : ℂ) * Complex.I) ^ 2 := by
    rw [← he, sq, ← Complex.exp_add]
    congr 1
    rw [hu]; push_cast; ring
  ext ⟨x, k⟩ ⟨y, l⟩
  rw [gateFlow_apply', Matrix.smul_apply, he, hE]
  simp only [siteShearImage, Matrix.diagonal_conjTranspose, Matrix.mul_diagonal, Matrix.diagonal_mul,
    Pi.star_apply, levelPerm_apply, mixImage_apply, smul_eq_mul]
  by_cases hk : k = l
  · subst hk
    simp only [if_true]
    fin_cases x <;> fin_cases y <;>
      simp [rot, Real.cos_neg, Real.sin_neg, Complex.conj_I, -Complex.ofReal_cos,
        -Complex.ofReal_sin] <;>
      apply Complex.ext <;>
      simp [sq, Complex.mul_re, Complex.mul_im, Complex.add_re, Complex.add_im, Complex.sub_re,
        Complex.sub_im, -Complex.ofReal_cos, -Complex.ofReal_sin] <;>
      linarith [hcsR]
  · have h1 : ((x, k) : Fin 2 × Fin n) ≠ (y, l) := fun h => hk (Prod.mk.inj h).2
    have h2 : ((Equiv.swap (0 : Fin 2) 1 y, l) : Fin 2 × Fin n) ≠ (x, k) :=
      fun h => hk (Prod.mk.inj h).2.symm
    simp [h1, h2, hk]

variable {S : Type} [Fintype S] [DecidableEq S]

/-- **THE LAYER FLOW IS EXECUTABLE** in any generated theory whose class is an architecture
containing the phase gates and the datum: the identity, membership by `mul` and `smul`, and the
constructor `op`. -/
theorem layerFlowExecutable_of_mixSourced {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hph : ∀ (n : ℕ) (p : Fin 2 × Fin n), 𝓘 (Fin 2 × Fin n) (phaseGate p))
    (hmix : ∀ (n : ℕ) (θ : ℝ), 𝓘 (Fin 2 × Fin n) (mixImage n θ)) :
    LayerFlowExecutable (genTheory 𝓘 arch (Fin 2)) (Equiv.swap 0 1) := by
  intro n t
  have hσ : ∀ x : Fin 2, Equiv.swap (0 : Fin 2) 1 (Equiv.swap 0 1 x) = x :=
    fun x => Equiv.swap_apply_self _ _ _
  refine SubstratumSource.genTheory_avail_conj arch ?_
    (gateFlow_unitary (LiftAudit.levelPerm_involutive hσ n) t)
  rw [gateFlow_eq_shear_mix]
  have hS := siteShear_mem arch hph n
  have hS' : 𝓘 (Fin 2 × Fin n) (siteShearImage n)ᴴ := by
    rw [siteShearImage_conjTranspose]
    exact arch.mul _ _ _ (arch.mul _ _ _ hS hS) hS
  refine arch.smul _ _ _ ?_ (arch.mul _ _ _ (arch.mul _ _ _ hS (hmix n _)) hS')
  rw [Complex.norm_exp_ofReal_mul_I]

/-- **T3 — THE THEORY EXECUTES THE LAYER FLOW OF THE SITE EXCHANGE.** -/
theorem mixTheory_layerFlowExecutable : LayerFlowExecutable (mixTheory (Fin 2)) (Equiv.swap 0 1) :=
  layerFlowExecutable_of_mixSourced mixC_arch (fun n p => MixR.phase n p) mixC_mix

theorem phaseGate_conjTranspose' {T : Type} [Fintype T] [DecidableEq T] (a : T) :
    (phaseGate a)ᴴ = phaseGate a * phaseGate a * phaseGate a := by
  rw [phaseGate, Matrix.diagonal_conjTranspose, Matrix.diagonal_mul_diagonal, Matrix.diagonal_mul_diagonal]
  congr 1
  funext p
  simp only [Pi.star_apply]
  split_ifs <;> simp [Complex.conj_I, Complex.I_mul_I]

/-- **`MixC` IS DAGGER-STABLE.** -/
theorem mixC_daggerStable : DaggerStable MixC := by
  intro T _ _ K h
  induction h with
  | perm K h => exact MixR.perm _ (scaled_conjTranspose h)
  | phase n p =>
    rw [phaseGate_conjTranspose']
    exact MixR.mul _ _ (MixR.mul _ _ (MixR.phase n p) (MixR.phase n p)) (MixR.phase n p)
  | mix n θ _ => rw [mixImage_conjTranspose]; exact mixC_mix n (-θ)
  | mul K L _ _ ihK ihL => rw [Matrix.conjTranspose_mul]; exact MixR.mul _ _ ihL ihK
  | smul a K ha _ ih =>
    rw [Matrix.conjTranspose_smul]
    exact MixR.smul _ _ (by simpa using ha) ih
  | proj m k =>
    rw [Matrix.diagonal_conjTranspose]
    have key : ∀ (U : Type) [Fintype U] [DecidableEq U],
        (star fun r : U × Fin m => if r.2 = k then (1 : ℂ) else 0)
          = fun r => if r.2 = k then (1 : ℂ) else 0 := by
      intro U _ _
      funext r; simp only [Pi.star_apply]; split_ifs <;> simp
    rw [key]
    exact MixR.proj m k
  | block m K f e _ ih => rw [ancBlock_conjTranspose']; exact MixR.block m _ e f ih
  | relabel e K _ ih => rw [Matrix.conjTranspose_reindex]; exact MixR.relabel e _ ih

theorem tensorOf_one_mixImage (R : Type) [Fintype R] [DecidableEq R] (n : ℕ) (θ : ℝ) :
    tensorOf (1 : Matrix R R ℂ) (mixImage n θ)
      = Matrix.reindex (ctxRelabel R n) (ctxRelabel R n) (mixImage (Fintype.card R * n) θ) := by
  ext ⟨r, s, k⟩ ⟨r', s', k'⟩
  simp only [tensorOf_apply, mixImage_apply, Matrix.reindex_apply, Matrix.submatrix_apply,
    ctxRelabel_symm_apply, Matrix.one_apply]
  by_cases hr : r = r'
  · subst hr
    by_cases hk : k = k'
    · subst hk; simp
    · have : finProdFinEquiv (Fintype.equivFin R r, k) ≠ finProdFinEquiv (Fintype.equivFin R r, k') := by
        intro h; apply hk; exact (Prod.mk.inj (finProdFinEquiv.injective h)).2
      simp [hk, this]
  · have : finProdFinEquiv (Fintype.equivFin R r, k) ≠ finProdFinEquiv (Fintype.equivFin R r', k') := by
      intro h; apply hr
      exact (Fintype.equivFin R).injective (Prod.mk.inj (finProdFinEquiv.injective h)).1
    simp [hr, this]

/-- The identity tensored with a phase gate is a relabelled product of phase gates at a higher
level. -/
theorem tensorOf_one_phaseGate_mem (R : Type) [Fintype R] [DecidableEq R] (n : ℕ)
    (p : Fin 2 × Fin n) : MixC (R × (Fin 2 × Fin n)) (tensorOf (1 : Matrix R R ℂ) (phaseGate p)) := by
  rw [phaseGate, tensorOf_one_diagonal]
  set e := ctxRelabel R n
  have hmem := phaseIndicator_mem mixC_arch (fun n p => MixR.phase n p) (Fintype.card R * n)
    (Finset.univ.filter fun x : Fin 2 × Fin (Fintype.card R * n) => p = (e x).2)
  have heq : (Matrix.diagonal fun q : R × (Fin 2 × Fin n) => if p = q.2 then Complex.I else 1)
      = Matrix.reindex e e (Matrix.diagonal fun x : Fin 2 × Fin (Fintype.card R * n) =>
          if x ∈ (Finset.univ.filter fun x : Fin 2 × Fin (Fintype.card R * n) => p = (e x).2)
          then Complex.I else 1) := by
    rw [Matrix.reindex_apply, Matrix.submatrix_diagonal_equiv]
    congr 1
    funext q
    simp
  rw [heq]
  exact MixR.relabel e _ hmem

/-- **`MixC` IS CONTEXT-STABLE.** -/
theorem mixC_contextStable : ContextStable MixC := by
  intro R T _ _ _ _ K h
  induction h with
  | perm K h => exact MixR.perm _ (scaled_tensor_one h)
  | phase n p => exact tensorOf_one_phaseGate_mem R n p
  | mix n θ _ => rw [tensorOf_one_mixImage]; exact MixR.relabel _ _ (mixC_mix _ _)
  | mul K L _ _ ihK ihL =>
    have key := tensorOf_mul' (1 : Matrix R R ℂ) (1 : Matrix R R ℂ) K L
    rw [Matrix.one_mul] at key
    rw [← key]
    exact MixR.mul _ _ ihK ihL
  | smul a K ha _ ih => rw [tensorOf_smul_right]; exact MixR.smul _ _ ha ih
  | proj m k =>
    rw [tensorOf_one_diagonal]
    exact MixR.perm _ (scaled_diagonal_indicator _)
  | block m K f e _ ih =>
    rw [tensorOf_one_ancBlock]
    exact MixR.block m _ f e (MixR.relabel _ _ ih)
  | relabel e K _ ih => rw [tensorOf_one_reindex]; exact MixR.relabel _ _ ih

/-- **THE CLOSURE** for any class with the stabilities, the stated access and the phase gates. -/
theorem derivedOI_of_stated {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hl : LabelInvariant 𝓘) (hd : DaggerStable 𝓘) (hc : ContextStable 𝓘)
    (hperm : ∀ (T : Type) [Fintype T] [DecidableEq T] (K : Matrix T T ℂ), permClass T K → 𝓘 T K)
    (hph : ∀ (n : ℕ) (p : Fin 2 × Fin n), 𝓘 (Fin 2 × Fin n) (phaseGate p)) :
    DerivedOI (genTheory 𝓘 arch (Fin 2)) :=
  ⟨genTheory_reversibleImplementationLocality 𝓘 arch hc hl hd,
    genTheory_embeddedObservation 𝓘 arch hl,
    fun _ a b => SubstratumSource.genTheory_avail_conj arch
      (hperm _ _ (permClass_permMatrix (Equiv.swap a b))) (permMatrix_isometry _),
    fun n a => SubstratumSource.genTheory_avail_conj arch (hph n a) (phaseGate_unitary a),
    fun _ _ _ F l => by
      rw [ReadWriteControl.readWriteOperator_eq_perm]
      exact SubstratumSource.genTheory_avail_conj arch
        (hperm _ _ (permClass_permMatrix (F.couple l))) (permMatrix_isometry _)⟩

/-- **T3 — THE THEORY SATISFIES THE CLOSURE `DerivedOI`.** -/
theorem mixTheory_derivedOI : DerivedOI (mixTheory (Fin 2)) :=
  derivedOI_of_stated mixC_arch (mixR_labelInvariant _) mixC_daggerStable mixC_contextStable
    (fun _ _ _ K h => MixR.perm K h) (fun n p => MixR.phase n p)

/-- **THE CLASS-LEVEL ENDPOINT**, under the scope amendment: architecture, the three stabilities,
the stated access, the phase gates and the datum at every level give the closure and exact finite
operational quantum mechanics on the two-valued alphabet. -/
theorem qm_of_mixSourced {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hl : LabelInvariant 𝓘) (hd : DaggerStable 𝓘) (hc : ContextStable 𝓘)
    (hperm : ∀ (T : Type) [Fintype T] [DecidableEq T] (K : Matrix T T ℂ), permClass T K → 𝓘 T K)
    (hph : ∀ (n : ℕ) (p : Fin 2 × Fin n), 𝓘 (Fin 2 × Fin n) (phaseGate p))
    (hmix : ∀ (n : ℕ) (θ : ℝ), 𝓘 (Fin 2 × Fin n) (mixImage n θ)) :
    DerivedOI (genTheory 𝓘 arch (Fin 2))
      ∧ ExactAllFiniteEndomorphicQuantumOps (genTheory 𝓘 arch (Fin 2)) := by
  have hderived := derivedOI_of_stated arch hl hd hc hperm hph
  have hσ : ∀ x : Fin 2, Equiv.swap (0 : Fin 2) 1 (Equiv.swap 0 1 x) = x :=
    fun x => Equiv.swap_apply_self _ _ _
  exact ⟨hderived, qm_of_derivedOI_layerFlowExecutable _ hderived hσ (x := (0 : Fin 2)) (by simp)
    (layerFlowExecutable_of_mixSourced arch hph hmix)⟩

/-- **T3 — PHASE-FREE RICHNESS**, through the cited reduction to a single pair. -/
theorem mixTheory_phaseFree : PhaseFreeRichness (mixTheory (Fin 2)) :=
  phaseFree_of_derivedOI_layerFlowExecutable _ mixTheory_derivedOI
    (fun x => Equiv.swap_apply_self _ _ x) (x := (0 : Fin 2)) (by simp) mixTheory_layerFlowExecutable

/-- **T3, T5 — THE ENDPOINT**: the theory of the stated access and one sourced pair coupling
satisfies the closure and is exact finite operational quantum mechanics. -/
theorem mixTheory_endpoint :
    DerivedOI (mixTheory (Fin 2)) ∧ ExactAllFiniteEndomorphicQuantumOps (mixTheory (Fin 2)) :=
  qm_of_mixSourced mixC_arch (mixR_labelInvariant _) mixC_daggerStable mixC_contextStable
    (fun _ _ _ K h => MixR.perm K h) (fun n p => MixR.phase n p) mixC_mix

theorem mixTheory_qm : ExactAllFiniteEndomorphicQuantumOps (mixTheory (Fin 2)) :=
  mixTheory_endpoint.2

end Bridge

/-! ### Section D — T4: the countercontrols -/

section Countercontrols

/-- The stated phase gates and the images at the angles of `D`, relabelled onto a carrier along
every bijection from every level. -/
def MixImagesAt (D : Set ℝ) (T : Type) [Fintype T] [DecidableEq T] : Set (Matrix T T ℂ) :=
  ⋃ (n : ℕ) (e : Fin 2 × Fin n ≃ T),
    (Set.range fun p : Fin 2 × Fin n => Matrix.reindex e e (phaseGate p))
      ∪ ((fun θ : ℝ => Matrix.reindex e e (mixImage n θ)) '' D)

/-- The depth-indexed generating sets, as in the polarization closure audit, with the stated
phase gates and the images at the angles of `D` at depth zero. -/
def GenM (D : Set ℝ) : ℕ → (T : Type) → [Fintype T] → [DecidableEq T] → Set (Matrix T T ℂ)
  | 0, T, _, _ => ZeroOne T ∪ MixImagesAt D T
  | k + 1, T, _, _ =>
      GenM D k T ∪ Set.image2 (fun (M N : Matrix T T ℂ) => M * N) (GenM D k T) (GenM D k T)
        ∪ ⋃ (m : ℕ) (f : Fin m) (e : Fin m),
            (fun K : Matrix (T × Fin m) (T × Fin m) ℂ => ancBlock K f e) '' GenM D k (T × Fin m)

theorem genM_succ (D : Set ℝ) (k : ℕ) (T : Type) [Fintype T] [DecidableEq T] :
    GenM D (k + 1) T = GenM D k T ∪ Set.image2 (fun (M N : Matrix T T ℂ) => M * N) (GenM D k T) (GenM D k T)
        ∪ ⋃ (m : ℕ) (f : Fin m) (e : Fin m),
            (fun K : Matrix (T × Fin m) (T × Fin m) ℂ => ancBlock K f e) '' GenM D k (T × Fin m) := rfl

theorem genM_zero (D : Set ℝ) (T : Type) [Fintype T] [DecidableEq T] :
    GenM D 0 T = ZeroOne T ∪ MixImagesAt D T := rfl

theorem genM_mono_succ (D : Set ℝ) (k : ℕ) (T : Type) [Fintype T] [DecidableEq T] :
    GenM D k T ⊆ GenM D (k + 1) T :=
  fun _ h => Or.inl (Or.inl h)

theorem genM_mono (D : Set ℝ) {k k' : ℕ} (h : k ≤ k') (T : Type) [Fintype T] [DecidableEq T] :
    GenM D k T ⊆ GenM D k' T := by
  induction h with
  | refl => exact fun _ h => h
  | step _ ih => exact fun M hM => genM_mono_succ D _ T (ih hM)

theorem mixImagesAt_countable {D : Set ℝ} (hD : D.Countable) (T : Type) [Fintype T] [DecidableEq T] :
    (MixImagesAt D T).Countable := by
  unfold MixImagesAt
  refine Set.countable_iUnion fun n => Set.countable_iUnion fun e => ?_
  exact (Set.finite_range _).countable.union (hD.image _)

theorem genM_countable {D : Set ℝ} (hD : D.Countable) :
    ∀ (k : ℕ) (T : Type) [Fintype T] [DecidableEq T], (GenM D k T).Countable := by
  intro k
  induction k with
  | zero =>
    intro T _ _
    exact (zeroOne_finite T).countable.union (mixImagesAt_countable hD T)
  | succ k ih =>
    intro T _ _
    rw [genM_succ]
    refine ((ih T).union ((ih T).image2 (ih T) _)).union ?_
    refine Set.countable_iUnion fun m => Set.countable_iUnion fun f => Set.countable_iUnion fun e => ?_
    exact (ih (T × Fin m)).image _

theorem genM_reindex (D : Set ℝ) :
    ∀ (k : ℕ) (T T' : Type) [Fintype T] [DecidableEq T] [Fintype T'] [DecidableEq T']
      (e : T ≃ T') (M : Matrix T T ℂ), M ∈ GenM D k T → Matrix.reindex e e M ∈ GenM D k T' := by
  intro k
  induction k with
  | zero =>
    intro T T' _ _ _ _ e M hM
    rw [genM_zero] at hM ⊢
    rcases hM with h | h
    · left
      intro i j
      simpa [Matrix.reindex_apply, Matrix.submatrix_apply] using h (e.symm i) (e.symm j)
    · right
      unfold MixImagesAt at h ⊢
      simp only [Set.mem_iUnion, Set.mem_union, Set.mem_range, Set.mem_image] at h ⊢
      obtain ⟨n, e₀, h⟩ := h
      refine ⟨n, e₀.trans e, ?_⟩
      rcases h with ⟨p, rfl⟩ | ⟨θ, hθ, rfl⟩
      · left; exact ⟨p, (reindex_reindex' e₀ e _).symm⟩
      · right; exact ⟨θ, hθ, (reindex_reindex' e₀ e _).symm⟩
  | succ k ih =>
    intro T T' _ _ _ _ e M hM
    rw [genM_succ] at hM ⊢
    rcases hM with (h | h) | h
    · exact Or.inl (Or.inl (ih T T' e M h))
    · obtain ⟨M₁, hM₁, M₂, hM₂, rfl⟩ := h
      refine Or.inl (Or.inr ⟨_, ih T T' e M₁ hM₁, _, ih T T' e M₂ hM₂, ?_⟩)
      exact (reindex_mul' e M₁ M₂).symm
    · right
      simp only [Set.mem_iUnion, Set.mem_image] at h ⊢
      obtain ⟨m, f, e', K, hK, rfl⟩ := h
      refine ⟨m, f, e', _, ih (T × Fin m) (T' × Fin m) (e.prodCongr (Equiv.refl (Fin m))) K hK, ?_⟩
      exact (reindex_ancBlock e K f e').symm

/-- **EVERY MEMBER OF `MixR D` IS A SCALAR MULTIPLE OF A MEMBER OF SOME DEPTH.** -/
theorem mixR_mem_genM (D : Set ℝ) :
    ∀ (T : Type) [Fintype T] [DecidableEq T] (K : Matrix T T ℂ), MixR D T K →
      ∃ (k : ℕ) (c : ℂ) (M : Matrix T T ℂ), M ∈ GenM D k T ∧ K = c • M := by
  intro T _ _ K h
  induction h with
  | perm K h =>
    obtain ⟨_, c, _, hall⟩ := h
    refine ⟨0, c, Matrix.of fun i j => if K i j = 0 then 0 else 1, Or.inl ?_, ?_⟩
    · intro i j
      by_cases hij : K i j = 0 <;> simp [hij]
    · ext i j
      by_cases hij : K i j = 0
      · simp [hij]
      · simp [hall i j hij]
  | phase n p =>
    refine ⟨0, 1, phaseGate p, Or.inr ?_, (one_smul _ _).symm⟩
    unfold MixImagesAt
    simp only [Set.mem_iUnion, Set.mem_union, Set.mem_range, Set.mem_image]
    exact ⟨n, Equiv.refl _, Or.inl ⟨p, by simp⟩⟩
  | mix n θ hθ =>
    refine ⟨0, 1, mixImage n θ, Or.inr ?_, (one_smul _ _).symm⟩
    unfold MixImagesAt
    simp only [Set.mem_iUnion, Set.mem_union, Set.mem_range, Set.mem_image]
    exact ⟨n, Equiv.refl _, Or.inr ⟨θ, hθ, by simp⟩⟩
  | mul K L _ _ ihK ihL =>
    obtain ⟨k₁, c₁, M₁, hM₁, rfl⟩ := ihK
    obtain ⟨k₂, c₂, M₂, hM₂, rfl⟩ := ihL
    refine ⟨max k₁ k₂ + 1, c₁ * c₂, M₁ * M₂, ?_, ?_⟩
    · rw [genM_succ]
      exact Or.inl (Or.inr ⟨M₁, genM_mono D (le_max_left _ _) _ hM₁, M₂,
        genM_mono D (le_max_right _ _) _ hM₂, rfl⟩)
    · rw [Matrix.smul_mul, Matrix.mul_smul, smul_smul]
  | smul a K _ _ ih =>
    obtain ⟨k, c, M, hM, rfl⟩ := ih
    exact ⟨k, a * c, M, hM, by rw [smul_smul]⟩
  | proj m k =>
    refine ⟨0, 1, _, Or.inl ?_, (one_smul _ _).symm⟩
    intro i j
    by_cases hij : i = j
    · subst hij; simp only [Matrix.diagonal_apply_eq]; split_ifs <;> simp
    · simp [Matrix.diagonal_apply_ne _ hij]
  | block m K f e _ ih =>
    obtain ⟨k, c, M, hM, rfl⟩ := ih
    refine ⟨k + 1, c, ancBlock M f e, ?_, ancBlock_smul c M f e⟩
    rw [genM_succ]
    right
    simp only [Set.mem_iUnion, Set.mem_image]
    exact ⟨m, f, e, M, hM, rfl⟩
  | relabel e K _ ih =>
    obtain ⟨k, c, M, hM, rfl⟩ := ih
    exact ⟨k, c, Matrix.reindex e e M, genM_reindex D k _ _ e M hM, reindex_smul' e c M⟩

/-- **T4 — WITH THE DATUM AT COUNTABLY MANY ANGLES THE CLASS IS COUNTABLE UP TO SCALAR.** -/
theorem mixR_countable_upToScalar {D : Set ℝ} (hD : D.Countable) (T : Type) [Fintype T]
    [DecidableEq T] :
    ∃ D' : Set (Matrix T T ℂ), D'.Countable ∧
      ∀ K : Matrix T T ℂ, MixR D T K → ∃ (c : ℂ) (M : Matrix T T ℂ), M ∈ D' ∧ K = c • M := by
  refine ⟨⋃ k, GenM D k T, Set.countable_iUnion fun k => genM_countable hD k T, fun K hK => ?_⟩
  obtain ⟨k, c, M, hM, rfl⟩ := mixR_mem_genM D T K hK
  exact ⟨c, M, Set.mem_iUnion.mpr ⟨k, hM⟩, rfl⟩

variable {S : Type} [Fintype S] [DecidableEq S]

/-- **T4 — THE COUNTABLE-ANGLE REPLACEMENT EXECUTES NO LAYER FLOW.** -/
theorem mixTheoryR_not_layerFlowExecutable {D : Set ℝ} (hD : D.Countable) {σ : Equiv.Perm S} {x : S}
    (hx : σ x ≠ x) : ¬ LayerFlowExecutable (mixTheoryR D S) σ := by
  obtain ⟨D', hD', hmem⟩ := mixR_countable_upToScalar hD (S × Fin 1)
  exact countable_not_layerFlowExecutable (mixR_arch D) hx D' hD' hmem

/-- **T4 — THE COUNTABLE-ANGLE REPLACEMENT IS NOT QUANTUM MECHANICS.** -/
theorem mixTheoryR_not_qm {D : Set ℝ} (hD : D.Countable) :
    ¬ ExactAllFiniteEndomorphicQuantumOps (mixTheoryR D (Fin 2)) := by
  intro h
  have hσ : ∀ x : Fin 2, Equiv.swap (0 : Fin 2) 1 (Equiv.swap 0 1 x) = x :=
    fun x => Equiv.swap_apply_self _ _ _
  exact mixTheoryR_not_layerFlowExecutable hD (x := (0 : Fin 2)) (by simp)
    (derivedOI_layerFlowExecutable_of_qm _ h hσ).2

/-- **T4 — THE BIJECTION-VALUED REPLACEMENT**: with the datum removed, every permutation-valued
family lying in the stated access already, the theory is not quantum mechanics. -/
theorem mixTheory_empty_not_qm : ¬ ExactAllFiniteEndomorphicQuantumOps (mixTheoryR ∅ (Fin 2)) :=
  mixTheoryR_not_qm Set.countable_empty

/-- **THE COMPARISON, RECORDED**: one pair coupling with a continuum of angles gives the
completion; the same closure with countably many angles, with no datum, and the polarization
closure do not. Comparisons, not a minimality theorem. -/
theorem comparison :
    ExactAllFiniteEndomorphicQuantumOps (mixTheory (Fin 2))
    ∧ (∀ D : Set ℝ, D.Countable → ¬ ExactAllFiniteEndomorphicQuantumOps (mixTheoryR D (Fin 2)))
    ∧ ¬ ExactAllFiniteEndomorphicQuantumOps (mixTheoryR ∅ (Fin 2))
    ∧ ¬ ExactAllFiniteEndomorphicQuantumOps (polarizedTheoryC (Fin 2)) :=
  ⟨mixTheory_qm, fun _ hD => mixTheoryR_not_qm hD, mixTheory_empty_not_qm, polarizedTheoryC_not_qm⟩

end Countercontrols

end StateMixingCoupling
end OIBridge

#print axioms OIBridge.StateMixingCoupling.mixR_arch
#print axioms OIBridge.StateMixingCoupling.mixR_le_mixC
#print axioms OIBridge.StateMixingCoupling.mixImage_mul
#print axioms OIBridge.StateMixingCoupling.mixImage_unitary
#print axioms OIBridge.StateMixingCoupling.mixImage_not_monomial
#print axioms OIBridge.StateMixingCoupling.mixImage_not_proportional
#print axioms OIBridge.StateMixingCoupling.mixC_uncountableNonMonomialRays
#print axioms OIBridge.StateMixingCoupling.phaseIndicator_mem
#print axioms OIBridge.StateMixingCoupling.siteShear_mem
#print axioms OIBridge.StateMixingCoupling.gateFlow_eq_shear_mix
#print axioms OIBridge.StateMixingCoupling.layerFlowExecutable_of_mixSourced
#print axioms OIBridge.StateMixingCoupling.mixTheory_layerFlowExecutable
#print axioms OIBridge.StateMixingCoupling.mixC_daggerStable
#print axioms OIBridge.StateMixingCoupling.mixC_contextStable
#print axioms OIBridge.StateMixingCoupling.derivedOI_of_stated
#print axioms OIBridge.StateMixingCoupling.mixTheory_derivedOI
#print axioms OIBridge.StateMixingCoupling.qm_of_mixSourced
#print axioms OIBridge.StateMixingCoupling.mixTheory_phaseFree
#print axioms OIBridge.StateMixingCoupling.mixTheory_endpoint
#print axioms OIBridge.StateMixingCoupling.mixTheory_qm
#print axioms OIBridge.StateMixingCoupling.mixR_countable_upToScalar
#print axioms OIBridge.StateMixingCoupling.mixTheoryR_not_layerFlowExecutable
#print axioms OIBridge.StateMixingCoupling.mixTheoryR_not_qm
#print axioms OIBridge.StateMixingCoupling.mixTheory_empty_not_qm
#print axioms OIBridge.StateMixingCoupling.comparison
