/-
OI_Gauge_Certificates.lean — self-contained Lean 4 certificates for the finite/algebraic
core of the local-gauge closure argument (papers/SM.md). No imports; checks with plain
`lean OI_Gauge_Certificates.lean` on any recent Lean 4. Companion numerical checks:
gauge_certificates_probe.py. See VERIFYING.md for the full procedure.

Contents:
  Part 1 — telescoping: a hom from an abelian alphabet into any group has commuting
    image, and a pure difference-map connection has every plaquette exactly trivial
    (arbitrary additive abelian alphabet, arbitrary target group).
  Part 2 — central-sign collapse: evenness + additivity give M² = 1; with q-torsion and
    q odd, M = 1 — for every odd q.
  Part 3 — the cubic counting layer: kernel-checked integer identities over the
    explicitly generated 24-element rotation action on the six directed links:
      |rots| = 24,  Σχ² = 72,  Σχ³ = 288,  Σχ·χ_broken = 144,
    plus χ-consistency and distinctness of the 24 actions.
    Bridge (planned, ROADMAP.md §A): the classical averaging identity
    |G|·dim Hom_G(V,W) = Σ_g χ_V(g)χ_W(g); dividing the kernel-checked sums by 24 gives
    Hom(V₆,V₆) = 3 (multiplicity-free), dim Hom_O(V₆, End V₆) = 12, and
    dim Hom_O(V₆, broken₂₂) = 6 — the counts used in papers/SM.md.
-/

universe u v

/-! ## Part 0: minimal self-contained algebra (no Mathlib) -/

class Grp (G : Type u) extends Mul G where
  one : G
  inv : G → G
  mul_assoc : ∀ a b c : G, a * b * c = a * (b * c)
  one_mul : ∀ a : G, one * a = a
  mul_one : ∀ a : G, a * one = a
  inv_mul : ∀ a : G, inv a * a = one

namespace Grp

variable {G : Type u} [Grp G]

theorem mul_inv (a : G) : a * inv a = one :=
  calc a * inv a = one * (a * inv a) := (one_mul _).symm
    _ = (inv (inv a) * inv a) * (a * inv a) := by rw [← inv_mul (inv a)]
    _ = inv (inv a) * (inv a * (a * inv a)) := mul_assoc _ _ _
    _ = inv (inv a) * ((inv a * a) * inv a) := by rw [← mul_assoc (inv a) a (inv a)]
    _ = inv (inv a) * (one * inv a) := by rw [inv_mul a]
    _ = inv (inv a) * inv a := by rw [one_mul (inv a)]
    _ = one := inv_mul _

theorem mul_left_cancel {a x y : G} (hxy : a * x = a * y) : x = y :=
  calc x = one * x := (one_mul _).symm
    _ = (inv a * a) * x := by rw [← inv_mul a]
    _ = inv a * (a * x) := mul_assoc _ _ _
    _ = inv a * (a * y) := by rw [hxy]
    _ = (inv a * a) * y := (mul_assoc _ _ _).symm
    _ = one * y := by rw [inv_mul a]
    _ = y := one_mul _

theorem eq_inv_of_mul_eq_one {x a : G} (hxa : x * a = one) : x = inv a :=
  calc x = x * one := (mul_one _).symm
    _ = x * (a * inv a) := by rw [← mul_inv a]
    _ = (x * a) * inv a := (mul_assoc _ _ _).symm
    _ = one * inv a := by rw [hxa]
    _ = inv a := one_mul _

/-- A central element conjugates trivially — the −I₆ step of the chain. -/
theorem central_conj (c x : G) (hc : ∀ y : G, c * y = y * c) :
    (c * x) * inv c = x :=
  calc (c * x) * inv c = (x * c) * inv c := by rw [hc x]
    _ = x * (c * inv c) := mul_assoc _ _ _
    _ = x * one := by rw [mul_inv c]
    _ = x := mul_one _

end Grp

class AddCommGrp (A : Type u) extends Add A, Neg A where
  zero : A
  add_assoc : ∀ a b c : A, a + b + c = a + (b + c)
  add_comm : ∀ a b : A, a + b = b + a
  zero_add : ∀ a : A, zero + a = a
  neg_add_cancel : ∀ a : A, -a + a = zero

namespace AddCommGrp

variable {A : Type u} [AddCommGrp A]

theorem add_zero (a : A) : a + zero = a := by
  rw [add_comm a zero, zero_add]

theorem add_neg_cancel (a : A) : a + -a = zero := by
  rw [add_comm a (-a), neg_add_cancel]

theorem eq_neg_of_add_eq_zero {x a : A} (hxa : x + a = zero) : x = -a :=
  calc x = x + zero := (add_zero _).symm
    _ = x + (a + -a) := by rw [← add_neg_cancel a]
    _ = (x + a) + -a := (add_assoc _ _ _).symm
    _ = zero + -a := by rw [hxa]
    _ = -a := zero_add _

theorem neg_add (a b : A) : -(a + b) = -a + -b := by
  have key : (-a + -b) + (a + b) = zero :=
    calc (-a + -b) + (a + b) = -a + (-b + (a + b)) := add_assoc _ _ _
      _ = -a + (-b + (b + a)) := by rw [add_comm a b]
      _ = -a + ((-b + b) + a) := by rw [← add_assoc (-b) b a]
      _ = -a + (zero + a) := by rw [neg_add_cancel b]
      _ = -a + a := by rw [zero_add a]
      _ = zero := neg_add_cancel _
  exact (eq_neg_of_add_eq_zero key).symm

theorem neg_neg (a : A) : -(-a) = a :=
  (eq_neg_of_add_eq_zero (add_neg_cancel a)).symm

/-- Exponent identity for the telescoping step: (b − a) + (c − b) = c − a. -/
theorem diff_add_diff (a b c : A) : (b + -a) + (c + -b) = c + -a :=
  calc (b + -a) + (c + -b) = (-a + b) + (c + -b) := by rw [add_comm b (-a)]
    _ = -a + (b + (c + -b)) := add_assoc _ _ _
    _ = -a + (b + (-b + c)) := by rw [add_comm c (-b)]
    _ = -a + ((b + -b) + c) := by rw [← add_assoc b (-b) c]
    _ = -a + (zero + c) := by rw [add_neg_cancel b]
    _ = -a + c := by rw [zero_add c]
    _ = c + -a := add_comm _ _

/-- Second exponent identity: (c − a) − (c − d) = d − a. -/
theorem diff_sub_diff (a c d : A) : (c + -a) + -(c + -d) = d + -a :=
  calc (c + -a) + -(c + -d) = (c + -a) + (-c + -(-d)) := by rw [neg_add c (-d)]
    _ = (c + -a) + (-c + d) := by rw [neg_neg d]
    _ = (-a + c) + (-c + d) := by rw [add_comm c (-a)]
    _ = -a + (c + (-c + d)) := add_assoc _ _ _
    _ = -a + ((c + -c) + d) := by rw [← add_assoc c (-c) d]
    _ = -a + (zero + d) := by rw [add_neg_cancel c]
    _ = -a + d := by rw [zero_add d]
    _ = d + -a := add_comm _ _

end AddCommGrp

/-- An additive-to-multiplicative homomorphism: the abstract form of the §6.5 map. -/
structure Ch (A : Type u) (G : Type v) [AddCommGrp A] [Grp G] where
  f : A → G
  map_add : ∀ a b : A, f (a + b) = f a * f b

namespace Ch

variable {A : Type u} {G : Type v} [AddCommGrp A] [Grp G] (h : Ch A G)

open Grp AddCommGrp

theorem map_zero : h.f zero = one := by
  have hz : h.f zero * h.f zero = h.f zero * one := by
    rw [← h.map_add, zero_add, mul_one]
  exact Grp.mul_left_cancel hz

theorem map_neg (a : A) : h.f (-a) = inv (h.f a) := by
  apply Grp.eq_inv_of_mul_eq_one
  rw [← h.map_add, neg_add_cancel, h.map_zero]

/-- lemma: the image of any additive character commutes. -/
theorem image_comm (a b : A) : h.f a * h.f b = h.f b * h.f a := by
  rw [← h.map_add, ← h.map_add, add_comm]

theorem hom_diff (x y : A) : h.f (x + -y) = h.f x * inv (h.f y) := by
  have hstep : h.f (x + -y) * h.f y = h.f x := by
    rw [← h.map_add, add_assoc, neg_add_cancel, add_zero]
  calc h.f (x + -y) = h.f (x + -y) * one := (mul_one _).symm
    _ = h.f (x + -y) * (h.f y * inv (h.f y)) := by rw [← mul_inv (h.f y)]
    _ = (h.f (x + -y) * h.f y) * inv (h.f y) := (mul_assoc _ _ _).symm
    _ = h.f x * inv (h.f y) := by rw [hstep]

/-- **T1 (/).** A pure difference-map connection is an exact coboundary:
the plaquette on corners a (00), b (10), c (11), d (01) is trivial, for EVERY
abelian alphabet, EVERY group, EVERY field configuration. -/
theorem plaquette_trivial (a b c d : A) :
    ((h.f (b + -a) * h.f (c + -b)) * inv (h.f (c + -d))) * inv (h.f (d + -a))
      = one := by
  rw [← h.map_add, diff_add_diff]
  rw [← h.hom_diff]
  rw [diff_sub_diff]
  exact mul_inv _

end Ch

/-! ## Part 2: the central-sign collapse (T2), for every odd q -/

section Pow

variable {G : Type u} [Grp G]

def gpow (a : G) : Nat → G
  | 0 => Grp.one
  | n + 1 => gpow a n * a

theorem gpow_one_pow (n : Nat) : gpow (Grp.one : G) n = Grp.one := by
  induction n with
  | zero => rfl
  | succ k ih =>
      simp only [gpow]
      rw [ih, Grp.mul_one]

theorem gpow_double (a : G) (k : Nat) : gpow a (k + k) = gpow (a * a) k := by
  induction k with
  | zero => rfl
  | succ m ih =>
      have hidx : (m + 1) + (m + 1) = ((m + m) + 1) + 1 := by omega
      rw [hidx]
      simp only [gpow]
      rw [ih]
      exact Grp.mul_assoc _ _ _

def OddN (q : Nat) : Prop := ∃ k, q = (k + k) + 1

/-- In any group: M² = 1 and M^q = 1 with q odd force M = 1. -/
theorem eq_one_of_sq_of_odd {M : G} {q : Nat}
    (h2 : M * M = Grp.one) (hodd : OddN q) (hq : gpow M q = Grp.one) :
    M = Grp.one := by
  cases hodd with
  | intro k hk =>
    rw [hk] at hq
    have h1 : gpow M ((k + k) + 1) = M := by
      simp only [gpow]
      rw [gpow_double, h2, gpow_one_pow, Grp.one_mul]
    rw [h1] at hq
    exact hq

end Pow

/-- **T2 ().** B₆-evenness of the state-to-link map (the −I₆ consequence,
`h.f (−a) = h.f a`) together with per-direction additivity and q-torsion at ODD q
forces the connection to be identically trivial.  This covers EVERY odd q — strictly
stronger than the q = 11 character census of the probe. -/
theorem trivial_connection {A : Type u} {G : Type v}
    [AddCommGrp A] [Grp G] (h : Ch A G)
    (heven : ∀ a : A, h.f (-a) = h.f a)
    {q : Nat} (hodd : OddN q)
    (htor : ∀ a : A, gpow (h.f a) q = Grp.one) :
    ∀ a : A, h.f a = Grp.one := by
  intro a
  have h1 : h.f a = Grp.inv (h.f a) := (heven a).symm.trans (h.map_neg a)
  have hsq : h.f a * h.f a = Grp.one := by
    have h2 := Grp.mul_inv (h.f a)
    rw [← h1] at h2
    exact h2
  exact eq_one_of_sq_of_odd hsq hodd (htor a)

/-! ### A8: the oddness hypothesis is necessary.

`trivial_connection` above covers every odd `q`. The census below is the countercontrol: at
`q = 4` the additive characters squaring to one are `k ∈ {0, 2}`, so a nontrivial survivor
exists and the `OddN` hypothesis cannot simply be dropped. -/

/-- The characters with `χ² = 1` at modulus `q`, as the residues `k` with `2k ≡ 0 (mod q)`. -/
def sqTrivial (q : Nat) : List Nat := (List.range q).filter (fun k => (2 * k) % q == 0)

/-- For odd `q` the census is trivial — the arithmetic shadow of `eq_one_of_sq_of_odd`. -/
theorem sqTrivial_odd :
    [sqTrivial 3, sqTrivial 5, sqTrivial 7, sqTrivial 9, sqTrivial 11, sqTrivial 13]
      = [[0], [0], [0], [0], [0], [0]] := by decide

/-- At `q = 4` the survivor `k = 2` appears: oddness is load-bearing, not decorative. -/
theorem sqTrivial_four : sqTrivial 4 = [0, 2] := by decide

/-! Smoke instances (nonvacuity of the classes; also exercises elaboration). -/

instance : AddCommGrp Int where
  zero := 0
  add_assoc := fun a b c => by omega
  add_comm := fun a b => by omega
  zero_add := fun a => by omega
  neg_add_cancel := fun a => by omega

instance : Mul Unit := ⟨fun _ _ => ()⟩

instance : Grp Unit where
  one := ()
  inv := fun _ => ()
  mul_assoc := fun _ _ _ => rfl
  one_mul := fun _ => rfl
  mul_one := fun _ => rfl
  inv_mul := fun _ => rfl

/-! ## Part 3: the cubic counting layer (T3) — kernel-checked integers.

The 24-element rotation action on the six directed links is generated explicitly
(all 48 signed axis-permutations, filtered by det = +1; the stored parities are
themselves kernel-validated against the inversion-count sign).  The characters are
exact integers.  The classical averaging identity |G|·dim Hom = Σ χχ is the ONE
deferred bridge (Mathlib phase); everything numerical below it is `decide`-checked. -/

namespace Cubic

abbrev F3 := Fin 3

def p0 : F3 → F3 := fun i => i
def p1 : F3 → F3 := fun i => if i = 0 then 1 else if i = 1 then 2 else 0
def p2 : F3 → F3 := fun i => if i = 0 then 2 else if i = 1 then 0 else 1
def t01 : F3 → F3 := fun i => if i = 0 then 1 else if i = 1 then 0 else 2
def t02 : F3 → F3 := fun i => if i = 0 then 2 else if i = 1 then 1 else 0
def t12 : F3 → F3 := fun i => if i = 0 then 0 else if i = 1 then 2 else 1

def perms : List ((F3 → F3) × Int) :=
  [(p0, 1), (p1, 1), (p2, 1), (t01, -1), (t02, -1), (t12, -1)]

/-- Permutation sign from the inversion count (validates the stored parities). -/
def psign (p : F3 → F3) : Int :=
  (if (p 1).val < (p 0).val then -1 else 1) *
  ((if (p 2).val < (p 0).val then -1 else 1) *
   (if (p 2).val < (p 1).val then -1 else 1))

theorem parities_correct :
    (perms.all (fun pp => psign pp.1 == pp.2)) = true := by decide

def Sgn := Bool × Bool × Bool

def signs : List Sgn :=
  [(false, false, false), (true, false, false), (false, true, false),
   (false, false, true), (true, true, false), (true, false, true),
   (false, true, true), (true, true, true)]

def sg (s : Sgn) : F3 → Bool :=
  fun i => if i = 0 then s.1 else if i = 1 then s.2.1 else s.2.2

def sprod (s : Sgn) : Int :=
  (if s.1 then -1 else 1) *
  ((if s.2.1 then -1 else 1) * (if s.2.2 then -1 else 1))

structure El where
  p : F3 → F3
  par : Int
  s : Sgn

def allElems : List El :=
  perms.flatMap (fun pp => signs.map (fun t => ⟨pp.1, pp.2, t⟩))

def det (g : El) : Int := g.par * sprod g.s

def rots : List El := allElems.filter (fun g => det g == 1)

def fixp (g : El) : Int :=
  (if g.p 0 = 0 then 1 else 0) + (if g.p 1 = 1 then 1 else 0) +
  (if g.p 2 = 2 then 1 else 0)

/-- Character of the signed 3-dim (T₁ / vector) piece. -/
def chiT (g : El) : Int :=
  (if g.p 0 = 0 then (if sg g.s 0 then -1 else 1) else 0) +
  (if g.p 1 = 1 then (if sg g.s 1 then -1 else 1) else 0) +
  (if g.p 2 = 2 then (if sg g.s 2 then -1 else 1) else 0)

def chiE (g : El) : Int := fixp g - 1
def chiA (_ : El) : Int := 1
def chi6 (g : El) : Int := chiT g + chiE g + chiA g

/-- Direct 6-dim trace: number of fixed directed links. -/
def chi6dir (g : El) : Int :=
  (if g.p 0 = 0 ∧ sg g.s 0 = false then 2 else 0) +
  (if g.p 1 = 1 ∧ sg g.s 1 = false then 2 else 0) +
  (if g.p 2 = 2 ∧ sg g.s 2 = false then 2 else 0)

/-- Character of the 22-dim broken restriction ⊕_{i<j}(Vᵢ⊗Vⱼ* ⊕ Vⱼ⊗Vᵢ*)
under the isotypic 3+2+1 splitting. -/
def chiBrk (g : El) : Int :=
  2 * (chiT g * chiE g + chiT g * chiA g + chiE g * chiA g)

def isum : List Int → Int
  | [] => 0
  | x :: xs => x + isum xs

/-- Action of g on directed link (axis i, orientation e), as an index in 0..5. -/
def dirIm (g : El) (i : F3) (e : Bool) : Nat :=
  2 * (g.p i).val + (if e != sg g.s i then 1 else 0)

def tbl (g : El) : List Nat :=
  [dirIm g 0 false, dirIm g 0 true, dirIm g 1 false,
   dirIm g 1 true, dirIm g 2 false, dirIm g 2 true]

def dedup : List (List Nat) → List (List Nat)
  | [] => []
  | x :: xs => if xs.contains x then dedup xs else x :: dedup xs

/-- |rotation group| = 24. -/
theorem rots_card : rots.length = 24 := by decide

/-- The 24 rotation actions on directed links are pairwise distinct. -/
theorem rots_distinct : (dedup (rots.map tbl)).length = 24 := by decide

/-- χ₆ = χ_T + χ_E + χ_A agrees with the direct fixed-direction count, on all 48. -/
theorem chi_consistent :
    (allElems.all (fun g => chi6 g == chi6dir g)) = true := by decide

/-- Σχ² = 72 = 24·3: with the averaging bridge, Hom(V₆,V₆) is 3-dimensional, so
V₆ has exactly three multiplicity-one constituents (Σmᵢ² = 3). -/
theorem sum_sq : isum (rots.map (fun g => chi6 g * chi6 g)) = 72 := by decide

/-- Σχ³ = 288 = 24·12: with the bridge, dim Hom_O(V₆, End V₆) = 12 (). -/
theorem sum_cube :
    isum (rots.map (fun g => chi6 g * (chi6 g * chi6 g))) = 288 := by decide

/-- Σχ₆·χ_broken = 144 = 24·6: with the bridge, exactly 6 equivariant coefficients
survive restriction to the 22 broken directions (). -/
theorem sum_broken :
    isum (rots.map (fun g => chi6 g * chiBrk g)) = 144 := by decide

/-! ### The irreducible characters, and the multiplicity certificates (A2-A4, A6).

The five irreducible characters of O are given as functions on `El`, not as a table of
trusted class data: `A₁` is constant, `E` and `T₁` are the pieces already used by `chi6`,
`A₂` is the stored parity, and `T₂ = T₁ ⊗ A₂`.  Row-orthonormality is then checked as a sum
over the actual 24 elements rather than over class weights, which is strictly stronger than
a table certificate — it needs no separate claim that the class census is right.

Every multiplicity below is `24 * m`, and the division by 24 is the one step deferred to the
averaging identity of the Mathlib phase.  The sums themselves are kernel-checked here. -/

/-- The sign character. On a rotation `det = par * sprod = 1`, so `par = sprod`; the stored
parity is validated against the inversion count by `parities_correct`. -/
def chiA2 (g : El) : Int := g.par

/-- `T₂ = T₁ ⊗ A₂`. -/
def chiT2 (g : El) : Int := chiT g * chiA2 g

/-- The five irreducible characters, in the order `A₁, A₂, E, T₁, T₂`. -/
def irr : List (El → Int) := [chiA, chiA2, chiE, chiT, chiT2]

/-- Each character evaluates to its own degree at the identity: `1, 1, 2, 3, 3`. -/
theorem irr_degrees :
    irr.map (fun c => c ⟨p0, 1, (false, false, false)⟩) = [1, 1, 2, 3, 3] := by decide

/-- Row-orthonormality over the 24 rotations: `⟨χᵢ, χⱼ⟩ = 24` on the diagonal and `0` off it.
This is A2's certificate, and it doubles as the irreducibility witness for all five. -/
theorem irr_orthonormal :
    (irr.map (fun a => irr.map (fun b => isum (rots.map (fun g => a g * b g)))))
      = [[24, 0, 0, 0, 0], [0, 24, 0, 0, 0], [0, 0, 24, 0, 0],
         [0, 0, 0, 24, 0], [0, 0, 0, 0, 24]] := by decide

/-- **A3.** `⟨χ₆, χᵢ⟩ = 24 · (1, 0, 1, 1, 0)`: V₆ is multiplicity-free on `{A₁, E, T₁}`. -/
theorem mult_V6 :
    irr.map (fun c => isum (rots.map (fun g => chi6 g * c g))) = [24, 0, 24, 24, 0] := by
  decide

/-- **A4.** `⟨χ₆², χᵢ⟩ = 24 · (3, 1, 4, 5, 3)` — the 36 dimensions of `End(V₆)`. -/
theorem mult_End :
    irr.map (fun c => isum (rots.map (fun g => chi6 g * chi6 g * c g)))
      = [72, 24, 96, 120, 72] := by decide

/-- The multiplicities of A4 account for all 36 dimensions: `3·1+1·1+4·2+5·3+3·3 = 36`. -/
theorem mult_End_dims : 3 * 1 + 1 * 1 + 4 * 2 + 5 * 3 + 3 * 3 = 36 := by decide

/-- **A6.** `⟨χ_broken, χᵢ⟩ = 24 · (0, 0, 2, 4, 2)` — the broken restriction carries no
`A₁` or `A₂`, so no equivariant scalar survives on it. -/
theorem mult_broken :
    irr.map (fun c => isum (rots.map (fun g => chiBrk g * c g))) = [0, 0, 48, 96, 48] := by
  decide

/-- The multiplicities of A6 account for all 22 dimensions, and `chiBrk` has degree 22. -/
theorem mult_broken_dims :
    2 * 2 + 4 * 3 + 2 * 3 = 22 ∧ chiBrk ⟨p0, 1, (false, false, false)⟩ = 22 := by decide

end Cubic

/- Optional visibility (safe to keep; prints during elaboration):
#eval Cubic.rots.length
#eval Cubic.isum (Cubic.rots.map (fun g => Cubic.chi6 g * (Cubic.chi6 g * Cubic.chi6 g)))
#eval Cubic.isum (Cubic.rots.map (fun g => Cubic.chi6 g * Cubic.chiBrk g))
-/
