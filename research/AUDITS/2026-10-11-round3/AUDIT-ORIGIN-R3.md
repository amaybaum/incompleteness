# Coordinator audit — `research/origin`, round 3

Thread head `de9285d6` (2026-10-11; round-3 commits `6240576b` … `de9285d6`). Base L = `9f9f8257`. Audited: the
round-3 rows of `RESULTS.md` (O8-K … O8-V, O10-K … O10-V, O9-K … O9-V, O9-E, the verdicts by node), `NOTES-O8.md`,
`NOTES-O10.md`, `NOTES-O9.md`, `experiments/o8_exclusive`, `o10_pair`, `o9_level2`, `o9_scope`, the design module
`lean/OriginExclusive.lean`, the receipts in `inbox/`, the handoff proposal `O8-O10-O9-round3-findings.md`, `LOG.md`.

## Method

1. **Receipts.** HO-12 v1 and HO-13 v1 copied verbatim (sha256 equal to the overview files at `2a055180`) and
   committed at `6240576b` with the reliance recorded in `LOG.md` (HO-12 items 1 and 4 as the SPEC target; HO-13 item 2
   as O10's target, item 1 only to read what a composite lacks). No earlier LOG entry was changed. Protocol satisfied.
2. **Replay.** Four scripts re-run (`python3 -I -B`, cwd `experiments/`): stdout IDENTICAL 4/4
   (`origin/REPLAY-LOG.txt`).
3. **Independent check.** `origin/indep_checkO3.py` (own code, own exact arithmetic in `Q(ζ₈)`; reads nothing;
   decision rule fixed before the first run): run 2 **7/7 CONFIRMED**, `INDEP-O3-FIXED`, replay identical. Run 1
   (kept) crashed in X6 inside the coordinator's harness (sympy could not integrate a sign-weighted vector integrand as
   a matrix); X1–X5 were CONFIRMED in run 1; no thread claim was involved.
   - X1 (O9-L2R): `⟨mixImage 2 (π/4), transposition, 4-cycle⟩` has order **2304**, contains `−1`, and each generator
     normalizes the real Pauli group (so the whole group does).
   - X2 (O9-L2C): the word `M2·SWAP·M2·SWAP·phaseGate(1,1)` has trace `(3+i)/2`, minimal polynomial `2x² − 6x + 5`
     (not an algebraic integer, so infinite order); the commutant of the generators' conjugation action on `M₄` has
     dimension **2** modulo the coordinator's own prime `2000000033` (3 for the real generators alone, the
     countercontrol); determinants `−1, −1, 1, i`.
   - X3 (O9-L1): the level-one group `⟨rot(π/4), X, diag(i,1), diag(1,i)⟩` has 192 elements and 24 channels;
     independently, the unit columns with entries in `ℤ[i][1/2]` number 24, those in `√2·ℤ[i][1/2]` number 24, the 2×2
     unitaries from same-class orthonormal pairs number 192 and give the same 24 channels.
   - X4 (O9-L1a): ordered four-square representations of `4^k` and `2·4^k`: 8 for 1, 24 otherwise (k ≤ 3).
   - X5 (O9-E): at `π/8` the word `rot·S·rot·S†` has trace `1 + √2/2` (minimal polynomial `2x² − 4x + 1`: infinite
     order); at `π/4` trace 1, order 6.
   - X6 (O10): `phiW = cnot(prodState xplus z3) = diag(1,1,−1,1)`, `S_CHSH = 14/5` at HO-3's settings; the
     controlled-rotation table `(1, 0; 0, C/2)` has partial-transpose eigenvalue `−1/8` and `S = 7/5`;
     `E[sgn(u·λ) λ] = u/2` (exact integral); the lune `{x > 0, z > 0}` has measure `1/4`; the 16 deterministic sign
     patterns give `S ∈ {−2, 2}`.
   - X7 (O8-T4): with every permutation and the readout of one nontrivial cell, the closure of the uniform state has
     exactly `C(2N−1, N) = 3, 10, 35` members for `N = 2, 3, 4`, containing every point mass; every nontrivial cell at
     `N = 3` gives 10; the trivial cells give 1.
4. **Kernel definitions read at L** for the O9 argument: `MixR` (StateMixingCoupling.lean:56, constructors `perm`,
   `phase`, `mix`, `mul`, `smul` with `‖a‖ ≤ 1`, `proj`, `block`, `relabel`), `IsScaledPartialPerm` (one scalar of
   modulus at most one on all nonzero entries, SubstratumInterfaceAudit.lean:231), `phaseGate` (entries 1, i),
   `mixImage`, `InstAvail` (ImplementationLocality.lean:268, constructors `op`, `readout` with the 0/1 `readProj`,
   `coarse`, `bind`, `discard` with `uniformAttach`), `genTheory` (:852), `ancBlock` and
   `discardWith_uniform_conjChannel` (AncillaClosure.lean:457, :461), `DenseUnitaryControl` (DiscreteCompletion.lean:45),
   `denseUnitaryControl_of_fixedGate` with its hypothesis `Irrational (α / π)` (:1522), `fixedGateTheory` (:1926),
   `fixedGateTheory_derivedOI` (:1929), `fixedGateTheory_fixedGateSourced` (:1933). NOTES-O9 §2's Claims 1–5 (Galois
   parity of the class, the contraction and isometry step, the uniform-ancilla averaging over `InstAvail`, the
   rank-one Choi step for Kraus operators of a unitary channel, the 2-adic norm step in the PID `ℤ[i][1/2]`, the
   four-square descent) read against these definitions: sound. The conclusion "the level-one clause of
   `DenseUnitaryControl` fails at `π/4`" follows from the finiteness of the channel set (24) and the compactness of
   the phases.
5. **Kernel citations.** The coordinator's sweep (`cite_check_r3.py`, lines added since `42bc3da6`) finds 34 distinct
   `File.lean:NNN` strings, two of them the thread's own module lines (`OriginExclusive.lean:313`, `:475`, not kernel
   citations); the remaining **32/32 resolve at L**, three whose citing line names a different identifier inspected and
   correct (RouteB.lean:279 `substratumTheory`, CompositionOrder.lean:378 `not_stagePreserving_of_infiniteOrderOn`,
   SubstratumInterfaceAudit.lean:231 `IsScaledPartialPerm`).
6. **Design runs** (`CI-RUNS-R3.md`): 38098314988 (`dev-origin/exclusive` @ `39fd0e67`): Mathlib bridge Build
   **failure**, three errors in `reach_mergeInto` (a `Decidable` instance naming the unrewritten term after `simp`),
   prints 27 standard + 3 `sorryAx` (`reach_mergeInto`, `reach_collectAt`, `reach_pointMass`); 38099172719
   (@ `5df964af`): Build success (3644 jobs, `Built OIBridge.OriginExclusive`), **33/33** prints on
   `[propext, Classical.choice, Quot.sound]`, release gate PASS on every step except `lean-manuscript` (1 problem),
   `lean-axioms` OK (5893 named results, no sorry), 43 receipts hold, legacy 303. Both runs: 32 jobs success, 1
   failure (the gate), nothing cancelled. The dev branch is cut from L (diff = the module and one import line). Design
   evidence only; nothing certified.

## Findings by row

| row | thread label | audit |
|---|---|---|
| O8-K | CERTIFIED (OperationalAssembly.lean:658, :675; CentralObservation.lean:486, :392) | verified at L |
| O8-T1 … O8-T3 | CONDITIONAL ([D], run 38099172719; [K]) | accepted; the module's `ExclusiveOn`, `not_exclusiveOn_of_refines`, `exists_straddle_of_exclusiveOn`, `exclusiveOn_factor`, `substratumTheory_exclusivity_false` read against the rows; the run verified |
| O8-T4 | CONDITIONAL ([D] `reach_pointMass`; [X]) | accepted; X7 reproduces the closures and the point masses independently |
| O8-D | CONDITIONAL ([X] + [W]) | accepted; the kernel-carrier failure of the disguise test rests on O1-T3 at its status, as stated |
| O8-C | CONDITIONAL ([X] X6) | accepted (replayed; not independently recomputed) |
| O8-V | CONDITIONAL; SRC OPEN | accepted |
| O10-K | CERTIFIED (KInfFoundations.lean:425, :427, :351, :449; CompositeDimension.lean:1222, :741, :744, :751; CompositionOrder.lean:378) | verified at L |
| O10-T1, O10-T2 | CONDITIONAL (on the cosine re-preparation law) | accepted; the circle-tower facts replayed |
| O10-T3 | CONDITIONAL ([X] B1–B3; [W]) | accepted; X6 reproduces the bound, the entangled Bell-local table and `phiW`'s `14/5` |
| O10-T4, O10-T5 | CONDITIONAL ([X] B4–B7; [W]) | accepted; the lune measure and the pure conditional states (X6); B4/B5's symbolic uniqueness replayed |
| O10-D | FAILED (as a source) | accepted |
| O10-V | CONDITIONAL | accepted; HO-9 item 6 extends to the continuous form |
| O9-K | CERTIFIED (DiscreteCompletion.lean:45, :1926, :1929, :1933, :1522; ImplementationLocality.lean:268, :852; SubstratumSource.lean:103; StateMixingCoupling.lean:56) | verified at L |
| O9-L2R | CONDITIONAL ([X]; the order of the real Clifford group [W/L]) | accepted; X1 |
| O9-L2C | CONDITIONAL ([X]; [W] + [L] Cartan) | accepted; X2 with a third prime |
| O9-L1 | CONDITIONAL ([W] Claims 1–5; [X] L1a–L1f) | accepted; X3, X4; the written argument read (method 4) |
| O9-S | CONDITIONAL (on O9-L1; [K]) | accepted: `fixedGateTheory (π/4)` has `DerivedOI` and `FixedGateSourced (π/4)` at L and, by O9-L1, not `DenseUnitaryControl`; the kernel theorem's irrationality hypothesis is not dropped by this — it is shown necessary at `π/4` |
| O9-C | CONDITIONAL (on O9-L1) | accepted; the correction applies to HO-9 v1's may-not-assume clause of item 7, whose conclusion stands and whose reason is replaced — HO-9 v2 issued |
| O9-L34 | CONDITIONAL ([X] L3X, L4; [W] + [L]) | accepted (replayed; not independently recomputed) |
| O9-V | CONDITIONAL | accepted |
| O9-E | CONDITIONAL ([X] S1, S2, CC; [W] + [L]) | accepted; X5 |

**Label changes: none.** Precision notes: (i) O9-L1's "192 elements" counts unitaries with their phases, its "24
channels" the conjugation maps — both confirmed; (ii) O9-S is a statement about the canonical fixed-gate theory at one
angle and is in no tension with any certified theorem (the certified density theorem assumes `α/π` irrational).

## Recorded for the overview

- The exclusive measure-and-re-prepare readout, stated in the kernel's vocabulary, is OI-N1's factor property relative
  to the observed algebra: false on the stated access (the native readout is the block pinching of the ancilla values,
  passive on every algebra refining the ancilla value, and one passive readout of any nontrivial cell with the exchanges
  reaches every point mass on any finite carrier), contradicting `readout_is_localLuders` with the structure field
  `readout_avail`; where it holds it presupposes coherence between ancilla values. It is not a source of SRC inside the
  kernel's operational structure; its realizations are token-level models outside the native readout.
- The pair obstruction for re-preparing laws is the Bell bound, not separability: product-law composites reach
  non-separable tables and never exceed 2; a cross-token law reaching `phiW` must take the first readout's setting and
  is then the cone's own conditioning rule with `cnot` given (FAILED as a source). The Kochen–Specker sphere tower carries
  HO-13's token pair (`cyc3` with the exact witness; the stage-crossing datum is `R_z(θ₀)`) — SRC's token half, not
  its pair half.
- `DenseUnitaryControl (fixedGateTheory (π/4))` is false, at level one: by every route of `MixR` and `InstAvail` the
  available unitary channels at level one are the 24 Clifford channels; the kernel theorem's irrationality hypothesis is
  necessary at `π/4`; at `π/8` (also rational) the level-one clause holds. Level two: the real Clifford group (2304)
  with the exchanges, dense up to phase with the quarter phase; levels three and four real: dense.
- New assumption-watch marker: in a generated theory, availability at a level is not the group generated at that
  level — `MixR.block` and `MixR.relabel` import every higher level and `InstAvail` adds protocols; the round-2
  reason "level one is finite" is replaced (HO-9 v2).
- Thread deviations disclosed (no local Lean toolchain, CI the only compile check; one S0 arithmetic slip on a
  countercontrol's trace, outcome as predicted; pre-run edits logged; dev branch cut from L) — noted, no action.
- Routed: HO-17 (origin → bridge, equivalence, countermodels); HO-9 v2 (correction of item 7's clause).
