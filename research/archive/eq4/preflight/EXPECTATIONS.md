# EQ4-F elaboration preflight — expectations fixed before the run

Owner authorization: one CI run, design-only, disposable branch from certified main bcbc516f; no F, PR,
merge, ROADMAP or manuscript edits; report failures before requesting further runs; an expected failure
of the aggregate release gate is not a green run.

## Objects
- Branch `claude/eq4f-preflight` = bcbc516f + one commit adding
  `OIBridge/FourCopyDefs.lean` (D), `OIBridge/FourCopyParity.lean` (P), `OIBridge/FourCopyPackage.lean` (S)
  and three import lines in `OIBridge.lean`.
- Module graph: D imports K2Guard; P imports D only; S imports D (+ MonoidalCompletion and four Mathlib
  modules), not P. A failure in P cannot block S's elaboration, and vice versa.

## Exact pre-checks (scratchpad, exact arithmetic; not kernel evidence)
- precheck_parity.py 22/22 PREFLIGHT-PRECHECK-EXACT (every equation P proves, kernel cnot tables).
- precheck_heavy.py 10/10 PREFLIGHT-HEAVY-EXACT (convention-sensitive S statements; H6c countercontrol).
- precheck_chart.py 5/5 PREFLIGHT-CHART-EXACT (chartR_gateOf ingredients; CC countercontrol).

## Decision rule for the report (fixed now)
1. "Statements elaborate" iff the Build step's `lake --rehash build` exits 0. Any `error:` line in D, P or S
   is a failure, reported verbatim with file:line.
2. "Completed proofs check" iff D and P build with no error AND every `#print axioms` report of a D/P
   declaration lists only axioms within {propext, Classical.choice, Quot.sound}; any `sorryAx` in a D/P
   report is a failure.
3. S's reports for target02, fourCopyCoherent_of_kt4Cone, fourCopyCoherent_of_kt4, kt4_forward,
   kt4_forward_lt are EXPECTED to list `sorryAx` (they compose open obligations). target01's report is
   expected free of `sorryAx`.
4. Release gate: EXPECTED FAILED with exactly lean-axioms (sorryAx from S's reports) and lean-manuscript
   (three UNCLASSIFIED modules). Any other failing step is an unexpected failure and is reported as such.
   The bridge job and the aggregate workflow conclusion are therefore expected `failure`; this is not
   reported as green under any reading.
5. Kernel and probe jobs: expected success (nothing they read changed).
6. If Build fails, the Release gate step does not run; the report then names the build errors and says the
   gate was not evaluated.

## Counts
- Design (FourCopyIE1.lean, UNBUILT): 56 `sorry` placeholders (an earlier "57" counted the word in the
  file header).
- Preflight: D 0, P 0, S 48 (each the whole proof of its theorem).
- Completed relative to the design: actTEquiv.map_add', actTEquiv.map_smul', ipW_gateOf, tens_sharpVec,
  kt4_parity_aligned (5); flatW is a plain function (1); dropped as unused: smul_mem_dualW,
  prodEff_eq_zero_of_vanish (2). 56 - 8 = 48.

## Addendum (before the push; decision rule unchanged)
- Branch: the preflight commit is carried on the session's designated branch
  `claude/network-tool-access-8jtdhm`, reset to certified main bcbc516f (its prior local tip 47d2288b is an
  ancestor of main; nothing on it was outside main). The name `claude/eq4f-preflight` above is superseded;
  no other object, count or rule above changes.
