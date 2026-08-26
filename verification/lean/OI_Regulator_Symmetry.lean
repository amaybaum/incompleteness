/-
  OI_Regulator_Symmetry.lean — the regulator-symmetry certificates (ROADMAP §A7, §A7b).

  Self-contained Lean 4: no Mathlib, no lake project, zero imports.  Kernel check:

      lean OI_Regulator_Symmetry.lean

  A clean exit is the certificate.  Companion probe: representation_bridge_probe.py
  (labels B5, B5b).

  ## What is established here, and what is not

  Two symmetry groups act on ℝ⁴ by signed permutations of the coordinates:

  * the **hypercubic** group — every signed permutation of all four coordinates, order 384;
  * the **native** group — signed permutations fixing the time axis setwise, i.e. spatial
    B₃ together with time reflection, order 96.

  For each we compute, in exact integer arithmetic, the character of the induced action on
  the space of quadratic forms — `Sym²(ℝ⁴)` for the metric sector (§A7) and
  `Sym²(Λ²ℝ⁴)` for the field-strength sector (§A7b) — summed over the group.  The sums are

      hypercubic : Σ χ = 384 = 1 · 384          native : Σ χ = 192 = 2 · 96

  so under the averaging identity the invariant subspaces have dimension **1** and **2**
  respectively.  That last division by the group order is the one step this file does not
  take: it is the classical averaging identity, deferred to the Mathlib phase (§A1), exactly
  as in the cubic counting layer of `OI_Gauge_Certificates.lean`.  What is proved here are
  the character sums themselves, and — independently of any dimension count — that the two
  named forms really are invariant under the native group and that one of them is *not*
  invariant under the hypercubic group.

  The physical reading: electric and magnetic normalizations are independent under the
  native symmetry and are locked to each other only by the Euclidean regulator.
-/

namespace Regulator

/-! ## Signed permutations of four coordinates

Coordinates are `Nat` values `0, 1, 2, 3` with `0` the time axis.  A group element is a
permutation tuple together with a sign pattern, in the same record style the cubic layer
uses.  The permutation list is not trusted: `perms_are_permutations` checks that every
entry is a bijection of `{0,1,2,3}`, and `perms_distinct` that there are 24 different ones.
-/

abbrev P4 := Nat × Nat × Nat × Nat
abbrev Sg4 := Bool × Bool × Bool × Bool

def ap (p : P4) (i : Nat) : Nat :=
  if i = 0 then p.1 else if i = 1 then p.2.1 else if i = 2 then p.2.2.1 else p.2.2.2

def sgn (s : Sg4) (i : Nat) : Int :=
  if i = 0 then (if s.1 then -1 else 1)
  else if i = 1 then (if s.2.1 then -1 else 1)
  else if i = 2 then (if s.2.2.1 then -1 else 1)
  else (if s.2.2.2 then -1 else 1)

def perms : List P4 :=
  [(0,1,2,3), (0,1,3,2), (0,2,1,3), (0,2,3,1),
   (0,3,1,2), (0,3,2,1), (1,0,2,3), (1,0,3,2),
   (1,2,0,3), (1,2,3,0), (1,3,0,2), (1,3,2,0),
   (2,0,1,3), (2,0,3,1), (2,1,0,3), (2,1,3,0),
   (2,3,0,1), (2,3,1,0), (3,0,1,2), (3,0,2,1),
   (3,1,0,2), (3,1,2,0), (3,2,0,1), (3,2,1,0)]

def signs : List Sg4 :=
  [(false,false,false,false), (false,false,false,true),
   (false,false,true,false),  (false,false,true,true),
   (false,true,false,false),  (false,true,false,true),
   (false,true,true,false),   (false,true,true,true),
   (true,false,false,false),  (true,false,false,true),
   (true,false,true,false),   (true,false,true,true),
   (true,true,false,false),   (true,true,false,true),
   (true,true,true,false),    (true,true,true,true)]

/-- Every listed tuple is a bijection of `{0,1,2,3}`: its image list is a permutation. -/
theorem perms_are_permutations :
    (perms.all (fun p =>
      ([ap p 0, ap p 1, ap p 2, ap p 3].all (fun v => v < 4)) &&
      (ap p 0 != ap p 1) && (ap p 0 != ap p 2) && (ap p 0 != ap p 3) &&
      (ap p 1 != ap p 2) && (ap p 1 != ap p 3) && (ap p 2 != ap p 3))) = true := by
  decide

def dedupP : List P4 → List P4
  | [] => []
  | x :: xs => if xs.contains x then dedupP xs else x :: dedupP xs

theorem perms_distinct : (dedupP perms).length = 24 := by decide

abbrev El4 := P4 × Sg4

/-- The hypercubic group: all signed permutations of the four coordinates. -/
def hyper : List El4 := perms.flatMap (fun p => signs.map (fun s => (p, s)))

/-- The native group: the time axis is not mixed with the spatial ones, so the permutation
fixes coordinate `0`. All sixteen sign patterns remain, time reflection included. -/
def native : List El4 := hyper.filter (fun g => ap g.1 0 == 0)

theorem hyper_card : hyper.length = 384 := by decide
theorem native_card : native.length = 96 := by decide

def isum : List Int → Int
  | [] => 0
  | x :: xs => x + isum xs

/-! ## §A7 — quadratic forms on ℝ⁴

`Sym²(ℝ⁴)` has the ten basis elements `e_a · e_b` for `a ≤ b`.  A signed permutation sends
`e_a · e_b` to `s_a s_b · e_{p a} · e_{p b}`, so it contributes to the trace exactly when
the unordered pair `{p a, p b}` is `{a, b}` again, and then contributes `s_a s_b`.
-/

def symIdx : List (Nat × Nat) :=
  [(0,0), (0,1), (0,2), (0,3), (1,1), (1,2), (1,3), (2,2), (2,3), (3,3)]

/-- Unordered-pair equality, on pairs already given in nondecreasing order. -/
def samePair (x y : Nat) (a b : Nat) : Bool :=
  (x == a && y == b) || (x == b && y == a)

/-- Character of the induced action on `Sym²(ℝ⁴)`. -/
def trSym (g : El4) : Int :=
  isum (symIdx.map (fun ab =>
    if samePair (ap g.1 ab.1) (ap g.1 ab.2) ab.1 ab.2
    then sgn g.2 ab.1 * sgn g.2 ab.2 else 0))

/-- The identity has character 10 — the dimension of `Sym²(ℝ⁴)`. -/
theorem trSym_id : trSym ((0,1,2,3), (false,false,false,false)) = 10 := by decide

/-- **§A7, hypercubic.** `Σ χ = 384 = 1 · 384`: one invariant quadratic form. -/
theorem sum_trSym_hyper : isum (hyper.map trSym) = 384 := by decide

/-- **§A7, native.** `Σ χ = 192 = 2 · 96`: two independent invariant quadratic forms. -/
theorem sum_trSym_native : isum (native.map trSym) = 192 := by decide

/-! ### The fixed basis, exhibited rather than counted

A diagonal quadratic form with entries `v` is invariant under `g` when for every basis pair
the transported coefficient matches.  The two forms below are `diag(1,0,0,0)` — the time
part — and `diag(0,1,1,1)` — the spatial part.  Invariance under the native group is checked
directly, and the failure of the first under the hypercubic group is the countercontrol
showing the two groups really do differ here.
-/

def diagFixed (v : Nat → Int) (g : El4) : Bool :=
  symIdx.all (fun ab =>
    let ga := ap g.1 ab.1
    let gb := ap g.1 ab.2
    let src : Int := if ab.1 == ab.2 then v ab.1 else 0
    let tgt : Int := if ga == gb then v ga else 0
    (sgn g.2 ab.1 * sgn g.2 ab.2 * src) == tgt)

def vTime : Nat → Int := fun i => if i = 0 then 1 else 0
def vSpace : Nat → Int := fun i => if i = 0 then 0 else 1

/-- Both named forms are invariant under the native group. -/
theorem native_fixes_both :
    (native.all (diagFixed vTime)) = true ∧ (native.all (diagFixed vSpace)) = true := by
  decide

/-- Countercontrol: the time form is **not** hypercubic-invariant, so the enlargement from
96 to 384 is what collapses the two-dimensional invariant space to one. -/
theorem hyper_does_not_fix_time : (hyper.all (diagFixed vTime)) = false := by decide

/-! ## §A7b — quadratic invariants of the field strength

`Λ²ℝ⁴` has the six basis bivectors `F_{ab}` for `a < b`; a signed permutation sends `F_{ab}`
to `s_a s_b · F_{p a, p b}`, with an extra minus sign when the images come out in the wrong
order.  `Sym²(Λ²ℝ⁴)` is then 21-dimensional, and the two forms of interest are
`Σ_i F_{0i}²` (electric) and `Σ_{i<j} F_{ij}²` (magnetic).
-/

def wPair : Nat → Nat × Nat
  | 0 => (0,1)
  | 1 => (0,2)
  | 2 => (0,3)
  | 3 => (1,2)
  | 4 => (1,3)
  | _ => (2,3)

/-- Index of the bivector `F_{ab}` for `a < b`. -/
def wIdx (a b : Nat) : Nat :=
  if a = 0 then (if b = 1 then 0 else if b = 2 then 1 else 2)
  else if a = 1 then (if b = 2 then 3 else 4)
  else 5

/-- Image index and sign of basis bivector `k` under `g`. -/
def wImg (g : El4) (k : Nat) : Nat × Int :=
  let ab := wPair k
  let ga := ap g.1 ab.1
  let gb := ap g.1 ab.2
  let s := sgn g.2 ab.1 * sgn g.2 ab.2
  if ga < gb then (wIdx ga gb, s) else (wIdx gb ga, -s)

def symWIdx : List (Nat × Nat) :=
  [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5),
   (1,1), (1,2), (1,3), (1,4), (1,5),
   (2,2), (2,3), (2,4), (2,5),
   (3,3), (3,4), (3,5),
   (4,4), (4,5), (5,5)]

/-- Character of the induced action on `Sym²(Λ²ℝ⁴)`. -/
def trWedge (g : El4) : Int :=
  isum (symWIdx.map (fun ij =>
    let a := wImg g ij.1
    let b := wImg g ij.2
    if samePair a.1 b.1 ij.1 ij.2 then a.2 * b.2 else 0))

/-- The identity has character 21 — the dimension of `Sym²(Λ²ℝ⁴)`. -/
theorem trWedge_id : trWedge ((0,1,2,3), (false,false,false,false)) = 21 := by decide

/-- **§A7b, hypercubic.** `Σ χ = 384 = 1 · 384`: a single quadratic invariant, which is why
the Euclidean regulator ties the electric and magnetic normalizations together. -/
theorem sum_trWedge_hyper : isum (hyper.map trWedge) = 384 := by decide

/-- **§A7b, native.** `Σ χ = 192 = 2 · 96`: two independent quadratic invariants, so the
electric and magnetic normalizations are *not* locked by the native symmetry alone. -/
theorem sum_trWedge_native : isum (native.map trWedge) = 192 := by decide

def wedgeFixed (v : Nat → Int) (g : El4) : Bool :=
  symWIdx.all (fun ij =>
    let a := wImg g ij.1
    let b := wImg g ij.2
    let src : Int := if ij.1 == ij.2 then v ij.1 else 0
    let tgt : Int := if a.1 == b.1 then v a.1 else 0
    (a.2 * b.2 * src) == tgt)

/-- `Σ_i F_{0i}²` — the electric form. -/
def vElectric : Nat → Int := fun k => if (wPair k).1 = 0 then 1 else 0
/-- `Σ_{i<j} F_{ij}²` — the magnetic form. -/
def vMagnetic : Nat → Int := fun k => if (wPair k).1 = 0 then 0 else 1

/-- Both field-strength forms are invariant under the native group: this is the basis the
roadmap names, exhibited rather than inferred from a dimension count. -/
theorem native_fixes_EB :
    (native.all (wedgeFixed vElectric)) = true ∧
    (native.all (wedgeFixed vMagnetic)) = true := by decide

/-- Countercontrol: the electric form is not hypercubic-invariant. Under the larger group
only the sum survives, which is precisely the regulator locking the two normalizations. -/
theorem hyper_does_not_fix_electric :
    (hyper.all (wedgeFixed vElectric)) = false := by decide

end Regulator
