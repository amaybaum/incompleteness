/-- Operators with values in a subspace: the kernel of a pointwise test has the dimension of the
operator space into the subspace. -/
theorem finrank_ker_eq_of_pointwise {M E : Type*} [AddCommGroup M] [Module ℝ M]
    [FiniteDimensional ℝ M] [AddCommGroup E] [Module ℝ E] [FiniteDimensional ℝ E]
    (S : Submodule ℝ E) (T : (M →ₗ[ℝ] E) →ₗ[ℝ] (M →ₗ[ℝ] E))
    (hT : ∀ f, T f = 0 ↔ ∀ u, f u ∈ S) :
    Module.finrank ℝ (LinearMap.ker T) = Module.finrank ℝ M * Module.finrank ℝ S := by
  let A : LinearMap.ker T →ₗ[ℝ] (M →ₗ[ℝ] S) :=
    { toFun := fun f => LinearMap.codRestrict S f.1 ((hT f.1).1 (LinearMap.mem_ker.mp f.2))
      map_add' := fun f g => LinearMap.ext fun u => rfl
      map_smul' := fun c f => LinearMap.ext fun u => rfl }
  let B : (M →ₗ[ℝ] S) →ₗ[ℝ] LinearMap.ker T :=
    { toFun := fun g => ⟨S.subtype ∘ₗ g, LinearMap.mem_ker.mpr ((hT _).2 fun u => (g u).2)⟩
      map_add' := fun g h => Subtype.ext (LinearMap.ext fun u => rfl)
      map_smul' := fun c g => Subtype.ext (LinearMap.ext fun u => rfl) }
  have hA : Function.Injective A := by
    intro f g hfg
    apply Subtype.ext; apply LinearMap.ext; intro u
    exact congrArg Subtype.val (LinearMap.congr_fun hfg u)
  have hB : Function.Injective B := by
    intro g h hgh
    apply LinearMap.ext; intro u; apply Subtype.ext
    exact LinearMap.congr_fun (congrArg Subtype.val hgh) u
  calc Module.finrank ℝ (LinearMap.ker T) = Module.finrank ℝ (M →ₗ[ℝ] S) :=
        le_antisymm (LinearMap.finrank_le_finrank_of_injective hA)
          (LinearMap.finrank_le_finrank_of_injective hB)
    _ = Module.finrank ℝ M * Module.finrank ℝ S := Module.finrank_linearMap

theorem finrank_ker_Pop_sub (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :
    Module.finrank ℝ (LinearMap.ker (Pop N - LinearMap.id))
      = Module.finrank ℝ (minusSpace N) * Module.finrank ℝ (plusSpace N) :=
  finrank_ker_eq_of_pointwise (plusSpace N) (Pop N - LinearMap.id) fun f => by
    constructor
    · intro h u
      rw [mem_plusSpace]
      have := LinearMap.congr_fun h u
      simpa only [LinearMap.sub_apply, LinearMap.id_apply, Pop_apply, LinearMap.zero_apply,
        sub_eq_zero] using this
    · intro h
      apply LinearMap.ext; intro u
      simp only [LinearMap.sub_apply, LinearMap.id_apply, Pop_apply, LinearMap.zero_apply,
        sub_eq_zero]
      exact mem_plusSpace.mp (h u)

theorem finrank_ker_Pop_add (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) :
    Module.finrank ℝ (LinearMap.ker (Pop N + LinearMap.id))
      = Module.finrank ℝ (minusSpace N) * Module.finrank ℝ (minusSpace N) :=
  finrank_ker_eq_of_pointwise (minusSpace N) (Pop N + LinearMap.id) fun f => by
    constructor
    · intro h u
      rw [mem_minusSpace]
      have := LinearMap.congr_fun h u
      simpa only [LinearMap.add_apply, LinearMap.id_apply, Pop_apply, LinearMap.zero_apply,
        add_eq_zero_iff_eq_neg] using this
    · intro h
      apply LinearMap.ext; intro u
      simp only [LinearMap.add_apply, LinearMap.id_apply, Pop_apply, LinearMap.zero_apply,
        add_eq_zero_iff_eq_neg]
      exact mem_minusSpace.mp (h u)

/-- **Parity (S5) from the frozen hypotheses.** The `+1` and `−1` eigenspaces of the homogenized
common NOT on the control space have the same dimension. -/
theorem finrank_plus_eq_finrank_minus {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) :
    Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N) := by
  have hpar := NativeGateBall.parity (Pop N) (Lop G hN.invol) (Lop_injective hN hG)
    (Lop_anti hN hG)
  rw [finrank_ker_Pop_sub, finrank_ker_Pop_add] at hpar
  exact Nat.eq_of_mul_eq_mul_left (one_le_finrank_minusSpace hN) hpar

/-! ### §J — the exclusions -/

/-- No even dimension carries a native gate. -/
theorem not_even_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) :
    ¬ Even d :=
  not_even_of_balanced (finrank_plus_add_finrank_minus hN.invol)
    (finrank_plus_eq_finrank_minus hN hG)

theorem ne_two_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) : d ≠ 2 :=
  fun h => not_even_of_nativeGate hN hG ⟨1, by omega⟩

theorem ne_four_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) : d ≠ 4 :=
  fun h => not_even_of_nativeGate hN hG ⟨2, by omega⟩

/-- The data the written S1–S2–S4 reduction extracts from a native gate whose `+1` eigenspace has
tangent dimension `p`: the `E₊` blocks `A`, `B` on a target index set of size `m`, antisymmetric
in the pair index, with the Lorentz positivity of `I + Γ` at `t = ±eᵢ` against every unit effect
and one nonzero entry. The reduction from `NativeGate` to this data is a written proof and is not
certified in this module; the data is the hypothesis of `NativeGateBall.p_le_one`. -/
structure BlockData (p : ℕ) : Prop where
  blocks : ∃ (m : ℕ) (A : Fin p → Matrix (Fin m) (Fin m) ℝ)
      (B : Fin p → Fin p → Matrix (Fin m) (Fin m) ℝ),
    (∀ r s, B r s = - B s r) ∧
    (∀ k l : Fin m, ∀ i : Fin p, ∀ s : ℝ, (s = 1 ∨ s = -1) →
      ∀ b : Fin p → ℝ, (∑ j, b j ^ 2) = 1 →
        0 ≤ (1 + s * A i k l)
          + ∑ j, b j * (A j k l + s * ((if j = i then (1:ℝ) else 0) + B j i k l))) ∧
    (∃ r k l, A r k l ≠ 0)

theorem p_le_one_of_blockData {p : ℕ} (h : BlockData p) : p ≤ 1 := by
  obtain ⟨m, A, B, hB, hpos, hne⟩ := h.blocks
  exact NativeGateBall.p_le_one p m A B hB hpos hne

/-- The tangent dimension of the `+1` eigenspace: its dimension less the unit direction. -/
noncomputable def tangentPlus (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) : ℕ :=
  Module.finrank ℝ (plusSpace N) - 1

/-- **The selector, conditional on the block reduction.** Two identical copies of the Euclidean
ball with a native gate whose block data is as the written reduction states have dimension one or
three. Parity is proved from the frozen hypotheses; the block data is the named premise. -/
theorem dim_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)
    (hB : BlockData (tangentPlus N)) : d = 1 ∨ d = 3 := by
  have hsum := finrank_plus_add_finrank_minus hN.invol
  have hbal := finrank_plus_eq_finrank_minus hN hG
  have hp := one_le_finrank_plusSpace N
  have hle := p_le_one_of_blockData hB
  exact NativeGateBall.dim_of_bounds (tangentPlus N) (Module.finrank ℝ (minusSpace N) - 1) d hle
    (by unfold tangentPlus; omega) (by unfold tangentPlus; omega)

theorem ne_five_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)
    (hB : BlockData (tangentPlus N)) : d ≠ 5 := by
  intro h
  rcases dim_of_nativeGate hN hG hB with h1 | h2 <;> omega

theorem ne_seven_of_nativeGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G)
    (hB : BlockData (tangentPlus N)) : d ≠ 7 := by
  intro h
  rcases dim_of_nativeGate hN hG hB with h1 | h2 <;> omega
