# LOG — research/bridge

Dated entries (UTC, from `date -u`), newest last. Every commit on this branch is recorded here with its purpose.

- 2026-10-10T19:56Z — thread branch created from checkpoint 4dc0321c (= L 9f9f8257 + research/archive); charter in README.md.
- 2026-10-10T20:15Z — reading complete, in the charter's order: INTEGRATION-NOTE-STAGE6 (§0, §3, §5; read in full);
  T6/TEST.md (in full); R6/REASSESSMENT.md (§1–§2, §4–§9); INTEGRATION-NOTE-STAGE5; drive/RESULT.md; opact/RESULT.md;
  kernel EmbeddedObservation, OIRealization, CompositeInterface (§A–§B and the declaration list), K2Guard,
  CompositeDimension (§A–§B, §K), KInfFoundations (§A, §C, §C′); Main.md:536–566 and §3.3 (:354–407); GR.md:220–236,
  :322–330; SM.md:791 context. Also D5/RESULT.md §0–§1.7, C5 finite-group verdicts and Z/RESULT.md claim D (for B2/B3).
  Inbox empty: no handoff received.
- 2026-10-10T20:16Z — decision: B1 is designed as a dichotomy, not as a single derivation. Locality of registers
  (L-REG) is tested both as a source of (b_H) and against the framework's Bell ceiling (Main.md:360–371), since
  `phiW` (CD:1220–1222) lies in every candidate cone. Decision rule written into `b1_hidden.py` before its first run.
- 2026-10-10T20:17Z — `b1_hidden.py` run 1: 17/17 PASS, VERDICT B1-HIDDEN-EXACT. Replay byte-identical (cmp on out
  and err). No failed runs.
- 2026-10-10T20:20Z — commit B1 (16806264, 20:20:08Z): NOTES-B1.md, b1_hidden.{py,out,err,replay.*}, RESULTS rows B1-1 to B1-4.
- 2026-10-10T20:21Z — decision: B2 transcribes each principle with the pair family as independent data (never as
  tensor products of token families), and certifies `Aut(K(Z_F))` membership by permutation of `Z_F` + ipW-orthogonality
  + explicit unitary implementation; non-membership only through `K ⊆ K*`. Decision rule written before the first run.
- 2026-10-10T20:24Z — `b2_transcriptions.py` pre-run edits (C2 wording; simplify → expand). Run 1: 18/18 PASS. Record
  defect: the header misstated the pre-run-edit time as 20:31Z (actual ≈ 20:24Z). Run 1 kept as `.run1.*`; the comment
  was corrected and the script re-run (output byte-identical to run 1), then replayed byte-identically.
- 2026-10-10T20:27Z — commit B2 (8b3b41b9, 20:26:43Z): NOTES-B2.md, b2 script/outputs/replay/run1, RESULTS rows B2-1 to B2-5. Verdict:
  CONFIRMING stage 5 (no principle at L excludes K(Z_F) through a clause that passes the disguise test).
- 2026-10-10T20:29Z — decision: B3 recast after reading stage 4's R1 record (INTEGRATION-NOTE-STAGE4.md:42): a single
  finite-order rotation suffices, so the dividing line tested is finite / locally finite realized pair groups with
  `cnot`, not finite / continuous order.
- 2026-10-10T20:32:58Z — `b3_finite.py` run 1: 11/11 PASS. Record defect (second occurrence): the header stated the
  rule as fixed at 20:44Z, a time later than the run; actual ≈ 20:31Z. Run 1 kept as `.run1.*`; the header was
  corrected (rule text unchanged), re-run (output identical to run 1) and replayed byte-identically. From here on the
  header time is taken from `date -u` immediately before writing.
- 2026-10-10T20:37Z — commit B3: NOTES-B3.md, b3 script/outputs/replay/run1, RESULTS rows B3-1 to B3-6; label fix of
  B2-1/B2-2 to the charter's label set (FAILED as routes); LOG times of the B1/B2 commits made exact.
- 2026-10-10T20:37Z — decision: B4 built as the framework's own reversible gluing machinery in branch (a) (two wing
  registers carrying the joint table); the obstruction probe uses only valid K(Z_F) instruments (a joint measurement
  {y, E00 − y} certified in K = K*), not local quarter-turns (which are not K(Z_F) symmetries and would misattribute
  the negativity). Decision rule written at 20:37Z (date -u taken before writing).
- 2026-10-10T20:39:55Z — `b4_realization.py`: pre-run edit at 20:39Z (R8 closure iterated to a fixed point; a guessed
  time "20:42Z" was written first and corrected to the `date -u` value before the run). Run 1: 13/13 PASS, VERDICT
  B4-REALIZATION-EXACT; replay byte-identical (20:40:41Z).
- 2026-10-10T20:44Z — B4 pressure test: preparation reachability examined as a candidate bridge (NOTES-B4 §4(d));
  recorded as FAILED (self-defeating at the finite level; T/H family at the completed level). B5 written as a synthesis
  (no new computation). Lean formalization of Theorem B1.1 not attempted (time budget; recorded as OPEN, B5-2).
- 2026-10-10T20:45Z — Lean formalization of Theorem B1.1 (B5-2) not attempted. Reasons: the Actions queue is backed up
  (other threads' dispatches queued since 20:27Z), and a new OIBridge module needs a census-registry disposition
  (§A.35) outside the module path this thread may write. B5-2 recorded as OPEN; no dispatch used (0 of 3).
- 2026-10-10T20:46Z — scope of B4 narrowed in NOTES-B4/NOTES-B5: "every constraint listed in §1" (realization theorem +
  branch (a)), not "every H-level constraint"; C1–C4 and the SM/GR spatial-graph constraints stated as not imposed.
  RESULTS V-1 (standing verdict) added. Handoff proposals HP-1, HP-2, HP-3 written.
- 2026-10-10T20:46Z — commit B4/B5 prepared (exact commit time recorded in the next entry): NOTES-B4.md, NOTES-B5.md, b4 script/outputs/replay, RESULTS rows B4-1..B5-3 and
  V-1, handoff-proposals/HP-1..HP-3.
