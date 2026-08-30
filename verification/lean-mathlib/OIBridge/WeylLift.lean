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

  The sign is a 2-cocycle on `G` with values in `{±1}`, and it is a coboundary — but not because
  each `H u` happens to be an involution, which is true of `H` everywhere and settles nothing. What
  trivializes it is that on an ISOTROPIC subspace a chosen `𝔽₂`-basis gives a family of COMMUTING
  involutions, and the ordered products of a commuting family of involutions are an honest
  representation of `(𝔽₂^t, +)`. Both halves are needed and both are used below: `H_mul_self` for
  the squares and `H_commute` for the reordering. No closed formula does this — a splitting is a
  choice of basis — so this file makes the choice explicit. Given a tuple `g : Fin t → PS s` of
  pairwise commuting generators, `lift` is the ordered product

      lift g c  =  fac (g 0) (c 0) · fac (g 1) (c 1) · ⋯,      fac u z = if z = 0 then 1 else H u,

  which IS a homomorphism `(𝔽₂^t, +) → matrices`, because the factors commute and square to `1`.
  Everything downstream — idempotence, orthogonality, the resolution of the identity — is then the
  ordinary character calculus of an elementary abelian 2-group, with no cocycle left in it.

  The lift depends on the tuple, not just on the subspace it spans. That is not a defect of the
  formalization; it is the content of the obstruction.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.WeylTwirl
import OIBridge.Separability
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

/-! ### Unit scalars

The lift's scalar is never pinned down by a formula, but it always has modulus one, and that is all
the conjugation `L ρ L†` needs in order to forget it. -/

/-- Modulus one is multiplicative. -/
theorem unit_mul {a b : ℂ} (ha : star a * a = 1) (hb : star b * b = 1) :
    star (a * b) * (a * b) = 1 := by
  rw [star_mul']
  calc star a * star b * (a * b) = (star b * b) * (star a * a) := by ring
    _ = 1 := by rw [ha, hb, mul_one]

theorem chi_unit (z : ZMod 2) : star (chi z) * chi z = 1 := by rw [chi_conj, chi_mul_self]

/-- **Each lift is a UNIT multiple of a single Weyl operator**, the one at the `𝔽₂`-combination the
coefficients name. The scalar is exactly what no formula pins down; that it has modulus one is what
makes the conjugation `L ρ L†` forget it entirely, which is how the projector sum reproduces the
twirl. -/
theorem lift_eq_smul_W : ∀ (t : ℕ) (g : Fin t → PS s) (c : Fin t → ZMod 2),
    ∃ ζ : ℂ, star ζ * ζ = 1 ∧ lift t g c = ζ • W (∑ i, c i • g i) := by
  intro t
  induction t with
  | zero =>
    intro g c
    refine ⟨1, by simp, ?_⟩
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
      · exact unit_mul (unit_mul (iPow_mul_star _) hζ) (chi_unit _)
      · rw [h0, fac_one, H, Matrix.smul_mul, Matrix.mul_smul, W_mul, smul_smul, smul_smul,
          hsum, h0, one_smul]

theorem lift_ne_zero (t : ℕ) (g : Fin t → PS s) (c : Fin t → ZMod 2) :
    ∃ ζ : ℂ, ζ ≠ 0 ∧ lift t g c = ζ • W (∑ i, c i • g i) := by
  obtain ⟨ζ, hζ, hL⟩ := lift_eq_smul_W t g c
  exact ⟨ζ, fun hc => by rw [hc] at hζ; simp at hζ, hL⟩

/-- **Conjugation by a lift is conjugation by its Weyl operator.** The unit scalar cancels against
its own conjugate, so the arbitrary choice the lift makes is invisible here — which is why a
tuple-dependent construction can reproduce the tuple-independent twirl. -/
theorem lift_conj (t : ℕ) (g : Fin t → PS s) (hg : ∀ i j, omega (g i) (g j) = 0)
    (c : Fin t → ZMod 2) (ρ : Matrix (Q s) (Q s) ℂ) :
    lift t g c * ρ * lift t g c
      = W (∑ i, c i • g i) * ρ * (W (∑ i, c i • g i))ᴴ := by
  obtain ⟨ζ, hζ, hL⟩ := lift_eq_smul_W t g c
  have hadj : (star ζ) • (W (∑ i, c i • g i))ᴴ = ζ • W (∑ i, c i • g i) := by
    rw [← Matrix.conjTranspose_smul, ← hL, lift_conjTranspose t g hg c, hL]
  calc lift t g c * ρ * lift t g c
      = (ζ • W (∑ i, c i • g i)) * ρ * ((star ζ) • (W (∑ i, c i • g i))ᴴ) := by
        rw [hadj, hL]
    _ = (star ζ * ζ) • (W (∑ i, c i • g i) * ρ * (W (∑ i, c i • g i))ᴴ) := by
        rw [Matrix.smul_mul, Matrix.mul_smul, Matrix.smul_mul, smul_smul]
    _ = W (∑ i, c i • g i) * ρ * (W (∑ i, c i • g i))ᴴ := by rw [hζ, one_smul]

/-! ### From a subspace to a spanning tuple

The manuscript theorem starts from an arbitrary isotropic `G` with `|G| = 2^s`, not from a tuple, so
the tuple must be PRODUCED and not assumed — otherwise the wrapper would quietly acquire a new
hypothesis. The extraction is greedy and elementary: start from the empty tuple, and while the span
is not all of `G`, adjoin any element outside it. Independence is preserved because in
characteristic two a new element either has coefficient `0`, in which case the old tuple's
independence applies, or coefficient `1`, in which case it lies in the old span. The span grows
strictly at every step, so the process stops; and when it stops, `2^t = |span| = |G| = 2^s` forces
`t = s`.

No basis theory is invoked. That is not only frugality: a `Submodule (ZMod 2) (PS s)` carries the
`Semiring` coming from `ZMod`'s `CommRing`, and Mathlib's vector-space lemmas want the one coming
from its `Field`, a defeq check that does not terminate here. -/

/-- The `𝔽₂`-combination a coefficient vector names. -/
def vsum (t : ℕ) (g : Fin t → PS s) (c : Fin t → ZMod 2) : PS s := ∑ i, c i • g i

theorem vsum_add (t : ℕ) (g : Fin t → PS s) (c c' : Fin t → ZMod 2) :
    vsum t g (c + c') = vsum t g c + vsum t g c' := by
  rw [vsum, vsum, vsum, ← Finset.sum_add_distrib]
  exact Finset.sum_congr rfl fun i _ => by rw [Pi.add_apply, add_smul]

theorem vsum_zero (t : ℕ) (g : Fin t → PS s) : vsum t g 0 = 0 := by
  rw [vsum, Finset.sum_congr rfl fun i (_ : i ∈ Finset.univ) => by
    show (0 : ZMod 2) • g i = 0
    rw [zero_smul], Finset.sum_const_zero]

/-- **Independence** of a tuple: only the zero coefficient vector sums to zero. -/
def Indep (t : ℕ) (g : Fin t → PS s) : Prop := ∀ c, vsum t g c = 0 → c = 0

theorem vsum_injective {t : ℕ} {g : Fin t → PS s} (h : Indep t g) :
    Function.Injective (vsum t g) := by
  intro c c' hcc
  have h0 : vsum t g (c + c') = 0 := by rw [vsum_add, hcc, addPS_self]
  have hz := h _ h0
  funext i
  have hi : c i + c' i = 0 := congrFun hz i
  show c i = c' i
  rcases zmod_two_cases (c i) with h1 | h1 <;> rcases zmod_two_cases (c' i) with h2 | h2 <;>
    rw [h1, h2] at hi ⊢ <;> first | rfl | (exfalso; revert hi; decide)

/-- The span of a tuple, as a `Finset`. -/
def spanF (t : ℕ) (g : Fin t → PS s) : Finset (PS s) :=
  Finset.image (vsum t g) Finset.univ

theorem mem_spanF {t : ℕ} {g : Fin t → PS s} {v : PS s} :
    v ∈ spanF t g ↔ ∃ c, vsum t g c = v := by simp [spanF]

theorem card_spanF {t : ℕ} {g : Fin t → PS s} (h : Indep t g) :
    (spanF t g).card = 2 ^ t := by
  rw [spanF, Finset.card_image_of_injective _ (vsum_injective h), Finset.card_univ,
    card_Q (s := t)]

theorem vsum_mem {t : ℕ} {g : Fin t → PS s} {G : Submodule (ZMod 2) (PS s)}
    (hmem : ∀ i, g i ∈ G) (c : Fin t → ZMod 2) : vsum t g c ∈ G :=
  Submodule.sum_mem _ fun i _ => Submodule.smul_mem _ _ (hmem i)

theorem spanF_subset {t : ℕ} {g : Fin t → PS s} {G : Submodule (ZMod 2) (PS s)}
    [DecidablePred (· ∈ G)] (hmem : ∀ i, g i ∈ G) : spanF t g ⊆ gset G := by
  intro v hv
  obtain ⟨c, rfl⟩ := mem_spanF.1 hv
  exact (mem_gset G).2 (vsum_mem hmem c)

theorem vsum_cons (t : ℕ) (u : PS s) (g : Fin t → PS s) (c : Fin (t + 1) → ZMod 2) :
    vsum (t + 1) (Fin.cons u g) c = c 0 • u + vsum t g (fun i => c i.succ) := by
  rw [vsum, Fin.sum_univ_succ, Fin.cons_zero, vsum]
  simp only [Fin.cons_succ]

theorem indep_cons {t : ℕ} {u : PS s} {g : Fin t → PS s} (h : Indep t g)
    (hu : u ∉ spanF t g) : Indep (t + 1) (Fin.cons u g) := by
  intro c hc
  rw [vsum_cons] at hc
  rcases zmod_two_cases (c 0) with h0 | h0
  · rw [h0, zero_smul, zero_add] at hc
    have hz := h _ hc
    funext i
    refine Fin.cases ?_ ?_ i
    · exact h0
    · intro j; exact congrFun hz j
  · exfalso
    rw [h0, one_smul] at hc
    refine hu (mem_spanF.2 ⟨fun i => c i.succ, ?_⟩)
    have h2 := congrArg (fun x : PS s => x + vsum t g (fun i => c i.succ)) hc
    simp only [zero_add] at h2
    rw [add_assoc, addPS_self, add_zero] at h2
    exact h2.symm

theorem spanF_subset_cons {t : ℕ} (u : PS s) (g : Fin t → PS s) :
    spanF t g ⊆ spanF (t + 1) (Fin.cons u g) := by
  intro v hv
  obtain ⟨c, rfl⟩ := mem_spanF.1 hv
  refine mem_spanF.2 ⟨Fin.cons 0 c, ?_⟩
  rw [vsum_cons, Fin.cons_zero, zero_smul, zero_add]
  simp only [Fin.cons_succ]

theorem mem_spanF_cons {t : ℕ} (u : PS s) (g : Fin t → PS s) :
    u ∈ spanF (t + 1) (Fin.cons u g) := by
  refine mem_spanF.2 ⟨Fin.cons 1 0, ?_⟩
  rw [vsum_cons, Fin.cons_zero, one_smul]
  have hz : (fun i : Fin t => (Fin.cons (1 : ZMod 2) 0 : Fin (t + 1) → ZMod 2) i.succ)
      = (0 : Fin t → ZMod 2) := funext fun i => by rw [Fin.cons_succ]
  rw [hz, vsum_zero, add_zero]

/-- **The greedy extraction.** -/
theorem exists_indep_span (G : Submodule (ZMod 2) (PS s)) [DecidablePred (· ∈ G)] :
    ∀ (n t : ℕ) (g : Fin t → PS s), (∀ i, g i ∈ G) → Indep t g →
      (gset G).card ≤ (spanF t g).card + n →
      ∃ (t' : ℕ) (g' : Fin t' → PS s), (∀ i, g' i ∈ G) ∧ Indep t' g' ∧ spanF t' g' = gset G := by
  intro n
  induction n with
  | zero =>
    intro t g hmem hind hle
    exact ⟨t, g, hmem, hind, Finset.eq_of_subset_of_card_le (spanF_subset hmem) (by omega)⟩
  | succ n ih =>
    intro t g hmem hind hle
    by_cases hEq : spanF t g = gset G
    · exact ⟨t, g, hmem, hind, hEq⟩
    · obtain ⟨u, huG, hus⟩ : ∃ u ∈ gset G, u ∉ spanF t g := by
        by_contra hc
        push Not at hc
        exact hEq (Finset.Subset.antisymm (spanF_subset hmem) hc)
      refine ih (t + 1) (Fin.cons u g) ?_ (indep_cons hind hus) ?_
      · intro i
        refine Fin.cases ?_ ?_ i
        · rw [Fin.cons_zero]; exact (mem_gset G).1 huG
        · intro j; rw [Fin.cons_succ]; exact hmem j
      · have hss : spanF t g ⊂ spanF (t + 1) (Fin.cons u g) :=
          (Finset.ssubset_iff_of_subset (spanF_subset_cons u g)).2
            ⟨u, mem_spanF_cons u g, hus⟩
        have := Finset.card_lt_card hss
        omega

theorem exists_spanning_tuple (G : Submodule (ZMod 2) (PS s)) [DecidablePred (· ∈ G)] :
    ∃ (t : ℕ) (g : Fin t → PS s), (∀ i, g i ∈ G) ∧ Indep t g ∧ spanF t g = gset G := by
  have hind0 : Indep 0 (Fin.elim0 : Fin 0 → PS s) := fun c _ => funext fun i => i.elim0
  refine exists_indep_span G (gset G).card 0 Fin.elim0 (fun i => i.elim0) hind0 ?_
  have h1 : (spanF 0 (Fin.elim0 : Fin 0 → PS s)).card = 1 := by
    rw [card_spanF hind0]; norm_num
  omega

/-- **THE BRIDGE.** An arbitrary Lagrangian subspace has an independent spanning tuple of length
exactly `s`, whose members pairwise commute. Everything the projector calculus needs about `G` is
produced here from `G` itself. -/
theorem exists_lagrangian_tuple (G : Submodule (ZMod 2) (PS s)) [DecidablePred (· ∈ G)]
    (hiso : Isotropic G) (hcard : (gset G).card = 2 ^ s) :
    ∃ g : Fin s → PS s, (∀ i, g i ∈ G) ∧ (∀ i j, omega (g i) (g j) = 0) ∧
      Indep s g ∧ spanF s g = gset G := by
  obtain ⟨t, g, hmem, hind, hspan⟩ := exists_spanning_tuple G
  have ht : t = s := by
    have h1 : (2 : ℕ) ^ t = 2 ^ s := by rw [← card_spanF hind, hspan, hcard]
    exact Nat.pow_right_injective (le_refl 2) h1
  subst ht
  exact ⟨g, hmem, fun i j => hiso _ (hmem i) _ (hmem j), hind, hspan⟩

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

/-! ### The dephasing identity

`Σ_χ P_χ ρ P_χ = Φ_G(ρ)`. Both sides are averages over `2^s` conjugations; the projector side runs
over characters and the twirl side over `G`, and the character orthogonality that turns one into the
other is the same one that made the projectors orthogonal. The tuple-dependence disappears here:
`lift_conj` says each conjugation forgets the lift's unit scalar, so a construction that had to pick
a basis reproduces an object that never did. -/

/-- Expanding a conjugation between two scalar-weighted sums. -/
theorem sum_conj_sum {ι κ : Type*} [Fintype ι] [Fintype κ]
    (a : ι → ℂ) (A : ι → Matrix (Q s) (Q s) ℂ) (b : κ → ℂ) (B : κ → Matrix (Q s) (Q s) ℂ)
    (ρ : Matrix (Q s) (Q s) ℂ) :
    (∑ i, a i • A i) * ρ * (∑ j, b j • B j)
      = ∑ i, ∑ j, (a i * b j) • (A i * ρ * B j) := by
  rw [Finset.sum_mul, Finset.sum_mul]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Matrix.smul_mul, Matrix.smul_mul, Finset.mul_sum, Finset.smul_sum]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [Matrix.mul_smul, smul_smul]

theorem coeff_add_eq_zero_iff {t : ℕ} (c c' : Fin t → ZMod 2) : c + c' = 0 ↔ c' = c := by
  constructor
  · intro h
    funext i
    have hi : c i + c' i = 0 := congrFun h i
    rcases zmod_two_cases (c i) with h1 | h1 <;> rcases zmod_two_cases (c' i) with h2 | h2 <;>
      rw [h1, h2] at hi ⊢ <;> first | rfl | (exfalso; revert hi; decide)
  · intro h
    subst h
    exact funext fun i => CharTwo.add_self_eq_zero _

/-- **The pinching by the character projectors is the average over the lifts.** -/
theorem sum_P_conj (t : ℕ) (g : Fin t → PS s) (ρ : Matrix (Q s) (Q s) ℂ) :
    (∑ e : Fin t → ZMod 2, P t g e * ρ * P t g e)
      = ((2 ^ t : ℕ) : ℂ)⁻¹ • ∑ c : Fin t → ZMod 2, lift t g c * ρ * lift t g c := by
  have hN := coeff_cast_ne_zero t
  have hstep : ∀ e : Fin t → ZMod 2, P t g e * ρ * P t g e
      = (((2 ^ t : ℕ) : ℂ)⁻¹ * ((2 ^ t : ℕ) : ℂ)⁻¹) •
        ∑ c : Fin t → ZMod 2, ∑ c' : Fin t → ZMod 2,
          (chi (dotF e c) * chi (dotF e c')) • (lift t g c * ρ * lift t g c') := by
    intro e
    rw [P, Matrix.smul_mul, Matrix.mul_smul, Matrix.smul_mul, smul_smul, sum_conj_sum]
  have hinner : ∀ c c' : Fin t → ZMod 2,
      (∑ e : Fin t → ZMod 2,
        (chi (dotF e c) * chi (dotF e c')) • (lift t g c * ρ * lift t g c'))
        = (if c' = c then ((2 ^ t : ℕ) : ℂ) else 0) • (lift t g c * ρ * lift t g c') := by
    intro c c'
    rw [← Finset.sum_smul]
    congr 1
    have h1 : ∀ e : Fin t → ZMod 2,
        chi (dotF e c) * chi (dotF e c') = chi (dotF (c + c') e) := by
      intro e
      rw [← chi_add, ← dotF_add_right, dotF_comm]
    rw [Finset.sum_congr rfl fun e (_ : e ∈ Finset.univ) => h1 e, sum_chi_dotF (s := t) (c + c')]
    by_cases hcc : c' = c
    · rw [if_pos hcc, if_pos ((coeff_add_eq_zero_iff c c').2 hcc)]
    · rw [if_neg hcc, if_neg fun hz => hcc ((coeff_add_eq_zero_iff c c').1 hz)]
  have hcol : ∀ c : Fin t → ZMod 2,
      (∑ c' : Fin t → ZMod 2,
        (if c' = c then ((2 ^ t : ℕ) : ℂ) else 0) • (lift t g c * ρ * lift t g c'))
        = ((2 ^ t : ℕ) : ℂ) • (lift t g c * ρ * lift t g c) := by
    intro c
    rw [Finset.sum_eq_single c]
    · rw [if_pos rfl]
    · intro b _ hb; rw [if_neg hb, zero_smul]
    · intro hc; exact absurd (Finset.mem_univ c) hc
  rw [Finset.sum_congr rfl fun e (_ : e ∈ Finset.univ) => hstep e, ← Finset.smul_sum,
    Finset.sum_comm,
    Finset.sum_congr rfl fun c (_ : c ∈ Finset.univ) => Finset.sum_comm,
    Finset.sum_congr rfl fun c (_ : c ∈ Finset.univ) =>
      Finset.sum_congr rfl fun c' (_ : c' ∈ Finset.univ) => hinner c c',
    Finset.sum_congr rfl fun c (_ : c ∈ Finset.univ) => hcol c, ← Finset.smul_sum, smul_smul]
  congr 1
  rw [mul_assoc, inv_mul_cancel₀ hN, mul_one]

/-- **`Σ_χ P_χ ρ P_χ = Φ_G(ρ)`.** The projectors are built from a tuple; the twirl is not; they
agree. -/
theorem sum_P_conj_eq_twirl (G : Submodule (ZMod 2) (PS s)) [DecidablePred (· ∈ G)]
    (g : Fin s → PS s) (hg : ∀ i j, omega (g i) (g j) = 0) (hind : Indep s g)
    (hspan : spanF s g = gset G) (ρ : Matrix (Q s) (Q s) ℂ) :
    (∑ e : Fin s → ZMod 2, P s g e * ρ * P s g e) = twirl G ρ := by
  have hcard : (gset G).card = 2 ^ s := by rw [← hspan, card_spanF hind]
  rw [sum_P_conj s g ρ,
    Finset.sum_congr rfl fun c (_ : c ∈ Finset.univ) => lift_conj s g hg c ρ,
    twirl, hcard]
  congr 1
  rw [← hspan, spanF, Finset.sum_image fun a _ b _ hab => vsum_injective hind hab]
  simp only [vsum]

/-! ### Rank one, used without choosing eigenvectors

The maximal case needs the joint eigenspaces to be lines, and `finrank_range_P` says they are. What
the Choi computation actually consumes is weaker and purely algebraic: a rank-one matrix factors
entrywise as `M a i = x a · y i`. Taking that as the interface avoids normalized eigenvectors, an
orthonormal basis, and any square root — nothing spectral is needed downstream. -/

/-- **Rank one is an entrywise factorization.** The columns of `M` all lie on the line that is its
range, so each is a scalar multiple of one fixed vector; the scalars are the second factor. -/
theorem exists_factor_of_finrank_range_eq_one {ι : Type*} [Fintype ι] [DecidableEq ι]
    (M : Matrix ι ι ℂ) (h : Module.finrank ℂ (LinearMap.range (Matrix.toLin' M)) = 1) :
    ∃ x y : ι → ℂ, ∀ a i, M a i = x a * y i := by
  have hne : LinearMap.range (Matrix.toLin' M) ≠ ⊥ := by
    intro hc
    rw [hc, finrank_bot] at h
    exact absurd h (by norm_num)
  obtain ⟨w, hwmem, hw0⟩ := Submodule.exists_mem_ne_zero_of_ne_bot hne
  have hspan : (ℂ ∙ w) = LinearMap.range (Matrix.toLin' M) := by
    refine Submodule.eq_of_le_of_finrank_le ?_ ?_
    · rwa [Submodule.span_singleton_le_iff_mem]
    · rw [h, finrank_span_singleton hw0]
  have hcol : ∀ i : ι, ∃ cc : ℂ, ∀ a, M a i = cc * w a := by
    intro i
    have hm : (Matrix.toLin' M) (Pi.single i 1) ∈ (ℂ ∙ w) := by
      rw [hspan]; exact LinearMap.mem_range_self _ _
    obtain ⟨cc, hcc⟩ := Submodule.mem_span_singleton.1 hm
    refine ⟨cc, fun a => ?_⟩
    have ha := congrFun hcc a
    simpa [Matrix.toLin'_apply, Matrix.mulVec_single] using ha.symm
  choose y hy using hcol
  exact ⟨w, y, fun a i => (hy i a).trans (mul_comm _ _)⟩

/-! ### The wrapper

The manuscript-facing statement of the maximal direction: an isotropic `G` of order `2^s` — no
tuple, no basis, no Clifford reduction in the hypotheses — has an entanglement-breaking twirl. -/

/-- **`G` isotropic and `|G| = 2^s` ⟹ `Φ_G` is entanglement breaking.** -/
theorem entanglementBreaking_twirl (G : Submodule (ZMod 2) (PS s)) [DecidablePred (· ∈ G)]
    (hiso : Isotropic G) (hcard : (gset G).card = 2 ^ s) :
    Separability.EntanglementBreaking (twirl G) := by
  obtain ⟨g, hmem, hg, hind, hspan⟩ := exists_lagrangian_tuple G hiso hcard
  have hfac : ∀ e : Fin s → ZMod 2, ∃ x y : Q s → ℂ, ∀ a i, P s g e a i = x a * y i := fun e =>
    exists_factor_of_finrank_range_eq_one _ (finrank_range_P g hg hind e)
  choose x y hxy using hfac
  have hchan : ∀ ρ, twirl G ρ = ∑ e : Fin s → ZMod 2, P s g e * ρ * (P s g e)ᴴ := by
    intro ρ
    rw [← sum_P_conj_eq_twirl G g hg hind hspan ρ]
    exact Finset.sum_congr rfl fun e _ => by rw [P_conjTranspose s g hg e]
  have hchoi : Separability.choi (twirl G)
      = ∑ e : Fin s → ZMod 2, Separability.prodProj (y e) (x e) := by
    rw [funext hchan, Separability.choi_sum]
    exact Finset.sum_congr rfl fun e _ =>
      Separability.choi_conj_of_factor (P s g e) (x e) (y e) (hxy e)
  exact Separability.separable_of_fintype y x hchoi

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
#print axioms lift_conj
#print axioms exists_lagrangian_tuple
#print axioms sum_P_conj
#print axioms sum_P_conj_eq_twirl
#print axioms exists_factor_of_finrank_range_eq_one
#print axioms finrank_range_P
#print axioms entanglementBreaking_twirl

end WeylLift

end OIBridge
