# NOTES (r1): #1169 synthesis, writer's working notes (not a record)

These notes accompany `SYNTHESIS-r1.md`.

## Method and limits

- Paper-only. No computation on any OI rule, no probe, no Lean build.
- The only tool run was the three cheap checks (`voice_check.py`, `claims_check.py`,
  `staleness_check.py`), on a copy of the synthesis placed under a temporary `papers/` root. All
  three returned OK. Staleness reports the copy as unstamped, which is expected.
- Git operations:
  - `git fetch origin <branch>` by name, with no `--depth`, for the four unit branches;
  - `git ls-remote` (each head equals its pinned SHA);
  - `git show <sha>:<path>`, `git rev-parse`, `git log`, `git ls-tree`, `git diff --stat`.
- Other reads: `sed` and `grep` on the `main` worktree at `c3b5f37a`, and `curl` reads of the
  GitHub API for:
  - #1169 comments (both pages; the last 25 read in full);
  - #1268, #1272, #1273 and #1274 comments and reviews;
  - the #1060 and #1147 bodies.
- `python3` was used only to print JSON fields and for one literal text substitution in the
  synthesis.
- The checkout was not edited. Nothing was committed, pushed or posted.

## Reading inventory

**Read in full at the exact heads:**
- TS r2 and its CONFIRM-r2 and NOTES-r2;
- P0 r3 and P0 CONFIRM-r3;
- REC-1 r7;
- BELL-LADDER r3, NOTES-r3 and CONFIRM-r3;
- OC `NEW-RESULTS.md` and `DEPENDENCIES.md`.

**Read on `main`, at the cited lines:**
- OA-1 r5: D1–D5, :418–421 and :515–600;
- OA-2 r4, by search and at :242–300, :577–605, :674–700, :745–795;
- OA-3 r4, by search and at :296–310, :566–585, :653–668;
- W1-1 r4: §8 and `STATUS.md`;
- OBS: :98–100, :119–121, :529–531, :890–902;
- MECH-1: :123–128, :940–946; MECH-2: :112–118, :830–836;
- PPS: :134–146; minacc-1 RESULT: :36–53;
- the cited Main lines;
- the OB theorem headers, located by `grep`.

**Not read directly:**
- BS (#1231), SB (#1232), QH (#1269), TUNE-1 Step 3A (#1267), OICORE-1 (#1214) and APPROX (#1221).
  Each is used only through a unit that cites it, and the unit's own §A.42 table governs that use.
- TUNE-1 S3, S4 and P on `main`. These are cited at the lines the units give, not re-read.
- The independent REVIEW-r1 files of TS, P0 and BL.
- OC's `PROVENANCE.md`, `CHANGES.md`, `review/REVIEW-r1.md`, `RESPONSE-r1.md` and `CONFIRM-r2.md`.
- #914, #1143 and #866 beyond the quotations in TS.

A reviewer may want to spot-check the OC review trail and the BL REVIEW-r1 witness. The synthesis
relies on BL r3's statement of that witness, not on the review file.

## Ranking decisions and alternatives considered

1. **MM-1 above MM-3.**
   - The instruction ranks by downstream blocking. MM-1 blocks every embedded protocol, classical
     ones included.
   - MM-3 is the only quantum-discriminating entry.
   - The alternative, MM-3 first, would rank by discriminating power instead. §3 item 3 states this
     second axis explicitly, so the reader can re-sort.
2. **MM-2 second.**
   - It is an interface definition, not a dynamical mechanism.
   - It is ranked high because it decides the scope of every affine-class classification, including
     the P0 outcome and AL.
   - The alternative was to place the C3 check as its own entry. It is the smallest next check of
     MM-2 instead, because C3 is a mathematical obligation, not a missing physical ingredient.
3. **MM-4 below MM-3.**
   - MM-4's necessity under every measure (D5) is the strongest shown-necessary statement in the
     list.
   - It is ranked below MM-3 because OA-1 shows the repair does not reach gap 3, so it unblocks
     classical targets only.
4. **MM-6 as a proposed route, not shown necessary.**
   - What the units show is that measurement independence is necessary *for the ceilings*, that is,
     for the obstruction, not for any mechanism.
   - Labelling it "shown necessary" would invert its role.
5. **MM-8's "shown necessary" is relative to the unrestricted class.** In that class PR is
   reachable (Main:360, :427). The label is a logical consequence of that fact plus the target;
   it carries no positive content about a selector.
6. **W1 is unranked.** It belongs to the GR calibration track (#1245), and REC-1 row 30 records
   no bearing on Q3 or Q4.

## Readings made in the synthesis (each "[A, here]" or cross-unit, unreviewed)

- **R-a (MM-6).**
  - Under μ-G, disjoint setting cells satisfy (xiv) (OA2:750) but are not selected.
  - Under `D_0`, selection is supplied and independence is a posit clause.
  - Classification: BORDERLINE; it restates two on-`main` facts side by side.
- **R-b (T4).**
  - OA-1 D1, together with the scope quoted at TS:306–308, would exclude an unconditioned producer
    under every invariant law.
  - Classification: ELABORATING, conditional on the owner question Q2. D1 is on `main`; the
    combination is new here.
- **R-c (A4).**
  - In P0, AL and E(b), the classical verdict holds when the observer has full, label-free or
    fixed-region record access, and the open case is a restricted record region.
  - Classification: ELABORATING. The units already carry the markers: AW-P0-1, and NOTES-r3:55–58
    and :76–78.
  - No formal map between (LF), (AL4) and (SP) is claimed.
- **R-d (T3).**
  - The planning edge O-RDY → O-RET, set against OA-1 D4(c), gives a cycle under μ-G.
  - Classification: CONFIRMING; a planning observation only.

No NEW finding. Fixed point (§A.31): one pass, so the 3–4-pass condition is not met. A reviewer pass
should pressure-test R-b and R-c, the two readings favourable to a clean classification.

## Open points for the reviewer

1. **TS's μ-O wording and OA-1 D1 (T4).** TS:140 and :247–251 say "conditional preparation
   through held records is open" under μ-O. OA-1 D1 is a theorem about every invariant law. Check
   that T4 does not misread either source. TS's "open" may refer to an H-PREP-type
   identification rather than a producer.
2. **AW-P0-2 (T5).** It is P0's record-only marker. The synthesis reports it as a tension with
   records on `main` and proposes only a read-only check. Check that this is not stronger than P0
   states.
3. **MM-3 row 3c.** Proposition B(ii) is used in the (⇐) direction only, so (CVX) is not needed.
   Check the direction against OA2:242–300 (§A.34).
4. **MM-4c.** AL gives a disjunction of four exits. The entry states that (vii) is one disjunct,
   not necessary on its own. Check that no other sentence reads it as necessary.
5. **MM-1a.** F-S2 is necessity within TUNE-1's schema only (ChatGPT review 5892912253: "not
   universal resource lower bounds"). Check that every place quoting the rate keeps the schema
   qualifier.
6. **The §8 table.** Every unit record is off `main`. The synthesis cannot land while those rows
   remain gaps, unless each one lands or the entry is narrowed.

## Not done

- No new derivation beyond the four readings above.
- No search for prior art beyond the units' own §A.19 inventories. The readings R-a to R-d were
  checked only against the records listed above.
