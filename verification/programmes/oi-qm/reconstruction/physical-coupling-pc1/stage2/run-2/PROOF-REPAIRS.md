# PC-1 stage 2, run-2 — proof repairs

**Authority.** Owner option A, PR #1022 comment 6547861508. It permits proof bodies only, plus
strictly necessary dependent tactic adjustments. This file lists every change made to
`verification/lean-mathlib/OIBridge/PC1Controls.lean` against run 1 (`f14b59b2`, blob `de0174a9`).
Line numbers are in the repaired file (blob `00988931`, sha256
`781b00b3c43e3959f7d917331542d090d836108ccb2e07ec816c3ad38b05652b`).

**Unchanged.** The header, the 14 fixed statement texts and their checksums, the names, the
declaration order, the definitions, the `#print axioms` lines and the vendored
`F2CoherenceControls.lean`. `git diff f14b59b2 -- …/PC1Controls.lean` changes proof lines only.
The run-2 statement check re-verifies each statement verbatim and records its sha256; the digests
equal run 1's.

## The defects, from run 1's CI

Run 41231679739, job 124627021904: `Build` failed and `Release gate` was skipped. The vendored
`F2CoherenceControls` built. Every error was in `PC1Controls.lean`.

| # | Defect at `f14b59b2` | Cause |
|---|---|---|
| D1 | L82, `aux_G11`: unsolved goal `Complex.I ^ 2 * (-3 / 5) = 3 / 5` | the second `first` alternative, `simp … <;> ring`, does not fail when `ring` cannot close the goal: `ring` falls back to `ring_nf` and leaves it open. `I ^ 2` was never rewritten |
| D2 | L252, L356, L365: unknown identifiers `_root_.mul_zero`, `_root_.zero_mul` | in this Mathlib these names are exported from `MulZeroClass` and are not root declarations, so the `_root_.` form does not resolve. The plain names are what `F2CoherenceControls` uses |
| D3 | `realSubclass_not_p1`, the two `simpa [LieRankSource.phaseGate] using congrFun …` steps: unsolved goals | the `simpa` normal form did not match the stated entry equations in this module |

## The changes

| Change | Line(s) | Defect | Description |
|---|---|---|---|
| R1 | 87–88 (`aux_G11`) | D1 | The alternatives `(simp [Complex.star_def] <;> ring)` and the two `Complex.ext` alternatives are replaced by `(simp [Complex.star_def]` followed by `linear_combination (-3 / 5 : ℂ) * Complex.I_sq)`. This closes the identity with `I ^ 2 = -1` explicitly, the idiom of `BridgeDictionary.lean` and other compiled modules. The first alternative, `(simp [Complex.star_def]; done)`, is kept |
| R2 | 251 (`scaled_rot_not_gauge_nonneg`, `h0c`) | D2 | `_root_.mul_zero` becomes `mul_zero` |
| R3 | 364 (`realSubclass_not_p1`, `hb`) | D2 | `_root_.zero_mul` becomes `zero_mul` |
| R4 | 373 (`realSubclass_not_p1`) | D2 | `_root_.mul_zero` becomes `mul_zero` |
| R5 | 347–352 (`realSubclass_not_p1`) | D3, dependent | A new local `have hentry` gives the entry equation `c * phaseGate (0,0) p q = b * ↑(M p q)`, by rewriting `congrFun (congrFun hM p) q` with `Matrix.smul_apply`, `smul_eq_mul` and `Matrix.map_apply`. It is the same rewrite chain as `hent` in `scaled_rot_not_gauge_nonneg`, which built in run 1 |
| R6 | 353 (`realSubclass_not_p1`) | D3, dependent | A new local `have hne : ¬ ((0, 0) = (1, 0))` by `decide` |
| R7 | 355–357 (`h0`) | D3 | `simpa` is replaced by `hentry (0,0) (0,0)`, rewritten with `LieRankSource.phaseGate`, `Matrix.diagonal_apply_eq` and `if_pos rfl` |
| R8 | 358–361 (`h1`) | D3 | `simpa` is replaced by `hentry (1,0) (1,0)`, rewritten with `LieRankSource.phaseGate`, `Matrix.diagonal_apply_eq`, `if_neg hne` and `_root_.mul_one`. `_root_.mul_one` resolved in run 1, in `gauged_rot_fixes_ones` |

No other line changes. The `have` statements `h0` and `h1` keep their exact types. The conclusion,
the hypotheses and every other proof step are unchanged.

There is no `sorry`, `admit`, new axiom, extra premise or weakening. The Lean was not built
locally. Run-2's evidence is its own CI `Build` and `Release gate` step conclusions at the run's
exact head.
