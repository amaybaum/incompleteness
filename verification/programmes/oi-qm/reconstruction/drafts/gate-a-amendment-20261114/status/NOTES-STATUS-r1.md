# Notes for STATUS-r1.md: what was read, and what was not checked

Writer's reading list for `STATUS-r1.md`. Paper-only: reading, `git` inspection, `diff`/`cmp`, grep
and public GitHub API reads. No computation on OI models, no Lean build, no repository checker run,
and nothing edited, committed, pushed or posted in any checkout or on GitHub. One `git fetch origin
main` was run in the checkout of the record branch, to read `main` by name. Times are UTC, 2026-11-14.

## Repository

- Checkout of branch `research/gate-a-amendment-1169-20261114`: `git rev-parse HEAD` =
  `927915e9923281dae3da9d414fa349ccbb5d8643`; `git ls-remote origin` returned the same head and
  `main` = `dfeec843bec08443b25cffe34d33dc8401c3b604` (about 12:12Z). Working tree clean in the
  record directory.
- `git log` and `git show --stat` of the five branch commits (`65b0a929`, `ae2de57a`, `cea26912`,
  `eb515150`, `927915e9`), with parents and messages; `git diff --stat c3b5f37a 927915e9` (16 files,
  3413 insertions, all in the record directory); `git ls-tree` blob ids of the sixteen files.
- `git diff eb515150 927915e9` (README change and added `CONFIRM-r4.md`); blob identity of
  `GATE-A-AMEND-r4.md` and `OWNER-QUESTIONS-r4.md` at `eb515150` and `927915e9`.
- Read in full: `README.md`, `GATE-A-AMEND-r4.md`, `OWNER-QUESTIONS-r4.md`,
  `GATE-A-AMEND-r3-TRACE.md` §2–§3. Read in part: `REVIEW-r1.md` (header, §0), `CONFIRM-r2.md`
  (header, §1, K1), `CONFIRM-r3.md` (header, verdict), `CONFIRM-r4.md` (header, verdict, §5–§7),
  `GATE-A-AMEND-r2.md`:246–251, `OWNER-QUESTIONS-r3.md`:8, `RESPONSE-r1.md`:14–15. Grep of all
  sixteen files for branch names, PR and Issue numbers, comment ids and checkout names.
- `main` at `dfeec843`: `AGENTS.md` §A.42 and §A.46 (item 8 present); `git diff c3b5f37a dfeec843`
  touches `AGENTS.md` only (two hunks in §A.46); `endpoints.md` blob `d9d92e03` at `dfeec843`,
  lines 19–29, 51–69, 114–123, 155–179 read; `papers/Main.md`:562, :598 and `papers/GR.md`:162
  located by content; ancestry of `fdc3dd7f`, `9d24914c`, `dc0b333a`, `c3b5f37a` to `dfeec843`
  checked; `git grep` at `dfeec843` for the record's directory and file names: no hit.

## GitHub (public API, read about 12:12Z–12:18Z)

- PR #1289: open, draft, head `927915e9`, base `main`, `mergeable` true, `mergeable_state` "behind",
  test-merge commit `29dd4cda` (parents `dfeec843`, `927915e9`, 11:05:47Z); description read in
  full; 0 issue comments, 0 reviews; five commits. Compare `main...927915e9`: diverged, 5 ahead, 9
  behind, merge base `c3b5f37a`.
- Check runs at `927915e9`: 27, from one workflow run, 43588379859 (`verify`, event `pull_request`,
  attempt 1, 11:05:52Z–11:16:17Z); jobs: 26 success, 1 skipped. No other workflow run for that head.
  `main` at `dfeec843`: 27 check runs, 26 success, 1 skipped.
- PR #1283: merged 09:11:18Z, merge commit `dfeec843`, head `bef57cbf`. #1283 comment 6875009394
  (09:10:38Z) read in part.
- PR #1287: open, draft, head `755f9bff`; description and file list read; `TARGET-THEOREM-r3.md`
  (lines 30–36, 121–129 and the T5b rows by grep) and `README.md` read at `755f9bff` through the raw
  content host.
- PR #1288: open, draft, head `485f9a2d`; description and file list read.
- PR #1290: open, draft, head `f5b3ee2d`, created 12:11:34Z; description and file list read.
- Comments read in full: #914 6875046763, 6875548603, 6876304390, 6876592679; #1169 6875724719,
  6876591512, 6874035457, 6874809552, 6875065295, 6875131690. All from `amaybaum`, association
  OWNER. First lines of every #1169 and #914 comment since 2026-11-14T00:00Z listed.
- Issues #914, #1169, #873: state open, labels, title; planning-status blocks read in part (#1169
  searched for writer, authorization and readiness lines).
- Quotation check: the quotations in `GATE-A-AMEND-r4.md` §1 compared with the comment texts by
  string match after whitespace normalization; all match except elided quotations, which match up
  to the ellipsis; "The accepted Gate A contract" is the rendered link text of the #1169 body.

## Working copies (not cited in STATUS-r1.md)

The reviewer working copies of r1, r2, the r2 trace, `REVIEW-r1.md`, `CONFIRM-r2.md` and
`NOTES-r1.md` held beside the checkout are byte-identical (`cmp`) to the committed files. This bears
only on which text the two uncommitted reviews read, and is not evidence on `main`.

## Not checked

- The coordinating sessions in which the owner's words were given; only the comment texts.
- The content of the reviews beyond their verdicts and the passages listed; the amendment's
  mathematics was not re-derived, and the 113-line trace was not re-checked line by line.
- Whether run 43588379859 used the merge commit `29dd4cda`; the run record names only the head.
- The local checks the PR description reports at `927915e9`; none was run.
- Whether any other record on a branch cites this record, beyond PR #1290's description.
- Issue #1143's body, and any Bell-track Issue; the note names none where the record names none.
- `STATUS-INCOMPLETE-DIAGNOSTIC.md` was opened only for its first section and headings; no fact or text was taken
  from it.
