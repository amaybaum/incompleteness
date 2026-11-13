# Working notes: STATUS.md for PR #1274

Writer pass under #1169 c.6865177667 OQ-1 (`amaybaum`, 2026-11-13T21:19:31Z): prepare a `STATUS.md`
for #1274 only; reviewed files unchanged; no merge. Scope kept narrow per #1274 c.6863419164.
Nothing committed, pushed or posted. No file other than `STATUS.md` and this note written.

## Sources read

- Package at `research/optc-1230-1232-20261113` = `d015131d6aad4ab09f80a7a78eb123384430186d` (read-only
  checkout): NEW-RESULTS.md, DEPENDENCIES.md, PROVENANCE.md, CHANGES.md, review/REVIEW-r1.md,
  review/RESPONSE-r1.md, review/CONFIRM-r2.md.
- Integration assessment, branch `research/integration-assess-20261113` fetched by name without
  `--depth`, read with `git show` at `c7ce4f2852cb90883b7a7c8ed645ba09db19f7ca`:
  INTEGRATION-ASSESS-r2.md (§0 item 1, §1, §2.2 #1274, §3 #1274, §4 step 1, §6 Basis, §7 OQ-1/OQ-9/OQ-10),
  REVIEW-r1.md (F6, F7, F8, F9, F11), CONFIRM-r2.md (incl. optional note A).
  The branch head moved during the pass to `d82dd02d` (adds NOTE-OQ10.md only; `c7ce4f28` is its
  parent). NOTE-OQ10.md skimmed: consistent with the basis wording used (practice, not literal
  item 2; ruling open).
- ChatGPT review 5895564670 via REST: user `amaybaum`, submitted 2026-11-13T17:44:35Z, commit
  `d015131d6aad…`, state COMMENTED. Integration requirements 1–3 copied byte-for-byte into STATUS.md
  (markup kept).
- OA-1 precedent: `origin/main:verification/programmes/oi-qm/reconstruction/oa-1-20261112/STATUS.md`.
- Owner comments via REST (author, created_at): #1169 c.6854728636 (amaybaum, 13:45:13Z);
  c.6855167580 (14:02:39Z); c.6863414487 (19:58:05Z); c.6865177667 (21:19:31Z); #1274 c.6863419164
  (19:58:18Z); #1265 c.6846206075 (06:44:20Z). All 2026-11-13.
- #1169 comments after 14:03Z grepped for #1230/#1232/step 5/#1274: no record replaces the
  2026-11-11 draft approvals. #1230, #1232, #1271 PR comments: none after their r2/r3 checkpoints.

## Measurements (2026-11-13)

- `git ls-remote`: main `c3b5f37a`; optc `d015131d`; rec-1 `3a3aa146`; intervene `ea12fde1`; substate
  `86a413c8`; reconcile `703ae20e`; bell-scope `e1534b08`; approx r4a `e41cf613`.
- PRs #1274, #1230, #1232, #1271, #1221, #1231, #1268: all open drafts (REST).
- `REC-1-r7.md` blob `f1ffac0e…` at `9f7d2612`, `cd38655c`, `3a3aa146`.
- Package blobs at `d015131d` and SHA-256 of each file: as tabled in STATUS.md (git ls-tree; sha256sum
  of `git show`).
- Last change to the four record files: `4b40dcdc`. Review files committed at `3f56d543` (REVIEW-r1),
  `4b40dcdc` (RESPONSE-r1), `d015131d` (CONFIRM-r2).
- `git merge-tree --write-tree origin/main d015131d`: exit 0. Check runs at `d015131d`: 26 success,
  1 skipped. (Not stated in STATUS.md: merge-time checks belong to the final head.)
- `tools/claims_check.py --root <status dir>`: OK; `tools/staleness_check.py`: OK.
- Forbidden-string grep of STATUS.md (path prefixes, session-storage word, "now", "no longer",
  "still", "currently"): one hit, "currently", inside a verbatim quotation of NEW-RESULTS.md:11–15.

## Decisions

- Heading "What the record supports, and at what strength" (assessment REVIEW-r1 F7).
- Superseded lines (F8): DEPENDENCIES.md:31 (row H head `cd38655c` "at this writing") and
  PROVENANCE.md:17 (same head "at writing"). PROVENANCE.md:17 carries the same time-indexed fact as
  row H; the assessment names row H only. Not listed: PROVENANCE.md:100 (F8: accurate), the
  "(open, draft)" states (measured: true), PROVENANCE.md:13 (heads measured: equal).
- Own-branch commits (F11) plus `d015131d`, which this note and review 5895564670 cite.
- Optional nit DEPENDENCIES.md:18 not applied (assessment §3, F9 reason).
- Basis stated as owner practice, ruling open (OQ-10); "not established" grounded in the record's
  own label rather than asserting the item-1 question (CONFIRM-r2 note A).
- §A.46 item 4 categories: "independently verified: none; known-invalid: none known"; whether
  model-written hand checks count as "partially verified" left to OQ-10, not decided.
- Accountable Issues: A1, D2, D3 → #1169; E2 → #868 (#1231 is the Bell-scope unit under #868;
  DEPENDENCIES row E2 ties it to the Bell ladder #868). Assessment wrote "under #868/#1169".
- REVIEW-r1 counts not restated: its summary says "Ten should-fix items" but its headings list
  findings 2–12 (eleven). STATUS.md says "findings 1–12, finding 1 blocking, and nits 1–13".

## Open points for the caller

1. c.6865177667 OQ-2/OQ-3 names #1231 and #1232 L3, not #1232 L2; gap D3 needs L2 (and class (a)3).
2. E2's accountable Issue (#868) differs from the assessment's "#868/#1169"; confirm.
3. PROVENANCE.md:17 listed beside row H as superseded; the assessment's step 1 names row H only.
4. The REC-1 head (row H) is re-measured at landing; STATUS.md records `3a3aa146`.
5. The package REVIEW-r1 should-fix count inconsistency (ten vs eleven) is in a reviewed
   file and is left unchanged.
