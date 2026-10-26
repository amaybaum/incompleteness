**ACCEPT at df2ea6f51c45d6a7ac6023fd2f9bc7a821d58420.** The overall verdict on faf90280..df2ea6f5 is ACCEPT, with no remaining findings. I committed and pushed nothing; the clone is clean at HEAD df2ea6f5.

Each of the author's claims checks out:

- **Commit shape:** single parent 95458016, and every changed path is inside `bh01_access_v1/`. PLAN.md is byte-identical (blob d8326165, unchanged since faf90280).
- **Mutants:** mutants.py and mutants-output.json are byte-identical to 95458016 (blobs 69ca71b3 and 459f7f32).
- **Verdicts:** none of the preregistered A–E verdicts changed, and `overall` and `item_F` are equal.
- **result.json diff:** exactly 3 added leaves under `/claims/C3/post_review_W_autonomous` (`bears_on_C3_verdict` false, `note`, `post_review_verdict` HOLDS), plus `verdict_text` going from 14 to 15 lines. The REPORT generated block matches it exactly.
- **Replay:** from an empty directory, both `-I -B` and `-I -B -O` exit 0. `result.json` is byte-identical to the committed file under both, and `sha256sum -c` passes 8/8.

How each nit was handled:

- **Nit 1:** the W-autonomous check now has its own verdict field. It holds only if there are 0 violations, 0 failures to recover, and more than 0 maps. It is marked as not bearing on C3, and C3's verdict is still computed from the preregistered product-map check alone.
- **Nit 2:** ch19 L334 is reclassified as "holds under unstated conditions (H-scramble)", noting the mismatch with L72.
- **Nit 3:** the L12 proposal now points to item F.
- **Nit 4:** I checked the turnover-window bound with exact rational arithmetic, and it holds.
  - The package's lower bound on t_evap is at least 1.785e76 s.
  - So x = 10^19/t_lo < 5.61e-58.
  - The mean-value step is valid: the derivative (1/3)(1−x)^{-2/3} increases with x, so the mass loss is at most x/(3(1−x)^{2/3}).
  - Both (x/3Y)³ < (1−x)² and 1−x > (1−Y)³ hold for Y = 1.9e-58. The actual value is about 1.87e-58, so "below 1.9e-58" is correct.
- **Nit 5:** R3 is now noted as more than C1/C2 need, and D1 is named as what needs it.

I did not rerun the mutant campaign. mutants.py is unchanged, and the checks.py diff touches only the C3 text in `decide()` and `verdict_lines()`. No function that a control or mutant targets changed, and the three source-mutant anchors are each still present exactly once.

Hygiene is clean: no absolute paths, secrets or e-mail addresses. `duplicate_check`, `voice_check` and `artifact_placement_check` all print OK, and the worktree was unchanged afterwards.

Files are in [local path removed]/:
- REVIEW.md
- window.py
- window-output.txt
- replay/
