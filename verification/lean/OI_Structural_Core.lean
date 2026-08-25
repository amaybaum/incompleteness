/-
OI_Structural_Core.lean — self-contained Lean 4 proofs of the structural-chain core of
the OI papers: Theorem 1a at operator level (papers/SM.md §4.1), the Susskind
factorization's cancellation mechanism (§4.2), the chirality algebra of Theorem 3 (§4.3),
and the quadratic boost-Ward identity. No imports; checks with plain
`lean OI_Structural_Core.lean`. Companion numerical checks: structural_core_probe.py
(which also certifies, exactly in integer arithmetic, that the concrete lattice operators
satisfy every hypothesis used here). See VERIFYING.md.

Design notes. Theorem 1a is proved at OPERATOR level — identities in any ring generated
by U and an idempotent P — strictly stronger than the state-applied display in the paper.
The Susskind theorem is proved from anticommutation and square hypotheses; the companion
probe certifies those hypotheses hold exactly for the d = 3 and d = 4 lattice operators,
and the derivation of the hypotheses from the generator relations is a planned addition
(ROADMAP.md §C).
-/

universe u

/-! ## Part 0: minimal ring (associative, unital, additive commutative group) -/

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

/-! operator powers -/

def opow (a : R) : Nat → R
  | 0 => one
  | n + 1 => opow a n * a

theorem opow_succ_left (a : R) (n : Nat) : opow a (n + 1) = a * opow a n := by
  induction n with
  | zero =>
      show opow a 0 * a = a * opow a 0
      show one * a = a * one
      rw [one_mul, mul_one]
  | succ m ih =>
      show opow a (m + 1) * a = a * opow a (m + 1)
      calc opow a (m + 1) * a = (a * opow a m) * a := by rw [ih]
        _ = a * (opow a m * a) := mul_assoc _ _ _
        _ = a * opow a (m + 1) := rfl

theorem opow_mul_comm (a : R) (n : Nat) : a * opow a n = opow a n * a :=
  (opow_succ_left a n).symm.trans rfl

/-! commutation kit: `x * r = r * x` propagated through the ring operations -/

theorem comm_mul {r x y : R} (hx : x * r = r * x) (hy : y * r = r * y) :
    (x * y) * r = r * (x * y) :=
  calc (x * y) * r = x * (y * r) := mul_assoc _ _ _
    _ = x * (r * y) := by rw [hy]
    _ = (x * r) * y := (mul_assoc _ _ _).symm
    _ = (r * x) * y := by rw [hx]
    _ = r * (x * y) := mul_assoc _ _ _

theorem comm_add {r x y : R} (hx : x * r = r * x) (hy : y * r = r * y) :
    (x + y) * r = r * (x + y) := by
  rw [right_distrib, left_distrib, hx, hy]

theorem comm_neg {r x : R} (hx : x * r = r * x) : (-x) * r = r * (-x) := by
  rw [neg_mul, hx, ← mul_neg]

theorem comm_one {r : R} : (one : R) * r = r * one := by
  rw [one_mul, mul_one]

theorem comm_opow {r x : R} (hx : x * r = r * x) (n : Nat) :
    opow x n * r = r * opow x n := by
  induction n with
  | zero => exact comm_one
  | succ m ih =>
      show (opow x m * x) * r = r * (opow x m * x)
      exact comm_mul ih hx

end Rng

/-! ## Part 1 (M1): Theorem 1a at operator level — the exact projected evolution and
kernel equivariance, in any ring generated by U and an idempotent P. -/

namespace MZ

open Rng

variable {R : Type u} [Rng R]

def Qm (P : R) : R := Rng.one + -P
def Am (U P : R) : R := P * U * P
def Bm (U P : R) : R := P * U * Qm P
def Cm (U P : R) : R := Qm P * U * P
def Dm (U P : R) : R := Qm P * U * Qm P

/-- memory accumulator: K 0 = 0, K (t+1) = D·K t + C·(P·Uᵗ). -/
def Kk (U P : R) : Nat → R
  | 0 => Rng.zero
  | t + 1 => Dm U P * Kk U P t + Cm U P * (P * opow U t)

theorem P_add_Q (P : R) : P + Qm P = Rng.one :=
  calc P + Qm P = P + (Rng.one + -P) := rfl
    _ = P + (-P + Rng.one) := by rw [add_comm Rng.one (-P)]
    _ = (P + -P) + Rng.one := (add_assoc _ _ _).symm
    _ = Rng.zero + Rng.one := by rw [add_neg_cancel P]
    _ = Rng.one := zero_add _

theorem Q_idem {P : R} (hP : P * P = P) : Qm P * Qm P = Qm P :=
  calc Qm P * Qm P = (Rng.one + -P) * Qm P := rfl
    _ = Rng.one * Qm P + (-P) * Qm P := right_distrib _ _ _
    _ = Qm P + (-P) * Qm P := by rw [one_mul]
    _ = Qm P + -(P * Qm P) := by rw [neg_mul]
    _ = Qm P + -(P * Rng.one + P * (-P)) := by rw [left_distrib]
    _ = Qm P + -(P + P * (-P)) := by rw [mul_one]
    _ = Qm P + -(P + -(P * P)) := by rw [mul_neg]
    _ = Qm P + -(P + -P) := by rw [hP]
    _ = Qm P + -(Rng.zero) := by rw [add_neg_cancel P]
    _ = Qm P + (-(Rng.zero) + Rng.zero) := by rw [add_zero (-(Rng.zero : R))]
    _ = Qm P + Rng.zero := by rw [neg_add_cancel (Rng.zero : R)]
    _ = Qm P := add_zero _

theorem PQ_zero {P : R} (hP : P * P = P) : P * Qm P = Rng.zero :=
  calc P * Qm P = P * (Rng.one + -P) := rfl
    _ = P * Rng.one + P * (-P) := left_distrib _ _ _
    _ = P + P * (-P) := by rw [mul_one]
    _ = P + -(P * P) := by rw [mul_neg]
    _ = P + -P := by rw [hP]
    _ = Rng.zero := add_neg_cancel _

theorem absorb_P {P : R} (hP : P * P = P) (W X : R) :
    (W * P) * (P * X) = (W * P) * X :=
  calc (W * P) * (P * X) = W * (P * (P * X)) := mul_assoc _ _ _
    _ = W * ((P * P) * X) := by rw [← mul_assoc P P X]
    _ = W * (P * X) := by rw [hP]
    _ = (W * P) * X := (mul_assoc _ _ _).symm

theorem absorb_Q {P : R} (hP : P * P = P) (W X : R) :
    (W * Qm P) * (Qm P * X) = (W * Qm P) * X :=
  calc (W * Qm P) * (Qm P * X) = W * (Qm P * (Qm P * X)) := mul_assoc _ _ _
    _ = W * ((Qm P * Qm P) * X) := by rw [← mul_assoc (Qm P) (Qm P) X]
    _ = W * (Qm P * X) := by rw [Q_idem hP]
    _ = (W * Qm P) * X := (mul_assoc _ _ _).symm

/-- one Koopman step, P-component: P·U^{t+1} = A·(P·Uᵗ) + B·(Q·Uᵗ). -/
theorem step_p {U P : R} (hP : P * P = P) (t : Nat) :
    P * opow U (t + 1) = Am U P * (P * opow U t) + Bm U P * (Qm P * opow U t) :=
  calc P * opow U (t + 1) = P * (U * opow U t) := by rw [opow_succ_left]
    _ = (P * U) * opow U t := (mul_assoc _ _ _).symm
    _ = ((P * U) * Rng.one) * opow U t := by rw [mul_one (P * U)]
    _ = ((P * U) * (P + Qm P)) * opow U t := by rw [P_add_Q P]
    _ = ((P * U) * P + (P * U) * Qm P) * opow U t := by rw [left_distrib]
    _ = ((P * U) * P) * opow U t + ((P * U) * Qm P) * opow U t := right_distrib _ _ _
    _ = ((P * U) * P) * (P * opow U t) + ((P * U) * Qm P) * opow U t := by
          rw [absorb_P hP (P * U) (opow U t)]
    _ = ((P * U) * P) * (P * opow U t) + ((P * U) * Qm P) * (Qm P * opow U t) := by
          rw [absorb_Q hP (P * U) (opow U t)]
    _ = Am U P * (P * opow U t) + Bm U P * (Qm P * opow U t) := rfl

/-- one Koopman step, Q-component: Q·U^{t+1} = C·(P·Uᵗ) + D·(Q·Uᵗ). -/
theorem step_q {U P : R} (hP : P * P = P) (t : Nat) :
    Qm P * opow U (t + 1) = Cm U P * (P * opow U t) + Dm U P * (Qm P * opow U t) :=
  calc Qm P * opow U (t + 1) = Qm P * (U * opow U t) := by rw [opow_succ_left]
    _ = (Qm P * U) * opow U t := (mul_assoc _ _ _).symm
    _ = ((Qm P * U) * Rng.one) * opow U t := by rw [mul_one (Qm P * U)]
    _ = ((Qm P * U) * (P + Qm P)) * opow U t := by rw [P_add_Q P]
    _ = ((Qm P * U) * P + (Qm P * U) * Qm P) * opow U t := by rw [left_distrib]
    _ = ((Qm P * U) * P) * opow U t + ((Qm P * U) * Qm P) * opow U t := right_distrib _ _ _
    _ = ((Qm P * U) * P) * (P * opow U t) + ((Qm P * U) * Qm P) * opow U t := by
          rw [absorb_P hP (Qm P * U) (opow U t)]
    _ = ((Qm P * U) * P) * (P * opow U t) + ((Qm P * U) * Qm P) * (Qm P * opow U t) := by
          rw [absorb_Q hP (Qm P * U) (opow U t)]
    _ = Cm U P * (P * opow U t) + Dm U P * (Qm P * opow U t) := rfl

/-- closed form of the hidden sector: Q·Uᵗ = Dᵗ·Q + K t. -/
theorem q_closed {U P : R} (hP : P * P = P) (t : Nat) :
    Qm P * opow U t = opow (Dm U P) t * Qm P + Kk U P t := by
  induction t with
  | zero =>
      show Qm P * Rng.one = Rng.one * Qm P + Rng.zero
      rw [mul_one, one_mul, add_zero]
  | succ s ih =>
      calc Qm P * opow U (s + 1)
          = Cm U P * (P * opow U s) + Dm U P * (Qm P * opow U s) := step_q hP s
        _ = Cm U P * (P * opow U s)
              + Dm U P * (opow (Dm U P) s * Qm P + Kk U P s) := by rw [ih]
        _ = Cm U P * (P * opow U s)
              + (Dm U P * (opow (Dm U P) s * Qm P) + Dm U P * Kk U P s) := by
              rw [left_distrib]
        _ = Cm U P * (P * opow U s)
              + ((Dm U P * opow (Dm U P) s) * Qm P + Dm U P * Kk U P s) := by
              rw [← mul_assoc (Dm U P) (opow (Dm U P) s) (Qm P)]
        _ = Cm U P * (P * opow U s)
              + ((opow (Dm U P) s * Dm U P) * Qm P + Dm U P * Kk U P s) := by
              rw [opow_mul_comm (Dm U P) s]
        _ = (opow (Dm U P) s * Dm U P) * Qm P
              + (Dm U P * Kk U P s + Cm U P * (P * opow U s)) := by
              rw [add_left_comm (Cm U P * (P * opow U s))
                    ((opow (Dm U P) s * Dm U P) * Qm P) (Dm U P * Kk U P s)]
        _ = opow (Dm U P) (s + 1) * Qm P + Kk U P (s + 1) := rfl

/-- **M1.1 (Theorem 1a, operator form).** The exact projected evolution. -/
theorem mz_identity {U P : R} (hP : P * P = P) (t : Nat) :
    P * opow U (t + 1)
      = Am U P * (P * opow U t)
        + (Bm U P * Kk U P t + Bm U P * (opow (Dm U P) t * Qm P)) :=
  calc P * opow U (t + 1)
      = Am U P * (P * opow U t) + Bm U P * (Qm P * opow U t) := step_p hP t
    _ = Am U P * (P * opow U t)
          + Bm U P * (opow (Dm U P) t * Qm P + Kk U P t) := by rw [q_closed hP t]
    _ = Am U P * (P * opow U t)
          + (Bm U P * (opow (Dm U P) t * Qm P) + Bm U P * Kk U P t) := by
          rw [left_distrib]
    _ = Am U P * (P * opow U t)
          + (Bm U P * Kk U P t + Bm U P * (opow (Dm U P) t * Qm P)) := by
          rw [add_comm (Bm U P * (opow (Dm U P) t * Qm P)) (Bm U P * Kk U P t)]

/-- **M1.2 (Theorem 1a, equivariance).** Every memory kernel B·Dᵐ·C commutes with R. -/
theorem kernel_equivariant {U P Rr : R} (hUR : U * Rr = Rr * U)
    (hPR : P * Rr = Rr * P) (m : Nat) :
    (Bm U P * (opow (Dm U P) m * Cm U P)) * Rr
      = Rr * (Bm U P * (opow (Dm U P) m * Cm U P)) := by
  have hQR : Qm P * Rr = Rr * Qm P := comm_add comm_one (comm_neg hPR)
  have hBR : Bm U P * Rr = Rr * Bm U P := comm_mul (comm_mul hPR hUR) hQR
  have hCR : Cm U P * Rr = Rr * Cm U P := comm_mul (comm_mul hQR hUR) hPR
  have hDR : Dm U P * Rr = Rr * Dm U P := comm_mul (comm_mul hQR hUR) hQR
  exact comm_mul hBR (comm_mul (comm_opow hDR m) hCR)

end MZ

/-! ## Part 2 (M2.1-abstract): the Susskind factorization's algebraic core, d = 3.
From the generator relations, the three staggered summands anticommute pairwise, so
D² = S₀² + S₁² + S₂² — the cross terms cancel identically. -/

namespace Stag

open Rng

variable {R : Type u} [Rng R]

/-! The generator-relations layer (η involutions, commuting shifts, the sign pattern) is
recorded as INSTANCE OBLIGATIONS: `l3_core_relations_probe.py` verifies, as exact int64
matrix facts on the concrete d = 3 and d = 4 lattice operators, that the staggered summands
pairwise anticommute and square to the shift-differences squared — the hypotheses of
`susskind3` below. Deriving those hypotheses from the generator relations inside Lean is
the next file's job (spec'd); the cancellation mechanism, which is the theorem's actual
content, is proved here in full. -/

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

/-- **M2.1-core (Theorem 2's mechanism).** Pairwise-anticommuting staggered summands with
A_μ² = S_μ² give D² = S₀² + S₁² + S₂² — the cross terms cancel identically. Instance
obligations (mirror-certified exact on the lattice operators): the anticommutation and the
squares. -/
theorem susskind3 (A0 A1 A2 S0 S1 S2 : R)
    (h10 : A1 * A0 = -(A0 * A1)) (h20 : A2 * A0 = -(A0 * A2))
    (h21 : A2 * A1 = -(A1 * A2))
    (hsq0 : A0 * A0 = S0 * S0) (hsq1 : A1 * A1 = S1 * S1)
    (hsq2 : A2 * A2 = S2 * S2) :
    ((A0 + A1) + A2) * ((A0 + A1) + A2) = (S0 * S0 + S1 * S1) + S2 * S2 := by
  rw [sq_of_anticomm3 A0 A1 A2 h10 h20 h21, hsq0, hsq1, hsq2]

end Stag

/-! ## Part 3 (M3): Theorem 3's chirality algebra, abstract. -/

namespace Chiral

open Rng

variable {R : Type u} [Rng R]

/-- Anticommutation with ε is additive. -/
theorem anti_add {x y e : R} (hx : x * e = -(e * x)) (hy : y * e = -(e * y)) :
    (x + y) * e = -(e * (x + y)) := by
  rw [right_distrib, hx, hy, ← neg_add, ← left_distrib]

/-- **M3.1.** With D ε-anticommuting, ε² = 1, and m, p₀ commuting with ε:
{D + m·ε + p₀, ε} = (m + m) + (p₀·ε + p₀·ε) — zero iff the center terms vanish. -/
theorem center_anticommutator (D e m p : R)
    (he : e * e = Rng.one) (hDe : D * e = -(e * D))
    (hme : m * e = e * m) (hpe : p * e = e * p) :
    (D + (m * e + p)) * e + e * (D + (m * e + p))
      = (m + m) + (p * e + p * e) :=
  calc (D + (m * e + p)) * e + e * (D + (m * e + p))
      = (D * e + (m * e + p) * e) + e * (D + (m * e + p)) := by
        rw [right_distrib D (m * e + p) e]
    _ = (D * e + (m * e + p) * e) + (e * D + e * (m * e + p)) := by
        rw [left_distrib e D (m * e + p)]
    _ = (D * e + e * D) + ((m * e + p) * e + e * (m * e + p)) :=
        add_add_add_comm _ _ _ _
    _ = (-(e * D) + e * D) + ((m * e + p) * e + e * (m * e + p)) := by rw [hDe]
    _ = Rng.zero + ((m * e + p) * e + e * (m * e + p)) := by
        rw [neg_add_cancel (e * D)]
    _ = (m * e + p) * e + e * (m * e + p) := zero_add _
    _ = ((m * e) * e + p * e) + e * (m * e + p) := by rw [right_distrib (m * e) p e]
    _ = ((m * e) * e + p * e) + (e * (m * e) + e * p) := by
        rw [left_distrib e (m * e) p]
    _ = (m * (e * e) + p * e) + (e * (m * e) + e * p) := by rw [mul_assoc m e e]
    _ = (m * Rng.one + p * e) + (e * (m * e) + e * p) := by rw [he]
    _ = (m + p * e) + (e * (m * e) + e * p) := by rw [mul_one m]
    _ = (m + p * e) + ((e * m) * e + e * p) := by rw [← mul_assoc e m e]
    _ = (m + p * e) + ((m * e) * e + e * p) := by rw [← hme]
    _ = (m + p * e) + (m * (e * e) + e * p) := by rw [mul_assoc m e e]
    _ = (m + p * e) + (m * Rng.one + e * p) := by rw [he]
    _ = (m + p * e) + (m + e * p) := by rw [mul_one m]
    _ = (m + p * e) + (m + p * e) := by rw [← hpe]
    _ = (m + m) + (p * e + p * e) := add_add_add_comm _ _ _ _

/-- **M3.2.** Given {D, ε} = 0, ε² = 1, m central for D and ε:
(D + m·ε)² = D² + m·m — the manuscript's "squares to −¼(□ − 4m²)". -/
theorem mass_square (D e m : R)
    (he : e * e = Rng.one) (hDe : D * e = -(e * D))
    (hme : m * e = e * m) (hmD : m * D = D * m) :
    (D + m * e) * (D + m * e) = D * D + m * m :=
  calc (D + m * e) * (D + m * e)
      = (D + m * e) * D + (D + m * e) * (m * e) := left_distrib _ _ _
    _ = (D * D + (m * e) * D) + (D + m * e) * (m * e) := by
        rw [right_distrib D (m * e) D]
    _ = (D * D + (m * e) * D) + (D * (m * e) + (m * e) * (m * e)) := by
        rw [right_distrib D (m * e) (m * e)]
    _ = (D * D + (m * e) * (m * e)) + ((m * e) * D + D * (m * e)) := by
        rw [add_add_add_comm (D * D) ((m * e) * D) (D * (m * e)) ((m * e) * (m * e)),
            add_comm ((m * e) * D) (D * (m * e)),
            add_add_add_comm (D * D) (D * (m * e)) ((m * e) * (m * e)) ((m * e) * D)]
    _ = (D * D + (m * e) * (m * e)) + (m * (e * D) + D * (m * e)) := by
        rw [mul_assoc m e D]
    _ = (D * D + (m * e) * (m * e)) + (m * (e * D) + (D * m) * e) := by
        rw [← mul_assoc D m e]
    _ = (D * D + (m * e) * (m * e)) + (m * (e * D) + (m * D) * e) := by rw [← hmD]
    _ = (D * D + (m * e) * (m * e)) + (m * (e * D) + m * (D * e)) := by
        rw [mul_assoc m D e]
    _ = (D * D + (m * e) * (m * e)) + m * (e * D + D * e) := by
        rw [← left_distrib m (e * D) (D * e)]
    _ = (D * D + (m * e) * (m * e)) + m * (e * D + -(e * D)) := by rw [hDe]
    _ = (D * D + (m * e) * (m * e)) + m * Rng.zero := by
        rw [add_neg_cancel (e * D)]
    _ = (D * D + (m * e) * (m * e)) + Rng.zero := by rw [mul_zero m]
    _ = D * D + (m * e) * (m * e) := add_zero _
    _ = D * D + m * (e * (m * e)) := by rw [mul_assoc m e (m * e)]
    _ = D * D + m * ((e * m) * e) := by rw [← mul_assoc e m e]
    _ = D * D + m * ((m * e) * e) := by rw [← hme]
    _ = D * D + m * (m * (e * e)) := by rw [mul_assoc m e e]
    _ = D * D + m * (m * Rng.one) := by rw [he]
    _ = D * D + m * m := by rw [mul_one m]

end Chiral

/-! ## Part 4: the quadratic boost-Ward identity, over any commutative ring
(the factor 2 generalized to any central c). -/

class CRng (R : Type u) extends Rng R where
  mul_comm : ∀ a b : R, a * b = b * a

namespace CRng

open Rng

variable {R : Type u} [CRng R]

theorem left_swap (a b x : R) : a * (b * x) = b * (a * x) := by
  rw [← Rng.mul_assoc a b x, mul_comm a b, Rng.mul_assoc b a x]

/-- **S9.1.** k·(−c·zt·ω) + ω·(c·zs·k) = c·(ωk)·(zs − zt): the boost-Ward residual. -/
theorem boost_ward (c w k zs zt : R) :
    k * (-(c * (zt * w))) + w * (c * (zs * k))
      = c * ((w * k) * (zs + -zt)) :=
  calc k * (-(c * (zt * w))) + w * (c * (zs * k))
      = -(k * (c * (zt * w))) + w * (c * (zs * k)) := by
        rw [Rng.mul_neg k (c * (zt * w))]
    _ = -(c * (k * (zt * w))) + w * (c * (zs * k)) := by
        rw [left_swap k c (zt * w)]
    _ = -(c * (k * (zt * w))) + c * (w * (zs * k)) := by
        rw [left_swap w c (zs * k)]
    _ = -(c * (zt * (k * w))) + c * (w * (zs * k)) := by
        rw [left_swap k zt w]
    _ = -(c * (zt * (w * k))) + c * (w * (zs * k)) := by
        rw [mul_comm k w]
    _ = -(c * ((w * k) * zt)) + c * (w * (zs * k)) := by
        rw [mul_comm zt (w * k)]
    _ = -(c * ((w * k) * zt)) + c * (zs * (w * k)) := by
        rw [left_swap w zs k, Rng.mul_assoc zs w k]
    _ = -(c * ((w * k) * zt)) + c * ((w * k) * zs) := by
        rw [mul_comm zs (w * k)]
    _ = c * ((w * k) * zs) + -(c * ((w * k) * zt)) := by
        rw [Rng.add_comm (-(c * ((w * k) * zt))) (c * ((w * k) * zs))]
    _ = c * ((w * k) * zs) + c * (-((w * k) * zt)) := by
        rw [← Rng.mul_neg c ((w * k) * zt)]
    _ = c * ((w * k) * zs + -((w * k) * zt)) := by
        rw [← Rng.left_distrib c ((w * k) * zs) (-((w * k) * zt))]
    _ = c * ((w * k) * zs + (w * k) * (-zt)) := by
        rw [← Rng.mul_neg (w * k) zt]
    _ = c * ((w * k) * (zs + -zt)) := by
        rw [← Rng.left_distrib (w * k) zs (-zt)]

end CRng

/-! Smoke instance (nonvacuity): the trivial ring on Unit. -/

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

instance : CRng Unit where
  mul_comm := fun _ _ => rfl
