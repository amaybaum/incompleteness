# Changes from `DRIFT-RECONCILIATION-PROPOSAL.md` to `DRIFT-RECONCILIATION-PROPOSAL-r1.md`

Base draft: `DRIFT-RECONCILIATION-PROPOSAL.md` (sha256
f870c7630b41ecf0cd218a2a525ae4a7941d1942978633b654d8040628aa2c2d).
Review: `review/review-records.md` (sha256
1ef18f194efa1c2055874f0ccac51ef55b902e1dcd2e6420af05859ef256a5f8), document B, verdict REVISE.
Owner decision: #1169 comment 7099655517 (`amaybaum`, 2026-11-23T11:26:50Z).
Section numbers below refer to the r1 proposal.

## Review's required corrections (document B)

| Correction | Finding | What r1 does | r1 sections |
|---|---|---|---|
| 1. D296 offset in bytes | B1 | Gives D296 as bytes 2332 to 2382 (end exclusive), lines 37-38, at `H`, `M` and PR #1553's head. Gives the character offset 2305 separately, with the reason it differs. `sha256(M[2332:2382])` = `old_sha256`. | 1.2 ("Position"); 4.3 R3-R4 |
| 2. Not append-only | B2 | States that #1552 inserted 4 lines into the lessons register (`H` byte 46677; `M` bytes 46677-47031, lines 715-718), and that the 28-line §A.49 block is appended (`M` bytes 102604-104517). Removes "append-only" and "no byte before them changed". Keeps the conclusion that every change lies at or after byte 46677, so D296's span is untouched and its translation is the identity, and that no §A.49 byte changes under D296. | 1.2 ("What #1552 changed", "§A.49"); 2 (table row `AGENTS.md`) |
| 3. Workflow role; `{path, blob_sha256}` pins | B3 | Cites PREREG §31.12.7 at `P` (`W` as the workflow base; `preserve_check.py` enforces `W`'s blob at each dispatch head) as the basis of the `trial-workflow` class. Pins both classified files by `{path, blob_sha256}`, with re-derived hashes: settings ad4130d0...5b9b (git b7f9b0a6); workflow f8c36855...1646 (git bca44ac0). Pins them both in `roles.side_change_classes` and inside the `oi-side-change-classes/1` record, so either reading of sec. 16.2 is met. Adds control N10. | 1.1; 1.3; 2; 4.4 N10 |
| 4. Re-base option | B4 | Withdraws the one-path re-base, giving four reasons: sec. 13.1's base invariant; drift is defined by paths changed `H..M`; `X` = `H` + splices; and the owner's exclusion of a silent baseline update. Records moving `H` to H′ as excluded by c.7093128173 and c.7099655517, and lists what such a move would carry. | 3.2; 3.3 |
| 5. Sec. 13.3 reading; pre-`F` record | B5 | States that sec. 13.3's foreseeability limit applies only to records written after `F`. Adopts the reconciliation record written, reviewed and authorized before `F` and frozen with `F` as the chosen approach, per the owner decision. Explains how it satisfies sec. 13.1's landing composition rule without moving `H`. | 3.1; 4 |
| 6. Stage 1 outcome; sec. 13.4 safeguard | B6 | States the expected Stage 1 predicted-main result without the records: FAIL `base-drift` on `AGENTS.md`, REVIEW `side-change-unclassified` on the two other files, overall FAIL. This is correct and not suppressed. States how sec. 13.4's no-`base-drift` requirement before the tool lands is met with the record: the records are authorized before the tool lands, RT-L2 runs with a predicted configuration, and the same blobs are frozen at `F`, with recomputation if `main` moves. Flags that authorizing the records before the tool lands needs an owner decision not yet given. | 5 |

## Review's optional points (document B)

| Point | What r1 does | r1 sections |
|---|---|---|
| sha256 of `AGENTS.md` at `H` and `M`, and of `M + D296` | Given in full, with git blob ids; adds `H + D296` = `T1'` = ledger `expected_sha256`. | 1.1; 1.2 |
| Term-regex counts unchanged at `M` | Stated, and extended to PR #1553's head and to the two classified files. | 1.3; 6 |

## Owner decision c.7099655517

| Element of the decision | Where r1 applies it |
|---|---|
| The §A.49 merge is real baseline drift | 0; 2 (`AGENTS.md` row); 3.1 |
| The drift failure is not suppressed | 2 ("Tool outcome" column); 3.4; 4.4 N0; 5; 7 |
| No baseline is updated silently | 3.2 (reason 4); 7 |
| Keep `H` unchanged | 3.1; 3.3; 7 |
| Reconcile through a reconciliation record frozen with the re-frozen plan, not a re-base of `AGENTS.md` alone and not a move of `H` | 3.1 (chosen); 3.2 and 3.3 (excluded); 4 (record) |
| `.claude/settings.json` = tool configuration | 2 (`tool-configuration`, SC1) |
| `.github/workflows/a1exit-trial-verify.yml` = trial workflow | 2 (`trial-workflow`, SC2) |
| The record shows that D296 identifies exactly one location | 4.3 R3, R4; 4.4 N1 |
| The record shows that D296 yields the approved text | 4.3 R6, R7, R8; 4.4 N4 |
| The record shows that D296 changes no byte of §A.49 | 1.2; 4.3 R9; 4.4 N5; 6 |
| Approach approved only; nothing amended now | 0; 7 |

## Further items requested for r1

| Item | r1 sections |
|---|---|
| Record content: schema per sec. 6.3 chain and sec. 16.2 pinning; asserted facts; verifier checks from git objects (uniqueness at `H` and `M_F`, approved text, §A.49 bytes, other ledgered paths unchanged); controls in both directions | 4.1; 4.2; 4.3; 4.4 |
| PR #1553: bytes changed, D296 span and lines 37-38, plan-pattern hits; the record computed against `main` at freeze time | 6 |
| What the proposal does not do | 7 |

## Removed from the draft

- "the same byte offset (2305, line 37)": corrected (correction 1).
- "The 32 added lines are appended after the last section; no byte before them changed" and
  "append-only change": corrected (correction 2).
- Option 1 "Re-base at the plan amendment (recommended)": withdrawn (correction 4, owner decision).
- Option 2's "fits poorly if the freeze happens after today": replaced by the correct reading of sec.
  13.3, and made the chosen approach as a record frozen with `F` (correction 5).
- The `tooling-config` and `trial-workflow` class records without blob pins: replaced by the pinned
  classes `tool-configuration` and `trial-workflow` (correction 3; class names follow the owner's
  wording).
