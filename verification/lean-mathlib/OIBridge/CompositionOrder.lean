/-
  OIBridge/CompositionOrder.lean — round ORD-1: iterated operation data and finite or infinite
  order on the completed body.

  An operation datum of `CompletionAction` that respects affine relations is composed with itself
  through the landed composition law `after`, and the order of the affine automorphism it induces
  on the chart body is studied. Order is a property of a single automorphism on a set of states:
  infinite order means that every positive power moves some state of the set, finite order that
  some positive power fixes every state of the set. ORD∞ is the predicate on a set of
  automorphisms that some member has infinite order.

  Proved here:
    §B  the `m`-fold composite of a datum respects affine relations, and the map it induces is
        the `m`-fold composite of the induced map (`induced_iterAfter`, `coe_induced_iterAfter`);
    §C  a reversible datum whose induced automorphism has infinite order on the chart body has
        every positive power nontrivial on the preparations (`exists_moved_of_infiniteOrderOn`);
    §D  a reversible datum that carries each stage's preparations to preparation vectors of the
        same stage induces an automorphism of finite order on the chart body
        (`finiteOrderOn_of_stagePreserving`), through a finite affinely spanning subset of the
        chart generators (`exists_finset_affineSpan_eq_top`) and a common period on it;
    §E  controls: finite and infinite order exclude each other, the identity and the Householder
        reflections of the ball have finite order, the rotation by one radian has infinite order
        on the ball, the Householder set has no member of infinite order, the automorphisms of the
        ball, the rotation family and the singleton of the one-radian rotation each have one, and
        a finite composition-closed set has none (`not_ordInf_of_finite_of_mulClosed`), with the
        singleton as the countercontrol for the closure hypothesis;
    §F  the verdict `ord1_core`.

  No transitivity, ball, dimension, drive or flow is claimed; TRANS ⇒ ORD∞ is not stated. Nothing
  here supplies an operation datum, finite rank, a completion chart or the stage-preservation
  hypothesis from an OI construction.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.CompletionAction
import Mathlib.Analysis.Real.Pi.Irrational

namespace OIBridge
namespace CompositionOrder

open Set KInfFoundations OrbitGeneration OrbitNormalization StageCompletion CompletionAction

/-! ### §A — order predicates and iterated composition -/

section Order

variable {V : Type*} [AddCommGroup V] [Module ℝ V]

/-- Infinite order on `Ω`: every positive power moves some state of `Ω`. Iteration is of the
underlying function. -/
def InfiniteOrderOn (Ω : Set V) (g : V ≃ᵃ[ℝ] V) : Prop :=
  ∀ m : ℕ, 1 ≤ m → ∃ x ∈ Ω, (⇑g)^[m] x ≠ x

/-- Finite order on `Ω`: some positive power fixes every state of `Ω`. -/
def FiniteOrderOn (Ω : Set V) (g : V ≃ᵃ[ℝ] V) : Prop :=
  ∃ N : ℕ, 1 ≤ N ∧ ∀ x ∈ Ω, (⇑g)^[N] x = x

/-- **ORD∞**: some member of `G` has infinite order on `Ω`. A predicate on a set of affine
automorphisms; nothing about closure. -/
def OrdInf (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)) : Prop := ∃ g ∈ G, InfiniteOrderOn Ω g

/-- Composition closure of a set of affine automorphisms. -/
def MulClosed (G : Set (V ≃ᵃ[ℝ] V)) : Prop := ∀ g ∈ G, ∀ h ∈ G, g.trans h ∈ G

/-- The `m`-fold composite of an affine self-map, by recursion. -/
def affPow (Φ : V →ᵃ[ℝ] V) : ℕ → V →ᵃ[ℝ] V
  | 0 => AffineMap.id ℝ V
  | m + 1 => Φ.comp (affPow Φ m)

theorem coe_affPow (Φ : V →ᵃ[ℝ] V) (m : ℕ) : ⇑(affPow Φ m) = (⇑Φ)^[m] := by
  induction m with
  | zero => rfl
  | succ k ih =>
    exact (congrArg (fun f => ⇑Φ ∘ f) ih).trans (Function.iterate_succ' (⇑Φ) k).symm

/-- Finite order is the negation of infinite order, one direction. -/
theorem finiteOrderOn_of_not_infiniteOrderOn {Ω : Set V} {g : V ≃ᵃ[ℝ] V}
    (h : ¬ InfiniteOrderOn Ω g) : FiniteOrderOn Ω g := by
  unfold InfiniteOrderOn at h
  push_neg at h
  exact h

/-- Finite order is the negation of infinite order, the other direction. -/
theorem not_infiniteOrderOn_of_finiteOrderOn {Ω : Set V} {g : V ≃ᵃ[ℝ] V}
    (h : FiniteOrderOn Ω g) : ¬ InfiniteOrderOn Ω g := by
  intro hinf
  obtain ⟨N, hN, hfix⟩ := h
  obtain ⟨x, hx, hne⟩ := hinf N hN
  exact hne (hfix x hx)

theorem not_infiniteOrderOn_iff {Ω : Set V} {g : V ≃ᵃ[ℝ] V} :
    ¬ InfiniteOrderOn Ω g ↔ FiniteOrderOn Ω g :=
  ⟨finiteOrderOn_of_not_infiniteOrderOn, not_infiniteOrderOn_of_finiteOrderOn⟩

/-- The identity has finite order on every set. -/
theorem finiteOrderOn_refl (Ω : Set V) : FiniteOrderOn Ω (AffineEquiv.refl ℝ V) :=
  ⟨1, le_rfl, fun _ _ => rfl⟩

/-- Two distinct powers of an automorphism that agree as functions give it finite order. -/
theorem finiteOrderOn_of_iterate_eq {Ω : Set V} {g : V ≃ᵃ[ℝ] V} {a b : ℕ} (hab : a < b)
    (h : (⇑g)^[a] = (⇑g)^[b]) : FiniteOrderOn Ω g := by
  refine ⟨b - a, by omega, fun x _ => ?_⟩
  apply g.injective.iterate a
  rw [← Function.iterate_add_apply, Nat.add_sub_of_le hab.le, ← h]

/-- **Closure control.** A finite composition-closed set of affine automorphisms has no member of
infinite order on any set: the composites of a member with itself stay in the set, two of them
coincide, and cancellation gives a positive power fixing everything. -/
theorem not_ordInf_of_finite_of_mulClosed {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)} (hG : G.Finite)
    (hcl : MulClosed G) : ¬ OrdInf Ω G := by
  rintro ⟨g, hg, hinf⟩
  obtain ⟨gpow, h0, hsucc⟩ : ∃ gpow : ℕ → V ≃ᵃ[ℝ] V, gpow 0 = g ∧
      ∀ n, gpow (n + 1) = (gpow n).trans g :=
    ⟨fun n => (fun e : V ≃ᵃ[ℝ] V => e.trans g)^[n] g, rfl,
      fun n => Function.iterate_succ_apply' _ n g⟩
  have hmem : ∀ n, gpow n ∈ G := by
    intro n
    induction n with
    | zero => rw [h0]; exact hg
    | succ k ih => rw [hsucc]; exact hcl _ ih _ hg
  have hcoe : ∀ n, ⇑(gpow n) = (⇑g)^[n + 1] := by
    intro n
    induction n with
    | zero => rw [h0]; exact (Function.iterate_one (⇑g)).symm
    | succ k ih =>
      rw [hsucc, AffineEquiv.coe_trans, ih]
      exact (Function.iterate_succ' (⇑g) (k + 1)).symm
  haveI : _root_.Finite ↥G := hG.to_subtype
  obtain ⟨a, b, hab, heq⟩ :=
    _root_.Finite.exists_ne_map_eq_of_infinite (fun n : ℕ => (⟨gpow n, hmem n⟩ : ↥G))
  have heq' : (⇑g)^[a + 1] = (⇑g)^[b + 1] := by
    rw [← hcoe, ← hcoe]
    exact congrArg DFunLike.coe (congrArg Subtype.val heq)
  rcases Nat.lt_or_ge a b with hlt | hge
  · exact not_infiniteOrderOn_of_finiteOrderOn
      (finiteOrderOn_of_iterate_eq (Ω := Ω) (by omega : a + 1 < b + 1) heq') hinf
  · exact not_infiniteOrderOn_of_finiteOrderOn
      (finiteOrderOn_of_iterate_eq (Ω := Ω) (by omega : b + 1 < a + 1) heq'.symm) hinf

end Order

/-! ### §A′ — finite extraction and periods, stated generically -/

section Generic

variable {α : Type*}

/-- A finite set carried into itself by an injective map returns every point. -/
theorem exists_return {S : Finset α} {f : α → α} (hf : Function.Injective f)
    (hm : ∀ w ∈ S, f w ∈ S) {w : α} (hw : w ∈ S) : ∃ p : ℕ, 0 < p ∧ f^[p] w = w := by
  have hmem : ∀ n : ℕ, f^[n] w ∈ S := by
    intro n
    induction n with
    | zero => exact hw
    | succ k ih => rw [Function.iterate_succ_apply']; exact hm _ ih
  obtain ⟨a, b, hab, heq⟩ :=
    _root_.Finite.exists_ne_map_eq_of_infinite (fun n : ℕ => (⟨f^[n] w, hmem n⟩ : ↥S))
  have heq' : f^[a] w = f^[b] w := congrArg Subtype.val heq
  rcases Nat.lt_or_ge a b with hlt | hge
  · refine ⟨b - a, by omega, ?_⟩
    apply hf.iterate a
    rw [← Function.iterate_add_apply, Nat.add_sub_of_le hlt.le]
    exact heq'.symm
  · have hlt : b < a := lt_of_le_of_ne hge (Ne.symm hab)
    refine ⟨a - b, by omega, ?_⟩
    apply hf.iterate b
    rw [← Function.iterate_add_apply, Nat.add_sub_of_le hlt.le]
    exact heq'

/-- Points of a finite set that each return under some positive power return together. -/
theorem exists_common_period {f : α → α} (A : Finset α)
    (h : ∀ w ∈ A, ∃ p : ℕ, 0 < p ∧ f^[p] w = w) :
    ∃ N : ℕ, 1 ≤ N ∧ ∀ w ∈ A, f^[N] w = w := by
  classical
  induction A using Finset.induction_on with
  | empty => exact ⟨1, le_rfl, fun w hw => absurd hw (Finset.notMem_empty w)⟩
  | insert a A ha ih =>
    obtain ⟨N, hN, hNA⟩ := ih fun w hw => h w (Finset.mem_insert_of_mem hw)
    obtain ⟨p, hp, hpa⟩ := h a (Finset.mem_insert_self a A)
    refine ⟨N * p, Nat.mul_pos hN hp, fun w hw => ?_⟩
    rcases Finset.mem_insert.1 hw with rfl | hw
    · rw [mul_comm, Function.iterate_mul]
      exact Function.iterate_fixed hpa N
    · rw [Function.iterate_mul]
      exact Function.iterate_fixed (hNA w hw) p

/-- **Finite extraction.** A set that affinely spans a finite-dimensional space contains a finite
subset that affinely spans it. -/
theorem exists_finset_affineSpan_eq_top {V P : Type*} [AddCommGroup V] [Module ℝ V]
    [AddTorsor V P] [FiniteDimensional ℝ V] {s : Set P} (h : affineSpan ℝ s = ⊤) :
    ∃ t : Finset P, (↑t : Set P) ⊆ s ∧ affineSpan ℝ (↑t : Set P) = ⊤ := by
  classical
  obtain ⟨p, hp⟩ := AffineSubspace.nonempty_of_affineSpan_eq_top ℝ V P h
  have hvs : Submodule.span ℝ ((· -ᵥ p) '' s) = ⊤ := by
    rw [← vectorSpan_eq_span_vsub_set_right ℝ hp]
    exact AffineSubspace.vectorSpan_eq_top_of_affineSpan_eq_top ℝ V P h
  obtain ⟨b, hbs, hspan, hli⟩ := exists_linearIndependent ℝ ((· -ᵥ p) '' s)
  have hbfin : b.Finite := hli.set_finite_of_isNoetherian
  have hfin : (insert p ((· +ᵥ p) '' b)).Finite := (hbfin.image _).insert p
  refine ⟨hfin.toFinset, ?_, ?_⟩
  · rw [Set.Finite.coe_toFinset]
    refine Set.insert_subset hp ?_
    rintro _ ⟨v, hv, rfl⟩
    obtain ⟨q, hq, rfl⟩ := hbs hv
    show (q -ᵥ p) +ᵥ p ∈ s
    rw [vsub_vadd]
    exact hq
  · rw [Set.Finite.coe_toFinset,
      AffineSubspace.affineSpan_eq_top_iff_vectorSpan_eq_top_of_nonempty ℝ V P
        (s := insert p ((· +ᵥ p) '' b)) ⟨p, Set.mem_insert p _⟩,
      vectorSpan_eq_span_vsub_set_right ℝ (s := insert p ((· +ᵥ p) '' b)) (Set.mem_insert p _),
      eq_top_iff]
    calc (⊤ : Submodule ℝ V) = Submodule.span ℝ ((· -ᵥ p) '' s) := hvs.symm
      _ = Submodule.span ℝ b := hspan.symm
      _ ≤ Submodule.span ℝ ((· -ᵥ p) '' insert p ((· +ᵥ p) '' b)) := by
        apply Submodule.span_mono
        intro v hv
        exact ⟨v +ᵥ p, Set.mem_insert_of_mem _ (Set.mem_image_of_mem (fun x => x +ᵥ p) hv),
          vadd_vsub v p⟩

end Generic

/-! ### §B — iteration through the composition law -/

variable {D : DirectedStages}

/-- The identity datum: every preparation to its own preparation vector. -/
def idDatum (D : DirectedStages) : OpDatum D where
  τ := prepVec D
  mem_body := prepVec_mem_body D

/-- **Stage preservation**: each preparation of stage `i` is carried to a preparation vector of
the same stage `i`. -/
def StagePreserving (T : OpDatum D) : Prop :=
  ∀ (i : D.ι) (x : (D.stage i).P), ∃ y : (D.stage i).P, T.τ ⟨i, x⟩ = prepVec D ⟨i, y⟩

theorem affineRespect_idDatum : AffineRespect (idDatum D) := fun _ _ _ h => h

variable (C : CompletionChart D)

/-- The `m`-fold composite of a datum with itself, through the landed composition law `after`. -/
noncomputable def iterAfter (T : OpDatum D) (hT : AffineRespect T) : ℕ → OpDatum D
  | 0 => idDatum D
  | m + 1 => after C T (iterAfter T hT m) hT

/-- The chart coordinates of the preparations of one stage, as a finset. -/
noncomputable def stageGen (i : D.ι) : Finset (Fin C.d → ℝ) := by
  classical exact Finset.univ.image fun y : (D.stage i).P => gen C ⟨i, y⟩

theorem induced_idDatum : induced C (idDatum D) affineRespect_idDatum = AffineMap.id ℝ _ :=
  induced_unique C fun x => by rw [induced_gen, AffineMap.id_apply]; try rfl

theorem affineRespect_iterAfter {T : OpDatum D} (hT : AffineRespect T) (m : ℕ) :
    AffineRespect (iterAfter C T hT m) := by
  induction m with
  | zero => exact affineRespect_idDatum
  | succ k ih => exact affineRespect_after C hT ih

/-- **Iterated composition.** The map induced by the `m`-fold composite is the `m`-fold composite
of the induced map. -/
theorem induced_iterAfter {T : OpDatum D} (hT : AffineRespect T) (m : ℕ) :
    induced C (iterAfter C T hT m) (affineRespect_iterAfter C hT m) =
      affPow (induced C T hT) m := by
  induction m with
  | zero => exact induced_idDatum C
  | succ k ih =>
    show induced C (after C T (iterAfter C T hT k) hT) _ =
      (induced C T hT).comp (affPow (induced C T hT) k)
    rw [← ih]
    exact induced_after C hT (affineRespect_iterAfter C hT k)

theorem coe_induced_iterAfter {T : OpDatum D} (hT : AffineRespect T) (m : ℕ) :
    ⇑(induced C (iterAfter C T hT m) (affineRespect_iterAfter C hT m)) =
      (⇑(induced C T hT))^[m] := by
  rw [induced_iterAfter, coe_affPow]

theorem coe_inducedEquiv {S T : OpDatum D} (hS : AffineRespect S) (hT : AffineRespect T)
    (hST : Undoes C S T hS) (hTS : Undoes C T S hT) :
    ⇑(inducedEquiv C hS hT hST hTS) = ⇑(induced C T hT) :=
  funext fun _ => rfl

/-! ### §C — an infinite-order datum keeps every power nontrivial -/

/-- A composite that returns every preparation induces the identity power. -/
theorem iterate_eq_id_of_fix {T : OpDatum D} (hT : AffineRespect T) (m : ℕ)
    (h : ∀ x, (iterAfter C T hT m).τ x = prepVec D x) : (⇑(induced C T hT))^[m] = id := by
  have h1 : induced C (iterAfter C T hT m) (affineRespect_iterAfter C hT m) =
      AffineMap.id ℝ _ :=
    induced_unique C fun x => by rw [induced_gen, h x, AffineMap.id_apply]; try rfl
  have h2 := congrArg DFunLike.coe h1
  rw [coe_induced_iterAfter C hT m] at h2
  exact h2

/-- **Every power of an infinite-order datum is nontrivial.** -/
theorem exists_moved_of_infiniteOrderOn {S T : OpDatum D} (hS : AffineRespect S)
    (hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT)
    (h : InfiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS)) :
    ∀ m : ℕ, 1 ≤ m → AffineRespect (iterAfter C T hT m) ∧
      ∃ x, (iterAfter C T hT m).τ x ≠ prepVec D x := by
  intro m hm
  refine ⟨affineRespect_iterAfter C hT m, ?_⟩
  by_contra hcon
  push_neg at hcon
  obtain ⟨w, -, hw⟩ := h m hm
  apply hw
  rw [coe_inducedEquiv]
  exact congrFun (iterate_eq_id_of_fix C hT m hcon) w

/-! ### §D — stage preservation and reversibility give finite order -/

theorem nonempty_prep (C : CompletionChart D) : Nonempty (Prep D) := by
  obtain ⟨_, x, -⟩ := AffineSubspace.nonempty_of_affineSpan_eq_top ℝ (Fin C.d → ℝ)
    (Fin C.d → ℝ) (affineSpan_gen C)
  exact ⟨x⟩

/-- A finite set of preparations whose chart coordinates affinely span the chart. -/
theorem exists_gen_finset :
    ∃ A : Finset (Prep D),
      affineSpan ℝ ((A.image (gen C) : Finset (Fin C.d → ℝ)) : Set (Fin C.d → ℝ)) = ⊤ := by
  classical
  obtain ⟨t, hts, ht⟩ := exists_finset_affineSpan_eq_top (affineSpan_gen C)
  have hts' : (t : Set (Fin C.d → ℝ)) ⊆ gen C '' Set.univ := by
    rw [Set.image_univ]
    exact hts
  obtain ⟨A, -, hA⟩ := Finset.subset_set_image_iff.1 hts'
  exact ⟨A, by rw [hA]; exact ht⟩

theorem mem_stageGen (i : D.ι) (y : (D.stage i).P) : gen C ⟨i, y⟩ ∈ stageGen C i := by
  unfold stageGen
  exact Finset.mem_image_of_mem (fun y : (D.stage i).P => gen C ⟨i, y⟩) (Finset.mem_univ y)

/-- A stage-preserving datum carries the chart coordinates of a stage into themselves. -/
theorem mapsTo_stageGen {T : OpDatum D} (hT : AffineRespect T) (hsp : StagePreserving T)
    (i : D.ι) : ∀ w ∈ stageGen C i, induced C T hT w ∈ stageGen C i := by
  intro w hw
  unfold stageGen at hw
  obtain ⟨y, -, rfl⟩ := Finset.mem_image.1 hw
  obtain ⟨y', hy'⟩ := hsp i y
  show induced C T hT (gen C ⟨i, y⟩) ∈ stageGen C i
  have h1 : induced C T hT (gen C ⟨i, y⟩) = gen C ⟨i, y'⟩ := by
    rw [induced_gen, hy']; try rfl
  rw [h1]
  exact mem_stageGen C i y'

/-- **Finite order from stage preservation.** A reversible datum that respects affine relations
and carries each stage's preparations to preparation vectors of the same stage induces an
automorphism of finite order on the chart body. -/
theorem finiteOrderOn_of_stagePreserving {S T : OpDatum D} (hS : AffineRespect S)
    (hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT)
    (hsp : StagePreserving T) :
    FiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS) := by
  classical
  have hinj : Function.Injective (induced C T hT) :=
    Function.LeftInverse.injective (g := induced C S hS)
      (fun w => congrFun (congrArg DFunLike.coe (comp_eq_id C hS hT hST)) w)
  obtain ⟨A, hA⟩ := exists_gen_finset C
  have hper : ∀ w ∈ A.image (gen C), ∃ p : ℕ, 0 < p ∧ (⇑(induced C T hT))^[p] w = w := by
    intro w hw
    obtain ⟨x, -, rfl⟩ := Finset.mem_image.1 hw
    obtain ⟨i, y⟩ := x
    exact exists_return hinj (mapsTo_stageGen C hT hsp i) (mem_stageGen C i y)
  obtain ⟨N, hN, hNA⟩ := exists_common_period (A.image (gen C)) hper
  have hext : affPow (induced C T hT) N = AffineMap.id ℝ _ := by
    apply AffineMap.ext_on hA
    intro w hw
    rw [AffineMap.id_apply, coe_affPow]
    exact hNA w (Finset.mem_coe.1 hw)
  refine ⟨N, hN, fun w _ => ?_⟩
  rw [coe_inducedEquiv, ← coe_affPow, hext, AffineMap.id_apply]

theorem not_infiniteOrderOn_of_stagePreserving {S T : OpDatum D} (hS : AffineRespect S)
    (hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT)
    (hsp : StagePreserving T) :
    ¬ InfiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS) :=
  not_infiniteOrderOn_of_finiteOrderOn (finiteOrderOn_of_stagePreserving C hS hT hST hTS hsp)

/-- A reversible datum of infinite order on the chart body crosses stages. -/
theorem not_stagePreserving_of_infiniteOrderOn {S T : OpDatum D} (hS : AffineRespect S)
    (hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT)
    (h : InfiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS)) :
    ¬ StagePreserving T :=
  fun hsp => not_infiniteOrderOn_of_stagePreserving C hS hT hST hTS hsp h

/-! ### §E — controls -/

/-- The Householder reflections of the ball. -/
def householder3 : Set ((Fin 3 → ℝ) ≃ᵃ[ℝ] (Fin 3 → ℝ)) := {g | ∃ d k hk, g = hh3 d k hk}

theorem hh3_hh3 (d : Fin 3 → ℝ) (k : ℝ) (hk : (d 0 ^ 2 + d 1 ^ 2 + d 2 ^ 2) * k = 1)
    (v : Fin 3 → ℝ) : hh3 d k hk (hh3 d k hk v) = v := by
  rw [hh3_apply, hh3_apply]
  exact hhFun_hhFun d k hk v

/-- Each Householder reflection has finite order on the ball. -/
theorem finiteOrderOn_hh3 (d : Fin 3 → ℝ) (k : ℝ) (hk : (d 0 ^ 2 + d 1 ^ 2 + d 2 ^ 2) * k = 1) :
    FiniteOrderOn ball3 (hh3 d k hk) :=
  ⟨2, by norm_num, fun v _ => hh3_hh3 d k hk v⟩

/-- **Control: the Householder set has no member of infinite order.** -/
theorem not_ordInf_householder3 : ¬ OrdInf ball3 householder3 := by
  rintro ⟨g, ⟨d, k, hk, rfl⟩, h⟩
  exact not_infiniteOrderOn_of_finiteOrderOn (finiteOrderOn_hh3 d k hk) h

theorem rot3_mem_fullAut3 (t : ℝ) : rot3 t ∈ fullAut3 := fun x hx =>
  preservesBody_flow (rot3 t) ⟨t, rfl⟩ x hx

theorem rot3_one_iterate (m : ℕ) (v : Fin 3 → ℝ) : (⇑(rot3 1))^[m] v = rotFun (m : ℝ) v := by
  induction m with
  | zero => simp [rotFun_zero]
  | succ k ih =>
    rw [Function.iterate_succ_apply', ih, rot3_apply, rotFun_add]
    congr 1
    push_cast
    ring

/-- **Control: the rotation by one radian has infinite order on the ball.** `cos m ≠ 1` for every
integer `m ≥ 1`, since `π` is irrational. -/
theorem infiniteOrderOn_rot3_one : InfiniteOrderOn ball3 (rot3 1) := by
  intro m hm
  refine ⟨![1, 0, 0], by show (1 : ℝ) ^ 2 + 0 ^ 2 + 0 ^ 2 ≤ 1; norm_num, fun h => ?_⟩
  rw [rot3_one_iterate] at h
  have h0 := congrFun h 0
  obtain ⟨a0, -, -⟩ := rotFun_apply (m : ℝ) ![1, 0, 0]
  rw [a0] at h0
  simp only [Matrix.cons_val_zero, Matrix.cons_val_one, mul_one, mul_zero, sub_zero] at h0
  obtain ⟨n, hn⟩ := (Real.cos_eq_one_iff _).mp h0
  have hmpos : (0 : ℝ) < m := by exact_mod_cast hm
  have hn0 : (n : ℝ) ≠ 0 := by
    intro hz
    rw [hz, zero_mul] at hn
    linarith
  apply irrational_pi.ne_rat ((m : ℚ) / (2 * n))
  push_cast
  field_simp
  linear_combination hn

/-- **Control: the automorphisms of the ball have a member of infinite order.** -/
theorem ordInf_fullAut3 : OrdInf ball3 fullAut3 :=
  ⟨rot3 1, rot3_mem_fullAut3 1, infiniteOrderOn_rot3_one⟩

/-- **Control: the rotation family has a member of infinite order.** -/
theorem ordInf_range_rot3 : OrdInf ball3 (Set.range rot3) :=
  ⟨rot3 1, ⟨1, rfl⟩, infiniteOrderOn_rot3_one⟩

/-- **Countercontrol for the closure hypothesis.** A finite set that is not composition-closed
may have a member of infinite order. -/
theorem ordInf_singleton_rot3 : OrdInf ball3 {rot3 1} :=
  ⟨rot3 1, Set.mem_singleton _, infiniteOrderOn_rot3_one⟩

/-! ### §F — the verdict -/

/-- **Round ORD-1.** A reversible stage-preserving datum induces an automorphism of finite order
on the chart body; a reversible datum of infinite order has every positive power nontrivial; the
rotation by one radian has infinite order on the ball; the Householder set has no member of
infinite order; the singleton of the rotation has one; a finite composition-closed set has none. -/
theorem ord1_core :
    (∀ (D : DirectedStages) (C : CompletionChart D) (S T : OpDatum D) (hS : AffineRespect S)
      (hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT),
        StagePreserving T → FiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS)) ∧
    (∀ (D : DirectedStages) (C : CompletionChart D) (S T : OpDatum D) (hS : AffineRespect S)
      (hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT),
        InfiniteOrderOn (chartBody C) (inducedEquiv C hS hT hST hTS) →
          ∀ m : ℕ, 1 ≤ m → ∃ x, (iterAfter C T hT m).τ x ≠ prepVec D x) ∧
    InfiniteOrderOn ball3 (rot3 1) ∧ ¬ OrdInf ball3 householder3 ∧ OrdInf ball3 {rot3 1} ∧
    (∀ (V : Type) [AddCommGroup V] [Module ℝ V] (Ω : Set V) (G : Set (V ≃ᵃ[ℝ] V)),
      G.Finite → MulClosed G → ¬ OrdInf Ω G) :=
  ⟨fun _ C _ _ hS hT hST hTS hsp => finiteOrderOn_of_stagePreserving C hS hT hST hTS hsp,
    fun _ C _ _ hS hT hST hTS h m hm => (exists_moved_of_infiniteOrderOn C hS hT hST hTS h m hm).2,
    infiniteOrderOn_rot3_one, not_ordInf_householder3, ordInf_singleton_rot3,
    fun _ _ _ _ _ hG hcl => not_ordInf_of_finite_of_mulClosed hG hcl⟩

end CompositionOrder
end OIBridge

#print axioms OIBridge.CompositionOrder.coe_affPow
#print axioms OIBridge.CompositionOrder.finiteOrderOn_of_not_infiniteOrderOn
#print axioms OIBridge.CompositionOrder.not_infiniteOrderOn_of_finiteOrderOn
#print axioms OIBridge.CompositionOrder.not_infiniteOrderOn_iff
#print axioms OIBridge.CompositionOrder.finiteOrderOn_refl
#print axioms OIBridge.CompositionOrder.finiteOrderOn_of_iterate_eq
#print axioms OIBridge.CompositionOrder.not_ordInf_of_finite_of_mulClosed
#print axioms OIBridge.CompositionOrder.exists_return
#print axioms OIBridge.CompositionOrder.exists_common_period
#print axioms OIBridge.CompositionOrder.exists_finset_affineSpan_eq_top
#print axioms OIBridge.CompositionOrder.affineRespect_idDatum
#print axioms OIBridge.CompositionOrder.induced_idDatum
#print axioms OIBridge.CompositionOrder.affineRespect_iterAfter
#print axioms OIBridge.CompositionOrder.induced_iterAfter
#print axioms OIBridge.CompositionOrder.coe_induced_iterAfter
#print axioms OIBridge.CompositionOrder.coe_inducedEquiv
#print axioms OIBridge.CompositionOrder.iterate_eq_id_of_fix
#print axioms OIBridge.CompositionOrder.exists_moved_of_infiniteOrderOn
#print axioms OIBridge.CompositionOrder.nonempty_prep
#print axioms OIBridge.CompositionOrder.exists_gen_finset
#print axioms OIBridge.CompositionOrder.mem_stageGen
#print axioms OIBridge.CompositionOrder.mapsTo_stageGen
#print axioms OIBridge.CompositionOrder.finiteOrderOn_of_stagePreserving
#print axioms OIBridge.CompositionOrder.not_infiniteOrderOn_of_stagePreserving
#print axioms OIBridge.CompositionOrder.not_stagePreserving_of_infiniteOrderOn
#print axioms OIBridge.CompositionOrder.hh3_hh3
#print axioms OIBridge.CompositionOrder.finiteOrderOn_hh3
#print axioms OIBridge.CompositionOrder.not_ordInf_householder3
#print axioms OIBridge.CompositionOrder.rot3_mem_fullAut3
#print axioms OIBridge.CompositionOrder.rot3_one_iterate
#print axioms OIBridge.CompositionOrder.infiniteOrderOn_rot3_one
#print axioms OIBridge.CompositionOrder.ordInf_fullAut3
#print axioms OIBridge.CompositionOrder.ordInf_range_rot3
#print axioms OIBridge.CompositionOrder.ordInf_singleton_rot3
#print axioms OIBridge.CompositionOrder.ord1_core
