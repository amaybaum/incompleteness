# Focused confirmation r2: integration assessment r2 against REVIEW-r1

**Verdict: CONFIRMED (ACCEPT).** All 18 findings of `REVIEW-r1.md` are resolved where and as
`RESPONSE-r1.md` says. The head facts and checks in r2 reproduce at the current heads. The §6
"Basis" paragraph and OQ-10 are accurate and do not overreach. Every changed line of the assessment
and the notes falls inside the declared delta tables. Nothing is blocking. Three optional notes
follow: two Low and one Info.

**Object.** Branch `research/integration-assess-20261113`, fetched by name with full history, at
`b2472bca21ca1753b1e2b45ac69bf40330436e97`. The history is:

| Commit | Content |
|---|---|
| `79b4d4cd` | r1 |
| `cc297f16` | adds `REVIEW-r1.md` |
| `b2472bca` | adds `INTEGRATION-ASSESS-r2.md` (IA2), `NOTES-r2.md` (N2) and `RESPONSE-r1.md` |

- The committed `REVIEW-r1.md` is byte-identical to the review's working copy (`cmp`).
- The r1 files are unchanged from `79b4d4cd` to `b2472bca` (`git diff --quiet`).

The work used a fresh detached worktree, to be removed with `git worktree remove`. It ran only git
read commands, the repository check scripts and host API reads.

***

## 1. Each finding against RESPONSE

| Finding | Confirmed at | Notes |
|---|---|---|
| F1 | IA2:40–45, :112, :385–410, :481–496, :585, :656–658 | `research/g3-offset-873-20261113` is at `1ad01923`: 28 files, all `A`, four unit 2(a) commits after `46a548fb`. #873 c.6863416405 is quoted for Q4/Q7/Q8. Options (a)/(b) are stated, and (b) has no ref movement. `G3-UNIT2A-r3.md` is blob `ff1875d4`, and its QU4 (r3:841, "Unit 1 text") exists as described. Gating route (a) on QU4 goes beyond the fix I specified; it is justified by r3's verdict (C) on Part 2. |
| F2 | IA2:46–50, :352–358, :517–519, :590 | 5897397957 and its integration sentence are quoted verbatim. |
| F3 | IA2:25–29, :50–52, :81, :162–163, :177, :287–300, :526–539, :588 | ChatGPT 5897679945 is on #1268 at `3a3aa146` (20:34:33Z). Its body quotes match: "ACCEPT (bounded housekeeping only)", the optional LOW, and "must close/narrow the off-main source gaps". `REC-1-r9.md`:495–496 keeps the landing bar, and the r9 blob is `945b7982`. |
| F4 | IA2:46–50, :118–119, :220–221, :361–362, :506–512, :659–662 | The (a)/(b) options match the fix. The untraced references are named, and REVISE on r4 is stated. |
| F5 | IA2:545–548, :569–572, :646–648 | As specified. |
| F6 | IA2:66–67, :254–256, every §3 "§A.46 basis" bullet, :343–345, :603–611, :669–671; N2:146–151 | #1271's reason is restated as its item 8 gap and the option (c) choice. N2's stricter-reading sentence is corrected. The EOI wording at IA2:114 and :421–424 is now consistent with ARP-1-MARC `preregistration.md`:124. |
| F7 | IA2:458–467 | Heading, verification-status line and per-gap remediation are present. |
| F8 | IA2:280–282, :471–472 | Reduced to row H. |
| F9 | IA2:229–230, :283–285, :569–571, :645; N2:160 | New reason. The support-only blob check excludes `6c127b0a`. |
| F10 | IA2:439–442 | As specified. |
| F11 | IA2:160, :468–469 | All four commits are listed. |
| F12 | IA2:619–621 | As specified. |
| F13 | IA2:96–97, :400–402; N2:78–79, :105–106 | As specified. |
| F14 | IA2:54–57, :128–131, :198–199, :329, :559–560, :591 | SB rows split, and the narrowing alternative is carried throughout. |
| F15 | IA2:222, :517–519 | `0e0b3ddc` is off `main` and provenance (`ASSESS-868.md`:139–140). |
| F16 | IA2:58–59, :376–381, :575–576, :672–673 | OQ-11 added. |
| F17 | N2:154–156 | As specified. |
| F18 | IA2:7–8, :414–415, :595–596 | Own disposition stated. #1270's "Preservation only. Not for merge." is quoted. |

## 2. Head facts and checks at the current heads

**Heads.**
- #1268 is at `3a3aa146` and #1275 at `1ad01923`.
- #1282 (`research/c3-rlin-xiii-20261113`) has moved from `a03af682` to `ee4db4f1`, "C3 check r2 from
  review r1" (Info note C below).

**`git merge-tree --write-tree origin/main <head>`.** Exit 0 at `3a3aa146`, `1ad01923`, `ee4db4f1` and
`b2472bca`.

**Add-only and disjoint.** Every head is add-only:

| Head | Added files |
|---|---|
| `3a3aa146` | 41 |
| `1ad01923` | 28 |
| `ee4db4f1` | 6 |
| `b2472bca` | 6 |

Across the eleven current heads (nine candidates plus #1279 and #1282), no path is added twice.

**Battery.** I ran the full battery on these heads: placement, claims, staleness, voice, duplicate,
dependency-label `--strict`, legacy records, citation roles, and SC-42 compared with `cmp`.

| Head | Result |
|---|---|
| `3a3aa146` | every check exits 0; SC-42 byte-equal |
| `1ad01923` | every check exits 0; SC-42 byte-equal |
| `ee4db4f1` | every check exits 0; SC-42 byte-equal |
| `b2472bca` (the assessment) | every check exits 0; SC-42 byte-equal |

**Added 40-hex ids.** 19 at `3a3aa146` and 10 at `1ad01923`, all resolving, as N2:95–96 states.

**CI** (check runs, host API):

| Head | Status |
|---|---|
| `3a3aa146` | 26 success, 1 skipped |
| `1ad01923` | 25 queued, 1 skipped |

Both match N2:103–106.

**Records.** I read each record that N2:98–102 lists, and each exists with the stated author and
time: 5897397957, c.6863753317, 5897679945, c.6864323211, c.6863416405 and c.6846206075.

## 3. The §6 basis and OQ-10

The statement is accurate:

- The quote of #1265 c.6846206075 is faithful, with ellipsis.
- It correctly calls the basis owner practice, not §A.46 item 2's literal text.
- It states the strict reading's consequence correctly: none of the nine qualifies.
- It puts the open question to the owner as OQ-10 instead of answering it.

It neither implies authorization nor promotes a claim. Note A below proposes one optional wording
refinement.

## 4. Scope of the change

Measured hunks and line counts:

| File pair | Hunks | Lines removed | Lines added | RESPONSE |
|---|---|---|---|---|
| `INTEGRATION-ASSESS-r1.md` → `-r2.md` | 70 | 177 | 268 | "177 lines removed, 268 added, in 70 hunks" |
| `NOTES-r1.md` → `-r2.md` | 9 | 16 | 57 | "16 lines removed, 57 added, in 9 hunks" |

Every hunk's r1 range lies inside a row of the corresponding delta table.

The changes RESPONSE lists as beyond the findings check out:
- the §1 rows;
- the #1282 remark at IA2:128–131, whose quote of 5897679945, "cannot be used to update", is
  accurate;
- unit 2(a)'s QU3 at IA2:628–629;
- the AW-C3-1 cross-reference at IA2:630. `C3-RLIN-r1.md`:416 carries AW-C3-1, and #1282's review
  says it restates AW-P0-2.

**Register.** None of the barred path prefixes or the session-storage word appears in IA2, N2 or
RESPONSE.

***

## Optional notes

**A (Low). IA2:607–611: the basis sentence answers the question that OQ-10 then asks.** "No claim
here is established (§A.46 item 1)" is true now, because no record is yet verifiable from `main`.
Read without that qualifier, it seems to pre-empt OQ-10.
- *Fix:* replace "no claim here is established (§A.46 item 1)" with "no claim here is established at
  present (§A.46 item 1: none is verifiable from `main` before it lands)".

**B (Low). IA2:58: #1276's inputs do not come from step 3.** #1276's inputs come from steps 1, 4, 5
and 6. Its §8 lists "QH (#1269) | not used". This change is not attributed to a finding in the
delta table, though it falls in the IA2:54–72 hunk.
- *Fix:* "every unit result it ranks is from steps 1 and 4–6".

**C (Info). IA2:28–29; N2:89, :93, :141: #1282 has moved.** #1282 moved from `a03af682` to `ee4db4f1`
(r2) after r2 was written. At `ee4db4f1` it is add-only (6 files, in its own directory), merges
cleanly, and passes the battery. It remains a non-candidate, so no conclusion changes.
- *Fix:* update the pin when the record is next touched.
