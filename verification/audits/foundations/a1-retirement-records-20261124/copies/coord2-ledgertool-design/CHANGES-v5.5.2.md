# DESIGN-v5.5.2: changes against DESIGN-v5.5.1

## Input and scope

The input is `DESIGN-v5.5.1.md`, sha256 8befd35c74b8e4dfa241e360d891de3222b3f878ca2aaf23ceaae1d00fbed649,
verified before use.

By owner decision of 2026-11-23, v5.5.1 is accepted, and N3 is the only substantive change; the
design is then frozen. The work was paper-only: no repository, git or GitHub write, no workflow
run and no host call.

## Changes

| Hunk (v5.5.1 lines) | Section | What changed | Item |
|---|---|---|---|
| 1 | title | "design v5.5.2" | title |
| after 9 | status | Two new bullets: v5.5.2 as the frozen design, adding only N3 to the accepted v5.5.1; and the owner's final decisions D1-D4 of 2026-11-23 | status lines |
| after 1331 | 6.3, "The freeze ledger" | See "N3" below | N3 |
| 776 | 5, durable evidence | The bullet now says that observed events are appended to the freeze ledger only with the append's own owner approval comment. This is a consequence of N3 | N3 |
| after 2176 | 10.4 | New refusal control TR47, see below | N3 |
| 2963 | 16.8, S13 control list | "TR1-TR46" becomes "TR1-TR47" | N3 (consequence) |

**N3.** A new bullet, "Approval of each acceptance-time append (N3)", sets these requirements:

- Every append to the freeze ledger, including an acceptance landing's append, needs its own
  explicit owner approval comment. The comment must:
  - be in the plan's authorized thread;
  - use the versioned first line
    `oi-freeze-ledger/1 append plan=<plan_id> round=<round_id> from=<ledger sha256 before> to=<ledger sha256 after>`;
  - be authored by numeric owner id 7273571;
  - be created before the merge.
- The comment is verified exactly like a designation: the thread read completely, the immutable
  id, author numeric id, creation time and edit status checked, never edited, no edit history,
  not hidden.
- A malformed `oi-freeze-ledger/` line, or one with an unknown version, refuses.
- Without a valid comment the append is refused and the landing does not merge. A ledger carrying
  an unapproved append is unverifiable, so later admissions refuse (TR36).

**TR47** covers each refusal separately:

- no approval comment;
- wrong ledger hashes;
- another numeric id, even with the owner's login;
- an edited or hidden comment;
- a comment outside the plan's thread;
- a comment created after the merge;
- a malformed or unknown-version line.

## Verification

`diff DESIGN-v5.5.1.md DESIGN-v5.5.2.md` has 6 hunks, all listed above, and the document grows from
2963 to 2998 lines. No other text changed. This is textual verification; no implementation exists.

## Not followed or not verified

- **Scope.** Besides the N3 bullet itself, I touched the sec. 5 evidence bullet and the S13 control
  list, so that the frozen text does not contradict N3 or omit its control. Both edits follow
  directly from N3.
- **Host semantics.** They are not exercised, as before.
- **Comment ids.** The owner's decisions are recorded without comment ids, which this writer does
  not hold.
