Independent read-only review of DESIGN-v5 (commit-independent ledger and terminology verification tool): bounded delta review

Verdict: ACCEPT WITH REQUIRED CORRECTIONS

Reviewer: the same independent, non-author subagent session that wrote review-v4. It wrote no part of DESIGN-v1 to v5.

The review was read-only:
- no change to the checkout;
- no git, GitHub or workflow action;
- every file written is new, under `D/review-v5/`, where D = <records>/coord2-ledgertool-design.

Recounts used my own scripts (`rv5_*.py`, plus my v4 helpers `rv_git.py`, `rv_prof.py` and `rv_hp.py`, copied unchanged). They read git objects only. I did not read or run any file in `work-v5/`. Date 2026-11-23.

Goal link (sec. A.47): A1-EXIT (#1169), the exception-free verification route. This review decides whether DESIGN-v5 meets the owner's acceptance criteria for the corrections of review-v4. It adopts no rule, record or count.

Input hashes (verified before any work; all match)

- DESIGN-v5.md 6693e5dd4dd2a0059e88a21091b979dfc36680e25e54960b9699d2a2f2972982
- CHANGES-v5.md 9e0efa6dda27d3441507c47e5c469ae324a7794c7a6b57d3165ba8af0e95e923
- review-v4/review-v4.md 113d1c129ad761114a4b529c5ec90d6d79a224d468bffa0cbe7b3cfd922cca6f

Summary

The decisive gate, V3, is met:
- all 95 retired A1 lines at H are FAIL under the proposed item-7 check;
- both directions of control hold.

V1, V2 and V4 to V8 are confirmed, and every figure the writer labels WN reproduces. Two items do not fully meet the owner's terms for points (b) and (c):

- (b) The design records the lost synthetic coverage for V4 and V15 only. One further constructed string that DR-2 caught before now PASSes, and it is not recorded (W1).
- (c) The writer explains the 4671-versus-4657 difference as a difference in refs. It is a difference in search method. The two searches together cover 4677 distinct blobs, and none matches DR-1d, DR-2 or DR-3 (W2).

Both corrections are text only. No count or rule changes.

***

Criterion 1. V3: no regression of item 7 (decisive gate)

My recount (`rv5_item7.py`) runs the proposed check (sec. 11 note 1) with no records. A line is a deny line when a deny rule matches it at line level. It is a `final-unclassified` line when it is a `ptr` or `count-grep` hit and no deny rule matches it.

| Figure | Writer | Mine |
|---|---|---|
| H: deny lines | 86 | 86 |
| H: `final-unclassified` lines | 123 | 123 |
| H: FAIL lines in all | 209 | 209 |
| T1': deny lines | 0 | 0 |
| T1': `final-unclassified` lines | 12: 7 W1, 4 W2, GR.md:58 | 12, the same lines (SM.md:1394, ch09:137, ch19:198, ch19:212, FULL:2554, FULL:5270, FULL:5284, FULL:5914, FULL:5925, appendix-b:235, appendix-b:246, GR.md:58) |
| Retired lines at H with no deny match | 95 | 95 (93 `ptr` only, 2 `ptr` plus `count-grep`) |
| The 95 among the FAIL lines | yes | yes, all 95 among the 123 |

- **Both directions.** V23 and V24 FAIL with `--final`:
  - ch02-substratum.md:136 at H is one of the 95 and matches no deny rule;
  - "six structural hypotheses" is a `count-grep` hit and matches no deny rule.

  V25 covers the other direction:
  - without `--final` they are REVIEW;
  - a W2 line with its rule passes;
  - a `resid`-only hit stays REVIEW.

  At T1' none of the 95 lines exists, and the 12 remaining hits are the ones that pass once their rules and record exist. The original's hard failure is preserved for every `\bA1\b` and posit-count line. V3 is resolved.
- **Definition (O8).** The 86 counts line-level deny matches only. If each line of a multi-line sentence that a deny rule matches is also counted, H has 93 deny lines and 216 FAIL lines; the 123 does not change. RT-I7A should state which definition its 86 and 209 use.

Criterion 2. Deny rules after V5-D1

- **DR-1d and DR-2 are out of the active set and preserved.**
  - Sec. 6.1 and 6.4 list only DR-1a/b/c, DR-3, DR-4 and DR-5.
  - Sec. 6.4.1 records each rule's purpose and its exact v4 pattern. I checked both patterns against v4 sec. 6.4; they are byte-identical apart from the table escapes.
  - Their ids are retired.
- **Counts with and without the two rules** (`rv5_dr.py`). Distinct deny lines are E 95, H 86, W 86 and T1' 0, the same with or without DR-1d and DR-2. Per rule:
  - at H: DR-1a 6, DR-1b 2, DR-1c 55, DR-4 28, DR-5 1;
  - at E: DR-1c 59 and DR-4 33.
- **Measurement for D1 (`rv5_hist14.py`).** No known retired A1 material escapes because of the removal. No line or sentence matched by DR-1d or DR-2 exists in any corpus tree or historical corpus blob (4677 blobs; see (c)).
- **DR-3's witness control (RT-DR3W).**
  - `AGENTS.md` at H has blob 12a9281fb88c14395b6715a3bf4b4f6b030f433c and sha256 d87acac54b5f6392af3323630236d98b14bb4d485d10c0ff56b20806b0883e27, as the design states.
  - Under splitter version 2 it has exactly one DR-3 sentence. It starts on line 37 ("Every posit of the substratum model ...") inside the list item that begins on line 36.
  - `AGENTS.md` at T1' has blob 9f4fc3e8..., sha256 59b68984...ce2, and 0 matches.
  - The control is sound. It reads one named blob, pinned by id and hash, with DR-3 alone. Sec. 6.4 and 16.2 make a control-only input readable only by its control, and make adding or changing one a widening change. So the production scan scope is not widened, silently or otherwise.
- **Splitter version 2 (O6) changes no deny count.** Sentence counts at E, H, W and T1' are identical under versions 1 and 2. At H: DR-1a 6, DR-1b 2, DR-1c 65, DR-4 28, DR-5 1. At E: DR-1c 70. At T1': none.

Criterion 3. V8: widened `resid` (`rv5_resid.py`)

| Tree | Writer | Mine |
|---|---|---|
| E: lines matched by resid-a / by resid-b or resid-c only / of those, hit by no other profile | 141 / 75 / 41 | 141 / 75 / 41 |
| H: same columns | 138 / 79 / 42 | 138 / 79 / 42 |
| T1', whole corpus: same columns | 98 / 88 / 46 | 98 / 88 / 46 |
| T1', added text: lines / `resid` hits / resid-a / added by resid-b or -c / hit by no other profile | 287 / 45 / 28 / 17 / 17 | 287 / 45 / 28 / 17 / 17 |
| New REVIEW lines at T1' | FULL:6265, appendix-c-objections.md:108, Complexity.md:206, Structure.md:1010 | the same 4. No deny rule matches any of them. |
| Review total | 226 | 226 = 200 + 5 + 4 + 17 |

The 4 new lines are legitimate wording; this is my reading, as in review-v4 task 3. They are proper review subjects, and none of them is a retired form.

Point (a): resid-c

- **It catches the missed example.** It matches "The substratum is assumed to have a finite number of states.", which resid-b does not match. The writer is right that my v4 claim was wrong: my V8 extension caught five of my six examples, not all six.
- **It adds no unintended match.** resid-c matches no line at E, H or T1' (whole corpus) and none of the 287 added-text lines.
- **It is documented precisely.** The pattern and reason are in DESIGN-v5 sec. 6.6, sec. 1 (the residual classes) and V26, and in CHANGES-v5 (the V8 row, and section 5).
- **Scope.** It stays within the purpose of the approved V8: V8's stated aim was to bring each listed escape to at least REVIEW, and resid-c does exactly that for the one string the V8 pattern missed. It goes beyond the letter of the approved pattern. It only adds REVIEW items, so it weakens nothing. The design already submits it to independent review with the rest of `resid`. Acceptable. The owner may wish to note that it is an addition.

Point (b): constructed strings that passed DR-1d or DR-2 coverage

Measured (`rv5_lost.py`). Every constructed string DR-1d or DR-2 matched in v4, and its outcome under v5 (item 7 with `--final`):

| String | v4 | v5 | Recorded in v5? |
|---|---|---|---|
| V4 "the framework's sixth structural property, finiteness of the bijection" | FAIL (DR-2) | PASS | yes (sec. 1, 6.4.1, V4) |
| V15 "the substratum's sixth axiom, finiteness" | FAIL (DR-1d) | REVIEW (resid-a) | yes (sec. 6.4.1, V15) |
| M-DR1d mutant line (glossary.md:11 at H, edited) | FAIL | FAIL (DR-4 on the same line) | not needed |
| M-DR2 mutant text "The framework's sixth structural property is finiteness of the substratum" (alone, or in the glossary.md:13 line) | FAIL (DR-2) | PASS | no |

- No known retired material escapes. All three strings that lost a FAIL are constructed, and the original literal item 7 also misses all three ("sixth structural" is neither "six structural" nor "sixth of"). Their passing does not conflict with criterion 1, which concerns the 95 real retired lines, or with D1, which asks that no known retired material escape and that no artificial evidence be used.
- The owner requires the lost synthetic coverage to be recorded. Sec. 6.4.1 records V4 and V15 but not the M-DR2 text, which now PASSes. Required correction W1.

Point (c): 4671 against 4657 blobs

The difference is the search method, not the set of refs. The local repository now has 794 refs, the number the writer used. Measured by me now:

- `git rev-list --all --objects -- papers book` (path-limited; my v4 method) yields 4657 blobs named `papers/*.md` or `book/*.md`.
- `git rev-list --all --objects` (unrestricted; the writer's figure) yields 4671.
- 20 blobs appear only in the unrestricted walk. The pathspec's history simplification drops commits that make no corpus change relative to the parent it follows, so blobs that exist only in side-branch commits are never listed. Example: 06aca25de4 (FULL.md) was introduced by 54b5188c, which is on branches a1exit-n8n10 and a1exit-s31.
- 6 blobs appear only in the path-limited walk. `--objects` names each blob by the first path it meets. In the unrestricted walk these 6 blobs are met first under a non-corpus path, so a filter on the path name drops them. The first paths are `repo/papers/Main.md`, `repo/papers/FREEZE-Main.md`, `repo/papers/Methodology.md`, `repo/papers/Structure.md`, a draft `Introduction-r15.md` under `verification/audits/` and `README.md`.
- The union is 4677 distinct blobs. All were scanned: the 4671 by `rv5_hist14.py` and the 6 by my v4 `rv_hist.py`. Under splitter versions 1 and 2, no line and no sentence matches DR-1d, DR-2 or DR-3. The 20 added blobs contain no relevant match.
- DESIGN-v5 sec. 0.3 and 6.4.1 attribute the difference to "the refs it saw". CHANGES-v5 section 5 does the same. That attribution is incorrect, and the writer's 4671 omits the 6 blobs. Required correction W2.

***

The other corrections

- **V1: confirmed.** Sec. 3.2 has the 9 groups by step: 8 at #1475 and Substratum.md 266/268 at #1474. Sec. 3.3 requires `own_lines` for all 22 sites. RT-T0 and 0.3 are corrected, and 8.2's HP row is updated. The groups match my v4 recount (`rv_merge.py`).
- **V2: confirmed.** `ptr` has 5 hits at T1', the 4 W2 lines and GR.md:58, as stated in sec. 6.5, sec. 11 row 1, 8.2 and RT-D. My recount reproduces it.
- **V4: confirmed.** The repo split is 96/31/14/35 by the class `classify()` returns, with the cause stated, in 0.3 and 8.2.
- **V5: confirmed.** "An HP obligation added, or a merge added to one" appears only in the widening list of sec. 16.2, with the reason. Z10 covers both directions and is part of S13.
- **V6:** see criterion 2.
- **V7: confirmed.** One label vocabulary (IR, IR+WR, WN) is used consistently in DESIGN-v5 sec. 0.3 and 8.2 and in CHANGES-v5. v3's 86 is attributed to the touching test alone, and the removed-site variant is kept only as an equivalent variant. This agrees with my v4 diagnosis of `work/measure10.py`.
- **V8:** see criterion 3.

The adopted optional points (writer's O2 to O7)

| Point | Check | Result |
|---|---|---|
| O2 | deny profiles run on every tree except E and H, and in op D on the named commit | consistent with RT-E, RT-H0, RT-DR and RT-I7A; no regression |
| O3 | rule-id assertions | correct |
| O4 | four hashes for LIST and TABLE adjudications | correct |
| O5 | root of trust | correct |
| O6 | splitter version 2 | deny counts unchanged at E, H, W and T1', at line and sentence level (criterion 2); the DR-3 witness becomes one exact sentence; no regression |
| O7 | scope bullet | correct |

O1 was declined, with the outcomes stated. That is acceptable.

Required corrections

W1. Sec. 6.4.1 ("What removing them costs") and sec. 1 (residual list): record that the constructed text of v4's former DR-2 countercontrol, "The framework's sixth structural property is finiteness of the substratum", now PASSes. No rule and no profile matches it, `resid` included, and the original literal item 7 misses it too. Add it as a control with expected PASS beside V4, so that a change in its outcome is visible. Also state that the M-DR1d line stays FAIL through DR-4.

W2. Sec. 0.3, sec. 6.4.1 and CHANGES-v5 section 5: replace "from the refs it saw" with the actual cause, which is method, not refs:
- path-limited history simplification omits 20 side-branch blobs;
- first-path naming in the unrestricted walk omits 6 blobs whose first-encountered path is outside the corpus.

State the union: 4677 distinct blobs, none matching DR-1d, DR-2 or DR-3. Specify the search as the union of both walks, or as every blob reachable at a corpus path in any commit, so that it does not depend on how the walk names blobs.

Optional points

- O8. RT-I7A and sec. 0.3: state that "86 deny lines" and "209" count line-level matches only. With sentence-level matches attributed to their lines, H has 93 and 216, and the 123 does not change.
- O9. Item 1 (sec. 11 row 1) still gives REVIEW for an unqualified `ptr` hit, where the original fails hard. Item 7's check with `--final` covers the same lines, so the plan as a whole does not regress. A `checks.item1` entry with `final_profiles: [ptr]` would make item 1 match its original on its own.
- O10. `resid`'s posit nouns omit "property" ("sixth structural property ... finiteness"). Adding it would bring V4 and the W1 string to REVIEW. Check the cost at T1' first, because the W1 lines contain "structural properties".

What I could not verify

- No implementation exists, so the controls were checked against the rules as specified, not run.
- The owner decisions V5-D1 and V5-D2 and their comment ids reached me only through the coordinator.
- My judgment of the 4 new `resid` lines as legitimate wording is a reviewer's reading, not a classification record.
- The history search covers objects reachable from the 794 local refs, not refs that exist only on the remote.

Files (all under D/review-v5/; MANIFEST.sha256 covers all of them)

- Scripts:
  - `rv5_rules.py`: the v5 active and retired rules, the widened `resid` and splitter versions 1 and 2, transcribed from the design;
  - `rv5_dr.py`, `rv5_item7.py`, `rv5_resid.py`, `rv5_lost.py`, `rv5_hist14.py`: the recounts and measurements;
  - `rv_git.py`, `rv_prof.py`, `rv_hp.py`: my v4 helpers, copied unchanged.
- Outputs:
  - `out5-denylines.json`, `out5-95.json`, `out5-resid17.json`, `out5-hist.txt`;
  - `only_pl.txt`, the 6 blobs found only by the path-limited walk.
- `data/`: the blobs read from E, H and P, as in v4.
