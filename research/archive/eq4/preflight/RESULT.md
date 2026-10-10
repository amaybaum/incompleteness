# EQ4-F elaboration preflight — result (design only; not adopted)

## The objects

- **Commit** `f0d37906`:
  - signed;
  - single parent: certified main `bcbc516f`;
  - adds `OIBridge/FourCopyDefs.lean` (D), `OIBridge/FourCopyParity.lean` (P) and `OIBridge/FourCopyPackage.lean` (S),
    plus three import lines in `OIBridge.lean`.
- **Branch.** It is carried on the session's designated branch, `claude/network-tool-access-8jtdhm`, used as the
  disposable branch. There is no PR, no F and no ROADMAP or manuscript change.
- **Run.** One `workflow_dispatch` run of `verify.yml`: **37900638054**, head `f0d37906`, attempt 1.
- **Review before the run.** An independent source review found no compile or elaboration errors
  (`review_agent.md`). Its optional hedges were not applied.

## Verdict against the decision rule fixed before the run (EXPECTATIONS.md)

**Rule 1: the statements elaborate. Holds.**
- The Build step (`lake --rehash build`) completed with success: "Build completed successfully (3646 jobs)".
- No `error:` line occurs anywhere in the job log, apart from the gate step's final
  "Process completed with exit code 1".
- Module times: FourCopyDefs 2.4 s, FourCopyPackage 5.1 s, FourCopyParity 5.5 s, OIBridge 7.8 s.
- Phase times: cache get 87 s, build 20 s.

**Rule 2: the completed proofs check. Holds.** D and P built with no error.
- D: 2/2 axiom reports, each exactly `[propext, Classical.choice, Quot.sound]`: `actTEquiv`, `cnotTw`.
- P: 17/17 axiom reports, each exactly `[propext, Classical.choice, Quot.sound]`.
  - The 17 are: `ipW_comm`, `ipW_tens`, `transposeW_transposeW`, `ipW_dg_smul`, `phiW_tabMul`, `ipW_gateOf`,
    `gateOf_sharp`, `gate_sharp_mem_dualW`, `dualW_of_inv`, `incl_I`, `incl_II`, `incl_I_aligned`,
    `incl_II_aligned`, `cnotTw_prodState_xplus_z3`, `gateOf_prodState_xplus_z3`, `gateOf_prodState_neg`,
    `kt4_parity_aligned`.
  - No `sorryAx` and no further axiom appears in either layer.
- P's only diagnostics are two style warnings from `linter.unnecessarySeqFocus`, at FourCopyParity.lean:79:47
  (`ipW_dg`) and 102:29 (`ipW_cnot`): "Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice". Neither is an error.

**Rule 3: the statement layer's reports. As expected.**
- `target01` is free of `sorryAx`: `[propext, Classical.choice, Quot.sound]`.
- Five reports list `sorryAx`: `target02`, `fourCopyCoherent_of_kt4Cone`, `fourCopyCoherent_of_kt4`,
  `kt4_forward` and `kt4_forward_lt`, each `[propext, sorryAx, Classical.choice, Quot.sound]`.
- There are 48 `declaration uses 'sorry'` warnings, one per open obligation.

**Rule 4: the release gate. FAILED, at exactly the two predicted steps.**
- `lean-axioms` reports 10 problems.
  - The checker counts each `sorryAx` report twice: once as a line containing the token `sorryAx`, once as an axiom
    outside the permitted three. 5 reports × 2 = 10.
  - Reproduced locally by running `tools/lean_axiom_check.py`'s `analyse` on the captured FourCopy output: 10
    problems, and all 25 declared prints were reported.
  - Any further problem (a silent print, a nonzero lake exit, a duplicated line) would raise the count above 10.
- `lean-manuscript` reports 3 problems: the three modules are not registered in the census.
- The other 19 steps pass, including legacy-records (303 records), v3-self-test, v3-corpus (140 vectors) and
  v3-receipts (42 hold).
- The Mathlib bridge job's conclusion is therefore `failure`. **This run is not green under any reading.**

**Rule 5: the other jobs.**
- Lean kernel check: success.
- All 30 numerical-probe jobs, including the dispatch-only A42 shards and the aggregate `probes` job: success.
- Totals: 32 jobs, 31 success, 1 failure (Mathlib bridge, at the release gate). The workflow's conclusion is
  `failure`, as predicted. Run window 07:43:15–08:00:07Z.

## What the run establishes, and what it does not

**Established:**
- Every statement of the package elaborates against Mathlib v4.33.0 and the certified base. That includes the
  minimal headline `kt4_forward` over COMP-1 `PreComposite`s, with no local-tomography field and with `TokenCoherent`
  explicit, and the convenience form `kt4_forward_lt` over `Composite`s.
- The completed layer's proofs check in the kernel, with standard axioms only: Lemma P, the gate-supplied effects, the
  inverse-gate dual action and inclusions (I) and (II).
- The elaborated term `kt4_forward_lt := kt4_forward … H.toKT4` derives the LT form from the minimal form by
  forgetting `lt`. Its `sorryAx` comes only through `kt4_forward`.

**Not established:**
- KT(4) ⇒ IE₁. Lemma B1 (`fourCopyCoherent_of_kt4`), Theorem C (`kt4_general`) and the rest of the heavy layer are
  open: 48 obligations.
- That any hypothesis is used inside those open proofs.
- That any hypothesis is necessary.

## Counts

- The design file had 56 `sorry` placeholders. The earlier "57" counted the word in its header.
- The preflight has D 0, P 0, S 48, so 56 − 8 = 48. The eight removed from the open set are:
  - five completed: `actTEquiv.map_add'`, `actTEquiv.map_smul'`, `ipW_gateOf`, `tens_sharpVec`,
    `kt4_parity_aligned`;
  - one made a plain definition: `flatW`;
  - two dropped as unused: `smul_mem_dualW`, `prodEff_eq_zero_of_vanish`.
