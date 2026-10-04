/-
  OIBridge/CompositeInterface.lean — round COMP-1: the weak field-neutral composite interface.

  Two factor bodies `ΩA ⊆ (Fin dA → ℝ)` and `ΩB ⊆ (Fin dB → ℝ)` in chart coordinates, and a composite
  carrier `V`, an arbitrary real normed space. The composite is a structure over `V`, not a
  construction: a bi-affine product-state map, a bilinear product-effect pairing into the affine
  functionals of `V`, a convex body `Ω ⊆ V` containing the product states, positivity of product effects
  on `Ω`, normalization, and local tomography. Local tomography is a premise field of the structure,
  not a theorem; no quantum tensor structure, no complex structure, no Bell inequality and no dimension
  is claimed. Nothing here constructs a composite larger than the minimal body, sources local
  tomography, or identifies the quantum composite.

  The structure is layered so that the premise is visible as a premise:
    `ProductData`   — product states and the product-effect pairing with its evaluation law;
    `PreComposite`  — adds the body `Ω` and the four body laws (convexity, products in the body,
                      positivity of product effects, normalization);
    `Composite`     — adds the one field `lt`, local tomography.

  Attachment (`attach x := prodState x r₀`), discard (`margA ω i := prodEff (coord i) 1 ω`), the
  conditional state (`condA`) and the sharp register readout (`readout f k := prodEff 1 (f k)`) are
  definitions, not fields. Joint reversible action is `OrbitGeneration.PreservesBody` of the composite
  body.

    §A  coordinate vocabulary: the unit functional, the coordinate functionals, the expansion of an
        affine functional of the chart in them (`affine_expand`);
    §B  the three structures and the derived operations;
    §C  the laws, all theorems of `PreComposite` except the last:
        L1  `margA_prodState`   the marginal of a product is its factor;
        L2  `margA_attach`      attach then discard is the identity;
        L3  `eff_margA`         pairing with the marginal is the product pairing with the unit;
        L4  `margA_mem`         the marginal of a composite state is a state (compact convex factor);
        L5  `readout_sum`, `isEffectOn_readout`   a sharp readout is a two-outcome test;
        L6  `readout_prodState` readout on a product reads the register;
        L7  `readout_attach`    readout after attaching the matching register state is certain;
        L8  `condA_mem`         the conditional state is a state (compact convex factor);
        L9  `condA_prodState`   no signalling on products;
        L10 `jointReversible_words`, `isEffectOn_readout_seedTransport`  reversible actions compose;
        L11 `minBody_subset`, `subset_maxBody`, `Composite.pairing_injective`  the body lies between
            the minimal and the maximal body and the product pairing separates it;
    §D  the minimal and maximal bodies of any product data are pre-composites
        (`ProductData.minPre`, `ProductData.maxPre`);
    §E  the coordinate model `Fin (dA + 1) → Fin (dB + 1) → ℝ` of product data, in which the product
        pairing separates points; local tomography is a theorem of this model, through the extension
        of agreement on effect pairs to agreement on all pairs (`prodEff_eq_of_eff_eq`, which needs
        only that affine functionals are bounded on the factor bodies);
    §F  the instances `bitComposite` (classical bit and bit), `ball3MinComposite` and
        `ball3MaxComposite` (two copies of `KInfFoundations.ball3`, minimal and maximal body);
    §G  the padding control: for any pre-composite `P` with nonempty body, `paddedPre P` on `V × ℝ`
        satisfies every field of `PreComposite` and is not locally tomographic, so no `Composite`
        extends it (`not_locallyTomographic_paddedPre`, `no_composite_over_paddedPre`); the field `lt`
        is therefore independent of the other fields and is never derived from them.

  The coordinate model of §E is a function space on index pairs and realizes a tensor product; it is
  confined to the instances and enters no statement about the interface. The stage-level product of
  two `DirectedStages` and the bridge from completed product towers to this interface are not part of
  this module.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.CompletionAction
import Mathlib.Analysis.LocallyConvex.Separation
import Mathlib.Analysis.Normed.Module.FiniteDimension

namespace OIBridge
namespace CompositeInterface

open Set KInfFoundations OrbitGeneration OrbitNormalization

/-! ### §A — coordinate vocabulary of the chart -/

section Chart

variable {d : ℕ}

/-- The unit functional of the chart: the constant affine functional `1`. -/
def unitEff (d : ℕ) : (Fin d → ℝ) →ᵃ[ℝ] ℝ := AffineMap.const ℝ (Fin d → ℝ) (1 : ℝ)

@[simp] theorem unitEff_apply (x : Fin d → ℝ) : unitEff d x = 1 := rfl

theorem unitEff_linear : (unitEff d).linear = 0 := rfl

/-- The `i`-th coordinate functional of the chart. -/
def coord (i : Fin d) : (Fin d → ℝ) →ᵃ[ℝ] ℝ :=
  (LinearMap.proj i : (Fin d → ℝ) →ₗ[ℝ] ℝ).toAffineMap

@[simp] theorem coord_apply (i : Fin d) (x : Fin d → ℝ) : coord i x = x i := rfl

theorem coord_linear (i : Fin d) : (coord i).linear = LinearMap.proj i := rfl

/-- The unit functional is an effect on every body. -/
theorem isEffectOn_unitEff (Ω : Set (Fin d → ℝ)) : IsEffectOn Ω (unitEff d) := fun x _ => by
  rw [unitEff_apply]
  exact ⟨zero_le_one, le_rfl⟩

/-- The complement of an effect is an effect. -/
theorem isEffectOn_unitEff_sub {Ω : Set (Fin d → ℝ)} {e : (Fin d → ℝ) →ᵃ[ℝ] ℝ}
    (he : IsEffectOn Ω e) : IsEffectOn Ω (unitEff d - e) := fun x hx => by
  rw [AffineMap.coe_sub, Pi.sub_apply, unitEff_apply]
  exact ⟨by linarith [(he x hx).2], by linarith [(he x hx).1]⟩

/-- Evaluation at a point, as an additive map on affine functionals. -/
def evalAddHom {P : Type} [AddCommGroup P] [Module ℝ P] (x : P) : (P →ᵃ[ℝ] ℝ) →+ ℝ where
  toFun e := e x
  map_zero' := by
    show (0 : P →ᵃ[ℝ] ℝ) x = 0
    rw [AffineMap.coe_zero, Pi.zero_apply]
  map_add' e e' := by
    show (e + e') x = e x + e' x
    rw [AffineMap.coe_add, Pi.add_apply]

/-- A finite sum of affine functionals evaluates termwise. -/
theorem affine_sum_apply {P : Type} [AddCommGroup P] [Module ℝ P] {ι : Type} (s : Finset ι)
    (g : ι → P →ᵃ[ℝ] ℝ) (x : P) : (∑ i ∈ s, g i) x = ∑ i ∈ s, g i x :=
  map_sum (evalAddHom x) g s

/-- An affine functional of the chart is its value at `0` plus its coordinate expansion. -/
theorem affine_eval (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (x : Fin d → ℝ) :
    e x = e 0 + ∑ i, e.linear (fun j => if i = j then 1 else 0) * x i := by
  have h1 : e x = e.linear x + e 0 := by
    have := congrFun (AffineMap.decomp e) x
    rw [Pi.add_apply] at this
    exact this
  rw [h1, LinearMap.pi_apply_eq_sum_univ e.linear x, add_comm]
  congr 1
  exact Finset.sum_congr rfl fun i _ => by rw [smul_eq_mul, mul_comm]

/-- The expansion of an affine functional of the chart in the unit and the coordinates. -/
theorem affine_expand (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) :
    e = e 0 • unitEff d + ∑ i, e.linear (fun j => if i = j then 1 else 0) • coord i := by
  ext x
  rw [affine_eval e x, AffineMap.coe_add, Pi.add_apply, affine_sum_apply, AffineMap.coe_smul,
    Pi.smul_apply, smul_eq_mul, unitEff_apply, mul_one]
  congr 1
  exact Finset.sum_congr rfl fun i _ => by
    rw [AffineMap.coe_smul, Pi.smul_apply, smul_eq_mul, coord_apply]

/-- Every affine functional is bounded in absolute value on `Ω`. -/
def BoundedAffine (Ω : Set (Fin d → ℝ)) : Prop :=
  ∀ e : (Fin d → ℝ) →ᵃ[ℝ] ℝ, ∃ B : ℝ, ∀ x ∈ Ω, |e x| ≤ B

theorem boundedAffine_of_isCompact {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) : BoundedAffine Ω :=
  fun e => by
    obtain ⟨B, hB⟩ := hc.exists_bound_of_continuousOn e.continuous_of_finiteDimensional.continuousOn
    exact ⟨B, fun x hx => by rw [← Real.norm_eq_abs]; exact hB x hx⟩

/-- An affine functional bounded on `Ω` is an affine combination of an effect on `Ω` and the unit. -/
theorem exists_effect_rescale {Ω : Set (Fin d → ℝ)} (hb : BoundedAffine Ω)
    (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) :
    ∃ (e' : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (a c : ℝ), IsEffectOn Ω e' ∧ e = a • e' + c • unitEff d := by
  obtain ⟨B, hB⟩ := hb e
  set K : ℝ := |B| + 1 with hK
  have hKpos : 0 < K := by rw [hK]; positivity
  have h2K : 0 < 2 * K := mul_pos two_pos hKpos
  have hK0 : (2 * K) ≠ 0 := h2K.ne'
  refine ⟨(2 * K)⁻¹ • (e + K • unitEff d), 2 * K, -K, fun x hx => ?_, ?_⟩
  · obtain ⟨hlo, hhi⟩ := abs_le.mp (hB x hx)
    have hB1 : B ≤ |B| := le_abs_self B
    simp only [AffineMap.coe_smul, AffineMap.coe_add, Pi.smul_apply, Pi.add_apply, unitEff_apply,
      smul_eq_mul, mul_one]
    constructor
    · exact mul_nonneg (inv_nonneg.mpr h2K.le) (by linarith)
    · exact (inv_mul_le_one₀ h2K).mpr (by linarith)
  · ext x
    simp only [AffineMap.coe_smul, AffineMap.coe_add, Pi.smul_apply, Pi.add_apply, unitEff_apply,
      smul_eq_mul, mul_one]
    rw [← mul_assoc, mul_inv_cancel₀ hK0, one_mul]
    ring

/-- Separation: a point outside a compact convex body is strictly negative for some effect on it. -/
theorem exists_effect_neg {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω) (hconv : Convex ℝ Ω)
    {z : Fin d → ℝ} (hz : z ∉ Ω) :
    ∃ g : (Fin d → ℝ) →ᵃ[ℝ] ℝ, IsEffectOn Ω g ∧ g z < 0 := by
  obtain ⟨f, u, hfu, hu⟩ := geometric_hahn_banach_closed_point hconv hc.isClosed hz
  have hcont : Continuous fun a : Fin d → ℝ => u - f a := continuous_const.sub f.continuous
  obtain ⟨B, hB⟩ := hc.exists_bound_of_continuousOn hcont.continuousOn
  set K : ℝ := |B| + 1 with hK
  have hKpos : 0 < K := by rw [hK]; positivity
  set g : (Fin d → ℝ) →ᵃ[ℝ] ℝ :=
    K⁻¹ • (u • unitEff d - (f : (Fin d → ℝ) →ₗ[ℝ] ℝ).toAffineMap) with hg
  have hg_apply : ∀ x, g x = K⁻¹ * (u - f x) := fun x => by
    simp only [hg, AffineMap.coe_smul, Pi.smul_apply, AffineMap.coe_sub, Pi.sub_apply,
      unitEff_apply, LinearMap.coe_toAffineMap, ContinuousLinearMap.coe_coe, smul_eq_mul, mul_one]
  refine ⟨g, fun x hx => ?_, ?_⟩
  · rw [hg_apply]
    have h1 : f x < u := hfu x hx
    have h2 : ‖u - f x‖ ≤ B := hB x hx
    rw [Real.norm_eq_abs] at h2
    have h3 : u - f x ≤ K := by
      calc u - f x ≤ |u - f x| := le_abs_self _
        _ ≤ B := h2
        _ ≤ |B| := le_abs_self B
        _ ≤ K := by rw [hK]; linarith
    constructor
    · exact mul_nonneg (inv_nonneg.mpr hKpos.le) (by linarith)
    · exact (inv_mul_le_one₀ hKpos).mpr h3
  · rw [hg_apply]
    exact mul_neg_of_pos_of_neg (inv_pos.mpr hKpos) (by linarith)

end Chart

/-! ### §B — the structures and the derived operations -/

section Interface

variable {dA dB : ℕ}

/-- Product-state and product-effect data on a real carrier `V`: a bi-affine product-state map and a
bilinear product-effect pairing with the evaluation law `prodEff e f (prodState x y) = e x * f y`. -/
structure ProductData (dA dB : ℕ) (V : Type) [NormedAddCommGroup V] [NormedSpace ℝ V] where
  prodState : (Fin dA → ℝ) → (Fin dB → ℝ) → V
  prodState_combo_left : ∀ (x x' : Fin dA → ℝ) (y : Fin dB → ℝ) (a b : ℝ), a + b = 1 →
    prodState (a • x + b • x') y = a • prodState x y + b • prodState x' y
  prodState_combo_right : ∀ (x : Fin dA → ℝ) (y y' : Fin dB → ℝ) (a b : ℝ), a + b = 1 →
    prodState x (a • y + b • y') = a • prodState x y + b • prodState x y'
  prodEff : ((Fin dA → ℝ) →ᵃ[ℝ] ℝ) →ₗ[ℝ] ((Fin dB → ℝ) →ᵃ[ℝ] ℝ) →ₗ[ℝ] (V →ᵃ[ℝ] ℝ)
  prodEff_apply : ∀ (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (x : Fin dA → ℝ)
    (y : Fin dB → ℝ), prodEff e f (prodState x y) = e x * f y

/-- A pre-composite: product data together with a convex body `Ω` of the carrier that contains the
product states, on which every product of effects is an effect and the unit pairing is one. These are
the eight fields of the interface other than local tomography. -/
structure PreComposite (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)
    [NormedAddCommGroup V] [NormedSpace ℝ V] extends ProductData dA dB V where
  Ω : Set V
  convex : Convex ℝ Ω
  prod_mem : ∀ x ∈ ΩA, ∀ y ∈ ΩB, prodState x y ∈ Ω
  prodEff_effect : ∀ (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ),
    IsEffectOn ΩA e → IsEffectOn ΩB f → IsEffectOn Ω (prodEff e f)
  prodEff_unit : ∀ ω ∈ Ω, prodEff (unitEff dA) (unitEff dB) ω = 1

/-- Local tomography of a pre-composite: two states of the body that agree on every product of
effects are equal. Stated as a predicate so that it can be asserted of a structure as a field and
refuted of another as a control. -/
def LocallyTomographic {ΩA : Set (Fin dA → ℝ)} {ΩB : Set (Fin dB → ℝ)} {V : Type}
    [NormedAddCommGroup V] [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V) : Prop :=
  ∀ ω ∈ P.Ω, ∀ ω' ∈ P.Ω, (∀ (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ),
    IsEffectOn ΩA e → IsEffectOn ΩB f → P.prodEff e f ω = P.prodEff e f ω') → ω = ω'

/-- **The weak composite interface.** A pre-composite with local tomography as a field. The field
`lt` is a premise of the structure; it is not derived from the other eight fields anywhere in this
module, and §G exhibits a pre-composite for which it fails. -/
structure Composite (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)
    [NormedAddCommGroup V] [NormedSpace ℝ V] extends PreComposite ΩA ΩB V where
  lt : ∀ ω ∈ Ω, ∀ ω' ∈ Ω, (∀ (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ),
    IsEffectOn ΩA e → IsEffectOn ΩB f → prodEff e f ω = prodEff e f ω') → ω = ω'

namespace ProductData

variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] (D : ProductData dA dB V)

/-- Register attachment: the product with a fixed register state `r₀`. -/
def attach (r₀ : Fin dB → ℝ) (x : Fin dA → ℝ) : V := D.prodState x r₀

/-- Discard of the register: the marginal on the first factor, read in chart coordinates. -/
def margA (ω : V) : Fin dA → ℝ := fun i => D.prodEff (coord i) (unitEff dB) ω

/-- The conditional state of the first factor given the register effect `f`. -/
def condA (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (ω : V) : Fin dA → ℝ :=
  fun i => D.prodEff (coord i) f ω / D.prodEff (unitEff dA) f ω

/-- Sharp register readout: the register effect `f k` paired with the unit on the first factor. -/
def readout (f : Fin 2 → (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (k : Fin 2) : V →ᵃ[ℝ] ℝ :=
  D.prodEff (unitEff dA) (f k)

/-- The minimal body: the convex hull of the product states. -/
def minBody (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) : Set V :=
  convexHull ℝ (Set.image2 D.prodState ΩA ΩB)

/-- The maximal body: the normalized points nonnegative on every product of effects. -/
def maxBody (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) : Set V :=
  {ω | D.prodEff (unitEff dA) (unitEff dB) ω = 1 ∧
    ∀ (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ),
      IsEffectOn ΩA e → IsEffectOn ΩB f → 0 ≤ D.prodEff e f ω}

/-- Attachment is affine. -/
theorem attach_combo (r₀ : Fin dB → ℝ) (x x' : Fin dA → ℝ) {a b : ℝ} (hab : a + b = 1) :
    D.attach r₀ (a • x + b • x') = a • D.attach r₀ x + b • D.attach r₀ x' :=
  D.prodState_combo_left x x' r₀ a b hab

/-- The marginal is affine. -/
theorem margA_combo (ω ω' : V) {a b : ℝ} (hab : a + b = 1) :
    D.margA (a • ω + b • ω') = a • D.margA ω + b • D.margA ω' := by
  funext i
  show D.prodEff (coord i) (unitEff dB) (a • ω + b • ω') = _
  rw [Convex.combo_affine_apply hab]
  rfl

/-- The product pairing expanded in the coordinates of the first factor. -/
theorem prodEff_expand (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (ω : V) :
    D.prodEff e f ω = e 0 * D.prodEff (unitEff dA) f ω +
      ∑ i, e.linear (fun j => if i = j then 1 else 0) * D.prodEff (coord i) f ω := by
  have hexp := affine_expand e
  calc D.prodEff e f ω
      = D.prodEff (e 0 • unitEff dA +
          ∑ i, e.linear (fun j => if i = j then 1 else 0) • coord i) f ω := by rw [← hexp]
    _ = _ := by
        rw [map_add, LinearMap.add_apply, AffineMap.coe_add, Pi.add_apply, LinearMap.map_smul,
          LinearMap.smul_apply, AffineMap.coe_smul, Pi.smul_apply, smul_eq_mul, map_sum,
          LinearMap.sum_apply, affine_sum_apply]
        congr 1
        exact Finset.sum_congr rfl fun i _ => by
          rw [LinearMap.map_smul, LinearMap.smul_apply, AffineMap.coe_smul, Pi.smul_apply,
            smul_eq_mul]

/-- **L1.** The marginal of a product state is its first factor. -/
theorem margA_prodState (x : Fin dA → ℝ) (y : Fin dB → ℝ) : D.margA (D.prodState x y) = x := by
  funext i
  show D.prodEff (coord i) (unitEff dB) (D.prodState x y) = x i
  rw [D.prodEff_apply, coord_apply, unitEff_apply, mul_one]

/-- **L2.** Attach, then discard, is the identity. -/
theorem margA_attach (r₀ : Fin dB → ℝ) (x : Fin dA → ℝ) : D.margA (D.attach r₀ x) = x :=
  D.margA_prodState x r₀

/-- **L6.** Readout on a product state reads the register. -/
theorem readout_prodState (f : Fin 2 → (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (k : Fin 2) (x : Fin dA → ℝ)
    (y : Fin dB → ℝ) : D.readout f k (D.prodState x y) = f k y := by
  show D.prodEff (unitEff dA) (f k) (D.prodState x y) = f k y
  rw [D.prodEff_apply, unitEff_apply, one_mul]

/-- The conditional state evaluated on an affine functional. -/
theorem eff_condA (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) {ω : V} (hf : D.prodEff (unitEff dA) f ω ≠ 0)
    (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) :
    e (D.condA f ω) = D.prodEff e f ω / D.prodEff (unitEff dA) f ω := by
  rw [D.prodEff_expand e f ω, affine_eval e (D.condA f ω), add_div, Finset.sum_div,
    mul_div_cancel_right₀ _ hf]
  congr 1
  exact Finset.sum_congr rfl fun i _ => by
    show _ * (D.prodEff (coord i) f ω / D.prodEff (unitEff dA) f ω) = _
    rw [mul_div_assoc]

/-- **L9.** No signalling on products: the conditional state of a product is its first factor. -/
theorem condA_prodState (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) {y : Fin dB → ℝ} (hy : f y ≠ 0)
    (x : Fin dA → ℝ) : D.condA f (D.prodState x y) = x := by
  funext i
  show D.prodEff (coord i) f (D.prodState x y) / D.prodEff (unitEff dA) f (D.prodState x y) = x i
  rw [D.prodEff_apply, D.prodEff_apply, coord_apply, unitEff_apply, one_mul]
  exact mul_div_cancel_right₀ (x i) hy

/-- Agreement on all effect pairs extends to agreement on all pairs of affine functionals, when
affine functionals are bounded on the factor bodies. This is linearity of the pairing; it says nothing
about which points of the carrier the pairing separates. -/
theorem prodEff_eq_of_eff_eq {ΩA : Set (Fin dA → ℝ)} {ΩB : Set (Fin dB → ℝ)}
    (hA : BoundedAffine ΩA) (hB : BoundedAffine ΩB) {ω ω' : V}
    (H : ∀ (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ),
      IsEffectOn ΩA e → IsEffectOn ΩB f → D.prodEff e f ω = D.prodEff e f ω')
    (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) :
    D.prodEff e f ω = D.prodEff e f ω' := by
  have step : ∀ e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ, IsEffectOn ΩA e →
      D.prodEff e f ω = D.prodEff e f ω' := by
    intro e he
    obtain ⟨f', a, c, hf', rfl⟩ := exists_effect_rescale hB f
    simp only [map_add, LinearMap.map_smul, AffineMap.coe_add, Pi.add_apply, AffineMap.coe_smul,
      Pi.smul_apply]
    rw [H e f' he hf', H e (unitEff dB) he (isEffectOn_unitEff ΩB)]
  obtain ⟨e', a, c, he', rfl⟩ := exists_effect_rescale hA e
  simp only [map_add, LinearMap.map_smul, LinearMap.add_apply, LinearMap.smul_apply,
    AffineMap.coe_add, Pi.add_apply, AffineMap.coe_smul, Pi.smul_apply]
  rw [step e' he', step (unitEff dA) (isEffectOn_unitEff ΩA)]

end ProductData

namespace PreComposite

variable {ΩA : Set (Fin dA → ℝ)} {ΩB : Set (Fin dB → ℝ)} {V : Type} [NormedAddCommGroup V]
  [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V)

/-- The body is nonempty when both factor bodies are. -/
theorem nonempty_of (hA : ΩA.Nonempty) (hB : ΩB.Nonempty) : P.Ω.Nonempty :=
  let ⟨x, hx⟩ := hA
  let ⟨y, hy⟩ := hB
  ⟨_, P.prod_mem x hx y hy⟩

/-! ### §C — the laws -/

/-- **L3.** Pairing the marginal with an affine functional is the product pairing with the unit. -/
theorem eff_margA {ω : V} (hω : ω ∈ P.Ω) (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) :
    e (P.margA ω) = P.prodEff e (unitEff dB) ω := by
  rw [P.toProductData.prodEff_expand, P.prodEff_unit ω hω, mul_one, affine_eval e (P.margA ω)]
  rfl

/-- **L4.** The marginal of a composite state is a state of a compact convex factor body. -/
theorem margA_mem (hcA : IsCompact ΩA) (hconvA : Convex ℝ ΩA) {ω : V} (hω : ω ∈ P.Ω) :
    P.margA ω ∈ ΩA := by
  by_contra hnot
  obtain ⟨g, hg, hneg⟩ := exists_effect_neg hcA hconvA hnot
  have hpos : 0 ≤ P.prodEff g (unitEff dB) ω :=
    (P.prodEff_effect g (unitEff dB) hg (isEffectOn_unitEff ΩB) ω hω).1
  rw [← P.eff_margA hω g] at hpos
  linarith

/-- A sharp register readout: a perfectly distinguishable pair of register states and effects whose
two effects sum to the unit functional. -/
structure SharpReadout (ΩB : Set (Fin dB → ℝ)) where
  y : Fin 2 → (Fin dB → ℝ)
  f : Fin 2 → (Fin dB → ℝ) →ᵃ[ℝ] ℝ
  pd : PerfectlyDistinguishable ΩB y f
  sum_eq : f 0 + f 1 = unitEff dB

/-- When the register body affinely spans its chart, the functional identity `f 0 + f 1 = 1` follows
from perfect distinguishability. -/
theorem sum_eq_unitEff_of_affineSpan (hspan : affineSpan ℝ ΩB = ⊤) {y : Fin 2 → (Fin dB → ℝ)}
    {f : Fin 2 → (Fin dB → ℝ) →ᵃ[ℝ] ℝ} (hpd : PerfectlyDistinguishable ΩB y f) :
    f 0 + f 1 = unitEff dB :=
  AffineMap.ext_on hspan fun x hx => by
    have := hpd.2.2.1 x hx
    rw [Fin.sum_univ_two] at this
    rw [AffineMap.coe_add, Pi.add_apply, unitEff_apply]
    exact this

/-- **L5, the test clause.** The two readout effects sum to one on the body. -/
theorem readout_sum (R : SharpReadout ΩB) {ω : V} (hω : ω ∈ P.Ω) :
    P.readout R.f 0 ω + P.readout R.f 1 ω = 1 := by
  have h := P.prodEff_unit ω hω
  rw [← R.sum_eq, map_add, AffineMap.coe_add, Pi.add_apply] at h
  exact h

/-- **L5, the effect clause.** Each readout is an effect on the body. -/
theorem isEffectOn_readout (f : Fin 2 → (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (hf : ∀ k, IsEffectOn ΩB (f k))
    (k : Fin 2) : IsEffectOn P.Ω (P.readout f k) :=
  P.prodEff_effect _ _ (isEffectOn_unitEff ΩA) (hf k)

/-- **L7.** Readout after attaching the matching register state is certain. -/
theorem readout_attach (R : SharpReadout ΩB) (k : Fin 2) (x : Fin dA → ℝ) :
    P.readout R.f k (P.attach (R.y k) x) = 1 := by
  show P.prodEff (unitEff dA) (R.f k) (P.prodState x (R.y k)) = 1
  rw [P.prodEff_apply, unitEff_apply, one_mul]
  exact R.pd.2.2.2 k

/-- **L8.** The conditional state given a register effect of nonzero probability is a state of a
compact convex factor body. -/
theorem condA_mem (hcA : IsCompact ΩA) (hconvA : Convex ℝ ΩA) {f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ}
    (hf : IsEffectOn ΩB f) {ω : V} (hω : ω ∈ P.Ω) (hne : P.prodEff (unitEff dA) f ω ≠ 0) :
    P.condA f ω ∈ ΩA := by
  by_contra hnot
  obtain ⟨g, hg, hneg⟩ := exists_effect_neg hcA hconvA hnot
  have hp : 0 < P.prodEff (unitEff dA) f ω :=
    lt_of_le_of_ne (P.prodEff_effect _ _ (isEffectOn_unitEff ΩA) hf ω hω).1 (Ne.symm hne)
  have hnum : 0 ≤ P.prodEff g f ω := (P.prodEff_effect g f hg hf ω hω).1
  have : 0 ≤ g (P.condA f ω) := by
    rw [P.toProductData.eff_condA f hne g]
    exact div_nonneg hnum hp.le
  linarith

/-- Joint reversible action: a family of affine automorphisms of the carrier preserving the body. -/
abbrev JointReversible (G : Set (V ≃ᵃ[ℝ] V)) : Prop := PreservesBody P.Ω G

/-- **L10.** Joint reversible actions compose: every word in a body-preserving family preserves the
body. -/
theorem jointReversible_words {G : Set (V ≃ᵃ[ℝ] V)} (hG : P.JointReversible G) :
    P.JointReversible (words G) :=
  preservesBody_words hG

/-- A readout transported along a joint reversible action is an effect on the body. -/
theorem isEffectOn_readout_seedTransport {G : Set (V ≃ᵃ[ℝ] V)} (hG : P.JointReversible G)
    {g : V ≃ᵃ[ℝ] V} (hg : g ∈ G) (f : Fin 2 → (Fin dB → ℝ) →ᵃ[ℝ] ℝ)
    (hf : ∀ k, IsEffectOn ΩB (f k)) (k : Fin 2) :
    IsEffectOn P.Ω (seedTransport (P.readout f k) g) :=
  isEffectOn_seedTransport (P.isEffectOn_readout f hf k) fun x hx => (hG g hg x hx).2

/-- **L11, lower bound.** The minimal body lies in the body. -/
theorem minBody_subset : P.toProductData.minBody ΩA ΩB ⊆ P.Ω :=
  convexHull_min (fun ω hω => by
    obtain ⟨x, hx, y, hy, rfl⟩ := hω
    exact P.prod_mem x hx y hy) P.convex

/-- **L11, upper bound.** The body lies in the maximal body. -/
theorem subset_maxBody : P.Ω ⊆ P.toProductData.maxBody ΩA ΩB := fun ω hω =>
  ⟨P.prodEff_unit ω hω, fun e f he hf => (P.prodEff_effect e f he hf ω hω).1⟩

end PreComposite

namespace Composite

variable {ΩA : Set (Fin dA → ℝ)} {ΩB : Set (Fin dB → ℝ)} {V : Type} [NormedAddCommGroup V]
  [NormedSpace ℝ V] (C : Composite ΩA ΩB V)

/-- **L11, separation.** On the body, the table of product-effect values determines the state. -/
theorem pairing_injective :
    Function.Injective fun ω : C.Ω => fun (e : {e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ // IsEffectOn ΩA e})
      (f : {f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ // IsEffectOn ΩB f}) => C.prodEff e.1 f.1 ω.1 := by
  intro ω ω' h
  apply Subtype.ext
  refine C.lt ω.1 ω.2 ω'.1 ω'.2 fun e f he hf => ?_
  exact congrFun (congrFun h ⟨e, he⟩) ⟨f, hf⟩

end Composite

/-! ### §D — the minimal and maximal bodies of any product data are pre-composites -/

namespace ProductData

variable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] (D : ProductData dA dB V)
  (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ))

theorem isEffectOn_minBody {e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ} {f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ}
    (he : IsEffectOn ΩA e) (hf : IsEffectOn ΩB f) : IsEffectOn (D.minBody ΩA ΩB) (D.prodEff e f) := by
  have hconv : Convex ℝ {ω : V | 0 ≤ D.prodEff e f ω ∧ D.prodEff e f ω ≤ 1} := by
    intro ω hω ω' hω' a b ha hb hab
    simp only [Set.mem_setOf_eq] at hω hω' ⊢
    rw [Convex.combo_affine_apply hab, smul_eq_mul, smul_eq_mul]
    constructor
    · exact add_nonneg (mul_nonneg ha hω.1) (mul_nonneg hb hω'.1)
    · calc a * D.prodEff e f ω + b * D.prodEff e f ω' ≤ a * 1 + b * 1 :=
            add_le_add (mul_le_mul_of_nonneg_left hω.2 ha) (mul_le_mul_of_nonneg_left hω'.2 hb)
        _ = 1 := by rw [mul_one, mul_one, hab]
  have hsub : Set.image2 D.prodState ΩA ΩB ⊆
      {ω : V | 0 ≤ D.prodEff e f ω ∧ D.prodEff e f ω ≤ 1} := by
    intro ω hω
    obtain ⟨x, hx, y, hy, rfl⟩ := hω
    rw [Set.mem_setOf_eq, D.prodEff_apply]
    exact ⟨mul_nonneg (he x hx).1 (hf y hy).1, mul_le_one₀ (he x hx).2 (hf y hy).1 (hf y hy).2⟩
  exact fun ω hω => convexHull_min hsub hconv hω

theorem unit_eq_one_minBody {ω : V} (hω : ω ∈ D.minBody ΩA ΩB) :
    D.prodEff (unitEff dA) (unitEff dB) ω = 1 := by
  have hconv : Convex ℝ {ω : V | D.prodEff (unitEff dA) (unitEff dB) ω = 1} := by
    intro ω hω ω' hω' a b ha hb hab
    simp only [Set.mem_setOf_eq] at hω hω' ⊢
    rw [Convex.combo_affine_apply hab, hω, hω', smul_eq_mul, smul_eq_mul, mul_one, mul_one, hab]
  have hsub : Set.image2 D.prodState ΩA ΩB ⊆
      {ω : V | D.prodEff (unitEff dA) (unitEff dB) ω = 1} := by
    intro ω hω
    obtain ⟨x, hx, y, hy, rfl⟩ := hω
    rw [Set.mem_setOf_eq, D.prodEff_apply, unitEff_apply, unitEff_apply, mul_one]
  exact convexHull_min hsub hconv hω

/-- The minimal body is a pre-composite. -/
def minPre : PreComposite ΩA ΩB V where
  toProductData := D
  Ω := D.minBody ΩA ΩB
  convex := convex_convexHull ℝ _
  prod_mem x hx y hy := subset_convexHull ℝ _ (Set.mem_image2_of_mem hx hy)
  prodEff_effect _ _ he hf := D.isEffectOn_minBody ΩA ΩB he hf
  prodEff_unit _ hω := D.unit_eq_one_minBody ΩA ΩB hω

theorem maxBody_convex : Convex ℝ (D.maxBody ΩA ΩB) := by
  intro ω hω ω' hω' a b ha hb hab
  obtain ⟨h1, h2⟩ := hω
  obtain ⟨h1', h2'⟩ := hω'
  refine ⟨?_, fun e f he hf => ?_⟩
  · rw [Convex.combo_affine_apply hab, h1, h1', smul_eq_mul, smul_eq_mul, mul_one, mul_one, hab]
  · rw [Convex.combo_affine_apply hab, smul_eq_mul, smul_eq_mul]
    exact add_nonneg (mul_nonneg ha (h2 e f he hf)) (mul_nonneg hb (h2' e f he hf))

theorem isEffectOn_maxBody {e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ} {f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ}
    (he : IsEffectOn ΩA e) (hf : IsEffectOn ΩB f) : IsEffectOn (D.maxBody ΩA ΩB) (D.prodEff e f) := by
  intro ω hω
  obtain ⟨h1, h2⟩ := hω
  refine ⟨h2 e f he hf, ?_⟩
  have ha := h2 (unitEff dA - e) f (isEffectOn_unitEff_sub he) hf
  have hb := h2 (unitEff dA) (unitEff dB - f) (isEffectOn_unitEff ΩA) (isEffectOn_unitEff_sub hf)
  rw [map_sub, LinearMap.sub_apply, AffineMap.coe_sub, Pi.sub_apply] at ha
  rw [map_sub, AffineMap.coe_sub, Pi.sub_apply, h1] at hb
  linarith

/-- The maximal body is a pre-composite. -/
def maxPre : PreComposite ΩA ΩB V where
  toProductData := D
  Ω := D.maxBody ΩA ΩB
  convex := D.maxBody_convex ΩA ΩB
  prod_mem x hx y hy :=
    ⟨by rw [D.prodEff_apply, unitEff_apply, unitEff_apply, mul_one],
      fun e f he hf => by rw [D.prodEff_apply]; exact mul_nonneg (he x hx).1 (hf y hy).1⟩
  prodEff_effect _ _ he hf := D.isEffectOn_maxBody ΩA ΩB he hf
  prodEff_unit _ hω := hω.1

end ProductData

end Interface

/-! ### §E — the coordinate model -/

namespace Model

variable {d dA dB : ℕ}

/-- The coordinate carrier of the model: functions on index pairs, each index carrying one
homogeneous coordinate. -/
abbrev Carrier (dA dB : ℕ) := Fin (dA + 1) → Fin (dB + 1) → ℝ

/-- Homogeneous coordinates of a chart point: `1` followed by the coordinates. -/
def hom (x : Fin d → ℝ) : Fin (d + 1) → ℝ := Fin.cons 1 x

theorem hom_zero (x : Fin d → ℝ) : hom x 0 = 1 := by
  unfold hom
  rw [Fin.cons_zero]

theorem hom_succ (x : Fin d → ℝ) (i : Fin d) : hom x i.succ = x i := by
  unfold hom
  rw [Fin.cons_succ]

theorem hom_combo {x x' : Fin d → ℝ} {a b : ℝ} (hab : a + b = 1) :
    hom (a • x + b • x') = a • hom x + b • hom x' := by
  funext μ
  refine Fin.cases ?_ (fun i => ?_) μ
  · simp only [hom_zero, Pi.add_apply, Pi.smul_apply, smul_eq_mul, mul_one]
    exact hab.symm
  · simp only [hom_succ, Pi.add_apply, Pi.smul_apply, smul_eq_mul]

/-- Homogeneous coefficients of an affine functional: its value at `0` followed by its linear
coefficients. -/
def coeff (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) : Fin (d + 1) → ℝ :=
  Fin.cons (e 0) fun i => e.linear (fun j => if i = j then 1 else 0)

theorem coeff_zero (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) : coeff e 0 = e 0 := by
  unfold coeff
  rw [Fin.cons_zero]

theorem coeff_succ (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (i : Fin d) :
    coeff e i.succ = e.linear (fun j => if i = j then 1 else 0) := by
  unfold coeff
  rw [Fin.cons_succ]

/-- The homogeneous pairing of coefficients and coordinates is evaluation. -/
theorem sum_coeff_hom (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (x : Fin d → ℝ) :
    ∑ μ, coeff e μ * hom x μ = e x := by
  rw [Fin.sum_univ_succ, coeff_zero, hom_zero, mul_one, affine_eval e x]
  congr 1
  exact Finset.sum_congr rfl fun i _ => by rw [coeff_succ, hom_succ]

theorem coeff_add (e e' : (Fin d → ℝ) →ᵃ[ℝ] ℝ) : coeff (e + e') = coeff e + coeff e' := by
  funext μ
  refine Fin.cases ?_ (fun i => ?_) μ
  · simp only [coeff_zero, Pi.add_apply, AffineMap.coe_add]
  · simp only [coeff_succ, Pi.add_apply, AffineMap.add_linear, LinearMap.add_apply]

theorem coeff_smul (a : ℝ) (e : (Fin d → ℝ) →ᵃ[ℝ] ℝ) : coeff (a • e) = a • coeff e := by
  funext μ
  refine Fin.cases ?_ (fun i => ?_) μ
  · simp only [coeff_zero, Pi.smul_apply, AffineMap.coe_smul]
  · simp only [coeff_succ, Pi.smul_apply, AffineMap.smul_linear, LinearMap.smul_apply]

/-- The product state of the model. -/
def pState (x : Fin dA → ℝ) (y : Fin dB → ℝ) : Carrier dA dB := fun μ ν => hom x μ * hom y ν

/-- The product effect of the model, as a linear functional of the carrier. -/
def pEffLin (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) : Carrier dA dB →ₗ[ℝ] ℝ where
  toFun ω := ∑ μ, ∑ ν, coeff e μ * coeff f ν * ω μ ν
  map_add' ω ω' := by
    simp only [Pi.add_apply, mul_add, Finset.sum_add_distrib]
  map_smul' a ω := by
    simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply, Finset.mul_sum]
    refine Finset.sum_congr rfl fun μ _ => Finset.sum_congr rfl fun ν _ => ?_
    ring

/-- The product effect of the model, as an affine functional. -/
def pEff (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) : Carrier dA dB →ᵃ[ℝ] ℝ :=
  (pEffLin e f).toAffineMap

theorem pEff_apply (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (ω : Carrier dA dB) :
    pEff e f ω = ∑ μ, ∑ ν, coeff e μ * coeff f ν * ω μ ν := rfl

theorem pEff_pState (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (x : Fin dA → ℝ)
    (y : Fin dB → ℝ) : pEff e f (pState x y) = e x * f y := by
  rw [pEff_apply, ← sum_coeff_hom e x, ← sum_coeff_hom f y, Finset.sum_mul_sum]
  refine Finset.sum_congr rfl fun μ _ => Finset.sum_congr rfl fun ν _ => ?_
  show coeff e μ * coeff f ν * (hom x μ * hom y ν) = coeff e μ * hom x μ * (coeff f ν * hom y ν)
  ring

theorem pEff_add_left (e e' : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) :
    pEff (e + e') f = pEff e f + pEff e' f := by
  ext ω
  simp only [pEff_apply, AffineMap.coe_add, Pi.add_apply, coeff_add, add_mul,
    Finset.sum_add_distrib]

theorem pEff_smul_left (a : ℝ) (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) :
    pEff (a • e) f = a • pEff e f := by
  ext ω
  simp only [pEff_apply, AffineMap.coe_smul, Pi.smul_apply, coeff_smul, smul_eq_mul, Finset.mul_sum]
  refine Finset.sum_congr rfl fun μ _ => Finset.sum_congr rfl fun ν _ => ?_
  ring

theorem pEff_add_right (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f f' : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) :
    pEff e (f + f') = pEff e f + pEff e f' := by
  ext ω
  simp only [pEff_apply, AffineMap.coe_add, Pi.add_apply, coeff_add, mul_add, add_mul,
    Finset.sum_add_distrib]

theorem pEff_smul_right (a : ℝ) (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) :
    pEff e (a • f) = a • pEff e f := by
  ext ω
  simp only [pEff_apply, AffineMap.coe_smul, Pi.smul_apply, coeff_smul, smul_eq_mul, Finset.mul_sum]
  refine Finset.sum_congr rfl fun μ _ => Finset.sum_congr rfl fun ν _ => ?_
  ring

/-- The product data of the coordinate model. -/
def modelData (dA dB : ℕ) : ProductData dA dB (Carrier dA dB) where
  prodState := pState
  prodState_combo_left x x' y a b hab := by
    funext μ ν
    simp only [pState, Pi.add_apply, Pi.smul_apply, smul_eq_mul, hom_combo hab]
    ring
  prodState_combo_right x y y' a b hab := by
    funext μ ν
    simp only [pState, Pi.add_apply, Pi.smul_apply, smul_eq_mul, hom_combo hab]
    ring
  prodEff := LinearMap.mk₂ ℝ pEff pEff_add_left pEff_smul_left pEff_add_right pEff_smul_right
  prodEff_apply e f x y := by
    rw [LinearMap.mk₂_apply]
    exact pEff_pState e f x y

theorem modelData_prodEff (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) :
    (modelData dA dB).prodEff e f = pEff e f := rfl

/-- The homogeneous basis functionals: the unit, then the coordinates. -/
def basisEff (μ : Fin (d + 1)) : (Fin d → ℝ) →ᵃ[ℝ] ℝ := Fin.cons (unitEff d) coord μ

theorem coeff_basisEff (μ ν : Fin (d + 1)) : coeff (basisEff μ) ν = if μ = ν then 1 else 0 := by
  refine Fin.cases ?_ (fun i => ?_) μ <;> refine Fin.cases ?_ (fun j => ?_) ν
  · rw [coeff_zero, basisEff, Fin.cons_zero, unitEff_apply, if_pos rfl]
  · rw [coeff_succ, basisEff, Fin.cons_zero, unitEff_linear, LinearMap.zero_apply,
      if_neg (Fin.succ_ne_zero j).symm]
  · rw [coeff_zero, basisEff, Fin.cons_succ, coord_apply, Pi.zero_apply,
      if_neg (Fin.succ_ne_zero i)]
  · rw [coeff_succ, basisEff, Fin.cons_succ, coord_linear, LinearMap.proj_apply]
    by_cases h : i = j
    · subst h
      rw [if_pos rfl, if_pos rfl]
    · rw [if_neg (Ne.symm h), if_neg (fun h' => h (Fin.succ_inj.mp h'))]

/-- The pairing of two basis functionals reads one coordinate of the carrier. -/
theorem pEff_basisEff (μ : Fin (dA + 1)) (ν : Fin (dB + 1)) (ω : Carrier dA dB) :
    pEff (basisEff μ) (basisEff ν) ω = ω μ ν := by
  rw [pEff_apply]
  simp only [coeff_basisEff]
  rw [Finset.sum_eq_single μ]
  · rw [Finset.sum_eq_single ν]
    · rw [if_pos rfl, if_pos rfl, one_mul, one_mul]
    · intro ν' _ hν'
      rw [if_neg (Ne.symm hν'), mul_zero, zero_mul]
    · intro h
      exact absurd (Finset.mem_univ ν) h
  · intro μ' _ hμ'
    rw [if_neg (Ne.symm hμ')]
    simp only [zero_mul, Finset.sum_const_zero]
  · intro h
    exact absurd (Finset.mem_univ μ) h

/-- In the coordinate model the product pairing separates points of the carrier. -/
theorem modelData_ext {ω ω' : Carrier dA dB}
    (h : ∀ (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ),
      (modelData dA dB).prodEff e f ω = (modelData dA dB).prodEff e f ω') : ω = ω' := by
  funext μ ν
  have := h (basisEff μ) (basisEff ν)
  simp only [modelData_prodEff, pEff_basisEff] at this
  exact this

/-- The minimal composite of two compact factor bodies in the coordinate model. Local tomography is a
theorem of this model: agreement on effect pairs extends to all pairs, which separate points. -/
def minComposite {ΩA : Set (Fin dA → ℝ)} {ΩB : Set (Fin dB → ℝ)} (hA : IsCompact ΩA)
    (hB : IsCompact ΩB) : Composite ΩA ΩB (Carrier dA dB) where
  toPreComposite := (modelData dA dB).minPre ΩA ΩB
  lt _ _ _ _ H := modelData_ext fun e f =>
    (modelData dA dB).prodEff_eq_of_eff_eq (boundedAffine_of_isCompact hA)
      (boundedAffine_of_isCompact hB) H e f

/-- The maximal composite of two compact factor bodies in the coordinate model. -/
def maxComposite {ΩA : Set (Fin dA → ℝ)} {ΩB : Set (Fin dB → ℝ)} (hA : IsCompact ΩA)
    (hB : IsCompact ΩB) : Composite ΩA ΩB (Carrier dA dB) where
  toPreComposite := (modelData dA dB).maxPre ΩA ΩB
  lt _ _ _ _ H := modelData_ext fun e f =>
    (modelData dA dB).prodEff_eq_of_eff_eq (boundedAffine_of_isCompact hA)
      (boundedAffine_of_isCompact hB) H e f

end Model

/-! ### §F — the instances -/

section Instances

open Model

/-- The probability simplex is compact. -/
theorem simplex_isCompact (N : ℕ) : IsCompact (simplex N) := by
  have hcl : IsClosed (simplex N) := by
    have h1 : IsClosed {p : Fin N → ℝ | ∀ i, 0 ≤ p i} := by
      have : {p : Fin N → ℝ | ∀ i, 0 ≤ p i} = ⋂ i, {p : Fin N → ℝ | 0 ≤ p i} := by
        ext p
        simp only [Set.mem_setOf_eq, Set.mem_iInter]
      rw [this]
      exact isClosed_iInter fun i => isClosed_le continuous_const (continuous_apply i)
    have h2 : IsClosed {p : Fin N → ℝ | ∑ i, p i = 1} :=
      isClosed_eq (continuous_finsetSum _ fun i _ => continuous_apply i) continuous_const
    exact h1.inter h2
  have hbd : simplex N ⊆ Metric.closedBall (0 : Fin N → ℝ) 1 := by
    intro p hp
    obtain ⟨hnn, hsum⟩ := hp
    rw [Metric.mem_closedBall, dist_zero_right, pi_norm_le_iff_of_nonneg zero_le_one]
    intro i
    rw [Real.norm_eq_abs, abs_le]
    have hle : p i ≤ 1 := by
      rw [← hsum]
      exact Finset.single_le_sum (fun j _ => hnn j) (Finset.mem_univ i)
    exact ⟨by linarith [hnn i], hle⟩
  exact Metric.isCompact_of_isClosed_isBounded hcl (Metric.isBounded_closedBall.subset hbd)

theorem zero_mem_ball3 : (0 : Fin 3 → ℝ) ∈ ball3 := by
  rw [mem_ball3]
  simp

/-- **Instance: the classical bit and bit.** Two copies of the probability simplex on two points,
with the minimal body. -/
def bitComposite : Composite (simplex 2) (simplex 2) (Carrier 2 2) :=
  minComposite (simplex_isCompact 2) (simplex_isCompact 2)

/-- **Instance: two copies of the ball, minimal body.** -/
def ball3MinComposite : Composite ball3 ball3 (Carrier 3 3) :=
  minComposite ball3_isCompact ball3_isCompact

/-- **Instance: two copies of the ball, maximal body.** -/
def ball3MaxComposite : Composite ball3 ball3 (Carrier 3 3) :=
  maxComposite ball3_isCompact ball3_isCompact

theorem vec10_mem_simplex : (![1, 0] : Fin 2 → ℝ) ∈ simplex 2 := by
  refine ⟨fun i => ?_, ?_⟩
  · fin_cases i <;> simp
  · rw [Fin.sum_univ_two]
    simp

theorem bitComposite_nonempty : bitComposite.Ω.Nonempty :=
  bitComposite.toPreComposite.nonempty_of ⟨_, vec10_mem_simplex⟩ ⟨_, vec10_mem_simplex⟩

theorem ball3MinComposite_nonempty : ball3MinComposite.Ω.Nonempty :=
  ball3MinComposite.toPreComposite.nonempty_of ⟨0, zero_mem_ball3⟩ ⟨0, zero_mem_ball3⟩

/-- The minimal body of the ball pair lies in its maximal body: L11 on the instances. -/
theorem ball3Min_subset_ball3Max : ball3MinComposite.Ω ⊆ ball3MaxComposite.Ω :=
  ball3MinComposite.toPreComposite.subset_maxBody

end Instances

/-! ### §G — the padding control -/

section Padding

variable {dA dB : ℕ} {ΩA : Set (Fin dA → ℝ)} {ΩB : Set (Fin dB → ℝ)} {V : Type}
  [NormedAddCommGroup V] [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V)

/-- The padded pairing: the pairing of `P` read on the first component of `V × ℝ`. -/
def padEff (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) : V × ℝ →ᵃ[ℝ] ℝ :=
  (P.prodEff e f).comp (AffineMap.fst : V × ℝ →ᵃ[ℝ] V)

theorem padEff_apply (e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ) (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (p : V × ℝ) :
    padEff P e f p = P.prodEff e f p.1 := rfl

/-- **The padding control.** The carrier `V × ℝ`, the body `P.Ω ×ˢ [0, 1]`, product states at height
`0` and the pairing read on the first component satisfy every field of `PreComposite`. -/
def paddedPre : PreComposite ΩA ΩB (V × ℝ) where
  prodState x y := (P.prodState x y, 0)
  prodState_combo_left x x' y a b hab := by
    rw [P.prodState_combo_left x x' y a b hab]
    exact Prod.ext (by simp) (by simp)
  prodState_combo_right x y y' a b hab := by
    rw [P.prodState_combo_right x y y' a b hab]
    exact Prod.ext (by simp) (by simp)
  prodEff := LinearMap.mk₂ ℝ (padEff P)
    (fun e e' f => by
      ext p
      simp only [padEff_apply, map_add, LinearMap.add_apply, AffineMap.coe_add, Pi.add_apply])
    (fun a e f => by
      ext p
      simp only [padEff_apply, LinearMap.map_smul, LinearMap.smul_apply, AffineMap.coe_smul,
        Pi.smul_apply])
    (fun e f f' => by
      ext p
      simp only [padEff_apply, map_add, AffineMap.coe_add, Pi.add_apply])
    (fun a e f => by
      ext p
      simp only [padEff_apply, LinearMap.map_smul, AffineMap.coe_smul, Pi.smul_apply])
  prodEff_apply e f x y := by
    rw [LinearMap.mk₂_apply, padEff_apply]
    exact P.prodEff_apply e f x y
  Ω := P.Ω ×ˢ Set.Icc (0 : ℝ) 1
  convex := P.convex.prod (convex_Icc 0 1)
  prod_mem x hx y hy := ⟨P.prod_mem x hx y hy, le_rfl, zero_le_one⟩
  prodEff_effect e f he hf p hp := by
    rw [LinearMap.mk₂_apply, padEff_apply]
    exact P.prodEff_effect e f he hf p.1 hp.1
  prodEff_unit p hp := by
    rw [LinearMap.mk₂_apply, padEff_apply]
    exact P.prodEff_unit p.1 hp.1

/-- **Local tomography fails for the padded pre-composite.** The two points of the body over one
state of `P` at heights `0` and `1` agree on every product of effects and differ. -/
theorem not_locallyTomographic_paddedPre (hne : P.Ω.Nonempty) :
    ¬ LocallyTomographic (paddedPre P) := by
  intro hlt
  obtain ⟨ω₀, hω₀⟩ := hne
  have h01 : ((ω₀, (0 : ℝ)) : V × ℝ) = (ω₀, 1) :=
    hlt (ω₀, 0) ⟨hω₀, le_rfl, zero_le_one⟩ (ω₀, 1) ⟨hω₀, zero_le_one, le_rfl⟩ fun _ _ _ _ => rfl
  exact zero_ne_one (congrArg Prod.snd h01)

/-- **No composite extends the padded pre-composite.** The eight fields other than `lt` do not
determine `lt`. -/
theorem no_composite_over_paddedPre (hne : P.Ω.Nonempty) :
    ¬ ∃ C : Composite ΩA ΩB (V × ℝ), C.toPreComposite = paddedPre P := by
  rintro ⟨C, hC⟩
  have hlt : LocallyTomographic C.toPreComposite := C.lt
  rw [hC] at hlt
  exact not_locallyTomographic_paddedPre P hne hlt

end Padding

section PaddedInstance

open Model

/-- The padding control on the ball pair. -/
def paddedBall3 : PreComposite ball3 ball3 (Carrier 3 3 × ℝ) :=
  paddedPre ball3MinComposite.toPreComposite

theorem not_locallyTomographic_paddedBall3 : ¬ LocallyTomographic paddedBall3 :=
  not_locallyTomographic_paddedPre _ ball3MinComposite_nonempty

theorem no_composite_over_paddedBall3 :
    ¬ ∃ C : Composite ball3 ball3 (Carrier 3 3 × ℝ), C.toPreComposite = paddedBall3 :=
  no_composite_over_paddedPre _ ball3MinComposite_nonempty

end PaddedInstance

/-! ### The verdict -/

open Model in
/-- Round COMP-1, together: the laws L1–L11 for every composite, the three instances, and the padding
control. -/
theorem comp1_core :
    (∀ (dA dB : ℕ) (V : Type) [NormedAddCommGroup V] [NormedSpace ℝ V] (D : ProductData dA dB V)
      (x : Fin dA → ℝ) (y : Fin dB → ℝ), D.margA (D.prodState x y) = x) ∧
    (∀ (dA dB : ℕ) (V : Type) [NormedAddCommGroup V] [NormedSpace ℝ V] (D : ProductData dA dB V)
      (r₀ : Fin dB → ℝ) (x : Fin dA → ℝ), D.margA (D.attach r₀ x) = x) ∧
    (∀ (dA dB : ℕ) (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)
      [NormedAddCommGroup V] [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V), ∀ ω ∈ P.Ω,
      ∀ e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ, e (P.margA ω) = P.prodEff e (unitEff dB) ω) ∧
    (∀ (dA dB : ℕ) (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)
      [NormedAddCommGroup V] [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V),
      IsCompact ΩA → Convex ℝ ΩA → ∀ ω ∈ P.Ω, P.margA ω ∈ ΩA) ∧
    (∀ (dA dB : ℕ) (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)
      [NormedAddCommGroup V] [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V)
      (R : PreComposite.SharpReadout ΩB), ∀ ω ∈ P.Ω,
      P.readout R.f 0 ω + P.readout R.f 1 ω = 1 ∧ IsEffectOn P.Ω (P.readout R.f 0) ∧
        IsEffectOn P.Ω (P.readout R.f 1)) ∧
    (∀ (dA dB : ℕ) (V : Type) [NormedAddCommGroup V] [NormedSpace ℝ V] (D : ProductData dA dB V)
      (f : Fin 2 → (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (k : Fin 2) (x : Fin dA → ℝ) (y : Fin dB → ℝ),
      D.readout f k (D.prodState x y) = f k y) ∧
    (∀ (dA dB : ℕ) (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)
      [NormedAddCommGroup V] [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V)
      (R : PreComposite.SharpReadout ΩB) (k : Fin 2) (x : Fin dA → ℝ),
      P.readout R.f k (P.attach (R.y k) x) = 1) ∧
    (∀ (dA dB : ℕ) (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)
      [NormedAddCommGroup V] [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V),
      IsCompact ΩA → Convex ℝ ΩA → ∀ f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ, IsEffectOn ΩB f →
      ∀ ω ∈ P.Ω, P.prodEff (unitEff dA) f ω ≠ 0 → P.condA f ω ∈ ΩA) ∧
    (∀ (dA dB : ℕ) (V : Type) [NormedAddCommGroup V] [NormedSpace ℝ V] (D : ProductData dA dB V)
      (f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ) (y : Fin dB → ℝ), f y ≠ 0 →
      ∀ x : Fin dA → ℝ, D.condA f (D.prodState x y) = x) ∧
    (∀ (dA dB : ℕ) (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)
      [NormedAddCommGroup V] [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V)
      (G : Set (V ≃ᵃ[ℝ] V)), P.JointReversible G → P.JointReversible (words G)) ∧
    (∀ (dA dB : ℕ) (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)
      [NormedAddCommGroup V] [NormedSpace ℝ V] (P : PreComposite ΩA ΩB V),
      P.toProductData.minBody ΩA ΩB ⊆ P.Ω ∧ P.Ω ⊆ P.toProductData.maxBody ΩA ΩB) ∧
    (∀ (dA dB : ℕ) (ΩA : Set (Fin dA → ℝ)) (ΩB : Set (Fin dB → ℝ)) (V : Type)
      [NormedAddCommGroup V] [NormedSpace ℝ V] (C : Composite ΩA ΩB V),
      Function.Injective fun ω : C.Ω =>
        fun (e : {e : (Fin dA → ℝ) →ᵃ[ℝ] ℝ // IsEffectOn ΩA e})
          (f : {f : (Fin dB → ℝ) →ᵃ[ℝ] ℝ // IsEffectOn ΩB f}) => C.prodEff e.1 f.1 ω.1) ∧
    Nonempty (Composite (simplex 2) (simplex 2) (Carrier 2 2)) ∧
    Nonempty (Composite ball3 ball3 (Carrier 3 3)) ∧
    ball3MinComposite.Ω ⊆ ball3MaxComposite.Ω ∧
    ¬ LocallyTomographic paddedBall3 ∧
    ¬ ∃ C : Composite ball3 ball3 (Carrier 3 3 × ℝ), C.toPreComposite = paddedBall3 :=
  ⟨fun _ _ _ _ _ D x y => D.margA_prodState x y,
    fun _ _ _ _ _ D r₀ x => D.margA_attach r₀ x,
    fun _ _ _ _ _ _ _ P ω hω e => P.eff_margA hω e,
    fun _ _ _ _ _ _ _ P hc hconv ω hω => P.margA_mem hc hconv hω,
    fun _ _ _ _ _ _ _ P R ω hω =>
      ⟨P.readout_sum R hω, P.isEffectOn_readout R.f R.pd.2.1 0, P.isEffectOn_readout R.f R.pd.2.1 1⟩,
    fun _ _ _ _ _ D f k x y => D.readout_prodState f k x y,
    fun _ _ _ _ _ _ _ P R k x => P.readout_attach R k x,
    fun _ _ _ _ _ _ _ P hc hconv f hf ω hω hne => P.condA_mem hc hconv hf hω hne,
    fun _ _ _ _ _ D f y hy x => D.condA_prodState f hy x,
    fun _ _ _ _ _ _ _ P _ hG => P.jointReversible_words hG,
    fun _ _ _ _ _ _ _ P => ⟨P.minBody_subset, P.subset_maxBody⟩,
    fun _ _ _ _ _ _ _ C => C.pairing_injective,
    ⟨bitComposite⟩, ⟨ball3MinComposite⟩, ball3Min_subset_ball3Max,
    not_locallyTomographic_paddedBall3, no_composite_over_paddedBall3⟩

end CompositeInterface
end OIBridge

#print axioms OIBridge.CompositeInterface.isEffectOn_unitEff
#print axioms OIBridge.CompositeInterface.isEffectOn_unitEff_sub
#print axioms OIBridge.CompositeInterface.affine_sum_apply
#print axioms OIBridge.CompositeInterface.affine_eval
#print axioms OIBridge.CompositeInterface.affine_expand
#print axioms OIBridge.CompositeInterface.boundedAffine_of_isCompact
#print axioms OIBridge.CompositeInterface.exists_effect_rescale
#print axioms OIBridge.CompositeInterface.exists_effect_neg
#print axioms OIBridge.CompositeInterface.ProductData.attach_combo
#print axioms OIBridge.CompositeInterface.ProductData.margA_combo
#print axioms OIBridge.CompositeInterface.ProductData.prodEff_expand
#print axioms OIBridge.CompositeInterface.ProductData.margA_prodState
#print axioms OIBridge.CompositeInterface.ProductData.margA_attach
#print axioms OIBridge.CompositeInterface.ProductData.readout_prodState
#print axioms OIBridge.CompositeInterface.ProductData.eff_condA
#print axioms OIBridge.CompositeInterface.ProductData.condA_prodState
#print axioms OIBridge.CompositeInterface.ProductData.prodEff_eq_of_eff_eq
#print axioms OIBridge.CompositeInterface.PreComposite.nonempty_of
#print axioms OIBridge.CompositeInterface.PreComposite.eff_margA
#print axioms OIBridge.CompositeInterface.PreComposite.margA_mem
#print axioms OIBridge.CompositeInterface.PreComposite.sum_eq_unitEff_of_affineSpan
#print axioms OIBridge.CompositeInterface.PreComposite.readout_sum
#print axioms OIBridge.CompositeInterface.PreComposite.isEffectOn_readout
#print axioms OIBridge.CompositeInterface.PreComposite.readout_attach
#print axioms OIBridge.CompositeInterface.PreComposite.condA_mem
#print axioms OIBridge.CompositeInterface.PreComposite.jointReversible_words
#print axioms OIBridge.CompositeInterface.PreComposite.isEffectOn_readout_seedTransport
#print axioms OIBridge.CompositeInterface.PreComposite.minBody_subset
#print axioms OIBridge.CompositeInterface.PreComposite.subset_maxBody
#print axioms OIBridge.CompositeInterface.Composite.pairing_injective
#print axioms OIBridge.CompositeInterface.ProductData.isEffectOn_minBody
#print axioms OIBridge.CompositeInterface.ProductData.unit_eq_one_minBody
#print axioms OIBridge.CompositeInterface.ProductData.maxBody_convex
#print axioms OIBridge.CompositeInterface.ProductData.isEffectOn_maxBody
#print axioms OIBridge.CompositeInterface.Model.hom_zero
#print axioms OIBridge.CompositeInterface.Model.hom_succ
#print axioms OIBridge.CompositeInterface.Model.hom_combo
#print axioms OIBridge.CompositeInterface.Model.coeff_zero
#print axioms OIBridge.CompositeInterface.Model.coeff_succ
#print axioms OIBridge.CompositeInterface.Model.sum_coeff_hom
#print axioms OIBridge.CompositeInterface.Model.coeff_add
#print axioms OIBridge.CompositeInterface.Model.coeff_smul
#print axioms OIBridge.CompositeInterface.Model.pEff_apply
#print axioms OIBridge.CompositeInterface.Model.pEff_pState
#print axioms OIBridge.CompositeInterface.Model.pEff_add_left
#print axioms OIBridge.CompositeInterface.Model.pEff_smul_left
#print axioms OIBridge.CompositeInterface.Model.pEff_add_right
#print axioms OIBridge.CompositeInterface.Model.pEff_smul_right
#print axioms OIBridge.CompositeInterface.Model.modelData_prodEff
#print axioms OIBridge.CompositeInterface.Model.coeff_basisEff
#print axioms OIBridge.CompositeInterface.Model.pEff_basisEff
#print axioms OIBridge.CompositeInterface.Model.modelData_ext
#print axioms OIBridge.CompositeInterface.simplex_isCompact
#print axioms OIBridge.CompositeInterface.zero_mem_ball3
#print axioms OIBridge.CompositeInterface.vec10_mem_simplex
#print axioms OIBridge.CompositeInterface.bitComposite_nonempty
#print axioms OIBridge.CompositeInterface.ball3MinComposite_nonempty
#print axioms OIBridge.CompositeInterface.ball3Min_subset_ball3Max
#print axioms OIBridge.CompositeInterface.padEff_apply
#print axioms OIBridge.CompositeInterface.not_locallyTomographic_paddedPre
#print axioms OIBridge.CompositeInterface.no_composite_over_paddedPre
#print axioms OIBridge.CompositeInterface.not_locallyTomographic_paddedBall3
#print axioms OIBridge.CompositeInterface.no_composite_over_paddedBall3
#print axioms OIBridge.CompositeInterface.comp1_core
