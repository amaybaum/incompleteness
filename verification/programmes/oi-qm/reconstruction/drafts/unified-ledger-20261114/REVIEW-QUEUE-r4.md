ACCEPT

# Focused confirmation review of QUEUE-PROPOSAL-r4

This review is read-only and paper-only. `QUEUE-PROPOSAL-r4.md` and `RESPONSE-QUEUE-r3.md` were
confirmed byte-identical to their copies on PR #1292 at `5e14a0b2`. `diff QUEUE-PROPOSAL-r3.md
QUEUE-PROPOSAL-r4.md` was read in full. The #1244 claims were checked on `main` (`dfeec843`) and through
the GitHub API. No other file was written, no computation was run, and nothing was posted.

## The coordinator's five checks

**1. #1244: confirmed.**
- **The merges.**
  - #1261 merged at 2026-11-12T18:40:51Z as `0ebf90db`.
  - #1262 merged at 2026-11-12T19:18:05Z as `fba459cb`.
  - Both are on `main`.
- **F-17 at :179.**
  - #1261's body reads "A/4 is removed from the 'distinguishes OI' row. The row keeps Cabibbo, Koide and
    the dark-sector phenomenology."
  - Structure:179 at `dfeec843` still places the dark-sector phenomenology at G3 × D, against :191–192.
  - A new unit is correctly proposed.
- **G-2.**
  - GR:12 at `dfeec843` still reads "the counting … itself unconditional".
  - Its last change is `9845c131`, from before #1262. #1262 did not touch it.
  - Commit `64aeb44c` states "Unconditional counting statements are unchanged (no class-(b) sites)".
  - G-2 is now only owner question 4, with no unit unless the owner revisits the rule. That is correct.
- **T-4.**
  - `git blame` puts Structure:453 at `6cf861e0`, "A/4 conditions point to GR §8.5(b) at the three #1253
    sites (#1244)".
  - #1253 merged at 2026-11-12T15:19:31Z as `609bd663`, which is on `main`.
  - Only the "any horizon entropy" bound remains, and r4 proposes a unit for that part alone.
- **The stale #1244 note.** It is recorded as a sourced fact for the owner.
- **§1.6's sentence about the authorized draft.** It is removed.

**2. RO-2: confirmed.** r2's wording is restored: "its verdict may be the residual class (C)".
`RESPONSE-QUEUE-r3.md` discloses the r3 change as "substantive and unintended".

**3. RO-3: confirmed.**
- **The §3.1 table.** It now reads "readiness undetermined (no row records the inventory's readiness)".
- **"What the evidence shows".** The sentence borrowing #1055's readiness is replaced by "#1055's
  readiness is for its recorded question; no row records the readiness of the inventory".
- **RO-3's recorded planning.** It qualifies #1055's "ready" the same way.
- **The ranking reason.** "Its scope is not frozen" is kept.

**4. Partial fits: confirmed.**
- S-17 joins MC-3 Substratum and K-5 joins MC-3 book, both in #1028.
- S-1 and S-2 stay on #1238. The row marks them as a partial fit, with the GR half named and the scope
  widening proposed.
- #1062 is kept for U-2, with the partial-fit caveat at the RO-9 row, in A.4 and in owner question 16.
- The REVIEW-QUEUE-r3 nits are also applied:
  - N1: D1 "under CON-04, a different defect";
  - N3: the clause splits are stated in A.0.

**5. Nothing else changed: confirmed.** The diff is limited to:
- the header and inputs (the #1244 vehicles);
- A.0, A.1, the RO-9 row, the #1028 MC-1, MC-3 Substratum and MC-3 book rows, the #1238 and #1244
  blocks, and A.4;
- §1.6, the RO-2 and RO-3 sentences and the §3.1 table;
- owner questions 2, 3, 4 and 16;
- the off-`main` table.

Nothing else is affected:
- The three kinds of work stay separate.
- No tier, readiness, authorization or manuscript wording changes.
- RO-1 and RO-2 keep "no default order".
- Readiness is nowhere presented as authorization.
