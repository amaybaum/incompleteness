/-!
OIBridge/ChiralCenterRecovery.lean — restricted recovery of SM Theorem 3.

This self-contained module proves the complete entrywise grading criterion,
arbitrary even-operator and site-dependent onsite perturbation criteria, and
uniform coefficient uniqueness when both parity sectors occur. No imports,
Mathlib build, physical-spin identification, or second-order/first-order
identification is used. Rng is scoped here so the existing plain-core identities
remain untouched. Kernel check: lean OIBridge/ChiralCenterRecovery.lean.
-/

universe u v

namespace OIBridge.ChiralCenterRecovery

class Rng (R : Type u) extends Add R, Mul R, Neg R where
  zero : R
  one : R
  add_assoc : ∀ a b c : R, a + b + c = a + (b + c)
  add_comm : ∀ a b : R, a + b = b + a
  zero_add : ∀ a : R, zero + a = a
  neg_add_cancel : ∀ a : R, -a + a = zero
  mul_assoc : ∀ a b c : R, a * b * c = a * (b * c)
  one_mul : ∀ a : R, one * a = a
  mul_one : ∀ a : R, a * one = a
  left_distrib : ∀ a b c : R, a * (b + c) = a * b + a * c
  right_distrib : ∀ a b c : R, (a + b) * c = a * c + b * c

namespace Rng

variable {R : Type u} [Rng R]

theorem add_zero (a : R) : a + zero = a := by
  rw [add_comm a zero, zero_add]

theorem add_neg_cancel (a : R) : a + -a = zero := by
  rw [add_comm a (-a), neg_add_cancel]

theorem add_left_cancel {a x y : R} (h : a + x = a + y) : x = y :=
  calc x = zero + x := (zero_add _).symm
    _ = (-a + a) + x := by rw [← neg_add_cancel a]
    _ = -a + (a + x) := add_assoc _ _ _
    _ = -a + (a + y) := by rw [h]
    _ = (-a + a) + y := (add_assoc _ _ _).symm
    _ = zero + y := by rw [neg_add_cancel a]
    _ = y := zero_add _

theorem eq_neg_of_add_eq_zero {x a : R} (hxa : x + a = zero) : x = -a :=
  calc x = x + zero := (add_zero _).symm
    _ = x + (a + -a) := by rw [← add_neg_cancel a]
    _ = (x + a) + -a := (add_assoc _ _ _).symm
    _ = zero + -a := by rw [hxa]
    _ = -a := zero_add _

theorem neg_neg (a : R) : -(-a) = a :=
  (eq_neg_of_add_eq_zero (add_neg_cancel a)).symm

theorem add_left_comm (a b c : R) : a + (b + c) = b + (a + c) := by
  rw [← add_assoc a b c, add_comm a b, add_assoc b a c]

theorem add_add_add_comm (u v w s : R) : (u + v) + (w + s) = (u + w) + (v + s) := by
  rw [add_assoc u v (w + s), add_left_comm v w s, ← add_assoc u w (v + s)]

theorem mul_zero (a : R) : a * zero = zero := by
  have h : a * zero + a * zero = a * zero + zero := by
    rw [← left_distrib, zero_add, add_zero]
  exact add_left_cancel h

theorem zero_mul (a : R) : zero * a = zero := by
  have h : zero * a + zero * a = zero * a + zero := by
    rw [← right_distrib, zero_add, add_zero]
  exact add_left_cancel h

theorem neg_mul (a b : R) : (-a) * b = -(a * b) := by
  apply eq_neg_of_add_eq_zero
  rw [← right_distrib, neg_add_cancel, zero_mul]

theorem mul_neg (a b : R) : a * (-b) = -(a * b) := by
  apply eq_neg_of_add_eq_zero
  rw [← left_distrib, neg_add_cancel, mul_zero]


end Rng

open Rng

variable {R : Type u} [Rng R]

/-- This is the load-bearing characteristic restriction, not a chiral hypothesis. -/
def NoTwoTorsion : Prop :=
  ∀ x : R, x + x = Rng.zero → x = Rng.zero

theorem recovery_neg_zero : -(Rng.zero : R) = Rng.zero := by
  have h := neg_add_cancel (Rng.zero : R)
  rw [add_zero] at h
  exact h

/-- Adding an ε-even operator to fixed ε-odd hopping exposes exactly twice its
right-parity product. No involution or characteristic hypothesis is used yet. -/
theorem even_perturbation_anticommutator (D C e : R)
    (hD : D * e = -(e * D)) (hC : C * e = e * C) :
    (D + C) * e + e * (D + C) = C * e + C * e :=
  calc
    (D + C) * e + e * (D + C)
        = (D * e + C * e) + (e * D + e * C) := by
          rw [right_distrib, left_distrib]
    _ = (D * e + e * D) + (C * e + e * C) :=
          add_add_add_comm _ _ _ _
    _ = Rng.zero + (C * e + C * e) := by
          rw [hD, neg_add_cancel, ← hC]
    _ = C * e + C * e := zero_add _

/-- The recovered restricted biconditional. C is any ε-even perturbation,
not necessarily an onsite term. Involution and no 2-torsion recover C itself. -/
theorem even_perturbation_iff (D C e : R)
    (he : e * e = Rng.one)
    (hD : D * e = -(e * D)) (hC : C * e = e * C)
    (h2 : NoTwoTorsion (R := R)) :
    ((D + C) * e + e * (D + C) = Rng.zero) ↔ C = Rng.zero := by
  constructor
  · intro h
    have ht : C * e + C * e = Rng.zero :=
      (even_perturbation_anticommutator D C e hD hC).symm.trans h
    have hz : C * e = Rng.zero := h2 (C * e) ht
    calc
      C = C * Rng.one := (mul_one C).symm
      _ = C * (e * e) := by rw [he]
      _ = (C * e) * e := (mul_assoc _ _ _).symm
      _ = Rng.zero := by rw [hz, zero_mul]
  · intro h
    rw [h, add_zero, hD, neg_add_cancel]

/-- Scalar parity sign. Both signs will be required for coefficient uniqueness. -/
def paritySign (b : Bool) : R :=
  if b then Rng.one else -Rng.one

/-- Entry form of {A,diag(ε)} = 0. This applies to arbitrary kernels, not only NN hopping. -/
def ChiralEntries {X : Type v} (parity : X → Bool) (A : X → X → R) : Prop :=
  ∀ i j, A i j * paritySign (parity j) +
    paritySign (parity i) * A i j = Rng.zero

/-- Exactly the entries connecting equal-parity sectors vanish. -/
def OddSupported {X : Type v} (parity : X → Bool) (A : X → X → R) : Prop :=
  ∀ i j, parity i = parity j → A i j = Rng.zero

/-- Complete entry-level classification: chirality is equivalent to opposite-parity support.
Finiteness is unnecessary because the diagonal parity actions involve no infinite sum. -/
theorem chiral_entries_iff_odd_support {X : Type v}
    (parity : X → Bool) (A : X → X → R)
    (h2 : NoTwoTorsion (R := R)) :
    ChiralEntries parity A ↔ OddSupported parity A := by
  constructor
  · intro h i j hij
    cases hi : parity i with
    | false =>
        have hj : parity j = false := hij.symm.trans hi
        have hz : (-A i j) + (-A i j) = Rng.zero := by
          simpa [paritySign, hi, hj, mul_neg, mul_one, neg_mul, one_mul] using h i j
        have hn : -A i j = Rng.zero := h2 (-A i j) hz
        calc
          A i j = -(-A i j) := (neg_neg _).symm
          _ = -(Rng.zero : R) := by rw [hn]
          _ = Rng.zero := recovery_neg_zero
    | true =>
        have hj : parity j = true := hij.symm.trans hi
        have hz : A i j + A i j = Rng.zero := by
          simpa [paritySign, hi, hj, mul_one, one_mul] using h i j
        exact h2 (A i j) hz
  · intro h i j
    cases hi : parity i <;> cases hj : parity j
    · have hz : A i j = Rng.zero := h i j (hi.trans hj.symm)
      simp [hz, zero_mul, mul_zero, zero_add]
    · simp [paritySign, mul_one, neg_mul, one_mul, add_neg_cancel]
    · simp [paritySign, mul_neg, mul_one, one_mul, neg_add_cancel]
    · have hz : A i j = Rng.zero := h i j (hi.trans hj.symm)
      simp [hz, zero_mul, mul_zero, zero_add]

/-- A uniform mass-parity/identity coefficient pair is identifiable when both
parity sectors occur. This is not assumed as linear independence; it is proved. -/
theorem scalar_center_zero_iff {X : Type v}
    (parity : X → Bool)
    (hpos : ∃ i, parity i = true) (hneg : ∃ i, parity i = false)
    (h2 : NoTwoTorsion (R := R)) (m p : R) :
    (∀ i, m * paritySign (parity i) + p = Rng.zero) ↔
      m = Rng.zero ∧ p = Rng.zero := by
  constructor
  · intro h
    obtain ⟨ip, hip⟩ := hpos
    obtain ⟨im, him⟩ := hneg
    have hp : m + p = Rng.zero := by
      simpa [paritySign, hip, mul_one] using h ip
    have hm : -m + p = Rng.zero := by
      simpa [paritySign, him, mul_neg, mul_one] using h im
    have hpm : p = m := by
      have h' : p + -m = Rng.zero := by rw [add_comm]; exact hm
      have h'' := eq_neg_of_add_eq_zero h'
      rw [neg_neg] at h''
      exact h''
    have hdouble : m + m = Rng.zero := by
      rw [hpm] at hp
      exact hp
    have hm0 : m = Rng.zero := h2 m hdouble
    exact ⟨hm0, hpm.trans hm0⟩
  · intro h i
    rw [h.1, h.2, zero_mul, zero_add]

/-- Add actual onsite diagonal coefficients to a fixed hopping kernel. -/
def addScalarCenter {X : Type v} [DecidableEq X]
    (parity : X → Bool) (D : X → X → R) (m p : R) : X → X → R :=
  fun i j => D i j + if i = j then m * paritySign (parity i) + p else Rng.zero

/-- Main restricted Theorem-3 candidate: fixed opposite-parity hopping plus the
two uniform onsite coefficients. Both directions and coefficient uniqueness are proved. -/
theorem scalar_center_chiral_iff {X : Type v} [DecidableEq X]
    (parity : X → Bool) (D : X → X → R)
    (hD : OddSupported parity D)
    (hpos : ∃ i, parity i = true) (hneg : ∃ i, parity i = false)
    (h2 : NoTwoTorsion (R := R)) (m p : R) :
    ChiralEntries parity (addScalarCenter parity D m p) ↔
      m = Rng.zero ∧ p = Rng.zero := by
  constructor
  · intro h
    have hodd := (chiral_entries_iff_odd_support parity
      (addScalarCenter parity D m p) h2).mp h
    have hc : ∀ i, m * paritySign (parity i) + p = Rng.zero := by
      intro i
      have hd : D i i = Rng.zero := hD i i rfl
      have hz := hodd i i rfl
      simpa [addScalarCenter, hd, zero_add] using hz
    exact (scalar_center_zero_iff parity hpos hneg h2 m p).mp hc
  · intro h
    apply (chiral_entries_iff_odd_support parity
      (addScalarCenter parity D m p) h2).mpr
    intro i j hij
    have hd : D i j = Rng.zero := hD i j hij
    simp [addScalarCenter, h.1, h.2, hd, zero_mul, zero_add]

/-- Add a genuinely onsite, site-dependent coefficient to fixed hopping. -/
def addOnsite {X : Type v} [DecidableEq X]
    (D : X → X → R) (c : X → R) : X → X → R :=
  fun i j => D i j + if i = j then c i else Rng.zero

/-- All onsite perturbations are classified, without uniformity or the presence
of both parity sectors. This is stronger than the uniform coefficient corollary. -/
theorem onsite_chiral_iff {X : Type v} [DecidableEq X]
    (parity : X → Bool) (D : X → X → R) (c : X → R)
    (hD : OddSupported parity D) (h2 : NoTwoTorsion (R := R)) :
    ChiralEntries parity (addOnsite D c) ↔ ∀ i, c i = Rng.zero := by
  constructor
  · intro h i
    have ho := (chiral_entries_iff_odd_support parity (addOnsite D c) h2).mp h
    have hz := ho i i rfl
    have hd : D i i = Rng.zero := hD i i rfl
    simpa [addOnsite, hd, zero_add] using hz
  · intro hc
    apply (chiral_entries_iff_odd_support parity (addOnsite D c) h2).mpr
    intro i j hij
    have hd : D i j = Rng.zero := hD i j hij
    simp [addOnsite, hd, hc i, zero_add]

theorem onsite_zero_of_chiral {X : Type v} [DecidableEq X]
    (parity : X → Bool) (D : X → X → R) (c : X → R)
    (hD : OddSupported parity D) (h2 : NoTwoTorsion (R := R))
    (h : ChiralEntries parity (addOnsite D c)) : ∀ i, c i = Rng.zero :=
  (onsite_chiral_iff parity D c hD h2).mp h

theorem onsite_chiral_of_zero {X : Type v} [DecidableEq X]
    (parity : X → Bool) (D : X → X → R) (c : X → R)
    (hD : OddSupported parity D) (h2 : NoTwoTorsion (R := R))
    (h : ∀ i, c i = Rng.zero) : ChiralEntries parity (addOnsite D c) :=
  (onsite_chiral_iff parity D c hD h2).mpr h

/- Directional witnesses for manuscript biconditionals (AGENTS A.34). -/
theorem even_perturbation_zero_of_chiral (D C e : R)
    (he : e * e = Rng.one)
    (hD : D * e = -(e * D)) (hC : C * e = e * C)
    (h2 : NoTwoTorsion (R := R))
    (h : (D + C) * e + e * (D + C) = Rng.zero) : C = Rng.zero :=
  (even_perturbation_iff D C e he hD hC h2).mp h

theorem chiral_of_even_perturbation_zero (D C e : R)
    (hD : D * e = -(e * D)) (hC : C = Rng.zero) :
    (D + C) * e + e * (D + C) = Rng.zero := by
  rw [hC, add_zero, hD, neg_add_cancel]

theorem odd_supported_of_chiral_entries {X : Type v}
    (parity : X → Bool) (A : X → X → R)
    (h2 : NoTwoTorsion (R := R)) (h : ChiralEntries parity A) :
    OddSupported parity A :=
  (chiral_entries_iff_odd_support parity A h2).mp h

theorem chiral_entries_of_odd_supported {X : Type v}
    (parity : X → Bool) (A : X → X → R)
    (h2 : NoTwoTorsion (R := R)) (h : OddSupported parity A) :
    ChiralEntries parity A :=
  (chiral_entries_iff_odd_support parity A h2).mpr h

theorem scalar_center_coefficients_zero_of_chiral {X : Type v} [DecidableEq X]
    (parity : X → Bool) (D : X → X → R)
    (hD : OddSupported parity D)
    (hpos : ∃ i, parity i = true) (hneg : ∃ i, parity i = false)
    (h2 : NoTwoTorsion (R := R)) (m p : R)
    (h : ChiralEntries parity (addScalarCenter parity D m p)) :
    m = Rng.zero ∧ p = Rng.zero :=
  (scalar_center_chiral_iff parity D hD hpos hneg h2 m p).mp h

theorem scalar_center_chiral_of_coefficients_zero {X : Type v} [DecidableEq X]
    (parity : X → Bool) (D : X → X → R)
    (hD : OddSupported parity D)
    (hpos : ∃ i, parity i = true) (hneg : ∃ i, parity i = false)
    (h2 : NoTwoTorsion (R := R)) (m p : R)
    (h : m = Rng.zero ∧ p = Rng.zero) :
    ChiralEntries parity (addScalarCenter parity D m p) :=
  (scalar_center_chiral_iff parity D hD hpos hneg h2 m p).mpr h

end OIBridge.ChiralCenterRecovery
