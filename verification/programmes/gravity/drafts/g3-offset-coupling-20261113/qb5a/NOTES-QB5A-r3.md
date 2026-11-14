# NOTES-QB5A-r3: working log for the G3 QB5(a) preregistration, revision 3

## 1. Pins and commit state

- **Source snapshot.** `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153`.
- **Branch.** `research/g3-offset-873-20261113`, in a read-only worktree. Head at reading time:
  `c006bf2a3`.
  - `c2b754afa` adds r2, NOTES-QB5A-r2 and RESPONSE-QB5A-r1. The committed r2 is byte-identical to the
    writer's r2 (`git show c2b754af:…/qb5a/G3-QB5A-PREREG-r2.md | cmp`).
  - `c006bf2a3` adds `qb5a/REVIEW-QB5A-PREREG-r2.md`. The copy the coordinator supplied is the one read.
- **Commit state, as observed when this file was written.**
  - r1 is committed at `2e18a2df`, and r2 at `c2b754af`.
  - r3, NOTES-QB5A-r3 and RESPONSE-QB5A-r2 are not committed.
  - The writer does not commit, push or post.

## 2. Authority and requests

- **Authorization.** #873 c.6872004336. **Owner guidance:** #873 c.6872277416. Both are as in r2.
- **The coordinator's request for r3** is a session message, not an owner record. It asks for:
  - the review's replacement text, applied verbatim;
  - nothing changed beyond the findings;
  - the OQ answers kept marked as pending;
  - RESPONSE to quote each replacement and give its r3 line;
  - r2 left unchanged.
- **The owner's qualifications** to OQ-2 and OQ-7 are taken from REVIEW-QB5A-PREREG-r2 §5, as relayed
  there:
  - OQ-2: "Δ9 must not become a route to a favourable exception after the result is seen".
  - OQ-7: "hedged statements, conditional derivations and imported assumptions keep their distinct
    statuses; plain claims are never treated as no claim".

  The writer has not seen these qualifications on #873. Their record status is for the coordinator to
  confirm when the owner's answers are recorded.

## 3. Sources read for r3

- `REVIEW-QB5A-PREREG-r2.md`, in full (520 lines).
- The writer's r2, to locate each replacement point.
- No corpus passage was opened for r3. No inventory passage was classified.

## 4. Decisions

| # | Decision | Reason |
|---|---|---|
| D-21 | The replacement text is applied verbatim through scripted exact-string replacements. Each replacement was asserted to match exactly once | It guarantees that the review's text lands unaltered and that no other passage is touched |
| D-22 | "Q-6a" is replaced by "Q-1b" in two places R2-3 does not list: the §7.2 Δ9.k row and the §14.2 deviation bullet | They name the removed node. Leaving them would point to a node that no longer exists |
| D-23 | I-BLIND item 1's "before any GRT verdict" is changed to "before any row is classified" | This is consistent with R2-3's X-19 text. Otherwise the two would state different deadlines |
| D-24 | OQ-4's applied answer lists R2-10's additions | It keeps §15 consistent with §4.2 |
| D-25 | GR:416 moves from the excluded list of NOTES-QB5A-r2 §5 to Group C (C-GR416), and GR:26, :549, :703 and :705 move to Group P | This follows R2-10. NOTES-QB5A-r2 §5's exclusions for these hits are superseded |
| D-26 | K-GR346 stays one row. Its s.4 is recorded as "on §2.2's list and is not a row" | R2-9 names K-GR340, K-GR342 and K-Sub385 to K-Sub389 only. GR:346 was already split by sentence. Only the R2-14 wording is applied to it |

## 5. Commands run

All were read-only, apart from writing the three new files.

- `ls -la` and `wc -l` on the folder holding the review.
- `git show c2b754af:<path> | cmp` of the committed r2 against the writer's r2: identical.
- `git log --oneline -3` in the worktree.
- `sed -n` and `grep -n` on r2 and r3, to locate text.
- A Python script that applies exact-string replacements to a copy of r2 and asserts that each matches
  once. It computes nothing on OI rules.
- `diff` of r2 against r3: 42 hunks.
- `grep` for the barred path strings: no hits.

## 6. Off-`main` references (§A.42 item 8)

The references of NOTES-QB5A-r2 §8 carry over. The following are added.

| Reference | Claim it is attached to | Class |
|---|---|---|
| `qb5a/G3-QB5A-PREREG-r2.md` at `c2b754af` (branch) | the base of r3 | support off `main`; lands with #1275 |
| `qb5a/REVIEW-QB5A-PREREG-r2.md` at `c006bf2a` (branch) | R2-1 to R2-15, their replacement texts, and the relayed owner qualifications | support off `main`; lands with #1275 |
