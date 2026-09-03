/-
  OIBridge/QuasilocalAlgebra.lean — OI_Q Level III, third entry: the quasilocal completion.

  LEVEL III, ROUND THREE. The second entry proved that the finite regions of the fixed-spacing
  lattice form the correct tower, that inclusions and restrictions compose and are dual, that
  consistent families are the admissible states, and that discrete dynamics respects the causal
  cone — all at the finite stages. This entry constructs the infinite-region object itself and
  proves that the finite-stage structure extends to it.

  (1) THE LOCAL ALGEBRA AS EQUIVALENCE CLASSES. A finite-region observable `X` on `Λ` has a
      kernel on global configurations (`kern`: the entry on the restricted configurations when
      the two agree off `Λ`, and zero otherwise), and inclusion into a larger region does not
      change the kernel (`kern_inclObs`). The kernel is realized as an operator on the free
      vector space over global configurations (`Scaffold`, `emb`); this space carries no inner
      product, no norm and no state, and is only the algebraic device by which the direct limit
      is realized as a ring. Two observables have the same operator exactly when they agree
      after inclusion into a common region (`emb_eq_iff`), so the local algebra `localAlg` — the
      operators of some finite region — IS the algebra of equivalence classes of finite-region
      observables, and the finite-stage facts that inclusion is multiplicative, unital and
      injective are recovered from it (`inclObs_mul`, `inclObs_one`, `inclObs_injective`).

  (2) COMPATIBLE ISOMETRIC INCLUSIONS AND THE C*-NORM. Inclusion is a star algebra homomorphism
      between finite stages (`inclHom`), injective, hence isometric for the operator norm
      (`norm_inclObs`, from the uniqueness of the C*-norm). The norm and the involution of a
      local element are those of any representative (`norm_ofM`, `star_ofM`), and with them the
      local algebra is a normed star algebra satisfying the C*-identity (`instCStarRingLocal`).

  (3) THE NORM COMPLETION. The quasilocal algebra `Quasilocal ι Q` is the abstract norm
      completion of the local algebra. Its involution is the continuous extension of the local
      one (`star_coe`), and the C*-identity, the star-ring and star-module laws pass to the
      completion by density; it is a C*-algebra (`instCStarAlgebraQuasilocal`). Each finite
      stage embeds by a star homomorphism `stage Λ`, compatible along inclusions
      (`stage_inclObs`), isometric (`norm_stage`), injective, and the algebra is the closure of
      the union of the stages (`closure_iUnion_stage`): `𝒜 = closure (⋃_Λ 𝒜_Λ)` literally.

  (4) STATES. A consistent family of density matrices (`IsStateFamily`) defines a functional on
      the local algebra whose value on a representative is the trace pairing, well defined by
      the duality of the second entry (`evalLocal_ofM`), linear, unital and positive
      (`evalLocal_one`, `evalLocal_nonneg`), and bounded with an explicit constant from the
      positivity of the finite-stage functionals (`norm_evalLocal_le`). It therefore extends
      uniquely to a continuous functional on the completion (`quasiState`, `quasiState_unique`)
      which is unital and positive there (`quasiState_one`, `quasiState_nonneg`): every
      consistent family is a state of the quasilocal algebra. The reference family of the second
      entry is a state family (`uniformFamily_isStateFamily`), and its state is the tracial
      reference state (`referenceState_stage`).

  (5) DYNAMICS. A reversible finite-range dynamics (`ReversibleDynamics`: a bijection of global
      configurations whose update and inverse both have finite dependence and finite influence)
      acts on scaffold operators by conjugation with its permutation operator (`heis`). The
      transport of a local observable of `Λ` is a local observable of an explicit finite region
      `hat Φ Λ` (`heis_emb`, with the transported matrix `transported`), so the local algebra is
      stable (`heis_mem`); the transport is a star homomorphism between finite stages
      (`transportedHom`), injective, hence isometric (`norm_transported`); the action on the
      local algebra is multiplicative, unital, star-preserving, isometric and invertible
      (`heisLoc_mul`, `heisLoc_star`, `norm_heisLoc`, `heisLoc_inv_heisLoc`), and extends by
      continuity to an automorphism of the quasilocal algebra (`heisQ`, `heisQ_mul`,
      `heisQ_star`, `norm_heisQ`, `heisQ_inv_heisQ`). Iterating, an observable of `Λ` after
      `k` steps lives on the `k`-fold hat region (`heis_iterate_emb`): the algebraic causal cone.

  WHAT IS ADDED: nothing. No representation is chosen (the scaffold is not a Hilbert space and
  selects no state), no continuity axiom, no completeness axiom beyond the completion of a
  normed space, and no continuous-time law: the dynamics is the discrete update of the
  substratum. The construction uses only the region tower of the second entry, the norm of the
  finite stages, and Mathlib's completion of a normed ring.

  WHAT IS NOT CLAIMED: no Hilbert-space representation of the quasilocal algebra is constructed
  and none is selected; no inequivalence of representations is proved; the boundedness constant
  of a state on the local algebra is not shown to be sharp; the target "quasilocal lattice QM
  with discrete time" is identified with this construction by definition, and no independent
  characterization of that target is proved here. Whether a given OI prediction requires a
  distinguished sector is not decided; it is not claimed either way. Bare OI and the frozen
  Level I and Level II statements are untouched.
-/

import OIBridge.RegionTower
import Mathlib.Analysis.CStarAlgebra.Hom
import Mathlib.Analysis.CStarAlgebra.PositiveLinearMap
import Mathlib.Analysis.Normed.Module.Completion
import Mathlib.Analysis.Normed.Operator.Extend
import Mathlib.Topology.Algebra.UniformRing

namespace OIBridge
namespace QuasilocalAlgebra

open Complex Matrix RegionTower
open scoped ComplexOrder Matrix.Norms.L2Operator

set_option linter.unusedSectionVars false

/-! ### Section A — the scaffold, kernels, and the local algebra -/

section Scaffold

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q]

/-- Restriction of a global configuration to a region. -/
def glob (Λ : Finset ι) (s : ι → Q) : Conf Λ Q := fun x => s x.1

/-- Overwrite a global configuration on a region. -/
def patch (Λ : Finset ι) (s : ι → Q) (f : Conf Λ Q) : ι → Q :=
  fun i => if h : i ∈ Λ then f ⟨i, h⟩ else s i

/-- Two global configurations agree off a region. -/
def AgreeOffG (Λ : Finset ι) (t s : ι → Q) : Prop := ∀ i, i ∉ Λ → t i = s i

theorem glob_patch (Λ : Finset ι) (s : ι → Q) (f : Conf Λ Q) : glob Λ (patch Λ s f) = f := by
  funext x
  simp [glob, patch, x.2]

theorem patch_apply_of_not_mem {Λ : Finset ι} {s : ι → Q} {f : Conf Λ Q} {i : ι} (h : i ∉ Λ) :
    patch Λ s f i = s i := by
  simp [patch, h]

theorem patch_apply_of_mem {Λ : Finset ι} {s : ι → Q} {f : Conf Λ Q} {i : ι} (h : i ∈ Λ) :
    patch Λ s f i = f ⟨i, h⟩ := by
  simp [patch, h]

theorem agreeOffG_patch (Λ : Finset ι) (s : ι → Q) (f : Conf Λ Q) :
    AgreeOffG Λ (patch Λ s f) s := fun _ hi => patch_apply_of_not_mem hi

theorem agreeOffG_refl (Λ : Finset ι) (s : ι → Q) : AgreeOffG Λ s s := fun _ _ => rfl

theorem agreeOffG_symm {Λ : Finset ι} {t s : ι → Q} (h : AgreeOffG Λ t s) : AgreeOffG Λ s t :=
  fun i hi => (h i hi).symm

theorem agreeOffG_trans {Λ : Finset ι} {t s r : ι → Q} (h : AgreeOffG Λ t s)
    (h' : AgreeOffG Λ s r) : AgreeOffG Λ t r := fun i hi => (h i hi).trans (h' i hi)

theorem eq_patch_of_agreeOffG {Λ : Finset ι} {t s : ι → Q} (h : AgreeOffG Λ t s) :
    t = patch Λ s (glob Λ t) := by
  funext i
  by_cases hi : i ∈ Λ
  · simp [patch, glob, hi]
  · simp [patch, hi, h i hi]

theorem patch_glob (Λ : Finset ι) (s : ι → Q) : patch Λ s (glob Λ s) = s :=
  (eq_patch_of_agreeOffG (agreeOffG_refl Λ s)).symm

theorem patch_eq_iff {Λ : Finset ι} {s t : ι → Q} {f : Conf Λ Q} :
    patch Λ s f = t ↔ AgreeOffG Λ t s ∧ glob Λ t = f := by
  constructor
  · rintro rfl
    exact ⟨agreeOffG_patch Λ s f, glob_patch Λ s f⟩
  · rintro ⟨h1, h2⟩
    rw [← h2]
    exact (eq_patch_of_agreeOffG h1).symm

/-- Agreement off a smaller region inside a larger one. -/
theorem agreeOffG_iff {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (t s : ι → Q) :
    AgreeOffG Λ t s ↔ AgreeOffG Λ' t s ∧ AgreeOff h (glob Λ' t) (glob Λ' s) := by
  constructor
  · intro hts
    exact ⟨fun i hi => hts i (fun hi' => hi (h hi')), fun x hx => hts x.1 hx⟩
  · rintro ⟨h1, h2⟩ i hi
    by_cases hi' : i ∈ Λ'
    · exact h2 ⟨i, hi'⟩ hi
    · exact h1 i hi'

theorem confRestrict_glob {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (s : ι → Q) :
    confRestrict h (glob Λ' s) = glob Λ s := rfl

open Classical in
/-- The kernel of a local observable on global configurations: the entry on the restricted
configurations when the two agree off the region, and zero otherwise. -/
noncomputable def kern (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) (t s : ι → Q) : ℂ :=
  if AgreeOffG Λ t s then X (glob Λ t) (glob Λ s) else 0

theorem kern_of_agree {Λ : Finset ι} (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) {t s : ι → Q}
    (h : AgreeOffG Λ t s) : kern Λ X t s = X (glob Λ t) (glob Λ s) := by
  unfold kern
  rw [if_pos h]

theorem kern_of_not_agree {Λ : Finset ι} (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) {t s : ι → Q}
    (h : ¬ AgreeOffG Λ t s) : kern Λ X t s = 0 := by
  unfold kern
  rw [if_neg h]

theorem kern_patch (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) (s₀ : ι → Q)
    (f g : Conf Λ Q) : kern Λ X (patch Λ s₀ f) (patch Λ s₀ g) = X f g := by
  rw [kern_of_agree X (fun i hi => by rw [patch_apply_of_not_mem hi, patch_apply_of_not_mem hi]),
    glob_patch, glob_patch]

/-- **KERNELS OF INCLUDED OBSERVABLES AGREE**: inclusion does not change the kernel. -/
theorem kern_inclObs {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    kern Λ' (inclObs h X) = kern Λ X := by
  funext t s
  by_cases hts : AgreeOffG Λ t s
  · obtain ⟨h1, h2⟩ := (agreeOffG_iff h t s).mp hts
    rw [kern_of_agree _ hts, kern_of_agree _ h1, inclObs_apply, if_pos h2, confRestrict_glob,
      confRestrict_glob]
  · rw [kern_of_not_agree _ hts]
    by_cases h1 : AgreeOffG Λ' t s
    · rw [kern_of_agree _ h1, inclObs_apply, if_neg]
      exact fun h2 => hts ((agreeOffG_iff h t s).mpr ⟨h1, h2⟩)
    · rw [kern_of_not_agree _ h1]

theorem kern_add (Λ : Finset ι) (X Y : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) (t s : ι → Q) :
    kern Λ (X + Y) t s = kern Λ X t s + kern Λ Y t s := by
  by_cases h : AgreeOffG Λ t s
  · simp only [kern_of_agree _ h, Matrix.add_apply]
  · simp only [kern_of_not_agree _ h, add_zero]

theorem kern_smul (Λ : Finset ι) (c : ℂ) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) (t s : ι → Q) :
    kern Λ (c • X) t s = c * kern Λ X t s := by
  by_cases h : AgreeOffG Λ t s
  · simp only [kern_of_agree _ h, Matrix.smul_apply, smul_eq_mul]
  · simp only [kern_of_not_agree _ h, mul_zero]

theorem kern_conjTranspose (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) (t s : ι → Q) :
    kern Λ Xᴴ t s = star (kern Λ X s t) := by
  by_cases h : AgreeOffG Λ t s
  · rw [kern_of_agree _ h, kern_of_agree _ (agreeOffG_symm h), Matrix.conjTranspose_apply]
  · rw [kern_of_not_agree _ h, kern_of_not_agree _ (fun h' => h (agreeOffG_symm h')), star_zero]

open Classical in
theorem kern_one (Λ : Finset ι) (t s : ι → Q) :
    kern Λ (1 : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) t s = if s = t then 1 else 0 := by
  by_cases h : AgreeOffG Λ t s
  · rw [kern_of_agree _ h, Matrix.one_apply]
    by_cases hst : s = t
    · subst hst
      simp
    · rw [if_neg hst, if_neg]
      intro hg
      apply hst
      rw [eq_patch_of_agreeOffG h, hg, patch_glob]
  · rw [kern_of_not_agree _ h, if_neg]
    rintro rfl
    exact h (agreeOffG_refl Λ s)

/-- The scaffold: the free vector space on global configurations. It carries no inner product,
no norm, and no state; it is the algebraic device by which the direct limit of the finite stages
is realized as a ring. -/
abbrev Scaffold (ι Q : Type) : Type := (ι → Q) →₀ ℂ

/-- One additive structure on the scaffold, so that the ring and semiring structures of its
endomorphisms are built from the same instance. -/
noncomputable instance instScaffoldAddCommGroup (ι Q : Type) : AddCommGroup (Scaffold ι Q) :=
  Finsupp.instAddCommGroup

/-- A local observable as an operator on the scaffold. -/
noncomputable def emb (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    Module.End ℂ (Scaffold ι Q) :=
  Finsupp.linearCombination ℂ
    (fun s => ∑ f : Conf Λ Q, X f (glob Λ s) • Finsupp.single (patch Λ s f) (1 : ℂ))

theorem emb_single (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) (s : ι → Q) (c : ℂ) :
    emb Λ X (Finsupp.single s c)
      = c • ∑ f : Conf Λ Q, X f (glob Λ s) • Finsupp.single (patch Λ s f) (1 : ℂ) :=
  Finsupp.linearCombination_single ℂ _ _

open Classical in
/-- The operator of a local observable has the observable's kernel. -/
theorem emb_single_apply (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) (s : ι → Q)
    (c : ℂ) (t : ι → Q) : emb Λ X (Finsupp.single s c) t = c * kern Λ X t s := by
  rw [emb_single, Finsupp.smul_apply, Finsupp.finsetSum_apply, smul_eq_mul]
  congr 1
  simp only [Finsupp.smul_apply, Finsupp.single_apply, smul_eq_mul, mul_ite, mul_one, mul_zero]
  by_cases h : AgreeOffG Λ t s
  · rw [kern_of_agree _ h, Finset.sum_eq_single (glob Λ t)]
    · rw [if_pos (patch_eq_iff.mpr ⟨h, rfl⟩)]
    · intro f _ hf
      rw [if_neg]
      intro hp
      exact hf (patch_eq_iff.mp hp).2.symm
    · intro habs
      exact absurd (Finset.mem_univ _) habs
  · rw [kern_of_not_agree _ h]
    refine Finset.sum_eq_zero fun f _ => ?_
    rw [if_neg]
    intro hp
    exact h (patch_eq_iff.mp hp).1

/-- The kernel of an operator on the scaffold. -/
noncomputable def kerOf (T : Module.End ℂ (Scaffold ι Q)) (t s : ι → Q) : ℂ :=
  T (Finsupp.single s 1) t

theorem kerOf_emb (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    kerOf (emb Λ X) = kern Λ X := by
  funext t s
  rw [kerOf, emb_single_apply, one_mul]

/-- An operator on the scaffold is determined by its kernel. -/
theorem ext_of_kerOf {T T' : Module.End ℂ (Scaffold ι Q)} (h : kerOf T = kerOf T') : T = T' := by
  apply Finsupp.lhom_ext
  intro s c
  have hs : Finsupp.single s c = c • Finsupp.single s (1 : ℂ) := by
    rw [Finsupp.smul_single, smul_eq_mul, mul_one]
  rw [hs, map_smul, map_smul]
  congr 1
  ext t
  exact congrFun (congrFun h t) s

theorem kerOf_add (T T' : Module.End ℂ (Scaffold ι Q)) (t s : ι → Q) :
    kerOf (T + T') t s = kerOf T t s + kerOf T' t s := rfl

theorem kerOf_smul (c : ℂ) (T : Module.End ℂ (Scaffold ι Q)) (t s : ι → Q) :
    kerOf (c • T) t s = c * kerOf T t s := rfl

open Classical in
theorem kerOf_one (t s : ι → Q) :
    kerOf (1 : Module.End ℂ (Scaffold ι Q)) t s = if s = t then 1 else 0 := by
  rw [kerOf, Module.End.one_apply, Finsupp.single_apply]

/-- **COMPATIBILITY**: the operator of an included observable is the operator of the
observable. -/
theorem emb_inclObs {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    emb Λ' (inclObs h X) = emb Λ X :=
  ext_of_kerOf (by rw [kerOf_emb, kerOf_emb, kern_inclObs])

theorem emb_add (Λ : Finset ι) (X Y : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    emb Λ (X + Y) = emb Λ X + emb Λ Y :=
  ext_of_kerOf (by
    funext t s
    rw [kerOf_emb, kerOf_add, kerOf_emb, kerOf_emb, kern_add])

theorem emb_smul (Λ : Finset ι) (c : ℂ) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    emb Λ (c • X) = c • emb Λ X :=
  ext_of_kerOf (by
    funext t s
    rw [kerOf_emb, kerOf_smul, kerOf_emb, kern_smul])

theorem emb_zero (Λ : Finset ι) : emb Λ (0 : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) = 0 := by
  have := emb_smul Λ (0 : ℂ) (0 : Matrix (Conf Λ Q) (Conf Λ Q) ℂ)
  rwa [zero_smul, zero_smul] at this

theorem emb_one (Λ : Finset ι) : emb Λ (1 : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) = 1 :=
  ext_of_kerOf (by
    funext t s
    rw [kerOf_emb, kerOf_one, kern_one])

/-- **MULTIPLICATIVITY**: the operator of a product is the composite of the operators. -/
theorem emb_mul (Λ : Finset ι) (X Y : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    emb Λ (X * Y) = emb Λ X * emb Λ Y := by
  refine ext_of_kerOf ?_
  funext t s
  rw [kerOf_emb, kerOf, Module.End.mul_apply, emb_single, one_smul, map_sum]
  simp only [map_smul, Finsupp.finsetSum_apply, Finsupp.smul_apply, emb_single_apply, one_mul,
    smul_eq_mul]
  have hag : ∀ g : Conf Λ Q, AgreeOffG Λ t (patch Λ s g) ↔ AgreeOffG Λ t s := fun g =>
    ⟨fun h => agreeOffG_trans h (agreeOffG_patch Λ s g),
     fun h => agreeOffG_trans h (agreeOffG_symm (agreeOffG_patch Λ s g))⟩
  by_cases h : AgreeOffG Λ t s
  · rw [kern_of_agree _ h, Matrix.mul_apply]
    refine Finset.sum_congr rfl fun g _ => ?_
    rw [kern_of_agree _ ((hag g).mpr h), glob_patch, mul_comm]
  · rw [kern_of_not_agree _ h]
    symm
    refine Finset.sum_eq_zero fun g _ => ?_
    rw [kern_of_not_agree _ (fun h' => h ((hag g).mp h')), mul_zero]

/-- **INJECTIVITY**: distinct observables of a region have distinct operators. -/
theorem emb_injective [Nonempty Q] (Λ : Finset ι) :
    Function.Injective (emb Λ : Matrix (Conf Λ Q) (Conf Λ Q) ℂ → Module.End ℂ (Scaffold ι Q)) := by
  intro X Y h
  have hk : kern Λ X = kern Λ Y := by rw [← kerOf_emb, ← kerOf_emb, h]
  let s₀ : ι → Q := fun _ => Classical.arbitrary Q
  ext f g
  rw [← kern_patch Λ X s₀ f g, ← kern_patch Λ Y s₀ f g, hk]

/-- **THE EQUIVALENCE-CLASS THEOREM**: two finite-region observables have the same operator
exactly when they agree after inclusion into a common region. The local algebra is therefore
the algebra of equivalence classes of finite-region observables. -/
theorem emb_eq_iff [Nonempty Q] {Λ Λ' : Finset ι} (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ)
    (Y : Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ) :
    emb Λ X = emb Λ' Y
      ↔ inclObs Finset.subset_union_left X = inclObs Finset.subset_union_right Y := by
  constructor
  · intro h
    apply emb_injective (Λ ∪ Λ')
    rw [emb_inclObs, emb_inclObs, h]
  · intro h
    rw [← emb_inclObs (Finset.subset_union_left (s₂ := Λ')) X, h, emb_inclObs]

/-- The finite-stage facts recovered from the scaffold: inclusion is multiplicative, unital,
and injective. -/
theorem inclObs_mul [Nonempty Q] {Λ Λ' : Finset ι} (h : Λ ⊆ Λ')
    (X Y : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    inclObs h (X * Y) = inclObs h X * inclObs h Y := by
  apply emb_injective Λ'
  rw [emb_mul, emb_inclObs, emb_inclObs, emb_inclObs, emb_mul]

theorem inclObs_one [Nonempty Q] {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') :
    inclObs h (1 : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) = 1 := by
  apply emb_injective Λ'
  rw [emb_inclObs, emb_one, emb_one]

theorem inclObs_injective [Nonempty Q] {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') :
    Function.Injective (inclObs h : Matrix (Conf Λ Q) (Conf Λ Q) ℂ → _) := by
  intro X Y hXY
  apply emb_injective Λ
  rw [← emb_inclObs h X, ← emb_inclObs h Y, hXY]

theorem inclObs_add {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (X Y : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    inclObs h (X + Y) = inclObs h X + inclObs h Y := by
  ext F G
  simp only [inclObs_apply, Matrix.add_apply]
  split_ifs <;> simp

theorem inclObs_smul {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (c : ℂ)
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) : inclObs h (c • X) = c • inclObs h X := by
  ext F G
  simp only [inclObs_apply, Matrix.smul_apply, smul_eq_mul]
  split_ifs <;> simp

theorem inclObs_conjTranspose {Λ Λ' : Finset ι} (h : Λ ⊆ Λ')
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) : inclObs h Xᴴ = (inclObs h X)ᴴ := by
  ext F G
  have hsymm : AgreeOff h F G ↔ AgreeOff h G F :=
    ⟨fun a x hx => (a x hx).symm, fun a x hx => (a x hx).symm⟩
  simp only [inclObs_apply, Matrix.conjTranspose_apply]
  by_cases hFG : AgreeOff h F G
  · rw [if_pos hFG, if_pos (hsymm.mp hFG)]
  · rw [if_neg hFG, if_neg (fun a => hFG (hsymm.mpr a)), star_zero]

/-- **THE LOCAL ALGEBRA**: the operators of the scaffold that are local observables of some
region. -/
noncomputable def localAlg (ι Q : Type) [DecidableEq ι] [Fintype Q] [DecidableEq Q] :
    Subalgebra ℂ (Module.End ℂ (Scaffold ι Q)) where
  carrier := {T | ∃ (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ), emb Λ X = T}
  mul_mem' := by
    rintro _ _ ⟨Λ, X, rfl⟩ ⟨Λ', Y, rfl⟩
    refine ⟨Λ ∪ Λ', inclObs Finset.subset_union_left X * inclObs Finset.subset_union_right Y, ?_⟩
    rw [emb_mul, emb_inclObs, emb_inclObs]
  one_mem' := ⟨∅, 1, emb_one ∅⟩
  add_mem' := by
    rintro _ _ ⟨Λ, X, rfl⟩ ⟨Λ', Y, rfl⟩
    refine ⟨Λ ∪ Λ', inclObs Finset.subset_union_left X + inclObs Finset.subset_union_right Y, ?_⟩
    rw [emb_add, emb_inclObs, emb_inclObs]
  zero_mem' := ⟨∅, 0, emb_zero ∅⟩
  algebraMap_mem' := fun c => ⟨∅, c • 1, by
    rw [emb_smul, emb_one, Algebra.algebraMap_eq_smul_one]⟩

/-- A finite-region observable as an element of the local algebra. -/
noncomputable def ofM (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) : localAlg ι Q :=
  ⟨emb Λ X, Λ, X, rfl⟩

theorem ofM_val (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    (ofM Λ X : Module.End ℂ (Scaffold ι Q)) = emb Λ X := rfl

theorem ofM_inclObs {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    ofM Λ' (inclObs h X) = ofM Λ X := Subtype.ext (emb_inclObs h X)

theorem ofM_add (Λ : Finset ι) (X Y : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    ofM Λ (X + Y) = ofM Λ X + ofM Λ Y := Subtype.ext (emb_add Λ X Y)

theorem ofM_mul (Λ : Finset ι) (X Y : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    ofM Λ (X * Y) = ofM Λ X * ofM Λ Y := Subtype.ext (emb_mul Λ X Y)

theorem ofM_smul (Λ : Finset ι) (c : ℂ) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    ofM Λ (c • X) = c • ofM Λ X := Subtype.ext (emb_smul Λ c X)

theorem ofM_one (Λ : Finset ι) : ofM Λ (1 : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) = 1 :=
  Subtype.ext (emb_one Λ)

theorem ofM_zero (Λ : Finset ι) : ofM Λ (0 : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) = 0 :=
  Subtype.ext (emb_zero Λ)

theorem ofM_neg (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    ofM Λ (-X) = -ofM Λ X := by
  rw [← neg_one_smul ℂ X, ofM_smul]
  exact neg_one_smul ℂ (ofM Λ X)

theorem ofM_sub (Λ : Finset ι) (X Y : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    ofM Λ (X - Y) = ofM Λ X - ofM Λ Y := by
  rw [sub_eq_add_neg, ofM_add, ofM_neg]
  exact (sub_eq_add_neg (ofM Λ X) (ofM Λ Y)).symm

theorem ofM_injective [Nonempty Q] (Λ : Finset ι) :
    Function.Injective (ofM Λ : Matrix (Conf Λ Q) (Conf Λ Q) ℂ → localAlg ι Q) :=
  fun _ _ h => emb_injective Λ (congrArg Subtype.val h)

theorem ofM_eq_iff [Nonempty Q] {Λ Λ' : Finset ι} (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ)
    (Y : Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ) :
    ofM Λ X = ofM Λ' Y
      ↔ inclObs Finset.subset_union_left X = inclObs Finset.subset_union_right Y := by
  rw [← emb_eq_iff]
  exact ⟨fun h => congrArg Subtype.val h, fun h => Subtype.ext h⟩

/-- Every element of the local algebra is a finite-region observable. -/
theorem exists_ofM (a : localAlg ι Q) :
    ∃ (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ), ofM Λ X = a := by
  obtain ⟨Λ, X, h⟩ := a.2
  exact ⟨Λ, X, Subtype.ext h⟩

/-- Two elements of the local algebra live on a common region. -/
theorem exists_ofM₂ (a b : localAlg ι Q) :
    ∃ (Λ : Finset ι) (X Y : Matrix (Conf Λ Q) (Conf Λ Q) ℂ), ofM Λ X = a ∧ ofM Λ Y = b := by
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  obtain ⟨Λ', Y, rfl⟩ := exists_ofM b
  exact ⟨Λ ∪ Λ', inclObs Finset.subset_union_left X, inclObs Finset.subset_union_right Y,
    ofM_inclObs _ _, ofM_inclObs _ _⟩

/-- Three elements of the local algebra live on a common region. -/
theorem exists_ofM₃ (a b c : localAlg ι Q) :
    ∃ (Λ : Finset ι) (X Y Z : Matrix (Conf Λ Q) (Conf Λ Q) ℂ),
      ofM Λ X = a ∧ ofM Λ Y = b ∧ ofM Λ Z = c := by
  obtain ⟨Λ, X, Y, rfl, rfl⟩ := exists_ofM₂ a b
  obtain ⟨Λ', Z, rfl⟩ := exists_ofM c
  exact ⟨Λ ∪ Λ', inclObs Finset.subset_union_left X, inclObs Finset.subset_union_left Y,
    inclObs Finset.subset_union_right Z, ofM_inclObs _ _, ofM_inclObs _ _, ofM_inclObs _ _⟩

end Scaffold

/-! ### Section B — the C*-norm, isometric inclusions, and the norm completion -/

section Norm

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]

/-- Inclusion of observables as a star algebra homomorphism between the finite stages. -/
noncomputable def inclHom {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') :
    Matrix (Conf Λ Q) (Conf Λ Q) ℂ →⋆ₐ[ℂ] Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ where
  toFun := inclObs h
  map_one' := inclObs_one h
  map_mul' := inclObs_mul h
  map_zero' := by
    rw [← zero_smul ℂ (0 : Matrix (Conf Λ Q) (Conf Λ Q) ℂ), inclObs_smul, zero_smul]
  map_add' := inclObs_add h
  commutes' c := by
    rw [Algebra.algebraMap_eq_smul_one, inclObs_smul, inclObs_one, Algebra.algebraMap_eq_smul_one]
  map_star' X := by
    rw [Matrix.star_eq_conjTranspose, Matrix.star_eq_conjTranspose, inclObs_conjTranspose]

theorem inclHom_apply {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    inclHom h X = inclObs h X := rfl

/-- **INCLUSION IS ISOMETRIC** for the operator norm: an injective star homomorphism between
C*-algebras preserves the norm. -/
theorem norm_inclObs {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    ‖inclObs h X‖ = ‖X‖ :=
  NonUnitalStarAlgHom.norm_map (inclHom h) (inclObs_injective h) X

/-- A representative of an element of the local algebra. -/
noncomputable def rep (a : localAlg ι Q) : Σ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ :=
  ⟨Classical.choose (exists_ofM a), Classical.choose (Classical.choose_spec (exists_ofM a))⟩

theorem ofM_rep (a : localAlg ι Q) : ofM (rep a).1 (rep a).2 = a :=
  Classical.choose_spec (Classical.choose_spec (exists_ofM a))

/-- The involution: the conjugate transpose of any representative. -/
noncomputable instance instStarLocal : Star (localAlg ι Q) :=
  ⟨fun a => ofM (rep a).1 (rep a).2ᴴ⟩

theorem star_ofM (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    star (ofM Λ X) = ofM Λ Xᴴ := by
  show ofM (rep (ofM Λ X)).1 (rep (ofM Λ X)).2ᴴ = ofM Λ Xᴴ
  have h := ofM_rep (ofM Λ X)
  rw [ofM_eq_iff] at h ⊢
  rw [inclObs_conjTranspose, inclObs_conjTranspose, h]

/-- The norm: the operator norm of any representative. -/
noncomputable def nrm (a : localAlg ι Q) : ℝ := ‖(rep a).2‖

theorem nrm_ofM (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) : nrm (ofM Λ X) = ‖X‖ := by
  have h := ofM_rep (ofM Λ X)
  rw [ofM_eq_iff] at h
  unfold nrm
  rw [← norm_inclObs (Finset.subset_union_left : (rep (ofM Λ X)).1 ⊆ (rep (ofM Λ X)).1 ∪ Λ), h,
    norm_inclObs]

/-- The norm as an additive group norm. -/
noncomputable def localNorm : AddGroupNorm (localAlg ι Q) where
  toFun := nrm
  map_zero' := by rw [← ofM_zero (∅ : Finset ι), nrm_ofM, norm_zero]
  add_le' a b := by
    obtain ⟨Λ, X, Y, rfl, rfl⟩ := exists_ofM₂ a b
    rw [← ofM_add, nrm_ofM, nrm_ofM, nrm_ofM]
    exact norm_add_le X Y
  neg' a := by
    obtain ⟨Λ, X, rfl⟩ := exists_ofM a
    rw [← ofM_neg, nrm_ofM, nrm_ofM, norm_neg]
  eq_zero_of_map_eq_zero' a h := by
    obtain ⟨Λ, X, rfl⟩ := exists_ofM a
    rw [nrm_ofM] at h
    rw [norm_eq_zero.mp h, ofM_zero]

noncomputable instance instNormedAddCommGroupLocal : NormedAddCommGroup (localAlg ι Q) :=
  localNorm.toNormedAddCommGroup

theorem norm_ofM (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) : ‖ofM Λ X‖ = ‖X‖ :=
  nrm_ofM Λ X

noncomputable instance instNormedRingLocal : NormedRing (localAlg ι Q) where
  __ := (inferInstance : NormedAddCommGroup (localAlg ι Q))
  __ := (inferInstance : Ring (localAlg ι Q))
  norm_mul_le a b := by
    obtain ⟨Λ, X, Y, rfl, rfl⟩ := exists_ofM₂ a b
    rw [← ofM_mul, norm_ofM, norm_ofM, norm_ofM]
    exact norm_mul_le X Y

noncomputable instance instNormedAlgebraLocal : NormedAlgebra ℂ (localAlg ι Q) where
  __ := (inferInstance : Algebra ℂ (localAlg ι Q))
  norm_smul_le c a := by
    obtain ⟨Λ, X, rfl⟩ := exists_ofM a
    rw [← ofM_smul, norm_ofM, norm_ofM, norm_smul]

noncomputable instance instStarRingLocal : StarRing (localAlg ι Q) where
  star_involutive a := by
    obtain ⟨Λ, X, rfl⟩ := exists_ofM a
    rw [star_ofM, star_ofM, Matrix.conjTranspose_conjTranspose]
  star_mul a b := by
    obtain ⟨Λ, X, Y, rfl, rfl⟩ := exists_ofM₂ a b
    rw [← ofM_mul, star_ofM, star_ofM, star_ofM, ← ofM_mul, Matrix.conjTranspose_mul]
  star_add a b := by
    obtain ⟨Λ, X, Y, rfl, rfl⟩ := exists_ofM₂ a b
    rw [← ofM_add, star_ofM, star_ofM, star_ofM, ← ofM_add, Matrix.conjTranspose_add]

noncomputable instance instStarModuleLocal : StarModule ℂ (localAlg ι Q) where
  star_smul c a := by
    obtain ⟨Λ, X, rfl⟩ := exists_ofM a
    rw [← ofM_smul, star_ofM, star_ofM, ← ofM_smul, Matrix.conjTranspose_smul]

/-- **THE C*-IDENTITY ON THE LOCAL ALGEBRA**, inherited from the finite stages. -/
noncomputable instance instCStarRingLocal : CStarRing (localAlg ι Q) where
  norm_mul_self_le a := by
    obtain ⟨Λ, X, rfl⟩ := exists_ofM a
    rw [star_ofM, ← ofM_mul, norm_ofM, norm_ofM]
    exact CStarRing.norm_mul_self_le X

theorem isometry_star_local : Isometry (star : localAlg ι Q → localAlg ι Q) :=
  Isometry.of_dist_eq fun a b => by rw [dist_eq_norm, dist_eq_norm, ← star_sub, norm_star]

/-- **THE QUASILOCAL ALGEBRA**: the norm completion of the local algebra. -/
abbrev Quasilocal (ι Q : Type) [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q] :=
  UniformSpace.Completion (localAlg ι Q)

noncomputable instance instNormedAlgebraQuasilocal : NormedAlgebra ℂ (Quasilocal ι Q) where
  __ := UniformSpace.Completion.algebra (localAlg ι Q) ℂ
  norm_smul_le := norm_smul_le

/-- The involution of the completion: the continuous extension of the involution. -/
noncomputable instance instStarQuasilocal : Star (Quasilocal ι Q) :=
  ⟨UniformSpace.Completion.map star⟩

theorem star_coe (a : localAlg ι Q) :
    star (a : Quasilocal ι Q) = ((star a : localAlg ι Q) : Quasilocal ι Q) :=
  UniformSpace.Completion.map_coe isometry_star_local.uniformContinuous a

theorem continuous_star_q : Continuous (star : Quasilocal ι Q → Quasilocal ι Q) :=
  UniformSpace.Completion.continuous_map

noncomputable instance instStarRingQuasilocal : StarRing (Quasilocal ι Q) where
  star_involutive x := by
    refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
    · exact isClosed_eq (continuous_star_q.comp continuous_star_q) continuous_id
    · rw [star_coe, star_coe, star_star]
  star_mul x y := by
    refine UniformSpace.Completion.induction_on₂ x y ?_ fun a b => ?_
    · exact isClosed_eq (continuous_star_q.comp continuous_mul)
        ((continuous_star_q.comp continuous_snd).mul (continuous_star_q.comp continuous_fst))
    · rw [← UniformSpace.Completion.coe_mul, star_coe, star_coe, star_coe, star_mul,
        UniformSpace.Completion.coe_mul]
  star_add x y := by
    refine UniformSpace.Completion.induction_on₂ x y ?_ fun a b => ?_
    · exact isClosed_eq (continuous_star_q.comp continuous_add)
        ((continuous_star_q.comp continuous_fst).add (continuous_star_q.comp continuous_snd))
    · rw [← UniformSpace.Completion.coe_add, star_coe, star_coe, star_coe, star_add,
        UniformSpace.Completion.coe_add]

noncomputable instance instStarModuleQuasilocal : StarModule ℂ (Quasilocal ι Q) where
  star_smul c x := by
    refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
    · exact isClosed_eq (continuous_star_q.comp (continuous_const_smul c))
        ((continuous_const_smul (star c)).comp continuous_star_q)
    · rw [← UniformSpace.Completion.coe_smul, star_coe, star_coe, star_smul,
        UniformSpace.Completion.coe_smul]

/-- **THE C*-IDENTITY ON THE COMPLETION**, by density. -/
noncomputable instance instCStarRingQuasilocal : CStarRing (Quasilocal ι Q) where
  norm_mul_self_le x := by
    refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
    · exact isClosed_le (continuous_norm.mul continuous_norm)
        (continuous_norm.comp (continuous_star_q.mul continuous_id))
    · rw [star_coe, ← UniformSpace.Completion.coe_mul, UniformSpace.Completion.norm_coe,
        UniformSpace.Completion.norm_coe]
      exact CStarRing.norm_mul_self_le a

/-- **THE QUASILOCAL ALGEBRA IS A C*-ALGEBRA.** -/
noncomputable instance instCStarAlgebraQuasilocal : CStarAlgebra (Quasilocal ι Q) :=
  CStarAlgebra.mk

/-- The finite stage embedded in the quasilocal algebra, as a star algebra homomorphism. -/
noncomputable def stage (Λ : Finset ι) :
    Matrix (Conf Λ Q) (Conf Λ Q) ℂ →⋆ₐ[ℂ] Quasilocal ι Q where
  toFun X := ((ofM Λ X : localAlg ι Q) : Quasilocal ι Q)
  map_one' := by rw [ofM_one, UniformSpace.Completion.coe_one]
  map_mul' X Y := by rw [ofM_mul, UniformSpace.Completion.coe_mul]
  map_zero' := by rw [ofM_zero, UniformSpace.Completion.coe_zero]
  map_add' X Y := by rw [ofM_add, UniformSpace.Completion.coe_add]
  commutes' c := by
    rw [Algebra.algebraMap_eq_smul_one, ofM_smul, ofM_one, UniformSpace.Completion.coe_smul,
      UniformSpace.Completion.coe_one, Algebra.algebraMap_eq_smul_one]
  map_star' X := by rw [Matrix.star_eq_conjTranspose, star_coe, star_ofM]

theorem stage_apply (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    stage Λ X = ((ofM Λ X : localAlg ι Q) : Quasilocal ι Q) := rfl

/-- **THE STAGES ARE COMPATIBLE**: the inclusions commute with the embeddings. -/
theorem stage_inclObs {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    stage Λ' (inclObs h X) = stage Λ X := by
  rw [stage_apply, stage_apply, ofM_inclObs]

/-- **THE STAGES ARE ISOMETRIC.** -/
theorem norm_stage (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) : ‖stage Λ X‖ = ‖X‖ := by
  rw [stage_apply, UniformSpace.Completion.norm_coe, norm_ofM]

theorem stage_injective (Λ : Finset ι) : Function.Injective (stage Λ (ι := ι) (Q := Q)) :=
  fun _ _ h => ofM_injective Λ (UniformSpace.Completion.coe_injective _ h)

/-- **THE QUASILOCAL ALGEBRA IS THE CLOSURE OF THE UNION OF THE FINITE STAGES.** -/
theorem closure_iUnion_stage :
    closure (⋃ Λ : Finset ι, Set.range (stage Λ (Q := Q))) = (Set.univ : Set (Quasilocal ι Q)) := by
  have h : (⋃ Λ : Finset ι, Set.range (stage Λ (Q := Q)))
      = Set.range ((↑) : localAlg ι Q → Quasilocal ι Q) := by
    ext x
    simp only [Set.mem_iUnion, Set.mem_range]
    constructor
    · rintro ⟨Λ, X, rfl⟩
      exact ⟨ofM Λ X, rfl⟩
    · rintro ⟨a, rfl⟩
      obtain ⟨Λ, X, rfl⟩ := exists_ofM a
      exact ⟨Λ, X, rfl⟩
  rw [h]
  exact UniformSpace.Completion.denseRange_coe.closure_range

end Norm

/-! ### Section C — consistent state families are states of the quasilocal algebra -/

section States

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]

open scoped MatrixOrder

/-- **A STATE FAMILY**: a consistent family of density matrices, one on every region. -/
structure IsStateFamily (ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ) : Prop where
  consistent : Consistent ρ
  posSemidef : ∀ Λ, (ρ Λ).PosSemidef
  trace_one : ∀ Λ, (ρ Λ).trace = 1

/-- The value of a family on a local element: the trace pairing with any representative. -/
noncomputable def evalLocal (ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ)
    (a : localAlg ι Q) : ℂ :=
  ((rep a).2 * ρ (rep a).1).trace

/-- **WELL-DEFINED**: for a consistent family the value does not depend on the representative,
by the duality of inclusion and restriction. -/
theorem evalLocal_ofM {ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ} (hρ : Consistent ρ)
    (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    evalLocal ρ (ofM Λ X) = (X * ρ Λ).trace := by
  have h := ofM_rep (ofM Λ X)
  rw [ofM_eq_iff] at h
  unfold evalLocal
  have h₀ : (rep (ofM Λ X)).1 ⊆ (rep (ofM Λ X)).1 ∪ Λ := Finset.subset_union_left
  have h₁ : Λ ⊆ (rep (ofM Λ X)).1 ∪ Λ := Finset.subset_union_right
  rw [← hρ _ _ h₀, ← trace_inclObs_mul_restrict, h, trace_inclObs_mul_restrict, hρ _ _ h₁]

theorem evalLocal_add {ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ} (hρ : Consistent ρ)
    (a b : localAlg ι Q) : evalLocal ρ (a + b) = evalLocal ρ a + evalLocal ρ b := by
  obtain ⟨Λ, X, Y, rfl, rfl⟩ := exists_ofM₂ a b
  rw [← ofM_add, evalLocal_ofM hρ, evalLocal_ofM hρ, evalLocal_ofM hρ, Matrix.add_mul,
    Matrix.trace_add]

theorem evalLocal_smul {ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ} (hρ : Consistent ρ)
    (c : ℂ) (a : localAlg ι Q) : evalLocal ρ (c • a) = c * evalLocal ρ a := by
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [← ofM_smul, evalLocal_ofM hρ, evalLocal_ofM hρ, Matrix.smul_mul, Matrix.trace_smul,
    smul_eq_mul]

/-- The value of a consistent family as a linear functional on the local algebra. -/
noncomputable def localStateₗ {ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ}
    (hρ : Consistent ρ) : localAlg ι Q →ₗ[ℂ] ℂ where
  toFun := evalLocal ρ
  map_add' := evalLocal_add hρ
  map_smul' c a := by rw [evalLocal_smul hρ, RingHom.id_apply, smul_eq_mul]

theorem evalLocal_one {ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ}
    (hρ : IsStateFamily ρ) : evalLocal ρ 1 = 1 := by
  rw [← ofM_one (∅ : Finset ι), evalLocal_ofM hρ.consistent, Matrix.one_mul, hρ.trace_one]

theorem trace_mul_nonneg_of_posSemidef {Λ : Finset ι} {σ : Matrix (Conf Λ Q) (Conf Λ Q) ℂ}
    (hσ : σ.PosSemidef) {X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ} (hX : 0 ≤ X) :
    0 ≤ (X * σ).trace := by
  obtain ⟨B, rfl⟩ := CStarAlgebra.nonneg_iff_eq_star_mul_self.mp hX
  rw [Matrix.star_eq_conjTranspose, Matrix.mul_assoc, Matrix.trace_mul_comm]
  exact (hσ.mul_mul_conjTranspose_same B).trace_nonneg

/-- **POSITIVITY** on the local algebra. -/
theorem evalLocal_nonneg {ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ}
    (hρ : IsStateFamily ρ) (a : localAlg ι Q) : 0 ≤ evalLocal ρ (star a * a) := by
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [star_ofM, ← ofM_mul, evalLocal_ofM hρ.consistent, Matrix.mul_assoc, Matrix.trace_mul_comm]
  exact ((hρ.posSemidef Λ).mul_mul_conjTranspose_same X).trace_nonneg

/-- The trace pairing with a density matrix as a positive linear functional on a finite stage. -/
noncomputable def stageFunctional {Λ : Finset ι} (σ : Matrix (Conf Λ Q) (Conf Λ Q) ℂ)
    (hσ : σ.PosSemidef) : Matrix (Conf Λ Q) (Conf Λ Q) ℂ →ₚ[ℂ] ℂ where
  toFun X := (X * σ).trace
  map_add' X Y := by simp only [Matrix.add_mul, Matrix.trace_add]
  map_smul' c X := by simp only [Matrix.smul_mul, Matrix.trace_smul, RingHom.id_apply]
  monotone' X Y hXY := by
    have h : 0 ≤ ((Y - X) * σ).trace :=
      trace_mul_nonneg_of_posSemidef hσ (sub_nonneg.mpr hXY)
    rw [Matrix.sub_mul, Matrix.trace_sub] at h
    exact sub_nonneg.mp h

/-- **BOUNDEDNESS** at a finite stage, with an explicit constant, from the positivity of the
functional (four positive parts, each bounded by the value at the identity). -/
theorem norm_trace_mul_le {Λ : Finset ι} {σ : Matrix (Conf Λ Q) (Conf Λ Q) ℂ}
    (hσ : σ.PosSemidef) (htr : σ.trace = 1) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    ‖(X * σ).trace‖ ≤ 4 * ‖X‖ := by
  obtain ⟨y, hy0, hyn, hXy⟩ := CStarAlgebra.exists_sum_four_nonneg X
  have h1 : ‖stageFunctional σ hσ 1‖ = 1 := by
    show ‖((1 : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) * σ).trace‖ = 1
    rw [Matrix.one_mul, htr, norm_one]
  calc ‖(X * σ).trace‖ = ‖stageFunctional σ hσ X‖ := rfl
    _ = ‖∑ i : Fin 4, Complex.I ^ (i : ℕ) • stageFunctional σ hσ (y i)‖ := by
        conv_lhs => rw [hXy]
        rw [map_sum]
        simp only [map_smul]
    _ ≤ ∑ i : Fin 4, ‖Complex.I ^ (i : ℕ) • stageFunctional σ hσ (y i)‖ := norm_sum_le _ _
    _ = ∑ i : Fin 4, ‖stageFunctional σ hσ (y i)‖ := by
        simp only [norm_smul, norm_pow, Complex.norm_I, one_pow, one_mul]
    _ ≤ ∑ _i : Fin 4, ‖X‖ := Finset.sum_le_sum fun i _ =>
        (PositiveLinearMap.norm_apply_le_of_nonneg _ _ (hy0 i)).trans
          (by rw [h1, one_mul]; exact hyn i)
    _ = 4 * ‖X‖ := by simp

theorem norm_evalLocal_le {ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ}
    (hρ : IsStateFamily ρ) (a : localAlg ι Q) : ‖evalLocal ρ a‖ ≤ 4 * ‖a‖ := by
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [evalLocal_ofM hρ.consistent, norm_ofM]
  exact norm_trace_mul_le (hρ.posSemidef Λ) (hρ.trace_one Λ) X

/-- The state of a family on the local algebra, as a continuous linear functional. -/
noncomputable def localState {ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ}
    (hρ : IsStateFamily ρ) : localAlg ι Q →L[ℂ] ℂ :=
  LinearMap.mkContinuous (localStateₗ hρ.consistent) 4 (norm_evalLocal_le hρ)

theorem localState_apply {ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ}
    (hρ : IsStateFamily ρ) (a : localAlg ι Q) : localState hρ a = evalLocal ρ a := rfl

/-- **THE STATE OF THE QUASILOCAL ALGEBRA**: the unique continuous extension of the family's
functional along the dense isometric embedding of the local algebra. -/
noncomputable def quasiState {ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ}
    (hρ : IsStateFamily ρ) : Quasilocal ι Q →L[ℂ] ℂ :=
  (localState hρ).extend UniformSpace.Completion.toComplL

theorem quasiState_coe {ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ}
    (hρ : IsStateFamily ρ) (a : localAlg ι Q) :
    quasiState hρ (a : Quasilocal ι Q) = evalLocal ρ a :=
  ContinuousLinearMap.extend_eq _ UniformSpace.Completion.denseRange_coe
    (UniformSpace.Completion.isUniformInducing_coe _) a

/-- On a finite stage the extended state is the trace pairing with the family's density. -/
theorem quasiState_stage {ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ}
    (hρ : IsStateFamily ρ) (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    quasiState hρ (stage Λ X) = (X * ρ Λ).trace := by
  rw [stage_apply, quasiState_coe, evalLocal_ofM hρ.consistent]

theorem quasiState_one {ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ}
    (hρ : IsStateFamily ρ) : quasiState hρ 1 = 1 := by
  rw [← UniformSpace.Completion.coe_one, quasiState_coe]
  exact evalLocal_one hρ

/-- **POSITIVITY ON THE COMPLETION**, by density. -/
theorem quasiState_nonneg {ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ}
    (hρ : IsStateFamily ρ) (x : Quasilocal ι Q) : 0 ≤ quasiState hρ (star x * x) := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_le continuous_const
      ((quasiState hρ).continuous.comp (continuous_star_q.mul continuous_id))
  · rw [star_coe, ← UniformSpace.Completion.coe_mul, quasiState_coe]
    exact evalLocal_nonneg hρ a

/-- **UNIQUENESS**: any continuous functional agreeing with the family on the local algebra is
the extended state. -/
theorem quasiState_unique {ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ}
    (hρ : IsStateFamily ρ) (g : Quasilocal ι Q →L[ℂ] ℂ)
    (hg : ∀ a : localAlg ι Q, g a = evalLocal ρ a) : g = quasiState hρ :=
  (ContinuousLinearMap.extend_unique (localState hρ) (e := UniformSpace.Completion.toComplL)
    UniformSpace.Completion.denseRange_coe (UniformSpace.Completion.isUniformInducing_coe _) g
    (ContinuousLinearMap.ext fun a => hg a)).symm

/-- The reference family of the second entry is a state family. -/
theorem uniformFamily_isStateFamily : IsStateFamily (uniformFamily ι Q) where
  consistent := uniform_family_consistent
  posSemidef Λ := by
    unfold uniformFamily
    refine Matrix.PosSemidef.one.smul ?_
    rw [show ((Fintype.card (Conf Λ Q) : ℂ))⁻¹ = (((Fintype.card (Conf Λ Q) : ℝ)⁻¹ : ℝ) : ℂ) by
      rw [Complex.ofReal_inv, Complex.ofReal_natCast]]
    exact Complex.zero_le_real.mpr (inv_nonneg.mpr (Nat.cast_nonneg _))
  trace_one Λ := by
    unfold uniformFamily
    rw [Matrix.trace_smul, Matrix.trace_one, smul_eq_mul]
    exact inv_mul_cancel₀ (by exact_mod_cast Fintype.card_ne_zero)

/-- **THE REFERENCE STATE OF THE QUASILOCAL ALGEBRA**: the extension of the uniform family. -/
noncomputable def referenceState : Quasilocal ι Q →L[ℂ] ℂ :=
  quasiState (uniformFamily_isStateFamily (ι := ι) (Q := Q))

theorem referenceState_stage (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    referenceState (stage Λ X) = ((Fintype.card (Conf Λ Q) : ℂ))⁻¹ * X.trace := by
  rw [referenceState, quasiState_stage, uniformFamily, Matrix.mul_smul, Matrix.mul_one,
    Matrix.trace_smul, smul_eq_mul]

end States

/-! ### Section D — finite-range reversible dynamics on the local and quasilocal algebra -/

section Dynamics

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]

/-- A finite-range update: each site's next value depends on a finite neighbourhood (the
coupling graph of the second entry), and each site influences only finitely many sites. -/
structure FiniteRange (ψ : (ι → Q) → (ι → Q)) extends CouplingGraph ψ where
  infl : ι → Finset ι
  mem_infl : ∀ i j, i ∈ nbhd j → j ∈ infl i

/-- The backward cone of a region: the sites its next values depend on. -/
def bwd {ψ : (ι → Q) → (ι → Q)} (G : FiniteRange ψ) (A : Finset ι) : Finset ι :=
  A.biUnion G.nbhd

/-- The forward cone of a region: the sites it can influence in one step. -/
def fwd {ψ : (ι → Q) → (ι → Q)} (G : FiniteRange ψ) (A : Finset ι) : Finset ι :=
  A.biUnion G.infl

/-- Configurations agreeing on the backward cone of `B` update to configurations agreeing
on `B`. -/
theorem glob_map_eq {ψ : (ι → Q) → (ι → Q)} (G : FiniteRange ψ) (B : Finset ι) {t t' : ι → Q}
    (h : ∀ i ∈ bwd G B, t i = t' i) : glob B (ψ t) = glob B (ψ t') := by
  funext x
  apply G.local_dep x.1
  intro y hy
  exact h y (Finset.mem_biUnion.mpr ⟨x.1, x.2, hy⟩)

/-- **FORWARD LOCALITY**: configurations agreeing off `A` update to configurations agreeing off
the forward cone of `A`. -/
theorem agreeOffG_map {ψ : (ι → Q) → (ι → Q)} (G : FiniteRange ψ) (A : Finset ι) {u u' : ι → Q}
    (h : AgreeOffG A u u') : AgreeOffG (fwd G A) (ψ u) (ψ u') := by
  intro j hj
  apply G.local_dep j
  intro i hi
  apply h i
  intro hiA
  exact hj (Finset.mem_biUnion.mpr ⟨i, hiA, G.mem_infl i j hi⟩)

theorem agreeOffG_mono {A B : Finset ι} (hAB : A ⊆ B) {t s : ι → Q} (h : AgreeOffG A t s) :
    AgreeOffG B t s := fun i hi => h i (fun hiA => hi (hAB hiA))

/-- **A REVERSIBLE FINITE-RANGE DYNAMICS**: a bijection of global configurations whose update
and whose inverse are both of finite range. -/
structure ReversibleDynamics (ι Q : Type) where
  φ : (ι → Q) ≃ (ι → Q)
  G : FiniteRange (φ : (ι → Q) → (ι → Q))
  G' : FiniteRange (φ.symm : (ι → Q) → (ι → Q))

/-- The inverse dynamics. -/
def ReversibleDynamics.inv (Φ : ReversibleDynamics ι Q) : ReversibleDynamics ι Q :=
  ⟨Φ.φ.symm, Φ.G', Φ.G⟩

/-- The permutation operator of the dynamics on the scaffold. -/
noncomputable def permOp (Φ : ReversibleDynamics ι Q) : Module.End ℂ (Scaffold ι Q) :=
  Finsupp.lmapDomain ℂ ℂ Φ.φ

/-- The permutation operator of the inverse dynamics. -/
noncomputable def permOpInv (Φ : ReversibleDynamics ι Q) : Module.End ℂ (Scaffold ι Q) :=
  Finsupp.lmapDomain ℂ ℂ Φ.φ.symm

theorem permOp_single (Φ : ReversibleDynamics ι Q) (s : ι → Q) (c : ℂ) :
    permOp Φ (Finsupp.single s c) = Finsupp.single (Φ.φ s) c := by
  rw [permOp, Finsupp.lmapDomain_apply, Finsupp.mapDomain_single]

theorem permOpInv_single (Φ : ReversibleDynamics ι Q) (s : ι → Q) (c : ℂ) :
    permOpInv Φ (Finsupp.single s c) = Finsupp.single (Φ.φ.symm s) c := by
  rw [permOpInv, Finsupp.lmapDomain_apply, Finsupp.mapDomain_single]

theorem permOpInv_apply (Φ : ReversibleDynamics ι Q) (f : Scaffold ι Q) (t : ι → Q) :
    permOpInv Φ f t = f (Φ.φ t) := by
  rw [permOpInv, Finsupp.lmapDomain_apply, Finsupp.mapDomain_equiv_apply, Equiv.symm_symm]

theorem permOp_permOpInv (Φ : ReversibleDynamics ι Q) : permOp Φ * permOpInv Φ = 1 := by
  apply Finsupp.lhom_ext
  intro s c
  rw [Module.End.mul_apply, permOpInv_single, permOp_single, Equiv.apply_symm_apply,
    Module.End.one_apply]

theorem permOpInv_permOp (Φ : ReversibleDynamics ι Q) : permOpInv Φ * permOp Φ = 1 := by
  apply Finsupp.lhom_ext
  intro s c
  rw [Module.End.mul_apply, permOp_single, permOpInv_single, Equiv.symm_apply_apply,
    Module.End.one_apply]

/-- **THE HEISENBERG ACTION** of the dynamics on scaffold operators: conjugation by the
permutation operator. -/
noncomputable def heis (Φ : ReversibleDynamics ι Q) (T : Module.End ℂ (Scaffold ι Q)) :
    Module.End ℂ (Scaffold ι Q) :=
  permOpInv Φ * T * permOp Φ

theorem heis_mul (Φ : ReversibleDynamics ι Q) (T T' : Module.End ℂ (Scaffold ι Q)) :
    heis Φ (T * T') = heis Φ T * heis Φ T' := by
  unfold heis
  simp only [mul_assoc]
  rw [← mul_assoc (permOp Φ) (permOpInv Φ), permOp_permOpInv, one_mul]

theorem heis_one (Φ : ReversibleDynamics ι Q) : heis Φ 1 = 1 := by
  rw [heis, mul_one, permOpInv_permOp]

theorem heis_add (Φ : ReversibleDynamics ι Q) (T T' : Module.End ℂ (Scaffold ι Q)) :
    heis Φ (T + T') = heis Φ T + heis Φ T' := by
  simp only [heis, mul_add, add_mul]

theorem heis_smul (Φ : ReversibleDynamics ι Q) (c : ℂ) (T : Module.End ℂ (Scaffold ι Q)) :
    heis Φ (c • T) = c • heis Φ T := by
  simp only [heis, mul_smul_comm, smul_mul_assoc]

theorem heis_inv_heis (Φ : ReversibleDynamics ι Q) (T : Module.End ℂ (Scaffold ι Q)) :
    heis Φ.inv (heis Φ T) = T := by
  have h1 : permOpInv Φ.inv = permOp Φ := by
    simp only [permOpInv, permOp, ReversibleDynamics.inv, Equiv.symm_symm]
  have h2 : permOp Φ.inv = permOpInv Φ := rfl
  rw [heis, heis, h1, h2]
  simp only [mul_assoc]
  rw [permOp_permOpInv, mul_one, ← mul_assoc, permOp_permOpInv, one_mul]

theorem heis_injective (Φ : ReversibleDynamics ι Q) : Function.Injective (heis Φ) :=
  fun T T' h => by rw [← heis_inv_heis Φ T, h, heis_inv_heis]

/-- The kernel of the transported operator is the kernel at the updated configurations. -/
theorem kerOf_heis (Φ : ReversibleDynamics ι Q) (T : Module.End ℂ (Scaffold ι Q)) (t s : ι → Q) :
    kerOf (heis Φ T) t s = kerOf T (Φ.φ t) (Φ.φ s) := by
  rw [kerOf, kerOf, heis, Module.End.mul_apply, Module.End.mul_apply, permOp_single,
    permOpInv_apply]

/-- The region carrying the transport of a region: the forward cone of the inverse together
with the backward cones needed to determine the transported entries. -/
def hat (Φ : ReversibleDynamics ι Q) (Λ : Finset ι) : Finset ι :=
  fwd Φ.G' Λ ∪ bwd Φ.G Λ ∪ bwd Φ.G (bwd Φ.G' (fwd Φ.G' Λ))

theorem fwd_subset_hat (Φ : ReversibleDynamics ι Q) (Λ : Finset ι) : fwd Φ.G' Λ ⊆ hat Φ Λ :=
  Finset.subset_union_left.trans Finset.subset_union_left

theorem bwd_subset_hat (Φ : ReversibleDynamics ι Q) (Λ : Finset ι) : bwd Φ.G Λ ⊆ hat Φ Λ :=
  Finset.subset_union_right.trans Finset.subset_union_left

theorem bwd_bwd_subset_hat (Φ : ReversibleDynamics ι Q) (Λ : Finset ι) :
    bwd Φ.G (bwd Φ.G' (fwd Φ.G' Λ)) ⊆ hat Φ Λ :=
  Finset.subset_union_right

/-- The target configuration of a transported matrix unit. -/
noncomputable def target (Φ : ReversibleDynamics ι Q) (Λ : Finset ι) (s : ι → Q)
    (f : Conf Λ Q) : Conf (hat Φ Λ) Q :=
  glob (hat Φ Λ) (Φ.φ.symm (patch Λ (Φ.φ s) f))

/-- The transported matrix unit lands on a patch of the hat region. -/
theorem symm_patch_eq_patch (Φ : ReversibleDynamics ι Q) (Λ : Finset ι) (s : ι → Q)
    (f : Conf Λ Q) :
    Φ.φ.symm (patch Λ (Φ.φ s) f) = patch (hat Φ Λ) s (target Φ Λ s f) := by
  apply eq_patch_of_agreeOffG
  have h := agreeOffG_map Φ.G' Λ (agreeOffG_patch Λ (Φ.φ s) f)
  rw [Equiv.symm_apply_apply] at h
  exact agreeOffG_mono (fwd_subset_hat Φ Λ) h

/-- A default global extension of a configuration of a region. -/
noncomputable def ext (Λ : Finset ι) (h : Conf Λ Q) : ι → Q :=
  patch Λ (fun _ => Classical.arbitrary Q) h

theorem glob_ext (Λ : Finset ι) (h : Conf Λ Q) : glob Λ (ext Λ h) = h := glob_patch _ _ _

/-- **THE TRANSPORTED ENTRIES DEPEND ONLY ON THE HAT REGION** (the update part). -/
theorem glob_map_of_glob_eq (Φ : ReversibleDynamics ι Q) (Λ : Finset ι) {s s' : ι → Q}
    (h : glob (hat Φ Λ) s = glob (hat Φ Λ) s') : glob Λ (Φ.φ s) = glob Λ (Φ.φ s') := by
  apply glob_map_eq Φ.G Λ
  intro i hi
  exact congrFun h ⟨i, bwd_subset_hat Φ Λ hi⟩

/-- **THE TRANSPORTED ENTRIES DEPEND ONLY ON THE HAT REGION** (the target part). -/
theorem target_of_glob_eq (Φ : ReversibleDynamics ι Q) (Λ : Finset ι) {s s' : ι → Q}
    (h : glob (hat Φ Λ) s = glob (hat Φ Λ) s') (f : Conf Λ Q) :
    target Φ Λ s f = target Φ Λ s' f := by
  have hs : ∀ i ∈ hat Φ Λ, s i = s' i := fun i hi => congrFun h ⟨i, hi⟩
  funext x
  simp only [target, glob]
  by_cases hx : x.1 ∈ fwd Φ.G' Λ
  · -- inside the forward cone: the inverse update depends on the backward cone of the cone
    have hmap : glob (fwd Φ.G' Λ) (Φ.φ.symm (patch Λ (Φ.φ s) f))
        = glob (fwd Φ.G' Λ) (Φ.φ.symm (patch Λ (Φ.φ s') f)) := by
      apply glob_map_eq Φ.G'
      intro j hj
      by_cases hjΛ : j ∈ Λ
      · rw [patch_apply_of_mem hjΛ, patch_apply_of_mem hjΛ]
      · rw [patch_apply_of_not_mem hjΛ, patch_apply_of_not_mem hjΛ]
        have hg := glob_map_eq Φ.G (bwd Φ.G' (fwd Φ.G' Λ)) (t := s) (t' := s')
          (fun i hi => hs i (bwd_bwd_subset_hat Φ Λ hi))
        exact congrFun hg ⟨j, hj⟩
    exact congrFun hmap ⟨x.1, hx⟩
  · -- outside the forward cone: the transported configuration agrees with the original
    have h1 := agreeOffG_map Φ.G' Λ (agreeOffG_patch Λ (Φ.φ s) f)
    have h2 := agreeOffG_map Φ.G' Λ (agreeOffG_patch Λ (Φ.φ s') f)
    rw [Equiv.symm_apply_apply] at h1 h2
    rw [h1 x.1 hx, h2 x.1 hx]
    exact hs x.1 x.2

/-- **THE TRANSPORTED OBSERVABLE**: the matrix on the hat region whose operator is the Heisenberg
transport of the operator of `X`. -/
noncomputable def transported (Φ : ReversibleDynamics ι Q) (Λ : Finset ι)
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) : Matrix (Conf (hat Φ Λ) Q) (Conf (hat Φ Λ) Q) ℂ :=
  fun g h => ∑ f ∈ Finset.univ.filter (fun f : Conf Λ Q => target Φ Λ (ext (hat Φ Λ) h) f = g),
    X f (glob Λ (Φ.φ (ext (hat Φ Λ) h)))

theorem heis_emb_single (Φ : ReversibleDynamics ι Q) (Λ : Finset ι)
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) (s : ι → Q) (c : ℂ) :
    heis Φ (emb Λ X) (Finsupp.single s c)
      = c • ∑ f : Conf Λ Q, X f (glob Λ (Φ.φ s)) •
          Finsupp.single (patch (hat Φ Λ) s (target Φ Λ s f)) (1 : ℂ) := by
  rw [heis, Module.End.mul_apply, Module.End.mul_apply, permOp_single, emb_single, map_smul,
    map_sum]
  congr 1
  refine Finset.sum_congr rfl fun f _ => ?_
  rw [map_smul, permOpInv_single, symm_patch_eq_patch]

/-- **ONE-STEP LOCALIZATION**: the Heisenberg transport of a local observable of `Λ` is a local
observable of the hat region. -/
theorem heis_emb (Φ : ReversibleDynamics ι Q) (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    heis Φ (emb Λ X) = emb (hat Φ Λ) (transported Φ Λ X) := by
  apply Finsupp.lhom_ext
  intro s c
  rw [heis_emb_single, emb_single]
  congr 1
  have hg : glob (hat Φ Λ) (ext (hat Φ Λ) (glob (hat Φ Λ) s)) = glob (hat Φ Λ) s := glob_ext _ _
  have hX : glob Λ (Φ.φ (ext (hat Φ Λ) (glob (hat Φ Λ) s))) = glob Λ (Φ.φ s) :=
    glob_map_of_glob_eq Φ Λ hg
  have hT : ∀ f, target Φ Λ (ext (hat Φ Λ) (glob (hat Φ Λ) s)) f = target Φ Λ s f :=
    fun f => target_of_glob_eq Φ Λ hg f
  simp only [transported, hX, hT, Finset.sum_smul]
  refine (Finset.sum_fiberwise Finset.univ (fun f => target Φ Λ s f)
    (fun f => X f (glob Λ (Φ.φ s)) •
      Finsupp.single (patch (hat Φ Λ) s (target Φ Λ s f)) (1 : ℂ))).symm.trans ?_
  refine Finset.sum_congr rfl fun g _ => Finset.sum_congr rfl fun f hf => ?_
  rw [(Finset.mem_filter.mp hf).2]

theorem emb_transported (Φ : ReversibleDynamics ι Q) (Λ : Finset ι)
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    emb (hat Φ Λ) (transported Φ Λ X) = heis Φ (emb Λ X) := (heis_emb Φ Λ X).symm

theorem transported_add (Φ : ReversibleDynamics ι Q) (Λ : Finset ι)
    (X Y : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    transported Φ Λ (X + Y) = transported Φ Λ X + transported Φ Λ Y := by
  apply emb_injective
  rw [emb_add, emb_transported, emb_transported, emb_transported, emb_add, heis_add]

theorem transported_smul (Φ : ReversibleDynamics ι Q) (Λ : Finset ι) (c : ℂ)
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    transported Φ Λ (c • X) = c • transported Φ Λ X := by
  apply emb_injective
  rw [emb_smul, emb_transported, emb_transported, emb_smul, heis_smul]

theorem transported_mul (Φ : ReversibleDynamics ι Q) (Λ : Finset ι)
    (X Y : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    transported Φ Λ (X * Y) = transported Φ Λ X * transported Φ Λ Y := by
  apply emb_injective
  rw [emb_mul, emb_transported, emb_transported, emb_transported, emb_mul, heis_mul]

theorem transported_one (Φ : ReversibleDynamics ι Q) (Λ : Finset ι) :
    transported Φ Λ (1 : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) = 1 := by
  apply emb_injective
  rw [emb_transported, emb_one, heis_one, emb_one]

/-- The transport commutes with the involution. -/
theorem transported_conjTranspose (Φ : ReversibleDynamics ι Q) (Λ : Finset ι)
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    transported Φ Λ Xᴴ = (transported Φ Λ X)ᴴ := by
  apply emb_injective
  apply ext_of_kerOf
  funext t s
  have h1 : kerOf (emb (hat Φ Λ) (transported Φ Λ Xᴴ)) t s
      = star (kern Λ X (Φ.φ s) (Φ.φ t)) := by
    rw [emb_transported, kerOf_heis, kerOf_emb, kern_conjTranspose]
  have h2 : kerOf (emb (hat Φ Λ) (transported Φ Λ X)ᴴ) t s
      = star (kern Λ X (Φ.φ s) (Φ.φ t)) := by
    rw [kerOf_emb, kern_conjTranspose, ← kerOf_emb, emb_transported, kerOf_heis, kerOf_emb]
  rw [h1, h2]

theorem transported_injective (Φ : ReversibleDynamics ι Q) (Λ : Finset ι) :
    Function.Injective (transported Φ Λ) := fun X Y h => by
  apply emb_injective Λ
  apply heis_injective Φ
  rw [← emb_transported, ← emb_transported, h]

/-- The transport as a star algebra homomorphism between finite stages. -/
noncomputable def transportedHom (Φ : ReversibleDynamics ι Q) (Λ : Finset ι) :
    Matrix (Conf Λ Q) (Conf Λ Q) ℂ →⋆ₐ[ℂ] Matrix (Conf (hat Φ Λ) Q) (Conf (hat Φ Λ) Q) ℂ where
  toFun := transported Φ Λ
  map_one' := transported_one Φ Λ
  map_mul' := transported_mul Φ Λ
  map_zero' := by
    rw [← zero_smul ℂ (0 : Matrix (Conf Λ Q) (Conf Λ Q) ℂ), transported_smul, zero_smul]
  map_add' := transported_add Φ Λ
  commutes' c := by
    rw [Algebra.algebraMap_eq_smul_one, transported_smul, transported_one,
      Algebra.algebraMap_eq_smul_one]
  map_star' X := by
    rw [Matrix.star_eq_conjTranspose, Matrix.star_eq_conjTranspose, transported_conjTranspose]

/-- **THE TRANSPORT IS ISOMETRIC** at the finite stages. -/
theorem norm_transported (Φ : ReversibleDynamics ι Q) (Λ : Finset ι)
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) : ‖transported Φ Λ X‖ = ‖X‖ :=
  NonUnitalStarAlgHom.norm_map (transportedHom Φ Λ) (transported_injective Φ Λ) X

/-- **THE LOCAL ALGEBRA IS STABLE** under the Heisenberg action. -/
theorem heis_mem (Φ : ReversibleDynamics ι Q) {T : Module.End ℂ (Scaffold ι Q)}
    (hT : T ∈ localAlg ι Q) : heis Φ T ∈ localAlg ι Q := by
  obtain ⟨Λ, X, rfl⟩ := hT
  exact ⟨hat Φ Λ, transported Φ Λ X, emb_transported Φ Λ X⟩

/-- The Heisenberg action on the local algebra. -/
noncomputable def heisLoc (Φ : ReversibleDynamics ι Q) (a : localAlg ι Q) : localAlg ι Q :=
  ⟨heis Φ a.1, heis_mem Φ a.2⟩

theorem heisLoc_ofM (Φ : ReversibleDynamics ι Q) (Λ : Finset ι)
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    heisLoc Φ (ofM Λ X) = ofM (hat Φ Λ) (transported Φ Λ X) := Subtype.ext (heis_emb Φ Λ X)

theorem heisLoc_mul (Φ : ReversibleDynamics ι Q) (a b : localAlg ι Q) :
    heisLoc Φ (a * b) = heisLoc Φ a * heisLoc Φ b := Subtype.ext (heis_mul Φ a.1 b.1)

theorem heisLoc_add (Φ : ReversibleDynamics ι Q) (a b : localAlg ι Q) :
    heisLoc Φ (a + b) = heisLoc Φ a + heisLoc Φ b := Subtype.ext (heis_add Φ a.1 b.1)

theorem heisLoc_smul (Φ : ReversibleDynamics ι Q) (c : ℂ) (a : localAlg ι Q) :
    heisLoc Φ (c • a) = c • heisLoc Φ a := Subtype.ext (heis_smul Φ c a.1)

theorem heisLoc_one (Φ : ReversibleDynamics ι Q) : heisLoc Φ 1 = 1 := Subtype.ext (heis_one Φ)

theorem heisLoc_sub (Φ : ReversibleDynamics ι Q) (a b : localAlg ι Q) :
    heisLoc Φ (a - b) = heisLoc Φ a - heisLoc Φ b := by
  rw [sub_eq_add_neg, heisLoc_add, ← neg_one_smul ℂ b, heisLoc_smul, neg_one_smul,
    ← sub_eq_add_neg]

theorem heisLoc_star (Φ : ReversibleDynamics ι Q) (a : localAlg ι Q) :
    heisLoc Φ (star a) = star (heisLoc Φ a) := by
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [star_ofM, heisLoc_ofM, heisLoc_ofM, star_ofM, transported_conjTranspose]

/-- **THE HEISENBERG ACTION IS ISOMETRIC** on the local algebra. -/
theorem norm_heisLoc (Φ : ReversibleDynamics ι Q) (a : localAlg ι Q) : ‖heisLoc Φ a‖ = ‖a‖ := by
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [heisLoc_ofM, norm_ofM, norm_ofM, norm_transported]

theorem heisLoc_inv_heisLoc (Φ : ReversibleDynamics ι Q) (a : localAlg ι Q) :
    heisLoc Φ.inv (heisLoc Φ a) = a := Subtype.ext (heis_inv_heis Φ a.1)

theorem heisLoc_heisLoc_inv (Φ : ReversibleDynamics ι Q) (a : localAlg ι Q) :
    heisLoc Φ (heisLoc Φ.inv a) = a := Subtype.ext (heis_inv_heis Φ.inv a.1)

theorem isometry_heisLoc (Φ : ReversibleDynamics ι Q) : Isometry (heisLoc Φ) :=
  Isometry.of_dist_eq fun a b => by rw [dist_eq_norm, dist_eq_norm, ← heisLoc_sub, norm_heisLoc]

/-- **THE DYNAMICS ON THE QUASILOCAL ALGEBRA**: the continuous extension of the Heisenberg
action. -/
noncomputable def heisQ (Φ : ReversibleDynamics ι Q) : Quasilocal ι Q → Quasilocal ι Q :=
  UniformSpace.Completion.map (heisLoc Φ)

theorem heisQ_coe (Φ : ReversibleDynamics ι Q) (a : localAlg ι Q) :
    heisQ Φ (a : Quasilocal ι Q) = ((heisLoc Φ a : localAlg ι Q) : Quasilocal ι Q) :=
  UniformSpace.Completion.map_coe (isometry_heisLoc Φ).uniformContinuous a

theorem continuous_heisQ (Φ : ReversibleDynamics ι Q) : Continuous (heisQ Φ) :=
  UniformSpace.Completion.continuous_map

theorem heisQ_stage (Φ : ReversibleDynamics ι Q) (Λ : Finset ι)
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    heisQ Φ (stage Λ X) = stage (hat Φ Λ) (transported Φ Λ X) := by
  rw [stage_apply, heisQ_coe, heisLoc_ofM, stage_apply]

theorem norm_heisQ (Φ : ReversibleDynamics ι Q) (x : Quasilocal ι Q) : ‖heisQ Φ x‖ = ‖x‖ := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq (continuous_norm.comp (continuous_heisQ Φ)) continuous_norm
  · rw [heisQ_coe, UniformSpace.Completion.norm_coe, UniformSpace.Completion.norm_coe,
      norm_heisLoc]

theorem heisQ_mul (Φ : ReversibleDynamics ι Q) (x y : Quasilocal ι Q) :
    heisQ Φ (x * y) = heisQ Φ x * heisQ Φ y := by
  refine UniformSpace.Completion.induction_on₂ x y ?_ fun a b => ?_
  · exact isClosed_eq ((continuous_heisQ Φ).comp continuous_mul)
      (((continuous_heisQ Φ).comp continuous_fst).mul ((continuous_heisQ Φ).comp continuous_snd))
  · rw [← UniformSpace.Completion.coe_mul, heisQ_coe, heisQ_coe, heisQ_coe, heisLoc_mul,
      UniformSpace.Completion.coe_mul]

theorem heisQ_add (Φ : ReversibleDynamics ι Q) (x y : Quasilocal ι Q) :
    heisQ Φ (x + y) = heisQ Φ x + heisQ Φ y := by
  refine UniformSpace.Completion.induction_on₂ x y ?_ fun a b => ?_
  · exact isClosed_eq ((continuous_heisQ Φ).comp continuous_add)
      (((continuous_heisQ Φ).comp continuous_fst).add ((continuous_heisQ Φ).comp continuous_snd))
  · rw [← UniformSpace.Completion.coe_add, heisQ_coe, heisQ_coe, heisQ_coe, heisLoc_add,
      UniformSpace.Completion.coe_add]

theorem heisQ_star (Φ : ReversibleDynamics ι Q) (x : Quasilocal ι Q) :
    heisQ Φ (star x) = star (heisQ Φ x) := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq ((continuous_heisQ Φ).comp continuous_star_q)
      (continuous_star_q.comp (continuous_heisQ Φ))
  · rw [star_coe, heisQ_coe, heisQ_coe, star_coe, heisLoc_star]

theorem heisQ_one (Φ : ReversibleDynamics ι Q) : heisQ Φ 1 = 1 := by
  rw [← UniformSpace.Completion.coe_one, heisQ_coe, heisLoc_one]

theorem heisQ_inv_heisQ (Φ : ReversibleDynamics ι Q) (x : Quasilocal ι Q) :
    heisQ Φ.inv (heisQ Φ x) = x := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq ((continuous_heisQ Φ.inv).comp (continuous_heisQ Φ)) continuous_id
  · rw [heisQ_coe, heisQ_coe, heisLoc_inv_heisLoc]

theorem heisQ_heisQ_inv (Φ : ReversibleDynamics ι Q) (x : Quasilocal ι Q) :
    heisQ Φ (heisQ Φ.inv x) = x := by
  refine UniformSpace.Completion.induction_on x ?_ fun a => ?_
  · exact isClosed_eq ((continuous_heisQ Φ).comp (continuous_heisQ Φ.inv)) continuous_id
  · rw [heisQ_coe, heisQ_coe, heisLoc_heisLoc_inv]

/-- The iterated hat region: the algebraic causal cone after `k` steps. -/
def hatIter (Φ : ReversibleDynamics ι Q) (Λ : Finset ι) : ℕ → Finset ι
  | 0 => Λ
  | k + 1 => hat Φ (hatIter Φ Λ k)

/-- **THE ALGEBRAIC CAUSAL CONE**: after `k` steps a local observable of `Λ` is a local
observable of the `k`-fold hat region. -/
theorem heis_iterate_emb (Φ : ReversibleDynamics ι Q) (Λ : Finset ι)
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) (k : ℕ) :
    ∃ Y : Matrix (Conf (hatIter Φ Λ k) Q) (Conf (hatIter Φ Λ k) Q) ℂ,
      (heis Φ)^[k] (emb Λ X) = emb (hatIter Φ Λ k) Y := by
  induction k with
  | zero => exact ⟨X, rfl⟩
  | succ k ih =>
    obtain ⟨Y, hY⟩ := ih
    exact ⟨transported Φ _ Y, by rw [Function.iterate_succ_apply', hY, heis_emb]; rfl⟩

end Dynamics

/-! ### Section E — the audit summary for the third entry -/

section Summary

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]

set_option maxHeartbeats 1000000 in
/-- **THE QUASILOCAL COMPLETION.** The finite stages embed compatibly and isometrically, the
quasilocal algebra is the closure of their union, every consistent family of density matrices is
a unital positive continuous functional on it, and every reversible finite-range dynamics acts on
it by an isometric star automorphism. -/
theorem quasilocal_completion (Φ : ReversibleDynamics ι Q) :
    (∀ (Λ Λ' : Finset ι) (h : Λ ⊆ Λ') (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ),
      stage Λ' (inclObs h X) = stage Λ X)
    ∧ (∀ (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ), ‖stage Λ X‖ = ‖X‖)
    ∧ closure (⋃ Λ : Finset ι, Set.range (stage Λ (Q := Q))) = (Set.univ : Set (Quasilocal ι Q))
    ∧ (∀ (ρ : ∀ Λ : Finset ι, Matrix (Conf Λ Q) (Conf Λ Q) ℂ) (hρ : IsStateFamily ρ),
        quasiState hρ 1 = 1 ∧ (∀ x : Quasilocal ι Q, 0 ≤ quasiState hρ (star x * x))
        ∧ ∀ (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ),
          quasiState hρ (stage Λ X) = (X * ρ Λ).trace)
    ∧ (∀ x y : Quasilocal ι Q, heisQ Φ (x * y) = heisQ Φ x * heisQ Φ y)
    ∧ (∀ x : Quasilocal ι Q, heisQ Φ (star x) = star (heisQ Φ x))
    ∧ (∀ x : Quasilocal ι Q, ‖heisQ Φ x‖ = ‖x‖)
    ∧ (∀ x : Quasilocal ι Q, heisQ Φ.inv (heisQ Φ x) = x) :=
  ⟨fun _ _ h X => stage_inclObs h X, norm_stage, closure_iUnion_stage,
    fun _ hρ => ⟨quasiState_one hρ, quasiState_nonneg hρ, quasiState_stage hρ⟩,
    heisQ_mul Φ, heisQ_star Φ, norm_heisQ Φ, heisQ_inv_heisQ Φ⟩

end Summary

#print axioms glob_patch
#print axioms patch_apply_of_not_mem
#print axioms patch_apply_of_mem
#print axioms agreeOffG_patch
#print axioms agreeOffG_refl
#print axioms agreeOffG_symm
#print axioms agreeOffG_trans
#print axioms eq_patch_of_agreeOffG
#print axioms patch_glob
#print axioms patch_eq_iff
#print axioms agreeOffG_iff
#print axioms confRestrict_glob
#print axioms kern_of_agree
#print axioms kern_of_not_agree
#print axioms kern_patch
#print axioms kern_inclObs
#print axioms kern_add
#print axioms kern_smul
#print axioms kern_conjTranspose
#print axioms kern_one
#print axioms emb_single
#print axioms emb_single_apply
#print axioms kerOf_emb
#print axioms ext_of_kerOf
#print axioms kerOf_add
#print axioms kerOf_smul
#print axioms kerOf_one
#print axioms emb_inclObs
#print axioms emb_add
#print axioms emb_smul
#print axioms emb_zero
#print axioms emb_one
#print axioms emb_mul
#print axioms emb_injective
#print axioms emb_eq_iff
#print axioms inclObs_mul
#print axioms inclObs_one
#print axioms inclObs_injective
#print axioms inclObs_add
#print axioms inclObs_smul
#print axioms inclObs_conjTranspose
#print axioms ofM_val
#print axioms ofM_inclObs
#print axioms ofM_add
#print axioms ofM_mul
#print axioms ofM_smul
#print axioms ofM_one
#print axioms ofM_zero
#print axioms ofM_neg
#print axioms ofM_sub
#print axioms ofM_injective
#print axioms ofM_eq_iff
#print axioms exists_ofM
#print axioms exists_ofM₂
#print axioms exists_ofM₃
#print axioms inclHom_apply
#print axioms norm_inclObs
#print axioms ofM_rep
#print axioms star_ofM
#print axioms nrm_ofM
#print axioms norm_ofM
#print axioms isometry_star_local
#print axioms star_coe
#print axioms continuous_star_q
#print axioms instCStarRingLocal
#print axioms instCStarAlgebraQuasilocal
#print axioms stage_apply
#print axioms stage_inclObs
#print axioms norm_stage
#print axioms stage_injective
#print axioms closure_iUnion_stage
#print axioms evalLocal_ofM
#print axioms evalLocal_add
#print axioms evalLocal_smul
#print axioms evalLocal_one
#print axioms trace_mul_nonneg_of_posSemidef
#print axioms evalLocal_nonneg
#print axioms norm_trace_mul_le
#print axioms norm_evalLocal_le
#print axioms localState_apply
#print axioms quasiState_coe
#print axioms quasiState_stage
#print axioms quasiState_one
#print axioms quasiState_nonneg
#print axioms quasiState_unique
#print axioms uniformFamily_isStateFamily
#print axioms referenceState_stage
#print axioms glob_map_eq
#print axioms agreeOffG_map
#print axioms agreeOffG_mono
#print axioms permOp_single
#print axioms permOpInv_single
#print axioms permOpInv_apply
#print axioms permOp_permOpInv
#print axioms permOpInv_permOp
#print axioms heis_mul
#print axioms heis_one
#print axioms heis_add
#print axioms heis_smul
#print axioms heis_inv_heis
#print axioms heis_injective
#print axioms kerOf_heis
#print axioms fwd_subset_hat
#print axioms bwd_subset_hat
#print axioms bwd_bwd_subset_hat
#print axioms symm_patch_eq_patch
#print axioms glob_ext
#print axioms glob_map_of_glob_eq
#print axioms target_of_glob_eq
#print axioms heis_emb_single
#print axioms heis_emb
#print axioms emb_transported
#print axioms transported_add
#print axioms transported_smul
#print axioms transported_mul
#print axioms transported_one
#print axioms transported_conjTranspose
#print axioms transported_injective
#print axioms norm_transported
#print axioms heis_mem
#print axioms heisLoc_ofM
#print axioms heisLoc_mul
#print axioms heisLoc_add
#print axioms heisLoc_smul
#print axioms heisLoc_one
#print axioms heisLoc_sub
#print axioms heisLoc_star
#print axioms norm_heisLoc
#print axioms heisLoc_inv_heisLoc
#print axioms heisLoc_heisLoc_inv
#print axioms isometry_heisLoc
#print axioms heisQ_coe
#print axioms continuous_heisQ
#print axioms heisQ_stage
#print axioms norm_heisQ
#print axioms heisQ_mul
#print axioms heisQ_add
#print axioms heisQ_star
#print axioms heisQ_one
#print axioms heisQ_inv_heisQ
#print axioms heisQ_heisQ_inv
#print axioms heis_iterate_emb
#print axioms quasilocal_completion

end QuasilocalAlgebra
end OIBridge
