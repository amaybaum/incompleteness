/-
  OIBridge/OperationalRigidity.lean — phase three, round six: operational separation and
  the order-isomorphism layer of C3b (milestones C3b.1 and C3b.2).

  THE GUARD. Round five (C3a) proved the accessible algebra is irreducible — but trivial
  commutant does NOT imply that an arbitrary data-preserving correspondence between two
  completions is inner. Before any rigidity classification, two completions with identical
  operational data must be shown to induce a genuinely structure-preserving map. That
  requires two exact layers, both delivered here:

  Section A — OPERATIONAL SEPARATION (C3b.1, the well-definedness guard).
    * `line_coefficient_vanish`, `conj_context_entry` — the single-line Dedekind
      extraction and the eigenbasis entry expansion of an s-conjugated context product.
    * `operational_separation` — THE BOXED LEMMA: if `Tr(C·X) = 0` for the normalization
      context, every one-slot context `U_t A_j U_t†`, and every two-slot context
      `U_t A_j U_t† · U_s A_k U_s†`, then `X = 0`. The mechanism chains two SINGLE
      parameter extractions: the t-extraction (round five's engine) kills every
      off-diagonal of `Y = V† X V` and reduces the two-slot datum to the s-expansion of
      one conjugated entry, whose line extraction kills the diagonal. AUDIT FINDING made
      exact by probe F18: ONE-slot contexts do NOT separate — their span has codimension
      `D − rank(diag N_j)` (2 at the (2,2) census carrier, where two distinct exact
      states carry identical one-slot data at every frequency); the two-slot layer is
      what closes the diagonal, exactly as the proof requires. Separation is a theorem
      about temporal DEPTH of the data, not just menu completeness.
    * `sameData_unique_state` — the state-side rigidity: two preparations with identical
      normalization, one-slot, and two-slot branch data are EQUAL. The preparation is
      operationally determined; no gauge freedom survives on the state side.

  Section B — THE DATA-DEFINED MAP (C3b.1, construction).
    * `sameData_combination_transfer` — identical pairing data against a separating state
      family transfers linear relations: `Σ c·G¹ = 0 ⟹ Σ c·G² = 0`. This is precisely
      the well-definedness of "map each accessible context of completion one to its
      data-matched twin", the step that trivial commutant alone cannot supply.
    * `sameData_linear_extension` — the map EXISTS: a ℂ-linear `Φ` with `Φ(G¹_i) = G²_i`
      for every context index, built by factoring the linear-combination map through its
      kernel (no choice of basis, no quotient left open).
    * `accessible_cone_full` — every positive matrix is a finite selective-word image
      `Σ M_i ρ M_i†` of ANY nonzero positive preparation: the accessible state cone is
      the full PSD cone, which is what makes positivity of the data-defined map an
      operational statement (its glue to `Φ` is the C3b.3 assembly).
    * `psd_trace_mul_nonneg` — the pairing positivity: `Tr(A·B) ≥ 0` for PSD `A, B`.

  Section C — ORDER ISOMORPHISM ⟹ JORDAN (C3b.2, kernel-internal Kadison).
    * `projection_extreme` / `extreme_projection` — the operator interval `[0, 1]` has
      the orthogonal projections as EXACTLY its extreme points. One direction is
      order-algebraic (a projection admits no symmetric perturbation inside the
      interval — the PSD kernel/range splitting); the other is spectral (a
      non-projection carries an eigenvalue in `(0,1)` and the explicit perturbation
      `λ(1−λ)` along its eigenvector).
    * `orderIso_maps_projections`, `orderIso_orthogonal` — a unital ℝ-linear bijection
      positive in BOTH directions transports extreme points, hence carries projections
      to projections and orthogonal families to orthogonal families.
    * `orderIso_square` — `Φ(A²) = Φ(A)²` on Hermitians, by the rank-one spectral
      resolution: the image dyads are pairwise-orthogonal projections, so the square
      recombines exactly.
    * `orderIso_jordan` — THE KADISON THEOREM, finite-dimensional, kernel-internal:
      a unital ℝ-linear star-preserving bijection `Φ` of `M_D(ℂ)` with `X ⪰ 0 ⟺
      Φ(X) ⪰ 0` satisfies `Φ(AB + BA) = Φ(A)Φ(B) + Φ(B)Φ(A)` on Hermitians — a Jordan
      ∗-isomorphism, by polarization of `orderIso_square`. No positivity of a single
      direction suffices: probe F18's pinching countercontrol (positive, unital, NOT an
      order isomorphism) violates the Jordan identity exactly; both matrix branches
      `X ↦ WXW†` and `X ↦ WX^TW†` satisfy it, as they must.

  WHAT THIS DOES NOT ESTABLISH. The assembled correspondence between two named
  completions — the instantiation of `Φ` with unitality, star preservation, and
  two-sided positivity discharged from the operational hypotheses (cone + transfer +
  span induction) — is the C3b.3 assembly, where `orderIso_jordan` then hands the
  classification to the unitary/transpose dichotomy on matrix units. Nothing here
  claims existence of completions (the (2,2) no-go stands), and nothing here yet
  eliminates the transpose branch: that is phase two's oriented reference, wired in
  round five.
-/
import OIBridge.AccessibleAlgebra
import Mathlib.Analysis.Matrix.Order
import Mathlib.Analysis.Matrix.PosDef

namespace OIBridge
namespace OperationalRigidity

open Complex Matrix CoherentLift AccessibleAlgebra
open scoped ComplexOrder

variable {Dm : ℕ}

/-! ### Section A — operational separation -/

/-- **Single-line Dedekind extraction**: an exponential combination over one line of
frequencies `E c − μ` vanishing at all times has every coefficient zero. -/
theorem line_coefficient_vanish (E : Fin Dm → ℝ) (hE : Function.Injective E) (μ : ℝ)
    (F : Fin Dm → ℂ)
    (hzero : ∀ s : ℝ, ∑ c, F c * Complex.exp (Complex.I * ((E c - μ : ℝ) : ℂ) * (s : ℂ)) = 0)
    (c : Fin Dm) : F c = 0 := by
  have hfib : ∀ s : ℝ, ∑ ω ∈ Finset.image (fun c' : Fin Dm => E c' - μ) Finset.univ,
      (∑ c' ∈ Finset.univ.filter (fun c' : Fin Dm => E c' - μ = ω), F c')
        * Complex.exp (Complex.I * (ω : ℂ) * (s : ℂ)) = 0 := by
    intro s
    rw [← hzero s]
    rw [← Finset.sum_fiberwise_of_maps_to (g := fun c' : Fin Dm => E c' - μ)
      (fun c' _ => Finset.mem_image_of_mem _ (Finset.mem_univ c'))]
    refine Finset.sum_congr rfl fun ω _ => ?_
    rw [Finset.sum_mul]
    refine Finset.sum_congr rfl fun c' hc' => ?_
    rw [(Finset.mem_filter.mp hc').2]
  have hval := BohrFrequency.coeffs_eq_zero hfib (E c - μ)
    (Finset.mem_image_of_mem _ (Finset.mem_univ c))
  have hsingle : Finset.univ.filter (fun c' : Fin Dm => E c' - μ = E c - μ) = {c} := by
    ext c'
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_singleton]
    constructor
    · intro h
      exact hE (by linarith)
    · intro h
      rw [h]
  rw [hsingle, Finset.sum_singleton] at hval
  exact hval

/-- The entry of a doubly diagonal sandwich against a fourth factor. -/
theorem diag_sandwich_apply (d e : Fin Dm → ℂ) (N Y : Matrix (Fin Dm) (Fin Dm) ℂ)
    (x y : Fin Dm) :
    (Matrix.diagonal d * N * Matrix.diagonal e * Y) x y
      = ∑ c, d x * N x c * e c * Y c y := by
  rw [Matrix.mul_apply]
  refine Finset.sum_congr rfl fun c _ => ?_
  rw [Matrix.mul_diagonal, Matrix.diagonal_mul]

/-- **The s-conjugated context entry, frequency-resolved**: sandwiching a one-slot
context times the operator between `V†…V` expands each entry as a line of gap
characters — the input to the second extraction. -/
theorem conj_context_entry {n : Type*} [Fintype n] (V : Matrix n (Fin Dm) ℂ)
    (hV' : Vᴴ * V = 1) (E : Fin Dm → ℝ) (B X : Matrix n n ℂ) (s : ℝ) (x y : Fin Dm) :
    (Vᴴ * (Matrix.of (BohrFrequency.Umat V E s) * B
        * (Matrix.of (BohrFrequency.Umat V E s))ᴴ * X) * V) x y
      = ∑ c, (Vᴴ * B * V) x c * (Vᴴ * X * V) c y
          * Complex.exp (Complex.I * ((E c - E x : ℝ) : ℂ) * (s : ℂ)) := by
  have hU := umat_spectral' V E s
  have hUH : (Matrix.of (BohrFrequency.Umat V E s))ᴴ
      = V * Matrix.diagonal (star fun a => Complex.exp (-(Complex.I * (E a : ℂ) * (s : ℂ))))
        * Vᴴ := by
    rw [hU, Matrix.conjTranspose_mul, Matrix.conjTranspose_mul,
      Matrix.conjTranspose_conjTranspose, Matrix.diagonal_conjTranspose]
    rw [← Matrix.mul_assoc]
  have hmid : Vᴴ * (Matrix.of (BohrFrequency.Umat V E s) * B
      * (Matrix.of (BohrFrequency.Umat V E s))ᴴ * X) * V
      = Matrix.diagonal (fun a => Complex.exp (-(Complex.I * (E a : ℂ) * (s : ℂ))))
        * (Vᴴ * B * V)
        * Matrix.diagonal (star fun a => Complex.exp (-(Complex.I * (E a : ℂ) * (s : ℂ))))
        * (Vᴴ * X * V) := by
    rw [hUH, hU]
    simp only [Matrix.mul_assoc]
    rw [← Matrix.mul_assoc Vᴴ V, hV', Matrix.one_mul]
  rw [hmid, diag_sandwich_apply]
  refine Finset.sum_congr rfl fun c _ => ?_
  rw [Pi.star_apply, BohrFrequency.star_phase]
  rw [show Complex.exp (Complex.I * ((E c - E x : ℝ) : ℂ) * (s : ℂ))
      = Complex.exp (-(Complex.I * (E x : ℂ) * (s : ℂ)))
        * Complex.exp (Complex.I * (E c : ℂ) * (s : ℂ)) from by
    rw [← Complex.exp_add]
    congr 1
    push_cast
    ring]
  ring

/-- **OPERATIONAL SEPARATION (C3b.1).** An operator invisible to the normalization
datum, every one-slot context, and every two-slot context is ZERO. The one-slot layer
kills the off-diagonal of `Y = V† X V` (round five's extraction); the two-slot layer
reduces, through the same extraction, to a line of gap characters in the second time,
whose coefficients kill the diagonal. Probe F18: one-slot data alone do NOT suffice —
the census carrier admits two distinct exact states with identical one-slot data —
so the two-slot hypothesis is load-bearing, not convenience. -/
theorem operational_separation {n ι' : Type*} [Fintype n] [DecidableEq n]
    (V : Matrix n (Fin Dm) ℂ) (E : Fin Dm → ℝ) (A : ι' → Matrix n n ℂ)
    (X : Matrix n n ℂ) (hV : V * Vᴴ = 1) (hV' : Vᴴ * V = 1)
    (hgap : ∀ a b c d : Fin Dm, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hcomplete : ∀ a b : Fin Dm, a ≠ b → ∃ j, (Vᴴ * A j * V) a b ≠ 0)
    (htr : Matrix.trace X = 0)
    (h1 : ∀ (j : ι') (t : ℝ),
      Matrix.trace (Matrix.of (BohrFrequency.Umat V E t) * A j
        * (Matrix.of (BohrFrequency.Umat V E t))ᴴ * X) = 0)
    (h2 : ∀ (j k : ι') (t s : ℝ),
      Matrix.trace (Matrix.of (BohrFrequency.Umat V E t) * A j
        * (Matrix.of (BohrFrequency.Umat V E t))ᴴ
        * (Matrix.of (BohrFrequency.Umat V E s) * A k
          * (Matrix.of (BohrFrequency.Umat V E s))ᴴ * X)) = 0) :
    X = 0 := by
  have hoff : ∀ a b : Fin Dm, a ≠ b → (Vᴴ * X * V) b a = 0 := by
    intro a b hab
    obtain ⟨j, hj⟩ := hcomplete a b hab
    have hzero : ∀ t : ℝ, ∑ q : Fin Dm × Fin Dm,
        (Vᴴ * A j * V) q.1 q.2 * (Vᴴ * X * V) q.2 q.1
          * Complex.exp (Complex.I * ((E q.2 - E q.1 : ℝ) : ℂ) * (t : ℂ)) = 0 := by
      intro t
      rw [← intervened_readout_expansion X (A j) V E t, Matrix.trace_mul_comm]
      exact h1 j t
    have hF := gap_coefficient_vanish E hgap
      (fun q : Fin Dm × Fin Dm => (Vᴴ * A j * V) q.1 q.2 * (Vᴴ * X * V) q.2 q.1) hzero hab
    exact (mul_eq_zero.mp hF).resolve_left hj
  have hdiag : ∀ a : Fin Dm, (Vᴴ * X * V) a a = 0 := by
    intro a
    by_cases hb : ∃ b : Fin Dm, b ≠ a
    · obtain ⟨b, hba⟩ := hb
      have hstep1 : ∀ (k : ι') (s : ℝ),
          (Vᴴ * (Matrix.of (BohrFrequency.Umat V E s) * A k
            * (Matrix.of (BohrFrequency.Umat V E s))ᴴ * X) * V) b a = 0 := by
        intro k s
        obtain ⟨j, hj⟩ := hcomplete a b (Ne.symm hba)
        have hzero : ∀ t : ℝ, ∑ q : Fin Dm × Fin Dm,
            (Vᴴ * A j * V) q.1 q.2
              * (Vᴴ * (Matrix.of (BohrFrequency.Umat V E s) * A k
                * (Matrix.of (BohrFrequency.Umat V E s))ᴴ * X) * V) q.2 q.1
              * Complex.exp (Complex.I * ((E q.2 - E q.1 : ℝ) : ℂ) * (t : ℂ)) = 0 := by
          intro t
          rw [← intervened_readout_expansion (Matrix.of (BohrFrequency.Umat V E s) * A k
            * (Matrix.of (BohrFrequency.Umat V E s))ᴴ * X) (A j) V E t,
            Matrix.trace_mul_comm]
          exact h2 j k t s
        have hF := gap_coefficient_vanish E hgap
          (fun q : Fin Dm × Fin Dm => (Vᴴ * A j * V) q.1 q.2
            * (Vᴴ * (Matrix.of (BohrFrequency.Umat V E s) * A k
              * (Matrix.of (BohrFrequency.Umat V E s))ᴴ * X) * V) q.2 q.1)
          hzero (Ne.symm hba)
        exact (mul_eq_zero.mp hF).resolve_left hj
      obtain ⟨k, hk⟩ := hcomplete b a hba
      have hE : Function.Injective E := by
        intro x y hxy
        by_contra hne
        exact hne (hgap x y y x hne (Ne.symm hne) (by rw [hxy])).1
      have hline : ∀ s : ℝ, ∑ c, (Vᴴ * A k * V) b c * (Vᴴ * X * V) c a
          * Complex.exp (Complex.I * ((E c - E b : ℝ) : ℂ) * (s : ℂ)) = 0 := by
        intro s
        rw [← conj_context_entry V hV' E (A k) X s b a]
        exact hstep1 k s
      have hcoef := line_coefficient_vanish E hE (E b)
        (fun c => (Vᴴ * A k * V) b c * (Vᴴ * X * V) c a) hline a
      exact (mul_eq_zero.mp hcoef).resolve_left hk
    · push Not at hb
      have htrY : Matrix.trace (Vᴴ * X * V) = 0 := by
        rw [Matrix.trace_mul_comm, ← Matrix.mul_assoc, hV, Matrix.one_mul, htr]
      rw [Matrix.trace, show (Finset.univ : Finset (Fin Dm)) = {a} from
        Finset.eq_singleton_iff_unique_mem.mpr ⟨Finset.mem_univ a, fun x _ => hb x⟩,
        Finset.sum_singleton] at htrY
      exact htrY
  have hY : Vᴴ * X * V = 0 := by
    ext p q
    rw [Matrix.zero_apply]
    by_cases hpq : p = q
    · subst hpq
      exact hdiag p
    · exact hoff q p (Ne.symm hpq)
  calc X = V * Vᴴ * X * (V * Vᴴ) := by rw [hV, Matrix.one_mul, Matrix.mul_one]
    _ = V * (Vᴴ * X * V) * Vᴴ := by simp only [Matrix.mul_assoc]
    _ = 0 := by rw [hY, Matrix.mul_zero, Matrix.zero_mul]

/-- **State-side rigidity**: two preparations carrying identical normalization,
one-slot, and two-slot branch data coincide. The completion's state is operationally
determined — no state-side gauge survives the two-slot data. -/
theorem sameData_unique_state {n ι' : Type*} [Fintype n] [DecidableEq n]
    (V : Matrix n (Fin Dm) ℂ) (E : Fin Dm → ℝ) (A : ι' → Matrix n n ℂ)
    (ρ σ : Matrix n n ℂ) (hV : V * Vᴴ = 1) (hV' : Vᴴ * V = 1)
    (hgap : ∀ a b c d : Fin Dm, a ≠ b → c ≠ d → E b - E a = E d - E c → a = c ∧ b = d)
    (hcomplete : ∀ a b : Fin Dm, a ≠ b → ∃ j, (Vᴴ * A j * V) a b ≠ 0)
    (htr : Matrix.trace ρ = Matrix.trace σ)
    (h1 : ∀ (j : ι') (t : ℝ),
      Matrix.trace (Matrix.of (BohrFrequency.Umat V E t) * A j
        * (Matrix.of (BohrFrequency.Umat V E t))ᴴ * ρ)
      = Matrix.trace (Matrix.of (BohrFrequency.Umat V E t) * A j
        * (Matrix.of (BohrFrequency.Umat V E t))ᴴ * σ))
    (h2 : ∀ (j k : ι') (t s : ℝ),
      Matrix.trace (Matrix.of (BohrFrequency.Umat V E t) * A j
        * (Matrix.of (BohrFrequency.Umat V E t))ᴴ
        * (Matrix.of (BohrFrequency.Umat V E s) * A k
          * (Matrix.of (BohrFrequency.Umat V E s))ᴴ * ρ))
      = Matrix.trace (Matrix.of (BohrFrequency.Umat V E t) * A j
        * (Matrix.of (BohrFrequency.Umat V E t))ᴴ
        * (Matrix.of (BohrFrequency.Umat V E s) * A k
          * (Matrix.of (BohrFrequency.Umat V E s))ᴴ * σ))) :
    ρ = σ := by
  have hsep := operational_separation V E A (ρ - σ) hV hV' hgap hcomplete
    (by rw [Matrix.trace_sub, htr, sub_self])
    (fun j t => by
      rw [Matrix.mul_sub, Matrix.trace_sub, h1 j t, sub_self])
    (fun j k t s => by
      rw [Matrix.mul_sub, Matrix.mul_sub, Matrix.trace_sub, h2 j k t s, sub_self])
  exact sub_eq_zero.mp hsep

/-! ### Section B — the data-defined map: well-definedness, existence, and the cone -/

variable {nn : Type*} [Fintype nn] [DecidableEq nn]

/-- **The well-definedness transfer (the audited step of C3b.1)**: identical pairing data
against a separating state family carries linear relations between the contexts of one
completion to the contexts of the other. "Same branch probabilities" defines the
correspondence unambiguously exactly BECAUSE the operational contexts separate. -/
theorem sameData_combination_transfer {ι κ : Type*}
    (G₁ G₂ : ι → Matrix nn nn ℂ) (σ₁ σ₂ : κ → Matrix nn nn ℂ)
    (hdata : ∀ i k, Matrix.trace (G₁ i * σ₁ k) = Matrix.trace (G₂ i * σ₂ k))
    (hsep : ∀ M : Matrix nn nn ℂ, (∀ k, Matrix.trace (M * σ₂ k) = 0) → M = 0)
    (s : Finset ι) (c : ι → ℂ)
    (hrel : ∑ i ∈ s, c i • G₁ i = 0) :
    ∑ i ∈ s, c i • G₂ i = 0 := by
  refine hsep _ fun k => ?_
  have h1 : Matrix.trace ((∑ i ∈ s, c i • G₁ i) * σ₁ k) = 0 := by
    rw [hrel, Matrix.zero_mul, Matrix.trace_zero]
  rw [Finset.sum_mul, Matrix.trace_sum] at h1
  rw [Finset.sum_mul, Matrix.trace_sum]
  rw [Finset.sum_congr rfl fun i _ => by
    rw [smul_mul_assoc, Matrix.trace_smul, ← hdata i k, ← Matrix.trace_smul,
      ← smul_mul_assoc]]
  exact h1

omit [Fintype nn] [DecidableEq nn] in
/-- **The data-defined map EXISTS**: spanning contexts on side one plus the transfer of
linear relations produce a ℂ-linear map carrying each context to its data-matched twin —
by factoring the linear-combination map through its kernel. No basis is chosen. -/
theorem sameData_linear_extension {ι : Type*} (G₁ G₂ : ι → Matrix nn nn ℂ)
    (hspan : Submodule.span ℂ (Set.range G₁) = ⊤)
    (htrans : ∀ l : ι →₀ ℂ, Finsupp.linearCombination ℂ G₁ l = 0 →
      Finsupp.linearCombination ℂ G₂ l = 0) :
    ∃ Φ : Matrix nn nn ℂ →ₗ[ℂ] Matrix nn nn ℂ, ∀ i, Φ (G₁ i) = G₂ i := by
  have hker : LinearMap.ker (Finsupp.linearCombination ℂ G₁)
      ≤ LinearMap.ker (Finsupp.linearCombination ℂ G₂) := fun l hl => htrans l hl
  have hsurj : Function.Surjective (Finsupp.linearCombination ℂ G₁) := by
    rw [← LinearMap.range_eq_top, Finsupp.range_linearCombination, hspan]
  refine ⟨(LinearMap.ker (Finsupp.linearCombination ℂ G₁)).liftQ
      (Finsupp.linearCombination ℂ G₂) hker ∘ₗ
    ((Finsupp.linearCombination ℂ G₁).quotKerEquivOfSurjective hsurj).symm.toLinearMap,
    fun i => ?_⟩
  have hGi : G₁ i = Finsupp.linearCombination ℂ G₁ (Finsupp.single i 1) := by
    rw [Finsupp.linearCombination_single, one_smul]
  rw [hGi, LinearMap.comp_apply]
  have hq : ((Finsupp.linearCombination ℂ G₁).quotKerEquivOfSurjective hsurj).symm
      (Finsupp.linearCombination ℂ G₁ (Finsupp.single i 1))
      = Submodule.Quotient.mk (Finsupp.single i 1) := by
    rw [← LinearMap.quotKerEquivOfSurjective_apply_mk
      (f := Finsupp.linearCombination ℂ G₁) hsurj]
    exact LinearEquiv.symm_apply_apply _ _
  have hfinal := congrArg
    (⇑((LinearMap.ker (Finsupp.linearCombination ℂ G₁)).liftQ
      (Finsupp.linearCombination ℂ G₂) hker)) hq
  have hT : Finsupp.linearCombination ℂ G₂ (Finsupp.single i 1) = G₂ i := by
    rw [Finsupp.linearCombination_single, one_smul]
  rw [Submodule.liftQ_apply, hT] at hfinal
  exact hfinal

/-! ### Section C — order isomorphism ⟹ Jordan (the kernel-internal Kadison theorem) -/

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- The rank-one dyad on the `i`-th column of `U`. -/
def edyad (U : Matrix n n ℂ) (i : n) : Matrix n n ℂ :=
  Matrix.of fun x y => U x i * star (U y i)

omit [Fintype n] [DecidableEq n] in
theorem edyad_apply (U : Matrix n n ℂ) (i x y : n) :
    edyad U i x y = U x i * star (U y i) := rfl

omit [Fintype n] [DecidableEq n] in
theorem edyad_isHermitian (U : Matrix n n ℂ) (i : n) : (edyad U i).IsHermitian := by
  ext x y
  rw [Matrix.conjTranspose_apply, edyad_apply, edyad_apply, star_mul', star_star]
  ring

omit [DecidableEq n] in
/-- Column dyads multiply through the Gram entry. -/
theorem edyad_mul_edyad (U : Matrix n n ℂ) (i j : n) :
    edyad U i * edyad U j
      = Matrix.of fun x y => (Uᴴ * U) i j * (U x i * star (U y j)) := by
  ext x y
  rw [Matrix.mul_apply, Matrix.of_apply, Matrix.mul_apply, Finset.sum_mul]
  refine Finset.sum_congr rfl fun r _ => ?_
  rw [edyad_apply, edyad_apply, Matrix.conjTranspose_apply]
  ring

/-- Orthonormal columns give idempotent dyads. -/
theorem edyad_idem (U : Matrix n n ℂ) (hU : Uᴴ * U = 1) (i : n) :
    edyad U i * edyad U i = edyad U i := by
  rw [edyad_mul_edyad, hU]
  ext x y
  rw [Matrix.of_apply, Matrix.one_apply_eq, one_mul, edyad_apply]

/-- Orthonormal columns give orthogonal dyads. -/
theorem edyad_orthogonal (U : Matrix n n ℂ) (hU : Uᴴ * U = 1) {i j : n} (hij : i ≠ j) :
    edyad U i * edyad U j = 0 := by
  rw [edyad_mul_edyad, hU]
  ext x y
  rw [Matrix.of_apply, Matrix.one_apply_ne hij, zero_mul, Matrix.zero_apply]

/-- The diagonal conjugation resolved into column dyads. -/
theorem conj_diagonal_eq_sum_edyad (U : Matrix n n ℂ) (d : n → ℂ) :
    U * Matrix.diagonal d * Uᴴ = ∑ i, d i • edyad U i := by
  ext x y
  rw [Matrix.sum_apply, Matrix.mul_apply]
  refine Finset.sum_congr rfl fun r _ => ?_
  rw [Matrix.mul_diagonal, Matrix.conjTranspose_apply, Matrix.smul_apply, edyad_apply,
    smul_eq_mul]
  ring

/-- Every matrix annihilating all vectors is zero. -/
theorem eq_zero_of_mulVec_zero {M : Matrix n n ℂ} (h : ∀ v : n → ℂ, M *ᵥ v = 0) :
    M = 0 := by
  ext i j
  have hj := congrFun (h (Pi.single j 1)) i
  rw [Matrix.mulVec, Pi.zero_apply] at hj
  rw [show M i ⬝ᵥ Pi.single j 1 = M i j from ?_] at hj
  · rw [hj, Matrix.zero_apply]
  · rw [dotProduct]
    rw [Finset.sum_eq_single j (fun b _ hb => by rw [Pi.single_eq_of_ne hb, mul_zero])
      (fun hj' => absurd (Finset.mem_univ j) hj')]
    rw [Pi.single_eq_same, mul_one]

omit [DecidableEq n] in
/-- **The interval kernel splitting**: a Hermitian perturbation squeezed between two
positive matrices annihilates the kernel of their midpoint. -/
theorem psd_pair_kernel {Q Z : Matrix n n ℂ}
    (hp : (Q + Z).PosSemidef) (hm : (Q - Z).PosSemidef) {v : n → ℂ}
    (hv : Q *ᵥ v = 0) : Z *ᵥ v = 0 := by
  have hpv : (Q + Z) *ᵥ v = Z *ᵥ v := by
    rw [Matrix.add_mulVec, hv, zero_add]
  have hmv : (Q - Z) *ᵥ v = -(Z *ᵥ v) := by
    rw [Matrix.sub_mulVec, hv, zero_sub]
  have h1 := hp.dotProduct_mulVec_nonneg v
  have h2 := hm.dotProduct_mulVec_nonneg v
  rw [hpv] at h1
  rw [hmv, dotProduct_neg] at h2
  have hquad : star v ⬝ᵥ ((Q + Z) *ᵥ v) = 0 := by
    rw [hpv]
    exact le_antisymm (neg_nonneg.mp h2) h1
  have hz := (hp.dotProduct_mulVec_zero_iff v).mp hquad
  rw [hpv] at hz
  exact hz

/-- Conjugation by a coisometry cancels. -/
theorem unitary_conj_cancel {U : Matrix n n ℂ} (hU1 : Uᴴ * U = 1) (M : Matrix n n ℂ) :
    Uᴴ * (U * M * Uᴴ) * U = M := by
  simp only [Matrix.mul_assoc]
  rw [← Matrix.mul_assoc Uᴴ U, hU1, Matrix.one_mul, Matrix.mul_one]

/-- A real-diagonal conjugate is Hermitian. -/
theorem real_conj_diag_hermitian (U : Matrix n n ℂ) (d : n → ℝ) :
    (U * Matrix.diagonal (fun i => ((d i : ℝ) : ℂ)) * Uᴴ).IsHermitian := by
  have hd : (star fun i => ((d i : ℝ) : ℂ)) = fun i => ((d i : ℝ) : ℂ) := by
    funext i
    simp [Pi.star_apply, Complex.conj_ofReal]
  show (U * Matrix.diagonal _ * Uᴴ)ᴴ = _
  rw [Matrix.conjTranspose_mul, Matrix.conjTranspose_mul, Matrix.conjTranspose_conjTranspose,
    Matrix.diagonal_conjTranspose, hd, ← Matrix.mul_assoc]

/-- A nonnegative-real-diagonal conjugate is positive semidefinite. -/
theorem conj_diag_psd (U : Matrix n n ℂ) (d : n → ℝ) (hd : ∀ i, 0 ≤ d i) :
    (U * Matrix.diagonal (fun i => ((d i : ℝ) : ℂ)) * Uᴴ).PosSemidef :=
  (Matrix.posSemidef_diagonal_iff.mpr fun i =>
    Complex.zero_le_real.mpr (hd i)).mul_mul_conjTranspose_same U

/-- Real-diagonal conjugates add through their diagonals. -/
theorem conj_diag_add (U : Matrix n n ℂ) (f g : n → ℝ) :
    U * Matrix.diagonal (fun i => ((f i : ℝ) : ℂ)) * Uᴴ
      + U * Matrix.diagonal (fun i => ((g i : ℝ) : ℂ)) * Uᴴ
      = U * Matrix.diagonal (fun i => ((f i + g i : ℝ) : ℂ)) * Uᴴ := by
  rw [← Matrix.add_mul, ← Matrix.mul_add, Matrix.diagonal_add]
  rw [show (fun i => ((f i : ℝ) : ℂ) + ((g i : ℝ) : ℂ))
      = fun i => ((f i + g i : ℝ) : ℂ) from by
    funext i
    norm_cast]

/-- Real-diagonal conjugates subtract through their diagonals. -/
theorem conj_diag_sub (U : Matrix n n ℂ) (f g : n → ℝ) :
    U * Matrix.diagonal (fun i => ((f i : ℝ) : ℂ)) * Uᴴ
      - U * Matrix.diagonal (fun i => ((g i : ℝ) : ℂ)) * Uᴴ
      = U * Matrix.diagonal (fun i => ((f i - g i : ℝ) : ℂ)) * Uᴴ := by
  rw [← Matrix.sub_mul, ← Matrix.mul_sub, Matrix.diagonal_sub]
  rw [show (fun i => ((f i : ℝ) : ℂ) - ((g i : ℝ) : ℂ))
      = fun i => ((f i - g i : ℝ) : ℂ) from by
    funext i
    norm_cast]

/-- The identity as a real-diagonal conjugate of a unitary. -/
theorem one_eq_conj_diag {U : Matrix n n ℂ} (hU2 : U * Uᴴ = 1) :
    (1 : Matrix n n ℂ) = U * Matrix.diagonal (fun _ : n => ((1 : ℝ) : ℂ)) * Uᴴ := by
  rw [show Matrix.diagonal (fun _ : n => ((1 : ℝ) : ℂ)) = 1 from by
    push_cast
    rw [Matrix.diagonal_one]]
  rw [Matrix.mul_one, hU2]

/-- Real-diagonal conjugates multiply through their diagonals. -/
theorem conj_diag_mul {U : Matrix n n ℂ} (hU1 : Uᴴ * U = 1) (f g : n → ℝ) :
    (U * Matrix.diagonal (fun i => ((f i : ℝ) : ℂ)) * Uᴴ)
      * (U * Matrix.diagonal (fun i => ((g i : ℝ) : ℂ)) * Uᴴ)
      = U * Matrix.diagonal (fun i => ((f i * g i : ℝ) : ℂ)) * Uᴴ := by
  have h : ∀ h₁ h₂ : n → ℂ, U * Matrix.diagonal h₁ * Uᴴ * (U * Matrix.diagonal h₂ * Uᴴ)
      = U * (Matrix.diagonal h₁ * Matrix.diagonal h₂) * Uᴴ := by
    intro h₁ h₂
    simp only [Matrix.mul_assoc]
    rw [← Matrix.mul_assoc Uᴴ U, hU1, Matrix.one_mul]
  rw [h, Matrix.diagonal_mul_diagonal]
  rw [show (fun i => ((f i : ℝ) : ℂ) * ((g i : ℝ) : ℂ)) = fun i => ((f i * g i : ℝ) : ℂ) from by
    funext i
    norm_cast]

/-- A vanishing real-diagonal conjugate of a coisometry has vanishing diagonal. -/
theorem conj_diag_eq_zero {U : Matrix n n ℂ} (hU1 : Uᴴ * U = 1) {d : n → ℝ}
    (h : U * Matrix.diagonal (fun i => ((d i : ℝ) : ℂ)) * Uᴴ = 0) : ∀ i, d i = 0 := by
  intro i
  have hD : Matrix.diagonal (fun i => ((d i : ℝ) : ℂ)) = 0 := by
    calc Matrix.diagonal (fun i => ((d i : ℝ) : ℂ))
        = Uᴴ * (U * Matrix.diagonal (fun i => ((d i : ℝ) : ℂ)) * Uᴴ) * U :=
          (unitary_conj_cancel hU1 _).symm
      _ = Uᴴ * 0 * U := by rw [h]
      _ = 0 := by rw [Matrix.mul_zero, Matrix.zero_mul]
  have he : Matrix.diagonal (fun i => ((d i : ℝ) : ℂ)) i i = (0 : Matrix n n ℂ) i i := by
    rw [hD]
  rw [Matrix.diagonal_apply_eq, Matrix.zero_apply] at he
  exact_mod_cast he

/-- **A projection is extreme in the operator interval**: no Hermitian perturbation of a
projection stays inside `[0, 1]` — the kernel/range splitting kills it. Note that no
spectral input is consumed: the argument is pure positivity. -/
theorem projection_extreme {P Z : Matrix n n ℂ} (hP2 : P * P = P)
    (hp1 : (P + Z).PosSemidef) (hp2 : ((1 : Matrix n n ℂ) - (P + Z)).PosSemidef)
    (hm1 : (P - Z).PosSemidef) (hm2 : ((1 : Matrix n n ℂ) - (P - Z)).PosSemidef) :
    Z = 0 := by
  have hker : ∀ v : n → ℂ, P *ᵥ v = 0 → Z *ᵥ v = 0 := fun v hv =>
    psd_pair_kernel hp1 hm1 hv
  have hran : ∀ v : n → ℂ, P *ᵥ v = v → Z *ᵥ v = 0 := by
    intro v hv
    have hv' : ((1 : Matrix n n ℂ) - P) *ᵥ v = 0 := by
      rw [Matrix.sub_mulVec, Matrix.one_mulVec, hv, sub_self]
    have hp1' : (((1 : Matrix n n ℂ) - P) + Z).PosSemidef := by
      rw [show ((1 : Matrix n n ℂ) - P) + Z = (1 : Matrix n n ℂ) - (P - Z) from by abel]
      exact hm2
    have hm1' : (((1 : Matrix n n ℂ) - P) - Z).PosSemidef := by
      rw [show ((1 : Matrix n n ℂ) - P) - Z = (1 : Matrix n n ℂ) - (P + Z) from by abel]
      exact hp2
    exact psd_pair_kernel hp1' hm1' hv'
  refine eq_zero_of_mulVec_zero fun v => ?_
  have h1 : Z *ᵥ (P *ᵥ v) = 0 := by
    refine hran _ ?_
    rw [Matrix.mulVec_mulVec, hP2]
  have h2 : Z *ᵥ (v - P *ᵥ v) = 0 := by
    refine hker _ ?_
    rw [Matrix.mulVec_sub, Matrix.mulVec_mulVec, hP2, sub_self]
  have hsplit : P *ᵥ v + (v - P *ᵥ v) = v := by abel
  rw [← hsplit, Matrix.mulVec_add, h1, h2, add_zero]

/-- The extremity argument on an opaque spectral form: a coisometric frame with a real
diagonal inside `[0, 1]` and no Hermitian perturbation is idempotent. -/
theorem extreme_projection_aux {U : Matrix n n ℂ} {lam : n → ℝ}
    (hU1 : Uᴴ * U = 1) (hU2 : U * Uᴴ = 1)
    (h0 : (U * Matrix.diagonal (fun i => ((lam i : ℝ) : ℂ)) * Uᴴ).PosSemidef)
    (h1 : ((1 : Matrix n n ℂ)
      - U * Matrix.diagonal (fun i => ((lam i : ℝ) : ℂ)) * Uᴴ).PosSemidef)
    (hext : ∀ Z : Matrix n n ℂ, Z.IsHermitian →
      (U * Matrix.diagonal (fun i => ((lam i : ℝ) : ℂ)) * Uᴴ + Z).PosSemidef →
      ((1 : Matrix n n ℂ)
        - (U * Matrix.diagonal (fun i => ((lam i : ℝ) : ℂ)) * Uᴴ + Z)).PosSemidef →
      (U * Matrix.diagonal (fun i => ((lam i : ℝ) : ℂ)) * Uᴴ - Z).PosSemidef →
      ((1 : Matrix n n ℂ)
        - (U * Matrix.diagonal (fun i => ((lam i : ℝ) : ℂ)) * Uᴴ - Z)).PosSemidef → Z = 0) :
    (U * Matrix.diagonal (fun i => ((lam i : ℝ) : ℂ)) * Uᴴ)
      * (U * Matrix.diagonal (fun i => ((lam i : ℝ) : ℂ)) * Uᴴ)
      = U * Matrix.diagonal (fun i => ((lam i : ℝ) : ℂ)) * Uᴴ := by
  have hUisUnit : IsUnit U := ⟨⟨U, Uᴴ, hU2, hU1⟩, rfl⟩
  have hdiag_bound : ∀ (M : Matrix n n ℂ) (d : n → ℝ),
      M = U * Matrix.diagonal (fun i => ((d i : ℝ) : ℂ)) * Uᴴ → M.PosSemidef →
      ∀ i, 0 ≤ d i := by
    intro M d hM hpsd i
    rw [hM] at hpsd
    have hD := (IsUnit.posSemidef_star_right_conjugate_iff hUisUnit).mp
      (by rwa [Matrix.star_eq_conjTranspose])
    have := Matrix.posSemidef_diagonal_iff.mp hD i
    exact Complex.zero_le_real.mp this
  have hlam0 : ∀ i, 0 ≤ lam i := hdiag_bound _ lam rfl h0
  have hlam1 : ∀ i, lam i ≤ 1 := by
    intro i
    have hc := h1
    rw [one_eq_conj_diag hU2, conj_diag_sub] at hc
    have := hdiag_bound _ (fun i => 1 - lam i) rfl hc i
    linarith
  have hZform := hext (U * Matrix.diagonal (fun i => ((lam i * (1 - lam i) : ℝ) : ℂ)) * Uᴴ)
    (real_conj_diag_hermitian _ _)
    (by
      rw [conj_diag_add]
      exact conj_diag_psd _ _ fun i => by nlinarith [hlam0 i, hlam1 i])
    (by
      rw [conj_diag_add, one_eq_conj_diag hU2, conj_diag_sub]
      exact conj_diag_psd _ _ fun i => by nlinarith [sq_nonneg (1 - lam i)])
    (by
      rw [conj_diag_sub]
      exact conj_diag_psd _ _ fun i => by nlinarith [sq_nonneg (lam i)])
    (by
      rw [conj_diag_sub, one_eq_conj_diag hU2, conj_diag_sub]
      exact conj_diag_psd _ _ fun i => by nlinarith [hlam0 i, hlam1 i])
  have hzd := conj_diag_eq_zero hU1 hZform
  rw [conj_diag_mul hU1]
  rw [show (fun i => ((lam i * lam i : ℝ) : ℂ)) = fun i => ((lam i : ℝ) : ℂ) from by
    funext i
    have := hzd i
    have hsq : lam i * lam i = lam i := by nlinarith
    rw [hsq]]

/-- **An extreme point of the operator interval is a projection**: a Hermitian element of
`[0, 1]` admitting no Hermitian perturbation has spectrum in `{0, 1}`, by the explicit
perturbation `λ(1−λ)` along its eigenframe. -/
theorem extreme_projection {P : Matrix n n ℂ} (hPh : P.IsHermitian)
    (h0 : P.PosSemidef) (h1 : ((1 : Matrix n n ℂ) - P).PosSemidef)
    (hext : ∀ Z : Matrix n n ℂ, Z.IsHermitian →
      (P + Z).PosSemidef → ((1 : Matrix n n ℂ) - (P + Z)).PosSemidef →
      (P - Z).PosSemidef → ((1 : Matrix n n ℂ) - (P - Z)).PosSemidef → Z = 0) :
    P * P = P := by
  have hU1 : (hPh.eigenvectorUnitary : Matrix n n ℂ)ᴴ * (hPh.eigenvectorUnitary : Matrix n n ℂ)
      = 1 := by
    rw [← Matrix.star_eq_conjTranspose]
    exact Unitary.star_mul_self_of_mem hPh.eigenvectorUnitary.prop
  have hU2 : (hPh.eigenvectorUnitary : Matrix n n ℂ) * (hPh.eigenvectorUnitary : Matrix n n ℂ)ᴴ
      = 1 := by
    rw [← Matrix.star_eq_conjTranspose]
    exact Unitary.mul_star_self_of_mem hPh.eigenvectorUnitary.prop
  have hspec : P = (hPh.eigenvectorUnitary : Matrix n n ℂ)
      * Matrix.diagonal (fun i => ((hPh.eigenvalues i : ℝ) : ℂ))
      * (hPh.eigenvectorUnitary : Matrix n n ℂ)ᴴ := by
    conv_lhs => rw [hPh.spectral_theorem]
    rw [Unitary.conjStarAlgAut_apply, Matrix.star_eq_conjTranspose]
    rfl
  obtain ⟨U, lam, hU1', hU2', hspec'⟩ :
      ∃ (U : Matrix n n ℂ) (lam : n → ℝ), Uᴴ * U = 1 ∧ U * Uᴴ = 1
        ∧ P = U * Matrix.diagonal (fun i => ((lam i : ℝ) : ℂ)) * Uᴴ :=
    ⟨_, _, hU1, hU2, hspec⟩
  rw [hspec'] at h0 h1 hext ⊢
  exact extreme_projection_aux hU1' hU2' h0 h1 hext

omit [DecidableEq n] in
/-- A Hermitian idempotent is positive. -/
theorem proj_psd {P : Matrix n n ℂ} (hPh : P.IsHermitian) (hP2 : P * P = P) :
    P.PosSemidef := by
  have hfac : P = Pᴴ * P := by rw [hPh, hP2]
  rw [hfac]
  exact Matrix.posSemidef_conjTranspose_mul_self P

/-- The complement of an idempotent is idempotent. -/
theorem compl_idem {P : Matrix n n ℂ} (hP2 : P * P = P) :
    ((1 : Matrix n n ℂ) - P) * ((1 : Matrix n n ℂ) - P) = (1 : Matrix n n ℂ) - P := by
  rw [Matrix.mul_sub, Matrix.mul_one, Matrix.sub_mul, Matrix.one_mul, hP2]
  abel

/-- **The order-isomorphism hypothesis package**: a unital ℝ-linear star-preserving
bijection of the matrix algebra, positive in BOTH directions. The two-sided positivity
is Kadison's `X ⪰ 0 ⟺ Φ(X) ⪰ 0`; probe F18's pinching countercontrol shows one-sided
positivity does not suffice for the Jordan conclusion. -/
structure OrderIsoHyp (Φ Ψ : Matrix n n ℂ → Matrix n n ℂ) : Prop where
  add : ∀ X Y, Φ (X + Y) = Φ X + Φ Y
  smul : ∀ (r : ℝ) (X : Matrix n n ℂ), Φ (r • X) = r • Φ X
  star : ∀ X, Φ Xᴴ = (Φ X)ᴴ
  one : Φ 1 = 1
  pos : ∀ X, X.PosSemidef → (Φ X).PosSemidef
  posInv : ∀ X, X.PosSemidef → (Ψ X).PosSemidef
  left : ∀ X, Ψ (Φ X) = X
  right : ∀ X, Φ (Ψ X) = X

namespace OrderIsoHyp

variable {Φ Ψ : Matrix n n ℂ → Matrix n n ℂ}

omit [Fintype n] in
theorem zero (h : OrderIsoHyp Φ Ψ) : Φ 0 = 0 := by
  have h0 := h.add 0 0
  rw [add_zero] at h0
  have h1 : Φ 0 + 0 = Φ 0 + Φ 0 := by
    rw [add_zero]
    exact h0
  exact (add_left_cancel h1).symm

omit [Fintype n] in
theorem neg (h : OrderIsoHyp Φ Ψ) (X : Matrix n n ℂ) : Φ (-X) = -Φ X := by
  have h2 := h.add X (-X)
  rw [add_neg_cancel, h.zero] at h2
  exact eq_neg_of_add_eq_zero_left (by rw [add_comm]; exact h2.symm)

omit [Fintype n] in
theorem sub (h : OrderIsoHyp Φ Ψ) (X Y : Matrix n n ℂ) : Φ (X - Y) = Φ X - Φ Y := by
  rw [sub_eq_add_neg, h.add, h.neg, ← sub_eq_add_neg]

omit [Fintype n] in
theorem sum (h : OrderIsoHyp Φ Ψ) {ι : Type*} (s : Finset ι) (f : ι → Matrix n n ℂ) :
    Φ (∑ i ∈ s, f i) = ∑ i ∈ s, Φ (f i) := by
  classical
  induction s using Finset.cons_induction with
  | empty => rw [Finset.sum_empty, Finset.sum_empty, h.zero]
  | cons a s ha ih => rw [Finset.sum_cons, Finset.sum_cons, h.add, ih]

omit [Fintype n] in
/-- The inverse side satisfies the same package. -/
theorem symm (h : OrderIsoHyp Φ Ψ) : OrderIsoHyp Ψ Φ where
  add X Y := by
    calc Ψ (X + Y) = Ψ (Φ (Ψ X) + Φ (Ψ Y)) := by rw [h.right, h.right]
      _ = Ψ (Φ (Ψ X + Ψ Y)) := by rw [h.add]
      _ = Ψ X + Ψ Y := h.left _
  smul r X := by
    calc Ψ (r • X) = Ψ (r • Φ (Ψ X)) := by rw [h.right]
      _ = Ψ (Φ (r • Ψ X)) := by rw [h.smul]
      _ = r • Ψ X := h.left _
  star X := by
    calc Ψ Xᴴ = Ψ ((Φ (Ψ X))ᴴ) := by rw [h.right]
      _ = Ψ (Φ ((Ψ X)ᴴ)) := by rw [h.star]
      _ = (Ψ X)ᴴ := h.left _
  one := by
    calc Ψ 1 = Ψ (Φ 1) := by rw [h.one]
      _ = 1 := h.left _
  pos X hX := h.posInv X hX
  posInv X hX := h.pos X hX
  left := h.right
  right := h.left

end OrderIsoHyp

/-- **Order isomorphisms transport projections** (extreme points of the operator
interval map to extreme points, and those are exactly the projections). -/
theorem orderIso_maps_projections {Φ Ψ : Matrix n n ℂ → Matrix n n ℂ}
    (h : OrderIsoHyp Φ Ψ) {P : Matrix n n ℂ}
    (hPh : P.IsHermitian) (hP2 : P * P = P) :
    (Φ P).IsHermitian ∧ Φ P * Φ P = Φ P := by
  have hΦh : (Φ P).IsHermitian := by
    show (Φ P)ᴴ = Φ P
    rw [← h.star, hPh]
  refine ⟨hΦh, ?_⟩
  have hsym := h.symm
  have hP0 : P.PosSemidef := proj_psd hPh hP2
  have hP1 : ((1 : Matrix n n ℂ) - P).PosSemidef :=
    proj_psd (Matrix.isHermitian_one.sub hPh) (compl_idem hP2)
  refine extreme_projection hΦh (h.pos P hP0) ?_ ?_
  · rw [← h.one, ← h.sub]
    exact h.pos _ hP1
  · intro Z _ hzp1 hzp2 hzm1 hzm2
    have hkey : Ψ Z = 0 := by
      have e1 : Ψ (Φ P + Z) = P + Ψ Z := by
        rw [hsym.add, h.left]
      have e2 : Ψ ((1 : Matrix n n ℂ) - (Φ P + Z)) = 1 - (P + Ψ Z) := by
        rw [hsym.sub, hsym.one, hsym.add, h.left]
      have e3 : Ψ (Φ P - Z) = P - Ψ Z := by
        rw [hsym.sub, h.left]
      have e4 : Ψ ((1 : Matrix n n ℂ) - (Φ P - Z)) = 1 - (P - Ψ Z) := by
        rw [hsym.sub, hsym.one, hsym.sub, h.left]
      refine projection_extreme hP2 ?_ ?_ ?_ ?_
      · rw [← e1]
        exact h.posInv _ hzp1
      · rw [← e2]
        exact h.posInv _ hzp2
      · rw [← e3]
        exact h.posInv _ hzm1
      · rw [← e4]
        exact h.posInv _ hzm2
    calc Z = Φ (Ψ Z) := (h.right Z).symm
      _ = Φ 0 := by rw [hkey]
      _ = 0 := h.zero

/-- **Order isomorphisms transport orthogonality** of projections: additivity plus the
projection transport force the anticommutator to vanish, and the projection algebra
turns that into a vanishing product. -/
theorem orderIso_orthogonal {Φ Ψ : Matrix n n ℂ → Matrix n n ℂ}
    (h : OrderIsoHyp Φ Ψ) {P Q : Matrix n n ℂ}
    (hPh : P.IsHermitian) (hQh : Q.IsHermitian)
    (hP2 : P * P = P) (hQ2 : Q * Q = Q)
    (hPQ : P * Q = 0) (hQP : Q * P = 0) :
    Φ P * Φ Q = 0 := by
  have hPQproj : (P + Q) * (P + Q) = P + Q := by
    rw [Matrix.add_mul, Matrix.mul_add, Matrix.mul_add, hP2, hQ2, hPQ, hQP]
    abel
  have himg := (orderIso_maps_projections h (hPh.add hQh) hPQproj).2
  rw [h.add] at himg
  have hp := (orderIso_maps_projections h hPh hP2).2
  have hq := (orderIso_maps_projections h hQh hQ2).2
  have hexp : Φ P * Φ Q + Φ Q * Φ P = 0 := by
    rw [Matrix.add_mul, Matrix.mul_add, Matrix.mul_add, hp, hq] at himg
    have h2 : Φ P * Φ Q + Φ Q * Φ P
        = (Φ P + Φ P * Φ Q + (Φ Q * Φ P + Φ Q)) - (Φ P + Φ Q) := by abel
    rw [h2, himg, sub_self]
  have hcomm : Φ P * Φ Q = Φ Q * Φ P := by
    have h3 : Φ P * (Φ P * Φ Q + Φ Q * Φ P) = Φ P * Φ Q + Φ P * Φ Q * Φ P := by
      rw [Matrix.mul_add, ← Matrix.mul_assoc, hp, ← Matrix.mul_assoc]
    have h4 : (Φ P * Φ Q + Φ Q * Φ P) * Φ P = Φ P * Φ Q * Φ P + Φ Q * Φ P := by
      rw [Matrix.add_mul, Matrix.mul_assoc (Φ Q) (Φ P) (Φ P), hp]
    have h5 : Φ P * Φ Q + Φ P * Φ Q * Φ P = 0 := by
      rw [← h3, hexp, Matrix.mul_zero]
    have h6 : Φ P * Φ Q * Φ P + Φ Q * Φ P = 0 := by
      rw [← h4, hexp, Matrix.zero_mul]
    have h7 : Φ P * Φ Q - Φ Q * Φ P
        = (Φ P * Φ Q + Φ P * Φ Q * Φ P) - (Φ P * Φ Q * Φ P + Φ Q * Φ P) := by abel
    rw [h5, h6, sub_zero] at h7
    exact sub_eq_zero.mp h7
  have h8 : (2 : ℂ) • (Φ P * Φ Q) = 0 := by
    rw [two_smul]
    calc Φ P * Φ Q + Φ P * Φ Q = Φ P * Φ Q + Φ Q * Φ P := by rw [hcomm]
      _ = 0 := hexp
  exact (smul_eq_zero.mp h8).resolve_left (by norm_num)

/-- **The square is preserved** (`Φ(A²) = Φ(A)²` on Hermitians): resolve `A` into its
rank-one eigenframe dyads; their images are pairwise-orthogonal projections, so both
squares recombine to the same eigenvalue-squared resolution. -/
theorem orderIso_square {Φ Ψ : Matrix n n ℂ → Matrix n n ℂ}
    (h : OrderIsoHyp Φ Ψ) {A : Matrix n n ℂ} (hAh : A.IsHermitian) :
    Φ (A * A) = Φ A * Φ A := by
  obtain ⟨U, lam, hU1, hspecA⟩ :
      ∃ (U : Matrix n n ℂ) (lam : n → ℝ), Uᴴ * U = 1
        ∧ A = ∑ i, lam i • edyad U i := by
    refine ⟨(hAh.eigenvectorUnitary : Matrix n n ℂ), hAh.eigenvalues, ?_, ?_⟩
    · rw [← Matrix.star_eq_conjTranspose]
      exact Unitary.star_mul_self_of_mem hAh.eigenvectorUnitary.prop
    · have hs : A = (hAh.eigenvectorUnitary : Matrix n n ℂ)
          * Matrix.diagonal (fun i => ((hAh.eigenvalues i : ℝ) : ℂ))
          * (hAh.eigenvectorUnitary : Matrix n n ℂ)ᴴ := by
        conv_lhs => rw [hAh.spectral_theorem]
        rw [Unitary.conjStarAlgAut_apply, Matrix.star_eq_conjTranspose]
        rfl
      conv_lhs => rw [hs]
      rw [conj_diagonal_eq_sum_edyad]
      refine Finset.sum_congr rfl fun i _ => ?_
      ext x y
      rw [Matrix.smul_apply, Matrix.smul_apply, smul_eq_mul]
      exact Complex.real_smul.symm
  have hproj : ∀ i, Φ (edyad U i) * Φ (edyad U i) = Φ (edyad U i) := fun i =>
    (orderIso_maps_projections h (edyad_isHermitian U i) (edyad_idem U hU1 i)).2
  have horth : ∀ i j, i ≠ j → Φ (edyad U i) * Φ (edyad U j) = 0 := fun i j hij =>
    orderIso_orthogonal h (edyad_isHermitian U i) (edyad_isHermitian U j)
      (edyad_idem U hU1 i) (edyad_idem U hU1 j)
      (edyad_orthogonal U hU1 hij) (edyad_orthogonal U hU1 (Ne.symm hij))
  have hA2 : A * A = ∑ i, (lam i * lam i) • edyad U i := by
    rw [hspecA, Finset.sum_mul]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [Finset.mul_sum]
    rw [Finset.sum_eq_single i (fun j _ hji => by
        rw [smul_mul_smul_comm, edyad_orthogonal U hU1 (Ne.symm hji), smul_zero])
      (fun hi => absurd (Finset.mem_univ i) hi)]
    rw [smul_mul_smul_comm, edyad_idem U hU1 i]
  have hΦA : Φ A = ∑ i, lam i • Φ (edyad U i) := by
    rw [hspecA, h.sum]
    exact Finset.sum_congr rfl fun i _ => h.smul _ _
  have hΦA2 : Φ A * Φ A = ∑ i, (lam i * lam i) • Φ (edyad U i) := by
    rw [hΦA, Finset.sum_mul]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [Finset.mul_sum]
    rw [Finset.sum_eq_single i (fun j _ hji => by
        rw [smul_mul_smul_comm, horth i j (Ne.symm hji), smul_zero])
      (fun hi => absurd (Finset.mem_univ i) hi)]
    rw [smul_mul_smul_comm, hproj i]
  rw [hA2, h.sum, hΦA2]
  exact Finset.sum_congr rfl fun i _ => h.smul _ _

/-- **THE KADISON THEOREM, kernel-internal (C3b.2).** A unital ℝ-linear star-preserving
bijection of `M_D(ℂ)` that is positive in both directions is a Jordan ∗-isomorphism on
Hermitians: `Φ(AB + BA) = Φ(A)Φ(B) + Φ(B)Φ(A)`. Polarization of `orderIso_square`. -/
theorem orderIso_jordan {Φ Ψ : Matrix n n ℂ → Matrix n n ℂ}
    (h : OrderIsoHyp Φ Ψ) {A B : Matrix n n ℂ}
    (hAh : A.IsHermitian) (hBh : B.IsHermitian) :
    Φ (A * B + B * A) = Φ A * Φ B + Φ B * Φ A := by
  have hAB := orderIso_square h (hAh.add hBh)
  have hA := orderIso_square h hAh
  have hB := orderIso_square h hBh
  have hexp : (A + B) * (A + B) = A * A + (A * B + B * A) + B * B := by
    noncomm_ring
  have hL : Φ ((A + B) * (A + B)) = Φ (A * A) + Φ (A * B + B * A) + Φ (B * B) := by
    rw [hexp, h.add, h.add]
  have hR : Φ (A + B) * Φ (A + B)
      = Φ A * Φ A + (Φ A * Φ B + Φ B * Φ A) + Φ B * Φ B := by
    rw [h.add]
    noncomm_ring
  have hkey : Φ (A * A) + Φ (A * B + B * A) + Φ (B * B)
      = Φ A * Φ A + (Φ A * Φ B + Φ B * Φ A) + Φ B * Φ B := by
    rw [← hL, hAB, hR]
  rw [hA, hB] at hkey
  have hkey2 := add_right_cancel hkey
  -- hkey2 : Φ A * Φ A + Φ (A*B + B*A) = Φ A * Φ A + (Φ A * Φ B + Φ B * Φ A)
  exact add_left_cancel hkey2

/-! ### Section D — the accessible state cone and the pairing positivity -/

/-- Products of nonnegative complex numbers are nonnegative (the `ComplexOrder` cone is
multiplicative). -/
theorem cx_mul_nonneg {z w : ℂ} (hz : 0 ≤ z) (hw : 0 ≤ w) : 0 ≤ z * w := by
  rw [Complex.nonneg_iff] at hz hw ⊢
  constructor
  · rw [Complex.mul_re, ← hz.2, ← hw.2, zero_mul, sub_zero]
    exact mul_nonneg hz.1 hw.1
  · rw [Complex.mul_im, ← hz.2, ← hw.2, mul_zero, zero_mul, add_zero]

/-- The spectral resolution of a Hermitian matrix into real-weighted column dyads of a
coisometric frame. -/
theorem hermitian_spectral_edyad {A : Matrix n n ℂ} (hAh : A.IsHermitian) :
    ∃ U : Matrix n n ℂ, Uᴴ * U = 1 ∧ A = ∑ i, hAh.eigenvalues i • edyad U i := by
  refine ⟨(hAh.eigenvectorUnitary : Matrix n n ℂ), ?_, ?_⟩
  · rw [← Matrix.star_eq_conjTranspose]
    exact Unitary.star_mul_self_of_mem hAh.eigenvectorUnitary.prop
  · have hs : A = (hAh.eigenvectorUnitary : Matrix n n ℂ)
        * Matrix.diagonal (fun i => ((hAh.eigenvalues i : ℝ) : ℂ))
        * (hAh.eigenvectorUnitary : Matrix n n ℂ)ᴴ := by
      conv_lhs => rw [hAh.spectral_theorem]
      rw [Unitary.conjStarAlgAut_apply, Matrix.star_eq_conjTranspose]
      rfl
    conv_lhs => rw [hs]
    rw [conj_diagonal_eq_sum_edyad]
    refine Finset.sum_congr rfl fun i _ => ?_
    ext x y
    rw [Matrix.smul_apply, Matrix.smul_apply, smul_eq_mul]
    exact Complex.real_smul.symm

omit [DecidableEq n] in
/-- The trace of a dyad against an operator is the quadratic form on the column. -/
theorem trace_edyad_mul (U : Matrix n n ℂ) (i : n) (B : Matrix n n ℂ) :
    Matrix.trace (edyad U i * B)
      = star (fun x => U x i) ⬝ᵥ (B *ᵥ fun x => U x i) := by
  rw [Matrix.trace]
  rw [Finset.sum_congr rfl fun x _ => by rw [Matrix.diag_apply, Matrix.mul_apply]]
  rw [Finset.sum_comm, dotProduct]
  refine Finset.sum_congr rfl fun y _ => ?_
  rw [Pi.star_apply, Matrix.mulVec, dotProduct, Finset.mul_sum]
  refine Finset.sum_congr rfl fun x _ => ?_
  rw [edyad_apply]
  ring

/-- **The pairing positivity**: the trace of a product of positives is nonnegative. -/
theorem psd_trace_mul_nonneg {A B : Matrix n n ℂ} (hA : A.PosSemidef) (hB : B.PosSemidef) :
    0 ≤ Matrix.trace (A * B) := by
  obtain ⟨U, hU1, hspecA⟩ := hermitian_spectral_edyad hA.1
  rw [hspecA, Finset.sum_mul, Matrix.trace_sum]
  refine Finset.sum_nonneg fun i _ => ?_
  rw [smul_mul_assoc, Matrix.trace_smul, trace_edyad_mul, Complex.real_smul]
  exact cx_mul_nonneg (Complex.zero_le_real.mpr (hA.eigenvalues_nonneg i))
    (hB.dotProduct_mulVec_nonneg _)

omit [DecidableEq n] in
/-- A selective word applied to a preparation: the exact state it produces. -/
theorem word_state (c : ℂ) (u wv : n → ℂ) (ρ : Matrix n n ℂ) :
    Matrix.of (fun p q => c * u p * star (wv q)) * ρ
        * (Matrix.of (fun p q => c * u p * star (wv q)))ᴴ
      = (c * star c * (star wv ⬝ᵥ (ρ *ᵥ wv))) • Matrix.of (fun p q => u p * star (u q)) := by
  ext x y
  rw [Matrix.mul_apply, Matrix.smul_apply, Matrix.of_apply, smul_eq_mul]
  calc ∑ q, (Matrix.of (fun p q => c * u p * star (wv q)) * ρ) x q
        * (Matrix.of (fun p q => c * u p * star (wv q)))ᴴ q y
      = ∑ q, ∑ p, (c * u x * star (wv p)) * ρ p q
          * (star c * star (u y) * wv q) := by
        refine Finset.sum_congr rfl fun q _ => ?_
        rw [Matrix.conjTranspose_apply, Matrix.of_apply, Matrix.mul_apply, Finset.sum_mul]
        refine Finset.sum_congr rfl fun p _ => ?_
        rw [Matrix.of_apply, star_mul', star_mul', star_star]
    _ = c * star c * (star wv ⬝ᵥ (ρ *ᵥ wv)) * (u x * star (u y)) := by
        rw [Finset.sum_comm, dotProduct, Finset.mul_sum, Finset.sum_mul]
        refine Finset.sum_congr rfl fun p _ => ?_
        rw [Pi.star_apply, Matrix.mulVec, dotProduct, Finset.mul_sum, Finset.mul_sum,
          Finset.sum_mul]
        refine Finset.sum_congr rfl fun q _ => ?_
        ring

/-- **THE ACCESSIBLE STATE CONE IS FULL**: every positive matrix is a finite sum of
selective-word images `M_i ρ M_i†` of ANY nonzero positive preparation. Combined with
the two-slot span (probe F18; the dual of `operational_separation`), every state is
operationally reachable, which is what makes positivity of the data-defined map an
operational property rather than an assumption — the C3b.3 assembly consumes exactly
this. -/
theorem accessible_cone_full {ρ : Matrix n n ℂ} (hρ : ρ.PosSemidef) (hne : ρ ≠ 0)
    (σ : Matrix n n ℂ) (hσ : σ.PosSemidef) :
    ∃ M : n → Matrix n n ℂ, σ = ∑ i, M i * ρ * (M i)ᴴ := by
  have hw : ∃ w : n → ℂ, star w ⬝ᵥ (ρ *ᵥ w) ≠ 0 := by
    by_contra hall
    push Not at hall
    refine hne (eq_zero_of_mulVec_zero fun v => ?_)
    exact (hρ.dotProduct_mulVec_zero_iff v).mp (hall v)
  obtain ⟨w, hwne⟩ := hw
  obtain ⟨r, hrpos, hrc⟩ : ∃ r : ℝ, 0 < r ∧ star w ⬝ᵥ (ρ *ᵥ w) = (r : ℂ) := by
    have hr0 := hρ.dotProduct_mulVec_nonneg w
    have hrc : star w ⬝ᵥ (ρ *ᵥ w) = (((star w ⬝ᵥ (ρ *ᵥ w)).re : ℝ) : ℂ) := by
      have him := (Complex.nonneg_iff.mp hr0).2
      apply Complex.ext
      · rw [Complex.ofReal_re]
      · rw [Complex.ofReal_im, him]
    have hrne : (star w ⬝ᵥ (ρ *ᵥ w)).re ≠ 0 := fun h0 => hwne (by rw [hrc, h0]; norm_num)
    exact ⟨_, lt_of_le_of_ne (Complex.nonneg_iff.mp hr0).1 (Ne.symm hrne), hrc⟩
  obtain ⟨U, hU1, hspec⟩ := hermitian_spectral_edyad hσ.1
  refine ⟨fun i => Matrix.of (fun p q =>
    ((Real.sqrt (hσ.1.eigenvalues i / r) : ℝ) : ℂ) * U p i * star (w q)), ?_⟩
  conv_lhs => rw [hspec]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [word_state]
  have hsc : ((Real.sqrt (hσ.1.eigenvalues i / r) : ℝ) : ℂ)
      * star ((Real.sqrt (hσ.1.eigenvalues i / r) : ℝ) : ℂ)
      * (star w ⬝ᵥ (ρ *ᵥ w))
      = ((hσ.1.eigenvalues i : ℝ) : ℂ) := by
    have hstar : star (((Real.sqrt (hσ.1.eigenvalues i / r)) : ℝ) : ℂ)
        = (((Real.sqrt (hσ.1.eigenvalues i / r)) : ℝ) : ℂ) :=
      Complex.conj_ofReal _
    rw [hstar, hrc, ← Complex.ofReal_mul, ← Complex.ofReal_mul,
      Real.mul_self_sqrt (div_nonneg (hσ.eigenvalues_nonneg i) hrpos.le),
      div_mul_cancel₀ _ hrpos.ne']
  rw [hsc]
  ext x y
  rw [Matrix.smul_apply, Matrix.smul_apply, smul_eq_mul]
  exact Complex.real_smul

#print axioms line_coefficient_vanish
#print axioms conj_context_entry
#print axioms operational_separation
#print axioms sameData_unique_state
#print axioms sameData_combination_transfer
#print axioms sameData_linear_extension
#print axioms psd_pair_kernel
#print axioms projection_extreme
#print axioms extreme_projection
#print axioms orderIso_maps_projections
#print axioms orderIso_orthogonal
#print axioms orderIso_square
#print axioms orderIso_jordan
#print axioms hermitian_spectral_edyad
#print axioms trace_edyad_mul
#print axioms psd_trace_mul_nonneg
#print axioms accessible_cone_full

end OperationalRigidity
end OIBridge
