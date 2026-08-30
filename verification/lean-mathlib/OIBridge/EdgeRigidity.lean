/-
  OIBridge/EdgeRigidity.lean — K4-rigidity of the edge-product structure.

  THE UNIVERSAL REDUCTION BEHIND THE [GR] TWO-BRANCH CLAIM. The open reconstruction step forces,
  for each row of overlap moduli, the pulled-back edge products q'_{σ(ab)} = p_a p_b to satisfy
  every four-cycle identity q_{ab} q_{cd} = q_{ac} q_{bd} of the complete graph. This file proves
  the two theorems that turn that observation from a six-mode computation into a universal
  mechanism:

    `k4_rigidity`         — for n ≥ 5, an edge permutation of K_n that preserves all four-cycle
                            product identities AS IDENTITIES (multiset of endpoints of each
                            matching preserved) is induced by a vertex permutation.

    `exceptional_relation` — contrapositive, manuscript-facing: an edge permutation NOT induced by
                            any vertex permutation forces a nontrivial exponent relation: some
                            nonzero integer vector w with ∑ w = 0 such that every log-modulus row
                            satisfying the pulled-back identities lies on the hyperplane w · L = 0.
                            ∑ w = 0 is the flat direction: uniform rows always survive, which is
                            exactly where the n = 6 homometric analysis found its exceptional
                            locus (`pulledBack_const` records that control).

  THE n = 4 EXCEPTION IS REAL AND IS EXPOSED, NOT ASSUMED AWAY. The second hypersimplex Δ(2,n)
  has coordinate-permutation symmetry only, except at n = 2k where complementation is one extra
  involution; for k = 2 that is n = 4. `compl4_preserves` and `compl4_not_induced` verify the
  complement map on the six edges of K₄ preserves every matching identity yet is induced by no
  vertex permutation — so the bound n ≥ 5 in `k4_rigidity` is sharp, and the proof step that uses
  it (a fourth fresh vertex) is the exact point where n = 4 escapes.

  ORIENTATION IS DELIBERATELY ABSENT. Moduli are blind to the direction of a pair — p_a p_b is
  symmetric — so the modulus layer lives on unordered edges, and a directed correspondence with
  μ(b,a) = rev μ(a,b) enters through its unordered quotient. Distinguishing the relabeling branch
  from the reversal branch (and excluding mixed orientations) is phase-level information, outside
  this file's scope.

  PROOF ARCHITECTURE (all elementary, no cardinality bounds beyond the star count):
    1. `exists_mem_inter` — two edges whose images share a vertex must themselves share a vertex:
       evaluate the matching identity at the shared image vertex (count 2 forces membership in
       both cross edges), then at the other endpoint (forces an equality of image edges that
       injectivity converts into a collision of source vertices).
    2. `exists_common_vertex` — the preimage of a star is a pairwise-intersecting family of
       2-sets; with n ≥ 5 it has four distinct members, and an intersecting family with four
       members has a common vertex (the triangle {ap, aq, pq} is the only escape and caps the
       family at three).
    3. `card_star` + `Finset.eq_of_subset_of_card_le` — the containment "preimage of star u ⊆
       star a" is an equality because both sides have n − 1 edges.
    4. The assignment u ↦ a is injective, hence a bijection, and its inverse is the inducing
       vertex permutation.
-/
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Finset.Card
import Mathlib.Data.Fintype.Prod
import Mathlib.Data.Fintype.Perm
import Mathlib.Data.Fintype.Powerset
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.DeriveFintype

namespace OIBridge

open Finset

/-- An edge of the complete graph on `Fin n`: a two-element vertex set. -/
def Edge (n : ℕ) := {s : Finset (Fin n) // s.card = 2}

namespace Edge

instance (n : ℕ) : DecidableEq (Edge n) := Subtype.instDecidableEq

instance (n : ℕ) : Fintype (Edge n) := Subtype.fintype _

variable {n : ℕ}

/-- The edge `{a, b}` for distinct `a`, `b`. -/
def emk (a b : Fin n) (h : a ≠ b) : Edge n := ⟨{a, b}, Finset.card_pair h⟩

@[simp] lemma emk_val (a b : Fin n) (h : a ≠ b) : (emk a b h).val = {a, b} := rfl

lemma mem_emk {v a b : Fin n} (h : a ≠ b) : v ∈ (emk a b h).val ↔ v = a ∨ v = b := by
  simp [emk]

lemma emk_comm (a b : Fin n) (h : a ≠ b) : emk a b h = emk b a h.symm :=
  Subtype.ext (Finset.pair_comm a b)

/-- Two members of an edge exhaust it. -/
lemma eq_pair_of_two_mem {e : Edge n} {x y : Fin n} (hx : x ∈ e.val) (hy : y ∈ e.val)
    (hxy : x ≠ y) : e.val = {x, y} := by
  refine (Finset.eq_of_subset_of_card_le ?_ ?_).symm
  · intro z hz
    rcases Finset.mem_insert.mp hz with h | h
    · exact h ▸ hx
    · exact (Finset.mem_singleton.mp h) ▸ hy
  · rw [e.prop, Finset.card_pair hxy]

/-- The erased edge is a singleton. -/
lemma erase_card_one (e : Edge n) (u : Fin n) (h : u ∈ e.val) :
    (e.val.erase u).card = 1 := by
  rw [Finset.card_erase_of_mem h, e.prop]

/-- The other endpoint of an edge, given one endpoint. -/
noncomputable def oth (e : Edge n) (u : Fin n) (h : u ∈ e.val) : Fin n :=
  (Finset.card_eq_one.mp (erase_card_one e u h)).choose

lemma oth_spec (e : Edge n) (u : Fin n) (h : u ∈ e.val) :
    oth e u h ∈ e.val ∧ oth e u h ≠ u := by
  have hm : oth e u h ∈ e.val.erase u := by
    rw [(Finset.card_eq_one.mp (erase_card_one e u h)).choose_spec]
    exact Finset.mem_singleton_self _
  exact ⟨Finset.mem_of_mem_erase hm, Finset.ne_of_mem_erase hm⟩

lemma val_eq_pair_oth (e : Edge n) (u : Fin n) (h : u ∈ e.val) :
    e.val = {u, oth e u h} :=
  eq_pair_of_two_mem h (oth_spec e u h).1 (oth_spec e u h).2.symm

lemma oth_eq {e : Edge n} {u y : Fin n} (h : u ∈ e.val) (hy : y ∈ e.val) (hne : y ≠ u) :
    oth e u h = y := by
  have := val_eq_pair_oth e u h
  rw [this] at hy
  rcases Finset.mem_insert.mp hy with h' | h'
  · exact absurd h' hne
  · exact (Finset.mem_singleton.mp h').symm

/-- The endpoint-count vector of an edge, the exponent vector of `q_e = p_a p_b`. -/
def cnt (e : Edge n) : Fin n → ℤ := fun v => if v ∈ e.val then 1 else 0

lemma cnt_emk {a b : Fin n} (h : a ≠ b) :
    cnt (emk a b h) = fun v => (if v = a then (1 : ℤ) else 0) + if v = b then 1 else 0 := by
  funext v
  by_cases hva : v = a <;> by_cases hvb : v = b <;>
    simp [cnt, hva, hvb] <;> omega

lemma sum_cnt (e : Edge n) : ∑ v, cnt e v = 2 := by
  unfold cnt
  rw [← Finset.sum_filter]
  have hf : Finset.univ.filter (fun v => v ∈ e.val) = e.val := by
    ext v; simp
  rw [hf, Finset.sum_const, e.prop]
  norm_num

lemma cnt_apply_of_mem {e : Edge n} {v : Fin n} (h : v ∈ e.val) : cnt e v = 1 := by
  simp [cnt, h]

lemma cnt_apply_of_not_mem {e : Edge n} {v : Fin n} (h : v ∉ e.val) : cnt e v = 0 := by
  simp [cnt, h]

end Edge

open Edge

variable {n : ℕ}

/-- The edge permutation `σ` preserves every four-cycle product identity as an identity: for four
distinct vertices, the endpoint multiset of the image of the matching `(ab | cd)` agrees with that
of the matching `(ac | bd)`. (The third matching follows by symmetry of `emk`.) -/
def Preserves (σ : Edge n ≃ Edge n) : Prop :=
  ∀ a b c d : Fin n, ∀ (hab : a ≠ b) (hcd : c ≠ d) (hac : a ≠ c) (hbd : b ≠ d)
    (_ : a ≠ d) (_ : b ≠ c),
    cnt (σ (emk a b hab)) + cnt (σ (emk c d hcd))
      = cnt (σ (emk a c hac)) + cnt (σ (emk b d hbd))

/-- STEP 1. Two edges whose `σ`-images share a vertex share a vertex themselves. -/
lemma exists_mem_inter {σ : Edge n ≃ Edge n} (hσ : Preserves σ) {e f : Edge n} {u : Fin n}
    (he : u ∈ (σ e).val) (hf : u ∈ (σ f).val) :
    ∃ v, v ∈ e.val ∧ v ∈ f.val := by
  by_contra hdisj
  push_neg at hdisj
  obtain ⟨a, b, hab, hev⟩ := Finset.card_eq_two.mp e.prop
  obtain ⟨c, d, hcd, hfv⟩ := Finset.card_eq_two.mp f.prop
  have ha : a ∈ e.val := by rw [hev]; exact Finset.mem_insert_self _ _
  have hb : b ∈ e.val := by rw [hev]; exact Finset.mem_insert_of_mem (Finset.mem_singleton_self _)
  have hc : c ∈ f.val := by rw [hfv]; exact Finset.mem_insert_self _ _
  have hd : d ∈ f.val := by rw [hfv]; exact Finset.mem_insert_of_mem (Finset.mem_singleton_self _)
  have hac : a ≠ c := fun h => hdisj a ha (h ▸ hc)
  have had : a ≠ d := fun h => hdisj a ha (h ▸ hd)
  have hbc : b ≠ c := fun h => hdisj b hb (h ▸ hc)
  have hbd : b ≠ d := fun h => hdisj b hb (h ▸ hd)
  have heE : e = emk a b hab := Subtype.ext (by rw [emk_val, hev])
  have hfE : f = emk c d hcd := Subtype.ext (by rw [emk_val, hfv])
  have H := hσ a b c d hab hcd hac hbd had hbc
  rw [← heE, ← hfE] at H
  set g₁ := σ (emk a c hac) with hg₁
  set g₂ := σ (emk b d hbd) with hg₂
  -- at u: 1 + 1 forces membership in both cross images
  have hu : u ∈ g₁.val ∧ u ∈ g₂.val := by
    have h1 := congrFun H u
    simp only [Pi.add_apply] at h1
    rw [cnt_apply_of_mem he, cnt_apply_of_mem hf] at h1
    by_cases c1 : u ∈ g₁.val <;> by_cases c2 : u ∈ g₂.val
    · exact ⟨c1, c2⟩
    all_goals
      first
      | (rw [cnt_apply_of_mem c1, cnt_apply_of_not_mem c2] at h1; omega)
      | (rw [cnt_apply_of_not_mem c1, cnt_apply_of_mem c2] at h1; omega)
      | (rw [cnt_apply_of_not_mem c1, cnt_apply_of_not_mem c2] at h1; omega)
  -- at the other endpoint of σ e: one of the cross images coincides with σ e
  set x := oth (σ e) u he with hxdef
  have hx_mem : x ∈ (σ e).val := (oth_spec (σ e) u he).1
  have hx_ne : x ≠ u := (oth_spec (σ e) u he).2
  have hx : x ∈ g₁.val ∨ x ∈ g₂.val := by
    have h1 := congrFun H x
    simp only [Pi.add_apply] at h1
    rw [cnt_apply_of_mem hx_mem] at h1
    by_cases c1 : x ∈ g₁.val
    · exact Or.inl c1
    by_cases c2 : x ∈ g₂.val
    · exact Or.inr c2
    exfalso
    rw [cnt_apply_of_not_mem c1, cnt_apply_of_not_mem c2] at h1
    by_cases cf : x ∈ (σ f).val
    · rw [cnt_apply_of_mem cf] at h1; omega
    · rw [cnt_apply_of_not_mem cf] at h1; omega
  -- either way, injectivity collapses two source edges sharing a vertex — contradiction
  rcases hx with hx1 | hx2
  · have : g₁.val = (σ e).val := by
      rw [eq_pair_of_two_mem hu.1 hx1 hx_ne.symm, val_eq_pair_oth (σ e) u he]
    have hge : g₁ = σ e := Subtype.ext this
    have : emk a c hac = emk a b hab := by
      apply σ.injective
      rw [← hg₁, hge, heE]
    have hcv : c ∈ ({a, b} : Finset (Fin n)) := by
      have hval := congrArg Subtype.val this
      rw [emk_val, emk_val] at hval
      rw [← hval]
      exact Finset.mem_insert_of_mem (Finset.mem_singleton_self _)
    rcases Finset.mem_insert.mp hcv with h | h
    · exact hac h.symm
    · exact hbc (Finset.mem_singleton.mp h).symm
  · have : g₂.val = (σ e).val := by
      rw [eq_pair_of_two_mem hu.2 hx2 hx_ne.symm, val_eq_pair_oth (σ e) u he]
    have hge : g₂ = σ e := Subtype.ext this
    have : emk b d hbd = emk a b hab := by
      apply σ.injective
      rw [← hg₂, hge, heE]
    have hdv : d ∈ ({a, b} : Finset (Fin n)) := by
      have hval := congrArg Subtype.val this
      rw [emk_val, emk_val] at hval
      rw [← hval]
      exact Finset.mem_insert_of_mem (Finset.mem_singleton_self _)
    rcases Finset.mem_insert.mp hdv with h | h
    · exact had h.symm
    · exact hbd ((Finset.mem_singleton.mp h).symm)

/-- A fresh vertex outside any set smaller than `n`. -/
lemma exists_fresh (s : Finset (Fin n)) (h : s.card < n) : ∃ w, w ∉ s := by
  by_contra hall
  push_neg at hall
  have : (Finset.univ : Finset (Fin n)) ⊆ s := fun v _ => hall v
  have := Finset.card_le_card this
  rw [Finset.card_univ, Fintype.card_fin] at this
  omega

/-- STEP 2. For `n ≥ 5`, all edges mapping into the star of `u` share a common vertex. -/
lemma exists_common_vertex {σ : Edge n ≃ Edge n} (hσ : Preserves σ) (hn : 5 ≤ n) (u : Fin n) :
    ∃ a : Fin n, ∀ e : Edge n, u ∈ (σ e).val → a ∈ e.val := by
  -- two distinct star edges and their preimages
  obtain ⟨w₁, hw₁⟩ := exists_fresh {u} (by rw [Finset.card_singleton]; omega)
  have hw₁u : w₁ ≠ u := by simpa using hw₁
  obtain ⟨w₂, hw₂⟩ := exists_fresh {u, w₁}
    (lt_of_le_of_lt (Finset.card_insert_le _ _) (by rw [Finset.card_singleton]; omega))
  have hw₂u : w₂ ≠ u := fun h => hw₂ (h ▸ Finset.mem_insert_self _ _)
  have hw₂w₁ : w₂ ≠ w₁ := fun h =>
    hw₂ (h ▸ Finset.mem_insert_of_mem (Finset.mem_singleton_self _))
  set e₁ := σ.symm (emk u w₁ hw₁u.symm) with he₁
  set e₂ := σ.symm (emk u w₂ hw₂u.symm) with he₂
  have hue₁ : u ∈ (σ e₁).val := by rw [he₁, σ.apply_symm_apply]; exact (mem_emk _).mpr (Or.inl rfl)
  have hue₂ : u ∈ (σ e₂).val := by rw [he₂, σ.apply_symm_apply]; exact (mem_emk _).mpr (Or.inl rfl)
  have he₁₂ : e₁ ≠ e₂ := by
    intro h
    have : emk u w₁ hw₁u.symm = emk u w₂ hw₂u.symm := by
      have := congrArg σ h
      rwa [he₁, he₂, σ.apply_symm_apply, σ.apply_symm_apply] at this
    have hval := congrArg Subtype.val this
    rw [emk_val, emk_val] at hval
    have : w₁ ∈ ({u, w₂} : Finset (Fin n)) := by
      rw [← hval]; exact Finset.mem_insert_of_mem (Finset.mem_singleton_self _)
    rcases Finset.mem_insert.mp this with h' | h'
    · exact hw₁u h'
    · exact hw₂w₁ (Finset.mem_singleton.mp h').symm
  obtain ⟨a, hae₁, hae₂⟩ := exists_mem_inter hσ hue₁ hue₂
  refine ⟨a, ?_⟩
  intro e hue
  by_contra hae
  -- e ≠ e₁, e₂, and e meets both, pinning e₁ = {a,p}, e₂ = {a,q}, e = {p,q}
  obtain ⟨p, hpe, hpe₁⟩ := exists_mem_inter hσ hue hue₁
  obtain ⟨q, hqe, hqe₂⟩ := exists_mem_inter hσ hue hue₂
  have hpa : p ≠ a := fun h => hae (h ▸ hpe)
  have hqa : q ≠ a := fun h => hae (h ▸ hqe)
  have he₁v : e₁.val = {a, p} := eq_pair_of_two_mem hae₁ hpe₁ hpa.symm
  have he₂v : e₂.val = {a, q} := eq_pair_of_two_mem hae₂ hqe₂ hqa.symm
  have hpq : p ≠ q := by
    intro h
    exact he₁₂ (Subtype.ext (by rw [he₁v, he₂v, h]))
  have hev : e.val = {p, q} := eq_pair_of_two_mem hpe hqe hpq
  -- a fourth star edge whose preimage avoids the triangle
  set y := oth (σ e) u hue with hy
  have hyu : y ≠ u := (oth_spec (σ e) u hue).2
  obtain ⟨w, hw⟩ := exists_fresh {u, w₁, w₂, y} (by
    calc ({u, w₁, w₂, y} : Finset (Fin n)).card
        ≤ 4 := by
          refine le_trans (Finset.card_insert_le _ _) ?_
          refine Nat.succ_le_succ ?_
          refine le_trans (Finset.card_insert_le _ _) ?_
          refine Nat.succ_le_succ ?_
          refine le_trans (Finset.card_insert_le _ _) ?_
          simp
      _ < n := by omega)
  have hwu : w ≠ u := fun h => hw (h ▸ Finset.mem_insert_self _ _)
  have hww₁ : w ≠ w₁ := fun h => hw (by rw [h]; simp)
  have hww₂ : w ≠ w₂ := fun h => hw (by rw [h]; simp)
  have hwy : w ≠ y := fun h => hw (by rw [h]; simp)
  set e' := σ.symm (emk u w hwu.symm) with he'
  have hue' : u ∈ (σ e').val := by
    rw [he', σ.apply_symm_apply]; exact (mem_emk _).mpr (Or.inl rfl)
  have he'e : e' ≠ e := by
    intro h
    have : emk u w hwu.symm = σ e := by rw [← h, he', σ.apply_symm_apply]
    have hyv : y ∈ ({u, w} : Finset (Fin n)) := by
      have hval := congrArg Subtype.val this
      rw [emk_val] at hval
      rw [hval]
      exact (oth_spec (σ e) u hue).1
    rcases Finset.mem_insert.mp hyv with h' | h'
    · exact hyu h'
    · exact hwy (Finset.mem_singleton.mp h').symm
  have he'e₁ : e' ≠ e₁ := by
    intro h
    have : emk u w hwu.symm = emk u w₁ hw₁u.symm := by
      have := congrArg σ h
      rwa [he', he₁, σ.apply_symm_apply, σ.apply_symm_apply] at this
    have hval := congrArg Subtype.val this
    rw [emk_val, emk_val] at hval
    have : w ∈ ({u, w₁} : Finset (Fin n)) := by
      rw [← hval]; exact Finset.mem_insert_of_mem (Finset.mem_singleton_self _)
    rcases Finset.mem_insert.mp this with h' | h'
    · exact hwu h'
    · exact hww₁ (Finset.mem_singleton.mp h')
  have he'e₂ : e' ≠ e₂ := by
    intro h
    have : emk u w hwu.symm = emk u w₂ hw₂u.symm := by
      have := congrArg σ h
      rwa [he', he₂, σ.apply_symm_apply, σ.apply_symm_apply] at this
    have hval := congrArg Subtype.val this
    rw [emk_val, emk_val] at hval
    have : w ∈ ({u, w₂} : Finset (Fin n)) := by
      rw [← hval]; exact Finset.mem_insert_of_mem (Finset.mem_singleton_self _)
    rcases Finset.mem_insert.mp this with h' | h'
    · exact hwu h'
    · exact hww₂ (Finset.mem_singleton.mp h')
  -- if e' avoids a, it equals e; so a ∈ e', and then e' cannot meet e at all
  by_cases hae' : a ∈ e'.val
  · -- e' = {a, r} with r ∉ {p, q}; but e' must meet e = {p, q}
    obtain ⟨s, hse', hse⟩ := exists_mem_inter hσ hue' hue
    have hsa : s ≠ a := by
      intro h
      rw [hev] at hse
      rcases Finset.mem_insert.mp hse with h' | h'
      · exact hpa (by rw [← h, h'])
      · exact hqa (by rw [← h, Finset.mem_singleton.mp h'])
    have he'v : e'.val = {a, s} := eq_pair_of_two_mem hae' hse' hsa.symm
    rw [hev] at hse
    rcases Finset.mem_insert.mp hse with h' | h'
    · -- s = p forces e' = {a, p} = e₁
      exact he'e₁ (Subtype.ext (by rw [he'v, he₁v, h']))
    · exact he'e₂ (Subtype.ext (by rw [he'v, he₂v, Finset.mem_singleton.mp h']))
  · -- a ∉ e': repeat the pinning to get e'.val = {p, q} = e.val
    obtain ⟨p', hp'e', hp'e₁⟩ := exists_mem_inter hσ hue' hue₁
    obtain ⟨q', hq'e', hq'e₂⟩ := exists_mem_inter hσ hue' hue₂
    have hp'a : p' ≠ a := fun h => hae' (h ▸ hp'e')
    have hq'a : q' ≠ a := fun h => hae' (h ▸ hq'e')
    have hp'p : p' = p := by
      rw [he₁v] at hp'e₁
      rcases Finset.mem_insert.mp hp'e₁ with h' | h'
      · exact absurd h' hp'a
      · exact Finset.mem_singleton.mp h'
    have hq'q : q' = q := by
      rw [he₂v] at hq'e₂
      rcases Finset.mem_insert.mp hq'e₂ with h' | h'
      · exact absurd h' hq'a
      · exact Finset.mem_singleton.mp h'
    have he'v : e'.val = {p, q} :=
      eq_pair_of_two_mem (hp'p ▸ hp'e') (hq'q ▸ hq'e') hpq
    exact he'e (Subtype.ext (by rw [he'v, hev]))

/-- The star of a vertex has `n - 1` edges. -/
lemma card_star (v : Fin n) :
    (Finset.univ.filter fun e : Edge n => v ∈ e.val).card = n - 1 := by
  have : ((Finset.univ : Finset (Fin n)).erase v).card = n - 1 := by
    rw [Finset.card_erase_of_mem (Finset.mem_univ v), Finset.card_univ, Fintype.card_fin]
  rw [← this]
  apply Finset.card_bij (fun e he => oth e v (by simpa using (Finset.mem_filter.mp he).2))
  · intro e he
    have hv : v ∈ e.val := (Finset.mem_filter.mp he).2
    exact Finset.mem_erase.mpr ⟨(oth_spec e v hv).2, Finset.mem_univ _⟩
  · intro e₁ h₁ e₂ h₂ heq
    have hv₁ : v ∈ e₁.val := (Finset.mem_filter.mp h₁).2
    have hv₂ : v ∈ e₂.val := (Finset.mem_filter.mp h₂).2
    apply Subtype.ext
    rw [val_eq_pair_oth e₁ v hv₁, val_eq_pair_oth e₂ v hv₂, heq]
  · intro w hw
    have hwv : w ≠ v := (Finset.mem_erase.mp hw).1
    refine ⟨emk v w hwv.symm, Finset.mem_filter.mpr ⟨Finset.mem_univ _, ?_⟩, ?_⟩
    · exact (mem_emk _).mpr (Or.inl rfl)
    · exact oth_eq _ ((mem_emk _).mpr (Or.inr rfl)) hwv

/-- STEP 3. The containment of step 2 is an equality: membership of `u` in the image is
membership of `a` in the source. -/
lemma exists_star_vertex {σ : Edge n ≃ Edge n} (hσ : Preserves σ) (hn : 5 ≤ n) (u : Fin n) :
    ∃ a : Fin n, ∀ e : Edge n, u ∈ (σ e).val ↔ a ∈ e.val := by
  obtain ⟨a, ha⟩ := exists_common_vertex hσ hn u
  refine ⟨a, ?_⟩
  have hsub : (Finset.univ.filter fun e : Edge n => u ∈ (σ e).val)
      ⊆ Finset.univ.filter fun e : Edge n => a ∈ e.val := by
    intro e he
    exact Finset.mem_filter.mpr ⟨Finset.mem_univ _, ha e (Finset.mem_filter.mp he).2⟩
  have hcards : (Finset.univ.filter fun e : Edge n => u ∈ (σ e).val).card
      = (Finset.univ.filter fun e : Edge n => a ∈ e.val).card := by
    rw [card_star]
    rw [← card_star (n := n) u]
    apply Finset.card_bij (fun e _ => σ e)
    · intro e he
      exact Finset.mem_filter.mpr ⟨Finset.mem_univ _, (Finset.mem_filter.mp he).2⟩
    · intro e₁ _ e₂ _ heq
      exact σ.injective heq
    · intro f hf
      refine ⟨σ.symm f, Finset.mem_filter.mpr ⟨Finset.mem_univ _, ?_⟩, σ.apply_symm_apply f⟩
      rw [σ.apply_symm_apply]
      exact (Finset.mem_filter.mp hf).2
  have heq := Finset.eq_of_subset_of_card_le hsub (le_of_eq hcards.symm)
  intro e
  constructor
  · intro h
    exact ha e h
  · intro h
    have : e ∈ Finset.univ.filter fun e : Edge n => a ∈ e.val :=
      Finset.mem_filter.mpr ⟨Finset.mem_univ _, h⟩
    rw [← heq] at this
    exact (Finset.mem_filter.mp this).2

/-- K4-RIGIDITY. For `n ≥ 5`, an edge permutation preserving all four-cycle product identities
as identities is induced by a vertex permutation. Sharp: `compl4_preserves` and
`compl4_not_induced` below exhibit the `n = 4` complement exception. -/
theorem k4_rigidity (hn : 5 ≤ n) (σ : Edge n ≃ Edge n) (hσ : Preserves σ) :
    ∃ τ : Fin n ≃ Fin n, ∀ a b (hab : a ≠ b),
      σ (emk a b hab) = emk (τ a) (τ b) (fun h => hab (τ.injective h)) := by
  choose A hA using fun u => exists_star_vertex hσ hn u
  have hAinj : Function.Injective A := by
    intro u u' huu'
    by_contra hne
    obtain ⟨x, hx⟩ := exists_fresh {u, u'}
      (lt_of_le_of_lt (Finset.card_insert_le _ _) (by rw [Finset.card_singleton]; omega))
    have hxu : x ≠ u := fun h => hx (h ▸ Finset.mem_insert_self _ _)
    have hxu' : x ≠ u' := fun h =>
      hx (h ▸ Finset.mem_insert_of_mem (Finset.mem_singleton_self _))
    -- the edge {u, x} contains u but not u', yet A u = A u' forces both memberships to agree
    set f := emk u x hxu.symm with hf
    have h1 : u ∈ (σ (σ.symm f)).val := by
      rw [σ.apply_symm_apply]; exact (mem_emk _).mpr (Or.inl rfl)
    have h2 : A u ∈ (σ.symm f).val := (hA u (σ.symm f)).mp h1
    have h3 : u' ∈ (σ (σ.symm f)).val := (hA u' (σ.symm f)).mpr (huu' ▸ h2)
    rw [σ.apply_symm_apply] at h3
    rcases (mem_emk _).mp h3 with h | h
    · exact hne h.symm
    · exact hxu' h.symm
  have hAbij : Function.Bijective A := (Finite.injective_iff_bijective).mp hAinj
  set E := Equiv.ofBijective A hAbij with hE
  refine ⟨E.symm, ?_⟩
  intro a b hab
  apply Subtype.ext
  apply Finset.ext
  intro v
  have hv : v ∈ (σ (emk a b hab)).val ↔ A v ∈ ({a, b} : Finset (Fin n)) := by
    rw [← emk_val a b hab]
    exact hA v (emk a b hab)
  rw [hv, emk_val]
  have hva : A v = a ↔ v = E.symm a := by
    constructor
    · intro h
      apply E.injective
      rw [E.apply_symm_apply]
      exact h
    · intro h
      have := congrArg E h
      rw [E.apply_symm_apply] at this
      exact this
  have hvb : A v = b ↔ v = E.symm b := by
    constructor
    · intro h
      apply E.injective
      rw [E.apply_symm_apply]
      exact h
    · intro h
      have := congrArg E h
      rw [E.apply_symm_apply] at this
      exact this
  simp only [Finset.mem_insert, Finset.mem_singleton]
  rw [hva, hvb]

/-- The vertex-induced edge permutation, one branch's shadow at the modulus level. -/
def indPerm (τ : Fin n ≃ Fin n) : Edge n ≃ Edge n where
  toFun e := ⟨e.val.image τ, by rw [Finset.card_image_of_injective _ τ.injective, e.prop]⟩
  invFun e := ⟨e.val.image τ.symm, by rw [Finset.card_image_of_injective _ τ.symm.injective, e.prop]⟩
  left_inv e := Subtype.ext (by
    simp only [Finset.image_image]
    have : (τ.symm ∘ τ) = id := by
      funext x; simp
    rw [this, Finset.image_id])
  right_inv e := Subtype.ext (by
    simp only [Finset.image_image]
    have : (τ ∘ τ.symm) = id := by
      funext x; simp
    rw [this, Finset.image_id])

/-- POSITIVE CONTROL: induced permutations preserve every four-cycle identity. -/
theorem induced_preserves (τ : Fin n ≃ Fin n) : Preserves (indPerm τ) := by
  intro a b c d hab hcd hac hbd had hbc
  have key : ∀ (x y : Fin n) (hxy : x ≠ y),
      indPerm τ (emk x y hxy) = emk (τ x) (τ y) (fun h => hxy (τ.injective h)) := by
    intro x y hxy
    apply Subtype.ext
    show ({x, y} : Finset (Fin n)).image τ = {τ x, τ y}
    rw [Finset.image_insert, Finset.image_singleton]
  rw [key a b hab, key c d hcd, key a c hac, key b d hbd]
  rw [cnt_emk, cnt_emk, cnt_emk, cnt_emk]
  funext v
  simp only [Pi.add_apply]
  ring

/-- THE MANUSCRIPT-FACING COROLLARY. A non-induced edge permutation forces a nontrivial exponent
relation on the log-moduli: a nonzero integer vector `w`, summing to zero (so uniform rows always
satisfy it — the flat locus survives this layer by construction), such that every `L` satisfying
the pulled-back four-cycle identities lies on the hyperplane `w · L = 0`. -/
theorem exceptional_relation (hn : 5 ≤ n) (σ : Edge n ≃ Edge n)
    (h : ¬∃ τ : Fin n ≃ Fin n, ∀ a b (hab : a ≠ b),
      σ (emk a b hab) = emk (τ a) (τ b) (fun h' => hab (τ.injective h'))) :
    ∃ w : Fin n → ℤ, w ≠ 0 ∧ (∑ v, w v) = 0 ∧
      ∀ L : Fin n → ℚ,
        (∀ a b c d : Fin n, ∀ (hab : a ≠ b) (hcd : c ≠ d) (hac : a ≠ c) (hbd : b ≠ d)
          (_ : a ≠ d) (_ : b ≠ c),
          (∑ v ∈ (σ (emk a b hab)).val, L v) + (∑ v ∈ (σ (emk c d hcd)).val, L v)
            = (∑ v ∈ (σ (emk a c hac)).val, L v) + (∑ v ∈ (σ (emk b d hbd)).val, L v)) →
        (∑ v, (w v : ℚ) * L v) = 0 := by
  have hnp : ¬ Preserves σ := fun hp => h (k4_rigidity hn σ hp)
  unfold Preserves at hnp
  push_neg at hnp
  obtain ⟨a, b, c, d, hab, hcd, hac, hbd, had, hbc, hne⟩ := hnp
  refine ⟨(cnt (σ (emk a b hab)) + cnt (σ (emk c d hcd)))
    - (cnt (σ (emk a c hac)) + cnt (σ (emk b d hbd))), ?_, ?_, ?_⟩
  · exact sub_ne_zero_of_ne hne
  · simp only [Pi.sub_apply, Pi.add_apply]
    rw [Finset.sum_sub_distrib, Finset.sum_add_distrib, Finset.sum_add_distrib,
      sum_cnt, sum_cnt, sum_cnt, sum_cnt]
    norm_num
  · intro L hL
    have hinst := hL a b c d hab hcd hac hbd had hbc
    have expand : ∀ e : Edge n, (∑ v, (cnt e v : ℚ) * L v) = ∑ v ∈ e.val, L v := by
      intro e
      have h1 : ∀ v, (cnt e v : ℚ) * L v = if v ∈ e.val then L v else 0 := by
        intro v
        unfold cnt
        split_ifs <;> simp
      rw [Finset.sum_congr rfl (fun v _ => h1 v), ← Finset.sum_filter]
      congr 1
      ext v
      simp
    have hsplit : ∑ v, ((((cnt (σ (emk a b hab)) v + cnt (σ (emk c d hcd)) v)
          - (cnt (σ (emk a c hac)) v + cnt (σ (emk b d hbd)) v) : ℤ) : ℚ)) * L v
        = ((∑ v, (cnt (σ (emk a b hab)) v : ℚ) * L v)
            + ∑ v, (cnt (σ (emk c d hcd)) v : ℚ) * L v)
          - ((∑ v, (cnt (σ (emk a c hac)) v : ℚ) * L v)
            + ∑ v, (cnt (σ (emk b d hbd)) v : ℚ) * L v) := by
      rw [← Finset.sum_add_distrib, ← Finset.sum_add_distrib, ← Finset.sum_sub_distrib]
      apply Finset.sum_congr rfl
      intro v _
      push_cast
      ring
    simp only [Pi.sub_apply, Pi.add_apply]
    rw [hsplit, expand, expand, expand, expand, hinst]
    ring

/-- CONTROL: uniform log-moduli satisfy every pulled-back identity for every edge permutation.
The exceptional relations of `exceptional_relation` never exclude the flat row — that is exactly
why the n = 6 analysis found its exceptional locus there. -/
theorem pulledBack_const (σ : Edge n ≃ Edge n) (c : ℚ) :
    ∀ a b c' d : Fin n, ∀ (hab : a ≠ b) (hcd : c' ≠ d) (hac : a ≠ c') (hbd : b ≠ d)
      (_ : a ≠ d) (_ : b ≠ c'),
      (∑ _v ∈ (σ (emk a b hab)).val, c) + (∑ _v ∈ (σ (emk c' d hcd)).val, c)
        = (∑ _v ∈ (σ (emk a c' hac)).val, c) + (∑ _v ∈ (σ (emk b d hbd)).val, c) := by
  intro a b c' d hab hcd hac hbd _ _
  rw [Finset.sum_const, Finset.sum_const, Finset.sum_const, Finset.sum_const,
    (σ _).prop, (σ _).prop, (σ _).prop, (σ _).prop]

/-- THE n = 4 EXCEPTION: complementation on the six edges of K₄. -/
def compl4 : Edge 4 ≃ Edge 4 :=
  Function.Involutive.toPerm
    (fun e => ⟨e.valᶜ, by rw [Finset.card_compl, e.prop]; rfl⟩)
    (fun e => Subtype.ext (by simp))

/-- The complement map preserves every four-cycle identity: each matching of a 4-set covers all
four vertices, and complementation permutes the three matchings of the SAME 4-set. -/
theorem compl4_preserves : Preserves compl4 := by
  unfold Preserves
  decide

/-- ...and yet no vertex permutation induces it: the hypersimplex Δ(2,4) exception is real,
so the `n ≥ 5` hypothesis of `k4_rigidity` is sharp. -/
theorem compl4_not_induced :
    ¬∃ τ : Fin 4 ≃ Fin 4, ∀ a b (hab : a ≠ b),
      compl4 (emk a b hab) = emk (τ a) (τ b) (fun h => hab (τ.injective h)) := by
  decide

#print axioms k4_rigidity
#print axioms exceptional_relation
#print axioms induced_preserves
#print axioms pulledBack_const
#print axioms compl4_preserves
#print axioms compl4_not_induced

end OIBridge
