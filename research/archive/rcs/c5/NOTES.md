# RELC-SELECT-1 design: the C5 countermodel at d = 5 (`RelcSelectC5.lean`)

Status: **UNBUILT DRAFT.** No local Lean toolchain was available, so nothing here has been compiled.
Every identity and table the proofs rely on is checked exactly by `c5_check.py`, which passes 44/44
(`c5_check.out`). Source snapshot: certified commit L = `e2426ba4` (read-only `wt-L`). Sorry count: **0**.

## Which C5, and why

NB-1's `d = 5` J/K map (its control C5) and the `d = 5` member `C_5` of REL-T's odd family are the
**same gate**. `c5_check.py` (A) shows that the tables parsed from the Lean file define exactly
`native_gate_ball_probe.jk_map()` at L and `relt_pos_exact.jk_gate(5)`. The two sources differ only in
how they prove positivity. NB-1 reduces to the complex CNOT through a boundary-circle argument. REL-T
gives a direct proof: an exact value identity plus AM–GM and Bessel. The draft uses REL-T's direct
proof, because it splits into small polynomial lemmas that use no `Real.sqrt`.

**The NOT.** No landed NOT fits. `n5` and `nK 2` are balanced (eigenspace dimensions (3,3)), and C5
needs `p_N = 1`, `q_N = 3`. With `n5`, the K-block would have to commute with an `N` that has odd-size
eigenspaces on `V₋`, which no complex structure can do. The draft therefore adds
`nC5 = diagSign cC5 = diag(1, −1, −1, −1, −1)`, which mirrors `n5`/`isNot_n5`. It reuses the landed
axis `z5`, `z5_unit`, `sum_univ_six'`, the `hom5_*` simp lemmas, `diagSign` and `OddChar.entW`.

**The gate.** `gC5` is a signed permutation of the 36 entries, defined like DIM-1's `cnot`
(`gC5Fun ω μ ν = sgnC5 μ ν * ω (pcC5 μ ν) (ptC5 μ ν)` with 36-arm `pcC5`/`ptC5` tables). It satisfies
`invFun = toFun`, so `gC5.symm = gC5` holds definitionally.

## Exported statements (namespace `OIBridge.RelcSelect`)

| name | statement |
|---|---|
| `oddC5`, `cC5`, `nC5` | the NOT `diag(1,−1,−1,−1,−1)` |
| `isNot_nC5` | `IsNot (eball 5) z5 nC5` |
| `gC5 : W 5 ≃ₗ[ℝ] W 5` | the J/K gate, `invFun = toFun = gC5Fun` |
| `gC5_frame (a b : Fin 2)` | `gC5 (prodState (corner z5 a) (corner z5 b)) = prodState (corner z5 a) (corner z5 (a + b))` |
| `gC5_relT` | `∀ ω, actT nC5 (gC5 (actT nC5 ω)) = gC5 ω` (stated pointwise in `ω`) |
| `gC5_not_relC` | `¬ ∀ ω, actC nC5 (gC5 (actC nC5 ω)) = actT nC5 (gC5 ω)` |
| `gC5_posFwd` | `∀ x ∈ eball 5, ∀ y ∈ eball 5, gC5 (prodState x y) ∈ maxCone (eball 5)` |
| `gC5_posInv` | the same with `gC5.symm` |
| `c5_sep` | `IsNot … ∧ frame ∧ relT ∧ posFwd ∧ posInv ∧ ¬ relC`; each conjunct is the `NativeGate` field text with `G := gC5`, `z := z5`, `N := nC5` |
| `not_nativeGate_gC5` | `¬ NativeGate (eball 5) z5 nC5 gC5` |
| `not_dim_of_relT` | `¬ ∀ d z N G, IsNot → frame → posFwd → posInv → relT → d = 1 ∨ d = 3` (the hypotheses of `dim_of_nativeGate` without `relC`) |

Auxiliary results:
- the decide lemmas `pcC5_pcC5`, `ptC5_ptC5`, `sgnC5_mul_sgnC5`, `oddC5_ptC5`;
- `homMap_nC5_sign`, `gC5_relC_lhs`, `gC5_relC_rhs`;
- `prodEffVal_gC5_prodState`, `gC5_prodEffVal_nonneg`;
- the real lemmas `selC5_*`.

**relC witness.** Take `ω = entW 3 3`, the matrix unit at `(w₁, w₁)`, and read entry `(4, 4)`, i.e.
`(w₂, w₂)`. The control side is `1` and the target side is `−1`. The cause is that `J : w₁ ↦ w₂` joins
two coordinates with the same `nC5`-sign, while `K` maps `V₋` to itself. This is checked in C.

## Positivity proof plan (each step is checked in `c5_check.py`)

Notation:
- `e = ehom e`, `f = ehom f` (each in `HVec 5`);
- `p = f₀ + f₁y₀` and `m = f₂y₁ + f₃y₂ + f₄y₃ + f₅y₄`, so that `p ± m = ⟨f, hom y⟩, ⟨f, homMap nC5 (hom y)⟩`;
- `α = f₀y₀ + f₁` and `β = f₅y₁ + f₄y₂ − f₃y₃ − f₂y₄`;
- `s₁ = e₁x₀ + e₂x₁ + e₃x₂ + e₄x₃` and `s₂ = e₂x₀ − e₁x₁ + e₄x₂ − e₃x₃`.

1. **Value identity** (`prodEffVal_gC5_prodState`, D). It states
   `value = (e₀ + x₄e₅)p + (e₅ + x₄e₀)m + s₁α + s₂β` as a polynomial identity. The proof mirrors
   `prodEffVal_cnot_prodState`: `simp only [… sum_univ_six']`, then `simp +decide [sgnC5, pcC5, ptC5]`,
   then `ring`.
2. **`selC5_cs`** (5-variable Cauchy–Schwarz). The Lagrange identity holds, with 10 squares (E).
3. **`selC5_besselJ` / `selC5_besselK`.** For example, `(a·b)² + (a·Jb)² ≤ |a|²|b|²`. The proof is the
   four-square identity with two explicit completion squares (E). The countercontrol in F is that the
   bound fails for a non-complex-structure (symmetric swap) term.
4. **`selC5_cauchy2`.** `(s₁α + s₂β)² ≤ (s₁² + s₂²)(α² + β²)`, by the identity with the square
   `(s₁β − s₂α)²`.
5. **`selC5_mix`.** If `A, B ≥ 0` and `u² ≤ AB`, then `0 ≤ A + B + 2u`. The proof uses
   `(A+B)² − 4u² = (A−B)² + 4(AB − u²)`, then `abs_le_of_sq_le_sq'`.
6. **`selC5_target`.** Assume `f₀ ≥ 0`, `Σf² ≤ f₀²` and `Σy² ≤ 1`. Then:
   - `p ± m ≥ 0`, by `selC5_cs` at `(y₀, ±y₁, …)` and `abs_le_of_sq_le_sq'`;
   - `α² + β² ≤ p² − m²`, by `p² − α² = (f₀² − f₁²)(1 − y₀²)` (E) together with `selC5_besselK` and
     `mul_le_mul`.
7. **`selC5_ctrl`.** Put `A = (1+x₄)(e₀+e₅)(p+m)` and `B = (1−x₄)(e₀−e₅)(p−m)`. Both are `≥ 0`, using
   `abs_le_of_sq_le_sq'`. Then `u² ≤ (s₁²+s₂²)(α²+β²) ≤ (e₀²−e₅²)(1−x₄²)(p²−m²) = AB` (identity
   `hprod`), and `A + B + 2u = 2·value` (identity `hsum`).
8. **`selC5_core`.** This bounds `s₁² + s₂² ≤ (e₀² − e₅²)(1 − x₄²)` by `selC5_besselJ` and
   `mul_le_mul`, then applies `selC5_ctrl`.
9. **`gC5_prodEffVal_nonneg`.** This mirrors `cnot_prodEffVal_nonneg`: `lor_ehom` → `selC5_lor` →
   `selC5_target` → `selC5_core`, then rewrites with the value identity and finishes with `linarith`.
   `gC5_posFwd` mirrors `cnot_prodState_mem_maxCone`. `gC5_posInv` rewrites with `gC5_symm_apply` and
   reuses `gC5_posFwd`.

Every `have … := by ring` identity in the Lean text (10 of them) is parsed from the file and checked as
a polynomial identity (H), including a parser self-test.

Every SOS step is written in the landed `cnot_core` style: an explicit identity by `ring`, then
`linarith`/`positivity`. So `linarith` only has to combine syntactically matching atoms. No step
depends on `nlinarith` search.

Sanity checks (not certificates):
- exact rational sampling over sphere products and boundary effects gives a minimum value `≥ 0` (G);
- the evaluator reproduces the landed `gJ5_value = −1/10`;
- the mutation `J := id` keeps the frame, relT and `G² = I`, and the sampler finds an exact negative
  value for it.

## Landed declarations used (at L)

- **CompositeDimension.lean:**
  - `HVec` 93, `W` 97, `hom` 100, `hom_zero` 102 (simp), `homMap` 112, `prodState` 161, `pairVal` 164,
    `ehom` 167, `prodEffVal` 182, `maxCone` 186, `actT` 198, `actC` 201, `corner` 205, `IsNot` 210,
    `NativeGate` 218;
  - `corner_zero`/`corner_one` 825–826, `actT_apply` 828, `actC_apply` 831, `prodState_apply` 834,
    `Lor` 869, `lor_ehom` 930.
  - Mirrored, not called: `cnot`/`cnotFun_cnotFun`/`sgn_mul_sgn` 766–790, `cnot_frame` 848,
    `cnot_relT` 854, `cnot_core` 1067, `cnot_target` 1107, `prodEffVal_cnot_prodState` 1129,
    `cnot_prodEffVal_nonneg` 1140, `cnot_prodState_mem_maxCone` 1152, `nativeGate_cnot` 1160,
    `dim_of_nativeGate` 2723.
  - `cnot1_core` 2821 was read but is not needed.
- **ParityNot.lean:** `diagSign` 292, `homMap_diagSign` 299, `z5` 573, `hom5_one…hom5_five` 625–629
  (simp), `z5_unit` 653, `sum_univ_six'` 687. Mirrored: `homMap_n5_sign` 582, `isNot_n5` 592,
  `gJ5_frame` 631.
- **OddChar.lean:** `entW` 238. Its open line (line 30) is exactly the module's open line.
- **TransitiveBody.lean:** `eball` 518, `mem_eball` 520. **KInfFoundations.lean:** `IsEffectOn` 116.

**Freshness.** Every new name returns 0 hits under `verification/lean-mathlib/OIBridge/` at L. No new
name collides with a declaration in an opened namespace. In particular `c5_sq` and `c5` from ParityNot
are avoided by using the `cC5`/`selC5_` prefixes.

## Mathlib names

The module uses no Mathlib name that the landed OIBridge modules do not already use. The names it uses
are: `abs_le_of_sq_le_sq'`, `mul_le_mul`, `mul_nonneg`, `add_nonneg`, `sq_nonneg`, `one_pow`,
`mul_one`, `one_mul`, `mul_pow`, `mul_assoc`, `sq`, `le_trans`, `le_of_eq`, `Fin.sum_univ_five`,
`Fin.cases`, `Matrix.cons_val_succ`, `Finset.sum_congr`, `Pi.add_apply`, `Pi.smul_apply`,
`smul_eq_mul`, `RingHom.id_apply`, `mul_add`, and the tactics `fin_cases`, `simp +decide`,
`split_ifs`, `positivity`, `linarith`, `norm_num`, `omega`, `decide`, `ring`, `simp_all`. Nothing is
marked `MATHLIB-NAME-UNVERIFIED`.

## Top compile risks

1. **`simp +decide` evaluating the 36-arm `pcC5`/`ptC5` matches on `Fin 6` at `Fin (5+1)` literals.**
   This affects `gC5_frame` (144 goals), `prodEffVal_gC5_prodState`, `gC5_relC_lhs/rhs` and
   `sgnC5_mul_sgnC5`. It is the same mechanism as the landed `cnot` (`Fin 4` with `W 3`) and
   `perm5`/`gJ5_value`, but the tables are larger. Fallback: tabulate with
   `pcC5 μ ν := if oddC5 ν then pJ μ else μ` and so on, or add `rfl` lemmas per entry. A second risk
   is elaboration time on the 144-goal frame proof.
2. **The value identity.** After `simp +decide`, `ring` must close a 36-term goal. If simp leaves
   `hom x k` unreduced for some literal form, `ring` fails. Fallback: add `hom5_*`/`hom_zero`
   explicitly to the second simp set, or `norm_num [...]` before `ring`.
3. **Unification and pattern steps that cannot be checked without a compiler.** These are:
   - `rw [e1, e2] at h2` in `selC5_target`: the instantiated `selC5_cs` must print `f2 * -y1` and
     `(-y1) ^ 2` syntactically;
   - the `_` unification of `p m al be` from `hP hQ hPQ` in `gC5_prodEffVal_nonneg`;
   - `simp only [… hodd]` in `gC5_relT`. A `simp_all` fallback is already in place there.

   Fallback for each: pass the arguments explicitly, or replace `rw … at` with
   `linarith`/`nlinarith`.

Also unchecked: `#print axioms` lines are included at the end, as in landed modules. A later round
must also add the module to `OIBridge.lean` and the census registry.
