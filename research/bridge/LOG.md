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
