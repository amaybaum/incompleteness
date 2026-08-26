/-
  OI_Structural_Chain.lean — ROADMAP §B, the parts that need no dependency.

  Self-contained Lean 4: no Mathlib, no lake project, zero imports. Kernel check:

      lean OI_Structural_Chain.lean

  Companion probe: structural_chain_probe.py (labels C4, C5).

  ## Part 1 — detailed balance (§B2)

  The GR lemma is usually stated with an exponential: on a transition graph with
  `W(m→n)/W(n→m) = exp(−τ(ω_n − ω_m))`, the stationary state is Gibbs and unique up to
  scale. The exponential is doing exactly one job — making the edge ratio a *gradient*,
  `R_{mn} = g_n / g_m` for a positive `g`. Stated that way, and cross-multiplied so no
  division is needed, the lemma is not analysis at all: it is a multiplicative cocycle plus
  connectivity, and it lives in a commutative monoid whose relevant elements are invertible.

  Nothing here needs a spectral argument. In particular Perron–Frobenius is not used and is
  not needed: uniqueness up to scale follows from connectivity and invertibility, not from
  irreducibility of a stochastic matrix. The statement proved is accordingly *stronger* than
  the numerical mirror's, which recovers a stationary vector as a null space — here, every
  edgewise-balanced `p` is proportional to `g` along any path, with no null space computed.

  ## Part 2 — the cubic invariant (§B3, algebraic core)

  Corollary 1a's algebraic content is that an equivariant quadratic form on three dimensions
  is forced to be a multiple of `δ`, so no quadratic spatial anisotropy survives. The
  character of the induced action on `Sym²(ℝ³)` sums to `48` over the 48-element signed
  permutation group `B₃`, and to `24` over its 24 rotations — one invariant either way. As in
  §A7, the closing division by the group order is the averaging identity and is deferred; the
  invariant itself is exhibited here rather than counted.
-/

/- Part 2's sums run over 48 elements with a 6-dimensional induced action, well inside the
default limits; Part 1 is proof-term work and needs none. The limit is raised only to match
the sibling regulator file's setting so the two read alike. -/
set_option maxRecDepth 10000

universe u

/-! ## Part 1: detailed balance without the exponential -/

namespace Balance

/-- A commutative monoid. Multiplication is all the detailed-balance argument uses — there is
no addition anywhere in it, so requiring a ring would overstate the hypotheses. -/
class CMon (M : Type u) where
  one : M
  mul : M → M → M
  mul_assoc : ∀ a b c : M, mul (mul a b) c = mul a (mul b c)
  mul_comm : ∀ a b : M, mul a b = mul b a
  one_mul : ∀ a : M, mul one a = a

namespace CMon

variable {M : Type u} [CMon M]

local infixl:70 " ⋆ " => CMon.mul

theorem mul_one (a : M) : a ⋆ CMon.one = a := by
  rw [mul_comm]; exact one_mul a

/-- Right cancellation by an element that has an inverse. -/
theorem cancel_right {x y c ci : M} (hc : c ⋆ ci = CMon.one) (h : x ⋆ c = y ⋆ c) : x = y :=
  calc x = x ⋆ CMon.one := (mul_one x).symm
    _ = x ⋆ (c ⋆ ci) := by rw [hc]
    _ = (x ⋆ c) ⋆ ci := (mul_assoc x c ci).symm
    _ = (y ⋆ c) ⋆ ci := by rw [h]
    _ = y ⋆ (c ⋆ ci) := mul_assoc y c ci
    _ = y ⋆ CMon.one := by rw [hc]
    _ = y := mul_one y

/-- Rearrangement used twice below: `(a ⋆ b) ⋆ c = (a ⋆ c) ⋆ b`. -/
theorem swap_right (a b c : M) : (a ⋆ b) ⋆ c = (a ⋆ c) ⋆ b :=
  calc (a ⋆ b) ⋆ c = a ⋆ (b ⋆ c) := mul_assoc a b c
    _ = a ⋆ (c ⋆ b) := by rw [mul_comm b c]
    _ = (a ⋆ c) ⋆ b := (mul_assoc a c b).symm

end CMon

open CMon

variable {M : Type u} [CMon M]

local infixl:70 " ⋆ " => CMon.mul

/-- Balance composes: proportionality is transitive along an edge, provided the intermediate
weight is invertible. This is the only step where invertibility is used. -/
theorem trans_step {p g gi : Nat → M} {a c b : Nat}
    (hc : g c ⋆ gi c = CMon.one)
    (h1 : p c ⋆ g a = p a ⋆ g c)
    (h2 : p b ⋆ g c = p c ⋆ g b) :
    p b ⋆ g a = p a ⋆ g b := by
  refine cancel_right hc ?_
  calc (p b ⋆ g a) ⋆ g c = (p b ⋆ g c) ⋆ g a := swap_right _ _ _
    _ = (p c ⋆ g b) ⋆ g a := by rw [h2]
    _ = (p c ⋆ g a) ⋆ g b := swap_right _ _ _
    _ = (p a ⋆ g c) ⋆ g b := by rw [h1]
    _ = (p a ⋆ g b) ⋆ g c := swap_right _ _ _

/-- Edgewise balance along a path, listed as consecutive nodes. -/
def PathBal (p g : Nat → M) : List Nat → Prop
  | [] => True
  | [_] => True
  | a :: b :: rest => (p b ⋆ g a = p a ⋆ g b) ∧ PathBal p g (b :: rest)

/-- Every node of the list is proportional to the base point `a`. -/
def AllProp (p g : Nat → M) (a : Nat) : List Nat → Prop
  | [] => True
  | b :: rest => (p b ⋆ g a = p a ⋆ g b) ∧ AllProp p g a rest

/-- Proportionality transports along an edge: if everything is proportional to `c`, and `c`
is proportional to `a`, then everything is proportional to `a`. -/
theorem rebase {p g gi : Nat → M} (hinv : ∀ n, g n ⋆ gi n = CMon.one) {a c : Nat}
    (h1 : p c ⋆ g a = p a ⋆ g c) :
    ∀ l : List Nat, AllProp p g c l → AllProp p g a l
  | [], _ => True.intro
  | _ :: rest, h => ⟨trans_step (hinv c) h1 h.1, rebase hinv h1 rest h.2⟩

/-- **§B2 — detailed balance forces proportionality.** On a path whose every edge is
balanced, every node carries the same constant of proportionality to `g`. Connectivity enters
as the path itself; invertibility of the weights enters only through `trans_step`. -/
theorem path_prop {p g gi : Nat → M} (hinv : ∀ n, g n ⋆ gi n = CMon.one) :
    ∀ (a : Nat) (l : List Nat), PathBal p g (a :: l) → AllProp p g a l
  | _, [], _ => True.intro
  | _, c :: rest, h => ⟨h.1, rebase hinv h.1 rest (path_prop hinv c rest h.2)⟩

/-! ### A nontrivial instance, and the countercontrol

The instance is `Int` under multiplication with weights in `{1, -1}`, so the invertibility
hypothesis is satisfied by genuinely varying weights rather than by a constant. The
countercontrol needs no inverses at all: a *failure* of proportionality is an inequality of
products, and is checked as one. -/

instance : CMon Int where
  one := 1
  mul := fun a b => a * b
  mul_assoc := fun a b c => Int.mul_assoc a b c
  mul_comm := fun a b => Int.mul_comm a b
  one_mul := fun a => Int.one_mul a

def gEx : Nat → Int := fun n => if n % 2 == 0 then 1 else -1
def pEx : Nat → Int := fun n => if n % 2 == 0 then 2 else -2

/-- The weights are their own inverses. Quantified over all nodes, so this is a case split
rather than a decision procedure. -/
theorem gEx_invertible : ∀ n, CMon.mul (gEx n) (gEx n) = (CMon.one : Int) := by
  intro n
  show gEx n * gEx n = 1
  unfold gEx
  by_cases h : (n % 2 == 0) = true
  · rw [if_pos h]; decide
  · rw [if_neg h]; decide

/-- The four-node path `0-1-2-3` is edgewise balanced with these weights. -/
theorem pEx_balanced : PathBal pEx gEx [0, 1, 2, 3] := by
  refine ⟨?_, ?_, ?_, True.intro⟩ <;> decide +kernel

/-- Its endpoints are therefore proportional — the conclusion of `path_prop`, instantiated. -/
theorem pEx_endpoints : AllProp pEx gEx 0 [1, 2, 3] :=
  path_prop (p := pEx) (g := gEx) (gi := gEx) gEx_invertible 0 [1, 2, 3] pEx_balanced

/-! ### Connectivity is load-bearing

Six nodes in two components `{0,1,2}` and `{3,4,5}`, with weights `g` and a state `p` that is
`1·g` on the first component and `3·g` on the second. Every edge inside a component is
balanced, and yet the two components disagree: `p 3 ⋆ g 0 ≠ p 0 ⋆ g 3`. The bridging edge
`(2,3)` is exactly what is missing, and it is not balanced. -/

def gD : Nat → Int := fun n => [1, 2, 4, 1, 3, 9].getD n 0
def pD : Nat → Int := fun n => [1, 2, 4, 3, 9, 27].getD n 0

/-- Every edge within a component is balanced. -/
theorem gD_edges_balanced :
    PathBal pD gD [0, 1, 2] ∧ PathBal pD gD [3, 4, 5] := by
  refine ⟨⟨?_, ?_, True.intro⟩, ⟨?_, ?_, True.intro⟩⟩ <;> decide +kernel

/-- But proportionality fails across the components, so connectivity cannot be dropped. -/
theorem gD_not_global : pD 3 * gD 0 ≠ pD 0 * gD 3 := by decide +kernel

/-- And the edge that would bridge them is not balanced — the two components really do carry
different constants. -/
theorem gD_bridge_unbalanced : pD 3 * gD 2 ≠ pD 2 * gD 3 := by decide +kernel

end Balance

/-! ## Part 2: the cubic quadratic invariant (§B3, algebraic core) -/

namespace Cubic3

abbrev P3 := Nat × Nat × Nat
abbrev Sg3 := Bool × Bool × Bool

def ap (p : P3) (i : Nat) : Nat :=
  if i = 0 then p.1 else if i = 1 then p.2.1 else p.2.2

def sgn (s : Sg3) (i : Nat) : Int :=
  if i = 0 then (if s.1 then -1 else 1)
  else if i = 1 then (if s.2.1 then -1 else 1)
  else (if s.2.2 then -1 else 1)

def perms : List P3 := [(0,1,2), (0,2,1), (1,0,2), (1,2,0), (2,0,1), (2,1,0)]

/-- Parity of each listed permutation, from the inversion count — validated, not stored. -/
def psign (p : P3) : Int :=
  (if ap p 1 < ap p 0 then -1 else 1) *
  ((if ap p 2 < ap p 0 then -1 else 1) * (if ap p 2 < ap p 1 then -1 else 1))

def signs : List Sg3 :=
  [(false,false,false), (false,false,true), (false,true,false), (false,true,true),
   (true,false,false),  (true,false,true),  (true,true,false),  (true,true,true)]

abbrev El3 := P3 × Sg3

/-- The full signed permutation group on three coordinates. -/
def b3 : List El3 := perms.flatMap (fun p => signs.map (fun s => (p, s)))

def det (g : El3) : Int := psign g.1 * (sgn g.2 0 * (sgn g.2 1 * sgn g.2 2))

/-- Its rotation subgroup — the same 24 elements the gauge layer calls `rots`. -/
def rot3 : List El3 := b3.filter (fun g => det g == 1)

theorem b3_card : b3.length = 48 := by decide +kernel
theorem rot3_card : rot3.length = 24 := by decide +kernel

/-- Every listed permutation is a bijection of `{0,1,2}`. -/
theorem perms_are_permutations :
    (perms.all (fun p =>
      ([ap p 0, ap p 1, ap p 2].all (fun v => v < 3)) &&
      (ap p 0 != ap p 1) && (ap p 0 != ap p 2) && (ap p 1 != ap p 2))) = true := by
  decide +kernel

def isum : List Int → Int
  | [] => 0
  | x :: xs => x + isum xs

/-- The six basis elements `e_a · e_b`, `a ≤ b`, of `Sym²(ℝ³)`. -/
def symIdx : List (Nat × Nat) := [(0,0), (0,1), (0,2), (1,1), (1,2), (2,2)]

def samePair (x y a b : Nat) : Bool := (x == a && y == b) || (x == b && y == a)

/-- Character of the induced action on `Sym²(ℝ³)`. -/
def trSym (g : El3) : Int :=
  isum (symIdx.map (fun ab =>
    if samePair (ap g.1 ab.1) (ap g.1 ab.2) ab.1 ab.2
    then sgn g.2 ab.1 * sgn g.2 ab.2 else 0))

/-- The identity has character 6 — the dimension of `Sym²(ℝ³)`. -/
theorem trSym_id : trSym ((0,1,2), (false,false,false)) = 6 := by decide +kernel

/-- **§B3 core, full group.** `Σ χ = 48 = 1 · 48`: one invariant quadratic form. -/
theorem sum_trSym_b3 : isum (b3.map trSym) = 48 := by decide +kernel

/-- **§B3 core, rotations.** `Σ χ = 24 = 1 · 24`: the same conclusion on half the group, so
the result does not depend on including the improper elements. -/
theorem sum_trSym_rot : isum (rot3.map trSym) = 24 := by decide +kernel

def diagFixed (v : Nat → Int) (g : El3) : Bool :=
  symIdx.all (fun ab =>
    let ga := ap g.1 ab.1
    let gb := ap g.1 ab.2
    let src : Int := if ab.1 == ab.2 then v ab.1 else 0
    let tgt : Int := if ga == gb then v ga else 0
    (sgn g.2 ab.1 * sgn g.2 ab.2 * src) == tgt)

def vDelta : Nat → Int := fun _ => 1
def vAnis : Nat → Int := fun i => if i = 0 then 1 else 0

/-- The invariant is `δ`, exhibited rather than inferred from a dimension count. -/
theorem b3_fixes_delta : (b3.all (diagFixed vDelta)) = true := by decide +kernel

/-- Countercontrol: a direction-singling form is **not** invariant. Together with the
character sum this is Corollary 1a's algebraic core — an equivariant quadratic form on three
dimensions is a multiple of `δ`, so quadratic spatial anisotropy is forbidden. -/
theorem b3_forbids_anisotropy : (b3.all (diagFixed vAnis)) = false := by decide +kernel

end Cubic3
