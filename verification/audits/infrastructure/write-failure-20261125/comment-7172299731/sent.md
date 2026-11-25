**Independent review of PR #1567 (focused review of r4) at `57ccccb35674a0046c6e3061bb7f83e45c6b637f`: reviewer text, verbatim.**

Reviewer: a Claude reviewer agent started with a fresh context, given only the review request and the commit; it wrote none of the reviewed work and made no GitHub or repository writes (owner decision at #1169 comment 7166418469). Redaction: no redaction. SHA-256 of the unredacted review text: `8ca9ad8feb64572eeb41422c5fe82956a9c8a08847b647582fd6cef160b7a4f4`. Writer responses, if any, are posted separately; acceptance is the owner's decision.

---- reviewer text begins ----

**Focused independent review of claims-checker redesign r4 (57ccccb3 against r3 29b21374), PR #1567**

**Verdict: ACCEPT WITH NITS.** None of the findings below blocks adoption. Corrections 1–4 and the `--main` default are implemented as the owner authorized them, and every reported number reproduces. The protection that corrections 1 and 2 add is narrower than CHANGES-r4 implies, and the owner should know that before adopting. Findings 1 and 3 ask for documentation only, not new mechanism.

## Reproduction (d)
Every output I re-ran is byte-identical to the published file:
- **Files compared:** `self-test.txt`, `controls-W.txt` (batch W SHA-256 verified), `compare.txt`, `exitcodes.txt`, `m2.txt`, `treeM-scan.txt` and the r4 summary JSON. Tree M was extracted with every `.md` file at 4c3ad079.
- **Controls:** all 195 have unchanged outcomes (67 exact / 54 blocked / 74 load, 0 MISS, 0 FPFAIL).
- **Batch W:** per rule 17 → 16 of 30; any rule firing 16 → 15.
- **Exit-code controls:** 73 of 73 hold. All 9 loophole probes exit 3 under r4; 4 of them gave 0 under r3.
- **M2:** 14,080 insertions, 0 PASS.
- **Review load at main 4c3ad079:** r3 256 → r4 234 (code C/A/P 158/68/8; 198 path–sentence pairs; 145 distinct texts; 22 files; 876 record-file REVIEWs). 36 of the 234 contain a hypothesis token; I confirmed that count independently.
- **Not re-run:** the injection runs, because of their cost.

## Silent PASS (e)
Silent PASS does not increase on any batch:
- earlier probes: 0 under both;
- author diagnostics D: 7 under both;
- batch W: falls by one (W-P-09).

In the injection run, three batch-W items gain 32 PASS between them. The author's explanation holds: the host paragraph was flagged under r3 through a bare head that correction 4 removes. I checked all 23 tree-M findings that r4 drops by reading their sentences. All of them were incidental matches ("finite-horizon", "background kinematics", "Euclidean KMS periodicity"), and none states a withdrawn claim.

## Findings (all non-blocking)

1. **Correction 2 checks the evidence text, and the record writer chooses that text.** It is implemented as specified, but it can be got around by choosing a wider span. These r4 probes give exit 0:
   - **Supposition:** the r3 supposition probe without its H-token, "The Hawking temperature $T_Q$ is state-independent, as one would expect.", with the evidence widened to "The Hawking temperature $T_Q$ is state-independent, as one would". The author's control uses this same sentence but only the narrow evidence "as one would expect", which is refused.
   - **Mention:** a quoted slogan that contains the match, with the same claim also asserted outside the quotation. The check asks only that the evidence contain some match of each set, not that it cover every occurrence in the sentence.
   - **Question:** a rhetorical "Why else would … be state-independent?" with the full clause as evidence.

   The r3 review's three record probes now give exit 3 because of correction 1, not correction 2. On sentences without an H-token, a misleading-qualifier record (for example "as one would expect") still depends on the reviewer's judgment. **Asked:** state this plainly in §5 and in CHANGES-r4. The line "the three probes give exit 3" should say that correction 1 refuses them.

2. **Correction 1 misses some ways of writing the H-token.** The pattern is `\bH-\w`. Lower case, digits and H-χ are all caught. These forms give exit 0:
   - `_H-slope_` (Markdown underscore italics: there is no word boundary after `_`);
   - `H‑slope` written with U+2011 or with an en dash;
   - `$H$-slope`;
   - a zero-width space after the hyphen.

   None of these forms occurs in active material at tree M, so nothing is exposed today. The fix is cheap: a lookbehind `(?<![A-Za-z0-9])` plus a class of hyphen characters, with invisible characters stripped. That arguably normalizes the existing token rather than adding vocabulary, but whether it is in scope is the owner's call.

3. **The residual the author reports (g) is confirmed, and it is wider than §5 says.** The documented control gives exit 0: a code-A finding, an `other-subject` record with evidence "It is", and H-slope only in the preceding sentence.
   - **Is it a loophole?** It belongs to the class of r3 finding 2: an `unrelated` record clears a claim qualified by a hypothesis, without a licence. It needs a false record, though, since "It" stands for T_Q. So it also sits within the reviewer-misjudgment residual. Documenting it and putting it to the owner is the right handling within the authorization.
   - **It is not limited to code A.** A code-C probe passes the same way: "Assume H-slope. Then the Hawking temperature $T_Q$ is state-independent in this regime.", with an `other-subject` record whose evidence is "Then", gives exit 0. Hypotheses assumed for a whole paragraph or section escape too.
   - **Size at tree M:** 0 code-A findings have an H-token in their window. 1 code-C finding has one in the preceding sentence (`papers/Substratum.md`, W-KDEG, "Coupling-degree minimization leaves the single-copy clause open").
   - **Asked:** §5 and owner question 1 should say that extending correction 1 to the code-A window closes only the anaphora part.

4. **Correction 3 (b) is correct.**
   - Rule identifiers are asserted unique.
   - An `other-subject` record for W-KDEG that cites its own subject is now refused.
   - My own probe confirms that W-KDEG records are checked against W-KDEG's own cues.
   - W-KDEG-ANSWER is checked against its own terms.
   - There are 0 W-KDEG-ANSWER findings at tree M.
   - **Side effect, harmless today:** with separate identifiers, a sentence that fires both rules now gives two findings, where r3 merged them by rule and position. No such sentence occurs at tree M.

5. **Correction 4 (c) adds no vocabulary.** I classified every pattern that changed between r3 and r4.
   - **Added inflections:** horizons; ratios, spectra, characters; formalisms, structures, rule (the singular of the existing "rules"), descriptions, behaviours; symbols, geometries, memories; values; conditions for; led to; couplings.
   - **Added rule phrase:** `substratum symmetr(y|ies)`, which comes from the rule's own bare template.
   - **Removed:** the bare heads `symmetr\w*` and `substratum` from W-BM-EUCLID, and bare `horizon` from W-GR-THERM-KIN.
   - **Nit:** the bare-head sweep covered only the three terms the r3 review named. `cubic`, `hidden`, `minim\w*` and `ignorance` remain as single words. Keeping them costs review load, not silent passes, but the text should say so.

6. **Documentation (f) and cross-references.**
   - §0 states the division of responsibility plainly, and the proto docstring repeats it.
   - M1 is dropped, and M2 and the injection run are restated as segmentation checks, as the owner described.
   - **Wrong references:** DESIGN-r4 lines 38, 52 and 159 cite §4 for content that is in §5. The proto docstring cites "DESIGN-r4 section 2" for changes listed in §1.

## For the adoption decision
- **Protection compared with r3:**
  - Every r3 record-loophole probe is closed, through correction 1 (H-token in the sentence) and correction 3.
  - One more batch-W item is caught.
  - Nothing that r3 caught is lost.
- **Review load:** 234 records at main. 36 of them can be cleared only by rewording or by an adopted licence. The load recurs whenever a flagged sentence or its window is edited.
- **What remains uncovered:**
  - rewording outside the frozen lists: 15 of 30 batch-W items still pass when any rule may fire. Independent scientific review is responsible for this class, as §0 now states;
  - misleading-qualifier records on sentences without an H-token (finding 1);
  - hypotheses that sit outside the flagged sentence (finding 3);
  - typographic variants of the H-token (finding 2);
  - reviewer misjudgment within the record bounds.

---- reviewer text ends ----

---
_Generated by [Claude Code](https://claude.ai/code)_