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
