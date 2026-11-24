# DESIGN-v5: changes against DESIGN-v4

Inputs, verified by sha256 before any work: `DESIGN-v4.md`
3cde34d2209dbcd6c5f03f991fb27385c2e709b9bd1557b60d965f9aa219c625, `CHANGES-v4.md`
c3214f10ea57879e7771bcacd2ea9a446b3fcc27c7464ad0d41cf665c145fdca, `review-v4/review-v4.md`
113d1c129ad761114a4b529c5ec90d6d79a224d468bffa0cbe7b3cfd922cca6f (verdict ACCEPT WITH REQUIRED
CORRECTIONS). The owner decisions of 2026-11-23 on the v4 review are called V5-D1 (deny rules) and
V5-D2 (`resid`) in the design, to keep them apart from the earlier D1-D4.

Paper-only: no repository change, no git or GitHub write, no workflow run. Measurement scripts are
new files in `work-v5/`. They read git objects only and did not import the v4 review's scripts.

Figure labels are those of DESIGN-v5 sec. 0.3, used identically here:

- **IR**: independently recounted by the v4 review.
- **IR+WR**: as IR, and recounted again by this writer for v5.
- **WN**: introduced or changed in v5, measured by this writer only.

## 1. Required corrections and owner decisions

| Item | v5 sections changed | What changed | How it was verified |
|---|---|---|---|
| V1: mergers are 9 groups covering 22 sites | 0.3; 3.2 (merger paragraph and table); 3.3 (`own_lines` for all 22); 8.2 (HP row); 10.3 RT-T0 | "At T1' there is one" is replaced by the 9 groups, by step: 8 at #1475, 1 at #1474. Only Substratum.md 266/268 is overlapped by an H..T1' splice (D029). `own_lines` is required for all 22 merged sites, whether or not a splice overlaps the region | `work-v5/walk.py`, a new implementation of sec. 3.2 from its text: 113 changed sites, 3 two-step sites, attribution 48/23/15/15/12, and 9 merger groups covering exactly the 22 sites the review lists. IR+WR |
| V2: `ptr` has 5 hits at T1' | 0.3; 6.5 (new paragraph "The fifth `ptr` hit"); 8.2 (new row); 11 row 1; 10.3 RT-D | Row 1 now expects 5 hits: the 4 W2 lines PASS with their rules, papers/GR.md:58 with its hit classification record, else REVIEW. States that W1 and W2 replace only P's first two `RESIDUAL_ALLOW` entries, not the third (GR.md:58, ledger X-70), and that GR.md:58 is one of the 84 | `work-v5/item7.py`: 5 `ptr` lines at T1'. GR.md:58 confirmed among the 84 (`work-v4/s84.txt`) and against P's `RESIDUAL_ALLOW` and strip in its verified `edits_check.py` blob. IR+WR |
| V3: item 7's failure behaviour is not weakened | 5 (`--check`, per-check `final_profiles`); 11 row 11 and note 1 (proposed check, V3 bullet); 16.2 (`checks` field, lint, widening); 16.4; 10.2 V23-V25, X9; 10.3 RT-I7A; 0.3 | The proposed check is `terms ... --check item7 --final`. Item 7's `final_profiles` are `ptr` and `count-grep`, so every unclassified `ptr` or `count-grep` hit is FAIL `final-unclassified`, as in the original. `final_profiles` moves from one global list to a per-check `checks` table (item 11 keeps `repo`). `--final` without `--check` is USAGE. A bare-A1 deny rule was not chosen: it would be a new deny rule needing its own review, and the per-check conversion gives the original's behaviour with no new pattern. Countercontrols in both directions: V23 (ch02:136 at H reinstated) and V24 ("six structural hypotheses") FAIL; V25 gives REVIEW without `--final`, PASS for a W2 line with its rule, and REVIEW for a `resid`-only hit | `work-v5/item7.py`: 95 retired lines at H (carrying `\bA1\b` or a `count-grep` literal, absent at T1', no deny match), all of them `ptr` or `count-grep` hits, so all FAIL. Counts with no records: at H, 86 deny lines plus 123 `final-unclassified` lines (209); at T1', 0 deny lines and 12 `final-unclassified` lines (7 W1, 4 W2, GR.md:58). `work-v5/esc.py`: V23 and V24 match no deny rule and are `ptr` and `count-grep` hits respectively. The 95 is IR+WR; the 209 and 12 are WN |
| V4: repo split 96/31/14/35 | 0.3; 8.2 | 14 substring lines (9 unrelated label, 1 historical record label, 1 registry identifier, 3 preserved historical evidence) and 35 IDENT, by the class `classify()` returns. States that v4's split attributed lines by path (first `EXPLAINED` entry), not by returned class | `work-v5/repo.py`: P's verified `edits_check.py` imported with `python -I`. Every `REPO_PAT` line of every tracked text file at T1' was classified, and its mechanism read from the same `EXPLAINED` table. Result 96/31/14/35, with 5486 historical and 2 generated lines. IR+WR |
| V5: HP obligations and merges are widening | 16.2 (non-widening list, widening list with the reason); 16.6 (Z10); 16.8 | "Adding an HP obligation or a merge to one" moves from the non-widening list to the widening list. A new merge turns a `provenance-foreign` step into an adjudicable one, and a new obligation turns RET `unauthorized-change` into adjudicable HP sites. Z10: such a change without a widening review is ERROR `CONFIG_UNREVIEWED` | Textual: the item appears only in the widening list. Z10 states both directions |
| V6 and V5-D1: DR-1d and DR-2 dropped; DR-3's real witness | 6.1 (deny table); 6.2 (`countercontrol` field: no constructed text); 6.4 (rewritten: active rules, measured table, DR-3 witness and control-only scan); 6.4.1 (new: rejected-candidate history); 1; 10.2 V2, V4, V15 (V8 removed); 10.3 RT-DR, RT-DR3W (new); 15 items 2-3; 16.2 (lint, control-only inputs widening); 16.4; 0.3 | (a) The purpose and exact patterns of DR-1d and DR-2 are recorded in sec. 6.4.1; their ids are retired, not reused. (b) No real-tree match exists; this supports removal but does not prove such forms can never occur. (c) Measured cost: no known retired line loses a FAIL, because none exists; the constructed V15 becomes REVIEW (via `resid`), and V4 becomes PASS, a stated residual that the original item 7 also misses. (d) DR-3's real witness is `AGENTS.md` at H, lines 37-39, the sentence that splice D296 rewrites. It lies outside the corpus scan scope. The production scope is not widened (other ledgered non-corpus files carry legitimate deny matches at T1'). Instead, control RT-DR3W scans that one blob, named by commit, path, git blob id and sha256 in the controls file, with DR-3 alone, and expects exactly one sentence; its countercontrol, `AGENTS.md` at T1', expects 0. Mutant countercontrols M-DR1d, M-DR2 and M-DR3 are removed; no constructed text is used as evidence | `work-v5/hist.py`: 4671 distinct `papers/*.md` and `book/*.md` blobs reachable from the 794 local refs (the v4 review counted 4657 from the refs it saw). The "sixth/seventh" prefilter is exact; 764 blobs pass it; 0 line or sentence matches of DR-1d or DR-2. Also 0 in every text file at H (3543), W (3543) and T1' (3550). DR-3 matches only `AGENTS.md` at H and W, and at T1' only the frozen `edits.json`, which quotes the old sentence. `work-v5/dr5.py`: active-set distinct lines 95 (E), 86 (H), 86 (W), 0 (T1'), the same with or without the two rules. The witness sentence was located with the v5 splitter, and D296's span (bytes 2332-2382, lines 37-38) was confirmed. `esc.py`: outcomes of V4 and V15 |
| V7: figure labels; source of v3's 86 | 0.3 (labels defined and applied to every figure; withdrawn list); 8.2 (label column); 14 (rewritten: v5 measurements, then the carried figures); this file | One label vocabulary (IR, IR+WR, WN) in both documents. v4's disagreement is resolved: 19/31 and 18 are IR (recounted by the v4 review), not "recounted for v4". v3's 86 is attributed to the touching test alone. Counting the removed sites' offset lines is kept only as an equivalent variant that v3's script did not use | `work-v5/m10strict.py`: `work/measure10.py` with only its overlap test made strict gives 84. The script skips empty images (`if seg and k >= 0`). IR+WR |
| V8 and V5-D2: `resid` widened | 1 (residual classes listed exactly; remaining escapes named); 6.6 (rewritten: resid-a, resid-b, resid-c, matches by tree, outcome per newly matched line); 8.2 (`resid` row 17, total 226); 10.2 V26; 10.3 RT-D; 15 item 3; 16.4; 0.3 | resid-b is the v4 review's pattern, unchanged. resid-c (`finite number/count of states|configurations|elements|points|sites`) is added, because the review listed "The substratum is assumed to have a finite number of states." as caught, and resid-b does not catch it. Every additional match is reported per tree. Only added-text lines at T1' get an outcome: the 4 new lines are REVIEW_REQUIRED `unclassified` (none FAIL: no deny match; none PASS without a record). Lines outside added text get no outcome | `work-v5/resid5.py`: on the 287 added-text lines, 45 `resid` hits; 17 hit by no other profile (13 as in v4, plus 4: FULL:6265, appendix-c-objections.md:108, Complexity.md:206, Structure.md:1010). The count equals the v4 review's target of 4, and the 4 lines are the same. The other 13 lines that resid-b newly matches are already hit by another profile. Whole-corpus matches of resid-b or resid-c only: E 75 (41 with no other profile), H 79 (42), T1' 88 (46). `resid5b.py`: resid-c matches no line at E, H or T1' and no added-text line; it matches the "finite number of states" string. Labels: 13 IR+WR; 4 and 226 WN |

## 2. Optional points of the v4 review

| Point | Decision | Where | Reason |
|---|---|---|---|
| O1: close anchored deny gaps ("six posits of the substratum", "fourteen-item", "lists fourteen", `$A_1$–$A_6$`, ranges with intermediate items, U+2212 and U+2010/U+2011, "Finiteness (A1)", "hypotheses" in N) | declined | sec. 1, 15 item 3 | None has a real-tree match at E, H or T1' (v4 review, `rv_dr6.py`), the same ground on which V5-D1 dropped DR-1d and DR-2. Their outcomes are stated (`esc.py`): ranges with intermediate items, U+2212, "Finiteness (A1)" and "six structural hypotheses" are REVIEW, and FAIL under item 7 with `--final` (V3). "six posits of the substratum", "six assumptions about the substratum", "lists fourteen", "fourteen-item" and `$A_1$–$A_6$` PASS, and the original item 7 misses them too. They are listed for the owner |
| O2: deny profiles on every tree except `E` and `H` | adopted | sec. 2.3 | It removes the dependence on a ledgered segment's endpoint. The trees are named through `roles.pin` and `roles.scientific_base` |
| O3: assert the target rule id on each countercontrol line | adopted | sec. 6.4 (measured table), RT-DR | Needed because the DR-1a and DR-4 lines also match other rules. With the mutants gone, it applies to the real lines |
| O4: LIST or TABLE adjudication matches both context and both structure hashes | adopted | sec. 4.1 | A site whose neighbour context changed while its structure hash did not would otherwise be resolvable by a structure-only adjudication |
| O5: root of trust | adopted | sec. 6.3 | The configuration's owner field is checked against `F`'s owner-designated pin table |
| O6: splitter ends a paragraph at a list item; terminator before closing emphasis | adopted, as splitter version 2 | sec. 6.1 | Also strips each line before joining. Re-measured (`dr5.py`, `sentcount.py`): deny counts at H and T1' unchanged at line and sentence level (H per sentence: 6/2/65/28/1, as in v4); the DR-3 witness in `AGENTS.md` is one sentence, lines 37-39, ending at "framework.". No fingerprints exist yet to re-measure. Changing `splitter_version` later is widening |
| O7: active non-corpus uses of "the sixth structural assumption" | adopted | sec. 11 note 1 (scope bullet), 6.4 | One line in the amendment's scope statement, and the note that DR-1's ordinal alternatives encode a corpus terminology decision |

## 3. Further changes

| Point | v5 sections | Reason |
|---|---|---|
| The `countercontrol` field of a deny rule no longer admits a mutant | 6.2; 16.2 lint | Follows V5-D1: no constructed text serves as evidence. A control-only input is a real blob named by id and hash |
| Adding or changing a control-only input is widening | 16.2 | It changes what a control exercises. It is reviewed with the controls file |
| `checks` replaces `final_profiles` in the configuration | 16.2, 16.4, 5, 11 | Needed by V3. Removing an entry from a check's `final_profiles`, or a check, is widening |
| S13's list of controls | 16.4, 16.8 | Updated to the v5 expectations (V4 PASS, V15 REVIEW, V23-V26, RT-I7A, RT-DR3W, Z10) |

## 4. v4 text deliberately left unchanged

| v4 text | Why it is kept |
|---|---|
| Sec. 3.2 rules 1-3 and the region-attributed decision basis | The walk was reimplemented and reproduces v4's figures exactly. V1 corrects only the merger account |
| DR-1 (a, b, c), DR-3, DR-4 and DR-5 patterns | V5-D1 keeps them. The v4 review confirmed their counts and controls |
| V20 ("the first being finiteness of S", DR-3) and V2 | DR-3 stays active. V2 is relabelled as a synthetic edit, since DR-3's evidence is now the real witness |
| The context rule, indicators and their counts (sec. 4) | All IR, with no correction required. O4 is the only change |
| Exit codes, acceptance predicate, ownership chain, delegation contract | Found resolved by the v4 review |
| The 32 and 154 error counts stay withdrawn | Recounted by no one, and used by no outcome |

## 5. Points not fully resolved

- The owner decisions are cited without comment ids. This writer received them only through the
  coordinating session (DESIGN-v5 sec. 15 item 1).
- The history-search blob count is 4671 here against the v4 review's 4657. Both find no match. The
  difference is in the set of local refs at the time of each search. I did not reconcile which
  blobs differ.
- The v4 review said its `resid` extension catches all six of its escape strings. Measured, it
  misses "The substratum is assumed to have a finite number of states."; v5 adds resid-c for it.
  The other five are caught by resid-b.
- Every figure labelled WN needs an independent recount.
