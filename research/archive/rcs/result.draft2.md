# Reconstruction round RELC-SELECT-1 — DIM-1's dimension selector without the target relation: parity from the control relation, the selector over the frame, both positivity clauses and the control relation, and a countermodel for each audited clause: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #805.

- **`D`** — `e2426ba4109dcd719d518aefbd3c417b7c6fdc5b`, the head of `main` after round ODD-CHAR-1 landed, certified by
  push run 37676443882.
- **`F`** — `@@F@@`, single parent `D`; `delta(D, F)` is the preregistration alone, blob `@@PREREG@@`. Its exact-head
  `workflow_dispatch` run @@FRUN@@ is its `check-run` attestation; the owner designated `F`. That run attests the control
  plane only.
- **Shape** — non-sealing; stages C1 (`@@C1@@`, `controls.py` blob `@@CONTROLS@@`), S1 (`@@S1@@`, the four modules, the
  four import lines and the census family) and this note (S2).

**Outcome:** `RELC-SELECT-1-READ`

**Q-PAR: RELC-PARITY-PROVED.** With `IsNot (eball d) z N` and the gate a linear equivalence of the joint carrier, the
control relation alone gives equal dimensions of the two eigenspaces of the homogenized NOT
(`finrank_plus_eq_finrank_minus_relC`), and so `¬ Even d` (`not_even_of_relC`). Through `toOp`, the control relation
makes the gate intertwine left composition with the homogenized NOT `H` and two-sided composition with it; the `±1`
eigenspaces of the first have dimensions `(d + 1)P` and `(d + 1)Q`, those of the second at most `P² + Q²` and `2PQ`, and
`P + Q = d + 1` with `Q ≥ 1` gives `P = Q`. The target relation, the frame and positivity are not read.

**Q-SEL: CTRL-SELECTOR-PROVED.** `CtrlGate` — `NativeGate`'s frame, two positivity clauses and control relation,
without its target relation — gives `d = 1 ∨ d = 3` with `IsNot (eball d) z N` (`dim_of_ctrlGate`) and `d = 3` with
the entangling clause as well (`three_of_ctrlGate`). The proof is DIM-1's block reduction restated over `CtrlGate` line
for line, except its one target-relation step, replaced by `actT_slice_ctrl`, and its parity step, replaced by Q-PAR's
theorem. Both values occur: DIM-1's `cnot1` at `d = 1` (`nativeGate_cnot1`, with `isNot_neg1`) and `cnot` at `d = 3`
(`nativeGate_cnot`, with `isNot_nflip`) are native gates and so, through `ctrlGate_of_nativeGate`, control gates. That
`IsNot` and `CtrlGate` give exactly `d = 1 ∨ d = 3` is these landed statements composed with `dim_of_ctrlGate`; no
standalone theorem of the round states it. The entangling clause excludes `d = 1` through `not_entangling_one_ctrl`, which
reads the frame alone.

**Q-POS: POSITIVITY-SEPARATION-PROVED.** At `d = 5`, with PARITY-NOT-1's `n5` and `z5`, the squeezed gate `gSq` has
`IsNot`, the frame, `GateRel n5 gSq` and forward positivity, and fails inverse positivity through the exact value `−1/2`
(`gSq_sep`); its inverse has `IsNot`, the frame, `GateRel n5 gSq.symm` and inverse positivity, and fails forward
positivity (`gSqInv_sep`). Neither is a native gate. Since `5` is neither `1` nor `3`, neither implication to
`d = 1 ∨ d = 3` with one positivity clause removed holds; that failure is the two witness theorems beside
`5 ∉ {1, 3}`, and no standalone theorem of the round states it. The control relation of `gSq.symm` comes from `GateRel n5 gSq`
through `gateRel_symm`, whose transfer of the control relation (`relC_symm_of_relT`) reads the target relation of
`gSq` as well.

**Q-REL: RELT-NOT-DIMENSION-SELECTING-PROVED.** At `d = 5`, the witness NOT `nC5` with the axis `z5` and NB-1's J/K map
`gC5` have `IsNot`, the frame, the target relation and both positivity clauses, and fail the control relation at the
entry `(4, 4)` of the image of `entW 3 3`, where its two sides are `1` and `−1` (`c5_sep`); so `IsNot`, the frame, both
positivity clauses and the target relation do not give `d = 1 ∨ d = 3` (`relT_not_dimension_selecting`). `nC5` is a
witness construction for this countermodel; it is not PARITY-NOT-1's `n5`, which the squeezed witnesses use. Its
homogenized map has sign `+1` at two homogeneous indices and `−1` at four, where `n5` has three of each, and the
balanced case is not decided.

The four cells are read by separate rules and none reads another's outcome. The earned reading:

> The target relation relT is unnecessary for the dimension selector. Under IsNot, the frame, both positivity clauses
> and the control relation relC, the dimension is 1 or 3. The control relation alone already forces odd dimension.
> Neither positivity clause can be dropped individually: explicit d = 5 gates satisfy all remaining clauses while
> violating one positivity direction.
>
> This round does not establish that the frame is necessary or unnecessary, and therefore does not claim a globally
> minimal hypothesis set. It establishes minimality only with respect to the audited relation and positivity clauses.

The non-inference rule:

> CtrlGate is the hypothesis of the dimension selector only. This round does not show that relT is redundant in
> NativeGate or in GateRel, that relT follows from the remaining clauses, or that every CtrlGate is a NativeGate:
> NativeGate, GateRel and every landed statement over them are unchanged, and relT remains a field of both. It does
> not show that the control relation of a gate gives the control relation of its inverse: the transfer used for the
> inverse of the squeezed gate, relC_symm_of_relT, reads the target relation as well. Its countermodel for the control
> relation uses the witness NOT nC5, whose homogenized map has two indices of sign +1 and four of sign −1; it does not
> decide whether the target relation, the frame and two-sided positivity select the dimension for a NOT whose two
> homogenized eigenspaces have equal dimension, such as PARITY-NOT-1's n5. The squeezed gate, its inverse, nC5 and gC5
> are mathematical countermodels for the clauses they separate; they are not postulates, adopted models, or a NOT or a
> gate of a physical theory, and the orthogonal complex structures J and K in the proof of gC5's positivity are tools
> of that proof. The selector concerns two copies of the Euclidean ball under the stated hypotheses; the round does
> not claim that OI selects a dimension, adopts no premise, and makes no manuscript claim and no ROADMAP claim.

***

## Execution facts

- **C1** — `@@C1@@`, single parent `F`, adds `controls.py`, blob `@@CONTROLS@@`, the frozen blob.
- **S1** — `@@S1@@`, single parent C1, adds the four modules, the four import lines and the census family.
- **The cells** — `controls.py verdict` at S1 prints `RELC-PARITY-PROVED`, `CTRL-SELECTOR-PROVED`,
  `POSITIVITY-SEPARATION-PROVED` and `RELT-NOT-DIMENSION-SELECTING-PROVED`.
- **Count facts** — the modules carry 34 `#print axioms` lines; the release gate's `lean-axioms` step reports 5860 named
  results at S1 and 5826 at `D`.
- **Linter warnings** — the parity, squeeze and C5 modules carry none. The block module carries DIM-1's seven, with the
  lines it copies: `RelcSelectBlock.lean` 606:23, 606:52, 608:10, 622:25, 622:54 and 623:70 (unused `simp` arguments)
  and 623:93 (an unnecessary `<;>`), inside `blockData_of_orthonormal_ctrl`. Those four lines are byte-identical to
  `CompositeDimension.lean` lines 2591, 2593, 2607 and 2608 at `D`, inside DIM-1's `blockData_of_orthonormal`, where
  DIM-1's exact-head run 37299337191 reports the same seven warnings at the same columns.
