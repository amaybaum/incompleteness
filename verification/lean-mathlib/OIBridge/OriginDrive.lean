import OIBridge.OriginTokenOrder
import OIBridge.OriginAngle
import OIBridge.BridgeAvailFull
import OIBridge.FrozenSourcing
import Mathlib.NumberTheory.Zsqrtd.GaussianInt
import Mathlib.Data.ZMod.Basic
import Mathlib.Algebra.Polynomial.Roots
import Mathlib.Data.Fintype.Pigeonhole

/-!
# Origin drive — design module of the research thread `research/origin` (round 5, O14)

A design artifact on a disposable branch; it is not part of any governed round and asserts no
status. It imports this thread's `OriginTokenOrder` and `OriginAngle` and the bridge thread's
`BridgeAvail` and `BridgeAvailFull` (research/bridge @ a34d20b5, carried verbatim with attribution).
Every statement is about operational availability in the kernel's protocols; the object of each
theorem is named: the **reversible group** at a carrier (the available unitary conjugations, closed
under composition and, where `InverseAccessibility` holds, inverse) or the **`InstAvail` closure**
(every protocol, ancilla blocks and relabellings of members at every level).

* **The drive** (`OpDrive`): the one-outcome conjugation by `diag(1, w) ⊗ 1ₙ`, `w = 3/5 + (4/5) i`,
  available on the token at every positive level (the bridge's `TokenAvailAt`). It holds for the
  monomial interface and the full class and fails on every fourth-root lattice — the stated access,
  `MixR ∅`, FM's `latticeClass` (`not_opDrive_of_quartLattice`).
* **I4.60 supplies it** (`opDrive_of_substratumAvail`, through the kernel's `diagonal_avail`), and FM
  fails I4.60 (`lattice_not_substratumAvail`).
* **Control entails it** (`opDrive_of_control`, `opDrive_of_qm`): composite unitary control, and so
  exact quantum mechanics, on the token's generated theory makes the drive available at every level.
* **The phase intervention at θ₀ as a class** (`driveClass`: submonomial, any two nonzero entries
  with fourth powers equal up to powers of `w⁴`): an architecture, context-stable, label-invariant,
  dagger-stable, unitary-ray saturated, structurally closed and configuration-level; its theory has
  `DerivedOI` on every carrier and `InverseAccessibility`; it has the drive (`opDrive_drive`) and no
  mixer (`drive_not_uJ`, `drive_not_rot`), and it is not quantum mechanics, has no composite control,
  no phase-free richness and no executable layer flow (`driveTheory_not_qm` and its neighbours).
* **The reversible group of a ray-saturated class is exactly the class's unitaries** at every
  carrier (`avail_unitary_iff`): the `InstAvail` closure adds no unitary conjugation beyond the
  class; in every submonomial class every available unitary is a multiple of a monomial
  (`avail_monomial_of_submonomial`), and the level-one clause of `DenseUnitaryControl` fails: the
  balanced mixer stays at operator distance `√2/2` from every available unitary up to phase
  (`not_levelOneClause_of_submonomial`; instances for the drive class, FM and the monomial interface,
  the phase intervention at every angle included).
* **The drive is the identity on every monomial token body** (`diagonal_trivial_on_body`,
  `zPh_trivial_on_drive_body`, `zPh_trivial_on_substratum_body`): on the stated access and on every
  monomial extension the token body is configuration-diagonal and every diagonal unitary fixes it.
* **The stated access's reversible group** (`lattice_avail_iff`, `lattice_avail_finite_upToScalar`,
  `mixEmpty_avail_finite_upToScalar`, `rootLat_pow_scalar`, `lattice_pow_scalar`,
  `lattice_not_infiniteOrderOn_univ`, `lattice_not_ordInf`): in FM, and so for `MixR ∅`, every
  available unitary — by every protocol, every composition included — is a nonzero multiple of a
  matrix with entries in `{0} ∪ μ₄`, a finite set at each carrier: the reversible group is finite up
  to scalar, and each of its elements has a scalar power; while the drive
  (`zPh_infiniteOrderOn_univ`) has infinite order on the full matrix algebra and is the identity on
  the body.
* **The non-torsion phase** (`w345_pow_ne_one`, `theta0`, `exp_theta0`, `irrational_theta0_div_pi`):
  `w` is no root of unity, so the fixed gate at `θ₀ = arccos (3/5)` has the kernel's dense unitary
  control (`fixedGateTheory_theta0_denseUnitaryControl`) and is not exact quantum mechanics
  (`fixedGateTheory_theta0_not_qm`): density is not exactness.
* **Descent** (`discard_tokOp_eq`, `tokenAvail_descend`): the uniform discard of
  `conjChannel (U ⊗ 1ₘ₊₁)` is `conjChannel U` — the discarded family is itself a unitary conjugation
  (`discardWith_uniform_conjChannel`, the proof of the kernel's `discard_tensorOf_one`) — so token
  availability at a positive level descends to level one for a label-invariant class.
* **The Clifford angles** (`LevelOneCliffordInput`, `zPh_X_conj_not_pauli`, `not_opDrive_pi_div_four`,
  `not_opDrive_of_rotClifford`): under O9-L1 as a named input, the balanced fixed gate and every
  Clifford-angle gate fail the drive at every positive level.
-/

namespace OIBridge
namespace OriginDrive

open Matrix MonoidalCompletion InterventionLocality StructuralClosure SubstratumInterface
  SubstratumInterfaceAudit StateMixingCoupling RouteB OIRealization MicroReversibility BridgeAvail
  BridgeAvailFull OperationalAssembly ReferenceExtension OriginTokenOrder DiscreteCompletion

open scoped Matrix
open scoped Matrix.Norms.L2Operator

/-! ### §A — the operational drive at θ₀, on the stated access and under I4.60 -/

section Drive

/-- **THE OPERATIONAL DRIVE AT θ₀**: the one-outcome conjugation by `diag(1, w) ⊗ 1ₙ` is available on
the token at every positive level in the theory the architecture generates (the bridge thread's
`TokenAvailAt`; K∞-Drive's operational reading at `t = θ₀`, H-T's token clause). -/
def OpDrive (𝓘 : ImplementationClass) (arch : Architecture 𝓘) : Prop :=
  ∀ n : ℕ, 0 < n → TokenAvailAt 𝓘 arch zPh n

/-- **POSITIVE CONTROL**: the monomial interface — the phase intervention at every angle — has it. -/
theorem opDrive_substratum : OpDrive substratumClass substratumClass_arch :=
  fun n _ => substratum_tokenAvail_zPh n

/-- **POSITIVE CONTROL**: the full class has it. -/
theorem opDrive_fullClass : OpDrive fullClass fullClass_arch := by
  intro n _
  unfold TokenAvailAt
  exact SubstratumSource.genTheory_avail_conj fullClass_arch trivial (tokOp_isometry zPh_unitary n)

/-- **ON A FOURTH-ROOT LATTICE THE DRIVE FAILS**, by every protocol at every positive level (the
bridge's invariant and ray step). -/
theorem not_opDrive_of_quartLattice {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hL : QuartLattice 𝓘) : ¬ OpDrive 𝓘 arch :=
  fun h => not_tokenAvail_zPh_of_lattice arch hL Nat.one_pos (h 1 Nat.one_pos)

/-- The stated access. -/
theorem not_opDrive_perm : ¬ OpDrive permClass permClass_arch :=
  not_opDrive_of_quartLattice _ permClass_quartLattice

/-- The stated access with the quarter phase. -/
theorem not_opDrive_mixEmpty : ¬ OpDrive (MixR (∅ : Set ℝ)) (mixR_arch (∅ : Set ℝ)) :=
  not_opDrive_of_quartLattice _ mixEmpty_quartLattice

/-- The full model FM. -/
theorem not_opDrive_lattice : ¬ OpDrive latticeClass latticeClass_arch :=
  not_opDrive_of_quartLattice _ latticeClass_quartLattice

/-- `zPh ⊗ 1ₙ` is the diagonal with `1` at the configuration `0` and `w` at `1`. -/
theorem tokOp_zPh_eq_diagonal (n : ℕ) :
    tokOp zPh n
      = Matrix.diagonal (fun p : Fin 2 × Fin n => (![(1 : ℂ), w345] : Fin 2 → ℂ) p.1) := by
  ext ⟨b, k⟩ ⟨b', k'⟩
  simp only [tokOp, tensorOf_apply, zPh, Matrix.diagonal_apply, Matrix.one_apply, Prod.mk.injEq]
  by_cases hb : b = b' <;> by_cases hk : k = k' <;> simp [hb, hk]

theorem zPh_entry_star (b : Fin 2) :
    star ((![(1 : ℂ), w345] : Fin 2 → ℂ) b) * (![(1 : ℂ), w345] : Fin 2 → ℂ) b = 1 := by
  fin_cases b
  · first
    | (show star (1 : ℂ) * 1 = 1; rw [star_one, one_mul])
    | simp
  · first
    | (show star w345 * w345 = 1; exact w345_star_mul)
    | simp [w345_star_mul]

/-- **I4.60 SUPPLIES THE DRIVE**: a theory on the token carrying the substratum's availability has
the conjugation by `zPh ⊗ 1ₙ` at every level (`diagonal_avail`, LiftAudit.lean:754). -/
theorem tokenAvail_zPh_of_substratumAvail (T : FiniteOperationalTheory (Fin 2))
    (hsub : LiftAudit.SubstratumAvail T) (n : ℕ) :
    T.availExt n Unit (fun _ => conjChannel (tokOp zPh n)) := by
  rw [tokOp_zPh_eq_diagonal]
  exact LiftAudit.diagonal_avail T hsub n _ (fun p => zPh_entry_star p.1)

theorem opDrive_of_substratumAvail {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hsub : LiftAudit.SubstratumAvail (genTheory 𝓘 arch (Fin 2))) : OpDrive 𝓘 arch :=
  fun n _ => tokenAvail_zPh_of_substratumAvail _ hsub n

/-- **FM FAILS I4.60** (the coordinator's F1, in design): the lattice theory does not carry the
substratum's availability, since it lacks the drive. -/
theorem lattice_not_substratumAvail : ¬ LiftAudit.SubstratumAvail (latticeTheory (Fin 2)) :=
  fun h => not_opDrive_lattice (opDrive_of_substratumAvail latticeClass_arch h)

/-- **COMPOSITE UNITARY CONTROL ENTAILS THE DRIVE**: the drive is one of the unitaries control makes
available at every level. -/
theorem opDrive_of_control {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (h : HasCompositeUnitaryControl (genTheory 𝓘 arch (Fin 2))) : OpDrive 𝓘 arch :=
  fun n _ => h n _ (tokOp_isometry zPh_unitary n)

/-- **QUANTUM MECHANICS ENTAILS THE DRIVE**: in the exact reading the drive is a consequence of the
target, so no premise set reaching the target avoids it. -/
theorem opDrive_of_qm {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (h : LevelOneSeam.ExactAllFiniteEndomorphicQuantumOps (genTheory 𝓘 arch (Fin 2))) :
    OpDrive 𝓘 arch :=
  opDrive_of_control arch (PhysicalCharacterization.physical_of_exactAll _ h).2.2.1

end Drive

/-! ### §B — the phase intervention at θ₀ as a class: the lattice of `⟨i, w⟩` -/

section DriveClass

/-- Two nonzero entries lie on the lattice of `w`: their fourth powers agree up to powers of `w⁴`
(the fourth-root lattice `QuartEq` is the case of equal fourth powers). -/
def WLat {T : Type} (K : Matrix T T ℂ) : Prop :=
  ∀ i j k l, K i j ≠ 0 → K k l ≠ 0 →
    ∃ a b : ℕ, K i j ^ 4 * w345 ^ (4 * a) = K k l ^ 4 * w345 ^ (4 * b)

/-- **THE DRIVE CLASS**: the submonomial operators on the lattice of `w` — the stated access with the
phase intervention at the one angle θ₀. -/
abbrev driveClass : ImplementationClass := fun _ _ _ K => IsSubmonomial K ∧ WLat K

theorem wlat_of_quart {T : Type} {K : Matrix T T ℂ} (h : QuartEq K) : WLat K :=
  fun i j k l h1 h2 => ⟨0, 0, by rw [h i j k l h1 h2]⟩

theorem wl_mul {T : Type} [Fintype T] {K L : Matrix T T ℂ} (hKs : IsSubmonomial K) (hK : WLat K)
    (hL : WLat L) : WLat (K * L) := by
  intro i j k l h1 h2
  obtain ⟨m, hm1, hm2⟩ := mul_entry_ne_zero h1
  obtain ⟨m', hm1', hm2'⟩ := mul_entry_ne_zero h2
  obtain ⟨a, b, hab⟩ := hK i m k m' hm1 hm1'
  obtain ⟨a', b', hab'⟩ := hL m j m' l hm2 hm2'
  refine ⟨a + a', b + b', ?_⟩
  rw [submonomial_mul_apply hKs hm1, submonomial_mul_apply hKs hm1', mul_pow, mul_pow, mul_add,
    mul_add, pow_add, pow_add]
  linear_combination (L m j ^ 4 * w345 ^ (4 * a')) * hab + (K k m' ^ 4 * w345 ^ (4 * b)) * hab'

theorem wl_smul {T : Type} (c : ℂ) {K : Matrix T T ℂ} (hK : WLat K) : WLat (c • K) := by
  intro i j k l h1 h2
  simp only [Matrix.smul_apply, smul_eq_mul] at h1 h2 ⊢
  obtain ⟨a, b, hab⟩ := hK i j k l (mul_ne_zero_iff.mp h1).2 (mul_ne_zero_iff.mp h2).2
  exact ⟨a, b, by rw [mul_pow, mul_pow]; linear_combination c ^ 4 * hab⟩

theorem wl_block {T : Type} [Fintype T] [DecidableEq T] {m : ℕ}
    {K : Matrix (T × Fin m) (T × Fin m) ℂ} (hK : WLat K) (f e : Fin m) :
    WLat (AncillaClosure.ancBlock K f e) :=
  fun i j k l h1 h2 => hK (i, f) (j, e) (k, f) (l, e) h1 h2

theorem wl_reindex {T T' : Type} (e : T ≃ T') {K : Matrix T T ℂ} (hK : WLat K) :
    WLat (Matrix.reindex e e K) := by
  intro i j k l h1 h2
  simp only [Matrix.reindex_apply, Matrix.submatrix_apply] at h1 h2 ⊢
  exact hK _ _ _ _ h1 h2

theorem wl_conjTranspose {T : Type} {K : Matrix T T ℂ} (hK : WLat K) : WLat Kᴴ := by
  intro i j k l h1 h2
  simp only [Matrix.conjTranspose_apply] at h1 h2 ⊢
  obtain ⟨a, b, hab⟩ := hK j i l k (star_ne_zero.mp h1) (star_ne_zero.mp h2)
  have h' := congrArg star hab
  simp only [star_mul', star_pow] at h'
  have key : ∀ n : ℕ, star w345 ^ n * w345 ^ n = 1 := fun n => by
    rw [← mul_pow, w345_star_mul, one_pow]
  refine ⟨b, a, ?_⟩
  linear_combination (w345 ^ (4 * a) * w345 ^ (4 * b)) * h'
    - (star (K j i) ^ 4 * w345 ^ (4 * b)) * key (4 * a)
    + (star (K l k) ^ 4 * w345 ^ (4 * a)) * key (4 * b)

theorem wl_tensorOf {R S : Type} [Fintype R] [DecidableEq R] [Fintype S] [DecidableEq S]
    {A : Matrix R R ℂ} {B : Matrix S S ℂ} (hA : WLat A) (hB : WLat B) : WLat (tensorOf A B) := by
  intro p q p' q' h1 h2
  simp only [tensorOf_apply] at h1 h2 ⊢
  obtain ⟨h1a, h1b⟩ := mul_ne_zero_iff.mp h1
  obtain ⟨h2a, h2b⟩ := mul_ne_zero_iff.mp h2
  obtain ⟨a, b, hab⟩ := hA _ _ _ _ h1a h2a
  obtain ⟨a', b', hab'⟩ := hB _ _ _ _ h1b h2b
  refine ⟨a + a', b + b', ?_⟩
  rw [mul_pow, mul_pow, mul_add, mul_add, pow_add, pow_add]
  linear_combination (B p.2 q.2 ^ 4 * w345 ^ (4 * a')) * hab
    + (A p'.1 q'.1 ^ 4 * w345 ^ (4 * b)) * hab'

theorem wl_one {S : Type} [DecidableEq S] : WLat (1 : Matrix S S ℂ) :=
  wlat_of_quart (quart_of_ones one_entries_one)

/-- **(1) ARCHITECTURE.** -/
theorem driveClass_arch : Architecture driveClass where
  one := fun _ _ _ => ⟨submonomial_one, wl_one⟩
  mul := fun _ _ _ _ _ hK hL => ⟨submonomial_mul hK.1 hL.1, wl_mul hK.1 hK.2 hL.2⟩
  smul := fun _ _ _ a _ _ hK => ⟨submonomial_smul a hK.1, wl_smul a hK.2⟩
  proj := fun _ _ _ _ _ =>
    ⟨submonomial_diagonal _, wlat_of_quart (quart_of_scaled (scaled_diagonal_indicator _))⟩
  block := fun _ _ _ _ _ f e hK => ⟨submonomial_block hK.1 f e, wl_block hK.2 f e⟩

/-- **(2) CONTEXT STABILITY.** -/
theorem driveClass_contextStable : ContextStable driveClass :=
  fun _ _ _ _ _ _ _ hK => ⟨submonomial_tensor_one hK.1, wl_tensorOf wl_one hK.2⟩

/-- **(3) LABEL INVARIANCE.** -/
theorem driveClass_labelInvariant : LabelInvariant driveClass :=
  fun _ _ _ _ _ _ e _ hK => ⟨submonomial_reindex e hK.1, wl_reindex e hK.2⟩

/-- **(4) DAGGER STABILITY.** -/
theorem driveClass_daggerStable : DaggerStable driveClass :=
  fun _ _ _ _ hK => ⟨submonomial_conjTranspose hK.1, wl_conjTranspose hK.2⟩

/-- **UNITARY-RAY SATURATION**: both conditions are invariant under a nonzero rescaling. -/
theorem driveClass_unitaryRaySaturated : UnitaryRaySaturated driveClass := by
  intro S _ _ c V hc _ h
  have h1 := submonomial_smul c⁻¹ h.1
  have h2 := wl_smul c⁻¹ h.2
  rw [smul_smul, inv_mul_cancel₀ hc, one_smul] at h1 h2
  exact ⟨h1, h2⟩

theorem driveClass_structurallyClosed : StructurallyClosed driveClass :=
  ⟨driveClass_arch, driveClass_contextStable, driveClass_labelInvariant, driveClass_daggerStable⟩

/-- **CONFIGURATION LEVEL**: every member is monomial. -/
theorem driveClass_configurationLevel : ManuscriptAxioms.ConfigurationLevel driveClass :=
  fun _ _ _ _ h => submonomial_monomial h.1

/-- The fourth-root lattice lies in the drive class. -/
theorem lattice_le_drive :
    ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), latticeClass S K → driveClass S K :=
  fun _ _ _ _ h => ⟨h.1, wlat_of_quart h.2⟩

/-- The stated access lies in the drive class. -/
theorem permClass_le_drive :
    ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ), permClass S K → driveClass S K :=
  fun S _ _ K h => lattice_le_drive S K (permClass_le_lattice S K h)

/-- The drive class lies in the monomial interface. -/
theorem drive_le_substratum :
    ∀ (S : Type) [Fintype S] [DecidableEq S] (K : Matrix S S ℂ),
      driveClass S K → substratumClass S K :=
  fun _ _ _ _ h => submonomial_monomial h.1

/-- Every quarter phase lies in the drive class. -/
theorem phaseGate_drive {S : Type} [Fintype S] [DecidableEq S] (p : S) :
    driveClass S (LieRankSource.phaseGate p) :=
  lattice_le_drive S _ (phaseGate_lattice p)

/-- **THE DRIVE THEORY** on a carrier: the stated access with the phase intervention at θ₀. -/
noncomputable abbrev driveTheory (A : Type) [Fintype A] [DecidableEq A] :
    FiniteOperationalTheory A :=
  genTheory driveClass driveClass_arch A

/-- **`DerivedOI` ON EVERY CARRIER**, by the kernel's own derivation (as the bridge did for the
lattice). -/
theorem driveTheory_derivedOI (A : Type) [Fintype A] [DecidableEq A] : DerivedOI (driveTheory A) :=
  ⟨genTheory_reversibleImplementationLocality driveClass driveClass_arch
      driveClass_contextStable driveClass_labelInvariant driveClass_daggerStable,
    genTheory_embeddedObservation driveClass driveClass_arch driveClass_labelInvariant,
    fun _ a b => SubstratumSource.genTheory_avail_conj driveClass_arch
      (permClass_le_drive _ _ (permClass_permMatrix (Equiv.swap a b)))
      (SpectatorBridge.permMatrix_isometry _),
    fun _ a => SubstratumSource.genTheory_avail_conj driveClass_arch (phaseGate_drive a)
      (LieRankSource.phaseGate_unitary a),
    fun _ _ _ F l => by
      rw [ReadWriteControl.readWriteOperator_eq_perm]
      exact SubstratumSource.genTheory_avail_conj driveClass_arch
        (permClass_le_drive _ _ (permClass_permMatrix (F.couple l)))
        (SpectatorBridge.permMatrix_isometry _)⟩

/-- **INVERSE ACCESSIBILITY**: the reversible group of the drive theory is closed under inverse. -/
theorem driveTheory_inverseAccessibility (A : Type) [Fintype A] [DecidableEq A] [Nonempty A] :
    InverseAccessibility (driveTheory A) :=
  inverseAccessibility_of_generated_daggerStable driveClass_arch
    (genTheory_generated driveClass driveClass_arch) driveClass_daggerStable
    driveClass_unitaryRaySaturated

/-- A matrix every nonzero entry of which has fourth power a power of `w⁴` lies on the lattice. -/
theorem wlat_of_entries {T : Type} {K : Matrix T T ℂ}
    (h : ∀ i j, K i j ≠ 0 → ∃ a : ℕ, K i j ^ 4 = w345 ^ (4 * a)) : WLat K := by
  intro i j k l h1 h2
  obtain ⟨a, ha⟩ := h i j h1
  obtain ⟨b, hb⟩ := h k l h2
  exact ⟨b, a, by rw [ha, hb, mul_comm]⟩

/-- The nonzero entries of the drive's operator are `1 = w⁰` and `w`. -/
theorem zPh_entries (i j : Fin 2) (h : zPh i j ≠ 0) : ∃ a : ℕ, zPh i j ^ 4 = w345 ^ (4 * a) := by
  fin_cases i <;> fin_cases j
  · exact ⟨0, by simp [zPh]⟩
  · exact (h (by simp [zPh])).elim
  · exact (h (by simp [zPh])).elim
  · exact ⟨1, by simp [zPh]⟩

theorem zPh_wlat : WLat zPh :=
  wlat_of_entries zPh_entries

theorem tokOp_zPh_drive (n : ℕ) : driveClass (Fin 2 × Fin n) (tokOp zPh n) := by
  unfold tokOp
  exact ⟨submonomial_tensorOf zPh_sub submonomial_one, wl_tensorOf zPh_wlat wl_one⟩

/-- **THE DRIVE CLASS HAS THE DRIVE**, as one step at every level. -/
theorem opDrive_drive : OpDrive driveClass driveClass_arch := by
  intro n _
  unfold TokenAvailAt
  exact SubstratumSource.genTheory_avail_conj driveClass_arch (tokOp_zPh_drive n)
    (tokOp_isometry zPh_unitary n)

/-- **AND NO `J`**: at every positive level, by every protocol. -/
theorem drive_not_uJ {n : ℕ} (hn : 0 < n) : ¬ TokenAvailAt driveClass driveClass_arch uJ n :=
  not_tokenAvail_uJ_of_submonomial driveClass_arch (fun _ _ _ _ h => h.1) hn

theorem rot_apply_01 (θ : ℝ) : StateMixingCoupling.rot θ 0 1 = -(Real.sin θ : ℂ) := rfl

/-- **IN A SUBMONOMIAL CLASS NO MIXER IS AVAILABLE**: the fixed gate at any angle in `(0, π/2)` has
two nonzero entries in its first row, so no multiple of its token operator is submonomial. -/
theorem not_tokenAvail_rot_of_submonomial {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hS : ∀ (T : Type) [Fintype T] [DecidableEq T] (K : Matrix T T ℂ), 𝓘 T K → IsSubmonomial K)
    {θ : ℝ} (hθ : θ ∈ Set.Ioo (0 : ℝ) (Real.pi / 2)) {n : ℕ} (hn : 0 < n) :
    ¬ TokenAvailAt 𝓘 arch (StateMixingCoupling.rot θ) n := by
  intro h
  haveI : Nonempty (Fin 2 × Fin n) := ⟨(0, ⟨0, hn⟩)⟩
  have h' : InstAvail 𝓘 (Fin 2 × Fin n) Unit
      (fun _ => conjChannel (tokOp (StateMixingCoupling.rot θ) n)) := h
  obtain ⟨a, ha, hmem⟩ := exists_scaled_mem_of_instAvail_unitary arch h'
  have hc : (Real.cos θ : ℂ) ≠ 0 := by
    exact_mod_cast (Real.cos_pos_of_mem_Ioo ⟨by linarith [hθ.1, Real.pi_pos], hθ.2⟩).ne'
  have hs : -(Real.sin θ : ℂ) ≠ 0 := by
    rw [neg_ne_zero]
    exact_mod_cast (Real.sin_pos_of_pos_of_lt_pi hθ.1 (by linarith [hθ.2, Real.pi_pos])).ne'
  have hne : ((0 : Fin 2), (⟨0, hn⟩ : Fin n)) ≠ ((1 : Fin 2), (⟨0, hn⟩ : Fin n)) := by
    intro hc'
    have h01 : (0 : Fin 2) = 1 := congrArg Prod.fst hc'
    exact absurd h01 (by decide)
  exact not_submonomial_smul (p := ((0 : Fin 2), (⟨0, hn⟩ : Fin n))) hne
    (by rw [tokOp_apply_same, StateMixingCoupling.rot_apply_00]; exact hc)
    (by rw [tokOp_apply_same, rot_apply_01]; exact hs)
    ha (hS _ _ hmem)

/-- The drive class supplies no mixer: the fixed gate at any angle in `(0, π/2)` is unavailable at
every positive level. -/
theorem drive_not_rot {θ : ℝ} (hθ : θ ∈ Set.Ioo (0 : ℝ) (Real.pi / 2)) {n : ℕ} (hn : 0 < n) :
    ¬ TokenAvailAt driveClass driveClass_arch (StateMixingCoupling.rot θ) n :=
  not_tokenAvail_rot_of_submonomial driveClass_arch (fun _ _ _ _ h => h.1) hθ hn

theorem driveTheory_closure (A : Type) [Fintype A] [DecidableEq A] :
    AncillaClosure.IteratedAncillaClosure (driveTheory A) :=
  PrimitiveSource.closure_of_embeddedObservation
    (genTheory_embeddedObservation driveClass driveClass_arch driveClass_labelInvariant)

/-- **THE DRIVE THEORY HAS NO COMPOSITE UNITARY CONTROL** on the token: `J` is not available. -/
theorem driveTheory_token_not_control : ¬ HasCompositeUnitaryControl (driveTheory (Fin 2)) :=
  fun h => drive_not_uJ Nat.one_pos (h 1 _ (tokOp_isometry uJ_unitary 1))

/-- **AND IS NOT QUANTUM MECHANICS.** -/
theorem driveTheory_not_qm :
    ¬ LevelOneSeam.ExactAllFiniteEndomorphicQuantumOps (driveTheory (Fin 2)) :=
  fun h => driveTheory_token_not_control (PhysicalCharacterization.physical_of_exactAll _ h).2.2.1

theorem driveTheory_not_phaseFree : ¬ MinimalRepertoire.PhaseFreeRichness (driveTheory (Fin 2)) :=
  fun h => driveTheory_token_not_control
    (MinimalRepertoire.control_of_phaseFree _ (driveTheory_closure (Fin 2)) h)

theorem driveTheory_not_layerFlowExecutable {S : Type} [Fintype S] [DecidableEq S]
    {σ : Equiv.Perm S} {x : S} (hx : σ x ≠ x) :
    ¬ LiftAudit.LayerFlowExecutable (driveTheory S) σ :=
  LiftAudit.configurationLevel_not_layerFlowExecutable driveClass_arch
    driveClass_configurationLevel hx

end DriveClass

/-! ### §C — the reversible group of a class at a carrier -/

section Reversible

variable {T : Type} [Fintype T] [DecidableEq T]

/-- **THE REVERSIBLE GROUP OF A UNITARY-RAY-SATURATED CLASS IS ITS SET OF UNITARIES**: a unitary
conjugation is available at the carrier by some protocol — ancillas, readouts, feed-forward,
discard and relabellings included — exactly when a nonzero multiple of the unitary is a member of
the class there (the kernel's ray step, and `op`). The `InstAvail` closure adds no unitary
conjugation beyond the class. -/
theorem avail_unitary_iff {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hs : UnitaryRaySaturated 𝓘) [Nonempty T] {V : Matrix T T ℂ} (hV : Vᴴ * V = 1) :
    InstAvail 𝓘 T Unit (fun _ => conjChannel V) ↔ ∃ c : ℂ, c ≠ 0 ∧ 𝓘 T (c • V) := by
  constructor
  · intro h
    exact exists_scaled_mem_of_instAvail_unitary arch h
  · rintro ⟨c, hc, hmem⟩
    exact InstAvail.op V (hs T c V hc hV hmem) hV

/-- The lattice theory's reversible group at every carrier: the unitaries some nonzero multiple of
which is a fourth-root monomial. -/
theorem lattice_avail_iff [Nonempty T] {V : Matrix T T ℂ} (hV : Vᴴ * V = 1) :
    InstAvail latticeClass T Unit (fun _ => conjChannel V)
      ↔ ∃ c : ℂ, c ≠ 0 ∧ IsSubmonomial (c • V) ∧ QuartEq (c • V) :=
  avail_unitary_iff latticeClass_arch latticeClass_unitaryRaySaturated hV

/-- The drive theory's reversible group at every carrier: the unitaries some nonzero multiple of
which is a monomial on the lattice of `w`. -/
theorem drive_avail_iff [Nonempty T] {V : Matrix T T ℂ} (hV : Vᴴ * V = 1) :
    InstAvail driveClass T Unit (fun _ => conjChannel V)
      ↔ ∃ c : ℂ, c ≠ 0 ∧ IsSubmonomial (c • V) ∧ WLat (c • V) :=
  avail_unitary_iff driveClass_arch driveClass_unitaryRaySaturated hV

/-- **IN A SUBMONOMIAL CLASS EVERY AVAILABLE UNITARY IS A MULTIPLE OF A MONOMIAL**, whatever the
protocol. -/
theorem avail_monomial_of_submonomial {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hsub : ∀ K : Matrix T T ℂ, 𝓘 T K → IsSubmonomial K) [Nonempty T] {V : Matrix T T ℂ}
    (h : InstAvail 𝓘 T Unit (fun _ => conjChannel V)) :
    ∃ c : ℂ, c ≠ 0 ∧ IsMonomial (c • V) := by
  obtain ⟨c, hc, hmem⟩ := exists_scaled_mem_of_instAvail_unitary arch h
  exact ⟨c, hc, submonomial_monomial (hsub _ hmem)⟩

end Reversible

/-! ### §C′ — no density in a submonomial class: the closure of its reversible group is monomial -/

section NoDensity

theorem rotQuarter_apply_00 :
    tokOp (StateMixingCoupling.rot (Real.pi / 4)) 1 ((0 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1))
      = ((Real.sqrt 2 / 2 : ℝ) : ℂ) := by
  rw [tokOp_apply_same, StateMixingCoupling.rot_apply_00, Real.cos_pi_div_four]

theorem rotQuarter_apply_10 :
    tokOp (StateMixingCoupling.rot (Real.pi / 4)) 1 ((1 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1))
      = ((Real.sqrt 2 / 2 : ℝ) : ℂ) := by
  rw [tokOp_apply_same, StateMixingCoupling.rot_apply_10, Real.sin_pi_div_four]

theorem norm_sqrt_two_div_two : ‖((Real.sqrt 2 / 2 : ℝ) : ℂ)‖ = Real.sqrt 2 / 2 := by
  rw [Complex.norm_real, Real.norm_of_nonneg (by positivity)]

theorem half_lt_sqrt_two_div_two : (1 / 2 : ℝ) < Real.sqrt 2 / 2 := by
  have h2 := Real.sq_sqrt (show (0 : ℝ) ≤ 2 by norm_num)
  nlinarith [Real.sqrt_nonneg 2]

/-- **IN A SUBMONOMIAL CLASS THE LEVEL-ONE CLAUSE OF `DenseUnitaryControl` FAILS**: every available
unitary is a multiple of a submonomial matrix (the ray step), so one of the two entries of its first
column vanishes, and there the balanced mixer differs from it by `√2/2`, an entry of the difference,
bounded by its operator norm. The closure of the reversible group at level one is not dense. -/
theorem not_levelOneClause_of_submonomial {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hS : ∀ (T : Type) [Fintype T] [DecidableEq T] (K : Matrix T T ℂ), 𝓘 T K → IsSubmonomial K) :
    ¬ OriginAngle.LevelOneClause (genTheory 𝓘 arch (Fin 2)) := by
  intro h
  obtain ⟨V, c, -, -, hav, hlt⟩ :=
    h _ (tokOp_isometry (DiscreteCompletion.rot_unitary (Real.pi / 4)) 1) (1 / 2) (by norm_num)
  haveI : Nonempty (Fin 2 × Fin 1) := ⟨((0 : Fin 2), (0 : Fin 1))⟩
  have hav' : InstAvail 𝓘 (Fin 2 × Fin 1) Unit (fun _ => conjChannel V) := hav
  obtain ⟨a, ha, hmem⟩ := exists_scaled_mem_of_instAvail_unitary arch hav'
  have hsub := hS _ _ hmem
  have key : V ((0 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1)) = 0
      ∨ V ((1 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1)) = 0 := by
    by_contra hne
    push Not at hne
    have h1 : (a • V) ((0 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1)) ≠ 0 := by
      rw [Matrix.smul_apply, smul_eq_mul]
      exact mul_ne_zero ha hne.1
    have h2 : (a • V) ((1 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1)) ≠ 0 := by
      rw [Matrix.smul_apply, smul_eq_mul]
      exact mul_ne_zero ha hne.2
    have h3 := hsub.2 _ _ _ h1 h2
    have h4 : (0 : Fin 2) = 1 := congrArg Prod.fst h3
    exact absurd h4 (by decide)
  have hbig : Real.sqrt 2 / 2
      ≤ ‖tokOp (StateMixingCoupling.rot (Real.pi / 4)) 1 - c • V‖ := by
    rcases key with h0 | h0
    · have e := FrozenSourcing.norm_entry_le_l2_opNorm
        (tokOp (StateMixingCoupling.rot (Real.pi / 4)) 1 - c • V)
        ((0 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1))
      rw [Matrix.sub_apply, Matrix.smul_apply, h0, smul_zero, sub_zero, rotQuarter_apply_00,
        norm_sqrt_two_div_two] at e
      exact e
    · have e := FrozenSourcing.norm_entry_le_l2_opNorm
        (tokOp (StateMixingCoupling.rot (Real.pi / 4)) 1 - c • V)
        ((1 : Fin 2), (0 : Fin 1)) ((0 : Fin 2), (0 : Fin 1))
      rw [Matrix.sub_apply, Matrix.smul_apply, h0, smul_zero, sub_zero, rotQuarter_apply_10,
        norm_sqrt_two_div_two] at e
      exact e
  linarith [half_lt_sqrt_two_div_two]

/-- The drive class: the phase intervention at θ₀ gives no dense control at level one. -/
theorem drive_not_levelOneClause : ¬ OriginAngle.LevelOneClause (driveTheory (Fin 2)) :=
  not_levelOneClause_of_submonomial driveClass_arch (fun _ _ _ _ h => h.1)

/-- FM: the fourth-root lattice gives none. -/
theorem lattice_not_levelOneClause : ¬ OriginAngle.LevelOneClause (latticeTheory (Fin 2)) :=
  not_levelOneClause_of_submonomial latticeClass_arch (fun _ _ _ _ h => h.1)

/-- **THE MONOMIAL INTERFACE — THE PHASE INTERVENTION AT EVERY ANGLE — GIVES NO DENSE CONTROL.** -/
theorem substratum_not_levelOneClause : ¬ OriginAngle.LevelOneClause (substratumTheory (Fin 2)) :=
  not_levelOneClause_of_submonomial substratumClass_arch (fun _ _ _ _ h => monomial_submonomial h)

theorem substratum_not_denseUnitaryControl : ¬ DenseUnitaryControl (substratumTheory (Fin 2)) :=
  fun h => substratum_not_levelOneClause (OriginAngle.levelOneClause_of_dense h)

theorem drive_not_denseUnitaryControl : ¬ DenseUnitaryControl (driveTheory (Fin 2)) :=
  fun h => drive_not_levelOneClause (OriginAngle.levelOneClause_of_dense h)

end NoDensity

/-! ### §D — the drive is the identity on every monomial token body -/

section Body

variable {T : Type} [Fintype T] [DecidableEq T]

theorem diagonal_fixes_diag (d : T → ℂ) (hd : ∀ p, star (d p) * d p = 1) {X : Matrix T T ℂ}
    (hX : X ∈ Diag) : Matrix.diagonal d * X * (Matrix.diagonal d)ᴴ = X := by
  ext p q
  rw [Matrix.diagonal_conjTranspose, Matrix.mul_diagonal, Matrix.diagonal_mul, Pi.star_apply]
  by_cases hpq : p = q
  · rw [← hpq]
    linear_combination X p p * hd p
  · rw [hX p q hpq, mul_zero, zero_mul]

/-- **A DIAGONAL UNITARY IS THE IDENTITY ON THE TOKEN BODY OF EVERY SUBMONOMIAL CLASS.** -/
theorem diagonal_trivial_on_body {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hsub : ∀ K : Matrix T T ℂ, 𝓘 T K → IsSubmonomial K) (d : T → ℂ)
    (hd : ∀ p, star (d p) * d p = 1) :
    ∀ X ∈ body 𝓘 T, conjChannel (Matrix.diagonal d) X = X := fun X hX => by
  rw [AncillaClosure.conjChannel_apply]
  exact diagonal_fixes_diag d hd (body_subset_diag (reach_diag_of_submonomial arch hsub) hX)

theorem drive_reach_diag : Reach driveClass T ⊆ Diag :=
  reach_diag_of_submonomial driveClass_arch (fun _ h => h.1)

theorem lattice_reach_diag : Reach latticeClass T ⊆ Diag :=
  reach_diag_of_submonomial latticeClass_arch (fun _ h => h.1)

/-- **THE DRIVE FIXES EVERY STATE OF THE DRIVE THEORY'S TOKEN BODY**, at every level. -/
theorem zPh_trivial_on_drive_body (n : ℕ) :
    ∀ X ∈ body driveClass (Fin 2 × Fin n), conjChannel (tokOp zPh n) X = X := by
  rw [tokOp_zPh_eq_diagonal]
  exact diagonal_trivial_on_body driveClass_arch (fun _ h => h.1) _ (fun p => zPh_entry_star p.1)

/-- **AND OF THE MONOMIAL INTERFACE'S**: the phase intervention at every angle has the same empty
content on its token body. -/
theorem zPh_trivial_on_substratum_body (n : ℕ) :
    ∀ X ∈ body substratumClass (Fin 2 × Fin n), conjChannel (tokOp zPh n) X = X := by
  rw [tokOp_zPh_eq_diagonal]
  exact diagonal_trivial_on_body substratumClass_arch (fun _ h => monomial_submonomial h) _
    (fun p => zPh_entry_star p.1)

/-- The drive class carries no datum of infinite order on its token body. -/
theorem drive_not_ordInf :
    ¬ CompositionOrder.OrdInf (body driveClass T) (availData driveClass T) :=
  not_ordInf_of_reach_diag drive_reach_diag

/-- FM carries no datum of infinite order on its token body. -/
theorem lattice_not_ordInf :
    ¬ CompositionOrder.OrdInf (body latticeClass T) (availData latticeClass T) :=
  not_ordInf_of_reach_diag lattice_reach_diag

/-- At every level, in the lattice theory every available unitary datum has finite order on the
token body. -/
theorem latticeTheory_datum_finiteOrderOn (n : ℕ)
    {U : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ} (hU : Uᴴ * U = 1)
    (hav : (latticeTheory (Fin 2)).availExt n Unit (fun _ => conjChannel U)) :
    CompositionOrder.FiniteOrderOn (body latticeClass (Fin 2 × Fin n)) (conjAff U hU) :=
  finiteOrderOn_of_reach_diag lattice_reach_diag hU hav

end Body

/-! ### §E — the reversible group of the stated access: finite up to scalar, not merely torsion -/

section RootLattice

variable {T : Type} [Fintype T] [DecidableEq T]

/-- Any two nonzero entries have equal `N`-th powers (`QuartEq` is `N = 4`). -/
def RootLat (N : ℕ) (K : Matrix T T ℂ) : Prop :=
  ∀ i j k l, K i j ≠ 0 → K k l ≠ 0 → K i j ^ N = K k l ^ N

theorem rootLat_four_of_quart {K : Matrix T T ℂ} (h : QuartEq K) : RootLat 4 K := h

theorem pow_unitary {U : Matrix T T ℂ} (hU : Uᴴ * U = 1) : ∀ k : ℕ, (U ^ k)ᴴ * U ^ k = 1
  | 0 => by rw [pow_zero, Matrix.conjTranspose_one, Matrix.one_mul]
  | k + 1 => by
    rw [pow_succ, Matrix.conjTranspose_mul]
    calc Uᴴ * (U ^ k)ᴴ * (U ^ k * U) = Uᴴ * ((U ^ k)ᴴ * U ^ k) * U := by
          simp only [Matrix.mul_assoc]
      _ = 1 := by rw [pow_unitary hU k, Matrix.mul_one, hU]

/-- Powers of a submonomial matrix with entries in `{0} ∪ μ_N` are submonomial with entries in
`{0} ∪ μ_N`. -/
theorem pow_rootEntries {N : ℕ} {M : Matrix T T ℂ} (hMs : IsSubmonomial M)
    (hMe : ∀ i j, M i j = 0 ∨ M i j ^ N = 1) :
    ∀ k : ℕ, IsSubmonomial (M ^ k) ∧ ∀ i j, (M ^ k) i j = 0 ∨ (M ^ k) i j ^ N = 1
  | 0 => by
    refine ⟨by rw [pow_zero]; exact submonomial_one, fun i j => ?_⟩
    rw [pow_zero, Matrix.one_apply]
    by_cases h : i = j
    · right
      rw [if_pos h, one_pow]
    · left
      rw [if_neg h]
  | k + 1 => by
    obtain ⟨hs, he⟩ := pow_rootEntries hMs hMe k
    rw [pow_succ]
    refine ⟨submonomial_mul hs hMs, fun i j => ?_⟩
    by_cases h : (M ^ k * M) i j = 0
    · left
      exact h
    · right
      obtain ⟨m, hm1, hm2⟩ := mul_entry_ne_zero h
      rw [submonomial_mul_apply hs hm1, mul_pow]
      rcases he i m with h0 | h1
      · exact absurd h0 hm1
      rcases hMe m j with h0' | h1'
      · exact absurd h0' hm2
      rw [h1, h1', one_mul]

/-- The entries `{0} ∪ μ_N`. -/
noncomputable def rootSet (N : ℕ) : Finset ℂ :=
  insert (0 : ℂ) (Polynomial.nthRootsFinset N (1 : ℂ))

theorem mem_rootSet {N : ℕ} (hN : 0 < N) {x : ℂ} (h : x = 0 ∨ x ^ N = 1) : x ∈ rootSet N := by
  unfold rootSet
  rw [Finset.mem_insert]
  rcases h with h | h
  · exact Or.inl h
  · exact Or.inr ((Polynomial.mem_nthRootsFinset hN (1 : ℂ)).mpr h)

/-- The entry functions of the matrices with entries in `{0} ∪ μ_N`: a finite set. -/
noncomputable def rootMats (N : ℕ) : Finset (T → T → ℂ) :=
  Fintype.piFinset fun _ : T => Fintype.piFinset fun _ : T => rootSet N

/-- **PIGEONHOLE**: two powers of such a matrix coincide. -/
theorem exists_pow_eq_of_rootEntries {N : ℕ} (hN : 0 < N) {M : Matrix T T ℂ}
    (hMs : IsSubmonomial M) (hMe : ∀ i j, M i j = 0 ∨ M i j ^ N = 1) :
    ∃ i j : ℕ, i ≠ j ∧ M ^ i = M ^ j := by
  have hmem : ∀ k : ℕ, Matrix.of.symm (M ^ k) ∈ rootMats (T := T) N := by
    intro k
    unfold rootMats
    rw [Fintype.mem_piFinset]
    intro i
    rw [Fintype.mem_piFinset]
    intro j
    rw [Matrix.of_symm_apply]
    exact mem_rootSet hN ((pow_rootEntries hMs hMe k).2 i j)
  obtain ⟨i, j, hij, hf⟩ := Finite.exists_ne_map_eq_of_infinite
    (fun k : ℕ => (⟨Matrix.of.symm (M ^ k), hmem k⟩ : rootMats (T := T) N))
  exact ⟨i, j, hij, Matrix.of.symm.injective (congrArg Subtype.val hf)⟩

/-- Two powers proportional to one matrix: their quotient power is a scalar (the carrier-general
form of `OriginAngle.pow_scalar_of_eq`). -/
theorem pow_scalar_of_eq' [Nonempty T] {W : Matrix T T ℂ} {i j : ℕ} (hij : i < j)
    (hu : (W ^ i)ᴴ * W ^ i = 1) {ci cj : ℂ} {M : Matrix T T ℂ}
    (hi : W ^ i = ci • M) (hj : W ^ j = cj • M) :
    ∃ c : ℂ, W ^ (j - i) = c • (1 : Matrix T T ℂ) := by
  have hu' : W ^ i * (W ^ i)ᴴ = 1 := mul_eq_one_comm.mp hu
  have hci : ci ≠ 0 := by
    rintro rfl
    rw [zero_smul] at hi
    rw [hi, Matrix.mul_zero] at hu
    exact zero_ne_one hu
  refine ⟨cj * ci⁻¹, ?_⟩
  have hM : M = ci⁻¹ • W ^ i := by rw [hi, smul_smul, inv_mul_cancel₀ hci, one_smul]
  have key : W ^ (j - i) * W ^ i = (cj * ci⁻¹) • W ^ i := by
    rw [← pow_add, Nat.sub_add_cancel hij.le, hj, hM, smul_smul]
  calc W ^ (j - i) = W ^ (j - i) * (W ^ i * (W ^ i)ᴴ) := by rw [hu', Matrix.mul_one]
    _ = (W ^ (j - i) * W ^ i) * (W ^ i)ᴴ := by rw [Matrix.mul_assoc]
    _ = ((cj * ci⁻¹) • W ^ i) * (W ^ i)ᴴ := by rw [key]
    _ = (cj * ci⁻¹) • (W ^ i * (W ^ i)ᴴ) := by rw [Matrix.smul_mul]
    _ = (cj * ci⁻¹) • (1 : Matrix T T ℂ) := by rw [hu']

/-- **NORMALIZATION**: a unitary some nonzero multiple of which is submonomial on a root lattice has
a nonzero multiple that is submonomial with every entry in `{0} ∪ μ_N` (divide by one nonzero
entry). -/
theorem rootLat_normalize [Nonempty T] {N : ℕ} {U : Matrix T T ℂ} (hU : Uᴴ * U = 1) {c : ℂ}
    (hc : c ≠ 0) (hs : IsSubmonomial (c • U)) (hr : RootLat N (c • U)) :
    ∃ l : ℂ, l ≠ 0 ∧ IsSubmonomial (l • U) ∧ ∀ i j, (l • U) i j = 0 ∨ (l • U) i j ^ N = 1 := by
  classical
  obtain ⟨i₀, j₀, h0⟩ : ∃ i j, (c • U) i j ≠ 0 := by
    by_contra hall
    push Not at hall
    have hz : c • U = 0 := by
      ext i j
      exact hall i j
    have hU0 : U = 0 := by
      have h' := congrArg (fun X : Matrix T T ℂ => c⁻¹ • X) hz
      simp only [smul_smul, inv_mul_cancel₀ hc, one_smul, smul_zero] at h'
      exact h'
    rw [hU0, Matrix.mul_zero] at hU
    exact zero_ne_one hU
  refine ⟨((c • U) i₀ j₀)⁻¹ * c, mul_ne_zero (inv_ne_zero h0) hc, ?_, ?_⟩
  · rw [← smul_smul]
    exact submonomial_smul _ hs
  · intro i j
    rw [← smul_smul, Matrix.smul_apply, smul_eq_mul]
    by_cases h : (c • U) i j = 0
    · left
      rw [h, mul_zero]
    · right
      rw [mul_pow, hr i j i₀ j₀ h h0, inv_pow, inv_mul_cancel₀ (pow_ne_zero _ h0)]

/-- **A UNITARY WHOSE SCALAR MULTIPLE IS SUBMONOMIAL ON A ROOT LATTICE HAS A SCALAR POWER**: after the
normalization its powers range over a finite set of matrices, two coincide, and the quotient power
is a scalar. -/
theorem rootLat_pow_scalar [Nonempty T] {N : ℕ} (hN : 0 < N) {U : Matrix T T ℂ}
    (hU : Uᴴ * U = 1) {c : ℂ} (hc : c ≠ 0) (hs : IsSubmonomial (c • U))
    (hr : RootLat N (c • U)) :
    ∃ m : ℕ, 0 < m ∧ ∃ μ : ℂ, U ^ m = μ • (1 : Matrix T T ℂ) := by
  obtain ⟨l, hl, hMs, hMe⟩ := rootLat_normalize hU hc hs hr
  obtain ⟨i, j, hij, hpow⟩ := exists_pow_eq_of_rootEntries hN hMs hMe
  have hUk : ∀ k : ℕ, U ^ k = (l ^ k)⁻¹ • (l • U) ^ k := by
    intro k
    rw [smul_pow, smul_smul, inv_mul_cancel₀ (pow_ne_zero _ hl), one_smul]
  rcases lt_or_gt_of_ne hij with hlt | hlt
  · have hj' : U ^ j = (l ^ j)⁻¹ • (l • U) ^ i := by
      rw [hUk j, hpow]
    obtain ⟨μ, hμ⟩ := pow_scalar_of_eq' hlt (pow_unitary hU i) (hUk i) hj'
    exact ⟨j - i, Nat.sub_pos_of_lt hlt, μ, hμ⟩
  · have hi' : U ^ i = (l ^ i)⁻¹ • (l • U) ^ j := by
      rw [hUk i, ← hpow]
    obtain ⟨μ, hμ⟩ := pow_scalar_of_eq' hlt (pow_unitary hU j) (hUk j) hi'
    exact ⟨i - j, Nat.sub_pos_of_lt hlt, μ, hμ⟩

/-- **THE LATTICE'S REVERSIBLE GROUP IS FINITE UP TO SCALAR** at every carrier: every available
unitary — by every protocol, ancillas and relabellings included — is a nonzero multiple of a matrix
with entries in `{0} ∪ μ₄`, a finite set fixed by the carrier. -/
theorem lattice_avail_finite_upToScalar [Nonempty T] {V : Matrix T T ℂ} (hV : Vᴴ * V = 1)
    (hav : InstAvail latticeClass T Unit (fun _ => conjChannel V)) :
    ∃ (b : ℂ) (M : Matrix T T ℂ), b ≠ 0 ∧ Matrix.of.symm M ∈ rootMats (T := T) 4 ∧ V = b • M := by
  obtain ⟨c, hc, hs, hq⟩ := (lattice_avail_iff hV).mp hav
  obtain ⟨l, hl, -, hle⟩ := rootLat_normalize hV hc hs (rootLat_four_of_quart hq)
  refine ⟨l⁻¹, l • V, inv_ne_zero hl, ?_, ?_⟩
  · unfold rootMats
    rw [Fintype.mem_piFinset]
    intro i
    rw [Fintype.mem_piFinset]
    intro j
    rw [Matrix.of_symm_apply]
    exact mem_rootSet (by norm_num) (hle i j)
  · rw [smul_smul, inv_mul_cancel₀ hl, one_smul]

/-- **THE STATED ACCESS WITH THE QUARTER PHASE (`MixR ∅`)**: the same, through the inclusion of its
class in the lattice and the monotonicity of availability. -/
theorem mixEmpty_avail_finite_upToScalar [Nonempty T] {V : Matrix T T ℂ} (hV : Vᴴ * V = 1)
    (hav : InstAvail (MixR (∅ : Set ℝ)) T Unit (fun _ => conjChannel V)) :
    ∃ (b : ℂ) (M : Matrix T T ℂ), b ≠ 0 ∧ Matrix.of.symm M ∈ rootMats (T := T) 4 ∧ V = b • M :=
  lattice_avail_finite_upToScalar hV (instAvail_mono mixEmpty_le_lattice hav)

/-- **THE STATED ACCESS'S REVERSIBLE GROUP, ON THE FULL MATRIX ALGEBRA**: in the lattice theory every
available unitary has a scalar power — the whole reversible group, every composition included, at
every carrier. -/
theorem lattice_pow_scalar [Nonempty T] {U : Matrix T T ℂ} (hU : Uᴴ * U = 1)
    (hav : InstAvail latticeClass T Unit (fun _ => conjChannel U)) :
    ∃ m : ℕ, 0 < m ∧ ∃ μ : ℂ, U ^ m = μ • (1 : Matrix T T ℂ) := by
  obtain ⟨c, hc, hs, hq⟩ := (lattice_avail_iff hU).mp hav
  exact rootLat_pow_scalar (by norm_num : 0 < 4) hU hc hs (rootLat_four_of_quart hq)

/-- A scalar power of a unitary fixes every matrix under the iterated conjugation. -/
theorem conjAff_iterate_scalar [Nonempty T] {U : Matrix T T ℂ} (hU : Uᴴ * U = 1) {m : ℕ} {μ : ℂ}
    (h : U ^ m = μ • (1 : Matrix T T ℂ)) (X : Matrix T T ℂ) :
    (⇑(conjAff U hU))^[m] X = X := by
  have hμ : star μ * μ = 1 := by
    have h1 := pow_unitary hU m
    simp only [h, Matrix.conjTranspose_smul, Matrix.conjTranspose_one, Matrix.smul_mul,
      Matrix.mul_smul, Matrix.one_mul, Matrix.mul_one, smul_smul] at h1
    have h2 := congrFun (congrFun h1 (Classical.arbitrary T)) (Classical.arbitrary T)
    simp only [Matrix.smul_apply, Matrix.one_apply_eq, smul_eq_mul, mul_one] at h2
    linear_combination h2
  have hμ' : μ * star μ = 1 := by rw [mul_comm]; exact hμ
  rw [conjAff_iterate, h]
  simp only [Matrix.conjTranspose_smul, Matrix.conjTranspose_one, Matrix.smul_mul,
    Matrix.mul_smul, Matrix.one_mul, Matrix.mul_one, smul_smul, hμ, hμ', one_smul]

/-- In the lattice theory every available unitary datum has finite order on the full matrix
algebra. -/
theorem lattice_finiteOrderOn_univ [Nonempty T] {U : Matrix T T ℂ} (hU : Uᴴ * U = 1)
    (hav : InstAvail latticeClass T Unit (fun _ => conjChannel U)) :
    CompositionOrder.FiniteOrderOn (Set.univ : Set (Matrix T T ℂ)) (conjAff U hU) := by
  obtain ⟨m, hm, μ, hμ⟩ := lattice_pow_scalar hU hav
  exact ⟨m, by omega, fun X _ => conjAff_iterate_scalar hU hμ X⟩

theorem lattice_not_infiniteOrderOn_univ [Nonempty T] {U : Matrix T T ℂ} (hU : Uᴴ * U = 1)
    (hav : InstAvail latticeClass T Unit (fun _ => conjChannel U)) :
    ¬ CompositionOrder.InfiniteOrderOn (Set.univ : Set (Matrix T T ℂ)) (conjAff U hU) :=
  CompositionOrder.not_infiniteOrderOn_of_finiteOrderOn (lattice_finiteOrderOn_univ hU hav)

end RootLattice

/-! ### §F — the non-torsion phase: `w` is no root of unity; `θ₀`; the kernel's density at `θ₀` -/

section Phase

/-- The ring map `ℤ[i] → ℤ/5`, `i ↦ 2`. -/
noncomputable def phi5 : GaussianInt →+* ZMod 5 :=
  Zsqrtd.lift ⟨(2 : ZMod 5), by
    first
    | decide
    | rfl
    | (push_cast; decide)
    | (norm_num; decide)⟩

theorem phi5_three_four : phi5 ⟨3, 4⟩ = 1 := by
  first
  | decide
  | rfl
  | (simp only [phi5, Zsqrtd.lift_apply_apply]; decide)
  | (simp [phi5]; done)
  | (simp [phi5]; decide)
  | (norm_num [phi5]; done)
  | (norm_num [phi5]; decide)

theorem phi5_five : phi5 5 = 0 := by
  rw [map_ofNat]
  first
  | decide
  | rfl
  | (simp; done)
  | (simp; decide)

theorem w345_eq_div : w345 = ((⟨3, 4⟩ : GaussianInt) : ℂ) / 5 := by
  rw [GaussianInt.toComplex_def']
  unfold w345
  push_cast
  ring

/-- **`w` IS NO ROOT OF UNITY**: `(3 + 4i)^m = 5^m` would reduce modulo `5`, through `i ↦ 2`, to
`1 = 0`. -/
theorem w345_pow_ne_one {m : ℕ} (hm : 1 ≤ m) : w345 ^ m ≠ 1 := by
  intro h
  have h5 : (5 : ℂ) ^ m ≠ 0 := pow_ne_zero _ (by norm_num)
  rw [w345_eq_div, div_pow, div_eq_iff h5, one_mul] at h
  have h2 : (⟨3, 4⟩ : GaussianInt) ^ m = 5 ^ m := by
    apply GaussianInt.toComplex_inj.mp
    rw [map_pow, map_pow, map_ofNat]
    exact h
  have h3 := congrArg phi5 h2
  rw [map_pow, map_pow, phi5_three_four, phi5_five, one_pow, zero_pow (by omega : m ≠ 0)] at h3
  exact absurd h3 (by decide)

/-- The entry between the configurations `0` and `1` of the iterates of the drive at level `n`. -/
theorem zPh_iterate_entry (n : ℕ) (k : Fin n) (m : ℕ)
    (X : Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ) :
    ((⇑(conjAff (tokOp zPh n) (tokOp_isometry zPh_unitary n)))^[m] X) (0, k) (1, k)
      = X (0, k) (1, k) * star (w345 ^ m) := by
  rw [conjAff_iterate, tokOp_zPh_eq_diagonal, Matrix.diagonal_pow, Matrix.diagonal_conjTranspose,
    Matrix.mul_diagonal, Matrix.diagonal_mul, Pi.star_apply, Pi.pow_apply, Pi.pow_apply]
  simp

/-- **THE DRIVE HAS INFINITE ORDER ON THE FULL MATRIX ALGEBRA** at every positive level — while it is
the identity on every monomial token body. -/
theorem zPh_infiniteOrderOn_univ {n : ℕ} (hn : 0 < n) :
    CompositionOrder.InfiniteOrderOn (Set.univ : Set (Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ))
      (conjAff (tokOp zPh n) (tokOp_isometry zPh_unitary n)) := by
  intro m hm
  refine ⟨Matrix.of fun _ _ => (1 : ℂ), Set.mem_univ _, fun h => ?_⟩
  have h1 := congrFun (congrFun h (0, ⟨0, hn⟩)) (1, ⟨0, hn⟩)
  rw [zPh_iterate_entry n ⟨0, hn⟩ m] at h1
  simp only [Matrix.of_apply, one_mul] at h1
  have h2 : w345 ^ m = 1 := by
    have h3 := congrArg star h1
    rwa [star_star, star_one] at h3
  exact w345_pow_ne_one hm h2

/-- The angle `θ₀ = arccos (3/5)`: `w = exp (i θ₀)`. -/
noncomputable def theta0 : ℝ := Real.arccos (3 / 5)

theorem cos_theta0 : Real.cos theta0 = 3 / 5 :=
  Real.cos_arccos (by norm_num) (by norm_num)

theorem sin_theta0 : Real.sin theta0 = 4 / 5 := by
  rw [theta0, Real.sin_arccos, show (1 : ℝ) - (3 / 5) ^ 2 = (4 / 5) ^ 2 by norm_num,
    Real.sqrt_sq (by norm_num : (0 : ℝ) ≤ 4 / 5)]

theorem exp_theta0 : Complex.exp (theta0 * Complex.I) = w345 := by
  rw [Complex.exp_mul_I, ← Complex.ofReal_cos, ← Complex.ofReal_sin, cos_theta0, sin_theta0]
  unfold w345
  push_cast
  ring

/-- The fixed gate at `θ₀` is the real `3-4-5` rotation. -/
theorem rot_theta0_apply_00 : StateMixingCoupling.rot theta0 0 0 = (3 / 5 : ℂ) := by
  rw [StateMixingCoupling.rot_apply_00, cos_theta0]
  first | norm_num | (push_cast; ring) | simp

theorem rot_theta0_apply_10 : StateMixingCoupling.rot theta0 1 0 = (4 / 5 : ℂ) := by
  rw [StateMixingCoupling.rot_apply_10, sin_theta0]
  first | norm_num | (push_cast; ring) | simp

/-- **`θ₀ / π` IS IRRATIONAL**: a rational value `q` would make `w ^ (2 · den q) = 1`. -/
theorem irrational_theta0_div_pi : Irrational (theta0 / Real.pi) := by
  intro h
  rw [Set.mem_range] at h
  obtain ⟨q, hq⟩ := h
  have hθ : (q : ℝ) * Real.pi = theta0 := (eq_div_iff Real.pi_ne_zero).mp hq
  have hden : (q : ℝ) * (q.den : ℝ) = (q.num : ℝ) := by exact_mod_cast Rat.mul_den_eq_num q
  have hreal : (2 * (q.den : ℝ)) * theta0 = (q.num : ℝ) * (2 * Real.pi) := by
    rw [← hθ]
    linear_combination (2 * Real.pi) * hden
  have hw : w345 ^ (2 * q.den) = 1 := by
    rw [← exp_theta0, ← Complex.exp_nat_mul]
    have e : ((2 * q.den : ℕ) : ℂ) * ((theta0 : ℂ) * Complex.I)
        = ((q.num : ℤ) : ℂ) * (2 * (Real.pi : ℂ) * Complex.I) := by
      have hc := congrArg (fun x : ℝ => (x : ℂ)) hreal
      push_cast at hc ⊢
      linear_combination Complex.I * hc
    rw [e, Complex.exp_int_mul_two_pi_mul_I]
  exact w345_pow_ne_one (by have := q.den_pos; omega) hw

/-- **THE FIXED GATE AT θ₀ HAS THE KERNEL'S DENSE UNITARY CONTROL** at every level: the closure, not
the exact group (`denseUnitaryControl_of_fixedGate` with the irrationality of `θ₀/π`). -/
theorem fixedGateTheory_theta0_denseUnitaryControl : DenseUnitaryControl (fixedGateTheory theta0) :=
  fixedGateTheory_denseUnitaryControl irrational_theta0_div_pi

/-- **AND IS NOT EXACT QUANTUM MECHANICS**: density is not exactness. -/
theorem fixedGateTheory_theta0_not_qm :
    ¬ LevelOneSeam.ExactAllFiniteEndomorphicQuantumOps (fixedGateTheory theta0) :=
  fixedGateTheory_not_qm theta0

end Phase

/-! ### §G — descent from a level to the token; the Clifford angles -/

section Descent

/-- The fresh-ancilla blocks of `U ⊗ 1ₙ`: `U` on the diagonal blocks, zero elsewhere. -/
theorem ancBlock_tokOp (U : Matrix (Fin 2) (Fin 2) ℂ) (n : ℕ) (f e : Fin n) :
    AncillaClosure.ancBlock (tokOp U n) f e = if f = e then U else 0 := by
  ext s t
  simp only [AncillaClosure.ancBlock, Matrix.of_apply, tokOp, tensorOf_apply, Matrix.one_apply]
  split_ifs <;> simp

/-- **THE UNIFORM DISCARD OF `conjChannel (U ⊗ 1ₘ₊₁)` IS `conjChannel U`** — the discarded family is
itself a unitary conjugation on the smaller system (`discardWith_uniform_conjChannel`; the proof of
the kernel's `MinimalRepertoire.discard_tensorOf_one`, on the token's carrier). -/
theorem discard_tokOp_eq (U : Matrix (Fin 2) (Fin 2) ℂ) (m : ℕ) :
    discardWith (A := Fin 2) (m + 1) (uniformAttach (m + 1)) (conjChannel (tokOp U (m + 1)))
      = conjChannel U := by
  rw [AncillaClosure.discardWith_uniform_conjChannel]
  have hc : ∀ f e : Fin (m + 1),
      conjChannel (AncillaClosure.ancBlock (tokOp U (m + 1)) f e)
        = if f = e then conjChannel U else 0 := by
    intro f e
    rw [ancBlock_tokOp]
    split_ifs <;> simp [MicroReversibility.conjChannel_zero']
  simp only [hc, Fintype.sum_prod_type, Finset.sum_ite_eq, Finset.mem_univ, if_true,
    Finset.sum_const, Finset.card_univ, Fintype.card_fin]
  rw [← Nat.cast_smul_eq_nsmul ℂ, smul_smul,
    inv_mul_cancel₀ (Nat.cast_ne_zero.mpr m.succ_ne_zero), one_smul]

/-- `U ⊗ 1₁` is the relabelling of `U` along `Fin 2 ≃ Fin 2 × Fin 1`. -/
theorem reindex_prodUnique (U : Matrix (Fin 2) (Fin 2) ℂ) :
    Matrix.reindex (Equiv.prodUnique (Fin 2) (Fin 1)).symm (Equiv.prodUnique (Fin 2) (Fin 1)).symm U
      = tokOp U 1 := by
  ext ⟨b, k⟩ ⟨b', k'⟩
  have hk : k = k' := Subsingleton.elim _ _
  subst hk
  simp [Matrix.reindex_apply, Matrix.submatrix_apply, tokOp, tensorOf_apply]

/-- **DESCENT**: for a label-invariant class, token availability at a positive level gives it at
level one — discard the uniform ancilla (a unitary conjugation again), then relabel. -/
theorem tokenAvail_descend {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hl : LabelInvariant 𝓘) (U : Matrix (Fin 2) (Fin 2) ℂ) (m : ℕ)
    (h : TokenAvailAt 𝓘 arch U (m + 1)) : TokenAvailAt 𝓘 arch U 1 := by
  have h' : InstAvail 𝓘 (Fin 2 × Fin (m + 1)) Unit (fun _ => conjChannel (tokOp U (m + 1))) := h
  have hd := InstAvail.discard (by omega : 0 < m + 1) h'
  simp only [discard_tokOp_eq U m] at hd
  have ht := instAvail_transport hl hd (Fin 2 × Fin 1) (Equiv.prodUnique (Fin 2) (Fin 1)).symm
  simp only [SpectatorBridge.transport_conjChannel, reindex_prodUnique] at ht
  exact ht

/-- **O9-L1 AS A NAMED INPUT**: every unitary whose conjugation is available at level one in the
balanced fixed-gate theory is a scalar multiple of a level-one group element placed at the ancilla
value `0` (written, with exact checks, in NOTES-O9 §2; not kernel-checked). -/
def LevelOneCliffordInput : Prop :=
  ∀ V : Matrix (Fin 2 × Fin 1) (Fin 2 × Fin 1) ℂ, Vᴴ * V = 1 →
    (fixedGateTheory (Real.pi / 4)).availExt 1 Unit (fun _ => conjChannel V) →
      ∃ (c : ℂ) (G : Matrix (Fin 2) (Fin 2) ℂ), Gen2 (Real.pi / 4) G ∧ V = c • blockOf (0 : Fin 1) G

/-- A Pauli with a vanishing `(0, 0)` entry has its off-diagonal entries equal or opposite. -/
theorem pauli_offdiag {P : Matrix (Fin 2) (Fin 2) ℂ} (h : P ∈ Pauli) (h00 : P 0 0 = 0) :
    P 0 1 = P 1 0 ∨ P 0 1 = -P 1 0 := by
  obtain ⟨k, q, rfl⟩ := mem_pauli.mp h
  have hk : Complex.I ^ (k : ℕ) ≠ 0 := pow_ne_zero _ Complex.I_ne_zero
  fin_cases q <;> simp [pauliBase, X2, Y2, Z2, hk, Complex.I_ne_zero] at h00 ⊢

/-- The entries of a matrix conjugated by the drive's operator. -/
theorem zPh_conj_apply (M : Matrix (Fin 2) (Fin 2) ℂ) (i j : Fin 2) :
    (zPh * M * zPhᴴ) i j
      = (![(1 : ℂ), w345] : Fin 2 → ℂ) i * M i j * star ((![(1 : ℂ), w345] : Fin 2 → ℂ) j) := by
  rw [zPh, Matrix.diagonal_conjTranspose, Matrix.mul_diagonal, Matrix.diagonal_mul, Pi.star_apply]

/-- **`zPh X zPhᴴ` IS NOT A PAULI**: its off-diagonal entries `w̄`, `w` are neither equal nor
opposite. -/
theorem zPh_X_conj_not_pauli : zPh * X2 * zPhᴴ ∉ Pauli := by
  intro h
  have e00 : (zPh * X2 * zPhᴴ) 0 0 = 0 := by
    rw [zPh_conj_apply]
    simp [X2]
  have e01 : (zPh * X2 * zPhᴴ) 0 1 = star w345 := by
    rw [zPh_conj_apply]
    simp [X2]
  have e10 : (zPh * X2 * zPhᴴ) 1 0 = w345 := by
    rw [zPh_conj_apply]
    simp [X2]
  rcases pauli_offdiag h e00 with h1 | h1
  · rw [e01, e10, w345_star] at h1
    unfold w345 at h1
    have : Complex.I = 0 := by linear_combination (-5 / 8 : ℂ) * h1
    exact Complex.I_ne_zero this
  · rw [e01, e10, w345_star] at h1
    unfold w345 at h1
    have : (6 / 5 : ℂ) = 0 := by linear_combination h1
    norm_num at this

/-- **UNDER THE LEVEL-ONE INPUT, THE BALANCED FIXED GATE HAS NO DRIVE**: a level-one availability of
`zPh ⊗ 1₁` would place a unit multiple of `zPh` in the level-one group, whose conjugation normalizes
the Pauli set, while `zPh X zPhᴴ` is not a Pauli. -/
theorem not_opDrive_pi_div_four (hB : LevelOneCliffordInput) :
    ¬ OpDrive (MixR {Real.pi / 4}) (mixR_arch {Real.pi / 4}) := by
  intro h
  have h1 : TokenAvailAt (MixR {Real.pi / 4}) (mixR_arch {Real.pi / 4}) zPh 1 := h 1 Nat.one_pos
  have h1' : (fixedGateTheory (Real.pi / 4)).availExt 1 Unit
      (fun _ => conjChannel (tokOp zPh 1)) := h1
  obtain ⟨c, G, hG, hV⟩ := hB _ (tokOp_isometry zPh_unitary 1) h1'
  rw [blockOf_fin_one] at hV
  have hzG : zPh = c • G := by
    ext b b'
    have e := congrFun (congrFun hV (b, 0)) (b', 0)
    simpa [tokOp, tensorOf_apply] using e
  have hc0 : c ≠ 0 := by
    rintro rfl
    rw [zero_smul] at hzG
    exact zPh_00_ne (by simp [hzG])
  have hG_eq : G = c⁻¹ • zPh := by rw [hzG, smul_smul, inv_mul_cancel₀ hc0, one_smul]
  have hunit : star c⁻¹ * c⁻¹ = 1 := by
    have hu := hG.unitary
    rw [hG_eq, Matrix.conjTranspose_smul, Matrix.smul_mul, Matrix.mul_smul, zPh_unitary,
      smul_smul] at hu
    have e := congrFun (congrFun hu 0) 0
    simpa using e
  have hP := Gen2.pauli_conj hG X2 X2_mem_pauli
  rw [hG_eq, Matrix.conjTranspose_smul, Matrix.smul_mul, Matrix.smul_mul, Matrix.mul_smul,
    smul_smul, mul_comm c⁻¹ (star c⁻¹), hunit, one_smul] at hP
  exact zPh_X_conj_not_pauli hP

/-- **AT EVERY CLIFFORD ANGLE**, through `OriginAngle`'s reduction of the class at `k·β` to the
class at `β`. -/
theorem not_opDrive_of_rotClifford (hB : LevelOneCliffordInput) {α : ℝ}
    (hα : OriginAngle.RotClifford α) : ¬ OpDrive (MixR {α}) (mixR_arch {α}) := by
  intro h
  obtain ⟨k, rfl⟩ := (OriginAngle.rotClifford_iff α).mp hα
  apply not_opDrive_pi_div_four hB
  intro n hn
  have h1 := h n hn
  unfold TokenAvailAt at h1 ⊢
  exact genTheory_mono _ _ (mixR_arch _) (OriginAngle.mixR_of_int_mul (Real.pi / 4) k) n _ h1

end Descent

/-! ### §H — the cores -/

section Cores

/-- **O14, THE CORE.** -/
theorem o14_core :
    OpDrive substratumClass substratumClass_arch ∧
    (∀ {𝓘 : ImplementationClass} (arch : Architecture 𝓘),
      LiftAudit.SubstratumAvail (genTheory 𝓘 arch (Fin 2)) → OpDrive 𝓘 arch) ∧
    (∀ {𝓘 : ImplementationClass} (arch : Architecture 𝓘),
      LevelOneSeam.ExactAllFiniteEndomorphicQuantumOps (genTheory 𝓘 arch (Fin 2)) → OpDrive 𝓘 arch) ∧
    ¬ OpDrive permClass permClass_arch ∧
    ¬ OpDrive (MixR (∅ : Set ℝ)) (mixR_arch (∅ : Set ℝ)) ∧
    ¬ OpDrive latticeClass latticeClass_arch ∧
    ¬ LiftAudit.SubstratumAvail (latticeTheory (Fin 2)) ∧
    OpDrive driveClass driveClass_arch ∧
    (∀ (A : Type) [Fintype A] [DecidableEq A], DerivedOI (driveTheory A)) ∧
    ¬ LevelOneSeam.ExactAllFiniteEndomorphicQuantumOps (driveTheory (Fin 2)) ∧
    (∀ n : ℕ, 0 < n → ¬ TokenAvailAt driveClass driveClass_arch uJ n) ∧
    ¬ DenseUnitaryControl (driveTheory (Fin 2)) ∧
    ¬ DenseUnitaryControl (substratumTheory (Fin 2)) ∧
    (∀ n : ℕ, ∀ X ∈ body driveClass (Fin 2 × Fin n), conjChannel (tokOp zPh n) X = X) ∧
    (∀ n : ℕ, 0 < n → CompositionOrder.InfiniteOrderOn
      (Set.univ : Set (Matrix (Fin 2 × Fin n) (Fin 2 × Fin n) ℂ))
      (conjAff (tokOp zPh n) (tokOp_isometry zPh_unitary n))) ∧
    Irrational (theta0 / Real.pi) ∧ DenseUnitaryControl (fixedGateTheory theta0) ∧
    ¬ LevelOneSeam.ExactAllFiniteEndomorphicQuantumOps (fixedGateTheory theta0) ∧
    (LevelOneCliffordInput → ∀ α : ℝ, OriginAngle.RotClifford α →
      ¬ OpDrive (MixR {α}) (mixR_arch {α})) :=
  ⟨opDrive_substratum, fun arch h => opDrive_of_substratumAvail arch h,
    fun arch h => opDrive_of_qm arch h, not_opDrive_perm,
    not_opDrive_mixEmpty, not_opDrive_lattice, lattice_not_substratumAvail, opDrive_drive,
    fun A _ _ => driveTheory_derivedOI A, driveTheory_not_qm, fun _ hn => drive_not_uJ hn,
    drive_not_denseUnitaryControl, substratum_not_denseUnitaryControl, zPh_trivial_on_drive_body,
    fun _ hn => zPh_infiniteOrderOn_univ hn, irrational_theta0_div_pi,
    fixedGateTheory_theta0_denseUnitaryControl, fixedGateTheory_theta0_not_qm,
    fun hB _ hα => not_opDrive_of_rotClifford hB hα⟩

/-- **THE STATED ACCESS'S REVERSIBLE GROUP, THE CORE.** -/
theorem latticeGroup_core :
    (∀ (T : Type) [Fintype T] [DecidableEq T] [Nonempty T] (V : Matrix T T ℂ), Vᴴ * V = 1 →
      (InstAvail latticeClass T Unit (fun _ => conjChannel V)
        ↔ ∃ c : ℂ, c ≠ 0 ∧ IsSubmonomial (c • V) ∧ QuartEq (c • V))) ∧
    (∀ (T : Type) [Fintype T] [DecidableEq T] [Nonempty T] (V : Matrix T T ℂ), Vᴴ * V = 1 →
      InstAvail latticeClass T Unit (fun _ => conjChannel V) →
        ∃ (b : ℂ) (M : Matrix T T ℂ), b ≠ 0 ∧ Matrix.of.symm M ∈ rootMats (T := T) 4 ∧ V = b • M) ∧
    (∀ (T : Type) [Fintype T] [DecidableEq T] [Nonempty T] (U : Matrix T T ℂ), Uᴴ * U = 1 →
      InstAvail latticeClass T Unit (fun _ => conjChannel U) →
        ∃ m : ℕ, 0 < m ∧ ∃ μ : ℂ, U ^ m = μ • (1 : Matrix T T ℂ)) ∧
    (∀ (T : Type) [Fintype T] [DecidableEq T],
      ¬ CompositionOrder.OrdInf (body latticeClass T) (availData latticeClass T)) ∧
    ¬ OriginAngle.LevelOneClause (latticeTheory (Fin 2)) :=
  ⟨fun _ _ _ _ _ hV => lattice_avail_iff hV,
    fun _ _ _ _ _ hV hav => lattice_avail_finite_upToScalar hV hav,
    fun _ _ _ _ _ hU hav => lattice_pow_scalar hU hav, fun _ _ _ => lattice_not_ordInf,
    lattice_not_levelOneClause⟩

end Cores

#print axioms opDrive_substratum
#print axioms opDrive_fullClass
#print axioms not_opDrive_of_quartLattice
#print axioms not_opDrive_perm
#print axioms not_opDrive_mixEmpty
#print axioms not_opDrive_lattice
#print axioms tokOp_zPh_eq_diagonal
#print axioms zPh_entry_star
#print axioms tokenAvail_zPh_of_substratumAvail
#print axioms opDrive_of_substratumAvail
#print axioms lattice_not_substratumAvail
#print axioms opDrive_of_control
#print axioms opDrive_of_qm
#print axioms wlat_of_quart
#print axioms wl_mul
#print axioms wl_smul
#print axioms wl_block
#print axioms wl_reindex
#print axioms wl_conjTranspose
#print axioms wl_tensorOf
#print axioms wl_one
#print axioms driveClass_arch
#print axioms driveClass_contextStable
#print axioms driveClass_labelInvariant
#print axioms driveClass_daggerStable
#print axioms driveClass_unitaryRaySaturated
#print axioms driveClass_structurallyClosed
#print axioms driveClass_configurationLevel
#print axioms lattice_le_drive
#print axioms permClass_le_drive
#print axioms drive_le_substratum
#print axioms phaseGate_drive
#print axioms driveTheory_derivedOI
#print axioms driveTheory_inverseAccessibility
#print axioms wlat_of_entries
#print axioms zPh_entries
#print axioms zPh_wlat
#print axioms tokOp_zPh_drive
#print axioms opDrive_drive
#print axioms drive_not_uJ
#print axioms rot_apply_01
#print axioms not_tokenAvail_rot_of_submonomial
#print axioms drive_not_rot
#print axioms driveTheory_closure
#print axioms driveTheory_token_not_control
#print axioms driveTheory_not_qm
#print axioms driveTheory_not_phaseFree
#print axioms driveTheory_not_layerFlowExecutable
#print axioms avail_unitary_iff
#print axioms lattice_avail_iff
#print axioms drive_avail_iff
#print axioms avail_monomial_of_submonomial
#print axioms rotQuarter_apply_00
#print axioms rotQuarter_apply_10
#print axioms norm_sqrt_two_div_two
#print axioms half_lt_sqrt_two_div_two
#print axioms not_levelOneClause_of_submonomial
#print axioms drive_not_levelOneClause
#print axioms lattice_not_levelOneClause
#print axioms substratum_not_levelOneClause
#print axioms substratum_not_denseUnitaryControl
#print axioms drive_not_denseUnitaryControl
#print axioms diagonal_fixes_diag
#print axioms diagonal_trivial_on_body
#print axioms drive_reach_diag
#print axioms lattice_reach_diag
#print axioms zPh_trivial_on_drive_body
#print axioms zPh_trivial_on_substratum_body
#print axioms drive_not_ordInf
#print axioms lattice_not_ordInf
#print axioms latticeTheory_datum_finiteOrderOn
#print axioms rootLat_four_of_quart
#print axioms pow_unitary
#print axioms pow_rootEntries
#print axioms mem_rootSet
#print axioms exists_pow_eq_of_rootEntries
#print axioms pow_scalar_of_eq'
#print axioms rootLat_normalize
#print axioms rootLat_pow_scalar
#print axioms lattice_avail_finite_upToScalar
#print axioms mixEmpty_avail_finite_upToScalar
#print axioms lattice_pow_scalar
#print axioms conjAff_iterate_scalar
#print axioms lattice_finiteOrderOn_univ
#print axioms lattice_not_infiniteOrderOn_univ
#print axioms phi5_three_four
#print axioms phi5_five
#print axioms w345_eq_div
#print axioms w345_pow_ne_one
#print axioms zPh_iterate_entry
#print axioms zPh_infiniteOrderOn_univ
#print axioms cos_theta0
#print axioms sin_theta0
#print axioms exp_theta0
#print axioms rot_theta0_apply_00
#print axioms rot_theta0_apply_10
#print axioms irrational_theta0_div_pi
#print axioms fixedGateTheory_theta0_denseUnitaryControl
#print axioms fixedGateTheory_theta0_not_qm
#print axioms ancBlock_tokOp
#print axioms discard_tokOp_eq
#print axioms reindex_prodUnique
#print axioms tokenAvail_descend
#print axioms pauli_offdiag
#print axioms zPh_conj_apply
#print axioms zPh_X_conj_not_pauli
#print axioms not_opDrive_pi_div_four
#print axioms not_opDrive_of_rotClifford
#print axioms o14_core
#print axioms latticeGroup_core

end OriginDrive
end OIBridge
