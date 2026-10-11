# Round-4 audit — `research/bridge` (B14–B17) at `a34d20b5`

Coordinator's audit of the bridge thread's round 4 (eight commits `7abe4da4..a34d20b5`, all under `research/bridge/`),
from the certified base L = `9f9f8257`, under the owner's round-4 acceptance criteria. Written 2026-10-11. Nothing here
is CERTIFIED; every label is the thread's unless a finding says otherwise.

## Method

1. **Receipts.** The twelve handoffs addressed to the bridge (HO-4, HO-5, HO-6, HO-9, HO-9 v2, HO-13, HO-16, HO-17,
   HO-18, HO-19, HO-24, HO-25) are in `inbox/`, each byte-identical to the overview blob at `742c6b2f` (git blob ids
   compared); the six new this round were received at `d877be82`. HO-20 … HO-23 are the bridge's own and were read for
   item numbering only, not copied; HO-26 is not addressed to it. The LOG records reliance item by item, and the
   "may not assume" clauses are honoured where it matters: HO-17 item 8 binds every availability predicate (checked:
   `PairAvailAt` is `InstAvail` at the carrier, every protocol, through `genTheory_availExt_iff`); HO-24 item 1's lift
   is re-derived before use (`b17_tower.py` K1); nothing sources K∞-Trans through self-duality (HO-19).
2. **Provenance.** The three dev branches `dev-bridge/r4-avail` (`152094b5`), `r4-conv` (`ca48c4c4`) and `r4-final`
   (`bf8ba746`) are each one commit cut from L (merge-base = L), changing `verification/lean-mathlib/OIBridge.lean`
   (import lines) and the design modules only. The thread's `lean/` copies equal the dev blobs of the dispatch they cite
   (`BridgeAvail` c88aafd5 on all three; `BridgeAvailFull` 192fca74 on `r4-conv` and `r4-final`; `BridgeConverge`
   d09c7050 and `BridgeReachDim` bf3e5564 on `r4-final`; the failed copies `*.run38115337569.lean` equal the `r4-conv`
   blobs 49ab5c89 and 8ccee631); `EqvK2Schema` on the dev branches equals the equivalence blob 659ae36c at `c10dbaee`;
   `BridgeDictionary` and `BridgeReach` equal the round-3 copies. Nothing outside `research/bridge/` changed on the
   thread branch; no pull request, no write to `main`.
3. **Replays.** All five round-4 scripts replay byte-identically on stdout (`bridge/REPLAY-LOG.txt`): `b14_preflight`,
   `b16_preflight`, `b17_tower` at the first attempt; `b14_fullmodel` and `b15_preflight` resolve their inputs relative
   to `experiments/` (as their headers say) and were re-run from there. The committed `.err` files carry the thread's
   `exit 0` line; the coordinator's are empty — the only difference.
4. **Independent check.** `bridge/indep_checkB4.py` (decision rule fixed in the header before run 1; reads nothing the
   thread wrote; exact arithmetic in Q(i) and, for the stage n = 3 of B17, in Q(ζ₈)): run 1 **8/8 PASS, countercontrols
   CC1–CC5 all False, verdict INDEP-B4-FIXED**, 19 s; replay byte-identical (`bridge/RUN-HISTORY.txt` for one
   informational flag inside X4's message). Coverage: X1 the lattice obstruction (|w|² = 1, w⁴ = (−527 − 336i)/625,
   no nonzero multiple of diag(1, w) has equal fourth powers, diag(1, i) admitted); X2 `U_J` (literal, unitary, two
   nonzero first-row entries, 2U_J = (1 − i)·X·[[1, −1], [1, 1]]·S³ exactly, Ad(1 ⊗ U_J) = actT cyc and
   Ad(1 ⊗ diag(1, w)) = actT R_z(θ₀) and Ad(1 ⊗ X) = actT nflip on all 16 basis tables, (P) on an instance); X3 the
   two-token stated access with the quarter phase (the thread's six generators: order 3072, every element on the
   lattice, no scalar multiple of 1 ⊗ diag(1, w) or 1 ⊗ U_J; the kernel-faithful monomials of `MixR ∅` at the pair
   carrier, all 24 permutations and the four single-configuration quarter phases: order 6144, containing the former
   and 1 ⊗ S, with the same exclusions); X4 Table A2 (199 rows, 118/68/13, the 68 NOT REACHED ids fixed in the script
   from the coordinator's own parse, R6's `TALLY Q3 {'NOT': 68, 'SATISFIES': 131}` and `CHECK (2) Q3 column has no
   FAILS PASS`); X5 B15 (rank 16, coordOf∘dict = id, the transfer identity at three rational points of the circle, the
   unitary scaled partial permutations of one token are exactly c·1 and c·X, nflip permutes Z_F, ⟨nflip, R_z(π/2)⟩ has
   order 8 without R_z(θ₀), R_z(θ₀) of infinite order, PSD preserved, e01 moved); X6 B16 (charts, prodDet = 5e − 6 with
   real part ≤ −1 at six exact points of the circle, the block-diagonal SU(2) × SU(2) carries 30 random vectors to
   products, 7 < 8); X7 G₃₈₄ modulo scalars (384), the orbit of h* (192 rays), overlaps in [25/2048, 13/16] over 18336
   pairs, the memberships of CNOT, 1 ⊗ Z, 1 ⊗ S, 1 ⊗ X, ζ₈ ∉ Q(i); X8 the n = 3 certificate: for every one of the 192
   orbit defects the projector onto V h_j (V = 1 ⊗ diag(1, ζ₈)) lies in K* (every squared overlap ≤ 400/401, decided by
   the exact sign of p + q√2) and pairs to 1 − c* = −1/400 with V d_j V*, so V d_j V* ∉ K; at n = 2 no defect is
   certified (positive control), and the identity certifies none (CC5).
5. **Citations.** `cite_check_r4_bridge.out`: 63 distinct `Name.lean:NNN` citations in the lines added since the
   round-3 head `7abe4da4`, all 63 resolved at L; 19 named-and-found by the checker's backtick heuristic, 40 with no
   backticked identifier on the citing line (the Python row table and prose), 4 with names not in the window. A
   supplementary pass with plain-text identifiers (`cite_supp_b4.py`, 33 matched) and a reading of the other 30 by hand
   find every cited line to be the intended declaration (`completedOI_iff_physical`:110,
   `observerRecursion_of_embeddedObservation`:217, `instAvail_transport`:644, `genTheory_availExt_iff`:909,
   `oiPlusLocal_iff_qm`:1070, `derivedOI_qm_iff_layerFlowExecutable`:812, `obsTheory`:769, `ball3Drive`:449, …).
   One citation is correct as a line and wrong as a chain: finding F1 below.
6. **CI.** The three `workflow_dispatch` runs verified from the run and job records and the saved job logs (the
   GitHub job-log tool, tail 5000 lines; `joblog_parse_b4.py`): `CI-RUNS-R4.md`. The complete dispatch-2 log, which
   would hold `BridgeReachDim`'s error block, is served from the blob host that neither the job-log tool (capped at the
   last 5000 lines whatever the requested tail) nor the built-in `gh` reaches; the thread's statement that the failure is
   undiagnosed is confirmed, not repaired.
7. **Lean statement review** (the owner's requirement: statements, hypotheses, dependencies, axiom reports — a green
   build is not the theorem). The four modules read in full; definitions compared with the notes; the kernel theorems
   they use read at L.
   - `BridgeAvail` (61 prints, all standard in runs 1 and 3): `PairAvailAt 𝓘 arch U n` is `availExt n Unit` of the
     one-outcome conjugation by `pairOp U n = (1 ⊗ U) ⊗ 1ₙ` in `genTheory 𝓘 arch (Fin 2 × Fin 2)`, i.e. `InstAvail` at
     `(Fin 2 × Fin 2) × Fin n` (every protocol, blocks and relabellings of members); `TokenAvailAt` likewise. The ray
     step is the kernel's `exists_scaled_mem_of_instAvail_unitary` (MicroscopicReversibility.lean:251, for an
     architecture and a nonempty carrier). `QuartLattice` = submonomial with equal fourth powers; `permClass` and
     `MixR ∅` lie on it (the latter by induction over the eight constructors, the datum case empty). The refutations
     `not_pairAvail_zPh_of_lattice` etc. hold for every architecture on the lattice and every `n > 0`; the
     countermodels `statedAccess_obstruction` (SourcedOI, the sealed core; four refutations), `quarterAccess_obstruction`
     (DerivedOI; four refutations) and `monomialInterface_split` state exactly what RESULTS B14-2/B14-3 say; (P) is
     `pairOp_prod`. No `sorry`, `admit`, `axiom` or `maxHeartbeats`.
   - `BridgeAvailFull` (50 prints, all standard in runs 2 and 3): `latticeClass` = `IsSubmonomial ∧ QuartEq`; the
     seven class properties; `latticeTheory = genTheory latticeClass`; `latticeTheory_derivedOI` builds the kernel's
     five conjuncts (`DerivedOI` at RouteB.lean:141 verified); the sealed core is transported from `permTheory` along
     the inclusion by `genTheory_mono` (ImplementationLocality.lean:919); `lattice_refutes` (pair and token, every
     `n > 0`); `pairAvail_of_control` is an instance of `HasCompositeUnitaryControl` (OperationalAssembly.lean:665,
     `∀ n U, Uᴴ U = 1 → availExt n Unit (conjChannel U)`); `latticeTheory_not_qm` goes through `physical_of_exactAll`
     (third conjunct = control, verified at PhysicalCharacterization.lean:295–306); `obs_zPhase_unavailable` and
     `obs_twoInRow_unavailable` hold for every kernel substratum and rule (obsTheory = permTheory on the configurations,
     :769). Imports: kernel modules and `BridgeAvail` only.
   - `BridgeConverge` (21 prints, all standard in run 3): `pauli`, `tokMat`, `dict` converge by `rfl`;
     `transferClause_iff` proves both directions against `BridgeDictionary.TransferClause` (:343, the existential
     form); `transferClause_Q3` is `PosSemidef.mul_mul_conjTranspose_same`; `transfer_counter` is a genuine
     countercontrol. Imports `EqvK2Schema` (used: `coordOf`, `dict_coordOf`, `dict_injective`, `Q3`).
   - `BridgeReachDim` (32 prints, all standard in run 3): `exists_not_mem_ranges` from `ContDiff.dimH_range_le` and
     `dense_compl_of_dimH_lt_finrank` with `finrank ℝ (ℝ × ℂ³) = 7 < 8`; `avoid_of_curves`, `avoidA_of_curves`;
     `reachUnitary_of_curveCover` and `reachAnti_of_curveCover` give the conclusions of `ReachUnitary` and `ReachAnti`
     (BridgeReach.lean:126, :132) — the anti form with no coset condition, stronger than `ReachAnti`'s hypotheses;
     `curveCover_of_countable` by constant curves. The import of `EqvK2Schema` is the only reference to it in the file
     (build order, as declared).
8. **Acceptance criteria.** Every result row names its reading (invariance or availability); every hypothesis is an
   inventory item at its L status or flagged introduced (the phase intervention at θ₀, I2.33; the datum at π/4; claim
   (D) [A]; Jordan and Cartan [L]); pair-level and full-model independence are kept apart (V-4 (i) versus (ii)); the
   defeated alternatives are named in the owner's words.

## Findings by row

- **B14-1 … B14-4** — labels as recorded; B14-2's "independence by models" is read at level M per B14-5 (correct:
  the models were checked against named kernel predicates, not the 68 rows).
- **B14-5** — availability implies invariance through the Kronecker composite and the converse fails: both sides
  [D] (`transferClause_Q3`, `lattice_refutes`), confirmed by statement.
- **B14-6, the full-model verdict** — the coordinator re-read the 68-row classification against the inventory
  records and the kernel at L. SAT 34: 17 module theorems [D] (statements verified), 7 kernel theorems [K]
  (verified at their lines), 8 written statements [W] about the PSD four-token composite and the ball token (I3.134,
  I3.136, I3.141, I3.154, I3.157, I3.158, I3.96, I3.99 — plausible for the quantum composite, not re-derived), 1
  [W]+[D], 1 [A]. NA 5: scope statements, correctly so. HARMLESS 29: for 27 the cited kernel theorem exists at its
  line with the stated direction, and its side hypotheses are rows FM satisfies (`IteratedAncillaClosure` for
  `control_of_phaseFree`, `DerivedOI` for `qm_of_derivedOI_pairFlowSourced`, the definitions for
  `PhysicalCompletionConditions`, `SubstantiveCompletion`, `ShadowQuantum`). **F1 — two chains are defective.** I4.56
  (`LayerFlowExecutable`) and I2.34 (the layer-flow form) cite `derivedOI_qm_iff_layerFlowExecutable`
  (LiftAudit.lean:812), whose hypothesis `SubstratumAvail T` (:745, every family available in the substratum theory
  is available in `T`) **fails for FM**: the substratum theory makes `zPh` available and the lattice theory does not
  (`lattice_strict_in_substratum`). The proof of `phaseFree_of_layerFlowExecutable` (:783) consumes it through
  `diagonal_avail` for diagonal phases at general angles, which FM lacks by construction. So the two rows are not
  HARMLESS by the cited kernel chain, as the thread's own rule requires. They do imply the conclusion by a written
  argument at the token carrier: for `S = Fin 2` and σ the exchange, `gateFlow (levelPerm σ n) t` is the token's
  `R_x`-type flow with the ancilla a spectator at every level; with the quarter phase (available, `DerivedOI`) and
  `avail_conj_mul` [K] the generated group on the token is SU(2) (Euler angles), so every token unitary — `zPh` and
  `uJ` among them — is available at every level, which is the conclusion itself. Disposition: the verdict "no
  HARMFUL row" stands with I4.56 and I2.34 at HARMLESS [W]; the thread's evidence column is wrong for these two rows
  and its scope sentence should say that two of the 29 rows rest on a written implication; label CONJECTURE
  ([D] + [A] + [W]) unchanged. Carried in HO-33 as a correction item for round 5.
  Also recorded: FM's pair cone `Q3` is the kernel's ambient PSD cone (every `genTheory` has it), not a cone
  generated by FM's operations — the thread says so (§8.5); the availability verdict does not depend on it.
- **B14-7** — confirmed; S0-19's withdrawn clause verified against `r4_tables.out`:141 ("operational availability
  open for Q3 likewise"); gem ELABORATING, as the thread concluded against its own prediction.
- **B14-8, V-4** — the standing-row audit is sound as far as checked (V-2 (iii), B9-1: `TransferClause` is an
  invariance clause by its definition); V-4 (i) states pair-level independence and leaves the full-model status of
  (b) OPEN, as the owner's distinction requires.
- **B15-1, B15-2, B15-3** — confirmed ([D] by statement; X5 for the two defeated clauses: the stated access
  transfers {id, actT nflip}, which permute Z_F, so K(Z_F) satisfies it; the quarter access transfers a group of order 8
  without R_z(θ₀)). B15-2 is CONDITIONAL on the clause, which nothing at L sources — correct.
- **B16-1, B16-2, B16-3** — confirmed ([D] by statement; the Cartan link [W+L] is sound and correctly left
  unformalized; the limit at dimension two is real: 2 + 6 = 8).
- **B17-1** — confirmed, with every one of the 192 certificates re-derived exactly in Q(ζ₈) (X8); CONJECTURE (exact
  computation) and CONDITIONAL on HO-24 items 4 and 6 for the exoticness, as stated.

No label changes. One correction item (F1).

## The owner's three objectives, as the bridge thread's round 4 answers them

1. *A sufficient bridge H with A + H ⇒ b*: none derived. The candidates named this round are defeated or need an
   introduced resource; H-T's token clause is the operational reading of K∞-Drive at θ₀ (B14-7).
2. *Independence and minimality of H*: the availability of `actT R_z(θ₀)` (and of `actT J`) with RESPECT and product
   behaviour is independent of every stage-6 item that does not itself imply composite unitary control or QM —
   full-model, relative to the inventory, with F1's two rows at [W]. Four weaker alternatives are shown to fail in the
   owner's words (the transfer clause for the stated access — K(Z_F) satisfies it; a finite group; a group whose
   identity component has dimension at most one; a finite stage).
3. *Bridge ≠ equivalence*: FM satisfies the transfer clause for every class while `zPh` is unavailable, so (b) does
   not imply H-T; availability implies invariance, not conversely.

## Deviations and notes

1. `BridgeReachDim` was rewritten for dispatch 3 without a diagnosis of its dispatch-2 failure (log tail limit,
   confirmed by the coordinator); the failed text is kept. The rewrite built 32/32 standard.
2. `BridgeReachDim` imports `EqvK2Schema` for build order only (verified: the import is the only reference).
3. The expected axiom count for dispatch 2 was mis-summed (6082) and corrected in the LOG (6078); the coordinator's
   recount agrees (222 prints on that tree, four short names recurring) and gives 6083 for dispatch 3 (227 − 4 + 5860),
   exactly the gate's figure.
4. Handoff-proposal numbering collides across threads (bridge HP-11 … HP-14, equivalence HP-11 … HP-13,
   countermodels HP7 … HP9); the coordinator's index names the thread with every HP from this round on.
5. NOTES-B15's S0-7 cell contains `|c|`, which breaks the table's rendering; left as pre-run text.
6. In dispatch 2 `BridgeConverge` printed 20 of 21 reports: 14 standard, 4 `sorryAx`, two error-recovery artifacts
   (`transferClause_Q3` "does not depend on any axioms", `Q3_phase_invariant` listing itself) and `pauli1_unitary`
   unprinted (unknown constant) — consistent with the thread's "14 not downstream of the four".

## Handoff items

- HO-33 (bridge → origin, countermodels, equivalence): FM; the verdict with F1's amendment; K∞-Drive's two readings;
  availability ⇒ invariance, not conversely; the standing-row audit; the correction item.
- HO-34 (bridge → equivalence, countermodels): one dictionary; the transfer clause in table form; two weaker clauses
  defeated.
- HO-35 (bridge → countermodels, equivalence): B7-1 under countable C¹ curve covers; dimension at most one through
  Cartan; "a group" defeated.
- HO-36 (bridge → countermodels, equivalence): HO-24's cone along the tower, first failing stage n = 3; "a finite
  stage" defeated.

## Evidence

| item | pointer |
|---|---|
| thread head | `research/bridge` @ `a34d20b5` (round 4: `d877be82` … `a34d20b5`) |
| receipts | 12/12 byte-identical to the overview at `742c6b2f` |
| replays | `bridge/REPLAY-LOG.txt` (5/5 identical) |
| independent check | `bridge/indep_checkB4.py` (sha256 0c497a8a…), `.out` (run 1, 2a892a56…), `.replay.out` (identical), `RUN-HISTORY.txt` |
| citations | `cite_check_r4_bridge.out` (63/63 resolved), `cite_supp_b4.py` / `.out` |
| CI | `CI-RUNS-R4.md` (runs 38110368244, 38115337569, 38117986499); logs parsed with `joblog_parse_b4.py` |
| hashes | `EVIDENCE-HASHES.txt` (46 bridge files at the commit that last wrote each) |
