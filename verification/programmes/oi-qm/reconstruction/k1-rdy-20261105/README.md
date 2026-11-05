# K1-RDY recovered text: identification limit (#1031)

This directory holds a retained record. It decides no gate, token or readiness result, and it changes no scientific
status. It changes nothing in K1-RDY-1's record (`../round-k1-rdy-1/`), and it authorizes nothing.

## What the digest establishes, and what it does not

- **Byte identity: established.** Lines 1–313 of `../round-k1-rdy-1/preregistration.md` on `main` have sha256
  `a93f3f33f0c5a6e8b2467312d184fa2d2e915296490948938c4dd7832c64bb63`:

  ```sh
  head -n 313 verification/programmes/oi-qm/reconstruction/round-k1-rdy-1/preregistration.md | sha256sum
  ```

  The same digest results from lines 5–317 of the body of #1031 comment 6567522034, as the GitHub API returns it
  (2026-11-02T02:20:43Z, headed "K1-RDY record, 1 of 2: decision-complete preregistration (verbatim; sha256 prefix
  `a93f3f33f0c5a6e8`). Not frozen."). It also matches the prefix in the table of the gate record, #1031 comment
  6567502036 (2026-11-02T02:19:04Z): "Preregistration (313 lines) | `a93f3f33f0c5a6e8`". So the 313 lines on `main`
  are byte for byte the text posted on 2026-11-02.
- **Acceptance: not established by the digest.** That this posted text is the one the 2026-11-02 reviewer accepted is
  a historical assertion. It rests on two things:
  - the gate record c.6567502036, posted by the coordinating session that also posted the text and the review;
  - the concordance in `SOURCES.md` §2–§3, which checks the posted text against #1031 comment 6567537517 (the review
    record) and the decision records.

  The reviewer's own record names a path and a line count (313), not a digest. The earlier revisions r1 and r2 are not
  retained, so the Confirmation's "no other line changed" cannot be checked line by line (`SOURCES.md` §6, A-2).
  K1-RDY-1's §12 (line 319) calls lines 1–313 the text "accepted on 2026-11-02". That acceptance has this support and
  no other.

## Files

| File | Content |
|---|---|
| `SOURCES.md` | Byte for byte the file of that name on PR #1114's branch `research/k1-rdy-reconstruction-20261105` at `66bee341bd5c2aacd145757f579d7973977245c0` (git blob `973a6d127b7961a16b4e5157972e45614fa77885`, unchanged since `e18b36e3`) |
| `README.md` | This file. Its "Limits" section below quotes the first two items of the "Limits" section of that branch's `README.md` at the same commit |

## How `SOURCES.md` reads on `main`

- `SOURCES.md` is retained as written. Its own status line ("WIP / UNVERIFIED. Not frozen") and its references to
  "this directory" and "this branch" describe the #1114 branch, not `main`.
- `PREREG-RECOVERED.md` is not on `main`. Its 313 lines are lines 1–313 of `../round-k1-rdy-1/preregistration.md`,
  with the same digest. "Line N" in `SOURCES.md` therefore resolves to line N of that file, for N ≤ 313.
- **Review.** The #1114 review, PR #1114 comment 6649791225, reviewed `SOURCES.md` at `794ebeb5` and returned ACCEPT
  WITH CHANGES. Its required revisions to `SOURCES.md` were applied at `e18b36e3`. Independent review of the retained
  copy is pending on the pull request that adds this directory.
- **Open items.** The items of `SOURCES.md` §4–§7 have homes in K1-RDY-1's amendments A1–A9 (#1031 comment
  6665340769 §2). The exception is §5 P-4, the RR-1 carry-forward mapping. That mapping, with its outstanding findings
  and who is responsible for each, is recorded in #1031 comment 6665594544. K1-RDY-1 did not discharge those findings.

## Limits

Quoted from the #1114 branch's `README.md` at `66bee341`:

> - The digest identifies the text the coordinator posted and hashed on 2026-11-02 (#1031 c.6567502036). That the
>   posted text is the one the reviewer accepted rests on that record and on the concordance in `SOURCES.md`. The
>   reviewer's own record names the file and its line count (313), not its digest.
> - Earlier revisions of the preregistration (r1, 275 lines; r2, 312 lines) are not retained anywhere found.

## References to content not on `main` (§A.42 item 8)

| Reference | Claim | Class |
|---|---|---|
| #1031 comment 6567522034 | the posted text equals lines 1–313 on `main` | The bytes are on `main`. The comment is the object compared, and the recipe above re-checks it through the API. Its header's prefix is quoted here |
| #1031 comments 6567502036 and 6567537517 | the historical acceptance | Provenance for an assertion this record does not establish. The table row cited is quoted here |
| PR #1114 branch at `66bee341`, and commits `794ebeb5` and `e18b36e3` | source of `SOURCES.md` and of the quoted lines | Provenance. The copied bytes are in this directory, and the branch is kept |
| PR #1114 comment 6649791225; #1031 comments 6665340769 and 6665594544 | review status; homes of open items | Provenance and planning records. No claim here rests on them |
