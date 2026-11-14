# Response to `REVIEW-r1.md` (findings F1–F9): disposition for `L54-r2.md`

`L54-r1.md` and `NOTES-r1.md` are unchanged. `r2:§n` refers to `L54-r2.md`. Citation forms are those
of `L54-r2.md`. Each finding was checked at the sources it cites before it was applied. Paper-only:
no computation on any OI rule or model; all arithmetic by hand.

## Findings

| # | Finding | Check at source | Disposition | Where in r2 |
|---|---|---|---|---|
| F1 | K1 is circular for C-POS-1 and C-POS-2 (it used Lemma 5 with the stated classification) and cites a proof failure, not a failure of (T), for R-nl | Confirmed. r1's entry inferred "(T) fails" from the argument under test. Lemma NA (S4:86–92) is about the proof; the conclusion's failure is S4:126, :181–185 | **Applied in modified form.** All three checks now rest on one fact outside the argument: a bijection preserves the multiset of atom probabilities. (i) C-POS-1: re-derived from its kernel (HA5:116–120, :128–135), including the hemisphere probability by hand; the reviewer's version, which cites "record laws equal the quantum branches" with Lemma 2 (i), was replaced by an atom count so that no lemma of the unit is used. (ii) R-nl: both rows of T3 recomputed by hand from the coefficients of `(1 + z + z²)^5`; multisets `{27, 90, 126}` and `{51, 51, 141}` differ. (iii) C-POS-2: done by hand from `finite-a2-v5/REPORT.md` (exact repeatability from the support of `ν_{sa}`; atom count for "`a`, `b`"). It uses one bound from the source record, the one-read coupling `κ` (FA2:150–164), read in full; its hemisphere input was re-derived, its cell-integration constants were not. Where `κ ≥ 1/4` the row's floor is at least `1/2` and the conclusion contradicts no stated classification (P:705–708). K1 is stated as green with that reliance named | §5 K1 |
| F2 | Headline statements omit load-bearing hypotheses; "closed" is wider than "fails Q5′" | Confirmed against r1 lines 23–29, 304–314 | **Applied in modified form.** The headline is the reviewer's eight-hypothesis statement (review §8) instead of the one-sentence replacement, so D4, the Lüders product target, the `ℓ = 0` reading with its fallback, H-∞, H-write and H-μ all sit in the blockquote. The outcome sentence is the reviewer's. "Closed" is removed everywhere; the class table states "fails Q5′, hence T1, under 1–7 [W]". The gate question, coarser record conventions and class D are stated separately as open or untouched. Proposition 2 carries (C) wherever it is mentioned | §0; §6 |
| F3 | "Theorem 1 implies FC-1 and FC-2" is false on `1/96 ≤ ε < 1/48` and at the tokens' `ε₀ = 1/50` | Confirmed (S3:128–129, :331–334; S4:328) | **Applied.** Proposition 2 implies the conclusions of FC-1 and FC-2 on the whole range `ε < 1/48`; Theorem 1 gives failure of Q5′ alone at `ε < 1/96`, says nothing on `1/96 ≤ ε < 1/48`, and does not reproduce the tokens at `1/50` | §5 K5 |
| F4 | Corollary 1a: adaptive prefixes in exchange mode; one weight vector; second check of the constant | Confirmed. Re-derived the extra line: in exchange mode the test labels are written after the prefix, so changing the second test label leaves `(r, h_1)` unchanged for every `u` and shifts `h_2` by a fixed element | **Applied.** The statement is the reviewed form (labels fixed in advance, one `w`, one assignment, AF:125–127), with the exchange-mode line for adaptive prefixes added and the second derivation of the constant credited to the review. The same line is used to extend Proposition 2 to heralded and adaptive witnesses in exchange mode; that extension is marked as derived once here and not reviewed | §4 Corollary 1a, Proposition 2; §8 item 7 |
| F5 | The Main:588 paragraph implies support inside the additive class | The reviewer is right: Main:588 concerns the continuously tunable state-mixing operation; Theorem 1 uses no gate | **Applied.** The two sentences relating the result to Main:588 are removed and replaced by the reviewer's text: the result does not bear on that statement | §6, Relation to Main |
| F6 | "NEW for TUNE-1" is defensible only relative to the TUNE-1 directory; the mechanism is on `main` | Confirmed at M1:424–427, OA1:369–375, :392, :365–367 and S2:238–244 | **Applied.** The three prior statements are quoted; what is added relative to them is listed (the invariant with a quantitative bound against `F(ε; 𝒯_R)`; the decision of the L5.4–L5.6 rows whatever the witnesses and laws; the two-read comparison of Proposition 2; Lemma 5). Classification under §A.31: Lemma 1 CONFIRMING; Theorem 1, Corollary 1a, Proposition 2, Lemma 4, Lemma 5 ELABORATING; nothing NEW. The assumption-watch marker on the L5 node tree is kept | §6, Prior art; §A.31 classification |
| F7 | The adaptive relabelling is triangular; Lemma 2 (i) does not extend | Confirmed with the reviewer's example (`z_1 = z_2` one fair bit) | **Applied** | §8 item 6; Lemma 1 |
| F8 | `ℓ = 0`: add S2:195 and S2:200 | Confirmed at both lines | **Applied** | §0 hypothesis 8; §1 reading paragraph; §8 item 1 |
| F9 | N7 verdict; Lemma 5 hypotheses; the word "closed" | Confirmed | **Applied.** N7 carries "under the identification of Lemma 4 (c)". Lemma 5 names D4, the Lüders target and `F` posed for the empty preparation; its hypothesis list was also reduced to 6–8, since its proof uses neither the rule nor H-μ. "Closed" does not occur in r2 | §3 N7; §4 Lemma 5; §6 |

## Coordinator items beyond the findings

- **Reviewer's observation (shared `x_O(τ)` under D4).** Assessed as correct and relevant; recorded
  in r2 §7, apart from the theorem. Re-derived: the statement and its constant (`1 − 2ε` on two
  configurations). Added there, each derived once and unreviewed: R2, the consequence for R-lin
  under a coset-uniform law (`|M_τ| ≤ 2` for `ε < 1/6`; failure at `τ = 1`, `q ≥ 3` when a site of
  `O` has a neighbour outside `O ∪ P`), and R3, one R-nl interface (`ε ≥ 1/18` in W-nl-2's
  interface, from table T3). The section states what this means for how Theorem 1 is read: it is
  not evidence that additivity is what separates R-lin from R-nl under Q5′.
- **Hypotheses in headline statements.** See F2.

## Declined

Nothing was declined. Two findings were applied in modified form (F1, F2), as stated in their rows.

## Not done, or done only partly

- The C-POS-2 control relies on the source record's one-read coupling bound without re-deriving its
  cell-integration constants.
- The exchange-mode extension of Proposition 2 and the items R2, R3 of r2 §7 are new in r2 and
  have had no review.
- Lemma 4 (c)'s identification of OA-2's objects with TUNE-1's remains an unreviewed reading.
- r2 is 521 lines; the 400-line aim set for r1 was not kept, because the full hypothesis list, the
  direct controls and the separate §7 were added.

## Additional reading for r2

`REVIEW-r1.md`, whole. `history-architecture-v5/REPORT.md` 1–70, 96–137, 190–210, 295–320.
`finite-a2-v5/REPORT.md` 1–300. `TUNE-1-STEP2-SESSION4.md` 60–200 (Lemma NA, Lemma M, tables T2 and
T3, W-nl-1, W-nl-2). `TUNE-1-STEP2-SESSION2.md` 188–202, 232–246. `OA-1-REPORT-r5.md` 352–392.
`TUNE-1-STEP2-PROPOSAL.md` 165–173, 199–205, 253–258, 857–862 (re-read). Commands: `ls`, `wc`,
`sed`, `cat -n`, `cut`, `grep`, `find`, `awk`; file assembly with `cat`. No interpreter was run in
this revision. Nothing in the repository or either worktree was edited, committed, pushed or
posted.

## Confirmation review (CONFIRM-r2.md)

`CONFIRM-r2.md` returned ACCEPT WITH CHANGES on `L54-r2.md` with five changes, C1–C5, to wording
and scope. Each was checked at its source and applied in `L54-r3.md`; `L54-r2.md` is unchanged. No
proof step changed. `r3:§n` refers to `L54-r3.md`.

| # | Change | Check at source | Disposition | Where in r3 |
|---|---|---|---|---|
| C1 | R2: "uniform on `V`" needs the uniform law, not any coset-uniform law, and the mode must be stated | Confirmed: a point mass is coset-uniform (S3:58–60). In exchange mode the shared slice is `O ∖ C` (P:155–157, :168–170) | **Applied**, text as given | §7 R2 |
| C2 | §7 assessment 2: Theorem 1 says nothing about R-nl; it shows every passing rule must lack (T) | Confirmed: Lemma 5 gives `dep(W_uu) ≠ dep(W_uv)` for a passing interface at `ε < 1/96`, so its laws are not coordinatewise bijective images | **Applied in modified form.** The reviewer's text is used except its last sentence. In place of a pointer into `CONFIRM-r2.md` §6 at this point, the sentence says the question is not decided in this document and points to the closing section §9, which is the one place r3 refers to the reviewer-authored material (coordinator instruction) | §7 assessment 2; §9 |
| C3 | State that hypothesis 7 (target with no persistent memory; comparison of complete-record laws) is load-bearing; L5.4–L5.6 are answered for Q5′ as AF defines it | Confirmed at AF:88–91, :107, :127–130; control K4 shows the invariant is unavailable at class level | **Applied**, text as given, with "as AF defines it" inserted in the sentence after the class table. The same qualification, and "nothing follows for R-nl", were also added to the closing paragraph of §0 and to the class-D bullet, so that the headline carries them | §6 "Left open"; §6 after the table; §0 |
| C4 | C-MEAS is a precedent for the test, not for the mechanism | Confirmed at `measurement-source.md`:87–127: the read leaves the signal unchanged and draws a fresh independent seed | **Applied**, all four replacements | §1; §6 prior art and classification |
| C5 | Nits: "hypotheses 1–7, with `F` posed as in 8"; two line references; the reliance sentences of K1 | Confirmed: "holds" is defined at P:705–706 and "applies" at P:706–709 | **Applied.** The reliance sentence is the reviewer's and appears once, in the C-POS-2 entry; the second sentence it replaced, after the K1 result line, was removed instead of repeating it | §0; §5 K1 |

**Also changed in r3.** The standing paragraph and §8 item 7 now record that the exchange-mode
extension of Proposition 2 and R1–R3 were checked once by the confirmation review, and that r3 itself
is unreviewed. A citation form `MS:n` was added.

**Reviewer-authored material (`CONFIRM-r2.md` §6).** Not imported. The rule-free lemma, the
non-additive example meeting Q5′ and the two-round additive example passing at class level are
listed in r3 §9 as reviewer-authored and pending independent check, with only what that section
claims; they were not re-derived, and Theorem 1 and its proof do not rest on them.

**Additional reading for r3.** `CONFIRM-r2.md`, whole. `oi-qm-ext-1/measurement-source.md` 84–128.
`TUNE-1-STEP2-PROPOSAL.md` 703–712 (re-read). Commands: `ls`, `wc`, `cat`, `sed -n`, `cut`, `grep`,
and two Python text substitutions that build `L54-r3.md` from `L54-r2.md`. No computation on any OI
rule or model. Nothing in the repository or either worktree was edited, committed, pushed or posted.

**Scope wording (coordinator instruction after C1–C5).** Applied as a small edit to `L54-r3.md` and
`SUMMARY-r3.md`: the headline conclusion reads "classes A, B and C fail Q5′ under its specified
target and record conventions", stated in a headline line, in §0, in §6 and in the summary; every
place that says L5.4–L5.6 are answered carries that scope. The standing line gives the review state:
r1 reviewed (ACCEPT WITH CHANGES), r2 confirmed (ACCEPT WITH CHANGES, C1–C5), r3 applies C1–C5 and
is itself unreviewed; the reviewer-authored §6 results are under separate independent check and are
not part of the theorem.
