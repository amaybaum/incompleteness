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

  THE NAME IS CERTIFIED, NOT ASSERTED. `isRot_iff` proves that the image of `linkAct` is exactly
  the set of antipode-preserving permutations of the six signed links whose `3 × 3` signed
  permutation matrix has determinant `+1` — the definition of a rotation. `card_sym` counts the
  full antipode-preserving group at 48 (`O_h`), `card_rot` counts the rotations at 24 (`O`), and
  `antiPerm_not_isRot` certifies that the inversion `-I`, the element separating them, is absent.
  Naming a group object after the geometry it is supposed to be is exactly the step that failed
  before, so it is now a theorem.

  THE ACCEPTANCE GATE is `character_gate`: the fixed-link character of this action is
  `(6, 0, 2, 0, 2)` on `(E, 8C₃, 3C₂, 6C₂', 6C₄)`, which is [SM] Theorem 7's own proof line. It
  fires BEFORE any representation theory is reconnected, because its absence is what let the wrong
  `S₄`-set through the first time.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.LinkDecomposition
import OIBridge.Averaging
import Mathlib.GroupTheory.Perm.Fin
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.RepresentationTheory.Subrepresentation

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

/-! ### The image is EXACTLY the rotation group

Calling `linkAct` "the cubic rotation action" is a naming claim, and this project has already been
burned once by a group object that carried the wrong name. So the name is certified rather than
asserted: a signed permutation of the three coordinate axes is a rotation exactly when its `3 × 3`
matrix has determinant `+1`, and the image of `linkAct` is proved to be precisely that set.

The determinant is computed in the coordinates `Link = (axis, orientation)` — a relabelling of the
axes or a flip of which orientation is `true` conjugates `linkMat` by a signed permutation matrix
and so leaves `detLink` alone, which is why the criterion does not depend on the arbitrary choices
inside `qtToLink`.

The two guards that follow are the 24-versus-48 check the whole file exists to protect: the full
antipode-preserving group `Sym` has 48 elements — that is `O_h` — the rotation subgroup has 24, and
the inversion `antiPerm = -I`, the element of `O_h` that is not a rotation, is certified absent. -/

/-- The `3 × 3` integer matrix of a permutation of the signed links: column `j` is the image of the
positive `j`-axis, written as a signed unit vector. -/
def linkMat (h : Perm Link) : Matrix (Fin 3) (Fin 3) ℤ := fun i j =>
  if (h (j, true)).1 = i then (if (h (j, true)).2 then 1 else -1) else 0

/-- The determinant of that matrix, written out so that it evaluates in the kernel. -/
def detLink (h : Perm Link) : ℤ :=
  linkMat h 0 0 * (linkMat h 1 1 * linkMat h 2 2 - linkMat h 1 2 * linkMat h 2 1)
    - linkMat h 0 1 * (linkMat h 1 0 * linkMat h 2 2 - linkMat h 1 2 * linkMat h 2 0)
    + linkMat h 0 2 * (linkMat h 1 0 * linkMat h 2 1 - linkMat h 1 1 * linkMat h 2 0)

/-- The explicit formula is Mathlib's determinant; the expansion is written by hand only so that
`decide` can evaluate it. -/
theorem detLink_eq_det (h : Perm Link) : detLink h = (linkMat h).det := by
  rw [Matrix.det_fin_three]
  unfold detLink
  ring

/-- **A rotation of the signed links**: it preserves antipodality and has determinant `+1`. -/
def IsRot (h : Perm Link) : Prop := Sym h ∧ detLink h = 1

instance : DecidablePred IsRot := fun h =>
  inferInstanceAs (Decidable ((∀ l, h (anti l) = anti (h l)) ∧ detLink h = 1))

/-- Every element of the image is a rotation. -/
theorem detLink_linkAct : ∀ g : Perm (Fin 4), detLink (linkAct g) = 1 := by decide

theorem isRot_linkAct (g : Perm (Fin 4)) : IsRot (linkAct g) :=
  ⟨sym_linkAct g, detLink_linkAct g⟩

instance : DecidablePred (fun h : Perm Link => Sym h) := fun h =>
  inferInstanceAs (Decidable (∀ l, h (anti l) = anti (h l)))

/-- **`O_h` has 48 elements**: the antipode-preserving permutations of the six signed links. -/
theorem card_sym : (Finset.univ.filter fun h : Perm Link => Sym h).card = 48 := by decide

/-- **`O` has 24**: its orientation-preserving half. -/
theorem card_rot : (Finset.univ.filter IsRot).card = 24 := by decide

/-- **The inversion is not a rotation.** `antiPerm` is `-I`; it lies in `O_h` and not in `O`, and
this is the concrete form of the guard that `O_h` is never silently substituted for `O`. -/
theorem detLink_antiPerm : detLink antiPerm = -1 := by decide

theorem antiPerm_not_isRot : ¬ IsRot antiPerm := by
  rintro ⟨-, h⟩
  rw [detLink_antiPerm] at h
  exact absurd h (by decide)

/-- **The image of `linkAct` is exactly the rotation group.** Faithfulness gives an image of 24
elements, all rotations; there are exactly 24 rotations; so the two finsets coincide. -/
theorem linkAct_image_eq_rot :
    Finset.univ.image linkAct = Finset.univ.filter IsRot := by
  refine Finset.eq_of_subset_of_card_le ?_ ?_
  · intro h hh
    obtain ⟨g, -, rfl⟩ := Finset.mem_image.1 hh
    exact Finset.mem_filter.2 ⟨Finset.mem_univ _, isRot_linkAct g⟩
  · rw [card_rot, Finset.card_image_of_injective _ linkAct_injective]
    exact le_of_eq (by decide)

/-- **The certified name**: a permutation of the six signed links is a cubic rotation exactly when
it is one of ours. -/
theorem isRot_iff (h : Perm Link) : IsRot h ↔ ∃ g : Perm (Fin 4), linkAct g = h := by
  constructor
  · intro hh
    have hmem : h ∈ Finset.univ.image linkAct := by
      rw [linkAct_image_eq_rot]
      exact Finset.mem_filter.2 ⟨Finset.mem_univ _, hh⟩
    obtain ⟨g, -, hg⟩ := Finset.mem_image.1 hmem
    exact ⟨g, hg⟩
  · rintro ⟨g, rfl⟩
    exact isRot_linkAct g

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

/-! ### The six-link representation

Built on `linkAct` — the action the gate certified — and given a fresh name so that neither Lean
nor a reader can confuse it with `OIBridge.lean`'s retained two-subset control. `permOp` is an
anti-homomorphism (`LinkDecomposition.permOp_mul`), so the representation carries the INVERSE.

`sym_linkAct` gives commutation with all three projectors immediately, so `LinkDecomposition`'s
projector algebra and its `3, 2, 1` dimensions carry over with no mathematical reproof. -/

open OIBridge.IdempotentTrace

/-- **`V₆`, the six-link representation of the cubic rotation group.** -/
noncomputable def rhoLinkQT : Representation ℚ (Perm (Fin 4)) LV where
  toFun g := permOp (linkAct g⁻¹)
  map_one' := by rw [inv_one, map_one, permOp_one]; rfl
  map_mul' g h := by rw [mul_inv_rev, map_mul, permOp_mul]; rfl

theorem rhoLinkQT_apply (g : Perm (Fin 4)) : rhoLinkQT g = permOp (linkAct g⁻¹) := rfl

theorem character_rhoLinkQT (g : Perm (Fin 4)) : rhoLinkQT.character g = (fixLink g⁻¹ : ℚ) := by
  rw [Representation.character, rhoLinkQT_apply, trace_permOp]
  rfl

theorem rhoLinkQT_comm_PT (g : Perm (Fin 4)) : rhoLinkQT g ∘ₗ PT = PT ∘ₗ rhoLinkQT g :=
  permOp_comp_PT (sym_linkAct g⁻¹)

theorem rhoLinkQT_comm_PE (g : Perm (Fin 4)) : rhoLinkQT g ∘ₗ PE = PE ∘ₗ rhoLinkQT g :=
  permOp_comp_PE (sym_linkAct g⁻¹)

theorem rhoLinkQT_comm_PA (g : Perm (Fin 4)) : rhoLinkQT g ∘ₗ PA = PA ∘ₗ rhoLinkQT g :=
  permOp_comp_PA (linkAct g⁻¹)

/-- The three summands, bundled under the CORRECT representation. Fresh objects: the ones in
`OIBridge.lean` are tied to the two-subset action and are not carried across. -/
noncomputable def TsubQT : Subrepresentation rhoLinkQT where
  toSubmodule := LinearMap.range PT
  apply_mem_toSubmodule g _ hv := mapsTo_range (rhoLinkQT_comm_PT g) _ hv

noncomputable def EsubQT : Subrepresentation rhoLinkQT where
  toSubmodule := LinearMap.range PE
  apply_mem_toSubmodule g _ hv := mapsTo_range (rhoLinkQT_comm_PE g) _ hv

noncomputable def AsubQT : Subrepresentation rhoLinkQT where
  toSubmodule := LinearMap.range PA
  apply_mem_toSubmodule g _ hv := mapsTo_range (rhoLinkQT_comm_PA g) _ hv

noncomputable def rhoT : Representation ℚ (Perm (Fin 4)) TsubQT.toSubmodule :=
  TsubQT.toRepresentation
noncomputable def rhoE : Representation ℚ (Perm (Fin 4)) EsubQT.toSubmodule :=
  EsubQT.toRepresentation
noncomputable def rhoA : Representation ℚ (Perm (Fin 4)) AsubQT.toSubmodule :=
  AsubQT.toRepresentation

/-- Each summand's character is `charOn`, through the trace lemma. -/
theorem character_rhoT (g : Perm (Fin 4)) : rhoT.character g = charOn PT (linkAct g⁻¹) :=
  trace_restrict_range PT_idem (rhoLinkQT_comm_PT g)

theorem character_rhoE (g : Perm (Fin 4)) : rhoE.character g = charOn PE (linkAct g⁻¹) :=
  trace_restrict_range PE_idem (rhoLinkQT_comm_PE g)

theorem character_rhoA (g : Perm (Fin 4)) : rhoA.character g = charOn PA (linkAct g⁻¹) :=
  trace_restrict_range PA_comp_PA (rhoLinkQT_comm_PA g)

/-- The three dimensions, carried over unchanged from `LinkDecomposition`. -/
theorem finrank_rhoT : Module.finrank ℚ TsubQT.toSubmodule = 3 := finrank_PT
theorem finrank_rhoE : Module.finrank ℚ EsubQT.toSubmodule = 2 := finrank_PE
theorem finrank_rhoA : Module.finrank ℚ AsubQT.toSubmodule = 1 := finrank_PA

/-! ### The character table of `O ≅ S₄` -/

/-- Links sent to their antipodes; with `fixLink` this gives the odd summand's character. -/
def fixLA (g : Perm (Fin 4)) : ℕ :=
  (Finset.univ.filter fun l => (antiPerm * linkAct g⁻¹) l = l).card

/-- Fixed axes. -/
def fix3 (g : Perm (Fin 4)) : ℕ :=
  (Finset.univ.filter fun a : Fin 3 => (linkAct g (a, false)).1 = a).card

/-- The sign, as inversion parity. -/
def sgnZ (g : Perm (Fin 4)) : ℤ :=
  if (Finset.univ.filter fun p : Fin 4 × Fin 4 => p.1 < p.2 ∧ g p.2 < g p.1).card % 2 = 0
  then 1 else -1

theorem sgnZ_eq_sign (g : Perm (Fin 4)) : sgnZ g = (Equiv.Perm.sign g : ℤ) := by
  revert g; decide

def chiA1 (_ : Perm (Fin 4)) : ℤ := 1
def chiA2 (g : Perm (Fin 4)) : ℤ := sgnZ g
def chiE (g : Perm (Fin 4)) : ℤ := (fix3 g : ℤ) - 1
/-- `T₁` is standard ⊗ sign, NOT the standard representation: a four-fold rotation is an odd
permutation, so `χ_std(4-cycle) = −1` while `χ_{T₁}(6C₄) = +1`. Writing this as `fix₄ − 1` would
leave every inner product unchanged and swap the two three-dimensional labels. -/
def chiT1 (g : Perm (Fin 4)) : ℤ := sgnZ g * ((nfix g : ℤ) - 1)
def chiT2 (g : Perm (Fin 4)) : ℤ := (nfix g : ℤ) - 1

def irrChars : List (Perm (Fin 4) → ℤ) := [chiA1, chiA2, chiE, chiT1, chiT2]

/-- **The five characters are orthonormal.** This is what makes them the irreducible characters. -/
theorem irr_orthonormal :
    irrChars.map (fun a => irrChars.map (fun b => ∑ g : Perm (Fin 4), a g * b g))
      = [[24, 0, 0, 0, 0], [0, 24, 0, 0, 0], [0, 0, 24, 0, 0],
         [0, 0, 0, 24, 0], [0, 0, 0, 0, 24]] := by decide

/-- **The multiplicities of `V₆`**, against the DERIVED character `chiLink` rather than a
transcription: `⟨χ₆, χᵢ⟩ = 24·(1, 0, 1, 1, 0)`. No `A₂`, no `T₂`. -/
theorem mult_link :
    irrChars.map (fun c => ∑ g : Perm (Fin 4), chiLink g * c g) = [24, 0, 24, 24, 0] := by decide

/-- The character of `V₆` splits as `T₁ + E + A₁`, pointwise. -/
theorem chiLink_split : ∀ g : Perm (Fin 4), chiLink g = chiT1 g + chiE g + chiA1 g := by decide

/-- The two fixed-point counts of the odd summand give exactly `2·χ_{T₁}`. -/
theorem fix_diff_eq :
    ∀ g : Perm (Fin 4), (fixLink g⁻¹ : ℤ) - (fixLA g : ℤ) = 2 * chiT1 g := by decide

theorem chi_inv : ∀ g : Perm (Fin 4), chiT1 g⁻¹ = chiT1 g ∧ chiE g⁻¹ = chiE g := by decide

/-- The character of `V₆` is a class function, so it is unchanged on inverses. -/
theorem chiLink_inv : ∀ g : Perm (Fin 4), chiLink g⁻¹ = chiLink g := by decide

theorem card_group : Nat.card (Perm (Fin 4)) = 24 := by
  rw [Nat.card_eq_fintype_card, Fintype.card_perm, Fintype.card_fin]
  rfl

/- Local so it cannot collide with the equivalent instance in `OIBridge.lean`'s `Cubic` section,
which is downstream of this file. -/
noncomputable local instance : Invertible ((Nat.card (Perm (Fin 4)) : ℚ)) :=
  invertibleOfNonzero (by rw [card_group]; norm_num)

/-! ### The summands are `T₁`, `E` and `A₁` -/

theorem character_rhoA_eq (g : Perm (Fin 4)) : rhoA.character g = (chiA1 g : ℚ) := by
  rw [character_rhoA, charOn_PA]; rfl

theorem character_rhoT_eq (g : Perm (Fin 4)) : rhoT.character g = (chiT1 g : ℚ) := by
  rw [character_rhoT, charOn_PT, trace_permOp, trace_permOp]
  have h : ((fixLink g⁻¹ : ℤ) : ℚ) - ((fixLA g : ℤ) : ℚ) = ((2 * chiT1 g : ℤ) : ℚ) := by
    exact_mod_cast congrArg (fun z : ℤ => (z : ℚ)) (fix_diff_eq g)
  push_cast at h
  show (1 / 2 : ℚ) * ((fixLink g⁻¹ : ℚ) - (fixLA g : ℚ)) = (chiT1 g : ℚ)
  linarith

/-- `χ_E` is derived, not recomputed: the full character splits and the other two are identified. -/
theorem character_rhoE_eq (g : Perm (Fin 4)) : rhoE.character g = (chiE g : ℚ) := by
  have hsum : rhoT.character g + rhoE.character g + rhoA.character g
      = (chiLink g : ℚ) := by
    rw [character_rhoT, character_rhoE, character_rhoA, charOn_sum, trace_permOp,
      show (Finset.univ.filter fun l => linkAct g⁻¹ l = l).card = fixLink g⁻¹ from rfl]
    rw [← chiLink_inv g]
    exact_mod_cast congrArg (fun z : ℤ => (z : ℚ)) (character_gate g⁻¹)
  rw [character_rhoT_eq, character_rhoA_eq] at hsum
  have hsplit : ((chiLink g : ℤ) : ℚ) = (chiT1 g : ℚ) + (chiE g : ℚ) + (chiA1 g : ℚ) := by
    exact_mod_cast congrArg (fun z : ℤ => (z : ℚ)) (chiLink_split g)
  linarith

/-! ### Irreducibility, over ℚ

`A₁` is one-dimensional and irreducible outright. For the other two the self-inner-product is `24`,
and `finrank_intertwiners` turns that into an endomorphism algebra of dimension one — Schur over ℚ
by Maschke, with no algebraically closed field and no complexification. -/

theorem sum_chiT1_sq : ∑ g : Perm (Fin 4), chiT1 g * chiT1 g⁻¹ = 24 := by decide

theorem sum_chiE_sq : ∑ g : Perm (Fin 4), chiE g * chiE g⁻¹ = 24 := by decide

theorem sum_chiA1_sq : ∑ g : Perm (Fin 4), chiA1 g * chiA1 g⁻¹ = 24 := by decide

/-- **The labelling certificate.** `T₁` and `T₂` are separated exactly at the four-fold class:
`χ_{T₁}(6C₄) = 1` and `χ_{T₂}(6C₄) = −1`. The summand's character is `χ_{T₁}`, so the
three-dimensional constituent is `T₁` and not `T₂`. -/
theorem chiT_c4 :
    chiT1 ⟨![1, 2, 3, 0], ![3, 0, 1, 2], by decide, by decide⟩ = 1 ∧
      chiT2 ⟨![1, 2, 3, 0], ![3, 0, 1, 2], by decide, by decide⟩ = -1 := by
  refine ⟨by decide, by decide⟩

theorem finrank_end_rhoT : Module.finrank ℚ (Representation.IntertwiningMap rhoT rhoT) = 1 := by
  have h := finrank_intertwiners rhoT rhoT
  rw [card_group] at h
  have hc : ∑ g : Perm (Fin 4), rhoT.character g * rhoT.character g⁻¹ = (24 : ℚ) := by
    have hterm : ∀ g : Perm (Fin 4), rhoT.character g * rhoT.character g⁻¹
        = ((chiT1 g * chiT1 g⁻¹ : ℤ) : ℚ) := by
      intro g; rw [character_rhoT_eq, character_rhoT_eq]; push_cast; ring
    rw [Finset.sum_congr rfl fun g _ => hterm g, ← Int.cast_sum, sum_chiT1_sq]
    norm_num
  rw [hc] at h
  field_simp at h
  have h' : (24 : ℕ) * Module.finrank ℚ (Representation.IntertwiningMap rhoT rhoT) = 24 := by
    exact_mod_cast h
  omega

theorem finrank_end_rhoA : Module.finrank ℚ (Representation.IntertwiningMap rhoA rhoA) = 1 := by
  have h := finrank_intertwiners rhoA rhoA
  rw [card_group] at h
  have hc : ∑ g : Perm (Fin 4), rhoA.character g * rhoA.character g⁻¹ = (24 : ℚ) := by
    have hterm : ∀ g : Perm (Fin 4), rhoA.character g * rhoA.character g⁻¹
        = ((chiA1 g * chiA1 g⁻¹ : ℤ) : ℚ) := by
      intro g; rw [character_rhoA_eq, character_rhoA_eq]; push_cast; ring
    rw [Finset.sum_congr rfl fun g _ => hterm g, ← Int.cast_sum, sum_chiA1_sq]
    norm_num
  rw [hc] at h
  field_simp at h
  have h' : (24 : ℕ) * Module.finrank ℚ (Representation.IntertwiningMap rhoA rhoA) = 24 := by
    exact_mod_cast h
  omega

theorem finrank_end_rhoE : Module.finrank ℚ (Representation.IntertwiningMap rhoE rhoE) = 1 := by
  have h := finrank_intertwiners rhoE rhoE
  rw [card_group] at h
  have hc : ∑ g : Perm (Fin 4), rhoE.character g * rhoE.character g⁻¹ = (24 : ℚ) := by
    have hterm : ∀ g : Perm (Fin 4), rhoE.character g * rhoE.character g⁻¹
        = ((chiE g * chiE g⁻¹ : ℤ) : ℚ) := by
      intro g; rw [character_rhoE_eq, character_rhoE_eq]; push_cast; ring
    rw [Finset.sum_congr rfl fun g _ => hterm g, ← Int.cast_sum, sum_chiE_sq]
    norm_num
  rw [hc] at h
  field_simp at h
  have h' : (24 : ℕ) * Module.finrank ℚ (Representation.IntertwiningMap rhoE rhoE) = 24 := by
    exact_mod_cast h
  omega

/-! ### The terminal equivariant decomposition

Not a conjunction: an actual `S₄`-equivariant linear equivalence `V₆ ≃ T₁ ⊕ E ⊕ A₁`, given by
`v ↦ (P_T v, P_E v, P_A v)` with inverse `(t, e, a) ↦ t + e + a`. -/

theorem mem_range_PT_apply {x : LV} (h : x ∈ LinearMap.range PT) : PT x = x :=
  apply_eq_self_of_mem_range PT_idem h

theorem mem_range_PE_apply {x : LV} (h : x ∈ LinearMap.range PE) : PE x = x :=
  apply_eq_self_of_mem_range PE_idem h

theorem mem_range_PA_apply {x : LV} (h : x ∈ LinearMap.range PA) : PA x = x :=
  apply_eq_self_of_mem_range PA_comp_PA h

/-- **`V₆ ≃ T₁ ⊕ E ⊕ A₁`.** -/
noncomputable def decompEquiv :
    LV ≃ₗ[ℚ] (TsubQT.toSubmodule × EsubQT.toSubmodule × AsubQT.toSubmodule) where
  toFun v := (⟨PT v, ⟨v, rfl⟩⟩, ⟨PE v, ⟨v, rfl⟩⟩, ⟨PA v, ⟨v, rfl⟩⟩)
  map_add' u v := by
    refine Prod.ext (Subtype.ext ?_) (Prod.ext (Subtype.ext ?_) (Subtype.ext ?_)) <;> simp
  map_smul' c v := by
    refine Prod.ext (Subtype.ext ?_) (Prod.ext (Subtype.ext ?_) (Subtype.ext ?_)) <;> simp
  invFun p := (p.1 : LV) + (p.2.1 : LV) + (p.2.2 : LV)
  left_inv v := by
    show PT v + PE v + PA v = v
    have := congrArg (fun f : LV →ₗ[ℚ] LV => f v) sum_proj
    simpa using this
  right_inv p := by
    obtain ⟨⟨t, ht⟩, ⟨e, he⟩, ⟨a, ha⟩⟩ := p
    have hPTe : PT e = 0 := by
      obtain ⟨y, rfl⟩ := he
      exact congrArg (fun f : LV →ₗ[ℚ] LV => f y) PT_comp_PE
    have hPTa : PT a = 0 := by
      obtain ⟨y, rfl⟩ := ha
      exact congrArg (fun f : LV →ₗ[ℚ] LV => f y) PT_comp_PA
    have hPEt : PE t = 0 := by
      obtain ⟨y, rfl⟩ := ht
      exact congrArg (fun f : LV →ₗ[ℚ] LV => f y) PE_comp_PT
    have hPEa : PE a = 0 := by
      obtain ⟨y, rfl⟩ := ha
      exact congrArg (fun f : LV →ₗ[ℚ] LV => f y) PE_comp_PA
    have hPAt : PA t = 0 := by
      obtain ⟨y, rfl⟩ := ht
      exact congrArg (fun f : LV →ₗ[ℚ] LV => f y) PA_comp_PT
    have hPAe : PA e = 0 := by
      obtain ⟨y, rfl⟩ := he
      exact congrArg (fun f : LV →ₗ[ℚ] LV => f y) PA_comp_PE
    refine Prod.ext (Subtype.ext ?_) (Prod.ext (Subtype.ext ?_) (Subtype.ext ?_))
    · show PT (t + e + a) = t
      rw [map_add, map_add, hPTe, hPTa, mem_range_PT_apply ht, add_zero, add_zero]
    · show PE (t + e + a) = e
      rw [map_add, map_add, hPEt, hPEa, mem_range_PE_apply he, zero_add, add_zero]
    · show PA (t + e + a) = a
      rw [map_add, map_add, hPAt, hPAe, mem_range_PA_apply ha, zero_add, zero_add]

/-- **…and it is `S₄`-EQUIVARIANT.** Each component intertwines the six-link representation with
the corresponding summand's own representation, which is what makes this a decomposition of
representations and not merely of vector spaces. -/
theorem decompEquiv_equivariant (g : Perm (Fin 4)) (v : LV) :
    decompEquiv (rhoLinkQT g v)
      = (rhoT g (decompEquiv v).1, rhoE g (decompEquiv v).2.1, rhoA g (decompEquiv v).2.2) := by
  refine Prod.ext (Subtype.ext ?_) (Prod.ext (Subtype.ext ?_) (Subtype.ext ?_))
  · show PT (rhoLinkQT g v) = rhoLinkQT g (PT v)
    exact (congrArg (fun f : LV →ₗ[ℚ] LV => f v) (rhoLinkQT_comm_PT g)).symm
  · show PE (rhoLinkQT g v) = rhoLinkQT g (PE v)
    exact (congrArg (fun f : LV →ₗ[ℚ] LV => f v) (rhoLinkQT_comm_PE g)).symm
  · show PA (rhoLinkQT g v) = rhoLinkQT g (PA v)
    exact (congrArg (fun f : LV →ₗ[ℚ] LV => f v) (rhoLinkQT_comm_PA g)).symm

/-! ### Theorem 7 -/

/-- **Theorem 7 (exact six-link representation), [SM] §4.1.**

The six signed simple-cubic links decompose under the cubic rotation group as
`V₆ ≅ T₁(3) ⊕ E(2) ⊕ A₁(1)`. The equivalence is explicit and equivariant; the three summands are
irreducible over ℚ, with dimensions `3, 2, 1`; their characters are `χ_{T₁}`, `χ_E`, `χ_{A₁}`; and
the whole character is the manuscript's `(6, 0, 2, 0, 2)`.

The action is the cubic ROTATION action, and that is certified twice over rather than asserted:
`isRot_iff` proves the acting group is EXACTLY the antipode-preserving permutations of the six
signed links with determinant `+1`, `card_rot` counts them as 24 rather than `O_h`'s 48, and
`character_gate` reproduces the manuscript's own character line before any representation theory
was attached.

This is geometry: the physical-carrier identification is **H-link**, a separate premise, and
appears only in `LinkDecomposition.hlink_transport`. -/
theorem theorem_7_link :
    (∀ h : Perm Link, IsRot h ↔ ∃ g : Perm (Fin 4), linkAct g = h) ∧
    (Finset.univ.filter IsRot).card = 24 ∧
    (∀ g : Perm (Fin 4), (fixLink g : ℤ) = chiLink g) ∧
    (∀ g : Perm (Fin 4), rhoT.character g = (chiT1 g : ℚ) ∧ rhoE.character g = (chiE g : ℚ) ∧
      rhoA.character g = (chiA1 g : ℚ)) ∧
    (Module.finrank ℚ TsubQT.toSubmodule = 3 ∧ Module.finrank ℚ EsubQT.toSubmodule = 2 ∧
      Module.finrank ℚ AsubQT.toSubmodule = 1) ∧
    (Module.finrank ℚ (Representation.IntertwiningMap rhoT rhoT) = 1 ∧
      Module.finrank ℚ (Representation.IntertwiningMap rhoE rhoE) = 1 ∧
      Module.finrank ℚ (Representation.IntertwiningMap rhoA rhoA) = 1) ∧
    (∀ g : Perm (Fin 4), ∀ v : LV, decompEquiv (rhoLinkQT g v)
      = (rhoT g (decompEquiv v).1, rhoE g (decompEquiv v).2.1, rhoA g (decompEquiv v).2.2)) :=
  ⟨isRot_iff, card_rot, character_gate,
   fun g => ⟨character_rhoT_eq g, character_rhoE_eq g, character_rhoA_eq g⟩,
   ⟨finrank_rhoT, finrank_rhoE, finrank_rhoA⟩,
   ⟨finrank_end_rhoT, finrank_end_rhoE, finrank_end_rhoA⟩,
   decompEquiv_equivariant⟩

/-! ### What these proofs rest on -/

#print axioms card_QT
#print axioms conjHom
#print axioms qtEquivLink_inv
#print axioms sym_linkAct
#print axioms linkAct_injective
#print axioms detLink_eq_det
#print axioms card_sym
#print axioms card_rot
#print axioms antiPerm_not_isRot
#print axioms isRot_iff
#print axioms character_gate
#print axioms character_values
#print axioms character_rhoLinkQT
#print axioms character_rhoT_eq
#print axioms character_rhoE_eq
#print axioms character_rhoA_eq
#print axioms irr_orthonormal
#print axioms mult_link
#print axioms finrank_end_rhoT
#print axioms finrank_end_rhoE
#print axioms decompEquiv_equivariant
#print axioms chiT_c4
#print axioms finrank_end_rhoA
#print axioms theorem_7_link

end QuarterTurn

end OIBridge
