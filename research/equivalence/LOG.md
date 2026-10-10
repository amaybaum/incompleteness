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
- 2026-10-10T20:48Z — E2 addenda (Ω₄ also carries seed-orbit availability and K∞-1 for full effects [W5]; K∞-V4 relocated
  to sequential closure [W]; the per-type matrix-level remark on K∞-Copy); E7 written (readiness table, skeletons S1–S6,
  drafts only, no control plane); handoff proposals HP-1 (coordinator, ROADMAP K wording, not applied), HP-2 (bridge),
  HP-3 (countermodels), HP-4 (origin); ledger summary recounted (22 rows: 18 OPEN, 3 CONDITIONAL, 1 EXTERNAL).
- 2026-10-10T20:50Z — NOTES-E3 §2: `block` and `LabelInvariant` shown load-bearing for the descent by written generated-class
  countermodels (CONJECTURE [W]); R-E3.3 and S3's controls updated.
- 2026-10-10T20:51Z — hygiene: two table cells carried `|x|⁴` (a pipe inside a markdown cell); written `‖x‖⁴` in LEDGER and
  RESULTS; every table row's column count checked.
- 2026-10-10T20:52Z — NOTES-E3 §3 scope caveat (pressure test): the descent to odd carriers needs `ContextStable` with an
  odd-size spectator; it fixes the repertoire of carriers the formalism has as types, it does not produce them; R-E3.2
  scope sentence added.
- 2026-10-10T20:52Z — close of the session's plan (E1–E7 done). Commits on `research/equivalence`: `04e69e04` (E1), `88cc525d`
  (E2), `dc31472c` (E3), `8103045f` (E4), `32612d8b` (E5, E6), `a9a8b34e` (E5 close), `7787b699` (E7, handoffs),
  `0e5673f7` (E3 addendum), `adfe2503` (table hygiene), `0f52efab` (E3 scope caveat), and this entry. Disposable branches
  (not for merge): `dev-equivalence/kinf-seams` (`0578b13d`, `f5367a7a`) and `dev-equivalence/kt4-at-l` (`288f80ec`).
  Dispatches used: 3 of 3 (runs 38083220991 failed at one declaration and was repaired; 38083519826 and 38084161796 green
  at module level). A diagnostic script for run 1 of `e2_copy_conj` was run from the session scratchpad (outside the
  repository); its output is summarized in NOTES-E2 §3 and the run-1 files are kept here.
- 2026-10-10T20:55Z — LOG correction: three entry times had been written later than the commits that carry them; set to those
  commits' times (`git log --format=%cI`): the E7/addenda entry 20:50Z → 20:48Z (`7787b699`, 20:48:58), the hygiene entry
  20:53Z → 20:51Z (`adfe2503`, 20:51:34), the close entry 20:53Z → 20:52Z (`2ae3d47b`, 20:52:52). Every other entry checked
  against its commit time; no other content changed. Commit: this entry's (reported in the final message).

## Round 2

- 2026-10-10T21:49Z — round 2 opened at thread head `8c67c7fb` (verified: `git status` clean, `git log -1`). Re-read the
  charter, LOG, LEDGER, RESULTS, NOTES-E2 … E7, and from the overview worktree (branch `research/overview` @ `62cbb3cf`,
  read-only) `research/AUDITS/2026-10-10-round1/AUDIT-EQUIVALENCE.md` and `research/OVERVIEW.md`.
- 2026-10-10T21:49Z — **receipt of HO-2 v1** (`research/HANDOFFS/HO-2-bridge-to-equivalence-and-countermodels-finite-substrata.md`
  at overview `62cbb3cf`, blob `06c9d4c6`, sha256 `13abf306c4ad6466…`), copied byte-identically to
  `inbox/HO-2-bridge-to-equivalence-and-countermodels-finite-substrata.md`. **Reliance, stated before use.** (i) Only at
  its own labels; nothing in HO-2 is CERTIFIED, and no ledger status changes on its strength. (ii) HO-2c's one-token
  clause is taken as a CONDITIONAL [L] constraint (on Jordan's theorem and the classification of finite subgroups of
  SO(3), neither checked here) on any sourcing of K∞-Act / K∞-Drive through finite stage-preserving operations: an
  off-axis `ElementaryDrivability` (KInfFoundations.lean:264) is never the closure of directed stage-preserving finite
  operations, so the generator must cross stages. This is consistent with, and sharper than, the kernel fact the ledger
  already records (`finiteOrderOn_of_stagePreserving` CompositionOrder.lean:348 [K]: a stage-preserving datum has finite
  order); it is cited in the Kinf-Act / Kinf-Drive rows as CONDITIONAL [L] and is not used as a premise of any draft.
  (iii) HO-2a (a finite realized pair group of unitary or antiunitary conjugations leaves an exotic self-dual cone with
  H1–H3; CONDITIONAL on claim D [A]) and HO-2d (A_miss ⟺ (b) for `{R_z(θ), R_x(θ)}`, `cos θ = 3/5`; CONDITIONAL on
  closedness of K) bear on node E10's countercontrol; E10 recomputes its own countercontrol by exact computation and
  cites HO-2a/HO-2d only as comparators at their labels. (iv) HO-2b (`tr(cnot · actC R1) = 10/9`) is not used.
