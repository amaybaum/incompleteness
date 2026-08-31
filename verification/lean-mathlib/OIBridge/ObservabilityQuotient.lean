/-
  OIBridge/ObservabilityQuotient.lean — the finite-horizon quotient theorem and the
  residual classification: OI earns G1 on exactly the distinctions it can operationally
  resolve, and nothing stronger.

  PHASE THREE, ROUND FIFTEEN. Round fourteen proved that itinerary separation makes the
  classical branch domain span the diagonal algebra. The audit point hiding in
  "finiteness picks a uniform horizon": Main's physical equivalence is scoped to finite
  accessible horizons, and C4 asks only for a readback gap on an accessible window —
  none of C1–C4 asserts complete microstate recovery. So this round proves the graded
  version and, with it, the exact residual theory when separation fails.

  §A — THE FINITE-HORIZON QUOTIENT THEOREM. With `s ∼_K t ⟺ ∀ k < K,
  vis(φ^k s) = vis(φ^k t)` (`itiRelK`) and the K-horizon branch domain `BranchDomainK`
  (the round-fourteen domain graded by the number of evolution steps used):

      ┌────────────────────────────────────────────────────────────────────┐
      │  span(𝒟_K)  =  { f : S → ℝ  |  f constant on every ∼_K class }     │
      └────────────────────────────────────────────────────────────────────┘

  (`branchDomain_span_eq_itineraryInvariant`). Soundness is
  `branchDomainK_invariant`; saturation decomposes any ∼_K-invariant function over the
  class indicators (`classIndicator`), each of which IS a K-horizon itinerary indicator
  (`classIndicator_eq_itiIndicator`) and hence a K-step branch preparation
  (`classIndicator_mem_BDK`). At an accessible K with singleton classes this makes the
  round-fourteen result physically sharp; with non-singleton classes it gives the exact
  intermediate theory. The ungraded domain is the union of the graded ones
  (`classicalBranchDomain_iff_horizon`), horizons stabilize at `orderOf φ`
  (`itiRelInf_iff_orderOf`), and the full-domain span is exactly the asymptotic
  itinerary invariants (`classicalBranch_span_eq_invariant`).

  §B — THE RESIDUAL CLASSIFICATION.
  `domainGlue_classification_mod_itineraryFibres`: the domain glue holds IFF the
  coherent dynamics transports every itinerary-class indicator exactly as the
  permutation does — the glue pins `U_τ` on the observable quotient `S/∼` and nothing
  finer. `domainGlue_unitary` (the base preparation already forces unitarity) and
  `glue_column_support` (columns of a fibre land in the φ-image of that fibre: the
  surviving freedom is block-unitary freedom inside itinerary-degenerate fibres,
  transported by φ) make the residual structure explicit. In the separating case every
  fibre is a singleton and the classification collapses to the monomial theorem of
  rounds thirteen and fourteen; in the label-symmetric four-cycle the fibres are pairs
  and the classification recovers probe F25's phased pair rotation — the countercontrol
  is now an instance of the classification, not merely a counterexample.

      ┌────────────────────────────────────────────────────────────────────┐
      │  OI earns G1 on exactly the distinctions the cut operationally     │
      │  resolves: full QM on the shell follows precisely when the         │
      │  observer cut is informationally complete there, and the           │
      │  remaining freedom is classified — block unitaries inside          │
      │  unresolved fibres — when it is not.                               │
      └────────────────────────────────────────────────────────────────────┘

  WHAT THIS DOES NOT DECIDE: whether the actual SM/GR cut is informationally complete
  on the relevant shells (the corpus's C2/C3/C4 are persistence, capacity, and history
  sensitivity — not complete observability), and whether minimality of the physical
  representative removes forever-indistinguishable microstates as redundant gauge (the
  route the audit ranks most promising, with the caveat that passive-itinerary
  equivalence may cease to be an equivalence once interventions are allowed). Those are
  the next targets; intervention existence stays behind them.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.DomainGlue

namespace OIBridge
namespace ObservabilityQuotient

open Complex Matrix CoherentLift CycleFibreHull DynamicsGlue DomainGlue
open scoped ComplexOrder

local notation "conj'" => (starRingEnd ℂ)

variable {S I : Type*} [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I]

/-! ### Section A₀ — the objects -/

/-- Itinerary equivalence at horizon `K`: agreement of the visible record on the
accessible window. -/
def itiRelK (φ : Equiv.Perm S) (vis : S → I) (K : ℕ) (s t : S) : Prop :=
  ∀ k, k < K → vis ((φ ^ k) s) = vis ((φ ^ k) t)

/-- Asymptotic itinerary equivalence: agreement of the entire visible record. -/
def itiRelInf (φ : Equiv.Perm S) (vis : S → I) (s t : S) : Prop :=
  ∀ k : ℕ, vis ((φ ^ k) s) = vis ((φ ^ k) t)

/-- The `∼_K`-invariant functions: the observables of the horizon-`K` quotient. -/
def ItineraryInvariantK (φ : Equiv.Perm S) (vis : S → I) (K : ℕ) :
    Submodule ℝ (S → ℝ) where
  carrier := {f | ∀ s t, itiRelK φ vis K s t → f s = f t}
  add_mem' := fun hf hg s t hst => by
    rw [Pi.add_apply, Pi.add_apply, hf s t hst, hg s t hst]
  zero_mem' := fun _ _ _ => rfl
  smul_mem' := fun c f hf s t hst => by
    rw [Pi.smul_apply, Pi.smul_apply, hf s t hst]

/-- The asymptotic itinerary invariants. -/
def ItineraryInvariant (φ : Equiv.Perm S) (vis : S → I) : Submodule ℝ (S → ℝ) where
  carrier := {f | ∀ s t, itiRelInf φ vis s t → f s = f t}
  add_mem' := fun hf hg s t hst => by
    rw [Pi.add_apply, Pi.add_apply, hf s t hst, hg s t hst]
  zero_mem' := fun _ _ _ => rfl
  smul_mem' := fun c f hf s t hst => by
    rw [Pi.smul_apply, Pi.smul_apply, hf s t hst]

/-- **The K-horizon branch domain**: the round-fourteen classical branch domain graded
by the number of evolution steps consumed — the preparations available on an accessible
window of length `K`. -/
inductive BranchDomainK (φ : Equiv.Perm S) (vis : S → I) : ℕ → (S → ℝ) → Prop
  | shell : BranchDomainK φ vis 0 fun _ => 1
  | mono {K : ℕ} {w : S → ℝ} : BranchDomainK φ vis K w →
      BranchDomainK φ vis (K + 1) w
  | evolve {K : ℕ} {w : S → ℝ} : BranchDomainK φ vis K w →
      BranchDomainK φ vis (K + 1) fun s => w (φ s)
  | branch (i : I) {K : ℕ} {w : S → ℝ} : BranchDomainK φ vis (K + 1) w →
      BranchDomainK φ vis (K + 1) fun s => if vis s = i then w s else 0

open scoped Classical in
/-- The `∼_K`-class indicator of `s`. -/
noncomputable def classIndicator (φ : Equiv.Perm S) (vis : S → I) (K : ℕ) (s : S) :
    S → ℝ :=
  fun t => if itiRelK φ vis K t s then 1 else 0

/-! ### Section A — the finite-horizon quotient theorem -/

omit [Fintype S] [DecidableEq S] [Fintype I] in
/-- Soundness: a K-horizon branch preparation is a `∼_K`-invariant. -/
theorem branchDomainK_invariant {φ : Equiv.Perm S} {vis : S → I} {K : ℕ} {w : S → ℝ}
    (h : BranchDomainK φ vis K w) : w ∈ ItineraryInvariantK φ vis K := by
  induction h with
  | shell => exact fun _ _ _ => rfl
  | mono _ ih => exact fun s t hst => ih s t fun k hk => hst k (Nat.lt_succ_of_lt hk)
  | evolve _ ih =>
      intro s t hst
      refine ih (φ s) (φ t) fun k hk => ?_
      have h1 := hst (k + 1) (Nat.succ_lt_succ hk)
      rw [pow_succ, Equiv.Perm.mul_apply, Equiv.Perm.mul_apply] at h1
      exact h1
  | branch i _ ih =>
      intro s t hst
      have h0 := hst 0 (Nat.succ_pos _)
      rw [pow_zero] at h0
      show (if vis s = i then _ else 0) = if vis t = i then _ else 0
      rw [show vis s = vis t from h0]
      by_cases hc : vis t = i
      · rw [if_pos hc, if_pos hc, ih s t hst]
      · rw [if_neg hc, if_neg hc]

omit [Fintype S] [DecidableEq S] [Fintype I] in
/-- Every class indicator is the itinerary indicator of its representative's word. -/
theorem classIndicator_eq_itiIndicator (φ : Equiv.Perm S) (vis : S → I) (K : ℕ)
    (s : S) :
    classIndicator φ vis K s = itiIndicator φ vis K fun k => vis ((φ ^ k) s) := by
  classical
  funext t
  rw [classIndicator, itiIndicator]
  exact if_congr ⟨fun h k hk => h k hk, fun h k hk => h k hk⟩ rfl rfl

omit [Fintype S] [DecidableEq S] [Fintype I] in
/-- The graded membership: the K-horizon itinerary indicator is a K-step branch
preparation — the branch/evolve recursion consumes exactly one evolution per symbol. -/
theorem itiIndicator_mem_BDK (φ : Equiv.Perm S) (vis : S → I) (T : ℕ) (c : ℕ → I) :
    BranchDomainK φ vis T (itiIndicator φ vis T c) := by
  induction T generalizing c with
  | zero =>
      rw [show itiIndicator φ vis 0 c = fun _ => (1 : ℝ) from funext fun t =>
        if_pos fun k hk => absurd hk (Nat.not_lt_zero k)]
      exact BranchDomainK.shell
  | succ T ih =>
      have h0 := BranchDomainK.branch (φ := φ) (vis := vis) (c 0)
        (BranchDomainK.evolve (ih fun k => c (k + 1)))
      rw [show (fun s => if vis s = c 0
          then itiIndicator φ vis T (fun k => c (k + 1)) (φ s) else 0)
          = itiIndicator φ vis (T + 1) c from ?_] at h0
      · exact h0
      · funext s
        rw [itiIndicator, itiIndicator]
        by_cases h1 : vis s = c 0
        · rw [if_pos h1]
          by_cases h2 : ∀ k, k < T → vis ((φ ^ k) (φ s)) = c (k + 1)
          · rw [if_pos h2, if_pos ?_]
            intro k hk
            cases k with
            | zero =>
                rw [pow_zero]
                exact h1
            | succ k =>
                rw [pow_succ, Equiv.Perm.mul_apply]
                exact h2 k (Nat.lt_of_succ_lt_succ hk)
          · rw [if_neg h2, if_neg ?_]
            intro hall
            refine h2 fun k hk => ?_
            rw [← Equiv.Perm.mul_apply, ← pow_succ]
            exact hall (k + 1) (Nat.succ_lt_succ hk)
        · rw [if_neg h1, if_neg ?_]
          intro hall
          refine h1 ?_
          have h3 := hall 0 (Nat.succ_pos T)
          rw [pow_zero] at h3
          exact h3

omit [Fintype S] [DecidableEq S] [Fintype I] in
/-- The class indicators are K-step branch preparations. -/
theorem classIndicator_mem_BDK (φ : Equiv.Perm S) (vis : S → I) (K : ℕ) (s : S) :
    BranchDomainK φ vis K (classIndicator φ vis K s) := by
  rw [classIndicator_eq_itiIndicator]
  exact itiIndicator_mem_BDK φ vis K _

omit [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- Saturation: every `∼_K`-invariant function is a combination of class indicators. -/
theorem invariant_le_span_classIndicators (φ : Equiv.Perm S) (vis : S → I) (K : ℕ) :
    ItineraryInvariantK φ vis K
      ≤ Submodule.span ℝ (Set.range (classIndicator φ vis K)) := by
  intro f hf
  classical
  have hrefl : ∀ s, itiRelK φ vis K s s := fun _ _ _ => rfl
  have hsymm : ∀ {s t}, itiRelK φ vis K s t → itiRelK φ vis K t s :=
    fun h k hk => (h k hk).symm
  have htrans : ∀ {s t u}, itiRelK φ vis K s t → itiRelK φ vis K t u
      → itiRelK φ vis K s u := fun h1 h2 k hk => (h1 k hk).trans (h2 k hk)
  have hcls : ∀ {s t}, itiRelK φ vis K t s →
      (Finset.univ.filter fun u => itiRelK φ vis K u s)
        = Finset.univ.filter fun u => itiRelK φ vis K u t := by
    intro s t hts
    refine Finset.ext fun u => ?_
    simp only [Finset.mem_filter, Finset.mem_univ, true_and]
    exact ⟨fun h => htrans h (hsymm hts), fun h => htrans h hts⟩
  have hdecomp : f = ∑ s, (f s
      / ((Finset.univ.filter fun u => itiRelK φ vis K u s).card : ℝ))
      • classIndicator φ vis K s := by
    funext t
    rw [Finset.sum_apply]
    rw [Finset.sum_congr rfl fun s _ => show
        ((f s / ((Finset.univ.filter fun u => itiRelK φ vis K u s).card : ℝ))
          • classIndicator φ vis K s) t
        = if itiRelK φ vis K t s then
            f s / ((Finset.univ.filter fun u => itiRelK φ vis K u s).card : ℝ)
          else 0 from by
      rw [Pi.smul_apply, smul_eq_mul, classIndicator]
      by_cases hc : itiRelK φ vis K t s
      · rw [if_pos hc, if_pos hc, mul_one]
      · rw [if_neg hc, if_neg hc, mul_zero]]
    rw [← Finset.sum_filter]
    have hval : ∀ s ∈ Finset.univ.filter fun u => itiRelK φ vis K t u,
        f s / ((Finset.univ.filter fun u => itiRelK φ vis K u s).card : ℝ)
        = f t / ((Finset.univ.filter fun u => itiRelK φ vis K u t).card : ℝ) := by
      intro s hs
      rw [Finset.mem_filter] at hs
      rw [hf s t (hsymm hs.2), hcls (hsymm hs.2)]
    rw [Finset.sum_congr rfl hval, Finset.sum_const, nsmul_eq_mul]
    have hsame : (Finset.univ.filter fun u => itiRelK φ vis K t u)
        = Finset.univ.filter fun u => itiRelK φ vis K u t :=
      Finset.ext fun u => by
        simp only [Finset.mem_filter, Finset.mem_univ, true_and]
        exact ⟨fun h => hsymm h, fun h => hsymm h⟩
    rw [hsame]
    have hpos : 0 < ((Finset.univ.filter fun u => itiRelK φ vis K u t).card : ℝ) := by
      have : t ∈ Finset.univ.filter fun u => itiRelK φ vis K u t :=
        Finset.mem_filter.mpr ⟨Finset.mem_univ t, hrefl t⟩
      exact_mod_cast Finset.card_pos.mpr ⟨t, this⟩
    rw [mul_div_cancel₀ (f t) hpos.ne']
  rw [hdecomp]
  exact Submodule.sum_mem _ fun s _ => Submodule.smul_mem _ _
    (Submodule.subset_span ⟨s, rfl⟩)

omit [DecidableEq S] [Fintype I] in
/-- **THE FINITE-HORIZON QUOTIENT THEOREM.** The span of the K-horizon branch domain is
exactly the algebra of `∼_K`-invariant functions: the operationally preparable diagonal
directions are precisely the distinctions the visible record resolves on the accessible
window, and nothing finer. -/
theorem branchDomain_span_eq_itineraryInvariant (φ : Equiv.Perm S) (vis : S → I)
    (K : ℕ) :
    Submodule.span ℝ {w : S → ℝ | BranchDomainK φ vis K w}
      = ItineraryInvariantK φ vis K := by
  refine le_antisymm (Submodule.span_le.mpr fun w hw => branchDomainK_invariant hw) ?_
  refine le_trans (invariant_le_span_classIndicators φ vis K) (Submodule.span_mono ?_)
  rintro w ⟨s, rfl⟩
  exact classIndicator_mem_BDK φ vis K s

omit [Fintype S] [DecidableEq S] [Fintype I] in
/-- The ungraded domain is the union of the graded ones. -/
theorem classicalBranchDomain_iff_horizon (φ : Equiv.Perm S) (vis : S → I)
    (w : S → ℝ) :
    ClassicalBranchDomain φ vis w ↔ ∃ K, BranchDomainK φ vis K w := by
  constructor
  · intro h
    induction h with
    | shell => exact ⟨0, BranchDomainK.shell⟩
    | evolve _ ih =>
        obtain ⟨K, hK⟩ := ih
        exact ⟨K + 1, BranchDomainK.evolve hK⟩
    | branch i _ ih =>
        obtain ⟨K, hK⟩ := ih
        exact ⟨K + 1, BranchDomainK.branch i (BranchDomainK.mono hK)⟩
  · rintro ⟨K, hK⟩
    induction hK with
    | shell => exact ClassicalBranchDomain.shell
    | mono _ ih => exact ih
    | evolve _ ih => exact ClassicalBranchDomain.evolve ih
    | branch i _ ih => exact ClassicalBranchDomain.branch i ih

omit [DecidableEq S] [Fintype I] [DecidableEq I] in
/-- Horizons stabilize at the order of the dynamics: the asymptotic itinerary relation
is the `orderOf φ`-horizon relation. -/
theorem itiRelInf_iff_orderOf (φ : Equiv.Perm S) (vis : S → I) (s t : S) :
    itiRelInf φ vis s t ↔ itiRelK φ vis (orderOf φ) s t := by
  constructor
  · exact fun h k _ => h k
  · intro h k
    rw [show (φ ^ k : Equiv.Perm S) = φ ^ (k % orderOf φ) from
      (pow_mod_orderOf φ k).symm]
    exact h _ (Nat.mod_lt k (orderOf_pos φ))

omit [DecidableEq S] [Fintype I] in
/-- **THE FULL-DOMAIN QUOTIENT THEOREM.** The span of the whole classical branch domain
is exactly the algebra of asymptotic itinerary invariants. -/
theorem classicalBranch_span_eq_invariant (φ : Equiv.Perm S) (vis : S → I) :
    Submodule.span ℝ {w : S → ℝ | ClassicalBranchDomain φ vis w}
      = ItineraryInvariant φ vis := by
  refine le_antisymm (Submodule.span_le.mpr fun w hw => ?_) ?_
  · obtain ⟨K, hK⟩ := (classicalBranchDomain_iff_horizon φ vis w).mp hw
    exact fun s t hst => branchDomainK_invariant hK s t fun k _ => hst k
  · intro f hf
    have h1 : f ∈ ItineraryInvariantK φ vis (orderOf φ) := fun s t hst =>
      hf s t ((itiRelInf_iff_orderOf φ vis s t).mpr hst)
    have h2 := (branchDomain_span_eq_itineraryInvariant φ vis (orderOf φ)).symm ▸ h1
    refine Submodule.span_mono ?_ h2
    intro w hw
    exact (classicalBranchDomain_iff_horizon φ vis w).mpr ⟨orderOf φ, hw⟩

/-! ### Section B — the residual classification -/

omit [Fintype I] [DecidableEq I] in
/-- The glue equation extends linearly from a set to its span — the round-fourteen span
induction, extracted at a general target. -/
theorem glueEq_span (U : Matrix S S ℂ) (φ : Equiv.Perm S) (D : Set (S → ℝ))
    (hglue : CompatibilityDomainGlue U φ D) (w : S → ℝ)
    (hw : w ∈ Submodule.span ℝ D) :
    U * Matrix.diagonal (fun s => ((w s : ℝ) : ℂ)) * Uᴴ
      = permMatrix φ * Matrix.diagonal (fun s => ((w s : ℝ) : ℂ)) * (permMatrix φ)ᴴ := by
  induction hw using Submodule.span_induction with
  | mem x hx => exact hglue x hx
  | zero =>
      rw [show (Matrix.diagonal fun s => (((0 : S → ℝ) s : ℝ) : ℂ)) = 0 from by
        rw [show (fun s => (((0 : S → ℝ) s : ℝ) : ℂ)) = fun _ => (0 : ℂ) from
          funext fun s => by rw [Pi.zero_apply, Complex.ofReal_zero]]
        exact Matrix.diagonal_zero]
      rw [Matrix.mul_zero, Matrix.zero_mul, Matrix.mul_zero, Matrix.zero_mul]
  | add x y _ _ hx hy =>
      rw [show (Matrix.diagonal fun s => (((x + y) s : ℝ) : ℂ))
          = Matrix.diagonal (fun s => ((x s : ℝ) : ℂ))
            + Matrix.diagonal (fun s => ((y s : ℝ) : ℂ)) from by
        ext a b
        rw [Matrix.add_apply, Matrix.diagonal_apply, Matrix.diagonal_apply,
          Matrix.diagonal_apply]
        by_cases hab : a = b
        · rw [if_pos hab, if_pos hab, if_pos hab, Pi.add_apply, Complex.ofReal_add]
        · rw [if_neg hab, if_neg hab, if_neg hab, add_zero]]
      rw [Matrix.mul_add, Matrix.add_mul, Matrix.mul_add, Matrix.add_mul, hx, hy]
  | smul c x _ hx =>
      rw [show (Matrix.diagonal fun s => (((c • x) s : ℝ) : ℂ))
          = (c : ℂ) • Matrix.diagonal (fun s => ((x s : ℝ) : ℂ)) from by
        ext a b
        rw [Matrix.smul_apply, Matrix.diagonal_apply, Matrix.diagonal_apply]
        by_cases hab : a = b
        · rw [if_pos hab, if_pos hab, Pi.smul_apply, smul_eq_mul, Complex.ofReal_mul,
            smul_eq_mul]
        · rw [if_neg hab, if_neg hab, smul_zero]]
      rw [Matrix.mul_smul, Matrix.smul_mul, Matrix.mul_smul, Matrix.smul_mul, hx]

omit [Fintype I] in
/-- **`domainGlue_classification_mod_itineraryFibres`.** The domain glue holds if and
only if the coherent dynamics transports every asymptotic itinerary-class indicator
exactly as the permutation does: the glue pins `U_τ` on the observable quotient and
nothing finer. In the separating case the classes are singletons and this collapses to
the monomial theorem; on itinerary-degenerate fibres the surviving freedom is exactly
the block transport the four-cycle countercontrol instantiates. -/
theorem domainGlue_classification_mod_itineraryFibres (U : Matrix S S ℂ)
    (φ : Equiv.Perm S) (vis : S → I) :
    CompatibilityDomainGlue U φ {w | ClassicalBranchDomain φ vis w}
      ↔ ∀ s : S,
        U * Matrix.diagonal
            (fun t => (((classIndicator φ vis (orderOf φ) s) t : ℝ) : ℂ)) * Uᴴ
        = permMatrix φ * Matrix.diagonal
            (fun t => (((classIndicator φ vis (orderOf φ) s) t : ℝ) : ℂ))
          * (permMatrix φ)ᴴ := by
  constructor
  · intro hglue s
    refine hglue _ ?_
    show ClassicalBranchDomain φ vis (classIndicator φ vis (orderOf φ) s)
    exact (classicalBranchDomain_iff_horizon φ vis _).mpr
      ⟨orderOf φ, classIndicator_mem_BDK φ vis (orderOf φ) s⟩
  · intro hcls w hw
    refine glueEq_span U φ (Set.range (classIndicator φ vis (orderOf φ)))
      (fun v hv => ?_) w ?_
    · obtain ⟨s, rfl⟩ := hv
      exact hcls s
    · have h1 : w ∈ ItineraryInvariantK φ vis (orderOf φ) := by
        obtain ⟨K, hK⟩ := (classicalBranchDomain_iff_horizon φ vis w).mp hw
        intro s t hst
        exact branchDomainK_invariant hK s t fun k hk =>
          (itiRelInf_iff_orderOf φ vis s t).mpr hst k
      exact invariant_le_span_classIndicators φ vis (orderOf φ) h1

omit [Fintype I] in
/-- The base preparation already forces unitarity: the glue at the shell ensemble is
`U U† = 1`. -/
theorem domainGlue_unitary (U : Matrix S S ℂ) (φ : Equiv.Perm S) (vis : S → I)
    (hglue : CompatibilityDomainGlue U φ {w | ClassicalBranchDomain φ vis w}) :
    U * Uᴴ = 1 := by
  have h1 := hglue (fun _ => 1) ClassicalBranchDomain.shell
  rw [show (Matrix.diagonal fun _ : S => (((1 : ℝ)) : ℂ)) = 1 from by
    rw [show (fun _ : S => (((1 : ℝ)) : ℂ)) = fun _ => (1 : ℂ) from
      funext fun _ => Complex.ofReal_one]
    exact Matrix.diagonal_one] at h1
  rw [Matrix.mul_one, Matrix.mul_one] at h1
  rw [h1, permMatrix_unitary]

omit [Fintype I] in
/-- **THE RESIDUAL BLOCK STRUCTURE.** Under the domain glue, every column of an
itinerary fibre lands in the φ-image of that fibre: the surviving freedom is
block-unitary freedom inside observational-equivalence fibres, transported by φ. -/
theorem glue_column_support (U : Matrix S S ℂ) (φ : Equiv.Perm S) (vis : S → I)
    (hglue : CompatibilityDomainGlue U φ {w | ClassicalBranchDomain φ vis w})
    (s x : S) (hx : ∀ t, itiRelInf φ vis t s → φ t ≠ x) : U x s = 0 := by
  classical
  have hcls := (domainGlue_classification_mod_itineraryFibres U φ vis).mp hglue s
  have hxx := congrFun (congrFun hcls x) x
  rw [conj_diag_entry, permMatrix_conj_diagonal, Matrix.diagonal_apply_eq] at hxx
  have hrhs : (((classIndicator φ vis (orderOf φ) s) (φ.symm x) : ℝ) : ℂ) = 0 := by
    rw [classIndicator]
    rw [if_neg fun hrel => hx (φ.symm x)
      ((itiRelInf_iff_orderOf φ vis (φ.symm x) s).mpr hrel)
      (φ.apply_symm_apply x)]
    exact Complex.ofReal_zero
  rw [hrhs] at hxx
  have hterm : ∀ t ∈ Finset.univ,
      0 ≤ U x t * (((classIndicator φ vis (orderOf φ) s) t : ℝ) : ℂ)
        * conj' (U x t) := by
    intro t _
    rw [classIndicator]
    by_cases hc : itiRelK φ vis (orderOf φ) t s
    · rw [if_pos hc, Complex.ofReal_one, mul_one, Complex.mul_conj]
      exact Complex.zero_le_real.mpr (Complex.normSq_nonneg _)
    · rw [if_neg hc, Complex.ofReal_zero, mul_zero, zero_mul]
  have hzero := (Finset.sum_eq_zero_iff_of_nonneg hterm).mp hxx
  have hs := hzero s (Finset.mem_univ s)
  rw [classIndicator,
    if_pos (show itiRelK φ vis (orderOf φ) s s from fun _ _ => rfl),
    Complex.ofReal_one, mul_one] at hs
  have hns : Complex.normSq (U x s) = 0 := by
    have h2 : ((Complex.normSq (U x s) : ℝ) : ℂ) = 0 := by
      rw [← Complex.mul_conj]
      exact hs
    exact_mod_cast h2
  exact Complex.normSq_eq_zero.mp hns

#print axioms branchDomainK_invariant
#print axioms classIndicator_eq_itiIndicator
#print axioms itiIndicator_mem_BDK
#print axioms classIndicator_mem_BDK
#print axioms invariant_le_span_classIndicators
#print axioms branchDomain_span_eq_itineraryInvariant
#print axioms classicalBranchDomain_iff_horizon
#print axioms itiRelInf_iff_orderOf
#print axioms classicalBranch_span_eq_invariant
#print axioms glueEq_span
#print axioms domainGlue_classification_mod_itineraryFibres
#print axioms domainGlue_unitary
#print axioms glue_column_support

end ObservabilityQuotient
end OIBridge
