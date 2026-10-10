# RELC-SELECT-1 design draft: the squeezed gate at d = 5 (`RelcSelectSqueeze.lean`)

Status: **UNBUILT**. No Lean toolchain was available. The module was written against the landed sources at
L = `e2426ba4` (read-only worktree `wt-L`). Lean v4.33.0 / Mathlib v4.33.0 per `lakefile.toml`. Nothing
here is frozen or governed. **Sorry count: 0.** Every proof is written in full. None has been
kernel-checked.

Parameters: ε = 1/10 and λ = 1/2, the ledger's values. The proof's bound is ε ≤ (1−λ)/(2(1+λ)) = 1/6.
The squared chain below needs only 4ε² ≤ 1/8, so ε = 1/10 has slack.

## 1. Exported statements (namespace `OIBridge.RelcSelect`; every name grep-fresh across `OIBridge/`)

General, any `d`, `Ω`, `z`, `N`, `G : W d ≃ₗ[ℝ] W d` (§A):
- `frame_symm` (hF : frame of G) : frame of G.symm
- `relT_symm` (hN : IsNot Ω z N) (hT : relT of G) : relT of G.symm
- `relC_symm` (hN) (hT) (hC : relC of G) : relC of G.symm
- `gateRel_symm` (hN) : GateRel N G → GateRel N G.symm

d = 5, `N = n5`, `z = z5`:
- `gSq : W 5 ≃ₗ[ℝ] W 5`. It is built from `gSqFun ω m n = sqW m n * ω (sqPc m n) (sqPt m n)` and
  `gSqInvFun` (weights `sqWi`). The index map `(sqPc, sqPt)` is an involution (`sqPc_sqPc`,
  `sqPt_sqPt`, both by `decide`).
- `gSq_frame (a b : Fin 2) : gSq (prodState (corner z5 a) (corner z5 b)) = prodState (corner z5 a) (corner z5 (a + b))`
- `gSq_relT : ∀ ω, actT n5 (gSq (actT n5 ω)) = gSq ω`
- `gSq_relC : ∀ ω, actC n5 (gSq (actC n5 ω)) = actT n5 (gSq ω)`
- `gateRel_gSq : GateRel n5 gSq`
- `gSq_posFwd : ∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq (prodState x y) ∈ maxCone (eball 5)`
- `gSq_symm_value : prodEffVal (sharpEff z5) (sharpEff (-x5)) (gSq.symm (prodState z5 x5)) = -1 / 2`
- `gSq_not_posInv : ¬ ∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq.symm (prodState x y) ∈ maxCone (eball 5)`
- `not_nativeGate_gSq : ¬ NativeGate (eball 5) z5 n5 gSq`, and `not_nativeGate_gSqInv` (the same for `gSq.symm`)
- `gSq_sep : IsNot (eball 5) z5 n5 ∧ (frame) ∧ GateRel n5 gSq ∧ (posFwd) ∧ ¬ (posInv)`
- `gSqInv_sep : IsNot (eball 5) z5 n5 ∧ (frame of gSq.symm) ∧ GateRel n5 gSq.symm ∧ (∀ x y, gSq.symm.symm (prodState x y) ∈ maxCone) ∧ ¬ (∀ x y, gSq.symm (prodState x y) ∈ maxCone)`.
  These are the five clauses for `gSq.symm`, with `posInv` holding and `posFwd` failing.

Countercontrol (§G; the ledger's preregistration suggestion, §6):
- `gCtl_value`. `gCtlFun` is the same `G_ε` with λ = 1 (no squeeze). On the test (e₁, e₂) with sharp
  effects (e₁, −e₂) it gives `−1/40`.
- `gSq_ctl_test_value`. The squeezed gate gives `9/80` on the same test.
- `gCtl_not_posFwd`. So without the squeeze, forward positivity fails.

Helper declarations (also exported): `add_add_fin2`, `sqCls`, `sqSig`, `sqPc`, `sqPt`, `sqR`, `sqK`,
`sqW`, `sqWi`, `sqSg`, the `decide` index lemmas, `sqWi_sqW`, `sqW_sqWi`, `homMap_n5_sqSg`,
`sqSg_sq`, `sqSg_sqPt`, `sqSg_sqPc`, `pairVal_gSq_prodState`, `lor_five`, `gSq_pairVal_nonneg`,
`rsq_cs4`, `rsq_ab`, `rsq_s`, `rsq_key`, `rsq_assemble`, `gSq_core`, `x5_unit`, `negx5_unit`,
`sharpVec_negx5`, `gSq_symm_not_mem_maxCone`, `gSqInv_posInv`, `e5b`, `e5b_unit`, `nege5b_unit`,
`sharpVec_x5`, `sharpVec_nege5b`, `gCtlFun`, `gCtlFun_apply`.

### The gate, entrywise

Homogeneous indices 0..5. The classical class is `sqCls = {0, 5}`. The parity is the landed `odd5`
(odd = {3, 4, 5}). `sqSig`: 0↔1, 3↔5, 2 and 4 fixed.
- `sqPc m n = if odd5 n then perm5 m else m`. On C, `perm5` is 0↔5. On T it is the ledger's `permT`
  (1↔3, 2↔4).
- `sqPt m n = if sqCls m then n else sqSig n`.
- `sqW m n = sqR m * sqK (sqPt m n)`, with `sqR = 1 | 1/10` (row ε) and `sqK = 1 | 1/2` (K_λ).
- `sqWi m n = (1 | 10) * (1 | 2)`, by the class of m and the class of n.

With ε = λ = 1 and σ = id this is the landed `gJ5 = sgate odd5 perm5`. The check script's check A1
proves that the table equals the ledger's independent model `possep_gate.Squeezed(2, 1/10, 1/2)` on
all 36 basis vectors.

## 2. Proof plan for `gSq_posFwd`, with the check for each step

Notation: a = ehom e and b = ehom f are cone vectors (`lor_ehom`, `lor_five`); x, y are ball points.

| step | Lean | statement | how verified |
|---|---|---|---|
| D0 | `pairVal_gSq_prodState` | `pairVal a b (gSq (prodState x y)) = (1+x₄)/2·(a₀+a₅)·A + (1−x₄)/2·(a₀−a₅)·B + (S_e C_e + S_o C_o)/10`, where A = b₀+b₅y₄+(b₁y₀+b₂y₁+b₃y₂+b₄y₃)/2, B = b₀−b₅y₄+(b₁y₀+b₂y₁−b₃y₂−b₄y₃)/2, S_e = b₁+(b₀y₀+b₂y₁)/2, S_o = b₃y₄+(b₅y₂+b₄y₃)/2, C_e = x₀a₁+x₁a₂+x₂a₃+x₃a₄, C_o = x₀a₃+x₁a₄+x₂a₁+x₃a₂ | 22-variable polynomial identity: `check_squeeze.py` B1 (model) and `check_lean_text.py` L1, which parses the Lean text |
| D1 | `rsq_cs4` | (p·q)² ≤ \|p\|²\|q\|² in 4 variables | C1: RHS−LHS is the sum of the 6 Lagrange squares. `linarith` with those 6 hints |
| D2 | `rsq_ab` | f, t, s ≥ 0, t ≤ f, s ≤ 1, u² ≤ (f²−t²)(1−s²), A ≥ f+u−ts/2, B ≥ f−u−ts/2 ⇒ A, B ≥ 0 and AB ≥ (t²+f²s²)/8 | C2: (f−ts)²−u² = [(f²−t²)(1−s²)−u²] + (fs−t)², so \|u\| ≤ f−ts (`abs_le_of_sq_le_sq'`). C3: AB − (t²+f²s²)/8 = [AB−L₁L₂] + [(f²−t²)(1−s²)−u²] + ½(t−fs)² + ⅜t²(1−s²) + ⅜s²(f²−t²). L6 re-checks this against the Lean text |
| D3 | `rsq_s` | S_e² + S_o² ≤ 2(b₁²+b₂²+b₃²+b₄²) + f²(y₀²+…+y₃²) | C5 / L5: RHS−LHS equals an explicit combination, with coefficients 1, 1, ½, ½, 2, ½, ½, ½, 2, 2, of 10 terms. Each term is nonnegative under the hypotheses (the `linarith` hint list) |
| D4 | `rsq_key` | b in the cone, y in the ball ⇒ A ≥ 0, B ≥ 0, (S_e²+S_o²)/50 ≤ AB (this is 2ε²(S_e²+S_o²) ≤ AB) | t := √(b₁²+…+b₄²) and s := √(y₀²+…+y₃²) are used only as witnesses with t ≥ 0, t² = …. Then `rsq_cs4` gives r₁², r₂² ≤ (ts)². D2 runs with u = b₅y₄. Final step C6: (T+F)/8 − (2T+F)/50 = (17/200)T + (21/200)F ≥ 0. L4 checks that the conjunct is exactly gSq_core's A, B, S_e, S_o |
| D5 | `rsq_assemble` | 1±α ≥ 0, p, q, A, B ≥ 0, T_c ≤ 1−α², T_a ≤ pq, C_e², C_o² ≤ T_cT_a, (S_e²+S_o²)/50 ≤ AB ⇒ V ≥ 0 | C7: AM–GM, P² − (1−α²)pqAB = (P₁−P₂)². C8: CS2. C9: the chain E² ≤ (S·C)/100 ≤ S·2T_cT_a/100 = (S/50)T_cT_a ≤ AB·T_cT_a ≤ (1−α²)pqAB ≤ P². Then P ≥ 0 and E² ≤ P² give P+E ≥ 0 (`abs_le_of_sq_le_sq'`). L3′ checks that the instantiation equals gSq_core's goal |
| D6 | `gSq_core` | coordinate form: 6+6+5+5 variables, hypotheses Lor(a), Lor(b), x, y ∈ ball | assembles D1–D5. The instantiation is `exact h` with a `linarith [h]` fallback. C10 is the T_a step |
| D7 | `gSq_pairVal_nonneg`, `gSq_posFwd` | `lor_five`, `Fin.sum_univ_five` on the ball, `rw [pairVal_gSq_prodState]`, then `exact gSq_core …`. maxCone membership is unfolded with the same `show` as landed `cnot_prodState_mem_maxCone` | L2′: the conclusion of gSq_core is textually the RHS of D0 under `a i ↦ ai`, so the `exact` matches syntactically |

Every `linarith` step in D1–D5 has a linear certificate over monomials. Each certificate was checked
as an exact sympy polynomial identity, so no `nlinarith` search is needed for correctness. `nlinarith`
is used only for the two-line facts `1−s² ≥ 0` and `f²−t² ≥ 0`, with the product hint supplied.

### The `posInv` witness (§E)

`gSq.symm (prodState z5 x5) = hom z5 ⊗ (1, 2, 0, 0, 0, 0)` (A13). Pairing it with `sharpVec z5 = (½,0,0,0,0,½)` and
`sharpVec (−x5) = (½,−½,0,0,0,0)` (A14) gives 1·(½ − 1) = −1/2 (A12). This agrees with the ledger's N3.4.
The value is proved like landed `gJ5_value`: rewrite both `sharpVec`s to explicit functions, then
`simp +decide` over the 36 entries, then `norm_num`.

## 3. Checks run (all exact; outputs saved next to the scripts)

- `check_squeeze.py` → `check_squeeze.out`: **34 PASS, 0 failed.**
  - A1–A17: the table against the ledger model; round trips; frame; relT; relC; sign lemmas; witness
    −1/2; countercontrol −1/40 and 9/80.
  - B1: the decomposition identity.
  - C1–C12: the certificates.
  - D0: the generic-(ε, λ) decomposition agrees with the ledger model at 60 rational points.
  - D1/D1′: the ε-bound is load-bearing. At ε = 1, λ = 1/2, posFwd fails at an exact rational point:
    x = e₁, y = e₂, effects sharp along e₁ and (−3/5, −4/5, 0, 0, 0), value −1/10. The ledger model
    confirms the value.
  - D2: a grid sanity check only, not a proof.
- `check_lean_text.py` → `check_lean_text.out`: **8 PASS, 0 failed.** It parses the `.lean` file
  itself (L1–L6).

## 4. Landed declarations used (file:line at L)

- CompositeDimension.lean:
  - Carrier and actions: `W` 97, `prodState` 161, `pairVal` 164, `prodEffVal` 182, `maxCone` 186,
    `actT` 198, `actC` 201, `corner` 205.
  - Gate structures: `IsNot` 210, `NativeGate` 218.
  - Rewrite and apply lemmas: `actT_actT` 471, `actC_actC` 476, `corner_zero`/`corner_one` 825–826,
    `actT_apply` 828, `actC_apply` 831, `prodState_apply` 834.
  - Cone: `Lor` 869, `lor_ehom` 930.
  - Idiom models only, not called: `cnot` 775, `cnot_core` 1067, `cnot_prodState_mem_maxCone` 1152.
- ParityNot.lean:
  - Relations: `GateRel` 42.
  - Idiom models only, not called: `sgateEquiv` 437, `sgate_relT` 456, `sgate_relC` 465.
  - The d = 5 data: `odd5` 556, `perm5` 559, `n5` 570, `z5` 573, `x5` 576.
  - Lemmas used: `homMap_n5_sign` 582, `isNot_n5` 592, `x5_mem` 612, `z5_mem` 616, `z5_unit` 653,
    `sharpVec_z5` 671, `sum_univ_six'` 687.
  - The `@[simp]` `hom5_one … hom5_five` 625–629 are used implicitly by `simp`.
  - Idiom models only, not called: `gJ5_frame` 631, `gJ5_value` 692.
- EffectSpace.lean: `sharpVec` 57, `sharpEff` 65, `sum_neg_sq` 75, `mem_eball_of_sphere` 78,
  `sharpEff_isEffectOn` 97, `prodEffVal_sharp` 514.
- TransitiveBody.lean: `eball` 518, `mem_eball` 520. KInfFoundations.lean: `IsEffectOn` 116.
- OddChar.lean: imported only. `nK 2 = n5` and `zK 2 = z5` up to the landed definitions. The module
  works with `n5`/`z5` directly, as the task specifies. The open line is copied from OddChar.lean:30.

## 5. Mathlib names

- Not used anywhere in OIBridge at L: `LinearEquiv.symm_symm` (**MATHLIB-NAME-UNVERIFIED**). It is
  only the fallback branch of a `first` in `gSqInv_posInv`. The primary branch is
  `exact gSq_posFwd …`, which relies on `gSq.symm.symm` being definitionally `gSq`.
- All other names occur in landed OIBridge code:
  - Equivalence lemmas: `G.symm_apply_apply`, `G.apply_symm_apply`, `G.injective`.
  - Order and arithmetic lemmas: `mul_le_mul`, `mul_le_mul_of_nonneg_left/right`, `sub_nonneg`,
    `abs_le_of_sq_le_sq'`, `add_nonneg`, `mul_nonneg`, `sq_nonneg`, `mul_pow`, `zero_le_one`.
  - Square root: `Real.sqrt`, `Real.sqrt_nonneg`, `Real.sq_sqrt`.
  - Finite sums: `Fin.sum_univ_five`.
  - Tactics: `linear_combination`, `simp +decide`, `fin_cases`, `decide`.

## 6. Top compile risks (most likely first) and the intended repair

1. **Brute-force `simp +decide` evaluation.** This covers `gSq_frame` (144 goals),
   `pairVal_gSq_prodState` (36 entries) and the three value lemmas. The steps rely on simp reducing
   `sqCls`/`sqSig`/`perm5`/`odd5` and the `if`s at the numerals produced by `fin_cases` and
   `sum_univ_six'`, which is the same mechanism as the landed `gJ5_frame`/`gJ5_value`/`prodEffVal_cnot_prodState`.
   - The risks are residual arithmetic, simp rewriting the right-hand side of an equation, and run
     time.
   - Mitigations already in place: `<;> norm_num` / `<;> ring` tails. `pairVal_gSq_prodState`
     simplifies the LHS only (`conv_lhs`), with the landed `cnot` pattern as a `first` fallback.
   - Repair if still needed: add `decide`-proved value tables (e.g. `sqPc 0 3 = 5`) as simp lemmas.
2. **The `simp only` shape before `linear_combination` in `gSq_relT`/`gSq_relC`.**
   - `gSqFun_apply` (indices `Fin 6`) and `homMap_n5_sqSg` (`Fin (5 + 1)`) must fire on terms whose
     indices come from `funext` on `W 5`. There is precedent: `cnotFun_apply` with `Fin 4`.
   - `sqSg_sqPc` uses `cases odd5 m`, as in the landed `sgate_relC`.
   - Repair: `funext m n; fin_cases m <;> fin_cases n <;> simp +decide [...]`, as in `cnot_relT`.
3. **`linarith` on the degree-4 certificates.** These are `rsq_s` (10 hints, 11 variables), the
   final steps of `rsq_key`/`rsq_assemble`, and `rsq_cs4`. Each certificate exists and is exactly
   verified, but linarith must find it after its polynomial normalization (as in the landed
   `cnot_core`), and run time may be noticeable.
   - Repair: pass the exact coefficients listed in §2 through intermediate `have`s, or switch to
     `nlinarith` with the same hints.

Minor risks:
- The `show` defeq steps in `sharpVec_negx5`/`sharpVec_x5`/`sharpVec_nege5b`, which follow the
  landed `sharpVec_w5`.
- `decide` on `∀ m n : Fin 6` for `if`-defined index maps (landed precedent: `pc_pc` on `Fin 4`).

## 7. What is not claimed

- That `gSq` is entangling (`Entangling` is not examined).
- Anything about `posFwd + Entangling`.
- Any d other than 5. The ledger's N3.5 is a written proof for general odd d and is not formalized
  here.
- Any statement about physics.

## 8. Files

- `RelcSelectSqueeze.lean`: the module.
- `check_squeeze.py` (`check_squeeze.out`): exact model and certificate checks. It imports the
  ledger's `possep/possep_gate.py` read-only.
- `check_lean_text.py` (`check_lean_text.out`): checks the statements as written in the `.lean` file.
