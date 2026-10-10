# Coordinator audit — `research/equivalence`, round 1

Thread head `8c67c7fbe22ca817858dc6711c413f7a5e3d45db` (2026-10-10). Base L = `9f9f8257`. Audited: `LEDGER.md`
(sha256 `a72a56f5dd13f23b…`), `RESULTS.md` (`92270237fbe5a8d4…`), `NOTES-E2.md` … `NOTES-E7.md`,
`experiments/e2_copy_conj` (run 2; run 1 kept), `e2_drive_trans`, `e3_compress`, `lean/EqvSeams.lean`,
`lean/EqvSeamsControl.lean`, the four handoff proposals.

## Method

1. **Replay.** Three scripts re-run (`python3 -I -B`): stdout and stderr IDENTICAL 3/3 (`equivalence/REPLAY-LOG.txt`).
2. **Independent check.** `equivalence/indep_checkE.py` (own code, reads nothing; decision rule fixed before the first
   run): run 2 **2/2 CONFIRMED**, `INDEP-E-FIXED`, replay identical. Run 1 (kept) was 1/2: the harness stated the
   ellipse control's curvatures backwards (the quartic's four zero curvatures and the circle control were already as
   predicted).
   - X1 the decisive step of R-E2.5: the central section `x⁴ + s⁴ = 1` of Ω₄ has curvature 0 at its four axis points
     (controls: circle 1; ellipse `x²/4 + s² = 1` has 2 and 1/4), so Ω₄ is not an affine image of a ball; with the
     certified TransitiveBody.lean:602 and DenseOrbit.lean:174 this is the negative half of the separation.
   - X2 the drivability data on Ω₄: convexity (the Hessian of `|x|⁴` is `4|x|²I + 8xxᵀ`), central symmetry, `R_z(t)` and
     `cyc3` preserve the body, `cyc3 R_z(t) cyc3⁻¹ = R_x(t)`, `cyc3³ = 1`, `R_x(π) = nflip`.
   The type-covariance instances (R-E2.3) and the compression descent instances (R-E3.1) were replayed, not
   re-derived independently.
3. **Kernel citations.** All 19 `file:line` citations verified at L (`cite_check.out`): CarrierGeneralOIPlus.lean:207
   `oiPlus_iff_qm`, TypedCompletion.lean:850 `typed_determined_iff`, SubstratumSource.lean:136
   `genTheory_qm_of_quantumArchitecture`, TransitiveBody.lean:602, DenseOrbit.lean:174/:398/:403,
   KInfFoundations.lean:590/:632, ImplementationLocality.lean:506/:359/:364, SubstratumSource.lean:77,
   K2Guard.lean:106/:110/:134/:143, QuasilocalCharacterization.lean:359 `canon_unique`, :497 `systemEquiv_dyn`.
4. **Design modules.** Run 38083519826 (`dev-equivalence/kinf-seams` @ `f5367a7a`): Build success (3645 jobs); twelve
   `EqvSeams` declarations (`sharpSeed_eball_of_stage`, `exists_sharpSeed_eball_of_stage`, `…_dense`,
   `actT_mem_maxCone`, `nativeGate2_conj`, `nativeGate_of_conj`, `dim_of_nativeGate2_conj`,
   `three_of_nativeGate2_conj_of_two_le`, `dim_of_nativeGate2_conj_neg`, …) and three `EqvSeamsControl` declarations
   on standard axioms; `lean-axioms` OK (5875, no sorry). Run 38084161796 (`dev-equivalence/kt4-at-l` @ `288f80ec`):
   Build success (3654 jobs); `FourCopyHeadline` `ie1_all`, `parity_all`, `kt4_general_ie1`, `kt4_forward_ie1`,
   `kt4_forward_ie1_kt4`, `kt4_forward_ie1_lt` on standard axioms; `lean-axioms` OK (6015, no sorry). Both gates red
   only on `claims`, `duplicate`, `lean-manuscript` — `CI-RUNS.md`. Design evidence only.

## Findings by row

| row | thread label | audit |
|---|---|---|
| R-E1.1 | OPEN ledger of 22 obligations with statuses at L | accepted; anchors verified |
| R-E2.1, R-E2.2 | CONJECTURE (design run) | accepted; declarations present with standard axioms in run 38083519826 |
| R-E2.3 | CONJECTURE (exact instances) | accepted (replayed; run 1 with two refuted countercontrol expectations kept) |
| R-E2.4, R-E2.6, R-E2.7, R-E2.8 | CONJECTURE [W] (+[L], +[K]) | accepted as labelled |
| R-E2.5 | CONJECTURE (complete written proof with exact checks) | accepted; the decisive negative step independently confirmed (X1); the positive properties are the thread's exact record |
| R-E3.1, R-E3.2, R-E3.3 | CONJECTURE ([W] + [X]) | accepted; HO-6 issued |
| R-E3.4 | CERTIFIED [K at L: import lines] | **precision note:** an exact, mechanically checkable fact about the source tree at L, not a kernel theorem; the overview lists it as [X]-grade (exact) rather than among kernel certifications. Its truth is not in question |
| R-E4.1, R-E4.2 | CONDITIONAL | accepted; the K2 schema's controls are at their audited status |
| R-E5.1 | CERTIFIED [K at L: tree comparison] | same precision note as R-E3.4 |
| R-E5.2, R-E5.3 | CONJECTURE ([W]; design run) | accepted; `kt4_forward_ie1` present on standard axioms in run 38084161796 |
| R-E6.1 | CONDITIONAL | accepted |
| R-E6.2 | CERTIFIED uniqueness; converse OPEN | verified at L (`canon_unique`, `systemEquiv_dyn`); the one-directional statement is correct (§A.34) |
| R-E7.1 | OPEN (readiness judgement) | accepted; S1–S6 listed in the overview as round-ready candidates, none created |

**Label changes: two precision notes** (R-E3.4, R-E5.1): "CERTIFIED" is reserved in the overview for kernel theorems
and landed rounds; these two rows are exact source-tree facts and are carried as [X]. No claim was found stronger than
its evidence.

## Recorded for the overview

- Round-ready candidates: S1 (K∞-Seed from a sharp stage test), S2 (type covariance for K∞-Copy), S3 (Kₙ-DESC), S4
  (the separation of K∞-Trans), S5 (the per-region Level III converse), S6 (the K2 schema: statement and controls,
  heavy proof); ROADMAP wording proposed in the thread's HP-1 (not applied; to land only with the corresponding round).
- Cautions recorded by the thread: the K∞-Copy weakening is not shown to admit any gate copy naturality excludes; the
  Kₙ reduction moves carrier generality into `ContextStable`, the matrix form of the spectator clause (b) needs — not a
  discharge.
