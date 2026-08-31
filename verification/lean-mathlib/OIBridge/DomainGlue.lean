/-
  OIBridge/DomainGlue.lean — the domain-relative glue: G_𝒟 on the classical branch
  domain, and the itinerary-separation theorem that earns G1 instead of postulating it.

  PHASE THREE, ROUND FOURTEEN. Round thirteen separated G0 (observable agreement) from
  G1 (diagonal-sector intertwining) and showed G1 ⟺ monomial sampled dynamics. The
  owner's call: bare OI licenses G0, and full G1 quantifies over arbitrary ontic diagonal
  weights that need not be operationally preparable — the honest middle ground is
  DOMAIN-RELATIVE glue:

    G_𝒟 (`CompatibilityDomainGlue`): the coherent lift intertwines the state dynamics on
    the compatibility domain 𝒟 of classical preparations it actually represents —
    `U_τ ℛ(μ) U_τ† = ℛ(φ_* μ)` for `μ ∈ 𝒟` — with the hierarchy G0 < G_𝒟 ≤ G1.

  The round's question is then not definitional but structural: is the ACTUAL domain
  rich enough to force G1?

  §A — THE LINEARITY BRIDGE. `spanning_domain_glue_implies_G1`:

      span_ℝ 𝒟 = ℝ^S   ⟹   (G_𝒟 ⟹ G1),

  immediate from linearity of `w ↦ U diag(w) U† − P diag(w) P†`. Everything then
  reduces to the span of the domain.

  §B — THE ACTUAL DOMAIN AND ITS SPAN. `ClassicalBranchDomain` is not invented for this
  round: it is the closure of the shell ensemble under the two operations the corpus's
  own classical branch functional already uses — reversible evolution and visible
  branch selection (the `class_fold` of the overlap identity, kernel
  `qfold_diagonal` / `intersection_consistent`). Its span is governed by a named
  physical property of the observer cut:

    `ItinerarySeparating`: distinct microstates have distinct visible itineraries —
    `(vis(φ^k s))_k = (vis(φ^k t))_k ⟹ s = t`, the classical observability of the
    partition.

  `itiIndicator_mem`: every finite-itinerary indicator lies in the domain (condition on
  the current visible value, evolve, repeat). `separating_singleton_mem`: under
  itinerary separation the domain contains every SINGLETON indicator (finiteness picks
  a uniform separation horizon), so `separating_domain_span_top`: the domain spans the
  whole diagonal algebra. Hence:

      ┌────────────────────────────────────────────────────────────────────┐
      │  ItinerarySeparating  ⟹  (G_𝒟 ⟹ G1):  the glue on the actual      │
      │  classical branch domain already forces monomial sampled dynamics  │
      │  (`classicalBranch_glue_forces_G1`, `…_forces_monomial`) —         │
      │  G1 is EARNED from the corpus's own preparations, not chosen.      │
      └────────────────────────────────────────────────────────────────────┘

  and the capstone `ergodicShell_SRC_of_domainGlue` chains through round thirteen:

      OI compatibility (G_𝒟 on the classical branch domain)
        + itinerary separation + ergodic shell
        ⟹  physical-flow SRC with canonical B, existence and uniqueness.

  THE LOAD-BEARING HYPOTHESIS IS EXPLICIT. Without itinerary separation the domain
  spans a proper subspace and non-monomial G_𝒟 solutions exist (probe F25 exhibits a
  label-symmetric cycle where EVERY unitary satisfies the constant-sector glue): the
  separation property, not a definition of "coherent completion", is what decides
  between outcome one (G1 derived) and F22's genuine underdetermination. Probe F25
  computes the span of the actual F22 shell domain exactly — the fibre-interleaved
  cycle IS itinerary-separating, and the branch-evolve closure reaches every singleton.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.DynamicsGlue

namespace OIBridge
namespace DomainGlue

open Complex Matrix CoherentLift CycleFibreHull DynamicsGlue
open scoped ComplexOrder

local notation "conj'" => (starRingEnd ℂ)

variable {S I : Type*} [Fintype S] [DecidableEq S] [Fintype I] [DecidableEq I]

/-! ### Section A — the domain-relative glue and the linearity bridge -/

/-- **G_𝒟, the domain-relative dynamics glue**: the coherent lift intertwines the state
dynamics on the given domain of classical preparations — no claim about ontic diagonal
weights outside it. `DiagonalSectorGlue` is the special case `𝒟 = ℝ^S`. -/
def CompatibilityDomainGlue (U : Matrix S S ℂ) (φ : Equiv.Perm S)
    (D : Set (S → ℝ)) : Prop :=
  ∀ w ∈ D, U * Matrix.diagonal (fun s => ((w s : ℝ) : ℂ)) * Uᴴ
    = permMatrix φ * Matrix.diagonal (fun s => ((w s : ℝ) : ℂ)) * (permMatrix φ)ᴴ

omit [Fintype I] [DecidableEq I] in
/-- **THE LINEARITY BRIDGE.** If the domain spans the whole diagonal algebra, the
domain-relative glue already implies the full diagonal-sector glue: the defect
`w ↦ U diag(w) U† − P diag(w) P†` is ℝ-linear and vanishes on a spanning set. -/
theorem spanning_domain_glue_implies_G1 (U : Matrix S S ℂ) (φ : Equiv.Perm S)
    (D : Set (S → ℝ)) (hspan : Submodule.span ℝ D = ⊤)
    (hglue : CompatibilityDomainGlue U φ D) : DiagonalSectorGlue U φ := by
  intro w
  have hw : w ∈ Submodule.span ℝ D := by rw [hspan]; trivial
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

/-! ### Section B — the actual domain: classical branch preparations -/

/-- **THE CLASSICAL BRANCH DOMAIN** — not invented for this round: the closure of the
shell ensemble under the two operations the corpus's classical branch functional already
uses, reversible evolution (pullback along `φ`; the inverse step is `φ^(L−1)`) and
visible branch selection. These are exactly the preparations of the overlap identity's
classical trajectory fold. Weights are unnormalized; normalization is a scalar and
irrelevant to the span. -/
inductive ClassicalBranchDomain (φ : Equiv.Perm S) (vis : S → I) : (S → ℝ) → Prop
  | shell : ClassicalBranchDomain φ vis fun _ => 1
  | evolve {w : S → ℝ} : ClassicalBranchDomain φ vis w →
      ClassicalBranchDomain φ vis fun s => w (φ s)
  | branch (i : I) {w : S → ℝ} : ClassicalBranchDomain φ vis w →
      ClassicalBranchDomain φ vis fun s => if vis s = i then w s else 0

/-- **THE OBSERVABILITY OF THE CUT**: distinct microstates have distinct visible
itineraries. A named physical property of the observer partition — the classical
sufficient condition under which the branch domain saturates the diagonal algebra. -/
def ItinerarySeparating (φ : Equiv.Perm S) (vis : S → I) : Prop :=
  ∀ s t : S, (∀ k : ℕ, vis ((φ ^ k) s) = vis ((φ ^ k) t)) → s = t

open scoped Classical in
/-- The indicator of a finite visible itinerary. -/
noncomputable def itiIndicator (φ : Equiv.Perm S) (vis : S → I) (T : ℕ) (c : ℕ → I) :
    S → ℝ :=
  fun t => if ∀ k, k < T → vis ((φ ^ k) t) = c k then 1 else 0

omit [Fintype S] [DecidableEq S] [Fintype I] in
/-- Every finite-itinerary indicator is a classical branch preparation: condition on the
current visible value, evolve, repeat. -/
theorem itiIndicator_mem (φ : Equiv.Perm S) (vis : S → I) (T : ℕ) (c : ℕ → I) :
    ClassicalBranchDomain φ vis (itiIndicator φ vis T c) := by
  induction T generalizing c with
  | zero =>
      rw [show itiIndicator φ vis 0 c = fun _ => (1 : ℝ) from funext fun t =>
        if_pos fun k hk => absurd hk (Nat.not_lt_zero k)]
      exact ClassicalBranchDomain.shell
  | succ T ih =>
      have h0 := ClassicalBranchDomain.branch (φ := φ) (vis := vis) (c 0)
        (ClassicalBranchDomain.evolve (ih fun k => c (k + 1)))
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

omit [Fintype I] in
/-- **SEPARATION PUTS EVERY SINGLETON IN THE DOMAIN**: finiteness picks a uniform
separation horizon, and the itinerary indicator at that horizon is the singleton. -/
theorem separating_singleton_mem (φ : Equiv.Perm S) (vis : S → I)
    (hsep : ItinerarySeparating φ vis) (s : S) :
    ClassicalBranchDomain φ vis fun t => if t = s then (1 : ℝ) else 0 := by
  have hex : ∀ t : S, t ≠ s → ∃ k : ℕ, vis ((φ ^ k) t) ≠ vis ((φ ^ k) s) := by
    intro t ht
    by_contra hall
    push Not at hall
    exact ht (hsep t s hall)
  classical
  have hK : ∀ t : S, ∃ k : ℕ, t ≠ s → vis ((φ ^ k) t) ≠ vis ((φ ^ k) s) := by
    intro t
    by_cases ht : t = s
    · exact ⟨0, fun h => absurd ht h⟩
    · obtain ⟨k, hk⟩ := hex t ht
      exact ⟨k, fun _ => hk⟩
  choose K hKs using hK
  have hlt : ∀ t, K t < Finset.univ.sup K + 1 := fun t =>
    Nat.lt_succ_of_le (Finset.le_sup (Finset.mem_univ t))
  rw [show (fun t => if t = s then (1 : ℝ) else 0)
      = itiIndicator φ vis (Finset.univ.sup K + 1) (fun k => vis ((φ ^ k) s)) from ?_]
  · exact itiIndicator_mem φ vis _ _
  · funext t
    rw [itiIndicator]
    by_cases ht : t = s
    · subst ht
      rw [if_pos rfl, if_pos fun k _ => rfl]
    · rw [if_neg ht, if_neg ?_]
      intro hall
      exact hKs t ht (hall (K t) (hlt t))

omit [Fintype I] in
/-- **THE ACTUAL DOMAIN SPANS.** Under itinerary separation the classical branch domain
spans the whole diagonal algebra: the singletons are already in it. -/
theorem separating_domain_span_top (φ : Equiv.Perm S) (vis : S → I)
    (hsep : ItinerarySeparating φ vis) :
    Submodule.span ℝ {w : S → ℝ | ClassicalBranchDomain φ vis w} = ⊤ := by
  rw [Submodule.eq_top_iff']
  intro w
  have hw : w = ∑ s, w s • (fun t => if t = s then (1 : ℝ) else 0) := by
    funext t
    rw [Finset.sum_apply, Finset.sum_congr rfl fun s _ => by
      rw [Pi.smul_apply, smul_eq_mul, mul_ite, mul_one, mul_zero],
      Finset.sum_ite_eq_of_mem Finset.univ t w (Finset.mem_univ t)]
  rw [hw]
  exact Submodule.sum_mem _ fun s _ => Submodule.smul_mem _ _
    (Submodule.subset_span (separating_singleton_mem φ vis hsep s))

/-! ### Section C — G1 earned, and the capstone -/

omit [Fintype I] in
/-- **G1 IS EARNED, NOT CHOSEN.** Under itinerary separation, the domain-relative glue
on the corpus's own classical branch preparations already implies the full
diagonal-sector glue. -/
theorem classicalBranch_glue_forces_G1 (U : Matrix S S ℂ) (φ : Equiv.Perm S)
    (vis : S → I) (hsep : ItinerarySeparating φ vis)
    (hglue : CompatibilityDomainGlue U φ {w | ClassicalBranchDomain φ vis w}) :
    DiagonalSectorGlue U φ :=
  spanning_domain_glue_implies_G1 U φ _ (separating_domain_span_top φ vis hsep) hglue

omit [Fintype I] in
/-- The monomial form follows: the sampled coherent dynamics of any completion whose
lift intertwines on the classical branch domain of an itinerary-separating cut is a
phased permutation. -/
theorem classicalBranch_glue_forces_monomial (U : Matrix S S ℂ) (φ : Equiv.Perm S)
    (vis : S → I) (hsep : ItinerarySeparating φ vis)
    (hglue : CompatibilityDomainGlue U φ {w | ClassicalBranchDomain φ vis w}) :
    ∃ d : S → ℂ, (∀ x, d x * conj' (d x) = 1)
      ∧ U = Matrix.diagonal d * permMatrix φ :=
  diagonalGlue_forces_monomial U φ (classicalBranch_glue_forces_G1 U φ vis hsep hglue)

omit [Fintype I] in
/-- **THE CAPSTONE.** OI compatibility — the domain-relative glue on the classical
branch domain — plus itinerary separation plus an ergodic shell close physical-flow SRC
with a canonical carrier: the classical shell ensemble is a stationary representation
reading out the uniform counting marginal, and EVERY stationary representation reads
out exactly that marginal. -/
theorem ergodicShell_SRC_of_domainGlue [Nonempty S] (U : Matrix S S ℂ)
    (φ : Equiv.Perm S) (vis : S → I) (hsep : ItinerarySeparating φ vis)
    (htrans : ∀ s t : S, ∃ k : ℕ, (φ ^ k) s = t)
    (hglue : CompatibilityDomainGlue U φ {w | ClassicalBranchDomain φ vis w}) :
    (∃ ρ : Matrix S S ℂ, ρ.PosSemidef ∧ Matrix.trace ρ = 1
        ∧ U * ρ * Uᴴ = ρ
        ∧ ∀ i, Matrix.trace (fiberProj vis i * ρ) = ((countMarginal vis i : ℝ) : ℂ))
    ∧ ∀ ρ : Matrix S S ℂ, ρ.PosSemidef → Matrix.trace ρ = 1
        → U * ρ * Uᴴ = ρ
        → ∀ i, Matrix.trace (fiberProj vis i * ρ) = ((countMarginal vis i : ℝ) : ℂ) :=
  ergodicShell_SRC_of_dynamicsGlue U φ vis htrans
    (classicalBranch_glue_forces_G1 U φ vis hsep hglue)

#print axioms spanning_domain_glue_implies_G1
#print axioms itiIndicator_mem
#print axioms separating_singleton_mem
#print axioms separating_domain_span_top
#print axioms classicalBranch_glue_forces_G1
#print axioms classicalBranch_glue_forces_monomial
#print axioms ergodicShell_SRC_of_domainGlue

end DomainGlue
end OIBridge
