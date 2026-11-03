import Mathlib.Tactic.Abel

/-!
# SUBSTATE-1: pure-gradient link flatness and reversible two-slice update

Research-only mathematical scope:
1. On ANY additive commutative gauge-angle group, the oriented gradient
   around one square telescopes to zero (and hence its exponential holonomy
   is the identity). This is a necessary countercontrol for the naive
   site-gradient proposal; it is not a no-go for general OI H-link carriers.
2. For ANY function F on an additive commutative group, the two-slice
   update (x,y) -> (F x - y,x) has the explicit inverse
   (u,v) -> (v,F v - u). This covers the reversibility structure of the
   finite wave update without asserting gauge covariance or Yang-Mills.

No physical gauge dynamics, nonabelian action selection or quantum
operational completion is claimed.
-/

namespace OIBridge.GradientLinkFlatness

universe u
variable {A : Type u} [AddCommGroup A]

/-- A link variable defined purely by differences of site fields has
zero additive plaquette curvature on any square. -/
theorem square_gradient_flat (a b c d : A) :
    (b - a) + (c - b) + (d - c) + (a - d) = 0 := by
  abel

/-- The general two-slice reversible rule, with no assumptions about F. -/
def waveStep (F : A → A) (p : A × A) : A × A :=
  (F p.1 - p.2, p.1)

/-- The inverse two-slice rule. -/
def waveUnstep (F : A → A) (p : A × A) : A × A :=
  (p.2, F p.2 - p.1)

theorem waveUnstep_waveStep (F : A → A) (p : A × A) :
    waveUnstep F (waveStep F p) = p := by
  rcases p with ⟨x, y⟩
  apply Prod.ext
  · rfl
  · change F x - (F x - y) = y
    abel

theorem waveStep_waveUnstep (F : A → A) (p : A × A) :
    waveStep F (waveUnstep F p) = p := by
  rcases p with ⟨x, y⟩
  apply Prod.ext
  · change F y - (F y - x) = x
    abel
  · rfl

#print axioms square_gradient_flat
#print axioms waveUnstep_waveStep
#print axioms waveStep_waveUnstep

end OIBridge.GradientLinkFlatness
