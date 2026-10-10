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
