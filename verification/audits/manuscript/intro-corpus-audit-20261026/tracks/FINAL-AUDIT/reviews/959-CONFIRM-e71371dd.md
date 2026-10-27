## Final confirmation of PR #959 at `e71371dd53b805f78190aaad2004c95149986040`

**Verdict: CONFIRM.** Commit `64c20e7e` (parent `72eece11`) makes only the listed changes, each correct, and merge commit `e71371dd` (parents `64c20e7e` and main `4449b0d9`, #958) reverts nothing from either side. One optional nit remains.

**1. `git diff 72eece11 64c20e7e -- '*.md'` contains only the listed changes, and each is correct.**
- **Bioinformatics :56** now opens "Where the relevant structure lies in the hidden fibers, the … ceiling … explains why …".
- **Bioinformatics :186** now reads "…is what the ceiling predicts where the relevant structure lies in the hidden fibers".
- **ch17:**
  - :12 says "conditional".
  - :22 says "conditional ceiling would explain".
  - :76 says "outperform transcriptome-only methods".
  - :78 now reads "Where the strict gap holds, … bounds what any method recovers; … an amount not computed here". This removes the unsupported "structurally calculable" claim.
  - :210 opens "Where the strict gap holds".
- **ch15:** the :134 SQUID sentence is deleted, and :91 now says "sizeable". ch15 no longer states a magnitude anywhere that a section says none is derived.
- **GR :591** now reads "$K_{mL}=I$ for every $m\ge0$ … for some $mL>s$". The step is correct.
- **FULL** mirrors every book edit.

**2. No unconditional ceiling, gap or explains-failure claim remains in Bioinformatics or ch17.** I re-scanned both files sentence by sentence.
- **Conditioned on their own line or within their item:** :138, :142, :463, :465 and :467; (P1), (P4), (P6) and (P7); ch17 :14, :20, :30, :36, :40, :42, :70, :72, :78 and :210.
- **Predictions or definitions, acceptable as written:** Bioinformatics :455 (table), :469, :473 and :537; ch17 :36 (the definition), :74 and :220 (P2).
- **Optional nit:** ch17 :26 still summarizes "*both* a structural ceiling (what cannot be achieved with current approaches)". Adding "conditional" would match :12.
- **Not this claim class:** Bioinformatics :14 and :84, and ch17 :16, are about the memory / non-Markovian explanation, not the ceiling.

**3. The merge reverts nothing.**
- **Landing equals the PR's own diff.** The changed lines of `git diff 4449b0d9 e71371dd` over `*.md` and `verification/` are identical to those of the PR's own `git diff 55e3217b 64c20e7e`. The file set is the same, and both show 38 files, +719/−631.
- **#958 survives.** Every line #958 added is present at `e71371dd`: FULL 3, appendix-b 1, ch07 1, glossary 1, GR 2, Main 4, SM 1, Substratum 3.
- **No shared lines.** #958 and #959 touched no common lines in SM, GR, Main or FULL.
- **Both sets of text are in the sources and PDFs.** The SC-26 text is present in GR :591 ($K_{mL}$, "$m\ge0$") and SM :112 ("two time slices"). Sample #958 and #959 phrases appear in the Main, GR, SM and FULL PDFs.
- **Generated files.** For Main, GR, SM, Substratum, Bioinformatics, Complexity, Computation, Explainer, Structure and FULL, fresh pandoc output matches the committed `.tex` apart from the source-sha256 stamp, and every stamp matches its `.md`.

**4. Mirrors, gate and probe.**
- **Mirrors.** The chapter edits and the FULL edits in the landing diff are the same 96 lines. No chapter, appendix, preface or glossary line is missing from FULL.
- **Release gate.** Every step passes except `lean-axioms`, which fails only because there is no lake locally.
- **Edge probe.** `edge_rigidity_probe.py` reports ALL CHECKS PASS.

**Answers**
- **(a) Is every substantive claim supported?** Yes. Each claim is stated with its notion and its hypotheses, and the ceiling claims carry their open premise throughout.
- **(b) Is any established result unnecessarily weakened?** No. The conditional theorem at Bioinformatics :138, :463 and ch17 :14 is at full strength. SM :112 and GR :591 state the recurrence-cycle result with an exhibited partition and the extension proof.

I removed the worktree and my scratch files.
