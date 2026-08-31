/-
  OIBridge/ProjectiveAction.lean — coherent functoriality: the named bridge H-functor,
  and the theorem that it forces the projective monomial unitary action.

  PHASE THREE, ROUND EIGHTEEN. Round seventeen classified the coherent CPTP
  extensions of a single classical action as the correlation-matrix family and proved
  the per-action fork: reversibility ⟺ rank one ⟺ the monomial unitary lift. The
  corpus audit answers that fork: coherent reversibility is NOT earned from bare OI —
  the foundations audit records intertwining on the whole coherent state space as
  strongly conservative (an extra hypothesis, because coherences are data the enlarged
  theory has and OI never supplied), and Main's reversible substratum dilations
  explicitly do not discharge operational reversibility. So the selection principle is
  adopted as a NAMED BRIDGE, not derived:

      H-functor (coherent composition):  two intervention words representing the same
      reversible physical transformation represent the same transformation on the
      completed coherent state space —
      `CoherentFunctoriality`:  Φ_e = id  and  Φ_g ∘ Φ_h = Φ_{gh}.

  For a whole intervention menu there are two consistency questions — per-action rank
  one, and compatibility of the different monomial lifts with the classical
  composition relations. One principle closes both at once:

      ┌────────────────────────────────────────────────────────────────────┐
      │  `coherentFunctoriality_iff_projectiveMonomial`:                   │
      │  a functorial family of classical CPTP extensions of a group      │
      │  action is EXACTLY a projective monomial unitary action —         │
      │  C_g(s,t) = α_g(s)·ᾱ_g(t) with |α_g| = 1, and                     │
      │  α_h(s)·α_g(ρ_h s) = ω(g,h)·α_{gh}(s) with |ω(g,h)| = 1,          │
      │  so U_g·U_h = ω(g,h)·U_{gh}  (`functorial_projective_unitaries`)  │
      │  and ω is a 2-cocycle (`functorial_cocycle`).                     │
      └────────────────────────────────────────────────────────────────────┘

  Unitarity is not postulated: it FOLLOWS from H-functor through the round-seventeen
  reversibility fork (Φ_{g⁻¹}∘Φ_g = Φ_e = id gives every member a CPTP left inverse).
  The projective — not strict — binding replaces the probe-level observation of the
  Weyl-lift layer (its L1: H(u)H(v) = ±H(u+v), a projective representation with the
  cocycle question left open) by the exact classification.

  THE EPISTEMIC BOUNDARY, made unmistakable: `groupFamily_comb_blind` — any two
  unit-diagonal families over the same classical action produce identical classical
  action-labelled comb statistics, so complete classical comb data do not imply
  coherent functoriality (probe F31 exhibits the dephasing family on C₃: identical
  combs, Φ_g ∘ Φ_{g²} ≠ Φ_e). The programme's status is therefore exact:

      bare OI  ⟹  controlled-minimal classical core
                    + the correlation-matrix coherent extensions;
      + H-functor  ⟹  the projective monomial unitary action — quantum mechanics.

  Full operational QM is not presently a theorem of bare OI; the quantum branch is
  selected by exactly this coherent composition principle, and that is the precise
  boundary the programme set out to locate.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.CoherentExtension

namespace OIBridge
namespace ProjectiveAction

open Complex Matrix CoherentLift DynamicsGlue CoherentExtension
open scoped ComplexOrder

local notation "conj'" => (starRingEnd ℂ)

variable {S G : Type*} [Fintype S] [DecidableEq S] [Group G]

/-- **H-functor, the named bridge**: the coherent lifts of a classical group action
compose strictly — the identity intervention lifts to the identity channel and the
lift of a composite is the composite of the lifts. Operationally: two intervention
words representing the same reversible physical transformation represent the same
transformation on the completed coherent state space. This is adopted, not derived:
bare OI supplies the classical comb, which is blind to the correlation matrices. -/
def CoherentFunctoriality (ρ : G →* Equiv.Perm S) (C : G → Matrix S S ℂ) : Prop :=
  correlationExtension (ρ 1) (C 1) = LinearMap.id
    ∧ ∀ g h : G, (correlationExtension (ρ g) (C g)).comp
        (correlationExtension (ρ h) (C h))
      = correlationExtension (ρ (g * h)) (C (g * h))

/-- The monomial lift of a phase assignment: `U_g|s⟩ = α_g(s)|ρ_g s⟩`. -/
def monomialLift (ρ : G →* Equiv.Perm S) (α : G → S → ℂ) (g : G) :
    Matrix S S ℂ :=
  Matrix.diagonal (fun a => α g ((ρ g).symm a)) * permMatrix (ρ g)

omit [Fintype S] [DecidableEq S] in
/-- A unimodular number is nonzero. -/
theorem unimodular_ne_zero {z : ℂ} (h : z * conj' z = 1) : z ≠ 0 := by
  intro h0
  rw [h0, zero_mul] at h
  exact zero_ne_one h

omit [Fintype S] in
/-- A member of the correlation family determines its correlation matrix. -/
theorem correlationExtension_matrix_eq {p : Equiv.Perm S} {C C' : Matrix S S ℂ}
    (h : correlationExtension p C = correlationExtension p C') : C = C' := by
  ext s t
  have h0 := LinearMap.congr_fun h (Matrix.single s t 1)
  rw [correlationExtension_single, correlationExtension_single] at h0
  have h1 := congrFun (congrFun h0 (p s)) (p t)
  rw [Matrix.smul_apply, Matrix.smul_apply, smul_eq_mul, smul_eq_mul,
    Matrix.single_apply_same, mul_one, mul_one] at h1
  exact h1

/-- **H-functor forces per-action rank one**: in a functorial family every member has
a CPTP left inverse — the lift of the classical inverse — so by the round-seventeen
reversibility fork every correlation matrix is a rank-one unimodular phase matrix. -/
theorem functoriality_forces_rankOne [Nonempty S] (ρ : G →* Equiv.Perm S)
    (C : G → Matrix S S ℂ) (hpsd : ∀ g, (C g).PosSemidef)
    (hdiag : ∀ g s, C g s s = 1) (hF : CoherentFunctoriality ρ C) (g : G) :
    ∃ d : S → ℂ, (∀ s, d s * conj' (d s) = 1)
      ∧ ∀ s t, C g s t = d s * conj' (d t) := by
  have hcomp := hF.2 g⁻¹ g
  rw [inv_mul_cancel, hF.1] at hcomp
  exact (reversibleExtension_iff_rankOne (ρ g) (C g) (hpsd g)
    (hdiag g)).mp ⟨correlationExtension (ρ g⁻¹) (C g⁻¹),
      correlationExtension_cptp (ρ g⁻¹) (C g⁻¹) (hpsd g⁻¹) (hdiag g⁻¹), hcomp⟩

omit [Fintype S] in
/-- **The Schur composition law of a functorial family**: the correlation matrices
multiply along the classical transport. -/
theorem functoriality_schur_law (ρ : G →* Equiv.Perm S) (C : G → Matrix S S ℂ)
    (hF : CoherentFunctoriality ρ C) (g h : G) (s t : S) :
    C h s t * C g (ρ h s) (ρ h t) = C (g * h) s t := by
  have h1 := hF.2 g h
  rw [correlationExtension_comp, map_mul] at h1
  have h2 := correlationExtension_matrix_eq h1
  have h3 := congrFun (congrFun h2 s) t
  rwa [Matrix.of_apply] at h3

/-- **THE CAPSTONE.** A family of classical CPTP extensions of a group action is
coherently functorial exactly when it is a projective monomial unitary action: every
correlation matrix is a rank-one unimodular phase matrix and the phases obey the
projective composition law with a unimodular multiplier. -/
theorem coherentFunctoriality_iff_projectiveMonomial [Nonempty S]
    (ρ : G →* Equiv.Perm S) (C : G → Matrix S S ℂ)
    (hpsd : ∀ g, (C g).PosSemidef) (hdiag : ∀ g s, C g s s = 1) :
    CoherentFunctoriality ρ C
      ↔ ∃ (α : G → S → ℂ) (ω : G → G → ℂ),
          (∀ g s, α g s * conj' (α g s) = 1)
          ∧ (∀ g s t, C g s t = α g s * conj' (α g t))
          ∧ (∀ g h, ω g h * conj' (ω g h) = 1)
          ∧ ∀ g h s, α h s * α g (ρ h s) = ω g h * α (g * h) s := by
  constructor
  · intro hF
    choose α hαu hαC using functoriality_forces_rankOne ρ C hpsd hdiag hF
    set s₀ := Classical.arbitrary S with hs₀
    refine ⟨α, fun g h => α h s₀ * α g (ρ h s₀) * conj' (α (g * h) s₀),
      hαu, hαC, ?_, ?_⟩
    · intro g h
      rw [map_mul, map_mul, Complex.conj_conj]
      linear_combination (α g (ρ h s₀) * conj' (α g (ρ h s₀)) * α (g * h) s₀
          * conj' (α (g * h) s₀)) * hαu h s₀
        + (α (g * h) s₀ * conj' (α (g * h) s₀)) * hαu g (ρ h s₀)
        + hαu (g * h) s₀
    · intro g h s
      have hs := functoriality_schur_law ρ C hF g h s s₀
      rw [hαC, hαC, hαC] at hs
      linear_combination (α h s₀ * α g (ρ h s₀)) * hs
        - (α h s * α g (ρ h s) * (α g (ρ h s₀) * conj' (α g (ρ h s₀))))
          * hαu h s₀
        - (α h s * α g (ρ h s)) * hαu g (ρ h s₀)
  · rintro ⟨α, ω, hαu, hαC, hωu, hlaw⟩
    have hα1 : ∀ s, α 1 s = ω 1 1 := by
      intro s
      have h1 := hlaw 1 1 s
      rw [map_one, Equiv.Perm.one_apply, one_mul] at h1
      exact mul_right_cancel₀ (unimodular_ne_zero (hαu 1 s)) h1
    constructor
    · rw [map_one]
      refine (correlationExtension_one_eq_id_iff (C 1)).mpr fun s t => ?_
      rw [hαC, hα1 s, hα1 t]
      exact hωu 1 1
    · intro g h
      rw [correlationExtension_comp, map_mul]
      congr 1
      ext s t
      rw [Matrix.of_apply, hαC, hαC, hαC]
      have h1 := hlaw g h s
      have h2 := congrArg conj' (hlaw g h t)
      rw [map_mul, map_mul] at h2
      rw [show α h s * conj' (α h t) * (α g (ρ h s) * conj' (α g (ρ h t)))
          = (α h s * α g (ρ h s)) * (conj' (α h t) * conj' (α g (ρ h t)))
          from by ring, h1, h2,
        show ω g h * α (g * h) s * (conj' (ω g h) * conj' (α (g * h) t))
          = (ω g h * conj' (ω g h)) * (α (g * h) s * conj' (α (g * h) t))
          from by ring, hωu, one_mul]

/-- The entries of a monomial matrix. -/
theorem monomial_entry (d : S → ℂ) (p : Equiv.Perm S) (a b : S) :
    (Matrix.diagonal d * permMatrix p) a b
      = d a * (if p b = a then 1 else 0) := by
  rw [Matrix.mul_apply]
  rw [Finset.sum_congr rfl fun k _ => show Matrix.diagonal d a k * permMatrix p k b
      = if a = k then d a * permMatrix p k b else 0 from by
    rw [Matrix.diagonal_apply]
    by_cases hak : a = k
    · rw [if_pos hak, if_pos hak]
    · rw [if_neg hak, if_neg hak, zero_mul]]
  rw [Finset.sum_ite_eq_of_mem Finset.univ a
    (fun k => d a * permMatrix p k b) (Finset.mem_univ a)]
  rw [show permMatrix p a b = (if p b = a then (1 : ℂ) else 0) from rfl]

/-- **The projective unitary law**: the monomial lifts of a phase family obeying the
projective composition law multiply projectively — `U_g·U_h = ω(g,h)·U_{gh}`. -/
theorem functorial_projective_unitaries (ρ : G →* Equiv.Perm S) (α : G → S → ℂ)
    (ω : G → G → ℂ) (hlaw : ∀ g h s, α h s * α g (ρ h s) = ω g h * α (g * h) s)
    (g h : G) :
    monomialLift ρ α g * monomialLift ρ α h
      = ω g h • monomialLift ρ α (g * h) := by
  ext a b
  rw [Matrix.smul_apply, smul_eq_mul, monomialLift, monomialLift, monomialLift,
    Matrix.mul_apply, monomial_entry]
  rw [Finset.sum_congr rfl fun k _ => by
    rw [monomial_entry, monomial_entry]]
  rw [Finset.sum_congr rfl fun k _ => show
      (α g ((ρ g).symm a) * if (ρ g) k = a then (1 : ℂ) else 0)
        * (α h ((ρ h).symm k) * if (ρ h) b = k then (1 : ℂ) else 0)
      = if (ρ h) b = k
        then (α g ((ρ g).symm a) * if (ρ g) k = a then (1 : ℂ) else 0)
          * α h ((ρ h).symm k) else 0 from by
    by_cases hk : (ρ h) b = k
    · rw [if_pos hk, if_pos hk, mul_one]
    · rw [if_neg hk, if_neg hk, mul_zero, mul_zero]]
  rw [Finset.sum_ite_eq_of_mem Finset.univ ((ρ h) b) _ (Finset.mem_univ _),
    Equiv.symm_apply_apply]
  by_cases hab : (ρ g) ((ρ h) b) = a
  · rw [if_pos hab, if_pos (show (ρ (g * h)) b = a from by rw [map_mul]; exact hab),
      mul_one, mul_one,
      show (ρ g).symm a = (ρ h) b from by rw [← hab, Equiv.symm_apply_apply],
      show (ρ (g * h)).symm a = b from by
        rw [← hab, map_mul]
        exact Equiv.symm_apply_apply (ρ g * ρ h) b]
    linear_combination hlaw g h b
  · rw [if_neg hab,
      if_neg (show ¬(ρ (g * h)) b = a from fun hc => hab (by
        rw [map_mul] at hc
        exact hc)),
      mul_zero, zero_mul, mul_zero, mul_zero]

omit [Fintype S] [DecidableEq S] in
/-- **The multiplier is a 2-cocycle**: associativity of the classical action forces
`ω(g,h)·ω(gh,k) = ω(g,hk)·ω(h,k)` — the exact statement behind the Weyl-lift probe's
projective-representation observation. -/
theorem functorial_cocycle [Nonempty S] (ρ : G →* Equiv.Perm S) (α : G → S → ℂ)
    (ω : G → G → ℂ) (hαu : ∀ g s, α g s * conj' (α g s) = 1)
    (hlaw : ∀ g h s, α h s * α g (ρ h s) = ω g h * α (g * h) s) (g h k : G) :
    ω g h * ω (g * h) k = ω g (h * k) * ω h k := by
  set s := Classical.arbitrary S with hs
  have h1 := hlaw g h ((ρ k) s)
  have h2 := hlaw (g * h) k s
  have h3 := hlaw h k s
  have h4 := hlaw g (h * k) s
  rw [show (ρ (h * k)) s = (ρ h) ((ρ k) s) from by rw [map_mul]; rfl] at h4
  rw [mul_assoc] at h2
  refine mul_right_cancel₀ (unimodular_ne_zero (hαu (g * (h * k)) s)) ?_
  linear_combination (-(α k s)) * h1 - ω g h * h2
    + (α g ((ρ h) ((ρ k) s))) * h3 + ω h k * h4

omit [Fintype S] in
/-- **THE EPISTEMIC BOUNDARY.** Two unit-diagonal families over the same classical
group action produce identical classical action-labelled comb statistics for every
group word and every diagonal preparation: complete classical comb data cannot
distinguish a functorial family from a non-functorial one — H-functor is a genuine
additional principle, not a consequence of OI's operational data. -/
theorem groupFamily_comb_blind (ρ : G →* Equiv.Perm S) (C C' : G → Matrix S S ℂ)
    (h1 : ∀ g s, C g s s = 1) (h2 : ∀ g s, C' g s s = 1) (w : List G) (μ : S → ℂ) :
    combFold (w.map fun g => (ρ g, C g)) μ
      = combFold (w.map fun g => (ρ g, C' g)) μ := by
  refine classicalComb_blind_to_correlation _ _ ?_ ?_ ?_ μ
  · rw [List.map_map, List.map_map]
    congr 1
  · intro p hp
    obtain ⟨g, _, rfl⟩ := List.mem_map.mp hp
    exact h1 g
  · intro p hp
    obtain ⟨g, _, rfl⟩ := List.mem_map.mp hp
    exact h2 g

#print axioms unimodular_ne_zero
#print axioms correlationExtension_matrix_eq
#print axioms functoriality_forces_rankOne
#print axioms functoriality_schur_law
#print axioms coherentFunctoriality_iff_projectiveMonomial
#print axioms monomial_entry
#print axioms functorial_projective_unitaries
#print axioms functorial_cocycle
#print axioms groupFamily_comb_blind

end ProjectiveAction
end OIBridge
