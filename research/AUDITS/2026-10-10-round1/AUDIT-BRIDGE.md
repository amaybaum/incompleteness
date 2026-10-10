# Coordinator audit — `research/bridge`, round 1

Thread head `5f4089a4500a59943c33ba13656b2530824068c5` (2026-10-10). Base L = `9f9f8257`. Audited: `RESULTS.md`
(sha256 `eac88347fa62fec0…`), `NOTES-B1.md` … `NOTES-B5.md`, `experiments/b1_hidden`, `b2_transcriptions`,
`b3_finite`, `b4_realization`, the three handoff proposals.

## Method

1. **Replay.** Every experiment script re-run with `python3 -I -B` from a clean interpreter and compared byte for byte
   with the committed `.out`/`.err`: 4/4 IDENTICAL (`bridge/REPLAY-LOG.txt`).
2. **Independent check.** `bridge/indep_checkB.py` (own table-level code, reads nothing; decision rule fixed before the
   first run): run 2 **5/5 CONFIRMED**, `INDEP-B-FIXED`, replay identical. Run 1 (kept, `indep_checkB.run1.*`) was 4/5:
   the single mismatch was the coordinator's own witness choice for the `R_z(θ)` row (eigenstate image instead of the
   flow-law witness `R_z(π/2) P_s`), not a thread error; the script header records the change.
   - X1 `tr(cnot · actC R1) = 10/9` (not an algebraic integer), control `tr(cnot · actC cyc3)` integral, `cnot² = 1`,
     `R1³ = 1`.
   - X2 `|⟨cnot, actC O, actT O⟩| = 11520` (24 octahedral rotations).
   - X3 `S`, `cyc3`, `R_z(θ)`, `R1` each move a defect out of K(Z_F) with certified negative witnesses; thresholds
     `−1/2, −1/2, −2/5` against `Q3` controls `1/2, 1/2, 9/20`.
   - X4 `phiW = diag(1,1,−1,1)`, `S_CHSH(phiW) = 14/5` at the stated settings; every defect reaches `14/5`.
   - X5 the measure-and-prepare realization reproduces the K(Z_F) law exactly; probabilities in `[0, 1]`;
     no-signalling marginals; every local threshold on the grid `G = 20`.
3. **Kernel citations.** Every `file:line` the thread cites checked at L (`cite_check.out`, part of the 69/69):
   CompositeDimension.lean:1220–1222 (`phiW`, `cnot_prodState_xplus_z3`), ImplementationLocality.lean:207
   (`redundancy_fails`), CompositeInterface.lean:245 (`lt`), StructuralClosure.lean:261
   (`substratumClass_contextStable`), SubstratumInterface.lean:75 (`IsMonomial`), KInfFoundations.lean:264
   (`ElementaryDrivability`).

## Findings by row

| row | thread label | audit |
|---|---|---|
| V-1 | CONDITIONAL on H-OI_g; the embedded-observation route FAILED | accepted; the synthesis follows from B1–B5 at their labels |
| B1-0 | CERTIFIED identity + [W] membership | accepted; identity verified at L |
| B1-1, B1-2 | CONDITIONAL on L-REG / (A) | accepted at the labels; Theorem B1.1 is a written proof, not formalized |
| B1-3 | FAILED route (L-REG is Bell-local) | accepted; CHSH 14/5 independently confirmed (X4) |
| B1-4 | CONDITIONAL reading of GR.md:326; assumption-watch marker | accepted; recorded in the overview's manuscript-obligation list (hold) |
| B2-1 … B2-5 | FAILED routes / CONDITIONAL transcriptions | accepted at the labels; the exact witnesses replayed; the transcriptions themselves are the thread's [W] and were not re-derived |
| B3-1, B3-2 | FAILED finite-substratum routes; exact obstruction | accepted; X1, X2 confirm the decisive numbers |
| B3-3 | CONDITIONAL on Jordan's theorem [L] | accepted as labelled; the literature input is named, not checked here |
| B3-4 | CONJECTURE B3.C with partial results [W] | accepted as a conjecture |
| B3-5 | CONDITIONAL on the finite subgroups of SO(3) [L] | accepted as labelled |
| B3-6 | CONDITIONAL reduction, witnesses [X] | accepted; X3 confirms the witnesses |
| B4-1 | CONDITIONAL on branch (a) and the general finite response construction | accepted; X5 confirms the law; scope: not the SM/GR lattice representative, (C1)–(C4) not imposed |
| B4-2 | FAILED H-level route without the spectator clause | accepted; X3 confirms the thresholds |
| B4-3 | FAILED as a new bridge | accepted (argument [W]) |
| B5-1 | CONDITIONAL on H-OI_g | accepted; H-OI_g recorded as a newly identified assumption |
| B5-2 | OPEN (not formalized) | accepted; proposed round-2 node |
| B5-3 | FAILED as a theorem at L | accepted; consistent with stage 6 |

**Label changes: none.** No claim was found stronger than its evidence.

## Recorded for the overview

- New assumptions: H-OI_g (availability in the pair context of one sufficient token operation — OI⁺-1 at level H);
  L-REG (locality of registers) as the operational reading of GR.md:326, Bell-local; Jordan's theorem and the
  classification of finite subgroups of SO(3) as [L] inputs.
- Eliminated alternatives: locality of registers as a bridge; fixed finite pair substrata; directed towers of finite
  substrata (for A_miss, off-frame circles, R1); preparation reachability as a new bridge; "K2-local (discrete form)"
  as a theorem at L.
- Round-ready: nothing from this thread yet; Theorem B1.1 as a design module is the natural next step (round 2).
