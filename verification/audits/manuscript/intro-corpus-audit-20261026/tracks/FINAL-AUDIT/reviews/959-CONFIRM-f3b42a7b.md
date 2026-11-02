## Confirmation of PR #959 at `f3b42a7b45b0dd8c772320715dc9f41c6b9b498e`

**Verdict: CONFIRM.** `eb986b42` (single parent `e71371dd`) makes only the ch17 :26 change and its FULL mirror. `f3b42a7b` (parents `eb986b42` and `f92279af`; `f92279af` is on main with parent `4449b0d9`) brings in #956 without reverting anything from either PR, and the merged Explainer and Complexity read consistently.

**1. `git diff e71371dd eb986b42 -- '*.md'`.**
- It contains only ch17 :26 and the identical line in FULL. Otherwise the commit touches only the regenerated FULL `.tex` and `.pdf`.
- The new text, "*both* a conditional structural ceiling (what cannot be achieved with current approaches where the strict gap holds)", matches the conditional at ch17 :12, :14, :20 and :206. The scientific scope is unchanged.

**2. The landing reverts nothing.**
- **Landing equals the PR's own diff.** The changed lines of `git diff f92279af f3b42a7b` over `*.md` and `verification/` are identical to those of `git diff 4449b0d9 eb986b42`: 284 lines, same file set.
- **#956 survives.** Every line #956 added is present at `f3b42a7b`: Medicine 6, Explainer 5, Methodology 1, Complexity 1, ch00/05/14/19 one each, and FULL 4.
- **No shared lines.**
  - Explainer: #956 touched base lines 294, 707, 709, 856 and 948; #959 touched 135, 684, 1005 and 1033.
  - Complexity: #956 touched :27; #959 touched :370 to :492.
- **Both texts are in the PDFs.** Phrases from each PR appear in the Explainer and Complexity PDFs.

**3. The merged Explainer and Complexity agree.**
- **Explainer :294 (#956)** says "nontrivially so where the dynamics is P-indivisible, which on a fixed finite reversible representative holds across its recurrence cycle whenever a rooted visible map is not a permutation". This is the same scoping as #959's :135 and :1005.
- **Explainer :707 and :948 (#956)** say that positive conditional memory at an accessible order holds exactly when history readback holds at that order. This agrees with Main :20 and with #959's :135 and :1033.
- **Complexity :27 (#956)** says C1–C4 give "positive conditional memory at an accessible order" and that every finite law admits the representation. This agrees with #959's §7 and §8.9 wording.
- I found no adjacent contradiction.

**4. Stamps, mirrors, gate.**
- **Stamps.** For all eleven papers and for FULL, fresh pandoc output matches the committed `.tex` apart from the source-sha256 stamp, and every stamp matches its `.md`. The eleven papers are Main, GR, SM, Substratum, Bioinformatics, Complexity, Computation, Explainer, Structure, Medicine and Methodology.
- **Mirrors.** The chapter edits and the FULL edits in the landing diff are the same 98 lines, and no chapter line is missing from FULL.
- **Release gate.** Every step passes except `lean-axioms`, which fails only because there is no lake locally.
- **Edge probe.** `edge_rigidity_probe.py` reports ALL CHECKS PASS.

**Answers**
- **(a) Is every claim supported?** Yes. Each claim names its notion and carries its hypotheses, and #956's merged text agrees with #959's.
- **(b) Is any established result unnecessarily weakened?** No.

I removed the worktree and my scratch files.
