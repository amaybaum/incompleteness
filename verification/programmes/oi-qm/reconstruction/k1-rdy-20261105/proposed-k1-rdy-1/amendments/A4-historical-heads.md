# A4. Holds and referenced historical heads

**Governs:** base line 229, its first sentence ("The holds on #1009, #1023, #1011, #1003 and #918 are unchanged."), and
base line 263, the row "Held heads unchanged".

**Line 229.** The formal holds on #1009, #1023, #1011, #1003 and #918 are retired as a scheduling mechanism by
`AGENTS.md` §A.45 rule 7 (owner, 2026-11-03); every other requirement in those hold statements remains in force as last
recorded by the owner. Lines 226–228 stand: §A.45 rule 7 states that "Separate restrictions, including #914 decision 7's
readiness-dependent condition, are unaffected." The rest of line 229 stands.

**Line 263.** The row reads:

| Invariant | Checkpoint |
|---|---|
| Referenced historical heads recorded | `gh api` GET of pulls 1009, 1023, 1011, 1003, 918 and 1025 at the start and end of execution, each compared with the head listed below. A mismatch is recorded in `result.md` and is not classified as VOID[stage]. If it alters an actual scientific dependency or a frozen input, the affected work stops and is reconciled before proceeding. No silent substitution |

Heads read on 2026-11-05 (`git ls-remote`, `refs/pull/<n>/head`): 1009 `d4a80fc8`, 1023 `af1e9be2`, 1011 `947761dd`,
1003 `0efd67a6`, 918 `44236326`, 1025 `e02544d5`. #918's head moved from the drafting value `fa32b043` (line 263) to
`44236326`, a descendant of it. Every anchor of this round is read at its pinned commit (lines 10–12, A7), never at a
pull request's head, so a moved head changes no input of the round.

**Source.** Owner, #1031 comment 6651204512 (amaybaum, 2026-11-05T06:15:48Z), quoted in §12: "A4: option (a), with a
material-change safeguard."
