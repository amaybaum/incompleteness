/-
  OIBridge/BoundaryRank.lean — [Main] Lemma 1 (boundary bound).

      rank M_HV ≤ |∂⁺R|      and      rank M_VH ≤ |∂⁻R|.

  TWO LAYERS, DELIBERATELY SEPARATED. The mathematics is a support statement and the rank bound is
  its reading over a ring where rank means what it usually means. So the file proves first, for an
  arbitrary commutative ring satisfying the strong rank condition and with no lattice anywhere in
  sight:

      a matrix whose rows vanish off a finite set `B` factors as `extend B * (its `B`-rows)`,
      hence has rank at most `|B|`.

  and only then instantiates it. The factorization is the ring-independent content; the rank
  inequality is what a field gives you.

  THE FACTOR OF TWO IS THE THING TO GET WRONG. Each lattice site carries two components, `u` and
  `v`, so the visible sector has dimension `2|R|` — and yet the bounds count SITES, not components.
  The reason is that exactly one of the two output rows at each site participates: `v'_y = u_y` is
  a hidden input read straight through, so its row in `M_HV` is identically zero, and dually for
  `M_VH`. The row-support sets `rowsHV` and `rowsVH` below therefore carry `h.val.2 = false` as
  half of their defining condition, and `rowsHV_card` is where `|∂⁺R|` rather than `2|∂⁺R|` is
  actually earned. The companion probe checks the vanishing of those rows directly, and checks that
  the bound is attained, so a spurious factor of two would fail it twice.

  The bound is by boundary SITES, not by cut edges: a star with its four leaves visible has four
  edges crossing the cut and one boundary site, and the rank is one.

  THE SHARPENING NEEDS SYMMETRY; THE LEMMA DOES NOT. The columns of each cross-block are supported
  on the OTHER boundary — `M_HV` reads visible input only through `u_x` for `x ∈ ∂⁻R` — so under
  `Symmetric adj` both ranks are bounded by `min(|∂⁻R|, |∂⁺R|)` (`lemma_1_sharpened`), which is
  what the strengthened Corollary 2 consumes. The symmetry is genuinely load-bearing and is
  therefore an explicit hypothesis rather than ambient: `innerB` asks for a neighbour pointing IN
  (`adj z x` with `z ∉ R`) while the column entry records an edge pointing OUT (`adj x y`), and for
  a directed relation the two come apart — the probe's B10 exhibits a one-edge digraph where the
  column bound fails outright while the row-side lemma, which never reverses an edge, still holds.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import Mathlib.LinearAlgebra.Matrix.Rank
import Mathlib.Data.ZMod.Basic

namespace OIBridge

namespace BoundaryRank

set_option autoImplicit false

open Matrix

/-! ### The generic support bound

Nothing here knows about lattices, boundaries, or `𝔽₂`. -/

section Generic

variable {K : Type*} [CommRing K] [StrongRankCondition K]
variable {O I : Type*} [Fintype O] [DecidableEq O] [Fintype I] [DecidableEq I]

/-- Extension by zero from the rows indexed by `B`. -/
def extend (B : Finset O) : Matrix O B K := fun o b => if (b : O) = o then 1 else 0

omit [StrongRankCondition K] [Fintype O] [Fintype I] [DecidableEq I] in
/-- **The factorization.** A matrix whose rows vanish off `B` is its own `B`-rows, extended by
zero. This is the ring-independent statement: no rank, no field, no dimension. -/
theorem eq_extend_mul_restrict (M : Matrix O I K) (B : Finset O)
    (h : ∀ o ∉ B, ∀ i, M o i = 0) :
    M = extend B * M.submatrix (Subtype.val : { x // x ∈ B } → O) id := by
  refine Matrix.ext fun o i => ?_
  symm
  rw [Matrix.mul_apply]
  by_cases ho : o ∈ B
  · rw [Finset.sum_eq_single (⟨o, ho⟩ : { x // x ∈ B })]
    · simp [extend]
    · intro b _ hb
      have hne : (b : O) ≠ o := fun hc => hb (Subtype.ext hc)
      simp [extend, hne]
    · intro hc; exact absurd (Finset.mem_univ _) hc
  · rw [h o ho i]
    refine Finset.sum_eq_zero fun b _ => ?_
    have hne : (b : O) ≠ o := fun hc => ho (hc ▸ b.2)
    simp [extend, hne]

omit [Fintype O] [DecidableEq I] in
/-- **The generic boundary bound.** Rank is at most the number of rows that can be nonzero. -/
theorem rank_le_card_of_rowSupport (M : Matrix O I K) (B : Finset O)
    (h : ∀ o ∉ B, ∀ i, M o i = 0) : M.rank ≤ B.card := by
  rw [eq_extend_mul_restrict M B h]
  refine (Matrix.rank_mul_le_left _ _).trans ?_
  simpa using Matrix.rank_le_card_width (extend B : Matrix O { x // x ∈ B } K)

/-- The projection onto the columns indexed by `B`; the column-side mirror of `extend`. -/
def project (B : Finset I) : Matrix B I K := fun b i => if (b : I) = i then 1 else 0

omit [StrongRankCondition K] [Fintype O] [DecidableEq O] [Fintype I] in
/-- The column-side factorization. -/
theorem eq_submatrix_mul_project (M : Matrix O I K) (B : Finset I)
    (h : ∀ i ∉ B, ∀ o, M o i = 0) :
    M = M.submatrix id (Subtype.val : { x // x ∈ B } → I) * project B := by
  refine Matrix.ext fun o i => ?_
  symm
  rw [Matrix.mul_apply]
  by_cases hi : i ∈ B
  · rw [Finset.sum_eq_single (⟨i, hi⟩ : { x // x ∈ B })]
    · simp [project]
    · intro b _ hb
      have hne : (b : I) ≠ i := fun hc => hb (Subtype.ext hc)
      simp [project, hne]
    · intro hc; exact absurd (Finset.mem_univ _) hc
  · rw [h i hi o]
    refine Finset.sum_eq_zero fun b _ => ?_
    have hne : (b : I) ≠ i := fun hc => hi (hc ▸ b.2)
    simp [project, hne]

omit [Fintype O] [DecidableEq O] in
/-- **The column-side bound.** Rank is also at most the number of columns that can be nonzero. -/
theorem rank_le_card_of_colSupport (M : Matrix O I K) (B : Finset I)
    (h : ∀ i ∉ B, ∀ o, M o i = 0) : M.rank ≤ B.card := by
  rw [eq_submatrix_mul_project M B h]
  refine (Matrix.rank_mul_le_left _ _).trans ?_
  simpa using Matrix.rank_le_card_width (M.submatrix id (Subtype.val : { x // x ∈ B } → I))

end Generic

/-! ### The lattice, the update, and the two boundaries -/

variable {Λ : Type*} [Fintype Λ] [DecidableEq Λ]
variable (adj : Λ → Λ → Prop) [DecidableRel adj]

/-- A state index: a site together with a component. `false` is the `u` field, `true` the `v`
field. -/
abbrev Idx (Λ : Type*) := Λ × Bool

/-- **The reversible nearest-neighbour update** `u'_x = Σ_{z ∼ x} u_z + v_x`, `v'_x = u_x`, as a
matrix over `𝔽₂`. Rows are outputs, columns are inputs. -/
def upd : Matrix (Idx Λ) (Idx Λ) (ZMod 2) := fun o i =>
  if o.2 then (if i = (o.1, false) then 1 else 0)
  else if i.2 then (if i.1 = o.1 then 1 else 0)
  else if adj i.1 o.1 then 1 else 0

omit [Fintype Λ] in
@[simp] theorem upd_v (x : Λ) (i : Idx Λ) :
    upd adj (x, true) i = if i = (x, false) then 1 else 0 := rfl

omit [Fintype Λ] in
@[simp] theorem upd_u (x : Λ) (i : Idx Λ) :
    upd adj (x, false) i =
      if i.2 then (if i.1 = x then 1 else 0) else (if adj i.1 x then 1 else 0) := rfl

variable (R : Finset Λ)

/-- The inner boundary `∂⁻R`: sites of `R` with a neighbour outside. -/
def innerB : Finset Λ := R.filter fun x => ∃ z, z ∉ R ∧ adj z x

/-- The outer boundary `∂⁺R`: sites outside `R` with a neighbour inside. -/
def outerB : Finset Λ := Finset.univ.filter fun y => y ∉ R ∧ ∃ z, z ∈ R ∧ adj z y

theorem mem_innerB {x : Λ} : x ∈ innerB adj R ↔ x ∈ R ∧ ∃ z, z ∉ R ∧ adj z x := by
  simp [innerB]

theorem mem_outerB {y : Λ} : y ∈ outerB adj R ↔ y ∉ R ∧ ∃ z, z ∈ R ∧ adj z y := by
  simp [outerB]

theorem outerB_not_mem {y : Λ} (hy : y ∈ outerB adj R) : y ∉ R := ((mem_outerB adj R).1 hy).1

theorem innerB_mem {x : Λ} (hx : x ∈ innerB adj R) : x ∈ R := ((mem_innerB adj R).1 hx).1

/-! ### The two sectors and the cross-blocks -/

/-- The visible index set: both components at every site of `R`, so of size `2|R|`. -/
abbrev Vis : Type _ := { p : Idx Λ // p.1 ∈ R }

/-- The hidden index set. -/
abbrev Hid : Type _ := { p : Idx Λ // p.1 ∉ R }

/-- `M_HV`: visible input to hidden output. -/
def MHV : Matrix (Hid R) (Vis R) (ZMod 2) :=
  (upd adj).submatrix Subtype.val Subtype.val

/-- `M_VH`: hidden input to visible output. -/
def MVH : Matrix (Vis R) (Hid R) (ZMod 2) :=
  (upd adj).submatrix Subtype.val Subtype.val

/-! ### The row supports

Both carry `.2 = false`. That is the whole content of the factor of two: the `v'` row at each site
reads a single input from its own sector and therefore contributes nothing to the cross-block. -/

/-- The rows of `M_HV` that can be nonzero: the `u'` component at outer-boundary sites. -/
def rowsHV : Finset (Hid R) :=
  Finset.univ.filter fun h => h.val.1 ∈ outerB adj R ∧ h.val.2 = false

/-- The rows of `M_VH` that can be nonzero: the `u'` component at inner-boundary sites. -/
def rowsVH : Finset (Vis R) :=
  Finset.univ.filter fun v => v.val.1 ∈ innerB adj R ∧ v.val.2 = false

/-- **One row per boundary site, not two.** -/
theorem rowsHV_card : (rowsHV adj R).card = (outerB adj R).card := by
  refine Finset.card_bij (fun h _ => h.val.1) ?_ ?_ ?_
  · intro h hh
    exact (Finset.mem_filter.1 hh).2.1
  · intro h₁ hh₁ h₂ hh₂ heq
    have hb₁ : h₁.val.2 = false := (Finset.mem_filter.1 hh₁).2.2
    have hb₂ : h₂.val.2 = false := (Finset.mem_filter.1 hh₂).2.2
    exact Subtype.ext (Prod.ext heq (hb₁.trans hb₂.symm))
  · intro y hy
    refine ⟨⟨(y, false), outerB_not_mem adj R hy⟩, ?_, rfl⟩
    exact Finset.mem_filter.2 ⟨Finset.mem_univ _, hy, rfl⟩

theorem rowsVH_card : (rowsVH adj R).card = (innerB adj R).card := by
  refine Finset.card_bij (fun v _ => v.val.1) ?_ ?_ ?_
  · intro v hv
    exact (Finset.mem_filter.1 hv).2.1
  · intro v₁ hv₁ v₂ hv₂ heq
    have hb₁ : v₁.val.2 = false := (Finset.mem_filter.1 hv₁).2.2
    have hb₂ : v₂.val.2 = false := (Finset.mem_filter.1 hv₂).2.2
    exact Subtype.ext (Prod.ext heq (hb₁.trans hb₂.symm))
  · intro x hx
    refine ⟨⟨(x, false), innerB_mem adj R hx⟩, ?_, rfl⟩
    exact Finset.mem_filter.2 ⟨Finset.mem_univ _, hx, rfl⟩

/-! ### The supports, from the update rule -/

/-- **`M_HV` vanishes off `rowsHV`.** The `v'` row reads a hidden input; the `u'` row reads a
visible input only at an outer-boundary site. -/
theorem rowSupport_MHV (h : Hid R) (hh : h ∉ rowsHV adj R) (v : Vis R) :
    MHV adj R h v = 0 := by
  obtain ⟨⟨y, c⟩, hy⟩ := h
  obtain ⟨⟨x, d⟩, hx⟩ := v
  cases c with
  | true =>
    show upd adj (y, true) (x, d) = 0
    rw [upd_v]
    refine if_neg ?_
    intro hc
    have hxy : x = y := congrArg Prod.fst hc
    exact hy (by rw [← hxy]; exact hx)
  | false =>
    show upd adj (y, false) (x, d) = 0
    rw [upd_u]
    cases d with
    | true =>
      show (if x = y then (1 : ZMod 2) else 0) = 0
      refine if_neg ?_
      intro hxy
      exact hy (by rw [← hxy]; exact hx)
    | false =>
      show (if adj x y then (1 : ZMod 2) else 0) = 0
      refine if_neg ?_
      intro hc
      exact hh (Finset.mem_filter.2 ⟨Finset.mem_univ _,
        (mem_outerB adj R).2 ⟨hy, x, hx, hc⟩, rfl⟩)

/-- **`M_VH` vanishes off `rowsVH`.** -/
theorem rowSupport_MVH (v : Vis R) (hv : v ∉ rowsVH adj R) (h : Hid R) :
    MVH adj R v h = 0 := by
  obtain ⟨⟨x, c⟩, hx⟩ := v
  obtain ⟨⟨y, d⟩, hy⟩ := h
  cases c with
  | true =>
    show upd adj (x, true) (y, d) = 0
    rw [upd_v]
    refine if_neg ?_
    intro hc
    have hyx : y = x := congrArg Prod.fst hc
    exact hy (by rw [hyx]; exact hx)
  | false =>
    show upd adj (x, false) (y, d) = 0
    rw [upd_u]
    cases d with
    | true =>
      show (if y = x then (1 : ZMod 2) else 0) = 0
      refine if_neg ?_
      intro hyx
      exact hy (by rw [hyx]; exact hx)
    | false =>
      show (if adj y x then (1 : ZMod 2) else 0) = 0
      refine if_neg ?_
      intro hc
      exact hv (Finset.mem_filter.2 ⟨Finset.mem_univ _,
        (mem_innerB adj R).2 ⟨hx, y, hy, hc⟩, rfl⟩)

/-! ### The column supports, under symmetric adjacency

The columns of `M_HV` are supported on `rowsVH` — the same finset that indexes the rows of `M_VH` —
and dually. `Symmetric adj` is the load-bearing hypothesis: the membership conditions of `innerB`
and `outerB` orient their edges INTO the named site, while a column entry records an edge OUT of
its input site, and only symmetry identifies the two. -/

/-- **`M_HV` vanishes off the columns `rowsVH`** — visible input enters only through the `u`
component at inner-boundary sites — provided adjacency is symmetric. -/
theorem colSupport_MHV (hsym : ∀ x y, adj x y → adj y x) (v : Vis R) (hv : v ∉ rowsVH adj R) (h : Hid R) :
    MHV adj R h v = 0 := by
  obtain ⟨⟨x, d⟩, hx⟩ := v
  obtain ⟨⟨y, c⟩, hy⟩ := h
  cases c with
  | true =>
    show upd adj (y, true) (x, d) = 0
    rw [upd_v]
    refine if_neg ?_
    intro hc
    have hxy : x = y := congrArg Prod.fst hc
    exact hy (by rw [← hxy]; exact hx)
  | false =>
    show upd adj (y, false) (x, d) = 0
    rw [upd_u]
    cases d with
    | true =>
      show (if x = y then (1 : ZMod 2) else 0) = 0
      refine if_neg ?_
      intro hxy
      exact hy (by rw [← hxy]; exact hx)
    | false =>
      show (if adj x y then (1 : ZMod 2) else 0) = 0
      refine if_neg ?_
      intro hc
      exact hv (Finset.mem_filter.2 ⟨Finset.mem_univ _,
        (mem_innerB adj R).2 ⟨hx, y, hy, hsym x y hc⟩, rfl⟩)

/-- **`M_VH` vanishes off the columns `rowsHV`**, dually. -/
theorem colSupport_MVH (hsym : ∀ x y, adj x y → adj y x) (h : Hid R) (hh : h ∉ rowsHV adj R) (v : Vis R) :
    MVH adj R v h = 0 := by
  obtain ⟨⟨y, d⟩, hy⟩ := h
  obtain ⟨⟨x, c⟩, hx⟩ := v
  cases c with
  | true =>
    show upd adj (x, true) (y, d) = 0
    rw [upd_v]
    refine if_neg ?_
    intro hc
    have hyx : y = x := congrArg Prod.fst hc
    exact hy (by rw [hyx]; exact hx)
  | false =>
    show upd adj (x, false) (y, d) = 0
    rw [upd_u]
    cases d with
    | true =>
      show (if y = x then (1 : ZMod 2) else 0) = 0
      refine if_neg ?_
      intro hyx
      exact hy (by rw [hyx]; exact hx)
    | false =>
      show (if adj y x then (1 : ZMod 2) else 0) = 0
      refine if_neg ?_
      intro hc
      exact hh (Finset.mem_filter.2 ⟨Finset.mem_univ _,
        (mem_outerB adj R).2 ⟨hy, x, hx, hsym y x hc⟩, rfl⟩)

/-! ### The lemma -/

theorem rank_MHV_le : (MHV adj R).rank ≤ (outerB adj R).card :=
  (rowsHV_card adj R) ▸
    rank_le_card_of_rowSupport (MHV adj R) (rowsHV adj R) (rowSupport_MHV adj R)

theorem rank_MVH_le : (MVH adj R).rank ≤ (innerB adj R).card :=
  (rowsVH_card adj R) ▸
    rank_le_card_of_rowSupport (MVH adj R) (rowsVH adj R) (rowSupport_MVH adj R)

/-- **[Main] LEMMA 1 (boundary bound).** `rank M_HV ≤ |∂⁺R|` and `rank M_VH ≤ |∂⁻R|`, for the
displayed update on any finite lattice and any region. -/
theorem lemma_1_boundary_bound :
    (MHV adj R).rank ≤ (outerB adj R).card ∧ (MVH adj R).rank ≤ (innerB adj R).card :=
  ⟨rank_MHV_le adj R, rank_MVH_le adj R⟩

/-! ### The sharpening -/

theorem rank_MHV_le_inner (hsym : ∀ x y, adj x y → adj y x) :
    (MHV adj R).rank ≤ (innerB adj R).card :=
  (rowsVH_card adj R) ▸
    rank_le_card_of_colSupport (MHV adj R) (rowsVH adj R) (colSupport_MHV adj R hsym)

theorem rank_MVH_le_outer (hsym : ∀ x y, adj x y → adj y x) :
    (MVH adj R).rank ≤ (outerB adj R).card :=
  (rowsHV_card adj R) ▸
    rank_le_card_of_colSupport (MVH adj R) (rowsHV adj R) (colSupport_MVH adj R hsym)

/-- **THE SHARPENED BOUNDARY BOUND.** Under symmetric adjacency both cross-blocks are bounded by
the SMALLER boundary. The symmetry hypothesis is not decoration: the probe exhibits a directed
one-edge graph where this fails while `lemma_1_boundary_bound` still holds. -/
theorem lemma_1_sharpened (hsym : ∀ x y, adj x y → adj y x) :
    (MHV adj R).rank ≤ min (innerB adj R).card (outerB adj R).card ∧
    (MVH adj R).rank ≤ min (innerB adj R).card (outerB adj R).card :=
  ⟨le_min (rank_MHV_le_inner adj R hsym) (rank_MHV_le adj R),
   le_min (rank_MVH_le adj R) (rank_MVH_le_outer adj R hsym)⟩

/-! ### What these proofs rest on -/

#print axioms eq_extend_mul_restrict
#print axioms rank_le_card_of_rowSupport
#print axioms rowsHV_card
#print axioms rowsVH_card
#print axioms rowSupport_MHV
#print axioms rowSupport_MVH
#print axioms rank_MHV_le
#print axioms rank_MVH_le
#print axioms lemma_1_boundary_bound
#print axioms rank_le_card_of_colSupport
#print axioms colSupport_MHV
#print axioms colSupport_MVH
#print axioms rank_MHV_le_inner
#print axioms rank_MVH_le_outer
#print axioms lemma_1_sharpened

end BoundaryRank

end OIBridge
