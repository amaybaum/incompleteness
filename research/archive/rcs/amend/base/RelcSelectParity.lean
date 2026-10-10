/-
  OIBridge/RelcSelectParity.lean — the parity count of the homogenized NOT from the control
  relation alone.

  Setting. `toOp` identifies `W d` with the operators of the control space `HVec d`. Through it the
  control action `actC N` is left composition with `H = homMap N` (`toOp_actC`) and, for a NOT of
  the ball, the target action `actT N` is right composition with `H` (`toOp_actT`). On operators,
  `relCLeft N` is `F ↦ H ∘ F` and `relCConj N` is `F ↦ H ∘ F ∘ H`.

  (A) Intertwining. With `IsNot (eball d) z N`, the control relation
  `∀ ω, actC N (G (actC N ω)) = actT N (G ω)` gives
  `opGate G (H ∘ F) = H ∘ opGate G F ∘ H` (`opGate_homMap_comp_relC`), and `opGate G` is injective
  (`opGate_injective_relC`). An injective map intertwining two maps sends each of the `±1`
  eigenspaces of the first injectively into the corresponding eigenspace of the second
  (`finrank_ker_sub_le_relC`, `finrank_ker_add_le_relC`).

  (B) The counts. With `P` and `Q` the dimensions of the `+1` and `−1` eigenspaces of `H`:
  the `+1` and `−1` eigenspaces of `relCLeft N` have dimensions `(d+1)·P` and `(d+1)·Q`
  (`finrank_ker_relCLeft_sub`, `finrank_ker_relCLeft_add`); restriction to the two eigenspaces of
  `H` embeds the `+1` eigenspace of `relCConj N` into `End(E₊) × End(E₋)` and its `−1` eigenspace
  into `Hom(E₊, E₋) × Hom(E₋, E₊)`, so their dimensions are at most `P² + Q²` and `2PQ`
  (`finrank_ker_relCConj_sub_le`, `finrank_ker_relCConj_add_le`).

  (C) Parity. `(P+Q)·P ≤ P² + Q²`, `(P+Q)·Q ≤ 2PQ` and `Q ≥ 1` give `P = Q`
  (`balance_of_bounds_relC`), so the two eigenspaces of the homogenized NOT have equal dimension
  (`finrank_plus_eq_finrank_minus_relC`) and `d` is odd (`not_even_of_relC`).

  The target relation, the frame and positivity are not hypotheses of any statement here; the gate
  enters through the control relation and its invertibility only.
-/
import OIBridge.OddChar

namespace OIBridge
namespace RelcSelect

open KInfFoundations TransitiveBody NativeGateBall CompositeDimension EffectSpace ParityNot

variable {d : ℕ}

/-! ### §A — left and two-sided composition with the homogenized NOT -/

/-- Left composition with the homogenized NOT, on all operators of the control space. -/
noncomputable def relCLeft (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :
    (HVec d →ₗ[ℝ] HVec d) →ₗ[ℝ] (HVec d →ₗ[ℝ] HVec d) where
  toFun F := homMap N ∘ₗ F
  map_add' F₁ F₂ := LinearMap.ext fun v => by
    simp only [LinearMap.comp_apply, LinearMap.add_apply, map_add]
  map_smul' c F := LinearMap.ext fun v => by
    simp only [LinearMap.comp_apply, LinearMap.smul_apply, map_smul, RingHom.id_apply]

/-- Two-sided composition with the homogenized NOT: `F ↦ H ∘ F ∘ H`. -/
noncomputable def relCConj (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :
    (HVec d →ₗ[ℝ] HVec d) →ₗ[ℝ] (HVec d →ₗ[ℝ] HVec d) where
  toFun F := homMap N ∘ₗ F ∘ₗ homMap N
  map_add' F₁ F₂ := LinearMap.ext fun v => by
    simp only [LinearMap.comp_apply, LinearMap.add_apply, map_add]
  map_smul' c F := LinearMap.ext fun v => by
    simp only [LinearMap.comp_apply, LinearMap.smul_apply, map_smul, RingHom.id_apply]

theorem relCLeft_apply (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (F : HVec d →ₗ[ℝ] HVec d)
    (v : HVec d) : relCLeft N F v = homMap N (F v) := rfl

theorem relCConj_apply (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (F : HVec d →ₗ[ℝ] HVec d)
    (v : HVec d) : relCConj N F v = homMap N (F (homMap N v)) := rfl

theorem relCLeft_eq (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (F : HVec d →ₗ[ℝ] HVec d) :
    relCLeft N F = homMap N ∘ₗ F := rfl

theorem relCConj_eq (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (F : HVec d →ₗ[ℝ] HVec d) :
    relCConj N F = homMap N ∘ₗ F ∘ₗ homMap N := rfl

/-! ### §B — the gate intertwines the two compositions -/

/-- The control relation in operator form, from the control relation alone. -/
theorem opGate_homMap_comp_relC {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N)
    (hC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)) (F : HVec d →ₗ[ℝ] HVec d) :
    opGate G (homMap N ∘ₗ F) = homMap N ∘ₗ opGate G F ∘ₗ homMap N := by
  obtain ⟨ω, rfl⟩ : ∃ ω, F = toOp ω := ⟨fromOp F, (toOp_fromOp F).symm⟩
  have h : G (actC N ω) = actC N (actT N (G ω)) := by
    rw [← hC ω, actC_actC hN.invol]
  rw [← toOp_actC, opGate_toOp, opGate_toOp, h, toOp_actC, toOp_actT hN]

/-- The gate in operator form is injective. -/
theorem opGate_injective_relC (G : W d ≃ₗ[ℝ] W d) : Function.Injective (opGate G) := by
  intro F₁ F₂ h
  obtain ⟨ω₁, rfl⟩ : ∃ ω, F₁ = toOp ω := ⟨fromOp F₁, (toOp_fromOp F₁).symm⟩
  obtain ⟨ω₂, rfl⟩ : ∃ ω, F₂ = toOp ω := ⟨fromOp F₂, (toOp_fromOp F₂).symm⟩
  rw [opGate_toOp, opGate_toOp] at h
  exact congrArg toOp (G.injective (toOp_injective h))

/-- An injective map intertwining `L` with `T` embeds the `+1` eigenspace of `L` into that of `T`. -/
theorem finrank_ker_sub_le_relC {V : Type*} [AddCommGroup V] [Module ℝ V] [FiniteDimensional ℝ V]
    (A L T : V →ₗ[ℝ] V) (hA : Function.Injective A) (hAL : ∀ v, A (L v) = T (A v)) :
    Module.finrank ℝ (LinearMap.ker (L - LinearMap.id))
      ≤ Module.finrank ℝ (LinearMap.ker (T - LinearMap.id)) := by
  have h1 : ∀ v ∈ LinearMap.ker (L - LinearMap.id), A v ∈ LinearMap.ker (T - LinearMap.id) := by
    intro v hv
    simp only [LinearMap.mem_ker, LinearMap.sub_apply, LinearMap.id_apply, sub_eq_zero] at hv ⊢
    rw [← hAL, hv]
  have inj1 : Function.Injective (A.restrict h1) := by
    intro x y hxy
    apply Subtype.ext
    apply hA
    have := congrArg Subtype.val hxy
    simpa [LinearMap.restrict_apply] using this
  exact LinearMap.finrank_le_finrank_of_injective inj1

/-- An injective map intertwining `L` with `T` embeds the `−1` eigenspace of `L` into that of `T`. -/
theorem finrank_ker_add_le_relC {V : Type*} [AddCommGroup V] [Module ℝ V] [FiniteDimensional ℝ V]
    (A L T : V →ₗ[ℝ] V) (hA : Function.Injective A) (hAL : ∀ v, A (L v) = T (A v)) :
    Module.finrank ℝ (LinearMap.ker (L + LinearMap.id))
      ≤ Module.finrank ℝ (LinearMap.ker (T + LinearMap.id)) := by
  have h1 : ∀ v ∈ LinearMap.ker (L + LinearMap.id), A v ∈ LinearMap.ker (T + LinearMap.id) := by
    intro v hv
    simp only [LinearMap.mem_ker, LinearMap.add_apply, LinearMap.id_apply] at hv ⊢
    rw [← hAL, ← map_add A (L v) v, hv, map_zero]
  have inj1 : Function.Injective (A.restrict h1) := by
    intro x y hxy
    apply Subtype.ext
    apply hA
    have := congrArg Subtype.val hxy
    simpa [LinearMap.restrict_apply] using this
  exact LinearMap.finrank_le_finrank_of_injective inj1

/-! ### §C — the eigenspaces of left composition -/

/-- The operators fixed by left composition with `H` are those with values in `E₊`. -/
theorem finrank_ker_relCLeft_sub (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :
    Module.finrank ℝ (LinearMap.ker (relCLeft N - LinearMap.id))
      = (d + 1) * Module.finrank ℝ (plusSpace N) := by
  have h := finrank_ker_eq_of_pointwise (plusSpace N) (relCLeft N - LinearMap.id) fun f => by
    constructor
    · intro hf u
      rw [mem_plusSpace]
      have := LinearMap.congr_fun hf u
      simpa only [LinearMap.sub_apply, LinearMap.id_apply, relCLeft_apply, LinearMap.zero_apply,
        sub_eq_zero] using this
    · intro hf
      apply LinearMap.ext; intro u
      simp only [LinearMap.sub_apply, LinearMap.id_apply, relCLeft_apply, LinearMap.zero_apply,
        sub_eq_zero]
      exact mem_plusSpace.mp (hf u)
  rw [Module.finrank_fin_fun] at h
  exact h

/-- The operators negated by left composition with `H` are those with values in `E₋`. -/
theorem finrank_ker_relCLeft_add (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :
    Module.finrank ℝ (LinearMap.ker (relCLeft N + LinearMap.id))
      = (d + 1) * Module.finrank ℝ (minusSpace N) := by
  have h := finrank_ker_eq_of_pointwise (minusSpace N) (relCLeft N + LinearMap.id) fun f => by
    constructor
    · intro hf u
      rw [mem_minusSpace]
      have := LinearMap.congr_fun hf u
      simpa only [LinearMap.add_apply, LinearMap.id_apply, relCLeft_apply, LinearMap.zero_apply,
        add_eq_zero_iff_eq_neg] using this
    · intro hf
      apply LinearMap.ext; intro u
      simp only [LinearMap.add_apply, LinearMap.id_apply, relCLeft_apply, LinearMap.zero_apply,
        add_eq_zero_iff_eq_neg]
      exact mem_minusSpace.mp (hf u)
  rw [Module.finrank_fin_fun] at h
  exact h

/-! ### §D — the eigenspaces of two-sided composition -/

/-- An operator vanishing on both eigenspaces of the homogenized NOT is zero. -/
theorem eq_zero_of_plus_minus_relC {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x)
    (F : HVec d →ₗ[ℝ] HVec d) (hp : ∀ u ∈ plusSpace N, F u = 0)
    (hm : ∀ u ∈ minusSpace N, F u = 0) : F = 0 := by
  apply LinearMap.ext; intro v
  have hdecomp : v = (1 / 2 : ℝ) • (v + homMap N v) + (1 / 2 : ℝ) • (v - homMap N v) := by
    module
  have hp' : (1 / 2 : ℝ) • (v + homMap N v) ∈ plusSpace N := by
    rw [mem_plusSpace, map_smul, map_add, homMap_homMap hN, add_comm (homMap N v) v]
  have hm' : (1 / 2 : ℝ) • (v - homMap N v) ∈ minusSpace N := (projMinus hN v).2
  rw [LinearMap.zero_apply, hdecomp, map_add, hp _ hp', hm _ hm', add_zero]

/-- An operator fixed by two-sided composition commutes with the homogenized NOT. -/
theorem homMap_comm_relC {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x)
    {F : HVec d →ₗ[ℝ] HVec d} (hF : F ∈ LinearMap.ker (relCConj N - LinearMap.id))
    (v : HVec d) : homMap N (F v) = F (homMap N v) := by
  have h := LinearMap.congr_fun (LinearMap.mem_ker.mp hF) (homMap N v)
  simp only [LinearMap.sub_apply, LinearMap.id_apply, relCConj_apply, homMap_homMap hN,
    LinearMap.zero_apply, sub_eq_zero] at h
  exact h

/-- An operator negated by two-sided composition anticommutes with the homogenized NOT. -/
theorem homMap_anticomm_relC {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x)
    {F : HVec d →ₗ[ℝ] HVec d} (hF : F ∈ LinearMap.ker (relCConj N + LinearMap.id))
    (v : HVec d) : homMap N (F v) = -F (homMap N v) := by
  have h := LinearMap.congr_fun (LinearMap.mem_ker.mp hF) (homMap N v)
  simp only [LinearMap.add_apply, LinearMap.id_apply, relCConj_apply, homMap_homMap hN,
    LinearMap.zero_apply, add_eq_zero_iff_eq_neg] at h
  exact h

/-- A commuting operator maps `E₊` into `E₊`. -/
theorem mem_plusSpace_of_comm_relC {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x)
    {F : HVec d →ₗ[ℝ] HVec d} (hF : F ∈ LinearMap.ker (relCConj N - LinearMap.id))
    (u : plusSpace N) : F (u : HVec d) ∈ plusSpace N := by
  rw [mem_plusSpace, homMap_comm_relC hN hF, mem_plusSpace.mp u.2]

/-- A commuting operator maps `E₋` into `E₋`. -/
theorem mem_minusSpace_of_comm_relC {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x)
    {F : HVec d →ₗ[ℝ] HVec d} (hF : F ∈ LinearMap.ker (relCConj N - LinearMap.id))
    (u : minusSpace N) : F (u : HVec d) ∈ minusSpace N := by
  rw [mem_minusSpace, homMap_comm_relC hN hF, mem_minusSpace.mp u.2, map_neg]

/-- An anticommuting operator maps `E₊` into `E₋`. -/
theorem mem_minusSpace_of_anticomm_relC {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hN : ∀ x, N (N x) = x) {F : HVec d →ₗ[ℝ] HVec d}
    (hF : F ∈ LinearMap.ker (relCConj N + LinearMap.id)) (u : plusSpace N) :
    F (u : HVec d) ∈ minusSpace N := by
  rw [mem_minusSpace, homMap_anticomm_relC hN hF, mem_plusSpace.mp u.2]

/-- An anticommuting operator maps `E₋` into `E₊`. -/
theorem mem_plusSpace_of_anticomm_relC {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hN : ∀ x, N (N x) = x) {F : HVec d →ₗ[ℝ] HVec d}
    (hF : F ∈ LinearMap.ker (relCConj N + LinearMap.id)) (u : minusSpace N) :
    F (u : HVec d) ∈ plusSpace N := by
  rw [mem_plusSpace, homMap_anticomm_relC hN hF, mem_minusSpace.mp u.2, map_neg, neg_neg]

/-- Restriction of a commuting operator to the two eigenspaces of the homogenized NOT. -/
noncomputable def relCSplitEven {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) :
    LinearMap.ker (relCConj N - LinearMap.id) →ₗ[ℝ]
      (plusSpace N →ₗ[ℝ] plusSpace N) × (minusSpace N →ₗ[ℝ] minusSpace N) where
  toFun F :=
    (LinearMap.codRestrict (plusSpace N) (F.1 ∘ₗ (plusSpace N).subtype)
        (fun u => mem_plusSpace_of_comm_relC hN F.2 u),
      LinearMap.codRestrict (minusSpace N) (F.1 ∘ₗ (minusSpace N).subtype)
        (fun u => mem_minusSpace_of_comm_relC hN F.2 u))
  map_add' _ _ := Prod.ext (LinearMap.ext fun _ => rfl) (LinearMap.ext fun _ => rfl)
  map_smul' _ _ := Prod.ext (LinearMap.ext fun _ => rfl) (LinearMap.ext fun _ => rfl)

/-- Restriction of an anticommuting operator to the two eigenspaces of the homogenized NOT. -/
noncomputable def relCSplitOdd {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) :
    LinearMap.ker (relCConj N + LinearMap.id) →ₗ[ℝ]
      (plusSpace N →ₗ[ℝ] minusSpace N) × (minusSpace N →ₗ[ℝ] plusSpace N) where
  toFun F :=
    (LinearMap.codRestrict (minusSpace N) (F.1 ∘ₗ (plusSpace N).subtype)
        (fun u => mem_minusSpace_of_anticomm_relC hN F.2 u),
      LinearMap.codRestrict (plusSpace N) (F.1 ∘ₗ (minusSpace N).subtype)
        (fun u => mem_plusSpace_of_anticomm_relC hN F.2 u))
  map_add' _ _ := Prod.ext (LinearMap.ext fun _ => rfl) (LinearMap.ext fun _ => rfl)
  map_smul' _ _ := Prod.ext (LinearMap.ext fun _ => rfl) (LinearMap.ext fun _ => rfl)

theorem relCSplitEven_injective {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) :
    Function.Injective (relCSplitEven hN) := by
  intro F₁ F₂ h
  have h1 : ∀ u ∈ plusSpace N, F₁.1 u = F₂.1 u := fun u hu => by
    have := congrArg Subtype.val (LinearMap.congr_fun (congrArg Prod.fst h) ⟨u, hu⟩)
    exact this
  have h2 : ∀ u ∈ minusSpace N, F₁.1 u = F₂.1 u := fun u hu => by
    have := congrArg Subtype.val (LinearMap.congr_fun (congrArg Prod.snd h) ⟨u, hu⟩)
    exact this
  apply Subtype.ext
  apply sub_eq_zero.mp
  apply eq_zero_of_plus_minus_relC hN
  · intro u hu
    rw [LinearMap.sub_apply, h1 u hu, sub_self]
  · intro u hu
    rw [LinearMap.sub_apply, h2 u hu, sub_self]

theorem relCSplitOdd_injective {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) :
    Function.Injective (relCSplitOdd hN) := by
  intro F₁ F₂ h
  have h1 : ∀ u ∈ plusSpace N, F₁.1 u = F₂.1 u := fun u hu => by
    have := congrArg Subtype.val (LinearMap.congr_fun (congrArg Prod.fst h) ⟨u, hu⟩)
    exact this
  have h2 : ∀ u ∈ minusSpace N, F₁.1 u = F₂.1 u := fun u hu => by
    have := congrArg Subtype.val (LinearMap.congr_fun (congrArg Prod.snd h) ⟨u, hu⟩)
    exact this
  apply Subtype.ext
  apply sub_eq_zero.mp
  apply eq_zero_of_plus_minus_relC hN
  · intro u hu
    rw [LinearMap.sub_apply, h1 u hu, sub_self]
  · intro u hu
    rw [LinearMap.sub_apply, h2 u hu, sub_self]

/-- The operators commuting with `H` have dimension at most `P² + Q²`. -/
theorem finrank_ker_relCConj_sub_le {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) :
    Module.finrank ℝ (LinearMap.ker (relCConj N - LinearMap.id))
      ≤ Module.finrank ℝ (plusSpace N) * Module.finrank ℝ (plusSpace N)
        + Module.finrank ℝ (minusSpace N) * Module.finrank ℝ (minusSpace N) := by
  have h := LinearMap.finrank_le_finrank_of_injective (relCSplitEven_injective hN)
  -- MATHLIB-NAME-UNVERIFIED (by compile): `Module.finrank_prod` is not used elsewhere in OIBridge;
  -- it is stated in Mathlib v4.33.0 `LinearAlgebra/Dimension/Constructions.lean` (simp lemma).
  have e : Module.finrank ℝ
      ((plusSpace N →ₗ[ℝ] plusSpace N) × (minusSpace N →ₗ[ℝ] minusSpace N))
        = Module.finrank ℝ (plusSpace N) * Module.finrank ℝ (plusSpace N)
          + Module.finrank ℝ (minusSpace N) * Module.finrank ℝ (minusSpace N) := by
    rw [Module.finrank_prod, Module.finrank_linearMap ℝ ℝ (plusSpace N) (plusSpace N),
      Module.finrank_linearMap ℝ ℝ (minusSpace N) (minusSpace N)]
  exact h.trans e.le

/-- The operators anticommuting with `H` have dimension at most `2PQ`. -/
theorem finrank_ker_relCConj_add_le {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} (hN : ∀ x, N (N x) = x) :
    Module.finrank ℝ (LinearMap.ker (relCConj N + LinearMap.id))
      ≤ Module.finrank ℝ (plusSpace N) * Module.finrank ℝ (minusSpace N)
        + Module.finrank ℝ (minusSpace N) * Module.finrank ℝ (plusSpace N) := by
  have h := LinearMap.finrank_le_finrank_of_injective (relCSplitOdd_injective hN)
  have e : Module.finrank ℝ
      ((plusSpace N →ₗ[ℝ] minusSpace N) × (minusSpace N →ₗ[ℝ] plusSpace N))
        = Module.finrank ℝ (plusSpace N) * Module.finrank ℝ (minusSpace N)
          + Module.finrank ℝ (minusSpace N) * Module.finrank ℝ (plusSpace N) := by
    rw [Module.finrank_prod, Module.finrank_linearMap ℝ ℝ (plusSpace N) (minusSpace N),
      Module.finrank_linearMap ℝ ℝ (minusSpace N) (plusSpace N)]
  exact h.trans e.le

/-! ### §E — parity from the control relation -/

/-- The count: `(P+Q)·P ≤ P² + Q²`, `(P+Q)·Q ≤ 2PQ` and `Q ≥ 1` force `P = Q`. -/
theorem balance_of_bounds_relC {n P Q : ℕ} (hn : P + Q = n) (hQ : 1 ≤ Q)
    (h1 : n * P ≤ P * P + Q * Q) (h2 : n * Q ≤ P * Q + Q * P) : P = Q := by
  subst hn
  have e1 : (P + Q) * P = P * P + Q * P := by ring
  have e2 : (P + Q) * Q = P * Q + Q * Q := by ring
  have e3 : P * Q = Q * P := by ring
  rw [e1] at h1
  rw [e2, e3] at h2
  have hA : Q * P ≤ Q * Q := by
    exact Nat.le_of_add_le_add_left h1
  have hB : Q * Q ≤ Q * P := by
    exact Nat.le_of_add_le_add_left h2
  exact Nat.eq_of_mul_eq_mul_left hQ (le_antisymm hA hB)

/-- **Parity from the control relation.** The `+1` and `−1` eigenspaces of the homogenized NOT
have the same dimension; the target relation, the frame and positivity are not read. -/
theorem finrank_plus_eq_finrank_minus_relC {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N)
    (hC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)) :
    Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N) := by
  have hinj := opGate_injective_relC G
  have hAL : ∀ F, opGate G (relCLeft N F) = relCConj N (opGate G F) := fun F => by
    rw [relCLeft_eq, relCConj_eq]
    exact opGate_homMap_comp_relC hN hC F
  have h1 : (d + 1) * Module.finrank ℝ (plusSpace N)
      ≤ Module.finrank ℝ (plusSpace N) * Module.finrank ℝ (plusSpace N)
        + Module.finrank ℝ (minusSpace N) * Module.finrank ℝ (minusSpace N) := by
    have hle := finrank_ker_sub_le_relC (opGate G) (relCLeft N) (relCConj N) hinj hAL
    rw [finrank_ker_relCLeft_sub] at hle
    exact hle.trans (finrank_ker_relCConj_sub_le hN.invol)
  have h2 : (d + 1) * Module.finrank ℝ (minusSpace N)
      ≤ Module.finrank ℝ (plusSpace N) * Module.finrank ℝ (minusSpace N)
        + Module.finrank ℝ (minusSpace N) * Module.finrank ℝ (plusSpace N) := by
    have hle := finrank_ker_add_le_relC (opGate G) (relCLeft N) (relCConj N) hinj hAL
    rw [finrank_ker_relCLeft_add] at hle
    exact hle.trans (finrank_ker_relCConj_add_le hN.invol)
  exact balance_of_bounds_relC (finrank_plus_add_finrank_minus hN.invol)
    (one_le_finrank_minusSpace hN) h1 h2

/-- No even dimension carries a NOT of the ball and an invertible gate with the control
relation. -/
theorem not_even_of_relC {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N)
    (hC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)) : ¬ Even d :=
  not_even_of_balanced (finrank_plus_add_finrank_minus hN.invol)
    (finrank_plus_eq_finrank_minus_relC hN hC)

end RelcSelect
end OIBridge

#print axioms OIBridge.RelcSelect.finrank_plus_eq_finrank_minus_relC
#print axioms OIBridge.RelcSelect.not_even_of_relC
