# Coordinator audit — `research/origin`, round 1

Thread head `4cec62c9ae9178b45512133abab37b2d9f59847d` (2026-10-10). Base L = `9f9f8257`. Audited: `RESULTS.md`
(sha256 `a3b3c17969b32fff…`), `NOTES-O1.md` … `NOTES-O4.md`, `experiments/o1_envelope`, `o1_fieldneutral`,
`o2_mechanisms`, `o3_continuous`, `o3_density` (run 2; run 1 VOID kept), `o4_dependency`, `lean/OriginEnvelope.lean`,
the handoff proposal O4-1.

## Method

1. **Replay.** Six scripts re-run (`python3 -I -B`): stdout and stderr IDENTICAL 6/6 (`origin/REPLAY-LOG.txt`).
2. **Independent check.** `origin/indep_checkO.py` (own code, reads nothing; decision rule fixed before the first run):
   run 2 **5/5 CONFIRMED**, `INDEP-O-FIXED`, replay identical. Run 1 (kept) was 4/5: the per-instance results were
   already right; the harness's unitarity control used phases (`exp(iπ/7)` etc.) that sympy does not reduce exactly;
   run 2 uses closed-form algebraic phases.
   - X1 (O1-T1) `Ad U` commutes with computational-basis dephasing iff `U` is monomial, on 14 unitary instances
     (9 monomial, 5 not: `H`, `√X`, `R_y(π/3)`, the 3×3 Fourier matrix, a 3×3 real rotation).
   - X2 (O1-T2) the qubit sandwich visibility is `2|a|²|b|²` symbolically; at the balanced angle the coherent and
     dephased probabilities are `1` and `1/2` (the owner's witness `(1, 1/2)`).
   - X3 (O4-I1) `cyc3 = R_z(π/2) R_x(π/2)`, `cyc3 R_z(t) cyc3⁻¹ = R_x(t)`, `cyc3³ = 1`.
   - X4 (O3-T2) `R_x(π/2) e_z` is pure and balanced for the frame readout; `R_x(π) = nflip`.
   - X5 (O3-T7) two Hadamards on overlapping pairs of three states generate an element with `2 cos θ = −3/2`
     (not an integer): infinite order; control `(HS)²⁴ = 1` at level two.
3. **Kernel citations.** All 43 `file:line` citations of the thread verified at L (`cite_check.out`), including the
   composition behind O1-T4b (InstrumentRealization.lean:628 `onesClass_arch`, :833 `isometry_fixes_ones`,
   :508 `onesClass_gateFlow`; SubstratumSource.lean:103 `genTheory_avail_conj`; LiftAudit.lean:138
   `gateFlow_half_entries`) and O3-K (LiftAudit.lean:812 `derivedOI_qm_iff_layerFlowExecutable`, RouteB.lean:161
   `derivedOI_qm_iff_phaseFree`, MinimalRepertoire.lean:569 `oiPlusMin_iff_qm`).
4. **Design module.** `lean/OriginEnvelope.lean` (sha256 `182af483a29a76c7…`) built on `dev-origin/envelope` @
   `c3f7fbb2`, workflow run 38084486326 (`workflow_dispatch`): Mathlib bridge *Build* step success (3644 jobs), twelve
   `OriginEnvelope` declarations on `[propext, Classical.choice, Quot.sound]` (including `conj_dephase_of_submonomial`,
   `instAvail_substratum_dephase`, `instAvail_permClass_dephase`, `gateFlow_half_not_monomial`,
   `onesFixing_class_carries_mixer`), `lean-axioms` OK (5871 named results, no sorry); the release gate failed only on
   `claims`, `duplicate` (research-archive scans present at the branch base) and `lean-manuscript` (no census
   disposition for a design module) — `CI-RUNS.md`. Design evidence only: not certified.

## Findings by row

| row | thread label | audit |
|---|---|---|
| O1-T1, O1-T2 | CONDITIONAL ([W], no kernel check; one half CERTIFIED) | accepted; X1, X2 confirm the exact content |
| O1-T3 | CONDITIONAL ([W]; branch commutation [D]) | accepted; the [D] declarations present with standard axioms in run 38084486326 |
| O1-T4a–d | CONDITIONAL; T4b CERTIFIED as a composition of landed declarations, packaged statement [D] | accepted with the precision the row already states: the five landed declarations are CERTIFIED at L; the composition (√X in the generated theory of `onesClass`) and non-monomiality are [W] + [D], not a kernel theorem at L |
| O1-T5, O1-T6 | CONDITIONAL ([W] + [X]) | accepted; passivity and outcome determinism are written arguments with exhaustive instances |
| O1-T7a, b | CONDITIONAL on the model / on KB-D | accepted; KB-D recorded as an unsourced assumption |
| O2 (A12 … CLO, G1–G4) | FAILED (envelope / disguise) | accepted; the classification rule was fixed in the script header before run 1 |
| O2-G5, O2-KB | CONDITIONAL on KB-D; OPEN | accepted |
| O3-K | CERTIFIED | verified at L |
| O3-T1 | CONDITIONAL ([W]) | accepted; X4 and the thread's C1 instances |
| O3-T2 | CONDITIONAL | accepted; X4 |
| O3-T3, O3-T7 | CONDITIONAL ([X]; [W]+[L]); density at π/4 OPEN | accepted; X5 confirms the infinite-order certificate independently; run 1 VOID correctly kept |
| O3-T4 (Lemma P) | CONDITIONAL ([W]) | accepted; handed to the bridge in HO-5 |
| O3-T5 | OPEN | — |
| O3-T6, O3-D | CONDITIONAL; FAILED as a source | accepted |
| O4-I1, O4-J, O4-I2, O4-D | CONDITIONAL | accepted; X3 confirms the group identities; HO-5 issued |

**Label changes: none.** One precision note: the thread's "CERTIFIED as a composition" in O1-T4b is read as "its
components are certified"; the composed statement is [W] + [D]. The row says so itself.

## Recorded for the overview

- New assumptions: KB-D (knowledge-balance readout; unsourced at L, contradicted by the native Lüders readout and A5
  passivity); the stipulated phase continuum as the carrier of the one-parameter family (O3-T1).
- Eliminated alternatives: every stated-resource mechanism for a discrete coherent mixer (A1–A2 bijections, the link
  coupling, phase interventions, read-write coupling, ancilla readback and record writing, coarse-graining, time
  averaging, closure); the kernel's four passing constructions as sources (they import the coherence); the slogan
  "ones-fixing ⇒ no mixer" (monomiality is the invariant; `√X` is available in `onesClass`'s generated theory).
- Round-ready: nothing; the SRC question is open on the stated access.
