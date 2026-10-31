# Final consolidated audit, slice 3: Lean evidence, receipts, ledger and CI (main `55e3217b`)

Independent read-only check, run in a detached, non-shallow worktree that has since been removed.

## Local checks
| Command | Result |
|---|---|
| `tools/release_gate.py` | 21 of 22 steps pass. `lean-axioms` fails only because no `lake` is installed in this environment; the step passed in CI |
| `v3_verifier.py --self-test` / `--corpus` / `--receipts HEAD` | self-test OK; 140 corpus vectors exact; 52 receipts hold |
| `legacy_records_check.py HEAD` | 303 records in 75 closed namespaces, all intact |
| `coverage_check.py` | OK: 128 canonical statements |
| `lean_manuscript_census.py` | OK: 20 current families; every cited identifier and path resolves |
| `verification/lean/edge_rigidity_probe.py` | all checks pass (R7-RCH included) |
| `architecture_check.py` | 259 invariants, 0 violations |
| `c3_necessity_probe.py` | all checks pass |
| foundations probes `review3`, `review4`, `c4_backflow`, `fastbath`, `c2_mixing`, `process_dilation`, `memory`, `opglue`, `equivalence_recovery`, `lg_comb` | all exit 0 |

## Main CI
`verify` run 40499930462 at `55e3217b`: success, all 26 jobs, including the Lean kernel check and the Mathlib bridge with `lake`. The runs at `9d975c11`, `d66bb70e`, `1a60e06b` and `a5168789` are also green.

## Lean against the manuscripts
- 282 backticked identifier citations were scanned.
  - 262 are attributed to the module their paragraph names.
  - 19 sit in paragraphs that name another module. None of these is a misattribution.
  - `fiber_freedom` is a probe check name, not a Lean identifier.
- One misattribution: `GR.md:276` cites `typed_determined_iff` "in `OIBridge/TypedPositive.lean`", but it is in `TypedCompletion.lean`.
- R7-RCH holds: no manuscript cites `RecurrenceHorizon`.

| Identifier(s) | Lean statement | Sites | Verdict |
|---|---|---|---|
| `isPermMatrix_of_stochastic_inverse` | A, B row-stochastic and AB = 1 or BA = 1 ⇒ A is a permutation | Main :133, :139 | matches; the composition with P-divisibility is marked as on paper |
| `c3_necessity` family, `card_hidden_ge_two_pow_Istar` | bijection V×H ≃ V×H with an arbitrary joint law on (Hist, V, H) | Main :500–510, :608, :610 | matches; :510 lacks the joint-law caveat that :99 and :602 carry |
| `distinguishability_floor`, `capacity_floor`, `unavoidable_hidden_predictive_memory`, `pushforward_identity` | the same `Realization`, with no positivity hypothesis | Main :99, :602 | matches, with the stated caveat |
| `S_imp_D`, `finite_horizon_equivalence`, `exists_perm_extending` | (S) ↔ (D) ↔ (Q_fb), with (D) allowing a correlated initial law | Main :99, :516, :542–548, :608 | matches; both directions are named (§A.34) |
| `c4e_implies_pIndivisible`, `c4r_implies_pIndivisible` | collision-and-revival, or strict TV increase, ⇒ not P-divisible | not cited | Main :153 states the same as a sufficient condition |
| `driveQ_isContinuousPath` | `driveQ R 0 = id`; each `driveQ R t` is a bijective isometric *-homomorphism; ∀ x, Continuous (t ↦ driveQ R t x) | Main :268, GR :292 and mirrors | **overreach**, finding 1 |

## Coverage ledger
- `MAIN:L-accessible-backflow-from-readback` is absent from `LEDGER.json`, tools, guards, registries and the census. It appears only in the three historical audit notes.
- `MAIN:L-accessible-conditional-memory-from-readback` has fingerprint `d8219030a30e750e`, equal to the census value.
- All 128 fingerprints match the census.
- The SC-20 and SC-21 entries agree with the merged text, and no note uses "backflow" in the conditional-memory sense.
- 87 of 128 `line` fields are stale. This is informational only: the check matches entries by fingerprint.

## Receipts and frozen records
For both `a5168789..55e3217b` and `14804075..55e3217b`, the diff is empty for:
- `verification/receipts`, `verification/seals` and `verification/certificates`;
- all 304 paths of `legacy-records.json`.

Under `verification/`, only `coverage/LEDGER.json` and `lean/c3_necessity_probe.py` changed: the governed ID retirement and a wording change.

## New findings
1. **Medium: continuity overstated.** Eight sites call the drive a "norm-continuous path of (local) *-automorphisms": Main :268 and :584, GR :292, Explainer :381, FULL :509 and :5286, ch01 :165, and ch19 :126.
   - `driveQ_isContinuousPath` proves pointwise (strong) continuity only. The lattice is not assumed finite, and no locality lemma is cited.
   - Proposed fix: "a strongly continuous path of isometric *-automorphisms (norm-continuous at each quasilocal element)", dropping "local" unless a locality lemma is cited.
2. **Medium: ledger level above the manuscript.** `MAIN:T-unavoidable-hidden-predictive-memory` is recorded at K3 with an empty delta, but Main :99 and :602 say the time-t joint-law reading is not formalized. `MAIN:T-c3-necessity` has the same gap. Proposed fix: K2, with the delta stated. This predates #947–#955.
3. **Low.** The kernel citation at Main :510 lacks the joint-law caveat.
4. **Low: ledger understates.** `MAIN:C-per-process-capacity-bound` is recorded as P with "no Lean statement", but `card_hidden_ge_two_pow_Istar` proves m ≥ 2^{I*}.
5. **Low: stale "backflow" wording in code.** `C3Necessity.lean:30–31` and `:114`, and the C5 message in `c3_necessity_probe.py` at :262–264. These are comments and messages only; changing the Lean file needs a kernel rebuild.
6. **Low: three items.**
   - The GR :276 module misattribution above.
   - Backticked `fiber_freedom` at Main :616 reads like a Lean identifier.
   - Main :608 restates the M_t biconditional without the "vanishing criterion not formalized" note that Main :99 carries.
