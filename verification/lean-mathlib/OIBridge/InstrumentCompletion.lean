/-
  OIBridge/InstrumentCompletion.lean — post-Level III instrument audit, first entry: the
  instrument interface on the quasilocal algebra, the finite-support redundancy theorem, and a
  stage-compatible automorphism that is not finite-support.

  THE SEAM. Level III completed the algebra, the state space, and one discrete dynamics. It did
  not complete the operational availability relation of Level II. This entry opens the audit of
  that seam. It is an audit, not a level: no target class is adopted, and the round decides which
  of the pre-registered questions the finite theory settles. See
  `verification/INSTRUMENT-COMPLETION-AUDIT.md` for the pre-registration and the status table.

  THE CONVENTION. Instruments are Heisenberg-picture: a finite family of maps of the algebra to
  itself whose sum is unital. Complete positivity enters through its concrete Kraus witness,
  conjugation by a family of algebra elements, which is what Levels I and II already use. The
  abstract completely positive class on the completion is NOT formalized here, and no claim is
  made that the two agree in either direction.

  (1) THE INTERFACE. Instrument data is a family `β` of elements of the quasilocal algebra with
      `∑ star (β k) * β k = 1` (`IsQInstrument`); a branch is
      `qBranch β out x z = ∑_{out k = x} star (β k) * z * β k`. No extension machinery is needed
      for the branches: multiplication in the completion is already defined, so a conjugation
      family acts on the whole algebra directly. The branches are additive and homogeneous
      (`qBranch_add`, `qBranch_smul`), carry `star z * z` to a sum of terms of that shape
      (`qBranch_star_mul_self`), and sum to a unital total map (`sum_qBranch`, `qBranch_sum_one`).
      An instrument is finite-support when all its elements lie in one finite stage
      (`IsFiniteSupport`).

  (2) Q1, DECIDED IN BOTH DIRECTIONS. A finite-region Kraus instrument with the Level II
      normalization gives a finite-support quasilocal instrument, the normalization transporting
      because `stage Λ` is a unital star homomorphism (`qInstrument_of_kraus`). Conversely a
      finite-support quasilocal instrument comes from a finite-region Kraus instrument, recovered
      by injectivity of the stage embedding along with its normalization
      (`kraus_of_finiteSupport`). The two directions are separate theorems with separate
      witnesses; `finiteSupport_iff_kraus` states the biconditional only because both are proved
      (§A.34). On a larger region the action is the inert spectator extension: the Kraus operators
      extended by the identity off their own region (`qBranch_stage_inclObs`). Locality and the
      normalization together make a finite-support instrument fix the observables of a disjoint
      region (`qTotal_stage_of_disjoint`).

  (3) COMPATIBLE WEIGHT FAMILIES. A `UnimodularFamily` assigns a unimodular weight to every
      configuration of every region, such that the weight ratio of two configurations agreeing off
      a region is the weight ratio of their restrictions. That is exactly what a conjugation
      family compatible with the inclusions needs: the conjugations commute with extension by the
      identity (`inclObs_wtConj`), are injective star homomorphisms of the stages hence isometric
      (`norm_wtConj`), and lift to an isometric star automorphism of the local algebra and of its
      completion (`wtLoc_mul`, `wtQ_mul`, `wtQ_star`, `norm_wtQ`).

  (4) THE WITNESS. The all-sites phase family gives each region the product, over its sites, of an
      onsite phase (`phaseAllWt`). It is compatible because sites outside a region contribute
      equal factors to two configurations agreeing there, and those cancel between the weight and
      its conjugate (`phaseAllWt_compat`) — the formal content of "every local observable samples
      only finitely many of the phases". The resulting automorphism is not the total map of any
      finite-support instrument: for any candidate support region there is a site outside it whose
      single-site matrix unit the automorphism multiplies by `i`, while a finite-support
      instrument fixes it (`phaseAll_not_finiteSupport`). The finite-support and stage-compatible
      classes are therefore distinct.

  WHAT IS NOT CLAIMED: no infinite-dimensional analogue of the Level II instrument
  characterization — the kernel characterizes the finite-support class and nothing wider; no claim
  that the Kraus class exhausts the completely positive instruments on the quasilocal algebra, in
  either direction; no claim that a general compatible family of stage instruments extends to the
  completion, which would need contractivity of unital positive maps, absent from the kernel; and
  no claim that stage-compatible operations are operationally available under OI_Q, which is a
  separate question and is not claimed either way. The phase witness shows non-finite-support, not
  availability: the Level III countermodel already shows it is induced by no reversible
  finite-range substratum dynamics. Bare OI and the frozen Level I, Level II and Level III
  statements are untouched, and no manuscript change is made in this round.
-/

import OIBridge.QuasilocalCharacterization

namespace OIBridge
namespace InstrumentCompletion

open Complex Matrix RegionTower QuasilocalAlgebra QuasilocalCharacterization
open scoped ComplexOrder Matrix.Norms.L2Operator

set_option linter.unusedSectionVars false
set_option maxHeartbeats 1000000

/-! ### Section A — the instrument interface, in the Heisenberg picture -/

section Interface

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]

/-- **INSTRUMENT DATA**: conjugation elements whose normalization is unitality of the branch sum.
Kraus form is the concrete witness of complete positivity; the abstract class is not formalized
here, and nothing below claims the two agree. -/
def IsQInstrument {n : ℕ} (β : Fin n → Quasilocal ι Q) : Prop :=
  ∑ k, star (β k) * β k = 1

/-- One branch of an instrument, in the Heisenberg picture. -/
noncomputable def qBranch {n m : ℕ} (β : Fin n → Quasilocal ι Q) (out : Fin n → Fin m)
    (x : Fin m) (z : Quasilocal ι Q) : Quasilocal ι Q :=
  ∑ k ∈ Finset.univ.filter (fun k => out k = x), star (β k) * z * β k

/-- The total map: the sum of the branches. -/
noncomputable def qTotal {n : ℕ} (β : Fin n → Quasilocal ι Q) (z : Quasilocal ι Q) :
    Quasilocal ι Q :=
  ∑ k, star (β k) * z * β k

theorem qBranch_add {n m : ℕ} (β : Fin n → Quasilocal ι Q) (out : Fin n → Fin m) (x : Fin m)
    (z w : Quasilocal ι Q) : qBranch β out x (z + w) = qBranch β out x z + qBranch β out x w := by
  simp only [qBranch, mul_add, add_mul, Finset.sum_add_distrib]

theorem qBranch_smul {n m : ℕ} (β : Fin n → Quasilocal ι Q) (out : Fin n → Fin m) (x : Fin m)
    (c : ℂ) (z : Quasilocal ι Q) : qBranch β out x (c • z) = c • qBranch β out x z := by
  simp only [qBranch, mul_smul_comm, smul_mul_assoc, Finset.smul_sum]

theorem qBranch_zero {n m : ℕ} (β : Fin n → Quasilocal ι Q) (out : Fin n → Fin m) (x : Fin m) :
    qBranch β out x 0 = 0 := by
  simp only [qBranch, mul_zero, zero_mul, Finset.sum_const_zero]

/-- **POSITIVITY**, in the concrete sense the Kraus form supplies: a branch carries `star z * z`
to a sum of terms of the same shape. -/
theorem qBranch_star_mul_self {n m : ℕ} (β : Fin n → Quasilocal ι Q) (out : Fin n → Fin m)
    (x : Fin m) (z : Quasilocal ι Q) :
    qBranch β out x (star z * z)
      = ∑ k ∈ Finset.univ.filter (fun k => out k = x), star (z * β k) * (z * β k) := by
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [star_mul]
  simp only [mul_assoc]

/-- The branches sum to the total map. -/
theorem sum_qBranch {n m : ℕ} (β : Fin n → Quasilocal ι Q) (out : Fin n → Fin m)
    (z : Quasilocal ι Q) : ∑ x : Fin m, qBranch β out x z = qTotal β z := by
  unfold qTotal qBranch
  exact Finset.sum_fiberwise Finset.univ out (fun k => star (β k) * z * β k)

/-- **THE NORMALIZATION**: the branch sum is unital exactly when the conjugation data is. -/
theorem qBranch_sum_one {n m : ℕ} {β : Fin n → Quasilocal ι Q} (out : Fin n → Fin m)
    (hβ : IsQInstrument β) : ∑ x : Fin m, qBranch β out x 1 = 1 := by
  rw [sum_qBranch, qTotal]
  simp only [mul_one]
  exact hβ

theorem qTotal_one {n : ℕ} {β : Fin n → Quasilocal ι Q} (hβ : IsQInstrument β) :
    qTotal β 1 = 1 := by
  rw [qTotal]
  simp only [mul_one]
  exact hβ

/-- **FINITE SUPPORT**: every conjugation element lies in one finite stage. -/
def IsFiniteSupport {n : ℕ} (β : Fin n → Quasilocal ι Q) : Prop :=
  ∃ Λ : Finset ι, ∀ k, β k ∈ Set.range (stage Λ)

end Interface

/-! ### Section B — Q1: the finite-support redundancy theorem, in both directions -/

section Redundancy

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]

/-- **DIRECTION ONE**: a finite-region Kraus instrument, with the Level II normalization, gives a
finite-support quasilocal instrument. -/
theorem qInstrument_of_kraus {n : ℕ} (Λ : Finset ι)
    (K : Fin n → Matrix (Conf Λ Q) (Conf Λ Q) ℂ) (hK : ∑ k, (K k)ᴴ * K k = 1) :
    IsQInstrument (fun k => stage Λ (K k)) ∧ IsFiniteSupport (fun k => stage Λ (K k)) := by
  constructor
  · unfold IsQInstrument
    have h : ∀ k, star (stage Λ (K k)) * stage Λ (K k) = stage Λ ((K k)ᴴ * K k) := by
      intro k
      rw [← map_star, ← map_mul, Matrix.star_eq_conjTranspose]
    simp only [h, ← map_sum, hK, map_one]
  · exact ⟨Λ, fun k => ⟨K k, rfl⟩⟩

/-- **DIRECTION TWO**: a finite-support quasilocal instrument comes from a finite-region Kraus
instrument, and the Level II normalization is recovered with it. -/
theorem kraus_of_finiteSupport {n : ℕ} {β : Fin n → Quasilocal ι Q}
    (hβ : IsQInstrument β) (hfs : IsFiniteSupport β) :
    ∃ (Λ : Finset ι) (K : Fin n → Matrix (Conf Λ Q) (Conf Λ Q) ℂ),
      (∀ k, β k = stage Λ (K k)) ∧ ∑ k, (K k)ᴴ * K k = 1 := by
  obtain ⟨Λ, hΛ⟩ := hfs
  choose K hK using hΛ
  refine ⟨Λ, K, fun k => (hK k).symm, ?_⟩
  apply stage_injective Λ
  rw [map_sum, map_one]
  have h : ∀ k, stage Λ ((K k)ᴴ * K k) = star (β k) * β k := by
    intro k
    rw [map_mul, ← Matrix.star_eq_conjTranspose, map_star, hK k]
  simp only [h]
  exact hβ

/-- **Q1**: the two directions together. The biconditional is stated because both directions are
proved above, not inferred from either. -/
theorem finiteSupport_iff_kraus {n : ℕ} (β : Fin n → Quasilocal ι Q) :
    (IsQInstrument β ∧ IsFiniteSupport β)
      ↔ ∃ (Λ : Finset ι) (K : Fin n → Matrix (Conf Λ Q) (Conf Λ Q) ℂ),
          (∀ k, β k = stage Λ (K k)) ∧ ∑ k, (K k)ᴴ * K k = 1 := by
  constructor
  · rintro ⟨h1, h2⟩
    exact kraus_of_finiteSupport h1 h2
  · rintro ⟨Λ, K, hβ, hK⟩
    have h : β = fun k => stage Λ (K k) := funext hβ
    rw [h]
    exact qInstrument_of_kraus Λ K hK

/-- **THE INERT SPECTATOR EXTENSION**: on the observables of a larger region, a finite-support
branch acts by the Kraus operators extended by the identity off their own region. -/
theorem qBranch_stage_inclObs {n m : ℕ} {Λ Λ' : Finset ι} (h : Λ ⊆ Λ')
    (K : Fin n → Matrix (Conf Λ Q) (Conf Λ Q) ℂ) (out : Fin n → Fin m) (x : Fin m)
    (Y : Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ) :
    qBranch (fun k => stage Λ (K k)) out x (stage Λ' Y)
      = stage Λ' (∑ k ∈ Finset.univ.filter (fun k => out k = x),
          (inclObs h (K k))ᴴ * Y * inclObs h (K k)) := by
  rw [qBranch, map_sum]
  refine Finset.sum_congr rfl fun k _ => ?_
  rw [← stage_inclObs h (K k), ← map_star, ← map_mul, ← map_mul,
    ← Matrix.star_eq_conjTranspose]

/-- A finite-support instrument leaves the observables of a disjoint region alone: locality plus
the normalization. -/
theorem qTotal_stage_of_disjoint {n : ℕ} {Λ₀ Λ : Finset ι} (hd : Disjoint Λ₀ Λ)
    {K : Fin n → Matrix (Conf Λ₀ Q) (Conf Λ₀ Q) ℂ} (hK : ∑ k, (K k)ᴴ * K k = 1)
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    qTotal (fun k => stage Λ₀ (K k)) (stage Λ X) = stage Λ X := by
  rw [qTotal]
  have hstep : ∀ k, star (stage Λ₀ (K k)) * stage Λ X * stage Λ₀ (K k)
      = stage Λ X * stage Λ₀ ((K k)ᴴ * K k) := by
    intro k
    rw [← map_star, Matrix.star_eq_conjTranspose,
      stage_comm_of_disjoint hd ((K k)ᴴ) X, mul_assoc, ← map_mul]
  simp only [hstep, ← Finset.mul_sum, ← map_sum, hK, map_one, mul_one]

end Redundancy

/-! ### Section C — compatible weight families and their automorphisms -/

section Weights

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]

/-- A family of unimodular weights on the configurations of every region, compatible with the
inclusions in the sense that the weight ratio of two configurations agreeing off a region is the
weight ratio of their restrictions. This is exactly what a conjugation family compatible with the
inclusions needs. -/
structure UnimodularFamily (ι Q : Type) [DecidableEq ι] [Fintype Q] [DecidableEq Q] where
  /-- The weight of a configuration of a region. -/
  wt : ∀ Λ : Finset ι, Conf Λ Q → ℂ
  unimodular : ∀ (Λ : Finset ι) (f : Conf Λ Q), wt Λ f * star (wt Λ f) = 1
  compat : ∀ {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (F G : Conf Λ' Q), AgreeOff h F G →
    wt Λ' F * star (wt Λ' G)
      = wt Λ (confRestrict h F) * star (wt Λ (confRestrict h G))

variable (W : UnimodularFamily ι Q)

theorem star_wt_mul (Λ : Finset ι) (f : Conf Λ Q) : star (W.wt Λ f) * W.wt Λ f = 1 := by
  rw [mul_comm]; exact W.unimodular Λ f

/-- The diagonal unitary of a region. -/
noncomputable def wtU (Λ : Finset ι) : Matrix (Conf Λ Q) (Conf Λ Q) ℂ := diagonal (W.wt Λ)

/-- Conjugation by the region's weight unitary. -/
noncomputable def wtConj (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    Matrix (Conf Λ Q) (Conf Λ Q) ℂ := wtU W Λ * X * (wtU W Λ)ᴴ

theorem wtConj_apply (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) (f g : Conf Λ Q) :
    wtConj W Λ X f g = W.wt Λ f * X f g * star (W.wt Λ g) := by
  rw [wtConj, wtU, diagonal_conjTranspose, mul_diagonal, diagonal_mul]
  simp only [Pi.star_apply]

theorem wtU_mul_conjTranspose (Λ : Finset ι) :
    wtU W Λ * (wtU W Λ)ᴴ = (1 : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) := by
  rw [wtU, diagonal_conjTranspose, diagonal_mul_diagonal, ← diagonal_one]
  congr 1
  funext f
  rw [Pi.star_apply, W.unimodular]

theorem conjTranspose_mul_wtU (Λ : Finset ι) :
    (wtU W Λ)ᴴ * wtU W Λ = (1 : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) := by
  rw [wtU, diagonal_conjTranspose, diagonal_mul_diagonal, ← diagonal_one]
  congr 1
  funext f
  rw [Pi.star_apply, star_wt_mul]

theorem wtConj_mul (Λ : Finset ι) (X Y : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    wtConj W Λ (X * Y) = wtConj W Λ X * wtConj W Λ Y := by
  unfold wtConj
  simp only [Matrix.mul_assoc]
  rw [← Matrix.mul_assoc (wtU W Λ)ᴴ (wtU W Λ), conjTranspose_mul_wtU, Matrix.one_mul]

theorem wtConj_one (Λ : Finset ι) :
    wtConj W Λ (1 : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) = 1 := by
  rw [wtConj, Matrix.mul_one, wtU_mul_conjTranspose]

theorem wtConj_add (Λ : Finset ι) (X Y : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    wtConj W Λ (X + Y) = wtConj W Λ X + wtConj W Λ Y := by
  simp only [wtConj, Matrix.mul_add, Matrix.add_mul]

theorem wtConj_smul (Λ : Finset ι) (c : ℂ) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    wtConj W Λ (c • X) = c • wtConj W Λ X := by
  simp only [wtConj, Matrix.mul_smul, Matrix.smul_mul]

theorem wtConj_conjTranspose (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    wtConj W Λ Xᴴ = (wtConj W Λ X)ᴴ := by
  simp only [wtConj, conjTranspose_mul, conjTranspose_conjTranspose, Matrix.mul_assoc]

theorem wtConj_injective (Λ : Finset ι) : Function.Injective (wtConj W Λ) := by
  intro X Y hXY
  have h2 := congrArg (fun M => (wtU W Λ)ᴴ * M * wtU W Λ) hXY
  simp only [wtConj] at h2
  simpa [Matrix.mul_assoc, ← Matrix.mul_assoc (wtU W Λ)ᴴ, conjTranspose_mul_wtU,
    wtU_mul_conjTranspose] using h2

/-- **COMPATIBILITY WITH THE INCLUSIONS**: the conjugations of a compatible weight family commute
with extension by the identity. -/
theorem inclObs_wtConj {Λ Λ' : Finset ι} (h : Λ ⊆ Λ')
    (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    inclObs h (wtConj W Λ X) = wtConj W Λ' (inclObs h X) := by
  ext F G
  rw [wtConj_apply, inclObs_apply, inclObs_apply]
  by_cases hFG : AgreeOff h F G
  · rw [if_pos hFG, if_pos hFG, wtConj_apply]
    have hc := W.compat h F G hFG
    calc W.wt Λ (confRestrict h F) * X (confRestrict h F) (confRestrict h G)
            * star (W.wt Λ (confRestrict h G))
        = X (confRestrict h F) (confRestrict h G)
            * (W.wt Λ (confRestrict h F) * star (W.wt Λ (confRestrict h G))) := by ring
      _ = X (confRestrict h F) (confRestrict h G) * (W.wt Λ' F * star (W.wt Λ' G)) := by rw [hc]
      _ = W.wt Λ' F * X (confRestrict h F) (confRestrict h G) * star (W.wt Λ' G) := by ring
  · rw [if_neg hFG, if_neg hFG, mul_zero, zero_mul]

/-- The conjugation as a star algebra homomorphism of a finite stage. -/
noncomputable def wtHom (Λ : Finset ι) :
    Matrix (Conf Λ Q) (Conf Λ Q) ℂ →⋆ₐ[ℂ] Matrix (Conf Λ Q) (Conf Λ Q) ℂ where
  toFun := wtConj W Λ
  map_one' := wtConj_one W Λ
  map_mul' := wtConj_mul W Λ
  map_zero' := by simp only [wtConj, Matrix.mul_zero, Matrix.zero_mul]
  map_add' := wtConj_add W Λ
  commutes' c := by
    rw [Algebra.algebraMap_eq_smul_one, wtConj_smul, wtConj_one]
  map_star' X := by
    rw [Matrix.star_eq_conjTranspose, Matrix.star_eq_conjTranspose, wtConj_conjTranspose]

theorem norm_wtConj (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    ‖wtConj W Λ X‖ = ‖X‖ :=
  NonUnitalStarAlgHom.norm_map (wtHom W Λ) (wtConj_injective W Λ) X

/-- The induced map on the local algebra. -/
noncomputable def wtLoc (a : localAlg ι Q) : localAlg ι Q :=
  ofM (rep a).1 (wtConj W (rep a).1 (rep a).2)

theorem wtLoc_ofM (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    wtLoc W (ofM Λ X) = ofM Λ (wtConj W Λ X) := by
  unfold wtLoc
  have h := ofM_rep (ofM Λ X)
  rw [ofM_eq_iff] at h ⊢
  rw [inclObs_wtConj, inclObs_wtConj, h]

theorem wtLoc_mul (a b : localAlg ι Q) : wtLoc W (a * b) = wtLoc W a * wtLoc W b := by
  obtain ⟨Λ, X, Y, rfl, rfl⟩ := exists_ofM₂ a b
  rw [← ofM_mul, wtLoc_ofM, wtLoc_ofM, wtLoc_ofM, ← ofM_mul, wtConj_mul]

theorem wtLoc_add (a b : localAlg ι Q) : wtLoc W (a + b) = wtLoc W a + wtLoc W b := by
  obtain ⟨Λ, X, Y, rfl, rfl⟩ := exists_ofM₂ a b
  rw [← ofM_add, wtLoc_ofM, wtLoc_ofM, wtLoc_ofM, ← ofM_add, wtConj_add]

theorem wtLoc_smul (c : ℂ) (a : localAlg ι Q) : wtLoc W (c • a) = c • wtLoc W a := by
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [← ofM_smul, wtLoc_ofM, wtLoc_ofM, ← ofM_smul, wtConj_smul]

theorem wtLoc_star (a : localAlg ι Q) : wtLoc W (star a) = star (wtLoc W a) := by
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [star_ofM, wtLoc_ofM, wtLoc_ofM, star_ofM, wtConj_conjTranspose]

theorem wtLoc_sub (a b : localAlg ι Q) : wtLoc W (a - b) = wtLoc W a - wtLoc W b := by
  rw [sub_eq_add_neg, wtLoc_add, ← neg_one_smul ℂ b, wtLoc_smul, neg_one_smul, ← sub_eq_add_neg]

theorem norm_wtLoc (a : localAlg ι Q) : ‖wtLoc W a‖ = ‖a‖ := by
  obtain ⟨Λ, X, rfl⟩ := exists_ofM a
  rw [wtLoc_ofM, norm_ofM, norm_ofM, norm_wtConj]

theorem isometry_wtLoc : Isometry (wtLoc W) :=
  Isometry.of_dist_eq fun a b => by rw [dist_eq_norm, dist_eq_norm, ← wtLoc_sub, norm_wtLoc]

/-- **THE AUTOMORPHISM OF THE QUASILOCAL ALGEBRA** determined by a compatible weight family. -/
noncomputable def wtQ : Quasilocal ι Q → Quasilocal ι Q :=
  UniformSpace.Completion.map (wtLoc W)

theorem wtQ_coe (a : localAlg ι Q) :
    wtQ W (a : Quasilocal ι Q) = ((wtLoc W a : localAlg ι Q) : Quasilocal ι Q) :=
  UniformSpace.Completion.map_coe (isometry_wtLoc W).uniformContinuous a

theorem continuous_wtQ : Continuous (wtQ W) := UniformSpace.Completion.continuous_map

theorem wtQ_stage (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    wtQ W (stage Λ X) = stage Λ (wtConj W Λ X) := by
  rw [stage_apply, wtQ_coe, wtLoc_ofM, stage_apply]

theorem wtQ_mul (z w : Quasilocal ι Q) : wtQ W (z * w) = wtQ W z * wtQ W w := by
  refine UniformSpace.Completion.induction_on₂ z w ?_ fun a b => ?_
  · exact isClosed_eq ((continuous_wtQ W).comp continuous_mul)
      (((continuous_wtQ W).comp continuous_fst).mul ((continuous_wtQ W).comp continuous_snd))
  · rw [← UniformSpace.Completion.coe_mul, wtQ_coe, wtQ_coe, wtQ_coe, wtLoc_mul,
      UniformSpace.Completion.coe_mul]

theorem wtQ_add (z w : Quasilocal ι Q) : wtQ W (z + w) = wtQ W z + wtQ W w := by
  refine UniformSpace.Completion.induction_on₂ z w ?_ fun a b => ?_
  · exact isClosed_eq ((continuous_wtQ W).comp continuous_add)
      (((continuous_wtQ W).comp continuous_fst).add ((continuous_wtQ W).comp continuous_snd))
  · rw [← UniformSpace.Completion.coe_add, wtQ_coe, wtQ_coe, wtQ_coe, wtLoc_add,
      UniformSpace.Completion.coe_add]

theorem wtQ_star (z : Quasilocal ι Q) : wtQ W (star z) = star (wtQ W z) := by
  refine UniformSpace.Completion.induction_on z ?_ fun a => ?_
  · exact isClosed_eq ((continuous_wtQ W).comp continuous_star_q)
      (continuous_star_q.comp (continuous_wtQ W))
  · rw [star_coe, wtQ_coe, wtQ_coe, star_coe, wtLoc_star]

theorem norm_wtQ (z : Quasilocal ι Q) : ‖wtQ W z‖ = ‖z‖ := by
  refine UniformSpace.Completion.induction_on z ?_ fun a => ?_
  · exact isClosed_eq (continuous_norm.comp (continuous_wtQ W)) continuous_norm
  · rw [wtQ_coe, UniformSpace.Completion.norm_coe, UniformSpace.Completion.norm_coe, norm_wtLoc]

theorem wtQ_one : wtQ W (1 : Quasilocal ι Q) = 1 := by
  rw [← UniformSpace.Completion.coe_one, wtQ_coe]
  have : wtLoc W (1 : localAlg ι Q) = 1 := by
    rw [← ofM_one (∅ : Finset ι), wtLoc_ofM, wtConj_one, ofM_one]
  rw [this]

end Weights

/-! ### Section D — the all-sites phase family: stage-compatible, not finite-support -/

section PhaseAll

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]

/-- The onsite phase: `i` at the reference value, `1` elsewhere. -/
noncomputable def siteWt (q : Q) : ℂ := if q = Classical.arbitrary Q then I else 1

theorem siteWt_unimodular (q : Q) : siteWt q * star (siteWt (Q := Q) q) = 1 := by
  unfold siteWt
  split_ifs <;> simp [Complex.conj_I]

/-- The all-sites weight of a region: the product of the onsite phases over its sites. -/
noncomputable def phaseAllWt (Λ : Finset ι) (f : Conf Λ Q) : ℂ :=
  ∏ i ∈ Λ, siteWt (ext Λ f i)

theorem phaseAllWt_unimodular (Λ : Finset ι) (f : Conf Λ Q) :
    phaseAllWt Λ f * star (phaseAllWt Λ f) = 1 := by
  unfold phaseAllWt
  rw [star_prod, ← Finset.prod_mul_distrib]
  exact Finset.prod_eq_one fun i _ => siteWt_unimodular _

theorem ext_eq_of_mem {Λ : Finset ι} (f : Conf Λ Q) {i : ι} (hi : i ∈ Λ) :
    ext Λ f i = f ⟨i, hi⟩ := patch_apply_of_mem hi

theorem ext_confRestrict {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (F : Conf Λ' Q) {i : ι} (hi : i ∈ Λ) :
    ext Λ (confRestrict h F) i = ext Λ' F i := by
  rw [ext_eq_of_mem _ hi, ext_eq_of_mem _ (h hi)]
  rfl

/-- **THE ALL-SITES FAMILY IS COMPATIBLE**: sites outside a region contribute equal factors to two
configurations agreeing there, and those factors cancel between the weight and its conjugate. -/
theorem phaseAllWt_compat {Λ Λ' : Finset ι} (h : Λ ⊆ Λ') (F G : Conf Λ' Q)
    (hFG : AgreeOff h F G) :
    phaseAllWt Λ' F * star (phaseAllWt Λ' G)
      = phaseAllWt Λ (confRestrict h F) * star (phaseAllWt Λ (confRestrict h G)) := by
  have key : ∀ A B : Conf Λ' Q,
      phaseAllWt Λ' A * star (phaseAllWt Λ' B)
        = ∏ i ∈ Λ', (siteWt (ext Λ' A i) * star (siteWt (ext Λ' B i))) := by
    intro A B
    unfold phaseAllWt
    rw [star_prod, ← Finset.prod_mul_distrib]
  rw [key F G]
  have hstep : ∏ i ∈ Λ', (siteWt (ext Λ' F i) * star (siteWt (ext Λ' G i)))
      = ∏ i ∈ Λ, (siteWt (ext Λ' F i) * star (siteWt (ext Λ' G i))) := by
    refine (Finset.prod_subset h fun i hi hiΛ => ?_).symm
    have hFG' : ext Λ' F i = ext Λ' G i := by
      rw [ext_eq_of_mem _ hi, ext_eq_of_mem _ hi]
      exact hFG ⟨i, hi⟩ hiΛ
    rw [hFG', siteWt_unimodular]
  rw [hstep]
  unfold phaseAllWt
  rw [star_prod, ← Finset.prod_mul_distrib]
  refine Finset.prod_congr rfl fun i hi => ?_
  rw [ext_confRestrict h F hi, ext_confRestrict h G hi]

/-- The all-sites phase family. -/
noncomputable def phaseAll (ι Q : Type) [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q] :
    UnimodularFamily ι Q where
  wt := phaseAllWt
  unimodular := phaseAllWt_unimodular
  compat := fun h F G hFG => phaseAllWt_compat h F G hFG

/-- The automorphism it determines. -/
noncomputable abbrev phaseAllQ : Quasilocal ι Q → Quasilocal ι Q := wtQ (phaseAll ι Q)

theorem phaseAllQ_mul (z w : Quasilocal ι Q) :
    phaseAllQ (z * w) = phaseAllQ z * phaseAllQ w := wtQ_mul _ z w

theorem phaseAllQ_star (z : Quasilocal ι Q) :
    phaseAllQ (star z) = star (phaseAllQ z) := wtQ_star _ z

theorem norm_phaseAllQ (z : Quasilocal ι Q) : ‖phaseAllQ (ι := ι) (Q := Q) z‖ = ‖z‖ :=
  norm_wtQ _ z

theorem phaseAllQ_stage (Λ : Finset ι) (X : Matrix (Conf Λ Q) (Conf Λ Q) ℂ) :
    phaseAllQ (stage Λ X) = stage Λ (wtConj (phaseAll ι Q) Λ X) := wtQ_stage _ Λ X

/-- At a single site the all-sites weight is the onsite phase. -/
theorem phaseAllWt_singleton (j : ι) (f : Conf ({j} : Finset ι) Q) :
    phaseAllWt ({j} : Finset ι) f = siteWt (f ⟨j, Finset.mem_singleton_self j⟩) := by
  unfold phaseAllWt
  rw [Finset.prod_singleton, ext_eq_of_mem _ (Finset.mem_singleton_self j)]

/-- **THE WITNESS**: the all-sites automorphism moves a single-site matrix unit at every site, so
no finite-support instrument's total map agrees with it. -/
theorem phaseAll_not_finiteSupport [Infinite ι] [Nontrivial Q] {n : ℕ}
    (β : Fin n → Quasilocal ι Q) (hβ : IsQInstrument β) (hfs : IsFiniteSupport β) :
    phaseAllQ (ι := ι) (Q := Q) ≠ qTotal β := by
  intro hEq
  obtain ⟨Λ₀, K, hK, hnorm⟩ := kraus_of_finiteSupport hβ hfs
  obtain ⟨j, hj⟩ := Infinite.exists_notMem_finset Λ₀
  set q₀ : Q := Classical.arbitrary Q with hq₀
  obtain ⟨q₁, hq₁⟩ := exists_ne q₀
  set Λ : Finset ι := {j} with hΛ
  set f₀ : Conf Λ Q := fun _ => q₀ with hf₀
  set f₁ : Conf Λ Q := fun _ => q₁ with hf₁
  set E : Matrix (Conf Λ Q) (Conf Λ Q) ℂ := Matrix.single f₀ f₁ (1 : ℂ) with hE
  have hd : Disjoint Λ₀ Λ := by
    rw [Finset.disjoint_singleton_right]
    exact hj
  have hβK : β = fun k => stage Λ₀ (K k) := funext hK
  have h1 : qTotal β (stage Λ E) = stage Λ E := by
    rw [hβK]
    exact qTotal_stage_of_disjoint hd hnorm E
  have h2 : phaseAllQ (stage Λ E) = stage Λ (wtConj (phaseAll ι Q) Λ E) := phaseAllQ_stage Λ E
  have hne : wtConj (phaseAll ι Q) Λ E ≠ E := by
    intro habs
    have hentry := congrFun (congrFun habs f₀) f₁
    rw [wtConj_apply] at hentry
    have hw₀ : (phaseAll ι Q).wt Λ f₀ = I := by
      show phaseAllWt Λ f₀ = I
      rw [phaseAllWt_singleton]
      unfold siteWt
      rw [if_pos rfl]
    have hw₁ : (phaseAll ι Q).wt Λ f₁ = 1 := by
      show phaseAllWt Λ f₁ = 1
      rw [phaseAllWt_singleton]
      unfold siteWt
      rw [if_neg hq₁]
    have hE01 : E f₀ f₁ = 1 := Matrix.single_apply_same f₀ f₁ 1
    rw [hw₀, hw₁, hE01, star_one, mul_one, mul_one] at hentry
    have him := congrArg Complex.im hentry
    simp at him
  exact hne (stage_injective Λ (by rw [← h2, hEq, h1]))

end PhaseAll

/-! ### Section E — the audit summary for the first entry -/

section Summary

variable {ι Q : Type} [DecidableEq ι] [Fintype Q] [DecidableEq Q] [Nonempty Q]

/-- **THE FIRST ENTRY.** Q1 is decided in both directions: a finite-support quasilocal instrument
is exactly a finite-region Kraus instrument with the Level II normalization, acting on larger
regions by the inert spectator extension. The classes of finite-support and stage-compatible
operations are distinct, witnessed by the all-sites phase automorphism. Nothing here decides
whether a general compatible family extends, whether such families are operationally available,
or whether the Kraus class exhausts the completely positive instruments. -/
theorem instrument_audit_entry_one [Infinite ι] [Nontrivial Q] :
    (∀ (n : ℕ) (β : Fin n → Quasilocal ι Q),
        (IsQInstrument β ∧ IsFiniteSupport β)
          ↔ ∃ (Λ : Finset ι) (K : Fin n → Matrix (Conf Λ Q) (Conf Λ Q) ℂ),
              (∀ k, β k = stage Λ (K k)) ∧ ∑ k, (K k)ᴴ * K k = 1)
    ∧ (∀ (n m : ℕ) (Λ Λ' : Finset ι) (h : Λ ⊆ Λ')
          (K : Fin n → Matrix (Conf Λ Q) (Conf Λ Q) ℂ) (out : Fin n → Fin m) (x : Fin m)
          (Y : Matrix (Conf Λ' Q) (Conf Λ' Q) ℂ),
        qBranch (fun k => stage Λ (K k)) out x (stage Λ' Y)
          = stage Λ' (∑ k ∈ Finset.univ.filter (fun k => out k = x),
              (inclObs h (K k))ᴴ * Y * inclObs h (K k)))
    ∧ (∀ z w : Quasilocal ι Q, phaseAllQ (z * w) = phaseAllQ z * phaseAllQ w)
    ∧ (∀ z : Quasilocal ι Q, ‖phaseAllQ (ι := ι) (Q := Q) z‖ = ‖z‖)
    ∧ (∀ (n : ℕ) (β : Fin n → Quasilocal ι Q), IsQInstrument β → IsFiniteSupport β →
        phaseAllQ (ι := ι) (Q := Q) ≠ qTotal β) :=
  ⟨fun _ β => finiteSupport_iff_kraus β, fun _ _ _ _ h K out x Y => qBranch_stage_inclObs h K out x Y,
    phaseAllQ_mul, norm_phaseAllQ, fun _ β hβ hfs => phaseAll_not_finiteSupport β hβ hfs⟩

end Summary

#print axioms qBranch_add
#print axioms qBranch_smul
#print axioms qBranch_zero
#print axioms qBranch_star_mul_self
#print axioms sum_qBranch
#print axioms qBranch_sum_one
#print axioms qTotal_one
#print axioms qInstrument_of_kraus
#print axioms kraus_of_finiteSupport
#print axioms finiteSupport_iff_kraus
#print axioms qBranch_stage_inclObs
#print axioms qTotal_stage_of_disjoint
#print axioms star_wt_mul
#print axioms wtConj_apply
#print axioms wtU_mul_conjTranspose
#print axioms conjTranspose_mul_wtU
#print axioms wtConj_mul
#print axioms wtConj_one
#print axioms wtConj_add
#print axioms wtConj_smul
#print axioms wtConj_conjTranspose
#print axioms wtConj_injective
#print axioms inclObs_wtConj
#print axioms norm_wtConj
#print axioms wtLoc_ofM
#print axioms wtLoc_mul
#print axioms wtLoc_add
#print axioms wtLoc_smul
#print axioms wtLoc_star
#print axioms wtLoc_sub
#print axioms norm_wtLoc
#print axioms isometry_wtLoc
#print axioms wtQ_coe
#print axioms continuous_wtQ
#print axioms wtQ_stage
#print axioms wtQ_mul
#print axioms wtQ_add
#print axioms wtQ_star
#print axioms norm_wtQ
#print axioms wtQ_one
#print axioms siteWt_unimodular
#print axioms phaseAllWt_unimodular
#print axioms ext_eq_of_mem
#print axioms ext_confRestrict
#print axioms phaseAllWt_compat
#print axioms phaseAllQ_mul
#print axioms phaseAllQ_star
#print axioms norm_phaseAllQ
#print axioms phaseAllQ_stage
#print axioms phaseAllWt_singleton
#print axioms phaseAll_not_finiteSupport
#print axioms instrument_audit_entry_one

end InstrumentCompletion
end OIBridge
