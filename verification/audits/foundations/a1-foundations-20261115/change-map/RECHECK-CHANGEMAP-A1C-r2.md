# Recheck of change map A1C r2 against the review of r1

**Reviewer.** The same independent, non-author reviewer as for r1. Paper-only: nothing in the repository was edited, committed, pushed or posted; no Lean, build or guard run. Read-only text searches and small read-only scripts were run against the worktree of `main` at `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6`.

## Verdict

**NOT CONFIRMED** — narrowly.

The good news first. All 31 findings of the review are applied at their stated r2 locations, and the fixes for the three blocking findings (F1–F3) are correct. Both corrected applications are sound: F18 (I-06 becomes NC under F21) and F28 (P-05 moves to F.2). The rows added in r2 pass the fidelity tests. The re-tagging under F11 follows the owner's split, and the counts are right.

Three new defects remain, each a small local text fix (R1–R3 below). One of them (R2) is my own error in r1, which r2 applied as I wrote it. With those three edits the map would be **CONFIRMED WITH NITS**.

***

## 1. The 31 findings at their r2 locations

| Finding | r2 location | Result |
|---|---|---|
| F1 (blocking) | M-31 | **Fixed.** Only the subject changes ("For a finite reversible realization"); the Hamiltonian clause stays as written. Main:453 is NC. |
| F2 (blocking) | M-08, K-ch01-38, R-03, D-2a | **Fixed.** No clause is added to Lemma 3. K3 is kept only after comparison with `determinism_reversibility_selected_measure` (`[Fintype S]`, `Equiv.Perm S`); otherwise the level is lowered or the delta recorded. The new statement (determinism; a bijection on a finite reversible realization; the counting measure as the realization's default prior) matches the Lean hypotheses as far as I can read them. |
| F3 (blocking) | G-12 | **Fixed.** "…and the structural assumptions A2–A6), in the reconstruction theorem's finite setting". Finiteness is not added to the commitments; A4 is referred to OQ-6. |
| F4 | M-41 | Fixed. Deletions only; nothing is added. |
| F5 | M-37, M-54, M-57, M-58, U-33, U-34, U-35, Y-11, K-ch01-16/183, K-ch03-40/162/180/186, K-appc-32/34, K-gl-19 | Fixed. Every site I listed has a row. M-58 :402 is NC with an adequate reason: it restates the theorem's hypotheses in the same paragraph. |
| F6 | T-04b, K-ch02-120, K-ch03-58/62, K-ch18-186/188/190, K-ch14-92, G-01b, M-59, M-60, K-ch05-41/95 | Applied. K-ch14-92 is wrong, through my own r1 error: see R2. M-59: nit N3. |
| F7 | M-11, K-ch01-41, K-ch02-16, K-ch07-12…161, K-ch09-129, K-ch18-122/138, K-ch19-22/30/72 | Applied, and OQ-4 is withdrawn. K-ch02-16 is correct. M-11 and its mirror K-ch01-41 introduce a contradiction: see R1. |
| F8 | D-2a to D-2f | Fixed. Every entry I named is present with the right level and action. |
| F9 | D-1a, D-1a′, D-3e, D.4, OQ-3, G.3 | Fixed. |
| F10 | U-09a, U-09b, W4, OQ-6 | Fixed (owner question; see §4). |
| F11 | the M-02/03/12/13, I-01, K-pref-3, K-ch00-53, K-ch01-93 a/b rows; OQ-1 | Fixed (see §3). |
| F12 | G-03, K-ch09-14/42/61/84/118, K-appa-111/117, OQ-2 | Applied: the recommendation is now (b), the dependent rows are held, and K-ch09-118 is split. The option (b) wording at G-03 overreaches: see R3. |
| F13 | D.5, OQ-5 | Fixed. The counts match my grep. |
| F14 | S-05, S-07 | Fixed. |
| F15 | K-ch14-90/268 | Fixed at :90 and :268. :92: see R2. |
| F16 | S-20, U-38, K-ch04-116/166, K-ch05-194, K-ch06-10, K-ch18-198/208, K-ch19-80 | Fixed. ch18:208 is NC, correctly: it already names the counting prior. |
| F17 | M-10 (6), (7) | Fixed. The Bell ceiling theorem is in the list, and the prong-input clause is kept. |
| F18 | I-06 | **Correction accepted.** With I-06 NC (F21), no span edit is needed. |
| F19 | header | Fixed. |
| F20 | E.2 | Fixed. |
| F21 | I-02 to I-08 | Fixed (nit N1). |
| F22 | M-10 (3), M-38, M-46, Y-02, U-06, X-03 | Fixed. G-03 waits on OQ-2. |
| F23 | M-36 | Fixed. |
| F24 | M-28, K-appb-451/454 | Fixed. |
| F25 | Y-04 | Fixed. |
| F26 | M-42 | Fixed. |
| F27 | K-appb-12/22 | Fixed. |
| F28 | P-05, F.2, G.4 | **Correction accepted.** Moving the row to F.2 is the right handling of a question that reading did not settle. |
| F29 | D-3e | Fixed. |
| F30 | M-19 | Fixed ("in the slow-bath regime"). |
| F31 | C-9 | Fixed. |

## 2. Rows added in r2: fidelity

**Quote test.** Every quoted fragment in Parts A–D of r2 (318 fragments) was tested against its stated file and line at `e4c6ba7f`. 37 did not match literally. On inspection:
- most are formatting (`\lvert` against `|`) or paraphrased locators;
- M-58's quotations are wrapped sentences spanning Main:391–393 and Main:401–404, and the stated lines (:393, :402) are their ends, which is acceptable as insertion points;
- the I-02 to I-08 "Current" cells carry a shared placeholder rather than quotations (N1).

No added row misquotes the text.

**Decisions and claims.** All added rows narrow, scope or remove; none adds a claim, a premise or recovery credit, and none asserts or implies infiniteness:
- the Bell and cone rows insert the scope of Main:414 (1)/(2) and Main:362;
- the bijectivity rows apply Q5 (a);
- the reciprocity rows name the counting prior (Q6 (e));
- the D.2 entries are re-affirmations with the correct levels: `MAIN:L-3` K3, `MAIN:T-statement` SUM, `MAIN:L-non-permutation-witness` P, and the rest GAP.

**Register.** No §A.32 or §A.33 phrase, history phrase or all-caps word appears in the proposed paper text. The disclaimer phrasings named in F22 were removed. The book keeps "the framework does not posit …" in appendix C and ch18, where the essay register allows it.

## 3. The F11 re-tagging

The re-tagging is correct.
- **Kept in 2a.** The model-scoped headline sentences (M-02a, M-03a, M-12a, M-13a, I-01a, K-pref-3a, K-ch00-53a) are NC in 2a. Each is explicitly scoped ("one fixed finite reversible representative", "every bijective realization", "In finite reversible models"), and with M-01 the abstract no longer calls the system finite.
- **Moved to 2b.** Their deletions are 2b options under OQ-1.
- **ch01:93 split.** The split is right: the sentence is unscoped, so its W2 scoping is 2a (K-ch01-93a), and the re-scoping of the chapter's central result is 2b (K-ch01-93b).

**Headlines left unnarrowed in 2a.** I re-scanned the openings and abstracts of every paper (first 30 lines), plus Main:80, the preface, ch00:53 and ch01:93, for an unsupported reading for nature that 2a leaves unnarrowed. I found none:
- Medicine:13 and Bioinformatics:14 are narrowed by D-01;
- Main:28 and Main:66 are A1-free;
- SM:14/20, Substratum:14/16/22, Complexity:21/27 and Computation:21 are covered by their rows.

## 4. The owner questions

**OQ-1.** Genuine. The options are right, the root trace is now correct (Step 1 stays in Main under every option), and recommendation (a) for this unit is sound.

**OQ-2.** Genuine, with correct options and a sound recommendation of (b). But the option (b) wording at G-03 drops "finite" from the Tier 1 framing (R3).

**OQ-3.** Genuine, with correct options; recommendation (a) is sound.

**OQ-5.** Genuine; the premise is corrected and recommendation (a) is sound.

**OQ-6.** Genuine, and stated honestly. It quotes both owner texts: the adopted Q3 (a) option text, which includes restating A4, and the qualification "Preserve finite periodic lattices where explicitly used as model conditions". The "class of finite models" rule is consistent with the qualification, because A4 sits among the "restrictions on the class of candidate substrates" (Sub:90) and Methodology:345 reads it so. It is **not** consistent with the literal option text, which is why it must go to the owner; the map presents it that way.

Recommendation (a) is defensible. One addition is needed (N4): under (a), the framework's specific representative stays a finite model through A4, so the sentences that name "OI's specific representative" or "OI's substratum" (Structure:134, :741, SM:14, :20) are statements about that finite model. The rule "no sentence presents A2–A6 as posited of nature" is asserted in W4, but it is not checked row by row for those sentences.

## 5. New errors, and the recount

### Required (must be fixed before the map is confirmed)

**R1. M-11 (Main:64) and K-ch01-41 assert and disclaim in the same remark (§A.30).**
*Evidence.* The new opening keeps "…is not an exotic commitment peculiar to this framework but the orthodox assumption of mainstream physics, imported here rather than invented", now with "the bijectivity of the constructed realizations" as its subject. The same remark then says "reversibility of nature's dynamics is not adopted as a postulate". Mainstream physics' assumption concerns nature's dynamics, so the remark first says the assumption is imported and then says it is not adopted. The book mirror (ch01:41: "the standard assumption of mainstream physics … The framework assumes no more than standard physics") has the same problem. No guard pins these phrases.
*Fix.* Opening: "The bijectivity of the constructed realizations — equivalently, that they conserve information — mirrors the orthodox assumption of mainstream physics rather than an exotic commitment." Delete "imported here rather than invented". Apply the same to ch01:41. The Remark title "(reversibility as the conservative assumption)" should match, for example "(reversibility and the orthodox assumption)"; check the title against the census and guard first.

**R2. K-ch14-92 misdescribes its paragraph. This is my r1 error (F6).**
*Evidence.* ch14:92 is the "exotic physics" paragraph. Its closed routes are closed timelike curves, excluded by deterministic dynamics, and naked singularities, excluded by bounded coupling degree. Neither exclusion uses finiteness. The r2 text "The arbitrary-precision route is closed by the lattice's finite site resolution" substitutes a route the paragraph does not discuss.
*Fix.* K-ch14-92 → NC. If any change is wanted: "These routes are closed by the framework's structural commitments". The :90 and :268 rows stand as drafted.

**R3. G-03 under OQ-2 (b) drops "finite" from the Tier 1 framing while Tier 1 still contains a finite-counting result.**
*Evidence.* Tier 1 includes "the classical horizon temperature of the boundary count", which GR:58 derives by restricting "the finite total system" to an energy shell. Option (b) as written names the shell counting as a condition only for "the results built on these". It also changes "for any finite deterministic system" to "for any deterministic system", so Tier 1's first item would be claimed without its hypothesis.
*Fix.* Under (b), either keep "finite" for the counting item ("…for any deterministic system meeting the four conditions …, the classical horizon temperature of the boundary count for a finite total system or under the shell-counting condition, …"), or add the shell-counting condition to that Tier 1 item explicitly. Mirror the fix in OQ-2's description of option (b) and in K-ch09-118's held sentence.

### Nits

- **N1.** I-02 to I-08 carry a shared placeholder in "Current" instead of locator quotations. Quote the sentence at each line so the NC can be checked.
- **N2.** S-16 still says "Uses of Theorem 19 elsewhere in SM … are mapped as a Stage 2 task, Part G item G-9". That is stale: S-20 now maps them and G.4 no longer lists G-9.
- **N3.** M-59 (Main:86): "By Lemma 3, the canonical choice is the Liouville measure". After M-08, Lemma 3 concerns finite realizations. Write "By the continuum form of Lemma 3's selection (Main:86's own parenthesis), …".
- **N4.** OQ-6 (a): state that under (a) the representative named at Structure:134, :741 and SM:14, :20 is a finite model through A4 (§4).
- **N5.** K-ch01-41: "of nature's dynamics injectivity on states that differ in registered content is established". Main's own wording (M-10 (7)) is "is the record requirement above"; use the same wording, per Q5's qualification.

### Recount

- **Rows.** Part A 318 (309 stage 2a, 9 stage 2b), Part B 21 (20 / 1), Part C 11, Part D 17. The total is **367**: 357 stage 2a and 10 stage 2b. U-09b is counted as 2a, as tagged ("2a under OQ-6 (b); otherwise 2b"). The map's header is confirmed, and no row ID is duplicated.
- **E.1.** R 95, R− 6, M 4, D 32, which sums to 137. Confirmed.
- **Manuscript counts.** Thirteen ledger items; ch09 "six" → "five" at all three occurrences (ch09:104 once, ch09:118 twice); ch02:74 and :120. All correct.

## What I could not check

- Guard, census and coverage tools were not run. The K3 match for `MAIN:L-3` and every pin statement come from reading the source.
- The unsampled book rows added in r2 were tested by the quote check only, not read in full context.
- The reading of $e^{S}$ at Computation:142 (P-05) is still open, as the map says.
