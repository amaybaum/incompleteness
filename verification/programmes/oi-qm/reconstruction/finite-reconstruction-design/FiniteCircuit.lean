import Mathlib

/- Finite circuit normal form. This is an abstract group identity: concrete
   target rotations still require their one-parameter and flip identities. -/
namespace FiniteReconstructionDesign

def signedAngle (flip : Bool) (a : ℝ) : ℝ := if flip then -a else a

section GroupCircuit

variable {G : Type*} [Group G]
variable (R : ℝ → G) (X : G)

def normalForm (flip : Bool) (a : ℝ) : G := (if flip then X else 1) * R a

theorem normalForm_mul
    (hR : ∀ a b, R a * R b = R (a + b))
    (hX : X * X = 1) (hcross : ∀ a, R a * X = X * R (-a))
    (p q : Bool) (a b : ℝ) :
    normalForm R X p a * normalForm R X q b =
      normalForm R X (Bool.xor p q) (signedAngle q a + b) := by
  cases p <;> cases q
  · simpa [normalForm, signedAngle] using hR a b
  · change (1 * R a) * (X * R b) = X * R (-a + b)
    rw [one_mul]
    rw [← mul_assoc, hcross, mul_assoc, hR]
  · change (X * R a) * (1 * R b) = X * R (a + b)
    rw [one_mul, mul_assoc, hR]
  · change (X * R a) * (X * R b) = 1 * R (-a + b)
    rw [one_mul]
    calc
      X * R a * (X * R b) = X * (R a * X) * R b := by group
      _ = X * (X * R (-a)) * R b := by rw [hcross]
      _ = R (-a) * R b := by rw [← mul_assoc, hX, one_mul]
      _ = R (-a + b) := hR _ _

/-- Circuit steps are chronological: rotation first, then conditional flip. -/
def circuit : List (ℝ × Bool) → G
  | [] => 1
  | (a, f) :: tail => circuit tail * normalForm R X f a

def circuitParity : List (ℝ × Bool) → Bool
  | [] => false
  | (_, f) :: tail => Bool.xor (circuitParity tail) f

def circuitAngle : List (ℝ × Bool) → ℝ
  | [] => 0
  | (a, f) :: tail => signedAngle f (circuitAngle tail) + a

theorem circuit_normalForm (hzero : R 0 = 1)
    (hR : ∀ a b, R a * R b = R (a + b))
    (hX : X * X = 1) (hcross : ∀ a, R a * X = X * R (-a))
    (steps : List (ℝ × Bool)) :
    circuit R X steps = normalForm R X (circuitParity steps) (circuitAngle steps) := by
  induction steps with
  | nil => simp [circuit, circuitParity, circuitAngle, normalForm, hzero]
  | cons step tail ih =>
    rcases step with ⟨a, f⟩
    simp only [circuit, circuitParity, circuitAngle, ih]
    exact normalForm_mul R X hR hX hcross _ _ _ _

theorem closed_circuit_rotation (hzero : R 0 = 1)
    (hR : ∀ a b, R a * R b = R (a + b))
    (hX : X * X = 1) (hcross : ∀ a, R a * X = X * R (-a))
    (steps : List (ℝ × Bool)) (hclosed : circuitParity steps = false) :
    circuit R X steps = R (circuitAngle steps) := by
  rw [circuit_normalForm R X hzero hR hX hcross, hclosed]
  simp [normalForm]

#print axioms normalForm_mul
#print axioms circuit_normalForm
#print axioms closed_circuit_rotation

end GroupCircuit
end FiniteReconstructionDesign
