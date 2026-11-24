Final bounded check of DESIGN-v5.1 (commit-independent ledger and terminology verification tool)

Verdict: ACCEPT on DESIGN-v5.1.md 0c4ff0e60331d0e9604ece0c997dec472b3f977bf24384676d74f850bff4a3fe with CHANGES-v5.1.md 89884a75d344f6019d829ad8ada684fead39a30a1bdb7eb3ab0d2bd0f8e943f1

Reviewer: the independent, non-author session that wrote review-v4 and review-v5. The check was read-only:

- no change to the checkout;
- no git, GitHub or workflow action;
- my only new files are under `D/review-v5.1/`, where D = <records>/coord2-ledgertool-design.

During the check I briefly wrote one temporary hash-list file in the workspace root, outside `review-v5.1/`, and deleted it at once. It contained only lines copied from `D/MANIFEST.sha256`.

My only script here is `rv51_treeset.py`. I did not read or run the writer's `work-v5/` scripts. Date 2026-11-23.

Goal link (sec. A.47): A1-EXIT (#1169), the exception-free verification route. This check decides whether v5.1 closes review-v5's required corrections without other change. It adopts no rule, record or count.

Input hashes (verified first; all match)

- DESIGN-v5.1.md 0c4ff0e60331d0e9604ece0c997dec472b3f977bf24384676d74f850bff4a3fe
- CHANGES-v5.1.md 89884a75d344f6019d829ad8ada684fead39a30a1bdb7eb3ab0d2bd0f8e943f1
- DESIGN-v5.md (base) 6693e5dd4dd2a0059e88a21091b979dfc36680e25e54960b9699d2a2f2972982
- review-v5/review-v5.md dff73392fa0f255f58d0d658ac579a7bfe8bcbddec31cd88f34b2e32b5756af7

1. W1, W2 and O8 are applied correctly

- **W1.** The text of the former DR-2 countercontrol (mutant M-DR2), "The framework's sixth structural property is finiteness of the substratum", is recorded as now PASS:
  - in sec. 1's residual list;
  - in sec. 6.4.1 ("What removing them costs");
  - in sec. 15 item 2;
  - as new control V27 (expected PASS, alone and as the edited glossary.md:13 line), which is also added to the S13 list in sec. 16.4.

  Sec. 6.4.1 also states that V4 went from FAIL to PASS, that V15 went from FAIL to REVIEW, and that the M-DR1d line stays FAIL through DR-4. All of this agrees with my measurement in review-v5 (`review-v5/rv5_lost.py`). That measurement found both forms of the M-DR2 text PASS, and the M-DR1d line FAIL through DR-4.
- **W2.** The 4671-versus-4657 difference is now explained by search method, not refs:
  - the path-limited walk misses 20 blobs, because history simplification drops side-branch commits;
  - the unrestricted walk misses 6 blobs, because each blob is named by the first path the walk meets;
  - the union is 4677 blobs, with zero matches of DR-1d, DR-2 or DR-3.

  This is stated in sec. 0.3, sec. 6.4.1 ("The history search") and sec. 14, and in the W2 row of CHANGES-v5.1. CHANGES-v5.1 also records that the wrong attribution in CHANGES-v5 section 5 is corrected there, not by editing CHANGES-v5. That keeps the earlier record unedited, which is right.
- **O8.** Sec. 0.3, RT-I7A, sec. 11 note 1 and sec. 14 now state that 86 and 209 count line-level deny matches only. With sentence matches attributed to their lines, H has 93 deny lines and 216 FAIL lines, and the 123 does not change. These figures agree with my review-v5 measurement (`rv5_item7.py`: 93 / 123 / 216; line level 86 / 123 / 209). The inputs are the same commits, so no recount was needed.

2. The changes are documentation only

- **Diff size.** `diff DESIGN-v5.md DESIGN-v5.1.md` has 14 hunks, with 25 lines removed and 69 added, as the writer reports.
- **Every hunk is accounted for.** I read each one:
  - title and status lines: 2 hunks;
  - W2: 3 hunks (sec. 0.3, sec. 6.4.1, sec. 14);
  - O8: 4 hunks (sec. 0.3, RT-I7A, sec. 11 note 1, sec. 14);
  - W1: 5 hunks (sec. 1, sec. 6.4.1, V27, sec. 15 item 2, the S13 list).

  This matches the CHANGES-v5.1 section 3 table.
- **Nothing behavioural changed.** No deny or review pattern, profile, scope, outcome mapping, exit code, threshold, configuration field, widening rule, or control expectation changed, other than the new V27 with expected PASS. No count changed except the two figure sets the corrections add (93 / 216, and 4677).
- **W2's new definition of the history search.** The searched set is every blob at a top-level `papers/<name>.md` or `book/<name>.md` path in the tree of any commit reachable from the local refs. It is a definition of the search set only. It feeds no rule, profile or verdict of the tool; it is evidence for the record of why DR-1d and DR-2 were dropped.
- **Spot-check of the 4677** (`rv51_treeset.py`, `git ls-tree` of every commit):
  - over 7857 commits, the tree-defined set has 4677 blobs;
  - it equals the union of the path-limited walk (4657) and the unrestricted walk (4671) exactly;
  - the earlier scan covered that union in full (4671 by `review-v5/rv5_hist14.py`, the remaining 6 by `review-v4/rv_hist.py`), with no match of DR-1d, DR-2 or DR-3.

  The definition is therefore equal to the 4677 union, and the zero-match result holds for it.

3. Behaviour accepted under V1 to V8 is unchanged

The diff touches no passage that carries V1 (mergers and `own_lines`), V2 (`ptr` 5), V3 (the `--check item7 --final` mechanism; the 95 lines; V23-V25), V4 (repo split), V5 (widening and Z10), V6 (active deny set; RT-DR3W), V7 (labels) or V8 (`resid` a/b/c; 226), apart from the documentation additions of O8 to the V3 counts. The O8 wording leaves the counts and the 95-line result unchanged.

4. Earlier evidence files are byte-identical

- **D/MANIFEST.sha256.** `sha256sum -c` over its lines for DESIGN.md, DESIGN-v2.md, DESIGN-v3.md, DESIGN-v4.md, DESIGN-v5.md, CHANGES-v4.md, CHANGES-v5.md, review-v2.md and review-v3.md gives OK for all nine.
- **D/review-v4/MANIFEST.sha256.** All entries OK.
- **D/review-v5/MANIFEST.sha256.** All entries OK.

5. O9 and O10 are deferred, not dropped

CHANGES-v5.1 section 2 lists both with their content and the status "not adopted, as directed; left for the owner". That is a deferral record, so the condition is met.

Optional notes (not required):

- DESIGN-v5.1 sec. 15 does not list them. Carrying them into the design's open points at the next revision would keep the design self-contained.
- They should be cited as "review-v5 O9" and "review-v5 O10". DESIGN-v5.1 already uses O9 as the id of an ownership control (sec. 10.2), and O1-O9 for that control family.

Findings

There is no required correction. The two optional notes are under point 5. What I could not verify is unchanged from review-v5:

- no implementation exists, so the controls were checked against the rules as written, not run;
- the owner decisions reached me without comment ids;
- the history search covers only the 794 local refs.

Files (D/review-v5.1/; MANIFEST.sha256 covers them)

- `review-v5.1.md`: this file.
- `rv51_treeset.py`: the spot-check that the tree-defined history set equals the union of the two walks.
