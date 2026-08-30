/-
  OIBridge/WeylTwirl.lean — the symplectic phase space, the Weyl operators, and the exact twirl.

      Φ_G (W v)  =  W v   if v ∈ G^⊥,      0 otherwise.

  LAYER 1 of [Main] Theorem (separability threshold). Everything here is exact finite algebra: no
  separability, no Choi matrix, no entanglement. What it delivers is the single identity the two
  halves of that theorem both run on — the twirl over an isotropic subspace is the Hilbert–Schmidt
  projection onto the Weyl operators commuting with it.

  G IS AN ISOTROPIC SUBSPACE, not a Pauli subgroup. The manuscript says "abelian subgroup of the
  Weyl group, of order 2^t modulo phases", and the phrase "modulo phases" is doing real work: the
  set `{X^a Z^b}` is NOT closed under multiplication — `(XZ)² = −1` — so "a subgroup of order 2^t"
  is not a statement about that set. The faithful object is the isotropic subspace of `𝔽₂^{2s}`,
  and taking it directly avoids a quotient that the theorem never uses. `isotropic_iff_commute`
  records that this is the same condition: a subspace is isotropic exactly when its Weyl operators
  pairwise commute.

  NO WITT, NO CLIFFORD. The printed proof reduces an arbitrary isotropic subspace to
  `⟨Z_1, …, Z_t⟩` by Witt's extension theorem and implements the symplectic map by a Clifford
  unitary. The twirl identity below makes that reduction unnecessary: both directions of the
  theorem can be read off `G` and `G^⊥` directly, for every isotropic subspace, without building
  the finite Clifford representation. That is a simplification of the route, not of the result.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.Data.ZMod.Basic
import Mathlib.Algebra.CharP.Two
import Mathlib.Data.Complex.Basic
import Mathlib.Analysis.RCLike.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Algebra.Order.BigOperators.Ring.Finset

namespace OIBridge

namespace WeylTwirl

set_option autoImplicit false

open Matrix Finset

variable {s : ℕ}

/-! ### The phase space

`Q s` is the computational basis, `𝔽₂^s`; `PS s = Q s × Q s` is the phase space `𝔽₂^{2s}`, whose
first component indexes translations (`X`) and second phases (`Z`). -/

/-- The computational basis index. -/
abbrev Q (s : ℕ) := Fin s → ZMod 2

/-- The phase space `𝔽₂^{2s}`. -/
abbrev PS (s : ℕ) := Q s × Q s

/-- The bilinear pairing on `𝔽₂^s`. -/
def dotF (a b : Q s) : ZMod 2 := ∑ i, a i * b i

theorem dotF_add_left (a b c : Q s) : dotF (a + b) c = dotF a c + dotF b c := by
  simp only [dotF, ← Finset.sum_add_distrib]
  exact Finset.sum_congr rfl fun i _ => by simp [add_mul]

theorem dotF_add_right (a b c : Q s) : dotF a (b + c) = dotF a b + dotF a c := by
  simp only [dotF, ← Finset.sum_add_distrib]
  exact Finset.sum_congr rfl fun i _ => by simp [mul_add]

theorem dotF_zero_left (a : Q s) : dotF 0 a = 0 := by simp [dotF]

theorem dotF_zero_right (a : Q s) : dotF a 0 = 0 := by simp [dotF]

/-- **The symplectic form on the phase space.** Two Weyl operators commute exactly when this
vanishes; the whole file turns on that. -/
def omega (u v : PS s) : ZMod 2 := dotF u.2 v.1 + dotF v.2 u.1

theorem omega_add_left (u v w : PS s) : omega (u + v) w = omega u w + omega v w := by
  simp only [omega, Prod.fst_add, Prod.snd_add, dotF_add_left, dotF_add_right]
  ring

theorem omega_add_right (u v w : PS s) : omega u (v + w) = omega u v + omega u w := by
  simp only [omega, Prod.fst_add, Prod.snd_add, dotF_add_left, dotF_add_right]
  ring

theorem omega_zero_left (v : PS s) : omega 0 v = 0 := by
  simp [omega, dotF_zero_left, dotF_zero_right]

theorem omega_comm (u v : PS s) : omega u v = omega v u := by
  simp only [omega]; ring

theorem omega_zero_right (u : PS s) : omega u 0 = 0 := by
  simp [omega, dotF_zero_left, dotF_zero_right]

theorem omega_self (u : PS s) : omega u u = 0 := by
  have h : omega u u = 2 * dotF u.2 u.1 := by simp only [omega]; ring
  rw [h, show (2 : ZMod 2) = 0 from rfl, zero_mul]

/-! ### The character

`chi` is the nontrivial character of `(ZMod 2, +)` in `ℂ`. Its only properties used below are that
it is multiplicative and real. -/

/-- The sign character. -/
def chi : ZMod 2 → ℂ := fun z => if z = 0 then 1 else -1

theorem zmod_two_cases (z : ZMod 2) : z = 0 ∨ z = 1 := by revert z; decide

@[simp] theorem chi_zero : chi (0 : ZMod 2) = 1 := rfl

theorem one_add_one : (1 : ZMod 2) + 1 = 0 := by decide

theorem chi_add (z z' : ZMod 2) : chi (z + z') = chi z * chi z' := by
  rcases zmod_two_cases z with rfl | rfl <;> rcases zmod_two_cases z' with rfl | rfl
  · norm_num [chi]
  · norm_num [chi]
  · norm_num [chi]
  · rw [one_add_one]; norm_num [chi]

theorem chi_conj (z : ZMod 2) : star (chi z) = chi z := by
  rcases zmod_two_cases z with rfl | rfl <;> simp [chi]

/-- Every phase-space vector is its own inverse; the two-torsion facts the file keeps needing. -/
theorem addQ_self (a : Q s) : a + a = 0 := funext fun _ => CharTwo.add_self_eq_zero _

theorem addPS_self (w : PS s) : w + w = 0 :=
  Prod.ext_iff.2 ⟨addQ_self w.1, addQ_self w.2⟩

theorem chi_mul_self (z : ZMod 2) : chi z * chi z = 1 := by
  rcases zmod_two_cases z with rfl | rfl <;> norm_num [chi]

theorem chi_eq_one_iff (z : ZMod 2) : chi z = 1 ↔ z = 0 := by
  rcases zmod_two_cases z with rfl | rfl <;> norm_num [chi]

theorem chi_ne_zero (z : ZMod 2) : chi z ≠ 0 := by
  rcases zmod_two_cases z with rfl | rfl <;> simp [chi]

/-! ### The Weyl operators

`W (a, b) = X^a Z^b`, acting as `|y⟩ ↦ (−1)^{b·y} |y + a⟩`. -/

/-- The Weyl operator `X^a Z^b`. -/
def W (u : PS s) : Matrix (Q s) (Q s) ℂ :=
  fun x y => if x = y + u.1 then chi (dotF u.2 y) else 0

@[simp] theorem W_apply (u : PS s) (x y : Q s) :
    W u x y = if x = y + u.1 then chi (dotF u.2 y) else 0 := rfl

@[simp] theorem W_zero : W (0 : PS s) = 1 := by
  refine Matrix.ext fun x y => ?_
  simp only [W_apply, Prod.fst_zero, Prod.snd_zero, add_zero, dotF_zero_left, chi_zero,
    Matrix.one_apply]

/-- **The Weyl product rule.** -/
theorem W_mul (u v : PS s) : W u * W v = chi (dotF u.2 v.1) • W (u + v) := by
  refine Matrix.ext fun x z => ?_
  rw [Matrix.mul_apply, Finset.sum_eq_single (z + v.1)]
  · have h2 : W v (z + v.1) z = chi (dotF v.2 z) := if_pos rfl
    rw [h2]
    show (if x = (z + v.1) + u.1 then chi (dotF u.2 (z + v.1)) else 0) * chi (dotF v.2 z)
        = chi (dotF u.2 v.1) * (if x = z + (u + v).1 then chi (dotF (u + v).2 z) else 0)
    have hxeq : (z + v.1) + u.1 = z + (u + v).1 := by
      simp only [Prod.fst_add]; abel
    rw [hxeq]
    by_cases h : x = z + (u + v).1
    · rw [if_pos h, if_pos h, dotF_add_right]
      show chi (dotF u.2 z + dotF u.2 v.1) * chi (dotF v.2 z)
          = chi (dotF u.2 v.1) * chi (dotF (u.2 + v.2) z)
      rw [dotF_add_left, chi_add, chi_add]
      ring
    · rw [if_neg h, if_neg h]; ring
  · intro y _ hy
    have h0 : W v y z = 0 := if_neg hy
    rw [h0, mul_zero]
  · intro hc
    exact absurd (Finset.mem_univ _) hc

/-- The adjoint of a Weyl operator is itself, up to a sign. -/
theorem W_conjTranspose (u : PS s) : (W u)ᴴ = chi (dotF u.2 u.1) • W u := by
  refine Matrix.ext fun x y => ?_
  simp only [Matrix.conjTranspose_apply, W_apply, Matrix.smul_apply, smul_eq_mul]
  by_cases h : x = y + u.1
  · have h' : y = x + u.1 := by rw [h, add_assoc, addQ_self u.1, add_zero]
    rw [if_pos h', if_pos h, chi_conj, h', dotF_add_right, chi_add]
    have hB := chi_mul_self (dotF u.2 u.1)
    calc chi (dotF u.2 x)
        = chi (dotF u.2 x) * (chi (dotF u.2 u.1) * chi (dotF u.2 u.1)) := by rw [hB, mul_one]
      _ = chi (dotF u.2 u.1) * (chi (dotF u.2 x) * chi (dotF u.2 u.1)) := by ring
  · have h' : ¬ y = x + u.1 := by
      intro hc; exact h (by rw [hc, add_assoc, addQ_self u.1, add_zero])
    rw [if_neg h', if_neg h, star_zero, mul_zero]

/-- **Conjugation is the symplectic character.** This is the identity the whole theorem rests on:
conjugating one Weyl operator by another multiplies it by `(−1)^{ω(u,v)}`. -/
theorem W_conj (u v : PS s) : W u * W v * (W u)ᴴ = chi (omega u v) • W v := by
  have hidx : u + v + u = v := by
    rw [show u + v + u = (u + u) + v from by abel, addPS_self, zero_add]
  rw [W_conjTranspose, mul_smul_comm, W_mul, smul_mul_assoc, W_mul, hidx, smul_smul, smul_smul]
  congr 1
  simp only [Prod.snd_add, omega]
  rw [dotF_add_left, chi_add, chi_add]
  linear_combination (chi (dotF u.2 v.1) * chi (dotF v.2 u.1)) * chi_mul_self (dotF u.2 u.1)

/-- A Weyl operator has a `1` entry, so it is never zero. -/
theorem W_entry_one (u : PS s) : W u u.1 0 = 1 := by
  simp [W, dotF_zero_right]

/-- **Weyl operators commute exactly on the symplectic form.** This is the manuscript's "abelian",
turned into isotropy. -/
theorem W_commute_iff (u v : PS s) : W u * W v = W v * W u ↔ omega u v = 0 := by
  constructor
  · intro h
    have h1 : chi (dotF u.2 v.1) • W (u + v) = chi (dotF v.2 u.1) • W (u + v) := by
      have e1 : W u * W v = chi (dotF u.2 v.1) • W (u + v) := W_mul u v
      have e2 : W v * W u = chi (dotF v.2 u.1) • W (v + u) := W_mul v u
      rw [← e1, h, e2, add_comm v u]
    have h2 := congrArg (fun M : Matrix (Q s) (Q s) ℂ => M (u + v).1 0) h1
    simp only [Matrix.smul_apply, smul_eq_mul, W_entry_one, mul_one] at h2
    have h3 : chi (dotF u.2 v.1 + dotF v.2 u.1) = 1 := by
      rw [chi_add, ← h2, chi_mul_self]
    exact (chi_eq_one_iff _).1 h3
  · intro h
    have hh := h
    rw [omega] at hh
    have h1 : dotF u.2 v.1 = dotF v.2 u.1 := by
      rcases zmod_two_cases (dotF u.2 v.1) with ha | ha <;>
        rcases zmod_two_cases (dotF v.2 u.1) with hb | hb <;>
        rw [ha, hb] at hh ⊢ <;> first | rfl | (exfalso; revert hh; decide)
    rw [W_mul, W_mul, h1, add_comm v u]

/-! ### Isotropic subspaces and their symplectic complements -/

variable (G : Submodule (ZMod 2) (PS s))

/-- **Isotropy**: the manuscript's "abelian", stated on the phase space. -/
def Isotropic : Prop := ∀ u ∈ G, ∀ v ∈ G, omega u v = 0

/-- The symplectic complement. -/
def perp : Submodule (ZMod 2) (PS s) where
  carrier := {v | ∀ u ∈ G, omega u v = 0}
  add_mem' {v w} hv hw := fun u hu => by rw [omega_add_right, hv u hu, hw u hu, add_zero]
  zero_mem' := fun u _ => omega_zero_right u
  smul_mem' c v hv := fun u hu => by
    rcases zmod_two_cases c with rfl | rfl
    · rw [zero_smul]; exact omega_zero_right u
    · simpa using hv u hu

@[simp] theorem mem_perp {v : PS s} : v ∈ perp G ↔ ∀ u ∈ G, omega u v = 0 := Iff.rfl

/-- Isotropy says exactly that `G ≤ G^⊥`. -/
theorem isotropic_iff_le_perp : Isotropic G ↔ G ≤ perp G :=
  ⟨fun h _ hv _ hu => h _ hu _ hv, fun h u hu _ hv => h hv u hu⟩

/-- **Isotropy is commutation of the Weyl operators**, which is the manuscript's own phrasing. -/
theorem isotropic_iff_commute :
    Isotropic G ↔ ∀ u ∈ G, ∀ v ∈ G, W u * W v = W v * W u :=
  ⟨fun h u hu v hv => (W_commute_iff u v).2 (h u hu v hv),
   fun h u hu v hv => (W_commute_iff u v).1 (h u hu v hv)⟩

/-! ### The twirl

The uniform mixture over `G`. Isotropy is not needed for the identity below — only that `G` is a
subgroup — which is worth keeping visible: what isotropy buys is used later, not here. -/

variable [DecidablePred (· ∈ G)]

/-- `G` as a `Finset`. -/
def gset : Finset (PS s) := Finset.univ.filter (· ∈ G)

@[simp] theorem mem_gset {v : PS s} : v ∈ gset G ↔ v ∈ G := by simp [gset]

/-- Membership in the symplectic complement is decidable: it is a finite conjunction. -/
instance decPerp : DecidablePred (· ∈ perp G) := fun v =>
  decidable_of_iff (∀ u ∈ gset G, omega u v = 0) (by simp [mem_gset])

theorem gset_card_pos : 0 < (gset G).card :=
  Finset.card_pos.2 ⟨0, (mem_gset G).2 G.zero_mem⟩

/-- **The character sum over a subgroup.** The standard orthogonality argument: the map
`g ↦ (−1)^{ω(g,v)}` is a character of `G`, so it sums to `|G|` if trivial and to `0` otherwise. -/
theorem char_sum (v : PS s) :
    (∑ g ∈ gset G, chi (omega g v)) = if v ∈ perp G then ((gset G).card : ℂ) else 0 := by
  by_cases hv : v ∈ perp G
  · rw [if_pos hv]
    rw [Finset.sum_congr rfl fun g hg => by
      rw [hv g ((mem_gset G).1 hg), chi_zero]]
    simp
  · rw [if_neg hv]
    simp only [mem_perp, not_forall] at hv
    obtain ⟨g₀, hg₀, hne⟩ := hv
    set S := ∑ g ∈ gset G, chi (omega g v) with hS
    have hbij : (gset G).image (fun g => g₀ + g) = gset G := by
      refine Finset.eq_of_subset_of_card_le ?_ ?_
      · intro x hx
        obtain ⟨g, hg, rfl⟩ := Finset.mem_image.1 hx
        exact (mem_gset G).2 (G.add_mem hg₀ ((mem_gset G).1 hg))
      · rw [Finset.card_image_of_injective _ (add_right_injective g₀)]
    have hshift : S = chi (omega g₀ v) * S := by
      conv_lhs => rw [hS, ← hbij]
      rw [Finset.sum_image fun a _ b _ hab => add_right_injective g₀ hab]
      rw [hS, Finset.mul_sum]
      exact Finset.sum_congr rfl fun g _ => by rw [omega_add_left, chi_add]
    have hval : chi (omega g₀ v) = -1 := by
      rcases zmod_two_cases (omega g₀ v) with h0 | h1
      · exact absurd h0 hne
      · rw [h1]; simp [chi]
    rw [hval] at hshift
    linear_combination (1 / 2 : ℂ) * hshift

/-- **The twirl.** -/
noncomputable def twirl (ρ : Matrix (Q s) (Q s) ℂ) : Matrix (Q s) (Q s) ℂ :=
  (((gset G).card : ℂ))⁻¹ • ∑ g ∈ gset G, W g * ρ * (W g)ᴴ

/-- **THE TWIRL IDENTITY.** `Φ_G` fixes the Weyl operators commuting with `G` and kills the rest —
the Hilbert–Schmidt projection onto `G^⊥`. Both halves of the separability theorem read off this. -/
theorem twirl_W (v : PS s) : twirl G (W v) = if v ∈ perp G then W v else 0 := by
  have hcard : ((gset G).card : ℂ) ≠ 0 := Nat.cast_ne_zero.2 (gset_card_pos G).ne'
  rw [twirl]
  rw [Finset.sum_congr rfl fun g _ => W_conj g v]
  rw [← Finset.sum_smul, char_sum]
  by_cases hv : v ∈ perp G
  · rw [if_pos hv, if_pos hv, smul_smul, inv_mul_cancel₀ hcard, one_smul]
  · rw [if_neg hv, if_neg hv, zero_smul, smul_zero]

/-! ### The self-adjoint normalization

`W` keeps its clean real-sign convention above — `(W u)ᴴ = (−1)^{b·a} W u`, which is what makes
the twirl a real-signed average. The maximal-isotropic direction, though, wants genuine self-adjoint
involutions to diagonalize, so the phase is normalized away HERE and only here:

    H u = i^{b·a} · W u,   Hᴴ = H,   H² = 1,   and ω(u,v) = 0 ⟹ H u and H v commute.

Nothing above changes; `H` is a separate interface for the diagonalization layer. -/

/-- `i^z` for `z` in `ZMod 2`. -/
noncomputable def iPow : ZMod 2 → ℂ := fun z => if z = 0 then 1 else Complex.I

/-- **The self-adjoint Weyl operator.** -/
noncomputable def H (u : PS s) : Matrix (Q s) (Q s) ℂ := iPow (dotF u.2 u.1) • W u

/-- **`H u` is self-adjoint.** -/
theorem H_conjTranspose (u : PS s) : (H u)ᴴ = H u := by
  rw [H, Matrix.conjTranspose_smul, W_conjTranspose, smul_smul]
  congr 1
  rcases zmod_two_cases (dotF u.2 u.1) with h | h <;> rw [h] <;> simp [iPow, chi]

/-- **`H u` is an involution.** -/
theorem H_mul_self (u : PS s) : H u * H u = 1 := by
  rw [H, Matrix.smul_mul, Matrix.mul_smul, W_mul, smul_smul, smul_smul, addPS_self, W_zero]
  rw [show iPow (dotF u.2 u.1) * iPow (dotF u.2 u.1) * chi (dotF u.2 u.1) = 1 from ?_, one_smul]
  rcases zmod_two_cases (dotF u.2 u.1) with h | h <;> rw [h] <;> simp [iPow, chi]

/-- **Commuting `W` gives commuting `H`**, so an isotropic subspace supplies a commuting family of
self-adjoint involutions — the input the joint-eigenspace decomposition wants. -/
theorem H_commute (u v : PS s) (h : omega u v = 0) : H u * H v = H v * H u := by
  rw [H, H, Matrix.smul_mul, Matrix.mul_smul, Matrix.smul_mul, Matrix.mul_smul,
    (W_commute_iff u v).2 h, smul_smul, smul_smul, mul_comm]

/-! ### What these proofs rest on -/

#print axioms W_mul
#print axioms W_conjTranspose
#print axioms W_conj
#print axioms W_commute_iff
#print axioms isotropic_iff_commute
#print axioms char_sum
#print axioms twirl_W
#print axioms H_conjTranspose
#print axioms H_mul_self
#print axioms H_commute

end WeylTwirl

end OIBridge
