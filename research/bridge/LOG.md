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
- 2026-10-10T20:46:21Z — commit B4/B5 recorded: 0e601e17 (pushed).
- 2026-10-10T20:48Z — decision: bounded depth-first attempt on the residual Conjecture B3.C (scope of the B3 no-go),
  timeboxed; written proofs only. Result: partial theorem (P1)–(P3) in NOTES-B3 §2.1. Wall recorded: non-grid or
  partially-product eigenbases and degenerate 2-tori need a moment-polytope covering analysis under `cnot ∈ N(T)`, not
  done. RESULTS B3-4 updated (still CONJECTURE, with partial results).
- 2026-10-10T20:50Z — B3.C: (P2) extended to (P2′), any orthonormal product eigenbasis (non-grid case: support-3
  products have pinned second factor, so face moduli lie on finitely many curves). Wall narrowed to eigenbases with
  exactly 1–3 product lines and degenerate 2-tori. Stopping the B3.C attempt at this wall (timebox).
- 2026-10-10T20:50:31Z — commit 9bb9ce3a (B3.C (P2′)) pushed; remote head verified equal to local.
- 2026-10-10T20:50Z — closing: nodes B1–B5 complete. Stop at the B3.C wall (no padding). Record defects of this
  session, all corrected forward and kept visible: timestamps were written from estimates instead of `date -u` in the
  b2 header, the b3 header, the b4 pre-run note (fixed before its run) and three LOG lines (this entry included: first
  written as 20:52Z). The two script cases are kept as `.run1.*` with outputs identical to the final
  runs. Lean dispatches used: 0 of 3. Inbox: empty throughout.

## Round 2

- 2026-10-10T21:48Z — round 2 opened at thread head 5f4089a4 (verified clean, up to date with origin). Read, in order:
  README.md, LOG.md, RESULTS.md, NOTES-B1 … NOTES-B5 (own round-1 record); the coordinator's
  AUDIT-BRIDGE.md and OVERVIEW.md on research/overview @ 62cbb3cf (read-only). Audit: no label changes; B5-2
  (formalization of Theorem B1.1) proposed as round-2 node.
- 2026-10-10T21:48Z — receipts. Copied from research/overview @ 62cbb3cf `research/HANDOFFS/` into `inbox/`,
  byte-identical (cmp), sha256:
  - HO-4 v1 (countermodels → bridge, KZ1–KZ12) `0c67c44937839c6293126082ec9aff66d90fab4d1c112435eeef91630370b184`;
  - HO-5 v1 (origin → bridge, SRC/SPEC, Lemma P) `25a4ff61de4b00ad32b266ff2328f8da0667c284d7540eef93852a93b81bbc8d`;
  - HO-6 v1 (equivalence → bridge, one map for K2(c) and Kₙ) `901e8d1074ce41cc7d51095eafb5e994f18f716dd2c5e4953835e22a3ae2b9b0`.
  Reliance (nothing in them is CERTIFIED; each item is used only at the label it carries):
  - **HO-4.** Relied on in B8 only: KZ6 (local symmetry group of order 384, 96 local unitary Cliffords) and KZ7 (the
    flow law `−sin t/8` for every axis) as CONDITIONAL exact facts of K(Z_F), both independently confirmed by the
    coordinator; I re-derive what B8 needs from them with my own exact code rather than cite them as premises. KZ5 is
    not relied on (rank-one-preserver input [U]). The composition-clause proposal is the object B8 tests, not an
    assumption. KZ11's `K_circ` is not used (existence by EBF only).
  - **HO-5.** Relied on in B9: item 1 (A_miss ⟺ (b) for `R_z(t)` all `t` ∧ (b) for `J = cyc3`) as CONDITIONAL [W]
    with [X] identities, re-checked in my own script before use; item 4 (matrix reduction through
    `substratumClass_contextStable`) as CONDITIONAL [W], used only to frame what B9 asks; item 5 (Lemma P) as a
    constraint on any realization I construct (no passive token-level observation where a drive is wanted). Item 6
    (the joint statement) is not relied on: unadopted proposal. SRC(J) and SPEC are OPEN and are not assumed.
  - **HO-6.** Relied on as a planning input for B9 (the dictionary request), at its labels: W-DESC / Kₙ-DESC
    CONJECTURE; the absence of a map at L [A]. I do not assume `ContextStable` is (b) (the handoff forbids the
    identification without a formal map; B9's job is to state what such a map needs).
- 2026-10-10T22:12Z — B6 design decisions (before writing the module). Theorem B1.1 is formalized in two forms:
  (i) RESPECT in readout-kernel form (`R ν = 0 → R (P ν) = 0`, the form B1 §2 and B3.1 use for readout-respecting
  permutations), product behaviour on a spanning set `X` of token points, (A); (ii) B1.1 exactly as written in
  NOTES-B1 §2 (RESPECT only on the convex set `𝒫`, normalized readout, H1 on the ball), reduced to (i) on the span of
  `𝒫` through differences of rays. Local tomography is proved as a theorem of the carrier from one-token spanning, not
  assumed. Controls in the module: an L-REG model on `Fin 4 × Fin 4` realizing the kernel's `cyc3` (linear part
  `cycEquiv`) as the hidden bijection `tokPerm × id` (positive control: all hypotheses hold), and the same model with
  `𝒫` a point mass (countercontrol: (A) fails and the conclusion fails). Generic linear-algebra core
  (`intertwine_of_respect`) so the actC/actT and convex forms share one proof.
- 2026-10-10T22:15Z — dev branch `dev-bridge/b11-lemma` created from the thread head e29b6a42 with git plumbing (a
  temporary index; the research/bridge working tree and index untouched): commit 00d43da4 adds
  `verification/lean-mathlib/OIBridge/BridgeLemma.lean` (blob 937a97e9, verbatim copy of `lean/BridgeLemma.lean`)
  and **one import line in the root `verification/lean-mathlib/OIBridge.lean`** (after `RelcSelectC5`). Deviation,
  recorded: the root file is outside `verification/lean-mathlib/OIBridge/`; it is needed because the lake library
  builds only modules reachable from the root and `tools/lean_axiom_check.py` fails on any unelaborated
  `#print axioms` line; the round-1 dev branches (`dev-equivalence/kinf-seams`, `dev-origin/envelope`) did the same.
  Dev branch only; never on research/bridge's verification tree.
- 2026-10-10T22:16:12Z — dispatch 1 of 3: `verify.yml` on `dev-bridge/b11-lemma` @ 00d43da4, run 38090784384
  (queued). No local Lean toolchain (and 7.8 GB free on a shared container: a Mathlib install was not attempted).
- 2026-10-10T22:26:50Z — B7 decision rule written into `b7_b3c.py` (date -u taken immediately before writing).
  Approach: reduce B3.C via claim (D) [A] to "H·P misses a pure state"; one uniform certificate for all
  four-eigenline cases (moment orbit near vertices; Lemma 2), Lemma 3 (exactly three product lines impossible), a
  separate argument for the `(2,1,1)` 2-tori. Instances in the CZ frame (local Hadamard on the target).
- 2026-10-10T22:28:51Z — `b7_b3c.py` run 1: 13/13 PASS, VERDICT B7-B3C-EXACT; replay byte-identical (22:29Z). No
  failed runs; no pre-run edits after the rule was fixed. I4 is certified by the second parameter triple of the fixed
  list (the first fails one order), as the rule provides.
- 2026-10-10T22:31Z — NOTES-B7 written; RESULTS rows B7-1 … B7-4 appended (round-2 section). B3-4 is not edited;
  B7-2 supersedes its label for the same statement.
- 2026-10-10T22:33Z — run 38090784384 (dispatch 1) read through the jobs API and the job log (GitHub MCP job-log
  reader; the built-in `gh` refuses the log host redirect). Mathlib bridge job 114326594532: **Build failure** (step 5,
  22:28:43–22:30:37Z), Release gate skipped; every other job of the run green or still queued at reading time.
  Cause: `𝒫` is Mathlib notation (`Set.powerset`) and cannot bind a variable, so the nine declarations binding it
  failed to parse (`unexpected token '𝒫'`) and their dependents reported unknown identifiers. Built with
  `#print axioms` = [propext, Classical.choice, Quot.sound]: `actCLin`, `actTLin`, `intertwine_of_respect`,
  `span_prodSetOf`, `span_hom_of_frame`, `span_productSet`, `ctl_intertwine`. No `sorry`.
- 2026-10-10T22:35Z — module corrected: `𝒫` renamed `Pd`; alternatives the linter reported as never executed removed
  (each first alternative had succeeded); `mem_diffSub` added; the countercontrol evaluates its two entries
  explicitly. The dispatch-1 text stays in history (3d775029 here; 00d43da4 on the dev branch).
- 2026-10-10T22:36:12Z — dispatch 2 of 3: dev commit f1c5f0fb (child of 00d43da4; module blob 1677640f), run
  38092042844.
- 2026-10-10T22:40:08Z — B8 decision rule written into `b8_composition.py`. Pre-run edit at 22:41:27Z (logged in
  the header; rule text unchanged): `ov2` as `a·conj(a)`, and the X3 part of X4 implemented as the rule states.
- 2026-10-10T22:41:34Z — `b8_composition.py` run 1: 4/4 PASS, VERDICT B8-EXACT; replay byte-identical. The
  realization theorem has no Lean declaration at L (its checker is `opglue_probes.py` per the coverage ledger); the
  kernel counterparts of its composition content are `InertSpectatorCompositionality` and
  `finiteOI_not_implies_inert` (OIRealization.lean:360).
- 2026-10-10T22:45Z — NOTES-B8 written; RESULTS rows B8-1 … B8-4 appended.
- 2026-10-10T22:45:37Z — B9 decision rule written into `b9_spec.py`. Correction (forward) of the previous entry: the
  line stamped 22:45Z for "NOTES-B8 written" is an estimate; the event preceded commit 9f2d40b3 (22:43:49Z).
- 2026-10-10T22:46:40Z — `b9_spec.py` pre-run edit (logged in its header; rule text unchanged): the `pc`/`pt` tables
  are parsed from CompositeDimension.lean at L; the draft's hand transcription of `pt` was its transpose. A further
  pre-run fix: the header's edit time was first written as an estimate (22:48Z) and corrected to the `date -u` value
  before the run.
- 2026-10-10T22:46:45Z — `b9_spec.py` run 1: 7/7 PASS, VERDICT B9-EXACT; replay byte-identical. The Y2 message text
  says "as transcribed"; the tables are parsed (printed in the output).
- 2026-10-10T22:49Z — NOTES-B9 written; RESULTS rows B9-1 … B9-4 appended.
- 2026-10-10T22:52:40Z — run 38090784384 cancelled (its remaining numerical-probe shards only). Its Mathlib bridge
  job had completed (Build failure, recorded above). The cancellation frees runners: the repository's queue at
  22:52Z held run 38092042844 (this thread, dispatch 2) behind three other threads' dispatches. Not a dispatch;
  dispatches used: 2 of 3.
- 2026-10-10T22:49–22:52Z (between commit 9c34afde, 22:49:29Z, and a `date -u` reading of 22:52:21Z) —
  `lean/BridgeDictionary.lean` drafted for B9: the two-token dictionary `dict` on the kernel's
  `tensorOf`, the product law `dict_tens`/`dict_prodState`, the certified monomial spectator theorem restated at the
  pair carrier, and the transfer clause `TransferClause` as a definition. Dispatched only if run 38092042844 is green
  (the last dispatch is reserved for B6 otherwise).
- 2026-10-10T22:53:52Z — handoff proposals HP-4 (B3.C, conditional on (D)), HP-5 (HO-4 tested; Stab_loc = V4), HP-6
  (SPEC side; HO-6's transfer needs) written for the coordinator to route.
- 2026-10-10T22:57:13Z — NOTES-B9 §2, row (D1): evidence cell made precise. b9 Y1 checks the product law only; the
  isomorphism `W 3 ≅ Herm(4)` is the standard Pauli-basis fact [W]. No result changes.
- 2026-10-10T22:57Z — NOTES-B6 drafted (declarations, mapping to NOTES-B1 §2, gaps); its CI section is filled in
  after run 38092042844.
- 2026-10-10T22:58:57Z — `b7b_generic.py` decision rule written (B7 robustness: generated bases).
- 2026-10-10T22:59:56Z — `b7b_generic.py` run 1: Z1 FAIL, Z2 PASS, Z3 PASS → VERDICT B7B-FAILED Z1. `G1[0]` came out
  with 2 product lines where the generator design expected 1. Recorded as is; no edit, no re-run. The certificate
  passed on all 12 bases and the countercontrol at all 13 product vertices. Replay byte-identical (23:00Z).
  NOTES-B7 §6 and RESULTS row B7-5 added.
- 2026-10-10T22:58:58Z — run 38092042844: Mathlib bridge job started (monitor); Build in progress at 23:00Z.
- 2026-10-10T23:01:27Z — run 38092042844, Mathlib bridge job 114330283929: **Build success** (started 22:59:12Z);
  Release gate in progress at reading time.
- 2026-10-10T23:01:40Z — dev commit 3 bbbefb72 (child of f1c5f0fb): adds `verification/lean-mathlib/OIBridge/
  BridgeDictionary.lean` (blob 119d85ba, verbatim copy of `lean/BridgeDictionary.lean`) and one more root import line
  (`import OIBridge.BridgeDictionary` after `BridgeLemma`). Dispatch 3 of 3 at 23:01:42Z: run 38093576860. The B6
  evidence is run 38092042844; run 3 bears only on the dictionary (B9).
- 2026-10-10T23:02:04Z — run 38092042844 complete, read via the jobs API and the job log. Mathlib bridge job
  114330283929:
  - Build **success** 22:59:12–23:01:10Z ("Build completed successfully (3644 jobs)"; `Built OIBridge.BridgeLemma`
    with warnings only: unused variables in `hpush`'s `rfl` fields, unexecuted fallback alternatives);
  - all 14 `#print axioms` lines of the module on [propext, Classical.choice, Quot.sound];
  - Release gate: `lean-axioms` **PASS** ("OK (5874 named result(s) reported, no sorr…"); FAIL only on `claims`,
    `duplicate`, `lean-manuscript` (1 problem), red by construction.
  B6 is [D]. NOTES-B6 §4 filled; RESULTS rows B6-1 and V-2 appended; NOTES-B9 §2's forward reference to B6 updated.
- 2026-10-10T23:03:07Z — run 38092042844: at 23:03Z 21 jobs completed (Lean kernel check success; Mathlib bridge as
  recorded), 11 numerical-probe shards still running. Remaining jobs cancelled to free runners for the other threads'
  queued dispatches. The cancelled jobs do not bear on B6. Not a dispatch.
- 2026-10-10T23:04:37Z — run 38093576860 (dispatch 3 of 3), Mathlib bridge job 114334767486:
  - **Build failure** 23:02:28–23:04:23Z; Release gate skipped.
  - `BridgeDictionary.dict_tens`: after `simp only [… Finset.sum_mul, Finset.mul_sum]` the right-hand double sum was
    nested with the second factor's index outside; the termwise `ring` failed. The `first` fallback did not run,
    because the error inside `exact (… by ring)` was recovered during elaboration. So `dict_tens` and
    `dict_prodState` print `sorryAx`.
  - `monomial_extension_admissible` built on the standard axioms. BridgeLemma rebuilt with all 14 axiom lines
    standard.
  - Dispatches used: 3 of 3. The dictionary stays a draft (RESULTS B9-5, OPEN). An untested fix is described in
    NOTES-B9 §4. The research copy `lean/BridgeDictionary.lean` is kept equal to the dispatched text.
  - Lesson recorded: a tactic error inside `exact (… by tac)` does not trigger `first`'s fallback.
- 2026-10-10T23:05Z — run 38093576860's remaining probe jobs cancelled (as for runs 1 and 2; they do not bear on this
  thread's work).
- 2026-10-10T23:05:23Z — HP-6 corrected to the measured dictionary outcome (draft did not build). NOTES-B6 §1 gains a
  one-line note on the `Pd` naming.
- 2026-10-10T23:05Z — closing, round 2. Nodes B6–B9 done:
  - B6: Theorem B1.1 [D], CI run 38092042844 green; both forms, local tomography proved, positive control and
    countercontrol.
  - B7: B3.C proved in all open cases, CONDITIONAL on claim (D) [A]; b7 13/13. Robustness run b7b recorded as
    FAILED Z1 (generator design), with Z2/Z3 PASS.
  - B8: HO-4 tested. The excluding clause is family membership; its matrix form is certified independent of the
    sealed core; Stab_loc(K(Z_F)) = V4. b8 4/4.
  - B9: transfer needs (D1), (D2) exact and (T) = (b) for the monomial images. The reduction to SPEC_P(J) is a
    relocation; SPEC_P(J) with H2 ⟺ (b) for the native Clifford family. b9 7/7. The dictionary draft did not build.
  Dispatches: 3 of 3 (runs 38090784384, 38092042844, 38093576860).
  Deviations, all recorded above:
  - one root import line per module on the dev branch (outside OIBridge/);
  - estimate-based timestamps corrected forward (B8 entry at 22:45Z) or before use (b9 header 22:48Z, LOG 22:52Z,
    the 22:50Z draft entry);
  - b9 Y2's message text "as transcribed" for parsed tables;
  - b7b's Z1 generator defect;
  - cancellation of the leftover probe jobs of all three runs.
  Inbox: HO-4 v1, HO-5 v1, HO-6 v1, received in e29b6a42.

## Round 3

- 2026-10-10T23:47:37Z — round 3 opened at thread head 3686049e (clean, up to date with origin). Read, in order:
  README.md, RESULTS.md, LOG.md, NOTES-B1 … NOTES-B9 (own record); research/OVERVIEW.md, the handoffs HO-9, HO-12,
  HO-13, HO-16, HANDOFFS/README.md and AUDIT-BRIDGE-R2.md on research/overview @ 2a055180 (read-only); AGENTS.md at
  L 9f9f8257 (§A.16, §A.21, §A.29, §A.31; identical to the read-only main checkout). Kernel reading at L for this
  round: CompositionOrder.lean (§A, §B `StagePreserving` :234, §D :348, :378), CompletionAction.lean (`OpDatum` :46,
  `AffineRespect` :58), KInfFoundations.lean (`rotFun` :351, `rotLin` :386, `rotEquiv` :400, `rot3` :411,
  `cycEquiv` :416, `ball3Drive` :449), CompositeDimension.lean (§A, §K), MonoidalCompletion.lean (`tensorOf` :193);
  Main.md:536–566 (the realization theorem: statement :544, clauses (1)–(5) at :546–:554, proof :558, remark :562);
  GR.md:228 (OI⁺-1); research/archive/pt/I3/INVENTORY.md I3.150–I3.170.
- 2026-10-10T23:55:08Z — receipts. Copied from research/overview @ 2a055180 `research/HANDOFFS/` into `inbox/`,
  byte-identical (cmp), sha256:
  - HO-9 v1 (origin → bridge, equivalence) `4b2c4a0f708e7ec5dda179002c88a71fca15f3d815bfa7c167a8261b3b7b6860`;
  - HO-13 v1 (equivalence → bridge, origin) `1d2c884cdbb8f88adbd5ec9f5d74520de4273c0a23863b3c14b3ea80d464de2e`;
  - HO-16 v1 (countermodels → bridge) `bd5a7af392275ebed5e817c104a20ea89f56e3356390eb3d772f9519450d4dfa`.
  HO-12 is this thread's own result (source), not copied. Kernel declarations named in the handoffs, checked at L
  before any use: CompositionOrder.lean:348 `finiteOrderOn_of_stagePreserving`, :378
  `not_stagePreserving_of_infiniteOrderOn`; OperationalAssembly.lean:658 `readout_is_localLuders`, :675
  `pureSeedPrep_available_of_swap` — all four resolve at those lines. These are the only CERTIFIED items the
  handoffs carry; everything else in them is used at its own label.
  Reliance:
  - **HO-9.** Relied on in B12 only. Item 3 (on a passive repeatable finite-rank tower every reversible datum has
    finite order) at its label CONDITIONAL; its stage-crossing clause is the kernel theorem CompositionOrder.lean:378,
    which I cite directly. Item 6 (SRC via KB-D is token-only: product-register composites are Bell-local) as a
    constraint on what a stage-crossing pair substratum may use. Items 1 and 5 as the current form of Origin's open
    premise (context only). Item 4 (the invasive re-preparing tower) is context, not a premise. Item 7 is not relied
    on. Not assumed: that KB-D, the re-preparing law or SRC is sourced; kernel status for the [D] declarations.
  - **HO-13.** Relied on in B10 and B12. Item 2 (in the schema H1 + H2 + H3, invariance under `R_z(θ₀)`,
    `cos θ₀ = 3/5`, and `J = cyc3` on one token suffices) at its label CONDITIONAL; it fixes the target clause of B10
    ((T) at one rational angle). Item 1 (the K2 schema's written proof) at CONDITIONAL, used only to say what the
    conjunction of the two halves forces. Item 3 (the finite clause, order 384) as context. The facts I use from it
    (the trace and infinite order of `R_z(θ₀)`, the irrationality of `θ₀/π`) are recomputed in my own scripts.
    Not assumed: that H2, H3, (b) or either operation is sourced; that lemma 4 is kernel-checked.
  - **HO-16.** Not relied on as a premise in B10–B12. Used as context in B10/B12 only to note where its eigenline-orbit
    mechanism does not apply (an identity component whose eigenlines are all products), and in B13 (if reached) for
    comparison. Not assumed: B3.C from it; EBF certified.
- 2026-10-11T00:00:28Z — receipts commit 0ccc1bef pushed (remote head verified equal). Disk check: 7.3 GB free on a
  shared container, no elan/lake; a local Mathlib install is again not attempted (the round-2 decision stands).
  B10 design decision: the target is (T)θ₀ (one token, `actT R_z(θ₀)` and `actT nflip`). The premise is tested in
  NOTES-B1's vocabulary only. B4's machine is copied from `b4_realization.py`, with its 129-table closure as a replay
  control. The Bloch image of the realization theorem's own 3-4-5 rotation is read from opglue_probes.py in this tree,
  which is identical to L (`git diff 9f9f8257 HEAD -- verification papers book` is empty). NOTES-B10 opened with the
  productivity test and the S0 table at 00:00:28Z, before any run.
- 2026-10-11T00:01:41Z — `b10_transfer.py` decision rule written. Pre-run edit at 00:03:56Z, logged in its header (T7
  reads the three traces off the matrices); rule text unchanged.
- 2026-10-11T00:04:05Z — `b10_transfer.py` run 1: 10/10 PASS, VERDICT B10-EXACT (00:04:22Z). Replay byte-identical
  (00:04:42Z). All S0 predictions held, including the guessed value `−2/5` for `actT`.
- 2026-10-11T00:08:06Z — NOTES-B10 §1–§7 written; RESULTS round-3 section opened with rows B10-1 … B10-7. Kernel
  lines re-checked at L before citing: OIRealization.lean:360, SpectatorBridge.lean:223/:233,
  ReferenceExtension.lean:447, StructuralClosure.lean:261, CompositeDimension.lean:97/:198/:201/:1220,
  CompositionOrder.lean:348/:378. B10's verdict:
  - H-T (one infinite-order frame-axis rotation's (A), with (W) and (P), plus the NOT) is the weakest premise;
  - the disguise test FAILS;
  - H-T is strictly weaker than H-OI_g, CONDITIONAL on claim (D);
  - the continuous half is locally finite;
  - B4 fails H-T at (A) alone.
- 2026-10-11T00:08:30Z — commit 5596c0ca (B10) pushed; remote head verified equal.
- 2026-10-11T00:28:49Z — B11 opened. NOTES-B11 S0 (success criterion, design decisions, predictions) written
  before any run or dispatch.
  - No local Lean is possible: the agent proxy's status log shows `lakecache.blob.core.windows.net` (Mathlib's olean
    cache) denied with a 403 at 00:01:10Z, from another process. Not retried by this thread.
  - Mathlib names are therefore checked against the pinned tag `v4.33.0` (lakefile.toml), read from
    raw.githubusercontent.com into the session scratchpad: Kronecker.lean (`mul_kronecker_mul`,
    `conjTranspose_kronecker`, `kronecker_add`, `kronecker_smul`, `add_kronecker`, `smul_kronecker`), Tactic/Module.lean,
    Data/Matrix/Mul.lean (`smul_mul`, `Matrix.mul_smul`, `mul_apply`), LinearAlgebra/Matrix/Defs.lean (`add_apply`,
    `smul_apply`), Data/Matrix/Diagonal.lean, ConjTranspose.lean, Data/Complex/Basic.lean (`I_sq`, `ofReal_*`,
    `star_def` simp), Fintype/BigOperators.lean (`Fintype.sum_prod_type`), Ring/Finset.lean (`mul_sum`, `sum_mul`).
  - The kernel at L already uses the same Kronecker rewrites (AncillaInterference.lean:123, ClosureObstruction.lean:282)
    and `set_option maxHeartbeats 1000000` (InstrumentAvailability.lean:72).
  - New names checked for clashes at L: none. `phaseU` exists in OperationalSourcing and QuasilocalCharacterization,
    so the phase is named `zPhase`.
- 2026-10-11T00:29:05Z — `b11_preflight.py` decision rule written. Run 1 (00:29:59Z): 10/10 PASS, VERDICT
  B11-PREFLIGHT-OK. Replay byte-identical (00:30:06Z). Every statement of the planned module is true under the
  kernel's conventions, including the countercontrol off the circle.
- 2026-10-11T00:38:04Z — module `lean/BridgeDictionary.lean` written for round 3 (sha256 48fc4a7e…).
  - The round-2 draft is preserved verbatim as `lean/BridgeDictionary.round2-draft.lean` (sha256 e4b60411…, cmp-equal to
    the dispatched dev blob at bbbefb72), so B9-5's pointer stays resolvable.
  - Proof design: the circle hypothesis is isolated in `zPhase_pauli0`/`zPhase_pauli3`, with `linear_combination`
    certificates tried in a `first` list. Every fallback alternative ends in `ring1`, which fails when the goal stays
    open (a `ring` that falls back to `ring_nf` would not trigger `first`'s next branch). The pair identities go
    through `conj_dict_right`/`conj_dict_left` and `module`. `dict_cnot` is entrywise.
- 2026-10-11T00:38:46Z — dev branch `dev-bridge/r3-dict` created and pushed with git plumbing (a temporary index;
  the research worktree and index untouched). Dev commit 3d554e7e, child of research/bridge 7fd01094. It adds
  `verification/lean-mathlib/OIBridge/BridgeDictionary.lean` (blob fece97f4, a verbatim copy of
  `lean/BridgeDictionary.lean`) and one import line in the root `verification/lean-mathlib/OIBridge.lean`, after
  `RelcSelectC5`. Deviation, as in rounds 1–2: the root file is outside `OIBridge/`, and the lake library builds
  only modules reachable from it. The branch is cut from research/bridge (its tree contains `research/archive/`).
- 2026-10-11T00:38:46Z — **dispatch 1 of 3**: `verify.yml` on `dev-bridge/r3-dict`, run 38099134414 (queued
  00:38:50Z, head 3d554e7e). At about 00:43Z, read through the jobs API: Mathlib bridge job 114351216052 has
  **Build success** (00:39:40–00:42:00Z); the Release gate is in progress. No job is cancelled (round-3 rule).
- 2026-10-11T00:44:30Z — run 38099134414 read via the jobs API and the job log (GitHub MCP job-log reader; the built-in
  `gh` again refuses the log host redirect). Mathlib bridge job 114351216052: **Build success** (00:39:40–00:42:00Z;
  "⚠ [3642/3644] Built OIBridge.BridgeDictionary (23s)", warnings only; "Build completed successfully (3644 jobs)").
  All 20 module `#print axioms` lines are on [propext, Classical.choice, Quot.sound]. Release gate (00:42:00–00:42:52Z):
  `lean-axioms` **PASS** (5880 named results, no sorry); FAIL only on `claims`, `duplicate`, `lean-manuscript` (by
  construction). Job conclusion "failure", from the gate only. The other jobs of the run were left running; none
  cancelled. Dispatches used: 1 of 3.
- 2026-10-11T00:45:30Z — NOTES-B11 §1–§3 written. RESULTS rows B11-1 and B11-2 appended. B11's verdict: (D1) and (D2)
  are [D]; the pull-back of (T) is formal modulo dictionary injectivity; gem classification ELABORATING (a
  formalization; the preflight and the build agree).
- 2026-10-11T00:45:30Z — B12 opened. NOTES-B12 §0 and S0 (productivity test, predictions S0-1 … S0-8) written before
  any run.
- 2026-10-11T00:46:30Z — `b12_stagecross.py` decision rule written. Pre-run edit at 00:48:22Z, logged in its header
  (U4 obtains the quadratic factor by division by `x − 1`, remainder checked); rule text unchanged.
- 2026-10-11T00:48:32Z — `b12_stagecross.py` run 1: 8/8 PASS, VERDICT B12-EXACT (00:48:32–00:48:36Z). Replay
  byte-identical (00:48:46Z). `⟨cnot, actT J⟩` has order 48; `G₁ = Stab_C(Z ⊗ 1)`, order 384; `|Λ₀| = 60`,
  `|Λ₁| = 588`; the guessed U8 value `−1/2` held.
- 2026-10-11T00:50:27Z — NOTES-B12 §1–§6 drafted.
- 2026-10-11T00:56:00Z — review of the draft, before commit. Two defects found:
  - S0-5's check column names `m = 1 … 24`, but the decision rule (00:46:30Z) and run 1 cover `m = 1 … 16`;
  - a draft sentence of §3 ("the octahedral group is the largest finite stage holding `J` and a `z`-rotation") is
    contradicted by the icosahedral group, which contains `T = ⟨J, R_z(π)⟩`.
  NOTES-B12 S0′ (predictions S0′-1 … S0′-3) written before the follow-up's first run.
- 2026-10-11T00:56:10Z — `b12_followup.py` decision rule written. Run 1 (00:57:14–00:57:15Z): 3/3 PASS, VERDICT
  B12F-EXACT. Replay byte-identical (00:57:18Z). `m = 17 … 24` checked, with a positive control (`2 cos(2π/m)`) and a
  countercontrol (`cos(2π/m)`, integral exactly for `m ∈ {1, 2, 4}`); `|⟨J, R_z(π), R_u⟩| = 60`.
- 2026-10-11T00:59:02Z — NOTES-B12 revised from the follow-up:
  - §3 now states what the certificate proves (every finite rotation group holding `J` has `z`-rotations of order
    1, 2 or 4 only) in place of the false draft sentence;
  - §2 and §6 now credit the single-generator obstruction to B10-5 and classify it ELABORATING;
  - §4 gains the determinant-ratio step that makes the identity component exactly `SU(2) × SU(2)`.
  RESULTS rows B12-1 … B12-5 appended. CompositionOrder.lean:348/:378 re-checked at L before citing. B12's verdict:
  NEW (i) the stabilizer identification and the `SU(2) × SU(2)` closure; NEW (ii) the `z`-rotation bound for finite
  groups holding `J`.
- 2026-10-11T00:59:02Z — forward correction of two B11 entries above. Their stamps were not `date -u` readings: both
  entries were appended by one command whose `date -u` read 00:45:20Z.
  - The entry stamped 00:44:30Z: the run was read between the readings 00:43:37Z and 00:44:56Z.
  - The entry stamped 00:45:30Z (later than its own append time): NOTES-B11 §1–§3 were written by the 00:44:56Z
    reading, and RESULTS B11-1/B11-2 and the two entries were appended at 00:45:20Z, before commit 3d7b23b8.
  The entries are not edited.
- 2026-10-11T01:09:22Z — B13 opened. NOTES-B13 S0 (success criterion, reading of "finite cases" as the case of a
  finite group, design, productivity test, predictions S0-1 … S0-4) written before any run or dispatch.
  - Mathlib names checked against the pinned tag `v4.33.0`, read from raw.githubusercontent.com into a new, empty
    scratchpad directory: Algebra/Star/Unitary.lean (the namespace is `Unitary`, e.g.
    `Unitary.mul_star_self_of_mem`), LinearAlgebra/UnitaryGroup.lean (`Matrix.mem_unitaryGroup_iff`),
    Combinatorics/Pigeonhole.lean (`Finset.exists_lt_card_fiber_of_mul_lt_card_of_maps_to`), Data/Finset/Card.lean
    (`two_lt_card_iff`, `card_range`), Data/Finset/Insert.lean (`Finset.induction_on`, `@[elab_as_elim]`, explicit
    insert binders), Data/Matrix/Mul.lean (`mulVec_mulVec`, `mulVec_add`, `mulVec_smul`, `one_mulVec`,
    `zero_mulVec`, `mulVec_zero`, all `@[simp]` where used by `simp`; `*ᵥ` is scoped in `Matrix`),
    Data/Fin/VecNotation.lean, Data/Set/Finite/Basic.lean, Data/Finite/Defs.lean (`Set.Infinite := ¬ s.Finite`),
    Algebra/Star/Basic.lean (`starRingEnd_self_apply`), Tactic/Push.lean (`push_neg`).
  - The kernel at L uses the same patterns: `induction s using Finset.induction_on with | empty | insert a s ha ih`
    (ClosureObstruction.lean:133), `Matrix.mem_unitaryGroup_iff` (BarandesTuple.lean:445), topology on
    `unitary (Matrix S S ℂ)` (PositiveReachability.lean:963), `push_neg at` (DitaHull.lean:573).
  - No declaration of the new module's names exists at L; there is no file `OIBridge/BridgeReach.lean`.
- 2026-10-11T01:09:57Z — `b13_preflight.py` decision rule written. Run 1 (01:10:34Z): 7/7 PASS, VERDICT
  B13-PREFLIGHT-OK. Replay byte-identical (01:10:41Z). Every algebraic statement the module relies on holds under
  its conventions. The module's induction, run exactly on 8 instances (6 unitary, 2 antiunitary), ends at
  `v = (2, 0, 1, 1)`.
- 2026-10-11T01:20:49Z — module `lean/BridgeReach.lean` written for B13.
  - Proof design: the elaboration-sensitive steps carry fallbacks in `first` lists, each alternative ending in
    `done` so that a partial `simp` falls through. These are `prodDet_bellV` (three alternatives) and the two
    conjugation lemmas (`simp only` with named lemmas, then `simp`).
  - Goals with beta-redexes are restated with `show` before `rw`. The `v ≠ 0` steps use one `simp [h0, prodDet]`
    instead of `rw` followed by `simp`.
- 2026-10-11T01:21:56Z — dev branch `dev-bridge/r3-reach` created and pushed with git plumbing (a temporary index in
  the scratchpad; the research worktree and index untouched). Dev commit 747bcf94, child of research/bridge 7266e30b.
  It adds `verification/lean-mathlib/OIBridge/BridgeReach.lean` (blob 7a279393, cmp-equal to
  `lean/BridgeReach.lean`, sha256 a6e055e4…, the module as dispatched) and one import line in the root
  `verification/lean-mathlib/OIBridge.lean` after `RelcSelectC5` (root blob a9981951). Deviation, as in rounds 1–3:
  the root file is outside `OIBridge/`, and the lake library builds only modules reachable from it.
- 2026-10-11T01:22:01Z — **dispatch 2 of 3**: `verify.yml` on `dev-bridge/r3-reach`, run 38101591388 (created
  01:22:01Z, head 747bcf94). Mathlib bridge job 114358450003, queued at 01:22:08Z. Waiting through the jobs API; no
  job is cancelled.
- 2026-10-11T01:26:30Z — charter deviation found and checked. The charter runs every script as `python3 -I -B`;
  `b10_transfer.py`, `b11_preflight.py` and `b12_stagecross.py` were run that way. `b12_followup.py` (run 1 and
  replay) and `b13_preflight.py` (run 1 and replay) were run as plain `python3`. A third run of each with
  `python3 -I -B` (01:26:28–01:26:30Z, outputs kept in the scratchpad only) is byte-identical to run 1, on `.out`
  and `.err`. The recorded outputs do not depend on the flags; the files are kept as they are.
- 2026-10-11T01:27:10Z — handoff proposals HP-7 (B10: the transfer clause at one rational angle, H-T), HP-8 (B11:
  the dictionary design module) and HP-9 (B12: the finite half as `Stab_C(Z ⊗ 1)`, the `z`-rotation bound, the
  `SU(2) × SU(2)` closure, B12-S) written under `handoff-proposals/`. Each states labels, evidence pointers and what
  the recipient may not assume. NOTES-B13 §1 (what the module states) written while run 38101591388 is queued
  behind run 38101580750 of another thread (16 jobs in progress).
- 2026-10-11T01:28:50Z — final state of run 38099134414 (B11, dispatch 1), read through the jobs API: completed
  01:03:02Z, head 3d554e7e. 33 jobs: 32 success, 1 failure, the Mathlib bridge job 114351216052, through its release
  gate (`claims`, `duplicate`, `lean-manuscript`, by construction). "Lean kernel check" success (00:42:56–00:43:41Z).
  Every numerical-probe shard success; the aggregate "Numerical probes" success at 01:03:01Z. No job of the run was
  cancelled.
- 2026-10-11T01:32:09Z — closing replay (§A.26). All five round-3 scripts, re-run with `python3 -I -B`
  (01:31:42–01:32:09Z, outputs in the scratchpad only), are byte-identical to their committed `.out` and `.err`:
  `b10_transfer`, `b11_preflight`, `b12_stagecross`, `b12_followup`, `b13_preflight`.
- 2026-10-11T01:36:52Z — run 38101591388 (dispatch 2 of 3, B13), Mathlib bridge job 114358450003, read through the
  jobs API and the job log (GitHub MCP job-log reader). The job started at 01:33:55Z after waiting in the queue.
  - **Build success** (01:34:13–01:36:15Z): "⚠ [3644/3646] Built OIBridge.BridgeReach (1.7s)", warnings only, then
    "Build completed successfully (3646 jobs)".
  - All 21 module `#print axioms` lines (module lines 355–375) are on [propext, Classical.choice, Quot.sound].
  - Release gate (01:36:15–01:36:47Z): `lean-axioms` **PASS** (5881 named results, no sorry); FAIL only on `claims`,
    `duplicate`, `lean-manuscript` (by construction). A local census run on the exported dev tree names the one
    problem: "UNCLASSIFIED module BridgeReach has no registry family".
  - Job conclusion "failure", from the gate only. "Lean kernel check" success (01:34:19–01:35:04Z).
  - At 01:38:58Z the run is in progress: 24 jobs success, 1 failure (the bridge job's gate), 7 numerical-probe shards
    running, left to finish. No job cancelled. Dispatches used: 2 of 3.
- 2026-10-11T01:38:58Z — NOTES-B13 S0 outcome (S0-1, S0-2, S0-4 held; S0-3 did not arise), §2 (CI record) and §3
  (reading and verdict: ELABORATING) written. RESULTS rows B13-1 (CONJECTURE, [D]) and B13-2 (CONDITIONAL on claim (D)
  [A]; evidence-level propagation to B7-4, label unchanged) appended, with the standing verdict V-3. Handoff proposal
  HP-10 (B7-1's formal statement and finite case) written. The dispatched module is unchanged (`lean/BridgeReach.lean`
  sha256 a6e055e4…, cmp-equal to the dev blob 7a279393).
- 2026-10-11T01:39:30Z — **round 3 closing.**
  - **Nodes done.** All four:
    - B10, commit 5596c0ca;
    - B11, commits 7fd01094 and 3d7b23b8;
    - B12, commit 69fbbc53;
    - B13, commits 7266e30b and fdc8e8ac.
  - **Recorded output.** RESULTS rows B10-1 … B10-7, B11-1, B11-2, B12-1 … B12-5, B13-1, B13-2 and the standing
    verdict V-3; no earlier row edited. Handoff proposals HP-7 … HP-10.
  - **Dispatches used: 2 of 3.** Both builds succeeded on the first try:
    - run 38099134414 (`dev-bridge/r3-dict` @ 3d554e7e, Mathlib bridge job 114351216052);
    - run 38101591388 (`dev-bridge/r3-reach` @ 747bcf94, Mathlib bridge job 114358450003).

    No CI job or run was cancelled in round 3.
  - **Deviations, each recorded above.**
    - Each dev branch adds one import line to the root `OIBridge.lean`, outside `OIBridge/`.
    - Two B11 LOG entries carried estimated stamps; they are corrected forward (00:59:02Z) and not edited.
    - Two pre-run edits, logged in the script headers: b10 T7 (00:03:56Z) and b12 U4 (00:48:22Z).
    - B12's S0-5 named `m ≤ 24`, but its rule checked `m ≤ 16`; the follow-up `b12_followup.py` checked the rest.
    - A false draft sentence of NOTES-B12 §3 was replaced before commit by what the certificate proves.
    - `b12_followup.py` and `b13_preflight.py` were run without `-I -B`; their re-runs with the flags are
      byte-identical.
    - The charter names `dev/bridge/<topic>`; the round-3 directive's `dev-bridge/<topic>` was followed.
  - **Governance.** Round-3 commits on `research/bridge` change only `research/bridge/`; `git diff --stat
    3686049e..HEAD` outside it is empty. `main`, manuscripts, `verification/` on the research branch, receipts,
    seals and legacy records are untouched. No pull request was opened and nothing was posted on GitHub.

## Round 4

- 2026-10-11T02:45:43Z — round 4 opened at thread head 7abe4da4 (clean, equal to origin). Own record re-read: README.md,
  LOG.md, RESULTS.md, NOTES-B1, NOTES-B3, NOTES-B7, NOTES-B10 … NOTES-B13. Read-only reads of the coordinator's branch
  research/overview @ 742c6b2f (as in rounds 2–3; cross-branch read on the coordinator's instruction), sha256 of what
  was read:
  - research/AUDITS/2026-10-11-round3/AUDIT-BRIDGE-R3.md `9f60a7b3690b43e2cab96f63d976c39000caff159c7e3c62340c2b8b7b042579`
    (the round-3 audit: no label changes);
  - research/OVERVIEW.md `c3ca2beae5ca2fcad60c0488abd6a3dfcbcecc4bcd390f9e4cf33eb07404c9f6` (§ "Next round (round 4)",
    the nodes B14–B17);
  - research/HANDOFFS/HO-20 … `f36b244824f1f096ed1bd554047bf2b7d24c3f27bb3e85e67f6e7784a2857497` and HO-23 …
    `3c1e126d889b2ff9734da4432f212ca074b2ec74291570c8e3a0398af4c0f3ae`: this thread's own round-3 results as routed,
    read only for their item numbering (B14 names HO-20 item 3). Not copied: they are not addressed to this thread.
- 2026-10-11T02:51:26Z — receipts. Copied from research/overview @ 742c6b2f `research/HANDOFFS/` into `inbox/`,
  byte-identical (cmp against `git show 742c6b2f:…`), sha256 equal to the overview blob:
  - HO-9 v2 (origin → bridge, equivalence) `bd62649d0b7eb594046d5da6ce8bf5de4f70dbdd43000445e98315c035bb7b44`;
  - HO-17 v1 (origin → bridge, equivalence, countermodels) `65d2f79a0421b1b15162603114febae17c0452c792699303b2953db4724bf3a6`;
  - HO-18 v1 (equivalence → bridge, countermodels) `df704843343310fb16ed1eac29564ca5091ce1a3225d3796ec185d8c6b6731ed`;
  - HO-19 v1 (equivalence → countermodels, bridge) `ad17f101a560674b437d170dce8b7c776da59a00021fbc990979d73093a3184b`;
  - HO-24 v1 (countermodels → equivalence, bridge) `27175857ac88aac878afdd50f124b5b532a9429d377bf5575169670a56bc688b`;
  - HO-25 v1 (countermodels → bridge, equivalence) `9341f3f3df33fdd2766b8b506a40f4bfb9465e95851bb26b326e27f985d7c437`.

  HO-9 v1 stays in `inbox/` (received 0ccc1bef); v2 supersedes it. Nothing in these handoffs is CERTIFIED except the
  kernel lines they cite; every item is used at its own label. The "may not assume" sections of all six are honoured.
  Reliance, handoff by handoff and item by item:
  - **HO-9 v2.** Items 1–6 are unchanged from v1 and relied on as in round 3. Item 3 at CONDITIONAL in B14 (a passive
    finite-rank tower carries no infinite-order datum); its stage-crossing clause is CompositionOrder.lean:378, cited
    directly. Item 6 as a constraint: product-register composites are Bell-local. Items 1 and 5 as context: the current
    form of Origin's open premise. Item 4 is context, not a premise. Item 7's density facts are not used. Its corrected
    may-not-assume clause is honoured: availability at a level is not the group generated at that level.
  - **HO-17 v1.** Items 1, 3 and 5 (addressed to this thread) are constraints in B14:
    - item 1: the exclusive readout is not a source inside the kernel's operational structure; refuted on the stated
      access ([D] there; the kernel facts OperationalAssembly.lean:658 and :675 are re-checked at L before any citation);
    - item 3: its disguise-test reading, as context for B14's own disguise test;
    - item 5: no re-preparing pair law short of the cone's own conditioning rule, with `cnot` given, realizes a
      candidate cone.

    **Item 8 binds every availability argument of this round.** Availability at a level includes the ancilla blocks
    `MixR.block` and the relabellings `MixR.relabel` of members at every level, and every `InstAvail` protocol. B14's
    predicate is stated over exactly that availability, never over a generated group. Item 4 (HO-13's token pair on
    one re-preparing token, CONDITIONAL on the cosine law) is context for B14's token side only. Items 2, 6 and 7 are not
    relied on. Not assumed: that the exclusive readout, the re-preparing law, SRC or SPEC is sourced; kernel status for
    the [D] items.
  - **HO-18 v1.** Relied on in B15:
    - item 1 at CONJECTURE ([D] run 38101580750): `dictEquiv`, `dict_injective` and their supporting lemmas as Lean
      text that builds against Mathlib v4.33.0 and the kernel at L, on the same definitions `pauli`, `tokMat`, `dict`;
      the text itself comes from the authorized read of `EqvK2Schema.lean` at c10dbaee (logged when made);
    - item 5 as the convergence target;
    - item 4 as a build-time fact about the one-list rendering only.

    Items 2 and 3 (the cone lemmas, the schema) are context only. Not assumed: certification; that the schema
    formalizes HO-13 item 2's two-rotation clause; anything beyond two tokens.
  - **HO-19 v1.** Not relied on as a premise. Recorded as a constraint: no round-4 argument sources K∞-Trans through
    self-duality. If one arose, item 3 (strong self-duality, not duality alone) is the obstruction it must clear.
  - **HO-24 v1.** Relied on in B17:
    - item 4 (`h*`, `c* = 401/400`, the 192-defect orbit) at CONDITIONAL;
    - item 1 (the Gaussian-rational lift of `G₃₈₄ = Stab_C(Z ⊗ 1)`), re-derived in my own script before use;
    - the (CC) and H1 tests as exact design rules.

    Item 3 (Theorem S′, [W]) only where a B17 statement needs self-duality of the cone; a non-invariance certificate
    that uses only `K ⊆ K*` (pairwise defect pairings `≥ 0`, checked exactly) does not rest on it. Item 6 is recorded
    as the cone step of B7-4's fixed-finite case for unitary groups containing `cnot` (an explicit surgery, CONDITIONAL
    on Theorem S′ [W], instead of claim (D) [A]); any RESULTS propagation is stated there with its label. Item 5 is
    context.
  - **HO-25 v1.** Context for B17:
    - item 2 (for the continuous half's group the rank-one surgery route is closed; existence there by claim (D) only);
    - item 3 (Lemma C13-O, [W]) at its label, if B17's reading uses it;
    - item 1 as the cone side of the Clifford half (B10-4's "leaves exotic cones" for that half, now explicit through
      Theorem S′ [W]).

    Item 4 is context. Not assumed: that S′ or C13-O is kernel-checked; that the continuous half's exotic cones exist
    other than through claim (D).
- 2026-10-11T02:52:11Z — B14: cross-branch read on the coordinator's instruction (authorized for B14 only, as a model
  of the statement style): `git show de9285d6:research/origin/lean/OriginExclusive.lean`, blob 28776414, sha256
  `a8eb5802c9c6e7bd2164a3f1e0b5b55da4f4925e17930d4b4f848d9ad66869a8` (equal to the value the directive names). Saved
  to the session scratchpad only; nothing of it is copied into this branch.
- 2026-10-11T03:09:18Z — NOTES-B14 opened: question, design, productivity test and predictions S0-1 … S0-10, before any
  run or dispatch.
- 2026-10-11T03:10:16Z — `b14_preflight.py` decision rule written. Pre-run edit at 03:11:13Z, logged in its header (P1
  compares `w⁴` by expanding the difference); rule text unchanged.
- 2026-10-11T03:11:19Z — `b14_preflight.py` run 1: 8/8 PASS, VERDICT B14-PREFLIGHT-OK. Recording defect: `.err` lacked
  the `exit N` line of the thread's convention. Run 1's outputs kept as `b14_preflight.run1.out/.err` (no `.run1.py`:
  the script is unchanged). Run 2 (03:11:54Z) with the convention: stdout byte-identical to run 1; replay
  byte-identical (`.out` and `.err`). A diagnostic of the P5 sampler, kept in the scratchpad only (not a record): of 300
  sampled words, 38 have more than one distinct nonzero entry and 191 a non-real entry, and a `diag(1, w, 1, 1)`
  insertion fails `QuartEq`; so P5's closure check is not vacuous.
- 2026-10-11T03:24:47Z — coordinator addendum received (owner's round-4 directions; node list and order unchanged).
  Recorded and applied from here on:
  - priority: B14–B15 first (with origin O11), then the other threads' nodes, then B16–B17;
  - B14's record must name either the inventory items a derivation of (A)/H-T uses, or the items a countermodel
    satisfies while (A) fails;
  - standing rule 1 (derive, do not introduce): every result lists its hypotheses, each classified as an item of the
    OI premise inventory at its status at L (cited by inventory id) or as an introduced hypothesis; "OI ⇒ X" only
    when all are inventory items, otherwise "OI + {named hypotheses} ⇒ X" with each flagged "introduced, not an OI
    premise" in the RESULTS row;
  - standing rule 2: the stage-6 premise inventory is the reference point;
  - standing rule 3: the evidence layers [D], [W], [K] and CERTIFIED are kept apart.
- 2026-10-11T03:30:29Z — inventory reads, authorized by the addendum (cross-branch read on the coordinator's
  instruction; the same blobs are also in this branch's `research/archive/`, inherited from 4dc0321c). All read with
  `git show 4dc0321c:…`; sha256 of what was read:
  - research/archive/pt/I4/INVENTORY.md `43bbada1db14f052e3ec3eb3d7fc99d1bb042d41a143c912aa6ca3e4cad75461` (equal to
    the addendum's value; its own render-control line reads "records 248", so the addendum's "633 records" is taken
    to count I1–I4 together);
  - research/archive/pt/I4/INVENTORY-HEADER.md `02c431ff5dd5ee68892128aa3162c48de78814edb3690ae2c98900e22cf0eb07`;
  - research/archive/pt/G6/GRAPH.md `83f4619f48982f881e43b0a19c14b7c6cc182179ea2a3c69dcf5992c4aab342c` (hash taken;
    read only where cited);
  - research/archive/pt/R6/REASSESSMENT.md `1ff62ad633fbd752f247d49b605e6cc8d984e23d8b7151b6497cdd60fa884ffe`
    (Table A2 and the rows above it, lines 255–340);
  - research/archive/pt/INTEGRATION-NOTE-STAGE6.md `1130a8c5e72e03503ebd8c6183b468dfadc8ebe813bfc857bc21f6262bcf0e6b`
    (hash taken; read in round 1);
  - the other three inventories, for the I1/I2/I3 numbering the addendum requires:
    research/archive/pt/I1/INVENTORY.md `a4a8806b219141975b6e2f6e5ccc13e723cb29c0b158386fa19049966eb66a99`,
    research/archive/pt/I2/INVENTORY.md `d923e63013c7fdf0fc2be61f6ce5566816ef1c339e7f070aee966ada6952325b`,
    research/archive/pt/I3/INVENTORY.md `51eff9afef1f7ed25d82dc140a83dd97a9b24765d39b84cfdb636fa38ca96d7d`.

  Records used for B14 (ids as issued there): I1.43/I1.47 (the sealed core, `OICore`), I1.46 (bare OI implies neither
  compositional principle), I1.49 `DerivedOI`, I1.50 `DerivedOICore`, I1.52, I1.55, I1.56 `ConfigurationLevel`,
  I1.59 (the observer theory of a substratum is `permTheory` on its configuration space), I1.60 `SourcedOI`;
  I2.31 (OI⁺-1, GR.md:228), I2.32, I2.33 (the phase intervention assumed); I3.150–I3.153 (forms of (b)), I3.165 (K2's
  clause, (b)), I3.168 K∞-Act, I3.169 K∞-Drive; I4.24–I4.32, I4.44, I4.58, I4.64, I4.110, I4.133, I4.148, I4.153,
  I4.154, I4.175, I4.240–I4.242, I4.247, I4.248.
- 2026-10-11T04:02:26Z — second coordinator addendum received (during B14 preparation, after the inventory reads;
  owner's framing; node list, order and budget unchanged). Recorded and applied from here on:
  - with A the applicable non-hypothetical OI premises at L and b the composite action, stage 6 gives
    K(Z_F) ⊨ A and K(Z_F) ⊭ b; the live objectives are (1) a sufficient bridge H with A + H ⇒ b, (2) the
    independence and minimality of H (weaker alternatives shown to fail; any sufficient bridge must exclude
    K(Z_F) or say why K(Z_F) fails its premises), (3) A + H ⇒ b is not yet an equivalence;
  - B14 ends in exactly one of: (i) a derivation of the availability of `actT R_z(θ₀)` or `actT J` (with
    RESPECT and product behaviour) from inventory items at L, through a bridge the stage-6 graph does not have,
    naming the NOT REACHED items it brings to the pair cone; (ii) a statement that no such derivation exists
    from the stated access, the obstruction named in inventory terms and independence shown by a model of the
    stated access in which the operation is unavailable; (iii) a precisely scoped OPEN naming the step at which
    the decision stops; in every case the disguise test on the predicate stated;
  - for B15–B17: a RESULTS row recording that an alternative weaker than H fails names the alternative it
    defeats, in those words.
- 2026-10-11T04:02:26Z — B14 pre-dispatch review of `lean/BridgeAvail.lean` (no local Lean; every change checked
  against the kernel source at L and the pinned Mathlib sources read in this session):
  - S0-1's ray lemma is already a kernel theorem at L: `MicroReversibility.exists_scaled_mem_of_instAvail_unitary`
    (MicroscopicReversibility.lean:251; for an architecture, an available unitary conjugation has a nonzero
    multiple of its operator in the class). The module's own `ray_of_instAvail` is removed and the kernel theorem
    used in its place, so the ray step is CERTIFIED [K] at L, not [D]. S0-1 stands as written; its check is now
    the kernel citation;
  - the unitarity proofs of `zPh` and `uJ` no longer depend on simp normal forms: the conjugates are computed by
    `Complex.star_def` and named map lemmas (`w345_star`, `uJ_star_a/b/c`), `zPh` through the diagonal lemmas,
    `uJ` entry by entry; `w345_ne_zero` now follows from `|w|² = 1`;
  - term-mode membership proofs restructured with explicit `unfold` steps (`zPh_sub`, `tokOp_zPh_substratum`,
    `pairOp_zPh_substratum`, `pairOp_nflip_permClass`, `quarter_on_lattice`, `sPh_quart`); explicit tactic
    imports added (`FinCases`, `NormNum`, `Ring`); two helpers renamed to avoid any clash with opened namespaces
    (`submonomial_mul_apply`, `one_entries_one`);
  - name check: none of the module's 72 declarations has a namesake among the kernel's declarations, and no
    identifier used resolves to two declarations in the namespaces opened;
  - the module now has 61 theorems, each with a `#print axioms` line; sha256
    `c75f6467795bd7f197e99e0e6a9f5780e18ed2f388630249dd2f01d827d1754e`, 794 lines.
- 2026-10-11T04:03:30Z — B14 dispatch (1 of 3 this round): dev branch `dev-bridge/r4-avail` cut from L
  (`9f9f8257`), commit `152094b5` (module verbatim from `937af1fb`, one import line after
  `import OIBridge.RelcSelectC5`); `verify.yml` dispatched on it; run 38110368244 (head `152094b5`, created
  2026-10-11T04:03:31Z, event `workflow_dispatch`). Waiting; no job or run will be cancelled.
- 2026-10-11T04:04:10Z — B15: cross-branch read on the coordinator's instruction (authorized for B15):
  `git show c10dbaee:research/equivalence/lean/EqvK2Schema.lean`, blob 659ae36c, 474 lines, sha256
  `0bc6da00d5b9ba9c4a2f9390db31c15830a19bf1e30fc2ee6889cd9211281221` (equal to the value the directive names).
  Saved to the session scratchpad; anything carried into this branch is carried verbatim with attribution.
- 2026-10-11T04:18:50Z — B14 CI result: run 38110368244 (head `152094b5`, created 2026-10-11T04:03:31Z) completed
  2026-10-11T04:16:41Z; Mathlib bridge job 114384480945: Build success (04:05:00–04:07:00Z, "Built
  OIBridge.BridgeAvail (3.7s)" with linter warnings only), 61/61 `#print axioms` lines of the module on
  `[propext, Classical.choice, Quot.sound]`, no `sorryAx`; `lean-axioms` PASS (5921 named results, no sorry); release
  gate red only on `lean-manuscript` (1 problem: no census family for the new module, by construction); every other
  job of the run green. The job log was read with the GitHub MCP job-log reader (the built-in `gh` refuses the log
  redirect, and the proxy refuses the blob host); the tail read covers the module's build lines, its 61 prints, the
  root build and the whole gate. NOTES-B14 §1–§7 written (form (ii)); RESULTS rows B14-1 … B14-4.
- 2026-10-11T05:24:25Z — third coordinator addendum received (after B14 closed green, during B15 preparation).
  Recorded and applied from here on, to B14 and to every later node:
  - an "independent bridge" verdict needs a full model: a model of the stated access satisfying the applicable OI
    premises at every level that applies to it, the NOT REACHED rows included so far as they apply to its level, in
    which `actT R_z(θ₀)` (or `actT J`) is not available with RESPECT and product behaviour. A model checked only
    against the 118 pair-level rows establishes pair-level independence and is labelled so. A "derived bridge" is a
    theorem transferring inventory items to the pair level with no introduced hypothesis; a "precisely scoped OPEN"
    names the unproved transfer, extension or reachability lemma and claims no independence;
  - (b), (T) and A_miss are cone-preserving admissibility (invariance) statements; (A) and H-T are operational
    availability through the kernel's protocols. Every RESULTS row from here on says which of the two it is about,
    and neither stands in for the other.
  Consequences for B14 (closed at b8f1f57e): §2's verdict was checked against the kernel predicates named in its
  table, not against the 68 NOT REACHED rows of Table A2, so as written it is not a full-model verdict. B14 is
  re-assessed in NOTES-B14 §8 (full-model check over the 68 rows at each level of a stated model, with a design
  module `BridgeAvailFull.lean` for the M-level rows not already kernel theorems at L, built in this round's second
  dispatch together with B15 and B16). RESULTS rows B14-1 … B14-4 stay as recorded; new rows carry the re-assessment
  and the reading of each B14 row. The standing rows of rounds 1–3 are audited once for the invariance/availability
  distinction (NOTES-B14 §8.8).
- 2026-10-11T05:35:47Z — B14 re-assessment, B15 and B16 opened (S0 in NOTES-B14 §8.0 at 05:25:38Z, NOTES-B15 at
  05:29:31Z, NOTES-B16 at 05:31:29Z, each before its first run). Exact runs, all from `experiments/`, each replayed
  byte-identically:
  - `b14_fullmodel.py` (05:28:13Z): the 68 NOT REACHED rows of Table A2 classed for the model FM — SAT 34,
    HARMLESS 29, NA 5, HARMFUL 0, the S0-17 tally exactly; controls C1–C5 and exact checks X1–X4 green (the group
    generated by the stated access with the quarter phase on two tokens has order 3072, lies on the fourth-root
    lattice and contains no multiple of `1 ⊗ diag(1, w)` or `1 ⊗ U_J`). Inputs R6/REASSESSMENT.md `1ff62ad6…`,
    R6/r4_tables.out `08d38e1c…`, I4/INVENTORY.md `43bbada1…`, all in this branch's `research/archive/`;
  - `b15_preflight.py`: run 1 (05:30:57Z, kept as `b15_preflight.run1.*`) failed P7 on list order only, a harness
    error; P7 compares as sets in run 2 (05:31:04Z), 12/12 green. P1 re-reads the equivalence module at `c10dbaee`
    (the cross-branch read logged at 04:04:10Z, hash re-checked: `0bc6da00…`);
  - `b16_preflight.py` (05:32:31Z): P1–P5 green.
  Pre-dispatch review of the three design modules (no local Lean; every kernel name read at L in this tree, every
  Mathlib name in the pinned sources): `lean/BridgeAvailFull.lean` (434 lines, 50 theorems, 50 prints, sha256
  `b93a732e…`), `lean/BridgeConverge.lean` (231 lines, 21/21, `1e4cbb86…`), `lean/BridgeReachDim.lean` (390 lines,
  27/27, `c49e3964…`). No new declaration has a namesake among the kernel's or the earlier design modules'
  declarations. Robustness fallbacks (`first | … | …`) are used where a proof depends on a simp normal form or on the
  defeq of a coercion.
- 2026-10-11T05:36:37Z — dispatch 2 of 3: dev branch `dev-bridge/r4-conv` cut from L (`9f9f8257`), commit `ca48c4c4`
  (BridgeAvail, BridgeAvailFull, BridgeConverge, BridgeReachDim verbatim from `bf585a14`; BridgeDictionary and
  BridgeReach from rounds 3; EqvK2Schema verbatim from `research/equivalence` @ `c10dbaee`, sha256 `0bc6da00…`, with
  attribution, for the build only; seven import lines after `import OIBridge.RelcSelectC5`); `verify.yml` dispatched;
  run 38115337569 (head `ca48c4c4`, created 2026-10-11T05:36:37Z, event `workflow_dispatch`). Expected `lean-axioms`
  count: 5860 + 222 = 6082. Waiting; no job or run will be cancelled.
- 2026-10-11T06:22:32Z — B17 (opened while dispatch 2 ran; S0 in NOTES-B17 at 05:39:54Z, before any run):
  `b17_tower.py` run 1 at 05:41:17Z, green (K1, K1b, S0-2, S0-3, K2, K3 all PASS; 192 of 192 orbit defects certified
  out of HO-24's cone under `1 ⊗ diag(1, e^{iπ/4})`; first failing stage n = 3); replay at 05:41:28Z byte-identical
  (`cmp`). Exact arithmetic throughout (Gaussian rationals; `√2` only through integer comparisons of `p + q√2`).
- 2026-10-11T06:22:32Z — dispatch 2 result: run 38115337569 (head `ca48c4c4`, created 05:36:37Z, completed 05:52:07Z,
  conclusion failure). Mathlib bridge job 114399008857 (05:36:40–05:39:34Z): Build step FAILED (05:37:00–05:39:31Z);
  Release gate SKIPPED, so no `lean-axioms` count this run; every other job of the run green. Per module:
  - `BridgeAvailFull` BUILT ("[3655/3659] Built OIBridge.BridgeAvailFull (4.6s)", linter warnings only), 50/50
    `#print axioms` reports on `[propext, Classical.choice, Quot.sound]`, no `sorryAx` (parsed from the job log);
    `BridgeDictionary` (20/20) and `EqvK2Schema` (22/22) rebuilt, all standard;
  - `BridgeConverge` FAILED ("[3657/3659] Building"): the postfix `ᴴ` did not parse at lines 79, 85, 96, 151
    (`open Matrix` / `open scoped Matrix` missing from the module's opens); every other error in the block is a
    cascade of those four (truncated statements of `transferMap`, `dict_transferMap`, `transferClause_iff`,
    `pauli1_unitary`; a type mismatch and a `whnf` timeout in `transferClause_Q3` against the truncated statement;
    a kernel unknown-constant error in `Q3_phase_invariant`). The 14 declarations not downstream of the four
    reported standard axioms;
  - `BridgeReachDim` FAILED (listed under "Some required targets logged failures"); its error block was printed
    before the readable tail (the job-log reader returns at most the last 5000 of 38194 lines; the built-in `gh`
    refuses the log redirect and the proxy refuses the blob host), so its errors are not recorded. This round
    records the failure without a diagnosis.
  Failed versions kept as `lean/BridgeConverge.run38115337569.lean` (sha256 `1e4cbb86…`) and
  `lean/BridgeReachDim.run38115337569.lean` (sha256 `c49e3964…`), equal to the dev-branch blobs.
- 2026-10-11T06:24:26Z — pre-dispatch review for dispatch 3 of 3 (the last; no local Lean; every Mathlib name read in
  the pinned sources, a local `leanprover-community/mathlib4` checkout at tag `v4.33.0` = `db584cd6`, the rev the
  lakefile pins; every kernel name read at L):
  - `lean/BridgeConverge.lean`: `open scoped Matrix` added (the cause of every dispatch-2 error in the module);
    `transferClause_Q3` restated so that the positive-semidefinite step is taken over one dictionary
    (`EqvK2Schema.dict`), with no cross-module definitional unfolding. 232 lines, 21 theorems, 21 prints, sha256
    `3f7155ca…`;
  - `lean/BridgeReachDim.lean`, rewritten without a diagnosis of its dispatch-2 failure. Every step whose outcome
    depended on a simp normal form, on the direction of `subst`, or on a defeq the unifier had to discover is
    replaced: the charts are `kron2 ![1, x₀] ![x₁, x₂]` and `kron2 ![0, 1] ![x₁, x₂]`; chart membership is proved
    entry by entry (`Fin.forall_fin_two`, `show` at literal indices, `ring` and `div_mul_cancel₀`) in
    `kron2_eq_chart0` / `kron2_eq_chart1`; smoothness of the chart entries through `vec2_contDiff`; the coset map
    through `badMapA_apply` and an explicit function equation; `dimH` bounded through a `calc` stated in this
    module's own instances; the controlled-phase control through `czMat_apply`, `czMat_mulVec`, `decide`d index
    inequalities and `rfl` entries of `ctlV`. Names checked: one Mathlib namespace changed since the D2 text
    (`unitary.star_mul_self_of_mem` is `Unitary.star_mul_self_of_mem` at v4.33.0; the D2 text reached the
    unitary step through a `first` fallback); `Matrix.UnitaryGroup.star_mul_self`, `Matrix.UnitaryGroup.inv_val`,
    `Set.Countable.exists_eq_range`, `Set.mem_compl_iff`, `Module.finrank_prod`, `Module.finrank_pi_fintype`,
    `Module.finrank_self`, `Complex.finrank_real_complex`, `Complex.conjCLE_apply`, `Complex.re_ofNat`,
    `Complex.im_ofNat`, `div_mul_cancel₀`, `contDiff_apply` (explicit `𝕜 E`), `ContDiff.dimH_range_le`,
    `dimH_iUnion`, `dense_compl_of_dimH_lt_finrank` read with their signatures. The module imports `EqvK2Schema`
    for build order only, so that its report is compiled after `EqvK2Schema` and falls in the readable tail of
    the job log; the import closure of `EqvK2Schema` was read for global notations, simp attributes and instances
    that could reach this module's proofs (simp lemmas only on kernel-specific definitions, instances only on
    kernel-specific types, notations all local). 484 lines, 32 theorems, 32 prints, sha256 `d4ee2170…`;
  - no declaration of either module has a namesake among the kernel's, the other design modules' or Mathlib's
    declarations; no identifier used unqualified resolves to a kernel declaration.
  Expected `lean-axioms` count for the dispatch-3 tree: 6083 distinct short names (baseline 5860 at L, 223 new). The
  dispatch-2 entry's 6082 summed the per-module print counts (222); the gate counts distinct short names, four of
  which recur across the design modules, so the dispatch-2 tree's figure was 6078 (that run's gate did not run).
- 2026-10-11T06:25:04Z — dispatch 3 of 3 (the last of the round): dev branch `dev-bridge/r4-final` cut from L
  (`9f9f8257`), commit `bf8ba746` (BridgeAvail, BridgeAvailFull, BridgeDictionary, BridgeReach unchanged since
  dispatch 2; BridgeConverge `3f7155ca…` and BridgeReachDim `d4ee2170…` from `b7038e6c`; EqvK2Schema verbatim from
  `research/equivalence` @ `c10dbaee`, sha256 `0bc6da00…`, with attribution, for the build only; the same seven
  import lines after `import OIBridge.RelcSelectC5`); `verify.yml` dispatched; run 38117986499 (head `bf8ba746`,
  created 2026-10-11T06:25:04Z, event `workflow_dispatch`). Expected `lean-axioms`: 6083. No dispatch remains this
  round; no job or run will be cancelled.
- 2026-10-11T06:29:39Z — dispatch 3 result, Mathlib bridge job 114406679644 (run 38117986499, head `bf8ba746`,
  06:25:07–06:28:44Z): Build SUCCESS (06:25:26–06:27:53Z, "Build completed successfully (3659 jobs)"); per module, in
  the readable tail: "[3652/3659] Built OIBridge.BridgeAvail" 61/61, "[3653] EqvK2Schema" 22/22, "[3654]
  BridgeAvailFull" 50/50, "[3655] BridgeReachDim (3.5s)" 32/32, "[3656] BridgeDictionary" 20/20, "[3657]
  BridgeConverge (2.2s)" 21/21 `#print axioms` reports on `[propext, Classical.choice, Quot.sound]`; `BridgeReach`
  (built before the tail) is covered by the gate; no `sorryAx` and no `error:` line in the tail. Diagnostics of the
  two revised modules are unused-tactic notes only: in every `first` block of BridgeReachDim the first alternative
  closed the goal, and in BridgeConverge the `simp` fallback of `pauli1_eq_perm` never ran. Release gate:
  `lean-axioms` PASS ("6083 named result(s) reported, no sorry"), exactly the predicted count; the only red step is
  `lean-manuscript` (7 problems: the seven design modules have no census family, by construction); every other gate
  step PASS. The rest of the run (numerical probes) still running at this entry; no job or run cancelled.
- 2026-10-11T06:35:56Z — final replay of every round-4 script from `experiments/` into the session scratchpad, compared
  with `cmp` against the committed `.out` and `.err`: `b14_preflight`, `b14_fullmodel`, `b15_preflight`,
  `b16_preflight`, `b17_tower` — all five byte-identical.
- 2026-10-11T06:36:40Z — outcomes written: NOTES-B14 §8.1–§8.8 (S0-11 … S0-20; the full-model row table; the verdict
  "independent bridge (full model, relative to the stage-6 inventory)", CONJECTURE; the reading of B14-1 … B14-4 with
  two sentences corrected forward; (b) and FM; gem re-assessed ELABORATING with a POSITIVE part — S0-19's clause "which
  no item at L states" withdrawn against R6 `r4_tables.out`:141 and stage 4, so S0-20's NEW is not confirmed; the
  standing-rows audit of rounds 1–3); NOTES-B15 §1–§5, NOTES-B16 §1–§5, NOTES-B17 §1–§4 (one sentence of B17 §2
  corrected before commit: the tower's closure is B10-4's 2-torus group, beyond B16's count, so its exotic cone rests
  on claim (D) through B7-2, not on B16). RESULTS rows B14-5 … B14-8, B15-1 … B15-3, B16-1 … B16-3, B17-1 and the
  standing verdict V-4, each with its reading. Handoff proposals HP-11 (full model, K∞-Drive's two readings, the
  audit), HP-12 (one dictionary), HP-13 (B7-1 under curve covers), HP-14 (HO-24's cone along the tower).
- 2026-10-11T06:41:34Z — dispatch 3's run 38117986499 completed at 06:41:23Z: 32 jobs success, 1 failure (the Mathlib
  bridge job, whose only red step is the release gate's `lean-manuscript`, as recorded at 06:29:39Z). No job or run
  of the round was cancelled.
- 2026-10-11T06:41:34Z — **round 4 closed.** Nodes: B14 re-assessed under the third addendum — independent bridge
  (full model, relative to the stage-6 inventory), CONJECTURE, reading availability; standing rows of rounds 1–3
  audited, corrections carried forward in V-4; gem ELABORATING with a POSITIVE part (S0-20's NEW not confirmed).
  B15 — one dictionary and the transfer clause in table form, CONJECTURE [D]; (b) for the phase circle in table form
  CONDITIONAL on the clause; "the transfer clause for the stated access" and "a finite group" FAILED as sufficient
  bridges; ELABORATING. B16 — B7-1 under countable C¹ curve covers, CONJECTURE [D]; for identity components of
  dimension at most one CONDITIONAL on Cartan [L]; "a group" with such an identity component FAILED as a sufficient
  bridge; ELABORATING. B17 — HO-24's explicit cone along B10-5's tower, first failing stage `n = 3`, CONJECTURE
  (exact); "a finite stage" FAILED as a sufficient bridge; CONFIRMING. Dispatches: 3 of 3 (runs 38110368244,
  38115337569, 38117986499). Cross-branch reads this round, each logged: `research/overview` @ `742c6b2f` (receipts),
  `research/origin` @ `de9285d6` (OriginExclusive.lean, B14), `4dc0321c` (inventory blobs, B14), `research/equivalence`
  @ `c10dbaee` (EqvK2Schema.lean, B15). Handoff proposals HP-11 … HP-14. Final replay of every round-4 script
  byte-identical (06:35:56Z). Nothing outside `research/bridge/` changed on this branch; no pull request, merge or
  write to `main` or to another thread's branch.

## Round 5

- 2026-10-11T07:37:26Z — round 5 opened at thread head a34d20b5 (clean, equal to origin/research/bridge; `git diff 9f9f8257 HEAD
  -- verification papers book` empty, so the kernel in this tree is L). Own record re-read: README.md, LOG.md,
  RESULTS.md, NOTES-B14 (§8), NOTES-B15, NOTES-B16, NOTES-B17, HP-11 … HP-14, lean/BridgeAvail.lean,
  lean/BridgeAvailFull.lean, lean/BridgeConverge.lean, lean/BridgeDictionary.lean. Read-only reads of the coordinator's
  branch research/overview @ 4c4a02b1 (authorized by the round-5 directive), sha256 of what was read:
  - research/AUDITS/2026-10-11-round4/AUDIT-BRIDGE-R4.md `3f23aff50458fbd8d69e4084cc4eab563c2e5244799e8869e90f30d5415badb9`
    (no label changes; finding F1 = the correction item of HO-33, taken up as B18);
  - research/HANDOFFS/HO-33 … `d5f9d19eafa2fdf39877fa701961bb1c95ae5cfde5bbfd13ace7a0ce08a21169`, HO-34 …
    `0a39ea8227e51cae331a4d3b9de62ba12f168b14e46993e4690eae42f94d1e6f`, HO-35 …
    `70d57d852f8f8f7e3500c464faeefffc0b64f62d795eefc48308c5ec3f2dee53`, HO-36 …
    `8b8a3bf52b6a834825e592cdfd75c3c40fbdd7cdbcf8a4fb566901b4fd536cd2`: this thread's own round-4 results as routed, read
    for their item numbering and for HO-33's correction item only. Not copied: they are not addressed to this thread.
- 2026-10-11T07:37:26Z — receipts. Copied from research/overview @ 4c4a02b1 `research/HANDOFFS/` into `inbox/`, byte-identical
  (`cmp` against `git show 4c4a02b1:…`), sha256 of each copy:
  - HO-18 v2 (equivalence → bridge, countermodels) `9aeac715ae694e44fcfa11789890b6644470995d29c9d352700adfe301c131ba`
    (overview blob ebd9e287);
  - HO-27 v1 (origin → bridge, equivalence, countermodels) `196fdad5e8917ef04ce6f229ab7405636d93b9fd98c41688245a0bd48cf9c2a4`
    (blob a817d94a);
  - HO-28 v1 (equivalence → countermodels, bridge) `608aca2ecef2e59281ede77ceeb6d387a0fbed39aa3d11df9b6e5fcd5a6a7034` (blob 841749d4);
  - HO-29 v1 (equivalence → bridge, origin) `5526735ff8f833a8b503e553889366942c7ffdaacb701b7610569e4ccad65aa0` (blob d3cf4e4d);
  - HO-30 v1 (countermodels → equivalence, bridge) `b9d380753e40f29d9fccd13290ca430b9b2c7b02f3191edad943ac93da4d5f38` (blob 15bd19b7);
  - HO-31 v1 (countermodels → bridge, origin, equivalence) `27263a957e2e50e5aaca8499f5355cf387fb30943c74226259fd5c52522feef8`
    (blob a5f86ba5);
  - HO-32 v1 (countermodels → equivalence, bridge, origin) `06a0ac6b463a41b62647d1b1aaf11263758fda7390516a53484abd5a98a2a0a9`
    (blob a5a6694b).

  HO-18 v1 stays in `inbox/` (received d877be82); v2 supersedes it. Nothing in these handoffs is CERTIFIED except the
  kernel lines they cite; every item is used at its own label. The "may not assume" sections of all seven are honoured.
  Reliance, handoff by handoff and item by item:
  - **HO-18 v2.** Item 1 (`EqvK2Schema`: the dictionary's product law, pairing, completeness, injectivity, `dictEquiv`)
    at CONJECTURE [D] (run 38101580750), relied on in B20 only through the round-4 `BridgeConverge` (B15-1, which already
    imports it) — `dict_injective`, `coordOf`, `dict_coordOf`, `Q3`. Item 2 (v2: LOWER and UPPER take a table of every
    rank-one positive matrix, not the products) is context; no step of rounds 1–4 read the lemmas with the products as
    hypothesis (round-4 LOG: items 2 and 3 were context only), and none does now. Item 3 (the schema's five hypotheses)
    is context: B20 claims nothing about the schema. Item 4 is a build-time fact about the one-list rendering. Item 5
    (the convergence target) was met in B15. Not assumed: certification; more than CONDITIONAL for
    `pairCone_eq_Q3_of_drive`; a formalized two-rotation clause; v1's wording of the cone lemmas; anything beyond two
    tokens.
  - **HO-27 v1.** Items 1–3 and 6 are addressed to this thread. Item 1 (N11: on origin's stated-access model every
    available unitary datum has finite order on the token body; OI ⇒ X with no introduced hypothesis) at CONDITIONAL
    [D], as context for B20's refutation statements; terminology recorded: origin's "stated-access model" is the
    substratum theory (`genTheory substratumClass`, I4.44), whereas this thread's "stated access" is the kernel's own
    phrase for `permClass` (I1.60) and for `MixR ∅` (OperationalSourcing.lean, SubstratumInterfaceAudit.lean:236,
    StateMixingCoupling.lean:13); FM's lattice theory lies between them. Item 2 ((L-O), OPEN) as the exact location of
    the open single-token transfer lemma: nothing this round assumes the stage-crossing datum independent of OI. Item 3
    (ORD∞ on the token body is coherence) as context for B20's disguise test: on the matrix carrier the frame-axis
    phase is a member of the monomial class, and what the lattice and the stated access lack is the member
    `diag(1, w)` itself (B14), not a coherent state. Item 6 (the re-preparation law is an operation datum) as a
    constraint, not used. Items 4, 5, 7 are addressed elsewhere; not relied on. Not assumed: independence of the
    stage-crossing datum from OI; kernel status for any [D] declaration or for O9-L1; dense control at every level;
    availability from cone invariance.
  - **HO-28 v1** (copy). Item 1 (the control relation counts chart dimensions: a native gate needs odd chart dimension)
    as a constraint on the bodies a transfer can reach; every object of this round has `d = 3`, so it is not used.
    Items 2–5 context. Not assumed: certification; that the count is sufficient; anything about OI as a whole from the
    hybrid token.
  - **HO-29 v1.** Item 1 (S6's necessity direction: `K = Q3` iff A_miss given H1–H3 and `ReachPure`, invariance reading
    only; a sufficient bridge must deliver the invariance form at the pair level) at CONJECTURE [D] as the target shape
    of B20; item 2 (`EqvK2Converse`: `dict_actT_rotLin`, `dict_actT_cyc`, `Q3_aMiss`; run 38112803530, 9/9 standard)
    relied on in B20 at CONJECTURE [D]: `dict_actT_cyc` is the cycEquiv intertwining B20 needs and `Q3_aMiss` the
    unconditional control at the kernel's own pair cone; the module is read at research/equivalence @ ab6788b9 (logged
    below) and carried verbatim with attribution on the dev branch only. Item 3 (the admissible wording: "independent of
    the transferred pair-level premises at L", never "independent of OI") adopted for every statement of this round.
    Not assumed: certification; that A_miss, H2, H3 or `ReachPure` is an OI premise or sourced; that invariance
    implies availability (B20 derives the opposite direction only); that the module formalizes the two-rotation clause.
  - **HO-30 v1.** Theorem S′ (finite form) as a design-built statement [D] (run 38112813276, 78/78 standard): relied on
    only in B21, if reached, as the H3 engine of the explicit cones (HO-24's `K384`, HO-31's `K768`), at CONJECTURE
    [D]; not used in B18–B20. Not assumed: certification; S′ for compact defect sets; the necessity of (CC); H1 for any
    cone; any OI content.
  - **HO-31 v1.** Item 1 (Theorem C19-1: the block-diagonal `SU(2) × SU(2)` with H1 and H3 forces `Q3`; with HO-22
    item 3 the mechanism by which the clause with the gate forces `Q3`) at CONDITIONAL, as the pair-level reading of
    B20's bridge (the two operations it delivers generate, with the gate, exactly that group: B12-3). Item 2 (the
    Clifford chain keeps explicit exotic cones; the first generator killing every surgery-type cone is non-Clifford of
    infinite order) at CONDITIONAL, as the statement that B20's `R_z(θ₀)` is of the required kind. Item 3 (Lemmas
    C18-1 … C18-3; case B and S2 with G16 OPEN) and the two assumption-watch markers are the inputs of B21, if reached.
    Item 4 context. Not assumed: certification; the closure identification of HO-22 item 3 beyond its label; explicit
    cones for case B, S2 with G16 or `K_circ`; exhaustiveness of the survivor search.
  - **HO-32 v1.** Items 1–5 (the four explicit cones against Table A2: 118/13/68 each; what each refutes) at
    CONDITIONAL, as the pair-level constraint on B20: a bridge delivering only finitely many Clifford rotations, or the
    drive flow without `J`, is refuted by an explicit cone; B20's two operations are `R_z(θ₀)` (non-Clifford, infinite
    order) and `J`. Item 2's three kinds of premise and item 4's list of refuted implications are used as stated. Not
    assumed: availability of any operation; that any cone "satisfies OI" or is "independent of OI"; anything about the
    68 NOT REACHED rows beyond R6; level-(ii) versions; invariance under any continuous family other than `Kk`'s.
- 2026-10-11T07:54:19Z — correction, forward: the HO-36 hash in the receipts entry above was first typed as `8b3b3a8b…`; the
  measured value is `8b8a3bf52b6a834825e592cdfd75c3c40fbdd7cdbcf8a4fb566901b4fd536cd2`, and the entry now carries it.
- 2026-10-11T07:54:19Z — **owner's round-5 directions received** through the coordinator (recorded in research/overview
  OVERVIEW.md, "Owner's round-5 directions"; binding from now; this thread has first priority with origin). Quoted:
  the question round 5 works is "can the existing OI principles generate the continuous operational control needed
  to force the quantum cone, without assuming that control separately?" Requirements: "(1) correct F1 WITHOUT relying
  on SubstratumAvail where it fails — the re-classification of I4.56 and I2.34 must rest on a chain whose every
  link's side hypotheses FM satisfies (the quarter phase from DerivedOI, avail_conj_mul, the exchange's layer flow),
  kernel-checked in design if small, else [W]; never cite LiftAudit.lean:812 or :783 for FM; (2) verify the
  sufficient bridge WITHOUT silently assuming the phase intervention: in B20, OpDrive(θ₀) and the J-datum are
  explicit introduced hypotheses, every other hypothesis of the derivation OI + {OpDrive(θ₀), J-datum} ⇒ (T) is an
  inventory item cited by id at its status at L, and no step uses any availability beyond those (in particular no
  diagonal_avail, no SubstratumAvail, no DrivesElementary); state the exact kernel closure rules used (bind /
  avail_conj_mul, spectator, transport, relabel, discard — HO-17 item 8)." Safeguard (shared with origin): "that
  every available primitive has finite order does not establish that compositions cannot generate continuous control
  (Hadamard and T are finite-order and generate a dense subgroup). So the bridge OpDrive(θ₀) is to be classified as
  SUFFICIENT, NOT NECESSARY, unless alternative generating sets are excluded: a finite-order non-Clifford datum on
  the token (a non-Clifford phase of finite order with the stated access) would also generate dense single-token
  control. In B20 record the bridge as 'sufficient'; list the alternative generating sets you can name (the origin
  thread characterizes the generated groups under the actual composition rules — do not duplicate that, cite it as
  pending: origin O14/O15); and make explicit which closure or limiting step (density → every unitary available, or
  only a dense set) your derived half needs: availability of each finite composition is exact, density is a closure
  statement that must be an inventory item or introduced. The transfer clause in table form needs the specific
  operations R_z(θ₀) and J available, not a dense set — say whether your chain needs exact availability of R_z(θ₀)
  (OpDrive as stated) or whether a dense subgroup plus a closure premise (H3's closedness of the cone) suffices for
  the invariance conclusion; keep the two versions apart." Everything else in the round-5 instructions stands.
  Applied from here on, before any dispatch: B18's chain takes its sign diagonal from DerivedOI's quarter phases
  (`PhasesAvailable`) through the kernel's `avail_conj_mul` and the exchanges from `ExchangesAvailable`, with the
  row's own executable layer flow — no `SubstratumAvail`, no `diagonal_avail`, and LiftAudit.lean:812/:783 cited
  only as the chain being replaced, never for FM; B20 records the bridge as sufficient, not necessary, lists the
  alternative generating sets, names the closure rules of every step, and keeps the exact-availability version
  (OpDrive as stated) apart from a dense-subgroup-plus-closedness version of the invariance conclusion. S0 addenda
  dated after this entry carry the adjustments in NOTES-B18 and NOTES-B20; the S0 sections already written stay as
  written.
- 2026-10-11T08:07:01Z — **two further owner distinctions received** through the coordinator (recorded in research/overview
  OVERVIEW.md under "Owner's round-5 directions"; binding for B18–B20). Quoted: "(1) Reversible groups versus general
  operational closure. Ancilla preparation and discard are not invertible and do not belong to a group of reversible
  operations. Your predicates PairAvailAt / TokenAvailAt are availabilities of one-outcome conjugation channels
  (reversible), but the kernel closure you use to move between them (B19: spectator, transport, relabel, and discard
  for the pair ⇒ token direction) includes non-invertible protocols. State for every theorem which domain it lives in
  — the reversible group generated at a level, or the InstAvail closure with ancillas and discard — and never let a
  group-generation step rely silently on a transformation outside its stated domain (when a token unitary is
  recovered by discarding an ancilla, the kernel's `discardWith_uniform_conjChannel` is the lemma that says the
  result is again a conjugation). (2) Dense control versus exact availability. In B20 keep three objects apart for
  the drive: (i) exact availability of R_z(θ₀) as a finite composition of available operations (OpDrive(θ₀) as
  stated; by bind the kernel's availability reaches exact finite compositions only); (ii) a dense subgroup of SU(2)
  (closure(⟨generators⟩) = SU(2) does NOT mean every element is exactly reachable); (iii) exact invariance of a pair
  cone under the full closure, which K2 requires. If your derived half passes from density to exact invariance,
  establish first the topological closure (H3: K closed, with the exact statement that a closed cone invariant under
  a dense subgroup is invariant under its closure) and the continuity property it needs (the action
  U ↦ coordOf(Ad(1 ⊗ U) dict ω) is continuous in U — state and, if small, prove it in design); label the closure
  step as the premise it is. If instead your chain needs exact availability of R_z(θ₀) and J, say so and do not
  invoke density at all. Non-Clifford status of a finite-order datum does not by itself give density: density is
  proved for the actual generating set, at the level claimed (the origin thread characterizes the generated groups;
  cite its result at its label, pending)." The owner's classification of the decisive outcome, to be applied by the
  coordinator to B20's verdict with origin O14: "(A) drive derived from existing OI premises; (B) drive derived only
  after a new independently motivated premise — conditional reconstruction with an explicit physical principle; (C)
  drive supplied by an assumption equivalent to the phase intervention — a sufficient bridge with no independent
  explanation of its origin; (D) existing premises admit non-quantum countermodels — demonstrated insufficiency at
  the audited scope. B20's expected classification is (C) unless origin's O14 moves it; say which it is, and keep
  the scope explicit: insufficiency for the complete stage-6 inventory is definitive within its scope and says
  nothing about every conceivable extension of OI." Applied from here on, before any dispatch: every theorem of
  B18–B20 carries its domain (the reversible group generated at a level by the bind rule on conjugations, or the
  InstAvail closure with ancillas and discard), recorded in the NOTES addenda and in every RESULTS row; B20's chain
  needs the exact availability of `R_z(θ₀)` and `J` and invokes no density (the dense-subgroup version is named as
  the different statement it is, with its two premises — a closed cone and the continuity of the transferred table —
  and is neither claimed nor built); the alternative generating sets are listed as candidates whose density is for
  the origin thread to establish, not asserted; B20's outcome is classified (C) and B14-6's (D) with the scope
  sentence. The addenda are dated after this entry.
- 2026-10-11T07:20:12Z (recorded here) — cross-branch read on the coordinator's instruction (authorized for the builds):
  `git show ab6788b9:research/equivalence/lean/EqvK2Schema.lean` (blob 659ae36c, 474 lines, sha256
  `0bc6da00d5b9ba9c4a2f9390db31c15830a19bf1e30fc2ee6889cd9211281221`, equal to the round-4 value) and
  `git show ab6788b9:research/equivalence/lean/EqvK2Converse.lean` (blob 4add9b8d, 234 lines, sha256
  `240abaf6c445112e1b2d5aa39932b51004e6b21cb93b9999ca6aacb5201b0554`, equal to HO-29's value). Saved to the session
  scratchpad; carried verbatim with attribution on the dev branch only (B20 imports `EqvK2Converse`, which imports
  `EqvK2Schema`); nothing of them is copied into this branch.
- 2026-10-11T07:39:54Z — NOTES-B18, NOTES-B19 and NOTES-B20 opened: question, design, productivity test and predictions,
  before any run or dispatch (S0-1 … S0-8; S0-1 … S0-6; S0-1 … S0-10).
- 2026-10-11T07:43:14Z — decision rules written into `b18_preflight.py`, `b19_preflight.py` and `b20_bridge.py` (one
  `date -u` reading immediately before writing the three headers).
- 2026-10-11T07:45:20Z — `b18_preflight.py` run 1: 6/6 PASS, VERDICT B18-PREFLIGHT-OK (the isolation identity rebuilt
  from the kernel's definitions, symbolic in `t`, at levels 1–3 and on the pair carrier; the scalar-free form; the sign
  diagonals on the lattice; the countercontrol with a fixed point). 07:45:21Z — `b19_preflight.py` run 1: 4/4 PASS,
  VERDICT B19-PREFLIGHT-OK. 07:45:34Z — `b20_bridge.py` run 1: 4/5, VERDICT B20-FAILED P3: no certified witness for the
  target `R_z(θ₀)` in the witness family searched (b8 X2's family — the defects' images and their sums with Bell
  projectors), while the `J` half of P3 passed with the value `−1`; kept as `b20_bridge.run1.{py,out,err}`.
- 2026-10-11T07:50:59Z — `b20_bridge.py` post-run edit, logged in its header (rule text unchanged): the witness family
  of b8 X3 — the Bell projectors rotated by the quarter phase or its Hadamard conjugate on either token — added to the
  candidates. Run 2 (07:50:59Z): 5/5 PASS, VERDICT B20-EXACT; P3's values `−4/5` for `R_z(θ₀)` (defect 0, the flow law
  `−s` at `s = 4/5`) and `−1` for `J` (defect 0), `Q3` controls green. Replays at 07:57:57Z, 07:58:11Z, 07:58:14Z
  byte-identical (`cmp`, `.out` and `.err`) for all three scripts.
- 2026-10-11T08:06:00Z — decision rule written into `b18_reclass.py` (loads `b14_fullmodel.py`'s row table unchanged by
  executing its text before `def main():`; two rows re-classed; C1–C5 re-run; new controls C6–C8; the design links
  tagged [D] only when `DESIGN_BUILT` is set after a green build, [W] before). Run 1 (08:09:47Z, `DESIGN_BUILT =
  False`): tally SAT 34 / HARMLESS 29 / NA 5 / HARMFUL 0, C1–C8 PASS, VERDICT B18-RECLASS-OK with the two rows HARMLESS
  [W] and the scope sentence "27 on a kernel chain at L whose side hypotheses FM satisfies, 2 (I4.56, I2.34) on a written
  chain [W]"; replay 08:11:04Z byte-identical. Run 2 follows the dispatch result.
- 2026-10-11T08:07:01Z — pre-dispatch review of the two round-5 modules (no local Lean; every kernel name read at L in
  this tree; every Mathlib name read in the pinned sources, the local checkout `/home/user/leanprover-community/mathlib4`
  at tag `v4.33.0` = `db584cd6`, the rev the lakefile pins):
  - `lean/BridgeToken.lean` (483 lines, 41 declarations, 36 `#print axioms` lines, sha256
    `417142becdcfe19d541f971581eae520a84f72580027d5375b48f1e033f018c8`): §A B19 (`assocPair`, `reindex_assoc_tokOp`,
    `pairAvail_of_tokenAvail`; `toEnd`, `reindex_toEnd_pairOp`, `discard_two`, `tokenAvail_of_pairAvail`;
    `pairAvail_iff_tokenAvail`); §B B18 (`signDiag`, `signDiag_empty`, `signDiag_insert`, `phaseGate_fourth`,
    `signDiag_avail_of_phases` by `Finset.induction_on`; `signFun_pm`, `signSet`, `diagonal_signFun_eq`,
    `diagonal_phaseFun_free`, `phaseFun_mul_star`; `phaseFree_of_layerFlowExecutable_free`, its `DerivedOI` form, the
    control and QM endpoints; FM's token and pair instances). Mathlib names read: `Equiv.swap_apply_self`,
    `Equiv.swap_apply_def`, `Equiv.symm_symm` (rfl), `Equiv.prodAssoc`'s definition, `Finset.induction_on` (binders
    `a s h ih`), `Finset.notMem_empty`, `Finset.mem_insert`, `Finset.mem_insert_self`, `Finset.mem_filter`,
    `Finset.mem_univ`, `Fintype.one_lt_card_iff`, `Matrix.diagonal_mul_diagonal`, `Matrix.diagonal_one`,
    `Matrix.diagonal_apply`, `Matrix.smul_apply`, `Matrix.one_apply`, `Matrix.smul_mul`, `Matrix.one_mul`,
    `Matrix.reindex_apply`, `Matrix.submatrix_apply`, `Complex.I_mul_I`, `inv_mul_cancel₀`, `Nat.cast_smul_eq_nsmul`.
    Robustness fallbacks (`first | … | …`) where a step depends on a simp normal form, a definitional unfolding or a
    literal (`assocPair_symm_apply`, the two reindex identities, `discard_two` through the kernel's
    `discard_tensorOf_one` at `m + 1 = 2`, the transport steps, `signDiag_insert`, `phaseGate_fourth`,
    `swap01_free`).
  - `lean/BridgeOpDrive.lean` (249 lines, 23 declarations, 21 prints, sha256
    `02f92407b9727e9944a457592df87b72145a6ea2d2b30b5db9a8db4f70db8d81`): `OpDrive`, `JDatum`; §A pair availability;
    §B `ancBlock_smul_tokOp`, `exists_scaled_mem_of_tokenAvail`, `mem_of_tokenAvail`; §C `zPh_eq_zPhase` (fallbacks),
    `uJ_eq_cycMat` (rfl), `transferMap_zPh`, `transferMap_uJ`; §D `transfer_of_opDrive`, `transfer_of_jDatum`,
    `bridge_derived_half`, `Q3_two_invariant`; §E the refutations, controls and exclusion lemmas.
  - Name check: none of the 64 new declarations has a namesake among the kernel's, the earlier design modules' or the
    equivalence modules' declarations (grep over `OIBridge/*.lean`, `lean/*.lean` and the two equivalence files).
  - Expected `lean-axioms` count for the dispatch tree: baseline 5860 + 240 prints (BridgeAvail 61, BridgeAvailFull 50,
    BridgeDictionary 20, BridgeConverge 21, EqvK2Schema 22, EqvK2Converse 9, BridgeToken 36, BridgeOpDrive 21) − 4
    short names recurring across the dictionary modules (`dict_tens`, `dict_prodState`, `dict_injective`,
    `dict_isHermitian`) = 6096 distinct short names.
- 2026-10-11T08:10:09Z — **dispatch 1 of 3**: dev branch `dev-bridge/r5-bridge` cut from L (`9f9f8257`) with git
  plumbing (a temporary index in the scratchpad; the research worktree and index untouched): commit `36083b22` (tree
  `be98ce01`), child of L, adding under `verification/lean-mathlib/OIBridge/` the blobs BridgeAvail `c88aafd5`,
  BridgeAvailFull `192fca74`, BridgeDictionary `fece97f4`, BridgeConverge `d09c7050` (the round-3/4 modules,
  unchanged), BridgeToken `e0d3ce0c`, BridgeOpDrive `722b20ef` (equal to `lean/*.lean` here), EqvK2Schema `659ae36c`
  and EqvK2Converse `4add9b8d` (verbatim from `research/equivalence` @ `ab6788b9`, with attribution in the commit
  message, for the build only), and eight import lines in the root `verification/lean-mathlib/OIBridge.lean` after
  `import OIBridge.RelcSelectC5` (root blob `cf1cbc30`). Deviation, as in rounds 1–4: the root file is outside
  `OIBridge/`, and the lake library builds only modules reachable from it. Pushed; `verify.yml` dispatched through
  `gh api -X POST repos/amaybaum/incompleteness/actions/workflows/verify.yml/dispatches -f ref=dev-bridge/r5-bridge`;
  run 38123860471 (head `36083b22`, created 2026-10-11T08:10:11Z, event `workflow_dispatch`). Waiting; no job or run
  will be cancelled.
- 2026-10-11T08:11:09Z — B21 cross-branch reads on the coordinator's instruction (authorized for B21 only; read, not
  copied): `research/countermodels` @ `644bf0a1` — NOTES-C18.md (187 lines, sha256
  `a247e83b07c6d0bf034f501ffd0b07f96ef78fd910fb753baef4fec308436817`), NOTES-C19.md (141 lines,
  `bfdfd94a1a6707932fdf50e0658c0ba95844228e97453a3f2ea668b8f6958d92`), experiments/c18_attempts.py (500 lines,
  `16eb933f96f76d435917227bb7381f7b5e28f880813c45173503d674a64832f8`), experiments/c19_groups.py (441 lines,
  `4517e4d2b79236fedc79748f454cff0860b836b41f173545b8d678f71d6e99db`); all four equal to the values HO-31 records.
  Saved to the session scratchpad; nothing of them is copied into this branch.
- 2026-10-11T08:20:00Z — dispatch 1 result: run 38123860471 (head `36083b22`), Mathlib bridge job 114424007491
  (08:10:14–08:13:04Z): Build FAILED (08:10:35–08:13:00Z), Release gate skipped; the Lean kernel check green. The job
  log read with the GitHub MCP job-log reader (tail 5000 of the log; the error block falls in the tail). Per module:
  BridgeAvail (61), EqvK2Schema (22), BridgeAvailFull (50), EqvK2Converse (9), BridgeDictionary (20), BridgeConverge
  (21) built with every `#print axioms` line standard; `BridgeToken` FAILED ("[3645/3651] Building") with three
  errors: (i) 199:2 "No goals to be solved" in `signDiag_empty` — `congr 1` already closed the goal (the two
  lambdas are definitionally equal: membership in the empty finset decides to `false`), so the following `funext`
  found none; (ii) 274:40 "failed to synthesize instance DecidablePred (And (τ z ≠ z))" and 274:19 "rewrite failed"
  in `diagonal_signFun_eq` — the term `if_neg (fun h => …)` carried no type ascription, so the condition of
  `if_neg` was a metavariable when its `Decidable` instance was sought. Every other declaration of the module
  elaborated: 36 axiom reports, of which the 16 non-standard ones are `diagonal_signFun_eq` (`sorryAx`), its 13
  dependents (`phaseFree_of_layerFlowExecutable_free` … `latticeTheory_pair_qm_iff_layerFlow`, all through that
  one lemma) and two `[Quot.sound]`-only reports (`assocPair_symm_apply`, `toEnd_symm_apply`, closed by `rfl`);
  the `first` fallbacks of `signDiag_insert` were not needed (unused-tactic notes). `BridgeOpDrive` was not
  attempted (it imports `BridgeToken`). Failed text kept as `lean/BridgeToken.run38123860471.lean` (sha256
  `417142be…`, equal to the dev blob `e0d3ce0c`).
- 2026-10-11T08:20:00Z — pre-dispatch review for dispatch 2 of 3 (no local Lean): `lean/BridgeToken.lean` — `signDiag_empty`
  guarded with `first | done | (funext p; …)`; `diagonal_signFun_eq` restructured: `by_cases hz : z ∈ signSet τ e a`
  before unfolding, the two conditions stated as typed `have`s (`hc`), then `rw [if_pos hz]; unfold signFun;
  rw [if_pos hc]` and the `neg` twin; nothing else changed. `lean/BridgeOpDrive.lean` (not yet compiled): the two
  injectivity steps written as `refine BridgeConverge.dict_injective ?_` instead of `apply`, and
  `ancBlock_smul_tokOp` given a `simp` fallback; nothing else changed. Expected `lean-axioms` count unchanged: 6096.
- 2026-10-11T08:20:14Z — **dispatch 2 of 3**: dev branch `dev-bridge/r5-bridge2` cut from L (`9f9f8257`) by the same
  plumbing: commit `16e75fbe` (tree `4cae40a2`), the same eight modules and root import lines as dispatch 1 except
  BridgeToken (blob `dda95f6b`, sha256 `23e3dcde…`) and BridgeOpDrive (blob `ce820b34`, sha256 `5d41b3f3…`), both equal
  to `lean/*.lean` here; pushed; `verify.yml` dispatched by the same `gh api` call with `ref=dev-bridge/r5-bridge2`;
  run 38124442150 (head `16e75fbe`, created 2026-10-11T08:20:16Z, event `workflow_dispatch`). Expected `lean-axioms`:
  6096. Waiting; no job or run will be cancelled.
