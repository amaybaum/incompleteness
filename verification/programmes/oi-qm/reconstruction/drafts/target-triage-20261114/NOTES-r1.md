# Notes for TRIAGE-r1: what was read, and what was not

Read-only work. Nothing was edited, committed, pushed or posted, and no computation on OI models
was run. All GitHub content was read through the public REST API on 2026-11-14 (about 11:05–11:40Z).

## 1. Target records (read in full)

- #914 c.6875046763 (2026-11-14T09:14:01Z), c.6875548603 (09:56:47Z), c.6876304390 (11:02:44Z; the
  authorization of this triage).
- #1169 c.6875724719 (authorization of the Gate A forward amendment).
- `wt-gatea/verification/programmes/oi-qm/reconstruction/drafts/gate-a-amendment-20261114/`:
  `GATE-A-AMEND-r4.md` and `OWNER-QUESTIONS-r4.md` in full; `README.md`; §2 and §3 of
  `GATE-A-AMEND-r3-TRACE.md`. The worktree head was `927915e9`. The amendment is a draft; r4 is
  unreviewed.

## 2. Issue list

`/issues?state=open&per_page=100`, pages 1–3: 130 open items, 40 with a `pull_request` key, 90
Issues. All 90 bodies and all comment threads (59 Issues have comments) were downloaded.

## 3. Depth of reading, per Issue

**Body read in full** (lines longer than about 1,300–1,500 characters were cut at that length in
#868, #1007, #1010, #1032 and #1236; the repeated sections "Pinned files", "Provenance" and "When
work becomes active" were skipped): #865, #866, #867, #868, #869, #870, #871, #872, #873, #874,
#875, #896, #897, #898, #899, #900, #913, #914, #944, #945, #983, #1007, #1010, #1013, #1014,
#1015, #1032, #1049, #1052, #1055, #1059, #1060, #1061, #1062, #1064, #1065, #1066, #1067, #1068,
#1069, #1112, #1142, #1143, #1147, #1169, #1188, #1210, #1211, #1216, #1217, #1220, #1234, #1236,
#1238, #1245.

**Body read in part** (title, labels, the planning block's tier, prerequisites, readiness and
authorization entries, the question or purpose paragraph, and every line matching a keyword list:
equivalence, both directions, two-way, non-quantum, necessity, F1, F2, Bell, Tsirelson, gravity,
sector, exact, approximation, and references to #914, #1169, #875, #1143): #901, #902, #903, #924,
#929, #934, #970 (its seven-track table was also read), #979, #985, #986, #996, #1004, #1008,
#1028, #1029, #1031, #1037, #1058, #1063, #1070, #1071, #1072, #1073, #1090, #1091, #1092, #1118,
#1141, #1155, #1162, #1163, #1190, #1193, #1244, #1255. The task asked for every body to be read;
for these 35 the reading was of the planning block, the question and the matched lines, not of
every line. Each is judged unaffected except #1063. A reviewer who needs certainty on one of them
should read its body in full.

**Comments read in full:**
- #875: both.
- #914: 6563412734, 6707416018, 6742050590, 6775022284, 6776048388, 6777841157, 6875046763,
  6875548603, 6876304390. The other 57 were read by first line only.
- #1169: 6703342848, 6717894314, 6763928950, 6791556736, 6854031895, 6854728636, 6863414487,
  6875724719. The last 45 of 224 were read by first line; the rest were not read except through
  the searches in §4.
- #1143: 6775039087, 6863602000; the last 22 by first line.
- #1216: 6741763726, 6742051100, 6775038456, 6793397036, 6853532320; the rest by first line.
- #1236: 6802597845, 6802769760, 6802878292, 6816189419, 6817129920, 6828822665, 6846408321,
  6846442383, 6846953975, 6847314661, 6847882040, 6873565446, 6874529744, 6875058407 (several cut
  at about 2,600 characters).
- #1238: all three.
- #868: 6791565399, 6854708572, 6873193841, 6874036684 (the first two cut at 3,000 characters).
- #873: 6859060590, 6859687612, 6872827835, 6872959810, 6872998421, 6875553420.
- #1028: 6657997292 and 6658060093, in part.
- First-line indexes only: #1049, #1059, #1060, #1210, #1211, #1234.
- No comment was read on the remaining Issues with comments, except through the searches in §4.

## 4. Searches run over all bodies and all comments

- For "Bell-first" and "Bell-scope verdict" (to locate the recorded priority).
- For two-way or class-wide wording: "both directions", "two-way", "bidirectional", "full …
  equivalence", "no non-quantum", "non-quantum behaviour", "quantum soundness", "every (admitted|OI)
  model", "full quantum equivalence fails", "OI ↔ QM equivalence". Hits outside the Issues listed
  as affected were inspected (#970, #1028, #1029, #1031, #1092, #1112, #1162, #1190, #1244) and
  judged not to state the target.

A search of this kind shows where a phrase occurs. It does not show that no other restatement of the
superseded requirement exists in the unread comments.

## 5. Other sources

- `f2-decision-memo.md` at `acfef447` (branch-only; read from the local object store for the target
  statement, the G1–G8 table and the N1/N3′ rows only). Cited in D-2 as provenance for what #875's
  decisions refer to.
- `papers/Main.md` lines 1–2, 66 and 598 and `papers/GR.md` line 162 in the `wt-gatea` worktree, to
  confirm the Main subtitle and the lines the target records cite.

## 6. Not read

- The GitHub Project *OI Research Programme* (board placements are taken from Issue text only).
- Any pull request body, review or diff, including #1287 (`TARGET-THEOREM-r3.md`), #1173, #1219,
  #1231, #1232, #1267, #1272, #1273, #1275.
- `verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md` itself; the Gate A
  contract is represented here by the amendment draft's quotations of it.
- `verification/ROADMAP.md`, `PROGRAMME.md` and the master dependency matrix (#914 c.6563412926).
- Closed Issues and closed pull requests.

## 7. Checks on the triage document

- Every string in double quotation marks (297 strings) was matched mechanically against the
  downloaded bodies and comments, the amendment files and the decision memo, after removing Markdown
  emphasis markers and normalizing whitespace; segments separated by "…" were matched separately.
  All matched. Quoted strings shorter than eight characters were not checked.
- All 90 Issue numbers appear; 39 are in §2 and 51 in §4.
- Table: 37 rows (one row groups #865, #867 and #869); the longest cell has 26 words.

## 8. Judgements a reviewer may want to test

- #1064, #899, #944, #1112, #1142, #1188 and the sourcing Issues #1031, #1032 and #1147 were in or
  near the first-pass list and are placed as unaffected.
- #1010, #1052, #1062, #1063, #1069 and #913 were not in the first-pass list as affected (#913 was
  on the check list) and are placed as affected.
- The statements marked *reading* in D-4 and D-37, and the mapping of #914 c.6777841157's three
  gates to parts of the target, are interpretations.
