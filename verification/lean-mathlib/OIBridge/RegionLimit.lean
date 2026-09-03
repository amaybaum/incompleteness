/-
  OIBridge/RegionLimit.lean — OI_Q Level III, first entry: the quasilocal-completion audit at the
  finite stages.

  LEVEL III, ROUND ONE. Level II closed with: under the carrier-general typed operational
  interface, current OI substratum + continuous off-diagonal controllability ⟺ exact
  finite-dimensional typed operational quantum mechanics. The remaining qualifier is
  FINITE-DIMENSIONAL. Level III asks what the substratum's own directed system of finite stages
  yields in the limit, and it asks it as an AUDIT: no continuity, completeness, or
  Hilbert-space axiom is added; the existing structure is tested and every claimed necessity
  must come with a countermodel.

  THE DIRECTED SYSTEM IS SPATIAL, NOT A REFINEMENT. The corpus is explicit that the lattice is
  the fundamental description at fixed spacing and that the continuum is a calculational
  approximation with a quantified error ([Substratum], remark on the continuum extension). No
  refinement of the lattice spacing is part of the physics. The directed system the substratum
  actually supplies is the family of finite REGIONS of the fixed-spacing lattice — increasing
  observation windows — with a finite carrier `S_Λ = ∏_{x ∈ Λ} Q` at each region. Passing from
  a region to a larger one adjoins the sites in between: `S_{Λ'} ≃ S_Λ × R`. This file works
  with that one-step form, which is the kernel's standard composite `S × R`; a tower of regions
  is an iterate of it.

  (1) THE RESTRICTION MAPS ARE ALREADY IN THE FROZEN INTERFACE. Restricting a state on the
      larger region to the smaller one is the partial trace over the adjoined factor, which is
      exactly the typed interface's `discardR` (`restrict_eq_discardR`), and its Heisenberg dual
      — extending an observable on the smaller region by the identity on the adjoined sites —
      is the tensor with the identity, with the duality `⟨X ⊗ 1, ρ⟩ = ⟨X, discard ρ⟩`
      (`trace_inclObs_mul`). The projective system of states and the inductive system of
      observables are therefore not new structure: they are the Level II discard and its dual.

  (2) CONSISTENT STATE FAMILIES EXIST WITHOUT A NEW POSTULATE. The reference family — the
      uniformly mixed adjoined factor, the only preparation the interface assumes — is
      consistent under restriction (`uniform_consistent`), and so is every pure product family
      (`pureProduct_consistent`), which Level II makes available.

  (3) THE FINITE SHADOW OF THE REPRESENTATION QUESTION. The overlap between the reference
      family and a pure product family on a region of `n` adjoined sites with `q` states each is
      the overlap on the base times `q^{-n}` (`overlap_uniform_pure`), so for every tolerance
      there is a region on which the two families are that close to orthogonal
      (`overlap_eventually_small`). This is the finite-stage content of the statement that the
      two families generate inequivalent representations in the infinite-volume limit: the
      finite stages determine the algebra and the consistent families, and compatible
      families that look inequivalent already occur at finite stages. Whether a distinguished
      representation is a theory-level input, or merely a state selection within one quasilocal
      theory (one algebra, many states, each with its own representation), is OPEN — outcome B
      of the pre-registered fork is not decided here.

  (4) CONTINUOUS TIME IS ADDITIONAL STRUCTURE — THE COUNTERMODEL. The substratum dynamics is a
      finite bijection; the corpus already states that a continuous one-parameter
      interpolation of a finite permutation is additional structure ([SM §2], [Main §3.2]).
      The kernel makes that a theorem: two Hermitian generators on the qubit whose passive
      flows agree at every integer time and differ at half-integer time
      (`continuous_extension_not_unique`). Every discrete-time datum is the same; the
      continuous-time law is not determined by it. Outcome C of the fork is DECIDED as a no-go:
      discrete evolution does not determine a continuous interpolation. Whether that is a
      missing ingredient depends on the target — none is needed for discrete-time quasilocal
      quantum mechanics, and a continuous-time dynamical law is an additional input only for
      the continuous-time Hamiltonian formulation.

  (5) NO CONTINUUM-STRUCTURE GAP ARISES because no continuum structure is claimed: the
      substratum has no refinement system to complete, so outcome D is empty by the corpus's
      own statement of what the lattice is.

  THE AUDIT SUMMARY (`continuum_audit_round1`) bundles (1)–(4). WHAT IS NOT CLAIMED: no
  infinite-volume algebra is constructed in the kernel; no representation is selected; no
  continuity axiom is introduced; nothing bears on `L²(ℝ³)`, which the corpus does not claim as
  a physical object. Bare OI and the frozen Level I and Level II statements are untouched.
-/

import OIBridge.TypedCompletion

namespace OIBridge
namespace RegionLimit

open Complex Matrix CoherentExtension MonoidalCompletion CoherentLift IndependenceCensus
open OperationalAssembly StinespringAssembly KrausSoundness CompositeSoundness
open DimensionalObstruction DimensionalCountermodel ReferenceExtension ReferenceSufficiency
open BoundaryAudit SpectatorBridge AncillaClosure ClosureObstruction CompositionalIndependence
open OIRealization OperationalValidity LevelOneSeam PhysicalCharacterization DiagonalTheory
open HiddenCoherence RankGapTheory GeneralCarrier ControlLie ReachabilitySeam OrbitReachability
open SubstantiveCensus OperationalRigidity OIHierarchy PrimitiveSource InterventionLocality
open MicroReversibility LieRankSource SubstratumSource SubstratumInterface ReadWriteControl
open StructuralClosure TypedCompletion

open scoped ComplexOrder Kronecker Matrix.Norms.L2Operator

/-! ### Section A — the one-step region extension: restriction and its dual -/

section Restriction

variable {S R : Type} [Fintype S] [DecidableEq S] [Fintype R] [DecidableEq R]

/-- Restricting a state on the larger region `S × R` to the region `S`: the partial trace over
the adjoined factor. -/
def restrict (R : Type) [Fintype R] [DecidableEq R] :
    Matrix (S × R) (S × R) ℂ →ₗ[ℂ] Matrix S S ℂ := discardR R

/-- **THE RESTRICTION IS THE LEVEL II DISCARD.** -/
theorem restrict_eq_discardR : restrict (S := S) R = discardR R := rfl

/-- Extending an observable on the region `S` by the identity on the adjoined sites. -/
def inclObs (R : Type) [Fintype R] [DecidableEq R] (X : Matrix S S ℂ) :
    Matrix (S × R) (S × R) ℂ := tensorOf X 1

theorem inclObs_apply (X : Matrix S S ℂ) (p q : S × R) :
    inclObs R X p q = X p.1 q.1 * (if p.2 = q.2 then 1 else 0) := by
  simp [inclObs, tensorOf_apply, Matrix.one_apply]

/-- The trace of a tensor is the product of the traces. -/
theorem trace_tensorOf (A : Matrix S S ℂ) (B : Matrix R R ℂ) :
    (tensorOf A B).trace = A.trace * B.trace := by
  simp only [Matrix.trace, Matrix.diag_apply, tensorOf_apply, Fintype.sum_prod_type,
    Finset.sum_mul_sum]

/-- Tensors multiply factorwise. -/
theorem tensorOf_mul (A C : Matrix S S ℂ) (B D : Matrix R R ℂ) :
    tensorOf A B * tensorOf C D = tensorOf (A * C) (B * D) := by
  ext p q
  simp only [Matrix.mul_apply, tensorOf_apply, Fintype.sum_prod_type, Finset.sum_mul_sum]
  refine Finset.sum_congr rfl fun u _ => Finset.sum_congr rfl fun v _ => ?_
  ring

/-- **DUALITY**: pairing an extended observable with a state on the larger region is pairing
the observable with the restricted state. -/
theorem trace_inclObs_mul (X : Matrix S S ℂ) (ρ : Matrix (S × R) (S × R) ℂ) :
    (inclObs R X * ρ).trace = (X * restrict R ρ).trace := by
  simp only [Matrix.trace, Matrix.diag_apply, Matrix.mul_apply, inclObs_apply, restrict,
    discardR_apply, Fintype.sum_prod_type, Finset.mul_sum, Finset.sum_mul]
  -- LHS: ∑ s, ∑ r, ∑ t, ∑ u, X s t * (if r = u then 1 else 0) * ρ (t, u) (s, r)
  -- RHS: ∑ s, ∑ t, ∑ r, X s t * ρ (t, r) (s, r)
  refine Finset.sum_congr rfl fun s _ => ?_
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun t _ => ?_
  refine Finset.sum_congr rfl fun r _ => ?_
  rw [Finset.sum_eq_single r (fun u _ hu => by simp [Ne.symm hu]) (by simp)]
  simp

end Restriction

/-! ### Section B — consistent families: the reference family and the pure product families -/

section Families

variable {S R : Type} [Fintype S] [DecidableEq S] [Fintype R] [DecidableEq R]

/-- The reference (uniformly mixed) extension of a state to the larger region. -/
noncomputable def uniformExt (R : Type) [Fintype R] [DecidableEq R] (ρ : Matrix S S ℂ) :
    Matrix (S × R) (S × R) ℂ := attachUniform R ρ

/-- The pure product extension: the adjoined sites in the basis state `r`. -/
def pureExt (r : R) (ρ : Matrix S S ℂ) : Matrix (S × R) (S × R) ℂ :=
  tensorOf ρ (Matrix.single r r 1)

/-- **THE REFERENCE FAMILY IS CONSISTENT UNDER RESTRICTION.** -/
theorem uniform_consistent [Nonempty R] (ρ : Matrix S S ℂ) :
    restrict R (uniformExt R ρ) = ρ :=
  discardR_attachUniform R ρ

/-- **EVERY PURE PRODUCT FAMILY IS CONSISTENT UNDER RESTRICTION.** -/
theorem pureProduct_consistent (r : R) (ρ : Matrix S S ℂ) :
    restrict R (pureExt r ρ) = ρ := by
  ext s t
  simp only [restrict, discardR_apply, pureExt, tensorOf_apply, Matrix.single_apply]
  simp [Finset.sum_ite_eq']

end Families

/-! ### Section C — the finite shadow of the representation question -/

section Overlap

variable {S Q : Type} [Fintype S] [DecidableEq S] [Fintype Q] [DecidableEq Q]

/-- The region with `n` adjoined sites of `q = |Q|` states each: the carrier `S × (Fin n → Q)`. -/
abbrev regionCarrier (S Q : Type) (n : ℕ) := S × (Fin n → Q)

/-- The reference family on the `n`-site region. -/
noncomputable def uniformRegion (n : ℕ) (ρ : Matrix S S ℂ) :
    Matrix (regionCarrier S Q n) (regionCarrier S Q n) ℂ :=
  uniformExt (Fin n → Q) ρ

/-- A pure product family on the `n`-site region, the adjoined sites in the configuration `f`. -/
def pureRegion (n : ℕ) (f : Fin n → Q) (ρ : Matrix S S ℂ) :
    Matrix (regionCarrier S Q n) (regionCarrier S Q n) ℂ :=
  pureExt f ρ

/-- **THE OVERLAP DECAYS AS `q^{-n}`**: the pairing of the reference family with a pure product
family on `n` sites is the base pairing times `|Q|^{-n}`. -/
theorem overlap_uniform_pure (n : ℕ) (f : Fin n → Q) (ρ π : Matrix S S ℂ) :
    (uniformRegion (Q := Q) n ρ * pureRegion n f π).trace
      = (ρ * π).trace * ((Fintype.card Q : ℂ) ^ n)⁻¹ := by
  simp only [uniformRegion, uniformExt, attachUniform_apply, pureRegion, pureExt, tensorOf_mul,
    trace_tensorOf, Matrix.smul_mul, Matrix.one_mul, Matrix.trace_smul, Matrix.trace_single_eq_same,
    smul_eq_mul, Fintype.card_fun, Fintype.card_fin]
  push_cast
  ring

/-- **FOR EVERY TOLERANCE THERE IS A REGION ON WHICH THE TWO FAMILIES ARE THAT CLOSE TO
ORTHOGONAL**: the finite-stage content of representation inequivalence, given at least two
states per site. -/
theorem overlap_eventually_small (hq : 2 ≤ Fintype.card Q) (ρ π : Matrix S S ℂ) (ε : ℝ)
    (hε : 0 < ε) :
    ∃ n : ℕ, ∀ f : Fin n → Q,
      ‖(uniformRegion (Q := Q) n ρ * pureRegion n f π).trace‖ < ε := by
  set c : ℝ := ‖(ρ * π).trace‖ with hc
  have hq1 : (1 : ℝ) / (Fintype.card Q : ℝ) < 1 := by
    rw [div_lt_one (by exact_mod_cast (by omega : 0 < Fintype.card Q))]
    exact_mod_cast (by omega : 1 < Fintype.card Q)
  have hq0 : (0 : ℝ) ≤ 1 / (Fintype.card Q : ℝ) := by positivity
  obtain ⟨n, hn⟩ := exists_pow_lt_of_lt_one (show 0 < ε / (c + 1) by positivity) hq1
  refine ⟨n, fun f => ?_⟩
  rw [overlap_uniform_pure, norm_mul, norm_inv, norm_pow, Complex.norm_natCast]
  have hcpos : 0 < c + 1 := by positivity
  calc c * ((Fintype.card Q : ℝ) ^ n)⁻¹
      = c * (1 / (Fintype.card Q : ℝ)) ^ n := by rw [_root_.one_div_pow, one_div]
    _ ≤ (c + 1) * (1 / (Fintype.card Q : ℝ)) ^ n := by
        gcongr
        linarith
    _ < (c + 1) * (ε / (c + 1)) := by gcongr
    _ = ε := by field_simp

end Overlap

/-! ### Section D — continuous time is additional structure: the countermodel -/

section Continuity

/-- The trivial generator. -/
def genZero : Matrix (Fin 2) (Fin 2) ℂ := 0

/-- A generator with a `2π` eigenvalue on one state and `0` on the other. -/
noncomputable def genTwoPi : Matrix (Fin 2) (Fin 2) ℂ :=
  Matrix.diagonal fun i => if i = 0 then ((2 * Real.pi : ℝ) : ℂ) else 0

theorem genZero_hermitian : genZeroᴴ = genZero := by
  simp [genZero]

theorem genTwoPi_hermitian : genTwoPiᴴ = genTwoPi := by
  ext i j
  rw [Matrix.conjTranspose_apply, genTwoPi, Matrix.diagonal_apply, Matrix.diagonal_apply]
  by_cases h : i = j
  · subst h
    split_ifs <;> simp
  · rw [if_neg (Ne.symm h), if_neg h, star_zero]

/-- The flow of the trivial generator is the identity at every time. -/
theorem flow_genZero (t : ℝ) : flow genZero t = 1 := by
  simp [flow, genZero, NormedSpace.exp_zero]

/-- The flow of `genTwoPi` at time `t` is diagonal with entries `e^{-2πit}` and `1`. -/
theorem flow_genTwoPi (t : ℝ) :
    flow genTwoPi t
      = Matrix.diagonal fun i => if i = 0 then Complex.exp (-(t : ℂ) * Complex.I * (2 * Real.pi))
          else 1 := by
  rw [flow, genTwoPi, ← Matrix.diagonal_smul, Matrix.exp_diagonal]
  congr 1
  funext i
  rw [Pi.exp_def]
  simp only [Pi.smul_apply, smul_eq_mul]
  split_ifs
  · rw [← Complex.exp_eq_exp_ℂ]
    congr 1
    push_cast
    ring
  · rw [mul_zero, NormedSpace.exp_zero]

/-- **THE TWO FLOWS AGREE AT EVERY INTEGER TIME.** -/
theorem flows_agree_integer (n : ℕ) : flow genZero n = flow genTwoPi n := by
  rw [flow_genZero, flow_genTwoPi]
  ext i j
  rw [Matrix.one_apply, Matrix.diagonal_apply]
  split_ifs with h1 h2
  · subst h1
    rw [show (-((n : ℝ) : ℂ) * Complex.I * (2 * Real.pi)) = ((-n : ℤ) : ℂ) * (2 * Real.pi * Complex.I) by
      push_cast; ring]
    rw [Complex.exp_int_mul_two_pi_mul_I]
  · rfl
  · rfl

/-- **THE TWO FLOWS DIFFER AT HALF-INTEGER TIME.** -/
theorem flows_differ_half : flow genZero (1 / 2) ≠ flow genTwoPi (1 / 2) := by
  rw [flow_genZero, flow_genTwoPi]
  intro h
  have h00 := congrFun (congrFun h 0) 0
  rw [Matrix.one_apply_eq, Matrix.diagonal_apply_eq, if_pos rfl] at h00
  have : Complex.exp (-((1 / 2 : ℝ) : ℂ) * Complex.I * (2 * Real.pi)) = -1 := by
    rw [show (-((1 / 2 : ℝ) : ℂ) * Complex.I * (2 * Real.pi)) = -(Real.pi * Complex.I) by
      push_cast; ring]
    rw [Complex.exp_neg, Complex.exp_pi_mul_I]
    norm_num
  rw [this] at h00
  norm_num at h00

/-- **CONTINUOUS TIME IS NOT DETERMINED BY THE DISCRETE DYNAMICS.** Two Hermitian generators
whose passive flows are isometries, agree at every integer time, and differ at time `1/2`. -/
theorem continuous_extension_not_unique :
    ∃ H₀ H₁ : Matrix (Fin 2) (Fin 2) ℂ, H₀ᴴ = H₀ ∧ H₁ᴴ = H₁
      ∧ (∀ t : ℝ, (flow H₀ t)ᴴ * flow H₀ t = 1) ∧ (∀ t : ℝ, (flow H₁ t)ᴴ * flow H₁ t = 1)
      ∧ (∀ n : ℕ, flow H₀ n = flow H₁ n) ∧ flow H₀ (1 / 2) ≠ flow H₁ (1 / 2) :=
  ⟨genZero, genTwoPi, genZero_hermitian, genTwoPi_hermitian,
    flow_isometry genZero genZero_hermitian, flow_isometry genTwoPi genTwoPi_hermitian,
    flows_agree_integer, flows_differ_half⟩

end Continuity

/-! ### Section E — the audit summary -/

section Summary

/-- **THE QUASILOCAL-COMPLETION AUDIT, FIRST ENTRY.** (1) the region restriction is the Level II
discard with the observable inclusion as its dual; (2) the reference family and every pure
product family are consistent under restriction; (3) their overlap on `n` adjoined sites decays
as `|Q|^{-n}`; (4) continuous time is not determined by the discrete dynamics. -/
theorem continuum_audit_round1 :
    (∀ (S R : Type) [Fintype S] [DecidableEq S] [Fintype R] [DecidableEq R]
        (X : Matrix S S ℂ) (ρ : Matrix (S × R) (S × R) ℂ),
        restrict R = discardR (S := S) R ∧ (inclObs R X * ρ).trace = (X * restrict R ρ).trace)
    ∧ (∀ (S R : Type) [Fintype S] [DecidableEq S] [Fintype R] [DecidableEq R] [Nonempty R]
        (ρ : Matrix S S ℂ) (r : R),
        restrict R (uniformExt R ρ) = ρ ∧ restrict R (pureExt r ρ) = ρ)
    ∧ (∀ (S Q : Type) [Fintype S] [DecidableEq S] [Fintype Q] [DecidableEq Q]
        (n : ℕ) (f : Fin n → Q) (ρ π : Matrix S S ℂ),
        (uniformRegion (Q := Q) n ρ * pureRegion n f π).trace
          = (ρ * π).trace * ((Fintype.card Q : ℂ) ^ n)⁻¹)
    ∧ (∃ H₀ H₁ : Matrix (Fin 2) (Fin 2) ℂ, H₀ᴴ = H₀ ∧ H₁ᴴ = H₁
        ∧ (∀ n : ℕ, flow H₀ n = flow H₁ n) ∧ flow H₀ (1 / 2) ≠ flow H₁ (1 / 2)) :=
  ⟨fun _ _ _ _ _ _ X ρ => ⟨restrict_eq_discardR, trace_inclObs_mul X ρ⟩,
    fun _ _ _ _ _ _ _ ρ r => ⟨uniform_consistent ρ, pureProduct_consistent r ρ⟩,
    fun _ _ _ _ _ _ n f ρ π => overlap_uniform_pure n f ρ π,
    ⟨genZero, genTwoPi, genZero_hermitian, genTwoPi_hermitian, flows_agree_integer,
      flows_differ_half⟩⟩

end Summary

#print axioms restrict_eq_discardR
#print axioms trace_tensorOf
#print axioms tensorOf_mul
#print axioms trace_inclObs_mul
#print axioms uniform_consistent
#print axioms pureProduct_consistent
#print axioms overlap_uniform_pure
#print axioms overlap_eventually_small
#print axioms genZero_hermitian
#print axioms genTwoPi_hermitian
#print axioms flow_genZero
#print axioms flow_genTwoPi
#print axioms flows_agree_integer
#print axioms flows_differ_half
#print axioms continuous_extension_not_unique
#print axioms continuum_audit_round1

end RegionLimit
end OIBridge
