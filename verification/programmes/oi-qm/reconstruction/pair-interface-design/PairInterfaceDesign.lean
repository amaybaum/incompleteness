/-
  PairInterfaceDesign.lean — research-only design: the pair instance of the combined interface
  between the adopted pair cone theorem (`EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone`) and the
  carrier-general implementation framework of `SubstratumSource` and KN-DESC-1. Not adopted, not a
  round, compiled on a disposable branch.

  (A) Admission of the cone gates. On one token the phase `phaseMat (cos t) (sin t)` is one diagonal
  transition flow (`phaseMat_eq_flow`) and the cyclic gate is a product of three transition flows
  (`cycMat_eq_flows`); on the pair the controlled NOT is the exchange of `(1, 0)` and `(1, 1)`
  (`cnotMat_eq_swap`). So an architecture admitting the one-token transition flows and that one
  exchange admits every gate of the pair theorem, the one-token gates on the target through
  `ContextStable`.

  (B) The combined pair theorem. With `PairCompat` — every admitted unitary on the pair carrier maps
  the cone into itself through the dictionary — the gate clauses of the pair theorem follow, and with
  its cone clauses the cone is `Q3` (`pairCone_eq_Q3_of_admitted`, `pairCone_eq_Q3_of_drives`,
  `pairCone_eq_Q3_of_quantumArchitecture`).

  (C) Controls. Positive: the full class with `Q3` satisfies every class-side premise
  (`fullClass_pairControl`). Converse: the diagonal class with `Q3` satisfies the four closure
  clauses and compatibility and does not drive the elementary transitions (`diagClass_pairControl`,
  `not_drives_of_pairCompat`), so the theorem has no converse.

  (D) Correlations at the pair with availability explicit. `prep` and `avail` are the available
  joint preparations and the available one-token tests. If the products are available
  preparations, mixing is available, the admitted unitaries carry available preparations to
  available preparations, the sharp tests are available and valid on every available preparation,
  then the available preparations are exactly `Q3` and an available preparation with four
  available two-outcome sharp measurements gives the CHSH value `2√2`
  (`pair_available_eq_Q3_and_chsh`). The marginal of one party does not depend on the other
  party's setting, for every joint vector (`marginal_independent`).

  Every clause is a premise. Nothing here sources drivability, compatibility, the availability of
  preparations, operations or tests, or the validity of product tests on joint preparations. No
  upper bound on CHSH is proved here.
-/
import OIBridge.EqvK2MaxCone
import OIBridge.SubstratumSource
import OIBridge.LiftAudit

namespace OIBridge
namespace PairInterfaceDesign

open InterventionLocality MonoidalCompletion CoherentLift LieRankSource MicroReversibility
open SubstratumSource

open scoped ComplexOrder Matrix

noncomputable section

/-! ### §A — the one-token gates as transition flows -/

/-- The flow of the diagonal generator `transition a a = 2 E_aa`
(the carrier-descent design's `flow_transition_self`, verbatim). -/
theorem flow_transition_self {S : Type} [Fintype S] [DecidableEq S] (a : S) (t : ℝ) :
    ReachabilitySeam.flow (transition a a) t
      = 1 + (Complex.exp ((-(t : ℂ) * Complex.I) * 2) - 1) • Matrix.single a a (1 : ℂ) := by
  have hE : Matrix.single a a (1 : ℂ) * Matrix.single a a (1 : ℂ) = Matrix.single a a (1 : ℂ) := by
    rw [Matrix.single_mul_single_same, mul_one]
  have hT : transition a a = (2 : ℂ) • Matrix.single a a (1 : ℂ) := by
    rw [transition, two_smul]
  rw [ReachabilitySeam.flow, hT, smul_smul, LiftAudit.exp_smul_idempotent hE]

theorem flow_self_zero (t : ℝ) :
    ReachabilitySeam.flow (transition (0 : Fin 2) 0) t
      = !![Complex.exp ((-(t : ℂ) * Complex.I) * 2), 0; 0, 1] := by
  rw [flow_transition_self]
  ext i j
  fin_cases i <;> fin_cases j <;> simp

theorem flow_self_one (t : ℝ) :
    ReachabilitySeam.flow (transition (1 : Fin 2) 1) t
      = !![1, 0; 0, Complex.exp ((-(t : ℂ) * Complex.I) * 2)] := by
  rw [flow_transition_self]
  ext i j
  fin_cases i <;> fin_cases j <;> simp

theorem flow_transition_zero_one (t : ℝ) :
    ReachabilitySeam.flow (transition (0 : Fin 2) 1) t
      = !![(Real.cos t : ℂ), -((Real.sin t : ℂ) * Complex.I);
          -((Real.sin t : ℂ) * Complex.I), (Real.cos t : ℂ)] := by
  rw [LiftAudit.flow_transition_closedForm (by decide : (0 : Fin 2) ≠ 1)]
  ext i j
  fin_cases i <;> fin_cases j <;> simp [LiftAudit.pairProj, transition]

/-- **The phase is one diagonal flow**: `diag(1, cos s + i sin s) = e^{i(s/2)·2E₁₁}`. -/
theorem phaseMat_eq_flow (s : ℝ) :
    EqvK2Converse.phaseMat (Real.cos s) (Real.sin s)
      = ReachabilitySeam.flow (transition (1 : Fin 2) 1) (-(s / 2)) := by
  rw [flow_self_one]
  have he : (-((-(s / 2) : ℝ) : ℂ) * Complex.I) * 2 = (s : ℂ) * Complex.I := by
    push_cast
    ring
  rw [he, Complex.exp_mul_I, ← Complex.ofReal_cos, ← Complex.ofReal_sin, EqvK2Converse.phaseMat]

theorem sqrt_two_half_mul_self : (Real.sqrt 2 / 2) * (Real.sqrt 2 / 2) = (1 / 2 : ℝ) := by
  have h := Real.mul_self_sqrt (show (0 : ℝ) ≤ 2 by norm_num)
  linear_combination h / 4

/-- **The cyclic gate is three flows**: `(I − i(X + Y + Z))/2 = R_z(π/2) R_x(π/2)`, with
`R_z(π/2)` the product of the two diagonal flows at `±π/8` and `R_x(π/2)` the transition flow at
`π/4`. -/
theorem cycMat_eq_flows :
    EqvK2Converse.cycMat
      = ReachabilitySeam.flow (transition (0 : Fin 2) 0) (Real.pi / 8)
        * ReachabilitySeam.flow (transition (1 : Fin 2) 1) (-(Real.pi / 8))
        * ReachabilitySeam.flow (transition (0 : Fin 2) 1) (Real.pi / 4) := by
  have h0 : Complex.exp ((-((Real.pi / 8 : ℝ) : ℂ) * Complex.I) * 2)
      = ((Real.sqrt 2 / 2 : ℝ) : ℂ) - ((Real.sqrt 2 / 2 : ℝ) : ℂ) * Complex.I := by
    have he : (-((Real.pi / 8 : ℝ) : ℂ) * Complex.I) * 2
        = ((-(Real.pi / 4) : ℝ) : ℂ) * Complex.I := by
      push_cast
      ring
    rw [he, Complex.exp_mul_I, ← Complex.ofReal_cos, ← Complex.ofReal_sin, Real.cos_neg,
      Real.sin_neg, Real.cos_pi_div_four, Real.sin_pi_div_four]
    push_cast
    ring
  have h1 : Complex.exp ((-((-(Real.pi / 8) : ℝ) : ℂ) * Complex.I) * 2)
      = ((Real.sqrt 2 / 2 : ℝ) : ℂ) + ((Real.sqrt 2 / 2 : ℝ) : ℂ) * Complex.I := by
    have he : (-((-(Real.pi / 8) : ℝ) : ℂ) * Complex.I) * 2
        = ((Real.pi / 4 : ℝ) : ℂ) * Complex.I := by
      push_cast
      ring
    rw [he, Complex.exp_mul_I, ← Complex.ofReal_cos, ← Complex.ofReal_sin, Real.cos_pi_div_four,
      Real.sin_pi_div_four]
  have hc := sqrt_two_half_mul_self
  rw [flow_self_zero, flow_self_one, flow_transition_zero_one, h0, h1, Real.cos_pi_div_four,
    Real.sin_pi_div_four, Matrix.mul_fin_two, Matrix.mul_fin_two]
  simp only [EqvK2Converse.cycMat]
  refine EqvK2Converse.mat2_ext ?_ ?_ ?_ ?_ <;> apply Complex.ext <;>
    simp only [Complex.add_re, Complex.add_im, Complex.sub_re, Complex.sub_im, Complex.mul_re,
      Complex.mul_im, Complex.neg_re, Complex.neg_im, Complex.ofReal_re, Complex.ofReal_im,
      Complex.I_re, Complex.I_im, Complex.one_re, Complex.one_im, Complex.zero_re, Complex.zero_im,
      Complex.div_ofNat_re, Complex.div_ofNat_im] <;>
    linarith

/-! ### §A — the pair gate, unitarity, and admission -/

/-- **The controlled NOT is one exchange**: of `(1, 0)` and `(1, 1)`. -/
theorem cnotMat_eq_swap :
    BridgeDictionary.cnotMat
      = CoherentLift.permMatrix (Equiv.swap ((1 : Fin 2), (0 : Fin 2)) (1, 1)) := by
  ext ⟨i, j⟩ ⟨k, l⟩
  fin_cases i <;> fin_cases j <;> fin_cases k <;> fin_cases l <;>
    simp +decide [BridgeDictionary.cnotMat, CoherentLift.permMatrix, BridgeDictionary.projZero,
      BridgeDictionary.projOne, BridgeDictionary.pauli, Matrix.one_apply, Matrix.diagonal_apply,
      Equiv.swap_apply_def]

theorem cnotMat_conjTranspose : BridgeDictionary.cnotMatᴴ = BridgeDictionary.cnotMat := by
  rw [cnotMat_eq_swap, CoherentLift.permMatrix_conjTranspose, Equiv.symm_swap]

theorem cnotMat_unitary : BridgeDictionary.cnotMatᴴ * BridgeDictionary.cnotMat = 1 := by
  rw [cnotMat_conjTranspose, cnotMat_eq_swap, ← LieRankSource.permMatrix_mul',
    Equiv.swap_mul_self, LieRankSource.permMatrix_one']

theorem conjTranspose_mul_self_of_mem {S : Type} [Fintype S] [DecidableEq S]
    {U : Matrix S S ℂ} (h : U ∈ unitary (Matrix S S ℂ)) : Uᴴ * U = 1 := by
  have h1 := (Unitary.mem_iff.mp h).1
  rwa [Matrix.star_eq_conjTranspose] at h1

theorem flow_transition_mem_unitary {S : Type} [Fintype S] [DecidableEq S] (a b : S) (t : ℝ) :
    ReachabilitySeam.flow (transition a b) t ∈ unitary (Matrix S S ℂ) :=
  ReachabilitySeam.flow_mem_unitary _ (transition_hermitian a b) t

theorem phaseMat_unitary (t : ℝ) :
    (EqvK2Converse.phaseMat (Real.cos t) (Real.sin t))ᴴ
      * EqvK2Converse.phaseMat (Real.cos t) (Real.sin t) = 1 := by
  rw [phaseMat_eq_flow]
  exact conjTranspose_mul_self_of_mem (flow_transition_mem_unitary _ _ _)

theorem cycMat_unitary : EqvK2Converse.cycMatᴴ * EqvK2Converse.cycMat = 1 := by
  rw [cycMat_eq_flows]
  exact conjTranspose_mul_self_of_mem (mul_mem (mul_mem (flow_transition_mem_unitary _ _ _)
    (flow_transition_mem_unitary _ _ _)) (flow_transition_mem_unitary _ _ _))

variable {𝓘 : ImplementationClass}

theorem phaseMat_mem
    (hflow : ∀ (a b : Fin 2) (t : ℝ), 𝓘 (Fin 2) (ReachabilitySeam.flow (transition a b) t))
    (t : ℝ) : 𝓘 (Fin 2) (EqvK2Converse.phaseMat (Real.cos t) (Real.sin t)) := by
  rw [phaseMat_eq_flow]
  exact hflow 1 1 _

theorem cycMat_mem (arch : Architecture 𝓘)
    (hflow : ∀ (a b : Fin 2) (t : ℝ), 𝓘 (Fin 2) (ReachabilitySeam.flow (transition a b) t)) :
    𝓘 (Fin 2) EqvK2Converse.cycMat := by
  rw [cycMat_eq_flows]
  exact arch.mul (Fin 2) _ _ (arch.mul (Fin 2) _ _ (hflow 0 0 _) (hflow 1 1 _)) (hflow 0 1 _)

/-! ### §B — compatibility and the combined pair theorem -/

/-- **Pair compatibility** (a premise, not sourced): every admitted unitary on the pair carrier maps
the cone into itself through the dictionary. -/
def PairCompat (𝓘 : ImplementationClass) (K : Set (CompositeDimension.W 3)) : Prop :=
  ∀ U : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ, 𝓘 (Fin 2 × Fin 2) U → Uᴴ * U = 1 →
    ∀ ω ∈ K, ∃ ω' ∈ K, EqvK2Schema.dict ω' = U * EqvK2Schema.dict ω * Uᴴ

/-- A map of tables intertwined with conjugation by an admitted unitary preserves a compatible
cone. -/
theorem mem_of_compat {K : Set (CompositeDimension.W 3)} (h : PairCompat 𝓘 K)
    {U : Matrix (Fin 2 × Fin 2) (Fin 2 × Fin 2) ℂ} (hU : 𝓘 (Fin 2 × Fin 2) U) (hu : Uᴴ * U = 1)
    {f : CompositeDimension.W 3 → CompositeDimension.W 3}
    (hf : ∀ ω, EqvK2Schema.dict (f ω) = U * EqvK2Schema.dict ω * Uᴴ) :
    ∀ ω ∈ K, f ω ∈ K := by
  intro ω hω
  obtain ⟨ω', hω', he⟩ := h U hU hu ω hω
  have hω'' : ω' = f ω := EqvK2Schema.dict_injective (he.trans (hf ω).symm)
  rwa [hω''] at hω'

/-- The gate clauses of the pair theorem from admission and compatibility. -/
theorem driveClauses_of_admitted (arch : Architecture 𝓘) (hC : ContextStable 𝓘)
    (hflow : ∀ (a b : Fin 2) (t : ℝ), 𝓘 (Fin 2) (ReachabilitySeam.flow (transition a b) t))
    (hswap : 𝓘 (Fin 2 × Fin 2)
      (CoherentLift.permMatrix (Equiv.swap ((1 : Fin 2), (0 : Fin 2)) (1, 1))))
    {K : Set (CompositeDimension.W 3)} (hcompat : PairCompat 𝓘 K) :
    (∀ ω ∈ K, CompositeDimension.cnot ω ∈ K) ∧ ∀ t : ℝ, ∀ ω ∈ K,
      CompositeDimension.actT (KInfFoundations.rotLin t) ω ∈ K ∧
      CompositeDimension.actT
        (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K := by
  refine ⟨mem_of_compat hcompat (f := fun ω => CompositeDimension.cnot ω)
    (by rw [cnotMat_eq_swap]; exact hswap) cnotMat_unitary fun ω => ?_, fun t ω hω => ⟨?_, ?_⟩⟩
  · rw [cnotMat_conjTranspose]
    exact BridgeDictionary.dict_cnot ω
  · exact mem_of_compat hcompat (hC (Fin 2) (Fin 2) _ (phaseMat_mem hflow t))
      (tensorOf_one_isometry' (phaseMat_unitary t))
      (f := fun ω => CompositeDimension.actT (KInfFoundations.rotLin t) ω)
      (fun ω => EqvK2Converse.dict_actT_rotLin t ω) ω hω
  · exact mem_of_compat hcompat (hC (Fin 2) (Fin 2) _ (cycMat_mem arch hflow))
      (tensorOf_one_isometry' cycMat_unitary)
      (f := fun ω => CompositeDimension.actT
        (KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω)
      (fun ω => EqvK2Converse.dict_actT_cyc ω) ω hω

/-- **The combined pair theorem, admission form.** -/
theorem pairCone_eq_Q3_of_admitted (arch : Architecture 𝓘) (hC : ContextStable 𝓘)
    (hflow : ∀ (a b : Fin 2) (t : ℝ), 𝓘 (Fin 2) (ReachabilitySeam.flow (transition a b) t))
    (hswap : 𝓘 (Fin 2 × Fin 2)
      (CoherentLift.permMatrix (Equiv.swap ((1 : Fin 2), (0 : Fin 2)) (1, 1))))
    {K : Set (CompositeDimension.W 3)} (hcompat : PairCompat 𝓘 K)
    (hH1 : ∀ x ∈ TransitiveBody.eball 3, ∀ y ∈ TransitiveBody.eball 3,
      CompositeDimension.prodState x y ∈ K)
    (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K)
    (hmax : K ⊆ CompositeDimension.maxCone (TransitiveBody.eball 3)) : K = EqvK2Schema.Q3 :=
  EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone hH1 hadd hsmul hmax
    (driveClauses_of_admitted arch hC hflow hswap hcompat).1
    (driveClauses_of_admitted arch hC hflow hswap hcompat).2

/-- **The combined pair theorem, drivability form.** -/
theorem pairCone_eq_Q3_of_drives (arch : Architecture 𝓘) (hC : ContextStable 𝓘)
    (hd : DrivesElementary 𝓘) {K : Set (CompositeDimension.W 3)} (hcompat : PairCompat 𝓘 K)
    (hH1 : ∀ x ∈ TransitiveBody.eball 3, ∀ y ∈ TransitiveBody.eball 3,
      CompositeDimension.prodState x y ∈ K)
    (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K)
    (hmax : K ⊆ CompositeDimension.maxCone (TransitiveBody.eball 3)) : K = EqvK2Schema.Q3 :=
  pairCone_eq_Q3_of_admitted arch hC (fun a b t => hd.1 (Fin 2) a b t)
    (hd.2.1 (Fin 2 × Fin 2) _ _) hcompat hH1 hadd hsmul hmax

/-- **The combined pair theorem, quantum-architecture form.** Label and dagger stability are not
used. -/
theorem pairCone_eq_Q3_of_quantumArchitecture (hQ : QuantumArchitecture 𝓘)
    {K : Set (CompositeDimension.W 3)} (hcompat : PairCompat 𝓘 K)
    (hH1 : ∀ x ∈ TransitiveBody.eball 3, ∀ y ∈ TransitiveBody.eball 3,
      CompositeDimension.prodState x y ∈ K)
    (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K)
    (hmax : K ⊆ CompositeDimension.maxCone (TransitiveBody.eball 3)) : K = EqvK2Schema.Q3 :=
  pairCone_eq_Q3_of_drives hQ.arch hQ.context hQ.drives hcompat hH1 hadd hsmul hmax

/-! ### §C — controls -/

/-- Compatibility holds for `Q3` and every class: unitary conjugation preserves positivity. -/
theorem pairCompat_Q3 (𝓘 : ImplementationClass) : PairCompat 𝓘 EqvK2Schema.Q3 := by
  intro U _ _ ω hω
  have hpsd : (U * EqvK2Schema.dict ω * Uᴴ).PosSemidef :=
    (EqvK2Schema.mem_Q3.mp hω).mul_mul_conjTranspose_same U
  refine ⟨EqvK2Schema.coordOf (U * EqvK2Schema.dict ω * Uᴴ), ?_,
    EqvK2Schema.dict_coordOf _ hpsd.isHermitian⟩
  rw [EqvK2Schema.mem_Q3, EqvK2Schema.dict_coordOf _ hpsd.isHermitian]
  exact hpsd

/-- **Positive control**: the full class with `Q3` satisfies every class-side premise. -/
theorem fullClass_pairControl :
    Architecture fullClass ∧ ContextStable fullClass ∧ DrivesElementary fullClass ∧
      PairCompat fullClass EqvK2Schema.Q3 :=
  ⟨fullClass_quantumArchitecture.arch, fullClass_quantumArchitecture.context,
    fullClass_quantumArchitecture.drives, pairCompat_Q3 fullClass⟩

/-- **Converse control**: the diagonal class with `Q3` satisfies the four closure clauses and
compatibility, and does not drive the elementary transitions. -/
theorem diagClass_pairControl :
    Architecture diagClass ∧ ContextStable diagClass ∧ LabelInvariant diagClass ∧
      DaggerStable diagClass ∧ PairCompat diagClass EqvK2Schema.Q3 ∧
      ¬ DrivesElementary diagClass :=
  ⟨diagClass_arch, diagClass_contextStable, diagClass_labelInvariant, diagClass_daggerStable,
    pairCompat_Q3 diagClass, diagClass_not_drivesElementary⟩

/-- The pair cone being `Q3`, with compatibility and the four closure clauses, does not give
drivability. -/
theorem not_drives_of_pairCompat :
    ¬ ∀ 𝓘 : ImplementationClass, Architecture 𝓘 → ContextStable 𝓘 → LabelInvariant 𝓘 →
      DaggerStable 𝓘 → PairCompat 𝓘 EqvK2Schema.Q3 → DrivesElementary 𝓘 :=
  fun h => diagClass_not_drivesElementary (h diagClass diagClass_arch diagClass_contextStable
    diagClass_labelInvariant diagClass_daggerStable (pairCompat_Q3 diagClass))

/-! ### §D — correlations at the pair, with availability explicit -/

/-- The correlator of the two-outcome sharp measurements along `a` and `b`. -/
def corr (a b : Fin 3 → ℝ) (ω : CompositeDimension.W 3) : ℝ :=
  CompositeDimension.prodEffVal (EffectSpace.sharpEff a) (EffectSpace.sharpEff b) ω
    - CompositeDimension.prodEffVal (EffectSpace.sharpEff a) (EffectSpace.sharpEff (-b)) ω
    - CompositeDimension.prodEffVal (EffectSpace.sharpEff (-a)) (EffectSpace.sharpEff b) ω
    + CompositeDimension.prodEffVal (EffectSpace.sharpEff (-a)) (EffectSpace.sharpEff (-b)) ω

/-- The CHSH combination. -/
def chsh (a a' b b' : Fin 3 → ℝ) (ω : CompositeDimension.W 3) : ℝ :=
  corr a b ω + corr a b' ω + corr a' b ω - corr a' b' ω

/-- A two-outcome sharp measurement along `c` is available. -/
def BinaryAvail (avail : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ)) (c : Fin 3 → ℝ) : Prop :=
  EffectSpace.sharpEff c ∈ avail ∧ EffectSpace.sharpEff (-c) ∈ avail

theorem binaryAvail_of_unit {avail : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ)}
    (hsharp : EffectSpace.sharpFamily 3 ⊆ avail) {c : Fin 3 → ℝ} (hc : ∑ j, c j ^ 2 = 1) :
    BinaryAvail avail c :=
  ⟨hsharp ⟨c, hc, rfl⟩, hsharp ⟨-c, by rw [EffectSpace.sum_neg_sq]; exact hc, rfl⟩⟩

theorem corr_phiW (a b : Fin 3 → ℝ) :
    corr a b CompositeDimension.phiW = a 0 * b 0 - a 1 * b 1 + a 2 * b 2 := by
  first
    | (simp [corr, CompositeDimension.prodEffVal, EffectSpace.sharpEff,
        CompositeDimension.ehom_affOf, CompositeDimension.pairVal, Fin.sum_univ_four,
        CompositeDimension.phiW, EffectSpace.sharpVec]; done)
    | (simp [corr, CompositeDimension.prodEffVal, EffectSpace.sharpEff,
        CompositeDimension.ehom_affOf, CompositeDimension.pairVal, Fin.sum_univ_four,
        CompositeDimension.phiW, EffectSpace.sharpVec]; ring)

/-- The second party's settings `(x ± z)/√2`, with `x` the first and `z` the third axis. -/
def bPlus : Fin 3 → ℝ := ![Real.sqrt 2 / 2, 0, Real.sqrt 2 / 2]

def bMinus : Fin 3 → ℝ := ![-(Real.sqrt 2 / 2), 0, Real.sqrt 2 / 2]

theorem chsh_phiW :
    chsh CompositeDimension.z3 CompositeDimension.xplus bPlus bMinus CompositeDimension.phiW
      = 2 * Real.sqrt 2 := by
  rw [chsh, corr_phiW, corr_phiW, corr_phiW, corr_phiW]
  first
    | (simp [CompositeDimension.z3, CompositeDimension.xplus, bPlus, bMinus]; done)
    | (simp [CompositeDimension.z3, CompositeDimension.xplus, bPlus, bMinus]; ring)

theorem z3_unit : ∑ j, CompositeDimension.z3 j ^ 2 = 1 := by
  rw [Fin.sum_univ_three]
  simp [CompositeDimension.z3]

theorem xplus_unit : ∑ j, CompositeDimension.xplus j ^ 2 = 1 := by
  rw [Fin.sum_univ_three]
  simp [CompositeDimension.xplus]

theorem bPlus_unit : ∑ j, bPlus j ^ 2 = 1 := by
  have h := Real.sq_sqrt (show (0 : ℝ) ≤ 2 by norm_num)
  rw [Fin.sum_univ_three]
  first
    | (simp [bPlus]; done)
    | (simp [bPlus]; linear_combination h / 2)
    | (simp [bPlus]; norm_num)
    | (simp [bPlus]; nlinarith [h])

theorem bMinus_unit : ∑ j, bMinus j ^ 2 = 1 := by
  have h := Real.sq_sqrt (show (0 : ℝ) ≤ 2 by norm_num)
  rw [Fin.sum_univ_three]
  first
    | (simp [bMinus]; done)
    | (simp [bMinus]; linear_combination h / 2)
    | (simp [bMinus]; norm_num)
    | (simp [bMinus]; nlinarith [h])

/-- **Attainment with availability explicit.** If the products are available preparations, the
controlled NOT carries available preparations to available preparations, and the sharp tests are
available, then an available preparation and four available two-outcome sharp measurements give
CHSH value `2√2`. -/
theorem chsh_attained_of_available {prep : Set (CompositeDimension.W 3)}
    {avail : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ)}
    (hprod : ∀ x ∈ TransitiveBody.eball 3, ∀ y ∈ TransitiveBody.eball 3,
      CompositeDimension.prodState x y ∈ prep)
    (hcnot : ∀ ω ∈ prep, CompositeDimension.cnot ω ∈ prep)
    (hsharp : EffectSpace.sharpFamily 3 ⊆ avail) :
    ∃ ω ∈ prep, ∃ a a' b b' : Fin 3 → ℝ, BinaryAvail avail a ∧ BinaryAvail avail a' ∧
      BinaryAvail avail b ∧ BinaryAvail avail b' ∧ chsh a a' b b' ω = 2 * Real.sqrt 2 := by
  have hω : CompositeDimension.phiW ∈ prep := by
    rw [← CompositeDimension.cnot_prodState_xplus_z3]
    exact hcnot _ (hprod _ CompositeDimension.xplus_mem _ CompositeDimension.z3_mem)
  exact ⟨_, hω, _, _, _, _, binaryAvail_of_unit hsharp z3_unit,
    binaryAvail_of_unit hsharp xplus_unit, binaryAvail_of_unit hsharp bPlus_unit,
    binaryAvail_of_unit hsharp bMinus_unit, chsh_phiW⟩

/-- **The pair clause.** Under the class-side premises, with the available preparations compatible
with every admitted unitary, containing the products, closed under mixing, and with the sharp tests
available and valid on every available preparation: the available preparations are exactly `Q3`,
and an available protocol attains CHSH value `2√2`. -/
theorem pair_available_eq_Q3_and_chsh (arch : Architecture 𝓘) (hC : ContextStable 𝓘)
    (hd : DrivesElementary 𝓘) {prep : Set (CompositeDimension.W 3)}
    {avail : Set ((Fin 3 → ℝ) →ᵃ[ℝ] ℝ)} (hcompat : PairCompat 𝓘 prep)
    (hprod : ∀ x ∈ TransitiveBody.eball 3, ∀ y ∈ TransitiveBody.eball 3,
      CompositeDimension.prodState x y ∈ prep)
    (hadd : ∀ ω ∈ prep, ∀ η ∈ prep, ω + η ∈ prep)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ prep, c • ω ∈ prep)
    (hvalid : prep ⊆ EffectSpace.maxConeOf avail)
    (hsharp : EffectSpace.sharpFamily 3 ⊆ avail) :
    prep = EqvK2Schema.Q3 ∧ ∃ ω ∈ prep, ∃ a a' b b' : Fin 3 → ℝ, BinaryAvail avail a ∧
      BinaryAvail avail a' ∧ BinaryAvail avail b ∧ BinaryAvail avail b' ∧
      chsh a a' b b' ω = 2 * Real.sqrt 2 :=
  ⟨pairCone_eq_Q3_of_drives arch hC hd hcompat hprod hadd hsmul
      (EqvK2MaxCone.maxCone_bound_of_sharp_available hvalid hsharp),
    chsh_attained_of_available hprod
      (driveClauses_of_admitted arch hC (fun a b t => hd.1 (Fin 2) a b t)
        (hd.2.1 (Fin 2 × Fin 2) _ _) hcompat).1 hsharp⟩

/-- **No signalling**: the marginal of one party's test does not depend on the other party's
setting, for every joint vector. -/
theorem marginal_independent (e : (Fin 3 → ℝ) →ᵃ[ℝ] ℝ) (b b' : Fin 3 → ℝ)
    (ω : CompositeDimension.W 3) :
    CompositeDimension.prodEffVal e (EffectSpace.sharpEff b) ω
        + CompositeDimension.prodEffVal e (EffectSpace.sharpEff (-b)) ω
      = CompositeDimension.prodEffVal e (EffectSpace.sharpEff b') ω
        + CompositeDimension.prodEffVal e (EffectSpace.sharpEff (-b')) ω := by
  first
    | (simp [CompositeDimension.prodEffVal, EffectSpace.sharpEff, CompositeDimension.ehom_affOf,
        CompositeDimension.pairVal, Fin.sum_univ_four, EffectSpace.sharpVec]; done)
    | (simp [CompositeDimension.prodEffVal, EffectSpace.sharpEff, CompositeDimension.ehom_affOf,
        CompositeDimension.pairVal, Fin.sum_univ_four, EffectSpace.sharpVec]; ring)

end

end PairInterfaceDesign
end OIBridge

#print axioms OIBridge.PairInterfaceDesign.phaseMat_eq_flow
#print axioms OIBridge.PairInterfaceDesign.cycMat_eq_flows
#print axioms OIBridge.PairInterfaceDesign.cnotMat_eq_swap
#print axioms OIBridge.PairInterfaceDesign.driveClauses_of_admitted
#print axioms OIBridge.PairInterfaceDesign.pairCone_eq_Q3_of_admitted
#print axioms OIBridge.PairInterfaceDesign.pairCone_eq_Q3_of_drives
#print axioms OIBridge.PairInterfaceDesign.pairCone_eq_Q3_of_quantumArchitecture
#print axioms OIBridge.PairInterfaceDesign.pairCompat_Q3
#print axioms OIBridge.PairInterfaceDesign.fullClass_pairControl
#print axioms OIBridge.PairInterfaceDesign.diagClass_pairControl
#print axioms OIBridge.PairInterfaceDesign.not_drives_of_pairCompat
#print axioms OIBridge.PairInterfaceDesign.chsh_phiW
#print axioms OIBridge.PairInterfaceDesign.chsh_attained_of_available
#print axioms OIBridge.PairInterfaceDesign.pair_available_eq_Q3_and_chsh
#print axioms OIBridge.PairInterfaceDesign.marginal_independent
