/-
OI_Time_Reversal.lean — self-contained Lean 4 proof of [SM] Theorem 17 (§5.1), the
time-reversal invariance of the discrete wave equation. No imports; checks with plain
`lean OI_Time_Reversal.lean`. Companion numerical check: time_reversal_probe.py.
See VERIFYING.md.

Added in b447's first closure wave. The coverage census found this statement at level GAP —
neither probe nor kernel — while being one of the cheapest conversions in the corpus: it is a
symmetry of a second-order linear recursion, so it needs no analysis, no lattice, no dimension
and no imported premise. It is therefore stated here over an arbitrary additive commutative
group of field values rather than over the reals, which is strictly more general than the
manuscript's reading and costs nothing.

WHAT IS PROVED, and it is the manuscript's statement rather than an instance of it:

    Theorem 17.  The discrete wave equation is invariant under time reversal
                 T : phi(n, t) -> phi(n, -t).

The proof is the manuscript's own substitution. Reading the wave equation at time -t and
rearranging it in the group is the whole content; NO property of the spatial coupling is used.
That last point settles a reading question the manuscript leaves open: §5.1 displays the
nearest-neighbour form while the theorem says "the discrete wave equation", which elsewhere in
[SM] is d-dimensional. The statement is therefore proved first with the spatial stencil left
ABSTRACT, and the displayed form is an instance -- so both readings are covered and neither is
assumed.

THE SECOND-ORDER STRUCTURE IS LOAD-BEARING, and the countercontrol says so. A first-order
transport rule phi(n, t+1) = phi(n+1, t) is a perfectly good reversible lattice update and is
NOT time-reversal invariant; `transport_not_time_reversal_invariant` exhibits the failure at an
explicit point. So the theorem is a fact about the wave equation's second-order form and not a
generality about lattice dynamics.
-/

universe u

/-! ## Part 0: minimal additive commutative group

The five core files are zero-import by design, so the algebra the statement needs is built here
rather than assumed. Only addition, negation and their laws are used — the wave equation has no
multiplication in it, so no ring structure is introduced. -/

class AbGrp (R : Type u) extends Add R, Neg R where
  zero : R
  add_assoc : ∀ a b c : R, a + b + c = a + (b + c)
  add_comm : ∀ a b : R, a + b = b + a
  zero_add : ∀ a : R, zero + a = a
  neg_add_cancel : ∀ a : R, -a + a = zero

namespace AbGrp

variable {R : Type u} [AbGrp R]

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

/-- The one rearrangement the theorem needs: in an additive commutative group, `a = b + -d` and
`d = b + -a` say the same thing. Everything else in the proof is index arithmetic. -/
theorem swap_neg {a b d : R} (h : a = b + -d) : d = b + -a := by
  have h1 : a + d = b := by
    calc a + d = (b + -d) + d := by rw [h]
      _ = b + (-d + d) := add_assoc _ _ _
      _ = b + zero := by rw [neg_add_cancel]
      _ = b := add_zero _
  apply add_left_cancel (a := a)
  calc a + d = b := h1
    _ = b + zero := (add_zero _).symm
    _ = b + (-a + a) := by rw [neg_add_cancel]
    _ = b + (a + -a) := by rw [add_comm (-a) a]
    _ = (b + a) + -a := (add_assoc _ _ _).symm
    _ = (a + b) + -a := by rw [add_comm b a]
    _ = a + (b + -a) := add_assoc _ _ _

end AbGrp

/-! ## Part 1: the discrete wave equation and its time reversal -/

open AbGrp

/-- The discrete wave equation of [SM] §5.1, written with `+ -` rather than `-` so that no
subtraction operation has to be introduced:

    phi(n, t+1) = phi(n-1, t) + phi(n+1, t) - phi(n, t-1).

Sites and times are both indexed by `Int`. No lattice structure is imposed on the site index —
the proof never uses one, and imposing one would make the statement narrower than the
manuscript's. -/
def Wave {R : Type u} [AbGrp R] (phi : Int → Int → R) : Prop :=
  ∀ n t : Int, phi n (t + 1) = phi (n - 1) t + phi (n + 1) t + -(phi n (t - 1))

/-- The same equation with the SPATIAL part left abstract:

    phi(n, t+1) = (S applied to the time-t slice)(n) - phi(n, t-1),

for an arbitrary stencil `S`. The manuscript displays the nearest-neighbour form when it proves
Theorem 17, but writes the theorem for "the discrete wave equation", which elsewhere in [SM] is
`d`-dimensional. Leaving `S` abstract settles the reading: the reversal argument uses NOTHING
about the spatial coupling, so it holds for the one-dimensional display, for the `d`-dimensional
lattice, and for any other stencil at once. -/
def WaveS {R : Type u} [AbGrp R] (S : (Int → R) → Int → R) (phi : Int → Int → R) : Prop :=
  ∀ n t : Int, phi n (t + 1) = S (fun m => phi m t) n + -(phi n (t - 1))

/-- The nearest-neighbour stencil of the displayed equation. -/
def nnStencil {R : Type u} [AbGrp R] (f : Int → R) (n : Int) : R := f (n - 1) + f (n + 1)

theorem wave_iff_waveS {R : Type u} [AbGrp R] (phi : Int → Int → R) :
    Wave phi ↔ WaveS nnStencil phi := Iff.rfl

/-- Time reversal `T : phi(n, t) -> phi(n, -t)`. -/
def timeReverse {R : Type u} (phi : Int → Int → R) : Int → Int → R :=
  fun n t => phi n (-t)

/-- **[SM] Theorem 17, in the form that settles the spatial reading.** For ANY stencil `S`, the
discrete wave equation is invariant under time reversal `T : phi(n, t) -> phi(n, -t)`.

The manuscript's proof, in the manuscript's order: substitute, read the equation at time `-t`,
and rearrange. The spatial coupling never enters, which is why it can stay abstract. -/
theorem waveS_time_reversal_invariant {R : Type u} [AbGrp R] (S : (Int → R) → Int → R)
    (phi : Int → Int → R) (h : WaveS S phi) : WaveS S (timeReverse phi) := by
  intro n t
  -- The equation at time `-t` is the hypothesis; the goal is its rearrangement.
  have hb : phi n (-t + 1) = S (fun m => phi m (-t)) n + -(phi n (-t - 1)) := h n (-t)
  have e1 : -(t + 1) = -t - 1 := by omega
  have e2 : -(t - 1) = -t + 1 := by omega
  show phi n (-(t + 1)) = S (fun m => phi m (-t)) n + -(phi n (-(t - 1)))
  rw [e1, e2]
  exact swap_neg hb

/-- **[SM] Theorem 17.** *The discrete wave equation is invariant under time reversal
`T : phi(n, t) -> phi(n, -t)`.*

The manuscript's displayed nearest-neighbour form, as an instance of the stencil-free statement
above. -/
theorem wave_time_reversal_invariant {R : Type u} [AbGrp R] (phi : Int → Int → R)
    (h : Wave phi) : Wave (timeReverse phi) :=
  waveS_time_reversal_invariant nnStencil phi h

/-! ## Part 2: controls

Two, in the order that matters: the equation is satisfied by something (so the theorem is not
vacuous), and the second-order structure is load-bearing (so the theorem is not a generality
about lattice updates). -/

/-- `Int` as an additive commutative group, so the controls below can be stated concretely. The
zero-import layer has no algebra library to draw this from, so it is supplied here. -/
instance : AbGrp Int where
  zero := 0
  add_assoc a b c := by omega
  add_comm a b := by omega
  zero_add a := by omega
  neg_add_cancel a := by omega

/-- Non-vacuity: a field constant in time solves the wave equation. -/
theorem wave_nonvacuous : Wave (fun n _ : Int => n) := by
  intro n _
  show n = (n - 1) + (n + 1) + -n
  omega

/-- The first-order transport rule, a reversible lattice update that is NOT second order. -/
def Transport (phi : Int → Int → Int) : Prop :=
  ∀ n t : Int, phi n (t + 1) = phi (n + 1) t

/-- The countercontrol. Time-reversal invariance is a fact about the wave equation's SECOND-ORDER
form, not about lattice updates in general: transport satisfies `Transport` and its time reversal
does not. -/
theorem transport_not_time_reversal_invariant :
    ¬ (∀ phi : Int → Int → Int, Transport phi → Transport (timeReverse phi)) := by
  intro hall
  have ht : Transport (fun n t : Int => n + t) := by
    intro n t
    show n + (t + 1) = (n + 1) + t
    omega
  have := hall _ ht 0 0
  simp [timeReverse] at this

/-! ### What these proofs rest on

Printed at build time so the kernel's own answer, not a claim in a comment, is what the log
carries. `sorryAx` in any of these lines would mean a hole. -/

#print axioms waveS_time_reversal_invariant
#print axioms wave_time_reversal_invariant
#print axioms wave_nonvacuous
#print axioms transport_not_time_reversal_invariant
