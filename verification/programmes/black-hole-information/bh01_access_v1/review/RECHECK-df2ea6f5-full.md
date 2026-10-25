ACCEPT — df2ea6f51c45d6a7ac6023fd2f9bc7a821d58420 (nit fixes on 954580165a7a1ea9fd58812afc1f23cf71e9af70). Overall verdict on faf90280..df2ea6f5: ACCEPT. The package is exploratory research with no manuscript change.

This was a read-only check: nothing was committed or pushed, and the clone stays clean at HEAD df2ea6f5. Scratch outputs are in this directory: `window.py` / `window-output.txt` and the replay logs under `replay/`.

## The author's claims, each checked

| claim | verified | how |
|---|---|---|
| single parent 954580165a7a1ea9fd58812afc1f23cf71e9af70; only `bh01_access_v1/` changed | yes | `git log`; no changed path lies outside the package |
| PLAN.md byte-identical | yes | blob d8326165 unchanged since faf90280 |
| mutants.py and mutants-output.json unchanged | yes | blobs 69ca71b3 and 459f7f32 are identical at both commits |
| preregistered verdicts A–E, `overall` and `item_F` unchanged | yes | no claim verdict changed; `overall` and `item_F` compare equal |
| result.json leaf diff is 3 added leaves under `/claims/C3/post_review_W_autonomous`, plus `verdict_text` (14 → 15 lines) | yes | the 3 leaves are `bears_on_C3_verdict`, `note` and `post_review_verdict`; nothing else is added, removed or changed |
| REPORT.md generated block equals `verdict_text` | yes | exact match |
| replay byte-identical under -B and -O | yes | recipe from an empty directory: both runs exit 0, result.json matches the committed file, `cmp` passes, `sha256sum -c` gives 8/8 OK |

The first three nit fixes:

- **Nit 1 (C3 verdict wiring).** The W-autonomous check now has its own `post_review_verdict`: HOLDS iff 0 record-distribution violations, 0 failures to recover, and more than 0 maps. It is marked `bears_on_C3_verdict: false`. The C3 verdict is still computed from the preregistered product-map check. The generated text shows the two as separate lines, and the proof note says the same.
- **Nit 2 (ch19 L334).** The row is reclassified as "holds under unstated conditions (H-scramble)", and the entry notes that it disagrees with ch19 L72.
- **Nit 3 (L12 proposal).** It now points to item F for its decoupling condition and says that condition "the manuscript does not presently establish".

## Nit 4: the turnover-window arithmetic, checked exactly with rationals in `window.py`

1. **Lower bound on t_evap.** The package's own bound, at Γ ≤ 1000 and π ≥ 333/106, satisfies t_lo ≥ 1.785×10^76 s. True.
2. **Bound on x.** x = t/t_evap ≤ 10^19/t_lo < 5.61×10^-58. True.
3. **Mean-value step.** The function 1 − (1 − x)^{1/3} has derivative (1/3)(1 − x)^{-2/3}, which increases with x. So the fractional mass loss is at most x/(3(1 − x)^{2/3}). This step is valid.
4. **The stated bound.** I checked it exactly in two equivalent ways:
   - (x/(3Y))³ < (1 − x)², with x = 5.61×10^-58 and Y = 1.9×10^-58;
   - 1 − x > (1 − Y)³.

   Both hold. The value is about 1.87×10^-58, so "below 1.9×10^-58" is correct.

## Nit 5 (R3) and the mutant campaign

- **Nit 5.** R3 now says plainly that cumulative records are more than C1 and C2 need, and that D1's monotonicity is what needs them.
- **Mutants: not rerun, and not needed.**
  - mutants.py is unchanged.
  - The checks.py diff touches only the C3 entry in `decide()` and the C3 lines in `verdict_lines()`.
  - No function named in a control or mutant changed. The source-mutant anchors are each still present exactly once: the `is_bijection` docstring, `def main(argv):` and the `"verdict_text": lines,` line.
  - The K6 baseline is covered by my own -B/-O replay.

## Hygiene

- No absolute paths, secrets, e-mail addresses or session paths in the package.
- `tools/duplicate_check.py`, `tools/voice_check.py` and `tools/artifact_placement_check.py` all print OK.
- The worktree was unchanged afterwards.

No remaining findings.
