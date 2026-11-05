# K1-RDY recovered text: identification limit (#1031)

This directory holds a retained record. It decides no gate, token or readiness result, and it changes no scientific
status. It changes nothing in K1-RDY-1's record (`../round-k1-rdy-1/`), and it authorizes nothing.

## What the digest establishes, and what it does not

- **Byte identity with the posted text.** The digest of the 313 lines on `main` can be reproduced from `main`. Lines
  1–313 of `../round-k1-rdy-1/preregistration.md` have sha256
  `a93f3f33f0c5a6e8b2467312d184fa2d2e915296490948938c4dd7832c64bb63`:

  ```sh
  head -n 313 verification/programmes/oi-qm/reconstruction/round-k1-rdy-1/preregistration.md | sha256sum
  ```

  The posted text is #1031 comment 6567522034 (2026-11-02T02:20:43Z). It is headed "K1-RDY record, 1 of 2:
  decision-complete preregistration (verbatim; sha256 prefix `a93f3f33f0c5a6e8`). Not frozen." Lines 5–317 of its
  body, as the GitHub API returns it, give the same digest:

  ```sh
  curl -s https://api.github.com/repos/amaybaum/incompleteness/issues/comments/6567522034 | jq -j .body | sed -n '5,317p' | sha256sum
  ```

  The independent reviews of PR #1114 (comment 6649791225 §1) and PR #1150 (comment 6665794090) report this match and
  a `cmp` identity. The table of the gate record, #1031 comment 6567502036 (2026-11-02T02:19:04Z), records the same
  prefix: "Preregistration (313 lines) | `a93f3f33f0c5a6e8`". So the 313 lines on `main` are byte for byte the text
  posted on 2026-11-02. That comparison needs the comment, which is not on `main`; `main` alone reproduces only the
  digest of the 313 lines.
- **Acceptance: not established by the digest.** That this posted text is the one the 2026-11-02 reviewer accepted is
  a historical assertion. It rests on two things:
  - the gate record c.6567502036, posted by the coordinating session that also posted the text and the review;
  - the concordance in `SOURCES.md` §2–§3, which checks the posted text against the review record, #1031 comment
    6567537517, and against the decision records.

  The reviewer's own record names a path and a line count, not a digest. Its body line 7 reads "**Under review.**
  `f2/k1rdy/PREREG.md` (275 lines)." Its line 178 reads "## Confirmation (owner decisions; r3 → current, 313 lines)".
  The earlier revisions r1 and r2 are not retained, so the Confirmation's "no other line changed" cannot be checked line
  by line (`SOURCES.md` §6, A-2). K1-RDY-1's §12 (line 319) calls lines 1–313 the text "accepted on 2026-11-02". That
  acceptance has this support and no other.
- **Accountable Issue (§A.46 item 4).** #1031 is the accountable Issue for §12's "accepted on 2026-11-02". Its status
  is this record: no further check is possible unless r1 or r2 is found, and §12 is frozen, so its wording changes only
  through a new native round.

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
- **Review.**
  - PR #1114 comment 6649791225 reviewed `SOURCES.md` at `794ebeb5`: ACCEPT WITH CHANGES. Its required revisions to
    `SOURCES.md` were applied at `e18b36e3`.
  - PR #1150 comment 6665794090 reviewed this directory at `df86968c`: ACCEPT WITH CHANGES. It confirmed the blob
    identity above.
  - Both reviews are model-authored.
- **Open items** of `SOURCES.md` §4–§7, placed as in #1031 comment 6665340769 §2:
  - In K1-RDY-1's amendments:
    - A-1 and PF-1 in A2;
    - PF-2 in A3;
    - P-1 and P-2 in A4;
    - P-3 in A5–A7;
    - P-5 in A6;
    - C-2 and C-3 in A1 and §12.
  - G point 1 in the O-3 ruling quoted in §12.
  - G point 2, F8, F9(a) and F9(e): not applied, and frozen at `F`.
  - C-1: resolved on #1031 (comment 6649659723).
  - A-2: in this README.
  - A-3: in `SOURCES.md` only; no claim uses it.
  - F9(c) and F9(f): not placed there. `SOURCES.md` ties them to A-1 and P-2, so they follow A2 and A4.
  - §5 P-4, the RR-1 carry-forward mapping: #1031 comment 6665594544, which supersedes P-4 where they differ. K1-RDY-1
    did not discharge those findings.

## Limits

Quoted from the #1114 branch's `README.md` at `66bee341`:

> - The digest identifies the text the coordinator posted and hashed on 2026-11-02 (#1031 c.6567502036). That the
>   posted text is the one the reviewer accepted rests on that record and on the concordance in `SOURCES.md`. The
>   reviewer's own record names the file and its line count (313), not its digest.
> - Earlier revisions of the preregistration (r1, 275 lines; r2, 312 lines) are not retained anywhere found.

## References to content not on `main` (§A.42 item 8)

**This README's references:**

| Reference | Claim | Class |
|---|---|---|
| #1031 comment 6567522034 | the posted text equals lines 1–313 on `main` | Support off `main`. The bytes compared are on `main`, but the comparison needs the comment: the API recipe above re-checks it while the comment exists, and the reviews report its result. From `main` alone, only the 313 lines' digest is established. The comment's header and recorded prefix are quoted above |
| #1031 comment 6567502036 | the historical acceptance; the recorded prefix | Provenance for an assertion this record does not establish. The table row cited is quoted above |
| #1031 comment 6567537517 | the reviewer named a path and line count | Support off `main`; lines 7 and 178 are quoted above |
| PR #1114 branch at `66bee341`; commits `794ebeb5` and `e18b36e3` | source of `SOURCES.md` and of the quoted lines | Provenance. The copied bytes are in this directory, and the branch is kept |
| PR #1114 comment 6649791225; PR #1150 comment 6665794090 | the "Review" statements above | Support off `main` for those statements only |
| #1031 comments 6665340769, 6649659723 and 6665594544 | the "Open items" placement | Support off `main` for the placement. The amendments named are on `main` |

**`SOURCES.md`'s references.** Every claim of `SOURCES.md` that rests on one of the references below is not established
from `main`. This covers its concordance (§2–§3), its attribution findings (§3.2, §3.4, C-2, C-3), its search results
and its open points.

| Reference in `SOURCES.md` | What `SOURCES.md` uses it for | Class |
|---|---|---|
| #1031 comment 6567522034 | the recovered text (§1) | as in the first table |
| #1031 comment 6567502036 | gate record G: §2, §3, C-2 | support off `main` |
| #1031 comment 6567537517 | review record R: §1–§3, A-2 | support off `main` |
| #1031 body | row I of §3.4 | support off `main` |
| #1031 comment 6567152798 | the P3 diagnostic (P-5) | support off `main` |
| #1031 comment 6625842789 | the RR-1 requirement (P-4) | support off `main` |
| #1031 comment 6649454594 | the activation finding (C-1) | support off `main` |
| #1031 comment 6649482038 | the authorization (header) | provenance |
| #914 comment 6566997020 | K-1 to K-18 and D-07(a): §3.4, C-3 | support off `main` |
| #914 comment 6563412926 | D-19 row of §3.4 | support off `main` |
| #914 comments 6564008455 and 6564018307 | proposal r3 and its review: digests (§1), A-3 | support off `main` |
| #914 comment 6567198108 | P-5 | support off `main` |
| #1025 comment 6559037887; `stage1/REVIEW.md` at `e02544d5` | the RR-1 findings (P-4) | support off `main` |
| PR #1114 comment 6649791225 | the A-1 ruling, PF-1, PF-2, and the additions to P-3 and P-5 | support off `main` |
| `e02544d5` (RR-1's preregistration) | anchor `RR:N` (P-3) | support off `main` |
| `d4a80fc8`, `0efd67a6`, `fa32b043`, `44236326` | held heads (P-2) | support off `main` |
| TA, TD, MAP, P2 | working records the text cites (P-3) | not found on any branch; not established |
| `f2/k1rdy/PREREG.md`, r1 and r2 | the reviewed file and its earlier revisions (§1, §2, A-2) | not retained; not established |

`SOURCES.md`'s other commit references (`07d94f2c`, `02009693`, `af1e9be2`, `947761dd`, `ff4d4beb` and `29ec36be`) are
reachable from `main`.
