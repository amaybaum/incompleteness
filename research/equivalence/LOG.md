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
- 2026-10-11T04:06Z — E17 begun (owner's priority 4). Search first (§A.19): R-E14.2 and NOTES-E14 §2 are the source; the
  stage-6 inventory has no item for H-DYN, Level III, `OISystem`, `LocalityPreserving` or `ReversibleDynamics` (search of
  `pt/I3/INVENTORY.md`, archive `4dc0321c`, sha256 `51eff9af…`; cross-branch read on the coordinator's instruction,
  addendum 1 rule 2). Read at L for the module: `QuasilocalSystem` (QuasilocalCharacterization.lean:168), `OISystem`
  (:463), `LocalityPreserving` (:475), `FiniteRange` (QuasilocalAlgebra.lean:919), `ReversibleDynamics` (:956), `hat`
  (:1040), `target` (:1054), `transported` (:1109). NOTES-E17 S0 (written 04:04Z: the objects, the finite-stage lemmas
  (a)–(c), the hypotheses classified, predictions) and the exact probe `experiments/e17_transport_finite.py` (decision
  rule in its header, written 04:05Z) committed together, before the probe's first run. Pre-run review simplified one
  expression of Z4 (a redundant conjunct); the decision rule was not changed.
- 2026-10-11T04:31Z — **coordinator addendum 3 received** (the owner's acceptance criteria; recorded before further
  research steps; nodes, order and budget unchanged). (1) S6's necessity direction proves the invariance reading only:
  A_miss in the module is cone-preserving admissibility (`K` invariant under `actT (rotLin t)` and `actT cycEquiv`);
  `Q3`'s invariance under every local unitary gives `Q3 ⇒ A_miss` in that reading and does not give operational
  availability of those operations through the kernel's protocols, which is the H-level premise (A)/H-OI_g, not in S6.
  The draft is to state "given H1–H3 and `ReachPure`, `K = Q3` iff A_miss, where A_miss is the invariance of `K` under
  the flow and `cycEquiv`", sufficiency witnessed by the schema and necessity by the invariance lemma; its scope section
  is to say that the equivalence is between cone-level statements, that availability is a separate H-level question
  not decided by S6, and that A_miss remains an introduced hypothesis, not a premise at L; the hypothesis table is to
  name "A_miss (invariance form, introduced)" and "(A)/H-OI_g (availability, H-level, not in S6)" separately. (2) Stage
  6 established `A_reached ⊭ (b)` for the 118 transferred pair-level rows; the 68 NOT REACHED rows have not been shown
  irrelevant, so no ledger entry may describe (b), A_miss or any pair-level hypothesis as "independent of OI";
  "independent of the transferred pair-level premises at L" is the admissible wording until B14/O11 decide the
  transfer question. The E15/E16 records and the ledger are brought under it next; the §G and E17 design modules
  (written, not yet dispatched) are unaffected in content.
- 2026-10-11T04:33Z — addendum 3 applied. Draft S6: the statement "given H1–H3 and `ReachPure`, `K = Q3` iff A_miss,
  where A_miss is the invariance of `K` under the flow and `cycEquiv`" (What the round is), Q-NEC, §G's paragraph, the
  scope section (cone-level equivalence; availability (A)/H-OI_g a separate H-level question not decided by S6; A_miss
  introduced, not a premise at L; (b) independent of the transferred pair-level premises at L, not shown independent of
  OI), the hypothesis table (rows "A_miss (invariance form, introduced)" and "(A)/H-OI_g (availability, H-level, not in
  S6)"), the earned reading, the non-inference rule, the unsourced-premises paragraph and the licensed ROADMAP wording.
  RESULTS R-E15.1, R-E15.4 and R-E16.3 and the LEDGER's round-4 K2 and K∞-Trans notes amended in place (rows of this
  round, unaudited). Two older surfaces carried the inadmissible wording and are corrected in place, old text recorded
  here: the LEDGER's K2 row, clause (c), "INDEPENDENT of every item at L (stage 6 [A])" → "independent of the
  transferred pair-level premises at L (stage 6 [A]: the 118 transferred rows; the 68 rows not reached not shown
  irrelevant)"; RESULTS R-E4.1, "independent of every item at L" → "independent of the transferred pair-level premises
  at L (the 68 rows not reached at stage 6 not shown irrelevant)". NOTES-E3 §4 (round 1, a node record) keeps its
  sentence "found independent of everything at L"; the corrected LEDGER and RESULTS rows are the reading. NOTES-E15 §4
  and NOTES-E16 §5 record the change. No measurement or label changed.
- 2026-10-11T04:33Z — E17 probe measured: `experiments/e17_transport_finite.py` run 1 (started 04:06:08Z, after commit
  `6ae7fd4f`; decision rule unchanged) 5/5, `COUNTER XZ1/XZ2/XZ3 fails as stated`,
  `VERDICT E17-TRANSPORT-FINITE-CONSISTENT`, `exit 0`; replay byte-identical (`cmp` silent; py `f1f8016f…`, out
  `cefedd2e…`). The two design modules written: `lean/EqvK2Converse.lean` (E15's §G; blob `4add9b8d`) and
  `lean/EqvTransport.lean` (E17; blob `0c7f92f8`); their reading rules and predictions written in NOTES-E15 §5 and
  NOTES-E17 §2 before the dispatch. A scratch exact check of §G's identity forms (session scratchpad, not committed; a
  design aid, not evidence) agreed. One name collision avoided: the kernel has `transport_apply` (SpectatorBridge.lean:353),
  so E17's lemma is `finiteStage_transport_apply`. E18 is deferred to the second dispatch (budget plan: dispatch 1 =
  §G + E17; dispatch 2 = repairs and E18; dispatch 3 = final repairs, any module still failing dropped).
- 2026-10-11T04:34Z — dispatch 1/3 (round 4): run **38112020014** (created 04:34:33Z, `workflow_dispatch` of `verify.yml`)
  on `2d978412` (branch `dev-equivalence/r4-design`, created by `git worktree add … -b dev-equivalence/r4-design 9f9f8257`,
  parent L; pushed 04:34Z). The diff from L is exactly `OIBridge/EqvK2Schema.lean` (blob `659ae36c`, unchanged from
  round 3), `OIBridge/EqvK2Converse.lean` (blob `4add9b8d`), `OIBridge/EqvTransport.lean` (blob `f48afc3c`) and the two
  import lines `import OIBridge.EqvK2Converse`, `import OIBridge.EqvTransport` after `import OIBridge.RelcSelectC5` in
  `OIBridge.lean` (the recorded deviation of earlier rounds: dev-branch writes under `verification/`). `EqvTransport`'s
  dispatched blob differs from the 04:33Z text of NOTES-E17 §2 (blob `0c7f92f8`) by one `first` fallback in the proof
  of `hsurj`, added at 04:34Z before the push; statements unchanged. The reading rules are those of NOTES-E15 §5 and
  NOTES-E17 §2.
- 2026-10-11T04:40Z — E18 begun (if budget; owner's priority 4) while dispatch 1 runs. Source: R-E13.1, NOTES-E13 §1.
  NOTES-E18 S0 (written 04:38Z: the polynomial form of the power cone, the witnesses, predictions) and the exact probe
  `experiments/e18_powercone.py` (decision rule in its header, written 04:40Z) committed together, before the probe's
  first run. Pre-run review simplified one detail string of XW2; the decision rule was not changed.
- 2026-10-11T04:49Z — dispatch 1 measured (run 38112020014; Mathlib bridge job 114389373318, 04:35:14Z–04:38:03Z; job log
  read through the GitHub MCP `get_job_logs`, the built-in `gh` refusing the log redirect): Build `failure` at
  `EqvTransport` only. `EqvK2Schema` 22/22 prints standard; `EqvK2Converse` built with warnings only and 9/9 prints
  standard; `EqvTransport` 4/9 standard (parse errors from the `Matrix`-scoped notation `ᴴ` not opened, lines 50, 153,
  195, 260; an untyped-lambda projection at 137:44). Release gate skipped; Lean kernel check job `success`. Readings by
  the rules: `EqvK2Converse` PARTIAL (Build step failed; module clean), `EqvTransport` PARTIAL. NOTES-E15 §6, NOTES-E17
  §3. Dispatched text kept as `lean/EqvTransport.run38112020014.lean` (blob `f48afc3c`); repair proof-only (blob
  `fadf980e`). E18: probe run 1 (started 04:38:20Z, after commit `8f3baf2e`) 5/5, `VERDICT E18-POWERCONE-SELFDUAL-EXACT`,
  replay byte-identical (py `402f9e88…`, out `aa53f144…`); module `lean/EqvPowerCone.lean` (blob `e7d7a286`) written;
  NOTES-E18 §1–§2 (reading rule and prediction before dispatch 2). LOG time correction: the E18 entry of this log (stamped
  04:40Z) and the probe header ("Written 2026-10-11T04:40Z") are later than the commit `8f3baf2e` (04:38:20Z) that holds
  them; both were written between 04:36:32Z and 04:38:20Z. The probe text is left as run (its replay identity depends on
  it). Dispatch 2 plan: `EqvK2Converse` byte-identical, `EqvTransport` repaired, `EqvPowerCone` first build.
- 2026-10-11T04:49Z — dispatch 2/3 (round 4): run **38112803530** (created 04:49:34Z, `workflow_dispatch` of `verify.yml`)
  on `20c207f1` (branch `dev-equivalence/r4-design`, fast-forward from `2d978412`; pushed 04:49Z). Diff from L:
  `EqvK2Schema` (blob `659ae36c`), `EqvK2Converse` (blob `4add9b8d`, unchanged from dispatch 1), `EqvTransport` (blob
  `fadf980e`, the repair), `EqvPowerCone` (blob `e7d7a286`, first build) and three import lines after
  `import OIBridge.RelcSelectC5`. Run 38112020014's remaining numerical-probe jobs were still running; the workflow
  has no concurrency group, so nothing is cancelled. One dispatch remains.
- 2026-10-11T04:55Z — final replay of the round-4 probes (04:53:52Z–04:54:07Z, `python3 -I -B`, outputs to the session
  scratchpad and compared with `cmp` against the recorded run-1 `.out`/`.err`): `e15_k2s6_probe` (py `78cd7c59…`, out
  `3ee625fe…`), `e16a_tokens_pair` (`b032f5c4…`, `fa854faf…`), `e16b_hybrid` (`6a53bad3…`, `105c8f85…`),
  `e17_transport_finite` (`f1f8016f…`, `cefedd2e…`), `e18_powercone` (`402f9e88…`, `aa53f144…`) — all five byte-identical,
  each rendering its verdict. `e8_cite_check` runs last, after the documents are final. Handoff proposals HP-11
  (coordinator), HP-12 (countermodels, cc bridge), HP-13 (bridge, origin) drafted; S6's §G surface and print count
  (31) updated to the built module; dispatch 2's Mathlib bridge job still queued (runners busy with run 1's probes).
- 2026-10-11T05:11Z — dispatch 2 measured (run 38112803530 on `20c207f1`; Mathlib bridge job 114391691368, 05:06:55Z–
  05:10:40Z; job log read through the GitHub MCP `get_job_logs`): **`Build completed successfully (3647 jobs)`**.
  Prints: `EqvK2Schema` 22/22, `EqvK2Converse` 9/9, `EqvTransport` 9/9, `EqvPowerCone` 7/7, all
  `[propext, Classical.choice, Quot.sound]`; warnings only (unused `simp` arguments, unreached `first` alternatives,
  deprecated `push_neg` and `Set.mem_setOf_eq`). Release gate red only at `lean-manuscript` (4 problems: the four
  unregistered design modules), by construction; `lean-axioms` 5907, no sorry; `legacy-records` 303 intact;
  `v3-receipts` 43 hold; `claims`, `duplicate` PASS. Lean kernel check job 114391691345 `success`. Readings by the rules
  fixed before the dispatches: `EqvK2Converse` BUILT (S6's `C0′` met), `EqvTransport` BUILT, `EqvPowerCone` BUILT. The
  `lean/` copies are byte-identical to the dispatched blobs. The third dispatch is not used. A dry run of the extended
  citation checker (output to the session scratchpad, not a recorded run) rendered `CITATIONS-RESOLVE` over 71
  citations at 04:56Z; the recorded run 5 comes last.
- 2026-10-11T05:15Z — `e39aaa68` pushed (05:14Z). Bare line references of the round-4 documents (a `:NNN` outside the
  checker's pattern, read against the file cited before it) checked at L by hand before run 5: draft S6's `cnot` (:775)
  after CompositeDimension.lean:97; `actT_reflY_phiW` (:106), `cnot_idW` (:110), `chain_value` (:134),
  `no_candidateCone_cnot_reflY` (:143) after K2Guard.lean:95; `cycEquiv` (:416) after KInfFoundations.lean:386; ROADMAP
  :1001–1006 (the K2 row) and the quotation of :1001–1003 — each line declares or reads as cited. NOTES-E17's
  `LocalityPreserving` (:475) after QuasilocalCharacterization.lean:168 resolves; its `OISystem` (:463) followed a
  citation of QuasilocalAlgebra.lean, whose line 463 is blank — the declaration is QuasilocalCharacterization.lean:463.
  Corrected in place to the full citation, which run 5 then checks; no other text changed.
- 2026-10-11T05:17Z — `experiments/e8_cite_check.py` run 5 (started 05:15:26Z, after commit `bc0820cf`; decision rule
  unchanged): 74 distinct citations (153 occurrences, 69 named pairs), countercontrols X1–X3 fail as stated,
  `VERDICT CITATIONS-RESOLVE`, `exit 0`; replay byte-identical (`cmp` silent; py `88847d31…`, out `e9168406…`). The 20
  citations new since run 4 are all additions (none of run 4's is lost); among them the design-module lines
  EqvK2Converse.lean:226, EqvTransport.lean:439, EqvPowerCone.lean:313 and EqvK2Schema.lean:297/:308, resolved by C1,
  the two names beside the last pair read by hand (`subset_Q3_of_pure_dual`, `Q3_subset_of_pure`); the `lean/` copies'
  blobs are those dispatched (`659ae36c`, `4add9b8d`, `fadf980e`, `e7d7a286`). Run 5 follows the final replay of the
  five round-4 probes (04:53–04:54Z); their scripts are unchanged since (sha256 rechecked at 05:16Z). RESULTS R-CITE.4.
- 2026-10-11T05:17Z — **Round 4 closed.** Nodes done, in the instructed order, under addenda 1–3:
  - **E15** — draft S6 (`K2-SCHEMA-1`, native V3 format, non-sealing; for owner review): given H1–H3 and `ReachPure`,
    `K = Q3` iff A_miss, A_miss the invariance of `K` under the flow and `cycEquiv`; sufficiency `pairCone_eq_Q3_of_drive`
    (built in round 3), necessity `Q3_aMiss` (§G, built in design run 38112803530; checkpoint `C0′` met); availability
    ((A)/H-OI_g) a separate H-level question not decided by S6; A_miss introduced, not a premise at L; countercontrol
    HO-24's cone recomputed exactly, the finite clause named as the weaker alternative that fails. POSITIVE (drafting),
    ELABORATING (an explicit non-invariance witness at `cos t = 3/5`).
  - **E16** — the owner's decisive question: positive below chart dimension 5 (OI ⇒ (d = 3 ∧ Ω an ellipsoid) ∨ (d odd
    ∧ d ≥ 5), every hypothesis an inventory item); negative in odd chart dimension through the hybrid token Ω_h (missing
    assumption K∞-Geom, or an elementary-scope predicate); self-duality alone and central symmetry alone named as
    failing weaker alternatives; residual OPEN. NEW ×2, CONFIRMING, ELABORATING.
  - **E17** — the transport form of H-DYN as a predicate on `QuasilocalSystem`, the kernel-form positive control and the
    finite-stage case built in design run 38112803530 (after a proof-only repair); `Passage` stated, not proved
    (R-E14.2's status). POSITIVE.
  - **E18** — the power cone of Ω⋆ equals its dual for the self-dualizing form, in polynomial form, built in the same
    run on its first dispatch. POSITIVE.
  Rows added: R-E15.1–R-E15.4, R-E16.1–R-E16.5, R-E17.1–R-E17.2, R-E18.1 (OPEN ×2, CONDITIONAL ×1, CONJECTURE ×9, of
  which four on design-run evidence [D]) and R-CITE.4; no label of an earlier round changed and no status at L changed.
  LEDGER round-4 notes: K2 (two), K∞-Trans (two), L3-conv. Handoff proposals HP-11 (coordinator), HP-12 (countermodels,
  cc bridge), HP-13 (bridge, origin). Dispatches used: 2 of 3 — 38112020014 (`dev-equivalence/r4-design` `2d978412`;
  Mathlib bridge job 114389373318; Build failure at `EqvTransport` only, `EqvK2Converse` 9/9 standard; readings PARTIAL
  by the rules) and 38112803530 (`20c207f1`; job 114391691368; Build success, 3647 jobs; `EqvK2Schema` 22/22,
  `EqvK2Converse` 9/9, `EqvTransport` 9/9, `EqvPowerCone` 7/7, all `[propext, Classical.choice, Quot.sound]`; gate red
  only at `lean-manuscript`, `lean-axioms` 5907); the third unused; no job or run cancelled. Cross-branch reads, all
  read-only and recorded above with their sha256: `research/overview` @ `742c6b2f` (nine handoffs copied to `inbox/`;
  HO-18 v1, HO-19 v1 and the handoffs README read, not copied); `research/archive` @ `4dc0321c` (the stage-6 inventory
  files under addendum 1 rule 2, `pt/I3/INVENTORY.md` at 03:29Z, 03:55Z and 04:06Z); one search's incidental lines of
  the C5 evidence snapshot (`d786a1f3…`), not relied on. Deviations, all recorded above: dev-branch writes under
  `verification/` (four design modules and three import lines in `OIBridge.lean` on `dev-equivalence/r4-design`;
  nothing under `verification/` on this branch); in-place amendments of this round's unaudited rows, notes and draft
  under addenda 1–3, and of two older surfaces under addendum 3 (the LEDGER's K2 row, clause (c); R-E4.1), old text in
  the 04:33Z entry; NOTES-E16's body-hypothesis classification corrected before its closing commit (K∞-Stage I3.167 in
  place of TRB-1's proved I3.88–I3.89); dispatch 1's `EqvTransport` blob differing from NOTES-E17 §2's text by one
  `first` fallback (statements unchanged); `EqvK2Converse` read PARTIAL in dispatch 1 by the rule's letter (the module
  clean, the Build step failed on another module); E18's module departing from S0's plan in two proof devices (NOTES-E18
  §2); two LOG time corrections (the E15 entry; the E18 entry and its probe header, the probe text left as run); a
  scratch exact check of §G's identity forms and a dry run of the citation checker (session scratchpad, not committed,
  not evidence); NOTES-E17's `OISystem` reference made a full citation before run 5; no local Lean toolchain, so every
  module was elaborated only in the design dispatches. Final replay: the five round-4 probes byte-identical
  (04:53–04:54Z), then `e8_cite_check` last (run 5, replay identical). No preregistration became a round; nothing was
  merged and no pull request opened; `main` and the other threads' branches untouched; nothing outside
  `research/equivalence/` changed on this branch.

## Round 5

- 2026-10-11T07:20Z — round 5 opened at thread head `ab6788b9` (verified: `git rev-parse HEAD` =
  `git rev-parse origin/research/equivalence` = `ab6788b9fbe07cb227a611c81b3998e9921293b8` after
  `git fetch origin research/equivalence`; `git status` clean). Re-read the charter, LOG, LEDGER, RESULTS,
  NOTES-E15 … E18, draft S6, HP-11 … HP-13 and the modules `lean/EqvK2Schema.lean`, `EqvK2Converse.lean`,
  `EqvTransport.lean`, `EqvPowerCone.lean`. Conventions unchanged (S0 before the first run with `date -u` readings;
  decision rules in script headers; failed runs kept as `.run1.*`; byte-identical replays before commit; dev branches
  `dev-equivalence/<topic>` cut from L `9f9f8257` with one commit carrying the modules and the import lines in
  `verification/lean-mathlib/OIBridge.lean`; `verify.yml` by `workflow_dispatch` through `gh api`; job logs through the
  GitHub MCP `get_job_logs`). Budget: at most three `workflow_dispatch` runs; no cancellation; no pull request.
- 2026-10-11T07:21Z — **receipt of HO-27 v1, HO-30 v1, HO-31 v1, HO-32 v1, HO-33 v1, HO-34 v1, HO-35 v1, HO-36 v1**
  (`research/HANDOFFS/` at `origin/research/overview` = `4c4a02b18ab80819694312a7526dd360c2dfea38`, fetched; the
  directory listed with `git ls-tree`), each copied byte-identically to `inbox/` by `git show 4c4a02b1:<path>` with the
  git blob of the copy checked equal to the source blob: HO-27 blob `a817d94a`, sha256
  `196fdad5e8917ef04ce6f229ab7405636d93b9fd98c41688245a0bd48cf9c2a4`; HO-30 `15bd19b7`,
  `b9d380753e40f29d9fccd13290ca430b9b2c7b02f3191edad943ac93da4d5f38`; HO-31 `a5f86ba5`,
  `27263a957e2e50e5aaca8499f5355cf387fb30943c74226259fd5c52522feef8`; HO-32 `a5a6694b`,
  `06a0ac6b463a41b62647d1b1aaf11263758fda7390516a53484abd5a98a2a0a9`; HO-33 `06eee1d8`,
  `d5f9d19eafa2fdf39877fa701961bb1c95ae5cfde5bbfd13ace7a0ce08a21169`; HO-34 `46870ef4`,
  `0a39ea8227e51cae331a4d3b9de62ba12f168b14e46993e4690eae42f94d1e6f`; HO-35 `5b5ea61f`,
  `70d57d852f8f8f7e3500c464faeefffc0b64f62d795eefc48308c5ec3f2dee53`; HO-36 `f9c74e69`,
  `8b8a3bf52b6a834825e592cdfd75c3c40fbdd7cdbcf8a4fb566901b4fd536cd2`. **Read, not copied** (authorized read-only
  cross-branch reads of `research/overview` @ `4c4a02b1`, extracted to the session scratchpad): the coordinator's audit
  `research/AUDITS/2026-10-11-round4/AUDIT-EQUIVALENCE-R4.md` (blob `ec94ee8a`, sha256
  `f4b3487416508490a1d8a9cc6f86ea1d0fc98cbc26312e9e9c2da09f0637bec4`); this thread's own handoffs as issued, for their
  item numbering: HO-18 v2 (blob `ebd9e287`, sha256 `9aeac715ae694e44fcfa11789890b6644470995d29c9d352700adfe301c131ba`),
  HO-28 v1 (`841749d4`, `608aca2ecef2e59281ede77ceeb6d387a0fbed39aa3d11df9b6e5fcd5a6a7034`), HO-29 v1 (`d3cf4e4d`,
  `5526735ff8f833a8b503e553889366942c7ffdaacb701b7610569e4ccad65aa0`). **Deviation (over-broad extraction):** the
  extraction loop also wrote `research/HANDOFFS/README.md`, `research/AUDITS/2026-10-11-round4/README.md`,
  `…/equivalence/REPLAY-LOG.txt` and `…/CI-RUNS-R4.md` to the scratchpad; they were not authorized for this round and
  were deleted without being read (the loop printed their sha256; nothing of their content was seen or is relied on).
  **Reliance, stated before use** (only at the labels the handoffs carry; nothing in them is CERTIFIED except kernel
  declarations named at L; every "may not assume" clause is honoured as stated under each item):
  - **HO-27 v1 (origin; items 4–7 addressed here).** Item 4 (at level one the angle condition of
    `denseUnitaryControl_of_fixedGate` is `¬RotClifford α`; CONDITIONAL [D] + inputs), item 5 (scope: level one;
    `DenseUnitaryControl` under `¬RotClifford α` at every level OPEN), item 6 (the re-preparation law is an operation
    datum; CONDITIONAL [W] + [K] + [X]) and item 7 (HO-17 item 7's scope sentence sharpened) are **recorded and not
    relied on**: no round-5 node uses the angle hypothesis, a fixed-gate theory or a re-preparation law. Item 2
    (independence of the stage-crossing datum: OPEN at (L-O)) is recorded as the exact location of the open transfer
    lemma; item 1 (N11) and item 3 (ORD∞ as coherence) are context for availability and are not cone statements.
    Honoured: no availability is inferred from cone invariance anywhere (E19 and E22 state every invariance as a
    property of a cone; S6's scope section keeps availability as the H-level premise (A)/H-OI_g, not in S6); nothing
    is taken as kernel status, as independence of OI, or as exactness at any angle.
  - **HO-30 v1 (countermodels).** Item 1 — Theorem S′ in finite form as the design-built `CmSprime.theorem_Sprime_ineq`
    (hypotheses: unit seeds, `c_k ∈ (1, 2]`, `c_k < card n`, pairwise nonnegative trace pairings, the inequality form of
    (CC) on every positively paired pair; 78/78 prints standard in run 38112813276; CONJECTURE [D]) — is **relied on in
    E19 (i)** for H3 of the countercontrol cones `K384` (S6's `K*`) and `K768`, **at [D] and only after this thread's own
    exact check of each hypothesis** (as the coordinator's X2/X3 did; the check is the node's probe). Item 2 (the
    evidence update of the explicit cones; the circle cones and `Kk` stay on S′ [W] for compact defect sets) is relied
    on as the label of `Kk` in S6's countercontrol family. Item 3 (the first dispatch's failure) is context. Honoured:
    nothing CERTIFIED; S′ not used for compact defect sets; (CC) used as sufficient only; H1 checked separately by the
    probe (Schmidt bound); no OI content attributed to S′.
  - **HO-31 v1 (countermodels; items 1–3 addressed here).** Item 1 — Theorem C19-1 (the block-diagonal
    `{P₀ ⊗ U₀ + P₁ ⊗ U₁}` carries every pure state to a product (a); with H1 and H3 it forces `Q3` (b); CONDITIONAL
    [W] + [K] + [X]) — is **the source statement of E19 (ii)**: the node restates (a) and (b) in the schema's
    vocabulary and proves them in its own design module; HO-31's text is cited as the source, its label unchanged.
    Item 2 — the `G₇₆₈` cone (seed `h*`, `c = 10001/10000`, 384 rays, no product, overlaps in `[1/1024, 13/16]`;
    CONDITIONAL on S′ [D] and HO-22 item 3 [W]) — is **relied on as the second countercontrol of S6 after the node's
    own exact recomputation** of every exact item (the group, the orbit, the overlaps, H1, (CC)). Item 3 (case B and
    S2 with G16: three routes closed; OPEN) and item 4 (survivor patterns; OPEN) are context. Honoured: nothing
    CERTIFIED; every statement read as cone invariance, never availability; HO-22 item 3's identification of the
    closure is **not** relied on — E19 states the group generated by `cnot`, the flow and `cycEquiv` by its own exact
    algebra (the determinant-ratio invariant and the two-reflection construction) and cites HO-22 item 3 only as a
    comparator; no claim about balanced rank-two surgeries, case B, S2 with G16 or `K_circ`.
  - **HO-32 v1 (countermodels).** Items 1–5 (the four explicit cones `K384`, `KC`, `Kk`, `K768` against Table A2:
    118 SATISFIES / 13 FAILS / 68 NOT REACHED each; the three kinds of premises; the operations by which each fails;
    the exact list of refuted implications; uniform FCC failing by one mechanism; CONDITIONAL at the labels stated) are
    **relied on in E19 (i)** as the documentation of the countercontrol family placed into S6's controls, each cone
    at its own label (H3 of `K384`, `KC`, `K768` on `theorem_Sprime_ineq` [D] per HO-30; `Kk` on S′ compact form [W]);
    item 4's reading — the finite clause and the Clifford group are refuted as sufficient invariances with H1–H3, and
    no cone of the record refutes the full-flow form — is the reading S6 records. The assumption-watch marker (which
    operation moves a cone depends on the cone) is recorded in the LEDGER. Honoured: no availability; no cone
    "satisfies OI" or is "independent of OI"; nothing about the 68 NOT REACHED rows beyond R6's record; `pauliW` and
    `twistQ3` not examined; no level-(ii) versions; no invariance under a continuous family other than `Kk`'s;
    `Kk` and the FCC mechanism not re-derived by the coordinator and not re-derived here.
  - **HO-33 v1 (bridge; items 5–6 addressed here).** Item 5 (availability implies invariance, not conversely:
    `transferClause_Q3` [D] while `zPh` is unavailable, `lattice_refutes` [D]; CONJECTURE) is **relied on as a
    constraint on S6's premises** — invariance premises do not supply availability — and is written into S6's scope
    section at its label. Item 6's reading markers (an availability statement *yields* (b), it is not (b);
    `TransferClause` is an invariance clause; a full model for the independence of (b) is OPEN) are recorded and
    followed in every round-5 text. Items 1–4 (the full model FM; the verdict with its scope; what supplies the
    operations; K∞-Drive's two readings) are context. Honoured: no certification; "independent of OI" never written
    without item 2's scope (and not written at all in this thread's own claims); nothing about (b) from FM; FM's pair
    cone not described as generated by its operations.
  - **HO-34 v1 (bridge).** Item 1 (one dictionary: `pauli`, `tokMat`, `dict` of `BridgeDictionary` and `EqvK2Schema`
    converge by `rfl` in `BridgeConverge`; CONJECTURE [D] run 38117986499) and item 2 (the transfer clause in table
    form, `transferClause_iff`, both directions, and `transferClause_mono`; CONJECTURE [D]) are **relied on in E22**:
    the two modules are to be carried verbatim with attribution onto this thread's dev branch (authorized read of
    `research/bridge` @ `a34d20b5`), and S6's (b)-instances are to be stated through `transferClause_iff`. Item 3 ((b)
    for the phase circle in table form; CONDITIONAL on the clause) is a comparator for `dict_actT_rotLin`. Item 4 (two
    weaker clauses defeated: the clause for the stated access, FAILED; a finite group, FAILED CONDITIONAL on claim
    (D)) is recorded in S6's controls as further failing weaker alternatives at those labels. Honoured: no
    certification; no sourcing of the transfer clause (every statement has it as a hypothesis); no availability.
  - **HO-35 v1 (bridge).** Items 1–3 (the curve-cover theorem `reachUnitary_of_curveCover` [D]; identity components of
    dimension at most one through Cartan, CONDITIONAL [L] + [W]; "a group" of that kind FAILED as a sufficient bridge,
    CONDITIONAL on claim (D), with the block-diagonal `SU(2) × SU(2)` as the countercontrol) are **relied on as
    context for E19 (ii)**: the reachability side of the schema fails for every closed subgroup whose identity
    component has dimension at most one, and the block group of C19-1 has dimension six, consistent with item 3's
    countercontrol; recorded in S6's controls at those labels. Honoured: no certification; B7-1 not used for identity
    components of dimension two or more; the Cartan link not treated as formalized.
  - **HO-36 v1 (bridge).** Items 1–2 (HO-24's cone is invariant under B10-5's stages `G_1`, `G_2` and under no `G_n`
    with `n ≥ 3`, every one of its 192 defects certified out of `K` at `n = 3` by the phase `e^{iπ/4}`; "a finite stage"
    FAILED as a sufficient bridge, CONDITIONAL on HO-24 items 4 and 6 and on claim (D)) are **relied on as context for
    S6's countercontrol** — a second explicit non-invariance witness for `K*` (at the phase `π/4`) beside this thread's
    witness at `cos t = 3/5` — and recorded in S6's controls at those labels. Honoured: `K`'s exoticness and
    self-duality taken only at HO-24 item 4's label (now HO-30's [D] finite form after the hypothesis check); nothing
    about a tower-invariant cone except through B10-4 and claim (D); no kernel check assumed.
  - **HO-18 v2, HO-28 v1, HO-29 v1 (this thread's own, read as issued, not copied).** HO-18 v2 corrects item 2 as
    HP-11 item 1 requested; every statement is as meant. The receipt asks a thread that relied on v1's item 2 to say
    which of its steps read the lemmas with the products as hypothesis: **none** — this thread's modules state LOWER
    and UPPER with every pure state as hypothesis (EqvK2Schema.lean:297, :308), and no note, row or draft of this
    thread read them otherwise. HO-28 (items 1–5) carries R-E16.1–R-E16.5 with the coordinator's precision that the
    count is necessary, not sufficient (its X2: `diag(−1, 1, −1)` and `diag(−1, −1, 1)` meet the count and fail `relC`
    with `Ad(CNOT)`); that precision is carried into E20's S0. HO-29 (items 1–3) carries R-E15.4 and the admissible
    wording; nothing to correct.
  - **The round-4 audit (`AUDIT-EQUIVALENCE-R4.md`).** No label changes; every row accepted; the deviations
    accepted; X2's precision (above) and the rule it motivates — a chain of kernel theorems applied to a model names
    the side hypotheses of every link and shows the model satisfies them, otherwise it is a written argument [W] — are
    applied to every round-5 use of a kernel theorem on a model (E19's cones, E20's bodies, E21's stages).
  No research step of round 5 precedes this receipt's commit.
- 2026-10-11T07:30Z — **authorized cross-branch reads** (read-only; each extracted to the session scratchpad by
  `git show <commit>:<path>` after `git fetch`, the commit checked to be the one named by the instruction, the git
  blob and sha256 recorded): `research/countermodels` @ `644bf0a15f0553ca9d5181363fe328a430a60184` —
  `research/countermodels/lean/CmSprime.lean` (blob `eb5e109a`, sha256
  `a10f47907c797da9fa5e40ece08b7606e122bad7deccf7c68b1e76863a9de434`, read: the definitions `pr`, `defect`, `dualH`,
  `surgery`, the statements of `selfDual_of_local`, `theorem_Sprime`, `cap_subset_cocap`, `theorem_Sprime_ineq`,
  `theorem_Sprime_C4`, `twoDefect`, `control_single_defect`), `NOTES-C19.md` (`6c51b8a0`,
  `bfdfd94a1a6707932fdf50e0658c0ba95844228e97453a3f2ea668b8f6958d92`, whole), `NOTES-C21.md` (`a2f46be3`,
  `f0d72871ae25493023a1afc4026f42544702bc097e83c1e103c2c59f934e8adc`, lines 1–120: the cones' table, the reading of
  the columns, S0), `experiments/c19_groups.py` (`0519f74d`,
  `4517e4d2b79236fedc79748f454cff0860b836b41f173545b8d678f71d6e99db`, whole — the seed `h_C` and the orbit survey),
  `experiments/c21_rows.py` (`3c777416`, `c4621d1e20d9ddaad07cd7d2a134ad19d385352682aa598bf1782b2632ee1fb4`,
  extracted, not read: NOTES-C21's table supplied what E19 needs); `research/bridge` @
  `a34d20b58d1f937c4705bfa4e24d3c1ecae793c4` — `research/bridge/lean/BridgeDictionary.lean` (blob `fece97f4`, sha256
  `48fc4a7e5b1f27d433ffb38cfd89f69a74544a803605465b2d0bd8b7a932156d`, whole) and `lean/BridgeConverge.lean`
  (`d09c7050`, `3f7155ca28787b56b130ec6573e97fa49d30f5f732f9dd5157242d463af8b829`, whole), for E22 (to be carried
  verbatim with attribution onto the dev branch). Nothing else on either branch was read. Kernel read at L in this
  branch's tree: CompositeDimension.lean:93–232 (`HVec`, `W`, `hom`, `homMap`, `prodState`, `maxCone`, `actT`,
  `actC`, `IsNot`, `NativeGate`, `Entangling`), :770–863 (`cnot`, `nflip`, `cnot_frame`, `cnot_relT`, `cnot_relC`),
  :2700–2756 (the selector and its block reduction), :274, :297, :682 (the eigenspace counts); KInfFoundations.lean:
  135–161, 260–291, 345–475; QuasilocalCharacterization.lean:150–209, 440–510; QuasilocalAlgebra.lean:900–975,
  1030–1130; TransitiveBody.lean:518–520; ImplementationLocality.lean:244; StructuralClosure.lean:180;
  SubstratumInterfaceAudit.lean:236; SubstratumInterface.lean:75. Mathlib API names checked against the local
  checkout `/home/user/leanprover-community/mathlib4` at `db584cd6` (the `v4.33.0` pin). The GitHub API (`gh api`)
  was used read-only: the workflow id of `verify.yml` (342319289) and the run queue (empty at 07:36Z).
- 2026-10-11T07:41Z — E19 begun. NOTES-E19 S0 (written 07:41Z: the productivity test, the analysis (A1)–(A5) — the
  hypotheses of `theorem_Sprime_ineq` and their reduction for a common `c`; the orbit reduction; the group the clause
  generates, decided by the determinant-ratio invariant; C19-1 in the schema's vocabulary with the block module's
  statements; the predicted answer to (ii) — and the predictions) and the exact probe
  `experiments/e19_s6_controls.py` (decision rule in its header, written 07:41Z) committed together, before the
  probe's first run.
- 2026-10-11T07:48Z — `experiments/e19_s6_controls.py` run 1 (started 07:47:46Z, after commit `ad029d38`): 7/8, K4
  FAIL on one item of the check: the harness multiplied the diagonal factor `(1 ⊗ U_J)` on the left of the two
  reflections, which gives the block pair `(U_J, U_J R)`, and compared it with the expected `(U_J, R U_J)` — an error
  in the expected order (NOTES-E19 (A3)'s construction is `(1, W)(U, U) = (U, W U)`, the reflections first), not in
  the mathematics; every other item of K4 and every other check passed (D1, K1, K2, K3, K5, K6, K7; XK1–XK4 failing as
  stated). Kept as `e19_s6_controls.run1.{py,out,err}` (exit 1, `VERDICT NOT RENDERED`). Run 2 corrects the order of
  the word in the K4 code and in the header's description of that item (the decision rule is unchanged: K4 must
  PASS, eight checks, four countercontrols); a bracketed note in the header records the run-1 error.
- 2026-10-11T07:55Z — **coordinator message received (the owner's round-5 directions, binding from now; recorded in
  `research/overview` OVERVIEW.md, "Owner's round-5 directions"), acknowledged before any dispatch.** Quoted: "Priority
  order across threads: origin and bridge first (they can change the foundational conclusion); your thread and
  countermodels establish the boundaries of what can legitimately be claimed. Requirement, in the owner's words:
  determine whether ReachPure GENUINELY follows from the revised S6 forcing group, or whether the forcing conditions
  already contain the desired conclusion. For E19 (ii) this means an explicit chain with every step's premise
  classified, and a circularity check: (a) state the hypothesis exactly — invariance of K under which group? the
  clause's two operations (the flow rotLin t for all t, and cycEquiv on one token: A_miss as stated) or the closure of
  the group they generate (the block-diagonal SU(2) × SU(2) of Theorem C19-1, by HO-22 item 3, which is [W] — if you
  use the closure, the passage 'invariant under the generators ⇒ invariant under the closure' needs K closed (H3) and
  the closure identification; name both, and HO-22 item 3's label); (b) C19-1 (a) gives, for that group, that every
  pure state is carried to a product — state whether this is ReachPure in your schema's exact form (which pure states,
  which products, which group action on the pair) or a stronger or weaker statement, and prove the equality or the
  gap; (c) then say which of your hypotheses carried the conclusion: if 'invariance under the continuous
  block-diagonal group' is taken as the hypothesis, decide whether that hypothesis is itself (b)/A_miss restated (it
  is cone invariance under a group containing the clause's operations — an instance of the invariance premise, not of
  QM), or whether it smuggles the conclusion (e.g. by containing a reachability or transitivity statement, or by
  presupposing a representation on ℂ² ⊗ ℂ² that is Q3's own); the test: exhibit a non-Q3 object satisfying every
  hypothesis except the one under examination, or prove none exists — the explicit cones of HO-24/HO-31/HO-32 are the
  tools (each is invariant under a finite group and fails under the continuous half: use them to show which hypothesis
  does the work); (d) record the outcome as one of: ReachPure DERIVED from A_miss + H3 + the closure identification
  (then S6 drops it as a separate hypothesis and the draft's premise list shrinks, with HO-22 item 3's [W] label
  carried), or ReachPure NOT derived (the forcing conditions contain it — say which clause), or OPEN at a named lemma.
  Keep necessity (Q3_aMiss, invariance only) and sufficiency as separate preregistered questions (§A.34), and never let
  an invariance hypothesis stand in for availability. Safeguard shared with the other threads: finite-order generators
  can generate continuous control by composition (Hadamard and T); when a hypothesis says 'invariant under the group
  generated by …', name the generated group and its closure exactly, and treat the closure step as a premise (K closed,
  H3) rather than as automatic. Everything else in your round-5 instructions stands (receipts first, ≤3 dispatches, no
  CI cancellation, S0 before runs, hypotheses classified, readings named, the F1 side-hypothesis rule)." Applied: a
  section S0-b of NOTES-E19 (the explicit chain, every step's premise classified; the circularity check (a)–(d)) is
  written now, before the probe's second run, before the module is written and before any dispatch; its load-bearing
  tests of (c) get their own exact probe `experiments/e19b_block_controls.py` with its own decision rule; the module's
  hypothesis is stated for the group named in (a); the draft's two directions stay separate questions; no invariance
  statement is read as availability.
- 2026-10-11T08:02Z — **second coordinator message received (a further owner distinction, binding for E19; recorded in
  OVERVIEW.md under "Owner's round-5 directions"), acknowledged before the probes' next runs and before any
  dispatch.** Quoted: "Dense control versus exact invariance. K2 requires EXACT invariance of the pair cone.
  closure(⟨G_1, …, G_n⟩) = SU(2) × SU(2) (or the block-diagonal group of Theorem C19-1) does not mean every element is
  exactly reachable by finite compositions of the clause's two operations; so when E19 passes from 'K invariant under
  rotLin t for all t and cycEquiv' to 'K invariant under the continuous block-diagonal group', establish the
  topological closure and continuity properties first and label them as premises: (i) K is closed (H3 — say exactly
  which of your hypotheses gives closedness, and whether self-duality alone does); (ii) the action of a unitary on
  tables is continuous (the map U ↦ coordOf(Ad(1 ⊗ U) dict ω) — state it; prove it in design if small); (iii) the
  identification of the closure of the generated group with the block-diagonal group is HO-22 item 3 [W] — carry its
  label; (iv) then the lemma 'a closed cone invariant under a dense subgroup is invariant under its closure' (exact
  statement, proved or cited). Only after these does C19-1 (a) give ReachPure. Record which of (i)–(iv) is an
  inventory item, which is one of S6's existing hypotheses (H3), and which is introduced; if any is introduced,
  ReachPure is not 'derived' but 'derived modulo that premise', and the draft's premise list says so. Keep necessity
  and sufficiency as separate preregistered questions. Also, for the circularity test: exhibit a cone invariant under
  the finitely generated group of the two operations' finite-order parts (your countercontrol family: G₃₈₄, G₇₆₈, C₂
  cones) and show precisely at which of (i)–(iv) they fail, so the record says which hypothesis carries the
  conclusion." Applied in NOTES-E19 S0-c (written now, before the probes' runs): the two forms are kept apart — in the
  **full-flow** form (A_miss as S6 states it, the flow at every real angle) every element of the block group is an
  exact finite word in the clause's operations (Euler angles [L]; exact instance B6 added to probe `e19b` before its
  first run), so the passage uses no closure, no continuity and no closedness, and (i)–(iv) are not premises of it;
  in the **dense-control** form (the two-rotation clause, one irrational angle) (i)–(iv) are exactly the premises,
  each classified in S0-c, with (iii) at HO-22 item 3's [W] label, (i) a consequence of S6's H3 (self-duality alone
  gives closedness; `K ⊆ dualW K` alone does not), (ii) and (iv) theorems to be proved in design in the E22 module
  (`continuous_transferMap`, `invariant_of_closure`, `isClosed_of_selfDual`), and the density of the one rotation's
  powers the introduced premise — so in that form `ReachPure` is derived **modulo** (iii) and the density premise, and
  the draft's premise list says so. The finite-order-part cones (`K384`, `K768`, `KC`) are closed, the action is
  continuous and (iv) holds for them vacuously; they fail at (iii): the group their generators generate is finite,
  equal to its own closure and not `H` — probe `e19b` B7 (added before run 1, with the decision rule's count raised
  from five to seven checks; no run of `e19b` preceded the amendment).
- 2026-10-11T08:13Z — `experiments/e19_s6_controls.py` run 2 (started 08:13:24Z; the word order corrected, decision
  rule unchanged): 8/8, `COUNTER XK1/XK2/XK3/XK4 fails as stated`, `VERDICT E19-S6-CONTROLS-EXACT`, `exit 0`, 25 s;
  replay byte-identical (`cmp` silent; py `80787ca1…`, out `ecaddd86…`). Every S0 prediction held, K3's `s_max`
  (not predicted) measured `1560203344561/1566477528100`. `experiments/e19b_block_controls.py` run 1 (08:13:49Z)
  stopped on its own guard before any check (a non-Pythagorean instance in the harness; kept as `.run1.*`); run 2
  (08:16:18Z; the instance replaced): 5/7, B3 and B7 failing on wrong-angle expectations — the matrix `D =
  diag((3 − 4i)/5, (3 + 4i)/5)` is the special-unitary form of the rotation by `2θ₀`, not `θ₀` (kept as `.run2.*`,
  the error recorded in the header); run 3 (08:17:53Z; the object relabelled, the two expectations replaced by the
  bound `< 1/c` and the `2θ₀` coordinates, the decision rule unchanged): 7/7, `COUNTER XB1/XB2/XB3 fails as stated`,
  `VERDICT E19B-BLOCK-CONTROLS-EXACT`, `exit 0`; replay byte-identical (py `92e6a5b3…`, out `b6f90dd7…`). NOTES-E19 §1.
- 2026-10-11T08:18Z — the design modules `lean/EqvK2Block.lean` (E19 §H) and `lean/EqvOneDictionary.lean` (E22; S0-c's
  (i), (ii), (iv)) written; no local Lean toolchain, every API name checked against the Mathlib checkout at the pin
  (`star_inv₀`, `Complex.cpow_nat_inv_pow`, `Continuous.matrix_mul/_elem/_conjTranspose/_trace`, `isClosed_biInter`,
  `closure_minimal`, `unitary.star_mem`, `Matrix.det_conjTranspose`, `Matrix.mul_vecMulVec`, `Matrix.vecMulVec_mul`,
  `Matrix.star_mulVec`); their reading rule and predictions in NOTES-E19 §2, written before the dispatch. Dev branch
  `dev-equivalence/r5-design` created by `git worktree add … -b dev-equivalence/r5-design 9f9f8257` (worktree
  `/home/user/wt-research/dev-equivalence-r5-design`), one commit `7dd71a7eacf029374a785d3bac51a9eb51bef4cb`
  (08:18:49Z, not yet pushed): `OIBridge/EqvK2Schema.lean` (blob `659ae36c`), `EqvK2Converse.lean` (`4add9b8d`),
  `BridgeDictionary.lean` (`fece97f4`) and `BridgeConverge.lean` (`d09c7050`) — the last two carried verbatim from
  `research/bridge` @ `a34d20b5` with attribution in the commit message — `EqvK2Block.lean` (`d339c6c5`),
  `EqvOneDictionary.lean` (`00ac3707`), and six import lines after `import OIBridge.RelcSelectC5` in `OIBridge.lean`
  (the recorded deviation of every round: dev-branch writes under `verification/`; nothing under `verification/` on
  this branch).
- 2026-10-11T10:16Z — **interruption and resumption (process change 1 of 2, logged once).** The session stopped at
  about 08:34Z on an API usage limit; a container restart followed; work resumed at 10:06Z from this thread's own
  transcript, under the coordinator's message of 10:05Z, which recorded the state. Verified at 10:07:30Z (`date -u`):
  HEAD `3715857c` = `origin/research/equivalence`; uncommitted, both my own writes and matching my last actions
  before the stop — `NOTES-E20.md` (sha256 `96e95bc5…`, mtime 08:26:43Z: E20's S0, written 08:27Z) and
  `experiments/e20_odd_bodies.py` (`5743149f…`, mtime 08:30:53Z: the probe, written after S0, never run); nothing
  else changed in the worktree; the dev worktree `dev-equivalence-r5-design` clean at `7dd71a7e` =
  `origin/dev-equivalence/r5-design`. Not logged before the stop: dispatch 1 (entry below, recorded now from the
  host's run record and job log). Dispatches used: 1 of 3.
- 2026-10-11T10:16Z — **commit trailers (process change 2 of 2, logged once).** From this entry on every commit
  message of this thread ends with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` followed by
  `Claude-Session: https://claude.ai/code/session_01XEQMD5kRhaU9WyeZt6dmM1` (the session's attribution changed);
  earlier commits keep their trailers and are not rewritten.
- 2026-10-11T08:20Z (recorded 10:16Z) — **dispatch 1 of 3.** `workflow_dispatch` of `verify.yml` (via `gh api`) on
  `dev-equivalence/r5-design`, pushed at 08:20Z with head `7dd71a7eacf029374a785d3bac51a9eb51bef4cb`: run
  `38124464622`, created 08:20:37Z, completed 08:56:31Z, conclusion `failure`. Mathlib bridge job `114425828153`
  (08:33:16Z–08:36:07Z): **Build failure**, Release gate **skipped** — so no `lean-axioms` reading and no gate reading
  exist for this run; every other job green (Lean kernel check and the numerical probes). Log read at 10:09Z with
  the GitHub MCP job-log tool, tail capped at 5000 of 38272 lines (the six modules' build lines all lie within the
  tail; the earlier 33272 lines, the build of modules this branch did not change, were not retrieved), saved in the
  scratchpad (sha256 `27c29eca…`). Build lines: `⚠ [3642/3649] Built OIBridge.EqvK2Schema` (22 prints, all
  `[propext, Classical.choice, Quot.sound]`), `⚠ [3643/3649] Built OIBridge.EqvK2Converse` (9, standard),
  `⚠ [3644/3649] Built OIBridge.BridgeDictionary` (20, standard), `✖ [3645/3649] Building OIBridge.EqvK2Block` (11
  prints: `dict_blockAct`, `blockMat_mulVec`, `conj_vecMulVec`, `suTo_isSU`, `Q3_blockInvariant` standard;
  `suTo_mulVec`, `dict_prod_bloch`, `reach_block`, `pairCone_eq_Q3_of_block`, `pairCone_eq_Q3_iff_block`,
  `aMiss_of_blockInvariant` with `sorryAx`), `⚠ [3646/3649] Built OIBridge.BridgeConverge` (21, standard);
  `EqvOneDictionary` not built (it imports `EqvK2Block`; it has no line in the log). The errors, all in
  `EqvK2Block` (verbatim heads, recorded before any repair): `184:32 Tactic rewrite failed: Did not find an
  occurrence of the pattern nrm a in the target expression 0 = ![↑(nrm 0), 0]` (`suTo_mulVec`, zero case: `rw [ha]`
  before `rw [h]`); `203:10 Unknown constant unitary.star_mem` (`isSU_conjTranspose`; at the pin the namespace is
  `Unitary`); `268:105 unsolved goals` (`tokMat_hom_bloch`: four entries left as `((↑α ^ 2 + ↑β ^ 2)⁻¹ • vecCons (α •
  star ![↑α, ↑β]) (vecCons (β • star ![↑α, ↑β]) !![,,])) i j` — `simp` unfolded `vecMulVec` into rows and did not
  apply the scalar); `291:2 unsolved goals` (`dict_prod_bloch`, degenerate case: sixteen goals `0 = tensorOf
  (vecCons 0 (vecCons 0 !![,,])) (vecCons (star ![1, 0]) (vecCons 0 !![,,])) (a, b) (c, d)`); `410:2` and `419:2
  unsolved goals` (`hphase_isSU`: `simp` rewrote the real half-angle cosine and sine into `Complex.cos (↑t * (1 /
  2))`, `Complex.sin …`, leaving `starRingEnd ℂ` and `Complex.I ^ 2`); `429:44 unsolved goals` (`hphase_eq`, entry
  (1, 1), the same normal form); `450:52 linarith failed` (`hphase_unit`, the same normal form); `455:2` and `462:2
  unsolved goals 1 / 2 + Complex.I ^ 2 * (-1 / 2) = 1` (`cycMat_isSU`). A common cause behind four of them: inside
  `first | ring | …`, `ring` that cannot close a goal falls back to `ring_nf`, succeeds as a tactic and leaves the
  goal open, so the later alternatives were never tried (`Try this: ring_nf` infos at 279:21, 416:10, 442:8, 460:10,
  465:8). **Reading** by NOTES-E19 §2's rule, fixed before the dispatch: the Build step failed, so no module is
  BUILT; `EqvK2Block` PARTIAL (5 of 11 prints standard; `reach_block` and the two main theorems carry `sorryAx`);
  `EqvK2Schema`, `EqvK2Converse`, `BridgeDictionary`, `BridgeConverge` PARTIAL by the rule's letter (their own build
  lines `Built`, every print standard); `EqvOneDictionary` NOT BUILT. Prediction `EqvK2Block` BUILT (0.4) failed,
  at the places §2 named as the risks (the sixteen-entry identities, §H.5's half-angle identities) and at one API
  name §2 did not foresee. The failed text is kept as `lean/EqvK2Block.run38124464622.lean` (blob `d339c6c5`) and
  the unbuilt `EqvOneDictionary` text as `lean/EqvOneDictionary.run38124464622.lean` (blob `00ac3707`, never
  compiled; kept because its repair-by-inspection changes it); the repair is proof-only, statements unchanged.
- 2026-10-11T10:16Z — cross-branch read (authorized by the coordinator's message of 10:05Z): `research/overview` @
  `51cce8ac353fffb6666999d5311d97b932ff03b7` (fetched 10:12Z), `git show 51cce8ac:research/OVERVIEW.md` (blob
  `9b13c2ce`, sha256 `4aed424d3d1251fc29717ea2971ec821a6d03daca9a9fc8f4fc2d7c89f3b9b41`), read in full for the
  section "The decisive round-5 outcome, classified (owner, 2026-10-11)" — outcomes (A) the drive derived from
  existing OI premises, (B) derived only after a new independently motivated premise, (C) supplied by an assumption
  equivalent to the phase intervention, (D) the existing premises admit non-quantum countermodels — and the
  explicit-scope rule ("a proof of insufficiency for the complete stage-6 inventory is definitive within its scope
  and establishes nothing about every conceivable extension of OI"); with it the round-5 node list and the two
  distinctions already relayed. Applied where E19 bears on the outcome: NOTES-E19 §3.
- 2026-10-11T10:18Z — **E20 begun (S0 and probe committed together, before the probe's first run).** `NOTES-E20.md` S0
  (written 08:27Z, unchanged, sha256 `96e95bc5…`) and `experiments/e20_odd_bodies.py`, reviewed after the
  resumption and corrected before its first run and first commit (draft `5743149f…` → `4f1a4739…` after the edits
  below, the header note dated 10:17Z): SF3's non-product test now takes the rank of the 4 × 4 table block (the
  draft took the rank of the block's density matrix, which is 1 for the pure entangled image — a harness error that
  would have failed SF3); a vacuous clause removed from C1. Decision rule unchanged.
- 2026-10-11T10:32Z — **dispatch 2 of 3.** The repair written (proof-only; NOTES-E19 §2-b, written 10:31Z before the
  dispatch, with the reading rule unchanged and the predictions): `lean/EqvK2Block.lean` (blob `23d0db23`) and
  `lean/EqvOneDictionary.lean` (blob `39b4188a`). Dev branch `dev-equivalence/r5-design`: commit
  `f67da96728f1ef54f0dc3aea3cc3c1a532d8eb0a` (the two modules only; the other four modules and the import lines
  unchanged), pushed; `workflow_dispatch` of `verify.yml` via `gh api` at 10:31:41Z: run `38132266383` (head
  `f67da967`), queued.
- 2026-10-11T10:34Z — coordinator message (usage-limit protection), applied from now on: "commit and push
  research/equivalence at every finished step (notes, scripts with their outputs, the lean/ copies, LOG entries), not
  only at node close; push your current uncommitted files as soon as they are in a consistent state. Do not change
  your plan otherwise; the dispatch cap (3) and all rules stand." Pushed now: the dispatch-2 repair texts
  (`lean/EqvK2Block.lean`, `lean/EqvOneDictionary.lean`), NOTES-E19 §2-b, E20's run 1 kept as
  `experiments/e20_odd_bodies.run1.*` (the shell wrapper had appended its exit status `exit 1` to the `.err` file;
  removed — the program wrote nothing to stderr, its stdout ends with `exit 1`), NOTES-E20 S0-b (10:33Z) and the
  run-2 harness (decision rule unchanged), before run 2.
- 2026-10-11T10:39Z — `experiments/e20_odd_bodies.py` run 2 (10:33:55Z–10:36:50Z; S0-b's threshold change and
  diagnostics): 7/8 again, C4 FAIL with the positive control `eball 3` `UNDECIDED(iterations)` at the same 18639
  constraints; `eball 5` and `Ω⋆⁵` `FEASIBLE(pool)`; D1: the `eball 5` candidate violates `posFwd` off the pool
  (minimum `−5.1·10⁻²`, 23 of 400 000 quadruples), the `Ω⋆⁵` candidate likewise (`−5.5·10⁻¹`, 6687); D2: both candidates
  violate `posInv` on the pool (minima `−16.9` and `−33.4`); `VERDICT NOT RENDERED`; kept as
  `experiments/e20_odd_bodies.run2.*` (py `ec95a697…`, out `d2bc6007…`). A debugging pass on a scratch copy (not a
  recorded run) shows the S0-b diagnosis of run 1 was wrong: the `eball 3` loop is not a tolerance stall — its margin
  settles at `t* = 6.24·10⁻³ > 0` while every round still finds pool violations of order `10⁻²` (the cutting plane
  converges slowly in the 48-dimensional `F`, 600 cuts a round, 40 rounds); no verdict is drawn from E20.
- 2026-10-11T10:39Z — **owner's direction (relayed by the coordinator, 10:38Z), binding: round 5 is narrowed.**
  Quoted: "1. Now: commit and push your uncommitted files (LOG.md, NOTES-E21.md, the e20 outputs). Label the E20/E21
  material in the commit message 'WIP — deferred to round 6, unverified'. WIP commits are acceptable on research
  branches only when labeled. 2. Complete E19 only. Finish the queued build (dispatch 2) and establish the strongest
  justified equivalence result. 3. E20–E22 move to round 6. Do E20–E22 work only if a portion is indispensable to
  completing E19, and say which portion and why. 4. State E19's result with sufficiency and necessity kept apart.
  Witness each direction of any equivalence separately (§A.34). Classify every hypothesis. Keep the circularity check
  (does ReachPure follow, or do the forcing conditions contain it) explicit. Keep exact generation and
  closure/density steps separate, as in your S0-b/S0-c. 5. Close E19 with RESULTS rows, LOG, handoff proposals, push,
  then stop. The cap of 3 dispatches stands." Applied: E20 (S0, S0-b, runs 1–2, the run-2 harness) and E21 (S0 only;
  no module written, nothing dispatched) are committed as WIP, deferred to round 6, unverified, with no RESULTS or
  LEDGER rows this round. Of E22, one portion is indispensable to E19 and is kept: §B of `lean/EqvOneDictionary.lean`
  (`isClosed_dualW`/`isClosed_of_selfDual`, `continuous_transferMap`, `invariant_of_closure`, `flow_of_dense`) with
  the two lemmas it uses from §A (`transferMap_phase`, `transferMap_cyc`) — because the owner's second round-5
  direction requires the dense-control form of E19 to establish (i) closedness, (ii) continuity of the action and
  (iv) the closure lemma as premises before C19-1 (a) gives `ReachPure`, and these are their proofs; the rest of the
  module (§A's two directions against the bridge's `TransferClause`, §C) is E22 proper — built in dispatch 2 because it
  was queued, its reading recorded, its analysis deferred to round 6.
- 2026-10-11T10:58Z — dispatch 2 measured (run `38132266383`, head `f67da967`): Mathlib bridge job `114448854872`
  (10:31:44Z–10:34:55Z) **Build success**; prints `EqvK2Schema` 22/22, `EqvK2Converse` 9/9, `EqvK2Block` 11/11,
  `BridgeDictionary` 20/20, `BridgeConverge` 21/21, `EqvOneDictionary` 10/10, every one `[propext, Classical.choice,
  Quot.sound]`; release gate red only at `lean-manuscript` (6 problems: the six unregistered design modules, by
  construction), `lean-axioms` PASS (5949 named results, no sorry), `legacy-records` 303 intact, `v3-receipts` 43
  hold, every other step PASS; Lean kernel check job `114448854875` success. Log read with the GitHub MCP job-log
  tool, tail 5000 of 38180 lines (scratchpad, sha256 `840c33ce…`). **Reading** by NOTES-E19 §2's rule: `EqvK2Block`
  BUILT, `EqvOneDictionary` BUILT (and the four carried modules BUILT). Predictions of §2-b held (0.6, 0.4, both
  0.3). The `lean/` copies are byte-identical to the dispatched blobs (`23d0db23`, `39b4188a`).
- 2026-10-11T10:58Z — E19, the generation step (the decisive question of the owner's first round-5 direction):
  `lean/EqvK2Generation.lean` drafted — exact finite words from the gate and the clause's two operations to every
  block pair of special unitaries (Euler factors through polar forms and one square root; the controlled phase as
  `gate · idle · gate · idle`; the cyclic lift's inverse as minus its square), hence `BlockInvariant` from H2 and
  A_miss with no closure, `ReachPure` as a theorem, and the two directions of the full-flow equivalence. Every
  `linear_combination` coefficient checked symbolically beforehand (sympy, scratchpad); not yet dispatched.
- 2026-10-11T11:05Z — **dispatch 3 of 3 (the last).** NOTES-E19 §2-c written at 11:04Z before it (reading rule
  unchanged, predictions). Dev branch `dev-equivalence/r5-design`: commit `f0c36cf9fa8395ac4349d944dc21dda80e4c2658`
  (adds `OIBridge/EqvK2Generation.lean`, blob `682f187e`, byte-identical to `lean/EqvK2Generation.lean`, and one
  import line after `import OIBridge.EqvOneDictionary`; nothing else changed), pushed; `workflow_dispatch` of
  `verify.yml` via `gh api` at 11:04:40Z: run `38134245361` (head `f0c36cf9`), queued. No dispatch remains.
- 2026-10-11T11:11Z — **dispatch 3 measured** (run `38134245361`, head `f0c36cf9`): Mathlib bridge job `114454742595`
  (11:06:17Z–11:09:57Z) **Build success** (`Build completed successfully (3650 jobs)`); prints `EqvK2Generation`
  12/12, `EqvK2Schema` 22/22, `EqvK2Converse` 9/9, `EqvK2Block` 11/11, `BridgeDictionary` 20/20, `BridgeConverge` 21/21,
  `EqvOneDictionary` 10/10, every one `[propext, Classical.choice, Quot.sound]`, no error (warnings only); release
  gate red only at `lean-manuscript` (7 problems: the seven unregistered design modules, by construction),
  `lean-axioms` PASS (5961 named results, no sorry), `legacy-records` 303 intact, `v3-receipts` 43 hold, every other
  step PASS. Log read with the GitHub MCP job-log tool, tail 5000 of 38389 lines (scratchpad, sha256 `f7a6d94b…`); the
  run's other jobs were still queued or running at 11:10Z (the Lean kernel check job `114454742690` queued) — no job
  or run was cancelled. **Reading** by NOTES-E19 §2's rule: `EqvK2Generation` BUILT (prediction 0.35 — it came true).
  So [D]: `su_euler` (Euler factors without angles), `blockInvariant_of_drive` (H2 and A_miss give block invariance
  by exact finite words), **`reachPure : ReachPure` (S6's L4 a theorem)**, `pairCone_eq_Q3_of_drive_exact` (H1, H2,
  H3, A_miss ⇒ `K = Q3`, no `ReachPure`), `Q3_cnot`, `pairCone_eq_Q3_iff_drive_exact` (given H1 and H3, `K = Q3` iff
  H2 and A_miss; the two directions separate theorems). The `lean/` copy is byte-identical to the dispatched blob
  (`682f187e`). All three dispatches used; none remains.
- 2026-10-11T11:19Z — `experiments/e8_cite_check.py` run 6 (run 5's files kept as `.run5.*`; the header extends the
  scope to the round-5 E19 documents and the round-5 design modules, lists another thread's design-module citations as
  out of scope, and leaves the decision rule as fixed before run 2): 75 distinct citations (158 occurrences), 71 named
  pairs, X1–X3 failing as stated, `VERDICT CITATIONS-RESOLVE`; `CmSprime.lean:1067` (NOTES-E19 S0) listed out of
  scope; replay byte-identical (py `14623c27…`, out `a8a0f83a…`). RESULTS row R-CITE.5.
- 2026-10-11T11:21Z — final replays (11:19Z): `e19_s6_controls` and `e19b_block_controls` byte-identical to their
  committed outputs (py `80787ca1…`/out `ecaddd86…`; py `92e6a5b3…`/out `b6f90dd7…`). Dispatch 3's run at 11:20Z: Lean
  kernel check `success`, Mathlib bridge as recorded (Build success, gate red only at `lean-manuscript`), 28 probe jobs
  `success`, three A42 shards still running — none cancelled. NOTES-E20 and NOTES-E21 carry a status line: work in
  progress, deferred to round 6, unverified.
- 2026-10-11T11:21Z — **round 5 closed.** Nodes: **E19 closed** — `ReachPure` is a theorem (`reachPure`) and, given H1
  and H3, `K = Q3` iff H2 and A_miss (`pairCone_eq_Q3_iff_drive_exact`, each direction its own theorem), with the
  generation step by exact finite words (`blockInvariant_of_drive`), the block form (`pairCone_eq_Q3_iff_block`), the
  dense-control premises (i), (ii), (iv) in design and DENSE(θ₀) at [L], and the countercontrol family on
  `theorem_Sprime_ineq` with its hypotheses checked exactly; RESULTS R-E19.1–R-E19.6 (CONJECTURE: design runs and exact
  checks), draft S6 revised, LEDGER round-5 notes, HP-equivalence-14, -15, -16; classification NEW (ReachPure derived),
  POSITIVE (the family), ELABORATING (angle-free Euler factors; the split of the closure identification). **E20, E21,
  E22 deferred to round 6** by the owner's direction (WIP committed and labelled; HP-equivalence-17). Dispatches: 3 of
  3 (runs 38124464622 failure at Build, 38132266383 and 38134245361 Build success with every print standard, gate red
  only at `lean-manuscript`); no CI job or run cancelled. Cross-branch reads, each logged with commit and sha256:
  `research/overview` @ `4c4a02b1` (the eight handoffs copied byte-identically; the round-4 audit, HO-18 v2, HO-28,
  HO-29 read) and @ `51cce8ac` (OVERVIEW.md); `research/countermodels` @ `644bf0a1` (CmSprime, NOTES-C19, NOTES-C21,
  `c19_groups.py`, `c21_rows.py`); `research/bridge` @ `a34d20b5` (BridgeDictionary, BridgeConverge, carried verbatim
  onto the dev branch); `research/archive` @ `4dc0321c` (free). Deviations, each recorded where it happened: four
  unauthorized overview extracts written by an over-broad loop and deleted unread (07:21Z); dev-branch writes under
  `verification/` (the dev branch only, as every round); dispatch 1 logged only after the interruption, from the host's
  record; timestamps written ahead of the measured time corrected before or at their commits (LOG 08:02Z, 10:34Z,
  10:58Z; NOTES-E19 §2-b; NOTES-E20 S0-b; the E20 header); the E20 harness corrected after the resumption before its
  first run, and S0-b's diagnosis of its run 1 later found wrong (10:39Z); the shell wrapper's `exit 1` line removed
  from E20 run 1's `.err`; a debugging pass on a scratch copy of the E20 probe (not a recorded run); `EqvOneDictionary`
  (E22) built in dispatch 2 although E22 was later deferred (queued before the narrowing; its §B belongs to E19); the
  third dispatch carried E19's generation module instead of E21's (E21 deferred, no module written); S0-c's label for
  DENSE(θ₀) ("introduced") revised in NOTES-E19 §3 to a mathematical statement at [L], recorded there.

## Round 6

- 2026-10-11T15:18Z — round 6 opened at thread head `3a46b811` (verified at 15:15:18Z by `date -u`: after `git fetch origin
  research/equivalence`, `git rev-parse HEAD` = `git rev-parse origin/research/equivalence` =
  `3a46b81103717c55510ea5b57ea7d520858cb478`; `git status --porcelain` empty). Re-read this thread's record: README,
  LOG, LEDGER, RESULTS, NOTES-E19, NOTES-E20 (S0, S0-b), NOTES-E21, HP-equivalence-14 … 17, `lean/*.lean`,
  `experiments/e20_odd_bodies.*` (runs 1 and 2 kept; the working script is byte-identical to `.run2.py`). NOTES-E22.md
  does not exist. Conventions unchanged from round 5. **Round-6 rule additions, applied from this entry:** (i) this LOG
  is append-only — a correction is a new entry naming the entry it corrects, never an edit in place, and every
  timestamp is read from `date -u` at writing time (finding F-E5-1); (ii) a `|` inside a code span in a Markdown table
  is written `\|`; (iii) every route from available operations to a limit names its closure premise and the form of
  transfer it needs, with the closedness of the cone it uses; (iv) results bearing on the transfer clause record the
  owner's four claims separately. Budget: at most three `workflow_dispatch` runs; no cancellation; no pull request.
  Not this thread's this round: E23 (the sources of H2, H3 and A_miss) and the S6 surface (`cnotMat` / `dict_cnot`),
  worked in `research/round6-transfer-sourcing`, which is not read.
- 2026-10-11T15:18Z — **receipt of HO-33 v2, HO-37 v1, HO-38 v1, HO-39 v1, HO-40 v1, HO-41 v1, HO-42 v1, HO-45 v1**
  (`research/HANDOFFS/` at `research/overview` @ `1325160c35ddb5b7a9f6f608cced0225a40401f1`, the commit the
  instruction names; `git fetch origin research/overview` at 15:16Z returned the later tip `39370c99b4395344…`, of
  which `1325160c` is an ancestor; every read of this round is at `1325160c`), each copied byte-identically to
  `inbox/` by `git show 1325160c:<path>`, the git blob of the copy checked equal to the source blob: HO-33 v2 blob
  `f3292240`, sha256 `17e217fa00fb4b7dc1bd0efbefb8b69fd1ce6da24698978ccba0c22213d58795`; HO-37 `ea15ac7a`,
  `e1daa4503eca9e31a51e7ff8ed7d02a381fa2ce9a006af1cf58bcc25f5fe2ff3`; HO-38 `e99bb756`,
  `867dbacd05557d3bcfbe77134e319213c12112ce95b9143b58883abf4f72012d`; HO-39 `ed856ba2`,
  `2fc5103f52ccfa80bc69f7e6b5dbe0017753a7daf5b57e48915194f9a0c54f27`; HO-40 `b9d294bd`,
  `8aaed02fcca73825383187bc6ad1615d4617ead367c89cb3339ca783bafe427e`; HO-41 `09d77949`,
  `1559c0984ef8acb2cfd3432112d889385666eabb27597326114193ee68fa5fd6`; HO-42 `dc32b186`,
  `f12ce49200067e3fbc80e688209d69411fbd5b77215887288bf42d1cd3c48ac7`; HO-45 `e72ce580`,
  `8aa5a61a9dfb8ce21a211917951c3d2da216101a9da91737464f610927cff301`. HO-33 v1 stays in `inbox/` unchanged (v2 replaces
  its item 2 and correction item only). **Reliance, item by item, stated before any use** (only at the labels the
  handoffs carry; nothing in them is CERTIFIED except kernel declarations named at L; every "may not assume" clause is
  honoured as stated under each handoff):
  - **HO-33 v2 (bridge, origin).** Item 2 (v2) — the availability of `actT R_z(θ₀)` and `actT J` is independent of
    every row of Table A2 that does not itself imply composite unitary control or QM, and not of the inventory as a
    whole: I4.60 `SubstratumAvail`, outside Table A2, implies OpDrive(θ₀) (`opDrive_of_substratumAvail` [D]); the two
    [W] rows on the design chain of HO-37 — is **relied on as a wording constraint** in E22 and in every round-6 text:
    no independence statement about these operations is written without "relative to Table A2's rows", and none is a
    premise of any statement here. Items 1 and 3–6 of v1: context at their v1 labels, as recorded in round 5 (07:21Z).
    Honoured: no "independent of the stage-6 inventory" without the Table-A2 scope; no certification or census
    disposition; v1's may-not-assume list.
  - **HO-37 v1 (bridge).** Items 1–2 (the layer-flow endpoint without `SubstratumAvail` for fixed-point-free
    involutions, [D]; FM's rows I4.56 and I2.34 HARMLESS) are **recorded and not relied on**: no round-6 node of this
    thread concerns `LayerFlowExecutable`, composite unitary control or FM's rows. Item 3 (a kernel theorem with
    `SubstratumAvail` among its hypotheses may be weaker than stated) is recorded as an assumption-watch marker; no
    round-6 statement here cites such a theorem. Honoured: no certification; nothing for involutions with a fixed
    point; LiftAudit.lean:812 not applied to FM.
  - **HO-38 v1 (bridge; addressed to E22).** Items 1–3 (`pairAvail_iff_tokenAvail` [D] for context-stable,
    label-invariant architectures; its domains; "the decision falls at the token") are **relied on in E22 only as the
    availability-side statement** from which E22's invariance-side statements are kept apart: availability lives in the
    `InstAvail` closure on the kernel's Kronecker carrier; `EqvOneDictionary` speaks of cones on `W 3`. No E22
    statement takes it as a premise. Honoured: no certification; nothing about a pair cone on `W 3` drawn from it;
    token ⇒ pair never used without context stability.
  - **HO-39 v1 (bridge; addressed to E19, E22).** Item 2's reading of (T)_𝓘 — `TransferClause` (BridgeDictionary [D]),
    `transferClause_iff` (BridgeConverge [D]), the derived half `bridge_derived_half` (CONDITIONAL [D]) — is **relied
    on in E22 as the reading of the bridge's clause**, with the definitions re-read from `research/bridge` @
    `5ba9218e` (authorized; logged when read). Items 1, 3 ((T) cannot be omitted from this construction, verified), 4
    (exact availability, not density: a dense subgroup gives membership of its own elements only; the limit needs a
    closed cone (H3) and continuity and gives invariance only), 5 and 6: **context for E22**; item 4 is the
    availability-side counterpart of R-E19.5's cone-side dense-control form, and E22 records the two apart. The
    four-claims table: **E22's result records the owner's four claims separately** (rule (iv)). The audit's §9 (whether
    the complete OI framework implies (T): OPEN) is recorded; E22 does not address it (E23/B22). Honoured: no
    certification; (T) for `{R_z(θ₀), J}` never drawn from the data without (T)_𝓘; neither OpDrive(θ₀) nor the transfer
    clause stated as necessary for QM; no inventory item at L said to imply either datum; no equivalence between the
    data and the invariances.
  - **HO-40 v1 (bridge).** Items 1–3 (the closure `G` of B10-4; no self-dual rank-one surgery with H1, CONDITIONAL on
    Lemma C18-1; what remains) are **recorded and not relied on**: no round-6 node of this thread uses S6's
    countercontrol family. Honoured: no kernel check; no exotic `G`-invariant cone; nothing about rank-two or
    non-surgery constructions; nothing about conjugacy to a subgroup of `G_B`.
  - **HO-41 v1 (countermodels).** Items 1–3 (Theorem S′ in compact form [D], run 38131214451; the closedness remark
    [W]; the consumers, `Kk` among them) are **recorded and not relied on this round**. Consequence noted for this
    thread's record: R-E19.1 and draft S6 label `Kk` "on Theorem S′ for compact defect sets [W]"; that label is not
    changed this round, because a change needs this thread's own check of `Kk`'s hypotheses against
    `theorem_Sprime_compact_ineq` (the rule applied to `K384`, `K768`, `KC` in round 5), which no round-6 node
    performs — a pending item. Honoured: no certification; item 2 not machine-checked; (CC) not necessary; no
    extremality; H1 of no cone from it; no OI content; no availability.
  - **HO-42 v1 (countermodels, with the coordinator's correction F-C5-1).** Items 1–6 (the universal orthogonal pair;
    the rank-one route closed for `c ∈ (1, 2)` and, as corrected, no `G_T`-orbit admissible for H1 at `c = 2`; the
    engine certifies nothing; OBSTRUCTED; the certificate) are **recorded and not relied on**. Its assumption-watch
    marker "invariance under a dense subgroup is invariance under its closure — for closed cones only; the step uses H3"
    agrees with R-E19.5 (i) (`isClosed_of_selfDual`) and is applied in E22's rule-(iii) statements. Honoured: nothing
    certified; no claim that no exotic `G_T`-invariant cone exists; nothing about balanced surgeries being
    non-self-dual; the proposal's Bell-circle statements not read as statements about `G_T`; no availability.
  - **HO-45 v1 (origin, with the coordinator's qualifications F-O5-2, F-O5-3).** Item 7's scope and its definition of
    the channel form (T^ch)_𝓘 with `K` closed are **relied on in E22 as vocabulary for rule (iii)**: the clause
    `EqvOneDictionary` meets is the unitary form (T)_𝓘; the channel form is neither stated nor built here; every limit
    route E22 names states its closure premise (`K` closed, from H3), the continuity it uses and its density input.
    Item 4 (exact QM entails the drive, `opDrive_of_qm` [D], availability) is **relied on** for any necessity statement
    about the drive's availability — E22 makes none. Items 1–3, 5, 6, 8, 9 and the generating-set table: context, not
    relied on. Honoured: no kernel status for any [D] declaration, item 5's valuation argument, item 6's protocol or
    O9-L1; item 6 never read as availability of the drive; nothing serves the bridge's cones without (T^ch)_𝓘 and
    closedness; the orders only at levels one and two; nothing about dilations; (T)_𝓘 and (T^ch)_𝓘 neither supplied
    nor said to be needed for QM; no availability from cone invariance.
  No research step of round 6 precedes this receipt's commit.
- 2026-10-11T15:18Z — **authorized cross-branch reads** (read-only, `research/overview` @ `1325160c`, each extracted to the session
  scratchpad by `git show 1325160c:<path>`, blob and sha256 recorded): `research/AUDITS/2026-10-11-round5/
  AUDIT-EQUIVALENCE-R5.md` (blob `e8e7f49a`, sha256 `8a7f882d5050263a5d553e8c90026048885c0b6c00f8d3e50b5b349b42010cdb`),
  read in full (§1–§10; the instruction's emphasis §7–§10 and F-E5-1); the handoffs issued from this thread's proposals,
  `research/HANDOFFS/HO-43-equivalence-to-bridge-origin-k2-target-h2-amiss-reachpure-derived.md` (`9473c660`,
  `2b66cf113ed9402d79d6b500bc4f4267627640ab0686acd56251ed110e8ba12b`) and `…/HO-44-equivalence-to-countermodels-where-exotic-
  cones-must-break.md` (`70a888f7`, `1e3d32d8ad689a3b133131e8484d39e46cfbe2d7d41c9a7c9df1e75f1f526511`), read in full;
  `research/OVERVIEW.md` (`a5ea093a`, `2346f6ad7c6b96691bae3bff9d75a4c2ef62c33a723001546536a88e4960ea64`): its
  Markdown headings listed to locate the section, then the round-6 section (lines 1126–1179) read, nothing else.
  **Acknowledged.** F-E5-1 (LOG timestamps edited in place in `a047ee43` and `1329adc9`): accepted; from this round
  every LOG correction is a new entry naming the corrected one (rule (i)). No finding on the mathematics; no label
  changes (R-E19.1 … R-E19.6, R-CITE.5 stand). The audit's independent check (`indep_checkE5.py`, Z1–Z7) and its
  reconstruction of E20's 08:30Z draft are recorded; E20's round-6 runs build on the committed run-2 harness. §10's
  carried items: E20, E21, E22 are this round's nodes; the sources of H2, H3, A_miss are E23, not this thread's this
  round. **HO-43 v1 and HO-44 v1** (from HP-equivalence-14, -15, -16): their items agree with the proposals and with
  R-E19.1 … R-E19.6; their seven line citations to this thread's design modules resolve, in the `lean/` copies, to the
  declarations they name (EqvK2Generation.lean:448 `blockInvariant_of_drive`, :499 `reachPure`, :535
  `pairCone_eq_Q3_iff_drive_exact`, :345 `su_euler`, :382 `rtrick`; EqvK2Block.lean:385 `pairCone_eq_Q3_iff_block`;
  EqvOneDictionary.lean:121 `aMiss_of_transferClause`). Nothing to correct.
