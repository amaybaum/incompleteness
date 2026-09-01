/-
  OIBridge/CoherentExtension.lean — the classification of coherent CPTP extensions of
  a reversible classical action: the correlation-matrix family, the rank-one
  reversibility fork, and the blindness of the classical comb.

  PHASE THREE, ROUND SEVENTEEN, PART TWO. The controlled quotient (part one) fixes the
  carrier; this file classifies what a coherent operational extension of one classical
  intervention can be. Complete positivity is taken in its finite-dimensional Choi
  form: `IsCompletelyPositive Φ := (choiMatrix Φ).PosSemidef`, with
  `choiMatrix Φ (s,a) (t,b) := Φ(E_{st})_{ab}` — Choi's theorem is the definition, as
  is standard in finite dimension.

  §A — THE PSD TOOLBOX. Elementary quadratic-form facts proved with explicit test
  vectors, no spectral machinery: conjugate symmetry of the Hermitian form
  (`hermitian_form_conj`), a null vector of the form is a null vector of the matrix
  (`psd_zero_form_mulVec_zero`, via a single concrete perturbation — no limits), a
  vanishing diagonal entry kills its row and column (`psd_diag_zero_entry_zero`), the
  unit-diagonal off-diagonal bound |C_{st}| ≤ 1 (`psd_unit_diag_entry_bound`), and the
  equality case: a PSD unit-diagonal matrix with unimodular entries is rank one,
  C_{st} = d_s d̄_t (`psd_unimodular_rank_one`).

  §B — THE CLASSIFICATION. If a completely positive `Φ` agrees with a permutation `g`
  on every classical pure state, Φ(E_{ss}) = E_{g(s)g(s)}, then the PSD Choi matrix
  has its diagonal supported on the section s ↦ (s, g s); the zero-diagonal lemma
  kills everything off the section, and what survives is exactly

      ┌────────────────────────────────────────────────────────────────────┐
      │   Φ(E_{st}) = C_{st} · E_{g(s)g(t)},   C ⪰ 0,   C_{ss} = 1:        │
      │   Φ = Ad(P_g) ∘ Schur_C — the correlation-matrix family            │
      │   (`cptpExtension_iff_correlationMatrix`).                         │
      └────────────────────────────────────────────────────────────────────┘

  The family is closed under composition with Schur-multiplied correlation
  (`correlationExtension_comp`), every member is CPTP
  (`correlationExtension_cptp`), and the identity member is the all-ones matrix
  (`correlationExtension_one_eq_id_iff`).

  §C — THE REVERSIBILITY FORK. `reversibleExtension_iff_rankOne`: a member admits a
  CPTP left inverse iff its correlation matrix is rank one with unimodular entries,
  C_{st} = d_s d̄_t — and then the member is exactly unitary conjugation by the
  monomial D·P_g (`rankOne_extension_monomial`, through round thirteen's
  `monomial_conj_apply`). The audit guard is structural: the classical inverse
  ℐ_{g⁻¹} always exists, but the COHERENT composite is Schur multiplication by
  C_{st}·C'_{g(s)g(t)}, identity only when that product is identically one. An
  independent selector: preserving purity of ONE everywhere-supported pure state
  already forces rank one (`purity_selector_rank_one`).

  §D — COMB BLINDNESS. The classical action-labelled comb — diagonal preparations
  pushed through any interleaving of members — depends only on the classical actions,
  never on the correlation matrices (`correlationExtension_diagonal`,
  `combFold_diagonal`, `classicalComb_blind_to_correlation`): classical OI comb
  statistics cannot select the member. The fork is therefore exact:

      classical OI comb        ⟹  the correlation-matrix family of extensions;
      + coherent reversibility ⟹  the monomial unitary intervention lift.

  Standard QM is the rank-one member; the other admissible members are its
  correlation/dephasing extensions, and only coherent data — a reversibility or
  purity principle, not comb statistics — separates them.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.ControlledQuotient

namespace OIBridge
namespace CoherentExtension

open Complex Matrix CoherentLift DynamicsGlue
open scoped ComplexOrder

local notation "conj'" => (starRingEnd ℂ)

/-! ### Section A — the PSD toolbox -/

section Toolbox

variable {P : Type*} [Fintype P] [DecidableEq P]

/-- The standard basis vector as a test vector. -/
def basisVec (p : P) : P → ℂ := fun u => if u = p then 1 else 0

omit [Fintype P] in
theorem star_basisVec (p : P) : star (basisVec p) = basisVec p := by
  funext u
  rw [Pi.star_apply, basisVec]
  by_cases h : u = p
  · rw [if_pos h, star_one]
  · rw [if_neg h, star_zero]

theorem basisVec_mulVec (M : Matrix P P ℂ) (p : P) :
    M.mulVec (basisVec p) = fun q => M q p := by
  funext q
  rw [Matrix.mulVec, dotProduct]
  rw [Finset.sum_congr rfl fun v _ => show M q v * basisVec p v
      = if v = p then M q v else 0 from by
    rw [basisVec]
    by_cases h : v = p
    · rw [if_pos h, if_pos h, mul_one]
    · rw [if_neg h, if_neg h, mul_zero]]
  exact Finset.sum_ite_eq_of_mem' Finset.univ p (fun v => M q v) (Finset.mem_univ p)

theorem basisVec_dot (v : P → ℂ) (p : P) : star (basisVec p) ⬝ᵥ v = v p := by
  rw [star_basisVec, dotProduct]
  rw [Finset.sum_congr rfl fun u _ => show basisVec p u * v u
      = if u = p then v u else 0 from by
    rw [basisVec]
    by_cases h : u = p
    · rw [if_pos h, if_pos h, one_mul]
    · rw [if_neg h, if_neg h, zero_mul]]
  exact Finset.sum_ite_eq_of_mem' Finset.univ p v (Finset.mem_univ p)

/-- The Hermitian form of a basis pair is the matrix entry. -/
theorem form_basis (M : Matrix P P ℂ) (p q : P) :
    star (basisVec p) ⬝ᵥ M.mulVec (basisVec q) = M p q := by
  rw [basisVec_mulVec, basisVec_dot]

omit [DecidableEq P] in
/-- Conjugate symmetry of the Hermitian form. -/
theorem hermitian_form_conj {M : Matrix P P ℂ} (hM : M.IsHermitian) (x y : P → ℂ) :
    star x ⬝ᵥ M.mulVec y = conj' (star y ⬝ᵥ M.mulVec x) := by
  have expand : ∀ p q : P → ℂ, star p ⬝ᵥ M.mulVec q
      = ∑ u, ∑ v, conj' (p u) * M u v * q v := by
    intro p q
    rw [dotProduct]
    refine Finset.sum_congr rfl fun u _ => ?_
    rw [Pi.star_apply, Complex.star_def, Matrix.mulVec, dotProduct,
      Finset.mul_sum]
    exact Finset.sum_congr rfl fun v _ => by ring
  rw [expand, expand, map_sum]
  rw [show (∑ u, conj' (∑ v, conj' (y u) * M u v * x v))
      = ∑ u, ∑ v, conj' (x v) * M v u * y u from
    Finset.sum_congr rfl fun u _ => by
      rw [map_sum]
      refine Finset.sum_congr rfl fun v _ => ?_
      rw [map_mul, map_mul, Complex.conj_conj,
        show conj' (M u v) = M v u from by
          rw [← Complex.star_def]
          exact hM.apply v u]
      ring]
  exact Finset.sum_comm

/-- **A null vector of the form is a null vector of the matrix** — proved with one
concrete perturbation vector, no limiting argument. -/
theorem psd_zero_form_mulVec_zero {M : Matrix P P ℂ} (hM : M.PosSemidef)
    {x : P → ℂ} (hx : star x ⬝ᵥ M.mulVec x = 0) (t : P) : M.mulVec x t = 0 := by
  set z := M.mulVec x t with hz
  obtain ⟨hre, him⟩ := Complex.nonneg_iff.mp (hM.diag_nonneg (i := t))
  have hcre : M t t = (((M t t).re : ℝ) : ℂ) :=
    Complex.ext (by rw [Complex.ofReal_re]) (by rw [Complex.ofReal_im, ← him])
  set c := (M t t).re with hc
  set δ : ℝ := 1 / (c + 1) with hδ
  have hδ0 : 0 < δ := by
    rw [hδ]
    exact one_div_pos.mpr (by linarith)
  set w : ℂ := ((-δ : ℝ) : ℂ) * z with hw
  have hse : star (basisVec t) ⬝ᵥ M.mulVec x = z := basisVec_dot (M.mulVec x) t
  have hxe : star x ⬝ᵥ M.mulVec (basisVec t) = conj' z := by
    rw [hermitian_form_conj hM.1, hse]
  have hee : star (basisVec t) ⬝ᵥ M.mulVec (basisVec t) = M t t := form_basis M t t
  have hval : star (x + w • basisVec t) ⬝ᵥ M.mulVec (x + w • basisVec t)
      = (((Complex.normSq z * (δ * δ * c - 2 * δ)) : ℝ) : ℂ) := by
    rw [star_add, star_smul, Matrix.mulVec_add, Matrix.mulVec_smul,
      add_dotProduct, dotProduct_add, dotProduct_add,
      smul_dotProduct, smul_dotProduct, dotProduct_smul, dotProduct_smul,
      hx, hse, hxe, hee, hcre, hw]
    simp only [star_mul', Complex.star_def, Complex.conj_ofReal, smul_eq_mul]
    push_cast
    linear_combination ((δ : ℂ) * (δ : ℂ) * (c : ℂ) - 2 * (δ : ℂ)) * Complex.mul_conj z
  have hkey := hM.dotProduct_mulVec_nonneg (x + w • basisVec t)
  rw [hval] at hkey
  have hreal : 0 ≤ Complex.normSq z * (δ * δ * c - 2 * δ) :=
    Complex.zero_le_real.mp hkey
  have hneg : δ * δ * c - 2 * δ < 0 := by
    have h1 : δ * c < 2 := by
      rw [hδ, div_mul_eq_mul_div, one_mul, div_lt_iff₀ (by linarith)]
      linarith
    nlinarith
  have h0 : Complex.normSq z = 0 := by
    nlinarith [Complex.normSq_nonneg z]
  exact Complex.normSq_eq_zero.mp h0

/-- A vanishing diagonal entry of a PSD matrix kills its row and its column. -/
theorem psd_diag_zero_entry_zero {M : Matrix P P ℂ} (hM : M.PosSemidef) {p : P}
    (hp : M p p = 0) (q : P) : M p q = 0 ∧ M q p = 0 := by
  have hform : star (basisVec p) ⬝ᵥ M.mulVec (basisVec p) = 0 := by
    rw [form_basis, hp]
  have hcol : M q p = 0 := by
    have h1 := psd_zero_form_mulVec_zero hM hform q
    rwa [basisVec_mulVec] at h1
  refine ⟨?_, hcol⟩
  have h2 := hM.1.apply p q
  rw [hcol, star_zero] at h2
  exact h2.symm

/-- The unit-diagonal off-diagonal bound: every entry of a PSD correlation matrix has
modulus at most one. -/
theorem psd_unit_diag_entry_bound {C : Matrix P P ℂ} (hC : C.PosSemidef)
    (hdiag : ∀ s, C s s = 1) (s t : P) : Complex.normSq (C s t) ≤ 1 := by
  have hts : C t s = conj' (C s t) := by
    rw [← Complex.star_def]
    exact (hC.1.apply t s).symm
  have hval : star ((-(C s t)) • basisVec s + basisVec t)
      ⬝ᵥ C.mulVec ((-(C s t)) • basisVec s + basisVec t)
      = (((1 - Complex.normSq (C s t)) : ℝ) : ℂ) := by
    rw [star_add, star_smul, Matrix.mulVec_add, Matrix.mulVec_smul,
      add_dotProduct, dotProduct_add, dotProduct_add,
      smul_dotProduct, smul_dotProduct, dotProduct_smul, dotProduct_smul,
      form_basis, form_basis, form_basis, form_basis,
      hdiag s, hdiag t, hts]
    simp only [star_neg, Complex.star_def, smul_eq_mul]
    push_cast
    linear_combination (-(1 : ℂ)) * Complex.mul_conj (C s t)
  have hkey := hC.dotProduct_mulVec_nonneg ((-(C s t)) • basisVec s + basisVec t)
  rw [hval] at hkey
  have := Complex.zero_le_real.mp hkey
  linarith

/-- **THE EQUALITY CASE**: a PSD unit-diagonal matrix all of whose entries are
unimodular is rank one — the correlation matrix of a pure phase family. -/
theorem psd_unimodular_rank_one [Nonempty P] {C : Matrix P P ℂ}
    (hC : C.PosSemidef) (hdiag : ∀ s, C s s = 1)
    (huni : ∀ s t, C s t * conj' (C s t) = 1) :
    ∃ d : P → ℂ, (∀ s, d s * conj' (d s) = 1) ∧ ∀ s t, C s t = d s * conj' (d t) := by
  set s₀ := Classical.arbitrary P with hs₀
  refine ⟨fun t => C t s₀, fun s => huni s s₀, fun s t => ?_⟩
  have hcs : C s s₀ = conj' (C s₀ s) := by
    rw [← Complex.star_def]
    exact (hC.1.apply s s₀).symm
  have hform : star (basisVec s + (-(C s₀ s)) • basisVec s₀)
      ⬝ᵥ C.mulVec (basisVec s + (-(C s₀ s)) • basisVec s₀) = 0 := by
    rw [star_add, star_smul, Matrix.mulVec_add, Matrix.mulVec_smul,
      add_dotProduct, dotProduct_add, dotProduct_add,
      smul_dotProduct, smul_dotProduct, dotProduct_smul, dotProduct_smul,
      form_basis, form_basis, form_basis, form_basis,
      hdiag s, hdiag s₀, hcs]
    simp only [star_neg, Complex.star_def, smul_eq_mul]
    linear_combination (-(1 : ℂ)) * huni s₀ s
  have h1 := psd_zero_form_mulVec_zero hC hform t
  rw [Matrix.mulVec_add, Matrix.mulVec_smul, Pi.add_apply, Pi.smul_apply,
    basisVec_mulVec, basisVec_mulVec, smul_eq_mul] at h1
  have h2 : C t s = C s₀ s * C t s₀ := by linear_combination h1
  have h3 : C s t = conj' (C t s) := by
    rw [← Complex.star_def]
    exact (hC.1.apply s t).symm
  rw [h3, h2, map_mul, ← hcs]

end Toolbox

/-! ### Section B — Choi form and the classification -/

variable {S : Type*} [Fintype S] [DecidableEq S]

/-- The Choi matrix of a linear map on the matrix algebra:
`choiMatrix Φ (s,a) (t,b) = Φ(E_{st})_{ab}`. -/
def choiMatrix (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) :
    Matrix (S × S) (S × S) ℂ :=
  Matrix.of fun p q => Φ (Matrix.single p.1 q.1 1) p.2 q.2

/-- Complete positivity, in its finite-dimensional Choi form. -/
def IsCompletelyPositive (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  (choiMatrix Φ).PosSemidef

/-- Trace preservation. -/
def IsTracePreserving (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  ∀ X : Matrix S S ℂ, (Φ X).trace = X.trace

/-- A quantum channel, in finite dimension. -/
def IsCPTP (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) : Prop :=
  IsCompletelyPositive Φ ∧ IsTracePreserving Φ

/-- Agreement with a classical action on every classical pure state. -/
def ClassicallyRealizes (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)
    (g : Equiv.Perm S) : Prop :=
  ∀ s : S, Φ (Matrix.single s s 1) = Matrix.single (g s) (g s) 1

/-- **The correlation-matrix family**: transport along the classical action,
Schur-multiplied by a correlation matrix — `Ad(P_g) ∘ Schur_C`. -/
def correlationExtension (g : Equiv.Perm S) (C : Matrix S S ℂ) :
    Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ where
  toFun X := Matrix.of fun a b =>
    C (g.symm a) (g.symm b) * X (g.symm a) (g.symm b)
  map_add' X Y := by
    ext a b
    show C (g.symm a) (g.symm b)
        * (X (g.symm a) (g.symm b) + Y (g.symm a) (g.symm b))
      = C (g.symm a) (g.symm b) * X (g.symm a) (g.symm b)
        + C (g.symm a) (g.symm b) * Y (g.symm a) (g.symm b)
    exact mul_add _ _ _
  map_smul' c X := by
    ext a b
    show C (g.symm a) (g.symm b) * (c * X (g.symm a) (g.symm b))
      = c * (C (g.symm a) (g.symm b) * X (g.symm a) (g.symm b))
    ring

omit [Fintype S] in
theorem single_entry (s t a b : S) :
    Matrix.single s t (1 : ℂ) a b = if s = a ∧ t = b then 1 else 0 := rfl

omit [Fintype S] in
/-- The family on matrix units: transport and Schur weight. -/
theorem correlationExtension_single (g : Equiv.Perm S) (C : Matrix S S ℂ)
    (s t : S) :
    correlationExtension g C (Matrix.single s t 1)
      = C s t • Matrix.single (g s) (g t) 1 := by
  ext a b
  rw [Matrix.smul_apply, smul_eq_mul]
  show C (g.symm a) (g.symm b) * Matrix.single s t 1 (g.symm a) (g.symm b)
    = C s t * Matrix.single (g s) (g t) 1 a b
  rw [single_entry, single_entry]
  by_cases h1 : g s = a
  · by_cases h2 : g t = b
    · have hs : g.symm a = s := by rw [← h1, Equiv.symm_apply_apply]
      have ht : g.symm b = t := by rw [← h2, Equiv.symm_apply_apply]
      rw [hs, ht, if_pos ⟨rfl, rfl⟩, if_pos ⟨h1, h2⟩]
    · rw [if_neg fun hh => h2 (by rw [hh.2, Equiv.apply_symm_apply]),
        if_neg fun hh => h2 hh.2, mul_zero, mul_zero]
  · rw [if_neg fun hh => h1 (by rw [hh.1, Equiv.apply_symm_apply]),
      if_neg fun hh => h1 hh.1, mul_zero, mul_zero]

omit [Fintype S] in
/-- Every unit-diagonal member classically realizes its action. -/
theorem correlationExtension_classical (g : Equiv.Perm S) (C : Matrix S S ℂ)
    (hdiag : ∀ s, C s s = 1) :
    ClassicallyRealizes (correlationExtension g C) g := fun s => by
  rw [correlationExtension_single, hdiag s, one_smul]

/-- The section embedding along the graph of `g`. -/
def sectionProj (g : Equiv.Perm S) : Matrix S (S × S) ℂ :=
  Matrix.of fun u p => if p = (u, g u) then 1 else 0

/-- Collapsing a sum against the graph indicator. -/
theorem embed_sum (g : Equiv.Perm S) (v : S → ℂ) (p : S × S) :
    (∑ u, (if p = (u, g u) then (1 : ℂ) else 0) * v u)
      = if p.2 = g p.1 then v p.1 else 0 := by
  by_cases hB : p.2 = g p.1
  · have hterm : ∀ u, (if p = (u, g u) then (1 : ℂ) else 0) * v u
        = if u = p.1 then v u else 0 := by
      intro u
      by_cases hu : u = p.1
      · rw [if_pos hu, if_pos (show p = (u, g u) from Prod.ext_iff.mpr
          ⟨hu.symm, by rw [hB, hu]⟩), one_mul]
      · rw [if_neg hu, if_neg (fun hp => hu (congrArg Prod.fst hp).symm), zero_mul]
    rw [if_pos hB, Finset.sum_congr rfl fun u _ => hterm u]
    exact Finset.sum_ite_eq_of_mem' Finset.univ p.1 v (Finset.mem_univ p.1)
  · rw [if_neg hB]
    refine Finset.sum_eq_zero fun u _ => ?_
    rw [if_neg (fun hp => hB (by
      rw [show p.2 = g u from congrArg Prod.snd hp,
        show u = p.1 from (congrArg Prod.fst hp).symm])), zero_mul]

/-- The Choi matrix of a family member is the correlation matrix transported onto the
graph section: `J = Pᴴ C P`. -/
theorem choi_correlation (g : Equiv.Perm S) (C : Matrix S S ℂ) :
    choiMatrix (correlationExtension g C)
      = (sectionProj g)ᴴ * C * sectionProj g := by
  have hPCP : ∀ p q : S × S, ((sectionProj g)ᴴ * C * sectionProj g) p q
      = (if p.2 = g p.1 then (1 : ℂ) else 0) * C p.1 q.1
        * (if q.2 = g q.1 then (1 : ℂ) else 0) := by
    intro p q
    rw [Matrix.mul_apply]
    have hrow : ∀ v, ((sectionProj g)ᴴ * C) p v
        = (if p.2 = g p.1 then (1 : ℂ) else 0) * C p.1 v := by
      intro v
      rw [Matrix.mul_apply]
      rw [Finset.sum_congr rfl fun u _ => by
        rw [Matrix.conjTranspose_apply,
          show star (sectionProj g u p) = (if p = (u, g u) then (1 : ℂ) else 0)
            from by
            show star (if p = (u, g u) then (1 : ℂ) else 0) = _
            by_cases hp : p = (u, g u)
            · rw [if_pos hp, star_one]
            · rw [if_neg hp, star_zero]]]
      rw [embed_sum g (fun u => C u v) p]
      by_cases hB : p.2 = g p.1
      · rw [if_pos hB, if_pos hB, one_mul]
      · rw [if_neg hB, if_neg hB, zero_mul]
    rw [Finset.sum_congr rfl fun v _ => by rw [hrow v]]
    rw [show (∑ v, (if p.2 = g p.1 then (1 : ℂ) else 0) * C p.1 v
          * sectionProj g v q)
        = (if p.2 = g p.1 then (1 : ℂ) else 0)
          * ∑ v, (if q = (v, g v) then (1 : ℂ) else 0) * C p.1 v from by
      rw [Finset.mul_sum]
      refine Finset.sum_congr rfl fun v _ => ?_
      rw [show sectionProj g v q = (if q = (v, g v) then (1 : ℂ) else 0) from rfl]
      ring]
    rw [embed_sum g (fun v => C p.1 v) q]
    by_cases hq : q.2 = g q.1
    · rw [if_pos hq, if_pos hq, mul_one]
    · rw [if_neg hq, if_neg hq, mul_zero, mul_zero]
  ext p q
  rw [hPCP p q]
  show correlationExtension g C (Matrix.single p.1 q.1 1) p.2 q.2 = _
  rw [correlationExtension_single, Matrix.smul_apply, smul_eq_mul, single_entry]
  by_cases h1 : g p.1 = p.2
  · by_cases h2 : g q.1 = q.2
    · rw [if_pos ⟨h1, h2⟩, if_pos h1.symm, if_pos h2.symm, mul_one, one_mul, mul_one]
    · rw [if_neg fun hh => h2 hh.2, if_pos h1.symm,
        if_neg (fun hh : q.2 = g q.1 => h2 hh.symm), mul_zero, one_mul, mul_zero]
  · rw [if_neg fun hh => h1 hh.1,
      if_neg (fun hh : p.2 = g p.1 => h1 hh.symm), mul_zero, zero_mul, zero_mul]

/-- Every PSD correlation matrix gives a completely positive member. -/
theorem correlationExtension_completelyPositive (g : Equiv.Perm S)
    (C : Matrix S S ℂ) (hpsd : C.PosSemidef) :
    IsCompletelyPositive (correlationExtension g C) := by
  show (choiMatrix (correlationExtension g C)).PosSemidef
  rw [choi_correlation]
  have h := hpsd.mul_mul_conjTranspose_same (sectionProj g)ᴴ
  rwa [Matrix.conjTranspose_conjTranspose] at h

omit [DecidableEq S] in
/-- Unit diagonal gives trace preservation. -/
theorem correlationExtension_trace (g : Equiv.Perm S) (C : Matrix S S ℂ)
    (hdiag : ∀ s, C s s = 1) :
    IsTracePreserving (correlationExtension g C) := by
  intro X
  rw [Matrix.trace, Matrix.trace]
  rw [Finset.sum_congr rfl fun a _ => show (correlationExtension g C X).diag a
      = X (g.symm a) (g.symm a) from by
    rw [Matrix.diag_apply]
    show C (g.symm a) (g.symm a) * X (g.symm a) (g.symm a) = _
    rw [hdiag, one_mul]]
  rw [show (∑ a, X (g.symm a) (g.symm a)) = ∑ s, X s s from
    Equiv.sum_comp g.symm (fun s => X s s)]
  exact Finset.sum_congr rfl fun s _ => (Matrix.diag_apply X s).symm

/-- **Every member of the family is a channel.** -/
theorem correlationExtension_cptp (g : Equiv.Perm S) (C : Matrix S S ℂ)
    (hpsd : C.PosSemidef) (hdiag : ∀ s, C s s = 1) :
    IsCPTP (correlationExtension g C) :=
  ⟨correlationExtension_completelyPositive g C hpsd,
    correlationExtension_trace g C hdiag⟩

omit [Fintype S] in
theorem single_eq_smul (s t : S) (c : ℂ) :
    Matrix.single s t c = c • Matrix.single s t 1 := by
  ext a b
  rw [Matrix.smul_apply, smul_eq_mul, single_entry]
  show (if s = a ∧ t = b then c else 0) = _
  by_cases h : s = a ∧ t = b
  · rw [if_pos h, if_pos h, mul_one]
  · rw [if_neg h, if_neg h, mul_zero]

/-- **THE CLASSIFICATION, forward direction.** A completely positive map that agrees
with a classical action on every classical pure state is a member of the
correlation-matrix family: purity of the classical outputs pins the Choi diagonal to
the graph section, positive semidefiniteness kills everything off it, and the section
principal block is the correlation matrix. -/
theorem cptp_classical_forces_correlation (g : Equiv.Perm S)
    (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) (hCP : IsCompletelyPositive Φ)
    (hcl : ClassicallyRealizes Φ g) :
    ∃ C : Matrix S S ℂ, C.PosSemidef ∧ (∀ s, C s s = 1)
      ∧ Φ = correlationExtension g C := by
  have hJdiag : ∀ s a, choiMatrix Φ (s, a) (s, a) = if g s = a then 1 else 0 := by
    intro s a
    show Φ (Matrix.single s s 1) a a = _
    rw [hcl s, single_entry]
    by_cases h : g s = a
    · rw [if_pos ⟨h, h⟩, if_pos h]
    · rw [if_neg fun hh => h hh.1, if_neg h]
  have hoff : ∀ (s : S) (a : S) (q : S × S), a ≠ g s
      → choiMatrix Φ (s, a) q = 0 ∧ choiMatrix Φ q (s, a) = 0 := by
    intro s a q ha
    exact psd_diag_zero_entry_zero hCP (by
      rw [hJdiag s a, if_neg fun h => ha h.symm]) q
  set C : Matrix S S ℂ := Matrix.of fun s t => choiMatrix Φ (s, g s) (t, g t)
    with hCdef
  have hbasis : ∀ s t, Φ (Matrix.single s t 1)
      = C s t • Matrix.single (g s) (g t) 1 := by
    intro s t
    ext a b
    rw [Matrix.smul_apply, smul_eq_mul, single_entry]
    show choiMatrix Φ (s, a) (t, b) = _
    by_cases h1 : g s = a
    · by_cases h2 : g t = b
      · rw [if_pos ⟨h1, h2⟩, mul_one, ← h1, ← h2]
        rfl
      · rw [if_neg fun hh => h2 hh.2, mul_zero]
        exact (hoff t b (s, a) fun hb => h2 hb.symm).2
    · rw [if_neg fun hh => h1 hh.1, mul_zero]
      exact (hoff s a (t, b) fun ha => h1 ha.symm).1
  have hCpsd : C.PosSemidef := by
    have hC2 : C = sectionProj g * choiMatrix Φ * (sectionProj g)ᴴ := by
      ext s t
      show choiMatrix Φ (s, g s) (t, g t)
        = (sectionProj g * choiMatrix Φ * (sectionProj g)ᴴ) s t
      rw [Matrix.mul_apply]
      rw [Finset.sum_congr rfl fun q _ => by
        rw [Matrix.mul_apply, Matrix.conjTranspose_apply,
          show star (sectionProj g t q) = (if q = (t, g t) then (1 : ℂ) else 0)
            from by
            show star (if q = (t, g t) then (1 : ℂ) else 0) = _
            by_cases hq : q = (t, g t)
            · rw [if_pos hq, star_one]
            · rw [if_neg hq, star_zero],
          show (∑ p, sectionProj g s p * choiMatrix Φ p q)
              = choiMatrix Φ (s, g s) q from by
            rw [Finset.sum_congr rfl fun p _ =>
              show sectionProj g s p * choiMatrix Φ p q
                = if p = (s, g s) then choiMatrix Φ p q else 0 from by
              show (if p = (s, g s) then (1 : ℂ) else 0) * _ = _
              by_cases hp : p = (s, g s)
              · rw [if_pos hp, if_pos hp, one_mul]
              · rw [if_neg hp, if_neg hp, zero_mul]]
            exact Finset.sum_ite_eq_of_mem' Finset.univ (s, g s)
              (fun p => choiMatrix Φ p q) (Finset.mem_univ _)]]
      rw [Finset.sum_congr rfl fun q _ =>
        show choiMatrix Φ (s, g s) q * (if q = (t, g t) then (1 : ℂ) else 0)
          = if q = (t, g t) then choiMatrix Φ (s, g s) q else 0 from by
        by_cases hq : q = (t, g t)
        · rw [if_pos hq, if_pos hq, mul_one]
        · rw [if_neg hq, if_neg hq, mul_zero]]
      rw [Finset.sum_ite_eq_of_mem' Finset.univ (t, g t)
        (fun q => choiMatrix Φ (s, g s) q) (Finset.mem_univ _)]
    rw [hC2]
    exact hCP.mul_mul_conjTranspose_same (sectionProj g)
  have hCdiag : ∀ s, C s s = 1 := by
    intro s
    show choiMatrix Φ (s, g s) (s, g s) = 1
    rw [hJdiag s (g s), if_pos rfl]
  refine ⟨C, hCpsd, hCdiag, ?_⟩
  refine LinearMap.ext fun X => ?_
  conv_lhs => rw [Matrix.matrix_eq_sum_single X]
  conv_rhs => rw [Matrix.matrix_eq_sum_single X]
  rw [map_sum, map_sum]
  refine Finset.sum_congr rfl fun s _ => ?_
  rw [map_sum, map_sum]
  refine Finset.sum_congr rfl fun t _ => ?_
  rw [single_eq_smul, map_smul, map_smul, hbasis, correlationExtension_single]

/-- **THE CLASSIFICATION.** Complete positivity plus classical agreement is EXACTLY
membership of the correlation-matrix family with a PSD unit-diagonal correlation. -/
theorem cptpExtension_iff_correlationMatrix (g : Equiv.Perm S)
    (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) :
    (IsCompletelyPositive Φ ∧ ClassicallyRealizes Φ g)
      ↔ ∃ C : Matrix S S ℂ, C.PosSemidef ∧ (∀ s, C s s = 1)
          ∧ Φ = correlationExtension g C := by
  constructor
  · rintro ⟨hCP, hcl⟩
    exact cptp_classical_forces_correlation g Φ hCP hcl
  · rintro ⟨C, hpsd, hdiag, rfl⟩
    exact ⟨correlationExtension_completelyPositive g C hpsd,
      correlationExtension_classical g C hdiag⟩

/-! ### Section C — the reversibility fork -/

omit [Fintype S] [DecidableEq S] in
/-- The family composes by composing actions and Schur-multiplying correlations. -/
theorem correlationExtension_comp (g g' : Equiv.Perm S) (C C' : Matrix S S ℂ) :
    (correlationExtension g' C').comp (correlationExtension g C)
      = correlationExtension (g' * g)
          (Matrix.of fun s t => C s t * C' (g s) (g t)) := by
  refine LinearMap.ext fun X => ?_
  ext a b
  show C' (g'.symm a) (g'.symm b)
      * (C (g.symm (g'.symm a)) (g.symm (g'.symm b))
        * X (g.symm (g'.symm a)) (g.symm (g'.symm b)))
    = (Matrix.of fun s t => C s t * C' (g s) (g t))
          ((g' * g).symm a) ((g' * g).symm b)
        * X ((g' * g).symm a) ((g' * g).symm b)
  rw [show ((g' * g).symm a) = g.symm (g'.symm a) from rfl,
    show ((g' * g).symm b) = g.symm (g'.symm b) from rfl,
    Matrix.of_apply, Equiv.apply_symm_apply, Equiv.apply_symm_apply]
  ring

omit [Fintype S] in
/-- The identity member of the family is the all-ones correlation. -/
theorem correlationExtension_one_eq_id_iff (C : Matrix S S ℂ) :
    correlationExtension 1 C = LinearMap.id ↔ ∀ s t, C s t = 1 := by
  constructor
  · intro h s t
    have h1 := LinearMap.congr_fun h (Matrix.single s t 1)
    have h2 := congrFun (congrFun h1 s) t
    rwa [show correlationExtension 1 C (Matrix.single s t 1) s t = C s t from by
        show C ((1 : Equiv.Perm S).symm s) ((1 : Equiv.Perm S).symm t)
            * Matrix.single s t 1 ((1 : Equiv.Perm S).symm s)
              ((1 : Equiv.Perm S).symm t) = C s t
        rw [show (1 : Equiv.Perm S).symm s = s from rfl,
          show (1 : Equiv.Perm S).symm t = t from rfl,
          Matrix.single_apply_same, mul_one],
      show (LinearMap.id (Matrix.single s t (1 : ℂ))) s t = 1 from
        Matrix.single_apply_same s t 1] at h2
  · intro h
    refine LinearMap.ext fun X => ?_
    ext a b
    show C ((1 : Equiv.Perm S).symm a) ((1 : Equiv.Perm S).symm b)
        * X ((1 : Equiv.Perm S).symm a) ((1 : Equiv.Perm S).symm b) = X a b
    rw [show (1 : Equiv.Perm S).symm a = a from rfl,
      show (1 : Equiv.Perm S).symm b = b from rfl, h a b, one_mul]

/-- **THE REVERSIBILITY FORK.** A member of the family admits a CPTP left inverse
exactly when its correlation matrix is a rank-one unimodular phase matrix — the
member is then the unitary monomial lift, and everything else in the family is
irreversibly dephasing. -/
theorem reversibleExtension_iff_rankOne [Nonempty S] (g : Equiv.Perm S)
    (C : Matrix S S ℂ) (hpsd : C.PosSemidef) (hdiag : ∀ s, C s s = 1) :
    (∃ Ψ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ, IsCPTP Ψ
        ∧ Ψ.comp (correlationExtension g C) = LinearMap.id)
      ↔ ∃ d : S → ℂ, (∀ s, d s * conj' (d s) = 1)
          ∧ ∀ s t, C s t = d s * conj' (d t) := by
  constructor
  · rintro ⟨Ψ, ⟨hΨcp, _⟩, hcomp⟩
    have hΨcl : ClassicallyRealizes Ψ g⁻¹ := by
      intro s'
      have h1 : correlationExtension g C
          (Matrix.single (g.symm s') (g.symm s') 1) = Matrix.single s' s' 1 := by
        rw [correlationExtension_single, hdiag, one_smul, Equiv.apply_symm_apply]
      have h2 := LinearMap.congr_fun hcomp
        (Matrix.single (g.symm s') (g.symm s') 1)
      rw [LinearMap.comp_apply, h1, LinearMap.id_apply] at h2
      rw [show (g⁻¹ : Equiv.Perm S) s' = g.symm s' from by
        rw [Equiv.Perm.inv_def]]
      exact h2
    obtain ⟨C', hC'psd, hC'diag, hΨeq⟩ :=
      cptp_classical_forces_correlation g⁻¹ Ψ hΨcp hΨcl
    rw [hΨeq, correlationExtension_comp, inv_mul_cancel] at hcomp
    have hprod : ∀ s t, C s t * C' (g s) (g t) = 1 := by
      intro s t
      have h3 := (correlationExtension_one_eq_id_iff _).mp hcomp s t
      rwa [Matrix.of_apply] at h3
    have huni : ∀ s t, C s t * conj' (C s t) = 1 := by
      intro s t
      have hb := psd_unit_diag_entry_bound hpsd hdiag s t
      have hb' := psd_unit_diag_entry_bound hC'psd hC'diag (g s) (g t)
      have hns : Complex.normSq (C s t) * Complex.normSq (C' (g s) (g t)) = 1 := by
        rw [← Complex.normSq_mul, hprod s t, Complex.normSq_one]
      have h1 : Complex.normSq (C s t) = 1 := by
        nlinarith [Complex.normSq_nonneg (C s t),
          Complex.normSq_nonneg (C' (g s) (g t))]
      rw [Complex.mul_conj, h1, Complex.ofReal_one]
    exact psd_unimodular_rank_one hpsd hdiag huni
  · rintro ⟨d, hd, hC⟩
    refine ⟨correlationExtension g⁻¹
      (Matrix.of fun a b => conj' (d ((g⁻¹ : Equiv.Perm S) a))
        * d ((g⁻¹ : Equiv.Perm S) b)), ⟨⟨?_, ?_⟩, ?_⟩⟩
    · refine correlationExtension_completelyPositive _ _ ?_
      rw [show (Matrix.of fun a b => conj' (d ((g⁻¹ : Equiv.Perm S) a))
            * d ((g⁻¹ : Equiv.Perm S) b))
          = Matrix.vecMulVec (fun a => conj' (d ((g⁻¹ : Equiv.Perm S) a)))
              (star fun a => conj' (d ((g⁻¹ : Equiv.Perm S) a))) from by
        ext a b
        rw [Matrix.vecMulVec_apply, Pi.star_apply, Complex.star_def,
          Complex.conj_conj]
        rfl]
      exact Matrix.posSemidef_vecMulVec_self_star _
    · refine correlationExtension_trace _ _ ?_
      intro a
      rw [Matrix.of_apply, mul_comm]
      exact hd ((g⁻¹ : Equiv.Perm S) a)
    · rw [correlationExtension_comp, inv_mul_cancel]
      refine (correlationExtension_one_eq_id_iff _).mpr fun s t => ?_
      rw [Matrix.of_apply, Matrix.of_apply, hC s t,
        show (g⁻¹ : Equiv.Perm S) (g s) = s from by
          rw [Equiv.Perm.inv_def, Equiv.symm_apply_apply],
        show (g⁻¹ : Equiv.Perm S) (g t) = t from by
          rw [Equiv.Perm.inv_def, Equiv.symm_apply_apply]]
      linear_combination (d t * conj' (d t)) * hd s + hd t

/-- **The rank-one member is the monomial unitary lift**: conjugation by `D·P_g` —
round thirteen's monomial form, now as the unique reversible coherent extension. -/
theorem rankOne_extension_monomial (g : Equiv.Perm S) (d : S → ℂ)
    (X : Matrix S S ℂ) :
    correlationExtension g (Matrix.of fun s t => d s * conj' (d t)) X
      = (Matrix.diagonal (fun a => d (g.symm a)) * permMatrix g) * X
        * (Matrix.diagonal (fun a => d (g.symm a)) * permMatrix g)ᴴ := by
  ext a b
  rw [monomial_conj_apply]
  show (Matrix.of fun s t => d s * conj' (d t)) (g.symm a) (g.symm b)
      * X (g.symm a) (g.symm b)
    = d (g.symm a) * conj' (d (g.symm b)) * X (g.symm a) (g.symm b)
  rw [Matrix.of_apply]

omit [Fintype S] [DecidableEq S] in
/-- **The purity selector**: a member that preserves purity of a single
everywhere-supported pure state already has rank-one correlation. -/
theorem purity_selector_rank_one (g : Equiv.Perm S) (C : Matrix S S ℂ)
    (hdiag : ∀ s, C s s = 1) (ψ χ : S → ℂ) (hψ : ∀ s, ψ s ≠ 0)
    (hpure : correlationExtension g C (Matrix.vecMulVec ψ (star ψ))
      = Matrix.vecMulVec χ (star χ)) :
    ∃ d : S → ℂ, (∀ s, d s * conj' (d s) = 1)
      ∧ ∀ s t, C s t = d s * conj' (d t) := by
  have hentry : ∀ s t, C s t * (ψ s * conj' (ψ t))
      = χ (g s) * conj' (χ (g t)) := by
    intro s t
    have h1 := congrFun (congrFun hpure (g s)) (g t)
    rw [show correlationExtension g C (Matrix.vecMulVec ψ (star ψ)) (g s) (g t)
        = C s t * (ψ s * conj' (ψ t)) from by
      show C (g.symm (g s)) (g.symm (g t))
          * Matrix.vecMulVec ψ (star ψ) (g.symm (g s)) (g.symm (g t)) = _
      rw [Equiv.symm_apply_apply, Equiv.symm_apply_apply,
        Matrix.vecMulVec_apply, Pi.star_apply, Complex.star_def]] at h1
    rw [h1, Matrix.vecMulVec_apply, Pi.star_apply, Complex.star_def]
  have hmod : ∀ s, χ (g s) * conj' (χ (g s)) = ψ s * conj' (ψ s) := by
    intro s
    have h := hentry s s
    rw [hdiag s, one_mul] at h
    exact h.symm
  have hcψ : ∀ s, conj' (ψ s) ≠ 0 := fun s hh => hψ s ((map_eq_zero _).mp hh)
  refine ⟨fun s => χ (g s) * (ψ s)⁻¹, fun s => ?_, fun s t => ?_⟩
  · rw [map_mul, map_inv₀,
      show χ (g s) * (ψ s)⁻¹ * (conj' (χ (g s)) * (conj' (ψ s))⁻¹)
        = (χ (g s) * conj' (χ (g s))) * ((ψ s)⁻¹ * (conj' (ψ s))⁻¹) from by ring,
      hmod s,
      show (ψ s * conj' (ψ s)) * ((ψ s)⁻¹ * (conj' (ψ s))⁻¹)
        = (ψ s * (ψ s)⁻¹) * (conj' (ψ s) * (conj' (ψ s))⁻¹) from by ring,
      mul_inv_cancel₀ (hψ s), mul_inv_cancel₀ (hcψ s), one_mul]
  · have h := hentry s t
    have hne : ψ s * conj' (ψ t) ≠ 0 := mul_ne_zero (hψ s) (hcψ t)
    rw [map_mul, map_inv₀]
    refine mul_right_cancel₀ hne ?_
    rw [h]
    rw [show χ (g s) * (ψ s)⁻¹ * (conj' (χ (g t)) * (conj' (ψ t))⁻¹)
          * (ψ s * conj' (ψ t))
        = (χ (g s) * conj' (χ (g t)))
          * (((ψ s)⁻¹ * ψ s) * ((conj' (ψ t))⁻¹ * conj' (ψ t))) from by ring,
      inv_mul_cancel₀ (hψ s), inv_mul_cancel₀ (hcψ t), one_mul, mul_one]

/-! ### Section D — comb blindness -/

omit [Fintype S] in
/-- The family acts on diagonal preparations by pure classical transport: the
correlation matrix drops out entirely. -/
theorem correlationExtension_diagonal (g : Equiv.Perm S) (C : Matrix S S ℂ)
    (hdiag : ∀ s, C s s = 1) (w : S → ℂ) :
    correlationExtension g C (Matrix.diagonal w)
      = Matrix.diagonal (fun a => w (g.symm a)) := by
  ext a b
  show C (g.symm a) (g.symm b) * Matrix.diagonal w (g.symm a) (g.symm b)
    = Matrix.diagonal (fun a => w (g.symm a)) a b
  by_cases hab : a = b
  · rw [hab, Matrix.diagonal_apply_eq, Matrix.diagonal_apply_eq, hdiag, one_mul]
  · rw [Matrix.diagonal_apply_ne _ (fun h => hab (g.symm.injective h)),
      Matrix.diagonal_apply_ne _ hab, mul_zero]

/-- A classical action-labelled comb: a diagonal preparation pushed through an
interleaving of family members. -/
def combFold (steps : List (Equiv.Perm S × Matrix S S ℂ)) (w : S → ℂ) :
    Matrix S S ℂ :=
  steps.foldl (fun X p => correlationExtension p.1 p.2 X) (Matrix.diagonal w)

/-- The classical transport realized by a comb. -/
def combPerm (steps : List (Equiv.Perm S × Matrix S S ℂ)) : Equiv.Perm S :=
  steps.foldl (fun h p => p.1 * h) 1

/-- The product of the classical actions of a list of permutations. -/
def permProd (l : List (Equiv.Perm S)) : Equiv.Perm S :=
  l.foldl (fun h g => g * h) 1

omit [Fintype S] [DecidableEq S] in
theorem permProd_foldl_init (l : List (Equiv.Perm S)) (h0 : Equiv.Perm S) :
    l.foldl (fun h g => g * h) h0 = permProd l * h0 := by
  induction l generalizing h0 with
  | nil => exact (one_mul h0).symm
  | cons g rest ih =>
      rw [List.foldl_cons, ih (g * h0),
        show permProd (g :: rest) = permProd rest * (g * 1) from by
          show List.foldl (fun h g => g * h) 1 (g :: rest) = _
          rw [List.foldl_cons]
          exact ih (g * 1),
        mul_one, mul_assoc]

omit [Fintype S] [DecidableEq S] in
theorem combPerm_foldl_init (steps : List (Equiv.Perm S × Matrix S S ℂ))
    (h0 : Equiv.Perm S) :
    steps.foldl (fun h p => p.1 * h) h0 = combPerm steps * h0 := by
  induction steps generalizing h0 with
  | nil => exact (one_mul h0).symm
  | cons p rest ih =>
      rw [List.foldl_cons, ih (p.1 * h0),
        show combPerm (p :: rest) = combPerm rest * (p.1 * 1) from by
          show List.foldl (fun h q => q.1 * h) 1 (p :: rest) = _
          rw [List.foldl_cons]
          exact ih (p.1 * 1),
        mul_one, mul_assoc]

omit [Fintype S] [DecidableEq S] in
theorem combPerm_cons (p : Equiv.Perm S × Matrix S S ℂ)
    (rest : List (Equiv.Perm S × Matrix S S ℂ)) :
    combPerm (p :: rest) = combPerm rest * p.1 := by
  show List.foldl (fun h q => q.1 * h) 1 (p :: rest) = combPerm rest * p.1
  rw [List.foldl_cons, combPerm_foldl_init rest (p.1 * 1), mul_one]

omit [Fintype S] in
/-- **Comb evaluation**: any interleaving of unit-diagonal members transports a
diagonal preparation classically — the result depends only on the composed classical
action. -/
theorem combFold_diagonal (steps : List (Equiv.Perm S × Matrix S S ℂ))
    (hsteps : ∀ p ∈ steps, ∀ s, p.2 s s = 1) (w : S → ℂ) :
    combFold steps w = Matrix.diagonal (fun a => w ((combPerm steps).symm a)) := by
  induction steps generalizing w with
  | nil => rfl
  | cons p rest ih =>
      show List.foldl (fun X q => correlationExtension q.1 q.2 X)
          (correlationExtension p.1 p.2 (Matrix.diagonal w)) rest = _
      rw [correlationExtension_diagonal p.1 p.2
        (hsteps p List.mem_cons_self) w]
      rw [show List.foldl (fun X q => correlationExtension q.1 q.2 X)
          (Matrix.diagonal fun a => w (p.1.symm a)) rest
          = combFold rest (fun a => w (p.1.symm a)) from rfl]
      rw [ih (fun q hq => hsteps q (List.mem_cons_of_mem p hq)), combPerm_cons]
      congr 1

omit [Fintype S] [DecidableEq S] in
/-- The classical transport of a comb depends only on the action labels. -/
theorem combPerm_eq_permProd (steps : List (Equiv.Perm S × Matrix S S ℂ)) :
    combPerm steps = permProd (steps.map Prod.fst) := by
  induction steps with
  | nil => rfl
  | cons p rest ih =>
      rw [combPerm_cons, ih, List.map_cons,
        show permProd (p.1 :: rest.map Prod.fst)
          = permProd (rest.map Prod.fst) * p.1 from by
        show List.foldl (fun h g => g * h) 1 (p.1 :: rest.map Prod.fst) = _
        rw [List.foldl_cons, permProd_foldl_init (rest.map Prod.fst) (p.1 * 1),
          mul_one]]

omit [Fintype S] in
/-- **COMB BLINDNESS.** Two combs with the same classical action labels produce
identical statistics on every diagonal preparation, whatever their correlation
matrices: the classical OI comb cannot select the member of the extension family. -/
theorem classicalComb_blind_to_correlation
    (steps steps' : List (Equiv.Perm S × Matrix S S ℂ))
    (hfst : steps.map Prod.fst = steps'.map Prod.fst)
    (h1 : ∀ p ∈ steps, ∀ s, p.2 s s = 1) (h2 : ∀ p ∈ steps', ∀ s, p.2 s s = 1)
    (w : S → ℂ) : combFold steps w = combFold steps' w := by
  rw [combFold_diagonal steps h1 w, combFold_diagonal steps' h2 w,
    combPerm_eq_permProd, combPerm_eq_permProd, hfst]

#print axioms basisVec_mulVec
#print axioms basisVec_dot
#print axioms form_basis
#print axioms hermitian_form_conj
#print axioms psd_zero_form_mulVec_zero
#print axioms psd_diag_zero_entry_zero
#print axioms psd_unit_diag_entry_bound
#print axioms psd_unimodular_rank_one
#print axioms correlationExtension_single
#print axioms correlationExtension_classical
#print axioms embed_sum
#print axioms choi_correlation
#print axioms correlationExtension_completelyPositive
#print axioms correlationExtension_trace
#print axioms correlationExtension_cptp
#print axioms cptp_classical_forces_correlation
#print axioms cptpExtension_iff_correlationMatrix
#print axioms correlationExtension_comp
#print axioms correlationExtension_one_eq_id_iff
#print axioms reversibleExtension_iff_rankOne
#print axioms rankOne_extension_monomial
#print axioms purity_selector_rank_one
#print axioms correlationExtension_diagonal
#print axioms combPerm_cons
#print axioms combFold_diagonal
#print axioms combPerm_eq_permProd
#print axioms classicalComb_blind_to_correlation

end CoherentExtension
end OIBridge
