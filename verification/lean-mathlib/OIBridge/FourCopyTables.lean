/-
  OIBridge/FourCopyTables.lean — design (EQ4-F), not adopted: the table calculus of the Bell-link
  map. Every proof in this file is complete.

  * The token actions are left and right multiplications of the table (`tabMul_actC_left`,
    `tabMul_actT_right`); the transpose of a local map moves between the factors of a product
    (`tabMul_actT_left`, `tabMul_actC_right`); `phiW` is the table of `reflY`.
  * G1 (`link_mul`, `Theta_eq`): the link product of two Bell-type tables is
    `actC (A·reflY·Bᵀ) ∘ actT (C·reflY·Dᵀ)`, for all local maps; no orthogonality is used.
  * G2 (`Theta_ipW`, `ThetaInv_Theta`, `Theta_ThetaInv`): for orthogonal locals Θ is orthogonal
    for the pairing, with inverse `ThetaInv`.
  * G8 (`link_left_ctrl`, `link_left_target`, `link_right_ctrl`, `link_right_target`): the
    rotated-link identities.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.FourCopyLocal

namespace OIBridge
namespace FourCopy

open Set CompositeDimension K2Guard EffectSpace KInfFoundations TransitiveBody

noncomputable section

local notation "E3" => ((Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))

/-! ### §A — token actions as table products -/

theorem tabMul_actC_left (M : E3) (X Y : W 3) : tabMul (actC M X) Y = actC M (tabMul X Y) := by
  funext μ ν
  have h : (fun κ => tabMul X Y κ ν) = ∑ l, Y l ν • (fun κ => X κ l) := by
    funext κ
    simp only [tabMul, Finset.sum_apply, Pi.smul_apply, smul_eq_mul]
    exact Finset.sum_congr rfl fun l _ => mul_comm _ _
  show ∑ κ, homMap M (fun κ' => X κ' κ) μ * Y κ ν = homMap M (fun κ => tabMul X Y κ ν) μ
  rw [h, map_sum, Finset.sum_apply]
  refine Finset.sum_congr rfl fun l _ => ?_
  rw [map_smul, Pi.smul_apply, smul_eq_mul]
  exact mul_comm _ _

theorem tabMul_actT_right (M : E3) (X Y : W 3) : tabMul X (actT M Y) = actT M (tabMul X Y) := by
  funext μ ν
  have h : tabMul X Y μ = ∑ κ, X μ κ • Y κ := by
    funext ν'
    simp only [tabMul, Finset.sum_apply, Pi.smul_apply, smul_eq_mul]
  show ∑ κ, X μ κ * homMap M (Y κ) ν = homMap M (tabMul X Y μ) ν
  rw [h, map_sum, Finset.sum_apply]
  refine Finset.sum_congr rfl fun κ _ => ?_
  rw [map_smul, Pi.smul_apply, smul_eq_mul]

theorem tabT_actC (M : E3) (X : W 3) : tabT (actC M X) = actT M (tabT X) := rfl

theorem tabT_actT (M : E3) (X : W 3) : tabT (actT M X) = actC M (tabT X) := rfl

theorem tabMul_actT_left (M : E3) (X Y : W 3) :
    tabMul (actT M X) Y = tabMul X (actC (trn M) Y) := by
  funext μ ν
  have h := homMap_adj (trn M) (X μ) (fun κ => Y κ ν)
  rw [trn_trn] at h
  exact h.symm

theorem tabMul_actC_right (M : E3) (X Y : W 3) :
    tabMul X (actC M Y) = tabMul (actT (trn M) X) Y := by
  rw [tabMul_actT_left, trn_trn]

theorem tabMul_phiW_left (Z : W 3) : tabMul phiW Z = actC reflY Z := by
  rw [phiW_eq_dg]
  funext μ ν
  fin_cases μ <;> simp [tabMul, dg, actC_apply, sum_univ_four']

theorem tabMul_phiW_right (Z : W 3) : tabMul Z phiW = actT reflY Z := by
  rw [phiW_eq_dg]
  funext μ ν
  fin_cases ν <;> simp [tabMul, dg, actT_apply, sum_univ_four']

theorem tabT_phiW : tabT phiW = phiW := by
  rw [phiW_eq_dg]
  funext μ ν
  fin_cases μ <;> fin_cases ν <;> simp [tabT, dg]

theorem trn_comp (A B : E3) : trn (A ∘ₗ B) = trn B ∘ₗ trn A := by
  apply LinearMap.toMatrix'.injective
  rw [toMatrix'_trn, LinearMap.toMatrix'_comp, LinearMap.toMatrix'_comp, toMatrix'_trn,
    toMatrix'_trn, Matrix.transpose_mul]

/-! ### §B — G1: the link product -/

/-- **G1.** The link product of two Bell-type tables. No orthogonality is needed. -/
theorem link_mul (P Q R S : E3) (g : W 3) :
    tabMul (tabMul (actC P (actT Q phiW)) g) (tabT (actC R (actT S phiW))) =
      actC (chartOf P Q) (actT (chartOf R S) g) := by
  have hl : tabMul (actC P (actT Q phiW)) g = actC (P ∘ₗ reflY ∘ₗ trn Q) g := by
    rw [tabMul_actC_left, tabMul_actT_left, tabMul_phiW_left, actC_comp, actC_comp,
      LinearMap.comp_assoc]
  have hr : ∀ Z : W 3, tabMul Z (tabT (actC R (actT S phiW))) =
      actT (R ∘ₗ reflY ∘ₗ trn S) Z := by
    intro Z
    rw [tabT_actC, tabT_actT, tabT_phiW, tabMul_actT_right, tabMul_actC_right,
      tabMul_phiW_right, actT_comp, actT_comp, LinearMap.comp_assoc]
  rw [hl, tabMul_actC_left, hr, chartOf, chartOf]

/-- G1 for the Bell tables: `Θ = actC R02 ∘ actT R13`. -/
theorem Theta_eq (A02 B02 A13 B13 : E3) (g : W 3) :
    Theta A02 B02 A13 B13 g = actC (chartOf A02 B02) (actT (chartOf A13 B13) g) :=
  link_mul A02 B02 A13 B13 g

/-! ### §C — G2: Θ is orthogonal and invertible -/

theorem isOrth3_chartOf {A B : E3} (hA : IsOrth3 A) (hB : IsOrth3 B) : IsOrth3 (chartOf A B) :=
  isOrth3_comp hA (isOrth3_comp isOrth3_reflY (isOrth3_trn hB))

/-- **G2a.** Θ is orthogonal for the pairing. -/
theorem Theta_ipW {A02 B02 A13 B13 : E3} (h1 : IsOrth3 A02) (h2 : IsOrth3 B02)
    (h3 : IsOrth3 A13) (h4 : IsOrth3 B13) (E X : W 3) :
    ipW (Theta A02 B02 A13 B13 E) (Theta A02 B02 A13 B13 X) = ipW E X := by
  rw [Theta_eq, Theta_eq, ipW_actC_orth (isOrth3_chartOf h1 h2),
    ipW_actT_orth (isOrth3_chartOf h3 h4)]

/-- **G2b.** -/
theorem ThetaInv_Theta {A02 B02 A13 B13 : E3} (h1 : IsOrth3 A02) (h2 : IsOrth3 B02)
    (h3 : IsOrth3 A13) (h4 : IsOrth3 B13) (g : W 3) :
    ThetaInv A02 B02 A13 B13 (Theta A02 B02 A13 B13 g) = g := by
  rw [Theta_eq, ThetaInv, ← actC_actT_comm, actC_comp, actT_comp,
    trn_comp_self (isOrth3_chartOf h1 h2), trn_comp_self (isOrth3_chartOf h3 h4), actC_id,
    actT_id]

/-- **G2c.** -/
theorem Theta_ThetaInv {A02 B02 A13 B13 : E3} (h1 : IsOrth3 A02) (h2 : IsOrth3 B02)
    (h3 : IsOrth3 A13) (h4 : IsOrth3 B13) (g : W 3) :
    Theta A02 B02 A13 B13 (ThetaInv A02 B02 A13 B13 g) = g := by
  rw [Theta_eq, ThetaInv, ← actC_actT_comm, actC_comp, actT_comp,
    comp_trn_self (isOrth3_chartOf h1 h2), comp_trn_self (isOrth3_chartOf h3 h4), actC_id,
    actT_id]

/-! ### §D — G8: rotated links -/

/-- **G8a.** A rotated left link, control side. -/
theorem link_left_ctrl {Aa : E3} (hA : IsOrth3 Aa) (Ba Ab Bb M : E3) (g : W 3) :
    tabMul (tabMul (actC (Aa ∘ₗ M) (actT Ba phiW)) g) (tabT (bellOf Ab Bb)) =
      actC (Aa ∘ₗ M ∘ₗ trn Aa) (Theta Aa Ba Ab Bb g) := by
  rw [bellOf, link_mul, Theta_eq, actC_comp]
  congr 1
  refine LinearMap.ext fun x => ?_
  simp only [chartOf, LinearMap.comp_apply, trn_apply_apply hA]

/-- **G8b.** A rotated left link, target side. -/
theorem link_left_target (Aa : E3) {Ba : E3} (hB : IsOrth3 Ba) (Ab Bb M : E3) (g : W 3) :
    tabMul (tabMul (actC Aa (actT (Ba ∘ₗ M) phiW)) g) (tabT (bellOf Ab Bb)) =
      Theta Aa Ba Ab Bb (actC (Ba ∘ₗ trn M ∘ₗ trn Ba) g) := by
  rw [bellOf, link_mul, Theta_eq, ← actC_actT_comm, actC_comp]
  congr 1
  refine LinearMap.ext fun x => ?_
  simp only [chartOf, LinearMap.comp_apply, trn_comp, trn_apply_apply hB]

/-- **G8c.** A rotated right link, control side. -/
theorem link_right_ctrl (Aa Ba : E3) {Ab : E3} (hA : IsOrth3 Ab) (Bb M : E3) (g : W 3) :
    tabMul (tabMul (bellOf Aa Ba) g) (tabT (actC (Ab ∘ₗ M) (actT Bb phiW))) =
      actT (Ab ∘ₗ M ∘ₗ trn Ab) (Theta Aa Ba Ab Bb g) := by
  rw [bellOf, link_mul, Theta_eq, ← actC_actT_comm, actT_comp]
  congr 1
  congr 1
  refine LinearMap.ext fun x => ?_
  simp only [chartOf, LinearMap.comp_apply, trn_apply_apply hA]

/-- **G8d.** A rotated right link, target side. -/
theorem link_right_target (Aa Ba Ab : E3) {Bb : E3} (hB : IsOrth3 Bb) (M : E3) (g : W 3) :
    tabMul (tabMul (bellOf Aa Ba) g) (tabT (actC Ab (actT (Bb ∘ₗ M) phiW))) =
      Theta Aa Ba Ab Bb (actT (Bb ∘ₗ trn M ∘ₗ trn Bb) g) := by
  rw [bellOf, link_mul, Theta_eq, actT_comp]
  congr 1
  congr 1
  refine LinearMap.ext fun x => ?_
  simp only [chartOf, LinearMap.comp_apply, trn_comp, trn_apply_apply hB]

end

end FourCopy
end OIBridge

#print axioms OIBridge.FourCopy.tabMul_actC_left
#print axioms OIBridge.FourCopy.tabMul_actT_right
#print axioms OIBridge.FourCopy.tabMul_actT_left
#print axioms OIBridge.FourCopy.tabMul_phiW_left
#print axioms OIBridge.FourCopy.tabMul_phiW_right
#print axioms OIBridge.FourCopy.tabT_phiW
#print axioms OIBridge.FourCopy.trn_comp
#print axioms OIBridge.FourCopy.link_mul
#print axioms OIBridge.FourCopy.Theta_eq
#print axioms OIBridge.FourCopy.Theta_ipW
#print axioms OIBridge.FourCopy.ThetaInv_Theta
#print axioms OIBridge.FourCopy.Theta_ThetaInv
#print axioms OIBridge.FourCopy.link_left_ctrl
#print axioms OIBridge.FourCopy.link_left_target
#print axioms OIBridge.FourCopy.link_right_ctrl
#print axioms OIBridge.FourCopy.link_right_target
