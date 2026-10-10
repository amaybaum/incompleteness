# RELC-SELECT-1 design batch — frozen statement census (pre-run-1)

- file `RelcSelectParity.lean` sha256 `6179547ebee49326335adc785e989036ee102e078dc26b8713ee6ac6e4c5077a`; prints 2; sorry False; axiom False
- file `RelcSelectBlock.lean` sha256 `cced762ff0f24486ea88a6c506e030540009b27b4583a7cdecd95e1fc6424760`; prints 5; sorry False; axiom False
- file `RelcSelectSqueeze.lean` sha256 `bbbf278722c78ddb2d3f51747cf856e6b8d1d82a48dd64ce97e5f29ab2f4245b`; prints 19; sorry False; axiom False
- file `RelcSelectC5.lean` sha256 `fdb701eaccfa33266498cda41858924b0b75cfda7b9a6f732a28e3b53aa1f78d`; prints 12; sorry False; axiom False

Total declarations frozen: 167

## Core statements

### `CtrlGate` (structure, sha256 baea2b39857e993c)
```
structure CtrlGate (Ω : Set (Fin d → ℝ)) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d) : Prop where frame : ∀ a b : Fin 2, G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b)) posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, G (prodState x y) ∈ maxCone Ω posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone Ω relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)
```
### `ctrlGate_of_nativeGate` (theorem, sha256 5f2b023aa3cfcda5)
```
theorem ctrlGate_of_nativeGate {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hG : NativeGate Ω z N G) : CtrlGate Ω z N G
```
### `finrank_plus_eq_finrank_minus_relC` (theorem, sha256 52ceeabb6c1b53a2)
```
theorem finrank_plus_eq_finrank_minus_relC {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)) : Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N)
```
### `not_even_of_relC` (theorem, sha256 425bcca583a7bacb)
```
theorem not_even_of_relC {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)) : ¬ Even d
```
### `actT_slice_ctrl` (theorem, sha256 790b24b569f2a923)
```
theorem actT_slice_ctrl {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) {c : Fin d → ℝ} (hc : ∑ j, c j ^ 2 ≤ 1) (hzc : ∑ j, z j * c j = 0) : actT N (G (tens (lift c) (Minv z G (hom 0)))) = G (tens (lift c) (Minv z G (hom 0)))
```
### `blockData_of_ctrlGate` (theorem, sha256 e4aa86a9567251f8)
```
theorem blockData_of_ctrlGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hd : 2 ≤ d) (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) : BlockData (tangentPlus N)
```
### `dim_of_ctrlGate` (theorem, sha256 477ac8923376e832)
```
theorem dim_of_ctrlGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) : d = 1 ∨ d = 3
```
### `three_of_ctrlGate` (theorem, sha256 68819eff0c3866ef)
```
theorem three_of_ctrlGate {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hG : CtrlGate (eball d) z N G) (hE : Entangling (eball d) G) : d = 3
```
### `frame_symm` (theorem, sha256 8abeb02b60319b1b)
```
theorem frame_symm {z : Fin d → ℝ} {G : W d ≃ₗ[ℝ] W d} (hF : ∀ a b : Fin 2, G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))) : ∀ a b : Fin 2, G.symm (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))
```
### `relT_symm` (theorem, sha256 19261b31c1dca91b)
```
theorem relT_symm {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot Ω z N) (hT : ∀ ω, actT N (G (actT N ω)) = G ω) : ∀ ω, actT N (G.symm (actT N ω)) = G.symm ω
```
### `relC_symm` (theorem, sha256 6873a13b0063375f)
```
theorem relC_symm {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot Ω z N) (hT : ∀ ω, actT N (G (actT N ω)) = G ω) (hC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)) : ∀ ω, actC N (G.symm (actC N ω)) = actT N (G.symm ω)
```
### `gateRel_symm` (theorem, sha256 15d8810cef142f6a)
```
theorem gateRel_symm {Ω : Set (Fin d → ℝ)} {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {G : W d ≃ₗ[ℝ] W d} (hN : IsNot Ω z N) (hR : GateRel N G) : GateRel N G.symm
```
### `gSq` (noncomputable def, sha256 75dc83a1bf8653f7)
```
noncomputable def gSq : W 5 ≃ₗ[ℝ] W 5 where toFun := gSqFun invFun := gSqInvFun map_add' ω₁ ω₂ := by funext m n simp only [gSqFun_apply, Pi.add_apply, mul_add] map_smul' c ω := by funext m n simp only [gSqFun_apply, Pi.smul_apply, smul_eq_mul, RingHom.id_apply] ring left_inv := gSqInvFun_gSqFun right_inv := gSqFun_gSqInvFun
```
### `gSq_frame` (theorem, sha256 c59c521ffcedf3e0)
```
theorem gSq_frame (a b : Fin 2) : gSq (prodState (corner z5 a) (corner z5 b)) = prodState (corner z5 a) (corner z5 (a + b))
```
### `gSq_relT` (theorem, sha256 42c8571e585caea5)
```
theorem gSq_relT : ∀ ω, actT n5 (gSq (actT n5 ω)) = gSq ω
```
### `gSq_relC` (theorem, sha256 5a67673cfdb086c2)
```
theorem gSq_relC : ∀ ω, actC n5 (gSq (actC n5 ω)) = actT n5 (gSq ω)
```
### `gSq_posFwd` (theorem, sha256 31a9c13e84d49819)
```
theorem gSq_posFwd : ∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq (prodState x y) ∈ maxCone (eball 5)
```
### `gSq_symm_value` (theorem, sha256 89dc8f78c7d9cff6)
```
theorem gSq_symm_value : prodEffVal (sharpEff z5) (sharpEff (-x5)) (gSq.symm (prodState z5 x5)) = -1 / 2
```
### `gSq_not_posInv` (theorem, sha256 ec4de920091b9187)
```
theorem gSq_not_posInv : ¬ ∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq.symm (prodState x y) ∈ maxCone (eball 5)
```
### `gSq_sep` (theorem, sha256 7131ed1ae76f5a77)
```
theorem gSq_sep : IsNot (eball 5) z5 n5 ∧ (∀ a b : Fin 2, gSq (prodState (corner z5 a) (corner z5 b)) = prodState (corner z5 a) (corner z5 (a + b))) ∧ GateRel n5 gSq ∧ (∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq (prodState x y) ∈ maxCone (eball 5)) ∧ ¬ (∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq.symm (prodState x y) ∈ maxCone (eball 5))
```
### `gSqInv_sep` (theorem, sha256 e875280fbd08af45)
```
theorem gSqInv_sep : IsNot (eball 5) z5 n5 ∧ (∀ a b : Fin 2, gSq.symm (prodState (corner z5 a) (corner z5 b)) = prodState (corner z5 a) (corner z5 (a + b))) ∧ GateRel n5 gSq.symm ∧ (∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq.symm.symm (prodState x y) ∈ maxCone (eball 5)) ∧ ¬ (∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq.symm (prodState x y) ∈ maxCone (eball 5))
```
### `nC5` (def, sha256 49145e5a06e04f52)
```
def nC5 : (Fin 5 → ℝ) →ₗ[ℝ] (Fin 5 → ℝ) := diagSign cC5
```
### `isNot_nC5` (theorem, sha256 e448466350f88485)
```
theorem isNot_nC5 : IsNot (eball 5) z5 nC5
```
### `gC5` (def, sha256 f154d16d5864ca0b)
```
def gC5 : W 5 ≃ₗ[ℝ] W 5 where toFun := gC5Fun invFun := gC5Fun map_add' ω₁ ω₂ := by funext μ ν simp only [gC5Fun_apply, Pi.add_apply, mul_add] map_smul' c ω := by funext μ ν simp only [gC5Fun_apply, Pi.smul_apply, smul_eq_mul, RingHom.id_apply] ring left_inv := gC5Fun_gC5Fun right_inv := gC5Fun_gC5Fun
```
### `gC5_frame` (theorem, sha256 3df4b3dc41cb1766)
```
theorem gC5_frame (a b : Fin 2) : gC5 (prodState (corner z5 a) (corner z5 b)) = prodState (corner z5 a) (corner z5 (a + b))
```
### `gC5_relT` (theorem, sha256 d128583806186026)
```
theorem gC5_relT (ω : W 5) : actT nC5 (gC5 (actT nC5 ω)) = gC5 ω
```
### `gC5_not_relC` (theorem, sha256 598c1352eec778dc)
```
theorem gC5_not_relC : ¬ ∀ ω, actC nC5 (gC5 (actC nC5 ω)) = actT nC5 (gC5 ω)
```
### `gC5_posFwd` (theorem, sha256 7d537947820e7853)
```
theorem gC5_posFwd : ∀ x ∈ eball 5, ∀ y ∈ eball 5, gC5 (prodState x y) ∈ maxCone (eball 5)
```
### `gC5_posInv` (theorem, sha256 97b441e96f56098c)
```
theorem gC5_posInv : ∀ x ∈ eball 5, ∀ y ∈ eball 5, gC5.symm (prodState x y) ∈ maxCone (eball 5)
```
### `c5_sep` (theorem, sha256 07a7009d9463071d)
```
theorem c5_sep : IsNot (eball 5) z5 nC5 ∧ (∀ a b : Fin 2, gC5 (prodState (corner z5 a) (corner z5 b)) = prodState (corner z5 a) (corner z5 (a + b))) ∧ (∀ ω, actT nC5 (gC5 (actT nC5 ω)) = gC5 ω) ∧ (∀ x ∈ eball 5, ∀ y ∈ eball 5, gC5 (prodState x y) ∈ maxCone (eball 5)) ∧ (∀ x ∈ eball 5, ∀ y ∈ eball 5, gC5.symm (prodState x y) ∈ maxCone (eball 5)) ∧ ¬ (∀ ω, actC nC5 (gC5 (actC nC5 ω)) = actT nC5 (gC5 ω))
```
### `not_dim_of_relT` (theorem, sha256 a727c946d998dbec)
```
theorem not_dim_of_relT : ¬ ∀ (d : ℕ) (z : Fin d → ℝ) (N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)) (G : W d ≃ₗ[ℝ] W d), IsNot (eball d) z N → (∀ a b : Fin 2, G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))) → (∀ x ∈ eball d, ∀ y ∈ eball d, G (prodState x y) ∈ maxCone (eball d)) → (∀ x ∈ eball d, ∀ y ∈ eball d, G.symm (prodState x y) ∈ maxCone (eball d)) → (∀ ω, actT N (G (actT N ω)) = G ω) → d = 1 ∨ d = 3
```
