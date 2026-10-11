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
- 2026-10-10T21:52Z — E8 begun: read `verification/infrastructure/v3/architecture.md` (K1, S7, G6, G10, S8 and the
  receipt field table) and the landed preregistrations of KTRANS-DENSE-1 and KT4-PREM-1 (block structure, decision
  rules, non-inference rule, controls, design evidence, predicted tree, stages, outcomes) and the invariant→checkpoint
  table of KINF-2 (§A.41). Mathlib API names checked against the Mathlib v4.33.0 sources fetched read-only from
  raw.githubusercontent.com into the session scratchpad (`Equiv.Perm.exists_extending_pair`, `Matrix.single_apply`,
  `submatrix_*`, `Fin.castLEEmb`, `AffineEquiv.map_vadd`, linarith's polynomial parsing).
- 2026-10-10T22:05Z — DEVIATION (scope of dev-branch writes, as in round 1): the Mathlib bridge builds only modules
  imported from the root `verification/lean-mathlib/OIBridge.lean`, so each dev branch adds one import line there
  besides its modules under `OIBridge/`; round 1's dev branches did the same. New this round: the dev branches are
  based on L `9f9f8257` directly (no `research/` tree), so the gate's `claims` and `duplicate` steps are meaningful and
  only `lean-manuscript` (no census family) is expected red.
- 2026-10-10T22:05Z — dispatch 1/3 (round 2): run **38090116254** on `05b5756c` (branch `dev-equivalence/kn-desc`,
  module `EqvKnDesc`, draft S3). Result (job 114324651733): `Build completed successfully (3644 jobs)`; all twelve
  `#print axioms` lines of `EqvKnDesc` `[propext, Classical.choice, Quot.sound]`; release gate every step PASS except
  `lean-manuscript` (1 problem: the unregistered module), `lean-axioms` 5872 named results, no sorry, 43 receipts hold,
  303 legacy records intact. Warnings only: three theorems carry unused `[Fintype S] [Fintype T]` section binders; one
  `haveI` style hint.
- 2026-10-10T22:18Z — dispatch 2/3: run **38090924005** on `195dfbee` (branch `dev-equivalence/omega4`, module
  `EqvOmega4`, draft S4). Result (job 114327010280): build FAILED at exactly two terms (lines 157, 215: `fun v hv =>
  le_of_lt hv` elaborated against `v ∈ omega4`, Type mismatch); every other declaration elaborated — the prints of
  `omega4_isCompact`, `conv_core`, `omega4_convex`, `abstract_strict`, `omega4_centrallySymmetric`, `sharpSeed_omega4`,
  `omega4_drivable` and `not_affine_eball_omega4` standard; the seven dependants of the two terms printed `sorryAx`
  (error recovery). Proof-only repair committed as `95beab2b` (blob `9030f471`), NOT dispatched: S4's one dispatch is
  spent; the repair is unmeasured.
- 2026-10-10T22:28Z — dispatch 3/3: run **38091534622** on `8c92343e` (branch `dev-equivalence/split-l3`): modules
  `StageSeed` (S1) and `CopyCovariance` (S2), split from the built `EqvSeams`/`EqvSeamsControl` with no statement
  changed, and `EqvLevel3` (node E9). This is S1's and S2's one dispatch and the round's last; no dispatch remains.
- 2026-10-10T22:28Z — drafts S1 (`preregistration-drafts/S1-kinf-seed.md`) and S2
  (`preregistration-drafts/S2-kinf-copy-type-covariance.md`) written; held for owner review; no round, PR or file under
  `verification/` created.
- 2026-10-10T22:31Z — LOG correction: the entry for drafts S1/S2 had been written as 22:30Z, later than its commit
  `7656bbe6` (22:28:46); set to 22:28Z. No other content changed.
- 2026-10-10T22:31Z — drafts S3 (`preregistration-drafts/S3-kn-descent.md`, design run 38090116254 green at the build)
  and S4 (`preregistration-drafts/S4-kinf-trans-separation.md`, marked not ready to freeze: its design run 38090924005
  failed at two terms and the proof-only repair `95beab2b` is unmeasured) written. Design modules copied verbatim to
  `lean/`: `EqvKnDesc.lean` (blob `8157f8ea`, = dev `05b5756c`), `EqvOmega4.run38090924005.lean` (blob `ee870649`, the
  built-and-failed text of `195dfbee`) and `EqvOmega4.lean` (blob `9030f471`, the repaired text of `95beab2b`).
- 2026-10-10T22:35Z — E9: `experiments/e9_level3.py` run 1: 7/7, `VERDICT LEVEL3-CONVERSE-BOUNDED`, replay identical (decision rule
  fixed before run 1; the script was edited before its first run only). `experiments/e9_dyn_finite.py` run 1: 3/3,
  `VERDICT FINITE-DYN-CONVERSE-INSTANCE`, replay identical. NOTES-E9 written (three readings of the converse: C-REG true
  by transfer along the stage map, C-DYN and C-KIN false with exact finite countermodels; repairing hypotheses H-FAC,
  H-UNIF, H-GEN, H-DYN). The design run of `EqvLevel3` (38091534622) is still queued; NOTES-E9 §6 pending.
- 2026-10-10T22:48Z — LOG correction: the two entries committed in `7b1a9205` (22:31:25) had been written as 22:32Z; set to 22:31Z.
- 2026-10-10T22:48Z — run 38091534622 (dispatch 3/3) measured: Mathlib bridge job 114328799399 `Build completed successfully (3646
  jobs)`; `StageSeed` 3, `CopyCovariance` 12 and `EqvLevel3` 4 prints, all `[propext, Classical.choice, Quot.sound]`;
  release gate every step PASS except `lean-manuscript` (3 problems: the three unregistered modules); `lean-axioms` 5879,
  no sorry. Modules copied byte-identically to `lean/` (`StageSeed` `b6369153`, `CopyCovariance` `fb9c73fe`, `EqvLevel3`
  `dc89d735`). NOTES-E9 §6 and drafts S1/S2 updated with the run. RESULTS rows R-AUDIT.1 (the coordinator's precision note
  on R-E3.4 and R-E5.1, acknowledged; old rows not edited), R-E8.1–R-E8.4 and R-E9.1–R-E9.4 appended. The E10 probe
  `experiments/e10_k2_schema.py` is running (run 1 started 22:43Z).
- 2026-10-10T22:52Z — E10: `experiments/e10_k2_schema.py` run 1 (started 22:43Z) terminated at 22:50Z after seven minutes at full
  CPU in sympy's simplification with no output (stdout block-buffered); kept as `e10_k2_schema.run1.{py,out,err}` (exit
  143). Run 2 changed the instances only (L2's flow at two rational angles; L4's five states with Gaussian-rational
  data, `φ₀` moved out of L4 and kept as F1's witness; `expand` for `simplify`; flushed prints), its decision rule
  fixed in the header before it ran: 9/9, `VERDICT K2-SCHEMA-SKELETON-CONSISTENT`, replay identical; the finite group
  `⟨cnot, actT R_z(π/2), actT cyc3⟩` has order 384. NOTES-E10 written (six-lemma skeleton; A_miss enters only at
  reachability; no spectral step; the finite clause and the flow alone fail at reachability; `R_z(θ₀)` with `cos θ₀ =
  3/5` and `cyc3` suffice given H3). RESULTS R-E10.1–R-E10.4; LEDGER round-2 notes (statuses at L unchanged). Handoff
  proposals HP-5 (coordinator), HP-6 (bridge, origin), HP-7 (countermodels) written.
- 2026-10-10T22:54Z — `experiments/e8_cite_check.py`: run 1 did not render (the checker read a design-module error location and a
  hypothesis name as kernel citations, and its floor of 40 exceeded the 37 citations found); kept as
  `e8_cite_check.run1.*`. Run 2 (scope rules and countercontrols X1–X3 in place of the floor, decision rule fixed
  before it ran): `VERDICT CITATIONS-RESOLVE`, 37 distinct citations, replay identical. RESULTS R-E8.5.
- 2026-10-10T23:04Z — E8 continued (S4's exact layer, which its Q-EXACT rule required and which was unwritten):
  `experiments/e8_ktrans_probe.py` assembled from `e2_drive_trans.py`'s D1–D9 and C1 (code copied, checked identical
  line for line; `e2_drive_trans.py` not edited) plus W5 (Euler identity; the gradient gap of `F` as an explicit sum of
  squares; eleven exact boundary points; a grid of 1669 states), the ball control C2 and the countercontrols XW1, XW2,
  its decision rule fixed in the header before run 1. Run 1: 12/12, XW1 and XW2 fail as stated,
  `VERDICT DRIVE-SEED-GEOM-SEC-CAP2-NOT-TRANS`; replay byte-identical. Pressure test: supporting-effect completeness with
  the full effects holds on every compact convex body in finite dimension and is already recorded in the archive
  (`threads/A/RESULT.md`; `threads/F/LEDGER.md` row B8), so W5 is CONFIRMING and S4 now advises omitting HP-1's phrase
  "and supporting-effect completeness". S4 updated (Q-EXACT question and rule, exact layer, non-inference rule, HP-1
  note, controls, invariant row, design table, predicted outputs); still not ready to freeze (`C0`). RESULTS R-E8.6.
- 2026-10-10T23:08Z — NOTES-E8 written: the round's instruction names a NOTES file per node and E8 had none; it records
  the four drafts, the three dispatches with their Mathlib bridge jobs and steps, S4's exact layer and the §A.31
  classification.
- 2026-10-10T23:09Z — `experiments/e8_cite_check.py` run 3: run 2's files kept as `e8_cite_check.run2.*` (they are the
  measurement R-E8.5 cites, at `4a18e16a`); the script's documents list gains NOTES-E8.md, its decision rule unchanged.
  `VERDICT CITATIONS-RESOLVE`, 43 distinct citations (59 occurrences, 31 named pairs), replay identical. RESULTS R-E8.7.
- 2026-10-10T23:10Z — run status read through the API: runs 38090116254 and 38090924005 concluded `failure` (the release
  gate at `lean-manuscript`, by construction on a dev branch; the build, respectively); run 38091534622 was still in
  progress in its numerical-probe jobs, its Mathlib bridge job 114328799399 complete as recorded at 22:48Z (Build
  success, release gate red at `lean-manuscript` only).

## Round 3

- 2026-10-10T23:50Z — round 3 opened at thread head `5d266133` (verified: `git status` clean, `git log -1`). Re-read the
  charter, LOG, LEDGER, RESULTS, NOTES-E2 … E10, the modules under `lean/`, the drafts under `preregistration-drafts/`,
  `research/OVERVIEW.md` at overview `2a055180` (fetched from `origin research/overview`), the handoffs addressed to this
  thread at that commit, and AGENTS.md at L (sha256 `959c4333…`, identical to the copy in the main checkout).
- 2026-10-10T23:50Z — **receipt of HO-9 v1, HO-10 v1, HO-12 v1, HO-15 v1** (`research/HANDOFFS/` at overview `2a055180`),
  each copied byte-identically to `inbox/` (sha256 and git blob checked equal to the source):
  HO-9 `4b2c4a0f708e7ec5…` (blob `3e1260e3`), HO-10 `ef909f693f4b058a…` (blob `134197b1`), HO-12 `b9584f3be12d1b47…`
  (blob `a9db4b81`), HO-15 `f941456f55174f23…` (blob `f9a525be`). HO-13 and HO-14 have this thread as source and are not
  copied. **Reliance, stated before use** (only at the labels the handoffs carry; nothing in them is CERTIFIED except the
  kernel declarations they name at L, each re-read at L before this entry):
  - **HO-9 (item 3 only; items 1, 2, 4–7 are addressed to bridge and origin and are context, not relied on).** Item 3 —
    on a passive, repeatable, finite-rank tower every reversible datum has finite order on the completed chart body, so
    no OPS-Γ datum and no drive — is taken as a CONDITIONAL constraint ([W] tower step, [D] origin design run) on any
    sourcing of K∞-Drive and K∞-Trans through classical conditioning towers; K∞-Seed is compatible with passive towers.
    Its stage-crossing clause is CERTIFIED: `not_stagePreserving_of_infiniteOrderOn` (CompositionOrder.lean:378, read at
    L). Used in the LEDGER round-3 notes (Kinf-Drive, Kinf-Trans) only; not a premise of any draft or theorem.
  - **HO-10.** Item 2 (B3.C: a compact pair group containing `cnot` with abelian identity component leaves an exotic
    invariant cone; CONDITIONAL on claim (D) [A]) and item 1 (the reachability theorem; CONJECTURE, written proof) are
    used as comparators for node E11: they say the reachability hypothesis of the K2 schema cannot be met by any such
    group, the complement of the schema's sufficient clause. Not a premise of the design module; nothing in HO-10 is
    kernel-checked.
  - **HO-12.** Item 1's (D1)–(D2) (the two-token dictionary and its intertwining; CONJECTURE-exact [X]) and the bridge's
    draft `BridgeDictionary.lean` (sha256 `e4b60411…`, which did not build at `dict_tens`) are the convergence target of
    node E11's dictionary, which re-derives the dictionary in this thread's own design module and cites the draft; the
    clause (T) (a named premise; FAILED as a bridge) and items 2–4 (the A_miss split; the non-forcing CONDITIONAL on claim
    (D); the order 11520 CONJECTURE) are recorded in the LEDGER round-3 note for K2 at their labels. HO-6's interface
    request is answered by item 1; nothing in HO-12 is CERTIFIED.
  - **HO-15.** Items 1–5 (Aut(Ω₄) = O(3) × ℤ₂; its orbits; `c*` constant on `C¹` bodies; the rank of the second
    fundamental form; Ω₄'s cone self-dual for no inner product), each CONDITIONAL [W]+[X], and the assumption-watch marker
    are the starting point of node E13 and a constraint on draft S4's non-inference rule and HP-1's wording; E13 re-checks
    item 5 by its own exact computation before using it. The two kernel theorems it names, `exists_affine_image_eq_eball`
    (TransitiveBody.lean:602) and `exists_affine_image_eq_eball_of_dense` (DenseOrbit.lean:174), are CERTIFIED at L (read
    at L). Nothing else in HO-15 is CERTIFIED.
  No research step of round 3 precedes this receipt's commit.
- 2026-10-10T23:52Z — E12 S0: `NOTES-E12.md` opened with its reading rule and predictions P1–P4 for the dispatch of
  `dev-equivalence/omega4` at `95beab2b` (head checked by `git ls-remote` at 23:51Z); committed before the dispatch.
- 2026-10-10T23:52Z — dispatch 1/3 (round 3): run **38096511360** on `95beab2b` (branch `dev-equivalence/omega4`, the repaired
  `EqvOmega4`, draft S4's checkpoint `C0`), no further repair.
- 2026-10-11T00:15Z — run 38096511360 measured (Mathlib bridge job 114343410536): Build `success` (3644 jobs), `EqvOmega4`
  built with warnings only (deprecated `Set.mem_setOf_eq`, `push_neg`), all fifteen prints `[propext, Classical.choice,
  Quot.sound]`; release gate every step PASS except `lean-manuscript` (1 problem), `lean-axioms` 5875, no sorry, 303 legacy
  records intact, 43 receipts hold. `C0` MET by the rule fixed at 23:52Z; P1–P3 held (P3 to the count). The `lean/` copy
  `EqvOmega4.lean` checked byte-identical to the dispatched blob (`9030f471`). NOTES-E12 measurement section; draft S4
  updated (readiness line, design table row 2, predicted outputs, invariant row `C0`, stages line); RESULTS R-E12.1; LEDGER
  round-3 note (Kinf-Trans).
- 2026-10-11T00:35Z — E11 begun. Read on the coordinator's instruction (a cross-branch read the README's round-1 rule did not
  foresee; recorded as a deviation): `research/bridge/lean/BridgeDictionary.lean` (sha256 `e4b60411…`) and NOTES-B9 §4
  (sha256 `949124f0…`) at `origin/research/bridge` `3686049e`. The design module `lean/EqvK2Schema.lean` uses that
  draft's `pauli`, `tokMat`, `dict` verbatim and the recorded fix for `dict_tens`. No local Lean toolchain exists and the
  shared disk has 7.3 GB free (other threads' worktrees are active on the same machine), so no Mathlib cache was fetched:
  every Lean API name was checked against the local Mathlib checkout at tag `v4.33.0` (`db584cd6`, the pin) and against
  kernel precedents at L (`pauliBase_mul_table` DiscreteCompletion; `Submonoid.closure_induction` PositiveReachability;
  `psdFactorization_discharged` BoundaryAudit.lean:100). NOTES-E11 S0 (predictions P-X, P-D and the reading rule) and
  the probe `experiments/e11_k2_dict.py` (decision rule in its header) committed before the probe's first run
  and before the dispatch.
- 2026-10-11T00:36Z — LOG and probe-header time correction: the E11 entry and the probe header had been written as 00:38Z and
  00:36Z, later than commit `97b6f080` (00:35:41Z); set to 00:35Z (the header now cites the `date -u` reading and the commit).
  Edited before the probe's first run; the decision rule is unchanged.
- 2026-10-11T00:36Z — `experiments/e11_k2_dict.py` run 1 stopped with a TypeError after C1–C5 passed (the helper `R(a, b)`
  called with one argument in C6's instance list); kept as `e11_k2_dict.run1.{py,out,err}`. Run 2 changes only those two
  calls (`R(0, 1)`, `R(1, 1)`), decision rule unchanged: 18/18, `COUNTER X1 fails as stated`, `COUNTER X2 fails as
  stated`, `VERDICT E11-DICT-STATEMENTS-EXACT`; replay byte-identical (py `09da63b1…`, out `2a73ca38…`). Prediction P-X held.
- 2026-10-11T00:37Z — dispatch 2/3 (round 3): run **38099025197** (created 00:36:52Z, `workflow_dispatch` of `verify.yml`)
  on `472835c5` (branch `dev-equivalence/k2-schema`, parent L; written by git plumbing into a scratch index, so no new
  worktree: the diff from L is exactly `verification/lean-mathlib/OIBridge/EqvK2Schema.lean`, blob `3edcf9b0`,
  byte-identical to `lean/EqvK2Schema.lean` at `97b6f080`, and the import line `import OIBridge.EqvK2Schema` after
  `import OIBridge.RelcSelectC5` in `OIBridge.lean`, the recorded deviation). Still queued at 00:53Z.
- 2026-10-11T00:53Z — E13 begun. NOTES-E13 S0 (written 00:46Z: productivity test, the candidate countermodel
  Ω⋆ = Ω_{1/3}, the lemma on centrally symmetric self-dual bodies, predictions) and the exact probe
  `experiments/e13_selfdual_body.py` (decision rule in its header, written 00:47Z) committed together, before the probe's
  first run. The probe was edited before any run (pre-run review: the witness for outside points with `u' = 0` or
  `v' = 0` rewritten, a guard against a zero direction vector, exact `cancel` in place of `simplify`); its decision rule
  was not changed. Read at L for E13: `ElementaryDrivability` (KInfFoundations.lean:264), `ball3Drive` (:449),
  `KInf1` (:1013), `SharpSeed` (OrbitGeneration.lean:65), `PreservesBody` (:69), `BoundaryTransitive` (:79),
  `DenseBoundaryOrbit` (DenseOrbit.lean:53) and the hypotheses of TransitiveBody.lean:602 and DenseOrbit.lean:174.
- 2026-10-11T01:07Z — LOG time correction: the E13 entry was written as 00:54Z, later than its commit `dc44e737`
  (00:53:45Z); set to 00:53Z. `experiments/e13_selfdual_body.py` run 1 (started 00:53:52Z, after that commit; decision
  rule unchanged): 11/11, `COUNTER XS1 fails as stated` (pairing −1/80), `COUNTER XS2 fails as stated` (−17/80), the
  true inner product on the same pair 3/16, `VERDICT E13-SELFDUAL-DRIVABLE-NOT-TRANS`; replay byte-identical (py
  `fffa8bb3…`, out `a0063f05…`). The probe's predictions in NOTES-E13 S0 held (A10 also measured the meridian's
  second derivative −24 at the regular point m = 1).
- 2026-10-11T01:17Z — E13, the centrally symmetric branch. NOTES-E13 S0-b (the lemma completed as L-a/L-b/L-c; the
  candidate Ω_cs; predictions) and the exact probe `experiments/e13b_central_selfdual.py` (decision rule in its header,
  written 01:15Z) committed together, before the probe's first run. S0 had predicted this branch would stay OPEN; the
  candidate came from written analysis after S0, and a floating-point scratch exploration in the session scratchpad (not
  committed; a design aid, not evidence) checked that its parameters close up. Pre-run review fixed two defects in the
  probe (the order J⁻¹, rot(π), J in B9; an exact matrix equality in place of `simplify` in B4); the decision rule was
  not changed. Kernel read at L for the branch: `card_le_two_of_centrallySymmetric` (KInfFoundations.lean:632).
- 2026-10-11T01:21Z — run 38099025197 measured (Mathlib bridge job 114350890660): Build `failure` at four proofs of
  `EqvK2Schema` (105:87 `dict_tens`, 122:67 `dict_smul`, 167:64 `trace_dict_mul`, 235:2 `dict_coordOf`), one
  rewriting-order defect (`Fin.sum_univ_four` before `Matrix.sum_apply`; `Matrix.add_apply` / `Matrix.trace_add`
  missing); prints standard for 10 of 22, `sorryAx` for the 12 that are or use those four. Reading PARTIAL by the rule
  fixed at 00:34Z. The dispatched text kept as `lean/EqvK2Schema.run38099025197.lean` (blob `3edcf9b0`); the repair
  (four `simp only` lists, proof-only) is `lean/EqvK2Schema.lean` (blob `659ae36c`), written into the dev commit
  `aabc649e` (parent `472835c5`, by plumbing). NOTES-E11 measurement section and the prediction for dispatch 3/3
  written before it.
- 2026-10-11T01:22Z — dispatch 3/3 (round 3; the last): run **38101580750** (created 01:21:50Z) on `aabc649e`
  (`dev-equivalence/k2-schema`, the proof-only repair; pushed 01:21:46Z, fast-forward from `472835c5`). No further
  dispatch is available this round.
- 2026-10-11T01:23Z — E13 measured. `experiments/e13b_central_selfdual.py` run 1 (started 01:17:53Z, after commit
  `6a7a1e77`; decision rule unchanged): 11/11, `COUNTER XB1 fails as stated`, `COUNTER XB2 fails as stated`, `VERDICT
  E13-CS-SELFDUAL-DRIVABLE-NOT-TRANS`; replay byte-identical (py `c3482560…`, out `24e01a77…`). NOTES-E13 §§1–5 (the
  written steps, the lemma L-a/L-b/L-c, the outcome NEW, the sharpened assumption-watch marker); RESULTS R-E13.1–R-E13.4;
  LEDGER round-3 note (Kinf-Trans, self-duality). S0's node prediction (centrally symmetric case OPEN) was wrong: the
  branch closed negatively (Ω_cs).
- 2026-10-11T01:30Z — E14 begun (time permits). Read at L: `QuasilocalSystem` (QuasilocalCharacterization.lean:168),
  `OISystem` (:463), `LocalityPreserving` (:475), `phaseQ_ne_heisQ` (:792), `CouplingGraph` (RegionTower.lean:254),
  `FiniteRange` (QuasilocalAlgebra.lean:919), `ReversibleDynamics` (:956), `hat` (:1040), `transported` (:1109).
  NOTES-E14 S0 (three readings of "H-DYN at every finite stage", predictions) and the exact probe
  `experiments/e14_hdyn_rings.py` (decision rule in its header, written 01:29Z) committed together, before the first run.
- 2026-10-11T01:31Z — LOG time correction: the E14 entry was written as 01:31Z, later than its commit `3c10fb14`
  (01:30:37Z); set to 01:30Z. `experiments/e14_hdyn_rings.py` run 1 (started 01:30:40Z; decision rule unchanged): 7/7,
  `COUNTER XR1 fails as stated`, `COUNTER XR2 fails as stated`, `VERDICT E14-HDYN-READINGS-SEPARATED`; replay
  byte-identical (py `1db6a11b…`, out `cfd9aa1f…`). NOTES-E14 §§1–3; RESULTS R-E14.1–R-E14.3; LEDGER round-3 note
  (L3-conv). Every S0 prediction held.
- 2026-10-11T01:33Z — run 38101580750 measured (Mathlib bridge job 114358419270): Build `success` (3644 jobs),
  `EqvK2Schema` built with warnings only, all 22 prints standard (EqvK2Schema.lean:453–474); release gate red only at
  `lean-manuscript` (1 problem), `lean-axioms` 5882, no sorry, 303 legacy records intact, 43 receipts hold; the
  Lean kernel check job `success`; seven long numerical-probe jobs still running at 01:32Z. Reading BUILT by the rule
  fixed at 00:34Z; the prediction written at 01:21Z held exactly. The `lean/` copy is byte-identical to the dispatched
  blob (`659ae36c`). NOTES-E11 measurement section; RESULTS R-E11.1–R-E11.4; LEDGER round-3 note (K2).
- 2026-10-11T01:35Z — handoff proposals HP-8 (bridge: the dictionary kernel-checked in a design run; the recorded
  `dict_tens` fix corrected), HP-9 (countermodels and coordinator: self-duality is not a source of K∞-Trans; the
  sharpened marker), HP-10 (coordinator: S4 ready; S6's skeleton built; the infinite-volume form of H-DYN). Citation
  re-check prepared: run 3's files kept as `e8_cite_check.run3.*`; run 4 extends the documents list to the round-3
  documents and applies the existing design-module rule to `EqvK2Schema` and to the repaired `EqvOmega4`; the decision
  rule is unchanged. Committed before run 4.
- 2026-10-11T01:36Z — `experiments/e8_cite_check.py` run 4 (started 01:35:37Z, after commit `b955d119`): 54 distinct
  citations (110 occurrences, 49 named pairs), countercontrols X1–X3 fail as stated, `VERDICT CITATIONS-RESOLVE`; replay
  byte-identical (py `88dd6b1d…`, out `2871d48e…`). RESULTS R-CITE.3.
- 2026-10-11T01:36Z — **Round 3 closed.** Nodes done, in the instructed order: E12 (S4's `C0` met; S4 ready for owner
  review), E11 (BUILT after one proof-only repair), E13 (two countermodels and a lemma; the centrally symmetric branch
  closed, against S0's prediction), E14 (three readings separated; the transport form gives the passage, written).
  Rows added: R-E12.1; R-E11.1–R-E11.4; R-E13.1–R-E13.4; R-E14.1–R-E14.3; R-CITE.3 — no earlier row's label changed.
  LEDGER round-3 notes: Kinf-Trans (two), K2, L3-conv, Kinf-Drive; statuses at L unchanged. Handoff proposals HP-8,
  HP-9, HP-10. Dispatches used: 3 of 3 — 38096511360 (`dev-equivalence/omega4` `95beab2b`; job 114343410536; Build
  success, 15/15 standard), 38099025197 (`dev-equivalence/k2-schema` `472835c5`; job 114350890660; Build failure at four
  proofs, 10/22 standard), 38101580750 (`dev-equivalence/k2-schema` `aabc649e`; job 114358419270; Build success, 22/22
  standard; gate red only at `lean-manuscript`, `lean-axioms` 5882). No job or run was cancelled; at 01:36Z seven long
  numerical-probe jobs of run 38101580750 were still running (they do not bear on the design measurement). Deviations,
  all recorded above: one import line per design module in `OIBridge.lean` on each dev branch; a cross-branch read of
  the bridge's draft dictionary and NOTES-B9 §4 on the coordinator's instruction; dev commits written by git plumbing
  into a scratch index (no new worktree); no local Lean toolchain (API names checked against the pinned Mathlib
  checkout); a floating-point scratch exploration (not committed) to choose Ω_cs's parameters before its exact probe;
  three LOG time corrections (entries written a few seconds ahead of their commits). Citation check re-run over the
  round-3 documents (run 4, R-CITE.3). No preregistration became a round; nothing was merged, and nothing outside
  `research/equivalence/` changed on this branch.

## Round 4

- 2026-10-11T03:04Z — round 4 opened at thread head `c10dbaee` (verified: `git status` clean, equal to
  `origin/research/equivalence`). Re-read the charter, LOG, LEDGER, RESULTS, NOTES-E10 … E14, `lean/EqvK2Schema.lean`,
  drafts S2 and S4 (the native V3 format) and HP-8 … HP-10. Read at L in this branch's own tree:
  CompositeDimension.lean (`IsNot` :210, `NativeGate` :218, `maxCone` :186, `actT` :198, `actC` :201,
  `finrank_plus_eq_finrank_minus` :682, `cnot` :775), QuasilocalCharacterization.lean (`QuasilocalSystem` :168,
  `OISystem` :463, `LocalityPreserving` :475), QuasilocalAlgebra.lean (`FiniteRange` :919, `ReversibleDynamics` :956,
  `hat` :1040, `transported` :1109). The round-3 coordinator audit and `research/OVERVIEW.md` were not read this round;
  the coordinator's summary of the audit (no label changes; the `dict_tens` finding holds for the one-list rendering;
  `EqvK2Schema`'s A_miss is the full-flow form of HO-5, not HO-13's two-rotation clause) is taken from the round-4
  instruction.
- 2026-10-11T03:04Z — **cross-branch reads on the coordinator's instruction**, all by
  `git -C /home/user/wt-research/overview show 742c6b2f:research/HANDOFFS/<file>` (branch `research/overview` @
  `742c6b2f`): the nine handoffs of the next entry (copied); HO-18 v1 (sha256
  `df704843343310fb16ed1eac29564ca5091ce1a3225d3796ec185d8c6b6731ed`) and HO-19 v1
  (`ad17f101a560674b437d170dce8b7c776da59a00021fbc990979d73093a3184b`), this thread's own handoffs as issued, read and not
  copied (as HO-13 and HO-14 in round 3); and `research/HANDOFFS/README.md`
  (`cdc742d205e49c60496a1ae247953a0b1cf640e05742f05144cd4cb0c2385a41`, the protocol and the index). Nothing else on that
  branch was read.
- 2026-10-11T03:04Z — **receipt of HO-9 v2, HO-17 v1, HO-20 v1, HO-21 v1, HO-22 v1, HO-23 v1, HO-24 v1, HO-25 v1,
  HO-26 v1** (`research/HANDOFFS/` at overview `742c6b2f`), each copied byte-identically to `inbox/` (sha256 and git blob
  checked equal to the source): HO-9 v2 `bd62649d0b7eb594…` (blob `bc4a8930`), HO-17 `65d2f79a0421b1b1…` (`fb5cd86c`),
  HO-20 `f36b244824f1f096…` (`c0d772b8`), HO-21 `5b8599be79351d86…` (`37350cdc`), HO-22 `3a6440f0fa4343c2…` (`1cffc118`),
  HO-23 `3c1e126d889b2ff9…` (`39579579`), HO-24 `27175857ac88aac8…` (`a84866aa`), HO-25 `9341f3f3df33fdd2…` (`3cbdc47b`),
  HO-26 `4ee56f58add22fed…` (`478a9fa1`). Kernel lines the relied-on items name, re-read at L before this entry:
  CompositionOrder.lean:348, :378; JordanClassification.lean:84 (`psd_iff_trace_nonneg`); KInfFoundations.lean:386
  (`rotLin`); BoundaryAudit.lean:100; StructuralClosure.lean:261; OIRealization.lean:360. **Reliance, stated before
  use** (only at the labels the handoffs carry; nothing in them is CERTIFIED except the kernel declarations they name
  at L):
  - **HO-9 v2** supersedes HO-9 v1 (received in round 3, `44c2708c`; the v1 file stays in `inbox/` as the record of that
    receipt). The change is item 7's may-not-assume clause only; this thread relied on item 3 only and still does, as
    a constraint on sourcing K∞-Drive and K∞-Trans through classical conditioning towers. Item 7's corrected clause is
    read as stated in v2; no round-4 node argues about `DenseUnitaryControl`.
  - **HO-17 v1 (items 4, 6, 7, 8 addressed here).** Item 4 (HO-13's token pair on one re-preparing token, CONDITIONAL on
    the cosine re-preparation law, which lies outside the stated access and is false there by item 1) is cited in draft
    S6 as context for the two-rotation clause, at its label; it is not a premise. Items 6 and 7 are recorded and not
    used: no round-4 node uses `DenseUnitaryControl` or the balanced angle. Item 8 (availability at a level is not the
    group generated at that level) is recorded as an assumption-watch marker; no round-4 node makes an availability
    argument over `genTheory`. Item 5's reading (the re-preparing premise supplies H1 and the token invariances, not H2
    or H3) is context for S6's statement of what it does not source. Items 1–3 are context.
  - **HO-20 v1.** Item 4 (the H-level premise of HO-13's clause, (T) at `θ₀` with `J`, is H-OI_g at `{R_z(θ₀), J}`,
    nothing weaker; CONDITIONAL on claim (D) [A], the stage-4 record [A] and HO-13 item 2) is recorded in S6 beside the
    two-rotation clause that S6 does not formalize. Item 6 (the L-REG marker) is recorded; no round-4 node reads the
    certified `substratumClass_contextStable` (StructuralClosure.lean:261) configuration-wise. Items 1–3, 5, 7 are
    context.
  - **HO-21 v1.** The bridge's `BridgeDictionary` (built, 20/20 [D]; not certified) carries the gate (D2), the monomial
    images and `rotZ (cos t) (sin t) = rotLin t` on the same definitions as `EqvK2Schema`. S6 records them as the
    statements a converged dictionary module would add; they are not part of S6's frozen surface, and S6's exact layer
    checks the conjugation formulas it uses by its own exact computation. Item 3 (two working renderings of the
    `dict_tens` proof) is recorded; it agrees with the coordinator's precision on HO-18.
  - **HO-22 v1.** Item 1 (`⟨cnot, actT J, actT S, actT nflip⟩ = Stab_C(Z ⊗ 1)`, order 384, CONJECTURE exact) and item 3
    (`cnot`, `actT J`, `actT R_z(θ₀)` close to the block-diagonal `SU(2) × SU(2)` fixing `Z ⊗ 1`, whose product orbit is
    every pure state; CONJECTURE exact + written) are cited in S6 as the structural reason the full-flow and
    two-rotation clauses reach every pure state and the finite clause does not; S6's probe recomputes the order 384
    itself. Items 2, 4, 5 are context.
  - **HO-23 v1.** The finite case of `ReachUnitary` (`reachUnitary_finite`, [D] on the bridge's branch, not certified) is
    cited in S6 as a comparator for the countercontrol's reachability side: for a finite group the analogue of
    `ReachPure` fails. S6 does not depend on it: the thread's own exact witness (`φ₀`, NOTES-E10 F1) is the frozen
    instance. B7-1 for subgroups of positive dimension is not used.
  - **HO-24 v1.** The explicit exotic cone `K(G₃₈₄·z*)` (`h* = (10, 2 − 2i, −1 − 3i, 3 − i)/√128`, `c* = 401/400`) is
    S6's countercontrol, as instructed. Its self-duality is CONDITIONAL on Theorem S′ [W] (read by the coordinator and
    found sound, not kernel-checked) and the operator-norm bound [W]; every exact item (the group of order 384, the 192
    defects, the overlap range, H1 for each defect, (CC) on all 18336 pairs at `401/400` and its failure at `301/300`)
    is recomputed by this thread's own probe before S6 cites it, and S6's decision rule for the countercontrol reads
    only those exact items. Items 2, 5, 6 are context for S6's non-inference rule.
  - **HO-25 v1.** Item 1 (the Clifford half alone leaves an explicit exotic cone, CONDITIONAL on S′ [W]) and item 2 (the
    continuous half: rank-one route closed; exotic cones by claim (D) [A] only) are recorded in S6 at their labels: each
    half of A_miss alone fails to force `Q3` on the cone side, so S6 asserts nothing about either half. Items 3–6 are
    context.
  - **HO-26 v1.** Item 1's two-defect criterion (the (CC) inequality, CONDITIONAL on S′ [W]) is the condition S6's probe
    checks pair by pair; item 3 (T fails on every explicit cone of the record; `K_circ` open) and the two refined
    assumption-watch markers are recorded in the LEDGER's round-4 note for K2 at their labels. E16 does not use T.
  - **HO-18 v1 and HO-19 v1 (this thread's own, read as issued).** HO-19: every statement is what NOTES-E13 and
    R-E13.1–R-E13.4 carry; its item 3 distributes the sub-labels differently from NOTES-E13 §2 (HO-19's "(L-c)" is the
    last sentence of NOTES-E13's L-b, and NOTES-E13's L-c is HO-19's concluding sentence), with no difference of
    content; no correction is requested. **HO-18 item 2 is not what this thread meant**: it describes LOWER as "every
    product of `eball 3` states has a positive semidefinite dictionary image" and UPPER as bounding "a cone containing
    the products". The module proves something else: LOWER `Q3_subset_of_pure` (EqvK2Schema.lean:308) — a set closed
    under addition that contains a table of every rank-one positive matrix `x xᴴ` contains `Q3`; UPPER
    `subset_Q3_of_pure_dual` (:297) — a set that contains a table of every rank-one positive matrix and lies in its own
    dual lies in `Q3` (R-E11.2). The hypothesis of both is every pure state, not the products; with products only,
    UPPER would make A_miss and `ReachPure` superfluous, which the exotic cones of the record (K(Z_F); HO-24's cone)
    refute. A corrected version is requested from the coordinator through handoff proposal HP-11 (to be written this
    round); the file is not edited. Every other statement of HO-18 is as meant (item 3 with the coordinator's precision;
    the conjugation facts of its countermodels clause agree with NOTES-E10 L2 up to a global phase of `U_J`).
  No research step of round 4 precedes this receipt's commit.
- 2026-10-11T03:10Z — E15 begun. NOTES-E15 S0 (written 03:08Z: what the node is, the draft's decisions, predictions) and
  the exact probe `experiments/e15_k2s6_probe.py` (decision rule in its header, written 03:08Z; X6's header text
  narrowed to the argument the code uses before any run) committed together, before the probe's first run.
- 2026-10-11T03:15Z — LOG time correction: the E15 entry committed in `f7c3668c` (03:10:56Z) had been written as 03:13Z,
  later than its commit; set to 03:10Z. No other content changed.
- 2026-10-11T03:15Z — E15 measured. `experiments/e15_k2s6_probe.py` run 1 (started 03:11:06Z, after commit `f7c3668c`;
  decision rule unchanged): 12/12, `COUNTER XC1/XC2/XC3 fails as stated`, `VERDICT E15-S6-EXACT-LAYER-CONSISTENT`; replay
  byte-identical (py `78cd7c59…`, out `3ee625fe…`). Every S0 prediction held; the flow witness's maximum overlap
  `1949/2048` equals the hand value of S0. Draft S6 written (`preregistration-drafts/S6-k2-schema-pair-cone.md`,
  round id `K2-SCHEMA-1`; nothing activated, nothing under `verification/`). NOTES-E15 §§1–3; RESULTS R-E15.1–R-E15.3;
  LEDGER round-4 note (K2). No dispatch used (the module was built in round 3, run 38101580750).
- 2026-10-11T03:29Z — **coordinator addendum received** (mid-round, while E16's S0 was being drafted; recorded before any
  further research step). The owner's round-4 priorities: (1) bridge B14–B15 with origin O11; (2) equivalence E15–E16,
  the decisive question stated as "can the pair-level results imply the transitivity needed at higher levels without
  adding assumptions?"; (3) countermodels C17–C20; (4) bridge B16–B17 and equivalence E17–E18. Three standing rules,
  effective now and applied to everything this thread records from here on: (1) derive, do not introduce — every result
  lists its hypotheses, each classified as (i) an item of the OI premise inventory at its status at L, cited by id, or
  (ii) an introduced hypothesis, flagged "introduced, not an OI premise" in the RESULTS row and the LEDGER; a result is
  written "OI ⇒ X" only when every hypothesis is of kind (i), otherwise "OI + {named hypotheses} ⇒ X"; an introduced
  hypothesis never becomes an OI axiom by use; for E16 a positive answer is written "OI + {…} ⇒ ellipsoid" with the
  braces filled, a negative answer names the exact body that meets the pair-level hypotheses and is not an ellipsoid;
  (2) the premise inventory (stage 6) is the reference point; (3) the evidence layers [D], [W], [K] and CERTIFIED are
  kept separate, and a preregistration draft states the layer of each cited input. Node list and order unchanged.
- 2026-10-11T03:29Z — **reads of the premise inventory, authorized by the addendum** (branch `research/archive` @
  `4dc0321c`, worktree `/home/user/wt-research/archive`, read-only; each file's sha256 checked equal to the value the
  addendum states, and its blob checked equal to the copy in this branch's own `research/archive/` tree):
  `research/archive/pt/I4/INVENTORY-HEADER.md` (`02c431ff5dd5ee68892128aa3162c48de78814edb3690ae2c98900e22cf0eb07`, read
  whole), `pt/I4/INVENTORY.md` (`43bbada1db14f052e3ec3eb3d7fc99d1bb042d41a143c912aa6ca3e4cad75461`, record index and
  section headers), `pt/G6/GRAPH.md` (`83f4619f48982f881e43b0a19c14b7c6cc182179ea2a3c69dcf5992c4aab342c`, §0),
  `pt/R6/REASSESSMENT.md` (`1ff62ad633fbd752f247d49b605e6cc8d984e23d8b7151b6497cdd60fa884ffe`, Table A2 from line 277),
  `pt/INTEGRATION-NOTE-STAGE6.md` (`1130a8c5e72e03503ebd8c6183b468dfadc8ebe813bfc857bc21f6262bcf0e6b`, read in round 1, not
  re-read). The K-programme records the addendum names are I3's, in `pt/I3/INVENTORY.md`
  (`51eff9afef1f7ed25d82dc140a83dd97a9b24765d39b84cfdb636fa38ca96d7d`, blob `49f08221`, 187 records; the stage-6 total of 633
  is I1 85 + I2 113 + I3 187 + I4 248): read the header, the record index, and records I3.1–I3.2, I3.8–I3.10, I3.42–I3.44,
  I3.66, I3.68, I3.88–I3.91, I3.103–I3.105, I3.113–I3.116, I3.143–I3.176.
- 2026-10-11T03:30Z — E15 brought under the standing rules (the node was closed at `5670ec63`, before the addendum):
  draft S6 gains a classification table of the schema's hypotheses against the inventory (kind (i): I3.1, the products
  clause of I3.43, the ball through I3.89 from the open K∞ seams; kind (ii), introduced, not OI premises: H2, H3, A_miss in
  the full-flow form, `ReachPure`) and a table of the evidence layer of every cited input; its earned reading, licensed
  wording and unsourced-premises paragraph name the four introduced hypotheses. RESULTS R-E15.1–R-E15.3 (rows of this
  round, unaudited) amended in place with the form of each result and the flags; the LEDGER's round-4 K2 note likewise.
  No measurement or label changed.
- 2026-10-11T03:34Z — E16 begun, under the standing rules. Record search first (§A.19): the trace form of the parity count
  from the control relation is the archive's relC ledger N1.3 [A] (`research/archive/relc/LEDGER.md`), landed for the
  ball only as `not_even_of_relC` (RelcSelectParity.lean:354) [K]; ODD-CHAR-1 (`exists_frame_gateRel_iff_odd`,
  OddChar.lean:184) and the KIRC no-go record (`kirc/THEOREM.md`, `kirc/UNIFORM-NOGO.md`: non-ball local systems are
  "Barnum–Wilce territory") read. NOTES-E16 S0 (written 03:31Z: the pair-level hypotheses P1–P4 stated and classified
  against the inventory; the analysis (A1)–(A4) before computation; the probe order; predictions) and the exact probe
  `experiments/e16a_tokens_pair.py` (decision rule in its header, written 03:31Z) committed together, before the probe's
  first run.
- 2026-10-11T03:41Z — **coordinator addendum 2 received** (the owner's framing; recorded before further research steps; node
  list, order and budget unchanged): with A the applicable non-hypothetical OI premises at L and (b) the composite action,
  stage 6 gives K(Z_F) ⊨ A and K(Z_F) ⊭ (b); the live objectives are (1) a sufficient bridge H with A + H ⇒ (b) — the
  candidate H-OI_g at `{R_z(θ₀), J}`, carried to `Q3` by the K2 schema with H1–H3 and `ReachPure`; (2) independence and
  minimality of H; (3) the obligations of the K ledger and Level III at their own levels. For E15: S6 states the schema
  as "given H1–H3 and `ReachPure`, `K = Q3` iff A_miss", the two directions separately witnessed (§A.34), A_miss
  classified as introduced against the inventory (I3.165, I3.150/I3.153) and named in the scope section as the open
  bridge, not a premise at L. For E16: the answer forms as before. In both nodes a failing weaker alternative is named in
  its RESULTS row in those words; the C21 safeguard is kept (a failure of a (b)-instance is a failure of `Q3` only through
  `Q3`'s invariance under that operation; `K ≠ Q3` is not a failure of any particular (b)-instance).
- 2026-10-11T03:41Z — E15 brought under addendum 2. Draft S6: the scope section names A_miss as the open bridge; Q-SCHEMA is
  split into Q-SUFF (`pairCone_eq_Q3_of_drive`, built) and Q-NEC (a new §G: two intertwining lemmas, `Q3_aMiss`,
  `pairCone_eq_Q3_iff_drive`; not yet built, checkpoint `C0′` pending, [W] + [X] until measured); the hypothesis table
  adds I3.165 to A_miss's row; the earned reading, non-inference rule, licensed wording, controls (26 prints; a
  mutation that turns the equivalence into the implication), invariant table and predicted outputs follow. RESULTS:
  R-E15.1 and R-E15.3 amended (R-E15.3 now names the weaker alternative "the finite clause" and carries the C21
  safeguard), R-E15.4 added (the necessity direction, CONJECTURE [W] + [X]). LEDGER K2 note likewise. **Scheduling
  decision:** §G is E15 work (owner's priority 2); its design module will be built in this round's shared design
  dispatch together with E17's and E18's modules (one dispatch for the three, two left for repairs), not in a dispatch of
  its own. Probe `e16b_hybrid` (written with S0-b at 03:36Z, before addendum 2) is unaffected and not yet run.
- 2026-10-11T03:43Z — E16 probe a measured. `experiments/e16a_tokens_pair.py` run 1 (started 03:35:01Z, after commit
  `aca4fc91`; decision rule unchanged): 11/11, `COUNTER XG1/XG2/XS1/XS2 fails as stated`,
  `VERDICT E16A-CHART4-PAIR-LEVEL-SEPARATED`; replay byte-identical (py `b032f5c4…`, out `fa854faf…`). Every S0 prediction
  for the probe held: no native gate on any body of chart dimension 4 (relC alone; the three tokens and `eball 4` alike);
  product-form pair self-duality excludes Ω₄ and admits Ω⋆ and Ω_cs, whose `K_min` and `K_max` differ. NOTES-E16 §1 and
  S0-b (written 03:36Z: the hybrid body, its chart transport, predictions) and the exact probe
  `experiments/e16b_hybrid.py` (decision rule in its header, written 03:36Z) committed together, before that probe's
  first run. Pre-run review fixed one defect of the probe (an identity matrix bound by an assignment expression inside a
  short-circuited conjunction, which could leave it undefined); the decision rule was not changed.
- 2026-10-11T03:55Z — E16 probe b measured. `experiments/e16b_hybrid.py` run 1 (started 03:43:23Z, after commit
  `f540b32c`; decision rule unchanged): 7/7, `COUNTER XH1/XH2/XH3 fails as stated`,
  `VERDICT E16B-HYBRID-MEETS-PAIR-LEVEL-NOT-ELLIPSOID`, `exit 0`; replay byte-identical (`cmp` silent; py `6a53bad3…`,
  out `105c8f85…`). Every S0-b prediction held. NOTES-E16 §2 (the measurement), §3 (the general case G1–G5, written after
  the instances agreed) and §4 (outcome) written. Cross-branch read on the coordinator's instruction (addendum 1, rule 2;
  read-only): `research/archive/pt/I3/INVENTORY.md` at archive `4dc0321c` (sha256 `51eff9af…`, unchanged since the 03:29Z
  read), entries I3.8–I3.10, I3.43, I3.50, I3.57–I3.76, I3.88–I3.89, I3.92–I3.108, I3.148–I3.153, I3.165–I3.177, to
  classify the hypotheses of G2 and Ω_h's standing; one search also returned lines of the evidence snapshot
  `research/archive/pt/C5/evidence/sweep-20261010T1818Z/snapshot/I3/INVENTORY.md` (sha256 `d786a1f3…`), not relied on.
  Two corrections from that read, applied before the closing commit: (i) the body hypotheses are carried by TRB-1's
  theorems (I3.88–I3.89, proved [K]), and the inventory item that supplies the body is K∞-Stage (I3.167, open) — S0's
  (A2) said "TRB-1's body hypotheses, assumed"; §3 G2 and G5 cite I3.167 and record the change; (ii) the standing table of
  Ω_h gained rows for the token body (I3.167's formalized clauses), the elementary scope (I3.177, not formalized: Ω_h has
  four perfectly distinguishable states), K∞-Act and K∞-V4, and the negative answer names an elementary-scope predicate
  as the second assumption that would exclude Ω_h. Kernel lines checked at L for the rows: RelcSelectParity.lean:354,
  CompositeDimension.lean:218, :1160, :1380, :2723, :2888, KInfFoundations.lean:160, :264, :529, :632,
  TransitiveBody.lean:602. RESULTS R-E16.1–R-E16.5 and the LEDGER's round-4 K∞-Trans note written, each result in the
  form of rule 1, the weaker alternatives named in those words (the pair-level hypotheses without K∞-Geom; self-duality
  alone; central symmetry alone).
- 2026-10-11T03:55Z — **E16 closed.** Outcome (§A.31): NEW — the dichotomy "OI ⇒ (d = 3 ∧ Ω an ellipsoid) ∨ (d odd ∧
  d ≥ 5)" with every hypothesis of kind (i), so "OI + {chart dimension at most 4} ⇒ ellipsoid"; NEW in the kernel's
  vocabulary — the exact body Ω_h answers the decisive question negatively in odd chart dimension (missing assumption
  K∞-Geom, or an elementary-scope predicate); CONFIRMING [A] the body-independence of the relC count; ELABORATING HO-19 —
  product-form pair self-duality reduces to token self-duality. Residual OPEN (R-E16.5). Labels: CONJECTURE ×4, OPEN ×1;
  no status at L changes. Dispatches used this round: 0 of 3.
