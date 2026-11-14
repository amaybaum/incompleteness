# RESPONSE-r3: disposition of CONFIRM-r3 for G3 unit 1

**Review.** `verification/programmes/gravity/drafts/g3-offset-coupling-20261113/CONFIRM-r3.md`, on
branch `research/g3-offset-873-20261113` at `95681321`. It is a delta check of r3 at `b207fbaa` and
gives the verdict NOT CONFIRMED. It raises two blocking findings (C-1, C-2), three should-fix findings
(C-3 to C-5) and one reclassification (C-6). It accepts departure D-1 ((DZ)) and departure D-2 (the
"not read back" wording).

**Files.** `G3-UNIT1-r4.md`, `NOTES-r4.md` and this file are new. All earlier files are unchanged.

**References.** "r4:n" is a line of G3-UNIT1-r4.md. "r3:n" is a line of G3-UNIT1-r3.md. Corpus lines
refer to `main` at `c3b5f37a`.

## Summary

| Finding | Disposition | r4 location |
|---|---|---|
| C-1 | Applied, in the review's text | §0 r4:42–46; §3.2 r4:369; B5 r4:475–476, :526; §5 r4:564–566; R0 r4:575–578; O0 r4:633–634; O1 r4:651–654; F1 r4:665; F8 r4:672 |
| C-2 | Applied, with one added caveat (see below). Part 2's category becomes "conditional on (ii-L)". | §0 r4:47–56, :67–73; B5 r4:486–530; §4 r4:543; §5 r4:567–570, :580–582; O0 r4:630–644; O1 r4:651–654; F8 r4:672; AW-loop r4:690–699; Q7 and Q8 in NOTES-r4 §5 |
| C-3 | Applied, in the review's text | §2 r4:225–227; §3.1 r4:334–336; §3.2 r4:376–379 |
| C-4 | Applied, in the review's text | r4:45, :352–354, :526, :565, :577–578, :633–634, F8 r4:672 |
| C-5 | Applied | R0 r4:575–576; the (ii-S) bullet r4:475–476 is changed the same way |
| C-6 | Applied | F8 r4:672; r4:532–533 |

No finding is rejected.

## C-1: applied

- The review's replacement for Part 1 is used in §0 (r4:42–46) and §5 (r4:564–566):
  > "on the weak and loop readings of requirement (ii) ((ii-W), (ii-L)); under the strong reading (ii-S), which corresponds for the source to GR:400 Reading 2, (SI) follows conditionally"
- "Every reading" is replaced by "(ii-W) and (ii-L); excluded by (ii-S)" at:
  - the §3.2 ordering row (r4:369);
  - the B5 node verdict (r4:526);
  - O0 (r4:633);
  - F1 (r4:665);
  - F8 (r4:672).
- O1's clause for K_cpl^free now reads "unless (ii-S) is held" (r4:652).
- The contradiction with B5's own (ii-S) bullet was a defect of r3, and the finding is correct.

## C-2: applied

**Agreement.** C-2 is correct.

- GR:400 Reading 1 feeds back "the ∼m²H² piece … an epoch-differential (relative) effect in the sense
  of §8.3".
- §8.3 ties relative effects to classical microstate differences (GR:573) and puts absolute emergent
  levels on the other side (GR:575).
- So the corpus's use reconciles GR:400 with GR:346 through that identification. It does not admit a
  loop through absolute post-partition data.
- r3's "the corpus's use admits K_cpl^conv" therefore did not hold.
- Part 2 is restated in the review's text (r4:47–56; §5 r4:567–570). Its category is changed from
  "counterexample" to "conditional on (ii-L)", as the review recommends.
- The corpus-use bullets and the node verdict are replaced by the §8.3 analysis (r4:486–530).
- AW-loop is rewritten in the review's text (r4:70–73, :690–699).
- O0 (r4:630–644), O1 (r4:651–654), R0 (r4:580–582), the §4 row (r4:543), Q7 and Q8 (NOTES-r4 §5)
  are updated to match.

**One addition, not a disagreement.** The added caveat is at r4:505–508 and in AW-loop at r4:697–698.

- The piece Reading 1 feeds back is relative *between epochs*.
- GR:579 records that the relative/absolute rule does not fix how energy changes between epochs couple
  (electroweak and QCD), and AUDIT.md:55 records the same as item 2.9.
- By analogy, classing an epoch-differential vacuum term as relative in §8.3's sense rests on GR:400's
  statement, not on a derivation [P].
- The caveat strengthens the review's first qualification, that the reconciliation is conditional. It
  leaves C-2's conclusion unchanged: the corpus's use does not establish that it admits K_cpl^conv.
- It is marked [P] and is offered for the reviewer's check.

**The force of (ii-L).** The review's sentence "Whether that argument holds against self-consistent
fixed points is not established" is carried into:

- Part 2 (r4:54–56);
- the skepticism bullet (r4:522–524), which now gives it as the reason Part 2 is conditional and not
  derived;
- R0 (r4:581–582);
- O0, as an open proof question, separate from the owner's premise decision (r4:638–642).

## C-3: applied

- (DZ) is redefined in the review's text: "the source minus `T^cl` contains no dependence on
  `e_Z([r])`, with `T^cl` given by the classical assignment (P11, W1-0)". A sentence is added saying it
  is a property of the source map (r4:225–227).
- "At fixed `T^cl`" is dropped at r3:323–325. The violation is now stated as the term `−ρ_Z g` in the
  source minus `T^cl`, and K_dec is said to satisfy (DZ) (r4:334–336).
- "At fixed `T^cl`" is also dropped at r3:364 (r4:376–377). A conditional sentence on the existence of
  pairs `κ, κ′` is added there, citing GR:573 (r4:378–379).

## C-4: applied

The review's qualifier "world-equivalent to K_dec with Λ₀ left undetermined (the union over Λ₀), the
corpus's standing for Λ (GR:162, GR:334, GR:356)" replaces the bare phrase at:

- r4:45 (§0);
- r4:352–354 (on shell, case (a)). The reason is added here: at a fixed `Λ^free_1` the completion
  admits every `Λ_eff`. A statement that it is not world-equivalent to K_dec at one fixed `Λ₀` is also
  added.
- r4:526 (node verdict);
- r4:565 (§5);
- r4:577–578 (R0);
- r4:633–634 (O0);
- F8 (r4:672).

## C-5: applied

"At fixed `κ`" becomes "for the uniform term" in R0 (r4:575–576). The (ii-S) bullet had the same
defect for (DZ). It now reads "(SI) holds at fixed `κ`, and (DZ) holds for the uniform term"
(r4:475–476).

## C-6: applied

- F8 is reclassified as "ELABORATING (assumption-watch AW-loop: the GR:346 / GR:400 reconciliation is
  conditional on §8.3 and unstated)" (r4:672).
- The NEW-count sentence is corrected (r4:532–533).

## Delta table, r3 to r4

The ranges come from `diff G3-UNIT1-r3.md G3-UNIT1-r4.md`.

| r3 | r4 | Change | Finding |
|---|---|---|---|
| 1 | 1 | Title r3 → r4 | none |
| 8–10 | 8–12 | Header lists CONFIRM-r3 and RESPONSE-r3 | none |
| 36–49 | 38–56 | §0 two-part verdict | C-1, C-2, C-4 |
| 60 | 67–68 | Shared-data sentence: requirement (ii) excepted, per B5 | C-2 |
| 62–63 | 70–73 | §0 AW-loop | C-2 |
| 68 | 78 | Split bullet (K_cpl^conv: SI, SI′, DZ) | formatting |
| 215–216 | 225–227 | (DZ) domain | C-3 |
| 323–325 | 334–336 | K_cpl^conv's response to the shift | C-3 |
| 341–342 | 352–354 | On shell (a) | C-4 |
| 357 | 369 | §3.2 ordering row | C-1 |
| 364–365 | 376–379 | "What differs" for K_cpl^conv; pairs `κ, κ′` | C-3 |
| 461–462 | 475–476 | (ii-S) bullet | C-5 |
| 474–479 | 488–512 | Corpus-use bullets: §8.3 analysis, epoch caveat, absolute `e_Z` | C-2 |
| 482–483 | 515–517 | Reading 1 stipulation, consistent with GR:575 | C-2 |
| 486–487 | 520–524 | Skepticism: cost only if §8.3 fails; force of (ii-L) | C-2 |
| 489–493 | 526–530 | Node verdict | C-1, C-2, C-4 |
| 495–496 | 532–533 | Finding-count sentence | C-6 |
| 506 | 543 | §4 ordering row | C-2 |
| 525–531 | 562–570 | §5 verdict | C-1, C-2, C-4 |
| 536–542 | 575–582 | R0 | C-2, C-4, C-5 |
| 593–599 | 633–644 | O0 | C-1, C-2, C-4 |
| 606–608 | 651–654 | O1 | C-1, C-2 |
| 619 | 665 | F1 | C-1, C-3 |
| 626 | 672 | F8 | C-1, C-2, C-4, C-6 |
| 644–648 | 690–699 | AW-loop marker | C-2 |

Every other line of r4 is identical to r3.

## Checks

- No computation, build or script was run.
- The review records the repository checks passing at `b207fbaa`. They do not scan the drafts.
- The new files were scanned by hand for the barred path strings and words, and for history-voice
  phrases.
- Corpus citations that are new or re-used in r4 were re-read at `c3b5f37a`: GR:162, :334, :356, :358,
  :374, :400, :573, :575 and :579, and AUDIT.md:55.
