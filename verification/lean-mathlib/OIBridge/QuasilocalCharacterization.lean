/-
  OIBridge/QuasilocalCharacterization.lean — OI_Q Level III, fourth entry: the characterization.

  LEVEL III, ROUND FOUR. The third entry constructed the quasilocal completion and proved that the
  finite-stage structure extends to it, but identified the target "quasilocal lattice QM with
  discrete time" with the construction by definition. This entry removes that tautology: the
  target class is defined independently of the construction, and the construction is proved to be
  its unique member up to a canonical isomorphism.

  (1) LOCALITY. Observables of disjoint regions commute (`emb_comm_of_disjoint`,
      `stage_comm_of_disjoint`): a finite-stage theorem proved on kernels, so that locality can be
      stated as an axiom of the target class and verified for the construction rather than assumed.

  (2) THE TARGET CLASS (`QuasilocalSystem`): a C*-algebra with, for every finite region, a unital
      star homomorphism from the matrix algebra of the region's configurations, compatible along
      inclusions, injective, with observables of disjoint regions commuting, and with the union of
      the stages dense. Nothing in the definition refers to the scaffold, the local algebra, or the
      completion. The OI region completion is a member (`oiSystem`).

  (3) THE UNIVERSAL PROPERTY AND THE CANONICAL ISOMORPHISM. A compatible family of stage maps into
      any system factors uniquely through the local algebra (`localMap_ofM`, `localHom`,
      `localHom_unique`), isometrically because the stages are injective (`norm_localHom`), and
      extends by continuity to the completion (`canon`). The extension is a star homomorphism
      (`canonHom`), isometric (`norm_canon`), injective, and surjective because its range is
      closed and contains the dense union of the stages (`canonHom_surjective`); it is therefore a
      star isomorphism (`canonEquiv`), and it is the unique continuous map compatible with the
      stages (`canon_unique`). Any two systems of the target class are canonically isomorphic
      (`systemEquiv`, `systemEquiv_stage`, `systemEquiv_unique`), and every consistent family of
      density matrices is a state of every system (`systemState_isState`, `systemState_stage`).

  (4) THE DYNAMICS, TARGET A. An OI system (`OISystem`) is a system of the target class carrying a
      star automorphism that acts on every stage as the transport of the substratum update; the
      OI completion with its Heisenberg action is one (`oiDynamical`), the automorphism preserves
      locality (`oi_localityPreserving`), the canonical map intertwines the dynamics (`canon_dyn`),
      and two OI systems with the same substratum dynamics are canonically isomorphic compatibly
      with their automorphisms (`systemEquiv_dyn`).

  (5) THE REDUNDANCY TEST FOR TARGET B FAILS. The stronger target — general locality-preserving
      discrete dynamics — is not implied by the substratum: conjugation by a phase unitary at one
      site is a compatible family of stage automorphisms (`inclObs_phaseConj`), defines an
      isometric star automorphism of the quasilocal algebra of order four (`phaseEquiv`,
      `phaseQ_four`) that preserves locality (`phase_localityPreserving`), and is induced by no
      reversible finite-range substratum dynamics (`phaseQ_ne_heisQ`): on a single-site matrix
      unit it produces the factor `I`, whereas every transported matrix has real entries. The
      Level III equivalence is therefore stated for the OI-induced discrete automorphism and not
      for general locality-preserving dynamics; that choice is a theorem, not a preference.

  WHAT IS ADDED: nothing. No representation, no continuity or continuous-time law, no axiom
  beyond the definition of the target class, whose members are compared by their stages.

  WHAT IS NOT CLAIMED: no Hilbert-space representation is constructed or selected; the
  uniqueness is uniqueness among systems with THESE local stages (the matrix algebras of the
  substratum's configurations), not a classification of all quasilocal C*-systems; Target B is
  shown strictly larger and is not characterized. Whether a given OI prediction requires a
  distinguished sector is not decided; it is not claimed either way. Bare OI and the frozen
  Level I and Level II statements are untouched.
-/

import OIBridge.QuasilocalAlgebra

namespace OIBridge
namespace QuasilocalCharacterization

open Complex Matrix RegionTower QuasilocalAlgebra
open scoped ComplexOrder Matrix.Norms.L2Operator

set_option linter.unusedSectionVars false
-- Applying a stage map makes the elaborator re-check the completion's ring structure, which
-- costs several seconds per application; statements with several applications need more room.
set_option maxHeartbeats 1000000

/-! ### Section A — locality: observables of disjoint regions commute -/

section Locality

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]

/-- The kernel of a product of two local operators. -/
theorem kerOf_emb_mul_emb (Λ Λ' : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ)
    (Y : Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ) (t s : ι → Q) :
    kerOf (emb Λ X * emb Λ' Y) t s
      = ∑ g : Conf Λ' Q, Y g (glob Λ' s) * kern Λ X t (patch Λ' s g) := by
  rw [kerOf, Module.End.mul_apply, emb_single, one_smul, map_sum]
  simp only [map_smul, Finsupp.finsetSum_apply, Finsupp.smul_apply, emb_single_apply, one_mul,
    smul_eq_mul]

theorem agreeOffG_patch_iff_of_disjoint {Λ Λ' : Finset ι} (hd : Disjoint Λ Λ') (t s : ι → Q)
    (g : Conf Λ' Q) :
    AgreeOffG Λ t (patch Λ' s g) ↔ AgreeOffG (Λ ∪ Λ') t s ∧ glob Λ' t = g := by
  constructor
  · intro h
    refine ⟨fun i hi => ?_, ?_⟩
    · have hi1 : i ∉ Λ := fun h1 => hi (Finset.mem_union_left _ h1)
      have hi2 : i ∉ Λ' := fun h2 => hi (Finset.mem_union_right _ h2)
      rw [h i hi1, patch_apply_of_not_mem hi2]
    · funext x
      have hx : x.1 ∉ Λ := Finset.disjoint_right.mp hd x.2
      rw [glob, h x.1 hx, patch_apply_of_mem x.2]
  · rintro ⟨h1, h2⟩ i hi
    by_cases hi' : i ∈ Λ'
    · rw [patch_apply_of_mem hi', ← h2]
      rfl
    · rw [patch_apply_of_not_mem hi']
      exact h1 i (fun h => (Finset.mem_union.mp h).elim hi hi')

theorem glob_patch_of_disjoint {Λ Λ' : Finset ι} (hd : Disjoint Λ Λ') (s : ι → Q)
    (g : Conf Λ' Q) : glob Λ (patch Λ' s g) = glob Λ s := by
  funext x
  rw [glob, glob, patch_apply_of_not_mem (Finset.disjoint_left.mp hd x.2)]

open Classical in
/-- The kernel of a product of observables of disjoint regions. -/
theorem kerOf_emb_mul_emb_of_disjoint {Λ Λ' : Finset ι} (hd : Disjoint Λ Λ')
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) (Y : Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ) (t s : ι → Q) :
    kerOf (emb Λ X * emb Λ' Y) t s
      = if AgreeOffG (Λ ∪ Λ') t s
          then X (glob Λ t) (glob Λ s) * Y (glob Λ' t) (glob Λ' s) else 0 := by
  rw [kerOf_emb_mul_emb]
  by_cases h : AgreeOffG (Λ ∪ Λ') t s
  · rw [if_pos h, Finset.sum_eq_single (glob Λ' t)]
    · rw [kern_of_agree _ ((agreeOffG_patch_iff_of_disjoint hd t s _).mpr ⟨h, rfl⟩),
        glob_patch_of_disjoint hd, mul_comm]
    · intro g _ hg
      rw [kern_of_not_agree _
        (fun h' => hg ((agreeOffG_patch_iff_of_disjoint hd t s g).mp h').2.symm), mul_zero]
    · intro habs
      exact absurd (Finset.mem_univ _) habs
  · rw [if_neg h]
    refine Finset.sum_eq_zero fun g _ => ?_
    rw [kern_of_not_agree _ (fun h' => h ((agreeOffG_patch_iff_of_disjoint hd t s g).mp h').1),
      mul_zero]

open Classical in
/-- **LOCALITY**: observables of disjoint regions commute. -/
theorem emb_comm_of_disjoint {Λ Λ' : Finset ι} (hd : Disjoint Λ Λ')
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) (Y : Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ) :
    emb Λ X * emb Λ' Y = emb Λ' Y * emb Λ X := by
  apply ext_of_kerOf
  funext t s
  rw [kerOf_emb_mul_emb_of_disjoint hd, kerOf_emb_mul_emb_of_disjoint hd.symm, Finset.union_comm]
  split_ifs
  · ring
  · rfl

theorem ofM_comm_of_disjoint {Λ Λ' : Finset ι} (hd : Disjoint Λ Λ')
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) (Y : Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ) :
    ofM Λ X * ofM Λ' Y = ofM Λ' Y * ofM Λ X := Subtype.ext (emb_comm_of_disjoint hd X Y)

theorem stage_comm_of_disjoint {Λ Λ' : Finset ι} (hd : Disjoint Λ Λ')
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) (Y : Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ) :
    stage Λ X * stage Λ' Y = stage Λ' Y * stage Λ X := by
  rw [stage_apply, stage_apply, ← UniformSpace.Completion.coe_mul,
    ← UniformSpace.Completion.coe_mul, ofM_comm_of_disjoint hd]

end Locality

/-! ### Section B — the target class, defined independently of the construction -/

section Target

variable (ι Q : Type) [DecidableEq ι] [Fintype Q] [DecidableEq Q]

/-- **THE TARGET CLASS**: a discrete quasilocal lattice C*-system with the given local stages.
A C*-algebra with, for every finite region, a unital star homomorphism from the matrix algebra
of the region's configurations, compatible along inclusions, injective, with observables of
disjoint regions commuting, and with the union of the stages dense. Nothing here refers to the
scaffold, the local algebra, or the completion of the third entry. -/
structure QuasilocalSystem where
  /-- The algebra. -/
  A : Type
  [inst : CStarAlgebra A]
  /-- The stage embeddings. -/
  st : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ →⋆ₐ[ℂ] A
  compat : ∀ (Λ Λ' : Finset ι) (h : Λ ⊆ Λ') (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ),
    st Λ' (inclObs h X) = st Λ X
  injective : ∀ Λ, Function.Injective (st Λ)
  local_comm : ∀ (Λ Λ' : Finset ι), Disjoint Λ Λ' →
    ∀ (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) (Y : Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ),
      st Λ X * st Λ' Y = st Λ' Y * st Λ X
  dense : closure (⋃ Λ : Finset ι, Set.range (st Λ)) = Set.univ

attribute [instance] QuasilocalSystem.inst

variable {ι Q}

/-- **THE OI REGION COMPLETION IS A SYSTEM OF THE TARGET CLASS.** -/
noncomputable def oiSystem [Nonempty Q] : QuasilocalSystem ι Q where
  A := Quasilocal ι Q
  st := stage
  compat := fun _ _ h X => stage_inclObs h X
  injective := stage_injective
  local_comm := fun _ _ hd X Y => stage_comm_of_disjoint hd X Y
  dense := closure_iUnion_stage

/-- A state of a C*-algebra: a unital positive continuous functional. -/
def IsState {A : Type} [CStarAlgebra A] (ω : A →L[ℂ] ℂ) : Prop :=
  ω 1 = 1 ∧ ∀ x, 0 ≤ ω (star x * x)

theorem quasiState_isState [Nonempty Q] {ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ}
    (hρ : IsStateFamily ρ) : IsState (quasiState hρ) :=
  ⟨quasiState_one hρ, quasiState_nonneg hρ⟩

end Target

/-! ### Section C — the universal property and the canonical isomorphism -/

section Canonical

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]
variable (S : QuasilocalSystem ι Q)

/-- The map from the local algebra determined by the stages: the value on any representative. -/
noncomputable def localMap (a : localAlg ι Q) : S.A := S.st (rep a).1 (rep a).2

/-- **THE UNIVERSAL PROPERTY OF THE LOCAL ALGEBRA**: a compatible family of stage maps factors
through the local algebra, the value on a representative being independent of the
representative. -/
theorem localMap_ofM (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    localMap S (ofM Λ X) = S.st Λ X := by
  have h := ofM_rep (ofM Λ X)
  rw [ofM_eq_iff] at h
  unfold localMap
  rw [← S.compat _ _ (Finset.subset_union_left : (rep (ofM Λ X)).1 ⊆ (rep (ofM Λ X)).1 ∪ Λ), h,
    S.compat]

/-- The factored map is a star algebra homomorphism. -/
noncomputable def localHom : localAlg ι Q →⋆ₐ[ℂ] S.A where
  toFun := localMap S
  map_one' := by rw [← ofM_one (∅ : Finset ι), localMap_ofM, map_one]
  map_mul' a b := by
    obtain ⟨Λ, X, Y, rfl, rfl⟩ := exists_ofM₂ a b
    rw [← ofM_mul, localMap_ofM, localMap_ofM, localMap_ofM, map_mul]
  map_zero' := by rw [← ofM_zero (∅ : Finset ι), localMap_ofM, map_zero]
  map_add' a b := by
    obtain ⟨Λ, X, Y, rfl, rfl⟩ := exists_ofM₂ a b
    rw [← ofM_add, localMap_ofM, localMap_ofM, localMap_ofM, map_add]
  commutes' c := by
    rw [Algebra.algebraMap_eq_smul_one, ← ofM_one (∅ : Finset ι), ← ofM_smul, localMap_ofM,
      map_smul, map_one, Algebra.algebraMap_eq_smul_one]
  map_star' a := by
    obtain ⟨Λ, X, rfl⟩ := exists_ofM a
    rw [star_ofM, localMap_ofM, localMap_ofM, ← Matrix.star_eq_conjTranspose, map_star]

theorem localHom_ofM (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    localHom S (ofM Λ X) = S.st Λ X := localMap_ofM S Λ X

/-- Any star homomorphism from the local algebra agreeing with the stages is the factored map. -/
theorem localHom_unique (g : localAlg ι Q → S.A)
    (hg : ∀ (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ), g (ofM Λ X) = S.st Λ X) :
    g = localHom S := by
  funext a
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [hg, localHom_ofM]

/-- The factored map is isometric, because the stages are injective. -/
theorem norm_localHom (a : localAlg ι Q) : ‖localHom S a‖ = ‖a‖ := by
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [localHom_ofM, norm_ofM]
  exact NonUnitalStarAlgHom.norm_map (S.st Λ) (S.injective Λ) X

theorem isometry_localHom : Isometry (localHom S) :=
  AddMonoidHomClass.isometry_of_norm _ (norm_localHom S)

/-- **THE CANONICAL MAP**: the continuous extension of the factored map to the completion. -/
noncomputable def canon : Quasilocal ι Q → S.A := UniformSpace.Completion.extension (localHom S)

theorem canon_coe (a : localAlg ι Q) : canon S a = localHom S a :=
  UniformSpace.Completion.extension_coe (isometry_localHom S).uniformContinuous a

theorem continuous_canon : Continuous (canon S) := UniformSpace.Completion.continuous_extension

theorem canon_stage (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    canon S (stage Λ X) = S.st Λ X := by
  rw [stage_apply, canon_coe, localHom_ofM]

theorem canon_mul (x y : Quasilocal ι Q) : canon S (x * y) = canon S x * canon S y := by
  refine UniformSpace.Completion.induction_on₂ x y ?_ fun a b => ?_
  · exact isClosed_eq ((continuous_canon S).comp continuous_mul)
      (((continuous_canon S).comp continuous_fst).mul ((continuous_canon S).comp continuous_snd))
  · rw [← UniformSpace.Completion.coe_mul, canon_coe, canon_coe, canon_coe, map_mul]

theorem canon_add (x y : Quasilocal ι Q) : canon S (x + y) = canon S x + canon S y := by
  refine UniformSpace.Completion.induction_on₂ x y ?_ fun a b => ?_
  · exact isClosed_eq ((continuous_canon S).comp continuous_add)
      (((continuous_canon S).comp continuous_fst).add ((continuous_canon S).comp continuous_snd))
  · rw [← UniformSpace.Completion.coe_add, canon_coe, canon_coe, canon_coe, map_add]

theorem canon_smul (c : ℂ) (x : Quasilocal ι Q) : canon S (c • x) = c • canon S x := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq ((continuous_canon S).comp (continuous_const_smul c))
      ((continuous_const_smul c).comp (continuous_canon S))
  · rw [← UniformSpace.Completion.coe_smul, canon_coe, canon_coe, map_smul]

theorem canon_star (x : Quasilocal ι Q) : canon S (star x) = star (canon S x) := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq ((continuous_canon S).comp continuous_star_q)
      (continuous_star.comp (continuous_canon S))
  · rw [star_coe, canon_coe, canon_coe, map_star]

theorem canon_one : canon S 1 = 1 := by
  rw [← UniformSpace.Completion.coe_one, canon_coe, map_one]

theorem canon_zero : canon S 0 = 0 := by
  rw [← UniformSpace.Completion.coe_zero, canon_coe, map_zero]

/-- **THE CANONICAL MAP IS ISOMETRIC.** -/
theorem norm_canon (x : Quasilocal ι Q) : ‖canon S x‖ = ‖x‖ := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq (continuous_norm.comp (continuous_canon S)) continuous_norm
  · rw [canon_coe, UniformSpace.Completion.norm_coe, norm_localHom]

/-- The canonical map as a star algebra homomorphism. -/
noncomputable def canonHom : Quasilocal ι Q →⋆ₐ[ℂ] S.A where
  toFun := canon S
  map_one' := canon_one S
  map_mul' := canon_mul S
  map_zero' := canon_zero S
  map_add' := canon_add S
  commutes' c := by
    rw [Algebra.algebraMap_eq_smul_one, canon_smul, canon_one, Algebra.algebraMap_eq_smul_one]
  map_star' := canon_star S

theorem canonHom_apply (x : Quasilocal ι Q) : canonHom S x = canon S x := rfl

theorem isometry_canonHom : Isometry (canonHom S) :=
  AddMonoidHomClass.isometry_of_norm (canonHom S) (norm_canon S)

theorem canonHom_injective : Function.Injective (canonHom S) := (isometry_canonHom S).injective

/-- **THE CANONICAL MAP IS SURJECTIVE**: its range is closed (an isometric image of a complete
space) and contains the dense union of the stages. -/
theorem canonHom_surjective : Function.Surjective (canonHom S) := by
  intro y
  have hclosed : IsClosed (Set.range (canonHom S)) :=
    (isometry_canonHom S).isClosedEmbedding.isClosed_range
  have hsub : (⋃ Λ : Finset ι, Set.range (S.st Λ)) ⊆ Set.range (canonHom S) := by
    intro z hz
    obtain ⟨Λ, hΛ⟩ := Set.mem_iUnion.mp hz
    obtain ⟨X, rfl⟩ := hΛ
    exact ⟨stage Λ X, canon_stage S Λ X⟩
  have h := hclosed.closure_subset_iff.mpr hsub
  rw [S.dense] at h
  exact h (Set.mem_univ y)

theorem canonHom_bijective : Function.Bijective (canonHom S) :=
  ⟨canonHom_injective S, canonHom_surjective S⟩

/-- **THE CANONICAL ISOMORPHISM** of the OI region completion with any system of the target
class. -/
noncomputable def canonEquiv : Quasilocal ι Q ≃⋆ₐ[ℂ] S.A :=
  StarAlgEquiv.ofBijective (canonHom S) (canonHom_bijective S)

theorem canonEquiv_apply (x : Quasilocal ι Q) : canonEquiv S x = canon S x := rfl

theorem canonEquiv_stage (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    canonEquiv S (stage Λ X) = S.st Λ X := canon_stage S Λ X

/-- **UNIQUENESS**: any continuous map agreeing with the stages is the canonical map. -/
theorem canon_unique (g : Quasilocal ι Q → S.A) (hg : Continuous g)
    (hst : ∀ (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ), g (stage Λ X) = S.st Λ X) :
    g = canon S := by
  funext x
  refine UniformSpace.Completion.induction_on x (isClosed_eq hg (continuous_canon S)) fun a => ?_
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [← stage_apply, hst, canon_stage]

/-- **ANY TWO SYSTEMS OF THE TARGET CLASS ARE CANONICALLY ISOMORPHIC**, compatibly with the
stages. -/
noncomputable def systemEquiv (S S' : QuasilocalSystem ι Q) : S.A ≃⋆ₐ[ℂ] S'.A :=
  (canonEquiv S).symm.trans (canonEquiv S')

theorem systemEquiv_apply (S S' : QuasilocalSystem ι Q) (y : S.A) :
    systemEquiv S S' y = canonEquiv S' ((canonEquiv S).symm y) := rfl

theorem systemEquiv_stage (S S' : QuasilocalSystem ι Q) (Λ : Finset ι)
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) : systemEquiv S S' (S.st Λ X) = S'.st Λ X := by
  rw [systemEquiv_apply, ← canonEquiv_stage S Λ X, StarAlgEquiv.symm_apply_apply,
    canonEquiv_stage]

theorem systemEquiv_canon (S S' : QuasilocalSystem ι Q) (x : Quasilocal ι Q) :
    systemEquiv S S' (canon S x) = canon S' x := by
  rw [systemEquiv_apply, ← canonEquiv_apply, StarAlgEquiv.symm_apply_apply, canonEquiv_apply]

/-- The canonical isomorphism is the unique continuous map compatible with the stages. -/
theorem systemEquiv_unique (S S' : QuasilocalSystem ι Q) (g : S.A → S'.A) (hg : Continuous g)
    (hst : ∀ (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ), g (S.st Λ X) = S'.st Λ X) :
    g = systemEquiv S S' := by
  have h : g ∘ canon S = canon S' :=
    canon_unique S' (g ∘ canon S) (hg.comp (continuous_canon S))
      (fun Λ X => by rw [Function.comp_apply, canon_stage, hst])
  funext y
  obtain ⟨x, rfl⟩ := canonHom_surjective S y
  rw [canonHom_apply, ← Function.comp_apply (f := g), h, systemEquiv_canon]

/-- The inverse of the canonical isomorphism as a continuous linear map. -/
noncomputable def canonInvL : S.A →L[ℂ] Quasilocal ι Q :=
  LinearMap.mkContinuous
    { toFun := (canonEquiv S).symm
      map_add' := fun x y => map_add (canonEquiv S).symm x y
      map_smul' := fun c x => map_smul (canonEquiv S).symm c x } 1 (fun y => by
      rw [one_mul]
      show ‖(canonEquiv S).symm y‖ ≤ ‖y‖
      rw [← norm_canon S ((canonEquiv S).symm y), ← canonEquiv_apply,
        StarAlgEquiv.apply_symm_apply])

theorem canonInvL_apply (y : S.A) : canonInvL S y = (canonEquiv S).symm y := rfl

/-- States transport along the canonical isomorphism: every consistent family of density
matrices is a state of every system of the target class. -/
noncomputable def systemState {ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ}
    (hρ : IsStateFamily ρ) : S.A →L[ℂ] ℂ :=
  (quasiState hρ).comp (canonInvL S)

theorem systemState_apply {ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ}
    (hρ : IsStateFamily ρ) (y : S.A) :
    systemState S hρ y = quasiState hρ ((canonEquiv S).symm y) := rfl

theorem systemState_stage {ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ}
    (hρ : IsStateFamily ρ) (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    systemState S hρ (S.st Λ X) = (X * ρ Λ).trace := by
  rw [systemState_apply, ← canonEquiv_stage S Λ X, StarAlgEquiv.symm_apply_apply,
    quasiState_stage]

theorem systemState_isState {ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ}
    (hρ : IsStateFamily ρ) : IsState (systemState S hρ) := by
  refine ⟨?_, fun y => ?_⟩
  · rw [systemState_apply, map_one, quasiState_one]
  · rw [systemState_apply, map_mul, map_star]
    exact quasiState_nonneg hρ _

end Canonical

/-! ### Section D — the dynamics: Target A, the OI-induced discrete automorphism -/

section Dynamics

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]

theorem heisQ_smul (Φ : ReversibleDynamics ι Q) (c : ℂ) (x : Quasilocal ι Q) :
    heisQ Φ (c • x) = c • heisQ Φ x := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq ((continuous_heisQ Φ).comp (continuous_const_smul c))
      ((continuous_const_smul c).comp (continuous_heisQ Φ))
  · rw [← UniformSpace.Completion.coe_smul, heisQ_coe, heisQ_coe, heisLoc_smul,
      UniformSpace.Completion.coe_smul]

/-- The OI-induced dynamics as a star algebra automorphism of the quasilocal algebra. -/
noncomputable def heisEquiv (Φ : ReversibleDynamics ι Q) : Quasilocal ι Q ≃⋆ₐ[ℂ] Quasilocal ι Q where
  toFun := heisQ Φ
  invFun := heisQ Φ.inv
  left_inv := heisQ_inv_heisQ Φ
  right_inv := heisQ_heisQ_inv Φ
  map_mul' := heisQ_mul Φ
  map_add' := heisQ_add Φ
  map_smul' := heisQ_smul Φ
  map_star' := heisQ_star Φ

theorem heisEquiv_apply (Φ : ReversibleDynamics ι Q) (x : Quasilocal ι Q) :
    heisEquiv Φ x = heisQ Φ x := rfl

/-- **TARGET A**: a system of the target class carrying the OI-induced discrete dynamics: a star
automorphism acting on every stage as the transport of the substratum update. -/
structure OISystem (ι Q : Type) [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]
    extends QuasilocalSystem ι Q where
  Φ : ReversibleDynamics ι Q
  α : A ≃⋆ₐ[ℂ] A
  α_stage : ∀ (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ),
    α (st Λ X) = st (hat Φ Λ) (transported Φ Λ X)

/-- The OI region completion with its Heisenberg dynamics is a Target A system. -/
noncomputable def oiDynamical (Φ : ReversibleDynamics ι Q) : OISystem ι Q :=
  { oiSystem with Φ := Φ, α := heisEquiv Φ, α_stage := heisQ_stage Φ }

/-- A locality-preserving automorphism: every stage is carried into some stage. -/
def LocalityPreserving (S : QuasilocalSystem ι Q) (α : S.A → S.A) : Prop :=
  ∀ Λ : Finset ι, ∃ Λ' : Finset ι, ∀ X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ,
    α (S.st Λ X) ∈ Set.range (S.st Λ')

theorem oi_localityPreserving (T : OISystem ι Q) :
    LocalityPreserving T.toQuasilocalSystem T.α :=
  fun Λ => ⟨hat T.Φ Λ, fun X => ⟨transported T.Φ Λ X, (T.α_stage Λ X).symm⟩⟩

theorem continuous_starAlgEquiv {A : Type} [CStarAlgebra A] (α : A ≃⋆ₐ[ℂ] A) : Continuous α :=
  (AddMonoidHomClass.isometry_of_norm α (StarAlgEquiv.norm_map α)).continuous

/-- **THE CANONICAL MAP INTERTWINES THE DYNAMICS.** -/
theorem canon_dyn (T : OISystem ι Q) (x : Quasilocal ι Q) :
    canon T.toQuasilocalSystem (heisQ T.Φ x) = T.α (canon T.toQuasilocalSystem x) := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq ((continuous_canon _).comp (continuous_heisQ _))
      ((continuous_starAlgEquiv T.α).comp (continuous_canon _))
  · obtain ⟨Λ, X, rfl⟩ := exists_ofM a
    rw [← stage_apply, heisQ_stage, canon_stage, canon_stage, T.α_stage]

/-- **UNIQUENESS OF TARGET A SYSTEMS**: two systems with the same substratum dynamics are
related by the canonical isomorphism, which intertwines their automorphisms. -/
theorem systemEquiv_dyn (T T' : OISystem ι Q) (hΦ : T.Φ = T'.Φ) (y : T.A) :
    systemEquiv T.toQuasilocalSystem T'.toQuasilocalSystem (T.α y)
      = T'.α (systemEquiv T.toQuasilocalSystem T'.toQuasilocalSystem y) := by
  obtain ⟨x, rfl⟩ := canonHom_surjective T.toQuasilocalSystem y
  rw [canonHom_apply, ← canon_dyn, systemEquiv_canon, systemEquiv_canon, hΦ, canon_dyn]

end Dynamics

/-! ### Section E — the redundancy test for Target B: a locality-preserving automorphism that
no substratum dynamics induces -/

section TargetB

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]

/-- The phase weight of a configuration: `I` when the site `i₀` lies in the region and carries
the reference value, `1` otherwise. -/
noncomputable def phaseWt (i₀ : ι) (Λ : Finset ι) (f : Conf Λ Q) : ℂ :=
  if h : i₀ ∈ Λ then (if f ⟨i₀, h⟩ = Classical.arbitrary Q then I else 1) else 1

theorem phaseWt_mul_star_self (i₀ : ι) (Λ : Finset ι) (f : Conf Λ Q) :
    phaseWt i₀ Λ f * star (phaseWt i₀ Λ f) = 1 := by
  unfold phaseWt
  split_ifs <;> simp [Complex.conj_I]

theorem star_mul_self_phaseWt (i₀ : ι) (Λ : Finset ι) (f : Conf Λ Q) :
    star (phaseWt i₀ Λ f) * phaseWt i₀ Λ f = 1 := by
  rw [mul_comm, phaseWt_mul_star_self]

theorem phaseWt_pow_four (i₀ : ι) (Λ : Finset ι) (f : Conf Λ Q) : phaseWt i₀ Λ f ^ 4 = 1 := by
  unfold phaseWt
  split_ifs <;> simp [Complex.I_pow_four]

theorem phaseWt_confRestrict {i₀ : ι} {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (hΛ : i₀ ∈ Λ)
    (F : Conf Λ' Q) : phaseWt i₀ Λ' F = phaseWt i₀ Λ (confRestrict h F) := by
  unfold phaseWt
  rw [dif_pos hΛ, dif_pos (h hΛ)]
  rfl

theorem phaseWt_of_not_mem {i₀ : ι} {Λ : Finset ι} (hΛ : i₀ ∉ Λ) (f : Conf Λ Q) :
    phaseWt i₀ Λ f = 1 := by
  unfold phaseWt
  rw [dif_neg hΛ]

theorem phaseWt_eq_of_agree {i₀ : ι} {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (hΛ : i₀ ∉ Λ)
    {F G : Conf Λ' Q} (hFG : AgreeOff h F G) : phaseWt i₀ Λ' F = phaseWt i₀ Λ' G := by
  unfold phaseWt
  by_cases hΛ' : i₀ ∈ Λ'
  · rw [dif_pos hΛ', dif_pos hΛ', hFG ⟨i₀, hΛ'⟩ hΛ]
  · rw [dif_neg hΛ', dif_neg hΛ']

/-- The phase unitary of a region. -/
noncomputable def phaseU (i₀ : ι) (Λ : Finset ι) : Matrix (Conf Λ Q) (Conf Λ Q) ℂ :=
  diagonal (phaseWt i₀ Λ)

/-- Conjugation by the phase unitary at a finite stage. -/
noncomputable def phaseConj (i₀ : ι) (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    Matrix (Conf Λ Q) (Conf Λ Q) ℂ :=
  phaseU i₀ Λ * X * (phaseU i₀ Λ)ᴴ

theorem phaseConj_apply (i₀ : ι) (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ)
    (f g : Conf Λ Q) :
    phaseConj i₀ Λ X f g = phaseWt i₀ Λ f * X f g * star (phaseWt i₀ Λ g) := by
  rw [phaseConj, phaseU, diagonal_conjTranspose, mul_diagonal, diagonal_mul]
  simp only [Pi.star_apply]

/-- **THE PHASE CONJUGATIONS ARE COMPATIBLE WITH INCLUSION.** -/
theorem inclObs_phaseConj (i₀ : ι) {Λ Λ' : Finset ι} (h : Λ ⊆ Λ')
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    inclObs h (phaseConj i₀ Λ X) = phaseConj i₀ Λ' (inclObs h X) := by
  ext F G
  rw [phaseConj_apply, inclObs_apply, inclObs_apply]
  by_cases hFG : AgreeOff h F G
  · rw [if_pos hFG, if_pos hFG, phaseConj_apply]
    by_cases hΛ : i₀ ∈ Λ
    · rw [phaseWt_confRestrict h hΛ, phaseWt_confRestrict h hΛ]
    · rw [phaseWt_of_not_mem hΛ, phaseWt_of_not_mem hΛ, phaseWt_eq_of_agree h hΛ hFG, star_one,
        one_mul, mul_one, mul_comm, ← mul_assoc, star_mul_self_phaseWt, one_mul]
  · rw [if_neg hFG, if_neg hFG, mul_zero, zero_mul]

theorem phaseU_mul_conjTranspose (i₀ : ι) (Λ : Finset ι) :
    phaseU i₀ Λ * (phaseU i₀ Λ)ᴴ = (1 : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) := by
  rw [phaseU, diagonal_conjTranspose, diagonal_mul_diagonal, ← diagonal_one]
  congr 1
  funext f
  rw [Pi.star_apply, phaseWt_mul_star_self]

theorem conjTranspose_mul_phaseU (i₀ : ι) (Λ : Finset ι) :
    (phaseU i₀ Λ)ᴴ * phaseU i₀ Λ = (1 : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) := by
  rw [phaseU, diagonal_conjTranspose, diagonal_mul_diagonal, ← diagonal_one]
  congr 1
  funext f
  rw [Pi.star_apply, star_mul_self_phaseWt]

theorem phaseConj_mul (i₀ : ι) (Λ : Finset ι) (X Y : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    phaseConj i₀ Λ (X * Y) = phaseConj i₀ Λ X * phaseConj i₀ Λ Y := by
  unfold phaseConj
  simp only [Matrix.mul_assoc]
  rw [← Matrix.mul_assoc (phaseU i₀ Λ)ᴴ (phaseU i₀ Λ), conjTranspose_mul_phaseU, Matrix.one_mul]

theorem phaseConj_one (i₀ : ι) (Λ : Finset ι) :
    phaseConj i₀ Λ (1 : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) = 1 := by
  rw [phaseConj, Matrix.mul_one, phaseU_mul_conjTranspose]

theorem phaseConj_add (i₀ : ι) (Λ : Finset ι) (X Y : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    phaseConj i₀ Λ (X + Y) = phaseConj i₀ Λ X + phaseConj i₀ Λ Y := by
  simp only [phaseConj, Matrix.mul_add, Matrix.add_mul]

theorem phaseConj_smul (i₀ : ι) (Λ : Finset ι) (c : ℂ) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    phaseConj i₀ Λ (c • X) = c • phaseConj i₀ Λ X := by
  simp only [phaseConj, Matrix.mul_smul, Matrix.smul_mul]

theorem phaseConj_conjTranspose (i₀ : ι) (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    phaseConj i₀ Λ Xᴴ = (phaseConj i₀ Λ X)ᴴ := by
  simp only [phaseConj, conjTranspose_mul, conjTranspose_conjTranspose, Matrix.mul_assoc]

theorem phaseConj_injective (i₀ : ι) (Λ : Finset ι) :
    Function.Injective (phaseConj i₀ Λ (Q := Q)) := by
  intro X Y h
  have h2 := congrArg (fun M => (phaseU i₀ Λ)ᴴ * M * phaseU i₀ Λ) h
  simp only [phaseConj] at h2
  simpa [Matrix.mul_assoc, ← Matrix.mul_assoc (phaseU i₀ Λ)ᴴ, conjTranspose_mul_phaseU,
    phaseU_mul_conjTranspose] using h2

/-- The phase conjugation as a star algebra homomorphism of a finite stage. -/
noncomputable def phaseHom (i₀ : ι) (Λ : Finset ι) :
    Matrix (Conf Λ Q) (Conf Λ Q) ℂ →⋆ₐ[ℂ] Matrix (Conf Λ Q) (Conf Λ Q) ℂ where
  toFun := phaseConj i₀ Λ
  map_one' := phaseConj_one i₀ Λ
  map_mul' := phaseConj_mul i₀ Λ
  map_zero' := by simp only [phaseConj, Matrix.mul_zero, Matrix.zero_mul]
  map_add' := phaseConj_add i₀ Λ
  commutes' c := by
    rw [Algebra.algebraMap_eq_smul_one, phaseConj_smul, phaseConj_one]
  map_star' X := by
    rw [Matrix.star_eq_conjTranspose, Matrix.star_eq_conjTranspose, phaseConj_conjTranspose]

theorem norm_phaseConj (i₀ : ι) (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    ‖phaseConj i₀ Λ X‖ = ‖X‖ :=
  NonUnitalStarAlgHom.norm_map (phaseHom i₀ Λ) (phaseConj_injective i₀ Λ) X

/-- Four phase conjugations are the identity. -/
theorem phaseConj_four (i₀ : ι) (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    phaseConj i₀ Λ (phaseConj i₀ Λ (phaseConj i₀ Λ (phaseConj i₀ Λ X))) = X := by
  ext f g
  simp only [phaseConj_apply]
  have hf := phaseWt_pow_four i₀ Λ f
  have hg : star (phaseWt i₀ Λ g) ^ 4 = 1 := by rw [← star_pow, phaseWt_pow_four, star_one]
  linear_combination (X f g * star (phaseWt i₀ Λ g) ^ 4) * hf + X f g * hg

/-- The phase automorphism of the local algebra. -/
noncomputable def phaseLoc (i₀ : ι) (a : localAlg ι Q) : localAlg ι Q :=
  ofM (rep a).1 (phaseConj i₀ (rep a).1 (rep a).2)

theorem phaseLoc_ofM (i₀ : ι) (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    phaseLoc i₀ (ofM Λ X) = ofM Λ (phaseConj i₀ Λ X) := by
  unfold phaseLoc
  have h := ofM_rep (ofM Λ X)
  rw [ofM_eq_iff] at h ⊢
  rw [inclObs_phaseConj, inclObs_phaseConj, h]

theorem phaseLoc_mul (i₀ : ι) (a b : localAlg ι Q) :
    phaseLoc i₀ (a * b) = phaseLoc i₀ a * phaseLoc i₀ b := by
  obtain ⟨Λ, X, Y, rfl, rfl⟩ := exists_ofM₂ a b
  rw [← ofM_mul, phaseLoc_ofM, phaseLoc_ofM, phaseLoc_ofM, ← ofM_mul, phaseConj_mul]

theorem phaseLoc_add (i₀ : ι) (a b : localAlg ι Q) :
    phaseLoc i₀ (a + b) = phaseLoc i₀ a + phaseLoc i₀ b := by
  obtain ⟨Λ, X, Y, rfl, rfl⟩ := exists_ofM₂ a b
  rw [← ofM_add, phaseLoc_ofM, phaseLoc_ofM, phaseLoc_ofM, ← ofM_add, phaseConj_add]

theorem phaseLoc_smul (i₀ : ι) (c : ℂ) (a : localAlg ι Q) :
    phaseLoc i₀ (c • a) = c • phaseLoc i₀ a := by
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [← ofM_smul, phaseLoc_ofM, phaseLoc_ofM, ← ofM_smul, phaseConj_smul]

theorem phaseLoc_star (i₀ : ι) (a : localAlg ι Q) :
    phaseLoc i₀ (star a) = star (phaseLoc i₀ a) := by
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [star_ofM, phaseLoc_ofM, phaseLoc_ofM, star_ofM, phaseConj_conjTranspose]

theorem phaseLoc_sub (i₀ : ι) (a b : localAlg ι Q) :
    phaseLoc i₀ (a - b) = phaseLoc i₀ a - phaseLoc i₀ b := by
  rw [sub_eq_add_neg, phaseLoc_add, ← neg_one_smul ℂ b, phaseLoc_smul, neg_one_smul,
    ← sub_eq_add_neg]

theorem norm_phaseLoc (i₀ : ι) (a : localAlg ι Q) : ‖phaseLoc i₀ a‖ = ‖a‖ := by
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [phaseLoc_ofM, norm_ofM, norm_ofM, norm_phaseConj]

theorem phaseLoc_four (i₀ : ι) (a : localAlg ι Q) :
    phaseLoc i₀ (phaseLoc i₀ (phaseLoc i₀ (phaseLoc i₀ a))) = a := by
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [phaseLoc_ofM, phaseLoc_ofM, phaseLoc_ofM, phaseLoc_ofM, phaseConj_four]

theorem isometry_phaseLoc (i₀ : ι) : Isometry (phaseLoc i₀ (Q := Q)) :=
  Isometry.of_dist_eq fun a b => by
    rw [dist_eq_norm, dist_eq_norm, ← phaseLoc_sub, norm_phaseLoc]

/-- **THE PHASE AUTOMORPHISM OF THE QUASILOCAL ALGEBRA**: the continuous extension. -/
noncomputable def phaseQ (i₀ : ι) : Quasilocal ι Q → Quasilocal ι Q :=
  UniformSpace.Completion.map (phaseLoc i₀)

theorem phaseQ_coe (i₀ : ι) (a : localAlg ι Q) :
    phaseQ i₀ (a : Quasilocal ι Q) = ((phaseLoc i₀ a : localAlg ι Q) : Quasilocal ι Q) :=
  UniformSpace.Completion.map_coe (isometry_phaseLoc i₀).uniformContinuous a

theorem continuous_phaseQ (i₀ : ι) : Continuous (phaseQ i₀ (Q := Q)) :=
  UniformSpace.Completion.continuous_map

/-- The phase automorphism preserves locality stage by stage. -/
theorem phaseQ_stage (i₀ : ι) (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    phaseQ i₀ (stage Λ X) = stage Λ (phaseConj i₀ Λ X) := by
  rw [stage_apply, phaseQ_coe, phaseLoc_ofM, stage_apply]

theorem phaseQ_mul (i₀ : ι) (x y : Quasilocal ι Q) :
    phaseQ i₀ (x * y) = phaseQ i₀ x * phaseQ i₀ y := by
  refine UniformSpace.Completion.induction_on₂ x y ?_ fun a b => ?_
  · exact isClosed_eq ((continuous_phaseQ i₀).comp continuous_mul)
      (((continuous_phaseQ i₀).comp continuous_fst).mul ((continuous_phaseQ i₀).comp continuous_snd))
  · rw [← UniformSpace.Completion.coe_mul, phaseQ_coe, phaseQ_coe, phaseQ_coe, phaseLoc_mul,
      UniformSpace.Completion.coe_mul]

theorem phaseQ_add (i₀ : ι) (x y : Quasilocal ι Q) :
    phaseQ i₀ (x + y) = phaseQ i₀ x + phaseQ i₀ y := by
  refine UniformSpace.Completion.induction_on₂ x y ?_ fun a b => ?_
  · exact isClosed_eq ((continuous_phaseQ i₀).comp continuous_add)
      (((continuous_phaseQ i₀).comp continuous_fst).add ((continuous_phaseQ i₀).comp continuous_snd))
  · rw [← UniformSpace.Completion.coe_add, phaseQ_coe, phaseQ_coe, phaseQ_coe, phaseLoc_add,
      UniformSpace.Completion.coe_add]

theorem phaseQ_smul (i₀ : ι) (c : ℂ) (x : Quasilocal ι Q) :
    phaseQ i₀ (c • x) = c • phaseQ i₀ x := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq ((continuous_phaseQ i₀).comp (continuous_const_smul c))
      ((continuous_const_smul c).comp (continuous_phaseQ i₀))
  · rw [← UniformSpace.Completion.coe_smul, phaseQ_coe, phaseQ_coe, phaseLoc_smul,
      UniformSpace.Completion.coe_smul]

theorem phaseQ_star (i₀ : ι) (x : Quasilocal ι Q) : phaseQ i₀ (star x) = star (phaseQ i₀ x) := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq ((continuous_phaseQ i₀).comp continuous_star_q)
      (continuous_star_q.comp (continuous_phaseQ i₀))
  · rw [star_coe, phaseQ_coe, phaseQ_coe, star_coe, phaseLoc_star]

theorem norm_phaseQ (i₀ : ι) (x : Quasilocal ι Q) : ‖phaseQ i₀ x‖ = ‖x‖ := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq (continuous_norm.comp (continuous_phaseQ i₀)) continuous_norm
  · rw [phaseQ_coe, UniformSpace.Completion.norm_coe, UniformSpace.Completion.norm_coe,
      norm_phaseLoc]

theorem phaseQ_four (i₀ : ι) (x : Quasilocal ι Q) :
    phaseQ i₀ (phaseQ i₀ (phaseQ i₀ (phaseQ i₀ x))) = x := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq ((continuous_phaseQ i₀).comp ((continuous_phaseQ i₀).comp
      ((continuous_phaseQ i₀).comp (continuous_phaseQ i₀)))) continuous_id
  · rw [phaseQ_coe, phaseQ_coe, phaseQ_coe, phaseQ_coe, phaseLoc_four]

/-- The phase automorphism as a star algebra automorphism of the quasilocal algebra. -/
noncomputable def phaseEquiv (i₀ : ι) : Quasilocal ι Q ≃⋆ₐ[ℂ] Quasilocal ι Q where
  toFun := phaseQ i₀
  invFun := fun x => phaseQ i₀ (phaseQ i₀ (phaseQ i₀ x))
  left_inv := phaseQ_four i₀
  right_inv := phaseQ_four i₀
  map_mul' := phaseQ_mul i₀
  map_add' := phaseQ_add i₀
  map_smul' := phaseQ_smul i₀
  map_star' := phaseQ_star i₀

theorem phaseEquiv_apply (i₀ : ι) (x : Quasilocal ι Q) : phaseEquiv i₀ x = phaseQ i₀ x := rfl

/-- The phase automorphism is a locality-preserving automorphism of the OI system. -/
theorem phase_localityPreserving (i₀ : ι) :
    LocalityPreserving (oiSystem (ι := ι) (Q := Q)) (phaseEquiv i₀) :=
  fun Λ => ⟨Λ, fun X => ⟨phaseConj i₀ Λ X, (phaseQ_stage i₀ Λ X).symm⟩⟩

/-- Entries of a transported observable are finite sums of entries of the observable. -/
theorem transported_im_zero (Φ : ReversibleDynamics ι Q) (Λ : Finset ι)
    {X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ} (hX : ∀ f g, (X f g).im = 0)
    (g h : Conf (hat Φ Λ) Q) : (transported Φ Λ X g h).im = 0 := by
  unfold transported
  rw [Complex.im_sum]
  exact Finset.sum_eq_zero fun f _ => hX f _

theorem inclObs_im_zero {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') {X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ}
    (hX : ∀ f g, (X f g).im = 0) (F G : Conf Λ' Q) : (inclObs h X F G).im = 0 := by
  rw [inclObs_apply]
  split_ifs
  · exact hX _ _
  · rfl

/-- **TARGET B IS NOT REDUNDANT**: the phase automorphism is a locality-preserving star
automorphism of the quasilocal algebra that is induced by no reversible finite-range substratum
dynamics. On a single-site matrix unit it produces the factor `I`, whereas every transported
matrix has real entries. -/
theorem phaseQ_ne_heisQ [Nontrivial Q] (i₀ : ι) (Φ : ReversibleDynamics ι Q) :
    phaseQ i₀ ≠ heisQ Φ := by
  intro hEq
  set q₀ : Q := Classical.arbitrary Q with hq₀
  obtain ⟨q₁, hq₁⟩ := exists_ne q₀
  let Λ₀ : Finset ι := {i₀}
  let f₀ : Conf Λ₀ Q := fun _ => q₀
  let f₁ : Conf Λ₀ Q := fun _ => q₁
  let E : Matrix (Conf Λ₀ Q) (Conf Λ₀ Q) ℂ := Matrix.single f₀ f₁ (1 : ℂ)
  have hE : ∀ f g, (E f g).im = 0 := by
    intro f g
    simp only [E, Matrix.single_apply]
    split_ifs <;> rfl
  have h1 : stage Λ₀ (phaseConj i₀ Λ₀ E) = stage (hat Φ Λ₀) (transported Φ Λ₀ E) := by
    rw [← phaseQ_stage, hEq, heisQ_stage]
  rw [stage_apply, stage_apply] at h1
  have h2 := UniformSpace.Completion.coe_injective (localAlg ι Q) h1
  rw [ofM_eq_iff] at h2
  -- evaluate both sides at a pair of configurations of the common region differing only at i₀
  let Λ'' : Finset ι := Λ₀ ∪ hat Φ Λ₀
  have hi₀ : i₀ ∈ Λ'' := Finset.mem_union_left _ (Finset.mem_singleton_self i₀)
  let F : Conf Λ'' Q := fun _ => q₀
  let G : Conf Λ'' Q := fun x => if x.1 = i₀ then q₁ else q₀
  have hFG : AgreeOff (Finset.subset_union_left : Λ₀ ⊆ Λ'') F G := by
    intro x hx
    have hx' : x.1 ≠ i₀ := fun h => hx (by rw [h]; exact Finset.mem_singleton_self i₀)
    simp only [F, G, if_neg hx']
  have hL : inclObs (Finset.subset_union_left : Λ₀ ⊆ Λ'') (phaseConj i₀ Λ₀ E) F G = I := by
    rw [inclObs_apply, if_pos hFG, phaseConj_apply]
    have hF : confRestrict (Finset.subset_union_left : Λ₀ ⊆ Λ'') F = f₀ := by
      funext x; rfl
    have hG : confRestrict (Finset.subset_union_left : Λ₀ ⊆ Λ'') G = f₁ := by
      funext x
      have hx : x.1 = i₀ := Finset.mem_singleton.mp x.2
      simp only [confRestrict, G, if_pos hx, f₁]
    rw [hF, hG]
    have hw₀ : phaseWt i₀ Λ₀ f₀ = I := by
      unfold phaseWt
      rw [dif_pos (Finset.mem_singleton_self i₀), if_pos rfl]
    have hw₁ : phaseWt i₀ Λ₀ f₁ = 1 := by
      unfold phaseWt
      rw [dif_pos (Finset.mem_singleton_self i₀), if_neg hq₁]
    have hE01 : E f₀ f₁ = 1 := Matrix.single_apply_same f₀ f₁ 1
    rw [hw₀, hw₁, hE01, star_one, mul_one, mul_one]
  have hR : (inclObs (Finset.subset_union_right : hat Φ Λ₀ ⊆ Λ'') (transported Φ Λ₀ E) F G).im
      = 0 :=
    inclObs_im_zero _ (transported_im_zero Φ Λ₀ hE) F G
  have := congrArg (fun M => (M F G).im) h2
  rw [hL, hR, Complex.I_im] at this
  exact one_ne_zero this

end TargetB

/-! ### Section F — the audit summary for the fourth entry -/

section Summary

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q] [Nontrivial Q]

/-- **THE CHARACTERIZATION.** Any two systems of the target class are canonically isomorphic
compatibly with the stages, uniquely so; every consistent family of density matrices is a state
of every system; the canonical map intertwines the OI-induced dynamics, which preserves locality;
and the phase automorphism is a locality-preserving automorphism induced by no substratum
dynamics. -/
theorem quasilocal_characterization (S S' : QuasilocalSystem ι Q) (T : OISystem ι Q) :
    (∀ (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ),
      systemEquiv S S' (S.st Λ X) = S'.st Λ X)
    ∧ (∀ g : S.A → S'.A, Continuous g →
        (∀ (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ), g (S.st Λ X) = S'.st Λ X) →
        g = systemEquiv S S')
    ∧ (∀ (ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ) (hρ : IsStateFamily ρ),
        IsState (systemState S hρ)
        ∧ ∀ (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ),
          systemState S hρ (S.st Λ X) = (X * ρ Λ).trace)
    ∧ (∀ x : Quasilocal ι Q,
        canon T.toQuasilocalSystem (heisQ T.Φ x) = T.α (canon T.toQuasilocalSystem x))
    ∧ LocalityPreserving T.toQuasilocalSystem T.α
    ∧ (∀ i₀ : ι, LocalityPreserving (oiSystem (ι := ι) (Q := Q)) (phaseEquiv i₀))
    ∧ (∀ (i₀ : ι) (Φ : ReversibleDynamics ι Q), phaseQ i₀ ≠ heisQ Φ) :=
  ⟨systemEquiv_stage S S', systemEquiv_unique S S',
    fun _ hρ => ⟨systemState_isState S hρ, systemState_stage S hρ⟩,
    canon_dyn T, oi_localityPreserving T, phase_localityPreserving, phaseQ_ne_heisQ⟩

end Summary

#print axioms kerOf_emb_mul_emb
#print axioms agreeOffG_patch_iff_of_disjoint
#print axioms glob_patch_of_disjoint
#print axioms kerOf_emb_mul_emb_of_disjoint
#print axioms emb_comm_of_disjoint
#print axioms ofM_comm_of_disjoint
#print axioms stage_comm_of_disjoint
#print axioms quasiState_isState
#print axioms localMap_ofM
#print axioms localHom_ofM
#print axioms localHom_unique
#print axioms norm_localHom
#print axioms isometry_localHom
#print axioms canon_coe
#print axioms continuous_canon
#print axioms canon_stage
#print axioms canon_mul
#print axioms canon_add
#print axioms canon_smul
#print axioms canon_star
#print axioms canon_one
#print axioms canon_zero
#print axioms norm_canon
#print axioms canonHom_apply
#print axioms isometry_canonHom
#print axioms canonHom_injective
#print axioms canonHom_surjective
#print axioms canonHom_bijective
#print axioms canonEquiv_apply
#print axioms canonEquiv_stage
#print axioms canon_unique
#print axioms systemEquiv_apply
#print axioms systemEquiv_stage
#print axioms systemEquiv_canon
#print axioms systemEquiv_unique
#print axioms canonInvL_apply
#print axioms systemState_apply
#print axioms systemState_stage
#print axioms systemState_isState
#print axioms heisQ_smul
#print axioms heisEquiv_apply
#print axioms oi_localityPreserving
#print axioms continuous_starAlgEquiv
#print axioms canon_dyn
#print axioms systemEquiv_dyn
#print axioms phaseWt_mul_star_self
#print axioms star_mul_self_phaseWt
#print axioms phaseWt_pow_four
#print axioms phaseWt_confRestrict
#print axioms phaseWt_of_not_mem
#print axioms phaseWt_eq_of_agree
#print axioms phaseConj_apply
#print axioms inclObs_phaseConj
#print axioms phaseU_mul_conjTranspose
#print axioms conjTranspose_mul_phaseU
#print axioms phaseConj_mul
#print axioms phaseConj_one
#print axioms phaseConj_add
#print axioms phaseConj_smul
#print axioms phaseConj_conjTranspose
#print axioms phaseConj_injective
#print axioms norm_phaseConj
#print axioms phaseConj_four
#print axioms phaseLoc_ofM
#print axioms phaseLoc_mul
#print axioms phaseLoc_add
#print axioms phaseLoc_smul
#print axioms phaseLoc_star
#print axioms phaseLoc_sub
#print axioms norm_phaseLoc
#print axioms phaseLoc_four
#print axioms isometry_phaseLoc
#print axioms phaseQ_coe
#print axioms continuous_phaseQ
#print axioms phaseQ_stage
#print axioms phaseQ_mul
#print axioms phaseQ_add
#print axioms phaseQ_smul
#print axioms phaseQ_star
#print axioms norm_phaseQ
#print axioms phaseQ_four
#print axioms phaseEquiv_apply
#print axioms phase_localityPreserving
#print axioms transported_im_zero
#print axioms inclObs_im_zero
#print axioms phaseQ_ne_heisQ
#print axioms quasilocal_characterization

end QuasilocalCharacterization
end OIBridge
