# DESIGN-v5.5.3: changes against DESIGN-v5.5.2

## Input and scope

The input is `DESIGN-v5.5.2.md`, sha256 835ff356200349db7689ea41ce936349015fb70f47b35a508945d681a8604323.
I verified the hash before use and did not modify the file.

The owner decided on 2026-11-23 to reopen the frozen design narrowly, for K7 only. K1 is not
touched, and nothing else changes besides the title and status lines.

The work was paper-only: nothing was written to the repository, git or GitHub, no workflow ran, and
no host was called.

## Changes

`diff DESIGN-v5.5.2.md DESIGN-v5.5.3.md` has 5 hunks, and the document grows from 2998 to 3027
lines.

| Hunk (v5.5.2 lines) | Section | What changed | Item |
|---|---|---|---|
| 1 | title | "design v5.5.3" | title |
| after 9 | status | A new bullet records the owner decision: v5.5.2 is reopened for K7 only, with the content of the allowance and the statement that no safeguard is weakened | status line |
| 1297-1298 | 6.3, trust root point 3 (execution identity) | See "The rule" below | K7 |
| after 2211 (after TR47) | 10.4 | Controls TR48-TR53, see "Controls" below | K7 |
| 2998 | 16.8, S13 control list | "TR1-TR47" becomes "TR1-TR53" | K7 (consequence) |

**The rule (K7).** The sentence "with no further file under `tools/ledger_coverage/`" is replaced by
an explicit list of the permitted files. Besides the files named by `A.engine_pins`, exactly two
files are permitted, each only at its own path and only as a regular file:

- **the authority record** at `tools/ledger_coverage/authority.json`. Its blob sha256 must equal that
  of the `A` admitted for the run, under the authority rules already in sec. 6.3;
- **the workflow** at `A.workflow.path`, if that path lies under the directory. Its content sha256
  must equal `A.workflow.content_sha256`.

Every other file in the directory refuses the run, including a second copy of either at another
path. A permitted path whose content differs, or that holds a symlink, submodule or other
non-regular entry, also refuses. The allowance is limited to these two independently pinned
components and relaxes no other check.

**Controls (TR48-TR53).**

- TR48 (positive): a valid tree holding the pinned files, the approved authority record and the
  approved workflow is accepted.
- TR49: a modified authority record is refused.
- TR50: a modified workflow is refused.
- TR51: a substituted file at either permitted path is refused, whether it has different content, is
  a symlink or is a submodule.
- TR52: an additional unauthorized file is refused.
- TR53: a byte-identical second copy of the authority record at another path is refused.

## Verification

Textual. The diff touches only the hunks listed above. No implementation exists, so the controls are
specified and have not been run.

## What I could not follow or verify

- **One added detail.** For the authority record's "own verification rules", the design now states
  them as blob equality with the admitted `A`. That is how the existing sec. 6.3 rules apply to a
  `main` commit. I also refuse non-regular entries (a symlink or submodule) at the permitted paths,
  reading "substituted" in the strict direction. The owner may want to confirm both points.
- **Comment ids.** The owner decision is recorded without a comment id, which I do not hold.
