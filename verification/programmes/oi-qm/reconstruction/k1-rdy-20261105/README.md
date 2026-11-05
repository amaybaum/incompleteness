# K1-RDY preregistration: recovered accepted text (#1031)

**Status: WIP / UNVERIFIED. Not frozen, not an `F` candidate, not reviewed in this form.** This directory
authorizes nothing. It changes no scientific status, no readiness result, no correctness band and no hold.

## Scope and authorization

- **Planning home:** #1031.
- **Authorization:** the owner's option (b), recorded in #1031 c.6649482038 (amaybaum, Claude Code session chat,
  2026-11-05): a paper-only reconstruction of the accepted K1-RDY preregistration, followed by a full independent
  review of the text at an exact commit. Designated writer `writer-k1rdy`; branch
  `research/k1-rdy-reconstruction-20261105`, from `main` `f5c281ae`.
- **Not authorized:** freeze or designation, computation (including the review's hand checks HC-A to HC-D), Lean,
  workflow dispatch, merge, promotion of any readiness result, new physical premises.

## What this directory holds

The activation finding, #1031 c.6649454594, recorded that the accepted text was on none of the repository's branches.
That finding is correct for branches. The text is, however, posted verbatim on #1031 itself:

- **c.6567522034**, "K1-RDY record, 1 of 2: decision-complete preregistration (verbatim; sha256 prefix
  `a93f3f33f0c5a6e8`)";
- **c.6567537517**, "K1-RDY record, 2 of 2", the independent review whose Confirmation accepts the 313-line text.

The work is therefore a **recovery**, not a reconstruction. No reconstructed text is offered beside the recovered one,
because a second text could differ from the accepted one only by reinterpretation.

| File | Content |
|---|---|
| `PREREG-RECOVERED.md` | The 313-line preregistration body of c.6567522034, byte for byte, with no header added, so that its digest can be checked against the recorded one |
| `SOURCES.md` | Provenance and the digest recipe; a concordance of the recovered text against every finding, fix and decision in the review record and #914's decisions; items left open before freeze; points for the independent review |
| `README.md` | This file |

## Limits

- The digest identifies the text the coordinator posted and hashed on 2026-11-02 (#1031 c.6567502036). That the
  posted text is the one the reviewer accepted rests on that record and on the concordance in `SOURCES.md`. The
  reviewer's own record names the file and its line count (313), not its digest.
- Earlier revisions of the preregistration (r1, 275 lines; r2, 312 lines) are not retained anywhere found.
- The recovered text cites working records (TA, TD, MAP, P2 and others) that are on no branch, and anchors off
  `main` (`e02544d5`). `SOURCES.md` lists them for the review under `AGENTS.md` §A.42 item 8. Nothing here closes
  those gaps.
- Freeze needs the independent review of this exact commit and a separate owner designation (K-11; #1031 gate 2).
  Execution needs a further owner authorization (#1031 gate 3).
