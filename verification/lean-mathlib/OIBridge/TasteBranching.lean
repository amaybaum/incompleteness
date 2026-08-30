/-
  OIBridge/TasteBranching.lean — [SM] Theorem 8 (taste branching): 4 = 1 ⊕ 3 under the cubic group.

  The 2³ = 8 Brillouin-zone corners `η ∈ 𝔽₂³` pair under `η ↔ 𝟙 − η = η + 𝟙` into four taste
  pairs, and the cubic rotation group splits them 1 + 3: the pair {0, 𝟙} is fixed, the three
  axis pairs form a single orbit.

  THE CARRIER SUBTLETY IS PART OF THE STATEMENT, per the manuscript's own remark. On the corner
  LABELS a rotation acts only through its axis permutation — sign flips are trivial on {0, π}
  momentum components, which is `𝟙 mod 2` here — so the label action on the three axis pairs is
  the S₃ permutation representation, and that is `A₁ ⊕ E`, NOT irreducible: `axis_rep_reducible`
  below exhibits the invariant all-ones line. The irreducible `T₁` of the theorem's "three triplet
  tastes" lives on the SIGNED carrier — the `γʲ`-represented tastes of Theorem 9 — which is the
  vector representation of the rotation group, and that is `QuarterTurn.rhoT`, whose
  irreducibility over ℚ is already in the kernel (`irreducible_rhoT`). This file states the
  branching as its own theorem and wires both carriers to it, rather than reading either off a
  character table.

  The rotation group enters through `QuarterTurn.linkAct`, the action on the six signed links
  already certified to be exactly the 24 rotations; the axis permutation is its orientation
  quotient, well defined because every rotation is a `Sym` of the link set.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.QuarterTurn
import Mathlib.RepresentationTheory.Irreducible

namespace OIBridge

namespace TasteBranching

set_option autoImplicit false
set_option maxRecDepth 200000

open Equiv Representation OIBridge.LinkDecomposition OIBridge.QuarterTurn

/-! ### The axis permutation: the orientation quotient of the link action -/

/-- The transported axis does not depend on the orientation, because every rotation commutes with
the antipode. -/
theorem linkAct_fst_orient (g : Perm (Fin 4)) (j : Fin 3) (s : Bool) :
    (linkAct g (j, s)).1 = (linkAct g (j, !s)).1 := by
  have h := sym_linkAct g (j, s)
  have hanti : anti (j, s) = (j, !s) := rfl
  rw [hanti] at h
  rw [h]
  rfl

/-- **The axis action**: the permutation of the three axes a rotation induces. -/
def axisAct (g : Perm (Fin 4)) : Perm (Fin 3) where
  toFun j := (linkAct g (j, false)).1
  invFun j := (linkAct g⁻¹ (j, false)).1
  left_inv j := by
    have h1 : (linkAct g⁻¹ ((linkAct g (j, false)).1, false)).1
        = (linkAct g⁻¹ ((linkAct g (j, false)).1, (linkAct g (j, false)).2)).1 := by
      rcases hb : (linkAct g (j, false)).2 with _ | _
      · rfl
      · rw [linkAct_fst_orient]
        rfl
    calc (linkAct g⁻¹ ((linkAct g (j, false)).1, false)).1
        = (linkAct g⁻¹ (linkAct g (j, false))).1 := by rw [h1]
      _ = j := by
          rw [show linkAct g⁻¹ (linkAct g (j, false)) = ((linkAct g⁻¹) * (linkAct g)) (j, false)
            from rfl, ← map_mul, inv_mul_cancel, map_one]
          rfl
  right_inv j := by
    have h1 : (linkAct g ((linkAct g⁻¹ (j, false)).1, false)).1
        = (linkAct g ((linkAct g⁻¹ (j, false)).1, (linkAct g⁻¹ (j, false)).2)).1 := by
      rcases hb : (linkAct g⁻¹ (j, false)).2 with _ | _
      · rfl
      · rw [linkAct_fst_orient]
        rfl
    calc (linkAct g ((linkAct g⁻¹ (j, false)).1, false)).1
        = (linkAct g (linkAct g⁻¹ (j, false))).1 := by rw [h1]
      _ = j := by
          rw [show linkAct g (linkAct g⁻¹ (j, false)) = ((linkAct g) * (linkAct g⁻¹)) (j, false)
            from rfl, ← map_mul, mul_inv_cancel, map_one]
          rfl

@[simp] theorem axisAct_apply (g : Perm (Fin 4)) (j : Fin 3) :
    axisAct g j = (linkAct g (j, false)).1 := rfl

/-- The axis action is a homomorphism. -/
theorem axisAct_mul (g h : Perm (Fin 4)) : axisAct (g * h) = axisAct g * axisAct h := by
  refine Equiv.ext fun j => ?_
  show (linkAct (g * h) (j, false)).1 = (linkAct g ((linkAct h (j, false)).1, false)).1
  rw [map_mul]
  show (linkAct g (linkAct h (j, false))).1 = _
  rcases hb : (linkAct h (j, false)).2 with _ | _
  · rw [show linkAct h (j, false) = ((linkAct h (j, false)).1, false) from Prod.ext rfl hb]
  · rw [show linkAct h (j, false) = ((linkAct h (j, false)).1, true) from Prod.ext rfl hb,
      linkAct_fst_orient]
    rfl

/-! ### The corners and the taste pairing -/

/-- A Brillouin-zone corner: a `{0, π}` choice per axis, coded over `𝔽₂`. -/
abbrev Corner := Fin 3 → ZMod 2

/-- The label action of a rotation on corners: only the axis permutation survives, because sign
flips are trivial on `{0, π}` components. This IS the manuscript remark's "unsigned" action. -/
def cornerAct (g : Perm (Fin 4)) : Corner → Corner := fun η => η ∘ (axisAct g).symm

/-- **The taste pairing** `η ↔ 𝟙 − η`, which over `𝔽₂` is `η + 𝟙`. -/
def mate (η : Corner) : Corner := η + 1

/-- The pairing is equivariant, so the action descends to the four taste pairs. -/
theorem cornerAct_mate (g : Perm (Fin 4)) (η : Corner) :
    cornerAct g (mate η) = mate (cornerAct g η) := by
  funext x
  simp [cornerAct, mate]

/-- **The singlet pair is fixed pointwise**: both constant corners are invariant under every
rotation. -/
theorem singlet_fixed (g : Perm (Fin 4)) :
    cornerAct g 0 = 0 ∧ cornerAct g (1 : Corner) = 1 :=
  ⟨rfl, rfl⟩

/-- The axis corners `e_j`. -/
def axisCorner (j : Fin 3) : Corner := Pi.single j 1

/-- The label action carries axis corners to axis corners, along the axis permutation. -/
theorem cornerAct_axisCorner (g : Perm (Fin 4)) (j : Fin 3) :
    cornerAct g (axisCorner j) = axisCorner (axisAct g j) := by
  funext x
  simp only [cornerAct, axisCorner, Function.comp_apply]
  by_cases hx : x = axisAct g j
  · rw [hx]
    rw [Pi.single_eq_same, show (axisAct g).symm (axisAct g j) = j from (axisAct g).symm_apply_apply j,
      Pi.single_eq_same]
  · rw [Pi.single_eq_of_ne hx, Pi.single_eq_of_ne]
    intro hc
    exact hx (by rw [← hc, (axisAct g).apply_symm_apply])

/-- **The axis action is transitive**: every axis reaches every axis, so the three axis pairs form
a single orbit and the branching is `4 = 1 + 3` with nothing further split off at the level of
pairs. Decided over the 24 rotations. -/
theorem axis_transitive : ∀ j k : Fin 3, ∃ g : Perm (Fin 4), axisAct g j = k := by
  decide

/-- **Every corner is accounted for**: the two constants and the six axis-pair members exhaust the
`2³` corners, so the four taste pairs are the whole Brillouin zone. -/
theorem corners_exhausted (η : Corner) :
    η = 0 ∨ η = 1 ∨ (∃ j, η = axisCorner j) ∨ (∃ j, η = mate (axisCorner j)) := by
  revert η
  decide

/-! ### The two carriers of the triplet

The label action on the three axis pairs extends linearly to the permutation representation below,
and that representation is REDUCIBLE — the all-ones line is invariant — which is the manuscript
remark's `A₁ ⊕ E`. The irreducible `T₁` is the signed carrier, `QuarterTurn.rhoT`, already proved
irreducible over ℚ in the kernel. -/

/-- The unsigned (label) permutation representation on the three axis pairs. -/
noncomputable def axisRep : Representation ℚ (Perm (Fin 4)) (Fin 3 → ℚ) where
  toFun g :=
    { toFun := fun v => v ∘ (axisAct g).symm
      map_add' := fun v w => rfl
      map_smul' := fun c v => rfl }
  map_one' := by
    refine LinearMap.ext fun v => ?_
    funext x
    show v ((axisAct 1).symm x) = v x
    congr 1
    have h1 : axisAct (1 : Perm (Fin 4)) = 1 := by
      refine Equiv.ext fun j => ?_
      show (linkAct 1 (j, false)).1 = j
      rw [map_one]
      rfl
    rw [h1]
    rfl
  map_mul' g h := by
    refine LinearMap.ext fun v => ?_
    funext x
    show v ((axisAct (g * h)).symm x) = v ((axisAct h).symm ((axisAct g).symm x))
    rw [axisAct_mul]
    rfl

/-- The all-ones vector is invariant under the label action. -/
theorem axisRep_fixes_allOnes (g : Perm (Fin 4)) :
    axisRep g (fun _ => (1 : ℚ)) = fun _ => (1 : ℚ) := rfl

/-- **The label action is NOT irreducible** — the manuscript remark's point, kernel-proved: the
all-ones line is a proper nonzero invariant subrepresentation, so the three axis pairs carry
`A₁ ⊕ E` on their labels and the irreducible triplet must live on the signed carrier. -/
theorem axis_rep_reducible : ¬ Representation.IsIrreducible axisRep := by
  intro hirr
  set allOnes : Fin 3 → ℚ := fun _ => 1 with hall
  have hinv : ∀ (g : Perm (Fin 4)), ∀ v ∈ Submodule.span ℚ {allOnes},
      axisRep g v ∈ Submodule.span ℚ {allOnes} := by
    intro g v hv
    obtain ⟨c, hc⟩ := Submodule.mem_span_singleton.1 hv
    rw [← hc, map_smul]
    exact Submodule.mem_span_singleton.2 ⟨c, by rw [axisRep_fixes_allOnes]⟩
  set σ : Subrepresentation axisRep :=
    ⟨Submodule.span ℚ {allOnes}, fun g v hv => hinv g v hv⟩ with hσ
  rcases hirr.eq_bot_or_eq_top σ with hbot | htop
  · have hspan : (Submodule.span ℚ ({allOnes} : Set (Fin 3 → ℚ)))
        = (⊥ : Submodule ℚ (Fin 3 → ℚ)) :=
      congrArg Subrepresentation.toSubmodule hbot
    have h0 : allOnes ∈ Submodule.span ℚ ({allOnes} : Set (Fin 3 → ℚ)) :=
      Submodule.mem_span_singleton_self _
    rw [hspan, Submodule.mem_bot] at h0
    have h1 := congrFun h0 0
    norm_num [hall] at h1
  · have hspan : (Submodule.span ℚ ({allOnes} : Set (Fin 3 → ℚ)))
        = (⊤ : Submodule ℚ (Fin 3 → ℚ)) :=
      congrArg Subrepresentation.toSubmodule htop
    have hmem : (Pi.single 0 1 : Fin 3 → ℚ) ∈ Submodule.span ℚ ({allOnes} : Set (Fin 3 → ℚ)) := by
      rw [hspan]
      exact Submodule.mem_top
    obtain ⟨c, hc⟩ := Submodule.mem_span_singleton.1 hmem
    have h0 := congrFun hc 0
    have h1 := congrFun hc 1
    simp only [Pi.smul_apply, hall, smul_eq_mul, mul_one] at h0 h1
    rw [Pi.single_eq_same] at h0
    rw [Pi.single_eq_of_ne (by norm_num)] at h1
    rw [h1] at h0
    norm_num at h0

/-! ### The theorem -/

/-- **[SM] THEOREM 8 (taste branching).** Under the cubic rotation group the four taste pairs
split `4 = 1 ⊕ 3`: the pairing is equivariant; the singlet pair `{0, 𝟙}` is fixed pointwise; the
three axis pairs are carried to one another transitively; the four pairs exhaust the Brillouin
zone; the triplet's signed carrier — the vector representation `rhoT` of the same rotation group —
is irreducible over ℚ; and the unsigned label action on the axis pairs is not, which is why the
manuscript's remark locates `T₁` on the signed carrier. -/
theorem theorem_8 :
    (∀ (g : Perm (Fin 4)) (η : Corner), cornerAct g (mate η) = mate (cornerAct g η)) ∧
    (∀ g : Perm (Fin 4), cornerAct g 0 = 0 ∧ cornerAct g (1 : Corner) = 1) ∧
    (∀ (g : Perm (Fin 4)) (j : Fin 3), cornerAct g (axisCorner j) = axisCorner (axisAct g j)) ∧
    (∀ j k : Fin 3, ∃ g : Perm (Fin 4), axisAct g j = k) ∧
    (∀ η : Corner,
      η = 0 ∨ η = 1 ∨ (∃ j, η = axisCorner j) ∨ (∃ j, η = mate (axisCorner j))) ∧
    Representation.IsIrreducible rhoT ∧
    ¬ Representation.IsIrreducible axisRep :=
  ⟨cornerAct_mate, singlet_fixed, cornerAct_axisCorner, axis_transitive, corners_exhausted,
   irreducible_rhoT, axis_rep_reducible⟩

/-! ### What these proofs rest on -/

#print axioms axisAct_mul
#print axioms cornerAct_mate
#print axioms singlet_fixed
#print axioms cornerAct_axisCorner
#print axioms axis_transitive
#print axioms corners_exhausted
#print axioms axisRep_fixes_allOnes
#print axioms axis_rep_reducible
#print axioms theorem_8

end TasteBranching

end OIBridge
