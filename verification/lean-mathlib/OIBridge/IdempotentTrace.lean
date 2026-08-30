/-
  OIBridge/IdempotentTrace.lean — the trace of a commuting endomorphism restricted to the image of
  an idempotent.

      Let `P` be idempotent and let `f` commute with `P`. Then `f` preserves both `im P` and
      `ker P`, the space splits as `im P ⊕ ker P`, and

          tr (f restricted to im P)  =  tr (f ∘ P).

  WHY THIS FILE EXISTS SEPARATELY. It is the missing library step that [SM] Theorem 7 is blocked
  on, and it is not a fact about representations: it is a fact about an idempotent and a commuting
  endomorphism of a finite-dimensional vector space, with no group, no character, and no
  equivariance anywhere in the statement. Keeping it general is what turns Theorem 7's "blocked on
  a Mathlib lemma that does not exist" into a resolved infrastructure dependency, reusable by every
  projector-based multiplicity argument the corpus has.

  WHAT MATHLIB ALREADY HAS, and what it does not. `LinearMap.IsProj.trace` gives
  `tr P = finrank (im P)` — the `f = id` case. The general commuting case is not there, and it is
  what a character computation on an isotypic component actually needs. The proof follows Mathlib's
  own route for the special case: an idempotent conjugates the space into `im P × ker P`, and in
  that decomposition `f` is block diagonal while `f ∘ P` is the same block diagonal with the second
  block replaced by zero.

  THE SHARP HYPOTHESIS. Commuting is sufficient but NOT necessary: only invariance of the image is
  used. Commuting additionally controls the kernel block, which the trace never sees. The companion
  probe is what established this — it could produce no countercontrol for commutativity, because
  there is none — and `trace_restrict_range_of_mapsTo` records the weaker form, since a consumer
  with an invariant subspace but no commuting map should not have to manufacture one.

  THE FREE COROLLARY. Setting `f = id` recovers `tr P = finrank (im P)` from this lemma rather than
  from Mathlib's, which is a small consistency check on the statement's orientation.

  Stated over an arbitrary field and an arbitrary finite-dimensional vector space. The freeness and
  finiteness instances the trace API wants are automatic there; over a general commutative ring they
  would have to be carried by hand on both `im P` and `ker P`, for no gain to any consumer in this
  corpus.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.LinearAlgebra.Trace
import Mathlib.LinearAlgebra.Projection
import Mathlib.LinearAlgebra.FiniteDimensional.Defs

namespace OIBridge

namespace IdempotentTrace

open LinearMap Submodule

variable {K V : Type*} [Field K] [AddCommGroup V] [Module K V]

/-! ### The two invariant blocks

Commuting with `P` is exactly what makes `f` preserve the image and the kernel. None of this needs
finite-dimensionality, and the section variable is deliberately introduced only below, where the
trace API first requires it. -/

/-- An idempotent fixes its image pointwise. -/
theorem apply_eq_self_of_mem_range {P : V →ₗ[K] V} (hP : P ∘ₗ P = P) {x : V}
    (hx : x ∈ range P) : P x = x := by
  obtain ⟨z, rfl⟩ := hx
  exact congrArg (fun g => g z) hP

/-- **`f` preserves the image of `P`.** -/
theorem mapsTo_range {P f : V →ₗ[K] V} (hc : f ∘ₗ P = P ∘ₗ f) :
    ∀ x ∈ range P, f x ∈ range P := by
  rintro _ ⟨z, rfl⟩
  exact ⟨f z, congrArg (fun g => g z) hc.symm⟩

/-- **`f` preserves the kernel of `P`.** -/
theorem mapsTo_ker {P f : V →ₗ[K] V} (hc : f ∘ₗ P = P ∘ₗ f) :
    ∀ x ∈ ker P, f x ∈ ker P := by
  intro x hx
  have : P (f x) = f (P x) := (congrArg (fun g => g x) hc).symm
  rw [mem_ker, this, (mem_ker.1 hx), map_zero]

/-- **The space splits.** `V = im P ⊕ ker P`, which is what makes the block decomposition below
meaningful. -/
theorem isCompl_range_ker {P : V →ₗ[K] V} (hP : P ∘ₗ P = P) :
    IsCompl (range P) (ker P) :=
  IsIdempotentElem.isCompl (f := P) hP

/-! ### The block decomposition and the trace identity

The block decomposition itself is dimension-free; only the trace identity needs the space to be
finite-dimensional, and the freeness and finiteness instances on `im P` and `ker P` come for free
over a field. -/

/-- In the decomposition `V = im P ⊕ ker P`, the map `f ∘ P` is `f` on the first block and zero on
the second. This is the whole content; the trace identity is then two Mathlib lemmas. -/
theorem comp_eq_conj_prodMap {P f : V →ₗ[K] V} (hP : P ∘ₗ P = P) (hc : f ∘ₗ P = P ∘ₗ f) :
    f ∘ₗ P
      = (Submodule.prodEquivOfIsCompl _ _ (isCompl_range_ker hP)).conj
          (LinearMap.prodMap (f.restrict (mapsTo_range hc)) 0) := by
  set e := Submodule.prodEquivOfIsCompl (range P) (ker P) (isCompl_range_ker hP) with he
  refine LinearMap.ext fun x => ?_
  -- write `x` in the two blocks
  obtain ⟨y, hy⟩ : ∃ y : (range P) × (ker P), e y = x := ⟨e.symm x, e.apply_symm_apply x⟩
  subst hy
  have hcoe : (e y : V) = (y.1 : V) + (y.2 : V) := by
    rw [he, Submodule.coe_prodEquivOfIsCompl']
  have hPy : P (e y) = (y.1 : V) := by
    rw [hcoe, map_add, apply_eq_self_of_mem_range hP y.1.2, (mem_ker.1 y.2.2), add_zero]
  have hconj : (e.conj (LinearMap.prodMap (f.restrict (mapsTo_range hc)) 0)) (e y)
      = f (y.1 : V) := by
    rw [LinearEquiv.conj_apply, LinearMap.comp_apply, LinearMap.comp_apply,
      LinearEquiv.coe_coe, LinearEquiv.coe_coe, e.symm_apply_apply]
    rw [he, Submodule.coe_prodEquivOfIsCompl']
    simp [LinearMap.prodMap_apply]
  rw [LinearMap.comp_apply, hPy, hconj]

variable [FiniteDimensional K V]

/-- **Trace of a commuting endomorphism on the image of an idempotent.**

`tr (f|_{im P}) = tr (f ∘ P)`. This is the lemma [SM] Theorem 7 is blocked on, and it is stated
without any reference to groups, characters or equivariance — an idempotent and a map commuting
with it, on a finite-dimensional vector space, is the whole hypothesis. -/
theorem trace_restrict_range {P f : V →ₗ[K] V} (hP : P ∘ₗ P = P) (hc : f ∘ₗ P = P ∘ₗ f) :
    trace K (range P) (f.restrict (mapsTo_range hc)) = trace K V (f ∘ₗ P) := by
  rw [comp_eq_conj_prodMap hP hc, trace_conj', trace_prodMap', map_zero, add_zero]

/-- **The sharp hypothesis: commuting is sufficient but not necessary.**

Only INVARIANCE OF THE IMAGE is needed. Commuting also controls the kernel block, which the trace
never sees: in the decomposition `V = im P ⊕ ker P`, image-invariance makes `f` block TRIANGULAR
rather than block diagonal, and `f ∘ P` kills the off-diagonal block either way. The companion
probe found this — it could produce no countercontrol for commutativity, because there is none.

The proof is the commuting case applied to the compression `P ∘ f ∘ P`, which commutes with `P`,
agrees with `f` on the image, and has the same composite with `P`. -/
theorem trace_restrict_range_of_mapsTo {P f : V →ₗ[K] V} (hP : P ∘ₗ P = P)
    (hm : ∀ x ∈ range P, f x ∈ range P) :
    trace K (range P) (f.restrict hm) = trace K V (f ∘ₗ P) := by
  set g : V →ₗ[K] V := P ∘ₗ f ∘ₗ P with hg
  have hfix : ∀ x : V, P (f (P x)) = f (P x) := fun x =>
    apply_eq_self_of_mem_range hP (hm _ ⟨x, rfl⟩)
  have hgP : g ∘ₗ P = f ∘ₗ P := by
    refine LinearMap.ext fun x => ?_
    have hx : P (P x) = P x := congrArg (fun t => t x) hP
    simp only [hg, LinearMap.comp_apply, hx, hfix]
  have hcg : g ∘ₗ P = P ∘ₗ g := by
    refine LinearMap.ext fun x => ?_
    have hx : P (P x) = P x := congrArg (fun t => t x) hP
    simp only [hg, LinearMap.comp_apply, hx, hfix]
  have hres : g.restrict (mapsTo_range hcg) = f.restrict hm := by
    refine LinearMap.ext fun x => ?_
    refine Subtype.ext ?_
    obtain ⟨z, hz⟩ := x.2
    simp only [LinearMap.restrict_apply, hg, LinearMap.comp_apply]
    rw [← hz]
    have hx : P (P z) = P z := congrArg (fun t => t z) hP
    rw [hx, hfix]
  rw [← hres, trace_restrict_range hP hcg, hgP]

/-- **The free corollary**: `tr P = dim (im P)`, by taking `f` to be the identity. Useful on its own
for projector-based multiplicity arguments, and a consistency check that the identity above is
oriented the way a character computation wants it. -/
theorem trace_eq_finrank_range {P : V →ₗ[K] V} (hP : P ∘ₗ P = P) :
    trace K V P = (Module.finrank K (range P) : K) := by
  have hc : (LinearMap.id : V →ₗ[K] V) ∘ₗ P = P ∘ₗ LinearMap.id := by
    ext x; simp
  have hrestrict : (LinearMap.id : V →ₗ[K] V).restrict (mapsTo_range hc)
      = LinearMap.id := by
    ext x; rfl
  have h := trace_restrict_range hP hc
  rw [hrestrict, trace_id] at h
  have hid : (LinearMap.id : V →ₗ[K] V) ∘ₗ P = P := by ext x; simp
  rw [hid] at h
  exact h.symm

/-! ### What these proofs rest on -/

#print axioms apply_eq_self_of_mem_range
#print axioms mapsTo_range
#print axioms mapsTo_ker
#print axioms isCompl_range_ker
#print axioms comp_eq_conj_prodMap
#print axioms trace_restrict_range
#print axioms trace_restrict_range_of_mapsTo
#print axioms trace_eq_finrank_range

end IdempotentTrace

end OIBridge
