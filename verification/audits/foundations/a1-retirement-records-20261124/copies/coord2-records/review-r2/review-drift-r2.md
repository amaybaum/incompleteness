# Independent review r2: drift reconciliation proposal r2 and its three draft records

Reviewer: the same independent non-author session as `review/review-records.md` and
`review-r1/review-drift-r1.md`. The review was read-only: no repository, git or GitHub writes. I
used `git show`, `rev-parse`, `rev-list`, `diff` and `log` on `<repo>`, and
`gh api` GET requests. I did not run the writer's `r2-work/` scripts. Their outputs served only as
the subject under check.

## Inputs

All 11 entries of `coord2-records/MANIFEST-r2.sha256` verified with `sha256sum -c`. The brief speaks
of 13 files, but the manifest lists 11 entries.

| File | sha256 |
|---|---|
| `DRIFT-RECONCILIATION-PROPOSAL-r2.md` | bfc6fa25ec4861d2ff927598a5a20cc5de830abd97d41e956c2f1b4aeeabc072 |
| `DRIFT-CHANGES-r2.md` | 3b1b2e6754e3318ac752a15955b28ac3fc275f7053c192227bdbf9b58b3b3ccb |
| `records-draft/a1exit-recon-agents-md-1.json` | 4417df9aa48f3affc00421a22c9f440be92b5737ad01c795b5febc13cb11d571 |
| `records-draft/a1exit-scc-tool-configuration-1.json` | d225a6663fda78dc4a28da6776942bbdede5aeb8e8ae01ae20adbd4f9801ecab |
| `records-draft/a1exit-scc-trial-workflow-1.json` | bc23c80f08bee5596797ef25fd5ec5aa9e463de35931e62ee91d3c74eec60674 |
| `r2-work/variant-pr1553-head/` (3 files) | listed in the manifest; all OK |

Objects used:

| Symbol | Object |
|---|---|
| H | 53c6601a |
| P | 4c79be64 |
| W | 413b0bb8 |
| M | 4fb2c1ee (`gh api` shows `main` still at M) |
| Q | 47e23023, PR #1553's head; still open, not merged |
| T1' | 14ac71b4 |

My script is `rv2_records.py`, with output in `rv2_records.out`. It recomputes every field of each
draft record from git objects, re-checks the record at M and the variant at Q, and diffs the draft
against the variant field by field. It reported 0 failures.

## Verdict: ACCEPT WITH REQUIRED CORRECTIONS (2)

I found nothing blocking. Every field of the three drafts re-derives exactly. My four r1 corrections
are resolved. The four optional points are adopted. The PR #1553 variant changes only the
reconciliation record. Both required corrections tighten the definition of when the record applies.
Neither changes a value in the drafts.

***

## 1. The four r1 corrections

| # | Status | Where |
|---|---|---|
| 1. Record location | Resolved. The records sit in the tool's audit directory and land with the tool. The safeguard reads them from the tree of the predicted M. The configuration at F pins the same `{path, blob_sha256}`. Relocation needs a new authorization, which N8 checks. This is the in-design option. | sec. 4.1, 5, 4.4 N8 |
| 2. N4 outcome | Resolved. N4 now names `landing-conflict-unresolved` (v2 sec. 13.2, "both changed") and says why `landing-drops-main-change` does not apply. | sec. 4.4 |
| 3. Blob ids | Resolved. The values X 9f4fc3e8, L at M 4075b78a, main with #1553 2503bb8d and L with #1553 3ce53ebb are confirmed (sec. 3). | sec. 4.2, R7, R8 |
| 4. Stage 1 expectation | Resolved. The tool's landing paths and any fixture drafts are listed (REVIEW and N11 `record-invalid` respectively). | sec. 5 |

### The writer's extra change: `main.computed_at`, binding, re-check at every run

The record names the commit it was computed at and asserts two facts: the AGENTS.md blob at `main`
(R2), and the exact list of first-parent commits on H..main that change AGENTS.md (R1). At every
run, meaning the safeguard, F and landing, it applies only if R1-R12 hold against `main` resolved
afresh.

**Against design sec. 13.1 to 13.4.**

- Sec. 13.1 keeps the recorded M at each run: the first parent of L is the M resolved and recorded
  for the landing. The record does not replace M; it is a condition evaluated at M.
- Sec. 13.3 is respected. The record is authorized before F and pinned by F's configuration. A change
  to AGENTS.md after F invalidates it through R1 and R2, so only a new record can cover it. The
  post-F rules allow a new record for an unforeseeable side change only.
- Sec. 13.4 re-resolves M before landing, and the re-check runs against that M.

The change is sound. Naming `M_F` was impossible for a record authorized before the tool lands, and
`computed_at` plus run-time binding is the correct replacement.

**Can later drift pass unreviewed?** No path I found does, provided the two corrections below are
made.

- A later change to AGENTS.md fails R2 (blob) and R1 (commit list), even if it is later reverted to
  the same blob. The result is `base-drift`.
- A later change to any other ledgered file fails R10.
- A later change to any corpus path fails R11's first clause. No class record can cover such a path.
- Any other changed path needs a class record whose pinned blob matches, and that record has its own
  review and authorization under sec. 6.3. Otherwise it is REVIEW `side-change-unclassified`.

Two gaps in the *definition* remain:

- **(a) The ledger used at the run.** The record pins `ledger.json` and `edits.json` at P (blobs
  2055e68f… and 528f146d…, confirmed), with the note "at F, the ledger pinned in F's table". R8 and
  R10 read "the pinned `ledger.json`" and "the ledger's `expected_sha256`" without saying which
  ledger that is. No item requires the ledger that the configuration uses at the run to be the one
  the record pins.
  - The re-freeze may well change `ledger.json` or move it.
  - In that case it is undefined whether the record applies.
  - If R8 read the record's own pinned P ledger while the configuration used an amended ledger with
    another AGENTS.md splice, R8 would pass on stale data. The landing check `expected.L` would
    still catch it, but only at landing.

  See required correction 1.
- **(b) Inconsistent wording inside the draft.**
  - `item_text.R1` says "main resolved by git ls-remote **at F**". The proposal (sec. 4.2, 4.3) and
    `main.applies_while` say "at every run".
  - `applies_while` names "R1-R11". The proposal names R1 to R12.

  See required correction 2.

## 2. The adopted optional points

- **Self-reference.** Stated as a requirement on the tool-landing class record, which is outside
  this proposal. Record files are matched through the configuration's `records` list, and the class
  record lists itself nowhere. Sound.
- **R11 and the plan amendment; R's tree.** R11 names the amendment's paths. The note on R's tree is
  added. Sound.
- **Reported form.** Reconciled drift is reported as a distinct item naming the record, never as
  `base-drift`. The exact name is left to Stage 1 and goes into the controls file. Sound.
- **PR #1553 head.** Q is given as the current head, beside the stale description head 6a547791.
  Confirmed with `gh api`.

## 3. Draft records: every field re-derived (rv2_records.out, 0 failures)

### `a1exit-recon-agents-md-1.json` (git blob dbddbfe3, 7527 bytes)

- **Identity and status.**
  - `schema` `oi-reconciliation/1`, `id`, `supersedes` null, `scientific_base` H = ledger `base`.
  - `main.computed_at` = M.
  - `draft_status` states UNREVIEWED, UNAUTHORIZED and "record-invalid".
  - `author` and every `ownership_chain` value are `<PLACEHOLDER…>`.
- **Pins.**
  - `ledger`: path, commit P, sha256 2055e68f…32b5, git ba37c1cd.
  - `edits`: path, commit P, sha256 528f146d…dec1.
- **The path and its blobs.**
  - `side_change_commits` = [4fb2c1ee]. Recomputed by walking `rev-list --first-parent H..M` and
    diffing each commit against its first parent.
  - `blobs.H`: git 12a9281f, sha256 d87acac5…, 102250 bytes.
  - `blobs.M`: git 4a348007, sha256 f75e0d58…, 104517 bytes.
  - `common_prefix_H_M_bytes` 46677.
- **`main_changes`.** Verified by reconstructing M from H: an insert at [46677, 47031) on M lines
  715-718, after H line 714, and an insert at [102604, 104517) on M lines 1524-1551, after H line
  1519 (H's last line).
- **The splice D296.**
  - Byte span 2332-2382 at H and at M, identity translation (prefix 46677 ≥ 2382).
  - `old_sha256` 8711166b… and `new_sha256` 532c5919… match both the ledger and the text.
  - The `old` text occurs exactly once at H and exactly once at M.
  - `char_offset_H` 2305; lines [37, 38].
- **`protected` §A.49.** [102610, 104517), sha256 07c69d0b…. The header occurs once. In M + D296,
  §A.49 is byte-identical at offset −23, and so is every byte after the splice.
- **Expected blobs.**
  - `expected.X`: git 9f4fc3e8 (= T1''s blob), sha256 59b68984… = ledger `expected_sha256`.
  - `expected.L`: git 4075b78a, sha256 31bf9ac2…, 104494 bytes.
  - `length_delta` −23.
- **Remaining fields.**
  - `unchanged_ledgered` 43: each of the 43 has the same blob at H and M, equal to its
    `base_sha256`.
  - No `papers/` or `book/` path changed between H and M.
  - `side_change_classes`: both references match the draft class files (sha256 d225a666… /
    bc23c80f…; git baf74eff / 7c28e8b7).
  - `changes_decisions_on_X` [].
  - `items` R1-R12 with matching `item_text` keys.

### `a1exit-scc-tool-configuration-1.json` (git baf74eff, 2093 bytes)

- `schema` `oi-side-change-classes/1`, `id`, `supersedes` null, `scientific_base` H.
- One item: `.claude/settings.json`, class `tool-configuration`, blob git b7f9b0a6 / sha256
  ad4130d0… at M and at Q.
- `blob_at_H` null (absent at H).
- Introduced by first-parent commit 4fb2c1ee, the only first-parent commit that changes the path.
- Not in the ledger. `ledgered` and `corpus` are false.
- Marked as a draft, with placeholders.

### `a1exit-scc-trial-workflow-1.json` (git 7c28e8b7, 2507 bytes)

- One item: `.github/workflows/a1exit-trial-verify.yml`, class `trial-workflow`, blob git bca44ac0 /
  sha256 f8c36855… at M and at Q.
- `blob_at_H` git dfcfd732 / sha256 5c767c9f….
- Introduced by 413b0bb8 = W, the only first-parent commit that changes the path.
- Not in the ledger.
- The basis cites PREREG §31.12.7 at P.
- Marked as a draft, with placeholders.

All three files carry an explicit `draft_status` stating that they are unreviewed and unauthorized
drafts, which the tool must reject as `record-invalid`. All three keep the review and authorization
as placeholders. Sec. 8 correctly says that `draft_status` and `ownership_chain` are removed before
review. It also says the class records are finalized first, because the reconciliation record pins
their blobs. Consequently none of the hashes above is final.

## 4. The PR #1553 variant

- **Class records.** The two class files in `variant-pr1553-head/` are byte-identical to the drafts.
- **Reconciliation record.** The variant re-derives in full at Q with 0 failures. Against the draft,
  exactly these fields differ, and each value matches sec. 7's table:

  | Field | Draft (M) | Variant (Q) |
  |---|---|---|
  | `main.computed_at` | M | Q |
  | `blobs.M` | git 4a348007, sha256 f75e0d58… | git 2503bb8d, sha256 702dbf57…, 105492 bytes |
  | `main_changes[1]` end | | 105492, line 1572 |
  | `protected[0]` (§A.49) | | end 104848, sha256 7601f051… |
  | `expected.L` | | git 3ce53ebb, sha256 b7fdda74…, 105469 bytes |
  | `side_change_commits` | [4fb2c1ee] | adds 4e375f6e, 6a547791, 47e23023 |

  For `side_change_commits`, Q's own first-parent chain is the dry-run stand-in, as sec. 7 states.
- **The D296 entry is unchanged, and §A.49 and every byte after the splice are unchanged** at Q
  shifted by −23.
- **One small mismatch.** Sec. 7's table lists `id` and `supersedes` as changing. The variant file
  keeps `id` `a1exit-recon-agents-md-1` and `supersedes` null. Sec. 7 calls it a dry run whose hash
  is not a real regeneration's, so this is consistent in substance, but the text should say so (see
  the optional points).

## 5. Blocking issues

None.

The owner decision named in sec. 5 is correctly identified as not yet given: authorizing the records
before the tool lands. Whether that act falls under §A.50 item 2, if #1553 merges, is correctly left
to the owner.

***

## Required corrections

1. **Bind the ledger and edits used at each run (sec. 4.2-4.3; record `ledger`, `edits`, R8, R10).**
   State that R6, R8 and R10 read the ledger and edit list that the configuration uses at the run.
   Add a check, either a new item or an extension of R8, that the record applies only if both of
   these hold:
   - that ledger's blob sha256 equals `ledger.blob_sha256`, and that edit list's blob sha256 equals
     `edits.blob_sha256`, or, at minimum, the AGENTS.md `files` entry and the AGENTS.md splice list
     are byte-equal to the pinned ones;
   - otherwise the record does not apply, and a superseding record is needed.

   Without this, whether the record applies after the re-freeze changes or moves `ledger.json` is
   undefined. With it, a stale record fails closed at the run rather than only at landing.
2. **Make the draft's own wording consistent (record `item_text.R1`, `main.applies_while`).**
   - In R1, replace "resolved by git ls-remote at F" with "at each run (the safeguard, F and
     landing)".
   - Make `applies_while` say R1-R12, as the proposal does.

## Optional

- **Sec. 7.** Note that the variant file keeps the draft's `id` and `supersedes`, and that a real
  regeneration changes both, as the table says.
- **Class records.** The `checks` bind only the blob. If wanted, also record the first-parent commit
  list for the path, as R1 does for AGENTS.md. The blob binding already makes this fail closed for
  any content change, so it is not needed.
- **Manifest count.** The brief speaks of 13 files, but `MANIFEST-r2.sha256` has 11 entries. If two
  files were meant to be covered, add them.

## Not verified

- The tool's behaviour and rule ids. The tool does not exist; every outcome is the design's stated
  behaviour.
- The final record hashes. The drafts are not final: `draft_status`, `ownership_chain`, `author`
  and the directory name all change before review.
- Anything merged to `main` after M. `main` was still M when checked.
- Whether a merge of #1553 leaves AGENTS.md equal to Q's blob. It does for a plain merge of Q; this
  is to be re-read at the actual merge.
