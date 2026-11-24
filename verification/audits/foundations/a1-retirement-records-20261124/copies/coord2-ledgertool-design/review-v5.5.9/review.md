# Independent bounded check: DESIGN-v5.5.9 (owner decision D-1, Option A)

Verdict: **ACCEPT**

## Inputs verified (sha256)

- DESIGN-v5.5.8.md f531948147b3638c5ad567f5ccf0eedfd04650a30be9fd0a9f2084aa13a77ad2 (matches)
- DESIGN-v5.5.9.md cdfbe08cd9ec331ac94e9d57d66f0e0c919cc2ff17038a8475a1ff2d7a779df9 (matches)
- CHANGES-v5.5.9-from-v5.5.8.diff 53a42cbed1cdd110ce94eb45efbe3e8cafa99910f9e926ccbd49c3980ce6f2f2 (matches)
- v5.5.9-MANIFEST.sha256: `sha256sum -c` OK for all three entries
- review-stage1-r6/review.md 0bf9a3ad1c56cd9bf0e0b30f2b0653ee5fc8827f023049ffec65e139f3fd2392 (matches; D-1 at its sec. 4)

## Check 1: scope — PASS

`diff DESIGN-v5.5.8.md DESIGN-v5.5.9.md` gives exactly three hunks, identical to the supplied diff:
line 1 (title v5.5.8 -> v5.5.9); lines 10-14 added (one status bullet describing the D-1 amendment,
naming v5.5.8 as authoritative until ACCEPT and adoption); line 2809 (v5.5.8 line 2804) where
"The empty freeze ledger lands with it." becomes "The empty freeze ledger lands in its own merge
after it, approved under “Owner at creation”." This is the owner's wording character for character,
curly quotes included. No other line differs. (Cosmetic only: the new line is not rewrapped and runs
past the document's usual width; rewrapping would not be in scope.)

## Check 2: consistency with DI-1 and the authority-change procedure — PASS

Trace for the first, empty ledger landing in its own merge after the first `A`:

- Sec. 6.3 "The freeze ledger", "How it changes" (l. 1453-1455): every ledger change lands through
  the authority-change procedure with an `oi-authority/1 approve` quoting the old and new ledger blob
  hashes. The procedure (l. 1414-1426) requires the approval comment in `A.authority_thread`, an
  independent review record naming both blobs, and a PR merge into `main` with merged-by equal to the
  owner (provenance).
- "Owner at creation", Approvals (l. 1344-1350): the approval counts only if it is an owner comment,
  its author equals the `owner.id` of the authority record governing the evaluation, which for a
  freeze-ledger change is "the version in force at its merge", and no owner change merged between its
  creation and that merge. Definitions (l. 1328-1333): a comment created when no version of `A` was
  in force is not an owner comment; "in force" requires a landing merge strictly before.
- Hence the approval must be created after the first `A`'s merge, and the ledger's merge is a
  separate, later merge, during which the first `A` is in force. This is exactly the amended route
  and it is admissible: owner 7273571 is in force, posts the approval, the review record is made, the
  owner merges.
- Different route impossible: in the same merge as the first `A`, no version is in force at the
  merge, so no governing record exists and no comment can be an owner comment (also r6 probe P3).
  The first-`A` exemption (l. 1357-1361, 1427-1429) is limited to the approval of `A` by the id it
  pins and does not extend to the ledger.
- N3 (l. 1456-1473): the `oi-freeze-ledger/1 append` comment governs appends of observed events
  (per plan and round). The first ledger is empty, adds no events and is not an acceptance-time
  append; N3 neither requires nor bars anything for it.
- Interim: between the two merges the ledger is missing at `A.freeze_ledger_path`; every admission
  then refuses (l. 1480-1481; TR36). Fail-closed; no rule requires the ledger to precede designations,
  and 0a requires only `A` before any freeze.

## Check 3: other passages — no conflict

Searched the whole of v5.5.9 for the first ledger, "lands with", same merge, approvals predating the
first `A`, and the initialization sequence.

| Line(s) | Passage | Conflict? |
|---|---|---|
| 14 | status bullet describing the amendment | no |
| 37-38, 47 | v5.5.2 status (N3: every acceptance-time append needs its own owner approval); D3 adopts the ledger with N3 | no |
| 1302 | `freeze_ledger_path` field of `A` | no (path pinned in `A`; ledger may arrive later) |
| 1319 | `oi-authority/1 approve from=<sha256 of the A replaced, or "none"> to=...` | no (see note 1) |
| 1326-1368 | "Owner at creation" (definitions, approvals, first `A`, completed actions) | no; it forces the amended route |
| 1414-1431 | Authority changes; "The first `A`"; every change to `A` | no; the first-`A` exemption names `A` only |
| 1446-1489 | The freeze ledger, N3, reconciliation (missing ledger refuses), residual | no |
| 1571-1590 | residual trust assumptions: lists only the first landing of `A` | no; consistent with check 4 |
| 2309-2310 | TR26, TR27 (bootstrap order: `F` must descend from `main` containing `A`) | no |
| 2314-2315, 2319 | TR31, TR32, TR36 (ledger missing/unverifiable -> ERROR) | no; TR36 covers the interim |
| 2330 | TR47 (acceptance-time append approvals) | no |
| 2340-2343 | TR57-TR60 (ledger-change approvals across owner changes; TR60 positive) | no; all presuppose an owner in force |
| 2805-2810 | sec. 15 item 0a (amended) | the amendment itself |

`R4-B2` does not occur in v5.5.9 (0 matches); nothing to check. No passage says or assumes the empty
ledger lands in the same merge or commit as the first `A`, or that a ledger approval may predate the
first `A`.

## Check 4: not an exception to DI-1 — PASS

The amended sentence routes the first ledger through the ordinary procedure and "Owner at creation";
it adds no exemption and no trust assumption. The residual list (l. 1585-1586) still names only the
first landing of `A`. Option B (an exemption) is not introduced.

## Non-blocking notes (no change required by this check)

1. The design does not spell out the `from=` value of the `oi-authority/1 approve` for the first
   ledger, which has no predecessor blob. The form's literal grammar admits `from=none`; the review
   record "names both blobs" likewise has only one. This underspecification predates v5.5.9 (it applied
   equally to v5.5.8's same-merge wording) and is not created by the amendment.
2. The amended line is not rewrapped (cosmetic).
