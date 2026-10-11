# Coordinator audit — `research/origin`, round 4

Thread head `7192e3b5` (2026-10-11; round-4 commits `8709fe41` … `7192e3b5`). Base L = `9f9f8257`. Audited: the
round-4 rows of `RESULTS.md` (O11-K … O11-V; O11-S1 … O11-S4; O12-K … O12-V; O13-K … O13-V), `NOTES-O11.md` (with §7),
`NOTES-O12.md`, `NOTES-O13.md`, `experiments/o11_token` (run 2; run 1 kept), `o12_angle`, `o13_ks`, the design modules
`lean/OriginTokenOrder.lean` and `lean/OriginAngle.lean` (with the failed dispatch's copy
`OriginAngle.run38111982910.lean`), the receipts in `inbox/`, the handoff proposal `O11-O12-O13-round4-findings.md`,
`LOG.md`. This is the first audit under the owner's round-4 acceptance criteria (the premise-inventory rule, the
pair-level/full-OI distinction, the invariance/availability distinction); the checks added for them are in method 8.

## Method

1. **Receipts.** HO-20 v1 and HO-22 v1 copied verbatim (sha256 `f36b2448…`, `3a6440f0…`, each equal to the overview
   file at `742c6b2f`, re-checked by the coordinator) and committed at `8709fe41`, with the reliance recorded in
   `LOG.md` item by item before any research step: HO-20 item 3 as the statement of the one-token sourcing target,
   items 5–6 as context and marker, items 1, 2, 4, 7 unused; HO-22 item 5 as O11's question verbatim, item 2 as a
   cross-check only, items 1, 3, 4 unused. The thread also read its own HO-9 v2 and HO-17 as issued and requested no
   correction (three reading notes, one of which — HO-17 item 7's scope sentence — O12 then decided). The three
   coordinator addenda arrived mid-round and were met by appended sections and rows (NOTES-O11 §7; RESULTS O11-S1 …
   O11-S4); no committed row or LOG entry was edited. One cross-branch read (`research/overview` @ `742c6b2f`), logged
   with hashes; the inventory reads were of `research/archive` @ `4dc0321c`, the branch's own base. Protocol satisfied.
2. **Replay.** Three scripts re-run (`python3 -I -B`, cwd `experiments/`): stdout IDENTICAL 3/3
   (`origin/REPLAY-LOG.txt`).
3. **Independent check.** `origin/indep_checkO4.py` (own code: an own class for `Q(ζ₁₆)` over Fractions, sympy exact
   radicals and minimal polynomials; reads nothing from the thread; decision rule fixed before run 1): run 1
   **8/8 CONFIRMED**, every countercontrol False, `INDEP-O4-FIXED`; replay identical.
   - X1 (O12-T1): on every reduced angle `πp/q`, `q ≤ 12`, the direct test — conjugation of `Z` and `X` by `rot α`
     lands in the sixteen-element Pauli set — agrees at every angle with the closed form `q | 4`; on `q ≤ 24` exactly 8
     of 360 grid angles are Clifford (`{0, π, π/2, 3π/2, π/4, 3π/4, 5π/4, 7π/4}`).
   - X2 (O12-T3): `⟨rot(kπ/4), S, X⟩` modulo scalars closes with 8 classes for even `k` and 24 for odd `k`, `k = 0 … 7`
     (BFS on the pair `(GXG†, GZG†)` in `Q(ζ₁₆)`).
   - X3 (O12-T4, O12-T5): `W = rot(π/8) · S rot(π/8) S†` has `det 1`, trace `1 + √2/2`, and no power `W^k`,
     `k ≤ 96`, is a scalar (exact in `Q(ζ₁₆)`); the Chebyshev sequence of that trace has no zero through `k = 400`
     (exact in `Q(√2)`); `tr W(α) = 2cos²α` and `det W(α) = 1` symbolically; on `q ≤ 24` the number `1 + cos 2α` is an
     algebraic integer (monic minimal polynomial) exactly at the 8 Clifford angles (352 of 360 non-integral).
   - X4 (O11-T4): the minimal polynomial of `(3 + 4i)/5` is `5x² − 6x + 5`, not monic.
   - X5 (O11-T6): `⟨rot(π/4), S, X⟩` with scalars has 192 elements and 24 channels; the channel orders in `PU(2)` are
     `{1: 1, 2: 9, 3: 8, 4: 6}` — all in `{1, 2, 3, 4}`.
   - X6 (O13-T1, O13-T2): over seven axes `Π_n = (1 + n·σ)/2` is submonomial exactly for `±z`; the Choi matrix of
     `X ↦ tr(Π X) Π` has rank one and equals `Πᵀ ⊗ Π` at every axis; its single Kraus operator is proportional to `Π`
     (checked at `(3/5, 4/5, 0)`); the Lüders selectors on the configuration basis are `F^z_±`.
   - X7 (O11-S2): `16 + 5 + 21 + 4 + 8 + 12 + 2 = 68`.
   - X8 (O11-T1): monomial unitaries on `Fin 4` with phases `{1, i, (3+4i)/5}` carry each configuration projector to a
     configuration projector (three permutations, two phase patterns, exact).
   - Countercontrols (all False, as expected): the Pauli test at `π/8`; a zero of the Chebyshev sequence; Choi rank
     one for `F_+ + F_−`; `Π_x` submonomial; the BFS at `π/8` closing within 200 classes.
4. **Modules read.** `lean/OriginTokenOrder.lean` (blob `f1ad72e5`, 45 declarations): `Reach` is the set of
   normalized nonzero-weight branches of every `InstAvail` family of the class at the carrier applied to a configuration
   state (feed-forward and the discard of ancillas enter through the constructors, so ancilla-assisted protocols are
   included at the token's carrier); `body` is the closed convex hull; `availData` ranges over conjugations by
   unitaries whose one-outcome channel is `InstAvail` at the carrier; ORD∞ is the kernel's `CompositionOrder.OrdInf`
   over these. `finiteOrderOn_of_reach_diag` carries each configuration state to a configuration state through
   `eq_cfg_of_diag` (a diagonal rank-one projector has one nonzero entry) and fixes the diagonal body after a common
   period (`exists_return`, `exists_common_period` at L); `reach_diag_of_submonomial` uses `realized_of_instAvail` at
   L. The statements of `substratum_not_ordInf`, `permClass_not_ordInf`, `substratumTheory_datum_finiteOrderOn`,
   `exists_nonsubmonomial_of_ordInf`, the frame-phase theorems, `coherent_of_ordInf`, `ordInf_of_coherent`,
   `ordInf_iff_coherent_of_extends`, `fullClass_ordInf`, `substratum_obstruction`, `obsTheory_obstruction` are those
   of the rows. **Precision:** the finite-order statement is about unitary conjugation data on the thread's own body;
   reversible data that are not unitary conjugations (O11-T7) and the kernel's completed chart body (O11-S3, (L-O))
   are written arguments, exactly as the rows say. `lean/OriginAngle.lean` (blob `f4da8c3d`, 52 declarations):
   `RotClifford` is Pauli-set invariance under conjugation by `rot α`; `rotClifford_iff` uses `Gen2.rot_int` and
   `Gen2.pauli_conj` at L for the converse; the reduction lemmas `mixR_of_int_mul`, `availExt_of_int_mul`,
   `levelOneClause_pi_div_four_of_rotClifford` are by induction on `MixR`; `Gen2FiniteUpToScalar` is the shape of the
   kernel's `gen2_multiple_finite_upToScalar`; `not_gen2Finite_pi_div_eight` is the Cayley–Hamilton and parity
   argument; `AngleWeakenedLevelOne`, `RationalDensityInput`, `BalancedFailureInput` are definitions and
   `angleSuffices_iff` takes the two inputs as hypotheses — nothing in the module proves density at a rational angle
   or the failure at `π/4`, as the rows say. `oddPair_odd` prints on `[propext, Quot.sound]`.
5. **Written arguments read.** O11 §0.6 (an available deterministic family with an available inverse maps the
   simplex of configuration-diagonal states onto itself affinely, hence permutes its vertices): sound as [W]; §0.7
   (the kernel's completed chart body of the token is affinely that simplex, every effect value depending only on
   the diagonal): sound as an argument, and the passage to the kernel's `StageCompletion`/`CompletionAction`
   construction is exactly (L-O), left OPEN — correctly. O12 §0.4–0.5 (a rational non-Clifford angle gives an
   infinite-order word, since a finite-order element of `SU(2)` has an algebraic-integer trace and the nonzero
   algebraic integer `cos 2α` has all conjugates in `[−1, 1]` with integer norm; the image in `SO(3)` then holds a
   quarter-turn about `z`, a half-turn about `x` and a rotation about `y` moving the `z`-line, so its closure is
   `SO(3)` by the classification of closed subgroups [L]): sound, exact on the grid by X3; §0.7 (the echo doubles the
   angle): verified against the kernel's `echo_identity` statement at L, which isolates `rot (2α)` on the chosen block.
   O13 W1 (Choi rank one forces every Kraus operator to be a multiple of `Π`): sound, X6; W2 (composition with
   `realized_of_instAvail`, every branch a finite sum of conjugations by class members at the carrier): sound against
   the kernel signature at ImplementationLocality.lean:530; W3–W5: sound, X6 for W3.
6. **Kernel citations.** The coordinator's sweep (`cite_check_r4.py`, lines added since `de9285d6`) finds 78 distinct
   `File.lean:NNN` strings; three are the thread's own module lines (`OriginTokenOrder.lean:653`,
   `OriginAngle.lean:181`, `:624`), not kernel citations; the remaining **75/75 resolve at L**
   (`cite_check_r4_origin.out`): 34 with the named identifier in the window, 27 naming no identifier, and 14 window
   misses inspected by hand — each cited line is the declaration the row means (`IsSubmonomial` :98,
   `InfiniteOrderOn` :51, `substratumTheory_not_layerFlowExecutable` LiftAudit:200,
   `observationalIndependence_of_implementationLocality` :957, `inertSpectator_iff_parallelReferenceExtension` :233,
   `qutrit_of_parallel` :474, `psd_iff_trace_nonneg` :84, `psd_trace_mul_nonneg` :917, `DerivedOI.implementationLocality`
   RouteB:149, `permClass` :236, `fullClass` :374, `echo_identity` :844, `fixedGateTheory_derivedOI` :1929) and
   StateMixingCoupling.lean:655 opens the cited range `:655–:682` (`mixR_countable_upToScalar` at :662). All correct.
7. **Design runs** (`CI-RUNS-R4.md`): 38108620996 (`dev-origin/token-order` @ `35d326a3`): Build success,
   `OriginTokenOrder` **45/45** prints on `[propext, Classical.choice, Quot.sound]` (two wrapped over log lines, joined
   and counted), `lean-axioms` OK 5905, gate red only at `lean-manuscript`; run completed 32 success, 1 failure (the
   bridge job through the gate). 38111982910 (`dev-origin/angle` @ `9dd6a173`): Build **failure**, one error at
   `OriginAngle.lean:181` (the rewrite direction of `blockOf_mul`), 52 prints: 46 standard, `oddPair_odd` on
   `[propext, Quot.sound]`, 5 `sorryAx` (`blockOf_gen2_mem` and its four dependents), gate skipped; run completed
   32/1. 38112242400 (`dev-origin/angle` @ `f0cd9272`, the one rewrite reversed): Build success, `OriginAngle`
   **52/52** on standard axioms (51 on the three, `oddPair_odd` on two), no `sorryAx`, `lean-axioms` OK 5912, gate red
   only at `lean-manuscript`; at the time of this audit the run was still in progress (29 success, 1 failure, two A42
   shards pending). Nothing cancelled. Both dev branches are cut from L and differ from it by the module and one
   aggregator import line (verified); the thread's module copies equal the dev-branch blobs (verified). Design
   evidence only; nothing certified.
8. **Acceptance-criteria checks (owner, 2026-10-11).**
   - *Hypothesis classification against the inventory.* Every round-4 row carries its hypotheses by inventory id or
     as introduced; O11 has no introduced hypothesis; O12 introduces the gate (`FixedGateSourced α`, recorded by the
     inventory's I4.239 as an independent datum) and the angle condition; O13 introduces the law it tests and, in the
     sufficiency construction, a coherent unitary. The sample of inventory records checked (I4.67, I4.241, I4.242,
     I4.26, I4.239, I4.127, I4.187, I3.96, I3.99, I3.108, I3.145, I2.30) has the kinds and levels the rows assign.
   - *Pair-level versus full-OI insufficiency.* No row claims independence. O11-S1 states N11 (finite order of every
     available unitary datum on the matrix-level token body, in a model satisfying every M-level row checked against
     it, 16 NOT REACHED rows included, and failing only rows flagged as OI⁺ completion conditions, packages or
     endpoints); O11-S2 classifies all 68 NOT REACHED rows (counts verified; the class-(a) kernel lines resolve to the
     theorems of the stated names); O11-S3 scopes the OPEN to (L-O). **Precision:** the RESULTS preamble and O11-V say
     "the datum is an additional principle, not a consequence of the items the obstruction satisfies"; read as the
     non-entailment by the items listed in O11-T2 — which is what the words say — this is correct, and the thread's
     own §7 supersedes any wider reading. The verdict form is the owner's third form (a precisely scoped OPEN) with the
     narrower M-level statement N11 established; it is not an "independent bridge" verdict and is not labelled as one.
   - *Cone invariance versus operational availability.* Every row names its kind; the definitions behind O11
     (`InstAvail`-reachable states, `InstAvail` channels) and O13 (`InstAvail` families, `realized_of_instAvail`) are
     availability statements; `RotClifford` is a property of the datum's matrix, as labelled; no row uses (b), (T) or
     A_miss.
   - *Defeated alternatives named.* O12-T3, O12-T4, O12-T6, O13-T2, O13-T3, O13-D each name the alternative in the
     coordinator's words.

## Findings by row

| row | thread label | audit |
|---|---|---|
| O11-K | CERTIFIED [K] (kernel facts at their lines) | accepted; lines verified at L |
| O11-T1 | CONDITIONAL ([D] run 38108620996; [X]) | accepted; the module read (method 4); X8; the design run verified |
| O11-T2 | CONDITIONAL ([D] + [K]; rule independence [W]) | accepted; the discharging kernel lines verified (method 6) |
| O11-T3 | CONDITIONAL ([D]) | accepted; `exists_nonsubmonomial_of_ordInf` read |
| O11-T4 | CONDITIONAL ([D]; [X] E3) | accepted; X4; the frame-phase theorems read |
| O11-T5 | CONDITIONAL ([D]; [X] E4) | accepted; both directions read, witnesses as the row states (§A.34) |
| O11-T6 | CONDITIONAL ([X] E5, E6; O9-L1 [W]; [K :109]) | accepted; X5 (192, 24, orders {1,2,3,4}), X3 (`π/8`) |
| O11-T7 | CONDITIONAL ([W]; [X] E8) | accepted; §0.6–0.7 read (method 5) |
| O11-D | FAILED as an independent target | accepted; the identification with SRC's content read |
| O11-V | CONDITIONAL; SRC OPEN | accepted with the precision of method 8 (the "additional principle" clause as the M-level non-entailment, scoped by O11-S1/O11-S3) |
| O11-S1 | CONDITIONAL ([D] + [K]) — N11 | accepted; the model's definitions read; the statement is availability, M-level |
| O11-S2 | CONDITIONAL ([K] per row; the class assignment [W]) | accepted; X7; sample records and class-(a) lines verified |
| O11-S3 | OPEN — (L-O) | accepted; correctly scoped; no independence claimed |
| O11-S4 | as the rows | accepted |
| O12-K | CERTIFIED [K] | accepted; lines verified at L (`echo_identity` read in full) |
| O12-T1 | CONDITIONAL ([D]; [X] A1) | accepted; X1; `rotClifford_iff` read |
| O12-T2 | CONDITIONAL ([D]) | accepted |
| O12-T3 | CONDITIONAL ([D]; O9-L1 [W + X]) | accepted; X2; the reduction lemmas read |
| O12-T4 | CONDITIONAL ([D]; [X] A5; density [W + L]) | accepted; X3 (det, trace, no scalar power to 96, Chebyshev to 400); the density argument read |
| O12-T5 | CONDITIONAL (O9-L1; density [W + L]; [X] A3–A4; [K :762]) | accepted; X3c (integrality exactly at the Clifford angles on `q ≤ 24`) |
| O12-T6 | CONDITIONAL ([D]) | accepted; `angleSuffices_iff` and the two controls read; the inputs are hypotheses, as stated |
| O12-T7 | CONDITIONAL; all-level statement OPEN | accepted; the echo statement verified at L |
| O12-D | FAILED as an independent principle; exact as a weakening | accepted |
| O12-V | CONDITIONAL | accepted |
| O13-K | CERTIFIED [K] | accepted; lines verified at L |
| O13-T1 | CONDITIONAL ([W] + [K] + [X]) | accepted; X6 (Choi rank one, the Kraus operator); W2 read against :530 |
| O13-T2 | CONDITIONAL ([X] K1, K4; [W]; [D] via O11-T1) | accepted; X6 (`±z` only; the Lüders selectors) |
| O13-T3 | CONDITIONAL ([K] + [W] + [X]) | accepted; the countable bound is all that is claimed, as the row says |
| O13-T4 | CONDITIONAL ([W]; [X] K3) | accepted |
| O13-D | FAILED as an independent source | accepted |
| O13-V | CONDITIONAL | accepted |

No label changes. The thread's recorded deviations (dev branches cut from L; one aggregator import line per dev
branch; no local Lean toolchain; pre-run edits logged for all three scripts; `o11_token` run 1 failed on its own
permutation test and is kept; the O12 module's first build failed on one rewrite direction and was repaired with the
last dispatch, so O13 has no module; addendum 3 met by appended sections and rows; one missed S0 estimate in O13 with
the decision quantity met; scratch files confined to `scratchpad/origin-r4/` after a shared-scratchpad note) are each
in the LOG and change nothing audited here.

## Handoff items

- The proposal `O11-O12-O13-round4-findings.md` (items 1–7) → **HO-27** to the bridge, equivalence and countermodels
  threads: N11 and the (L-O) OPEN; ORD∞ ⟺ coherence by directions; the angle condition at level one with its scope;
  the re-preparation law as an operation datum; item 7 (HO-17 item 7's scope sentence sharpened to the level-one
  characterization, CONDITIONAL on O9-L1 and the density argument) carried in HO-27 rather than as an HO-17 v2, since
  HO-17's sentence stays true as a scope guard.
