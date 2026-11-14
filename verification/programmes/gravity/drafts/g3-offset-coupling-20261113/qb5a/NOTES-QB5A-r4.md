# NOTES-QB5A-r4: working log for the G3 QB5(a) preregistration, revision 4

## 1. Pins and commit state

**Source snapshot.** `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153`.

**Branch.** `research/g3-offset-873-20261113`.

- r3 is committed at `4a157f19`.
- The committed r3 is byte-identical to the writer's r3. The check was
  `git show 4a157f19:<path> | cmp` against the writer's copy.
- The edit check `CONFIRM-QB5A-PREREG-r3.md` was read from the copy the coordinator supplied. The
  coordinator reports that it is committed unchanged beside r3.

**Commit state, as observed when this file was written.**

- r4, NOTES-QB5A-r4 and RESPONSE-QB5A-r3 are not committed.
- The writer does not commit, push or post.

## 2. Authority and request

- Authorization and owner guidance are as in r3: #873 c.6872004336 and c.6872277416.
- The coordinator's request for r4 is a session message, not an owner record. It asks for:
  - CF3-1 and CF3-2, applied verbatim;
  - no change beyond them, apart from the title and the history;
  - the Q-6b/Q-6c labels and the absence of a K-GR346·s4 row left as they are;
  - the OQ answers kept marked as pending.

## 3. Sources read

- `CONFIRM-QB5A-PREREG-r3.md`, in full.
- The writer's r3, to locate each replacement point.
- No corpus passage was opened. No inventory passage was classified.

## 4. Decisions

| # | Decision | Reason |
|---|---|---|
| D-27 | The CF3 replacement text is applied by scripted exact-string replacement, each asserted to match once | The review's text lands unaltered, and nothing else is touched |
| D-28 | The Group P paragraph is re-wrapped after the replacement, with its words unchanged | The file's line width is kept |
| D-29 | The commit carrying the edit check is not named in r4's history | Its ID was not given to the writer. RESPONSE-QB5A-r3 §3 notes this for the coordinator |

## 5. Commands run

All were read-only, apart from writing the three new files.

- `cat` of the edit check.
- `git show 4a157f19:<path> | cmp` against the writer's r3.
- `sed -n` and `grep -n` on r3 and r4.
- A Python script applying exact-string replacements to a copy of r3. It computes nothing on OI rules.
- `diff` of r3 against r4: 7 hunks.
- `grep` for the barred path strings: no hits.

## 6. Off-`main` references (§A.42 item 8)

The references of NOTES-QB5A-r3 §6 carry over. The following are added.

| Reference | Claim it is attached to | Class |
|---|---|---|
| `qb5a/G3-QB5A-PREREG-r3.md` at `4a157f19` (branch) | the base of r4 | support off `main`; lands with #1275 |
| `qb5a/CONFIRM-QB5A-PREREG-r3.md` (branch) | CF3-1 and CF3-2, and their replacement texts | support off `main`; lands with #1275 |
