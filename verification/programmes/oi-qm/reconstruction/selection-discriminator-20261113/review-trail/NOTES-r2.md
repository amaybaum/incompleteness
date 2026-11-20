# NOTES (r2): #1169 synthesis, writer's working notes (not a record)

These notes accompany `SYNTHESIS-r2.md`. r2 answers `REVIEW-r1.md` (findings F1–F21); the
dispositions and the r1→r2 delta table are in `RESPONSE-r1.md`.

## Method and limits

- Paper-only. No computation on any OI rule, no probe, no Lean build.
- The only tools run were the three cheap checks (`voice_check.py`, `claims_check.py`,
  `staleness_check.py`), on a copy of the synthesis placed under a temporary `papers/` root. All
  three returned OK. Staleness reports the copy as unstamped, which is expected. They scan
  manuscripts only, so a manual scan of the added lines for the §A.32/§A.33 phrase families was
  also done.
- Git operations:
  - `git fetch origin <branch>` by name, with no `--depth`: the four unit branches (r1); the #1268
    branch again and `research/synthesis-1169-20261113` (r2);
  - `git ls-remote` (each head is recorded in §0 of the synthesis; #1268 moved to `2a9f10ba`);
  - `git show <sha>:<path>`, `git rev-parse`, `git log`, `git ls-tree`, `git diff`, `cmp`.
- r2 checks: the committed `SYNTHESIS-r1.md`, `NOTES-r1.md` and `REVIEW-r1.md` at `71253fd4` are
  byte-identical to the working copies; `REC-1-r7.md` and `REC-1-P0-r3.md` have the same blobs at
  `cd38655c` and `2a9f10ba`; the r7→r8 diff touches only r8's header and the three passages.
- Other reads: `sed` and `grep` on the `main` worktree at `c3b5f37a`, and `curl` reads of the
  GitHub API (r1 list unchanged).
- `python3` was used only to print JSON fields and for literal text substitutions in the drafts.
- The checkout was not edited. Nothing was committed, pushed or posted.

## Reading inventory

**r1 reading** (unchanged): TS r2, CONFIRM-r2 and NOTES-r2; P0 r3 and CONFIRM-r3; REC-1 r7;
BELL-LADDER r3, NOTES-r3 and CONFIRM-r3; OC `NEW-RESULTS.md` and `DEPENDENCIES.md`; OA-1, OA-2,
OA-3, W1-1, OBS, MECH-1, MECH-2, PPS and minacc-1 at the cited lines; the cited Main lines; the OB
theorem headers.

**Added for r2.**
- `REVIEW-r1.md` in full.
- The r7→r8 diff and the head of `REC-1-REVIEW-r8.md` at `2a9f10ba`.
- OA-1 r5 :149–150, :196–200, :526–529, :565–574; OA-2 r4 :370–374, :528–537, :552–560, :587–613;
  OA-3 r4 :132–136, :296–310, :349–352.
- S4 :464–474 (NL-C′, with `ε < 1/8`, `K ≥ L + 1`, `O ⊇ C`); P :143, :184–199 (fixed `r_O`;
  program blocks are translates of `C` outside `O`). r1 cited these through TS without re-reading.
- OB: `obsTheory_nonnegBounded` (FrozenSourcing.lean:84), `nonnegBounded_not_derivedOI` (:111),
  `DenseUnitaryControl` (DiscreteCompletion.lean:45, a `Fin 2` definition), `obsTheory`
  (SubstratumInterfaceAudit.lean:770–771), by header.

**Not read directly** (unchanged): BS, SB, QH, 3A, OICORE-1 and APPROX; TUNE-1 S3; the
independent REVIEW-r1 files of TS, P0 and BL; OC's provenance, changes and review files; #914,
#1143 and #866 beyond the quotations in TS.

## Ranking decisions and alternatives considered

1. **The metric was fixed from F12's definition before the counts were made.**
   - "Blocks" means a premise of a construction target. The eight targets T1–T8 are the ones the
     units name.
   - The lexicographic order puts strength of support first: shown necessary on its own, then one
     member of a disjunction, then load-bearing role shown. A disjunct can be bypassed by another
     member, and a load-bearing input is not shown to block.
   - Under this metric MM-3 ranks first. r1's order (MM-1 first) is recovered when MM-3's sub-rows
     are counted separately. MM-2 ranks first when any role counts once. All three are stated in §3,
     and the choice is SQ8.
2. **Why MM-1 no longer ranks first under the primary metric.** F1 and F2 narrowed it: (1b) is an
   absence result and (1c) a disjunction, so MM-1 is shown necessary on its own for T1 (1b′, R-lin
   and μ-G) and T4 (1a, TUNE-1's schema) only.
3. **MM-2 is a proposed route with load-bearing role shown** (F9). It ranks sixth because no target
   is shown to fail without a particular derivation of it; it is a disjunct for T1, T2 and T4.
4. **MM-4 below MM-3 and MM-1.** It is shown necessary on its own for one target (T3) under every
   measure; it unblocks no MM-3 route by itself (F8).
5. **MM-6 is a proposed route, not shown necessary, and is listed last.** What the units show is
   that measurement independence is a hypothesis of E(b), OBL-SP and the Bell stage-5 ceiling, not
   of AL or Theorem S (F3). It blocks no construction.
6. **MM-8's "shown necessary" is relative to the unrestricted class**, and follows from the
   definition of a selector plus Main:360 and :427. The entry now says so (F19).
7. **W1 is unranked.** It belongs to the GR calibration track (#1245), and REC-1 row 30 records no
   bearing on Q3 or Q4.

## Readings made in the synthesis (each "[A, here]" or cross-unit, unreviewed)

- **R-a (MM-6).** Under μ-G, disjoint setting cells satisfy (xiv) (OA2:750) but are not selected;
  under `D_0`, selection is supplied and independence is a posit clause. BORDERLINE: it restates
  two on-`main` facts side by side.
- **R-b (T4).** OA-1 D1, together with the scope quoted at TS:306–308, would exclude an
  unconditioned producer under every invariant law. ELABORATING, conditional on SQ2. The review
  checked that T4 reads TS and OA-1 D1 correctly.
- **R-c (A4), narrowed in r2 (F5).** P0's scoped pass, AL and E(b) each carry a record-access clause
  ((LF), (AL4), (H4)), and dropping it leaves the case open; each also has other open exits
  (non-additive observers and non-spanning laws for E(b); non-coset laws, non-cell settings and
  postselection for AL). r1's "in each, the open case is a restricted record region" was wrong.
  No formal map between the three clauses is claimed. ELABORATING.
- **R-d (T3).** The planning edge O-RDY → O-RET, against OA-1 D4(c), gives a cycle under μ-G.
  CONFIRMING; a planning observation only.

No NEW finding. Fixed point (§A.31): two passes (writer r1, review), the second yielding no NEW
finding but five scope corrections. A third pass, the focused confirmation, should check the §3
counts against the entries.

## Open points for the confirmation

1. **§3 count table.** Check each cell against its entry, in particular MM-2's disjunct for T1
   (OA1:522: gap 1 "resolved classically by MP-0a or MP-0b") and MM-3's T4 cell (3b(iii), NL-C′).
2. **MM-4d.** New in r2 (from F8): MM-4 as one disjunct of a G3 escape within Corollary E1's
   scope. Check against OA2:587–604 and OA2:596–599 (E1 does not make the gap-2 repair necessary
   for gap 3 outright).
3. **§8.** Every reference now has its own row. Check that no row classifies a reference that the
   text uses as "provenance".
4. **Names.** "SQ1–SQ9" replace r1's "Q1–Q8" for this record's own questions.

## Not done

- No new derivation beyond the readings above.
- No search for prior art beyond the units' own §A.19 inventories.
