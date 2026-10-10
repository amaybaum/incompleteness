# EQ4-F preflight: static elaboration review of FourCopyDefs / FourCopyParity / FourCopyPackage

Scope: `verification/lean-mathlib/OIBridge/FourCopy{Defs,Parity,Package}.lean` and the three added
imports at the end of the `OIBridge.lean` import block. I read the source only and did not run Lean.
Names and signatures were checked against the Mathlib v4.33.0 checkout and the OIBridge base modules.

## Verdict

I found no compile or elaboration error in any of the three files or in the import lines.
- Every tactic proof in Defs and Parity should succeed.
- Every statement in Package should elaborate.
- The ten written-out Package proofs should typecheck.

Two **CI release-gate failures** are certain, but they are not Lean errors (findings 1 and 2):
`lake --rehash build` should pass, and the next step, `Release gate` in the `Mathlib bridge` job, will
fail. The other findings are low-probability risks with optional hedges.

## Findings

1. **FourCopyPackage.lean:555–559: `sorryAx` reaches the axiom gate.** Certain. This is a CI-gate
   failure, not an elaboration error.
   - Five of the six `#print axioms` lines will print `sorryAx`:
     - `target02` depends on `fourVal_eq_01` and `fourVal_eq_02`.
     - `fourCopyCoherent_of_kt4Cone` depends on `fourVal_eq_01`, `effB_prodA` and `effA_prodB`.
     - `fourCopyCoherent_of_kt4` is itself `sorry`.
     - `kt4_forward` and `kt4_forward_lt` depend on it, and on `kt4_general`.
   - `tools/lean_axiom_check.py:88-93` hard-fails on any output line containing `sorryAx`.
   - That check is release-gate step `lean-axioms` (`tools/release_gate.py`).
   - The gate runs in CI at `.github/workflows/verify.yml:149-150`, right after the build.
   - The 48 `sorry` warnings themselves do not contain the token. Only the `#print axioms` lines do.
   - Fix, for a green run: delete lines 555–559 and keep 554 (`target01` uses no sorry). Or leave
     FourCopyPackage out of `OIBridge.lean`. Otherwise, accept a red gate on a disposable branch.

2. **All three files: no census disposition.** Certain. This is a CI-gate failure, not an
   elaboration error.
   - `tools/lean_manuscript_census.py:57-63,113-116` globs `OIBridge/*.lean`.
   - It reports `UNCLASSIFIED module …` for any module with no family in
     `verification/lean-manuscript-census.json`. That file has no FourCopy entry.
   - This is release-gate step `lean-manuscript`.
   - Fix: add a family with `modules: [FourCopyDefs, FourCopyParity, FourCopyPackage]`,
     `status: "kernel-only"` (or `"verification-only"`) and `manuscript: []`.
   - Those two statuses need no anchor (`ANCHORED`, census.py:47).

3. **FourCopyParity.lean:73–79, `ipW_dg`: heartbeat budget.** Possible, low.
   - This is the heaviest `simp`: three nested sums over `![…]` tables with symbolic entries.
   - Under binders, `Matrix.cons_val'` pushes symbolic indices before `sum_univ_four'` instantiates
     them. That is extra work but bounded (the term is 4×4).
   - I expect it to fit within `maxHeartbeats 1000000`.
   - Fix if it times out: `simp only [ipW, tabMul, tabT, sum_univ_four']`, then `simp [dg]`, then
     `ring`.

4. **FourCopyParity.lean:116–119, `tens_sharpVec`: `simp … <;> ring`.** Possible, very low.
   - It would fail only if `simp` turned an entry into a disjunction through `mul_eq_mul_left_iff` or
     `mul_eq_mul_right_iff`. Both are `@[simp]` (Mathlib `Algebra/GroupWithZero/Defs.lean:67,93`).
   - I traced all 16 entries. After `one_div`, the two sides never share a syntactic factor, for
     example `b 0 / 2 * (c 1 / 2) = 4⁻¹ * (b 0 * c 1)`.
   - `div_mul_div_comm`, `div_mul_eq_mul_div` and `mul_div_assoc'` are not simp lemmas in this
     Mathlib (`Algebra/Group/Basic.lean`, `@[to_additive]` only).
   - So `ring` receives a plain ring identity. This matches K2Guard `sharpVec_negX`, which uses
     `simp [sharpVec]` after `fin_cases`. No change needed.

5. **`simp` closures with no fallback tactic.** Possible, very low.
   - Affected: Parity:65 `phiW_eq_dg`, :71 `smul_dg`, :90 `actT_reflY_dg`, :96 `phiW_tabMul`,
     :183 `reflY_z3`, :195 `cnot_prodState_neg`.
   - Each closes only if both sides reach the same `simp` normal form. I traced representative entries
     (the `neg_mul`, `mul_neg`, `neg_mul_neg`, `mul_one` and `zero_mul` paths are confluent) and checked
     the maths exactly (finding 7).
   - In `phiW_tabMul`, the index literals on the two sides can differ only as `Fin 4` against
     `Fin (3 + 1)`: one side's come from `fin_cases` and `Fin.reduceFinMk`, the other's from
     `sum_univ_four'`. These unify by Nat-offset defeq; the NeZero instance arguments are proofs.
   - The other five copy K2Guard `actT_reflY_phiW` and CompositeDimension
     `cnot_prodState_xplus_z3` almost verbatim.
   - Optional hedge: append `<;> ring` to line 96. It does nothing if `simp` already closes the goals.

6. **Name resolution: no problem found.** Checked by script over the 39-module OIBridge import
   closure.
   - Every unqualified identifier that resolves through an `open`ed namespace resolves in exactly one
     of them.
   - Nothing is shadowed by `OIBridge.X`. The only top-level `OIBridge.*` declarations are the 16
     graph names (`Edge`, `Preserves`, `k4_rigidity`, …).
   - Nothing clashes with a Mathlib `_root_.` or `Set.` declaration.
   - No `OIBridge.Matrix` or `OIBridge.Set` namespace exists, so `open Set` and
     `open scoped Matrix` open the intended namespaces.
   - The 144 declarations in the three files have no duplicate names. Parity and Package are disjoint,
     so importing both into `OIBridge.lean` is safe.
   - `φ`, `ψ`, `θ`, `ε`, `Ω` are notation only under scoped or local namespaces, none of them opened.

7. **The arithmetic behind every closing tactic holds.** Checked in exact rationals with the real
   `pc`, `pt` and `sgn` tables.
   - `phiW = dg 1 1 (-1) 1`; `idW = dg 1 1 1 1`.
   - `actT reflY (dg p q r s) = dg p q (-r) s`; `smul_dg`.
   - `tabMul (tabMul phiW f) (tabT phiW) = transposeW f`.
   - `ipW` self-adjointness for `cnot`, `actT reflY`, `cnotTw` and `transposeW`;
     `transposeW ∘ transposeW = id`.
   - `tens_sharpVec`; `ipW_dg`.
   - `cnot (prodState (-xplus) (-z3)) = dg 1 (-1) (-1) (-1)`.
   - `cnotTw (prodState (-xplus) (-z3)) = dg 1 (-1) 1 (-1)`.
   - `cnotTw (prodState xplus z3) = idW`.
   - The `famI` value is `(σ−1)/16` at all 16 twist patterns, and it is negative exactly at the odd
     patterns.
   - The sorry'd `fourVal_eq_01/23/02/13`, `effA_prodA`, `effB_prodB`, `effB_prodA` and `effA_prodB`
     are also true.
   - Scripts: `identities.py` and `fourval.py` in this directory.

8. **Lexical and syntax checks: no problem found.**
   - No tabs, NBSPs, zero-width characters or CRLFs.
   - Block comments are balanced, with no stray `-/` and no nested `/-`. Delimiters are balanced.
   - Every `/-- -/` is followed by a declaration.
   - `set_option … in` precedes the docstring at Parity:73, :92 and :220.
   - The three import lines in `OIBridge.lean` sit inside the import block, before `namespace OIBridge`.

## Mathlib v4.33.0 facts used (grepped)

- **`≪≫ₗ`:** global `notation3`, left-associative (Algebra/Module/Equiv/Defs.lean:314). Mathlib
  proves `LinearEquiv.trans_apply` by `rfl` (:343), which supports `cnotTw_apply := rfl`. That file is
  `@[expose] public section`.
- **`LinearEquiv.map_smul (e : N₁ ≃ₗ[R₁] N₂) (c) (x) : e (c • x) = c • e x`:** `e` explicit, not
  deprecated (:507).
- **`apply_symm_apply`:** `e` explicit (`variable (e e')`, :199).
- **`map_smul`:** simp, MulActionHomClass form.
- **`Matrix.orthogonalGroup (n) [DecidableEq n] [Fintype n] (R) [CommRing R]`:** abbrev for
  `unitaryGroup` under a local `starRingOfComm`. `specialOrthogonalGroup` has the same shape
  (LinearAlgebra/UnitaryGroup.lean:295, :315).
- **`Matrix.PosSemidef`:** needs `[Ring R] [PartialOrder R] [StarRing R]` and no Fintype.
  `PartialOrder ℂ` comes from `open scoped ComplexOrder` (Analysis/Complex/Order.lean:51).
- **`!![`:** global syntax (LinearAlgebra/Matrix/Notation.lean:100).
- **`ᵀ` and `ᴴ`:** scoped in `Matrix`, so `open scoped Matrix` supplies them.
- **`Matrix.vecMulVec`:** exists. The `TopologicalSpace (Matrix m n R)` instance exists.
- **`finProdFinEquiv`:** has implicit `{m n}`, so `@finProdFinEquiv 4 4 : Fin 4 × Fin 4 ≃ Fin (4 * 4)`.
  `Fin (4*4)` and `Fin 16` are defeq.
- **`∑` notation:** a leading `term` with body `term:67`, so `c • ∑ …` parses; Mathlib uses it.
- **`Matrix.cons_val`:** a default dsimproc (declared with no set, so the default `simproc` attribute
  applies). `Fin.reduceFinMk` is a default simproc; Mathlib disables it by name elsewhere.
- **Import paths:** all four Package Mathlib imports exist, and `Mathlib.Tactic.LinearCombination` is
  in Parity's closure.

## Per-declaration notes (all: no error found)

**Defs**
- `actTEquiv`: patterned on the base `cnot`. The `map_add'` and `map_smul'` `simp only` reduce both
  sides to `homMap N (ω₁ μ) ν + homMap N (ω₂ μ) ν` and `c * homMap N (ω μ) ν` respectively.
  `left_inv` and `right_inv := actT_actT hN` match the base `cnot` pattern.
- `cnotTw_apply`: `rfl` via `trans_apply`.
- `gateOf_false` and `gateOf_true`: `rfl` through the match.
- `mem_dualW`: `Iff.rfl`, as in `mem_eball`.

**Parity**
- **Rewrite chains:**
  - `ipW_gateOf` (true branch): kabstract matches the LHS first. The final
    `rw [ipW_actT_reflY]` leaves syntactically equal sides, so `rw`'s `rfl` closes the goal.
  - `cnotTw_prodState_xplus_z3` / `_neg`: `actT_prodState` cannot unify with the outer
    `actT reflY (cnot …)` at reducible or instance transparency, so it rewrites the inner occurrence.
  - The final `neg_neg` in `cnotTw_prodState_neg` hits `- -1` and not `-1`.
- **`gateOf_prodState_*`:** each `show` is defeq: `gateOf false ≡ cnot` and `sgnB false ≡ -1`.
- **`kt4_parity_aligned`:**
  - `simp only` fires `gateOf_sharp` and then the `gateOf_prodState_*` lemmas.
  - `ipW_dg_smul` then matches the whole `ipW`, giving
    `hv : 0 ≤ 1/4*(1/4)*(1*1*1*1 + 1*1*1*-1 + σ + 1*1*1*-1)`.
  - `cases` reverts the dependent `g··`/`h·` hypotheses automatically.
  - `norm_num [sgnB, EvenCycle4, Bool.toNat]` closes all 16 cases.
- **Other proofs:** `incl_*`, `dualW_of_inv`, `gate_sharp_mem_dualW` and `gateOf_sharp` are standard
  `rw`, `refine` and `rintro` steps with matching patterns.

**Package**
- `target01`: anonymous constructor.
- `target02`: `rw [← fourVal_eq_01] at h1` instantiates `(E,F,X,Y)`, then `fourVal_eq_02` gives
  exactly the goal.
- `fourCopyCoherent_of_kt4Cone` and `exists_kt4Cone_of_fourCopyCoherent`:
  - The `rw` patterns are correct.
  - `⟨…⟩` and `hΩ.1` work through set-builder membership, as `h₁.2` does at
    CompositeDimension:1359.
- `idW_mem_twin`: image membership with `⟨phiW, phiW_mem_Q3, actT_reflY_phiW⟩`.
- `isClosed_Q3`: `rw [← dualW_Q3]` gives `IsClosed (dualW Q3)`.
- `KT4LT.toKT4`: `H.CA.Ω` is `H.CA.toPreComposite.Ω`.
- `kt4_forward`, `kt4_forward_lt` and `kt4_forward_drive`: the argument order and the `.p01`
  dot-idents are correct.
- `Pr … deriving DecidableEq` is fine inside `noncomputable section`.

## Expected warnings (harmless)

- 48 `declaration uses 'sorry'` in Package.
- Possibly some unused-variable linter warnings in sorry'd theorems.
