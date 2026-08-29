/-
  OIBridge/QuarterTurn.lean — the cubic rotation action on the six signed links, built from the six
  quarter turns.

  THE POINT OF THIS FILE is to supply what `LinkDecomposition` needs and the bridge did not have: a
  GENUINE 24-element rotation group acting on the actual six links, with the CORRECT action. An
  earlier attempt transported `Cubic.rho`'s action on the six two-element subsets of the body
  diagonals; that is a different `S₄`-set, carrying `T₂` where the links carry `T₁`, and
  `OIBridge.lean`'s `LinkJoin` section records the discrepancy and the three reasons the previous
  evidence could not see it.

  THE CONSTRUCTION. The six four-cycles of `S₄` ARE the six quarter turns `±C₄ₓ, ±C₄ᵧ, ±C₄_z`, and
  those are the six oriented axes — the links. `S₄` acts on them by CONJUGATION, which is
  automatically a group action, so no coset quotient has to be formalized: the stabilizer of a
  four-cycle is its centralizer `C₄`, so the orbit is `S₄/C₄` for free. And antipodality is
  canonical, `q ↦ q⁻¹`: a quarter turn and its inverse are the two orientations of one axis. The
  equivalence to `Link` is therefore INVERSE-PRESERVING, which is exactly the hypothesis
  `LinkDecomposition.Sym` asks for, so the projectors' invariance comes back with nothing reproved.

  THE ACCEPTANCE GATE is `character_gate`: the fixed-link character of this action is
  `(6, 0, 2, 0, 2)` on `(E, 8C₃, 3C₂, 6C₂', 6C₄)`, which is [SM] Theorem 7's own proof line. It
  fires BEFORE any representation theory is reconnected, because its absence is what let the wrong
  `S₄`-set through the first time.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.LinkDecomposition
import Mathlib.GroupTheory.Perm.Fin

namespace OIBridge

namespace QuarterTurn

open Equiv OIBridge.LinkDecomposition

/- Several statements below are decided by evaluation over the six quarter turns or the 24 group
elements. The recursion limit is raised file-wide for the same reason as elsewhere in this project:
it bounds the evaluator's depth, not the trusted base, and `native_decide` is deliberately never
used here — it would put the Lean compiler in the trusted base. -/
set_option maxRecDepth 200000

/-! ### The six quarter turns

In `S₄` the elements of order four are exactly the four-cycles, and `q⁴ = 1` with `q² ≠ 1` picks
them out: it excludes the three-cycles (order three), the identity and both classes of involutions. -/

/-- A quarter turn: an element of order four in `S₄`. -/
def IsQT (q : Perm (Fin 4)) : Prop := q ^ 4 = 1 ∧ q ^ 2 ≠ 1

instance : DecidablePred IsQT := fun q => inferInstanceAs (Decidable (q ^ 4 = 1 ∧ q ^ 2 ≠ 1))

/-- The six quarter turns. -/
abbrev QT := {q : Perm (Fin 4) // IsQT q}

theorem card_QT : Fintype.card QT = 6 := by decide

/-! ### Conjugation, and the antipode

Conjugation is a group action with no work, and the centralizer of a four-cycle in `S₄` is the
cyclic group it generates — order four — so the orbit has six elements and is `S₄/C₄` without a
quotient ever being formalized. -/

theorem isQT_conj (g : Perm (Fin 4)) {q : Perm (Fin 4)} (h : IsQT q) : IsQT (MulAut.conj g q) := by
  refine ⟨?_, ?_⟩
  · rw [← map_pow, h.1, map_one]
  · rw [← map_pow]
    intro hc
    exact h.2 ((MulAut.conj g).injective (hc.trans (map_one (MulAut.conj g)).symm))

/-- The conjugation action on the quarter turns. -/
def conjQT (g : Perm (Fin 4)) (q : QT) : QT := ⟨MulAut.conj g q.1, isQT_conj g q.2⟩

theorem conjQT_one (q : QT) : conjQT 1 q = q := by
  refine Subtype.ext ?_
  simp [conjQT]

theorem conjQT_mul (g h : Perm (Fin 4)) (q : QT) : conjQT (g * h) q = conjQT g (conjQT h q) := by
  refine Subtype.ext ?_
  simp [conjQT, map_mul]

/-- The action as a permutation of the six quarter turns. -/
def conjPerm (g : Perm (Fin 4)) : Perm QT where
  toFun := conjQT g
  invFun := conjQT g⁻¹
  left_inv q := by rw [← conjQT_mul, inv_mul_cancel, conjQT_one]
  right_inv q := by rw [← conjQT_mul, mul_inv_cancel, conjQT_one]

/-- …and as a genuine group homomorphism, so this is an action of `S₄` and not a family of maps. -/
def conjHom : Perm (Fin 4) →* Perm QT where
  toFun := conjPerm
  map_one' := Equiv.ext fun q => conjQT_one q
  map_mul' g h := Equiv.ext fun q => conjQT_mul g h q

theorem conjHom_apply (g : Perm (Fin 4)) (q : QT) : conjHom g q = conjQT g q := rfl

/-- **The antipode**: a quarter turn and its inverse are the two orientations of one axis. -/
theorem isQT_inv {q : Perm (Fin 4)} (h : IsQT q) : IsQT q⁻¹ := by
  refine ⟨?_, ?_⟩
  · rw [inv_pow, h.1, inv_one]
  · rw [inv_pow]
    intro hc
    exact h.2 (inv_eq_one.1 hc)

def qtInv (q : QT) : QT := ⟨q.1⁻¹, isQT_inv q.2⟩

/-- Conjugation commutes with the antipode, which is what makes the transported action a symmetry
of the link set. -/
theorem conjQT_qtInv (g : Perm (Fin 4)) (q : QT) : conjQT g (qtInv q) = qtInv (conjQT g q) := by
  refine Subtype.ext ?_
  simp [conjQT, qtInv, map_inv]

/-! ### The quarter turns ARE the links

The axis of a quarter turn is read off its square — a fixed-point-free involution, one per
coordinate axis — and the orientation separates `q` from `q⁻¹`. -/

/-- The axis of a quarter turn, read off `q²`. -/
def qtAxis (q : QT) : Fin 3 :=
  if q.1 (q.1 0) = 1 then 0 else if q.1 (q.1 0) = 2 then 1 else 2

/-- The orientation, separating `q` from `q⁻¹`. -/
def qtSign (q : QT) : Bool := decide (q.1⁻¹ 0 < q.1 0)

def qtToLink (q : QT) : Link := (qtAxis q, qtSign q)

/-- The six quarter turns, listed. Given explicitly so the equivalence stays computable and the
character gate can be decided. -/
def linkToQT (l : Link) : QT :=
  if l.1 = 0 then
    (if l.2 then ⟨⟨![3, 2, 0, 1], ![2, 3, 1, 0], by decide, by decide⟩, by decide⟩
     else ⟨⟨![2, 3, 1, 0], ![3, 2, 0, 1], by decide, by decide⟩, by decide⟩)
  else if l.1 = 1 then
    (if l.2 then ⟨⟨![3, 0, 1, 2], ![1, 2, 3, 0], by decide, by decide⟩, by decide⟩
     else ⟨⟨![1, 2, 3, 0], ![3, 0, 1, 2], by decide, by decide⟩, by decide⟩)
  else
    (if l.2 then ⟨⟨![2, 0, 3, 1], ![1, 3, 0, 2], by decide, by decide⟩, by decide⟩
     else ⟨⟨![1, 3, 0, 2], ![2, 0, 3, 1], by decide, by decide⟩, by decide⟩)

/-- **The six quarter turns are the six links.** -/
def qtEquivLink : QT ≃ Link :=
  ⟨qtToLink, linkToQT, by decide, by decide⟩

/-- **The equivalence is inverse-preserving**: `q⁻¹` is the antipodal link. This is the property the
whole construction turns on, and it is what `LinkDecomposition.Sym` consumes. -/
theorem qtEquivLink_inv (q : QT) : qtEquivLink (qtInv q) = anti (qtEquivLink q) := by
  revert q; decide

/-! ### The rotation action on the links -/

/-- **The cubic rotation action on the six signed links.** -/
def linkAct : Perm (Fin 4) →* Perm Link where
  toFun g := (qtEquivLink.symm.trans (conjHom g)).trans qtEquivLink
  map_one' := by
    refine Equiv.ext fun l => ?_
    simp [map_one]
  map_mul' g h := by
    refine Equiv.ext fun l => ?_
    simp [map_mul, Perm.mul_apply]

theorem linkAct_apply (g : Perm (Fin 4)) (l : Link) :
    linkAct g l = qtEquivLink (conjQT g (qtEquivLink.symm l)) := rfl

/-- **Every rotation is a symmetry of the link set**, from inverse-preservation and the fact that
conjugation commutes with inversion. Proved structurally, with no enumeration over the group, so
`LinkDecomposition`'s three projectors are invariant under this action with none of their algebra
reproved. -/
theorem sym_linkAct (g : Perm (Fin 4)) : Sym (linkAct g) := by
  intro l
  have hl : qtEquivLink.symm (anti l) = qtInv (qtEquivLink.symm l) := by
    refine qtEquivLink.injective ?_
    rw [Equiv.apply_symm_apply, qtEquivLink_inv, Equiv.apply_symm_apply]
  rw [linkAct_apply, linkAct_apply, hl, conjQT_qtInv, qtEquivLink_inv]

/-- The action is faithful: `S₄` has trivial centre, so conjugation is. -/
theorem linkAct_injective : Function.Injective linkAct := by
  intro g h hgh
  have hq : ∀ q : QT, conjQT g q = conjQT h q := by
    intro q
    refine qtEquivLink.injective ?_
    have := congrArg (fun σ => σ (qtEquivLink q)) hgh
    simpa [linkAct_apply, Equiv.symm_apply_apply] using this
  revert hq
  revert g h
  decide

/-! ### The acceptance gate

The fixed-link character of this action, against [SM] Theorem 7's own proof line. Nothing
downstream may be reconnected until this fires: its absence is what let the wrong `S₄`-set through
before. -/

/-- The number of links a rotation fixes — the character of `V₆`. -/
def fixLink (g : Perm (Fin 4)) : ℕ := (Finset.univ.filter fun l => linkAct g l = l).card

/-- The number of diagonals a permutation fixes, used to separate the two involution classes. -/
def nfix (g : Perm (Fin 4)) : ℕ := (Finset.univ.filter fun i : Fin 4 => g i = i).card

/-- **[SM] Theorem 7's character of `V₆`**, as a class function: `6` at the identity, `0` on `8C₃`,
`2` on `3C₂`, `0` on `6C₂'`, `2` on `6C₄`. Under `O ≅ S₄` those classes are the identity, the
three-cycles, the double transpositions, the transpositions and the four-cycles. -/
def chiLink (g : Perm (Fin 4)) : ℤ :=
  if g = 1 then 6
  else if g * g = 1 then (if nfix g = 2 then 0 else 2)
  else if g * g * g = 1 then 0
  else 2

/-- **THE ACCEPTANCE GATE.** The fixed-link character of the conjugation action is exactly the
manuscript's `(6, 0, 2, 0, 2)`. With this the `S₄`-set is confirmed correct BEFORE any
representation theory is reconnected — which is the check whose absence admitted the two-subset
model. -/
theorem character_gate : ∀ g : Perm (Fin 4), (fixLink g : ℤ) = chiLink g := by decide

/-- The gate, read off at one representative of each class, in the manuscript's own order. -/
theorem character_values :
    fixLink 1 = 6 ∧
    fixLink (Equiv.swap 0 1 * Equiv.swap 1 2) = 0 ∧
    fixLink (Equiv.swap 0 1 * Equiv.swap 2 3) = 2 ∧
    fixLink (Equiv.swap 0 1) = 0 ∧
    fixLink ⟨![1, 2, 3, 0], ![3, 0, 1, 2], by decide, by decide⟩ = 2 := by
  refine ⟨by decide, by decide, by decide, by decide, by decide⟩

/-! ### What these proofs rest on -/

#print axioms card_QT
#print axioms conjHom
#print axioms qtEquivLink_inv
#print axioms sym_linkAct
#print axioms linkAct_injective
#print axioms character_gate
#print axioms character_values

end QuarterTurn

end OIBridge
