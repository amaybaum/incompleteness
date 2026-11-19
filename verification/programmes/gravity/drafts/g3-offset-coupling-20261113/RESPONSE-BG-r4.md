# RESPONSE-BG-r4: dispositions of CONFIRM-BG-r4 for G3 unit 2(b) r5

**Reviewed object.** `G3-UNIT2B-BG-r4.md` at `297ee246`.

**Review.** `CONFIRM-BG-r4.md` at `905b68cc`, ACCEPT WITH CHANGES.

**Revision.** `G3-UNIT2B-BG-r5.md` ("r5:n" is its line n), with `NOTES-BG-r5.md`.

All four findings are accepted. Each is applied with the review's replacement text exactly. Nothing else
changes beyond the title and one revision-history line (r5:1, r5:16–18). The outcome stands: (C), on
Reading G, case β, conditional on N5-G. Earlier files are not edited.

***

## DF-1. The "same kind" sentence is mis-scoped in the §8.3 branch

**Accepted.** The review's text, now at r5:603–608:

> "For the running channel in particular: without §8.3, a carve-out that admits it and excludes the
> witness must separate two quantities of the same kind, emergent vacuum energies depending on `H`
> through the mode count (U2Ar3:690–691). With §8.3, K3 makes it admit the witness's R-dependence too,
> which unit 2(a) found to be 'the same kind of piece that Reading 1 feeds back' (U2Ar3:692–693). The
> witness is then excluded only through its absolute part (above), and the separation needed is the
> relative/absolute one, which reduces to the counterpart question."

RESPONSE-BG-r3's description of the r4 sentence (RESP:80–82) is superseded by this. RESPONSE-BG-r3 is not
edited.

## DF-2. State the universal negative behind (B), and count F4-null in §7

**Accepted.**

- **Item 1**, now at r5:709–711:

  > "F4-null is CoC-content with respect to the witness's term (R-6). Its controls are not assessed here;
  > it does not decide the outcome while F5 is admissible, and it would have to be eliminated, with F5,
  > for (A)."

- **Item 2**, now at r5:222–223, after the "not shown to be exhaustive" line of §1.3:

  > "(B) through F4-c therefore requires showing that no class with a difference relevant to grounding
  > exists."

## DF-3. QB7(a): qualify the rejection by QB7(b)'s answer

**Accepted.** The review's text, now at r5:883–885 (QB7(a)):

> "If it is held, uniform F4 is rejected by (b2) wherever it excludes the channel: without §8.3, and with
> §8.3 unless the answer to (b) is a fixed-cell quantity. The outcome is then (C) with F4-c's K3 named."

- The following sentence, "It would be (B) only if no grounded carve-out exists", is kept as it was
  (r5:885).
- The same qualifier is applied at r5:112–114 (§0, r4:111) and r5:725–727 (§7, r4:714).
- QB7(b) is unchanged (r5:886–888).

## DF-4. F4-c's candidate classes: misfiled failure and mismatched reasons

**Accepted.**

- **Item 1**, now at r5:218–219 (r4:216–217):

  > "Partition-definedness covers `ρ_Z`, so it does not yield an F4-c; removing `ρ_Z` from it ad hoc
  > fails K3."

- **Item 2.** The same change is made at r5:594–595 (r4:590). The rest of that bullet is unchanged.
- **Item 3**, now at r5:70–71 (r4:69–70):

  > "has K3 undetermined, because the candidate classes examined fail and are not shown to be exhaustive"

- **Item 4.** NOTES-BG-r5 §3 states K3's reading as:

  > "K3 fails a carve for which no difference relevant to grounding is stated; each carve stated so far
  > is of that kind."

  This corrects the paraphrase at N4:49–53 and RESP:30–31, which are not edited.

***

## r4 → r5 diff

`diff G3-UNIT2B-BG-r4.md G3-UNIT2B-BG-r5.md` gives 11 hunks. r5 has 902 lines, against r4's 889.

| r4 lines | r5 lines | Change | Finding |
|---|---|---|---|
| 1; 16–17 | 1; 16–18 | title; revision-history line | bookkeeping |
| 70 | 71 | F4-c's K3 reason in §0 | DF-4 |
| 111–113 | 112–115 | §0 QB7(a) consequence, qualified | DF-3 |
| 216–217 | 218–219 | partition-definedness refiled | DF-4 |
| after 219 | 222–223 | universal negative for (B) | DF-2 |
| 590 | 594–595 | partition-definedness refiled (F4-5) | DF-4 |
| 598–600 | 603–608 | "same kind" sentence scoped by branch | DF-1 |
| after 700 | 709–711 | F4-null counted in §7 | DF-2 |
| 714–715 | 725–727 | §7 QB7(a) consequence, qualified | DF-3 |
| 871–872 | 883–885 | QB7(a), qualified | DF-3 |

**Owner questions.** The final text of QB1 to QB7 is at r5:851–888, in §11 "Owner questions": QB1 at
r5:853 and QB7 at r5:880–888.

**Checks.** `claims_check`, `staleness_check` and `voice_check` all exit 0 at `905b68cc`, and none of them
scans the drafts. The barred-string scan of the r5 files finds no hits. The worktree is clean.
