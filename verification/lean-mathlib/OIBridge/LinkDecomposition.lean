/-
  OIBridge/LinkDecomposition.lean — [SM] Theorem 7, the exact six-link representation.

      The six signed simple-cubic links decompose as `T₁ ⊕ E ⊕ A₁`, of dimensions `3 ⊕ 2 ⊕ 1`.

  BUILT ON THE LINKS THEMSELVES. The space is functions on `Fin 3 × Bool` — an axis and a sign,
  which is what a signed nearest-neighbour link IS — so the geometry is the definition rather than
  a model of it. The antipodal map `(i, s) ↦ (i, ¬s)` is `−1` on link vectors, and the whole
  decomposition is read off it.

  THE DECOMPOSITION IS NOT A MULTIPLICITY COUNT. Three explicit projectors are constructed,
  proved idempotent, pairwise orthogonal and summing to the identity, and each is shown to commute
  with every symmetry of the link set. Their images are therefore invariant subspaces and the space
  is their internal direct sum. The dimensions `3, 2, 1` come from `IdempotentTrace`'s
  `trace_eq_finrank_range` — the infrastructure lemma validated in its intended consumer — rather
  than from ad hoc bases.

  THE GROUP. The projectors commute with EVERY permutation of the links that preserves the
  antipodal pairing, which is exactly the group of signed axis permutations, `O_h`. The
  decomposition therefore holds a fortiori for the proper rotation group `O` the manuscript names,
  and the three subspaces are the same for both. What distinguishes `O` is the LABELS: the two
  three-dimensional irreducibles `T₁` and `T₂` are separated by their character at a four-fold
  rotation, and `char_c4_odd` computes it to be `1` — `T₁`'s value, not `T₂`'s `−1`. The 48-element
  `O_h` of `CubicIsotropy` is deliberately NOT substituted here; that file is about quadratic forms
  on ℝ³ and has no bearing on which three-dimensional irreducible of `O` appears.

  SCOPE GUARD, stated because the manuscript is explicit about it. THIS FILE PROVES GEOMETRY, NOT
  THE PHYSICAL-CARRIER IDENTIFICATION. The six-link decomposition is unconditional. **H-link** — the
  identification of that link space with the complete physical gauge carrier — is a named premise,
  and it appears here only as the hypothesis of the separate transport theorem at the end.
  **H-cust**, the custodial condensate-stabilizer reading, belongs downstream and appears nowhere in
  this file.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.IdempotentTrace
import Mathlib.LinearAlgebra.Matrix.ToLin
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Matrix.Basis

namespace OIBridge

namespace LinkDecomposition

open LinearMap Submodule OIBridge.IdempotentTrace

/-! ### The six links, and the antipodal map -/

/-- A signed simple-cubic link: an axis and a sign. These are the six vectors `±e₁, ±e₂, ±e₃`. -/
abbrev Link := Fin 3 × Bool

/-- The link space `V₆`. -/
abbrev LV := Link → ℚ

theorem card_link : Fintype.card Link = 6 := by decide

/-- The antipodal map, which is `−1` on link vectors. -/
def anti : Link → Link := fun l => (l.1, !l.2)

theorem anti_anti (l : Link) : anti (anti l) = l := by
  simp [anti]

theorem anti_ne (l : Link) : anti l ≠ l := by
  simp [anti, Prod.ext_iff]

/-- The antipodal map as a permutation. -/
def antiPerm : Equiv.Perm Link := Function.Involutive.toPerm anti anti_anti

/-! ### Traces of permutation operators

Everything below reduces to counting fixed points, and this is the lemma that does the reducing. -/

/-- Precomposition with a permutation of the links. -/
def permOp (h : Equiv.Perm Link) : LV →ₗ[ℚ] LV where
  toFun f := fun l => f (h l)
  map_add' _ _ := rfl
  map_smul' _ _ := rfl

theorem permOp_apply (h : Equiv.Perm Link) (f : LV) (l : Link) : permOp h f l = f (h l) := rfl

/-- **The trace of a permutation operator is its fixed-point count.** -/
theorem trace_permOp (h : Equiv.Perm Link) :
    trace ℚ LV (permOp h) = ((Finset.univ.filter fun l => h l = l).card : ℚ) := by
  classical
  rw [LinearMap.trace_eq_matrix_trace ℚ (Pi.basisFun ℚ Link), Matrix.trace]
  have hentry : ∀ l : Link,
      (LinearMap.toMatrix (Pi.basisFun ℚ Link) (Pi.basisFun ℚ Link) (permOp h)) l l
        = if h l = l then 1 else 0 := by
    intro l
    rw [LinearMap.toMatrix_apply]
    simp only [Pi.basisFun_repr, Pi.basisFun_apply, permOp_apply]
    by_cases hl : h l = l
    · rw [if_pos hl, hl]; simp
    · rw [if_neg hl]
      simp [hl]
  simp only [Matrix.diag_apply, hentry]
  rw [Finset.sum_boole]

/-- **`permOp` is an ANTI-homomorphism.** Precomposition reverses the order of composition, so any
REPRESENTATION built from it has to carry the inverse: `rho g = permOp (h g⁻¹)`. Recorded as a
lemma rather than left to the reader, because the `S₄` characters here happen to satisfy
`χ(g⁻¹) = χ(g)` and every numeric consequence would come out right even with the orientation
wrong. -/
theorem permOp_mul (h₁ h₂ : Equiv.Perm Link) : permOp (h₁ * h₂) = permOp h₂ ∘ₗ permOp h₁ := by
  refine LinearMap.ext fun f => ?_
  funext l
  rfl

theorem permOp_one : permOp 1 = LinearMap.id := by
  refine LinearMap.ext fun f => ?_
  funext l
  rfl

/-! ### The three projectors

`C` is the antipodal involution on functions. `P_T` is its `−1` eigenprojector — the odd functions,
which are the link vectors themselves. `P_A` averages onto constants. `P_E` is what is left. -/

/-- The antipodal involution on functions. -/
def C : LV →ₗ[ℚ] LV := permOp antiPerm

/-- Averaging onto the constants. -/
def PA : LV →ₗ[ℚ] LV where
  toFun f := fun _ => (1 / 6 : ℚ) * ∑ l, f l
  map_add' f g := by
    funext l
    show (1 / 6 : ℚ) * ∑ m, (f m + g m)
      = (1 / 6 : ℚ) * (∑ m, f m) + (1 / 6 : ℚ) * ∑ m, g m
    rw [Finset.sum_add_distrib]; ring
  map_smul' c f := by
    funext l
    show (1 / 6 : ℚ) * ∑ m, (c * f m) = c * ((1 / 6 : ℚ) * ∑ m, f m)
    rw [← Finset.mul_sum]; ring

/-- `P_T`: the odd part. Dimension 3 — the link vectors. -/
noncomputable def PT : LV →ₗ[ℚ] LV := (1 / 2 : ℚ) • (LinearMap.id - C)

/-- The even part, before the constants are removed. -/
noncomputable def Peven : LV →ₗ[ℚ] LV := (1 / 2 : ℚ) • (LinearMap.id + C)

/-- `P_E`: even, with the three pair-values summing to zero. Dimension 2. -/
noncomputable def PE : LV →ₗ[ℚ] LV := Peven - PA

/-! ### The projector algebra

All of it is direct computation: `C² = id`, and averaging is unchanged by the antipodal map because
the sum over the links is. -/

theorem C_apply (f : LV) (l : Link) : C f l = f (anti l) := rfl

theorem C_comp_C : C ∘ₗ C = LinearMap.id := by
  refine LinearMap.ext fun f => ?_
  funext l
  simp only [LinearMap.comp_apply, C_apply, anti_anti, LinearMap.id_apply]

theorem PA_apply (f : LV) (l : Link) : PA f l = (1 / 6 : ℚ) * ∑ m, f m := rfl

theorem sum_comp_anti (f : LV) : ∑ l, f (anti l) = ∑ l, f l :=
  Fintype.sum_equiv antiPerm _ _ fun _ => rfl

theorem PA_comp_C : PA ∘ₗ C = PA := by
  refine LinearMap.ext fun f => ?_
  funext l
  simp only [LinearMap.comp_apply, PA_apply, C_apply, sum_comp_anti]

theorem C_comp_PA : C ∘ₗ PA = PA := by
  refine LinearMap.ext fun f => ?_
  funext l
  simp only [LinearMap.comp_apply, C_apply, PA_apply]

theorem PA_comp_PA : PA ∘ₗ PA = PA := by
  refine LinearMap.ext fun f => ?_
  funext l
  simp only [LinearMap.comp_apply, PA_apply, Finset.sum_const, Finset.card_univ, card_link,
    nsmul_eq_mul]
  ring

theorem PT_idem : PT ∘ₗ PT = PT := by
  have h : (LinearMap.id - C) ∘ₗ (LinearMap.id - C) = (2 : ℚ) • (LinearMap.id - C) := by
    rw [LinearMap.comp_sub, LinearMap.sub_comp, LinearMap.sub_comp, C_comp_C]
    refine LinearMap.ext fun f => ?_
    funext l
    simp only [LinearMap.sub_apply, LinearMap.id_apply, LinearMap.smul_apply, Pi.smul_apply,
      Pi.sub_apply, LinearMap.comp_apply]
    ring
  rw [PT, LinearMap.smul_comp, LinearMap.comp_smul, h]
  rw [smul_smul, smul_smul]
  norm_num

theorem Peven_idem : Peven ∘ₗ Peven = Peven := by
  have h : (LinearMap.id + C) ∘ₗ (LinearMap.id + C) = (2 : ℚ) • (LinearMap.id + C) := by
    rw [LinearMap.comp_add, LinearMap.add_comp, LinearMap.add_comp, C_comp_C]
    refine LinearMap.ext fun f => ?_
    funext l
    simp only [LinearMap.add_apply, LinearMap.id_apply, LinearMap.smul_apply, Pi.smul_apply,
      Pi.add_apply, LinearMap.comp_apply]
    ring
  rw [Peven, LinearMap.smul_comp, LinearMap.comp_smul, h]
  rw [smul_smul, smul_smul]
  norm_num

theorem Peven_comp_PA : Peven ∘ₗ PA = PA := by
  rw [Peven, LinearMap.smul_comp, LinearMap.add_comp, LinearMap.id_comp, C_comp_PA]
  refine LinearMap.ext fun f => ?_
  funext l
  simp only [LinearMap.smul_apply, Pi.smul_apply, LinearMap.add_apply, Pi.add_apply]
  ring

theorem PA_comp_Peven : PA ∘ₗ Peven = PA := by
  rw [Peven, LinearMap.comp_smul, LinearMap.comp_add, LinearMap.comp_id, PA_comp_C]
  refine LinearMap.ext fun f => ?_
  funext l
  simp only [LinearMap.smul_apply, Pi.smul_apply, LinearMap.add_apply, Pi.add_apply]
  ring

theorem PE_idem : PE ∘ₗ PE = PE := by
  rw [PE, LinearMap.sub_comp, LinearMap.comp_sub, LinearMap.comp_sub, Peven_idem,
    Peven_comp_PA, PA_comp_Peven, PA_comp_PA]
  abel

theorem PT_comp_Peven : PT ∘ₗ Peven = 0 := by
  rw [PT, Peven, LinearMap.smul_comp, LinearMap.comp_smul, LinearMap.sub_comp,
    LinearMap.comp_add, LinearMap.comp_add, LinearMap.id_comp, LinearMap.id_comp, C_comp_C]
  refine LinearMap.ext fun f => ?_
  funext l
  simp only [LinearMap.smul_apply, Pi.smul_apply, LinearMap.sub_apply, LinearMap.add_apply,
    Pi.sub_apply, Pi.add_apply, LinearMap.id_apply, LinearMap.comp_apply, LinearMap.zero_apply,
    Pi.zero_apply]
  ring

theorem Peven_comp_PT : Peven ∘ₗ PT = 0 := by
  rw [PT, Peven, LinearMap.smul_comp, LinearMap.comp_smul, LinearMap.add_comp,
    LinearMap.comp_sub, LinearMap.comp_sub, LinearMap.id_comp, LinearMap.id_comp, C_comp_C]
  refine LinearMap.ext fun f => ?_
  funext l
  simp only [LinearMap.smul_apply, Pi.smul_apply, LinearMap.sub_apply, LinearMap.add_apply,
    Pi.sub_apply, Pi.add_apply, LinearMap.id_apply, LinearMap.comp_apply, LinearMap.zero_apply,
    Pi.zero_apply]
  ring

theorem PT_comp_PA : PT ∘ₗ PA = 0 := by
  rw [PT, LinearMap.smul_comp, LinearMap.sub_comp, LinearMap.id_comp, C_comp_PA]
  simp

theorem PA_comp_PT : PA ∘ₗ PT = 0 := by
  rw [PT, LinearMap.comp_smul, LinearMap.comp_sub, LinearMap.comp_id, PA_comp_C]
  simp

theorem PT_comp_PE : PT ∘ₗ PE = 0 := by
  rw [PE, LinearMap.comp_sub, PT_comp_Peven, PT_comp_PA, sub_zero]

theorem PE_comp_PT : PE ∘ₗ PT = 0 := by
  rw [PE, LinearMap.sub_comp, Peven_comp_PT, PA_comp_PT, sub_zero]

theorem PE_comp_PA : PE ∘ₗ PA = 0 := by
  rw [PE, LinearMap.sub_comp, Peven_comp_PA, PA_comp_PA, sub_self]

theorem PA_comp_PE : PA ∘ₗ PE = 0 := by
  rw [PE, LinearMap.comp_sub, PA_comp_Peven, PA_comp_PA, sub_self]

/-- **Completeness**: the three projectors sum to the identity. With idempotence and pairwise
orthogonality this is what makes the decomposition a direct sum. -/
theorem sum_proj : PT + PE + PA = LinearMap.id := by
  rw [PE, PT, Peven]
  refine LinearMap.ext fun f => ?_
  funext l
  simp only [LinearMap.add_apply, LinearMap.sub_apply, LinearMap.smul_apply, Pi.smul_apply,
    Pi.add_apply, Pi.sub_apply, LinearMap.id_apply, LinearMap.add_apply]
  ring

/-! ### The dimensions, via the trace lemma

This is the infrastructure theorem in its intended consumer: the dimension of each summand is the
trace of its projector, and each trace is a fixed-point count. -/

theorem trace_id_LV : trace ℚ LV LinearMap.id = 6 := by
  have h : (LinearMap.id : LV →ₗ[ℚ] LV) = permOp 1 := by
    refine LinearMap.ext fun f => ?_; funext l; rfl
  rw [h, trace_permOp]
  have hc : (Finset.univ.filter fun l : Link => (1 : Equiv.Perm Link) l = l).card = 6 := by decide
  rw [hc]; norm_num

theorem trace_C : trace ℚ LV C = 0 := by
  rw [C, trace_permOp]
  have hc : (Finset.univ.filter fun l : Link => antiPerm l = l).card = 0 := by decide
  rw [hc]; norm_num

theorem trace_PA : trace ℚ LV PA = 1 := by
  classical
  rw [LinearMap.trace_eq_matrix_trace ℚ (Pi.basisFun ℚ Link), Matrix.trace]
  have hentry : ∀ l : Link,
      (LinearMap.toMatrix (Pi.basisFun ℚ Link) (Pi.basisFun ℚ Link) PA) l l = (1 / 6 : ℚ) := by
    intro l
    rw [LinearMap.toMatrix_apply]
    simp only [Pi.basisFun_repr, PA_apply, Pi.basisFun_apply]
    rw [Finset.sum_pi_single']
    simp
  simp only [Matrix.diag_apply, hentry, Finset.sum_const, Finset.card_univ, card_link,
    nsmul_eq_mul]
  norm_num

theorem trace_PT : trace ℚ LV PT = 3 := by
  rw [PT, map_smul, map_sub, trace_id_LV, trace_C]
  norm_num

theorem trace_Peven : trace ℚ LV Peven = 3 := by
  rw [Peven, map_smul, map_add, trace_id_LV, trace_C]
  norm_num

theorem trace_PE : trace ℚ LV PE = 2 := by
  rw [PE, map_sub, trace_Peven, trace_PA]
  norm_num

/-- **The three dimensions are 3, 2, 1**, each read off its projector's trace by
`IdempotentTrace.trace_eq_finrank_range`. -/
theorem finrank_PT : Module.finrank ℚ (range PT) = 3 := by
  have h := trace_eq_finrank_range PT_idem
  rw [trace_PT] at h
  exact_mod_cast h.symm

theorem finrank_PE : Module.finrank ℚ (range PE) = 2 := by
  have h := trace_eq_finrank_range PE_idem
  rw [trace_PE] at h
  exact_mod_cast h.symm

theorem finrank_PA : Module.finrank ℚ (range PA) = 1 := by
  have h := trace_eq_finrank_range PA_comp_PA
  rw [trace_PA] at h
  exact_mod_cast h.symm

/-! ### Equivariance

Every symmetry of the link set — every permutation preserving the antipodal pairing, which is
exactly the group of signed axis permutations — commutes with all three projectors, so all three
images are invariant subspaces. -/

/-- A symmetry of the link set: a permutation preserving the antipodal pairing. Equivalently a
signed permutation of the coordinate axes. -/
def Sym (h : Equiv.Perm Link) : Prop := ∀ l, h (anti l) = anti (h l)

theorem permOp_comp_C {h : Equiv.Perm Link} (hh : Sym h) : permOp h ∘ₗ C = C ∘ₗ permOp h := by
  refine LinearMap.ext fun f => ?_
  funext l
  simp only [LinearMap.comp_apply, C_apply, permOp_apply, hh l]

theorem permOp_comp_PA (h : Equiv.Perm Link) : permOp h ∘ₗ PA = PA ∘ₗ permOp h := by
  refine LinearMap.ext fun f => ?_
  funext _l
  simp only [LinearMap.comp_apply, PA_apply, permOp_apply]
  congr 1
  exact (Fintype.sum_equiv h _ _ fun m => rfl).symm

theorem permOp_comp_PT {h : Equiv.Perm Link} (hh : Sym h) :
    permOp h ∘ₗ PT = PT ∘ₗ permOp h := by
  rw [PT, LinearMap.comp_smul, LinearMap.smul_comp, LinearMap.comp_sub, LinearMap.sub_comp,
    LinearMap.comp_id, LinearMap.id_comp, permOp_comp_C hh]

theorem permOp_comp_PE {h : Equiv.Perm Link} (hh : Sym h) :
    permOp h ∘ₗ PE = PE ∘ₗ permOp h := by
  have hev : permOp h ∘ₗ Peven = Peven ∘ₗ permOp h := by
    rw [Peven, LinearMap.comp_smul, LinearMap.smul_comp, LinearMap.comp_add, LinearMap.add_comp,
      LinearMap.comp_id, LinearMap.id_comp, permOp_comp_C hh]
  rw [PE, LinearMap.comp_sub, LinearMap.sub_comp, hev, permOp_comp_PA]

/-! ### The characters, and which three-dimensional irreducible appears

`T₁` and `T₂` are separated by their character at a four-fold rotation. The one below is the
quarter turn about the third axis: `e₁ ↦ e₂`, `e₂ ↦ −e₁`, `e₃ ↦ e₃`. -/

/-- The quarter turn about the third axis, as a map on the links: `e₁ ↦ e₂`, `e₂ ↦ −e₁`,
`e₃ ↦ e₃`. -/
def c4 : Link → Link := fun l =>
  if l.1 = 0 then (1, l.2) else if l.1 = 1 then (0, !l.2) else l

/-- Its inverse, given explicitly so the permutation stays computable and `decide` can run on it. -/
def c4inv : Link → Link := fun l =>
  if l.1 = 1 then (0, l.2) else if l.1 = 0 then (1, !l.2) else l

/-- The quarter turn as a permutation. -/
def c4Perm : Equiv.Perm Link :=
  ⟨c4, c4inv, by decide, by decide⟩

theorem c4Perm_apply (l : Link) : c4Perm l = c4 l := rfl

theorem sym_c4 : Sym c4Perm := by
  unfold Sym
  decide

/-- The character of a summand at a symmetry, via `IdempotentTrace.trace_restrict_range`. -/
noncomputable def charOn (P : LV →ₗ[ℚ] LV) (h : Equiv.Perm Link) : ℚ :=
  trace ℚ LV (permOp h ∘ₗ P)

theorem charOn_eq_trace_restrict {P : LV →ₗ[ℚ] LV} (hP : P ∘ₗ P = P) {h : Equiv.Perm Link}
    (hc : permOp h ∘ₗ P = P ∘ₗ permOp h) :
    trace ℚ (range P) ((permOp h).restrict (mapsTo_range hc)) = charOn P h :=
  trace_restrict_range hP hc

theorem trace_permOp_c4 : trace ℚ LV (permOp c4Perm) = 2 := by
  rw [trace_permOp]
  have hc : (Finset.univ.filter fun l : Link => c4Perm l = l).card = 2 := by decide
  rw [hc]; norm_num

theorem trace_permOp_anti_c4 : trace ℚ LV (permOp (antiPerm * c4Perm)) = 0 := by
  rw [trace_permOp]
  have hc : (Finset.univ.filter fun l : Link => (antiPerm * c4Perm) l = l).card = 0 := by decide
  rw [hc]; norm_num

/-- **The character reduction for the odd summand**, general in the symmetry: composing with the
antipodal involution is composing with the antipodal permutation. With `trace_permOp` this turns
every character of `im P_T` into a difference of two fixed-point counts. -/
theorem permOp_comp_C_eq (h : Equiv.Perm Link) : permOp h ∘ₗ C = permOp (antiPerm * h) := by
  refine LinearMap.ext fun f => ?_
  funext l
  simp only [LinearMap.comp_apply, C_apply, permOp_apply]
  rfl

theorem permOp_c4_comp_C : permOp c4Perm ∘ₗ C = permOp (antiPerm * c4Perm) :=
  permOp_comp_C_eq c4Perm

/-- **The character reduction for the constants**: every symmetry acts trivially on them, so the
one-dimensional summand's character is constantly `1` — the trivial representation `A₁`. -/
theorem permOp_absorb_PA (h : Equiv.Perm Link) : permOp h ∘ₗ PA = PA := by
  refine LinearMap.ext fun f => ?_
  funext l
  simp only [LinearMap.comp_apply, PA_apply, permOp_apply]

theorem charOn_PA (h : Equiv.Perm Link) : charOn PA h = 1 := by
  rw [charOn, permOp_absorb_PA, trace_PA]

/-- The odd summand's character at any symmetry, as a difference of fixed-point counts. -/
theorem charOn_PT (h : Equiv.Perm Link) :
    charOn PT h = (1 / 2 : ℚ) * (trace ℚ LV (permOp h) - trace ℚ LV (permOp (antiPerm * h))) := by
  rw [charOn, PT, LinearMap.comp_smul, map_smul, LinearMap.comp_sub, map_sub,
    LinearMap.comp_id, permOp_comp_C_eq]
  norm_num

/-- The three characters sum to the character of the whole space, at every symmetry. -/
theorem charOn_sum (h : Equiv.Perm Link) :
    charOn PT h + charOn PE h + charOn PA h = trace ℚ LV (permOp h) := by
  simp only [charOn, ← map_add, ← LinearMap.comp_add]
  rw [show PT + PE + PA = LinearMap.id from sum_proj, LinearMap.comp_id]

/-- **The three-dimensional summand is `T₁`, not `T₂`.** Its character at the quarter turn is `1`;
`T₂`'s is `−1`. That value is the whole discriminant between the two three-dimensional
irreducibles of the rotation group. -/
theorem char_c4_odd : charOn PT c4Perm = 1 := by
  rw [charOn, PT, LinearMap.comp_smul, map_smul, LinearMap.comp_sub, map_sub,
    LinearMap.comp_id, permOp_c4_comp_C, trace_permOp_c4, trace_permOp_anti_c4]
  norm_num

/-- The character of the constants at the quarter turn is `1`: the trivial representation, `A₁`. -/
theorem char_c4_const : charOn PA c4Perm = 1 := charOn_PA c4Perm

/-- The character of the two-dimensional summand at the quarter turn is `0`, which is `E`'s. -/
theorem char_c4_E : charOn PE c4Perm = 0 := by
  have hsum := charOn_sum c4Perm
  rw [char_c4_odd, char_c4_const, trace_permOp_c4] at hsum
  linarith

/-- `A₁` really is the trivial representation: the image of `PA` is the constants, and every
symmetry acts on it as the identity. -/
theorem PA_trivial (h : Equiv.Perm Link) (f : LV) : permOp h (PA f) = PA f := by
  funext l
  simp only [permOp_apply, PA_apply]

/-! ### The theorem -/

/-- **Theorem 7 (exact six-link representation), [SM] §4.1.**

The six signed simple-cubic links carry three invariant subspaces of dimensions `3`, `2`, `1` whose
projectors are idempotent, pairwise orthogonal and sum to the identity — an internal direct sum,
not a multiplicity count. Every symmetry of the link set commutes with all three. The
three-dimensional summand has character `1` at a quarter turn, which is `T₁`'s value and not
`T₂`'s; the one-dimensional summand is the trivial representation `A₁`; the two-dimensional one is
`E`.

The decomposition is GEOMETRY and is unconditional. It says nothing about the physical carrier —
see `hlink_transport`. -/
theorem theorem_7 :
    (PT ∘ₗ PT = PT ∧ PE ∘ₗ PE = PE ∧ PA ∘ₗ PA = PA) ∧
    (PT ∘ₗ PE = 0 ∧ PE ∘ₗ PT = 0 ∧ PT ∘ₗ PA = 0 ∧ PA ∘ₗ PT = 0 ∧ PE ∘ₗ PA = 0 ∧ PA ∘ₗ PE = 0) ∧
    PT + PE + PA = LinearMap.id ∧
    (Module.finrank ℚ (range PT) = 3 ∧ Module.finrank ℚ (range PE) = 2 ∧
      Module.finrank ℚ (range PA) = 1) ∧
    (∀ h : Equiv.Perm Link, Sym h →
      permOp h ∘ₗ PT = PT ∘ₗ permOp h ∧ permOp h ∘ₗ PE = PE ∘ₗ permOp h ∧
        permOp h ∘ₗ PA = PA ∘ₗ permOp h) ∧
    (charOn PT c4Perm = 1 ∧ charOn PE c4Perm = 0 ∧ charOn PA c4Perm = 1) :=
  ⟨⟨PT_idem, PE_idem, PA_comp_PA⟩,
   ⟨PT_comp_PE, PE_comp_PT, PT_comp_PA, PA_comp_PT, PE_comp_PA, PA_comp_PE⟩,
   sum_proj,
   ⟨finrank_PT, finrank_PE, finrank_PA⟩,
   fun h hh => ⟨permOp_comp_PT hh, permOp_comp_PE hh, permOp_comp_PA h⟩,
   ⟨char_c4_odd, char_c4_E, char_c4_const⟩⟩

/-- **The H-link transport, stated separately, and genuinely equivariantly.**

**H-link** is the premise that the physical carrier is identified with the link space AS A
REPRESENTATION — an isomorphism intertwining the carrier's action with the link action, not merely
a linear isomorphism. Under it the carrier inherits the whole structure: three projectors,
idempotent, pairwise orthogonal, summing to the identity, each commuting with the carrier's own
action, with images of dimensions `3`, `2`, `1`. A dimension-only transport would be strictly
weaker and is not what the manuscript's second clause says.

Nothing here argues for the premise. **H-cust**, the custodial condensate-stabilizer reading,
appears nowhere: it is downstream of this and is not part of the geometry. -/
theorem hlink_transport {W : Type*} [AddCommGroup W] [Module ℚ W]
    (act : Equiv.Perm Link → (W →ₗ[ℚ] W)) (e : W ≃ₗ[ℚ] LV)
    (hinter : ∀ h : Equiv.Perm Link, Sym h →
      e.toLinearMap ∘ₗ act h = permOp h ∘ₗ e.toLinearMap) :
    ∃ QT QE QA : W →ₗ[ℚ] W,
      (QT ∘ₗ QT = QT ∧ QE ∘ₗ QE = QE ∧ QA ∘ₗ QA = QA) ∧
      (QT ∘ₗ QE = 0 ∧ QE ∘ₗ QT = 0 ∧ QT ∘ₗ QA = 0 ∧ QA ∘ₗ QT = 0 ∧
        QE ∘ₗ QA = 0 ∧ QA ∘ₗ QE = 0) ∧
      QT + QE + QA = LinearMap.id ∧
      (∀ h : Equiv.Perm Link, Sym h →
        act h ∘ₗ QT = QT ∘ₗ act h ∧ act h ∘ₗ QE = QE ∘ₗ act h ∧ act h ∘ₗ QA = QA ∘ₗ act h) ∧
      (Module.finrank ℚ (range QT) = 3 ∧ Module.finrank ℚ (range QE) = 2 ∧
        Module.finrank ℚ (range QA) = 1) := by
  classical
  set conj : (LV →ₗ[ℚ] LV) → (W →ₗ[ℚ] W) :=
    fun P => e.symm.toLinearMap ∘ₗ P ∘ₗ e.toLinearMap with hconj
  have hee : e.toLinearMap ∘ₗ e.symm.toLinearMap = LinearMap.id := by
    refine LinearMap.ext fun x => ?_
    simp
  have hmul : ∀ P Q : LV →ₗ[ℚ] LV, conj P ∘ₗ conj Q = conj (P ∘ₗ Q) := by
    intro P Q
    refine LinearMap.ext fun x => ?_
    simp [hconj]
  have hzero : conj 0 = 0 := by simp [hconj]
  have hone : conj LinearMap.id = LinearMap.id := by
    refine LinearMap.ext fun x => ?_
    simp [hconj]
  have hadd : ∀ P Q : LV →ₗ[ℚ] LV, conj (P + Q) = conj P + conj Q := by
    intro P Q
    simp only [hconj, LinearMap.add_comp, LinearMap.comp_add]
  -- the action really is conjugate to the link action, which is what H-link supplies
  have hact : ∀ h : Equiv.Perm Link, Sym h → act h = conj (permOp h) := by
    intro h hh
    have := hinter h hh
    have hl : e.symm.toLinearMap ∘ₗ (e.toLinearMap ∘ₗ act h)
        = e.symm.toLinearMap ∘ₗ (permOp h ∘ₗ e.toLinearMap) := by rw [this]
    rw [← LinearMap.comp_assoc, ← LinearMap.comp_assoc] at hl
    have hse : e.symm.toLinearMap ∘ₗ e.toLinearMap = LinearMap.id := by
      refine LinearMap.ext fun x => ?_; simp
    rw [hse, LinearMap.id_comp] at hl
    rw [hl, hconj, LinearMap.comp_assoc]
  have hrank : ∀ P : LV →ₗ[ℚ] LV,
      Module.finrank ℚ (range (conj P)) = Module.finrank ℚ (range P) := by
    intro P
    have himg : range (conj P) = (range P).map e.symm.toLinearMap := by
      ext w
      simp only [hconj, LinearMap.mem_range, Submodule.mem_map, LinearMap.comp_apply]
      constructor
      · rintro ⟨x, rfl⟩
        exact ⟨P (e x), ⟨e x, rfl⟩, rfl⟩
      · rintro ⟨y, ⟨x, rfl⟩, rfl⟩
        exact ⟨e.symm x, by simp⟩
    rw [himg]
    exact (Submodule.equivMapOfInjective _ e.symm.injective (range P)).finrank_eq.symm
  refine ⟨conj PT, conj PE, conj PA, ?_, ?_, ?_, ?_, ?_⟩
  · exact ⟨by rw [hmul, PT_idem], by rw [hmul, PE_idem], by rw [hmul, PA_comp_PA]⟩
  · refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩ <;>
      rw [hmul] <;>
      simp [PT_comp_PE, PE_comp_PT, PT_comp_PA, PA_comp_PT, PE_comp_PA, PA_comp_PE, hzero]
  · rw [← hadd, ← hadd, sum_proj, hone]
  · intro h hh
    rw [hact h hh]
    exact ⟨by rw [hmul, hmul, permOp_comp_PT hh],
           by rw [hmul, hmul, permOp_comp_PE hh],
           by rw [hmul, hmul, permOp_comp_PA h]⟩
  · exact ⟨by rw [hrank, finrank_PT], by rw [hrank, finrank_PE], by rw [hrank, finrank_PA]⟩

/-! ### What these proofs rest on -/

#print axioms trace_permOp
#print axioms permOp_mul
#print axioms PT_idem
#print axioms PE_idem
#print axioms sum_proj
#print axioms finrank_PT
#print axioms finrank_PE
#print axioms finrank_PA
#print axioms permOp_comp_PT
#print axioms permOp_comp_C_eq
#print axioms charOn_PA
#print axioms charOn_PT
#print axioms charOn_sum
#print axioms char_c4_odd
#print axioms char_c4_E
#print axioms theorem_7
#print axioms hlink_transport

end LinkDecomposition

end OIBridge
