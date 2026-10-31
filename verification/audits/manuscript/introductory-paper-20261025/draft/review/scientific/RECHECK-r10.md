# Re-check of Introduction r10 (diff-only, independent)

- **Branch and head:** `draft/oi-introductory-paper-20261025` at `74330267`. The review is read-only and its outputs are in scratch only.
- **Base:** `Introduction-r9.md`, sha256 `880ee98d…c552`. The match was verified, so r9 is unchanged.
- **Target:** `Introduction-r10.md`, sha256 `b87ef6f9…9830`. This matches the `SHA256SUMS` entry, as do the entries for `CHANGES-r10.md` and `build_r10.py`.

## 1. Reproduction

- `python3 -I build_r10.py Introduction-r9.md out.md` reported "applied 7 edits: title block; Weinberg VERIFY; T1; T2; T3; T4; T5", and `cmp` with r10 shows the files are **byte-identical**.
- `diff r9 r10` has exactly 7 change sites and nothing else:
  - the title block (r9 lines 1–4, 3 lines added);
  - T1 (r9 36–37, deleted);
  - T2 (r9 58);
  - T3 (r9 60);
  - T5 (r9 102);
  - T4 (r9 120);
  - Weinberg (r9 144).
- The diff has 8 added lines and 10 removed lines. **PASS.**

## 2. Trims

Page effect of each trim. Each variant was built from r9 with the title and Weinberg edits plus the listed subset of trims. The position is where "Code, data and formal verification" starts.

| Trims applied | "Code, data…" starts | Main text ≤ 12 pp? |
|---|---|---|
| none | p.13, line 7 | no |
| all five (= r10) | p.13, line 1 | yes |
| all but T1 | p.13, line 5 | no |
| all but T2 | p.13, line 1 | yes |
| all but T3 | p.13, line 1 | yes |
| all but T4 | p.13, line 5 | no |
| all but T5 | p.13, line 1 | yes |
| T1 + T4 only | p.13, line 1 | yes |

**T1 and T4 meet the page budget on their own. T2, T3 and T5 contribute nothing to it.**

- **T1 (the roadmap at the opening of §2): genuine transition and repetition. OK.**
  - "Where a law's memory must sit / what finite recurrence does with it" survives at r10:26 ("the content lies in where the memory of a law must sit (§2.4) and what finite recurrence does with it (§2.5)") and in the headings of §2.4 and §2.5 (r10:72, r10:90).
  - "Proofs are in the cited papers" survives at r10:26 ("Proofs, the status ledger and the probe code are in [Main]") and r10:28 ("The results of §3.2–§3.3 are proved in [GR] and [Main]").
  - "Three classes … coincide" is r10:42–54 itself.
  - No hypothesis or qualification is lost.
- **T2 ("[Main] writes Theorem 1 as $S\iff D\iff Q_{\mathrm{fb}}$"): nonessential notation cross-reference. OK.**
  - The mapping $\mathsf Q_K\leftrightarrow Q_{\mathrm{fb}}$ remains legible from the Lean names, which are paired with their inclusions at r10:56 (`D_imp_Qfb` with $\mathsf D_K\subseteq\mathsf Q_K$, `Qfb_imp_S` with $\mathsf Q_K\subseteq\mathsf S_K$) and at Appendix A r10:212.
  - No $Q_{\mathrm{fb}}$ or $S\iff D$ notation is left in r10's prose that would need it.
- **T3 (the theorem label dropped from "[Main §3.4, Theorem (finite-horizon stochastic–reversible–unitary equivalence); EGGH26, Prop. 13]"): recoverable, but a loss of citation precision with no page benefit. Nit.**
  - The theorem's identity can still be recovered. The paragraph opens "For $\mathsf S_K\subseteq\mathsf D_K$", which is an inclusion of Theorem 1, and Theorem 1's label at r10:50 carries the same name with [Main §3.4].
  - But [Main §3.4] is not a section holding two theorems. It holds about a dozen theorem-level results (papers/Main.md §3.4: C2 necessity ×2, intervention dilation, C3 necessity, finite-horizon process dilation, the equivalence, finite operational realization, uniform continuum realization, unavoidable hidden predictive memory, canonical predictive quotient, plus lemmas and propositions).
  - The next sentence (r10:58) cites [Main §3.4, Theorem (finite-horizon process dilation)] with a label. The unlabelled citation directly beside it therefore reads as less specific than its neighbour.
  - Main's proof of S ⇒ D (Main:532) points to "the response-table construction of §3.4", which lives under the process-dilation theorem's extension (Main:498). A reader of a bare [Main §3.4] can therefore land on the wrong theorem.
  - T3 is not needed for the page budget. r10 with T3 reverted builds to 17 pp, with "Code, data…" at the top of p.13, 0 overfull boxes and 0 missing characters.
- **T4 (the label dropped from Theorem 4's citation): within the rule, with a caveat for the record.**
  - The removed text is literally the label repeated inside its own citation. The theorem name "operational-completion characterization" still stands immediately before [GR §3.3], and it matches GR's heading verbatim (GR:216, "**The operational-completion characterization.**"; GR:218, "**Theorem (operational-completion characterization).**"). So the reader can still find the theorem in a section titled "Gauge-fixing and the dimensional obstruction".
  - The explicit "Theorem (…)" pointer was added in response to the editorial review (`review/editorial/REVIEW.md:173`, applied in r2 as F10). T4 reverses that fix, and CHANGES-r10 does not say so.
  - Note that the Intro's labels are not uniformly source names. Theorem 3's label, "recurrence and overlap", is not a theorem name in Main. So the convention alone does not tell a reader that Theorem 4's label is GR's name.
  - T4 is load-bearing for the page budget: without it, 4 lines of §6.4 spill onto p.13.
  - **§A.34 is unaffected.** r10:120 is byte-identical to r9. The two directions are cited separately: ⇒ `physical_of_exactAll` (`OIBridge/PhysicalCharacterization.lean:301`, `ExactAll… → PhysicalCompletionConditions`) and ⇐ `exactAll_of_physical_general` (`OIBridge/GeneralCarrier.lean:93`, `PhysicalCompletionConditions → ExactAll…`). Both were verified at the cited lines, and both are also listed at Appendix A r10:218.
- **T5 (the Appendix B pointer): genuine repetition. OK.**
  - All three items are kept.
  - The removed phrase "with its classical and quantum scope" is stated in full at B.3 (classical stochastic on card inputs; entanglement-breaking one-step channel; classical-memory decomposition; no Bell violation) and at §6.2 item 6 (r10:180).
  - "Memory without short-window indivisibility" now matches B.2's heading verbatim (r10:234).
  - T5 does not affect the page count.
- **No limitation, hypothesis, evidence qualification or argument is removed by any trim.**

## 3. Title

- The words are unchanged. r9's `# Observational Incompleteness: From Deterministic Dynamics to Quantum Observations` became a pandoc `%` title block with the identical string, and the author and date are unchanged. The Status and Classification lines are kept.
- Every occurrence of "observational…incompleteness" in r10 was checked:
  - r10:1 and r10:14 (the §1 heading) read "Observational Incompleteness".
  - r10:12 and r10:22 read "Observational incompleteness (OI)" in sentence-case prose. This is unchanged from r9 and is ordinary sentence case.
  - There is no hyphenated variant, and no "observational-" or "-incompleteness" anywhere in r10.
- **PASS.**

## 4. Weinberg marker

- The marker (r10:142) states the source "is not read first-hand and is not treated as verified".
- It gives the reasons: APS is paywalled, and the UT ScholarWorks copy (hdl 2152/61094) is blocked by its bot check. Both agree with `review/references/FINDINGS.md` (lines 19, 36, 38–46).
- The guarded sentence (r10:143, the zero-point sum about 120 orders above the observed density) is byte-identical to r9 and carries no citation key.
- "Weinberg" occurs in r10 only inside the marker, and there is no Weinberg entry in the bibliography. Nothing is attributed to Weinberg.
- **PASS.** Two observations for the owner are in findings 3 and 4.

## 5. Build

The build used `pandoc r10.md -s --pdf-engine=xelatex --include-in-header=tools/unicode-fix.tex` (the repo copy), plus a direct xelatex run ×2 on the emitted `.tex` to obtain the log.

- r10 is 17 pp, with **0 overfull boxes and 0 "Missing character"** (3 underfull boxes, the same as r9).
- The title sets on three centred lines: "Observational Incompleteness: From / Deterministic Dynamics to Quantum / Observations". There is **no hyphenation**. The PDF Title metadata is the full unhyphenated string.
- In `pdftotext -layout` output, §6.4 ends at **p.12, line 40** and "Code, data and formal verification" starts at **p.13, line 1**. So the main text is ≤ 12 pp, which agrees with CHANGES-r10. The margin is about 2 lines.
- For comparison, r9 had "Code, data…" at p.12, line 39.
- **PASS.**

## 6. Register (§A.32/§A.33) on the 8 added lines

- **Phrase families.** A scan for meta-commentary, reader instruction, self-assessment, label-restating and revision history ("now", "no longer", "formerly", "withdrawn", "current form", "corrected form", "as redefined", "earlier", "previously", …) found **0 hits**.
- **Caps.** The only ALL-CAPS words, VERIFY and FINDINGS, are inside the HTML comment. Rendered prose has none.
- **`tools/voice_check.py`.** Run with r10 and the added lines placed under a scratch `papers/`, it reports OK.
- **PASS.**

## Findings

1. **(Nit) Revert T3.** Restore "[Main §3.4, Theorem (finite-horizon stochastic–reversible–unitary equivalence); EGGH26, Prop. 13]".
   - The trim does not contribute to the page budget: r10 with T3 reverted keeps "Code, data…" at the top of p.13, with 0 overfull and 0 missing.
   - It removes the only theorem-level pointer into a [Main §3.4] that holds about a dozen results, next to a sentence that keeps its own label.
2. **(Nit, record only) T4 reverses the editorial fix of `review/editorial/REVIEW.md:173` (r2 F10). CHANGES-r10 should say so, and should say why findability survives:** the label name stands before [GR §3.3] and matches GR:216/218 verbatim.
   - T4 is needed for the page budget, together with T1.
   - §A.34 directional witnesses are unchanged and verified.
3. **(Owner question) The Weinberg landing gate.**
   - r9's marker was an OWNER *landing gate* ("to be read first-hand … before the paper lands"). r10 reclassifies it as a VERIFY marker whose text no longer says it gates landing.
   - Under the r9 README (lines 139–146), the remaining VERIFY markers for unreachable sources do not gate landing. The reclassification therefore silently moves Weinberg into the non-gating class.
   - It also means r9's README still lists "Weinberg 1989 must be read first-hand (owner gate)".
   - The owner's words ("not treated as verified until … checked") are satisfied. The owner should confirm whether the gate still blocks landing, since the guarded empirical sentence would otherwise land uncited.
   - Minor wording point: "cited for that sentence only once the source is read" can be misread as "cited only one time". "Only after the source is read" is unambiguous.
4. **(Nit) Status surfaces.**
   - Unlike the r9 draft commit, `draft/README.md` gains no r10 entry. It still lists title hyphenation as open (README:54, 143) and "three remaining VERIFY markers" (README:146), against four in r10.
   - CHANGES-r10's Method line names `S/paper/draft/scripts5/build_r10.py`. The committed script is `draft/scripts/build_r10.py`, as the commit message says.
   - Update both at r10's confirmation at the latest.
5. **Everything else verified clean:**
   - byte-for-byte reproduction, with exactly 7 edits;
   - T1, T2 and T5 are within the rule, with their content located in r10;
   - the title words are unchanged, with no hyphenated variant;
   - 0 overfull and 0 missing characters;
   - main text ≤ 12 pp;
   - the register check is clean.

## Verdict: **ACCEPT WITH NITS** (findings 1, 2 and 4 are editorial; finding 3 is an owner decision, not a defect of the edit)
