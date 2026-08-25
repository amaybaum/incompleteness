/-
OI_Staggered_Relations.lean — the staggered generator relations imply the factorization.

This file closes the gap left open in OI_Structural_Core.lean, where the Susskind
factorization was proved from anticommutation and square HYPOTHESES. Here those hypotheses
are DERIVED from the generator relations themselves — eta involutions, commuting shifts,
and the phase pattern in which eta_mu anticommutes with the shifts of strictly earlier axes
and commutes with those of later axes — and the factorization is then concluded for three
and four axes with no remaining obligations.

Self-contained: no imports; checks with plain `lean OI_Staggered_Relations.lean`. The ring
preamble and cancellation kit are shared verbatim with OI_Structural_Core.lean; keeping the
files independently checkable is the price of the zero-dependency discipline, and the two
copies collapse into one once the Mathlib bridge (ROADMAP.md section A) lands.

Axes are indexed by natural numbers, so the same structure serves any dimension; the
concrete d = 3 and d = 4 lattice operators satisfy every field of `Gens` exactly in integer
arithmetic (companion: staggered_relations_probe.py, S1).
-/

universe u

/-! ## Part 0: minimal ring -/

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

theorem eq_neg_symm {a b : R} (h : a = -b) : b = -a := by
  rw [h, neg_neg]

theorem neg_add (a b : R) : -(a + b) = -a + -b := by
  have key : (-a + -b) + (a + b) = zero :=
    calc (-a + -b) + (a + b) = -a + (-b + (a + b)) := add_assoc _ _ _
      _ = -a + (-b + (b + a)) := by rw [add_comm a b]
      _ = -a + ((-b + b) + a) := by rw [← add_assoc (-b) b a]
      _ = -a + (zero + a) := by rw [neg_add_cancel b]
      _ = -a + a := by rw [zero_add a]
      _ = zero := neg_add_cancel _
  exact (eq_neg_of_add_eq_zero key).symm

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

/-! ## Part 1: the generator relations -/

namespace Staggered

open Rng

variable {R : Type u} [Rng R]

/-- The staggered generator data on an arbitrary set of axes indexed by `Nat`:
`e i` are the phase involutions, `t i` the shifts, `s i` their inverses. -/
structure Gens (R : Type u) [Rng R] where
  e : Nat → R
  t : Nat → R
  s : Nat → R
  he : ∀ i, e i * e i = Rng.one
  hee : ∀ i j, e i * e j = e j * e i
  het : ∀ i, e i * t i = t i * e i
  hes : ∀ i, e i * s i = s i * e i
  hlt_t : ∀ i j, j < i → e i * t j = -(t j * e i)
  hlt_s : ∀ i j, j < i → e i * s j = -(s j * e i)
  hgt_t : ∀ i j, i < j → e i * t j = t j * e i
  hgt_s : ∀ i j, i < j → e i * s j = s j * e i
  htt : ∀ i j, i ≠ j → t i * t j = t j * t i
  hts : ∀ i j, i ≠ j → t i * s j = s j * t i
  hst : ∀ i j, i ≠ j → s i * t j = t j * s i
  hss : ∀ i j, i ≠ j → s i * s j = s j * s i

variable (g : Gens R)

/-- The shift difference `T_i - T_i⁻¹`. -/
def S (i : Nat) : R := g.t i + -(g.s i)

/-- The staggered summand `η_i (T_i - T_i⁻¹)`. -/
def A (i : Nat) : R := g.e i * S g i

/-! ### helpers: transporting a relation across the difference -/

/-- Commuting with both parts gives commuting with the difference. -/
theorem comm_diff {x a b : R} (ha : x * a = a * x) (hb : x * b = b * x) :
    x * (a + -b) = (a + -b) * x := by
  rw [left_distrib, right_distrib, ha, mul_neg, hb, ← neg_mul]

/-- Anticommuting with both parts gives anticommuting with the difference. -/
theorem anti_diff {x a b : R} (ha : x * a = -(a * x)) (hb : x * b = -(b * x)) :
    x * (a + -b) = -((a + -b) * x) := by
  rw [left_distrib, right_distrib, ha, mul_neg, hb, neg_mul, neg_neg, neg_add, neg_neg]

/-- Commuting on the left of both parts gives commuting with the difference. -/
theorem diff_comm {x a b : R} (ha : a * x = x * a) (hb : b * x = x * b) :
    (a + -b) * x = x * (a + -b) := (comm_diff ha.symm hb.symm).symm

/-! ### the derived relations -/

/-- `η_i` commutes with its own difference. -/
theorem e_comm_self (i : Nat) : g.e i * S g i = S g i * g.e i :=
  comm_diff (g.het i) (g.hes i)

/-- `η_i` commutes with the difference of a LATER axis. -/
theorem e_comm_gt {i j : Nat} (h : i < j) : g.e i * S g j = S g j * g.e i :=
  comm_diff (g.hgt_t i j h) (g.hgt_s i j h)

/-- `η_i` anticommutes with the difference of an EARLIER axis. -/
theorem e_anti_lt {i j : Nat} (h : j < i) : g.e i * S g j = -(S g j * g.e i) :=
  anti_diff (g.hlt_t i j h) (g.hlt_s i j h)

/-- Differences on distinct axes commute. -/
theorem S_comm {i j : Nat} (h : i ≠ j) : S g i * S g j = S g j * S g i := by
  have ht : g.t i * S g j = S g j * g.t i := comm_diff (g.htt i j h) (g.hts i j h)
  have hs : g.s i * S g j = S g j * g.s i := comm_diff (g.hst i j h) (g.hss i j h)
  exact diff_comm ht hs

/-- **Squares.** `A_i² = S_i²` — the first hypothesis of the factorization, discharged. -/
theorem A_sq (i : Nat) : A g i * A g i = S g i * S g i :=
  calc A g i * A g i = (g.e i * S g i) * (g.e i * S g i) := rfl
    _ = g.e i * (S g i * (g.e i * S g i)) := mul_assoc _ _ _
    _ = g.e i * ((S g i * g.e i) * S g i) := by rw [← mul_assoc (S g i) (g.e i) (S g i)]
    _ = g.e i * ((g.e i * S g i) * S g i) := by rw [← e_comm_self g i]
    _ = g.e i * (g.e i * (S g i * S g i)) := by rw [mul_assoc (g.e i) (S g i) (S g i)]
    _ = (g.e i * g.e i) * (S g i * S g i) := (mul_assoc _ _ _).symm
    _ = Rng.one * (S g i * S g i) := by rw [g.he i]
    _ = S g i * S g i := one_mul _

/-- Both summands, rewritten with the phases collected on the left. -/
theorem A_mul_A {i j : Nat} (hij : j < i) :
    A g i * A g j = (g.e i * g.e j) * (S g i * S g j) :=
  calc A g i * A g j = (g.e i * S g i) * (g.e j * S g j) := rfl
    _ = g.e i * (S g i * (g.e j * S g j)) := mul_assoc _ _ _
    _ = g.e i * ((S g i * g.e j) * S g j) := by rw [← mul_assoc (S g i) (g.e j) (S g j)]
    _ = g.e i * ((g.e j * S g i) * S g j) := by rw [← e_comm_gt g hij]
    _ = g.e i * (g.e j * (S g i * S g j)) := by rw [mul_assoc (g.e j) (S g i) (S g j)]
    _ = (g.e i * g.e j) * (S g i * S g j) := (mul_assoc _ _ _).symm

/-- Anticommutation in the orientation the computation produces. -/
theorem A_anti_raw {i j : Nat} (hij : j < i) (hne : j ≠ i) :
    A g j * A g i = -(A g i * A g j) :=
  calc A g j * A g i = (g.e j * S g j) * (g.e i * S g i) := rfl
    _ = g.e j * (S g j * (g.e i * S g i)) := mul_assoc _ _ _
    _ = g.e j * ((S g j * g.e i) * S g i) := by rw [← mul_assoc (S g j) (g.e i) (S g i)]
    _ = g.e j * ((-(g.e i * S g j)) * S g i) := by
          rw [eq_neg_symm (e_anti_lt g hij)]
    _ = g.e j * (-((g.e i * S g j) * S g i)) := by rw [neg_mul]
    _ = -(g.e j * ((g.e i * S g j) * S g i)) := by rw [mul_neg]
    _ = -(g.e j * (g.e i * (S g j * S g i))) := by rw [mul_assoc (g.e i) (S g j) (S g i)]
    _ = -((g.e j * g.e i) * (S g j * S g i)) := by rw [← mul_assoc (g.e j) (g.e i) (S g j * S g i)]
    _ = -((g.e i * g.e j) * (S g j * S g i)) := by rw [g.hee j i]
    _ = -((g.e i * g.e j) * (S g i * S g j)) := by
          rw [S_comm g hne]
    _ = -(A g i * A g j) := by rw [← A_mul_A g hij]

/-- **Anticommutation.** `A_i A_j = -(A_j A_i)` for `j < i` — the second hypothesis of the
factorization, discharged from the phase pattern alone. -/
theorem A_anti {i j : Nat} (hij : j < i) (hne : j ≠ i) :
    A g i * A g j = -(A g j * A g i) :=
  eq_neg_symm (A_anti_raw g hij hne)

end Staggered

/-! ## Part 2: the cancellation kit -/

namespace Rng

variable {R : Type u} [Rng R]

/-- Two anticommuting elements: the cross terms cancel. -/
theorem sq_of_anticomm2 (x y : R) (h : y * x = -(x * y)) :
    (x + y) * (x + y) = x * x + y * y :=
  calc (x + y) * (x + y) = (x + y) * x + (x + y) * y := left_distrib _ _ _
    _ = (x * x + y * x) + (x + y) * y := by rw [right_distrib x y x]
    _ = (x * x + y * x) + (x * y + y * y) := by rw [right_distrib x y y]
    _ = (x * x + -(x * y)) + (x * y + y * y) := by rw [h]
    _ = x * x + (-(x * y) + (x * y + y * y)) := add_assoc _ _ _
    _ = x * x + ((-(x * y) + x * y) + y * y) := by rw [← add_assoc (-(x * y)) (x * y) (y * y)]
    _ = x * x + (Rng.zero + y * y) := by rw [neg_add_cancel (x * y)]
    _ = x * x + y * y := by rw [zero_add (y * y)]

/-- The three-way cancellation shuffle, proved once. -/
theorem cancel3 (a b c p q r : R) :
    (((a + -p) + -q) + ((p + b) + -r)) + ((q + r) + c) = (a + b) + c := by
  have hab : (a + -p) + (p + b) = a + b :=
    calc (a + -p) + (p + b) = a + (-p + (p + b)) := add_assoc _ _ _
      _ = a + ((-p + p) + b) := by rw [← add_assoc (-p) p b]
      _ = a + (Rng.zero + b) := by rw [neg_add_cancel p]
      _ = a + b := by rw [zero_add b]
  calc (((a + -p) + -q) + ((p + b) + -r)) + ((q + r) + c)
      = (((a + -p) + (p + b)) + (-q + -r)) + ((q + r) + c) := by
        rw [add_add_add_comm (a + -p) (-q) (p + b) (-r)]
    _ = ((a + b) + (-q + -r)) + ((q + r) + c) := by rw [hab]
    _ = (a + b) + ((-q + -r) + ((q + r) + c)) := add_assoc _ _ _
    _ = (a + b) + (((-q + -r) + (q + r)) + c) := by
        rw [← add_assoc (-q + -r) (q + r) c]
    _ = (a + b) + (((-q + q) + (-r + r)) + c) := by
        rw [add_add_add_comm (-q) (-r) q r]
    _ = (a + b) + ((Rng.zero + (-r + r)) + c) := by rw [neg_add_cancel q]
    _ = (a + b) + ((Rng.zero + Rng.zero) + c) := by rw [neg_add_cancel r]
    _ = (a + b) + (Rng.zero + c) := by rw [zero_add (Rng.zero : R)]
    _ = (a + b) + c := by rw [zero_add c]

/-- Three pairwise-anticommuting elements: all six cross terms cancel. -/
theorem sq_of_anticomm3 (x y z : R)
    (hyx : y * x = -(x * y)) (hzx : z * x = -(x * z)) (hzy : z * y = -(y * z)) :
    ((x + y) + z) * ((x + y) + z) = (x * x + y * y) + z * z :=
  calc ((x + y) + z) * ((x + y) + z)
      = ((x + y) + z) * (x + y) + ((x + y) + z) * z := left_distrib _ _ _
    _ = (((x + y) + z) * x + ((x + y) + z) * y) + ((x + y) + z) * z := by
        rw [left_distrib ((x + y) + z) x y]
    _ = (((x + y) * x + z * x) + ((x + y) + z) * y) + ((x + y) + z) * z := by
        rw [right_distrib (x + y) z x]
    _ = (((x * x + y * x) + z * x) + ((x + y) + z) * y) + ((x + y) + z) * z := by
        rw [right_distrib x y x]
    _ = (((x * x + y * x) + z * x) + ((x + y) * y + z * y)) + ((x + y) + z) * z := by
        rw [right_distrib (x + y) z y]
    _ = (((x * x + y * x) + z * x) + ((x * y + y * y) + z * y)) + ((x + y) + z) * z := by
        rw [right_distrib x y y]
    _ = (((x * x + y * x) + z * x) + ((x * y + y * y) + z * y)) + ((x + y) * z + z * z) := by
        rw [right_distrib (x + y) z z]
    _ = (((x * x + y * x) + z * x) + ((x * y + y * y) + z * y)) + ((x * z + y * z) + z * z) := by
        rw [right_distrib x y z]
    _ = (((x * x + -(x * y)) + z * x) + ((x * y + y * y) + z * y)) + ((x * z + y * z) + z * z) := by
        rw [hyx]
    _ = (((x * x + -(x * y)) + -(x * z)) + ((x * y + y * y) + z * y)) + ((x * z + y * z) + z * z) := by
        rw [hzx]
    _ = (((x * x + -(x * y)) + -(x * z)) + ((x * y + y * y) + -(y * z))) + ((x * z + y * z) + z * z) := by
        rw [hzy]
    _ = (x * x + y * y) + z * z :=
        cancel3 (x * x) (y * y) (z * z) (x * y) (x * z) (y * z)
/-- Anticommuting with each of three elements gives anticommuting with their sum. -/
theorem anti_sum3 {x a b c : R}
    (ha : x * a = -(a * x)) (hb : x * b = -(b * x)) (hc : x * c = -(c * x)) :
    x * ((a + b) + c) = -(((a + b) + c) * x) :=
  calc x * ((a + b) + c) = x * (a + b) + x * c := left_distrib _ _ _
    _ = (x * a + x * b) + x * c := by rw [left_distrib x a b]
    _ = (-(a * x) + -(b * x)) + -(c * x) := by rw [ha, hb, hc]
    _ = -((a * x + b * x)) + -(c * x) := by rw [← neg_add (a * x) (b * x)]
    _ = -((a * x + b * x) + c * x) := by rw [← neg_add ((a * x + b * x)) (c * x)]
    _ = -(((a + b) * x) + c * x) := by rw [← right_distrib a b x]
    _ = -(((a + b) + c) * x) := by rw [← right_distrib (a + b) c x]

/-- Four pairwise-anticommuting elements: all twelve cross terms cancel. -/
theorem sq_of_anticomm4 (x y z w : R)
    (hyx : y * x = -(x * y)) (hzx : z * x = -(x * z)) (hzy : z * y = -(y * z))
    (hwx : w * x = -(x * w)) (hwy : w * y = -(y * w)) (hwz : w * z = -(z * w)) :
    (((x + y) + z) + w) * (((x + y) + z) + w)
      = ((x * x + y * y) + z * z) + w * w := by
  have hcross : w * ((x + y) + z) = -(((x + y) + z) * w) := anti_sum3 hwx hwy hwz
  calc (((x + y) + z) + w) * (((x + y) + z) + w)
      = ((x + y) + z) * ((x + y) + z) + w * w :=
        sq_of_anticomm2 ((x + y) + z) w hcross
    _ = ((x * x + y * y) + z * z) + w * w := by
        rw [sq_of_anticomm3 x y z hyx hzx hzy]

end Rng

/-! ## Part 3: the factorization, hypotheses discharged -/

namespace Staggered

open Rng

variable {R : Type u} [Rng R] (g : Gens R)

/-- **Three axes.** `(A₀ + A₁ + A₂)² = S₀² + S₁² + S₂²`, with anticommutation and squares
both derived from the generator relations. -/
theorem factorization3 :
    ((A g 0 + A g 1) + A g 2) * ((A g 0 + A g 1) + A g 2)
      = ((S g 0 * S g 0 + S g 1 * S g 1) + S g 2 * S g 2) := by
  have h10 : A g 1 * A g 0 = -(A g 0 * A g 1) := A_anti g (by decide) (by decide)
  have h20 : A g 2 * A g 0 = -(A g 0 * A g 2) := A_anti g (by decide) (by decide)
  have h21 : A g 2 * A g 1 = -(A g 1 * A g 2) := A_anti g (by decide) (by decide)
  rw [sq_of_anticomm3 (A g 0) (A g 1) (A g 2) h10 h20 h21,
      A_sq g 0, A_sq g 1, A_sq g 2]

/-- **Four axes.** The same statement with a fourth axis. -/
theorem factorization4 :
    (((A g 0 + A g 1) + A g 2) + A g 3) * (((A g 0 + A g 1) + A g 2) + A g 3)
      = (((S g 0 * S g 0 + S g 1 * S g 1) + S g 2 * S g 2) + S g 3 * S g 3) := by
  have h10 : A g 1 * A g 0 = -(A g 0 * A g 1) := A_anti g (by decide) (by decide)
  have h20 : A g 2 * A g 0 = -(A g 0 * A g 2) := A_anti g (by decide) (by decide)
  have h21 : A g 2 * A g 1 = -(A g 1 * A g 2) := A_anti g (by decide) (by decide)
  have h30 : A g 3 * A g 0 = -(A g 0 * A g 3) := A_anti g (by decide) (by decide)
  have h31 : A g 3 * A g 1 = -(A g 1 * A g 3) := A_anti g (by decide) (by decide)
  have h32 : A g 3 * A g 2 = -(A g 2 * A g 3) := A_anti g (by decide) (by decide)
  rw [sq_of_anticomm4 (A g 0) (A g 1) (A g 2) (A g 3) h10 h20 h21 h30 h31 h32,
      A_sq g 0, A_sq g 1, A_sq g 2, A_sq g 3]

end Staggered

/-! ## Smoke instance (nonvacuity) -/

instance : Add Unit := ⟨fun _ _ => ()⟩
instance : Mul Unit := ⟨fun _ _ => ()⟩
instance : Neg Unit := ⟨fun _ => ()⟩

instance : Rng Unit where
  zero := ()
  one := ()
  add_assoc := fun _ _ _ => rfl
  add_comm := fun _ _ => rfl
  zero_add := fun _ => rfl
  neg_add_cancel := fun _ => rfl
  mul_assoc := fun _ _ _ => rfl
  one_mul := fun _ => rfl
  mul_one := fun _ => rfl
  left_distrib := fun _ _ _ => rfl
  right_distrib := fun _ _ _ => rfl

def unitGens : Staggered.Gens Unit where
  e := fun _ => ()
  t := fun _ => ()
  s := fun _ => ()
  he := fun _ => rfl
  hee := fun _ _ => rfl
  het := fun _ => rfl
  hes := fun _ => rfl
  hlt_t := fun _ _ _ => rfl
  hlt_s := fun _ _ _ => rfl
  hgt_t := fun _ _ _ => rfl
  hgt_s := fun _ _ _ => rfl
  htt := fun _ _ _ => rfl
  hts := fun _ _ _ => rfl
  hst := fun _ _ _ => rfl
  hss := fun _ _ _ => rfl
