/-
  OIBridge/WeylLift.lean — trivializing the sign cocycle, and the character projectors.

  LAYER 3 of [Main] Theorem (separability threshold): the maximal case `t = s`.

  WHY THIS FILE EXISTS. The natural way to diagonalize a commuting family of Weyl operators is to
  take the self-adjoint involutions `H u = i^{b·a} W u` and build the character projectors
  `P_χ = |G|⁻¹ Σ_{g ∈ G} χ(g) H g`. That construction is wrong, and `WeylTwirl.H_not_multiplicative`
  is the kernel-checked reason: `H` is a PROJECTIVE representation on an isotropic subspace, not a
  representation. `H u · H v = ±H (u+v)`, and the sign is `−1` for commuting pairs — at `s = 2`, for
  the Lagrangian `⟨(0,1|0,1), (1,0|1,0)⟩`, on six of its pairs. Without multiplicativity `P_χ` is not
  idempotent; numerically its trace is still `1` but its rank is `2^s`.

  The sign is a 2-cocycle on `G` with values in `{±1}`, and it IS a coboundary — every `H u` is an
  involution, so the extension splits — but no closed formula trivializes it: a splitting is a choice
  of basis. This file makes that choice explicit. Given a tuple `g : Fin t → PS s` of pairwise
  commuting generators, `lift` is the ordered product

      lift g c  =  fac (g 0) (c 0) · fac (g 1) (c 1) · ⋯,      fac u z = if z = 0 then 1 else H u,

  which IS a homomorphism `(𝔽₂^t, +) → matrices`, because the factors commute and square to `1`.
  Everything downstream — idempotence, orthogonality, the resolution of the identity — is then the
  ordinary character calculus of an elementary abelian 2-group, with no cocycle left in it.

  The lift depends on the tuple, not just on the subspace it spans. That is not a defect of the
  formalization; it is the content of the obstruction.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.WeylTwirl
import Mathlib.LinearAlgebra.Trace
import Mathlib.LinearAlgebra.Projection
import Mathlib.LinearAlgebra.Matrix.ToLin

namespace OIBridge

namespace WeylLift

set_option autoImplicit false

open Matrix Finset OIBridge.WeylTwirl

variable {s : ℕ}

/-! ### The single-generator factor -/

/-- `fac u 0 = 1`, `fac u 1 = H u`. -/
noncomputable def fac (u : PS s) (z : ZMod 2) : Matrix (Q s) (Q s) ℂ := if z = 0 then 1 else H u

@[simp] theorem fac_zero (u : PS s) : fac u 0 = 1 := if_pos rfl

@[simp] theorem fac_one (u : PS s) : fac u 1 = H u := if_neg (by decide)

/-- **The factor is multiplicative**, because `H u` is an involution. -/
theorem fac_mul (u : PS s) (z z' : ZMod 2) : fac u z * fac u z' = fac u (z + z') := by
  rcases zmod_two_cases z with rfl | rfl <;> rcases zmod_two_cases z' with rfl | rfl <;>
    simp [H_mul_self, one_add_one]

theorem fac_conjTranspose (u : PS s) (z : ZMod 2) : (fac u z)ᴴ = fac u z := by
  rcases zmod_two_cases z with rfl | rfl <;> simp [H_conjTranspose]

theorem fac_commute_H (u v : PS s) (h : omega u v = 0) (z : ZMod 2) :
    fac u z * H v = H v * fac u z := by
  rcases zmod_two_cases z with rfl | rfl <;> simp [H_commute u v h]

/-! ### The multiplicative lift -/

/-- **The lift along a spanning tuple.** The ordered product `∏_{i : c i = 1} H (g i)`. -/
noncomputable def lift : (t : ℕ) → (Fin t → PS s) → (Fin t → ZMod 2) → Matrix (Q s) (Q s) ℂ
  | 0, _, _ => 1
  | t + 1, g, c => fac (g 0) (c 0) * lift t (fun i => g i.succ) (fun i => c i.succ)

@[simp] theorem lift_zero (g : Fin 0 → PS s) (c : Fin 0 → ZMod 2) : lift 0 g c = 1 := rfl

theorem lift_succ (t : ℕ) (g : Fin (t + 1) → PS s) (c : Fin (t + 1) → ZMod 2) :
    lift (t + 1) g c = fac (g 0) (c 0) * lift t (fun i => g i.succ) (fun i => c i.succ) := rfl

/-- Anything commuting with every generator commutes with every lift. -/
theorem commute_lift (M : Matrix (Q s) (Q s) ℂ) :
    ∀ (t : ℕ) (g : Fin t → PS s) (c : Fin t → ZMod 2),
      (∀ i, M * H (g i) = H (g i) * M) → M * lift t g c = lift t g c * M := by
  intro t
  induction t with
  | zero => intro g c _; rw [lift_zero, mul_one, one_mul]
  | succ t ih =>
    intro g c h
    rw [lift_succ]
    have hA : M * fac (g 0) (c 0) = fac (g 0) (c 0) * M := by
      rcases zmod_two_cases (c 0) with h0 | h0 <;> rw [h0]
      · rw [fac_zero, mul_one, one_mul]
      · rw [fac_one]; exact h 0
    have hL := ih (fun i => g i.succ) (fun i => c i.succ) fun i => h i.succ
    rw [← mul_assoc, hA, mul_assoc, hL, ← mul_assoc]

/-- **The lift is a homomorphism `(𝔽₂^t, +) → matrices`.** This is the whole point of the file:
the sign that defeats `H` is gone. -/
theorem lift_mul : ∀ (t : ℕ) (g : Fin t → PS s), (∀ i j, omega (g i) (g j) = 0) →
    ∀ c c' : Fin t → ZMod 2, lift t g c * lift t g c' = lift t g (c + c') := by
  intro t
  induction t with
  | zero => intro g _ c c'; rw [lift_zero, lift_zero, lift_zero, mul_one]
  | succ t ih =>
    intro g hg c c'
    rw [lift_succ, lift_succ, lift_succ]
    have hcomm : fac (g 0) (c' 0) * lift t (fun i => g i.succ) (fun i => c i.succ)
        = lift t (fun i => g i.succ) (fun i => c i.succ) * fac (g 0) (c' 0) :=
      commute_lift _ t _ _ fun i => fac_commute_H (g 0) (g i.succ) (hg 0 i.succ) (c' 0)
    have step : fac (g 0) (c 0) * lift t (fun i => g i.succ) (fun i => c i.succ) *
          (fac (g 0) (c' 0) * lift t (fun i => g i.succ) (fun i => c' i.succ))
        = fac (g 0) (c 0) * fac (g 0) (c' 0) *
          (lift t (fun i => g i.succ) (fun i => c i.succ) *
            lift t (fun i => g i.succ) (fun i => c' i.succ)) := by
      simp only [mul_assoc]
      rw [← mul_assoc (lift t (fun i => g i.succ) (fun i => c i.succ)), ← hcomm, mul_assoc]
    rw [step, fac_mul, ih (fun i => g i.succ) (fun i j => hg i.succ j.succ)
      (fun i => c i.succ) (fun i => c' i.succ)]
    rfl

theorem lift_conjTranspose : ∀ (t : ℕ) (g : Fin t → PS s), (∀ i j, omega (g i) (g j) = 0) →
    ∀ c : Fin t → ZMod 2, (lift t g c)ᴴ = lift t g c := by
  intro t
  induction t with
  | zero => intro g _ c; rw [lift_zero, Matrix.conjTranspose_one]
  | succ t ih =>
    intro g hg c
    rw [lift_succ, Matrix.conjTranspose_mul, fac_conjTranspose,
      ih (fun i => g i.succ) (fun i j => hg i.succ j.succ) (fun i => c i.succ)]
    exact (commute_lift _ t _ _ fun i =>
      fac_commute_H (g 0) (g i.succ) (hg 0 i.succ) (c 0)).symm

theorem lift_coeff_zero : ∀ (t : ℕ) (g : Fin t → PS s), lift t g 0 = 1 := by
  intro t
  induction t with
  | zero => intro g; rw [lift_zero]
  | succ t ih =>
    intro g
    rw [lift_succ]
    show fac (g 0) 0 * lift t (fun i => g i.succ) 0 = 1
    rw [fac_zero, one_mul, ih]

/-- **Each lift is a nonzero multiple of a single Weyl operator**, the one at the `𝔽₂`-combination
the coefficients name. The sign is exactly what no formula pins down; that it is nonzero is all the
trace computation needs. -/
theorem lift_eq_smul_W : ∀ (t : ℕ) (g : Fin t → PS s) (c : Fin t → ZMod 2),
    ∃ ζ : ℂ, ζ ≠ 0 ∧ lift t g c = ζ • W (∑ i, c i • g i) := by
  intro t
  induction t with
  | zero =>
    intro g c
    refine ⟨1, one_ne_zero, ?_⟩
    rw [lift_zero, Finset.univ_eq_empty, Finset.sum_empty, W_zero, one_smul]
  | succ t ih =>
    intro g c
    obtain ⟨ζ, hζ, hL⟩ := ih (fun i => g i.succ) (fun i => c i.succ)
    have hsum : (∑ i, c i • g i) = c 0 • g 0 + ∑ i : Fin t, c i.succ • g i.succ :=
      Fin.sum_univ_succ _
    rw [lift_succ, hL]
    rcases zmod_two_cases (c 0) with h0 | h0
    · refine ⟨ζ, hζ, ?_⟩
      rw [h0, fac_zero, one_mul, hsum, h0, zero_smul, zero_add]
    · refine ⟨iPow (dotF (g 0).2 (g 0).1) * ζ *
        chi (dotF (g 0).2 (∑ i : Fin t, c i.succ • g i.succ).1), ?_, ?_⟩
      · exact mul_ne_zero (mul_ne_zero (iPow_ne_zero _) hζ) (chi_ne_zero _)
      · rw [h0, fac_one, H, Matrix.smul_mul, Matrix.mul_smul, W_mul, smul_smul, smul_smul,
          hsum, h0, one_smul]

/-! ### The character projectors

`P t g e = 2^{-t} Σ_c (−1)^{e·c} lift g c`, the projector onto the joint eigenspace where each
`H (g i)` has eigenvalue `(−1)^{e i}`. With `lift` a genuine homomorphism, every property below is
the ordinary character calculus of `(𝔽₂^t, +)`. -/

/-- The size of the coefficient space. -/
theorem card_coeff (t : ℕ) : Fintype.card (Fin t → ZMod 2) = 2 ^ t := card_Q (s := t)

theorem coeff_cast_ne_zero (t : ℕ) : ((2 ^ t : ℕ) : ℂ) ≠ 0 := by
  simp

/-- **The character projector.** -/
noncomputable def P (t : ℕ) (g : Fin t → PS s) (e : Fin t → ZMod 2) : Matrix (Q s) (Q s) ℂ :=
  ((2 ^ t : ℕ) : ℂ)⁻¹ • ∑ c : Fin t → ZMod 2, chi (dotF e c) • lift t g c

/-- **`P` is self-adjoint.** -/
theorem P_conjTranspose (t : ℕ) (g : Fin t → PS s) (hg : ∀ i j, omega (g i) (g j) = 0)
    (e : Fin t → ZMod 2) : (P t g e)ᴴ = P t g e := by
  rw [P, Matrix.conjTranspose_smul, Matrix.conjTranspose_sum]
  congr 1
  · simp
  · exact Finset.sum_congr rfl fun c _ => by
      rw [Matrix.conjTranspose_smul, chi_conj, lift_conjTranspose t g hg c]

/-- **`P` is idempotent.** -/
theorem P_mul_self (t : ℕ) (g : Fin t → PS s) (hg : ∀ i j, omega (g i) (g j) = 0)
    (e : Fin t → ZMod 2) : P t g e * P t g e = P t g e := by
  have hN := coeff_cast_ne_zero t
  simp only [P]
  rw [Matrix.smul_mul, Matrix.mul_smul, smul_smul, Finset.sum_mul_sum]
  have hinner : ∀ c : Fin t → ZMod 2,
      (∑ c' : Fin t → ZMod 2, (chi (dotF e c) • lift t g c) * (chi (dotF e c') • lift t g c'))
        = ∑ d : Fin t → ZMod 2, chi (dotF e d) • lift t g d := by
    intro c
    have hre : (∑ c' : Fin t → ZMod 2,
          (chi (dotF e c) • lift t g c) * (chi (dotF e (c + c')) • lift t g (c + c')))
        = ∑ c' : Fin t → ZMod 2,
          (chi (dotF e c) • lift t g c) * (chi (dotF e c') • lift t g c') :=
      Fintype.sum_equiv (Equiv.addLeft c) _ _ fun _ => rfl
    rw [← hre]
    refine Finset.sum_congr rfl fun d _ => ?_
    rw [Matrix.smul_mul, Matrix.mul_smul, smul_smul, ← chi_add, lift_mul t g hg,
      ← add_assoc, add_comm c c, ]
    rw [show ∀ x : Fin t → ZMod 2, x + x = 0 from fun x => funext fun i =>
      CharTwo.add_self_eq_zero _]
    rw [zero_add]
    congr 1
    rw [← dotF_add_right]
    congr 1
    rw [← add_assoc, add_comm c c, show ∀ x : Fin t → ZMod 2, x + x = 0 from fun x =>
      funext fun i => CharTwo.add_self_eq_zero _, zero_add]
  rw [Finset.sum_congr rfl fun c _ => hinner c, Finset.sum_const, card_univ, card_coeff,
    ← Nat.cast_smul_eq_nsmul ℂ, smul_smul]
  congr 1
  rw [mul_assoc, inv_mul_cancel₀ hN, mul_one]

/-- **Distinct characters give orthogonal projectors.** -/
theorem P_mul_of_ne (t : ℕ) (g : Fin t → PS s) (hg : ∀ i j, omega (g i) (g j) = 0)
    {e e' : Fin t → ZMod 2} (hne : e ≠ e') : P t g e * P t g e' = 0 := by
  have hsum : e + e' ≠ 0 := fun hc => hne (by
    have := congrArg (fun x : Fin t → ZMod 2 => e + x) hc
    simpa [← add_assoc, show ∀ x : Fin t → ZMod 2, x + x = 0 from fun x =>
      funext fun i => CharTwo.add_self_eq_zero _] using this.symm)
  rw [P, P, Matrix.smul_mul, Matrix.mul_smul, smul_smul, Finset.sum_mul_sum]
  have hzero : (∑ c : Fin t → ZMod 2, ∑ c' : Fin t → ZMod 2,
      (chi (dotF e c) • lift t g c) * (chi (dotF e' c') • lift t g c')) = 0 := by
    have hre : ∀ c : Fin t → ZMod 2,
        (∑ c' : Fin t → ZMod 2, (chi (dotF e c) • lift t g c) * (chi (dotF e' c') • lift t g c'))
          = ∑ d : Fin t → ZMod 2,
            (chi (dotF (e + e') c) * chi (dotF e' d)) • lift t g d := by
      intro c
      have hshift : (∑ d : Fin t → ZMod 2,
            (chi (dotF e c) • lift t g c) * (chi (dotF e' (c + d)) • lift t g (c + d)))
          = ∑ c' : Fin t → ZMod 2,
            (chi (dotF e c) • lift t g c) * (chi (dotF e' c') • lift t g c') :=
        Fintype.sum_equiv (Equiv.addLeft c) _ _ fun _ => rfl
      rw [← hshift]
      refine Finset.sum_congr rfl fun d _ => ?_
      have hcc : ∀ x : Fin t → ZMod 2, x + x = 0 := fun x => funext fun i =>
        CharTwo.add_self_eq_zero _
      rw [Matrix.smul_mul, Matrix.mul_smul, smul_smul, lift_mul t g hg,
        ← add_assoc, add_comm c c, hcc, zero_add, dotF_add_right, dotF_add_left, chi_add, chi_add]
      ring_nf
    rw [Finset.sum_congr rfl fun c _ => hre c, Finset.sum_comm]
    refine Finset.sum_eq_zero fun d _ => ?_
    have : (∑ c : Fin t → ZMod 2, (chi (dotF (e + e') c) * chi (dotF e' d)) • lift t g d)
        = ((∑ c : Fin t → ZMod 2, chi (dotF (e + e') c)) * chi (dotF e' d)) • lift t g d := by
      rw [← Finset.sum_smul, ← Finset.sum_mul]
    rw [this, sum_chi_dotF (s := t) (e + e'), if_neg hsum, zero_mul, zero_smul]
  rw [hzero, smul_zero]

/-- **The projectors resolve the identity.** -/
theorem sum_P (t : ℕ) (g : Fin t → PS s) : (∑ e : Fin t → ZMod 2, P t g e) = 1 := by
  have hN := coeff_cast_ne_zero t
  simp only [P]
  rw [← Finset.smul_sum, Finset.sum_comm]
  have : (∑ c : Fin t → ZMod 2, ∑ e : Fin t → ZMod 2, chi (dotF e c) • lift t g c)
      = ((2 ^ t : ℕ) : ℂ) • lift t g 0 := by
    refine (Finset.sum_eq_single (0 : Fin t → ZMod 2) ?_ ?_).trans ?_
    · intro c _ hc
      rw [← Finset.sum_smul,
        Finset.sum_congr rfl fun e (_ : e ∈ Finset.univ) => congrArg chi (dotF_comm (s := t) e c),
        sum_chi_dotF (s := t) c, if_neg hc, zero_smul]
    · intro hc; exact absurd (Finset.mem_univ _) hc
    · rw [← Finset.sum_smul,
        Finset.sum_congr rfl fun e (_ : e ∈ Finset.univ) => congrArg chi (dotF_comm (s := t) e 0),
        sum_chi_dotF (s := t) 0, if_pos rfl]
  rw [this, lift_coeff_zero, smul_smul, inv_mul_cancel₀ hN, one_smul]

/-- **The trace of a projector.** With the generators independent, every `lift` but the trivial one
is traceless, so only the `c = 0` term survives. -/
theorem trace_P (t : ℕ) (g : Fin t → PS s)
    (hind : ∀ c : Fin t → ZMod 2, (∑ i, c i • g i) = 0 → c = 0) (e : Fin t → ZMod 2) :
    Matrix.trace (P t g e) = ((2 ^ t : ℕ) : ℂ)⁻¹ * ((2 ^ s : ℕ) : ℂ) := by
  rw [P, Matrix.trace_smul, Matrix.trace_sum, smul_eq_mul]
  congr 1
  refine (Finset.sum_eq_single (0 : Fin t → ZMod 2) ?_ ?_).trans ?_
  · intro c _ hc
    obtain ⟨ζ, _, hL⟩ := lift_eq_smul_W t g c
    rw [Matrix.trace_smul, hL, Matrix.trace_smul, trace_W, if_neg fun h0 => hc (hind c h0),
      smul_zero, smul_zero]
  · intro hc; exact absurd (Finset.mem_univ _) hc
  · rw [lift_coeff_zero, dotF_zero_right, chi_zero, one_smul, Matrix.trace_one, card_Q]

/-- **At `t = s` the projectors have trace one.** Together with idempotence and self-adjointness
this is the rank-one statement the maximal case needs: the joint eigenspaces are lines. -/
theorem trace_P_eq_one (g : Fin s → PS s)
    (hind : ∀ c : Fin s → ZMod 2, (∑ i, c i • g i) = 0 → c = 0) (e : Fin s → ZMod 2) :
    Matrix.trace (P s g e) = 1 := by
  rw [trace_P s g hind e, inv_mul_cancel₀ (coeff_cast_ne_zero s)]

/-! ### Rank one

The gate the maximal case turns on: at `t = s` with independent generators, each joint eigenspace is
a LINE. Idempotence makes `P` a projection onto its range, so its trace is that range's dimension,
and the trace is `1`. Nothing here is hidden under "maximal abelian". -/

theorem isIdempotentElem_toLin' (t : ℕ) (g : Fin t → PS s) (hg : ∀ i j, omega (g i) (g j) = 0)
    (e : Fin t → ZMod 2) : IsIdempotentElem (Matrix.toLin' (P t g e)) := by
  have h : Matrix.toLin' (P t g e) * Matrix.toLin' (P t g e) = Matrix.toLin' (P t g e) := by
    rw [Module.End.mul_eq_comp, ← Matrix.toLin'_mul, P_mul_self t g hg e]
  exact h

/-- **Each character projector has rank one.** -/
theorem finrank_range_P (g : Fin s → PS s) (hg : ∀ i j, omega (g i) (g j) = 0)
    (hind : ∀ c : Fin s → ZMod 2, (∑ i, c i • g i) = 0 → c = 0) (e : Fin s → ZMod 2) :
    Module.finrank ℂ (LinearMap.range (Matrix.toLin' (P s g e))) = 1 := by
  have hproj := LinearMap.IsIdempotentElem.isProj_range _ (isIdempotentElem_toLin' s g hg e)
  have htr := hproj.trace
  rw [Matrix.trace_toLin'_eq, trace_P_eq_one g hind e] at htr
  exact_mod_cast htr.symm

/-! ### What these proofs rest on -/

#print axioms fac_mul
#print axioms lift_mul
#print axioms lift_conjTranspose
#print axioms lift_eq_smul_W
#print axioms P_conjTranspose
#print axioms P_mul_self
#print axioms P_mul_of_ne
#print axioms sum_P
#print axioms trace_P
#print axioms trace_P_eq_one

end WeylLift

end OIBridge
