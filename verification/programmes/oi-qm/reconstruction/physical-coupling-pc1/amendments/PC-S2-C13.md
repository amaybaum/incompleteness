# PC-1 — amendment PC-S2-C13: correction of control C13's reference

**Status: append-only, minimally scoped correction.** It is made under the owner's Option 1, PR
#1022 comment 6547368529 (amaybaum, OWNER, 2026-10-31T18:21:48Z). It executes nothing: no Python,
no Lean and no CI. The following stay unchanged as historical records:
- the preregistration (`948b30c1`);
- PC★ (`72b4af27`);
- PC-S2 (`4d2c4d56`: blob `f81dca8cd4bc231a3e97377b73430cc9749590e3`, sha256
  `ad6ed9b53400451a5b2f0d73d839142263d59ca9b9e871e75c7daf51efcbb5d6`), including its original C13
  expected row and exhibit wording;
- the two-track disposition.

This file changes only C13's reference, and the wiring stage 2 needs in order to encode it (§5).
Every other control (C1–C12, C14, C15), mutation, decision table, stage-1 screen and scientific
claim is unchanged. Revised stage-2 execution waits for an independent acceptance of this exact
commit.

***

## 1. Before and after

| Item | Before (preregistration §9; PC-S2 S2-4, S2-8) | After (this correction) |
|---|---|---|
| Object | polar factor of a 2-cell baseline compression; fixed model `X = Fin 13`, uniform measure, `C₀ = {0..3}`, `C₁ = {4..12}`, `σ = (0 4)(1 5)(2 6)(3 7)` | unchanged |
| Exact values | `K = [[0, 2/3], [2/3, 5/9]]`, `U = [[−5/13, 12/13], [12/13, 5/13]]` | unchanged (no rescaling, no added generator) |
| Exhibit `E` | "the polar factor, real and non-monomial where it arises" | listed unchanged; **`exhibits_verified: false`**. Under the inherited exhibit definition (F2-1 prereg §3), an entry must equal `rot` up to a scalar or carry a relative phase in its named basis. The real reflection `U` does neither |
| Screen | item 11 flags it (no executing process) | unchanged, recorded independently of the operator classification |
| `R` | PC-S2 S2-8 item 3: paper, level-one closure only | `¬R` for the full generated class at every availability level: paper proof, §3 |
| `P₁` | kernel `realSubclass_not_p1`, plus the paper containment "the class is real" | unchanged; a direct paper proof is added in §4 |
| Expected row | 3(a) (frozen); PC-S2 S2-8: "3(b) or 9" | **row 9** (§6: L1 not met, `¬R ∧ ¬P₁`, no verified exhibit) |
| Purpose | the screen catches a rule that formally passes (row 3(a)) | a negative control: a representational polar-factor construction against physically executed access (§2) |

## 2. The revised purpose

A polar factor is computed from the baseline image, but no process executes it. So it cannot
count as a physical source, whatever operators it yields; screen item 11 records this. C13 checks
two separate things:
1. the screen rejects the representational construction for its missing executing process;
2. on the fixed model, the construction does not even yield the target operations.

C13's generated class leaves `N` and `O`: `U` has a negative entry and moves the all-ones vector.
Yet it has neither `R` nor `P₁`. So leaving both invariants is necessary, not sufficient (A★4
item 2).

## 3. `¬R` for the full generated class (paper proof)

**The class.** The C13 model's processes are `id` and `σ` (`σ² = id`), together with the register
readout. The polar-factor rule therefore generates, on the register carrier `Fin 2 × Fin 1`:
- `Θ(id) = 1`;
- `Θ(σ) = U`;
- the computed readout projectors `P₀ = diag(1, 0)` and `P₁′ = diag(0, 1)`.

C13's class `𝓘₁₃` is the least `Architecture` containing these. For robustness, the argument below
also covers a class that contains the swap `π = [[0, 1], [1, 0]]`. The swap is not a C13 generator.

**Reduction to class membership.**
- The `Architecture` operations are `one`, `mul`, `smul` (`|a| ≤ 1`), the ancilla-index projectors
  `proj` and the blocks `block` (`ImplementationLocality.lean:506`). There is no operation that
  carries an operator to a larger carrier, and no sum.
- Availability is `InstAvail` (`:268`): one isometric class step, readout with class projectors,
  coarse-graining, bind and uniform discard.
- `RouteB.FalsifierUnavailable` (`RouteB.lean:179`) is the negation of `availExt 1 Unit` of
  `conjChannel rot`.
- Suppose `𝓘₁₃ ⊆ 𝓙` for an `Architecture 𝓙`. Then `instAvail_mono` (`ImplementationLocality.lean:305`)
  carries any availability for `𝓘₁₃` to `𝓙`. The Kraus bridge `exists_scaled_mem_of_instAvail_unitary`
  (`MicroscopicReversibility.lean:251`; kernel) then gives, from `R`, a `c ≠ 0` with
  `c • rot ∈ 𝓙 (Fin 2 × Fin 1)`.
- This covers every route through ancillas, discards and outcome-dependent continuation, because
  the bridge is proved for all of `InstAvail`.

So it suffices to exhibit an `Architecture 𝓙 ⊇ 𝓘₁₃` that contains no nonzero multiple of `rot`
at `Fin 2 × Fin 1`.

**The bounding class `𝓙`.** Let `𝒲` be the multiplicative monoid of real 2×2 matrices generated
by `U`, `π`, `P₀` and `P₁′`. Every element of `𝒲` has operator norm at most 1, so every entry has
modulus at most 1. Define `𝓙(S)` by the size of `S`:
- if `|S| = 2`: all `a · reindex e e W`, with `|a| ≤ 1`, `W ∈ 𝒲` and `e : Fin 2 ≃ S` any bijection;
- if `|S| = 1`: all `x · [1]` with `|x| ≤ 1`;
- otherwise: all `a · D` with `|a| ≤ 1` and `D` a diagonal 0/1 matrix.

**`𝓙` is an `Architecture`.**
- **`one`.** The identity is in `𝒲` and is diagonal 0/1.
- **`smul`.** This is clear in every case.
- **`mul`.** For `|S| = 2`, `reindex e₁ W₁ · reindex e₂ W₂ = reindex e₁ (W₁ · τW₂τ⁻¹)`, where
  `τ = e₁⁻¹e₂` is a permutation of `Fin 2` (the identity or `π`). Since `π ∈ 𝒲`, the product lies
  in `𝒲`. In the other cases, products of diagonal 0/1 matrices are diagonal 0/1, and products of
  scalars are scalars.
- **`proj`.** `diag(r.2 = k)` is diagonal 0/1. On a 2-element carrier it is `1`, `P₀`, `P₁′` or
  `0 = 0 · 1`, all in `𝒲` up to reindexing.
- **`block`** (`S × Fin m → S`).
  - If `|S × Fin m| = 2` with `|S| = 2` and `m = 1`, the block `(0, 0)` is the same matrix
    transported to `S`, so it lies in `𝓙(S)`.
  - If `|S × Fin m| = 2` with `|S| = 1` and `m = 2`, a block is a 1×1 matrix `a · w` with
    `|aw| ≤ 1`, so it lies in `𝓙(S)`.
  - If `|S × Fin m| ≠ 2`, the element is `a · D`, and a block of a diagonal 0/1 matrix is diagonal
    0/1 or zero. That holds also when `|S| = 2`, since diagonal 0/1 matrices lie in `𝒲`.

`U`, `P₀` and `P₁′` lie in `𝓙(Fin 2 × Fin 1)`, and so does `π`. So `𝓘₁₃ ⊆ 𝓙`, because `𝓘₁₃` is
the least such class. This holds equally for any class that also contains `π`.

**No nonzero multiple of `rot` in `𝓙(Fin 2 × Fin 1)`.** Suppose `c · rot = a · W'` with `c ≠ 0`,
where `W' = reindex e e W` is again in `𝒲`, because `π ∈ 𝒲`.
- **Rank.** `a ≠ 0`, and `W'` has rank 2. Any product containing `P₀` or `P₁′` has rank at most
  1. So `W'` is a product of `U` and `π` alone, and lies in the group `𝔇` they generate.
- **Shape of `𝔇`.** `U` and `π` are orthogonal reflections. Their product is the rotation
  `ρ := Uπ = [[12/13, −5/13], [5/13, 12/13]]`. So `𝔇 = {ρⁿ, πρⁿ : n ∈ ℤ}`.
- **Determinant and scalar.** `W'` and `rot` are real orthogonal, and `c/a ≠ 0`. So `W' = (c/a) rot`
  forces `c/a` real with `|c/a| = 1`. Since `det rot = 1` and `det(πρⁿ) = −1`, `W' = ρⁿ` and
  `ρⁿ = ±rot`.
- **As complex numbers.** Identify `[[x, −y], [y, x]]` with `x + iy`. Then `ρ ↔ (12 + 5i)/13` and
  `rot ↔ (3 − 4i)/5`. The case `n = 0` gives `1 = ±(3 − 4i)/5`, which is impossible. Otherwise,
  with `k = |n| ≥ 1`: `5 · (12 ± 5i)^k = ± 13^k · (3 − 4i)`, the sign `±` inside `(12 ± 5i)`
  following the sign of `n`.
- **Gaussian primes.** In the unique factorization domain `ℤ[i]`:
  - `3 − 4i = (2 − i)²`;
  - `5 = (2 + i)(2 − i)`;
  - `13 = (3 + 2i)(3 − 2i)`;
  - `12 ± 5i` has norm 169, so its prime factors lie over 13, and `2 ± i` does not divide it.

  The exponent of the prime `2 − i` is 1 on the left and 2 on the right. Units and signs do not
  change exponents. This is a contradiction.

Hence `¬R` for `𝓘₁₃`, and for any class between `𝓘₁₃` and `𝓙`.

**Rigour.** The argument is a complete paper proof. The bridge and monotonicity steps are existing
kernel theorems. The construction of `𝓙`, its `Architecture` check and the factorization step are
paper, and are not kernel-checked. In C13's record, `R` is labelled `paper`, never `kernel`.

## 4. `¬P₁` (paper proof, together with the existing kernel statement)

`P₁` is the availability at level one of `conjChannel(phaseGate (0, 0))`, with
`phaseGate (0, 0) = diag(i, 1)` (`LieRankSource.lean:209`). By the same bridge, `P₁` gives a
`c ≠ 0` with `c · diag(i, 1) = a · W'`, where `W' ∈ 𝒲` and `a ≠ 0`.
- **Rank.** `W'` has rank 2, so `W' ∈ 𝔇` and is real.
- **Entries.** The diagonal entries give `W'₀₀ = (c/a) i` and `W'₁₁ = c/a`. Both are real, which
  forces `c/a = 0`. That contradicts `c ≠ 0`.

The complex scalar `a` is covered by the argument, and ancilla routes are covered by the bridge.
Independently, `𝓘₁₃ ⊆ realClass`, because `realClass` is an `Architecture` containing `U`, `P₀`
and `P₁′`. So the fixed kernel statement `realSubclass_not_p1` (PC-S2 S2-3) also gives `¬P₁` once
it is built. The record labels `P₁` as `kernel` (that statement), with the containment `paper`.

## 5. The corrected reference, and the wiring stage 2 needs

**C13's reference.**
- Row 9.
- `R: false (paper, this §3)`.
- `P₁: false (kernel realSubclass_not_p1; containment paper)`.
- `exhibits_verified: false`.
- `screen_flags: ["no executing process" (item 11)]`.
- L1 not met.

The exact checks of `K` and `U` (`UᵀU = 1`, `UᵀK` symmetric positive semidefinite) still run and
are recorded, as checks of the fixed model, not as exhibits. With `¬R ∧ ¬P₁`, row 3(a) does not
fire. Row 3(b) does not fire because the exhibit is not verified. Row 9 applies.

**Evidence footing.** Frozen §6 lists row 9's evidence layer as kernel. C13's `¬R` rests on kernel
steps (`instAvail_mono`, `exists_scaled_mem_of_instAvail_unitary`) together with a paper class
bound and a paper Gaussian-integer factorization (§3). Its `¬P₁` rests on the kernel statement
`realSubclass_not_p1` with a paper containment. Row 9's evidence column is therefore met in this
mixed form, as PC-S2 already accepts for C10 (paper containment) and C12 (paper transport), and the
paper steps are independently reviewed. It is not a kernel-only proof and is not labelled as one.
If the owner reads row 9's "kernel" strictly, the owner's own rule applies instead: C13 routes to
row 10, with `R` named as the predicate not settled in the kernel.

**The wiring changes.** These are exact and complete. They are made at stage 2, not here.
- **W1.** In `stage2/controls.py`, the C13 record has these fields: `R = False`, with
  `R_source = "paper:PC-S2-C13 §3"`; `P1 = False`, with `P1_source = "kernel:realSubclass_not_p1"`;
  `exhibits_verified = False`; `screen_flags = ["no_executing_process"]`; `L1 = "not met"`.
- **W2.** C13's expected row in the controls table is `"9"`, replacing `"3a"`. The results field
  `controls.C13` gains `"reference_source": "amendments/PC-S2-C13.md"`.
- **W3.** C13's exhibit check is recorded as `"exhibit_listed": "U", "exhibit_verified": false,
  "reason": "neither rot up to a scalar nor a relative phase in its named basis"`. The model checks
  of `K` and `U` stay under `exact`.
- **W4.** The freeze checkpoint and the `inputs` field add this file by blob and sha256, beside the
  four frozen inputs and `PC-S2.md`.
- **W5.** `RESULT.md` cites this correction for C13.

**No other change.** No self-test case and no mutation references C13 (PC-S2 S2-5), so neither
needs a change. The decision function, the Lean statements and every other control reference stay
unchanged.

## 6. What this correction does not do

- It runs nothing.
- It edits no earlier file.
- It invents no exhibit, changes no model, rescales nothing and adds no generator.
- It does not change the decision function or the strict token, which stays `INCONCLUSIVE (void)`
  under 0(vi).
- It does not claim that a polar-factor rule can be a physical source.
- The exclusion of §3 concerns C13's fixed model and classes between `𝓘₁₃` and `𝓙`, and nothing
  more.
