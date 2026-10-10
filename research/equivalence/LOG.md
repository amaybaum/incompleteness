# LOG — research/equivalence

Dated entries (UTC, from `date -u`), newest last. Every commit on this branch is recorded here with its purpose.

- 2026-10-10T19:56Z — thread branch created from checkpoint 4dc0321c (= L 9f9f8257 + research/archive); charter in README.md.
- 2026-10-10T20:02Z — read the charter, `verification/ROADMAP.md` at L (queue :61–75; P1 sections :665–1102; settled /
  not-prioritized / declared-input sections :1392–1463) and the charter's records: `k-infinity/K-INF-DESIGN.md`,
  `k2d/K2-LEDGER.md`, `sa/SA-LEDGER.md`, `k2c/K2C-LEDGER.md`, `kn/KN-CENSUS-RESULT.md`, `eqreview/HINF-REVIEW.md`,
  `eqreview/EQ2-SYNTHESIS.md`, `eq5/F/ASSUMPTIONS.md`, `eqreview/EQ5-SOURCE-AUDIT.md`, `opact/RESULT.md`,
  `drive/RESULT.md`, `pt/INTEGRATION-NOTE-STAGE6.md` (all), stage-3/4/5 notes (the parts defining H1–H3, (b), Y2), and
  the result notes at L of the rounds landed after the archive bases (K2-GUARD-1, K1-SHARP-TESTS-1, KTRANS-DENSE-1,
  PARITY-NOT-1, ODD-CHAR-1, RELC-SELECT-1, KT4-PREM-1, KINF-1, KINF-2), the audits `kinf-seams-audit.md` and
  `kn-elementary-carrier-census.md`, and the H-Bell control plane HB-1 (merged, never executed). Kernel anchors
  re-grepped at L.
- 2026-10-10T20:13Z — scheduling decision: the E2 Lean design work was started before the E1 ledger was written so
  that CI runs while the ledger is drafted (node order of the write-up unchanged; depth-first order on obligations
  unchanged).
- 2026-10-10T20:13Z — DEVIATION (branch name): `git push` of `dev/equivalence/kinf-seams` was rejected by origin
  ("directory file conflict": a branch named `dev` exists on origin, so no `dev/...` ref can be created). The
  disposable branch is `dev-equivalence/kinf-seams` instead (worktree `/home/user/wt-research/dev-equivalence-kinf-seams`).
- 2026-10-10T20:18Z — dispatch 1/3: run 38083220991 on `0578b13d` (design modules `EqvSeams`, `EqvSeamsControl`).
  Mathlib bridge Build failed at one declaration (`sum_mul_ehom`, `congr 1` closed the head goal; unsolved goal
  157:2); all other declarations of `EqvSeams` elaborated, §A printed `[propext, Classical.choice, Quot.sound]`;
  `EqvSeamsControl` not attempted (imports the failed module).
- 2026-10-10T20:21Z — DEVIATION (tool): `gh api …/jobs/<id>/logs` refuses the redirect to the log blob host; the job
  log was read with the GitHub MCP tool `get_job_logs` (a read of the same Actions job, no other host contacted by
  this session's tools).
- 2026-10-10T20:22Z — dispatch 2/3: run 38083519826 on `f5367a7a` (repair of `sum_mul_ehom` only).
- 2026-10-10T20:25Z — commit `04e69e04` (E1): LEDGER.md first version, RESULTS R-E1.1, LOG.
- 2026-10-10T20:27Z — `experiments/e2_copy_conj.py` run 1: VERDICT NOT RENDERED (two countercontrol expectations false:
  the swapped gate is a one-NOT gate with the target NOT; the d = 7 J/K map meets relT(NA)); kept as `.run1.*`. Checks
  C4/J3 restated, C6 added as a recorded run-1 fact; run 2: 13/13, `VERDICT TYPE-COVARIANCE-CONSISTENT`; replay identical.
- 2026-10-10T20:30Z — `experiments/e2_drive_trans.py`: 10/10, `VERDICT DRIVE-SEED-GEOM-CAP2-NOT-TRANS`; replay identical.
- 2026-10-10T20:31Z — run 38083519826 (dispatch 2/3) on `f5367a7a`: Mathlib bridge `Build completed successfully (3645
  jobs)`; all 15 `#print axioms` lines of `EqvSeams`/`EqvSeamsControl` standard; gate `lean-axioms` OK (5875, no sorry);
  gate failures `lean-manuscript` (2 unregistered modules), `claims`, `duplicate` (scans of the branch's research tree).
  The two modules are copied byte-identically to `research/equivalence/lean/` as [D] (blobs `ae09a26a`, `b9eb24b4`).
- 2026-10-10T20:32Z — dispatch 3/3: run 38084161796 on `288f80ec`, branch `dev-equivalence/kt4-at-l` (the ten Pauli-free
  FourCopy modules of `ff9c3a35`, blobs checked equal, over L's kernel; FourCopyPackage omitted) — for E5.
- 2026-10-10T20:35Z — commit `88cc525d` (E2): NOTES-E2, `lean/EqvSeams.lean`, `lean/EqvSeamsControl.lean`, probes, ledger rows.
- 2026-10-10T20:36Z — `experiments/e3_compress.py`: 7/7, `VERDICT COMPRESSION-DESCENT-EXACT`; replay identical. Import
  graph at L re-checked (no ball-side ↔ complex-side edge).
- 2026-10-10T20:38Z — commit `dc31472c` (E3): NOTES-E3, `e3_compress` probe and replay, ledger Kn row.
- 2026-10-10T20:40Z — E4 written (no new probe; citations re-read against the kernel anchors at L); commit `8103045f`.
- 2026-10-10T20:44Z — E5 and E6 written (E5's design-run result pending: run 38084161796 in progress).
- 2026-10-10T20:44Z — run 38084161796 (dispatch 3/3) on `288f80ec`: `Build completed successfully (3654 jobs)`; the six
  FourCopyHeadline prints standard; gate `lean-axioms` OK (6015, no sorry); gate failures `lean-manuscript` (10 unregistered
  modules), `claims`, `duplicate`. Recorded in NOTES-E5 §4 (R-E5.3). No dispatch remains in this thread's allowance.
- 2026-10-10T20:50Z — E2 addenda (Ω₄ also carries seed-orbit availability and K∞-1 for full effects [W5]; K∞-V4 relocated
  to sequential closure [W]; the per-type matrix-level remark on K∞-Copy); E7 written (readiness table, skeletons S1–S6,
  drafts only, no control plane); handoff proposals HP-1 (coordinator, ROADMAP K wording, not applied), HP-2 (bridge),
  HP-3 (countermodels), HP-4 (origin); ledger summary recounted (22 rows: 18 OPEN, 3 CONDITIONAL, 1 EXTERNAL).
- 2026-10-10T20:50Z — NOTES-E3 §2: `block` and `LabelInvariant` shown load-bearing for the descent by written generated-class
  countermodels (CONJECTURE [W]); R-E3.3 and S3's controls updated.
- 2026-10-10T20:53Z — hygiene: two table cells carried `|x|⁴` (a pipe inside a markdown cell); written `‖x‖⁴` in LEDGER and
  RESULTS; every table row's column count checked.
- 2026-10-10T20:55Z — NOTES-E3 §3 scope caveat (pressure test): the descent to odd carriers needs `ContextStable` with an
  odd-size spectator; it fixes the repertoire of carriers the formalism has as types, it does not produce them; R-E3.2
  scope sentence added.
