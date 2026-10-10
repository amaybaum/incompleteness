/-
  OIBridge/BridgeLemma.lean — design module of the research thread `research/bridge` (node B6).
  Not certified. Built on the disposable branch `dev-bridge/b11-lemma` only; not for merge.

  The H→P bridge lemma (Theorem B1.1 of the thread's NOTES-B1 §2) at the table level of DIM-1's
  pair carrier `W 3`.

  A finite hidden pair model consists of hidden vectors `Λ → ℝ`, a linear pair readout
  `R : (Λ → ℝ) →ₗ[ℝ] W 3`, a set `𝒫` of hidden vectors (the hidden distributions the pair can be
  in) and a linear hidden map `P`; the pushforward `hpush π` along a hidden bijection `π` is one.
  The hidden composite cone `hiddenCone R 𝒫` is the set of rays through `R '' 𝒫`.

  Proved here:
    §A  the two local actions as linear maps of the carrier (`actCLin`, `actTLin`) and the control
        action on product states (`actC_prodState`; the target action is K2Guard's
        `actT_prodState`);
    §B  the intertwining lemma (`intertwine_of_respect`): for linear `R`, `P`, `T`, a submodule `D`
        of hidden vectors and a set `G` spanning `W 3`, if `P` respects the readout on `D`
        (`R ν = 0 → R (P ν) = 0` for `ν ∈ D`) and each element of `G` is realized in `D` by a
        hidden vector whose image under `P` reads out as `T` of it, then `R ∘ P = T ∘ R` on `D`;
    §C  local tomography of the carrier from one-token spanning: if the homogenized points of a set
        `X` of token points span `HVec 3`, the product states over `X` span `W 3`
        (`span_prodSetOf`); the four points `0, e_x, e_y, e_z` suffice (`span_hom_of_frame`), so
        the product states of the ball span `W 3` (`span_productSet`);
    §D  Theorem B1.1 in two forms.
        `bH_respect`: RESPECT in readout-kernel form on all hidden vectors, product behaviour (P)
        on the products of a set `X` of token points with spanning homogenized points, and
        availability in context (A) give `R ∘ P = actC O ∘ R` and `actC O` maps the hidden
        composite cone into itself; `bH_respect_target` is the same for `actT O`; `bH_perm` is the
        form for a readout-respecting hidden bijection.
        `bH_convex`: the statement of NOTES-B1 §2, with RESPECT assumed only on `𝒫` (convex, with
        normalized readout), product behaviour on the realized products of the ball, and (A):
        the same conclusions on `𝒫`. The readout-kernel form on the span of `𝒫` is derived
        (`respect_diff`, through the differences of two rays `diffSub`).
    §E  controls. A finite hidden pair model with product registers `Fin 4 × Fin 4`, local readout
        and the hidden bijection `tokPerm × id` (`ctlR`, `ctlPerm`) satisfies every hypothesis of
        `bH_perm` for the linear part `cycEquiv` of the kernel's `cyc3`, on the probability
        simplex (`ctl_bH`, positive control). With `𝒫` the single point mass at `(e_x, 0)`, the
        same model keeps RESPECT and product behaviour, (A) fails, and `actC cycEquiv` moves the
        hidden cone (`ctl_counter`, countercontrol: (A) is not redundant).

  Every hypothesis is a premise. Nothing here sources (A), a cone, or a local action on a pair. The
  conclusion is the composite action for the token operation `O` relative to the hidden pair
  model; it relocates the local-action clause to the hidden premise (A) and discharges no
  obligation.

  Kernel check (dev branch):  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.K2Guard
import Mathlib.Analysis.Convex.Basic
import Mathlib.Tactic.Abel
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

namespace OIBridge
namespace BridgeLemma

open KInfFoundations TransitiveBody CompositeDimension K2Guard

/-! ### §A — the two local actions as linear maps of the carrier -/

/-- `N` acting on the control index, as a linear map of the carrier. -/
def actCLin {d : ℕ} (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) : W d →ₗ[ℝ] W d where
  toFun := actC N
  map_add' ω ω' := by
    funext μ ν
    first
      | exact congrFun (map_add (homMap N) (fun κ => ω κ ν) (fun κ => ω' κ ν)) μ
      | (simp only [actC_apply, Pi.add_apply];
          rw [show (fun κ => ω κ ν + ω' κ ν) = (fun κ => ω κ ν) + (fun κ => ω' κ ν) from rfl,
            map_add, Pi.add_apply])
  map_smul' c ω := by
    funext μ ν
    first
      | exact congrFun (map_smul (homMap N) c (fun κ => ω κ ν)) μ
      | (simp only [actC_apply, Pi.smul_apply, smul_eq_mul, RingHom.id_apply];
          rw [show (fun κ => c * ω κ ν) = c • (fun κ => ω κ ν) from rfl, map_smul,
            Pi.smul_apply, smul_eq_mul])

theorem actCLin_apply {d : ℕ} (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) :
    actCLin N ω = actC N ω := rfl

/-- `N` acting on the target index, as a linear map of the carrier. -/
def actTLin {d : ℕ} (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) : W d →ₗ[ℝ] W d where
  toFun := actT N
  map_add' ω ω' := by
    funext μ
    first
      | exact map_add (homMap N) (ω μ) (ω' μ)
      | (show homMap N (ω μ + ω' μ) = homMap N (ω μ) + homMap N (ω' μ); exact map_add _ _ _)
  map_smul' c ω := by
    funext μ
    first
      | exact map_smul (homMap N) c (ω μ)
      | (simp only [RingHom.id_apply]; exact map_smul (homMap N) c (ω μ))

theorem actTLin_apply {d : ℕ} (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (ω : W d) :
    actTLin N ω = actT N ω := rfl

/-- A local linear map of the first copy carries a product state to a product state. -/
theorem actC_prodState {d : ℕ} (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (x y : Fin d → ℝ) :
    actC N (prodState x y) = prodState (N x) y := by
  show actC N (tens (hom x) (hom y)) = tens (hom (N x)) (hom y)
  rw [actC_tens, homMap_hom]

/-! ### §B — the intertwining lemma -/

section Generic

variable {V : Type*} [AddCommGroup V] [Module ℝ V]

/-- The pair vectors realized by a hidden vector of `D` whose image under `P` reads out as `T` of
the pair vector. A submodule of `W 3`. -/
def lawSub (R : V →ₗ[ℝ] W 3) (P : V →ₗ[ℝ] V) (T : W 3 →ₗ[ℝ] W 3) (D : Submodule ℝ V) :
    Submodule ℝ (W 3) where
  carrier := {ω | ∃ μ ∈ D, R μ = ω ∧ R (P μ) = T ω}
  add_mem' := by
    rintro _ _ ⟨μ, hμ, rfl, h⟩ ⟨ν, hν, rfl, h'⟩
    refine ⟨μ + ν, D.add_mem hμ hν, map_add R μ ν, ?_⟩
    rw [map_add P, map_add R, h, h', map_add T]
  zero_mem' := ⟨0, D.zero_mem, map_zero R, by rw [map_zero P, map_zero R, map_zero T]⟩
  smul_mem' := by
    rintro c _ ⟨μ, hμ, rfl, h⟩
    refine ⟨c • μ, D.smul_mem c hμ, map_smul R c μ, ?_⟩
    rw [map_smul P, map_smul R, h, map_smul T]

theorem mem_lawSub {R : V →ₗ[ℝ] W 3} {P : V →ₗ[ℝ] V} {T : W 3 →ₗ[ℝ] W 3} {D : Submodule ℝ V}
    {ω : W 3} : ω ∈ lawSub R P T D ↔ ∃ μ ∈ D, R μ = ω ∧ R (P μ) = T ω := Iff.rfl

/-- **The intertwining lemma.** If `G` spans the carrier, `P` respects the readout on `D`, and each
element of `G` is realized in `D` by a hidden vector whose image reads out as `T` of it, then the
readout intertwines `P` with `T` on `D`. -/
theorem intertwine_of_respect (R : V →ₗ[ℝ] W 3) (P : V →ₗ[ℝ] V) (T : W 3 →ₗ[ℝ] W 3)
    (D : Submodule ℝ V) (G : Set (W 3)) (hG : Submodule.span ℝ G = ⊤)
    (hW : ∀ ν ∈ D, R ν = 0 → R (P ν) = 0)
    (hreal : ∀ g ∈ G, ∃ μ ∈ D, R μ = g ∧ R (P μ) = T g) :
    ∀ μ ∈ D, R (P μ) = T (R μ) := by
  have hle : Submodule.span ℝ G ≤ lawSub R P T D :=
    Submodule.span_le.mpr fun g hg => mem_lawSub.mpr (hreal g hg)
  rw [hG] at hle
  intro μ hμ
  have hmem : R μ ∈ lawSub R P T D := hle Submodule.mem_top
  obtain ⟨μ', hμ', h1, h2⟩ := mem_lawSub.mp hmem
  have hk : R (μ - μ') = 0 := by rw [map_sub, h1, sub_self]
  have h3 := hW (μ - μ') (D.sub_mem hμ hμ') hk
  rw [map_sub, map_sub, sub_eq_zero] at h3
  rw [h3, h2]

end Generic

/-! ### §C — local tomography of the carrier from one-token spanning -/

/-- The product states of two copies of a set `X` of token points. -/
def prodSetOf (X : Set (Fin 3 → ℝ)) : Set (W 3) :=
  {ω | ∃ x ∈ X, ∃ y ∈ X, ω = prodState x y}

theorem prodSetOf_eball : prodSetOf (eball 3) = productSet := rfl

/-- Elementary tensors lie in the span of the products of `X` when the homogenized points of `X`
span `HVec 3`. -/
theorem tens_mem_span_prodSetOf {X : Set (Fin 3 → ℝ)} (hX : Submodule.span ℝ (hom '' X) = ⊤)
    (A B : HVec 3) : tens A B ∈ Submodule.span ℝ (prodSetOf X) := by
  have h1 : ∀ x ∈ X, ∀ B : HVec 3, tens (hom x) B ∈ Submodule.span ℝ (prodSetOf X) := by
    intro x hx B
    have hle : Submodule.span ℝ (hom '' X) ≤
        (Submodule.span ℝ (prodSetOf X)).comap (tensL (hom x)) := by
      rw [Submodule.span_le]
      rintro _ ⟨y, hy, rfl⟩
      rw [SetLike.mem_coe, Submodule.mem_comap]
      exact Submodule.subset_span
        ⟨x, hx, y, hy, (tensL_apply (hom x) (hom y)).trans (prodState_eq_tens x y).symm⟩
    have hB : B ∈ Submodule.span ℝ (hom '' X) := by rw [hX]; exact Submodule.mem_top
    have h := Submodule.mem_comap.mp (hle hB)
    rwa [tensL_apply] at h
  have hle : Submodule.span ℝ (hom '' X) ≤ (Submodule.span ℝ (prodSetOf X)).comap (tensR B) := by
    rw [Submodule.span_le]
    rintro _ ⟨x, hx, rfl⟩
    rw [SetLike.mem_coe, Submodule.mem_comap, tensR_apply]
    exact h1 x hx B
  have hA : A ∈ Submodule.span ℝ (hom '' X) := by rw [hX]; exact Submodule.mem_top
  have h := Submodule.mem_comap.mp (hle hA)
  rwa [tensR_apply] at h

/-- **Local tomography from one-token spanning.** If the homogenized points of `X` span `HVec 3`,
the product states over `X` span the carrier `W 3`. -/
theorem span_prodSetOf {X : Set (Fin 3 → ℝ)} (hX : Submodule.span ℝ (hom '' X) = ⊤) :
    Submodule.span ℝ (prodSetOf X) = ⊤ := by
  rw [Submodule.eq_top_iff']
  intro ω
  have hω : ω = tens (![1, 0, 0, 0] : HVec 3) (ω 0) + tens (![0, 1, 0, 0] : HVec 3) (ω 1)
      + tens (![0, 0, 1, 0] : HVec 3) (ω 2) + tens (![0, 0, 0, 1] : HVec 3) (ω 3) := by
    funext μ ν
    fin_cases μ <;>
      first
        | (simp [tens_apply]; done)
        | (simp +decide [tens_apply]; done)
        | norm_num [tens_apply]
  rw [hω]
  exact Submodule.add_mem _ (Submodule.add_mem _ (Submodule.add_mem _
    (tens_mem_span_prodSetOf hX _ _) (tens_mem_span_prodSetOf hX _ _))
    (tens_mem_span_prodSetOf hX _ _)) (tens_mem_span_prodSetOf hX _ _)

/-- The token point `e_y`. -/
def yplus : Fin 3 → ℝ := ![0, 1, 0]

theorem yplus_mem : yplus ∈ eball 3 := by
  rw [mem_eball, Fin.sum_univ_three]; simp [yplus]

theorem zero_mem_eball3 : (0 : Fin 3 → ℝ) ∈ eball 3 := by
  rw [mem_eball]; simp

/-- One-token spanning from the frame: if `X` contains `0, e_x, e_y, e_z`, the homogenized points of
`X` span `HVec 3`. -/
theorem span_hom_of_frame {X : Set (Fin 3 → ℝ)} (h0 : (0 : Fin 3 → ℝ) ∈ X) (h1 : xplus ∈ X)
    (h2 : yplus ∈ X) (h3 : z3 ∈ X) : Submodule.span ℝ (hom '' X) = ⊤ := by
  rw [Submodule.eq_top_iff']
  intro v
  have hv : v = v 0 • hom (0 : Fin 3 → ℝ) + v 1 • (hom xplus - hom (0 : Fin 3 → ℝ))
      + v 2 • (hom yplus - hom (0 : Fin 3 → ℝ)) + v 3 • (hom z3 - hom (0 : Fin 3 → ℝ)) := by
    funext i
    fin_cases i <;>
      first
        | (simp [xplus, yplus, z3]; done)
        | (simp [hom, xplus, yplus, z3]; done)
        | norm_num [hom, xplus, yplus, z3]
  have m : ∀ x ∈ X, hom x ∈ Submodule.span ℝ (hom '' X) := fun x hx =>
    Submodule.subset_span ⟨x, hx, rfl⟩
  rw [hv]
  exact Submodule.add_mem _ (Submodule.add_mem _ (Submodule.add_mem _
    (Submodule.smul_mem _ _ (m _ h0))
    (Submodule.smul_mem _ _ (Submodule.sub_mem _ (m _ h1) (m _ h0))))
    (Submodule.smul_mem _ _ (Submodule.sub_mem _ (m _ h2) (m _ h0))))
    (Submodule.smul_mem _ _ (Submodule.sub_mem _ (m _ h3) (m _ h0)))

/-- The product states of the ball span the carrier `W 3`. -/
theorem span_productSet : Submodule.span ℝ productSet = ⊤ := by
  rw [← prodSetOf_eball]
  exact span_prodSetOf (span_hom_of_frame zero_mem_eball3 xplus_mem yplus_mem z3_mem)

/-! ### §D — Theorem B1.1 -/

section Hidden

variable {Λ : Type*}

/-- The pushforward of hidden vectors along a hidden bijection. -/
def hpush (π : Equiv.Perm Λ) : (Λ → ℝ) →ₗ[ℝ] (Λ → ℝ) where
  toFun μ := fun l => μ (π.symm l)
  map_add' μ ν := rfl
  map_smul' c μ := by
    first
      | rfl
      | (funext l; simp)

theorem hpush_apply (π : Equiv.Perm Λ) (μ : Λ → ℝ) (l : Λ) : hpush π μ l = μ (π.symm l) := rfl

/-- The hidden composite cone: the rays through the realized pair states. -/
def hiddenCone (R : (Λ → ℝ) →ₗ[ℝ] W 3) (𝒫 : Set (Λ → ℝ)) : Set (W 3) :=
  {ω | ∃ c : ℝ, 0 ≤ c ∧ ∃ μ ∈ 𝒫, ω = c • R μ}

/-- A linear map of the carrier intertwined with the hidden map on an invariant set of hidden
vectors maps the hidden composite cone into itself. -/
theorem hiddenCone_mapsTo (R : (Λ → ℝ) →ₗ[ℝ] W 3) (P : (Λ → ℝ) →ₗ[ℝ] (Λ → ℝ))
    (𝒫 : Set (Λ → ℝ)) (T : W 3 →ₗ[ℝ] W 3) (hA : ∀ μ ∈ 𝒫, P μ ∈ 𝒫)
    (hint : ∀ μ ∈ 𝒫, R (P μ) = T (R μ)) :
    ∀ ω ∈ hiddenCone R 𝒫, T ω ∈ hiddenCone R 𝒫 := by
  rintro _ ⟨c, hc, μ, hμ, rfl⟩
  exact ⟨c, hc, P μ, hA μ hμ, by rw [map_smul, hint μ hμ]⟩

/-- **Theorem B1.1, readout-kernel form (control token).** RESPECT on all hidden vectors, product
behaviour on the products of a set `X` of token points whose homogenized points span `HVec 3`, and
availability in context (A): the readout intertwines `P` with `actC O`, and `actC O` maps the
hidden composite cone into itself. -/
theorem bH_respect {X : Set (Fin 3 → ℝ)} (hX : Submodule.span ℝ (hom '' X) = ⊤)
    (R : (Λ → ℝ) →ₗ[ℝ] W 3) (P : (Λ → ℝ) →ₗ[ℝ] (Λ → ℝ)) (𝒫 : Set (Λ → ℝ))
    (O : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))
    (hW : ∀ ν, R ν = 0 → R (P ν) = 0)
    (hP : ∀ x ∈ X, ∀ y ∈ X, ∃ μ, R μ = prodState x y ∧ R (P μ) = prodState (O x) y)
    (hA : ∀ μ ∈ 𝒫, P μ ∈ 𝒫) :
    (∀ μ, R (P μ) = actC O (R μ)) ∧ ∀ ω ∈ hiddenCone R 𝒫, actC O ω ∈ hiddenCone R 𝒫 := by
  have hint : ∀ μ ∈ (⊤ : Submodule ℝ (Λ → ℝ)), R (P μ) = actCLin O (R μ) := by
    refine intertwine_of_respect R P (actCLin O) ⊤ (prodSetOf X) (span_prodSetOf hX)
      (fun ν _ h0 => hW ν h0) ?_
    rintro _ ⟨x, hx, y, hy, rfl⟩
    obtain ⟨μ, h1, h2⟩ := hP x hx y hy
    exact ⟨μ, Submodule.mem_top, h1, by rw [h2, actCLin_apply, actC_prodState]⟩
  exact ⟨fun μ => hint μ Submodule.mem_top,
    hiddenCone_mapsTo R P 𝒫 (actCLin O) hA (fun μ _ => hint μ Submodule.mem_top)⟩

/-- **Theorem B1.1, readout-kernel form (target token).** -/
theorem bH_respect_target {X : Set (Fin 3 → ℝ)} (hX : Submodule.span ℝ (hom '' X) = ⊤)
    (R : (Λ → ℝ) →ₗ[ℝ] W 3) (P : (Λ → ℝ) →ₗ[ℝ] (Λ → ℝ)) (𝒫 : Set (Λ → ℝ))
    (O : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))
    (hW : ∀ ν, R ν = 0 → R (P ν) = 0)
    (hP : ∀ x ∈ X, ∀ y ∈ X, ∃ μ, R μ = prodState x y ∧ R (P μ) = prodState x (O y))
    (hA : ∀ μ ∈ 𝒫, P μ ∈ 𝒫) :
    (∀ μ, R (P μ) = actT O (R μ)) ∧ ∀ ω ∈ hiddenCone R 𝒫, actT O ω ∈ hiddenCone R 𝒫 := by
  have hint : ∀ μ ∈ (⊤ : Submodule ℝ (Λ → ℝ)), R (P μ) = actTLin O (R μ) := by
    refine intertwine_of_respect R P (actTLin O) ⊤ (prodSetOf X) (span_prodSetOf hX)
      (fun ν _ h0 => hW ν h0) ?_
    rintro _ ⟨x, hx, y, hy, rfl⟩
    obtain ⟨μ, h1, h2⟩ := hP x hx y hy
    exact ⟨μ, Submodule.mem_top, h1, by rw [h2, actTLin_apply, actT_prodState]⟩
  exact ⟨fun μ => hint μ Submodule.mem_top,
    hiddenCone_mapsTo R P 𝒫 (actTLin O) hA (fun μ _ => hint μ Submodule.mem_top)⟩

/-- **Theorem B1.1 for a readout-respecting hidden bijection.** -/
theorem bH_perm {X : Set (Fin 3 → ℝ)} (hX : Submodule.span ℝ (hom '' X) = ⊤)
    (R : (Λ → ℝ) →ₗ[ℝ] W 3) (π : Equiv.Perm Λ) (𝒫 : Set (Λ → ℝ))
    (O : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ))
    (hW : ∀ ν, R ν = 0 → R (hpush π ν) = 0)
    (hP : ∀ x ∈ X, ∀ y ∈ X, ∃ μ, R μ = prodState x y ∧ R (hpush π μ) = prodState (O x) y)
    (hA : ∀ μ ∈ 𝒫, hpush π μ ∈ 𝒫) :
    (∀ μ, R (hpush π μ) = actC O (R μ)) ∧
      ∀ ω ∈ hiddenCone R 𝒫, actC O ω ∈ hiddenCone R 𝒫 :=
  bH_respect hX R (hpush π) 𝒫 O hW hP hA

/-- Two rays through a convex set add to a ray through it. -/
theorem ray_add {𝒫 : Set (Λ → ℝ)} (hconv : Convex ℝ 𝒫) {a a' : ℝ} (ha : 0 ≤ a) (ha' : 0 ≤ a')
    {μ μ' : Λ → ℝ} (hμ : μ ∈ 𝒫) (hμ' : μ' ∈ 𝒫) :
    ∃ A : ℝ, 0 ≤ A ∧ ∃ m ∈ 𝒫, a • μ + a' • μ' = A • m := by
  rcases eq_or_lt_of_le (add_nonneg ha ha') with h | h
  · have h1 : a = 0 := by linarith
    have h2 : a' = 0 := by linarith
    exact ⟨0, le_refl 0, μ, hμ, by simp only [h1, h2, zero_smul, add_zero]⟩
  · have hne : a + a' ≠ 0 := h.ne'
    refine ⟨a + a', h.le, (a / (a + a')) • μ + (a' / (a + a')) • μ',
      hconv hμ hμ' (div_nonneg ha h.le) (div_nonneg ha' h.le) ?_, ?_⟩
    · rw [← add_div, div_self hne]
    · rw [smul_add, smul_smul, smul_smul, mul_div_cancel₀ a hne, mul_div_cancel₀ a' hne]

/-- The differences of two rays through a convex nonempty set `𝒫`: a submodule of hidden vectors
containing `𝒫`. -/
def diffSub (𝒫 : Set (Λ → ℝ)) (hconv : Convex ℝ 𝒫) (hne : 𝒫.Nonempty) :
    Submodule ℝ (Λ → ℝ) where
  carrier := {ν | ∃ a b : ℝ, 0 ≤ a ∧ 0 ≤ b ∧ ∃ μ₁ ∈ 𝒫, ∃ μ₂ ∈ 𝒫, ν = a • μ₁ - b • μ₂}
  add_mem' := by
    rintro _ _ ⟨a₁, b₁, ha₁, hb₁, μ₁, hμ₁, μ₂, hμ₂, rfl⟩
      ⟨a₂, b₂, ha₂, hb₂, μ₃, hμ₃, μ₄, hμ₄, rfl⟩
    obtain ⟨A, hA, m, hm, hAm⟩ := ray_add hconv ha₁ ha₂ hμ₁ hμ₃
    obtain ⟨B, hB, m', hm', hBm⟩ := ray_add hconv hb₁ hb₂ hμ₂ hμ₄
    refine ⟨A, B, hA, hB, m, hm, m', hm', ?_⟩
    rw [← hAm, ← hBm]
    abel
  zero_mem' := by
    obtain ⟨μ, hμ⟩ := hne
    exact ⟨0, 0, le_refl 0, le_refl 0, μ, hμ, μ, hμ, by rw [zero_smul, sub_zero]⟩
  smul_mem' := by
    rintro c _ ⟨a, b, ha, hb, μ₁, hμ₁, μ₂, hμ₂, rfl⟩
    rcases le_total 0 c with hc | hc
    · exact ⟨c * a, c * b, mul_nonneg hc ha, mul_nonneg hc hb, μ₁, hμ₁, μ₂, hμ₂,
        by rw [smul_sub, smul_smul, smul_smul]⟩
    · refine ⟨-c * b, -c * a, mul_nonneg (neg_nonneg.mpr hc) hb,
        mul_nonneg (neg_nonneg.mpr hc) ha, μ₂, hμ₂, μ₁, hμ₁, ?_⟩
      rw [smul_sub, smul_smul, smul_smul, neg_mul, neg_mul, neg_smul, neg_smul]
      abel

/-- RESPECT on a convex set with normalized readout gives RESPECT in readout-kernel form on the
differences of rays through it. -/
theorem respect_diff (R : (Λ → ℝ) →ₗ[ℝ] W 3) (P : (Λ → ℝ) →ₗ[ℝ] (Λ → ℝ)) (𝒫 : Set (Λ → ℝ))
    {hconv : Convex ℝ 𝒫} {hne : 𝒫.Nonempty}
    (hnorm : ∀ μ ∈ 𝒫, R μ 0 0 = 1)
    (hW : ∀ μ ∈ 𝒫, ∀ ν ∈ 𝒫, R μ = R ν → R (P μ) = R (P ν))
    {ν : Λ → ℝ} (hν : ν ∈ diffSub 𝒫 hconv hne) (h0 : R ν = 0) : R (P ν) = 0 := by
  obtain ⟨a, b, ha, hb, μ₁, hμ₁, μ₂, hμ₂, rfl⟩ := hν
  have hR : a • R μ₁ = b • R μ₂ := by
    rw [map_sub, map_smul, map_smul, sub_eq_zero] at h0
    exact h0
  have hab : a = b := by
    have h00 := congrFun (congrFun hR 0) 0
    simp only [Pi.smul_apply, smul_eq_mul, hnorm μ₁ hμ₁, hnorm μ₂ hμ₂, mul_one] at h00
    exact h00
  subst hab
  rcases eq_or_lt_of_le ha with h | h
  · simp only [← h, zero_smul, sub_zero, map_zero]
  · have hR' : R μ₁ = R μ₂ := smul_right_injective (W 3) h.ne' hR
    first
      | (simp only [map_sub, map_smul]; rw [hW μ₁ hμ₁ μ₂ hμ₂ hR', sub_self])
      | (rw [map_sub, map_sub, map_smul, map_smul, map_smul, map_smul, hW μ₁ hμ₁ μ₂ hμ₂ hR',
          sub_self])

/-- **Theorem B1.1 as stated in NOTES-B1 §2.** RESPECT on the convex set `𝒫` of hidden
distributions with normalized readout, the products of the ball realized in `𝒫` (H1) with product
behaviour (P), and availability in context (A): on `𝒫` the readout intertwines `P` with `actC O`,
and `actC O` maps the hidden composite cone into itself. -/
theorem bH_convex (R : (Λ → ℝ) →ₗ[ℝ] W 3) (P : (Λ → ℝ) →ₗ[ℝ] (Λ → ℝ)) (𝒫 : Set (Λ → ℝ))
    (O : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) (hconv : Convex ℝ 𝒫)
    (hnorm : ∀ μ ∈ 𝒫, R μ 0 0 = 1)
    (hW : ∀ μ ∈ 𝒫, ∀ ν ∈ 𝒫, R μ = R ν → R (P μ) = R (P ν))
    (hH1 : ∀ x ∈ eball 3, ∀ y ∈ eball 3, ∃ μ ∈ 𝒫, R μ = prodState x y)
    (hP : ∀ μ ∈ 𝒫, ∀ x ∈ eball 3, ∀ y ∈ eball 3, R μ = prodState x y →
      R (P μ) = prodState (O x) y)
    (hA : ∀ μ ∈ 𝒫, P μ ∈ 𝒫) :
    (∀ μ ∈ 𝒫, R (P μ) = actC O (R μ)) ∧
      ∀ ω ∈ hiddenCone R 𝒫, actC O ω ∈ hiddenCone R 𝒫 := by
  have hne : 𝒫.Nonempty := by
    obtain ⟨μ, hμ, _⟩ := hH1 0 zero_mem_eball3 0 zero_mem_eball3
    exact ⟨μ, hμ⟩
  have hsub : ∀ μ ∈ 𝒫, μ ∈ diffSub 𝒫 hconv hne := fun μ hμ =>
    ⟨1, 0, zero_le_one, le_refl 0, μ, hμ, μ, hμ, by rw [one_smul, zero_smul, sub_zero]⟩
  have hint : ∀ μ ∈ diffSub 𝒫 hconv hne, R (P μ) = actCLin O (R μ) := by
    refine intertwine_of_respect R P (actCLin O) (diffSub 𝒫 hconv hne) (prodSetOf (eball 3))
      (span_prodSetOf (span_hom_of_frame zero_mem_eball3 xplus_mem yplus_mem z3_mem))
      (fun ν hν h0 => respect_diff R P 𝒫 hnorm hW hν h0) ?_
    rintro _ ⟨x, hx, y, hy, rfl⟩
    obtain ⟨μ, hμ, h1⟩ := hH1 x hx y hy
    exact ⟨μ, hsub μ hμ, h1, by rw [hP μ hμ x hx y hy h1, actCLin_apply, actC_prodState]⟩
  exact ⟨fun μ hμ => hint μ (hsub μ hμ),
    hiddenCone_mapsTo R P 𝒫 (actCLin O) hA (fun μ hμ => hint μ (hsub μ hμ))⟩

/-- The probability simplex on the hidden configurations. -/
def hidSimplex (κ : Type*) [Fintype κ] : Set (κ → ℝ) := {μ | (∀ l, 0 ≤ μ l) ∧ ∑ l, μ l = 1}

theorem hpush_hidSimplex {κ : Type*} [Fintype κ] (π : Equiv.Perm κ) {μ : κ → ℝ}
    (hμ : μ ∈ hidSimplex κ) : hpush π μ ∈ hidSimplex κ := by
  refine ⟨fun l => hμ.1 (π.symm l), ?_⟩
  show ∑ l, μ (π.symm l) = 1
  rw [Equiv.sum_comp π.symm μ]
  exact hμ.2

end Hidden

/-! ### §E — controls -/

/-- The four token points `0, e_x, e_y, e_z` of the control model. -/
def tok : Fin 4 → (Fin 3 → ℝ) := ![0, xplus, yplus, z3]

/-- The hidden bijection of the control model's first register: `0` is fixed and
`e_x ↦ e_y ↦ e_z ↦ e_x`. -/
def tokPerm : Equiv.Perm (Fin 4) where
  toFun := ![0, 2, 3, 1]
  invFun := ![0, 3, 1, 2]
  left_inv := by
    intro a
    fin_cases a <;> first | rfl | decide | simp
  right_inv := by
    intro a
    fin_cases a <;> first | rfl | decide | simp

/-- The linear part of the kernel's `cyc3` permutes the token points as `tokPerm` does. -/
theorem cyc_tok (a : Fin 4) : cycEquiv.toLinearMap (tok a) = tok (tokPerm a) := by
  fin_cases a <;> funext i <;> fin_cases i <;>
    first
      | rfl
      | (simp [tok, tokPerm, cycEquiv, xplus, yplus, z3]; done)
      | norm_num [tok, tokPerm, cycEquiv, xplus, yplus, z3]

/-- The control model's pair readout on the hidden registers `Fin 4 × Fin 4`: a hidden vector reads
out as the combination of the products of its token points (product registers, local readout). -/
def ctlR : (Fin 4 × Fin 4 → ℝ) →ₗ[ℝ] W 3 where
  toFun μ := ∑ l, μ l • prodState (tok l.1) (tok l.2)
  map_add' μ ν := by simp only [Pi.add_apply, add_smul, Finset.sum_add_distrib]
  map_smul' c μ := by
    simp only [Pi.smul_apply, smul_eq_mul, mul_smul, RingHom.id_apply, Finset.smul_sum]

/-- The control model's hidden bijection: `tokPerm` on the first register, the identity on the
second. -/
def ctlPerm : Equiv.Perm (Fin 4 × Fin 4) where
  toFun l := (tokPerm l.1, l.2)
  invFun l := (tokPerm.symm l.1, l.2)
  left_inv l := by simp
  right_inv l := by simp

/-- In the control model the readout intertwines the hidden bijection with `actC cycEquiv`. -/
theorem ctl_intertwine (μ : Fin 4 × Fin 4 → ℝ) :
    ctlR (hpush ctlPerm μ) = actC cycEquiv.toLinearMap (ctlR μ) := by
  show ∑ l, μ (ctlPerm.symm l) • prodState (tok l.1) (tok l.2) =
    actCLin cycEquiv.toLinearMap (∑ l, μ l • prodState (tok l.1) (tok l.2))
  rw [map_sum]
  refine Fintype.sum_equiv ctlPerm.symm _ _ (fun l => ?_)
  show μ (ctlPerm.symm l) • prodState (tok l.1) (tok l.2) =
    actCLin cycEquiv.toLinearMap
      (μ (ctlPerm.symm l) • prodState (tok (ctlPerm.symm l).1) (tok (ctlPerm.symm l).2))
  rw [map_smul, actCLin_apply, actC_prodState, cyc_tok]
  show μ (ctlPerm.symm l) • prodState (tok l.1) (tok l.2) =
    μ (ctlPerm.symm l) • prodState (tok (tokPerm (tokPerm.symm l.1))) (tok l.2)
  rw [Equiv.apply_symm_apply]

theorem ctlR_single (a b : Fin 4) :
    ctlR (Pi.single (a, b) 1) = prodState (tok a) (tok b) := by
  show ∑ l, (Pi.single (a, b) (1 : ℝ) : Fin 4 × Fin 4 → ℝ) l • prodState (tok l.1) (tok l.2) = _
  rw [Finset.sum_eq_single (a, b)]
  · simp
  · intro l _ hl
    simp [Pi.single_apply, hl]
  · intro h
    exact absurd (Finset.mem_univ _) h

/-- **Positive control.** The control model satisfies every hypothesis of `bH_perm` for the linear
part of `cyc3`, with `X` the four token points and `𝒫` the probability simplex. -/
theorem ctl_bH :
    (∀ μ, ctlR (hpush ctlPerm μ) = actC cycEquiv.toLinearMap (ctlR μ)) ∧
      ∀ ω ∈ hiddenCone ctlR (hidSimplex (Fin 4 × Fin 4)),
        actC cycEquiv.toLinearMap ω ∈ hiddenCone ctlR (hidSimplex (Fin 4 × Fin 4)) := by
  refine bH_perm (X := Set.range tok)
    (span_hom_of_frame ⟨0, rfl⟩ ⟨1, rfl⟩ ⟨2, rfl⟩ ⟨3, rfl⟩) ctlR ctlPerm
    (hidSimplex (Fin 4 × Fin 4)) cycEquiv.toLinearMap ?_ ?_ ?_
  · intro ν h0
    rw [ctl_intertwine, h0]
    exact map_zero (actCLin cycEquiv.toLinearMap)
  · rintro _ ⟨a, rfl⟩ _ ⟨b, rfl⟩
    exact ⟨Pi.single (a, b) 1, ctlR_single a b,
      by rw [ctl_intertwine, ctlR_single, actC_prodState]⟩
  · intro μ hμ
    exact hpush_hidSimplex ctlPerm hμ

/-- **Countercontrol.** With `𝒫` the single point mass at the product `(e_x, 0)`, the control model
keeps RESPECT and product behaviour (`ctl_bH`) while (A) fails, and `actC cycEquiv` moves the
hidden cone: (A) is not redundant in `bH_respect`. -/
theorem ctl_counter :
    ¬ ∀ ω ∈ hiddenCone ctlR {Pi.single ((1 : Fin 4), (0 : Fin 4)) (1 : ℝ)},
      actC cycEquiv.toLinearMap ω ∈ hiddenCone ctlR {Pi.single ((1 : Fin 4), (0 : Fin 4)) (1 : ℝ)} := by
  intro h
  obtain ⟨c, _, μ, hμ, heq⟩ := h (ctlR (Pi.single ((1 : Fin 4), (0 : Fin 4)) (1 : ℝ)))
    ⟨1, zero_le_one, Pi.single ((1 : Fin 4), (0 : Fin 4)) (1 : ℝ), Set.mem_singleton _,
      (one_smul ℝ _).symm⟩
  rw [Set.mem_singleton_iff] at hμ
  subst hμ
  rw [ctlR_single, actC_prodState, cyc_tok] at heq
  have e1 := congrFun (congrFun heq 0) 0
  have e2 := congrFun (congrFun heq 1) 0
  simp [prodState, tok, tokPerm, xplus, yplus] at e1 e2
  linarith

#print axioms actCLin
#print axioms actTLin
#print axioms intertwine_of_respect
#print axioms span_prodSetOf
#print axioms span_hom_of_frame
#print axioms span_productSet
#print axioms bH_respect
#print axioms bH_respect_target
#print axioms bH_perm
#print axioms respect_diff
#print axioms bH_convex
#print axioms ctl_intertwine
#print axioms ctl_bH
#print axioms ctl_counter

end BridgeLemma
end OIBridge
