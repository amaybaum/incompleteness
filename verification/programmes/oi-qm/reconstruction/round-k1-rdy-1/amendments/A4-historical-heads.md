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
| Referenced historical heads recorded | `gh api` GET of pulls 1009, 1023, 1011, 1003, 918 and 1025 at the start and end of execution, each compared with the head recorded at `F`. A mismatch is recorded in `result.md` and is not automatically classified as VOID[stage]. If it alters an actual scientific dependency or a frozen input, the affected work stops and is reconciled before proceeding. No silent substitution |

**Heads recorded at `F`.** Read with `git ls-remote origin refs/pull/<n>/head` at 2026-11-05T11:58:40Z, in the commit that is
intended as the last control-plane commit before `F`:

| Pull | Head |
|---|---|
| 1009 | `d4a80fc871473285a7c848a4984940d52817ff8c` |
| 1023 | `af1e9be2ceabd5f6181b8d56b537b7ce1a4a3bba` |
| 1011 | `947761dd40c17e4fdedcd8972a0b4e53e8bfba42` |
| 1003 | `0efd67a630fc80ac55fde1ca49fe8c5cbdbf10c3` |
| 918 | `44236326976d2c9ad743f52595365b64ceb86d35` |
| 1025 | `e02544d54b365b6a123ee284bd16442fb617c0b2` |

The independent exact-head review and the `F` `check-run` cover the commit that carries this table. If any further
control-plane commit precedes `F`, the heads are read again and entered in it. #918's head moved from the drafting value `fa32b043` (line 263) to
`44236326`, a descendant of it. Every anchor of this round is read at its pinned commit (lines 10–12, A7), never at a
pull request's head, so a moved head changes no input of the round.

**Source.** Owner, #1031 comment 6651204512 (amaybaum, 2026-11-05T06:15:48Z), quoted in §12: "A4: option (a), with a
material-change safeguard." The owner's ruling R4 (#1031 comment 6656166518, quoted in part): "R4: Fill A4's
historical-heads placeholder in the final control-plane revision before F. Require exact-head independent review and
the appropriate check run on that revision."
