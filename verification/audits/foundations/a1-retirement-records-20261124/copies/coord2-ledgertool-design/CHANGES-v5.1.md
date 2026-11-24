# DESIGN-v5.1: changes against DESIGN-v5

Inputs, verified by sha256 before any work:

- `review-v5/review-v5.md`: dff73392fa0f255f58d0d658ac579a7bfe8bcbddec31cd88f34b2e32b5756af7. Verdict
  ACCEPT WITH REQUIRED CORRECTIONS: V3 and every other item confirmed; required corrections W1 and
  W2; optional points O8, O9 and O10.
- `DESIGN-v5.md`: 6693e5dd4dd2a0059e88a21091b979dfc36680e25e54960b9699d2a2f2972982.
- `CHANGES-v5.md`: 9e0efa6dda27d3441507c47e5c469ae324a7794c7a6b57d3165ba8af0e95e923.

As directed, v5.1 applies W1, W2 and O8 (as documentation only), and nothing else. Paper-only: no
repository change, no git or GitHub write, no workflow run. Two new measurement scripts are in
`work-v5/`: `w1o8.py` and `hist2.py`. They read git objects only.

`CHANGES-v5.md` is not edited. Its section 5 attributes the blob-count difference to refs, which
is wrong. The correction is recorded in the W2 row below and in DESIGN-v5.1.

## 1. Corrections applied

| Item | DESIGN-v5.1 sections changed | What changed | How it was verified |
|---|---|---|---|
| W1: lost coverage of the former DR-2 countercontrol text | 1 (residual list); 6.4.1 ("What removing them costs": three new bullets); 10.2 (new control V27, beside V4); 15 item 2; 16.4 (S13 list) | Records that "The framework's sixth structural property is finiteness of the substratum" now PASSes, alone or inside the glossary.md:13 line that the mutant edited. No rule, no profile and no `resid` alternative matches it, and the original literal item 7 misses it too. V27 expects PASS. Records that the former M-DR1d line stays FAIL through DR-4. States the full lost coverage: V4 and the M-DR2 text went from FAIL to PASS, and V15 from FAIL to REVIEW. No known retired real-tree material is affected | `work-v5/w1o8.py`, under the v5 rules. The M-DR2 text, its sentence form and the edited glossary.md:13 line at H give PASS, including under item 7 with `--final`; only the retired DR-2 matches them. The edited glossary.md:11 line gives FAIL through DR-4 (the retired DR-1d also matches it) |
| W2: the blob-count explanation | 0.3 (DR-1d/DR-2/DR-3 history bullet); 6.4.1 ("Why they were dropped", and the new paragraph "The history search"); 14 (history-search bullet) | The cause is search method, not refs. The path-limited walk (4657) omits 20 blobs found only in side-branch commits. The unrestricted walk (4671) omits 6 blobs first met under a non-corpus path. The search is now defined by commit trees, independent of how a walk names blobs: every blob at a top-level `papers/<name>.md` or `book/<name>.md` path in any commit reachable from any local ref. That set has 4677 blobs, and DR-1d, DR-2 and DR-3 match none of them | `work-v5/hist2.py`, over 794 local refs and 7857 commits. Path-limited walk 4657; unrestricted walk 4671; 20 only in the unrestricted walk, 6 only in the path-limited walk; union 4677. The tree-defined set (`git ls-tree` of each commit) is exactly the union. All 4677 scanned at line and sentence level (v5 splitter, no prefilter): 0 matches of DR-1d, DR-2 or DR-3 |
| O8 (documentation only) | 0.3 (item-7 bullet); 10.3 RT-I7A; 11 note 1 (V3 bullet); 14 (item-7 bullet) | States that 86 and 209 count line-level deny matches only. Counting each line of a matching multi-line sentence gives 93 and 216 at H; the 123 is unchanged | `work-v5/w1o8.py`: line level 86 + 123 = 209; with every line of each matching sentence attributed, 93 + 123 = 216. This agrees with the v5 review |

## 2. Optional points not adopted (left for the owner)

| Point | Content (review-v5) | Status |
|---|---|---|
| O9 | Item 1 (sec. 11 row 1) still gives REVIEW for an unqualified `ptr` hit, where the original fails hard. A `checks.item1` entry with `final_profiles: [ptr]` would make item 1 match its original on its own. The plan as a whole does not regress, because item 7's check covers the same lines | not adopted, as directed; left for the owner |
| O10 | Add "property" to `resid`'s posit nouns, which would bring V4 and the W1 string (V27) to REVIEW, after checking the cost at T1' (the W1 lines contain "structural properties") | not adopted, as directed; left for the owner. Not measured for v5.1 |

## 3. Nothing else changed

`diff DESIGN-v5.md DESIGN-v5.1.md` has 14 hunks. 25 lines are removed and 69 added; the line count
goes from 2023 to 2067. Each hunk belongs to one of the items above, apart from the title and
status lines:

| v5 lines | Section | Item |
|---|---|---|
| 1 | title ("design v5.1") | document identity |
| 7-8 | Status: what this document supersedes, and the input review-v5 with its hash | document identity |
| 196-198 | 0.3, history bullet | W2 |
| after 203 | 0.3, item-7 bullet: the O8 definition and 93 / 216 | O8 |
| 268-271 | 1, residual list | W1 |
| 1008-1012 | 6.4.1, "Why they were dropped" and the new "The history search" | W2 |
| after 1024 | 6.4.1, three new bullets on lost coverage | W1 |
| after 1371 | 10.2, new row V27 | W1 |
| 1450 | 10.3, RT-I7A reference column | O8 |
| 1503 | 11 note 1, V3 bullet | O8 |
| 1651-1654 | 14, history-search bullet | W2 |
| 1660 | 14, item-7 bullet | O8 |
| 1712-1713 | 15 item 2 | W1 |
| 1945 | 16.4, S13 control list (adds V27) | W1 |

No rule, pattern, count other than those named above, expected outcome other than the new V27, or
section structure changed.

The figure labels of sec. 0.3 are kept as in v5. The WN figures that the v5 review reproduced (the
209 and 12 item-7 counts among them) keep the label WN. The two figure sets added here, 93 / 216 and
4677, are described in the text as measured by the v5 review and by this writer, because the IR
label is defined as the v4 review's recount. Relabelling the other WN figures would be a change
beyond W1, W2 and O8, so it was not made.

## 4. Points not fully resolved

- The owner decisions are still cited without comment ids (DESIGN-v5.1 sec. 15 item 1).
- The history search covers objects reachable from the 794 local refs, not refs that exist only on
  the remote.
